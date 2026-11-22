# Passation courte 2 — développement du lanceur v4 et de la commande v9 du réajustement — 2026-11-22

Suite de la passation 1 (`passation-developpement-v4-1-20261122.md`, `e3027319…`).

## Fait
- Sceaux posés trop tôt (commit `443bd8d3f`) sur le lanceur v4, le module de rangement, l'amorce v4, le dépôt réduit v4, les essais
  v1 du lanceur v4 et l'essai à blanc v3 : l'outil de scellement refuse ensuite toute nouvelle empreinte au même nom (R12) ; refus
  déclaré, non contourné. Ces pièces restent telles quelles ; ce qui devait changer prend un nom neuf.
- Essai à blanc v3 joué sur `443bd8d3f` (journal `essai-a-blanc-amorce-b-beta-v3.txt`, scellé) : **non conforme, 12 écarts, tous au cas
  nominal et à sa relance** — un essai embarqué importait le programme de comparaison, absent de l'arbre réduit ; tous les autres cas
  conformes (reprise, échec, clôture en échec 23, quatorze formes refusées au croquis, gardes d'entrée, carte).
- Essais v2 du lanceur v4 (`tests/test_neuron_lens_b_beta_lancer_v4_v2.py`) : les deux défauts corrigés, cinq essais renforcés ; la v1
  archivée sans modification dans `brouillons-scelles/` (hors des essais collectés). Amorce v5, dépôt réduit v5, essai à blanc v4 :
  nom neuf seul changé. Banc d'altérations : **32 tuées sur 32**, témoin passant (`sortie-banc-alterations-lanceur-v4-v1.txt`).
- Brouillon de la commande v9 et table des items (non scellés).

## Reste
Essai à blanc v4 sur le commit de cette passation ; essai de l'arbre propre (dépôt réduit v5) ; rendu, empreintes, scellement de la
commande v9 et de la table.

## Prochaine action
`bash scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v4.sh <commit> <dossier neuf>`, journal versé dans `developpement-v4/`.

## Instances actives
Aucune.
