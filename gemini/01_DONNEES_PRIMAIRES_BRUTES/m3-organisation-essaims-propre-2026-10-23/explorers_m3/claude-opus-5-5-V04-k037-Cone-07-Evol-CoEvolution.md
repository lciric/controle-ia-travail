BASSIN_MATH: Seuil d'Eigen à Cliquet de Muller Recombiné (SECMR)

LOI_PROPOSEE: $\dot x_i=\sum_j x_j\,f_j\,Q_{ji}(d)-\bar f\,x_i$, avec une fidélité $Q_{ii}(d)=q_i^{\,d}$ et un plafond de profondeur $d^*_i=\dfrac{\ln\sigma_i}{\ln(1/q_i)}$. Une lignée ne délègue que si $d<d^*_i$. Sinon, elle est recombinée avec la consigne racine.

**1. Mécanisme d'auto-organisation hors-poids**

Un génotype $i$ est un triplet (famille de poids, rôle, prompt-stratégie). Le rôle vaut explorateur, démolisseur ou synthétiseur.

- **Fidélité.** $q_i$ est la similarité `jev` entre la consigne transmise et la racine, mesurée à chaque saut. Elle est gratuite.
- **Avantage sélectif.** $\sigma_i=f_i/\bar f_{-i}$.
- **Seuil de délégation.** Au-delà de $d^*_i$ (seuil d'Eigen), la dérive H9 devient une catastrophe d'erreur. La délégation est donc bloquée.
- **Anti-cliquet de Muller.** Toute lignée dont $q_i^{\,d}<\theta$ subit une recombinaison forcée : la consigne racine est réinjectée et la stratégie locale est conservée.
- **Sélection fréquence-dépendante négative.** $f_i\leftarrow f_i-\lambda\,\rho(e_i,\bar e)$, où $\rho$ est la corrélation des erreurs avec la population. Les monocultures corrélées (H4') perdent du poids. Une chimère n'émerge que si elle réduit $\rho$.
- **Choix du rôle à engendrer.** On crée un explorateur dans une case vide de l'archive MAP-Elites (famille × rôle × profondeur × sous-domaine). On crée un démolisseur (parasite) lorsque la valeur ajoutée d'un hôte reste stable pendant $k$ générations.
- **Budget.** La part de budget de chaque lignée suit $x_i$. Deux pools séparés sont tenus (100 USD Claude, 20 USD Gemini). Chaque lignée a un plancher de $5\%$ pour éviter l'extinction prématurée.

**2. Fonction objectif et anti-Goodhart**

$$f_i=\frac{V_i\cdot\mathbb 1[\text{DOI résolu}]\;-\;\lambda\,\rho_i\;-\;\mu\,|J_i-V_i|\;-\;\nu\,P_i}{\text{coût}_i}$$

- $V_i$ : affirmations vérifiées par les graphes Crossref et Semantic Scholar. Les citations non résolues comptent zéro, ce qui neutralise la récitation paramétrique.
- $J_i$ : score d'un panel `jev` tiré au hasard et renouvelé à chaque génération. Le terme $|J_i-V_i|$ punit l'écart entre le juge et la vérification, contre la loi de Goodhart.
- $P_i$ : fraction des affirmations falsifiées par les parasites.
- **Diagnostic de Price.** On suit $\Delta\bar q=\mathrm{Cov}(w,q)+\mathbb E[w\,\Delta q]$. Si le terme de transmission devient négatif, le pas de mutation est réduit.

**3. Duel décisif ($H_A\perp H_B$), budget constant de 120 USD**

Quatre bras, avec 30 graines par bras :

- **A** : SECMR.
- **B** : essaim fixe (topologie et rôles figés).
- **C** : essaim i.i.d. (créations aléatoires avec la même distribution de profondeur que A).
- **D, contrôle négatif** : SECMR avec un signal $q$ permuté aléatoirement.

Critères :

- **Métrique principale** : rendement vérifié par dollar, $\sum V/\$$.
- **Métriques secondaires** : dérive $1-q$ à profondeur 4, et $\rho$ moyen.

Les deux hypothèses à départager :

- **$H_A$** : A surpasse B, C et D (test de Holm, $\alpha=0.05$).
- **$H_B$** : une transition de phase observable apparaît dans C à $d\approx d^*$, et elle est absente de A.

D doit égaler C. Sinon, le gain de A ne vient pas de la fidélité, et SECMR est réfuté.
