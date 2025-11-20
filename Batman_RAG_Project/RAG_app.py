import os
import logging
import warnings

from transformers import logging as transformers_logging
from dotenv import load_dotenv
import openai

from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer, CrossEncoder
import numpy as np
import faiss


# -----------------------------
# 1. Load environment & suppress noisy logs
# -----------------------------
load_dotenv()

# Suppress LangChain / HF / general warnings
logging.getLogger("langchain_text_splitters").setLevel(logging.ERROR)
transformers_logging.set_verbosity_error()
warnings.filterwarnings("ignore")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Make sure your .env file has OPENAI_API_KEY set.")

openai.api_key = api_key


# -----------------------------
# 2. Read pre-scraped Batman document
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(BASE_DIR, "Selected_Document.txt")

if not os.path.exists(DOC_PATH):
    raise FileNotFoundError(
        f"Selected_Document.txt not found at {DOC_PATH}. "
        "Run text_extractor.py first to create it."
    )

with open(DOC_PATH, "r", encoding="utf-8") as file:
    text = file.read()


# -----------------------------
# 3. Parameters
# -----------------------------
chunk_size = 500
chunk_overlap = 50  
model_name = "sentence-transformers/all-distilroberta-v1"

top_k = 20
cross_encoder_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
top_m = 8


# -----------------------------
# 4. Split into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
)

chunks = text_splitter.split_text(text)


# -----------------------------
# 5. Embed & build FAISS index
# -----------------------------
embedder = SentenceTransformer(model_name)
embeddings = embedder.encode(chunks, show_progress_bar=False)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(embeddings)


# -----------------------------
# 6. Retrieval (bi-encoder + FAISS)
# -----------------------------
def retrieve_chunks(question: str, k: int = top_k):
    """
    Encode the question and search the FAISS index for top k similar chunks.
    """
    q_vec = embedder.encode([question], show_progress_bar=False)
    q_arr = np.array(q_vec).astype("float32")
    distances, I = faiss_index.search(q_arr, k)
    return [chunks[i] for i in I[0]]


# -----------------------------
# 7. Re-ranking (cross-encoder)
# -----------------------------
reranker = CrossEncoder(cross_encoder_name)


def _dedupe_preserve_order(items):
    seen = set()
    out = []
    for it in items:
        key = " ".join(it.split())  # normalize whitespace
        if key not in seen:
            seen.add(key)
            out.append(it)
    return out


def rerank_chunks(question: str, candidate_chunks: list[str], m: int = top_m) -> list[str]:
    """
    Score (question, chunk) pairs with a cross-encoder and return the top-m chunks.
    """
    if not candidate_chunks:
        return []

    pairs = [(question, c) for c in candidate_chunks]
    scores = reranker.predict(pairs)  # higher = more relevant
    ranked = sorted(zip(candidate_chunks, scores), key=lambda x: float(x[1]), reverse=True)
    best = [c for c, _ in ranked[:m]]
    return _dedupe_preserve_order(best)


# -----------------------------
# 8. Q&A with ChatGPT
# -----------------------------
def answer_question(question: str) -> str:
    """
    Retrieves candidate chunks, re-ranks them, and uses OpenAI's Chat Completions API to answer.
    """
    # Retrieve candidate chunks via FAISS
    candidates = retrieve_chunks(question)

    # Re-rank to final context
    relevant_chunks = rerank_chunks(question, candidates, m=top_m)

    # Combine chunks into a single context string separated by double newlines
    context = "\n\n".join(relevant_chunks)

    system_prompt = (
        "You are a knowledgeable assistant that answers questions based on the provided context. "
        "If the answer is not in the context, say you don’t know."
    )

    user_prompt = f"""Context:
{context}

Question: {question}

Answer:
"""

    resp = openai.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_completion_tokens=500,
    )

    return resp.choices[0].message.content.strip()


# -----------------------------
# 9. Interactive loop
# -----------------------------
if __name__ == "__main__":
    print("Enter 'exit' or 'quit' to end.")
    while True:
        question = input("Your question: ")
        if question.lower() in ("exit", "quit"):
            break
        print("Answer:", answer_question(question))
