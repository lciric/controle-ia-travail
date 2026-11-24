# Critique croisée de méthode, tour III.2 (proposition A)

*Pièces : les conceptions B et C sont présentes et paraissent complètes, puisque chacune se termine par FIN-DE-CELLULE. Je ne modifie aucun statut attribué par B ou C. Je signale seulement à l'arbitre les attributions que je conteste. Tous les chiffres que j'introduis sont illustratifs, sauf mention contraire ; les calculs élémentaires reposent sur les valeurs illustratives données par les pièces.*

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Le critère de P1 est vrai ou faux par construction.**
   - Dans un monde planté dont l'alternative est simple et connue, le test du rapport de vraisemblance est le plus puissant à horizon fixe : Jerzy Neyman et Egon S. Pearson (1933), *On the Problem of the Most Efficient Tests of Statistical Hypotheses*. Ce résultat publié est VÉRIFIÉ ; son applicabilité ici reste une HYPOTHÈSE.
   - Le test séquentiel de Wald minimise l'effectif moyen : Abraham Wald et Jacob Wolfowitz (1948), *Optimum Character of the Sequential Probability Ratio Test*. Résultat publié VÉRIFIÉ, applicabilité HYPOTHÈSE.
   - Or le test de Wald figure dans le nul d'archive de B. Le seuil « +15 points sur l'archive » n'est donc franchissable que si l'on prive les bases d'archive de l'information sur l'alternative. L'issue de P1 dépend de ce que l'on autorise les bases à connaître, et non de la fécondité de l'organisme.

2. **Le contrôle des fausses alertes en Zone 2 est tautologique.** Dans un monde simulé, le nul est connu. Un e-processus correctement codé y respecte l'inégalité de Ville par construction. La vérification par Monte-Carlo détecte donc des erreurs d'implémentation, pas une invalidité. La seule question qui compte est de savoir si $\mathbb{E}[e_t\mid\mathcal F_{t-1}]\le 1$ sous la loi honnête réelle des activations, et elle relève de P2.

3. **La boucle de retour honnête crée une fuite.**
   - Les statistiques renvoyées vers la Zone 2 sont choisies parce qu'elles « ont mis en défaut le nul » d'un candidat. Le canal est donc conditionné par les candidats : c'est une analyse adaptative sur la référence honnête.
   - Si les mêmes trajectoires honnêtes servent ensuite à mesurer $\widehat{\text{FPR}}$ en P2, l'estimation est biaisée vers l'optimisme.
   - B ne prévoit pas de partition entre les honnêtes qui calibrent les mondes, ceux qui ajustent la projection anti-style et ceux qui évaluent le taux de fausses alertes. La mention « sans ré-entraînement » en P2 est inexacte, car la projection quotient est ajustée sur des paires honnêtes.

4. **L'origine des dommages synthétiques de P2 n'est pas précisée.** B ne dit pas qui conçoit ces dommages plantés « hors familles ». S'ils sont conçus par l'équipe qui voit les moniteurs, la puissance mesurée en P2 est circulaire au regard de la règle de l'instance aveugle (RAPPORTÉ).

5. **Le filtre de non-redondance est confondu avec la difficulté des mondes.** B rejette un candidat si la corrélation de Spearman entre profils de scores dépasse 0,85. Or tous les détecteurs réussissent sur les mondes faciles et échouent sur les difficiles. Ce facteur commun peut porter la corrélation au-dessus de 0,85 entre deux mécanismes réellement distincts. Inversement, une reparamétrisation d'un test de somme cumulée peut passer sous le seuil si l'ensemble de mondes est peu varié.

6. **P1 souffre de la malédiction du gagnant.** H_A est vérifiée par « au moins un candidat ». Le meilleur de 2 000 candidats (illustratif) est le maximum d'estimations bruitées. B ne prévoit pas de jeu Monte-Carlo de confirmation, tenu à l'écart et tiré après le gel du candidat.

7. **P5 est une pseudo-réplication.**
   - L'unité de généralisation est la famille de sabotage, non la trajectoire. Avec une seule famille lue une fois, la variance entre familles n'est pas estimable.
   - L'issue « échec » ne « démontre » pas qu'un transfert unidirectionnel suffit. Elle ne falsifie que H_A sur cette famille.
   - H_B est composite (écart insuffisant OU fausses alertes franchies), donc ses deux branches ne falsifient pas la même chose.

8. **Une attribution de statut est contestée, sans la modifier.** B qualifie de VÉRIFIÉ par calcul l'affirmation selon laquelle $\mathbb E[e_t]=1+\varepsilon$ entraîne un taux de fausses alertes proche de 100 %.
   - Le calcul établit seulement que $\mathbb E[M_T]$ croît. Le franchissement de $1/\alpha$ dépend de $\mathbb E[\log(1-\lambda+\lambda e_t)]$.
   - Contre-exemple (illustratif) : $e_t\in\{0;\,2{,}01\}$ avec probabilité ½ chacun et $\lambda=0{,}5$. Alors $\mathbb E[e_t]=1{,}005$, mais $\mathbb E\log=\tfrac12(\ln 0{,}5+\ln 1{,}505)\approx-0{,}14<0$. Dans ce cas, $M_t\to0$ presque sûrement.
   - Le cœur du propos reste juste : la garantie de Ville est perdue. La quantification est fausse.
   - De même, B cite Dwork et al. (2015) à l'appui d'un énoncé spécifique à cette boucle. Cette référence établit un mécanisme général, non cet énoncé.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Axe 1, mise à l'échelle de l'alternative choisie par B.** Sous une dérive par acte de $\delta/\sqrt T$ dans un bruit gaussien de variance unité et indépendant, la divergence de Kullback-Leibler cumulée vaut $T\cdot\delta^2/(2T)=\delta^2/2$, indépendamment de $T$. La puissance à niveau α est alors bornée par $\Phi(\delta-z_\alpha)$ pour tout détecteur (calcul élémentaire ; l'hypothèse de loi est illustrative). Allonger l'horizon n'apporte rien, et le gain sur l'archive est fixé analytiquement par δ.

- **Esquisse par projection aléatoire de dimension $d$ vers $k$.** Pour un signal de rang un $u$ dans un bruit isotrope $\sigma^2 I$, le rapport signal sur bruit optimal passe de $\|u\|^2/\sigma^2$ à environ $(k/d)\|u\|^2/\sigma^2$, soit un facteur 1/16 pour $256/4096$ (calcul élémentaire, valeurs illustratives de B).
  - La propriété de Johnson-Lindenstrauss conserve les distances entre points. Elle ne conserve pas la détectabilité d'une direction faible.
  - La perte est pire si $u$ vit dans des directions de faible variance d'un bruit anisotrope.

- **Signal absent des activations.** Si la loi des activations sous sabotage est identique à la loi honnête sur les couches mesurées, la puissance de tout détecteur boîte blanche vaut α. P2, qui repose sur des dommages synthétiques, ne peut pas distinguer ce cas d'une perte de signal dans la chaîne de traitement.

- **Projection anti-style.** Soit $P_S$ le projecteur sur le sous-espace de style et $u_I$ l'écart moyen dû à l'intention. La puissance tend vers α quand $\|(I-P_S)u_I\|/\sigma\to0$, c'est-à-dire quand le style et l'intention sont presque colinéaires.

- **Axe 3, résidu spectral.**
  - Il faut d'abord que $\Sigma_{\text{poids}}$ ne dépende pas de la loi des entrées. Sinon le résidu n'est pas centré sous le nul, et les fausses alertes croissent avec l'écart entre les entrées de calibration et celles de l'épreuve.
  - Ensuite, en dimension $p$ avec $n$ échantillons d'estimation, une perturbation de rang faible d'intensité $\theta$ (en unités de variance du bruit) n'émerge du bord du spectre que si $\theta>\sqrt{p/n}$ : Jinho Baik, Gérard Ben Arous et Sandrine Péché (2005), *Phase Transition of the Largest Eigenvalue for Nonnull Complex Sample Covariance Matrices*. Résultat publié VÉRIFIÉ ; son transfert au cas réel et aux matrices de Gram inter-copies reste une HYPOTHÈSE.

- **Fuite mesurée par $\hat I\le 0{,}05$ bit.**
  - L'estimateur par substitution a un biais d'environ $(|S|-1)(|Y|-1)/(2n\ln2)$ bits sous indépendance. Ce biais suffit à dépasser 0,05 bit si les traces sont discrétisées finement et que $n$ est modéré.
  - L'information mutuelle dépend aussi de la loi a priori du secret, qui est un choix de conception. En la resserrant, on obtient une petite valeur par construction.
  - Si le seuil reste fixe sur $K$ épisodes, l'information cumulée $I(S;Y_{1..K})$ peut approcher $H(S)$. Une borne par épisode ne dit alors rien de la fuite totale.

- **Estimateur de Horvitz-Thompson corrigé par $\hat p(s)$.**
  - La variance diverge comme $1/(\pi_s p(s))$ quand $p(s)\to0$.
  - Le biais est non nul dès que $p$ dépend du type de dommage $Z$ à l'intérieur d'une strate et que la loi de $Z$ diffère entre dommages plantés et sabotage réel.

- **« Taux de survie en Zone 3 divisé par le coût ».** Le numérateur est un comptage de loi approximativement de Poisson, de moyenne inférieure à quelques unités. Le ratio n'est pas jugeable à l'échelle d'une feuille de route.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Partition honnête en trois jeux** : calibrage des mondes, ajustement de la projection, évaluation du taux de fausses alertes. Il faut aussi un contrôle comparant $\widehat{\text{FPR}}$ sur les honnêtes déjà vus et sur des honnêtes frais. Un écart signe une fuite.
2. **Base d'archive informée en Zone 2** (rapport de vraisemblance connaissant l'alternative plantée). Sans elle, le gain de P1 est un artefact.
3. **Organisme placebo en P1** à budget égal (graphe permuté ou archive caviardée). B ne dispose que de la boucle ouverte, qui n'isole pas la contribution de l'organisme.
4. **Témoin positif d'injection en P2** : un déplacement planté d'amplitude connue directement dans les activations honnêtes réelles. Sans lui, un échec de P2 est ininterprétable.
5. **Essaim honnête aux entrées décorrélées et essaim hétérogène** (lignées distinctes) en P3. Le seul contrôle « même biais honnête » ne sépare pas la corrélation due aux entrées de celle due aux poids.
6. **Secret permuté** pour estimer le plancher de biais de $\hat I$.
7. **Détecteur ne dépendant que de la difficulté** du monde, pour étalonner le seuil de Spearman.
8. **En P5, un retour structuré mais non pertinent**, par exemple les statistiques honnêtes d'une autre lignée, à la place du bruit gaussien. Tout retour structuré bat du bruit : ce contrôle est trop faible.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Fuite par spécification dans E1.**
   - Les fiches d'obstruction (axe 1 au-delà de N, confusion de style, corrélation implicite) décrivent exactement ce que les mondes-miroirs instancient.
   - Le second volet de H_B, selon lequel le bras « obstructions + corpus stratégiques » gagne, est donc favorisé par construction : ce bras reçoit l'énoncé de l'épreuve.
   - Rendre le module générateur « aveugle aux candidats » ne suffit pas s'il n'est pas aveugle aux fiches.
   - Le même défaut menace le « Cahier des charges » de B.

2. **Les sas 2 et 2.5 ne sont pas indépendants.** Les mondes-miroirs sont paramétrés par les statistiques honnêtes du jeu d'exploration, et le sas 2.5 filtre sur des trajectoires honnêtes du même jeu. Une partie du succès en 2.5 est prédite par construction.

3. **La sélection au sas 2.5 rend optimiste le taux de fausses alertes retenu.** E4 exige des honnêtes tenus à l'écart, ce qui est correct. En revanche, l'instrument 6 (valeur prédictive positive du sas) utilise des taux de fausses alertes déjà sélectionnés.

4. **E2 mesure la mauvaise quantité.**
   - Les faits décrivent un plafonnement de l'accumulation au-delà de la taille de la référence (RAPPORTÉ). La lecture la plus directe est un plafond d'évidence, puisqu'une p-valeur empirique est minorée par $1/(N+1)$. C'est une question de puissance.
   - E2 teste la conservation du taux de fausses alertes. Un candidat peut passer E2 alors que l'obstruction subsiste.
   - La clause de falsification de H_B (« alors que l'accumulateur à référence fixe plafonne ou dérive ») mélange les deux phénomènes.

5. **Le critère de E2 récompense la prudence.** Une borne supérieure d'intervalle de confiance au plus égale à 0,07 favorise les candidats sur-conservateurs, donc peu puissants. Validité et puissance sont confondues dans un même filtre.

6. **E3 est déterminée par la définition d'« orthogonale ».**
   - Si les familles finales ont un support disjoint des familles d'épreuve, la boucle fermée échoue par construction. Si elles sont proches, elle gagne par construction.
   - Le contrôle i.i.d. ne couvre qu'une extrémité. E3 mesure le générateur plutôt que la boucle.
   - Les 30 graines sont des réplications de l'organisme, non des familles : la variance pertinente n'est pas échantillonnée.

7. **Le témoin « sans organisme » de E4 est mal apparié.**
   - Le « coût égal » n'est pas défini (appels, jetons, temps). Les candidats de l'organisme ont traversé les sas 0 à 2.5, alors que le témoin est un « appel ponctuel ».
   - Un gain peut donc venir de la cascade de filtres, et non de l'organisme.
   - S'y ajoute la pseudo-réplication déjà relevée chez B : 100 trajectoires d'une seule famille.

8. **Le placebo par graphes permutés est trop faible s'il est fait naïvement.** Une permutation qui casse la distribution des degrés ou la structure de dates peut dégrader mécaniquement l'organisme. « Battre le placebo » devient alors trivial.

9. **L'ordre de lecture des gardes est inversé.**
   - Les zones de non-décision de E1 ($0{,}20\le\rho<0{,}50$), de E2 (de 0,07 à 0,10) et de E4 (Δ entre 0,05 et 0,12) ne falsifient rien. Elles contredisent B4 sur une partie de l'espace des issues, ce que C ne signale pas.
   - Le statut OBSERVÉ-NON-AUDITÉ attribué au présupposé « l'organisme apporte un gain » est contestable, sans que je le modifie. Les faits rapportent une évaluation interne, non une observation de gain en contrôle. Ce statut risque d'être lu comme un constat.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1, corrélation de Spearman sur $k$ versions.**
  - Avec $k=5$, la plus petite p-valeur unilatérale exacte vaut $1/5!=1/120\approx0{,}0083$ (calcul élémentaire, VÉRIFIÉ) ; en bilatéral, elle vaut environ 0,017.
  - Le critère « $p<0{,}01$ » est donc inatteignable pour $k\le4$. À $k=5$, il exige un ordre parfait.
  - Le seuil $\rho\ge0{,}5$ est alors sans objet : c'est la p-valeur qui décide.

- **E2, fausses alertes sur 200 trajectoires (illustratif).**
  - Pour un candidat exactement au niveau ($\text{FPR}=\alpha=0{,}05$), la borne supérieure à 95 % est au plus égale à 0,07 seulement si le nombre d'alarmes est au plus 8 environ sur 200. Pour une loi binomiale de moyenne 10 et d'écart-type environ 3,1, cette probabilité vaut environ 0,31 (approximation normale, illustratif).
  - Dans environ 69 % des cas, un candidat valide tombe en zone grise : non jugeable.

- **E2, dérive due au style.** Pour que $|\Delta\text{FPR}_{\text{style}}|\le0{,}03$ soit jugeable, il faut que $1{,}96\sqrt{2\alpha(1-\alpha)/n}\ll0{,}03$, soit $n\gtrsim400$ par registre à $\alpha=0{,}05$ (calcul élémentaire, illustratif). C ne fixe pas ce $n$.

- **E4, effectif.**
  - Avec 100 trajectoires par bras non appariées et un taux de détection de base proche de 0,5, l'écart-type de Δ vaut environ 0,07. Δ = 0,12 donne alors une statistique z d'environ 1,7, soit $p\approx0{,}045$ (illustratif).
  - Le critère conjoint « Δ ≥ 0,12 et $p<0{,}01$ » est incompatible sauf appariement fortement corrélé (même trajectoire vue par chaque détecteur) ou Δ ≥ 0,17 environ.

- **E3.** L'écart $\Delta_{\text{gen}}$ perd sa puissance si la distance entre lois de familles (d'épreuve contre finales) sort de la plage où la boucle peut transférer. Il ne la regagne qu'en balayant ce paramètre.

- **Sas 0.** Le seuil de « corrélation des décisions » n'est pas spécifié, et la corrélation est confondue avec la difficulté (comme chez B). Le critère n'est pas jugeable en l'état.

- **Mondes-miroirs à alternative connue.** L'optimalité du rapport de vraisemblance (Neyman-Pearson, Wald-Wolfowitz) borne le gain possible sur une archive qui contient ce rapport. C est exposé au même artefact que B.

- **Oracle.** Les mêmes conditions que chez B s'appliquent : $p_s\to0$, et $p$ dépend du type de dommage à l'intérieur d'une strate.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Fiches-leurres en E1** : un bras reçoit des fiches décrivant des obstructions absentes des mondes-miroirs.
2. **Trois jeux honnêtes disjoints** : paramétrage des miroirs, sas 2.5, évaluation des fausses alertes en E4.
3. **Témoin de puissance au-delà de N sur honnêtes réels** (dommage planté, aucune famille consommée). Sans lui, E2 ne touche pas l'obstruction réelle.
4. **Témoin LLM passé par la même cascade** de sas, avec le même nombre de candidats générés.
5. **Placebo par recâblage qui préserve les degrés et les dates.**
6. **Extrémité « familles disjointes » en E3**, où les deux bras doivent échouer, en complément de l'extrémité i.i.d. déjà prévue.
7. **En E4, des honnêtes appariés issus d'une lignée de modèle non vue**. C la réserve à la vérification externe ; elle devrait aussi servir de contrôle interne au taux de fausses alertes.

---

## Expérience de discrimination issue de cette critique

Je reprends ici le défaut de fuite par spécification, présent chez C (fiches) et chez B (cahier des charges).

**Les deux hypothèses exclusives :**

- **H_A (connaissance transférable)** : le gain du bras qui a reçu les fiches persiste sur des obstructions tenues à l'écart. Ces obstructions sont conçues à l'aveugle des fiches et ne sont pas décrites aux bras.
- **H_B (appariement fiche-monde)** : le gain n'existe que sur les obstructions décrites.

**Plan :**

- Six familles de mondes-miroirs, notées $O_1$ à $O_6$ (illustratif). Seules $O_1$ à $O_3$ font l'objet de fiches. Les familles $O_4$ à $O_6$ sont produites par un générateur qui n'a vu aucune fiche.
- Trois bras à budget processeur égal :
  1. fiches vraies ;
  2. fiches-leurres ;
  3. aucune fiche.

**Métrique** : on calcule le rapport $R=\Delta_{O_{4..6}}/\Delta_{O_{1..3}}$. Ici, $\Delta$ est le gain de taux de détection du bras « fiches vraies » sur le bras « fiches-leurres », mesuré à taux de fausses alertes fixé.

**Variance** : elle est estimée entre familles, non entre trajectoires.

**Seuils et falsifications (illustratifs) :**

- $R\le0{,}2$ avec $\Delta_{O_{1..3}}>0$ falsifie H_A.
- $R\ge0{,}6$, avec un intervalle de confiance au-dessus de 0,2, falsifie H_B.
- Entre 0,2 et 0,6, l'issue est déclarée non concluante. Le nombre de familles est alors augmenté avant toute lecture du sas 3.

**Contrôles :**

- Contrôle négatif : le bras « fiches-leurres » doit rester proche de 0 sur $O_{1..6}$.
- Témoin positif : une base d'archive informée doit gagner sur $O_{1..3}$.

**Coût** : processeur seul, quelques dizaines d'heures-cœur (illustratif). Aucune famille de sabotage ni aucune lecture unique n'est consommée.

**Limite** : cette expérience ne dit rien du transfert vers les modèles ouverts de huit milliards de paramètres. Elle conditionne seulement l'interprétation de E1 (C) et de P1 (B).

FIN-DE-CELLULE