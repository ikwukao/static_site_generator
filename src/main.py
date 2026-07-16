from pathlib import Path

from copystatic import copy_static
from generate_page import generate_pages_recursive


def main():

    root = Path(__file__).resolve().parent.parent

    copy_static(
        root / "static",
        root / "public",
    )

    generate_pages_recursive(
        root / "content",
        root / "template.html",
        root / "public",
    )


if __name__ == "__main__":
    main()
