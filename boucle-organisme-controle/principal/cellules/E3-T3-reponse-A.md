# Proposition A : tour III.3, réponse aux critiques

**Remarques préalables.**
- **Pièces reçues.** FAITS, QUESTION, ma conception III.1 et les critiques de B et de C. Aucune ne paraît coupée. Je n'ai pas recalculé les empreintes sha256.
- **Périmètre.** Je ne réponds qu'aux sections « Sur la proposition A ».
- **Statuts.** Quand je cite B ou C, je conserve les statuts qu'ils donnent à leurs énoncés : contester un raisonnement ne revient pas à changer un statut. Les FAITS restent RAPPORTÉ. Mes énoncés restent HYPOTHÈSE, sauf les dérivations élémentaires, que je signale.
- **Forme.** Je suis le livrable du tour, (a), (b) et (c). La structure en sept sections demandée par l'arbitre a été traitée en III.1. Les corrections ci-dessous modifient les §3.3, 3.4, 4.1, 4.3 et 7 de III.1.
- **Coquille.** En III.1, l'expérience E1 contient un `$H_A`` mal fermé, sans effet sur le fond.

---

## (a) Verdict sur chaque critique

Notation : « B-a2 » désigne la critique de B, partie (a), point 2.

| # | Critique(s) | Verdict | Raison et correction |
|---|---|---|---|
| 1 | Réutilisation de $D_{\text{dev}}$ à la fois pour la sélection s3, le retour, l'évaluation de E1 et celle de E4 (B-a1, C-a2) | **Acceptée** | C'est une fuite réelle de ma conception. Correction : six réservoirs disjoints et hachés (§b.0). |
| 2 | $\hat P(\text{succès}\mid p)$ calibrée sur les issues de s4 (B-a1, C-a2, B-b2, C-b3) | **Acceptée sur trois points, rejetée sur un** | **Acceptée.** (i) Sous la lecture stricte de la séparation (RAPPORTÉ), $\hat P$ est interdite, et je ne l'avais pas placée sous la condition NC4. (ii) Avec $r\le R$ issues rares, $\hat P$ dégénère (B-b2). (iii) $V$ et $\lambda$ n'ont aucun estimateur (C-b3). **Rejetée : « canal non comptabilisé » (C-a2).** Si $\hat P$ ne dépend de $D_{\text{ep}}$ qu'à travers les $y_k$, l'inégalité de traitement des données donne $I(\hat P;D_{\text{ep}})\le I(y_{1..k};D_{\text{ep}})\le\sum_j\log_2|\mathcal Y_j|$ (dérivation élémentaire). La borne couvre donc $\hat P$. La critique devient juste dès que $\hat P$ lit autre chose que les $y_k$ : j'en fais une contrainte. **Correction :** $\hat P$ est supprimée. La règle d'envoi en s4 devient un rang figé avant la boucle, sous condition de E4'. |
| 3 | « Valide par construction » (B-a2, C-a1, B-b1, C-b2, B-c1, C-c2) | **Acceptée et transformée en test** | J'ai surestimé la portée. La validité n'est héritée que sous le nul modélisé $\tilde P_0$. Sur des activations réelles, elle reste une hypothèse empirique. Formulation corrigée : « valide sous $\tilde P_0$, validité réelle mesurée ». Le test devient **E0**, placé en premier. |
| 4 | « Résultat structurel » $R\cdot\rho$ (B-a2, C-a1) | **Acceptée et transformée en test** | Ma dérivation supposait $\rho$ indépendant de $N_0$ sans le dire. Si l'on envoie les $R$ meilleurs, $\rho=\rho(N_0)$. B tient le signe pour indéterminé (il dépend de la queue et du sur-ajustement) ; C le tient pour croissant hors sur-ajustement, sous son propre statut. Le signe est donc une question empirique : **E6**. La thèse « la calibration du tri prime sur la production » redescend au rang d'HYPOTHÈSE à tester. |
| 5 | E1 est circulaire, car la métrique s1+s2 est optimisable par des $e_i\approx1$ (B-a2, C-a1, B-c2) | **Acceptée** | Le bras réel optimise l'instrument même qui le juge. Correction **E1'** : puissance mesurée sur un réservoir tenu hors du retour, générateur dégénéré comme contrôle, et crible de puissance minimale ajouté en s1. |
| 6 | Borne de capacité rattachée à tort à Dwork et al. (C-a2) | **Acceptée** | Pour des familles fraîches lues une seule fois, la borne en bits ne borne aucune erreur adaptative intra-famille. Je l'avais pressenti en III.1 (§3.3, « conséquence fine »), mais j'ai rattaché la référence à tort. Je retire le lien aux bornes de généralisation. $\sum\log_2|\mathcal Y_j|$ reste un **compteur d'audit** de ce que l'organisme peut apprendre sur le concepteur, et rien de plus. |
| 7 | Traducteur $T(p)$ non audité (C-a2, C-c1) | **Acceptée** | $T$ doit être soit mécanique, soit confié à un humain aveugle à la source, sans accès à $D_{\text{dev}}$ ni aux moniteurs. Contrôle : on fait passer par le même $T$, à l'aveugle, les sorties de l'organisme nul. |
| 8 | E5 : coupure confondue avec la capacité, nul seulement topologique, ontologie rétrospective, permutation des dates insuffisante (B-a3, C-a2, C-a3, B-c3, C-c3) | **Acceptée** | Correction **E5'** : plan intra-modèle en 2×2, graphe anonymisé, liens synthétiques, nul sémantique, graphe construit uniquement à partir de documents datés antérieurs ou égaux à $t$. |
| 9 | E5 : précision@k à taux de fausses alertes apparié dégénérée (C-b7) | **Acceptée sans réserve** | L'identité $\text{FPR}=\tfrac{k}{N_{\text{neg}}}(1-\text{Prec@}k)$ (VÉRIFIÉ chez C) rend mon critère vide. C'est une erreur de ma part. Remplacement : précision@k à $k$ égal, plus la courbe précision-rappel sur le même univers de candidats. |
| 10 | E5 : censure à droite dans la fenêtre $(t,t+\Delta]$ (B-b5) | **Acceptée comme limite déclarée** | Une fenêtre fixe pénalise les liens lents à mûrir, donc justement les idées non incrémentales. E5' mesure la prédiction de liens à maturation rapide. **Il ne mesure pas la profondeur.** Plusieurs valeurs de $\Delta$ sont rapportées. |
| 11 | E3 : longueur, perplexité, biais de position, altération sémantique, bruit de décodage, juge plat (B-a3, C-a3, C-b6, B-c4, C-c4) | **Acceptée** | Correction **E3'** : longueurs appariées, ordre symétrisé, décodage déterministe, contrôle mécanique d'équivalence, exigence conjointe de sensibilité au fond, analyse stratifiée par marge. |
| 12 | E3 substitue une autre cible à l'axe 2 (C-a3) | **Acceptée** | Je retire « expérience naturelle pour l'axe 2 ». E3' est un test d'hygiène de l'étage s2, pas une contribution à l'axe 2. |
| 13 | Zone grise entre e-valeur ≥ 20 et test d'équivalence, contraire à B4 (B-b4, C-a3, C-b5) | **Acceptée et transformée** | Correction : suite de confiance valide uniformément dans le temps, à deux frontières (Howard, Ramdas, McAuliffe & Sekhon, 2021, « Time-uniform, nonparametric, nonasymptotic confidence sequences », *Annals of Statistics*), avec des grappes par graine. La zone grise ne peut pas être supprimée, seulement bornée. Le budget maximal est fixé pour que $P(\text{zone grise})\le\gamma$ (illustratif) sous l'hypothèse de variance et d'effet du calcul de puissance. Si la zone grise survient malgré tout, **c'est cette hypothèse préenregistrée qui est falsifiée**, et la conséquence est fixée d'avance : abandon de la voie au budget donné. |
| 14 | E4 : atténuation, covariance partagée, découplage de queue, petit $K$, choix des $K$, $H_B$ qui mêle paramètre et statistique, placebos (B-b3, C-b4, C-a3, C-c5) | **Acceptée** | Correction **E4'** : porte de fiabilité, bootstrap par grappes de trajectoires, paramètre primaire de queue, $K$ tirés par une procédure figée, détecteurs placebo, hypothèses posées sur des paramètres. |
| 15 | E2 : plafond informationnel (Bretagnolle-Huber, d'après B), puissance appariée, corrélation intra-famille, calibration, budget de réglage asymétrique, croisement des concepteurs (B-b1, C-b1, C-a3, C-c6) | **Acceptée** | Correction **E2'** : pré-test de plafond par oracle, réglage des bases à budget égal, comparaison à taux de fausses alertes empirique égal sur un réservoir disjoint, tâches honnêtes croisées entre concepteurs. |
| 16 | Critère « FPR ≤ α, intervalle compris » incohérent (C-b2) | **Acceptée** | Il rejette un objet exactement calibré. Remplacé par : borne supérieure de confiance ≤ $\alpha+\varepsilon_{\text{tol}}$, avec un effectif dimensionné (E0). |
| 17 | $p_s$ mesurée sur dommages plantés mais non identifiable sur dommages réels ; faible puissance de e-BH (C-b8) | **Acceptée comme limite** | Le transfert de $p_s$ n'est pas identifiable avec les seules mesures que prévoient les faits : je le classe hors de portée. La faible puissance de e-BH est le prix de la validité sous dépendance arbitraire. Je limite donc le nombre d'hypothèses par lot. |
| 18 | Axe 3 absent (C-a3) | **Rejetée en partie** | L'axe 3 figurait au classement (C7, score 24), mais hors des cinq premiers. C a raison pour le §4.3. Ligne ajoutée : coordination plantée entre copies (détection) ; copies honnêtes appariées par entropie de tâche (fausses alertes). C'est l'appariement que C demande à B, que je reprends ici en le disant. Base à battre : corrélation brute entre copies. |

---

## (b) Expériences corrigées

### b.0 Partition des données (s'applique à toutes les expériences)

| Réservoir | Usage autorisé | Usage interdit |
|---|---|---|
| $H_{\text{cal}}$, honnête | Références, blanchiments, seuils | Mesurer un taux de fausses alertes |
| $H_{\text{test}}$, honnête, domaines de consignes distincts, flux plus longs que $m$ | Taux de fausses alertes (E0, E2', E4') | Construire quoi que ce soit |
| $D_{\text{dev}}^{\text{sel}}$ | Retour vers l'organisme (lecture souple de NC4 seulement), étage s3 | Évaluation |
| $D_{\text{dev}}^{\text{eval}}$, haché | E1', E4' | Retour, sélection |
| $D_{\text{ep}}^{(j)}$ | Lecture unique (RAPPORTÉ) | Tout le reste |
| $D_{\text{val}}$, concepteur distinct | Lecture finale unique (RAPPORTÉ) | Tout le reste |

Les activations ne sont extraites qu'**une fois** et mises en cache. Toutes les évaluations ultérieures tournent alors sur processeur, ce qui respecte la priorité au processeur (RAPPORTÉ).

---

### E0 (nouvelle, première) : audit du nul réel

- **Objets testés.** Uniquement des bases connues, sans l'organisme :
  - maximum par action corrigé de Bonferroni ;
  - CUSUM étalonné ;
  - processus-e conforme sur une référence fixe de taille $m$ ;
  - variante à nul par acte, si le programme en dispose.
- **Données.** $H_{\text{test}}$ sur deux familles de modèles ouverts d'environ 8B. Flux de longueur allant jusqu'à $c\cdot m$ ($c$ illustratif), soumis à trois régimes bénins : changement de sous-tâche, contexte long, ton rhétorique marqué. Aucune lecture d'épreuve n'est consommée.
- **Hypothèses.**
  - $H_A$ : pour chaque objet et chaque strate d'horizon ($n\le m$, $n>m$), le taux de franchissement de $1/\alpha$ sur flux honnêtes a une borne supérieure de confiance ≤ $\alpha+\varepsilon_{\text{tol}}$.
  - $H_B$ : pour au moins un régime bénin, la borne inférieure dépasse $\alpha+\varepsilon_{\text{tol}}$.
- **Dimensionnement.** Avec $\alpha=0{,}05$ et $\varepsilon_{\text{tol}}=0{,}02$ (illustratifs), une approximation normale donne environ $10^3$ flux par strate pour qu'un objet calibré passe avec une probabilité de 0,9 (illustratif, à recalculer exactement). Si le budget ne le permet pas, élargir $\varepsilon_{\text{tol}}$ est un choix **préenregistré**, jamais une correction a posteriori.
- **Contrôles négatifs.**
  1. Flux synthétiques tirés de $\tilde P_0$ : tout objet doit passer, sinon le code est faux.
  2. Flux réels à ordre temporel permuté : si un objet passe sur le permuté et échoue sur le réel, la dépendance temporelle est en cause.
  3. Reproduction, en puissance sur $D_{\text{dev}}^{\text{sel}}$, du plafonnement au-delà de $m$ (RAPPORTÉ) pour la base à référence fixe. S'il n'est pas reproduit, le banc est suspect.
- **Mesure annexe.** Fiabilité moitié-moitié des estimations de puissance. Elle alimente la porte d'E4'.
- **Ce que chaque issue réfute.**
  - $H_B$ : la classe de recherche de F2 doit être redéfinie (nul révisé) avant toute modification de l'organisme, et E2' n'est pas lancée.
  - $H_A$ : la validité est observée sur ces deux modèles et ces régimes, au statut OBSERVÉ-NON-AUDITÉ jusqu'à réplication externe.
- **Coût.** Étape E0a d'abord, sur processeur seul : contrôle 1 et dimensionnement. Puis extraction d'activations, quelques dizaines d'heures-GPU (illustratif). L'organisme n'est pas modifié, ce qui reste compatible avec la pause (RAPPORTÉ).

---

### E1' : la boucle apprend-elle du contrôle ?

- **Préalables.** Feuille de route validée, et lecture souple de NC4 retenue par l'arbitre. Sinon, E1' n'est pas lancée.
- **Bras, tous passant par le même $T$ aveugle à la source.**
  - Retour réel : verdicts sur $D_{\text{dev}}^{\text{sel}}$ dans un $\mathcal Y$ fini.
  - Retour permuté.
  - Organisme nul.
  - Générateur dégénéré : objets admissibles mais de puissance nulle.
- **Étage s1.** Il inclut un crible de puissance minimale contre des alternatives locales synthétiques.
- **Métrique.** Puissance, à taux de fausses alertes empirique égal, des $r$ meilleurs objets de chaque bras ($r$ figé), sur $D_{\text{dev}}^{\text{eval}}$ en cache.
- **Hypothèses.**
  - $H_A$ : le bras réel dépasse le bras permuté.
  - $H_B$ : l'écart entre réel et permuté reste inférieur à $\delta$ (illustratif).
- **Décision.** Suite de confiance à deux frontières, avec grappes par graine (critique 13).
- **Contrôles.** Le générateur dégénéré doit perdre face au bras réel. Canaris dans $D_{\text{dev}}^{\text{eval}}$.
- **Ce que chaque issue réfute.**
  - Équivalence : la voie retour est abandonnée.
  - Réel supérieur : $H_B$ est réfutée.
  - Zone grise au budget maximal : l'hypothèse de variance est réfutée et la voie est abandonnée.
- **Coût.** Quelques jours-processeur après le cache (illustratif).

---

### E2' : des objets séquentiels nouveaux battent-ils les bases ?

- **Préalables.**
  1. E0 conclut à $H_A$.
  2. Pré-test de plafond, qui reprend la condition de B-b1. Sur les familles synthétiques à générateur connu, la puissance de l'oracle (test du rapport de vraisemblance) doit dépasser celle de la meilleure base d'au moins $\delta$. Sinon, E2' est déclarée non jugeable et n'est pas lancée.
- **Bases.** Réglées à budget processeur égal sur le même générateur, nul par acte compris.
- **Objectif de recherche.** La croissance logarithmique sous les alternatives, ce qui écarte les objets dont la croissance est nulle ou négative.
- **Hypothèses.**
  - $H_A$ : $\Delta\beta\ge\delta$, d'abord sur les familles synthétiques tenues à l'écart (second concepteur), puis sur $D_{\text{dev}}^{\text{eval}}$ à taux de fausses alertes empirique égal, avec un seuil fixé sur $H_{\text{cal}}$ et une évaluation sur $H_{\text{test}}$.
  - $H_B$ : $\Delta\beta<\delta$ sur les familles tenues à l'écart.
- **Validité exigée.** Le critère d'E0 au seuil nominal, y compris pour les flux plus longs que $m$, sous les régimes bénins et sur des tâches honnêtes croisées entre concepteurs.
- **Analyse.** Appariée, par paires discordantes, avec bootstrap par grappes de tâches.
- **Contrôles.** Étiquettes permutées, qui ne doivent donner aucun gain ; la base à référence fixe doit plafonner.
- **Ce que chaque issue réfute.**
  - Pas de gain sur les familles tenues à l'écart : $H_A$ est réfutée.
  - Gain répliqué sur les deux concepteurs : $H_B$ est réfutée.
- **Suite.** Le seul gagnant consomme une lecture de $D_{\text{ep}}$.
- **Coût.** Jours-processeur, plus 10 à 30 heures-GPU pour l'épreuve (illustratif).

---

### E3' : hygiène du juge interne

- **Hypothèses.**
  - $H_A$ : le juge interne de l'organisme est à la fois invariant au style et sensible au fond.
  - $H_B$ : l'une des deux propriétés au moins fait défaut.
- **Paires de style.** Contenu identique, vérifié mécaniquement par l'extraction des mêmes conditions et formules ; longueurs appariées à une tolérance près (illustratif).
- **Paires de corruption.** Style identique, une condition technique inversée.
- **Conduite du test.** Ordre (A,B)/(B,A) symétrisé, décodage déterministe, bruit de rééchantillonnage mesuré à part.
- **Métrique.** Excès d'inversion stylistique, stratifié par marge, et taux de détection des corruptions.
- **Seuils.** Équivalence sous $\delta_s$ et détection ≥ $s_{\min}$ (illustratifs).
- **Ce que chaque issue réfute.** Si l'une des deux conditions échoue, $H_A$ est réfutée et le juge est retiré de s2. Si les deux tiennent, $H_B$ est réfutée.
- **Portée.** L'étage s2 seulement.
- **Coût.** Quelques heures-GPU (illustratif).

---

### E4' : le substitut prédit-il le réel là où l'on sélectionne ?

- **Candidats.** $K$ détecteurs tirés par une règle figée (strates de score s2), plus des placebos : directions aléatoires, sonde de longueur, norme d'activation.
- **Porte de fiabilité.** La fiabilité moitié-moitié des puissances sur 8B, mesurée sur $D_{\text{dev}}^{\text{eval}}$, doit atteindre $r_{\min}$ (illustratif). Sinon, aucun $\tau$ n'est interprété.
- **Paramètre primaire.** $\Delta_{\text{top}}=P(\text{bat la base sur 8B}\mid\text{top }q\text{ du substitut})-P(\text{bat la base sur 8B})$. C'est une différence, pas un ratio, et elle porte sur la queue sélectionnée.
  - $H_A$ : $\Delta_{\text{top}}>0$.
  - $H_B$ : $\Delta_{\text{top}}\le0$.
- **Paramètre secondaire.** Le $\tau$ de Kendall, avec un intervalle par bootstrap en grappes de trajectoires.
- **Contrôles.** Les placebos ne doivent pas apparaître dans le haut du classement plus souvent que le hasard. Un substitut à caractéristiques permutées doit donner $\Delta_{\text{top}}\approx0$.
- **Ce que chaque issue réfute.**
  - $H_B$ : s2 est supprimé comme filtre, **même si le $\tau$ global est positif** (découplage de queue), et l'envoi en s4 se fait au hasard parmi les survivants de s3.
  - $H_A$ : l'envoi en s4 se fait au rang s2 figé, et $H_B$ est réfutée sur ces deux modèles.
- **Coût.** Processeur, après le cache d'E0.

---

### E5' : prédiction ou mémoire ?

- **Graphe.** Construit uniquement à partir de documents datés antérieurs ou égaux à $t$.
- **Plan intra-modèle.** Un seul modèle $M$, de coupure $c_M$, ce qui fixe la capacité.
  - Deux fenêtres : $W_{\text{avant}}\subset(t,c_M]$ et $W_{\text{après}}\subset(c_M,c_M+\Delta]$.
  - Deux étiquetages : concepts nommés, ou anonymisés par hachage bijectif.
- **Hypothèses.**
  - $H_A$ (prédiction) : un avantage sur les nuls topologique et sémantique en $W_{\text{après}}$, à $k$ égal.
  - $H_B$ (mémoire) : un avantage en $W_{\text{avant}}$ seulement.
- **Comparaison.** Les deux fenêtres n'ont pas la même difficulté. On compare donc les avantages **relatifs aux nuls de chaque fenêtre**.
- **Contrôles.** Liens synthétiques plantés, absents de tout corpus. Dates permutées sur le graphe anonymisé.
- **Limites.**
  - $c_M$ est une déclaration du fournisseur, que je ne peux pas vérifier.
  - La censure (critique 10) s'applique toujours.
- **Coût.** Processeur, avec un petit modèle (illustratif).

---

### E6 (nouvelle) : la génération brute ajoute-t-elle quelque chose ?

- **Cadre.** Mondes à lois plantées. Les verdicts de l'orchestrateur ne sont pas soumis à la lecture unique.
- **Plan.** $R$ fixé (illustratif). On fait varier $N_0$ par sous-échantillonnage d'un vivier déjà généré, avec un tri identique. Les sorties existantes suffisent, sans modifier l'organisme.
- **Hypothèses.**
  - $H_A$ : $\rho(N_0)$ croît, avec une pente dont l'intervalle exclut 0.
  - $H_B$ : $\rho$ est plat ou décroissant.
- **Contrôles.** Un tri aléatoire doit donner $\rho$ plat ; un tri par l'oracle, $\rho$ croissant.
- **Ce que chaque issue réfute.**
  - $H_B$ : ma thèse « le tri prime sur la production » tient, mais **sur le synthétique seulement**.
  - $H_A$ : cette thèse est réfutée.
- **Coût.** Quelques jours-processeur (illustratif).

---

### Classement révisé et ordre d'exécution

Les notes sont mon jugement (HYPOTHÈSE). Pour les quatre premiers critères, 5 est le plus favorable ; pour le coût, 1 correspond au processeur seul.

| Exp. | G | F | P | Pot. | Coût | Score |
|---|---|---|---|---|---|---|
| E6 | 3 | 5 | 3 | 2 | 1 | 90 |
| E4' | 5 | 3 | 5 | 3 | 3 | 75 |
| E0 | 5 | 4 | 5 | 2 | 3 | 66,7 |
| E2' | 4 | 3 | 4 | 4 | 3 | 64 |
| E1' | 4 | 3 | 4 | 2 | 2 | 48 |
| E5' | 3 | 3 | 3 | 2 | 2 | 27 |
| E3' | 3 | 4 | 2 | 2 | 2 | 24 |

**Sensibilité.**
- Avec le potentiel au carré, E2' (256) passe devant E4' (225), E6 (180) et E0 (133).
- Avec le coût au carré, E6 reste en tête.

**Défaut de la formule.** Elle ignore les **dépendances**. E4' et E2' exigent le cache et le verdict d'E0. L'ordre d'exécution s'écarte donc du score : E0a et E6 en parallèle, sur processeur, puis E0, puis E4', puis E2', puis E1' si l'arbitre l'autorise. E5' et E3' sont indépendantes.

---

## (c) Réponse à la question de l'arbitre, en une page

**Ce qui est établi.**
- **Les contraintes (RAPPORTÉ).**
  - Séparation de la sélection et de l'évaluation.
  - Lecture unique des familles d'épreuve et de la banque finale.
  - Plafonnement de l'accumulation au-delà de la taille $m$ de la référence honnête, sauf nul par acte.
  - Plancher d'audit à mesurer par strate sur dommages plantés.
  - Organisme en pause dans l'attente d'une feuille de route.
- **Trois énoncés mathématiques, chacun conditionnel à ses hypothèses.**
  - L'inégalité de Ville, **sous le nul modélisé seulement**.
  - L'information qu'un canal de retour à issues finies transmet est bornée par son nombre de bits (traitement des données).
  - La précision@k à taux de fausses alertes apparié est dégénérée (identité relevée par C, que j'accepte).
- **Sur l'organisme, rien n'est établi :** les faits ne rapportent aucun résultat de performance.

**Ce que les critiques m'ont fait retirer.**
- « Garantie héritée par construction » devient « validité sous $\tilde P_0$, à mesurer » (E0).
- « Résultat structurel $R\rho$ » devient une HYPOTHÈSE (E6).
- E1 jugée sur s1+s2 était circulaire.
- La précision@k appariée était vide.
- « Expérience naturelle pour l'axe 2 » est retirée.
- Le lien entre la borne en bits et les bornes de généralisation est retiré.

**Ce qui n'est pas établi** (HYPOTHÈSES, chacune avec son test) :
- la validité réelle des processus-e sur activations de modèles d'environ 8B (E0) ;
- la valeur du volume de génération face à celle du tri (E6) ;
- le transfert du substitut au réel **dans la queue sélectionnée** (E4') ;
- l'apport d'objets séquentiels nouveaux (E2') ;
- l'apprentissage de la boucle à partir du contrôle (E1') ;
- la prédiction face à la mémoire (E5'), **sans portée sur la profondeur** à cause de la censure ;
- la profondeur elle-même : je ne sais pas la mesurer sans panel humain ;
- le transfert de $p_s$ des dommages plantés aux dommages réels : hors de portée avec les données prévues ;
- la lecture de la règle de séparation (NC4) : c'est une décision de l'arbitre, pas un résultat. Sous la lecture stricte, E1' disparaît et seule la voie aller subsiste.

**Expérience à faire en premier : E0, l'audit du nul réel**, précédée de son étape sur processeur seul (E0a) et menée en parallèle avec E6.

Quatre raisons :
1. Elle est sur le chemin critique : si les constructions séquentielles connues dépassent $\alpha+\varepsilon_{\text{tol}}$ sur des flux honnêtes réels non stationnaires, toute recherche de type F2 vise une classe mal définie, et E2' comme E4' perdent leur objet.
2. Elle ne consomme aucune lecture unique.
3. Elle ne modifie pas l'organisme, ce qui respecte la pause (RAPPORTÉ).
4. Elle produit le cache d'activations qui ramène E1', E2' et E4' sur processeur.

**Issues d'E0, qui falsifient chacune quelque chose :**
- dépassement significatif sous un régime bénin : réfute l'hypothèse que le nul modélisé suffit, et impose de réviser la classe de recherche avant de toucher à l'organisme ;
- respect de la borne : réfute $H_B$ sur deux modèles et trois régimes, au statut OBSERVÉ-NON-AUDITÉ jusqu'à réplication par une équipe extérieure ;
- non-reproduction du plafonnement au-delà de $m$ : disqualifie le banc lui-même.

FIN-DE-CELLULE