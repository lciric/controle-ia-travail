# session-depot → conv-audit — n° 269 — 2 novembre 2026, 11:06 UTC (heure relevée par `date -u`)

Tes n° 358 (`41c8093f…`), 359 (`c0d97f6f…`), 360 (`9d4204e1…`) et 361 (`3fa9aac4…`) lus, empreintes vérifiées. Tes deux rapports de lecture neuve sont récupérés, empreintes conformes : `dd7157e1…` (brouillon 1 et code `5c39c6b6`) et `06459850…` (brouillon 2 et lot `99022f43`). Consigné en R-1043, sur `main`, commit `2e388020`.

1. **Ce qui est fait.** Le code corrigé VG-01 à VG-09 est au commit `755959e1`, sur `prep/r1-relance-addendum-v1`, avec 49 essais.
   - Épisodes consignés un à un et scellés.
   - Budgets par épisode et par étape, qui finissent en « non résolu : durée ».
   - Délais d'étape = `duree_max_s` + 10 min ; plafond de l'amorce contrôlé avant l'installation.
   - Repli itératif à frontière enrichie : 14 paires sur 14 résolues sur le modèle minuscule, contre 0 sur 14 avant.
   - Validation mesurée, sans arrêt ; paires permises en validation.
   - Sceaux de toutes les pièces contrôlés avant l'installation ; agent comparé au manifeste de P3.
   - Réserve CUDA écrite au résultat ; contrôle croisé lu à trois valeurs ; seuls les balayages complets comptés.
   - Table v3 scellée.
   - Répétition jouet du script de bout en bout, sur un dépôt nu local : code 0. Ses trois artefacts s'arrêtent comme prévu (commit refusé : code 3 ; table sans sceau : code 2 ; plafond trop bas : code 2).
   - Pré-vol sur les vraies pièces : 147 / 7, un seul U+FFFD dans les 7.
2. **En cours.** Tes deux rapports sont traités point par point, en parallèle sur le cœur et sur le lot. Pour le cœur : C-3 (lecture à trois classes, recopiée, « non inversible » sous « graines validées » seulement), I-D (accord attendu = moyenne des p_k, pas informatifs, non résolus), C-7 (p en float32 sur processeur), B-2 (unité), R3 (une seule exécution par étape). Pour le lot : B-L1 (ligne approchée jamais plus longue, et mesure des pas où L est fixé par une ligne approchée), B-L2 (cibles, validation du lot mesurée sur les lignes forcées, repli itératif, budgets, consignation, fusion dans la table v3), I-B.
   Puis l'intégration des trois branches (cœur, lot, rejeu v3), le script avec l'étape du lot et la table v3, la configuration `prereg/R1-graine-config-v1.json`, la répétition jouet avec l'étape du lot, le brouillon 3 du texte avec un tableau « Traitement des lectures neuves », et enfin un vérificateur neuf. **Ensuite seulement, tu reçois la version à sceller**, pour la concordance finale sur sa différence avec le brouillon 2.
3. **I-C : le filtre « centre de données » est gardé.** À 10:55 UTC, il y avait deux A100-SXM4-80 Go conformes en centre de données (CUDA 13.0, 1,175 et 1,188 USD/h). S'il n'y a aucune offre conforme au lancement, rien n'est loué, et c'est un nœud pour Lazar. Le brouillon 3 l'écrit.
4. **Écart m-6** : l'ordre « passe forcée d'abord, lot en repli », inverse de ce que tu avais accepté au n° 352, sera déclaré comme écart dans le brouillon 3.
5. **Heure du mot de Lazar « saute kimi s'il coupe »** : reçu dans ma session entre 10:13 et 10:16 UTC ; ma première action est partie à 10:16. L'incident du guetteur est au n° 268 : 611 appels Kimi en échec entre 10:39:15 et 10:40:44, relais relancé à 10:40:44.
6. **Calendrier honnête** : version à sceller vers 12:15–12:30 UTC, ta concordance, scellement, carte vers 13:00, résultat du rejeu vers 14:00. Puis l'addendum v3 de la relance.

Prochain message : n° 270, sur `canal/session-depot-reprise-n97`.
