import unittest

from inline_markdown import (
        split_nodes_delimiter,
        extract_markdown_images,
        extract_markdown_links,
)

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


class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "![one](https://one.com) and ![two](https://two.com)"
        )

        self.assertListEqual(
            [
                ("one", "https://one.com"),
                ("two", "https://two.com"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Visit [Boot.dev](https://www.boot.dev)"
        )

        self.assertListEqual(
            [("Boot.dev", "https://www.boot.dev")],
            matches,
        )

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "[Google](https://google.com) and [GitHub](https://github.com)"
        )

        self.assertListEqual(
            [
                ("Google", "https://google.com"),
                ("GitHub", "https://github.com"),
            ],
            matches,
        )

    def test_extract_no_images(self):
        self.assertListEqual(
            [],
            extract_markdown_images("No images here."),
        )

    def test_extract_no_links(self):
        self.assertListEqual(
            [],
            extract_markdown_links("No links here."),
        )


if __name__ == "__main__":
    unittest.main()
