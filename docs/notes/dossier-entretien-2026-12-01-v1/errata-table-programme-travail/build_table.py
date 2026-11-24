# Construit l'erratum 1 de la table des revendications v2 corrigée (v1).
# Ecrit un seul fichier : celui que la consigne nomme.
import hashlib, sys

RACINE = '/home/user/controle-ia-travail/'
CIBLE = 'docs/notes/revendications-en-vigueur-v2/table-revendications-en-vigueur-v2-corrigee-v1.md'
SORTIE = 'docs/notes/revendications-en-vigueur-v2/table-revendications-en-vigueur-v2-corrigee-v1-erratum-1.md'
ERR1 = 'docs/notes/dossier-entretien-2026-12-01-v1/erratum-1-programme-v3-lemme-application-v3.md'

lignes_err1 = open(RACINE + ERR1, encoding='utf-8').read().split('\n')
k = [i for i, l in enumerate(lignes_err1) if l.startswith('**Variante B — le temps seul.**')]
assert len(k) == 1
ENONCE_B = lignes_err1[k[0] + 2]
assert ENONCE_B.startswith('> Chez des agents qui sabotent')
ENONCE_B = ENONCE_B[2:]
assert "du nombre d'actions entre lesquelles le sabotage est réparti" in ENONCE_B
assert "ou d'agents" not in ENONCE_B

GO5 = "GO-2026-11-24-21, point 5"
FICHE = "`docs/notes/revendications-en-vigueur-v2/fiche-onze-noeuds-table-v2-v1.md`"

def dec(n, opt):
    return "go.md GO-2026-11-24-21 (point 5 : nœud %s de la fiche des onze nœuds, option %s)" % (n, opt)

# Chaque groupe : (titre, résumé de la ligne après application, [entrées])
# Chaque entrée : (identifiant, ancien, nouveau, raison)
G = []

G.append((
    "Tête de la table : un statut de plus, et la correspondance des numéros",
    None,
    [
        ("T-0a",
         "**proposition sans décision** : changement proposé par une pièce lue, qu'aucun mot de Lazar trouvé n'accorde.",
         "**proposition sans décision** : changement proposé par une pièce lue, qu'aucun mot de Lazar trouvé n'accorde. **proposition accordée** (statut ajouté par l'erratum 1 de cette table, aucun des cinq autres ne convenant) : changement proposé par une pièce lue, qu'un mot de Lazar accorde ; la ligne dit où sa lettre est portée : sur la ligne visée, ou dans une pièce à venir, nommée ; dans ce second cas, la ligne visée garde son énoncé d'ici là.",
         "Les nœuds 8 à 11 de la fiche accordent des propositions ; pour les nœuds 8 et 11, la lettre vient par une pièce à écrire (préenregistrement du papier C, programme v4). Aucun des cinq statuts ne le dit. Choix de tenue de table, non décision : signalé en fin de fichier."),
        ("T-0b",
         "Section réécrite selon la question 4 de la contre-lecture. Rien ci-dessous n'est tranché par cette table.",
         "Section réécrite selon la question 4 de la contre-lecture. Rien ci-dessous n'est tranché par cette table. Depuis l'erratum 1 de cette table : Lazar a tranché le 24 novembre neuf des onze nœuds de 3.1, selon les recommandations de la fiche des onze nœuds (" + FICHE + ", 72784e0f ; go.md " + GO5 + ") ; deux restent ouverts (go.md GO-2026-11-24-31, point 4). La fiche ne numérote pas les nœuds comme cette section, et les mots de Lazar suivent les numéros de la fiche. Correspondance, numéro d'ici puis numéro de la fiche : 1 et 1 ; 2 et 5 ; 3 et 6 ; 4 et 2 ; 5 et 10 ; 6 et 7 ; 7 et 8 ; 8 et 9 ; 9 et 3 ; 10 et 11 ; 11 et 4. Les deux nœuds ouverts sont donc le 2 et le 6 d'ici (le 5 et le 7 de la fiche).",
         "GO-2026-11-24-21, point 5, et GO-2026-11-24-31, point 4. Les deux numérotations diffèrent ; sans la correspondance, « nœuds 5 et 7 » se lirait ici comme la loi sur les moniteurs et le papier C."),
    ]))

G.append((
    "Nœud 1 de la fiche (nœud 1 de la table) — lettre de l'accumulation sur sondes (H2) : tranché, option (a)",
    "Ligne de l'accumulation séquentielle (table 1.1). Statut : resserrée, inchangé. Énoncé : inchangé, c'est la lettre du programme v3. Décision : s'ajoute GO-2026-11-24-21, point 5. La réserve « non confirmé » tombe en section 2.",
    [
        ("T-1a",
         "GO-2026-11-22-24 (point 2, pour le seul modèle nul de la thèse)",
         "GO-2026-11-22-24 (point 2, pour le seul modèle nul de la thèse) ; " + dec(1, "a"),
         "GO-2026-11-24-21, point 5 : recommandation (a) de la fiche, nœud 1."),
        ("T-1b",
         "Voir nœud 1.",
         "Remplacement confirmé par Lazar le 24 novembre (" + GO5 + " ; nœud 1 de la fiche, option a) : le go à la version 3 vaut le mot que N-076 exige (§ 13, point 4), et la lettre de N-007 sur l'horizon est resserrée. Un erratum de N-076 doit le dire : il reste à écrire.",
         "La fiche recommande (a), « en le disant dans un erratum de N-076 ». Cet erratum n'est pas écrit ici."),
        ("T-1c",
         "la modification de l'énoncé est un nœud sans défaut selon N-076 (§ 13, point 4), non confirmé (nœud 1)",
         "la modification de l'énoncé, nœud sans défaut selon N-076 (§ 13, point 4), est confirmée par Lazar le 24 novembre (" + GO5 + " ; nœud 1)",
         "Section 2. La moitié « non confirmé » de la réserve tombe ; la moitié « scellement provisoire » reste."),
        ("T-1d",
         "programme v3, § 5 (scellement provisoire ; nœud 1)",
         "programme v3, § 5 (scellement provisoire) ; " + GO5 + " (nœud 1)",
         "Section 2, colonne des décisions : la décision qui confirme est citée."),
        ("T-1e",
         "1. **Lettre de l'accumulation sur sondes (H2).**",
         "1. **Lettre de l'accumulation sur sondes (H2) — tranché le 24 novembre (nœud 1 de la fiche, option a ; " + GO5 + ").** Le go à la version 3 vaut le mot que N-076 exige : la lettre du programme v3 fait foi, celle de N-007 est resserrée ; un erratum de N-076 reste à écrire pour le dire. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

G.append((
    "Nœud 2 de la fiche (nœud 4 de la table) — courbe selon le nombre d'agents (H3), « somme plate » : tranché, option (b)",
    "Ligne de la courbe de sécurité selon le nombre d'agents (table 1.3). Statut : resserrée, inchangé. Énoncé : la somme globale n'est dite plate que sous copies honnêtes indépendantes ; la marque « sous simulation » reste. Décision : s'ajoute GO-2026-11-24-21, point 5.",
    [
        ("T-2a",
         "Lettre du programme v3, **sous simulation** : à budget et nombre total d'actions fixés, la somme globale est prédite plate en nombre d'agents et le maximum décroissant (Avenhaus et Jaech 1981) ; la sonde change la constante, non la pente. C'est une prévision, non un constat.",
         "Lettre du programme v3, précisée le 24 novembre, **sous simulation** : à budget et nombre total d'actions fixés, la somme globale est prédite plate en nombre d'agents, seulement sous copies honnêtes indépendantes, et le maximum décroissant (Avenhaus et Jaech 1981) ; la sonde change la constante, non la pente. C'est une prévision, non un constat. La condition d'indépendance est écrite par décision de Lazar (" + GO5 + " ; nœud 2 de la fiche, option b) : si les copies honnêtes sont corrélées, la somme n'est pas dite plate. Le programme v3 scellé porte encore *plate* sans cette condition : un erratum du programme reste à écrire.",
         "GO-2026-11-24-21, point 5 : recommandation (b) de la fiche, « plate seulement sous copies honnêtes indépendantes ». Aucune décision lue ne lève la marque « sous simulation » : elle reste."),
        ("T-2b",
         "GO-2026-11-24-15 (point 1) ; `decision-N-013-v1.md` 157d388e (§ 8)",
         "GO-2026-11-24-15 (point 1), GO-2026-11-24-21 (point 5 : nœud 2 de la fiche des onze nœuds, option b) ; `decision-N-013-v1.md` 157d388e (§ 8)",
         "La décision qui précise la lettre est citée sur la ligne."),
        ("T-2c",
         "Lettre remplacée : l'énoncé nomme l'agrégateur.",
         "Lettre remplacée : l'énoncé nomme l'agrégateur. Condition d'indépendance des copies honnêtes ajoutée par l'erratum 1 de cette table.",
         "Colonne « changement » tenue à jour."),
        ("T-2d",
         "Vise H3.",
         "Vise H3. Accordé le 24 novembre pour la seule condition d'indépendance des copies honnêtes (" + GO5 + " ; nœud 2 de la fiche) : voir la ligne de la courbe. Écrire le terme de corrélation honnête lui-même reste sans décision.",
         "Ligne de la proposition (table 1.3). La fiche n'accorde que la condition ; le reste de la proposition garde son statut."),
        ("T-2e",
         "La courbe selon le nombre d'agents (H3) dans sa lettre du programme v3 : une prévision, sous simulation, non un constat.",
         "La courbe selon le nombre d'agents (H3) dans sa lettre du programme v3, la somme n'étant dite plate que sous copies honnêtes indépendantes : une prévision, sous simulation, non un constat.",
         "Section 2 : ce qui reste est dit dans la lettre précisée."),
        ("T-2f",
         "(scellement provisoire ; sous simulation ; nœud 4)",
         "(scellement provisoire ; sous simulation) ; " + GO5 + " (nœud 4 d'ici, nœud 2 de la fiche)",
         "Section 2, colonne des décisions : le nœud est tranché."),
        ("T-2g",
         "4. **Courbe selon le nombre d'agents (H3).**",
         "4. **Courbe selon le nombre d'agents (H3) — tranché le 24 novembre (nœud 2 de la fiche, option b ; " + GO5 + ").** La somme n'est dite plate que sous copies honnêtes indépendantes ; la marque sous simulation reste. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

G.append((
    "Nœud 3 de la fiche (nœud 9 de la table) — transposition du jeton à l'action : tranché, option (a)",
    "Ligne de la transposition du jeton à l'action (table 1.1). Statut : de « revendiquée » à « resserrée » (la question reste revendiquée ; sa lettre perd trois mots). Énoncé : la question, sans les mots « angle mort identifié ». Décision : GO-2026-11-24-21, point 5.",
    [
        ("T-3a",
         "Angle mort identifié, non calibré.",
         "Question non calibrée. Les mots *angle mort identifié* sont retirés le 24 novembre (" + GO5 + " ; nœud 3 de la fiche, option a) : la recherche exhaustive ne les soutient pas (R-4771, règle R8). Le programme v3 scellé les porte encore : un erratum du programme reste à écrire.",
         "GO-2026-11-24-21, point 5 : recommandation (a) de la fiche. La raison est celle de la fiche."),
        ("T-3b",
         "Rien de nommé. Un nœud du 14 novembre propose de corriger sa prémisse",
         "Les mots *angle mort identifié*, retirés le 24 novembre : ne plus les écrire. Un nœud du 14 novembre propose de corriger sa prémisse",
         "Colonne « non revendiqué à côté » : les mots retirés y sont nommés."),
        ("T-3c",
         "| revendiquée | `docs/programme-controle-ia-v2.md` 2fd63bad (§ 5) ; `docs/decisions/decision-N-013-v1.md` 157d388e (§ 8) ; `registres/decisions.md` R-2670",
         "| resserrée | " + dec(3, "a") + " ; `docs/programme-controle-ia-v2.md` 2fd63bad (§ 5) ; `docs/decisions/decision-N-013-v1.md` 157d388e (§ 8) ; `registres/decisions.md` R-2670",
         "Une décision réduit la lettre : c'est la définition de « resserrée » dans cette table. Choix de tenue de table : signalé en fin de fichier."),
        ("T-3d",
         "(§ 1, liste des hypothèses revendiquées du papier A au 21 novembre) | Aucun. |",
         "(§ 1, liste des hypothèses revendiquées du papier A au 21 novembre) | De *revendiquée* à *resserrée* : trois mots retirés de l'énoncé ; la question ne change pas. |",
         "Colonne « changement » tenue à jour."),
        ("T-3e",
         "Le programme v3 garde ces mots.",
         "Le programme v3 garde ces mots. Leur retrait est accordé le 24 novembre (" + GO5 + " ; nœud 3 de la fiche) : voir la ligne de la transposition. La reformulation en question sur le maximum sous fragmentation reste sans décision.",
         "Ligne de la proposition (table 1.1). La fiche n'accorde que le retrait des mots."),
        ("T-3f",
         "9. **Transposition du jeton à l'action (Tr).**",
         "9. **Transposition du jeton à l'action (Tr) — tranché le 24 novembre (nœud 3 de la fiche, option a ; " + GO5 + ").** Les mots *angle mort identifié* sont retirés. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

G.append((
    "Nœud 4 de la fiche (nœud 11 de la table) — mesure des audits économisés : tranché, option (a)",
    "Ligne de la mesure des audits économisés (table 1.1). Statut : de « mesure descriptive gardée (par défaut) » à « revendiquée », comme prédiction secondaire du papier A. Énoncé : prédiction secondaire revendiquée, scellée avant la porte de fin de phase 1 (G1), hors de son critère. Décision : GO-2026-11-22-12, point 1, et GO-2026-11-24-21, point 5.",
    [
        ("T-4a",
         "Mesure secondaire du papier A ; sa prévision est scellée avant la porte de fin de phase 1 (G1).",
         "Prédiction secondaire revendiquée du papier A, hors du critère de la porte de fin de phase 1 (G1) ; sa prévision est scellée avant cette porte.",
         "GO-2026-11-24-21, point 5 : recommandation (a) de la fiche, « hors du critère de G1 »."),
        ("T-4b",
         "| mesure descriptive gardée (par défaut : la décision dit",
         "| revendiquée (prédiction secondaire du papier A, hors du critère de la porte de fin de phase 1 ; la décision du 22 novembre dit",
         "Statut, première moitié de la cellule. Les mots cités de la décision du 22 novembre restent entre les deux entrées."),
        ("T-4c",
         "; une prévision scellée est une promesse, que ce statut ne dit pas ; nœud 11)",
         "; tranché le 24 novembre : " + GO5 + " ; nœud 11 d'ici, nœud 4 de la fiche)",
         "Statut, seconde moitié de la cellule. Le renvoi au nœud devient le renvoi à la décision."),
        ("T-4d",
         "| go.md GO-2026-11-22-12 (point 1) | Ligne neuve. |",
         "| go.md GO-2026-11-22-12 (point 1) ; GO-2026-11-24-21 (point 5 : nœud 4 de la fiche des onze nœuds, option a) | Ligne neuve. Statut tranché par l'erratum 1 de cette table : de *mesure descriptive gardée, par défaut* à *revendiquée*. |",
         "La décision qui tranche est citée sur la ligne."),
        ("T-4e",
         "11. **Mesure des audits économisés.**",
         "11. **Mesure des audits économisés — tranché le 24 novembre (nœud 4 de la fiche, option a ; " + GO5 + ").** Prédiction secondaire revendiquée du papier A, scellée avant la porte de fin de phase 1 (G1), hors de son critère. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

PHRASE_COLL = "Un collisionneur sur une question qui nomme les copies multiples est proposé après l'entretien (note de sortie du collisionneur sur les revendications)."

G.append((
    "Nœud 5 de la fiche (nœud 2 de la table) — co-élévation entre copies : ouvert",
    "Ligne de la co-élévation des scores de sondes entre copies (table 1.3) : rien ne change. Statut : resserrée. Énoncé : la lettre de N-069. La proposition de la resserrer reste « proposition sans décision ».",
    [
        ("T-5",
         "2. **Co-élévation entre copies.**",
         "2. **Co-élévation entre copies — reste ouvert (nœud 5 de la fiche ; GO-2026-11-24-31, point 4, option b).** La note de sortie du collisionneur sur les revendications ne dit rien de direct sur les copies multiples : sa concordance n'est qu'indirecte. " + PHRASE_COLL + " Texte d'origine, toujours en vigueur :",
         "GO-2026-11-24-31, point 4 : les nœuds 5 et 7 restent ouverts. La note de sortie (`docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-revendications-v1.md`, 32a2ffc2) dit : « rien de direct »."),
    ]))

G.append((
    "Nœud 6 de la fiche (nœud 3 de la table) — statistique conjointe : tranché, option (b)",
    "Ligne de la statistique conjointe dans le temps et entre agents (table 1.3). Statut : resserrée, inchangé. Énoncé : le gain n'est revendiqué que sur les sabotages qui déplacent la dépendance ; le bras « adversaire entraîné contre elle » n'est plus promis, il reste une mesure descriptive. Décision : s'ajoute GO-2026-11-24-21, point 5 ; la lettre de N-069 reste à réécrire.",
    [
        ("T-6a",
         ", à fausses alarmes égales, y compris sous un adversaire entraîné contre elle. Le programme v3 y ajoute (E3.1) : la somme globale est une base obligatoire ; le gain n'est revendiqué que sur les sabotages qui déplacent la dépendance.",
         ", à fausses alarmes égales, sur les seuls sabotages qui déplacent la dépendance ; la somme globale est une base obligatoire (lettre du programme v3, E3.1). Le bras *sous un adversaire entraîné contre elle* n'est plus promis : il reste au plan comme mesure descriptive, rapportée sans promesse (" + GO5 + " ; nœud 6 de la fiche, option b). La lettre de N-069 (§ 4, point 2) est à réécrire sur celle du programme v3 : ce travail d'écriture reste à faire.",
         "GO-2026-11-24-21, point 5 : recommandation (b) de la fiche, « réécrire N-069 et garder ce bras comme mesure descriptive »."),
        ("T-6b",
         "programme v3 (§ 10, E3.1, scellement provisoire)",
         "programme v3 (§ 10, E3.1, scellement provisoire) ; " + dec(6, "b"),
         "La décision qui tranche est citée sur la ligne."),
        ("T-6c",
         "Lettre de N-069 non réécrite (nœud 3).",
         "Bras de l'adversaire entraîné devenu mesure descriptive par l'erratum 1 de cette table. Lettre de N-069 à réécrire (nœud 3 d'ici, nœud 6 de la fiche : tranché).",
         "Colonne « changement » tenue à jour."),
        ("T-6d",
         "l'égalité avec la somme globale serait le résultat attendu.",
         "l'égalité avec la somme globale serait le résultat attendu. Accordé le 24 novembre pour le seul bras de l'adversaire entraîné, devenu mesure descriptive (" + GO5 + " ; nœud 6 de la fiche) : voir la ligne de la statistique conjointe. Les deux autres points restent sans décision.",
         "Ligne de la proposition (table 1.3). La fiche n'accorde que le sort du bras."),
        ("T-6e",
         "3. **Statistique conjointe.**",
         "3. **Statistique conjointe — tranché le 24 novembre (nœud 6 de la fiche, option b ; " + GO5 + ").** La lettre de N-069 est à réécrire sur celle du programme v3 ; le bras de l'adversaire entraîné reste une mesure descriptive, sans promesse. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

G.append((
    "Nœud 7 de la fiche (nœud 6 de la table) — thèse du papier B : ouvert",
    "Ligne de la proposition « thèse du papier B à deux nuls hérités, porte position ou dépendance, repli écrit d'avance » (table 1.3) : rien ne change. Statut : proposition sans décision.",
    [
        ("T-7",
         "6. **Papier B.**",
         "6. **Papier B — reste ouvert (nœud 7 de la fiche ; GO-2026-11-24-31, point 4, option b).** La note de sortie du collisionneur sur les revendications ne dit rien de la thèse du papier B ; elle n'éclaire que la forme d'une porte préalable. À trancher avant l'écriture du préenregistrement de la porte de la phase 2 (G2), selon la fiche. " + PHRASE_COLL + " Texte d'origine, toujours en vigueur :",
         "GO-2026-11-24-31, point 4 : les nœuds 5 et 7 restent ouverts. L'échéance est celle de la recommandation de la fiche, nœud 7."),
    ]))

ACC8 = "| — | proposition accordée (lettre à venir : adoptée dans le préenregistrement du papier C, où elle est écrite et contre-lue ; d'ici son scellement, la ligne visée garde son énoncé) | " + dec(8, "a") + " ; "
R8 = "GO-2026-11-24-21, point 5 : recommandation (a) de la fiche, les six propositions adoptées en bloc dans le préenregistrement du papier C, « chacune contre-lue dans ce préenregistrement »."
G.append((
    "Nœud 8 de la fiche (nœud 7 de la table) — six propositions sur le papier C : tranché, option (a)",
    "Six lignes de propositions (table 1.2). Statut : de « proposition sans décision » à « proposition accordée ». Énoncé : inchangé ; la lettre de chacune vient par le préenregistrement du papier C, et d'ici là les six lignes visées (de la loi de déférence au second terrain) gardent leur énoncé. Décision : GO-2026-11-24-21, point 5.",
    [
        ("T-8a",
         "| — | proposition sans décision | réponse 22C f0505144 (table ; décision 3) ; réponse 22P cb010f4c |",
         ACC8 + "réponse 22C f0505144 (table ; décision 3) ; réponse 22P cb010f4c |",
         "Nul par placebo et banc à vérité plantée pour la loi de déférence. " + R8),
        ("T-8b",
         "| — | proposition sans décision | réponse 22C f0505144 (table ; décision 2) ; réponse 22P cb010f4c |",
         ACC8 + "réponse 22C f0505144 (table ; décision 2) ; réponse 22P cb010f4c |",
         "Prédictions « déplacement nul » récrites en équivalence. Même décision."),
        ("T-8c",
         "| — | proposition sans décision | réponse 22C f0505144 (table ; phrases 3 et 9) |",
         ACC8 + "réponse 22C f0505144 (table ; phrases 3 et 9) |",
         "Taxe de déplacement par classe d'attaquant et par budget. Même décision."),
        ("T-8d",
         "| — | proposition sans décision | réponse 22C f0505144 (table) ; réponse 22P cb010f4c |",
         ACC8 + "réponse 22C f0505144 (table) ; réponse 22P cb010f4c |",
         "Quorum comparé à un quorum de deux juges. Même décision."),
        ("T-8e",
         "| — | proposition sans décision | réponse 22C f0505144 (table ; phrase 4) |",
         ACC8 + "réponse 22C f0505144 (table ; phrase 4) |",
         "Rang sous les attaques adaptatives mesurées. Même décision."),
        ("T-8f",
         "| — | proposition sans décision | réponse 22C f0505144 (constat 3 ; décision 4) ; réponse 22P cb010f4c |",
         ACC8 + "réponse 22C f0505144 (constat 3 ; décision 4) ; réponse 22P cb010f4c |",
         "Archive du juge statistique déclarée. Même décision."),
        ("T-8g",
         "7. **Papier C.**",
         "7. **Papier C — tranché le 24 novembre (nœud 8 de la fiche, option a ; " + GO5 + ").** Les six propositions sont adoptées en bloc dans le préenregistrement du papier C, chacune contre-lue dans ce préenregistrement. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

G.append((
    "Nœud 9 de la fiche (nœud 8 de la table) — porteur de la comparaison « texte contre accès interne » : tranché, option (a)",
    "Ligne de la proposition « un seul porteur de la comparaison » (table 1.6). Statut : « proposition accordée », pour le seul porteur. Énoncé : le papier A porte la comparaison, avec un renvoi depuis le papier C ; le reste de la ligne reste sans décision. Décision : GO-2026-11-24-21, point 5.",
    [
        ("T-9a",
         "| — | proposition sans décision | réponse 22P cb010f4c (décision 3) ; réponse 22C f0505144 (décision 1) |",
         "| — | proposition accordée pour le seul porteur : le papier A porte la comparaison, avec un renvoi depuis le papier C (la pièce où l'inscrire n'est pas dite) ; le reste de la ligne, métrique d'union et partage de l'hypothèse sur la validité, reste sans décision | " + dec(9, "a") + " ; réponse 22P cb010f4c (décision 3) ; réponse 22C f0505144 (décision 1) |",
         "GO-2026-11-24-21, point 5 : recommandation (a) de la fiche, « la confier au papier A », « avec un renvoi depuis C ». La fiche ne tranche que le porteur."),
        ("T-9b",
         "Portée à quatre endroits ; aucun porteur désigné",
         "Tranché le 24 novembre (nœud 9 de la fiche, option a ; " + GO5 + ") : la comparaison est confiée au papier A, dont c'est la question centrale, avec un renvoi depuis le papier C. Texte d'avant la décision : Portée à quatre endroits ; aucun porteur désigné",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire. Le titre du nœud porte des guillemets : l'entrée vise la phrase qui le suit."),
    ]))

G.append((
    "Nœud 10 de la fiche (nœud 5 de la table) — loi sur le nombre et la diversité des moniteurs (H5) : tranché, option (b)",
    "Ligne du nombre et de la diversité des moniteurs (table 1.3). Statut : de « resserrée » à « mesure descriptive gardée ». Énoncé : plus une loi revendiquée ; la mesure de la ligne reste, descriptive ; réouverture possible après la lecture ciblée sur PDF. Décision : GO-2026-11-24-21, point 5.",
    [
        ("T-10a",
         "La loi : la sécurité croît avec le nombre de moniteurs seulement par leur diversité effective. Diversité et quorum se mesurent sous attaque ; s'ajoute une quantité rapportée, le silence commun des regards sous attaque (N-075).",
         "Plus une loi revendiquée : retirée comme loi le 24 novembre (" + GO5 + " ; nœud 10 de la fiche, option b). Son appui, un résultat cité de mémoire, n'est pas vérifié sur PDF. Lettre retirée, pour mémoire : la sécurité croît avec le nombre de moniteurs seulement par leur diversité effective. La mesure reste au plan, descriptive : diversité et quorum se mesurent sous attaque ; s'ajoute une quantité rapportée, le silence commun des regards sous attaque (N-075). Réouverture possible après la lecture ciblée sur PDF.",
         "GO-2026-11-24-21, point 5 : recommandation (b) de la fiche, « retrait comme loi maintenant, mesure gardée », « avec réouverture possible après la lecture ». La mesure gardée est celle que la ligne portait déjà."),
        ("T-10b",
         "La décorrélation des erreurs bénignes comme critère.",
         "La décorrélation des erreurs bénignes comme critère. La loi elle-même, depuis le 24 novembre.",
         "Colonne « non revendiqué à côté » : la loi retirée y est nommée."),
        ("T-10c",
         "| resserrée | `docs/decisions/decision-N-013-v1.md` 157d388e (§ 7) ; `registres/decisions.md` R-2664 ; `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v4.md` e4039549 (§ 3, point 3) | Énoncé inchangé. Quantité rapportée ajoutée. |",
         "| mesure descriptive gardée | " + dec(10, "b") + " ; `docs/decisions/decision-N-013-v1.md` 157d388e (§ 7) ; `registres/decisions.md` R-2664 ; `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v4.md` e4039549 (§ 3, point 3) | De *resserrée* à *mesure descriptive gardée* : la loi est retirée comme loi, la mesure reste. Quantité rapportée ajoutée (N-075). |",
         "Statut, décision et colonne « changement » de la ligne."),
        ("T-10d",
         "| — | proposition sans décision | réponse 22B c5980780 (table ; décision 5) ; réponse 22P cb010f4c ; réponse 22 22c56521",
         "| — | proposition accordée pour le retrait comme loi, porté sur la ligne visée ; les deux mesures de remplacement nommées ici ne sont pas dites accordées | " + dec(10, "b") + " ; réponse 22B c5980780 (table ; décision 5) ; réponse 22P cb010f4c ; réponse 22 22c56521",
         "Ligne de la proposition (table 1.3). La fiche dit « mesure gardée » sans nommer la corrélation des erreurs ni le gain d'union : je ne les écris pas comme accordés."),
        ("T-10e",
         "5. **Loi sur le nombre et la diversité des moniteurs (H5).**",
         "5. **Loi sur le nombre et la diversité des moniteurs (H5) — tranché le 24 novembre (nœud 10 de la fiche, option b ; " + GO5 + ").** Retirée comme loi, mesure gardée ; réouverture possible après la lecture ciblée sur PDF. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

ACC11 = "| — | proposition accordée (lettre à venir : adoptée avec le programme v4, en un seul chantier ; d'ici là, rien ne change au programme v3 ni aux lignes visées) | " + dec(11, "a") + " ; "
G.append((
    "Nœud 11 de la fiche (nœud 10 de la table) — forme commune de thèse ; loi de la référence honnête étendue : tranché, option (a)",
    "Deux lignes de propositions (table 1.6). Statut : de « proposition sans décision » à « proposition accordée ». Énoncé : inchangé ; la lettre vient avec le programme v4. Décision : GO-2026-11-24-21, point 5.",
    [
        ("T-11a",
         "| — | proposition sans décision | réponse 22P cb010f4c (décision 1) |",
         ACC11 + "réponse 22P cb010f4c (décision 1) |",
         "Forme commune de thèse pour les trois papiers. GO-2026-11-24-21, point 5 : recommandation (a) de la fiche, « adopter avec le programme v4 »."),
        ("T-11b",
         "| — | proposition sans décision | réponse 22P cb010f4c (décision 2) ; réponses 22A, 22B, 22C |",
         ACC11 + "réponse 22P cb010f4c (décision 2) ; réponses 22A, 22B, 22C |",
         "Loi de la référence honnête étendue à toutes les références. Même décision."),
        ("T-11c",
         "10. **Forme commune de thèse ; loi de la référence honnête étendue à toutes les références.**",
         "10. **Forme commune de thèse ; loi de la référence honnête étendue à toutes les références — tranché le 24 novembre (nœud 11 de la fiche, option a ; " + GO5 + ").** Adoptées avec le programme v4, en un seul chantier. Texte d'avant la décision :",
         "Le nœud est marqué tranché ; son texte d'origine reste, pour mémoire."),
    ]))

G.append((
    "Ligne du lemme d'additivité dans son application au contrôle (table 1.1), et les deux reprises de la vérification de la table",
    "Statut : revendiquée (application), inchangé. Énoncé : celui de l'erratum 1 du programme v3, variante B, le temps seul ; la portée « le temps et les agents » vient en suite conditionnelle. Décision : GO-2026-11-24-18 ; GO-2026-11-24-21, point 8, pour la portée. Reprise 1 : la fiche du nœud du lemme est citée sur la ligne (T-L4). Reprise 2 : la condition de la règle R8 est écrite sur la ligne (T-L2, T-L3).",
    [
        ("T-L1",
         "(conservation du déplacement cumulé sous fragmentation) |",
         "(conservation du déplacement cumulé sous fragmentation ; portée : le temps seul) |",
         "GO-2026-11-24-21, point 8 : « (B) pour le premier papier, puis (A) une fois la première mesure faite : go ». B est la variante « le temps seul » de l'erratum 1 du programme v3."),
        ("T-L2",
         "**Énoncé exact à venir par l'erratum 1 du programme v3 (Fable, en cours)** ; il est rédigé par Fable et contre-lu avant tout usage.",
         "**Énoncé (erratum 1 du programme v3, variante B, le temps seul).** " + ENONCE_B + " Portée : le temps seul, au papier A, pour le premier papier ; la portée *le temps et les agents* (variante A du même erratum) vient en suite conditionnelle, une fois la première mesure faite (GO-2026-11-24-21, point 8). D'ici là, entre agents, rien n'est revendiqué ; la prévision sur la somme globale (H3) garde son statut. C'est une prévision à éprouver, non un constat ; sa mesure est à préenregistrer. La règle de lecture à trois issues (tenue, réfutée, indéterminée), les deux modes d'induction, le témoin à consigne de fragmentation sans sabotage exécuté et les cinq hypothèses sont ceux de l'erratum 1, section 1. Antériorité (règle R8) : la veille du 24 novembre conclut *Voisins seulement — non trouvé dans les pièces lues* ; cela ne dit pas que le champ est vide, et des lectures restent. Voisin le plus proche, à citer d'emblée : Makins et al. 2026, en boîte noire.",
         "L'énoncé est copié de l'erratum 1 du programme v3 (" + "`" + ERR1 + "`" + ", 5b8be265), section 1, variante B, par programme. Portée : GO-2026-11-24-21, point 8. Antériorité : verdict de la veille, tel que l'erratum 1 le rapporte (section 3)."),
        ("T-L3",
         "Toute phrase sur cette revendication avant l'énoncé exact contre-lu.",
         "Toute phrase de nouveauté sur la forme mesurée : son antériorité n'est pas établie (règle R8). La conservation chez un saboteur réel ; une conservation lue sur le seul organisme à consigne cachée, présentée comme une propriété des sondes. Toute revendication entre agents avant la suite conditionnelle. Tout usage de l'énoncé avant la vérification des corrections de l'erratum 1 par son contre-lecteur (GO-2026-11-24-18).",
         "Les deux phrases à ne pas écrire sont celles de l'erratum 1 du programme v3 (section 1). GO-2026-11-24-18 exige un énoncé « contre-lu avant tout usage »."),
        ("T-L4",
         "go.md (commit 5fd8fc305) GO-2026-11-24-18 ; decisions.md R-5265 ; go.md GO-2026-11-22-42, GO-2026-11-22-64",
         "go.md (commit 5fd8fc305) GO-2026-11-24-18 ; decisions.md R-5265 ; go.md GO-2026-11-22-42, GO-2026-11-22-64 ; go.md GO-2026-11-24-21 (point 8 : portée) ; erratum 1 du programme v3 `" + ERR1 + "` 5b8be265 (sections 1, 3 et 5) ; fiche du nœud `docs/notes/dossier-entretien-2026-12-01-v1/fiche-noeud-lemme-application-v1.md` 53396904 ; veille d'antériorité `docs/notes/dossier-entretien-2026-12-01-v1/rapport-veille-anteriorite-lemme-v1.md` d38cd21c",
         "Reprise 1 de la vérification de la table : citer la fiche du nœud du lemme. S'ajoutent la décision de portée, l'erratum et la veille. Empreintes relevées par `sha256sum` ; la fiche du nœud et le rapport de veille ne sont pas lus."),
        ("T-L5",
         "son énoncé exact vient par l'erratum 1 du programme v3.",
         "son énoncé exact est celui de l'erratum 1 du programme v3, variante B, le temps seul : voir la ligne du lemme en table 1.1.",
         "Section 2 : l'énoncé n'est plus à venir."),
        ("T-L6",
         "Reste un travail d'écriture : l'énoncé exact, par l'erratum 1 du programme v3 (Fable, en cours), contre-lu avant tout usage.",
         "L'énoncé exact est écrit : erratum 1 du programme v3, variante B, le temps seul (GO-2026-11-24-21, point 8), porté sur la ligne du lemme en table 1.1 ; la portée *le temps et les agents* vient en suite conditionnelle. Antériorité : voisins seulement, non trouvé dans les pièces lues ; aucune phrase de nouveauté (règle R8).",
         "Point L de la section 3.2 : le travail d'écriture annoncé est fait."),
    ]))

n_entrees = sum(len(g[2]) for g in G)

tete = """# Erratum 1 de la table des revendications en vigueur, v2 corrigée (v1)

Écrit le 2026-11-24 vers 18:50Z (`date -u` relevé à 18:40Z au début du travail, à 18:47Z à l'écriture). Rédacteur : Claude Fable 5.2 (`claude-fable-5-2`), effort élevé, sur la consigne `docs/notes/dossier-entretien-2026-12-01-v1/consigne-fable-errata-table-et-programme-v1.md` (80c156c7). Pièce de travail : ni scellée, ni contre-lue à l'écriture.

**Verdict.** %d entrées enregistrent les décisions de Lazar du 24 novembre sur la table. Neuf nœuds sont tranchés, deux restent ouverts, et la ligne du lemme porte son énoncé exact. La table n'en prend aucune : chaque entrée cite la décision qui la commande.

**Attention : deux numérotations.** Les mots de Lazar suivent les numéros de la fiche des onze nœuds, non ceux de la section 3.1 de la table. Correspondance, fiche puis table : 1 et 1 ; 2 et 4 ; 3 et 9 ; 4 et 11 ; 5 et 2 ; 6 et 3 ; 7 et 6 ; 8 et 7 ; 9 et 8 ; 10 et 5 ; 11 et 10. Les nœuds ouverts, « 5 et 7 », sont la co-élévation entre copies et la thèse du papier B. C'est ma lecture ; ses indices sont en fin de fichier.

**Décisions enregistrées** (`registres/go.md` sur `origin/main`, commit `138bb1070`, SHA-256 du fichier d231e77a) :
- GO-2026-11-24-21, point 5 : les onze nœuds selon les recommandations de la fiche, « les nœuds 5 et 7 après la note du collisionneur » ; point 8 : portée du lemme, « (B) pour le premier papier, puis (A) une fois la première mesure faite : go ».
- GO-2026-11-24-31, point 4 : nœuds 5 et 7, option (b), « restent ouverts (concordance indirecte de la note du collisionneur) ».
- GO-2026-11-24-18 : le lemme est revendiqué dans son application au contrôle de l'intelligence artificielle ; énoncé à l'erratum 1 du programme v3.

**Lu.** La table corrigée, en entier (cefd3d79). La fiche des onze nœuds (72784e0f). La note de sortie du collisionneur sur les revendications, en entier (32a2ffc2). Le programme v3 scellé provisoirement (fcc27171), en entier. Son erratum 1, version 3, en entier (5b8be265). Les trois lignes d'accord ci-dessus, et GO-2026-11-24-22 pour l'erratum du programme. Le résumé de `CLAUDE.md`.

**Non lu.** La fiche du nœud du lemme et le rapport de veille d'antériorité : empreintes relevées, contenu non ouvert (hors de ma liste). La pièce de vérification de la table, d'où viennent les deux reprises : je les tiens de la consigne. La vérification des corrections de l'erratum du lemme. GO-2026-11-24-15, que la fiche cite. Aucune décision de `docs/decisions/`. Aucun fichier de résultats, de diagnostic, de scores, de verdict ou de lecture ; rien sous `coffre/`.

## Forme, pour le programme d'application

Cible : `%s` (cefd3d79e10526bce7cada17008a8e69ef29a7caa75af8fc8cda8372e68c2fe8).

Même forme que l'erratum 1 du programme v3. Un bloc tient en trois lignes consécutives : l'identifiant en gras puis le texte ANCIEN entre guillemets français ; le texte NOUVEAU, de même ; la raison. Une ligne vide sépare les blocs. Le texte va du premier guillemet ouvrant qui suit l'étiquette au dernier guillemet fermant de la ligne ; l'espace simple qui suit l'un et précède l'autre n'en fait pas partie. Aucun texte ANCIEN ni NOUVEAU ne porte de guillemet français ni de saut de ligne : dans les textes neufs, les mots cités sont en italique. Les lignes « Ligne après application » résument ; elles ne s'appliquent pas.

Vérifié par programme, en lecture seule : chaque ANCIEN figure une fois dans la cible ; les ANCIEN ne se recouvrent pas ; appliquées dans l'ordre par simple remplacement, les entrées trouvent chacune leur texte une fois. L'empreinte de la table après application est donnée en fin de fichier.

## Entrées

""" % (n_entrees, CIBLE)

corps = []
for titre, resume, entrees in G:
    corps.append("### " + titre + "\n")
    if resume:
        corps.append("Ligne après application. " + resume + "\n")
    for ident, ancien, nouveau, raison in entrees:
        for s in (ancien, nouveau):
            assert '«' not in s and '»' not in s and '\n' not in s, ident
        corps.append("**%s.** ANCIEN : « %s »\nNOUVEAU : « %s »\nRaison : %s\n" % (ident, ancien, nouveau, raison))

# Vérification et empreinte après application
t = open(RACINE + CIBLE, encoding='utf-8').read()
assert hashlib.sha256(t.encode('utf-8')).hexdigest().startswith('cefd3d79')
spans = []
for titre, resume, entrees in G:
    for ident, ancien, nouveau, raison in entrees:
        assert t.count(ancien) == 1, (ident, t.count(ancien))
        i = t.find(ancien)
        spans.append((i, i + len(ancien), ident))
spans.sort()
for a, b in zip(spans, spans[1:]):
    assert a[1] <= b[0], (a, b)
u = t
for titre, resume, entrees in G:
    for ident, ancien, nouveau, raison in entrees:
        assert u.count(ancien) == 1, ('séquentiel', ident, u.count(ancien))
        u = u.replace(ancien, nouveau)
assert u.count('\n') == t.count('\n')
h_apres = hashlib.sha256(u.encode('utf-8')).hexdigest()

fin = """## Ce qui reste ouvert

1. **Les nœuds 5 et 7 de la fiche** (co-élévation entre copies ; thèse du papier B). Ouverts par GO-2026-11-24-31, point 4. Un collisionneur sur une question qui nomme les copies multiples est proposé après l'entretien (note de sortie du collisionneur sur les revendications). Dire si la concordance indirecte suffit reste à Lazar.
2. **Ma lecture des numéros.** Les deux lignes d'accord disent « de la table », mais leurs numéros sont ceux de la fiche. Indices : la fiche recommande (b) pour ses nœuds 5 et 7, en attendant la note du collisionneur ; cette note traite « les nœuds 5 et 7 de la fiche » ; la consigne lie ces deux nœuds aux copies multiples. Si Lazar visait la section 3.1 de la table, les nœuds ouverts seraient la loi sur les moniteurs et le papier C : les entrées T-5, T-7, T-8 et T-10 seraient à reprendre.
3. **Deux choix de tenue de table, qui ne sont pas des décisions.** Un sixième statut, « proposition accordée » (T-0a), pour une proposition accordée dont la lettre vient par une pièce à écrire. La transposition du jeton à l'action passe de « revendiquée » à « resserrée » (T-3c), par la définition de ce statut. Le contre-lecteur peut préférer d'autres mots.
4. **Écritures que ces décisions commandent, et que cet erratum ne fait pas.** Un erratum de N-076 pour la clause d'horizon (nœud 1). Un erratum du programme v3 pour trois passages de sa section 5 : « plate » sans la condition d'indépendance (H3), « angle mort identifié » (Tr), la loi sur les moniteurs (H5) ; l'erratum 2 du programme ne porte que le calendrier. La réécriture de N-069 (nœud 6). Le préenregistrement du papier C, qui porte les six propositions (nœud 8). Le renvoi depuis le papier C vers le papier A, et la pièce où l'inscrire (nœud 9). Le programme v4 (nœud 11). L'index de `CLAUDE.md`, non touché.
5. **Mesure gardée de la loi sur les moniteurs.** La fiche dit « mesure gardée » sans la nommer. J'ai gardé celle que la ligne portait. Les deux mesures que la proposition nommait (corrélation des erreurs, gain d'union) ne sont pas écrites comme accordées.
6. **Porteur de la comparaison.** La fiche confie toute la comparaison au papier A. La proposition la partageait (détection au papier A, corruptibilité au papier C). J'ai écrit la lettre de la fiche ; le reste de la proposition reste sans décision.
7. **Suite conditionnelle du lemme.** Les mots de Lazar sont « une fois la première mesure faite ». Rien ne dit si la mesure doit seulement être faite, ou la conservation tenue, ni si le passage à la portée « le temps et les agents » demande un mot neuf.
8. **Vérification de l'erratum 1 du programme.** Cet erratum se dit lui-même à vérifier par son contre-lecteur avant tout usage. Un fichier de vérification existe au dossier ; il est hors de ma liste et je ne l'ai pas lu. La ligne du lemme garde donc la réserve (T-L3).
9. **Les deux reprises.** Je n'ai pas lu la pièce de vérification de la table. J'ai compris : citer la fiche du nœud du lemme sur sa ligne ; écrire sur cette ligne la condition de la règle R8 (« non trouvé dans les pièces lues » ne dit pas « trou du champ » ; aucune phrase de nouveauté). À confirmer contre la pièce.
10. **Section 2 de la table, pour le jury.** Elle ne reçoit pas de ligne neuve pour la loi sur les moniteurs, les mots « angle mort identifié » et le bras de l'adversaire entraîné : la forme de cet erratum remplace du texte, elle n'ajoute pas de ligne. À porter dans une version suivante de la table.
11. **La marque « sous simulation » de la courbe selon le nombre d'agents.** Aucune décision lue ne la lève. Elle reste.

## Empreinte après application, et confiance

Table après application des %d entrées, dans l'ordre, par simple remplacement : `%s`. Le fichier appliqué n'est pas écrit : l'empreinte est calculée en mémoire.

**Confiance.** Exactitude des textes ANCIEN : 0,97, vérifiée par programme. Fidélité aux recommandations de la fiche : 0,85. Lecture des numéros (fiche, non table) : 0,9. Choix de statuts : 0,7. Compréhension des deux reprises : 0,7. Ensemble : 0,8.
""" % (n_entrees, h_apres)

texte = tete + "\n".join(corps) + "\n" + fin
open(RACINE + SORTIE, 'w', encoding='utf-8').write(texte)
print(n_entrees, 'entrées ;', h_apres)
print(hashlib.sha256(texte.encode('utf-8')).hexdigest())
