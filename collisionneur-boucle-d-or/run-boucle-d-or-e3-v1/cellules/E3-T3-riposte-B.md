# Proposition B — Tour III.3 : riposte

**Pièces.** Ma conception (E3-T1-B) et les deux attaques (E3-T2-A, E3-T2-C) sont présentes et complètes à la lecture. Je ne réponds qu'aux sections « contre la proposition B ». Quand je reprends une attaque adressée à l'autre proposition, je le signale.

**Statuts.** Ils sont inchangés : pièces **RAPPORTÉ** ; mes souvenirs **HYPOTHÈSE** ; mes chiffres **illustratif**.

**Deux corrections de statut dans les attaques elles-mêmes.**
- **C-a1** affirme que les 50 tirages de calibrage servent à « ajuster les poids du nul augmenté ». P dit seulement « 50 tirages de calibrage et 200 tirages frais ». L'usage précis n'est pas dans les faits : c'est une HYPOTHÈSE de C. L'attaque tient sans elle, car ces tirages appartiennent au juge, quel qu'en soit l'usage.
- **C-a6** dit que la probabilité de conclure H_A est « nulle ». Elle vaut au plus environ 2,5 % par forme, comme l'écrit A (B1), soit de l'ordre de 0,025⁷ pour sept formes ensemble (illustratif). Le fond est juste, le mot ne l'est pas.

---

## (a) Sort de chaque attaque

### E0 — validation du juge

| Attaque | Sort | Raison et suite |
|---|---|---|
| **A-B1, C-a6, C-c1** : H_A inatteignable pour un juge de niveau exactement α | **Acceptée** | J'ai confondu « ≤ α » avec « borne supérieure < α ». Correctif en E0′ : marge d'équivalence fixée d'avance, correction pour tests multiples, et un témoin « nul exact » soumis à la même règle. Ce témoin doit pouvoir conclure H_A ; sinon, c'est la règle qui est fausse. |
| **C-b6** : la zone grise force à relever la tolérance α′, et le tricheur s'y loge | **Acceptée en partie** | La marge ε est fixée **avant** lancement et n'est jamais relevée en cours d'essai. Si la zone grise persiste à N_max, l'issue est « juge non validé », traitée comme un échec pour la suite. Un tricheur à α + ε″ < α + ε passe E0′ **par construction**. Je le dis et je borne son coût : au plus 40·ε promotions fausses de plus par génération de 40 tests (illustratif). « L'essai ne se termine jamais » est **rejeté** : N_max le termine. |
| **A-B2, A-c1, évasion A contre E0** : une liste figée valide une liste, pas un juge | **Acceptée, transformée en test** | Ajout d'une famille paramétrée (masse de la loi aveugle, amplitude, sous-population ciblée), dont l'enveloppe perturbée de 2δ₀ + ε nommée par A. Les paramètres sont cherchés de façon adverse sur des mondes de développement, puis évalués sur des mondes réservés. |
| **A-c2** : garde de fraîcheur | **Acceptée** | On ajoute un juge volontairement fuyant, qui voit les 200 tirages frais. La garde doit le prendre, comme le « calculateur volontairement fuyant » de T. |

### P et E1 — fenêtre fixe contre fenêtre apprise

| Attaque | Sort | Raison et suite |
|---|---|---|
| **A-B3** : avec a + b = 2, l'a priori est presque plat ; « domine les deux extrêmes » est vrai par construction | **Acceptée** | Les deux forces deviennent deux bras distincts. Seule la force a + b = 10 porte une revendication. La moyenne a priori est fixée explicitement, faute de quoi le bras reste ambigu. A soulève ce défaut contre lui-même, C le soulève contre A ; il vaut aussi chez moi. |
| **A-B4** : l'oracle de case n'est pas un plafond | **Acceptée** | On ajoute un **oracle continu** qui connaît v(s). L'oracle de case est gardé comme diagnostic de la perte due à la grille. |
| **A-B9, A-c3** : l'asymétrie de la question 5 dépend du budget | **Acceptée, transformée en test** | Si l'apprentissage ne converge pas en 40 tests, son regret se répète à chaque génération. On teste aux budgets 40, 80 et 160, et sur des générations successives avec transmission de la loi a posteriori. |
| **A, contrôle 5** (adressé à C, « conséquence commune ») : Thompson à grille alignée | **Reprise, en le disant** | C'est le duel qui tranche mon point b0.3 : voir b0′. |

### E2 — entropie contre espérance

| Attaque | Sort | Raison et suite |
|---|---|---|
| **C-b4** : on inonde les cases vides pour piéger le gradient de connaissance | **Transformée en test ; rejetée comme fatale** | Le gaspillage est borné par le nombre de cases, un test au plus par case vide et par génération (illustratif). On ajoute un réservoir inondé et on mesure le regret. |
| **A-C5** (adressée à C) : la puissance du juge est le facteur confondant | **Reprise, en le disant** | Elle s'applique à mon E2 : si la probabilité de promotion vaut v × puissance et reste sous 0,5, E2 ne départage rien. Elle devient un préalable mesuré. |
| **C-b3** (adressée à A) : dilution jusqu'à p ≈ 0,5 | **Reprise, en le disant** | C'est le meilleur argument contre l'entropie comme objectif : elle récompense les candidates rendues incertaines exprès. Ajoutée comme monde de E2′. |

### E3 — rétrodiction

| Attaque | Sort | Raison et suite |
|---|---|---|
| **A-B5** : la distance (ii) est colinéaire avec RA ; la distance (i) risque d'être dégénérée, car les termes sont spécifiques par construction | **Acceptée** | La distance (ii) est rétrogradée en simple diagnostic. Pour (i), deux préalables sont rapportés avant toute issue : variance et corrélation de rang avec RA. En cas d'échec, E3′ est déclaré non exécutable sur ces données. Ce n'est alors pas un résultat. |
| **A-B6, C-a3, C-b3** : la quadratique encode la réponse ; une courbe concave qui sature donne β₂ < 0 et un sommet intérieur fictif | **Acceptée** | Mon critère aurait classé « cloche » une monotonie saturée. La parabole est remplacée par trois éléments : vingtiles libres, régression unimodale contre isotone, et test des deux droites. |
| **C-c2** : contrôle de monotonie saturée injectée | **Acceptée** | On y ajoute le contrôle positif symétrique : une cloche injectée doit être détectée. |
| **C-a4** : les déciles 4 à 7 sont arbitraires | **Acceptée, transformée** | La bande est **apprise sur le découpage placebo** (2003-2006 / 2007-2010), puis **évaluée sur le découpage principal**. Plus d'arbitraire, plus de sélection dans l'échantillon. |
| **A-c4, A-c5** : permutation de d à score RA constant ; corrélation de rang annoncée d'avance | **Acceptées** | Intégrées à E3′. |
| **C-a5, C-c3** (adressées à A) : troncature (K > 0, aucune cooccurrence avant), conditionnement par PA et CN | **Reprises, en le disant** | Elles valent pour mon E3. Toute forme trouvée est conditionnelle à ce support ; aucune conclusion sur une cloche globale. |

### E4 — la bonne variable

| Attaque | Sort | Raison et suite |
|---|---|---|
| **A-B7, C-a1** : la variable (4) se calcule sur les tirages du juge | **Acceptée** | Ma phrase « pas de fuite vers le juge » était fausse. (4) sort des variables calculées avant le test. Elle ne peut revenir que par un criblage **payant**, sur des tirages dédiés et disjoints, compté dans le budget : c'est un duel séparé. |
| **C-b2** : la fille mémorise les 50 tirages | **Rejetée sur le mécanisme, gardée comme garde** | La fiche est gelée et empreintée **avant** l'expérience (C, § 1). Une loi gelée ne peut pas mémoriser des tirages qu'elle n'a pas vus. L'attaque ne tient que si l'agent voit les tirages : il faut l'interdire et le vérifier mécaniquement (garde de E0′). Le biais d'un même échantillon qui sert à ajuster l'enveloppe et à mesurer le gain est **accepté** : on passe à l'ajustement croisé. |
| **A-B8, C-a2, C-c3, A-c7** : l'archive est sélectionnée par l'allocateur et par le filtre | **Acceptée** | On réserve un lot uniforme. « Variance du recouvrement d'opérateurs quasi nulle » n'est accepté **qu'en partie** : partager au moins une étiquette réduit la variance du Jaccard sans l'annuler. On mesure la variance **avant** de calculer l'aire. Sous le seuil, la variable est déclarée « non testable », et non « sans valeur ». |
| **C-a5** : la divergence de Jensen-Shannon n'est pas définie entre observables différents | **Rejetée comme fatale, retenue comme limite** | Le nul augmenté du juge (parents, mélanges, enveloppes) exige lui aussi que les parents prédisent les mêmes issues sur les mêmes instances. La variable (3) est donc définie exactement là où le juge v1 l'est. Si une correspondance entre observables est nécessaire, elle fait partie de la fille, et (3) n'est plus une propriété des parents. On rapporte la part des filles où (3) est définie. |
| **C-b1** : une permutation T(X) gonfle la divergence sans contenu | **Acceptée, transformée** | C'est une raison de ne jamais allouer sur (3) avant validation. On plante des parents permutés comme témoins. |
| **Évasion A contre E4** (« des champs que l'adversaire écrit ») et **C-b4** (déguisement lexical, adressé à A, mais il vise ma mesure s) | **Acceptées en partie** | (1), (2) et (3) portent sur les **parents**, fiches gelées et empreintées. L'auteur d'une fille ne peut pas les réécrire sans changer leur empreinte. Reste un risque à long terme : des parents écrits, génération après génération, par des générateurs adverses. Contre-mesure : s calculée par un extracteur d'une autre famille de modèles (R1 : trois familles distinctes), sur deux représentations (A-c6). |
| **A-c6** : deux représentations de s | **Acceptée** | Si leur concordance de rang tombe sous le seuil, (1) n'est « pas une variable ». |

### Instruments

| Attaque | Sort | Raison et suite |
|---|---|---|
| **C-b5, C-c4** : l'annotateur humain prend le jargon pour un pont | **Acceptée** | On mêle à l'aveugle des leurres de jargon : paires techniques sans voisin commun, ou synonymes à l'intérieur d'un même domaine. L'instrument est invalidé si plus de 10 % des leurres (illustratif) sont jugés « pont substantiel ». |

**« Tous à la fois » (A et C).** J'accepte la conclusion de A : seul un juge **sans trou**, sur **des tirages non vus**, arrête la fille composite. Cela renforce l'ordre que je proposais, E0 d'abord ; cela ne l'affaiblit pas.

---

## (b) Expériences corrigées

### E0′ — le juge contre les tricheuses fixes et adaptatives (préalable)

- **Formes testées :**
  - les sept de ma conception, dont « parent + loi aveugle » ;
  - une famille paramétrée tirée au hasard ;
  - la meilleure configuration trouvée par recherche adverse sur 200 mondes de développement (illustratif), réévaluée sur des mondes réservés.
- **H_A :** pour toute forme, taux de promotion ≤ α + ε.
- **H_B :** au moins une forme a un taux > α + ε.
- **Paramètres :** ε = 0,015 (illustratif), fixé avant lancement.
- **Règle de décision :**
  - H_A si la borne supérieure de Clopper-Pearson, corrigée par Holm sur le nombre de formes, est < α + ε pour toutes ;
  - H_B si la borne inférieure corrigée est > α + ε pour au moins une ;
  - sinon on augmente le nombre de mondes jusqu'à N_max. Une zone grise à N_max donne « juge non validé ».
- **Taille :** environ 1 700 mondes par forme pour une demi-largeur d'environ 0,015 autour de 0,05 avec une dizaine de formes ; N_max = 3 400 (illustratif).
- **Contrôles :**
  - **nul exact** : une fille dont la loi est le nul, donc promue au taux α par construction. Elle doit sortir en H_A, sinon la règle est invalide ;
  - **juge fuyant** : il voit les 200 tirages frais et doit être pris par la garde ;
  - **puissance** sur les filles vraies, par tranche de force (de 0,3 à 1,5), rapportée. Si la puissance à force 1,0 est inférieure à 0,5 (illustratif), E0′ est « non concluant pour l'allocation » : un juge frileux passe H_A sans rien prouver.
- **Ce que chaque issue falsifie :**
  - **H_A** falsifie la motivation « écarter les triviales » de la fenêtre, dans la limite des familles testées et de la marge ε. Il ne reste à la fenêtre qu'un argument de coût ;
  - **H_B** falsifie le point 3 de la pièce A. Elle disqualifie tout allocateur récompensé par la promotion (le Thompson de P, l'entropie) tant que le trou reste ouvert.
- **Coût :** processeur, 0 USD.

### b0′ — addendum au plan P, sans toucher à P

P est scellé avant lancement. Le modifier détruirait son préenregistrement. P tourne donc tel quel, et ses résultats se lisent avec les réserves de b0. Un **addendum P2**, scellé avant son propre lancement, ajoute :

- **Thompson à grille alignée** (cases 0-0,12 ; 0,12-0,26 ; 0,26-0,8), pour le duel du monde cloche :
  - **H_A :** la fenêtre bat le Thompson aligné, l'intervalle de la différence étant au-dessus de 0. L'avantage tient à la bande fixe ;
  - **H_B :** ils sont indistincts. L'avantage de P ne tenait qu'à la grille ;
  - chacune des deux issues falsifie l'une des deux lectures de b0.3.
- **Oracle continu** comme plafond ; oracle de case comme diagnostic.
- **Comparateur fixé d'avance** : Thompson seul, ce qui supprime le maximum de deux moyennes bruitées (b0.5).
- **« Fenêtre gloutonne »** (même bande, choix par espérance) à côté de « fenêtre entropie », pour isoler l'entropie. A propose ce bras contre C ; je le reprends.
- **Budgets** 40, 80 et 160.
- **Verdict « indistincte partout »** : « l'essai ne départage rien à ce budget ». Ce cas n'avait pas de verdict dans P.

### E1′ — fenêtre fixe contre a priori réversible contre apprentissage

- **Bras :**
  - hasard ;
  - Thompson sur grille fine ;
  - Thompson aligné ;
  - **a priori fort** : bêta de moyenne 0,5 et de force a + b = 10 dans [0,12 ; 0,26], bêta(1, 3) ailleurs (illustratif, fixé avant lancement) ;
  - **a priori faible** (a + b = 2), rapporté sans revendication ;
  - fenêtre fixe ;
  - oracle continu.
- **Mondes :**
  - cloches de centre c tiré uniformément sur [0,1 ; 0,7] et de largeur w ∈ {0,07 ; 0,14 ; 0,28} ;
  - les cinq mondes de P ;
  - les mondes hostiles de P (bords, décroissant) appliqués explicitement aux a priori. C demande ce contrôle contre A ; je le reprends.
- **Budgets et générations :** 40, 80 et 160 ; cinq générations successives avec transmission de la loi a posteriori (illustratif).
- **Duel 1 :**
  - **H_A :** l'a priori fort ne perd pas plus de δ = 0,02 découverte par dollar (illustratif) dans aucun monde hostile, et gagne plus de δ quand c est dans la bande ;
  - **H_B :** il perd plus de δ dans au moins un monde hostile ;
  - H_A falsifie « tout a priori fixe est risqué » ; H_B falsifie la forme réversible comme défaut sûr.
- **Duel 2 :**
  - **H_A :** la fenêtre fixe bat l'apprentissage hors de la bande à 160 tests. C'est un artefact, à chercher ;
  - **H_B :** elle perd hors de la bande dès 80 tests. L'explication « apprentissage lent » est alors limitée aux petits budgets.
- **Taille :** 200 répétitions par monde, nombres aléatoires communs (illustratif).
- **Contrôle négatif :** le monde plat, où tous les bras doivent être indistincts.

### E2′ — entropie contre espérance

- **Préalable :** la puissance par force, mesurée en E0′. S'il n'existe aucune case où la probabilité de promotion dépasse 0,5, E2′ n'est pas lancé. L'équivalence est alors rapportée comme une propriété du régime, sans conclusion sur l'entropie.
- **Bras :**
  - entropie maximale ;
  - espérance par dollar ;
  - Thompson ;
  - gradient de connaissance (Frazier, Powell, Dayanik, 2008, *SIAM Journal on Control and Optimization*, HYPOTHÈSE (souvenir), pages à vérifier) ;
  - fenêtre gloutonne.
- **Mondes :**
  - v jusqu'à 0,9 avec des forces d'au moins 1,0 ;
  - coût variable de 1 à 5 dollars simulés (illustratif) ;
  - régime de P, comme témoin d'équivalence ;
  - **réservoir inondé** de candidates factices dans les cases vides ;
  - **filles diluées** : une loi vraie mélangée au nul jusqu'à p ≈ 0,5.
- **H_A :** l'entropie fait au moins autant de découvertes vraies par dollar que l'espérance dans tous les mondes.
- **H_B :** l'espérance fait mieux de plus de δ dans au moins un monde où des probabilités dépassent 0,5, ou dans le monde dilué.
- **Prédiction signée :** H_B dans le monde dilué.
- **Ce que chaque issue falsifie :**
  - **H_B** falsifie l'entropie comme objectif ;
  - **H_A** falsifie mon argument de dilution.

### E3′ — une forme non monotone dans la rétrodiction ?

- **Préalables**, rapportés avant tout calcul d'issue, avec des seuils fixés d'avance :
  - variance et écart interquartile de d (i) ;
  - corrélation de Spearman entre d et RA. Si |ρ| > 0,5 (illustratif), la définition est écartée ;
  - si d (i) est dégénérée, passage aux sous-catégories d'arXiv si les métadonnées versées les contiennent (à vérifier). Sinon, E3′ est non exécutable.
- **Distance (ii) :** diagnostic seulement.
- **Forme :**
  - taux d'issue par vingtile de d, à l'intérieur de strates de RA, PA et CN ;
  - régression unimodale contre isotone, par rapport de vraisemblance, avec un seuil fixé par rééchantillonnage ;
  - test des deux droites (Simonsohn, U., 2018, « Two lines: A valid alternative to the invalid testing of U-shaped relationships with quadratic regressions », *Advances in Methods and Practices in Psychological Science* ; HYPOTHÈSE (souvenir), pages à vérifier).
- **H_A (non monotone) :** pente positive significative avant le point de rupture **et** négative après, l'unimodal battant l'isotone. Signe stable au placebo.
- **H_B :** l'une des deux pentes est non significative ou de même signe que l'autre, ou l'isotone n'est pas battu.
- **Contrôles :**
  - permutation de d à l'intérieur des strates de RA : on doit conclure H_B ;
  - monotonie saturée injectée sur les d réels : on doit conclure H_B ;
  - cloche injectée : on doit conclure H_A, sinon l'instrument est aveugle ;
  - issues permutées, reprises de T.
- **Test opératoire :** bande apprise sur le placebo, évaluée sur le découpage principal. RA restreint à cette bande contre RA, seuil +10 % relatif (illustratif).
- **Portée :** le résultat est conditionnel au support de T (K > 0, aucune cooccurrence avant, pour l'essentiel math – physique et cs – physique) et à l'issue « cooccurrence lexicale future ».
- **Ce que chaque issue falsifie :**
  - **H_A** falsifie « la distance n'ajoute rien à RA » sur ce support ;
  - **H_B** falsifie la cloche pour cette issue.

### E4′ — la bonne variable

- **Lot uniforme réservé :** au moins 300 filles (illustratif), tirées parmi les candidates du générateur **avant** tout allocateur. Un sous-lot contourne l'appariement d'opérateurs, pour la variable (2).
- **Calcul des variables :**
  - (1), (2) et (3) sur les parents gelés, par un extracteur d'une autre famille ;
  - (1) sur deux représentations, avec un seuil de concordance de rang ;
  - (3) seulement là où les parents partagent l'observable, la part étant rapportée.
- **Témoins plantés :**
  - parents permutés (C-b1) ;
  - parent uniforme sur la moitié des traits (A) ;
  - variable bruit (hachage de l'identifiant).
- **H_A :** (1) prédit la promotion vraie au moins aussi bien que (2) et (3).
- **H_B :** l'une des deux fait mieux d'au moins 0,05 d'aire sous la courbe (illustratif).
- **Duel séparé sur (4) :**
  - **H_A :** un criblage payant de k = 15 tirages dédiés et disjoints, à budget total égal, plus K copies renommées d'une fausse fille pour mesurer la malédiction du vainqueur, fait plus de découvertes par dollar que l'absence de criblage ;
  - **H_B :** il fait moins bien ou autant.

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi** (RAPPORTÉ, et rien de plus) :
- **T :** sur la cooccurrence lexicale future dans arXiv, l'allocation de ressources bat la marche à la Swanson en précision à 10 000 (−0,82 point [−1,43 ; −0,25]). **Aucune distance n'y est mesurée.**
- **R2 :** la forme déterminantale corrigée vaut un tirage uniforme. Un a priori d'éloignement gagne +11,9 dans un monde synthétique et perd −11,6 dans le monde inversé : **le signe suit le monde construit.**
- **Pièce A :** chiffres d'Uzzi et collègues lus par transcription, non vérifiés sur PDF empreinté. Ils décrivent une interaction entre conventionnalité et nouveauté dans les références d'**un** article, pas une cloche de la valeur sur la distance entre **deux** parents.
- **Aucune pièce** ne mesure le lien entre la distance des parents et la vérité ou la promotion d'une fille.

**Ce qui ne l'est pas :**
- **Q1, la littérature.** Mes souvenirs (Fleming 2001 ; Wang, Veugelers, Stephan 2017 ; Foster, Rzhetsky, Evans 2015) suggèrent que la nouveauté joue sur la **variance** de l'impact plutôt qu'elle ne dessine une cloche de sa moyenne. Ce sont des HYPOTHÈSES (souvenir, à vérifier sur PDF). Elles portent toutes sur la citation ou le brevet, jamais sur la vérité d'une prédiction.
- **« Le juge écarte les triviales »** est une propriété de conception, non mesurée. R1 décrit le critère comme franchissable, et P exclut un trou connu.
- **« Entropie ≡ espérance sous 0,5 »** est ma déduction, encore HYPOTHÈSE. Elle n'a de portée que si la puissance du juge laisse les probabilités de promotion sous 0,5, ce qui n'est pas mesuré.
- **Q2, la bonne variable.** Inconnue. Les candidates calculables avant le test portent sur les **parents gelés** : similarité, recouvrement d'opérateurs, divergence des lois. La synergie n'est pas disponible avant le test sans un budget de criblage dédié (A-B7, acceptée).
- **Q3, l'objectif d'allocation.** L'espérance de découvertes vraies par dollar, avec une exploration apprise (Thompson, gradient de connaissance), est ma proposition (HYPOTHÈSE), à départager par E2′. L'entropie récompense les candidates rendues incertaines exprès : c'est l'attaque de C contre A, reprise en E2′. La fenêtre, si elle sert, servirait comme **a priori réversible**, jamais comme filtre dur : un filtre dur ne teste jamais hors de sa bande et ne peut pas apprendre qu'il a tort. Cette asymétrie dépend elle-même du budget (A-B9) : E1′ la teste.
- **Q4, conclure que la fenêtre n'apporte rien.** Trois conditions ensemble :
  - E1′ : l'a priori fort perd plus de δ dans un monde hostile, et ne gagne rien que l'oracle continu n'explique ;
  - E2′ : l'entropie ne bat jamais l'espérance ;
  - E3′ : pas de forme non monotone stable au placebo, et pas de gain relatif de +10 % sur RA.
- **Q5, ce qu'on perdrait.** Adopter une fenêtre fixe fausse : environ 0,26 à 0,56 fois les découvertes du hasard selon le monde (illustratif), sans correction possible. L'écarter alors qu'elle est juste : un regret d'exploration, borné seulement si l'apprentissage converge au budget donné.

**L'expérience à faire en premier : E0′.**

Si le juge laisse passer une tricheuse au-delà de α + ε, tout allocateur récompensé par la promotion récompense la triche. Les deux équipes rouges le confirment : leur fille composite franchit fenêtre, variables et entropie, et seul un juge **sans trou**, sur **des tirages non vus**, l'arrête.

E0′ tourne sur processeur, pour 0 USD. Sa règle est désormais atteignable (marge ε, Holm, témoin nul exact) et sa liste n'est plus figée (recherche adverse). Chacune de ses issues réfute quelque chose : la motivation « triviales » de la fenêtre, ou le point 3 de la pièce A.

Ensuite : l'addendum P2, scellé sans toucher à P ; puis E1′ et E2′ ; puis E3′ sur les fichiers de T ; enfin E4′ quand le lot uniforme existe.

FIN-DE-CELLULE