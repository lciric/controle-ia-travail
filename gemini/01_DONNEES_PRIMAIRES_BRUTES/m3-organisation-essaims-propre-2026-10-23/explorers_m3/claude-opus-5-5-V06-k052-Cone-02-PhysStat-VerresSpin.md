BASSIN_MATH: Ligne AT-Nishimori de Spawn (AT-NISH)

LOI_PROPOSEE: $m_i=\tanh\!\big(\beta_N h_i+\beta_N\sum_j J_{ij}m_j-\beta_N^2 m_i\sum_j J_{ij}^2(1-m_j^2)\big)$, $\lambda_{AT}=1-\frac{\beta_N^2}{N}\sum_{ij}J_{ij}^2(1-m_i^2)(1-m_j^2)$, avec $\beta_N=\tfrac12\ln\frac{a}{1-a}$, où $a$ est l'exactitude de `jev` sur une partition cachée. On spawne un d?molisseur si $\lambda_{AT}>\epsilon$ et un explorateur si $\lambda_{AT}<-\epsilon$.

**1. M?canisme d'auto-organisation hors-poids**

Chaque agent $i$ de famille $f(i)$ porte un spin $s_i=\pm1$, son verdict sur une affirmation. $h_i$ est le champ externe fourni par `jev` et par les graphes bibliographiques. $J_{ij}$ est la confiance de $j$ vers $i$, apprise de fa?on hebbienne sur les labels retenus : $\Delta J_{ij}=\eta(y-m_i)\,m_j$. Ce sont les seules variables apprises, sans aucune modification des poids.

Le terme d'Onsager retranche l'?cho de soi. Il p?nalise ainsi la r?citation param?trique et les accords dus ? des poids partag?s (`H4'`).

La topologie suit le signe du r?plicon $\lambda_{AT}$ :
- **$\lambda_{AT}>0$ (phase RS, consensus stable)** : le risque est la fausse unanimit?. On spawne alors un Red-Team d'une famille diff?rente.
- **$\lambda_{AT}<0$ (phase RSB, plusieurs ?tats de Parisi)** : on spawne un explorateur charg? de la requ?te bibliographique qui s?pare le mieux les ?tats.

L'arbitrage entre monoculture et chim?re se fait par les recouvrements. Si $q_{ff}-q_{ff'}>\delta$, la famille est surcorr?l?e : on chim?rise. Sinon, on garde la monoculture, moins ch?re.

Contre la d?rive de consigne (`H9`), toute d?l?gation recopie $h_i$ d'origine, et un enfant ne peut modifier que $J$.

Le budget est allou? proportionnellement ? $\partial\lambda_{AT}/\partial(\text{USD})$, avec un plafond de 100 USD pour Claude et de 20 USD pour Gemini.

**2. Fonction objectif et anti-Goodhart**

$$R=\frac{I(s;y_{\text{cach?}})}{\text{USD}}-\mu\,|q_{ff}-q_{ff'}|-\nu\,\big|\overline{m}-\overline{m^2}\big|_{\text{Nishimori}}$$

Sur la ligne de Nishimori, l'identit? $\mathbb E[m]=\mathbb E[m^2]$ est exacte. Sa violation signale donc un surajustement au juge, c'est-?-dire Goodhart. De plus, les labels `jev` tournent par blocs cach?s, de sorte que $J$ n'en voit jamais la partition d'?valuation.

**3. Duel d?cisif ($H_A\perp H_B$)**

On utilise 400 affirmations plant?es, de v?rit? connue et post?rieures ? la coupure d'entra?nement, ? budget strictement identique. Les bras compar?s sont :
- (A) AT-NISH ;
- (B) un essaim ? topologie fixe ;
- (C) des agents i.i.d. avec vote majoritaire ;
- (N1) un contr?le n?gatif o? $J$ est permut? ? spectre conserv? ;
- (N2) une variante o? $\beta\neq\beta_N$.

Les m?triques sont l'exactitude, la corr?lation inter-erreurs par famille et le nombre de r?tractations.

- **$H_A$** : A d?passe B et C de plus de 5 points, avec un intervalle bootstrap ? 95 % qui exclut z?ro.
- **$H_B$** : ce gain s'annule sous N1 et N2.

Si $H_A$ est vraie sans $H_B$, le gain vient du budget ou du hasard, et non de la loi. La loi est donc r?fut?e. Le protocole est pr?enregistr?, avec cinq graines.
