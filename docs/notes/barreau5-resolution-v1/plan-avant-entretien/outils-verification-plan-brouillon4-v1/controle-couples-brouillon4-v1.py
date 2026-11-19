#!/usr/bin/env python3
"""Vérification du brouillon 4 (barreau 5, plan « sabotage ou empreinte ») : contrôle des couples appliqués, v1.

Écrit par le vérificateur (Claude Opus 5.5) le 20 novembre 2026. Ne lit que des textes du dépôt (aucune donnée du
programme) ; n'écrit rien : tout sort sur la sortie standard.
  1. Les 15 couples « toujours » de ma vérification du brouillon 3 (lus dans mon programme scellé de couples) : leur
     « après » est-il présent à l'octet dans le brouillon 4 ? Pour ceux qui ne le sont pas, la reprise que la table des
     corrections décrit est cherchée par des fragments exacts.
  2. Les 39 couples du code (`couples-du-code-pour-brouillon4-v1.md`) : rejoués en mémoire, dans leur ordre, sur le
     brouillon 3 et son devis après mes 15 couples (chaque « avant » unique au moment où il s'applique) ; puis leur
     « après » est cherché à l'octet dans le brouillon 4 ou son devis.
  3. Restes et marques : chaînes que le compte rendu de la fabrique signale, marques « [à confirmer par le rapport v4] ».
"""
from __future__ import annotations

import hashlib
import re
import runpy
from pathlib import Path

ICI = Path(__file__).resolve().parent
PLAN = ICI.parent
RACINE = PLAN.parents[3]
T3 = RACINE / "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md"
T4 = RACINE / "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md"
DV3 = PLAN / "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md"
DV4 = PLAN / "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md"
CODE = PLAN / "couples-du-code-pour-brouillon4-v1.md"
MIENS = PLAN / "contre-lecture-outils-plan-brouillon3-v1" / "couples-verification-brouillon3-v1.py"
ATTENDU = {T3: "525f338e", T4: "dbe66dc9", DV3: "7ac56a7b", DV4: "084cd547", CODE: "1e929542", MIENS: "0c98ad03"}

# fragments exacts qui disent la reprise, pour les couples « toujours » dont l'« après » n'est plus à l'octet
REPRISES = {
    "V-M2a": ["P(a, b) = δ̄_a·δ̄_b, produit des déplacements moyens", "mondes C21, C22 et C34"],
    "V-M1a": ["hypothèse de travail, que ce plan ne vérifie pas", "C'était le défaut de l'étalon du brouillon 3"],
    "V-M1b": ["et si la divergence propre du saboteur est indépendante de celles des deux membres édités"],
    "V-M4a": ["ramène après coup les deux membres édités, le sur-saboteur et le jumeau, à la même poussée"],
    "V-M5a": ["| V9, 500 | force sur la seule part propre à la famille", "| V10, 200 | dans chaque monde, deux familles"],
    "V-m3a": ["une famille absente de E1, de E2a ou de E2b seulement ne manque qu'à celle-là ; chaque demi-épreuve de "
              "E2 compte ses propres familles"],
}
MOTIF = re.compile(r"#### Couple (?P<nom>[CD]-\d+[a-z]) — (?P<piece>T|DV) — [^\n]*\n\nAvant :\n\n```text\n(?P<avant>.*?)"
                   r"\n```\n\nAprès :\n\n```text\n(?P<apres>.*?)\n```\n", re.S)
RESTES = ["E1, E2 et E3", "à norme égale", "sonde apprise contre les jumeaux", "lun. 23", "mer. 25",
          "[à confirmer par le rapport v4]", "brouillon 3 n'a plus de série à norme égale"]


def lire(p: Path) -> str:
    t = p.read_text(encoding="utf-8")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print(f"- {p.relative_to(RACINE)} : {h[:16]}… ({'attendue' if h.startswith(ATTENDU[p]) else 'INATTENDUE'})")
    return t


def main():
    print("# Contrôle des couples appliqués au brouillon 4 — sortie (v1)\n")
    t3, t4, dv3, dv4, code = lire(T3), lire(T4), lire(DV3), lire(DV4), lire(CODE)
    lire(MIENS)
    miens = [c for c in runpy.run_path(str(MIENS), run_name="verificateur")["COUPLES"] if c[2] == "toujours"]

    print("\n## 1. Mes 15 couples « toujours »\n")
    copie3 = t3
    oui = non = 0
    for ident, _constat, _g, _f, avant, apres in miens:
        n_av = copie3.count(avant)
        copie3 = copie3.replace(avant, apres, 1)
        present = t4.count(apres)
        if present:
            oui += 1
            print(f"{ident:6s} « avant » unique au brouillon 3 : {n_av == 1} ; « après » à l'octet au brouillon 4 : oui ({present})")
        else:
            non += 1
            frag = [(f[:60] + "…", t4.count(f)) for f in REPRISES.get(ident, [])]
            print(f"{ident:6s} « avant » unique au brouillon 3 : {n_av == 1} ; « après » à l'octet au brouillon 4 : non ; "
                  f"reprise : {frag}")
    print(f"\nà l'octet : {oui} ; repris : {non}")

    print("\n## 2. Les 39 couples du code\n")
    couples = [m.groupdict() for m in MOTIF.finditer(code)]
    print(f"couples lus : {len(couples)}")
    piece = {"T": copie3, "DV": dv3}
    lit = 0
    for c in couples:
        n_av = piece[c["piece"]].count(c["avant"])
        piece[c["piece"]] = piece[c["piece"]].replace(c["avant"], c["apres"], 1)
        cible = t4 if c["piece"] == "T" else dv4
        present = cible.count(c["apres"])
        lit += present > 0
        print(f"{c['nom']:5s} {c['piece']:2s} « avant » unique au moment d'appliquer : {n_av == 1} ; "
              f"« après » à l'octet au brouillon 4 : {'oui' if present else 'non'}")
    print(f"\nà l'octet : {lit} sur {len(couples)}")

    print("\n## 3. Restes et marques\n")
    for r in RESTES:
        print(f"« {r} » : texte {t4.count(r)} ; devis {dv4.count(r)}")
        for i, l in enumerate(t4.split("\n"), 1):
            if r in l and r not in ("[à confirmer par le rapport v4]",):
                j = l.index(r)
                print(f"    texte l. {i} : …{l[max(0, j - 70):j + len(r) + 50]}…")


if __name__ == "__main__":
    main()
