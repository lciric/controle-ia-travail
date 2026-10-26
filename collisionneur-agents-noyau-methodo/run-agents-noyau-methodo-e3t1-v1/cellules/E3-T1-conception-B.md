# Proposition B — Tour III.1 : conception à l'aveugle

**Pièces.**
- Le bloc FAITS est vide par décision de l'arbitre, ce que le bloc lui-même consigne. Rien n'y est donc invoqué.
- Les propositions A et C ne me sont pas visibles à ce tour. B1 s'applique donc à la question elle-même, que j'attaque là où elle présuppose.
- La « règle R-468 » est citée sans contenu. Je n'en suppose rien.

**Statuts employés.**
- RAPPORTÉ : énoncé par la question, non audité.
- VÉRIFIÉ : seulement pour une arithmétique que j'ai refaite ici.
- HYPOTHÈSE : tout le reste.

Tout chiffre de ma main sans dérivation est « illustratif ».

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| a1 | Le cadre : $\mathcal{O}$, un hôte fixe, 6 rondes de conception + 4 itérations, 60 items par part, ≥ 96 en confirmation. | RAPPORTÉ | Non audité. « 60 items par part (36 et 24 par famille) » est ambigu : les parts sont-elles train/val/final ? val/final ? Les 36/24 sont-ils par famille ou par classe ? Tout calcul de puissance en dépend. |
| a2 | L'erreur type vaut ≈ 0,07 sur 36 items et ≈ 0,09 sur 24. | VÉRIFIÉ (arithmétique : $\sqrt{0{,}1875/36}=0{,}072$ ; $\sqrt{0{,}1875/24}=0{,}088$) | Le calcul suppose des items i.i.d. Bernoulli de même probabilité 0,75, ce qui est une HYPOTHÈSE. Des items de difficulté hétérogène et un déséquilibre des classes changent l'erreur type. |
| a3 | « Un écart < 0,2 reste dans le bruit. » | HYPOTHÈSE | Le seuil vaut $1{,}96\cdot\sqrt2\cdot0{,}072\approx0{,}20$, ce qui suppose **deux échantillons indépendants**. Or deux variantes notées sur les **mêmes** items sont appariées. L'erreur type de la différence est alors $\approx\sqrt{p_d/n}$, où $p_d$ est la fraction d'items discordants. Avec $p_d=0{,}2$ (illustratif), elle vaut 0,075 et le seuil tombe à ≈ 0,15. Le seuil de 0,2 est donc trop prudent pour l'item et ignore la variance d'exécution. |
| a4 | « Variance entre graines » désigne une seule quantité. | HYPOTHÈSE | Il y a **au moins trois niveaux** : (i) les items ; (ii) la stochasticité d'évaluation, à code de $\mathcal{O}$ fixé (appels aux modèles) ; (iii) la **trajectoire de conception**, puisque le code de $\mathcal{O}$ est réécrit par des modèles et que deux exécutions « identiques » produisent deux programmes différents. La question de fond (une complexité ajoutée aide-t-elle ?) porte sur le niveau (iii), le plus coûteux à mesurer. |
| a5 | « Complexité ajoutée » est un facteur unique. | HYPOTHÈSE | Les agents outillés regroupent plusieurs facteurs : nombre de pas, exécution de code, recherche et **budget de calcul**. Un gain peut venir du seul calcul supplémentaire. |
| a6 | Les quatre manières sont commensurables. | HYPOTHÈSE | Seule (1) change **l'objet étudié**. (2) et (3) changent la **fiabilité de l'instrument**. (4) **est** la boucle adaptative, donc la source du surapprentissage. Les comparer sur un même axe mélange l'objet et la mesure. |
| a7 | Le relecteur indépendant détecte les défauts. | HYPOTHÈSE | Aucun taux de détection n'est connu (voir c1). |
| a8 | Un Thresholdout est utile à n = 60. | HYPOTHÈSE, probablement fausse au sens des garanties | Voir (b) E3. À n = 60, une borne uniforme de Hoeffding sur 20 lectures non adaptatives vaut déjà ±0,24. Les garanties formelles sont vides ; seul un effet empirique reste possible. |
| a9 | « $D_{\mathrm{final}}$ n'est jamais rendu à $\mathcal{O}$ » protège $D_{\mathrm{final}}$. | HYPOTHÈSE | La règle protège contre $\mathcal{O}$, pas contre les **concepteurs**. Si les humains ou les modèles concepteurs lisent les scores sur $D_{\mathrm{final}}$ entre deux exécutions, $D_{\mathrm{final}}$ devient un second jeu de validation adaptatif. La question ne dit pas qui lit quoi. |
| a10 | Le jeu de confirmation est « neuf ». | HYPOTHÈSE | Cela exige un contrôle mécanique de non-recouvrement (hachages, quasi-doublons), absent du cadre. |
| a11 | Déclarer qu'on a lu les scores borne la contamination. | HYPOTHÈSE | Une déclaration n'est pas une borne. Voir E4 pour ce qui est réellement bornable. |
| a12 | Les bornes de l'hôte (temps, coût, recherches) suffisent à rendre le coût fini et l'exécution reproductible. | HYPOTHÈSE | La recherche sur un index vivant n'est pas reproductible, même sous borne. |
| a13 | L'exactitude est la bonne métrique. | HYPOTHÈSE | Les taux de base des classes ne sont pas donnés. Sur 24 items, un classifieur majoritaire peut atteindre 0,75 (illustratif). |
| a14 | La famille tenue à l'écart mesure la même chose que la confirmation. | HYPOTHÈSE | Elle confond « gain de la variante » et « transfert à une famille nouvelle ». La confirmation doit aussi couvrir une famille connue. |

---

## (b) Expériences décisives (duels H_A / H_B)

### Modèle commun

Pour l'item $i$, la variante $j$ et l'exécution $r$ (graine, trajectoire comprise) :

$$\operatorname{logit}\Pr(Y_{ijr}=1)=\mu+\beta_j+a_i+(ab)_{ij}+c_{jr},\quad a_i\sim\mathcal N(0,\sigma_a^2),\ c_{jr}\sim\mathcal N(0,\sigma_c^2).$$

Sur l'échelle des exactitudes, pour une différence appariée moyennée sur $R$ exécutions par bras :

$$\operatorname{Var}(\hat\Delta)\approx\frac{s^2_{\text{item}}}{n}+\frac{2\,\sigma^2_{\text{run}}}{R},$$

où $s^2_{\text{item}}\approx p_d$.

**Conséquence centrale.** Répéter les graines réduit le second terme, **jamais le premier**.
- Exemple : à n = 96 et $p_d=0{,}25$ (illustratif), le plancher dû aux items est $\sqrt{0{,}25/96}\approx0{,}051$.
- Ce plancher vaut pour toute inférence portant sur la population d'items.
- Si l'estimand est « sur ces 96 items-là », seules les répétitions comptent. Il faut choisir l'estimand avant l'expérience.

### E1 — Le bruit d'exécution est-il négligeable ? (test A/A)

- **H_A :** $\sigma_{\text{run}}$ est petit devant le bruit d'item ($\sigma_{\text{run}}<0{,}03$, illustratif). Une exécution par variante suffit alors, à l'erreur binomiale près.
- **H_B :** $\sigma_{\text{run}}\ge$ le bruit binomial ($\ge0{,}07$ sur 36 items). Une exécution unique ne permet de conclure sur rien.
- **Dessin :** une configuration de $\mathcal{O}$ fixée, deux régimes, $R=8$ exécutions chacun (illustratif) :
  - **R-éval** : code de $\mathcal{O}$ figé, seule l'évaluation est rejouée. Cela mesure le niveau (ii).
  - **R-traj** : conception complète relancée. Cela mesure le niveau (iii).
- **Métrique :** $\hat\sigma_{\text{run}}$ estimé par un modèle mixte ou par une ANOVA à deux facteurs item × exécution. L'intervalle se calcule par bootstrap à deux voies (items et exécutions rééchantillonnés ensemble).
- **Contrôle négatif :** hôte rendu déterministe (température 0 et réponses en cache rejouées). On doit observer $\hat\sigma_{\text{run}}\approx0$. Sinon, une non-déterminisme caché existe dans l'hôte, et E1 n'est pas interprétable.
- **Falsification :**
  - H_A est falsifiée si la borne inférieure de l'IC à 95 % de $\sigma_{\text{run}}$ (R-traj) dépasse 0,03.
  - H_B est falsifiée si la borne supérieure reste sous 0,07.
  - Entre les deux, l'issue est indécidable : on le consigne et on augmente $R$.
- **Mise en garde :** avec $R=8$, l'IC sur un écart-type est large. Un rapport max/min d'environ 2 est plausible (illustratif). E1 tranche les cas tranchés, pas les cas limites.

### E2 — La complexité apporte-t-elle un gain au-delà du bruit et du calcul ?

- **Bras :**
  - (S) appels simples ;
  - (S+) appels simples à **calcul apparié** (vote majoritaire sur k appels, k choisi pour égaler le coût médian du bras agent) ;
  - (A) agents outillés.
- **Contraste primaire :** A contre S+. A contre S est secondaire, car il confond capacité et budget.
- **H_A :** $\Delta_{A-S+}\ge m$.
- **H_B :** $|\Delta_{A-S+}|<m$, testée par **équivalence (TOST)**. Ainsi chaque issue falsifie l'une des deux, ce que le seul « non significatif » ne fait pas.
- **Où :** jeu de confirmation (≥ 96 items), plan scellé, $R=6$ exécutions par bras (illustratif), intervalles appariés par item.
- **Seuil :** la marge $m$ doit être atteignable.
  - Avec un plancher de 0,051 dû aux items, la demi-largeur de l'IC à 90 % est ≈ 0,084 hors terme d'exécution.
  - $m<0{,}1$ rend l'équivalence pratiquement inatteignable à n = 96.
  - Je propose $m=0{,}10$ en équivalence et un seuil de supériorité ≈ 0,14 pour une puissance d'environ 80 % ($2{,}8\times0{,}051$). Tout est illustratif tant que $p_d$ n'est pas mesuré.
- **Contrôles :**
  - Contrôle négatif : bras A dont les outils sont désactivés (même boucle, outils renvoyant une erreur). Il doit rejoindre S+ ; sinon, le « gain » vient de la boucle ou du prompt, pas des outils.
  - Références : classifieur majoritaire, classifieur lexical trivial (longueur, mots-clés), S.
- **Falsification :**
  - H_A est falsifiée si l'IC à 90 % est contenu dans $(-m,m)$.
  - H_B est falsifiée si la borne inférieure de l'IC à 95 % dépasse $m$.
  - Si l'IC chevauche $m$, la conclusion est « non tranché à cette taille ». C'est un résultat, pas un échec.
- **Ce qui reste invisible :** un gain réel de 0,05. Le voir demanderait un plancher ≈ 0,025, donc $n\approx0{,}25/0{,}025^2=400$ items (illustratif, dépend de $p_d$).

### E3 — La réutilisation des 60 items gonfle-t-elle les scores, et quel garde-fou réduit ce gonflement ?

- **Deux boucles adaptatives :**
  - interne : $\mathcal{O}$ lit 4 scores par exécution ;
  - externe : les concepteurs lisent les scores entre exécutions.
- **Mesure de l'optimisme :** $O=\text{score}_{\text{val}}(\text{retenue})-\text{score}_{\text{frais}}(\text{retenue})$.
- **H_A :** l'optimisme sous sélection adaptative ne dépasse pas celui d'une sélection non adaptative. La réutilisation est inoffensive à cette échelle.
- **H_B :** l'optimisme croît avec le nombre de lectures $k$.
- **Dessin peu coûteux :** on conserve les prédictions par item de toutes les variantes déjà exécutées, puis on **rejoue hors ligne** des politiques de sélection sur des rééchantillons val/frais. Il n'y a presque aucun appel de modèle.
- **Politiques comparées :**
  - (P0) lecture brute ;
  - (P1) arrondi au pas de 0,1 ;
  - (P2) règle de type Ladder : publication seulement si le gain dépasse un pas $\eta$ ;
  - (P3) Thresholdout : réponse « estimation d'entraînement » sauf si l'écart avec la validation dépasse $T$ plus un bruit de Laplace ;
  - (P4) budget de $k$ lectures, puis arrêt.
- **Contrôle positif :** variantes nulles (A/A, mêmes codes, graines différentes) sélectionnées sur la validation. L'optimisme y est pure malédiction du vainqueur et doit être > 0. Sinon, la mesure est aveugle.
- **Contrôle négatif :** sélection tirée à pile ou face. L'optimisme attendu est 0.
- **Falsification :**
  - H_A est falsifiée si l'optimisme de P0 dépasse celui du tirage aléatoire au-delà de son IC bootstrap.
  - H_B est falsifiée si la pente optimisme/$k$ a un IC qui contient 0 et une borne supérieure inférieure à 0,02 par lecture (illustratif).
- **Duel secondaire, par garde-fou :** P_x réduit-il l'optimisme par rapport à P0 **sans** réduire la probabilité de retenir la meilleure variante réelle, mesurée sur le frais ? Un garde-fou qui ne fait que geler la sélection « gagne » trivialement. Le second critère l'interdit.
- **Pourquoi les garanties formelles sont vides ici :** pour $k$ requêtes non adaptatives, la déviation uniforme de Hoeffding est $\sqrt{\ln(2k/\beta)/(2n)}$. Avec $k=20$, $\beta=0{,}05$ et $n=60$, cela donne $\sqrt{6{,}68/120}\approx0{,}24$ (VÉRIFIÉ, arithmétique). Le cas adaptatif est pire. Toute protection sur 60 items est donc **empirique**, à mesurer par E3, jamais garantie.

### E4 — Lire les scores de conception contamine-t-il la confirmation ?

- **Distinction préalable :** sur données fraîches, avec un plan scellé et **une** hypothèse primaire, le risque α reste valide conditionnellement à la sélection. La lecture biaise **le choix** de l'hypothèse et **l'estimation de l'effet** (malédiction du vainqueur), pas le test. C'est un raisonnement standard ; il reste une HYPOTHÈSE pour son application ici, car il exige trois conditions vérifiables mécaniquement :
  1. aucun recouvrement d'items ;
  2. plan haché et horodaté avant tout accès aux données de confirmation ;
  3. multiplicité déclarée et corrigée (Holm).
- **H_A :** les effets estimés en conception sont fiables, avec un rapport de rétrécissement $\rho=\hat\Delta_{\text{conf}}/\hat\Delta_{\text{conception}}\ge0{,}8$.
- **H_B :** ils sont fortement gonflés, avec $\rho\le0{,}5$ (seuils illustratifs).
- **Dessin :** deux plans scellés concurrents.
  - Plan « informé » : auteurs ayant lu les scores.
  - Plan « aveugle » : un tiers qui n'a vu que le journal expurgé des scores et choisit la variante à confirmer selon un critère a priori, par exemple la plus simple qui passe les essais de l'hôte.
  - Les deux sont exécutés sur la confirmation.
- **Contrôle négatif :** une variante confirmée identique dans les deux plans doit donner le même $\hat\Delta$ à la variance d'exécution près.
- **Falsification :** l'IC de $\rho$ (bootstrap sur items et exécutions) tranche entre H_A et H_B. Si le plan aveugle fait aussi bien que le plan informé, la lecture des scores n'a rien apporté. Cela falsifie l'utilité, et non la validité, de la conception adaptative.

---

## (c) Instruments : mesure minimale de leur fonctionnement

**Principe commun.**
- Pour chaque instrument, on plante des défauts dans des cas et on garde des **jumeaux honnêtes** : même diff, même longueur, sans le défaut.
- L'instrument est valide s'il bat une vérification mécanique peu coûteuse en détection, à fausses alertes égales.
- Avec 20 paires, l'IC à 95 % sur un taux est d'environ ±0,2 (approximation de Wilson, illustratif). Les seuils ci-dessous ne valent qu'à l'ordre de grandeur.

| # | Instrument (nommé dans la question) | Défauts plantés / jumeaux honnêtes | Métrique, seuil (illustratif) | Vérification mécanique à battre |
|---|---|---|---|---|
| c1 | Relecteur indépendant des textes et du code | Fuite d'étiquette dans les features ; lecture d'un chemin $D_{\mathrm{final}}$ ; scoreur décalé d'un item ; graine figée cachée ; boucle d'appels non bornée | Détection ≥ 0,8, fausses alertes ≤ 0,1, sur 20 + 20 | Analyse statique (chaînes de chemins, appels réseau), tests unitaires du scoreur, **canari** |
| c2 | Relecteurs qui **refont et éprouvent** les essais de l'hôte, manière (3) | Configuration non déterministe insérée ; version de modèle changée en douce ; cache périmé | Détection de non-reproductibilité ≥ 0,8 ; fausses alertes sur reruns honnêtes ≤ 0,1 | Comparaison automatique des hachages de sorties sur rejeu déterministe |
| c3 | Essai réel court payant, manière (2) | Identifiant de modèle erroné ; limite de débit ; troncature au plafond de jetons ; prix réel différent du prix configuré ; format de réponse changé | Pannes visibles seulement en réel, détectées ≥ 0,9 ; fausses alertes (erreurs transitoires) ≤ 0,05 après une relance | Validation de schéma de configuration et simulateur rejouant des **codes d'erreur réels enregistrés**. Si le simulateur enrichi attrape tout, (2) n'apporte rien : c'est le duel. |
| c4 | Essais en simulation de l'hôte | Mêmes défauts que c3 | Recouvrement : fraction des pannes réelles historiques reproduites | Journal des pannes réelles passées |
| c5 | Thresholdout / arrondi / budget de lectures | Variantes **mémorisantes** (table hachage → étiquette des items de validation) contre jumelles honnêtes | Optimisme rapporté ≥ 0,15 de moins que sous P0 pour les mémorisantes ; perte ≤ 0,02 pour les honnêtes | P0 suivi d'un contrôle sur un petit jeu frais, et borne de Hoeffding/Bonferroni brute |
| c6 | Réserve intouchée | Accès simulés à la réserve (lecture directe, copie, inférence par erreur temporelle) | Toute lecture détectée (1,0), aucune fausse alerte | Permissions système, journal d'accès, empreintes hachées vérifiées avant et après |
| c7 | Journal de tous les essais | Exécutions retirées du journal (échecs omis) | Omissions détectées ≥ 0,95 | **Rapprochement avec la facturation de l'API** et les journaux de l'hôte |
| c8 | Boucle exécuter-lire-corriger-relancer, manière (4) | Variantes nulles (A/A) soumises à la boucle | **Taux de fausses découvertes** : fraction d'« améliorations » retenues entre variantes identiques ≤ 0,05 | Règle mécanique : n'accepter que si la borne inférieure de l'IC apparié > 0 avec R ≥ 3 |
| c9 | Bac à sable des agents (question 4) | Canari dans un faux $D_{\mathrm{final}}$ monté en leurre ; prompt induisant une boucle infinie ; requête de recherche visant le jeu public | Canari jamais présent dans les sorties ni les journaux (1,0) ; plafond de coût jamais dépassé | Filtrage réseau sortant, recherche de chaîne canari dans tous les journaux, plafond dur de facturation |
| c10 | Classifieur trivial de référence | Ce n'est pas un détecteur | Doit être calculé sur **les mêmes items** et rapporté avec chaque score | — |

**Mesure de c8, peut-être la plus révélatrice.** Si la boucle (4) « trouve » des améliorations entre variantes identiques plus de 5 fois sur 100, toute amélioration de conception non répétée doit être tenue pour non probante. Ce constat se tranche avant toute dépense agentique.

---

## (d) Ancrage matériel (tout est illustratif ; rien ne vient des faits)

**Modèles ouverts.**
- Familles disponibles à ma connaissance : Llama 3.1 Instruct (8B, 70B), Qwen2.5 Instruct et Qwen2.5-Coder (7B, 72B), Mistral 7B Instruct.
- En octobre 2026, des versions plus récentes existent probablement : à remplacer.
- Héberger soi-même un modèle ouvert est la seule façon d'obtenir un rejeu déterministe vérifiable (contrôle négatif de E1). Une API fermée peut changer de version sans préavis, ce qui ouvre un canal de non-reproductibilité (HYPOTHÈSE).

**Bac à sable.**
- Conteneur sans réseau, avec un noyau isolé (de type gVisor) et un système de fichiers où $D_{\mathrm{final}}$ **n'est pas monté**.
- Recherche servie par un index local figé (BM25 sur instantané daté) plutôt que par le web vivant.

**Ordre de grandeur des jetons (illustratif).**
- Exécution à appels simples : 60 items × 4 itérations × ~1k jetons ≈ 0,24 M, plus ~0,1 M de réécriture de code, soit **≈ 0,35 M**.
- Exécution agentique : ×10 (illustratif), soit **≈ 3,5 M**.

**Nombre d'exécutions.**

| Expérience | Exécutions | Jetons |
|---|---|---|
| E1 (2 régimes × 8, simple et agent) | 32 | ~60 M |
| E2 (3 bras × 6 sur ≥ 96 items, ×1,6 en jetons) | 18 | ~45 M |
| E3 (rejeu hors ligne) | ≈ 0 | ≈ 0 |
| E4 (2 plans × 6) | 12 | ~25 M |
| c1–c9 (essais plantés, surtout hors modèle) | — | ~5 M |
| **Total** | | **~135 M** |

**Coût.**
- Auto-hébergé, modèle 7–8B en inférence groupée à ~1 500 jetons/s : ≈ 25 h-GPU.
- Avec un modèle 70B : ×8 à ×10.
- Via API à 0,5–10 $/M jetons : de 70 $ à 1 400 $.
- Toutes ces valeurs sont illustratives.
- Le poste dominant est le niveau (iii) de E1 (trajectoires complètes). C'est aussi le seul qui répond à la question de fond.

---

## Réponses aux six points

### 1. Les quatre manières

| Manière | Apport à la question de fond | Coût | Risque principal | Ce qui manque |
|---|---|---|---|---|
| (1) Agents outillés | **Seule** à tester la complexité, mais confondue avec le calcul | Le plus élevé, variance de coût large | Fuite vers $D_{\mathrm{final}}$, coût non borné, non-reproductibilité | Bras à calcul apparié (E2), canari (c9) |
| (2) Essai réel court | Aucun direct ; protège l'instrument | Faible par essai, récurrent | Faux sentiment de sécurité ; un essai « vert » sur 3 items ne dit rien du score | Taux de pannes réelles non simulables (c3) |
| (3) Relecteurs qui refont | Aucun direct ; reproductibilité | Gratuit en dépense, pas en attention | Relecture complaisante, détection inconnue | c1, c2 |
| (4) Exécuter-corriger-relancer | **Négatif par défaut** : c'est le moteur du surapprentissage | Faible par tour, cumulatif | Poursuite du bruit | FDR mesuré (c8), budget de lectures |

**Ordre proposé (une voie parmi d'autres) :**
1. (3) et les vérifications mécaniques.
2. E1 sur appels simples.
3. (2), seulement si c4 montre des pannes réelles non simulables.
4. (1) sous dessin factoriel.
5. (4) seulement dans un budget journalisé.

**Combinaison** recommandée : (3)+(2) avant toute exécution de (1).

### 2. Une conception itérative qui reste de la science

- **Journal à ajout seul** : haché, chaque exécution horodatée, échecs compris, rapproché de la facturation (c7).
- **Plan factoriel fractionnaire plutôt qu'un facteur à la fois.**
  - Facteurs : pas multiples (oui/non), exécution de code (oui/non), recherche (oui/non), budget (bas/haut). Un $2^{4-1}$ fait 8 cellules.
  - Chaque exécution informe plusieurs effets principaux, au prix de confondre les interactions d'ordre 3. Le confondement est déclaré.
  - Un facteur à la fois coûte plus cher et ignore les interactions entre outils.
- **Analyse adaptative :**
  - budget de $k\le10$ lectures de $D_{\mathrm{val}}$ par concepteur avant confirmation (illustratif) ;
  - scores rendus arrondis à 0,1 ;
  - P2 ou P3 seulement si E3 montre un gain.
- **Réserve intouchée :** à 60 items, la découper encore la rend inutilisable. La vraie réserve est le jeu de confirmation, scellé jusqu'au plan.
- **Règle d'arrêt (illustratif).** On arrête la conception dès que l'une des trois conditions est remplie :
  - le budget de lectures est épuisé ;
  - une variante bat S+ avec une borne inférieure appariée > 0 sur R = 3 ;
  - trois variantes consécutives ont un IC apparié contenant 0 et une borne supérieure < $m$ (futilité).
- **Contamination :** bornée sur α par les conditions 1 à 3 de E4 ; non bornée sur l'estimation de l'effet, qu'on mesure par $\rho$.

### 3. Séparer du bruit

- **Une exécution par variante** permet seulement d'écarter les variantes cassées, c'est-à-dire sous le classifieur trivial au-delà de 2 erreurs types d'item. Elle ne permet de classer aucune paire de variantes tant que $\sigma_{\text{run}}$ est inconnu.
- **Minimum : R ≥ 3 par variante comparée.** C'est le plus petit nombre qui donne une estimation de la variance, très instable (illustratif). R ≈ 8 vaut une fois, dans E1.
- **Références obligatoires** : majorité, lexical, S.
- **Invisible sans répétition :**
  - le niveau (iii), dont deux programmes nés de la même consigne ;
  - l'interaction variante × graine ;
  - la non-déterminisme de l'hôte.

### 4. Agents servis par l'hôte

**Dessin minimal :**
- au plus N pas (N = 8, illustratif) ;
- exécution de code dans le bac à sable c9, **sans recherche au premier étage** ;
- plafond dur de jetons, de temps et de dollars, appliqué par l'hôte et non par l'agent ;
- transcription complète hachée ;
- seconde étape : recherche sur l'index figé, jamais le web vivant tant que les items pourraient être publics (canal de contamination, HYPOTHÈSE).

**Essais de l'hôte préalables :**
- canari (c9) ;
- rejeu déterministe (contrôle négatif de E1) ;
- prompt adversarial de boucle infinie, qui doit être coupé au plafond ;
- test de non-montage de $D_{\mathrm{final}}$.

### 5. Références

Attributions données de mémoire. Les détails de publication sont à vérifier ; aucun identifiant n'est fourni.

**Analyse exploratoire puis confirmatoire :**
- Wagenmakers, Wetzels, Borsboom, van der Maas, Kievit (2012), « An Agenda for Purely Confirmatory Research », *Perspectives on Psychological Science* (à vérifier).
- Nosek, Ebersole, DeHaven, Mellor (2018), « The Preregistration Revolution », *PNAS* (à vérifier).
- Gelman, Loken (2013), « The Garden of Forking Paths », document de travail (à vérifier).

**Réutilisation adaptative d'un jeu de test :**
- Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), « The Reusable Holdout: Preserving Validity in Adaptive Data Analysis », *Science* (à vérifier).
- Blum, Hardt (2015), « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », ICML (à vérifier).
- Roelofs et al. (2019), « A Meta-Analysis of Overfitting in Machine Learning », NeurIPS (à vérifier).
- Recht, Roelofs, Schmidt, Shankar (2019), « Do ImageNet Classifiers Generalize to ImageNet? », ICML (à vérifier).

**Variance entre graines et significativité :**
- Reimers, Gurevych (2017), « Reporting Score Distributions Makes a Difference… », EMNLP (à vérifier).
- Dodge et al. (2020), « Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping » (à vérifier).
- Bouthillier et al. (2021), « Accounting for Variance in Machine Learning Benchmarks », MLSys (à vérifier).
- Dror, Baumer, Shlomov, Reichart (2018), « The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing », ACL (à vérifier).
- Card et al. (2020), « With Little Power Comes Great Responsibility », EMNLP (à vérifier).
- Miller (2024), « Adding Error Bars to Evals » : référence à vérifier.

**Agents outillés et bacs à sable :**
- Ruan et al. (2024), « Identifying the Risks of LM Agents with an LM-Emulated Sandbox », ICLR (à vérifier).
- Jimenez et al. (2024), « SWE-bench… », ICLR (à vérifier).
- Kapoor, Stroebl, Siegel, Nadgir, Narayanan (2024), « AI Agents That Matter » : comparaisons à coût contrôlé ; à vérifier.

### 6. Comment départager les voies

Trois voies, aucune n'est « la » réponse.

- **V1 — « Conception non inférentielle, confirmation seule ».**
  - La conception n'est qu'un générateur de candidats. Aucun score de conception n'est cité comme résultat. Tout se joue dans E2 sur ≥ 96 items.
  - Elle gagne si E3 montre un optimisme fort et si E4 donne $\rho\le0{,}5$.
- **V2 — « Conception protégée ».**
  - Répétitions R ≥ 3, garde-fous P1 à P4, règle d'arrêt.
  - Elle gagne si E1 montre $\sigma_{\text{run}}$ petit et si E3 montre qu'un garde-fou réduit l'optimisme sans perdre la bonne variante.
- **V3 — « Plus d'items plutôt que plus de graines ».**
  - Elle gagne si E1 montre $\sigma_{\text{run}}\ll$ bruit d'item. Le budget va alors aux items (vers n ≈ 400, illustratif), seul moyen de voir des gains de 0,05.

**Le premier arbitre est E1.** Il est peu coûteux en régime R-éval et départage déjà V2 et V3.

**Ce qu'il faudrait savoir de plus :**
- qui lit les scores de $D_{\mathrm{final}}$ pendant la conception (a9) ;
- les taux de base des classes (a13) ;
- si les textes sont publics (canal de recherche) ;
- si l'hôte peut être rendu déterministe ;
- le budget réel en dollars ;
- l'estimand visé : ces items-là, ou la population d'items (b).

FIN-DE-CELLULE