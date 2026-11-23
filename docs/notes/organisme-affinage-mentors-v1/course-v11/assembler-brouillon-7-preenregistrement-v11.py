#!/usr/bin/env python3
"""Assemble le brouillon 7 de la v11 à partir du brouillon 6.

Objet, sur les messages de la session de l'organisme du 23 novembre 2026 datés 05:54Z et 05:58Z : les décisions datées 05:45Z
sont citées sous R-5132 ; la mesure préalable de la réflexion d'Argon est accordée par Lazar (GO-2026-11-23-07, plan de
R-5132, plafond 10,50 USD, échéance 2026-11-30 ; inscrite par R-5134) et se joue après le scellement de ce texte ; les
réponses datées 05:58Z confirment la fiche du juge de la mesure, demandent de dire que la lecture des fonctions de fiches a été
faite sur la copie v53 (la contre-lecture la vérifie sur la v54 épinglée), et ajoutent une condition à la règle de lecture
(réponse mesurée qui porte `hypothese_sortie_maximale_tenue` faux) ; ces réponses ne sont encore dans aucune ligne du registre
de `main` lu : un emplacement de référence les attend ; devis v11f.
Les lignes 1 à 295 du brouillon 6 gardent leur numéro ; le point 16 du différentiel v10 → v11 (ligne 296) et la dernière
section (à retirer de la version scellée) sont récrits. Chaque remplacement exige que l'ancienne chaîne figure exactement une
fois dans la ligne visée ; sinon le programme s'arrête.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré dans le brouillon).
Usage : python3 -I assembler-brouillon-7-preenregistrement-v11.py BROUILLON-6.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

B6_SHA = "a8de23b50e0e359e0cf45caf143674a845ceeed2958b9aa1e209cef4c8f95b3d"
DEVIS_V11E_SHA = "c824fb2b4493f595dcdb2b05d01a3a72a75326deb540153033767ef6c313192b"
DEVIS_V11F_SHA = "ae76963e3280e05ea66173ce17db44d0f884667aeb5e1ca59bba8ad378bc9885"
ANNEXE_SHA = "abb967a9e2190f0ca607e8f136e1527105137d42c8225ed8f30a8234f9096b95"
FICHES_V53 = "docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/fiches_v53.py"
FICHES_V53_SHA = "7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6"
LU_B7 = {"commit": "1b26780dc04631554f0d344b3d5a527f8b7855ce",
         "go": "f17a81eadd8664abe32415ba81dd05abf7bbf63f120c37c7856594d76d7c3be7",
         "decisions": "f975fe6a48d8a57e9c66dc8bdecf85cf59d2df35922e004d5e66a7c0472c499d"}
N = "docs/notes/organisme-affinage-mentors-v1"
REF6 = "RÉFÉRENCE À INSCRIRE : ligne du registre des décisions où la mère les inscrit avec R-5130"
REF7 = "RÉFÉRENCE À INSCRIRE : ligne du registre des décisions qui les porte"
GO7 = "GO-2026-11-23-07"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == B6_SHA, "la source n'est pas le brouillon 6"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 334, len(L)   # 333 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
assert lignes[296].startswith("16. **Mesure préalable de la réflexion d'Argon**") and lignes[297] == ""
assert lignes[298].startswith("## Emplacements et points à trancher avant le scellement")
ligne_du_b1_au_b6 = lignes[333]
assert ligne_du_b1_au_b6.startswith("Du brouillon 1 au brouillon 2 :") and "Du brouillon 5 au brouillon 6" in ligne_du_b1_au_b6
touchees = set()


def sub(n, ancien, nouveau, fois=1):
    assert lignes[n].count(ancien) == fois, (n, ancien[:80], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


# ------------------------------------------------------------------------------------------------ en-tête
sub(3, "- **État de ce fichier : brouillon 6 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 5 (",
    "- **État de ce fichier : brouillon 7 de la v11, non scellé comme préenregistrement.** Il remplace le brouillon 6 "
    "(`course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-6.md`, `" + B6_SHA + "`), le brouillon 5 (")
sub(3, "message daté 05:45Z (" + REF6 + ") — mesure préalable fixée",
    "message daté 05:45Z (**R-5132**, registre des décisions de `main`) — mesure préalable fixée")
sub(3, "inerte de la configuration v11d retiré ; devis v11e.",
    "inerte de la configuration v11d retiré ; devis v11e. Objet du brouillon 7 : R-5132 cité ; mesure préalable accordée par "
    "Lazar (**" + GO7 + "**, plan de R-5132, plafond 10,50 USD, échéance 2026-11-30), jouée après le scellement de ce texte ; "
    "sur les réponses de la session de l'organisme datées 05:58Z (" + REF7 + "), fiche du juge de la mesure confirmée et "
    "condition `hypothese_sortie_maximale_tenue` ajoutée à sa règle de lecture ; devis v11f.")
sub(4, "lecture des fiches d'une réponse, forme d'entrée du juge.",
    "lecture des fiches d'une réponse, forme d'entrée du juge. Pour le brouillon 7, il a relu sur `main` (commit `"
    + LU_B7["commit"][:9] + "`) R-5132, R-5134 et la ligne " + GO7 + ".")
sub(5, "- Date (UTC) de ce brouillon : 2026-11-23T05:54:27Z (`date -u +%FT%TZ`) ; brouillon 5 : 2026-11-23T05:40:12Z ;",
    "- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; brouillon 6 : 2026-11-23T05:54:27Z ; brouillon 5 : "
    "2026-11-23T05:40:12Z ;")
sub(7, "chiffrée par le devis v11e", "chiffrée par le devis v11f")
sub(7, "(gabarit du relevé des crédits v11d), devis v11e, contre-lecteur",
    "(gabarit du relevé des crédits v11d), devis v11f, contre-lecteur")
sub(8, "nœud de dépense porté à Lazar par R-5130, rien ne part avant son mot ; ses deux cas : liste d'arrêt, « Avant le départ, "
       "hors du lanceur »).",
    "nœud de dépense porté à Lazar par R-5130 ; **accordée par Lazar, " + GO7 + "** : « go recos » vers 05:55Z, plan de R-5132, "
    "plafond 10,50 USD, échéance 2026-11-30, inscrite par R-5134 ; jouée après le scellement de ce texte ; ses deux cas : "
    "liste d'arrêt, « Avant le départ, hors du lanceur »).")
sub(8, "champ inerte de la configuration v11d retiré (" + REF6 + ").",
    "champ inerte de la configuration v11d retiré (**R-5132**). **Brouillon 7** : " + GO7 + " (mesure accordée) ; réponses de "
    "la session de l'organisme datées 05:58Z, étage 1 — fiche du juge de la mesure confirmée, lecture des fonctions de fiches "
    "faite sur la copie v53 à vérifier sur la v54 par la contre-lecture, condition `hypothese_sortie_maximale_tenue` ajoutée "
    "à la règle de lecture (" + REF7 + ") ; registres relus sur `main` au commit `" + LU_B7["commit"] + "` (`registres/go.md` `"
    + LU_B7["go"] + "`, `registres/decisions.md` `" + LU_B7["decisions"] + "`, où figurent R-5132 et R-5134).")

# ------------------------------------------------------------------------------------------------ pièces
sub(12, "est retiré (décision de la session de l'organisme, 05:45Z) ;", "est retiré (R-5132) ;")
sub(22, "  - **devis v11e** : `" + N + "/devis-course-affinage-mentors-v11e.md`, `" + DEVIS_V11E_SHA + "` — c'est le devis v11d (",
    "  - **devis v11f** : `" + N + "/devis-course-affinage-mentors-v11f.md`, `" + DEVIS_V11F_SHA + "` — c'est le devis v11e (`"
    + N + "/devis-course-affinage-mentors-v11e.md`, `" + DEVIS_V11E_SHA + "`) sans aucun chiffre changé, avec R-5132, " + GO7
    + " et la condition `hypothese_sortie_maximale_tenue` ; le devis v11e est le devis v11d (")
sub(22, "dans ce texte, « devis v11 » désigne ce devis v11e ;", "dans ce texte, « devis v11 » désigne ce devis v11f ;")
sub(22, "(23 novembre, R-5130 et message daté 05:45Z), à contre-lire ;",
    "(23 novembre, R-5130 et R-5132, et ses réponses datées 05:58Z), à contre-lire ;")

# ------------------------------------------------------------------------------------------------ espèces, mesure
sub(60, "(la mesure préalable de cette réflexion, si Lazar la confirme, éprouve ce risque et le suivant avant le départ :",
    "(la mesure préalable de cette réflexion, accordée par Lazar, " + GO7 + ", éprouve ce risque et le suivant avant le départ :")
sub(80, "devis v11 (v11e ; estimation inchangée depuis le v11)", "devis v11 (v11f ; estimation inchangée depuis le v11)")
sub(91, "nœud de dépense porté à Lazar par R-5130 ; rien ne part avant son mot) — deux cas, fixés ici avant toute mesure. "
        "**(a) Sans la mesure** (Lazar ne la confirme pas) :",
    "nœud de dépense porté à Lazar par R-5130 ; **accordée par Lazar, " + GO7 + "**, plan de R-5132, échéance 2026-11-30 ; jouée "
    "après le scellement de ce texte et avant le départ) — deux cas, fixés ici avant toute mesure (R-5132 : ce texte vaut avec "
    "ou sans elle). **(a) Sans la mesure** (si elle n'est pas jouée ; une mesure dont un envoi est parti relève du cas (b), et, "
    "laissée, elle est inachevée) :")
sub(91, "**(b) Avec la mesure** (mot de Lazar) : elle est jouée après le scellement de ce texte et avant le départ,",
    "**(b) Avec la mesure** (" + GO7 + ") : elle est jouée après le scellement de ce texte et avant le départ, au plus tard à "
    "l'échéance de sa ligne,")
sub(91, "**Appels et pièces, fixés ici** (décisions de la session de l'organisme, 05:45Z ; règle de choix par rang, aucun contenu "
        "lu) :",
    "**Appels et pièces, fixés ici** (R-5132 ; règle de choix par rang, aucun contenu lu) :")
sub(91, "avec un identifiant opaque — avant la course, aucune autre fiche n'existe pour le juge.",
    "avec un identifiant opaque — avant la course, aucune autre fiche n'existe pour le juge (réponses datées 05:58Z ; cette "
    "lecture des fonctions de fiches de l'orchestrateur a été faite par le rédacteur sur une copie empreintée de la v53, "
    "`pole/fiches_v53.py`, `" + FICHES_V53_SHA[:8] + "…`, et non sur la v54 épinglée : la contre-lecture la vérifie sur la v54, "
    "§ Contre-lecture).")
sub(91, "texte vide), si la réflexion moyenne mesurée,",
    "texte vide), si une réponse mesurée porte `hypothese_sortie_maximale_tenue` faux (la commande en flux v2 l'écrit après "
    "chaque réponse : réflexion et texte n'ont pas tenu ensemble dans la sortie maximale, contre la page de Google versée sur "
    "laquelle reposent les pires cas d'Argon et de Carbon et le plafond de session des juges ; réponses datées 05:58Z), si la "
    "réflexion moyenne mesurée,")

# ------------------------------------------------------------------------------------------------ plafond, contre-lecture
sub(101, "R-5130 et message daté 05:45Z ; à contre-lire).", "R-5130 et R-5132, et ses réponses datées 05:58Z ; à contre-lire).")
sub(101, "est de nouveau portée à Lazar, R-5130 ;", "a été de nouveau portée à Lazar, R-5130, qui l'a accordée, " + GO7 + " ;")
sub(167, "L'acte de gel écrit par le lanceur au lancement (empreintes du préenregistrement et de la contre-lecture, verdict lu) est "
         "la spécification servie à l'orchestrateur.",
    "L'acte de gel écrit par le lanceur au lancement (empreintes du préenregistrement et de la contre-lecture, verdict lu) est "
    "la spécification servie à l'orchestrateur. **v11 (brouillon 7)** : la contre-lecture vérifie aussi, sur la v54 épinglée "
    "de l'orchestrateur (`pole/fiches_v54.py`), la lecture des fiches que suppose la mesure préalable d'Argon (liste d'arrêt, "
    "« Avant le départ, hors du lanceur ») : le rédacteur l'a faite sur la copie v53.")

# ------------------------------------------------------------------------------------------------ différentiel v10 → v11
sub(290, "10. **Devis v11e** (écrit pour cette version, à contre-lire ; le devis v11d plus la mesure préalable d'Argon fixée,",
    "10. **Devis v11f** (écrit pour cette version, à contre-lire ; le devis v11e avec R-5132, " + GO7 + " et la condition "
    "`hypothese_sortie_maximale_tenue`, sans chiffre changé ; le devis v11e est le devis v11d plus la mesure préalable d'Argon "
    "fixée,")
POINT_16 = ("16. **Mesure préalable de la réflexion d'Argon** (brouillons 5 à 7 ; R-5130, R-5132 et " + GO7 + ") : deux cas "
            "fixés d'avance — sans la mesure, départ sous les risques dits ; avec la mesure (accordée par Lazar, " + GO7
            + ", au plus 10,50 USD, hors du plafond de la course, échéance 2026-11-30 ; jouée après le scellement), un appel de "
            "proposeur puis quatre de juge, aux arguments du gabarit, pièces choisies par rang, 4,58 USD au pire sans reprise, "
            "reprises des statuts 429 et de 500 et plus au plus deux fois par appel dans la limite de la ligne ; une mesure "
            "commencée relève de ce cas ; règle de lecture : départ refusé si un appel mesuré est refusé par le fournisseur pour "
            "sa requête ou rend un défaut, si une réponse mesurée porte `hypothese_sortie_maximale_tenue` faux, si la réflexion "
            "moyenne mesurée, pondérée comme dans la course, passe 31 462 jetons par appel, ou si la mesure reste inachevée "
            "(liste d'arrêt, « Avant le départ, hors du lanceur »). Lanceur v11d, configuration v11d (champ inerte retiré), "
            "gabarit du relevé des crédits v11d, devis v11f ; emplacement du gabarit du relevé du prix Claude retiré.")

# ------------------------------------------------------------------------------------------------ dernière section, récrite
DERNIERE = """## Emplacements et points à trancher avant le scellement (section à retirer de la version scellée)

Emplacements à remplir (empreintes des pièces du lanceur v11d, que la session de l'organisme envoie quand elles sont définitives, après la vérification du même contre-lecteur ; entre parenthèses, au texte, les valeurs scellées avec le lanceur v11c, qui peuvent encore changer) :

1. EMPREINTE À INSCRIRE — configuration fixe v11d (pièces).
2. EMPREINTE À INSCRIRE — commande en flux v2 d'Argon et de Carbon, et ses essais (pièces). Le relais Gemini v3 est inscrit (`2cf6bc6d…`) ; les réglages d'Argon et de Carbon et les bornes de leurs relais sont inscrits, ceux du code (§ Espèces, liste d'arrêt).
3. EMPREINTE À INSCRIRE — sonde commune d'Astra v3 et ses essais (pièces) ; la sonde d'Astra v3 est inscrite (`32366123…`).
4. EMPREINTE À INSCRIRE — essais du lanceur v11d ; gabarit de déclaration (v11c, ou v11d s'il en est écrit un) ; gabarit du relevé des crédits v11d (pièces) ; celle du lanceur seulement s'il ne porte plus l'empreinte de ce texte dans son code (sinon, cycle d'empreintes).
5. RÉFÉRENCE À INSCRIRE — ligne du registre des décisions qui porte les réponses de la session de l'organisme datées 05:58Z (fiche du juge confirmée ; condition `hypothese_sortie_maximale_tenue` ajoutée) ; en-tête, deux fois. Au registre de `main` lu à `""" + LU_B7["commit"][:9] + """`, aucune ligne ne les porte (lignes R-5132 à R-5136 lues).
6. Inscrits : au brouillon 4, le libellé de la contre-lecture (« Opus 5.5, contre-lecteur neuf ») ; au brouillon 5, R-5130 et le retrait du gabarit du relevé du prix Claude (le lanceur lit le relevé du jour, `course-v11/releve-prix-claude-course-affinage-v11.json`, jamais un gabarit) ; au brouillon 7, R-5132 et """ + GO7 + """.

Points tranchés ou à confirmer, avec la recommandation du rédacteur :

1. **Plafond de session des juges : 1,00 USD** — tranché (R-5018 ; R-5130) : pire cas d'un appel de juge d'Argon 0,917240 USD (lanceur v11b) ou 0,917356 (lanceurs v11c et v11d, entrée de juge de la forme de l'orchestrateur) ; marge de plus de 20 000 jetons d'entrée. La version scellée gardera les deux valeurs, avec leur source.
2. **Page de prix relue le jour du départ** : retenu, inchangé.
3. **Période** : la forme est établie (GO-2026-11-22-80 comme GO de la course ; essai du lanceur v11b sur la vraie lecture de l'orchestrateur). Un départ après le 25 novembre demande la confirmation de Lazar inscrite au registre et nommée dans une configuration neuve, donc un lanceur neuf (R12).
4. **Écrit de la mère sur les autres dépenses de la clé LUC** (R-5007, point (b)) : inchangé ; ce texte le lit « du départ à la fin de la course » et ne le fait pas contrôler par le lanceur ; à confirmer par la mère.
5. **Refus de l'interface et déclencheurs** : tranché (R-5130) : déclencheurs larges et cause écrite telle que le lanceur la lit ; texte aligné (liste d'arrêt ; § Règle des clés, « Clé LUC », point 5).
6. **Mesure préalable de la réflexion d'Argon** : accordée par Lazar (""" + GO7 + """, plan de R-5132, plafond 10,50 USD, échéance 2026-11-30 ; inscrite par R-5134) ; jouée après le scellement de ce texte (R1) et avant le départ ; plan et seuil de R-5132 (un appel de proposeur puis quatre de juge, pièces de rang 1, reprises au plus deux par appel dans la limite de la ligne, seuil de 31 462 jetons, la marge comprise ; le rédacteur recommandait 32 476, confiance 0,6, la décision est écrite telle quelle) ; pire cas 4,58 USD sans reprise (devis v11, § 4). Le texte garde ses deux cas (R-5132 : valable avec ou sans la mesure) ; une mesure dont un envoi est parti relève du cas (b). Si elle n'est pas jouée avant l'échéance de sa ligne, le cas (a) vaut tel qu'il est écrit. Recommandation du rédacteur, inchangée (confiance 0,7) : la jouer dès le scellement.
7. **Fiche du juge de la mesure** : tranché (réponses datées 05:58Z) : la première fiche acceptée par l'orchestrateur épinglé dans la réponse de l'appel de proposeur de la mesure, passée par programme, sans lecture. Lecture des fonctions de fiches faite sur la copie v53 (`""" + FICHES_V53 + """`, `""" + FICHES_V53_SHA[:8] + """…`), non sur la v54 épinglée, absente de ce conteneur : la contre-lecture la vérifie sur la v54 (§ Contre-lecture).
8. **Condition `hypothese_sortie_maximale_tenue`** : tranché (réponses datées 05:58Z) : ajoutée à la règle de lecture de la mesure (liste d'arrêt).
9. **Argon à 45 056 jetons de sortie en flux** : jamais servi au-delà de 32 768 dans les pièces lues. Sans la mesure, un refus du fournisseur pour ce réglage ferait échouer chaque appel d'Argon, et A3 arrêterait ses deux rôles (étape des juges « non mesurée (technique) ») ; avec la mesure, un tel refus interdit le départ (liste d'arrêt). La porte à blanc et l'essai à blanc n'appellent pas le fournisseur.
10. **Notes de la configuration** : tranché (R-5132) : champ inerte retiré en v11d, notes corrigées (commande en flux v2 nommée) ; à constater sur la pièce scellée.

Points que ce texte fixe et que le lanceur v11d doit tenir, avec un essai sain et un essai artefact chacun (R5) ; si le lanceur fait autrement, le texte ou le lanceur change, jamais un écart silencieux. La liste phrase par phrase est dans `course-v11/phrases-du-brouillon-2-qui-supposent-une-garde-du-lanceur-v11.md` (`""" + ANNEXE_SHA + """`), écrite sur le brouillon 2 : ses numéros de lignes (l. 1 à 295) valent pour ce brouillon 7, dont seules la ligne 296 (point 16 du différentiel) et la dernière section changent ; les brouillons 4 à 7 changent les phrases des items A1 à A4 (GO de la course GO-2026-11-22-80, GO-2026-11-18-14 exigé, registre dérivé, confirmation nommée dans la configuration), B2 et B5 (champs `solde_non_lu` et `reference`, montants et champs hors liste refusés ; gabarit du relevé des crédits v11d), C1 (réserve par appel lue et écrite), C4 (lecture confirmée par l'essai du développeur du lanceur v11), D1 à D4 et D6 (lecture toutes les 10 s, journal du run nommé ; déclencheurs élargis — l'item D3 est renversé : les refus propres au relais, 401, 403, 404 et 413, arrêtent la course — ; part engagée au plafond ; état illisible trois fois ; cause écrite ; relecture finale refaite jusqu'à trois fois), F1 à F5 (garde rejouée sur le corps de l'entrée la plus longue ; limite de l'invite comptée en caractères ; réglages et bornes du relais écrits ; trois gardes des v8 et v9 gardées en flux), G1 à G4 (même commande que Carbon ; garde rejouée sur la plus longue entrée de chaque rôle, juge dans la forme de l'orchestrateur ; pire cas du juge sur un cadre de 1 000 caractères supposé, non « réel » ; champ `argon_v11.plafond_session_juge_usd` ; bornes du relais d'Argon), I2 (base 35,683 : exacte 35,683407, lanceur 35,683424), I4 (libellé) et I6 (pièces : lanceur v11d, commande en flux v2, relais Gemini v3, sondes v3 ; aucun gabarit du relevé du prix Claude), et la section K (dépôt de travail qui porte la garde commune de `main` ; mesure préalable de la réflexion d'Argon, tenue hors du lanceur, l. 91). En résumé :

- le plafond du relais Claude égal à 45,00 USD au centime (arguments lus par PID et état), sa réserve par appel lue et écrite, et l'entrée de la clé LUC au relevé des crédits (`solde_non_lu` vrai, `reference` GO-2026-11-22-124, aucun montant, aucun autre champ que `source` et `note`) ;
- le GO de la course GO-2026-11-22-80 passé à l'orchestrateur et nommé par la configuration ; la lecture des lignes GO-2026-11-18-14, GO-2026-11-22-80, GO-2026-11-22-107 et GO-2026-11-22-124, et, après le 2026-11-25, de la ligne de confirmation nommée dans la configuration ;
- le relevé de l'état et du journal du relais Claude au moins une fois par minute (toutes les 10 s), le journal du run, l'arrêt au premier déclencheur (statut 400 à 499 hors 429 au journal, refus compté dans l'état, part engagée au plafond, trois lectures illisibles), la relecture finale, le code 5 et l'alerte `alerte-arret-part-claude.json` (nature, statut, cause lue) ;
- la garde gelée des appels aux modèles de Google sur la commande en flux de Carbon et d'Argon, avant l'envoi et après la réponse ; les prix d'Argon et de Carbon à 4 et 20 USD par million de jetons ; les réglages d'Argon (24 576, 45 056, en flux) et de Carbon (28 672, 65 536) ; le plafond de session des juges à 1,00 USD, et le pire cas d'un appel de juge d'Argon contrôlé sur la plus longue entrée de juge que bâtit le lanceur ;
- la sonde d'Astra faite avec `gpt-6.2-astra`, `OPENAI_API_KEY_2` et les prix 8 et 40, liée à la sonde commune v3 du jour, qui porte la variable de clé du relais jeté ;
- la base de l'écart au devis, 35,683 USD pour cinq espèces ;
- le libellé « Opus 5.5, contre-lecteur neuf » exigé de la contre-lecture ;
- les gardes héritées des lanceurs v7 à v10 que ce texte garde (bornes basses de tous les relais, exclusion mutuelle avec la course d'auto-conception, sonde liée à la sonde commune, état de relais neuf et lisible, codes de sortie distincts dont le code 6, plafond de session des proposeurs à 3,00 USD).

"""
DU_B6_AU_B7 = (" Du brouillon 6 au brouillon 7 (messages de la session de l'organisme datés 05:54Z et 05:58Z) : R-5132 cité ; "
               "mesure accordée par Lazar (" + GO7 + ", échéance 2026-11-30), jouée après le scellement ; une mesure commencée "
               "relève du cas (b) ; condition `hypothese_sortie_maximale_tenue` ajoutée à la règle de lecture ; fiche du juge "
               "confirmée, lecture des fonctions de fiches faite sur la v53, vérifiée sur la v54 par la contre-lecture ; devis "
               "v11f ; aucun chiffre changé.")
corps = [lignes[n] for n in range(1, 296)]
texte = "\n".join(corps) + "\n" + POINT_16 + "\n\n" + DERNIERE + ligne_du_b1_au_b6 + DU_B6_AU_B7 + "\n"
assert "RÉGLAGE À INSCRIRE" not in texte and REF6 not in texte
assert texte.count("RÉFÉRENCE À INSCRIRE") == 4, texte.count("RÉFÉRENCE À INSCRIRE")   # l. 3 deux fois, l. 8, dernière section
assert "si Lazar la confirme" not in texte and "Lazar ne la confirme pas" not in texte
assert "releve-prix-claude-gabarit" not in texte
assert texte.count("\n## Emplacements et points à trancher avant le scellement") == 1
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), dst)
print("lignes du brouillon 6 touchées (1 à 295) :", sorted(touchees))
print("lignes du brouillon 7 :", texte.count("\n"))
print("emplacements « EMPREINTE À INSCRIRE » :", texte.count("EMPREINTE À INSCRIRE"), "; « RÉFÉRENCE À INSCRIRE » :",
      texte.count("RÉFÉRENCE À INSCRIRE"))
