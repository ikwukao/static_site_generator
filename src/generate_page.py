from pathlib import Path

from markdown_parser import markdown_to_html_node


def extract_title(markdown: str) -> str:
    """
    Extract the H1 heading from a Markdown document.
    """
    for line in markdown.splitlines():
        line = line.strip()

        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No H1 heading found.")


def generate_page(from_path, template_path, dest_path):
    """
    Generate a single HTML page from a Markdown file.
    """
    print(
        f"Generating page from '{from_path}' "
        f"to '{dest_path}'"
    )

    markdown = Path(from_path).read_text(encoding="utf-8")

    template = Path(template_path).read_text(
        encoding="utf-8"
    )

    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    page = template.replace(
        "{{ Title }}",
        title,
    )

    page = page.replace(
        "{{ Content }}",
        html,
    )

    destination = Path(dest_path)

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    destination.write_text(
        page,
        encoding="utf-8",
    )


def generate_pages_recursive(
    dir_path_content,
    template_path,
    dest_dir_path,
):
    """
    Recursively generate HTML pages for every Markdown
    file inside the content directory.
    """

    content_dir = Path(dir_path_content)

    output_dir = Path(dest_dir_path)

    for item in content_dir.iterdir():

        if item.is_dir():

            generate_pages_recursive(
                item,
                template_path,
                output_dir / item.name,
            )

        elif item.suffix == ".md":

            destination = (
                output_dir
                / item.with_suffix(".html").name
            )

            generate_page(
                item,
                template_path,
                destination,
            )
