#!/usr/bin/env python3
"""Assemble le brouillon 6 de la v11 à partir du brouillon 5.

Objet, sur le message de la session de l'organisme du 23 novembre 2026 daté 05:45Z (décisions de la session, étage 1, à
inscrire par la mère avec R-5130) : la mesure préalable de la réflexion d'Argon (GO-2026-11-22-128), si Lazar la confirme,
compte un appel de proposeur puis quatre appels de juge, aux arguments exacts du gabarit de la course, sur des pièces choisies
par une règle de rang ; un statut 429 ou de 500 et plus se rejoue au plus deux fois par appel, dans la limite de la ligne ; le
seuil de la règle de lecture est 31 462 jetons, les autres postes à leur marge de 10 % ; la règle de lecture est retenue telle
quelle (sa clause de repli, devenue sans objet, est retirée) ; le champ inerte `relais_persistants_v4.plafond_relais_claude_usd`
est retiré de la configuration v11d ; devis v11e et programme de calcul de la mesure.
Les lignes 1 à 295 du brouillon 5 gardent leur numéro ; le point 16 du différentiel v10 → v11 (ligne 296) et la dernière
section (à retirer de la version scellée) sont récrits. Chaque remplacement exige que l'ancienne chaîne figure exactement une
fois dans la ligne visée ; sinon le programme s'arrête.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré dans le brouillon).
Usage : python3 -I assembler-brouillon-6-preenregistrement-v11.py BROUILLON-5.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B5_SHA = "3fd9267fd364a9e595d300061def1b858cd0c28a0af2ac4f84fe5cd3a66b0163"
DEVIS_V11C_SHA = "94f7f378c36e6af70a05166c9b26e9b012e9a44c7cd4df2ce059fa13a653bb2e"
DEVIS_V11D_SHA = "daf218f260f835a755db63cf1bc214c44a23dbe5880a23bb3d1520f98d5bad7d"
DEVIS_V11E_SHA = "c824fb2b4493f595dcdb2b05d01a3a72a75326deb540153033767ef6c313192b"
CALCUL_MESURE_SHA = "6416e1c56c2cde540221e3bd54f31e4fde81b4db9fdc1c7043c97fbec915dc04"
ANNEXE_SHA = "abb967a9e2190f0ca607e8f136e1527105137d42c8225ed8f30a8234f9096b95"
FICHES_V53 = "docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/fiches_v53.py"
FICHES_V53_SHA = "7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6"
N = "docs/notes/organisme-affinage-mentors-v1"
REF6 = "RÉFÉRENCE À INSCRIRE : ligne du registre des décisions où la mère les inscrit avec R-5130"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B5_SHA, "la source n'est pas le brouillon 5"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 331, len(L)   # 330 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
assert lignes[296].startswith("16. **Mesure préalable de la réflexion d'Argon**") and lignes[297] == ""
assert lignes[298].startswith("## Emplacements et points à trancher avant le scellement")
ligne_du_b1_au_b5 = lignes[330]
assert ligne_du_b1_au_b5.startswith("Du brouillon 1 au brouillon 2 :") and "Du brouillon 4 au brouillon 5" in ligne_du_b1_au_b5
touchees = set()


def sub(n, ancien, nouveau, fois=1):
    assert lignes[n].count(ancien) == fois, (n, ancien[:80], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


# ------------------------------------------------------------------------------------------------ en-tête
sub(3, "- **État de ce fichier : brouillon 5 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 4 (",
    "- **État de ce fichier : brouillon 6 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 5 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-5.md`, `" + B5_SHA + "`), le brouillon 4 (")
sub(3, "mesure préalable de la réflexion d'Argon dite dans ses deux cas, avec et sans ; devis v11d.",
    "mesure préalable de la réflexion d'Argon dite dans ses deux cas, avec et sans ; devis v11d. Objet du brouillon 6 : "
    "décisions de la session de l'organisme du 23 novembre, message daté 05:45Z (" + REF6 + ") — mesure préalable fixée (un "
    "appel de proposeur puis quatre de juge, pièces choisies par une règle de rang, reprises des statuts 429 et de 500 et "
    "plus au plus deux fois par appel, dans la limite de la ligne), seuil de sa règle de lecture à 31 462 jetons, champ "
    "inerte de la configuration v11d retiré ; devis v11e.")
sub(3, "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et une dernière section de points à trancher :",
    "Il porte des emplacements « EMPREINTE À INSCRIRE : <chemin> » et « RÉFÉRENCE À INSCRIRE », et une dernière section de "
    "points à trancher :")
sub(4, "à l'octet celles du travail interrompu, et R-5130.",
    "à l'octet celles du travail interrompu, et R-5130. Pour le brouillon 6, il a lu en plus la docstring de la commande en "
    "flux v2 scellée (compte d'un envoi échoué) et, la v54 épinglée de l'orchestrateur n'étant pas dans son conteneur, les "
    "fonctions de fiches de la v53 dans une copie versée et empreintée (`" + FICHES_V53 + "`, `" + FICHES_V53_SHA + "`, "
    "liste `empreintes-copie-v1.txt` de la copie, compagnon vérifié) : lecture des fiches d'une réponse, forme d'entrée du "
    "juge.")
sub(5, "- Date (UTC) de ce brouillon : 2026-11-23T05:40:12Z (`date -u +%FT%TZ`) ; brouillon 4 : 2026-11-23T05:22:30Z ;",
    "- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 5 : 2026-11-23T05:40:12Z ; brouillon 4 : "
    "2026-11-23T05:22:30Z ;")
sub(7, "chiffrée par le devis v11d", "chiffrée par le devis v11e")
sub(7, "(gabarit du relevé des crédits v11d), devis v11d, contre-lecteur",
    "(gabarit du relevé des crédits v11d), devis v11e, contre-lecteur")
sub(8, "où figure R-5130).",
    "où figure R-5130). **Brouillon 6** : décisions de la session de l'organisme du 23 novembre, message daté 05:45Z, étage 1 "
    "— seuil de la règle de lecture de la mesure préalable (31 462 jetons, la marge comprise), appels, pièces et reprises de "
    "la mesure, champ inerte de la configuration v11d retiré (" + REF6 + ").")

# ------------------------------------------------------------------------------------------------ pièces
sub(12, "et le champ inerte `relais_persistants_v4.plafond_relais_claude_usd`, 150 en v11c, passe à 45 ou est retiré, selon "
        "la session de l'organisme ; à constater sur la pièce scellée)",
    "et le champ inerte `relais_persistants_v4.plafond_relais_claude_usd`, 150 en v11c, est retiré (décision de la session "
    "de l'organisme, 05:45Z) ; à constater sur la pièce scellée)")
sub(12, "(`relais_persistants_v4`, dont le champ `plafond_relais_claude_usd` garde 150, et `carbon_v5`, qui décrit le lot)",
    "(`relais_persistants_v4`, dont le champ `plafond_relais_claude_usd` gardait 150 jusqu'à la v11c et est retiré en v11d, "
    "et `carbon_v5`, qui décrit le lot)")
sub(22, "  - **devis v11d** : `" + N + "/devis-course-affinage-mentors-v11d.md`, `" + DEVIS_V11D_SHA + "` — c'est le devis v11c (`"
        + N + "/devis-course-affinage-mentors-v11c.md`, `" + DEVIS_V11C_SHA + "`) sans aucun chiffre changé,",
    "  - **devis v11e** : `" + N + "/devis-course-affinage-mentors-v11e.md`, `" + DEVIS_V11E_SHA + "` — c'est le devis v11d (`"
    + N + "/devis-course-affinage-mentors-v11d.md`, `" + DEVIS_V11D_SHA + "`) plus la mesure préalable d'Argon fixée (un appel "
    "de proposeur et quatre de juge ; pire cas 4,58 USD sans reprise ; seuil 31 462 ; § 4), chiffrée par `" + N
    + "/course-v11/calcul-mesure-prealable-argon-v11e.py` (`" + CALCUL_MESURE_SHA + "`, 19 chiffres contrôlés, aucun écart) ; "
    "le devis v11d est le devis v11c (`" + N + "/devis-course-affinage-mentors-v11c.md`, `" + DEVIS_V11C_SHA + "`) sans aucun "
    "chiffre changé,")
sub(22, "dans ce texte, « devis v11 » désigne ce devis v11d ;", "dans ce texte, « devis v11 » désigne ce devis v11e ;")
sub(22, "(23 novembre, R-5130), à contre-lire ;", "(23 novembre, R-5130 et message daté 05:45Z), à contre-lire ;")

# ------------------------------------------------------------------------------------------------ mesure, liste d'arrêt
sub(80, "devis v11 (v11d ; estimation inchangée depuis le v11)", "devis v11 (v11e ; estimation inchangée depuis le v11)")
DEBUT_MESURE = "**Mesure préalable de la réflexion d'Argon** (GO-2026-11-22-128, au plus 10,50 USD, clé de Google,"
assert lignes[91].count(DEBUT_MESURE) == 1 and lignes[91].endswith("la session d'exécution la tient et la cite aux commandes exactes.")
MESURE = (
    "**Mesure préalable de la réflexion d'Argon** (GO-2026-11-22-128, au plus 10,50 USD, clé de Google, hors du plafond de la "
    "course ; nœud de dépense porté à Lazar par R-5130 ; rien ne part avant son mot) — deux cas, fixés ici avant toute mesure. "
    "**(a) Sans la mesure** (Lazar ne la confirme pas) : la course part sous les deux risques dits au § Espèces et au § Plafond "
    "— une réflexion moyenne d'Argon au-delà de 32 476 jetons par appel fait couper l'étape des juges ; la sortie maximale de "
    "45 056 jetons en flux n'a jamais été servie à Argon —, sans autre condition. **(b) Avec la mesure** (mot de Lazar) : elle "
    "est jouée après le scellement de ce texte et avant le départ, par la session d'exécution, par la commande en flux épinglée "
    "et un relais jeté, aux arguments exacts du gabarit de déclaration pour Argon (niveau `high`, provision 24 576, sortie "
    "maximale 45 056, en flux, prix 4 et 20 ; plafond de session de 3,00 USD pour l'appel de proposeur et de 1,00 USD pour "
    "chaque appel de juge, ceux de la course). **Appels et pièces, fixés ici** (décisions de la session de l'organisme, 05:45Z ; "
    "règle de choix par rang, aucun contenu lu) : d'abord **un appel de proposeur**, sur la case de rang 1 dans l'ordre du "
    "relevé (§ Ce qui est servi), dans la consigne de proposeur de la course que bâtit l'orchestrateur épinglé ; puis **quatre "
    "appels de juge** sur une même entrée : la première fiche, dans l'ordre de la liste que rend cet appel de proposeur, que "
    "l'orchestrateur épinglé accepte (champs obligatoires, garde A4), servie dans la consigne du juge de la course sous la forme "
    "d'entrée de l'orchestrateur épinglé, avec un identifiant opaque — avant la course, aucune autre fiche n'existe pour le "
    "juge. La fiche passe de la réponse du proposeur à l'entrée du juge par programme ; la mesure ne lit que des comptes "
    "(jetons d'entrée, de texte et de réflexion, raison de fin, statut), jamais un contenu ; son rapport est scellé et versé "
    "avant le départ. Pire cas compté par la commande : 4,58 USD sans reprise (devis v11, § 4). Un statut 429 ou de 500 et plus "
    "se rejoue au plus deux fois par appel ; aucun envoi ne part si le cumul compté de la mesure, plus le pire cas de cet envoi, "
    "passerait 10,50 USD (la commande compte un envoi échoué à son pire cas dès que la requête de génération est partie, sauf "
    "usage lu). **Règle de lecture, fixée ici** : le départ est refusé, et la course demande une version suivante et une "
    "décision nommée, si un appel mesuré est refusé par le fournisseur pour sa requête (statut 400 à 499 hors 429) ou rend un "
    "défaut au sens de la garde après la réponse (zéro jeton de pensée, fin autre que `STOP` — `MAX_TOKENS` compris —, texte "
    "vide), si la réflexion moyenne mesurée, pondérée comme dans la course (16 appels de proposeur pour 160 de juge : la "
    "réflexion de l'appel de proposeur au poids 1/11, la moyenne des quatre appels de juge au poids 10/11), passe **31 462 "
    "jetons** par appel (§ Plafond : le seuil où l'estimation atteint 150 USD, les autres postes à leur marge de 10 %), ou si "
    "la mesure reste inachevée (reprises épuisées, envoi arrêté par la limite de la ligne, ou aucune fiche acceptée dans la "
    "réponse du proposeur) ; sinon la course part sous ce texte, inchangé. La mesure porte sur cinq appels : elle tranche la "
    "faisabilité mieux qu'elle ne prédit la réflexion moyenne de la course, qui reste un risque dit. Le lanceur ne vérifie pas "
    "cette mesure : la session d'exécution la tient et la cite aux commandes exactes.")
lignes[91] = lignes[91][:lignes[91].index(DEBUT_MESURE)] + MESURE
touchees.add(91)

# ------------------------------------------------------------------------------------------------ plafond
sub(101, "**v11** : devis v11 (v11d, écrit pour cette version sur les décisions de la mère, R-5007, point (d), et R-5018, et "
         "sur celles de la session de l'organisme du 23 novembre, R-5130 ; à contre-lire).",
    "**v11** : devis v11 (v11e, écrit pour cette version sur les décisions de la mère, R-5007, point (d), et R-5018, et sur "
    "celles de la session de l'organisme du 23 novembre, R-5130 et message daté 05:45Z ; à contre-lire).")
sub(101, "ses deux cas, avec et sans, sont fixés à la liste d'arrêt, « Avant le départ, hors du lanceur » ; devis v11, § 4)",
    "ses deux cas, avec et sans, sont fixés à la liste d'arrêt, « Avant le départ, hors du lanceur », avec un seuil de lecture "
    "de 31 462 jetons, la marge comprise ; devis v11, § 4)")

# ------------------------------------------------------------------------------------------------ différentiel v10 → v11
sub(290, "10. **Devis v11d** (écrit pour cette version, à contre-lire ; le devis v11c, sans chiffre changé, avec R-5130, le "
         "lanceur v11d et la mesure préalable d'Argon dite avec et sans ;",
    "10. **Devis v11e** (écrit pour cette version, à contre-lire ; le devis v11d plus la mesure préalable d'Argon fixée, 4,58 "
    "USD au pire sans reprise ; le devis v11d est le devis v11c, sans chiffre changé, avec R-5130, le lanceur v11d et la mesure "
    "préalable d'Argon dite avec et sans ;")
sub(294, "; les configurations v11, v11b et v11c, au GO de la course et aux notes près (pièces).",
    "; les configurations v11, v11b et v11c, au GO de la course, aux notes et au champ inerte "
    "`relais_persistants_v4.plafond_relais_claude_usd` près, retiré en v11d (pièces).")
POINT_16 = ("16. **Mesure préalable de la réflexion d'Argon** (brouillons 5 et 6 ; R-5130 et décisions de la session de "
            "l'organisme datées 05:45Z) : deux cas fixés d'avance — sans la mesure, départ sous les risques dits ; avec la "
            "mesure (mot de Lazar ; GO-2026-11-22-128, au plus 10,50 USD, hors du plafond de la course), un appel de "
            "proposeur puis quatre de juge, aux arguments du gabarit, pièces choisies par rang, 4,58 USD au pire sans "
            "reprise, reprises des statuts 429 et de 500 et plus au plus deux fois par appel dans la limite de la ligne ; "
            "règle de lecture : départ refusé si un appel mesuré est refusé par le fournisseur pour sa requête ou rend un "
            "défaut, si la réflexion moyenne mesurée, pondérée comme dans la course, passe 31 462 jetons par appel, ou si la "
            "mesure reste inachevée (liste d'arrêt, « Avant le départ, hors du lanceur »). Lanceur v11d, configuration v11d "
            "(champ inerte retiré), gabarit du relevé des crédits v11d, devis v11e ; emplacement du gabarit du relevé du "
            "prix Claude retiré.")

# ------------------------------------------------------------------------------------------------ dernière section, récrite
DERNIERE = """## Emplacements et points à trancher avant le scellement (section à retirer de la version scellée)

Emplacements à remplir (empreintes des pièces du lanceur v11d, que la session de l'organisme envoie quand elles sont définitives, après la vérification du même contre-lecteur ; entre parenthèses, au texte, les valeurs scellées avec le lanceur v11c, qui peuvent encore changer) :

1. EMPREINTE À INSCRIRE — configuration fixe v11d (pièces).
2. EMPREINTE À INSCRIRE — commande en flux v2 d'Argon et de Carbon, et ses essais (pièces). Le relais Gemini v3 est inscrit (`2cf6bc6d…`) ; les réglages d'Argon et de Carbon et les bornes de leurs relais sont inscrits, ceux du code (§ Espèces, liste d'arrêt).
3. EMPREINTE À INSCRIRE — sonde commune d'Astra v3 et ses essais (pièces) ; la sonde d'Astra v3 est inscrite (`32366123…`).
4. EMPREINTE À INSCRIRE — essais du lanceur v11d ; gabarit de déclaration (v11c, ou v11d s'il en est écrit un) ; gabarit du relevé des crédits v11d (pièces) ; celle du lanceur seulement s'il ne porte plus l'empreinte de ce texte dans son code (sinon, cycle d'empreintes).
5. RÉFÉRENCE À INSCRIRE — ligne du registre des décisions où la mère inscrit, avec R-5130, les décisions de la session de l'organisme datées 05:45Z (en-tête, deux fois).
6. Inscrits : au brouillon 4, le libellé de la contre-lecture (« Opus 5.5, contre-lecteur neuf ») ; au brouillon 5, la référence des décisions du 23 novembre (R-5130) et le retrait du gabarit du relevé du prix Claude (le lanceur lit le relevé du jour, `course-v11/releve-prix-claude-course-affinage-v11.json`, jamais un gabarit).

Points tranchés ou à confirmer, avec la recommandation du rédacteur :

1. **Plafond de session des juges : 1,00 USD** — tranché (R-5018 ; R-5130) : pire cas d'un appel de juge d'Argon 0,917240 USD (lanceur v11b) ou 0,917356 (lanceurs v11c et v11d, entrée de juge de la forme de l'orchestrateur) ; marge de plus de 20 000 jetons d'entrée. La version scellée gardera les deux valeurs, avec leur source.
2. **Page de prix relue le jour du départ** : retenu, inchangé.
3. **Période** : la forme est établie (GO-2026-11-22-80 comme GO de la course ; essai du lanceur v11b sur la vraie lecture de l'orchestrateur). Un départ après le 25 novembre demande la confirmation de Lazar inscrite au registre et nommée dans une configuration neuve, donc un lanceur neuf (R12).
4. **Écrit de la mère sur les autres dépenses de la clé LUC** (R-5007, point (b)) : inchangé ; ce texte le lit « du départ à la fin de la course » et ne le fait pas contrôler par le lanceur ; à confirmer par la mère.
5. **Refus de l'interface et déclencheurs** : tranché (R-5130) : déclencheurs larges et cause écrite telle que le lanceur la lit ; texte aligné (liste d'arrêt ; § Règle des clés, « Clé LUC », point 5).
6. **Mesure préalable de la réflexion d'Argon** (GO-2026-11-22-128) : portée à Lazar (R-5130), rien ne part avant son mot ; fixée par la session de l'organisme (05:45Z) : un appel de proposeur puis quatre de juge, pièces de rang 1, reprises des statuts 429 et de 500 et plus au plus deux fois par appel dans la limite de la ligne, seuil de lecture de 31 462 jetons, la marge comprise (le rédacteur recommandait 32 476, confiance 0,6 ; la décision est écrite telle quelle) ; pire cas 4,58 USD sans reprise (devis v11, § 4). Règle de lecture retenue telle quelle ; sa clause « la moyenne des seuls appels de juge si aucun appel de proposeur n'est mesuré » est retirée, sans objet : une mesure achevée compte toujours son appel de proposeur. Recommandation du rédacteur, inchangée (confiance 0,7) : la jouer avant le départ.
7. **Pièces de la mesure, lecture du rédacteur, à confirmer** : avant la course, aucune fiche n'existe pour le juge ; « la première fiche dans l'ordre épinglé de la matière servie pour le rôle de juge » est écrite comme la première fiche, dans l'ordre de la liste que rend l'appel de proposeur de la mesure, que l'orchestrateur épinglé accepte. Lecture faite sur la v53 des fonctions de fiches (`""" + FICHES_V53 + """`, `""" + FICHES_V53_SHA[:8] + """…` : bloc `fiches` de la réponse, `preparer`, `entree_une_fiche`), non sur la v54 épinglée, absente de ce conteneur : la session d'exécution la constate sur la v54. Si une autre lecture est voulue (par exemple une fiche d'une course antérieure), le texte change avant le scellement.
8. **Une condition de plus, proposée, non ajoutée** (règle retenue telle quelle) : refuser aussi le départ si une réponse mesurée porte `hypothese_sortie_maximale_tenue` faux (la commande en flux v2 l'écrit après chaque réponse) ; ce cas contredirait la page de Google versée, sur laquelle reposent les pires cas d'Argon et de Carbon et le plafond de session des juges. Recommandation : l'ajouter, confiance 0,7 ; sinon le rapport de la mesure le dit, sans effet sur le départ.
9. **Argon à 45 056 jetons de sortie en flux** : jamais servi au-delà de 32 768 dans les pièces lues. Sans la mesure, un refus du fournisseur pour ce réglage ferait échouer chaque appel d'Argon, et A3 arrêterait ses deux rôles (étape des juges « non mesurée (technique) ») ; avec la mesure, un tel refus interdit le départ (liste d'arrêt). La porte à blanc et l'essai à blanc n'appellent pas le fournisseur.
10. **Notes de la configuration** : tranché (05:45Z) : champ inerte retiré en v11d, notes corrigées (commande en flux v2 nommée) ; à constater sur la pièce scellée.

Points que ce texte fixe et que le lanceur v11d doit tenir, avec un essai sain et un essai artefact chacun (R5) ; si le lanceur fait autrement, le texte ou le lanceur change, jamais un écart silencieux. La liste phrase par phrase est dans `course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md` (`""" + ANNEXE_SHA + """`), écrite sur le brouillon 2 : ses numéros de lignes (l. 1 à 295) valent pour ce brouillon 6, dont seules la ligne 296 (point 16 du différentiel) et la dernière section changent ; les brouillons 4 à 6 changent les phrases des items A1 à A4 (GO de la course GO-2026-11-22-80, GO-2026-11-18-14 exigé, registre dérivé, confirmation nommée dans la configuration), B2 et B5 (champs `solde_non_lu` et `reference`, montants et champs hors liste refusés ; gabarit du relevé des crédits v11d), C1 (réserve par appel lue et écrite), C4 (lecture confirmée par l'essai du développeur du lanceur v11), D1 à D4 et D6 (lecture toutes les 10 s, journal du run nommé ; déclencheurs élargis — l'item D3 est renversé : les refus propres au relais, 401, 403, 404 et 413, arrêtent la course — ; part engagée au plafond ; état illisible trois fois ; cause écrite ; relecture finale refaite jusqu'à trois fois), F1 à F5 (garde rejouée sur le corps de l'entrée la plus longue ; limite de l'invite comptée en caractères ; réglages et bornes du relais écrits ; trois gardes des v8 et v9 gardées en flux), G1 à G4 (même commande que Carbon ; garde rejouée sur la plus longue entrée de chaque rôle, juge dans la forme de l'orchestrateur ; pire cas du juge sur un cadre de 1 000 caractères supposé, non « réel » ; champ `argon_v11.plafond_session_juge_usd` ; bornes du relais d'Argon), I2 (base 35,683 : exacte 35,683407, lanceur 35,683424), I4 (libellé) et I6 (pièces : lanceur v11d, commande en flux v2, relais Gemini v3, sondes v3 ; aucun gabarit du relevé du prix Claude), et la section K (dépôt de travail qui porte la garde commune de `main` ; mesure préalable de la réflexion d'Argon, tenue hors du lanceur, l. 91). En résumé :

- le plafond du relais Claude égal à 45,00 USD au centime (arguments lus par PID et état), sa réserve par appel lue et écrite, et l'entrée de la clé LUC au relevé des crédits (`solde_non_lu` vrai, `reference` GO-2026-11-22-124, aucun montant, aucun autre champ que `source` et `note`) ;
- le GO de la course GO-2026-11-22-80 passé à l'orchestrateur et nommé par la configuration ; la lecture des lignes GO-2026-11-18-14, GO-2026-11-22-80, GO-2026-11-22-107 et GO-2026-11-22-124, et, après le 2026-11-25, de la ligne de confirmation nommée dans la configuration ;
- le relevé de l'état et du journal du relais Claude au moins une fois par minute (toutes les 10 s), le journal du run, l'arrêt au premier déclencheur (statut 400 à 499 hors 429 au journal, refus compté dans l'état, part engagée au plafond, trois lectures illisibles), la relecture finale, le code 5 et l'alerte `alerte-arret-part-claude.json` (nature, statut, cause lue) ;
- la garde gelée des appels aux modèles de Google sur la commande en flux de Carbon et d'Argon, avant l'envoi et après la réponse ; les prix d'Argon et de Carbon à 4 et 20 USD par million de jetons ; les réglages d'Argon (24 576, 45 056, en flux) et de Carbon (28 672, 65 536) ; le plafond de session des juges à 1,00 USD, et le pire cas d'un appel de juge d'Argon contrôlé sur la plus longue entrée de juge que bâtit le lanceur ;
- la sonde d'Astra faite avec `gpt-6.2-astra`, `OPENAI_API_KEY_2` et les prix 8 et 40, liée à la sonde commune v3 du jour, qui porte la variable de clé du relais jeté ;
- la base de l'écart au devis, 35,683 USD pour cinq espèces ;
- le libellé « Opus 5.5, contre-lecteur neuf » exigé de la contre-lecture ;
- les gardes héritées des lanceurs v7 à v10 que ce texte garde (bornes basses de tous les relais, exclusion mutuelle avec la course d'auto-conception, sonde liée à la sonde commune, état de relais neuf et lisible, codes de sortie distincts dont le code 6, plafond de session des proposeurs à 3,00 USD).

"""
DU_B5_AU_B6 = (" Du brouillon 5 au brouillon 6 (décisions de la session de l'organisme du 23 novembre, message daté 05:45Z) : mesure "
               "préalable fixée — un appel de proposeur puis quatre de juge, pièces choisies par rang, reprises des statuts 429 "
               "et de 500 et plus au plus deux fois par appel dans la limite de la ligne, 4,58 USD au pire sans reprise — ; "
               "seuil de la règle de lecture à 31 462 jetons, la marge comprise ; clause de repli sans objet retirée ; champ "
               "inerte de la configuration v11d retiré ; devis v11e et programme de calcul de la mesure ; aucun chiffre de la "
               "course changé.")
corps = [lignes[n] for n in range(1, 296)]
texte = "\n".join(corps) + "\n" + POINT_16 + "\n\n" + DERNIERE + ligne_du_b1_au_b5 + DU_B5_AU_B6 + "\n"
assert "RÉGLAGE À INSCRIRE" not in texte
assert texte.count("RÉFÉRENCE À INSCRIRE") == 4, texte.count("RÉFÉRENCE À INSCRIRE")   # en-tête deux fois, l. 8, dernière section
assert "32 476 jetons par appel (§ Plafond" not in texte and "la moyenne des seuls appels de juge si aucun" not in texte.split("\n## Emplacements")[0]
assert "releve-prix-claude-gabarit" not in texte
assert texte.count("\n## Emplacements et points à trancher avant le scellement") == 1
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 5 touchées (1 à 295) :", sorted(touchees))
print("lignes du brouillon 6 :", texte.count("\n"))
print("emplacements « EMPREINTE À INSCRIRE » :", texte.count("EMPREINTE À INSCRIRE"), "; « RÉFÉRENCE À INSCRIRE » :",
      texte.count("RÉFÉRENCE À INSCRIRE"))
