from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "normal_text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # for testing and ==
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            raise TypeError("cannot compare TextNode with a different type")
        if self.text == other.text:
                if self.text_type == other.text_type:
                     if self.url == other.url:
                          return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
# standalone function for text to html conversion
def text_node_to_html_node(node):
    if node.text_type == TextType.TEXT:
        return LeafNode(None, node.text)
    if node.text_type == TextType.BOLD:
        return LeafNode("b", node.text)
    if node.text_type == TextType.ITALIC:
        return LeafNode("i", node.text)
    if node.text_type == TextType.CODE:
        return LeafNode("code", node.text)
    if node.text_type == TextType.LINK:
        return LeafNode("a", node.text, {"href": node.url})
    if node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": node.url, "alt": node.text})
    raise TypeError("node.text_type is not of type TextType(Enum)")