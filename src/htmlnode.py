class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    # overriden by children
    def to_html(self):
        raise NotImplementedError()
    
    # prints props dict as string
    def props_to_html(self):
        props_string = ""
        if self.props is None:
            return props_string
        for key in self.props:
            props_string += f" {key}=\"{self.props[key]}\""
        return props_string
    
    # for printing
    def __repr__(self):
        print(f"HTMLNode\n Tag: {self.tag}\n Value: {self.value}")
        print(f"Children: {self.children}\n Props: {self.props_to_html()}")


# LeafNode is an HTMLNode that has one tag and no children
# Example: <p>test<p>
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

# ParentNode is an HTMLNode that has no value but required children
# Example: <p><b>test</b></p> - <p> here is the parent
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must has a tag.")
        if self.children is None:
            raise ValueError("ParentNode must have children.")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_string += child.to_html()
        return html_string + f"</{self.tag}>"