# Consigne à Fable 5.2 — table des revendications en vigueur, version 2 — v1

Écrite le 2026-11-24 vers 10:20Z (`date -u` relevé à 10:17Z). Rédigée par la session « dossier de l'entretien et billets », reprise sur le compte 01Qi7 (Opus 5.5). Pièce de travail.
Dosage : Fable 5.2, effort élevé. Raison : pièce qui porte les revendications (une erreur se propage au papier et à l'entretien), mais application de décisions déjà prises, sans conception neuve. Contre-lecture ensuite par un Opus neuf, puis vérification des corrections par le même.

## Le mandat

Lazar a choisi l'option (b) : la table des revendications v2 est réécrite **avant l'entretien du 1er décembre**, par Fable (GO-2026-11-24-15, point 1 ; R-5261, sur origin/main). C'est la décision 2 de la réponse 22 (« refaire la table en y propageant les retraits »).

La v1 (`docs/notes/revendications-en-vigueur-v1/table-revendications-en-vigueur-v1.md`) date du 19 novembre. Elle ignore :
- le retrait du lemme et du théorème négatif comme résultats (22 novembre) ;
- les lignes T et L ;
- N-075, N-076 et N-077 (H6 retirée) ;
- le programme v3.

Le second erratum de la demande 27 (entrée E2-4) ne fait que l'avertir et la marquer. La v2 réécrit les lignes.

## Règle de fond, sans exception

**La table enregistre des décisions ; elle n'en prend aucune.**
- Toute ligne change par une décision nommée (N-0xx, GO-…, R-…), citée avec son chemin et son empreinte.
- Une proposition sans décision reste écrite comme telle : par exemple, la co-élévation entre copies et la statistique conjointe du papier B, « signalées à resserrer par la réponse 22 (proposition, sans décision) ».
- Si tu crois qu'une revendication doit changer sans décision qui le dise, tu ne la changes pas : tu l'écris dans une section finale « Nœuds pour Lazar », une ligne chacun.
- Aucun chiffre de résultat. « Non trouvé » veut dire non trouvé dans les pièces lues, jamais trou du champ (R8).

## À lire (et rien d'autre)

1. La table v1 (ci-dessus), qui donne la forme à garder : sources vérifiées par empreinte, tables par papier, statut par ligne.
2. Le programme v3 tel qu'il sera scellé provisoirement le 24 à 18:30Z : `/tmp/claude-0/-home-user-controle-ia-travail/b3386204-a5cb-5f9f-8d39-6b43585b5980/scratchpad/blanc-complement-v2/programme-controle-ia-v3-complement-applique.md`. C'est l'application à blanc, sans échec, du complément v2. Lazar a gardé ses marques sur la bascule de H8 et sur le repli de N-004.
3. Le complément d'erratum v2 : `docs/notes/dossier-entretien-2026-12-01-v1/application-a-blanc-demande-27-v1/complement-erratum-demande-27-fable-v2.md`, sections 5 à 7 (second erratum, dont E2-4).
4. Les réponses 22, 22A, 22B, 22C et 22P : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22*/relecture-fable-api.md`.
5. Les décisions de `docs/decisions/` citées par la v1. Y ajouter N-057 à N-077 (versions finales ; pour N-075, la v4 ; pour N-076, ses errata, le 3 prime ; pour N-060, la v4 et son erratum 1). Le résumé de `CLAUDE.md` (section « Documents qui font foi ») sert d'index, non de source.
6. Pour les décisions du 22 novembre (retrait du lemme et du théorème, lignes T et L) : `registres/go.md`, lignes GO-2026-11-22-12, -20 et -24, et `registres/decisions.md`, lignes R-4767 à R-4830. Prends la version d'`origin/main` (`git show origin/main:registres/go.md`), plus récente que la branche.

Interdits :
- aucun fichier de résultats, de diagnostic, de scores, de verdict ou de lecture ;
- rien sous `coffre/` ;
- aucune pièce sur le mode tenu à l'écart au-delà de son existence.

## Ce que tu écris

Un seul fichier : `docs/notes/revendications-en-vigueur-v2/table-revendications-en-vigueur-v2.md`. Rien de scellé, rien d'autre de modifié, pas de commit.

Forme :
- l'en-tête de la v1, mis à jour ;
- la table des sources, avec les empreintes vérifiées par `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier <fichier>` ;
- par papier, une ligne par revendication : énoncé en vigueur, statut, décision qui le fixe ;
- statut, un seul parmi : **revendiquée**, **resserrée**, **retirée**, **mesure descriptive gardée**, **proposition sans décision** ;
- une colonne « changement depuis la v1 » ;
- puis une table courte « Ce que nous ne revendiquons plus, et pourquoi », utile au jury de l'entretien ;
- puis « Nœuds pour Lazar ».

Langue : français, sans sigle nu (les identifiants internes entre parenthèses, après l'énoncé en clair) ; phrases courtes.

Réponse finale : chemin du fichier, nombre de lignes par statut, nœuds pour Lazar, confiance.
