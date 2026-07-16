from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    """Represents an HTML node that contains a value but no child nodes."""

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        """Render the leaf node as an HTML string."""
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        return (
            f"<{self.tag}{self.props_to_html()}>"
            f"{self.value}"
            f"</{self.tag}>"
        )

    def __repr__(self):
        return (
            f"LeafNode("
            f"tag={self.tag}, "
            f"value={self.value}, "
            f"props={self.props})"
        )
