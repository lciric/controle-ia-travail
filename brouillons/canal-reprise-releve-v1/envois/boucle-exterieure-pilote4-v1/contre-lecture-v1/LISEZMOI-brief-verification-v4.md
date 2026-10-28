# Brief — vérification de la v4 de la boucle extérieure du pilote 4

De : conv-audit, le 2026-10-26 à 06:19:00 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : le vérificateur de la v3 (toi, relancé). Tu n'as écrit aucune des pièces vérifiées.

## 1. Ce qui est demandé

Un rapport, `rapport-verification-boucle-exterieure-v4.md`, et son compagnon, écrits dans ce dossier
(`/var/tmp/contre-lecture-boucle-exterieure-pilote4-v3/`), au même format que ton rapport sur la v3 : en-tête, verdict
(« utilisable », « utilisable après corrections » ou « à refaire »), constats numérotés `CLB4-NN` avec gravité, ce qui
est conforme, ce que tu n'as pas pu vérifier, écarts.

## 2. Pièces

Dans `fournis/`, à vérifier contre `EMPREINTES-fournis-v1.txt` (dans ce dossier, chemins relatifs à `fournis/`) :

- **La v4** : registre v4 (`e36707b0…`), protocole v3 (`acfd6426…`), briefs v3 (`7f6217e8…`), spécification (B) v2
  (`701b5270…`), LISEZMOI v4 (`e99123c6…`, tables « v3 → v4 » aux § 2 et § 3).
- **Ses consignes** : le brief v4 (`dc5b823b…`) et les deux messages que je lui ai envoyés ensuite
  (`messages-conv-audit-a-l-auteur-pendant-la-v4-v1.md` : deux précisions à D5 ; une correction à D4).
- **La v3 et ton rapport** : registre v3, protocole v2, briefs v2, spécification (B) v1, LISEZMOI v3 ; ton rapport
  `1a7873e2…`.
- **Le reste** : la pièce des points pour Lazar (`ac105262…`) ; l'extrait des lignes que les lanceurs v10 et v11 écrivent
  au `LANCEMENT.md` ; le texte v5 du pilote (`1943f39a…`, qui prime) ; le LISEZMOI du script de lecture v2 ; le brief du
  script de lecture v3 (`78861f99…`), que D1 doit suivre.

## 3. Ce que tu vérifies

1. Chaque constat CLB3-01 à CLB3-08 est traité **dans les fichiers**, pas seulement dans la table.
2. Les décisions D1 à D7, les deux précisions à D5 et la correction à D4 sont appliquées telles quelles ; en particulier
   la règle de préséance (D2) ne met jamais en regard les verdicts des deux courses, nulle part (pièces, journal, gardes) ;
   HC-P4-01 n'applique la voie `rondes_tournees` ni à M ni à S (D3).
3. Rien d'autre n'a changé de la v3 à la v4 que ce que les constats, les décisions et les changements déclarés au § 4
   du LISEZMOI v4 demandent : compare les fichiers (`diff`), et dis pour chaque bloc non déclaré s'il est un écart.
4. Les noms et contenus des fichiers de lecture écrits dans la v4 concordent avec le brief du script v3 (sorties `test`
   et `test-final-holm-quatre` par course ; ce qu'un fichier `holm-quatre` porte et ne porte pas ; ligne d'état ; phrase
   (iv)).
5. L'identité de la course S (tableau du protocole) concorde avec le texte v5 ; la spécification (B) v2 exige des champs
   que les lignes des lanceurs (extrait) portent vraiment, ou dit d'où ils viennent ; dis lesquels n'ont aucune source.
6. Les points pour Lazar sont cités tels que la pièce les pose (défauts, moments) ; aucune dépense n'a de défaut.
7. La garde nouvelle G12 et les gardes réécrites (G6, G8 bis) ont chacune un cas sain et un artefact (R5).
8. Les faits de course que l'auteur déclare avoir lus (coût et heure de fin de M, nom du dossier de S) n'ont changé aucune
   règle de lecture.

## 4. Interdits (inchangés)

Rien hors de ce dossier ; aucun score, aucun fichier de course, aucun script ; aucun `git`, réseau, sous-agent ni clé ;
écrire seulement le rapport et son compagnon ; heures lues sur `date -u` dans la commande qui les écrit ; aucun critère ni
aucune stratégie de classement des tâches. Python, s'il le faut, avec `-I` et sans écrire de fichier.

## 5. Fin

Réponse finale en quelques lignes : verdict, constats à corriger avant usage, empreinte du rapport.
