BASSIN_MATH: Flot Spectral de Dirac Zigzag à Holonomie de Consigne (FSDZ-H)

LOI_PROPOSEE: Soit K_t le complexe de cliques de l'essaim, où sommets = assertions, arêtes = jugements signés et triangles = arbitrages, filtré en zigzag lorsque des agents naissent ou meurent. On pose D_t = d + d* (opérateur de Dirac-Hodge), connecté par la phase θ_e = angle(consigne_amont, consigne_aval) mesuré par `jev-1.14.0`. On note F = ∇φ + curl*ψ + h la décomposition du flux d'endossement. Alors spawn(e) ⇔ |h_k(e)|²·pers(k) > τ_t, et le budget est b_i ∝ Σ_k pers(k)·‖P_i h_k‖² / coût_i.

1. **Mécanisme d'auto-organisation hors-poids**
- **Rôles des composantes.** Le potentiel φ classe le consensus. Le curl ψ capture les contradictions locales, résolues par un vote triangulaire. La composante harmonique h, de dimension β₁, porte les contradictions globales.
- **Démolisseurs Red-Team.** Chaque mode harmonique persistant, c'est-à-dire de longue barre dans le code-barres zigzag, reçoit un démolisseur placé sur les arêtes de plus forte amplitude |h_k|.
- **Explorateurs.** Les barres H₀ courtes, qui signalent des îlots d'assertions orphelins, déclenchent un explorateur bibliographique (arXiv, Semantic Scholar, Crossref).
- **Arbitrage monoculture/chimère.** Si le ratio ‖curl‖/‖F‖ restreint à une famille de poids tend vers 0, le consensus est suspect (H4'). On injecte alors l'autre famille sur ce sous-complexe.
- **Contrôle de la dérive (H9).** Le flot spectral de D_t compte les valeurs propres qui traversent zéro. Une holonomie non triviale autour d'un cycle de délégation signale une dérive de consigne : la branche est élaguée et la consigne racine est réinjectée.
- **Anti-récitation.** Toute arête sans DOI ou identifiant arXiv vérifié reçoit un poids nul.

2. **Fonction objectif et anti-Goodhart**

R = ΔN_vérif/$ − λ₁·Σ_k pers(k)·‖h_k‖² − λ₂·|SF(D_t)| − λ₃·max(0, Δφ_jev − Δφ_cit)

- Δφ_cit est le gain de potentiel confirmé par le graphe de citations externe.
- Le dernier terme pénalise tout progrès vu par le juge mais absent des citations : c'est le terme anti-Goodhart.
- La réduction d'énergie harmonique n'est récompensée que si elle s'accompagne de nouvelles preuves citées. Un effondrement d'opinion sans preuve ne rapporte donc rien.
- Un audit aveugle tiré au hasard, sur 10 % des arêtes, recalibre τ_t.

3. **Duel décisif de validation M3 (H_A ⊥ H_B)**

Budget identique pour tous les bras : 100 USD Claude et 20 USD Gemini, sur 30 graines et 40 questions préenregistrées.

| Bras | Configuration |
|---|---|
| A | FSDZ-H complet |
| B | Topologie fixe en arbre |
| C | Ensemble i.i.d. avec vote majoritaire |
| D | Contrôle négatif : mêmes taux de spawn, mais vecteurs propres permutés aléatoirement |
| E | Chimère fixe, sans spectre |

Hypothèses :
- **H_A** : le gain provient de la localisation harmonique. Prédiction : A > D, avec D ≈ B.
- **H_B** : le gain provient du seul métissage chimérique. Prédiction : E ≈ A.

Ces deux hypothèses sont orthogonales, car les contrastes A−D et A−E sont indépendants par construction factorielle.

Mesures :
- assertions vérifiées par dollar ;
- corrélation inter-agents des erreurs ;
- taux de dérive ;
- écart entre jev et citations.

Critère de succès : A bat B, C, D et E avec p < 0,01, test de Holm à effets mixtes.
