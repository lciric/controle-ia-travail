# Bilan de la suite complète d'essais du dépôt, code v17 du témoin de Bailey — 13 novembre 2026

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Ne se réécrit pas (R12). Complète la passation `…-0148-…` (`a829b869…`) et
le § 3 de l'addendum 4 (« son compte final est inscrit dans la passation »).

Déroulé : 6 687 essais collectés. Passe 1 (en un seul processus) : coupée par un redémarrage du conteneur à 4 862 essais
joués ; puis le disque temporaire s'est rempli (≈ 16 Go de dossiers temporaires de pytest, supprimés : `/tmp/pytest-of-root`,
rien d'autre). Passe 2 : les 1 825 essais restants, rejoués **par fichier** (25 fichiers, le premier repris en entier), avec
un dossier temporaire vidé entre deux fichiers.

- Partie 1 (4 862 essais) : 4 800 passés, 25 sautés, **37 échecs**, tous dans des fichiers d'autres chantiers :
  `test_cibles_invisibles_v1.py` (2), `_v2.py` (1), `test_corpus_arxiv.py` (3, `pypandoc` absent), `test_hote_durable_a1_v3_v3.py`
  (16, interpréteur 3.13 exigé), `test_lanceur_durable_v5_a1v4.py` (1), `test_t06_*` (12 fichiers, 1 chacun),
  `test_t07_lecture_v1.py` (2).
- Partie 2 (25 fichiers) : 1 894 passés, 8 sautés, **2 échecs** : `test_t07_lecture_v1.py::test_mahalanobis_miroir_egal_a_familles_v2_au_commit_8cb539f9`
  (autre chantier, fichier à cheval sur les deux parties) ; `test_temoin_bailey_condition6_v13.py::test_v13_P2_processus_reels_veilleur_arrete_autre_pid_jamais_signale`
  (essai instable connu des essais v13, cause établie et bénigne, corrigé dans les essais v16 et v17 par une attente
  bornée ; addendum 3, § 3).
- Essais du témoin pour le code exécuté : `test_temoin_bailey_condition6_v17.py` 168 passés, 1 sauté ; v14, v15, v16 :
  tous passés ; `test_temoin_bailey_analyse_v3.py` : passé.

Aucun échec dans le code exécuté sur l'instance. Les échecs des autres chantiers ne sont ni examinés ni corrigés ici
(hors du périmètre de cette session).
