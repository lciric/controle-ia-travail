# Erratum 1 de la note de sortie sur la cible de publication du papier D

- **Date** : 2026-11-24, vers 13:35 UTC. Classe C. Rédigé par la session fille qui a mené le dossier.
- **Pièce corrigée** : `note-sortie-cible-publication-papier-d-v1.md` (inchangée, R12).

**Correction.** La note dit qu'Opus 5.5 a été appelé « sans provision de réflexion », par contraste avec Carbon (« high ») et Neon (« xhigh »). C'est inexact. Selon la documentation d'Anthropic (référence du kit d'interface, section « Thinking & Effort », relue le 24 novembre 2026), Opus 5.5 réfléchit toujours : sa réflexion est adaptative et ne peut pas être coupée, et l'effort (`output_config.effort`) est le seul réglage. Le programme v8d envoie l'effort « high » (journal : `effort: high` pour les trois cellules d'Opus). « Provision de réflexion 0 » est un poste du devis du programme, pas un réglage envoyé. Opus a donc réfléchi, à l'effort « high », un cran sous « xhigh » et deux sous « max ».

**Ce qui reste vrai.** Les niveaux ne sont pas comparables d'un fournisseur à l'autre ; la note ne doit pas en tirer d'écart de traitement entre les modèles.
