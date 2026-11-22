# Conformité du code de la seconde passe au texte scellé v2, point par point — v1

Développeur neuf de la seconde passe, 2026-11-21 (UTC). Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md`
(`a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`), section « Code neuf », lignes 2428 à 2635. Le texte décide ;
là où il laisse un choix, un nœud daté est écrit dans `noeuds-et-precisions-seconde-passe-v1.md` (N-dev-1 à N-dev-10). Les essais
nommés sont dans `table-essais-seconde-passe-v1.md`. Tout est joué sur jouets : aucun modèle, aucune lentille, aucun corpus réel.

Légende : **tenu** (codé et éprouvé, cas sain et artefact) ; **tenu, avec nœud** ; **écart** (dit en clair).

## A. « Ce que la v2 ajoute au module »

| point du texte | état | où, et ce qui est à savoir |
|---|---|---|
| noms neufs, modules de la v1 non réécrits | tenu | 10 modules neufs (dont `constantes_v2`, non nommé par le texte : constantes seules) ; aucun fichier existant modifié (`git diff --stat` du premier au dernier commit : ajouts seuls) |
| `nos_lentilles_v1` : fiche de rangement, lecture et vérification | tenu, avec nœud | forme JSON choisie (N-dev-2) |
| condition de lecture (verdict, variante, lignes exigées, audit, stabilité, limites de la seconde course) | tenu, avec nœuds | N-dev-3 (comment la ligne du mot de Lazar nomme la lentille), N-dev-4 (couche écartée : booléen attendu) |
| essai d'un octet de nos fichiers ; lecture en flux à la révision, SHA-256 et taille sur le flux ; jamais de repli | tenu | `cible_un_octet`, `lire_ajustement_en_flux` |
| analyse de l'archive (`data.pkl` par dépickleur à liste blanche sur stockages factices ; positions) | tenu | précision : la version de torch installée (2.14.1) n'écrit pas les tailles dans l'en-tête local ; elles viennent de `data.pkl` ou du descripteur vérifié par somme de contrôle. Réserve : forme du descripteur au-delà de 4 Gio non éprouvée sur un vrai fichier |
| extraction des couches 7, 15, 23 de `sums[("out", h)]` ; contrôles de `meta`, de l'état, des matrices | tenu | `meta` de S lue dans la pièce du 18 novembre sur son empreinte |
| place de la ligne de l'addendum de concentration (brouillon 4) | tenu | `exiger_registre_v2` |
| `montage_v2` : `montage_v1` plus plongements, seuils d'espace, garde par les noms de variables, appel de `nos_lentilles_v1` | tenu, avec nœud | N-dev-1 : les cibles du corpus des jetons gardés ne sont pas branchées (voir D) |
| `lecture_entree_v1` : covecteur, normalisation, plongements centrés, référence « plongements seuls », chemin indépendant en double précision | tenu | « scores des 89 498 jetons » : éprouvé à taille de jouet seulement |
| `comparaisons_lentilles_v1` : recouvrements, p, médiane, corrélations, moitiés, libellés, calibration (borne haute seule) | tenu, avec nœud | N-dev-10 (motif ajouté pour une calibration hors bornes) |
| `reproduction_v1` : tables ouvertes sur l'empreinte de leur ligne ; comparaison par programme ; « non calculable » des directions qui diffèrent | tenu | les vingt premiers jetons sont comparés comme ensembles ; même ensemble dans un autre ordre compté à part, sans réserve (précision de lecture) |
| `audits_v2`, `phrases_v2` : déclencheurs, phrase de tête, six formes comparées octet pour octet au texte, refus d'une paraphrase interdite | tenu, avec nœud | N-dev-7 (dernier crochet indéterminable : phrase non écrite, note) |
| modules de la v1 réemployés tels quels si leur interface le permet ; sinon version neuve déclarée, et phrase « code de lecture différent […] » | tenu | réemployés : `lecture_v1`, `nuls_v1`, `entrees_v3` (N-dev-5 : exige les lignes de la première passe), `statistiques_v2` et `v3` ; neufs et déclarés : `statistiques_v4`, `lanceur_seconde_passe_v1` ; la phrase est écrite en tête de la reproduction |
| un lanceur de la seconde passe, horloge de 10 h | tenu, avec nœuds | `lanceur_seconde_passe_v1` ; N-dev-8 (forme de la fiche du code), N-dev-9 (instant où l'état de la première passe se lit) |
| statistique corrigée et règle de départage ; comptes d'égalités écrits dans les tables | tenu | `statistiques_v4` ; aucune garde d'égalité dans la seconde passe |

## B. « Essais ajoutés » (v2)

| groupe du texte | état | remarque |
|---|---|---|
| lignes et fiche | tenu | table, § 1 |
| condition de lecture, un cas par mention | tenu | table, § 3 |
| accès | tenu | table, § 4 |
| archive | **tenu, avec un écart dit** | « égale au chargement entier par `lenses.load_fits` » : le code voisin n'est pas versé et rien ne se télécharge ; comparé à `torch.load` du fichier entier et à la formule écrite dans le texte (N-dev-6). L'essai opposable de la forme de l'archive est versé scellé (script et sortie) et exigé par la fiche du code |
| poids | tenu | table, § 4 |
| lecture | tenu | « indépendance exacte à la norme » : exacte en mathématiques, à l'arrondi près en simple précision (écart relatif sous 10⁻⁵, mêmes vingt jetons) |
| comparaisons | tenu | table, § 7 |
| reproduction | tenu | table, § 7 |
| phrases | tenu | table, § 7 |
| procédure | tenu | bout en bout sur un Llama miniature, une fois par palier, plus un monde où la première passe est lancée et non achevée |

## C. Essais des brouillons 4, 5 et 6

| groupe du texte | état | remarque |
|---|---|---|
| statistique corrigée, concentration et part ; taux à petite taille (M = 19, 128 jetons, 2 000 répliques, entre 0,03 et 0,065) | tenu | table, § 6 |
| ses deux arrêts | tenu | |
| règle de départage, listes de vingt (signe −, liste par z, ordre d'entrée) | tenu | |
| règle de départage, listes de dix ; garde de la fonction de lecture | tenu | |
| pôles à cosinus égal | tenu | |
| comptes d'égalités écrits | tenu | |
| ligne de l'addendum de concentration | tenu | |
| phrase du déclencheur (vi), toutes ses formes | tenu | |
| première passe lancée et non achevée ; tables sans entrées | tenu | |
| fiche muette | tenu | |
| une lentille à chaque palier | tenu | |
| issue des nœuds N12 et N17 ; règles de N12 et de N17 | tenu, avec nœud | N-dev-3 |
| étiquettes du programme | tenu | |

Graines des essais : `numpy.random.SeedSequence`, clés `lentilles-bbis-v2/essai/<garde>` (`tests/lentilles_sondes_bbis_seconde_passe_jouets_v1.py`,
fonction `rng`). Le calcul lui-même garde les clés de graine de la première passe (éprouvé de bout en bout).

## D. Ce qui n'est pas tenu en l'état, ou reste à faire avant un lancement

1. **Cibles du corpus des jetons gardés non branchées** (N-dev-1) : le montage réel s'arrête tant que la lecture paginée de
   l'arbre, écrite par un autre développeur, n'est pas branchée ; la brancher demande une version neuve du lanceur et sa fiche.
2. **Rien n'a tourné à taille réelle** : pas de banc de temps ni de mémoire de la seconde passe (aucun modèle ni fichier réel
   n'est ouvert par ce mandat). L'horloge de 10 heures et les 8 Go ne sont éprouvés que comme gardes.
3. **Formes attendues par le code, que le texte ne fixe pas** : fiche de rangement (N-dev-2), ligne « Lentille nommée » (N-dev-3),
   booléen de couche écartée (N-dev-4), fiche du code (N-dev-8). À faire suivre à la session qui écrit ces pièces.
4. **La suite entière du dépôt n'a pas été jouée** (plus de deux heures) : seuls le paquet des lentilles et ses voisins l'ont été.
5. **Contre-lecture (R2)** : ce code n'a pas été contre-lu ; la fiche du code de la seconde passe et sa ligne de registre ne sont
   pas écrites (ce n'est pas mon rôle).
