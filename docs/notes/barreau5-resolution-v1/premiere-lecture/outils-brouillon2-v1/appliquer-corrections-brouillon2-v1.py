"""Applique au brouillon 1 du texte neuf et au brouillon 1 du devis les 29 remarques (44 couples) de la contre-lecture, a la lettre
(couples « avant », « apres » lus dans l'outil scelle de la contre-lecture, sans les recopier), puis les changements
« hors correction » du redacteur du brouillon 2, ecrits ici un par un. Chaque « avant » doit paraitre une seule fois.
Ecrit les deux brouillons 2 (refus si un fichier existe deja) et un releve JSON. N'ouvre aucun score.
Usage : python3 -B appliquer-corrections-brouillon2-v1.py <racine du depot> <releve .json> [--a-blanc]
"""
import hashlib
import json
import sys
from pathlib import Path

RACINE = Path(sys.argv[1])
A_BLANC = "--a-blanc" in sys.argv
DOS = "docs/notes/barreau5-resolution-v1/premiere-lecture/"
PRE1 = "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md"
PRE2 = "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md"
DEV1 = DOS + "devis-relecture-meme-chemin-v1-brouillon1.md"
DEV2 = DOS + "devis-relecture-meme-chemin-v1-brouillon2.md"
OUTIL = DOS + "contre-lecture-outils-v1/remarques-contre-lecture-v1.py"
ATTENDU = {PRE1: "c5cd92596af8083c5643d1877a9e1a5eed8c3ea77b926b03303f0db263306d43",
           DEV1: "d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d",
           OUTIL: "a37fc7da85d25ade2792038d7c5f14e6b92553f9f3c1fc1c69a63ea8a9855dca"}


def sha(chemin):
    return hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest()


for chemin, attendu in ATTENDU.items():
    assert sha(chemin) == attendu, ("empreinte", chemin)

# Les remarques de la contre-lecture : la liste R de son outil, chargee sans lancer son programme principal.
espace = {"__name__": "remarques_contre_lecture"}
exec(compile((RACINE / OUTIL).read_text(encoding="utf-8"), OUTIL, "exec"), espace)
REMARQUES = espace["R"]

HEURE_FIN = "15:55"

# ---------------------------------------------------------------------------------------------- hors correction, devis
HORS_DEVIS = [
    ("HD1", "en-tête : nom du brouillon",
     "pour la seconde lecture du texte neuf « validité de l'adaptateur pour les sondes apprises sur la tâche » — v1 — brouillon 1",
     "pour la seconde lecture du texte neuf « validité de l'adaptateur pour les sondes apprises sur la tâche » — v1 — brouillon 2"),
    ("HD2", "en-tête : auteur et date du brouillon 2",
     "**Date (UTC)** : 2026-11-19, vers 14:10 (`date -u`).",
     "**Date (UTC)** : 2026-11-19, vers 14:10 (`date -u`). **Brouillon 2** : corrections de la contre-lecture appliquées "
     "par un autre rédacteur neuf, sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`, Claude Fable 5.2, le "
     "2026-11-19 entre 15:25 et " + HEURE_FIN + " environ."),
    ("HD3", "en-tête : statut",
     "- **Statut** : brouillon de devis, scellé comme brouillon, non contre-lu.",
     "- **Statut** : brouillon 2 de devis, scellé comme brouillon. Le brouillon 1 "
     "(`d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d`) a été contre-lu avec le texte neuf "
     "(`" + DOS + "contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md`, "
     "`13bde37898a0…`, empreinte entière dans son compagnon) ; ses trois corrections (B2.4, M7.1, M7.2) sont appliquées "
     "ici ; leur vérification reste à faire (`" + DOS + "table-corrections-brouillon2-v1.md`)."),
    ("HD4", "en-tête : texte servi",
     "- **Texte servi** : `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md`",
     "- **Texte servi** : `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md`"),
    ("HD5", "en-tête : source des nombres ajoutés par la correction M7 (R6)",
     "à verser par la session mère à côté de ce devis. Aucune donnée du programme n'y est ouverte.",
     "à verser par la session mère à côté de ce devis (versées depuis dans `pieces/`, même dossier, empreintes "
     "inchangées). Aucune donnée du programme n'y est ouverte. Les nombres ajoutés au brouillon 2 par la correction M7 "
     "(4,96 heures, ≈ 8,42 USD, manque de 0,29 USD, notation portée à ≈ 99 % par le bloc A) viennent de "
     "`contre-lecture-outils-v1/sortie-arithmetique-contre-lecture-v1.json` "
     "(`14e8de07bf9bf73997df28aac78712172c57eebc8f5a32bdcea5ba3c83b0a23a`), bloc D ; l'outil du devis n'est pas refait."),
    ("HD6", "induit par M7.2 : la phrase « En une ligne » disait sans condition que le pire cas garde les quatre doses",
     "garde les quatre cases du saboteur aux quatre doses et leurs scores (≈ 8,0 USD) ; il perd d'abord",
     "garde les quatre cases du saboteur aux quatre doses et leurs scores (≈ 8,0 USD) si 70 % de la notation revient au "
     "bloc A ; si le bloc A la porte toute (≈ 8,4 USD), ce qui est le cas attendu, la garde par série sacrifie la dose "
     "0,75 du bloc A, puis la 0,25. L'ordre de sacrifice perd d'abord"),
    ("HD7", "induit par M7.2 : le montant du pire cas du bloc A seul ne disait que l'hypothèse des 70 %",
     "**≈ 8,0** pour le bloc A seul, scores poussés (4,66 heures).",
     "**≈ 8,0** pour le bloc A seul, scores poussés (4,66 heures), si 70 % de la notation lui revient ; **≈ 8,4** "
     "(4,96 heures) s'il la porte toute."),
]

EMPREINTE_DEVIS2 = "@@EMPREINTE_DEVIS2@@"

# ---------------------------------------------------------------------------------------------- hors correction, texte
HORS_TEXTE = [
    ("HT1", "en-tête : nom du brouillon",
     "puis relecture des quatre cases par un même chemin de calcul — v1 — brouillon 1",
     "puis relecture des quatre cases par un même chemin de calcul — v1 — brouillon 2"),
    ("HT2", "en-tête : rédacteur du brouillon 2",
     "Il ne sera ni développeur du code de lecture, ni tireur des mondes de l'épreuve, ni lecteur, ni juge d'un verdict de ce texte.",
     "Il ne sera ni développeur du code de lecture, ni tireur des mondes de l'épreuve, ni lecteur, ni juge d'un verdict de ce texte. "
     "**Brouillon 2** : les corrections de la contre-lecture sont appliquées par un autre rédacteur neuf, sous-agent de la "
     "session mère `session_01XJ6Mgr8BN6UanALsQatc5E`, Claude Fable 5.2 (`claude-fable-5-2`), sous les mêmes exclusions "
     "de rôle ; hors de l'en-tête, du paragraphe « Rédacteur du brouillon 2 » et de la section « Contre-lecture », les "
     "« je » de ce texte restent ceux du rédacteur du brouillon 1."),
    ("HT3", "en-tête : date du brouillon 2",
     "(relevés `date -u` : 13:52:27Z au début, 14:32:00Z à la relecture).",
     "(relevés `date -u` : 13:52:27Z au début, 14:32:00Z à la relecture). Brouillon 2 écrit le 2026-11-19, de 15:25 à "
     + HEURE_FIN + " environ (relevé `date -u` : 15:27:27Z à la lecture des pièces)."),
    ("HT4", "en-tête : mandat du brouillon 2",
     "décision 3, option a (relecture des quatre cases par un même chemin, accord de principe, la dépense attend son devis).",
     "décision 3, option a (relecture des quatre cases par un même chemin, accord de principe, la dépense attend son devis). "
     "Brouillon 2 : mandat écrit de la session mère, `" + DOS + "mandat-redacteur-corrections-brouillon2-v1.md`, "
     "`217ea246d7ab30275cd1fd9c6e3ed1eee2f5194219dea4ffd6a55fdfba3e1545`."),
    ("HT5", "en-tête : statut",
     "**brouillon 1, scellé comme brouillon**, non contre-lu, non scellable : il porte des marqueurs (table en fin de texte).",
     "**brouillon 2, scellé comme brouillon** : le brouillon 1 "
     "(`c5cd92596af8083c5643d1877a9e1a5eed8c3ea77b926b03303f0db263306d43`) a été contre-lu, ses corrections sont "
     "appliquées ici, leur vérification reste à faire (section « Contre-lecture ») ; non scellable : il porte des "
     "marqueurs (table en fin de texte)."),
    ("HT6", "en-tête : le devis cité devient son brouillon 2 ; la contre-lecture et ses sorties, que les corrections M1.1 "
            "et m6.1 citent, reçoivent chemin et empreinte (R6)",
     "  - brouillon de devis de la relecture : `docs/notes/barreau5-resolution-v1/premiere-lecture/devis-relecture-meme-chemin-v1-brouillon1.md`, `d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d` ;",
     "  - brouillon de devis de la relecture : `" + DEV2 + "`, `" + EMPREINTE_DEVIS2 + "` (brouillon 2 ; le brouillon 1, "
     "`d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d`, est remplacé) ;\n"
     "  - contre-lecture du brouillon 1 de ce texte : `" + DOS + "contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md`, "
     "`13bde37898a0…` (empreinte entière dans son compagnon `.sha256`) ; ses sorties citées par ce texte, sous "
     "`" + DOS + "contre-lecture-outils-v1/` : `sortie-arithmetique-contre-lecture-v1.json`, "
     "`14e8de07bf9bf73997df28aac78712172c57eebc8f5a32bdcea5ba3c83b0a23a` (bande de la prévision, famille, règle E2) ; "
     "`sortie-simulation-independante-contre-lecture-v1.json`, "
     "`955f8ec9030c432624cf3d9d806daf4750e0d007f8020ac688ea8c77c384a88f` (variante V2, tendance) ;"),
    ("HT7", "exposition du rédacteur du brouillon 2, déclarée (R1)",
     "Aucune sortie de T0.7, de la course exploratoire, du bras A ou du saboteur à budget.",
     "Aucune sortie de T0.7, de la course exploratoire, du bras A ou du saboteur à budget.\n\n"
     "**Rédacteur du brouillon 2.** J'ai lu le brouillon 1 de ce texte, donc toutes les aires qu'il recopie ; sa "
     "contre-lecture, entière, avec la sortie de son arithmétique et le début de son outil des remarques ; le brouillon 1 "
     "du devis ; la note des nœuds restants ; `registres/go.md`, l. 495 ; dans la note 02 du socle, par filtre sur les "
     "seuls nombres que les corrections M6, M9 et m10 insèrent, des fragments des lignes 117, 118, 213, 216, 245, 290, "
     "296, 346, 394, 399, 401 et 419 (j'y ai vu, en plus de ces nombres, deux différences « texte égal moins adaptateur "
     "seul » de la sonde de l'organisme à consigne cachée, +0,0356 et +0,0446, et la suite 0,5111 ; 0,5267 ; 0,8908 du "
     "lecteur honnête) ; les noms des méthodes de `t07bbis/commun_v1.Graines` ; le début du validateur. Je n'ai ouvert "
     "aucun fichier de scores, ni `lecture-bbis.json`, ni le verdict de l'étape B bis, ni aucun fichier interdit par mon "
     "mandat."),
    ("HT8", "section « Contre-lecture » : état réel (le marqueur reste à la session mère)",
     "En attente : ce brouillon n'a pas été contre-lu. La contre-lecture sera faite par un sous-agent neuf d'un autre modèle que le rédacteur (Claude Opus 5.5), qui n'a écrit ni ce texte ni la note de résolution ; son identifiant, l'empreinte du brouillon relu, le chemin et l'empreinte de son rapport et le traitement de chaque remarque seront écrits ici : `<<CONTRE_LECTURE_1>>`.",
     "Le brouillon 1 (`c5cd92596af8083c5643d1877a9e1a5eed8c3ea77b926b03303f0db263306d43`) a été contre-lu le 19 novembre "
     "2026 par un sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Opus 5.5 "
     "(`claude-opus-5-5`), autre modèle que le rédacteur, qui n'a écrit ni ce texte ni la note de résolution. Rapport : "
     "`" + DOS + "contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md` (`13bde37898a0…`, empreinte "
     "entière dans son compagnon). Conclusion : « scellable après ces corrections exactes » ; 3 remarques bloquantes, "
     "10 majeures, 16 mineures : 29 remarques, 44 couples « avant, après », dont 41 dans ce texte et 3 dans le devis. Ce brouillon 2 "
     "les applique tous à la lettre, par programme ; il y ajoute des changements « hors correction », chacun avec sa "
     "raison, dont ceux qu'une correction rend nécessaires, marqués « à trancher par le vérificateur ». Le traitement de "
     "chaque remarque est dans `" + DOS + "table-corrections-brouillon2-v1.md` ; l'outil d'application et son relevé sont "
     "sous `" + DOS + "outils-brouillon2-v1/`. **La vérification des corrections reste à faire.** Écart déclaré à la "
     "règle « vérification par le même contre-lecteur » : le contre-lecteur d'origine est resté sur un autre compte et "
     "n'est pas joignable ; un agent neuf du même modèle (Claude Opus 5.5) vérifiera à partir de la table, du rapport et "
     "de la différence entre les deux brouillons. L'entrée de contre-lecture au format du validateur (deux empreintes "
     "entières, table de traitement) reste à écrire par la session mère : `<<CONTRE_LECTURE_1>>`."),
    ("HT9", "calendrier : la vérification n'est plus faite par le même contre-lecteur (écart déclaré)",
     "corrections ; vérification des corrections par le même contre-lecteur ; nœuds portés à Lazar",
     "corrections (brouillon 2) ; vérification des corrections par un agent neuf du même modèle, le contre-lecteur "
     "d'origine n'étant pas joignable (écart déclaré, section « Contre-lecture ») ; nœuds portés à Lazar"),
    # ---- changements qu'une correction rend nécessaires ; écrits par le rédacteur ; à trancher par le vérificateur
    ("HT10", "induit par B1.1, M5.1, M5.2 et B2.1 : les phrases reçoivent deux crochets neufs ([état scellé à d ; "
             "différence [bas ; haut]], marque de la grille D) dont rien ne disait la source ni la place, alors que le code "
             "n'a pas le droit d'ouvrir `lecture-bbis.json` et que deux programmes doivent rendre des phrases identiques (E5)",
     "une phrase « première lecture seule » n'est plus éligible pour une dose relue, une phrase « deux lectures » ne l'est que pour une dose relue.",
     "une phrase « première lecture seule » n'est plus éligible pour une dose relue, une phrase « deux lectures » ne l'est que pour une dose relue.\n\n"
     "**Deux crochets, leur source et leur place.** Le crochet « [état scellé à d ; différence [bas ; haut]] » est rempli "
     "par des constantes écrites dans le code, recopiées de la ligne « texte égal moins adaptateur seul (99 %) » de la "
     "table « Aires déjà lues » de ce texte ; `lecture-bbis.json` n'est pas ouvert : dose 0,25, non établie, +0,0184 "
     "[−0,0189 ; +0,0541] ; dose 0,5, non établie, −0,0290 [−0,0726 ; +0,0090] ; dose 0,75, non établie, +0,0025 "
     "[−0,0029 ; +0,0082] ; dose 1, contraire, −0,0102 [−0,0209 ; −0,0019]. La marque que la grille D donne à une issue "
     "(« non relue ([motif]) », « relecture [non jouée | accordée après la première lecture | réduite après la première "
     "lecture] ») est écrite à la fin de la phrase « première lecture seule » de cette issue, entre crochets."),
    ("HT11", "induit par M2.2 et M3.1 réunies : une fois les paires à coût égal retirées, P_t peut être nul dans une tâche "
             "à deux actions utiles ou plus, et d_kt divise par P_t",
     "La part des paires à coût égal est écrite par groupe, par dose et par pli.",
     "La part des paires à coût égal est écrite par groupe, par dose et par pli. Une tâche dont P_t est nul dans un groupe "
     "(tous ses coûts déclarés égaux) est traitée dans ce groupe comme une tâche à moins de deux actions utiles : exclue, "
     "comptée, y compris pour le test par changement de signe de la tendance."),
    ("HT12", "précision de M4.1, que le rédacteur juge fausse sur un point si elle est lue pour les deux paires de mondes : "
             "sous le changement de signe des scores, la condition de plancher de la tendance n'a pas de miroir exact",
     "Les taux de M+, M−, MA et MA− restent écrits tels quels.",
     "Les taux de M+, M−, MA et MA− restent écrits tels quels. L'état miroir de la tendance n'est exigé qu'entre MA et "
     "MA− : sous le seul changement de signe des scores (M+ et M−), sa condition de plancher n'a pas de miroir exact (le "
     "quantile 0,95 des tau des directions y devient l'opposé de leur quantile 0,05, et le groupe dont le plancher est "
     "exigé n'est pas échangé) ; l'état miroir de l'interaction est exigé dans les deux paires."),
    ("HT13", "induit par M2.1 et m3.2 : la section « Fautes trouvées », point 1, disait encore que l'accord de la jumelle se "
             "juge sur son seul intervalle, ce que « Seuil » ne dit plus",
     "l'accord de la jumelle se juge sur le signe de son propre intervalle, sans plancher.",
     "l'accord de la jumelle se juge sur le signe de son propre intervalle et sur son test par changement de signe, sans "
     "plancher (section « Seuil »)."),
    ("HT14", "induit par M2.1 : la tendance a maintenant une valeur p ; la règle du niveau corrigé de famille ne disait le "
             "seuil de la valeur p que pour l'interaction (calcul sans choix, E5)",
     "pour l'interaction, valeur p du changement de signe sous 0,00625)",
     "pour l'interaction et pour la tendance, valeur p du changement de signe sous 0,00625)"),
    ("HT15", "induit par B2.1 et B2.3 : la section 0 disait encore, sans condition, que la seconde lecture fait foi pour "
             "tout ce qu'elle recalcule, ce que la grille D ne dit plus quand la relecture est accordée ou réduite après "
             "l'ouverture des scores",
     "La seconde lecture **fait foi** pour tout ce qu'elle recalcule.",
     "La seconde lecture **fait foi** pour tout ce qu'elle recalcule, dans les cas que fixe la grille D des critères de "
     "lecture, et sous ses marques."),
]


def appliquer(texte, edits, releve, genre):
    for ident, quoi, avant, apres in edits:
        n = texte.count(avant)
        assert n == 1, (ident, "occurrences du texte avant", n)
        texte = texte.replace(avant, apres)
        releve.append(dict(repere=ident, genre=genre, quoi=quoi, occurrences_avant=n))
    return texte


def corrections(fichier):
    sortie = []
    for r in REMARQUES:
        for k, (f, avant, apres) in enumerate(r["edits"], 1):
            if f == fichier:
                sortie.append(("%s.%d" % (r["id"], k), r["classe"], avant, apres))
    return sortie


releve = dict(sources=ATTENDU, corrections=[], hors_correction=[], presence_des_apres=[])

# Devis d'abord : son empreinte entre dans l'en-tête du texte.
devis = (RACINE / DEV1).read_text(encoding="utf-8")
devis = appliquer(devis, corrections(DEV1), releve["corrections"], "devis")
devis = appliquer(devis, HORS_DEVIS, releve["hors_correction"], "devis")
texte = (RACINE / PRE1).read_text(encoding="utf-8")
texte = appliquer(texte, corrections(PRE1), releve["corrections"], "texte")
texte = appliquer(texte, HORS_TEXTE, releve["hors_correction"], "texte")
empreinte_devis2 = hashlib.sha256(devis.encode("utf-8")).hexdigest()
assert texte.count(EMPREINTE_DEVIS2) == 1
texte = texte.replace(EMPREINTE_DEVIS2, empreinte_devis2)

# Chaque « apres » d'une correction doit se trouver, entier, dans le brouillon 2.
for fichier, contenu in ((DEV1, devis), (PRE1, texte)):
    for ident, classe, avant, apres in corrections(fichier):
        releve["presence_des_apres"].append(dict(repere=ident, classe=classe, apres_present=contenu.count(apres),
                                                 avant_encore_present=contenu.count(avant) if avant not in apres else None))
releve["compte"] = dict(corrections=len(releve["corrections"]), hors_correction=len(releve["hors_correction"]),
                        apres_tous_presents=all(x["apres_present"] >= 1 for x in releve["presence_des_apres"]),
                        avant_tous_partis=all(x["avant_encore_present"] in (0, None) for x in releve["presence_des_apres"]))
releve["sorties"] = {DEV2: empreinte_devis2, PRE2: hashlib.sha256(texte.encode("utf-8")).hexdigest()}

if not A_BLANC:
    for chemin, contenu in ((DEV2, devis), (PRE2, texte)):
        cible = RACINE / chemin
        assert not cible.exists(), ("existe déjà", chemin)
        cible.write_text(contenu, encoding="utf-8")
Path(sys.argv[2]).write_text(json.dumps(releve, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(dict(compte=releve["compte"], sorties=releve["sorties"], a_blanc=A_BLANC), ensure_ascii=False, indent=1))
