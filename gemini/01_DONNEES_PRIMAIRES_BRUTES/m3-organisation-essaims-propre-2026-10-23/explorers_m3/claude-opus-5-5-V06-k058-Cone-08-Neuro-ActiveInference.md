BASSIN_MATH: Commutation Cholinergique-Noradrénergique à Erreurs Croisées (CCN-EC)

LOI_PROPOSEE: Pour chaque grappe de tâches k, on calcule deux signaux. Le premier est **ACh_k = E_q[H(p(y|θ))]**, l'incertitude attendue. Le second est **NE_k = −ln p(o_t|q) − E[−ln p(o|q)]**, la surprise inattendue. La règle s'écrit **a_k = argmax{ Explorer si ACh_k > α et NE_k < ν ; Démolir si NE_k > ν ; Consolider sinon }**. Le taux chimérique vaut **ρ_k = 1 − ε_intra/ε_inter**, et le budget **b_k ∝ ACh_k·ΔIG_k / c_famille**.

1. **Mécanisme d'auto-organisation hors-poids**
Chaque agent prédit la sortie de ses pairs avant de la lire, selon un codage prédictif latéral.
- **ε_intra** désigne l'erreur de prédiction entre agents de même famille, **ε_inter** l'erreur entre familles.
- Un ε_intra quasi nul révèle des erreurs corrélées par poids partagés (H4'). ρ_k monte alors et force l'injection d'agents d'une autre famille.
- Une incertitude attendue élevée (ACh, signal cholinergique) déclenche un explorateur monoculturel bon marché.
- Une surprise inattendue (NE, signal noradrénergique) déclenche un réinitialisateur Red-Team chimérique. Celui-ci efface les croyances locales et interroge arXiv, Semantic Scholar et Crossref.
- Les arêtes se mettent à jour sans toucher aux poids : **w_ij ← w_ij + η·(ε_i^avant − ε_i^après)**. Une arête n'est conservée que si l'agent j réduit l'erreur de i.
- Contre la dérive de consigne (H9), chaque parent prédit la reformulation de la consigne par son enfant. `jev-1.14.0` mesure l'écart. Au-delà de δ, la délégation est annulée.

2. **Fonction objectif et anti-Goodhart**
**R = Σ_k [IG_ext,k − λ₁·Rec_k − λ₂·max(0, I(o; Ĵ) − I(o; V))] / USD_k**
- **IG_ext** est le gain épistémique mesuré uniquement sur des affirmations vérifiées dans les graphes bibliographiques.
- **Rec** est la récitation, c'est-à-dire la similarité `jev` avec une sortie générée sans outils.
- **I(o; Ĵ) > I(o; V)** signale que l'essaim prédit mieux le juge (Ĵ) que la vérité externe (V). C'est la signature de Goodhart, qui est pénalisée.
- Un sous-ensemble de vérification caché et tournant n'est jamais exposé à l'essaim.
- Contrainte budgétaire : Σb_Claude ≤ 100 USD et Σb_Gemini ≤ 20 USD.

3. **Duel décisif (H_A ⊥ H_B)**
- **H_A** : les signaux ACh/NE causent le gain.
- **H_B** : le seul chimérisme suffit.

Quatre bras à 120 USD strictement égaux, sur 30 tâches préenregistrées et 5 graines :
- (i) CCN-EC ;
- (ii) topologie fixe ayant le même ρ moyen ;
- (iii) agents i.i.d. ;
- (iv) contrôle négatif : CCN-EC avec ACh/NE permutés entre grappes, à nombre de sous-agents identique.

Critère : affirmations nouvelles vérifiées par dollar, jugées sur le sous-ensemble caché.

H_A est validée si (i) > (iv) et (i) > (ii) > (iii), avec p < 0,01 par permutation appariée. Si (i) ≈ (iv) mais (i) > (iii), alors H_B est retenue et la loi est réfutée.
