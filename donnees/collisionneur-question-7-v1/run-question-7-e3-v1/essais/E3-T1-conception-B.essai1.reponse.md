# Proposition B — Question 7 : L'allumage comme ensemble autocatalytique de fiches

---

## (a) Ce que la question suppose sans que ce soit établi

J'identifie sept présupposés dans l'hypothèse de conv-audit. Chacun reçoit un statut.

| # | Présupposé | Statut | Commentaire |
|---|-----------|--------|-------------|
| P1 | Les ensembles autocatalytiques de Kauffman (réseaux NK, adjacent possible) et les ensembles RAF de Hordijk & Steel disposent d'un algorithme polynomial de détection applicable à des graphes de fiches. | SUPPOSÉ | Conv-audit cite ces travaux de mémoire. L'algorithme RAF existe dans la littérature (référence à vérifier : Hordijk & Steel, 2004, « Detecting autocatalytic, self-sustaining sets in chemical reaction systems », *J. Theor. Biol.* — SUPPOSÉ). Son applicabilité à un graphe de fiches n'est pas démontrée : les conditions formelles (clôture, auto-entretien, « food set ») doivent être redéfinies. |
| P2 | L'analogie fiche = molécule, fusion = réaction, corpus = substrat est structurellement valide. | HYPOTHÈSE | Trois ruptures d'isomorphisme identifiées ci-dessous (§ cassures). |
| P3 | Le paramètre de contrôle est la « dose de contact » (nombre de fusions par génération) et la transition est un seuil net. | HYPOTHÈSE | Bettencourt et al. 2006/2008/2009 (SUPPOSÉ pour le contenu exact, existence VÉRIFIÉE via listing arXiv 1504.00319) proposent deux mécanismes de seuil ($R_0 > 1$ ; composante géante), mais aucun n'a été testé sur un graphe de fiches synthétiques. La « dose de contact » pourrait ne pas être le bon paramètre : la diversité des fiches en entrée (nombre de niches couvertes), la profondeur du graphe de dépendances, ou le taux de survie aux tests de mort pourraient dominer. |
| P4 | La fertilité d'une paire se réduit à sa contribution à la fermeture autocatalytique. | HYPOTHÈSE | C'est une définition candidate, pas un fait. Elle ignore l'impact externe (reprise hors du lot) et le coût de vérification. |
| P5 | Un « allumage » est observable à l'échelle d'une course de quelques générations. | HYPOTHÈSE | Le nombre de fiches dans la génération 1 est probablement trop faible pour qu'une composante géante ou un RAF apparaisse. Kauffman lui-même montre que la probabilité d'un RAF dépend exponentiellement du rapport entre le nombre de réactions possibles et le nombre de catalyseurs — et ce rapport n'est pas connu pour nos fiches. |
| P6 | L'absence d'allumage à toute dose constitue un critère de mort du bisociateur. | HYPOTHÈSE | C'est la proposition de conv-audit. Mais un bisociateur peut produire des idées utiles (reprises, tests de mort franchis) sans jamais former de cycle autocatalytique clos — auquel cas le critère de mort serait trop sévère. |
| P7 | Les antériorités (Kauffman, Arthur, Hordijk, Loreto, Tria) ont effectivement appliqué le cadre autocatalytique à la technologie ou aux idées. | SUPPOSÉ | Kauffman évoque l'« adjacent possible » pour l'innovation (référence à vérifier : Kauffman, 2000, *Investigations*, Oxford UP — SUPPOSÉ). Arthur (2009, *The Nature of Technology* — SUPPOSÉ) parle de recombinaison technologique, pas explicitement d'ensembles autocatalytiques au sens RAF. Tria et al. 2014 (existence VÉRIFIÉE, *Sci. Rep.* 4:5890) modélisent les nouveautés corrélées, pas la fermeture autocatalytique. Le pont entre RAF et idées n'est peut-être fait par personne explicitement. |

### Où l'analogie casse : trois ruptures d'isomorphisme

**Cassure 1 : non-consommation.** Une molécule consommée dans une réaction disparaît du pool ; une fiche fusionnée reste disponible. Conséquence : le graphe de fiches n'a pas de dynamique de déplétion. Le « food set » (substrat) est permanent. Cela simplifie la condition d'auto-entretien (pas besoin de régénérer les réactifs) mais supprime la compétition pour les ressources qui, dans les modèles chimiques, sélectionne les cycles autocatalytiques les plus efficaces. Sans compétition, tout lot suffisamment dense est trivialement auto-entretenu — ce qui viderait la notion d'allumage de son contenu discriminant.

**Cassure 2 : stœchiométrie absente.** Une réaction chimique a des coefficients fixes (2H₂ + O₂ → 2H₂O). Une fusion de fiches est un acte créatif dont le nombre et la nature des « produits » (nouvelles fiches, lemmes, outils) sont contingents et non déterministes. Le graphe de réactions n'est pas donné a priori ; il est construit par les proposeurs. On ne peut pas vérifier la clôture d'un RAF sur un graphe qui n'existe pas encore.

**Cassure 3 : le goulot du jugement.** Dans un système chimique, la « catalyse » est un fait physique : la molécule C abaisse l'énergie d'activation de A + B → D. Dans l'organisme, la catalyse est un acte de vérification humaine ou mécanique (test de mort, lecture distincte). Le taux de catalyse dépend du budget de vérification, pas de la structure du lot. Un lot peut être « potentiellement autocatalytique » mais ne jamais s'allumer faute de cycles de vérification. Le modèle RAF ne contient pas ce goulot.

**Conséquence pour l'analogie.** L'analogie est féconde comme **générateur d'hypothèses** (elle fournit un paramètre d'ordre, un seuil, des marques observables) mais elle n'est pas un isomorphisme. Le cadre RAF doit être adapté : (i) supprimer la déplétion (food set permanent), (ii) remplacer la stœchiométrie par une relation probabiliste (une fusion de fiches $f_i, f_j$ produit une fiche $f_k$ avec probabilité $p_{ij}^k$ conditionnée au proposeur et au juge), (iii) intégrer le goulot de vérification comme contrainte de flux.

---

## (b) Expériences décisives — duels H_A / H_B

### Expérience 1 : Existence d'un seuil d'allumage

**H_A (transition de phase)** : Il existe une valeur critique $\delta_c$ du paramètre de contrôle (dose de contact = nombre de fusions tentées par génération, normalisé par le nombre de fiches disponibles) au-delà de laquelle la probabilité qu'un sous-ensemble RAF (adapté : clôture et auto-entretien sans déplétion) apparaisse dans le graphe fiche→fusion→fiche passe brusquement de ~0 à ~1.

**H_B (croissance lisse)** : Le nombre de fiches réutilisées comme entrée de nouvelles fusions croît linéairement (ou sous-linéairement) avec la dose de contact, sans seuil net ; il n'y a pas de transition de phase.

**Métrique** : Taille de la plus grande composante « auto-entretenue » du graphe dirigé fiche→fusion→fiche, normalisée par le nombre total de fiches. Formellement : le plus grand sous-graphe $S$ tel que toute fiche $f \in S$ est le produit d'au moins une fusion dont les deux entrées sont aussi dans $S$.

**Seuil de décision** : H_A est corroborée si la courbe taille($S$)/taille(total) en fonction de $\delta$ présente un point d'inflexion avec une dérivée seconde négative suivie d'une dérivée seconde positive (forme sigmoïde), identifiable par un test de changement de pente (Clauset et al. 2009, pour la détection de lois de puissance — référence à vérifier). H_B est corroborée si la courbe est monotone concave ou linéaire sans inflexion.

**Contrôle négatif** : Graphe fiche→fusion→fiche où les identités des fiches d'entrée de chaque fusion sont permutées aléatoirement (même densité de liens, même nombre de fusions par génération, mais aucune structure sémantique). Si H_A apparaît aussi dans le contrôle permuté, la transition est un artefact de la densité du graphe, pas de la structure épistémique.

**Ce qui falsifie quoi** :
- H_A est falsifiée si la courbe reste lisse et sans inflexion, ou si le contrôle permuté présente la même transition.
- H_B est falsifiée si une inflexion nette est détectée dans le graphe réel et absente du contrôle permuté.

### Expérience 2 : Fertilité paire → fermeture autocatalytique vs. fertilité paire → impact isolé

**H_A (fertilité autocatalytique)** : Les paires dont la fusion contribue à la fermeture d'un sous-ensemble auto-entretenu (au sens de l'expérience 1) produisent des fiches de plus grande valeur (mesurée par le nombre de réutilisations en génération suivante + survie aux tests de mort) que les paires dont la fusion ne ferme aucun cycle.

**H_B (fertilité indépendante)** : La valeur d'une fusion est prédite par les traits de la paire d'entrée (distance sociale, proximité formelle, taille des niches — cf. section D des faits) indépendamment de sa position dans le graphe de dépendances ; la fermeture autocatalytique n'ajoute rien.

**Métrique** : Régression du nombre de réutilisations et du taux de survie aux tests de mort sur (i) les traits de la paire et (ii) un indicateur binaire « la fusion ferme-t-elle un cycle auto-entretenu ? ». Le test est la significativité et la taille d'effet de (ii) après contrôle par (i).

**Contrôle négatif** : Paires appariées par traits (même $d_{\text{soc}}$, $d_{\text{lex}}$, $d_{\text{math}}$ ± tolérance) dont l'une ferme un cycle et l'autre non.

**Ce qui falsifie quoi** :
- H_A est falsifiée si l'indicateur (ii) est non significatif ou de taille d'effet négligeable après contrôle.
- H_B est falsifiée si l'indicateur (ii) est significatif avec une taille d'effet substantielle (par exemple, Cohen $d > 0,5$ — seuil illustratif).

### Expérience 3 : Nécessité du goulot de vérification

**H_A (goulot déterminant)** : À dose de contact fixée, le taux d'allumage (apparition d'un sous-ensemble auto-entretenu) dépend plus du taux de vérification (fraction de fusions soumises à un test de mort) que de la dose elle-même.

**H_B (dose déterminante)** : Le goulot de vérification ne change pas qualitativement le seuil d'allumage ; seule la dose de contact compte.

**Métrique** : Seuil $\delta_c$ estimé pour différents taux de vérification $v \in \{0.1, 0.3, 0.5, 0.8, 1.0\}$ (illustratifs). H_A est corroborée si $\delta_c$ varie significativement avec $v$ ; H_B si $\delta_c$ est invariant (± écart-type de bootstrap).

**Contrôle** : Vérification aléatoire (le test de mort est appliqué à des fusions tirées au hasard, sans priorité).

**Ce qui falsifie quoi** :
- H_A falsifiée si $\delta_c$ est invariant sous $v$.
- H_B falsifiée si $\delta_c$ diminue significativement quand $v$ augmente (la vérification abaisse le seuil d'allumage en éliminant les fusions stériles qui diluent le graphe).

---

## (c) Instruments nommés et mesures minimales de fonctionnement

### Instrument 1 : Algorithme de détection RAF (Hordijk & Steel)

L'algorithme de détection RAF est conçu pour des réseaux de réactions chimiques avec food set, clôture et auto-entretien. Pour l'appliquer aux fiches, il faut :

**Adaptation requise** : (i) Définir le food set : les fiches initiales (importées du corpus, non produites par fusion). (ii) Définir la clôture : toute fiche du lot est soit dans le food set, soit produit d'une fusion dont les deux entrées sont dans le lot. (iii) Définir l'auto-entretien : chaque réaction (fusion) du lot est « catalysée » par au moins une fiche du lot. C'est ici que l'analogie est la plus fragile : qu'est-ce qui « catalyse » une fusion ? Proposition : une fiche $f_c$ catalyse la fusion $(f_i, f_j) \to f_k$ si $f_c$ a été citée ou utilisée comme contexte par le proposeur pendant la génération de $f_k$. Cela requiert une journalisation explicite (voir §e).

**Taux de détection (rappel)** : Sur des graphes synthétiques avec RAF injectés (10 graphes de 100 nœuds avec un RAF de taille 10 planté, 10 graphes sans RAF — illustratifs), l'algorithme doit retrouver le RAF planté dans ≥ 9/10 cas positifs.

**Taux de fausses alertes** : Sur les 10 graphes sans RAF planté, l'algorithme ne doit détecter aucun RAF de taille ≥ 3 (seuil illustratif). Si des RAF « parasites » apparaissent dans les graphes nuls, le critère de fermeture est trop lâche.

**Cas honnêtes appariés** : Graphes réels de la génération 1, appariés à des graphes permutés (même topologie, sémantique détruite).

**Vérification mécanique à battre** : Détection naïve de cycles dans le graphe dirigé (composantes fortement connexes par Tarjan). Si l'algorithme RAF ne détecte pas plus de structure que les composantes fortement connexes, il n'apporte rien.

### Instrument 2 : Composante géante du graphe fiche→fusion→fiche (Bettencourt et al. 2009)

**Mesure** : Fraction du graphe dans la plus grande composante connexe (non dirigée) et dans la plus grande composante fortement connexe (dirigée), par génération.

**Taux de détection** : Sur des graphes Erdős–Rényi de même taille et densité, le seuil théorique de la composante géante est $p = 1/n$. Si la composante géante du graphe réel apparaît à une densité significativement différente de $1/n$, il y a structure épistémique.

**Fausses alertes** : Comparaison avec 100 graphes nuls (même séquence de degrés, arêtes permutées) — illustratif.

### Instrument 3 : $R_0$ épidémiologique (Bettencourt et al. 2006/2008)

**Mesure** : $R_0$ = nombre moyen de fusions de génération $g+1$ dont au moins une entrée provient d'une fiche produite en génération $g$. C'est le « nombre de reproduction » d'une fiche.

**Seuil** : $R_0 > 1$ signifie que chaque fiche « engendre » en moyenne plus d'une fiche en génération suivante : le lot est auto-entretenu. $R_0 < 1$ : extinction progressive.

**Contrôle** : $R_0$ calculé sur le graphe permuté. Si $R_0^{\text{permuté}} > 1$ aussi, le signal est un artefact de densité.

**Fausses alertes** : Si $R_0 > 1$ mais toutes les fiches de génération $g+1$ échouent aux tests de mort, le $R_0$ est gonflé par des fusions stériles. Il faut un $R_0^{\text{filtré}}$ : ne compter que les fiches ayant survécu au test de mort.

---

## (d) Ancrage matériel

### Modèles ouverts utilisables

- **Détection RAF** : Implémentation de l'algorithme de Hordijk & Steel dans le package `catinger` (Python) ou `RAF` (R) — référence à vérifier. Alternative : implémentation à partir du pseudo-code de Hordijk & Steel (2004 — SUPPOSÉ) sur le graphe de fiches, complexité annoncée polynomiale en $O(n \cdot |R|)$ où $n$ = nombre de types moléculaires (fiches) et $|R|$ = nombre de réactions (fusions).
- **Graphes** : NetworkX (Python, open source) pour les composantes fortement connexes, la composante géante, les métriques de percolation.
- **Proposeurs de fusions** : Modèles ouverts de la gamme Llama 3/3.1 (Meta, licence communautaire) ou Mistral (Apache 2.0) pour les tests en bac à sable. Les faits ne spécifient pas quel modèle est utilisé dans les courses ; si c'est un modèle fermé, le coût est celui de l'API.

### Calcul nécessaire

- **Génération 1** : Les faits ne donnent pas le nombre de fiches ni le nombre de fusions prévues. Estimation illustrative : 50 fiches initiales × 200 fusions tentées = 10 000 appels à un LLM proposeur + 200 tests de mort. À ~$0,01/appel (modèle ouvert sur GPU cloud, illustratif) : ~$100 pour la génération. L'algorithme RAF sur un graphe de 250 nœuds et 200 arêtes : négligeable (<1 s sur un CPU).
- **Génération 2** : Si la génération 1 produit 80 fiches survivantes (illustratif), et qu'on tente 500 fusions : ~$250 (illustratif).
- **Contrôles permutés** : 100 graphes × algorithme RAF = quelques secondes.

### Coût total estimé

~$350–$500 pour deux générations avec contrôles (illustratif). Le goulot n'est pas le calcul mais la conception des tests de mort (travail humain de l'arbitre et des juges figés).

---

## Définition opérationnelle de l'allumage et de la fertilité

En intégrant les cassures de l'analogie et les instruments ci-dessus, je propose :

**Allumage** (définition opérationnelle) : Un lot de fiches est « allumé » à la génération $g$ si et seulement si :
1. Il existe un sous-ensemble $S$ de fiches de taille $|S| \geq s_{\min}$ (seuil à fixer, par exemple $s_{\min} = 5$ — illustratif) tel que toute fiche $f \in S$ non initiale est le produit d'une fusion dont les deux entrées sont dans $S$ (clôture) ;
2. Toute fiche de $S$ a survécu au test de mort ;
3. Le $R_0^{\text{filtré}}$ de $S$ (calculé sur les fiches de $S$ ayant produit des fusions en génération $g+1$) est $> 1$.

La condition 2 est la parade à la cassure 3 (goulot de vérification). La condition 3 est la prédiction falsifiable pour la génération suivante.

**Fertilité d'une paire** (définition opérationnelle) : La fertilité de la paire $(f_i, f_j)$ est la variation marginale de la taille du plus grand sous-ensemble allumé $S$ quand on ajoute la fusion $(f_i, f_j) \to f_k$ au graphe. Formellement : $\text{Fert}(f_i, f_j) = |S^{+}| - |S^{-}|$ où $S^{+}$ est le plus grand ensemble allumé avec la fusion et $S^{-}$ sans.

---

## Prédiction chiffrée et critère de mort pour la génération 2

**Prédiction (H_A — transition de phase)** : Si la dose de contact $\delta$ (fusions tentées / fiches disponibles) dépasse $\delta_c$ (à estimer sur graphes synthétiques calibrés sur la génération 1 — valeur inconnue a priori, on journalise $\delta$ pour l'estimer a posteriori), alors un sous-ensemble allumé de taille $\geq 5$ (illustratif) apparaît en génération 2.

**Critère de mort du bisociateur** (version non triviale) : Le bisociateur est déclaré « non autocatalytique » si, après deux générations à dose maximale (toutes les paires possibles tentées dans la contrainte de budget), aucun sous-ensemble allumé de taille $\geq 3$ n'apparaît. **Mais** cela ne tue pas le bisociateur en tant que générateur d'idées utiles ; cela tue seulement l'hypothèse autocatalytique. Conv-audit ne distingue pas les deux, et c'est une erreur conceptuelle : un bisociateur qui produit des fiches reprises et vérifiées sans jamais boucler peut être scientifiquement utile (mode « mine à ciel ouvert ») même si l'allumage au sens autocatalytique n'a pas lieu.

**Critère de mort du bisociateur tout court** (plus général, hors analogie RAF) : Le bisociateur est stérile si, sur deux générations, le taux de survie aux tests de mort des fusions est inférieur au taux de survie de fiches générées par réflexion profonde sans croisement inter-niches, à budget de calcul égal. Ce critère est indépendant de l'allumage.

---

## Antériorités à vérifier

| Auteurs | Année | Titre / objet | Domaine d'application | Statut |
|---------|-------|--------------|----------------------|--------|
| Kauffman, S. A. | 1993 | *The Origins of Order* | Auto-organisation chimique, ensembles autocatalytiques | SUPPOSÉ |
| Kauffman, S. A. | 2000 | *Investigations* | Adjacent possible, innovation | SUPPOSÉ |
| Hordijk, W. & Steel, M. | 2004 | Détection d'ensembles RAF | Chimie prébiotique | SUPPOSÉ |
| Arthur, W. B. | 2009 | *The Nature of Technology* | Recombinaison technologique | SUPPOSÉ |
| Tria, F., Loreto, V., et al. | 2014 | *Dynamics of correlated novelties* | Adjacent possible, nouveautés | VÉRIFIÉ (existence) |
| Bettencourt, L. M. A. et al. | 2006, 2008, 2009, 2015 | Seuil $R_0$, transitions topologiques | Émergence de champs scientifiques | VÉRIFIÉ (existence), SUPPOSÉ (contenu) |
| Solé, R. V. et al. | ~2000 | Réseaux autocatalytiques et innovation technologique | Technologie | SUPPOSÉ — référence à vérifier ; je soupçonne l'existence de travaux de Solé et collaborateurs appliquant les réseaux autocatalytiques à l'évolution technologique, mais je ne peux pas attribuer de titre précis. |
| Iacopini, I. et al. / Steel, M. et al. | ~2020s | Extensions des RAF aux systèmes d'information | Idées / mèmes | SUPPOSÉ — je n'ai pas de référence vérifiable. |

**Lacune importante** : je n'ai trouvé dans les faits aucune référence vérifiée appliquant explicitement le cadre RAF (au sens strict de Hordijk & Steel) aux idées ou à la technologie. L'analogie de conv-audit est peut-être originale. Cela mériterait une recherche systématique avant de la présenter comme une transposition d'un cadre existant.

---

## (e) Ce qu'il faut journaliser dès la génération 1

Pour que les expériences ci-dessus soient réalisables sur les données de la génération 1, il faut journaliser, pour chaque fusion :

1. **Identifiants des fiches d'entrée** ($f_i$, $f_j$) et de la fiche produite ($f_k$), avec horodatage et numéro de génération.
2. **Contexte utilisé par le proposeur** : liste des fiches consultées ou citées pendant la génération de $f_k$ au-delà de $f_i$ et $f_j$ (nécessaire pour définir la « catalyse » dans le cadre RAF adapté).
3. **Résultat du test de mort** : binaire (survie / échec), avec le type de test (formel, bac à sable, lecture distincte).
4. **Traits de la paire** : $d_{\text{soc}}$, $d_{\text{lex}}$, $d_{\text{math}}$ tels que définis dans la section A des faits (si disponibles ; sinon, les données brutes pour les calculer a posteriori).
5. **Réutilisations** : à chaque fusion de génération $g+1$, enregistrer quelles fiches de génération $g$ sont utilisées en entrée (nécessaire pour calculer $R_0$).
6. **Dose de contact** $\delta_g$ : nombre de fusions tentées / nombre de fiches disponibles en début de génération $g$.
7. **Budget de vérification** $v_g$ : fraction des fusions soumises à un test de mort.

Sans les points 2 et 5, l'algorithme RAF et le $R_0$ ne sont pas calculables. Le point 2 est le plus coûteux à journaliser (il demande que le proposeur explicite son contexte), mais c'est aussi le point qui distingue l'approche autocatalytique d'une simple analyse de graphe de citations.

---

## Note finale de synthèse

L'analogie RAF est un **bon générateur d'hypothèses testables** et un **mauvais modèle littéral**. Les trois cassures (non-consommation, absence de stœchiométrie, goulot de vérification) empêchent une transposition directe. Mais l'analogie fournit trois quantités mesurables dès la génération 1 (taille du plus grand sous-ensemble clos, $R_0^{\text{filtré}}$, fertilité marginale), un paramètre de contrôle ($\delta$), et un critère de mort pour l'hypothèse autocatalytique (pas pour le bisociateur lui-même — distinction que conv-audit ne fait pas). Le risque principal est de confondre « le lot n'est pas autocatalytique » avec « le bisociateur est stérile » : ce sont deux constats distincts, et seul le second est fatal.

FIN-DE-CELLULE