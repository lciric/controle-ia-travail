BASSIN_MATH: Mécanisme-Ostrovsky-Lambert-Bickel-Shaked-Rayo-Segal (OL-BS-RS)
LOI_PROPOSEE: L'auto-organisation de l'essaim est un jeu d'agrégation d'informations séparables au sens d'Ostrovsky avec divulgation partielle de Rayo-Segal et règles de score sphériques de Bickel, où `jev-1.14.0` opère un filtrage préliminaire à coût nul avant l'arbitrage par contrats de pari de Lambert.

1. **Loi d'apprentissage & d'auto-organisation hors-poids (OL-BS-RS)** :
Soit un état de vérité latent $\omega \in \{H_A, H_B\}$ sur la validité causale d'un pont inter-études.
- **Pré-filtrage Rayo-Segal gratuit (`jev-1.14.0` + API)** : L'espace des paires d'articles $(u, v)$ extraits du graphe de citations est partitionné par `jev-1.14.0` qui agit comme un émetteur de Rayo-Segal. Il maximise le produit pertinence $\times$ non-trivialité en regroupant les paires dans des signaux de divulgation partielle $\pi(s | u,v)$, rejetant 99.9% du bruit sans dépenser un centime de LLM.
- **Agrégation séquentielle d'Ostrovsky & Auto-financement de Lambert** : Les signaux survivants $s$ ouvrent un marché prédictif séquentiel. Les agents Gemini ($0.02\$$/passe, éclaireurs chimériques) et Claude ($0.25\$$/passe, synthétiseurs profonds) parient séquentiellement leur allocation budgétaire $w_i$ via des contrats auto-financés de Lambert. Par le théorème de séparabilité d'Ostrovsky, la croyance publique $p_t \in [0,1]$ converge vers $\omega$. L'allocation hors-poids évolue par sélection réplicatrice sur le score sphérique de Bickel :
$$w_{i, t+1} = w_{i,t} + \eta \left[ \frac{p_{i,t}(\omega)}{\|p_{i,t}\|_2} - \sum_{j} \frac{w_{j,t} p_{j,t}(\omega)}{\|p_{j,t}\|_2} \right]$$
Claude n'est invoqué que lorsque la volatilité martingale $|p_t - p_{t-1}|$ dépasse un seuil critique d'incertitude de Shaked.

2. **Fonction objectif anti-vernis** :
Le gain d'un pont $(u,v)$ combine la distance géodésique bibliométrique $d_{cit}(u,v)$, l'orthogonalité sémantique sous `jev-1.14.0`, et le gain d'information de Shaked-DeGroot sous score sphérique :
$$\mathcal{J}(u,v) = \log(1 + d_{cit}(u,v)) \cdot \left(1 - \cos(\vec{e}_{jev}(u), \vec{e}_{jev}(v))\right) \cdot \mathbb{E}_{\pi}\left[
