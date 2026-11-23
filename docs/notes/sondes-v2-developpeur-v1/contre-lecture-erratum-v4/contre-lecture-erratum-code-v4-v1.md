# Contre-lecture de l'erratum de code des sondes v2 (lecture v2, statistiques v2, monde planté v4, chargeurs des trois formats) — v1

- **Contre-lecteur** : Opus 5.5 (`claude-opus-5-5`), neuf, n'a pas écrit ce code. Classe B (instrument). Aucun fichier du dépôt modifié.
- **Date (UTC, `date -u`)** : lun. 23 nov. 2026, 08:42Z (début de la lecture).
- **Dépôt** : `/home/user/controle-ia-travail`, branche `sondes-v2/code-v2`, commit `29ecef82d`, arbre propre.
- **Cloisonnement** : rien lu sous `diag/` ni `runs/`, aucun chemin « coffre », « verdict », « sel », « barreau5 » ou « b5 » hors du code de `src/controle_ia/sondes_v2/` (seul `magasin_v1.py` a été ouvert, pour l'expression `_CHEMIN_B5` et `series_depuis_barreau5`), aucune autre branche, aucun résultat de sonde. Aucun appel réseau, aucune dépense, aucun sous-agent.
- **Aucun résultat de sonde dans ce rapport.** L'essai d'égalité entre la v3 et la v4 (B, point 3) n'imprime que des booléens.

## Fichiers lus (sha256)

| fichier | sha256 |
|---|---|
| `docs/notes/sondes-v2-concepteur-opus-v1/decisions-concepteur-sondes-v2-v2.md` | `cb27059038cc7d9467913f9fb56af189d94dfecd06639d6ed49a179383ea84c6` |
| `docs/notes/sondes-v2-concepteur-opus-v1/erratum-1-decisions-et-plan-v2.md` | `019cff392fbd5e5403f0b1d07c1fddc0e9b8303745aaf72845ef9b34543249ed` |
| `docs/notes/sondes-v2-concepteur-opus-v1/spec-note-des-effectifs-v2.md` | `0ebc790aacf9dcd3c52ac497d699e22ac5cf4c05c182a388a82871d90c66585b` |
| `docs/notes/sondes-v2-concepteur-opus-v1/spec-correspondance-rejeu-croise-v2.md` | `31296b05a10d31a3c53bb6085b27fb3d1caa5ac3a84c6658637ca29e7e7c5aa6` |
| `docs/notes/sondes-v2-concepteur-opus-v1/spec-table-de-l-ouvreur-v2.md` | `7e48bc24b35374595bb74feb84fab83ce0fa7dd2a32cc718aec75f7c88a047a3` |
| `docs/notes/sondes-v2-concepteur-opus-v1/plan-epreuve-plantee-et-devis-v2.md` (§ 1 à 3) | `717cea17b031d7d8a9439d0cbcef41eafdff52fcba3cfeb207ae39886ef76462` |
| `docs/notes/sondes-v2-concepteur-opus-v1/verites-mondes-plantes-v4-projet-v2.json` | `b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533` |
| `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json` | `b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533` (identique à l'octet, `cmp` ; compagnon conforme) |
| `src/controle_ia/sondes_v2/statistiques_v2.py` | `2399780c7eb4f7b52fc777cc594f4ca703d994af1623c026b1f67eb3a42c7056` |
| `src/controle_ia/sondes_v2/lecture_v2.py` | `8463175747ea724f14486ae3771392bef5148f5751225c5774144970dd426fdf` |
| `src/controle_ia/sondes_v2/monde_plante_v4.py` | `afef0d5508d5f1146e7c6c3c9e0e6e6e68f5a2a7212ebb390c2342c4c7f1a960` |
| `src/controle_ia/sondes_v2/programme_monde_plante_v4.py` | `e73d93a18eaef8ee32b736e3c51d429d0346f924d8648639e81fbf59bdfe79ea` |
| `src/controle_ia/sondes_v2/formats_v1.py` | `e8a63e4a7fb847c0c54bf15ba11bc56d3a0bd7859d5357c8b2dbcad800f557c9` |
| `tests/test_sondes_v2_erratum_v4.py` | `fb93c75662754cef15a7c27101ec569369d986f5f4787ac5d0cf8b99d586bc88` |
| `tests/test_sondes_v2_formats.py` | `8d3967cac55fd32009712e03da6b7a2f3eb509ec5c5acd863269e7778a1d07eb` |
| référence : `statistiques_v1.py` | `c498147816094592fdb75fa8513a76e93f4e7a675a70f50a3d2a92a5931404a8` |
| référence : `lecture_v1.py` | `d9cefb660bda8ca0f8d650c3dd26c517345ba4cfd482fd66f6f186af16bd7633` |
| référence : `monde_plante_v3.py` | `0381e42955a94f8ef717850b77d7f8581063b0c02bc6ffa81eab18ac002ceb6c` |
| référence : `programme_monde_plante_v3.py` | `db1679a3766d371da7ed0e8e34bb8db6860c7a3ac2adde5030437a194b456561` |
| référence : `magasin_v1.py` (extraits) | `9bb3cc48918c7e1855da1b2f82ffe3529030ffb3fb3bb7f0072236020dddee32` |

## Verdict

**Bon après corrections.** Les points 1 à 9 du § 7 (lus avec l'erratum 1) sont codés fidèlement sur le fond. Je ne trouve aucun défaut majeur. Trois défauts moyens portent sur des gardes de chargeur ou de fusion qui manquent ou ne sont que facultatives. Il y a onze défauts mineurs. Aucune règle ne peut se choisir sur résultat dans l'épreuve plantée.

- Essais : `PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py` donne **171 passés, 1 sauté** en 96 s.
- R12 : `git diff --stat 00b60266d -- src/controle_ia/sondes_v2/ tests/` ne montre que des fichiers neufs (cinq modules, les vérités v4, deux fichiers d'essais et leurs compagnons). La v1, la v3 et les vérités v1 à v3 n'ont pas changé. Les empreintes compagnons sont conformes.

## A. Fidélité au § 7 (avec l'erratum 1)

| point | état | où |
|---|---|---|
| 1. Contraste | conforme. `contraste_testable` rend faux si max(2^(1−P), 1/(1+R)) > α, avec R = `n_nul`, le nombre de rejeux demandés. Ensuite « établie » si p ≤ α, « non établie à cette puissance » sinon. « nul_principal » suit la même règle. `contraste_apparie` rend `nature = MENTION_DESCRIPTIF` sans aucun libellé. Ce que le test rejette est écrit dans la documentation (`CE_QUE_REJETTE_LE_CONTRASTE`). Le plafond est recalculé et concorde avec la table du § 1 (vérifié à la main pour P = 6, R = 39). Réserve : voir m1, sur la différence entre R demandé et R effectif. | `lecture_v2.py:44-68`, `monde_plante_v4.py:133-137` |
| 2. Q10 | conforme. Comparaison « ≤ α » dans `lecture_signee`, dans le contraste, dans « nul_principal » et dans « texte ». Les fonctions de la v1 qui appellent `lecture_signee` en interne n'existent pas, donc rien ne retombe sur le « < » de la v1. | `lecture_v2.py:35-41`, `monde_plante_v4.py:161` |
| 3. E-2, trois gardes | conforme, et chaque garde est éprouvée. Case absente : « case manquante : (poids, source) ». Case d'origine sans ligne « origine » : « chemin d'une case différent du texte scellé ». Ligne « origine » sur une case relue : arrêt nommé. | `statistiques_v2.py:52-68`, essai `test_rejeu_v2_gardes_e2` |
| 4. E-8 et cas mixte | conforme. Quand toutes les tâches ont un contrôle, l'écart se calcule par tâche (moyenne de origine − relu, réduite par l'écart type du pli) et la valeur corrigée vaut brute − 2 × écart. Dans le cas mixte sans règle fixée, le code s'arrête avec le motif « règle du cas mixte non fixée » avant toute lecture corrigée. `regle_cas_mixte` n'a pas de défaut. | `statistiques_v2.py:116-139` |
| 5. Deux seuils, mêmes valeurs p | conforme. `libeller_rejeu` travaille sur une copie profonde et reprend les valeurs ajustées par Holm, sans nouveau tirage. Les lectures `interaction_holm` et `interaction_brute_holm` (seuil α / D) sont dans `CRITERES`. Les générateurs sont dans le même état en v3 et en v4 après une lecture complète (voir B). | `statistiques_v2.py:211-234`, `monde_plante_v4.py:143-147` |
| 6. Grandeurs et plafond | conforme pour l'essentiel : interaction brute et corrigée, aire principale, U et ρ (avant et après contrôle) ; moyenne et quantiles 0,05, 0,5, 0,95 ; nombre de rejeux et plafond du contraste par monde au mode complet. Écart à la lettre « par famille » : voir m7. | `monde_plante_v4.py:162-164`, `programme_monde_plante_v4.py:104-110` |
| 7. Vérités v4 | conforme. Copie identique à l'octet (`b310e1af…`), chargée par la v4 avec le format exigé. Écart à la v3 vérifié par programme : seuls les critères des mondes « interaction », « interaction contraire » et « décalage de chemin » changent (deux gardes de signe bornées à 0,10, puissance à α / D, critère des 80 % déplacé vers `interaction_brute_holm`). Aucun monde ni aucune composante ne change. | `monde_plante_v4.py:38, 168-183` |
| 8. Chargeurs | présents, avec un essai sain et des essais d'artefact pour la plupart des gardes. Lacunes : C ci-dessous, M1, M3, m3 à m6, m9. | `formats_v1.py` |
| 9. Plages de répliques | conforme. Les graines dérivent de `{mode}/{case}/{monde}/{r}/`, comme en v3, et jamais de la plage. La synthèse fusionnée est identique à l'octet à celle d'un processus seul (essai). Les gardes de plage, de contiguïté et de couverture sont en place. Lacune : M2. | `programme_monde_plante_v4.py:133-237` |
| 10. Vitesse | **confirmé non fait** : aucun code de vitesse dans le diff (facultatif). | — |

## B. Correction, cas limites, égalité avec la v1 et la v3

1. **Ordre des tirages** : il est le même en v3 et en v4. La v4 n'ajoute que des copies et des lectures sans tirage. `rejeu_croise` v2 consomme `reechantillonnage` et `signes` dans le même ordre que la v1 (brute, corrigée, résiduelle) dès que toutes les tâches sont contrôlées ou qu'aucune ne l'est, les deux seuls cas que produit `table_rejeu`.
2. **Le cas mixte n'arrive jamais dans les mondes plantés**. `table_rejeu` relit toutes les origines ou n'en relit aucune. L'arrêt nommé n'est donc éprouvé que par l'essai sur table fabriquée, ce qui est conforme.
3. **Essai d'égalité v3 contre v4** (script du bloc-notes `eq/eq.py`, d = 32, 8 paires, 8 tâches, 3 actions, 19 rejeux, 2 répliques par monde, booléens seuls). Mondes : identité seule, interaction, interaction contraire, décalage de chemin, étiquettes permutées, texte seul, fuite de pli, trace faible.
   - Toutes les lectures non modifiées sont égales : interaction, interaction brute, sans contrôle, décalage maîtrisé, transport, transport après contrôle, identité, fuite.
   - Les états des générateurs nommés sont égaux après la lecture.
   - À D = 1, les lectures au seuil de Holm sont égales aux lectures à α.
   - Seule diffère la lecture « texte » du monde « texte seul ». C'est le changement Q10 attendu : avec 19 rejeux, la plus petite valeur p vaut exactement α, si bien que « < » ne peut jamais lire « établi » alors que « ≤ » le peut.
4. Résiduelle v2 contre v1 : sortir une colonne constante ou nulle ne change pas la projection, donc les résidus restent égaux en arithmétique exacte. L'ordre des plis est maintenant trié (la v1 itérait un ensemble). Les deux changements sont neutres, mais voir m2.

## C. Gardes des spécifications non appliquées ou non éprouvées

- **Note des effectifs, § 4** : les quatre gardes nommées sont appliquées et éprouvées (compagnon faux, champ manquant ou en trop, nombre non entier, clé de rôle). Manquent la cohérence de la case complète (M1) et plusieurs contrôles de valeur (m4, m5).
- **Correspondance, § 3 et 4** : les gardes « empreinte fausse », « colonne absente », « valeur non prévue », « quatre cases » (sous forme de doublon d'action), « clé sans jumelle comptée » et « règle non permise » sont appliquées et éprouvées. Manquent : les colonnes non finies (m3), la sélection vide et les clés de `valeurs` (m6). Les contrôles « recodage hors des valeurs admises » et « champ qui demande une colonne » ne sont pas éprouvés (m9).
- **Ouvreur, § 3 et 4** : toutes les gardes de la liste sont appliquées. « Verdict non inscrit au registre » n'est que facultative (M3). « nu de type nu », « deux familles partagent (recette, dose) », « producteur inconnu » et « dose non numérique » ne sont pas éprouvées (m9).

## D. Ce que le code fait sans qu'on le lui ait demandé

- Les trois règles nommées du cas mixte (`REGLES_CAS_MIXTE`, options a, b, c du § 6, point 3) sont **acceptables**. Aucune n'est un défaut, la conduite sans règle reste l'arrêt nommé, et toute autre valeur arrête. Dans l'épreuve plantée, la règle n'a aucun effet, puisque le cas mixte n'y arrive jamais. Elle ne peut donc pas être choisie sur un résultat de l'épreuve. Elle n'y est pas non plus mise à l'épreuve, ce qui est une réserve pour le concepteur.
- Le risque est ailleurs : rien ne lie `--regle-cas-mixte` à l'additif scellé ni à la note (m11).
- Le reste du code ajouté est demandé par une spécification ou neutre : les colonnes constantes sorties de la résiduelle, « variable absente » dans les prédicteurs triviaux, et `charger_table_ouvreur` qui rend les cases hors de la grille.

## Défauts

### Moyens

**M1 — `formats_v1.py:153-172` : case complète partiellement contrôlée.**
- Ce qui ne va pas : seules `complet.taches` (minimum sur les doses des tâches tenues) et `doses_holm` sont confrontées à la règle du § 3. `complet.actions` n'est pas confrontée à « minimum, sur les quatre cases, de max(1, arrondi(actions de la case / tâches)) ». `complet.paires` n'est pas fixée à 8 « par convention » : seul ≥ 2 est exigé.
- Conséquence : `cas_depuis_note` passe ces valeurs telles quelles au mode complet, qui gouverne la ligne du rejeu croisé. Une note fautive gouvernerait donc sans arrêt. L'essai sain lui-même porte une case (8, 11, 3) dont les actions ne sont pas vérifiées.
- Correction : pour chaque dose et chaque case, calculer max(1, `arrondi_moitie_bas`(Σ actions de la case sur les plis / tâches tenues de la dose)). Exiger que `complet.actions` soit égal au minimum de ces valeurs sur les doses et les cases, et `paires == 8`. Si la lecture « par dose » n'est pas celle du concepteur, le faire préciser par un erratum de la spécification. Éprouver par un artefact.

**M2 — `programme_monde_plante_v4.py:199-237` : la fusion ne vérifie pas que les plages viennent du même code.**
- Ce qui ne va pas : `fusionner` compare le format, le mode, les vérités, les arguments et l'entropie. Il ne compare ni `manifeste.commit`, ni `manifeste.depot_propre`, ni `manifeste.reserves`. Des plages jouées sur des commits différents, ou l'une d'elles sur un arbre sale autorisé, se réuniraient en une seule synthèse au nom d'un seul code.
- Autre manque : la fusion rend la synthèse sans la sceller et sans la liste des empreintes des rapports réunis.
- Correction : exiger le même `commit`, `depot_propre` vrai partout (ou les mêmes réserves) et le même `config_sha256` hors de `plage`. Ajouter une fonction qui écrit et scelle la synthèse fusionnée avec les empreintes des rapports. Éprouver sur deux rapports de commits différents.

**M3 — `formats_v1.py:328, 346-351` : garde « verdict non inscrit au registre » facultative.**
- Ce qui ne va pas : par défaut, `chemin_registre=None`, et la garde se réduit au motif `R-\d+`. Or la spécification en fait une condition d'ouverture (liste d'arrêt).
- Correction : rendre `chemin_registre` obligatoire (ou sans défaut) et éprouver l'appel sans registre.

### Mineurs

**m1 — `monde_plante_v4.py:133-137`, `programme_monde_plante_v4.py:110` : R demandé ou R effectif ?**
- Ce qui ne va pas : la testabilité et le plafond emploient R = `n_nul`, le nombre demandé. La valeur p, elle, vaut (1 + b)/(1 + R_eff), où R_eff = `npr["repliques"]` : `lecture_v1.py:709-713` écarte jusqu'à 1 % de répliques dégénérées.
- Conséquence : à 199 rejeux et α = 0,005, une seule réplique dégénérée rend « établie » inatteignable alors que la règle déclare le contraste testable. Le mandat dit « rejeux demandés », les décisions disent « tirés ».
- Correction : lire la testabilité sur R_eff (plus prudent) et rapporter les deux nombres, ou faire trancher le concepteur.

**m2 — `statistiques_v2.py:176-184` : constance testée sur le mauvais ensemble (hérité de la v1).**
- Ce qui ne va pas : la constance d'une variable est testée sur tout le pli, alors que la régression n'apprend que sur les honnêtes. Une variable constante chez les honnêtes mais variable chez les saboteurs est colinéaire à la constante dans `X[h]`. `lstsq` rend alors la solution de norme minimale, et la prédiction pour les saboteurs dépend de ce choix arbitraire.
- Correction : tester `np.ptp` sur les seules lignes honnêtes, sortir la variable et la nommer.

**m3 — `formats_v1.py:271-293`, `statistiques_v2.py:141-143`, `statistiques_v1.py:425` : valeurs non finies ou illisibles.**
- Ce qui ne va pas : un « nan » ou une valeur infinie dans `longueur` ou `pas`, colonnes déclarées présentes, est rapporté « variable absente ». C'est un repli silencieux au sens de R5. Un texte non numérique lève `ValueError` et non `GardeArret`, pour le score comme pour les variables.
- Correction : arrêter, avec motif, sur une valeur non finie d'une colonne déclarée présente, et convertir les `ValueError` en `GardeArret`.

**m4 — `formats_v1.py:94-175` : valeurs de la note non contrôlées.**
- Les valeurs de `minimums` (« atteints | non atteints »), leurs clés par dose et leur cohérence avec la règle des 8 tâches et 40 actions.
- `chemin_de_calcul.source` ∈ {manifeste, attestation}.
- `identique_pour_toutes_les_series` et `nu_relit_les_cles_communes` booléens, avec une réserve exigée s'ils sont faux.
- Une seule série « nu », et des doses distinctes.
- `actions_en_origine_et_en_relu` > 0 avec `taches_avec_controle_du_chemin` = 0, ou l'inverse : l'incohérence est lue « contrôle absent ».

**m5 — `formats_v1.py:82, 176-183` : clé de retour et calcul du cas mixte.**
- La documentation annonce la clé `cas_mixte`, le code rend `controle_du_chemin`.
- Le cas mixte est calculé sur toutes les doses réunies, alors que E-8 se lit dose par dose. Une dose entièrement contrôlée à côté d'une dose sans contrôle est déclarée « cas mixte ». C'est prudent, mais cela porterait un nœud inutile à Lazar.
- Correction : calculer par dose et rendre l'état de chaque dose.

**m6 — `formats_v1.py:230-233, 252` : sélection vide et clés de recodage.**
- Une sélection qui ne retient aucune ligne rend une table vide, sans arrêt.
- Les clés inconnues de `valeurs` sont ignorées.
- Correction : arrêter sur une table vide après sélection, et appliquer `_cles_exactes` aux clés de `valeurs`.

**m7 — `programme_monde_plante_v4.py:104-106` : grandeurs « par famille » et répliques manquantes.**
- En mode étalon, U et ρ de toutes les familles d'une case sont réunis dans un seul résumé, et non résumés « par famille » (§ 7, point 6).
- Les répliques sans grandeurs (ligne non calculée) ne sont pas comptées dans `non_finies`. Seul `n` le laisse voir.
- Correction : résumer par indice de famille, et compter les répliques manquantes.

**m8 — `programme_monde_plante_v4.py:240-249, 282-290` : extension et doses en mode étalon.**
- Avec `--note-effectifs`, en mode étalon et extension déclenchée, la grille de 416 cases part sans garde, alors que le plan exige un devis neuf et un GO neuf.
- `--doses-rejeu` est ignoré sans le dire en mode étalon.
- Correction : refuser l'extension sans un drapeau explicite qui cite le GO, et refuser `--doses-rejeu` en mode étalon.

**m9 — Gardes appliquées mais non éprouvées sur un artefact (R5).**
- Ouvreur : « nu doit être de type nu », « deux familles partagent le couple (recette, dose) », « producteur inconnu », « dose numérique », empreinte d'adaptateur mal formée.
- Correspondance : recodage hors des valeurs admises, champ qui demande une colonne, valeur vide de `longueur`.
- Note : empreinte hexadécimale mal formée, `nombre_de_doses` différent du nombre de doses listées.
- Fusion : entropies ou vérités différentes.
- Correction : ajouter un essai d'artefact pour chacune.

**m10 — `formats_v1.py:361-373` et `magasin_v1.py:561-562` : poids des séries propres et contrôles d'unicité.**
- `poids_par_serie` ne porte pas les séries propres, et `series_depuis_barreau5` leur donne alors son défaut silencieux (adaptateur nommé, dose inconnue). C'est conforme à la lettre de la spécification (§ 4), mais c'est à signaler au concepteur.
- Ni l'unicité de `empreinte_adaptateur` ni le préfixe `propre-` ne sont contrôlés.

**m11 — `programme_monde_plante_v4.py:274, 286-290` (question D) : règle du cas mixte sans lien avec l'additif ni la note.**
- `--regle-cas-mixte` s'accepte sans référence à l'additif scellé qui doit la fixer.
- L'état du contrôle du chemin rendu par la note n'est pas employé : une note « cas mixte » ne bloque pas le lancement sans règle, et une note « contrôle absent » accepte une règle.
- Correction : exiger `--additif-cas-mixte CHEMIN`, vérifié par son compagnon, dès qu'une règle est passée. Refuser une règle si la note ne dit pas « cas mixte ». Arrêter au lancement si la note dit « cas mixte » sans règle.
- Pour le futur programme de lecture, appliquer la même liaison.

## Remarque pour le concepteur (hors code)

Le critère de fausse lecture du contraste dans le monde « étiquettes permutées » (borne haute 0,10, lecture admise « établie ») passe sans rien prouver si le contraste est « non testable à cet effectif ». À la case prévue (8 paires, 39 rejeux, α = 0,05), il est testable. Dans une autre case, il faudrait lire ce passage avec le plafond rapporté à côté.

**Verdict : bon après corrections. Défauts : 0 majeur, 3 moyens, 11 mineurs.**
