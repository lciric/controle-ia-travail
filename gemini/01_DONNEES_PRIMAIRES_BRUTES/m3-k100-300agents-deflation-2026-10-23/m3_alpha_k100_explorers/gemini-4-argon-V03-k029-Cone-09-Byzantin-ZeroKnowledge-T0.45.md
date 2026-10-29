BASSIN_MATH: SommeCheck-GKR-ArbreDeKarp-Bracha
LOI_PROPOSEE: L'essaim organise la littérature en circuit arithmétique stratifié $\mathcal{C}$ de profondeur $d$ et converge hors-poids via le protocole de vérification interactive Goldwasser-Kalai-Rothblum (GKR) couplé à une diffusion fiable de Bracha déterministe exécutée gratuitement par `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Le graphe de citations gratuit est compilé en un circuit arithmétique sur $\mathbb{F}_p$ où la couche $l \in \{0..d\}$ regroupe des articles en silos thématiques. Les agents génératifs (Gemini : $20\$$, feuilles d'exploration ; Claude : $100\$$, nœuds d'agrégation profonds) agissent comme prouveurs non-fiables cherchant à synthétiser des ponts mécanistes. `jev-1.14.0` agit comme vérificateur GKR à budget illimité : à chaque couche $l$, il exécute le protocole *Sum-Check* sur l'extension multilinéaire $\tilde{V}_l : \mathbb{F}_p^k \to \mathbb{F}_p$ des scores de validité causale :
$$\sum_{x, y \in \{0,1\}^k} \tilde{a}_l(z, x, y) \left( \tilde{V}_{l+1}(x) \oplus \tilde{V}_{l+1}(y) \right) = \tilde{V}_l(z)$$
Où $\tilde{a}_l$ est le prédicat de câblage structural évalué sans coût par `jev-1.14.0`. Si un sous-essaim hallucine (faute byzantine), l'erreur de somme localise la porte défaillante par dichotomie en $\mathcal{O}(\log |\mathcal{C}|)$ requêtes `jev-1.14.0`. L'allocation budgétaire $B_i(t)$ suit une diffusion de Bracha : un pont n'active un appel payant à Claude que s'il franchit les seuils $(n-t)$ d'échos `jev` sur des sous-graphes de citations disjoints, éliminant toute collusion sémantique.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(H_A, H_B) = d_{\text{Spec}}(u,v) \cdot \left( \min_{r \in \mathbb{F}_p^k} |\tilde{V}_{H_A}(r) - \tilde{V}_{H_B}(r)| \right) \cdot \mathbb{I}\left[\text{Rang}_{\text{JEV}}(M_{A \land B}) = 0\right]$$
Où $d_{\text{Spec}}(u,v)$ est la distance spectrale dans le graphe de citations entre silos $u$ et $v$, le second terme mesure la divergence de Schwartz-Zippel entre les polynômes de prédiction expérimentale sur Llama-3.1-8B/70B, et $M_{A \land B}$ est la matrice de co-satisfiabilité évaluée par `jev
