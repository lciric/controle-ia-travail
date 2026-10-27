# Proposition A — Tour III.1 : la « Boucle d'or » (fenêtre de distance et allocation des expériences)

Pièces reçues : A, P, R1, R2, T, C — toutes présentes et lisibles ; aucune coupure détectée. Les résultats de P sont absents **par construction** (plan seul) : je n'en invente aucun.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Que « la distance entre les idées combinées » est un scalaire, et que la similarité de domaine le mesure.** RAPPORTÉ (R2, § 3) : le vecteur de domaine n'a pesé sur rien dans les ponts plantés (noyau corrigé ≈ tirage uniforme ; pénalité de 0,6 % à cos = 0,28). RAPPORTÉ (T) : « champs éloignés » s'y réduit à math–physique et cs–physique. Donc la seule variable sur laquelle la fenêtre agit est, dans nos propres essais, celle qui n'a rien expliqué. HYPOTHÈSE : qu'un scalaire de distance existe pour des *fiches d'hypothèses*.

2. **Que le juge écarte les filles triviales (« survit au plus à α »).** C'est l'argument central de la critique (A), mais c'est une propriété de conception (C, § 1) : la batterie de tricheurs (R1, « première expérience ») est annoncée **en cours** et C4 est absente. Statut : HYPOTHÈSE, non éprouvée. Si un tricheur (enveloppe aveugle, copie renommée) passe au-delà de α, la fonction « éviter les triviales » de la fenêtre n'est plus redondante — la critique s'effondre sur ce point, et l'essai P mesure alors autre chose que ce qu'il croit.

3. **Que P teste la fenêtre honnêtement.** P donne à l'allocateur fenêtre la bande [0,12 ; 0,26] et construit le monde « cloche » exactement sur cette bande. P a retiré la calibration (bon), mais pas la **position** : le monde cloche est un monde où le devin a raison par construction. Statut : VÉRIFIÉ par lecture de P. L'essai mesure « que vaut une fenêtre juste contre un apprenant », pas « que vaut une fenêtre fixée d'avance ».

4. **Que l'entropie du verdict mesure l'incertitude sur la vérité.** Dans P, la probabilité de promotion d'une fille vraie dépend de la force de l'effet (uniforme sur [0,3 ; 1,5]) et de la puissance du juge à 200 tirages et marge 0,02. Un verdict à p ≈ 0,5 peut donc signaler **une fille vraie à petit effet** (incertitude de mesure), pas une fille dont la vérité est incertaine (incertitude épistémique). L'entropie confond les deux ; elle envoie le budget vers les tests sous-puissants. Statut : HYPOTHÈSE (raisonnement, non mesuré).

5. **Que « entropie × 4p(1−p) × pénalité » diffère d'un classement par entropie.** VÉRIFIÉ (mathématique) : H₂(p) et 4p(1−p) sont tous deux symétriques en p = 1/2 et strictement décroissants en |p − 1/2| ; leur produit l'est aussi. Le classement par ce score, à pénalité égale, est **identique** au classement par |p − 1/2|. A dit « compte deux fois » ; c'est plus fort : le second facteur n'ajoute rien, même pas un double comptage.

6. **Que le coût pertinent est celui du test.** P fixe un dollar par test. Dans C, l'étape coûteuse peut être la **fusion par modèle** (générer la fille) plutôt que le test sur processeur. Si la génération coûte plus que le test, l'allocation porte sur « quelles paires fusionner », et la fenêtre redevient un filtre de tirage — exactement ce que R2 a tranché (stratifié gardé). Statut : HYPOTHÈSE sur les coûts, aucun chiffre dans les faits.

7. **Que les filles sont indépendantes.** Deux filles des mêmes parents partagent des traits ; tester l'une informe sur l'autre. P tire 300 filles sans structure de parenté ; Thompson, tri et fenêtre traitent les filles comme indépendantes. HYPOTHÈSE : la corrélation entre sœurs est négligeable.

8. **Que l'issue de la rétrodiction (cooccurrence lexicale future) renseigne sur la valeur.** T le nie explicitement (« pas une découverte féconde », têtes de RA faites de mots courants). RAPPORTÉ. Tout test de la fenêtre « sur données réelles » par T parle de cooccurrence, pas de vérité ni d'impact.

9. **Que l'étude d'Uzzi et collègues porte sur une distance entre deux parents.** VÉRIFIÉ (attribution) : Uzzi, Mukherjee, Stringer, Jones (2013), « Atypical Combinations and Scientific Impact », *Science* 342 (6157), 468-472. Elle mesure, **par article**, la distribution des z de cooccurrence des paires de revues citées ; la « cloche » est un croisement 2 × 2 (conventionnalité médiane × queue atypique), pas une courbe sur un scalaire de distance. Les chiffres 9,11 et 5,33 pour 100 : RAPPORTÉ par A, transcription non auditée. La transposition à deux parents : HYPOTHÈSE (de Gemini), et A a raison de le dire.

**Question 1 de l'arbitre — ce que je sais et ce que je suppose.** Ce que je peux attribuer :
- Fleming (2001), « Recombinant Uncertainty in Technological Search », *Management Science* 47 (1), 117-132 (brevets) : la familiarité avec les composants élève la moyenne et **réduit la variance** ; les combinaisons nouvelles donnent plus d'échecs et plus de rares succès. VÉRIFIÉ (attribution) ; c'est un résultat sur la variance, pas une cloche sur la moyenne.
- Wang, Veugelers, Stephan (2017), « Bias against novelty in science: A cautionary tale for users of bibliometric indicators », *Research Policy* 46 (8), 1416-1436 (pages à vérifier) : nouveauté = paires de revues jamais citées ensemble ; les articles très nouveaux ont plus de chances d'être au 1 % du haut **sur longue fenêtre** et aussi plus de chances d'être peu cités ; reconnaissance retardée. Même lecture : variance et délai, pas cloche.
- Foster, Rzhetsky, Evans (2015), « Tradition and Innovation in Scientists' Research Strategies », *American Sociological Review* 80 (5), 875-908 (pages à vérifier) : stratégies innovantes rares, plus récompensées en espérance conditionnelle à la publication, plus risquées.
- Boudreau, Guinan, Lakhani, Riedl (2016), « Looking across and looking beyond the knowledge frontier… », *Management Science* 62 (10), 2765-2783 (pages à vérifier) : les évaluateurs notent **moins bien** les propositions distantes de leur expertise. Conséquence : toute courbe impact–distance observée sur la littérature publiée est filtrée par une sélection qui pénalise la distance ; la « chute aux chimères » peut être un artefact d'évaluation.
- Rzhetsky, Foster, Foster, Evans (2015), « Choosing experiments to accelerate collective discovery », *PNAS* 112 (47), 14569-14574 : les stratégies humaines de choix d'expériences (chimie) sont loin de celles qui maximiseraient la découverte collective ; pertinent pour la question 3, pas pour la cloche.
- Swanson (1986), « Fish oil, Raynaud's syndrome, and undiscovered public knowledge », *Perspectives in Biology and Medicine* 30 (1), 7-18.
- Shi et Evans (2023), « Surprising combinations of research contents and contexts are related to impact… », *Nature Communications* 14 (référence à vérifier pour le numéro d'article).

Ce que je **suppose** : aucune de ces études ne mesure la vérité d'une hypothèse ; toutes mesurent des citations ou des brevets ; aucune ne définit la distance entre deux parents. La forme « cloche sur la moyenne » n'est établie nulle part à ma connaissance ; la forme « variance croissante avec la distance » l'est plusieurs fois. Pour un pôle dont l'aptitude est la **sévérité survécue** et non le signe du résultat (C, § 1), une loi de variance n'implique pas une fenêtre : elle implique un **portefeuille** (répartir, pas exclure).

---

## (b) Expériences décisives, en duels

### Duel 1 — La fenêtre fixe contre l'apprentissage, à position inconnue

Correction du défaut n° 3 de P : le centre c et la demi-largeur w de la bande sont **tirés par répétition** (c uniforme sur [0,06 ; 0,74], w uniforme sur [0,04 ; 0,12] ; chiffres illustratifs), contraste v = 0,5 dans la bande, 0,05 dehors. L'allocateur fenêtre garde sa bande [0,12 ; 0,26] fixée d'avance. On ajoute un cinquième bras : **Thompson à a priori informé** (pseudo-comptes k = 4, illustratif, placés dans la bande de Gemini, apprentissage libre ensuite) — c'est la fenêtre rendue molle.

- H_A : la connaissance a priori de la bande vaut plus que 40 tests d'exploration — la fenêtre fixe bat Thompson plat **en moyenne sur les positions tirées**.
- H_B : la fenêtre fixe perd en moyenne sur les positions tirées ; seule la fenêtre molle (a priori informé) ne perd pas.
- Métrique : D₁ de P (découvertes vraies par dollar, apparié). Seuil préenregistré : intervalle à 95 % de D₁ entièrement d'un côté de 0 ; 100 répétitions (P en prévoit 30 ; avec un écart-type apparié de l'ordre de 0,08 par répétition, illustratif, 30 répétitions bornent à ±0,03, 100 à ±0,016 — c'est le second qu'il faut pour déclarer « indistincte » avec un plus petit effet d'intérêt de 0,05 découverte par dollar, soit deux découvertes sur 40).
- Contrôle négatif : monde plat (v = 0,2) ; tout bras qui s'y distingue du hasard accuse l'instrument.
- Issue qui falsifie H_A : la fenêtre fixe perd en moyenne sur positions tirées → la fenêtre est une **hypothèse sur le monde**, pas une politique ; elle ne vaut que si l'on sait d'avance où est la bande, ce que personne n'a mesuré.
- Issue qui falsifie H_B : la fenêtre fixe gagne même sur positions tirées → le budget 40 est trop petit pour apprendre, et l'allocateur à a priori informé est inutile ; mais alors la question devient « d'où vient la bande ? », renvoyée au duel 3.
- Issue qui met l'essai en défaut : Thompson plat ne bat pas le hasard dans les mondes à bande (P le prévoit déjà) ; alors augmenter le budget avant toute lecture.

### Duel 2 — La bonne variable : similarité de domaine contre recouvrement des signatures prédictives

Monde où la vérité d'une fille est engendrée **par les parents**, non par s. Chaque parent est une loi sur des sous-populations (forme de P). On définit trois traits visibles par l'allocateur : s (domaine), o (recouvrement des opérateurs, étiquettes de R2), et σ (synergie : part de la variance des issues expliquée par les deux prédictions jointes moins la somme des parts séparées, estimée sur les 50 tirages de calibrage du juge, donc **avant** le test frais). La vérité est tirée avec une probabilité qui dépend de σ seul (monde « synergie »), de s seul (monde « domaine »), ou des deux (monde « mixte »), avec corrélation s–σ de 0,3 (illustratif) pour imiter un proxy bruité.

- H_A : la similarité de domaine des parents prédit la promotion aussi bien que σ dans les trois mondes (s suffit).
- H_B : σ prédit mieux que s dès que la corrélation s–σ est inférieure à 0,5, et s n'apporte rien conditionnellement à σ.
- Métrique : gain de vraisemblance hors échantillon (log-perte) du modèle de promotion sur s, sur σ, sur (s, σ) ; et découvertes par dollar d'un Thompson à cases sur s contre un Thompson à cases sur σ.
- Seuil : écart de log-perte à intervalle entièrement d'un côté de 0 sur 100 mondes.
- Contrôle négatif : monde où la vérité est indépendante des deux ; aucun des deux ne doit battre le hasard.
- Falsifie H_A : σ bat s dans le monde « synergie » et dans le monde « mixte » ; la fenêtre porte sur la mauvaise variable, et l'étalonnage d'Uzzi n'est plus même pertinent.
- Falsifie H_B : s fait jeu égal partout → la synergie estimée sur 50 tirages est trop bruitée pour servir, et la similarité de domaine, moins chère, reste le trait d'allocation.
- Réserve : ce monde encode que la synergie est calculable sur les traits — HYPOTHÈSE. Sur nos fiches (C), σ se mesure sur les prédictions chiffrées des parents appliquées aux mêmes instances de calibrage ; c'est une mesure mécanique, sans appel de modèle.

### Duel 3 — Sur données réelles : la cooccurrence future est-elle non monotone en la distance ?

Sur les 1 000 000 de paires de T (scores et issues empreintés, RAPPORTÉ) : définir pour chaque paire de termes une distance d antérieure à T (par exemple 1 − cosinus des vecteurs de contexte d'avant, calculés sur la matrice d'avant 2003-2010 ; aucune information d'après). Ranger les paires en 20 vingtiles de d ; taux de positifs par vingtile.

- H_A : la courbe taux(d) a un maximum intérieur (unimodale, pic strictement entre les bords).
- H_B : la courbe est monotone (ou plate) ; tout pic intérieur est bruit.
- Métrique : différence de log-vraisemblance hors échantillon entre une régression unimodale et une régression isotone (monotone) sur d ; validation croisée par découpage des paires en 10 plis.
- Seuil préenregistré : la régression unimodale doit gagner sur au moins 8 plis sur 10 **et** la position du pic doit tomber dans le même vingtile (± 2) au découpage placebo 2003-2006 / 2007-2010 — la stabilité du placebo est le critère que T a déjà utilisé (tau de Kendall).
- Contrôle négatif : issues permutées (déjà en place dans T) ; les deux régressions doivent se valoir.
- Contrôle de sensibilité : injecter dans les issues permutées une dépendance unimodale synthétique de même amplitude que le taux de base × 3 (illustratif) et vérifier que la régression unimodale la retrouve — sinon l'instrument ne peut pas voir une cloche.
- Falsifie H_A : monotone ou plat sur le principal, ou pic instable au placebo → sur ce proxy, aucune fenêtre ; ce que gagne la fenêtre en simulation ne se retrouve pas dans la seule donnée réelle disponible.
- Falsifie H_B : pic stable aux deux découpages → la cooccurrence future est non monotone en la distance lexicale ; cela ne dit **rien** de la vérité (T, « ce que le test ne dit pas »), mais cela fournit enfin un étalonnage du centre, ce que ni Gemini ni Uzzi ne fournissent.
- Pour aller à l'impact : OpenAlex avec citations (décision de Lazar, accès réseau, hors de cette cellule).

### Duel 4 — L'objectif d'allocation : entropie du verdict contre espérance de sévérité gagnée

Objectif concurrent, aligné sur C (aptitude = sévérité survécue) : choisir la fille qui maximise E[(−log p_nul) · 1{promue}] / coût, estimé en ligne par case (sur s ou σ selon le duel 2). Monde de P enrichi : la force d'effet des filles vraies est visible par l'allocateur sous forme bruitée (une « prédiction chiffrée » de la fiche, C § 1), si bien que certaines filles vraies sont **prévisiblement sous-puissantes** à 200 tirages.

- H_A : l'allocation par entropie du verdict fait au moins autant de découvertes vraies par dollar que l'allocation par espérance de sévérité gagnée.
- H_B : l'entropie perd, et perd d'autant plus que la part de filles vraies à petit effet est grande.
- Métrique : découvertes vraies par dollar ; mesure secondaire : part du budget dépensé sur des filles dont la probabilité de promotion sachant la vérité est inférieure à 0,6 (illustratif).
- Seuil : intervalle apparié à 95 % sur 100 répétitions ; falsification de H_A si l'intervalle est sous 0 dans le monde « petits effets fréquents » (force uniforme sur [0,2 ; 0,6], illustratif).
- Contrôle négatif : monde où toutes les filles vraies ont la même force (p de promotion identique) ; les deux objectifs doivent se valoir — sinon l'écart vient d'ailleurs.
- Falsifie H_B : entropie ≥ sévérité dans le monde à petits effets → la confusion épistémique/aléatoire que j'allègue au point (a-4) n'a pas d'effet pratique à ce budget.
- Sur « récompenser la survie facile » : la survie facile est exactement une promotion à faible sévérité ; l'objectif proposé la pèse par −log p_nul, qui tend vers 0 pour un test que le nul passe souvent. L'entropie, elle, ne voit pas la sévérité.

### Duel 5 — Préalable : le juge écarte-t-il les triviales ? (R1, à faire avant les duels 1 et 4)

- H_A : copies, enveloppes aveugles et mélanges sont promus à un taux ≤ α (juge v1, nul augmenté, marge 0,02).
- H_B : au moins un tricheur dépasse α.
- Métrique : taux de promotion par tricheur sur 1 000 mondes (illustratif) ; intervalle de Wilson.
- Contrôle négatif : fille vraie à force 1,0 promue à un taux élevé (sinon le juge n'a pas de puissance et un taux ≤ α ne prouve rien).
- Falsifie H_A : un tricheur promu > α → l'allocateur **doit** porter une part du filtrage, et la fenêtre n'est plus redondante ; la critique (A, point 3) tombe.
- Falsifie H_B : tous ≤ α → la fenêtre ne peut plus se réclamer d'« éviter les triviales » ; il lui reste à prouver qu'elle trouve des vraies, ce que mesure le duel 1.

---

## (c) Mesure minimale par instrument

| Instrument | Détection à mesurer | Fausse alerte à mesurer | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Fenêtre fixe [0,12 ; 0,26]** | part des mondes « bande à position tirée » où D₁ > 0 (intervalle) | part des mondes plat / monotone / bords où D₁ > 0 (attendu ≤ 2,5 %) | même graine, même réservoir, même juge pour tous les bras (déjà dans P) | Thompson par cases plat ; Thompson à a priori informé ; régression unimodale en ligne (fenêtre apprise) |
| **Score d'entropie** | bits gagnés par dollar sur la calibration (réduction de l'entropie a posteriori des taux par case) | part du budget sur filles à promotion ≤ 0,6 sachant vraies | monde « forces égales » (aucune différence attendue) contre monde « petits effets fréquents » | espérance de découvertes par dollar ; espérance de sévérité gagnée par dollar |
| **Juge v1** | puissance : part des filles vraies promues, par force d'effet (0,3 à 1,5) | part des copies / enveloppes / mélanges promus, à comparer à α | même parents, même nombre de tirages (50 + 200), même urne | test de permutation sur les mêmes tirages ; rapport de vraisemblance direct fille contre nul composite |
| **Similarité de domaine s** | sépare paires « même domaine » et « domaines éloignés » plantées (R2 : 0,54 / 0,28 / 0,03, RAPPORTÉ) | homonymes et jargons rares rangés à tort comme éloignés (R2 : ≈ 0,03 à 0,04 des paires, RAPPORTÉ) | mêmes articles sous TF-IDF et fréquences brutes (R2 § 9 : le choix a changé les cosinus 0,11 → 0,28) | l'étiquette de domaine seule (juste à 0,95 dans R2) : si s ne bat pas l'étiquette, le scalaire est inutile |
| **Synergie σ sur fiches** | retrouve la synergie plantée dans le monde du duel 2 | σ > 0 sur des parents indépendants plantés (attendu : au niveau du bruit) | mêmes 50 tirages de calibrage pour tous les traits | recouvrement brut des variables (ensembles) ; recouvrement des opérateurs |
| **Rétrodiction comme instrument de distance** | puissance sur signal unimodal injecté (contrôle de sensibilité du duel 3) | pic détecté sur issues permutées (attendu : jamais stable au placebo) | principal contre placebo, mêmes définitions (T) | régression isotone ; vingtiles sur une distance au hasard |
| **Étude citée (Uzzi 2013)** | relire 9,11 / 5,33 pour 100 sur PDF empreinté (R7) | — | — | aucune : c'est une donnée d'attribution, pas un instrument ; sa transposition ne se mesure que par les duels 2 et 3 |

Sur la ligne « juge v1 » : tant que la ligne n'est pas remplie (duel 5), les deux lignes du haut mesurent un allocateur sous un juge dont la fausse alerte est inconnue ; c'est l'ordre des opérations, pas un détail.

---

## (d) Ancrage matériel

- **Duels 1, 2, 4, 5** : processeur seul, Python, bibliothèque standard ou NumPy ; aucun appel de modèle ; même infrastructure que P et R2 (R2 : run complet en 93 s, 4 000 mondes, RAPPORTÉ). Estimation : 100 répétitions × 6 mondes × 5 bras × 40 tests × 250 tirages ≈ 3·10⁷ tirages de juge par duel, quelques minutes de processeur (illustratif). Coût monétaire ≈ 0 USD hors temps d'orchestration (par comparaison, un tour du collisionneur a coûté 8,86 USD, R1, RAPPORTÉ).
- **Duel 3** : réutilise les artefacts empreintés de T (`scores-principal-v1.npz`, `issues-principal-v1.npz`, matrices d'avant), numpy 2.3.4, scipy 1.16.3, duckdb 1.4.1 (RAPPORTÉ). Le calcul des vecteurs de contexte d'avant pour 43 162 termes est de l'ordre d'une matrice termes × termes dense de 1,9·10⁹ entrées en flottants simples ≈ 7 Go (illustratif) ; en creux ou par projection aléatoire à 256 dimensions, quelques centaines de Mo (illustratif). Aucun réseau, aucune clé.
- **Extension à l'impact** (citations) : instantané OpenAlex, accès réseau et clé — décision de Lazar ; volume de plusieurs dizaines de Go (illustratif).
- **Modèles ouverts** : aucun n'est nécessaire aux cinq duels. Un modèle de plongement ouvert n'interviendrait que pour une variante de s sur fiches en texte libre ; je ne la recommande pas avant le duel 2, puisque la question est précisément de savoir si s est la bonne variable.
- **Préenregistrement** : scellé avant toute exécution, comme R2 et T (empreintes, graine maîtresse 20261027 de P pour l'exploration, graine distincte pour la confirmation), avec les prédictions signées. Mes prédictions, confiance : duel 1, la fenêtre fixe perd en moyenne sur positions tirées (0,8) et la fenêtre molle ne perd pas (0,6) ; duel 3, pas de pic stable au placebo (0,7) ; duel 4, l'entropie perd dans le monde à petits effets (0,7) ; duel 5, aucune prédiction (c'est le point aveugle).

**Question 5 — ce qu'on perd.** Adopter une fenêtre fausse : on exclut 82,5 % des filles (bande de largeur 0,14 sur [0 ; 0,8], VÉRIFIÉ par arithmétique sur P) ; dans le monde « bords » ou « décroissant » de P, la perte est bornée par le contraste du monde — mesurable, et c'est la ligne « fausse alerte » du tableau. Écarter une fenêtre juste : la perte est le coût d'exploration de Thompson, soit une fraction du budget dépensée dans des cases vides (jusqu'à 7 cases sur 8 au premier passage, ordre de 15 à 35 % des 40 tests, illustratif). L'asymétrie suggère la forme **a priori informé** (pseudo-comptes) plutôt que le choix binaire « fixer ou apprendre » que pose la question 3 : la perte en cas d'erreur est bornée par k pseudo-tests, le gain en cas de justesse est presque celui de la fenêtre. C'est une HYPOTHÈSE ; le duel 1 la tranche.

FIN-DE-CELLULE