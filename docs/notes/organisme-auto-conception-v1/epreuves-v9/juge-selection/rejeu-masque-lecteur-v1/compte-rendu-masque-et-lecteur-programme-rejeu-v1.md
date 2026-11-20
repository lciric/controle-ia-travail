# Compte rendu — masque et lecteur par programme, rejeu v1 (exécutant neuf, modèle S)

Heure : 2026-11-20T08:07:10Z (`date -u`). Verdict : ARRÊT au masque (refus du programme, code 2). Étapes 3 et 4 non jouées. Aucune sortie produite.

## Vérifications
- Mandat : `sha256sum -c` OK (bae4b1a8…).
- Programmes copiés, empreintes vérifiées : masque 07ed8725…, lecteur de99117b… (bibliothèque standard seulement, aucun module voisin).
- Pièce de scellement : relue ; `main` local ne la contient pas, tirée de `origin/main`.
- Configurations tirées de `origin/main` : A 8a8548d1…, B b44371d2… (égales aux empreintes attendues).
- `test -f` sur le fichier des cartes : code 0.

## Commandes et codes
1. `python3 --version` : 0 (3.13.18).
2. `python3 -B scripts/verifier_environnement_agent_v1.py` : 0, statut « lu », aucune anomalie.
3. Masque (`masque_style_cartes_v1.py`, cartes ba65c411…, configuration A 8a8548d1…) : code 2.
   Message écran : « REFUS : cartes : champ(s) hors de la configuration (1) — l'ordre fixe ne les place nulle part ; rien n'est écrit ».
   Aucune sortie, aucun compagnon.
4. Lecteur sur les cartes : non joué (arrêt, règle 5).
5. Lecteur sur le masque : non joué (pas de sortie du masque).

## Écarts à signaler
- Première tentative de `git show --output=` : le fichier est resté vide (empreinte e3b0c442…) et la commande a imprimé le contenu d'une pièce non-carte ; j'ai tiré les deux configurations de nouveau par redirection shell vers les mêmes fichiers (écrasement de fichiers vides de mon propre dossier, empreintes ensuite conformes).
- La commande du masque a été écrite avec `; echo "rc=$?"` : entorse à « une commande simple par appel ». Le masque n'a été lancé qu'une fois.
- Lecture du code des deux programmes (permise par le mandat) : aucune carte lue ou affichée.

## Motif du refus (lu dans le code, aucune carte ouverte)
`extraire_contenus` refuse quand au moins une carte porte, dans `contenu`, un champ absent des dix champs de la configuration A. Un champ en trop dans une carte (un seul champ distinct signalé). Sa nature n'est pas connue de moi et n'a pas été cherchée. Il s'agit d'un écart entre la configuration scellée A et le fichier des cartes : à trancher par la session mère (nouvelle configuration scellée ou autre décision), pas par moi.

## Prochaine action proposée
Aucune relance. Décision de la mère sur l'écart de champs.
