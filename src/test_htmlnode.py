import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    #testing HTMLNode

    def test_to_html(self):
        node = HTMLNode("p", "this is test text", None, None)
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("p", "this is test text", None, {"href":"https://google.com"})
        self.assertEqual(" href=\"https://google.com\"", node.props_to_html())

    # testing LeafNode
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link", {"href":"https://google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://google.com\">This is a link</a>")

    # testing ParentNode

    def test_parent_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_parent_with_no_children(self):
        parent_node = ParentNode("span", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_parent_with_three_children(self):
        child_1 = LeafNode("b", "berries")
        child_2 = LeafNode("i", "igloos")
        child_3 = LeafNode(None, "normal")
        parent_node = ParentNode("span", [child_1, child_2, child_3])
        self.assertEqual(parent_node.to_html(), "<span><b>berries</b><i>igloos</i>normal</span>")