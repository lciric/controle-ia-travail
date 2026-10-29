BASSIN_MATH: Écho-Bracha à Pliage FRI sous Effet de Plan Familial (EB-FRI-EPF)

LOI_PROPOSEE: $f_{\text{eff}}(C)=\sum_k m_k\,[1+(m_k-1)\hat\kappa_k]\,\hat p_k$, avec la contrainte $|C|\ge 3f_{\text{eff}}+1$. On résout $C^*=\arg\max_C \dfrac{\Delta I_{\text{vérifiée}}(C)}{\text{coût}(C)}$ sous $\Pr[\text{accepter un faux}]\le(1-\delta)^q\le\varepsilon$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Domaines de faute.** Chaque famille $k$ (fable, opus, argon) forme un domaine de faute. $\hat\kappa_k$ est l'accord intra-famille en excès du hasard, mesuré gratuitement par `jev-1.14.0` (risque H4′). $\hat p_k$ est le taux d'erreur observé. Le terme $1+(m_k-1)\hat\kappa_k$ joue le rôle d'un « effet de plan » : $m$ clones corrélés valent moins que $m$ votants.
- **Arbitrage monoculture/chimère.** Une monoculture n'est admise que si $\hat\kappa_k\to0$. Dès que $f_{\text{eff}}$ viole la borne de Bracha, l'essaim greffe l'agent de la famille qui réduit le plus $f_{\text{eff}}$ par dollar. Gemini, moins cher, sert de témoin décorrélé.
- **Anti-dérive (H9).** Toute délégation suit le protocole Bracha à deux phases ECHO puis READY, en portant l'empreinte $h_0$ de la consigne racine. Un sous-agent n'agit que s'il reçoit $2f_{\text{eff}}+1$ ECHO portant le même $h_0$. Une divergence jev$(\text{tâche},h_0)>\tau$ déclenche un rejet.
- **Spawn explorateur vs démolisseur.** Chaque réponse est décomposée en affirmations atomiques, assimilées à des « évaluations ». Un vérificateur Arthur tire $q$ positions selon le principe Fiat-Shamir, sur une graine engagée après la réponse. Ces positions sont contrôlées via Crossref, arXiv ou Semantic Scholar contre la récitation paramétrique.
  - Si le test de proximité échoue (distance $>\delta$), on spawne un démolisseur Red-Team d'une famille différente de l'auteur.
  - Si le test réussit mais que l'information gagnée est faible, on spawne un explorateur.
- **Apprentissage.** Il porte uniquement sur $\hat\kappa_k$, $\hat p_k$ et les prompts-rôles archivés, jamais sur les poids.

**2. Fonction objectif et anti-Goodhart**

$$R=\sum_{a\in\text{READY}}\mathbb 1[\text{vérif. externe}(a)]\cdot\text{nouv}(a)\;-\;\lambda\sum_{i\ne j}\big(\hat\kappa_{ij}-\kappa_0\big)_+\;-\;\mu\,\text{USD}\;-\;\nu\,\text{acc}_{\text{canari}}$$

- Le juge jev n'est interrogé qu'à des positions aléatoires révélées a posteriori, ce qui empêche de l'optimiser à l'avance.
- Des canaris, sur lesquels jev a tort par construction, pénalisent toute flatterie envers le juge.
- La récompense finale repose sur une vérification bibliographique externe, et non sur jev.

**3. Duel décisif ($H_A\perp H_B$)**

- **Banc d'essai.** 200 tâches de revue dans lesquelles on plante des fautes : citations fabriquées, inversions de résultats, consignes dérivées.
- **Budget.** Il est constant pour tous les bras : 100 USD Claude et 20 USD Gemini, répartis au prorata.
- **Bras comparés.**
  - (A) EB-FRI-EPF.
  - (B) Topologie fixe chimérique.
  - (C) Échantillons i.i.d. à vote majoritaire.
  - (N) Contrôle négatif : EB-FRI-EPF avec étiquettes familiales permutées, donc $\hat\kappa$ faussé.
- **Hypothèses.**
  - $H_A$ : A > B et A > C en taux de détection des fautes plantées par dollar, avec moins de dérive $h_0$.
  - $H_B$ : N ≈ C, ce qui montre que le gain provient de la modélisation de la collusion.
- **Analyse.** Plan préenregistré, bootstrap apparié, correction de Holm, $\alpha=0{,}01$.
- **Réfutation.** La loi est réfutée si N ≈ A.
