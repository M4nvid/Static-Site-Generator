class HTMLNode:
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list["HTMLNode"] | None = None, 
                 props: dict[str, str] | None = None,
                 ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError ("to_html method not implemented")
    
    def props_to_html(self) -> str:
        
        if not self.props:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, 
                 tag: str | None, 
                 value: str, 
                 props = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError ("ERROR: No value found")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self,
                  tag: str, 
                  children: list["HTMLNode"], 
                  props: dict [str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError ("ERROR: No tag found")
        if not self.children:
            raise ValueError ("ERROR: No node children found")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    