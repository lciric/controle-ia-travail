# Contrôle du différentiel v4 → v5 du code de l'idée 1.1 (R2) — lentille « conformité au texte scellé » — contre `prereg/organisme-idee-1-1-poids-du-nul-v2.md` (`3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`)

- Auteur : contre-lecteur neuf, modèle C, sous-agent de la session mère. Je n'ai écrit ni le préenregistrement, ni le code des versions 1 à 5, ni leurs rapports, ni les contrôles précédents.
- Date (UTC, `date -u`) : 2026-11-16, de 13:16 à 13:25 environ. Code lu sur `main`, tête `4efae812` ; seul fichier non suivi de l'arbre : un script d'une autre session, hors de l'idée 1.1.
- Ce que je n'ai pas fait : aucun essai, aucun `pytest`, aucun calcul d'expérience (le processus 10918 de l'étape 0 v5 vivait à chaque vérification, `kill -0` : vivant à 13:16 et à 13:18) ; je n'ai donc **pas rejoué les quatre fichiers d'essais v5 ni l'essai d'égalité** (le développeur rapporte 102 sur 102, non vérifié par moi). Aucun fichier existant modifié, aucun commit, aucun réseau, aucune variable d'environnement affichée.

## 0. Verdict

**Jouable : étape 0 v5, puis jeu après addendum, sans nouveau mot du directeur sur ce point, sous réserve que l'addendum déclare l'écart de lettre décrit au § 1 (D5) et que la mère le porte à Lazar en une ligne d'information.** Aucune correction de code exigée.

- Ma lecture, nette : l'ajout du module est **l'exécution fidèle du préalable 1 (c)**, pas un changement de critère. C'est en revanche un **écart de lettre** à l'énumération des compléments et à la composition de la vue ; il est du même genre que E2 et E3 et que le complément R-2930, et il se déclare à l'addendum (§ 1, § 5).
- Rien d'autre ne change un critère, un seuil, une graine, une réduction, la règle de lecture ou la liste d'arrêt (§ 2). E2 et E3 sont inchangés (§ 3).
- Réserve de fond : la lecture contraire existe (§ 1.3) ; je dis pourquoi je ne la retiens pas, et ce que coûte de se tromper.

## 1. Le quatrième fichier : écart ou exécution fidèle ?

### 1.1 Ce que le texte dit (lignes du fichier scellé)

- **Compléments cités** : l. 38 à 43 — `banc_tricheurs_v9.py` (`7e4bff59…`, R-2930), puis `banc_tricheurs_v8.py` (`0be47e4b…`) et `banc_tricheurs_v7.py` (`ef016d25…`), provenances v1 et v2, essai d'origine `test_nul_v9.py` (`d42a50eb…`). `pole/nul_v9.py` : l. 78. **Aucun `attaque_goodhart_v2.py`** : le texte ne le connaît pas.
- **Ce que la vue contient** : l. 672 à 675 (préalable 1 (c)) — « une vue faite du paquet `pole` de `94bfd92`, de `pole/nul_v9.py`, de `demonstrations/` et de `essais/`, chaque fichier vérifié par empreinte ». Le module neuf n'est ni dans le paquet `pole` de `94bfd92`, ni `nul_v9.py` : **il ne tient pas dans cette énumération à la lettre**.
- **Ce que l'étape exige** : l. 672 « route première : les essais d'origine du v9 … **rejoués depuis le banc** » ; l. 692 à 704 : les seules raisons de ne pas rejouer un essai sont (1) il lit le dépôt tiers ou ses empreintes, (2) il lance le banc comme programme ou écrit hors du dossier de travail ; « un essai d'origine qui échoue ou ne s'importe pas pour toute autre raison n'est jamais déclaré "non rejouable" : pas de jeu » ; l. 706 à 708 « Aucune réécriture ne remplace un essai d'origine rejouable ».
- **Ce que le texte prévoit d'un module manquant** : l. 683 à 686 — « un module manquant ferait échouer le rejeu, donc le préalable » ; et l. 685 à 686 « Compatibilité … établie par le rejeu lui-même, pas avant ». Liste d'arrêt, l. 612 : « préalable 1 ou 2 non levé : pas de jeu ».
- **Précédent dans le texte** : l. 679 à 685 et l. 785 à 788 : les bancs v8 et v7 ont été découverts manquants au contrôle des brouillons, **versés par la mère** (« décision de la mère », R-2930), même commit `a41b7b5`, et le texte a été amendé avant scellement. L. 78 à 83 et `COMPAGNON_SEUL` du code : la copie contient déjà un fichier (`mutations_nul_v9.py`) que le texte ne cite pas, vérifié contre son seul compagnon.
- **Addendum** : l. 9 à 11 — il porte les empreintes du code, « qui ne change rien d'autre » ; l. 530 à 532 — temps, nombre de processus, durée attendue, réductions ; l. 494 (« liste dans l'addendum ») pour les essais réécrits, **aucun ici**.

### 1.2 Ma lecture

1. **Pas de changement de fond.** Le fichier est du même commit public `a41b7b5`, recopié octet pour octet (`PROVENANCE-complement-v3.md`, `a4a62a88…`), vérifié contre son empreinte et son compagnon avant la vue (`vue_v9_v2.py`, `verifier_copie_v9`, lignes 76 à 90 ; essai neuf dans `gardes_v5` qui refuse une altération). Il n'est importé que par l'essai d'origine, paresseusement (`test_nul_v9.py` l. 406, lu par moi) ; `nul_v9.py` ne le cite que dans une docstring ; aucun module du jeu ne l'importe (`grep` dans `src/` et `scripts/` : seulement des docstrings et la vue). Le jeu charge `nul_v9` depuis la copie, pas depuis la vue assemblée (`vue_v9_v2.charger`, l. 127 à 135) : **l'ajout n'entre pas dans le chemin du jeu**.
2. **C'est la seule voie conforme à la route première.** Les deux autres sorties sont écrites et fermées : déclarer l'essai « non rejouable » (interdit : l'erreur d'import n'est pas l'une des deux raisons) ou le réécrire (interdit : « aucune réécriture ne remplace un essai d'origine rejouable »). Le verser, c'est faire jouer l'essai d'origine tel qu'écrit.
3. **Le critère de l'essai n'est pas déplacé** : même `test_nul_v9.py` (`d42a50eb…`), mêmes 37 essais, même règle « tous passent ».
4. **Ce qui reste d'écart : la lettre** — énumération des compléments (trois fichiers de banc, l. 38 à 43) et composition de la vue (l. 673 à 675). Je l'appelle **D5** pour la suite (suite de D1 à D4 du contrôle v4).

### 1.3 La lecture contraire, et pourquoi je ne la retiens pas

- Elle dit : l. 683 à 686 écrivent la conséquence d'un module manquant — « donc le préalable [échoue] » — et la liste d'arrêt dit « pas de jeu » ; la sortie de « pas de jeu » serait « texte neuf », donc nœud de décision (CLAUDE.md : « écart à un préenregistrement scellé »), donc mot de Lazar.
- Pourquoi non : (i) cette phrase décrit l'échec d'un **rejeu**, qui a eu lieu et a été consigné (R-2976, `etape0-idee-1-1-v4.json`, `bloquants` : « préalable 1 (c) : pas de jeu : essai d'origine en échec ou réécriture absente », `jeu_permis` faux, 36 sur 37) ; elle n'interdit pas de **repasser** le préalable après un versement, le texte disant lui-même que la compatibilité « s'établit, avant l'addendum » (l. 664 à 666) ; (ii) le texte a déjà traité ce même cas deux fois comme une **décision de la mère** (bancs v8, v7, v9) ; (iii) la liste d'arrêt n'a pas de ligne « module non listé versé » : rien de gelé n'est franchi (aucun critère, seuil, graine, réduction ou règle de lecture).
- **Coût d'une erreur de ma part** : si le directeur jugeait l'écart de lettre à lui, le jeu lancé sur l'addendum de la mère devrait être revu après coup ; le fond ne bougerait pas (le module ne touche pas le jeu). C'est pourquoi je demande la **déclaration à l'addendum et une ligne d'information à Lazar**, sans retarder l'étape 0.

## 2. Rien d'autre ne change

Vérifié par `diff` direct v4 → v5 sur chacun des dix fichiers, **et** par un rejeu indépendant des couples (script de ma main, hors du dépôt : chaque source v4, chaque « ancien » présent au nombre `n` déclaré, couples appliqués dans l'ordre, ajout de fin, comparaison octet pour octet à la cible) : **10 égaux sur 10**, aucun écart de nombre d'occurrences.

- **Vue** (`vue_v9_v2`) : docstring ; deux entrées dans `EMPREINTES_V9` (module `3c9de8b8…` et `PROVENANCE-complement-v3.md` `a4a62a88…`, égaux à leurs fichiers et compagnons, recalculés) ; constante `COMPLEMENT_V3`. Aucune autre empreinte ni autre fonction touchée. Les autres empreintes (`nul_v9.py` `7ae450df…`, essai `d42a50eb…`, bancs) sont inchangées.
- **Étape 0** : docstring ; import de la vue v2 ; `declarations_v5()` = `declarations_v3()` plus la clef `complement_copie_v9`. **Aucun seuil, graine, essai d'égalité, mutation ou calcul de la garde P4 touché** (mutations v4 et banc v2 : même fichier qu'au commit `d39e1bf9`, `git diff --stat` vide).
- **Exécution** : nom du run en v5 et refus des runs v1 à v5 ; `FICHIERS_GELES` : 46 fichiers, sans doublon, tous présents ; retirés : les 15 fichiers v3 et deux fichiers v4 de différentiel (déjà sources d'un contrôle fait), ajoutés : les 12 fichiers v5 ; `ESSAIS` : les essais v5 plus `lecture_v4` et `projection_v4`. Aucun critère, graine, réduction ou limite de durée. `PROCESSUS_MAX` (trois) inchangé.
- **Trois scripts** : docstrings, imports, nom de commande, `version_lanceur` 5, chemin de sortie de l'étape 0. Le jeu lit `processus` et `reductions` à l'addendum et refuse une reprise qui les change (`jouer_idee_1_1_v5.py` l. 118 à 131) : **comportement v4 conservé**.
- **Essais** : imports et noms ; un essai neuf de la vue (complément listé, vérifié, refusé si altéré) ; une assertion sur la clef `complement_copie_v9` ; l'essai d'égalité neuf.
- **Lecture, mutations, banc, juge, lois, seuils du texte** : fichiers identiques à ceux contrôlés en v4 (lecture `1ce2d5f9…`, mutations `c5a5fed8…`, banc `c3d77494…`), compagnons égaux. Tous les compagnons des onze fichiers v5 recalculés : égaux.
- **Fichiers sans compagnon dans `FICHIERS_GELES`** : `src/controle_ia/__init__.py`, `gardes.py`, `scellement.py`, `manifeste.py`, `prereg.py`, `tests/conftest.py` — hérités de la v4 à l'identique ; leurs empreintes entrent à l'addendum par la liste (comme le texte l. 12 le dit pour `prereg.py`). Pas un écart nouveau.

## 3. E2 et E3 (GO-2026-11-16-01)

**Inchangés.** E2 (le jeu appelle les fonctions internes du juge et du v9) et E3 (« J9-Dc sans coût de plus » faux) vivent dans le banc `banc_idee_1_1_v2.py`, `juge_v1.py`, `lois_v1.py` : aucun n'est touché par la v5. L'acceptation (GO-2026-11-16-01, 3) vise ces deux écarts nommés ; **elle ne couvre pas D5**, qui est neuf.

## 4. Autres points de conformité au texte

- **Liste d'arrêt** : aucune ligne modifiée dans le code ; la ligne l. 612 (« copie de `nul_v9.py` ≠ `7ae450df…` ») garde son empreinte.
- **Étape 0 rejouée en entier, mêmes graines** : le texte interdit de rejouer les graines **après un échec de la garde P4** (l. 515 à 518 : « jamais de graines rejouées ») ; or la v4 n'a **pas** échoué sur P4 (H7 sans garde 86 et 58 sur 200, 0 sous gel ; Hn 19 et 9, 0 sous gel, `etape0-idee-1-1-v4.json`, `resultat`). La v5 n'ouvre donc pas de seconde chance : le code de la garde est le même, les comptes sont déterministes. **À l'addendum : inscrire les comptes de la v5 et dire s'ils sont égaux à ceux de la v4** ; toute différence est un cas R4 (audit avant jeu), car le code n'a pas changé.
- **Chronométrage et processus** : la v4 donnait `D_h` 10,07 heures à `processus` 3 ; la v5 tourne à **deux processus** (R-2979). Le texte permet p ≤ 3 « inscrit à l'addendum » (l. 641 à 643) et exige D ≤ 32 heures : le chiffre de la v5 est celui du fichier d'étape 0 v5, que je n'ai pas lu. Le jeu devra tourner au nombre de processus de l'addendum, ni plus ni moins (garde déjà dans le lanceur).
- **Durée** : 30 lignes × 1 000 répétitions inchangées ; aucune réduction attendue (v4 : aucune) ; à confirmer sur le fichier v5.
- **Nom du run** `idee-1-1-poids-du-nul-v5` : nom neuf (R12), cohérent avec le jeu.

## 5. Ce que l'addendum d'empreintes devra déclarer

1. **Le complément de la copie** (bloc `complement_copie_v9` de `declarations_v5()`) : `orchestrator/pole/attaque_goodhart_v2.py` `3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703` ; provenance `PROVENANCE-complement-v3.md` `a4a62a888adf273779ffe198cab9b958692106ea1208efc4aaf79bf02c63cfac` ; même commit `a41b7b5` ; R-2976 ; **et la phrase d'écart D5** : « le texte ne cite comme compléments de la copie que les bancs v7, v8, v9 ; la vue contient en plus ce module, requis par l'essai d'origine `TricheursParMorceaux.test_monde_w2_de_l_attaque_membre_du_nul_v9` (l. 406 de `test_nul_v9.py`) ; écart de lettre à l. 38 à 43 et 673 à 675, sans effet sur un critère ; le module n'entre pas dans le chemin du jeu ». Le bloc du code porte déjà la remarque ; je demande qu'elle cite les lignes du texte et que l'addendum la classe comme **écart de lettre D5**, à côté de E2 et E3, avec renvoi à R-2976, R-2978 et à ce contrôle.
2. **La liste des empreintes** : la liste de `scripts/etape0_idee_1_1_v5.py --lister-empreintes` (46 fichiers gelés plus les copies tierces, y compris les deux entrées nouvelles de la copie du v9).
3. **Le préalable 1** : (a) 16 noms ; (b) E9 ; (c) rejeu des 37 essais d'origine de la v5, avec le résultat de **l'étape 0 v5** (pas celui du développeur, qui n'est qu'un rejeu à titre d'essai) ; **aucun essai déclaré non rejouable ni réécrit** (liste vide) ; vue : nombre de fichiers (58 chez le développeur, à confirmer sur la sortie officielle) et empreinte de la liste (`96107ec2…` chez le développeur).
4. **Les points D1 à D4 du contrôle v4** (lecture v4 inchangée, mêmes lignes : l. 785 à 786, 754, 766, 772, 708 à 720) : à déclarer tels quels, **comme dans le contrôle v4, § 9**, sans nouveau tour.
5. **Nombre de processus** (deux), durée attendue D, réductions (aucune si le fichier le confirme), temps par bras : ceux du fichier d'étape 0 v5.
6. **Comptes de la garde P4** de la v5 (H7 et Hn, sans garde et sous gel), avec la mention « égaux à ceux de la v4 » ou l'écart (§ 4).
7. **Mention de l'écart du premier échec** : l'étape 0 v4 (`c6c34fd0…`) est gardée, versée, **non effacée** ; la v5 la remplace pour le préalable 1 (c) seul ; les autres comptes sont identiques par construction.

## 6. Ce que je n'ai pas pu vérifier

- Le résultat de l'étape 0 v5 (en cours : je ne l'ai pas ouvert).
- Les 102 essais v5 et l'essai d'égalité : non rejoués par moi (processus 10918 vivant). Je les remplace par : `diff` direct des dix couples, rejeu des couples (10 sur 10), empreintes des onze fichiers et de leurs compagnons, relecture de la liste gelée, lecture du chemin de la vue.
- La vérification que les 37 essais d'origine passent sur la vue v2 : seulement par le rapport du développeur (37 sur 37, 43 s).

## 7. Avant l'étape 0 et le jeu

1. Rien à corriger dans le code v5.
2. Porter D5 et le bloc de déclarations à l'addendum (§ 5) ; une ligne d'information à Lazar sur D5.
3. Étape 0 v5 en cours : en lire la sortie par un sous-agent neuf (R2), comparer les comptes P4 à ceux de la v4, puis addendum scellé, puis jeu au nombre de processus de l'addendum.

## 8. Incidents de ma main

- Aucun incident de fond. Une première commande de vérification des compagnons (`sha256sum -c` depuis la racine) a échoué sur les chemins relatifs des compagnons ; refaite par comparaison des empreintes : égales. Un script jetable d'analyse de la liste gelée a échoué une fois (nom d'attribut) ; corrigé, rejoué.
- Calculs de ma main : hachages, `diff`, un script de rejeu de couples (quelques millisecondes) et un script de lecture syntaxique de la liste gelée, tous en priorité la plus basse (`nice -n 19`), pendant que le processus 10918 vivait ; aucun essai, aucun `pytest`.
- Je n'ai rien ouvert ni écrit sous `diag/`, `runs/`, `donnees/`, ni dans `/home/user/jeu-idee-1-2-copie`, ni dans `/home/user/etape0-idee-1-1-copie-v5`.

## Déclaration d'exclusion

- Rôle : contre-lecteur neuf (R2), lentille « conformité au texte scellé », différentiel v4 → v5 du code de l'idée 1.1. Modèle : lettre C.
- Heures (UTC, `date -u`) : 2026-11-16 de 13:16 à 13:25 environ.
- Pièces lues, empreintes recalculées : `rapport-code-idee-1-1-v5.md` `6ce11448a382ab16…` ; `couples-v4-vers-v5.json` `61008bafa5b51cd9…` ; `controle-differentiel-code-idee-1-1-v4.md` `9ba07614ea7bc081…` ; `prereg/organisme-idee-1-1-poids-du-nul-v2.md` `3ffe1739aa83ea8d…` ; `etape0-idee-1-1-v4.json` `c6c34fd0ae823d9f…` (clefs `bloquants`, `jeu_permis`, `prealable_1`, `programme` seulement) ; `PROVENANCE-complement-v3.md` `a4a62a888adf273779…` (v1 et v2 : empreintes `032eaeeb…` et `c38ba643…` recalculées ; texte lu pour la v3 seulement) ; `attaque_goodhart_v2.py` `3c9de8b83b6fcf198d…` (imports et lignes 140 à 160 seulement) ; `test_nul_v9.py` (lignes 400 à 410) ; `vue_v9_v1.py` `ff2db3d6…` et `vue_v9_v2.py` `bab7b645…` ; les dix fichiers v5 et leurs sources v4 (différentiel direct) ; `lecture_idee_1_1_v4.py` `1ce2d5f9…`, `mutations_idee_1_1_v4.py` `c5a5fed8…`, `banc_idee_1_1_v2.py` `c3d77494…` (empreintes seulement) ; lignes R-2976, R-2978, R-2979 de `registres/decisions.md`, R-2942 et R-2950 (grep), ligne GO-2026-11-16-01 de `registres/go.md`.
- Jamais ouvert : la sortie de l'étape 0 v5 ; rien sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, P3-bis ni du bras d'attaque ; `/home/user/jeu-idee-1-2-copie` ; `/home/user/etape0-idee-1-1-copie-v5` ; aucune valeur de clé ; `env` ni `printenv`.
- Incidents de ma main : § 8.
