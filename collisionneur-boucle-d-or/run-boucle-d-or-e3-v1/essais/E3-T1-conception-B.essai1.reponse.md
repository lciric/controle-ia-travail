# Proposition B — « Boucle d'or » : ce que la question suppose, et des duels qui peuvent échouer

**Pièces.** A, P, R1, R2, T et C sont présentes et complètes à la lecture. Deux éléments manquent :
- la réponse de Gemini et son script (`2784138…`) ne sont pas versés. Je n'en dis rien au-delà de ce qu'en rapporte la pièce A ;
- les propositions A et C de ce tour ne me sont pas visibles, puisque le tour est à l'aveugle. Je n'ai donc rien à attaquer ni à reprendre chez elles.

Dans ce qui suit, « pièce A » désigne le fait servi, jamais la proposition A.

**Statuts.** Tout ce qui vient des pièces est **RAPPORTÉ**. Les chiffres d'Uzzi et collègues que donne la pièce A sont **RAPPORTÉ, lus par transcription, non vérifiés sur PDF empreinté**. Mes souvenirs de littérature sont **HYPOTHÈSE (souvenir, à vérifier sur PDF)**. Mes calculs faits à partir des v(s) de P sont marqués « illustratif ».

---

## (a) Ce que la question suppose sans que ce soit établi

### a1. « Chez nous, une fille triviale ne survit qu'au plus à α ; c'est le juge qui l'écarte »

**Statut :** propriété de conception, RAPPORTÉE (pièce A, point 3). Elle n'est pas établie empiriquement dans les faits.

Ce qui manque pour l'établir :
- **R1 n'a pas couru l'expérience.** La synthèse place la validation du critère de contenu contre une batterie de tricheurs en *première* expérience, et dit que le code est « en cours d'écriture ». Aucun résultat de cette batterie n'est servi.
- **R1 décrit le critère comme franchissable à coût nul.** Le critère « la fille prédit plus que ses parents » est franchi par l'enveloppe aveugle, la copie renommée, le pari couvert et l'adimensionnement.
- **P confirme un trou ouvert.** Le plan exclut de son essai le trou connu « parent + loi aveugle ».

**Conséquence.** La critique la plus forte contre Gemini (« ce n'est pas l'allocateur qui écarte les triviales, c'est le juge ») est conditionnelle à une expérience non faite. Si le juge fuit, l'allocation redevient une ligne de défense, et récompenser la promotion revient à récompenser la triche. C'est l'expérience E0 ci-dessous, à faire avant toutes les autres.

### a2. « Sur la littérature réelle, l'allocation de ressources bat la marche à la Swanson »

**Statut :** RAPPORTÉ (T), mais plus étroit que la formule de la question.

T établit seulement ceci :
- RA bat S à la précision à 10 000 : S − RA = −0,82 point [−1,43 ; −0,25] ;
- RA bat S en tête de liste : 28,4 % contre 19,2 % à 1 000 ;
- S a la meilleure aire sous la courbe, avec des intervalles qui se recouvrent.

Trois limites, toutes rapportées par T :
- l'issue mesurée est la **cooccurrence lexicale future**, « pas une découverte féconde » ;
- la tête de liste de RA est faite de mots courants (« ball — consistently ») ;
- les « champs éloignés » se réduisent pour l'essentiel à math – physique et cs – physique.

Ni RA ni S ne disent donc quoi que ce soit de la *valeur* d'une distance.

### a3. La distance de domaine entre parents est mesurable sur nos fiches et a une échelle commune

**Statut :** HYPOTHÈSE.

- La fiche de C porte un champ « domaines », pas une métrique.
- Les bornes 0,12-0,26 viennent de la bande du milieu de la simulation de Gemini (pièce A, P). Elles ne sont rattachées à aucune représentation de nos fiches.
- R2 montre la fragilité de toute mesure de ce genre. En TF-IDF, domaines proches et éloignés étaient presque indiscernables (cosinus 0,11 contre 0,009). Il a fallu passer aux fréquences brutes, choix qui, selon R2, *favorise* la forme testée.
- Un seuil absolu sur un cosinus ne se transporte pas d'une représentation à l'autre.

### a4. « Proche = triviale, lointain = chimère »

**Statut :** HYPOTHÈSE.

Aucune pièce ne mesure la trivialité ou la chimérité en fonction de la distance. Dans les mondes synthétiques de R2 :
- un a priori d'éloignement gagne : b_eloigne +11,9 [+10,4 ; +13,4] ;
- le même a priori s'effondre quand le monde est inversé : −11,6 [−12,5 ; −10,8].

Le signe suit le monde construit. Un monde synthétique encode la réponse ; R2 le dit lui-même (section 6).

### a5. Le résultat d'Uzzi et collègues porte sur la question

**Statut :** RAPPORTÉ (pièce A, transcription) pour les chiffres ; la transposition est une HYPOTHÈSE réfutée sur le plan conceptuel par la pièce A.

Trois raisons s'ajoutent à celle de la pièce A (paires de revues *dans un* article, et non similarité *entre deux* parents) :
- **L'objet n'est pas une courbe sur une variable.** Les chiffres rapportés (9,11 pour 100 de « hits » en forte conventionnalité et forte nouveauté, 5,33 en faible conventionnalité et forte nouveauté, 5 en moyenne) décrivent une interaction entre deux variables. Ils ne décrivent pas une courbe en cloche sur un axe de distance. L'article très atypique « reste au niveau de la moyenne » ; il ne « s'effondre » pas.
- **La valeur mesurée est la citation.** Ce n'est ni la vérité ni la fécondité, qui sont les variables de notre juge.
- **Le sens de lecture est inversé.** L'article combine un cœur conventionnel et une queue atypique. Une fille issue de deux parents n'a pas de « cœur » au sens d'Uzzi.

### a6. Ce que l'on sait, au-delà des pièces (question 1)

Tout ce paragraphe est **HYPOTHÈSE (souvenir, à vérifier sur PDF)**. Les pages ne sont données que là où la pièce A les fournit.

| Référence | Souvenir du résultat |
|---|---|
| Uzzi, B., Mukherjee, S., Stringer, M., Jones, B. (2013). « Atypical combinations and scientific impact ». *Science* 342, 468-472 (pages rapportées par la pièce A) | Interaction entre conventionnalité et nouveauté, comme ci-dessus |
| Fleming, L. (2001). « Recombinant uncertainty in technological search ». *Management Science* (pages à vérifier) | Sur des brevets, les combinaisons nouvelles ont une utilité moyenne plus basse et une variance plus haute |
| Wang, J., Veugelers, R., Stephan, P. (2017). « Bias against novelty in science: A cautionary tale for users of bibliometric indicators ». *Research Policy* (pages à vérifier) | Les articles « nouveaux » (paires de revues inédites) ont un impact plus variable, une reconnaissance plus tardive et une probabilité accrue d'être très cités à long terme |
| Foster, J. G., Rzhetsky, A., Evans, J. A. (2015). « Tradition and innovation in scientists' research strategies ». *American Sociological Review* (pages à vérifier) | Les stratégies innovantes sont plus risquées, et la récompense moyenne n'en compense pas entièrement le risque |

**Ce qui en ressort, si ces souvenirs sont exacts :**
- la variable qui revient dans ces travaux est la **variance**, pas une cloche de la moyenne ;
- l'issue est toujours la citation ou le brevet, jamais la vérité d'une prédiction ;
- aucune de ces études ne mesure la similarité entre *deux sources* combinées en une prédiction testable.

**Ce que je suppose, et ne sais pas :** qu'une cloche existe pour la promotion vraie par notre juge. Rien ne la soutient ni ne la réfute aujourd'hui.

### a7. L'entropie du verdict est un objectif distinct de l'espérance de découvertes

**Statut :** HYPOTHÈSE, et fausse dans le régime de P.

Quand toutes les probabilités de promotion sont sous 0,5, maximiser l'entropie revient à choisir la plus grande probabilité de promotion. C'est alors le même choix que le tri glouton par espérance. Dans P, v(s) ne dépasse jamais 0,60 et la puissance du juge est inférieure à 1. Les cellules au-dessus de 0,5 sont donc rares au mieux (illustratif). Point b1 ci-dessous.

### a8. Le score H₂(p) × 4p(1−p) × pénalité « compte deux fois la même chose »

**Statut :** critique RAPPORTÉE (pièce A). Elle est juste, mais incomplète.

H₂(p) et 4p(1−p) sont symétriques autour de 0,5 et strictement décroissantes en |p − 0,5|. Leur produit range donc les candidates *exactement comme* H₂ seule, à pénalité constante. La redondance ne change rien au classement. Seule la pénalité agit.

Cette déduction se vérifie en deux lignes de calcul. Je la laisse en HYPOTHÈSE tant qu'un tiers ne l'a pas contre-vérifiée. Le score est donc moins un double compte nuisible qu'un habillage : il ne faut lui accorder ni crédit ni débit au-delà de sa pénalité.

---

## (b) Expériences décisives (duels H_A contre H_B)

### b0. Attaque du plan P avant qu'il tourne

P est le seul test prévu. Sept défauts le rendent en partie circulaire, dans le sens inverse de la simulation de Gemini. Les valeurs suivantes sont calculées à partir des v(s) de P et sont **illustratives**.

**1. Trois mondes sur quatre sont tranchés par l'arithmétique.** La fenêtre (52 filles en moyenne sur 300, pour un budget de 40) teste presque uniquement dans la bande. Sa valeur moyenne y est :
- monde **bords** : 0,05 dans la fenêtre contre 0,196 en moyenne dans le réservoir ;
- monde **croissant** : environ 0,18 contre 0,325.

La défaite y vérifie la construction. Ce n'est pas un résultat.

**2. Le monde « décroissant » ne fait pas perdre la fenêtre contre le hasard.** Dans la bande, v vaut environ 0,47, contre 0,325 en moyenne. D₂ devrait être positif. La défaite contre les allocateurs appris ne dépend que de la vitesse à laquelle Thompson trouve la case s < 0,1 (v ≈ 0,57) avec 40 tests. Or P range justement cette lenteur parmi les causes d'échec de l'essai. La prédiction « perd (0,8) » repose donc sur ce que l'essai lui-même déclare non départageable.

**3. Dans le monde « cloche », le gain mesure la grille.** Les cases de Thompson ont une largeur de 0,1 et chevauchent la fenêtre :
- la case [0,1 ; 0,2) a v ≈ 0,41 ;
- la case [0,2 ; 0,3) a v ≈ 0,32 ;
- la fenêtre a v = 0,5.

Même un allocateur appris parfait plafonne à environ 0,82 fois la fenêtre. Si la grille était alignée sur la fenêtre, l'écart disparaîtrait. « Gagne dans cloche » ne départage donc pas l'idée de fenêtre ; cela départage un choix de cases.

**4. La composante « entropie » n'est pas testée** (voir a7). Dans la bande du monde cloche, v est constant : l'entropie n'a rien à y choisir.

**5. Le comparateur est choisi après coup.** D₁ compare la fenêtre au meilleur des deux allocateurs appris, retenu par sa moyenne dans le même échantillon. Ce maximum de deux moyennes bruitées biaise D₁ vers le bas : la règle est trop sévère pour « gagne » et trop indulgente pour « perd ».

**6. Pas de plafond.** P n'a pas d'oracle de case. On ne peut donc pas dire si un allocateur appris a échoué parce qu'il apprend mal ou parce que le budget ne le permet pas. R2 avait un plafond (0,750), et c'est ce qui lui permettait d'affirmer que « l'instrument sait enregistrer de grands gains ».

**7. Verdict non couvert.** Le cas « indistincte partout » n'a pas de verdict prévu.

**Correctifs minimaux.** Ajouter un oracle de case (qui connaît v par case). Choisir le comparateur par une règle fixée d'avance, par exemple Thompson seul. Ajouter les mondes de b2 et b3.

### E0. Le juge écarte-t-il les triviales et les tricheuses ? (préalable)

- **H_A :** pour chaque forme triviale ou tricheuse, la promotion reste ≤ α. Les formes à tester sont : copie, copie renommée, enveloppe aveugle, mélange, pari couvert, adimensionnement, et **parent + loi aveugle**.
- **H_B :** au moins une forme est promue au-delà de α.
- **Métrique :** taux de promotion par forme sur des mondes où la fille est fausse. Puissance sur les filles vraies, appariées (même monde, mêmes tirages).
- **Seuil :**
  - H_A si la borne supérieure de Clopper-Pearson à 95 % est < α pour toutes les formes ;
  - H_B si la borne inférieure est > α pour au moins une forme ;
  - sinon, on augmente le nombre de mondes. Il faut environ 2 000 mondes par forme pour une borne serrée autour de α = 0,05 (illustratif).
- **Contrôle négatif :** filles vraies de force faible (0,3), dont la puissance doit rester mesurable et non nulle. Un juge qui ne promeut rien passe trivialement H_A.
- **Ce que chaque issue falsifie :**
  - H_A falsifie la motivation « éviter les triviales » de la fenêtre. Il ne reste à la fenêtre qu'un argument de coût ;
  - H_B falsifie le point 3 de la pièce A. Elle invalide aussi tout allocateur récompensé par la promotion, ce qui inclut le Thompson de P.

### E1. Fenêtre fixée d'avance contre fenêtre apprise

- **H_A :** une fenêtre fixe [0,12 ; 0,26] fait plus de découvertes vraies par dollar que des allocateurs qui apprennent en ligne, *quand la valeur suit une cloche dont on ne connaît pas la position*.
- **H_B :** les allocateurs appris font aussi bien ou mieux dès que la cloche n'est pas exactement dans la fenêtre.
- **Mondes :**
  - cloche de centre c tiré uniformément sur [0,1 ; 0,7] et de largeur w ∈ {0,07 ; 0,14 ; 0,28}, avec v = 0,5 dedans et 0,05 dehors ;
  - plus les cinq mondes de P.
- **Allocateurs :**
  - hasard ;
  - Thompson sur grille fine et sur grille de P ;
  - Thompson à a priori de fenêtre, c'est-à-dire bêta(a, b) relevé dans [0,12 ; 0,26], avec a + b ∈ {2 ; 10} ;
  - fenêtre fixe de P ;
  - oracle de case.
- **Métrique :** découvertes vraies par dollar, différences appariées, nombres aléatoires communs.
- **Seuil (illustratif, à fixer avant lancement) :** δ = 0,02 découverte par dollar.
- **Contrôle négatif :** le monde plat, où tous les allocateurs doivent être indistincts. Un écart y signalerait un artefact d'ordre ou de graine.
- **Taille :** 200 répétitions par monde, parce que c varie (illustratif). Avec 40 tests et p ≈ 0,3, l'écart-type est d'environ 0,07 par dollar et par répétition. L'appariement réduit l'écart des différences (illustratif).
- **Ce que chaque issue falsifie :**
  - si la fenêtre fixe ne gagne que lorsque c ∈ [0,12 ; 0,26], son avantage est celui d'un a priori juste, pas une découverte : H_A est falsifiée comme règle générale ;
  - si elle gagne même hors de cette zone (par exemple parce que l'apprentissage est trop lent à 40 tests), H_B est falsifiée. Il faut alors conclure qu'à ce budget, tout a priori fixe bat l'apprentissage, et chercher le bon a priori sur données réelles (E3).
  - le bras « a priori de fenêtre » départage une troisième voie : si une force d'a priori faible ne perd jamais plus de δ et gagne quand c est dans la fenêtre, il domine les deux extrêmes.

### E2. Entropie du verdict contre espérance de découvertes et gradient de connaissance (question 3)

- **H_A :** viser l'entropie maximale du verdict fait au moins autant de découvertes vraies par dollar que viser l'espérance maximale.
- **H_B :** l'espérance (ou le gradient de connaissance) fait strictement mieux quand des cases ont une probabilité de promotion au-dessus de 0,5.
- **Mondes :**
  - v jusqu'à 0,9, avec des forces de [1,0 ; 1,5] pour obtenir des probabilités de promotion supérieures à 0,6 ;
  - un monde à coût variable par test (1 à 5 dollars simulés, illustratif) ;
  - le régime de P comme témoin, où les deux objectifs doivent être confondus.
- **Allocateurs :**
  - entropie maximale ;
  - tri par espérance par dollar ;
  - Thompson ;
  - gradient de connaissance : Frazier, P., Powell, W., Dayanik, S. (2008). « A knowledge-gradient policy for sequential information collection ». *SIAM Journal on Control and Optimization* (pages à vérifier).
- **Seuil :** δ comme en E1, intervalle apparié.
- **Contrôle négatif :** le régime de P, où toutes les probabilités sont sous 0,5. Entropie et espérance doivent y être indistinctes, sinon il y a une erreur de mise en œuvre.
- **Ce que chaque issue falsifie :**
  - si l'espérance gagne quand des probabilités dépassent 0,5, H_A est falsifiée ;
  - si l'entropie fait aussi bien, H_B est falsifiée, et l'on rapporte cette égalité comme une coïncidence du régime.
- **Survie facile.** Avec un juge validé par E0, récompenser la promotion contre le nul augmenté ne récompense pas la survie facile. L'aptitude reste la sévérité (C, § 1). Sans E0, aucun objectif d'allocation n'est sûr.

### E3. La cloche existe-t-elle dans la rétrodiction ? (données réelles)

Données : les paires et les issues déjà calculées par T.

- **H_A (cloche) :** à score RA égal, le taux d'issue est non monotone en distance, avec un maximum intérieur.
- **H_B :** il est monotone ou plat.
- **Distance :** calculée **sur les seuls documents d'avant**. Deux définitions, fixées d'avance avant tout calcul :
  - (i) cosinus des profils de champ des deux termes, normalisés par la part de chaque champ. C'est le correctif proposé par T, point 1 des points mal posés, contre le « tout physique ») ;
  - (ii) cosinus des vecteurs de contexte de cooccurrence.
  La définition (i) est primaire.
- **Analyse :**
  - régression logistique de l'issue sur une fonction lissée du score RA (20 strates), plus β₁·d + β₂·d² ;
  - cloche si β₂ < 0 (intervalle sous 0) **et** sommet entre les déciles 1 et 9 de d ;
  - monotone si le sommet est hors de cet intervalle ou si l'intervalle de β₂ contient 0 et celui de β₁ l'exclut.
- **Test opératoire :** précision à 10 000 de « RA restreint à la bande des déciles 4 à 7 de d » contre RA.
- **Seuil relatif :** +10 % du taux de RA (illustratif). R2 et T recommandent tous deux un seuil relatif. T montre qu'un seuil absolu bascule avec le taux de base : 9,61 points en principal, 13,13 au placebo.
- **Contrôles négatifs :**
  - issues permutées (déjà dans T) : β₂ doit être nul ;
  - placebo 2003-2006 / 2007-2010 : le signe de β₂ doit être stable.
- **Biais connu, à dire d'avance :** la cooccurrence lexicale future favorise mécaniquement les termes proches. L'issue penche donc vers H_B. Une cloche trouvée malgré ce biais serait plus convaincante ; une monotonie ne l'est que pour cette issue-là. Pour les citations, il faut OpenAlex avec une clé, ce qui relève d'une décision de Lazar (pièce A).
- **Ce que chaque issue falsifie :**
  - H_A falsifiée si l'intervalle de β₂ contient 0 ou si le sommet est au bord, et si la restriction n'améliore pas RA de 10 % ;
  - H_B falsifiée si β₂ < 0 avec un sommet intérieur, stable au placebo.

**Ce qui ferait conclure que la fenêtre n'apporte rien (question 4).** Les trois conditions ensemble :
- E1 : la fenêtre fixe ne bat pas l'a priori faible hors du cas c ∈ fenêtre ;
- E2 : l'entropie n'est jamais meilleure que l'espérance ;
- E3 : pas de sommet intérieur stable, et pas de +10 % sur RA.

### E4. La bonne variable (question 2)

- **H_A :** la similarité de domaine des parents prédit la promotion vraie d'une fille au moins aussi bien que les autres variables.
- **H_B :** une variable *prédictive* fait mieux d'au moins 0,05 d'aire sous la courbe (illustratif).

Quatre variables, toutes calculables avant le test :

| Variable | Calcul sur nos fiches | Coût |
|---|---|---|
| (1) Similarité de domaine | représentation à fixer d'avance (voir a3) | aucun tirage |
| (2) Recouvrement d'opérateurs | Jaccard des champs « opérateurs » des fiches | aucun tirage |
| (3) Divergence des signatures prédictives | divergence de Jensen-Shannon entre les lois des deux parents sur des traits d'instances (sans issues), possible parce que chaque fiche engage une loi des issues sachant les traits | aucun tirage |
| (4) Synergie estimée | gain de log-vraisemblance de la fille sur l'enveloppe et le mélange des parents, sur les **50 tirages de calibrage seulement** | ces tirages, à compter dans le coût ; les 200 tirages frais restent intacts, donc pas de fuite vers le juge |

Pour la synergie au sens informationnel : Williams, P., Beer, R. (2010). « Nonnegative decomposition of multivariate information » (support et pages à vérifier).

- **Lieu du test :** les archives des générations du pôle, avec des témoins plantés et l'évaluation scellée de C, et non une simulation. En simulation, la variable que le monde encode gagne (même leçon que R2, section 6).
- **Taille :** au moins 300 filles testées pour une aire sous la courbe à ±0,05 (illustratif).
- **Contrôle négatif :** une variable bruit, c'est-à-dire un hachage de l'identifiant. Son aire doit contenir 0,5.
- **Ce que chaque issue falsifie :**
  - si (1) ne fait pas mieux que le bruit, la fenêtre perd sa variable, quelle que soit sa forme ;
  - si (1) domine (3) et (4), H_B est falsifiée et la fenêtre garde au moins un support.

---

## (c) Instruments : la mesure minimale de fonctionnement

| Instrument | Détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Juge figé** (pari contre nul composite) | puissance sur filles vraies, force de 0,3 à 1,5 | promotion par forme tricheuse (E0), y compris « parent + loi aveugle » exclue par P | même monde, mêmes tirages : fille vraie contre sa version tricheuse | comparaison de log-vraisemblance sur tirages frais contre le seul meilleur parent, sans nul augmenté. Le juge doit avoir moins de fausses alertes à puissance égale |
| **Critère de fille** (bat parents, mélanges, enveloppes) | même mesure | R1 : l'enveloppe aveugle bat la conjonction ; d'où la règle durcie « battre l'enveloppe de 2δ₀ » | fille neuve contre enveloppe des mêmes parents | règle « bat la conjonction » seule |
| **Mesure de similarité de domaine** | aire sous la courbe pour « même champ / champ voisin / champ lointain » étiqueté à l'aveugle sur des paires de fiches | paires classées « lointaines » alors qu'elles sont du même champ | paires appariées par opérateur partagé | étiquette de champ seule (taxonomie), qui ne coûte rien. R2 montre qu'une représentation peut échouer : TF-IDF 0,11 contre 0,009 |
| **Fenêtre** | enrichissement : taux de filles vraies dans la bande divisé par le taux de base | part de filles fausses dans la bande | paires de même score RA (ou même probabilité a priori) différant par la distance | hasard ; RA ; a priori faible (E1) |
| **Allocateur à entropie** | regret contre l'oracle de case | calibration de son p appris (score de Brier) : une entropie sur un p mal calibré vise au hasard | mêmes réservoirs et mêmes issues (nombres communs, comme dans P) | tri par espérance (équivalent sous 0,5) et Thompson |
| **Score H₂ × 4p(1−p) × pénalité** | voir a8 : vérifier mécaniquement que son classement égale celui de H₂ à pénalité constante | cas où la pénalité seule change le choix | mêmes candidates | H₂ seule |
| **Tirage stratifié, opérateur après tirage** | précision des paires (R2 : 0,203 [0,192 ; 0,215] en « bien ») | pièges moyeux (R2 : 0,385, contre 0,122 pour la marche de Swanson) | mêmes 40 candidats, même étage commun (R2) | tirage uniforme avec le même étage (R2 : −5,2 pour l'uniforme contre le stratifié) |
| **Filtre de compatibilité** | rappel 0,57 à 0,60 (R2) | rejets à tort 4 à 5 % (R2) ; fusions contradictoires 55,9 % → 34,4 % (R1, génération 0, non réaudité) | paires identiques, contraintes vraies compatibles ou non | règle de négation lexicale sur la même variable (à mesurer ; aucune pièce ne la mesure) |
| **Abstention faute de pont** | taux d'abstention dans le monde sans pont | abstentions quand un pont existe | même vivier avec ou sans pont planté | aucune mesure dans les faits. R2 mesure un placebo de précision, pas l'abstention. **Instrument non mesuré** |
| **RA et marche à la Swanson** | précision à 10 000 sur la cooccurrence future (T) | têtes de liste faites de mots courants (T, 15 exemples) | les deux têtes ont 2 378 paires communes sur 10 000 (T) | stratifié et attachement préférentiel (T). **Manque :** un échantillon des têtes étiqueté à l'aveugle « pont substantiel / non » (200 paires par méthode, illustratif). Sans lui, la validité de l'issue n'est pas mesurée |

---

## Question 5 : ce qu'on perdrait

Toutes les valeurs de cette section sont calculées à partir des v(s) de P et sont **illustratives**.

- **Adopter une fenêtre fixe qui est fausse.**
  - Dans le monde croissant, environ 0,56 fois les découvertes du hasard. Dans le monde bords, environ 0,26 fois.
  - Surtout, une fenêtre fixe ne teste jamais hors de sa bande. Elle ne peut donc **jamais apprendre** qu'elle a tort. La perte est irréversible tant que le réglage reste fixe.
- **Écarter une fenêtre qui est juste.**
  - Dans le monde cloche, l'enrichissement de la bande vaut environ 3,9 fois le hasard (0,5 contre 0,129).
  - Un allocateur appris en récupère une partie, au prix d'un regret borné par le budget d'exploration.
- **Asymétrie.** La première perte est sans borne si personne ne revient sur la règle. La seconde est bornée. C'est pourquoi le bras « a priori de fenêtre faible » d'E1 me paraît la forme à départager en premier.

Ce choix reste une **HYPOTHÈSE** tant qu'E1 n'a pas tourné. Il serait falsifié si l'a priori faible perdait plus de δ contre l'apprentissage pur dans les mondes où la cloche est hors de la fenêtre.

---

## (d) Ancrage matériel

| Expérience | Calcul | Modèle | Coût estimé |
|---|---|---|---|
| E0 | processeur ; NumPy ou bibliothèque standard, comme R2 (Python 3.13.17, RAPPORTÉ) | aucun | moins d'une heure de processeur pour 7 formes × 2 000 mondes × 250 tirages (illustratif) ; 0 USD |
| b0 et E1 | processeur | aucun | quelques minutes pour 10 mondes × 200 répétitions × 6 allocateurs (illustratif) ; 0 USD |
| E2 | processeur | aucun | même ordre (illustratif) ; 0 USD |
| E3 | processeur ; réutilise les `npz` de scores, d'issues et de vocabulaire de T (RAPPORTÉ). Il ne reste qu'à calculer la distance à partir des matrices d'avant | aucun | moins d'une heure (illustratif) ; 0 USD. Pour les citations : OpenAlex avec clé, sur décision de Lazar (RAPPORTÉ, pièce A) |
| Étiquetage des têtes RA / S et des paires de fiches | humain, à l'aveugle | aucun | quelques heures-personne (illustratif) |
| E4 | les fiches viennent des générations du pôle. Si un générateur ouvert est voulu en complément de la version 0 de C : un modèle ouvert de 7 à 8 milliards de paramètres sur un seul processeur graphique de 24 Go (illustratif) | familles distinctes pour générateur, extracteur et fusionneur (R1) | ordre de grandeur de quelques USD de location pour quelques centaines de fiches (illustratif). Dépense seulement sur le mot direct de Lazar (QUESTION) |

Pour comparaison : le tour « recombinaison » du collisionneur a coûté 8,86 USD (RAPPORTÉ, R1).

**Ordre proposé :**
1. E0, parce que tout l'argument « c'est le juge qui écarte » en dépend ;
2. b0, pour corriger P, puis E1 et E2 ;
3. E3 ;
4. E4 quand l'archive le permet.

**Ce qui peut être réfuté en premier :**
- le point 3 de la pièce A, par E0 ;
- la prédiction de P « décroissant : perd » contre le hasard, par b0.2 ;
- l'existence d'une cloche sur la cooccurrence future, par E3.

FIN-DE-CELLULE