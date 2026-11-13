# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Traitement critique par critique

Je regroupe par méthode, puis par thème transversal. Chaque critique est attribuée à son auteur (A, C, D, E).

---

### Sur M1 (DPP sur les vues)

**A-a.6 — « Si le noyau code des strates et que le concepteur connaît le générateur, c'est une fuite. La liste des transformations de vue doit être scellée avant le tirage de la graine du monde. »**
→ **Acceptée.** C'est une exigence élémentaire que j'aurais dû formuler. Correction : la liste $\mathcal{V}$ et le noyau $\kappa$ sont scellés (hachage SHA-256) *avant* le tirage de la graine du monde planté. Toute modification après tirage invalide le bras.

**C-a.1 — « Le titre annonce un noyau de Stein mais la définition est un DPP standard. »**
→ **Acceptée.** Le titre « Repulsive Structured Prompting par noyau de Stein » est trompeur. L'objet est un DPP $L$-ensemble, point. Je supprime la mention du noyau de Stein. Aucun opérateur de Stein n'est impliqué.

**C-a.1 (suite) — « Le DPP garantit la diversité des vues, jamais celle des cartes. Si $\Phi : \mathcal{V} \to \mathcal{P}(\mathcal{F})$ est constante, la diversité des cartes est nulle. »**
→ **Transformée en test.** C'est exactement l'hypothèse S4 de ma proposition : que la diversité des vues entraîne la diversité des bassins couverts. Le test est : mesurer $\Pi_v(B)$ (probabilité de couverture du bassin étroit par appel) pour chaque vue $v$ dans le pilote. Si $\operatorname{Var}_v[\Pi_v(B)] \approx 0$, le DPP est inutile. Critère scellé : $\operatorname{Var}_v[\Pi_v(B)] > 0.01$ (illustratif) pour poursuivre.

**D-a — « Un DPP ne maximise pas le volume ; il favorise les grands déterminants. Le gain $p_s > p_0$ est ce qu'il faudrait mesurer. »**
→ **Acceptée partiellement.** Le DPP ne maximise pas $\det(L_S)$ ; il *échantillonne* avec $\Pr(S) \propto \det(L_S)$. La formulation « maximise la diversité volumique » était abusive. Correction : « favorise exponentiellement les sous-ensembles de vues mutuellement distinctes dans le noyau ». La mesure de $p_s$ versus $p_0$ est exactement ce que le pilote doit fournir — c'est l'objet du test ci-dessus.

**E-b — « Le témoin pertinent est un tirage uniforme sans remise dans le même catalogue. »**
→ **Acceptée.** Le témoin doit être un tirage uniforme sans remise dans $\mathcal{V}$, pas un ensemble de vues identiques. Corrigé dans le duel (voir §b).

**A-a.3 (partie M1) — « Vue et identité du proposeur sont confondues ; sans permutation des attributions entre courses, aucun effet de vue n'est séparable d'un effet de modèle. »**
→ **Acceptée.** J'ajoute une permutation aléatoire des attributions vue↔proposeur entre courses (plan en carré latin incomplet, scellé avant la course).

**C-c.2 — « Il manque un bras témoin de paraphrases neutres de la même vue complète pour séparer l'effet $\det(L_S)$ du bruit de formulation. »**
→ **Acceptée.** Ajout d'un bras « paraphrases neutres » : $K$ reformulations de la vue standard complète, de même longueur en jetons, tirées sans critère de diversité thématique.

---

### Sur M2 (exploration conditionnelle séquentielle)

**A-a.1 — « La divergence $D_{\mathrm{KL}}(\hat{p}(Y|t_i,t_j) \| \hat{p}(Y|t_i)\hat{p}(Y|t_j))$ est mal définie : le produit n'est pas normalisé. L'ensemble candidat est juste le complément des paires déjà archivées. »**
→ **Acceptée.** L'expression telle qu'écrite est mathématiquement incorrecte : $\hat{p}(Y|t_i)\hat{p}(Y|t_j)$ ne somme pas à 1 sur $Y$. C'est une erreur de définition, pas une imprécision. **Correction :** je remplace par l'information mutuelle conditionnelle :
$$I_{\mathcal{A}}(Y ; t_j \mid t_i) = \sum_{y, t_j} \hat{p}_{\mathcal{A}}(y, t_j \mid t_i) \log \frac{\hat{p}_{\mathcal{A}}(y \mid t_i, t_j)}{\hat{p}_{\mathcal{A}}(y \mid t_i)}$$
calculée sous les lois de l'archive. Si aucune carte de l'archive ne conditionne conjointement sur $(t_i, t_j)$, alors $\hat{p}_{\mathcal{A}}(y \mid t_i, t_j) = \hat{p}_{\mathcal{A}}(y \mid t_i)$ et $I_{\mathcal{A}} = 0$. A a raison que l'ensemble des candidats à $I = 0$ est essentiellement le complément des paires archivées, sans ordonnancement informatif. Cependant, le filtre « au moins un trait impliqué dans une carte archivée » réduit la taille de $O(d^2)$ à $O(d \cdot |\mathcal{T}(\mathcal{A})|)$, ce qui est opérationnel pour $d \leq 12$.

**A-a.2 — « Incohérence : si seul $t_1$ est archivé et que la composante étroite est $t_3$ conditionnel à $t_2 > 0$, le filtre exclut $(t_2, t_3)$. »**
→ **Acceptée.** C'est une incohérence fatale entre le filtre de M2 et le monde planté du duel. **Deux corrections possibles :** (i) planter un effet marginal de $t_2$ dans l'archive initiale (mais cela change la nature du bassin, comme A le note) ; (ii) lever le filtre et proposer l'énumération complète des paires. **Je choisis (ii) pour le duel principal**, et j'ajoute un **bras factoriel** avec le filtre pour tester si le filtre améliore ou dégrade : voir §b.

**A-a.1 (fin) — « B ne compare pas M2 à l'énumération lexicographique. »**
→ **Acceptée et transformée en contrôle.** J'ajoute un **témoin énumératif** : vues portant l'énumération lexicographique de toutes les paires, même longueur de contexte (voir A-c « Témoin énumératif »). Si M2 ne bat pas l'énumération, l'instrument mathématique (le graphe de dépendance) est inutile et seule agit la consigne de conditionnement.

**C-a.3 — « Même corrigée, une divergence marginale nulle n'exclut pas une interaction conditionnelle qui s'annule en moyenne. Le graphe mesure l'archive, pas le monde. »**
→ **Acceptée.** C'est fondamental : le graphe est un outil de comptabilité de l'archive, pas de détection. Il ne « découvre » rien ; il identifie les paires non encore explorées. La valeur ajoutée de M2 (HYPOTHÈSE) est que *pointer* ces paires au proposeur augmente $\Pi_v(B)$. Ce n'est pas un théorème ; c'est l'objet du test.

**E-b — « M2 : la divergence est bien VÉRIFIÉE comme non définie. La normalisation ne transforme pas automatiquement l'expression en mesure d'interaction. »**
→ **Acceptée** (couvert par la correction ci-dessus).

**C-c.3 — « Il manque un énumérateur aléatoire uniforme de paires. »**
→ **Acceptée.** L'énumérateur aléatoire (tirage uniforme d'une paire par appel, sans graphe) est ajouté comme bras de contrôle.

**D-a — « M2 contient un objet mal défini [...]. L'invitation aléatoire de même longueur est un contrôle nécessaire. »**
→ **Acceptée** (couvert par les corrections précédentes).

---

### Sur M3 (Bayesian Quadrature / GP)

**C-a.2 — « Soit $g(f)$ utilise le verdict (violation N-053), soit c'est une distance publique et l'acquisition par variance maximale est une prime de nouveauté (rejetée au premier tour). »**
→ **Acceptée.** C'est un dilemme que je n'avais pas identifié. Le cas 1 viole N-053, le cas 2 rouvre le rejet de la prime de nouveauté. M3 est **retirée** de la proposition. Je la conserve uniquement comme piste théorique à rouvrir si un argument montre que la prime de nouveauté dans l'*espace des lois* (et non dans le juge) n'a pas les effets néfastes du premier tour.

**E-b — « Demander un écart minimal au nul rouvre la prime de nouveauté. »**
→ **Acceptée** (couvert par le retrait).

**D-a — « M3 n'observe pas le gain qu'elle prétend modéliser. »**
→ **Acceptée** (couvert par le retrait).

---

### Sur M4 (codes couvrants)

**A — Pas de critique directe sur M4 de la part de A.**

**D-a — « La borne de couverture est vraie par construction pour les sous-ensembles. Elle ne dit rien des fonctions, seuils ou chaînes conditionnelles. »**
→ **Acceptée.** L'espace des idées n'est pas $2^d$ ; une idée peut être une fonction, pas un sous-ensemble de traits. M4 reste une borne inférieure théorique sur la couverture des idées *additives par trait* ; elle ne couvre pas les composantes conditionnelles. J'avais noté ce risque mais pas assez fort. **M4 est rétrogradée** à un outil descriptif de couverture combinatoire, pas une méthode active. Elle peut servir à vérifier a posteriori que les vues ont couvert les sous-ensembles de traits simples.

**E-b — « Une borne inférieure sur la taille d'un code ne prouve pas l'existence d'un code de cette taille. B confond cartes et appels. »**
→ **Acceptée.** La confusion cartes/appels est corrigée : 5 proposeurs × 1 appel × 6 cartes = 30 cartes par génération, mais seulement 5 vues distinctes (une par proposeur). Le code couvrant porte sur les vues (5 points), pas sur les cartes (30). Pour $d = 10$ et $r = 2$, il faut $|C| \geq 19$ vues ; avec 5 vues par génération, la couverture prend au moins 4 générations, pas une. Chiffre illustratif corrigé.

---

### Sur M5 (homologie persistante)

**C-b.3 — « Avec $N_a \leq 50$, la bande de confiance dépasse le diamètre de l'espace : aucun cycle $H_1$ n'est discernable du bruit. »**
→ **Acceptée.** J'avais classé M5 dernière précisément pour cette raison. Le calcul de C confirme mon scepticisme. **M5 est retirée** comme méthode active. Elle pourrait être utile à titre exploratoire à partir de ~100 lois, mais ce n'est pas le régime de la course actuelle.

**D-a — « M5 confond trou d'échantillonnage et trou d'archive. »**
→ **Acceptée** (couvert par le retrait).

---

### Critiques transversales sur le duel

**A-a.3 — « Trois générations avec archive héritée : l'effet mesuré est un effet de trajectoire, pas seulement du traitement. La vue M2 est plus longue ; le contrôle négatif doit avoir le même nombre d'invitations et de jetons. »**
→ **Acceptée.** Corrections : (i) la métrique $C_E$ est lue aux trois étages (brut / représentants / retenues) conformément à [C3] §4.1, comme A le demande ; (ii) toutes les vues (M2, contrôle négatif, témoin standard, énumérateur) ont le même budget de jetons ± 5 %, vérifié mécaniquement ; (iii) le nombre d'invitations est identique entre bras M2 et contrôle négatif.

**A-a.4 — « Fuite instrument/évaluation : calibration du regroupement sur le monde du duel, pilote de 5 courses insuffisant. »**
→ **Acceptée.** Corrections : (i) les mondes de calibration du regroupement sont des mondes distincts (graines différentes, même famille de structure), jamais les mondes du duel ; (ii) le pilote ne « calibre » pas $(p_L, p_E)$ mais les *estime* avec un intervalle de confiance, pour vérifier que le monde est dans le régime visé ($p_E < 0.5$, $p_L > 0.5$). Si l'intervalle de $p_E$ à 95 % couvre [0, 0.5], le monde est rejeté et remplacé par un monde à composante plus étroite.

**A-a.5 — « Dessin neuf non déclaré. »**
→ **Acceptée.** M2 (et M1) modifient les consignes pendant la course. Ceci est un **dessin neuf** au sens de [C3] §4.1 (RAPPORTÉ). Je le déclare explicitement. L'objection du premier tour (que modifier les consignes est un dessin neuf qui doit être justifié) s'applique. **Justification** : la question de l'arbitre demande précisément « quelles méthodes permettraient de pousser l'organisme » ; toute réponse opérationnelle modifie le dessin. Les contraintes préservent la garde (le juge est inchangé, pas de score servi, pas de verdict), et la mesure de diversité D2 par l'oracle est lue *après* la course, pas pendant.

**A-b — « Puissance du Fisher : pour $p_{\text{std}} = 0.10$ vs $p_{\text{M2}} = 0.30$, $N = 30$, la puissance est ~0.4–0.5 ; l'issue la plus probable est l'indécision. Zone $[+0.05, +0.20]$ non jugeable. »**
→ **Acceptée.** $N = 30$ est insuffisant pour le seuil $\Delta = 0.20$. **Correction** : (i) le seuil de décision est abaissé à $\Delta > 0$ (test bilatéral d'égalité des proportions, pas test de supériorité à +0.20) ; (ii) $N$ est augmenté à 60 courses par bras (justifié ci-dessous en ancrage matériel) ; (iii) la zone d'indécision est déclarée explicitement : si l'intervalle de confiance à 95 % de $\hat{\Delta}$ chevauche 0, le résultat est « non concluant ». Le seuil de pertinence pratique ($\Delta > 0.15$, illustratif) est un critère secondaire.

**C-b.4 — « La puissance du Fisher bilatéral au seuil $\alpha = 0.05$ avec $N = 30$ est < 0.45 pour $\Delta = 0.20$. »**
→ **Acceptée** (couvert par l'augmentation de $N$).

**A-c — « Monde nul absent. Copies renommées injectées absentes. Témoin énumératif absent. »**
→ **Acceptée intégralement.** Les trois contrôles sont ajoutés :
- **Monde nul** : aucune composante hors archive. Métrique : taux de promotions. Cible : $\leq \alpha$ (conformément à e-BH).
- **Copies renommées** : injectées mécaniquement dans chaque bras pour mesurer la pression vers `si_sinon`.
- **Témoin énumératif** : vues portant l'énumération lexicographique de toutes les paires, même longueur.

**C-c.1 — « Il manque un monde purement nul sous le bras M2 (aucune composante conditionnelle). »**
→ **Acceptée** (couvert par le monde nul ci-dessus).

**D-a (duel) — « Couvrir la composante parmi les retenues ne permet pas d'attribuer l'effet aux invitations plutôt qu'au regroupement, au juge ou à l'archive. »**
→ **Acceptée.** La lecture aux trois étages (brut / représentants / retenues) permet de localiser l'effet. Si $C_E^{\text{brut}}(\text{M2}) > C_E^{\text{brut}}(\text{standard})$ mais $C_E^{\text{ret}}(\text{M2}) = C_E^{\text{ret}}(\text{standard})$, l'effet est perdu au juge, pas aux invitations.

**E-a — « Statut de v67 : B qualifie d'OBSERVÉ-NON-AUDITÉ, mais les faits disent RAPPORTÉ. »**
→ **Acceptée.** Le statut de v67 est **RAPPORTÉ** ([F12] §2). Ma proposition citait S2 comme « OBSERVÉ-NON-AUDITÉ pour v67 » parce que je faisais référence à l'interprétation « variantes proches d'un même constat » qui est dans [F12] §2 (RAPPORTÉ), pas dans [S1]. Je corrige le statut : **RAPPORTÉ**.

**E-a — « Calibration circulaire : sélectionner les mondes du pilote puis réutiliser les observations. »**
→ **Transformée en règle.** Les mondes du pilote sont exclus du duel principal. Le pilote sert uniquement à vérifier le régime ($p_E < 0.5$) et à dimensionner $N$. Les graines du duel sont tirées après le pilote et scellées.

---

## (b) Expériences corrigées

### Duel principal corrigé

**Monde planté.** $d = 6$ traits binaires. Composante A (large) : effet additif de $t_1$. Composante B (étroite) : effet de $t_3$ conditionnel à $t_2 > 0$, nul en moyenne sur $t_2$. **Graine scellée avant le tirage.** Mondes de calibration du regroupement : graines distinctes, même famille.

**Bras (5 au total) :**

| Bras | Description | Vue |
|---|---|---|
| T1 — M2 complet | Invitations sur toutes les paires non archivées | Même longueur |
| T2 — Énumérateur | Invitations identiques (toutes les paires), liste lexicographique | Même longueur |
| T3 — Aléatoire | Une paire tirée uniformément par appel | Même longueur |
| T4 — Contrôle négatif | Invitations sur des paires dont aucun trait n'a d'interaction plantée | Même longueur |
| T5 — Standard | Vue standard v67 identique pour tous | Même longueur (remplie par du texte neutre) |

**Plan de permutation :** attribution vue↔proposeur par carré latin incomplet, permutée entre courses. Scellée avant la course.

**Catalogue de vues pour DPP (M1) :** testé dans un **duel séparé** (DPP vs tirage uniforme sans remise dans $\mathcal{V}$), pour isoler l'effet du DPP de celui de M2. Le catalogue $\mathcal{V}$ et le noyau $\kappa$ sont scellés avant le tirage de la graine.

**Métriques (trois étages, gelées) :**
- $C_E^{\text{brut}}$ : proportion de courses où ≥1 carte brute couvre la composante B (par l'oracle, lu après la course).
- $C_E^{\text{rep}}$ : idem parmi les représentants.
- $C_E^{\text{ret}}$ : idem parmi les retenues après test de mort.
- $\text{FD}^{\text{ret}}$ : nombre de retenues ne correspondant à aucune composante plantée.

**Taille :** $N = 60$ courses par bras, $5 \times 60 = 300$ courses. Puissance estimée (illustratif) pour $p_{\text{std}} = 0.10$, $p_{\text{M2}} = 0.30$, Fisher bilatéral $\alpha = 0.05$ : ~0.75 avec $N = 60$.

**Hypothèses exclusives du duel T1 vs T5 :**
- $H_A$ : $C_E^{\text{brut}}(\text{T1}) > C_E^{\text{brut}}(\text{T5})$ (effet des invitations sur les propositions brutes), avec $\text{FD}^{\text{ret}}(\text{T1}) \leq 1.5 \times \text{FD}^{\text{ret}}(\text{T5})$.
- $H_B$ : $C_E^{\text{brut}}(\text{T1}) \leq C_E^{\text{brut}}(\text{T5})$, ou $\text{FD}^{\text{ret}}(\text{T1}) > 1.5 \times \text{FD}^{\text{ret}}(\text{T5})$.
- $H_A$ falsifié si l'intervalle de confiance à 95 % de $\hat{\Delta}^{\text{brut}}$ est entièrement $\leq 0$, ou si FD dépasse le seuil.
- $H_B$ falsifié si l'intervalle est entièrement $> 0$ et FD est conforme.

**Sous-duel T1 vs T2 :** si T2 ≥ T1, le graphe de dépendance est inutile ; seule la consigne « explorez des paires » agit.

**Sous-duel T1 vs T3 :** si T3 ≥ T1, même l'énumération est inutile ; le simple fait de mentionner une paire suffit.

**Monde nul :** 60 courses sur un monde sans composante hors archive. Cible : taux de promotions $\leq \alpha$. Si le bras T1 a un taux significativement supérieur à $\alpha$, la pression vers `si_sinon` a affaibli la garde et **la méthode est rejetée**.

### Ancrage matériel corrigé

| Poste | Détail | Coût (illustratif) |
|---|---|---|
| Pilote (10 courses × 5 bras) | 50 courses, ~9 000 appels | ~900 $ |
| Duel principal (60 × 5 bras + 60 nul) | 360 courses, ~64 800 appels | ~6 480 $ |
| Orchestrateur + juge (CPU) | ~500 h CPU | ~100 $ |
| **Total** | | **~7 480 $** (illustratif) |

Le coût a quadruplé par rapport à la v1. C'est le prix de la puissance statistique et des contrôles nécessaires. Si le budget est insuffisant, la première coupe est le duel DPP séparé (économie ~1 300 $, illustratif) ; la deuxième est la réduction à 3 bras (T1, T3, T5) en sacrifiant le diagnostic fin T1 vs T2.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

1. **Les proposeurs convergent vers un même bassin** dans les conditions de v67 (RAPPORTÉ, [F12] §2). L'observation [B] (47 % ne quittent jamais leur premier bassin) est cohérente mais provient d'un contexte différent (agents avec feedback, 24 h).

2. **Aucune méthode ne bat le tirage i.i.d. sans structure exploitable** (No Free Lunch). Toute méthode suppose que les traits publics, la grammaire et l'archive portent de l'information sur l'emplacement des bassins étroits. La composante conditionnelle de [C4] §2.1 a cette propriété par construction (son trait conditionnant est public).

3. **Le juge ne peut pas être le levier** : toute prime de nouveauté dans la valeur e viole $\mathbb{E}[e] \leq 1$ sous $H_0$ (OBSERVÉ-NON-AUDITÉ, [S1]). Le levier restant est la **formulation des vues** — ce qui constitue un **dessin neuf** au sens de [C3] §4.1.

4. **La dilution** (OBSERVÉ-NON-AUDITÉ, [S1]) rend toute méthode globale (distance moyenne, GP global, homologie à petit échantillon) aveugle aux bassins étroits confinés à des strates rares.

### Ce qui n'est pas établi

1. Que les bassins « étroits » de la question existent effectivement dans les mondes plantés considérés avec un gain suffisant (**HYPOTHÈSE** S1).

2. Que modifier les vues change la probabilité $\Pi_v(B)$ de couvrir un bassin (**HYPOTHÈSE** S4, testable).

3. Que l'invitation à explorer des paires de traits augmente $\Pi_v(B)$ *au-delà* de l'effet trivial de diversifier le prompt (**HYPOTHÈSE**, objet du sous-duel T1 vs T3).

4. Que le graphe de dépendance (M2 corrigé) apporte un gain par rapport à l'énumération lexicographique (**HYPOTHÈSE**, objet du sous-duel T1 vs T2).

5. Que la pression vers l'exploration ne pousse pas vers `si_sinon` au point d'affaiblir la garde (**HYPOTHÈSE**, objet du monde nul).

### L'expérience à faire en premier

**Le pilote de 50 courses** (10 par bras, 5 bras), sur un monde planté à composante conditionnelle, graine scellée avant le tirage, catalogue de vues scellé. Coût : ~900 $ (illustratif). Il répond à trois questions bloquantes :

1. **$p_E$ est-il < 0.5 ?** Si non, le bassin n'est pas étroit et la question est mal posée. On ajuste le monde.
2. **$\operatorname{Var}_v[\Pi_v(B)] > 0$ ?** Si non, M1 et M2 sont sans objet : les vues ne changent rien.
3. **Le taux de promotions sous le monde nul est-il $\leq \alpha$ dans tous les bras ?** Si non dans le bras T1, la pression a affaibli la garde : arrêt immédiat.

Si les trois réponses sont favorables, le duel principal à 300 courses est lancé. Sinon, le budget est réaffecté.

FIN-DE-CELLULE