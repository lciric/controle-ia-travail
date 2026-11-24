"""Taux d'erreur relevés par programme, par modèle, sur toutes les cellules des courses incluses.

1. Mentions « VÉRIFIÉ » sans source ni calcul sur la même ligne (lignes de légende exclues).
2. Calculs simples « a op b = c » rejoués par code (op ∈ × * / + − -), tolérance : la moitié de la
   dernière décimale affichée de c, et au moins 0,5 % relatif ; « ≈ » tolère 5 %.
3. Identifiants arXiv : format impossible (mois hors 01-12, date après novembre 2026, nombre de chiffres
   incompatible avec la date) ; pour ceux dont le PDF est dans le dépôt, concordance entre le contexte
   de citation et la première page du PDF (au moins un nom propre ou mot rare commun), sinon « suspecte ».
Sortie : sorties/erreurs-v1.json (+ listes des cas pour relecture humaine).
"""
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from audit_commun_v2 import SORTIES, mots
from cellules_v1 import charger

LEGENDE = re.compile(r"V[ÉE]RIFI[ÉE]\W{0,4}\s*[:=—–-]\s*(calcul|ce |tout|fait|affirm|ce qui|[ée]nonc|v[ée]rifi|j'ai|refait|r[ée]sultat)", re.I)
SOURCE = re.compile(r"(`[^`]{3,}`|\bp\.\s?\d|\bpages?\s\d|\bl\.\s?\d|\blignes?\s\d|[0-9a-f]{8,}|\d{4}\.\d{4,5}|faits|FAITS|§|"
                    r"\bF\d|\bfait\s?\d|\bpoint\s\d|dossier|pi[èe]ce|question|tableau|section|annexe|=|≈|≤|≥|<|>|"
                    r"\d+\s?[×x*/+−-]\s?\d+|calcul|refait|recalcul|v[ée]rifi[ée] (ici|par|sur|dans)|cf\.|voir )", re.I)


META = re.compile(r"(selon [A-G]\b|par [A-G]\b|de [A-G]\b|[A-G] note|not[ée]s? V|marqu[ée]|statuts?|n'est V|pas V|comme V|« ?\[?V[ÉE]RIFI[ÉE]\]? ?»|"
                  r"auto-?attribu|sans audit|lis comme|garde RAPPORT|abus|dit V|qualifi[ée] de|\bV[ÉE]RIFI[ÉE]S?\b\s*(?:par moi|ici par))", re.I)
CALCUL_OU_PIECE = re.compile(r"(=|≈|≤|≥|\d\s?[×*/+−-]\s?\d|calcul|refait|recalcul|d[ée]velopp|d[ée]riv|`[^`]{3,}`|\bfaits?\b|FAITS|"
                             r"\bp\.\s?\d|\bl\.\s?\d|ligne\s\d|[0-9a-f]{8,}|\bF\d|pi[èe]ce)", re.I)


def verifie_strict(C):
    """Étiquette « VÉRIFIÉ » posée par le modèle sur sa propre affirmation, hors mentions sur autrui,
    sans calcul visible ni renvoi à une pièce servie sur la même ligne."""
    par = defaultdict(lambda: {"etiquettes": 0, "sans_calcul_ni_piece": 0, "caracteres": 0, "echantillon": []})
    for c in C:
        if c["rejeu_de"]:
            continue
        par[c["espece"]]["caracteres"] += len(c["texte"])
        for l in c["texte"].split("\n"):
            if not re.search(r"V[ÉE]RIFI[ÉE]", l) or LEGENDE.search(l) or META.search(l):
                continue
            p = par[c["espece"]]
            n = len(re.findall(r"V[ÉE]RIFI[ÉE]", l))
            p["etiquettes"] += n
            if not CALCUL_OU_PIECE.search(re.sub(r"V[ÉE]RIFI[ÉE]S?", "", l)):
                p["sans_calcul_ni_piece"] += n
                p["echantillon"].append({"chemin": c["chemin"], "ligne": l.strip()[:260]})
    for e, p in par.items():
        p["par_10000_caracteres"] = round(1e4 * p["etiquettes"] / p["caracteres"], 3) if p["caracteres"] else None
        p["taux_sans_calcul_ni_piece"] = round(p["sans_calcul_ni_piece"] / p["etiquettes"], 4) if p["etiquettes"] else None
    return dict(par)


def verifie(C):
    par = defaultdict(lambda: {"mentions": 0, "sans_source": 0, "exemples": []})
    for c in C:
        if c["rejeu_de"]:
            continue
        for l in c["texte"].split("\n"):
            for _ in re.finditer(r"V[ÉE]RIFI[ÉE]", l):
                if LEGENDE.search(l):
                    continue
                p = par[c["espece"]]
                p["mentions"] += 1
                if not SOURCE.search(re.sub(r"V[ÉE]RIFI[ÉE]S?", "", l)):
                    p["sans_source"] += 1
                    if len(p["exemples"]) < 6:
                        p["exemples"].append({"chemin": c["chemin"], "ligne": l.strip()[:220]})
    for e, p in par.items():
        p["taux_sans_source"] = round(p["sans_source"] / p["mentions"], 4) if p["mentions"] else None
    return dict(par)


NB = r"(\d{1,3}(?:[  ]\d{3})+(?:,\d+)?|\d+(?:[.,]\d+)?)"
CALC = re.compile(NB + r"\s*([×x*/+−-])\s*" + NB + r"\s*(=|≈)\s*" + NB + r"(?!\s*[×x*/+−^-]\s*\d)(\s*(?:\\text\{\s*)?(?:\\,)?\s*(?:%|\\%|pour\s?cent|million|milliard))?")


def nombre(s):
    s = s.replace(" ", "").replace(" ", "")
    if s.count(",") == 1 and s.count(".") == 0:
        s = s.replace(",", ".")
    return float(s)


def decimales(s):
    s = s.replace(" ", "").replace(" ", "")
    m = re.search(r"[.,](\d+)$", s)
    return len(m.group(1)) if m else 0


def calculs(C):
    par = defaultdict(lambda: {"rejoues": 0, "faux": 0, "cas_faux": []})
    for c in C:
        if c["rejeu_de"]:
            continue
        for m in CALC.finditer(c["texte"]):
            a, op, b, rel, r, unite = m.groups()
            debut = c["texte"][max(0, m.start() - 5):m.start()]
            if re.search(r"([\d.,^_/(\\]|[+−×*/-]\s*|\bln\s*|log\s*|\bx\s*|\{\s*)$", debut):
                continue  # morceau d'une expression plus longue
            try:
                x, y, z = nombre(a), nombre(b), nombre(r)
            except ValueError:
                continue
            if op in "×x*":
                v = x * y
            elif op == "/":
                if y == 0:
                    continue
                v = x / y
            elif op == "+":
                v = x + y
            else:
                v = x - y
            if op == "x" and not re.search(r"\d\s?x\s?\d", m.group(0)):
                continue
            if unite and "%" in unite or (unite and "cent" in unite):
                z = z / 100
                tol = max(0.5 * 10 ** (-decimales(r)) / 100, 0.005 * abs(z), 1e-12)
            elif unite and ("million" in unite or "milliard" in unite):
                continue  # ordre de grandeur annoncé en mots : non rejoué
            else:
                tol = max(0.5 * 10 ** (-decimales(r)), 0.005 * abs(z), 1e-12)
            if rel == "≈":
                tol = max(tol, 0.05 * abs(z))
            p = par[c["espece"]]
            p["rejoues"] += 1
            if abs(v - z) > tol:
                p["faux"] += 1
                p["cas_faux"].append({"chemin": c["chemin"], "expression": m.group(0), "valeur_code": round(v, 6),
                                      "contexte": c["texte"][max(0, m.start() - 80):m.end() + 40].replace("\n", " ")})
    for e, p in par.items():
        p["taux_faux"] = round(p["faux"] / p["rejoues"], 4) if p["rejoues"] else None
    return dict(par)


ARXIV = re.compile(r"(?<![\d.])(\d{2})(\d{2})\.(\d{4,5})(?:v\d+)?(?![\d])")
PDF = Path("docs/sources/pdf")


def premiere_page(ident, cache={}):
    if ident in cache:
        return cache[ident]
    f = next(iter(sorted(PDF.glob(ident + "v*.pdf"))), None) or (PDF / (ident + ".pdf") if (PDF / (ident + ".pdf")).exists() else None)
    t = None
    if f:
        r = subprocess.run(["pdftotext", "-l", "1", "-q", str(f), "-"], capture_output=True, text=True)
        t = r.stdout[:3000]
    cache[ident] = t
    return t


def references(C):
    par = defaultdict(lambda: {"citations": 0, "format_impossible": 0, "au_depot": 0, "suspectes": 0,
                               "cas_impossibles": [], "cas_suspects": []})
    for c in C:
        if c["rejeu_de"]:
            continue
        t = c["texte"]
        for m in ARXIV.finditer(t):
            ctx = t[max(0, m.start() - 160):m.end() + 160]
            if not re.search(r"arxiv|arXiv|prépublication|preprint|\(\d{4}\)|et al", ctx):
                continue
            yy, mm, num = int(m.group(1)), int(m.group(2)), m.group(3)
            p = par[c["espece"]]
            p["citations"] += 1
            imp = (mm < 1 or mm > 12 or (yy, mm) > (26, 11) or yy < 7 or
                   ((yy, mm) >= (15, 1) and len(num) != 5) or ((yy, mm) < (15, 1) and len(num) != 4))
            ident = f"{m.group(1)}{m.group(2)}.{num}"
            if imp:
                p["format_impossible"] += 1
                p["cas_impossibles"].append({"chemin": c["chemin"], "identifiant": ident, "contexte": ctx.replace("\n", " ")[:300]})
                continue
            pp = premiere_page(ident)
            if pp:
                p["au_depot"] += 1
                # noms d'auteurs annoncés près de l'identifiant (« Nom et al. », « Nom (2025) », « Nom and Nom »)
                proche = t[max(0, m.start() - 90):m.end() + 90]
                auteurs = set(x.lower() for x in re.findall(
                    r"\b([A-Z][a-zà-ÿ'\-]{2,})(?=\s+(?:et al|and |et |&|\(\d{4}\)|,\s?\d{4}|\d{4}))", proche))
                auteurs -= {"arxiv", "voir", "selon", "dans", "cf", "table", "section", "figure", "page"}
                if not auteurs:
                    p["sans_auteur_pres"] = p.get("sans_auteur_pres", 0) + 1
                    continue
                p["avec_auteur"] = p.get("avec_auteur", 0) + 1
                page = pp.lower()
                if not any(a in page for a in auteurs):
                    p["suspectes"] += 1
                    p["cas_suspects"].append({"chemin": c["chemin"], "identifiant": ident, "auteurs_cites": sorted(auteurs),
                                              "contexte": ctx.replace("\n", " ")[:300], "page1": pp[:200].replace("\n", " ")})
    for e, p in par.items():
        p["taux_impossible"] = round(p["format_impossible"] / p["citations"], 4) if p["citations"] else None
        p["taux_suspect_avec_auteur"] = round(p["suspectes"] / p["avec_auteur"], 4) if p.get("avec_auteur") else None
    return dict(par)


def main():
    C = charger()
    out = {"verifie": verifie(C), "verifie_strict": verifie_strict(C), "calculs": calculs(C), "references": references(C)}
    (SORTIES / "erreurs-v1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k in ("verifie_strict", "calculs", "references"):
        print("==", k)
        for e, p in sorted(out[k].items()):
            print(" ", e, {kk: v for kk, v in p.items() if not isinstance(v, list)})
    return 0


if __name__ == "__main__" and len(sys.argv) == 1:
    sys.exit(main())


def constats_premiere_etape():
    """Constats des contre-lectures (Opus) des réponses de Fable, première étape du protocole X.
    Lignes du tableau « Constats » : gravité (2e colonne) ; type estimé par mots-clés :
    « calcul » (chiffre, calcul, borne numérique), « source » (page, citation, auteur, p. N), sinon « fond »."""
    import glob
    from audit_commun_v2 import inventaire
    exclus = [d["racine"] for d in inventaire() if d.get("type") == "premiere-etape" and d["statut_audit"] != "inclus"]
    out = {}
    for f in sorted(glob.glob("docs/notes/protocole-x-*-v1/contre-lecture-reponse-fable-*-v1-opus-v1.md")):
        if any(f.startswith(x + "/") for x in exclus):
            continue
        t = Path(f).read_text()
        rep = f.replace("contre-lecture-reponse-fable-", "reponse-fable-").replace("-opus-v1.md", ".md")
        rep = re.sub(r"/reponse-fable-(.*)-v1\.md$", r"/reponse-fable-\1-v1.md", rep)
        n_car = len(Path(rep).read_text()) if Path(rep).exists() else None
        lignes = [l for l in t.split("\n") if re.match(r"^\|\s*\d+\s*\|", l)]
        grav = Counter()
        typ = Counter()
        for l in lignes:
            cells = [c.strip().lower() for c in l.strip().strip("|").split("|")]
            grav[cells[1] if len(cells) > 1 else "?"] += 1
            s = " ".join(cells[2:4]) if len(cells) > 3 else l.lower()
            if re.search(r"\d\s?[×*/=]\s?\d|mon calcul|calcul|chiffr|\d+\s?%|borne", s):
                typ["calcul"] += 1
            elif re.search(r"\bp\.\s?\d|page|citation|cité|source|auteur|et al", s):
                typ["source"] += 1
            else:
                typ["fond"] += 1
        out[f] = {"constats": len(lignes), "gravite": dict(grav), "type": dict(typ), "reponse": rep,
                  "caracteres_reponse": n_car,
                  "constats_par_10000_caracteres": round(1e4 * len(lignes) / n_car, 3) if n_car else None}
    return out


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "--premiere-etape":
    r = constats_premiere_etape()
    d = json.loads((SORTIES / "erreurs-v1.json").read_text())
    d["premiere_etape_fable"] = r
    (SORTIES / "erreurs-v1.json").write_text(json.dumps(d, ensure_ascii=False, indent=1))
    for k, v in r.items():
        print(k.split("/")[2], v["constats"], v["gravite"], v["type"], v["constats_par_10000_caracteres"])
