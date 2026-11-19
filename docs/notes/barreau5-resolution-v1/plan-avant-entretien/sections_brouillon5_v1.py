# -*- coding: utf-8 -*-
"""Barreau 5 : écritures du rédacteur (Claude Fable 5.2) pour le brouillon 5, employées par `fabrique-brouillon5-v1.py`.

Deux sortes seulement, appliquées après les 20 couples de la vérification du brouillon 4 :
  « mots de Lazar » : les décisions GO-2026-11-19-86 à -88 écrites comme décidées ;
  « tenue du brouillon » : titre, statut, filiation, renvois, état de la vérification.
Rien d'autre n'est changé. Aucune donnée du programme.
"""
GO86, GO87, GO88 = "`GO-2026-11-19-86`", "`GO-2026-11-19-87`", "`GO-2026-11-19-88`"

CHANGE_B5 = (
    "**Ce qui change au brouillon 5.** Rien dans la construction. (1) Les 20 couples de la vérification du brouillon 4 (verdict : « scellable après ces couples », aucun constat bloquant) sont appliqués à la lettre. Ses deux constats majeurs portent sur la lecture : l'étalon de la poussée est fragile là où il porte tout, et la phrase, la table des rivales et les taux d'erreur le taisaient ; ils le disent maintenant partout où le mot ou ses taux sont dits. (2) Les mots de Lazar du 19 novembre au soir (" + GO86 + " à `-88`) sont écrits comme décidés : accord de calcul sous un plafond commun de 200 USD ; enveloppe de relance de 56 USD, à part ; aucun comptage d'avance ; répétition générale sur les quatre adaptateurs existants si le code de lecture est prêt, sinon sur le modèle jouet ; garde des activations sur un volume de 200 Go, prix porté à Lazar avant toute dépense, replis écrits sinon ; témoin à changement bénin après l'entretien ; niveau déclaré de 95 % sous huit familles. (3) Les marques « [à confirmer par le rapport v4] » restent : le rapport v4 du développeur n'était pas scellé à l'écriture ; elles se lèvent par un erratum.\n\n"
    "## Ce que le rédacteur savait avant d'écrire (exposition, ligne par ligne)")

ETAT_NOEUDS = (
    "**État au brouillon 5 : tous les nœuds qui précèdent le départ sont tranchés.** Lignes de `registres/go.md`, relues par moi. `GO-2026-11-19-79` et `-82` : le plan (nœud 1) ; 39 adaptateurs ; la voie (iii) ; un départ au plus tôt. " + GO86 + " : accord de calcul de la formation, répétition générale comprise, sous un plafond commun de 200 USD, aux coupures du devis scellé ; il ne vaut qu'après les lignes `SCELLEMENT-B5F` et `CODE-FORMATION-B5F`, et si le devis scellé ne dépasse ni l'attendu (88 à 132 USD) ni ce plafond ; sinon retour à Lazar (nœud 2). " + GO87 + " : enveloppe de relance, à part de ce plafond, 56 USD au plus, pour deux instances tombées au plus, une fois chacune, au sens de ce texte. " + GO88 + " : aucun comptage d'avance dans des textes déjà produits ; répétition générale et points d'ancrage sur les quatre adaptateurs existants si le code de lecture est prêt à temps, sinon répétition sur le modèle jouet (nœud 3) ; garde des activations sur un volume de 200 Go, accord de principe, le prix étant relevé et porté à Lazar avant toute dépense, sinon les replis de « Données gardées » (nœud 4) ; témoin à changement bénin après l'entretien (nœud 5) ; sous huit familles présentes, issue au niveau déclaré de 95 % (nœud 6). Nœud 7 : l'écart au gabarit est celui que décrit l'en-tête. Reste le nœud 8, après le verdict.\n\n")

VERIF_B4 = (
    "**Vérification du brouillon 4**, par le même contre-lecteur (Claude Opus 5.5). Brouillon relu : le brouillon 4, empreinte `dbe66dc99332a1c40cbc6f6bceee7f9c7c49c741f0e99feaa7f7949609109256`. Rapport : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/verification-plan-brouillon4-v1.md`, empreinte `a091eed230a10ddd3566187e213a736f764e04d105a58d0ef62f91f6ba1a9df4`. Verdict : « scellable après ces couples », aucun constat bloquant, deux majeurs sur la lecture (W-M1, W-M2), quatre mineurs, 20 couples exacts.\n\n"
    "Traitement (le détail est dans `table-corrections-plan-brouillon5-v1.md`) :\n"
    "- **Les 20 couples sont appliqués à la lettre**, par programme, chaque « avant » trouvé une fois : treize au texte, cinq au devis, deux à la fiche.\n"
    "- **W-M1 et W-M2, acceptés** : l'hypothèse de l'étalon est étendue à ce qui se projette sur le déplacement du saboteur ; sa fragilité est chiffrée ; une ligne « ouverte » de plus à la table des rivales ; la phrase « sabotage », le seuil, la puissance et l'en-tête la disent.\n"
    "- Aucune remarque refusée. Aucune autre phrase n'est changée, hors les mots de Lazar écrits comme décidés et la tenue du brouillon (titre, statut, renvois).\n\n"
    "**Vérification du différentiel du brouillon 5 : en attente**, par le même contre-lecteur. Puis scellement sous le nom définitif, après la levée des marques « [à confirmer par le rapport v4] ».\n\n")

STATUT = (
    "- Statut : **brouillon 5, en attente de la vérification de son différentiel par le même contre-lecteur, non scellable sous ce nom** (scellé comme brouillon, pour fixer ce qui a été écrit). Il part du brouillon 4 (`dbe66dc99332a1c40cbc6f6bceee7f9c7c49c741f0e99feaa7f7949609109256`) et de sa vérification (`a091eed230a10ddd3566187e213a736f764e04d105a58d0ef62f91f6ba1a9df4`, verdict « scellable après ces couples »). Il n'en diffère que par les 20 couples de cette vérification, appliqués à la lettre, par les mots de Lazar écrits comme décidés, et par la tenue du brouillon. Les brouillons précédents : brouillon 3 (`525f338e7899e6a8f57b73fffef7f0eeef3d6a16eee0e7d6c2823cddb44c9e50`) et sa vérification (`a1b2250de628f90fb28253ded8e12ae6be88678f4915cced28c979197c02d19b`, constat bloquant V-B1), fiche de décision `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-decision-v-b1-lazar-v1.md` (`78cadfd2…`), couples du code (`couples-du-code-pour-brouillon4-v1.md`, `1e929542…`), vérification des corrections du code (`code-formation/verification-corrections-code-formation-v1.md`, `3517677f…`). **Le texte scellé portera le nom `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`** : le code de formation refuse un nom qui contient « brouillon ». Table des changements : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/table-corrections-plan-brouillon5-v1.md` (brouillon 4 : `table-corrections-plan-brouillon4-v1.md`). Les phrases marquées « [à confirmer par le rapport v4] » supposent un comportement du code que je n'ai pas pu lire dans un rapport scellé ; elles se lèvent par un erratum. Rien lancé sur carte, rien dépensé, rien commis.")

# (nom, sorte, avant, après) — chaque « avant » doit se trouver une fois, après les 20 couples
RETOUCHES_TEXTE = [
    ("titre", "tenue", "— v1 — brouillon 4", "— v1 — brouillon 5"),
    ("date", "tenue", "brouillon 4 de 21:50 à la nuit", "brouillon 4 de 21:50 à 22:12, brouillon 5 à partir de 22:50"),
    ("ce-qui-change", "tenue", "## Ce que le rédacteur savait avant d'écrire (exposition, ligne par ligne)", CHANGE_B5),
    ("calendrier-avant-depart", "tenue", "vérification du brouillon 4 par le même contre-lecteur ; corrections ; réponses de Lazar (plafond, enveloppe de relance)",
     "vérification du brouillon 4 (rendue dans la nuit : « scellable après ces couples ») ; brouillon 5 ; vérification de son différentiel ; levée des marques sur le rapport v4 du développeur"),
    ("calendrier-risque", "tenue",
     "- La vérification de ce brouillon : elle porte une construction neuve des épreuves. Un second « à reprendre » retarde le scellement, donc le départ, même si les sections dont dépend la formation ne sont pas en cause : le code exige le texte entier scellé.",
     "- La vérification du différentiel de ce brouillon, et la levée des marques « [à confirmer par le rapport v4] » : le code exige le texte entier scellé. La construction des épreuves, elle, est vérifiée (brouillon 4 : « scellable après ces couples »)."),
    ("contre-lecture", "tenue", "**Vérification du brouillon 4 : en attente**", VERIF_B4 + "**Demandé à la vérification du brouillon 4 (pour mémoire)**"),
    ("marqueur-M10", "tenue", "M-10 : vérification du brouillon 4 par le même contre-lecteur ;",
     "M-10 : fait (vérification du brouillon 4 rendue, « scellable après ces couples ») ; reste la vérification du différentiel du brouillon 5 ;"),
    ("depense", "lazar", "plafond demandé 200 (205 si Lazar le dit : le texte tient sous l'un ou l'autre, le plafond est celui de la ligne d'accord) ; à part, et seulement sur un mot de Lazar, une enveloppe de relance de 56 USD au plus.",
     "plafond commun de 200 USD (accord de calcul " + GO86 + ") ; à part, une enveloppe de relance de 56 USD au plus (" + GO87 + ")."),
    ("borne-relance", "lazar",
     "L'enveloppe n'est ouverte que par un mot de Lazar, donné d'avance sous la condition « instance tombée au sens de ce texte », ou le jour même ; sans ce mot, aucune relance, et la règle du paragraphe précédent s'applique comme si la ligne manquait.",
     "L'enveloppe est ouverte d'avance par Lazar (" + GO87 + " : 56 USD au plus, pour deux instances tombées au plus, une fois chacune, au sens de ce texte) ; chaque relance porte la ligne `GO-RELANCE-FORMATION-B5F`, qui cite cet accord."),
    ("point-18-accord", "lazar", "(sous nœud 3).** Si Lazar l'accorde :",
     "(nœud 3, tranché : " + GO88 + ").** Accordés si le code de lecture est prêt à temps, c'est-à-dire si la ligne `CODE-LECTURE-B5F` est inscrite à la fin de la formation (règle mécanique du calendrier) :"),
    ("point-18-sinon", "lazar", "Sans accord : la répétition se fait sur le modèle jouet.",
     "Sinon : la répétition se fait sur le modèle jouet, et aucun point d'ancrage n'est lu."),
    ("garde-activations", "lazar", "Lieu de dépôt : nœud 4 (volume de stockage du projet).",
     "Lieu de dépôt : un volume de stockage de 200 Go (nœud 4, accord de principe : " + GO88 + " ; le prix est relevé et porté à Lazar avant toute dépense)."),
    ("niveau-sous-huit", "lazar", "(nœud 6, règle recommandée, tenue par défaut)", "(nœud 6, tranché : " + GO88 + ")"),
    ("marqueur-M3", "lazar", "M-3 : empreinte du devis scellé et ligne d'accord ;",
     "M-3 : empreinte du devis scellé ; l'accord de calcul est donné (" + GO86 + "), sous condition que le devis scellé ne dépasse ni l'attendu de 88 à 132 USD ni le plafond de 200 ;"),
]
PARTOUT_TEXTE = [("renvoi-devis", "tenue", "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md", "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md", 2)]
LIGNES_TEXTE = [
    ("statut", "tenue", "- Statut :", STATUT, False),
    ("decisions", "lazar", "- Décisions du 19 novembre au soir",
     "- Décisions du 19 novembre, vers 22:42Z, lignes " + GO86 + ", " + GO87 + " et " + GO88 + " de `registres/go.md` (relues) : accord de calcul de la formation sous un plafond commun de 200 USD ; enveloppe de relance de 56 USD, à part ; les autres recommandations de la fiche v4 (détail dans « Nœuds »).", True),
    ("documents", "tenue", "  - vérification du brouillon 3 et ses outils",
     "  - vérification du brouillon 4 et ses outils (mondes inventés) : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/verification-plan-brouillon4-v1.md`, `a091eed2…` ; `outils-verification-plan-brouillon4-v1/couples-verification-brouillon4-v1.py` (20 couples), `simulation-verification-brouillon4-v1.py` et `controle-precision-verification-brouillon4-v1.py` avec leurs sorties (empreintes dans leurs compagnons) : ce sont eux que citent les phrases « vérification du brouillon 4 » ;", True),
]
BLOCS_TEXTE = [("etat-des-noeuds", "lazar", "**État au brouillon 4.**", "1. **Le plan**", ETAT_NOEUDS)]

RETOUCHES_DEVIS = [
    ("devis-titre", "tenue", "— v1 — brouillon 4\n", "— v1 — brouillon 5\n"),
    ("devis-texte-chiffre", "tenue",
     "- Texte qu'il chiffre : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`,",
     "- **Brouillon 5** (nuit du 19 au 20 novembre) : le brouillon 4 (`084cd547…`), avec les cinq couples de sa vérification (`verification-plan-brouillon4-v1.md`, `a091eed2…` : « scellable après ces couples »), appliqués à la lettre, et les mots de Lazar écrits comme décidés (" + GO86 + " à `-88`). Aucun chiffre ne change. Il attend la vérification de son différentiel.\n"
     "- Texte qu'il chiffre : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md`,"),
    ("devis-plafond", "lazar", "**Plafond** : 200 USD demandés ; Lazar peut dire 205 ; le devis tient sous l'un ou l'autre.",
     "**Plafond** : 200 USD, plafond commun (accord de calcul " + GO86 + " ; il ne vaut qu'après les lignes `SCELLEMENT-B5F` et `CODE-FORMATION-B5F`, et si le devis scellé ne dépasse ni l'attendu de 88 à 132 USD ni ce plafond)."),
    ("devis-ensemble", "lazar", "**204 ; plafond demandé : 200 (", "**204 ; plafond commun : 200 ("),
    ("devis-enveloppe", "lazar", "L'enveloppe n'est ouverte que par un mot de Lazar, donné d'avance ou le jour même ; sans ce mot, aucune relance.",
     "L'enveloppe est ouverte d'avance par Lazar (" + GO87 + " : 56 USD au plus, pour deux instances tombées au plus, une fois chacune) ; chaque relance porte la ligne `GO-RELANCE-FORMATION-B5F`, qui cite cet accord."),
    ("devis-repetition", "lazar", "| répétition générale (si accordée) |",
     "| répétition générale (accordée si le code de lecture est prêt à temps, " + GO88 + " ; sinon sur le modèle jouet, sans dépense) |"),
    ("devis-volume", "lazar", "C'est une ressource payante neuve : nœud 4 du texte ;",
     "C'est une ressource payante neuve : accord de principe de Lazar (" + GO88 + "), le prix étant relevé et porté à Lazar avant toute dépense ; sinon les replis (b), puis (c) ;"),
    ("devis-recharge", "lazar", "si Lazar ouvre d'avance l'enveloppe de relance (56 USD au plus), la recharge la compte : 236 USD,",
     "l'enveloppe de relance étant ouverte (" + GO87 + ", 56 USD au plus), la recharge la compte : 236 USD,"),
]

RETOUCHES_FICHE = [
    ("fiche-titre", "tenue", "(fiche v4)", "(fiche v5)"),
    ("fiche-etat", "lazar", "## Où en est le texte\n",
     "**Fiche v5** : la fiche v4 (`a88a3a12…`), avec les deux couples de la vérification du brouillon 4, pour mémoire. Les huit décisions du tableau sont prises (" + GO86 + " à `-88`, 19 novembre vers 22:42Z), toutes selon la recommandation ; le texte et le devis du brouillon 5 les écrivent comme décidées.\n\n"
     "## Où en est le texte\n"),
]
