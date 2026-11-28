# Fiche de faisabilité — données publiques de l'étalonnage court de la prédiction de liens entre littératures (version 1)

Pièce de travail (classe C), écrite le 2026-11-24 vers 06:55Z par la session fille de l'étalonnage, **avant tout téléchargement de données ou de résultats**. Seules ont été lues : les notices, les licences, les tables des matières des archives (lues à distance, en-têtes seulement), le schéma d'un fichier de colonnes, et le code public de chargement. Aucune note d'intérêt, aucune arête datée, aucune relation n'a été lue.

## 1. Notes d'intérêt de Gu et Krenn (piste « surface et structure », IDE-2026-11-23-028)

- Dépôt public du code et des données d'évaluation : `artificial-scientist-lab/SciMuse`, commit `0be934a2b04aa8177ab62ea2829c19a3f10772e5`, licence MIT (lue dans `LICENSE`).
- Fichier tabulaire des notes et des traits : `graph_feature_plot/evaluation_feature_dataset.csv` (10 528 449 octets, non téléchargé). D'après le code public `graph_feature_plot/Fig4_features_interest_suggestion.py` (lu) : une ligne d'en-tête, puis colonnes `0` type d'institut de l'auteur (`nat`, `soc`), `1` type de suggestion (`random` : paire de concepts tirée au hasard ; `semnet` : paire choisie par le réseau), `2` type d'institut du partenaire (`nat`, `same`, `soc`), `3` clarté, `4` intérêt (échelle de 1 à 5, `-1` = manquant), puis `144` traits numériques.
- Second fichier : `interest_prediction/all_evaluation_data.pkl` (3 949 340 octets, non téléchargé), clés `features` et `interest` d'après `run_prediction_comparison.py` (lu) ; la binarisation des auteurs est « intérêt > 3 ».
- **Identité des paires de concepts** : le README dit que « les questions de recherche et les classements des experts sont privés » ; le code public ne lit aucune colonne de concept. Hypothèse de travail : **l'identité des deux concepts n'est pas publique** ; à vérifier, après scellement, sur les seuls noms de colonnes et de clés.
- Disposition des 141 premiers traits, déduite du code public `artificial-scientist-lab/Impact4Cast` (commit `d2af4f3d69e1e5272c168d3f950b56b31845a51f`, `features_utils.py`, fonction `get_all_feature`) et recoupée par les indices nommés dans `Fig4_features_interest_suggestion.py` (`0` degré du concept A, `14` rang de page de A, `20` citations de A, `26` citations totales de A, `75` rang de la croissance annuelle des citations de B, `87` coefficient de Simpson de la paire, `137` nombre minimal d'articles sur A ou B jusqu'à deux ans avant, `141` impact prédit, `143` « distance sémantique ») :
  - `0` à `19` : 10 traits de graphe par nœud (degré à y, y−1, y−2 ; nouveaux voisins sur 1 et 2 ans et leurs rangs ; rang de page à y, y−1, y−2), entrelacés A (indice pair), B (indice impair) ;
  - `20` à `77` : 29 traits de citations par nœud, entrelacés A (pair), B (impair) ;
  - `78` à `98` : 7 traits de paire (voisins communs, indice géométrique, cosinus, Simpson, attachement préférentiel, Sørensen-Dice, Jaccard) × 3 années (y, y−1, y−2), rangés trait par trait ;
  - `99` à `140` : 14 traits de citations de la paire × 3 années ;
  - `141` impact prédit ; `142` et `143` : deux distances entre les sous-graphes des deux chercheurs (d'après l'article, version HTML arXiv 2405.17044v4, section des traits).
  - Les traits de nœuds sont remis à l'échelle par ligne, ceux de paire par colonne (`rescaling_row`, `rescaling_col`). Cette disposition est une déduction de code : une garde doit la vérifier (nombre de colonnes, parité A/B).
- Article : Gu et Krenn, arXiv 2405.17044 (version 4 lue en HTML pour la seule déclaration de disponibilité des données) ; aucun chiffre de l'article n'est opposable avant lecture sur PDF empreinté (R7).

## 2. Graphe daté de concepts de Gu et Krenn (bras « coupure temporelle »)

- Zenodo, enregistrement `13900962`, licence **CC BY 4.0** (lue dans la notice de l'interface de programmation de Zenodo), publié le 2024-10-09.
- Fichiers : `load_full_knowledge_graph.ipynb` (1 917 octets, lu) et `scimuse_full_dynamic_graph.zip` (3 018 689 216 octets, somme MD5 `9e0546256c44ef2708c0fe9260a036a8`, non téléchargé).
- Table des matières lue à distance : `376` entrées, dont `375` fichiers `full_dynamic_graph/partial_dynamic_graph_NNN.parquet`, `3 138 228 301` octets décompressés au total.
- Schéma (lu sur le pied d'un fichier de 121 lignes, sans lire les valeurs) : `v1`, `v2` (identifiants entiers des deux concepts), `time` (jours depuis le 1er janvier 1990 d'après `Impact4Cast/prepare_eval_data/prepare_eval_feature_data.py`, `day_origin = date(1990,1,1)`), `ct` (citations totales de l'article), `c2023` … `c2012` (citations par année). Une ligne = une co-mention de deux concepts dans un article daté.
- Noms des concepts : fichier `concept` du dépôt SciMuse (2 738 356 octets) ; la notice parle de 123 128 concepts (chiffre de notice, non opposable).

## 3. Relations biomédicales typées de PubTator 3 (piste « le pont suit-il la carte ? », IDE-2026-11-23-027)

- Serveur public de la bibliothèque nationale de médecine des États-Unis : `https://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator3/`, mis à jour le 2026-11-17.
- Licence : **domaine public** (« United States Government Work », avis lu dans `README.txt`, aucune restriction d'usage ni de reproduction).
- Fichier : `relation2pubtator3.gz` (288 mégaoctets, non téléchargé) ; quatre colonnes : identifiant PubMed, type de relation (`Association`, `Positive_Correlation`, `Negative_Correlation`, `Co-treatment`, `Drug_interaction`, `Comparison`, `Conversion`, `Binding`), premier concept avec son type d'entité et son identifiant, second concept de même. Relations extraites par le système BioREx.
- **Pas de date dans le fichier.** Horloge possible : l'ordre des identifiants PubMed, attribués à l'entrée dans la base ; étalonnage de cette horloge sur un échantillon tiré au hasard, daté par les utilitaires publics et gratuits de PubMed (`eutils.ncbi.nlm.nih.gov`, joignable, sans clé, trois requêtes par seconde au plus, 200 identifiants par requête).

## 4. Moyens

- Processeur : 4 cœurs ; mémoire vive : 15 gigaoctets ; disque libre : environ 50 gigaoctets.
- Python 3.13, NumPy 2.4.6, SciPy 1.17.1, pandas 3.1.1, pyarrow 26.0.1, scikit-learn 1.9.1, POT (transport optimal) 0.9.7.
- Dépense : `0` USD ; aucun appel payant.
