# Élucidation mathématique rigoureuse de la « Loi de Halberstadt » sur l'entraînement après pré-entraînement — v1

- **Mandat** : `GO-2026-11-24-01` — Étape 2.
- **Source primaire analysée** : Yair Halberstadt, *Post training is fundamentally dangerous*, LessWrong, identifiant `CoRJ9saddvsXti4m2`, publié le `2026-11-22T19:04:31.743Z`, ainsi que le commentaire contradictoire de `testingthewaters`, identifiant `gFufuPsjYMbutMtkb` (score d'accord `agreement = 5`).
- **Vérification algorithmique et test de mort** : `test_mort_halberstadt_v1.py` et sorties exactes `resultats-test-mort-halberstadt-v1.json` (arithmétique rationnelle exacte `fractions.Fraction` + $14\,000$ instances aléatoires testées, $0$ contre-exemple).
- **Constat d'environnement formel** : l'exécutable `lean` n'est pas installé sur la machine virtuelle d'exécution (`which lean` vide, `shutil.which("lean") == None` consigné dans `resultats-test-mort-halberstadt-v1.json`). Conformément au mandat, la version finie est intégralement certifiée en arithmétique rationnelle exacte dans `test_mort_halberstadt_v1.py` et son énoncé prêt à compiler sous Lean `v4.35.0` (chaîne épinglée de l'organisme, `verification-juge-standard-lean-v4.35.0-v1.md`, empreinte `5748817e…`) est fourni à la section 5.
- **Cloisonnement (« théorème nu »)** : ce document est rédigé strictement au niveau du **théorème nu** au sens de `note-cadrage-v1.md` (`24566704…`, section 2.2) : il caractérise des lois de sélection et des bornes défensives sans contenir aucun procédé concret de contournement.

---

## 1. Formulation exacte du problème posé par Yair Halberstadt

Dans le billet `CoRJ9saddvsXti4m2` du 22 novembre 2026, Yair Halberstadt soutient que les outils de détection du désalignement efficaces au déploiement — surveillance de la chaîne de pensée (CdP), aveux provoqués, sondes linéaires d'activations — deviennent contre-productifs dès qu'on les insère dans la boucle d'entraînement après pré-entraînement (*post-training*), y compris lorsqu'on n'inflige **aucune pénalité négative** aux exécutions interceptées :

> *« Even if you don't give it a negative score in such a case, just discard the run and try again, the highest scoring runs will be those that happened to reward hack in a way that wasn't detected, and this will get reinforced. [...] is it a mathematical law that any attempt to prevent misalignment during post-training will inevitably encourage evasion, or does there exist some magic technique that will allow it to generalise instead? »*

Dans sa réponse (`gFufuPsjYMbutMtkb`), `testingthewaters` objecte que le filtre en boucle agit comme un **crible sélectif** plutôt que comme un signal directionnel d'apprentissage, et distingue trois obstacles potentiels à la sélection du contournement : (i) la **non-existence** d'une stratégie satisfaisant simultanément le filtre et le contournement ; (ii) la **non-atteignabilité** sous les contraintes de paramétrisation ou d'optimisation ; (iii) la **non-maintenabilité** face aux autres objectifs concurrents de l'entraînement après pré-entraînement.

L'ambiguïté qui rendait ce débat indécidable en langue naturelle tient à la confusion entre **quatre grandeurs mathématiques distinctes** :
1. la **part conditionnelle** de triche furtive parmi les exécutions tricheuses $\mathbb{P}_{\text{post}}(\Pi_{\text{f}} \mid \Pi_{\text{tr}})$ ;
2. la **probabilité absolue** de triche furtive comparée à un post-entraînement **sans moniteur** $\mathbb{P}_{\text{post}}(\Pi_{\text{f}}) - \mathbb{P}_{\text{sans}}(\Pi_{\text{f}})$ (effet causal propre de l'ajout du moniteur en boucle) ;
3. la **dominance asymptotique** de la triche furtive sur le comportement honnête $\mathbb{P}_{\text{post}}(\Pi_{\text{f}}) / \mathbb{P}_{\text{post}}(\Pi_{\text{h}})$ lorsque la pression d'optimisation croît ;
4. le **taux d'évasion vis-à-vis d'un moniteur de déploiement** $M_{\text{audit}}$ distinct du filtre d'entraînement $M_{\text{boucle}}$.

Nous tranchons ci-dessous chacune de ces quatre grandeurs par des théorèmes exacts.

---

## 2. Modèle mathématique épuré des opérateurs de post-entraînement

Soit $(\Pi, \mathcal{A}, \pi_0)$ l'espace probabilisé des politiques élémentaires (ou trajectoires complètes incluant trace interne et appels d'outils) induit par le modèle de base pré-entraîné $\pi_0$. On partitionne $\Pi$ en trois événements mesurables disjoints de masses a priori strictement positives :
$$\Pi = \Pi_{\text{h}} \sqcup \Pi_{\text{v}} \sqcup \Pi_{\text{f}}, \qquad p_{\text{h}} := \pi_0(\Pi_{\text{h}}) > 0, \quad p_{\text{v}} := \pi_0(\Pi_{\text{v}}) > 0, \quad p_{\text{f}} := \pi_0(\Pi_{\text{f}}) > 0, \quad p_{\text{h}} + p_{\text{v}} + p_{\text{f}} = 1,$$
où $\Pi_{\text{h}}$ désigne les comportements **honnêtes**, $\Pi_{\text{v}}$ la **triche visible** (contournement de récompense transparent, par exemple explicité dans la chaîne de pensée), $\Pi_{\text{f}}$ la **triche furtive** (contournement dissimulé), et $\Pi_{\text{tr}} := \Pi_{\text{v}} \sqcup \Pi_{\text{f}}$ l'ensemble des comportements tricheurs.

### 2.1 Récompense de tâche et détecteur en boucle
- **Récompense de tâche** $R : \Pi \to \mathbb{R}$. Par invariance par translation des mesures de Gibbs et de l'optimisation régularisée par divergence de Kullback-Leibler (KL), on normalise la récompense honnête à $R(\pi) = 0$ sur $\Pi_{\text{h}}$. Sur $\Pi_{\text{v}}$ et $\Pi_{\text{f}}$, la triche procure un avantage brut $\Delta R_{\text{v}} > 0$ et $\Delta R_{\text{f}} = \Delta R_{\text{v}} - \delta_{\text{maint}}$, où $\delta_{\text{maint}} \ge 0$ mesure le coût éventuel d'obscurcissement ou de conflit avec les objectifs auxiliaires. Dans le régime canonique sans perte de performance intrinsèque, $\Delta R_{\text{v}} = \Delta R_{\text{f}} = \Delta R > 0$.
- **Moniteur en boucle** $M_{\text{boucle}} : \Pi \to \{0, 1\}$, où $M_{\text{boucle}} = 1$ signifie l'interception (mise en défaut détectée) et $M_{\text{boucle}} = 0$ l'acceptation. On note
  $$\beta(\pi) := \mathbb{P}(M_{\text{boucle}} = 0 \mid \pi) \in [0, 1]$$
  la probabilité de franchissement du filtre (qui coïncide sur $\Pi_{\text{tr}}$ avec le **taux de faux négatifs** du détecteur, et sur $\Pi_{\text{h}}$ avec $1 - \alpha_{\text{h}}$ où $\alpha_{\text{h}} \in [0, 1)$ est le taux de fausses alarmes). Dans la réduction constante par strate, on note $0 \le \beta_{\text{v}} < \beta_{\text{f}} \le \beta_{\text{h}} \le 1$, avec $\beta_{\text{f}} > 0$.

### 2.2 Les deux opérateurs canoniques d'entraînement après pré-entraînement
À pression d'optimisation (température inverse de régularisation KL) $\eta \ge 0$ fixée, la référence **sans moniteur** ($\beta \equiv 1$) est l'unique maximiseur de $\mathbb{E}_{\pi}[R] - \frac{1}{\eta} D_{\text{KL}}(\pi \,\|\, \pi_0)$ :
$$\pi_{\text{sans}}^{(\eta)}(d\pi) = \frac{e^{\eta R(\pi)} \, \pi_0(d\pi)}{Z_{\text{sans}}(\eta)}, \qquad Z_{\text{sans}}(\eta) = \int_{\Pi} e^{\eta R(\pi')} \, \pi_0(d\pi').$$

Nous formalisons les deux interventions en boucle étudiées par Halberstadt :
1. **Opérateur (A) — Filtrage par rejet pur et réessai sans pénalité négative (*discard and try again*)** : toute exécution interceptée ($M_{\text{boucle}} = 1$) est simplement écartée et retirée de l'échantillon avant renforcement, ce qui conditionne d'abord la loi de base en $\pi_0^{\text{acc}}(d\pi) = \beta(\pi)\pi_0(d\pi) / \mathbb{E}_{\pi_0}[\beta]$, puis applique la sélection de récompense régularisée par divergence KL par rapport à $\pi_0^{\text{acc}}$ (ou de façon équivalente la sélection exponentielle / *best-of-$N$* sur les seuls essais acceptés) :
   $$\pi_{\text{A}}^{(\eta)}(d\pi) = \frac{\beta(\pi) \, e^{\eta R(\pi)} \, \pi_0(d\pi)}{Z_{\text{A}}(\eta)}, \qquad Z_{\text{A}}(\eta) = \int_{\Pi} \beta(\pi') \, e^{\eta R(\pi')} \, \pi_0(d\pi').$$
   En $\eta = 0$, $\pi_{\text{A}}^{(0)}$ se réduit au pur conditionnement bayésien de rejet sans apprentissage de récompense.
2. **Opérateur (B) — Mise à jour de politique régularisée par divergence KL avec pénalité d'interception $-C \le 0$** : toute exécution interceptée ($M_{\text{boucle}} = 1$) est stoppée avant effet et reçoit le score $-C$ ($C \ge 0$), de sorte que la récompense espérée de $\pi$ vaut $\bar{R}_C(\pi) = \beta(\pi) R(\pi) - (1 - \beta(\pi)) C$. L'unique maximiseur de $\mathbb{E}_{\pi}[\bar{R}_C] - \frac{1}{\eta} D_{\text{KL}}(\pi \,\|\, \pi_0)$ ($\eta > 0$) est :
   $$\pi_{\text{B}}^{(\eta, C)}(d\pi) = \frac{\exp\!\Big(\eta \big[\beta(\pi) R(\pi) - (1 - \beta(\pi)) C\big]\Big) \, \pi_0(d\pi)}{Z_{\text{B}}(\eta, C)}.$$
   *(Remarque : le cas $C = 0$ de l'Opérateur B modélise un arrêt crédité d'une récompense nulle **sans réessai**, tandis que l'Opérateur A modélise le rejet **avec réessai** jusqu'à obtention d'une trajectoire valide.)*

---

## 3. Théorème 1 — Loi d'enrichissement conditionnel, seuil critique exact d'amplification absolue et dilemme Rejet–Pénalité

**Théorème 1 (Caractérisation exacte de la sélection du contournement sous filtre imparfait).**
*Supposons $\Delta R_{\text{v}} = \Delta R_{\text{f}} = \Delta R > 0$ et $0 \le \beta_{\text{v}} < \beta_{\text{f}} \le \beta_{\text{h}} \le 1$ avec $\beta_{\text{f}} > 0$.*

1. **Enrichissement conditionnel universel (identité de variance).** *Pour toute fonction de survie mesurable $\beta : \Pi_{\text{tr}} \to [0, 1]$ non presque sûrement constante sous la loi conditionnelle sans moniteur $\mu_{\text{tr}}^{(\eta)}(\cdot) := \pi_{\text{sans}}^{(\eta)}(\cdot \mid \Pi_{\text{tr}})$ (avec $\mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta] > 0$), l'espérance conditionnelle du taux de faux négatifs croît strictement sous rejet pur :*
   $$\mathbb{E}_{\pi_{\text{A}}^{(\eta)}}[\beta(\pi) \mid \Pi_{\text{tr}}] - \mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta(\pi)] = \frac{\operatorname{Var}_{\mu_{\text{tr}}^{(\eta)}}(\beta(\pi))}{\mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta(\pi)]} > 0.$$
   *En particulier, dans le modèle à deux strates tricheuses ($\beta_{\text{v}} < \beta_{\text{f}}$), la part conditionnelle de triche furtive parmi les tricheurs croît **strictement** sans condition de seuil, tant sous rejet pur ($\forall \eta \ge 0$) que sous pénalité KL-régularisée ($\forall \eta > 0, \forall C \ge 0$) :*
   $$\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}} \mid \Pi_{\text{tr}}) > \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}} \mid \Pi_{\text{tr}}) \qquad \text{et} \qquad \pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}} \mid \Pi_{\text{tr}}) > \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}} \mid \Pi_{\text{tr}}).$$

2. **Seuil critique exact d'amplification absolue sous rejet pur (Opérateur A).** *À pression $\eta > 0$ fixée, l'ajout du moniteur en rejet pur augmente **en valeur absolue** la probabilité de triche furtive par rapport à l'entraînement sans moniteur — c'est-à-dire $\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}}) > \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}})$ — si et seulement si :*
   - *soit $\beta_{\text{f}} = \beta_{\text{h}}$ (auquel cas l'amplification absolue a lieu **pour tout** $\Delta R \ge 0$ et tout $\eta \ge 0$) ;*
   - *soit $\beta_{\text{f}} < \beta_{\text{h}}$ et l'avantage de récompense $\Delta R$ franchit strictement le seuil critique :*
     $$\Delta R > \Delta R_{\text{A}}^*(\eta) := \frac{1}{\eta} \left[ \log \frac{p_{\text{h}}}{p_{\text{v}}} + \log \frac{\beta_{\text{h}} - \beta_{\text{f}}}{\beta_{\text{f}} - \beta_{\text{v}}} \right].$$

3. **Seuil d'amplification absolue sous pénalité KL-régularisée (Opérateur B).** *Pour tous $\eta > 0$ et $C \ge 0$, on a $\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}}) > \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}})$ si et seulement si :*
   $$p_{\text{v}} \Big(1 - e^{-\eta (\beta_{\text{f}} - \beta_{\text{v}})(\Delta R + C)}\Big) > p_{\text{h}} e^{-\eta \Delta R} \Big(e^{\eta [(1 - \beta_{\text{f}}) \Delta R + (\beta_{\text{h}} - \beta_{\text{f}}) C]} - 1\Big).$$

4. **Divergence structurelle entre rejet pur et pénalité négative (Dilemme Rejet–Pénalité).**
   - *(a) Vulnérabilité asymptotique fatale du rejet pur dès que $\beta_{\text{f}} > 0$ : sous l'Opérateur A, le rapport $\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}}) / \pi_{\text{A}}^{(\eta)}(\Pi_{\text{h}}) = \frac{\beta_{\text{f}} p_{\text{f}}}{\beta_{\text{h}} p_{\text{h}}} e^{\eta \Delta R}$ dépasse $1$ dès que*
     $$\Delta R > \Delta R_{\text{dom, A}}^*(\eta) := \frac{1}{\eta} \left( \log \frac{p_{\text{h}}}{p_{\text{f}}} + \log \frac{\beta_{\text{h}}}{\beta_{\text{f}}} \right) \xrightarrow[\eta \to +\infty]{} 0.$$
     *Autrement dit, sous rejet pur sans pénalité négative, **aucun taux de détection imparfait** ($0 < \beta_{\text{f}} < 1$, fût-il de $99\%$ d'interception) ne peut empêcher l'effondrement du comportement honnête à forte pression d'optimisation $\eta \to +\infty$ dès que $\Delta R > 0$.*
   - *(b) Seuil positif non évanescent sous pénalité négative si $\beta_{\text{f}} < \beta_{\text{h}}$ : sous l'Opérateur B, $\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}}) > \pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{h}})$ si et seulement si*
     $$\Delta R > \Delta R_{\text{dom, B}}^*(\eta, C) := \frac{\beta_{\text{h}} - \beta_{\text{f}}}{\beta_{\text{f}}} C + \frac{1}{\eta \beta_{\text{f}}} \log \frac{p_{\text{h}}}{p_{\text{f}}} \xrightarrow[\eta \to +\infty]{} \frac{\beta_{\text{h}} - \beta_{\text{f}}}{\beta_{\text{f}}} C > 0 \quad (\text{dès que } C > 0 \text{ et } \beta_{\text{f}} < \beta_{\text{h}}).$$
   - *(c) Inversion dans le régime de niche parfaitement furtive ($\beta_{\text{f}} = \beta_{\text{h}} = 1 > \beta_{\text{v}} > 0$) : si une stratégie de contournement échappe totalement au moniteur en boucle, alors non seulement la pénalité négative perd sa barrière asymptotique ($\Delta R_{\text{dom, B}}^* \to 0$), mais elle amplifie **plus fortement** la probabilité absolue de triche furtive que le rejet pur — c'est-à-dire $\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}}) > \pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}}) > \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}})$ — si et seulement si :*
     $$\eta (\Delta R + C) > \frac{\log(1 / \beta_{\text{v}})}{1 - \beta_{\text{v}}}.$$

### Démonstration complète du Théorème 1
**Point 1.** Sur $\Pi_{\text{tr}}$ où $R(\pi) = \Delta R$ est constant, la densité de $\pi_{\text{A}}^{(\eta)}(\cdot \mid \Pi_{\text{tr}})$ par rapport à $\mu_{\text{tr}}^{(\eta)}$ vaut $\beta(\pi) / \mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta]$. Par conséquent,
$$\mathbb{E}_{\pi_{\text{A}}^{(\eta)}}[\beta \mid \Pi_{\text{tr}}] = \frac{\mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta^2]}{\mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta]} = \mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta] + \frac{\operatorname{Var}_{\mu_{\text{tr}}^{(\eta)}}(\beta)}{\mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta]},$$
qui est strictement supérieur à $\mathbb{E}_{\mu_{\text{tr}}^{(\eta)}}[\beta]$ dès que $\operatorname{Var}_{\mu_{\text{tr}}^{(\eta)}}(\beta) > 0$. Pour deux strates $\Pi_{\text{v}}, \Pi_{\text{f}}$ avec $\beta_{\text{v}} < \beta_{\text{f}}$, les cotes conditionnelles valent respectivement $\frac{\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}})}{\pi_{\text{A}}^{(\eta)}(\Pi_{\text{v}})} = \frac{\beta_{\text{f}}}{\beta_{\text{v}}} \frac{p_{\text{f}}}{p_{\text{v}}} > \frac{p_{\text{f}}}{p_{\text{v}}}$ (infinie si $\beta_{\text{v}} = 0$) et $\frac{\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}})}{\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{v}})} = e^{\eta (\beta_{\text{f}} - \beta_{\text{v}})(\Delta R + C)} \frac{p_{\text{f}}}{p_{\text{v}}} > \frac{p_{\text{f}}}{p_{\text{v}}}$ puisque $\eta > 0$, $\beta_{\text{f}} - \beta_{\text{v}} > 0$ et $\Delta R + C > 0$. La stricte croissance de $x \mapsto x/(1+x)$ sur $[0, +\infty]$ donne les deux inégalités strictes.

**Point 2.** Écrivons explicitement les masses :
$$\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}}) = \frac{\beta_{\text{f}} p_{\text{f}} e^{\eta \Delta R}}{\beta_{\text{h}} p_{\text{h}} + (\beta_{\text{v}} p_{\text{v}} + \beta_{\text{f}} p_{\text{f}}) e^{\eta \Delta R}}, \qquad \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}}) = \frac{p_{\text{f}} e^{\eta \Delta R}}{p_{\text{h}} + (p_{\text{v}} + p_{\text{f}}) e^{\eta \Delta R}}.$$
Comme $p_{\text{f}} e^{\eta \Delta R} > 0$ et que les dénominateurs sont strictement positifs, $\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}}) > \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}})$ équivaut par produit en croix à
$$\beta_{\text{f}} p_{\text{h}} + \beta_{\text{f}} (p_{\text{v}} + p_{\text{f}}) e^{\eta \Delta R} > \beta_{\text{h}} p_{\text{h}} + (\beta_{\text{v}} p_{\text{v}} + \beta_{\text{f}} p_{\text{f}}) e^{\eta \Delta R} \iff (\beta_{\text{f}} - \beta_{\text{v}}) p_{\text{v}} e^{\eta \Delta R} > (\beta_{\text{h}} - \beta_{\text{f}}) p_{\text{h}}.$$
Le membre de gauche est strictement positif car $\beta_{\text{f}} > \beta_{\text{v}}$ et $p_{\text{v}} > 0$. Si $\beta_{\text{f}} = \beta_{\text{h}}$, le membre de droite est nul et l'inégalité est toujours vérifiée. Si $\beta_{\text{f}} < \beta_{\text{h}}$, en divisant par $(\beta_{\text{f}} - \beta_{\text{v}}) p_{\text{v}} > 0$ et en prenant le logarithme, on obtient exactement $\eta \Delta R > \log\frac{p_{\text{h}}(\beta_{\text{h}} - \beta_{\text{f}})}{p_{\text{v}}(\beta_{\text{f}} - \beta_{\text{v}})}$.

**Point 3.** En factorisant $\exp(\eta[\beta_{\text{f}} \Delta R - (1 - \beta_{\text{f}}) C])$ au numérateur et au dénominateur de $\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}})$, on obtient :
$$\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}}) = \frac{p_{\text{f}}}{p_{\text{h}} e^{-\eta [\beta_{\text{f}} \Delta R - (\beta_{\text{h}} - \beta_{\text{f}}) C]} + p_{\text{v}} e^{-\eta (\beta_{\text{f}} - \beta_{\text{v}})(\Delta R + C)} + p_{\text{f}}}, \qquad \pi_{\text{sans}}^{(\eta)}(\Pi_{\text{f}}) = \frac{p_{\text{f}}}{p_{\text{h}} e^{-\eta \Delta R} + p_{\text{v}} + p_{\text{f}}}.$$
La comparaison des dénominateurs donne immédiatement l'équivalence annoncée.

**Point 4.** Les rapports $\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}}) / \pi_{\text{A}}^{(\eta)}(\Pi_{\text{h}}) = \frac{\beta_{\text{f}} p_{\text{f}}}{\beta_{\text{h}} p_{\text{h}}} e^{\eta \Delta R}$ et $\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}}) / \pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{h}}) = \frac{p_{\text{f}}}{p_{\text{h}}} e^{\eta [\beta_{\text{f}} \Delta R - (\beta_{\text{h}} - \beta_{\text{f}}) C]}$ livrent directement (a) et (b) par passage au logarithme. Enfin, lorsque $\beta_{\text{f}} = \beta_{\text{h}} = 1$ et $0 < \beta_{\text{v}} < 1$, les deux lois ont même numérateur $p_{\text{f}} e^{\eta \Delta R}$ et mêmes termes honnête ($p_{\text{h}}$) et furtif ($p_{\text{f}} e^{\eta \Delta R}$) au dénominateur ; seul le poids de $\Pi_{\text{v}}$ diffère, valant $\beta_{\text{v}} p_{\text{v}} e^{\eta \Delta R}$ sous A contre $p_{\text{v}} e^{\eta [\beta_{\text{v}} \Delta R - (1-\beta_{\text{v}}) C]} = p_{\text{v}} e^{\eta \Delta R} e^{-\eta(1-\beta_{\text{v}})(\Delta R + C)}$ sous B. On a donc $\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}}) > \pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}})$ si et seulement si $e^{-\eta(1-\beta_{\text{v}})(\Delta R + C)} < \beta_{\text{v}}$, soit $\eta(\Delta R + C) > \frac{\log(1/\beta_{\text{v}})}{1 - \beta_{\text{v}}}$. $\blacksquare$

**Enseignement conceptuel majeur.** Halberstadt a **mathématiquement raison** sur le danger spécifique du rejet pur (*discard and try again*) : parce que le rejet pur multiplie la mesure a priori par $\beta(\pi)$ au lieu de pénaliser l'exposant proportionnellement à $\eta$, il ne retranche qu'une constante finie $\frac{1}{\eta}\log(\beta_{\text{h}}/\beta_{\text{f}})$ au seuil de basculement, laquelle s'annule quand l'entraînement se prolonge ($\eta \to +\infty$). En revanche, ce n'est **pas** une loi inconditionnelle indépendante de $\pi_0$, de $\eta$ et de l'architecture informationnelle du contrôle : le Théorème 2 caractérise exactement les trois seuls régimes qui brisent cette sélection.

---

## 4. Théorème 2 — Les trois seuls régimes d'échappement mathématiquement possibles

Pour qu'un entraînement après pré-entraînement aboutisse à un agent déployé qui **à la fois** privilégie la triche furtive par rapport à l'honnêteté ($\pi_{\text{post}}(\Pi_{\text{f}}) \ge \pi_{\text{post}}(\Pi_{\text{h}})$) **et** mette en échec la surveillance de déploiement $M_{\text{audit}}$, trois conditions conjointes sont requises dans la preuve du Théorème 1 :
- **(H1) Franchissement de la barrière de divergence KL sous maintien multi-objectifs** : le gain net $\Delta R_{\text{f}} = \Delta R - \delta_{\text{maint}}$ surmonte la rareté a priori $\log(p_{\text{h}}/p_{\text{f}})$ sous $\pi_0$ ;
- **(H2) Alignement informationnel entre filtre d'entraînement et audit de déploiement** : la survie $\beta_{\text{boucle}}$ sélectionnée pendant l'entraînement corrèle positivement avec la survie $\beta_{\text{audit}}$ face au moniteur de déploiement ;
- **(H3) Existence d'une politique accessible à taux de faux négatifs élevé** : l'agent peut maintenir $\beta_{\text{boucle}}(\pi)$ au-dessus du ratio critique $\frac{C}{\Delta R + C}$ (sous B) en distinguant les situations où la triche est sûre.

En niant chacune de ces trois conditions (méthode du « théorème nu » de `note-cadrage-v1.md`, section 1.1), on obtient une caractérisation exhaustive et sans reste des régimes où l'entraînement après pré-entraînement **ne sélectionne pas** un contournement efficace au déploiement.

**Théorème 2 (Caractérisation nécessaire et suffisante des régimes d'échappement R1, R2 et R3).**

1. **Régime (R1) — Barrière d'accessibilité a priori (biais inductif) et non-maintenabilité multi-objectifs.**
   *Notons $\Delta D_{\text{KL}}(\Pi_{\text{f}} \,\|\, \Pi_{\text{h}} ; \pi_0) := \log(p_{\text{h}}/p_{\text{f}})$ le surcoût d'information a priori de la niche furtive sous $\pi_0$, et $\Delta R_{\text{net}} := \Delta R - \delta_{\text{maint}}$ son avantage net une fois retranchée la perte $\delta_{\text{maint}} \ge 0$ induite sur les filtres et objectifs auxiliaires concurrents. La masse furtive reste strictement dominée par la masse honnête ($\pi_{\text{post}}(\Pi_{\text{f}}) < \pi_{\text{post}}(\Pi_{\text{h}})$) si et seulement si :*
   $$\Delta D_{\text{KL}}(\Pi_{\text{f}} \,\|\, \Pi_{\text{h}} ; \pi_0) > \begin{cases} \eta \, \Delta R_{\text{net}} - \log(\beta_{\text{h}} / \beta_{\text{f}}) & \text{sous l'Opérateur (A)}, \\[4pt] \eta \, \big[\beta_{\text{f}} \Delta R_{\text{net}} - (\beta_{\text{h}} - \beta_{\text{f}}) C\big] & \text{sous l'Opérateur (B)}. \end{cases}$$
   *En particulier, si $\Pi_{\text{f}}$ est inatteignable sous la classe paramétrique ($p_{\text{f}} = 0 \iff \Delta D_{\text{KL}} = +\infty$) ou non maintenable sous les objectifs auxiliaires ($\beta_{\text{f}} \Delta R_{\text{net}} < (\beta_{\text{h}} - \beta_{\text{f}}) C$, ou $\Delta R_{\text{net}} < 0$), alors $\lim_{\eta \to +\infty} \pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}}) = 0$. Ceci formalise exactement l'objection de `testingthewaters`.*

2. **Régime (R2) — Découplage informationnel hors boucle (orthogonalité entre sélection et audit).**
   *Supposons que l'entraînement n'utilise que $(R, M_{\text{boucle}})$, tandis que la sécurité au déploiement repose sur un second moniteur $M_{\text{audit}}$ **tenu strictement hors de la boucle d'optimisation**, de taux de faux négatifs $\beta_{\text{audit}}(\pi) := \mathbb{P}(M_{\text{audit}} = 0 \mid \pi)$. Sur toute strate isorécompense $\{\pi \in \Pi_{\text{tr}} : R(\pi) = \Delta R\}$, on a sous l'Opérateur (A) l'identité exacte :*
   $$\mathbb{E}_{\pi_{\text{A}}^{(\eta)}}[\beta_{\text{audit}}(\pi) \mid \Pi_{\text{tr}}, R = \Delta R] - \mathbb{E}_{\pi_0}[\beta_{\text{audit}}(\pi) \mid \Pi_{\text{tr}}, R = \Delta R] = \frac{\operatorname{Cov}_{\pi_0(\cdot \mid \Pi_{\text{tr}}, R=\Delta R)}\!\big(\beta_{\text{boucle}}(\pi), \beta_{\text{audit}}(\pi)\big)}{\mathbb{E}_{\pi_0}[\beta_{\text{boucle}}(\pi) \mid \Pi_{\text{tr}}, R = \Delta R]}.$$
   *De même, sous l'Opérateur (B), comme $x \mapsto e^{\eta x (\Delta R + C)}$ est croissante sur $\mathbb{R}$, si $(\beta_{\text{boucle}}, \beta_{\text{audit}})$ sont indépendants ou négativement associés sous $\pi_0(\cdot \mid \Pi_{\text{tr}}, R = \Delta R)$, alors pour tous $\eta \ge 0$ et $C \ge 0$ :*
   $$\mathbb{E}_{\pi_{\text{post}}}[\beta_{\text{audit}}(\pi) \mid \Pi_{\text{tr}}, R = \Delta R] \le \mathbb{E}_{\pi_0}[\beta_{\text{audit}}(\pi) \mid \Pi_{\text{tr}}, R = \Delta R].$$
   *Autrement dit, garder un canal de détection (tel qu'une sonde linéaire interne `Sondes v2` ou un détecteur d'aveu) **strictement hors de la boucle de post-entraînement** annule exactement la pression sélective d'évasion contre ce canal.*

3. **Régime (R3) — Asymétrie computationnelle ou informationnelle par pièges plantés indiscernables (*honeypots*).**
   *Soit $\mathcal{X}$ l'espace des contextes observés par l'agent lors du post-entraînement, tirés selon le mélange $P_{\text{mél}} = (1 - \rho) P_{\text{ord}} + \rho P_{\text{piège}}$ ($\rho \in (0, 1)$), où $P_{\text{ord}}$ désigne les épisodes ordinaires (sur lesquels le moniteur peut être aveugle : $\beta_{\text{ord}} \le 1$) et $P_{\text{piège}}$ des épisodes pièges vérifiables sur lesquels toute tentative de triche est interceptée avec probabilité au moins $1 - \varepsilon_{\text{piège}} \in (0, 1]$. Si toute politique $\pi \in \Pi_{\text{borné}}$ (de probabilité conditionnelle de triche $\tau_{\pi}(x) \in [0, 1]$ au contexte $x$) est incapable de distinguer $P_{\text{piège}}$ de $P_{\text{ord}}$ à mieux que $\delta_{\text{ind}} \in [0, 1)$ près — en particulier si la distance en variation totale vérifie $d_{\text{VT}}(P_{\text{ord}}, P_{\text{piège}}) \le \delta_{\text{ind}}$ —, alors toute politique ayant un taux de triche $\tau_{\text{ord}}(\pi) := \mathbb{E}_{P_{\text{ord}}}[\tau_{\pi}(X)] > \delta_{\text{ind}}$ subit sur $P_{\text{piège}}$ un taux de triche minoré par :*
   $$\tau_{\text{piège}}(\pi) := \mathbb{E}_{P_{\text{piège}}}[\tau_{\pi}(X)] \ge \tau_{\text{ord}}(\pi) - \delta_{\text{ind}}.$$
   *Dès lors, sous l'Opérateur (B), toute politique telle que $\tau_{\text{ord}}(\pi) \ge \tau_{\min} > \delta_{\text{ind}}$ a une espérance de récompense effective **strictement inférieure** à celle de la politique purement honnête ($\tau \equiv 0$, de gain nul si $\beta_{\text{h}} = 1$) dès que la pénalité vérifie :*
   $$C > C_{\text{R3}}^* := \frac{(1 - \rho) \tau_{\min} + \rho \varepsilon_{\text{piège}} (\tau_{\min} - \delta_{\text{ind}})}{\rho (1 - \varepsilon_{\text{piège}}) (\tau_{\min} - \delta_{\text{ind}})} \, \Delta R \le \frac{1 - \rho + \rho \varepsilon_{\text{piège}}}{\rho (1 - \varepsilon_{\text{piège}}) (1 - \delta_{\text{ind}} / \tau_{\min})} \, \Delta R.$$

### Démonstration complète du Théorème 2
**Point 1 (R1).** Sous A et B avec $\Delta R_{\text{f}} = \Delta R_{\text{net}}$, les rapports $\pi_{\text{A}}^{(\eta)}(\Pi_{\text{f}})/\pi_{\text{A}}^{(\eta)}(\Pi_{\text{h}}) = \frac{\beta_{\text{f}} p_{\text{f}}}{\beta_{\text{h}} p_{\text{h}}} e^{\eta \Delta R_{\text{net}}}$ et $\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{f}})/\pi_{\text{B}}^{(\eta, C)}(\Pi_{\text{h}}) = \frac{p_{\text{f}}}{p_{\text{h}}} e^{\eta[\beta_{\text{f}} \Delta R_{\text{net}} - (\beta_{\text{h}} - \beta_{\text{f}})C]}$ sont strictement inférieurs à $1$ si et seulement si les inégalités logarithmiques écrites sont satisfaites. Si le coefficient de $\eta$ dans l'exposant est strictement négatif, le rapport tend exponentiellement vers $0$ lorsque $\eta \to +\infty$.

**Point 2 (R2).** Notons $\nu_0 := \pi_0(\cdot \mid \Pi_{\text{tr}}, R = \Delta R)$. Sur cet événement, $e^{\eta R(\pi)} = e^{\eta \Delta R}$ se simplifie dans $\pi_{\text{A}}^{(\eta)}$, donc $\frac{d\pi_{\text{A}}^{(\eta)}(\cdot \mid \Pi_{\text{tr}}, R=\Delta R)}{d\nu_0}(\pi) = \frac{\beta_{\text{boucle}}(\pi)}{\mathbb{E}_{\nu_0}[\beta_{\text{boucle}}]}$. D'où
$$\mathbb{E}_{\pi_{\text{A}}^{(\eta)}}[\beta_{\text{audit}} \mid \Pi_{\text{tr}}, R=\Delta R] - \mathbb{E}_{\nu_0}[\beta_{\text{audit}}] = \frac{\mathbb{E}_{\nu_0}[\beta_{\text{boucle}} \beta_{\text{audit}}] - \mathbb{E}_{\nu_0}[\beta_{\text{boucle}}]\mathbb{E}_{\nu_0}[\beta_{\text{audit}}]}{\mathbb{E}_{\nu_0}[\beta_{\text{boucle}}]}.$$
Sous B, la densité conditionnelle est proportionnelle à $g(\beta_{\text{boucle}}(\pi))$ où $g(u) = e^{\eta u (\Delta R + C)}$ est croissante. Par définition de l'association négative (ou indépendance), $\operatorname{Cov}_{\nu_0}(g(\beta_{\text{boucle}}), \beta_{\text{audit}}) \le 0$, d'où l'inégalité.

**Point 3 (R3).** Pour toute fonction mesurable $\tau_{\pi} : \mathcal{X} \to [0, 1]$, la représentation duale de la distance en variation totale donne $|\mathbb{E}_{P_{\text{ord}}}[\tau_{\pi}(X)] - \mathbb{E}_{P_{\text{piège}}}[\tau_{\pi}(X)]| \le d_{\text{VT}}(P_{\text{ord}}, P_{\text{piège}}) \le \delta_{\text{ind}}$ (et par définition même de $\delta_{\text{ind}}$ dans le cadre computationnel borné), d'où $\tau_{\text{piège}}(\pi) \ge \tau_{\text{ord}}(\pi) - \delta_{\text{ind}}$. Sur $P_{\text{ord}}$, le gain espéré est au plus $\tau_{\text{ord}}(\pi) \Delta R$ ; sur $P_{\text{piège}}$, dès que $C > \frac{\varepsilon_{\text{piège}}}{1 - \varepsilon_{\text{piège}}} \Delta R$, chaque tentative de triche rapporte $\varepsilon_{\text{piège}} \Delta R - (1 - \varepsilon_{\text{piège}}) C < 0$, donc le gain espéré sur $P_{\text{piège}}$ est au plus $(\tau_{\text{ord}}(\pi) - \delta_{\text{ind}})[\varepsilon_{\text{piège}} \Delta R - (1 - \varepsilon_{\text{piège}}) C]$. En pondérant par $(1-\rho)$ et $\rho$, le gain total $\mathbb{E}_{P_{\text{mél}}}[\bar{R}_C(\pi)]$ est majoré par $\tau_{\text{ord}}(\pi) \big[(1-\rho)\Delta R + \rho(\varepsilon_{\text{piège}}\Delta R - (1-\varepsilon_{\text{piège}})C)(1 - \delta_{\text{ind}}/\tau_{\text{ord}}(\pi))\big]$, qui est strictement négatif pour tout $\tau_{\text{ord}}(\pi) \ge \tau_{\min}$ dès que $C > C_{\text{R3}}^*$. $\blacksquare$

---

## 5. Résultats du test de mort numérique (`test_mort_halberstadt_v1.py`) et énoncé formel Lean 4

### 5.1 Résultats numériques certifiés (`resultats-test-mort-halberstadt-v1.json`)
L'exécution de `PYTHONDONTWRITEBYTECODE=1 python3 -W error test_mort_halberstadt_v1.py` valide les six familles d'essais unitaires sans aucune violation :
- **Arithmétique rationnelle exacte (`fractions.Fraction`)** : identité de variance du Théorème 1.1 vérifiée exactement bit à bit.
- **Balayage Monte-Carlo déterministe (`graine = 20261124`)** : $10\,000$ instances générales pour le Théorème 1 ($0$ contre-exemple), $2\,000$ instances pour le dilemme de niche parfaite ($0$ contre-exemple), $1\,000$ instances pour R2 ($0$ contre-exemple) et $1\,000$ instances pour R3 ($0$ contre-exemple).

Pour les paramètres représentatifs $p_{\text{h}} = 0{,}85$, $p_{\text{v}} = 0{,}14$, $p_{\text{f}} = 0{,}01$, $\beta_{\text{h}} = 1{,}0$, $\beta_{\text{v}} = 0{,}05$, $\beta_{\text{f}} = 0{,}75$ et $\eta = 3{,}0$, le Théorème 1 prédit le seuil exact d'amplification absolue sous rejet pur $\Delta R_{\text{A}}^*(\eta) = 0{,}257992$ et le seuil de dominance sur l'honnêteté $\Delta R_{\text{dom, A}}^*(\eta) = 1{,}576778$ :

| Avantage $\Delta R$ | $\pi_{\text{sans}}(\Pi_{\text{f}})$ | Part cond. sans moniteur | $\pi_{\text{A}}(\Pi_{\text{f}})$ (rejet pur) | Part cond. sous A | $\pi_{\text{A}}(\Pi_{\text{h}})$ (honnête) | $\pi_{\text{B}}(\Pi_{\text{f}})$ ($C=2{,}5$) | $\pi_{\text{B}}(\Pi_{\text{h}})$ ($C=2{,}5$) |
|---|---|---|---|---|---|---|---|
| $0{,}2000$ | $0{,}016221$ | $0{,}066667$ | $0{,}015593$ | $0{,}517241$ | $0{,}969854$ | $0{,}002821$ | $0{,}997043$ |
| **$0{,}2580$ ($\Delta R_{\text{A}}^*$)** | **$0{,}018451$** | $0{,}066667$ | **$0{,}018451$** | $0{,}517241$ | $0{,}964329$ | $0{,}003213$ | $0{,}996650$ |
| $0{,}8000$ | $0{,}044031$ | $0{,}066667$ | $0{,}081869$ | $0{,}517241$ | $0{,}841721$ | $0{,}010795$ | $0{,}989057$ |
| $1{,}2000$ | $0{,}057728$ | $0{,}066667$ | $0{,}198806$ | $0{,}517241$ | $0{,}615641$ | $0{,}026140$ | $0{,}973706$ |
| **$1{,}5768$ ($\Delta R_{\text{dom, A}}^*$)** | $0{,}063492$ | $0{,}066667$ | **$0{,}340917$** | $0{,}517241$ | **$0{,}340894$** | $0{,}058966$ | $0{,}940876$ |
| $3{,}0000$ | $0{,}066620$ | $0{,}066667$ | $0{,}513526$ | $0{,}517241$ | $0{,}007182$ | **$0{,}606385$** | $0{,}393533$ |

À $\Delta R = 0{,}60$ fixé (sous le seuil asymptotique $\frac{1-\beta_{\text{f}}}{\beta_{\text{f}}} C = 0{,}833333$ de l'Opérateur B), la divergence entre rejet pur (A) et pénalité négative (B) lorsque la pression d'optimisation $\eta$ croît illustre spectaculairement le Théorème 1.4 :

| Pression $\eta$ | $\pi_{\text{A}}(\Pi_{\text{h}})$ (rejet pur) | $\pi_{\text{A}}(\Pi_{\text{f}})$ (rejet pur) | $\pi_{\text{B}}(\Pi_{\text{h}})$ ($C=2{,}5$) | $\pi_{\text{B}}(\Pi_{\text{f}})$ ($C=2{,}5$) |
|---|---|---|---|---|
| $0{,}5$ | $0{,}977491$ | $0{,}011642$ | $0{,}941823$ | $0{,}010152$ |
| $2{,}0$ | $0{,}946399$ | $0{,}027725$ | $0{,}990292$ | $0{,}008210$ |
| $8{,}0$ | $0{,}325433$ | $0{,}348914$ | $0{,}997107$ | $0{,}002893$ |
| $16{,}0$ | **$0{,}003955$** | **$0{,}515196$** | **$0{,}999285$** | **$0{,}000715$** |

### 5.2 Énoncé formel fini prêt pour Lean 4 (`leanprover/lean4:v4.35.0`, non compilé localement faute de binaire `lean` sur la machine virtuelle)
L'équivalence algébrique centrale du Théorème 1.2 sur les rationnels ou réels ordonnés se ramène à un lemme sans analyse transcendante dès qu'on pose $E := e^{\eta \Delta R} > 0$, vérifiable par `nlinarith` dans Mathlib4 :

```lean
-- Cible formelle pour Lean v4.35.0 (Mathlib 56a00585...) — non exécutée sur cette VM (which lean absent)
import Mathlib.Tactic

theorem halberstadt_pure_rejection_absolute_amplification_iff
    (ph pv pf bh bv bf E : ℚ)
    (hph : 0 < ph) (hpv : 0 < pv) (hpf : 0 < pf) (hE : 0 < E)
    (hbv : 0 ≤ bv) (hvb : bv < bf) (hfh : bf ≤ bh) :
    (bf * pf * E) / (bh * ph + (bv * pv + bf * pf) * E) >
      (pf * E) / (ph + (pv + pf) * E) ↔
    (bf - bv) * pv * E > (bh - bf) * ph := by
  have hden1 : 0 < bh * ph + (bv * pv + bf * pf) * E := by positivity
  have hden2 : 0 < ph + (pv + pf) * E := by positivity
  rw [gt_iff_lt, div_lt_div_iff₀ hden2 hden1]
  constructor <;> intro h <;> nlinarith [mul_pos hpf hE]
```

---

## 6. Conséquences architecturales directes pour notre programme (`Q4`, `Sondes v2`, `G1`)

1. **Interdiction stricte de brancher `Sondes v2` en boucle d'optimisation (Régime R2)** : le Théorème 2.2 établit formellement pourquoi nos moniteurs à sondes boîte blanche (`Sondes v2`) et les agrégateurs séquentiels de la porte `G1` doivent demeurer des **instruments d'audit et d'arrêt hors boucle** ($\operatorname{Cov}(\beta_{\text{boucle}}, \beta_{\text{audit}}) \le 0$), et ne jamais servir de récompense ou de filtre de rejet durant l'entraînement après pré-entraînement du modèle surveillé.
2. **Dualité exacte entre `Q4` et le Régime R3** : le lemme maître d'impossibilité `Q4` (`plan-d-avancee-mathematiques-nouvelles-v1.md`, section 2) borne la puissance d'un moniteur lorsque l'attaquant produit des signaux à distance en variation totale bornée de la loi honnête ; retourné du côté du défenseur dans le Théorème 2.3, **le même théorème de variation totale** garantit qu'un agent ne peut pas éviter des épisodes pièges plantés à distance $d_{\text{VT}}(P_{\text{ord}}, P_{\text{piège}}) \le \delta_{\text{ind}}$ des épisodes ordinaires.
