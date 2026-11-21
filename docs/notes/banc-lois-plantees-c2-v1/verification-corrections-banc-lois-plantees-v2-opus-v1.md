# Vérification des corrections — conception du banc de recherche à lois plantées, v2 — par le contre-lecteur de la v1

- **Date** : 2026-11-21, 16:22 UTC (`date -u`) ; dépôt à `ebf861d34`.
- **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), le même contre-lecteur que pour la v1 (règle « Qui conçoit », R-3735 : vérification des corrections par le même contre-lecteur). Mandat de la mère, sous GO-2026-11-21-63.
- **Contre-lecture vérifiée** : `contre-lecture-conception-fable-banc-lois-plantees-v1-opus-v1.md`, `122f2afd8bac51e8047a304f24dfa23c1621b9a411daf8c4884a8dc4f5056b8e`.
- **Pièces lues, empreintes conformes à leurs compagnons** (`sha256sum -c`, tous « OK ») :
  - `conception-fable-banc-lois-plantees-v2.md`, `62c519c0c46c8406ce5cb4a172ca4f251df62da52eba7a710f4f3d54737164aa` (lue en entier, sauf les § 2 à 5, que j'ai fouillés par motifs) ;
  - `calculs-banc-lois-plantees-v2.py`, `5adc6a09e7b1f8433826e2f081bda2563d1e23abd8c6af77f8aad621dea6c5a0` (blocs neufs lus en entier, lignes 640 à 962) ;
  - `calculs-banc-lois-plantees-v2-sortie.txt`, `6bb7f5a5ae17fd2ead23a6e76f47b72e698d2ea8924e0850fef53044b5b121f2` ;
  - `faits-banc-lois-plantees-v2.md`, `f17ad13ff0a956d6c605114f2b283245fb81eedeb2f31fd6f09cd19087113519` ; `question-banc-lois-plantees-v2.md`, `59179279f21fe2e9418a282e72024ac7d8535eadf3fa8685d251864c37367bdc` (comparées ligne à ligne à la v1).
- **Rejeu** : le `.py` v2 a été lancé une fois dans mon bloc-notes (`.venv/bin/python -I`, python 3.13.18, numpy 2.4.6, 39 s). Sa sortie est **identique à l'octet** au `.txt`. Les blocs A à G de la sortie v2 ne diffèrent de la v1 que par la ligne des graines.
- **Cloisonnement** : je n'ai ouvert aucun chemin interdit, fait aucun commit ni aucune poussée, aucun appel payant ni aucune recherche en ligne.

## Verdict

**Conforme**, avec quatre remarques mineures à porter par erratum. Les quatorze constats sont portés juste. Le cinquième laisse un résidu mineur (remarque R3). L'amendement du troisième est fondé sur un calcul que j'ai rejoué. Une précision lui manque (R1). Les six blocs neufs disent ce que la note leur fait dire. Le couple v2 est neutre.

## Les quatorze constats

| n° | état | où et comment |
|---|---|---|
| 1 | porté juste | La règle de cohérence joue dans les deux sens (§ 6.3, épreuve 11). Les doses de l'épreuve 6 sont plantées au niveau des gestes, avec une trajectoire cohérente. Le pilote reçoit un bras scripté, ou bien l'épreuve est dite « non jouée » (§ 8). Le bloc I.1 éprouve la règle sur un cas sain et sur deux artefacts. |
| 2 | porté juste | La règle 2 reprend le texte proposé. Le verdict, point 3, est restreint aux noms. Le devin conditionné à la fiche est calculé (bloc J) et fixe la barre de l'épreuve 7. La note en tire aussi une conséquence de plus : à la composition actuelle, l'épreuve 8 tue le banc. |
| 3 | porté juste, amendement accepté | « À dommage moyen égal » remplace « dommage égal ». Les trois défauts sont écrits et chiffrés (blocs H.1 et H.2). « Lit l'intention » sort de la décision D-3. Une épreuve 13 est ajoutée. L'amendement tient : le handicap par l'instrument se voit à la dispersion des données (aire 0,980, rejouée). Je retire donc « handicap invisible » comme propriété. Réserve : remarque R1. |
| 4 | porté juste | Verdict, point 1 ; § 6.6 ; relevé, pas 4 ; lectures corrigées du bloc B. |
| 5 | porté juste, résidu mineur | Le § 6.4, la décision D-4 et le § 1, point 13, ne nomment plus de famille. Le marqueur dit deux exceptions et interdit de servir la note, entière ou amputée du bloc, avant le passage d'un lecteur isolé. Un résidu demeure : remarque R3. |
| 6 | porté juste | § 6.4 ; épreuve 1 ; lectures corrigées du bloc F.1. |
| 7 | porté juste | Épreuve 3 ; § 6.4. Le bloc I.2 vérifie qu'une dose au niveau des gestes n'est plus une identité (0,710 ± 0,049 pour 0,730). |
| 8 | porté juste | Verdict, point 2 ; molette des sentinelles. |
| 9 | porté juste | § 6.8, dernier alinéa, avec l'avertissement à donner au tiers. |
| 10 | porté juste | § 9 et faits v2, au texte de la page 3. |
| 11 | porté juste | Le bloc G bis est rejoué ; les chiffres du § 8 sont fidèles (3 089 à 35 163, arrondis à 3 100 et 35 200 ; 44 373, arrondi à 44 400). |
| 12 | porté juste | Le bloc C bis donne 522 et 1 338 paires ; le § 8 dit la corrélation supposée. |
| 13 | porté juste | Décision D-2 : le retirage des mondes sans défaut, et un nœud s'il s'écarte du texte scellé. |
| 14 | porté juste | « Limites déjà vues » et la définition du flou sortent des faits. La sous-question (a) demande au-delà des travaux cités, et la (b) ne présuppose plus de définition. |

## Les six blocs neufs

- **C bis et G bis** : l'arithmétique est refaite et fidèle au texte de la note.
- **H** : la loi exacte du bloc H.1 est juste. Pour un excès d'une loi, le handicap perd 0,084 en classe 5, et le retrait uniforme 0,422. Le prototype H.2 a son contrôle (400 sur 400) et des attentes écrites ; les deux aires sont calculées sans appariement, 400 contre 400. Les aires de 1,000 (budget) et de 0,980 (dispersion) tiennent.
- **I** : la dose au niveau des gestes ne lit ni la vérité ni les données (graine 10). La règle de cohérence est muette sur cette dose et signale tout retrait fait dans le registre seul. Les aires du lecteur de budget (0,836 à 1,000) tiennent. La lecture « le prototype ne sait pas planter une dose fine invisible » est juste pour le seul geste qu'il a, le budget.
- **J** : les cinq traits sont invariants par permutation des noms. Le devin apprend sur les mondes 400 à 2 399 et est éprouvé sur les mondes 0 à 399, sans recouvrement ni lecture de la vérité à l'épreuve. Son témoin permuté retombe au hasard (0,508). L'aire de 0,694 et les 2,33 lois tiennent, et « plancher, cinq traits » est bien dit.

## Remarques nouvelles (toutes mineures)

| n° | lieu | remarque | correction proposée |
|---|---|---|---|
| R1 | § 6.5, « Il se voit » ; épreuve 13 ; décision D-3 | Les devins du handicap comparent le témoin à l'**honnête ordinaire**. La seconde lecture de D-3 oppose pourtant le témoin au **saboteur**. Un handicap visible contre l'ordinaire peut ressembler à la trace du saboteur : dans le prototype, les deux dépensent moins de budget (blocs H.2 et I.2). Ce n'est donc pas, en soi, un défaut pour cette lecture. | À l'épreuve 13 : « les devins du handicap sont rapportés deux fois, témoin contre honnête ordinaire et témoin contre saboteur ; seule la seconde aire borne ce que la lecture de D-3 peut dire ». |
| R2 | § 6.5, « Il se voit » ; bloc H.2 | L'aire de 0,980 du lecteur de dispersion dépend de l'étendue des variances naturelles du générateur, que le lecteur connaît par l'a priori public. Elle ne dit pas qu'un tel handicap est visible en soi. | Ajouter : « visible pour ce générateur ; l'étendue des variances naturelles est une molette qui peut le masquer, à éprouver ». |
| R3 | § 6.4, « Ce que l'oracle ne couvre pas » | « Le dommage né de l'assemblage » nomme hors du bloc une famille du bloc. Ce lieu n'est pas l'une des deux exceptions déclarées par le marqueur. | « Le dommage qui ne se forme qu'au niveau de la campagne… », ou ajouter ce lieu comme troisième exception au marqueur. |
| R4 | épreuve 11 ; § 6.3 | Sur 400 épisodes honnêtes, la règle de cohérence est muette par construction : l'analyste scripté inscrit exactement ce qui franchit le seuil. Sur des agents de langue, elle pourra sonner chez l'honnête. Filtrer les épisodes « diffus » ne doit alors pas trier différemment le jumeau et le suspect. | À l'épreuve 11 : « taux de la règle chez l'honnête, mesuré sur modèle et rapporté ; aucun épisode exclu d'un seul côté de la paire ». |

## Ce qui tient

Le rejeu est identique à l'octet. Les trois trouvailles neuves sont vraies dans le prototype : l'aire de 0,69 du devin de la fiche, les aires de 1,00 et 0,98 des handicaps, la dose de budget visible. Chacune est écrite contre la v1, avec ses limites. Les chances d'admission baissent en conséquence. Le couple v2 ne contient aucun nom de personne ni de modèle, aucun identifiant de décision, aucun chemin interne : la recherche de motifs est vide. Le seul ajout aux faits, la fiche composée par case, est un fait du dessin, non une réponse glissée.
