import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello World"

        self.assertEqual(
            extract_title(md),
            "Hello World",
        )

    def test_extract_title_with_whitespace(self):
        md = "   # Tolkien Fan Club   "

        self.assertEqual(
            extract_title(md),
            "Tolkien Fan Club",
        )

    def test_extract_title_missing(self):
        md = "This is just a paragraph."

        with self.assertRaises(ValueError):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
