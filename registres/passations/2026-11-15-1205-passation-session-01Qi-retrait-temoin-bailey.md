# Passation — session `session_01Qi7Gr4ct592cQ35N3cGWJW` (attaquant informé, sans clés) se retire du témoin de Bailey — 15 novembre 2026, 12:05 UTC

Branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas (R12). Aucune note de sonde ni de juge lue ; aucun
`notes-v3.jsonl` ni `technique-v3.jsonl` ouvert ; aucune liste de sauvegarde des sondes ouverte.

## Fait
- Routine de reprise le 14 (empreintes de `docs/` en accord ; `verifier-arbre` : 113 écarts, dont 2 connus et 111 journaux
  bruts non scellés sous `runs/temoin-bailey-v1-20261111/` ; essais : 222 passés, 1 sauté après ajout de pandas, omegaconf,
  hydra-core, vastai 2.4.6 absents de `requirements-cpu.txt`).
- Surveillance en lecture seule (branche, Vast, Hetzner) toutes les 5 min jusqu'à la fin : fin de la relance vue à 11:48Z
  (14e ligne du journal de conduite, cause d'arrêt « dépense », 36 tours complets, aucune garde tombée), puis les trois
  fichiers de fin à 11:58Z (`detruite` vrai, `transfert_complet` vrai, dépense 73,03 USD).
- Instances d'autres chantiers signalées, aucune touchée : 60599797, 60632409, 60632417, 60670453, 60671759, 60693560,
  60756203, 60760941 (« bbis-t07-repetition-v1 »), 60770175, 60773264 (« neuron-lens-b-alpha »).

## Constat et décision (routine)
Une session à clés (`session_016QhUrudziqEQujXt4ofM8u`) a fait les étapes de fin : poste v12 détruit, dossier de lecture
assemblé, registres (commit `e84b3735`). Cette session ne fait donc aucune étape de fin (ni registre, ni assemblage, ni
verdict, ni destruction) pour ne pas la croiser. Rien lancé, rien dépensé, aucune instance ni aucun serveur touché.

## Réserves
- `journal_chien` « non transféré (CalledProcessError) » dans `bilan-conduite-v5.json`.
- La carte de 60480302 n'a calculé qu'une part du temps depuis le 14 à 22:30Z (processeur près de 100 % pendant les creux).
- Mon estimation de l'heure de la garde D (11:30Z) reposait sur un calcul hors poste ; le poste l'a atteinte à 11:46Z.

## Instances actives
Aucune créée par cette session. Vues à 11:50Z : Hetzner 175884265 (poste v9), 176187199 (sauvegarde v2 de l'autre
session) ; Vast : seulement 58936096, 58936099, 58936100 (arrêtées).

## Prochaine action
Aucune pour cette session. Verdict (R13) et continuation : Lazar avec la session à clés.
