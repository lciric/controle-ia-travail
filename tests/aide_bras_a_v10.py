"""Aides des essais du bras A, version 10 du code : courses, livraisons, configurations, registres et constats de
lancement **fabriqués pour l'essai**.

Rien ici ne vient du module du côté habilité : les chaînes de `motif`, les déclarations du schéma, la statistique de
l'agrégateur, la forme des doses et les empreintes du module et de son rapport de contre-lecture sont **inventées**,
pour éprouver que le code les lit dans la configuration scellée et n'en devine aucune. Les choix nommés ont ici une
valeur par commodité d'essai — chaque essai qui porte sur un choix le donne en toutes lettres ; le code, lui, n'en a
aucune par défaut.

**Rangement d'une course fabriquée** (conventions des brouillons 26 à 30) : un dossier de course, qui porte le dossier
des arrêts (`arrets/`, commun) et un dossier d'analyse par livraison (`livraison-<rang>/`), où se rangent la
configuration de la livraison, son constat de lancement, et, si elle est lue, les constats de l'étape (m), le fichier
de l'étape (m) et le fichier des grandeurs de l'étape (n).

**Constat de lancement** : `constat` le fait par le programme (`scripts/constat_de_lancement_discretion_bras_a_v3.py`) ;
`constat_a_la_main` écrit et scelle un constat aux huit bons champs sans passer par le programme — le programme
d'analyse ne distingue pas l'un de l'autre (c'est une garde de procédure), et les essais s'en servent pour atteindre
les gardes de l'analyse que le programme du constat aurait arrêtées avant elle. **Contrôle de lancement** : `controle`
joue le programme en mode de contrôle ; sain ou malsain, il scelle `controle-de-lancement-bras-a-<date>.json` dans le
dossier de la livraison — l'analyse exige que le plus récent soit sain, et en exige un pour un rejeu après un acte de
reprise. **Provenance** : la clé de `piece_source` qui porte l'empreinte du module est obligatoire (brouillon 33) ;
les pièces fabriquées la portent (`provenance`), sous un nom de clé inventé (`CLE_DU_MODULE`)."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

from controle_ia.organismes_discrets import analyse_bras_a_v10 as an
from controle_ia.organismes_discrets import arrets_bras_a_v10 as ar
from controle_ia.organismes_discrets import configuration_bras_a_v10 as cf
from controle_ia.organismes_discrets import graines_bras_a_v10 as g
from controle_ia.scellement import sceller

N = 2000
Q = 1 - 0.05 / 15
MODULE = "c" * 64          # empreinte inventée du module du côté habilité (la vraie n'est pas ouverte par la relance)
RAPPORT = "b" * 64         # empreinte inventée du rapport de sa contre-lecture
COMMIT = "0123abc"         # commit inventé du registre courant
CLE_DU_MODULE = "sha256_du_module"      # nom inventé de la clé de `piece_source` qui porte l'empreinte du module
DATE = "2099-01-01T00:00:00Z"
_COMPTEUR = itertools.count()

# Le programme du constat de lancement, chargé de son fichier (`scripts/` n'est pas un paquet).
_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "constat_de_lancement_discretion_bras_a_v3.py"
_spec = importlib.util.spec_from_file_location("constat_de_lancement_discretion_bras_a_v3", _SCRIPT)
constat_de_lancement = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(constat_de_lancement)
PROGRAMME = hashlib.sha256(_SCRIPT.read_bytes()).hexdigest()      # l'empreinte du programme du constat, que la configuration inscrit

# Chaînes inventées du module (les vraies ne sont pas transmises à la relance).
M_PLI, M_CLASSE, M_NON_AJUSTABLE = "pli sans action (essai)", "classe absente (essai)", "moniteur appris non ajustable (essai)"
M_PERDUES, M_DEGENERES, M_IMPOSSIBLE = "permutations perdues (essai)", "tirages dégénérés (essai)", "intervalle impossible (essai)"
MOTIFS = {M_PLI: cf.CAUSE_ANTERIEURE, M_CLASSE: cf.CAUSE_ANTERIEURE, M_NON_AJUSTABLE: cf.CAUSE_NON_AJUSTABLE,
          M_PERDUES: cf.CAUSE_PERMUTATIONS_PERDUES, M_DEGENERES: cf.CAUSE_TIRAGES_DEGENERES,
          M_IMPOSSIBLE: cf.CAUSE_INTERVALLE_IMPOSSIBLE}
# Ce que la configuration inscrit : la déclaration du seul schéma que le texte garde, l'échange dans chaque paire.
DECLARATIONS = {cf.SCHEMA_ECHANGE: {"permutation": "echange dans la paire (essai)", "unite_de_la_permutation": "paire (essai)"}}
# Ce qu'une livraison peut déclarer dans ses réglages : le schéma retenu — ou, pour un artefact, la permutation libre
# d'un module resté à la rédaction retirée.
REGLAGES_DU_SCHEMA = {**DECLARATIONS, cf.SCHEMA_LIBRE: {"permutation": "libre dans la tache (essai)", "unite_de_la_permutation": "episode (essai)"}}
CHOIX = {cf.CHOIX_SCHEMA: cf.SCHEMA_ECHANGE, cf.CHOIX_SEUIL: cf.SEUIL_SUR_LES_DEMANDES,
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


def empreinte(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def configuration(choix=None, pieces=None, **chaines):
    """Contenu d'une configuration : les cinq choix (ceux de l'essai, changés par `choix`), les chaînes inventées, et
    les cinq pièces attendues — le module et son rapport de contre-lecture inventés, aucun registre, l'empreinte du
    programme du constat, le dossier des arrêts de la course (`../arrets`) —, sauf données par `pieces`."""
    attendues = {cf.MODULE_DU_COTE_HABILITE: MODULE, cf.RAPPORT_DE_CONTRE_LECTURE: RAPPORT, cf.REGISTRE_ATTENDU: None,
                 cf.PROGRAMME_DU_CONSTAT: PROGRAMME, cf.DOSSIER_DES_ARRETS: "../arrets"}
    attendues.update(pieces or {})
    c = {"choix": {**CHOIX, **(choix or {})}, "pieces_attendues": attendues,
         "chaines_du_module": {"motifs": dict(MOTIFS), "motif_au_cas_a": None, "calculable": {"A": True, "D": False, "E": False},
                               "declarations_du_schema": json.loads(json.dumps(DECLARATIONS)),
                               "statistique_agregateur": "moyenne (essai)",
                               "doses_de_la_famille": ["dose-0.50", "dose-0.75", "dose-1.00"],
                               "dose_pour_information": "dose-0.25",
                               "cles_des_doses_dans_lectures": {d: d for d in ar.FORMES_DOSE},
                               "valeurs_du_champ_dose": {d: d for d in ar.FORMES_DOSE},
                               "quantile_borne_haute": Q,
                               cf.CHAINE_DES_DOSES_DU_FICHIER: {d: d for d in ar.FORMES_DOSE},
                               cf.CHAINE_DE_LA_CONDITION_DE_L_HONNETE: "honnete",
                               cf.CHAINE_DE_LA_CLE_DU_MODULE: CLE_DU_MODULE}}
    c["chaines_du_module"].update(chaines)
    return c


def nouvelle_course(tmp):
    """Un dossier de course neuf, avec son dossier des arrêts, vide."""
    course = nouveau_dossier(tmp, "course")
    (course / "arrets").mkdir()
    return course


def fichier_de_configuration(tmp, choix=None, pieces=None, course=None, rang=1, **chaines):
    """Écrit et scelle la configuration d'une livraison, dans `livraison-<rang>/` d'une course (neuve, sauf donnée)."""
    course = nouvelle_course(tmp) if course is None else Path(course)
    return ecrire_scelle(course / f"livraison-{rang}" / cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION, configuration(choix, pieces, **chaines))


def dossier_des_arrets(configuration_scellee):
    return cf.dossier_des_arrets(cf.lire_la_configuration_scellee(configuration_scellee))


def dossier_de_la_livraison(configuration_scellee):
    return Path(configuration_scellee).parent


def registre(dossier, lignes, nom="go.md"):
    """Registre des accords fabriqué pour l'essai (table à barres verticales ; troisième colonne : le type)."""
    f = Path(dossier) / nom
    f.write_text("# Registre des accords (fabriqué pour l'essai)\n\n| identifiant | date | type | objet |\n|---|---|---|---|\n"
                 + "".join(l + "\n" for l in lignes), encoding="utf-8")
    return f


def ligne_d_inscription(configuration_scellee, go="GO-2099-12-31-01"):
    """La ligne d'inscription d'une configuration, fabriquée dans la forme du texte : type « inscription », la marque,
    puis l'empreinte entière (les deux constantes de `graines_bras_a_v10`)."""
    return (f"| {go} | 2099-12-31 | {g.TYPE_DE_LA_LIGNE_D_INSCRIPTION} | {g.MARQUE_DE_LA_LIGNE_D_INSCRIPTION} "
            f"{empreinte(configuration_scellee)} |")


def lignes_figees(registre_fige):
    return [] if registre_fige is None else Path(registre_fige).read_text(encoding="utf-8").splitlines()[4:]


def constat_et_causes(tmp, configuration_scellee, registre_fige=None, lignes_de_plus=(), inscrite=True, ligne_de_go=None,
                      mode=None):
    """Fait le constat de lancement d'une configuration, **par le programme** : le registre courant fabriqué porte les
    lignes de l'état figé (s'il y en a un), la ligne d'inscription de la configuration (sauf `inscrite=False`), et
    les lignes de plus. Rend (constat, chemin du fichier scellé ou `None`, causes)."""
    courant = registre(nouveau_dossier(tmp, "registre-courant"),
                       lignes_figees(registre_fige) + ([ligne_d_inscription(configuration_scellee)] if inscrite else [])
                       + list(lignes_de_plus))
    return constat_de_lancement.constater(configuration_scellee, courant, commit_du_registre_courant=COMMIT, date_utc=DATE,
                                          registre_fige=registre_fige, ligne_de_go=ligne_de_go,
                                          mode=constat_de_lancement.MODE_CONSTAT if mode is None else mode)


def constat(tmp, configuration_scellee, registre_fige=None, lignes_de_plus=(), inscrite=True, ligne_de_go=None):
    """Comme `constat_et_causes`, sans les causes : (constat, chemin du fichier scellé ou `None`)."""
    return constat_et_causes(tmp, configuration_scellee, registre_fige, lignes_de_plus, inscrite, ligne_de_go)[:2]


PLUS_TARD = "2099-01-03T12:00:00Z"     # une date de contrôle, postérieure à celle des constats de l'essai


def controle(tmp, configuration_scellee, registre_fige=None, ligne_de_go=None, lignes_de_plus=(), date_utc=PLUS_TARD, commit="89abcde"):
    """Joue le programme du constat **à titre de contrôle** (avant un rejeu), sur un registre courant fabriqué : les
    lignes de l'état figé, la ligne d'inscription, et les lignes de plus. Rend (constat du contrôle, chemin du
    contrôle scellé — sain ou malsain —, causes : vides s'il est sain)."""
    courant = registre(nouveau_dossier(tmp, "registre-courant"),
                       lignes_figees(registre_fige) + [ligne_d_inscription(configuration_scellee)] + list(lignes_de_plus))
    return constat_de_lancement.constater(configuration_scellee, courant, commit_du_registre_courant=commit, date_utc=date_utc,
                                          registre_fige=registre_fige, ligne_de_go=ligne_de_go,
                                          mode=constat_de_lancement.MODE_CONTROLE)


def constat_a_la_main(configuration_scellee, ligne_de_go=None, **change):
    """Écrit et scelle, **sans le programme**, un constat aux huit champs, sain, pour cette configuration et cette
    ligne de GO (`change` : des champs à changer, ou à retirer s'ils valent `...`). Le programme d'analyse ne le
    distingue pas de celui du programme : garde de procédure, tenue par la session qui lance."""
    lue = cf.lire_la_configuration_scellee(configuration_scellee)
    c = {"date_utc": DATE, "sha256_de_la_configuration": lue["sha256"],
         "sha256_du_registre_fige": lue["pieces_attendues"][cf.REGISTRE_ATTENDU], "commit_du_registre_courant": COMMIT,
         "configuration_inscrite": True, "revocation_entree": False,
         "sha256_du_programme_du_constat": lue["pieces_attendues"][cf.PROGRAMME_DU_CONSTAT], "ligne_de_go": ligne_de_go}
    c.update(change)
    c = {k: x for k, x in c.items() if x is not ...}
    return ecrire_scelle(Path(configuration_scellee).parent / cf.NOM_DU_CONSTAT_DE_LANCEMENT, c)


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


def reglages(schema=cf.SCHEMA_ECHANGE, **plus):
    r = {"n_permutations": N, "n_tirages": N, "taille_de_la_famille": 15, "niveau": 0.05,
         "statistique_agregateur": "moyenne (essai)", "doses_de_la_famille": ["dose-0.50", "dose-0.75", "dose-1.00"],
         "dose_pour_information": "dose-0.25", **REGLAGES_DU_SCHEMA[schema]}
    r.update(plus)
    return r


def provenance(note, module=MODULE):
    """Le `piece_source` d'une pièce fabriquée : l'empreinte du module, sous la clé que la configuration de l'essai
    inscrit, et une note qui distingue les pièces."""
    return {CLE_DU_MODULE: module, "note": note}


def sortie(change=None, schema=cf.SCHEMA_ECHANGE, **cles):
    """Sortie fabriquée de la lecture commune, aux onze noms de la version 8 : les cinq moniteurs aux quatre doses, tous
    au cas A et « ne repèrent pas », sauf ce qui est donné dans `change[(moniteur, dose)]`."""
    lectures = {forme(d): {mo: cas_a(mo, d) for mo in an.MONITEURS} for d in an.QUATRE_DOSES}
    for (mo, d), e in (change or {}).items():
        lectures[forme(d)][mo] = e
    s = {"plis": {"t00": 0, "t01": 1}, "lectures": lectures, "piece_source": provenance("piece-fabriquee-pour-l-essai"),
         "reglages": reglages(schema),
         "agregateur_somme_sans_etat": {forme(d): 0.51 for d in an.QUATRE_DOSES},        # un seul nombre par dose (brouillon 31)
         "agregateur_maximum_sans_etat": {forme(d): 0.55 for d in an.QUATRE_DOSES},
         "exclues": {"non lu": 3}, "preuve_d_ordre": {"ouvertures": 5},
         "scores_par_unite": {"fichier": an.NOM_DU_FICHIER_DES_RANGS, "sha256": "0" * 64, "lignes": 0,
                              "champs": list(an.CHAMPS_DU_FICHIER_DES_RANGS), "forme": "rang moyen dans le pli"},
         "comptes_des_lectures": {"juge": 2560}, "nombres_rendus": ["aire", "valeur_p_haut"]}
    s.update(cles)
    if isinstance(s.get("piece_source"), str):                # un texte : la note d'une pièce qui vient bien du module de l'essai
        s["piece_source"] = provenance(s["piece_source"])
    return s


def piece(tmp, contenu):
    """Écrit et scelle une pièce « du côté habilité » fabriquée ; rend son chemin."""
    return ecrire_scelle(nouveau_dossier(tmp, "livraison") / "sortie-de-la-lecture-commune-fabriquee.json", contenu)


def regle(tmp, change=None, choix=None, contenu=None, course=None, rang=1, go=None, registre_fige=None, chaines=None,
          pieces=None, **cles):
    """Écrit la pièce, la configuration de la livraison (dans une course neuve, sauf donnée) et son constat de
    lancement, puis lit la règle de discrétion."""
    schema = (choix or {}).get(cf.CHOIX_SCHEMA, cf.SCHEMA_ECHANGE)
    p = piece(tmp, sortie(change, schema, **cles) if contenu is None else contenu)
    c = fichier_de_configuration(tmp, choix, pieces, course, rang, **(chaines or {}))
    constat(tmp, c, registre_fige, ligne_de_go=go)
    return an.regle_de_discretion(p, c, go_de_la_reprise=go, registre_fige=registre_fige)


def ligne_de_reprise(go, fichier_d_arret, phrase=None, module=MODULE, rapport=RAPPORT, plus=""):
    """Ligne d'accord d'une livraison refaite, fabriquée : la phrase, et les trois empreintes entières — fichier
    d'arrêt de la livraison refusée, module corrigé et rapport de sa contre-lecture (ceux que la configuration de
    l'essai inscrit)."""
    phrase = g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE if phrase is None else phrase
    return (f"| {go} | 2099-01-01 | décision | {phrase} ; fichier d'arrêt {empreinte(fichier_d_arret)} ; module corrigé "
            f"{module} ; rapport de contre-lecture {rapport}{plus} |")


def fichier_d_arret(dossier, piece_refusee):
    """Chemin du fichier d'arrêt d'une livraison refusée, dans le dossier des arrêts."""
    return Path(dossier) / an.NOM_DES_FICHIERS_D_ARRET.format(empreinte(piece_refusee)[:16])
