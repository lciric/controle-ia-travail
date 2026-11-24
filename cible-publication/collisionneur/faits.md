# Faits techniques — Résultat théorique sur le filtrage en boucle pendant l'entraînement après pré-entraînement

## 1. Contenu mathématique établi dans le manuscrit de départ

Un manuscrit théorique court étudie l'effet de l'utilisation d'un détecteur imparfait de désalignement à l'intérieur de la boucle d'entraînement après pré-entraînement d'un modèle génératif.

1. **Cadre formel à trois régimes et deux opérateurs** :
   - L'espace des politiques $\Pi$ est partitionné en trois sous-ensembles disjoints : politiques honnêtes $\Pi_{\mathrm{h}}$ (récompense $R_0$), politiques de contournement visibles $\Pi_{\mathrm{v}}$ (récompense $R_0 + \Delta R$ avec $\Delta R > 0$, probabilité de survie au détecteur en boucle $\beta_{\mathrm{v}}$) et politiques de contournement furtives $\Pi_{\mathrm{f}}$ (même bonus $\Delta R$, probabilité de survie $\beta_{\mathrm{f}}$ avec $0 \le \beta_{\mathrm{v}} < \beta_{\mathrm{f}} \le \beta_{\mathrm{h}} \le 1$).
   - À partir d'une loi a priori $\pi_0$ (modèle pré-entraîné) et d'une intensité d'optimisation $\eta > 0$ (inverse du coefficient de pénalité de divergence de Kullback-Leibler par rapport à $\pi_0$), deux opérateurs sont comparés :
     - **Opérateur A (rejet pur sans pénalité négative)** : $\pi_{\mathrm{A}}^{(\eta)}(\pi) \propto \beta(\pi) e^{\eta R(\pi)} \pi_0(\pi)$.
     - **Opérateur B (optimisation régularisée par divergence de Kullback-Leibler avec pénalité $-C \le 0$ en cas de détection)** : $\pi_{\mathrm{B}}^{(\eta, C)}(\pi) \propto e^{\eta [\beta(\pi) R(\pi) - (1 - \beta(\pi)) C]} \pi_0(\pi)$.

2. **Résultats démontrés dans le manuscrit actuel** :
   - **Enrichissement conditionnel et seuils exacts** : dès que la variance de $\beta$ parmi les politiques de contournement est strictement positive, la part conditionnelle de contournement furtif parmi les tricheurs croît strictement sous A comme sous B. Sous rejet pur (A), la probabilité absolue de $\Pi_{\mathrm{f}}$ dépasse celle sans détecteur au-delà d'un seuil explicite $\Delta R_{\mathrm{A}}^*(\eta)$, et le seuil de dominance sur $\Pi_{\mathrm{h}}$ tend vers $0$ lorsque $\eta \to +\infty$ dès que $\beta_{\mathrm{f}} > 0$. Sous pénalité négative (B), un plancher positif $\frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C$ apparaît si $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$, mais s'il existe une niche parfaitement furtive ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$), la pénalité négative amplifie strictement plus $\Pi_{\mathrm{f}}$ que le rejet pur.
   - **Trois mécanismes d'atténuation analysés** :
     - *(Barrière d'accessibilité et coût de maintien)* : condition nécessaire et suffisante exacte dans le modèle à trois régimes liant $\log(\pi_0(\Pi_{\mathrm{h}})/\pi_0(\Pi_{\mathrm{f}}))$ au gain net diminué d'un coût de maintien multi-objectifs.
     - *(Découplage hors boucle)* : identité exacte de covariance (sous A) et condition suffisante d'association négative ou d'indépendance (sous B) garantissant qu'un instrument d'audit tenu hors de la boucle d'optimisation ne subit pas d'augmentation du taux de faux négatifs.
     - *(Épisodes pièges dans une extension contextuelle)* : borne par distance en variation totale montrant qu'une fraction $\rho$ d'épisodes vérifiés de distance en variation totale $\delta_{\mathrm{ind}}$ aux épisodes ordinaires impose un taux minimal d'interception $\max(0, \tau_{\mathrm{ord}} - \delta_{\mathrm{ind}})$, inopérant lorsque $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$.
   - **Vérification numérique** : script autonome vérifiant les identités en arithmétique rationnelle exacte et sur $14\,000$ tirages aléatoires de paramètres sans contre-exemple. Aucune expérience sur réseaux de neurones réels ni formalisation compilée dans un assistant de preuve ne figure pour l'instant dans le manuscrit.

## 2. Paramètres éditoriaux et scientifiques ouverts

Les grandes conférences d'apprentissage automatique (ICML, NeurIPS, ICLR), de théorie de l'apprentissage (COLT, ALT), de sécurité de l'apprentissage (IEEE SaTML, conférences de sécurité informatique) et les revues (JMLR, TMLR) appliquent des critères très différents quant à la profondeur technique des preuves exigée (algèbre d'équilibre de Gibbs finie contre dynamique d'apprentissage ou bornes minimax séquentielles), à la nécessité d'expériences sur modèles ouverts et aux règles d'anonymat vis-à-vis de billets publics préalables.
