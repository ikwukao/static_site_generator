from pathlib import Path

from markdown_parser import markdown_to_html_node


def extract_title(markdown: str) -> str:
    """
    Extract the H1 title from a Markdown document.
    """
    for line in markdown.splitlines():
        line = line.strip()

        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("Markdown document does not contain an H1 heading.")


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} "
        f"to {dest_path} using {template_path}"
    )

    markdown = Path(from_path).read_text(encoding="utf-8")

    template = Path(template_path).read_text(encoding="utf-8")

    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    destination = Path(dest_path)

    destination.parent.mkdir(parents=True, exist_ok=True)

    destination.write_text(page, encoding="utf-8")
