# Rapport du développeur — code de l'étage 1 de la ligne 3, corrections de la contre-lecture (C1, C2, C3) — v2

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel), sous le mandat `mandat-developpeur-code-etage-1-ligne-3-v3.md` (`8d7e9a36bd4c4cf7aaaad49c3a9dd69996f40b5b3f7e7657dc101ed2d246a281`, égal à son compagnon). Il garde l'objet et les interdits des mandats v1 et v2.

Les fichiers n'existent que dans le bloc-notes du développeur (`…/developpeur-etage-1-ligne-3-v3/code-etage-1-v2/`). Rien n'est écrit dans le dépôt (arbre propre avant et après), rien n'est committé, rien n'est poussé. Le v1 n'est pas touché.

## Verdict

Les trois corrections sont faites :
- **109 essais passés, 0 échoué**.
- **70 défauts réintroduits sur 70 vus**, dont **les 35 mutants de la contre-lecture**, que ce soit par les essais visés ou par le fichier d'essais entier (méthode de la contre-lecture).
- Un seul changement de calcul : C2. Aucun tirage ne change.

## Pièces lues, empreintes recalculées

| pièce | sha256 | contrôle |
|---|---|---|
| texte qui fait foi, `git show origin/main:prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (après `git fetch origin main`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | égale à l'attendue |
| `contre-lecture-code-etage-1-ligne-3-v1.md` | `3aed6849c76a4ed421207470e4a6b8a45fcecf6a8ef5325a5203c84fda2f85ff` | égale au mandat et à son compagnon |
| `mutants_cl.py` | `c3ece475abba3de912b99e6589e787190da19e1c13957262f4e57bab133ef6a0` | égale à son compagnon |
| `rapport_ctrl_cl.json` | `02bd16c536fb91cf23d20e723a3ab12ee3f71929d65b4529e61ea921fe873cf7` | égale à son compagnon |
| `banc_juges_scriptes_ligne_3_v1.py` | `1d474cc905c25351ce3c4cc2c2a0661cefca353c31898c353700e34f8dd4ca0f` | égale |
| `essais_banc_juges_scriptes_ligne_3_v1.py` | `13b2b8988825091e0f1c6af99cffff75d94efb1b640ffef99131dfd3bfb2e174` | égale |
| `controle_defauts_reintroduits_ligne_3_v1.py`, `chronometrer_banc_ligne_3_v1.py`, `rapport-defauts-reintroduits-ligne-3-v1.json`, `rapport-developpeur-code-etage-1-ligne-3-v1.md` | — | chacune égale à son compagnon |
| mandats v1 et v2 du développeur | — | lus |

Environnement : `scripts/verifier_environnement_agent_v1.py` (`9714a00f…`). Python 3.13.18 (`/usr/local/bin/python3`), numpy 2.5.3, pytest 9.1.1.

Remplacements : par `scripts/remplacer_texte_exact_v1.py` (`391db990…`) pour le banc, le chronométrage et les essais, à partir des fichiers v1, et pour une reprise du contrôle. Le JSON des essais est construit par un programme écrit en fichier. Le contrôle v2 est un fichier neuf.

## Fichiers rendus (dossier `code-etage-1-v2/`)

| fichier | sha256 |
|---|---|
| `banc_juges_scriptes_ligne_3_v2.py` | `ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3` |
| `essais_banc_juges_scriptes_ligne_3_v2.py` | `d90eb6f3d8ad4772b274ba53e70e2c2e21b12ba5b094c2ac6646fde326200fe2` |
| `chronometrer_banc_ligne_3_v2.py` | `9bcea5306fd444afffbcc8a8a13565d7cba103d27be858e8f9c9161f66176e74` |
| `controle_defauts_reintroduits_ligne_3_v2.py` | `1ead27755f433e4e88bbd6ff4b72605ce22ab24b4b7c96741f89245a1a6afd7f` |
| `rapport-defauts-reintroduits-ligne-3-v2.json` (mode « visé ») | `09f089cf9ce159d020c91657bad12b820b9ad4f9eefc41618c0a1ec2133e89be` |
| `rapport-defauts-reintroduits-fichier-entier-ligne-3-v2.json` (mode « complet ») | `fde1277c219c5322356494374906c6d0f0ed925adda1e183b647f5a6b7a068dc` |
| `rapport-developpeur-code-etage-1-ligne-3-v2.md` (ce rapport) | dans son compagnon |

Chaque fichier a son compagnon `.sha256`. Les journaux de l'outil de remplacement (différentiels exacts v1 → v2) sont dans `…/developpeur-etage-1-ligne-3-v3/brouillons/b01/` et `b02/`.

Le chronométrage v2 ne change que le banc qu'il charge (v2) et le nom de son manifeste.

## Ce que fait la version 2

### C2 — branche (2), « à partir de laquelle » (seul changement de calcul)

Je lis le texte comme la contre-lecture : « la plus petite taille d'étalonnage à partir de laquelle la branche tient dans toutes les cellules » = la plus petite taille t de la grille (25, 50, 100, 200) telle que la branche tient dans toutes les cellules à t **et à toutes les tailles plus grandes de la grille**. Je n'ai pas d'autre lecture : je ne rends donc qu'une grandeur, et aucune question de texte n'est ouverte sur ce point.

- Nouvelle fonction `plus_petite_taille_a_partir_de_laquelle` ; `criteres_branche_2` rend la clé renommée `plus_petite_taille_d_etalonnage_a_partir_de_laquelle_la_branche_tient_partout` (l'ancienne clé `…_ou_la_branche_tient_partout` disparaît, pour qu'aucun lecteur ne prenne l'une pour l'autre).
- J'ajoute, comme information, la table `tient_dans_toutes_les_cellules_par_taille_d_etalonnage` (vrai ou faux par taille). Ce n'est pas une seconde lecture.
- Choix le plus étroit, déclaré : si une taille de la grille n'a aucune cellule (cela n'arrive qu'avec une configuration réduite d'essai), la clé vaut « incomplet : tailles de la grille sans cellule […] ». Ce n'est jamais un repli silencieux.
- Aucun tirage ne change ; seuls les noms changent par ailleurs (`VERSION`, fichiers de sortie `resultat-…-v2.json` et `manifeste-…-v2.json`, manifeste du chronométrage en v2).

### C3 — garde des graines, `verifier_autorisation` seule

- Essai sain : un additif factice présent, d'empreinte égale, est accepté pour 2026111931, 2026111932 et 2026111933, avec chemin `Path` ou chaîne. Le journal des dérivations et l'enregistrement des `SeedSequence` restent inchangés.
- Huit artefacts, chacun refusé avec son motif (`match=`) et sans dérivation : aucune autorisation ; type inattendu ; empreinte en majuscules, courte ou absente ; chemin absent ; chemin d'un dossier ; empreinte d'un autre fichier.
- Six défauts visés sur cette fonction seule (G01 à G06) : empreinte non comparée ; additif absent accepté ; absence d'autorisation acceptée ; empreinte mal formée non refusée comme telle ; additif valide refusé ; type non vérifié. Ils sont **tous vus**.
- Ces défauts sont protégés par une garde du contrôle, jouée avant tout lancement. Leur texte ancien doit se trouver dans le corps de `verifier_autorisation`. Leurs essais visés commencent par `test_verifier_autorisation_` et, avec les fonctions qu'ils appellent (analyse de l'arbre syntaxique), ne nomment ni `generateurs`, ni `Contexte`, ni `_gens`, ni `main`, ni `executer_etage_1`, ni `tirages`, ni `reechantillonnage`, ni le chronométrage. Ces défauts ne sont jamais joués contre le fichier entier.
- Le défaut sur `generateurs` reste non réintroduit, à raison (il ferait dériver une racine décisive).

### C1 — règles de lecture et constantes épinglées

Il y a 36 essais neufs, chacun sain et artefact, ou sain et artefact dans le même essai. Dans ce dernier cas, l'essai affirme aussi que la variante fautive **se distingue** sur le cas joué, pour qu'aucun essai ne passe par un cas qui ne discrimine pas.

- `mot_fa38` : 15 % contre chacune des deux références, référence « sans prise » sous 0,02 (0,019 et 0,021), marge de 0,05 sur les vrais rejetés, ordre des lectures. Dans une cellule à cinq juges rejouée, les références sont « poids égaux » et R à k = J, avec un mot par ρ′.
- Branche (2) : seuil de 0,02 par cellule ; taille d'étalonnage n / 2 ; lettre « à partir de laquelle » (C2) ; deux juges et loi hors branche ignorés.
- Branche (3) : seule la colonne δ = 0,5 est lue (artefact : parts à δ = 0,2 et 0,5 échangées) ; « plus de 10 % » strict ; « rapporté sans mot » pour le lecteur (c).
- Clause (i) : marge de 0,05 des vrais rejetés, « sans prise » sous 0,02, ordre « réfuté » avant « sans prise ».
- Constantes du « Seuil » et de la grille (tolérances, Holm 0,05, marge 0,05, puissance 0,5, niveau d'alarme 0,05 / 11, seuils de cadrage, ρ, n, taux, ρ′ de R, f, tailles d'étalonnage), plus la configuration décisive entière. La constante altérée est vue sur un faux module.
- Qualité de l'estimateur : biais 0,04 (tient) et 0,06 (non) ; erreur quadratique 0,09 et 0,11 ; couverture 0,90 (tient), 0,85 et 1,00 (non, audit levé) ; part « indéfini » 0,02 et 0,04 ; couverture comptée sur les seules répliques définies, intervalle indéfini compté « non couvrant ».
- Centiles 2,5 et 97,5 : `_centiles` sur une suite connue ; intervalle par répliques rejoué sur les mêmes tirages.
- Bras C : poids contre un calcul indépendant (S intra-classes / (n − 2), d, λ = 0,1 tr(S)/J, bornes), sans repli, le juge le plus exact plus lourd. Seuil au milieu des deux moyennes de classe (ni la moyenne globale, ni celle des bons).
- Bras P : plancher de 0,05 pour un juge à exactitude 0,5 ; paire à ρ = 0,67 divisée par deux, paires à ρ < 0 non divisées.
- Cellule à cinq juges rejouée sur les mêmes tirages (mêmes graines de la racine des essais) : stabilité = centile 95 de |écart| ; bras N « au moins q » ; bras R à k = 5, majorité « au moins 3 », pour les trois ρ′.
- Garde de cadrage rejouée : « dépasse » strict, avec des rondes exactement au seuil.
- Puissance de ρ′ − ρ rejouée : borne basse au centile 2,5.
- Monde de puissance rejoué : écarts observés, valeurs de probabilité `(1 + #{écart ≤ 0}) / (B + 1)`, Holm à 0,05, marge 0,05, R lié au juge 2. Les variantes Holm 0,10 et marge 0,10 se distinguent sur le cas joué.
- Alarme à seuils serrés, sur un générateur factice qui enregistre les appels et rend des comptes écrits d'avance (aucune graine) :
  - 69 cartes notables contre 50 tombent entre le seuil unilatéral (2,61) et le bilatéral (2,84) ; 71 cartes passent au-delà ;
  - la sentinelle est en alarme en génération 12 seulement sur une suite sans changement ;
  - valeurs exactes de détection, délai, fausse alarme, alarme avant changement et part des détections à effet, pour les bras A à D ;
  - arguments des tirages : génération du changement dans 4..10, référence 50 + 50, ancres m/2 + m/2, production 70 + 30, bras D à 70 % arrondi, taux du monde.

Les 73 essais de la v1 sont gardés tels quels, à leurs noms près (banc, chronométrage, fichiers de sortie en v2).

## Essais

`TMPDIR=<bloc-notes>/tmp python3 -B -m pytest -q -p no:cacheprovider essais_banc_juges_scriptes_ligne_3_v2.py` : **109 passés, 0 échoué** (9 s). Le premier brouillon passait déjà ; aucun essai n'a échoué en chemin. Ce n'est pas lu comme une preuve : la preuve des dents des essais est le contrôle ci-dessous, et chaque essai neuf affirme lui-même que la variante fautive se distingue.

## Contrôle « trop beau » (R4), rejoué

- **Mode « visé »** (`rapport-defauts-reintroduits-ligne-3-v2.json`) : essais visés sur le banc sain, 72 passés. **70 défauts sur 70 vus** :

  | famille | vus |
  |---|---|
  | v1 | 27 / 27 |
  | mutants de la contre-lecture, textes de `mutants_cl.py` recopiés à l'identique | 35 / 35 |
  | inverse de C2 | 1 / 1 |
  | « dépasse » strict de la branche (3) | 1 / 1 |
  | graines | 6 / 6 |

  Le rapport porte pour chaque défaut la ligne d'échec de pytest (`--tb=line`). Je les ai lues : chaque défaut échoue sur l'assertion qui le nomme (par exemple M13 sur « aucun repli », M24 sur la part déclenchée, M07 sur la fausse alarme 1,0 au lieu de 0,5, M33 sur `(4, 10, 8)`, G02 sur « DID NOT RAISE », G04 sur le motif, G06 sur `AttributeError`).
- **Mode « complet »** (`rapport-defauts-reintroduits-fichier-entier-ligne-3-v2.json`), méthode de la contre-lecture (fichier entier, `-x`) : fichier entier sur le banc sain, 109 passés ; **64 défauts sur 64 vus**. Les 6 défauts « graines » sont joués sur leurs seuls essais visés, et vus.
- **Mutants de la contre-lecture non vus : aucun.** Les 30 que la contre-lecture voyait passer sont tous vus, dans les deux modes.

## Graines

- Seule la racine des essais, 2026111930, a été dérivée pendant mon travail : essais, deux contrôles, essai du chronométrage à `--essai` compris dans les essais.
- Aucune graine de 2026111931 à 2026111937.
- L'essai final `test_zz_final_aucune_graine_des_racines_decisives_derivee` passe dans le fichier entier sur le banc sain, aux deux lancements des essais et au mode complet du contrôle. Sous un défaut, l'arrêt au premier échec (`-x`) l'empêche de tourner. Aucun défaut hors « graines » ne touche la garde des graines ; les défauts « graines » ne jouent que des essais qui n'appellent que `verifier_autorisation`.
- Aucun calcul décisif, aucun chronométrage à pleine taille.

## Questions de texte laissées à la mère (je ne tranche pas)

- **Silence 1** (relevé par la contre-lecture) : « part des alarmes qui portent sur un changement à effet ». Le code compte la part des détections de changement qui portent sur un changement à effet, et non la part de toutes les alarmes, fausses alarmes des suites sans changement comprises. L'essai neuf de l'alarme **épingle le calcul actuel** (0,5 sur le cas factice) ; il ne le choisit pas.
- **Silence 2** : l'alarme ne reçoit aucun mot calculé. Le texte ne donne que la borne de 0,08 de la fausse alarme, lue à la main.
- **A** : monde de la puissance de ρ′ − ρ (loi 1 emboîtée, taux 0,20, 100 témoins sans partage). L'essai neuf épingle la borne basse au centile 2,5, non ce monde.
- **B** : ρ′ du bras R fixé à 0 dans les mondes « unanimité » et « juge seul » (famille de Holm des quatre comparaisons, donc puissance qui décide).
- **C** : R lié au juge 1 à l'étage 1, au juge 2 dans le monde de puissance. Les essais neufs **épinglent les deux choix actuels** (cellule à cinq juges : juge 1 ; monde de puissance : juge 2, mutant M34 vu). Si la mère tranche autrement, l'essai change avec le code.
- **D** : alarme à un seul juge et composition des suites. L'essai factice épingle cette composition, sans la trancher.
- **E** : table gelée sans ligne pour « tient à n = 50 seulement » ; le code rend « cas non prévu, rendu à la mère ».
- **Constantes et configuration décisive** : l'essai épingle aussi les choix déclarés de la v1, qui ne sont pas la lettre du texte (par exemple `lois_J2 = [1, 2, 3]`, choix 2 ; tailles d'étalonnage 25 à 200, choix 1).
- **C2** : aucune divergence de lecture, donc pas de double grandeur. Une seule addition, déclarée plus haut : « incomplet » si une taille de la grille n'a pas de cellule.

## Ce que je n'ai pas fait

- Ni l'étage 1 décisif ni le chronométrage décisif ; aucune autre racine que 2026111930.
- Aucune pièce de l'étage 2.
- Aucun appel de modèle, aucun réseau hors `git fetch` et `git show`, aucune écriture dans le dépôt.
- Aucune commande sous `archives-reponses-modeles/`.

**Aucun refus d'outil.**

Développeur, modèle L′.
