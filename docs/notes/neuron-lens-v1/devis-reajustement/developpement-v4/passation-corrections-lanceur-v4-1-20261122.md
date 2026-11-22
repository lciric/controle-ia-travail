# Passation courte 1 — corrections après la contre-lecture du lanceur v4 — 2026-11-22

Mandat `mandats/mandat-developpeur-corrections-lanceur-v4-v1.md` (`10dddebf…`, vérifié).

## Fait
- Rangement v2 (`rangement_lentilles_v2.py`) : attente de 60 s puis 300 s entre les essais d'un même fichier (C-1), borne d'attente de
  1 200 s par appel (nœud N-5), libellé de la vérification (C-3), relecture « sans objet » au code 4 (C-2).
- Lanceur v5 (= v4 plus l'attente du contexte), amorce v6, dépôt réduit v6, essai à blanc v5, essais `…_lancer_v5.py`,
  `…_etapes_b_beta_v7.py`, `…_montage_b_beta_v5.py` : 84 passés hors l'essai de l'arbre réduit (à rejouer après ce commit).
- Banc d'altérations du lanceur v5 : 45 tuées sur 45, témoin passe (sortie scellée).
- Brouillon de la commande v10 (non scellé, liste du dépôt réduit à remplir).

## Reste
Essai à blanc v5 sur ce commit ; liste neuve dans la commande v10 ; table des items v2 ; corrections ; empreintes v2 ; poussée.

## Prochaine action
`bash scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v5.sh <ce commit> <dossier neuf>`.

## Instances actives
Aucune.
