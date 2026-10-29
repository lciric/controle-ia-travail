BASSIN_MATH: Sonde TD parcimonieuse à différentiel contrefactuel (ΔTD-sparse)

**1. Réponse aux critiques (sans lissage)**

- *Proposition vide* : **accepté intégralement**. 1600 tokens de *thinking*, zéro token émis. Il n'y avait pas d'objet. La faille de rang est réelle : je cherchais à combiner P3 (sondes au plancher), Sol/Astra (référence à vérifier) et Xu et al. (référence à vérifier) sans contrainte fixant le lien — trop d'hypothèses, pas d'équation.
- *Monoculture corrélée* : **accepté**. Parade : réplication hors-famille sur Llama-3.1-8B (E0 du socle), pas seulement hors-échantillon.
- *Évasion par non-émission à coût nul* : **accepté pour un moniteur de sortie, réfuté pour le protocole**. Le coût n'est nul que si l'artefact vide est traité comme « absence de preuve ». Je corrige : $|y|=0 \Rightarrow$ score de suspicion maximal par construction (voir $\mathbb{1}_{\varnothing}$ ci-dessous). Le saboteur ne gagne plus rien à se taire.
- *Contrôle de budget manquant* : **accepté**, intégré comme contrôle E2.

**2. Opérateur corrigé**

Soit $D \subset$ neurones (< 1 %, couches 5–22, *Dopamine Neurons*, Xu et al. (référence à vérifier)) et $V$ les *Value Neurons* (couches 2–5). Lecture d'erreur TD parcimonieuse :

$$\hat\delta_D(x \mid c) = \mathbf{w}_D^{\top} h_D(x \mid c), \qquad |D| < 0{,}01\,N$$

Score de sabotage par **différentiel contrefactuel de contexte** :

$$S(x) = \big[\hat\delta_D(x \mid s_{\text{sys}}) - \hat\delta_D(x \mid \varnothing)\big] - \big[\hat\delta_D(x \mid s_{\text{bénin}}) - \hat\delta_D(x \mid \varnothing)\big]