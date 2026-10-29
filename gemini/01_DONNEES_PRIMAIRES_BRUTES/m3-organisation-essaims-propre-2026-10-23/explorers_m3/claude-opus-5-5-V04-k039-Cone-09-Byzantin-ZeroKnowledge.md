BASSIN_MATH: Contraction Dolev-Lynch à Rognage par Familles (CDL-RF)

LOI_PROPOSEE: $x_i^{t+1}=\operatorname{moy}\big(\operatorname{trim}_{\hat f_t}\{x_j^t\}_{j\in N(i)}\big)$, sous la contrainte $\kappa(G_t)\ge 2\hat f_t+1$, avec $\hat f_t=\omega\big(C_t^{>\tau}\big)$ et une mutation pilotée par $\rho_t=\delta_{t+1}/\delta_t$.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids de l'essaim**

L'unité de faute n'est pas l'agent mais la famille de poids. Une monoculture collusoire compte donc pour une seule voix byzantine, ce qui traite H4′.

- **Estimation de la collusion.** Le classifieur jev-1.14.0 évalue les erreurs de chaque agent sur des sondes à vérité connue. On en tire une matrice de corrélation d'erreurs $C_t$. On estime $\hat f_t$ comme la clique maximale du graphe $C_t>\tau$.
- **Topologie.** On ajoute les arêtes les moins coûteuses, en privilégiant les arêtes inter-familles (chimère), jusqu'à atteindre la connectivité de Dolev $\kappa\ge2\hat f_t+1$. La chimère est achetée seulement si elle augmente $\kappa$ à moindre coût. Sinon, la monoculture Gemini, moins chère, est conservée.
- **Spawning selon le taux de contraction $\rho_t$ :**
  - si $\rho_t>\rho^{*}$ (stagnation), on spawne un explorateur ;
  - si $\rho_t<\rho_{\min}$ (consensus trop rapide, signature de collusion), on spawne un démolisseur Red-Team issu d'une famille minoritaire.
- **Dérive de consigne (H9).** Chaque délégation transporte le hachage de la consigne racine. Arthur, ici jev, tire au hasard un message et teste sa fidélité à cette consigne. Un message infidèle est traité comme une valeur byzantine, puis rogné.
- **Apprentissage hors-poids.** Les seuils $\tau,\rho^{*},\rho_{\min}$ et les arêtes conservées sont stockés dans une mémoire de protocole externe, mise à jour par bandit.

2. **Fonction objectif et anti-Goodhart**

$$R=\frac{V_{\text{API}}}{\text{USD}}-\lambda\,\overline{C_t}-\mu\,\big|s_{\text{jev}}-V_{\text{API}}\big|-\nu\,\text{Récit}$$

- $V_{\text{API}}$ est la fraction d'affirmations vérifiées sur arXiv, Semantic Scholar et Crossref.
- $\text{Récit}$ est le taux de références non retrouvées, qui mesure la récitation paramétrique.
- Jev sert à rogner, jamais à récompenser. L'écart entre jev et les API est pénalisé. Le juge ne peut donc pas être optimisé seul.

3. **Duel décisif de validation M3 ($H_A\perp H_B$)**

Le budget est identique pour tous les bras : 100 USD Claude et 20 USD Gemini, répartis en parts égales. Le corpus comprend 200 questions bibliographiques à vérité API, partagées entre les bras.

Bras comparés :
- **A :** CDL-RF.
- **B :** topologie fixe, avec le même nombre d'agents.
- **C :** agents i.i.d. avec vote majoritaire.
- **Contrôle négatif :** CDL-RF avec étiquettes de famille permutées aléatoirement. Le rognage est alors aveugle à la collusion.

Hypothèses :
- **$H_A$ :** l'erreur vérifiée de A est inférieure à celle de B et de C.
- **$H_B$ :** cet avantage disparaît sous le contrôle négatif.

Le test est un bootstrap apparié avec correction de Holm. La loi est validée seulement si $H_A$ et $H_B$ tiennent conjointement. Elle est réfutée si le contrôle permuté égale A, car le gain viendrait alors du seul rognage, pas de la détection de collusion.
