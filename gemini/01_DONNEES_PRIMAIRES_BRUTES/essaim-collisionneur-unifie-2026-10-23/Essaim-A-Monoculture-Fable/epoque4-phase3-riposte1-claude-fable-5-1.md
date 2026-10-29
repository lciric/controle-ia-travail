BASSIN_MATH: Contraste TD-parcimonieux contrefactuel (lecture + ablation croisée)

**1. Réponse aux critiques (aucun lissage)**

- *Sous-détermination, rang 0* : **accepté intégralement**. Il n'y avait pas de proposition ; je ne la réinvente pas rétroactivement. Ce qui suit est une proposition *nouvelle*, datée époque 4/4, et doit être jugée comme telle.
- *Monoculture* : **accepté**. Le risque de mimétisme d'artefact (cas *Astra*, rapport OpenAI oct. 2026, référence à vérifier) est structurel. Parade : le protocole ci-dessous exige qu'un modèle d'une autre lignée (Llama-3.1-8B, Contrôle E0) serve de cible, et qu'au moins un critère de falsification soit calculable sans aucun jugement de `claude-fable-5-1`.
- *Risque de remplissage* : **accepté**. Pour l'empêcher, toute affirmation ci-dessous est soit une équation, soit un critère d'échec numérique.

**2. Opérateur corrigé**

Soit $S$ l'ensemble parcimonieux de neurones TD (Value couches 2–5, Dopamine couches 5–22, Xu et al., arXiv:2602.00986v2, référence à vérifier), $|S| < 1\%$ (socle). Pour une entrée $x$ avec prompt système $\sigma$ :

$$\Delta_{\text{lec}}(x) = \big\| \delta_S(x \mid \sigma) - \delta_S(x \mid \varnothing) \big\|_1$$

où $\delta_S$ est l'erreur TD lue sur $S$, et $\varnothing$ le re-forward sans prompt système (Contrôle E1 du socle).

$$\Delta_{\text{abl}}(x) = \text{Cap}(x) - \text{Cap}(x \mid S \leftarrow 0)$$

chute de capacité par ablation de $S$ (socle : −54,9 pts sur le modèle d'origine).

Statistique finale : $T(x) = \Delta_{\text{lec}}(x) \cdot \mathbb{1}\big[\Delta_{\text{abl}}(x) \geq \tau_{\text{abl}}\big] + \lambda\,\mathbb{1}\big[\