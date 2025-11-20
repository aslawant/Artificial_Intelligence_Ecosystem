import os
import requests
from bs4 import BeautifulSoup

# Save Selected_Document.txt next to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "Selected_Document.txt")


def fetch_and_extract(url: str) -> str:
    """
    Fetch the given URL, extract the main Wikipedia article text,
    and save it to Selected_Document.txt (UTF-8).
    """
    try:
        # More realistic User-Agent so Wikipedia is happy
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=15)
        print("HTTP status:", response.status_code)

        if response.status_code != 200:
            print(f"Failed to retrieve the page. HTTP Status Code: {response.status_code}")
            return ""

        soup = BeautifulSoup(response.text, "html.parser")

        # Try the standard Wikipedia content div first
        content_div = soup.find("div", class_="mw-parser-output")
        paragraphs = []

        if content_div:
            paragraphs = content_div.find_all("p")
            print("Paragraphs found in mw-parser-output:", len(paragraphs))

        # 🔁 Fallback: if that found nothing, use ALL <p> tags on the page
        if not paragraphs:
            print("Falling back to all <p> tags on the page.")
            paragraphs = soup.find_all("p")
            print("Paragraphs found in whole page:", len(paragraphs))

        # Collect non-empty paragraph text
        extracted_text = "\n\n".join(
            p.get_text(strip=True)
            for p in paragraphs
            if p.get_text(strip=True)
        )

        print("Length of extracted text:", len(extracted_text))

        # Write (even if short) so you can inspect it
        with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
            file.write(extracted_text)

        if not extracted_text.strip():
            print("WARNING: No non-empty paragraph text extracted.")
            return ""

        print(f"Page successfully retrieved and content saved to '{OUTPUT_PATH}'.")
        return extracted_text

    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return ""


def main():
    # Hardcoded Batman URL (per assignment instructions)
    url = "https://en.wikipedia.org/wiki/Batman"
    fetch_and_extract(url)


if __name__ == "__main__":
    main()
