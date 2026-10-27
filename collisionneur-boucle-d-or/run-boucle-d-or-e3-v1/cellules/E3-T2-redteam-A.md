# Proposition A — Tour III.2 : équipe rouge croisée contre B et C

**Pièces.** B et C sont présentes et complètes à la lecture. Comme eux, je note que les résultats du plan P et la pièce de Gemini (`2784138…`) sont absents : je n'en dis rien. Tout ce qui vient des pièces est **RAPPORTÉ** ; mes calculs à partir des v(s) de P sont **illustratifs** ; mes conjectures sont **HYPOTHÈSE**. Je ne confirme ni n'infirme de mémoire les références que B et C citent : elles restent « référence à vérifier ».

**Ce que je reprends, en le disant.** De B, le point a7 (sous 0,5 de probabilité de promotion, maximiser l'entropie revient au tri glouton) : je m'en sers contre C. De B et de C ensemble, le constat identique du désalignement de la grille de P (cases de 0,1 à cheval sur [0,12 ; 0,26], taux de case 0,41 et 0,32, illustratif) : deux lectures indépendantes convergent, je le tiens pour solide et j'en tire une conséquence que ni l'un ni l'autre ne tire (section C-c).

---

## Contre la proposition B

### (a) Failles

**B1. E0 a une issue H_A inatteignable par construction.** B déclare H_A « si la borne supérieure de Clopper-Pearson à 95 % est < α pour toutes les formes ». Pour un juge de niveau exactement α, le taux vrai de promotion d'une forme nulle vaut ≈ α ; la borne supérieure d'un intervalle à 95 % ne descend sous α qu'avec une probabilité d'environ 2,5 % par forme (illustratif). La règle « sinon on augmente le nombre de mondes » boucle sans fin : E0 ne peut conclure H_A que si le juge est conservateur, c'est-à-dire sous-puissant. Il faut une marge d'équivalence (α + ε, ε fixé d'avance, comme le fait C avec 0,065) ou un test unilatéral de « > α ». Tel qu'écrit, E0 ne vérifie pas le juge : il vérifie que le juge est frileux.

**B2. E0 valide le juge contre une liste figée.** Les sept formes sont celles de R1 plus « parent + loi aveugle ». Un juge qui passe E0 est validé contre ces sept scripts, pas contre un adversaire qui connaît la liste. B ne prévoit pas de forme « paramétrée pour passer la marge » (enveloppe + perturbation de 2δ₀ + ε sur une sous-population) ; c'est le trou que R1 nomme déjà (« battre l'enveloppe de 2δ₀ ») et il n'est pas scripté.

**B3. E1 : le vainqueur annoncé est vrai par construction.** Le bras « Thompson à a priori de fenêtre, a + b = 2 » est un Thompson presque plat : il ne peut perdre contre le Thompson pur que par le poids de deux pseudo-tirages. La propriété « ne perd jamais plus de δ » est donc assurée d'avance ; seule la force a + b = 10 est un vrai pari. B présente les deux forces comme un seul bras et conclut que l'a priori faible « domine les deux extrêmes » : il domine parce qu'il *est* l'un des extrêmes.

**B4. E1 : l'« oracle de case » n'est pas un plafond.** Quand le centre c de la cloche est tiré au hasard sur [0,1 ; 0,7], une cloche de largeur 0,07 tombe presque toujours à cheval sur deux cases de 0,1 : l'oracle de case plafonne sous la fenêtre quand c ∈ [0,12 ; 0,26] par le même artefact que B dénonce en b0.3. L'écart « fenêtre − oracle de case » mesure alors la grille, pas l'a priori. Il faut un oracle **continu** (qui connaît v(s)) ; R2 avait un plafond de ce genre (0,750), B l'exige pour P (b0.6) et ne se l'applique pas.

**B5. E3 : la distance (ii) est colinéaire avec le score qu'elle est censée corriger.** « Cosinus des vecteurs de contexte de cooccurrence » et RA sont deux fonctions du même voisinage d'avant. Régresser l'issue sur « RA lissé en 20 strates + β₁d + β₂d² » laisse à d² tout ce que le lissage de RA n'a pas capté : un β₂ < 0 peut n'être que la courbure résiduelle de RA. La définition (i) (profils de champ) évite ce confondant mais a un autre défaut : six champs, termes « spécifiques » par construction (T : fréquence concentrée dans un champ), donc profils quasi orthogonaux et distance presque constante sur les paires inter-champs ; les déciles de d seront des déciles de bruit (HYPOTHÈSE, à mesurer avant tout usage : variance de d et corrélation de rang avec RA, chiffres à rapporter d'avance).

**B6. E3 : « sommet intérieur » est presque automatique pour une quadratique.** Dès que β₂ < 0, le sommet −β₁/2β₂ est intérieur sauf si |β₁| est grand ; un plateau haut aux deux bords (monde « bords » de P) donne β₂ > 0, mais un monde « croissant puis plat » donne β₂ < 0 et un sommet intérieur sans cloche. La forme quadratique encode la réponse. Il faut une forme libre (strates de d, comme C le fait par déciles) et la quadratique seulement comme résumé.

**B7. E4 : la variable (4) fuit vers le juge.** B écrit « sur les 50 tirages de calibrage seulement, donc pas de fuite vers le juge ». Mais P dit que le juge v1 utilise « 50 tirages de calibrage et 200 tirages frais » : les 50 servent au juge. Sélectionner les filles sur un score calculé sur les tirages qui calibrent le juge, c'est sélectionner les filles pour lesquelles la calibration sera favorable. Le niveau α du juge n'est plus garanti après sélection. Même faille chez C (Δ_syn sur n₀ = 15 « pris sur les 50 de calibrage ») : les deux propositions la partagent.

**B8. E4 : lieu de test biaisé.** Mesurer l'aire sous la courbe de s « sur les archives des générations » suppose que les filles testées sont un échantillon représentatif. Elles ont été choisies par un allocateur ; si cet allocateur a utilisé s, l'aire de s est biaisée par la sélection. Il faut un lot de filles testées par tirage uniforme, réservé à E4, et le dire d'avance.

**B9. Question 5 : l'asymétrie est conditionnelle au budget.** « La seconde perte est bornée » suppose que l'apprentissage converge en 40 tests ; P lui-même liste « Thompson pas meilleur que le hasard » comme mode d'échec. Si l'apprentissage ne converge pas à ce budget, le regret de l'allocateur appris se répète à chaque génération et n'est borné que par le nombre de générations.

### (b) Scénarios d'évasion

Adversaire : un agent qui rédige les fiches filles (et, au pire, l'expérimentateur de C). Coût compté en appels de modèle et en tirages.

- **Contre E0 (juge)** : après E0, la liste des sept formes est connue. L'adversaire soumet une « enveloppe + loi neuve sur une sous-population de masse ε », réglée pour dépasser la marge 2δ₀ de justesse : forme hors liste, coût d'un appel pour l'écrire, aucun tirage. E0 ne la voit pas.
- **Contre l'allocateur récompensé par la promotion (Thompson de P, et E2)** : si le trou « parent + loi aveugle » n'est pas fermé, l'adversaire fabrique des filles de probabilité de promotion ≈ 0,5 (il la règle par la masse de la loi aveugle). L'allocateur entropique s'y jette ; le Thompson récompensé par la promotion aussi. Coût : nul par fille. B le reconnaît en a1 ; il ne chiffre pas la contre-mesure.
- **Contre E4** : les quatre variables sont calculées sur des champs que l'adversaire écrit. (1) « domaines » et (2) « opérateurs » sont du texte : il place s et le Jaccard où il veut (R1 : « jargons rares fabriqués »). (3) la divergence de Jensen-Shannon entre lois parentes se manipule en déclarant pour un parent une loi uniforme sur la moitié des traits. (4) la synergie sur 50 tirages se sur-ajuste si l'adversaire voit les tirages (C ne l'interdit pas ; B non plus). Coût : zéro tirage, un appel.
- **Tous à la fois** : une fille « parent A + loi aveugle » déclarée dans la bande de s, à opérateurs rares partagés, à loi parentale déclarée orthogonale, sur-ajustée sur les 50 tirages de calibrage. Elle passe la fenêtre, le tri par variables, la synergie, et le juge par le trou. Coût total : un appel de modèle et la lecture de 50 tirages. Seul le juge **sans trou**, sur **200 tirages non vus**, l'arrête ; aucun instrument de B n'en dépend autrement.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E0** : une forme « adaptative » tirée au hasard dans une famille paramétrée (masse ε de la loi aveugle, amplitude de la perturbation), et non une liste fixe ; sans elle, E0 valide une liste, pas un juge.
2. **E0** : un essai de garde comme celui de T (« calculateur volontairement fuyant pris par la garde ») : un juge auquel on fait voir les 200 tirages frais doit être pris ; sinon on ne sait pas si « frais » est vérifié mécaniquement.
3. **E1** : la même batterie à budget 80 et 160 ; si l'a priori fixe gagne encore à 160, l'explication « apprentissage trop lent » est réfutée et il faut chercher un artefact.
4. **E3** : permutation de d **à score RA constant** (mélange de d dans chaque strate de RA) ; β₂ doit être nul. La permutation des issues de T détruit toute relation : trivialement nulle, elle ne contrôle pas le confondant B5.
5. **E3** : corrélation de rang entre d et RA rapportée **avant** la régression, avec un seuil préenregistré au-delà duquel la définition (ii) est abandonnée.
6. **E4** : s calculée avec deux représentations (TF-IDF et fréquences brutes, R2) ; si le classement des filles change (Spearman sous un seuil fixé), la variable n'est pas une variable.
7. **E4** : un lot de filles testées par tirage uniforme, indépendant de l'allocateur.

---

## Contre la proposition C

### (a) Failles

**C1. Statuts faux (règle 1).** C étiquette **RAPPORTÉ (littérature)** trois souvenirs d'articles (Wang et collègues 2017 ; Bromham et collègues 2016 ; Leahey et collègues 2017) non servis dans les faits et non vérifiés sur PDF. Ce sont des **HYPOTHÈSE (souvenir)**, comme B les étiquette. De même, « juge v1 : OBSERVÉ-NON-AUDITÉ dans son principe » : aucune pièce ne rapporte une exécution du juge ; c'est une propriété de conception, RAPPORTÉE par A et P. Je ne me prononce pas sur l'exactitude des références : référence à vérifier.

**C2. H_B de l'Expérience 2 est présentée comme déjà prouvée par T.** C écrit que RA « prouve que ce sont les paires ayant le plus fort couplage structurel local qui forment des ponts réalisés, et non une bande médiane de distance ». T ne mesure aucune distance et dit lui-même que l'issue est la cooccurrence lexicale future. Que RA soit croissante en son propre score n'établit rien sur une variable qu'il ne contient pas. C surinterprète RAPPORTÉ en résultat ; H_B est une HYPOTHÈSE, sinon l'Expérience 2 n'est pas un duel.

**C3. Expérience 2 : la variable s est, dans l'une de ses deux définitions, une fonction du graphe que RA résume.** « Vecteur de voisins normalisé sur le vocabulaire d'avant » : le cosinus de deux vecteurs de voisins est une proximité de second ordre, comme RA, AA et CN. Restreindre RA aux déciles bas de s retire mécaniquement la tête de RA (forte proximité de second ordre). H_A perd alors **par construction**, et C ne distingue pas « la fenêtre est fausse » de « s et RA sont la même variable ». Le choix entre « profil de sous-catégories » et « vecteur de voisins » est laissé ouvert (« ou ») : un degré de liberté qui décide de l'issue. Même attaque que B5, aggravée : B nomme une primaire, C non.

**C4. Expérience 2 : seuil absolu importé contre l'avis de sa source.** C reprend « +2,0 points, seuil D2 de T ». T consacre un paragraphe à dire qu'un seuil absolu bascule avec le taux de base (9,61 réfuté, 13,13 retenu, même ordre). C ignore la réserve de la pièce qu'il cite ; B l'a lue. Avec un taux de base de 0,28 %, « +2,0 points » sur RA_fenêtre dépend surtout de la part des 10 000 que la restriction retire.

**C5. Expérience 1 : la « cloche à cœur riche » ne teste l'entropie que si la puissance du juge est élevée.** C raisonne sur v(s) = 0,85 au cœur et 0,50 aux flancs, et conclut que l'allocateur entropique « fuit le pic ». Mais l'allocateur de P apprend la **probabilité de promotion**, qui vaut v × puissance du juge. Avec des forces tirées sur [0,3 ; 1,5] et 200 tirages, la puissance moyenne n'est pas rapportée ; si elle est sous 0,6 (HYPOTHÈSE), les probabilités de promotion restent sous 0,5 partout et, par le point a7 de B, l'entropie équivaut au glouton : la fenêtre ne fuit rien, H_B « perd » sans que l'entropie ait été testée. C ne chiffre pas la puissance ; c'est la variable confondante de toute l'expérience 1.

**C6. Expérience 1 : TQ est mal spécifié dans les mondes de P.** C affirme que la famille logit quadratique « contient exactement » les cinq mondes. Les mondes de P sont des indicatrices à bords nets (0,5 / 0,05) ; un logit quadratique n'en est qu'une approximation lisse, et le monde « bords » (< 0,06 ou > 0,6, asymétrique sur le rang) demande θ₁ ≠ 0 et θ₂ > 0 avec un minimum déplacé. TQ peut perdre par mal-spécification, et C lira « H_A non falsifiée ». Il manque un bras de contrôle : TQ **avec les vrais θ donnés** (oracle de forme), pour séparer « apprend mal » de « forme fausse ».

**C7. Expérience 3 : les variables de synergie sont vraies par construction dans le simulateur de P.** Les mondes de P n'ont ni opérateurs ni résidus : RA_op et ρ_res devront être **construits**. Or la vérité d'une fille, dans P, est définie par « parent A sur la sous-population 0, loi neuve sur la 1 » : c'est exactement la structure que ρ_res détecte (résidus complémentaires par sous-population). Bras 2 gagne « dans tous les mondes » parce que le monde définit la vérité par la variable du bras 2. C reproche à Gemini une simulation construite pour passer ; l'Expérience 3 l'est aussi.

**C8. Expérience 3 : fuite de calibrage (comme B7).** n₀ = 15 « pris sur les 50 de calibrage » : la sélection sur Δ_syn biaise les tirages qui calibrent le juge. Le contrôle « monde purement nul » de C attraperait une inflation moyenne de α, mais pas une inflation conditionnelle à la sélection si la calibration est par fille.

**C9. Expérience 3 : règle de falsification asymétrique (B4).** H_A tombe si Bras 2 gagne dans 4 mondes sur 5 ; H_B tombe seulement si Bras 2 perd dans « cloche ». Issue « gagne dans 4, perd dans cloche » : les deux tombent. Issue « gagne dans 3, cloche indistincte » : aucune. Ce n'est pas un duel exclusif.

**C10. Fermer le trou par « battre chaque parent sur chaque sous-population déclarée ou induite ».** Multiplicité : k sous-populations, k tests ; sans correction, α croît. Et « induite par l'arbre de partition » laisse l'adversaire choisir la partition.

### (b) Scénarios d'évasion

- **Contre RA_op** : opérateurs déclarés rares et partagés (R1 : « jargons rares fabriqués ») ; RA_op = Σ 1/freq(o) est maximal pour un opérateur inventé, partagé par deux fiches, de fréquence 2. Coût : un mot.
- **Contre |ρ_res|** : déclarer pour un parent une loi quasi uniforme sur la moitié des traits : résidus orthogonaux par déclaration. Coût : nul.
- **Contre Δ_syn à n₀ = 15** : même sans voir les tirages, soumettre K copies renommées d'une fausse fille ; sur 15 tirages, la variance de Δ_syn est grande (illustratif : écart-type de l'ordre de 0,1 en log-vraisemblance moyenne pour des lois raisonnables), le seuil δ₀ = 0,01 est franchi par une part notable des copies ; le second étage reçoit les 32 « gagnantes » du bruit (malédiction du vainqueur). Le juge frais les arrête, mais le budget frais est consommé : 32 tests perdus par génération. Coût : K appels. Avec accès aux tirages : sur-ajustement, coût nul.
- **Contre TQ** : l'adversaire contrôle s (texte « domaines »). Il sculpte la courbe que TQ apprend et y place ses tricheuses calibrées sur le trou ; avec le « prieur transmis d'une génération à l'autre avec oubli contrôlé », il empoisonne lentement le prieur. Coût : nul par fiche, étalé sur quelques générations.
- **Contre la fermeture du trou par sous-populations** : déclarer de nombreuses sous-populations fines ; la multiplicité fait le reste.
- **Tous à la fois** : fille « parent A + loi aveugle », opérateur rare fabriqué, parent B déclaré uniforme sur la moitié des traits, soumise en K copies. Elle passe RA_op > 0, ρ_res ≈ 0, Δ_syn (par loterie), TQ (par s déclaré), et le juge par le trou. Coût : K appels, aucun tirage. Les trois étages de C ne coûtent rien à l'adversaire parce qu'ils lisent des champs qu'il écrit ; seul le juge sur tirages non vus coûte quelque chose, et il a un trou.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Expérience 2** : corrélation de rang entre s et RA rapportée **avant** le découpage en déciles, seuil fixé d'avance ; au-delà, abandon de la définition « voisins » pour « sous-catégories ». Et permutation de s à RA constant (comme B-c.4).
2. **Expérience 2** : essai d'absence de fuite temporelle **pour s**, à l'identique de T (documents d'après modifiés → s inchangé au bit près).
3. **Expérience 1** : puissance du juge mesurée par tranche de force, rapportée avant l'allocation ; un monde « cœur riche » où elle est > 0,8 (force ≥ 1,0) et un où elle est < 0,5 ; sans cela, « l'entropie fuit le pic » n'est pas départagé de « l'entropie égale le glouton ».
4. **Expérience 1** : bras « fenêtre glouton » (même bande, choix par espérance) à côté de « fenêtre entropie », pour isoler l'effet de l'entropie de l'effet de la bande ; et TQ-oracle (θ vrais donnés), plafond continu.
5. **Expérience 1**, et c'est la conséquence commune à B et C que ni l'un ni l'autre ne tire : un bras Thompson **à grille alignée** sur [0,12 ; 0,26] (cases 0–0,12, 0,12–0,26, 0,26–0,8). Duel : H_A « la fenêtre bat Thompson aligné dans cloche » (l'avantage est la bande fixe) contre H_B « indistincts » (l'avantage de P n'était que la grille). Chaque issue falsifie l'une des deux lectures de b0.3.
6. **Expérience 3** : un monde où les filles vraies n'ont **pas** la structure « A sur 0, neuve sur 1 » (interaction diffuse sur tous les traits, HYPOTHÈSE de forme à préenregistrer) ; si Bras 2 y perd son avantage, C7 est confirmé.
7. **Expérience 3** : bras « 32 tests complets au hasard, sans criblage » ; sans lui, « Bras 2 bat Bras 1 » peut n'être que l'effet de tester 32 filles hors fenêtre dans un monde où la fenêtre est fausse.
8. **Expérience 3** : K copies renommées d'une fausse fille soumises au criblage ; taux de passage au second étage rapporté ; c'est la mesure directe de la malédiction du vainqueur.
9. **Juge (table d, ligne 1)** : niveau α mesuré **après** sélection sur les tirages de calibrage, pas seulement en monde nul sans sélection.

---

## Ce qui, chez B et C, me réfuterait

Si le contrôle 5 ci-dessus donne « indistincts », ma lecture (comme celle de B et C) de b0.3 est confirmée et le monde « cloche » de P ne mesure que la grille. Si la puissance du juge dépasse 0,8 dans « cœur riche » **et** que la fenêtre entropique y bat le glouton, C5 est réfuté et l'entropie a un contenu que je lui refuse. Si la corrélation de rang entre s « voisins » et RA est sous le seuil, C3 et B5 tombent et l'Expérience 2 redevient un duel.

FIN-DE-CELLULE