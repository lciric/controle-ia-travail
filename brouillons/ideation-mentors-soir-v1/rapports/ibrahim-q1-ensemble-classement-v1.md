# Classement D — question 1 de Lujain Ibrahim, ensemble (tour, fiches du matin, course) — v1

Classeur neuf D, 3 novembre 2026, de 15:07:06 à environ 15:24 UTC (`date -u`). Aucune recherche, aucun appel de modèle autre que le classeur. Je n'ai lu ni le classement précédent d'une partie, ni `lecteur-A/`, `pour-lazar/`, `/tmp/soir-tours-v1/`, `coffre-*` ou la clé de préparation. Seuls les noms des dossiers voisins sont apparus dans une liste du dossier parent.
**Pas de témoin déguisé** (protocole du soir, section 2) : l'axe d'originalité n'est pas contrôlé. La note d'originalité vient de la moisson seule.

## Entrées vérifiées
- Consigne `soir-classeur-D-ibrahim-q1-ensemble-v1.md`, sha256 `15804e62…6aafa` : concorde.
- Protocole du soir, sha256 `fbbbb520…a5ca5b347` : concorde. Ancres : protocole Heimersheim v1, section 5, sha256 `942b9324…0fdbad18`, et pièce `piece-ibrahim-v1.md`, section 1, sha256 `4e3851e3…a6d6149`. La consigne ne donnait aucune empreinte attendue pour ces deux fichiers ; je consigne celles que j'ai mesurées.
- Fiches `fiches-servies-v1.json` (23 fiches), sha256 `b77b8c5f…a94a9e1` : concorde. Moisson `moisson-fusionnee-v1.json` (23 entrées), sha256 `21021ef7…57ec04ac` : concorde.

## Porte (19 dans le sujet, 4 hors sujet)
Règle : une fiche est dans le sujet si elle peut être la première expérience de la direction de la pièce. Cette direction est la persistance, après un apprentissage par renforcement, d'une persona installée par entraînement de caractère, et son effet sur la sycophancie. Une porte d'instrument de cette expérience compte aussi.
Hors sujet : IB-05, IB-11, IB-12 et IB-13. Ce sont les quatre fiches dont la moisson porte la mention « moisson du matin ». Elles traitent de la loi des notes sous pression du modèle de base, sur les fichiers des campagnes antérieures, sans persona ni renforcement. Elles ne sont pas notées. Ce choix est le mien : si le directeur les juge dans le sujet, elles restent à noter.

## Notes (ancres et raisons en une ligne : `notes-v1.json`)
Colonnes : originalité vérifiée, puis testable en jours, puis prolonge un outil de la mentore, puis la somme.

| Fiche | Originalité | Testable | Outil | Somme | | Fiche | Originalité | Testable | Outil | Somme |
|---|---|---|---|---|---|---|---|---|---|---|
| IB-17 | 2 | 3 | 3 | **8** | | IB-01 | 2 | 1 | 2 | 5 |
| IB-18 | 2 | 2 | 3 | **7** | | IB-15 | 2 | 2 | 1 | 5 |
| IB-20 | 2 | 2 | 3 | **7** | | IB-19 | 2 | 1 | 2 | 5 |
| IB-03 | 2 | 2 | 2 | **6** | | IB-21 | 2 | 1 | 2 | 5 |
| IB-10 | 1 | 3 | 2 | **6** | | IB-09 | 1 | 2 | 2 | 5 |
| IB-16 | 1 | 2 | 3 | **6** | | IB-14 | 1 | 2 | 2 | 5 |
| IB-22 | 1 | 2 | 3 | **6** | | IB-02 | 1 | 2 | 1 | 4 |
| IB-23 | 1 | 2 | 3 | **6** | | IB-07 | 1 | 1 | 2 | 4 |
| IB-04 | 1 | 2 | 3 | 6 (tirée hors des huit) | | IB-08 | 1 | 2 | 1 | 4 |
| | | | | | | IB-06 | 1 | 1 | 1 | 3 |

Aucune fiche dans le sujet n'est « ouverte » d'après la moisson. Aucune non plus n'est « déjà faite ».
Une réserve commune n'est pas comptée : toutes les fiches à persona dépendent des poids d'Open Character Training, dont l'accès est annoncé comme filtré et n'a pas été vérifié (pièce, section 3).

## Les huit et leurs égalités
On range par somme. Une égalité se départage d'abord par l'originalité, comme le veut la consigne. Il en restait. J'ai donc appliqué les critères suivants dans l'ordre où la consigne les énonce : testable en jours, puis prolonge un outil. IB-10 entre ainsi grâce à sa note 3 en testabilité.
IB-04, IB-16, IB-22 et IB-23 restaient alors à égalité parfaite (1, 2, 3) pour trois places. J'ai tiré au sort avec `default_rng(SeedSequence(e).spawn(1)[0]).permutation(4)` sur leurs identifiants triés. Ce flux de graines est distinct de celui des paires. Ordre tiré : IB-23, IB-22, IB-16, IB-04 ; **IB-04 est exclue**. Cette règle a été fixée après lecture des notes, mais avant tout jugement par paires.
Les huit retenues : IB-03, IB-10, IB-16, IB-17, IB-18, IB-20, IB-22 et IB-23.

## Paires et forces de Bradley-Terry
- Il y a 28 paires, chacune jugée dans les deux ordres, soit 56 jugements. Ils suivent l'ordre `default_rng(SeedSequence(e)).permutation(56)`, avec e = 13221315473417726430 (hexadécimal `b77b8c5fa07069de`). Codage : les paires sont rangées dans l'ordre lexicographique des identifiants triés, et l'indice vaut k = 2p + o, où o = 1 inverse l'ordre.
- Les jugements ont été écrits par lots de 14, à 15:16:38, 15:17:56, 15:18:23 et 15:18:50, dans `paires-v1.jsonl`. Le script revérifie le plan tiré, rang par rang.
- Le script est en numpy seul (version 2.5.3) et ne fait appel à aucun modèle. Il utilise l'algorithme de minorisation-majorisation. Ses gardes ont été éprouvées avant le calcul. Sur le cas sain simulé, l'ordre est retrouvé (Spearman 1,0, écart maximal de 0,017 sur l'échelle logarithmique). Un juge cohérent au format réel est accepté. Neuf artefacts sont refusés : jugement manquant, rang en double, ordre hors plan, gagnante hors de la paire, mauvaise graine, identifiants changés, graphe non connexe, séparation sans pseudo-comptes, matrice non finie.
- L'estimateur du maximum de vraisemblance n'existe pas (condition de Ford). IB-20 perd tout, et IB-17 et IB-18 gagnent tout sauf l'une contre l'autre. Les forces sont donc calculées sous pseudo-comptes déclarés : 0,5 victoire ajoutée à chaque côté de chaque paire.
- Victoires sur 14 : IB-17 13, IB-18 13, IB-10 10, IB-03 7, IB-22 7, IB-16 4, IB-23 2, IB-20 0. La première présentée gagne 30 fois sur 56 : pas d'effet d'ordre marqué.
- Forces sur l'échelle logarithmique : IB-17 = IB-18 = +1,341 ; IB-10 +0,636 ; IB-03 = IB-22 = +0,005 ; IB-16 −0,628 ; IB-23 −1,086 ; IB-20 −1,615.
- Rééchantillonnage des 28 paires (2 000 tirages ; 2 tirages exclus et déclarés, une fiche y était absente). Rangs médians : IB-17 2 et IB-18 2 (rang 1 dans 47 % et 48 % des tirages), IB-10 3, IB-22 4, IB-03 5, IB-16 6, IB-23 7, IB-20 8. Les intervalles à 95 % se chevauchent par blocs : [1 ; 3] pour IB-17 et IB-18, [1 ; 5] pour IB-10, [3 ; 6] pour IB-03 et IB-22, [4 ; 7] pour IB-16, [6 ; 8] pour IB-23 et IB-20.
- **Défaut relevé dans le script v1** : deux égalités exactes de force (IB-17 et IB-18 ; IB-03 et IB-22) ne sont pas signalées. Son champ `ordre_final` les range par ordre alphabétique, ce qui n'est pas un départage. Je ne réécris pas la sortie. Je départage selon une règle déclarée : la somme des notes d'abord (IB-17 8 contre IB-18 7), puis l'originalité (IB-03 2 contre IB-22 1, à somme égale de 6). Cette règle donne le même ordre que le tri alphabétique, mais pour une raison écrite.

## Cohérence
26 paires sur 28 concordent dans les deux ordres, soit **0,929** : c'est au-dessus de 0,8. Les deux discordances sont IB-17 contre IB-18 et IB-03 contre IB-22. Dans les deux cas, j'ai changé d'avis à la réflexion sur une paire serrée.
**Réserve, juge unique** : un seul juge, dans un seul contexte, se souvient de ses jugements précédents. Plusieurs raisons renvoient d'ailleurs à un rang antérieur (« même raison qu'au rang N »). La cohérence mesure donc surtout la mémoire, non la stabilité. Le seuil de « presque parfaite » (0,9, dans le script) a été choisi après les jugements. La réserve vaut quel que soit ce seuil.

## Drapeaux de risque devant la mentore (parmi les huit)
- **IB-16, oui.** La fiche prête à sa taxonomie une prédiction empirique, à savoir que les cellules ne covarient pas. Elle déclare « la fragmentation morte » si ρ ≥ 0,8. Or, dans la taxonomie, la fragmentation désigne des études qui donnent le même nom à des comportements de forme différente (pièce, section 1.2). La mentore peut récuser ce critère de mort.
- **IB-22, oui.** La fiche écrit « 470 ou 235, chiffres non réconciliés » et en fait une faiblesse de son juge. La mentore peut réconcilier ces chiffres d'emblée : la prépublication donne deux accords et deux kappas sur 235 réponses (pièce, section 1.1). Le cœur de la fiche, la validité de son juge d'un point de contrôle à l'autre, reste sain.
- **IB-17, IB-18, IB-10, IB-03, IB-20, IB-23, non.** Ce qu'elles disent des travaux de la mentore est conforme à la pièce : AnthroBench (9 comportements sur 14), traitement des refus, taxonomie, limites déclarées. Une précision pour IB-18 : dire « sur plusieurs tours » plutôt que « longitudinale » pour AnthroBench, car son travail « dans la durée » est un autre papier (pièce, section 1.5).
- Hors des huit : IB-04 et IB-01 portent aussi un drapeau « oui » (détail dans `notes-v1.json`). Les deux touchent ELEPHANT : IB-04 traite la validation des sentiments comme du simple style, et IB-01 présente comme sienne la distinction entre émotion et conduite.

## Ordre final
**IB-17, IB-18, IB-10, IB-03, IB-22, IB-16, IB-23, IB-20.**
IB-17 et IB-18 sont à égalité de force ; la somme des notes les départage. IB-03 et IB-22 sont aussi à égalité de force ; l'originalité les départage. Les intervalles de rang se chevauchent ; seuls les blocs {IB-17, IB-18}, {IB-10}, {IB-03, IB-22, IB-16} et {IB-23, IB-20} sont nets.

## Fichiers (dans `/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/classement-D/`)
- `notes-v1.json`, sha256 `1ad71fce9be878f7a066d2fe99a663e7ec1d4409f6388fc018ccb72c09c4a8e9`
- `paires-v1.jsonl`, sha256 `8c5001b7c3080a0d103d492a9382d6bcad3090a7fcd8335972bddbef8269a1d2`
- `bradley_terry_ibrahim_q1_v1.py`, sha256 `e5082dbe6f19a3ba1e9205c25a06bb6be1a210738a41d699dbd6614e9a990eb3`
- `bradley_terry_ibrahim_q1_v1-sortie.json`, sha256 `da494d130a41e7fa9856c23f60383d16bab463e925dea23e3da34572295a0c50` (elle consigne les empreintes du script, des paires et des notes ; je les ai vérifiées)
- `classement-v1.md` : son empreinte est donnée dans la réponse finale.
