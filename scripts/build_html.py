from string import Template
import markdown
from pathlib import Path
import subprocess

MD_INPUT_DIR = "./src/markdown"
TEMPLATES_INPUT_DIR = "./src/templates"
OUTPUT_DIR = "./course"

base_template = Path(TEMPLATES_INPUT_DIR, "base.html").read_text()


def convert_markdown_to_html(md_path: Path, output_dir: Path, style: str):
    html_file = Path(output_dir, md_path.parent.name, md_path.stem + ".html")
    html_file.parent.mkdir(exist_ok=True)

    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    html = markdown.markdown(
        text, extensions=["pymdownx.superfences", "codehilite", "tables"]
    )
    tpl = Template(base_template)
    html = tpl.substitute(title=md_path.stem, body=html, head=f"<style>{style}</style>")

    Path(html_file).write_text(html, encoding="utf-8")

    return html_file


def generate_codehilite_css():
    output = subprocess.run(
        ["pygmentize", "-S", "default", "-f", "html", "-a", ".highlight"],
        check=True,
        capture_output=True,
    )

    return output.stdout.decode("utf-8")


def generate_index_html(files: list[Path], output_dir: Path, style: str):
    print(f"Generating index file...")
    links = "\n".join(
        f'<li><a href="{file.parent.name}/{file.name}">{file.name}</a></li>'
        for file in files
    )
    tpl = Template(base_template)
    html = tpl.substitute(
        title="Index of Documents",
        body=f"<h1>Index</h1><ul>{links}</ul>",
        head=f"<style>{style}</style>",
    )

    Path(output_dir, "index.html").write_text(html, encoding="utf-8")


def main():
    input_path = Path(MD_INPUT_DIR)
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(exist_ok=True)
    base_css = generate_codehilite_css()

    html_files = []

    for md_file in sorted(input_path.glob("**/*.md")):
        print(f"Converting {md_file.name}...")
        html_file = convert_markdown_to_html(md_file, output_path, base_css)
        html_files.append(html_file)

    generate_index_html(html_files, output_path, base_css)
    print(f"\nDone. HTML files written to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
