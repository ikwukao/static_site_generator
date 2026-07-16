def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Split a Markdown document into individual blocks.

    A block is separated by one or more blank lines.
    Leading and trailing whitespace is removed from each block,
    and empty blocks are discarded.
    """
    blocks = markdown.split("\n\n")

    cleaned_blocks = []

    for block in blocks:
        block = block.strip()

        if block:
            cleaned_blocks.append(block)

    return cleaned_blocks
