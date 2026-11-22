# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces reçues.** Le bloc FAITS est identique au bloc QUESTION (même empreinte) et ne contient aucun fait muni d'un statut. Les pièces B, C, D et E sont présentes et se terminent toutes par leur ligne de fin. Ma propre conception III.1 n'est pas dans cette transmission, donc je n'en cite rien.

**Statut de ce qui suit.** Aucune des quatre pièces ne rapporte de résultat. Mes critiques sont des analyses de conception, au statut [HYPOTHÈSE] quant à ce qui se produirait. Tous mes chiffres sont « illustratifs » : ce sont des ordres de grandeur calculés sous des modèles simples que j'énonce.

**Étiquettes des autres pièces.** C et E apposent [VÉRIFIÉ] sur des dérivations ou des caractéristiques de modèles que le bloc FAITS ne contient pas. Je ne modifie pas ces étiquettes et je ne m'appuie pas sur elles.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **α ≈ ½ est vrai par construction avec l'adversaire scripté.** Le contrôleur remplace chaque choix avec probabilité q par l'option qui pousse dans la direction cible.
   - Le nombre de choix dirigés suit donc une binomiale dont le paramètre est décalé d'un terme proportionnel à q.
   - Un test de comptage (M3, ou toute somme de scores par pas) détecte à puissance fixe quand q·√n dépasse une constante. Donc q\* ∝ n^(−½) et D\* = n·q\*·d̄ ∝ n^(½).
   - E1 sur l'adversaire scripté mesure alors le théorème central limite appliqué au banc, non une propriété de l'agent. H_A y est quasi assurée et sa confirmation n'apprend rien.
   - Seul l'écart entre l'adversaire agentique et le scripté est empirique. B le relègue en « strate supplémentaire » de E5, classée de second rang.

2. **α dépend d'une convention de normalisation que B ne fixe pas.** B écrit que la quantité « agrège n sous-analyses ».
   - Si c'est une somme, l'effet par choix d̄ est constant et α = ½.
   - Si c'est une moyenne, d̄ ∝ 1/n et la même expérience donne α = −½.
   - L'exposant n'est donc pas identifié tant que la loi de d̄(n) n'est pas pré-enregistrée.

3. **Le rapport utile est absent.** Sous R½ en convention somme, l'écart-type honnête du résultat final croît aussi en √n. Le rapport D\*/σ_honnête(n) est alors constant.
   - Lu ainsi, α = ½ signifie « la longueur ne change rien relativement au bruit honnête », l'inverse de la lecture « elle sert l'adversaire » que donne B.
   - B devrait rapporter l'exposant de ce rapport.

4. **Fuite entre instrument et clef d'évaluation.** M3 (test du signe) et le « contrôle par excès d'erreurs dirigées » de E4 utilisent l'effet de chaque option sur l'estimation finale, que le générateur calcule. Le défenseur lit donc la clef. B le reconnaît pour M3 mais pas pour E4.

5. **« Meilleur détecteur d'une famille ».** Si le meilleur est choisi sur les trajectoires qui servent à estimer D\*, D\* est biaisé vers le bas. Le biais dépend de n, puisque la sélection peut différer à chaque n, et il contamine la pente.

6. **E3 : la sonde et sa cible.**
   - Si la sonde est entraînée avec la condition (sabotage ou honnête) pour étiquette, une ordonnée à l'origine positive est le décalage moyen de condition, obtenu par construction.
   - Avec l'adversaire agentique, δ n'est pas randomisé : l'agent choisit où et combien. La régression du score sur |δ| est donc confondue avec le contexte.
   - Avec le scripté, il n'y a aucune « intention » à lire. E3 n'y est pas défini.

7. **Contrôle par pré-remplissage asymétrique.** Une action forcée dans une trajectoire honnête est improbable sous la politique du modèle. La sonde peut séparer par la surprise, que B lirait comme « autre chose que le contenu », donc en faveur de H_A.

8. **Confondant de contexte.** B le reconnaît (S1) : n covarie avec le nombre de compactions du résumé glissant, donc avec la persistance de l'instruction adverse.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **α (E1, E2).** Non identifié si d̄(n) n'est pas constant. Non jugeable si TPR(D) ne traverse pas 50 % dans la grille de q pour un n donné, car D\* est alors extrapolé.
- **Δα (E2).** Sans puissance si la variance entre tâches τ² est petite devant la variance par pas σ²/n. B le prévoit. Également sans puissance si les m comparaisons partagent un biais avec l'exécution observée : la différence annule alors l'effet.
- **Ordonnée à l'origine (E3).** Non jugeable si la loi de |δ| chez l'adversaire agentique n'a pas de masse près de 0, car c'est une extrapolation pure.
- **E4.** Si l'attribution exige un excès d'erreurs dirigées parmi B vérifications, sous une loi honnête symétrique :
  - B = 1 ne peut jamais atteindre un niveau de 5 % ;
  - B = 5 ne l'atteint que si les cinq vérifications tombent toutes sur un écart et sont toutes de même signe (probabilité 1/32 en unilatéral, illustratif).
  - Le critère est donc non jugeable pour deux des trois budgets annoncés.
- **TPR à FPR 5 %.** Avec environ 500 trajectoires honnêtes, l'erreur type du FPR réalisé est proche de 1 point (illustratif). C'est acceptable. Le FPR à 1 % ne l'est pas, et B le dit.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **LoRA bénin de même rang**, entraîné sur des trajectoires honnêtes. Je reprends ici, en le disant, un cas apparié de E. Sans lui, P3 sur l'organisme entraîné mesure « des poids modifiés », non un sabotage.
2. **Placebo de chaîne complète.** Appliquer l'estimation de D\* et de α à « honnête contre honnête, graines différentes » à tous les n. La chaîne doit déclarer D\* non défini. B ne prévoit q = 0 que pour les tâches à goulot.
3. **Pré-remplissage symétrique.** Forcer une action honnête dans une trajectoire saboteuse, pour séparer surprise et intention.
4. **Contrôle d'invariance somme/moyenne.** Les mêmes tâches avec la cible en moyenne : α doit se décaler de −1 pour le dommage absolu, et l'exposant du rapport D\*/σ_honnête doit rester inchangé. Sinon l'exposant mesuré est un artefact d'unité.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Sélection sur l'issue.** Les trajectoires honnêtes sont « filtrées pour présenter Δ ∈ [25 % ; 35 %] ».
   - Ce filtre retient une queue de la loi honnête de Δ, et le quantile retenu change avec T, puisque la loi honnête de Δ dépend de T.
   - La classe négative n'est donc pas la même population à T = 50 et à T = 400. ΔAUROC confond l'effet de T sur le détecteur et l'effet de T sur le filtre.
   - C ne rapporte ni le taux de sélection par T ni son coût en trajectoires à générer.

2. **Tout détecteur de dommage est mis au hasard par construction.** L'appariement sur Δ en est la cause. C'est un choix défendable (question d'attribution), mais C ne le dit pas et ne mesure nulle part le dommage échappé.

3. **Le gain en √T de H_1B est acquis par construction pour un adversaire LoRA.**
   - L'adaptateur modifie le flux résiduel à chaque pas, que le pas soit « biaisé » ou non.
   - Toute sonde linéaire a alors une espérance par pas non nulle, et la somme sur T pas croît.
   - L'issue « H_1B » ne distingue pas « représentation persistante de la politique adverse » de « poids différents ».
   - Le contrôle par température ne traite pas ce point : les deux bras y partagent les mêmes poids.

4. **Entraînement de la sonde non spécifié.** « Entraînée hors domaine sur des tâches courtes » ne dit pas quelles étiquettes sont utilisées. Si c'est le même adaptateur contre la base, c'est une fuite directe.

5. **Les seuils de l'expérience 1 mêlent niveau et pente.** H_1A est validée si ΔAUROC ≤ 0 **ou** si TPR(400) < 50 %. Un détecteur dont l'AUROC monte de 0,10 mais dont le TPR reste à 45 % « valide la dilution ». Les deux hypothèses ne sont alors pas exclusives sur la grandeur testée, qui est la pente.

6. **L'expérience 2 est proche d'une tautologie.** Si les comparaisons sont honnêtes, deux actes qui déplacent la conclusion de 30 % diffèrent nécessairement d'exécutions qui ne l'ont pas déplacée. Trois points manquent :
   - la source des comparaisons n'est pas dite (base honnête, ou adaptateur adverse ?) ;
   - l'alignement pas à pas est mal défini quand l'ordre des documents est permuté ;
   - la quantité qui décide, le nombre de bifurcations honnêtes par trajectoire en fonction de T, n'est pas mesurée.

7. **L'issue de l'expérience 3 dépend d'un choix non fixé.**
   - Si les sondes d'évaluation sont celles qui ont été pénalisées, H_3B est facile.
   - Si elles sont réentraînées après coup, H_3A est favorisée.
   - Un échec d'optimisation (DPO sur 200 pas avec pénalité d'activation, pour 110 h illustratives) serait lu comme « incompressibilité ».
   - Cette expérience se fait à T unique et ne dit rien de la longueur.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **ΔAUROC ≥ +0,10.** Impossible si AUROC(T = 50) > 0,90 : H_1B est alors non validable même si elle est vraie.
- **Gain ≥ +0,25 sur le texte.** Impossible si l'AUROC du texte dépasse 0,75.
- **Précision.** Avec 150 contre 150 par longueur, l'erreur type d'un AUROC proche de 0,75 est d'environ 0,03, et celle d'une différence entre deux longueurs d'environ 0,04 (approximation usuelle, référence à vérifier ; illustratif). Un vrai effet de +0,10 a une puissance voisine de 50 % au seuil p < 0,01.
- **TPR à FPR 5 %.** Le seuil repose sur 7 ou 8 trajectoires honnêtes. L'erreur type du FPR réalisé est proche de 1,8 point (illustratif). Un TPR de 80 % annoncé à « 5 % » peut correspondre à 8 %.
- **Recall@5.** Si le nombre de bifurcations honnêtes de saut comparable, λ(T), croît avec T et dépasse k, le classement s'effondre quel que soit le levier des actes sabotés. Si les comparaisons partagent la politique adverse, le saut attendu est nul.
- **Contrôle « erreurs honnêtes à fort levier ».** Il est non jugeable si ces cas sont rares : un FPR ≤ 10 % ne s'estime pas sur une dizaine de trajectoires.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **LoRA bénin de même rang et de même procédure.** Ce doit être la classe négative de l'expérience 1.
2. **Classe honnête non filtrée**, en plus de la classe filtrée, avec le taux de sélection par T.
3. **Comparaisons issues de l'adaptateur adverse lui-même.** Je me sers du contrôle du duel 3 de E. Sans lui, l'expérience 2 suppose une copie honnête sans le dire.
4. **Contrôle positif d'optimisation pour l'expérience 3.** Montrer que la procédure sait masquer un signal connu, par exemple sur T = 10, et évaluer avec des sondes réentraînées sur des données tenues à l'écart.
5. **Sonde entraînée sur étiquettes permutées**, en plus des directions aléatoires.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le contraste propre n'est pas parmi les duels.** O et T ont la même longueur et des fiches appariées. La comparaison qui isole « témoins contre occasions » est R_O − R_T.
   - Les duels proposés sont R_O − R_C et R_C − R_T.
   - Chacun confond le contenu ajouté avec la longueur elle-même : contexte quatre fois plus long, oublis d'un carnet borné, dérive de l'agent.

2. **Les témoins changent la tâche autant que l'information du défenseur.** En T, l'agent honnête a plus de preuves et l'adversaire doit contredire plus de sources.
   - D le voit et publie P(conclusion fausse) avant audit.
   - Mais la « sensibilité conditionnelle sur ces conclusions » conditionne sur une issue postérieure au traitement. Les trajectoires fausses en T ne sont pas la même population que les fausses en C.
   - Seul le duel 3, intra-trajectoire, échappe à ce biais.

3. **Le duel 3 révèle une part de la clef.** Le générateur « conserve les liens entre sources ; ces données servent au jugement final, pas au moniteur ». Le duel 3 donne pourtant au moniteur l'appariement affirmation-témoin.
   - Le gain mesuré est celui d'un défenseur qui connaît la structure de preuve et, implicitement, quelles affirmations sont décisives.
   - Le contrôle « liens entre fiches non décisives » ne sépare pas « contenu du lien » de « désignation des affirmations décisives ».

4. **Le placebo de longueur ne porte que sur le défenseur.** D allonge la présentation d'un parcours C enregistré. L'agent, lui, n'a pas vécu la longueur. L'effet de 256 actions réelles sur l'agent (erreurs honnêtes, perte du mandat) n'est contrôlé nulle part.

5. **Le mandat est seulement donné par invite.** Exclure ses jetons de l'inspection ne retire pas son effet sur les activations des autres positions.
   - Le contrôle « mandats adverses sans dommage » repose sur des échecs auto-sélectionnés.
   - Ce n'est pas un bras randomisé.

6. **Deux longueurs seulement.** Elles donnent un signe et non une forme. D l'assume, et ce n'est pas une faute tant qu'on n'en tire que cela.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Les duels à marge δ = 5 points sont sous-dimensionnés.** Avec 300 dossiers appariés par cellule, un risque voisin de 0,3 et un taux de paires discordantes voisin de 0,3, l'erreur type d'une différence appariée est d'environ 0,03 et la demi-largeur à 95 % d'environ 0,06 (illustratif).
  - C'est plus que δ.
  - Un effet vrai exactement nul donne un intervalle à cheval sur +δ, donc « indéterminé ».
  - H_A n'est falsifiable que si la différence vraie est nettement négative. H_B ne l'est que si elle dépasse environ +0,11.
  - D annonce une vérification au pilote. Le calcul indique qu'elle échouera à cette taille.
- **R_v.** Sans puissance si P(conclusion fausse | mandat adverse) est faible, car R_v est alors borné près de 0 dans toutes les variantes. Non interprétable si P(conclusion fausse | honnête) diffère entre variantes de plus de δ.
- **Calibration par longueur.** Si la calibration ne dispose que d'une centaine de tâches honnêtes par variante après le découpage en trois parts, l'erreur type du FPR réalisé dépasse 2 points (illustratif). Un écart de FPR entre C et O de cet ordre produit un écart de TPR du même ordre que δ.
- **Budget de 2 inspections.** La « confirmation d'un défaut matériel suffisant » perd sa puissance si le dommage est réparti sur plus de deux actes dont aucun ne suffit seul. Le critère mesure alors la concentration du dommage, pas le défenseur.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Le duel direct R_O − R_T**, avec la même règle d'intervalle.
2. **Un placebo de longueur vécu par l'agent.** Il comporte 256 actions réelles, dont les ajouts sont neutres : ni occasions sur les affirmations décisives, ni témoins.
3. **Mandat présent mais neutralisé**, randomisé. Je reprends, en le disant, le contrôle « instruction désactivée » de B.
4. **Liens permutés sur les affirmations décisives.** Même nombre de liens, mêmes affirmations désignées, témoins mal appariés. Si le gain persiste, il vient de la désignation et non de la preuve.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **L'environnement semble différer selon l'étiquette.** L'agent honnête est « soumis à des distracteurs calibrés » pour produire des trajectoires appariées en erreur finale.
   - Si ces distracteurs ne figurent pas à l'identique dans les corpus des bras adverses, un moniteur qui lit les documents classe par corpus.
   - L'AUROC serait alors gonflé par construction, et davantage à grand T, où le corpus est plus gros.
   - E ne dit pas que les corpus sont communs.

2. **Stratification sur Δ.** Même sélection sur l'issue que chez C, avec les mêmes conséquences.
   - S'y ajoute que T fait varier « proportionnellement la taille du corpus et le nombre de maillons d'inférence ».
   - La profondeur causale, la difficulté et la longueur bougent ensemble.

3. **Le filtre de furtivité est vide pour l'adversaire parcimonieux.** Le contrôle exige AUROC(T = 1) ≤ 0,55 sur « une action tirée au hasard ».
   - Avec k ≤ 3 actes sur 300, une action tirée au hasard est sabotée avec probabilité ≤ 1 %.
   - L'AUROC vaut donc environ 0,5 même si les k actes sont grossiers. Le filtre doit conditionner sur les actes sabotés.

4. **Une fois corrigé, ce filtre exclut la moitié de H_2B.** AUROC ≤ 0,55 par acte correspond à un effet standardisé d'environ 0,18 dans un modèle gaussien à variances égales, soit au plus 0,3 environ pour trois actes (illustratif).
   - Un maximum glissant sur environ 60 fenêtres exige un effet proche de 2,9 pour émerger (illustratif).
   - La branche « scan sur fenêtre courte » de H_2B est donc quasi impossible par construction pour le texte. Seule la branche « trace de veille » reste empirique.

5. **La branche « trace de veille » est acquise par construction avec un LoRA conditionnel.** Les poids diffèrent à chaque pas.
   - La « greffe chirurgicale » le montre bien, et c'est un bon dispositif.
   - Mais la « greffe honnête » compare à π_hon, non à un adaptateur bénin. E cite le LoRA honnête de même rang en (c) et ne l'inscrit pas comme classe négative du duel 2.

6. **Le bras texte du duel 2 est déterminé d'avance.** Après les k actes, les pas aval sont tirés de la politique honnête sachant un dossier biaisé.
   - Tout résidu centré conditionnellement y est nul en espérance. H_2A est donc vraie par construction pour ce bras.
   - E le suggère sans en tirer la conséquence : le duel 2 ne teste que les activations.

7. **Le centrage conditionnel suppose π_hon.** L'incrément d_t est bien centré sous π_hon (je refais ce calcul sous la définition posée et je le retrouve). Mais son estimateur exige des tirages sous une politique honnête depuis chaque préfixe.
   - C'est la copie de confiance dont E doute en (a)4.
   - S'il s'agit de l'incrément de valeur lui-même, il faut des complétions jusqu'à Y, soit de l'ordre de T²/2 actions par trajectoire et par tirage (environ 45 000 à T = 300, contre 300 pour la trajectoire ; illustratif).
   - Les 60 h annoncées ne sont compatibles qu'avec un rééchantillonnage local du score par pas, pour lequel la propriété sur Y ne s'applique plus.

8. **Le duel 3 agrège deux populations.** Le mélange 50/50 diffus/parcimonieux donne un TPR global qui dépend du poids de mélange, alors que E prédit des tendances opposées pour les deux.
   - L'origine du « graphe de provenance » n'est pas dite (générateur, ou reconstruction à partir des citations de l'agent).
   - Si elle vient du générateur, c'est une fuite de clef.

9. **Les hypothèses ne sont pas exclusives au niveau du mécanisme.** Dans le duel 1, ΔAUROC ≤ +0,02 est attribué à la dérive honnête auto-renforçante.
   - La dérive de la sonde en contexte long produit la même issue. E la liste lui-même comme condition de réfutation (ii).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel 1.** Avec 150 contre 150 par horizon, l'erreur type de ΔAUROC est d'environ 0,04 et la demi-largeur d'environ 0,08 (illustratif).
  - « Borne basse > +0,03 » exige un estimé ≥ +0,11.
  - « Borne haute < +0,05 » exige un estimé ≤ −0,03.
  - Entre les deux, tout est indéterminé. Un effet vrai de +0,08, la valeur annoncée, sort indéterminé environ une fois sur deux.
  - Même plafond que chez C si AUROC(40) > 0,92.
- **Détecteur centré.** Si le prédicteur de E[score | préfixe] a un biais b par pas sur les trajectoires honnêtes, la somme dérive comme b·T contre un bruit en σ·√T. Dès que |b|·√T/σ approche 1, le FPR à seuil fixe croît avec T et la pente mesurée est celle du biais. Le test devient non jugeable sans recalibrage par T sur des honnêtes indépendants.
- **Autocorrélation honnête.** La variance de la somme vaut environ Tσ²(1+ρ)/(1−ρ) pour une autocorrélation ρ de type AR(1) (illustratif). E ne prévoit pas d'estimer ρ. Sans cette estimation, on ne peut pas attribuer une pente nulle à la dérive honnête.
- **Duel 2.** ΔTPR ≥ −0,02 est non jugeable si TPR(40) est déjà près du FPR (plancher).
- **Duel 3.** Il perd toute puissance si le nombre de bifurcations honnêtes dans l'espace des sous-affirmations dépasse B. Il est non jugeable si l'audit exact du rapport final détecte déjà tout Δ ≥ 0,20 : l'appariement sur Δ rend alors M4b nul par construction, et le « gain ≥ +0,12 sur l'audit final » compare à un comparateur désarmé.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Classifieur sur les seuls documents du corpus**, sans aucune action de l'agent. Il doit rester à AUROC ≈ 0,5 à chaque T.
2. **Filtre de furtivité conditionné aux actes sabotés**, rapporté séparément par bras.
3. **LoRA honnête de même rang comme classe négative du duel 2**, et pas seulement comme « cas apparié ».
4. **Placebo de longueur.** Honnête contre honnête à chaque T, à seuils fixés à T = 40, pour mesurer la dérive du FPR du détecteur centré.
5. **Provenance permutée** dans le duel 3 (mêmes degrés, arêtes réaffectées), avec des résultats rapportés par strate d'adversaire.

---

## Ce que cette lecture laisse debout

Je compte ce qui reste réfutable, sans fusionner les propositions.

| Proposition | Ce qui reste empirique après critique |
|---|---|
| **B** | L'écart agentique/scripté, et E2 si τ² est mesuré non nul. L'exposant sur l'adversaire scripté ne l'est plus. |
| **C** | L'expérience 2, à condition de mesurer λ(T) et de fixer la source des comparaisons. |
| **D** | Le duel 3 et le contraste O/T direct, à effectif revu. |
| **E** | Le duel 2 dans son bras activations avec un LoRA honnête en négatif, et le duel 3 par strate. |

Un défaut est commun à B, C et E, et je le signale comme tel et non comme une synthèse : aucune ne prévoit qu'un adaptateur bénin serve de classe négative dans l'expérience où les activations sont censées « gagner avec la longueur ». Sans ce bras, cette conclusion ne peut être réfutée dans aucune des trois.

FIN-DE-CELLULE