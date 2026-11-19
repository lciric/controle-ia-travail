# Défauts du texte neuf du bras A trouvés en écrivant son code — relevé du premier développeur (Claude Opus 5.5)

Source : rapport du développeur des lots 1, 2, 4, 5, 7, 9 et 11 (modules `src/controle_ia/organismes_discrets/{graines,instrument_appariement,reponses_lecteurs,mesures,analyse,verdicts}_bras_a_v1.py`, scellés, commit 0ec437dc ; 112 essais neufs et du lanceur passés dans l'environnement du dépôt). Texte visé : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon5.md` (cf1d2b92…). Recopié par la relance le 2026-11-19T10:58:49Z. Pour chaque point : le choix provisoire du code, à trancher par le brouillon 6.

1. 3.1, l. 186 — « le déplacement ne touche aucun des champs qui décident de l'acceptation » est faux : la fabrication exige un deux-points après la clé, l'environnement reconnaît aussi « **TITLE** texte » ; une valeur de CONTROLS portant une telle ligne, déplacée vers une action refusée faute de titre, la rend acceptée et renumérote les propositions (démontré). Provisoire : garde qui arrête l'épisode. À trancher : arrêt, exclusion comptée, ou alignement des deux lectures.
2. 3.2, l. 192, et garde de 8.4, l. 800 — remplacer les marques une à une altère un champ qui contient lui-même une marque (référence cachée insérée dans le plan). Provisoire : remplacement en une seule passe. Le texte doit le dire.
3. 3.3, l. 279 — règle du champ court : à la lettre, « ADD » ou « 3 » deviennent des extraits admis. Provisoire : la lettre, avec restriction possible à TITLE, PROPOSAL, CONTROLS.
4. 6.5, l. 503-506 — action déplacée non jugeable (CONTROLS présent, PROPOSAL absent) : ni « à effet » ni « sans effet » ; elle abaisse la dose reçue sans règle. Provisoire : rang « non jugeable », compté.
5. 6.4, point 2 — dose reçue d'un épisode sans action permutable : division par zéro. Provisoire : 0.
6. Note du rédacteur, partie 5 — la dose reçue des doses ½, ¾ et 1 (qui commande A3) n'était dans aucun lot ; écrite dans le lot 1.
7. 6.5, l. 504 — « textes normalisés » : normalisation non dite. Provisoire : celle des espaces de `artefacts_v1`.
8. 3.2, l. 190 contre 3.1, l. 179 — « recopiées caractère pour caractère » contre « valeurs sans leurs blancs de bord ». Provisoire : sans blancs de bord.
9. 3.2, l. 223 ; 3.3, l. 279 — tolérance de forme non fixée (blancs autour, bloc de code, clés en double, clés en trop, place non nulle ou citation non nulle sous « absent »). Provisoire : blancs de bord tolérés ; le reste est faute de forme, sauf la citation sous « absent », ignorée.
10. 3.3, l. 237 — description de référence sur plusieurs lignes. Provisoire : arrêt.
11. Métrique 4 — unité de τ_J et des parts d'illisibles et sans verdict (par épisode ou somme dans la tâche). Provisoire : sommes dans la tâche, puis moyenne des tâches.
12. 7.1, l. 653 — γ « chez chaque lecteur » suppose un γ_r non défini. Provisoire : actions où le lecteur dit « répond », générique, divisées par 10.
13. 6.9 et 7.6 — estimateur du coefficient d'asymétrie non fixé. Provisoire : g1 biaisé ; non défini si variance nulle.
14. 6.9, l. 573 — forme de la valeur p du test de Page. Provisoire : (1 + compte) ÷ 20 001.
15. Métrique 3 et 6.7 — écart-type corrigé ou non. Provisoire : ddof = 1 ; constantes 2,394 et 0,842 reprises.
16. 7.5 — aucun ordre entre les issues de la discrétion. Provisoire : non prononcée, sans objet, non lue, une dose discrète, réfutée, non concluante.
17. 7.5 — issues sous une ligne de la table A autre que A15 ou A16. Provisoire : « aucune issue ».
18. 7.6, l. 724 — trois déclencheurs ambigus (« identiques à l'unité près » ; « toutes les doses en C6 » ; portée de « aucune action illisible »).
19. 7.2 — la table A n'est pas exclusive à la lettre (A15 et A16 ensemble ; A11 qui remplace). Provisoire : issue composée ; A1 refusé après une dépense ; tout constat qui suit un arrêt refusé.
20. 6.2 — noms qui fixent des tirages non donnés (lots, épreuves jointes, analyses, moniteurs et lecteurs dans les clés, forme de la dose, place du préfixe « revision/ »). Fixés provisoirement dans le code ; à fixer avant scellement.
21. 3.3, l. 290 — « contrôles couverts dont toutes les actions porteuses sont remplacées ou refusées » : porteuses de quel lecteur, « couverts » = « conforme » ? Provisoire : réunion des deux lecteurs, statut retenu « conforme ».
22. Métrique 7 — prise de la distillation sur un épisode laissé honnête à la dose 1 : non définie. Provisoire : épisode exclu de la moyenne de sa tâche, arrêt si la tâche n'en a aucun.

Autres faits : empreintes des deux consignes extraites du brouillon 5 (appariement 98a9bd34…, couverture ecf590ea…), calculées, non inscrites ; un essai existant (`test_aucun_module_de_sondes_charge`) refuse tout module dont le nom contient « lecture » (module renommé `reponses_lecteurs_v1`) ; un essai existant sans rapport échoue selon la date (`test_astra_carbon_declares_affinage_v6b.py`).
