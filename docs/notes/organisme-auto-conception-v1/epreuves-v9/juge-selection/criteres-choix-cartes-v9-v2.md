# Critères de choix des cartes à éprouver — organisme d'idéation, courses d'auto-conception — v2

- **Écrits le 2026-11-19 (`date -u` : 2026-11-19T13:52:08Z) sans lecture d'aucune carte ; scellés avant toute lecture.**
- Écrits par un rédacteur neuf (modèle F), sur mandat de la mère, après GO-2026-11-19-68, point 4 (« deux ou trois cartes veto par juge » ; « le probleme est donc les criteres de selection qui sont trop severes pour astra et carbon et les eliminent »). Pièce de travail, à contre-lire par un modèle O. Processeur seul, aucune dépense, aucun appel de modèle.
- **Remplace, pour les sélections à venir**, `docs/notes/organisme-auto-conception-v1/course-v2/criteres-choix-cartes-v9-v1.md` (sha256 `8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326`), qui reste archivé sans modification. Ne refait pas la sélection de la course v9 : celle-ci est tranchée par GO-2026-11-19-55 à -63.
- **Lu, et rien d'autre** (sur `main`, commit `0cf9ac92`, empreintes recalculées) : les critères v1 (`8881dbb2…`) ; la proposition `proposition-cartes-a-eprouver-v9-v1.md` (`a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856`) ; sa contre-lecture `contre-lecture-proposition-cartes-v9-v1.md` (`a923cb57702a055d7c0460c990e5ecff5dd6125c1f0c0460cedba67de606fc43`) ; les lignes GO-2026-11-19-55 à -68 de `registres/go.md` ; sur la branche, la note de conception sur le juge v1 (`3b0332a1…`) et sa contre-lecture (`6214b44d…`).
- **Non lus** : aucune carte (ni `fiches.json` ni aucun autre fichier de cartes), aucun verdict de juge, le classement, le coffre, le champ de l'espèce.
- **Limite dite d'avance.** La proposition et sa contre-lecture nomment des cartes de la v9, leurs notes et ce qui les a fait tomber : je sais donc quels critères de la v1 ont écarté quoi. Cette règle est conçue en connaissance de ces écarts. Son rejeu sur la v9 ne serait pas une épreuve tenue à l'écart ; sa première épreuve honnête est la course suivante, où elle est scellée avant l'ouverture des cartes.
- Ce texte ne choisit rien. Il fixe la règle qu'appliqueront les lecteurs, à la lettre. Un critère inapplicable ne se change pas : l'écart s'écrit dans la proposition.

## 0. Principe, et ce qui n'est pas un critère

**Principe (mot de Lazar ; N-058).** « ce sont les essais avec experiences qui doivent trancher in fine les cartes et les tetss de mort ». Cette règle, les lecteurs, les juges et le veto ne font que choisir ce qui va à l'épreuve et dans quel ordre le proposer. Aucun d'eux n'adopte ni ne condamne une carte. Une carte non retenue n'est pas réfutée : elle n'est pas éprouvée.

Ne sont pas des critères :
- le verdict des juges de la course (« notable » ou non), leur avis pondéré et le classement de l'orchestrateur ; les lecteurs n'ouvrent pas le classement ;
- l'espèce du proposeur : les cartes se lisent sans leur champ `meta` ; aucune espèce n'est lue par un lecteur, à aucun moment de la sélection ;
- **le coût de l'épreuve** : il est rapporté (§ 6) ; il n'entre ni dans une note, ni dans un plancher, ni dans le départage ;
- le nombre de cartes d'un regroupement, ou la rencontre de plusieurs espèces sur une même idée ;
- le mot « inédit » d'un proposeur, et tout chiffre ou travail publié cité par une carte (règles R7 et R8) ;
- l'ordre alphabétique d'un identifiant, ou tout autre ordre sans contenu.

## 1. Lecteurs

- **Deux lecteurs neufs**, qui n'ont écrit ni ces critères ni une carte : l'un de la lignée Opus, l'autre de la lignée Fable. Ils sont de la même famille : c'est déclaré, et leur accord ne vaut pas deux regards indépendants. Un troisième lecteur d'une autre famille est un appel payant : sur devis et ligne neuve seulement.
- Chacun lit toutes les cartes sans le champ de l'espèce, seul, sans voir le travail de l'autre, et rend : exclusions, voie, notes, raisons, veto.
- Le masque d'espèce est imparfait (un style se reconnaît). Chaque lecteur écrit, pour chaque carte de son veto, s'il croit en reconnaître la lignée.
- **Aucun désaccord n'est résolu par discussion.** Les deux lectures sont versées telles quelles ; un programme les assemble selon les § 4 à 9.

## 2. Exclusions, appliquées d'abord, sur le texte de la carte

Une carte est écartée, sans note, si **les deux lecteurs** y trouvent le même cas. Si un seul le trouve, la carte est notée, avec la réserve écrite.

- **X1 — un modèle décide.** Un modèle (note, score, juge, aiguilleur, vote de modèles) trie, promeut, élimine, alloue le budget ou choisit ce qui va à l'épreuve, dans le mécanisme ou dans le critère de l'épreuve. Un modèle qui propose, traduit ou écrit, sous un critère calculé par programme, n'est pas un modèle qui décide. Si la carte porte une mesure séparable de sa part décisionnelle sans changer son épreuve, elle reste pour sa mesure seule, avis descriptif (GO-2026-11-19-63, point 1) ; sinon elle est écartée.
- **X2 — porte « le séquentiel doit battre le meilleur de N tirages à budget égal »** prise comme mécanisme ou comme critère décisif (N-073, § 2). Si ce critère est un témoin parmi d'autres et que l'épreuve se juge sans lui, la carte reste, avec la réserve « critère à réécrire, pratique à citer ».
- **X3 — pas d'oracle exécutable.** L'épreuve se juge par la note d'un juge, par une lecture humaine, ou sur un monde sans vérité plantée.
- **X4 — sélection d'agents sur le verdict d'un juge** (N-053, point 5 ; N-058 ; N-059, point 14).
- **X5 — principe occupé présenté comme le mécanisme même, sans forme distincte** (listes « Ne plus écrire » et « Ne pas écrire » de N-073 et de ses compléments ; composantes du juge cédées par N-067, § 4).
- **X6 — les cartes retenues par l'aiguilleur de la course** : hors du choix, non ouvertes.

Chaque exclusion est nommée dans la proposition avec le cas et la phrase de la carte qui le porte. Aucune carte n'est « rangée sans un mot ».

## 3. Trois voies d'entrée

Chaque lecteur range chaque carte non exclue dans **une** voie, par cette suite de questions, dans cet ordre :

1. La carte dit-elle comment mesurer, rejouer ou adopter un mécanisme, plutôt qu'un mécanisme de l'organisme ? → **voie I, instrument**.
2. Sinon, son épreuve répond-elle directement à l'une des cinq questions du programme ? → **voie P, question du programme**.
3. Sinon → **voie N, question neuve**. Le lecteur écrit la question en une phrase. S'il ne peut pas l'écrire, la carte est « sans question » et le dit ; elle garde ses notes des § 4.1 et 4.3 et reste dans le lot tiré au sort (§ 8).

Les cinq questions du programme sont celles des critères v1, § 2, critère C2, lues à la lettre : (a) l'héritage ; (b) le juge au nul formé des lois connues ; (c) la sélection — ce que la génération suivante lit, et toute **règle de survie des fiches**, condition de conservation, d'oubli ou de réentrée comprise ; (d) la multiplicité entre cartes et entre essais ; (e) les juges croisés. La liste se met à jour par décision de Lazar seulement, avant l'ouverture.

Si les deux lecteurs ne donnent pas la même voie, la carte est candidate dans les deux ; elle ne compte qu'une fois si elle est retenue, dans la voie où son rang est le meilleur.

## 4. Trois critères notés, chacun de 0 à 2

**4.1 — E, ce que la carte permet d'éprouver sur monde planté** (critère C1 de la v1, inchangé).
- 2 : la carte dit, ou permet d'écrire sans rien inventer, (i) un oracle qui est un programme comparant les sorties à la vérité plantée ; (ii) un bras témoin sans le mécanisme, à coût apparié, et une base bon marché ; (iii) une règle de lecture chiffrable d'avance, où un « oui » et un « non » sont tous deux définis.
- 1 : l'oracle est exécutable, mais le témoin ou l'appariement du coût manque et peut être ajouté sans toucher au mécanisme.
- 0 : cas X3.

**4.2 — Q, la question.** Elle se note dans la voie de la carte ; **une question neuve n'y vaut jamais zéro par construction**.
- Voie P. 2 : l'épreuve répond directement à l'une des cinq questions, nommée. 1 : elle l'éclaire de biais ; le lecteur dit laquelle et pourquoi de biais.
- Voie N. 2 : la question, écrite en une phrase, ne se ramène à aucune des cinq, et la décision de conception qu'elle commande est nommée (quel module garder, retirer ou régler). 1 : la question est écrite, mais elle est voisine de l'une des cinq (le lecteur dit laquelle), ou la décision qu'elle commande n'est pas nommée.
- Voie I. 2 : l'instrument sert la mesure ou l'adoption de plusieurs lignes, ou de toute modification de l'organisme. 1 : il n'en sert qu'une, nommée.
- 0, dans toute voie : le lecteur ne peut écrire ni question ni usage. Il l'écrit en toutes lettres.

**4.3 — D, valeur des deux issues** (critère C5 de la v1 ; règles R3 et R4).
- 2 : un « oui » et un « non » changeraient chacun une décision de conception nommée.
- 1 : une seule des deux issues apprend quelque chose.
- 0 : aucune.

**Ce qui était noté et ne l'est plus.**
- Le coût (critère C3 de la v1) : rapporté, § 6.
- La collision avec un travail publié (critère C4 de la v1, qui valait 1 pour toutes les lignes et ne départageait rien) : rapportée, § 6. Une collision n'interdit pas de mesurer, elle interdit de dire ; elle n'exclut qu'au cas X5.

**Chaque note porte sa raison en une phrase**, pour chaque carte et chaque lecteur. Une note sans raison est une lecture à refaire, pas une note.

## 5. Plancher, fusion, strates, nombre visé

- **Plancher, le même dans les trois voies** : E ≥ 1, Q ≥ 1, D ≥ 1 et E + Q + D ≥ 4 sur 6. **Une carte passe le plancher dès qu'un des deux lecteurs l'y met.** L'erreur de lecture est un mode d'échec constaté (contre-lecture `a923cb57…`, majeure M9) : un seul lecteur ne suffit pas à faire tomber une carte.
- **Note d'une carte** : la somme des totaux des deux lecteurs, de 0 à 12. Tout écart de deux points sur un même critère entre les deux lecteurs est listé dans la proposition.
- **Fusion** : seulement les cartes qu'une même épreuve juge — même oracle, mêmes bras, même monde planté —, quand les deux lecteurs le disent. La ligne porte la carte la mieux notée et prend sa note ; les autres sont des variantes ou des bras. Tout autre rapprochement est une « fusion raisonnée » : il est dit comme tel et ne retire aucune carte de la liste.
- **Strates.** Une strate est une voie ; dans la voie P, chacune des cinq questions est une sous-strate. Les strates se définissent par le contenu de la carte, **jamais par l'espèce**.
- **Nombre visé, K lignes.** K est donné par la mère avant l'ouverture des cartes, d'après la charge d'écriture permise (GO-2026-11-19-67) ; à défaut, K = 9.
- **Quotas par strate.** Deux places réservées par voie, tant que la voie a deux lignes au plancher (une seule si elle n'en a qu'une). Les places restantes vont au rang, toutes voies confondues. Dans la voie P : deux lignes au plus par question, tant qu'une ligne au plancher existe pour une question non couverte.
- **Rien n'est éliminé par le nombre visé.** La proposition liste **toutes** les lignes au plancher, dans l'ordre, celles au-delà de K marquées « au plancher, hors du nombre visé ». K borne ce que la proposition recommande en premier, pas ce que Lazar peut prendre.

## 6. Ce qui est rapporté sans peser

- **Coût.** Pour chaque ligne : l'étage sur processeur s'il existe et ce qu'il peut conclure ; le premier étage capable de porter un « oui » et un « non » ; son ordre de grandeur en dollars et l'hypothèse de calcul ; la mention « plusieurs générations » le cas échéant. **Une seule convention, la même pour toutes les lignes** : le coût rapporté est celui du premier étage qui porte les deux issues, non celui d'un étage préparatoire. Ces ordres de grandeur ne sont pas des devis. Le coût sert ensuite à l'ordre de passage — amélioration attendue d'abord (GO-2026-11-19-60), puis bon marché d'abord (N-045, point 4) — et à la décision de dépense de Lazar, sur devis ; il ne sert pas ici.
- **Collision.** Voisins nommés, tous « non vérifié » sauf ceux lus sur source et nommés par les décisions ; citations obligatoires à porter ; revendication resserrée touchée (juge au nul, héritage) et sa lettre.
- **Réserves des juges de la course**, si elles sont connues par une pièce versée : dites comme telles, sans effet sur la note.

## 7. Droit de veto contre l'élimination

Mot de Lazar (GO-2026-11-19-68) : « deux ou trois cartes veto par juge ».

- **Titulaires.** Chaque lecteur du § 1. Chaque juge de la course aussi, si la course lui a fait rendre sa liste de veto dans une sortie prévue pour cela et scellée avant l'ouverture des cartes par les lecteurs ; sinon, les lecteurs seuls.
- **Ce que le veto fait.** Il empêche l'élimination : la carte désignée entre dans la proposition, sur une liste à part, « entrée par veto », en plus du nombre visé. **Il ne fait rien adopter, ne retire aucune carte, ne change aucune note ni aucun rang, et ne s'exerce jamais contre une carte.**
- **Sur quoi.** Toute carte non retenue : sous le plancher, hors du nombre visé, perdue au départage ou absorbée par une fusion. Le veto ne lève aucune exclusion du § 2.
- **Limite.** V cartes par titulaire, la même pour tous : **V = 3 s'il y a trois titulaires au plus, V = 2 au-delà**, sauf mot contraire de Lazar avant l'ouverture. Un veto non exercé ne se reporte pas et ne se cède pas.
- **Hors de sa lignée.** Le titulaire désigne sans voir l'espèce : il rend une liste **ordonnée** de V cartes et de deux suppléantes. Après le dépôt de toutes les listes, un programme lit l'espèce, retire de chaque liste les cartes de la lignée du titulaire et garde les V premières qui restent. Le titulaire n'apprend pas ce qui a été retiré avant la fin de la sélection. Les veto tombés sur une carte de la même famille sans être de la même lignée (Opus et Fable) restent valides, et sont comptés à part.
- **Ce que le titulaire écrit, pour chaque carte.** L'issue qu'il prédit pour l'oracle, et la décision de conception que l'épreuve changerait. Scellé avec la liste. Chaque veto devient ainsi une prédiction vérifiable après l'épreuve.
- **Gardes.** Le taux de réussite des veto est rapporté par titulaire ; il ne sert ni à choisir ni à pondérer un juge ou un lecteur (N-058 ; N-059, point 14). La répartition des veto par espèce est comptée après coup par programme, dans les deux sens (§ 10).

## 8. Lot tiré au sort, bras témoin

- **Vivier** : les lignes non exclues, avec E ≥ 1 chez un lecteur au moins, qui ne sont ni dans le nombre visé ni entrées par veto — au plancher ou non.
- **Tirage** : une ligne par voie (trois au plus), sans pondération, par programme. La graine est dérivée par `numpy.random.SeedSequence` de l'empreinte de ce fichier scellé et de l'identifiant de la course (règle R9) : elle est fixée avant toute lecture et consignée au manifeste.
- **Rôle** : bras témoin. Aucun modèle n'y décide. Ces lignes vont à l'épreuve comme les autres, marquées « tirées au sort », et donnent la base contre laquelle se compare ce que la règle et le veto ont proposé : part des épreuves qui changent une décision de conception, et leur coût.
- Le lot n'est pas une voie de repêchage et ne remplace aucun veto.

## 9. Règle de départage, dans cet ordre

1. note la plus haute (somme des deux lecteurs) ;
2. E le plus haut ;
3. D le plus haut ;
4. Q le plus haut ;
5. la strate ou la sous-strate qu'aucune ligne mieux classée ne couvre ;
6. le plus petit écart entre les deux lecteurs ;
7. en dernier recours, **tirage au sort par programme**, graine dérivée comme au § 8 et consignée. La proposition nomme les lignes départagées ainsi, « à égalité, départagées par tirage ».

Jamais par le coût, le verdict d'un juge, le classement de l'orchestrateur, l'espèce ou l'ordre alphabétique. Une ligne à égalité stricte avec la dernière retenue, et perdante au tirage, est signalée en tête de la liste « hors du nombre visé ».

## 10. Ce que la proposition doit dire

- Pour chaque carte : voie, trois notes et leur raison, par lecteur. Pour chaque ligne : sa strate, la question nommée, le rapport de coût et de collision du § 6.
- Quatre listes, distinctes : lignes dans le nombre visé ; lignes au plancher hors du nombre visé ; cartes entrées par veto (titulaire, prédiction, décision visée) ; lignes tirées au sort (graine).
- Les désaccords des deux lecteurs : voies, exclusions vues par un seul, écarts de deux points.
- **L'espèce, en dernier, par programme** : la part de chaque espèce dans chacune des quatre listes et sous le plancher. Un écart fort, dans un sens ou dans l'autre, pour n'importe quelle espèce, déclenche le même audit (règle R4) ; il ne corrige jamais la liste.
- Les écarts à ces critères, non corrigés.
- La proposition propose ; Lazar choisit ; l'épreuve tranche.

## 11. Ce que ces critères ne font pas, et ce qui attend le mot de Lazar

- Ils ne disent pas qu'une carte vaut mieux qu'une autre, ni que la règle v1 avait tort : seule l'épreuve le dira.
- Ils ne corrigent aucun biais d'un juge : aucun n'est mesuré.
- Ils ne fixent ni devis, ni seuil d'épreuve, ni hypothèse, ni revendication.
- **À confirmer par Lazar avant le premier usage** : (1) le coût retiré de la note pour toutes les cartes, ce qui va au-delà de la lettre de GO-2026-11-19-60, qui ne le lève que pour une carte dont l'amélioration attendue est considérable ; (2) la limite du veto, trois à trois titulaires au plus, deux au-delà ; (3) le nombre visé par défaut, neuf ; (4) les trois lignes du lot tiré au sort, qui sont des épreuves en plus.
