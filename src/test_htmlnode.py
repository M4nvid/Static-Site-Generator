import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        none_tester = HTMLNode("p", "this is a paragraph", None, None)
        self.assertEqual(none_tester.props_to_html(), "")
    def test_empty(self):
        empty_tester = HTMLNode("p", "this is a paragraph", None, {})
        self.assertEqual(empty_tester.props_to_html(), "")
    def test_props(self):
        dict_tester = HTMLNode("p", "this is a paragraph", None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(dict_tester.props_to_html(), ' href="https://www.google.com" target="_blank"')
if __name__ == "__main__":
    unittest.main()    