from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    """Represents an HTML node that contains one or more child nodes."""

    def __init__(self, tag, children, props=None):
        super().__init__(
            tag=tag,
            value=None,
            children=children,
            props=props,
        )

    def to_html(self):
        """Render this parent node and all of its children as HTML."""
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return (
            f"<{self.tag}{self.props_to_html()}>"
            f"{children_html}"
            f"</{self.tag}>"
        )

    def __repr__(self):
        return (
            f"ParentNode("
            f"tag={self.tag}, "
            f"children={self.children}, "
            f"props={self.props})"
        )
