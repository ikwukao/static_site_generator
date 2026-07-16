from textnode import (
    text_to_textnodes,
    text_node_to_html_node,
)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    children = []

    for node in text_nodes:
        children.append(text_node_to_html_node(node))

    return children


def heading_to_html(block):
    level = 0

    while block[level] == "#":
        level += 1

    text = block[level + 1 :]

    return ParentNode(
        f"h{level}",
        text_to_children(text),
    )


def paragraph_to_html(block):
    text = " ".join(block.split("\n"))

    return ParentNode(
        "p",
        text_to_children(text),
    )


def quote_to_html(block):
    lines = []

    for line in block.split("\n"):
        lines.append(line.lstrip("> ").strip())

    text = " ".join(lines)

    return ParentNode(
        "blockquote",
        text_to_children(text),
    )


def unordered_list_to_html(block):
    items = []

    for line in block.split("\n"):
        item = line[2:]

        items.append(
            ParentNode(
                "li",
                text_to_children(item),
            )
        )

    return ParentNode("ul", items)

def code_to_html(block):
    lines = block.split("\n")

    code = "\n".join(lines[1:-1]) + "\n"

    return ParentNode(
        "pre",
        [
            LeafNode(
                "code",
                code,
            )
        ],
    )


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            children.append(heading_to_html(block))

        elif block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html(block))

        elif block_type == BlockType.CODE:
            children.append(code_to_html(block))

        elif block_type == BlockType.QUOTE:
            children.append(quote_to_html(block))

        elif block_type == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html(block))

        elif block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html(block))

    return ParentNode("div", children)
