BASSIN_MATH: Déficience-Aléatoire-MartinLöf-SlepianWolf-Solomonoff (DAMS-Swarm)
LOI_PROPOSEE: L'essaim maximise la déficience d'aléatoire conjointe de Martin-Löf sous contrainte de codage distribué de Slepian-Wolf entre sous-graphes bibliographiques disjoints, via une allocation budgétaire gouvernée par le gain de compression de la mesure universelle de Solomonoff.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Les agents opèrent comme des codeurs distribués sans communication (théorème de Slepian-Wolf) sur des silos disjoints $X, Y$ du graphe de citations gratuit. L'état hors-poids de l'essaim est un dictionnaire de préfixes $D_t$ maintenu par élagage radical. Le classifieur gratuit `jev-1.14.0` approxime la probabilité a priori algorithmique de Solomonoff $M(x) = \sum_{p: U(p)=x*} 2^{-|p|}$ en mesurant la surprise cross-entropique d'un pont candidat $(x,y)$ conditionnellement à $D_t$. 
L'allocation du budget asymétrique ($B_{\text{Gemini}}=20\$$ pour l'extraction de lemmes compressés, $B_{\text{Claude}}=100\$$ pour la synthèse de programmes de traduction $p_{X \leftrightarrow Y}$) suit le gradient de la **déficience d'aléatoire de Martin-Löf** $\delta(x,y | D_t) = -\log_2 M(x,y | D_t) - K(x,y | D_t)$, estimée gratuitement par `jev-1.14.0` via la chute de longueur de code minimale (MDL) lors de la fusion de deux arbres de citations :
$$w_i(t+1) = w_i(t) \cdot \exp\left(\eta \cdot \frac{\Delta \delta_i(x,y | D_t)}{\text{Coût}_{\text{API}}(i)}\right)$$
Seuls les paires $(x,y)$ franchissant un seuil critique de déficience d'aléatoire (régularité algorithmique cachée) déclenchent un appel payant à Claude.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(x, y, H_A, H_B) = \underbrace{\left(1 - \frac{I_{\text{cite}}(X;Y)}{\min(H(X), H(Y))}\right)}_{\text{Distance Slepian-Wolf inter-silos}} \times \underbrace{\left[\delta(x,y) - (\delta(x) + \delta(y))\right]}_{\text{Synergie de Martin-Löf (Anti-vernis)}} \times \underbrace{D_{\text{KL}}\left(M(\mathcal{O} \mid \text{do}(H_A)) \,\|\, M(\mathcal{O} \mid \text{do}(H_B))\right)}_{\text{Falsifiabilité causale } H_A \perp H_B}$$
Le vernis verbal augmente $K(x,y)$ sans réduire $-\log_2 M(x,y)$, annulant le
