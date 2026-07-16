import unittest

from markdown_blocks import (
        BlockType,
        block_to_block_type,
        markdown_to_blocks,
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = "Just one paragraph."

        self.assertEqual(
            markdown_to_blocks(md),
            ["Just one paragraph."],
        )

    def test_extra_blank_lines(self):
        md = """

First block


Second block



Third block

"""

        self.assertEqual(
            markdown_to_blocks(md),
            [
                "First block",
                "Second block",
                "Third block",
            ],
        )

    def test_empty_markdown(self):
        self.assertEqual(
            markdown_to_blocks(""),
            [],
        )


class TestBlockTypes(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading"),
            BlockType.HEADING,
        )

    def test_heading_level_six(self):
        self.assertEqual(
            block_to_block_type("###### Small Heading"),
            BlockType.HEADING,
        )

    def test_code_block(self):
        block = """```
print("Hello")
```"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE,
        )

    def test_quote_block(self):
        block = """>One
>Two
>Three"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE,
        )

    def test_unordered_list(self):
        block = """- One
- Two
- Three"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        block = """1. One
2. Two
3. Three"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST,
        )

    def test_paragraph(self):
        block = """This is a paragraph.
It spans multiple lines."""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )

    def test_invalid_ordered_list(self):
        block = """1. One
3. Three"""

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH,
        )


if __name__ == "__main__":
    unittest.main()
