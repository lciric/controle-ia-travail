"""NON LANCÉ — EN ATTENTE DU MOT DE LAZAR. Programme qui enchaîne les étapes 6 bis et 7 du palier 0b (code v6), écrit à part du
paquet (un fichier de plus dans le paquet ferait refuser le verrou), sur le modèle de `outils-dev/lancer_etapes_8_et_9_v1.py` ;
il n'a été exécuté que par ses essais, sous la couche « essai-de-forme », sur une racine et des fichiers gelés factices.

Ordre des opérations (préenregistrement v13 et brouillon v14) : « 6 bis. Couche mécanique rejouée aux réglages gelés, sous des
étiquettes de graines disjointes, pour la garde d'équivalence. 7. Garde d'équivalence S8. » Le programme n'appelle que des
fonctions du code v6 ; il ne réécrit aucun calcul :
1. le verrou : `graines.Autorisation(texte, racine)` (texte présenté scellé, pièce d'autorisation du verrou, GO inscrit, commit
   et empreinte du texte, modules lancés conformes à la table du texte), puis la pièce de contrôle de la mère, sous la racine,
   scellée (`graines.verifier_scelle`), qui doit porter le commit du code et l'empreinte de ce programme (PROPOSITION) ;
2. la relecture des fichiers gelés des étapes 5 et 6, sous le contrôle de leurs empreintes et de leurs compagnons
   (`etapes.relire_fichiers_geles`) ;
3. les configurations « aux réglages gelés » (PROPOSITION, `configurations_aux_reglages_geles`) : chaque couple (proposeur,
   dose) que le plan des cases tire (`etapes.plan_des_cases` sur `etapes.reglages_pour_le_plan`), à sa configuration de
   référence (taille 1 ou force 1 ; sans taille ni force pour les proposeurs sans réglage) — 22 couples, 66 comparaisons quand
   toutes les cibles sont atteignables (la « soixantaine de comparaisons » de S8) ;
4. les étapes 6 bis et 7 : `etapes.etape_6_bis_et_7` (couche mécanique rejouée, couche statistique, `equivalence.garde_equivalence`),
   sous la couche « mecanique-reglages », racine des graines gelée ;
5. l'écriture, dans un dossier neuf : le détail de la garde (ou la cause de son arrêt), scellé, puis le manifeste du run
   (`tirages.ecrire_manifeste`, règle R9 : configuration, versions, racine, étiquettes, commit, fichiers gelés vérifiés).
Une garde S8 en échec est un arrêt (liste d'arrêt, point 4) : elle est écrite et scellée avec le manifeste, puis le programme
s'arrête avec un code non nul.

Usage, dossier courant : le dossier du code (celui qui porte `src/`), `PYTHONPATH=src` seul, interpréteur avec `-B` :

    python -B <chemin>/lancer_etapes_6bis_et_7_v1.py TEXTE RACINE FREQUENCES SHA_FREQUENCES REGLAGES SHA_REGLAGES DOSSIER

Il n'a ni paramètre de couche ni paramètre de taille sur la ligne de commande : couche « mecanique-reglages », 24 sources par
proposeur et par dose sur la couche mécanique, valeurs du code v6 pour le reste. La fonction `lancer` accepte la couche
« essai-de-forme » et des tailles réduites pour ses seuls essais ; toute autre couche est refusée avant tout geste.
"""

import hashlib
import json
import os
import sys

from controle_ia.heritage_etage_processeur_v1 import constantes as K
from controle_ia.heritage_etage_processeur_v1 import equivalence as EQ
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import tirages as TI

COUCHE_DES_ETAPES = "mecanique-reglages"  # graines.py : « mecanique-reglages » (étape 6 bis) ; B8 : étiquettes disjointes
COUCHE_DES_ESSAIS = "essai-de-forme"
# B8, « Version 12 », remarque 5 et décision de la mère R-4292 (v13, annexe H) : la pièce de contrôle de la mère, sous la racine
CHEMIN_PIECE_DE_CONTROLE = ("docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/"
                            "controle-lancement-palier-0b-par-la-mere-v1.md")
FICHIER_DU_DETAIL = "garde-equivalence-s8.json"
FICHIER_DE_L_ARRET = "arret-garde-equivalence-s8.txt"


class ArretProgramme(RuntimeError):
    pass


def empreinte_du_programme():
    with open(os.path.abspath(__file__), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def verifier_pieces(texte, racine):
    """Le verrou (code v6, sans changement), puis la pièce de contrôle de la mère : existante et scellée sous la racine, portant
    le commit du code (celui de la pièce d'autorisation, égal à celui de l'en-tête du texte) et l'empreinte de ce programme
    (PROPOSITION : la forme de cette pièce n'est fixée par aucun texte ; seule la présence de ces deux chaînes est exigée).
    Rend l'autorisation ; refus (`GraineRefusee`) ou arrêt (`ArretProgramme`) sinon."""
    a = GR.Autorisation(texte, racine)
    piece = os.path.join(os.path.abspath(racine), CHEMIN_PIECE_DE_CONTROLE)
    GR.verifier_scelle(piece)
    with open(piece, encoding="utf-8") as fh:
        contenu = fh.read()
    if a.commit not in contenu:
        raise ArretProgramme("la pièce de contrôle de la mère ne porte pas le commit du code de la pièce d'autorisation : arrêt")
    if empreinte_du_programme() not in contenu:
        raise ArretProgramme("la pièce de contrôle de la mère ne porte pas l'empreinte de ce programme : arrêt")
    return a


def configurations_aux_reglages_geles(lignes):
    """PROPOSITION (silence du texte : « rejouée aux réglages gelés » ne dit ni quels proposeurs, ni quelles doses, ni quelle taille
    ou force) : chaque couple (proposeur, dose) que tire `etapes.plan_des_cases`, construit sur les réglages gelés, à sa
    configuration de référence — cases sans taille ni force, ou à la taille 1, ou à la force 1. Deux configurations différentes
    pour un même couple arrêtent (aucun choix silencieux). Rend {(proposeur, dose) : configuration}."""
    cases, _ = EP.plan_des_cases(EP.reglages_pour_le_plan(lignes))
    out = {}
    for c in cases:
        if c.get("taille") not in (None, K.TAILLE_REFERENCE):
            continue
        if c.get("force") not in (None, K.FORCE_REFERENCE_SUIVEUR, K.FORCE_REFERENCE_GENERALISTE):
            continue
        cle = (c["proposeur"], c["dose"])
        if cle in out and out[cle] != c["config"]:
            raise ArretProgramme(f"deux configurations de référence pour {cle} : arrêt")
        out[cle] = c["config"]
    if not out:
        raise ArretProgramme("aucune configuration aux réglages gelés : arrêt")
    return out


def _ecrire_scelle(chemin, texte):
    """Écrit un fichier neuf et son compagnon « <empreinte>  <nom de base> » ; jamais d'écrasement."""
    octets = texte.encode("utf-8")
    with open(chemin, "xb") as fh:
        fh.write(octets)
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="ascii") as fh:
        fh.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def lancer(texte, racine, chemin_frequences, sha_frequences, chemin_reglages, sha_reglages, dossier, couche=COUCHE_DES_ETAPES,
           sources_mecaniques=None, sources_statistiques=None, seulement=None):
    """Les étapes 6 bis et 7. `couche`, `sources_mecaniques`, `sources_statistiques` et `seulement` (une liste de couples
    (proposeur, dose)) ne servent qu'aux essais, sous la couche « essai-de-forme » ; sous la couche des étapes, les tailles sont
    celles du code v6 et toutes les configurations sont jouées. Rend {"dossier", "detail", "manifeste"}."""
    if couche not in (COUCHE_DES_ETAPES, COUCHE_DES_ESSAIS):
        raise ArretProgramme(f"couche {couche!r} interdite : seules {COUCHE_DES_ETAPES!r} et, pour les essais, "
                             f"{COUCHE_DES_ESSAIS!r} : arrêt avant tout geste")
    reduit = (sources_mecaniques, sources_statistiques, seulement) != (None, None, None)
    if couche == COUCHE_DES_ETAPES and reduit:
        raise ArretProgramme("sous la couche des étapes, aucune taille réduite ni sous-ensemble : arrêt avant tout geste")
    if os.path.exists(dossier):
        raise ArretProgramme(f"dossier déjà présent : {dossier} (un dossier neuf est exigé) : arrêt avant tout geste")
    autorisation = verifier_pieces(texte, racine)
    f, lignes, fichiers_geles = EP.relire_fichiers_geles(chemin_frequences, sha_frequences, chemin_reglages, sha_reglages)
    configurations = configurations_aux_reglages_geles(lignes)
    if seulement is not None:
        manquants = [c for c in seulement if tuple(c) not in configurations]
        if manquants:
            raise ArretProgramme(f"couples absents des configurations : {manquants} : arrêt")
        configurations = {tuple(c): configurations[tuple(c)] for c in seulement}
    graines = GR.Graines(K.RACINE_GRAINES, autorisation=autorisation)
    tailles = {}
    if sources_mecaniques is not None:
        tailles["sources_mecaniques"] = sources_mecaniques
    if sources_statistiques is not None:
        tailles["sources_statistiques"] = sources_statistiques
    os.makedirs(dossier)
    try:
        detail = EP.etape_6_bis_et_7(graines, couche, os.path.join(dossier, "couche-mecanique"), f, configurations, **tailles)
        arret = None
    except EQ.ArretEquivalence as e:
        detail, arret = None, str(e)
    if arret is None:
        _ecrire_scelle(os.path.join(dossier, FICHIER_DU_DETAIL), json.dumps(
            {"|".join(str(x) for x in cle): v for cle, v in sorted(detail.items(), key=str)}, ensure_ascii=False,
            sort_keys=True, indent=1) + "\n")
    else:
        _ecrire_scelle(os.path.join(dossier, FICHIER_DE_L_ARRET), arret + "\n")
    configuration = {"etapes": "6 bis et 7", "couche": couche, "programme_sha256": empreinte_du_programme(),
                     "configurations": {f"{p}|{d}": c for (p, d), c in sorted(configurations.items(), key=str)},
                     "tailles": tailles or "valeurs du code v6", "issue": "tenue" if arret is None else "arrêt"}
    manifeste = os.path.join(dossier, "manifeste.json")
    TI.ecrire_manifeste(manifeste, configuration, graines, autorisation.commit, fichiers_geles)
    if arret is not None:
        raise ArretProgramme(f"garde d'équivalence S8 en échec (liste d'arrêt, point 4) : {arret}")
    return {"dossier": dossier, "detail": detail, "manifeste": manifeste}


def main(arguments):
    if len(arguments) != 7:
        raise SystemExit(__doc__)
    texte, racine, frequences, sha_f, reglages, sha_r, dossier = arguments
    r = lancer(texte, racine, frequences, sha_f, reglages, sha_r, dossier)
    with open(r["manifeste"] + ".sha256", encoding="ascii") as fh:
        print("étapes 6 bis et 7 :", r["manifeste"], fh.read().split()[0], len(r["detail"]), "comparaisons, garde tenue",
              flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
