import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
