# Avenant aux trois consignes relancées le 4 novembre 2026 (instance fusionnée) — v1

Écrit vers 01:45 UTC (`date -u`). Les trois sous-agents arrêtés par Lazar le 3 novembre à 11:07 UTC (R-1361 de la branche
`canal/conv-audit-n04` : « aucun n'est relancé sans son mot ») sont relancés sur son mot du 4 novembre (vers 01:20 UTC), verbatim :
« avance en autonomie pendant 12h sur les programmes controle ia et organisme ». Chaque consigne d'origine vaut telle quelle, sauf ce
qui suit, propre à la machine neuve.

## Pour les trois
- `/home/claude/controle-ia-travail` est un arbre de travail de la branche `canal/conv-audit-n04` (tête `e7726dce` ou plus récente) ;
  `main` est dans `/home/user/controle-ia-travail` (lecture seule pour toi). Les registres vivants (`registres/go.md`,
  `registres/decisions.md`) sont désormais sur `main` à partir de R-1450 ; ceux de la branche restent valables jusqu'à R-1449.
- Le travail partiel de vos prédécesseurs, laissé sur l'ancienne machine le 3 novembre, **n'existe plus** ici (non committé) : vous
  repartez de zéro, sans le chercher. En particulier `/home/claude/scratch/juges-v3/` et l'ancien `/home/claude/wt/r1-v4` sont absents.
- `.venv` : celui de `/home/user/controle-ia-travail/.venv` (requirements-cpu, `pypandoc_binary` compris) ; `PYTHONPATH=src` du dépôt
  où vous travaillez.
- Votre dernier message : chemins et sha256 de vos fichiers, comme le demande la consigne.

## Contre-lecture des juges v2, brouillon 3
- `/home/claude/ideation-organism` est un lien vers le clone public `/home/user/ideation-organism`, tête `faff48b` (lecture seule ;
  vos fichiers neufs vont dans `orchestrator/prereg/` comme le dit la consigne, sans commit).

## Pilote de l'exposant p, brouillon 2
- Le GO de 30 USD est inscrit sur `main` (GO-2026-11-04-03) ; le devis doit tenir dessous.
- Le dépôt public `sycophancy-psychophysical-law` est déjà cloné en lecture seule : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (tête `b3ecaec`) ; R9-bis y est committé (`preregistrations/2026-11-03_addendum_R9bis_dose_curves.md`) mais pas encore archivé sous DOI : gardez le marqueur `<<DOI_R9_BIS>>`.
- Le PDF de 2606.24964 n'est toujours pas versé : la réserve R7 tient.

## Développeur de R1 v4
- L'arbre de travail `/home/claude/wt/r1-v4/` existe, branche locale `prep/r1-relance-v4` partie de `origin/prep/r1-relance-v3`
  (`04bc323a`) : vous y travaillez seul.
- GO-2026-11-03-03 (60 USD) est dans `registres/go.md` des deux branches.
