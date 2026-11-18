"""Course d'idéation de l'organisme : lanceur, **version 9** — bras du juge externe différé avec remplacement déclaré du
modèle d'un juge (`pole/bras_remplacement_v1.py`). Ajout seul : les lanceurs v2 à v8 ne sont pas touchés (R12).

- Sans `--remplacement-modele-juge` : rend la main au lanceur v8, inchangé.
- Avec : exige `--bras-rapporte-differe` ; le bras est joué par `executer_bras_differe_avec_remplacement`, mêmes arguments
  que le bras d'origine. Le juge externe se donne au **modèle joué** (`--juge-externe ETIQUETTE=MODELE_JOUE`).

  python -I -B demonstrations/ideation_v9.py SORTIE --bras-rapporte-differe --attestation-lecture-humaine ATTEST.json \
      --juge-externe ETIQUETTE=MODELE_JOUE --commande-externe "…" … \
      --remplacement-modele-juge ETIQUETTE=MODELE_COURSE=MODELE_JOUE=GO-AAAA-MM-JJ-NN --mot-remplacement "ETIQUETTE=mot verbatim"

Codes : ceux du lanceur v8 ; 2 pour tout refus de ce lanceur (motif sur la sortie d'erreur), avant tout appel.
"""

import importlib.util
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)

_spec = importlib.util.spec_from_file_location("ideation_v8_lanceur_pour_v9", os.path.join(ICI, "ideation_v8.py"))
v8 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v8)  # instance propre (R12 : le lanceur v8 n'est pas touché)
lanceur_v2 = v8.v7.v6.base.base.base  # v6 → v5 → v4 → v2 : le lanceur qui appelle `idn.executer_bras_differe`

from pole import bras_remplacement_v1 as brv  # noqa: E402

VERSION = "lanceur-ideation-v9 (bras à remplacement déclaré du modèle d'un juge, v1)"
DRAPEAU, DRAPEAU_MOT = "--remplacement-modele-juge", "--mot-remplacement"


class Refus(Exception):
    pass


def extraire(argv):
    """Retire les deux drapeaux de ce lanceur ; rend (argv restant, {etiquette: {modele_course, modele_joue, go, mot}})."""
    reste, bruts, mots, i = [], [], [], 0
    while i < len(argv):
        if argv[i] in (DRAPEAU, DRAPEAU_MOT):
            if i + 1 >= len(argv):
                raise Refus(f"{argv[i]} : valeur manquante")
            (bruts if argv[i] == DRAPEAU else mots).append(argv[i + 1])
            i += 2
        elif argv[i].startswith(DRAPEAU + "=") or argv[i].startswith(DRAPEAU_MOT + "="):
            raise Refus("les drapeaux de remplacement se donnent en deux arguments (DRAPEAU VALEUR)")
        else:
            reste.append(argv[i])
            i += 1
    remplacements = {}
    for b in bruts:
        champs = b.split("=")
        if len(champs) != 4 or not all(champs):
            raise Refus(f"{DRAPEAU} : ETIQUETTE=MODELE_COURSE=MODELE_JOUE=GO attendu (reçu {b!r})")
        if champs[0] in remplacements:
            raise Refus(f"{DRAPEAU} : étiquette {champs[0]!r} donnée deux fois")
        remplacements[champs[0]] = {"modele_course": champs[1], "modele_joue": champs[2], "go": champs[3]}
    for m in mots:
        etiquette, sep, mot = m.partition("=")
        if not sep or etiquette not in remplacements or "mot" in remplacements[etiquette]:
            raise Refus(f"{DRAPEAU_MOT} : ETIQUETTE=mot, une fois par étiquette remplacée (reçu {m!r})")
        remplacements[etiquette]["mot"] = mot
    manquants = sorted(e for e, r in remplacements.items() if "mot" not in r)
    if manquants:
        raise Refus(f"{DRAPEAU_MOT} manquant pour {manquants}")
    if mots and not remplacements:
        raise Refus(f"{DRAPEAU_MOT} sans {DRAPEAU}")
    return reste, remplacements


class _CoeurAvecRemplacement:
    """Le cœur `pole.ideation_v2` vu par le lanceur v2, où seul `executer_bras_differe` est celui du remplacement."""

    def __init__(self, coeur, remplacements):
        self._coeur, self._remplacements = coeur, remplacements

    def __getattr__(self, nom):
        return getattr(self._coeur, nom)

    def executer_bras_differe(self, sortie, **arguments):
        return brv.executer_bras_differe_avec_remplacement(sortie, remplacements_modele_juge=self._remplacements, **arguments)


def principal(argv=None, environnement=None, etage1=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        reste, remplacements = extraire(argv)
        if not remplacements:
            return v8.principal(argv, environnement, etage1)  # la version 8, inchangée
        if "--bras-rapporte-differe" not in reste or "--course-2" in reste or "--pre-pilote" in reste:
            raise Refus(f"{DRAPEAU} ne se donne qu'avec --bras-rapporte-differe")
        donnes = {}
        for i, a in enumerate(reste):
            if a == "--juge-externe" and i + 1 < len(reste):
                e, _, m = reste[i + 1].partition("=")
                donnes[e] = m
        for e, r in remplacements.items():
            if donnes.get(e) != r["modele_joue"]:
                raise Refus(f"--juge-externe {e}={donnes.get(e)!r} : le juge remplacé se donne au modèle joué {r['modele_joue']!r}")
    except Refus as e:
        print(json.dumps({"arret": "Refus : " + str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    coeur = lanceur_v2.idn
    lanceur_v2.idn = _CoeurAvecRemplacement(coeur, remplacements)
    try:
        return v8.principal(reste, environnement, etage1)
    finally:
        lanceur_v2.idn = coeur


if __name__ == "__main__":
    raise SystemExit(principal())
