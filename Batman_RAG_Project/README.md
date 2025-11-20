## Description of the document you selected

I selected the Wikipedia article about Batman. The article covers Batman’s origins, his creators (Bob Kane and Bill Finger), his debut in *Detective Comics* #27, and key elements of his character such as his secret identity, Gotham City, allies, enemies, and cultural impact.

---

## 5 important questions and answers

### 1. How does chunk_size affect retrieval quality?

**Answer:**  
Smaller chunk sizes create more—but shorter—chunks, which improves precision for specific questions. Larger chunks include more context and produce smoother answers but give FAISS fewer options, which can reduce fine-grained accuracy.

---

### 2. Why is chunk_overlap needed?

**Answer:**  
Overlap prevents important sentences near chunk boundaries from getting cut in half. Without it, meaningful information could end up split across chunks and weaken embedding quality. More overlap increases recall but also increases redundancy.

---

### 3. Why use a bi-encoder for retrieval and a cross-encoder for re-ranking?

**Answer:**  
The bi-encoder (SentenceTransformer) creates embeddings quickly and lets FAISS do fast similarity search. The cross-encoder (ms-marco-MiniLM-L-6-v2) re-scores each question-chunk pair using a full attention model, which captures nuance the bi-encoder misses. This combination balances speed and accuracy.

---

### 4. How does FAISS decide which chunks are relevant?

**Answer:**  
FAISS compares vector distances between the question embedding and every chunk embedding in the index using L2 similarity. The closest vectors are returned as the top-k most relevant chunks. FAISS makes this process extremely fast even with thousands of embeddings.

---

### 5. Why does embedding dimensionality matter?

**Answer:**  
My embedding model produces 768-dimensional vectors. Higher dimensions capture more semantic meaning, which improves search quality. But more dimensions also mean more memory usage and slower FAISS operations. The chosen model provides a good balance between rich embeddings and efficient retrieval.

---

## 3 Questions and Answer Quality

**Question:** Who is Batman?  
**Answer:** Batman is a fictional superhero who fights crime as a masked vigilante in Gotham City. His secret identity is Bruce Wayne, a wealthy industrialist.

**Question:** Who created Batman?  
**Answer:** Batman was created by artist Bob Kane and writer Bill Finger. His debut was in *Detective Comics* #27 in 1939.

**Question:** When did Batman first appear?  
**Answer:** Batman first appeared in *Detective Comics* #27 in 1939.

The quality of these answers was very good because the Batman Wikipedia article is detailed and contains direct information about his identity, creators, and publication history. The RAG system consistently found the correct chunks and answered accurately.

To test chunk-size behavior, I used the question:  
**“Tell me about Batman.”**  
This ensured the retrieved content came from different chunking strategies for comparison.

---

**Chunk size = 800**  
**Overlap = 100**

**Answer:**  
Batman is a fictional superhero created by Bob Kane and Bill Finger who first appeared in *Detective Comics* #27 in 1939. His secret identity is Bruce Wayne, a wealthy Gotham City industrialist who fights crime as a masked vigilante and is supported by allies such as Robin and Alfred. The larger chunk size provided more context, resulting in longer and more descriptive answers.

---

**Chunk size = 200**  
**Chunk overlap = 50**

**Answer:**  
Batman is a fictional superhero who first appeared in *Detective Comics* #27 in 1939. He protects Gotham City as a masked vigilante, and his secret identity is Bruce Wayne. The smaller chunks produced shorter, more direct answers with less narrative detail.

---

**Chunk size = 100**  
**Chunk overlap = 50**

**Answer:**  
Batman is a fictional superhero with the secret identity of Bruce Wayne. With very small chunks, the answer became noticeably less detailed because each chunk contains less context.

---

In general, the smaller the chunk size and the smaller the overlap, the shorter and less detailed the answers become.
