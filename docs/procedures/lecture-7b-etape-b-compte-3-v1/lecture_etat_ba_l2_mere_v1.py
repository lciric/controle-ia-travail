"""Lecture, par la session mère, du seul état de la ligne BA-L2 de la base (A) de T0.8 avant l'étape B de T0.7, v1.

Écrit le 2026-11-14 par le préparateur (modèle A), sur la décision de Lazar (R-2741, nœud N-C) : « la session mère lit, par
programme, le seul état BA-L2 » (exception explicite à son exclusion des lectures de 7b). Texte scellé de T0.7, l. 2183 : « La
session mère ne lance l'étape B qu'après avoir lu, dans le fichier scellé `diag/<run-mc>/base-a-t08.json` que cite la ligne
`LECTURE-T08-BASE-A` du registre, l'état de la ligne BA-L2 » ; si BA-L2 s'applique, ou si ce fichier ou cette ligne manque alors
que `ISSUE-MOTS-ET-COUT-T06` est inscrite, l'étape B attend le mot de Lazar.

Bibliothèque standard seule. N'écrit rien. N'affiche **que** l'état (s'applique, ne s'applique pas, illisible) et des motifs
sans valeur lue : jamais une aire, un nombre, une phrase ni un autre champ du fichier.

Contrôles, dans l'ordre :
  1. registre : exactement une ligne `LECTURE-T08-BASE-A`, au format `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |`, datée
     strictement avant l'instant ; présence de `ISSUE-MOTS-ET-COUT-T06` relevée (pour le cas « ligne absente ») ;
  2. fichier cité présent, empreinte égale à la ligne et à son compagnon ;
  3. JSON lisible ; champ désigné par `--cle-json` (défaut `lignes.BA-L2.s_applique`, forme que la consigne du développeur de la
     pièce « mots et coût » doit fixer) présent et booléen.

    python3 -I -B lecture_etat_ba_l2_mere_v1.py --racine R --registre REG [--cle-json lignes.BA-L2.s_applique] [--instant AAAA-MM-JJTHH:MM:SSZ]

Codes : 0 « ne s'applique pas » ; 3 « s'applique » (mot de Lazar avant l'étape B) ; 2 illisible ou refus (mot de Lazar si la
ligne ou le fichier manque alors que `ISSUE-MOTS-ET-COUT-T06` est inscrite ; sinon la mère lève la cause) ; 1 erreur d'appel.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CLE, ISSUE = "LECTURE-T08-BASE-A", "ISSUE-MOTS-ET-COUT-T06"
DATE, SHA = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"), re.compile(r"[0-9a-f]{64}")
FMT = "%Y-%m-%dT%H:%M:%SZ"


class Illisible(Exception):
    pass


def _instant(date: str) -> int:
    return int(datetime.strptime(date, FMT).replace(tzinfo=timezone.utc).timestamp())


def lignes_de(registre: Path, cle: str) -> list[list[str]]:
    sortie = []
    for brute in Path(registre).read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in brute.strip().strip("|").split("|")]
        if c and c[0] == cle:
            sortie.append(c)
    return sortie


def etat_ba_l2(racine: Path, registre: Path, cle_json: str, instant: int) -> bool:
    lignes = lignes_de(registre, CLE)
    if len(lignes) != 1:
        issue = len(lignes_de(registre, ISSUE)) > 0
        raise Illisible(f"{len(lignes)} ligne(s) {CLE} au registre, une attendue"
                        + (f" ; {ISSUE} est inscrite : l'étape B attend le mot de Lazar (T0.7, l. 2183)" if issue else ""))
    c = lignes[0]
    if len(c) != 4 or not DATE.fullmatch(c[1]) or not SHA.fullmatch(c[3]) or not c[2] or c[2].startswith("/") or ".." in Path(c[2]).parts:
        raise Illisible(f"ligne {CLE} hors du format | CLÉ | date | chemin relatif | sha256 |")
    if not _instant(c[1]) < instant:
        raise Illisible(f"ligne {CLE} datée {c[1]}, pas strictement antérieure à {datetime.fromtimestamp(instant, timezone.utc).strftime(FMT)}")
    f = Path(racine) / c[2]
    if not f.is_file():
        raise Illisible(f"{c[2]} absent sous la racine : mot de Lazar (T0.7, l. 2183) si {ISSUE} est inscrite")
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    comp = Path(str(f) + ".sha256")
    lu = (comp.read_text(encoding="utf-8").split() or [""])[0] if comp.is_file() else ""
    if h != c[3] or h != lu:
        raise Illisible(f"{c[2]} : empreinte {h[:12]}… ≠ ligne ({c[3][:12]}…) ou compagnon ({lu[:12] or 'absent'}…)")
    try:
        doc = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Illisible(f"{c[2]} : JSON illisible ({type(e).__name__})") from None
    x = doc
    for part in cle_json.split("."):
        if not isinstance(x, dict) or part not in x:
            raise Illisible(f"champ {cle_json!r} absent de {c[2]}")
        x = x[part]
    if not isinstance(x, bool):
        raise Illisible(f"champ {cle_json!r} de type {type(x).__name__}, booléen attendu (valeur non affichée)")
    return x


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--racine", required=True)
    p.add_argument("--registre", required=True)
    p.add_argument("--cle-json", default="lignes.BA-L2.s_applique")
    p.add_argument("--instant", default=None)
    a = p.parse_args(argv)
    instant = _instant(a.instant) if a.instant else int(time.time())
    try:
        s = etat_ba_l2(Path(a.racine), Path(a.registre), a.cle_json, instant)
    except Illisible as e:
        print(f"ÉTAT BA-L2 : illisible — {e}")
        return 2
    if s:
        print("ÉTAT BA-L2 : s'applique — l'étape B attend le mot de Lazar ; réserve R-BA1 à côté de toute phrase sur le critère 3")
        return 3
    print("ÉTAT BA-L2 : ne s'applique pas")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except (OSError, ValueError) as e:
        print(f"ERREUR D'APPEL : {type(e).__name__} : {e}")
        sys.exit(1)
