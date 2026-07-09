import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_no_tag(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_more_children(self):
        boy_node = LeafNode("b", "Bold text")
        girl_node = LeafNode("i", "italic text")
        plant_node = LeafNode(None, "Normal text")
        parent_node = ParentNode ("div", [boy_node, girl_node, plant_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>Bold text</b><i>italic text</i>Normal text</div>",
    )
         
if __name__ == "__main__":
    unittest.main()    