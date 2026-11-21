#!/usr/bin/env python3
"""faire_av2.py — compose l'avenant 2 à partir de son gabarit.

Confronte chaque citation à sa ligne dans la pièce citée, relève par programme les
lignes touchées par chiffre, insère la sortie du calcul. N'écrit que le fichier de
sortie donné en argument, et refuse de l'écraser.

usage : faire_av2.py ARBRE BLOC_NOTES HEURE COMMIT_MAIN SORTIE
"""
import hashlib
import os
import re
import sys

ARBRE, BLOC, HEURE, C_MAIN, SORTIE = sys.argv[1:6]
REL = os.path.join(ARBRE, "docs/notes/relance-organismes-discrets-v1")
CHEMINS = {
    "devis": os.path.join(REL, "devis-essais-admission-mistral-neon-bras-a-v1.md"),
    "av1": os.path.join(REL, "avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md"),
    "verif_av1": os.path.join(REL, "verification-avenant-1-v3-devis-essais-admission-v1.md"),
    "confront": os.path.join(REL, "confrontation-regle-google-livraison3-v1.md"),
    "note": os.path.join(REL, "note-programme-essais-admission-bras-a-v3.md"),
    "mandat": os.path.join(REL, "mandat-redacteur-fable-avenant-2-plafond-65536-v1.md"),
    "taux": os.path.join(REL, "taux-de-change-v1/bce-eurofxref-daily-releve-2026-11-21T1749Z.xml"),
    "calc": os.path.join(BLOC, "calc_av2.py"),
}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def lignes(cle):
    return open(CHEMINS[cle], encoding="utf-8").read().split("\n")


L = {k: lignes(k) for k in ("devis", "av1", "confront", "note")}
EXTRAITS = {
    "regle": open(os.path.join(BLOC, "regle_google.txt"), encoding="utf-8").read(),
    "go": open(os.path.join(BLOC, "go_lignes.txt"), encoding="utf-8").read(),
    "od": open(os.path.join(BLOC, "od_lignes.txt"), encoding="utf-8").read(),
}
N_CIT = 0


def verifie(cle, n, texte):
    global N_CIT
    ligne = L[cle][n - 1]
    assert texte in ligne, f"citation absente : {cle} ligne {n} : {texte!r}"
    N_CIT += 1


def cellule(texte):
    return "« " + texte.replace("|", "\\|") + " »"


def table(cle, rangs):
    out = []
    precedent = 0
    for n, section, citations, effet in rangs:
        assert n >= precedent, ("ordre des lignes", n)
        precedent = n
        for c in citations:
            verifie(cle, n, c)
        out.append(f"| {n} | {section} | " + " ; ".join(cellule(c) for c in citations) + f" | {effet} |")
    return "\n".join(out)


# ------------------------------------------------------------------ devis, 1.1
DEVIS_1 = [
    (17, "0, point 5", ["**Sortie maximale envoyée : 32 768 jetons aux deux** (décidé par Lazar)"], "Google : 65 536 ; Mistral : 32 768, inchangé"),
    (36, "1, mot « goreco », décision 2", ["**la sortie maximale envoyée aux deux files est de 32 768 jetons**, à revoir si les délais ne tiennent pas"], "remplacé pour Google seulement"),
    (101, "4.2, appel A", ["**Son corps porte exactement les réglages de la file** : même sortie maximale"], "lettre inchangée : les appels A et A′ de Google portent donc 65 536"),
    (130, "4.4, ligne 2", ["Google : `outputTokenLimit` rendu par l'appel de liste, sous 32 768"], "« sous 65 536 » : aucun appel payant, et la décision est à reprendre"),
    (162, "4.6", ["Sortie maximale : **256** (`max_tokens: 256` ; `maxOutputTokens: 256`)"], "inchangé : la sonde garde 256, sous l'exemption de la section 6"),
    (188, "4.6, limites", ["elle suppose que la borne se comporte de même à 32 768"], "« à 65 536 »"),
    (201, "5.1", ["niveau de réflexion le plus haut, `xhigh` | **32 768** | sans flux"], "65 536 ; le niveau le plus haut est gardé"),
    (211, "5.3", ["`generationConfig.maxOutputTokens: 32768`"], "`65536`"),
    (215, "5.4", ["**32 768 jetons aux deux : décidé par Lazar** (section 1)"], "de même que la ligne 17"),
    (221, "5.4, part 1", ["**Une sortie facturée au-dessus de 32 768 n'arrête plus la file**"], "chez Google : au-dessus de 65 536"),
    (263, "5.6", ["une réponse de 32 768 jetons tient dans 2 690 secondes si le service rend **12,2 jetons par seconde ou plus** (C)"], "Google : 65 536 jetons, 24,4 jetons par seconde (section 5)"),
    (337, "6.4", ["Google, file | 32 768 jetons, la sortie maximale envoyée | 0,507 ; 0,564"], "65 536 jetons ; 0,999 ; 1,056"),
    (338, "6.4", ["Google, vérification | 32 768 jetons | 0,492"], "65 536 jetons ; 0,984"),
    (343, "6.4, régime courant", ["chez Google, 32 768 jetons de sortie", "sous la supposition que la borne se comporte à 32 768 comme à 256"], "65 536, aux deux endroits"),
    (532, "10, garde 3", ["le corps porte la sortie maximale de sa ligne (32 768 ; 256 à la sonde)", "corps sans sortie maximale, à 65 536"], "à Google, 65 536 est la valeur saine et 32 768 un artefact ; chez Mistral, rien ne change"),
    (571, "11", ["**la sortie maximale de 32 768 ne tient dans les délais que si le service rend 12,2 jetons par seconde ou plus, débit non mesuré**"], "ligne 4 : 65 536 et 24,4 ; ligne 3 : inchangée"),
]

# ------------------------------------------------------------------ devis, 1.2
DEVIS_2 = [
    (13, "0, point 1", ["File Neon : 8 appels, 16 envois au plus, plafond **8,50 USD**."], "16,50 USD"),
    (14, "0, point 2", ["Google, plafond **1,50 USD**"], "3,00 USD, pour chacune des deux vérifications"),
    (24, "0, point 12", ["au plus 2,18 USD à la vérification, 7,58 USD à la file"], "1,69 et 7,09 USD"),
    (134, "4.4, ligne 6", ["cela passe le plafond de la ligne, chez Google (2,68 USD contre 1,50)"], "2,68 ne passe plus 3,00 ; la ligne s'arrête quand même : 3,66 avec la réserve de l'envoi suivant (2.4)"),
    (181, "4.6, texte porté à Lazar", ["le plafond de 8,50 USD est tenu par compteur si la sortie maximale borne la réflexion ; sinon, excès possible d'un seul envoi, au plus 7,58 USD au débit déclaré de 200 jetons par seconde (S), soit 16,08 USD au plus pour la file", "**un envoi coupé au délai de 45 minutes arrête la file, sans reprise, et elle ne tient pas**"], "16,50 ; 7,09 ; 23,59 ; la seconde phrase ne vaut plus telle quelle (2.4)"),
    (183, "4.6", ["est d'au moins 16,08 USD (plafond et excès de la file)"], "23,59 USD, par projet (section 3)"),
    (192, "4.6, limites", ["c'est l'excès de la ligne 2 (6.4), 2,18 USD au débit déclaré"], "1,69 USD"),
    (307, "6.3", ["0,507 ; 0,564 | 8,33 | 0,507 ; 0,564 | **8,50** | 7,58 | 12,50"], "0,999 ; 1,056 ; 16,20 ; 16,50 ; 7,09 ; 24,30"),
    (310, "6.3", ["0,492 | 1,48 | 0,492 | **1,50** | 2,18"], "0,984 ; 2,96 ; 3,00 ; 1,69"),
    (311, "6.3", ["14,26 | | **15,25** | 12,74"], "à six lignes : 26,57 ; 27,75 ; 13,45"),
    (345, "6.4", ["Un envoi qui dure moins de 164 secondes chez Google", "Un appel de vérification de Google coupé à 890 secondes est compté 2,68 USD, au-dessus du plafond de 1,50", "avec la réserve de l'envoi suivant, cela passe 8,50, et **la file s'arrête, sans reprise**"], "328 secondes ; 2,68, sous 3,00, l'envoi suivant refusé ; à 16,50, la reprise part (2.4)"),
    (346, "6.4", ["le régime prudent compterait 8,09 USD un envoi de Neon coupé au délai de 45 minutes, et la file s'arrêterait sans la reprise que la règle 1 lui donne"], "ne vaut plus pour un premier envoi coupé (2.4)"),
    (370, "6.4, cas 3", ["7,93 USD chez Neon (envoi de couverture)", "Chez Neon, 8,33 au plus, sous 8,50."], "15,44 ; 16,20 au plus, sous 16,50"),
    (380, "6.4", ["| 1,50 | **2,18** | 0,85 | 4,85 |"], "3,00 ; 1,69 ; 0,36 ; 4,36"),
    (381, "6.4", ["| 8,50 | **7,58** | 3,55 | 15,65 |"], "16,50 ; 7,09 ; 3,06 ; 15,16"),
    (383, "6.4", ["3,68 USD pour la ligne 2 ; 16,08 pour la ligne 4"], "4,69 ; 23,59"),
    (389, "6.4", ["soit 72,77 USD au débit déclaré, contre 4,56 comptés"], "72,77 inchangé ; 8,99 comptés ; borne de la file : 80,29"),
    (433, "6.5", ["crédit prépayé vu d'au moins **19,76 USD**"], "28,28 USD, par projet"),
    (434, "6.5", ["au moins **16,08 USD**, plafond et excès de la file"], "23,59 USD, par projet"),
    (450, "6.6", ["plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi 7,58 USD à 200 jetons par seconde"], "16,50 et 7,09 ; pour une vérification, 3,00 et 1,69"),
    (530, "10, garde 1", ["32 768 jetons chez Google", "le premier est compté au-dessus du plafond, le deuxième n'est pas envoyé, la ligne s'arrête", "file Neon partie sur un mot de Lazar, envoi coupé à son délai total : la reprise est refusée, file arrêtée à son plafond"], "65 536 ; le premier est compté sous le plafond (2,68), le deuxième n'est pas envoyé ; la reprise part, et un second envoi coupé à 45 minutes arrête la file"),
    (539, "10, garde 10", ["est d'au moins 16,08 USD"], "23,59 USD"),
    (558, "11", ["**1,50 USD** | 2,18 USD, si la sortie maximale ne borne pas la réflexion"], "3,00 USD ; 1,69 USD"),
    (560, "11", ["**8,50 USD** | 7,58 USD, si la sortie maximale ne borne pas la réflexion"], "16,50 USD ; 7,09 USD"),
    (563, "11", ["Total des plafonds : **15,25 USD**", "Plafonds et excès ensemble : 27,99 USD"], "à six lignes : 27,75 ; 41,20"),
    (565, "11", ["au plus 2,18 USD (ligne 2, délai de 900 secondes) ou 7,58 USD (ligne 4)"], "1,69 ou 7,09"),
    (571, "11", ["à la ligne 4, un envoi coupé au délai de 45 minutes arrête la file, sans reprise"], "ne vaut plus telle quelle (2.4)"),
    (624, "13, point 12", ["elle peut coûter jusqu'à 0,49 USD par appel chez Google"], "0,99 USD"),
    (640, "13, point 28", ["son prix serait une file Neon arrêtée sur un seul délai de 45 minutes, sans la reprise de la règle 1"], "ne vaut plus : à 16,50, la reprise part après un premier envoi coupé (2.4)"),
]

# ------------------------------------------------------------------ avenant 1, 1.3
AV1 = [
    (9, "en-tête", ["aucun plafond de ligne (0,25 ; 1,50 ; 4,75 ; 8,50 ; 0,25 USD), aucun excès d'un envoi", "les valeurs des seuils de crédit (19,76 et 16,08 USD)"], "les deux plafonds de Google, leurs excès et les deux seuils changent : 3,00 et 16,50 ; 1,69 et 7,09 ; 28,28 et 23,59"),
    (14, "0, point 1", ["**Pire cas chez Google : 84,06 USD, sans borne dure, accepté par Lazar** (GO-2026-11-21-68)", "76,70 USD, et deux vérifications de clé à 3,68 USD (C)", "Au régime prudent, ou si la supposition de la sonde tient : 23,44 USD."], "89,67 ; 80,29 et 4,69 ; 32,97"),
    (15, "0, point 2", ["un seul plafond de 8,50 USD", "(1,50 USD de plafond)"], "16,50 ; 3,00"),
    (17, "0, point 4", ["**Seuils de crédit** : 19,76 et 16,08 USD, inchangés", "**plus une recharge automatique, une seule**"], "28,28 et 23,59 ; la recharge n'est pas comptée (1.5)"),
    (129, "2.2", ["| 1,50 | 2,18 | **3,68** (D, ligne 383)"], "3,00 ; 1,69 ; 4,69"),
    (130, "2.2", ["| 8,50 | 7,58 | **16,08** (D, ligne 383)"], "16,50 ; 7,09 ; 23,59"),
    (131, "2.2", ["si la borne se comporte à 32 768 comme à 256"], "à 65 536"),
    (132, "2.2", ["**76,70** (C : 8,50 + 9 × 7,578 = 76,702)"], "80,29 (16,50 + 9 × 7,08696)"),
    (137, "2.2", ["soit **23,44 USD** et **84,06 USD**"], "32,97 et 89,67"),
    (143, "2.2", ["1,50 + 4,85 + 8,50 + 15,65 = **30,50 USD**", "8,50 + 9 × 15,65 = **149,35 USD**"], "39,02 et 152,92 (une seule vérification, à 400 jetons par seconde)"),
    (161, "2.4", ["**23,44 USD** au régime prudent, **84,06 USD** au cas des neuf excès (C)"], "32,97 et 89,67"),
    (162, "2.4", ["À 400 jetons par seconde : 36,85 USD au régime prudent, 162,05 USD au cas des neuf excès (C)."], "46,38 et 167,64"),
    (163, "2.4", ["il retirerait la reprise unique que la règle 1 donne"], "ne vaut plus pour un premier envoi coupé (2.4)"),
    (217, "4.1", ["(4,17 USD d'envois finis par clé, 8,34 pour les deux, sous 8,50 ; C)"], "8,10 par clé, 16,20 pour les deux, sous 16,50"),
    (220, "4.1", ["un plafond de 8,50 USD"], "16,50"),
    (229, "4.2", ["le plafond est celui de la file entière, 8,50 USD"], "16,50"),
    (255, "4.4", ["Les valeurs ne changent pas : **19,76 USD** avant une vérification de clé, **16,08 USD** avant la file (devis, 6.5)."], "elles changent : 28,28 et 23,59"),
    (261, "4.4, point 3", ["`crédit compté(P) − dépense retirée ≥ 19,76`", "la première a pu prendre jusqu'à 3,68 USD"], "28,28 ; 4,69"),
    (262, "4.4, point 4", ["`crédit compté(P) − dépense retirée ≥ 16,08`"], "23,59"),
    (264, "4.4, point 6", ["2 × 3,68 + 16,08 = 23,44 USD"], "2 × 4,69 + 23,59 = 32,97"),
    (265, "4.4, point 7", ["16,08 + 7,36 = **23,44 USD**"], "23,59 + 9,38 = 32,97"),
    (333, "6, ligne 2", ["plafond 1,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 2,18 USD", "avec une recharge automatique [valeur]"], "texte neuf en section 8"),
    (335, "6, ligne 6", ["plafond 1,50 USD, excès possible d'un seul envoi de 2,18 USD"], "texte neuf en section 8"),
    (337, "6, ligne 4", ["plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 7,58 USD", "où un envoi coupé à 45 minutes arrête la file sans reprise", "pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 84,06 USD, accepté"], "texte neuf en section 8"),
    (339, "6, sommes", ["plafonds, 15,25 + 1,50 = **16,75 USD**", "12,74 + 2,18 = **14,92 USD**", "ensemble, **31,67 USD**"], "27,75 ; 13,45 ; 41,20"),
    (343, "6, geste de paiement", ["les deux soldes vus (11,93 € et 15,59 €) et une recharge automatique par projet doivent couvrir 19,76 USD sur chaque projet"], "texte neuf en section 8"),
    (355, "7, point 7", ["Avant toute vérification de Google, les deux projets à 19,76 ; avant la file, les deux projets à 16,08", "la file part (19,76 − 3,68 = 16,08)", "la file ne part pas (19,76 − 3,70 = 16,06)"], "28,28 et 23,59 ; 28,28 − 4,69 = 23,59 ; 28,28 − 4,71 = 23,57"),
    (415, "9, point 4", ["**Pire cas de 84,06 USD sans borne dure**, accepté.", "à 400 jetons par seconde, 162,05 USD"], "89,67 ; 167,64"),
    (423, "9, point 12", ["toute ligne nouvelle de vérification y ajoute 3,68 USD"], "4,69 USD"),
]

# ------------------------------------------------------------------ citations dans le fil du texte
EN_LIGNE = [
    ("devis", 17, "Neon, niveau de réflexion le plus haut (`xhigh`)"),
    ("confront", 50, "(a) si l'interface admet le budget avec Neon"),
    ("confront", 50, "(b) seulement comme repli, en connaissance du doublement des plafonds"),
    ("av1", 259, "`t` est le taux en USD par euro de la pièce de constat, daté d'au plus 24 heures avant elle."),
    ("av1", 259, "le solde vu, plus le montant d'une recharge si la page affiche un montant"),
    ("av1", 327, "L'heure du taux est au plus 24 heures avant l'heure de la pièce qui le cite, jamais après."),
    ("note", 36, "borne écrite : l'heure du taux est au plus 24 heures avant l'heure de la pièce, au plus 6 heures après, jamais après l'envoi"),
    ("note", 57, "**exigé à `false` en définitive**"),
    ("note", 51, "19,76 dollars avant une vérification de Google, 16,08 avant la file, par projet"),
    ("note", 89, "la plus tardive des heures des valeurs vues"),
    ("av1", 8, "2026-11-21T16:24:17Z"),
    ("confront", 45, "d'environ 16,50 au lieu de 8,50"),
    ("confront", 45, "d'environ 3,00 au lieu de 1,50"),
    ("devis", 346, "la file s'arrêterait sans la reprise que la règle 1 lui donne"),
    ("note", 64, "borne de réflexion déclarée à la configuration"),
    ("confront", 43, "non vérifiable : il faut supposer une borne de la réflexion (≤ 49 536), qu'aucune pièce ne donne"),
    ("devis", 215, "à des efforts plus bas"),
    ("devis", 215, "de 49 à 1 239 jetons, réflexion comprise"),
    ("devis", 219, "**non établi pour les deux appels de ce devis.**"),
    ("note", 65, "`consignes.<nom>.limite_de_mots` × `fournisseurs.google.jetons_par_mot` ≤ plafond − réflexion"),
    ("devis", 101, "sa réponse est courte"),
    ("devis", 162, "Même réglage de raisonnement, même mode de lecture, même traitement de la température que l'appel sain."),
    ("devis", 95, "Le texte des réponses de code 200 n'est ni lu ni rapporté."),
    ("devis", 163, "par programme, sur la sortie facturée de 5.5, le motif de fin et la réflexion constatée"),
    ("confront", 77, "Il faut une **exemption nommée de la règle**, accordée par Lazar : c'est un écart à une règle permanente, donc un nœud."),
]
EXTRAITS_CITES = [
    ("regle", "le plafond de sortie n'atteint pas réflexion plus 16 000 jetons de texte"),
    ("regle", "la limite de mots de l'invite ne tient pas dans le plafond de texte"),
    ("go", "contact, publication, paiement restent à Lazar"),
    ("od", "passe sur les deux projets"),
]

# ------------------------------------------------------------------ lignes touchées, par chiffre


HISTOIRE = {"devis": {315, 321, 424}, "av1": set()}


def releve(cle, fin, chiffre, exclues=()):
    motif = re.compile(r"(?<![\d,])" + re.escape(chiffre) + r"(?![\d])")
    return [i for i, l in enumerate(L[cle][:fin], 1)
            if motif.search(l) and i not in exclues and i not in HISTOIRE[cle]]


def listes(cle, fin, plan):
    out = []
    for chiffre, neuf, quoi, exclues in plan:
        ls = releve(cle, fin, chiffre, exclues)
        assert ls, ("aucune ligne", cle, chiffre)
        out.append(f"- {quoi} : {chiffre} devient **{neuf}** — ligne" + ("s " if len(ls) > 1 else " ") + ", ".join(str(x) for x in ls) + ".")
    return "\n".join(out)


MISTRAL = {169, 192, 200, 321, 336, 350, 352, 353, 359, 368, 369, 424, 545, 548, 585}
PLAN_DEVIS = [
    ("32 768", "65 536", "sortie maximale envoyée à Google", MISTRAL),
    ("32768", "65536", "le même nombre, dans le corps de l'appel", {206}),
    ("8,50", "16,50", "plafond de la file du juge", ()),
    ("1,50", "3,00", "plafond d'une vérification de clé", ()),
    ("7,58", "7,09", "excès d'un envoi de la file", ()),
    ("2,18", "1,69", "excès d'un envoi de vérification", ()),
    ("16,08", "23,59", "plafond et excès de la file, seuil d'avant la file", ()),
    ("3,68", "4,69", "plafond et excès d'une vérification", ()),
    ("19,76", "28,28", "seuil d'avant une vérification", ()),
    ("0,507", "0,999", "réserve d'un envoi d'appariement", ()),
    ("0,564", "1,056", "réserve d'un envoi de couverture", ()),
    ("0,492", "0,984", "réserve d'un envoi de vérification", ()),
    ("8,33", "16,20", "pire cas des seize envois", ()),
    ("1,48", "2,96", "pire cas des trois envois d'une vérification", ()),
    ("12,2", "24,4", "débit qui tient la sortie pleine, pour Google", ()),
    ("7,93", "15,44", "seuil de refus du compteur", ()),
    ("12,50", "24,30", "trois envois par appel, pour information", ()),
    ("4,56", "8,99", "neuf envois coupés, comptés à leur réserve", ()),
    ("0,49", "0,99", "coût d'un appel de vérification à sortie pleine", ()),
    ("15,65", "15,16", "excès de la file à 400 jetons par seconde", ()),
    ("3,55", "3,06", "excès de la file à 100 jetons par seconde", ()),
    ("4,85", "4,36", "excès d'une vérification à 400 jetons par seconde", ()),
    ("0,85", "0,36", "excès d'une vérification à 100 jetons par seconde", ()),
    ("14,26", "26,57", "pire cas à la sortie maximale, tous envois, à six lignes", ()),
    ("15,25", "27,75", "somme des plafonds, à six lignes", ()),
    ("15,00", "27,50", "la même, sans la ligne 5", ()),
    ("12,74", "13,45", "somme des excès, à six lignes", ()),
    ("11,57", "12,28", "la même, sans la ligne 5", ()),
    ("27,99", "41,20", "plafonds et excès ensemble, à six lignes", ()),
    ("26,57", "39,78", "les mêmes, sans la ligne 5", ()),
]
PLAN_AV1 = [
    ("32 768", "65 536", "sortie maximale envoyée à Google", ()),
    ("8,50", "16,50", "plafond de la file du juge", ()),
    ("1,50", "3,00", "plafond d'une vérification de clé", ()),
    ("7,58", "7,09", "excès d'un envoi de la file", ()),
    ("7,578", "7,08696", "le même, à trois décimales", ()),
    ("2,18", "1,69", "excès d'un envoi de vérification", ()),
    ("16,08", "23,59", "plafond et excès de la file, seuil d'avant la file", ()),
    ("3,68", "4,69", "plafond et excès d'une vérification", ()),
    ("7,36", "9,38", "deux vérifications au pire", ()),
    ("19,76", "28,28", "seuil d'avant une vérification", ()),
    ("23,44", "32,97", "Google, deux vérifications, régime prudent ; crédit à avoir au pire", ()),
    ("76,70", "80,29", "file, neuf excès", ()),
    ("80,38", "84,98", "Google, une vérification, neuf excès", ()),
    ("84,06", "89,67", "Google, deux vérifications, pire cas", ()),
    ("30,50", "39,02", "à 400 jetons par seconde, une vérification, régime prudent", ()),
    ("149,35", "152,92", "à 400 jetons par seconde, une vérification, neuf excès", ()),
    ("36,85", "46,38", "à 400 jetons par seconde, deux vérifications, régime prudent", ()),
    ("162,05", "167,64", "à 400 jetons par seconde, deux vérifications, neuf excès", ()),
    ("4,17", "8,10", "envois finis d'une clé, sortie pleine", ()),
    ("8,34", "16,20", "envois finis des deux clés", ()),
    ("27,99", "36,51", "avec Mistral, une seule vérification de Google", ()),
    ("16,75", "27,75", "somme des six plafonds", ()),
    ("14,92", "13,45", "somme des excès", ()),
    ("31,67", "41,20", "plafonds et excès ensemble", ()),
]

# contrôle des exclusions : chaque ligne écartée porte bien « Mistral » ou une phrase d'histoire
for n in sorted(MISTRAL):
    l = L["devis"][n - 1]
    assert "32 768" in l, n
    assert ("Mistral" in l) or ("octets" in l) or ("brouillon" in l) or ("262 144" in l), (n, l[:120])
assert "max_tokens: 32768" in L["devis"][205]

t1, t2, t3 = table("devis", DEVIS_1), table("devis", DEVIS_2), table("av1", AV1)
for cle, n, texte in EN_LIGNE:
    verifie(cle, n, texte)
for cle, texte in EXTRAITS_CITES:
    assert texte in EXTRAITS[cle], (cle, texte)
    N_CIT += 1

gabarit = open(os.path.join(BLOC, "av2_gabarit.md"), encoding="utf-8").read()
sortie_calc = open(os.path.join(BLOC, "calc_av2.sortie.txt"), encoding="utf-8").read().strip("\n")
rempl = {
    "@@H_DEVIS@@": sha(CHEMINS["devis"]),
    "@@H_AV1@@": sha(CHEMINS["av1"]),
    "@@H_VERIF_AV1@@": sha(CHEMINS["verif_av1"]),
    "@@H_CONFRONT@@": sha(CHEMINS["confront"]),
    "@@H_NOTE@@": sha(CHEMINS["note"]),
    "@@H_MANDAT@@": sha(CHEMINS["mandat"]),
    "@@H_TAUX@@": sha(CHEMINS["taux"]),
    "@@H_CALC@@": sha(CHEMINS["calc"]),
    "@@HEURE@@": HEURE,
    "@@C_MAIN@@": C_MAIN,
    "@@TABLE_DEVIS_1@@": t1,
    "@@TABLE_DEVIS_2@@": t2,
    "@@TABLE_AV1@@": t3,
    "@@LISTES_DEVIS@@": listes("devis", 685, PLAN_DEVIS),
    "@@LISTES_AV1@@": listes("av1", 423, PLAN_AV1),
    "@@SORTIE_CALC@@": sortie_calc,
    "@@N_CIT@@": str(N_CIT),
}
doc = gabarit
for k, v in rempl.items():
    assert k in doc, k
    doc = doc.replace(k, v)
assert "@@" not in doc, "marque non remplie"

# chaque citation du fil du texte figure bien dans la pièce composée
for cle, n, texte in EN_LIGNE:
    assert texte in doc, ("citation en ligne absente de la pièce", cle, n, texte)
for cle, texte in EXTRAITS_CITES:
    assert texte in doc, ("extrait absent de la pièce", cle, texte)

assert not os.path.exists(SORTIE), "refus d'écraser : " + SORTIE
with open(SORTIE, "w", encoding="utf-8") as f:
    f.write(doc)
print(f"écrit : {SORTIE}")
print(f"citations confrontées : {N_CIT}")
print(f"lignes : {doc.count(chr(10))}")
