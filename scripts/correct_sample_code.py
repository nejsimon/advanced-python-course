import random
import time
from pathlib import Path
from google import genai
from dotenv import load_dotenv
from google.genai import errors

# === Configuration ===
CHALLENGES_DIR = Path("src/markdown")
MODEL = "gemini-2.5-flash"

load_dotenv()
client = genai.Client()

def correct_sample_code(challenge_text: str) -> str:
    """
    Send a challenge markdown file to Gemini to correct / insert sample code.
    Returns the full corrected markdown document.
    """
    prompt = (
        "Your job is to create or modify sample code from programming challenges. "
        "Follow these instructions strictly:\n"
        "1. If a sample code block already exists, verify that it is appropriate for the challenge and change as needed.\n"
        "2. If a code block exists but solves the challenge, replace it with sample code only (e.g., stubs, empty functions, etc.).\n"
        "3. If no sample code exists, add suitable sample code if possible.\n"
        "4. All sample code must run, pass lint, and typecheck. If not possible, comment out problematic code as a last resort.\n"
        "5. Non-Python sample code can be included in a separate code block, as comments in Python, or integrated (e.g. json.loads(), yaml.loads()).\n"
        "6. It is acceptable to output no sample code when appropriate.\n"
        "7. Response format must be Markdown and must include the complete challenge definition as provided.\n\n"
        "Challenge:\n"
        + challenge_text
    )

    attempt = 0
    initial_delay = 5
    max_retries = 10
    max_delay = 60

    while True:
        try:
            response = client.models.generate_content(
                model=f"models/{MODEL}",
                contents=prompt,
            )

            if not response.text:
                raise Exception("Empty response from API")

            return response.text

        except errors.APIError as e:
            if (e.message and "429" in e.message) or (e.status and "429" in e.status):
                delay = min(initial_delay * (2 ** attempt), max_delay) + random.uniform(0, 1)
                print(f"Attempt {attempt + 1}/{max_retries}: Got 429 error. Retrying in {delay:.2f} seconds...")
                time.sleep(delay)
                attempt += 1
                if attempt >= max_retries:
                    raise Exception("Max retries reached for 429 errors")
            else:
                print(f"Caught a non-429 error: {e}")
                raise

def main():
    for md_file in CHALLENGES_DIR.glob("**/*Challenge.md"):
        print(f"Processing {md_file.name}...")

        original_text = md_file.read_text(encoding="utf-8")

        try:
            corrected_text = correct_sample_code(original_text)
        except Exception as e:
            print(f"Failed to correct {md_file.name}: {e}")
            continue

        # Replace the challenge file with the corrected version
        md_file.write_text(corrected_text, encoding="utf-8")
        print(f"Updated {md_file.name}")

if __name__ == "__main__":
    main()
