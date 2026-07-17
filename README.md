# 🚀 Static Site Generator

A production-style static site generator built entirely from scratch in Python.

This project parses Markdown documents, transforms them into an intermediate representation, and generates complete HTML pages using a custom rendering engine. It recursively processes directories, copies static assets, applies HTML templates, and produces a deployable static website without relying on external frameworks.

Developed as part of the Boot.dev Backend Developer curriculum, this project demonstrates core software engineering concepts including object-oriented programming, recursive algorithms, parsing, HTML generation, and filesystem automation.

---

## ✨ Features

- 📄 Convert Markdown documents into semantic HTML
- 📝 Support for:
  - Headings
  - Paragraphs
  - Bold
  - Italics
  - Inline code
  - Code blocks
  - Blockquotes
  - Ordered lists
  - Unordered lists
  - Images
  - Hyperlinks
- 🌳 Recursive HTML node rendering using custom node classes
- 📂 Recursive content discovery and page generation
- 🎨 Automatic copying of static assets
- 🧩 HTML template rendering
- 🌐 Configurable base path for GitHub Pages deployment
- ✅ Comprehensive unit test suite using Python's `unittest`

---

# Architecture

```
static_site_generator/
│
├── content/                 # Markdown source files
├── static/                  # CSS, images, favicon
├── docs/                    # Generated production website
│
├── src/
│   ├── main.py
│   ├── generate_page.py
│   ├── markdown_parser.py
│   ├── markdown_blocks.py
│   ├── inline_markdown.py
│   ├── htmlnode.py
│   ├── leafnode.py
│   ├── parentnode.py
│   ├── textnode.py
│   └── ...
│
├── template.html
├── build.sh
├── main.sh
└── README.md
```

---

# How It Works

The generator follows a simple compilation pipeline:

```
Markdown Files
       │
       ▼
Split into Blocks
       │
       ▼
Determine Block Types
       │
       ▼
Parse Inline Markdown
       │
       ▼
Create TextNodes
       │
       ▼
Convert to HTMLNodes
       │
       ▼
Render HTML
       │
       ▼
Inject into Template
       │
       ▼
Copy Static Assets
       │
       ▼
Deployable Static Website
```

---

# Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Regular Expressions (Regex)
- Recursive Algorithms
- HTML5
- Markdown
- Python Standard Library
- unittest

---

# Skills Demonstrated

This project demonstrates practical experience with:

- Object-Oriented Design
- Recursive Tree Structures
- Parsing Algorithms
- Markdown Processing
- HTML Generation
- File System Traversal
- Recursive Directory Walking
- Static Site Generation
- Test-Driven Development
- Git & GitHub

---

# Installation

Clone the repository:

```bash
git clone https://github.com/ikwukao/static_site_generator.git
cd static_site_generator
```

---

# Running Locally

Generate the website:

```bash
python3 src/main.py
```

or

```bash
./main.sh
```

The generated site is written to the `docs/` directory.

To preview it locally:

```bash
cd docs
python3 -m http.server 8888
```

Visit:

```
http://localhost:8888
```

---

# Production Build

For GitHub Pages deployment:

```bash
./build.sh
```

The build script generates the site using the configured repository base path and outputs the production-ready files into the `docs/` directory.

---

# Running Tests

Run the complete test suite:

```bash
./test.sh
```

or

```bash
python3 -m unittest discover -s src
```

---

# Example Output

```
content/
    index.md
    blog/
        post.md

        │

        ▼

docs/
    index.html
    blog/
        post/
            index.html
```

---

# Learning Outcomes

Building this project from scratch strengthened my understanding of:

- Designing recursive data structures
- Building parsers without third-party libraries
- Transforming Markdown into HTML
- Recursive filesystem traversal
- Template-based rendering
- Python project organization
- Writing maintainable, testable code

---

# Future Improvements

- Table support
- Nested lists
- Footnotes
- Syntax highlighting
- Live development server
- Incremental builds
- Plugin architecture
- YAML front matter
- RSS feed generation
- Search indexing

---

# Acknowledgements

Built as part of the **Boot.dev Backend Development** curriculum.

---

## License

This project is licensed under the MIT License.
