import os
import re

INPUT_FOLDER = "../docs"
OUTPUT_FOLDER = "../excercises"


def extract_challenges_from_markdown(content):
    # Split by challenge sections
    challenges = re.split(r"^## (Challenge \d+: .+)", content, flags=re.MULTILINE)
    header = challenges[0].strip()
    results = []

    for i in range(1, len(challenges), 2):
        title = challenges[i].strip()
        body = challenges[i + 1].strip()

        # Extract everything before the code block as description
        parts = re.split(r"```python", body, maxsplit=1)
        description = parts[0].strip()
        code = ""
        if len(parts) > 1:
            code_match = re.search(r"(.*?)```", parts[1], re.DOTALL)
            if code_match:
                code = code_match.group(1).strip()

        results.append({"title": title, "description": description, "code": code})

    return header, results


def convert_to_python_file(md_path, py_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    header, challenges = extract_challenges_from_markdown(content)

    with open(py_path, "w", encoding="utf-8") as f:
        # Write the file header as comments
        for line in header.strip().splitlines():
            f.write(f"# {line.strip()}\n")
        f.write("\n")

        for challenge in challenges:
            f.write(f"# {challenge['title']}\n")
            for line in challenge["description"].splitlines():
                f.write(f"# {line.strip()}\n")
            f.write("\n")
            f.write("# Add your solution below ...\n")
            if challenge["code"]:
                f.write(f"{challenge['code']}\n")
            f.write("\n# --- End of Challenge ---\n\n")


def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.endswith("-challenge.md"):
            base_name = filename[: -len("-challenge.md")]
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.py")

            convert_to_python_file(input_path, output_path)
            print(f"Converted: {filename} -> {base_name}.py")


if __name__ == "__main__":
    main()
