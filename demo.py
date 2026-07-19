#!/usr/bin/env python3
"""
Demo script for Rich Diff — run to see the diff renderable in action.

Usage:
    python demo.py              # Compare two built-in samples
    python demo.py file1 file2  # Compare two real files
"""

import sys
from rich.console import Console
from rich_diff import Diff


def demo_builtin():
    """Compare two sample Python functions."""
    old_code = """\"\"\"Math utilities module.\"\"\"

import math
from typing import List, Optional

def calculate_mean(values: List[float]) -> float:
    \"\"\"Calculate arithmetic mean.\"\"\"
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_std(values: List[float]) -> float:
    \"\"\"Calculate standard deviation.\"\"\"
    mean = calculate_mean(values)
    squared_diffs = [(x - mean) ** 2 for x in values]
    return math.sqrt(sum(squared_diffs) / len(values))

def linear_regression(x: List[float], y: List[float]) -> tuple:
    \"\"\"Simple linear regression.\"\"\"
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi * xi for xi in x)
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept

# Legacy function — to be removed
def legacy_helper():
    return "deprecated"
"""

    new_code = """\"\"\"Math utilities module — enhanced.\"\"\"

import math
import statistics
from typing import List, Optional, Tuple

def calculate_mean(values: List[float]) -> float:
    \"\"\"Calculate arithmetic mean using statistics module.\"\"\"
    if not values:
        return 0.0
    return statistics.mean(values)

def calculate_std(values: List[float]) -> float:
    \"\"\"Calculate sample standard deviation.\"\"\"
    if len(values) < 2:
        return 0.0
    return statistics.stdev(values)

def linear_regression(x: List[float], y: List[float]) -> Tuple[float, float]:
    \"\"\"Simple linear regression with R-squared.\"\"\"
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi * xi for xi in x)
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    intercept = (sum_y - slope * sum_x) / n

    # Calculate R-squared
    y_mean = sum_y / n
    ss_total = sum((yi - y_mean) ** 2 for yi in y)
    ss_residual = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
    r_squared = 1 - ss_residual / ss_total if ss_total != 0 else 0

    return slope, intercept, r_squared

def calculate_correlation(x: List[float], y: List[float]) -> float:
    \"\"\"Calculate Pearson correlation coefficient.\"\"\"
    return statistics.correlation(x, y)
"""

    console = Console()

    console.print()
    console.rule("[bold]Rich Diff — Unified View[/]", style="cyan")
    console.print()
    console.print(
        Diff(old_code, new_code, syntax="python", context_lines=3,
             title_a="Before: math_utils.py", title_b="After: math_utils.py")
    )

    console.print()
    console.rule("[bold]Rich Diff — Split View[/]", style="cyan")
    console.print()
    console.print(
        Diff(old_code, new_code, view="split", syntax="python",
             title_a="Before: math_utils.py", title_b="After: math_utils.py")
    )


def demo_files(path_a: str, path_b: str):
    """Compare two files from the filesystem."""
    console = Console()

    try:
        diff = Diff.from_paths(path_a, path_b)
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/]")
        sys.exit(1)

    console.print()
    console.rule(f"[bold]Diff: {path_a} → {path_b}[/]", style="cyan")
    console.print()
    console.print(diff)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        demo_files(sys.argv[1], sys.argv[2])
    else:
        demo_builtin()
