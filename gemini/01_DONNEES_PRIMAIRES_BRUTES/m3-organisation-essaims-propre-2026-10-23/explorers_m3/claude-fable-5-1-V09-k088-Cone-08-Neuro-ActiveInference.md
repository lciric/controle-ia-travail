BASSIN_MATH: Rejeu-Hippocampique-Successeur-Veille-Sommeil (RHSVS)
LOI_PROPOSEE: Topologie $A_{t+1}=\arg\min_A \sum_{i}\big[\underbrace{D_{KL}(q_i(s|A)\,\|\,p(s|C_0))}_{risque/dérive}-\underbrace{I(o_i;\theta_{fam})}_{gain\ épistémique}\big]$, apprise en phase « sommeil » par rejeu priorisé $P(\text{rejeu}_k)\propto |\delta_k|^{\alpha}$ sur la représentation successeur $M=(I-\gamma T)^{-1}$ du graphe de tâches.

**1. Mécanisme.** L'essaim alterne deux phases, sans gradient sur les poids. *Veille* : chaque agent $i$ reçoit un modèle génératif (prompt) et agit en minimisant l'énergie libre attendue $G_i=\m
