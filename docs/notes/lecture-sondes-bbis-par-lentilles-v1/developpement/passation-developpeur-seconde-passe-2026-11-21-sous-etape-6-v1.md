# Passation courte — développeur de la seconde passe — sous-étape 6 — 2026-11-21 17:30 UTC

**Fait.** Le montage de la seconde passe (`montage_v2`) et le lanceur de la seconde passe (`lanceur_seconde_passe_v1`, horloge de
10 heures, 8 Go au départ), leurs jouets (`tests/lentilles_sondes_bbis_seconde_passe_jouets_v2.py`) et leurs essais
(`tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py`, 34 essais : 21 de procédure, 13 de bout en bout sur un Llama
miniature, une fois par palier, et un monde où la première passe est lancée et non achevée). Sortie : 21 de procédure passés
(environ 13 s), 13 de bout en bout passés (583 s). Essai des essais : lanceur 10 altérations vues sur 10, montage 5 sur 6 (une
équivalente, double garde de l'empreinte du 18 novembre). Table « garde → essai sain → essai artefact » écrite (non encore scellée).

**Reste.** Sous-étape 7 : jouer le paquet entier `tests/test_lentilles_sondes_bbis_*.py` et garder sa sortie ; sceller la table des
essais, la note de conformité point par point au texte v2, la note de développement v2, les nœuds (brouillon à sceller sous un
nom versionné), les empreintes du code ; rendu.

**Réserves.** Le corpus des jetons gardés n'est pas branché (nœud N-dev-1) : `montage_v2.cibles_du_corpus` s'arrête tant que la
lecture paginée (`corpus_pagine_v1`, écrite ailleurs) n'est ni donnée ni présente ; la brancher demandera une version neuve du
lanceur (liste de ses modules). Les essais de bout en bout injectent la fonction de `montage_v1` sur un arbre simulé d'une page.

**Prochaine action exacte.** Sous-étape 7, ci-dessus. Rien ne tourne ; aucune instance.
