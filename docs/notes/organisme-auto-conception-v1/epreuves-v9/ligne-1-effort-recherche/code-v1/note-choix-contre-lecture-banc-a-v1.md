# Note — choix entre les deux contre-lectures du code du banc A de la ligne 1 — v1

Pièce de travail (classe C), écrite par la session du compte organisme le 2026-11-19 vers 15:58Z, sur le mot de la mère (vers 15:5xZ : « Écris une note courte (classe C) qui retient cette contre-lecture et verse l'autre telle quelle, avec la raison ») et le mot de Lazar « go reprise, go recos ».

## Les deux pièces

| pièce | auteur | verdict | empreinte |
|---|---|---|---|
| `contre-lecture-banc-a-ligne1-v1.md` | contre-lecteur du modèle S, ancienne session | « Conforme », sans correction ; quatre réserves portées au lancement | voir son `.sha256` |
| `contre-lecture-code-banc-a-ligne-1-v1-v1.md` | contre-lecteur du modèle S, session de reprise ; arrêté au premier refus d'outil, compte rendu recopié | « Conforme après corrections », sept corrections | `c0bca7dddce57d4e989ec2cd9526b9b3c0e144fd0bbb7569497d7129fc029a37` |

## Choix

**Retenue** : la seconde (`c0bca7dd…`). Les sept corrections s'appliquent au code par un développeur, sous des noms neufs (R12), puis un contre-lecteur d'un autre modèle que le développeur vérifie les corrections.

**Raison** : ses corrections relèvent d'écarts à des règles écrites, non de goûts : effacement des fichiers partiels d'une course interrompue (« récupérer ce qui est récupérable », R-3661, et R-3851) ; reprise de l'étalonnage qui saute les portes sans le dire, et six gardes sans essai sur cas sain et sur artefact (R5) ; empreinte de l'ensemble absente du manifeste du dépôt (R-3851) ; versions absentes de la sortie de l'étalonnage (R9) ; un essai qui se compare à lui-même. Un « conforme » sans correction devant ces points appelle le même audit qu'un résultat trop propre (R4).

**Versée telle quelle** : la première, que rien ne change. Ses quatre réserves de lancement (journal du lanceur ouvert en ajout, vérification des processus avant toute reprise, recoupement de M1-nul depuis le journal, gardes A7 et A11 passant par la ligne 0 de la table) sont reprises dans le mandat du développeur et dans l'addendum, parce qu'elles ne contredisent pas la seconde.

## Limite

Les deux contre-lectures sont du même modèle. La vérification des corrections ne départage pas les deux lectures : elle dit seulement si les sept corrections sont faites et justes.
