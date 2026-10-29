BASSIN_MATH: Grammaire-Sequitur-Chaitin-ZivMerhav-LempelZiv (GSCZ-LZ)
LOI_PROPOSEE: L'essaim maximise la divergence de compression croisée de Ziv-Merhav sur des grammaires hors-contexte sans préfixe (Sequitur) extraites gratuitement par `jev-1.14.0`, n'allouant les jetons LLM qu'aux nœuds-charnières proches de la borne d'incomplétude de Chaitin ($\Omega_L$).

**1. Auto-organisation hors-poids et allocation budgétaire :**
Le graphe de citations et d'études (arXiv, Alignment Forum, GitHub) est traité comme une suite finie de symboles. Le classifieur gratuit `jev-1.14.0` opère en continu une inférence grammaticale hiérarchique par l'algorithme de Nevill-Manning (Sequitur), générant un dictionnaire de règles sans préfixe $G_i$ pour chaque silo $i$ (unicité des digrammes, utilité des règles $\ge 2$). 
La topologie de l'essaim mute hors-poids en fusionnant les agents dont la divergence de Ziv-Merhav $\Delta_{ZM}(S_1 || S_2) = \frac{1}{|S_2|} [C_{LZ}(S_1 \cdot S_2) - C_{LZ}(S_1)]$ dépasse un seuil critique, où $C_{LZ}$ est la longueur de codage Lempel-Ziv-78. 
Allocation des 120 USD : Gemini (20$) effectue un élagage rapide des productions grammaticales redondantes. Claude (100$) est déclenché exclusivement lorsque `jev-1.14.0` détecte une singularité de Chaitin : deux sous-grammaires $G_A, G_B$ incompressibles séparément ($|G| > L - c$) mais dont la concaténation produit une chute brutale de longueur de description minimale (MDL) via une règle-pont non-terminale unique $R^*$.

**2. Fonction objectif anti-vernis :**
$$\mathcal{J}(G_A, G_B, H_A, H_B) = \Delta_{ZM}(G_A || G_B) \cdot \left( |G_A| + |G_B| - |G_{A \cup B}| \right) \cdot \exp\left( - \frac{C_{LZ}(E(H_A) \cdot E(H_B)) - [C_{LZ}(E(H_A)) + C_{LZ}(E(H_B))]}{\max(C_{LZ}(E(H_A)), C_{LZ}(E(H_B)))} \right)$$
où $E(H)$ est la trace d'exécution des activations de Llama-3.1-8B/70B sous intervention causale. Le premier terme garantit la distance inter-silos ; le second impose une compression structurelle profonde (anti-vernis) ; le troisième force l'orthogonalité algorithmique des prédictions expérimentales ($H_A \perp H_B$).

**3. Pont inédit et duel causal :**
*Étude A :* Grammaires de circuits et têtes
