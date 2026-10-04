# Registre des GO

Seul Lazar accorde un GO. Une ligne par GO, jamais modifiée ; une révocation est une nouvelle ligne de type « révocation ».
Format lu par la garde `.claude/hooks/garde_calcul.py` : 8 colonnes ; dates ISO ; type ∈ {calcul, porte, dépôt distant, publication, contact, révocation}.
Tout lancement d'instance payante cite l'identifiant d'un GO de type « calcul » en cours de validité.

| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |
|---|---|---|---|---|---|---|---|
