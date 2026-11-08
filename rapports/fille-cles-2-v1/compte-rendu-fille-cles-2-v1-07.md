# Fille clés 2 — compte rendu court 07 — FINAL

Heures par `date -u`.

## Verdict
Lecture principale de l'étiqueteur **finie, code 0** (10:07:58Z → 14:40Z). Bloc 4-5 et bloc 21 conformes. Aucun arrêt de la section 4.4 atteint. Analyse non lancée (lecteur neuf, section 5).

## Nombres
- Relecture finie : A 59 « ok » + 1 « illisible » sur 60 ; B 60 « ok » sur 60.
- Manifeste : A ok 448, illisible 8 (7 en principale = 1,77 % de 396, sous le seuil de 8 ; 1 en relecture) ; B ok 456, illisible 0 ; arret None ; lecteurs_arretes {} ; tentatives interrompues 0.
- **depense_estimee_dollars 41.08914** (essai de format 1.164904 compris).
- Relais 248, après : 463 appels, depense_usd 12.925556, restant 285.904444, refus 0, écarts de modèle servi 0, usages absents 7, délais dépassés 0, réponses 200 : 456, 429 : 4, 502 : 3.
- Bloc 21 : `reponses-phase1-A-v4.jsonl` 5d0e8296d1b9410d7771e5839188430273f0813fd4701c52699732bba3b99e2e, `reponses-phase1-B-v4.jsonl` b03fccb51b37d088080bda4fefc5cf860aef85c95ebe03595dc05a256454237a, égales au manifeste ; A ≠ B ; 396 + 60 lignes chacun, 0 ligne d'un autre lecteur : conforme.
- Manifeste de la lecture : 47a13f944e52aa4310038d8d679d161f5c31f108671956a87297454771ae9e2d.

## Processus
Lancés : 248 (relais), 340 (lecture). 340 fini de lui-même ; 248 arrêté par son numéro ; les deux vérifiés morts (`kill -0`). Sentinelle et guets finis.

## Rendus
- Données : branche `donnees/etiqueteur-phase1-lecture-principale-v1` (partie de `main` 06451e59), commit 16aef7a0b318603a5e4b949087d797583e0547e4, sous `diag/etiqueteur-phase1-v1/lecture-principale-fille-cles-2-v1/` : `lecture-principale/` (7 fichiers), `relais-principale/` sans console (4), `compte-rendu/` (8), chacun avec son `.sha256` ; copies identiques aux empreintes de `empreintes-lecture-principale-v1.txt` ; garde des secrets 0.
- `compte-rendu-phase1-v1.md` complété par la section « Exécution par la fille clés 2 » : d2aba508c66eec1f296cb58b9dc014e343bf1a8dd22958609c7d940f0ae303f3.
- Arbre du code `/home/user/epreuve-etiqueteur-phase1-v1/code` laissé en place (ordre, section 6).
