# Compte rendu 63 : fin des bancs plantés et notes de sortie

Écrit à 2026-11-22T14:40:54Z (`date -u`). Classe C, session des collisionneurs.

## Bancs plantés
- Dossier : `runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546`.
- Arrêt par PID (python 11355, puis enchaîneur 11349) à 14:34:33Z, après la conception de Neon. Il n'y avait plus rien de neuf à faire sur Luc, dont le solde était de 6,20 USD (GO-2026-11-22-73). Opus 4.6 et Fable 5.1 n'ont pas joué. La garde 11373 est sortie seule.
- Le tour III.1, à **7 cellules sur 9**, tient lieu de résultat (option a). Il n'y a ni critiques ni réponses.
- Dépense : **14,27 USD**. Luc 11,92 (Fable 8,58 dont le rejeu, Opus 3,34) ; Google 1,97 ; Kimi 0,17 ; OpenAI 0,21.
- Note de sortie : `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-bancs-plantes-v1.md` et `.pdf`. Les décisions 2, 4.1, 4.2 et 5 sont tranchées ; la décision 1 l'est en partie ; la décision 3 ne l'est pas (4 contre 3), elle est à renvoyer à une demande approfondie.

## Notes de sortie (règle de Lazar, transmise à 14:29Z)
Toutes sont dans `docs/notes/collisionneur-v9/notes-de-sortie-v1/`, en Markdown et en PDF, chacune écrite par un lecteur Opus neuf sur les seules cellules de son dossier :
- papier A : `note-sortie-papier-a-v1` ;
- papier B : `note-sortie-papier-b-v1` ;
- cœurs algorithmiques : `note-sortie-coeurs-algorithmiques-v1` ;
- tâches de sabotage : `note-sortie-taches-sabotage-v2`, qui fait foi ; la v1 est archivée, à lecture partielle ;
- bancs plantés : `note-sortie-bancs-plantes-v1`.

Le convertisseur est `md_vers_pdf_v1.py` : pandoc, puis Chromium sans tête.
