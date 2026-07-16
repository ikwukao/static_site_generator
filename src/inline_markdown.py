from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType,
) -> list[TextNode]:
    """
    Split text nodes around a Markdown delimiter.

    Example:
    "This is `code` text"
    ->
    TEXT("This is ")
    CODE("code")
    TEXT(" text")
    """

    new_nodes = []

    for old_node in old_nodes:
        # Leave non-text nodes untouched.
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        sections = old_node.text.split(delimiter)

        # An even number of sections means an unmatched delimiter.
        if len(sections) % 2 == 0:
            raise ValueError(f"Invalid markdown: unmatched '{delimiter}' delimiter")

        for i, section in enumerate(sections):
            if section == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))

    return new_nodes
