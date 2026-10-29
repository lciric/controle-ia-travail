**BASSIN_MATH:** Compression-Différentielle-Wyner (CDW)

**LOI_PROPOSEE:** L'essaim minimise la longueur de code à deux parties $\mathcal{L}(S)=K(S)+\sum_i K(y_i\mid S)$ sous contrainte $C_W(y_i;y_j)\le\tau$ (information commune de Wyner entre agents), où $S$ est la structure partagée (topologie + plan) et $y_i$ les sorties ; chaque mutation de topologie est acceptée ssi $\Delta\mathcal{L}/\Delta\$ < 0$.

**1. Mécanisme.** Les complexités sont approximées par le compresseur gelé `jev-1.14.0` (NCD : $K(x\mid y)\approx C(xy)-C(y)$). Règles :
(a) *Spawn explorateur* si le résidu $K(\text{tâche}\mid \bigcup y_i)$ reste au-dessus de $\theta$ après deux tours (information non capturée).
(b) *Spawn Red-Team* si $K(y_i)$ chute sous le quantile 10 % des réponses du corpus arXiv/S2 sur le même sujet : sortie trop compressible = récitation paramétrique.
(c) *Chimère vs monoculture* : on estime $C_W$ par paire de familles ; on appaire les agents minimisant $C_W$ (familles différentes si $C_W^{\text{intra}}>C_W^{\text{inter}}$), attaquant directement $H4'$.
(d) *Anti-dérive $H9$* : une délégation $c_0\to c_k$ n'est transmise que si $\mathrm{NCD}(c_0,c_k)<\varepsilon$, sinon la consigne originale est réinjectée.
(e) *Budget* : chaque dollar est alloué à l'agent/famille maximisant le gain de compression marginal $-\partial\mathcal{L}/\partial\$$ (prix Claude/Gemini distincts).
