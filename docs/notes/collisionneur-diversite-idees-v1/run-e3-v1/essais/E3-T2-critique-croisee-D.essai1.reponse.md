Les quatre pièces sont présentes et lisibles. Les remarques ci-dessous sont des analyses de conception, pas des résultats expérimentaux. Je ne reprends ni les budgets ni les priorités des propositions.

## Sur la proposition A

### (a) Défauts de méthode

- **E1 ne sépare pas « monde » et « proposeurs ».** Le passage à des mondes riches modifie simultanément la dimension des traits, les interactions, les tailles d’effet et le nombre de promotions possibles. Surtout, la couverture des **propositions brutes** reste mesurée par l’instrument oracle construit avec les mêmes mondes : une couverture faible peut venir des proposeurs, d’une mauvaise attribution des composantes, ou d’une détectabilité conditionnelle surestimée. Les deux hypothèses peuvent aussi être vraies ensemble : le monde offre plusieurs signaux et les proposeurs n’en prennent qu’un.
- **D_oracle est un étalon seulement relativement à une décomposition choisie.** Les composantes \(C_w\), les mondes neutralisés \(w\setminus c\) et le drapeau de détectabilité proviennent du même dispositif de conception. Une neutralisation peut modifier plusieurs composantes, la loi des traits et la marginale de référence. Compter les composantes ainsi définies ne démontre pas qu’elles constituent des idées observationnellement distinctes.
- **La couverture par chute relative de gain est instable.** Si le gain initial d’une loi est nul ou minuscule, la fraction de chute est indéfinie ou dominée par le bruit. Une loi peut contenir le bon mécanisme mais avoir un faible gain global à cause d’autres coefficients erronés ; inversement, sa chute après neutralisation ne prouve pas qu’elle utilisait la composante neutralisée.
- **La séparation calibration/évaluation de \(\tau\) n’est pas explicitement close.** Le seuil sert à regrouper, à prédire le refus par le juge et à évaluer détection/fausses alertes. Sans mondes disjoints pour choisir \(\tau\), choisir la règle de représentant et estimer ces taux, les performances de D_contenu sont optimistes. Le tirage aléatoire du représentant ne répare pas un groupe mal formé.
- **E3 et E5 ont des issues non exhaustives.** Deux fournisseurs peuvent faire *moins bien* que \(N\) tirages, ce qui n’est ni « autant » ni « strictement plus ». Le coût total rapporté ne permet pas d’appeler Kimi « le moins cher ». Dans E5, un calage peut provenir du juge, du test de mort, du hasard ou de l’archive servie, sans trancher entre les deux hypothèses. L’ordre décroissant des tailles nominales d’effet n’est pas nécessairement l’ordre des gains conditionnels à l’archive.
- **E2 surestime ce que prouve l’absence de copie promue sur un petit banc.** Zéro événement observé n’établit pas un taux faible sans borne de confiance dimensionnée. M6 ne couvre, lui, qu’une classe de morceaux sur grille : il ne ferme ni les produits, ni les compositions générales, ni les seuils hors grille.

### (b) Conditions de non-puissance ou de non-jugeabilité

Soit \(r\) la loi du jeu factice et deux lois identiques hors d’une région \(A\). Leur Jensen–Shannon moyenne vérifie \(d_{JS}\le r(A)\ln2\). Si \(r(A)<\tau/\ln2\), elles sont donc regroupées **quelle que soit leur différence sur \(A\)**. Une interaction ou une sous-population rare peut ainsi être supprimée alors même qu’elle reste détectable par son log-score sur les tirages du juge.

D_oracle cesse également d’être interprétable lorsque :

- deux composantes produisent la même loi observationnelle \(p^\star\), par redondance des traits ou support nul ;
- le gain \(G_w(\ell)\), défini par différence de log-scores, est trop proche de zéro pour estimer une chute relative ;
- une composante est détectable marginalement, mais son gain résiduel contre le **nul augmenté** est nul ou faible ;
- la valeur e n’est pas un simple rapport de vraisemblance : l’approximation d’un log e attendu proportionnel à \(N\Delta\), déjà présentée comme hypothétique par A, ne fournit alors ni le seuil de détectabilité ni l’ordre promis dans E5.

### (c) Contrôles négatifs dont l’absence serait fatale

- Des **composantes fictives**, des neutralisations sans effet et des paires de générateurs différents mais observationnellement équivalents, évalués hors des mondes ayant servi à construire \(C_w\). Sinon D_oracle peut inventer ou effacer des mécanismes sans être contredit.
- Des paires honnêtes identiques sur presque tout le support de \(r\), mais différentes sur une région hors jeu factice ou très rare. Les paires appariées par forme et traits ne testent pas ce mode d’échec.
- Pour E2/M6, des attaques **hors grille et hors paires d’archive** : produits, compositions et morceaux multiples. Les copies de représentants et les copies de sœurs ne contrôlent que les cas anticipés par le concepteur.
- Un monde global sans signal résiduel, répété sur toute la chaîne avec archive réduite, et pas seulement dans E4. Sans lui, la garde du nouveau calendrier de sélection n’est pas estimée.

## Sur la proposition B

### (a) Défauts de méthode

- **Exp. 1 conditionne sa métrique sur la promotion.** Le nombre de clusters parmi les promues mélange idéation brute, puissance du juge, test de mort et taille de l’archive. Un monde riche peut produire davantage d’idées brutes mais moins de promotions parce que chaque effet est plus faible. L’expérience ne peut donc pas attribuer le résultat aux proposeurs.
- **Son contrôle « K1-riche » est invalide.** Utiliser tous les traits ne signifie pas approcher la loi vraie : interactions, seuils, sous-populations et coefficients peuvent rester faux. Une promotion contre cette archive n’établit donc pas une fuite du juge ; une absence de promotion peut simplement signifier un manque de puissance.
- **Exp. 2 introduit une sélection par la plus grande valeur e.** Si ce maximum sert à choisir le représentant avant la décision finale, la décision utilise deux fois les mêmes données fraîches : sélection du gagnant puis revendication de sa valeur e. Cela crée un biais du vainqueur et exige une nouvelle preuve de validité, pas seulement une comparaison empirique. Si le choix intervient après promotion, l’expérience ne teste plus le même mécanisme de réduction des promotions.
- **Le « constat » oracle reste opérationnellement circulaire.** Dans Exp. 2, une fiche écartée est faussement regroupée si son constat n’apparaît dans aucune autre fiche **promue**. Le verdict de l’instrument dépend donc du pipeline qu’il est censé évaluer.
- **Exp. 5 et les validations C1/C2 ne séparent pas clairement construction et évaluation.** Lois synonymes, lois distinctes, lois adversariales, distance, seuil et méthode de lien sont conçus dans le même banc. Un F1 supérieur à celui de la forme syntaxique peut alors mesurer la facilité du banc plutôt que la généralisation.
- **Exp. 3 confond deux fautes différentes.** Être une recombinaison hors classe du nul ne rend pas une loi fausse selon \(p^\star\) ; être fausse selon l’oracle n’implique pas non plus exploiter la brèche. Exp. 4 confond enfin nombre d’appels, température, variation de prompt et coût réel des contextes répétés : « même nombre de lois » n’apparie ni les jetons ni les dollars.

### (b) Conditions de non-puissance ou de non-jugeabilité

Pour \(d_{L1}(q,q')=\mathbb E_{X\sim r}\|q(\cdot|X)-q'(\cdot|X)\|_1\), deux lois identiques hors de \(A\) satisfont \(d_{L1}\le2r(A)\). Si \(2r(A)\) est sous le seuil, elles fusionnent nécessairement. Sur un échantillon fini, la région peut même être absente du jeu synthétique ; l’estimation Monte-Carlo donne alors une distance nulle et une stabilité illusoire du clustering.

Le critère de Exp. 1 devient non jugeable lorsque le nombre de promues est inférieur au nombre de clusters exigé : l’échec est alors mécanique. Plus généralement, des contrastes peuvent avoir une distance L1 faible tout en conservant un gain de vraisemblance important si les probabilités de référence sont proches de zéro ; distance L1, gain de log-score et puissance de la valeur e ne sont pas interchangeables.

Enfin, « vraie/fausse selon l’oracle » reste non estimable tant qu’aucune tolérance sur une divergence, un contraste ou un gain prédictif n’est fixée. L’égalité exacte à \(p^\star\) rejetterait toute approximation utile ; une tolérance non scellée rend le taux de faux positifs arbitraire.

### (c) Contrôles négatifs dont l’absence serait fatale

- Un monde dont l’archive contient **exactement** \(p^\star\), et non une loi utilisant seulement tous les traits, ainsi qu’un monde avec traits supplémentaires purement non causaux.
- Un banc entièrement tenu à l’écart pour la distance et le clustering, comprenant des différences rares hors échantillon de calibration et des synonymes non produits par les transformations ayant servi à choisir le seuil.
- Pour la consigne de diversité, un monde sans structure résiduelle **et** une batterie distincte de recombinaisons hors classe. Le témoin à consigne neutre ne mesure ni le taux de fausses alertes ni l’exploitation du nul.
- Pour Exp. 2, un contrôle où le représentant est fixé indépendamment des valeurs e. Sans lui, on ne peut distinguer l’effet du regroupement de celui de la sélection du maximum.

## Sur la proposition C

### (a) Défauts de méthode

- **M1 superpose plusieurs traitements.** Quotas de formes, exclusion de traits, sous-échantillonnage de l’archive, nombre d’appels et température ne permettent pas d’attribuer un gain à un mécanisme particulier. Masquer une partie de l’archive ajoute surtout une perte d’information : les proposeurs peuvent redécouvrir des lois absentes de leur vue mais présentes dans le nul complet.
- **M2 n’assure pas l’absence de perte de puissance.** L’indépendance vis-à-vis des tirages frais protège éventuellement la validité de la sélection, pas sa puissance. Choisir systématiquement la loi la moins complexe favorise la suppression d’interactions et de régimes rares. Le regroupement glouton par paires n’est pas non plus une relation d’équivalence : \(A\) proche de \(B\) et \(B\) proche de \(C\) n’implique pas \(A\) proche de \(C\).
- **Le noyau de \(N_{\mathrm{eff}}\) n’est pas établi.** Rien ne démontre que \(K_{ij}=1-d_{JS}(f_i,f_j)/\ln2\) soit semi-défini positif. Avec des valeurs propres négatives, les logarithmes spectraux ne sont pas définis. La présentation assimile en outre entropie de Rényi d’ordre deux et exponentielle de l’entropie de Shannon, qui ne donnent pas le même estimateur.
- **Plusieurs critères sont vrais par construction.** Après regroupement, un singleton donne \(N_{\mathrm{eff}}/|S|=1\), sans aucune diversité. Les fiches algébriquement équivalentes injectées dans M2 ont une distance nulle et doivent être fusionnées : ce contrôle teste l’implémentation, pas la validité scientifique du regroupement.
- **La couverture causale par ablation n’est pas mécaniquement définie pour les six formes.** Ablier un trait dans `softmax`, une branche de `si_sinon` ou un composant de `melange` n’a pas la même signification. Une loi peut contenir une composante vraie et des termes parasites ; l’ablation ne fournit pas automatiquement une attribution causale.
- **Exp. 1 et Exp. 2 ne ferment pas leurs duels.** Leur échec peut venir du juge, des mondes ou de l’instrument spectral sans établir l’« effondrement modal ». Exp. 4 n’étend le nul qu’à certains seuils et certaines paires, mais revendique la fermeture d’une classe comprenant aussi produits et compositions. Choisir ensuite entre deux tailles de jugement sur les mêmes résultats ajouterait une adaptation non scellée.

### (b) Conditions de non-puissance ou de non-jugeabilité

Comme pour A, si deux lois ne diffèrent que sur \(A\) avec \(r(A)\ln2<\tau_{\text{doublon}}\), M2 les considère comme doublons quelle que soit leur divergence conditionnelle sur \(A\). Le choix du représentant le plus simple est particulièrement défavorable lorsque le vrai mécanisme exige une branche supplémentaire à faible poids dans \(r\).

\(N_{\mathrm{eff}}\) n’est pas comparable entre bras lorsque leurs nombres de fiches diffèrent : sa borne supérieure est \(k\). Il peut aussi augmenter avec du bruit prédictif faux. La couverture oracle devient non identifiable si deux arbres du générateur donnent la même loi \(p^\star\), si une composante n’agit que hors du support naturel, ou si son effet est déjà absorbé par une combinaison du nul.

Pour Exp. 4, une interaction vraie peut avoir une forte taille paramétrique mais un gain résiduel trop faible après enrichissement du nul. La puissance dépend alors de la loi du pari e, de sa variance et de la multiplicité, non du seul nombre de tirages.

### (c) Contrôles négatifs dont l’absence serait fatale

- Des paires honnêtes **hors support du jeu factice**, non utilisées pour choisir le seuil, et un contrôle de non-transitivité à trois lois. Les cas appariés du tableau ne suffisent pas s’ils suivent la même loi d’échantillonnage que le jeu factice.
- Des attaques inédites hors seuils quartiles, avec plus de deux morceaux, produits et compositions. Sans elles, Exp. 4 mesure seulement la couverture de la classe que le concepteur de v9 a anticipée.
- Un pilote A/A qui fait varier réellement les réponses des proposeurs ; répéter une graine de regroupement déterministe ne mesure pas ce bruit.
- Pour le scanner de fuite, des fuites transformées — paramètres arrondis, combinaisons linéaires, indices structurels — et pas uniquement des injections exactes. La détection des injections fabriquées par le scanner lui-même est tautologique.

## Sur la proposition E

### (a) Défauts de méthode

- **La couverture de contrastes n’est pas une mesure de nouveauté.** Une loi déjà présente dans l’archive, ou une recombinaison couverte par le nul, peut obtenir \(E_r(q)\) sous le seuil. Le maximum sur un portefeuille crédite aussi davantage les configurations produisant plus de fiches, même à budget monétaire égal.
- **Le score mesure une amplitude de contraste, pas nécessairement un mécanisme.** Pour un contraste linéaire, un mélange entre la bonne loi et une loi à contraste nul peut être crédité sans représenter correctement le mécanisme. Le seuil retenu ne garantit ni calibration, ni gain de log-score, ni promotion possible.
- **La séparation privé/public reste perfectible.** Les contrastes privés, les sentinelles et les mondes de validation viennent du même générateur. Si les seuils, régions stratifiées ou attaques sont révisés après les pilotes sans nouveaux mondes d’évaluation, les performances du regroupement et de la sécurité sont entachées par cette réutilisation.
- **Le duel sur les mondes riches mesure la récupérabilité de sentinelles choisies.** Il ne mesure pas directement le nombre d’occasions accessibles aux proposeurs. Une sentinelle construite à partir de l’oracle peut être beaucoup mieux adaptée que toute loi qu’un proposeur est susceptible d’émettre.
- **Le critère de « promotion indûment qualifiée de nouvelle » reste sémantique.** Sans définition fondée sur un gain résiduel contre une classe de lois, le duel de sécurité ne peut distinguer une fausse nouveauté d’une composition réellement utile.
- **A/A ne contrôle que le bruit, pas un biais commun.** Deux pipelines identiques peuvent être parfaitement équivalents parce que leur couverture est constamment nulle ou parce qu’ils partagent le même défaut d’instrument.

### (b) Conditions de non-puissance ou de non-jugeabilité

Le dénominateur de \(E_r\) peut être non nul mais arbitrairement petit. Son estimateur devient alors instable, et une erreur Monte-Carlo négligeable en absolu change la décision de couverture. Deux mécanismes séparables dans le code du générateur mais donnant la même loi observationnelle restent impossibles à distinguer : les compter ensemble après coup ne restaure pas une validation indépendante.

La métrique peut également diverger de la puissance statistique : une petite erreur quadratique sur des probabilités ne garantit pas un gain de log-score résiduel suffisant contre l’archive. Inversement, des différences portant sur des événements de très faible probabilité peuvent produire une forte divergence de vraisemblance tout en étant invisibles sur la grille publique.

Le duel des rôles est non jugeable sur les mondes sans mécanisme accessible si la « couverture accessible » est une normalisation par zéro. Enfin, attribuer une valeur e nulle aux fiches écartées peut être conservateur, mais la perte de puissance devient arbitrairement grande lorsque la grille publique ne représente pas les régions où porte le signal.

### (c) Contrôles négatifs dont l’absence serait fatale

- Des **lois d’archive et recombinaisons couvertes** soumises à la couverture : elles doivent être comptées comme anciennes, sinon la mesure crédite des redécouvertes.
- Des contrastes fictifs, des dénominateurs proches de zéro et des générateurs différents mais observationnellement équivalents, sur mondes privés disjoints de ceux ayant servi à définir \(T_r\).
- Pour le regroupement, le contrôle rare déjà prévu doit être réellement **hors grille publique et hors régions de calibration**. Sinon il ne teste pas la fuite entre construction et évaluation.
- Pour la sécurité, des familles d’attaques inédites et un monde global sans signal résiduel, en plus du témoin honnête apparié. Ce dernier mesure les faux rejets, pas le taux de fausses promotions.
- Pour les sentinelles, une sentinelle dégradée ou mal spécifiée mais de même contraste nominal. Sans elle, le duel peut établir seulement que l’oracle sait écrire une fiche détectable par son propre instrument.

FIN-DE-CELLULE