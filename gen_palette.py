#!/usr/bin/env python3
"""
Reads `palette.json`, generates SVG circle assets for each color, and prints
HTML table rows for README.
"""

import json
from pathlib import Path
import shutil


PALETTE_PATH = "palette.json"


def gen_circle_svg(color):
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="50" fill="{color}" />
</svg>
"""[1:]


def gen_table_item(path, name, hex):
    return f"""
  <tr>
    <td><img src="{path}" width="23"/></td>
    <td>{name}</td>
    <td><code>{hex}</code></td>
  </tr>
"""[1:]


palette_path = Path(PALETTE_PATH)
palette = json.loads(palette_path.read_text(encoding="utf-8"))

circles_path = Path("assets", "circles")

if circles_path.exists():
    shutil.rmtree(circles_path)
circles_path.mkdir(parents=True, exist_ok=True)

for color_name, hex in palette["palette"].items():
    hex_code = hex[1:]
    circle_path = circles_path / f"{hex_code}.svg"
    circle_svg = gen_circle_svg(hex)
    circle_path.write_text(circle_svg)

    pretty_color_name = color_name.capitalize()
    table_item = gen_table_item(str(circle_path), pretty_color_name, hex)
    print(table_item, end="")

# TODO: handle palette["asci"].
