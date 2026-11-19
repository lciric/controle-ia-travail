# Contre-lecture de la note de conception « Le juge et la sélection des cartes écartées (Astra, Carbon) » v1 — v1

- **Contre-lecteur** : modèle O, neuf, qui n'a pas écrit la note (règle R2). Écrit le 2026-11-19, vers 13:47Z (`date -u` : 2026-11-19T13:47:32Z). Processeur seul, aucune dépense, aucun appel de modèle.
- **Pièce contre-lue** : `note-conception-juge-selection-cartes-ecartees-v1.md`, sha256 `3b0332a144db9a042632ea0549d11a72f3acd406d8aa7ea98561b25f78c95b43`, égale à son compagnon `.sha256` (recalculée).
- **Lu sur `main`** (commit `d110a20e`), empreintes recalculées, toutes égales à celles que la note cite : `criteres-choix-cartes-v9-v1.md` `8881dbb2…` ; `proposition-cartes-a-eprouver-v9-v1.md` `a2cd45ad…` ; `contre-lecture-proposition-cartes-v9-v1.md` `a923cb57…` ; `especes-et-originalite-cartes-v9-v1.md` `2af9e67f…` ; `cartes-reexaminees-cout-non-limitant-v9-v1.md` `de7ed04d…` ; `lecture-course-v9-v1.md` `0306adf7…` ; `lecture-course-v9-v1-erratum-1.md` `9a771600…` ; sortie `…-verif-probabilites-v1-sortie.txt` `3cea377a…` ; décisions N-045 v2 `c7b05e39…`, N-053 `2204256d…`, N-058 `854f2724…`. Lus en plus, non cités par la note : `cartes-reexaminees-cout-non-limitant-v9-v1-erratum-1.md` `9326ffa2…` ; sortie `…-verif-citations-par-espece-v1-sortie.txt` `aaadd4c1…`. Registres : lignes GO-2026-11-19-55 à -65 de `registres/go.md`, R-3831 à R-3845 de `registres/decisions.md`. Sur la branche : `ordre-de-passage-epreuves-v9-v3.md` `b19f550b…` (égale à son compagnon).
- **Non lus** : aucune carte, aucun verdict de juge, le classement, le coffre. Les comptes ci-dessous viennent tous de pièces déjà versées.

## Constats

### 1. Majeur — la cause de l'écart d'Astra est réduite à « C2 et C3 », ce que les pièces ne portent pas

La note dit (§ 1, § 6 « Enjeu ») : les cartes d'Astra « sont tombées sur deux critères de la règle (questions déjà posées, coût) ». Les pièces montrent davantage :
- **L'interprète de référence** (`fd81c25c080e8`, 5 cartes d'Astra sur 9) passait le plancher à 8 (proposition, § 2, tableau) et n'a perdu la cinquième place qu'au dernier recours du départage, l'ordre alphabétique de l'identifiant (proposition, § 2). La contre-lecture `a923cb57…` (§ 2 et § 4) la note 9 à la lettre de la question (c), « règle de survie des fiches » : avec cette note, elle entrait dans les cinq.
- **Le portefeuille par couverture** (porteuse `fdcf828b0dc80`, d'Astra) passait à 8 et a été écarté au départage par C5 = 1 (proposition, § 2), non par C2 ni C3.
- **Les certificats de portée** (`f1675a6c453a9`, Astra) étaient au plancher (7 au barème de la proposition) et ont été « rangés sous le plancher sans un mot » (contre-lecture `a923cb57…`, majeure M9).
- Puis **GO-2026-11-19-56**, choix parmi les écartées de justesse, a pris la banque d'échecs, le placebo, le jumeau permuté et les instruments, et non l'interprète ni le portefeuille ; GO-2026-11-19-59 les a ajoutés ensuite.

Au moins 7 des 17 cartes d'Astra hors des neuf lignes étaient donc au plancher ou au-dessus ; elles sont sorties par le nombre visé de cinq lignes, par le départage (C5, ordre alphabétique), par deux erreurs de lecture relevées par la contre-lecture, puis par la sélection de GO-56. La raison « question neuve = 0 à C2 » ne vaut que pour les six cartes originales d'Astra « non nommées » (`2af9e67f…`, § c), et sur une seule lecture.

**Correction.** § 1, première phrase, à remplacer par : « Les cartes d'Astra et de Carbon n'ont pas été écartées par un juge : elles l'ont été par l'application de la règle de choix (plancher, nombre visé de cinq lignes, départage), écrite avant l'ouverture et appliquée sans le champ de l'espèce — avec deux erreurs de lecture relevées par la contre-lecture sur des lignes portées par Astra —, puis par le choix de GO-2026-11-19-56 parmi les écartées de justesse. Le critère C2 à zéro n'explique que six cartes d'Astra, sur une seule lecture ; le coût explique surtout Carbon. » Même reprise au § 6, « Enjeu », et une ligne au tableau du § 2 pour `a923cb57…` (majeure M9, note 9 de l'interprète). Conséquence pour la voie (iii) : l'erreur de lecture est un mode d'échec démontré, ce qui renforce l'exigence de deux lecteurs et des désaccords rapportés. R-3845 porte la même simplification (« question neuve notée zéro, coût ») : à signaler à la mère.

### 2. Majeur — « les neuf premières lignes » est faux

Tableau du § 2, ligne `2af9e67f…` (et le rapport du rédacteur) : « part des cartes dans les neuf premières lignes retenues ». La pièce dit « les neuf lignes retenues (cinq de GO-55, quatre de GO-56) ». Ce ne sont pas les neuf premières par la note : les rangs 6 (interprète) et 8 (portefeuille par couverture), tous deux portés par Astra, n'y sont pas ; la banque d'échecs (7) et les instruments (hors plancher) y sont. **Correction** : « dans les neuf lignes retenues par GO-2026-11-19-55 et -56 ».

### 3. Majeur — Carbon : « c'est le coût qui les tenait dehors » est plus net que les pièces

`de7ed04d…` ne le dit pas en toutes lettres pour la ligne 2.1 (il le dit, en sens inverse, pour 2.2 et 2.3). La proposition (§ 5) jugeait que le regroupement 7, où sont les quatre cartes de Carbon, « n'apporte rien d'autre » que deux bras à l'épreuve de l'héritage : ces cartes sont tombées avec l'héritage, sorti par le coût (C3 = 0), mais aussi sous trois réserves de fond (§ 4 : on sert des survivants alors que le complément 3 de N-073 fixe un registre des tentatives ; lettre d'origine de N-073 ; verdict agrégé servi). `de7ed04d…` reprend ce nœud, et son erratum 1 (`9326ffa2…`, R-3837), non cité par la note, compte le critère « battre le meilleur de N tirages » dans les sept cartes de la ligne, porteuse comprise : réserve voisine de l'exclusion X2. La cinquième, `f7cc0003c4b2c`, est une porte sur les modifications, donc un instrument que C2 ne voit pas par construction (proposition, écart 2), et le juge Opus l'a marquée pour le même critère (lecture descriptive, § 4, « Ce que les juges ont marqué »).

**Correction** (tableau du § 2, ligne `de7ed04d…`) : « quatre des cinq cartes de Carbon alors non gardées étaient rattachées par la proposition à l'épreuve de l'héritage, sortie par le coût, avec deux réserves de fond (objet servi : survivants contre registre des tentatives ; critère du meilleur de N dans les sept cartes, erratum `9326ffa2…`) ; la cinquième, une porte de modification, tombait comme instrument par C2 (écart 2) ». Dire d'où vient l'espèce de ces identifiants (lecture descriptive, § 4, identifiants vérifiés par le programme de l'erratum, sortie `d9360b31…`).

### 4. Moyen — la matrice est exacte, mais sa source et la faisabilité de la mesure 1 sont à préciser

Vérifié à l'unité sur `3cea377a…` : juge Opus 12, 20, 13, 11, 11 ; juge Argon 19, 20, 16, 13, 15. Mais :
- les comptes « sans marque de citation : 33 notables sur 39 ; avec : 34 sur 55 » viennent de la sortie `aaadd4c1…` (marques par espèce), non de `3cea377a…` : citer les deux ;
- la mesure 1 ne peut pas se faire « sur les champs des verdicts » seuls : la marque de citation se calcule par motifs sur le texte des cartes (programme `50ad93a5…`). Écrire « champs des verdicts et motifs de citation des cartes, par programme, sans lecture par un agent » ;
- **règle R1** : une part de la réponse est déjà calculable sur les pièces versées. Les 39 cartes sans citation comptent les 20 d'Astra, toutes notables ; les 19 autres en ont 13 (33 − 20). La seule strate où Astra existe donne donc déjà le même signe : « confondue » doit devenir « en partie confondue ». Le préenregistrement de la mesure 1 doit déclarer ce qui est déjà connu et ne compter comme épreuve que le reste (par item, par juge). Il doit aussi dire que les cases sont presque vides (Astra : aucune carte avec citation ; Argon : une seule sans citation) et la puissance que cela laisse.

### 5. Majeur — la lecture qui départage le collège oublie le coût et le témoin à coût apparié

§ 4, « Lecture qui départage » : le collège gagne « s'il a plus de votes effectifs que deux juges ». Ajouter des juges donne presque toujours un peu plus de votes effectifs. N-058 (point 1) juge toute composition sur l'oracle **et le coût mesuré**. N-045 (point 4) impose le témoin « un modèle, vote à k, coût apparié », que la ligne 3.3 de la proposition prévoit déjà (« un seul juge, k votes »). **Correction** : le collège ne gagne une place que s'il bat, à coût apparié, un juge seul répété k fois et le collège à deux juges sur les témoins plantés (faux acceptés, vrais rejetés), avec son coût rapporté par carte.

### 6. Moyen — l'ouverture de la voie (ii) est asymétrique et contredit le § 3

§ 4 : « La voie (ii) ne s'ouvre que si la mesure 4 montre une interaction défavorable à Astra ». Or le § 3 dit que même alors le remède serait la récusation ou l'étalonnage, non le surpoids. Et viser une seule espèce et un seul sens va contre les règles R3 et R4. **Correction** : « Toute interaction juge × lignée, dans les deux sens et pour chaque lignée (le juge Argon passe 19 de ses 21 cartes), lue sous contrôle de multiplicité (cinq juges × cinq lignées), appelle la récusation ou l'étalonnage du juge en cause ; la voie (ii), comme surpoids, reste fermée. »

### 7. Moyen — deux renvois débordent la lettre des décisions

- Voie (ii) : « un juge Astra sur des cartes d'Astra est le cas que N-053 veut éviter ». N-053 dit, au point 4, « juge d'une autre lignée » pour les lectures du programme de contrôle, et au point 5 l'invariant « aucun score de moniteur dans la sélection de l'agent ». Aucun ne parle d'un juge face aux cartes de sa lignée. Écrire « contraire à l'esprit de N-053, point 4, sans en être la lettre ».
- Garde commune et voie (ii) : N-058 fixe la composition **des proposeurs** ; l'étendre à celle des juges passe par N-059, point 14 (la table par juge est un score de juge), que citent la proposition (§ 3.3) et l'ordre de passage (rang 3). Le citer, ou dire « par extension ».

### 8. Moyen — N-045 et GO-2026-11-19-60 ne sont pas tenus en toutes lettres

La note lit N-045 v2 mais ne la cite nulle part dans le corps. À écrire au § 3 :
- point 1 : un juge de lignée Astra ou Carbon est un choix de « modèle par rôle », variable à juger sur l'oracle et le coût (rejoint le constat 5) ;
- point 4 : les mesures 1 à 3 avant la 4, ce que fait déjà l'ordre du § 4 ;
- point 2 : il porte sur le signal rendu à l'organisme et ne touche pas la règle de sélection de la mère.

La voie (iii), « le coût n'entre plus dans la note », va au-delà de GO-60, qui ne retire le coût que pour une carte dont l'amélioration est considérable. C'est un changement à demander à Lazar en toutes lettres dans l'option (a). Il faut dire aussi que le coût reste dans l'ordre de passage : amélioration attendue d'abord (GO-60), puis bon marché d'abord (N-045).

### 9. Moyen — mesure 2 : « gratuit » et « lignées différentes » ne vont pas ensemble

Seuls les lecteurs des lignées Opus et Fable sont sans dépense, et la note les dit elle-même de la même famille (§ 3, voie i). Un lecteur d'Argon, d'Astra ou de Carbon est un appel payant : il faut un devis et une ligne de GO. **Correction** : « deux lecteurs neufs, l'un Opus, l'autre Fable (même famille, déclaré), sans dépense ; un troisième d'une autre famille, sur devis ». Il faut déclarer aussi le masque d'espèce imparfait (`2af9e67f…`, limite 2). La même remarque vaut pour les défenses de la voie (iv) dans la mesure 3.

### 10. Moyen — mesure 3 : la règle (iii) n'est pas éprouvée hors échantillon

La règle (iii) est conçue après avoir vu quelles cartes de la v9 sont tombées, et pour faire entrer celles-là. Sa « validation après coup » sur la même course n'est pas une épreuve tenue à l'écart. **Correction** : le dire en limite. L'épreuve décisive est la course suivante, avec la règle scellée avant l'ouverture de ses cartes. La mesure 3 reste descriptive pour la v9.

### 11. Mineur — en-tête et état présent

- GO-2026-11-19-65 et R-3845 sont maintenant sur `main` (commit `d110a20e`) : remplacer « je ne les ai pas trouvés » par leur lecture.
- « État présent » : citer GO-2026-11-19-59, qui a ajouté l'essentiel des lignes d'Astra avant GO-61.
- Verdict, ligne 1 : « appliquée sans l'espèce » doit devenir « sans le champ de l'espèce ; masque imparfait, le style d'Astra se reconnaît (`2af9e67f…`, limite 2) ».
- Voie (i) : la récusation par lignée se fait par programme ; le juge reste aveugle à l'espèce (N-058, point 1).

### 12. Mineur — dire à Lazar ce que (a) donne au juge

Lazar demande que « le juge puisse sélectionner » (GO-65). Sous (a), un juge peut **proposer** une carte par le droit de défense, mais il ne sélectionne pas. Le dire en une phrase dans l'option (a), pour que l'écart à la demande soit visible.

### Ce qui tient

- Aucun biais d'un juge contre Astra n'est mesuré, et le seul compte disponible va en sens inverse : exact.
- Aucun juge de lignée Astra ou Carbon en v9 : exact (lecture descriptive ; erratum, point 4).
- Il est exact que « notable » mesure en bonne part l'absence de citation (erratum, point 5), avec la nuance du constat 4.
- Les voies comparées respectent l'exclusion « un modèle décide » et GO-63 : le juge ou le collège propose, l'avis pondéré reste descriptif, rien n'est trié à l'intérieur de l'organisme.
- Mesures ordonnées, gratuites d'abord ; ordres de grandeur de coût cohérents avec les pièces (25 dollars pour deux juges, 9,27 dollars réels de juges).
- Aucune revendication neuve, aucun seuil, aucun devis.
- Fiche de décision au format : décision en une phrase, enjeu, trois options avec avantage et inconvénient, recommandation et confiance, défaut sous 48 heures limité à la part sans dépense, sans changer la règle en vigueur. Aucun identifiant de modèle, aucun sigle non développé.

## Verdict

Scellable après corrections.

Le dessein tient : changer la règle plutôt que les juges, mesurer le collège avant de lui confier quoi que ce soit, ne pas ajouter de poids à une lignée. La recommandation (a) n'est pas touchée. Il faut en revanche corriger avant de sceller les faits qui la fondent :
- l'écart d'Astra (constats 1 et 2) : la cause n'est pas seulement C2 et C3, mais le départage, des erreurs de lecture et GO-56 ;
- l'écart de Carbon (constat 3) ;
- la lecture qui départage le collège (constat 5 : coût et témoin à coût apparié) ;
- les conditions de gratuité de la mesure 2 (constat 9).
Les autres constats sont des précisions à porter dans la même version.
