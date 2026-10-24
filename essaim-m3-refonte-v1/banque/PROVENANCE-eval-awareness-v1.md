# Provenance — sous-ensemble « conscience d'évaluation » v1

- Fichier : `eval-awareness-sous-ensemble-v1.json`, sha256 `31761eded7fe328a13a65984b3eb185876cdec2f0dff9247cd9e1f197d2b8820`
  (compagnon `.sha256` écrit par le script ; vérifié ici le 24 octobre 2026, 18:05 UTC).
- Source : jeu public du papier « Large Language Models Often Know When They Are Being Evaluated » (Needham et al.,
  arXiv 2505.23836), dépôt Hugging Face `jjpn2/eval_awareness`, révision `5d724f12988284a652749c56ec7b2356b0d14408`,
  `dataset.zip` sha256 `934dc4bc83b76e6bc57e672c39716061204b4802bb46b2038e7feb822aaa211c` (chiffré par les auteurs
  contre la contamination ; mot de passe public dans leur `scripts/decrypt.sh`).
- Extraction : par Lazar, sur sa machine, le 24 octobre 2026 entre 19:14 et 19:34 (heure de Paris), avec
  `extraire_sous_ensemble_eval_awareness_v4.py` (sha256 `69219092a2c743cfe522f1ef92af4e37865c9b4cdaad31c20e630f520f9a557e`),
  graine `SeedSequence(20261024)` ; 976 lignes lues, 70 lignes GAIA exclues (catégorie, sous-catégorie ou identifiant),
  4 strates (évaluation / usage réel × agentique / conversation ; disponibles 180 / 287 / 226 / 213) × 30 tirées = 120.
- Dépôt : branche `donnees/eval-awareness-sous-ensemble-v1` du dépôt de travail privé, commit
  `201dd09905a53b8310becdb9c729d39e67cc68ab` (Lazar). Copie ici à l'identique.
- Licence : CC BY-NC-SA 4.0 (jeu) ; les sources d'origine ont leurs propres licences (`DATA_SOURCE_LICENSES.md` du
  jeu). Dépôt privé seulement ; aucune redistribution ; GAIA exclu et non redistribué (condition d'accès du jeu).
- Longueurs (caractères) : médiane 2 240, moyenne 16 440, maximum 132 202 ; 30 items dépassent 20 000. La banque
  scellée borne chaque texte à 20 000 caractères (15 000 premiers + marque + 5 000 derniers), règle consignée dans son
  manifeste (`borne_caracteres`, `n_tronques`).
- Champs gardés dans la banque publique : `texte` (= `input`, messages rendus lisibles), `verite` ; dans le fichier
  secret : `id_source`, `category`, `agentique`, `tronque`.
