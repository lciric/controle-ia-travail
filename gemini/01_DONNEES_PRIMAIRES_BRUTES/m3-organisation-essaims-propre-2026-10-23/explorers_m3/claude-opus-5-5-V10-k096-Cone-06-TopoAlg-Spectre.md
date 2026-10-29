BASSIN_MATH: Diffusion de Faisceau Cellulaire à Cohomologie d'Obstruction (DFC-CO)

LOI_PROPOSEE: $\dot x=-\alpha L_{\mathcal F}x,\quad L_{\mathcal F}=\delta^\top W\delta,\quad \dot w_e=\eta\big(\|(\delta x)_e\|^2-\bar\tau_e\big)\,\mathbb 1[e\notin\ker\delta^\top]$. On spawne un sous-agent lorsque $\beta_1^{\mathcal F}[t,t+\Delta]>0$ persiste.

1. **Auto-organisation hors-poids**

Chaque agent $v$ possède une tige $\mathcal F(v)=\mathbb R^d$, qui est son embedding de thèses calculé par `jev-1.14.0`. Chaque arête de délégation $e=(u,v)$ porte deux applications de restriction $\mathcal F_{v\trianglelefteq e}$, apprises par moindres carrés sur les traductions de consigne observées. La dérive de consigne (H9) correspond à l'énergie $\|(\delta x)_e\|^2$ hors des sections globales. Une incohérence irréductible correspond à une classe de $H^1(\mathcal F)$, détectée par le spectre persistant du laplacien de faisceau sur une filtration par confiance.

- **Spawn d'un explorateur** : il se déclenche si $\lambda_2(L_{\mathcal F})<\epsilon$, ce qui signale un consensus trop rapide. Ce cas correspond à une monoculture suspecte (H4'). Le nouvel agent est obligatoirement d'une autre famille, ce qui forme une chimère.
- **Spawn d'un démolisseur Red-Team** : il se déclenche si une classe de $H^1$ survit au-delà de $\Delta$. Le démolisseur est placé sur le support du générateur harmonique.
- **Budget** : la dépense est $b_v\propto |\phi_{H^1}(v)|^2/c_{\text{fam}(v)}$, sous les plafonds de 100 USD pour Claude et de 20 USD pour Gemini.
- **Élagage** : les arêtes dont $w_e\to0$ sont supprimées.

2. **Objectif et dispositif anti-Goodhart**

$$R=\underbrace{\tfrac{1}{|C|}\textstyle\sum_{c}\mathrm{Ver}_{\text{Crossref/S2}}(c)\,J_{S'}(c)}_{\text{vérifié}}-\mu\,\overline{\rho}_{\text{err}}^{\text{intra-fam}}-\nu\,\mathrm{sim}(c,c^{\text{no-ctx}})-\kappa\,\textstyle\sum_e\|(\delta x)_e\|^2$$

- **Anti-Goodhart** : le juge est découpé en sous-espaces de traits aléatoires disjoints. Le sous-espace $S$ sert à apprendre $\mathcal F$, et le sous-espace $S'$, tiré à chaque époque, sert seul à calculer $R$.
- **Anti-récitation** : le terme $\nu$ pénalise toute ressemblance avec la réponse produite sans contexte.
- **Corrélation des erreurs** : le terme $\mu$ pénalise la corrélation d'erreurs entre agents de même famille.
- **Vérification bibliographique** : $\mathrm{Ver}$ exige que la référence existe effectivement dans Crossref ou Semantic Scholar.

3. **Duel décisif ($H_A\perp H_B$)**

Le budget est identique pour tous les bras (120 USD), avec 40 tâches de revue présentées en ordre randomisé.

| Bras | Configuration |
|---|---|
| A | DFC-CO |
| B | Topologie fixe en arbre |
| C | Essaim i.i.d. avec vote majoritaire |
| N (contrôle négatif) | DFC-CO avec des restrictions $\mathcal F$ permutées aléatoirement, même nombre de spawns |

Hypothèses :
- $H_A$ : $R_A>\max(R_B,R_C)$.
- $H_B$ : $R_A>R_N$, ce qui montre que le gain vient de la cohomologie et non du simple fait de spawner.

Les deux hypothèses sont testées par permutation appariée, à $\alpha=0{,}025$ chacune.

Métriques secondaires préenregistrées :
- $\overline\rho_{\text{err}}$ ;
- la dérive racine–feuille ;
- le taux de citations fantômes.

Critère de réfutation : la loi est réfutée si $R_N\ge R_A$.
