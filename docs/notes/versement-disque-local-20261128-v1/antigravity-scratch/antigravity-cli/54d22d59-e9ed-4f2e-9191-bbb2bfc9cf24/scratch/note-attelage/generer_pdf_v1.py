#!/usr/bin/env python3
"""Convertit note-de-sortie-collisionneur-attelage-plan-turing-v1.md en HTML propre puis PDF via Microsoft Edge headless."""

from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

ROOT = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain\54d22d59-e9ed-4f2e-9191-bbb2bfc9cf24\scratch\note-attelage"
)
MD_PATH = ROOT / "note-de-sortie-collisionneur-attelage-plan-turing-v1.md"
HTML_PATH = ROOT / "note-de-sortie-collisionneur-attelage-plan-turing-v1.html"
PDF_PATH = ROOT / "note-de-sortie-collisionneur-attelage-plan-turing-v1.pdf"
EDGE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")


def inline_md(text: str) -> str:
    s = html.escape(text)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def md_to_html(md_text: str) -> str:
    lines = md_text.splitlines()
    title = ""
    subtitle = ""
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            m_t = re.match(r'^title:\s*"(.*)"\s*$', lines[i])
            m_s = re.match(r'^subtitle:\s*"(.*)"\s*$', lines[i])
            if m_t:
                title = m_t.group(1)
            if m_s:
                subtitle = m_s.group(1)
            i += 1
        i += 1

    out = []
    if title:
        out.append(f"<header><h1>{html.escape(title)}</h1>")
        if subtitle:
            out.append(f"<p class='subtitle'>{html.escape(subtitle)}</p>")
        out.append("</header>")

    in_ul = False
    in_ol = False
    in_code = False
    code_buf: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            close_lists()
            if not in_code:
                in_code = True
                code_buf = []
            else:
                out.append("<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        stripped = line.strip()
        if not stripped:
            close_lists()
            i += 1
            continue
        if stripped == "---":
            close_lists()
            out.append("<hr/>")
            i += 1
            continue

        # Tables
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-\|]+\|$", lines[i + 1].strip()):
            close_lists()
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append("<table><thead><tr>")
            for h in headers:
                out.append(f"<th>{inline_md(h)}</th>")
            out.append("</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>")
                for c in r:
                    out.append(f"<td>{inline_md(c)}</td>")
                out.append("</tr>")
            out.append("</tbody></table>")
            continue

        # Headings
        m_h = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m_h:
            close_lists()
            lvl = len(m_h.group(1))
            out.append(f"<h{lvl}>{inline_md(m_h.group(2))}</h{lvl}>")
            i += 1
            continue

        # Lists
        m_ul = re.match(r"^-\s+(.*)$", stripped)
        if m_ul:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(m_ul.group(1))}</li>")
            i += 1
            continue

        m_ol = re.match(r"^\d+\.\s+(.*)$", stripped)
        if m_ol:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(m_ol.group(1))}</li>")
            i += 1
            continue

        close_lists()
        out.append(f"<p>{inline_md(stripped)}</p>")
        i += 1

    close_lists()
    body = "\n".join(out)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8"/>
<title>{html.escape(title)}</title>
<style>
  @page {{ size: A4; margin: 16mm 14mm 18mm 14mm; }}
  body {{ font-family: "Segoe UI", "Liberation Sans", Arial, sans-serif; font-size: 9.2pt; line-height: 1.42; color: #1a1a1a; }}
  header {{ border-bottom: 2px solid #222; margin-bottom: 12pt; padding-bottom: 6pt; }}
  h1 {{ font-size: 16pt; margin: 0 0 4pt 0; color: #111; }}
  .subtitle {{ font-size: 10.5pt; color: #444; margin: 0; font-style: italic; }}
  h2 {{ font-size: 12pt; margin-top: 14pt; margin-bottom: 5pt; border-bottom: 1px solid #bbb; padding-bottom: 2pt; page-break-after: avoid; }}
  h3 {{ font-size: 10.2pt; margin-top: 10pt; margin-bottom: 4pt; page-break-after: avoid; }}
  p {{ margin: 4pt 0 6pt 0; text-align: justify; }}
  ul, ol {{ margin: 4pt 0 6pt 0; padding-left: 16pt; }}
  li {{ margin-bottom: 3pt; }}
  table {{ width: 100%; border-collapse: collapse; margin: 7pt 0 9pt 0; font-size: 7.7pt; table-layout: auto; }}
  th, td {{ border: 0.6pt solid #999; padding: 3pt 4pt; vertical-align: top; text-align: left; word-wrap: break-word; overflow-wrap: anywhere; }}
  th {{ background: #eef1f5; font-weight: 600; }}
  tr {{ page-break-inside: avoid; }}
  code {{ font-family: Consolas, "Courier New", monospace; font-size: 7.8pt; background: #f4f4f4; padding: 0.5pt 2pt; border-radius: 2pt; }}
  pre {{ background: #f4f4f4; padding: 6pt; border: 0.6pt solid #ccc; white-space: pre-wrap; word-break: break-all; font-size: 7.2pt; }}
  hr {{ border: none; border-top: 0.8pt solid #ccc; margin: 10pt 0; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def main() -> None:
    md_text = MD_PATH.read_text(encoding="utf-8")
    HTML_PATH.write_text(md_to_html(md_text), encoding="utf-8")
    cmd = [
        str(EDGE),
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        HTML_PATH.as_uri(),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    print("EDGE_RC:", res.returncode)
    if res.stderr:
        print("EDGE_STDERR:", res.stderr[:500])
    if PDF_PATH.exists():
        print("PDF_BYTES:", PDF_PATH.stat().st_size)


if __name__ == "__main__":
    main()
