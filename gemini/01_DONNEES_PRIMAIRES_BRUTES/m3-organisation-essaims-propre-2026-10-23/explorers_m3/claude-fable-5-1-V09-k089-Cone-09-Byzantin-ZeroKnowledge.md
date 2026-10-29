BASSIN_MATH: Dispersion-Reed-Solomon-Commit-Révélation-Accusation (DRCA)

LOI_PROPOSEE: Tâche $T$ encodée en polynôme $P_T$ de degré $k-1$ sur $\mathbb{F}_q$ ; l'essaim de $n$ agents reçoit $n$ évaluations (dispersion d'information de Rabin) avec $n \ge 3\hat f+1$, $k = n-2\hat f$ ; décodage Berlekamp-Welch tolère $\hat f$ shards byzantins ; $\hat f_{t+1} = \hat f_t + \eta(\text{accusations prouvées} - \hat f_t)$.

**1. Auto-organisation hors-poids.** Chaque agent *s'engage* (hash $h_i = H(\text{réponse}_i \| \text{consigne})$) avant toute lecture des pairs (commit-révélation : tue sycophantie et collusion), puis révèle
