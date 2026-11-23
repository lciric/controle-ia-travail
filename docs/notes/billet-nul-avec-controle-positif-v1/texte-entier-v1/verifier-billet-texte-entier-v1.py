"""Vérifie chaque nombre du corps du billet (texte entier v1) contre le registre des affirmations.

Contrôles, sans rien recalculer des résultats :
 1. empreintes des six verdicts et des quatre PDF égales à celles du registre (et aux compagnons .sha256) ;
 2. pour chaque entrée : le motif est à la ligne écrite de la source (ou sur la page écrite du PDF) ;
    la valeur à la source est dans le motif ; arrondie au nombre de décimales écrit, elle égale le nombre du billet ;
 3. couverture : la suite des nombres du corps du billet (du titre aux notes hors billet, sans les
    identifiants arXiv, le nom du modèle et « log10 ») est exactement la suite des nombres du registre ;
 4. autotest : un nombre faussé, un motif déplacé et une citation privée d'un mot doivent être refusés.
Usage : python3 verifier-billet-texte-entier-v1.py  (depuis n'importe où dans le dépôt). Code 0 si tout est conforme.
Pièce de classe B. Écrit le 2026-11-23 par le rédacteur habilité du billet.
"""
import copy
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[3]
BILLET = ICI / "billet-texte-entier-en-v1.md"
REG = ICI / "registre-affirmations-v1.json"
MOTS = {"huit": 8, "quatre": 4, "cinq": 5, "une": 1, "S100": 1, "T100": 1, "dose 1": 1}


def sha_b(b):
    return hashlib.sha256(b).hexdigest()


def num(s):
    return float(s.replace("−", "-").replace(",", ".").rstrip("%").lstrip("+"))


def decimales(s):
    s = s.rstrip("%")
    return len(s.split(".")[1]) if "." in s else 0


def nombres_du_corps(texte):
    corps = texte.split("# Probes on a cost-inflating saboteur", 1)[1].split("## Hors billet", 1)[0]
    corps = re.sub(r"arXiv:\S+|Llama-3\.1-8B-Instruct|log10", "", corps)
    return re.findall(r"(?<![\w.])[−-]?\d+(?:\.\d+)?%?", corps), len(corps.split())


def texte_pdf(ref, chemin, page, h, cache):
    cle = (ref, chemin)
    if cle not in cache:
        b = subprocess.run(["git", "-C", str(RACINE), "show", f"{ref}:{chemin}"], capture_output=True, check=True).stdout
        if sha_b(b) != h:
            raise SystemExit(f"PDF {chemin} : empreinte {sha_b(b)} ≠ {h}")
        d = tempfile.mkdtemp()
        f = pathlib.Path(d) / "x.pdf"
        f.write_bytes(b)
        cache[cle] = f
    pages = []
    for mode in ("-raw", "-layout"):
        t = subprocess.run(["pdftotext", mode, "-f", str(page), "-l", str(page), str(cache[cle]), "-"],
                           capture_output=True, text=True).stdout
        pages.append(" ".join(t.split()))
    return pages


def valeur_ok(e):
    n, v = e["nombre"], e["valeur_source"]
    if v in MOTS:
        return MOTS[v] == num(n)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}|\d{8}", v):
        return n in v
    try:
        x = num(v)
    except ValueError:
        return False
    d = decimales(n)
    return abs(round(x + (1e-12 if x >= 0 else -1e-12), d) - num(n)) < 1e-9


def verifier(reg, texte, dire=print):
    defauts = 0
    lignes = {}
    for k, s in reg["sources"].items():
        b = (RACINE / s["chemin"]).read_bytes()
        comp = (RACINE / (s["chemin"] + ".sha256")).read_text().split()[0]
        ok = sha_b(b) == s["sha256"] == comp
        defauts += not ok
        dire(f"source {k} {s['chemin']} : empreinte {'égale' if ok else 'DIFFÉRENTE'} ({s['sha256'][:12]}…)")
        lignes[k] = b.decode("utf-8").splitlines()
    cache = {}
    for e in reg["entrees"]:
        src = e["source"]
        if src.startswith("PDF:"):
            _, k, page = src.split(":")
            p = reg["pdf"][k]
            pages = texte_pdf(p["ref"], p["chemin"], int(page), p["sha256"], cache)
            motif_ok = any(" ".join(e["motif"].split()) in t for t in pages)
            val_ok = (e["nombre"].rstrip("%") in e["motif"]) or (e["nombre"] == page)
            ou = f"{k} p. {page}"
        else:
            l = lignes[src][e["ligne"] - 1] if 0 < e["ligne"] <= len(lignes[src]) else ""
            motif_ok = e["motif"] in l and e["valeur_source"] in l
            val_ok = valeur_ok(e)
            ou = f"{src} l. {e['ligne']}"
        bon = motif_ok and val_ok
        defauts += not bon
        dire(f"{e['n']:3d} {e['nombre']:>8} ← {ou:<14} valeur source {e['valeur_source']!r:<24} "
             f"{'conforme' if bon else 'ÉCART (motif ' + str(motif_ok) + ', valeur ' + str(val_ok) + ')'}")
    toks, mots = nombres_du_corps(texte)
    attendus = [e["nombre"] for e in reg["entrees"]]
    couv = toks == attendus
    defauts += not couv
    dire(f"couverture : {len(toks)} nombres dans le corps, {len(attendus)} entrées ; suites égales : {couv}")
    if not couv:
        for i, (a, b) in enumerate(zip(toks, attendus)):
            if a != b:
                dire(f"  premier écart au rang {i + 1} : billet {a!r}, registre {b!r}")
                break
    dire(f"mots du corps (wc -w, marques de blocs comprises) : {mots}")
    return defauts


def main():
    reg = json.loads(REG.read_text(encoding="utf-8"))
    texte = BILLET.read_text(encoding="utf-8")
    print("billet", BILLET.name, sha_b(BILLET.read_bytes()))
    print("registre", REG.name, sha_b(REG.read_bytes()))
    d = verifier(reg, texte)
    # autotest : trois artefacts doivent être refusés
    muet = lambda *_: None
    r1 = copy.deepcopy(reg); r1["entrees"][14]["nombre"] = "0.5749"
    t1 = texte.replace("deception 0.5748", "deception 0.5749", 1)
    r2 = copy.deepcopy(reg); r2["entrees"][14]["ligne"] += 1
    r3 = copy.deepcopy(reg)
    i3 = next(i for i, e in enumerate(r3["entrees"]) if e["source"] == "PDF:FIBS:34")
    r3["entrees"][i3]["motif"] = r3["entrees"][i3]["motif"].replace("nearly ", "")
    r3["entrees"][i3]["motif"] = r3["entrees"][i3]["motif"].replace("outright", "plainly")
    auto = [verifier(r1, t1, muet) > 0, verifier(r2, texte, muet) > 0, verifier(r3, texte, muet) > 0]
    print("autotest (nombre faussé, ligne déplacée, citation altérée) refusés :", auto)
    tout = d == 0 and all(auto)
    print("RÉSULTAT :", "CONFORME" if tout else f"ÉCARTS ({d})")
    sys.exit(0 if tout else 1)


if __name__ == "__main__":
    main()
