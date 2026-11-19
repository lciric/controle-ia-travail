# Rejeu à blanc des critères de choix des cartes v2 sur la course v9 — lecteur F — v1

- **Écrit le 2026-11-19 (`date -u` : 2026-11-19T14:05:06Z)** par un lecteur neuf (modèle F), sur mandat de la mère (GO-2026-11-19-68). Processeur seul, hors ligne, aucune dépense, aucun appel de modèle.
- **Ce que c'est.** Une épreuve à blanc de la règle v2, par un seul des deux lecteurs qu'elle prévoit. Elle ne refait pas la sélection de la course v9, tranchée par GO-2026-11-19-55 à -63, et ne propose rien à éprouver. Les juges, les lecteurs et le veto ne font que choisir ce qui va à l'épreuve ; l'épreuve tranche (mot de Lazar ; N-058).
- **Verdict en trois lignes.**
  1. Le plancher de la v2 n'élimine plus rien : 92 cartes sur 94 y passent, et 49 des 50 cartes que les lignes GO nomment comme gardées. Les quatre cartes nommées comme non gardées y passent aussi.
  2. La règle ne départage presque pas : 28 cartes ont la note maximale, et les neuf places du nombre visé ont été données par tirage au sort entre ex æquo. Le recoupement du nombre visé avec les cartes gardées par Lazar est de 3 sur 9.
  3. Le seul critère qui sépare les cartes dans ma lecture est D (valeur des deux issues), et il tombe du même côté pour presque toutes les cartes que les lignes GO attribuent à Astra, Carbon et Argon : la sévérité que Lazar nomme a quitté le plancher et se retrouve dans le rang. À regarder avant le premier usage réel (règle R4).

## 1. Pièces, empreintes, ordre des lectures

| Pièce | Chemin | sha256 |
|---|---|---|
| Critères v2 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-choix-cartes-v9-v2.md` | `4ae09b15e2816fcda0ba0ba008ca11b58906d7712351253d04f52214e9a629c1` |
| Cartes | `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json` | `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481` |
| Sélections scellées | `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/selections-rejeu-a-blanc-criteres-v2-lecteur-f-v1.json` | `e42b5f05d0f9b2c8423fc0d005e5d5c414c1023208e049201074ecf91ec69fc6` |
| Lignes GO | `registres/go.md` sur `main`, commit `416a33428e2d1bba28751680721a759f4d1359d3` | `0682f0aa8a102b9c76256878e8ab08dfd8bcc7dcff57e99cbd824f8c98752aa1` |

Ordre tenu, vérifiable dans l'historique de la branche `lot/compte-organisme-v1` :

1. L'empreinte des critères v2 a été recalculée et comparée au compagnon : identique. Leur commit `14e9954d` (2026-11-19T13:53:31Z) précède ma première ouverture de `fiches.json` (après 13:56:51Z).
2. Les 94 cartes ont été lues en entier pour six champs (titre, module changé, mécanisme, épreuve sur monde planté, ce qui la réfuterait, et le début de ce qui la distingue), par un programme qui retire le champ `meta` avant tout affichage.
3. Les notes, la liste de veto et le programme d'assemblage ont été écrits ; le programme a tourné **une seule fois** ; sa sortie a été scellée, versée et poussée (commit `3543a767bd4e67189ba8e28c7b76f57b09f31d82`).
4. Seulement ensuite, les lignes GO-2026-11-19-55, -56, -57, -59, -61 et -63 ont été ouvertes, pour leurs identifiants.

**Non ouverts** : les verdicts des juges, le classement, le coffre, le dossier d'aiguillage, le champ `meta`, le rejeu de l'autre lecteur, la proposition v1 et sa contre-lecture.

## 2. Limites, à lire avant les chiffres

- **Un seul lecteur.** La v2 demande deux lecteurs et fait de leur somme la note (0 à 12). Ici la note est mon total (0 à 6). Les règles « écartée si les deux lecteurs y trouvent le même cas », « passe le plancher dès qu'un des deux l'y met », la fusion et le départage par l'écart entre lecteurs n'ont pas pu jouer. Une exclusion vue par moi seul devrait, à la lettre du § 2, laisser la carte notée avec réserve ; je la rapporte comme exclusion de ce lecteur.
- **Ce n'est pas une épreuve tenue à l'écart.** La v2 le dit elle-même : elle a été conçue en connaissance de ce que la v1 avait écarté sur ces mêmes cartes.
- **Masque d'espèce imparfait.** Le champ `meta` n'a jamais été affiché, mais les styles se reconnaissent : au moins quatre manières d'écrire reviennent (phrases à l'infinitif très courtes ; modules en gras ; protocole « à budget égal » récité ; prose en phrases complètes). Je n'ai attribué aucune carte à une lignée pendant la lecture. Les lignes GO, ouvertes après le scellement, nomment l'espèce de 44 cartes : je ne l'ai su qu'à ce moment.
- **Lecture en six champs.** Les champs coût, limites et plus proche voisin n'ont pas été lus. Le coût et la collision ne sont pas des critères de la v2 ; le rapport du § 6 (coût, collision) n'est pas fait ici.
- **X6 non appliqué.** Le mandat donne les 94 cartes à passeport ; je n'ai pas ouvert le dossier d'aiguillage pour en retirer celles que l'aiguilleur de la course aurait retenues.
- **Filtre de lignée du veto non appliqué** : il exige de lire l'espèce.
- **Fusions non appliquées.** Elles exigent l'accord de deux lecteurs. Les familles voisines sont marquées dans le JSON (`groupe_fusion_raisonnee`) et ne retirent aucune carte : le nombre visé peut donc contenir deux cartes d'une même famille.
- **K = 9** (défaut du § 5), **V = 3** (deux titulaires).

## 3. Ce que la règle a donné

### 3.1 Exclusions (§ 2) : 2 cartes

- `fafa0062508c9`, coupe avant exécution par contraste de logits — **X1**. La carte écrit que l'orchestrateur « ordonne les cartes par leur écart à la médiane des témoins faux plantés » et n'envoie à l'épreuve « que la tranche supérieure » : le score d'un modèle lecteur choisit ce qui va à l'épreuve, et le critère de l'épreuve mesure ce tri. Aucune mesure séparable sans changer l'épreuve.
- `fefca0bd94064`, pondération décorrélée des juges — **X1**. La carte « pondère l'agrégation des juges croisés par la covariance inverse pour trier l'accès au budget des tests de mort », et son critère (rappel des lois vraies après ce tri) juge le tri. J'ai lu la mesure comme non séparable sans changer l'épreuve. **Divergence avec GO-2026-11-19-63, point 1**, qui garde cette carte avec l'avis des juges seulement descriptif, et renvoie à Lazar si le rédacteur ne peut pas séparer.

Cinq autres cartes sur les juges croisés (`f6f8c8b855234`, `fa38f9faa24e0`, `fb3a2cc87251c`, `fc37640a0181d`, `fcfa3d98b90f8`) restent, avec la réserve « X1 vu en partie, carte gardée pour sa mesure seule » : leur épreuve mesure l'erreur des juges contre la vérité plantée, non un tri. Vingt-deux cartes portent la réserve X2 (« meilleur de N » témoin parmi d'autres, critère à réécrire, pratique à citer) ; aucune n'est exclue pour X2. Aucun cas X3, X4 ou X5 trouvé.

### 3.2 Voies et notes

| Voie | Cartes notées | Au plancher | Note 6 | Dans le nombre visé |
|---|---|---|---|---|
| I, instrument | 13 | 13 | 4 | 2 |
| P, question du programme | 44 | 44 | 19 | 5 |
| N, question neuve | 35 | 35 | 5 | 2 |
| Total | 92 | 92 | 28 | 9 |

Dans la voie P : question (a) héritage, 4 cartes ; (b) juge au nul, 4 ; (c) sélection et règle de survie, 25 ; (d) multiplicité, 5 ; (e) juges croisés, 6.

Les triplets de notes sont au nombre de quatre seulement : (E 2, Q 2, D 1) pour 60 cartes ; (2, 2, 2) pour 28 ; (2, 1, 2) pour 2 ; (2, 1, 1) pour 2.

- **E vaut 2 partout.** Toutes les cartes écrivent un oracle programmé, un bras sans le mécanisme, une base bon marché et une règle de lecture chiffrable : la consigne de la course l'imposait. Le critère E ne départage rien sur ce lot.
- **Q vaut 2 pour 88 cartes sur 92.** Dans la voie N, écrire la question en une phrase et nommer le module touché suffit presque toujours.
- **D porte tout le rang.** J'ai donné 2 quand la carte nomme ce que le « non » change (« la base suffit », « on cesse de servir », « tout reste la règle », « rien à corriger ») et 1 quand le « non » n'est écrit que comme abandon du mécanisme.

### 3.3 Les quatre listes

**Dans le nombre visé (9).** Les six premières sont les places réservées ; les neuf ont été départagées par tirage, les rangs 4, 7, 8 et 9 après que le départage par sous-strate non couverte a réduit le lot des ex æquo.

| Rang | Carte | Voie | Titre |
|---|---|---|---|
| 1 | `f76714f1ddda4` | I | Porte séquentielle sur chaque auto-modification de l'organisme |
| 2 | `f7219bb36cfcb` | I | Bras à retour permuté : l'épreuve lie-t-elle la génération suivante ? |
| 3 | `fc53dfee17677` | P (c) | Réentrée par quota des éliminées à faible marge |
| 4 | `fcfa3d98b90f8` | P (e) | Double rendu des cartes et abstention du juge instable |
| 5 | `fe0ce53be28b3` | N | Verdict de mort sur réimplémentations indépendantes |
| 6 | `ff3f04bf88c72` | N | Séparer hypothèse réfutée et exécution invalide |
| 7 | `f0d21fb62aff2` | P (a) | Archive servie ou factice, lue à trois échéances |
| 8 | `f01d286e78e83` | P (d) | Porte e-BH et rejeu de quarantaine avant entrée en état |
| 9 | `fcc96538bff00` | P (b) | Témoin d'énumération sans modèle dans le nul du pari |

**Au plancher, hors du nombre visé (83)**, dont 19 à égalité stricte avec la dernière retenue. Liste ordonnée dans le JSON.

**Entrées par veto du lecteur F (3)**, liste écrite avant le tirage, prise dans l'ordre parmi les cartes non retenues :

| Carte | Titre | Issue prédite pour l'oracle | Décision que l'épreuve changerait | Lignée reconnue ? |
|---|---|---|---|---|
| `f51c0935052f6` | Nul de rappel : sessions sans données dans le nul du juge | la part des promotions rappelées baisse, la puissance sur les lois neuves tient | nul du juge statistique complété ou non | je crois reconnaître la famille des lignées Opus et Fable, sans pouvoir dire laquelle |
| `f6e7646851ba5` | Rejeu d'inertie de chaque mécanisme ajouté à une version | rappel de 1 sur les mécanismes inertes ; la couverture de code en laisse passer | rejeu à chaque version, ou simple couverture de code | même réponse |
| `f169420b8d1d8` | Effort de recherche compté dans le seuil de promotion | sans registre, le niveau est dépassé quand les variantes sont nombreuses | procédure de fin de course de N-059, point 2 | même réponse |

Suppléantes, dans l'ordre : `fed7a993d9671` (héritage lu contre placebo), `f562951db6c70` (témoins jumeaux contre l'a priori familier). Si le filtre de lignée retirait les trois premières, il ne resterait que ces deux-là : la liste d'un lecteur qui reconnaît mal les lignées peut se vider.

**Tirées au sort (3)**, une par voie, graine dérivée de l'empreinte des critères et de l'identifiant de la course : `ff60dbc7baa6f` (I, vivier de 10), `f17603c39bc32` (P, vivier de 37), `f19c4c823d67c` (N, vivier de 33).

Total proposé à l'épreuve par ce rejeu : **15 cartes** (I : 4 ; P : 8 ; N : 3).

## 4. Comparaison aux cartes gardées par Lazar

Les six lignes GO nomment par leur identifiant **50 cartes gardées** et **4 cartes non gardées** (GO-2026-11-19-63, point 2). Les 40 autres ne sont pas nommées. Ce compte est un plancher : les lignes gardent aussi des « fusionnées » sans les nommer, une liste de cartes « les plus originales » rendue ailleurs, et la question de l'héritage sans identifiant.

| Ensemble de ce rejeu | Taille | Nommées gardées | Nommées non gardées | Non nommées |
|---|---|---|---|---|
| Au plancher | 92 | 49 | 4 | 39 |
| Note 6 | 28 | 11 | 0 | 17 |
| Nombre visé | 9 | 3 | 0 | 6 |
| Veto | 3 | 2 | 0 | 1 |
| Tirées au sort | 3 | 3 | 0 | 0 |
| Proposées à l'épreuve (les trois listes) | 15 | 8 | 0 | 7 |
| Exclues | 2 | 1 | 0 | 1 |

**Gardées par Lazar, et que la v2 aurait proposées (8).** Nombre visé : `f01d286e78e83`, `f76714f1ddda4`, `fcc96538bff00`. Veto : `f169420b8d1d8`, `f6e7646851ba5`. Tirage : `f17603c39bc32`, `f19c4c823d67c`, `ff60dbc7baa6f`.

**Gardées par Lazar, et que la v2 n'aurait pas proposées en premier (42).** Une est exclue (`fefca0bd94064`, X1, voir § 3.1). Les 41 autres sont au plancher, donc sur la liste que la v2 remet à Lazar « au plancher, hors du nombre visé » : six à la note 6, perdues au tirage (`f5373a31410ab`, `f856659046065`, `f8c05bffe7cb1`, `fb3a2cc87251c`, `fc36c3c3125ac`, `ff99ce570c638`) ; trente-trois à la note 5 ; deux à la note 4 (`f14a90c4535dd`, `fec2307cbabb1`). La v2 ne les élimine pas ; elle ne les recommande pas en premier.

**Proposées par la v2, et non nommées par les lignes GO (7).** `f7219bb36cfcb` (bras à retour permuté), `fc53dfee17677` (réentrée par marge, sœur de `f856659046065` qui est gardée), `fcfa3d98b90f8` (double rendu et abstention du juge instable), `fe0ce53be28b3` (réimplémentations indépendantes), `ff3f04bf88c72` (hypothèse réfutée ou exécution invalide, voisine de l'interprète de référence gardé « avec ses fusionnées »), `f0d21fb62aff2` (archive servie ou factice : c'est la question de l'héritage, que GO-2026-11-19-55 garde sans identifiant), et par veto `f51c0935052f6` (nul de rappel). Deux seulement ouvrent une ligne que les GO n'ont sous aucune forme, à ma lecture des identifiants : le bras à retour permuté et le double rendu des cartes.

**Note 6 non nommées par les GO (17)** : outre les six ci-dessus hors veto et le nul de rappel, `f11193560f4d4`, `f2033ad1cbe45`, `f2d60f571d0e2`, `f473bb6a03ca3`, `f6f8c8b855234`, `f760c773d6f15`, `f7a4918afe116`, `fc37640a0181d`, `fdfac3afd4bae`, `fed7a993d9671`. Sept de ces dix-sept portent sur l'héritage ou sur ce que la génération suivante lit.

**Les quatre cartes nommées non gardées** (`f4a47f030c829`, `fcf27198b7462`, `f98b6974fb1dd`, `fbac0bab50a65`) ont toutes la note 5 et passent le plancher : rien dans la v2 ne les distingue des trente-trois cartes gardées de même note.

## 5. Ce que l'épreuve à blanc dit de la règle

1. **Le plancher ne trie plus.** Avec E à 2 partout, le plancher (4 sur 6, chaque note au moins 1) laisse tout passer. L'effet voulu par GO-2026-11-19-68 est atteint, au-delà : la règle ne dit plus « non » à rien d'autre qu'aux deux cartes X1.
2. **Le rang est un tirage.** Vingt-huit cartes à égalité stricte sur les quatre premiers départages ; le nombre visé est une loterie stratifiée entre elles. Deux lecteurs donneront des sommes de 8 à 12 et moins d'ex æquo, mais le lot tiré au sort du § 8, censé servir de bras témoin, se distinguera mal du nombre visé.
3. **Le critère D suit la manière d'écrire.** D'après les espèces nommées par les lignes GO (lues après scellement, 44 cartes) : Astra, 12 cartes nommées, aucune à la note 6 ; Argon, 16, aucune ; Carbon, 10, une seule ; Opus, 3, aucune ; Fable, 3, deux. Dans le nombre visé : Astra 0, Argon 0, Carbon 1, Fable 1. Le veto n'a rien corrigé : mes trois veto sont tombés sur des cartes que je crois de ma propre famille. Ce compte porte sur 44 cartes seulement, et sur un seul lecteur, de la lignée Fable. Deux lectures restent ouvertes, et je ne peux pas les départager : ces cartes disent réellement moins ce qu'un « non » changerait ; ou bien ma lecture de D récompense une phrase de plus (« la base suffit ») que certaines lignées écrivent par habitude. Dans les deux cas, le fait est le même : **sous la v2 lue par ce lecteur, aucune carte nommée d'Astra ni d'Argon n'entre dans le nombre visé ni par veto ; une seule carte d'Astra entre, par le lot tiré au sort.**
4. **Pistes, pour Lazar seul (rien n'est changé ici).** (a) Préciser D : dire si « abandon du mécanisme » vaut une décision nommée, ce qui mettrait presque toutes les cartes à 6 et ferait du nombre visé un tirage assumé. (b) Faire jouer le filtre de lignée du veto avec des suppléantes plus nombreuses, puisqu'un lecteur désigne d'abord ce qui lui ressemble. (c) Attendre le second lecteur, d'une autre manière de lire, avant de conclure : l'accord de deux lecteurs de la même famille ne vaut pas deux regards (§ 1 de la v2).

## 6. Écarts à la lettre des critères, non corrigés

- Un lecteur au lieu de deux ; note sur 6 ; pas de liste des désaccords.
- Exclusions prononcées par un seul lecteur.
- X6 non appliqué ; aucune fusion ; filtre de lignée du veto non appliqué.
- Rapport de coût et de collision du § 6 non fait ; part de chaque espèce du § 10 non calculée par programme (le champ `meta` n'est pas lu), remplacée par le compte partiel du § 5, point 3.
- Programmes d'assemblage et de comparaison gardés hors du dépôt (dossier de travail de la session) ; leur sortie est le JSON scellé.

## Annexe A — les 94 cartes, une ligne par carte

Colonnes : identifiant ; titre ; voie (I instrument, P question du programme avec sa lettre, N question neuve, X exclue) ; E, Q, D et total ; sort dans ce rejeu (K : dans le nombre visé, avec son rang ; V : veto du lecteur F ; T : tirée au sort ; P : au plancher, hors du nombre visé ; X : exclue) ; ligne GO qui la nomme comme gardée (« non » : nommée comme non gardée par GO-2026-11-19-63 ; « — » : non nommée). Les raisons de chaque note, la question écrite pour chaque carte de la voie N et les réserves sont dans le JSON scellé.

| Carte | Titre | Voie | E | Q | D | Total | Sort | GO |
|---|---|---|---|---|---|---|---|---|
| `f01d286e78e83` | Porte e-BH et rejeu de quarantaine avant entrée en état | P (d) | 2 | 2 | 2 | 6 | K8 | -57 |
| `f0497de657ec8` | Témoin à calcul apparié pour chaque bras du bisociateur | I | 2 | 1 | 2 | 5 | P | — |
| `f0a8378953d43` | Portefeuille orthogonal et bifurcation à vidage mémoire | P (c) | 2 | 2 | 1 | 5 | P | -61 |
| `f0d21fb62aff2` | Archive servie ou factice, lue à trois échéances | P (a) | 2 | 2 | 2 | 6 | K7 | — |
| `f11193560f4d4` | Dose d'archive aux proposeurs, jugée sur familles plantées | P (c) | 2 | 2 | 2 | 6 | P | — |
| `f11f00774547f` | Jumeau contrefactuel aveugle dans les tests de mort | N | 2 | 2 | 1 | 5 | P | — |
| `f1373c384a771` | Seuil d'e-valeur pénalisé par les essais et jetons amont | P (d) | 2 | 2 | 1 | 5 | P | — |
| `f14a90c4535dd` | Compacter la mémoire sans changer ses propositions | N | 2 | 1 | 1 | 4 | P | -59 |
| `f1675a6c453a9` | Certificats de portée pour les conclusions | N | 2 | 2 | 1 | 5 | P | -59 |
| `f169420b8d1d8` | Effort de recherche compté dans le seuil de promotion | P (d) | 2 | 2 | 2 | 6 | V | -55 |
| `f17603c39bc32` | Réducteur à oubli programmé et bifurcation sans juge | P (c) | 2 | 2 | 1 | 5 | T | -61 |
| `f19c4c823d67c` | Portefeuilles d'épreuves par pouvoir de distinction | N | 2 | 2 | 1 | 5 | T | -59 |
| `f19c7995f9c6a` | Deux exécutions indépendantes avant de garder | N | 2 | 2 | 1 | 5 | P | — |
| `f1c19731ccffb` | Garde de parité d'information et rejeu d'ablation du nul | P (b) | 2 | 2 | 1 | 5 | P | -57 |
| `f1d7c5f2e47d7` | Banque d'échecs étalonnée et bornée par tests de mort | P (c) | 2 | 2 | 1 | 5 | P | -57 |
| `f2033ad1cbe45` | Verdict de mort sur k réimplémentations indépendantes | N | 2 | 2 | 2 | 6 | P | — |
| `f20fbf8b6d797` | Banque d'échecs structurels calibrée avec péremption | P (c) | 2 | 2 | 1 | 5 | P | — |
| `f232221730a16` | Allocation des bras du bisociateur sur l'issue scellée | N | 2 | 2 | 1 | 5 | P | -61 |
| `f2d60f571d0e2` | Double implémentation aveugle avant tout « survit » | N | 2 | 2 | 2 | 6 | P | — |
| `f2e3582b5fa97` | Carrés factoriels de modifications complémentaires | N | 2 | 2 | 1 | 5 | P | — |
| `f319823a86ea7` | Contrat exécutable entre carte et mesure | N | 2 | 2 | 1 | 5 | P | — |
| `f327b86c669cc` | Rotation de contexte à quotas structurels | P (c) | 2 | 2 | 1 | 5 | P | -61 |
| `f38a6ed2f7434` | Coupure de lignée et réensemencement sur plateau d'oracle | P (c) | 2 | 2 | 1 | 5 | P | -63 |
| `f4250eb75fbba` | Empilement préquentiel M-ouvert et audit de décision nulle | P (b) | 2 | 2 | 1 | 5 | P | -57 |
| `f473bb6a03ca3` | Bifurquer puis vider le contexte servi, sur déclencheur codé | P (c) | 2 | 2 | 2 | 6 | P | — |
| `f4a47f030c829` | Fourche et purge sur saturation des bardeaux d'archive | P (c) | 2 | 2 | 1 | 5 | P | non |
| `f4b85ff3c1033` | Portefeuille sous-modulaire de survie inter-générations | P (c) | 2 | 2 | 1 | 5 | P | -57 |
| `f4cbf7e62ff7b` | Paires de fusion à couverture équilibrée | N | 2 | 2 | 1 | 5 | P | — |
| `f51c0935052f6` | Nul de rappel : sessions sans données dans le nul du juge | P (b) | 2 | 2 | 2 | 6 | V | — |
| `f5373a31410ab` | Mémoire négative datée : l'échec gardé avec sa condition | P (c) | 2 | 2 | 2 | 6 | P | -56 |
| `f562951db6c70` | Témoins jumeaux contrefactuels contre l'a priori familier | I | 2 | 2 | 1 | 5 | P | -61 |
| `f5662015db5bf` | Disjonction d'exécution et quarantaine des échecs aux tests | N | 2 | 2 | 1 | 5 | P | -57 |
| `f5ee3a75faea3` | Ancrage structurel par facettes et quota d'anti-effondrement | N | 2 | 2 | 1 | 5 | P | -63 |
| `f68f93bac44e8` | Seuil de réentrée et vidage périodique contre la dérive | P (c) | 2 | 2 | 1 | 5 | P | -63 |
| `f69c4a2a9c9e7` | Redite mesurée sur ce que les lois engagées prédisent | N | 2 | 2 | 1 | 5 | P | — |
| `f6bb348e95955` | Recenser les idées par leur comportement | I | 2 | 2 | 1 | 5 | P | -59 |
| `f6caf922edbf1` | Banque d'échecs étalonnée à expiration et seuil de rejet | P (c) | 2 | 2 | 1 | 5 | P | -57 |
| `f6e7646851ba5` | Rejeu d'inertie de chaque mécanisme ajouté à une version | I | 2 | 2 | 2 | 6 | V | -56 |
| `f6f8c8b855234` | Votes effectifs du collège, mesurés sur témoins plantés | P (e) | 2 | 2 | 2 | 6 | P | — |
| `f71350282d0c0` | Appariement par conflit d'issues vérifiées au bisociateur | N | 2 | 2 | 1 | 5 | P | -63 |
| `f7219bb36cfcb` | Bras à retour permuté : l'épreuve lie-t-elle la génération suivante ? | I | 2 | 2 | 2 | 6 | K2 | — |
| `f760c773d6f15` | Réducteur d'archive servie, lu à trois points du budget | P (c) | 2 | 2 | 2 | 6 | P | — |
| `f76714f1ddda4` | Porte séquentielle sur chaque auto-modification de l'organisme | I | 2 | 2 | 2 | 6 | K1 | -61 |
| `f772b4c18818b` | Portefeuille couvrant des survivants et quota de queue | P (c) | 2 | 2 | 1 | 5 | P | -61 |
| `f7782e931911d` | Épreuve de permutation causale des issues en bac à sable | N | 2 | 2 | 1 | 5 | P | -56, -57 |
| `f7a4918afe116` | Mémoire factice appariée : héritage lu à trois budgets | P (a) | 2 | 2 | 2 | 6 | P | — |
| `f7b38afebd589` | Décomposition résiduelle des facettes par l'orchestrateur | N | 2 | 2 | 1 | 5 | P | — |
| `f7cc0003c4b2c` | Porte contrefactuelle sur l'auto-modification du harnais | I | 2 | 2 | 1 | 5 | P | -61 |
| `f856659046065` | Réentrée tirée des cartes éliminées contre la famine | P (c) | 2 | 2 | 2 | 6 | P | -55 |
| `f89c771e3ac68` | Dédupliquer les prédictions, pas leurs formulations | N | 2 | 2 | 1 | 5 | P | -55, -59 |
| `f8c05bffe7cb1` | Placebo de sélection et tirage de confirmation scellé | P (c) | 2 | 2 | 2 | 6 | P | -56 |
| `f91a7a590c8fe` | Oubli programmé et plafond de réentrée entre générations | P (c) | 2 | 2 | 1 | 5 | P | -61 |
| `f98b6974fb1dd` | Porte d'auto-modification contrefactuelle à e-valeurs | I | 2 | 2 | 1 | 5 | P | non |
| `f9a517d00f493` | Sas d'admission à double strate contre la dérive d'état | P (d) | 2 | 2 | 1 | 5 | P | -57 |
| `f9c8c39740352` | Quotas de dépense contre la famine des cartes coûteuses | N | 2 | 2 | 1 | 5 | P | — |
| `fa312929593cf` | Mémoire négative admise par seul verdict de test de mort | P (c) | 2 | 2 | 1 | 5 | P | — |
| `fa38f9faa24e0` | Étalonnage continu des juges par erreurs plantées | P (e) | 2 | 2 | 1 | 5 | P | -57, -63 |
| `fa46f1f3bd417` | Rejeu de réimplémentation fraîche aux tests de mort | N | 2 | 2 | 1 | 5 | P | — |
| `fafa0062508c9` | Coupe avant exécution par contraste de logits sur témoins | X (X1) | — | — | — | — | X | — |
| `fb2a799e80c91` | Contre-épreuve par permutation causale aux tests de mort | N | 2 | 2 | 1 | 5 | P | — |
| `fb3a2cc87251c` | Votes effectifs du collège mesurés sur témoins plantés | P (e) | 2 | 2 | 2 | 6 | P | -55 |
| `fb45c8739b3d2` | Seuil d'e-valeur indexé sur la dépense amont scellée | P (d) | 2 | 2 | 1 | 5 | P | -57 |
| `fb484116eccc4` | Pièges à raccourcis contrefactuels et test de permutation | N | 2 | 2 | 1 | 5 | P | — |
| `fb6f958eb1bb6` | Redite comptée par la loi prédictive, non par les mots | N | 2 | 2 | 1 | 5 | P | — |
| `fb9e8ae1b97b8` | Transmission entre générations d'une banque d'échecs prouvés | P (c) | 2 | 2 | 1 | 5 | P | -57 |
| `fbac0bab50a65` | Masquage contrefactuel des témoins et du bac à sable | N | 2 | 2 | 1 | 5 | P | non |
| `fbae5b702558e` | Porte transactionnelle des auto-modifications | I | 2 | 2 | 1 | 5 | P | — |
| `fc1f059e8873e` | Témoin d'archive factice entre deux générations | I | 2 | 1 | 2 | 5 | P | — |
| `fc36c3c3125ac` | Audit de rejeu : un mécanisme change-t-il une décision ? | I | 2 | 2 | 2 | 6 | P | -56 |
| `fc37640a0181d` | Votes effectifs du collège mesurés sur témoins plantés | P (e) | 2 | 2 | 2 | 6 | P | — |
| `fc53dfee17677` | Réentrée par quota des éliminées à faible marge | P (c) | 2 | 2 | 2 | 6 | K3 | — |
| `fcbf4a2dd1a57` | Sentinelle de dérive des juges sur un panier d'ancrage | P (e) | 2 | 2 | 1 | 5 | P | — |
| `fcc96538bff00` | Témoin d'énumération sans modèle dans le nul du pari | P (b) | 2 | 2 | 2 | 6 | K9 | -55 |
| `fcd56a5ce3c1c` | Masquer les explications, conserver les observations | N | 2 | 2 | 1 | 5 | P | -59 |
| `fcf27198b7462` | Bifurcation et vidage sur détection déterministe de bassin | P (c) | 2 | 2 | 1 | 5 | P | non |
| `fcfa3d98b90f8` | Double rendu des cartes et abstention du juge instable | P (e) | 2 | 2 | 2 | 6 | K4 | — |
| `fd31770b6907d` | Redite lue sur la loi engagée, étalonnée sur jumeaux | N | 2 | 2 | 1 | 5 | P | — |
| `fd688912a8667` | Porte de version à témoins de modification plantés | I | 2 | 2 | 1 | 5 | P | -56 |
| `fd81c25c080e8` | Réplication par interprète indépendant | N | 2 | 2 | 1 | 5 | P | -59 |
| `fd9bbc7b19deb` | Choisir les expériences qui séparent les hypothèses | N | 2 | 2 | 1 | 5 | P | -59 |
| `fdafe4598caad` | Réducteur d'oubli et bifurcation à calendrier fixe | P (c) | 2 | 2 | 1 | 5 | P | -63 |
| `fdcf828b0dc80` | Portefeuille de survivants à couverture comportementale | P (c) | 2 | 2 | 1 | 5 | P | -59 |
| `fdfac3afd4bae` | Placebo d'héritage : sélection servie contre permutée | P (a) | 2 | 2 | 2 | 6 | P | — |
| `fe0ce53be28b3` | Verdict de mort sur réimplémentations indépendantes | N | 2 | 2 | 2 | 6 | K5 | — |
| `fe15813583b5c` | Paires de fusion éloignées par leurs prédictions | N | 2 | 2 | 1 | 5 | P | -61 |
| `fe887ca5cb62c` | Jumeaux permutés et trace de lecture aux tests de mort | N | 2 | 2 | 1 | 5 | P | — |
| `fec2307cbabb1` | Certificat de nouveauté dans une archive finie | N | 2 | 1 | 1 | 4 | P | -59 |
| `fed7a993d9671` | Héritage lu contre héritage placebo, à trois échéances | P (a) | 2 | 2 | 2 | 6 | P | — |
| `fefca0bd94064` | Pondération décorrélée des juges sur témoins à erreurs | X (X1) | — | — | — | — | X | -63 |
| `ff3f04bf88c72` | Séparer hypothèse réfutée et exécution invalide | N | 2 | 2 | 2 | 6 | K6 | — |
| `ff60dbc7baa6f` | Porte de version sur familles plantées tenues à l'écart | I | 2 | 2 | 1 | 5 | T | -61 |
| `ff6ddb6c537f6` | Vérifier que le script teste bien la carte | N | 2 | 2 | 1 | 5 | P | — |
| `ff76aee57bba1` | Bifurcation à vidage sur plateau de coût marginal | P (c) | 2 | 2 | 1 | 5 | P | -61 |
| `ff99ce570c638` | Arrêt sur plateau de redites et réallocation au bras neuf | N | 2 | 2 | 2 | 6 | P | -61 |

