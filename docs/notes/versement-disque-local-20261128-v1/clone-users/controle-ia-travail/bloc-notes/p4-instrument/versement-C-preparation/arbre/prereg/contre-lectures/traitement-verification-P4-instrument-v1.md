# Traitement de la contre-lecture 2 de P4-instrument (vérification des corrections des brouillons 2 et 3) — v1

Session 14, 2026-10-20 vers 13:49 UTC. Rapport : `…/p4-instrument/verification/verification-corrections-brouillons2-3-P4-v1.md`
(`9c94c2205b3f08e522917fd7c078748f8dc583fe4242ed9a26c325af71e7228e`), sous-agent neuf, sur le brouillon 3
(`2ec30d6860838f5b9e9c2e637906101a8b0d2ad2a1df2cfdc355bf552374cd4c`) : « scellable après corrections », trois majeurs, dix
mineurs. Les treize constats sont acceptés. Corrections portées au brouillon 4
(`…/p4-instrument/P4-instrument-v1-brouillon4.md`). Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

| constat | décision | où |
|---|---|---|
| VP3-01 (majeur) : registre des GO à quatre colonnes, la garde bloque ; formes de dépense non lisibles | accepté. Registre réparé hors du texte : lignes GO-2026-10-20-01 à 08 remises à huit colonnes, contenu inchangé (R-281) ; `lire_go` et `decider` rejoués, test du registre réel repassé. Dans le texte : GO cité par la commande, GO-2026-10-20-07 seul (type « calcul », échéance 2026-11-30 dans sa colonne) ; plafond par lancement lu dans sa colonne « plafond », qui doit commencer par « 10 USD par lancement » ; plafond de la phase vérifié par la session à l'accord ; formes exactes de la révocation ; garde gelée rejouée, jamais contournée | en-tête « GO et dépense » ; Plan d'analyse, point 7 ; Liste d'arrêt |
| VP3-02 (majeur) : l'artefact (i) est sans effet si l'espace passe par le texte (le gabarit rogne) | accepté : identifiant 220 inséré dans les identifiants du contexte, après `<|end_header_id|>` et l'identifiant 271 du premier message de l'utilisateur ; garde « un identifiant de plus, à cette place, à chaque pas », sinon épreuve « non éprouvée », niveau 2 désactivé, réserve ; tests cas sain et artefact (espace dans le texte d'un gabarit qui rogne) | Garde d'identité, épreuve ; Tests |
| VP3-03 (majeur) : « au-dessous » fondé sur une symétrie fausse des aires du plancher | accepté : « au-dessous » sur le quantile 0,05 des 200 aires ; 1 − quantile 0,95 rapporté, sans effet ; « symétrique par construction » retiré, fait corrigé (`evaluation.py` l. 79 et 81, `harnais/sondes.py` l. 75-76) ; « au-dessus » et « au-dessous » exclusifs par construction. Plancher haut : la session retient le critère miroir « quantile 0,05 au-dessous de 0,20 » (seuils de la note gardés) et ajoute en descriptif la part des directions à \|aire − 0,5\| > 0,15, jamais une ligne | Métrique, « Plancher » ; Seuil ; P4-C1 ; L9, L10, L11 ; descriptives ; Tests |
| VP3-04 : réserve « plancher haut » discordante | accepté : règle unique dans le Seuil (L6 à L8 « la sonde les dépasse » ; L9 « la sonde est au-dessous d'elles, de signe inversé » ; L1 à L5 aucune ; L10 « ni au-dessus ni au-dessous ») ; cinq passages mis d'accord | Seuil ; Métrique ; Plan, point 5 ; L6 à L10 ; Réserves |
| VP3-05 : R-275 et R-279 corrigent R-266 | accepté : plancher apparié du projet précédent cité (chemins, empreintes, médianes 0,6646 et 0,8856 contre 0,272), recette différente, branche C3 rouverte ; a priori interne déclaré, non opposable ; registres relus au brouillon 4 | Documents qui font foi ; A priori |
| VP3-06 : deux trous de la table | accepté : L3 couvre M5 en échec ; L1 couvre une lecture refusée par une garde du mode décisif ; l'attente du verdict complété est un report | Critères de lecture ; Plan, point 2 ; Liste d'arrêt |
| VP3-07 : B′ et garde d'affect | accepté : B′ = « urban », « indoor », « outdoor », dans cet ordre (validés par le vérificateur neuf) ; liste d'arrêt : adjectifs de B et de B′ | Métrique, « Phrases » ; Liste d'arrêt |
| VP3-08 : frontière des 95 % | accepté : « au moins 403 des 424 sondes légères (95 %, arrondi au-dessus) » ; test 403 contre 402 | Seuil ; Garde d'identité ; Tests |
| VP3-09 : ligne du verdict complété en texte libre | accepté : cellule qui commence par « **Verdict complété de P3 scellé** », chemin et empreinte égale au sceau ; artefact testé | Plan, point 2 ; Tests |
| VP3-10 : plan v1 contraire au texte | accepté : le texte prime ; écarts du v1 listés ; plan v2 aligné avant le candidat ; le rédacteur du module a le texte pour seule source | Chaîne de lancement |
| VP3-11 : citations et nombres | accepté : Σ (l. 72-74 ; l. 117-120 et 80-81 ; rang déficient) ; planchers de P3 par jeu avec leurs clés ; 430 colonnes ; clés sous `resultat.` ; plancher d'une séparation sur les séparations repliées ; ex aequo du rang ; tokeniseur cité en entier | Données lues ; Nombres connus ; Métrique ; descriptives |
| VP3-12 : quatre décisions non écrites | accepté : GP4-07 (MC-2 le dit, le candidat l'écrit) ; A5 exclue ; mesures de conception admises au titre de R1 ; suite complète des tests sur l'instance | Mesures de conception ; Pare-feu ; en-tête « Tests attendus » |
| VP3-13 : puissance lisible comme celle de P3 | accepté : « ordre de grandeur pour C1 de P4, sous l'hypothèse d'une erreur type égale à celle réalisée par P3 ; ce n'est pas l'aire minimale détectable de P3, qui relève de l'addendum 2 ; sans effet sur P3 » | Plan, point 5 ; P4-C1 |

La vérification des corrections du brouillon 4 se fera au candidat, par un sous-agent neuf (contre-lecture 3), avec la
fidélité du module au texte.
