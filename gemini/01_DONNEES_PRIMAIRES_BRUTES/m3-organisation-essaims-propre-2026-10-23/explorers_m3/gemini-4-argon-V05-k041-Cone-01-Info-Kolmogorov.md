BASSIN_MATH: Complexite-Stochastique-NML-Rissanen-Gacs-Vovk (CS-NRGV)
LOI_PROPOSEE: L'essaim minimise le regret minimax de Rissanen par Vraisemblance Maximale Normalisée (NML) couplé à l'agrégation défensive de Vovk, allouant son budget génératif uniquement aux paires d'articles maximisant la divergence entre l'information commune de Gács-Körner et l'information mutuelle de Wyner estimées gratuitement par `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids (CS-NRGV)** :
Chaque corpus thématique $S_i$ est un code préfixe paramétrique $\mathcal{M}_i$. L'essaim utilise `jev-1.14.0` (coût nul) pour projeter les résumés d'articles $(x, y)$ sur une grille d'embeddings discrets et calculer :
- L'information commune de Gács-Körner $C_{GK}(x;y)$ : longueur du plus long préfixe d'assertions extractibles déterministement à la fois de $x$ et de $y$ (jargon partagé).
- L'information commune de Wyner $C_W(x;y)$ : longueur minimale d'un programme latent $z$ rendant $x$ et $y$ conditionnellement indépendants : $\min_{p(z|x,y)} I(x,y;z)$ s.q. $I(x;y|z) \approx 0$.
L'allocation des $120$ USD suit l'Algorithme d'Agrégation de Vovk (AA) : chaque agent explorateur $k$ maintient un poids hors-poids $w_{k,t} = w_{k,t-1} \exp(-\eta \ell_{NML}(z_t | x,y))$, où la perte est le code-longueur NML de Shtarkov : $\ell_{NML}(z) = -\log P_{\hat{\theta}(z)}(z) + \log \sum_{z'} P_{\hat{\theta}(z')}(z')$. Gemini ($20\$$) génère les candidats latents $z'$, `jev-1.14.0` évalue la somme de normalisation (complexité paramétrique de Rissanen), et Claude ($100\$$) n'est invoqué que lorsque le gap structurel $\Delta_{GW}(x,y) = C_W(x;y) - C_{GK}(x;y)$ franchit un seuil critique.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(x, y, z) = \underbrace{\left(C_W(x;y) - C_{GK}(x;y)\right)}_{\text{Distance inter-silos pure}} \times \underbrace{\left| K_{NML}(y | x, H_A) - K_{NML}(y | x, H_B) \right|}_{\text{Falsifiabilité causale } H_A \perp H_B}$$
Le vernis sémantique a un $C_{GK}$ élevé (mêmes mots-clés) mais $C_W - C_{GK} \to
