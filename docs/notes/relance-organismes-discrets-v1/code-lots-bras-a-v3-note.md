# Module de construction des lots du bras A — note de code, version 3

- **Objet** : corriger le module des lots v2 selon sa contre-lecture (`docs/notes/relance-organismes-discrets-v1/contre-lecture-lots-bras-a-v2-v1.md`, `c40db8a64207489c44a0103c2b8a19b248432f6cb45d7fc6c899a90eecbecf36` ; verdict « à corriger », deux majeurs, quatre mineurs), contre `prereg/T0.7-organismes-discrets-v-a-v2-brouillon51.md` (`6de63aabf773559b43574b25737b4b93f1d87ab3665603c462da1627cbaa97bf` ; 6.2, 6.5, 6.8, lignes 551-552, 714, 719, 806, 808, 812, 815, 822, 846). Pièce de classe B : à revérifier par le même contre-lecteur.
- **Fichiers** (nom neuf, R12 ; v1 et v2 et leurs notes inchangées ; compagnons `.sha256`, R6) :
  - `src/controle_ia/organismes_discrets/lots_bras_a_v3.py` — `81dae4118be599a23714a1e7234b529376ee421a608591a22ac9fee4ef43a545` (841 lignes) ;
  - `tests/test_lots_bras_a_v3.py` — `d1051378fcd2452627dfed29cf5357902e8427379a0c9d0918f4f0a976731816` (48 fonctions, 56 essais : les 43 de la v2, portés, et 13 neufs).
- Processeur seul, aucun réseau, aucune dépense, rien committé ; aucune pièce cloisonnée ouverte.

## Corrections, et l'essai qui tient chacune

| défaut | correction | essai |
|---|---|---|
| **M-1** voie de l'étape (e′) | `voie_de_service_de_l_etape_e_prime(ancre_plans, ancre_jumeaux_)` : lot `ancre-jumeaux` complet → un tableau, rang à partir de 1 ; constat `ancre-jumeaux` → liste vide, **aucun arrêt**, rien au juge (ligne 812), le constat tient lieu de l'objet (inscrit au manifeste) ; révision comprise ; tout autre objet, épreuves mêlées, ancre incomplète : `GardeArret` | sain : `test_voie_de_service_de_l_etape_e_prime_saine` ; artefacts (onze) : `…_artefacts` |
| **M-2** égalité exacte | `len(h) < 128` et `len(h) < 64` (au lieu de `<=`) : à 128 et à 64 exactement, cas complet, actions **tirées par graine** (ligne 714 ; ligne 806 « moins … qu'une épreuve n'en demande », au sens strict), même lecture que les génériques à 64 et les relues à 160 | `test_egalite_exacte_tiree` (129, 128, 127, 65, 64, 63 ; espion des `choice` par clé) ; `test_egalite_exacte_donneuses_recalculees` |
| **m-3** identité des plans | le lot honnête de la couverture garde dans ses comptes `empreinte-des-plans-de-la-dose-1` (sha256 des deux listes triées, plans déplacés et épisodes laissés honnêtes) ; le lot des jumeaux la recalcule et arrête si elle diffère ou manque | `test_jumeaux_couverture_identite_des_plans` (échange de deux plans à mêmes effectifs 44/20, empreinte absente, empreinte fausse, cas sain) |
| **m-4** tâches sans plan | comptes `taches-sans-plan` (lot honnête de la couverture, ligne 815) et `taches-sans-plan-deplace` (lot des jumeaux, ligne 822) | `test_taches_sans_plan_comptees` |
| planchers | commentaire « à confirmer par Lazar » remplacé par GO-2026-11-22-90 (point 1 ; brouillon 51, fin de la ligne 806) ; valeurs inchangées 32, 24, 32, 32, 80 | `test_planchers_confirmes_go_2026_11_22_90` |

## Changement d'octets (déclaré)

- **Cas complet (576 honnêtes jugeables, 64 plans) : aucun tirage ne change.** Lot honnête et lot des jumeaux de l'appariement, trois ancres, lot mécanique, lot décisif : mêmes octets que la v2 (`test_egal_a_la_version_2_hors_des_corrections`) et que la v1 (essai de la v2, porté).
- **Lots honnête et des jumeaux de la couverture : leurs octets changent, au cas complet aussi**, par leurs seuls comptes (m-3 : `taches-sans-plan`, `empreinte-des-plans-de-la-dose-1` ; m-4 : `taches-sans-plan-deplace`) ; appels, identifiants, tables et ancre de la couverture inchangés. Leur sha256 au manifeste n'est donc pas celui de la v2.
- **M-2, hors du cas complet** : à exactement 128 actions honnêtes jugeables, le lot honnête de l'appariement diffère de la v1 et de la v2 (le tirage des 128 consomme le générateur avant les donneuses). À exactement 64, mêmes octets (l'ensemble tiré est le tout et aucun tirage ne suit sous `join/texte-sans-rapport`) ; à 127, 129 et 65, mêmes octets.

## Lectures déclarées, portées de la v2

Inchangées (note v2, « Lectures prises à la lettre », points 1 à 5), plus M-2 ci-dessus. Le texte ne dit pas autrement à la lettre pour l'égalité : « moins » est strict, et la ligne 714 écrit les effectifs complets « sans remise » sous `join/{épreuve}`.

## Questions de texte, non tranchées par le code

1. **Nouvelle : ancre sur plans honnêtes à effectif insuffisant, ancre des jumeaux construite** (critère de 812 : « les 24 honnêtes de la première partie ») : `voie_de_service_de_l_etape_e_prime` lève `AmbiguiteDuTexte` ; aucun jumeau n'est envoyé tant que le texte ne le dit pas (`test_etape_e_prime_premiere_partie_insuffisante_ambigue`). Les deux parties à effectif insuffisant : liste vide (rien à choisir). La construction de l'ancre des jumeaux elle-même n'est pas bloquée.
2. **m-1** (160 juste tiré) : lecture littérale gardée (seule lecture selon la contre-lecture) ; à porter au texte.
3. **m-2** (un seul constat « couverture » portant les deux comptes) : forme de la v2 gardée, non tranchée ; la suite écrite (instrument en échec, aucun lot, ancre non jugée) est unique, seule l'étiquette du constat (un ou deux) diffère : à porter au texte. Aucun `AmbiguiteDuTexte` ici, car il arrêterait un chemin que le texte prescrit.
4. Restent de la v2 : aucune donneuse d'une autre tâche ; moins de 896 plans des conditions (chacun `AmbiguiteDuTexte`).

## Commandes et sorties

    $ PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v3.py
    56 passed
    $ PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v3.py tests/test_lots_bras_a_v2.py tests/test_lots_bras_a_v1.py tests/test_graines_bras_a_v4.py
    224 passed

Campagne de mutations (bloc-notes de la session, `mutations_lots_v3.py` et `neufs_v3.py`) **sur une copie** : l'arbre `src/`, `pyproject.toml`, `conftest.py` et les essais v3 sont copiés dans le bloc-notes ; le module importé est vérifié être la copie ; chaque mutant n'est écrit que dans la copie et effacé dès le jeu des essais (`-x`) ; le module du dépôt n'est jamais écrit, et son empreinte est confrontée avant et après.

    premier passage : 67 mutants : 63 tués, 4 survivants
    second passage  : 67 mutants : 65 tués, 2 survivants ; copie restaurée, module du dépôt intact (81dae4118be599a2…)

Deux survivants du premier passage tués par l'essai des artefacts de (e′), renforcé (ancre sur plans de 47 actions ;
constat d'un autre objet en première place, qui levait `AmbiguiteDuTexte` au lieu d'un simple arrêt : un artefact doit
arrêter sans ambiguïté). **Deux survivants équivalents**, déclarés : « jumeaux couverture : comptes non confrontés »
(la garde des comptes est désormais impliquée par celle de l'empreinte, m-3 : mêmes plans, mêmes comptes ; gardée
comme première garde, au message plus lisible) ; « m-3 : empreinte non triée » (les listes viennent déjà triées de
`_partition`, par `_distinctes`).

Les mutants : les 49 de la v2 qui s'appliquent encore, et 18 neufs (M-2 : égalité sans tirage, à 128 et à 64 ; M-1 : constat des jumeaux envoyé, constat des jumeaux en arrêt, ambiguïté tranchée, ambiguïté en simple arrêt, épreuves mêlées, ancre sur plans incomplète, constat d'un autre objet admis à chaque place, ancre des jumeaux incomplète ; m-3 : identité non confrontée, empreinte absente admise, empreinte non triée ; m-4 : comptes à zéro, à l'envers, sur les plans honnêtes ; planchers : commentaire « à confirmer » rétabli).
