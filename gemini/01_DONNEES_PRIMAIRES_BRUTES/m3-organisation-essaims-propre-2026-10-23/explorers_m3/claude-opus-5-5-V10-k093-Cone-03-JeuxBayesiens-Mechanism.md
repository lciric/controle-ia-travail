BASSIN_MATH: Sérum de Vérité Bayésien Prelec à Surprise Inter-Familles (SVB-SIF)

LOI_PROPOSEE: $S_i=\sum_k x_{ik}\log\frac{\bar x_k}{\bar y_k}+\alpha\sum_k \bar x_k\log\frac{y_{ik}}{\bar x_k}$, avec $\log\bar y_k=\frac1n\sum_j\log y_{jk}$. Le budget suit $w_f\propto \exp(\eta\,\bar S_f/\text{USD}_f)$, sous les plafonds 100 USD pour Claude et 20 USD pour Gemini.

1. **Auto-organisation hors-poids**
Chaque agent $i$ rend deux éléments :
- sa réponse $x_i$ ;
- sa prédiction $y_i$ de la distribution des réponses des autres familles.

Le premier terme de $S_i$ récompense une réponse plus fréquente que prévu, ce qui est la signature du « surprisingly popular ». Une erreur partagée par poids communs (`H4'`) est prédite par sa propre famille, donc elle n'est pas surprenante et rapporte peu.

La topologie se règle sur l'écart $\Delta_k=\bar x_k-\bar y_k$ :
- **Explorateur.** Si $\max_k|\Delta_k|>\tau$ entre familles, on spawne un explorateur chimérique sur l'hypothèse $k$.
- **Démolisseur Red-Team.** Si le consensus a $\Delta<0$ (réponse populaire mais attendue, signe de récitation), on spawne un démolisseur Red-Team.
- **Monoculture ou chimère.** Si la divergence $D_{KL}(y^{\text{Claude}}\|y^{\text{Gemini}})$ est faible, on garde la monoculture, moins chère. Sinon, on passe en chimère.

Contre la dérive `H9`, chaque sous-agent prédit la consigne originelle. Un faible score $\alpha$ sur ce terme coupe la branche de délégation. L'apprentissage passe uniquement par une mémoire de contexte : on conserve les prompts et routages de $S$ élevé, sans aucun réentraînement des poids.

2. **Fonction objectif et anti-Goodhart**
$$R=\mathbb E[S_i]+\lambda\,\mathbb 1_{\text{audit}}\log p_i(\text{jev})-\mu\,\big|\operatorname{corr}(S_i,\phi_{\text{jev}})\big|$$
- **Audit caché.** L'audit `jev-1.14.0` est tiré avec une probabilité $q$ et reste caché. Les agents ne voient jamais ses sorties, donc le log-score propre ne peut pas être optimisé directement.
- **Pénalité de corrélation.** La pénalité $\mu$ punit l'alignement sur les traits lexicaux $\phi$ du juge.
- **Incitation honnête.** Le SVB est compatible avec l'incitation à l'équilibre bayésien lorsque le prior est commun et $n$ est grand. Il ne nécessite pas de vérité terrain.

3. **Duel décisif ($H_A\perp H_B$)**
Le budget est fixé à 120 USD par bras. Les tâches sont construites à partir d'articles arXiv postérieurs au cutoff des modèles, avec une vérité vérifiée via Semantic Scholar et Crossref, ce qui neutralise la récitation.

Bras comparés :
- (A) SVB-SIF adaptatif ;
- (B) topologie fixe ;
- (C) tirages i.i.d. des mêmes modèles ;
- (N) contrôle négatif : SVB dont les prédictions $y$ sont permutées aléatoirement entre agents.

Hypothèses :
- **$H_A$ :** A bat B et C en exactitude, avec un test apparié préenregistré et $\alpha=0{,}01$.
- **$H_B$ :** N n'est pas meilleur que C.

Si N égale A, le gain venait de l'adaptivité seule et non de l'information de surprise : la loi est réfutée. La validation exige à la fois $H_A$ vrai et $H_B$ vrai.
