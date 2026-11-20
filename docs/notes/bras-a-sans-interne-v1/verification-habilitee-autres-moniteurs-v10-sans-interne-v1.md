# Vérification habilitée des corrections du module des cinq moniteurs, version 10 — sans interne — v1

Écrit par le lecteur habilité côté moniteurs du bras A (Claude Fable 5.2, accord de Lazar GO-2026-11-20-21), le 20 novembre 2026. Aucun seuil, trait, vocabulaire, poids ni texte de consigne de moniteur. Ce qui fonde chaque ligne est dans la pièce interne `docs/notes/bras-a-moniteurs-v1/verification-habilitee-autres-moniteurs-v10-v1.md`, qui ne sort pas. La session principale relit cette pièce avant de la transmettre.

**Objet.** Module `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v10.py`, `42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c`, commit `d5602cd57` ; ses essais, `75ef245065ae8407eed36d50290e3ffbef4065de6462e0830f41b5efda374537`. Réponses du développeur sans interne, v3 : `6c0f71f6a6b04201acbf4d9c729a3d1131fdb7c714fa1ee683fd2a7ff1d877ae`.

## Verdict : **conforme**

- Les quatre corrections demandées à la version 9 sont faites : la forme de `comptes_des_lectures` et de `preuve_d_ordre` est fermée ; au cas A, la borne haute est un nombre de 0 à 1 ; les phrases de `nombres_rendus` sont récrites ; l'épreuve de forme est refaite à la forme d'une vraie livraison, cinq moniteurs au fichier par unité. Les sorties de l'épreuve de forme de la version 10 remplacent celles de la version 9.
- **Aucun calcul d'aire, de score, de borne ni de valeur p ne change** de la version 9 à la version 10, ni, avec la contre-lecture précédente, de la version 8 à la version 10 (comparaison ligne à ligne).
- La pièce sans interne v3 du développeur ne porte **aucune fuite**. Une retouche d'exactitude : la version 10 a maintenant un commit, `d5602cd57`.
- Rejeu par le vérificateur : essais, `77 passed` ; épreuve par retrait, 65 retraits joués, 65 mordent, dont les deux que la contre-lecture de la version 9 avait vus sans morsure.
- Les réponses aux demandes 1, 2, 3, 13, 15, 16, 17 et 31 de la pièce v3 valent pour la version 10. `calculable` : vrai aux cas A, D et E ; faux aux cas B et C.

**Ce qui reste**, hors de cette vérification : l'attestation qu'aucun calcul ne change entre la version 7 et la version qui fait foi (demande 24 a), à écrire à part ; le lanceur de l'étape de discrétion, non écrit.

Cette pièce ne dépense rien et n'autorise rien.
