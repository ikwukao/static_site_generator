import unittest

from inline_markdown import (
        split_nodes_delimiter,
        extract_markdown_images,
        extract_markdown_links,
        text_to_textnodes,
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


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )

    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode(
                "image",
                TextType.IMAGE,
                "https://i.imgur.com/zjjcJKZ.png",
            ),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image",
                TextType.IMAGE,
                "https://i.imgur.com/3elNhQu.png",
            ),
        ],
        split_nodes_image([node]),
    )


def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://boot.dev) and another [Google](https://google.com)",
        TextType.TEXT,
    )

    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode(
                "link",
                TextType.LINK,
                "https://boot.dev",
            ),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "Google",
                TextType.LINK,
                "https://google.com",
            ),
        ],
        split_nodes_link([node]),
    )


def test_split_image_no_images(self):
    node = TextNode(
        "Plain text only",
        TextType.TEXT,
    )

    self.assertListEqual(
        [node],
        split_nodes_image([node]),
    )


def test_split_link_no_links(self):
    node = TextNode(
        "Plain text only",
        TextType.TEXT,
    )

    self.assertListEqual(
        [node],
        split_nodes_link([node]),
    )


def test_split_non_text_node(self):
    node = TextNode(
        "Already bold",
        TextType.BOLD,
    )

    self.assertListEqual(
        [node],
        split_nodes_link([node]),
    )


def test_text_to_textnodes(self):
    nodes = text_to_textnodes(
        "This is **bold** text with _italic_ and `code`."
    )

    self.assertEqual(
        nodes,
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ],
    )


if __name__ == "__main__":
    unittest.main()
