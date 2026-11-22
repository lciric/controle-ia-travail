# Bilan de la concordance des deux annotateurs, jeu d'épreuve de la bibliothécaire (v1)

- Date : 22 novembre 2026. Auteur : agent de concordance neuf (Claude Opus 5.5), qui n'a écrit ni les questions ni les clés et n'a pas ouvert le mémo.
- Entrées (empreintes vérifiées par leurs compagnons) : `candidates-annotateur-1-v1.jsonl`, `cles-annotateur-2-v1.jsonl`. Procédure : `docs/notes/memoire-conception-v1/epreuve-bibliothecaire-v1.md`, § 2.
- Règle appliquée : concordance = même réponse sur le fond (même concept ou même source, même état ; « non trouvé » contre « non trouvé » ; « hors périmètre » contre « hors périmètre »). Un désaccord qui demanderait de trancher qui a raison n'est pas tranché : la question est écartée et comptée.

## Comptes par type

| Type | Cible (§ 2) | Proposées | Concordantes | Écartées | Cible atteinte | Mise au point / réserve |
|---|---|---|---|---|---|---|
| Paraphrases | 30 | 36 | 35 | 1 | oui (+5) | 17 / 18 |
| À ne pas confondre | 10 | 12 | 12 | 0 | oui (+2) | 8 / 4 |
| Détails hors mémo | 10 | 12 | 12 | 0 | oui (+2) | 7 / 5 |
| Sans réponse | 20 | 24 | 24 | 0 | oui (+4) | 11 / 13 |
| Hors périmètre | 10 | 12 | 12 | 0 | oui (+2) | 6 / 6 |
| Erratum qui prime | 10 | 14 | 14 | 0 | oui (+4) | 5 / 9 |
| **Total** | **90** | **110** | **109** | **1** | | **54 / 55** |

- Chaque type atteint sa cible ; aucune question de plus n'est à écrire.
- Une question écartée (paraphrase) : les deux clés désignent deux concepts distincts ; motif dans `concordance-v1.jsonl`.
- Le jeu final dépasse les cibles dans chaque type. La procédure ne dit pas s'il faut ramener chaque type à sa cible ; je ne l'ai pas fait. Point à trancher par la session qui conduit l'épreuve, avant le premier essai (les seuils 3 et 4 du § 3 sont écrits pour 30 et 20 questions).
- Le tirage des moitiés porte sur la liste entière des id concordants, sans strate par type : la répartition par type entre les moitiés est donc inégale (colonne de droite). Commande : `tirage-v1.txt`.
- Réserve : deux clés concordantes peuvent porter des différences de détail (sources secondaires, précisions ajoutées par l'un) ; le jeu final garde la clé et les sources de l'annotateur 1, comme demandé.
