# Proposition B, tour III.1

**Pièce transmise.** Le bloc QUESTION DE L'ARBITRE reprend mot pour mot le bloc FAITS, avec la même empreinte sha256. Il ne pose donc aucune question ciblée. Je retiens comme question la tâche en sept parties, ainsi que sa forme, et j'y range les livrables : (a) en partie 1, (b) en parties 5 et 7, (c) en partie 4, (d) en partie 7.

**Statuts.** H1 à H10 sont des HYPOTHÈSES, tirées des faits. Chaque affirmation tirée de la littérature est RAPPORTÉE : je la cite de mémoire et je n'ai rien vérifié pendant cette session. Toute proposition de ma part est une HYPOTHÈSE. Rien ici n'est VÉRIFIÉ. Les faits ne contiennent aucun chiffre, donc tous les chiffres qui suivent sont **illustratifs**. Ce tour est à l'aveugle : aucune autre proposition ne m'est parvenue, je n'en critique donc aucune.

---

## 1. Confrontation à la littérature

### 1.0 Trois questions que les hypothèses mêlent

- **L'intérêt, qui dépend du public.** Selon Davis (1971, « That's interesting! », *Philosophy of the Social Sciences* 1), une thèse paraît intéressante quand elle nie une croyance que son public tient pour acquise (RAPPORTÉ). L'intérêt se mesure donc comme un écart aux attentes du moment, pas comme une propriété de l'idée.
- **La vérité et la fécondité.** On ne les observe qu'après coup : réplication, réutilisation par d'autres groupes.
- **La production.** C'est un processus de recherche : combinaison, transfert, analogie.

H1 mélange les deux premières : la distance de surface ferait l'intérêt, la proximité cachée la viabilité. H7 confond la fécondité avec un intérêt reconnu après coup. H5 et H8 parlent de production, H10 d'intérêt.

### (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut |
|---|---|---|
| a1 | L'« idée intéressante » est une propriété de l'idée, et non une relation entre l'idée et un public | HYPOTHÈSE. Davis (1971) la contredit (RAPPORTÉ) |
| a2 | Les concepts sont des unités repérables et stables dans le temps | HYPOTHÈSE. Le sens des mots dérive : Hamilton, Leskovec & Jurafsky (2016), *Diachronic word embeddings reveal statistical laws of semantic change*, ACL (RAPPORTÉ) |
| a3 | On peut mesurer la distance de surface et la proximité cachée **indépendamment l'une de l'autre** | HYPOTHÈSE. Si les deux se mesurent sur le même texte, le raisonnement tourne en rond |
| a4 | Une « distance » au sens métrique existe. Or H2 (A–B, B–C, donc A–C) suppose une transitivité qui contredit H4 si l'inégalité triangulaire ne tient pas | HYPOTHÈSE |
| a5 | Les exemples historiques (horloges et relativité, fluides et trous noirs) décrivent de vraies causes | HYPOTHÈSE dans les faits. Galison (2003), *Einstein's Clocks, Poincaré's Maps*, défend un rôle des horloges, ce qui reste discuté (RAPPORTÉ). Unruh (1981, *Phys. Rev. Lett.* 46) a proposé l'analogue sonique pour des raisons théoriques, et les expériences en fluides sont venues **ensuite** (RAPPORTÉ). Le transfert irait donc dans le sens inverse de celui que suggère H5 |
| a6 | Les découvertes simultanées sont des événements indépendants, et pas des artefacts de querelles de priorité ou de définition | HYPOTHÈSE |
| a7 | Un modèle de langage peut avoir un état « équivalent à l'anesthésie » | HYPOTHÈSE, sans définition opérationnelle |
| a8 | La surprise est un scalaire mesurable chez un agent, et elle suit l'intérêt | HYPOTHÈSE |
| a9 | On peut faire de la prédiction rétrospective avec des modèles entraînés sur des données postérieures à la date de coupure | HYPOTHÈSE à rejeter : ces modèles connaissent déjà la suite (fuite) |
| a10 | Les mariages réussis laissent une trace dans les publications | HYPOTHÈSE. Le savoir tacite et les échecs restent largement non publiés |

### 1.1 Verdict pour chaque hypothèse (toutes les références sont RAPPORTÉES)

**H1, mariage éloigné.**
- *Soutenue pour l'impact, inconnue pour la proximité cachée.*
- Uzzi, Mukherjee, Stringer & Jones (2013), *Atypical combinations and scientific impact*, *Science* 342 : l'impact est plus fréquent quand une queue de combinaisons atypiques s'appuie sur un noyau conventionnel.
- Shi & Evans (2023), *Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines*, *Nature Communications*.
- Wang, Veugelers & Stephan (2017), *Bias against novelty in science*, *Research Policy* : les travaux nouveaux sont plus risqués et reconnus plus tard.
- Côté cognition, Gick & Holyoak (1980), *Analogical problem solving*, *Cognitive Psychology* 12 : le transfert spontané entre analogues éloignés en surface est rare.
- À ma connaissance, aucun de ces travaux ne teste l'idée que la proximité *structurelle* expliquerait la viabilité.

**H2, cascades et transferts.**
- *Soutenue comme heuristique.* C'est le modèle ABC de Swanson (1986), *Fish oil, Raynaud's syndrome, and undiscovered public knowledge*, *Perspectives in Biology and Medicine* 30. Voir aussi Henry & McInnes (2017), *Literature based discovery: models, methods, and trends*, *J. Biomedical Informatics*. Le taux de succès des liens A–C proposés reste mal évalué.
- *L'exemple de l'anesthésie appliqué à un modèle de langage est une métaphore non opérationnalisée.* Les marqueurs humains reposent sur la perturbation d'un substrat physique : Alkire, Hudetz & Tononi (2008), *Consciousness and anesthesia*, *Science* 322 ; Casali et al. (2013), *A theoretically based index of consciousness independent of sensory processing and behavior*, *Sci. Transl. Med.* 5.

**H3, serrure et clé.**
- *Soutenue pour l'analogie.* Gentner (1983), *Structure-mapping: A theoretical framework for analogy*, *Cognitive Science* 7, avec son principe de systématicité. Falkenhainer, Forbus & Gentner (1989), *The structure-mapping engine*, *Artificial Intelligence* 41. Holyoak & Thagard (1989), *Analogical mapping by constraint satisfaction*, *Cognitive Science* 13.
- *Noether et le lagrangien sont une métaphore.* Un graphe de concepts n'a ni action ni symétrie continue définies. Je les écarte et les remplace par un morphisme partiel (partie 2).

**H4, ni trop près ni trop loin.**
- *Soutenue, mais sous une autre forme.* Fleming (2001), *Recombinant uncertainty in technological search*, *Management Science* 47 : recombiner des éléments éloignés augmente surtout la **variance** des résultats. Uzzi et al. (2013) décrivent un mélange de proche et de lointain, pas un optimum de distance unique.
- « Trop loin, rien ne se lie » est banal.
- Le U inversé de l'intérêt reste *inconnu*, et il est exposé au biais du survivant.

**H5, champ et air du temps.**
- *Le phénomène des découvertes multiples est rapporté.* Ogburn & Thomas (1922), *Are inventions inevitable?*, *Political Science Quarterly* 37. Merton (1961), *Singletons and multiples in scientific discovery*, *Proc. Am. Philos. Soc.* 105.
- *L'explication par l'air du temps est contestée.* Simonton (1979), *Multiple discovery and invention: Zeitgeist, genius, or chance?*, *J. Personality and Social Psychology* 37, trouve une distribution compatible avec un modèle de hasard (le détail est à vérifier).
- Le ferromagnétisme n'est qu'une image. L'« emboîtement aléatoire comme les protéines » n'a pas de contenu : je l'écarte.
- Reste un contenu testable : une méthode nouvelle, adoptée par deux champs, sert de **cause commune** aux liens qui se forment ensuite.

**H6, connexion et distinction.**
- *Inconnue.* La différenciation chaleur/température est décrite par Wiser & Carey (1983) (référence à vérifier).
- C'est testable comme une scission de sens au fil du temps.

**H7, profondeur de l'idée fille.**
- *En grande partie confondue avec l'attachement préférentiel.* Price (1965), *Networks of scientific papers*, *Science* 149. Barabási & Albert (1999), *Emergence of scaling in random networks*, *Science* 286. Tomber près des nœuds est le comportement attendu par défaut.
- Le volet « unifier » peut se mesurer par l'indice de disruption : Funk & Owen-Smith (2017), *Management Science* ; Park, Leahey & Funk (2023), *Papers and patents are becoming less disruptive over time*, *Nature* 613.

**H8, émergence.**
- *L'effet de la diversité et des outsiders est partiellement soutenu.* Hofstra et al. (2020), *The diversity–innovation paradox in science*, *PNAS* 117. Shi & Evans (2023).
- *La percolation est une image*, sauf si l'on observe une transition brutale qui résiste à un test de mise à l'échelle de taille finie. À ma connaissance, ce n'est pas montré : statut *inconnu*.

**H9, structure cachée du langage.**
- *Partiellement soutenue.* Landauer & Dumais (1997), théorie de l'analyse sémantique latente (LSA), *Psychological Review* 104. Tshitoyan et al. (2019), *Unsupervised word embeddings capture latent knowledge from materials science literature*, *Nature* 571. Krenn & Zeilinger (2020), *PNAS*. Krenn et al. (2023), *Nature Machine Intelligence* (Science4Cast).
- *Limite.* Les plongements de mots (vecteurs appris à partir des cooccurrences) mesurent surtout la proximité d'usage, donc la surface. C'est justement ce que H1 veut dépasser.
- Les analogies calculées sur ces vecteurs sont fragiles : Linzen (2016), RepEval ; Rogers, Drozd & Li (2017), *SEM.
- Rien n'indique que les axes de variance maximale de l'analyse en composantes principales (ACP) portent la structure relationnelle.

**H10, signal de surprise.**
- *Le construit formel existe.* Itti & Baldi (2009), *Bayesian surprise attracts human attention*, *Vision Research* 49. Schultz, Dayan & Montague (1997), *A neural substrate of prediction and reward*, *Science* 275. Schmidhuber (2010), *Formal theory of creativity, fun, and intrinsic motivation*, *IEEE TAMD* 2. Pathak et al. (2017), *Curiosity-driven exploration by self-supervised prediction*, ICML.
- « Analogue dopaminergique » n'est qu'une image.
- Limite connue en apprentissage par renforcement : la surprise est maximale sur le bruit.

**Bilan.**
- Déjà établies ou banales : H2 (ABC), H4 (sous sa forme « variance »), H7 (attachement préférentiel), H9 en partie.
- Métaphores sans contenu : Noether, ferromagnétisme, protéines, dopamine, et percolation sauf test.
- **Centrales et inconnues** : le volet caché de H1, et la cause commune des multiples dans H5.

---

## 2. Modèle formel minimal (HYPOTHÈSE)

### Objets

- **Concepts.** $V_t$, chacun avec sa date d'apparition.
- **Couche usage $U_t$.** Graphe pondéré des cooccurrences dans les textes antérieurs ou égaux à $t$.
- **Couche structure $S_t$.** Graphe dont les arêtes portent un type de relation $r\in R$ (prédications « traite », « inhibe », etc., ou opérateurs dans les arbres d'équations). **Les noms des concepts y sont effacés.**
- **Couche communauté $C_t$.** Graphe biparti auteurs–concepts.

### Variables pour une paire $(i,j)$ non liée à $t$

- **Distance de surface linguistique.** $D_u = 1-\cos(e_i^{(t)},e_j^{(t)})$, sur des plongements entraînés uniquement sur des données antérieures ou égales à $t$.
- **Distance de surface sociale.** $D_c = 1-\text{Jaccard}(\text{auteurs}_i,\text{auteurs}_j)$.
- **Proximité cachée.** $\Pi$ est la similarité de rôle dans $S_t$ : un noyau de Weisfeiler-Lehman (qui compare des graphes par leurs voisinages étiquetés) appliqué aux voisinages de $i$ et de $j$, avec pour seules étiquettes les types de relation. Comme $S_t$ ne contient pas les mots, $\Pi$ est indépendant de $D_u$ par construction, ce qui traite a3.
- **Serrure et clé.** On cherche une injection partielle $\varphi: N_S(i)\to N_S(j)$ entre les voisinages de $i$ et de $j$. Deux grandeurs en découlent :
  - la couverture $\kappa = |\{(a,b,r)\in E(N_i): (\varphi a,\varphi b,r)\in E(N_j)\}|/|E(N_i)|$, part des relations préservées ;
  - les conflits $\chi$, nombre d'arêtes dont l'image porte un type contradictoire.
  
  On peut utiliser $\Pi' = \kappa-\lambda\chi$ à la place de $\Pi$.
- **Le « champ », réduit à ce qu'il a de mesurable.** $M_{ij}(t)=\sum_m a_{im}(t)\,a_{jm}(t)$, où $m$ parcourt les méthodes ou instruments d'âge inférieur à $\tau$, et $a_{im}(t)$ vaut 1 si le concept $i$ a adopté $m$.
- **Termes de base.** $CN_{ij}$, nombre de chemins de longueur 2 entre $i$ et $j$ (le modèle ABC), et $k_i$, degré de $i$.

### Naissance d'une idée

Probabilité qu'un lien apparaisse entre $t$ et $t+\Delta$ :

$$\text{logit}\,P(L_{ij}^{t+\Delta}=1)=\underbrace{\beta_0+\beta_1\log k_ik_j+\beta_2\log(1{+}CN_{ij})-\beta_3D_u-\beta_4D_c}_{B_0}+\underbrace{\gamma_1\Pi+\gamma_2\,\Pi D_u+\gamma_3M_{ij}}_{B_1}$$

- H1 prédit $\gamma_1>0$ et $\gamma_2>0$ : la proximité cachée pèse davantage quand la surface est lointaine.
- H5 prédit $\gamma_3>0$.
- L'hypothèse rivale H_B est $\gamma=0$ hors échantillon.

### Intérêt de l'idée fille

Deux grandeurs distinctes, jamais fusionnées d'avance :

- **Surprise relative au public.** $\sigma_{ij}=-\log\hat P_{B_0,\le t}(L_{ij})$. C'est une opérationnalisation de Davis (1971), où $B_0$ tient lieu des croyances collectives du moment.
- **Fécondité.** $F_{ij}$ est le nombre de groupes d'auteurs, disjoints des fondateurs, qui réutilisent le lien pendant $[t+\Delta,t+2\Delta]$. S'y ajoute l'indice de disruption des articles fondateurs.

Prédictions :
- H1 (volet viabilité) : à $\sigma$ fixé, $\partial F/\partial\Pi>0$.
- H4 : $E[F\mid\sigma]$ non monotone.

### Analogies physiques

| Analogie | Apporte-t-elle plus qu'une image ? | Décision |
|---|---|---|
| Puits | Un potentiel $V=-\log P$ ne fait que réécrire la probabilité | Écartée |
| Champ | Seule une covariable partagée $M_{ij}(t)$ est mesurable | Réduite à $M$ |
| Polarisation | Aucune grandeur mesurable | Écartée |
| Résonance | Aucune fréquence définie | Écartée |
| Noether et lagrangien | Ni action ni symétrie continue | Écartée, remplacée par le morphisme $(\kappa,\chi)$ |
| Percolation | Testable : la plus grande composante du graphe inter-champs, en fonction de sa densité, saute-t-elle plus nettement que dans un modèle de configuration à mêmes degrés ? | Gardée sous condition, sinon écartée |

Aucune dynamique d'émergence n'est conservée.

### Modèle de base et comparaison

- **Le modèle de base** est $B_0$ : attachement préférentiel, plus fermeture des triangles, plus décroissance avec la distance de surface. L'apparition de nouveautés y est décrite par une urne de Pólya avec déclenchement, version formelle du « possible adjacent » : Tria, Loreto, Servedio & Strogatz (2014), *The dynamics of correlated novelties*, *Sci. Rep.* 4. Ce cadre rejoint la croissance par recombinaison de Weitzman (1998), *QJE* 113 (RAPPORTÉ).
- **$B_1$ n'ajoute que trois paramètres.** $B_0$ prédit que les liens lointains qui se forment sont ceux qui ont un $CN$ élevé. $B_1$ prédit qu'à $CN$ et $D_u$ égaux, $\Pi$ départage encore les paires.
- **Règle de décision.** Si $B_1$ n'apporte aucun gain hors échantillon, $B_0$ suffit et ni H1 ni H5 ne sont nécessaires.

---

## 3. Données brutes

| Source | Variables tirées |
|---|---|
| OpenAlex : métadonnées, citations, auteurs, thèmes datés | $k$, $D_c$, $CN$, $F$, indice de disruption |
| S2ORC (Lo et al., 2020, ACL), PubMed Central OA, arXiv avec sources LaTeX | $U_t$ et $D_u$. Arbres d'opérateurs des équations, obtenus en passant du LaTeX au MathML, pour $S_t$ |
| MeSH (année d'introduction de chaque descripteur), PhySH, classification MSC | $V_t$ et dates de naissance des concepts |
| SemMedDB : prédications sujet–relation–objet extraites de PubMed (Kilicoglu et al., 2012, *Bioinformatics*) | $S_t$ typé, côté biomédical |
| Mentions de techniques et de logiciels (branche « techniques » de MeSH, à vérifier) | $M_{ij}(t)$ |
| Multiples : Ogburn & Thomas (1922), Merton (1961), listes secondaires à auditer | Test de H5. Codage : date, champs parents, indépendance attestée |
| Échecs : liens apparus puis abandonnés, rétractations (base Retraction Watch), paires A–C proposées et non confirmées, négatifs de Science4Cast | Dénominateur du biais du survivant |
| Découvertes reconnues (prix et articles fondateurs ; jeu annoté existant, référence à vérifier) | Évaluation seulement, jamais l'entraînement |

---

## 4. Méthodes et outils

### Pipeline

- **Entités.** scispaCy (Neumann et al., 2019, BioNLP), avec normalisation vers UMLS.
- **Plongements datés.** word2vec skip-gram (Mikolov et al., 2013), entraîné sur chaque tranche de temps antérieure ou égale à $t$, puis alignement des tranches par Procrustes orthogonal (Hamilton et al., 2016). **Aucun grand modèle de langage entraîné après $t$** pour calculer les variables (a9).
- **$\Pi$.** Noyau de Weisfeiler-Lehman (Shervashidze et al., 2011, *JMLR* 12), avec struc2vec en alternative (Ribeiro, Saverese & Figueiredo, 2017, KDD).
- **$\kappa$ et $\chi$.** SME sur les petits cas. À grande échelle, appariement de graphes FAQ (Vogelstein et al., 2015, *PLOS ONE*).
- **Prédiction de liens.** Régression logistique pénalisée, avec LightGBM comme contrôle. Métriques : aire sous la courbe ROC et sous la courbe précision-rappel (AUC-ROC, AUC-PR), précision sur les $k$ premiers. Comparaison des aires par le test de DeLong (DeLong, DeLong & Clarke-Pearson, 1988, *Biometrics* 44) et par bootstrap.
- **Vitesse d'apparition des liens.** Modèle de Cox avec covariables qui varient dans le temps.
- **U inversé.** Test des « deux droites » de Simonsohn (2018), *Advances in Methods and Practices in Psychological Science*.
- **Multiples.** Modèle nul de Poisson ou binomial négatif, dans la lignée de Simonton (1979). Régression logistique conditionnelle sur des paires multiple/singleton appariées.
- **Percolation.** Modèle de configuration comme référence, mise à l'échelle de taille finie : Stauffer & Aharony, *Introduction to Percolation Theory* (livre).
- **Surprise.** Surprisal moyenne par token de l'énoncé « i r j », sous un modèle de langage dont les données s'arrêtent avant $t$.

### (c) Mesure minimale pour chaque instrument nommé dans la question

**1. ACP ou modèle non supervisé comme détecteur de dimension cachée (H9).**
- *Cas honnêtes appariés.* On prend un sous-corpus et on remplace chaque terme du domaine par un jeton neuf. La surface devient maximale, la structure reste intacte. Le détecteur doit apparier chaque jeton renommé avec son original.
- *Contrôle négatif.* Même renommage, puis permutation des relations, à fréquences constantes.
- *Mesures.* Taux de détection au rang 1. Taux de fausses alertes sur le corpus permuté.
- *Vérification mécanique à battre.* Un appariement fondé seulement sur le profil de fréquence et de degré.

**2. $\Pi$ et le critère serrure-clé (H1, H3).**
- *Cas positifs.* Des paires inter-champs dont les équations ont le même arbre d'opérateurs une fois les variables renommées, par exemple la diffusion dans plusieurs disciplines.
- *Cas négatifs appariés.* Même $D_u$ et même degré, mais des arbres non isomorphes.
- *Vérification mécanique à battre.* L'isomorphisme exact d'arbres canoniques. $\Pi$ doit l'égaler sur ces cas, puis faire des détections hors équations qui tiennent en évaluation aveugle.

**3. Signal de surprise (H10).**
- *Cas positifs.* Les liens qui se forment avec un $F$ élevé.
- *Cas appariés.* Des liens tout aussi rares à $t$ (cooccurrence nulle, mêmes degrés) qui ne se forment jamais. S'y ajoutent des paires aléatoires absurdes.
- *Vérifications mécaniques à battre.* $-\log$ de la cooccurrence, rareté des mots, longueur de l'énoncé.
- *Exigence.* Une aire sous la courbe ROC supérieure à celle de ces vérifications, et un taux d'alerte sur les paires absurdes au plus égal au taux sur les vrais cas.

**4. Motif « anesthésie » dans un modèle de langage (H2).**
- Aucun cas étalon n'existe, donc on ne peut pas valider ce motif comme marqueur de conscience.
- *Mesure minimale.* Un analogue de l'indice de complexité perturbationnelle, calculé sur les activations, doit distinguer deux états contrôlés : l'attention entre tokens coupée, contre un bruit de même norme injecté ailleurs.
- *Vérifications mécaniques à battre.* La norme des activations, leur entropie, la perplexité. Si ces quantités prédisent le score ($R^2>0{,}8$, illustratif), le motif n'apporte rien.
- Une issue positive ne dirait rien de la conscience. Elle dirait seulement que le marqueur transposé n'est pas trivial.

---

## 5. Validation hors de l'auteur du modèle et duels (b)

### Principes

- **Découpage temporel.** Entraînement jusqu'à $T$, test sur $(T, T+\Delta]$.
- **Biais du survivant.** Le dénominateur contient **toutes** les paires non liées à $T$. Un lien qui apparaît puis tombe à l'abandon compte comme $F=0$.
- **Bases de comparaison.** $B_0$, l'attachement préférentiel seul, le cosinus seul, le hasard.
- **Préenregistrement.** Code, graines aléatoires, seuils et puissance statistique gelés avant d'ouvrir les années de test.
- **Évaluation humaine en aveugle.** Des experts reçoivent une liste mêlée : les $k$ premières paires de $B_1$, celles de $B_0$, de vrais liens futurs et des paires aléatoires appariées en distance. Ils notent séparément la *plausibilité* et l'*intérêt*, conformément à la distinction de 1.0.

### Duels

Tous les seuils sont illustratifs.

**D1, volet caché de H1.**
- *H_A.* $\Pi$ améliore la prédiction des liens lointains (paires du quintile supérieur de $D_u$).
- *H_B.* $B_0$ suffit.
- *Métrique.* Gain d'AUC-PR de $B_1$ sur $B_0$.
- *Seuil.* Gain d'au moins 0,02, avec un intervalle de confiance à 95 % qui exclut 0.
- *Contrôle négatif.* $\Pi$ recalculé sur un $S_t$ aux types permutés et aux degrés conservés : le gain doit être à peu près nul.
- *Ce qui falsifie H_A.* Un intervalle qui contient 0, ou un $\Pi$ permuté aussi performant.
- *Ce qui falsifie H_B.* Un gain au-dessus du seuil avec un contrôle nul.

**D2, interaction prédite par H1.**
- *H_A.* $\gamma_2>0$.
- *H_B.* $\gamma_2\le0$.
- *Contrôle négatif.* Le même modèle, ajusté sur des paires proches seulement.
- *Ce qui falsifie H_A.* $\Pi$ n'aide que pour les paires proches.
- *Ce qui falsifie H_B.* $\gamma_2>0$, avec un intervalle de confiance à 95 % qui exclut 0.

**D3, U inversé de H4.**
- *H_A.* Parmi les liens formés, $F(\sigma)$ forme un U inversé : le test des deux droites donne des pentes de signes opposés, chacune avec $p<0{,}05$.
- *H_B.* $F(\sigma)$ est monotone.
- *Contrôle négatif.* $F$ permuté à l'intérieur de chaque couple champ × année : aucune forme ne doit apparaître.
- *Ce qui falsifie H_A.* Une seule pente significative.
- *Ce qui falsifie H_B.* Deux pentes opposées significatives.
- *Biais du survivant.* On publie aussi la version non conditionnée sur la formation du lien.

**D4, H5 et les multiples.**
- *H_A.* Avant une découverte multiple, $M$ est plus élevé qu'avant un singleton apparié (même champ, même décennie, même $CN$).
- *H_B.* Le nul de Poisson de Simonton suffit, et $M$ n'ajoute rien.
- *Métrique.* Rapport de cotes (odds ratio, OR) associé à $M$.
- *Seuil.* OR supérieur à 1,5.
- *Contrôle négatif.* $M$ calculé avec des méthodes apparues *après* la découverte : il doit être nul, sinon le codage fuit.
- *Ce qui falsifie H_A.* Un OR proche de 1.
- *Ce qui falsifie H_B.* Un OR supérieur à 1,5 et une surdispersion du nombre de multiples expliquée par $M$.

**D5, H10 face à la simple rareté.**
- *H_A.* La surprisal d'un modèle de langage daté prédit $F$ au-delà de la rareté mécanique.
- *H_B.* Tout le signal tient dans la rareté.
- *Métrique.* Gain d'aire sous la courbe ROC.
- *Contrôle négatif.* Les paires absurdes.
- *Ce qui falsifie H_A.* Aucun gain, ou des alertes plus fréquentes sur les absurdes.
- *Ce qui falsifie H_B.* Un gain significatif sans hausse des alertes sur les absurdes.

**D6, H7 face à l'attachement préférentiel.**
- *H_A.* À degré égal, les liens féconds tombent plus près des nœuds que ne le prédit l'attachement préférentiel.
- *H_B.* L'attachement préférentiel suffit.
- *Ce qui falsifie H_A.* Un résidu nul après contrôle du degré.
- *Ce qui falsifie H_B.* Un résidu positif dont l'intervalle de confiance exclut 0.

### Test sur les découvertes simultanées

Le modèle doit attribuer aux multiples, *avant* leur date, une probabilité d'apparition plus élevée qu'aux singletons appariés.

### Résultat qui réfute le modèle

D1 nul alors que la puissance avait été calculée d'avance pour l'effet minimal préenregistré. Dans ce cas, le modèle se réduit à $B_0$.

---

## 6. Ce que les hypothèses oublient

- **Les problèmes et les anomalies.** Une idée naît souvent d'une question ou d'un échec empirique, et pas d'une paire de concepts (Kuhn, 1962). Il faudrait modéliser des nœuds « problème ».
- **La faisabilité et le coût des tests.** Un lien peut être conçu tôt et testé tard : Ke, Ferrara, Radicchi & Flammini (2015), *Defining and identifying Sleeping Beauties in science*, *PNAS* 112. Il faudrait une variable de délai.
- **La reconnaissance sociale.**
  - L'effet Matthieu : Merton (1968), *Science* 159.
  - La relève des générations : Azoulay, Fons-Rosen & Graff Zivin (2019), *Does science advance one funeral at a time?*, *AER* 109.
  - Le biais contre la nouveauté : Wang et al. (2017).
  
  Ce que l'on observe comme « intéressant » est en fait intéressant **et** reconnu. Il faut modéliser la sélection.
- **Le savoir négatif et tacite.** Les corpus sont biaisés vers les succès par leur structure même.
- **Les stratégies des chercheurs.** Foster, Rzhetsky & Evans (2015), *Tradition and innovation in scientists' research strategies*, *American Sociological Review* 80. Rzhetsky, Foster, Foster & Evans (2015), *Choosing experiments to accelerate collective discovery*, *PNAS* 112. Le choix entre tradition et risque est endogène.
- **La direction du transfert.** H2 et a5 décrivent un transfert d'une source vers une cible, alors que $\Pi$ est symétrique. Il faudrait une version orientée.
- **La dérive des concepts.** Un lien « neuf » peut n'être qu'un renommage.

---

## 7. Une première expérience peu coûteuse, avec l'ancrage matériel (d)

**Cible.** D1 et D2 : le volet caché de H1, que je juge à la fois le plus central et inconnu.

### Protocole (HYPOTHÈSE ; dates et seuils illustratifs)

- **Domaine.** Le biomédical, parce que SemMedDB fournit déjà des relations typées.
- **Période.** $T=2005$, test sur 2006–2015.
- **Concepts.** Les concepts UMLS mentionnés avant 2005, au moins 50 fois. Filtrer sur la première mention évite la fuite par les concepts nés plus tard.
- **Variables.**
  - $D_u$ par word2vec sur les résumés antérieurs ou égaux à 2005.
  - $\Pi$ par le noyau de Weisfeiler-Lehman sur les voisinages SemMedDB antérieurs ou égaux à 2005, noms effacés, arêtes étiquetées par le type de prédicat.
  - $CN$ et degrés.
- **Échantillon.** Les paires du quintile supérieur de $D_u$, non liées en 2005.
  - Positives : une première prédication entre 2006 et 2015, réutilisée par au moins 2 groupes indépendants.
  - Négatives : échantillonnées à un ratio fixe, avec correction en conséquence.

### Prédiction de H1

Un gain d'AUC-PR de $B_1$ sur $B_0$ d'au moins 0,02, avec un intervalle de confiance qui exclut 0. Le gain obtenu avec $\Pi$ permuté doit rester sous 0,005 en valeur absolue.

### Lecture des issues

1. **$\Pi$ aide et le $\Pi$ permuté n'aide pas.** H1 survit à ce test, sans être prouvée : les types de SemMedDB peuvent encore porter de la surface.
2. **Les deux aident.** C'est un artefact de degré ou de fréquence. H1 n'est pas soutenue.
3. **Aucun gain, avec la puissance calculée d'avance.** H1 est réfutée dans ce domaine et sur cette fenêtre de temps.
4. **Gain sur les paires proches seulement.** Cela contredit l'interaction que H1 prédit.

### (d) Ancrage matériel (tout est illustratif, sauf les noms des ressources)

| Élément | Choix | Calcul et coût |
|---|---|---|
| Prétraitement, word2vec (gensim), noyau de Weisfeiler-Lehman | Processeur seul | 1 machine de 32 cœurs et 128 Go, 2 à 4 jours, moins de 300 € en cloud |
| Données | PubMed (libre). SemMedDB et UMLS sous licence gratuite avec inscription (RAPPORTÉ) | 0 € |
| Instruments à base de modèles de langage (D5, motif « anesthésie ») | Pythia (Biderman et al., 2023, ICML), choisi pour ses données publiques et ses checkpoints. OLMo (Groeneveld et al., 2024), choisi pour ses données ouvertes (Dolma), qui permettent de vérifier la contamination. Dates de coupure RAPPORTÉES, à vérifier. La période de test doit être postérieure à la coupure | 1 GPU de 24 à 80 Go, quelques heures pour environ 10⁵ énoncés, quelques dizaines d'euros |
| Préenregistrement | OSF, avant l'ouverture des années 2006–2015 | 0 € |

FIN-DE-CELLULE