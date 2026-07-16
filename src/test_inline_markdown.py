import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode(
            "This is text with a `code block` word",
            TextType.TEXT,
        )

        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "`",
                TextType.CODE,
            ),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_bold(self):
        node = TextNode(
            "This is **bold** text",
            TextType.TEXT,
        )

        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD,
            ),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_italic(self):
        node = TextNode(
            "This is _italic_ text",
            TextType.TEXT,
        )

        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "_",
                TextType.ITALIC,
            ),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_non_text_node(self):
        node = TextNode(
            "Already bold",
            TextType.BOLD,
        )

        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD,
            ),
            [node],
        )

    def test_invalid_markdown(self):
        node = TextNode(
            "This is `broken markdown",
            TextType.TEXT,
        )

        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [node],
                "`",
                TextType.CODE,
            )


if __name__ == "__main__":
    unittest.main()
