import sys
from pathlib import Path

from copystatic import copy_static
from generate_page import generate_pages_recursive


def main():
    root = Path(__file__).resolve().parent.parent

    # Default to "/" for local development
    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    docs_dir = root / "docs"

    copy_static(
        root / "static",
        docs_dir,
    )

    generate_pages_recursive(
        root / "content",
        root / "template.html",
        docs_dir,
        basepath,
    )


if __name__ == "__main__":
    main()
