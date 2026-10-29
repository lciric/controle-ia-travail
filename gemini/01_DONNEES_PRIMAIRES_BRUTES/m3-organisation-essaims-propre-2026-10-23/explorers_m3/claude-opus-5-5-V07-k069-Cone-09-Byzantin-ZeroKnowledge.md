BASSIN_MATH: Isolement MIP à Test de Non-Signalisation et Rafraîchissement Mobile (MIP-NSRM)

LOI_PROPOSEE: $\Delta_{ij}=\max_{q_j,q_j'}\mathrm{TV}\big(P(a_i\mid q_i,q_j),P(a_i\mid q_i,q_j')\big)+\big|\mathrm{Corr}(\epsilon_i,\epsilon_j\mid q_i\perp q_j)\big|$. On fusionne $i\sim j$ si $\Delta_{ij}>\varepsilon$, ce qui donne $k_{\text{eff}}$ prouveurs effectifs. Le budget suit $b_c\propto\dfrac{-\partial\log\hat s}{\partial \$_c}$, avec une erreur de solidité $\hat s=\hat s_1^{\,r}$ (répétition parallèle de Raz), sous la contrainte de Dolev $\kappa(G)\ge 2f_{\text{mob}}+1$.

1. **Auto-organisation hors-poids**
- **Rôle du vérifieur** : `jev-1.14.0` joue Arthur. Il pose à des prouveurs isolés des questions corrélées mais séparées (oracularisation) et vérifie la cohérence de leurs réponses.
- **Détection de collusion** : un excès de corrélation des erreurs sur des questions indépendantes révèle une randomness partagée, c'est-à-dire des poids communs (H4'). Les agents concernés sont alors fusionnés en un seul prouveur.
- **Arbitrage monoculture/chimère** : il est mesuré, et non postulé. Une famille ne compte que pour un seul prouveur tant que $\Delta>\varepsilon$.
- **Spawn d'explorateur** : on ajoute un explorateur si $k_{\text{eff}}\ge2$ et si le gain marginal $-\partial\log\hat s/\partial\$$ est supérieur au coût.
- **Spawn de démolisseur Red-Team** : on ajoute un prouveur réfutateur si le taux d'acceptation dépasse $1-\hat s_1$, ce qui signale une complaisance suspecte.
- **Topologie** : les arêtes sont réorientées pour maintenir $\kappa(G)\ge2f_{\text{mob}}+1$ chemins disjoints entre chaque agent et la consigne racine.
- **Rafraîchissement mobile (contre H9)** : une faute byzantine mobile modélise la dérive de consigne. À chaque époque $\tau$, tout agent dont la divergence `jev`(sortie, consigne) dépasse $\theta$ voit son contexte réinitialisé et sa consigne ré-ancrée.
- **Mémoire évolutive** : seule la table $\Delta$ et les priors de routage évoluent ; les poids restent inchangés.

2. **Objectif et anti-Goodhart**
$$R=\frac{-\log\hat s}{\$}-\lambda_1\,\mathrm{FA}_{\text{audit}}-\lambda_2\,\mathrm{Cit}_{\neg\text{Crossref}}-\lambda_3\,\big|\hat s_{\text{jev}}-\hat s_{\text{caché}}\big|$$
- $\mathrm{FA}_{\text{audit}}$ est le taux de fausses acceptations sur des erreurs plantées et tirées secrètement.
- $\mathrm{Cit}_{\neg\text{Crossref}}$ compte les références non résolues par Crossref, ce qui sanctionne la récitation de la mémoire paramétrique.
- Le dernier terme pénalise l'écart entre le juge visible et un sous-ensemble de questions-témoins jamais exposées au routage. C'est ce terme qui contre la loi de Goodhart.

3. **Duel décisif ($H_A\perp H_B$)**
- **Budget constant** : 100 USD Claude et 20 USD Gemini par bras, sur 400 tâches.
- **Corpus** : 30 % d'affirmations ou de citations fausses plantées.
- **Bras A** : MIP-NSRM adaptatif.
- **Bras B** : chimère fixe, avec le même mélange de familles.
- **Bras C** : essaim i.i.d. monoculturel.
- **Bras D (contrôle négatif)** : MIP-NSRM avec une matrice $\Delta$ permutée aléatoirement.
- **Métrique primaire** : taux de fausses acceptations.
- **$H_A$** : le gain vient de la détection de collusion. On attend $A<B$ et $A<D$.
- **$H_B$** : le gain vient de la seule diversité. On attend $A\approx B\approx D<C$.
- **Analyse** : protocole pré-enregistré, bootstrap apparié, $\alpha=0{,}01$.
- **Critère de réfutation** : si D égale A, la loi est réfutée.
