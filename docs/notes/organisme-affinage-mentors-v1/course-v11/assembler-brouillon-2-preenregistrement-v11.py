#!/usr/bin/env python3
"""Assemble le brouillon 2 de la v11 à partir du brouillon 1 (lui-même assemblé à partir du texte scellé de la v10 par
`assembler-brouillon-1-preenregistrement-v11.py`).

Toute ligne du brouillon 1 qui n'est pas nommée ici est recopiée à l'octet près. Chaque remplacement de sous-chaîne exige
que l'ancienne chaîne figure exactement une fois dans la ligne visée ; chaque remplacement de ligne exige son début ; sinon
le programme s'arrête (aucun repli silencieux).
Usage : python3 -I assembler-brouillon-2-preenregistrement-v11.py BROUILLON-1.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B1_SHA = "cde6b2d34ddaed05fb5bcd7308896dd0c955bf3d6c15d3db2c5dc99e9f0903f8"
DEVIS_V11_SHA = "34271cb3cb3dba89c897cc076f7a65cbf73630d96f7106f2f40adac9a2590d52"
CALCUL_SHA = "deac25b6fe59332b646cd7b67580126221f3aa5f547623a6270c58b2330428ee"
LANCEUR_V10_SHA = "b08290254982744ba7985232ea54a354bfb31ef7f92ada682d32e349d3294577"
COMMIT_MAIN = "9a5f45db503b52b644185f4045b62c810989027c"
GO_SHA = "ee1c9cec090b150c55cd26aa27c8b23303f5443a1caa5501c2ebfd43b7f0c17e"
DECISIONS_SHA = "996cd20acc7ceb37d7279d2d093cec4b16c1a0a45af924ac13879a18289a855b"
PAGE_PRIX = "docs/sources/prix/page-prix-gemini-api-20261122T104129Z.html"
PAGE_PRIX_SHA = "d3aa716e33e77c7df9da385258dac241f7a608926669f190f42293961201c017"
CLAUDE_MD_SHA = "605db83acc28c7fcc6d8d12de8edb41bcdb6ea7b37b717967d6fde29f5301960"
ANNEXE = "course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B1_SHA, "la source n'est pas le brouillon 1"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 311, len(L)   # 310 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
touchees, supprimees = set(), set()
apres = {}   # n -> lignes neuves insérées après la ligne n du brouillon 1


def debut(n, prefixe):
    assert lignes[n].startswith(prefixe), (n, lignes[n][:80])


def remplacer_ligne(n, prefixe, texte):
    debut(n, prefixe)
    lignes[n] = texte
    touchees.add(n)


def sub(n, ancien, nouveau):
    assert lignes[n].count(ancien) == 1, (n, ancien[:70], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


def remplacer_depuis(n, marqueur, nouveau):
    """Remplace la fin de la ligne n, du marqueur (présent une seule fois) jusqu'au bout."""
    assert lignes[n].count(marqueur) == 1, (n, marqueur[:70], lignes[n].count(marqueur))
    lignes[n] = lignes[n][:lignes[n].index(marqueur)] + nouveau
    touchees.add(n)


def ajouter_fin(n, prefixe, texte):
    debut(n, prefixe)
    lignes[n] = lignes[n] + texte
    touchees.add(n)


def supprimer(n, prefixe):
    debut(n, prefixe)
    supprimees.add(n)


def inserer_apres(n, *textes):
    apres.setdefault(n, []).extend(textes)


# ------------------------------------------------------------------------------------------------ en-tête
remplacer_ligne(3, "- **État de ce fichier : brouillon 1", (
    "- **État de ce fichier : brouillon 2 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 1 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-1.md`, `" + B1_SHA + "`, qui reste en place, "
    "R12) après les décisions de la mère sur cette version (R-4995, R-5006, R-5007, R-5018) et les mots de Lazar inscrits en "
    "GO-2026-11-22-124. Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et « RÉGLAGE À INSCRIRE », et une "
    "dernière section de points à trancher : les pièces qu'ils nomment (lanceur, essais, gabarits, configuration, "
    "commandes et relais de Carbon et d'Argon, sonde d'Astra) sont en écriture ou en contre-lecture ailleurs. Le "
    "préenregistrement v11 n'existera, sous le nom `course-v11/preenregistrement-course-affinage-mentors-v11.md`, qu'une "
    "fois ces emplacements remplis de valeurs réelles, cette ligne et la dernière section retirées, le fichier scellé puis "
    "contre-lu (R1, R2, R12). Le compagnon `.sha256` de ce brouillon ne sert qu'à son transport (R6) ; aucun lanceur ne "
    "doit l'épingler."))

ajouter_fin(4, "- Auteur de la v11", (
    " Pour les réglages de la garde et pour les prix, il a lu deux notes de contrôle du collisionneur sur `main` (réglages "
    "et comptes de jetons seulement, aucun contenu de réponse) et la page de prix du fournisseur versée au dépôt ; elles "
    "sont citées par le devis v11."))

sub(5, "- Date (UTC) de ce brouillon : 2026-11-22T18:54:51Z (`date -u +%FT%TZ`) ; v10 :",
    "- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 1 : 2026-11-22T18:54:51Z ; v10 :")

sub(6, "- **Numéro et base (écart au mandat, déclaré).**",
    "- **Numéro et base (écart au mandat, déclaré, tranché par la mère).**")
sub(6, "Le périmètre de la ligne de GO ne change pas ; la mère note la correspondance des numéros au registre : "
       "RÉFÉRENCE À INSCRIRE.",
    "Le périmètre de la ligne de GO ne change pas : la mère l'a inscrit au registre des décisions de `main` (R-4995 : "
    "« v8 » de GO-2026-11-22-107 se lit « v11 », périmètre et plafond inchangés).")

remplacer_ligne(7, "- **Ce que la v11 change, et rien d'autre**", (
    "- **Ce que la v11 change, et rien d'autre** (les trois changements du mandat, et trois décisions de la mère qui en "
    "découlent) : (1) **clé Claude** — `RR_ANTHROPIC_API_KEY_LUC` au lieu de `RR_ANTHROPIC_API_KEY_MINUIT`, avec la règle "
    "de départ et la garde de dépense propres à cette clé (plafond propre de la part Claude, 45 USD ; arrêt de la course "
    "au premier refus) ; (2) **Astra** — `gpt-6.2-astra` au lieu de `gpt-6-astra`, clé déclarée `OPENAI_API_KEY_2`, prix "
    "relevés ; (3) **Carbon** — appel en flux sous la garde gelée des appels aux modèles de Google, au lieu de la commande "
    "par lot ; (4) **Argon** — sous la même garde gelée, qui vaut pour tout envoi à un modèle de Google (décision de la "
    "mère, R-5007, point (c)) ; (5) **plafond de session des juges** — 1,00 USD au lieu de 0,60, conséquence de (4), "
    "chiffrée par le devis v11 (R-5007, point (c) ; R-5018) ; (6) **prix comptés pour Argon et pour Carbon** — 4 et 20 USD "
    "par million de jetons, prix le plus haut de la page de prix du fournisseur versée au dépôt, au lieu des bornes 8,3 et "
    "41,5 (décision de la mère, R-5018). S'y ajoutent leurs seules conséquences mécaniques : noms et chemins `v11`, "
    "configuration fixe v11, relevés et gabarits v11, devis v11, contre-lecteur. Hypothèse (aucune), prédiction (aucune), "
    "seuil (aucun), critères de lecture gelés, matière servie et retirée, plan, plan d'analyse, plafond d'arrêt (150 USD), "
    "budget et plafonds des étapes, plafonds de session des proposeurs (3,00 USD) et de l'aiguilleur (0,25 USD), "
    "composition déclarée (deux Claude, Argon, Astra, Carbon ; pas de Kimi), orchestrateur épinglé : **inchangés**."))

remplacer_depuis(8, "**v11** : exception déclarée à la règle « Claude par l'abonnement »", (
    "**v11** : exception déclarée à la règle « Claude par l'abonnement » (GO-2026-11-22-70) pour les appels Claude de "
    "cette course, faits par l'interface de programmation sur la clé `RR_ANTHROPIC_API_KEY_LUC` (GO-2026-11-22-107, "
    "échéance 2026-11-25 ; mot direct de Lazar, GO-2026-11-22-110 ; recharge automatique de la clé, GO-2026-11-22-111 ; "
    "**GO-2026-11-22-124** : plancher de couverture levé, lecture du solde non exigée, plafond de la part Claude de 45 USD "
    "et plafond de la course inchangés, exception portée au 2026-12-15 sous la réserve d'une confirmation de Lazar) ; "
    "décisions de la mère sur cette version (registre des décisions de `main` : R-4995, numéro et base ; R-5006 et R-5007, "
    "plafond propre de la part Claude, Argon sous la garde gelée, plafond de session des juges, devis v11 ; R-5018, prix "
    "déclarés d'Argon et de Carbon et plafond de session des juges à 1,00 USD) ; clé "
    "« Minuit » sans crédit (R-4833) ; prolongation de GO-2026-11-18-14 au 2026-12-15 (GO-2026-11-22-80) ; « Astra » "
    "désigne `gpt-6.2-astra` (règle de Lazar, R-4900 ; prix relevés, R-4905) ; garde gelée des appels aux modèles de "
    "Google (GO-2026-11-21-71) et plafond de sortie de Carbon (GO-2026-11-21-47), règles permanentes de `CLAUDE.md` sur "
    "`main` ; « une panne technique n'est pas un résultat » (GO-2026-11-22-77). Lignes lues sur `main` au commit `"
    + COMMIT_MAIN + "` : `registres/go.md` (`" + GO_SHA + "`), `registres/decisions.md` (`" + DECISIONS_SHA
    + "`), `CLAUDE.md` (`" + CLAUDE_MD_SHA + "`)."))

# ------------------------------------------------------------------------------------------------ pièces
sub(12, "le plafond du relais Claude (150 USD remplacé par le plafond de la part Claude, § Règle des clés), le bloc "
        "descriptif de Carbon",
    "le plafond du relais Claude (**45 USD**, plafond de la part Claude, au lieu de 150 ; § Règle des clés), le **plafond "
    "de session des juges (1,00 USD au lieu de 0,60** ; § Espèces, « Argon », et devis v11, § 2), le bloc descriptif de "
    "Carbon")
sub(12, "budget, plafonds de relais des étapes, plafonds de session (proposeur 3,00 ; aiguilleur 0,25 ; juge 0,60 USD), "
        "espèces,",
    "budget, plafonds de relais des étapes, plafonds de session des proposeurs (3,00 USD) et de l'aiguilleur (0,25 USD), "
    "espèces,")

sub(14, "**Argon** — `commande_argon_v3d.py` `46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46` sous "
        "l'enveloppe `appel-argon-v5.sh` `37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a`, relais Gemini "
        "v2 `relais_gemini_v2.py` `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` (inchangés depuis la "
        "v6, sous la réserve du point « Argon » du § Espèces) ;",
    "**Argon, v11** — commande d'Argon sous la garde gelée : EMPREINTE À INSCRIRE : <chemin de la commande d'Argon sous "
    "la garde> ; son enveloppe, s'il en reste une : EMPREINTE À INSCRIRE : <chemin de l'enveloppe d'Argon> ; relais Gemini "
    "v2 `relais_gemini_v2.py` `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` (inchangé depuis la v6 ; "
    "EMPREINTE À INSCRIRE : <chemin du relais d'Argon> seulement si la commande sous la garde en demande un autre) ; "
    "**retrait** : la commande `commande_argon_v3d.py` (`46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46`) "
    "sous l'enveloppe `appel-argon-v5.sh` (`37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a`), épinglée "
    "de la v6 à la v10, ne tient pas la garde (§ Espèces) et n'est plus employée ;")

debut(15, "  - garde commune des appels aux modèles de Google (**v11**)")
inserer_apres(15, (
    "  - page de prix du fournisseur pour Argon et Carbon (**v11**) : `" + PAGE_PRIX + "` sur `main`, `" + PAGE_PRIX_SHA
    + "`, l. 153-163 (`gemini-4-carbon`) et l. 372-382 (`gemini-4-argon`) : entrée 2,00 USD par million de jetons jusqu'au "
    "30 novembre 2026 et 4,00 à partir du 1er décembre ; sortie, jetons de réflexion compris, 10,00 puis 20,00 ; le prix "
    "le plus haut, **4 et 20**, est le prix déclaré des deux espèces (décision de la mère, R-5018) ; copie versée, non "
    "une lecture de la console de facturation ;"))

sub(21, "  - **devis v10** :",
    "  - devis v10 (remplacé par le v11, qui en reprend les hypothèses de Carbon, les seuils des étapes et la part Claude "
    "estimée) :")
lignes[21] = (
    "  - **devis v11** : `docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v11.md`, `"
    + DEVIS_V11_SHA + "`, écrit pour cette version sur les décisions de la mère (R-5007, point (d) ; R-5018), à "
    "contre-lire ; ses chiffres sont recalculés par `docs/notes/organisme-affinage-mentors-v1/course-v11/calcul-devis-"
    "course-affinage-mentors-v11.py`, `" + CALCUL_SHA + "` — Argon et Carbon comptés à 4 et 20 USD par million de jetons ; "
    "Carbon au prix plein (0,4805 USD par appel estimé) ; plafond de session des juges 1,00 USD au lieu de 0,60 (§ 2) ; "
    "cinq espèces, **sans la réflexion d'Argon**, non mesurée : 35,68 USD sans marge, 39,25 avec ; 3,52 USD de plus par "
    "millier de jetons de réflexion moyenne par appel d'Argon, 93,36 USD si Argon réfléchit à sa provision entière à "
    "chaque appel ; l'étape des juges n'est coupée par le plafond d'arrêt qu'au-delà d'environ 32 500 jetons de moyenne "
    "(§ 4) ; aucun « haut » ; pire cas 150 ; parts au pire par clé : clé LUC 45 (plafond de la part Claude), clé de Google "
    "198, clé d'OpenAI 48 ; § 8 : comparaison aux bornes des v6 à v10 ;\n" + lignes[21])
supprimer(25, "  - **devis, v11** : aucun devis neuf")

sub(26, "  - lanceur : `scripts/lancer_course_affinage_mentors_v11.py` (il épingle",
    "  - lanceur : `scripts/lancer_course_affinage_mentors_v11.py`, écrit à partir du lanceur v10 "
    "(`scripts/lancer_course_affinage_mentors_v10.py`, `" + LANCEUR_V10_SHA + "`, branche de la v10) par un développeur "
    "qui n'est pas le rédacteur de ce texte (il épingle")

# ------------------------------------------------------------------------------------------------ espèces
sub(56, "Argon (obligatoire aussi, car il tient le second juge)",
    "Argon (obligatoire aussi, car il tient le second juge ; **v11** : sous la garde gelée des appels aux modèles de "
    "Google, détail plus bas)")

sub(58, "(a) le pire cas d'un appel, au prix plein (8,3 et 41,5 USD par million de jetons, bornes hautes de R-3271 ; plus "
        "de facteur de lot), tient sous le plafond de session d'un proposeur (3,00 USD) — au plafond de sortie le plus "
        "haut que la garde admet et sur l'entrée gardée la plus longue de la course (2 618 jetons, devis v10, § 1), il "
        "vaut (2 618 × 8,3 + 65 536 × 41,5) / 10⁶ = 2,7415 USD, dans la lecture où la réflexion compte dans le plafond de "
        "sortie (documentation du fournisseur, retenue depuis la v9) ;",
    "(a) le pire cas d'un appel, **tel que la commande épinglée le compte**, aux prix déclarés (4 et 20 USD par million "
    "de jetons, réflexion comprise dans la sortie : prix le plus haut de la page de prix versée, R-5018 ; 8,3 et 41,5, "
    "bornes hautes de R-3271, de la v5 à la v10 ; plus de facteur de lot), tient sous le plafond de session d'un proposeur "
    "(3,00 USD) sur l'entrée gardée la plus longue de la course (2 618 jetons, devis v10, § 1) : au plafond de sortie le "
    "plus haut que la garde admet, il vaut (2 618 × 4 + 65 536 × 20) / 10⁶ = 1,3212 USD si la commande compte la réflexion "
    "dans le plafond de sortie (lecture de la documentation du fournisseur et de la garde commune), et 2,3042 USD si elle "
    "y ajoute la provision de réflexion de Carbon sous la même garde dans le collisionneur (49 152 jetons ; convention de "
    "la commande par lot des v8 à v10, qui tient dans les deux lectures) : devis v11, § 2 ;")
sub(58, "**Risque dit** : la réflexion de Carbon en flux sur les consignes de l'affinage n'est pas mesurée ;",
    "**Risque dit** : la réflexion de Carbon en flux sur les consignes de l'affinage n'est pas mesurée (sur d'autres "
    "consignes, 21 réponses réelles de Carbon en flux portaient 19 727 à 44 101 jetons de pensées, devis v11, § 3) ;")

remplacer_ligne(59, "- **Argon et la garde gelée (v11, point à trancher avant le scellement).**", (
    "- **Argon sous la garde gelée (v11 ; décision de la mère, R-5007, point (c)).** La garde gelée vaut pour tout envoi "
    "à un modèle de Google, donc aussi pour Argon, proposeur et second juge de cette course. La commande d'Argon épinglée "
    "de la v6 à la v10 (`commande_argon_v3d.py`, sous l'enveloppe `appel-argon-v5.sh`) ne la tient pas : elle pose un "
    "budget de réflexion (8 192 jetons par défaut) sans demander les pensées en retour, abaisse le plafond de sortie à ce "
    "que le plafond de session paie sans plancher de 16 000 jetons de texte, et ne lit pas une réponse sans jeton de "
    "pensée comme un défaut ; sous un tel budget, Argon n'a rendu aucun jeton de pensée sur 22 réponses relevées ailleurs "
    "(devis v11, § 2). **Elle est retirée.** En v11, chaque appel d'Argon, de proposeur comme de juge, passe par une "
    "commande épinglée par le lanceur (empreinte aux pièces), qui emploie ou reproduit la garde commune "
    "(`garde_google_v3.py`), essais et mutations à l'appui. **Avant l'envoi**, une vérification par programme refuse "
    "l'appel, et rien ne part, si : le niveau de réflexion n'est pas explicite dans le corps, n'est pas le plus haut admis "
    "pour Argon (`high` dans la table de la garde) ou s'accompagne d'un budget ; les pensées ne sont pas demandées en "
    "retour ; le plafond de sortie n'atteint pas la provision de réflexion plus 16 000 jetons de texte, ou dépasse la "
    "limite de sortie d'Argon dans le mode de l'appel (32 768 jetons hors flux, 65 536 en flux, table de la garde) ; une "
    "limite de mots demandée par la consigne ne tient pas dans le plafond de texte. **Après la réponse** : zéro jeton de "
    "pensée, fin en `MAX_TOKENS`, `SAFETY`, `RECITATION` ou autre refus du fournisseur, fin autre que `STOP`, ou texte "
    "vide = **défaut journalisé, jamais une réponse** ; la commande rend alors un échec à l'orchestrateur, aucun texte "
    "n'est servi comme carte ni compté comme verdict, et l'échec compte pour A3 et A14. Aucun repli silencieux (R5) : le "
    "seul repli que la garde connaît (un renvoi unique au budget de réflexion prévu quand le fournisseur refuse le niveau) "
    "est écrit au journal s'il est fait. **Réglages retenus pour chiffrer** (ceux d'Argon sous la même garde dans le "
    "collisionneur ; devis v11, § 2) : niveau `high`, provision de réflexion 16 384 jetons, plafond de sortie 32 768 "
    "jetons, soit 16 384 jetons de texte, appel hors flux ; réglages exacts : RÉGLAGE À INSCRIRE, ceux du gabarit de "
    "déclaration v11, que le lanceur refuse de voir changés et écrit au manifeste de départ. **Plafond de session des "
    "juges : 1,00 USD au lieu de 0,60** (configuration v11 ; R-5018). Raison : aux réglages ci-dessus et sur une entrée "
    "de juge de 3 855 jetons (consigne du juge, une carte de 9 000 caractères au plus, cadre ; devis v11, § 2), le pire "
    "cas d'un appel de juge d'Argon, aux prix déclarés (4 et 20 USD par million de jetons), vaut 0,9985 USD quand la "
    "provision s'ajoute au plafond de sortie (convention de la commande retirée, qui tient dans les deux lectures) et "
    "0,6708 USD quand la réflexion y est comptée : les deux dépassent 0,60 USD, et 1,00 USD est la plus petite valeur au "
    "dixième qui tient dans les deux cas. **Marge étroite dans le premier cas** : 1,00 USD laisse alors passer une entrée "
    "de juge de 4 240 jetons au plus, 385 de plus que l'entrée attendue, dont le cadre est supposé ; au-delà, la commande "
    "refuse l'appel avant l'envoi (échec du juge, compté pour A3 et A14) ; le lanceur contrôle ce pire cas avant le "
    "départ, sur la plus longue entrée de juge admise (liste d'arrêt). Le plafond de session est fixé par rôle : le "
    "relèvement vaut aussi pour le juge Claude, estimé à 0,037 USD par appel, très en dessous des deux valeurs. Le plafond "
    "de session des proposeurs (3,00 USD, inchangé) couvre le pire cas d'un appel de proposeur d'Argon aux mêmes réglages "
    "(0,9935 USD). Rien d'autre ne change aux juges : consigne, items, aveuglement, agrégation, nombre d'appels. **Risque "
    "dit** : la réflexion d'Argon au niveau `high` sur ces consignes n'est mesurée dans aucune pièce lue ; elle est "
    "comptée au prix de sortie à chacun de ses 176 appels (16 de proposeur, 160 de juge), et son effet sur la dépense est "
    "au § Plafond ; un appel dont la réflexion et le texte dépassent ensemble le plafond de sortie finit en `MAX_TOKENS` "
    "(défaut), et, Argon tenant le second juge, A3 peut alors arrêter ce juge et A14 marquer l'étape des juges « non "
    "mesurée (technique) »."))

# ------------------------------------------------------------------------------------------------ mesures, bonne fin
sub(79, "**v11** : Carbon au prix plein, 0,9970 USD par appel — cinq espèces : 49,112 USD sans marge, § Plafond), reste "
        "estimé de chaque clé.",
    "**v11** : devis v11, Argon et Carbon aux prix déclarés (4 et 20 USD par million de jetons), Carbon au prix plein, "
    "0,4805 USD par appel, réflexion d'Argon non comptée — cinq espèces : 35,683 USD sans marge ; l'écart mesuré dit donc "
    "aussi la réflexion d'Argon, § Plafond), reste estimé de chaque clé "
    "(**v11** : sauf la clé LUC, dont le solde n'est pas lu, § Règle des clés).")

sub(84, "**v11** : un arrêt par la garde de la part Claude (plafond de la part Claude atteint, code 5 du lanceur ; § Règle "
        "des clés) est possible aussi : il interdit la bonne fin et se rapporte tel quel, sans relance.",
    "**v11** : un arrêt par la garde de la part Claude (premier refus du relais Claude à son plafond de 45 USD, ou premier "
    "refus de l'interface d'Anthropic relayé par lui ; code 5 du lanceur ; § Règle des clés) est possible aussi : il "
    "interdit la bonne fin et se rapporte tel quel, sans relance.")

# ------------------------------------------------------------------------------------------------ liste d'arrêt
sub(88, "**v11** : ligne de l'exception GO-2026-11-22-107 (appels Claude par l'interface de programmation sur la clé LUC) "
        "absente, hors période ou révoquée ;",
    "**v11** : ligne de l'exception GO-2026-11-22-107 (appels Claude par l'interface de programmation sur la clé LUC) ou "
    "ligne GO-2026-11-22-124 (qui la précise) absente ou révoquée ; date du jour hors de la période de ces lignes, "
    "prolongations comprises (§ Règle des clés, « Période ») ; après le 2026-11-25, ligne de prolongation absente, ou "
    "confirmation par Lazar de la prolongation de l'exception non inscrite au registre ou non nommée au lanceur ;")
sub(88, "pire cas d'un appel au-dessus du plafond de session (3,00 USD) ;",
    "pire cas d'un appel au-dessus du plafond de session (3,00 USD) ; **v11, commande d'Argon** : commande autre que la "
    "commande épinglée sous la garde, ou d'autres arguments que ceux du gabarit ; niveau de réflexion absent du corps, "
    "autre que le plus haut admis, ou accompagné d'un budget ; pensées non demandées en retour ; plafond de sortie sous la "
    "provision de réflexion plus 16 000 jetons de texte, ou au-delà de la limite d'Argon dans le mode de l'appel ; limite "
    "de mots de la consigne qui ne tient pas dans le plafond de texte (même garde gelée, contrôlée sur l'entrée de "
    "proposeur la plus longue et la plus courte de la course, et sur une entrée de juge) ; pire cas d'un appel de "
    "proposeur d'Argon au-dessus de 3,00 USD, ou d'un appel de juge d'Argon au-dessus de 1,00 USD sur la plus longue "
    "entrée de juge admise (consigne du juge, carte de 9 000 caractères, cadre réel) ; plafond de session des juges de la "
    "configuration autre que 1,00 USD ; **v11, prix d'Argon et de Carbon** : prix autres que 4 et 20 USD par million de "
    "jetons dans les arguments de leurs commandes (et dans l'état de leurs relais s'ils en portent) ;")
sub(88, "Claude, plafond égal, au centime, au plafond de la part Claude calculé du relevé des crédits (**v11** ; 150 en v7 "
        "à v10)",
    "Claude, plafond égal, au centime, au plafond de la part Claude, 45,00 USD, et journal du relais nommé à ses "
    "arguments et lisible par le lanceur (**v11** ; plafond de 150 en v7 à v10)")
sub(88, "solde illisible sans dispense R-3237 ou d'une clé non dispensable ; **v11, clé LUC** : lecture du solde par Lazar "
        "absente du relevé, d'un autre jour que le départ, sans heure lisible ou sans la ligne du registre de `main` qui "
        "la porte ; recharge automatique déclarée au-delà de 40 euros ; réserves absentes (une liste vide s'écrit) ou mal "
        "formées ; écrit de la mère sur les autres dépenses de la clé non cité ; plafond de la part Claude sous le "
        "plancher de 20,65 USD (code 3) ;",
    "solde illisible sans dispense R-3237 ou d'une clé non dispensable (**v11** : hors la clé LUC, ci-après) ; **v11, clé "
    "LUC** : entrée de la clé LUC absente du relevé des crédits, ou qui ne dit pas « solde non lu » avec la référence "
    "GO-2026-11-22-124, ou qui porte un solde (aucun solde, aucune couverture et aucun plancher n'entrent dans une règle "
    "de départ de cette clé : § Règle des clés) ;")

inserer_apres(89, (
    "- **Avant le départ, hors du lanceur (v11 ; conditions de GO-2026-11-22-107)** : la session d'exécution ne lance pas "
    "la course tant que ne sont pas réunis : la contre-lecture de ce texte et celle du lanceur v11 (le lanceur vérifie la "
    "première, § Contre-lecture) ; les prix relevés le jour du départ (Claude : relevé scellé du jour, vérifié par le "
    "lanceur ; Astra : R-4905, repris par la sonde du jour ; Argon et Carbon : page de prix du fournisseur relue le jour "
    "du départ par la session d'exécution et versée au dépôt — un prix au-dessus de 4 ou de 20 USD par million de jetons "
    "interdit le départ) ; **un essai à blanc** du lanceur v11, sans appel à un "
    "fournisseur, joué jusqu'au manifeste de fin sur la configuration v11 et versé au dépôt avant le départ réel. Le "
    "lanceur ne vérifie ni qu'un essai à blanc a été versé ni que la page de prix a été relue : ces deux conditions sont "
    "tenues par la session d'exécution et citées par les commandes exactes. Après le 2026-11-25, la confirmation par "
    "Lazar de la prolongation de l'exception est exigée par le lanceur lui-même (§ Règle des clés, « Période »)."))

remplacer_ligne(93, "- **Pendant, en plus (v11) — garde de la part Claude**", (
    "- **Pendant, en plus (v11) — garde de la part Claude** : le lanceur relève l'état et le journal du relais Claude au "
    "moins une fois par minute (compte de la part Claude au fil de l'eau) ; au **premier refus** — appel refusé par ce "
    "relais parce que son plafond de 45 USD est atteint (statut 402 du relais), ou appel que l'interface d'Anthropic "
    "refuse et que le relais relaie (statut 400 à 499, hors 429, écrit à son journal ; forme relevée du manque de crédit : "
    "400 « credit balance is too low », R-4833 et R-4842) — → arrêt de la course par le lanceur (signal à l'orchestrateur "
    "par son PID, arrêt propre, manifestes écrits, **code 5**), ce qui a été fait est écrit, et une alerte scellée pour la "
    "mère (`alerte-arret-part-claude.json`), qui prévient Lazar ; détail au § Règle des clés, « Clé LUC ». Cette garde "
    "est essayée sur un cas sain (aucun refus : la course va à son terme) et sur deux artefacts (un refus pour plafond, "
    "puis un refus de l'interface, plantés dans l'état et le journal d'un relais factice : arrêt, code 5, alerte), R5."))

sub(95, " (**v11** : dont un plafond de la part Claude sous son plancher)", "")

# ------------------------------------------------------------------------------------------------ plafond
remplacer_depuis(99, "**v11** : aucun devis neuf ;", (
    "**v11** : devis v11 (écrit pour cette version sur les décisions de la mère, R-5007, point (d), et R-5018 ; à "
    "contre-lire). Quatre choses changent. **Les prix comptés pour Argon et pour Carbon** sont 4 et 20 USD par million de "
    "jetons, réflexion comprise dans la sortie, au lieu des bornes 8,3 et 41,5 : c'est le prix le plus haut de la page de "
    "prix du fournisseur versée au dépôt (2 et 10 jusqu'au 30 novembre 2026, 4 et 20 à partir du 1er décembre ; pièces). "
    "**Carbon** est au prix plein (le lot avait un facteur 0,5) : avec les hypothèses du devis v10 (§ 2 : réflexion 20 000 "
    "jetons, réponse 3 500, entrée 2 618), (2 618 × 4 + 23 500 × 20) / 10⁶ = 0,4805 USD par appel, 7,69 USD pour seize "
    "appels (7,98 au devis v10, au prix du lot et aux bornes). **Les juges** ont un plafond de session de 1,00 USD au lieu "
    "de 0,60 (§ Espèces, « Argon ») ; la borne des plafonds de session passe de 472 à 600 USD (80 × 3,00 + 160 × 0,25 + "
    "320 × 1,00) : seul le plafond d'arrêt borne la dépense. **La réflexion d'Argon** sous la garde s'ajoute à ses deux "
    "postes, au prix de sortie ; elle n'est mesurée dans aucune pièce lue. Cinq espèces, **sans la réflexion d'Argon** : "
    "**35,68** USD sans marge, **39,25** avec (41,14 et 45,25 au devis v10) ; base de l'écart au devis : 35,683. Chaque "
    "millier de jetons de réflexion moyenne par appel d'Argon ajoute 3,52 USD (176 appels : 0,32 USD pour le proposeur, "
    "3,20 pour le juge) ; à sa provision entière (16 384 jetons à chaque appel), le sous-total est 93,36 USD, 102,69 avec "
    "la marge ; le cumul n'atteint 150 USD qu'au-delà de 32 476 jetons de moyenne (31 462 avec la marge sur les autres "
    "postes), presque le plafond de sortie d'Argon lui-même : aux prix déclarés, la réflexion d'Argon n'a pas de prise "
    "réaliste sur le plafond d'arrêt (aux bornes des v6 à v10, ce seuil était à 13 812 jetons : devis v11, § 8). Le devis "
    "v11 ne donne plus de « haut ». Astra : le devis compte tout proposeur hors Claude à un prix par appel supposé "
    "(0,276 USD), qu'il ne tire pas d'un prix par jeton ; les prix relevés de `gpt-6.2-astra` (8 et 40 USD par million, "
    "R-4905) sont plus bas que ceux de la commande en v10 (10 et 50) : aucun chiffre n'est changé de ce fait. **Dépense "
    "comptée et facture** : le plafond d'arrêt, les plafonds des étapes et les plafonds de session portent sur la dépense "
    "**comptée** par les commandes, aux prix déclarés ; jusqu'au 30 novembre 2026, les prix déclarés d'Argon et de Carbon "
    "sont le double du prix de la page, et la dépense comptée sur la clé de Google le double de la dépense facturée, si la "
    "page dit vrai ; un prix réel au-dessus du prix déclaré ferait sous-compter la dépense, ce que les bornes des v6 à v10 "
    "excluaient : la page est relue le jour du départ (liste d'arrêt). **Pire cas 150**, parts au pire de la clé de Google "
    "(198) et de la clé d'OpenAI (48) : inchangés ; part au pire de la clé Claude : le plafond de la part Claude, 45 USD "
    "(paragraphe suivant le bloc des plafonds des étapes, et § Règle des clés)."))

ajouter_fin(108, "Ce régime suppose une proposition bien au-delà de son haut", (
    " **v11** : aucun seuil n'est changé (mêmes budgets d'étapes dans la configuration v11) ; le « haut » cité ci-dessus "
    "est celui du devis v10 (aux bornes, Carbon au prix du lot, sans réflexion d'Argon). Aux estimations du devis v11, "
    "sans réflexion d'Argon, le cumul avant les juges est 27,09 USD et l'étape des juges reçoit un plafond dur de "
    "122,91 USD ; elle coûte 8,60 USD, plus 3,20 USD par millier de jetons de réflexion moyenne par appel de juge "
    "d'Argon : à la provision entière d'Argon à chaque appel, rien n'est coupé (devis v11, § 4)."))

remplacer_ligne(110, "**Plafond de la part Claude (v11).**", (
    "**Plafond de la part Claude (v11).** La part Claude de la course (deux proposeurs, aiguilleur, premier juge) a, en "
    "plus, son propre plafond, plus bas : **45 USD**, plafond propre à la clé LUC (décision de la mère, R-5007, point "
    "(a) ; mots de Lazar, GO-2026-11-22-124 : plafond inchangé, plancher de départ et lecture du solde retirés ; § Règle "
    "des clés, « Clé LUC »). Il est tenu par le relais Claude, non par l'orchestrateur ; il ne change ni S17, ni les "
    "plafonds des étapes, ni les seuils ci-dessus, qui restent calculés sur 150 USD. Quand il est atteint, ou quand "
    "l'interface d'Anthropic refuse un appel avant qu'il le soit, le lanceur arrête la course (code 5, alerte) : une étape "
    "peut donc être interrompue alors que son plafond dur n'est pas épuisé. Repères, sans valeur de borne : part Claude "
    "estimée 20,65 USD (devis v11, § 5) ; cumul estimé de la part Claude après la proposition 8,69 USD, après l'aiguillage "
    "14,14 USD (prix par appel du devis v6, § 2, marge de 10 % comprise : (16 × 0,141 + 16 × 0,3525) × 1,1, puis "
    "+ 160 × 0,031 × 1,1)."))

# ------------------------------------------------------------------------------------------------ règle des clés
sub(114, "(R-3228 ; **v11** : GO-2026-11-22-107) :", "(R-3228 ; **v11** : GO-2026-11-22-107 et GO-2026-11-22-124) :")

sub(123, "accordée par Lazar pour cette course (GO-2026-11-22-107, échéance 2026-11-25 ; mot direct, GO-2026-11-22-110).",
    "accordée par Lazar pour cette course (GO-2026-11-22-107 ; mot direct, GO-2026-11-22-110 ; précisions, "
    "GO-2026-11-22-124 ; période au paragraphe suivant).")
debut(124, "")
assert lignes[124] == ""
inserer_apres(124, (
    "**Période (v11).** La ligne GO-2026-11-18-14 porte l'échéance 2026-11-25 ; GO-2026-11-22-80 la prolonge au "
    "2026-12-15, mêmes périmètre, conditions et plafond. La ligne de l'exception GO-2026-11-22-107 porte l'échéance "
    "2026-11-25 ; GO-2026-11-22-124 la porte au 2026-12-15 « avec la course », sur une lecture de la mère (le mot de "
    "Lazar « ho » lu « ok ») que la ligne dit elle-même **à confirmer par Lazar**. Le lanceur lit ces quatre lignes dans "
    "le registre de `main` (présence, type « calcul », accordées par Lazar, aucune révocation qui les vise ; plafond de "
    "150 USD lu sur GO-2026-11-18-14) ; le registre dérivé qu'il passe à l'orchestrateur porte la période ainsi lue, dans "
    "la forme que la lecture de l'orchestrateur épinglé accepte (à établir par l'essai du lanceur). **Jusqu'au 2026-11-25 "
    "inclus**, le départ ne dépend d'aucune prolongation. **Du 2026-11-26 au 2026-12-15**, le départ exige les deux "
    "prolongations, et celle de l'exception ne vaut que confirmée : le lanceur exige alors, nommée par un de ses "
    "arguments, la ligne du registre où la mère a inscrit la confirmation de Lazar (accordée par Lazar, citant "
    "GO-2026-11-22-124) ; sans elle, pas de départ (code 2). Après le 2026-12-15 : pas de départ."), "")

sub(125, "pour la clé LUC, la part au pire est le plafond de la part Claude, et la règle de départ est celle du paragraphe "
         "« Clé LUC » ci-dessous.",
    "pour la clé LUC, la part au pire est le plafond de la part Claude (45 USD) et aucun reste n'est lu : la règle de "
    "départ est celle du paragraphe « Clé LUC » ci-dessous.")

sub(127, "(**v11** : la clé LUC, que seule la console de facturation rend, part sur la lecture de Lazar, paragraphe « Clé "
         "LUC » ;",
    "(**v11** : sauf la clé LUC, que seule la console de facturation rend ; elle part sans lecture de son solde, sur le "
    "mot de Lazar, GO-2026-11-22-124, paragraphe « Clé LUC » ;")

remplacer_ligne(129, "**Clé LUC : couverture, plafond de la part Claude, compte au fil de l'eau", (
    "**Clé LUC : plafond de la part Claude, compte au fil de l'eau, arrêt au premier refus (v11 ; GO-2026-11-22-107, "
    "-110, -111 et -124 ; R-5007).** Quatre faits fixent la règle. Le solde de la clé LUC n'est pas lisible par "
    "l'interface de programmation (GO-2026-11-22-110). La clé est en compte payant à recharge automatique, et Lazar a dit "
    "la recharge disponible « jusqu'à 40 euros » (GO-2026-11-22-111). La clé sert aussi d'autres chantiers, et ses soldes "
    "lus le 22 novembre (lignes GO-2026-11-22-72 et GO-2026-11-22-73) sont très en dessous des 150 USD de la part au pire "
    "d'un relais qui tient l'aiguilleur et un juge : appliquée à LUC, la règle de la v10 (reste lu au-dessus de 150 USD, "
    "sinon refus) interdirait tout départ. Enfin Lazar a tranché (GO-2026-11-22-124) : la part Claude repose sur la "
    "recharge automatique ; pas de plancher de couverture ; la lecture du solde le jour du départ n'est pas une "
    "condition ; l'arrêt au premier refus de l'interface reste, sans repli silencieux ; le plafond de la part Claude "
    "(45 USD) et le plafond de la course (150 USD) ne changent pas. La règle de la v10 est donc remplacée, **pour cette "
    "clé seulement**, par un départ sans lecture de solde, **sous un plafond propre de la seule part Claude**, sans "
    "toucher au plafond d'arrêt de 150 USD ni à rien de ce que la course sert ou mesure :"))

remplacer_ligne(131, "1. **Couverture déclarée.**", (
    "1. **Départ sans lecture de solde.** Le relevé des crédits du jour porte, pour la clé LUC, la mention « solde non "
    "lu » et la référence GO-2026-11-22-124 ; il ne porte ni solde, ni couverture, ni réserve, et aucun montant de cette "
    "clé n'entre dans une règle de départ : ni plancher, ni part au pire confrontée à un reste. Ce que la clé peut payer "
    "n'est connu de ce texte par aucune pièce : la recharge automatique (« jusqu'à 40 euros », GO-2026-11-22-111) est dite "
    "en euros, sans cours de change relevé, et le solde du jour n'est pas lu. Noms des champs : ceux du gabarit du relevé "
    "des crédits v11."))

remplacer_ligne(132, "2. **Plafond de la part Claude.**", (
    "2. **Plafond de la part Claude : 45 USD.** C'est le plafond propre à la clé LUC pour la part Claude de cette course "
    "(R-5007, point (a) ; GO-2026-11-22-124 : la couverture déclarée et ses quatre cinquièmes, que R-5007 posait à côté, "
    "tombent avec la lecture du solde). Le relais Claude est lancé avec 45 USD pour plafond en dollars, et le lanceur "
    "refuse le départ si le plafond lu par PID et dans l'état du relais en diffère d'un centime. Ce plafond est la part au "
    "pire de la clé LUC dans cette course, au dépassement du relais près (point 6). Il borne la seule part Claude (deux "
    "proposeurs, aiguilleur, premier juge) ; le plafond d'arrêt de 150 USD et les plafonds des étapes ne changent pas, et "
    "l'orchestrateur ne connaît pas ce plafond : pour lui, un appel que le relais refuse est un appel en échec du rôle "
    "(A3, A14) — lecture à confirmer sur l'orchestrateur épinglé par l'essai du lanceur."))

remplacer_ligne(133, "3. **Plancher de départ.**", (
    "3. **Aucun plancher de départ (GO-2026-11-22-124).** La course peut partir alors que la clé LUC ne couvre pas la part "
    "Claude estimée (20,65 USD, marge de 10 % comprise, devis v11, § 5) : la tentative unique est alors consommée par "
    "l'arrêt du point 5, sans avoir pu finir. C'est le risque que Lazar accepte par son mot (« on utilise la recharge "
    "automatique »), écrit ici ; ce texte n'y ajoute aucune condition."))

remplacer_ligne(134, "4. **Compte au fil de l'eau.**", (
    "4. **Compte au fil de l'eau.** Pendant la course, le lanceur lit l'état du relais Claude (dépense, montant engagé, "
    "appels, refus) et les lignes neuves de son journal (statut de chaque appel) au moins une fois par minute, et écrit "
    "chaque lecture dans un journal du run (montants, comptes et statuts, jamais un contenu). La **part Claude** est la "
    "dépense comptée par ce relais, à son barème, que le lanceur a vérifié égal au relevé du prix Claude du jour ; la "
    "**part Claude engagée** est cette dépense plus les montants réservés des appels en vol. Le relais refuse un appel dès "
    "que la part engagée, plus la réserve de cet appel (0,40 USD, défaut du programme épinglé), dépasserait 45 USD : "
    "au-delà de 44,60 USD de part engagée."))

remplacer_ligne(135, "5. **Arrêt et message.**", (
    "5. **Arrêt et message, au premier refus.** Deux refus valent arrêt : (a) le **refus du relais Claude** parce que son "
    "plafond est atteint (statut 402 du relais, écrit à son journal avec son motif) ; (b) le **refus de l'interface "
    "d'Anthropic**, que le relais épinglé relaie tel quel et dont son journal ne garde que le statut : tout appel relayé "
    "dont le statut rendu par l'interface est de 400 à 499, hors 429 (limite de débit). La forme relevée du manque de "
    "crédit est un statut 400, « credit balance is too low » (R-4833, R-4842) ; le journal du relais ne gardant pas le "
    "message, un statut 400 d'une autre cause (requête refusée) arrête la course de la même façon, et l'alerte dit le "
    "statut, non la cause. Les statuts 429 et 500 à 599 et les pannes de transport ne sont pas des refus au sens de cette "
    "garde : ce sont des échecs d'appel, laissés aux règles de l'orchestrateur (A3, A14). Au premier refus (a) ou (b), le "
    "lanceur arrête la course : signal d'arrêt à l'orchestrateur par son PID, arrêt propre, manifestes écrits, **code 5** ; "
    "il écrit et scelle une alerte pour la mère (`alerte-arret-part-claude.json` : nature du refus, statut, plafond, "
    "dépense et montant engagé lus, appels, étape en cours, ce qui a été fait), qui prévient Lazar. Si l'orchestrateur "
    "s'arrête de lui-même avant que le lanceur ait lu ce refus (A3 : trois appels refusés de suite arrêtent le rôle), le "
    "lanceur relit l'état et le journal du relais à la fin : un refus (a) ou (b) y vaut le code 5 et l'alerte, par la "
    "priorité des codes (4, puis 5, puis 6). Le lanceur ne relance rien, et aucun repli n'est fait (autre clé, autre "
    "modèle, abonnement) ; les cartes déjà produites sont rapportées ; la bonne fin n'est pas atteinte. C'est une cause "
    "technique déclarée (crédit ou plafond) au sens de la règle « une panne technique n'est pas un résultat » "
    "(GO-2026-11-22-77) : l'essai se rapporte tel quel, avec son issue codée, et une relance demande une version suivante "
    "et une décision nommée."))

remplacer_ligne(136, "6. **Ce que cette garde ne voit pas.**", (
    "6. **Ce que cette garde ne voit pas, et ce qu'elle suppose.** (i) Un refus qui n'arrive pas sous un statut 400 à "
    "499 : un flux ouvert sous le statut 200 puis coupé par une erreur du fournisseur est, pour le journal du relais, un "
    "appel de statut 200 ; l'appel est alors un échec du rôle pour l'orchestrateur (A3, A14), sans arrêt promis par le "
    "lanceur sur ce motif ; le manifeste de fin écrit le compte des appels du relais Claude par statut. (ii) Le "
    "dépassement du relais : il réserve un montant par appel avant de l'envoyer (0,40 USD) et règle au coût lu ; sa "
    "dépense peut dépasser 45 USD d'au plus (coût d'un appel − réserve) par appel en vol quand le plafond est atteint ; le "
    "dépassement lu dans son état est écrit au manifeste de fin. (iii) Le délai de la recharge automatique : ni son seuil "
    "de déclenchement ni son délai ne sont dans les pièces lues ; un refus de l'interface pendant ce délai arrête la "
    "course, alors que la recharge aurait pu couvrir la suite — conséquence dite de l'arrêt au premier refus. (iv) Les "
    "autres dépenses sur la clé LUC : la mère a écrit qu'aucune dépense neuve ne passe sur cette clé jusqu'à la fin de la "
    "course, hors du reste éventuel de GO-2026-11-22-72 (R-5007, point (b), qui partait « de la lecture du solde » ; ce "
    "texte le lit « du départ », la lecture n'ayant plus lieu) ; le lanceur ne le contrôle pas. Une autre dépense sur LUC "
    "pendant la course rapproche le refus de l'interface ; elle ne peut faire dépasser ni le plafond de la part Claude ni "
    "le plafond d'arrêt."))

remplacer_ligne(138, "Condition de GO-2026-11-18-14 (« Lazar prévenu avant qu'une clé n'atteigne zéro »)", (
    "Condition de GO-2026-11-18-14 (« Lazar prévenu avant qu'une clé n'atteigne zéro ») : pour la clé LUC, elle n'est plus "
    "tenue par une lecture de solde ni par un plancher ; Lazar a choisi de s'en remettre à la recharge automatique "
    "(GO-2026-11-22-124, mot postérieur, pour cette clé). Ce que ce texte garde : le plafond propre de 45 USD, l'arrêt au "
    "premier refus et l'alerte scellée, par laquelle la mère prévient Lazar. La clé LUC peut donc atteindre zéro pendant "
    "la course, et Lazar l'apprend alors par cette alerte, non avant."))

sub(140, "plafond : celui de la part Claude, au centime, **v11** ; 150 en v4 à v10",
    "plafond : celui de la part Claude, 45,00 USD, au centime, **v11** ; 150 en v4 à v10")

sub(142, "**v11** : la clé LUC n'est ni lisible par programme ni dispensée, elle part sur la couverture déclarée du "
         "paragraphe « Clé LUC ».",
    "**v11** : la clé LUC n'est ni lisible par programme ni dispensée par la mère ; elle part sans lecture de solde, sur "
    "le mot de Lazar (GO-2026-11-22-124), et le relevé l'écrit « solde non lu » avec cette référence (paragraphe « Clé "
    "LUC »).")
sub(142, "**v11**, clé LUC : reste estimé = couverture déclarée moins la part Claude comptée par le relais, à confirmer par "
         "une lecture de Lazar à la console.",
    "**v11**, clé LUC : aucun reste n'est estimé (solde non lu) ; le manifeste de fin écrit la part Claude comptée par le "
    "relais, que la mère transmet à Lazar.")
sub(142, "(**v11**, clé LUC : sous un cinquième de la couverture déclarée)", "(**v11** : sans objet pour la clé LUC)")

# ------------------------------------------------------------------------------------------------ différentiel v10 → v11
remplacer_ligne(275, "Mandat de la session de l'organisme (`0f7ddc54…`)", (
    "Mandat de la session de l'organisme (`0f7ddc54…`) sur la ligne GO-2026-11-22-107, décisions de la mère sur cette "
    "version (R-4995, R-5006, R-5007, R-5018) et mots de Lazar (GO-2026-11-22-124) : les trois changements du mandat, trois "
    "décisions qui en découlent, et leurs conséquences mécaniques. **Inchangés** : objet, question, absence d'hypothèse, "
    "de prédiction et de seuil ; ce qui est servi et retiré ; plan ; ce qui est mesuré et ne l'est pas (à deux précisions "
    "de coût près, points 4 et 10) ; plan d'analyse et critères de lecture gelés ; règles de N-073 ; ce que la course ne "
    "dit pas ; plafond d'arrêt 150 USD (GO-2026-11-18-14) ; budget, plafonds de relais et plafonds durs des étapes ; "
    "plafonds de session des proposeurs et de l'aiguilleur ; composition déclarée (deux Claude, Argon, Astra, Carbon ; "
    "pas de Kimi) ; orchestrateur épinglé ; consignes et liste des fils ; garde de crédit v6 ; porte de plafond ; "
    "procédure des relais persistants ; parts au pire des clés de Google (198) et d'OpenAI (48) ; gardes v7 à v10, hors "
    "celles que les points 5 à 7 retirent ; numéros des codes de sortie."))

DIFFERENTIEL = [
    "1. **Numéro et base** (écart au mandat, déclaré en tête ; R-4995) : v11 et non v8 ; base v10 et non v6.",
    "2. **Clé Claude** : `RR_ANTHROPIC_API_KEY_LUC` au lieu de `RR_ANTHROPIC_API_KEY_MINUIT` (sans crédit, R-4833) pour "
    "les deux proposeurs Claude, l'aiguilleur et le premier juge ; exception déclarée à la règle « Claude par "
    "l'abonnement » (GO-2026-11-22-70), accordée en GO-2026-11-22-107 et précisée en GO-2026-11-22-124 ; le lanceur exige "
    "la variable de la clé LUC, refuse un relais Claude sur une autre clé et vérifie les lignes de l'exception en plus de "
    "la ligne du plafond. **Retraits** : la clé Minuit, son crédit déclaré de 200 USD et son compte « au prix relevé » "
    "(v2 à v10).",
    "3. **Règle de départ de la clé LUC** (§ Règle des clés, « Clé LUC » ; R-5007, GO-2026-11-22-124) : départ sans "
    "lecture de solde, sans plancher ni couverture déclarée ; **plafond propre de la part Claude, 45 USD**, tenu par le "
    "relais Claude, lancé à ce plafond exactement. **Remplace**, pour cette clé seulement, la règle « reste lu au-dessus "
    "de la part au pire de 150 USD et d'un cinquième du crédit », qui interdirait tout départ sur LUC. La condition "
    "« Lazar prévenu avant qu'une clé n'atteigne zéro » n'est plus tenue, pour cette clé, que par l'alerte de l'arrêt. Le "
    "plafond d'arrêt de 150 USD et tout ce que la course sert ou mesure ne changent pas.",
    "4. **Garde de la part Claude pendant la course** : compte au fil de l'eau sur l'état et le journal du relais Claude ; "
    "arrêt de la course au premier refus — du relais à son plafond (statut 402), ou de l'interface d'Anthropic relayé par "
    "lui (statut 400 à 499, hors 429) — (code 5) et alerte scellée pour la mère, qui prévient Lazar ; limites de la garde "
    "écrites (refus sous un statut 200, dépassement du relais, délai de la recharge, autres dépenses sur la clé) ; cette "
    "issue est ajoutée aux critères de bonne fin (elle l'interdit) et à la liste d'arrêt, et la part Claude relevée au fil "
    "de l'eau à ce qui est mesuré.",
    "5. **Astra** : `gpt-6.2-astra` au lieu de `gpt-6-astra` (R-4900) ; clé déclarée `OPENAI_API_KEY_2` ; prix relevés 8 "
    "et 40 USD par million de jetons (16 et 60 au-delà de 272 000 jetons d'entrée, hors d'atteinte), R-4905 ; sonde du "
    "jour refaite avec ce modèle, cette clé et ces prix, par des programmes de sonde neufs. **Retraits** : la sonde v2 et "
    "la sonde commune v1, qui portent `gpt-6-astra` en dur.",
    "6. **Carbon** : appel en flux sous la garde gelée des appels aux modèles de Google (GO-2026-11-21-71, "
    "GO-2026-11-21-47), au prix plein ; pire cas d'un appel dit dans les deux façons de compter la réflexion. "
    "**Retraits** : la commande Gemini par lot, le relais Gemini v4, le facteur de lot, et les gardes v8 et v9 propres au "
    "lot (provision de 28 672 jetons et son minimum de 25 870, délai de lot de 1 620 s, sortie retenue d'au moins 24 500 "
    "jetons, bornes de lots et de relevés du relais) ; en flux, les contrôles sont ceux de la garde gelée et les réglages "
    "à inscrire.",
    "7. **Argon** (décision de la mère, R-5007, point (c)) : sous la même garde gelée — niveau de réflexion `high`, "
    "pensées demandées en retour, 16 000 jetons de texte au moins au-delà de la provision, défauts lus après la réponse. "
    "**Retraits** : la commande `commande_argon_v3d.py` et son enveloppe `appel-argon-v5.sh`, épinglées de la v6 à la "
    "v10.",
    "8. **Prix comptés pour Argon et pour Carbon** (décision de la mère, R-5018) : 4 et 20 USD par million de jetons, "
    "réflexion comprise dans la sortie, prix le plus haut de la page de prix du fournisseur versée au dépôt (2 et 10 "
    "jusqu'au 30 novembre 2026, 4 et 20 ensuite), au lieu des bornes 8,3 et 41,5 ; le lanceur refuse d'autres prix dans "
    "les arguments des deux commandes ; la page est relue le jour du départ.",
    "9. **Plafond de session des juges** : 1,00 USD au lieu de 0,60 (configuration v11 ; R-5018) : aux réglages d'Argon "
    "sous la garde, le pire cas d'un appel de juge vaut 0,9985 USD (0,6708 si la réflexion compte dans le plafond de "
    "sortie) ; le relèvement vaut aussi pour le juge Claude. Borne des plafonds de session : 600 USD au lieu de 472 ; "
    "seul le plafond d'arrêt borne la dépense.",
    "10. **Devis v11** (écrit pour cette version, à contre-lire) : aux prix déclarés, Carbon au prix plein, 0,4805 USD par "
    "appel estimé ; cinq espèces, sans la réflexion d'Argon : 35,68 USD sans marge, 39,25 avec ; base de l'écart au devis "
    "35,683 ; réflexion d'Argon non mesurée, 3,52 USD par millier de jetons moyens par appel, 93,36 USD à sa provision "
    "entière ; plus de « haut » ; pire cas 150, inchangé (§ Plafond).",
    "11. **Lignes de GO et période** : GO-2026-11-18-14 (plafond d'arrêt, échéance 2026-11-25, prolongée au 2026-12-15 "
    "par GO-2026-11-22-80) ; GO-2026-11-22-107 (exception, échéance 2026-11-25, portée au 2026-12-15 par "
    "GO-2026-11-22-124 sous la réserve d'une confirmation de Lazar) ; jusqu'au 2026-11-25, départ sans prolongation ; "
    "ensuite, confirmation inscrite exigée (§ Règle des clés, « Période »).",
    "12. **Conditions de GO-2026-11-22-107 tenues hors du lanceur** : essai à blanc du lanceur v11 versé avant le "
    "départ ; page de prix d'Argon et de Carbon relue le jour du départ ; ajoutées à la liste d'arrêt.",
    "13. **Contre-lecture** : par un Opus neuf, puis vérification des corrections par le même contre-lecteur (pièce de "
    "classe A) ; le modèle K contre-lisait les v2 à v10.",
    "14. **Configuration v11** : la v9 au nom de la clé Claude, au plafond du relais Claude (45 USD), au plafond de "
    "session des juges (1,00 USD) et au bloc descriptif de Carbon près.",
    "15. **Chemins et noms** : contre-lecture, déclaration, relevés, commandes et rapports de sonde sous `course-v11/` "
    "(`declaration-relais-course-affinage-mentors-v11.json`, `releve-credits-avant-course-affinage-mentors-v11.json`, "
    "`releve-prix-claude-course-affinage-v11.json`, `commandes-exactes-course-affinage-v11.md`) ; sorties "
    "`/home/user/sorties-course-affinage-mentors-v11/` et `runs/<id>-course-affinage-mentors-v11/` ; alerte neuve "
    "`alerte-arret-part-claude.json` ; une seule course de v1 à v11.",
]
ANCIENS = {277: "1. **Numéro et base**", 278: "2. **Clé Claude**", 279: "3. **Règle de départ de la clé LUC**",
           280: "4. **Garde de la part Claude pendant la course**", 281: "5. **Astra**", 282: "6. **Carbon**",
           283: "7. **Devis**", 284: "8. **Lignes de GO**", 285: "9. **Contre-lecture**", 286: "10. **Configuration v11**",
           287: "11. **Chemins et noms**", 288: "12. **Point ouvert**"}
for n, p in ANCIENS.items():
    debut(n, p)
# les points repris tels quels du brouillon 1 doivent l'être à l'octet près
assert lignes[281] == DIFFERENTIEL[4], "point Astra du différentiel"
assert lignes[285].split(" : ", 1)[1] == DIFFERENTIEL[12].split(" : ", 1)[1], "point Contre-lecture du différentiel"
assert lignes[287].split(" : ", 1)[1] == DIFFERENTIEL[14].split(" : ", 1)[1], "point Chemins et noms du différentiel"
assert len(DIFFERENTIEL) == 15 and all(x.startswith(f"{i + 1}. **") for i, x in enumerate(DIFFERENTIEL))
lignes[277] = "\n".join(DIFFERENTIEL)
touchees.add(277)
for n in range(278, 289):
    supprimees.add(n)

# ------------------------------------------------------------------------------------------------ dernière section
debut(290, "## Emplacements et points à trancher avant le scellement (section à retirer de la version scellée)")
FINALE = [
    "## Emplacements et points à trancher avant le scellement (section à retirer de la version scellée)",
    "",
    "Emplacements à remplir :",
    "",
    "1. EMPREINTE À INSCRIRE — configuration fixe v11 (pièces).",
    "2. EMPREINTE À INSCRIRE — commande de Carbon en flux et relais de Carbon (pièces) ; RÉGLAGE À INSCRIRE — provision "
    "de réflexion, plafond de sortie, délais et bornes du relais de Carbon (§ Espèces, liste d'arrêt).",
    "3. EMPREINTE À INSCRIRE — commande d'Argon sous la garde, son enveloppe s'il en reste une, son relais s'il change "
    "(pièces) ; RÉGLAGE À INSCRIRE — réglages exacts d'Argon (§ Espèces).",
    "4. EMPREINTE À INSCRIRE — programme de la sonde d'Astra et sonde commune de cette version (pièces).",
    "5. EMPREINTE À INSCRIRE — essais du lanceur, gabarit de déclaration, gabarits des deux relevés (pièces) ; celle du "
    "lanceur seulement s'il ne porte plus l'empreinte de ce texte dans son code (sinon, cycle d'empreintes).",
    "6. RÉGLAGE À INSCRIRE — libellé du modèle que la contre-lecture doit dire (§ Contre-lecture).",
    "",
    "Points à trancher ou à confirmer, avec la recommandation du rédacteur :",
    "",
    "1. **Plafond de session des juges : 1,00 ou 1,10 USD.** La mère a fixé 1,00 USD (R-5018). Si la commande d'Argon sous "
    "la garde ajoute la provision au plafond de sortie, la marge n'est que de 385 jetons au-dessus de l'entrée de juge "
    "attendue, dont le cadre est supposé (devis v11, § 2). Recommandation : 1,10 USD dans ce cas (entrée couverte : 29 240 "
    "jetons), 1,00 USD si la commande compte la réflexion dans le plafond de sortie ; à trancher avec qui écrit la "
    "commande d'Argon, avant de sceller la configuration v11.",
    "2. **Page de prix relue le jour du départ** : condition ajoutée par le rédacteur à la lettre « prix relevés » de "
    "GO-2026-11-22-107, parce qu'un prix réel au-dessus du prix déclaré ferait sous-compter la dépense ; à confirmer.",
    "3. **Période** : ce brouillon exige, après le 2026-11-25, la confirmation de Lazar inscrite au registre et nommée au "
    "lanceur (retenu par la session de l'organisme le 22 novembre) ; la forme du registre dérivé que l'orchestrateur "
    "épinglé accepte pour une échéance prolongée par une autre ligne est à établir par l'essai du lanceur.",
    "4. **Écrit de la mère sur les autres dépenses de la clé LUC** (R-5007, point (b)) : ce brouillon le lit « du départ à "
    "la fin de la course » et ne le fait pas contrôler par le lanceur (retenu par la session de l'organisme le 22 "
    "novembre) ; à confirmer par la mère.",
    "5. **Refus de l'interface** : ce brouillon arrête la course sur tout statut 400 à 499, hors 429, relayé par le relais "
    "Claude, faute de message au journal du relais épinglé (retenu par la session de l'organisme le 22 novembre) ; si le "
    "lanceur v11 peut lire le message d'erreur ailleurs (journaux de l'orchestrateur), la règle peut être resserrée au "
    "seul manque de crédit — par un changement de ce texte, non par un écart silencieux.",
    "",
    "Points que ce texte fixe et que le lanceur v11 doit tenir, avec un essai sain et un essai artefact chacun (R5) ; si "
    "le lanceur fait autrement, le texte ou le lanceur change, jamais un écart silencieux. La liste phrase par phrase est "
    "dans `" + ANNEXE + "` ; en résumé :",
    "",
    "- le plafond du relais Claude égal à 45,00 USD au centime (arguments lus par PID et état), et l'entrée « solde non "
    "lu, GO-2026-11-22-124 » de la clé LUC au relevé des crédits, sans solde, plancher ni couverture ;",
    "- la lecture des lignes GO-2026-11-18-14, GO-2026-11-22-80, GO-2026-11-22-107 et GO-2026-11-22-124, et, après le "
    "2026-11-25, de la ligne de confirmation nommée ;",
    "- le relevé de l'état et du journal du relais Claude au moins une fois par minute, l'arrêt au premier refus (statut "
    "402 du relais ; statut 400 à 499, hors 429, de l'interface), le code 5 et l'alerte `alerte-arret-part-claude.json` ;",
    "- la garde gelée des appels aux modèles de Google sur les commandes de Carbon et d'Argon, avant l'envoi et après la "
    "réponse ; les prix d'Argon et de Carbon à 4 et 20 USD par million de jetons ; le plafond de session des juges à "
    "1,00 USD, et le pire cas d'un appel de juge d'Argon contrôlé sur la plus longue entrée de juge admise ;",
    "- la sonde d'Astra faite avec `gpt-6.2-astra`, `OPENAI_API_KEY_2` et les prix 8 et 40 ;",
    "- la base de l'écart au devis, 35,683 USD pour cinq espèces ;",
    "- les gardes héritées des lanceurs v7 à v10 que ce texte garde (bornes basses de tous les relais, exclusion mutuelle "
    "avec la course d'auto-conception, sonde liée à la sonde commune, état de relais neuf et lisible, codes de sortie "
    "distincts dont le code 6, plafond de session des proposeurs à 3,00 USD).",
    "",
    "Du brouillon 1 au brouillon 2 : numéro et base tranchés (R-4995) ; plafond de la part Claude fixé à 45 USD ; "
    "couverture déclarée, quatre cinquièmes, plancher de 20,65 USD et lecture du solde retirés (R-5007, "
    "GO-2026-11-22-124) ; refus de l'interface ajouté à l'arrêt ; Argon sous la garde (R-5007) ; prix d'Argon et de "
    "Carbon déclarés à 4 et 20 USD par million de jetons et plafond de session des juges à 1,00 USD (R-5018) ; devis v11 "
    "cité ; pire cas de Carbon dit dans les deux façons de compter ; période et confirmation de la prolongation ; "
    "conditions de GO-2026-11-22-107 hors du lanceur.",
]
lignes[290] = "\n".join(FINALE)
touchees.add(290)
for n in range(291, 311):
    supprimees.add(n)

# ------------------------------------------------------------------------------------------------ assemblage
sortie = []
for n in range(1, 311):
    if n not in supprimees:
        sortie.append(lignes[n])
    sortie.extend(apres.get(n, []))
texte = "\n".join(sortie) + "\n"
for interdit in ("RÉFÉRENCE À INSCRIRE", "quatre cinquièmes de la couverture", "couverture déclarée du paragraphe"):
    assert interdit not in texte, interdit
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 1 touchées :", sorted(touchees))
print("lignes du brouillon 1 supprimées :", sorted(supprimees))
print("insertions après les lignes :", sorted(apres))
print("lignes du brouillon 2 :", texte.count("\n"))
