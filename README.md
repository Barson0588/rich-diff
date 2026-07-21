# Rich Diff — Diff Renderable for Rich

A terminal diff viewer built as a [Rich](https://github.com/Textualize/rich) renderable.

```python
from rich.console import Console
from rich.diff import Diff

console = Console()
console.print(Diff(old_text, new_text, syntax="python"))
```

## Features

- **Unified diff view** with colored additions (green) and deletions (red)
- **Split / side-by-side view** with left (old) and right (new) panes
- **Syntax highlighting** via pygments lexers (auto-detected from file extension)
- **Line numbers** in unified view
- **Configurable context lines**
- **File path diffing** with `Diff.from_paths("old.py", "new.py")`
- **Full Rich renderable protocol**: implements `__rich_console__` and `__rich_measure__`

## Installation

Copy `rich_diff.py` into `rich/diff.py` in your Rich installation, or add it to your project.

## Usage

### Quick start

```python
from rich.diff import Diff
from rich.console import Console

old = "def add(a, b):\n    return a + b"
new = "def add(a, b):\n    \"\"\"Add two numbers.\"\"\"\n    return a + b"

console = Console()
console.print(Diff(old, new))
```

### Compare files

```python
diff = Diff.from_paths("old/main.py", "new/main.py", syntax="python")
console.print(diff)
```

### Split view

```python
console.print(Diff(old, new, view="split"))
```

### Output preview

```
--- a
+++ b

@@ -1,2 +1,3 @@
-def add(a, b):          (red background)
-    return a + b
+def add(a, b):          (green background)
+    \"\"\"Add two numbers.\"\"\"
+    return a + b
```

## Author

Barson0588

## License

MIT
