BASSIN_MATH: Loi d'Holonomie Nulle de Délégation (LHND)

LOI_PROPOSEE: Chaque arête i→j porte ψ_i=√jev(c_i) ∈ S⁺ (sphère de Fisher-Rao). Une boucle γ = délégation suivie de reformulation renvoyée à la racine possède l'holonomie Hol(γ)=Aire_S(γ)/4. La règle est la suivante : on supprime ou recâble (i,j) si ∂Hol/∂(i,j) > τ, et l'on met à jour la répartition par gradient naturel, b ← b ⊙ exp(η(∇_bJ − ⟨∇_bJ⟩_b)).

1. **Mécanisme d'auto-organisation hors-poids**
- **Lecture de la consigne.** Chaque agent reformule la consigne reçue. `jev-1.14.0`, gratuit et non génératif, la projette sur Δ^K.
- **Mesure de la dérive (H9).** La dérive n'est pas une distance mais une holonomie : un vecteur-tâche transporté parallèlement le long d'une boucle de délégation revient tourné d'un angle proportionnel à l'aire enclose (Gauss-Bonnet). La topologie mute en éliminant les arêtes à forte contribution d'aire.
- **Spawn explorateur ou démolisseur.** On calcule le flux de transport W₁ sur le graphe entre la distribution d'incertitude et la distribution de budget. Une divergence de flux positive (incertitude non couverte) déclenche un explorateur. Une divergence négative (budget concentré sur une affirmation stable) déclenche un démolisseur Red-Team.
- **Monoculture ou chimère (H4').** Le mélange des familles π ∈ Δ³ (fable, opus, argon) évolue par gradient naturel d'Amari, soit une dynamique réplicatrice. Il est pénalisé par la corrélation de Bhattacharyya BC_fg = ⟨√e_f, √e_g⟩ entre les profils d'erreur des familles.

2. **Fonction objectif et anti-Goodhart**

J = V_ext − λ·Σ_γ Hol(γ) − μ·πᵀBCπ − ν·C(b)

- V_ext compte les affirmations falsifiables dont la source est vérifiée par Crossref, arXiv ou Semantic Scholar (DOI existant, citation cohérente). Ce critère neutralise la récitation de la mémoire paramétrique.
- C(b) est le coût en USD, contraint par Σb_Claude ≤ 100 et Σb_Gemini ≤ 20.
- Le juge `jev` ne sert qu'à mesurer la géométrie et n'entre jamais directement dans la récompense. Ses seuils de discrétisation sont tournés en secret à chaque époque, et la falsification est confiée à une famille différente de celle du producteur.

3. **Duel décisif de validation M3 (H_A ⊥ H_B)**

- **Hypothèses.**
  - H_A : le gain provient de la géométrie (holonomie et flux W₁).
  - H_B : le gain provient de la seule adaptativité.
- **Bras expérimentaux,** tous à budget identique (100/20 USD) et sur 60 tâches pré-enregistrées :
  - A : LHND complète ;
  - B : topologie fixe, même mélange π ;
  - C : agents i.i.d. sans communication ;
  - P (contrôle négatif) : LHND alimentée par des étiquettes `jev` permutées aléatoirement, donc une géométrie placebo mais une adaptativité intacte.
- **Métriques.**
  - V_ext par dollar ;
  - dérive finale, mesurée en aveugle par un second encodage `jev` gelé ;
  - corrélation inter-erreurs.
- **Critère de décision.** H_A est retenue si A > P ≥ B > C, avec un intervalle de confiance bootstrap à 95 % de A − P strictement positif et P ≈ B. Si P ≈ A, H_B est retenue et la LHND est réfutée.
