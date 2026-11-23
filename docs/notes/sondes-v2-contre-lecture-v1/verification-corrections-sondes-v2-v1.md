# Vérification des corrections du code des sondes v2 (v1 vers v2)

- **Pièce** : classe B. Même contre-lecteur (Sonnet 5.5), mêmes interdits (ni coffre, ni verdict, ni sel ; aucune dépense). Tête vérifiée : `8718975d` (code `831d1cfb`), fiche v2 `0a789768…` (empreinte recalculée : concordante). Tous les compagnons `.sha256` des fichiers modifiés concordent.
- **Essais du paquet** : `PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py` sur `8718975d` : **127 passés, 1 sauté (l'essai lent), 41,42 s**. `'torch' in sys.modules` après import de tous les modules du paquet : **faux**.

## Verdict : conforme avec une réserve mineure restante (défaut 8 c)

## Défaut par défaut

| n° | état | preuve |
|---|---|---|
| 1 (majeur, R9) | corrigé | `programme_monde_plante_v3.py:61-66` commit et état git, dépôt sale refusé sauf `--autoriser-depot-sale` (consigné en réserve) ; l. 78-85 configuration complète empreintée, commit passé à `manifeste_lecture`. Essais ajoutés. |
| 2 (majeur) | corrigé, nul valide | voir ci-dessous |
| 3 | corrigé | `monde_plante_v3.py:262-269` cas sain jumeau (unité et tâche) joué avant l'artefact |
| 4 | corrigé | `programme_monde_plante_v3.py:108-113` arrêt si critère jamais lu ou manquant (seule exception : le monde de fuite) |
| 5 | corrigé | `statistiques_v1.py:368-382` drapeau par tirage |
| 6 | corrigé | `--nul-identite` (200) distinct, passé à `lire_etalon` et `lire_monde` ; écrit aux arguments du rapport |
| 7 | corrigé | `lecture_v1.py:584,600-603` plis sans deux classes rapportés, « prédicteur non évalué » |
| 8 | partiel | (a) corrigé, l. 603 `effectifs_plan`, `n_plis` ; (b) corrigé, l. 801-818 comparaison sans accents ; (c) partiellement : liste fermée `STATISTIQUES_RESUME` (l. 782-794), mais la présence ou l'absence de `memorisation`, `triviaux` ou `intervalle_taches` distingue encore une ligne calculée d'une ligne « non calculable » sans intervalle. Mineur : fixer les clés du résumé quelle que soit l'issue. Note : les mots `fort`/`faible` en sous-chaîne feraient refuser un nom de lecture tel que « trace_forte » ; sans effet sur des lectures réelles, à surveiller. |
| 9 | corrigé | `magasin_v1.py:370` `np.load(io.BytesIO(octets))` |
| 10 | corrigé | `magasin_v1.py:399-401` garde `source_textes`, diagnostic nommé avec `melange_de_sources` (`valeur_declaree` toujours non comparée : sans conséquence ici) |
| 11 | corrigé | LISEZ-MOI (essai lent `…_v3.py`, E-1 à E-8, durée), en-tête de `lecture_v1`, fiche v2 |
| 12 | corrigé | `reemploi_v1.py` copies sans torch, essai d'égalité aux originaux, essai « torch non chargé » ; vérifié ci-dessus |
| 13 | corrigé | `statistiques_v1.py:516-518` choix marqué E-8 ; essai d'équivalence de Holm ajouté |

## Majeur 2 : le nul reste-t-il valide ?

Oui. `lecture_v1.py:611-668` :
- Le nul prend les paires dans la **structure du jeu** (`paires_structurelles`, l. 667), non dans la famille de sonde : sous la logistique, la paire de poids de l'unité est de nouveau échangée d'un bloc, comme l'observé le suppose.
- Étiquette portée par le jeu de poids sans paires : permutation des étiquettes **entre séries**, chaque série d'un bloc (l. 651-657). C'est une symétrie échangeable correcte sous l'hypothèse nulle ; elle conserve le nombre de séries positives et la structure d'identité, ce que la permutation de lignes détruisait.
- Étiquette ni du texte, ni de la série, ni appariée, sur un jeu à unités : `GardeArret` nommé « unité échangeable inconnue » (l. 658-660) ; la permutation de lignes n'est plus permise que sans unités, là où l'étiquette est propre à la ligne.
- Trois essais l'éprouvent : blocs de série (chaque série à étiquette constante, effectif conservé, plusieurs configurations vues), arrêt nommé, paires structurelles sous la logistique (étiquette constante par unité). Cas sain et artefact y figurent.
- Limite non défaut : avec peu de séries, le nombre de permutations distinctes est petit et la valeur p plancher en dépend ; c'est la propriété du plan, déjà rapportée dans le LISEZ-MOI.

## Reste

Défaut 8 c seulement (mineur). Aucune régression constatée : le monde de fuite, les gardes et le manifeste sont éprouvés.
