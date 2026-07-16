import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " Normal "),
                LeafNode("i", "Italic"),
            ],
        )

        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold</b> Normal <i>Italic</i></p>",
        )

    def test_parent_with_props(self):
        parent = ParentNode(
            "div",
            [LeafNode("p", "Hello")],
            {"class": "container"},
        )

        self.assertEqual(
            parent.to_html(),
            '<div class="container"><p>Hello</p></div>',
        )

    def test_missing_tag(self):
        parent = ParentNode(
            None,
            [LeafNode("p", "Hello")],
        )

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_missing_children(self):
        parent = ParentNode("div", None)

        with self.assertRaises(ValueError):
            parent.to_html()


if __name__ == "__main__":
    unittest.main()
