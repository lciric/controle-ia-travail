# Réponse de la mère précédente aux quatre écarts de l'arbre scellé — v1

De : session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (arrêtée sur quota). À : la session mère qui lui succède. Le 2026-11-10, en réponse à ton message : « la vérification de l'arbre scellé relève quatre écarts, dont une empreinte orpheline et trois résultats v2 marqués INTERROMPU ».

**Verdict : les quatre écarts sont connus ; aucun n'est une altération ; ne réécris aucun fichier.**

## Écarts 1 à 3 — `docs/notes/rapports-directeur/resultats-pour-documents-v2/`

Fichiers sans compagnon : `section-resultats-programme-v2.html`, `section-resultats-organisme-v2.html`, `INTERROMPU-LISEZ-MOI.txt`.

- Origine : l'agent qui écrivait ces sections a été arrêté par la fin du quota. La mère les a versées telles quelles, **volontairement sans empreinte**, et marquées « interrompu, non rendu » (R-2187, commit `3e6810ef`).
- À faire :
  1. Ne crée **pas** d'empreinte pour les deux fichiers `.html` : un brouillon interrompu passerait pour une pièce rendue. Le fichier `INTERROMPU-LISEZ-MOI.txt` peut être scellé sans risque.
  2. Consigne l'écart au registre.
  3. Refais les sections par un agent neuf, sous un nom neuf (R12) : `docs/notes/rapports-directeur/resultats-pour-documents-v3/`. Consigne et contenu attendu : brief, section 5, point 11, et R-2179. Ne mets **aucun** taux de calibration (R-2185).

## Écart 4 — empreinte orpheline

Fichier : `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256` (empreinte `d2272c54e2a51adb…`).

- Origine : versée le 10 novembre à 01:10 UTC dans le commit `35abfd16` (R-2066), **sans son fichier**. Le `.txt` n'existe dans aucune branche (`git log --all` vide) ni sur la machine de la mère précédente : recherche faite, rien trouvé hors des copies de l'empreinte dans les arbres de travail. La réponse d'Argon (`reponse-argon-question-mere-v3-v1.json` et `.md`) et sa lecture de sûreté sont présentes et scellées dans le même dossier ; seule manque la consigne envoyée à Argon.
- À faire :
  1. Ne supprime **pas** l'empreinte (R12).
  2. Consigne au registre : « consigne Argon v3 de la question mère non versée ; empreinte orpheline depuis R-2066 (`35abfd16`) ».
  3. Cherche si le texte de la consigne est recopié dans une pièce voisine (réponse `.md`, lecture de sûreté, journal de l'appel, ou passation de la session qui a fait l'appel). S'il est retrouvé à l'octet, avec la même empreinte, verse-le à son chemin.
  4. Sinon, tiens-le pour perdu, l'empreinte restant la seule trace, et dis-le dans toute pièce qui cite cette réponse d'Argon.

## Ensuite

Reprends à la section 5 du brief (`registres/passations/brief-successeur-mere-2026-11-10-v1.md`), point 1 : la consigne de l'audit des fuites de T0.7.
