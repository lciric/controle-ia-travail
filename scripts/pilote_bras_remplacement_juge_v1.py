"""Pilote du bras du juge externe différé avec remplacement déclaré du modèle d'un juge, sur l'orchestrateur livré par le
compte de l'organisme (`pole/bras_remplacement_juge_v2.py`). Les lanceurs livrés n'offrent pas l'option de remplacement :
ce pilote charge le lanceur livré `demonstrations/ideation_v2_juges_externes_uniques_v1.py`, lui fait appeler, pour le
seul bras différé, `bras_remplacement_juge_v2.executer_bras_differe` avec la déclaration, et lui rend tout le reste.

Usage (répertoire courant : `orchestrator/` de l'orchestrateur assemblé) :
  python3 -I -B CHEMIN/pilote_bras_remplacement_juge_v1.py ORCHESTRATEUR \
      --remplacement ETIQUETTE=MODELE_COURSE=MODELE_JOUE=GO-AAAA-MM-JJ-NN --mot-verbatim "ETIQUETTE=mot verbatim" -- ARGUMENTS DU LANCEUR
Les arguments du lanceur doivent porter `--bras-rapporte-differe` et `--juge-externe ETIQUETTE=MODELE_JOUE`.
Codes : ceux du lanceur ; 2 pour tout refus du pilote, avant tout appel.
"""
import importlib.util
import json
import os
import sys


class Refus(Exception):
    pass


def lire(argv):
    if "--" not in argv or len(argv) < 2:
        raise Refus("usage : ORCHESTRATEUR --remplacement E=COURSE=JOUE=GO --mot-verbatim E=mot -- arguments du lanceur")
    coupe = argv.index("--")
    tete, reste = argv[:coupe], argv[coupe + 1:]
    orchestrateur, options = tete[0], tete[1:]
    if len(options) % 2 or any(o not in ("--remplacement", "--mot-verbatim") for o in options[::2]):
        raise Refus("options du pilote : --remplacement VALEUR et --mot-verbatim VALEUR seulement")
    remplacements = {}
    for nom, valeur in zip(options[::2], options[1::2]):
        if nom == "--remplacement":
            c = valeur.split("=")
            if len(c) != 4 or not all(c) or c[0] in remplacements:
                raise Refus(f"--remplacement : ETIQUETTE=MODELE_COURSE=MODELE_JOUE=GO, une fois par étiquette (reçu {valeur!r})")
            remplacements[c[0]] = {"modele_course": c[1], "modele_joue": c[2], "reference_go": c[3]}
    for nom, valeur in zip(options[::2], options[1::2]):
        if nom == "--mot-verbatim":
            e, sep, mot = valeur.partition("=")
            if not sep or e not in remplacements or "mot_verbatim" in remplacements[e]:
                raise Refus(f"--mot-verbatim : ETIQUETTE=mot, une fois par étiquette remplacée (reçu {valeur!r})")
            remplacements[e]["mot_verbatim"] = mot
    if not remplacements or any("mot_verbatim" not in r for r in remplacements.values()):
        raise Refus("au moins un --remplacement, et un --mot-verbatim par étiquette remplacée")
    if "--bras-rapporte-differe" not in reste:
        raise Refus("le pilote ne joue que le bras différé (--bras-rapporte-differe exigé)")
    donnes = {}
    for i, a in enumerate(reste):
        if a.startswith("--juge-externe="):
            raise Refus("--juge-externe se donne en deux arguments")
        if a == "--juge-externe" and i + 1 < len(reste):
            e, _, m = reste[i + 1].partition("=")
            if e in donnes:
                raise Refus(f"--juge-externe donné deux fois pour {e!r}")
            donnes[e] = m
    for e, r in remplacements.items():
        if donnes.get(e) != r["modele_joue"]:
            raise Refus(f"--juge-externe {e}={donnes.get(e)!r} : le juge remplacé se donne au modèle joué {r['modele_joue']!r}")
    return orchestrateur, remplacements, reste


class _Coeur:
    """Le cœur vu par le lanceur, où seul `executer_bras_differe` est celui de la livraison, avec la déclaration."""

    def __init__(self, coeur, bras, remplacements):
        self._coeur, self._bras, self._remplacements = coeur, bras, remplacements

    def __getattr__(self, nom):
        return getattr(self._coeur, nom)

    def executer_bras_differe(self, sortie, **reglages):
        return self._bras.executer_bras_differe(sortie, remplacements_juges_externes=self._remplacements, **reglages)


def principal(argv=None) -> int:
    try:
        orchestrateur, remplacements, reste = lire(list(sys.argv[1:] if argv is None else argv))
        cible = os.path.join(orchestrateur, "demonstrations", "ideation_v2_juges_externes_uniques_v1.py")
        if not os.path.isfile(cible):
            raise Refus(f"lanceur livré absent : {cible}")
    except Refus as e:
        print(json.dumps({"arret": "Refus du pilote : " + str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    spec = importlib.util.spec_from_file_location("lanceur_livre_pour_pilote_v1", cible)
    livre = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(livre)                      # met `orchestrator/` en tête de sys.path et charge le lanceur v2
    from pole import bras_remplacement_juge_v2 as bras
    coeur = livre.LANCEUR.idn
    livre.LANCEUR.idn = _Coeur(coeur, bras, remplacements)
    try:
        return livre.principal(reste)
    finally:
        livre.LANCEUR.idn = coeur


if __name__ == "__main__":
    raise SystemExit(principal())
