# Vérification de la version 4 du code des verdicts de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, B-β)

- **Vérificateur neuf** (R2) : n'a écrit, contre-lu ni vérifié aucune pièce de ce travail (ni le texte gelé, ni le code v1 à v4, ni les essais, ni la contre-lecture de la v1, ni les vérifications de la v2 et de la v3). Rien lu sous `registres/` ni `diag/`. Aucun autre fichier modifié, rien committé ; sondes jetables hors du dépôt (dossier temporaire de la session).
- **Date** : 2026-11-18 05:31 UTC (`date -u`).
- **Vérification ciblée et étroite** : les points de la vérification de la v3, le diff v3 → v4, l'égalité exigée entre les deux résultats de la relance commune aux audits A1 et A5. Le reste du module n'a pas été relu ligne à ligne.
- **Empreintes vérifiées** (recalculées, égales aux compagnons `.sha256`) :
  - `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py` : `8c07434f9db0e35e10eb806218da320bc0d6e404e41c4f60c495b35906d88b87`
  - `tests/test_neuron_lens_verdicts_b_beta_v4.py` : `1b63c8cbbcdff180e0a3433ebeb139eea3c4aeeb13fcc3f694352219a4f7bb5a`
  - `src/controle_ia/neuron_lens/verdicts_b_beta_v3.py` : `3c4572f209328afc66487c02072ea6b2b3bce9dcb51b2d864b158d3b80b4f10b`
  - `tests/test_neuron_lens_verdicts_b_beta_v3.py` : `a4f7f8b55a71e033678efb2e54588035e77898fd370c0de19c6768b531fd1eda`
  - vérification de la v3, `verification-verdicts-b-beta-v3.md` : `79605cac67cf46774902ee06731f8b3bb6914ceec2d339d790e06895e091eb2c`
  - sortie versée des essais v4, `sortie-essais-verdicts-b-beta-v4.txt` : compagnon vérifié (82 passés ; « contre la v3 : 6 échecs, 76 passés »)
  - texte qui fait foi, `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` : `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`
- **Ce qui a été fait** : lecture de la vérification de la v3, du diff v3 → v4 du module (9 groupes de lignes) et des essais, du module v4 en entier, des lignes du texte gelé sur `read_S`, la part silencieuse, l'accord du premier jeton et les audits A1 et A5 ; essais v4 rejoués (82 passés, comme la sortie versée) ; les mêmes essais joués contre le module v3 (6 échecs, 76 passés) et contre le module v2 (22 échecs, 60 passés) par copies jetables ; 16 mutations d'une copie jetable du module v4, chacune rejouée contre les essais v4 ; environ 60 sondes jetables (égalité des deux résultats, `nan`, objets numpy, tables mal formées, garde (g), bornes de [0, 1]) ; comparaison de la v3 et de la v4 sur 44 000 entrées tirées au hasard (graines fixées).

## Verdict : **employable**

Le majeur N1 de la vérification de la v3 (résultat de l'audit A5 écarté sans message) est corrigé et prouvé par un essai qui échoue sur la v3. Les six mineurs n2 à n7 sont corrigés dans le code ; chacun a son essai, sauf deux restes de forme. Le diff ne change rien d'autre : sur 44 000 tirages, toute différence entre la v3 et la v4 est l'une des quatre voulues. L'égalité exigée entre les deux résultats est sûre dans le sens qui compte : elle ne laisse jamais passer deux résultats différents ; elle peut seulement refuser à tort, avec bruit, des tables portées par des tableaux numpy.

Comptes : bloquant 0 ; majeur 0 ; mineurs neufs 6.

## (1) Points repris

Essais v4 joués contre le module v3 : 6 échecs, ceux des essais neufs — résultats différents pour les audits A1 et A5 : 1 ; garde (g) sans déclencheur et réserve : 1 ; table de la graine 1 à `None` : 1 ; valeurs hors de [0, 1] : 3.

| point | état dans la v4 | essai qui échoue sur la v3 (vérifié) | mutation de la v4 | reste |
|---|---|---|---|---|
| **N1, majeur** — les deux audits A1 et A5 déclenchés, seul le résultat de A1 lu | **corrigé** (l. 350-351) : deux résultats qui ne sont ni le même objet ni égaux sont refusés (`ValueError`, message du module). Sondes : témoin manqué dans A5 seul, dans A1 seul, une valeur de table différente, un n différent, une lentille en trop, « non joué » pour l'un seulement → tous refusés ; même objet, deux copies profondes égales, deux lectures `json` du même contenu → acceptés, même verdict que la v3. | `test_a1_a5_resultats_differents_refuses` : échoue sur la v3 (verdict rendu au lieu du refus) | retour au contrôle de la v3, contrôle retiré, identité seule sans égalité : les trois tuées | rien |
| n2 — `declencheurs` rend des audits sous une différence entre moitiés non finie | **corrigé** (l. 288-289) : liste vide. Sondes : `nan` et `inf`, avec les déclencheurs de A1, A4 et A5 réunis → `[]`, puis `verdict` rend « chaîne en défaut (g) ». | `test_g_sans_declencheur_et_avec_reserve_a6` (première assertion) | retour anticipé retiré : tuée | la condition de la l. 293 est devenue toujours vraie (forme, neuf n-d) |
| n3 — essai de m4 non discriminant | **corrigé** : clé en trop à 0,01 (aucun audit) ; valeur négative avec le résultat de l'audit A2 fourni. | **échoue sur la v2**, les deux cas (`test_stabilite_refusee[cle_en_trop]`, `[negative]`) ; passe sur la v3, attendu (la v3 portait déjà la correction du code) | clés exactes retirées, négatif accepté : les deux tuées (elles survivaient à la v3) | rien |
| n4 — réserve de l'audit des deux codes sous la garde (g) sans essai | **essai ajouté** (`test_g_sans_declencheur_et_avec_reserve_a6`, dernière assertion) ; code inchangé. | sans objet (code déjà juste) ; l'essai échoue sur la v3 par sa première assertion seulement | réserve retirée : tuée | rien |
| n5 — table ou n de la graine 1 à `None` | **corrigé** (l. 345-347) : `score` et `n` doivent être des tables, sinon `ValueError` avec message ; contrôlé même quand le témoin est manqué. Sondes : `None`, liste → refus du module ; table vide → refus de `valider_table`. | `test_table_graine1_none_refusee` (la v3 levait `TypeError`) | contrôle retiré : tuée | un `None` un cran plus bas lève encore `TypeError` (neuf n-e) |
| n6 — valeurs hors de [0, 1] | **corrigé** (l. 125, 129) : accord du premier jeton, `read_S` et part silencieuse exigés dans [0, 1], bornes comprises (0, 1, `-0.0` acceptés ; −10⁻¹², 1 + 2·10⁻¹⁶, `nan`, `inf` refusés). Conforme au texte : les trois grandeurs sont des parts (« part des pôles… », l. 135, 154-157). | `test_valeurs_hors_de_0_1_refusees` (3 cas) | bornes retirées, haute seule, basse seule, bornes strictes : tuées, **sauf** la borne basse de l'accord retirée, qui survit (neuf n-c) | n-c |
| n7 — commentaire « inchangées » ; pièces muettes sur les mineures restantes | **corrigé pour le commentaire** (l. 136 : « reprises ; lectures déclarées en tête »). | sans objet | sans objet | l'en-tête des essais ne dit toujours pas quelles mineures anciennes restent (reste de m1, reste de m2) : neuf n-f |

## (2) Le diff v3 → v4 ne change rien d'autre

Le diff du module tient en neuf groupes : en-tête (3), bornes de [0, 1] (2), commentaire (1), retour anticipé de `declencheurs` (1), contrôle des tables (1), égalité des deux résultats (1). Aucune ligne de mesure, de garde, de rang ni de seuil n'est touchée.

Comparaison sur 44 000 entrées tirées (20 000 générales ; 6 000 forçant les deux audits avec le même objet ; 6 000 avec deux copies profondes égales ; 6 000 avec deux résultats tirés à part ; 6 000 avec des valeurs hors de [0, 1]) ; résultats d'audit tirés (joués, manqués, « non joué », table de la graine 1 retouchée dans 40 % des cas) :

| | égal | différent | explication de chaque différence |
|---|---|---|---|
| `declencheurs` | 42 959 | 1 041 | 178 : différence entre moitiés non finie, liste vide en v4 (n2) ; 863 : valeur hors de [0, 1] refusée par la v4 (n6) |
| `verdict` | 38 218 | 5 782 | 3 440 : deux résultats différents pour les audits A1 et A5, refusés par la v4, verdict rendu par la v3 (N1) ; 1 479 : « non joué » pour l'un seulement, refusé par les deux, seul le message change ; 863 : valeur hors de [0, 1] refusée par la v4 (n6) |

Aucune différence inexpliquée. Là où les deux versions rendent un verdict, tout est égal : verdict d'ensemble, défauts, réserves, état des audits, verdict et valeurs de chaque mesure (15 553 chaînes en défaut, 2 315 « non conclu », 7 « non reproduit », 16 523 « reproduit », 3 820 « partiel »). Les 6 000 tirages à deux copies profondes égales sont tous acceptés à l'identique.

Entrées que la v4 refuse et que la v3 acceptait, toutes bruyantes (`ValueError`) : deux résultats différents pour les audits A1 et A5 ; accord, `read_S` ou part silencieuse hors de [0, 1]. Entrée où seule l'erreur change : `score` ou `n` de la graine 1 qui n'est pas une table (`TypeError` → `ValueError`).

## (3) L'égalité `==` sur des tables imbriquées est-elle sûre ?

**Oui dans le sens qui compte ; non sans bruit pour les tableaux numpy.**

- **Aucun passage à tort.** Le résultat lu est celui de l'audit A1, entièrement validé (`valider_audits`, puis `valider_table` si le témoin tient). Si `==` rend vrai, le résultat de A5 a les mêmes clés, les mêmes booléens (stricts, contrôlés avant, dans les deux) et des tables égales en valeur ; le code ne lit ces tables que par des comparaisons numériques. Écarts que `==` ne voit pas : `0.0` contre `-0.0` (le déclencheur de A1 compte les deux comme zéro), `0.5` contre `numpy.float64(0.5)`, 64 contre `numpy.int64(64)` — sans effet sur un verdict (sondé).
- **`nan`.** Deux tables portant `nan` au même endroit : même objet ou copie profonde → l'égalité passe (Python compare d'abord l'identité), puis `valider_table` refuse (« valeur absente ou non finie ») ; deux objets `nan` distincts → refus par l'égalité (message « identiques », trompeur mais bruyant). Dans les deux cas refusé. Seule issue sans refus : témoin ou norme manqué, où la table n'est pas ouverte et la chaîne en défaut (l) est rendue — déjà relevé sans reproche à la vérification de la v3.
- **Objets numpy.** `valider_table` accepte des tableaux numpy pour les séries et pour n. Deux résultats distincts portés par des tableaux, **même égaux**, lèvent l'erreur de numpy (« The truth value of an array with more than one element is ambiguous ») : c'est une `ValueError`, donc bruyante et sans verdict faux, mais le message n'est pas celui du module et un essai `pytest.raises(ValueError)` la prendrait pour le refus voulu. Le même objet, ou une copie superficielle (mêmes tableaux), passe. Des listes de scalaires numpy se comparent bien. Mineur neuf n-a.
- **Liste contre tuple** de mêmes valeurs : refusé (bruyant). Un objet dont `==` rend toujours vrai (sous-classe de table écrite exprès) trompe le contrôle, comme il trompait déjà la lecture de « non joué » : hors de toute entrée qu'un code de course produit, non retenu.

## (4) Points neufs

Aucun bloquant, aucun majeur.

| rang | lieu | constat vérifié | correction proposée |
|---|---|---|---|
| mineur n-a | `valider_audits`, l. 350 | Deux résultats distincts dont les tables sont des tableaux numpy : erreur de numpy au lieu du message du module, même quand ils sont égaux. Bruyant, aucun verdict faux. Sans objet si le code de course passe le même objet aux deux audits, ou des listes lues d'un fichier `json`. | Écrire dans la description de `verdict` : « le même objet, ou des listes » ; ou comparer après mise en listes ; un essai. |
| mineur n-b | même lieu | Deux objets `nan` distincts au même endroit : refus sous le message « identiques » au lieu de « non finie ». Bruyant. | Aucune, ou valider les tables avant l'égalité. |
| mineur n-c | essai `test_valeurs_hors_de_0_1_refusees` | La borne basse de l'accord du premier jeton n'a pas d'essai : la mutation qui la retire survit (l'essai ne pose que 1,01). Code sondé juste. | Un cas à −0,01 pour l'accord. |
| mineur n-d | `declencheurs`, l. 293 | Condition devenue toujours vraie après le retour anticipé de la l. 288 ; son commentaire décrit un cas qui n'arrive plus. Forme. | Retirer la condition. |
| mineur n-e | `valider_table`, l. 91-99 | `None` un cran sous la table de la graine 1 (`score[cible]`, `score[cible][lentille]`, `n[cible]`) : `TypeError` de Python sans message du module. Bruyant. Reste de n5. | Contrôler le type à chaque niveau, ou attraper `TypeError` et la relever en `ValueError`. |
| mineur n-f | en-tête des essais ; `valider`, l. 125-129 | Aucune pièce de la v4 ne dit quelles mineures anciennes restent (reste de n7). Entrées encore acceptées, déjà dans la v3 : un booléen comme accord, une chaîne « 0.5 » comme `read_S`. Sans effet sur une entrée bien formée. | Trois lignes en tête des essais ; exiger un nombre. |

## Non vérifiable

- Que le code de course passe aux audits A1 et A5 le même objet, ou des listes lues d'un fichier `json` : ce code n'est pas parmi les fichiers donnés ; c'est ce qui borne la portée du mineur n-a.
- Que l'accord du premier jeton, `read_S` et la part silencieuse sortent toujours dans [0, 1] des scripts du dépôt voisin (`lens_compare.py`, `reads_at_firings.py`), sans dépassement d'un cheveu par arrondi flottant : scripts non lus ; le texte gelé les définit comme des parts. Un dépassement donnerait un refus bruyant à l'étape des verdicts, sans verdict faux.
- Que la différence entre moitiés est calculée avant l'appel à `declencheurs` sur la machine, ce dont dépend que la liste vide de la garde (g) épargne bien les audits.
- Les points « non vérifiable » de la vérification de la v3 (booléens Python du code de course, forme de la sortie de `score` à la graine 1, gardes constatées sur la machine, lectures reprises de la tranche précédente) : inchangés, non réexaminés ici.
