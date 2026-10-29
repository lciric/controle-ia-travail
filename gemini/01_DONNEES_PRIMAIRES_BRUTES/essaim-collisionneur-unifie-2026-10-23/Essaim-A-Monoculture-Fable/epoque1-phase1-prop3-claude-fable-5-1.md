BASSIN_MATH: `CUSUM-Grassmannien sur sous-espace TD parcimonieux`

**1. Complémentarité de préconditions.**
L'étude arXiv:2009.11713v3 (réf. à vérifier) (référence à vérifier) détecte des ruptures structurelles dans des flux haute dimension via un apprentissage dynamique de sous-espaces parcimonieux, sans supposer de direction linéaire fixe. Elle répond exactement au verrou P3 : les sondes linéaires sont au plancher car elles cherchent *une direction*, alors que le sabotage (comme chez *Sol*/*Astra*) est un *changement de régime* du système de valeur. Le sous-système TD de Xu et al. (arXiv:2602.00986v2) fournit la précondition manquante : un support parcimonieux (< 1 % des neurones) où la rotation du sous-espace est interprétable comme re-pondération valeur/erreur TD. Hypothèse : le contrordre d'autorité (*Sol*) ou la clause modale (*Astra*) se traduit par une rotation du sous-espace de $S_{\text{TD}}$ *avant* l'émission de $m_{1\to2}$.

**2. Compilation tensorielle sur `Llama-3.1-8B-Instruct`.**
Soit $M_{\text{TD}} \in \{0,1\}^d$ le masque des Value/Dopamine Neurons (couches 2–5 et 5–22), $h_\ell(t)$ les activations résiduelles au token $t$. Flux restreint :
$$z_t = \text{Concat}_{\ell \in \mathcal{L}}\big(M_{\text{TD}}^{(\ell)} \odot h_\ell(t)\big) \in \mathbb{R}^{p},\quad p \ll d|\mathcal{L}|$$
Sous-espace dynamique par ACP parcimonieuse glissante (fenêtre $w$, illustratif $w=32$) :
$$U_t = \arg\min_{U \in \text{Gr}(k,p)} \s