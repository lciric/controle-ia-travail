# Contre-lecture de la version qui fera foi v2 du crible (v) : tour 2 (tour différentiel court, R-2993) : lecteur C

Lecteur : modèle C, neuf (n'a écrit aucune pièce). Pièce lue : `crible-v-version-foi-v2.md`, `2b99627dd378564dba816bc10593cdb0d06d77a3fdd4eb9e3cca022c76838715` (égale à son compagnon). Précédente : `crible-v-version-foi-v1.md`, `ee7aab415c2a07d38967cfcd5d987ee5a5ba7bdc23b700e0a369b59ca96f4330`. Rapport du tour 1 : `5c67b370b6a8f21a2dac30ad692a1993e4ee5a9a666bb2c07a9a701e719609d5`. Lecture du 2026-11-16, vers 23:34Z à 23:36Z (`date -u`). Issue du pilote non ouverte ; rien sous `diag/`, `runs/`, `donnees/` ; aucun appel, aucune dépense, aucun fichier existant modifié.

Note : la consigne décrit la pièce comme « v1 » ; le fichier présent et à lire est la v2, qui applique le tour 1. J'ai donc contrôlé la v2 contre la v1 (le tour 1 ayant déjà jugé la v1 contre le brouillon 9).

## Verdict : **scellable** (aucune correction exigée ; deux remarques facultatives)

## 1. Correction du tour 1 appliquée fidèlement
- Une seule correction exigée au tour 1 (M1, mineure). Le nouveau paragraphe « Préséance des chiffres de devis » de la v2 est égal, au caractère près (589 caractères, comparé par programme), au « nouveau » du rapport du tour 1 ; il est présent une fois, inséré juste avant la ligne « Mentions de rédacteur » (R-2992, point 0), qui existe une fois dans la v1 et une fois dans la v2, reprise telle quelle. Aucune section gelée touchée.
- La sous-section citée par la préséance (« Devis refait sur le pilote MR-2 (fait foi) ») existe (l. 523) ; les chiffres périmés qu'elle désigne (« ≈ 50 à 53 % », « ≈ 48 USD », « ≈ + 73,30 », « 0,71 à 0,75 ») sont bien dans les sections laissées gelées.
- Le « 0,71 à 0,75 » garde déjà sa réserve (8) ; cohérent.
- F-1 et F-2 (facultatives) non appliquées, dit dans l'entrée « Contre-lecture 10 » ; acceptable (la mère reçoit F-1 comme action avant inscription de κv2).

## 2. Différentiel : rien d'autre
- `diff -u` v1 → v2 refait : corps égal à `diff-crible-v-foi-v1-vers-foi-v2.txt` (`e1a342a3…`) ; `diff -u` brouillon 9 → v2 égal à `diff-crible-v-b-vers-foi-v2.txt` (`6849aa14…`) (comparaison par programme, en-têtes exceptés). Les empreintes des deux différentiels, de la pièce et du programme d'application (`8502a20407ad…`) sont égales à leurs compagnons.
- Les zones nouvelles de la v2 par rapport à la v1 sont exactement six : titre ; ligne d'en-tête « Version qui fera foi v2 » ; Statut ; paragraphe M1 ; tête de la section « Contre-lecture » ; entrée « Contre-lecture 10 ». Aucune ne touche une prédiction, un seuil, une graine, une ligne d'arrêt, le devis, les lignes de GO ni l'annexe. Prédictions V1 à V7, devis, durées, enveloppe : identiques à l'octet à la v1, donc au brouillon 9 hors les écarts déjà jugés au tour 1.
- Le programme d'application vérifie les empreintes de la v1 et du rapport, lit le couple dans le rapport, écrit en mode « x » (cible neuve) : conforme à R12.
- Validateur `controle_ia.prereg.problemes` sur la v2 : liste vide. Aucun identifiant de modèle (seules les clés `opus55`, `fable52`, `argon`, `astra`, gelées). Les mentions de rédacteur de l'entrée 10 (rédacteur du modèle C, écart de rôle déclaré par rapport à R-2982) sont franches.

## 3. Vérifications que la correction a pu déranger
- Nombres du devis (attendus par appel, parts sur crédits de Claude 0,84 / 0,73 et hors crédits, pires cas 196,60 et 204,67, B_a = 900 s, M, garde, enveloppe 474,67 et 1 323,67 de GO-2026-11-15-06 d'échéance 2026-11-30) : inchangés par octet depuis la v1, que le tour 1 a recalculés ; la correction n'y touche pas, donc rien à refaire. Les deux parts restent séparées.
- Le paragraphe M1 ne contredit aucune ligne : il ne change aucun attendu, il donne la préséance au devis refait.

## 4. Remarques facultatives (ne bloquent pas ; je ne les exige pas)
- **F-3** : le titre de la section « Écarts au brouillon 9 (version qui fera foi v1) » garde « v1 » dans la v2 ; l'entrée 10 le dit (« la liste reste celle de la v1 ; les écarts propres à la v2 sont les six couples »). Sans incidence ; pourrait se préciser lors d'une version suivante.
- **F-1 (reprise)** : avant d'inscrire κv2, lire sur la pièce de dépense du pilote les coûts par appel de Pr-1, la ligne κv2 affirmant l'absence de dépassement (réserve (4) renvoie déjà à cette lecture).

## 5. Points pour la mère
1. La pièce peut être scellée par `sceller_prereg` et copiée sous `prereg/` telle quelle (R1, R2) : tour différentiel 2 passé, aucune correction exigée.
2. Toujours bloquant avant tout lancement (inchangé, déjà dans la pièce) : quatre durées du journal d'états de la machine du pilote à relever (budget « non lançable » sinon) ; code neuf contre-lu ; sonde neuve et essai à blanc ; lignes κv1 et κv2 ; phrase de Lazar. Ordre d'inscription des cinq cribles à décider (1 323,67 > 1 275 USD ; le dernier est un nœud de Lazar). Rien n'interdit de lancer avant le 21 : seule la liste ci-dessus compte, et l'accord expire le 30 novembre.
3. V7 : à confirmer gelée (R-2993 ne nomme que V1 à V6) ; budget de durée optimiste (états hors règle et 790 s) : décision de la mère ou de Lazar ; placebo à remesurer à l'étape 0.
4. Écart de rôle : correction écrite par un rédacteur du modèle C au lieu du modèle A (R-2982) ; à dire tenu ou non.

## 6. Incidents
Aucun. Une exécution en lecture de `controle_ia.prereg.problemes` (liste vide) ; une première tentative l'a appelé avec le texte au lieu du chemin (erreur de nom de fichier trop long, sans effet). Aucune machine, aucun appel, aucun fichier existant modifié.
