from pathlib import Path

from copystatic import copy_static
from generate_page import generate_page


def main():
    root = Path(__file__).resolve().parent.parent

    copy_static(
        root / "static",
        root / "public",
    )

    generate_page(
        root / "content" / "index.md",
        root / "template.html",
        root / "public" / "index.html",
    )


if __name__ == "__main__":
    main()
