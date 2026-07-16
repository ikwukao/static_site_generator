import unittest

from textnode import (
        TextNode, 
        TextType,
        text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """TextNodes with identical proprties should be equal."""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        """TextNodes with different text should not be equal."""
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Wprld", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_equal_text_type(self):
        """TextNodes with different types should not be equal."""
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Boote.dev", TextType.LINK, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_equal_with_none_url(self):
        """TextNodes with None URLs should compare as equal."""
        node = TextNode("Code", TextType.CODE)
        node2 = TextNode("Code", TextType.CODE)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")


    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")


    def test_code(self):
        node = TextNode("print('Hello')", TextType.CODE)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello')")


    def test_link(self):
        node = TextNode(
            "Boot.dev",
            TextType.LINK,
            "https://www.boot.dev",
        )
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(
            html_node.props,
            {"href": "https://www.boot.dev"},
        )


    def test_image(self):
        node = TextNode(
            "logo",
            TextType.IMAGE,
            "logo.png",
        )
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {
                "src": "logo.png",
                "alt": "logo",
            },
        )


    def test_invalid_text_type(self):
        node = TextNode("Invalid", "INVALID")

        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
