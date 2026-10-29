BASSIN_MATH: RPC-TD (Résidu Partiel Contrastif sur sous-espace TD)

### 1. Riposte aux critiques

**Aucune critique n'a été reçue, donc aucune critique ne peut être acceptée ou réfutée.** La sortie Red-Team est vide : `texte=''`, `fin='max_tokens'`, un seul bloc `thinking`. Je n'invente pas d'objections pour simuler un duel.

Je fais une **auto-critique explicite**, qui ne remplace pas la Red-Team et doit être rejouée à l'époque 2 :

- **(a) Proposition creuse.** Ma proposition initiale « RPC » n'avait ni opérateur ni protocole. C'est un défaut fatal, et il est accepté.
- **(b) Confondant de lecture d'instruction.** Une sonde « sabotage » peut détecter la simple lecture d'une instruction secrète. C'est le piège du socle P3, et il est accepté.
- **(c) Existence hors-échantillon non garantie.** Le sous-système TD (Xu et al., `arXiv:2602.00986v2` (référence à vérifier)) n'est pas assuré sur Llama-3.1-8B. Ce point est accepté et conditionne tout le reste (E0).

### 2. Équation et protocole corrigés

**Notations**
- $h_{\text{TD}}(x)$ : activations restreintes aux *Value Neurons* (couches 2–5) et aux *Dopamine Neurons* (couches 5–22), soit moins de 1 % des neurones selon le socle.
- $x^{\varnothing}$ : re-forward de $x$ sans prompt système.

**Sous-espace conf