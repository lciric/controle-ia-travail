# Proposition B — Critique croisée de méthode, Tour III.2

---

## Préliminaires

La pièce de la proposition A est absente (statut : REFUS). La pièce de la proposition D est absente (statut : ECHEC). Je n'en invente pas le contenu. Mon analyse porte donc sur les propositions C et E uniquement.

Je suis la proposition B ; je critique les deux textes reçus sans les lisser ni les fusionner. Quand j'exploite un de leurs arguments, je le dis explicitement.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Confusion entre capacité algébrique du maître et validité du dispositif expérimental.**

C structure son analyse autour de cinq « expériences décisives » (E1–E5). Le problème central est que E1 et E2 portent exclusivement sur le maître. La capacité du maître à produire du dommage M2 n'est pas une variable expérimentale : c'est un pré-calcul déterministe. L'appeler « expérience » et lui attribuer des hypothèses $H_A$ / $H_B$ avec des seuils illustratifs confère à un test unitaire logiciel le statut rhétorique d'une expérience falsificatrice. Cela dilue la distinction entre ce qui est vrai par construction (l'identité M-3 sur le maître, RAPPORTÉ) et ce qui requiert un test empirique (le comportement de l'élève). C le reconnaît partiellement en proposant E1–E2 comme « porte d'arrêt CPU », mais le cadrage en duels $H_A / H_B$ avec des seuils illustratifs suggère un degré d'incertitude épistémique qui n'existe pas : on peut simplement calculer la réponse.

**2. Les seuils illustratifs des expériences décisives ne sont pas liés entre eux par un modèle statistique.**

C propose $0{,}25$ décade pour E1 (maître), $R_{1/2} \geq 0{,}30$ pour E2 (convexité), $\tau_{\text{élève}} \leq -0{,}25$ pour E3, AUROC $\in [0{,}45 ; 0{,}55]$ pour E4, et $|\Delta_0| \leq 0{,}03$ décade pour E5. Ces seuils sont tous marqués « illustratif », ce qui est correct. Mais aucune discussion ne lie la puissance statistique de chaque test au nombre d'actions disponibles (8 à 16 tâches, RAPPORTÉ, avec un nombre d'actions par tâche non spécifié). Pour que E3 ait une puissance non triviale de détecter $\tau_{\text{élève}} \leq -0{,}25$ au niveau $\alpha = 0{,}05$, il faut au minimum environ $n \geq 15$ paires intra-classe (illustratif) pour un test de Kendall unilatéral. Si les classes ont $n_k = 2$ ou $3$ (risque 1, RAPPORTÉ), le test de corrélation de rang intra-classe n'a littéralement aucune puissance discriminante. C ne dit pas comment agréger les $\tau$ entre classes de taille variable, ce qui est précisément l'endroit où l'on peut introduire un biais de pondération.

**3. Variable confondante dans E5 : le sur-lissage n'est pas la seule source de biais du témoin $p=0$.**

C identifie correctement le risque que la distillation à $p=0$ réduise la variance et abaisse $\text{M2}(p=0)$. Mais le raisonnement suppose que l'adaptateur à $p=0$ apprend l'identité sur sa propre distribution avec des gradients quasi nuls. Ce n'est pas garanti : si le corpus du maître à $p=0$ contient des transcriptions multiples par action (sélectionnées ou non), l'adaptateur peut apprendre à « moyenner » les modes, ce qui est distinct de l'identité. C propose de comparer $\text{M2}(p=0)$ au modèle de base nu, ce qui est un bon contrôle. Mais la proposition omet que le modèle de base nu génère à température $> 0$ (implicite dans le fait que 8 suites servent de référence), tandis que l'adaptateur à $p=0$ peut avoir été entraîné sur une seule suite par action du maître. Le facteur confondant est la multiplicité des suites du maître, pas seulement la norme de l'adaptateur.

**4. Faille 4 (contamination autorégressive) est correcte mais incomplète.**

C observe que si `COST` précède d'autres champs, l'élève conditionnera sa suite sur un coût anormal. C'est un point fort. Cependant, C ne distingue pas deux cas : (i) `COST` est le dernier champ d'une action isolée (l'invariance pourrait survivre), (ii) l'épisode est multi-tours et le coût d'un tour conditionne le tour suivant. Les FAITS ne spécifient pas le format, ce que C note implicitement mais ne traite pas comme une pièce manquante.

**5. L'estimation de coût (section d) est trop optimiste et sous-estime la variance de conception.**

C estime $\approx 2{,}2$ GPU-heures pour E1–E5, soit 3,50–6,50 \$. Ce chiffre suppose un seul GPU A100-80GB et une seule graine par adaptateur (sauf $p=0$ et $p=1$ dupliqués). Le problème est que E3 requiert une corrélation de rang significative, ce qui nécessite un nombre d'actions suffisant *par classe*. Si le jeu de conception a 8 tâches × 15 actions × classes de taille 3, on a ~40 classes avec ~3 actions chacune : chaque $\tau$ intra-classe est essentiellement du bruit. Pour obtenir de la puissance, il faut soit plus d'actions (plus de tâches, ce que le jeu de conception ne permet pas), soit agréger les $\tau$ entre classes sous des hypothèses d'homogénéité que C ne mentionne pas. Le devis sous-estime donc le coût réel de la résolution du problème de puissance.

### (b) Conditions probabilistes sous lesquelles chaque mesure perdrait sa puissance

**E1 (M2 du maître à $p=1$).**
Perd sa puissance si : la distribution intra-classe de $\log_{10}(\text{COST})$ a un écart-type $\sigma_k < 0{,}08$ décade (illustratif) dans plus de 70 % des classes. Sous cette condition, le réappariement anti-monotone maximal déplace chaque coût de moins de $2\sigma_k \approx 0{,}16$ décade, ce qui rend le seuil de $0{,}25$ décade inatteignable. Paramètre critique : la distribution jointe $(n_k, \sigma_k)$ des tailles et dispersions de classe. C identifie $n_k$ mais pas $\sigma_k$ comme paramètre limitant.

**E3 ($\tau_{\text{élève}}$ intra-classe).**
Perd sa puissance si : la taille effective (nombre de classes × taille médiane de classe) est telle que $\sum_k (n_k - 1) < 50$ (illustratif). La variance de l'estimateur agrégé $\hat{\tau}$ (pondéré par classe) est approximativement $\frac{4(2n_{\text{eff}}+5)}{9n_{\text{eff}}(n_{\text{eff}}-1)}$ pour des classes de taille $n_{\text{eff}}$ (illustratif, formule asymptotique du $\tau$ de Kendall), et le test unilatéral à $\alpha = 0{,}05$ ne peut rejeter $\tau = 0$ que si $|\hat{\tau}| > z_{0{,}05} \cdot \text{se}(\hat{\tau})$. Avec des classes de taille 2–3, $\text{se}(\hat{\tau})$ est de l'ordre de 0,4–0,7, rendant le seuil de $-0{,}25$ non discriminant.

**E4 (AUROC de la base sur l'élève).**
Perd sa puissance si : le nombre total d'épisodes évalués par condition est inférieur à ~100 (illustratif). Avec 16 tâches × 3 graines = 48 épisodes par condition, la variance de l'AUROC estimée (sous $H_0$ : AUROC = 0,5) est $\approx \frac{1}{12n} \approx 0{,}0017$ (illustratif), soit un écart-type de $\approx 0{,}04$. L'intervalle $[0{,}45 ; 0{,}55]$ correspond alors à $\pm 1{,}25\sigma$, ce qui donne une probabilité de rejet à tort de $\approx 21\%$ (illustratif). Le seuil est donc trop étroit pour 48 épisodes, ou trop large pour être informatif.

**E5 ($\Delta_0$ témoin vs base nue).**
Le seuil de $0{,}03$ décade est non jugeable si l'erreur plancher $\text{M2}_{\text{plancher}}$ (variance de la médiane basse sur 8 suites) est elle-même $> 0{,}03$ décade. C reconnaît ce risque dans la section « instrument M2 » mais ne le connecte pas au verdict de E5.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de sensibilité de la base (absent de E4).** C propose de tester la base sur maître à $p=1$ vs $p=0$ (doit donner AUROC = 0,5 exactement). Mais il manque le contrôle positif sur l'élève : un élève *intentionnellement dégradé* (par exemple entraîné sur des transcriptions où `COST` est remplacé par un bruit uniforme) doit être détecté par la base avec AUROC $> 0{,}80$ (illustratif). Sans ce contrôle, un AUROC $\in [0{,}45 ; 0{,}55]$ sur l'élève à $p=1$ pourrait simplement refléter l'incompétence de la base.

2. **Contrôle de transfert hors-entraînement (absent ou implicite).** Les cinq expériences de C évaluent toutes sur le « jeu de conception » (8–16 tâches de réserve, RAPPORTÉ). Aucune ne mentionne un partage entraînement/évaluation *à l'intérieur* de ce jeu. Si l'adaptateur est entraîné sur les mêmes tâches que celles utilisées pour E3–E5, l'élève peut mémoriser les correspondances action–coût du maître sans rien apprendre de transférable. C'est un overfitting banal. Le contrôle négatif manquant : évaluer l'adaptateur sur des tâches retenues hors de l'entraînement de l'adaptateur.

3. **Contrôle d'interaction entre dose et graine de permutation (absent de E2).** C propose un contrôle par « permutation aléatoire uniforme intra-classe ». Mais le contrôle critique pour E2 est l'évaluation sur *deux jeux de graines différents* à la même dose nominale : si $\text{M2}_{\text{maître}}$ varie fortement entre graines à $p = 1/2$, la non-linéarité observée est un artefact du tirage, pas de l'échelle Kendall.

---

## Sur la proposition E

### (a) Défauts de méthode

**1. Les duels sont formulés à un niveau d'abstraction qui rend leur falsification ambiguë.**

E propose cinq duels (I–V). Le duel I porte sur « P4 est-elle réellement une identité du maître ». Les hypothèses sont : $H_A$ — « la transformation préserve exactement la représentation complète dont le score de la base dépend » ; $H_B$ — « elle ne la préserve pas ». Le problème est que $H_A$ n'est pas testable sans connaître la représentation interne de la base. E dit « vérification formelle de la dépendance du score », mais le code de la base n'est pas fourni (E le reconnaît : « le code des bases, les six indicateurs et les données sont absents »). En l'absence de ce code, le duel I est un appel à une vérification logicielle qui peut être exécutée mais pas planifiée en détail ici. L'hypothèse $H_A$ est alors un prédicat sur un artefact non disponible, ce qui la rend non falsifiable *dans le contexte actuel*.

**2. L'objection sur la distribution jointe (section A.1) est la contribution la plus forte, mais elle est sous-développée.**

E écrit : « Préserver séparément les mots et les coûts ne préserve pas nécessairement leur distribution jointe. » C'est exact et potentiellement dévastateur pour P4. Si la base « mots et coût » utilise un score de vraisemblance conditionnelle $P(\text{COST} | \text{action, description})$ plutôt qu'une comparaison marginale, alors le réappariement anti-monotone intra-classe modifie cette vraisemblance conditionnelle même si les marginales sont préservées. Le maître à $p=1$ présente des paires (action, coût) individuellement *incohérentes* bien que collectivement *correctes en marginale*. E ne quantifie pas cette faille : sous quelle distribution jointe la base passerait-elle de AUROC = 0,5 à AUROC > 0,8 ? L'absence de modèle paramétrique rend l'objection juste mais non calibrée.

**3. Le contre-exemple de la section A.2 (référence inversement corrélée au coût initial) est théoriquement valide mais empiriquement improbable sans explication.**

E observe que le réappariement anti-monotone *par rapport au coût initial* pourrait *rapprocher* les déclarations de la référence cachée si la référence est anti-corrélée aux coûts initiaux. C'est logiquement correct. Mais les FAITS indiquent que les coûts initiaux proviennent de « transcriptions honnêtes du modèle de base 8B » (RAPPORTÉ) et que la référence cachée est la « médiane basse de huit suites du modèle de base » (RAPPORTÉ). Si les deux proviennent du même modèle sur les mêmes tâches, leur corrélation est positive par construction (ce sont des tirages de la même distribution). L'anti-corrélation exigerait un événement pathologique (par exemple, la transcription unique du maître est un tirage extrême). E ne conditionne pas son contre-exemple sur cette circonstance, ce qui en affaiblit l'impact pratique.

**4. L'enveloppe budgétaire (section D) est un ordre de grandeur plus chère que celle de C, sans justification détaillée.**

E propose 40–160 GPU-heures et 80–800 € (illustratifs). C propose 2,2 GPU-heures et 3,50–6,50 \$. L'écart de ~20–70× est frappant. E ne détaille pas la source de ce surcoût. L'explication probable est que E inclut trois graines par dose (12 entraînements), un corpus plus large (2 M jetons, 2 passages), et ne suppose pas de gain d'efficacité du pipeline. Mais sans décomposition ligne par ligne, l'enveloppe est un intervalle opaque qui n'aide pas à identifier le goulot d'étranglement ni à arbitrer entre les deux propositions.

**5. La structure en « portes séparées » (Verdict proposé) est correcte mais ne dit pas comment traiter les interactions entre portes.**

E propose quatre portes : P4-maître, P3-maître, P3-élève, Discrétion-élève. C'est un bon séquençage. Mais E ne dit pas ce qui se passe si P4-maître échoue partiellement (la base détecte le maître à AUROC = 0,58, juste au-dessus du seuil) : faut-il abandonner le bras B, redéfinir les classes, ou restreindre l'analyse aux classes où P4 tient ? L'absence de règle d'interaction entre portes laisse un degré de liberté exploitable après les résultats.

### (b) Conditions probabilistes sous lesquelles chaque mesure perdrait sa puissance

**Duel I (identité de P4).**
N'est pas un test statistique mais une vérification logicielle. Perd sa pertinence si la base utilise des caractéristiques non documentées dans les six indicateurs (par exemple, position séquentielle de l'action dans l'épisode). Condition formelle : si l'ensemble des caractéristiques effectives $\mathcal{F}$ de la base n'est pas un sous-ensemble des caractéristiques préservées par le couplage, P4 ne tient pas. Ce n'est pas une condition probabiliste mais une condition ensembliste — ce qui est approprié pour une identité.

**Duel II (M2 du maître, $\Delta_1 \geq 0{,}15$ décade).**
Perd sa puissance sous les mêmes conditions que E1 de C (dispersion intra-classe faible). Condition additionnelle propre à la formulation de E : E exige la *non-décroissance* sur la grille ($\Delta_{1/4} \leq \Delta_{1/2} \leq \Delta_1$). Cette monotonie est un test joint sur trois inégalités. Si la variance de $\Delta_p$ entre graines de permutation est $\sigma_\Delta \geq 0{,}05$ décade (illustratif) et qu'il n'y a qu'une graine par dose (ce que E ne spécifie pas), la probabilité d'observer une inversion accidentelle entre deux doses voisines est substantielle même sous $H_A$.

**Duel III (transfert de la distillation).**
Perd sa puissance si le nombre de familles de tâches réservées est $\leq 3$ (illustratif). E dit que les effets sont estimés « par famille de tâches et graine, non en traitant chaque action comme indépendante ». C'est statistiquement correct mais impose que l'unité d'analyse est la famille, réduisant $n_{\text{eff}}$ à ~2–4 (8–16 tâches groupées en familles). Un test de rang signé de Wilcoxon sur 3–4 familles n'a essentiellement aucune puissance pour tout seuil raisonnable.

**Duel V (stabilité entre lots de références).**
Perd son jugement si : la variance inter-lots de $\Delta_1$ est dominée par la variance inter-tâches plutôt qu'inter-lots. Pour deux lots de 8 suites tirés du même modèle, la différence des médianes basses est approximativement $\text{se} \approx \frac{\sigma_{\log c}}{\sqrt{8}} \cdot \sqrt{\pi/2}$ (illustratif, approximation de la variance de la médiane d'une loi normale). Si $\sigma_{\log c} \approx 0{,}10$ décade (illustratif), $\text{se} \approx 0{,}044$ décade, et le seuil de E ($0{,}05$ décade) est essentiellement la résolution de l'estimateur. Le test ne discriminerait alors rien.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de compétence de la base (mentionné mais non opérationnalisé).** E dit : « une base faible pourrait échouer sur tout » et recommande des « anomalies mécaniques connues comme contrôle de sensibilité ». Mais aucune anomalie spécifique n'est définie. Le contrôle négatif fatal manquant : un élève entraîné sur des transcriptions où le champ `COST` est systématiquement remplacé par la constante « 1.00 » doit être détecté par la base. Si la base ne le détecte pas, elle est aveugle par incompétence et tout résultat de discrétion est non interprétable.

2. **Contrôle de dégradation générale (mentionné mais non spécifié).** E écrit : « Une dégradation générale constatée sur les contrôles non ciblés invaliderait l'interprétation spécifique. » Le contrôle manquant : mesurer la perplexité de l'élève (ou un proxy de compétence) sur une tâche non liée au coût (par exemple, génération de texte générique). Si la perplexité augmente de plus de $x$% (illustratif) entre l'adaptateur $p=0$ et l'adaptateur $p=1$, la hausse de M2 peut être attribuée à une dégradation générale plutôt qu'à un réappariement spécifique.

3. **Contrôle de mémorisation vs généralisation (absent).** E mentionne le transfert hors entraînement dans le duel III mais ne spécifie pas le protocole de partage. Le contrôle fatal : un partage train/test *au niveau des classes de forme*, pas seulement des tâches. Si les mêmes classes apparaissent dans l'entraînement et l'évaluation (sur des tâches différentes mais avec les mêmes indicateurs de forme), l'adaptateur peut mémoriser la table de correspondance classe → coût moyen sans apprendre le mécanisme d'inversion.

---

## Synthèse comparative

| Dimension | Proposition C | Proposition E |
|---|---|---|
| Granularité | Cinq expériences avec seuils numériques ; sur-spécifié pour le maître, sous-spécifié pour l'élève | Cinq duels abstraits ; correctement hiérarchisés mais non opérationnalisables sans le code de la base |
| Point fort principal | Faille 3 (effondrement modal de l'élève) et la métrique $\rho_{\text{élève}}$ | Faille A.1 (distribution jointe vs marginales) — attaque la prémisse même de P4 |
| Point faible principal | Puissance statistique non calibrée au jeu de conception (8–16 tâches) | Budget non justifié ; duels non falsifiables sans artefacts absents |
| Contrôle négatif le plus utile proposé | Témoin de permutation inter-épisodes à rang quasi-identique (E5) | Lot de références indépendant (Duel V) |
| Contrôle négatif fatal manquant | Partage train/test au niveau des tâches pour l'adaptateur | Contrôle de compétence opérationnel de la base |

Les deux propositions convergent sur trois failles que je considère comme les plus dangereuses pour le bras B :

1. **Les classes de forme peuvent être à la fois trop petites et trop étroites en dispersion pour que le maître produise un dommage détectable** (C : faille 1 ; E : section A.4). C'est une faille fatale en faux négatif, vérifiable avant toute dépense GPU.

2. **L'élève peut augmenter M2 par dégradation générale plutôt que par inversion de rang** (C : faille 3 ; E : section A.5). C'est une faille fatale en faux positif, nécessitant $\rho_{\text{élève}}$ ou un équivalent.

3. **P4 sur le maître ne garantit pas P4 sur l'élève, et pourrait ne pas tenir même sur le maître si la base utilise la distribution jointe** (C : faille 4 ; E : section A.1). C'est une faille fatale en faux positif de discrétion.

Je ne lisse ni ne fusionne ces analyses. Je note que C est plus actionnable (elle propose des seuils et un séquençage) et que E est plus fondamentale (elle attaque la prémisse de P4 au bon niveau). Ni l'une ni l'autre ne résout le problème de puissance sur un jeu de 8–16 tâches.

FIN-DE-CELLULE