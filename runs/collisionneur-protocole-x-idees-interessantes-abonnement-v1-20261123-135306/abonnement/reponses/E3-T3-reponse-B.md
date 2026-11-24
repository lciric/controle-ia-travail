# Proposition B, tour III.3 : réponse aux critiques

**Pièces.** Toutes les pièces sont présentes et vont jusqu'à leur ligne de fin, sans coupure visible : FAITS, QUESTION DE L'ARBITRE, ma conception III.1 et les critiques A, C, D, E. Le bloc QUESTION reproduit le bloc FAITS et porte la même empreinte déclarée, que je n'ai pas recalculée. Je traite donc (c) comme une réponse condensée à la tâche en sept parties.

**Statuts.**
- Ce que j'attribue aux critiques est OBSERVÉ-NON-AUDITÉ : c'est ma lecture des pièces.
- Je reprends leurs statuts tels quels. Plusieurs dérivations sont marquées VÉRIFIÉ par leurs auteurs. Je ne les ai pas refaites et je ne modifie pas ces statuts.
- Les références sont RAPPORTÉES, de mémoire.
- Mes verdicts et mes protocoles sont des HYPOTHÈSES.
- Tous les chiffres sont illustratifs.

**Règle B1.** Plusieurs critiques visent le même défaut. Je les range par défaut et je cite chaque source, sans fondre leurs arguments : je signale où ils diffèrent.

---

## (a) Verdict sur chaque critique

Les quatre critiques désignent en premier, chacune de son côté, le même défaut central (ligne 1). Je le reconnais : mon expérience III.1 n'aurait pas pu distinguer le volet caché de H1 d'une simple compatibilité de classes ontologiques.

| # | Critique (sources) | Verdict | Ce qui change |
|---|---|---|---|
| 1 | « Π indépendant de $D_u$ par construction » est faux. Effacer les noms sépare les *mesures*, pas les *variables*. Les prédicats de SemMedDB (TREATS, INHIBITS…) sont contraints par la classe UMLS, et la première itération de Weisfeiler-Lehman (WL) la reconstruit (A-a1, C-a1, D-a1, E-a1(i)). Si un effet de paire de classes existe, γ₁ n'est pas identifiable (D-b1) | **Acceptée.** Ma phrase était fausse | Je retire l'énoncé. Nouvelle base **B0+** : B0, plus des effets fixes par paire de groupes sémantiques UMLS, plus le cosinus des vecteurs de degrés typés (ce qu'est WL à h=1). L'objet de H1 devient $\Pi^{(h\ge2)}$ *au-delà de B0+*. Contrôle : recâblage typé à l'intérieur de chaque groupe sémantique, qui conserve le vecteur de degrés typés de chaque nœud (A-c2, C-c1, D-c1, E-c1) |
| 2 | $D_u$ et $S_t$ viennent du même corpus (E-a1(ii)). Sélectionner le quintile supérieur d'un $D_u$ bruité produit une régression vers la moyenne (A-a3) et sur-sélectionne les concepts rares (D-b1) | Acceptée | Je partage les PMID au hasard en deux moitiés : $D_u$ est calculé sur l'une, Π sur l'autre, ce qui coupe le bruit commun. Plus de troncature sur $D_u$. Seuil de fréquence exigé dans chaque moitié |
| 3 | Π et l'étiquette positive sortent du même extracteur, SemRep (A-a2). Le bruit d'extraction écrase Π aux forts degrés (A-b3) | Acceptée, transformée en test | Ajout d'une cible indépendante de l'extracteur : la co-indexation MeSH faite par des indexeurs humains (A-c3). Ajout d'une cible placebo, la co-mention sans prédication (A-c1). Une prédication n'est retenue que si elle est attestée par au moins 2 phrases distinctes |
| 4 | Fuite temporelle par une version récente d'UMLS et de scispaCy (C-a3, D-a4, E-a1, D-c3, E-c1(ii)) | Acceptée. J'ajoute que la fuite touche aussi $S_t$, puisque SemMedDB est produit avec un Métathésaurus récent (HYPOTHÈSE) | Version UMLS 2005 si la NLM la fournit (à vérifier). Dans tous les cas, analyse sur un sous-ensemble stable : identifiants CUI et synonymes inchangés depuis 2005 |
| 5 | WL dégénère : à h=1 il ne voit que l'histogramme des degrés typés ; à h≥2, soit aucun recouvrement, soit les hubs dominent, et Var(Π \| degrés typés) → 0 (C-b1). Le contrôle par permutation est sans effet quand l'entropie des types est faible (A-b2) | La moitié sur h=1 est acceptée. La moitié sur h≥2 est rejetée en partie et transformée en pré-contrôle | L'argument asymptotique de C-b1 porte sur l'étiquette de la racine. Or le noyau compare des histogrammes sur *tous* les nœuds du sous-graphe ego, et beaucoup sont de faible degré : rien n'impose que Π tende vers 0 ou vers 1 (HYPOTHÈSE). Le risque empirique reste réel, d'où deux pré-contrôles avant d'ouvrir les années de test : Var($\Pi^{(h\ge2)}$ \| B0+)/Var($\Pi^{(h\ge2)}$) ≥ 0,1, et une part du type dominant inférieure à 0,8 dans chaque groupe (seuils illustratifs) |
| 6 | Limites connues de 1-WL : il confond certains graphes réguliers non isomorphes (D-a1). Il est complet sur les arbres, donc ma calibration sur les arbres d'équations est vraie par construction (E-a2) | Acceptée | Je rapporte le taux de collision des classes WL. La calibration sur les arbres devient un contrôle positif de l'implémentation, plus un test |
| 7 | ΔAUC-PR dépend du ratio d'échantillonnage des négatifs, sa variance explose, et une borne rend le seuil de 0,02 inatteignable même pour un classifieur bayésien optimal (A-b1, A-b7, C-b2, D-b2, E-b1) | Acceptée | Critère principal : ΔAUC-ROC, invariant au tirage cas-témoins. S'y ajoute la déviance hors échantillon d'une régression logistique cas-témoins, où seul l'intercept est corrigé (Prentice & Pyke, 1979, *Logistic disease incidence models and case-control studies*, *Biometrika* 66). La précision sur les $k$ premiers, pondérée, passe en secondaire. Le nombre de positifs requis est simulé avant ouverture |
| 8 | Dépendance dyadique : le test de DeLong sans regroupement sous-estime la variance (E-b1, E-b5) | Acceptée | Bootstrap par grappes de nœuds, avec variance dyadique (Aronow, Samii & Assenova, 2015, *Cluster-robust variance estimation for dyadic data*, *Political Analysis*) |
| 9 | D2 : γ₂ n'est pas identifiable sur un échantillon tronqué. L'ajustement sur les paires proches n'est pas un contrôle. Le signe d'une interaction en logit dépend de la fonction de lien (A-a4, A-b4, C-b3, E-a3, E-b2, E-c3) | Acceptée | Interaction mesurée sans échelle : pente des ΔAUC-ROC calculés à l'intérieur de chaque décile de $D_u$. Le rang ne dépend d'aucune fonction de lien. L'étiquette « contrôle » est retirée |
| 10 | D3 : la version non conditionnée est vraie par construction et la version conditionnée conditionne sur un collisionneur (A-a5). σ agrège des effets opposés (C-a2) et plafonne F par la taille des communautés (D-a3, D-b3). σ est un régresseur estimé dont l'incertitude est ignorée (E-a4, E-b3). Le test des deux droites n'a pas de taille d'effet minimale (A-b5) | Acceptée. Une nuance sur C-a2 : l'agrégation *peut* fabriquer un U, elle ne le fait pas *mécaniquement*. Le point se tranche par simulation (A-c5, C-c2, E-c4) | D3 est retiré. Je le remplace par D3', une notation humaine sur des paires non sélectionnées. Le volet « fécondité » de H4 est déclaré non testable sans variable instrumentale |
| 11 | D4 : le contrôle par méthodes postérieures passe par définition, et les catalogues historiques n'ont pas de texte intégral (A-a6). M croît avec le volume d'activité (A-a6, D-a3, C-c3). Sous le nul, un bassin latent d'équipes donne un OR > 1 (D-b4, E-b4). La puissance ne vient que des paires discordantes (A-b6) | Acceptée | D4' : multiples modernes seulement, M normalisé, modèle nul biparti (D-c3), méthodes placebo appariées en fréquence et en croissance (A-c4, E-c5). Le confondant latent est déclaré comme résidu |
| 12 | D4 : le contrôle serait inversé par causalité inverse, car une découverte entraînerait l'adoption ultérieure des méthodes (E-a5) | Raison rejetée, conclusion acceptée | Dans ma définition, $a_{im}(t)$ est mesuré à $t$, *avant* la découverte (lecture de ma pièce, OBSERVÉ-NON-AUDITÉ) : une adoption postérieure n'y entre pas. C'est A qui a raison : le contrôle ne teste que la datation. Il est remplacé (ligne 11) |
| 13 | D5 : une période de test postérieure à la coupure de Pythia ou d'OLMo laisse F censuré (A-a9, E-a6, E-b5). Biais de fragmentation en sous-mots (E-c6) | Acceptée | Modèle entraîné de zéro sur les textes ≤ T, avec un modèle n-gramme en base. La cible devient la naissance du lien, plus F. Appariement sur le nombre de jetons |
| 14 | D6 n'a pas d'estimateur. F croît avec le nombre d'auteurs (A-a7, E-a6, E-b6) | Acceptée | D6 est retiré. F reçoit en décalage (offset) le logarithme du nombre de groupes actifs sur les deux concepts |
| 15 | Calibration 1 vraie par construction : le contexte reste inchangé et la vérification par la fréquence atteint son plafond (A-a8, D-a2, E-a2) | Acceptée | Chiffrement intégral du vocabulaire d'une moitié du corpus, contexte compris (D-c2, E-c2). Alignement non supervisé (Conneau, Lample, Ranzato, Denoyer & Jégou, 2018, *Word translation without parallel data*, ICLR) contre un appariement par rang de fréquence, qui n'est plus au plafond puisque les deux moitiés diffèrent |
| 16 | Calibration 4, l'« anesthésie » : couper l'attention annule par construction la jacobienne croisée (E-a2), et le critère R² est colinéaire à l'intervention (E-b6) | Acceptée | Retirée du programme. Sans étalon, aucun contraste peu coûteux ne la rend jugeable |
| 17 | D1 laisse une zone sans verdict : un gain entre 0 et 0,02 dont l'intervalle exclut 0 (A-a10) | Acceptée | Règle à quatre issues, chacune falsifiant quelque chose (voir (b)) |
| 18 | La partie 7 mêle la naissance d'un lien (production) et sa fécondité (E-a6) | Acceptée | Cible principale : la naissance attestée. Le critère « au moins 2 groupes » ne sert plus que de filtre de bruit et est présenté comme tel. F est analysé à part |
| 19 | La percolation n'est pas identifiable sous une loi de degrés à queue lourde (E-b6) | Acceptée | Abandonnée |

Bilan : aucune critique n'est rejetée en bloc. La moitié « h≥2 » de C-b1 est rejetée en partie et la raison de E-a5 est rejetée, dans les deux cas pour un motif que j'ai donné et sans changer la correction qui en découle.

---

## (b) Expériences corrigées (HYPOTHÈSES ; tous les seuils et effectifs sont illustratifs)

### E7' : volet caché de H1 en biomédical (prioritaire)

**Hypothèses opposées.**
- **H_A.** La similarité de rôle d'ordre ≥ 2, $\Pi^{(h\ge2)}$, prédit la naissance de liens au-delà de B0+ (classes, degrés typés, degrés, voisins communs, $D_u$, $D_c$).
- **H_B.** B0+ suffit.

**Données et variables.**
- **Corpus et découpage.** Résumés PubMed ≤ 2005, PMID partagés au hasard en deux moitiés P1 et P2. Concepts : identifiants CUI présents dans une version UMLS 2005 (disponibilité à vérifier) ou dans le sous-ensemble stable, mentionnés au moins 50 fois dans *chaque* moitié.
- **Distance de surface.** $D_u$ par word2vec sur P1 seulement.
- **Proximité cachée.** Π par noyau WL (h = 1, 2, 3, chaque niveau rapporté à part) sur les prédications SemMedDB de P2. Une prédication n'est retenue que si elle est attestée par au moins 2 phrases.
- **Cibles, sur 2006–2015.**
  - $T_A$ : première prédication, dans au moins 2 articles signés par des groupes d'auteurs disjoints.
  - $T_M$ : première co-indexation MeSH des deux concepts comme sujets majeurs, faite par des indexeurs humains (RAPPORTÉ ; le passage à l'indexation automatique serait postérieur à la fenêtre, à vérifier).
  - $T_0$ (placebo) : co-mention sans prédication.
- **Échantillon.** Toutes les paires non liées en 2005, sans troncature sur $D_u$. Négatifs tirés au ratio $r$, stratifiés par décile de $D_u$. Logistique avec correction de l'intercept.
- **Contrôles.**
  - $\Pi$ recalculé sur $S_t$ recâblé à l'intérieur de chaque groupe sémantique, vecteurs de degrés typés conservés.
  - $\Pi^{(h=1)}$ seul, qui fait partie de B0+.
  - La cible placebo $T_0$.
  - Simulation sous B0+ pour vérifier qu'aucun gain n'apparaît par construction.

**Pré-contrôles (go/no-go), avant d'ouvrir 2006–2015.**
1. Var($\Pi^{(h\ge2)}$ \| B0+)/Var($\Pi^{(h\ge2)}$) ≥ 0,1.
2. Part du type de prédicat dominant inférieure à 0,8 dans chaque groupe.
3. Nombre de positifs suffisant, par simulation, pour une demi-largeur d'intervalle ≤ δ/2.

Un échec est publié comme « instrument non jugeable dans ce domaine ». Il falsifie la faisabilité du test, pas H1. C'est déjà un résultat : si (1) échoue, la « structure cachée » des graphes biomédicaux typés n'est rien d'autre que la classe des concepts.

**Critère.** ΔAUC-ROC de (B0+ + $\Pi^{(h\ge2)}$) sur B0+, avec δ = 0,01 préenregistré, un intervalle de confiance (IC) à 95 % par bootstrap dyadique et la déviance hors échantillon en concordance.

**Règle de décision, examinée dans cet ordre.**
1. **Gain > δ, mais aussi avec Π recâblé, ou sur $T_A$ seulement, ou au même niveau sur le placebo $T_0$.** Cela falsifie l'instrument : Π mesure la classe, l'extractibilité ou l'activité. H1 n'est pas soutenue.
2. **Borne basse de l'IC > δ sur $T_A$ et sur $T_M$, avec un contrôle recâblé dont l'IC contient 0.** Cela falsifie H_B. H1 survit dans ce domaine, sans être prouvée.
3. **Borne haute de l'IC < δ sur $T_A$ et sur $T_M$.** Cela falsifie H_A pour ce domaine et cette fenêtre (test d'équivalence).
4. **IC à cheval sur δ.** Cela falsifie l'hypothèse de variance du calcul de puissance. Aucun verdict sur H1, et c'est publié comme tel.

**D2' (interaction de H1), sur les mêmes données.**
- *Mesure.* Pente, à travers les déciles de $D_u$, du ΔAUC-ROC calculé dans chaque décile.
- *H_A.* La pente est > 0 et son IC exclut 0.
- *H_B.* La borne haute de l'IC est sous une pente minimale préenregistrée.
- Si $\Pi$ n'aide que dans les déciles proches, l'interaction prédite par H1 est contredite.

**Coût.** Une machine de 32 cœurs, 2 à 4 jours, moins de 300 € (illustratif). PubMed est en accès libre. SemMedDB et UMLS demandent une licence gratuite (RAPPORTÉ). Préenregistrement sur OSF.

### D3' : H4 sous l'angle de l'intérêt, sans biais du survivant

- **Paires.** Tirées dans le graphe *actuel*, uniformément par décile de $D_u$ × tercile de Π, sans condition sur la formation d'un lien. Le jugement porte donc sur les croyances présentes, au sens de Davis, et l'issue n'est encore connue de personne.
- **Notation.** Des experts notent en aveugle la plausibilité et l'intérêt, séparément. On leur demande s'ils reconnaissent la paire, on exclut celles qui sont reconnues, et on rapporte la concordance entre juges (ICC).
- **H_A.** L'intérêt suit un U inversé en $D_u$ : deux droites de pentes opposées, chacune d'au moins $b_{min}$ en valeur absolue.
- **H_B.** L'intérêt est monotone en $D_u$.
- **Lecture des issues.** Une seule pente ≥ $b_{min}$ falsifie H_A. Deux pentes opposées falsifient H_B. Aucune pente ≥ $b_{min}$ falsifie l'hypothèse de puissance.
- **Prédiction secondaire de H1.** À $D_u$ fixé, la plausibilité croît avec Π.
- **Suivi.** La formation des liens est relevée à 5 ans, selon un protocole gelé.

### D4' : H5 sur des multiples modernes

- **Multiples.** Première attestation d'un lien par au moins 2 groupes d'auteurs disjoints en moins de 12 mois, sans aucun critère de co-citation future.
- **Singletons.** Première attestation par un seul groupe.
- **Variable.** $M$ normalisé par $\sqrt{\sum_m a_{im}\sum_m a_{jm}}$, comparé à sa loi sous un recâblage biparti qui conserve le nombre d'adoptions de chaque concept. Covariable : logarithme de l'activité de chaque concept.
- **Contrôle.** Des méthodes placebo appariées en fréquence et en croissance.
- **H_A.** Pour les multiples, $M$ dépasse le nul et le placebo.
- **H_B.** Aucun excès.
- **Troisième issue.** Un excès identique avec le placebo falsifie l'instrument : $M$ ne mesure alors que l'activité.
- **Résidu déclaré.** Le bassin latent d'équipes (D-b4) n'est pas observé.

### D5' : H10 face à la rareté

- **Modèles.** Un petit modèle de langage entraîné de zéro sur les textes ≤ T, et un modèle n-gramme en base.
- **Cible.** La naissance du lien, pas F.
- **Appariement.** Sur la rareté et le nombre de jetons.
- **Contrôle.** Des paires absurdes.
- **H_A.** La surprisal apporte un gain d'AUC-ROC au-delà de la rareté, sans plus d'alertes sur les paires absurdes.
- **H_B.** La rareté suffit.

**Retirés du programme :** D3 dans sa forme initiale, D6, le motif « anesthésie » et la percolation.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi
Tout ce qui suit est RAPPORTÉ, de mémoire, et n'a pas été vérifié pendant cette session.
- **L'intérêt est une relation entre une idée et un public.** Une thèse paraît intéressante quand elle nie une croyance tenue pour acquise (Davis, 1971).
- **Les combinaisons atypiques posées sur un noyau conventionnel vont de pair avec l'impact** (Uzzi et al., 2013). La recombinaison lointaine augmente surtout la *variance* des résultats (Fleming, 2001), et la nouveauté est reconnue plus tard (Wang, Veugelers & Stephan, 2017). H4 tient donc sous la forme « variance », pas sous la forme « optimum ».
- **Les chaînes A–B–C produisent des hypothèses** (Swanson, 1986), mais leur taux de succès est mal mesuré. H2 est établie comme heuristique.
- **Les découvertes multiples existent** (Merton, 1961). Leur distribution serait compatible avec un modèle de hasard (Simonton, 1979, détail à vérifier).
- **L'analogie repose sur un appariement de structure** (Gentner, 1983). Le transfert spontané entre analogues éloignés est rare (Gick & Holyoak, 1980).
- **Tomber près des nœuds est le comportement attendu de l'attachement préférentiel** (Price, 1965 ; Barabási & Albert, 1999). H7 se confond en grande partie avec lui.
- **Des plongements datés portent un savoir latent prédictif** (Tshitoyan et al., 2019), mais ils mesurent la proximité d'usage, c'est-à-dire la surface.

### Ce qui ne l'est pas (HYPOTHÈSES)
- **Le volet caché de H1** : une proximité structurelle qui prédirait la viabilité d'un mariage au-delà de la classe ontologique et du profil de rôle. Ce tour montre que mon protocole III.1 ne pouvait pas le distinguer d'une compatibilité de classes. C'est le constat convergent des quatre critiques (OBSERVÉ-NON-AUDITÉ), et je l'accepte. H1 n'a donc pas encore été testée, pas même en principe.
- **H5** comme cause commune des multiples. Le test est faible par nature, parce que le volume d'activité confond le signal.
- **H4**, côté intérêt : non testée. Côté fécondité : non testable sans variable instrumentale.
- **H6, H10 au-delà de la rareté, le motif « anesthésie »** et les métaphores physiques (Noether, ferromagnétisme, puits, résonance, percolation) : soit aucun contenu mesurable, soit aucun instrument validé.

### L'expérience à faire en premier : E7'
- **Pourquoi elle.** Elle vise l'hypothèse la plus centrale et la plus inconnue, avec des données gratuites, pour quelques jours de calcul et moins de 300 € (illustratif).
- **Ce qu'elle tranche avant tout résultat.** Son pré-contrôle dit déjà si une structure d'ordre ≥ 2 existe au-delà de la classe des concepts.
- **Prédiction de H1.** Un ΔAUC-ROC sur B0+ dont la borne basse dépasse δ = 0,01 (illustratif), sur la cible SemRep et sur la cible MeSH indépendante de l'extracteur, avec un contrôle recâblé nul.
- **Lecture.**
  - *Gain aussi avec le contrôle recâblé, ou sur une seule cible, ou sur le placebo* : l'instrument mesure la classe, l'extractibilité ou l'activité, et H1 n'est pas soutenue.
  - *Borne haute sous δ* : H1 est réfutée dans ce domaine et sur cette fenêtre, et B0+ suffit.
  - *Intervalle à cheval sur δ* : le calcul de puissance est faux, et c'est publié sans verdict.

FIN-DE-CELLULE