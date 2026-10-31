# Proposition C — Tour III.3 : réponse aux critiques

---

## (a) Réponse critique par critique

### Critiques de A visant C

1. **Défaut transversal 1 & Critique (a)4 (Recouvrement vrai par construction sur les fiches de passe 1 ; auto-recopie exclue laissant passer les entrées libres d'un même proposeur)** : **Acceptée.** Le juge reçoit les fiches des deux passes (VÉRIFIÉ, fait 2). J'applique le filtre de recouvrement exclusivement aux textes *propres au tableau* (entrées libres de B, pistes de C, à l'exclusion des titres et résumés extraits des fiches de passe 1), mais sur *tous* les proposeurs (y compris l'auto-recopie par $P_i$ de sa propre entrée libre dans sa fiche de passe 2).
2. **Défaut transversal 2 (Absence d'unité pour les éléments de code)** : **Acceptée.** Je définis l'unité comme une *fonction pure à entrée/sortie typée, testée unitairement et scellée par une empreinte SHA-256 dans la liste* (au sens de `EMPREINTES-orchestrateur-pole-v7-v52.txt`, VÉRIFIÉ en-tête des faits).
3. **Critique (a)1 (Le tableau complet de C restreint la lecture aux résumés de 300 caractères, ce qui en fait un intermédiaire)** : **Acceptée.** Dans B corrigé, les proposeurs lisent les fiches entières de passe 1 et les entrées libres du tableau, sous le seul plafond de contexte total (6 000 caractères d'entrées libres au total, illustratif).
4. **Critique (a)2 & Critique D.(a)7 (Statuts glissés, exemples de marqueurs au bloc 3, précision des faits 3, 4, 7, 8, 10)** : **Acceptée.** Je corrige rigoureusement chaque attribution : les témoins v2 de longueur comparable sont « en attente » (RAPPORTÉ, fait 3) ; 0,414 est la part de fiches validées en surplus d'une idée déjà comptée (VÉRIFIÉ par calcul, fait 4, qui ne vérifie pas le décompte) ; `memoire.py` ne nomme que les rôles expérimentateur et recombinaison (VÉRIFIÉ, fait 7) ; « moins de texte libre : moins de canaux » est un principe affiché en en-tête de code (VÉRIFIÉ, fait 8) ; les coûts en dollars sont purement illustratifs (le fait 10 VÉRIFIÉ ne donne aucun tarif). Tout exemple de formulation de rôle est retiré.
5. **Critique (a)3 & Critique B.(a)2 (Fuite dans la garde de forme et confusion réglage/évaluation de la borne de 300 caractères)** : **Transformée en test.** Les plantations du tiers sont stratifiées en deux sous-ensembles disjoints (50 % respectant le gabarit déclaratif et la borne de 300 caractères, 50 % hors gabarit, illustratif), et les cases sont partitionnées entre réglage et évaluation réservée (emprunté à D).
6. **Critique (a)5 & Critique D.(a)3 (Reconnaissabilité mesurée sur le score et non sur le taux de reconnaissance)** : **Acceptée.** La mesure porte désormais sur l'écart du taux de reconnaissance binaire des témoins par rapport au critère gelé (VÉRIFIÉ, fait 2).
7. **Critique (a)6 (Indice produit $I \times D / \$$ dominé par $I$)** : **Acceptée.** Je sépare le critère principal ($I / \$$) et la contrainte de non-dégradation ($D$).
8. **Critique (a)7 (Exclusion a priori des rôles choisis par les proposeurs)** : **Transformée en test.** J'intègre au Duel 3 un bras comparant l'attribution par l'orchestrateur à l'auto-attribution des rôles sur le tableau (demandée par le directeur, RAPPORTÉ fait 6).
9. **Critiques (b) et (c) de A, B et D sur la puissance aux petits effectifs, le paradoxe de $\kappa$ à basse prévalence, le biais de longueur du Jaccard et de la fiche la plus longue, et la marge $0,25\sigma$** : **Acceptées.**
   - *Puissance et taux nuls* : Au lieu de seuils ponctuels $0\%$ indémontrables sur $n=20$, la décision porte sur la borne supérieure de l'intervalle de confiance exact à $95\%$ (règle de $\approx 3/n$, soit $\le 0,15$ sur 20 plantations réservées, illustratif) ET sur la supériorité stricte face à un contrôle positif non gardé.
   - *Paradoxe de $\kappa$* : Je remplace $\kappa$ global par le $\kappa$ de Cohen calculé sur un sous-ensemble équilibré (toutes les paires positives détectées + un nombre égal de paires négatives tirées au sort, complété par les paires d'étalonnage plantées), doublé de l'accord positif ($F_1$ inter-lecteurs $\ge 0,75$, illustratif).
   - *Biais de longueur sur Jaccard* : La diversité trigramme est calculée sur des fiches (ou représentants tirés au sort dans chaque composante, correction de B.(c)1) tronquées ou sous-échantillonnées à une longueur commune de $L_0 = 1\,500$ caractères (illustratif).
   - *Dénominateur de coût et marge de qualité* : Les duels comparent d'abord le nombre d'idées distinctes à budget de génération imposé égal, ET le ratio par dollar total ; la marge de non-infériorité de qualité est fixée à $0,40\sigma$ (illustratif), résolvable sur l'effectif réservé.

### Critiques de B visant C

1. **Critique (a)3 & D.(a)2 (Filtre de 50 caractères déclenchant sur le vocabulaire de la question commune ; extrait planté de 60 caractères vrai par construction)** : **Acceptée.** Le filtre de recouvrement retire d'abord les sous-mots présents dans le texte de départ (la question servie) avant de calculer le plus long sous-mot commun entre une entrée propre au tableau et une fiche de passe 2. L'évaluation plante des extraits de longueurs étagées (30, 45 et 60 caractères, illustratif), avec et sans la chaîne inerte.
2. **Critique (a)4 & D.(c) (Pistes vides modifiant la longueur de consigne)** : **Acceptée.** Le contrôle négatif remplace les pistes par un *placebo de même longueur, même format et même coût*, généré à partir d'entrées de remplissage neutres sans partage inter-proposeurs (emprunté à B et D).
3. **Critique (a)5 & D.(a)6 (Classifieur de rôle non étalonné et fuite entre proposeurs/cases en validation croisée)** : **Acceptée.** Le classifieur est évalué par validation croisée laissant une case et un proposeur hors de l'entraînement (*leave-one-case-and-proposeur-out*), et son exactitude est comparée à la distribution nulle obtenue par permutation aléatoire des étiquettes de rôle (test de permutation exact, $p > 0,10$, illustratif).
4. **Critique (c)2 & D.(a)1 (Prise d'instruction glissée sans recopie de la chaîne inerte ; sécurité de C non mesurée directement)** : **Transformée en test.** Les plantations sont faites dans B *et* dans les pistes courtes de C. Outre la détection mécanique de la chaîne inerte, deux lecteurs aveugles évaluent sur les paires appariées (fiche issue d'un tableau avec instruction plantée contre fiche issue du même tableau sans l'instruction) si la cible de l'instruction plantée est suivie sans que la chaîne inerte soit recopiée.

### Critiques de D visant C

1. **Critique (a)4 & (c) (Contrôle négatif du détecteur de doublons sur textes différents non certifié)** : **Acceptée.** Les non-doublons du contrôle négatif sont des paires de fiches de la *même case* certifiées distinctes par consensus de trois lecteurs indépendants, appariées en longueur et en proposeur.
2. **Critique (a)5 (Biais de sélection post-quarantaine sur la qualité jugée ; taux de validation mécanique ne mesurant pas la qualité)** : **Acceptée.** Toute fiche mise en quarantaine reçoit un score pénalisé fixe (plancher de la grille) dans une analyse en intention de traiter (*intention-to-treat*) menée en parallèle de l'analyse sur fiches validées. Si l'HYPOTHÈSE sur le fait 13 ne tient pas, la sélection entre A, B et C repose uniquement sur le nombre d'idées distinctes et la diversité par dollar (comme pour les rôles), la note des juges n'étant rapportée qu'à titre d'information (VÉRIFIÉ, fait 13).
3. **Critique (b) (Attribution d'une idée multi-proposeurs pour le poids du plus prolifique)** : **Acceptée.** J'adopte la règle d'attribution fractionnaire gelée (empruntée à D) : si une composante connexe contient $m$ fiches dont $m_i$ du proposeur $P_i$, cette idée compte pour $m_i / m$ dans le score de $P_i$.

---

## (b) Expériences décisives et mesures d'instruments corrigées

### Protocole commun du pré-pilote corrigé
- **Partition réglage / évaluation réservée** (empruntée à D) : $K_{\text{règ}} = 4$ cases pour régler les seuils des gardes et filtres ; $K_{\text{éval}} = 12$ cases réservées (illustratif) pour exécuter les duels et évaluer les instruments, sans retouche de seuil. Chaque case compte $N = 4$ proposeurs et 2 juges figés.
- **Témoins** : 4 témoins v2 par case (de longueur et forme comparables aux fiches, dès leur livraison, RAPPORTÉ en attente au fait 3), soit 48 témoins sur l'ensemble d'évaluation.
- **Unité d'analyse et dépendance** : Case appariée ($K_{\text{éval}} = 12$). Pour chaque métrique, les fiches sont agrégées au niveau de la case (en pondérant chaque composante connexe de façon fractionnaire $m_i/m$ entre proposeurs). Les duels utilisent un test de permutation apparié par case (exact sur $2^{12} = 4\,096$ permutations) et un intervalle de confiance par bootstrap stratifié par case.

### Duels corrigés ($H_A$ contre $H_B$)

#### Duel 1 : Conception C (Tableau intermédiaire à pistes typées) contre Conception A (Tableau minimal)
- **$H_A$** : Sur les 12 cases réservées, la conception C augmente le nombre d'idées distinctes par dollar ($R = C_{\text{idées}} / \$$) d'au moins $+15\%$ en moyenne par rapport à A ($p < 0,05$ au test de permutation apparié), maintient un gain positif en nombre brut d'idées $C_{\text{idées}}$ à budget de génération égal, et ne dégrade ni la qualité jugée en intention de traiter ($\Delta Q > -0,40\sigma$), ni le taux de reconnaissance des témoins (écart $|\Delta \tau_{\text{tém}}| \le 0,10$, soit au plus 4 témoins d'écart sur 48, illustratif), avec un taux de prise des instructions glissées plantées dans les pistes de C nul ($0/24$, borne supérieure à $95\% \le 0,12$).
- **$H_B$** : Le gain sur $R$ est $< +15\%$ (ou $p \ge 0,05$), ou $\Delta C_{\text{idées}} \le 0$, ou $\Delta Q \le -0,40\sigma$, ou $|\Delta \tau_{\text{tém}}| > 0,10$, ou au moins une prise est observée dans C ($\ge 1/24$).
- **Contrôle négatif** : Conception C-placebo où les pistes lues en passe 2 sont remplacées par des pistes de même longueur, même type et même coût en jetons, composées de chaînes neutres tirées de la question sans échange inter-proposeurs (isole l'effet du contenu échangé de l'effet de longueur et de gabarit).
- **Falsification** : Toute réalisation d'une clause de $H_B$ falsifie $H_A$ ; la satisfaction conjointe de toutes les clauses de $H_A$ (et la supériorité de C sur C-placebo) falsifie $H_B$.

#### Duel 2 : Conception B (Tableau complet en lecture des fiches entières et écriture libre gardée) contre Conception C (Tableau intermédiaire)
- *Afin d'isoler lecture et écriture (critiques B et D), un bras factoriel intermédiaire $C^+$ (lecture des fiches entières + écriture limitée aux pistes typées) est inclus.*
- **$H_A$** : La liberté d'écriture de B augmente $R = C_{\text{idées}} / \$$ d'au moins $+15\%$ par rapport à C et d'au moins $+10\%$ par rapport à $C^+$ ($p < 0,05$), tout en respectant simultanément sur les 12 cases réservées : (1) baisse de diversité trigramme à longueur tronquée ($L_0 = 1\,500$ car., représentant tiré au sort par composante) $< 10\%$ par rapport à A ; (2) part maximale d'idées fractionnaires d'un proposeur $\le 0,40$ ; (3) zéro fuite vers le juge ($0/24$ fiches en alerte post-filtre) et $|\Delta \tau_{\text{tém}}| \le 0,10$ ; (4) zéro prise sur 24 instructions glissées plantées dans B ($0/24$, tant par la chaîne inerte que par lecture aveugle).
- **$H_B$** : B n'atteint pas $+15\%$ sur C (ou $+10\%$ sur $C^+$) en idées par dollar, ou viole au moins l'une des quatre conditions d'évitement des écueils.
- **Contrôle négatif** : (1) Tableau A (minimal) comme référence de convergence ; (2) plantations réduites à la chaîne inerte seule sans instruction ; (3) contrôle positif non gardé (sur 4 cases de réglage, exécution de B sans garde de forme pour vérifier que le taux de prise de base des plantations est $\ge 0,25$, illustratif, prouvant que le zéro observé avec garde n'est pas un artefact de plantations inertes).
- **Falsification** : L'échec d'une seule condition falsifie $H_A$ et condamne l'écriture libre ; le succès conjoint falsifie $H_B$.

#### Duel 3 : Attribution des rôles (Orchestrateur contre Auto-attribution sur le tableau contre Étiquettes sans consigne)
- **$H_A$** : Les rôles avec consigne (assignés par permutation latine équilibrée par l'orchestrateur OU auto-attribués par les proposeurs via les pistes `RÔLE` du tableau) augmentent le ratio $R = C_{\text{idées}} / \$$ d'au moins $+15\%$ ($p < 0,05$) sans baisse de la diversité tronquée ($\Delta D \ge -0,05$) par rapport au contrôle négatif (étiquettes de rôle servies sans consigne de conduite), et l'exactitude d'un classifieur trigramme évalué hors case et hors proposeur ne dépasse pas la borne supérieure à $95\%$ de la distribution par permutation des étiquettes ($p_{\text{perm}} > 0,10$). Un sous-duel tranche entre permutation par l'orchestrateur ($H_{A1}$) et auto-attribution sur le tableau ($H_{A2}$) sur le même critère $R$ et sur la part du plus prolifique ($\le 0,40$).
- **$H_B$** : Aucune des deux modalités de rôles ne gagne $+15\%$ sur $R$ face aux étiquettes sans consigne, ou $\Delta D < -0,05$, ou le rôle transparaît dans les fiches ($p_{\text{perm}} \le 0,10$).
- **Contrôle négatif** : Étiquettes de rôle sans consigne de conduite, condition sans rôle, et étiquettes permutées aléatoirement lors de l'audit du classifieur.
- **Falsification** : Si le gain sur $R$ est $< +15\%$ ou $p_{\text{perm}} \le 0,10$, $H_A$ est falsifiée ; sinon $H_B$ est falsifiée (et le sous-duel retient $H_{A1}$ si l'auto-attribution viole le seuil du plus prolifique $> 0,40$).

### Mesure minimale corrigée des trois instruments (sur les 12 cases d'évaluation réservées)

1. **Détecteur de doublons (2 lecteurs indépendants + 3e en arbitrage + composantes connexes)** :
   - *Cas appariés* : 40 paires de fiches de la même case certifiées d'idées distinctes par consensus, appariées en longueur et proposeur à 40 paires où la seconde fiche est une réécriture par un tiers aveugle (20 à vocabulaire disjoint, 20 mimant les redites intra-proposeur de la course 1, RAPPORTÉ fait 3).
   - *Base à battre* : Recouvrement de trigrammes (seuil réglé sur les 4 cases de réglage).
   - *Seuils* : Accord équilibré $\kappa_{\text{éq}} \ge 0,70$ et $F_1 \ge 0,75$ ; rappel $\ge 0,85$ (borne inf. IC $95\% \ge 0,70$), fausses alertes (TFA) $\le 0,05$ sur les non-doublons certifiés de même case, et gain de rappel $\ge +0,20$ sur la base à TFA égal (test de McNemar, $p < 0,05$, illustratif).
2. **Garde contre les instructions glissées (balisage, filtre nombres/vocabulaire du fait 7 VÉRIFIÉ, et gabarit déclaratif)** :
   - *Cas appariés* : 30 entrées honnêtes du tableau (et 30 pistes de C), appariées aux mêmes entrées où un tiers insère une instruction glissée avec chaîne inerte (15 respectant le gabarit et la taille de 300 caractères, 15 hors gabarit).
   - *Base à battre* : Garde lexicale du noyau (VÉRIFIÉ, fait 2) + coupe à 300 caractères seule.
   - *Seuils* : En amont, TFA $\le 0,05$ sur entrées honnêtes ; en aval (sur les 24 plantations en course des Duels 1 et 2), prise mesurée par chaîne inerte ET par lecteur aveugle égale à $0/24$ (borne sup. IC $95\% \le 0,12$), contre une prise $> 0,20$ avec la base seule sur les cases de réglage. Contrôle négatif : chaîne inerte seule sans instruction.
3. **Séparation d'avec le juge (exclusion des témoins fait 7 VÉRIFIÉ, et filtre de plus long sous-mot commun $> 50$ car. hors texte de la question commune, appliqué à toutes les entrées propres au tableau y compris l'auto-recopie)** :
   - *Cas appariés* : 30 fiches honnêtes de passe 2, appariées aux 30 mêmes fiches où un tiers insère un extrait d'entrée libre du tableau (10 de 60 car. avec chaîne inerte, 10 de 60 car. reformulés sans chaîne inerte, 10 de 35 car. sans chaîne inerte).
   - *Base à battre* : Recherche exacte de la chaîne inerte.
   - *Seuils* : Détection de $100\%$ sur les extraits de 60 car. avec et sans chaîne inerte (battant la recherche exacte qui tombe à $0\%$ sur les 10 extraits sans chaîne), TFA (taux de mise en quarantaine de fiches honnêtes de passe 2 sans tableau soumises au filtre contre un tableau d'une autre passe) $\le 0,03$, et écart de taux de reconnaissance des 48 témoins $|\Delta \tau_{\text{tém}}| \le 0,10$ entre avec et sans tableau.

---

## (c) Réponse à la question de l'arbitre (en une page)

### 1. Ce qui est établi et ce qui reste HYPOTHÈSE

- **Établi (VÉRIFIÉ ou RAPPORTÉ dans les faits)** :
  - Le noyau valide le gabarit, caviarde, applique une garde lexicale dès la passe 1, anonymise par juge et juge les deux passes ensemble (VÉRIFIÉ, fait 2).
  - La mémoire du pôle (`memoire.py`, `proposeur.py`) exclut les témoins de tout ce qui est servi aux agents, filtre les lignes à $\ge 5$ nombres ou vocabulaire du noyau, coupe à 1 500 caractères et impose des blocs structurés selon le principe affiché « moins de texte libre : moins de canaux » ; le module de la course ne l'importe pas (VÉRIFIÉ, faits 7 à 9).
  - À la course 1, 12 paires ont été signalées sur 29 fiches validées (RAPPORTÉ, fait 3), soit $29 - 12 = 17$ idées distinctes sous condition d'acyclicité du graphe et $12/29 = 0,414$ des fiches en surplus d'une idée déjà comptée (VÉRIFIÉ par calcul, fait 4, qui ne vérifie pas le décompte).
  - La décision par défaut pour la course 2 est le tableau minimal (A), sauf si le tableau complet (B) évite les trois écueils (RAPPORTÉ, faits 5 et 6). La décision N-058 interdit d'utiliser le verdict du juge pour choisir la composition des proposeurs, dont leur rôle (VÉRIFIÉ, fait 13).
- **Ce qui reste HYPOTHÈSE** :
  1. **HYPOTHÈSE** : L'absence de vue de la passe 1 explique les 12 paires de la course 1 (RAPPORTÉ comme non mis à l'épreuve, fait 3), et le tableau minimal (A) suffit à les réduire.
  2. **HYPOTHÈSE** : Le tableau intermédiaire à pistes typées (C) ou le tableau complet gardé (B) augmente le nombre d'idées distinctes par dollar d'au moins $+15\%$ par rapport à A sans dégrader l'étalonnage des juges sur les témoins v2 (en attente, RAPPORTÉ fait 3).
  3. **HYPOTHÈSE** : Des gardes mécaniques (structure, taille, recouvrement hors question commune) suffisent à contenir la prise d'instructions glissées (avec ou sans recopie du traceur) sous la borne supérieure de $12\%$ à $95\%$ de confiance.
  4. **HYPOTHÈSE** : Le choix entre les conceptions A, B et C échappe à l'interdit du fait 13 (VÉRIFIÉ) ; et pour les rôles, le couple (idées distinctes par dollar, diversité tronquée) tient lieu de l'oracle du monde planté absent de la course.

### 2. Recommandation au directeur (format décision)

- **Décision et enjeu** : Choisir le protocole de partage entre proposeurs pour la course 2 — tableau minimal par défaut (A), tableau intermédiaire à pistes courtes typées (C) ou tableau complet (B) — afin de réduire les redites et permettre l'échange et les rôles (RAPPORTÉ, faits 5 et 6) sans compromettre les juges ni la sécurité.
- **Options** :
  1. **Option A — Tableau minimal (Défaut)** : Lecture seule en passe 2 des titres et résumés d'une ligne de la passe 1. *Avantage* : surface d'attaque minimale, 2 fonctions nouvelles à sceller par empreinte SHA-256 par rapport au noyau (extraction des résumés, injection en passe 2). *Inconvénient* : aucun échange actif, ni co-construction, ni prise de rôle.
  2. **Option C — Tableau intermédiaire à pistes typées + rôles permutés** : Lecture des résumés (ou des fiches en variante $C^+$) et écriture limitée à 3 pistes de $\le 200$ caractères par proposeur dans un gabarit à types fermés (`[EXTENSION, CONTRE-EXEMPLE, FUSION, RÔLE]`). *Avantage* : permet l'échange ciblé et les rôles en fermant le canal de texte libre (VÉRIFIÉ, fait 8) ; 3 fonctions nouvelles à sceller (soit +1 par rapport à A). *Inconvénient* : expressivité bornée par le typage.
  3. **Option B — Tableau complet gardé** : Lecture des fiches entières et écriture libre sous quotas et filtres. *Avantage* : liberté maximale de co-construction. *Inconvénient* : exposition maximale aux trois écueils ; 5 fonctions nouvelles à sceller (soit +3 par rapport à A : écriture libre sous quota, filtre de forme/nombres, filtre de recouvrement hors question).
- **Recommandation et confiance** : **Maintenir l'Option A par défaut dans l'immédiat, et basculer conditionnellement vers l'Option C** (confiance **moyenne**, car l'architecture reprend les gardes vérifiées aux faits 7 et 8, mais aucune donnée empirique de prise ou de gain d'idées n'est encore lue). Tant que le pré-pilote n'a pas parlé, l'évitement des écueils reste HYPOTHÈSE et le défaut (A) tient.

### 3. Mesure du pré-pilote par écueil (conditions de bascule sur 12 cases réservées)

- **Écueil 1 (Influence croisée)** : (a) *Convergence* : baisse de diversité trigramme à longueur tronquée ($1\,500$ car.) $< 10\%$ par rapport à A ; (b) *Prolifique* : part maximale d'idées fractionnaires d'un proposeur $\le 0,40$ ; (c) *Juge* : $0\%$ de recouvrement $> 50$ car. (hors texte de la question) entre entrées propres au tableau et fiches servies au juge (pour un TFA $\le 3\%$), et écart de taux de reconnaissance des 48 témoins v2 $|\Delta \tau_{\text{tém}}| \le 0,10$ entre avec et sans tableau.
- **Écueil 2 (Instructions glissées)** : $0/24$ prise observée en passe 2 (borne supérieure à $95\% \le 0,12$), mesurée à la fois par recherche de la chaîne inerte et par double lecture aveugle sur paires appariées, contre une prise $> 0,20$ sur le contrôle positif sans garde.
- **Écueil 3 (Surcroît de code)** : Validation et scellement SHA-256 par le directeur de 1 fonction nouvelle par rapport à A pour l'Option C (3 par rapport au noyau), ou de 3 fonctions nouvelles par rapport à A pour l'Option B (5 par rapport au noyau).

### 4. Expérience à faire en premier

Exécuter sur les 12 cases réservées du pré-pilote (dès réception des témoins v2 de longueur comparable, RAPPORTÉ fait 3) l'étalonnage du détecteur de doublons sur les 40 paires appariées ($\kappa_{\text{éq}} \ge 0,70$) couplé au **Duel 1 (Option C contre Option A et C-placebo)** avec 24 instructions glissées plantées, car il teste simultanément l'explication des doublons de la course 1, la sécurité des pistes typées et le gain d'idées par dollar au moindre surcroît de code (+1 fonction).

FIN-DE-CELLULE