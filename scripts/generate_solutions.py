import random
import re
import time
from pathlib import Path
from google import genai
from dotenv import load_dotenv
from google.genai import errors

# === Configuration ===
CHALLENGES_DIR = Path("src/markdown")
SOLUTIONS_DIR = Path("solutions")
SOLUTIONS_DIR.mkdir(exist_ok=True, parents=True)
MODEL="gemini-2.5-flash"

load_dotenv()
client = genai.Client()

def generate_solution(challenge_text: str) -> str:
    prompt = (
        "You are an expert Python programmer. "
        "Read the challenge below and provide a solution."
        "Use any sample code from the challenge if possible. "
        "Return code solutions in fenced code blocks, non-code solutions as a numbered list. "
        "If the challenge cannot be solved, explain why. "
        "Do not include extra text such as reasoning, explanations or similar. "
        "The response format should be markdown."
        "\n\nChallenge:\n" + challenge_text
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
                raise Exception("Empty respones from API")

            return response.text
        except errors.APIError as e:
            if e.message and "429" in e.message or e.status and "429" in e.status:
                # Calculate exponential backoff with jitter
                delay = min(initial_delay * (2 ** attempt), max_delay) + random.uniform(0, 1)
                print(f"Attempt {attempt + 1}/{max_retries}: Got 429 error. Retrying in {delay:.2f} seconds...")
                time.sleep(delay)
                attempt += 1
            else:
                # Re-raise for other errors
                print(f"Caught a non-429 error: {e}")
                raise
      

# === Split markdown into second-level headings ===
def split_challenges(md_text: str) -> list[tuple[str, str]]:
    """
    Returns a list of tuples: (heading_text, challenge_content)
    Splits on ## heading lines.
    """
    pattern = re.compile(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", re.DOTALL | re.MULTILINE)
    return [(m[0].strip(), m[1].strip()) for m in pattern.findall(md_text)]

# === Main script ===
def main():
    for md_file in CHALLENGES_DIR.glob("**/*Challenge.md"):
        solution_file = Path(md_file.parent, f"{md_file.stem} Solution.md")
        if solution_file.exists():
            print(f"Skipping {md_file.name}, solution already exists.")
            continue

        print(f"Processing {md_file.name}...")
        md_text = md_file.read_text(encoding="utf-8")
        challenges = split_challenges(md_text)

        all_solutions = []
        for heading, content in challenges:
            print(f"Generating solution for '{heading}'...")

            try:
                solution_markdown = generate_solution(content)
            except Exception as e:
                solution_markdown = f"Failed to generate solution: {e}"

            # Wrap solution in pymdownx.details block with indentation
            wrapped_solution = f"??? solution \"{heading}\"\n"
            indented_solution = "\n".join(f"    {line}" if line.strip() else "" for line in solution_markdown.splitlines())
            wrapped_solution += indented_solution

            all_solutions.append(wrapped_solution)

        # Write combined solution file    
        solution_file.write_text("\n\n".join(all_solutions), encoding="utf-8")
        print(f"Saved solutions to {solution_file.name}")


if __name__ == "__main__":
    main()
