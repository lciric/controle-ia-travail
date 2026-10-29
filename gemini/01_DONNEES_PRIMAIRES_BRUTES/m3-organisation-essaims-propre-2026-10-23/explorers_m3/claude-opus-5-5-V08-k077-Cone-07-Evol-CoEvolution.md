BASSIN_MATH: Principe de Fisher à Investissement Croisé Explorateur-Démolisseur (PF-ICED)

LOI_PROPOSEE: Chaque découverte validée exige un producteur E (explorateur) et un démolisseur R (Red-Team). Son crédit V est donc partagé ½/½, d'où w_E = V/(2C_E) et w_R = V/(2C_R). La dynamique réplicateur-mutateur s'écrit ẋ_i = Σ_j x_j w_j Q_ji − x_i w̄. Elle converge vers l'équilibre de Fisher C_E* = C_R* : les dépenses totales s'égalisent, et non les effectifs.

1. **Mécanisme d'auto-organisation hors-poids**
- **Génome** : g = (consigne, rôle, famille, profondeur de délégation). Il mute par réécriture de prompt, selon la matrice Q.
- **Spawn** : le rôle rare gagne une valeur marginale plus élevée. Si C_E > C_R, l'essaim engendre des démolisseurs, sinon des explorateurs. La sex-ratio fishérienne fait office de thermostat.
- **Topologie** : E parle uniquement à R, et R parle uniquement à E. Cette co-évolution hôte-parasite est bipartite et interdit les échos intra-rôle.
- **Monoculture ou chimère** : on mesure la « parenté » κ_ij comme la corrélation d'erreurs estimée par jev-1.14.0 (H4'). L'accouplement E-R est consanguin si κ > κ* et se paie alors par la dépression V(1−κ). La chimère n'est donc retenue que là où elle décorrèle effectivement.
- **Budget** : la règle d'égalisation s'applique séparément à chaque pool, Claude (100 USD) et Gemini (20 USD).
- **Archive** : une grille MAP-Elites indexée par (famille, profondeur, sous-domaine) préserve un élite par cellule.

2. **Fonction objectif et anti-Goodhart**

Décomposition de Price : Δz̄ = Cov(w,z)/w̄ + E[wΔz]/w̄.
- Le terme de transmission E[wΔz] mesure la dérive de consigne à travers les délégations (H9). On le mesure par la distance jev entre la consigne racine et la consigne transmise.

Récompense :

R = V_vérif · (1 − κ̄) · 𝟙[nouvelle cellule ∨ amélioration] − λ|E[wΔz]| − μ·Rec

- **V_vérif** : une affirmation n'est validée que si elle survit à l'attaque R et à une vérification par graphe (arXiv, Semantic Scholar, Crossref) d'identifiants réels.
- **Rec** : taux de récitation, c'est-à-dire de références introuvables ou antérieures à l'horizon de connaissance déclaré.
- **Anti-Goodhart** : la rubrique jev change à chaque génération et reste cachée aux agents. Un audit croisé inter-famille sur 5 % des cas tirés au hasard permet de pénaliser tout écart jev/audit.

3. **Duel décisif (H_A ⊥ H_B), à budget constant de 120 USD**

Quatre bras, avec 10 graines chacun et un pré-enregistrement :
- **A** : PF-ICED.
- **B** : topologie fixe à ratio E:R = 1:1 en effectifs.
- **C** : agents i.i.d. sans rôles.
- **Contrôle négatif D** : PF-ICED avec crédit permuté aléatoirement entre E et R, ce qui détruit le signal fishérien.

Hypothèses :
- **H_A** : A dépasse B, C et D en QD-score de découvertes vérifiées non récitées, et C_E/C_R → 1 ± 0,1.
- **H_B** (réfutation) : si D ≈ A, l'avantage provient du simple bruit de mutation, et non de la loi.

Statistiques : test de permutation, α = 0,01, correction de Holm. On vérifie aussi que |E[wΔz]| est plus faible dans A que dans B.
