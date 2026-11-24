# Mandat — extraction de la banque de 64 tâches neuves pour la course de dose–réponse de l'organisme à consigne cachée — v1

Pièce de classe C (mandat), écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3`. Première des deux sessions à lancer ; le développeur du code vient ensuite.

## But

Former la banque de 64 tâches de la course, par la seule suite du tirage scellé des papiers, sans graine nouvelle, et la livrer scellée par compagnon, prête pour la ligne `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` du registre des scellements. Aucune dépense en dollars. Rien n'est lancé sur une carte.

## Texte qui fait foi

`prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, une fois scellé par la mère (vérifier son compagnon avant tout travail) : plan d'analyse, point 1, et liste d'arrêt. En cas de doute, ce texte prime sur ce mandat.

## À lire, et rien d'autre

- le point 1 du plan d'analyse et la liste d'arrêt du texte ci-dessus ;
- `docs/procedures/T0.5-selection-papiers-v1.md` (chaîne par papier, § 7, motifs d'exclusion) et `docs/procedures/T0.5-extraction-v1.md` (énoncé, classification, cibles semées, reprise, contre-vérification) ;
- `diag/20261006-134235-t05-corpus/` : `tirage.json`, `corpus.json`, `candidats.json` et les pages scellées de la requête du 6 octobre 2026 (version de chaque papier) ;
- le code du tirage et de l'extraction des 96 tâches, et le manifeste de cette extraction (7 octobre 2026), pour le modèle des sous-agents ;
- `donnees/20261007-082440-t05-extraction/taches-evaluation.json` et `taches-entrainement.json`, pour l'exclusion seulement (identifiants).

Cloisonnement : aucun score, aucun verdict, aucune sortie de course, aucun coffre. **Ne pas ouvrir** `brouillons/g0-criteres-2-3-v1/consignes-privees-dose-reponse-consigne-cachee-v*.json` ni `prereg/P3-consignes-v1.md` : cette session n'en a pas besoin. S'inscrire sur une liste « qui a lu quoi » avant toute lecture.

## Travail

1. Prendre les papiers **à partir du rang 125** de `tirage.json`, dans l'ordre du tirage ; aucun papier n'est lu avant son tour.
2. Pour chaque papier : la chaîne par papier de la procédure de sélection, puis la procédure d'extraction, avec leurs règles d'exclusion, de reprise et de contre-vérification, inchangées. Version du papier : celle des pages scellées du 6 octobre 2026, consignée par fiche. Sous-agents d'extraction et de contre-vérification : le modèle que nomme le manifeste de l'extraction des 96 ; sinon, écart déclaré et nommé.
3. Un papier exclu est remplacé par le suivant du tirage. La banque est formée des **64 premiers papiers retenus** ; elle n'est fixée que lorsque chaque papier de rang inférieur à celui du 64e retenu a un sort définitif ; un papier examiné au-delà n'entre pas.
4. Seule la portée des deux procédures change (rang de départ 125, cible de 64 tâches) : la porter par du code **sous nom neuf**, sans modifier le code scellé ; contre-lecture par un autre modèle (classe B), puis vérification des corrections par le même contre-lecteur.
5. Les cibles semées sont écrites mais ne sont montrées à aucun agent de la course.

## Arrêts

- Candidats épuisés avant 64 tâches : arrêt, nœud de Lazar.
- Empreinte du tirage, des fiches ou d'une procédure différente de celle que cite le texte scellé : arrêt, sans rien écrire (R11).
- Aucun changement de règle, aucune graine tirée, aucune tâche de la banque initiale.

## Livrables

- le fichier des 64 tâches, dans un dossier daté sous `donnees/`, au format des fichiers de tâches de l'extraction des 96, avec son compagnon ;
- les fiches par papier (rang, version, sort, motif d'exclusion), avec compagnon ;
- un manifeste (code et empreinte, commit, modèle des sous-agents, versions) ;
- un contrôle joué et sa sortie : 64 tâches exactement, aucune parmi les 96, aucun papier de rang inférieur à 125, rangs retenus dans l'ordre du tirage ;
- la ligne proposée `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` (chemin, empreinte, commit), que la mère inscrit ;
- compte rendu à la mère : chemins, empreintes, nombre de papiers examinés et exclus par motif, écarts déclarés.
