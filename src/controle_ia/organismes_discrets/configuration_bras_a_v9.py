"""Configuration scellée de l'analyse de la discrétion, bras A des organismes discrets, version 9 du code
(préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon31.md`, conventions, « Configuration scellée de
l'analyse de la discrétion » ; 6.9 ; section 12, points 17 à 21 ; 13.2).

`configuration_bras_a_v8.py` n'est pas modifié (R12). **Ce qui change à la version 9** (brouillons 29 et 30) :
`pieces_attendues` a **cinq entrées** — s'y ajoute `sha256_du_programme_du_constat`, l'empreinte entière du programme
du constat de lancement, que le programme d'analyse confronte au huitième champ du constat — ; le constat de
lancement a **huit champs**. Le fichier porte son nom, fixé au texte :
`configuration-de-l-analyse-de-la-discretion-bras-a.json`. **Une configuration par livraison** : la première livraison
a la sienne ; une livraison refaite a la sienne, scellée avant sa réception. Chaque livraison a son **dossier
d'analyse**, `livraison-<rang>/` (rang 1 pour la première), qui porte sa configuration et, si elle est lue, son
fichier de l'étape (m) et ses constats. Rien n'est jamais réécrit. **Le dossier des arrêts est à part, commun à toutes
les livraisons.**

Un objet JSON à **trois parties et elles seules** :

1. **`choix` — les choix qui attendent Lazar.** Cinq choix nommés, **obligatoires, sans valeur par défaut** : le
   schéma de permutation (point 17) ; le seuil du 1 % (point 18, fiche 9) ; l'intervalle impossible (point 19,
   fiche 10) ; le moniteur appris non ajustable (point 20, fiche 11) ; l'issue d'un arrêt (point 21, fiche 12). Aucun
   n'a de valeur dans ce module ; chacun recopie la rédaction restée au texte scellé, et **ils sont les mêmes pour
   toutes les livraisons** : un écart entre deux configurations de la course est refusé
   (`exiger_configurations_de_la_course`).
2. **`chaines_du_module` — ce que la case du module de 13.1 inscrit**, et que la relance ne devine pas : valeurs de
   `motif` et cause que nomme chacune ; `motif` au cas A ; `calculable` aux cas A, D et E ; déclarations du schéma ;
   statistique de l'agrégateur ; forme des doses ; `quantile_borne_haute` ; `doses_du_fichier_des_scores` et
   `condition_de_l_honnete_du_fichier_des_scores`. **Une chaîne de plus, que le texte ne porte pas encore** (relevé
   des défauts du texte, version 8 ; vérification du code de la version 7, M-6 ; demande 18 de la note du brouillon
   26) : `cle_du_module_dans_piece_source`, le nom de la clé de `piece_source` qui porte l'empreinte du module qui a
   produit la livraison. Inscrite, la livraison est confrontée au module que cette configuration nomme ; `null`,
   `piece_source` n'est pas lu, et le résultat le dit. Le code ne devine pas la forme de `piece_source`.
3. **`pieces_attendues` — ce que le programme doit connaître sans pouvoir le deviner**, cinq entrées (la cinquième à la version 9 :
   `sha256_du_programme_du_constat`) :
   - `sha256_du_module_du_cote_habilite` : l'empreinte entière du module dont les chaînes sont inscrites ;
   - `sha256_du_rapport_de_contre_lecture_du_module` : l'empreinte entière du rapport de sa contre-lecture ;
   - `sha256_du_registre_des_accords` : l'empreinte du registre lu — le registre des accords de la branche
     principale **tel qu'il était quand cette configuration a été scellée**, remis au programme comme une pièce —, ou
     `null` quand la lecture ne dépend d'aucune ligne du registre (première livraison) ;
   - `dossier_des_arrets` : le chemin du dossier des arrêts, relatif au dossier de ce fichier, **le même dans toutes
     les configurations de la course** (vérification du code de la version 7, M-2 : le dossier venait de l'appelant).
     Le code ne reçoit plus ce dossier d'aucun appelant : il le lit ici.

`lire_la_configuration_scellee` vérifie le nom du fichier, celui de son dossier, son compagnon, ses listes fermées de
noms et chacune de ses valeurs, et rend avec elle l'empreinte du fichier. Ce module ne lit que des configurations. Il
ne nomme aucune ligne d'aucune table de verdict.
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
# La chaîne de plus de la version 8, `null` tant que la session principale n'a pas dit comment `piece_source` désigne
# le module (demande 18 de la note du brouillon 26).
CHAINE_DE_LA_CLE_DU_MODULE = "cle_du_module_dans_piece_source"
CHAINES = ("motifs", "motif_au_cas_a", "calculable", "declarations_du_schema", "statistique_agregateur",
           "doses_de_la_famille", "dose_pour_information", "cles_des_doses_dans_lectures", "valeurs_du_champ_dose",
           "quantile_borne_haute", CHAINE_DES_DOSES_DU_FICHIER, CHAINE_DE_LA_CONDITION_DE_L_HONNETE,
           CHAINE_DE_LA_CLE_DU_MODULE)
MODULE_DU_COTE_HABILITE = "sha256_du_module_du_cote_habilite"
RAPPORT_DE_CONTRE_LECTURE = "sha256_du_rapport_de_contre_lecture_du_module"
REGISTRE_ATTENDU = "sha256_du_registre_des_accords"
DOSSIER_DES_ARRETS = "dossier_des_arrets"
PROGRAMME_DU_CONSTAT = "sha256_du_programme_du_constat"                             # brouillon 30
EMPREINTES_ATTENDUES = (MODULE_DU_COTE_HABILITE, RAPPORT_DE_CONTRE_LECTURE, REGISTRE_ATTENDU, PROGRAMME_DU_CONSTAT)
PIECES_ATTENDUES = EMPREINTES_ATTENDUES + (DOSSIER_DES_ARRETS,)                    # cinq entrées
# Dossier d'analyse d'une livraison : `livraison-<rang>/`, rang 1 pour la première (conventions du brouillon 26).
DOSSIER_D_UNE_LIVRAISON = re.compile(r"livraison-([1-9][0-9]*)")
# Constat de lancement (conventions du brouillon 27) : la pièce que rend `scripts/constat_de_lancement_discretion_bras_a_v2.py`,
# rangée dans le dossier de la livraison ; **huit champs et eux seuls** (brouillon 29 : `ligne_de_go`, l'identifiant de
# la ligne de GO que la lecture emploie, `null` pour une première livraison ; brouillon 30 :
# `sha256_du_programme_du_constat`, l'empreinte du programme qui a fait le constat, que le programme d'analyse confronte
# à celle que la configuration inscrit).
NOM_DU_CONSTAT_DE_LANCEMENT = "constat-de-lancement-bras-a.json"
CHAMPS_DU_CONSTAT_DE_LANCEMENT = ("date_utc", "sha256_de_la_configuration", "sha256_du_registre_fige",
                                  "commit_du_registre_courant", "configuration_inscrite", "revocation_entree",
                                  "sha256_du_programme_du_constat", "ligne_de_go")
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
    - `cle_du_module_dans_piece_source` : un texte, ou `null` ;
    - `pieces_attendues`, cinq entrées : l'empreinte du module du côté habilité, celle du rapport de sa
      contre-lecture et celle du programme du constat de lancement, toujours exigées ; celle de l'état figé du registre
      des accords, ou `null` ; le chemin du dossier des arrêts, relatif au dossier de la configuration (barres
      obliques, non absolu)."""
    _liste_fermee(c, RACINE, "racine")
    choix, chaines = c["choix"], c["chaines_du_module"]
    pieces = c["pieces_attendues"]
    _liste_fermee(pieces, PIECES_ATTENDUES, "pièces attendues")
    for nom in EMPREINTES_ATTENDUES:
        if pieces[nom] is None and nom == REGISTRE_ATTENDU:
            continue
        if not isinstance(pieces[nom], str) or _EMPREINTE.fullmatch(pieces[nom]) is None:
            raise GardeArret(f"configuration scellée, `pieces_attendues.{nom}` : une empreinte entière (64 signes) exigée"
                             + (", ou `null`" if nom == REGISTRE_ATTENDU else " — le code ne peut pas la connaître autrement"))
    dites = [pieces[nom] for nom in EMPREINTES_ATTENDUES if pieces[nom] is not None]
    if len(set(dites)) != len(dites):
        raise GardeArret("configuration scellée, `pieces_attendues` : la même empreinte pour deux pièces")
    dossier = pieces[DOSSIER_DES_ARRETS]
    if not isinstance(dossier, str) or not dossier.strip() or "\\" in dossier or "\n" in dossier or dossier.startswith("/") \
            or re.match(r"[A-Za-z]:", dossier):
        raise GardeArret(f"configuration scellée, `pieces_attendues.{DOSSIER_DES_ARRETS}` : chemin relatif au dossier de la "
                         "configuration exigé (barres obliques, non absolu) — le dossier des arrêts ne vient d'aucun appelant")
    _liste_fermee(choix, VALEURS_DES_CHOIX, "choix")
    for nom, permises in VALEURS_DES_CHOIX.items():
        if not isinstance(choix[nom], str) or choix[nom] not in permises:
            raise GardeArret(f"configuration scellée, choix `{nom}` = {choix[nom]!r} : l'un de {permises} exigé, écrit en "
                             "toutes lettres — aucune valeur par défaut")
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
    if chaines[CHAINE_DE_LA_CLE_DU_MODULE] is not None:
        _texte(chaines[CHAINE_DE_LA_CLE_DU_MODULE], f"`{CHAINE_DE_LA_CLE_DU_MODULE}`")
    return c


def lire_la_configuration_scellee(chemin) -> dict:
    """Lit la configuration scellée : le fichier **porte son nom**, est rangé dans **le dossier d'analyse d'une
    livraison** (`livraison-<rang>/`) et répond à son empreinte compagnon ; c'est un objet JSON, sans champ en double ;
    il passe `exiger_configuration`. Rend `{"choix", "chaines_du_module", "pieces_attendues", "sha256", "chemin",
    "rang"}`. Un chemin absent, un fichier d'un autre nom ou d'un autre dossier, non scellé ou retouché, un
    dictionnaire donné à la place du chemin sont refusés (gardes ordinaires : rien n'est lu d'aucune livraison)."""
    try:
        est_un_fichier = isinstance(chemin, (str, Path)) and Path(chemin).is_file()
    except OSError:
        est_un_fichier = False
    if not est_un_fichier:
        raise GardeArret("configuration scellée : le chemin d'un fichier scellé est exigé — un dictionnaire donné par "
                         "l'appelant n'est pas admis (contre-lecture du code de la version 5, C-2)")
    if Path(chemin).name != NOM_DU_FICHIER_DE_LA_CONFIGURATION:
        raise GardeArret(f"configuration scellée : fichier `{NOM_DU_FICHIER_DE_LA_CONFIGURATION}` exigé (conventions)")
    rang = DOSSIER_D_UNE_LIVRAISON.fullmatch(Path(chemin).resolve().parent.name)
    if rang is None:
        raise GardeArret("configuration scellée : elle se range dans le dossier d'analyse de sa livraison, `livraison-<rang>/` "
                         "(rang 1 pour la première) — une configuration par livraison (conventions)")
    verifier(chemin)
    brut = Path(chemin).read_bytes()
    try:
        c = json.loads(brut.decode("utf-8"), object_pairs_hook=_sans_doublon)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise GardeArret("configuration scellée : JSON illisible") from None
    exiger_configuration(c)
    return {"choix": c["choix"], "chaines_du_module": c["chaines_du_module"], "pieces_attendues": c["pieces_attendues"],
            "sha256": hashlib.sha256(brut).hexdigest(), "chemin": str(Path(chemin)), "rang": int(rang.group(1))}


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


def _lue(configuration) -> Mapping:
    if not isinstance(configuration, Mapping) or not {"sha256", "chemin", "rang", "pieces_attendues", "choix"} <= set(configuration):
        raise GardeArret("configuration lue du fichier scellé exigée (`lire_la_configuration_scellee`)")
    return configuration


def registre_attendu(configuration: Mapping) -> str:
    """Empreinte du registre lu : le registre des accords de la branche principale **dans son état figé au scellement
    de la configuration**. `null` : la lecture ne dépend d'aucune ligne du registre — demander une ligne sous cette
    configuration arrête, en le disant."""
    attendue = _lue(configuration)["pieces_attendues"][REGISTRE_ATTENDU]
    if attendue is None:
        raise GardeArret("la configuration scellée ne dit pas quel registre des accords lire "
                         f"(`pieces_attendues.{REGISTRE_ATTENDU}` est `null`) : aucune ligne de GO ne se lit sous elle — une "
                         "livraison refaite a sa configuration, qui porte l'empreinte du registre de la branche principale "
                         "dans son état figé au scellement de cette configuration")
    return attendue


def module_du_cote_habilite(configuration: Mapping) -> str:
    """Empreinte du module du côté habilité que la configuration scellée inscrit."""
    return _lue(configuration)["pieces_attendues"][MODULE_DU_COTE_HABILITE]


def rapport_de_contre_lecture(configuration: Mapping) -> str:
    """Empreinte du rapport de contre-lecture du module que la configuration scellée inscrit."""
    return _lue(configuration)["pieces_attendues"][RAPPORT_DE_CONTRE_LECTURE]


def programme_du_constat(configuration: Mapping) -> str:
    """Empreinte du programme du constat de lancement que la configuration scellée inscrit (brouillon 30)."""
    return _lue(configuration)["pieces_attendues"][PROGRAMME_DU_CONSTAT]


def cle_du_module_dans_piece_source(configuration: Mapping) -> str | None:
    """Nom de la clé de `piece_source` qui porte l'empreinte du module, ou `None` si elle n'est pas inscrite."""
    return _lue(configuration)["chaines_du_module"][CHAINE_DE_LA_CLE_DU_MODULE]


def dossier_de_la_livraison(configuration: Mapping) -> Path:
    """Le dossier d'analyse de la livraison, `livraison-<rang>/` : celui de la configuration. Le fichier de l'étape
    (m) de cette livraison et ses constats s'y rangent."""
    return Path(_lue(configuration)["chemin"]).resolve().parent


def dossier_des_arrets(configuration: Mapping) -> Path:
    """Le dossier des arrêts que la configuration scellée nomme, résolu contre le dossier de son fichier. **Il ne
    vient d'aucun appelant.** Il doit exister (il peut être vide). Il est **à part** : ni le dossier d'une livraison,
    ni sous lui, ni au-dessus de lui."""
    c = _lue(configuration)
    base = dossier_de_la_livraison(c)
    dossier = (base / c["pieces_attendues"][DOSSIER_DES_ARRETS]).resolve()
    if not dossier.is_dir():
        raise GardeArret(f"dossier des arrêts que la configuration scellée nomme ({c['pieces_attendues'][DOSSIER_DES_ARRETS]}) : "
                         "dossier existant exigé (il peut être vide)")
    dans_une_livraison = any(p.parent == base.parent and DOSSIER_D_UNE_LIVRAISON.fullmatch(p.name) for p in (dossier, *dossier.parents))
    if dans_une_livraison or dossier in base.parents:
        raise GardeArret("dossier des arrêts : il est à part, commun à toutes les livraisons — ni le dossier d'analyse d'une "
                         "livraison, ni sous lui, ni au-dessus de lui (conventions)")
    return dossier


def configurations_de_la_course(configuration: Mapping) -> dict[int, Mapping]:
    """Les configurations scellées de la course, une par dossier `livraison-<rang>/` voisin de celui de la
    configuration donnée (elle comprise), par rang. Un dossier de livraison sans configuration est refusé."""
    c = _lue(configuration)
    course = dossier_de_la_livraison(c).parent
    lues = {}
    for d in sorted(course.iterdir()):
        rang = DOSSIER_D_UNE_LIVRAISON.fullmatch(d.name)
        if rang is None or not d.is_dir():
            continue
        lues[int(rang.group(1))] = lire_la_configuration_scellee(d / NOM_DU_FICHIER_DE_LA_CONFIGURATION)
    if lues.get(c["rang"]) != dict(c):
        raise GardeArret("configuration scellée : celle qui est donnée n'est pas celle que porte son dossier de livraison")
    return lues


def exiger_configurations_de_la_course(configuration: Mapping) -> dict[int, Mapping]:
    """Garde des configurations de la course (conventions du brouillon 26) : **les cinq choix sont les mêmes pour
    toutes les livraisons**, et **le dossier des arrêts est le même dans toutes les configurations**. Un écart est
    refusé (garde ordinaire : rien n'est lu d'aucune livraison). Rend les configurations, par rang."""
    c = _lue(configuration)
    toutes = configurations_de_la_course(c)
    dossier = dossier_des_arrets(c)
    for rang, autre in toutes.items():
        if autre["choix"] != c["choix"]:
            raise GardeArret(f"configurations de la course : les cinq choix de `livraison-{rang}/` ne sont pas ceux de "
                             f"`livraison-{c['rang']}/` — ils sont les mêmes pour toutes les livraisons (conventions) : un "
                             "écart est un écart au préenregistrement")
        if dossier_des_arrets(autre) != dossier:
            raise GardeArret(f"configurations de la course : le dossier des arrêts de `livraison-{rang}/` n'est pas celui de "
                             f"`livraison-{c['rang']}/` — il est le même dans toutes les configurations de la course")
    return toutes
