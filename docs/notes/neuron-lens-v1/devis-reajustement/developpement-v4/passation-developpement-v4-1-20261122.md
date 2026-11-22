# Passation courte 1 — développement du lanceur v4 et de la commande v9 du réajustement de nos lentilles — 2026-11-22

Développeur neuf, sous le mandat `docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-developpeur-lanceur-v4-commande-v9-reajustement-v1.md`
(`6ed542449c34f6f2a6d61ecd80216702d1f79e03958b4b1b1dfd7965eaca690c`, vérifiée), depuis le commit `33371746d`.

## Fait (brouillon, rien encore de scellé hors cette passation)
- `src/controle_ia/neuron_lens/b_beta_lancer_v4.py` : la v3 copiée puis changée item par item (a) à (m) (repères dans le code).
- `src/controle_ia/neuron_lens/rangement_lentilles_v1.py` : copie vérifiée (machine) et relecture en flux (session), faux transport en essai.
- `scripts/amorce_neuron_lens_b_beta_v4.sh` ; `scripts/depot_reduit_neuron_lens_b_beta_v4.py` ;
  `tests/test_neuron_lens_b_beta_lancer_v4.py` ; `tests/test_neuron_lens_etapes_b_beta_v6.py` et `…_montage_b_beta_v4.py` (copies des
  essais embarqués, import seul changé). Essais : 71 passés, 1 écarté (l'essai du dépôt réduit, à jouer après le commit).

## Reste
Essai à blanc v3 de l'amorce v4 ; commande v9 ; scellements, empreintes, table des items, nœuds.

## Prochaine action
Écrire `scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v3.sh` et le jouer ; puis la commande v9.

## Instances actives
Aucune (rien loué, rien lancé, aucune requête au loueur ni à la plateforme de modèles).
