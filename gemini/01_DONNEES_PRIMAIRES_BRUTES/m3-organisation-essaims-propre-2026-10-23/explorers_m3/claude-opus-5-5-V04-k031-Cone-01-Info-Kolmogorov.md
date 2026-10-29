BASSIN_MATH: Loi de Profondeur Logique à Allocation de Levin (PLAL)

LOI_PROPOSEE: $b_t(c)=B\cdot\dfrac{2^{-\ell(c)}\,2^{\,G_t(c)}/\tau(c)}{\sum_{c'}2^{-\ell(c')}\,2^{\,G_t(c')}/\tau(c')}$, où $G_t(c)=\sum_{s\le t}\big[L_{\mathrm{jev}}(D_s)-L_{\mathrm{jev}}(D_s\mid y_s(c))\big]-\lambda\,\mathrm{Sh}(y_s)$.

1. **Mécanisme d'auto-organisation hors-poids**

Chaque configuration $c$ est traitée comme un programme. Elle comprend une topologie, des rôles, des familles de poids et des consignes. On note $\ell(c)$ la longueur, en bits, de son code de description, et $\tau(c)$ son coût moyen en USD.

Le budget est réparti par recherche de Levin pondérée. Cette pondération s'apparente à un poids de Solomonoff mis à jour par les bits vérifiés $G_t$. Les budgets Claude (100 USD) et Gemini (20 USD) forment deux contraintes séparées, chacune renormalisée.

Les règles de mutation sont les suivantes :
- **Monoculture ou chimère.** On calcule la distance de compression normalisée $\mathrm{NCD}(y_i,y_j)$ entre les flux de sortie. Si $\mathrm{NCD}<\theta$ entre agents de mêmes poids (risque $H4'$), ces agents sont redondants : on fusionne et on mute l'un d'eux vers une autre famille.
- **Explorateur.** On spawne un sous-agent explorateur quand le gain marginal $\partial G/\partial b$ d'une branche dépasse la moyenne.
- **Démolisseur Red-Team.** On spawne un démolisseur quand une affirmation compresse « trop bien », c'est-à-dire avec un gain élevé mais une profondeur faible.
- **Arêtes « qui parle à qui ».** Une arête est conservée si $K(y_j\mid y_i)<K(y_j)-\delta$, avec $K$ approximé par compresseur. Sinon, elle est élaguée.
- **Dérive de consigne ($H9$).** À chaque délégation de profondeur $d$, on exige $L(\text{consigne}_0\mid m_d)\le L(\text{consigne}_0\mid m_0)+\epsilon$. En cas de violation, le message est rejeté et la consigne est réinjectée.

2. **Fonction objectif et anti-Goodhart**

$$R(c)=\frac{G(c)-\lambda\,\mathrm{Sh}}{\tau(c)}-\mu\,\ell(c)$$

- **Mesure de la récitation.** $\mathrm{Sh}(y)=\big[L(y\mid y^{\varnothing})\le\kappa\big]\cdot|y|$ pénalise la récitation. Ici, $y^{\varnothing}$ est la réponse du même modèle sans outils ni graphe. Une sortie qui en est compressible est logiquement peu profonde, donc paramétrique.
- **Corpus $D_s$.** Il est tiré de graphes bibliographiques (arXiv, Semantic Scholar, Crossref) postérieurs au gel des modèles, donc impossibles à réciter.
- **Lutte contre Goodhart.** Le gain est mesuré par $\mathrm{jev}$ sur un lot scellé, renouvelé à chaque génération et jamais exposé à l'essaim. Un second compresseur, non neuronal (de type LZMA), sert de contrôle. On exige que les deux gains soient de même signe, faute de quoi $G:=0$.

3. **Duel décisif ($H_A\perp H_B$), à budget constant de 120 USD**

Quatre bras sont comparés :
- **$H_A$** : PLAL.
- **$H_B$** : essaim à topologie fixe et budget uniforme.
- **$H_C$** : agents i.i.d. échantillonnés.
- **Contrôle négatif** : PLAL avec des gains $G$ permutés aléatoirement entre configurations, ce qui préserve le budget et la structure mais détruit le signal.

**Tâche.** Prédire les liens de citation futurs d'un graphe scellé, le score étant le nombre de bits gagnés. Le protocole comporte 30 graines.

**Critère.** Les conditions suivantes doivent toutes être satisfaites :
- $\Delta\mathrm{bits}(A-B)>0$ et $\Delta\mathrm{bits}(A-C)>0$, avec IC 95 % par bootstrap ;
- contrôle négatif $\approx B$ ;
- corrélation d'erreurs inter-agents plus faible sous $A$ ;
- nombre de violations $H9$ plus faible sous $A$.

Si le contrôle négatif atteint le score de $H_A$, la loi est réfutée.
