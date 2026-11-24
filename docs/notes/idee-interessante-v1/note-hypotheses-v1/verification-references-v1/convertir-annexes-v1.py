"""Convertit les trois réponses de Google en LaTeX (annexes), sans changer le fond.
Seules transformations de forme : listes de références de Neon écrites en paragraphe
(séparateur « — ») mises en liste ; titres sans numérotation LaTeX (les réponses portent
leur propre numérotation). Vérifie que le texte est conservé (mêmes caractères hors
séparateurs et blancs)."""
import re, subprocess, sys, pathlib

src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
SHIFT = {"argon": -1, "carbon": 0, "neon": 0}

def split_refs(md: str) -> str:
    lines = md.split("\n"); res = []
    for i, ln in enumerate(lines):
        prev = lines[i - 1] if i else ""
        is_block = (prev.strip() == "**Références de la partie 1 :**" and " — " in ln) \
            or (ln.startswith("*Références ajoutées :*") and " — " in ln)
        if is_block:
            head = ""
            if ln.startswith("*Références ajoutées :*"):
                head, ln = "*Références ajoutées :*", ln[len("*Références ajoutées :*"):].strip()
            items = ln.split(" — ")
            if head:
                res.append(head); res.append("")
            res.extend("- " + it.strip() for it in items)
        else:
            res.append(ln)
    return "\n".join(res)

def norm(s):
    return re.sub(r"[\s\-—*]", "", s)

for m in ("argon", "carbon", "neon"):
    md = (src / f"reponse-{m}-v1.md").read_text(encoding="utf-8")
    md2 = split_refs(md)
    assert norm(md) == norm(md2), f"texte modifié pour {m}"
    tex = subprocess.run(["pandoc", "-f", "markdown-auto_identifiers", "-t", "latex",
                          f"--shift-heading-level-by={SHIFT[m]}"], input=md2,
                         capture_output=True, text=True, check=True).stdout
    tex = re.sub(r"\\(sub)*section\{", lambda x: x.group(0)[:-1] + "*{", tex)
    tex = tex.replace("≠", r"\ensuremath{\neq}")
    (out / f"annexe-{m}.tex").write_text(tex, encoding="utf-8")
    print(m, "ok", len(md), "->", len(tex))
