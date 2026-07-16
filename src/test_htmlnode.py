import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_property(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com"',
        )

    def test_props_to_html_multiple_properties(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html_empty_props(self):
        node = HTMLNode()

        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none_props(self):
        node = HTMLNode(props=None)

        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
