BASSIN_MATH: Tri de Reeb à Intégrale d'Euler Pondérée (TRIE-P)

LOI_PROPOSEE: $b_k = B\,\dfrac{\left|\int_{U_k}\varphi\,d\chi\right|}{\sum_j\left|\int_{U_j}\varphi\,d\chi\right|}$, avec $\int\varphi\,d\chi=\int_0^\infty\big[\chi(\varphi\ge s)-\chi(\varphi<-s)\big]\,ds$. Une branche du graphe de Reeb $\mathrm{Reeb}(K,f)$ déclenche un explorateur ; un cycle $\beta_1(\mathrm{Reeb})>0$ déclenche un démolisseur.

1. **Mécanisme d'auto-organisation hors-poids**
   - **Complexe et fonction.** Les affirmations produites forment un complexe simplicial $K$ : sommets = affirmations, arêtes = co-justification. La fonction $f$ est la confiance attribuée par `jev-1.14.0`, à coût nul. L'incertitude est $\varphi = 1-2|f-\tfrac12|$.
   - **Divisions du travail.** Le graphe de Reeb contracte les composantes des niveaux de $f$. Une bifurcation signale une hypothèse qui se scinde : on y spawne un explorateur. Un cycle persistant signale une boucle de justification circulaire : on y spawne un démolisseur Red-Team.
   - **Budget.** Le budget $B$ est réparti entre les régions $U_k$ selon l'intégrale d'Euler, appliquée séparément à Claude (100 USD) et à Gemini (20 USD).
   - **Monoculture ou chimère.** Pour chaque famille $F$, on calcule $\mathrm{Reeb}_F$. Si la distance d'entrelacement vérifie $d_I(\mathrm{Reeb}_F,\mathrm{Reeb}_{F'})<\varepsilon$, les erreurs des deux familles sont corrélées (risque H4'). On impose alors une chimère sur $U_k$ ; sinon, on conserve la monoculture, moins coûteuse.
   - **Contrôle de la dérive (H9).** Chaque délégation transporte la fonction-consigne $g$. Un sous-agent est élagué dès que $d_I(\mathrm{Reeb}(K,g_{\text{parent}}),\mathrm{Reeb}(K,g_{\text{enfant}}))>\delta$.
   - **Apprentissage sans poids.** L'apprentissage porte sur les seuils $(\varepsilon,\delta)$ et sur la topologie conservée en mémoire externe.

2. **Fonction objectif et anti-Goodhart**
   $$R = N_{\text{vérif}} \;-\; \lambda\,\big\|\mathrm{ECC}_{\text{jev}}-\mathrm{ECC}_{\text{cit}}\big\|_{L^1} \;-\; \mu\,\bar\rho_{\text{fam}} \;-\; \nu\,\mathrm{coût}$$
   - $N_{\text{vérif}}$ compte les affirmations confirmées par un DOI ou un lien arXiv, Semantic Scholar ou Crossref.
   - $\mathrm{ECC}$ désigne la courbe de caractéristique d'Euler de deux filtrations indépendantes : le score jev et la distance dans le graphe de citations.
   - $\bar\rho_{\text{fam}}$ est la corrélation moyenne des erreurs entre familles.
   - Tromper le juge déforme une seule des deux filtrations, ce qui fait diverger les courbes et pénalise $R$.
   - Les seuils de jev sont tirés au hasard et cachés à chaque épisode.
   - Contre la récitation de la mémoire paramétrique, une affirmation sans ancrage bibliographique vaut zéro.

3. **Duel décisif $H_A \perp H_B$**
   - **Hypothèses.** $H_A$ : le gain provient de la topologie de Reeb. $H_B$ : le gain provient seulement du nombre de spawns.
   - **Bras à budget identique (100 + 20 USD) :**
     - (i) essaim fixe ;
     - (ii) spawns i.i.d. en nombre égal à celui de TRIE-P ;
     - (iii) TRIE-P ;
     - (iv) contrôle négatif : TRIE-P avec $f$ permutée aléatoirement sur les sommets, ce qui préserve les comptes mais détruit la topologie.
   - **Plan.** 30 tâches pré-enregistrées, appariées et rejouées sur 3 graines.
   - **Mesures :** $N_{\text{vérif}}$, $\bar\rho_{\text{fam}}$ et la dérive de consigne.
   - **Tests.** Test de permutation apparié avec correction de Holm.
   - **Lecture.** $H_A$ est validée si (iii) > (ii) ≈ (iv) > (i). L'égalité entre (iii) et (iv) réfuterait la loi.
