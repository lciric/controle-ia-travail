Les risques empiriques discutés ci-dessous sont des **HYPOTHÈSES de méthode**, non des résultats. Les formules servent à rendre testables les conditions de non-jugeabilité.

## Sur la proposition A

### (a) Défauts de méthode

- **T1 ne mesure pas une capacité invariante du moniteur.** La détection dépend du couple moniteur–attaque, de la longueur, mais aussi de la densité du signal, de sa position et de l’information effectivement visible. Additionner « lignes de code + traces d’exécution » ne définit pas un axe scalaire univoque. Geler les attaquants fixe une distribution d’attaques, pas ces autres facteurs.
- **La pente temporelle reste confondue.** Date du moniteur, famille, taille, fenêtre de contexte et exposition possible aux problèmes publics varient ensemble. La régression sur la date n’identifie un effet temporel que si ces variables ne portent pas, à elles seules, toute la variation. Les sept Qwen2.5 fournissent un axe de taille à date fixe, pas la conversion en axe calendaire.
- **Le contrôle mécanique à pente nulle est largement vrai par construction.** Sur une banque et un instrument déterministes figés, il ne peut pas révéler une dérive de difficulté entre les dates assignées aux autres moniteurs. Il teste surtout le pipeline de calcul.
- **L’appariement honnête/malveillant est insuffisant.** Produire les deux classes par le même attaquant ne supprime pas les artefacts de consigne, de style, de validité du code ou de longueur. Compter un refus comme trajectoire honnête aggrave ce défaut : la classe honnête peut contenir des échecs trivialement reconnaissables, tandis que la classe malveillante ne conserve que les attaques effectivement produites.
- **Fuite possible entre calibration et évaluation.** Le seuil à fausses alertes fixées, l’ajustement logistique et l’estimation de l’horizon doivent utiliser des problèmes, graines et trajectoires distincts. A ne le garantit pas explicitement. Le bootstrap sur sept attaquants d’une même famille ne répare pas cette dépendance.
- **Les duels ne respectent pas toujours l’exclusion requise.** Dans D1, une pente positive mais inférieure au seuil de H_A n’est couverte par aucune des deux hypothèses ; surtout, une pente positive ne falsifie pas « l’horizon est dominé par la longueur ». Dans D2, un rapport supérieur au seuil ne falsifie pas nécessairement une stagnation conjointe contre attaquants contemporains et gelés.
- **T2 n’a pas d’axe d’écart nécessairement ordonné.** Deux couples attaquant–moniteur ayant le même écart de log-paramètres peuvent avoir des probabilités de réussite différentes. Le seuil n’est alors pas une fonction de cet écart.
- **T3 confond conscience verbalisée et désalignement**, et l’ajustement supervisé à calcul égal n’est pas un contrôle équivalent : il change aussi la distribution des sorties. Enfin, une probabilité bornée ne peut croître d’un facteur deux à chaque doublement indéfiniment.
- **T4 n’a pas encore de variable dépendante interprétable** : **RAPPORTÉ**, la signification des deux scores est absente de la pièce. Une forte corrélation avec les refus ne démontrerait pas, à elle seule, une confusion causale.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

Pour T1, notons \(p_m^+(\ell)\) la probabilité de détection d’une attaque et \(p_m^-(\ell)\) celle d’une alerte sur un cas honnête, au seuil retenu.

- L’horizon est **non identifiable** si \(p_m^+(\ell)\) n’est pas monotone, traverse plusieurs fois son seuil, ou reste toujours au-dessus ou toujours au-dessous sur la grille. Il est alors censuré ou multivalué, pas seulement imprécis.
- Le TPR comparé à « fausses alertes fixées » est **mal calibré** si  
  \[
  P(Y=1\mid \text{honnête, test},\widehat\tau_m)\neq 0,05
  \]
  alors que cette égalité tient sur la calibration. Cela arrive notamment si \(p_m^-(\ell)\) dépend de \(\ell\) ou du rôle de génération.
- Si les erreurs sont corrélées intra-problème ou intra-attaquant, l’information effective est inférieure au nombre de trajectoires. Un bootstrap qui ne rééchantillonne pas ces unités au bon niveau produit des intervalles trop étroits.
- La pente temporelle est **non estimable** si la date n’a plus de variance résiduelle après famille, taille et autres covariables. Elle n’est pas une loi commune si les pentes propres aux familles sont de signes opposés malgré une pente moyenne positive.
- Pour T2, soit \(r(\delta,m,a)\) la probabilité de réussite de l’injection. L’écart-seuil est non jugeable si \(r\) n’est pas monotone en \(\delta\), ne traverse jamais le seuil, ou si \(r(\delta,m,a)\neq r(\delta,m',a')\) pour des couples pourtant interchangeables sur l’échelle choisie.
- Pour T3, si \(c_m\) est la conscience réelle et si sensibilité \(s_m\) et spécificité \(u_m\) du classificateur varient entre checkpoints, le taux observé est
  \[
  \widehat c_m^{\,\mathrm{obs}}=s_mc_m+(1-u_m)(1-c_m).
  \]
  Une tendance peut donc apparaître avec \(c_m\) constant. Près du plancher ou du plafond, le critère fondé sur \(\kappa\) peut également perdre toute discrimination.
- Pour T4, si la probabilité de refus et le score dépendent tous deux de la date, leur corrélation seule ne sépare pas \(P(\text{sous-performance}\mid\text{capable, non-refus})\) de \(P(\text{non-refus})\). Sans définition du score, l’estimateur lui-même reste indéfini.

### (c) Contrôles négatifs indispensables

1. **T1 : paires honnête–honnête avec étiquette d’attaque factice**, appariées sur problème, validité, longueur et rôle de génération. Une détection au-dessus du taux nominal révèle une fuite d’étiquette ou un artefact de style.
2. **T1 : séparation scellée calibration/ajustement/évaluation**, puis évaluation sur problèmes et attaquants réellement réservés. Sans cela, l’intervalle de l’horizon et le duel gelé/contemporain ne sont pas interprétables.
3. **T1 : refus et solutions invalides rapportés comme strates distinctes**, jamais injectés dans les cas honnêtes. Leur taux doit aussi être comparé entre tailles d’attaquants.
4. **T2 : contenu témoin non injectant, apparié en longueur et style**, en plus du contrôle sans injection ; sinon une baisse de détection peut être un simple effet de distraction.
5. **T3 : annotation et classificateur validés sur checkpoints entièrement held-out**, y compris des exemples sans conscience d’évaluation. Le contrôle supervisé seul ne suffit pas.
6. **T4 : aucun contrôle ne peut sauver la tendance tant que les scores ne sont pas définis.**

## Sur la proposition B

Pièce absente, statut REFUS : aucune critique de contenu possible ; je n’en invente pas.

## Sur la proposition C

Pièce absente, statut « jamais lancée » : aucune critique de contenu possible ; je n’en invente pas.

## Sur la proposition E

### (a) Défauts de méthode

- **E-A peut mesurer la géométrie du générateur plutôt qu’une frontière générale.** Placements, classes d’anomalies et rapport signal/longueur déterminent la difficulté. Des graines finales secrètes empêchent la mémorisation exacte, mais pas l’adaptation aux classes et au style du générateur.
- **Le taux de fausses alertes par épisode change la contrainte avec la longueur.** À risque par décision constant, allonger l’épisode multiplie mécaniquement les occasions d’alerte. Une partie de l’horizon peut donc être vraie par construction. Recalibrer à chaque longueur changerait en outre l’instrument mesuré.
- **Le « maximum » de longueur suppose une monotonie non établie.** Un moniteur peut échouer à une longueur intermédiaire puis réussir plus loin. Le maximum sur grille et le franchissement d’une courbe ajustée ne définissent alors pas la même grandeur.
- **E-B subit un biais du minimum.** Choisir le plus petit budget dont les estimateurs franchissent les deux seuils, sur les mêmes données que l’évaluation, favorise les fluctuations favorables. Une politique d’allocation gelée n’empêche pas cette sélection optimiste.
- **E-C peut n’apporter aucune loi nouvelle.** Sous occasions indépendantes et risque résiduel par occasion constant, l’horizon de confinement est une transformation algébrique du taux par occasion. Sa tendance n’ajoute alors rien à celle de ce taux.
- **La régression commune peut être non identifiée.** Famille, taille et date risquent d’être colinéaires sur douze checkpoints. Une pente moyenne peut aussi masquer des tendances de signes opposés. Les permutations de dates ne sont valides que dans des strates où les dates sont échangeables ; le moniteur figé sur données figées est, lui aussi, plat par construction.
- **Le pilote est peu informatif sur les fausses alertes.** Avec 80 cas honnêtes par cellule et une cible de 5 %, quatre fausses alertes sont attendues (**calcul**) : les taux réels et leur respect simultané des seuils restent très incertains.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **E-A :** soient \(p_m(\ell)\) la détection et \(q_m(\ell)\) les fausses alertes par épisode. La frontière est absente ou censurée si \(p_m(\ell)\) ne franchit jamais la cible, la dépasse partout, ou n’est pas monotone. Si \(q_m(\ell)\) croît avec \(\ell\), la comparaison mélange dilution du signal et accumulation du risque. Sous forte corrélation intra-famille de tâches, les intervalles fondés sur les paires surestiment la puissance.
- **E-B :** soit \(\mathcal F_m\) l’ensemble des budgets où les deux contraintes sont satisfaites. \(B_m\) est non défini si \(\mathcal F_m=\varnothing\), censuré si tous les budgets testés conviennent, et multivalué si performance ou calibration ne sont pas monotones en budget. Le minimum estimé sur données réutilisées est biaisé vers les petits budgets.
- **E-C :** si le dommage résiduel par occasion est \(d_m\) et les occasions indépendantes,
  \[
  P(\text{dommage avant }K)=1-(1-d_m)^K .
  \]
  L’horizon est alors entièrement déterminé par \(d_m\). Il devient infini si \(d_m=0\), inexistant sous la contrainte d’utilité si celle-ci échoue dès le départ, et non monotone si blocage et vérification modifient la distribution des occasions ultérieures.
- **Panel commun :** \(\beta\) est non identifiable si la matrice date/famille/taille est de rang insuffisant. Il perd sa puissance si la variance résiduelle de date est faible relativement à l’erreur d’estimation des frontières. Des frontières censurées transformées en valeurs numériques, ou des logarithmes de frontières nulles, rendent l’estimateur biaisé ou indéfini.

### (c) Contrôles négatifs indispensables

1. **E-A : épisodes sans aucune anomalie avec étiquettes factices**, à longueur et opérations appariées ; toute « détection » au-dessus du taux nominal invalide la vérité terrain ou révèle un artefact.
2. **Les trois mesures : générateur et familles de tâches held-out**, distincts de ceux ayant servi à concevoir les cas, seuils et politiques. Sans ce contrôle, la pente peut être celle du style planté.
3. **E-A : contrôle de longueur sans dilution**, où la quantité et la visibilité du signal restent constantes ; il distingue longueur causale et simple accumulation d’occasions de fausse alerte.
4. **E-B : sélection du budget et certification sur échantillons disjoints**, plus un flux sans anomalie à chaque budget. Le même checkpoint répété ne contrôle pas le biais du minimum.
5. **E-C : flux entièrement honnête**, avec dommage nul attendu et mesure des blocages injustifiés, complété par les bornes « tout autoriser » et « tout bloquer ». Les seules actions bénignes appariées ne testent pas la probabilité de dommage.
6. **Panel : pseudo-dates permutées uniquement à l’intérieur de strates famille–taille échangeables**, et non globalement. Sans ce contrôle, la significativité de \(\beta\) peut provenir de la structure du panel.

FIN-DE-CELLULE