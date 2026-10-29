# Proposition C — Conception de la recombinaison bisociative à deux espaces (Tour III.1)

**Intégrité des pièces reçues (Règle 2) :** Les pièces A et B sont complètes et **VÉRIFIÉES** quant à leur empreinte. La pièce C est un extrait restreint au préambule (lignes 22 à 31) et la pièce D est un extrait restreint aux points 5 et 6 (lignes 29 à 33), sans les mentions de « mémoire qui refuse les redites » et « héritage récompensé » annoncées par la question (**VÉRIFIÉ** par l'en-tête des faits). Aucun contenu absent n'est inventé.

---

## (a) Ce que la question suppose sans que ce soit établi

Chaque présupposé implicite de la question ou des pièces est isolé ci-dessous avec son statut épistémique strict.

1. **Séparabilité empirique du domaine et du concept mathématique dans les fiches.** La question suppose qu'il existe deux espaces de représentation ($D$ pour le domaine applicatif, $C$ pour la structure mathématique sous-jacente) mutuellement quasi-orthogonaux ou décorrélés. Statut : **HYPOTHÈSE** (et marqué SUPPOSÉ). Dans les textes réels, le vocabulaire mathématique est fortement inféodé à la communauté de domaine (homonymies, notations propres).
2. **Défaillance structurelle des noyaux de sommets pour l'appariement de paires.** La question propose encore en exemple un noyau composé sur les fiches ($S = S_{\text{domaine}} \odot \text{ou} \oplus S_{\text{concept}}$) dont on tirerait un sous-ensemble par déterminant. Or, maximiser le volume d'un sous-ensemble de $k$ fiches (processus ponctuel déterminantal sur les *sommets*) sélectionne des fiches mutuellement distantes, ce qui laisse $\binom{k}{2}$ paires où les paires de domaines proches dominent les paires valides par simple densité de partage d'opérateurs de fond. Statut : **VÉRIFIÉ** dans le code (Pièce A, lignes 182-194) et **RAPPORTÉ** dans l'audit du mécanisme (Pièce B, § 3 : part de paires proches $0,452$ avec $q \equiv 1$ et $0,449$ avec $q$, identique au tirage uniforme $0,449$ ; l'essai `a_2dpp` déterminantal exact à 2 éléments perd aussi à $-5,1$ et $-1,9$ points contre le stratifié).
3. **Inversion de signe des noyaux composés sur les sommets.** Si l'on place le rapport « proximité conceptuelle / proximité de domaine » dans les termes hors-diagonale $L_{ij}$ d'une matrice de sommets et qu'on maximise $\det(L_Y)$, le déterminant $2 \times 2$ vaut $L_{ii}L_{jj} - L_{ij}^2$ : maximiser le déterminant *minimise* $L_{ij}^2$ et donc *repousse* les fiches qui partagent un concept. C'est exactement l'effet qui a fait échouer la forme du rapport de Gemini une fois régularisée. Statut : **RAPPORTÉ** (Pièce B, § 4, bras (e) : précision $0,147$ contre $0,151$ pour l'uniforme, écart $-5,7$ contre le stratifié, « une fois réparée, elle repousse les paires qu'elle visait »).
4. **Fécondité supérieure des paires bisociatives lors de la fusion par un modèle de langage.** La question suppose qu'envoyer à l'agent de fusion une paire (loin en domaine, proche en concept) augmente la probabilité que la fiche fille passe les portes du juge (notamment K1-K5 en Pièce C et la validation `ce_que_la_fille_predit_de_plus` en Pièce A). Statut : **HYPOTHÈSE** (explicitement réservé en Pièce B, § 6 : « Il ne dit rien de la qualité des hypothèses fusionnées par un modèle »).
5. **Indépendance entre l'aptitude $q_i$ des parents et la présence d'un pont.** Dans les mondes synthétiques de la Pièce B, la qualité $q$ est indépendante de la vérité et varie d'un facteur $9$ en $q^2$, écrasant la répulsion de domaine (corrélation de rang $0,977$ entre l'ordre glouton et $q$). Statut : **RAPPORTÉ** (Pièce B, § 3). Que $q$ soit corrélé ou non aux vrais ponts dans les vraies courses reste une **HYPOTHÈSE**.

---

## (b) Conception ciblée (Points 1 à 4) et duels d'inférence forte

Conformément au format demandé par la question, chaque point présente les options, leurs avantages/inconvénients, une recommandation avec niveau de confiance (marqué illustratif / SUPPOSÉ), puis les expériences décisives formulées en duels $H_A$ contre $H_B$ (Règle B4).

### Point 1 — L'objectif mathématique à deux espaces

#### Question préalable : « Minimiser le produit scalaire des domaines » est-il contenu dans « maximiser le volume » ?
* **Réponse analytique (**VÉRIFIÉ** mathématiquement) :** Pour une paire de vecteurs unitaires $(d_i, d_j)$ dans l'espace des domaines, le volume au carré du parallélépipède (déterminant de Gram) est $\det G_{\{i,j\}} = 1 - \langle d_i, d_j \rangle^2 = \sin^2 \theta_{ij}$ (ou $1 - \langle d_i, d_j \rangle^4$ avec le noyau de Schur $S_{ij} = \langle d_i, d_j \rangle^2$ de la Pièce A). Maximiser ce volume sur une paire isolée équivaut donc strictement à minimiser $|\langle d_i, d_j \rangle|$.
* **Pourquoi cela échoue pourtant dans la Pièce A (**RAPPORTÉ** en Pièce B, § 3) :**
  1. **Échelle et applatissement :** Autour de $\langle d_i, d_j \rangle = 0,28$ (domaines proches en Pièce B), la pénalité en $\cos^4$ dans $(1+\gamma)^2 - \cos^4$ n'est que de $0,6\%$ face à $q_i^2 q_j^2$ qui varie d'un facteur $9$. La dérivée de $1 - x^4$ en $x \to 0$ est nulle : le déterminant punit la colinéarité stricte ($x \to 1$), mais est aveugle aux proximités modérées.
  2. **Sélection de sommets vs sélection d'arêtes :** Tirer $k > 2$ sommets par volume maximal garantit qu'aucun domaine n'est dupliqué, mais lors de la formation des paires parmi ces $k$ sommets, le filtre d'opérateur commun ne retient que les paires connectées — qui sont majoritairement les paires de domaines proches. **Il faut donc un terme d'affinité de paire explicite ou changer l'objet du noyau (passer des sommets aux paires).**

#### Options pour l'objectif à deux espaces

* **Option 1a — Noyau composé sur les sommets (fiches) :** $L_{ij} = q_i q_j S^{\text{dom}}_{ij} (1 - S^{\text{conc}}_{ij}) + \gamma \delta_{ij}$.
  * *Avantage :* Conserve l'architecture exacte de `recombinaison.py` (Pièce A, dimension $N \times N$).
  * *Inconvénient :* Non garanti semi-défini positif sans un $\gamma$ massif (Pièce B, § 4, bras (e) : $\gamma$ médian $0,94$), et souffre du paradoxe des sommets : tirer $k$ fiches mutuellement proches en concept et éloignées en domaine est un problème de clique/anti-clique combinatoire que le déterminant sur sommets ne résout pas.
* **Option 1b — Score bilinéaire de Swanson-Volume avec couverture stratifiée (sans DPP) :** On évalue directement chaque paire valide $e = (i,j)$ par un poids d'utilité bisociative :
  $$w_{ij} = (q_i q_j)^\beta \cdot \underbrace{\left(1 - \langle d_i, d_j \rangle^2\right)^{\alpha_D}}_{\text{Volume de domaine } V_D(i,j)} \cdot \underbrace{\sum_{c \in C_i \cap C_j} \text{idf}(c)^2}_{\text{Affinité de Swanson } A_C(i,j)}$$
  avec sélection gloutonne sous contrainte de strates de domaines disjointes.
  * *Avantage :* Coût $\mathcal{O}(N^2)$, aucune inversion matricielle, combine directement `b_eloigne` ($+11,9$ points en Pièce B) et `d1_inv` ($+5,3$ points en Pièce B).
  * *Inconvénient :* Ne gère pas nativement la redondance conceptuelle entre les $m$ paires tirées (peut tirer $m$ fois le même pont conceptuel rare entre des strates différentes).
* **Option 1c — Processus déterminantal sur l'espace des PAIRES (Edge-DPP à deux espaces) :**
  L'objet élémentaire n'est plus la fiche $i \in \{1,\dots,N\}$, mais la **paire candidate valide** $e = (i,j) \in \mathcal{E}$ ($M = |\mathcal{E}| \le \binom{N}{2}$). On définit un noyau $K \in \mathbb{R}^{M \times M}$ indexé par les paires $e = (i,j)$ et $e' = (k,l)$ :
  1. **Qualité bisociative de la paire $e=(i,j)$ (diagonale / norme) :**
     $$Q_e = (q_i q_j)^\beta \cdot \sqrt{1 - \langle d_i, d_j \rangle^2} \cdot \langle c_i, c_j \rangle_{\text{IDF}}$$
     où $\sqrt{1 - \langle d_i, d_j \rangle^2}$ est **exactement le volume du parallélépipède 2D** engendré par les vecteurs unitaires de domaine $(d_i, d_j)$, et $\langle c_i, c_j \rangle_{\text{IDF}} = \frac{\sum_{u \in C_i \cap C_j} \text{idf}(u)^2}{\|c_i\|_{\text{IDF}} \|c_j\|_{\text{IDF}}}$ est la proximité conceptuelle pondérée par la rareté (Swanson).
  2. **Similarité entre deux paires $e=(i,j)$ et $e'=(k,l)$ (répulsion inter-paires pour diversifier le lot de $m$ fusions) :**
     Soit $\Phi(e) = \frac{d_i \otimes d_j + d_j \otimes d_i}{\|d_i \otimes d_j + d_j \otimes d_i\|} \oplus \frac{c_i \odot c_j}{\|c_i \odot c_j\|}$ le plongement symétrisé du couple de domaines et du pont conceptuel actif. La matrice de Gram entre paires est $S^{\text{paire}}_{e,e'} = \langle \Phi(e), \Phi(e') \rangle^2$.
  3. **Noyau complet sur les paires :**
     $$K_{e,e'} = Q_e \, S^{\text{paire}}_{e,e'} \, Q_{e'} + \gamma \delta_{e,e'}$$
     On tire $m = \text{max\_paires}$ paires par sélection gloutonne de $\log \det(K_Y)$ avec la fonction `cholesky` et `tirage_glouton` déjà présentes dans la Pièce A (lignes 91-137).
  * *Propriétés mathématiques (**VÉRIFIÉ**) :* $S^{\text{paire}}$ est le produit de Schur d'une matrice de Gram par elle-même, donc semi-définie positive (théorème de Schur) ; $K = \text{diag}(Q) S^{\text{paire}} \text{diag}(Q) + \gamma I$ est strictement définie positive pour tout $\gamma > 0$. Le déterminant est bien défini. Coût : pour $N = 40$ survivantes (Pièce B), $M \le 780$ paires (et après filtre de pont, typiquement $M < 150$), le glouton de Cholesky de taille $m = 4$ prend $\mathcal{O}(m^3 M)$ opérations, soit $< 5\,\text{ms}$ en pur Python (illustratif / SUPPOSÉ).
  * *Ce qu'il maximise exactement :* Un compromis entre la valeur bisociative intrinsèque de chaque paire tirée ($\prod_{e \in Y} Q_e^2$, qui force simultanément un grand volume entre les deux domaines de la paire et une forte proximité conceptuelle IDF) et la diversité mutuelle des $m$ paires envoyées en fusion ($\det S^{\text{paire}}_Y$, qui interdit de tirer deux fois la même strate de domaines ou deux fois le même opérateur-pont moyeu).

* **Recommandation :** **Option 1c (Edge-DPP à deux espaces)** comme forme principale, et **Option 1b** comme ablation directe sans répulsion inter-paires. Confiance : $0,85$ (illustratif / SUPPOSÉ), car elle corrige l'erreur de type (sommets vs arêtes) démontrée à la section 3 de la Pièce B tout en réutilisant $100\%$ de l'algèbre linéaire vérifiée de la Pièce A.

---

### Point 2 — La représentation des concepts mathématiques

Comment extraire le vecteur conceptuel $c_i$ sans juge-modèle dans la boucle de tirage, sans manipulation par le proposeur, et en garantissant qu'il code le concept et non le domaine ?

#### Options de représentation

* **Option 2a — Champ déclaratif en liste fermée dans le gabarit de fiche (Pièce C) :** Le proposeur choisit au plus $r = 3$ (illustratif / SUPPOSÉ) étiquettes dans une taxonomie scellée $\mathcal{T}_{\text{conc}}$ de structures mathématiques (ex. : *inégalité de concentration martingale, processus ponctuel déterminantal, test de rapport de vraisemblance séquentiel, invariance par groupe, borne de Fano/information mutuelle, décomposition spectrale*).
  * *Avantage :* Coût nul au tirage, alignement exact entre fiches.
  * *Inconvénient :* Risque d'écoconception/manipulation (le proposeur déclare des concepts rares factices pour maximiser son $Q_e$).
* **Option 2b — Extraction déterministe par programme (AST mathématique et motifs structurels) :** Analyse lexicale et syntaxique hors-modèle du texte de la fiche (formules LaTeX, opérateurs, théorèmes nommés, citations d'antériorités du champ `antériorités` de la Pièce C) projetée par dictionnaire de synonymes vers $\mathcal{T}_{\text{conc}}$, après **caviardage** des substantifs de domaine.
  * *Avantage :* Non manipulable par simple déclaration gratuite si le corps de la méthode ne contient pas les opérateurs ; déterministe ; coût processeur négligeable.
  * *Inconvénient :* Couverture imparfaite (rappel limité face aux paraphrases littéraires, analogue au monde « moyen » ou « mal observé » de la Pièce B où la couverture tombe à $0,70$ ou $0,45$).
* **Option 2c — Hybride « Déclaration ancrée vérifiée mécaniquement » (Recommandée) :** Le gabarit (Pièce C) ajoute un champ obligatoire `concepts_mathematiques` (1 à 3 clés de la liste fermée $\mathcal{T}_{\text{conc}}$), mais une clé déclarée $u \in \mathcal{T}_{\text{conc}}$ n'est activée dans le vecteur $c_i$ que si un **vérificateur mécanique par expressions régulières** trouve dans les champs `hypothèse`, `méthode` ou `antériorités` au moins deux marqueurs formels associés à $u$ dans le lexique scellé (équations, symboles d'opérateurs, noms de lemmes).

#### Garde-fous contre la manipulation par les proposeurs (Anti-gaming)
1. **Ancrage lexical obligatoire (Preuve de travail syntaxique) :** Comme décrit en 2c, toute étiquette conceptuelle déclarée mais non soutenue par ses marqueurs formels dans le corps de la fiche est mise à zéro avant le tirage (et peut invalider la porte K1 du juge en Pièce C si le champ est frauduleux).
2. **Normalisation $\ell_2$ et plafond de cardinalité :** Le vecteur $c_i$ est normalisé ($\|c_i\|_2 = 1$, comme `vecteurs_domaine` en Pièce A, ligne 69 : `1.0 / math.sqrt(len(etiquettes))`). Ajouter des étiquettes dilue le poids de chacune en $1/\sqrt{|C_i|}$ ; un plafond strict $|C_i| \le 3$ (illustratif / SUPPOSÉ) empêche l'arrosage (« keyword stuffing »).
3. **Pénalité d'IDF endogène au vivier :** Si tous les proposeurs tentent de déclarer le même concept « à la mode » pour être tirés, sa fréquence documentaire dans le vivier des survivantes augmente, son $\text{idf}(u) = \log\frac{N + 1}{\text{df}(u) + 1}$ chute automatiquement, et ce concept devient un « moyeu » ignoré par la pondération de Swanson.

#### Test de séparabilité Domaine / Concept (Information Mutuelle Ajustée et Permutations)
Pour vérifier mécaniquement que la représentation $C$ capte la structure mathématique et non le domaine $D$ :
* **Mesure :** Sur un corpus d'étalonnage où chaque fiche possède une étiquette de domaine $d_i$ et une étiquette de concept $c_i$, on calcule :
  1. L'Information Mutuelle Ajustée $\text{AMI}(D, C)$ entre le partitionnement par domaines et le partitionnement par concepts.
  2. La corrélation de Mantel $r_M(S^{\text{dom}}, S^{\text{conc}})$ entre la matrice de similarité de domaine et la matrice de similarité de concept sur toutes les paires $\binom{N}{2}$.
  3. Le score de silhouette croisé : cohésion intra-concept des fiches de *domaines différents* comparée à la cohésion intra-domaine des fiches de *concepts différents*.
* **Critère de réussite :** $r_M(S^{\text{dom}}, S^{\text{conc}}) < 0,10$ (illustratif / SUPPOSÉ) et rappel à $k=5$ plus proches voisins dans l'espace $C$ pour retrouver une fiche de même opérateur mais d'un *autre* domaine supérieur à $0,60$ (illustratif / SUPPOSÉ).

* **Recommandation :** **Option 2c (Déclaration en liste fermée + validation mécanique d'ancrage)** couplée à un vecteur de domaine $d_i$ calculé par fréquences des termes de domaine après soustraction du lexique mathématique $\mathcal{T}_{\text{conc}}$. Confiance : $0,80$ (illustratif / SUPPOSÉ).

---

### Point 3 — Le test (Préenregistrement sur mondes étendus et passage à la Course 2)

#### 3.1. Extension des mondes synthétiques de la Pièce B à deux espaces
Les mondes de la Pièce B (`monde_v1.py`, § 5 : 8 domaines $\times$ 5 articles, 2 à 4 champs, 3 greffes et 3 jumeaux, moyeu à $25\%$) sont étendus pour distinguer **ponts de surface** et **ponts conceptuels profonds** :
* **Espace 1 (Domaine $D$) :** Inchangé (cosinus exacts validés à $0,54 / 0,28 / 0,03$ pour même domaine / même champ / champs différents, Pièce B § 2.3 et § 5).
* **Espace 2 (Concept mathématique $C$ vs Opérateur de surface $O$) :** On sépare les étiquettes partagées en trois régimes :
  1. *Vrais ponts bisociatifs (vérité terrain positive) :* Fiches de **champs différents** ($\cos_D \approx 0,03$), partageant un **concept mathématique profond** non-moyeu (greffe ou jumeau structurel), avec contraintes compatibles ($9,5$ paires valides en moyenne en monde « bien », Pièce B § 5).
  2. *Ponts de surface / faux ponts inter-champs (piège nouveau) :* Fiches de champs différents partageant un **terme méthodologique générique ou homonyme de surface** (ex. « seuil », « moyenne », « régression ») sans partager de structure mathématique profonde.
  3. *Partages intra-champ (piège de proximité) :* Fiches de domaines proches (même champ, $\cos_D \approx 0,28$) partageant à la fois des concepts mathématiques et des opérateurs de fond (haute densité de paires valides, mais non bisociatives car dans le même champ).

#### 3.2. Protocole préenregistré (gelé avant exécution)
* **Hypothèse :** Le tirage par noyau déterminantal sur les paires à deux espaces (**bras (f) Edge-DPP 2-espaces**) bat le tirage stratifié (**bras (b)**), la forme corrigée v6.3 (**bras (a)**) et la marche de Swanson seule (**bras (d1)**) sur la précision des vrais ponts bisociatifs, parce qu'il élimine simultanément les partages intra-champ (grâce au facteur de volume $\sqrt{1-\langle d_i,d_j\rangle^2}$) et les moyeux/faux ponts (grâce au facteur conceptuel IDF $\langle c_i,c_j\rangle_{\text{IDF}}$ et à la répulsion inter-paires).
* **Métrique principale :** Précision sur les 12 paires tirées par monde ($k=4$ paires $\times 3$ générations, budget identique à la Pièce B § 1), moyenne sur $N_{\text{mondes}} = 400$ mondes par condition, intervalle de confiance à $95\%$ par $2\,000$ rééchantillonnages bootstrap appariés par monde (même graine `20261026` qu'en Pièce B § 5).
* **Comparateurs obligatoires (témoins) :**
  * **(b)** Tirage stratifié avec étage commun (référence : précision $0,203$ en « bien » et $0,127$ en « moyen » dans les mondes v1, Pièce B § 1).
  * **(a)** Forme corrigée v6.3 ($0,155$ et $0,105$ en Pièce B § 1).
  * **(d1)** Marche de Swanson par étiquette rare ($0,239$ et $0,165$ en Pièce B § 1).
  * **(b_eloigne)** Diagnostic d'éloignement seul ($0,322$ et $0,193$ en Pièce B § 1), utilisé comme témoin de la part « éloignement pur ».
* **Prédiction chiffrée, signe et seuil d'adoption :**
  * Comme souligné à la section 7.3 de la Pièce B (« À des précisions de 10 à 20 %, +12 points signifie $\times 1,6$ à $\times 2,2$ : même l'a priori d'éloignement idéalisé ne l'atteint pas dans les deux mondes »), nous fixons une règle d'adoption à double détente (SUPPOSÉ / illustratif) :
    1. **Sur le stratifié (b) :** Gain apparié $\Delta(\text{f}, \text{b}) \ge +12,0\text{ points}$ en monde « bien observé » **ET** $\Delta(\text{f}, \text{b}) \ge +6,0\text{ points}$ en monde « moyennement observé » (borne inférieure de l'IC à $95\%$ strictement supérieure à $+9,0$ et $+4,0$ points respectivement).
    2. **Sur Swanson seul (d1) et l'éloignement seul (b_eloigne) [Test d'ingrédient manquant] :** Pour conclure que *« la combinaison des deux espaces dans l'objectif est l'ingrédient manquant »*, (f) doit battre **à la fois** (d1) d'au moins $+5,0\text{ points}$ (borne inf IC $95\% > +2,5$) **et** (b_eloigne) d'au moins $+3,0\text{ points}$ (borne inf IC $95\% > +1,0$) dans les mondes « bien » et « moyen ». Si (f) bat (b) et (d1) mais ne bat pas (b_eloigne), alors seul l'éloignement des domaines compte (la proximité conceptuelle dans l'objectif est superflue au-delà du filtre binaire). Si (f) ne bat pas (d1), l'éloignement de domaine dans l'objectif est superflu.
* **Puissance statistique :** Avec $400$ mondes appariés, l'écart-type de la différence appariée observé en Pièce B (§ 1, demi-largeur d'IC à $95\%$ d'environ $1,1$ à $1,5$ point, soit $\text{SE} \approx 0,6$ point) donne une puissance $> 0,99$ au seuil $\alpha = 0,05$ pour détecter un effet vrai de $+3,0\text{ points}$ (**VÉRIFIÉ** à partir des largeurs d'intervalles de la Pièce B).
* **Contrôles négatifs corrigés (intégrant les critiques de la Pièce B § 7) :**
  1. *Monde sans pont :* Écart au placebo $|\Delta| < 1,5\text{ point}$ (IC contenant $0$).
  2. *Monde à vérité inversée (les vrais ponts relient des domaines proches du même champ) :* Au lieu de demander seulement $\Delta_{\text{inversé}}(\text{f}, \text{b}) < 0$ (biaisé en Pièce B § 2.2), on exige une **chute franche de l'écart par rapport à l'uniforme (c)** : $\Delta_{\text{inversé}}(\text{f}, \text{c}) - \Delta_{\text{normal}}(\text{f}, \text{c}) \le -10,0\text{ points}$ (illustratif / SUPPOSÉ).
* **Liste d'arrêt (Critères de mort immédiate) :**
  1. Le noyau $K$ sur les paires lève `NonDefiniePositive` sur $\ge 1\%$ des mondes avec $\gamma = 10^{-3}$.
  2. $\Delta(\text{f}, \text{b}) < +6,0\text{ points}$ en monde « bien » ou $< +3,0\text{ points}$ en monde « moyen ».
  3. En condition « moyeux dominants » (deux moyeux à $0,6$, Pièce B § 2.3), (f) perd plus de $2,0\text{ points}$ contre (d1).

#### 3.3. Passage sur les vraies fiches de la Course 2 sans sélection sur le verdict (Garde N-053)
Sur les vraies fiches de la Course 2 (Pièce C), la « vérité terrain » d'un pont n'est pas annotée d'avance, et **lire la qualité des filles après le juge pour choisir la méthode de tirage violerait N-053 (sélection sur le verdict)**. Protocole en trois étages étanches :
1. **Étage hors-boucle sur paires candidates (Zéro appel LLM, zéro lecture du juge) :** Sur le vivier figé des fiches survivantes du tour 1 de la Course 2, on fait tourner (b), (d1) et (f) à graine scellée. On mesure uniquement des propriétés géométriques **avant fusion** : taux de collision sur des opérateurs-moyeux (fréquence $> 25\%$ du vivier), distance inter-domaines moyenne $1 - \langle d_i, d_j \rangle^2$ des paires tirées, et entropie des strates couvertes. Le choix de l'extracteur et la vérification d'absence de dégénérescence se font ici, **sans générer aucune fiche fille**.
2. **Épreuve d'appariement aveugle à budget symétrique (Plan en blocs randomisés) :** Dans une course d'évaluation dédiée, à chaque génération, on tire $m=3$ paires par le bras (b) (témoin stratifié) et $m=3$ paires par le bras (f) (en dédupliquant : si une paire est tirée par les deux, elle n'est fusionnée qu'une fois par le même appel `consigne_fusion` de la Pièce A, ligne 146, et créditée aux deux bras). Toutes les filles sont anonymisées (`identifiant` neutre, ordre mélangé) avant de passer devant le juge figé (portes K1 à K5 de la Pièce C) et le test de supériorité prédictive sur les parents (`ce_que_la_fille_predit_de_plus` et marge sur les enveloppes parentales en sélection par pari, Pièce A lignes 157-160).
3. **Critère de succès sur vraies fiches (verdict unique préenregistré) :** Le bras (f) n'est retenu que si le taux de filles recevables et promues (passant `valider_fille` en Pièce A ligne 166 + portes K1-K5 en Pièce C) dépasse celui du bras (b) d'au moins $+15\text{ points}$ de pourcentage (illustratif / SUPPOSÉ) ou présente un gain moyen de $\log W$ (preuve en mémoire, Pièce A ligne 27) strictement positif au test des rangs signés de Wilcoxon à $\alpha = 0,05$ en une seule lecture.

---

### Point 4 — Antériorités et zones vierges (Règles 3, R7, R8)

Conformément à la Règle 3, seuls les travaux dont l'attribution (auteurs, année, titre) est certaine sont cités ; les autres portent la mention « référence à vérifier ». Aucun identifiant arXiv n'est donné de mémoire.

1. **Créativité bisociative à deux matrices de pensée :**
   * *Arthur Koestler (1964), The Act of Creation.* Introduit le concept de **bisociation** comme l'intersection d'un même élément opératoire avec deux « matrices de pensée » (plans associatifs / domaines) habituellement incompatibles ou indépendantes, par opposition à la pensée routinière qui opère dans une seule matrice (**VÉRIFIÉ** conceptuellement dans la littérature ; pagination exacte : *référence à vérifier*).
   * *Ce qui lui manque :* Aucune formalisation algébrique, ni métrique de volume, ni processus de tirage algorithmique.
2. **Découverte fondée sur la littérature (Ponts A–B–C dans des littératures disjointes) :**
   * *Don R. Swanson (1986), « Fish oil, Raynaud's syndrome, and undiscovered public knowledge », Perspectives in Biology and Medicine* (cité en Pièce B § 4 ; titre exact à vérifier sur PDF). Formalise la recherche de connexions latentes entre deux littératures disjointes $A$ et $C$ ($S^{\text{dom}}_{AC} \approx 0$) via des termes intermédiaires partagés $B$.
   * *Travaux ultérieurs de pondération par rareté / TF-IDF des termes-ponts (Wren, Weeber, Gordon & Lindsay) :* *références à vérifier*.
   * *Ce qui leur manque :* L'optimisation porte sur le classement de paires isolées $(A,C)$ ou de termes $B$, sans sélection déterminantale d'un sous-ensemble diversifié de paires ni séparation formelle entre lexique de domaine et opérateurs mathématiques.
3. **Combinaisons atypiques en scientométrie :**
   * *Brian Uzzi, Satyam Mukherjee, Michael Stringer, Ben Jones (2013), « Atypical combinations and scientific impact », Science* (cité en Pièce B § 4 ; à vérifier sur PDF). Mesure la distribution des co-citations de journaux (z-score de proximité observée contre un modèle nul de permutation du graphe de citations) et montre que les articles à fort impact combinent un socle conventionnel élevé (forte proximité dans un espace) avec une queue de combinaisons rares/atypiques (éloignement dans les paires de domaines).
   * *Ce qui leur manque :* C'est un instrument descriptif *post hoc* sur le graphe des journaux, pas un opérateur génératif de recombinaison d'hypothèses ni un noyau défini positif.
4. **Processus ponctuels déterminantaux (DPP) et décomposition Qualité $\times$ Diversité :**
   * *Alex Kulesza, Ben Taskar (2012), « Determinantal Point Processes for Machine Learning », Foundations and Trends in Machine Learning* (à vérifier sur PDF). Formalise la décomposition $L = \text{diag}(q) S \text{diag}(q)$ utilisée dans la Pièce A (ligne 4), ainsi que les opérations de clôture des noyaux semi-définis positifs (somme, produit de Schur $S^{(1)} \odot S^{(2)}$).
   * *Noyaux déterminantaux sur les arêtes ou paires (Edge-DPPs / Line-graph DPPs) :* Étudiés en théorie des probabilités pour les arbres couvrants uniformes (théorème de Burton-Pemantle, 1993 — *référence à vérifier*) et en apprentissage pour la sélection de liens.
   * *Ce qui leur manque :* Chez Kulesza & Taskar, la qualité $q_i$ est un scalaire attaché à l'*individu* $i$, jamais une fonction bilinéaire de *tension entre deux espaces* $Q_{(i,j)} = f(\text{volume}_D(i,j), \text{proximité}_C(i,j))$ portée sur la diagonale d'un noyau d'arêtes.
5. **Recombinaison en évolution ouverte (Open-Endedness) et Programmation Génétique :**
   * *Kenneth O. Stanley, Joel Lehman (2011), « Abandoning Objectives: Evolution through the Search for Novelty Alone », Evolutionary Computation* (à vérifier sur PDF) ; et les algorithmes Illuminating Search / MAP-Elites (*Jean-Baptiste Mouret, Jeff Clune, 2015, « Illuminating search spaces by mapping elites »* — à vérifier sur PDF). Maintiennent des archives structurées par descripteurs comportementaux.
   * *Croisement assortatif / disassortatif en algorithmes évolutionnaires (Assortative / Disassortative Mating, Fitness Sharing, Speciation dans NEAT de Stanley & Miikkulainen, 2002 — références à vérifier) :* NEAT restreint le croisement aux individus *proches* structurellement (même espèce topologique) pour éviter les hybrides non viables, tandis que le croisement disassortatif croise des individus *éloignés* phénotypiquement pour préserver la diversité.
   * *Zone vierge identifiée (Règle R8) :* Comment coupler simultanément un **croisement disassortatif dans l'espace phénotypique/domaine** (maximiser le volume entre domaines des parents) et un **croisement assortatif dans l'espace génotypique/opérateur mathématique** (exiger une isomorphie d'opérateur rare) au sein d'un unique noyau déterminantal sur l'espace produit des paires ? À notre connaissance, cette formulation exacte (Edge-DPP à facteur de qualité bisociatif $\text{Volume}_D \times \text{Swanson}_C$) constitue une **question ouverte / zone vierge** à vérifier dans la littérature de découverte scientifique automatisée.

---

### Duels expérimentaux d'inférence forte (Règle B4)

Chaque expérience oppose deux hypothèses exclusives $H_A$ et $H_B$, avec métrique, seuil, contrôle négatif et issue falsificatrice dans les deux sens.

#### Duel 1 — Espace du noyau : Déterminant sur les paires (Edge-DPP) vs Déterminant sur les sommets (Node-DPP composé)
* **$H_A$ (Hypothèse d'arête) :** La bisociation est une propriété relationnelle d'ordre 2 ; seul un noyau défini directement sur l'espace des paires $\mathcal{E}$ (Option 1c, où le volume de domaine $\sqrt{1-\langle d_i,d_j\rangle^2}$ et l'affinité conceptuelle $\langle c_i,c_j\rangle_{\text{IDF}}$ sont dans la norme $Q_e$ de la paire) cible l'éloignement des paires et bat le tirage stratifié.
* **$H_B$ (Hypothèse de sommet) :** Un noyau composé sur les fiches $N \times N$ (Option 1a ou variante à noyau gaussien plus tranchant $S^{\text{dom}}_{ij} = \exp(-\tau \langle d_i, d_j \rangle^2)$ évoquée en Pièce B § 6) suffit à produire des paires bisociatives après filtrage sans construire l'espace des paires.
* **Protocole et Métrique :** Sur les $400$ mondes « bien observés » et $400$ mondes « moyennement observés » de la Pièce B, on compare la précision sur les 12 paires tirées de l'Option 1c (Edge-DPP) contre le meilleur Node-DPP à noyau exponentiel balayé sur $\tau \in \{1, 5, 10, 20\}$ (illustratif).
* **Contrôle négatif :** Monde sans pont (écart au placebo nul pour les deux) et ablation $q \equiv 1$.
* **Seuils et issues de falsification :**
  * Si $\text{Précision}(\text{Edge-DPP}) - \text{Précision}(\text{Node-DPP}) \ge +8,0\text{ points}$ (IC $95\%$ excluant $+5,0$) et que la part de paires éloignées du Node-DPP reste $< 0,58$ (contre $0,654$ pour le stratifié en Pièce B § 1), **$H_B$ est réfutée** : aucun noyau de sommets ne résout le problème de densité des paires proches.
  * Si le Node-DPP exponentiel atteint une part de paires éloignées $\ge 0,65$ et un écart à l'Edge-DPP $< 2,0\text{ points}$, **$H_A$ est réfutée** : le passage à l'espace des paires $\mathcal{O}(M^2)$ est une complication inutile, la platitude de $1-\cos^4$ suffisait à expliquer l'échec de la Pièce B.

#### Duel 2 — Rôle de la proximité conceptuelle : Dans l'objectif continu vs Simple filtre binaire après éloignement
* **$H_A$ (Hypothèse de co-optimisation à deux espaces) :** Intégrer la proximité conceptuelle pondérée par l'IDF ($\langle c_i, c_j \rangle_{\text{IDF}}$) multiplicativement avec le volume de domaine dans l'objectif $Q_e$ (Option 1c ou 1b) est indispensable pour éviter les moyeux et les faux ponts de surface entre domaines éloignés.
* **$H_B$ (Hypothèse de séparabilité étagée) :** Il suffit de maximiser l'éloignement de domaine (comme le diagnostic `b_eloigne` de la Pièce B, qui fait $+11,9$ points) et d'appliquer le filtre binaire d'opérateur commun existant (`ponts(a, b)` non vide, Pièce A ligne 142).
* **Protocole et Métrique :** Sur les mondes étendus à deux espaces (avec $25\%$ de moyeux et $15\%$ de faux ponts de surface inter-champs, illustratif), comparaison appariée entre `Edge-DPP(Volume_D × Swanson_C)` et `b_eloigne` (qui trie par strates de domaines dissemblables puis tire au hasard parmi les paires ayant un pont binaire). Métriques : Précision des vrais ponts et Taux de pièges moyeux/surface tirés.
* **Contrôle négatif :** Monde à moyeux rares ($5\%$, Pièce B § 4) et sans faux ponts de surface (où l'avantage de $H_A$ sur $H_B$ doit s'annuler).
* **Seuils et issues de falsification :**
  * Si `Edge-DPP` bat `b_eloigne` d'au moins $+5,0\text{ points}$ de précision en condition nominale et d'au moins $+12,0\text{ points}$ en condition « moyeux dominants » (en abaissant le taux de pièges moyeux sous $0,15$, contre $0,385$ pour le stratifié en Pièce B § 1), **$H_B$ est réfutée** : la proximité conceptuelle graduée doit entrer dans l'objectif.
  * Si l'écart entre `Edge-DPP` et `b_eloigne` reste dans $[-2,0 ; +2,0]\text{ points}$ en condition nominale, **$H_A$ est réfutée** : l'ingrédient manquant de la Pièce A n'était que la mauvaise implémentation de l'éloignement de domaine, le filtre binaire d'opérateur suffisait.

#### Duel 3 — Effet de la diversité inter-paires : Edge-DPP complet (Option 1c) vs Score glouton par strates (Option 1b)
* **$H_A$ (Hypothèse de répulsion conceptuelle inter-paires) :** Le déterminant du noyau $K_{e,e'}$ sur les paires augmente le **rappel** de ponts distincts sur les 12 tirages en empêchant de consommer plusieurs paires du budget sur le même concept-pont rare.
* **$H_B$ (Hypothèse de suffisance de la stratification de domaine) :** Imposer une paire par strate de domaines $(D_a, D_b)$ avec le score scalaire $w_{ij} = Q_{(i,j)}$ (Option 1b, sans déterminant inter-paires) suffit à diversifier les 12 paires.
* **Protocole et Métrique :** Rappel des vrais ponts distincts à budget fixé ($12$ paires sur $3$ générations, Pièce B § 1) dans des mondes où un même concept rare relie 3 paires d'articles à travers différentes strates (illustratif).
* **Contrôle négatif :** Tirage d'une seule paire ($m=1$), où Option 1c et Option 1b sélectionnent mathématiquement la même paire maximale ($\arg\max_e Q_e^2$) et doivent avoir un écart strictement nul ($0,000$).
* **Seuils et issues de falsification :**
  * Si le rappel de ponts conceptuels distincts de 1c dépasse celui de 1b de $\ge +3,5\text{ points}$ (IC $95\%$ hors de $0$), **$H_B$ est réfutée**.
  * Si l'écart de rappel est $< +1,5\text{ point}$, **$H_A$ est réfutée** : par rasoir d'Ockham (même règle qui a fait préférer le stratifié en Pièce B), on abandonne Cholesky sur les paires et on garde le score bilinéaire stratifié 1b.

---

## (c) Mesure minimale de fonctionnement pour chaque instrument nommé

Pour chaque brique instrumentale nommée dans la question et les pièces, voici le protocole minimal qui certifie qu'elle fonctionne *avant* son intégration, avec taux de détection (rappel), taux de fausses alertes (FPR), cas honnêtes appariés et vérification mécanique triviale à battre.

| Instrument nommé | Cas honnêtes appariés (Vérité terrain) | Métrique : Taux de détection (Rappel) & Fausses alertes (FPR) | Vérification mécanique (Baseline) à battre | Seuil minimal de fonctionnement (illustratif / SUPPOSÉ) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Extracteur / Représentation des concepts mathématiques ($c_i$)** | 100 paires de fiches (ou résumés arXiv/OpenAlex, Pièce B § 8) : 50 paires *isomorphes* (même outil mathématique, ex. concentration de martingale, mais domaines disjoints : trafic réseau vs génomique) et 50 paires *homonymes/thématiques* (même domaine applicatif, outils mathématiques disjoints : martingale vs géométrie algébrique). | **Détection :** Rappel à $\cos(c_i, c_j) > \theta$ sur les 50 paires isomorphes inter-domaines.<br>**Fausses alertes :** FPR sur les 50 paires de même domaine mais concepts disjoints + paires partageant un mot-outil générique (« borne », « linéaire »). | Intersection lexicale brute (TF-IDF des mots du texte complet ou simple correspondance exacte des chaînes `a.operateurs & b.operateurs` de la Pièce A ligne 142). | **Rappel $\ge 0,80$** pour un **FPR $\le 0,05$** sur les paires de même domaine à concepts différents ; gain de rappel $\ge +25$ points sur le TF-IDF brut à FPR égal. |
| **2. Représentation et volume de domaine ($\sqrt{1-\langle d_i,d_j\rangle^2}$)** | 400 mondes de validation (`validation-generateur-v1.json`, Pièce B § 10) + 200 paires de vraies fiches annotées par axe/sous-domaine (même domaine, même champ mais domaines distincts, champs disjoints). | **Détection :** Taux de paires de champs disjoints classées dans le quartile supérieur de volume.<br>**Fausses alertes :** Taux de paires du *même domaine* ou *même champ* dont le volume calculé dépasse le seuil d'éloignement (erreur d'orthogonalité due à un vocabulaire trop creux). | Étiquette discrète du premier domaine déclaré `_domaine_estime(f)` (Pièce A ligne 181 : `1` si domaines différents, `0` sinon, qui confond domaines proches du même champ et domaines éloignés). | Séparation stricte des médianes : $\langle d_i,d_j\rangle_{\text{même champ}} \ge 0,25$ et $\langle d_i,d_j\rangle_{\text{champs disjoints}} \le 0,05$ (conforme à Pièce B § 2.3 : $0,28$ vs $0,03$) ; **AUC $\ge 0,92$** pour distinguer « domaines proches (même champ) » de « domaines éloignés (champs distincts) », là où `_domaine_estime` binaire a une AUC de $0,50$ sur les paires de domaines distincts. |
| **3. Filtre de compatibilité des contraintes (`compatibles(a, b)`, Pièce A l. 58)** | Jeu d'essai b4 (Pièce B § 5) + 100 paires de fiches réelles dont 50 contiennent une contradiction mathématique vraie (ex. hypothèse de bruit i.i.d. stationnaire vs régime adversarial non stationnaire) et 50 sont compatibles mais utilisent les deux adjectifs dans des sous-parties distinctes (ex. « opérateur linéaire sur un espace non linéaire »). | **Détection :** Rappel des vraies contradictions (en Pièce B § 5, le filtre actuel ne mesure qu'un rappel de **$0,57$ à $0,60$** et laisse passer $0,251$ à $0,274$ de contraintes incompatibles parmi les 12 paires, Pièce B § 1).<br>**Fausses alertes :** Rejets à tort de paires compatibles (actuellement $4$ à $5\%$ en Pièce B § 5). | Les 5 paires d'expressions régulières globales `PAIRES_CONTRADICTOIRES` de la Pièce A (lignes 41-42) appliquées sans portée syntaxique sur tout le champ `contraintes`. | Maintenir les **fausses alertes (rejets à tort) $\le 0,05$** tout en montant le **rappel des contradictions vraies de $0,58$ à $\ge 0,75$** (par rattachement de l'adjectif au sujet grammatical ou typage des hypothèses dans le gabarit). |
| **4. Moteur de tirage à deux espaces (`Edge-DPP` / `Swanson-Volume`)** | Les 400 mondes « bien » et 400 mondes « moyen » à ponts plantés de la Pièce B, plus les 400 mondes à vérité inversée et 400 mondes à moyeux dominants ($0,6$). | **Détection :** Précision et rappel des vrais ponts plantés parmi les 12 paires tirées.<br>**Fausses alertes :** Part de pièges tirés parmi les 12 paires (opérateurs-moyeux, homonymes, parasites, partages intra-champ). | Tirage stratifié `(b)` (précision $0,203 / 0,127$, moyeux $0,385$) ET Marche de Swanson `(d1)` (précision $0,239 / 0,165$, paires éloignées seulement $0,446$). | **Précision $\ge 0,33$** en « bien » et **$\ge 0,20$** en « moyen » ; **part de paires éloignées $\ge 0,70$** (contre $0,446$ pour d1) ; **pièges moyeux $\le 0,12$** (contre $0,385$ pour b). |
| **5. Garde de supériorité prédictive de la fille (`valider_fille` + sélection par pari, Pièce A l. 157-180)** | 50 fiches filles synthétiques ou historiques : 25 « vraies synergies » (la loi prédictive combinée bat chaque parent et leurs mélanges convexes) et 25 « perroquets / concaténations » (reformulation d'un parent ou simple disjonction « si domaine A alors parent A, sinon parent B »). | **Détection :** Taux d'acceptation des vraies synergies.<br>**Fausses alertes :** Taux de promotion de filles qui ne sont que des enveloppes convexes, mélanges harmoniques ou concaténations `si/sinon` des parents (Pièce A ligne 159). | `valider_fille` actuel (Pièce A lignes 174-177 : vérifie seulement que `ce_que_la_fille_predit_de_plus` est non vide et que le hash `signature_prediction` diffère exactement de ceux de A et B — ce qu'un changement d'une décimale contourne). | **FPR $\le 0,02$** sur les concaténations `si/sinon` et les perturbations epsilon d'un parent (contre $1,00$ pour le simple test d'égalité de signature), pour un **rappel $\ge 0,85$** sur les vraies lois synergiques. |

---

## (d) Ancrage matériel, modèles ouverts, calcul nécessaire et coût estimé

Conformément à la Règle 4 et aux consignes de la question, tous les chiffres tirés de la Pièce B sont distingués des estimations nouvelles, lesquelles sont marquées **illustratif / SUPPOSÉ** ; aucune dépense ni accès réseau n'est engagé sans devis et GO de Lazar.

1. **Étage 1 — Banc d'essai synthétique à deux espaces (Extension de `trancher_v1.py`, Pièce B) :**
   * **Environnement :** Processeur seul (CPU), bibliothèque standard de Python 3.13 (`python3 -I -B`, aucune dépendance externe, conformité totale avec la Pièce A et la Pièce B).
   * **Modèles utilisés :** Aucun modèle de langage ($0$ jeton).
   * **Volume de calcul et temps :** Le banc v1 de la Pièce B ($4\,000$ mondes $\times 10$ bras/diagnostics) tourne en **$93\text{ secondes}$** sur un cœur CPU (**RAPPORTÉ**, Pièce B § 5). L'ajout de l'Edge-DPP (Cholesky de rang $m=4$ sur $M \le 150$ paires valides par génération) ajoute environ $3\text{ ms}$ par monde, soit un temps total estimé à **$120\text{ à }180\text{ secondes}$ CPU** pour $4\,000$ mondes (**illustratif / SUPPOSÉ**).
   * **Coût financier :** **$0,00\text{ USD}$** (**VÉRIFIÉ** pour le calcul local sur processeur).

2. **Étage 2 — Calibrage de l'extracteur de concepts et rétrodiction sur littérature ouverte (Pièce B § 8) :**
   * **Données :** Corpus local déjà téléchargé ou instantané ouvert d'arXiv / OpenAlex (après GO de Lazar pour l'accès réseau, Pièce B § 8), par exemple $10\,000$ résumés datés répartis sur 8 catégories arXiv (ex. `math.PR`, `stat.ML`, `cs.IT`, `physics.soc-ph`, `q-bio.NC`, `econ.TH`, `cs.CR`, `math.OC`, **illustratif / SUPPOSÉ**).
   * **Calcul de l'extraction (Option 2c) :** Analyse par expressions régulières, AST LaTeX et tables de fréquences en Python pur : environ **$2\text{ minutes}$ sur CPU** pour $10\,000$ résumés (**illustratif / SUPPOSÉ**), **$0,00\text{ USD}$**.
   * **Optionnel — Étiquetage hors-boucle par modèle ouvert local (si test de l'Option 2b par modèle tiers scellé avant tirage) :** Utilisation d'un modèle à poids ouverts exécuté localement à température $0$ avec graine fixe, par exemple **Qwen-2.5-7B-Instruct** ou **Llama-3.1-8B-Instruct** (ou un modèle d'enchâssement mathématique ouvert comme **MathBERT** / **SPECTER2** pour le test de séparabilité, **illustratif / SUPPOSÉ**). Sur une carte GPU locale de $24\text{ Go}$ VRAM (type RTX 3090/4090 ou A10G), l'extraction structurée sur $1\,000$ fiches prend environ **$0,2\text{ heure GPU}$** (soit **$\approx 0,20\text{ à }0,50\text{ USD}$** en équivalent cloud, **illustratif / SUPPOSÉ**).

3. **Étage 3 — Validation de bout en bout sur les vraies fiches de la Course 2 (avec appel à l'agent de fusion) :**
   * **Protocole :** Sur un vivier figé de $N = 20$ à $40$ fiches survivantes de la Course 2, exécution de `recombiner()` (Pièce A ligne 212) pour comparer le bras témoin `stratifie` et le bras `edge_dpp_deux_espaces` sur $3$ générations $\times 3$ paires par bras $= 9$ fusions par bras (au plus $18$ appels à `adaptateur.lancer("recombinaison", ...)` par course d'essai, Pièce A ligne 265).
   * **Modèles :** Soit un modèle ouvert local de taille moyenne (**Qwen-2.5-32B-Instruct** ou **Llama-3.3-70B-Instruct** sur $1 \text{ à } 2 \times \text{A100 80 Go}$, **illustratif / SUPPOSÉ**), soit le modèle d'API configuré dans `config.modele_recombinaison` (Pièce A ligne 266).
   * **Coût estimé :** À raison d'environ $4\,000$ jetons d'entrée (2 fiches parentes + mémoire, Pièce A lignes 148-161) et $2\,000$ jetons de sortie par fusion, 18 fusions représentent $\approx 72\,\text{k}$ jetons d'entrée et $36\,\text{k}$ jetons de sortie, soit **$0,50\text{ à }2,50\text{ USD}$** au total selon le tarif du modèle retenu dans `plafond_recombinaison_usd` (**illustratif / SUPPOSÉ**, soumis au devis et au GO de Lazar).

FIN-DE-CELLULE