# Mesure de la relecture en flux et préparation du relevé de prix — réajustement (commande v11, préalables) — v1

Session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z), 2026-11-22T06:27:33Z. Aucune dépense, aucune clé, aucune requête au loueur.

## Relecture en flux (devis v9, § 5, point 3 : « à mesurer sur un fichier d'essai et à dire avant le GO »)
- Fichier d'essai **public** (aucune clé, aucune donnée du projet) : `openai-community/gpt2`, `model.safetensors`, branche principale,
  548 105 171 octets, lu par `curl` depuis le conteneur de cette session et passé directement à `sha256sum`, **sans écriture sur disque**.
- Résultat : code 200, 548 105 171 octets reçus, **7,5 s**, débit moyen **73,5 Mo/s** (≈ 588 Mbit/s). Empreinte calculée
  `248dfc3911869ec493c76e65bf2fcf7f615828b0254c12b473182f0f81d3a707`, **égale** à l'empreinte que la plateforme déclare pour ce fichier
  (interface publique `paths-info`, même taille).
- Extrapolation pour ≈ 31 Go au même débit : **≈ 7 min** (≈ 422 s) ; trafic entrant du conteneur ≈ 31 Go, sans coût de location. Au
  dixième de ce débit, ≈ 70 min. Limites : un seul fichier, public, servi peut-être par un cache ; le dépôt privé de Lazar et la clé
  restreinte ne sont pas encore là : la relecture réelle se mesurera sur le premier fichier copié.

## Préparation du relevé de prix (commande v11, étape 4)
- Script `docs/notes/neuron-lens-v1/devis-b-beta/releve_prix_h100_v3.py` (321872f3…) et ses essais (25e6d199…) : empreintes vérifiées ;
  essais hors réseau : **16 passés sur 16**.
- Outil du loueur installé hors du dépôt (`/home/user/vastai-env`, `vastai==1.11.0`, commande v8, étape 1) ; version lue, aucun appel.
- Le relevé lui-même se fait **dans l'heure qui précède la création**, après le feu de la mère.
