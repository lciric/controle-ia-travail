# Rapport — préenregistrement hors échantillon de la simulation d'essaim — v1 (brouillon 1)

**Verdict** : brouillon 1 écrit, codé et essayé ; rien de décisif lancé ; à contre-lire (R2) puis à sceller par l'étape 0. Constat de fond avant tout run : sous la loi de référence, ⌈K/2⌉ n'est pas une frontière (la forme close exacte donne une puissance au-dessus du taux dès m/K = 0,3) ; sous la loi P3 de la sonde des enjeux, le modèle de substitution prévoit la co-élévation **sous** son taux à m = ⌈K/2⌉. Les deux sont préenregistrés comme prédictions qui peuvent échouer.

## Fichiers (sha256 au moment du rapport)

| Fichier | sha256 |
|---|---|
| `preenregistrement-essaim-hors-echantillon-v1-brouillon1.md` | voir la session principale (le texte change après ce rapport ; empreinte à prendre au commit) |
| `grille-essaim-hors-echantillon-v1-brouillon1.json` | `889a2b30e54f8d647ff0cbff8e4c161aa84b335b48ca1fcb41e5d7cbc062c828` |
| `generer_grille_v1.py` | `a97d5088cd2f57f11a2dfe1d7163c22d1097a4ca9bc9ae79cd7f849068a924aa` |
| `tables-valeurs-predites-v1.md` | `a8073409c94954632f33395fa65b37ce76862dfad20e74d28848c9d842b103cd` |
| `moments_et_substitution_v1.py` | `ac7ffecaef0a29c24a6545582b182ab837377e505527452c03b60bd3714c357f` |
| `sortie-moments_et_substitution_v1.txt` | `99e0a1a1771608f71495b39a46c2e3808fd9057a9af7dc519b3b5f51739c56b2` |
| `chrono_point_v1.py` | `1e3d16f914f16d39982839b73a0c034e986cda9d6516e5fd8b0f74cf07246a94` |
| `sortie-chronometrage-v1.txt` | `14cef7c33403dc2f0c44c3f5e37dfd83c62d2037e00c10a8c01444de45ce023e` |
| `src/controle_ia/simulation_essaim/bornes_synchro_v1.py` | `ce7e1885083a4127107332de8173fbe5daf020d896ef36ad0d53c22231cd48d9` |
| `src/controle_ia/simulation_essaim/loi_p3_v1.py` | `bb1487064195339fc6f47fd3c1e66e6be9e47b59366dd70dfbb1df6c066f1596` |
| `src/controle_ia/simulation_essaim/blocs_hors_echantillon_v1.py` | `a89be529b8c4f43ff6570c5df07570b0a4c5b428c21bd4ee1f06f229d2d43eab` |
| `src/controle_ia/simulation_essaim/lecture_hors_echantillon_v1.py` | `a4e1a1ec87418d8d936136d2bcdbbbe8dae496306433da53b972191739d4d892` |
| `src/controle_ia/simulation_essaim/run_essaim_hors_echantillon_v1.py` | `3dd3eeab09abe6c2640960bd022a54a2777d10cf866e2f244fea4186f693de8c` |
| `tests/test_simulation_essaim_hors_echantillon_v1.py` | `b0d1669dd23fc75056f256d6f93377a1b0c8b5b1c89d11cf80f6c2d1254c8190` |
| `donnees/20261019-230011-p3-reel/scores-p3.npz` (vérifiée) | `968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf` |

Aucun fichier commité modifié ; aucun `.sha256` écrit ; aucun commit.

## Cellules neuves et preuve qu'elles n'ont pas été explorées

- Couples (K, T) déjà calculés avant ce texte : grille v1 (5, 40), (10, 20), (20, 20), (10, 50) ; explorations v1 (10, 24), (10, 45), (6, 32), (12, 16), (16, 24), (5, 36), (10, 22), (20, 22) (lus dans les scripts `explorations-brouillon1/exploratoire_*.py`, dont les empreintes sont listées dans `empreintes.txt`, sha256 `63c00c62…c664`, vérifié). Essai à blanc et chronométrage v1 : tailles de la grille v1 seulement.
- S : e10x10, e20x10 — jamais calculés (aucun T = 10 nulle part). 12 cellules de synchronisation : m ∈ {3, 4, 5, 6, 7, 10} et {6, 8, 10, 12, 14, 20}.
- Q : e10x20 sous c ∈ {0,1 ; 0,3}, m ∈ {3, 5, 7, 10} — jamais calculés (v1 : c ∈ {0,2 ; 0,4}, m ∈ {5, 10}). Une cellule déjà vue, rejouée et étiquetée : c = 0,4, m = 5.
- P : loi réelle jamais utilisée ; 12 cellules (2 sondes × m ∈ {3, 4, 5, 6, 7, 10}).
- L'essai `test_grille_cellules_neuves_et_predictions_existantes` vérifie mécaniquement ces exclusions.

## Prédictions et dérivation (détail au préenregistrement)

- **Formes closes neuves** (`bornes_synchro_v1`) : pour un agent synchronisé, l'indicateur au pas commun vaut 1{N ≥ 1}, N ~ Bin(T, q), et ses indicateurs aux autres pas forment un sous-ensemble uniforme de taille max(N − 1, 0) ; d'où les lois jointes exactes des comptes sur 1, 2, 3 pas et les bornes de Bonferroni d'ordre 1 à 3 de P(max_t C_t ≥ j). Bandes de largeur ≤ 2·10⁻⁴ aux cellules S. Vérifiées par Monte-Carlo sur configurations jetables (K = 6, T = 8). Sous équicorrélation : borne basse exacte au pas commun par quadrature (égale à la borne de v1 à c = 0, vérifié).
- **Conséquence** : sous la loi de référence, e10x10 : 0,121 à m = 3 ; 0,227 ; 0,378 ; 0,541 ; 0,686 ; 0,929 à m = 10 ; e20x10 : 0,302 à m = 6 … 0,999. La « frontière » de v1 n'existe pas comme telle. Sous corrélation, la borne s'effondre aux petites fractions (c = 0,3 : 0,009 à m = 3, 0,029 à m = 5) : la frontière monte avec c.
- **Loi P3** : x et les signes viennent d'un modèle gaussien X = μ_t + τ Z_i + bruit de variance v_t − τ², paramètres = moments lus. Les deux sondes ont un profil moyen par pas opposé (tromperie culmine aux pas 0 et 1 ; enjeux au pas 9, +0,97 écart-type) : le modèle prévoit la co-élévation au-dessus de son taux dès m = 4 pour la tromperie, mais **en dessous** à m ∈ {3, 4, 5} pour les enjeux (0,025 à 0,032), et l'e-valeur cumulée **au-dessus** pour les enjeux à toutes les fractions (0,08 à 0,17). x = 0,55 (tromperie) et 0,31 (enjeux) pour la synchronisation totale (modèle moins 0,15).
- **Statuts** : instrument (HS.1–3, HQ.1–3, HP.1–3) ; signe tiré d'une forme close (HS.4, HQ.4) ; heuristique risquée (HS.5, HQ.5, HQ.7) ; rejouée (HQ.6) ; modèle de substitution, risquée (HP.4–6).

## Essais

`tests/test_simulation_essaim_hors_echantillon_v1.py` : 11 essais, tous passés (9,6 s) — bornes contre Monte-Carlo (configurations jetables), cohérence avec la borne de v1, gardes de domaine ; loi P3 : empreinte sur le vrai fichier (cas sain) et sur une copie altérée d'un octet (artefact), fichier absent, sonde absente ; refus d'un épisode non honnête, d'un épisode à action non honnête, de pas faux ; rééchantillonnage par épisode entier, sans remise dans un essaim, K trop grand refusé ; critère « dans la bande » ; grille (cellules neuves, prédictions rattachées à des cellules existantes) ; chaîne complète du lanceur sur mini-grille dans un dépôt jetable avec **données P3 factices**, run unique, données altérées refusées ; garde de calibrage du bloc générique (cas sain, artefact). Aucun essai ne calcule une cellule de la grille ni ne forme un essaim de vrais épisodes. Suites essaim v1, v2 et hors échantillon ensemble : 64 passés (40,9 s). Suite complète lancée avec `-x` : 99 passés puis arrêt sur `tests/test_corpus_arxiv.py::test_traiter_papier_garde` (`ModuleNotFoundError: pypandoc`, environnement, sans lien avec ce travail) ; le reste de la suite n'a pas été rejoué.

## Commande et durée

`PYTHONPATH=src python -m controle_ia.simulation_essaim.run_essaim_hors_echantillon_v1 --prereg prereg/essaim-hors-echantillon-v1.md --grille prereg/essaim-hors-echantillon-grille-v1.json`, depuis l'arbre séparé de l'étape 0. Durée ≈ 3 minutes (jusqu'à 6 sous charge), 311 cellules dont 33 trajectorielles.

## Réserves

1. Les marges 0,015 (HP.5, HP.6) et 0,15 (HP.4) ont été fixées après avoir vu les valeurs du modèle de substitution (pas les données réelles) ; déclaré au texte.
2. Les essaims P sont des assemblages d'épisodes indépendants : aucune corrélation entre agents d'un vrai essaim ; calibrage et épreuve tirent dans les mêmes 60 épisodes (disjonction en essaims, pas en épisodes).
3. Les prédictions « en dessous » de marge 0,015 sont à la limite de résolution à R = 20 000 : un effet réel un peu plus faible donne « non concluant ». C'est écrit dans les issues.
4. HS.3 et HS.4 ne peuvent échouer que par une erreur de forme close ou de code ; leur intérêt est de remplacer la lecture « frontière à ⌈K/2⌉ » de v1 (lignes 3 et 9 de sa table E), ce qui est une proposition pour Lazar, pas une modification du programme.
