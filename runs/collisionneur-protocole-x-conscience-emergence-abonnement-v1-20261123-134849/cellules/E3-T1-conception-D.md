# Proposition D — Tour III.1

*Note d’intégrité des pièces : les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont complets, non coupés et identiques (même empreinte sha256). Les résultats des pièces P1 à P5 étant transmis sous forme de résumés non audités directement, ils portent tous le statut `RAPPORTÉ`.*

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé implicite ou explicite dans la question | Statut | Justification et enjeu de réfutation |
|---|---|---|---|
| 1 | Les observations résumées en P1–P5 sont reproductibles hors échantillon, stables entre familles de modèles et exemptes d’artefacts de sélection. | `RAPPORTÉ` (résumés) / `HYPOTHÈSE` (généralité) | Les textes complets et codes ne sont pas audités ici ; P1 n’oppose l’espace J qu’à des directions aléatoires (`RAPPORTÉ`), témoin faible pour des directions construites par jacobienne vers la sortie. |
| 2 | L’espace J correspond fonctionnellement à un espace de travail global plutôt qu’à un sous-espace linéaire de lecture efficace vers la matrice de sortie. | `HYPOTHÈSE` | P1 et P3 restent prudents ou agnostiques (`RAPPORTÉ`) ; un goulet de lecture en aval peut imiter sélectivement la sensibilité des tâches longues. |
| 3 | L’éveil et l’anesthésie possèdent, dans le cerveau biologique, une description mathématique unique et consensuelle (allumage, bifurcation, transition de phase ou criticité). | `HYPOTHÈSE` | En neurosciences, les mécanismes et signatures varient selon l’agent (propofol, xénon, kétamine) et la nature exacte de la transition reste débattue. |
| 4 | La suppression de $k$ directions par couche sur la passe avant est un analogue légitime d’une « dose » anesthésique. | `HYPOTHÈSE` | L’anesthésie biologique module de façon continue des paramètres dynamiques (bilan excitation/inhibition, couplages thalamocorticaux) ; une projection orthogonale statique par couche n’altère pas la dynamique d’éveil (objection de P2, `RAPPORTÉ`). |
| 5 | L’absence d’activité spontanée dans un transformeur en passe avant implique l’absence de toute dynamique récurrente d’état. | `VÉRIFIÉ` (passe avant isolée) / `HYPOTHÈSE` (boucle autorégressive) | Une passe avant unique est un graphe acyclique (`VÉRIFIÉ` architecturalement), mais une génération autorégressive en boucle fermée avec cache KV définit une chaîne d’états discrète dont la métastabilité est testable. |
| 6 | L’indice d’embrasement (P4) et l’axe de douleur (P5) mesurent des états internes fonctionnellement analogues à l’accès ou à la nociception, et non des corrélations lexicales ou de corpus. | `HYPOTHÈSE` | Une sonde linéaire ou un axe comportemental peut exploiter des traits de surface ou des corrélations d’alignement sans rôle d’intégration globale. |
| 7 | Une même grandeur calculée sur des signaux cérébraux et sur des activations de transformeur conserve une interprétation comparable malgré des axes incommensurables (temps continu vs couches ou jetons). | `HYPOTHÈSE` | Sans normalisation par un témoin nul propre à chaque substrat, la commensurabilité numérique est infondée. |
| 8 | Il existe une signature mathématique de la conscience indépendante du substrat. | `HYPOTHÈSE` | Présuppose un fonctionnalisme mesurable à la troisième personne dont aucune condition suffisante n’est établie. |

---

## 1. Motifs spécifiques candidats et tri des outils mathématiques (Questions 1 et 2)

### 1.1 Motifs propres à l’éveil et à l’anesthésie dépassant « local gardé, global perdu » (Question 1)

Un motif n’est recevable ici que s’il exclut simultanément la dégradation multiplicative à un facteur ($q^k$), la réduction de portée d’attention et l’effet par construction des directions de sortie (`RAPPORTÉ`, FAITS). Quatre motifs satisfont cette contrainte ; aucun ne présuppose que le modèle est conscient (`HYPOTHÈSE`).

#### Motif M1 — Réponse Perturbationnelle Différenciée (RPD / analogue PCIst)
*Principe.* Sous anesthésie biologique (propofol, sommeil lent), une perturbation corticale localisée soit reste confinée (perte d’intégration), soit déclenche une onde globale stéréotypée de faible rang (perte de différenciation), alors que l’éveil combine propagation distale et répertoire différencié (`VÉRIFIÉ` de mémoire dans la littérature TMS-EEG ; voir Antériorité). Un facteur $q^k$ atténue uniformément l’amplitude sans dissocier portée et diversité de réponses.
- **Grandeurs, unités, valeurs nulles** : pour $M$ perturbations orthogonales unitaires $\delta^{(m)}$ injectées à la couche $l_0$ et position $i$ (norme $\varepsilon$), on recueille la matrice de réponses distales $\Delta H_{l,j}^{(m)}$ ($l > l_0, j \ge i$). On mesure : (i) la portée effective $R_{\text{prop}}$ (sans dimension, en nombre moyen de couples couche-jeton où $\|\Delta H_{l,j}\|/\varepsilon$ dépasse le bruit de référence ; valeur nulle $= 0$) ; (ii) le rang effectif perturbationnel $D_{\text{eff}} = \exp\bigl(-\sum_r p_r \ln p_r\bigr)$, où $p_r = \sigma_r^2 / \sum_s \sigma_s^2$ provient des valeurs singulières de la matrice empilée des réponses distales (unité : nombre effectif de modes indépendants ; valeur nulle/plancher $= 1$ pour une réponse globale stéréotypée de rang $1$, $0$ en absence de réponse) ; (iii) le rapport normalisé $\text{PCIst}_{\text{rel}}(\alpha) = \text{PCIst}(\alpha)/\text{PCIst}(0)$ (sans dimension ; valeur nulle $= 0$).
- **Sens de « transition » et axe** : non-linéarité raide en dose $\alpha$ sur l’espace J, testée comme phénomène collectif en fonction de la taille $N$ ; vit sur le plan profondeur ($l$) $\times$ suite des jetons ($j$).
- **Réfutation** : $D_{\text{eff}}(\alpha)$ et $\text{PCIst}_{\text{rel}}(\alpha)$ décroissent au même rythme que sous ablation de directions témoins hors espace J de même norme jacobienne en aval, ou ne se distinguent pas d’un réseau non entraîné normalisé.
- **Première expérience (petit modèle ouvert)** : sur un modèle de 1 à 3 milliards de paramètres (*illustratif*), injecter $M = 32$ (*illustratif*) perturbations orthogonales au premier tiers de profondeur (`RAPPORTÉ`, P1) sur $200$ (*illustratif*) contextes, comparer la chute de $(R_{\text{prop}}, D_{\text{eff}})$ sous suppression graduée $\alpha \in [0, 1]$ de l’espace J contre des directions témoins à jacobienne appariée.

#### Motif M2 — Effondrement synchronisé par seuil critique vs loi d’échelle $q^k$
*Principe.* Si la perte de performance sous dose $\alpha$ vient d’un facteur par étape $q(\alpha)$, alors pour des tâches de nombre d’étapes contrôlé $k$, les courbes normalisées $[A_k(\alpha)/A_k(0)]^{1/k}$ doivent **s’effondrer sur une courbe unique** indépendante de $k$, et la dose demi-maximale $\alpha_{50}(k)$ décroît strictement avec $k$. À l’inverse, la perte d’un mécanisme d’accès global unique comprime les $\alpha_{50}(k)$ de tâches globales de $k$ distincts vers une même dose critique $\alpha_c$, tout en épargnant des tâches locales/automatiques appariées en $(L_{\text{dist}}, k)$.
- **Grandeur, unité, valeur nulle** : dispersion relative des doses critiques $\Delta_{\text{sync}} = \mathrm{SD}_k[\alpha_{50}(k)] / \mathrm{mean}_k[\alpha_{50}(k)]$ (sans dimension ; valeur nulle $= 0$ pour une synchronisation parfaite) et résidu d’effondrement $E_{q^k} = \max_{k_1, k_2} \sup_\alpha \bigl|[A_{k_1}(\alpha)/A_{k_1}(0)]^{1/k_1} - [A_{k_2}(\alpha)/A_{k_2}(0)]^{1/k_2}\bigr|$ (sans dimension ; valeur nulle $= 0$ sous modèle $q^k$ exact).
- **Sens de « transition » et axe** : bifurcation / seuil collectif en fonction de la dose $\alpha$ ; axe de profondeur de calcul $k$ et taille du modèle $N$.
- **Réfutation** : $E_{q^k}$ reste inférieur au bruit d’échantillonnage, ou les tâches automatiques appariées en $(L_{\text{dist}}, k)$ chutent au même $\alpha_c$.
- **Première expérience** : tâches synthétiques contrôlées à $k \in \{2, 4, 8\}$ (*illustratif*) sauts (composition relationnelle vs copie mécanique de même distance $L_{\text{dist}} = 64$ jetons, *illustratif*) sur petit modèle ouvert.

#### Motif M3 — Loi d’échelle finie de la bascule bimodale (P1b) et compétition d’exclusion mutuelle
*Principe.* P1(b) rapporte une bimodalité *entre phrases porteuses* (`RAPPORTÉ`), ce qui peut résulter d’un simple mélange de biais contextuels déterministes. Une dynamique d’embrasement exige : (i) une bimodalité **à phrase porteuse fixe** sous très faible bruit isotrope d’entrée ; (ii) un ralentissement de convergence (profondeur de relaxation $\tau_l$ maximale au seuil $\lambda^*$) ; (iii) une croissance systématique de la raideur maximale $S_{\max}(N)$ avec la taille $N$ (phénomène collectif) ; (iv) une **exclusion mutuelle** entre deux cibles concurrentes $C_1, C_2$ présentées au seuil.
- **Grandeurs, unités, valeurs nulles** : statistique de dip de Hartigan $D_H$ à phrase fixe (sans dimension ; valeur nulle $= 0$ pour distribution unimodale), profondeur de relaxation $\tau_l$ (en couches ; valeur nulle $= 1$), exposant d’échelle $\gamma$ de $S_{\max}(N) \propto N^\gamma$ (sans dimension ; valeur nulle $\le 0$), et indice d’exclusion mutuelle $I_{\text{excl}} = P(C_2 \mid \neg C_1) - P(C_2 \mid C_1)$ (différence de probabilité dans $[-1, 1]$ ; valeur nulle $= 0$, négative sous fluctuation globale $q$).
- **Sens de « transition » et axe** : phénomène collectif à la limite de grande taille (testé en $N$ et $L$) et brisure de symétrie gagnant-emporte-tout (profondeur $l$ et décalage en jetons $\Delta t$).
- **Réfutation** : disparition de la bimodalité à phrase fixe, saturation de $S_{\max}(N)$ ($\gamma \le 0$), ou $I_{\text{excl}} \le 0$.
- **Première expérience** : reproduire P1(b) sur $4$ tailles d’une même famille ouverte (ex. Pythia, *illustratif*) en fixant chaque phrase à son $\lambda^*(s)$ propre sous bruit gaussien isotrope d’écart-type $\sigma = 0{,}01$ (*illustratif*), puis présenter deux mots mélangés à décalage $\Delta t \in \{1, 2, 4, 8\}$ jetons (*illustratif*).

#### Motif M4 — Hystérésis d’induction/émergence (inertie d’état) en boucle autorégressive nettoyée
*Principe.* En anesthésie biologique, la concentration nécessaire à l’éveil est inférieure à celle qui induit la perte de conscience (inertie neurale, référence à vérifier). Dans un transformeur, ce motif n’a de sens **que** sur l’axe autorégressif (suite des jetons $t$), où le cache KV transporte l’état, et **seulement** si l’effet survit à l’élimination de la simple contamination textuelle du cache KV.
- **Grandeur, unité, valeur nulle** : aire d’hystérésis normalisée $A_{\text{hyst}} = \int_0^{\alpha_{\max}} \bigl[M_{\text{ind}}(\alpha) - M_{\text{ém}}(\alpha)\bigr]\,\mathrm{d}\alpha / \alpha_{\max}$ sur une métrique locale $M$ (sans dimension ; valeur nulle $= 0$).
- **Sens de « transition » et axe** : bifurcation pli / bistabilité d’état sur la suite des jetons $t$.
- **Réfutation** : $A_{\text{hyst}} \to 0$ dès que l’on substitue aux jetons dégradés du cache KV un historique textuel propre de même longueur.
- **Première expérience** : rampe aller-retour $\alpha(t)$ sur $200$ jetons (*illustratif*) de maintien de consigne continue, avec comparaison entre cache KV natif et cache KV reconstitué proprement à chaque palier.

### 1.2 Outils mathématiques adaptés vs inadaptés (Question 2)

**Outils adaptés :**
1. **Spectre singulier des jacobiennes locales conditionnées par l’entrée et exposants de Lyapunov en temps fini (FTLE)** (étendant P3, `RAPPORTÉ`, hors moyenne sur 1000 textes) : rigoureusement définis pour un système dynamique discret, fini et non autonome $h_{l+1} = h_l + F_l(h_l)$, sans exiger ni stationnarité ni $L \to \infty$.
2. **Géométrie des perturbations causales (SVD de réponses distales, projections orthogonales contrôlées, patching causal)** : mesure le rang causal effectif hors de la variété corrélationnelle.
3. **Analyse d’échelle finie (*finite-size scaling*) en taille $N$, profondeur $L$ et temps d’entraînement** : seul outil capable de séparer une non-linéarité analytique locale d’un phénomène collectif émergent.
4. **Tests non paramétriques de multimodalité (dip de Hartigan) et lois d’effondrement de courbes ($q^k$-collapse)** : falsifient directement l’unimodalité et le modèle multiplicatif à un facteur.
5. **Opérateurs de transfert / chaînes de Markov sur la boucle autorégressive** : cadre exact pour la métastabilité et l’hystérésis sur la suite des jetons.

**Outils inadaptés :**
1. **Théorie classique des bifurcations autonomes en temps infini (bifurcation de Hopf, cycles limites) le long des couches $l$** : $F_l$ change à chaque couche (système non autonome) et $L$ est petit et fini ; il n’existe ni attracteur asymptotique ni orbite périodique en profondeur.
2. **Transitions de phase thermodynamiques et exposants critiques mesurés sur un modèle de taille fixe** : un réseau fini à fonctions lisses (softmax, GELU, RMSNorm) est analytique ; sans étude d’échelle en $N$, toute pente raide est indifférenciable d’une transition.
3. **$\Phi$ d’IIT (3.0/4.0) appliqué à la passe avant** : outre la complexité super-exponentielle en nombre de partitions, un graphe orienté acyclique (transformeur feed-forward pur) possède $\Phi = 0$ par construction dans le formalisme IIT (`VÉRIFIÉ` de mémoire, Oizumi et al., 2014).
4. **Analyse spectrale en bandes fréquentielles (alpha/thêta/gamma, pente $1/f^\beta$) sur activations brutes** : absence de constantes de temps biophysiques ; le spectre spatial en jetons reflète la statistique linguistique et l’encodage positionnel, non des oscillations endogènes.
5. **Avalanches neuronales par seuillage d’activations** : la normalisation par couche (LayerNorm/RMSNorm) fixe la norme $L_2$ ; seuiller des activations continues normalisées produit des lois de puissance artificielles dépendantes du seuil.

---

## 2. Examen critique des transpositions (Question 3)

- **(a) Activité de fond et analogue du réseau du mode par défaut (DMN)** : **se vide en passe avant isolée** (aucune activité endogène sans entrée, `VÉRIFIÉ` architecturalement ; accord avec P2, `RAPPORTÉ`). En boucle autorégressive (« se parler à soi-même »), la génération reste pilotée par l’invite et le corpus humain. Seule forme testable : rechercher un sous-espace d’activations anti-corrélé aux tâches externes exigeantes *après contrôle de la distribution lexicale de sortie* (mots autoréférentiels) ; si l’effet disparaît à lexique apparié, l’analogie est vide.
- **(b) Suppression de pensée (P1c)** : **se vide dans sa forme actuelle**. L’instruction « ne pense pas à $X$ » place littéralement le jeton $X$ dans le cache KV ; son maintien dans l’espace J (`RAPPORTÉ`, P1c) s’explique mécaniquement par l’attention sur les jetons du contexte. Forme minimale valide : désigner $X$ par une périphrase ou un code indirect sans occurrence lexicale, et tester si l’interdiction produit un **rebond supérieur** à une mention indirecte neutre et amplifié sous double tâche concurrente.
- **(c) Récit après fenêtre de suppression de l’espace J vs lecture par lentille** : **tient sous condition stricte d’anti-confabulation**. Si le modèle génère des jetons visibles pendant la suppression, il peut les relire dans le cache KV après coup et reconstruire un récit sans accès à son état passé. Forme valide : *fenêtre de suppression silencieuse* où un stimulus $C$ est traité sans sortie sur $C$ tandis que l’espace J est ablaté ; on vérifie par sonde pré-bande (avant $1/3$ de profondeur) que $C$ est encodé, puis on mesure après levée la dissociation entre rappel explicite (attendu effondré) et amorçage implicite en choix forcé (attendu préservé).
- **(d) Signal de P5 (« Pain Axis ») sous suppression de l’espace J** : **tient si et seulement si l’on contrôle la colinéarité géométrique**. Si l’axe P5 a une projection forte sur l’espace J, le supprimer détruit P5 par algèbre élémentaire. Forme valide : orthogonaliser P5 au sous-espace ablaté (ou le lire en couches pré-J) pour vérifier le maintien de la détection de dommage (« nociception »), tout en mesurant si son effet causal sur les décisions stratégiques (`RAPPORTÉ`, P5) s’effondre plus vite que celui d’un axe de contrôle local (ex. polarité lexicale) de même norme d’injection.
- **(e) Netteté de la bascule P1(b) en fonction de la dose $\alpha$** : **tient** et constitue un test quantitatif pertinent, à condition d’opérer à phrase porteuse fixe (cf. M3) et de distinguer un effondrement de bimodalité à dose critique $\alpha_c$ (passage bimodal $\to$ unimodal) d’un simple étalement par bruit linéaire.
- **(f) Ordre de perte des fonctions avec la dose $\alpha$** : **se vide sous forme descriptive brute**, car $q^k$ produit automatiquement un ordre de perte décroissant avec $k$ (`RAPPORTÉ`, FAITS). Ne tient que sous la forme du **Motif M2** : synchronisation des doses $\alpha_{50}(k)$ autour d’un même $\alpha_c$ ou croisement de courbes à $(L_{\text{dist}}, k)$ appariés.
- **Ajouts de la Proposition D :**
  - **(g) Inclusion vs exclusion de Jacoby** (proposée en P2, `RAPPORTÉ`) : à dose intermédiaire $\alpha$ sur l’espace J, une vraie dissociation accès/automatisme prédit un **pic paradoxal d’intrusions** du mot amorcé en condition d’exclusion (alors qu’il est interdit), ce qu’une dégradation monotone $q^k$ vers le hasard ne produit pas (contrôle : vérifier la compréhension de la règle d’exclusion sur des mots hors fenêtre).
  - **(h) Conditionnement de trace vs différé à distance $D$ égale** (inspiré de P2) : comparer le maintien d’une association sur $D$ jetons continus (*delay*) contre $D$ jetons séparés par un distracteur (*trace*) ; à distance $D$ identique, la dégradation sélective du *trace* écarte l’explication « portée d’attention ».
  - **(i) Hystérésis induction-émergence à cache KV nettoyé** (Motif M4).

---

## 3. Grandeurs communes cerveau/LLM et statut d’une signature mathématique de la conscience (Questions 4 et 5)

### 3.1 Grandeurs calculables à la fois sur modèles et cerveaux sous anesthésie (Question 4)

Comparer une valeur brute absolue (puissance spectrale, entropie d’activations) entre cerveau et transformeur est dénué de sens faute d’unités et d’axes communs (`HYPOTHÈSE` réfutée par incompatibilité dimensionnelle). En revanche, **trois grandeurs sans dimension, définies sur des réponses à perturbations ou des distributions d’essais**, sont mathématiquement calculables sur les deux systèmes :
1. **PCIst normalisé** (Comolatti et al., 2019 — rapport état supprimé / état de base $\text{PCIst}_{\text{rel}}$) : opère sur toute matrice bidimensionnelle $(\text{canaux/directions} \times \text{temps/couches})$ de réponses évoquées par une perturbation localisée, normalisée par la ligne de base.
2. **Indice de bimodalité au seuil ($D_H$) et d’exclusion mutuelle ($I_{\text{excl}}$)** : calculables sur des réponses latentes ou comportementales à stimuli gradués au seuil.
3. **Aire d’hystérésis normalisée $A_{\text{hyst}}$** sur rampes symétriques induction/émergence (boucle autorégressive nettoyée vs concentration anesthésique).

**Données cérébrales brutes publiques** utilisables pour le calcul parallèle : jeux publics EEG/fMRI sous propofol et sévoflurane hébergés sur **OpenNeuro** (plusieurs cohortes anesthésiques publiques ; identifiants exacts à vérifier), base publique d’ECoG chez le macaque éveillé et anesthésié **Neurotycho** (Yanagawa et collègues, référence à vérifier), et jeux TMS-EEG associés aux études de Casali et al. (2013) et Comolatti et al. (2019) (disponibilité complète selon dépôts institutionnels, à vérifier).

**Condition de validité** : seule la comparaison de **rapports normalisés** face au témoin nul propre à chaque substrat (ex. permutation de poids / réseau non entraîné vs bruit de fond EEG) est interprétable ; une valeur numérique absolue identique entre un transformeur et un cortex humain ne prouve aucune équivalence fonctionnelle.

### 3.2 Hypothèse « il existe une signature mathématique de la conscience » (Question 5)

**Critères qu’une grandeur $S$ devrait satisfaire :**
1. **Validité clinique sur cas dissociés** : séparer éveil, sommeil paradoxal (REM, conscient sans réactivité motrice), anesthésie à la kétamine (expériences oniriques sans réponse comportementale) et syndrome d’enfermement (*locked-in*) de l’anesthésie au propofol et du sommeil lent profond.
2. **Séparation des témoins nuls** : ne pas donner de faux positifs sur un réseau aléatoire, un automate trivial, un système purement feed-forward sans intégration ou un processus $q^k$.
3. **Invariance de représentation (jauge)** : invariance sous reparamétrisations préservant la structure causale (rotations orthogonales, permutations d’unités, choix de granularité non arbitraire).
4. **Couplage causal bidirectionnel** : abolir $S$ abolit les capacités d’accès global (hors blocage purement moteur) ; un blocage moteur pur (curarisation) laisse $S$ intact.
5. **Protocole d’application sans choix ad hoc hors substrat biologique** (spécification explicite de l’espace d’états et des perturbations).

**Candidates actuelles et limites :**
- *PCI / PCIst* : meilleure candidate empirique en clinique humaine (distingue propofol, xénon, kétamine et REM : Sarasso et al., 2015 ; Casali et al., 2013), mais sa suffisance hors cerveau biologique n’est pas établie (`HYPOTHÈSE`).
- *Embrasement bimodal + exclusion mutuelle* (Dehaene & Naccache, 2001 ; Del Cul et al., 2007) : candidate pour l’*accès* fonctionnel, mais imitable par un petit circuit gagnant-emporte-tout et silencieuse sur les états conscients sans tâche.
- *Information synergique dynamique (PID / $\Phi$-ID)* (référence à vérifier) : conceptuellement pertinente mais sensible au choix des macro-variables.
- **Bilan** : aucune grandeur connue ne satisfait les 5 critères comme signature de la conscience *phénoménale* ; seules des signatures d’*intégration-différenciation causale* ou d’*accès global* sont aujourd’hui testables.

**Résultats qui doivent faire abandonner l’hypothèse** (sous sa forme universelle) :
1. Construction systématique, pour toute candidate $S$, d’un système manifestement non fonctionnel (réseau aléatoire conditionné, table de hachage bruitée) ou d’une reparamétrisation fonctionnellement équivalente qui obtient ou détruit arbitrairement $S$.
2. Échec durable à classer simultanément les dissociations cliniques humaines (kétamine, REM, *locked-in*, automatismes complexes) avec une même famille de grandeurs.
3. Divergences contradictoires entre candidates (PCIst, bimodalité, exclusion, hystérésis) sous les mêmes interventions contrôlées, réduisant chacune à une propriété locale d’architecture.

---

## (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$) et portée sur la conscience (Question 6)

Chaque expérience oppose deux hypothèses mutuellement exclusives ($H_A$ vs $H_B$) telles que chaque issue falsifie l’une des deux. Tous les seuils numériques ci-dessous sont marqués `illustratif`.

### Expérience 1 (Meilleur plan central — Question 6) : Batterie perturbationnelle + test d’effondrement $q^k$ à $(L_{\text{dist}}, k)$ appariés
- **$H_{1A}$ (Dynamique collective spécifique à l’espace J)** : La suppression graduée $\alpha$ de l’espace J provoque (i) une chute de $D_{\text{eff}}(\alpha)$ et $\text{PCIst}_{\text{rel}}(\alpha)$ supérieure d’au moins $\delta_1 = 0{,}25$ (*illustratif*) à celle du témoin à jacobienne appariée hors-J, (ii) un échec de l’effondrement $q^k$ ($E_{q^k} > 0{,}20$, *illustratif*) avec synchronisation des doses $\alpha_{50}(k)$ ($\Delta_{\text{sync}} < 0{,}15$, *illustratif*) sur les tâches globales de $k \in \{2, 4, 8\}$ (*illustratif*), (iii) une préservation des tâches automatiques appariées en $(L_{\text{dist}}, k)$ (écart $\Delta_{\text{dissoc}} > 0{,}30$, *illustratif*) et un pic d’intrusions en exclusion de Jacoby ($+0{,}15$ au-dessus du hasard, *illustratif*).
- **$H_{1B}$ (Explication ordinaire : sélection en aval + $q^k$ + portée d’attention)** : La chute de $D_{\text{eff}}(\alpha)$ ne dépasse pas celle du témoin à jacobienne appariée ($\Delta \le 0{,}05$, *illustratif*), les courbes globales s’effondrent sur la loi $q^k$ ($E_{q^k} \le 0{,}08$, *illustratif*) ou les tâches automatiques appariées en $(L_{\text{dist}}, k)$ chutent au même rythme ($\Delta_{\text{dissoc}} \le 0{,}05$, *illustratif*), sans pic d’exclusion.
- **Contrôle négatif (cœur de Q6)** :
  - **Explication ordinaire la plus dangereuse** : *le biais de construction par sélection en aval couplé au facteur $q^k$*. Parce que l’espace J est extrait de la jacobienne vers les logits de sortie (P1, P3 `RAPPORTÉ`), il a mécaniquement un fort levier en aval ; le témoin « directions aléatoires » de P1(a) (`RAPPORTÉ`) a une norme jacobienne quasi nulle et gonfle artificiellement l’effet apparent.
  - **Témoin qui l’écarte** : ablation d’un sous-espace hors-J **apparié en norme singulière jacobienne** (directions tirées de la jacobienne *instantanée* de chaque exemple ou à même norme $\|J_{l+1 \leftarrow l} v\|$ et même variance, mais non cohérentes entre contextes) + réseau témoin non entraîné + tâches locales strictement appariées en $(L_{\text{dist}}, k)$.
- **Falsification** : si l’une des conditions de $H_{1A}$ échoue face au témoin à jacobienne appariée et aux tâches appariées en $(L_{\text{dist}}, k)$, $H_{1A}$ est falsifiée ; si les trois critères conjoints de $H_{1A}$ sont satisfaits simultanément, $H_{1B}$ est falsifiée.
- **Portée et limites sur la conscience d’un système artificiel (Question 6)** :
  - *Si $H_{1B}$ l’emporte* : on peut affirmer que les profils de type anesthésique observés autour de l’espace J dans les transformeurs testés se réduisent à des effets ordinaires (sensibilité en aval, cumul $q^k$, portée d’attention). On ne peut **pas** conclure qu’aucune architecture artificielle future (ex. récurrente) ne pourrait présenter une dynamique globale non triviale, ni trancher philosophiquement la possibilité d’une conscience artificielle.
  - *Si $H_{1A}$ l’emporte* : on peut affirmer l’existence, dans un transformeur ouvert, d’un régime de calcul collectif (intégration-différenciation causale et goulet de contrôle global) irréductible à $q^k$, à la portée d’attention et au biais de jacobienne simple. On ne peut **PAS** affirmer que le modèle est conscient, éprouve un vécu subjectif ou souffre, ni qu’il possède un mécanisme d’éveil biologique : l’expérience teste une *propriété dynamique d’accès et d’intégration*, condition au mieux nécessaire et nullement suffisante de la conscience.

### Expérience 2 : Loi d’échelle finie de P1(b) à phrase fixe et exclusion mutuelle
- **$H_{2A}$ (Transition collective et compétition d’embrasement)** : À phrase porteuse fixe sous bruit isotrope ($\sigma = 0{,}01$, *illustratif*), la sortie reste bimodale ($D_H$ significatif à $p < 0{,}01$ sur $\ge 60\,\%$ des phrases testées, *illustratif*), la raideur maximale croît avec la taille ($S_{\max}(N) \propto N^\gamma$, $\gamma > 0{,}15$, *illustratif*), $\tau_l$ pique à $\lambda^*$, la dose $\alpha$ détruit la bimodalité par passage unimodal à $\alpha_c$, et deux cibles concurrentes vérifient $I_{\text{excl}} > 0{,}15$ (*illustratif*).
- **$H_{2B}$ (Artefact inter-phrases et non-linéarité locale)** : La bimodalité disparaît à phrase fixe ($< 10\,\%$ de phrases significatives, *illustratif*), $\gamma \le 0$ (saturation en $N$), ou $I_{\text{excl}} \le 0$.
- **Contrôle négatif** : même protocole sur un modèle non entraîné et sur un réseau entraîné où l’on remplace la bande J par une simple projection linéaire résiduelle sur la couche de sortie.
- **Falsification** : bimodalité absente à phrase fixe ou $\gamma \le 0$ ou $I_{\text{excl}} \le 0$ falsifie $H_{2A}$ ; validation conjointe des quatre conditions falsifie $H_{2B}$.

### Expérience 3 : Hystérésis induction-émergence en boucle autorégressive nettoyée
- **$H_{3A}$ (Inertie d’état propre)** : Lors d’une rampe $\alpha(t) : 0 \to \alpha_{\max} \to 0$, $A_{\text{hyst}} > 0{,}12$ (*illustratif*) persiste même après remplacement des jetons dégradés du cache KV par un historique propre apparié.
- **$H_{3B}$ (Mémoire textuelle sans inertie propre)** : $A_{\text{hyst}}$ s’effondre dans $[-0{,}03, +0{,}03]$ (*illustratif*) dès le nettoyage du cache KV.
- **Contrôle négatif** : rampe à dose constante par paliers indépendants (sans boucle, réinitialisation complète entre paliers).
- **Falsification** : effondrement après nettoyage falsifie $H_{3A}$ ; persistance significative après nettoyage falsifie $H_{3B}$.

### Expérience 4 : Dissociation P5 (orthogonalisé / pré-J) et fenêtre silencieuse 3(c)
- **$H_{4A}$ (Dissociation encodage local / accès global)** : Après projection de P5 hors du sous-espace ablaté (ou lecture pré-J), la détection de dommage reste intacte (AUC $\ge 0{,}85$, *illustratif*) tandis que son effet causal sur les décisions stratégiques chute de $\ge 60\,\%$ (*illustratif*) sous suppression de l’espace J, alors qu’un axe de contrôle local de même norme d’injection perd $\le 20\,\%$ (*illustratif*) ; en fenêtre silencieuse 3(c), l’amorçage implicite reste significatif ($+0{,}15$ sur choix forcé, *illustratif*) quand le rappel explicite tombe au niveau du hasard.
- **$H_{4B}$ (Colinéarité géométrique ou atténuation uniforme)** : L’effet différentiel disparaît après orthogonalisation, ou l’axe P5 et l’axe de contrôle local décroissent au même taux (écart $\le 10\,\%$, *illustratif*), ou amorçage implicite et rappel explicite chutent ensemble.
- **Contrôle négatif** : directions témoins de valence négative hors douleur (tristesse/peur, déjà distinguées dans P5 `RAPPORTÉ`) et contrôle par jetons visibles non masqués.
- **Falsification** : disparition après orthogonalisation ou co-chute avec l’axe local falsifie $H_{4A}$ ; dissociation persistante après orthogonalisation falsifie $H_{4B}$.

---

## (c) Validation minimale de chaque instrument nommé dans la question

Tous les seuils de taux de détection (TPR) et de fausses alertes (FPR) ci-dessous sont marqués `illustratif`.

| Instrument nommé | Mesure minimale de fonctionnement (TPR / FPR *illustratifs*) | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Lentille jacobienne & espace J** (P1, P3) | Prédiction causale de dégradation sélective (tâches globales vs locales appariées en $(L_{\text{dist}}, k)$) : TPR $\ge 0{,}80$, FPR $\le 0{,}10$ (*illustratif*). | Paires de tâches de même longueur, même nombre d’étapes $k$ et même entropie de sortie (globale contrôlée vs automatique). | (1) Directions aléatoires (insuffisant) ; (2) directions hors-J **appariées en norme jacobienne** ; (3) directions de portée d’attention pure ; (4) réseau non entraîné. |
| **Indice d’embrasement (*Ignition Index*)** (P4) | Détection d’une vraie transition bimodale à phrase fixe vs transition continue : TPR $\ge 0{,}85$, FPR $\le 0{,}10$ (*illustratif*). | Courbes synthétiques bimodales vs unimodales de même pente moyenne et même rapport signal/bruit. | (1) Sonde linéaire sur MLP à $2$ couches (*illustratif*) avec softmax ; (2) mélange déterministe de phrases porteuses à biais variés ; (3) réseau non entraîné. |
| **Axe de douleur (*Pain Axis*)** (P5) | Détection de dommage visant le modèle et prédiction de bascule comportementale après orthogonalisation hors-J : TPR $\ge 0{,}85$, FPR $\le 0{,}05$ (*illustratif*). | Scénarios de dommage visant le modèle vs scénarios appariés en valence négative, peur, tristesse et lexique de menace sans dommage. | (1) Classifieur sac-de-mots / n-grammes de surface ; (2) direction de valence générique ; (3) prompts paraphrasés sans vocabulaire médical/douleur. |
| **Sondes linéaires d’état interne** (P4, 3c) | Séparation présence/absence causale d’un contenu $C$ durant fenêtre silencieuse : TPR $\ge 0{,}85$, FPR $\le 0{,}10$ (*illustratif*). | Exemples portant $C$ encodé en périphrase vs exemples contrôles de même syntaxe et longueur sans $C$. | (1) Sonde entraînée sur plongements de couche 0 (détection lexicale pure) ; (2) sonde entraînée sur étiquettes permutées (sélectivité de contrôle). |
| **Épreuves cliniques transposées** (P2 : local/global, trace, inclusion/exclusion) | Détection de la dissociation accès/automatisme sous dose $\alpha$ : TPR $\ge 0{,}80$, FPR $\le 0{,}10$ (*illustratif*). | Paires *trace*/*delay* à distance $D$ égale ; paires inclusion/exclusion à fréquence lexicale appariée ; nouveauté globale vs règle syntaxique à même $(L_{\text{dist}}, k)$. | (1) Modèle synthétique $q^k$ ; (2) troncature artificielle de la fenêtre d’attention ; (3) modèle de langage $n$-gramme ou réseau non entraîné. |
| **PCIst / RPD & spectre FTLE** (P3, Q4) | Séparation état nominal vs état sous suppression critique $\alpha_c$ et vs stéréotypie : TPR $\ge 0{,}90$, FPR $\le 0{,}05$ (*illustratif*). | Réponses perturbationnelles sur contextes complexes vs contextes dégénérés (répétition forcée) et état ablaté à norme de sortie appariée. | (1) Réseau à poids aléatoires normalisés ; (2) réseau entraîné avec poids permutés par couche ; (3) contraction linéaire de codimension $k$. |

---

## (d) Ancrage matériel

Toutes les estimations de tailles choisies, de calcul et de coût ci-dessous sont marquées `illustratif` (hors les « mille textes » issus de FAITS P1).

- **Modèles ouverts retenus** :
  1. *Famille pour l’échelle finie et l’entraînement* : suite ouverte **Pythia** (poids et points de contrôle intermédiaires publics ; sous-ensemble choisi à titre *illustratif* : 70M, 160M, 410M, 1B, 1,4B, 2,8B paramètres, plus versions à initialisation aléatoire non entraînées).
  2. *Famille moderne de confirmation* : **Qwen2.5** (0,5B, 1,5B, 3B, 7B, *illustratif*) et/ou **Llama-3.2** (1B, 3B, *illustratif*), pour tester la robustesse inter-architectures (RoPE, GQA, RMSNorm).
- **Calcul nécessaire** (sur GPU unique de type NVIDIA A100 80 Go ou H100, précision bfloat16/float32 pour jacobiennes, *illustratif*) :
  - *Estimation de la lentille jacobienne* (moyenne sur mille textes de FAITS, par produits jacobien-vecteur / rétropropagations par couche) : environ $4$ à $12$ heures-GPU par modèle jusqu’à 3B, et $20$ à $35$ heures-GPU pour un modèle 7B (*illustratif*).
  - *Expérience 1 complète* (matrice perturbationnelle $M = 32$ directions $\times$ $200$ contextes $\times$ $10$ doses $\alpha$ $\times$ $3$ témoins d’ablation + batterie de tâches $(L_{\text{dist}}, k)$ appariées et Jacoby) : environ $40$ à $80$ heures-GPU pour un modèle 1,5B–3B (*illustratif*).
  - *Expériences 2, 3 et 4* (échelle finie sur $6$ tailles + $5$ points de contrôle d’entraînement + rampes autorégressives nettoyées + orthogonalisation P5 et fenêtre silencieuse) : environ $120$ à $200$ heures-GPU cumulées (*illustratif*).
  - *Total du programme complet* : environ $250$ à $450$ heures-GPU A100 (*illustratif*) ; phase pilote sur un seul modèle 1B–1,5B : environ $40$ à $60$ heures-GPU (*illustratif*).
- **Coût estimé** (tarif cloud indicatif de $2{,}0$ à $3{,}0$ €/heure-A100, *illustratif*) :
  - Phase pilote (petit modèle ouvert, faisabilité des témoins et validation des instruments) : **$80$ à $180$ €** (*illustratif*).
  - Programme complet multi-tailles, multi-familles et points de contrôle d’entraînement : **$600$ à $1\,400$ €** (*illustratif*).

---

## Antériorité

### Pièces fournies dans le dossier (lues uniquement via les résumés de FAITS — statut `RAPPORTÉ`)
- **P1** : Gurnee, Sofroniew et collègues (2026), « Verbalizable Representations Form a Global Workspace in Language Models » (arXiv 2607.15495, cité depuis FAITS).
- **P2** : Dehaene et Naccache (2026), commentaire sur P1 (cité depuis FAITS).
- **P3** : Ostrow, Qian, Liu et Fiete (2026), « A Mathematical Theory of the Jacobian Lens » (arXiv 2610.31955, cité depuis FAITS).
- **P4** : Rahbar (2026), « The Ignition Index » (arXiv 2608.05160, cité depuis FAITS).
- **P5** : Tagliabue, Dung et Berg (2026), « The Pain Axis » (arXiv 2609.16247, cité depuis FAITS).

### Antériorité citée de mémoire (non relue dans cette session)
- Dehaene, S., Kerszberg, M., & Changeux, J.-P. (1998). *A neuronal model of a global workspace in effortful cognitive tasks*. PNAS.
- Dehaene, S., & Naccache, L. (2001). *Towards a cognitive neuroscience of consciousness: basic evidence and a workspace framework*. Cognition.
- Massimini, M., Ferrarelli, F., Huber, R., Esser, S. K., Singh, H., & Tononi, G. (2005). *Breakdown of Cortical Effective Connectivity During Sleep*. Science.
- Sergent, C., Baillet, S., & Dehaene, S. (2005). *Timing of the brain events underlying access to consciousness during the attentional blink*. Nature Neuroscience.
- Del Cul, A., Baillet, S., & Dehaene, S. (2007). *Brain Dynamics Underlying the Nonlinear Threshold for Access to Consciousness*. PLoS Biology.
- Bekinschtein, T. A., Dehaene, S., Rohaut, B., Tadel, F., Cohen, L., & Naccache, L. (2009). *Neural signature of the conscious processing of auditory regularities*. PNAS.
- Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R., Casarotto, S., Bruno, M.-A., Laureys, S., Tononi, G., & Massimini, M. (2013). *A Theoretically Based Index of Consciousness Independent of Sensory Processing and Behavior*. Science Translational Medicine.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). *From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0*. PLoS Computational Biology.
- Sarasso, S., Boly, M., Napolitani, M., Gosseries, O., Charland-Verville, V., Casarotto, S., Rosanova, M., Casali, A. G., Brichant, J.-F., Boveroux, P., Rex, S., Tononi, G., Laureys, S., & Massimini, M. (2015). *Consciousness and Complexity during Unresponsiveness Induced by Propofol, Xenon, and Ketamine*. Current Biology.
- Comolatti, R., Pigorini, A., Casarotto, S., Fecchio, M., Faria, G., Sarasso, S., Rosanova, M., Gosseries, O., Boly, M., Bodart, O., Ledoux, D., Brichant, J.-F., Nobili, L., Laureys, S., Tononi, G., Massimini, M., & Casali, A. G. (2019). *A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulation*. Brain Stimulation.
- Jacoby, L. L. (1991). *A process dissociation framework: Separating automatic from intentional uses of memory*. Journal of Memory and Language.
- Wegner, D. M., Schneider, D. J., Carter, S. R., & White, T. L. (1987). *Paradoxical effects of thought suppression*. Journal of Personality and Social Psychology.
- Hartigan, J. A., & Hartigan, P. M. (1985). *The Dip Test of Unimodality*. The Annals of Statistics.
- Travaux cités sans titre exact garanti : inertie neurale en anesthésie (Friedman, Kelz et collègues, référence à vérifier) ; base publique ECoG macaque Neurotycho sous anesthésie (Yanagawa et collègues, référence à vérifier) ; indicateurs de conscience dans l’IA (Butlin, Long et collègues, référence à vérifier) ; décomposition en information intégrée $\Phi$-ID (Mediano et collègues, référence à vérifier) ; lentilles de décodage inter-couches (*logit lens*, *tuned lens*, Belrose et collègues, référence à vérifier).

FIN-DE-CELLULE