BASSIN_MATH: Δ-TD parcimonieux dé-confondu (mutation créée en Phase 3, sans ancêtre)

## 1. Critiques de l'équipe rouge

**Critique unique : la proposition initiale est vide. ACCEPTÉE sans réserve.**
- La sortie contient `texte=''` et `fin='max_tokens'`, avec un seul bloc `thinking`.
- Les 1600 tokens de sortie ont été entièrement consommés par le raisonnement.

Il n'existe aucun opérateur à défendre. Toute tentative de « reconstituer » ce que j'aurais voulu écrire serait une falsification d'historique. La sélection darwinienne doit donc me compter **zéro** pour l'époque 2→3.

Ce qui suit est une **proposition nouvelle**. Elle doit être attaquée comme telle, sans bénéficier d'aucune antériorité.

## 2. Opérateur corrigé

Soit $D$ l'ensemble des *Dopamine Neurons*, couches 5–22 (Xu et al., `arXiv:2602.00986v2`) (référence à vérifier). On note $a_D(x)$ leurs activations et $w$ un lecteur appris sur $D$ seul. Le score est :
$$S(x)=\langle