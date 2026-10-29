BASSIN_MATH: Kolmogorov-Chaitin-Schnorr-PrefixTree-Swarm (KCS-PTS)
LOI_PROPOSEE: Maximiser la divergence de complexité à ressource bornée de Schnorr sur un arbre de préfixes (Tunstall-Krichevsky-Trofimov) par compression croisée d'articles distants, filtrée par martingales constructives sur `jev-1.14.0`.

1. **Loi d'apprentissage & auto-organisation hors-poids** : L'essaim maintient un arbre de préfixes auto-adaptatif $\mathcal{T}$ (code de Tunstall dynamique) sur le graphe bibliographique gratuit. Chaque nœud $v \in \mathcal{T}$ agrège les résumés d'articles d'un sous-domaine via l'estimateur universel de Krichevsky-Trofimov $P_{KT}(x^n) = \frac{\prod_{a} (\tau_a - 1/2)!}{(n + |\Sigma|/2)!}$. `jev-1.14.0` (illimité) agit comme une martingale constructive de Schnorr $d(v)$ élaguant les branches où la complexité à temps borné $K^t(y|x)$ stagne (bruit ou redondance). Allocation budgétaire :
   - **0 USD** : `jev-1.14.0` calcule la longueur de code croisée $L_{KT}(A|B) = -\log_2 P_{KT}(A|B)$ sur des millions de paires $(A,B)$ à distance géodésique $d_{cit}(A,B) \ge 4$.
   - **20 USD (Gemini)** : Synthèse de programmes candidats $p$ (prompts d'hypothèses) aux feuilles de $\mathcal{T}$ maximisant la chute de complexité $K^t(A) - K^t(A|B, p)$.
   - **100 USD (Claude)** : Déploiement ciblé uniquement lorsque la martingale $d(v)$ franchit le seuil critique $2^{\Delta L_{KT}} > \tau$, pour compiler le protocole expérimental exact sur Llama-3.1-8B/70B.

2. **Fonction objectif anti-vernis** :
   $$\mathcal{J}(A, B, p) = \underbrace{\left(1 - \frac{L_{KT}(A \mid B, p) + L_{KT}(B \mid A, p)}{L_{KT}(A) + L_{KT}(B)}\right) \cdot d_{cit}(A,B)}_{\text{Compression croisée inter-silos}} \times \underbrace{\left| \log_2 \frac{P_{KT}(D_{\text{Llama}} \mid H_A)}{P_{KT}(D_{\text{Llama}} \mid H_B)} \right| - |p|_{\text{préfixe}}}_{\text{Falsifiabilité causale MDL } (H_A \perp H_B)}$$
   Le terme $-|p|_{\text{préfixe}}$ pénalise implacablement le vernis verbal (les longs prompts verbeux sans pouvoir compressif sur les activations $D_{\text{Llama}}$).

3. **Pont inédit & Duel ($H_A \perp H_B$)** :
   - **Ét
