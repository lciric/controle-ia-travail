"""Contrôle à blanc, sur une COPIE des registres, des lignes que la session mère s'apprête à inscrire pour P3-bis (v1).

Pourquoi : une ligne du registre des préalables ne se corrige jamais (R12 ; une seconde ligne de la même clé donne
`ligne-double`) ; un fichier de décision scellé ne se réécrit pas. Une faute de forme découverte par la vraie garde serait
donc définitive. Ce contrôle rejoue la garde du module scellé (`ouverture_p3bis_v3.garde_ouverture`, code de S) sur une
copie temporaire, avant toute inscription, et imprime les lignes exactes à inscrire.

Ce qu'il ne fait jamais : ouvrir un paquet, lire un paquet, écrire dans la racine donnée, écrire au journal des ouvertures,
lire un texte cité (les fichiers cités sont reliés par lien symbolique, seulement hachés par la garde).

    PYTHONPATH=<src du module de S> python -B controle_prealables_p3bis_v1.py --racine <clone de main> --bac <dossier neuf> \
        --mode reduite|pleine|pleine-anticipee [--ecrits AAAA-MM-JJTHH:MM:SSZ] \
        [--decision <brouillon du fichier de décision> --date-ligne AAAA-MM-JJTHH:MM:SSZ] [--instant AAAA-MM-JJTHH:MM:SSZ]

`--ecrits D` : ajoute à la copie les trois lignes d'écrit datées D, qui citent le texte scellé de T0.7 (`PREREG_T07`) à son
empreinte calculée. `--decision B --date-ligne D` : place B à `docs/decisions/rendez-vous-P3-bis-vN.md` (N suivant) dans la
copie, l'y scelle et ajoute la ligne `RENDEZ-VOUS-P3BIS-N` datée D. `--instant` : instant de l'ouverture simulée (défaut :
une minute après la plus tardive des dates ajoutées, sinon l'horloge). Code 0 si la garde autoriserait le mode demandé, 2
sinon (refus imprimé, tous les défauts), 1 sur une erreur d'appel.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
import time
from pathlib import Path

from controle_ia.premier_test_ia import ouverture_p3bis_v3 as o
from controle_ia.scellement import sceller

COPIES = (o.REGISTRE_PREALABLES, o.REGISTRE_SCELLEMENTS, o.JOURNAL_OUVERTURES)


def relier(racine: Path, copie: Path, chemin: str) -> None:
    """Lien symbolique vers le fichier cité et son compagnon (s'ils existent), jamais une copie de leur contenu."""
    for c in (chemin, chemin + ".sha256"):
        src, dst = racine / c, copie / c
        if src.exists() and not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(src.resolve(), dst)


def main(argv) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", required=True)
    ap.add_argument("--bac", required=True)
    ap.add_argument("--mode", required=True, choices=o.MODES)
    ap.add_argument("--ecrits", default=None)
    ap.add_argument("--decision", default=None)
    ap.add_argument("--date-ligne", default=None)
    ap.add_argument("--instant", default=None)
    a = ap.parse_args(argv)
    racine, bac = Path(a.racine).resolve(), Path(a.bac)
    if bac.exists():
        print(f"ERREUR : {bac} existe déjà (R12)", file=sys.stderr)
        return 1
    if (a.decision is None) != (a.date_ligne is None):
        print("ERREUR : --decision et --date-ligne vont ensemble", file=sys.stderr)
        return 1
    copie = bac / "racine-copie"
    for r in COPIES:
        if (racine / r).is_file():
            (copie / r).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(racine / r, copie / r)
    (copie / "registres").mkdir(parents=True, exist_ok=True)
    pre = copie / o.REGISTRE_PREALABLES
    dates, a_inscrire = [], []
    if a.ecrits is not None:
        o.instant_utc(a.ecrits)
        sha7 = hashlib.sha256((racine / o.PREREG_T07).read_bytes()).hexdigest()
        a_inscrire += [f"| {k} | {a.ecrits} | {o.PREREG_T07} | {sha7} |" for k in o.CLES_ECRITS]
        dates.append(a.ecrits)
    if a.decision is not None:
        o.instant_utc(a.date_ligne)
        deja = sum(1 for x in (pre.read_text(encoding="utf-8").splitlines() if pre.exists() else [])
                   if o.RENDEZ_VOUS.fullmatch(o._cellules(x)[0] if x.strip().startswith("|") else ""))
        n = deja + 1
        chemin = o.FICHIER_DECISION.format(n=n)
        (copie / chemin).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(a.decision, copie / chemin)
        sha_d = sceller(copie / chemin)
        a_inscrire.append(f"| RENDEZ-VOUS-P3BIS-{n} | {a.date_ligne} | {chemin} | {sha_d} |")
        dates.append(a.date_ligne)
    if a_inscrire:
        avant = pre.read_bytes() if pre.exists() else b""
        with open(pre, "a", encoding="utf-8") as f:
            if avant and not avant.endswith(b"\n"):
                f.write("\n")
            f.write("\n".join(a_inscrire) + "\n")
    # fichiers cités par les lignes lues par la garde : liens symboliques (jamais lus ici)
    for r in (o.REGISTRE_PREALABLES, o.REGISTRE_SCELLEMENTS):
        if (copie / r).is_file():
            for brute in (copie / r).read_text(encoding="utf-8").splitlines():
                c = o._cellules(brute) if brute.strip().startswith("|") else []
                if len(c) == 4 and c[2] and not c[2].startswith("/") and ".." not in Path(c[2]).parts:
                    if r == o.REGISTRE_SCELLEMENTS and c[0] not in o.CLES_T07_LUES:
                        continue
                    if r == o.REGISTRE_SCELLEMENTS and c[0] in (o.SCORES_T07, o.SONDES_T07):
                        x = c[2] + ".sha256"                 # D8 : le compagnon seul ; le fichier de T0.7 n'est pas relié
                        if (racine / x).exists() and not (copie / x).exists():
                            (copie / x).parent.mkdir(parents=True, exist_ok=True)
                            os.symlink((racine / x).resolve(), copie / x)
                        continue
                    relier(racine, copie, c[2])
    if a.instant is not None:
        instant = o.instant_utc(a.instant)
    elif dates:
        instant = max(o.instant_utc(d) for d in dates) + 60
    else:
        instant = int(time.time())
    print(f"copie : {copie} ; ouverture simulée à {o.date_utc(instant)} ; mode demandé {a.mode}")
    for x in a_inscrire:
        print(f"LIGNE À INSCRIRE (telle quelle) : {x}")
    try:
        g = o.garde_ouverture(copie, a.mode, instant)
    except o.RefusOuverture as e:
        print(f"CONTRÔLE À BLANC : REFUS {e.code} : {e.texte}")
        return 2
    print(f"CONTRÔLE À BLANC : AUTORISÉ {g['mode']} ({g['chemin']}) ; appui {g['appui']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
