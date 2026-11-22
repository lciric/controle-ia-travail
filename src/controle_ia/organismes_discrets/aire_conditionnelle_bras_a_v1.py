"""Programme de l'aire conditionnelle du bras A des organismes discrets, version 1 : point d'entrée en commande de
l'étape (n), lancé à part par l'enchaînement de la lecture de la discrétion (version 2).

Texte qui fait foi : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md` — 6.3 (n) ; 6.9 ; 3.5 (b) (le programme
de l'aire conditionnelle « ne rend que les aires (valeur, intervalle, comptes), jamais une ligne du fichier ») ; 8.4.
Contrat : celui que l'enchaînement version 2 écrit dans sa documentation et dans `jouer_l_aire_conditionnelle`
(`enchainement_discretion_bras_a_v2.py`, empreinte 3b3c3a8b…). Décision de la session mère, option (a′).

**Ce que fait ce programme, et rien d'autre** : il compose trois fonctions de l'analyse, version 13 —
la lecture du fichier des rangs par unité, `aires_conditionnelles`, `ecrire_fichier_des_grandeurs_de_l_etape_n` —
selon ce contrat. Aucun calcul propre : ni arithmétique, ni tri, ni filtre sur les données ; il ne fait que lire ses
arguments et l'entrée standard, mettre les comptes des actions désappariées dans la forme que l'analyse attend
(table par (tâche, épisode), sans rien en retirer : un épisode écrit deux fois est refusé), appeler, et écrire la ligne.

**Avant tout import de l'analyse**, il vérifie que le fichier que l'import prendrait (`controle_ia.organismes_discrets.
analyse_bras_a_v13`, cherché sur `sys.path` par le chercheur de chemins de Python, sans exécuter aucun paquet) a
exactement l'empreinte `SHA256_DE_L_ANALYSE` ; sinon il sort sur le code 4 sans rien lire d'autre (ni arguments
lus, ni entrée standard, ni pièce). L'import se fait ensuite **sans cache de code compilé** (`sys.pycache_prefix`
porté sur un dossier vide, `sys.dont_write_bytecode`) : un fichier `.pyc` posé à côté ne remplace pas la source
vérifiée. Après l'import, le module chargé doit venir de ce même fichier, toujours à la même empreinte.

**Où il trouve `controle_ia`** : l'enchaînement le lance depuis une copie dans un dossier temporaire, avec
`PYTHONPATH=<racine du code>/src` (`_environnement`) et le dossier de travail à la racine du code ; c'est ce chemin
que Python suit. Ce programme ne déduit rien de son propre emplacement.

Arguments : `--configuration`, `--sortie`, `--fichier-des-unites`, et `--sortie-d-origine` pour une reprise de l'étape
(n). Entrée standard : un objet JSON aux quatre clés `actions_desappariees` (par dose écrite, une liste de [tâche,
épisode, compte]), `taches_de_verification`, `entropie_de_la_configuration_du_bras`, `autres_grandeurs`.
Codes de sortie :
- 0 : une seule ligne JSON `{"aires": {dose: {moniteur: sortie de l'aire}}, "cles": [...]}` ; le fichier des
  grandeurs de l'étape (n) est écrit et scellé par l'analyse ;
- 3 : arrêt de la lecture de la discrétion levé par l'analyse (consigné par elle), sortie standard vide ;
- 4 : garde ordinaire (de l'analyse, ou de ce programme : empreinte de l'analyse, forme de l'entrée standard),
  sortie standard vide, une seule ligne sur la sortie d'erreur, **sans le message de l'analyse** (6.9 : aucun nombre
  de la livraison) — seule l'étape est nommée ;
- 8 : erreur inattendue, sortie standard vide, son type seul sur la sortie d'erreur. Une erreur d'arguments sort sur
  le code 2 d'`argparse`. L'enchaînement ne rend rien de ces deux codes.

**Limites, écrites.** (a) Seule l'analyse est vérifiée à son empreinte ; les modules qu'elle importe (configuration,
dépôts, graines, arrêts, permutation, version 12) ne le sont pas ici — l'enchaînement relève leurs empreintes dans
son compte rendu. (b) Entre la vérification et l'import, le fichier pourrait changer ; la seconde empreinte, prise
après l'import, le voit s'il n'est pas remis à l'identique entre-temps. (c) Ce programme nomme la lecture du
fichier des rangs : la garde statique version 13 le refuse ; il n'est admis que par la garde statique version 14,
qui l'ajoute à la liste des programmes de l'aire conditionnelle.
"""
from __future__ import annotations

import argparse
import atexit
import hashlib
import importlib.machinery
import json
import shutil
import sys
import tempfile
from pathlib import Path

VERSION = 1
NOM_DE_L_ANALYSE = "controle_ia.organismes_discrets.analyse_bras_a_v13"
SHA256_DE_L_ANALYSE = "a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf"
CODE_DES_AIRES, CODE_DE_L_ARRET, CODE_DE_LA_GARDE, CODE_DE_L_ERREUR = 0, 3, 4, 8
CLES_DE_L_ENTREE = ("actions_desappariees", "taches_de_verification", "entropie_de_la_configuration_du_bras",
                    "autres_grandeurs")


class _Refus(Exception):
    """Garde de ce programme (empreinte de l'analyse, forme de l'entrée standard) : code 4, une ligne."""


# --- l'analyse, vérifiée à son empreinte avant tout import ------------------------------------------------------------

def _empreinte(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def chemin_de_l_analyse() -> Path | None:
    """Le fichier de l'analyse que l'import prendrait, cherché sur `sys.path` paquet par paquet par le chercheur de
    chemins de Python (`PathFinder`), **sans exécuter aucun paquet** ; `None` s'il n'est pas trouvé."""
    emplacements, spec = None, None
    for nom in ("controle_ia", "controle_ia.organismes_discrets", NOM_DE_L_ANALYSE):
        spec = importlib.machinery.PathFinder.find_spec(nom, emplacements)
        if spec is None:
            return None
        emplacements = spec.submodule_search_locations
    return Path(spec.origin) if spec.origin else None


def importer_l_analyse():
    """Vérifie l'empreinte du fichier de l'analyse, puis l'importe sans cache de code compilé, puis vérifie que le
    module chargé vient de ce fichier, toujours à la même empreinte. Tout écart : `_Refus`."""
    chemin = chemin_de_l_analyse()
    if chemin is None or not chemin.is_file():
        raise _Refus("analyse version 13 introuvable sur le chemin des modules — non importée")
    if _empreinte(chemin) != SHA256_DE_L_ANALYSE:
        raise _Refus("analyse version 13 : son empreinte n'est pas celle que ce programme inscrit — non importée")
    sys.dont_write_bytecode = True
    sys.pycache_prefix = tempfile.mkdtemp(prefix="aire-conditionnelle-sans-cache-")    # vide : aucun .pyc n'y est lu
    atexit.register(shutil.rmtree, sys.pycache_prefix, True)
    import controle_ia.organismes_discrets.analyse_bras_a_v13 as analyse    # le module que NOM_DE_L_ANALYSE nomme
    if Path(analyse.__file__).resolve() != chemin.resolve() or _empreinte(chemin) != SHA256_DE_L_ANALYSE:
        raise _Refus("analyse version 13 : le module chargé n'est pas le fichier vérifié — refusé")
    return analyse


# --- entrée standard ---------------------------------------------------------------------------------------------------

def _sans_doublon(paires):
    cles = [k for k, _ in paires]
    if len(cles) != len(set(cles)):
        raise _Refus("entrée standard : une clé en double — illisible")
    return dict(paires)


def _constante_refusee(nom):
    raise _Refus(f"entrée standard : `{nom}` — refusé")


def lire_l_entree_standard(texte: str) -> dict:
    """L'objet JSON de l'entrée standard, aux quatre clés et à elles seules. Les comptes des actions désappariées sont
    mis dans la forme que l'analyse attend — par dose écrite, une table (tâche, épisode) → compte —, sans rien en
    retirer ni en calculer ; un triplet hors de sa forme ou un épisode écrit deux fois : `_Refus`. Le reste est passé
    tel quel : l'analyse fait ses gardes."""
    try:
        o = json.loads(texte, object_pairs_hook=_sans_doublon, parse_constant=_constante_refusee)
    except json.JSONDecodeError:
        raise _Refus("entrée standard : pas un objet JSON") from None
    if not isinstance(o, dict) or set(o) != set(CLES_DE_L_ENTREE):
        raise _Refus(f"entrée standard : exactement les clés {CLES_DE_L_ENTREE}")
    ecrites = o["actions_desappariees"]
    if not isinstance(ecrites, dict):
        raise _Refus("entrée standard : `actions_desappariees` — une table par dose")
    par_dose = {}
    for dose, triplets in ecrites.items():
        if not isinstance(triplets, list) or any(not isinstance(t, list) or len(t) != 3 for t in triplets):
            raise _Refus("entrée standard : `actions_desappariees` — par dose, une liste de [tâche, épisode, compte]")
        comptes = {}
        for tache, episode, compte in triplets:
            if (tache, episode) in comptes:
                raise _Refus("entrée standard : `actions_desappariees` — un épisode écrit deux fois")
            comptes[(tache, episode)] = compte
        par_dose[dose] = comptes
    return {"desappariees": par_dose, "taches": o["taches_de_verification"],
            "entropie": o["entropie_de_la_configuration_du_bras"], "autres": o["autres_grandeurs"]}


# --- commande ------------------------------------------------------------------------------------------------------------

def _une_ligne(texte: str) -> None:
    sys.stderr.write(" ".join(str(texte).split()) + "\n")


def main(argv: list[str]) -> int:
    try:
        analyse = importer_l_analyse()
    except _Refus as x:
        _une_ligne(f"garde du programme de l'aire conditionnelle : {x}")
        return CODE_DE_LA_GARDE
    from controle_ia.gardes import GardeArret

    lecteur = argparse.ArgumentParser(description="Aire conditionnelle, bras A (étape (n)), version 1.")
    lecteur.add_argument("--configuration", required=True)
    lecteur.add_argument("--sortie", required=True)
    lecteur.add_argument("--fichier-des-unites", required=True)
    lecteur.add_argument("--sortie-d-origine", default=None)
    a = lecteur.parse_args(argv)
    etape = "lecture de l'entrée standard"
    try:
        entree = lire_l_entree_standard(sys.stdin.read())
        etape = "lecture du fichier des unités"
        rangs = analyse.lire_fichier_des_rangs(a.fichier_des_unites, a.sortie, a.configuration,
                                               analyse.USAGE_AIRE_CONDITIONNELLE, sortie_d_origine=a.sortie_d_origine)
        etape = "aires_conditionnelles"
        resultat = analyse.aires_conditionnelles(rangs, entree["desappariees"], entree["taches"], entree["entropie"])
        etape = "ecrire_fichier_des_grandeurs_de_l_etape_n"
        analyse.ecrire_fichier_des_grandeurs_de_l_etape_n(
            aires_conditionnelles=resultat, autres_grandeurs=entree["autres"], rangs=rangs, piece_scellee=a.sortie,
            configuration_scellee=a.configuration, sortie_d_origine=a.sortie_d_origine)
        del rangs
        etape = "écriture de la ligne"
        ligne = json.dumps({"aires": {analyse._forme_dose(d): {m: resultat["aires"][(m, d)] for m in analyse.MONITEURS}
                                      for d in analyse.QUATRE_DOSES},
                            "cles": resultat["cles"]}, ensure_ascii=False, allow_nan=False)
    except analyse.ArretDeLaLectureDeLaDiscretion:
        return CODE_DE_L_ARRET                       # consigné par l'analyse ; rien n'est écrit sur la sortie standard
    except _Refus as x:
        _une_ligne(f"garde du programme de l'aire conditionnelle : {x}")
        return CODE_DE_LA_GARDE
    except GardeArret:
        _une_ligne(f"garde ordinaire de l'analyse, étape « {etape} » — son message n'est pas rendu (6.9)")
        return CODE_DE_LA_GARDE
    except Exception as x:                           # noqa: BLE001 — son type seul : aucune variable n'en sort
        _une_ligne(f"erreur inattendue, étape « {etape} » : {type(x).__name__}")
        return CODE_DE_L_ERREUR
    sys.stdout.write(ligne + "\n")
    return CODE_DES_AIRES


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
