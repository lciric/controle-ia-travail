# Proposition A — Tour III.2 : critique croisée de méthode

**État des pièces.** B, C, D, E et F sont présentes et closes par leur ligne de fin ; empreintes non recalculées (seule la lecture m'était permise). Ma conception du tour III.1 ne figure pas dans le texte servi : je ne m'y réfère pas. Le bloc FAITS répète la question et ne contient aucun fait à statut.

**Statuts.** Sauf mention, chaque critique est une HYPOTHÈSE (argument de méthode, non testé). RAPPORTÉ : littérature citée de mémoire. Rien n'est VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ. Règle 4 : tout nombre de cette cellule est illustratif, y compris les seuils repris des pièces et mes calculs, qui partent d'effectifs illustratifs.

**Notations des points (b).** *p* : probabilité qu'une cellule de la matrice binarisée vaille 1, d'entropie *H(p)*. *f* : fiabilité de la mesure de base qui sert à apparier (variance vraie sur variance observée). *κ* : atténuation commune du signal entre deux états. *n₊*, *n₋* : nombres de réseaux indépendants par classe, non de séquences. *q^k* : rétention d'une fonction qui exige *k* composants successifs, chacun survivant avec probabilité *q*.

## Sur la proposition B

**(a) Défauts de méthode**

1. **E2, plan incomplet.** Un seul type de bloc est décrit : le déviant global est aussi le standard local, donc niveau et identité du dernier symbole sont confondus (D prévoit le bloc croisé). Un modèle qui apprend en contexte attend y après habituation : E_loc peut être nul sur le modèle intact, et les deux effets relèvent d'une même copie à deux portées. L'appariement en AUC n'égalise pas la distance ; E le fait, je m'en sers ici.
2. **E2, marquage fréquentiel.** À structure de phrase fixe, la catégorie lexicale est périodique à la fréquence de la phrase : un plongement statique produit le pic « global » (Frank & Yang, 2018 — référence à vérifier). Vrai par construction du stimulus.
3. **E1, critères incompatibles.** H_A veut des témoins appariés en gain ; H_B veut un R² élevé d'une régression sur le gain, entre autres. L'appariement restreint la variance de ce régresseur : les deux critères ne se lisent pas sur le même jeu.
4. **E1, contexte neutre.** Les têtes d'induction agissent peu sans répétition : L1 s'y confond avec le modèle intact, et H_A tombe par le choix du sondage. L2, tirée à nombre de têtes et Δperte égaux, est une queue de distribution obtenue par rejet.
5. **E3, duel non exclusif.** Dans un réseau déterministe, tout état est fonction de l'entrée : H_B est vraie par construction. Le gain d'AUC oppose des activations, qui portent toute l'entrée, à quatre caractéristiques ; le détecteur peut n'apprendre que la norme.

**(b) Pertes de puissance**

- **PCI_art.** La variance de c/H(p) diverge quand p tend vers 0 ou 1 ; si la loi de p diffère entre classes, l'AUC lit p.
- **AUC entraîné contre témoins.** Elle porte sur les sites d'un seul réseau entraîné. Si l'unité est le réseau, n₊ = 1 : sous échangeabilité, une séparation parfaite a la probabilité 1/(n₋ + 1) (calcul).
- **S.** B ne dit pas que l'appariement utilise d'autres mesures que l'origine des courbes. À valeur observée égale, l'écart vrai attendu entre familles vaut (1 − f)(μ_loc − μ_glob) : S ≠ 0 sous l'hypothèse nulle dès que f < 1.
- **E3.** Le gain d'AUC n'est défini que relativement à la classe des prédicteurs d'entrée ; il tend vers 0 quand sa capacité croît.
- **E4.** Si la part normalisée au-delà de la base est atténuée d'un même κ pour tout jeu de traits X, alors C_X = (1 − κ)·ΔR²_éveil,X : l'ordre des C reproduit celui de l'éveil, et H_A est acquise sans traitement résiduel particulier. Seules les rétentions κ_X testent la question ; elles ne sont pas jugeables si l'intervalle du plafond de bruit sous sédation contient 0.

**(c) Contrôles négatifs indispensables**

- Un modèle à plongements statiques doit donner un rapport de 1 à la fréquence de la phrase.
- Appariement sur une moitié des items, mesure sur l'autre.
- Sonde réduite à la norme ; sonde lisant les activations d'un *autre* modèle sur la même entrée : un gain égal désigne une propriété du texte.
- Données d'éveil dégradées par un bruit ajusté au plafond de la sédation : l'écart de rétention entre traits doit y être nul.

## Sur la proposition C

**(a) Défauts de méthode**

1. **Statuts et attributions.** « VÉRIFIÉ » couvre des faits d'architecture et des noms de modèles, sans vérification décrite. Le local-global sous propofol est attribué à Bekinschtein et al. (2009), qui de mémoire ne porte pas sur le propofol (Uhrig et al., 2016 ; Nourski et al., 2018 — références à vérifier).
2. **Exp. 1, sélection qui code la distance.** Cibler les têtes « à longue portée » choisit les composants par le critère qui définit S_global : c'est, par sélection, la troncature que C écarte comme tricherie.
3. **Exp. 1, arrêt optionnel.** λ\* est la première dose où S_global ≤ 0,1·S_global(0), sur les items qui donnent D(λ\*) : S_global y est sélectionné bas, S_local non, donc D est biaisé vers le haut.
4. **Exp. 2, filtre circulaire.** Si le modèle de référence qui définit T_long est le modèle testé, G_global > 0 est imposé par sélection ; si c'en est un autre, le mode en 0 mesure un écart de capacité. Le contexte tronqué à 8 jetons est hors distribution. Une bimodalité entre positions signale un mélange de types de dépendance, pas une bistabilité. Dans la table, les positifs du détecteur sont fabriqués en masquant les têtes à longue portée : r(t) y répond par définition.
5. **Exp. 3.** La lecture finale des couches 1 à 4 confond prédictivité linéaire et identité d'opérations, absence de réponse et absence de conscience (objection a1 de B, que je reprends).
6. **Exp. 4.** σ_l vient de perturbations sous-seuil : en régime linéaire, réponse et référence sont proportionnelles au même jacobien, et la densité de M est réglée par le rapport des normes d'impulsion, que choisit l'expérimentateur. Les valeurs singulières par matrice ne fixent pas le gain de bout en bout : le jumeau « iso-spectral » n'est pas apparié en gain.

**(b) Pertes de puissance**

- **D(λ\*).** Le biais de sélection croît avec l'erreur type de Ŝ_global rapportée à S_global(0) et avec le nombre de doses ; s'y ajoute (1 − f)(μ_loc − μ_glob) après stratification sur ΔNLL(0).
- **Wilcoxon.** « Indiscernable de 0 » par p > 0,05 accepte une hypothèse nulle : sans puissance ≥ 0,9 contre S_global = 0,1·S_global(0), le critère est vide.
- **Hartigan.** Sous autocorrélation φ entre positions voisines, la taille effective est de l'ordre de n(1 − φ)/(1 + φ). Une divergence est bornée en 0 : toute masse π₀ > 0 au plancher fait rejeter l'unimodalité quand n croît.
- **BF₀₁ ≥ 3.** Avec 15 à 20 sujets, ce seuil dépend de l'échelle de l'a priori : à rapporter sur une plage d'échelles.
- **Δr.** Avec 5 à 8 minutes de récit, les blocs temporels indépendants sont peu nombreux devant 2 048 régresseurs : la régularisation ramène Δr vers 0 dans tous les états.
- **PCI_ANN.** Indéfini si H(M) = 0 ; AUROC avec n₊ ≤ 2, les points de contrôle d'une même course n'étant pas indépendants.

**(c) Contrôles négatifs indispensables**

- La règle de choix de λ\* appliquée aux interventions aléatoires, sur items tenus à part.
- G_global d'un second modèle aux mêmes positions ; troncature présentée dans un format d'entrée ordinaire.
- Éveil bruité au niveau de la sédation.
- Gain jacobien de bout en bout mesuré sur le jumeau iso-spectral.

## Sur la proposition D

**(a) Défauts de méthode**

1. **Échelle de la rétention.** R est un rapport d'AUC − 0,5, fonction non linéaire de la discriminabilité d′. Sous atténuation uniforme de d′ (κ = 0,5), une AUC de 0,90 retient 0,60 et une AUC de 0,60 retient 0,50 (calcul). Ce biais d'environ 0,1 va vers H_A ; seul, il ne simule pas 0,8 contre 0,2, mais il égale la tolérance de 0,1 accordée aux inversions. Les contrastes de veille sont exigés « mesurables », pas appariés.
2. **Décodeur.** Entraîné par palier, ou transféré depuis la veille ? Un décalage de latence sous anesthésique fait chuter le transfert sans perte d'information ; l'entraînement par palier a moins d'essais propres en profondeur.
3. **Ce que l'effet de bloc indexe.** Il dépend de la consigne et de l'attention (Pitts et al., 2014, cité par B). De mémoire, il disparaît à des doses où le sujet répond encore (Nourski et al., 2018 — référence à vérifier) : le palier intermédiaire peut isoler un désengagement de la tâche.
4. **Deuxième duel, issue écrite d'avance.** Le masque retire exactement l'information qui définit l'effet de bloc et épargne celle qui définit l'effet local : les deux bornes de rétention sont arithmétiques. D le reconnaît (« témoin de possibilité ») ; l'issue H_A ne réfute alors qu'un énoncé trivial, ce qui manque à B4. Seule la comparaison à la dégradation diffuse informe.
5. **Seuils communs à deux échelles.** 0,8 et 0,2 s'appliquent à une AUC sur signal bruité et à des bits sur un système déterministe ; la rétention n'est pas invariante par changement monotone d'échelle.
6. **Troisième duel.** Exclure des taux les configurations « indécidables » ne garde que les cas nets. L'ordre « fixé » des axes est arbitraire, et la longueur de Lempel-Ziv en dépend.

**(b) Pertes de puissance**

- **R.** L'intervalle de Fieller du rapport est non borné dès que celui de E_veille contient 0.
- **Règle d'intervalles.** Si « par participant » désigne un intervalle pour chaque participant, la probabilité de succès est ∏ᵢ Pᵢ et décroît avec l'effectif. Si c'est l'unité de rééchantillonnage, l'objection tombe ; la règle doit le dire.
- **Fausses alertes ≤ 5 %.** Pour une borne supérieure à 95 % sous 0,05 avec zéro fausse alerte, il faut n₋ ≥ 60 configurations indépendantes (calcul, règle 3/n) ; or les unités indépendantes sont les familles d'interventions.
- **Gain de 10 points.** Si la combinaison mécanique détecte déjà plus de 0,9, le gain est impossible : H_B par plafond.
- **Exclusions.** Les taux ne se transportent que si la loi du score est la même dans la fraction exclue.

**(c) Contrôles négatifs indispensables**

- EEG de veille additionné d'un bruit ajusté au rapport signal/bruit de chaque palier : R_local − R_bloc doit y être nul sur l'échelle retenue.
- Un palier où le sujet répond encore et tient la consigne.
- Le masque inverse, de même masse, visant l'intérieur de la suite : il doit éteindre le local et épargner le bloc.
- Score recalculé sur des ordres d'axes tirés au hasard : dispersion inférieure à l'écart entre états.

## Sur la proposition E

**(a) Défauts de méthode**

1. **Statuts.** « VÉRIFIÉ » qualifie des prédictions (compétence nulle du jumeau, conditionnement conservé) : une hypothèse y est présentée comme un résultat. Le résultat sur la kétamine est attribué à Casali et al. (2013) ; de mémoire il relève de Sarasso et al. (2015), que B, C et F citent : attribution à vérifier.
2. **E.I, intervention quasi positionnelle.** Amortir la rétention d'état d'un modèle à espace d'états impose un oubli exponentiel, soit la « pénalité exponentielle sur la distance » que E range parmi les vérifications mécaniques à battre. Choisir les têtes par leur entropie d'attention est un substitut de la portée. Le contraste Transformeur/Mamba compare donc deux interventions de nature différente, avec n = 1 par architecture et des corpus d'entraînement distincts.
3. **E.I, sélection.** « Il existe c\* » sur 20 doses et plusieurs familles, lu sur les mêmes quintuplets : maximum d'une statistique bruitée. L'AUROC de confiance à c = 0 n'est pas exigée ; un petit modèle peut être déjà sous 0,55.
4. **Local et global par taxonomie.** La distance est égalisée, pas le nombre d'étapes de calcul.
5. **E.II.** G_loc est lu dans les couches basses, G_glob dans les hautes : niveau et profondeur sont confondus. Le témoin d'historique croisé contredit l'exigence de coréférence distante : si l'antécédent est dans l'historique, le changer supprime le signal par l'entrée.
6. **E.III.** H_A est « réfutée » par une non-significativité, qu'un manque de puissance suffit à produire.
7. **E.IV.** Lésions appariées en norme, pas en perte. S_spec ≥ 0,80 et R² > 0,90 avec ‖J‖₂ peuvent coexister : les deux hypothèses seraient réfutées. La source de 50 modèles fonctionnels indépendants n'est pas donnée.

**(b) Pertes de puissance**

- **ISA.** Sous ISA(c) = 0, l'espérance du maximum sur m combinaisons quasi indépendantes vaut environ σ·√(2 ln m), soit 2,9 σ pour m = 60 (calcul).
- **Composition.** Si la rétention vaut q(c)^k, ISA > 0 pour tout q < 1 dès que k_glob > k_loc. Signature : un rapport ln P̃_glob / ln P̃_loc constant en c et entre familles signale une fragilité générique ; seule sa variation hors intervalle soutient une sélectivité.
- **Hartigan par cible.** Avec 50 historiques, un mode de poids π a un effectif attendu de 50π, soit 1 pour π = 0,02 : puissance voisine du niveau. Le log-ratio n'existe pas si P(G ≤ 0) > 0 : l'échantillon est tronqué.
- **S_spec.** E[min(Â₁, Â₂)] ≤ min(A₁, A₂) ; à AUROC égales le biais vaut −0,56 erreur type, soit environ −0,04 pour 30 paires (calcul), dans une bande de décision de 0,60 à 0,80.
- **AUROC fonctionnel contre jumeau.** C'est une fonctionnelle du couple de lois, et la loi nulle a des paramètres libres (gain, netteté de l'attention) : non jugeable si elle traverse 0,5 sur leur plage.

**(c) Contrôles négatifs indispensables**

- La pénalité exponentielle de distance appliquée au Transformeur, à horizon effectif égal, comme comparateur de l'intervention sur Mamba.
- c\* choisi sur des quintuplets, ISA lu sur d'autres.
- Historiques croisés avec antécédent dans le paragraphe cible ; mêmes historiques lus par un autre modèle.
- Lésions appariées en norme et en perte (D le demande ; je m'en sers).

## Sur la proposition F

**(a) Défauts de méthode**

1. **Exp. 1, rôle double du bruit.** Le bruit gaussien interne est à la fois intervention candidate et témoin naturel (chez B, il définit la loi nulle). Si toute perturbation uniforme donne S ≥ 0,25, F conclut à une « vulnérabilité sélective structurelle » qu'un modèle de composition prédit sans spécificité. Le bruit sur les logits ne contrôle que la marge, par des écarts indépendants ; une perturbation interne en produit de corrélés.
2. **Exp. 1, construction de S_anesth.** L'intégrale sur λ ∈ [0, 1] dépend de la paramétrisation. Les marges sont appariées sur les items mêmes qui sont évalués. L'asymétrie de retour avec cache est triviale (argument a7 de B, que je reprends).
3. **Exp. 2.** D(x_t) peut lire un contenu du préfixe (nombre d'entités concurrentes) absent des covariables de surface. Greffer des activations « à haut score » transporte du contenu, pas seulement un régime ; un vecteur aléatoire de même norme est un témoin trop facile. Aucun contrôle positif ne montre que la greffe peut restaurer G. Quatre détecteurs candidats, un retenu.
4. **Exp. 3.** Dans la table, les sujets « avec traitement sémantique résiduel attesté » n'ont pas de source indépendante : c'est la limite des labels énoncée par D, que je reprends.
5. **Exp. 4.** « Au moins une métrique » parmi quatre et leurs réglages : chemins multiples. La validation sur EEG valide un code pour séries temporelles, pas celui des matrices couches × positions. wSMI et Φ_approx le long des positions mesurent l'entraînement commun par le texte. L'ensemble des transformations isofonctionnelles n'est pas spécifié : avec normalisation de couche et non-linéarités par élément, peu conservent exactement la fonction.

**(b) Pertes de puissance**

- **S_anesth.** Sous rétention q^k, S > 0 sans spécificité. Au-delà de la dose plancher, le numérateur est constant et le dénominateur croît : S dépend de la borne d'intégration.
- **ΔAUROC_spont.** Avec 40 erreurs locales, l'erreur type d'une AUROC proche de 0,6 vaut environ 0,05 (calcul) : l'intervalle à 95 % de la différence couvre toute la zone entre les seuils 0,04 et 0,10.
- **k\*.** Si Δr_s(k) = κ_s·g(k), avec g concave et un seuil de détection θ, le k\* estimé décroît avec κ_s seul : la monotonie exigée par H_3A est prédite par le rapport signal/bruit.
- **Équivalence ±0,005.** Elle requiert une erreur type de Δr d'environ 0,003 (calcul) ; au-dessus, toute issue est indéterminée.
- **Exp. 4.** Si l'unité est le réseau, avec n₊ = 1 et n₋ = 10, P(AUROC ≥ 0,80) = 3/11 par métrique sous échangeabilité, et jusqu'à 0,72 pour quatre métriques indépendantes (calcul). Le dénominateur de ρ_inv est un maximum : il croît avec la taille de l'ensemble de transformations.

**(c) Contrôles négatifs indispensables**

- Une tâche locale exigeant autant d'étapes que G ; des directions internes tirées de la covariance des activations comme loi nulle.
- Greffe de différences naturelles de même norme ; greffe réussie sous λ\* comme contrôle positif préalable.
- Éveil bruité : k\* ne doit pas rétrécir.
- wSMI et Φ_approx entre deux réseaux séparés lisant le même texte : valeur nulle exigée.
- Écart de logits à la précision numérique sous chaque transformation dite isofonctionnelle.

FIN-DE-CELLULE