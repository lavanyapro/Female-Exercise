"""Wrap the Petite Power page into a full HTML document for the Android app.

Usage (from the PetitePowerAndroid folder):
    python tools/bundle_html.py ../petite-power.html
Writes app/src/main/assets/index.html.
"""
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else root.parent / "petite-power.html")
body = src.read_text(encoding="utf-8")

head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px system-ui,sans-serif;-webkit-tap-highlight-color:transparent}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""

out = head + body + "\n</html>\n"
dest = root / "app" / "src" / "main" / "assets" / "index.html"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(out, encoding="utf-8")
print(f"Wrote {dest} ({len(out):,} bytes)")
