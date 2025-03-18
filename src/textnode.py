from enum import Enum

class TextType(Enum):
    NORMAL = "normal_text"
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