# Proposition A — Tour III.2 : critique croisée de méthode

**Préambule.** Les quatre pièces B, C, D, E sont complètes (chacune se termine par sa ligne de clôture). Statuts conservés : tout ce qui est repris des faits garde son statut ; tout chiffre que j'avance est **illustratif** ; les calculs combinatoires que je fais sont les miens et sont à revérifier. Je ne fusionne pas les propositions : chaque section est autonome.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **M2 est vide par construction.** La « divergence KL conditionnelle sous les lois de l'archive » est calculée sur les *lois* de l'archive, pas sur des données. Une paire $(t_i,t_j)$ qu'aucune carte archivée ne conditionne conjointement a une divergence **exactement nulle sous l'archive**, quelle que soit la vérité du monde. L'ensemble des « candidats » est donc le complément des paires déjà archivées : aucune information n'ordonne les $O(d^2)$ paires, et le filtre « au moins un trait impliqué dans une carte archivée » ne restreint qu'à $O(d\cdot|\mathcal T(\mathcal A)|)$. L'objet mathématique annoncé (un graphe de dépendance) se réduit à une énumération lexicographique ; B ne la compare pas à cette énumération. De plus, l'expression $D_{KL}(\hat p(Y|t_i,t_j)\,\|\,\hat p(Y|t_i)\hat p(Y|t_j))$ compare une loi sur $Y$ à un produit de deux lois sur $Y$, qui n'est pas normalisé : la quantité n'est pas définie telle quelle.

2. **Incohérence interne entre M2 et le monde planté.** La composante étroite B est « $t_3$ conditionnel à $t_2>0$ », mais aucun effet marginal de $t_2$ n'est planté ni archivé. Le filtre de M2 (paires dont un trait est archivé) exclut alors $(t_2,t_3)$ si seul $t_1$ est archivé : le bras actif ne peut pas produire l'invitation dont le duel mesure l'effet. Soit le filtre est levé (et M2 devient l'énumération de toutes les paires), soit le monde doit planter un effet marginal de $t_2$, ce qui change la nature du bassin (il devient une chaîne, non une interaction pure).

3. **Confusions dans le duel.** (i) Trois générations avec archive héritée : dès la génération 2, les vues diffèrent entre bras par l'archive héritée, pas seulement par le traitement ; l'effet mesuré à $\le 3$ générations est un effet de trajectoire. (ii) La vue M2 est plus longue que la vue standard ; le contrôle négatif (invitations non pertinentes) ne corrige la longueur que s'il a **le même nombre d'invitations et le même nombre de jetons**, ce qui n'est pas écrit. (iii) M1 attribue une vue distincte par appel de proposeur : vue et identité du proposeur sont confondues ; sans permutation des attributions entre courses, aucun effet de vue n'est séparable d'un effet de modèle.

4. **Fuite instrument/évaluation.** La calibration du regroupement (« 100 paires annotées par l'oracle, sur le monde planté de contrôle ») utilise le monde du duel. Si les mêmes graines servent à régler $\varepsilon$ et à juger les bras, le seuil est ajusté sur la cible. Idem pour le pilote de 5 courses qui « calibre $(p_L,p_E)$ » : estimer $p_E\approx 0{,}1$ sur 5 courses donne un intervalle couvrant pratiquement $[0,0{,}5]$ ; la calibration n'en est pas une.

5. **Dessin neuf non déclaré.** Changer les consignes pendant la course est, selon [C3] §4.1 (RAPPORTÉ), un dessin neuf. B ne le dit pas et ne répond pas à l'objection correspondante.

6. **M1 : garantie déplacée.** Le DPP garantit la diversité volumique **dans le noyau choisi par le concepteur** ; si le noyau code le recouvrement des strates mises en avant et que la liste des strates candidates est écrite par quelqu'un qui connaît le générateur de monde, l'alignement vue↔composante est une fuite de conception. La liste des transformations de vue doit être scellée **avant** le tirage de la graine du monde.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Métrique $C_E$ (couverture parmi les **retenues**) avec test exact de Fisher, $N\ge 30$ par bras. Si $p_{\text{std}}\to 0$ et que le juge a une puissance $\pi_J<1$ sur la composante B, $C_E\le \pi_J\cdot p_{\text{prop}}$ dans les deux bras ; une différence de proposition de 0,2 devient une différence de rétention $0{,}2\,\pi_J$, et le seuil 0,2 n'est atteignable que si $\pi_J\approx1$. Sans lecture aux trois étages (brut / représentants / retenues, [C3] §4.1), un échec n'est pas localisable.
- Zone d'indécision non déclarée entre $+0{,}05$ et $+0{,}20$ : le protocole y est non jugeable.
- Métrique secondaire « taux de fausses découvertes $>1{,}5\times$ le bras standard » : si le taux standard est nul ou à un seul événement sur 30 courses, le ratio est indéfini ou dominé par un événement ; condition : $\mathbb E[\text{FD}_{\text{std}}]\cdot N<5$ (illustratif) rend le critère non jugeable.
- Puissance du Fisher : pour $p_{\text{std}}=0{,}10$ contre $p_{\text{M2}}=0{,}30$ et $N=30$ par bras, la puissance est de l'ordre de 0,4–0,5 (illustratif) : l'issue la plus probable est l'indécision.

### (c) Contrôles négatifs dont l'absence est fatale

- **Monde nul** (aucune composante étroite, seule A archivée) : absent de B ; sans lui, la métrique secondaire n'a pas de référence.
- **Copies renommées injectées** mécaniquement dans chaque bras : absentes ; la pression vers `si_sinon` ([S1], OBSERVÉ-NON-AUDITÉ) ne peut pas être mesurée sans elles.
- **Témoin énumératif** : vues portant l'énumération lexicographique de toutes les paires, même longueur. Duel : $H_A$ « M2 bat l'énumération d'au moins $\delta$ » / $H_B$ « non ». Si $H_B$, le graphe de dépendance est inutile ; si $H_A$, c'est l'énumération complète qui est réfutée comme suffisante.
- **Permutation des attributions vue↔proposeur** entre courses (M1).

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Le plan couvrant annoncé n'existe pas.** C utilise $\text{CA}(4;2,12,2)$. Pour des tableaux couvrants binaires de force 2, le nombre maximal de facteurs couverts par $N$ lignes est $\binom{N-1}{\lfloor N/2\rfloor}$ (Kleitman–Spencer, Katona ; références à vérifier) : 4 lignes couvrent au plus 3 facteurs ; 12 facteurs demandent au moins 7 lignes selon mon calcul. Le bras traitement, tel qu'écrit, ne réalise pas la propriété qu'il invoque. De plus, un tableau couvrant garantit l'apparition de toutes les combinaisons de $t$ colonnes, **pas** l'« isolement d'une interaction dans une projection où les traits archivés sont constants » : ce sont deux objets différents, et le second n'est pas défini.

2. **Confusion des trois traitements.** Le bras M cumule Méthode 1 (vue), Méthode 2 (juge) et Méthode 3 (représentants). C promet un factoriel 2×2 par « relecture hors ligne », mais la génération 2 dépend des retenues de la génération 1 : on ne peut pas rejouer hors ligne ce que les proposeurs auraient rendu sous un autre juge. Le factoriel n'est réalisable que pour $D_2^{\text{brut}}$ en génération 1 ; $D_2^{\text{ret}}$ reste attribué à un bloc indissociable.

3. **Banc de l'Instrument B vrai par construction.** La valeur $e$ de l'unique carte étroite est fixée à $12/\alpha$ (= 240 pour $\alpha=0{,}05$). Avec $m=24$ groupes à poids uniformes, e-BH exige, pour une seule découverte, $e\ge m/\alpha=480$ : la carte échoue ; avec un poids $w\ge 2/24$, elle passe. Le chiffre est choisi dans la fenêtre exacte où seul le poids décide : le gain « +20 points » est une conséquence du paramètre choisi, pas une mesure. Il faut balayer $e$ sur une grille et rapporter la courbe.

4. **Fuite possible dans la Méthode 2.** La hiérarchie dyadique doit être « fixée d'avance indépendamment des données du juge ». Insuffisant : si celui qui écrit la partition connaît les seuils $\tau_1,\tau_2$ du générateur (strate de masse 0,04), un alignement des cellules sur $(X_1>\tau_1,X_2>\tau_2)$ est une fuite de conception vers l'instrument. Condition : partition scellée avant le tirage de la graine, seuils $\tau$ tirés par le programme.

5. **Méthode 2 et la classe du nul.** C exige que le nul local de chaque cellule contienne les lois de l'archive **recalibrées sur $C$**. Mais le nul de l'orchestrateur contient aussi les recombinaisons ([F12] §1, RAPPORTÉ). Si le nul local contient toutes les recombinaisons restreintes à $C$, toute déviation locale exprimable comme recombinaison dans $C$ est absorbée : la méthode gagne contre la dilution mais perd exactement là où la déviation est une « branche » ; si le nul local ne les contient pas, la garde cède dans $C$. C ne choisit pas et ne mesure pas l'arbitrage.

6. **Dessin neuf non déclaré** pour la Méthode 1 (consignes pendant la course, [C3] §4.1).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Métrique $D_2^{\text{ret}}\in\{0,1,2,3\}$ sur 20 mondes appariés, Wilcoxon apparié. $B_3$ n'est atteignable que si $B_1$ est retenue en génération 1 : $\Pr(B_3\text{ ret.})\le \Pr(B_1\text{ ret. en G1})$. Si cette probabilité est inférieure à ~0,3 (illustratif) dans les deux bras, la composante 3 est hors de portée et la métrique sature à 2. Les différences appariées nulles abondent ; Wilcoxon avec $>50\,\%$ d'ex æquo à zéro perd l'essentiel de sa puissance.
- Zone d'indécision non déclarée entre $+0{,}30$ et $+0{,}60$.
- $B_2$ : $r(A)=0{,}04$, $\Delta=0{,}30$ nat (illustratifs). Par la borne de Bretagnolle–Huber que C invoque elle-même, aucune détection si $n\,r(A)\Delta<\ln(1/\alpha)\approx3$, soit $n<250$ ; et la pénalité $\ln(1/w_{C^*})$ de la Méthode 2 (4–6 nats illustratifs) exige $n\,r(A)\Delta\gtrsim 8$–$9$, soit $n\gtrsim 700$. Le paramètre $n$ du juge n'est pas fixé par C : la jugeabilité en dépend entièrement.
- Méthode 3 : si une fraction $\phi$ des cartes est du bruit orthogonal, les poids $w_j$ proportionnels au sinus de l'angle principal s'y concentrent ; la puissance sur les groupes non orthogonaux chute comme $(1-\phi)$. Condition de non-jugeabilité : $\phi>0{,}5$ (illustratif), fréquent si la Méthode 1 pousse vers `si_sinon` sur $X_6\ldots X_{12}$.
- Instrument A : la cible « $\mathbb E_{H_0}[E^{\text{multi}}]\le1$ empirique avec IC à 99 % » sur 250 mondes nuls est peu informative : la variance d'une valeur $e$ sous $H_0$ est lourde à droite, et un IC à 99 % sur la moyenne avec 250 tirages peut dépasser 1 sans violation. Le critère pertinent est $\Pr_{H_0}(E\ge 1/\alpha)\le\alpha$, estimable.

### (c) Contrôles négatifs dont l'absence est fatale

- **Un seul traitement par bras** : trois bras au minimum (vue seule, juge+DPP seuls, bloc), sinon aucune attribution.
- **Plan couvrant contre attribution aléatoire des mêmes lentilles** : $H_A$ « le plan bat le tirage aléatoire des lignes à nombre égal » / $H_B$ « non ». Si $H_B$, la combinatoire est inutile et seule la stratification compte.
- **Copies renommées injectées** et **recombinaisons `si_sinon` sur frontière de cellule** dans le banc de l'Instrument A (C ne teste que des recombinaisons de l'archive globale, pas des recombinaisons alignées sur les cellules de la partition).
- **Balayage de $e$** pour l'Instrument B (voir a.3).

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Alignement dictionnaire↔générateur non contrôlé (M2).** Le moment $h=\operatorname{signe}(x_j)(y-\mu_0(x))$ est exactement la forme de la composante conditionnelle de [C4] §2.1 (RAPPORTÉ). Si le générateur de monde produit des composantes de cette forme, le dictionnaire couvre la cible par construction et le gain mesuré est celui de la coïncidence de deux programmes écrits par la même équipe. D note l'exhaustivité illusoire mais ne prévoit pas de mondes dont la structure conditionnelle sort du dictionnaire (seuil $\ne0$, dépendance à trois traits, condition sur une transformée).

2. **Orthogonalité locale.** Le développement $D_{KL}\approx\frac{\theta^2}{2}\operatorname{Var}_{P_0}(h)$ est pris autour de $P_0$ et sous les lois de l'archive simulées. Si les traits publics sont dépendants sous la loi du monde, $h$ n'est plus orthogonal aux scores ni centré, et la direction « invisible en moyenne » ne l'est pas ; D l'écrit en risque mais aucune mesure n'est proposée pour le vérifier.

3. **Effectif.** 96 appels pour un factoriel $2\times2$ à deux bras, c'est 12 appels par cellule et par bras. D déclare que la variance du pilote fixe l'effectif ; mais présenter ce dessin comme « expérience décisive la moins chère » tout en admettant que l'issue probable est l'indécision est une contradiction : un pilote de variance n'est pas un duel.

4. **Estimation de la largeur.** Juste principe (la largeur est mesurée sur le témoin, non décrétée), mais la cellule « étroit » est définie par le taux de succès brut du témoin sur des mondes d'étalonnage. Si la classification porte sur les **paramètres du générateur** (type de monde), elle est transférable ; si elle porte sur des **graines** individuelles, les graines classées étroites par malchance du témoin régressent vers la moyenne et avantagent le bras traité. D ne précise pas lequel.

5. **M4 et la fermeture du nul.** $e=q/\sup_{\mathcal N}p$ est valide pour le nul spécifié. Si $\mathcal N$ est clos par recombinaison `si_sinon` sur partitions publiques, toute $q$ qui ne diffère de l'archive que par branche a $\sup p\ge q$ presque partout : $e\le1$ identiquement. La méthode qui doit « ne pas confondre rareté et copie » annule alors la puissance sur les composantes conditionnelles, précisément celles que M1+M2 cherchent. D énonce le conservatisme sans en donner la condition.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- $\Delta$ sur la cellule étroit-profond, randomisation par monde. Avec $n$ mondes par bras et $p_B,p_A$ probabilités de couverture retenue, $\operatorname{SE}(\hat\Delta)\approx\sqrt{(p_A(1-p_A)+p_B(1-p_B))/n}$ ; pour $p_B=0{,}1$, $p_A=0{,}3$, atteindre une borne inférieure $>0{,}20$ demande $n$ de l'ordre de plusieurs centaines (illustratif), pas 12.
- M3 : $\delta(P)=\max_A\inf_Q D_A(P,Q)$ ; variance Monte-Carlo de $D_A$ en $1/(n\,r(A))$ ; avec $|\mathcal A|$ strates, le maximum a un biais positif d'ordre $\sqrt{2\ln|\mathcal A|/(n\,r_{\min})}$ (illustratif) : non jugeable dès que $n\,r_{\min}<50$.
- M2 : si $\operatorname{Cov}(x_i,x_j)\ne0$ sous la loi des traits, $\mathbb E[h]\ne0$ et la composante « nulle en moyenne » cesse de l'être ; condition mesurable : $|\mathbb E[x_ix_j]|>\theta\sqrt{\operatorname{Var}(h)}$ (illustratif).
- Taux de cartes invalides : si le modèle 14B/32B produit $>50\,\%$ de cartes hors grammaire, le « coût égal en euros » devient une comparaison de taux d'invalidité, non d'idées.

### (c) Contrôles négatifs dont l'absence est fatale

- **Mondes hors dictionnaire** (structure conditionnelle non couverte par M2) : $H_A$ « le gain persiste » / $H_B$ « il disparaît ». Si $H_B$, le gain est l'alignement de deux programmes ; si $H_A$, l'hypothèse « le dictionnaire est la cause » est réfutée et il faut une autre explication.
- **Classification étroit/large sur paramètres du générateur**, graines de test tirées après classification.
- **Monde à condition verrouillée** (composante conditionnelle dont le parent n'a pas d'effet marginal) : le bras traité ne doit rien promouvoir ; toute promotion est une fausse découverte au sens de l'oracle.
- D possède déjà monde nul, copies, placebo, énumération, strates permutées : c'est la liste la plus complète des quatre.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Le compilateur recrée la classe non couverte.** Un contraste $\chi_{\{a,b\}}$ recompilé dans la grammaire devient `si_sinon` ou `par_sous_population` sur $x_a$ : exactement la zone où la garde cède ([F12] §1, RAPPORTÉ ; [S1] danger commun). E le dit, mais son Duel G ne teste la garde que sur des « familles gelées » de copies et compositions, pas spécifiquement sur **des cartes compilées depuis des contrastes qui coïncident avec une recombinaison de l'archive**. Un contraste $x_a\cdot(\text{pente archivée})$ peut être une copie réécrite : la canonisation doit le reconnaître ; E le met au tableau des instruments (renommages exacts) sans l'inclure dans Duel G.

2. **Orthogonalité conditionnelle.** E distingue proprement « démontrable sous mesure produit équilibrée » et « non postulée pour traits dépendants », mais la bibliothèque est gelée avant la course sans mesurer, sur le jeu public d'instances sans issue, les corrélations entre traits. Les contrastes « invisibles en moyenne » qui ne le sont pas dans le monde déplacent le problème : la composante n'est plus étroite au sens des données.

3. **Méthode C et le quota de formes.** Allouer le budget selon $2^{-L(h)}$ dans un langage du concepteur revient à imposer une loi a priori sur les **formes** de dérivation. L'objection « quota de formes » ([S1]) ne porte pas littéralement, mais l'argument de rejet (forme $\neq$ idée) s'applique : E le reconnaît comme dessin neuf sans dire pourquoi l'objection ne s'applique pas.

4. **Méthode C et $m$.** Une énumération de prolongements produit un grand nombre de candidats ; si tous passent au juge, $m$ croît et le seuil e-BH croît avec lui ; si l'orchestrateur en filtre (par longueur), c'est une sélection publique mais qui doit être scellée. E ne fixe pas la règle sur $m$ alors que [C3] §3.1 exige $m$ fixé par règle écrite.

5. **Duel A : témoin réinvesti.** « Budget économisé réinvesti dans des appels indépendants » : le témoin a plus d'appels, donc plus de cartes, donc plus de groupes et un $m$ plus grand au juge. L'égalité de coût amont crée une inégalité aval (seuil e-BH plus sévère pour le témoin). Il faut fixer $m$ identique par règle ou lire la métrique au niveau brut aussi.

6. **Ablation par énumérateur mécanique** : bon contrôle ; mais si l'énumérateur égale le modèle, E conclut « intérêt du compilateur » ; il faut aussi la condition inverse, où le modèle bat l'énumérateur mais seulement sur des mondes alignés avec la bibliothèque.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Duel A : $\Delta$ apparié sur 100 mondes, $\delta=0{,}10$. Pour $p\approx0{,}3$, $\operatorname{SE}(\hat\Delta)\approx0{,}05$–$0{,}06$ (illustratif) : une borne inférieure au-dessus de 0,10 exige $\hat\Delta\gtrsim0{,}22$ ; en dessous, indécision par construction.
- Méthode A : la probabilité qu'un contraste soit « invisible en moyenne » tient si $\mathbb E[x_ax_b]=0$ ; condition de perte : $|\mathbb E[x_ax_b]|$ comparable à l'amplitude plantée ; mesurable sur le jeu public sans issue.
- Méthode B : si la distribution des lois rendues est invariante par $G$ (équivariance), le gain est nul ; test : distance (Hellinger, par strates) entre lois rendues sous $v$ et sous $g v$ ramenées au repère commun ; non jugeable si la variance d'échantillonnage inter-appels domine, c'est-à-dire si le nombre d'appels par vue est inférieur au nombre de groupes prédictifs distincts observés.
- Méthode C : si le programme cible a longueur $L$ et que la part de budget est $2^{-L}$, la probabilité d'atteinte en $K$ créneaux est $\le K\,2^{-L}$ ; pour $L>\log_2 K+3$ (illustratif) la méthode est équivalente au hasard.
- Duel G : métrique « proportion de courses avec $\ge1$ promotion sous nul complet $\le\alpha$ ». Sous nul complet, FDR et FWER coïncident, donc le critère est bien celui garanti par e-BH ; mais avec $\alpha=0{,}05$ et $R$ courses, l'intervalle sur une proportion attendue de 0,05 a une demi-largeur $\approx 1{,}96\sqrt{0{,}0475/R}$ ; pour $R=25$, $\pm0{,}085$ : le duel est non jugeable en dessous de $R\approx 200$ courses nulles (illustratif), ou il faut lire la valeur $e$ elle-même (loi de $E$ sous $H_0$), pas la fréquence de promotion.

### (c) Contrôles négatifs dont l'absence est fatale

- **Cartes compilées depuis contrastes coïncidant avec des recombinaisons de l'archive**, injectées dans Duel G : si elles sont promues, la garde cède dans la classe que la Méthode A alimente ; absence fatale.
- **Mondes à traits dépendants** où les contrastes de la bibliothèque ne sont pas centrés : $H_A$ « la couverture brute des composantes réellement conditionnelles ne baisse pas » / $H_B$ « elle baisse ou des contrastes faux sont promus ».
- **Règle scellée sur $m$** identique entre bras ; sans elle, Duel A confond coût amont et sévérité aval.
- E possède déjà : mondes additifs, bibliothèque appariée non alignée, proposeur équivariant, énumérateur, nul complet. Il lui manque le **monde à condition verrouillée** (parent sans effet marginal) pour vérifier que les contrastes n'accroissent pas les fausses découvertes au sens de l'oracle là où aucune chaîne n'existe.

---

## Remarques transversales (non une synthèse)

- Trois des quatre pièces (B, C, et la Méthode C de E) modifient les consignes ou le dessin de la course ; seules D et E le déclarent comme dessin neuf au sens de [C3] §4.1. Une pièce qui ne le déclare pas ne répond pas à la règle sur les rejets du premier tour.
- Toutes les métriques aux **retenues** mélangent trois événements : proposer, ne pas être fusionné à tort, survivre au juge. Toute différence entre bras est non attribuable sans les trois étages de [C3] §4.1 ; B et E (Duel A principal) ne les imposent pas comme critères gelés.
- Aucune pièce ne fixe $n$, la taille des tirages frais du juge, alors que la jugeabilité de toute composante étroite confinée à une strate de masse $r(A)$ et de profondeur $\Delta$ dépend de $n\,r(A)\Delta$ et non du dessin des vues.

FIN-DE-CELLULE