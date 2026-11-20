# Contre-lecture — préenregistrement du palier 0b, version 14 (BROUILLON, erratum après le code v6) — v1

**BROUILLON EN ATTENTE DU MOT DE LAZAR : rien n'est scellé ; la version 13 scellée reste le texte en vigueur.**

- **Auteur** : contre-lecteur neuf, modèle O. Je n'ai écrit aucune version du texte ni aucun code ; j'ai contre-lu la version 12 et vérifié la version 13. Pièce de travail (classe C).
- **Date** : 2026-11-20 ; `date -u` lu à 18:05Z en cours de travail.
- **Mandat** : celui de la contre-lecture (`P/mandat-contre-lecteur-palier-0b-v12-v1.md`, `84b76af6…`, en-tête compris), et le message de la session du compte organisme qui demande cette contre-lecture. P = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- **Conditions** : processeur seul. Aucun tirage, aucun lancement du palier, aucune pièce d'autorisation, aucun appel à un fournisseur de modèles, aucune dépense. Aucune écriture dans l'arbre de travail du dépôt, aucun commit. Un `git fetch origin main`, puis deux `git show origin/main:…` redirigés vers mon dossier. Aucune commande de liste, aucun heredoc, aucun code en ligne. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**À corriger.** Deux corrections de justesse, aucune de fond (C1, C2). Quatre textes non exigés (N1 à N4), au choix de la mère. Sept points pour la mère (§ 6), dont deux à régler avant le lancement : le remplissage du blanc et les étapes 3 à 7. Après C1 et C2, et le mot de Lazar : « Conforme (brouillon), à sceller après le mot de Lazar ».

- **Rejeu.** L'outil appliqué à la v13 (`d9591d5b…`) avec le jeu (`7d9c1276…`) donne « FAIT : 33 remplacement(s) » et une sortie `840400f3…`. `cmp` avec la v14 est muet. Mon `diff -u` est égal au différentiel versé hors des deux lignes d'en-tête. Les 20 lignes retirées sont toutes sous une ancre ; les 33 lieux sont ceux du rapport du rédacteur.
- **Ligne du commit et table.**
  - Une seule ligne commence par « - Commit du code d'analyse : ».
  - `COMMIT_V6` figure une seule fois dans le texte. La ligne du commit ne porte aucun `` `<40 hex>` ``.
  - Le bloc qui la suit (l. 9 à 74) compte 64 lignes ; retrait de deux espaces ôté, il est égal à l'octet à `table-empreintes-code-v6.txt` (`639335b9…`).
  - Cette table est elle-même égale à l'octet au bloc du § 12 du rapport du code v6, que le rédacteur n'avait pas comparé. Ses 64 lignes sont justes sur `P/code-v6/` (`sha256sum -c`).
- **Lecteur d'en-tête du verrou du code v6** (`graines.py`, `bebabac8…`, empreinte de la table).
  - Sur une copie où le blanc est remplacé par un commit factice de 40 chiffres hexadécimaux (`56eaef70…`), il lit ce commit et la table des 64, égale à la table extraite.
  - Sur une copie égale à la v14, il **refuse** : « aucun commit du code dans la ligne « Commit du code d'analyse » du texte ».
  - Aucune graine dérivée. Seule `lire_en_tete_du_texte` est appelée, sur des copies.
- **§ 7 du rapport du code v6 et R-4332** : les points 1 à 11 sont portés, et les décisions de R-4332 et du mandat le sont à la lettre (§ 3).
  - Les citations de R-4304, R-4332, R-4295, R-4296 et `GO-2026-11-20-66` sont à la lettre : chaque morceau entre « […] » figure dans la ligne du registre sur `origin/main` (`84171548…`).
  - Les dix-neuf silences sont fidèles au rapport et à la vérification.
  - Le n° 13 est bien un constat, non une règle, sauf un renvoi de l'ordre des opérations (C1).
- **Point (i) du rédacteur** : je n'ai trouvé aucune phrase hors des sections touchées que l'erratum rende fausse (§ 4), avec une limite de méthode, déclarée. Dans une section touchée, la clause de portée de la ligne du commit range dans l'histoire une règle qui vaut encore (C2).

## 1. Rejeu et lieux

- **Empreintes égales aux compagnons** :
  - le brouillon : v14 (`840400f3…`), différentiel (`aa37724f…`), jeu (`7d9c1276…`), journal (`706b5869…`, heure 17:54:49Z), rapport (`f24d4769…`) ;
  - les pièces qui font foi : mandat du rédacteur (`2a44da18…`), rapport du code v6 (`0f408c6f…`), vérification du code v6 (`a7d0b1bc…`), audit des trous (`8e965f80…`), table (`639335b9…`), mesure de l'étape 8 (`216e2309…`).
- **Lieux** (`lieux_v1.py`, sortie `sortie-lieux-v14-v1.txt`) : titre (1) ; statut (2) ; date (3) ; ligne du commit (4 à 6) ; table (7 à 16) ; mandats et pièces (17, 18) ; B7 bis (19) ; B8 (20, 21) ; M7 (22) ; ordre des opérations (23, 24) ; « Ce qui est rapporté » (25, 26) ; « Contre-lecture » (27, 28) ; annexe C (29) ; réserve 24 (30) ; « Erratum du commit » (31) ; « Version 12 », § 2, silence n° 14 (32) ; fin du texte (33).
- **Table** : « hors de `src/`, deux fichiers d'essais changent d'empreinte et six fichiers sont neufs » est juste (64 − 58 = 6 neufs : le programme de lancement, trois sorties du banc, `mutations_v5.py`, l'essai `lancement`).

## 2. Lecteur d'en-tête du verrou (code v6)

Fait par `controle_v14_v1.py`, sortie `sortie-controle-v14-v1.txt`, sur des copies.

- `constantes.py` (`74c477d7…`) est inchangé depuis le code v5 (silence n° 17).
- `lire_en_tete_du_texte` lit le commit par le motif `` `([0-9a-f]{40})` `` (l. 111 et 155 de `graines.py`).
- Avec le blanc, le verrou refuse avant de lire la pièce, ce que la v14 dit « sans l'avoir lancé » : **c'est désormais éprouvé**.
- Avec un commit factice, il lit le commit et la table des 64, dont 24 sous `src/`.
- Le texte porte 20 groupes `` `<40 hex>` `` hors de la ligne du commit (anciens commits, dans l'histoire) ; le lecteur ne lit que la seule ligne au préfixe.

## 3. Les onze points du § 7, les décisions, le mandat

| point du § 7 | où la v14 le porte | jugement |
|---|---|---|
| 1 — ligne du commit, table des 64, forme du verrou | en-tête | juste ; commit en blanc, comme le mandat le veut |
| 2 — champ `mode` ; « aucune graine existante ne change » (n° 1) | B8, « Version 14 » ; § 2 | juste |
| 3 — lots, source étrangère de H, lot d'une source (n° 2, 3) | B8 ; B7 bis ; § 2 | juste ; n° 3 à la lettre de R-4332 et du mandat |
| 4 — reliquat, registre de la course source, aucune lecture, description, dossiers (n° 4 à 7) ; inventaire du § 6 | B8 ; « Ce qui est rapporté » ; § 2 | juste ; « ventilation par génération perdue » et « code v7 » écrits (R-4332, mandat) ; inventaire en renvoi (§ 5, remarque 4) |
| 5 — un seul lancement, manifestes, `verifier_cases` (n° 8, 9) | B8 ; § 2 | juste ; artefacts nommés (essais `point_3`) |
| 6 — étapes 8 et 9, relecture des gelés, case retirée, étape 9, dénominateur de R (n° 10 à 13, 16) | ordre, points 8 et 9 ; M7 ; § 2 | juste, sauf le renvoi « silences n° 10 à 13 » de l'ordre des opérations, alors que le n° 13 est laissé (C1) ; n° 16 écrit à M7 (R-4332) |
| 7 — la phrase « aucun programme … n'existe encore », aux deux lieux (n° 15) | B8 (l. 332 de la v13) ; silence n° 14 (l. 991) ; § 3 | juste, aux deux lieux que la vérification nomme |
| 8 — « Ce qui demande un code v6 » | § 5 | juste (sept points de l'audit) |
| 9 — annexe C, comptes, paramètres d'essai, essai de forme (n° 14, 18 ; 17, 19) | annexe C | juste : 6 + 17 + 10 + 10 + 18 + 5 + 15 + 11 + 24 + 1 = 117 ; 113 + 34 = 147 |
| 10 — ordre des opérations, statut | point 2 ; en-tête | juste ; le statut porte « BROUILLON, non scellé, en attente du mot de Lazar » |
| 11 — trois remarques du § 8 | § 6 | juste, en remarque, sans règle |

- **Décisions de la mère (R-4332 et le mandat)** :
  - n° 3, 4 et 16 acceptés, n° 13 laissé : portés ;
  - l'empreinte du programme de lancement (`67052a4b…`, égale à la ligne de la table) va dans la pièce de contrôle : écrit (B8 et § 3) ;
  - nœud du GO qui nomme la v14 : § 8 ;
  - tenue : faite.
- **Rien d'autre ne change** : aucun critère, aucun seuil, aucune valeur gelée, aucune prédiction, aucune issue. Aucune phrase neuve ne lit un résultat.

## 4. Point (i) : une phrase de la v13, hors des sections touchées, que l'erratum rendrait fausse ?

**Méthode, et sa limite.** Je n'ai pas relu ligne à ligne les 347 Ko de la v13. J'ai cherché dans le texte entier (`grep -n -o` avec contexte) chaque mot que l'erratum touche, puis j'ai lu chaque lieu trouvé hors des 33 remplacements. Familles de mots :
- reliquat ;
- « un seul lancement », `lancer_famille`, nombre commun de tirages ;
- « manifeste par run » ;
- « aucun programme », « n'existe encore », « programme de lancement » ;
- « 200 000 », lots, « 2 000 » ;
- noms et dossiers des cases ;
- champs d'étiquette ;
- « même commit », « commit inscrit en tête », « au commit du code » ;
- « code v5 » (chaque ligne qui le porte, hors des remplacements, vue).

J'ai aussi lu en entier : B8 (tableau des familles et alinéa « Graines »), M7, S7, la liste d'arrêt, l'ordre des opérations, l'annexe C, et le § 2 de l'annexe H, « Version 12 ».

**Constat : aucune phrase rendue fausse.**
- Les lieux qui disent le code v5 « sur `main` », la table « des 58 », les « neuf fichiers d'essais », 107 et 113 sont couverts par la clause de la ligne de version et par le § 9 (« Restent tels quels ») :
  - annexe C, « Version 12 » ;
  - « Contre-lecture », pièces de la version 12 ;
  - réserves ;
  - annexe H, « Ce qui demande un code v5 » et « Version 12 ».
- B8, « Chaque case garde ainsi 10 000 tirages » : la table des familles disait déjà « sur 200 000 sources par case » pour D, E, H, et la v14 dit les deux modes.
- Annexe F (l. 700) : « l'ordre des champs d'une étiquette » se dit du développeur du code v3 ; la v14 y ajoute `mode` en le disant.
- Métrique (l. 186) : l'intervalle de M7 par rééchantillonnage des sources reste vrai (deux séries, chacune sur ses sources).
- Annexe C (l. 514) : « le temps de calcul et la mémoire … ne sont estimés nulle part ailleurs » reste vrai **du texte**. La mesure de l'étape 8 en est une estimation hors du texte (N3).

**Deux phrases restent vraies mais tendent un fil** (§ 6, point 4) :
- « Version 12 », § 2, silence n° 16 (l. 1006) : « le point 1 de la liste d'arrêt les interdit [les étapes 3 à 7] tant que l'erratum du commit n'est pas contre-lu » ;
- « Erratum du commit », « Version 14 » : pour ce texte, rien ne se tire tant que le blanc n'est pas rempli et l'erratum scellé.

Sous la v13 scellée, l'erratum du code v5 est contre-lu : rien dans les textes n'empêche aujourd'hui de jouer les étapes 3 à 7 au code v5, alors que le code v6 change `etalonnage.py` et relit les réglages gelés par une fonction neuve.

**Dans une section touchée — C2.** La ligne du commit dit : « ce qui suit, jusqu'aux mots « Forme que le verrou lit », se dit de la version 12 et du commit du code v5 ». Cela range dans l'histoire la phrase « Le commit inscrit ici doit être celui que portera la pièce d'autorisation du verrou (B8) », qui vaut pour le code v6 (le rédacteur le signale, remarque 9).

## 5. Les neuf remarques du rédacteur

1. **Le blanc et l'empreinte ; un mot ou deux de Lazar.** Juste : la question est ouverte. Remplir le seul `COMMIT_V6` laisserait fausses les phrases qui le suivent (« — BLANC, À REMPLIR … » et « Tant que ce blanc n'est pas rempli … et refuse. »). Pour la mère : texte prêt au § 6, point 1.
2. **La mesure de l'étape 8.** Elle est désormais faite (`mesure-etape-8-essai-de-forme-v1.md`, `216e2309…`, compagnon OK ; pièce de travail, en attente du mot de Lazar, non contre-lue).
   - Extrapolation : ≈ 47 min sur un processus, ≈ 4,5 Go de mémoire (au plus ≈ 8 Go), ≈ 1,52 Go de disque.
   - Elle a joué la grille entière, non les « deux nombres de sources » de l'annexe C ; sa limite 4 le dit.
   - Ma recommandation : la porter comme constat, sans règle (N3), et dire à Lazar que l'annexe C n'est pas suivie à la lettre sur ce point. Le texte de l'annexe C ne change pas.
3. **Silence n° 5, l'agrégation.** Juste de ne pas trancher. S7 ne lit que R (M7) ; part et facteurs sont « rapportés à côté », sans seuil. Ma recommandation : la fixer au préenregistrement du programme d'analyse (étape 10), avant toute lecture. Aucun texte maintenant.
4. **L'inventaire du § 6.** Juste : renvoi. Ma recommandation : que le programme d'analyse s'y conforme ligne à ligne.
5. **Silence n° 10 hors de la table des critères.** Juste : l'audit (c) dit que la lecture ne change pas la règle de C1 et de C4. Garder.
6. **NE-2 et NE-3 de la v13.** R-4295 les dit « gardés pour une version suivante » ; la v14 en est une, mais le mandat ne les nomme pas.
   - Le rédacteur a écrit à la ligne de date « version 13 … vers 14:25Z (son en-tête) », qui répète l'heure inexacte.
   - Ma recommandation : les porter (N1, N2), avec l'heure exacte de la v14 (journal : 17:54:49Z) au lieu de « après 17:46Z ».
7. **La ligne de la pièce de contrôle pour `67052a4b…`.** À la mère. Ma recommandation, dans la forme de R-4296 (point, attendu, constaté, verdict) : une ligne « programme de lancement : `outils-dev/lancer_etapes_8_et_9_v1.py` de l'arbre lancé ; attendu `67052a4b…` ; constaté : empreinte recalculée ; verdict ». Le chemin y est écrit, et la commande de lancement appelle ce fichier-là.
8. **Étapes 3 à 7 sans programme d'enchaînement.** Juste, et c'est le point le plus lourd (§ 6, point 4).
9. **Troisième remarque du § 8, et la tournure de la ligne du commit.** La remarque est juste (le point 11 en nomme trois). La tournure n'est pas seulement de style : C2.

## 6. Pour la mère

1. **Remplir le blanc.** Ce n'est pas un remplacement d'un mot : un remplacement exact unique, puis le contrôle de son différentiel par un contre-lecteur, et le contrôle « ancêtre de `main` » refait. Ancre (comptée une fois dans la v14) : du texte `**`COMMIT_V6` — BLANC, À REMPLIR PAR LA MÈRE :` jusqu'à `… n'y trouve aucun commit et refuse.` (la phrase entière de la ligne du commit qui s'achève ainsi). Neuf proposé, `<COMMIT>` étant à remplacer par les 40 chiffres :
   `**`<COMMIT>`, sur `main` : c'est le code v6, vérifié « Conforme ».** La mère a inscrit ce commit à la place du blanc du brouillon, après avoir vérifié qu'il est un ancêtre de `main` (`git merge-base --is-ancestor`) et que les 64 fichiers de la table y ont les empreintes inscrites ; le lecteur d'en-tête du verrou du code v6, appliqué à une copie du brouillon au commit factice, y lisait le commit et la table (contre-lecture de la version 14).`
   Les phrases « à l'heure de ce brouillon » restent vraies de leur heure. Confiance moyenne à haute.
2. **Un mot ou deux de Lazar.** Le GO doit nommer l'empreinte du texte scellé, qui n'existe qu'après le blanc rempli. Ma recommandation, la plus sûre : deux mots.
   - Un premier mot sur la v14 contre-lue et corrigée (« à sceller, le blanc rempli par la mère »).
   - Puis le GO qui nomme l'empreinte scellée, comme `GO-2026-11-20-66` nommait `d9591d5b…`.
   - Un seul mot suffit si Lazar accepte de nommer la v14 par son chemin, l'empreinte étant inscrite par la mère au scellement.
   Confiance moyenne.
3. **N1 à N4** : à prendre, ou à garder pour une version suivante.
   - N1, N2 : l'heure de la v13 (R-4295) et celle de la v14.
   - N3 : la mesure de l'étape 8, en constat.
   - N4 : le chemin de la vérification de la v13, que la phrase « La mère inscrira ici » attend.
   Recommandation : les prendre avec C1 et C2, en une seule passe. Confiance moyenne à haute.
4. **Les étapes 3 à 7 et le commit.**
   - La v14 ne dit pas sous quel commit se jouent l'audit, la couche mécanique, le gel des fréquences, l'étalonnage et l'équivalence.
   - Le code v6 change `etalonnage.py`, et l'étape 8 relit les réglages gelés par sa fonction neuve.
   - L'audit des trous dit qu'aucun programme n'enchaîne ces étapes (6 bis et 7 attendent des configurations qu'aucune fonction ne construit).
   Ma recommandation :
   - qu'aucune étape 3 à 7 ne se joue sous la v13 et le code v5 d'ici le GO sur la v14 ;
   - que toutes, de 3 à 9, se jouent au seul commit du code v6, ce que la pièce de contrôle de la mère consigne ;
   - que le manque d'un programme pour 6 bis et 7 soit réglé (un code v7, ou une règle écrite) avant le GO.
   C'est un nœud de la mère, non de ce texte. Confiance élevée sur le constat, moyenne sur la voie.
5. **Ligne de la pièce de contrôle pour le programme de lancement** : § 5, remarque 7.
6. **Agrégation de l'enrichissement** : au préenregistrement du programme d'analyse (§ 5, remarque 3).
7. **La mesure de l'étape 8 et l'annexe C** : constat sans règle (N3) ; écart à la clause « deux nombres de sources » à dire à Lazar.

## 7. Corrections et textes non exigés

Chaque ancien est compté une fois par `grep -c -F -e` dans la v14 (six comptes à 1). C1 et C2 s'appliquent ensemble sur la v14 : « FAIT : 2 remplacement(s) », sortie `2c36dadbeca9e8fd178860557004db55535cf8c723339ffc19422ed8770d374a`. N1 à N4 s'appliquent par-dessus : « FAIT : 4 remplacement(s) », sortie `d670fd4cba4614c2c607e53b3ebe4a6cc12bf2b61bf12b38e2630ed7a1880e55`. Ce sont des essais, non des versions. Sur les deux, il reste une ligne au préfixe, `COMMIT_V6` une fois, aucun `` `<40 hex>` `` dans la ligne, et le bloc de 64 lignes égal à la table (`sortie-entete-essais-v1.txt`).

Jeux : `corrections-palier-0b-v14-v1.json` (C1, C2) ; `textes-non-exiges-palier-0b-v14-v1.json` (N1 à N4). Règle des textes : la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord ; `verifier_textes_v1.py` les tient égaux aux jeux.

- **C1** — ordre des opérations, point 9 (rang 24). Le n° 13 est laissé par la mère, non inscrit comme règle.
  - Ancien : `**Version 14** (silences n° 10 à 13 du rapport du code v6 ; annexe H, « Version 14 », § 2, qui fait foi pour le détail)`
  - Neuf : `**Version 14** (silences n° 10 à 12 du rapport du code v6 ; le n° 13, laissé par la mère, n'y est pas une règle ; annexe H, « Version 14 », § 2, qui fait foi pour le détail)`
- **C2** — ligne du commit (rang 5) : la portée de l'histoire s'arrête avant la règle qui vaut encore.
  - Ancien : `ce qui suit, jusqu'aux mots « Forme que le verrou lit », se dit de la version 12 et du commit du code v5.`
  - Neuf : `ce qui suit, jusqu'aux mots « la mère refait ce contrôle (annexe H, « Version 12 », § 2, silence n° 15) », se dit de la version 12 et du commit du code v5 ; la phrase qui suit ces mots, « Le commit inscrit ici doit être celui que portera la pièce d'autorisation du verrou (B8) », vaut pour le commit du code v6.`

**Textes non exigés.**

- **N1** — ligne de version, alinéa de la version 13 (NE-2 de la vérification de la v13, R-4295).
  - Ancien : `Cette version 13 est produite le 2026-11-20, vers 14:25Z (`date -u` à 14:21Z en cours de travail ; les heures exactes sont aux trois journaux de l'outil),`
  - Neuf : `Cette version 13 est produite le 2026-11-20, de 14:21Z à 14:22Z (heures des trois journaux de l'outil : 14:21:36Z, 14:21:43Z et 14:22:44Z ; `date -u` à 14:21Z en cours de travail),`
- **N2** — ligne de date : l'entrée de la version 13 (NE-3, R-4295) et l'heure de la version 14 (journal versé : 17:54:49Z).
  - Ancien : `version 13 le 2026-11-20, vers 14:25Z (son en-tête) ; version 14, brouillon, le 2026-11-20, après 17:46Z (`date -u` à 17:46Z en cours de travail ; l'heure exacte est au journal de l'outil),`
  - Neuf : `version 13 le 2026-11-20, à 14:22Z (heure du journal de l'outil : 14:22:44Z ; `date -u` à 14:21Z en cours de travail), dans les mêmes conditions, avec un `git fetch` de `main` et un `git show` redirigé vers le dossier du rédacteur, pour relire la décision R-4292 ; version 14, brouillon, le 2026-11-20, à 17:54Z (heure du journal de l'outil : 17:54:49Z ; `date -u` à 17:46Z en cours de travail),`
- **N3** — annexe H, « Version 14 », § 7, fin de la remarque 2 : la mesure de l'étape 8, en constat.
  - Ancien : `aucune règle de ce texte ne le dit (point hors liste (a) de la vérification du code v6).`
  - Neuf : `aucune règle de ce texte ne le dit (point hors liste (a) de la vérification du code v6). **Constat, depuis ce brouillon** : cette mesure a été faite (`palier-0b/mesure-etape-8-v1/mesure-etape-8-essai-de-forme-v1.md`, `216e230997a3290146aa74cdb3a330d221fb7e0964e0344e87309bf7481fe0c8`, pièce de travail, en attente du mot de Lazar) : l'étape 8 jouée sous la couche « essai-de-forme », sur le code v6 vérifié, à 50, 100 et 200 tirages par case et à 4 000 ou 8 000 sources par case, sur des fichiers gelés factices, sans graine décisive et sans lire aucun résultat ; extrapolée aux tailles gelées, de l'ordre de 47 minutes sur un processus, de 4,5 Go de mémoire (au plus de l'ordre de 8 Go, borne tirée du code) et de 1,52 Go de disque — une extrapolation, non une mesure à pleine taille. Elle lit chaque tirage à la grille entière, non aux « deux nombres de sources » de l'essai de forme de l'annexe C, clause qui, selon cette pièce, vise `tirages.essai_de_forme` (son § 5, limite 4). Ce texte n'en tire aucune règle.`
- **N4** — section « Contre-lecture », alinéa « Version 14 » (rang 27) : le chemin de la vérification de la v13, relevé sur disque (`2f52cc4f…`).
  - Ancien : `et la phrase qui précède, que la version 13 portait, n'est pas complétée par lui).`
  - Neuf : `et la phrase qui précède, que la version 13 portait, n'est pas complétée par lui ; ce rapport est `palier-0b/contre-lecture-v12/verification-palier-0b-v13-v1.md` (`2f52cc4fbf863e9f62671b23ce3af46d8fd4ed066ecd77e071c997b6bbf7f5d7`), sur la version 13 (`d9591d5b…`), relevé sur disque par le contre-lecteur de la version 14).`

## 8. Écarts et gestes

- **Un `git fetch origin main`**, demandé par le message. Il met à jour la référence distante (`origin/main` à `84171548…`, le commit que le rédacteur a lu), sans toucher l'arbre de travail.
- **Lecteur d'en-tête.** Le message dit « analyse statique seulement ; aucun lancement » et demande en même temps si le lecteur d'en-tête du code v6, sur une copie à commit factice, lit le commit. J'ai suivi l'exception que mon mandat donne : la seule fonction `lire_en_tete_du_texte`, par mon programme, sur des copies. Ni tirage ni pièce d'autorisation ; seuls `graines`, `constantes`, le paquet et `numpy` sont chargés.
- **Lecture de la v13** par familles de mots, non ligne à ligne (§ 4) : c'est la limite du point (i).
- **Lancés** :
  - l'outil : le rejeu ; la copie à commit factice ; deux essais ;
  - mes programmes : `controle_v14_v1.py`, `lieux_v1.py`, `citations_v1.py`, `entete_essais_v1.py`, `verifier_textes_v1.py` (pièce de la contre-lecture de la v12) et `deplier_jeu_v1.py` (lecture).
- **Commandes de lecture** sur des fichiers nommés : `sha256sum -c` de la table sur `P/code-v6/` (lecture seule) ; `sed -n`, `awk`, `grep -n -o`, `tail`.
- Aucun identifiant de modèle dans cette pièce ni dans mes jeux. Les copies de travail des registres en portent ; elles ne sont pas rendues.

## 9. Fichiers

`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/v14/`.

Avec compagnons :
- cette pièce ;
- `corrections-palier-0b-v14-v1.json` ; `textes-non-exiges-palier-0b-v14-v1.json` ;
- `controle_v14_v1.py` et `sortie-controle-v14-v1.txt` ;
- `lieux_v1.py` et `sortie-lieux-v14-v1.txt` ;
- `citations_v1.py` et `sortie-citations-v1.txt` ;
- `entete_essais_v1.py` et `sortie-entete-essais-v1.txt` ;
- `commit-factice-v1.json` ;
- `sortie-verifier-textes-v14-v1.txt`.

Fichiers de travail, non rendus :
- `rejeu-v14.md`, `copie-v14-commit-factice.md`, `essai-v14-corrige.md`, `essai-v14-corrige-avec-ne.md` et leurs journaux ;
- les différentiels ;
- `table-du-rapport-v6-section-12.txt` ;
- `jeu-v14-deplie.txt`, `jeu-v14-rang33.txt` ;
- `decisions-main.md`, `go-main.md`.

*Contre-lecteur neuf, modèle O.*
