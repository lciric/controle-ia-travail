# Registre des GO

Seul Lazar accorde un GO. Une ligne par GO, jamais modifiée ; une révocation est une nouvelle ligne de type « révocation ».
Format lu par la garde `.claude/hooks/garde_calcul.py` : 8 colonnes ; dates ISO ; type ∈ {calcul, porte, dépôt distant, publication, contact, revendication, révocation} ; « revendication » : modification d'hypothèse ou de revendication du programme (nœud), effet permanent, échéance = date de la décision.
Tout lancement d'instance payante cite l'identifiant d'un GO de type « calcul » en cours de validité.

| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |
|---|---|---|---|---|---|---|---|
| GO-2026-10-04-01 | 2026-10-04 | dépôt distant | création du dépôt GitHub privé lciric/controle-ia et poussée de l'historique (N-001) | — | 2026-10-04 | Lazar | message de Lazar dans la session du 2026-10-04 : « GO N-001 : crée le dépôt privé lciric/controle-ia » |
| GO-2026-10-04-02 | 2026-10-04 | revendication | N-003, option (a) de `livrables/anteriorite-niveau1-v1/decisions-v2.md` (renforcée) : théorème négatif énoncé par invariance (T1 à T4 de la note v2, classes C et K distinguées, temps et agents comme sous-groupes de permutations, 2606.10456 cité comme antécédent défectueux) ; effet permanent | — | 2026-10-04 | Lazar | message de Lazar dans la session du 2026-10-04 : « GO N-003 a, N-004 a » |
| GO-2026-10-04-03 | 2026-10-04 | revendication | N-004, option (a) de `livrables/premier-rendu-v1/decisions-v1.md` : lemme d'additivité en énoncé adverse (invariance terminale et spatiale, borne inférieure toujours valide, coût du report chiffré, non-compensation comme condition empirique) ; effet permanent | — | 2026-10-04 | Lazar | même message |
