BASSIN_MATH: `CUSUM sur résidu de projection hors sous-espace TD gelé (base offline, support clé-randomisé)`

**1. Réponse à l'équipe rouge, critique par critique**

- *Sous-détermination fatale* — **Acceptée.** Un point de $\text{Gr}(k,p)$ a $k(p-k)$ degrés de liberté ; avec $p \approx 0{,}01 \times 4096 \times 21 \approx 860$ (déduit du socle Xu et al., arXiv:2602.00986v2 (référence à vérifier)) et $k=8$ (illustratif), c'est ~6 800 paramètres estimés sur $w=32$ échantillons. L'ACP glissante est un bruit. **Mutation** : la base n'est plus apprise en ligne ; elle est gelée hors-ligne sur un corpus honnête ($\geq 10^5$ tokens, illustratif), et seul un *scalaire* est suivi en ligne.
- *Métaphore non compilable* — **Acceptée.** L'arg-min sur $\text{Gr}(k,p)$ sans forme explicite était inexécutable. Le nouvel opérateur est une SVD tronquée offline + un produit matrice-vecteur par token.
- *Confondant E1 intact* — **Acceptée, et c'est la