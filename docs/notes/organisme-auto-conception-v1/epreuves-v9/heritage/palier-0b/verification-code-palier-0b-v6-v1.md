# Vérification du code de l'étage sur processeur du palier 0b, version 6 — v1

Vérificateur neuf, modèle S (n'a écrit ni le texte, ni le code v1 à v6, ni leurs vérifications, ni l'audit). 2026-11-20. Pièce de travail (classe C) sur une pièce d'instrument (classe B). Rien n'est lancé, rien n'est écrit dans le dépôt.

## Verdict : **Conforme**

Aucune correction exigée. Quatre points à la mère (§ 6), aucun bloquant.

## 1. Empreintes
- Mandat (`6e9980f5…`), mandat du développeur (`46a5e1a4…`), v13 (`d9591d5b…`), audit (`8e965f80…`), vérification v5 (`0e2c46bb…`), table v6 (`639335b9…`), rapport v6 (`0f408c6f…`) : égaux à ceux du mandat.
- `sha256sum -c` de la table sur `code-v6/` : 64 lignes, 64 OK. Compagnons `.sha256` de chaque fichier de `src/`, `tests/`, `outils-dev/` et du rapport : tous OK. La table v6 ne diffère de celle du v5 que par : 4 fichiers de `src/` changés (`etalonnage`, `etapes`, `graines`, `tirages`), 2 essais changés (`statistique`, `verrou`), 1 essai neuf (`lancement`), `mutations_v5.py`, `lancer_etapes_8_et_9_v1.py` et 3 sorties du banc neuves. 24 fichiers sous `src/` (23 du paquet + `src/controle_ia/__init__.py`).

## 2. Différentiels v5 → v6 (`diff -u`, refaits)
`graines.py` : un seul morceau (champ `mode` inséré après `repere` dans `ORDRE_DES_CHAMPS`) ; aucune ligne d'`Autorisation`, du verrou, de `exiger_autorisation_pour`, de `ecrire_manifeste`/`verifier_manifeste` ne change (ces deux dernières, et `mecanique.py`, `mondes.py`, `statistique.py`, `analyse.py`, `frequences.py`, absents du différentiel). `etalonnage.py` : une fonction ajoutée (`lire_reglages_geles`). `tirages.py` et `etapes.py` : seulement les sept points de l'audit. Essais `statistique` et `verrou` : trois appels adaptés à la signature neuve, rien d'affaibli. `mutations_v5.py` contre `mutations_v4.py` : 4 lignes retirées (docstring, sélection de partie), les 113 défauts du v4 intacts, 34 ajoutés.

## 3. Le code contre la v13 et les sept points
1. **Cases « sources », champ de mode, aucune graine existante ne change** : éprouvé à part (script `etiquettes_du_plan.py`, étiquette de chaque case du plan entier, réglages plantés tous atteignables, v5 contre v6) : les lignes du mode « tirages » et leur empreinte sont identiques ; seules les cases « sources » changent d'étiquette (`mode=sources`) et de nom (`-sources`). Et par un petit lancement joué dans les deux codes (`sorties_v5_v6.py`, couche « essai », 3 cases) : empreintes des `M1`, `D`, `I`, `fausses_tenues`, `lecture-*` égales à l'octet ; liste des étiquettes égale ; ne changent que les `case.json` et les 3 ou 5 `reliquat-bras-*` neufs par case.
2. **Mode dans le nom** : juste ; deux cases de même nom arrêtent avant tout tirage et toute autorisation (`verifier_cases`).
3. **`lancer_famille`** : clé de chaque case (une et une seule), un appel, un manifeste par étape ; contrôles de taille gelée (10 000 / 200 000 sous « decisif », grille entière ; sous « confirmation », seules les cases de C1 et C4, 100 000, nombres lus). Conforme à B8, étape 8, annexe C.
4. **Reliquat et enrichissement** : `enrichissement` appelée, sorties `source-*` aux seules cases du repli en mode « sources » (B8, famille D ; S7, M7) ; reliquat par bras aux deux modes. Inventaire du rapport § 6 relu ligne à ligne contre T:393 : juste.
5. **`etape_8`** : relecture des gelés par empreinte (réglages : compagnon, nom de base, garde 22), plan entier, un seul lancement, manifeste inscrivant les empreintes vérifiées et les cases « non atteignables », aucune case lue.
6. **`etape_9`** : manifeste de l'étape 8 vérifié, couche, gelés confrontés, comptes de C1 et C4 depuis les seules sorties scellées (72 et 72 exigés), retrait de la case entière lue aux nombres retirés, rien d'écrit sans case à confirmer, statut par `regle_de_confirmation`. Conforme à C1, C4 et à l'audit (c).
7. **Docstring d'`etapes.py`** corrigé ; verrou (a) à (e) et garde 27 inchangés (différentiel).

Programme `outils-dev/lancer_etapes_8_et_9_v1.py` : lu, non lancé. Il n'a ni couche ni taille en paramètre, refuse un dossier existant, n'écrit à la sortie que chemins, empreintes et nombre de cases ; signature des appels (`Autorisation`, `Graines`, `etape_8`, `etape_9`) vérifiée contre le code. Rien à corriger.

## 4. Essais et banc, rejoués sur une copie du code
- Collecte : 117 essais, dont 10 dans `lancement`.
- **Suite entière, un processus : 117 passés, 0 échoué (1 465 s)**, variables `HERITAGE_DEPOT` et `HERITAGE_COPIE_ORGANISME` (dossier `orchestrator/` de `code-organisme-94bfd92`) comme au v5. L'essai final « aucune graine décisive » passe (seul et en suite). Fichiers joués seuls : `lancement` 10, `verrou` 24, `statistique` 11, `gardes` 17, `outils` 15, `zz` 1 passés (`etapes`, `mecanique`, `mondes`, `organisme` : vus en suite seulement).
- **Banc `mutations_v5.py`** : `--verifier` : 147 défauts, 147 identifiants distincts, 0 problème. Rejoué en trois parties : « v3 » 71 appliqués, 71 vus ; « v4 » 42 et 42 ; « v5 » 34 et 34 ; **147 sur 147, chacun par un essai de code 1, aucun code 2 ou plus, témoins au vert**. Trois défauts neufs revus à la main sur leur copie mutée (`etape-9-couche-non-controlee`, `lot-d-une-source-accepte`, `enrichissement-mal-pris`) : chacun échoue sur l'assertion visée, non sur une erreur de montage.

## 5. Sorties v5 → v6
Mon rejeu est plus petit que celui du développeur (3 cases, pas 531 empreintes) : il confirme la règle (rien ne change hors du point 3 et du point 4), non le compte « 526 sur 531 » lui-même, que je n'ai pas rejoué. Les cinq sorties changeantes du rapport (`case.json` ×2, `sorties_scellees`, deux manifestes) et les six neuves (`reliquat-bras-1 à 3`) relèvent des points 3 et 4 ; mon rejeu y retrouve `case.json` et les `reliquat-bras-*`.

## 6. Les 19 silences et la liste de l'erratum v14
- **Justes, à inscrire comme proposé** : n° 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19.
- **À la mère, avec ma recommandation** :
  - n° 3 (source étrangère de H = suivante du même lot) : accepter ; sans effet sur la loi, un lot de 2 000 n'arrête jamais.
  - n° 4 (reliquat = somme sur les quatre générations) : accepter, mais l'erratum doit dire que la ventilation par génération n'est pas conservée ; si l'analyse la veut, c'est un code v7.
  - n° 13 (compagnon des fréquences contrôlé sans le nom de base) : laisser ; l'égalité d'empreinte est exigée, seul le nom de base n'est pas comparé.
  - n° 16 (dénominateur de R pris à la famille B) : accepter, à écrire à M7.
- **Liste de l'erratum (rapport § 7), onze points** : juste et complète. Précisions : au point 7, la phrase « aucun programme de lancement des étapes 8 et 9 n'existe encore » figure à deux lieux, B8 (paragraphe « Graines », « n'existant encore », ligne 332 de la v13) et silence n° 14 (ligne 991) ; les corriger tous deux. Aux points 9 et 10, les comptes d'essais deviennent 117 (10 pour `lancement`) et celui du banc 147, que j'ai rejoués.
- **Points hors liste, pour la mère** : (a) le temps de calcul et la mémoire de l'étape 8 aux tailles gelées ne sont estimés nulle part (le rapport le dit) ; l'essai de forme de l'annexe C n'est pas étendu au mode « sources » (silence n° 18) ; à décider avant le GO s'il faut une mesure sous la couche « essai-de-forme » ; (b) `lancer_etapes_8_et_9_v1.py` n'est pas contrôlé par le verrou (hors paquet) : la pièce de contrôle de la mère devrait inscrire son empreinte (`67052a4b…`) ; (c) le programme d'analyse de l'étape 10 reste à écrire (remarque 1 du rapport) ; (d) un texte v14 demande un GO qui le nomme (nœud de l'audit).

## 7. Écarts à mon mandat
- Un `ls` du dossier `orchestrator/` du code de l'organisme, hors des dossiers permis, pour y trouver `exemples/` et `pole/` que lisent les essais ; sans effet.
- Les trois parties du banc et la suite ont tourné en parallèle sur quatre processeurs partagés ; les durées en sont allongées, non les résultats.
- Deux scripts à moi (fichiers, pas de code en ligne) dans mon dossier : `etiquettes_du_plan.py`, `sorties_v5_v6.py`.
- Aucun refus de permission, de classifieur ni de garde. Aucune écriture dans le dépôt, aucun appel à un fournisseur, rien sous `archives-reponses-modeles/` ni `/root/.claude/`.

Signé : vérificateur, modèle S.
