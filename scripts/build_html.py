import markdown
from pathlib import Path
import subprocess

INPUT_DIR = "./src"
OUTPUT_DIR = "./course"


def convert_markdown_to_html(md_path: Path, output_dir: Path):
    html_file = Path(output_dir, md_path.parent.name, md_path.stem + ".html")
    html_file.parent.mkdir(exist_ok=True)

    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    html = markdown.markdown(text, extensions=["pymdownx.superfences", "codehilite"])
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(
            f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{md_path.stem}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
{html}
</body>
</html>
"""
        )
    return html_file


def generate_css(output_dir: Path):
    print(f"Generating css file...")
    output_css = Path(output_dir, "style.css")

    # Ensure output folder exists
    output_css.parent.mkdir(exist_ok=True)

    # Run pygmentize
    subprocess.run(
        ["pygmentize", "-S", "default", "-f", "html", "-a", ".highlight"],
        stdout=output_css.open("w"),
        check=True,
    )


def generate_index_html(files: list[Path], output_dir: Path):
    print(f"Generating index file...")
    links = "\n".join(
        f'<li><a href="{file.parent.name}/{file.name}">{file.name}</a></li>'
        for file in files
    )
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index of Documents</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Index</h1>
    <ul>
        {links}
    </ul>
</body>
</html>
"""
    with open(output_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(index_html)


def main():
    input_path = Path(INPUT_DIR)
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(exist_ok=True)

    html_files = []

    for md_file in sorted(input_path.glob("**/*.md")):
        print(f"Converting {md_file.name}...")
        html_file = convert_markdown_to_html(md_file, output_path)
        html_files.append(html_file)

    generate_css(output_path)
    generate_index_html(html_files, output_path)
    print(f"\nDone. HTML files written to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
