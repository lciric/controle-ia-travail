"""Contrôle d'avant création de l'instance des notations complémentaires de T0.5 (contre-lecture CE-06, CE-11) : rejoue,
sur le clone extrait au commit de scellement et sans aucun calcul, ce que l'instance vérifiera avant son premier
manifeste, pour chaque fiche : lecture des citations du script d'instance (`lire_unique` : intitulé cité une seule
fois ; tests attendus égaux d'une fiche à l'autre ; fichiers cités et leurs sceaux présents et conformes), fiche
scellée et conforme (`exiger_prereg_scelle`), puis toutes les gardes de `noter_complement_t05.executer` jusqu'au
manifeste exclu (la création du manifeste est remplacée par un arrêt témoin : rien n'est écrit).

    cd <clone> && <python avec torch> -B controle_avant_creation_v1.py PREREG_1 [PREREG_2]

Sort en code 0 si tout tient (une ligne par contrôle), 1 sinon (motif)."""
import json
import re
import sys
from pathlib import Path

RACINE = Path.cwd()
sys.path.insert(0, str(RACINE / "src"))
from controle_ia.environnements import noter_complement_t05 as m  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.prereg import exiger_prereg_scelle  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

INTITULES = ("Chemin de la configuration du complément", "Chemin des tâches du run source",
             "Chemin du manifeste du run source", "Chemin des épisodes du run source")


class Temoin(Exception):
    pass


def lire_unique(texte: str, intitule: str) -> str:
    n = texte.count(f"{intitule} : `")
    if n != 1:
        raise GardeArret(f"« {intitule} » cité {n} fois (une seule citation attendue par le script d'instance)")
    return re.search(re.escape(intitule) + r" : `([^`]*)`", texte).group(1)


def controler(prereg: str, attendus: list) -> None:
    texte = Path(prereg).read_text(encoding="utf-8")
    a = lire_unique(texte, "Tests attendus")
    if not a.isdigit() or (attendus and a != attendus[0]):
        raise GardeArret(f"tests attendus {a!r} (autre fiche : {attendus})")
    attendus.append(a)
    cites = [lire_unique(texte, i) for i in INTITULES]
    for f in cites:
        verifier(f)
    print(f"{prereg} : citations du script lues une fois chacune ; tests attendus {a} ; sceaux conformes : {', '.join(cites)}")
    print(f"{prereg} : fiche scellée et conforme {exiger_prereg_scelle(prereg)}")
    config = json.loads(Path(cites[0]).read_text(encoding="utf-8"))

    def temoin(*_a, **_k):
        raise Temoin

    m.creer_manifeste = temoin
    try:
        m.executer(config, RACINE, "controle-avant-creation", prereg, cites[1])
    except Temoin:
        print(f"{prereg} : gardes du module tenues jusqu'au manifeste (mode {config['mode']}, run source "
              f"{config['run_source']}, notations {config['notations_attendues_par_juge']})")
        return
    raise GardeArret("le module n'a pas atteint la création du manifeste")


def main(fiches: list[str]) -> int:
    attendus: list = []
    try:
        for p in fiches:
            controler(p, attendus)
    except GardeArret as e:
        print(f"ARRÊT : {e}")
        return 1
    print("contrôle d'avant création : tout tient")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
