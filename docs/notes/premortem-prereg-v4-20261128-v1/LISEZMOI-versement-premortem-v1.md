# Pré-mortem des brouillons de Gemini (additif du critère 3 de G0, architecture de G1, arbitrages du 28) — versement (v1)

Classe C. Versé le 28 novembre 2026 par la session mère, après que Lazar a repassé le dépôt en privé (vérifié vers 12:45Z : l'interface de programmation de GitHub rend `private: true`, la page publique sans authentification rend 404, aucune copie dérivée). Ces pièces étaient retenues hors du dépôt tant qu'il était public (R-5448, R-5449).

## Ce que c'est
Trois lecteurs neufs, Fable 5.2 en effort maximal, ont fait le pré-mortem des trois brouillons de Gemini versés le matin (`brouillons/prereg-v4-c-furtif-g1/`) : ce qui pourrait échouer, pourquoi, comment l'éviter, sur la demande reformulée en quatre points.
- `lecteur-A/` : brouillon de l'additif du critère 3 de G0 (micro-course du saboteur discret à coût déclaré). Rendu `rendu-lecteur-A-v1.md` (`9548feda…`).
- `lecteur-B/` : brouillon de l'architecture de G1 (puissance de H1 et de H2, coûts). Rendu `rendu-lecteur-B-v1.md` (`5e9f1784…`).
- `lecteur-C/` : arbitrages du 28 (texte des accords du 28 novembre, numéros 1 à 3) et banc de G1 (banque de tâches Python contre la ligne en vigueur). Rendu `rendu-lecteur-C-v1.md` (`01ccdfa2…`).
- Chaque lecteur : `scripts/` (épreuves rejouables), `sorties/` (résultats bruts), relevé des fichiers lus avec empreintes.
- `reformulation-quatre-points-v1.md` : la demande reformulée servie aux trois lecteurs.
- `clef-de-la-mere-ne-pas-servir-aux-lecteurs/` : ce que la mère attendait, écrit avant les rendus et jamais servi aux lecteurs (contrôle de leur indépendance). **Ne pas la servir aux lecteurs à froid des textes réécrits.**
- Note d'antériorité liée : `docs/notes/anteriorite-sondes-code-v1/anteriorite-sondes-code-v1.md`.

## Ce qui n'est pas versé
Les copies d'entrées faites pour les lecteurs (blocs de la course dose-réponse, textes, mesures), dont les originaux sont dans le dépôt : 718 fichiers, inventoriés par chemin, taille et empreinte dans `inventaire-copies-d-entrees-non-versees-v1.tsv`.

## Écart de nom
`lecteur-B/empreintes-lecteur-B-v1.sha256` est versé sous `lecteur-B/empreintes-lecteur-B-v1-liste-sha256.txt`, contenu inchangé : son suffixe l'aurait fait prendre pour un compagnon orphelin par la vérification de l'arbre.

## Garde de lecture des sondes
Aucun fichier `*.npz`, `*.npy` ni `*.safetensors` ; aucun chemin interdit (consignes privées, dossier du saboteur à budget, consignes de P3, code `iib`) dans les relevés de lecture des trois lecteurs.
