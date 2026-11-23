"""Note Markdown -> PDF (v1) : pandoc rend le HTML (feuille de style incluse), Chromium (sans tête) imprime le PDF.
Usage : python md_vers_pdf_v1.py NOTE.md [NOTE2.md ...] ; écrit NOTE.pdf à côté (jamais par-dessus un PDF existant)."""
import subprocess
import sys
import tempfile
from pathlib import Path

CHROMIUM = "/opt/pw-browsers/chromium"
STYLE = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 11pt; line-height: 1.45; max-width: 17cm; margin: auto; color: #111; }
h1 { font-size: 18pt; margin-bottom: .2em; } h2 { font-size: 14pt; margin-top: 1.4em; border-bottom: 1px solid #ccc; }
h3 { font-size: 12pt; margin-top: 1em; } table { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: .6em 0; }
th, td { border: 1px solid #bbb; padding: 3px 5px; vertical-align: top; text-align: left; } th { background: #f0f0f0; }
code { font-size: 9pt; word-break: break-all; } blockquote { color: #444; border-left: 3px solid #ccc; margin-left: 0; padding-left: .8em; }
"""


def convertir(md):
    md = Path(md).resolve()
    pdf = md.with_suffix(".pdf")
    if pdf.exists():
        raise SystemExit(f"ARRÊT : {pdf} existe ; rien n'est écrasé")
    with tempfile.TemporaryDirectory() as t:
        css = Path(t) / "style.css"
        css.write_text(STYLE, encoding="utf-8")
        html = Path(t) / "note.html"
        subprocess.run(["pandoc", str(md), "-f", "gfm", "-t", "html5", "-s", "--embed-resources", "--css", str(css),
                        "--metadata", f"pagetitle={md.stem}", "-o", str(html)], check=True)
        subprocess.run([CHROMIUM, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", html.as_uri()], check=True, capture_output=True)
    if not pdf.exists() or pdf.stat().st_size < 1000:
        raise SystemExit(f"ARRÊT : PDF absent ou vide pour {md}")
    print(pdf)


if __name__ == "__main__":
    for f in sys.argv[1:]:
        convertir(f)
