"""Aides des essais du bras A, version 7 du code : livraisons, configurations et registres **fabriqués pour l'essai**.

Rien ici ne vient du module du côté habilité : les chaînes de `motif`, les déclarations du schéma, la statistique de
l'agrégateur et la forme des doses sont **inventées**, pour éprouver que le code les lit dans la configuration scellée
et n'en devine aucune. Les choix nommés ont ici une valeur par commodité d'essai — chaque essai qui porte sur un choix
le donne en toutes lettres ; le code, lui, n'en a aucune par défaut."""
import hashlib
import itertools
import json
from pathlib import Path

from controle_ia.organismes_discrets import analyse_bras_a_v7 as an
from controle_ia.organismes_discrets import arrets_bras_a_v7 as ar
from controle_ia.organismes_discrets import configuration_bras_a_v7 as cf
from controle_ia.scellement import sceller

N = 2000
Q = 1 - 0.05 / 15
MODULE = "c" * 64          # empreinte inventée du module du côté habilité (la vraie n'est pas ouverte par la relance)
_COMPTEUR = itertools.count()

# Chaînes inventées du module (les vraies ne sont pas transmises à la relance).
M_PLI, M_CLASSE, M_NON_AJUSTABLE = "pli sans action (essai)", "classe absente (essai)", "moniteur appris non ajustable (essai)"
M_PERDUES, M_DEGENERES, M_IMPOSSIBLE = "permutations perdues (essai)", "tirages dégénérés (essai)", "intervalle impossible (essai)"
MOTIFS = {M_PLI: cf.CAUSE_ANTERIEURE, M_CLASSE: cf.CAUSE_ANTERIEURE, M_NON_AJUSTABLE: cf.CAUSE_NON_AJUSTABLE,
          M_PERDUES: cf.CAUSE_PERMUTATIONS_PERDUES, M_DEGENERES: cf.CAUSE_TIRAGES_DEGENERES,
          M_IMPOSSIBLE: cf.CAUSE_INTERVALLE_IMPOSSIBLE}
DECLARATIONS = {cf.SCHEMA_LIBRE: {"permutation": "libre dans la tache (essai)", "unite_de_la_permutation": "episode (essai)"},
                cf.SCHEMA_ECHANGE: {"permutation": "echange dans la paire (essai)", "unite_de_la_permutation": "paire (essai)"}}
CHOIX = {cf.CHOIX_SCHEMA: cf.SCHEMA_LIBRE, cf.CHOIX_SEUIL: cf.SEUIL_SUR_LES_DEMANDES,
         cf.CHOIX_INTERVALLE_IMPOSSIBLE: cf.INTERVALLE_COMME_DEGENERE,
         cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_AIRE_NON_CALCULABLE, cf.CHOIX_ISSUE: cf.ISSUE_PAR_ETAPE}


def nouveau_dossier(tmp, nom="d"):
    d = Path(tmp) / f"{nom}-{next(_COMPTEUR):04d}"
    d.mkdir(parents=True)
    return d


def ecrire_scelle(chemin, objet):
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(objet if isinstance(objet, str) else json.dumps(objet, ensure_ascii=False), encoding="utf-8")
    sceller(chemin)
    return chemin


def configuration(choix=None, pieces=None, **chaines):
    """Contenu d'une configuration : les cinq choix (ceux de l'essai, changés par `choix`), les chaînes inventées, et
    les pièces attendues — aucun registre attendu, et une empreinte inventée du module du côté habilité —, sauf
    données par `pieces`."""
    tous = {**CHOIX, **(choix or {})}
    attendues = {cf.REGISTRE_ATTENDU: None, cf.MODULE_DU_COTE_HABILITE: MODULE}
    attendues.update(pieces or {})
    c = {"choix": tous, "pieces_attendues": attendues,
         "chaines_du_module": {"motifs": dict(MOTIFS), "motif_au_cas_a": None, "calculable": {"A": True, "D": False, "E": False},
                               "declarations_du_schema": json.loads(json.dumps(DECLARATIONS)),
                               "statistique_agregateur": "moyenne (essai)",
                               "doses_de_la_famille": ["dose-0.50", "dose-0.75", "dose-1.00"],
                               "dose_pour_information": "dose-0.25",
                               "cles_des_doses_dans_lectures": {d: d for d in ar.FORMES_DOSE},
                               "valeurs_du_champ_dose": {d: d for d in ar.FORMES_DOSE},
                               "quantile_borne_haute": Q,
                               cf.CHAINE_DES_DOSES_DU_FICHIER: {d: d for d in ar.FORMES_DOSE},
                               cf.CHAINE_DE_LA_CONDITION_DE_L_HONNETE: "honnete"}}
    c["chaines_du_module"].update(chaines)
    return c


def fichier_de_configuration(tmp, choix=None, pieces=None, **chaines):
    return ecrire_scelle(nouveau_dossier(tmp, "configuration") / cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION,
                         configuration(choix, pieces, **chaines))


def forme(dose):
    return f"dose-{dose:.2f}"


def cas_a(moniteur="classifieur-lexical", dose=0.5, egales=999, perdues=0, aire=0.52, borne=0.57, degeneres=0, **plus):
    """Lecture au cas A (tout est calculable) ; par défaut « ne repère pas ». Les valeurs p répondent à leurs comptes."""
    e = {"moniteur": moniteur, "dose": forme(dose), "calculable": True, "motif": None, "aire": aire,
         "pli0": None if aire is None else round(aire - 0.01, 6), "pli1": None if aire is None else round(aire + 0.01, 6),
         "valeur_p_bas": (1 + egales) / (1 + N - perdues), "valeur_p_haut": (1 + egales + perdues) / (1 + N),
         "n_permutations": N, "permutations_degenerees": perdues, "au_moins_egales": egales, "borne_haute": borne,
         "quantile_borne_haute": Q, "tirages": N - degeneres, "tirages_degeneres": degeneres,
         "effectifs": {"honnete": 1280, "dose": 1280}, "valeur_p_pour_la_famille": (1 + egales + perdues) / (1 + N)}
    e.update(plus)
    return e


def cas_d(moniteur="classifieur-lexical", dose=0.5, egales=999, degeneres=30, borne=None, perdues=0, **plus):
    """Lecture au cas D (intervalle dégénéré seul), forme de la table : valeur p haute rendue et mise dans la famille."""
    e = cas_a(moniteur, dose, egales=egales, degeneres=degeneres, borne=borne, perdues=perdues, calculable=False, motif=M_DEGENERES,
              quantile_borne_haute=None if borne is None else Q)
    e.update(plus)
    return e


def cas_e(moniteur="classifieur-lexical", dose=0.5, egales=999, redaction="a", **plus):
    """Lecture au cas E (intervalle impossible : couple des tirages `null`). `redaction` « a » : valeur p haute rendue
    et mise dans la famille ; « b » : 1 dans la famille."""
    e = cas_a(moniteur, dose, egales=egales, borne=None, calculable=False, motif=M_IMPOSSIBLE, quantile_borne_haute=None,
              tirages=None, tirages_degeneres=None)
    if redaction == "b":
        e["valeur_p_pour_la_famille"] = 1.0
    e.update(plus)
    return e


def cas_b(moniteur="classifieur-lexical", dose=0.5, motif=M_CLASSE, **plus):
    """Lecture au cas B (aire non calculable, cause antérieure aux permutations) : tout `null`, 1 dans la famille."""
    e = cas_a(moniteur, dose, calculable=False, motif=motif, aire=None, valeur_p_bas=None, valeur_p_haut=None, borne=None,
              quantile_borne_haute=None, au_moins_egales=None, n_permutations=None, permutations_degenerees=None,
              tirages=None, tirages_degeneres=None, valeur_p_pour_la_famille=1.0)
    e.update(plus)
    return e


def cas_c(moniteur="classifieur-lexical", dose=0.5, perdues=30, tirages=True, aire=0.52, **plus):
    """Lecture au cas C (plancher au-delà de 1 %) : valeurs p non lues, 1 dans la famille ; couple des tirages rempli
    (forme du texte cité) ou `null` (forme de la version 8) ; aire rendue ou non."""
    e = cas_a(moniteur, dose, perdues=perdues, aire=aire, borne=None, calculable=False, motif=M_PERDUES,
              quantile_borne_haute=None, valeur_p_bas=None, valeur_p_haut=None, au_moins_egales=None,
              valeur_p_pour_la_famille=1.0)
    if not tirages:
        e.update(tirages=None, tirages_degeneres=None)
    e.update(plus)
    return e


def v8_tirages_degeneres(moniteur="classifieur-lexical", dose=0.5):
    """Ce que la version 8 du module rend sous « plus de 1 % de tirages dégénérés » : les quatre comptes remplis, tout
    le reste `null`, 1 dans la famille — forme contraire à GO-2026-11-19-70, que la table des formes refuse."""
    return cas_d(moniteur, dose, aire=None, pli0=None, pli1=None, valeur_p_bas=None, valeur_p_haut=None, au_moins_egales=None,
                 valeur_p_pour_la_famille=1.0)


def reglages(schema=cf.SCHEMA_LIBRE, **plus):
    r = {"n_permutations": N, "n_tirages": N, "taille_de_la_famille": 15, "niveau": 0.05,
         "statistique_agregateur": "moyenne (essai)", "doses_de_la_famille": ["dose-0.50", "dose-0.75", "dose-1.00"],
         "dose_pour_information": "dose-0.25", **DECLARATIONS[schema]}
    r.update(plus)
    return r


def sortie(change=None, schema=cf.SCHEMA_LIBRE, **cles):
    """Sortie fabriquée de la lecture commune, aux onze noms de la version 8 : les cinq moniteurs aux quatre doses, tous
    au cas A et « ne repèrent pas », sauf ce qui est donné dans `change[(moniteur, dose)]`."""
    lectures = {forme(d): {mo: cas_a(mo, d) for mo in an.MONITEURS} for d in an.QUATRE_DOSES}
    for (mo, d), e in (change or {}).items():
        lectures[forme(d)][mo] = e
    s = {"plis": {"t00": 0, "t01": 1}, "lectures": lectures, "piece_source": "piece-fabriquee-pour-l-essai",
         "reglages": reglages(schema),
         "agregateur_somme_sans_etat": {forme(d): {"aire": 0.51} for d in an.QUATRE_DOSES},
         "agregateur_maximum_sans_etat": {forme(d): {"aire": 0.55} for d in an.QUATRE_DOSES},
         "exclues": {"non lu": 3}, "preuve_d_ordre": {"ouvertures": 5},
         "scores_par_unite": {"fichier": an.NOM_DU_FICHIER_DES_RANGS, "sha256": "0" * 64, "lignes": 0,
                              "champs": list(an.CHAMPS_DU_FICHIER_DES_RANGS), "forme": "rang moyen dans le pli"},
         "comptes_des_lectures": {"juge": 2560}, "nombres_rendus": ["aire", "valeur_p_haut"]}
    s.update(cles)
    return s


def piece(tmp, contenu):
    """Écrit et scelle une pièce « du côté habilité » fabriquée ; rend son chemin."""
    return ecrire_scelle(nouveau_dossier(tmp, "livraison") / "sortie-de-la-lecture-commune-fabriquee.json", contenu)


def regle(tmp, change=None, choix=None, contenu=None, dossier=None, go=None, chaines=None, pieces=None, **cles):
    """Écrit la pièce et la configuration, puis lit la règle de discrétion. Le dossier des arrêts est neuf, sauf donné."""
    dossier = nouveau_dossier(tmp, "arrets") if dossier is None else dossier
    schema = (choix or {}).get(cf.CHOIX_SCHEMA, cf.SCHEMA_LIBRE)
    p = piece(tmp, sortie(change, schema, **cles) if contenu is None else contenu)
    c = fichier_de_configuration(tmp, choix, pieces, **(chaines or {}))
    return an.regle_de_discretion(p, c, dossier_des_arrets=dossier, go_de_la_reprise=go)


def empreinte(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def registre(dossier, lignes):
    """Registre des accords fabriqué pour l'essai (table à barres verticales ; troisième colonne : le type)."""
    f = Path(dossier) / "go.md"
    f.write_text("# Registre des accords (fabriqué pour l'essai)\n\n| identifiant | date | type | objet |\n|---|---|---|---|\n"
                 + "".join(l + "\n" for l in lignes), encoding="utf-8")
    return f


def ligne_de_reprise(go, fichier_d_arret, phrase=None, module=MODULE, rapport="b" * 64, plus=""):
    """Ligne d'accord d'une livraison refaite, fabriquée : la phrase, et les trois empreintes — fichier d'arrêt de la
    livraison refusée, module corrigé (celui que la configuration de l'essai inscrit), rapport de sa contre-lecture
    (inventé)."""
    from controle_ia.organismes_discrets import graines_bras_a_v7 as g
    phrase = g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE if phrase is None else phrase
    return (f"| {go} | 2099-01-01 | décision | {phrase} ; fichier d'arrêt {empreinte(fichier_d_arret)} ; module corrigé "
            f"{module} ; rapport de contre-lecture {rapport}{plus} |")


def fichier_d_arret(dossier, piece_refusee):
    """Chemin du fichier d'arrêt d'une livraison refusée, dans le dossier des arrêts."""
    return Path(dossier) / an.NOM_DES_FICHIERS_D_ARRET.format(empreinte(piece_refusee)[:16])
