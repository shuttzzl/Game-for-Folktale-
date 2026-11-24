from pathlib import Path
import sys
import webbrowser

ROOT = Path(__file__).resolve().parent


def build():
    code = (ROOT / "game.py").read_text(encoding="utf-8")
    if "</script" in code.lower():
        raise ValueError("A Python source contains an HTML script closing tag")
    page = ROOT / "index.html"
    page.write_text(
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<meta name="theme-color" content="#090e18"><title>Who Stole the Stairs?</title>\n'
        '<script src="runtime/brython.js"></script></head><body>\n'
        '<script type="text/python">\n' + code + '\n</script></body></html>\n',
        encoding="utf-8")
    return page


def main():
    page = build()
    if "--build" not in sys.argv:
        print("Opening", page)
        webbrowser.open(page.as_uri())


if __name__ == "__main__":
    main()
