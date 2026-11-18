"""Contrôle de dépôt d'UN fichier de codage, avant scellement (grille brouillon 3, section 4.5).

Gestes : complétude (25 lignes de geste et une ligne AVEUGLE par billet), modalités de la grille,
doublons ; appui exigé pour toute modalité de l'indicateur ; chaque fragment d'appui (séparés par
« […] », 25 mots au plus, deux au plus) retrouvé dans la copie neutre après la normalisation de la
grille ; pour les modalités d'en-tête, appui commençant avant la borne.
Objections : complétude contre la liste des commentaires codables, classes O0–O13, doublons.

Usage :
  python controler_depot_v1.py gestes --grille G --fichier F --copies DOSSIER_BILLETS [--sortie R.json]
  python controler_depot_v1.py objections --fichier F --codables cles/commentaires-codables.json [--sortie R.json]
Code de sortie 0 si le dépôt est accepté, 2 sinon.
"""
import argparse
import json
import os
import re
import sys

BORNE = "⟦FIN DE L'EN-TÊTE — 250 MOTS⟧"
EN_TETE = {"G02": {"premier-paragraphe", "en-tête"}, "G04": {"bloc-étiqueté", "liste-non-étiquetée"},
           "G05": {"avec-comparaison", "seul"}, "G10": {"en-tête"}, "G11": {"figure-de-résultat"}}
PARIS = {"bien-noté", "peu-noté", "ne-sait-pas"}
CLASSES_O = [f"O{i}" for i in range(14)]
SEP = " […] "


class Refus(Exception):
    pass


def norm(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_\\]", "", t)
    return " ".join(t.split())


def lire_grille(p):
    t = open(p, encoding="utf-8").read()
    g = {}
    for m in re.finditer(r"^### (G\d{2})\. .*?$(.*?)(?=^### |^## |^---|\Z)", t, re.M | re.S):
        c = m.group(2)
        g[m.group(1)] = {
            "modalites": re.findall(r"`([^`]+)`", re.search(r"^- \*\*Modalités\*\* : (.*)$", c, re.M).group(1)),
            "indicateur": set(re.findall(r"`([^`]+)`", re.search(r"^- \*\*Indicateur\*\* : (.*)$", c, re.M).group(1))),
            "analyse": re.search(r"^- \*\*Analyse\*\* : (comparée|descriptive)", c, re.M).group(1),
        }
    if sorted(g) != [f"G{i:02d}" for i in range(1, 26)]:
        raise Refus("grille : gestes G01 à G25 attendus")
    return g


def lire_jsonl(p):
    out = []
    for k, l in enumerate(open(p, encoding="utf-8"), 1):
        if l.strip():
            try:
                out.append(json.loads(l))
            except json.JSONDecodeError:
                raise Refus(f"ligne {k} illisible")
    return out


def controler_gestes(grille, fichier, copies):
    G = lire_grille(grille)
    billets = sorted(f[:-3] for f in os.listdir(copies) if f.endswith(".md"))
    textes = {}
    refus, vus, aveugle, codeurs = [], {}, {}, set()
    for l in lire_jsonl(fichier):
        codeurs.add(l.get("codeur"))
        b, g = l.get("billet"), l.get("geste")
        if b not in billets:
            refus.append(f"billet inconnu {b}")
            continue
        if g == "AVEUGLE":
            if b in aveugle:
                refus.append(f"ligne AVEUGLE en double {b}")
            if not isinstance(l.get("reconnu"), bool) or l.get("pari_statut") not in PARIS:
                refus.append(f"ligne AVEUGLE mal formée {b}")
            aveugle[b] = l
            continue
        if g not in G:
            refus.append(f"geste inconnu {b} {g}")
            continue
        if (b, g) in vus:
            refus.append(f"doublon {b} {g}")
            continue
        m = l.get("modalite")
        vus[(b, g)] = m
        if m not in G[g]["modalites"]:
            refus.append(f"modalité hors grille {b} {g} {m!r}")
            continue
        if not isinstance(l.get("doute"), bool):
            refus.append(f"doute absent {b} {g}")
        appui = (l.get("appui") or "").strip()
        if not appui:
            if m in G[g]["indicateur"]:
                refus.append(f"appui absent pour une modalité de l'indicateur {b} {g} {m}")
            continue
        frags = [f.strip() for f in appui.split(SEP)]
        if len(frags) > 2:
            refus.append(f"plus de deux fragments {b} {g}")
            continue
        if b not in textes:
            textes[b] = norm(open(os.path.join(copies, f"{b}.md"), encoding="utf-8").read())
        src = textes[b]
        pos_borne = src.find(norm(BORNE))
        for f in frags:
            nf = norm(f)
            if len(nf.split()) > 25:
                refus.append(f"fragment de plus de 25 mots {b} {g}")
                continue
            pos = src.find(nf)
            if not nf or pos < 0:
                refus.append(f"appui introuvable dans la copie {b} {g}")
                continue
        if g in EN_TETE and m in EN_TETE[g]:
            p0 = src.find(norm(frags[0]))
            if p0 >= 0 and pos_borne >= 0 and p0 > pos_borne:
                refus.append(f"appui d'en-tête après la borne {b} {g}")
    for b in billets:
        for g in G:
            if (b, g) not in vus:
                refus.append(f"ligne absente {b} {g}")
        if b not in aveugle:
            refus.append(f"ligne AVEUGLE absente {b}")
    if len(codeurs) != 1:
        refus.append(f"un seul codeur attendu par fichier : {sorted(map(str, codeurs))}")
    return {"fichier": fichier, "billets": len(billets), "lignes_geste": len(vus), "lignes_aveugle": len(aveugle),
            "refus": refus, "accepte": not refus}


def controler_objections(fichier, codables_p):
    cod = json.load(open(codables_p, encoding="utf-8"))["codables"]
    attendus = {(b, c) for b, cs in cod.items() for c in cs}
    refus, vus, codeurs = [], set(), set()
    for l in lire_jsonl(fichier):
        codeurs.add(l.get("codeur"))
        k = (l.get("billet"), l.get("commentaire"))
        if k not in attendus:
            refus.append(f"commentaire inconnu ou réponse d'auteur {k}")
        elif k in vus:
            refus.append(f"doublon {k}")
        elif l.get("classe") not in CLASSES_O:
            refus.append(f"classe hors grille {k} {l.get('classe')!r}")
        vus.add(k)
    for k in sorted(attendus - vus):
        refus.append(f"ligne absente {k}")
    if len(codeurs) != 1:
        refus.append("un seul codeur attendu par fichier")
    return {"fichier": fichier, "attendus": len(attendus), "lignes": len(vus), "refus": refus, "accepte": not refus}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("passe", choices=["gestes", "objections"])
    for a in ("grille", "fichier", "copies", "codables", "sortie"):
        ap.add_argument("--" + a)
    A = ap.parse_args()
    r = (controler_gestes(A.grille, A.fichier, A.copies) if A.passe == "gestes"
         else controler_objections(A.fichier, A.codables))
    if A.sortie:
        json.dump(r, open(A.sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ACCEPTÉ" if r["accepte"] else f"REFUSÉ : {len(r['refus'])} motifs ; premiers : {r['refus'][:5]}")
    return 0 if r["accepte"] else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Refus as e:
        print("REFUS :", e)
        sys.exit(2)
