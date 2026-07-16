from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)

from parentnode import ParentNode
from leafnode import LeafNode


def text_to_children(text: str):
    """
    Convert inline markdown text into a list of HTMLNode children.
    """
    return [
        text_node_to_html_node(node)
        for node in text_to_textnodes(text)
    ]


def heading_to_html(block: str) -> ParentNode:
    """
    Convert a Markdown heading into an HTML heading node.
    """
    level = 0

    while block[level] == "#":
        level += 1

    text = block[level + 1 :]

    return ParentNode(
        f"h{level}",
        text_to_children(text),
    )


def paragraph_to_html(block: str) -> ParentNode:
    """
    Convert a paragraph block into a <p> element.
    """
    text = " ".join(
        line.strip()
        for line in block.split("\n")
    )

    return ParentNode(
        "p",
        text_to_children(text),
    )


def quote_to_html(block: str) -> ParentNode:
    """
    Convert a Markdown blockquote into a <blockquote>.
    """
    lines = []

    for line in block.split("\n"):
        lines.append(line[1:].strip())

    text = " ".join(lines)

    return ParentNode(
        "blockquote",
        text_to_children(text),
    )


def unordered_list_to_html(block: str) -> ParentNode:
    """
    Convert an unordered Markdown list into a <ul>.
    """
    items = []

    for line in block.split("\n"):
        text = line[2:]

        items.append(
            ParentNode(
                "li",
                text_to_children(text),
            )
        )

    return ParentNode("ul", items)


def ordered_list_to_html(block: str) -> ParentNode:
    """
    Convert an ordered Markdown list into an <ol>.
    """
    items = []

    for line in block.split("\n"):
        text = line.split(". ", 1)[1]

        items.append(
            ParentNode(
                "li",
                text_to_children(text),
            )
        )

    return ParentNode("ol", items)


def code_to_html(block: str) -> ParentNode:
    """
    Convert a fenced code block into
    <pre><code>...</code></pre>.
    """
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


def markdown_to_html_node(markdown: str) -> ParentNode:
    """
    Convert an entire Markdown document into
    a single HTML node tree.
    """
    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:

        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            children.append(
                heading_to_html(block)
            )

        elif block_type == BlockType.PARAGRAPH:
            children.append(
                paragraph_to_html(block)
            )

        elif block_type == BlockType.CODE:
            children.append(
                code_to_html(block)
            )

        elif block_type == BlockType.QUOTE:
            children.append(
                quote_to_html(block)
            )

        elif block_type == BlockType.UNORDERED_LIST:
            children.append(
                unordered_list_to_html(block)
            )

        elif block_type == BlockType.ORDERED_LIST:
            children.append(
                ordered_list_to_html(block)
            )

    return ParentNode("div", children)
