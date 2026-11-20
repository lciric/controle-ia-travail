# Rapport du développeur du code de lecture du barreau 5 — v5 (couple P1)

Écrit le 20 novembre 2026 par le développeur du code de lecture (Claude Opus 5.5), sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`. Pièce d'instrument (classe B), suite du rapport v4 (`1bc78521…`, non modifié). Même mandat ; aucune donnée, aucun réseau, aucun commit.

## Le couple et le texte

Le couple **P1** vient de la contre-lecture de la seconde programmation (`contre-lecture-seconde-programmation-v1.md`, `35254454e6bd6ad8ba1f8b8a8f951a9301bba950cf6643ad596ccb9c3ede5005`, vérifiée), section (d) et section « Premier programme ». Le texte le fixe deux fois :
- « Critères de lecture gelés », paragraphe « Sous huit familles présentes » : « Sous six familles : issue N, motif « niveau non atteignable ». »
- « Liste d'arrêt », point 13 : « Moins de six familles présentes : issue N, motif « niveau non atteignable », nœud. »

Je juge le couple juste : le motif est écrit en toutes lettres et ne porte aucune suite. Je l'applique à la lettre dans `lecture_v1.py`, fonction `issue`, l. 1042. Le motif de l'issue N sous six familles de E3 devient exactement « niveau non atteignable ». Rien d'autre ne change dans le code. La phrase N de ce cas est écrite à partir des motifs : elle devient « Non établi : niveau non atteignable. »

## Essais et mutation

| point | ce qui change, ou le résultat | essai ou outil |
|---|---|---|
| essai repris | il exige désormais le motif exact, le niveau `null` et la phrase | `test_moins_de_six_familles_issue_n_niveau_non_atteignable` (`tests/test_barreau5_familles_lecture_v1.py`) |
| essais | **244 passés, aucun échec** sur les six fichiers d'essais de la lecture ; aucun essai ajouté | — |
| plancher de l'amorce | inchangé : `MIN_ESSAIS=146` ; l'amorce n'est pas modifiée | — |
| mutation | P1 défaite, c'est-à-dire l'ancienne suite remise : **1 jouée, 1 attrapée**, par l'essai repris ; témoin vert (102 passés) | `outils-developpeur-code-lecture-v1/mutations-code-lecture-v5.py` (scellé) |
| syntaxe | Python 3.11.18, sans erreur | — |

La copie de travail et les temporaires sont effacés par leur chemin.

## Empreintes

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/lecture_v1.py` | `ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f` |
| `tests/test_barreau5_familles_lecture_v1.py` | `6ed14bdbdb895cedb759ce149dfba99a3c439f28b31a570ee364030baae5e6d7` |
| `…/outils-developpeur-code-lecture-v1/mutations-code-lecture-v5.py` | `65d4ab6fe132d5896e23dfee079be472944d46de9956fb385bac18eb7fbbf861` |
| `scripts/amorce_b5f_lecture_v1.sh` (inchangé) | `54a676f35bde811e8ebcfb0f643d510c2a1a79ca6a8554d61b7a39dd8e44453f` |

## Ce qui menace le gel

Le couple change l'empreinte de `lecture_v1.py`. La contre-lecture d'instrument de ce couple, que demande la contre-lecture de la seconde programmation (section 8, point 2), vient avant la ligne `CODE-LECTURE-B5F`.
