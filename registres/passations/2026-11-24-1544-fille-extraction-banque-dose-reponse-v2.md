# Passation — session fille d'extraction de la banque de 64 tâches neuves (suite, consigne v2)

Session fille (mère : session_01Qi7Gr3Ggccg85kjmP654WC), branche `banque/dose-reponse-consigne-cachee-v1`. Suite de `2026-11-24-1334-fille-extraction-banque-dose-reponse.md`.

## Fait
- Repli (b) (GO-2026-11-24-27) : consigne d'enveloppe v2 de l'extracteur (étape 2b, relecture de l'énoncé contre la liste de H.9). Contre-lue par un Sonnet 5.5 neuf, 7 remarques traitées (dont une bloquante : la réextraction lisait encore la v1), vérifiée « utilisable en l'état ». Scellée (`44da46b3…`). Erratum 1 du module v2 (déclaration du modèle).
- Essai sur les 16 papiers d'octobre, seuil scellé avant : 1 échec sur 16, probant (sous la v1 : 10).
- Extraction des 80 papiers sous la v2 : banque de 64 tâches formée, contrôle joué conforme. Bilan, écarts et ligne proposée : `docs/notes/banque-dose-reponse-consigne-cachee-v1/bilan-banque-formee-consigne-v2-v1.md` (`c66650c5…`).
- Compte rendu à la mère envoyé ; ligne `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` proposée (fichier `taches-banque.json`, `0065065b…`, commit `e1fe6cea`).

## Reste
- La mère inscrit la ligne au registre. La PR #108 (brouillon) attend le mot de Lazar pour la fusion.
- À la fusion dans `main` : il faut une liste neuve des lecteurs admis de la référence cachée (v6, après la v5 de `main`). Elle admet comme lecteurs d'extraction, au même titre que `extraire_t05.py` : `extraire_banque_dose_reponse_v1.py` et `_v2.py` (`_main`, `assembler`, `assembler.tache`, `bilan_echantillon`, `lire_contre_verification`, `verdicts_lisibles`), ainsi que `rejeu_contre_verification_banque_v1.py::lire` et `reextraction_echantillon_96_v2.py::lire`.

## Réserves
- Suite complète des essais : 1 836 passent, 1 échoue (`tests/test_cibles_invisibles_v4.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`, arrêt au premier échec, 37 minutes). La garde relève les modules ci-dessus, qui ne sont pas encore admis, et aussi deux modules `t08` déjà présents à la base de la branche (`fabrique_jouet_v1.py::taches_factices`, `rendu_juges_v1.py::exiger_tache_projetee`). Cette seconde partie de l'échec précède cette session. Les essais au-delà du premier échec n'ont pas tourné.
- Le juge est du même modèle que l'extracteur. Il est aussi celui qui faisait échouer la v1. Le code n'a requis aucun audit, le cas étant intermédiaire.
- Deux faux échecs du classifieur de sécurité ont abouti au second lancement.

## Prochaine action
Attendre la mère : inscription de la ligne, puis décision sur la liste v6 des lecteurs admis et sur la fusion de la PR #108.

## Instances actives
Aucune (aucune dépense, aucun calcul loué).
