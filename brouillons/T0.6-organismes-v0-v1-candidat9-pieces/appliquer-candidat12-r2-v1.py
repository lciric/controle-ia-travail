"""Candidat 12, révision 2 (nouveau fichier, R12) : le marqueur `<<TESTS_ATTENDUS_T06>>` est rempli par la voie (a) décidée par la mère (8 novembre ~07:10Z) : **1914**, avec sa dérivation et sa réserve.
Source : `candidat12.md` (`379328fa…`, vérifiée avant tout). Chaque « ancien » doit se trouver exactement une fois, sinon arrêt sans rien écrire.

    python3 -I -B appliquer-candidat12-r2-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

C12, PREFIXE = "brouillons/T0.6-organismes-v0-v1-candidat12.md", "379328fa97638a6c"
C12R2 = "brouillons/T0.6-organismes-v0-v1-candidat12-r2.md"
DERIVATION = ("dérivation (voie (a), décision de la mère du 8 novembre ~07:10Z) : **liste v1** (`scripts/tests-cibles-t06-v1.txt`, 81 fichiers) : 1 878 essais collectés en local sous Python 3.11.18, et, sur l'instance d'E3 bis "
              "(A100-SXM4-80GB, 2,1 To de mémoire vive, 255 cœurs), « 1878 passed in 4009.60s (1:06:49) » (compte rendu 2 de la fille 6) : **égalité exacte** ; **liste v2** (`scripts/tests-cibles-t06-v2.txt`, 83 fichiers) : "
              "**1 914 essais collectés en local**, d'où 1914. **Réserve : la liste v2 n'a pas été relevée sur l'instance.** Si l'instance compte autre chose, l'amorce s'arrête avant le run (« tests : … ≠ 1914 passed ») : c'est la garde voulue, "
              "au coût d'environ une heure de machine, sans donnée fausse. Durée mesurée de la suite : 67 minutes (liste v1), environ 68 minutes pour la liste v2")


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(racine: Path) -> int:
    src = racine / C12
    if not sha(src).startswith(PREFIXE):
        raise SystemExit("candidat 12 : empreinte non conforme")
    sortie = racine / C12R2
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    t = src.read_text(encoding="utf-8")

    def une(nom, ancien, nouveau):
        nonlocal t
        n = t.count(ancien)
        if n != 1:
            raise SystemExit(f"{nom} : « {ancien[:70]}… » trouvé {n} fois, une attendue : arrêt, rien écrit")
        t = t.replace(ancien, nouveau)

    une("W1 en-tête", "- Tests attendus : `<<TESTS_ATTENDUS_T06>>` — dernière ligne exacte de la suite ciblée et figée (`scripts/tests-cibles-t06-v1.txt`, E3 bis)",
        "- Tests attendus : `1914` — dernière ligne exacte attendue de la suite ciblée et figée (`scripts/tests-cibles-t06-v2.txt`) ; " + DERIVATION + " ;")
    une("W2 plan daté", "(`<<TESTS_ATTENDUS_T06>>`, session principale, avant le scellement)", "(`1914`, voie (a) : dérivation à la ligne « Tests attendus » de l'en-tête)")
    une("W3 table", "écrite dans l'en-tête, sur la seule ligne de citation de la clé « Tests attendus » | E3 bis, avant le scellement | session principale |",
        "écrite dans l'en-tête, sur la seule ligne de citation de la clé « Tests attendus » | **rempli : 1914** (voie (a), dérivation et réserve à l'en-tête) | la mère |")
    une("W4 statut", "- Statut : **candidat 12**, écrit le 2026-11-08", "- Statut : **candidat 12, révision 2** (nouveau fichier, R12 ; `<<TESTS_ATTENDUS_T06>>` rempli par la voie (a) : 1914, dérivation à la ligne « Tests attendus » de l'en-tête) ; candidat 12 initial : écrit le 2026-11-08")
    sortie.write_text(t, encoding="utf-8")
    print(sha(sortie))
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
