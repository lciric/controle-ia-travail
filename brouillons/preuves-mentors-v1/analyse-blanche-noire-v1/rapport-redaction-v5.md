# Rapport de rédaction — analyse appariée boîte blanche / boîte noire, brouillon 5 (texte seul, voie B)

Rédacteur : l'auteur des brouillons 1 à 4 et du code v1 à v3 (Claude, Opus 5.5), le 2026-11-02, après le commit `1a9f1b97` de la contre-lecture 4 (`contre-lecture-4-preenregistrement-analyse-v1.md`, `dbf68e82…`, lu en entier). **Décision de la session (routine) : voie B, sans contre-lecture 5** : le brouillon 5 est le brouillon 4 plus exactement les remplacements H1 à H4 et B1 à B7 du rapport, appliqués par un script. Code et essais inchangés depuis le brouillon 3 (`git diff c67d7a6f HEAD` vide sur le code d'analyse et les essais). Aucune donnée de R1, R2 ni R4 ; aucun commit ; aucune empreinte compagnon ; brouillon 4 laissé tel quel (R12).

**Script** : `appliquer-contre-lecture-4-v1.py`. Il vérifie l'empreinte du brouillon 4 (`ee116316…`) et celle du rapport (`dbf68e82…`), puis lit les remplacements dans le rapport lui-même (blocs « remplacer … par » sous chaque titre « #### »). Il les applique dans l'ordre H1-H4, B1-B7, Z3-Z5, puis applique les ajouts de l'auteur, en exigeant une seule occurrence de chaque ancien texte. Il refuse un brouillon 5 déjà existant et finit par les vérifications. **Trace** : `appliquer-contre-lecture-4-v1-sortie.txt`, 25 remplacements, code 0.

| point | traitement |
|---|---|
| H1 | mot pour mot (étape 0.e : rien n'est récupéré de `calcul/r1-r2-reel-v1` ni de `calcul/r4-dose-reel-v1` avant le scellement de l'analyse principale et sa vérification de concordance) |
| H2 (3 remplacements) | mot pour mot (conséquence de l'emploi de la moyenne dite : un nœud, porté par la session comme réserve ; écart 5 étendu aux comparaisons principales, aux critères de lecture et aux contrôles du fournisseur ; règle écrite du quantile ; cinq écarts gardés) |
| H3 | mot pour mot (étape 0.a : rapports de rédaction et de contre-lecture) ; complété par l'auteur (Z2 et voie B) : fichiers du rejeu versés, script d'application et sa sortie |
| H4 | mot pour mot (exceptions complètes de l'entrée de la contre-lecture 3) |
| B1 | mot pour mot (titre « brouillon 5 ») |
| B2 | mot pour mot, chevron rempli (commit `1a9f1b97`) |
| B3 (3 remplacements) | mot pour mot, chevron rempli dans le premier (commit `1a9f1b97`) |
| B4 (1) | ancien du rapport ; nouveau adapté (voie B) : « brouillon 5, brouillon 4 corrigé selon la contre-lecture 4, sans contre-lecture 5 : décision de la session, voie B » |
| B4 (2) | ancien du rapport ; nouveau adapté (voie B) : « aucun autre (l'entrée de la contre-lecture 4 est remplie dès le brouillon 5 ; pas de contre-lecture 5) » ; avec l'ajout « le marqueur de gabarit restant » dans la même étape 0.c |
| B5 | ancien du rapport ; nouveau adapté (voie B) : l'item 2 des « Marqueurs de gabarit » dit qu'aucune ligne de contre-lecture ne porte de marqueur ; ajout « Un seul marqueur reste (item 1) » |
| B6 | mot pour mot |
| B7 | entrée de la contre-lecture 4 : texte du rapport, chevrons remplis (empreinte `dbf68e82…`, commit `1a9f1b97`, exceptions, sort des suggestions) ; la ligne « Contre-lecture 5 » du rapport est remplacée par une ligne « Pas de contre-lecture 5 » qui déclare la voie B et l'écart à la règle R2 (H1 et H2, écrits par le contre-lecteur 4, appliqués mot pour mot sans relecture par un tiers) |
| Z1 | appliquée au seul marqueur restant : le point final qui suit le marqueur reste en place, aucun n'est ajouté ; la partie « guillemets » est sans objet (aucun marqueur de contre-lecture ne reste) |
| Z2 | appliquée : script et sortie du rejeu de la contre-lecture 3, encore présents dans le bloc-notes, versés sous des noms neufs, mêmes octets (`rejeu-frequence-regle-decision-v2-sur-v3-contre-lecture-3-v1.py`, `774ec9fb…` ; `…-sortie.txt`, `7b2d1a7b…`, empreintes vérifiées par le script) ; cités par chemin ; la ligne finale « exit 0 » est dite ; ajoutés à l'étape 0.a |
| Z3 (2 remplacements), Z4, Z5 | mot pour mot (« reste à sceller à la date de ce texte » ; « la règle du coût déclaré (C) » ; le lecteur de concordance n'a écrit ni ce texte, ni celui de l'analyse principale, ni celui du fournisseur) |

**Vérifications** (trace du script ; refaites à la main) :
- `lecture_v3.exiger_code_cite` accepte le brouillon 5 : 27 fichiers, constantes `273c0a68…`.
- Il reste un seul « À REMPLIR », celui du commit cité.
- `prereg.problemes` renvoie `['marqueur À REMPLIR restant hors des sections exigées']`.
- Après remplacement simulé du marqueur sur une copie jetable : une seule ligne différente, et `problemes` renvoie `[]`.

**Essais v3** : 13 réussis en 27,3 s, sous `nice -n 10`.

**Fichiers neufs** : le brouillon 5 ; ce rapport ; le script et sa sortie ; les deux copies du rejeu ; `differences-brouillon4-brouillon5-v1.diff` (diff par mots du brouillon 4 au brouillon 5) ; `procedure-scellement-analyse-blanche-noire-v1.md` (étape 0, arrêt avant toute récupération de données).
