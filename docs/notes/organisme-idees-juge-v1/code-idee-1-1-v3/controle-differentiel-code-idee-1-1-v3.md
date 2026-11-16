# Contrôle du différentiel v2 → v3 du code de l'idée 1.1 (R2) — contre le préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md` (`3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`)

- Auteur : contre-lecteur neuf, sous-agent de la session mère. Je n'ai écrit ni le texte, ni le code v1, v2 ou v3, ni les rapports du développeur, ni les deux contre-lectures précédentes.
- Date (UTC, `date -u`) : du 2026-11-15 à 23:53 au 2026-11-16 à 00:05. Code lu sur `main` au commit `6322dbee` (code v3). Deux commits d'autres sessions sont arrivés pendant le contrôle (`0bc91a34`, `1d675f0c`) : ils ne touchent aucun fichier de l'idée 1.1 (vérifié par `git diff --stat`). Arbre propre au début et à la fin.
- **Interruption** : un premier passage de ce contrôle a été coupé par une erreur passagère du service. Il n'avait laissé aucune trace sur disque (ni rapport, ni script, ni journal : vérifié). Tout ce qui suit a donc été fait après la reprise, d'un seul tenant ; rien n'est repris de mémoire.
- Ce que je n'ai pas fait :
  - aucun fichier existant modifié, aucun commit, aucune poussée, aucun clone ;
  - aucun appel réseau ni payant ; aucune variable d'environnement affichée ;
  - ni le jeu, ni l'étape 0, ni la lecture d'une sortie de jeu ; rien ouvert ni écrit sous `diag/`, `runs/`, `donnees/`.
- Une exécution du banc hors de tout jeu : **82 répétitions isolées** sous une **racine d'essai de ma main**, différente de celle du texte (vérifié par une assertion) et de celles des essais du développeur. Tout est écrit dans le dossier temporaire de la session.
- Pièces lues, empreintes recalculées et égales : la vérification précédente (`549e4597…`), le rapport v3 (`aa014c9e…`), `couples-v2-vers-v3.json` (`d4ec2946…`), les quinze fichiers v3 et leurs compagnons, chaque `diff` v2 → v3, le banc `banc_idee_1_1_v2.py` (inchangé), et dans le texte : « Métrique », « Coût et durée » (règle de réduction), liste d'arrêt.

## 0. Verdict

**Corrections avant l'étape 0 : une seule (C1), petite, exigée par R5. Tout le reste est conforme ; jouable ensuite.**

- **N1 est corrigé.** De vrais enregistrements du banc, des 30 lignes, passent toute la chaîne de lecture v3, sans réduction et sous les cinq réductions (section 2). Je n'ai trouvé **aucun autre désaccord de format** entre ce que le banc écrit et ce que la lecture lit.
- **C1** — `src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v3.py`, l. 726 et 727 : la garde « ligne V sans engagement jumeau » de `verifier_format` **ne peut jamais se déclencher**. Elle compare un nom de ligne à `B.LIGNES_V`, qui contient des indices. Sur l'artefact, la lecture rend alors un résultat **sans arrêt ni message** (section 4).
  - Portée : aucun enregistrement que le banc gelé peut écrire n'atteint ce cas (`actifs_pour` garde au moins 250 répétitions du jumeau sur chaque ligne V). Aucun verdict du jeu n'est en cause.
  - Je le classe pourtant en correction, pour deux raisons : R5 exige que toute garde soit éprouvée sur un artefact et interdit le repli silencieux ; et la lecture v3 sera gelée par l'addendum, donc incorrigible après le jeu sans écart.
  - Si la mère préfère ne pas refaire un tour de noms neufs, l'autre voie est de **déclarer la garde inerte à l'addendum**. Je ne la recommande pas : R5 est une règle gelée.
- Mineurs nouveaux, sans effet sur un verdict : n6 à n9 (section 7).
- Essais v3 rejoués : **149 passés sur 149** en 263,38 s (section 9).

## 1. Égalité v3 = v2 + différentiel déclaré

- **Rejeu indépendant de l'essai d'égalité**, par un script de ma main hors du dépôt. Pour chacun des 12 fichiers du JSON : le v2 est égal à son compagnon, chaque « ancien » est présent une seule fois, et le v2 avec les couples appliqués dans l'ordre puis l'ajout de fin est égal octet pour octet au v3. **12 égaux sur 12.** Chaque v3 est égal à son compagnon.
- Les trois fichiers hors du JSON : `test_…projection_v3.py` a la même empreinte que son v2 (`6e53851e…`) ; `test_…differentiel_v3.py` et `test_…bout_en_bout_v3.py` sont neufs, lus en entier.
- **Aucun fichier v1 ou v2 n'a changé** : `git diff --stat c817619c 6322dbee` ne montre que des ajouts (33 fichiers, aucune ligne retirée), soit les fichiers v3, leurs compagnons, les deux notes et une ligne de `registres/decisions.md`.
- **Chaque `diff` relu sur son contenu.** Le différentiel ne contient rien de plus que ceci :
  - **lecture** : docstring ; arrêt avec message dans `lire_rho`, `lire_rho_strate` et `lire_decomposition` si tous les rééchantillons sont écartés ; compte des écartés et niveau dans la décomposition ; deux paires de McNemar ; A2 lu par `log_w_200` ; `return res` de `lire_v2` puis l'ajout de fin (`LECTURES_DECLAREES`, tables de champs, `verifier_format`, `lire_v3`) ;
  - **exécution** : docstring, nom du run et liste des noms refusés, `FICHIERS_GELES`, `ESSAIS` limité aux essais v3, import de l'étape 0 v3 ;
  - **étape 0** : docstring, import des mutations v3, `declarations_v3` ;
  - **mutations** : docstring et import de la lecture v3 ;
  - **scripts** : docstrings, imports, `version_lanceur` à 3, nom de la commande, `lire_v3`, chemin de sortie de l'étape 0 ;
  - **essais** : imports, noms des scripts, compte des essais (7), enregistrement synthétique mis au format du banc, et les six essais neufs de la lecture.
- L'arrêt ajouté dans `lire_rho` (l. 222 et 223) est dans le code de la v1. Il ne change aucune valeur : sans lui, `numpy.quantile` sur une liste vide lève `IndexError` (vérifié sur la version installée). Une trace devient un arrêt avec message.

## 2. N1 : l'épreuve refaite sur de vrais enregistrements

**Ce que j'ai joué**, par `banc_idee_1_1_v2.jouer_repetition`, un processus, `nice -n 10` :

| lot | répétitions | réductions |
|---|---|---|
| les 30 lignes, répétition 0 | 30 | aucune |
| Q1, Q9a, V5(0.8), Hn, H7, répétition 1 | 5 | aucune |
| les 15 lignes V, répétitions 0, 250 et 500 | 45 | 1 à 5 |
| Q9a et Q9b, répétition 500 | 2 | 1 à 5 |

Les enregistrements réduits ont bien la forme attendue de la règle, lue sur les vrais enregistrements :
- ligne V, répétition 0 sous réduction : `strate_sans_log` absent ;
- ligne V, répétition 250 : `J9-D40`, `J9-D`, `J9-Dc`, `ED_ecart_T8` absents ;
- ligne V, répétition 500 : en plus, `La-P` et `journal_La-P` absents ;
- Q9a et Q9b, répétition 500 : `J9-P`, `La-P` et leurs deux journaux absents.

**Chaîne suivie** : tranches écrites par `ecrire_json_scelle`, index scellé, `charger_sortie`, `verifier_format`, `lire_v3`, écriture scellée de `lecture.json`, relecture. Le nombre de répétitions par ligne est ramené à 100 puis à 600 dans mon seul processus d'essai.

Pour franchir les étages, je règle les valeurs `promue` comme le développeur, mais par un **réglage strict** : il refuse d'écrire une clé `promue` qui n'existe pas déjà ou qui n'est pas un booléen. Il ne peut donc masquer aucun champ.

| épreuve | résultat |
|---|---|
| forme brute, aucun réglage : `verifier_format`, `taux_des_cellules`, `lire_mcnemar`, `lire_v3` sur les 30 lignes | passés ; 342 cellules ; `lire_v3` s'arrête à l'étage 2 comme attendu d'une seule répétition, sans erreur |
| A — sans réduction, 100 répétitions par ligne | étages 1 à 3 franchis ; les 18 rubriques présentes ; 18 bras lus ; A2 lu sur les 25 lignes sans mémoire ; 195 tests de McNemar (15 lignes × 13 paires) ; `lecture.json` scellé et relu, version 3 |
| B — réductions 1 à 5, 600 répétitions par ligne | étages 1 à 3 franchis ; les 18 rubriques présentes ; secondaires lus sur leurs premières répétitions (jumeau : 250 ; La-P : 500 ; J9-P contre La : 600) ; McNemar aux mêmes comptes ; cellules de Q9a à projection lues sur 500, ses cellules fatales sur 600 ; strate descriptive vide |

**Aucun désaccord de format, avec ou sans réduction.** Les chiffres de ces épreuves n'ont aucun sens : les promotions sont réglées et la racine est d'essai. Je n'en ai lu aucun comme résultat.

Ce que le rapport du développeur laissait ouvert (« les formats réduits ne sont éprouvés que sur des données synthétiques ») est donc fermé par cette épreuve.

## 3. L'essai de bout en bout du développeur

- **Il couvre bien les 30 lignes et tous les bras** : il joue la répétition 0 de chaque ligne, sans réduction. À la répétition 0, tous les groupes sont actifs, strate descriptive et journal entier compris.
- **Ce qu'il ne couvre pas** : une seule répétition par ligne, recopiée 100 fois. Aucune forme réduite, donc. Le rapport le dit.
- **Le motif synthétique peut masquer un champ, en principe.** `_promue` (essai, l. 33 à 35) écrit `rec[bras]["promue"]` dès que le bras existe : si le banc n'écrivait pas ce champ, le motif le créerait. Il en va de même pour `J9-P-nu`, `J9-P-gel` et `strate_sans_log` (l. 43 à 49).
  - Le second essai, `test_format_reel_de_chaque_ligne_accepte`, passe les enregistrements bruts à `verifier_format`. Il ferme ce masque pour les bras que `verifier_format` contrôle.
  - Il reste quatre champs que ni l'un ni l'autre n'éprouve à l'état brut : `J9-Dc.promue`, `temoin_lambda.promue`, `strate_sans_log.*.promue`, et `promue` et `max` sous `J9-P-gel`.
  - **En fait, rien n'est masqué** : mon réglage strict a passé sur les 82 vrais enregistrements, et le code du banc écrit ces quatre champs (banc, l. 798 à 802, 821, 862, 949 et 956). C'est un défaut de l'essai, pas du code (n8).

## 4. `verifier_format` et les arrêts

J'ai cassé de vrais enregistrements de vingt façons, puis appelé `lire_v3`. Le cas sain est accepté.

| artefact | issue |
|---|---|
| `A2.log_w_200` absent ; `ecart_residuel_La` absent ; `journal_J9-P.c_moins_1_max` absent ; `J9-D.quantite_fatale` absent d'une cellule fatale | arrêt par `verifier_format`, message qui nomme la ligne, la répétition et le champ |
| `J9-D` absent d'une seule répétition de Q1 (réapparaît) | arrêt, « réapparaît après une réduction » |
| `J9-P-nu.lineaire_seul.max` absent sur Hg | arrêt, « incomplet » |
| enregistrement qui n'est pas un dictionnaire ; répétition hors d'ordre ; ligne en trop ; ligne vide | arrêt par `verifier_format` |
| `J9-P-gel.complet.max` ou `.promue` absent ; `promue` absent sous `J9-P-nu` de H7, sous `J9-Dc`, sous `temoin_lambda` ; `strate_sans_log.J9-P` absent ; `max` de J8 à `None` | arrêt par l'enveloppe de `lire_v3`, message qui nomme l'erreur (`KeyError`, `TypeError`) mais pas la ligne |
| `J9-D` absent de toute la ligne Q1 ; `J9-P` absent d'une ligne V dès la répétition 50 ; bras à projection absents de toute la ligne Q9a | arrêt par l'enveloppe |
| **`J9-D` absent de toute une ligne V** | **accepté, sans message (C1)** |
| `promue` écrit comme chaîne de caractères | accepté (n7) |

**C1, démontré.** Sur les données A, j'ai retiré `J9-D` de toutes les répétitions de V3(0.8) :
- `verifier_format` accepte. La condition de la l. 726 est `l in B.LIGNES_V` ; `l` est un nom, `B.LIGNES_V` est une suite d'indices (`range(7, 22)`) ; le test est toujours faux. `B.LIGNES_H`, lui, contient des noms : la branche des lignes H est juste ;
- `lire_v3` rend un résultat complet. Le secondaire « J9-D contre J9 » y porte `n = 0`, une estimation et des bornes **non numériques**, et `gain: False`. P10 est dite fausse. Deux avertissements numpy, aucun arrêt ;
- le fichier `lecture.json` serait écrit et scellé, avec des valeurs non numériques.

Deux variantes de même sorte :
- le jumeau entier absent d'une ligne V : même issue ;
- `La-P` absent de toute une ligne V : le secondaire « La-P contre La » est rendu « sans objet », sans message.

**Correction proposée**, à la l. 726 : `if l in V` (les 15 noms), étendue à `J9-D40` et à `La-P` ; et un artefact à l'essai `test_format_inattendu_rend_une_garde_avec_message`. Une garde plus forte serait de comparer, pour chaque groupe réductible, la première répétition absente aux bornes de la règle (250 ou 500), que l'index scellé permet de connaître par son champ `reductions` ; je la signale sans l'exiger (n6).

**Gardes neuves que les essais du développeur n'éprouvent sur aucun artefact**, et que j'ai éprouvées : « réapparaît après une réduction », « sans répétition », « incomplet », et l'arrêt de `lire_rho` quand tous les rééchantillons sont écartés. Toutes les quatre se déclenchent pour leur raison. À ajouter aux essais dans la même passe.

**Replis silencieux** : aucun autre que C1. `lire_gain` sur l'ensemble I, tous rééchantillons écartés, lève `IndexError` en appel direct ; sous `lire_v3` l'enveloppe la rend en arrêt.

## 5. n1 à n5, artefacts de m4 et m7, essai v2 corrigé

| point | fait | remarque |
|---|---|---|
| n1 | oui : `scripts/jouer_idee_1_1_v3.py`, l. 90, `"version_lanceur": 3` | |
| n2 | oui : règle déclarée, arrêt avec message (lecture, l. 547 et 548) | essai sain et artefact |
| n3 | oui : 13 paires | **aucun verdict changé** : McNemar n'est que rapporté. Sur mes données, 195 tests, aux bons comptes sous réduction |
| n4 | oui : écartés comptés, niveau écrit dans la sortie, arrêt avec message | essai sain et artefact |
| n5 | oui : `rho_plus_primaires`, par un appel à part dans `lire_v3` | **aucun verdict changé** : `rho_plus` reste calculé par l'appel de la v1, sur J9-P seul. Vérifié sur mes données : `rho_plus_primaires["J9-P"]` est égal, champ pour champ, à `rho_plus["J9-P"]` ; La et Ld présents. L'appel neuf n'ajoute aucun arrêt possible : les rééchantillons écartés ne dépendent pas du bras |
| m4, artefact | oui | dent manquée et trou ensemble : les trois lectures rendues à part |
| m7, artefacts | oui | P5 « partielle » à 2 lignes ; une partie de P12 réfutée, « toutes vraies » faux |
| lectures à déclarer | oui : `LECTURES_DECLAREES`, jointes à `lecture.json` et, par `declarations_v3`, au fichier d'étape 0 et au bloc d'addendum imprimé | le script d'étape 0 imprime `res["declarations"]`, qui vient bien de `declarations_v3` (module, l. 390) |

**Verdicts de la lecture : aucun n'a changé.** Sur les données A et B, j'ai comparé le résultat de `lire_v3` à celui de `lire` du module v2 (le code de la v1, que N1 ne touche pas) : **toutes les clés communes sont égales**, cellules, dents, ρ, principale, ρ⁺, La, Ld, secondaires, garde P4, étage 8, issue, audit et prédictions comprises.

**L'essai v2 corrigé par un couple** (`test_…lecture_v3.py`, l. 178 et 179) : **légitime**. L'essai d'origine exigeait l'ensemble exact des clés de la décomposition. n4 demandait d'y ajouter le compte des écartés et le niveau. L'essai neuf exige toujours l'ensemble exact, avec ces deux clés, et garde le contrôle des trois intervalles. Le couple est déclaré au JSON.

## 6. Le lanceur ne rejoue que les essais v3 : suffisant

- Chaque fichier d'essais v3 contient **tous les essais de son v1 et de son v2**, par leur nom de fonction (projection 12, gardes 26 puis 29, banc 12 puis 15, lecture 12 puis 17 puis 23, exécution 8) ; aucun nom de v1 ou de v2 ne manque en v3.
- Les lignes de v1 qui ne sont plus en v3 sont des imports, un compte d'essais, des noms de scripts, l'enregistrement synthétique (N1), un essai factice de l'étape 0 refait pour M2, et l'ancien champ `verdict` de la garde P4 (m4). Aucun essai n'est affaibli.
- Les essais v3 importent le banc v2 et les modules restés en v1 (`projection_bras_v1`, `projection_commun_v1`, `projection_methodes_v1`, `attaque_projection_extrait_v1`, `vue_v9_v1`, `execution_v1`) : ce que les essais v1 et v2 couvraient de ces modules est donc rejoué sur les mêmes modules.
- Remarque déjà vraie en v1 : le lanceur n'a jamais rejoué les essais propres des modules partagés (`juge_v1`, `lois_v1`, et les autres) ; les copies tierces sont gardées par empreinte. La v3 n'y change rien.

## 7. Fichiers gelés, imports, mineurs

**Fermeture dynamique des imports** (les trois scripts v3 importés, la vue chargée, `declarations_v3` appelée) : 35 fichiers du dépôt chargés.
- Hors de `FICHIERS_GELES`, seulement les copies tierces (`code-organisme-94bfd92/orchestrator/pole/*`, `copie-nul-v9-a41b7b5/…/nul_v9.py`), gardées par `verifier_copie` et `verifier_copie_v9` avant le jeu, comme en v1 et v2.
- De l'idée 1.1, un seul module d'une version antérieure est importé : `banc_idee_1_1_v2.py`, inchangé et gelé. **Aucun module v1 ou v2 touché n'est importé.**
- La liste compte 48 fichiers, sans doublon, tous présents. Elle gèle aussi les sources v2 de l'essai d'égalité, le JSON des couples, `tests/conftest.py` et les sept essais v3. Les fichiers v1 en sortent : ils ne sont plus source d'aucun essai rejoué.

**Mineurs nouveaux** (aucun ne porte un verdict) :
- **n6** — `lecture_idee_1_1_v3.py`, `verifier_format` : la première répétition où un groupe réductible manque n'est pas comparée à la règle (250, 500). Un jumeau absent dès la répétition 7 est lu sur 7 répétitions, sans message. Le banc ne peut pas l'écrire ; à fermer avec C1 si la mère le veut.
- **n7** — même fonction : le type des valeurs n'est pas contrôlé. Un `promue` écrit en chaîne est lu comme vrai. Le banc n'écrit que des booléens (vérifié sur les 82 enregistrements).
- **n8** — `tests/test_…bout_en_bout_v3.py`, l. 33 à 49 : le réglage peut créer un champ `promue` absent (section 3). À rendre strict.
- **n9** — `execution_idee_1_1_v3.py`, l. 259, et `scripts/lire_idee_1_1_v3.py`, l. 68 : un enregistrement sans champ `r` arrête `charger_sortie` sur une trace `KeyError`, avant `verifier_format`. Le script ne rattrape que `GardeArret`. Démontré sur une tranche scellée. Le défaut ferme du côté de l'arrêt et rien n'est écrit, mais sans message propre.
- Forme : commentaire resté en « version 2 » (`execution_idee_1_1_v3.py`, l. 90) ; nom et commentaire restés en « v2 égal à v1 » (`test_…differentiel_v3.py`, l. 30 à 33).

## 8. Écarts au texte scellé

- **Écart nouveau : aucun.**
  - A2 lu « à 200 » : c'est la seule valeur que le banc écrit, et celle du texte.
  - ρ⁺ pour les trois primaires, aux quantiles de Bonferroni : c'est la définition gelée (« ρ⁺_X », « mêmes quantiles de Bonferroni »).
  - Arrêt quand tous les rééchantillons sont écartés : le texte dit « écarté et compté » ; sans aucun rééchantillon, il n'y a pas d'intervalle. L'arrêt remplace une trace.
  - La règle de réduction du banc est inchangée ; les secondaires réduits sont lus « sur leurs seules premières répétitions », comme le texte l'écrit.
- **E2 et E3** : inchangés, le banc n'étant pas touché. Ils restent au directeur.
- Lectures déclarées, sans écart, portées au bloc d'addendum : tableau des strates, règle des strates, niveau de la décomposition, paires de McNemar, ρ⁺ des primaires, m6, m9 à m11, comptes non écrits.

## 9. Essais rejoués

- Conditions : les sept fichiers `tests/test_organisme_idees_juge_idee_1_1_*_v3.py` ; un seul processus ; `nice -n 10` ; `OMP_NUM_THREADS=1` ; variables `GIT_*` retirées par leur nom, sans afficher aucune valeur ; sans cache.
- **Résultat : 149 passés, 0 échec, 263,38 s**, de 23:53:41 à 23:58:05 UTC. C'est le compte du rapport.
- Décompte par fichier, cas paramétrés comptés : projection 22, gardes 33, banc 44, lecture 27, exécution 8, égalité 13, bout en bout 2 ; total 149.
- À part, hors du dépôt : le rejeu de l'égalité (12 sur 12), la fermeture des imports, les deux lectures de bout en bout (A et B), 20 artefacts de format et le cas sain, 5 variantes de C1 et 4 épreuves de gardes.

## 10. Avant l'étape 0

1. **C1** : `lecture_idee_1_1_v3.py`, l. 726 et 727, avec son artefact à l'essai.
2. Dans la même passe, au choix de la mère : n6 à n9 et les quatre artefacts de gardes de la section 4.
3. Noms neufs (R12), différentiel déclaré, essais rejoués. Le différentiel sera court ; son contrôle aussi.
4. Ensuite : l'étape 0, puis le jeu après le mot du directeur sur E2 et E3 et l'addendum scellé.

## 11. Incidents de ma main

- Un premier passage coupé par le service, sans trace ; repris depuis le début (en tête).
- Mon premier script d'égalité lisait mal la forme des couples (une paire au lieu d'un dictionnaire `ancien`, `nouveau`) et a rendu « inégal » à tort ; corrigé, rejoué : 12 sur 12.
- Aucun fichier existant modifié. Un seul fichier créé dans le dépôt : ce rapport et son compagnon.
- Scripts de travail, vrais enregistrements d'essai et journaux : dans le dossier temporaire de la session, hors du dépôt.
- Aucune variable d'environnement affichée ; aucun appel réseau.
