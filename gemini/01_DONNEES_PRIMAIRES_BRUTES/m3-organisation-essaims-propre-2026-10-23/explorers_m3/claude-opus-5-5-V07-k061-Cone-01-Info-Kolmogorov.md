BASSIN_MATH: Conservation d'Indépendance de Levin à Déficience Martin-Löf (CIL-DML)

LOI_PROPOSEE: Un arc i→j ou un spawn k n'est conservé que si Ψ = Î(x_k : T | x_{pa(k)}) − λ·Î(e_k : e_{pa(k)}) − μ·[Î(x_{pa}:c) − Î(x_k:c)]₊ − ν·d_ML(s_k) > κ·coût_k. Ici Î(a:b) = C(a) + C(b) − C(ab) est l'information mutuelle algorithmique, estimée par un compresseur fixe C.

**1. Mécanisme d'auto-organisation hors-poids**

Chaque sortie x_k est encodée en codes discrets par `jev-1.14.0`, qui sert de compresseur gratuit et illimité. Le vecteur e_k ∈ {0,1}ⁿ enregistre les verdicts d'erreur de l'agent k sur une batterie de sondes.

- **Topologie.** Un agent j écoute i seulement si i apporte un gain conditionnel Î(x_j : T | x_i) positif. Les arcs redondants, c'est-à-dire fortement compressibles l'un par l'autre, sont élagués.
- **Monoculture ou chimère.** Si Î(e_i : e_j) est élevé, les erreurs se compressent ensemble : c'est la signature de H4'. Le binôme est alors rendu chimérique en remplaçant un agent par un modèle d'une autre famille de poids. Sinon, on garde la monoculture, moins chère.
- **Dérive de consigne (H9).** Par la conservation de Levin, le traitement ne peut pas augmenter Î(x : c). Toute chute le long d'une chaîne de délégation mesure donc la dérive. Au-delà d'un seuil, le maillon est coupé et la consigne c est réinjectée.
- **Explorateur ou démolisseur.** On spawne un explorateur quand le gain marginal Î/coût est maximal. On spawne un démolisseur Red-Team quand d_ML(s_k) est élevé, c'est-à-dire quand le score du juge est atypique pour son ensemble de référence : c'est le symptôme d'un exploit.
- **Récitation.** Si C(x | M) ≪ C(x | R), la sortie est explicable par la mémoire paramétrique M plutôt que par les sources récupérées R. Elle est pénalisée.
- **Apprentissage.** L'apprentissage est un journal de topologies et de prompts sélectionnés par Ψ, sans aucune mise à jour des poids.

**2. Fonction objectif et anti-Goodhart**

R = Î(X : T_val) − γ·Σ_{i<j} Î(e_i : e_j) − η·Σ_chaînes Δdérive − β·Σ_k d_ML(s_k)

Le budget est alloué par la règle argmax_k ΔR_k / $_k, sous les contraintes $Claude ≤ 100 et $Gemini ≤ 20.

Le terme d_ML = n − C(s | ensemble) rend tout score trop typé coûteux, ce qui neutralise la loi de Goodhart. T_val n'est jamais montré au juge.

**3. Duel décisif (H_A ⊥ H_B) à budget constant de 120 USD**

Le protocole compare cinq bras, avec les mêmes tâches, les mêmes graines et les mêmes 120 USD :

| Bras | Description |
|---|---|
| A | CIL-DML |
| B | Topologie fixe : planificateur, chercheurs, critique |
| C | N agents i.i.d. avec vote majoritaire |
| D (contrôle négatif) | CIL-DML avec codes jev permutés aléatoirement |
| E | CIL-DML sans terme d_ML |

**Critère principal.** Nombre d'affirmations vérifiées par citation réelle via Semantic Scholar et Crossref, puis jugées par `jev-1.14.0`, sur un lot tenu à l'écart et préenregistré.

**Critères secondaires.**
- Corrélation d'erreurs inter-agents.
- Taux de récitation, mesuré par des citations fantômes.
- Écart entre score du juge et vérité.

**Hypothèses.**
- H_A : A > B et A > C, au seuil p < 0,01 par bootstrap apparié.
- H_B : D ≈ C, ce qui prouve que le gain vient de l'information mesurée et non de l'adaptativité seule. De plus, E montre un écart juge-vérité plus grand que A.

**Réfutation.** La loi est réfutée si D ≈ A, ou si A ne surpasse pas C.
