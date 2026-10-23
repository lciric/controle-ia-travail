**BASSIN_MATH:** Sérum-de-Vérité-Bayésien-Chimérique (SVBC)

**LOI_PROPOSEE:** Chaque agent $i$ (modèle $m_i$) émet sur la tâche $t$ une réponse $x_i\in\mathcal{K}$ et une prédiction $y_i\in\Delta(\mathcal{K})$ de la distribution des réponses des autres. Score (Prelec, règle propre sans juge) :
$$s_i=\underbrace{\log\frac{\bar x_{k=x_i}}{\bar y_{k=x_i}}}_{\text{surprise commune}}+\alpha\sum_k \bar x_k\log\frac{y_i^k}{\bar x_k},\quad \bar x=\text{fréquence empirique},\ \bar y=\text{moy. géom. des }y_j.$$
Allocation : $\max_{\text{top
