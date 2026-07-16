# Static Site Generator (SSG)

A custom static site generator built from scratch in Python. This engine reads structural raw Markdown files, extracts text metadata, passes tokens into an abstract syntax tree (AST), and dynamically compiles them into a clean, public-facing static website using HTML5 templates.

Building this project from scratch eliminates reliance on heavy external frameworks, proving mastery over core object-oriented programming (OOP), recursive file structures, and string parsing algorithms.

## 🚀 Key Features

* **Custom Markdown-to-HTML Parser**: Handles block-level structures (headings, paragraphs, code blocks, quotes, lists) and nested inline formatting (bold, italic, links, images).
* **Abstract Syntax Tree (AST) Architecture**: Implements recursive HTML node scaling to convert tokens into safe, predictable tree branches.
* **Smart Asset Synchronization**: Traverses and copies your `/static` asset folders cleanly into your deployment environment while ensuring stale, deleted files from previous builds are systematically wiped.
* **Dynamic Template Injection**: Recursively injects compiled HTML content and document title headers into a central boilerplate master layout.

## 🏗️ Software Architecture & Design

The engine is cleanly decoupled into four specialized architectural segments to ensure solid scalability:

```text
├── src/
│   ├── htmlnode.py       # Base, Leaf, and Parent Node layout abstractions
│   ├── textnode.py       # Inline styling token extraction maps
│   ├── block_markdown.py # Block-level document division and type filtering
│   └── main.py           # Core orchestrator handling file-I/O loops
```

1. **The HTML Tree (`htmlnode.py`)**: Utilizes custom composite objects (`ParentNode` and `LeafNode`) to scale components recursively into strict, nested raw HTML string fragments without template engine leaks.
2. **The Inline Lexer (`textnode.py`)**: Extracts inline syntax variables (like backticks for code or bracket delimiters for hyperlinks) using raw string processing boundaries.
3. **The Block Parser (`block_markdown.py`)**: Sections files into layout blocks, evaluates their syntactic semantic types, and maps structural markers to correct markup containers.
4. **The Build Engine (`main.py`)**: Coordinates system File-I/O operations. It handles absolute path validation, flushes prior compilation data, mirrors asset assets, and maps content down nested directory endpoints.

## 🛠️ Tech Stack & Skills Demonstrated

* **Language**: Python 3.12+ (Built strictly using standard library modules like `os`, `shutil`, and `re`).
* **Testing Suite**: Automated regression testing implemented using Python's native `unittest` framework.
* **CS Principles Demonstrated**: Recursion, Abstract Data Types (ADTs), Tree Traversals, Lexical Analysis, and Regular Expressions (Regex).

## 💻 Installation & Quickstart

### Prerequisites
Make sure you have Python 3 installed on your machine:
```bash
python3 --version
```

### Installation
Clone this repository down to your local directory framework:
```bash
git clone https://github.com
cd static-site-generator
```

### Running the Build Engine
To execute a build sweep and compile your raw files into standard static web packages, execute the orchestrator script:
```bash
python3 src/main.py
```
This commands the engine to look inside your `/content` and `/static` parameters and output your new operational deployment platform package directly within a freshly targeted `/public` directory.

### Running Local Test Suites
To trigger the complete test matrix covering token parsing boundary constraints and recursive tree regressions, run:
```bash
python3 -m unittest discover -s src
