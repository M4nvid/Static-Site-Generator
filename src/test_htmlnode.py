import unittest
from htmlnode import HTMLNode, LeafNode

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
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_value_none(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_leaf_tag_none(self):
        node = LeafNode(None, "Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
    def test_leaf_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')
if __name__ == "__main__":
    unittest.main()    