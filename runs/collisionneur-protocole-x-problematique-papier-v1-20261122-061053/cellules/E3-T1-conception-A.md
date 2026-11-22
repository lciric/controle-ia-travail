# Proposition A — Tour III.1 : conception ciblée

**Pièces reçues.** Les blocs FAITS et QUESTION sont présents, non coupés, et de contenu identique. Aucun fait n'y porte de statut explicite et aucun résultat expérimental n'y figure : je traite le cadre comme posé, non comme établi. Tout ce qui suit est de la conception (HYPOTHÈSE). Tous les chiffres sont illustratifs, sauf « deux mois » et « huit milliards de paramètres ». Je n'ai vu aucune autre proposition, donc B1 est sans objet à ce tour.

## (a) Ce que la question suppose sans que ce soit établi

Chaque point ci-dessous a le statut HYPOTHÈSE, parce que les faits ne fournissent ni statut ni mesure.

| # | Présupposé | Pourquoi il compte |
|---|---|---|
| P1 | Le lieu de l'adversaire est fixé : l'agent lui-même (consigne ou poids altérés) ou un tiers qui modifie les entrées. | Les faits ne le disent pas. Un moniteur d'activations n'a de sens que si la dégradation passe par le calcul interne de l'agent. |
| P2 | « Non suspecte isolément » signifie signal faible mais non nul par étape. | Si le signal par étape est nul pour tous les instruments, aucun cumul ne détecte rien. |
| P3 | Le dommage est une grandeur mesurable, à peu près additive sur les touches, et bornée par étape. | Sans cela, on ne peut définir ni « petite touche », ni loi d'échelle, ni borne. Rien dans les faits ne borne le dommage d'une étape. |
| P4 | Les exécutions honnêtes de référence sont échangeables avec l'exécution surveillée en l'absence d'attaque. | Tout étalonnage des fausses alertes en dépend. |
| P5 | Les activations contiennent une information absente du texte produit. | Sinon le moniteur interne est un moniteur de texte plus cher. |
| P6 | La vérification coûteuse est fiable et peut voir une touche sur une étape isolée. | Si la dégradation n'existe qu'à l'agrégat (biais systématique entre options toutes défendables), l'audit par étape ne voit rien. |
| P7 | « Attaques jamais vues » désigne une classe délimitée. | Sans modèle de menace, une garantie est soit fausse, soit irréfutable. |
| P8 | Refaire toute la tâche honnêtement est trop cher pour être la défense. | Sinon comparer le résultat à quelques ré-exécutions suffit et le problème disparaît. |
| P9 | Un modèle de 8 milliards de paramètres mène une tâche longue avec un bruit honnête assez faible pour qu'une dégradation s'en distingue. | Sinon l'expérience mesure le bruit du modèle. |
| P10 | Les trois types sont séparables. | Le type 3 peut fournir la forme de l'énoncé du type 1 et la ligne de base du type 2. |

## (b) Expériences décisives

**Banc commun (HYPOTHÈSE de conception).** La tâche est une analyse synthétique à T étapes, avec T ∈ {8, 16, 32, 64, 128}. À chaque étape, l'agent prend une micro-décision (inclure un lot, choisir une correction, extraire une valeur d'un document) qui contribue au résultat final. La vérité est connue par construction. L'état est résumé d'étape en étape pour borner le contexte.

- **Dommage D** : écart du résultat final à la valeur honnête, en unités de σ_H, l'écart-type entre exécutions honnêtes.
- **Trois familles d'adversaire** (réponse à P1) : (i) consigne système de sabotage d'amplitude δ par étape ; (ii) adaptateur LoRA saboteur, sans consigne visible ; (iii) injection externe dans les sorties d'outil.
- **Cas honnêtes appariés** : même graine et mêmes données sans adversaire ; « honnête perturbé » (consigne neutre de même longueur) ; « honnête fautif » (erreurs naturelles de l'agent).
- **Seconde tâche moins structurée** : synthèse d'un corpus synthétique à faits plantés, pour vérifier qu'un résultat ne tient pas à la construction du banc.
- Seuils et configurations des détecteurs sont gelés et hachés avant toute attaque. Entre deux seuils, l'issue est déclarée « non concluante », pas comptée comme succès.

### Type 3 — loi importée : la racine carrée de la stéganographie

**Question.** La dégradation totale maximale qu'un adversaire peut injecter dans une trajectoire de T étapes, à taux de détection fixé, croît-elle comme √T face à un détecteur qui cumule, plutôt que comme T ?

**Raisonnement (HYPOTHÈSE).** Si une touche δ déplace le score d'une étape d'une quantité proportionnelle à δ, le dommage vaut T·δ et la détectabilité cumulée vaut √T·δ. À détectabilité constante, le dommage maximal D* croît donc comme √T. Face à un détecteur qui seuille étape par étape, δ reste borné par une constante et D* croît comme T.

**Réponse attendue, réfutable.** D*(T) = c·T^γ avec :
1. γ ∈ [0,4 ; 0,6] contre le détecteur cumulatif ;
2. γ ≥ 0,85 contre le détecteur « maximum par étape » ;
3. au-delà d'une longueur T*, γ remonte vers 1 quand le nombre N de références diminue, parce que l'erreur d'estimation du niveau honnête ne se moyenne pas sur T.

**Antériorité la plus proche.**
- Ker, Pevný, Kodovský, Fridrich, 2008, « The Square Root Law of Steganographic Capacity » (de mémoire ; lieu de publication à vérifier).
- Loi voisine en détection de rupture : Lorden, 1971, « Procedures for Reacting to a Change in Distribution » (de mémoire).
- Je ne connais pas de mesure de cet exposant pour le sabotage d'agents. C'est un aveu d'ignorance, pas une attribution de nouveauté.

**Duel.**
- H_A : la borne supérieure de l'intervalle à 95 % de γ est ≤ 0,65 contre le détecteur cumulatif.
- H_B : la borne inférieure de l'intervalle est ≥ 0,85.
- Falsification : une borne inférieure > 0,65 falsifie H_A ; une borne supérieure < 0,85 falsifie H_B.

**Métrique.** Pour chaque T, on balaie six niveaux de δ, avec 100 trajectoires par cellule (illustratif). D*(T) est le dommage moyen au niveau où la détection vaut 50 %, à 5 % de fausses alertes par trajectoire. γ est la pente log-log, avec intervalle par bootstrap sur les trajectoires.

**Contrôles.**
- Négatif : à δ = 0 (consigne neutre), la détection doit rester à 5 % pour tout T. Si elle dérive avec T, le détecteur cumule une dérive honnête et la mesure est invalide.
- Positif d'instrument : un décalage gaussien connu, injecté dans les scores honnêtes, doit redonner γ = 0,5 à ± 0,05.
- Dépendance : autocorrélation des scores honnêtes entre étapes, et permutation de l'ordre des étapes.

**Issue qui rend la question sans intérêt.**
- Pas de relation dose-réponse monotone entre δ et le score par étape : la loi n'a pas d'objet.
- Dommage non additif (écart à T·δ supérieur à 20 %).
- γ ≈ 0,5 sur la tâche synthétique mais pas sur la seconde tâche : le résultat est vrai par construction du banc.
- Si l'adversaire à 8 milliards de paramètres ne sait pas moduler δ, c'est un échec de faisabilité, à déclarer comme tel.

### Type 2 — mécanisme : cumul séquentiel orientant les vérifications

**Question.** Un test séquentiel qui cumule les scores sous-seuil des moniteurs de texte et d'activations, étalonné sur les références honnêtes, et qui dirige les vérifications coûteuses vers les étapes où l'évidence cumulée croît le plus, détecte-t-il plus de dégradations, à fausses alertes et budget égaux, que le seuillage par étape avec audit aléatoire ?

**Réponse attendue, réfutable.** À 5 % de fausses alertes par trajectoire et un budget k = 5 % des étapes, la détection des attaques de dommage D ≥ 2σ_H gagne au moins 15 points absolus sur la meilleure ligne de base mécanique. Le gain est mesuré sur une famille d'attaques absente de l'étalonnage (entraînement sur (i), test sur (ii) et (iii)).

**Antériorité la plus proche.**
- Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » (de mémoire) : moniteur de confiance et budget d'audit.
- Page, 1954, « Continuous Inspection Schemes » (de mémoire) : le cumul lui-même.
- Bhatt et al., 2025, « Ctrl-Z: Controlling AI Agents via Resampling » (de mémoire, liste d'auteurs à vérifier) : protocoles multi-étapes.
- Le cumul de scores de suspicion le long d'une trajectoire existe probablement déjà dans cette littérature : référence à vérifier.

**Duel principal.**
- H_A : le gain a une borne inférieure d'intervalle > 5 points sur la famille tenue à l'écart.
- H_B : le gain a une borne supérieure < 5 points, donc le signal par étape n'est pas cumulable ou les lignes de base le captent déjà.
- Falsification : l'une des deux conditions falsifie l'autre hypothèse.

**Duel d'ablation (P5).**
- H_A′ : ajouter la sonde d'activations au cumul apporte au moins 5 points, à fausses alertes égales, par rapport au texte seul.
- H_B′ : l'apport est ≤ 2 points, donc le moniteur interne est redondant dans ce cadre.

**Lignes de base à battre.**
- maximum par étape du moniteur de texte ;
- moyenne simple des scores (si elle fait aussi bien, le « mécanisme » se réduit à une moyenne) ;
- audit uniforme à budget égal ;
- régression logistique sur sac de mots ;
- longueur et perplexité sous le modèle honnête ;
- comparaison du résultat final à une ré-exécution (P8).

**Contrôles négatifs.**
- sonde entraînée sur étiquettes permutées ;
- direction aléatoire de même norme ;
- fausses alertes sur « honnête perturbé » et « honnête fautif », qui doivent rester ≤ 2 fois le niveau nominal.

**Issue sans intérêt.** La moyenne simple du moniteur de texte, ou la comparaison à une ré-exécution, atteint la même détection. Ou bien le gain n'existe que sur la famille (i), ce qui indiquerait que le mécanisme détecte la présence de la consigne, pas la dégradation.

### Type 1 — garantie : audit aléatoire et plafond d'influence

**Question.** Sous deux hypothèses mesurables (dommage par étape plafonné à c ; sensibilité q de la vérification coûteuse sur une étape touchée), la borne « un dommage non détecté supérieur à D survit avec probabilité au plus exp(−k·q·D/(c·T)) » tient-elle face à des attaques construites, après gel du défenseur, par une équipe qui n'a pas vu sa conception ?

**Origine de la borne (calcul élémentaire d'échantillonnage, à revérifier ; pas un théorème nouveau).** Un dommage D exige au moins m = D/c étapes touchées. Avec k audits tirés uniformément, la probabilité qu'aucun audit ne tombe sur une étape touchée et ne la voie est au plus (1 − q·m/T)^k, donc au plus exp(−k·q·m/T).

La borne ne s'appuie pas sur les moniteurs. Face à l'inconnu, seul le hasard de l'audit a un taux d'échec indépendant de la forme de l'attaque. Les moniteurs traitent les grosses touches et l'audit aléatoire traite les attaques à nombreuses petites touches.

**Exemple illustratif.** T = 64, k = 8, q = 0,8, c = 0,25σ_H, D = 4σ_H donnent m ≥ 16 et une borne d'environ 0,20. Avec k = 16, la borne tombe à environ 0,04. La garantie est donc faible aux petits budgets.

**Réponse attendue, réfutable.** Sur au moins 200 trajectoires d'attaques inédites réalisant D ≥ 4σ_H, réparties en trois familles conçues par l'équipe rouge :
- la fréquence de survie est inférieure ou égale à la borne ;
- q mesuré sur l'inédit est ≥ q supposé − 0,1 ;
- aucune étape ne dépasse c.

**Antériorité la plus proche.**
- Greenblatt et al., 2023 (cité plus haut, de mémoire) : sûreté empirique contre une équipe rouge. De mémoire, ce n'est pas une borne sur l'inédit.
- Vovk, Gammerman, Shafer, 2005, « Algorithmic Learning in a Random World » (de mémoire) : contrôle des fausses alertes sans hypothèse de loi.
- Plans d'échantillonnage pour acceptation en contrôle qualité : référence à vérifier.

**Duel.**
- H_A : la borne supérieure de l'intervalle sur la fréquence de survie est ≤ la borne théorique, pour les trois familles.
- H_B : la borne inférieure de l'intervalle dépasse la borne théorique pour au moins une famille.
- Sous H_B, on dit quelle hypothèse a cédé : q (touches invisibles en isolation, P6) ou c (dommage sur-additif, P3).
- Limite : H_A non falsifiée se rapporte comme « non réfutée par trois familles », jamais comme tenue contre toute attaque.

**Contrôles.**
- Négatif : le taux de faux positifs de la vérification sur étapes honnêtes doit être ≤ 2 %, sinon q n'a pas de sens.
- Placebo : attaque à δ = 0.
- Positif : une attaque grossière connue doit être prise au taux prédit.

**Issue sans intérêt.**
- La borne est ≥ 0,5 pour D = 4σ_H à k ≤ 10 % de T : garantie creuse.
- q sur étape isolée est indistinguable du taux de faux positifs : la garantie par étape n'a pas d'objet et il faut auditer au niveau du résultat.
- Imposer le plafond c coûte plus de 10 % de qualité honnête.

## (c) Mesure minimale par instrument

Le protocole est commun aux quatre instruments. Les seuils sont fixés sur les honnêtes d'étalonnage. L'évaluation se fait sur des honnêtes frais appariés (même état, continuation honnête contre continuation touchée) et sur une famille d'attaques tenue à l'écart. Les intervalles sont à 95 %.

| Instrument | Mesure | Cas honnêtes appariés | Vérifications mécaniques à battre | Critère « fonctionne » |
|---|---|---|---|---|
| Moniteur de texte (juge de langue notant chaque étape) | Taux de détection par étape à 1 % et 5 % de fausses alertes ; même mesure par trajectoire | Honnête, honnête perturbé, honnête fautif | Longueur ; perplexité sous modèle honnête ; expressions régulières ; sac de mots ; recalcul numérique de l'étape s'il est bon marché | Au moins 10 points au-dessus de la meilleure ligne mécanique, intervalle excluant 0 ; fausses alertes sur honnête fautif ≤ 2 fois le nominal |
| Moniteur d'activations (sonde linéaire, couche médiane, moyenne sur les jetons de l'étape) | Idem, entraîné sur (i), testé sur (ii) et (iii) | Idem | Direction aléatoire ; étiquettes permutées ; sonde de ré-encodage (voir ci-dessous) | Au moins 5 points au-dessus du moniteur de texte et de la sonde de ré-encodage, sur la famille tenue à l'écart |
| Références honnêtes (étalonnage du niveau nul) | Fausses alertes réalisées contre nominales, pour N ∈ {5, 20, 80} et pour chaque T ; part de variance entre tâches | Au moins 500 trajectoires honnêtes fraîches | Seuil constant sans référence ; références mélangées entre tâches contre références appariées à la tâche | Taux réalisé dans l'intervalle binomial du nominal ; échec si > 2 fois le nominal ou si dérive avec T |
| Budget de vérifications coûteuses (oracle par étape, vérité du banc) | Sensibilité q sur étape touchée ; faux positifs sur étape honnête ; taux de ciblage (part des audits tombant sur une étape touchée) | Étapes honnêtes du même état | Allocation uniforme à budget égal ; vérification du seul résultat final par ré-exécution | q − faux positifs ≥ 0,5 ; ciblage ≥ 2 fois le taux de base m/T, sinon l'allocation guidée n'apporte rien |

Deux précisions sur le tableau :
- **Sonde de ré-encodage.** On repasse le texte produit dans un modèle propre, sans contexte adverse, et on y entraîne la même sonde. Si elle fait aussi bien, le moniteur « interne » lit le texte.
- **Plancher des références.** Avec N références, le plus petit niveau d'alerte étalonnable sans hypothèse de loi est 1/(N+1). Avec N = 5, aucun seuil sous 17 % n'est garanti.

**Porte d'arrêt.** Si le moniteur de texte et la sonde échouent tous deux à leur critère, les types 2 et 3 n'ont pas de signal à cumuler. On s'arrête et on rapporte l'échec.

## (d) Ancrage matériel (tout est illustratif)

- **Modèle.** Un modèle ouvert d'environ 8 milliards de paramètres, par exemple Llama-3.1-8B-Instruct. Cet exemple n'est pas imposé par les faits. Il sert d'agent, de base du saboteur LoRA et de juge de texte. La sonde est entraînée sur ses activations résiduelles.
- **Volume.** Environ 2×10⁵ étapes d'agent (5 longueurs × 6 amplitudes × 100 trajectoires, plus honnêtes et familles tenues à l'écart), à environ 2 500 jetons par étape.
- **Calcul.** 400 à 800 heures de processeur graphique de 48 Go, soit 1 000 à 3 000 € en location. L'entraînement des adaptateurs prend quelques heures.
- **Stockage.** Moins de 50 Go, avec des activations moyennées par étape sur 2 ou 3 couches.
- **Personnes.** Deux personnes pendant huit semaines, plus une équipe rouge séparée pour le type 1 (environ une semaine-personne par famille), tenue à l'écart de la conception du défenseur.
- **Calendrier.**
  - Semaines 1-2 : banc et exécutions honnêtes, mesure de σ_H (test de P9).
  - Semaines 3-4 : instruments (c) et porte d'arrêt.
  - Semaines 5-6 : types 3 et 2, sur les mêmes trajectoires.
  - Semaine 7 : équipe rouge du type 1.
  - Semaine 8 : analyse.
- **Limite.** La validité externe à des agents plus capables n'est pas testée.

## Classement

1. **Type 3.** Trois prédictions chiffrées peuvent échouer indépendamment (exposant contre cumul, exposant contre maximum, effet de N). Les deux issues informent. La courbe dose-réponse qu'il exige est aussi le prérequis des deux autres types.
2. **Type 2.** Il est réfutable, mais sa valeur tient à l'écart avec des lignes de base anciennes (une moyenne, un audit uniforme). Le risque d'un gain nul ou spécifique à une famille est élevé.
3. **Type 1.** En deux mois, la garantie ne vaut que par P3 et P6. Aux budgets réalistes, la borne risque d'être creuse, et « non réfutée par trois familles » n'est pas « tenue contre l'inédit ».

**Ce qui me ferait changer de classement.**
- Le type 1 passe premier si la borne est ≤ 0,2 pour D = 4σ_H à k ≤ 10 % de T, si elle n'est pas violée sur les trois familles, et si le plafond c coûte moins de 10 % de qualité honnête.
- Le type 2 passe devant le type 3 s'il n'y a pas de dose-réponse mais que la sonde d'activations apporte quand même au moins 15 points sur famille tenue à l'écart. Il passe aussi devant si γ ≈ 0,5 n'apparaît que sur la tâche synthétique.
- Le type 3 passe dernier si l'adversaire ne sait pas moduler δ.

## Quatrième type oublié

- **4a. Borne d'impossibilité** (dual du type 1). Exemple : « aucun détecteur étalonné sur N références ne distingue un décalage par étape inférieur à l'incertitude sur le niveau honnête, donc le dommage indétectable croît linéairement en T au-delà de T* ». Elle se réfute en exhibant un détecteur qui y parvient.
- **4b. Instrument de mesure.** Le banc paramétré lui-même (cas honnêtes appariés, dommage à vérité connue). On le juge sur sa fidélité test-retest et sur sa capacité à séparer deux moniteurs que les lignes mécaniques ne séparent pas.

## Nouveauté

Je n'en attribue aucune. La procédure de vérification serait la suivante :
- remonter les citations descendantes de Greenblatt et al. 2023 et de Ker et al. 2008 ;
- chercher les croisements « square root law / covert / steganography » × « agents / monitoring / sabotage », et « sequential test / CUSUM » × « AI control » ;
- soumettre les trois questions à deux spécialistes, l'un du contrôle d'agents, l'autre de la stéganalyse ;
- consigner les requêtes et leur date dans l'article.

FIN-DE-CELLULE