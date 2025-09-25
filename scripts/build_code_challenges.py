from pathlib import Path
import re

INPUT_FOLDER = "./src/markdown"
OUTPUT_FOLDER = "./challenges"


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

        code = ""
        if len(parts) > 1:
            code_match = re.search(r"(.*?)```", parts[1], re.DOTALL)
            if code_match:
                code = code_match.group(1).strip()

        description = body.replace(f"\n```python\n{code}\n```\n", "").strip()
        results.append({"title": title, "description": description, "code": code})

    return header, results


def convert_to_python_file(md_file, py_path):
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    header, challenges = extract_challenges_from_markdown(content)

    with open(py_path, "w", encoding="utf-8") as f:
        # Write the file header as comments
        for line in header.strip().splitlines():
            f.write(f"# {line.strip()}\n")
        f.write("\n")

        for challenge in challenges:
            f.write(f"# {challenge['title']}\n")
            f.write("\n")
            for line in challenge["description"].splitlines():
                f.write(f"# {line.strip()}\n")
            f.write("\n")
            f.write(f"print(\"{challenge['title']}\")\n")
            f.write("\n")
            f.write("# Write your solution below ...\n")
            if challenge["code"]:
                f.write(f"{challenge['code']}\n")
            f.write("\n# --- End of Challenge ---\n\n")


def main():
    input_folder = Path(INPUT_FOLDER)
    output_folder = Path(OUTPUT_FOLDER)
    output_folder.mkdir(exist_ok=True)
    filename_suffix = " Challenge.md"

    for md_file in input_folder.glob("**/*.md"):
        if md_file.name.endswith(filename_suffix):
            base_name = md_file.name[: -len(filename_suffix)]
            output_file_path = Path(
                output_folder, md_file.parent.name, f"{base_name}.py"
            )
            output_file_path.parent.mkdir(exist_ok=True)

            convert_to_python_file(md_file, output_file_path)
            print(f"Converted: {md_file.name} -> {base_name}.py")


if __name__ == "__main__":
    main()
