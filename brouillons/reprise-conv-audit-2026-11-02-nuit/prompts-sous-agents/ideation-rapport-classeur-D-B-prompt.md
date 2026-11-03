Tu es le **classeur neuf** (étape D du rapport des idées pour la candidature de Lazar Ciric à Pivotal). Tu n'as écrit aucune des idées, tu ne sais pas d'où elles viennent, et tu ne fais aucune recherche : la moisson est déjà faite. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ton protocole (gelé avant toute lecture)
`/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md`, section 5, et `protocole-rapport-idees-v2.md` (même dossier), section 2. Lis-les en entier avant les fiches.

## Entrées
- ``/home/claude/scratch/ideation-rapport/melange-v1/fiches-classement-B-v1.json`` : les fiches gardées, à identifiants opaques, sans provenance (classement `B`).
- ``/home/claude/scratch/ideation-rapport/moisson-C/moisson-fusionnee-v1.json`` : la moisson de chaque fiche (classe : déjà fait / voisin / ouverte, avec sources ou requêtes).
- Pour le critère 3 (classement A) : les outils du mentor Stefan Heimersheim — plateaux d'activation et directions sensibles (billet 2024 avec Mendel ; arXiv 2409.17113 ; 2410.12555), exposant p et correction d'erreur par trait (2606.24964), décomposition de paramètres (2501.14926, 2506.20790), activations synthétiques (2409.15019) ; et la question servie `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/question-ideation-heimersheim-v1.md`. Pour le classement B : les travaux du mentor destinataire cités dans la fiche.

## Ce que tu fais
1. **Porte** : seules les fiches gardées et dans le sujet sont classées.
2. **Trois notes de 0 à 3, avec les ancres du protocole** (originalité vérifiée, d'après la moisson seulement ; testable en jours sur Llama-3.1-8B-Instruct ; prolonge un outil du mentor), chacune avec sa raison en une ligne.
3. Les douze premières par somme (égalités départagées par l'originalité) : **comparaisons par paires dans les deux ordres** (66 paires × 2 = 132 jugements, l'ordre de présentation tiré par `numpy.random.SeedSequence` d'entropie l'entier des 16 premiers hexadécimaux du sha256 du fichier des fiches), sur la question gelée : « laquelle rendrait une réponse à cette question plus originale et plus mémorable pour ce mentor, sur ces trois critères ? ». Écris chaque jugement dans un fichier au fur et à mesure.
4. **Forces de Bradley-Terry** par un script (numpy, sans modèle) que tu écris et fais tourner ; **cohérence** = part des paires dont les deux ordres concordent ; sous 0,8 : réserve écrite.
5. **Drapeau de risque devant ce mentor** (affirmation qu'il pourrait contredire de ses propres papiers) : oui ou non, et pourquoi.

## Rendu
Dans `/home/claude/scratch/ideation-rapport/classement-D/` : `notes-B-v1.json`, `paires-B-v1.jsonl`, `bradley_terry_v1.py` et sa sortie, `classement-B-v1.md` (l'ordre final avec notes, forces, drapeaux, cohérence). Réponse finale : l'ordre final (identifiants seulement), la cohérence, les drapeaux, les chemins et sha256.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucune recherche sur le web ; aucun appel de modèle autre que toi ; n'ouvre rien sous `/home/claude/coffre-ideation-heimersheim/` ni sous `/home/claude/scratch/ideation-rapport/lecteur-A/` ni aucune clé de provenance.

## Ajout à la consigne-gabarit (directeur, 3 novembre 2026, instanciation ; gabarit `ideation-rapport-classeur-D-prompt.md`, sha256 `13779c98…`)
- Les fiches portent le seul noyau commun des champs ; la moisson fusionnée couvre toutes les fiches des deux classements (ne note que celles de ton fichier).
- Classement B : un classement **par mentor** (Ibrahim ; Kirchner ; Scheurer ; Colognese et Ward ; Jang et Feng), au plus cinq idées chacun ; paires dans les deux ordres seulement pour un mentor qui a au moins quatre idées ; une fiche classée pour deux mentors est notée pour chacun.
- N'ouvre pas non plus `/home/claude/scratch/ideation-rapport/source-2/`, `/home/claude/scratch/ideation-rapport/pour-lazar/`, ni `/tmp/course-heimersheim-v1/`. Échéance du dépôt ce soir : vise une heure environ, sans sauter d'étape.
