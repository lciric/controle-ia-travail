#!/usr/bin/env python3
"""Extraits nettoyés d'un brouillon du texte du bras A, pour un rédacteur appelé par l'API — version 1.

Usage : extraits_nettoyes_brouillon_v1.py SOURCE PLAGES SORTIE TABLE [--tronque L:TETE:QUEUE …]
  PLAGES : « 1-12,186-210,… » (lignes de SOURCE, bornes comprises).
  SORTIE : texte des extraits, chaque ligne préfixée « L<numéro>␉ » ; une ligne tronquée porte « ⟦…coupé…⟧ » au milieu.
  TABLE  : JSON {marque: texte d'origine} pour rétablir les originaux (jamais envoyé).
Chaque passage refusé par la garde de motifs de relecture_fable_api_v5 (nom, identifiant de session, UUID, courriel,
termes de chemin) est remplacé par une marque ⟦Xn⟧ ; la même chaîne reçoit toujours la même marque. Le programme
refuse (code 2) si la garde n'est pas vide sur la sortie, ou si une marque existe déjà dans la source.
"""
import json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from controle_ia import relecture_fable_api_v5 as r

MOT = re.compile(r"[^\s`|()\[\]«»\"',;]+")


def sans(t):
    return r.sans_accents(t)


def nettoyer(lignes):
    table, inverse = {}, {}
    def marque(prefixe, texte):
        if texte not in inverse:
            n = sum(1 for k in table if k.startswith("⟦" + prefixe)) + 1
            m = f"⟦{prefixe}{n}⟧"
            table[m], inverse[texte] = texte, m
        return inverse[texte]
    sortie = []
    for ligne in lignes:
        for motif, p in ((r.MOTIF_SESSION, "S"), (r.MOTIF_UUID, "U"), (r.MOTIF_COURRIEL, "C")):
            ligne = motif.sub(lambda m: marque(p, m.group(0)), ligne)
        def mot(m):
            t = m.group(0); s = sans(t)
            if any(n in s for n in r.NOMS_INTERDITS):
                return marque("D", t) if s.strip(".:*") in ("lazar", "ciric") else marque("N", t)
            if any(mt.search(s) for mt in r.TERMES_PARTOUT.values()):
                return marque("T", t)
            if any(x in s for x in r.TERMES_DE_CHEMIN) and (any(c in s for c in "/\\_-") or r.EXTENSION.search(s) or "`" in t):
                return marque("P", t)
            return t
        ligne = r.CODE_EN_LIGNE.sub(lambda m: marque("P", m.group(0)) if any(x in sans(m.group(1)) for x in r.TERMES_DE_CHEMIN) else m.group(0), ligne)
        ligne = MOT.sub(mot, ligne)
        sortie.append(ligne)
    return sortie, table


def main(argv):
    src, plages, sortie, tab = argv[:4]
    tronques = {}
    for a in argv[4:]:
        if a.startswith("--tronque="):
            n, tete, queue = a.split("=", 1)[1].split(":"); tronques[int(n)] = (int(tete), int(queue))
    texte = Path(src).read_text(encoding="utf-8")
    if "⟦" in texte or "⟧" in texte:
        print("refus : la source porte déjà une marque", file=sys.stderr); return 2
    toutes = texte.split("\n")
    choisies = []
    for pl in plages.split(","):
        a, b = (int(x) for x in pl.split("-"))
        choisies += list(range(a, b + 1))
    brutes = []
    for n in choisies:
        l = toutes[n - 1]
        if n in tronques:
            t, q = tronques[n]
            l = l[:t] + " ⟦…coupé…⟧ " + l[-q:]
        brutes.append(l)
    propres, table = nettoyer(brutes)
    lignes = [f"L{n}\t{l}" for n, l in zip(choisies, propres)]
    out = "\n".join(lignes) + "\n"
    reste = r.garde_motifs([("extraits", out)])
    if reste:
        print("refus : garde non vide après nettoyage :", json.dumps(reste[:20], ensure_ascii=False), file=sys.stderr); return 2
    Path(sortie).write_text(out, encoding="utf-8")
    Path(tab).write_text(json.dumps(table, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"lignes": len(lignes), "signes": len(out), "marques": len(table)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
