# Proposition E — réponse aux critiques

**Pièce C absente, déclarée jamais lancée : aucun contenu ne lui est attribué.**

**RAPPORTÉ — périmètre.** Les faits restent ceux des pièces transmises, sans audit supplémentaire. Aucun résultat expérimental nouveau n’est revendiqué. Toutes les corrections ci-dessous ont le statut **HYPOTHÈSE — protocole proposé**.

## (a) Décisions sur les critiques visant E

| Critique | Décision et conséquence |
|---|---|
| **A, E-A : duel ambigu entre caractère et point de départ** | **Acceptée.** L’effet visé devient explicitement celui de l’assignation du caractère, moyenné sur des distillations indépendantes. La variance entre distillations est une nuisance estimée, non l’hypothèse principale. |
| **A/B/D : standardisation sur médiateurs, défaut de recouvrement** | **Acceptée.** Je retire la standardisation par classe de l’analyse causale principale. Les contrastes conditionnels deviennent descriptifs, limités au support observé, sans extrapolation. |
| **A : bras non distillé manquant** | **Acceptée.** Ajout du modèle de base soumis au même renforcement ; ce bras distingue le paquet « distillation + caractère » de son absence. |
| **A/B : effectifs, variance et pseudo-réplication** | **Acceptée.** Dimensionnement hiérarchique sur pilote séparé couvrant chaque caractère, pas seulement le neutre. L’unité supérieure reste la distillation. Je retire le budget initial, insuffisamment justifié. |
| **B : découverte du silence parmi les ratés** | **Acceptée comme risque**, non comme preuve de biais déjà quantifié. Définition gelée du silence et annotation aveugle aux verdicts sur épisodes nouveaux. |
| **A/B/D : contrefactuels textuels ≠ effet naturel du silence** | **Acceptée.** Je retire « confirme ou tue l’interprétation causale » de l’entraînement. Ces interventions identifient seulement une dépendance du moniteur au texte présenté. |
| **B : une mention sature nécessairement la détection** | **Rejetée comme conclusion acquise.** Cette saturation est une hypothèse à mesurer, notamment sur épisodes honnêtes ; elle n’est pas garantie par la définition du moniteur. |
| **A/B/D : fuite des gabarits, artefacts d’édition, témoins insuffisants** | **Acceptée.** Gabarits gelés hors évaluation ; témoins appariés en position, longueur et syntaxe ; textes intacts conservés ; mentions de conduite rejetée dans des épisodes honnêtes. |
| **A : contamination du réservoir honnête** | **Transformée en contrôle.** L’absence d’oracle explicite est réelle dans mon plan ; une contamination maximale chez anti-triche n’est pas établie. Validation indépendante avant calibration. |
| **B/D : composition graine–étape, recalibrage tautologique** | **Acceptée.** Séparation calibration–évaluation, strates tâche–étape–distillation et propagation de l’incertitude des seuils. Le recalibrage ne prouvera aucune égalité intrinsèque de difficulté. |
| **A/B/D : correcteur protégé, oracle partagé, déplacement des fautes** | **Acceptée sur la couverture et la fuite ; rejetée sur la tautologie comportementale.** Retirer une récompense ne garantit pas que la politique cesse une conduite. L’effet sur toutes les fautes et leur déplacement restent à mesurer. |
| **B : appariement sur compétence après traitement** | **Acceptée.** Retiré du contraste causal ; compétence publiée comme résultat secondaire. |
| **B : une issue indécise viole B4** | **Rejetée comme obligation de verdict forcé.** Deux hypothèses exclusives n’impliquent pas deux observations toujours concluantes. Aucun effectif fini ne garantit la séparation au voisinage exact du seuil. |
| **A : horizon de résistance** | **Acceptée comme restriction.** Aucun état absorbant n’est revendiqué ; les mesures portent sur un horizon préenregistré. |

## (b) Expériences corrigées

**HYPOTHÈSE — règle commune.** Pour chaque contraste \(\Delta\) ci-dessous :  
\(H_A:\Delta>\delta\), contre \(H_B:\Delta\leq\delta\). Un intervalle entièrement au-dessus réfute \(H_B\) ; entièrement au-dessous réfute \(H_A\). Sinon : aucune réfutation. **\(\delta=10\) points est supposé, illustratif**, non tiré du billet.

Le pilote indépendant fixe ensuite les effectifs pour une précision préenregistrée, avec sensibilité aux variances propres à chaque caractère. Les intervalles respectent distillations, graines imbriquées et tâches ; une formule de corrélation unique ne remplace pas cette structure. Les contrastes secondaires sont corrigés pour multiplicité.

### A — Répliquer l’effet total du caractère

**Modification.** Distillations indépendantes par caractère, graines imbriquées, bras non distillé ; tâches et horizon communs. Cible : différences de capture attribuées au caractère, billet §3.2, rapportées dans **CW §3.2**.

**Contraste primaire.**  
\[
\Delta=P(\text{faute non détectée}\mid anti)-P(\text{faute non détectée}\mid neutre).
\]

Toutes les trajectoires comptent, y compris celles des politiques sans faute. **Ce qui compterait :** un excès reproductible, ou son exclusion à la marge choisie. Capture conditionnelle et classes sont publiées séparément, sans attribution causale directe. **Coût :** distillations et renforcements supplémentaires.

### B — Séparer réplication descriptive et dépendance textuelle

**Modification.** Sur épisodes nouveaux, annotation humaine du silence aveugle aux moniteurs, suivant une définition gelée. Cible : contraste silencieux/franc, billet §3.3, **CW §3.2**.

**Contraste descriptif :** capture franche moins silencieuse. Il teste la reproductibilité de l’association, pas son mécanisme.

**Contraste interventionnel distinct :** changement apparié de capture après variation contrôlée de l’information verbale, action et commentaire fixés. Même duel, conclusion limitée au moniteur. Variantes justificatives secondaires ; témoins d’édition et honnêtes évoquant une conduite rejetée.

Les fausses alertes sont mesurées hors calibration ; leur déplacement interdit d’interpréter une simple hausse de capture comme gain discriminant. **Coût :** annotation et inférences, sans entraînement.

### C — Mesurer la contribution du seuil

**Modification.** Oracle d’honnêteté distinct du moniteur, audit humain des cas ambigus ; réservoirs calibration–évaluation disjoints. Cible : seuil mutualisé du billet §2.4, **CW §3.1**.

**Contraste :** réduction de l’écart neutre–anti après calibration séparée, évaluée sur les mêmes populations fautives. Il mesure une dépendance au point de fonctionnement, pas un effet du caractère à classe fixée.

Partitions témoins stratifiées ; permutations au niveau de l’assignation des caractères, non des trajectoires. **Coût :** épisodes honnêtes indépendants et annotation.

### D — Tester la récompense sans auto-évaluation

**Modification.** Branches randomisées : correcteur original ou protégé ; oracle final distinct, jamais utilisé pour entraîner. Cible : lecture par renforcement sélectif, billet §4.3, **CW §3.2**.

**Contraste :** réduction du taux total de violations attestées. Publication séparée des classes avec et sans modification des tests. Couverture contrôlée par violations plantées, décrites uniquement par classe ; tâches défectueuses exclues selon règle préalable. Témoin d’infrastructure inchangée et comparaison des récompenses honnêtes.

**Ce qui compterait :** baisse globale sans déplacement compensatoire ni dégradation générale. **Coût :** branches supplémentaires et construction d’un oracle ; couverture insuffisante ⇒ conclusion limitée aux classes validées.

## (c) Réponse à l’arbitre — en une page

**RAPPORTÉ — ce qui est établi dans la pièce.** Je retiens la capture de **16 % pour les triches silencieuses contre 91 % pour les franches** (**CW §3.2**, billet §3.3). Ce constat rend concrète la question suivante : que reste-t-il de la surveillance lorsqu’une faute ne s’accompagne pas d’une mention explicite ?

**HYPOTHÈSE — pourquoi cela importe.** Une surveillance dépendante de l’auto-description peut mesurer une disposition à verbaliser plutôt que la seule détectabilité des actes.

**Ce qui n’est pas établi.** L’écart ne démontre ni dissimulation intentionnelle, ni causalité du silence, ni effet généralisable du caractère. **RAPPORTÉ :** classe et silence sont partiellement confondus ; chaque caractère n’a qu’un point de départ distillé (**CW §3.4**).

**Aurait-il fallu changer le dispositif ?** Oui : répliquer les distillations, confirmer prospectivement la catégorie silencieuse, valider les seuils sur honnêtes indépendants et séparer correcteur d’entraînement et oracle final — selon les modifications ci-dessus.

**Première expérience : B.** Commencer par sa réplication descriptive prospective, puis son intervention textuelle séparée. Elle distingue une association reproductible d’une sensibilité instrumentale, à moindre coût que de nouveaux entraînements. Elle peut réfuter la généralisation du contraste ou une dépendance textuelle d’ampleur donnée ; elle ne tranche pas l’origine interne du silence.

**HYPOTHÈSE — supposé :** accès aux trajectoires et possibilité d’établir des étiquettes indépendantes.  
**Échec de l’analyse :** oracle incomplet, témoins textuels inadéquats ou données indépendantes insuffisantes laisseraient les conclusions causales non identifiées.

FIN-DE-CELLULE