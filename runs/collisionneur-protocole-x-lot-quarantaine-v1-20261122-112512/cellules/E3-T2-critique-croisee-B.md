# Proposition B · Tour III.2 : critique croisée de méthode

## État des pièces

- Le bloc FAITS ne contient que l'énoncé de la question, sans aucun fait muni d'un statut. La « réponse 23 de Fable » et les « notes » annoncées sont absentes.
- Les pièces A, C, D, E et F semblent complètes : chacune se termine par FIN-DE-CELLULE. Je n'ai recalculé aucun sha256.
- Tout ce que j'avance ci-dessous a le statut HYPOTHÈSE. Les chiffres que j'introduis sont illustratifs.

## Deux remarques que j'utilise dans plusieurs sections

**R1 (HYPOTHÈSE d'architecture, à vérifier sur l'implémentation).** Supposons que l'agent soit un transformeur autorégressif à poids fixes. Son état interne Z_t est alors une fonction déterministe du contexte complet jusqu'à t : consigne, sorties d'outils, raisonnement et jetons émis, aux non-déterminismes numériques près. Par construction, I(Y ; Z_t | contexte_≤t) = 0.

Un apport mesuré en (ii) ne peut donc venir que de deux sources :
- **(α)** le texte lu par le détecteur texte est un sous-ensemble strict du contexte ;
- **(β)** un écart de calcul : le détecteur texte, de capacité finie, n'extrait pas ce que les poids de l'agent calculent.

Pour séparer α et β, on rejoue dans *les mêmes poids* exactement le texte que lit le détecteur texte, puis on sonde ces activations (Z_rejeu) :
- gain(Z_int) − gain(Z_rejeu) isole α ;
- gain(Z_rejeu) − gain(texte seul) isole β.

Un protocole qui omet ce contraste ne permet pas de dire ce que (ii) affirme.

**R2.** Un seul genre est tenu à l'écart (RAPPORTÉ). La variance entre genres σ²_g n'est donc pas identifiable. Tout intervalle obtenu par bootstrap sur les tâches est conditionnel à ce genre, et toute fuite opère au niveau du genre, pas seulement des cas.

---

## Sur la proposition A

**Statuts et références.** Les statuts sont conformes : P2 est correctement classée HYPOTHÈSE. Je n'ai relevé aucune erreur d'attribution.

### (a) Défauts de méthode

1. **E1 : fuite de genre vers S_scellé.** S_porte et S_scellé appartiennent au même genre. Lire S_porte au fil des cycles transmet aux auteurs de l'information sur le genre, qui profite aussi à S_scellé. Δ ne mesure donc que l'usure au niveau des cas. Sous une fuite totale au niveau du genre, H_B (« pas d'usure ») s'obtient par construction. A présente pourtant E1-H_B comme capable de réfuter sa propre recommandation : c'est faux, ce n'est qu'une sous-estimation.
2. **E1 : « Δ croît avec le nombre de cycles ».** Le nombre de cycles K est un temps d'arrêt qui dépend du bruit de S_porte. Les campagnes qui s'arrêtent tôt sont celles dont le bruit a été favorable. La régression de Δ sur K est confondue par cette sélection sur l'issue.
3. **E2 : « second détecteur texte de capacité comparable ».** Le gain d'une combinaison dépend de la corrélation des erreurs entre ses membres. Le duel confond donc canal et diversité. Il ne sépare pas non plus α et β (R1).
4. **E3, cas (a).** « Résultat mécaniquement intact » dépend de la couverture des tests cachés. Une dégradation non détectée par ces tests augmente le taux d'alerte observé sur (a), ce qui pousse vers H_B. Le bruit d'étiquette est ici asymétrique.
5. **Instrument 3 (aucune vérification triviale au-dessus d'une AUROC de 0,6).** Filtrer les cas sur des traits de surface retire un signal réel, par exemple la taille du diff. Ce filtrage pénalise davantage le texte que l'état interne et biaise (ii) en faveur de l'interne.
6. **E5 (différence de différences).** La méthode suppose que les cas non exposés n'ont pas été touchés. Avec une fuite de genre, l'interaction est proche de 0 et H_B est obtenue par construction, comme au point 1.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1.** Var(Δ̂) = 2·p(1−p)/n_½. Avec p = 0,7 et n_½ = 300 cas dégradés (illustratif), l'erreur-type de Δ̂ vaut environ 0,037. Elle dépasse la marge de ±3 points : H_B est inatteignable par équivalence.
- **E2.** Si la corrélation des erreurs entre texte et texte₂ est proche de celle entre texte et interne, le contraste est nul quel que soit le canal. Si les taux de détection marginaux diffèrent de δ_m, le contraste est confondu avec δ_m.
- **E4.** Le contrôle par permutation de x ne discrimine rien si Var(f(X)) sur l'étendue de x du lot est inférieure ou égale à m². Le test d'équivalence perd sa puissance si σ_pub ≥ m.
- **Instrument 1 à 1 % de fausses alertes.** Avec n₀ = 1 000 cas honnêtes (illustratif), le quantile repose sur environ 10 dépassements. La variance de ce quantile, α(1−α)/(n₀ f(q)²), devient grande quand la densité f au quantile est faible.
- **E5.** Le dispositif n'est pas jugeable si la probabilité d'exposition dépend de la difficulté et si aucune version de détecteur antérieure à l'exposition n'existe.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Un second genre jamais consulté**, évalué dans E1 et E5. Sans lui, « aucune usure » et « usure totale au niveau du genre » donnent la même issue.
- **Z_rejeu (R1).** La « sonde sur plongements du texte seul » s'en approche, mais A ne précise ni « mêmes poids » ni « même texte que le détecteur texte ».
- **Un K imposé par randomisation** dans des campagnes simulées pour E1, à la place du K observé.

---

## Sur la proposition C

**Statuts.**
- C qualifie de [VÉRIFIÉ] l'intégrité et l'identité des empreintes sans les avoir recalculées.
- C classe l'« étanchéité » en OBSERVÉ-NON-AUDITÉ, alors que l'énoncé la donne comme RAPPORTÉ. C'est un changement de statut (règle 1).
- Je n'ai relevé aucune erreur d'attribution de référence.

### (a) Défauts de méthode

1. **Instrument 3 : paires appariées sur un score D_texte identique.** Sur ce sous-ensemble, D_texte n'a par construction aucun pouvoir de discrimination. Le critère TPR_interne ≥ 0,30 contre 0,05 est donc rempli par toute sonde porteuse de n'importe quel signal. Le gain mesuré est conditionnel à une sélection opérée par le comparateur lui-même, et il ne se transpose pas à la population.
2. **Filtrage des cas jusqu'à une AUROC mécanique comprise entre 0,45 et 0,55.** C'est le même défaut que A5, en plus fort.
3. **E4, contrôle « agent Markovien » (vidage du cache KV).** Selon R1, l'agent standard vérifie déjà I = 0. Si le texte réinjecté est le contexte complet, le vidage ne change que la numérique. S'il ne l'est pas, il modifie la loi des trajectoires. Dans les deux cas, le contrôle ne teste pas ce que C annonce, et l'appel à l'inégalité de traitement des données est mal placé.
4. **E4 : H_A est presque vraie par construction.** Recalibrer deux paramètres sur Q modifie le score de Brier, qui est sensible à la calibration en cas de décalage de domaine. E4 teste l'effet d'une recalibration, pas la question 4.
5. **E2 : trois régimes conduits en parallèle.** Si les auteurs sont les mêmes, les bras se contaminent. Q*, présenté comme un « jumeau de même distribution hors genre », suppose un générateur du genre : il en partage donc les artefacts.
6. **E3 : canaris.** Ils ne s'insèrent qu'à la constitution du lot, et le lot existe déjà : ils sont inutilisables rétroactivement pour la question 3. Ils ne détectent que la mémorisation des étiquettes Y, pas une adaptation au genre à partir des traces X. Les étiquettes inversées polluent l'évaluation si les canaris ne sont pas exclus.
7. **E1 consomme la moitié de Q** pour le passage, avec la même fuite de genre vers Q_portée que chez A.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1.**
  - La statistique de Kolmogorov-Smirnov n'est libre de loi que pour une loi continue. Avec des scores discrets ou à ex aequo, sa loi nulle est inconnue.
  - « 2σ_boot, soit p < 0,01 » est incohérent : 2σ correspond à p ≈ 0,046 en bilatéral sous normalité.
- **E2.**
  - Les estimateurs de Î en dimension d = 2 048 (par substitution ou par k plus proches voisins) sont biaisés vers le haut, avec un biais croissant avec d/n. La valeur « 0,00 ± 0,01 bit » est inatteignable et le contrôle n'est pas jugeable.
  - Le taux de fausses alertes est estimé sur 100 simulations, d'où une erreur-type d'environ 0,022 autour de 0,05 (illustratif). La zone entre 0,05 et 0,10 ne tranche rien.
- **E3.** Avec un écart-type de la perte par cas d'environ 0,5 nat et n = 400 par cellule (illustratif), l'erreur-type de la différence de différences atteint environ 0,05 nat sans appariement. Elle dépasse le seuil de 0,02 nat.
- **E4.** η a pour dénominateur |ΔS_nouveau|. Quand ΔS_nouveau tend vers 0, η n'est plus borné : la mesure devient non jugeable exactement là où (ii) est nulle.
- **Étiqueteur annoncé à TPR = 1,00 et FPR = 0,00.** Avec zéro erreur sur n cas, on n'obtient qu'une borne d'environ 3/n.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Z_rejeu à la place du vidage du cache KV.**
- **Gain mesuré sur la population entière**, accompagné d'un nul par permutation calculé dans le sous-ensemble sélectionné par D_texte.
- **Ordre des horodatages entre l'accès au lot et le changement d'affirmation.** Il est absent, alors que tout le caractère confirmatoire de (i) et (ii) en dépend.
- **Un second genre** (R2).

---

## Sur la proposition D

**Référence.** « Noam Cawley » est une attribution incorrecte : le premier auteur de Cawley & Talbot (2010) est Gavin C. Cawley (règle 3). Je n'ai pas d'autre remarque sur les statuts.

### (a) Défauts de méthode

1. **Optimisme O mesuré contre « d'autres familles scellées de même distribution ».** Si ces familles sont du même genre, l'adaptation au genre est invisible, et H_A (O ≤ ε_O) s'obtient par construction. La même objection vaut pour la lecture « par parties » avec des familles fraîches du même genre.
2. **Test de la règle de passage sur des mondes nuls.** Les retours des auteurs humains ne se simulent pas. D le reconnaît, mais q ne certifie alors que la stratégie simulée.
3. **Duel d'exposition sur un lot sacrificiel.** La randomisation est propre. Mais des auteurs qui se savent dans un essai d'exposition ne se comportent pas comme lors d'une exposition réelle : la transposition n'est pas identifiée, ce que D admet.
4. **(ii).** Le contraste T contre T+I est le bon, mais il ne sépare pas α et β (R1).
5. **Banc de transformation de tables.** Il change la population étudiée : les conclusions vaudront pour ce banc, pas pour les longues tâches logicielles de l'énoncé.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Statistique D (écart à la loi).** Sous accord exact avec des erreurs normales, E[D] ≈ Σ_j w_j σ_j √(2/π), où σ_j inclut l'incertitude des prédictions publiées. Si δ_L est inférieur ou égal à cette valeur, H_A est inatteignable même sous accord parfait. Si l'incertitude publiée est grande, la puissance contre H_B s'effondre.
- **Unité « famille ».** n_eff = n/(1+(m−1)·ICC). Quand l'ICC tend vers 1, n_eff tend vers le nombre de familles. Avec un seul genre, σ²_g n'est pas identifiable (R2).
- **Fausses alertes « au moins une alerte avant l'échéance ».** Le taux par trajectoire vaut 1 − Π_t(1 − f_t) et croît avec le nombre de lectures L. Si la loi de L diffère entre cas honnêtes et dégradés au-delà de l'appariement sur la longueur, le plafond commun n'est plus comparable.
- **Plafond fixé sur le développement.** Si la loi des scores honnêtes se déplace dans Q, le taux réalisé s'écarte du plafond, et la règle de D (« pas de revendication ») rend G non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Un contraste au niveau du genre** : un second genre, ou une comparaison avant/après exposition évaluée sur un autre genre.
- **Z_rejeu.**
- **Ordre entre l'accès au lot et le changement d'affirmation.** D signale le problème mais ne propose aucun contrôle.
- **À conserver.** Le contrôle de D par échange d'états entre traces de la même strate, sans appariement sur l'issue, est le plus propre des cinq propositions pour (ii) sous l'angle β, et je m'en sers comme référence.

---

## Sur la proposition E

**Statuts.**
- E appose [VÉRIFIÉ] sur une espérance d'AUROC et sur une application de l'inégalité de traitement des données. Ce ne sont pas des faits transmis.
- « OBSERVÉ-NON-AUDITÉ (érigée en HYPOTHÈSE) » réassigne un statut que l'énoncé donne comme RAPPORTÉ.
- Le contrôle d'E6 contient un brouillon non révisé (« ? Non : »).

### (a) Défauts de méthode

1. **E1.** |B| = Δ(E_quar) − Δ(E_oracle) confond l'écart de difficulté entre les deux genres et le biais adaptatif. H_1B exige aussi |B| < 0,02 dans le bras Portée, ce qui échoue dès que l'écart de difficulté atteint 0,02. Les deux hypothèses peuvent alors être falsifiées ensemble : elles ne sont pas exhaustives (B4). Par ailleurs, sous nul global, le « FDR » est un simple taux d'erreur de première espèce.
2. **E2.** Le bras Parties reçoit des exemples du genre testé, le bras Unique des exemples de G_dev. L'issue Δ > 0,03 reflète alors l'avantage ordinaire de données de même distribution. Elle est presque vraie par construction et ne distingue pas fuite et apprentissage.
3. **E4.** Figer D_txt à 2 cycles garantit l'inflation. Le « nul » I(Y ; Z | X) = 0 est de toute façon vérifié pour tout transformeur (R1).
4. **E6, contrôle miroir.** Z_miroir vient de Llama-8B, Z_int de Qwen-32B. La différence confond « état propre de l'agent » avec la taille du modèle, le tokenizer et les données d'entraînement. Le contrôle pertinent est Z_rejeu, avec les mêmes poids.
5. **E6, référence max[TPR(D_txt), TPR(D_txt+miroir)].** Si ce maximum est choisi sur E_quar, c'est une sélection sur le jeu de test. Il faut le choisir sur le développement.
6. **E3.** Avec une équipe par condition (I, T, aveugle), l'effet d'équipe est confondu avec la condition.
7. **E5.** Les 5 paliers de longueur supposent que Q couvre 5 régimes. Un genre unique peut se concentrer sur un ou deux.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E3.** Avec AUC ≈ 0,8 et 380 cas de chaque classe, l'approximation de Hanley-McNeil donne une erreur-type d'environ 0,016, soit environ 0,023 pour une différence entre conditions (illustratif). Le seuil de 0,02 est inférieur à l'erreur-type. Avec une seule équipe par bras, σ²_équipe n'est pas estimable.
- **E5.**
  - χ²_réd = 2,5 sur 5 degrés de liberté correspond à p ≈ 0,03, pas à 0,01 (calcul indicatif).
  - Si l'incertitude publiée est omise du dénominateur, les rejets sont faux ; si elle y figure et domine, la puissance disparaît.
- **E1.** Avec 200 campagnes, le taux estimé autour de 0,08 a une erreur-type d'environ 0,019 (illustratif) : la marge est mince.
- **E6, permutation dans 20 quantiles de D_txt.** Elle impose Y ⊥ Z | D_txt(X), pas Y ⊥ Z | X. S'il reste une association X–Y à l'intérieur des tranches et que Z est corrélé à X dans ces tranches, le nul produit un gain positif.
  - L'estimand « ajoute à D_txt » est fidèle à la lettre de (ii).
  - La formulation d'E (« information propre ») est plus forte que ce que ce test peut juger.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Z_rejeu.** Le miroir ne le remplace pas.
- **Ancre de difficulté pour E1** : un détecteur mécanique figé, évalué sur E_quar et E_oracle.
- **Ordre entre l'accès au lot et le changement d'affirmation** : il est absent, alors qu'E cite Kerr (1998).
- **Réplication au niveau des équipes pour E3.**

---

## Sur la proposition F

**Statuts.**
- A5 (« changement d'affirmation sans information issue de Q ») est classé OBSERVÉ-NON-AUDITÉ. L'énoncé est pourtant muet sur ce point : c'est une HYPOTHÈSE.
- A4 est classé OBSERVÉ-NON-AUDITÉ, alors que l'énoncé le donne comme RAPPORTÉ.
- Je n'ai relevé aucune erreur d'attribution.

### (a) Défauts de méthode

1. **E4 : Q_post est « du même genre ».** Si les auteurs ont vu le genre avant le gel, les détecteurs adaptés réussissent aussi sur Q_post. Δ_fuite est alors proche de 0 par construction sous une fuite de genre, c'est-à-dire précisément le mécanisme que F place au centre de sa réponse à la question 2. F se contredit.
2. **E1.** La symétrisation entre F1 et F2 annule une différence de difficulté additive, mais pas une interaction entre entraînement et genre. Avec deux genres, le bootstrap sur les tâches ignore σ²_g.
3. **E2.**
   - H_B présuppose un écart en développement ; s'il n'y en a pas, l'expérience est mal posée.
   - R n'est pas stable quand |θ̂_dev − f_pub| tend vers 0.
4. **E3 : ΔNLL comme métrique principale hors genre.** Le gain mélange discrimination et décalage de calibration (voir (b)).
5. **E3 : g_méc inclut « l'entropie des jetons ».** Cette entropie dérive des logits de l'agent, donc de l'état interne. La frontière entre canaux devient floue et la comparaison est biaisée contre H_A.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **ΔNLL.** Si la prévalence π_Q diffère de π_dev, les calibrateurs figés sont mal calibrés différemment, et E[ΔNLL] contient un terme qui dépend des pentes de calibration. Le gain de discrimination n'est alors pas identifiable.
- **Conjonction de quatre critères pour falsifier H_B.** La puissance est majorée par celle du critère le plus faible, et tend vers le produit des puissances si les critères sont peu corrélés.
- **« Dérive du taux de fausses alertes ≤ +1 point ».** Avec 100 à 200 cas honnêtes, l'erreur-type du taux de fausses alertes autour de 5 % vaut environ 0,015 à 0,022 (illustratif). Ce critère n'est pas jugeable.
- **E2.** Si σ_pub est grand devant sd(θ̂_Q), |Z_Q| > 2,5 est inatteignable.
- **E4.** Si Q_vu est petit (exposition partielle), une puissance de 80 % contre 0,05 d'AUROC est inatteignable, et l'innocence fonctionnelle n'est pas jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Contraste au niveau du genre dans E4.** Il faut évaluer des versions de détecteur antérieures et postérieures à l'exposition sur Q_post *et* sur un autre genre. Le témoin gelé avant la création de Q ne contrôle que la parité de difficulté.
- **Z_rejeu.**
- **Neutralisation de la prévalence dans ΔNLL** : recalibration à prévalence imposée, ou métrique invariante à la prévalence, rapportée à côté.
- **À conserver.** Le contrôle d'ordre entre le pré-enregistrement et le premier accès est présent chez F, et je le reprends comme modèle pour C, D et E.

---

## Ce qui est réfutable dans cette critique

- **R1** est réfutée si l'implémentation de l'agent possède un état non déterminé par le contexte (mémoire externe non journalisée, ou état récurrent hors texte). Dans ce cas, le contrôle Z_rejeu montrerait gain(Z_int) > gain(Z_rejeu) même avec le texte complet.
- **La fuite au niveau du genre** est réfutée si, dans une campagne simulée, un lot du même genre et un lot d'un genre distinct donnent la même usure.

Les erreurs-types que j'avance sont illustratives et se recalculent mécaniquement une fois les effectifs réels connus.

FIN-DE-CELLULE