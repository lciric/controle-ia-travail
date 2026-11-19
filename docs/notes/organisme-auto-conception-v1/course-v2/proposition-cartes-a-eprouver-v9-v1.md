# Proposition — cartes de la course d'auto-conception v9 à éprouver sur monde planté — v1

- Écrite par un rédacteur neuf (Claude Fable 5.2), sur mandat de la mère (règle « Qui conçoit », R-3735), le 2026-11-19. Pièce de travail (classe C). Processeur seul, aucune dépense, rien de commis. **Ce texte propose ; le choix est un nœud de la mère et de Lazar, et chaque épreuve est sur devis** (N-058 ; préenregistrement de la course, « Plan d'analyse »).
- Critères appliqués : `criteres-choix-cartes-v9-v1.md`, sha256 `8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326`, scellés avant l'ouverture des cartes.
- Cartes lues : `fiches.json`, commit `8029ae7f`, sha256 `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`, conforme. Les 94 cartes à passeport lues en entier, champ `meta` retiré (espèce non lue). Les deux cartes retenues par l'aiguilleur n'y figurent pas et n'ont pas été cherchées. Coûts : lecture descriptive `lecture-course-v9-v1.md` (`0306adf7…`), § 3.
- Non lus : le classement de l'orchestrateur, le coffre (verdicts et clés), tout fichier interdit par le mandat. Les réserves des juges citées ici sont celles que la lecture descriptive nomme (§ 4) ; je n'ai pas ouvert les verdicts carte par carte (écart 3, § 6).
- Chaque carte est l'avis d'un proposeur, jamais un fait. Tout travail cité par une carte est **non vérifié** (règle R7). Rien ici n'est dit nouveau, propre ou libre (règle R8).

## 1. Verdict

Cinq lignes passent en tête, toutes notées 8 ou 9 sur 10, et **toutes commencent par un étage sur processeur seul** : proposeurs ou juges scriptés, vérité plantée, aucun appel de modèle.

| rang | ligne | carte porteuse | question | note |
|---|---|---|---|---|
| 1 | l'effort de recherche compté dans le seuil de promotion | `f169420b8d1d8` | multiplicité | 9 |
| 2 | ce que le nul formé des lois connues laisse passer | `fcc96538bff00` | juge au nul | 9 |
| 3 | les votes effectifs des juges croisés, mesurés sur témoins plantés | `fb3a2cc87251c` | juges croisés | 9 |
| 4 | la réentrée tirée au sort des cartes éliminées de peu | `f856659046065` | sélection | 9 |
| 5 | la redite comptée par ce que les lois prédisent | `f89c771e3ac68` | multiplicité et nul, de biais | 8 |

La question de l'héritage (N-073, § 1) n'entre pas dans les cinq : ses cartes passent le plancher (7 sur 10) mais leur épreuve coûte plusieurs courses. C'est l'écart le plus lourd de cette proposition ; il est dit au § 6 et porté dans la décision (§ 7).

## 2. Application des critères

- **Exclusions.** X1, un modèle décide : `fafa0062508c9` (un score de logits trie ce qui va à l'épreuve ; le juge Opus l'avait marqué, ma lecture le confirme). X2, la comparaison à calcul apparié contre des tirages indépendants prise comme mécanisme même : `f0497de657ec8` ; elle reste une condition du programme (N-073, § 2), pas une carte à prendre. X6 : les deux cartes retenues, non ouvertes. X3, X4, X5 : aucune carte.
- **Au plancher ou au-dessus** : 58 cartes, en treize lignes après fusion. **Sous le plancher** : 34 cartes, presque toutes par le coût (plusieurs générations à trois ou quatre bras, C3 = 0) joint à un lien de biais ou nul avec les cinq questions.
- **Notes des lignes** (C1 éprouvable, C2 question, C3 coût, C4 collision, C5 deux issues) :

| ligne | porteuse | C1 | C2 | C3 | C4 | C5 | total |
|---|---|---|---|---|---|---|---|
| effort de recherche dans le seuil | `f169420b8d1d8` | 2 | 2 | 2 | 1 | 2 | 9 |
| ce que le nul laisse passer | `fcc96538bff00` | 2 | 2 | 2 | 1 | 2 | 9 |
| votes effectifs des juges | `fb3a2cc87251c` | 2 | 2 | 2 | 1 | 2 | 9 |
| réentrée des éliminées de peu | `f856659046065` | 2 | 2 | 2 | 1 | 2 | 9 |
| redite par les prédictions | `f89c771e3ac68` | 2 | 1 | 2 | 1 | 2 | 8 |
| interprète de référence face au script | `fd81c25c080e8` | 2 | 1 | 2 | 1 | 2 | 8 |
| jumeau permuté aux tests de mort | `f7782e931911d` | 2 | 1 | 2 | 1 | 2 | 8 |
| portefeuille de survivants par couverture | `fdcf828b0dc80` | 2 | 2 | 2 | 1 | 1 | 8 |
| placebo de sélection et tranche fraîche | `f8c05bffe7cb1` | 2 | 2 | 1 | 1 | 2 | 8 |
| héritage : archive servie, factice ou aucune | `fed7a993d9671` | 2 | 2 | 0 | 1 | 2 | 7 |
| banque d'échecs datée | `f5373a31410ab` | 2 | 2 | 0 | 1 | 2 | 7 |
| quarantaine des exécutions avortées | `f5662015db5bf` | 2 | 1 | 1 | 1 | 2 | 7 |
| portefeuille sous-modulaire sur quatre générations | `f4b85ff3c1033` | 2 | 2 | 0 | 1 | 2 | 7 |

- **C4 vaut 1 partout** : aucune porteuse n'a ses voisins lus sur source au dépôt. C'est un constat sur l'état des lectures, pas un départage.
- **Départage du cinquième rang.** Cinq lignes à 8. Le coût écarte le placebo de sélection (C3 = 1) ; la valeur des deux issues écarte le portefeuille par couverture (C5 = 1 : maximiser la distance entre signatures couvre presque mécaniquement plus de classes qu'un tirage uniforme, un « oui » apprendrait peu). Restent la redite, l'interprète et le jumeau permuté. Le jumeau permuté a deux voisins non lus, les deux autres un seul. Entre ces deux, le dernier recours (ordre alphabétique de l'identifiant) donne la redite. Je le dis tel quel : ce cinquième rang tient à peu de chose.

## 3. Les cinq lignes proposées

Coûts réels de la v9, pour l'échelle : un appel de proposeur de 0,38 à 2,25 USD selon l'espèce ; un juge de 0,03 à 0,07 USD par carte ; la course entière 72,50 USD, soit 1,8 fois son devis. Un « étage sur processeur » ne coûte aucun appel ; il coûte un préenregistrement écrit par Fable, sa contre-lecture par l'autre modèle, et du temps de machine.

### 3.1 L'effort de recherche compté dans le seuil de promotion — `f169420b8d1d8`, « Effort de recherche compté dans le seuil de promotion »

- **Fusionnées** : `f1373c384a771` et `fb45c8739b3d2` (seuil indexé sur les essais et les jetons dépensés en amont) ; en second temps `f01d286e78e83` et `f9a517d00f493` (une carte promue ne devient état transmis qu'après un rejeu sur données fraîches, sous correction de multiplicité).
- **Ce qu'elle changerait.** Le juge statistique compte aujourd'hui les cartes soumises. Il compterait tous les engagements scellés de la course, y compris ceux que l'aiguilleur, la mémoire anti-redite ou la règle « affinage » ont refusés. Un registre des essais tenu par l'orchestrateur, jamais servi à un agent.
- **Épreuve.** Monde planté à lois vraies (effets faibles compris) et fausses. Proposeurs **scriptés**, deux classes au même nombre d'appels : « peu de variantes par lignée » et « beaucoup de variantes ». Quatre bras : l'organisme actuel ; la correction de Bonferroni sur les cartes soumises ; une confirmation unique sur un lot tenu à l'écart ; le registre.
  - Oracle : part des lois fausses plantées promues, avec sa borne haute, et part des lois vraies promues.
  - Un « oui » : dans la classe « beaucoup de variantes », l'organisme actuel dépasse le niveau d'erreur annoncé et le registre le tient, sans tomber sous la puissance de la confirmation unique. La multiplicité entre cartes est alors un trou réel, et bouchable.
  - Un « non » : soit l'organisme actuel tient déjà le niveau (rien à corriger), soit la confirmation unique domine (on garde la base bon marché), soit le registre ne tient pas le niveau (le compte des essais est mal défini).
- **Coût.** Étage scripté : processeur seul, 0 USD d'appels. Avec de vrais proposeurs, plus tard : de l'ordre d'une course v9 par bras, sur devis.
- **Voisins à vérifier, non vérifiés** : « What survives honest evaluation? » (439.1 du catalogue) ; « Finite Resources False Discovery Rate Control » (210.1) ; « When Statistical Discoveries Become State » (512.1) ; « Replay the Scientist » (511.0).
- **Réserves.** Le contrôle des comparaisons multiples par e-valeurs n'est plus revendiqué (N-067, § 4) : la carte le dit elle-même, tout texte devra le redire avec les citations obligatoires. Des proposeurs scriptés ne sont pas des modèles. Ce qui compte comme « un essai » est un choix, rattaché par des bardeaux de mots que la ligne 3.5 met justement en doute. La procédure de fin de course reste à fixer sur devis (N-059, point 2).

### 3.2 Ce que le nul formé des lois connues laisse passer — `fcc96538bff00`, « Témoin d'énumération sans modèle dans le nul du pari »

- **Fusionnées** : `f4250eb75fbba` (nul par empilement des lois de l'archive, contre les mélanges convexes et les doublons reparamétrés) ; `f1c19731ccffb` (nul informé des mêmes entrées que les proposeurs, et rejeu qui écarte une loi qui ne déplace aucune prédiction) ; `fec2307cbabb1` (certificat qu'une proposition ne se dérive pas d'une archive finie) ; en étage payant `f51c0935052f6` (« nul de rappel » : lois écrites par des sessions qui ne voient aucune donnée).
- **Ce qu'elle changerait.** Aujourd'hui une promotion dit « bat les lois de l'archive ». Le nul recevrait en plus ce qu'on trouve sans mérite : ce qu'une énumération sans modèle retrouve, ce qu'un mélange des lois connues prédit déjà, ce qui se rappelle sans données.
- **Épreuve.** Un banc de témoins que le nul devrait absorber, tous étiquetés par construction : lois vraies « à portée » d'un dictionnaire et « hors de portée », mélanges convexes et doublons de l'archive, témoins « vrais mais dérivables ». Bras : le nul d'archive actuel ; le nul réduit à la meilleure loi passée ; le nul enrichi de l'énumération ; le nul empilé ; un contrôle à dictionnaire vide, qui doit égaler le nul actuel.
  - Oracle : part des promotions tombant sur des lois que le nul aurait dû absorber ; puissance sur les lois hors de portée ; fausses promotions sous le niveau annoncé. Les trois conditions sont jointes, sur deux grammaires fixées d'avance.
  - Un « oui » : le nul enrichi retire des promotions sans mérite sans perdre de puissance sur les lois hors de portée. On sait alors ce que le nul actuel laissait passer, et de combien.
  - Un « non » : le nul actuel écartait déjà tout cela (bonne nouvelle, à rapporter comme mesure), ou l'enrichissement mange la puissance, ou le contrôle à vide diffère (le banc est faux).
- **Coût.** Étage principal : processeur seul, de quelques minutes à quelques heures par famille selon la carte. Le « nul de rappel » demande des sessions de modèle et des bras à vrais proposeurs : de l'ordre d'une course v9 ou plus, sur devis.
- **Voisins à vérifier, non vérifiés** : « Dictionaries, Not Darwin » (arXiv 2607.04108 ; N-073, § 2, le range parmi les gardes « très probablement prises ») ; « Stacking-Based Weighting for Large Language Bayes in M-Open Settings » (451.0) ; « Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects » (indice 57) ; « Recursive self-improvement of AI research agents » (indice 112).
- **Réserves.** C'est la ligne la plus exposée. N-071 dit la mise en commun ajustée occupée dans ses deux moitiés (Large Language Bayes et sa variante par empilement, lues) ; l'empilement ne peut donc pas être présenté comme un apport. Seule la réunion reste revendicable, sous réserve, et « libre hors du dépôt » reste non déclarable. La mesure, elle, est celle que N-067, § 5, dit « à faire » : le nul d'archive écarte-t-il ce qu'un nul classique laisse passer. La validité des e-valeurs sous un nul qui mêle archive et énumération n'est pas établie. La grammaire du dictionnaire est un choix humain qui peut encoder la vérité plantée : audit du générateur d'abord (N-073, § 4).

### 3.3 Les votes effectifs des juges croisés, mesurés sur témoins plantés — `fb3a2cc87251c`, « Votes effectifs du collège mesurés sur témoins plantés »

- **Fusionnées** : `f6f8c8b855234` et `fc37640a0181d` (même titre ; pondération gelée après étalonnage, puis épreuve sur juges réels) ; `fa38f9faa24e0` et `fefca0bd94064` (pondération par les erreurs sur témoins). Sur le même banc de juges scriptés, deux bras voisins : `fcfa3d98b90f8` (chaque carte rendue deux fois, vote instable compté comme abstention) et `fcbf4a2dd1a57` (alarme quand un juge change sous un nom inchangé).
- **Ce qu'elle changerait.** L'agrégation des juges, aujourd'hui fixée et comptant chaque juge pour un vote indépendant, lirait la corrélation de leurs erreurs sur les témoins plantés. Le nombre de votes effectifs serait rapporté à chaque course.
- **Épreuve, en deux étages.**
  - Étage 1, processeur seul : juges **scriptés** dont la corrélation des erreurs est plantée sur une grille (de 0 à 0,9). Oracle : écart entre votes effectifs estimés et vrais ; taux de témoins faux acceptés et de vrais rejetés, contre un seuil fixe, un juge seul et l'unanimité.
  - Étage 2, payant : les deux juges réels sur une centaine de témoins plantés, moitié pour l'étalonnage, moitié lue une fois ; témoin « un seul juge, k votes » à coût apparié.
  - Un « oui » : l'estimateur retrouve la corrélation plantée, et sur juges réels l'agrégation corrigée bat l'agrégation fixe et le juge seul répété. Le second juge achète alors quelque chose.
  - Un « non » : l'estimateur est trop bruité au nombre de témoins disponible, ou un juge répété vaut le collège. Résultat à porter tel quel : il dit ce que vaut le croisement des juges.
- **Coût.** Étage 1 : 0 USD d'appels. Étage 2 : environ 25 USD (cent témoins, deux juges à 0,10 USD la carte au total, le témoin répété, la marge de moitié).
- **Voisins à vérifier, non vérifiés** : « Nine Judges, Two Effective Votes » (556.0) ; « LLM Reviewers Err Together » (564.0) ; « AUDIT: Validating LLM Judges Through Controlled Error Injection » (558.0) ; « LLM-as-a-Judge Version Shift » (416.0).
- **Réserves.** Les juges scriptés plantent une loi d'erreur choisie par nous. La table par juge est un score de juge : son usage pour changer la composition relève de N-059, point 14, et de N-058. Je retire de la fusion la part de `fefca0bd94064` où les juges pondérés trient l'accès aux tests de mort : c'est un modèle qui décide de ce qui va à l'épreuve. Les juges ont marqué `f6f8c8b855234` et `fc37640a0181d` pour une citation obligatoire de N-073 sans « non vérifié » : défaut de forme, sans effet sur l'épreuve. Indice contraire à citer si l'on parle de juges de fournisseurs différents : Ferreira, Liu, Zheng (N-073, § 5). Lien avec le papier C (N-065, rôle 1) : la ligne mesure la tenue de juges honnêtes, pas leur corruptibilité sous attaque.

### 3.4 La réentrée tirée au sort des cartes éliminées de peu — `f856659046065`, « Réentrée tirée des cartes éliminées contre la famine »

- **Fusionnée** : `fc53dfee17677` (marge d'élimination calculée par rééchantillonnage du fichier brut, quota gelé, carte réentrant figée).
- **Ce qu'elle changerait.** Une carte éliminée sort aujourd'hui pour toujours. Un petit quota, tiré par programme parmi les éliminées de peu, repasserait le test de mort sur données fraîches ; chaque réépreuve compterait dans le budget d'erreur.
- **Épreuve.** Monde planté dont un tiers des lois vraies ont un effet faible, proche du seuil de puissance. Étage hors ligne à proposeurs **scriptés**, puis étage réel court. Bras : l'organisme actuel ; le même budget dépensé à relever la taille de tous les premiers tests ; une réentrée uniforme, sans égard à la marge ; le mécanisme.
  - Oracle : rappel final des lois vraies faibles ; rappel des lois fortes, qui ne doit pas baisser ; lois fausses promues sous le budget d'erreur ; et la marge sépare-t-elle, parmi les éliminées, les vraies des fausses mieux que le hasard.
  - Un « oui » : la réentrée récupère des lois faibles que la puissance uniforme relevée ne récupère pas, sans promouvoir plus de fausses. La règle d'oubli de la sélection change.
  - Un « non » : relever la puissance suffit, ou la marge ne trie rien (la réentrée uniforme fait aussi bien : on retire la stratification, pas le principe), ou les fausses promotions montent (mécanisme dangereux).
- **Coût.** Étage scripté : 0 USD d'appels. Étage réel : il suppose les tests de mort branchés sur le lanceur, ce qui ne l'est pas ; sur devis, au moins une course.
- **Voisins à vérifier, non vérifiés** : « Tail Starvation in Recursive Discovery: A Boundary for Validation and Re-entry » (551.0) ; « When Failure Banks Kill Good Ideas » (499.2). Les cartes disent elles-mêmes qu'elles en sont peut-être une reprise.
- **Réserves.** L'étage hors ligne tourne sur l'exécuteur simulé. La carte ne traite que l'élimination par faible puissance, pas par script défaillant. La réentrée ajoute des comparaisons : elle touche la ligne 3.1 et devrait être lue après elle.

### 3.5 La redite comptée par ce que les lois prédisent — `f89c771e3ac68`, « Dédupliquer les prédictions, pas leurs formulations »

- **Fusionnées** : `f6bb348e95955`, `fb6f958eb1bb6`, `f69c4a2a9c9e7`, `fd31770b6907d` (même idée, seuils réglés sur une moitié et lus sur l'autre) ; `f7b38afebd589` (variante par facettes syntaxiques, sans exécuter de loi).
- **Ce qu'elle changerait.** La mémoire anti-redite compare des mots. Pour les cartes qui engagent une loi exécutable, elle comparerait aussi les prédictions de cette loi sur des sondes fixées d'avance.
- **Épreuve.** Banque de paires plantées en quatre classes : même loi sous d'autres mots ; mots proches et lois différentes ; tout différent ; lois égales sur le domaine sous des formes différentes. Bras : les bardeaux actuels ; une base de normalisation syntaxique ; le mécanisme. Seuil réglé sur une moitié des lois, lu sur l'autre ; audit préalable que la présentation seule ne sépare pas les classes.
  - Oracle : erreur de détection par classe ; fusions à tort, dont une seule réfute la variante exacte.
  - Un « oui » : les bardeaux manquent les redites reformulées et le compteur par prédictions les prend. Le « zéro redite » de la v9 ne vaudrait alors pas ce qu'il dit (lecture descriptive, § 6, point 4).
  - Un « non » : les bardeaux ou la base syntaxique suffisent sur ce banc.
- **Coût.** Processeur seul. La mesure en course (économie d'appels de juges) est un second temps, sur devis.
- **Voisins à vérifier, non vérifiés** : « Mutation Without Variation » (401.0) ; « The Hitchhiker's Guide to Monoculture » (28.0) ; « StructSim » (419.0) ; « Multi-LLM Systems Exhibit Robust Semantic Collapse » (43.0).
- **Réserves.** Ne vaut que pour des cartes écrites dans une grammaire finie, ce que les cartes de l'organisme ne sont pas aujourd'hui : le premier travail est de dire quelle part des cartes réelles y entre. Deux lois égales sur les sondes peuvent différer ailleurs. Lien de biais seulement avec les questions ouvertes : elle sert le compte des essais de la ligne 3.1 et dit ce que le nul ne voit pas entre cartes sœurs d'une même génération.

## 4. Cartes écartées de justesse

- **L'héritage : archive servie, factice ou aucune** — `fed7a993d9671`, avec `fdfac3afd4bae`, `f0d21fb62aff2`, `f7a4918afe116`, `fc1f059e8873e`, `f7219bb36cfcb`, `f473bb6a03ca3`, `f760c773d6f15`, `f11193560f4d4`. Note 7. C'est la question de N-073, § 1, et les épreuves sont bien construites : dose de lois héritables plantée, avec une dose nulle qui invalide la lecture si un écart y apparaît (`fed7a993d9671`) ; mondes à dépendance plantée et sans dépendance (`fc1f059e8873e`) ; répondeur scripté qui ne survit que s'il lit le vrai retour (`f7219bb36cfcb`). Raison de l'écart : le coût. Trois ou quatre bras, plusieurs mondes et graines, de vrais proposeurs : entre 150 et 350 USD selon les espèces, au-dessus de la course v9. Trois réserves de fond s'ajoutent : les cartes servent la sélection des survivants, alors que le complément 3 de N-073 fixe l'objet comme un registre des tentatives, hérité puis tenu, comparé au même registre né vide et à aucun ; elles citent la lettre d'origine de N-073, § 1, que les compléments 1 à 3 ont remplacée ; servir des survivants sert un verdict agrégé, ce qui touche la garde « la mémoire ne sert jamais un verdict ». Le plan à trois bras attend déjà trois corrections avant tout préenregistrement (R-3643).
- **La banque d'échecs datée** — `f5373a31410ab`, avec `f1d7c5f2e47d7`, `f6caf922edbf1`, `fb9e8ae1b97b8`, `fa312929593cf`, `f20fbf8b6d797`. Note 7. Même raison : quatre à six générations, trois ou quatre bras. La porteuse plante de « faux échecs » (lois vraies tuées par un test sous-puissant) et mesure leur résurrection ; elle demande d'étendre ce que la mémoire sert au verdict du test de mort, ce qui est un nœud.
- **Le placebo de sélection et la tranche fraîche** — `f8c05bffe7cb1`. Note 8, hors des cinq par le coût. Trois régimes plantés (aucun signal, signal faible, corrélat parasite) : la sélection porte-t-elle un signal avant d'être servie.
- **L'interprète de référence face au script** — `fd81c25c080e8`, avec huit cartes sur la traduction d'une carte en code plus d'une fois. Note 8, sixième par le dernier recours du départage.
- **Le jumeau permuté aux tests de mort** — `f7782e931911d`, avec `fb484116eccc4`, `f11f00774547f`, `fb2a799e80c91`, `fe887ca5cb62c`. Note 8, septième. Processeur seul ; deux de ces cartes prennent « le meilleur de N » comme base, à réécrire comme pratique citée.
- **Les instruments transversaux, hors plancher par le seul critère C2** — le rejeu d'inertie (`f6e7646851ba5`, `fc36c3c3125ac` : un mécanisme ajouté change-t-il une seule décision, rejoué sans appel sur des journaux scellés) et la porte de version à témoins de modification plantés (`fd688912a8667`). Ils ne répondent à aucune des cinq questions ; ils disent comment adopter une carte une fois éprouvée. Voir l'écart 2.

## 5. Regroupements de la lecture descriptive fusionnés en une épreuve

- **Regroupements 9 (multiplicité) et la carte hors regroupement `f9a517d00f493`** : une épreuve, ligne 3.1.
- **Regroupement 11 (enrichir le nul), plus `f4250eb75fbba` (rangée au 9) et `f1c19731ccffb` (rangée au 10)** : une épreuve, ligne 3.2. La lecture descriptive les séparait par module ; l'oracle est le même.
- **Regroupement 3 (juges)** : un seul banc, ligne 3.3.
- **Regroupement 6, scindé** : la réentrée (ligne 3.4) se juge sans génération suivante, sur processeur ; la banque d'échecs servie aux proposeurs, non.
- **Regroupement 5 (héritage), plus `f7219bb36cfcb` (regroupement 2), `f473bb6a03ca3` et `f760c773d6f15` (regroupement 7), `f11193560f4d4` (isolée)** : une seule épreuve à bras multiples — archive vraie, archive factice d'un monde disjoint, verdicts permutés, dose d'appels sans archive, rien. Le regroupement 7, le plus large, n'apporte rien d'autre que ces deux bras : ses douze cartes déclenchent un vidage, et ce qu'elles mesurent au fond est ce que l'archive servie apporte.
- **Regroupements 1 et 2** : je ne les fusionne pas. Le premier éprouve la traduction de la carte en code, le second ce que le script lit dans les données ; mêmes mondes, bras différents. Ils pourraient partager un banc de scripts plantés.

## 6. Écarts aux critères, non corrigés

1. **La question de l'héritage reste hors des cinq.** Mes critères notent le coût sur le même pied que le lien avec les questions ouvertes, et la règle de couverture ne fait que plafonner. La question que le mandat nomme la première sort donc par le coût. Je ne change pas la règle ; je porte le point dans la décision.
2. **Le critère C2 ne voit pas les instruments transversaux.** Le rejeu d'inertie aurait 7 sans lui, et il se rejouerait presque gratuitement sur les journaux scellés de la v9. Il tombe par construction de mes cinq questions, pas par défaut de la carte.
3. **Réserves des juges.** Les critères prévoyaient de relire de près chaque carte marquée fausse sur un item. Je n'ai pas ouvert le coffre : je m'en suis tenu aux marques que la lecture descriptive nomme. Aucune porteuse n'y figure, sauf deux variantes de la ligne 3.3, pour un défaut de forme.
4. **C4 ne départage rien** : il vaut 1 pour toutes les lignes.
5. **Le coût n'est qu'un ordre de grandeur.** La v9 n'a joué ni tests de mort ni pari : aucun coût réel n'existe pour ces étages, et les tests de mort réels ne sont pas branchés sur le lanceur.

## 7. Décision pour Lazar

**Décision.** Quelles lignes de la course v9 passent à l'épreuve sur monde planté, et l'héritage en fait-il partie maintenant ?

**Enjeu.** Les cinq lignes en tête se jouent d'abord sur processeur seul, sans appel de modèle, et touchent ce que le programme dit ouvert sur le juge : la multiplicité entre cartes, ce que le nul laisse passer, ce que valent deux juges croisés, la règle d'oubli de la sélection. L'héritage, lui, demande de vrais proposeurs sur plusieurs bras : de 150 à 350 USD, et un plan qui attend encore trois corrections.

**Options.**
- **(a) Les cinq lignes, étage sur processeur d'abord, une à la fois.** Ordre proposé : l'effort de recherche dans le seuil, ce que le nul laisse passer, les votes effectifs des juges, la réentrée, la redite. Chaque étage payant ensuite sur son devis. Avantage : aucune dépense d'appels avant d'avoir un premier résultat par ligne ; quatre des cinq questions couvertes. Inconvénient : cinq préenregistrements à écrire et à contre-lire ; l'héritage attend.
- **(b) Les trois lignes du juge seulement** (effort de recherche, nul, votes effectifs). Avantage : charge moindre, et ce sont celles qui servent le second terrain du papier C et la mesure que N-067 dit à faire. Inconvénient : la sélection et la redite attendent ; rien sur l'héritage non plus.
- **(c) L'option (a), plus l'héritage préparé sans dépense** : corriger le plan à trois bras selon la lettre du complément 3 de N-073, en y versant les bons éléments des cartes (dose plantée avec dose nulle, mondes avec et sans dépendance, répondeur scripté), puis devis. Avantage : la question de N-073, § 1, avance sans attendre. Inconvénient : une sixième pièce délicate dans un chantier déjà chargé.

**Recommandation.** (a), confiance 0,7. Les quatre premières lignes sont solides ; la cinquième tient à un départage mince et peut céder sa place à l'interprète de référence ou au jumeau permuté sans que j'y voie d'objection. Si l'héritage compte plus pour toi que mon barème ne le pèse, (c) est le bon choix : mon écart 1 dit pourquoi le barème le sous-pèse.

**Défaut.** Aucun : c'est un nœud.
