#!/usr/bin/env python3
"""Compte les articles des décisions de conception de l'organisme (lecteur : modèle C), version 2.

Remplace la v1 (qui reste, R12). LECTURE SEULE sur les décisions ; écrit seulement articles-decisions-v2.json
(création : refuse d'écraser). Aucun accès réseau, aucune clé, aucune recherche dans l'arbre : les fichiers sont nommés.

RÈGLE DE DÉCOUPAGE v2 (une seule, la même pour toutes les décisions ; corrige les constats 4 et 5 de la critique)
  Une section est un bloc introduit par une ligne « ## ». Toute section d'une décision est une section d'articles,
  SAUF : les « Mots de Lazar » (source, pas dispositif), le « Contexte », les « Points à régler » (questions
  ouvertes, non décidées), et l'en-tête (tout ce qui précède la première section : provenance, transcription,
  portée). Pour N-049 et N-050, qui reprennent la même note transcrite, chaque fichier ne compte que sa propre
  section (de « ## N-049 » à « ## N-050 » ; de « ## N-050 » à la fin).
  Dans une section d'articles, un ARTICLE est une unité de premier niveau :
    (a) un point numéroté « N. » ; un point « 5. et 6. » donne deux articles (5 et 6) de même texte, marqués
        « jumelé » ;
    (b) une puce « - » de premier niveau ;
    (c) un paragraphe libre (bloc de lignes non vides hors points et puces), SAUF s'il commence par « Numéro »
        (formalité d'inscription : seule exclusion de contenu) ; un paragraphe qui se termine par « : » (amorce)
        est un article, de type « amorce », et reçoit le rang 0.
  Chaque article porte la « nature » de sa section : « dispositif » (énoncés retenus, ce que la décision fixe,
  lecture retenue, réserve, section N-049 ou N-050), « conséquence » (« Ce que cela change »), « borne » (« Ce que
  cela ne décide pas », « Ce que la décision ne fixe pas », « Ce qui ne change pas »).
  L'identifiant est « N-0xx.k » où k est le rang (1, 2, ...) de l'article non amorce dans l'ordre du fichier, tous
  les articles confondus ; l'amorce est « N-0xx.0 » ; pour N-045 : « N-045v1.k » (remplacée) et « N-045v2.k ». Un
  point numéroté garde son numéro quand la suite est continue. Les identifiants de la v1 gardent leur sens.
  La « ligne » est la première ligne du fichier source (numérotée à partir de 1), « ligne_fin » la dernière.

LE CLASSEMENT N'EST PAS DÉDUIT : le tableau PORTEE est un jugement de l'auteur ; le programme vérifie seulement que
chaque phrase de fondement est une sous-chaîne du fichier cité (gras et accents graves ôtés).

MASQUAGE : le texte recopié et les fondements sont écrits avec un masque « [modèle masqué] » à la place de tout
identifiant de modèle de la famille de l'assistant (interdit dans les fichiers produits) ; la ligne et
l'empreinte de la source permettent de relire l'original. Le masque est rejouable (voir MASQUES).

Usage :
  python3 -I -B compter_articles_decisions_v2.py [--racine DOSSIER] [--sortie DOSSIER] [--table] [--totaux] [--verifier-md FICHIER]
"""
import argparse, hashlib, json, os, re, sys

RACINE_DEFAUT = "/home/user/controle-ia-travail"
SORTIE_DEFAUT = RACINE_DEFAUT + "/docs/notes/organisme-ecart-conception-code-v1"

FICHIERS = [
    ("N-044", "docs/decisions/decision-N-044-v1.md", "2b70bdac", "N-044"),
    ("N-045-v1", "docs/decisions/decision-N-045-v1.md", "42be51f6", "N-045v1"),
    ("N-045-v2", "docs/decisions/decision-N-045-v2.md", "c7b05e39", "N-045v2"),
    ("N-049", "docs/decisions/decision-N-049-v1.md", "8a5bf5e5", "N-049"),
    ("N-050", "docs/decisions/decision-N-050-v1.md", "a54b128d", "N-050"),
    ("N-052", "docs/decisions/decision-N-052-v1.md", "817d218b", "N-052"),
    ("N-058", "docs/decisions/decision-N-058-v1.md", "854f2724", "N-058"),
    ("N-059", "docs/decisions/decision-N-059-v1.md", "41aff854", "N-059"),
    ("N-065", "docs/decisions/decision-N-065-v1.md", "f820e90d", "N-065"),
]
FENETRES = {  # préfixe de la ligne de début, préfixe de la ligne de fin (exclue) ; absent = tout le fichier
    "N-049": ("## N-049 (proposé)", "## N-050 (proposé)"),
    "N-050": ("## N-050 (proposé)", None),
}
SECTIONS_EXCLUES = ("Mots de Lazar", "Les mots de Lazar", "Contexte", "Points à régler")

# --- masque (motifs construits par morceaux pour ne pas écrire les identifiants dans ce fichier) ---
_A = "cla" + "ude"
_NOMS = "|".join(["op" + "us", "fa" + "ble", "son" + "net", "hai" + "ku"])
MASQUES = [
    re.compile(r"\b" + _A.upper() + r"_[A-Z0-9_]+"),
    re.compile(_A + r"-[a-z0-9.-]+", re.I),
    re.compile(r"\b(?:" + _NOMS + r")\b(?:\s*5\.[?0-9]+)?", re.I),
    re.compile(r"(?<=-)(?:" + _NOMS + r")(?=-)", re.I),
]
MASQUE = "[modèle masqué]"

def masquer(s):
    n = 0
    for m in MASQUES:
        s, k = m.subn(MASQUE, s)
        n += k
    return s, n

def norm(s):
    s = s.replace("**", "").replace("`", "")
    return " ".join(s.split())

# --- portée : objet, base, fondements (clé de décision, phrase exacte), statut, nœud ---
OI_T = "organisme d'idéation (texte)"
OI_I = "organisme d'idéation (par inférence écrite)"
CA = "lignée conv-audit seulement"
PC = "programme de contrôle"
MIXTE = "mixte (voir note)"
COORD = "ordre de travail entre lignées"
GOUV = "gouvernance du dépôt (hors objet d'organisme)"
ETAB = "portée à établir (lecture du document cité)"
OBJETS = [OI_T, OI_I, CA, PC, MIXTE, COORD, GOUV, ETAB]
# base : T = une phrase de l'article nomme l'objet ; S = l'objet vient d'une autre section de la même décision
# (portée, titre de section, « Ce que cela change ») ; I = inférence écrite (chaîne au § 1 du document) ;
# A = aucun objet d'organisme nommé, classement de l'auteur.

def _f(k, *phr):
    return [(k, p) for p in phr]

PORTEE = {}
def P(ident, objet, base, fond, statut="retenu", noeud="", note=""):
    PORTEE[ident] = dict(objet=objet, base=base, fond=fond, statut=statut, noeud=noeud, note=note)

# ---- N-044
P("N-044.1", PC, "T", _f("N-044", "Objectif ultime (axe « contrôle de populations d'agents », essaim autonome)",
                         "cette note fixe la lecture du programme pour les préenregistrements à venir (étape 2 et suivants)"))
P("N-044.2", CA, "T", _f("N-044", "en attente de son mot pour l'étape 1", "restent en attente du mot de Lazar"), "en attente du mot de Lazar")
P("N-044.3", CA, "T", _f("N-044", "Pour l'étape 1, seul le vivier de conception entre dans sa v4 (R-378)",
                         "identifiants disjoints du test et du test final, vérifiés par le script d'extraction"))
P("N-044.4", CA, "T", _f("N-044", "le noyau peut poser une question en texte libre (question_ouverte)",
                         "posée aux organismes avant tout matériau de notre part (anti-enfermement)",
                         "les réponses sont du matériau, jamais une consigne")
  + _f("N-065", "Il reçoit des questions ouvertes du programme"),
  "retenu ; extension à l'atelier d'idées non décidée (nœud 2)", "2",
  "le noyau est l'objet nommé ; le pluriel « aux organismes » ne nomme pas l'organisme d'idéation")
P("N-044.5", CA, "T", _f("N-044", "trois bras à l'étape 2 (mission + miroir fonctionnel rendu dans historique ; contrainte câblée dans le noyau ; rien)"))
P("N-044.6", CA, "T", _f("N-044", "la v4 de l'étape 1 sert le vivier pendant la conception",
                         "les préenregistrements de l'étape 2 testent l'universalité sur des familles retenues"))
P("N-044.7", PC, "A", _f("N-044", "les règles R1 à R14, la banque scellée"), "retenu (invariant)")
# ---- N-045 (v1 remplacée, v2 en vigueur) : points 1 à 3 = lignée par leur section et « Ce que cela change » ; nœud 1
for v, rempl in (("v1", "remplacée par N-045v2"), ("v2", "retenu")):
    k = "N-045-" + v
    p = "N-045" + v
    st13 = rempl if v == "v1" else "retenu ; extension à l'organisme d'idéation non décidée (nœud 1)"
    P(p + ".1", CA, "S", _f(k, "à partir de l'étape 2", "Noyau (étape 2 et après ; à coder par « session-depot »",
                            "ou instrument local entraîné par le noyau (sonde, adaptateur : espèces LOCAL:<identifiant>)"), st13, "1",
      "les trois phrases de « Ce que cela change » rattachent le point au noyau et aux préenregistrements de l'étape 2")
    P(p + ".2", CA, "S", _f(k, "à partir de l'étape 2",
                            "le score de développement rendu à l'organisme dans historique porte, à côté de l'exactitude équilibrée, le coût de la génération",
                            "le juge consigne le coût de la génération par espèce et par rôle",
                            "Le juge externe (exactitude équilibrée sur le test caché, métrique de choix) ne change pas"), st13, "1",
      "reclassé : portée douteuse en v1, lignée conv-audit en v2 (même critère que N-045v2.5)")
    P(p + ".3", CA, "S", _f(k, "à partir de l'étape 2", "La nécessité de la frontière est une sortie mesurée, pas un choix d'avance",
                            "Préenregistrements (étape 2 et suivants) : forme du score net et λ gelés ; lecture à deux axes ; ablation « sans frontière » rapportée"),
      st13, "1")
    P(p + ".4", CA, "T", _f(k, "Aucune voie à concepteur entraîné par renforcement n'est payée avant qu'une voie bon marché ait montré"), rempl)
if True:  # v1 : points 5 à 9
    P("N-045v1.5", MIXTE, "A", _f("N-045-v1", "les cerveaux de frontière ne sont jamais entraînés", "la vérité du test caché ne nourrit ni l'organisme ni un concepteur",
                                  "R1 à R14 ; la banque scellée ; H-E1 et H-G1 tels que scellés ou en cours de scellement"),
      "remplacée par N-045v2", "", "invariants du programme (R1 à R14, banque, H-E1, H-G1) et de la lignée (cerveaux de frontière, test caché, concepteur)")
    P("N-045v1.6", CA, "T", _f("N-045-v1", "Noyau (étape 2 et après ; à coder par « session-depot »", "le juge consigne le coût de la génération par espèce et par rôle"), "remplacée par N-045v2")
    P("N-045v1.7", CA, "T", _f("N-045-v1", "Préenregistrements (étape 2 et suivants) : forme du score net et λ gelés"), "remplacée par N-045v2")
    P("N-045v1.8", PC, "T", _f("N-045-v1", "cette note en fixe la lecture jusqu'à une version nouvelle, comme N-044"), "remplacée par N-045v2")
    P("N-045v1.9", CA, "T", _f("N-045-v1", "le bras « score permuté » dans la v8 de la confrontation", "les témoins de sortie du modèle de 8 milliards pour les sondes de l'étape 1"),
      "remplacée par N-045v2 ; points reportés (borne)")
P("N-045v2.5", CA, "T", _f("N-045-v2", "ce que cet énoncé ajoute vaut pour l'étape 2 et le concepteur", "Pour les organismes des courses actuelles"))
P("N-045v2.6", CA, "T", _f("N-045-v2", "l'organisme entraîne lui-même, par l'instrument (B), un adaptateur qui propose des conceptions",
                           "le concepteur figé reçoit une archive consultable des mêmes trajectoires"))
P("N-045v2.7", CA, "T", _f("N-045-v2", "un concepteur à sortie contrainte et un concepteur à sortie libre", "la voie est à fixer après le tour v4 du collisionneur"),
  "à fixer (après le tour v4 du collisionneur)")
P("N-045v2.8", MIXTE, "A", _f("N-045-v2", "les cerveaux de frontière ne sont jamais entraînés", "la vérité du test caché ne nourrit ni l'organisme ni un concepteur",
                              "R1 à R14 ; la banque scellée ; H-E1 et H-G1 tels que scellés ou en cours de scellement"),
  "retenu (invariants)", "", "invariants du programme (R1 à R14, banque, H-E1, H-G1) et de la lignée (cerveaux de frontière, test caché, concepteur) ; reclassé : programme de contrôle en v1 du document")
P("N-045v2.9", CA, "T", _f("N-045-v2", "Noyau (étape 2 et après ; à coder par « session-depot »", "le juge consigne le coût de la génération par espèce et par rôle",
                           "les instruments entraînés sont servis comme espèces LOCAL:<identifiant>"), "retenu (conséquence)")
P("N-045v2.10", CA, "T", _f("N-045-v2", "Préenregistrements (étape 2 et suivants) : forme du score net et λ gelés ; lecture à deux axes ; ablation « sans frontière » rapportée"),
  "retenu (conséquence)")
P("N-045v2.11", PC, "T", _f("N-045-v2", "cette note en fixe la lecture jusqu'à une version nouvelle, comme N-044"), "retenu (conséquence)")
P("N-045v2.12", CA, "T", _f("N-045-v2", "sur les concepteurs entraînés (multi-tour, mémoire, familles tenues à l'écart) est lancée ; aucune revendication avant",
                            "la valeur de λ ; la forme exacte de la récompense d'héritage (K, actualisation) ; la réponse au tour v4 (format)"),
  "borne mixte : points reportés ; une règle décidée (recherche bibliographique avant toute revendication)", "",
  "mots de Lazar, lignes 40-41 : « go » sur la recherche bibliographique obligatoire avant de revendiquer")
# ---- N-049, N-050
P("N-049.1", CA, "T", _f("N-049", "pour les pilotes de conception à partir du pilote 5, le noyau sert à chaque génération une part test tirée"))
P("N-049.2", CA, "T", _f("N-049", "même générateur que la banque v3, tâches neuves, identifiants disjoints de v3 et de v6"))
P("N-049.3", CA, "T", _f("N-049", "la confirmation (étape 1 décisive, confrontation, pilote décisif (b)) sur la banque v6 scellée, une famille tenue à l'écart"), "retenu (invariant)")
P("N-050.1", CA, "T", _f("N-050", "À la fin de chaque course d'un pilote de conception"))
P("N-050.2", CA, "T", _f("N-050", "Ce n'est pas un écart au texte du pilote 4"))
P("N-050.3", CA, "T", _f("N-050", "Conséquence pour le registre d'hypothèses de la boucle extérieure"))
# ---- N-052
P("N-052.0", CA, "T", _f("N-052", "(faute de frappe). Dans l'ordre de la proposition :"), "retenu (amorce : la lecture retenue elle-même)")
P("N-052.1", CA, "T", _f("N-052", "l'analyste de chaque course, le correcteur, et l'agent qui lit un dossier d'audit"))
P("N-052.2", CA, "T", _f("N-052", "le contre-lecteur (parties A et B) et tout agent d'audit chargé d'attaquer un verdict (protocole de la boucle, § 12.3)"))
P("N-052.3", CA, "T", _f("N-052", "Le paramètre « famille » du protocole prend la valeur"))
P("N-052.4", CA, "T", _f("N-052", "conv-audit le consigne au journal et le dit à Lazar"))
# ---- N-058 : l'organisme d'idéation par inférence (aucune phrase ne l'écrit) ; N-058.3 = ordre entre lignées
P("N-058.1", OI_I, "I", _f("N-058", "l'oracle du monde planté (structures retrouvées, témoins plantés vrais promus et faux rejetés)",
                           "Le verdict du juge sur les fiches reste aveugle à l'identité du proposeur"),
  "retenu", "", "chaîne I1 du document, § 1")
P("N-058.2", OI_I, "I", _f("N-058", "classer les proposeurs par les fiches que le juge promeut, c'est sélectionner un agent sur le verdict du juge",
                           "aucun score de moniteur ni de juge n'entre dans un signal d'entraînement ou de sélection de l'agent"),
  "retenu", "", "chaîne I1 du document, § 1")
P("N-058.3", COORD, "T", _f("N-058", "L'ordre de travail de conv-audit : la version 32 de l'orchestrateur (prise « idéation », corrections CL31-01 à 10 de la contre-lecture R2) d'abord",
                            "d'abord, puis les sept demandes de dimensionnement de la couche 2"),
  "retenu", "", "ordre de travail entre lignées : aucune règle sur l'un ou l'autre organisme ; reclassé : « les deux » en v1 du document")
P("N-058.4", OI_I, "I", _f("N-058", "Le duel n'est pas relancé par cette inscription : sa relance exige le critère réécrit au devis (conv-audit), la plomberie démontrée"),
  "borne : relance du duel soumise à trois conditions", "", "chaîne I1")
P("N-058.5", OI_I, "I", _f("N-058", "Rien ne change pour le juge des fiches lui-même", "l'interdit porte sur la sélection d'agents, pas sur celle des fiches"),
  "borne : borne la portée de N-058.2", "", "chaîne I1")
# ---- N-059
P("N-059.0", ETAB, "A", _f("N-059", "recommandations de la conception de l'affinage v2", "sont retenues"),
  "retenu (amorce : désigne le document dont dépend la portée)", "3a",
  "document désigné par chemin et empreinte, section 10.2 ; non lu par l'auteur de ce document (hors de la liste de lecture)")
_ar = "recommandations de la conception de l'affinage v2"
P("N-059.1", OI_I, "I", _f("N-059", "générations d'étalonnage entières, à calendrier secret, et témoins silencieux à chaque génération de production ; aucun témoin ne passe par un proposeur en production",
                           "le duel se tient en générations d'étalonnage (mondes plantés seulement)"), "retenu", "3b", "objets nommés : proposeur en production, génération d'étalonnage ; chaîne I1 et lien par le point 5")
P("N-059.2", ETAB, "A", _f("N-059", _ar, "un budget par génération, réparti entre les configurations enregistrées"), "retenu, détail à fixer (procédure avec un statisticien, sur devis)", "3a")
P("N-059.3", ETAB, "A", _f("N-059", _ar, "retirée de cette course"), "retenu", "3a")
P("N-059.4", ETAB, "A", _f("N-059", _ar, "Troisième famille de modèles pour le détecteur d'injection et la revue des extensions"), "retenu, détail à fixer (choix et dépense sur devis)", "3a")
P("N-059.5", OI_I, "I", _f("N-059", "le duel se tient en générations d'étalonnage (mondes plantés seulement)", "déjà fixés par N-058"), "retenu", "",
  "jumelé avec .6 (même texte) ; objet par le point sur N-058")
P("N-059.6", OI_I, "I", _f("N-059", "le duel se tient en générations d'étalonnage (mondes plantés seulement)", "déjà fixés par N-058"), "retenu", "",
  "jumelé avec .5 (même texte)")
P("N-059.7", ETAB, "A", _f("N-059", _ar, "La banque de familles inédites qui sert à confirmer est distincte de la famille tenue à l'écart de l'évaluation finale")
  + _f("N-065", "la réserver comme famille tenue à l'écart pour mesurer l'universalité (N-044, N-054)"), "retenu", "3a",
  "indice : vocabulaire de N-044 et N-049.3 (familles inédites, famille tenue à l'écart)")
P("N-059.8", ETAB, "A", _f("N-059", _ar, "admise, avec un plafond (à fixer en v3)"), "retenu, détail à fixer (plafond en v3)", "3a")
P("N-059.9", ETAB, "A", _f("N-059", _ar, "lots en phase de proposition, puis affineur isolé par fiche"), "retenu", "3a",
  "indice : « fiche » (N-058 l. 22 et 38, N-065.2 « ses fiches »)")
P("N-059.10", ETAB, "A", _f("N-059", _ar, "plafond petit, fixé fiche par fiche à une porte, sous revue externe"), "retenu", "3a",
  "indice : « fiche »")
P("N-059.11", OI_I, "I", _f("N-059", "l'épreuve est lue jusqu'au budget, partout, dès maintenant", "le seuil de réfutation est fixé par la course, jamais par le proposeur"),
  "retenu", "3b", "inférence plus faible : « le juge » existe aussi dans la lignée (« juge externe », N-045v2.2)")
P("N-059.12", GOUV, "A", _f("N-059", "est ratifiée comme son dépôt de travail ; aucune fusion avant la contre-lecture de la version concernée"), "retenu", "3c")
P("N-059.13", GOUV, "A", _f("N-059", "a été confirmée par Lazar lui-même : l'écart est ratifié"), "retenu", "3c")
P("N-059.14", OI_I, "I", _f("N-059", "les taux par proposeur entre deux courses ne sont lus que par le directeur ; un changement de composition se fonde sur l'étalonnage seul"),
  "retenu", "3b", "objets nommés : proposeur, composition ; chaîne I1 (N-058.1 : composition des proposeurs)")
P("N-059.15", MIXTE, "A", _f("N-059", "Les trois rapports de la v2 sont ajoutés au dépôt de la session", "avant le codage du juge et de la mémoire"),
  "retenu", "3b et 3c", "première moitié : gouvernance du dépôt ; seconde moitié : juge et mémoire (inférence faible)")
# ---- N-065
P("N-065.1", OI_T, "T", _f("N-065", "l'organisme d'idéation est un second terrain du papier C"))
P("N-065.2", OI_T, "T", _f("N-065", "l'organisme est un atelier d'idées du programme", "Il reçoit des questions ouvertes du programme ; ses fiches sont du matériau, jamais une preuve"),
  "retenu", "2")
P("N-065.3", OI_T, "T", _f("N-065", "faire d'un proposeur à poids ouverts qui trompe le juge une famille de menaces diffuses pour les papiers A et B", "Rôle 3, à trancher"),
  "à trancher (mot de Lazar : « rôle 3 à trancher »)", "", "reclassé : programme de contrôle en v1 du document ; la décision est titrée « place de l'organisme d'idéation »")
P("N-065.4", OI_T, "T", _f("N-065", "aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme (N-053)",
                           "citations obligatoires de N-064 dans tout texte qui présente l'organisme"))
P("N-065.5", MIXTE, "A", _f("N-065", "R1 à R14 ; les hypothèses et les portes du programme ; les revendications O1 à O20 de l'organisme dans l'état fixé par N-064"),
  "retenu (invariants)", "", "invariants du programme (R1 à R14, hypothèses, portes) et de l'organisme d'idéation (O1 à O20)")

RE_NUM = re.compile(r"^(\d+)\.\s+(?:et\s+(\d+)\.\s+)?")

def nature(titre):
    if titre.startswith(("Ce que cela ne décide pas", "Ce que la décision ne fixe pas", "Ce qui ne change pas")):
        return "borne"
    if titre.startswith("Ce que cela change"):
        return "conséquence"
    return "dispositif"

def sections(lignes, cle):
    """Liste de (titre, indice de première ligne de contenu, indice de fin exclue) des sections d'articles."""
    deb, fin = 0, len(lignes)
    if cle in FENETRES:
        d, f = FENETRES[cle]
        deb = next(k for k, l in enumerate(lignes) if l.startswith(d))
        if f is not None:
            fin = next(k for k in range(deb + 1, len(lignes)) if lignes[k].startswith(f))
    res, cur = [], None
    for k in range(deb, fin):
        l = lignes[k]
        if l.startswith("## "):
            if cur is not None and cur[2] is None and k == cur[3]:   # ligne de titre qui continue la précédente
                cur[3] = k + 1
                cur[0] += " " + l[3:]
                cur[1] = k + 1
                continue
            if cur is not None and cur[2] is None:
                cur[2] = k
            cur = [l[3:], k + 1, None, k + 1]
            res.append(cur)
        elif l.startswith("# "):
            if cur is not None and cur[2] is None:
                cur[2] = k
            cur = None
    for s in res:
        if s[2] is None:
            s[2] = fin
    return [(t, a, b) for t, a, b, _ in res if not t.startswith(SECTIONS_EXCLUES)]

def decouper(lignes, cle):
    unites = []
    for titre, a, b in sections(lignes, cle):
        cur = None
        def clore():
            nonlocal cur
            if cur is not None:
                unites.append(cur)
                cur = None
        for k in range(a, b):
            l = lignes[k].rstrip("\n")
            if not l.strip():
                clore(); continue
            if l.strip() == "---":
                clore(); continue
            m = RE_NUM.match(l)
            if m:
                clore()
                nums = [int(m.group(1))] + ([int(m.group(2))] if m.group(2) else [])
                cur = {"type": "numero", "nums": nums, "debut": k + 1, "fin": k + 1, "lignes": [l], "section": titre}
            elif l.startswith("- "):
                clore()
                cur = {"type": "puce", "nums": [], "debut": k + 1, "fin": k + 1, "lignes": [l], "section": titre}
            elif cur is not None:
                cur["lignes"].append(l); cur["fin"] = k + 1
            else:
                cur = {"type": "paragraphe", "nums": [], "debut": k + 1, "fin": k + 1, "lignes": [l], "section": titre}
        clore()
    return unites

def articles_de(cle, prefixe, lignes):
    out, rang = [], 0
    for u in decouper(lignes, cle):
        txt = "\n".join(u["lignes"])
        typ = u["type"]
        if typ == "paragraphe":
            plat = " ".join(txt.split())
            if plat.startswith("Numéro"):
                continue
            if plat.endswith(":"):
                typ = "amorce"
        nb = len(u["nums"]) if typ == "numero" else 1
        for q in range(nb):
            if typ == "amorce":
                ident = "%s.0" % prefixe
            else:
                rang += 1
                ident = "%s.%d" % (prefixe, rang)
            out.append({"decision": cle, "identifiant": ident, "type": typ, "jumele": nb > 1,
                        "section": " ".join(u["section"].split()), "nature": nature(u["section"]),
                        "ligne": u["debut"], "ligne_fin": u["fin"], "texte_brut": txt})
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=RACINE_DEFAUT)
    ap.add_argument("--sortie", default=SORTIE_DEFAUT)
    ap.add_argument("--table", action="store_true", help="imprime les lignes de la table markdown")
    ap.add_argument("--totaux", action="store_true", help="imprime le tableau des totaux")
    ap.add_argument("--verifier-md", default=None)
    a = ap.parse_args()
    erreurs, sources, textes, arts = [], {}, {}, []
    for cle, rel, pref, idp in FICHIERS:
        ch = os.path.join(a.racine, rel)
        data = open(ch, "rb").read()
        h = hashlib.sha256(data).hexdigest()
        comp = open(ch + ".sha256").read().split()[0]
        if not h.startswith(pref) or h != comp:
            erreurs.append("empreinte %s : calculée %s, attendue %s…, compagnon %s" % (rel, h, pref, comp))
        t = data.decode("utf-8")
        lignes = t.split("\n")
        sources[cle] = {"chemin": rel, "sha256": h, "nombre_de_lignes": len(lignes) - (1 if lignes[-1] == "" else 0)}
        textes[cle] = norm(t)
        arts.extend(articles_de(cle, idp, lignes))
    ids = [x["identifiant"] for x in arts]
    if len(set(ids)) != len(ids):
        erreurs.append("identifiants en double")
    if set(ids) != set(PORTEE):
        erreurs.append("articles sans portée : %s ; portées sans article : %s" % (sorted(set(ids) - set(PORTEE)), sorted(set(PORTEE) - set(ids))))
    for i, d in PORTEE.items():
        if d["objet"] not in OBJETS:
            erreurs.append("objet inconnu pour %s" % i)
        for k, ph in d["fond"]:
            if norm(ph) not in textes[k]:
                erreurs.append("fondement introuvable dans %s pour %s : %s" % (k, i, ph))
    if erreurs:
        for e in erreurs:
            print("ERREUR", e, file=sys.stderr)
        sys.exit(2)
    out = []
    for x in arts:
        d = PORTEE[x["identifiant"]]
        txt, n = masquer(x.pop("texte_brut"))
        fm = [{"decision": k, "phrase": masquer(ph)[0]} for k, ph in d["fond"]]
        x.update({"texte": txt, "masque_applique": n > 0, "objet": d["objet"], "base": d["base"], "fondement": fm,
                  "statut": d["statut"], "noeud": d["noeud"], "note": masquer(d["note"])[0]})
        out.append(x)
    totaux = {}
    for x in out:
        totaux[x["decision"]] = totaux.get(x["decision"], 0) + 1
    def corps(x):
        return norm(re.sub(r"^\d+\.\s+", "", x["texte"].replace("\n", " ")))
    v1 = [x for x in out if x["decision"] == "N-045-v1"]
    v2 = [x for x in out if x["decision"] == "N-045-v2"]
    diff = {"identiques": [], "nouveaux_dans_v2": [], "absents_de_v2": []}
    for x in v1:
        c = next((y for y in v2 if corps(y) == corps(x)), None)
        if c:
            diff["identiques"].append([x["identifiant"], c["identifiant"]])
        else:
            diff["absents_de_v2"].append(x["identifiant"])
    pris = {p[1] for p in diff["identiques"]}
    diff["nouveaux_dans_v2"] = [y["identifiant"] for y in v2 if y["identifiant"] not in pris]
    vig = [x for x in out if x["decision"] != "N-045-v1"]
    par_objet = {o: sum(1 for x in vig if x["objet"] == o) for o in OBJETS}
    res = {"programme": "compter_articles_decisions_v2.py", "lecteur": "modèle C",
           "regle": __doc__.split("RÈGLE DE DÉCOUPAGE v2")[1].split("LE CLASSEMENT N'EST PAS DÉDUIT")[0].strip(),
           "sources": sources, "totaux_par_decision": totaux, "total_general": sum(totaux.values()),
           "total_en_vigueur_hors_N-045-v1": len(vig), "en_vigueur_par_objet": par_objet,
           "diff_N-045_v1_v2": diff, "articles": out}
    if a.table:
        for x in out:
            fl = " ; ".join(("« %s »" if f["decision"] == x["decision"] else "[" + f["decision"] + "] « %s »") % f["phrase"] for f in x["fondement"])
            print("| %s | %d-%d | %s | %s | %s | %s | %s | %s |" % (x["identifiant"], x["ligne"], x["ligne_fin"], x["nature"], x["objet"], x["base"],
                                                                x["statut"], x["noeud"] or "—", fl.replace("|", "/")))
    if a.totaux:
        decs = [c[0] for c in FICHIERS]
        noms = {"N-045-v1": "N-045 v1 (remplacée)", "N-045-v2": "N-045 v2"}
        print("| décision | articles | " + " | ".join(OBJETS) + " |")
        print("|---|---|" + "---|" * len(OBJETS))
        for c in decs:
            xs = [x for x in out if x["decision"] == c]
            print("| %s | %d | " % (noms.get(c, c), len(xs)) + " | ".join(str(sum(1 for x in xs if x["objet"] == o)) for o in OBJETS) + " |")
        print("| **Total** | **%d** | " % len(out) + " | ".join("**%d**" % sum(1 for x in out if x["objet"] == o) for o in OBJETS) + " |")
        print("| **En vigueur (sans N-045 v1)** | **%d** | " % len(vig) + " | ".join("**%d**" % par_objet[o] for o in OBJETS) + " |")
    if a.verifier_md:
        md = open(a.verifier_md, encoding="utf-8").read()
        manque = [i for i in ids if ("| %s |" % i) not in md]
        dbl = [i for i in ids if md.count("| %s |" % i) != 1]
        print("md : identifiants manquants", manque, "; non uniques", dbl)
        if manque or dbl:
            sys.exit(3)
    dest = os.path.join(a.sortie, "articles-decisions-v2.json")
    if not (a.table or a.totaux or a.verifier_md):
        os.makedirs(a.sortie, exist_ok=True)
        with open(dest, "x", encoding="utf-8") as f:   # création seulement
            json.dump(res, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("écrit", dest)
    print("totaux", json.dumps(totaux, ensure_ascii=False), "total", res["total_general"], "en vigueur", res["total_en_vigueur_hors_N-045-v1"], file=sys.stderr)
    print("par objet (en vigueur)", json.dumps(par_objet, ensure_ascii=False), file=sys.stderr)
    print("diff N-045", json.dumps(diff, ensure_ascii=False), file=sys.stderr)

if __name__ == "__main__":
    main()
