BASSIN_MATH: Loi SPRT-CUSUM du Contrôle Particulaire d'Essaim (SCOPE)

LOI_PROPOSEE: $a_t^*=\arg\max_{a=(f,r,e)}\ \mathbb{E}_{\hat b_t}\!\left[\Delta I_a-\lambda_C c_a^{C}-\lambda_G c_a^{G}-\gamma\,\hat\rho_{f}\right]+\beta\sqrt{\tfrac{\ln t_w}{n_{a,w}}}$. Une sous-tâche s'arrête dès que $\Lambda_t\notin(B,A)$ (SPRT). La topologie mute dès que $S_t>h$ (CUSUM).

**1. Mécanisme d'auto-organisation hors-poids**

- **Croyance.** Un filtre particulaire $\hat b_t=\{(\theta^i,w^i)\}$ porte sur les hypothèses de recherche. Les poids sont mis à jour par vraisemblance via `jev-1.14.0`, à coût nul, et rééchantillonnés quand $\mathrm{ESS}<N/2$.
- **Actions.** Chaque action $a=(f,r,e)$ combine une famille $f\in\{\text{fable},\text{opus},\text{argon}\}$, un rôle $r\in\{\text{explorateur},\text{démolisseur}\}$ et une arête $e$ (qui parle à qui).
- **Choix.** L'action est choisie par un bandit contextuel à fenêtre glissante $w$ (sliding-window UCB), conçu pour la non-stationnarité. Les multiplicateurs suivent $\lambda_C\leftarrow[\lambda_C+\eta(\text{dépense}_C-100\,t/T)]^+$, et de même pour $\lambda_G$ avec un plafond de 20 USD.
- **Spawn.** Un explorateur est lancé si l'entropie $H(\hat b_t)$ dépasse un seuil $\tau$. Un démolisseur Red-Team est lancé si le CUSUM d'accord inter-agents vérifie $S^{acc}_t=\max(0,S^{acc}_{t-1}+\mathbb{1}[\text{accord}]-k)>h$. Un consensus trop rapide est en effet le symptôme de H4'.
- **Monoculture ou chimère.** $\hat\rho_f$ est la corrélation empirique des erreurs entre agents de même poids, mesurée sur des canaris à vérité connue. La chimère est imposée dès que $\hat\rho_f>\rho^*$.
- **Anti-H9.** Un CUSUM porte sur la distance `jev` entre la consigne racine et chaque consigne déléguée. Une alarme élague la branche et réinjecte la consigne racine.
- **Anti-récitation.** Toute affirmation sans DOI vérifié via Crossref ou Semantic Scholar reçoit une vraisemblance nulle.

**2. Fonction objectif et anti-Goodhart**

$$R_t=\underbrace{D_{KL}(\hat b_{t+1}\Vert\hat b_t)}_{\Delta I}-\lambda\cdot c_t-\gamma\hat\rho+\alpha\,\mathrm{Acc}_{\text{canaris}}-\mu\,\big|s_{jev}-s_{jev}^{\text{held-out}}\big|$$

Le juge est scindé en deux : `jev` publique pour le guidage, et `jev` sur canaris et vérité-terrain cachés, avec des seeds tournantes. Le dernier terme pénalise l'écart entre les deux, donc toute optimisation qui ne serait que proxy.

**3. Duel décisif $H_A\perp H_B$**

- **Hypothèses.** $H_A$ : le gain vient de l'adaptativité séquentielle (SPRT, CUSUM, bandit). $H_B$ : le gain vient de la seule diversité des poids.
- **Plan.** Plan factoriel 2×2 {adaptatif, fixe} × {monoculture, chimère}, plus un essaim i.i.d. aléatoire. Le budget est identique pour tous : 100 USD Claude et 20 USD Gemini.
- **Banc.** 200 tâches comportant des failles plantées et des fausses citations.
- **Contrôle négatif.** SCOPE est exécuté avec des récompenses `jev` permutées. Il doit retomber au niveau i.i.d. ; sinon, le gain est un artefact.
- **Métrique.** Nombre de failles détectées par dollar, et taux d'hallucination bibliographique.
- **Validation.** Un SPRT inter-bras ($\alpha=\beta=0{,}05$) valide $H_A$ si l'effet principal « adaptatif » est significatif et que l'interaction adaptatif × chimère est nulle (orthogonalité). Dans le cas contraire, la loi SCOPE est réfutée.
