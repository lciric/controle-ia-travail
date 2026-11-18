# Identités des fichiers de sondes de la lecture des sondes (T0.7) — v1

Extraction par programme, identités seulement (aucune mesure). Branche distante `origin/donnees/t07-etape-a-v1` (tête `0c176db582ec13705e8fb7cc2d281215e2766e42`) ; les deux fichiers sont absents de `main` et du disque du dépôt.

## Fichiers

| fichier | branche | chemin | empreinte SHA-256 | clés | formes |
|---|---|---|---|---|---|
| sondes-neuves-t07.npz | `origin/donnees/t07-etape-a-v1` | `donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz` (versé en 9 morceaux `…npz.morceau-000` à `-008` + `…npz.morceaux.json`, concaténés dans l'ordre) | `374ad47346ae40d5a4d350724d0d19b5961724066dd7fdfaaf0adf1c3a4cbb79` (égale à son compagnon `.sha256` de la branche ; fichier reconstitué 431 599 709 octets) | 834 : `index` + 15 sondes (clés `s0_…` à `s14_…`) + 800 directions de plancher | `s*_w` (4096,) float64 ×809 ; `s*_mu` (4096,) ×6 ; `s*_s` (4096,) ×3 ; `s*_q` (4096,) ×3 ; `s*_W` (16, 4096) ×3 ; `s*_c` (16,) ×3 ; `s*_v` (16,) ×3 ; `s*_P` (4096, 4096) ×3 ; `index` (267119,) uint8 |
| planchers-figees-t07.npz | `origin/donnees/t07-etape-a-v1` | `donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz` | `94ca013c66e5dbd35b3ea55ec8aa4eb7b299e5dd63a95f7ccea7ced8d120f224` (égale à son compagnon `.sha256`) | 1601 : `index` + 1600 directions `s0_w` à `s1599_w` | `s*_w` (4096,) float64 ×1600 ; `index` (510199,) uint8 |

Empreinte d'ensemble des tableaux (SHA-256 sur clés triées, forme, type, octets), calculée par ce rédacteur : sondes neuves `33b7c92f062685b930c88849b5bf16ee6f89263289839a090d3f900462f5e6b3` ; planchers `fd526df8065fac3bf8554ab35d264e47559f50ce031a2361ed006f7869ffb651`.

Les noms des sondes ne sont pas des clés du fichier : ils sont dans le tableau `index` (JSON en octets, écrit par `premier_test_ia/figees.py::ecrire_sondes`), avec classe, famille, couche et empreinte de chaque sonde. Les noms ci-dessous viennent de cet `index`. Aucun autre fichier de `diag/` n'a été lu (dont `sondes-t07.json`).

## Contenu nommé

- Planchers (`planchers-figees-t07.npz`) : 800 directions pour `tromperie-difference_moyennes-c15-t07` et 800 pour `enjeux-lineaire-c15-t07` (classe `SondeLineaireJetons`, famille `plancher`, couche 15 ; noms `…-plancher-0` à `-799`).
- Sondes neuves (`sondes-neuves-t07.npz`) : un seul concept, `dissimulation` ; 5 familles × couches 7, 15, 23 = 15 sondes, plus 800 directions de plancher de `dissimulation-lineaire-c15`. Le concept `domaine` n'est dans aucun des deux fichiers.

## Les quatre sondes principales

| concept | nom | famille | couche | empreinte du vecteur | où |
|---|---|---|---|---|---|
| tromperie | `tromperie-difference_moyennes-c15` (sonde figée de P3) | différence de moyennes | 15 | non enregistré dans ces fichiers (seulement ses 800 directions de plancher) | sonde dans `sondes-figees-legeres.npz` de P3, non ouvert ici |
| enjeux élevés | `enjeux-lineaire-c15` (sonde figée de P3) | linéaire | 15 | non enregistré dans ces fichiers (seulement ses 800 directions de plancher) | idem |
| dissimulation | `dissimulation-lineaire-c15` | linéaire | 15 | tableau `w` (clé `s4_w`, (4096,) float64) : `fe414af79cd1effc154cf2c322fb7dbf7d0e9d7dbf29bd23bdba7d1c5c93cdf5` ; empreinte de la sonde dans l'`index` : `e537e4f82269c5525bae62a43e30ae8558a45c7956e0ac1305cc129eb092a8c1` | `sondes-neuves-t07.npz` ; désignée par la clé `principales` de l'`index` |
| domaine | non trouvée dans ces fichiers | — | — | — | le prérégistrement nomme « sonde du domaine » sans nom de fichier ; aucun nom `domaine-…` dans les deux `index` |

## Autres sondes de la même famille (empreintes de sonde dans l'`index`, 16 premiers caractères)

dissimulation : différence de moyennes c7 `098bd810783a8720`, c15 `00eca921c5a38a7b`, c23 `83a3b32d26f726ed` ; linéaire c7 `45e9a5ef9b459da6`, c23 `6a29177412829de7` ; perceptron c7 `c94f1df723dbf57f`, c15 `a29a9257f9c1f649`, c23 `e5982eb076c5842b` ; attention c7 `23c40902ad04dac0`, c15 `08b877c0a18bb254`, c23 `684690d5a3b7412f` ; Mahalanobis c7 `06be2baa2b6ea303`, c15 `72d5874cbd7b2bb7`, c23 `2c27f9a3c55c316d`.

## Non trouvé / hors mandat

- Vecteurs de `tromperie` et `enjeux` : hors de ces deux fichiers. Sonde du domaine : absente des deux fichiers.
- Le texte scellé `prereg/T0.7-sondes-v0-v1.md` ne donne pas les noms complets des quatre sondes principales ; ils sont lus dans les `index`. Pour la dissimulation, la clé `principales` de l'`index` donne le nom ; pour le domaine, rien.
- Lectures hors mandat : en-têtes de `meta` des `index` limités aux noms de clés et au nom de la principale ; recherche par motif dans le texte scellé (lignes de table, aucune valeur retenue).
