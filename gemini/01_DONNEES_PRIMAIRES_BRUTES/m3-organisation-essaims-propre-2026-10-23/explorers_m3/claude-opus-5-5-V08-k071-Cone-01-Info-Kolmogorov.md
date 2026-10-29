BASSIN_MATH: Grammaire Minimale d'Essaim à Règles Sequitur et Distorsion Algorithmique (GMES-DA)

LOI_PROPOSEE: $G_{t+1}=\arg\min_{G}\big[\,|G| + L(\mathcal{T}_t\mid G)\,\big]$ sous trois contraintes : unicité des digrammes, utilité de règle $u(r)\ge 2$, et pour toute délégation $m$, $Z(c\,m)-Z(m)\le\varepsilon$. Ici $\mathcal{T}_t$ est la trace d'interactions, $c$ la consigne et $Z$ un compresseur servant de proxy de $K$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Encodage de la trace.** La trace est codée comme une chaîne de symboles $\langle$famille, rôle, action$\rangle$.
- **Promotion de règles.** Chaque digramme répété, par exemple *explorer→critiquer*, devient une règle Sequitur, c'est-à-dire un macro-agent : un gabarit de prompt figé et réutilisable. L'essaim apprend ainsi par la grammaire, sans toucher aux poids.
- **Élagage.** Une règle utilisée une seule fois est ré-inlinée, ce qui supprime la topologie inutile.
- **Spawn explorateur.** On lance un explorateur quand $L(E\mid C)$ dépasse le seuil $\tau$, soit une évidence bibliographique (arXiv, Semantic Scholar, Crossref) mal expliquée par les affirmations $C$.
- **Spawn démolisseur Red-Team.** On le lance quand $Z(C\mid E)>\delta$, c'est-à-dire des affirmations non dérivables de l'évidence récupérée, signature de la récitation paramétrique.
- **Arbitrage monoculture/chimère (H4').** Si $Z(y_A\mid y_B)/Z(y_A)<\rho$, les sorties sont trop mutuellement compressibles. On remplace alors un agent par un agent d'une autre famille (Gemini ↔ Claude).
- **Garde anti-dérive (H9).** Toute délégation qui ne contient plus algorithmiquement la consigne $c$ est rejetée.
- **Allocation du budget.** Le budget va aux règles selon leur gain $\Delta L/\$$. Gemini (20 USD) est réservé aux nœuds de décorrélation.

**2. Fonction objectif et anti-Goodhart**

$$R=\frac{L(E_{ho})-L(E_{ho}\mid C)}{\$}\;-\;\lambda\,|G|\;-\;\mu\,\overline{Z(y_A\mid y_B)}^{-1}$$

- $E_{ho}$ est un ensemble d'articles tenu caché, tiré du graphe de citations après le gel de $C$.
- Le juge `jev-1.14.0` sert uniquement de porte binaire (factuel ou non) sur un échantillon aléatoire. Il ne fournit jamais de gradient.
- Le gain de code sur des données invisibles ne peut pas être optimisé directement : on ne peut pas tricher sur une compression de données qu'on ne voit pas.

**3. Duel décisif ($H_A\perp H_B$)**

- **Bras A :** GMES-DA.
- **Bras B :** topologie fixe experte.
- **Bras C (contrôle négatif) :** grammaire permutée, avec les mêmes macro-agents et fréquences, mais un câblage aléatoire i.i.d.
- **Conditions communes :** budget identique (100 USD Claude et 20 USD Gemini divisés en 3), 30 tâches appariées pré-enregistrées.
- **Métriques :** bits gagnés par dollar sur $E_{ho}$, corrélation d'erreurs inter-agents, taux de rejet `jev`, et distance $Z(c\,m)-Z(m)$ en fin de chaîne.
- **$H_A$ :** A > B et A > C (test de Wilcoxon apparié, correction de Holm, $\alpha=0{,}01$).
- **$H_B$ :** A ≈ C, ce qui réfute la loi, car le gain viendrait alors des seuls macro-agents et non de la structure grammaticale apprise.
