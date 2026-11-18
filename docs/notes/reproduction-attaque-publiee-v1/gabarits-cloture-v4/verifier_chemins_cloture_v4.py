# v4 : renommé (R12), contenu inchangé depuis la v3
# v3 : corrections de la contre-lecture de la v2 (8 constats)
# v2 : corrections de la contre-lecture de la v1 (14 constats)
"""Vérification des chemins de la clôture — témoin de Bailey, addendum 7, § 3 (v4).

v3 : renommé `verifier_chemins_cloture_v4.py` (R12 : nouvelle version, nouveau nom) ; logique inchangée depuis la v2.
Le rapport de chaque lecteur (paramètre `RAPPORTS` de `commandes-cloture-bailey-v4.sh`) passe par `--autre` en e2 ;
le refus des chemins ignorés par git est joué par `commandes-cloture-bailey-v4.sh` (e2), hors de ce script.

Règle vérifiée (§ 3, puce « Clôture de la confirmation ») : « avant le premier `--calculer-attendu`, la session fixe ces
chemins et vérifie par programme (chemins résolus, `Path.resolve().is_relative_to`) qu'aucun chemin d'attendu, de
sortie, de `<P>`, du dossier factice, de son attendu et de sa sortie, ni de la note de clôture n'est sous
`<racine>/src` ni sous aucun des dossiers donnés à une lecture ; un chemin qui échoue est remplacé avant toute
écriture ; tout chemin neuf pris ensuite […] passe la même vérification avant d'être écrit ». Le § 3 exige encore des
chemins absolus (« tous chemins absolus ») et un `<P>` « absent ou vide ».

v2 : `--pousse X` (répétable) nomme un chemin que la session ajoute ensuite à la branche (`git add`, hors de `src/`,
§ 3 : « `add`, `commit` et `push` hors de `src/` restent permis ») pour que le contrôle final puisse être joué dans un
arbre recloné (« après récupération par git de chaque sortie, de son compagnon et de son attendu ») : il doit être
absolu et résolu sous `<racine>`, hors de `<racine>/src`, de `<racine>/.git` et de chaque dossier lu. `--autre`
couvre aussi le chemin du rapport d'un lecteur (consigne du lecteur, `<CHEMIN_RAPPORT>`), vérifié avant le lancement.

Bibliothèque standard seulement. Ne lit aucun fichier, n'écrit rien : seuls `Path.resolve()`, `is_relative_to`,
`exists`, `is_dir` et la liste des entrées de `<P>` (s'il existe) sont joués. Ne s'appuie sur aucun code du dépôt.

Usage (tous chemins absolus ; `--dossier-lu`, `--attendu`, `--sortie` et `--autre` se répètent) :
    python3 -I verifier_chemins_cloture_v4.py --racine R --dossier-lu D1 [--dossier-lu D2] \
        --attendu A1 [--attendu A2] --sortie S1 [--sortie S2] --cache-p P \
        --factice-dossier F --factice-attendu FA --factice-sortie FS --note N [--autre X …] [--pousse Y …]

Rend sur la sortie standard « conforme » (code 0), ou une ligne « écarts : n » suivie d'un écart par ligne (code 1).
Arguments manquants : code 2 (argparse).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _resolu(chemin: str) -> Path:
    return Path(chemin).resolve()


def ecarts(racine: str, dossiers_lus: list[str], verifies: list[tuple[str, str]], cache_p: str | None,
           pousses: list[str] | None = None) -> list[str]:
    """Liste des écarts ; vide si conforme. `verifies` : couples (rôle, chemin) à tenir hors de `<racine>/src` et hors
    de chaque dossier lu. `pousses` : chemins à ajouter à la branche, tenus en outre sous `<racine>` et hors de
    `<racine>/.git` (et vérifiés hors de `src/` et des dossiers lus comme les autres)."""
    out: list[str] = []
    pousses = list(pousses or [])
    verifies = verifies + [("chemin poussé", x) for x in pousses]
    for role, ch in [("racine", racine)] + [("dossier lu", d) for d in dossiers_lus] + verifies:
        if not Path(ch).is_absolute():
            out.append(f"{role} : chemin non absolu ({ch})")
    src = _resolu(racine) / "src"
    lus = [(d, _resolu(d)) for d in dossiers_lus]
    for role, ch in verifies:
        r = _resolu(ch)
        if r.is_relative_to(src):
            out.append(f"{role} : chemin résolu sous <racine>/src ({ch} -> {r})")
        for d, rd in lus:
            if r.is_relative_to(rd):
                out.append(f"{role} : chemin résolu sous le dossier lu {d} ({ch} -> {r})")
    rr = _resolu(racine)
    for ch in pousses:
        r = _resolu(ch)
        if not r.is_relative_to(rr):
            out.append(f"chemin poussé : chemin résolu hors de <racine> ({ch} -> {r})")
        elif r.is_relative_to(rr / ".git"):
            out.append(f"chemin poussé : chemin résolu sous <racine>/.git ({ch} -> {r})")
    if cache_p is not None:
        p = Path(cache_p)
        if p.exists() and not (p.is_dir() and not any(p.iterdir())):
            out.append(f"<P> : ni absent ni répertoire vide ({cache_p})")
    return out


def principal(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Vérification des chemins de la clôture (addendum 7, § 3).")
    ap.add_argument("--racine", required=True)
    ap.add_argument("--dossier-lu", action="append", required=True, dest="dossiers_lus")
    ap.add_argument("--attendu", action="append", required=True, dest="attendus")
    ap.add_argument("--sortie", action="append", required=True, dest="sorties")
    ap.add_argument("--cache-p", required=True)
    ap.add_argument("--factice-dossier", required=True)
    ap.add_argument("--factice-attendu", required=True)
    ap.add_argument("--factice-sortie", required=True)
    ap.add_argument("--note", required=True)
    ap.add_argument("--autre", action="append", default=[], dest="autres",
                    help="tout autre chemin écrit pendant la clôture (journal de consignation, chemin neuf, "
                         "rapport d'un lecteur)")
    ap.add_argument("--pousse", action="append", default=[], dest="pousses",
                    help="chemin ajouté ensuite à la branche : sous <racine>, hors de src/, de .git/ et des dossiers lus")
    a = ap.parse_args(argv)
    verifies = ([("attendu", x) for x in a.attendus] + [("sortie", x) for x in a.sorties]
                + [("<P>", a.cache_p), ("dossier factice", a.factice_dossier),
                   ("attendu factice", a.factice_attendu), ("sortie factice", a.factice_sortie),
                   ("note de clôture", a.note)] + [("autre", x) for x in a.autres])
    liste = ecarts(a.racine, a.dossiers_lus, verifies, a.cache_p, a.pousses)
    if not liste:
        print("conforme")
        return 0
    print(f"écarts : {len(liste)}")
    for e in liste:
        print(e)
    return 1


if __name__ == "__main__":
    sys.exit(principal())
