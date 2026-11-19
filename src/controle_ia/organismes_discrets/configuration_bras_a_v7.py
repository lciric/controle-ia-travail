"""Configuration scellée de l'analyse de la discrétion, bras A des organismes discrets, version 7 du code
(préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md`, conventions, « Configuration scellée de
l'analyse de la discrétion » ; 6.9 ; section 12, points 17 à 21).

`configuration_bras_a_v6.py` n'est pas modifié (R12). Le fichier porte maintenant **son nom**, fixé au texte :
`configuration-de-l-analyse-de-la-discretion-bras-a.json`. Il est écrit par la session de relance après le scellement
du texte, scellé, et inscrit au registre par son empreinte avant la réception de la sortie de la lecture commune.

Deux choses n'appartiennent pas au code, et il ne les devine pas :

1. **`choix` — les choix qui attendent Lazar.** Cinq choix nommés, **obligatoires, sans valeur par défaut** :
   - le schéma de permutation des étiquettes (point 17) ;
   - le nombre sur lequel se compte le seuil de 1 % de tirages dégénérés (point 18, fiche 9) ;
   - l'état d'un moniteur dont l'intervalle n'a pas pu être calculé (point 19, fiche 10) ;
   - l'état d'un moniteur appris qui n'a pas pu être ajusté (point 20, fiche 11) ;
   - ce que vaut un arrêt de la lecture de la discrétion (point 21, fiche 12).
   Aucun n'a de valeur dans ce module. Ils ne se décident pas dans ce fichier : chacun recopie la rédaction restée au
   texte scellé, et une valeur qui s'en écarte est un écart au préenregistrement.
2. **`chaines_du_module` — les chaînes du module du côté habilité** que la relance ne connaît pas : valeurs de `motif`
   et cause que nomme chacune ; valeur de `motif` au cas A ; valeur de `calculable` aux cas A, D et E ; ce que
   `reglages.permutation` et `reglages.unite_de_la_permutation` portent sous chaque schéma ; `statistique_agregateur` ;
   forme des doses ; contenu de `quantile_borne_haute` ; **et, pour le fichier des scores par unité, les valeurs du
   champ `dose` et la valeur du champ `condition` pour l'honnête** (brouillon 25 ; vérification du code de la version
   6, C-1 : elles étaient écrites en dur). Elles sont inscrites à la lettre, par qui les tient du développeur
   habilité (case du module, 13.1).

**Une troisième partie, que le texte ne nomme pas encore** (relevé des défauts du texte, version 7) :
3. **`pieces_attendues`** — deux empreintes que le code doit connaître sans pouvoir les deviner :
   - `sha256_du_registre_des_accords` : l'empreinte du registre des accords **de la branche principale** au moment où
     cette configuration est scellée. Le code ne lit le registre du dépôt (`registres/go.md`) que s'il porte cette
     empreinte ; sinon il s'arrête en disant les deux empreintes : il ne lit jamais un registre en retard, ni en
     avance, sans le dire. `null` : aucun registre n'est lu sous cette configuration, et une lecture qui demanderait
     une ligne de GO (une livraison refaite) s'arrête. C'est une solution **sans réseau** : la branche qui porte le
     code n'a pas à savoir où est la branche principale ; qui scelle la configuration le sait (vérification du code,
     M-2 ; mandat de la version 7, point 5) ;
   - `sha256_du_module_du_cote_habilite` : l'empreinte du module du côté habilité dont les chaînes sont inscrites
     ici, telle que la case du module de 13.1 la porte ; **toujours exigée**. Elle sert deux fois. Sous le choix
     « module corrige » du point 20, c'est l'empreinte du module corrigé : le code ne peut pas savoir autrement que le
     module est corrigé, et la différence entre les rédactions (a) et (c) tient toute à cette version (vérification du
     code, M-6). Et pour une livraison refaite, c'est « le module corrigé » que la ligne de GO doit citer : une ligne
     qui cite un autre module n'ouvre rien (8.4, « livraison refaite : une ligne de GO par livraison »). Le code
     n'ouvre pas ce module : il compare des empreintes.

`lire_la_configuration_scellee` vérifie le nom du fichier, son compagnon, ses listes fermées de noms et chacune de ses
valeurs, et rend avec elle l'empreinte du fichier, que portent le résultat de la règle de discrétion et les constats
de l'étape (m). Ce module ne lit que ce fichier. Il ne nomme aucune ligne d'aucune table de verdict.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Mapping

from ..gardes import GardeArret
from ..scellement import verifier

# --- Les cinq choix nommés, et leurs valeurs permises ---------------------------------------------------------------------
CHOIX_SCHEMA = "schema_de_permutation"
SCHEMA_LIBRE, SCHEMA_ECHANGE = "libre par episode", "echange dans chaque paire"

CHOIX_SEUIL = "seuil_du_un_pour_cent"
SEUIL_SUR_LES_DEMANDES, SEUIL_SUR_LES_CALCULES = "sur les tirages demandes", "sur les tirages calcules"

CHOIX_INTERVALLE_IMPOSSIBLE = "intervalle_impossible"
INTERVALLE_COMME_DEGENERE, INTERVALLE_INDECIS_D_OFFICE, INTERVALLE_ANOMALIE = (
    "comme un intervalle degenere", "indecis d'office", "anomalie")

CHOIX_NON_AJUSTABLE = "moniteur_appris_non_ajustable"
NON_AJUSTABLE_AIRE_NON_CALCULABLE, NON_AJUSTABLE_ANOMALIE, NON_AJUSTABLE_MODULE_CORRIGE = (
    "aire non calculable", "anomalie", "module corrige")

CHOIX_ISSUE = "issue_d_un_arret_de_la_lecture_de_la_discretion"
ISSUE_LIGNE_D_ARRET_DE_LA_COURSE, ISSUE_DISCRETION_NON_LUE, ISSUE_PAR_ETAPE = (
    "ligne d'arret de la course, en entier", "discretion non lue", "discretion non lue, en distinguant les etapes")

VALEURS_DES_CHOIX = {
    CHOIX_SCHEMA: (SCHEMA_LIBRE, SCHEMA_ECHANGE),
    CHOIX_SEUIL: (SEUIL_SUR_LES_DEMANDES, SEUIL_SUR_LES_CALCULES),
    CHOIX_INTERVALLE_IMPOSSIBLE: (INTERVALLE_COMME_DEGENERE, INTERVALLE_INDECIS_D_OFFICE, INTERVALLE_ANOMALIE),
    CHOIX_NON_AJUSTABLE: (NON_AJUSTABLE_AIRE_NON_CALCULABLE, NON_AJUSTABLE_ANOMALIE, NON_AJUSTABLE_MODULE_CORRIGE),
    CHOIX_ISSUE: (ISSUE_LIGNE_D_ARRET_DE_LA_COURSE, ISSUE_DISCRETION_NON_LUE, ISSUE_PAR_ETAPE),
}

# --- Les chaînes du module du côté habilité ------------------------------------------------------------------------------
# Causes que la table des formes distingue (6.9) : trois au cas B — dont « moniteur appris non ajustable », lu selon
# le point 20 —, une aux cas C, D et E. La configuration donne, pour chaque valeur de `motif`, la cause qu'elle nomme.
CAUSE_ANTERIEURE = "cause anterieure aux permutations"                 # cas B : pli sans action, classe absente…
CAUSE_NON_AJUSTABLE = "moniteur appris non ajustable"                  # cas B, selon le point 20
CAUSE_PERMUTATIONS_PERDUES = "plus de 1 % de permutations perdues"     # cas C
CAUSE_TIRAGES_DEGENERES = "plus de 1 % de tirages degeneres"           # cas D
CAUSE_INTERVALLE_IMPOSSIBLE = "intervalle impossible"                  # cas E
CAUSES = (CAUSE_ANTERIEURE, CAUSE_NON_AJUSTABLE, CAUSE_PERMUTATIONS_PERDUES, CAUSE_TIRAGES_DEGENERES,
          CAUSE_INTERVALLE_IMPOSSIBLE)
CAS_DE_LA_CAUSE = {CAUSE_ANTERIEURE: "B", CAUSE_NON_AJUSTABLE: "B", CAUSE_PERMUTATIONS_PERDUES: "C",
                   CAUSE_TIRAGES_DEGENERES: "D", CAUSE_INTERVALLE_IMPOSSIBLE: "E"}
FORMES_DOSE = ("dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00")
CAS_OU_CALCULABLE_EST_INSCRIT = ("A", "D", "E")       # aux cas B et C, le texte exige « faux »

# Les deux chaînes de plus du brouillon 25, pour le fichier des scores par unité (6.9) : pour chacune des quatre doses,
# la valeur du champ `dose` d'une ligne ; et la valeur du champ `condition` d'une ligne de l'honnête.
CHAINE_DES_DOSES_DU_FICHIER = "doses_du_fichier_des_scores"
CHAINE_DE_LA_CONDITION_DE_L_HONNETE = "condition_de_l_honnete_du_fichier_des_scores"
CHAINES = ("motifs", "motif_au_cas_a", "calculable", "declarations_du_schema", "statistique_agregateur",
           "doses_de_la_famille", "dose_pour_information", "cles_des_doses_dans_lectures", "valeurs_du_champ_dose",
           "quantile_borne_haute", CHAINE_DES_DOSES_DU_FICHIER, CHAINE_DE_LA_CONDITION_DE_L_HONNETE)
REGISTRE_ATTENDU = "sha256_du_registre_des_accords"
MODULE_DU_COTE_HABILITE = "sha256_du_module_du_cote_habilite"
PIECES_ATTENDUES = (REGISTRE_ATTENDU, MODULE_DU_COTE_HABILITE)
RACINE = ("choix", "chaines_du_module", "pieces_attendues")
NOM_DU_FICHIER_DE_LA_CONFIGURATION = "configuration-de-l-analyse-de-la-discretion-bras-a.json"
_EMPREINTE = re.compile(r"[0-9a-f]{64}")
CHAMPS_D_UNE_DECLARATION = ("permutation", "unite_de_la_permutation")


def _sans_doublon(paires):
    vues = {}
    for k, v in paires:
        if k in vues:
            raise GardeArret(f"configuration scellée : champ {k!r} en double")
        vues[k] = v
    return vues


def _liste_fermee(objet, noms, ou: str) -> None:
    if not isinstance(objet, dict) or sorted(objet) != sorted(noms):
        recus = sorted(map(str, objet)) if isinstance(objet, dict) else type(objet).__name__
        raise GardeArret(f"configuration scellée, {ou} : champs {recus} — exactement {sorted(noms)} exigés ; un choix ou "
                         "une chaîne qui manque n'a pas de valeur par défaut")


def _texte(x, ou: str) -> str:
    if not isinstance(x, str) or not x.strip() or "\n" in x:
        raise GardeArret(f"configuration scellée, {ou} : texte non vide, d'une ligne, exigé")
    return x


def exiger_configuration(c) -> dict:
    """Contrôle d'une configuration lue : les deux parties, leurs listes fermées de noms, et chaque valeur.
    - `choix` : les cinq choix, chacun pris dans ses valeurs permises, écrit en toutes lettres ;
    - `chaines_du_module.motifs` : pour chaque valeur de `motif` que le module peut rendre, la cause qu'elle nomme
      (l'une de `CAUSES`) ; chaque cause a au moins une valeur ; c'est la liste fermée des valeurs de `motif` ;
    - `motif_au_cas_a` : ce que porte `motif` quand tout est calculable (nul, ou un texte qui n'est pas un motif de
      cause) ;
    - `calculable` : la valeur de ce champ aux cas A, D et E (booléens) ;
    - `declarations_du_schema` : pour chacun des deux schémas, ce que la livraison porte dans `reglages.permutation` et
      `reglages.unite_de_la_permutation` ; les deux schémas se déclarent différemment ;
    - `statistique_agregateur`, `doses_de_la_famille`, `dose_pour_information` : ce que `reglages` doit porter, tel
      quel (aucune valeur nulle : nul voudrait dire « non inscrit ») ;
    - `cles_des_doses_dans_lectures`, `valeurs_du_champ_dose` : pour chacune des quatre doses, la clé de `lectures` et
      la valeur du champ `dose` d'une lecture ;
    - `quantile_borne_haute` : ce que porte ce champ quand il dit le quantile 1 − 0,05 ÷ 15 ;
    - `doses_du_fichier_des_scores` : pour chacune des quatre doses, la valeur du champ `dose` d'une ligne du fichier
      des scores par unité (quatre textes distincts) ; `condition_de_l_honnete_du_fichier_des_scores` : la valeur du
      champ `condition` d'une ligne de l'honnête (un texte, qui n'est la valeur d'aucune dose) ;
    - `pieces_attendues` : l'empreinte attendue du registre des accords, ou `null` ; l'empreinte du module du côté
      habilité dont les chaînes sont inscrites, toujours exigée."""
    _liste_fermee(c, RACINE, "racine")
    choix, chaines = c["choix"], c["chaines_du_module"]
    pieces = c["pieces_attendues"]
    _liste_fermee(pieces, PIECES_ATTENDUES, "pièces attendues")
    for nom in PIECES_ATTENDUES:
        if pieces[nom] is not None and (not isinstance(pieces[nom], str) or _EMPREINTE.fullmatch(pieces[nom]) is None):
            raise GardeArret(f"configuration scellée, `pieces_attendues.{nom}` : une empreinte entière (64 signes), ou `null`")
    _liste_fermee(choix, VALEURS_DES_CHOIX, "choix")
    for nom, permises in VALEURS_DES_CHOIX.items():
        if not isinstance(choix[nom], str) or choix[nom] not in permises:
            raise GardeArret(f"configuration scellée, choix `{nom}` = {choix[nom]!r} : l'un de {permises} exigé, écrit en "
                             "toutes lettres — aucune valeur par défaut")
    if pieces[MODULE_DU_COTE_HABILITE] is None or pieces[MODULE_DU_COTE_HABILITE] == pieces[REGISTRE_ATTENDU]:
        raise GardeArret(f"configuration scellée, `pieces_attendues.{MODULE_DU_COTE_HABILITE}` : l'empreinte du module du côté "
                         "habilité dont les chaînes sont inscrites est exigée (case du module, 13.1) — sous le choix « "
                         f"{NON_AJUSTABLE_MODULE_CORRIGE} » du point 20, c'est celle du module corrigé, que le code ne peut pas "
                         "connaître autrement")
    _liste_fermee(chaines, CHAINES, "chaînes du module")
    motifs = chaines["motifs"]
    if not isinstance(motifs, dict) or not motifs:
        raise GardeArret("configuration scellée, `motifs` : pour chaque valeur de `motif`, la cause qu'elle nomme")
    for valeur, cause in motifs.items():
        _texte(valeur, "`motifs`")
        if not isinstance(cause, str) or cause not in CAUSES:
            raise GardeArret(f"configuration scellée, `motifs[{valeur!r}]` = {cause!r} : l'une de {CAUSES} exigée")
    manquantes = [x for x in CAUSES if x not in motifs.values()]
    if manquantes:
        raise GardeArret(f"configuration scellée, `motifs` : aucune valeur ne nomme {manquantes}")
    au_cas_a = chaines["motif_au_cas_a"]
    if au_cas_a is not None:
        if _texte(au_cas_a, "`motif_au_cas_a`") in motifs:
            raise GardeArret("configuration scellée, `motif_au_cas_a` : c'est aussi le motif d'une cause")
    _liste_fermee(chaines["calculable"], CAS_OU_CALCULABLE_EST_INSCRIT, "`calculable`")
    if any(not isinstance(x, bool) for x in chaines["calculable"].values()):
        raise GardeArret("configuration scellée, `calculable` : un booléen par cas (A, D, E)")
    declarations = chaines["declarations_du_schema"]
    _liste_fermee(declarations, VALEURS_DES_CHOIX[CHOIX_SCHEMA], "`declarations_du_schema`")
    for schema, d in declarations.items():
        _liste_fermee(d, CHAMPS_D_UNE_DECLARATION, f"`declarations_du_schema[{schema!r}]`")
        for champ in CHAMPS_D_UNE_DECLARATION:
            _texte(d[champ], f"`declarations_du_schema[{schema!r}].{champ}`")
    if declarations[SCHEMA_LIBRE] == declarations[SCHEMA_ECHANGE]:
        raise GardeArret("configuration scellée, `declarations_du_schema` : les deux schémas ont la même déclaration — la "
                         "livraison ne dirait pas lequel a servi")
    for nom in ("statistique_agregateur", "doses_de_la_famille", "dose_pour_information", "quantile_borne_haute"):
        if chaines[nom] is None:
            raise GardeArret(f"configuration scellée, `{nom}` : valeur non inscrite")
    _liste_fermee(chaines["cles_des_doses_dans_lectures"], FORMES_DOSE, "`cles_des_doses_dans_lectures`")
    cles = [_texte(x, "`cles_des_doses_dans_lectures`") for x in chaines["cles_des_doses_dans_lectures"].values()]
    if len(set(cles)) != len(FORMES_DOSE):
        raise GardeArret("configuration scellée, `cles_des_doses_dans_lectures` : quatre clés distinctes exigées")
    _liste_fermee(chaines["valeurs_du_champ_dose"], FORMES_DOSE, "`valeurs_du_champ_dose`")
    valeurs = list(chaines["valeurs_du_champ_dose"].values())
    if any(x is None or isinstance(x, (dict, list, bool)) for x in valeurs) \
            or len({json.dumps(x, sort_keys=True) for x in valeurs}) != len(FORMES_DOSE):
        raise GardeArret("configuration scellée, `valeurs_du_champ_dose` : quatre valeurs distinctes (texte ou nombre)")
    _liste_fermee(chaines[CHAINE_DES_DOSES_DU_FICHIER], FORMES_DOSE, f"`{CHAINE_DES_DOSES_DU_FICHIER}`")
    doses = [_texte(x, f"`{CHAINE_DES_DOSES_DU_FICHIER}`") for x in chaines[CHAINE_DES_DOSES_DU_FICHIER].values()]
    if len(set(doses)) != len(FORMES_DOSE):
        raise GardeArret(f"configuration scellée, `{CHAINE_DES_DOSES_DU_FICHIER}` : quatre textes distincts exigés")
    if _texte(chaines[CHAINE_DE_LA_CONDITION_DE_L_HONNETE], f"`{CHAINE_DE_LA_CONDITION_DE_L_HONNETE}`") in doses:
        raise GardeArret(f"configuration scellée, `{CHAINE_DE_LA_CONDITION_DE_L_HONNETE}` : c'est aussi la valeur d'une "
                         "dose — une ligne ne dirait pas si elle est de l'honnête")
    return c


def lire_la_configuration_scellee(chemin) -> dict:
    """Lit la configuration scellée : le fichier **porte son nom** (conventions du brouillon 25) et répond à son
    empreinte compagnon ; c'est un objet JSON, sans champ en double ; il passe `exiger_configuration`. Rend `{"choix",
    "chaines_du_module", "pieces_attendues", "sha256", "chemin"}`. Un chemin absent, un fichier d'un autre nom, non
    scellé ou retouché, un dictionnaire donné à la place du chemin sont refusés."""
    try:
        est_un_fichier = isinstance(chemin, (str, Path)) and Path(chemin).is_file()
    except OSError:
        est_un_fichier = False
    if not est_un_fichier:
        raise GardeArret("configuration scellée : le chemin d'un fichier scellé est exigé — un dictionnaire donné par "
                         "l'appelant n'est pas admis (contre-lecture du code de la version 5, C-2)")
    if Path(chemin).name != NOM_DU_FICHIER_DE_LA_CONFIGURATION:
        raise GardeArret(f"configuration scellée : fichier `{NOM_DU_FICHIER_DE_LA_CONFIGURATION}` exigé (conventions)")
    verifier(chemin)
    brut = Path(chemin).read_bytes()
    try:
        c = json.loads(brut.decode("utf-8"), object_pairs_hook=_sans_doublon)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise GardeArret("configuration scellée : JSON illisible") from None
    exiger_configuration(c)
    return {"choix": c["choix"], "chaines_du_module": c["chaines_du_module"], "pieces_attendues": c["pieces_attendues"],
            "sha256": hashlib.sha256(brut).hexdigest(), "chemin": str(Path(chemin))}


def choix(configuration: Mapping, nom: str) -> str:
    """Valeur d'un choix nommé d'une configuration lue par `lire_la_configuration_scellee`."""
    if nom not in VALEURS_DES_CHOIX:
        raise GardeArret(f"choix {nom!r} inconnu")
    if not isinstance(configuration, Mapping) or "sha256" not in configuration or "choix" not in configuration:
        raise GardeArret("configuration lue du fichier scellé exigée (`lire_la_configuration_scellee`)")
    valeur = configuration["choix"][nom]
    if valeur not in VALEURS_DES_CHOIX[nom]:
        raise GardeArret(f"choix `{nom}` hors de ses valeurs permises")
    return valeur


def registre_attendu(configuration: Mapping) -> str:
    """Empreinte attendue du registre des accords, lue de la configuration scellée. `null` : aucun registre n'est lu
    sous cette configuration — arrêt, en le disant."""
    if not isinstance(configuration, Mapping) or "sha256" not in configuration or "pieces_attendues" not in configuration:
        raise GardeArret("configuration lue du fichier scellé exigée (`lire_la_configuration_scellee`)")
    attendue = configuration["pieces_attendues"][REGISTRE_ATTENDU]
    if attendue is None:
        raise GardeArret("la configuration scellée ne dit pas quel registre des accords lire "
                         f"(`pieces_attendues.{REGISTRE_ATTENDU}` est `null`) : aucune ligne de GO ne se lit sous elle — "
                         "sceller une configuration qui porte l'empreinte du registre de la branche principale")
    return attendue


def module_du_cote_habilite(configuration: Mapping) -> str:
    """Empreinte du module du côté habilité que la configuration scellée inscrit (jamais `null`)."""
    if not isinstance(configuration, Mapping) or "sha256" not in configuration or "pieces_attendues" not in configuration:
        raise GardeArret("configuration lue du fichier scellé exigée (`lire_la_configuration_scellee`)")
    return configuration["pieces_attendues"][MODULE_DU_COTE_HABILITE]
