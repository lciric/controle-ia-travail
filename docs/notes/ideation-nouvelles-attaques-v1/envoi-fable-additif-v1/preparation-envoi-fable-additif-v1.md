# Préparation de l'envoi de l'additif du véhicule à Fable par l'API — v1

Pièce de travail de la session de l'organisme. **Rien n'est envoyé.** L'envoi part sur le feu écrit de la mère, une fois sa ligne de GO inscrite (6 USD), et une fois la version 3 de l'additif écrite avec les réponses du directeur.

## Outil
- `src/controle_ia/relecture_fable_api_v3.py`, empreinte `95bea064c753ca24…`, égale à celle de `main`.
- Modèle `claude-fable-5-2`, effort `high`, `max_tokens` 128 000 par défaut, aucune relance, aucun repli.
- Clé lue par son nom seul : `RR_ANTHROPIC_API_KEY_MINUIT`.

## Copies sans nom (garde de motifs)
- `copies_sans_nom_v1.py` (ce dossier) fait une seule retouche : il remplace le nom du directeur par « le directeur », avec ses accords, puis applique à chaque ligne la garde même de l'outil (`garde_motifs_ligne`). S'il reste un motif, le code est 3 et rien ne part.
- **Épreuve, cas sain** : les trois pièces de la v2, avec 31, 13 et 2 remplacements, ne gardent aucun motif. Code 0.
- **Épreuve, artefact** : une pièce qui porte un nom, un identifiant de session et un terme de chemin interdit. Trois motifs sont pris, code 3.

## Pièces de l'envoi
- `--consigne` : `consigne-relecture-additif-vehicule-na-v1.md` (ce dossier).
- `--piece` : la copie sans nom de `additif-vehicule-na-projet-v3.md`, **à écrire**.
- `--avant` : la copie sans nom de `additif-vehicule-na-projet-v2.md`.
- `--remarques` : les copies sans nom de la contre-lecture de la v1 et de la vérification de la v2.

## Commandes, dans cet ordre (C = `docs/notes/ideation-nouvelles-attaques-v1`, E = `C/envoi-fable-additif-v1`)
1. Copies :

   `.venv/bin/python -I E/copies_sans_nom_v1.py E/copies-v1 C/additif-vehicule-na-projet-v3/additif-vehicule-na-projet-v3.md C/additif-vehicule-na-projet-v2/additif-vehicule-na-projet-v2.md C/additif-vehicule-na-projet-v1/contre-lecture-v1/contre-lecture-additif-vehicule-na-projet-v1.md C/additif-vehicule-na-projet-v2/verification-v1/verification-additif-vehicule-na-projet-v2.md`

   Le code attendu est 0.
2. Envoi, sur le feu de la mère seulement :

   `PYTHONPATH=src .venv/bin/python -m controle_ia.relecture_fable_api_v3 relire --consigne E/consigne-relecture-additif-vehicule-na-v1.md --piece E/copies-v1/additif-vehicule-na-projet-v3-copie-sans-nom.md --avant E/copies-v1/additif-vehicule-na-projet-v2-copie-sans-nom.md --remarques E/copies-v1/contre-lecture-additif-vehicule-na-projet-v1-copie-sans-nom.md --remarques E/copies-v1/verification-additif-vehicule-na-projet-v2-copie-sans-nom.md --sortie E/reponse-fable-v1 --cle RR_ANTHROPIC_API_KEY_MINUIT --plafond-ligne 6 --journal-depense E/journal-depense-v1.jsonl --effort high`

   Le préfixe `GO_ID=<ligne de la mère>` est ajouté à la ligne d'envoi.
3. Si l'outil refuse (garde, plafond, compagnon, défaut de réponse), je m'arrête et je le dis à la mère. Rien ne se relance sans son mot.
