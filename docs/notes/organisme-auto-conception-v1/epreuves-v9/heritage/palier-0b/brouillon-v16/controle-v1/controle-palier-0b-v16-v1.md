# Contrôle du brouillon de la version 16 — préenregistrement du palier 0b — v1

**BROUILLON EN ATTENTE DU MOT DE LAZAR. Rien n'est scellé ; la version 13 scellée reste le texte en vigueur.**

- **Auteur** : contre-lecteur neuf, modèle O, celui des versions 14 et 15. Je n'ai écrit aucune version du texte, aucun programme, aucune vérification. Pièce de travail (classe C).
- **Date** : 2026-11-20 ; `date -u` à 22:09Z en cours de travail.
- **Mandat** : l'en-tête du mandat `84b76af6…`, et deux messages de la session du compte organisme. Le premier demande ce contrôle (points 1 à 6). Le second ajoute un point 7 : les réponses de la mère arrivées à 22:03Z.
- **Conditions** :
  - ce que j'ai fait : un `git fetch origin main`, puis un `git show origin/main:registres/decisions.md` redirigé vers mon dossier ; l'outil de remplacement, sur des copies ; des lectures de fichiers nommés ;
  - ce que je n'ai pas fait : aucun lancement d'un programme ni du code, aucun essai, aucun tirage, aucune pièce d'autorisation ni de contrôle, aucune écriture dans l'arbre de travail du dépôt ;
  - **aucun refus de permission, de classifieur ni de garde.**

## Verdict : **À corriger**

Onze corrections, regroupées en quatre groupes :
- huit portent les réponses de la mère de 22:03Z : R-4335 citée, remarques 2 à 6 changées en règles ;
- deux corrigent un fait : les manifestes du programme 1 portent eux aussi les champs du verrou non nuls ;
- une ajuste la remarque 7 en conséquence.

Aucune correction ne touche un critère, un seuil, une valeur gelée, la ligne du commit ou la table. Jeu : `corrections-palier-0b-v16-v1.json`. Chaque ancre est comptée une fois par `grep -c -F -e` dans la v16 (onze comptes à 1). Sur une copie de la v16, l'outil rend « FAIT : 11 remplacement(s) », sortie `ee5ff01398149875259ce580aab768f75410d5641eb70c851354d9a34451ce2c` : c'est un essai, non une version. Le rédacteur appliquera ces corrections dans une version 17 ; la v16 n'est pas touchée.

## 1. Rejeu des deux passes

**Empreintes** : chaque pièce est égale à son compagnon.
- Mandat (`df49b3b1…`) ; dossier `brouillon-v16/` : v16, différentiel (`d0d18a1a…`), rapport (`f636a0f7…`), deux jeux, sortie de la passe 1.
- Rapports, vérifications et essais des programmes : `ef1196cd…`, `0042de7a…`, `14158882…`, `5dae3b94…`, `beeaf621…`, `59907a0d…`, `3c0b1cb3…`, `8d891152…`, `62065d04…`.

**Rejeu depuis la v15** (`33b04ff4…`) :
- passe 1 : « FAIT : 12 remplacement(s) », sortie `54d20af4…`, égale à la passe 1 versée ;
- passe 2 : « FAIT : 5 remplacement(s) », sortie `c37bdb2f301f3bd9efa8767f36158006e7b1f58c4b2ab628d96cfa1eaa3bfa0d`. **`cmp` avec la v16 : muet. Même empreinte.**

## 2. Les points 1 à 8 du mandat, et rien d'autre

**Lieux** (`lieux_v1.py`, sortie `sortie-lieux-passe-1-v1.txt`) :

| remplacements | lieu |
|---|---|
| passe 1, n° 1 | les deux sections neuves avant « Ce qui est rapporté » |
| passe 1, n° 2 et 3 | ordre des opérations, points 2 et 3 à 7 |
| passe 1, n° 4 | sous la table de la liste d'arrêt |
| passe 1, n° 5 | annexe C |
| passe 1, n° 6 | B8 |
| passe 1, n° 7 et 8 | annexe H, « Version 14 », remarques 8 et 9 |
| passe 1, n° 9 et 10 | mandat et pièces |
| passe 1, n° 11 | fin du texte |
| passe 1, n° 12 | critères de lecture, renvoi à l'écart |
| passe 2 | titre, statut, date, « Contre-lecture » |

Les autres lignes que le différentiel retire sont celles de la passe 2.

**Jugement, point par point :**
- (1) **Section neuve des programmes** : chemins, empreintes entières, commandes, ordre, ce que chacun rend et ce que le suivant reçoit, essais (33 pour le programme 1, en version 4, le programme restant la version 2) : porté.
- (2) **Décisions de la mère**, citées avec leur heure, aux lieux nommés (étapes 3 à 7, liste d'arrêt, annexe C, pièce de contrôle) : porté.
- (3) **Pièce de contrôle** : ce qu'elle porte, écrite avant l'étape 3, remarque sur les espaces : porté.
- (4) **Phrases « aucun programme »** : deux lieux, remarques 8 et 9. J'ai cherché d'autres lieux dans la v15 (« enchaîne », « à écrire et vérifier ») : il n'y en a pas d'autre, hors de la citation de R-4333, qui reste à la lettre.
- (5) **ÉCART POUR LAZAR** : porté (§ 5 ci-dessous).
- (6) **Remarque « fichier entier, sans sélection »** : portée, sans règle.
- (7) **Nœud du GO, blanc gardé** : porté.
- (8) **Tenue** : faite. Statut « BROUILLON, non scellé, en attente du mot de Lazar » ; date 22:00Z ; journal de la passe 2 : 22:00:47Z.

**Hors mandat** : aucun ajout. L'alinéa sous la liste d'arrêt et le renvoi des critères de lecture servent les points 2 et 5. Aucun mot de la table de la liste d'arrêt ne change.

## 3. Fidélité aux pièces

**Décisions de la mère.**
- R-4334 est citée à la lettre. Ses deux morceaux, de part et d'autre de « […] », figurent dans la ligne du registre sur `origin/main` (`480cb4e0…`), et la citation entière est comptée une fois dans la v16.
- Les décisions de 18:29Z et de 18:53Z sont portées comme le mandat les donne ; R-4335 les inscrit depuis (§ 7, point a).

**Silences et vérifications.**
- Programme 1, silences n° 1 à 10 (rapport v1, § 3) et n° 11 (rapport v2) : rendus fidèlement. Noms des fichiers, dossiers, racine `famille=organisme|role=racine`, tâche `palier-0b|etape-4`, arrêts propagés sans manifeste, verrou et pièce dès l'étape 3, commit pris de l'autorisation.
- Programme 1, condition du point 5 : conforme au code. Le programme lit le point 5 sur les réglages rendus, l. 233 à 237, et inscrit `reglages_sha256` au manifeste d'arrêt, l. 235.
- Programme 2, silences n° 1 à 10 : rendus fidèlement. 22 couples et 66 comparaisons, couche « mecanique-reglages », tailles, verrou, pièce, commit, fichiers, arrêts, lieu.
- Silence n° 10 du programme 2 : dit fermé.
- Remarques S8 : portées.
- Avis du vérificateur sur la garde 17 (vérification du programme 1 en version 1, point 2) : « accepter, pas un écart bloquant ». Exact.

**Un fait inexact.** La v16 dit le contraire en deux lieux, et la remarque 7 le laisse ouvert : **les manifestes du programme 1 portent eux aussi les trois champs du verrou non nuls**. Le programme construit les graines de chaque étape avec l'autorisation (`lancer_etapes_3_5_6_v2.py`, l. 172, 181, 213 et 224), et `tirages.ecrire_manifeste` prend ces champs de l'autorisation des graines (code v6, l. 361 à 364). Corrections K1, K2 et K3.

**Empreintes des trois programmes**, recomptées sur disque :
- `1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14` ;
- `ed91813a88c9f58e65dd21d5e7a15fd6d4f2ae810787eb57bf57e7caceeb71d0` ;
- `67052a4b7af9bd02c5f28f3b8a7926fd7b7ac5a98fb797f14b3d6f424bedc2a5`.

Toutes trois sont égales au texte et au mandat.

**Commandes.**
- La première et la deuxième sont celles des rapports, § 4. Pour la première, avec le programme v2, comme dans le rapport v2.
- La troisième, de la main du rédacteur, est conforme à l'en-tête de `code-v6/outils-dev/lancer_etapes_8_et_9_v1.py` :
  - dossier courant : celui du code ;
  - `PYTHONPATH=src` seul, interpréteur avec `-B` ;
  - neuf arguments, dans l'ordre TEXTE, RACINE, FREQUENCES, SHA_FREQUENCES, REGLAGES, SHA_REGLAGES, DOSSIER_8, DOSSIER_9, COMMIT, que `main` exige (l. 30 à 32).
- Ce que la v16 dit de la sortie et des dossiers neufs est exact (l. 33 à 46).

## 4. La ligne du commit

Contrôle sur la copie égale à la v16, sortie `sortie-entete-v16-v1.txt`. La copie corrigée donne le même résultat (`sortie-entete-essai-v16-v1.txt`).
- Une seule ligne commence par « - Commit du code d'analyse : ».
- `COMMIT_V6` figure une fois.
- La ligne ne porte aucun `` `<40 hex>` ``.
- Le premier bloc qui suit compte 64 lignes, égales à l'octet à `table-empreintes-code-v6.txt`. Le verrou le lit sans changement.

## 5. ÉCART POUR LAZAR (garde 17)

- **Fidélité** : la citation de B2 et celle des critères de lecture sont chacune comptées une fois dans la v15, à la lettre.
- **Honnêteté** :
  - ce que fait le programme est exact : il exige la copie avant toute étape et refuse avant l'étape 3 ;
  - le rétrécissement est dit pour ce qu'il est : aucune issue « lisible » n'est rendue plus facile, et ce qui est perdu est nommé ;
  - les deux voies sont présentées avec leur avantage et leur inconvénient ; la voie (b) est décrite sans être dépréciée.
- **Non tranché** : la recommandation (a) est donnée comme celle du rédacteur, avec sa confiance et ce qu'elle ne couvre pas ; « Défaut : aucun ». Le statut, l'alinéa sous la liste d'arrêt et les critères de lecture disent l'écart non tranché.
- **Rien à corriger.**

## 6. Les remarques 1 à 8 du rapport (annexe H, « Version 16 », § 2)

- **N° 1 (commande du programme 8–9)** : reste une remarque. La commande est conforme à l'en-tête (§ 3).
- **N° 2, 3, 4, 5 et 6** : elles devaient devenir des règles ou des citations, et la mère l'a tranché (§ 7).
  - **N° 2.** Avant même la réponse de la mère, la remarque laissait sans écrit le seul contrôle de l'empreinte du programme 8–9 : ce programme ne lit pas la pièce de contrôle.
  - **N° 3.** Le risque est réel. Après un arrêt au point 5, le fichier des réglages est gelé, relisible et inscrit au manifeste d'arrêt. Le programme 2 le relirait sans voir l'arrêt : il contrôle l'empreinte et le compagnon, non l'issue du manifeste de l'étape 6.
- **N° 7** : la phrase de B8 (« Version 12 ») peut rester avec sa lecture, comme ce texte le fait de ses autres phrases d'histoire. Mais le constat restreint aux étapes 6 bis et 7 est inexact : corrections K1 à K3.
- **N° 8** : reste une remarque.

## 7. Les réponses de la mère de 22:03Z (point 7)

**(a) R-4335 citée.** Relue sur `origin/main` après `git fetch` : commit `480cb4e0c1513f7c92458a52ba4469f0b680443c`, `decisions.md` `60fffc72…`, l. 4473, sous l'heure 2026-11-20T22:03:22Z. Corrections A1 à A4 :
- A1 : citation à la lettre, au mandat de la version 16 ;
- A2 : renvoi à R-4335 dans l'en-tête de la section des programmes ;
- A3 : renvoi à R-4335 en tête de l'annexe H, « Version 16 » ;
- A4 : la remarque 6 dit les décisions inscrites depuis.

**(b) Remarque 2 en règle** (correction B) : la mère contrôle à la main, au lancement, l'empreinte du programme 8–9 contre `67052a4b…`, et l'écrit dans sa pièce de contrôle. La pièce est scellée avant l'étape 3, donc l'écrit va dans un complément, sous un nom neuf (règle R12).

**(c) Remarque 3 en règle** (correction C). **Écart à la lettre de la réponse, à trancher par la mère.**
- La réponse dit « manifeste présent, aucun `arret.json` ». Aucun programme n'écrit de fichier `arret.json`.
- Le programme 1 écrit, à un arrêt nommé, `arret.txt` (et, à l'étape 3, `rapport-joint-a-l-arret.json`), **et un manifeste d'issue « arrêt »**, l. 145 à 152.
- Le programme 2 écrit `arret-garde-equivalence-s8.txt` et un manifeste d'issue « arrêt », l. 141 à 156.
- Lu à la lettre, le constat « manifeste présent, aucun `arret.json` » laisserait passer un arrêt nommé, en particulier l'arrêt au point 5.
- Mon texte constate donc :
  - après le programme 1 : les quatre manifestes présents, scellés, d'issue « tenue », aucun `arret.txt`, et les deux lignes de sortie ;
  - après le programme 2 : son manifeste d'issue « tenue », aucun `arret-garde-equivalence-s8.txt`, et la sortie « garde tenue ».
- Recommandation : retenir cette forme. Confiance élevée.

**(d) Libellés** (correction D). « commit du programme » et « empreinte du programme », un de chaque par programme. **Oui, le libellé doit porter le nom du programme**, pour trois raisons :
- R-4335 veut la pièce « sans équivoque » ;
- trois lignes « empreinte du programme : » ne disent pas à quel programme chaque empreinte appartient ;
- les programmes 1 et 2 ne lisent pas les libellés : ils cherchent le commit et leur empreinte dans la pièce entière (`a.commit not in contenu`, `empreinte_du_programme() not in contenu`). Les libellés ne servent qu'au contrôle de la mère, qui doit pouvoir lire sans ambiguïté.

Forme proposée : `commit du programme lancer_etapes_3_5_6_v2.py : <commit>` et `empreinte du programme lancer_etapes_3_5_6_v2.py : <empreinte>`, de même pour les deux autres. Le nom de fichier ne contient aucune empreinte, et chaque ligne garde une seule valeur. Si la mère veut les libellés sans le nom, il suffit d'ôter de mon texte « pour que la pièce reste sans équivoque … avant les deux-points : » et les trois noms. Je le déconseille : confiance élevée.

**(e) Remarque 5 en règle** (correction E) : les dossiers des sorties des étapes 6 bis à 9 sont fixés par la mère dans sa pièce de contrôle, dans un complément sous un nom neuf si elle est déjà scellée (R12), avant chaque lancement, sans espace.

**Point pour la mère : le nom des compléments.** R-4292 réserve `…-v1-complement-1.md` à la règle n° 8, jouée après le lancement des étapes 8 et 9. Or les règles neuves demandent des compléments **avant** :
- les fichiers gelés ;
- le constat de fin sans arrêt, deux fois ;
- le contrôle de l'empreinte du programme 8–9 ;
- les dossiers des sorties.

Le numéro 1 serait déjà pris, et l'alinéa « Version 13 » de la remarque 5 (« Version 12 ») le nomme. Recommandation : une ligne du registre qui numérote les compléments dans l'ordre où ils s'écrivent, celui de la règle n° 8 venant en dernier, et une correction de l'alinéa « Version 13 » dans la v17. Confiance moyenne à haute. Je n'en fais pas une correction de ce jeu, parce que la lettre de la mère manque.

## 8. Les corrections (ancre, lieu)

| n° | lieu | objet |
|---|---|---|
| A1 | « Mandat de la version 16 » | R-4335 citée à la lettre |
| A2 | section des programmes, en-tête | renvoi à R-4335 |
| A3 | annexe H, « Version 16 », en-tête | renvoi à R-4335 |
| A4 | annexe H, « Version 16 », remarque 6 | inscrites par R-4335 |
| B | remarque 2 | règle : contrôle de l'empreinte du programme 8–9 |
| C | remarque 3 | règle : constat de fin sans arrêt, aux noms réels des fichiers |
| D | remarque 4 | libellés, avec le nom du programme |
| E | remarque 5 | règle : dossiers des étapes 6 bis à 9 |
| K1 | section des programmes, programme 2, *Le commit du manifeste* | les manifestes du programme 1 portent aussi les champs non nuls |
| K2 | B8, « Version 16 » | « les manifestes des étapes 3 à 7 portent » |
| K3 | remarque 7 | constat pour les étapes 3 à 6 |

Les textes Ancien et Neuf exacts sont dans le jeu JSON. Les ancres A1 à A3, K1 et K2 sont des phrases ; les ancres des remarques 2 à 7 sont leurs lignes entières.

## 9. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/v16/`.

Avec compagnons :
- cette pièce ;
- `corrections-palier-0b-v16-v1.json` ;
- `sortie-lieux-passe-1-v1.txt` ;
- `sortie-entete-v16-v1.txt` ;
- `sortie-entete-essai-v16-v1.txt`.

Les programmes employés sont ceux de la contre-lecture de la v14 (`v14/lieux_v1.py`, `v14/entete_essais_v1.py`) et `deplier_jeu_v1.py`.

Fichiers de travail, non rendus :
- `rejeu-passe-1.md`, `rejeu-passe-2.md`, `essai-v16-corrige.md` et leurs journaux ;
- `passe-1-deplie.txt`, `passe-2-deplie.txt` ;
- `decisions-main.md`, copie du registre, qui porte des noms de modèle.

*Contre-lecteur neuf, modèle O.*
