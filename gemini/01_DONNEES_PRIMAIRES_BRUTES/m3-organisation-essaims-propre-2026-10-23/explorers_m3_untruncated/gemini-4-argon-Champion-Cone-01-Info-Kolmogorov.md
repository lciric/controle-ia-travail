BASSIN_MATH: Compression-Kolmogorov-Wyner-MDL
LOI_PROPOSEE: $k_{t+1}, T_{stop} = \arg\min_{k_t, s_t} \left[ \frac{L(C_0 | Y_t) + \lambda C_{Wyner}(Y_t^{Claude}, Y_t^{Gemini})}{JEV(Y_t) \cdot K_{Zlib}(Y_t | G_{arXiv})} \right]$ sous contrainte $\sum c_t \le B_{max}$

1. **Mécanisme d'Auto-Organisation (Essaim + Collisionneur Adaptatif)** :
L'apprentissage sans poids opère par minimisation de la Longueur de Description Minimale (MDL, Rissanen 1978, `(référence à vérifier)`). L'état de l'essaim au tour $t$ est un programme génératif produisant les sorties $Y_t = \{y_{1,t}, \dots, y_{k_t,t}\}$.
- **Routage prédateur inter-espèces (contre `H4'`)** : On estime l'Information Commune de Wyner (Wyner 1975, `(référence à vérifier)`) entre sous-essaims par la Distance de Compression Normalisée $NCD(y_i, y_j) = \frac{Z(y_i y_j) - \min(Z(y_i), Z(y_j))}{\max(Z(y_i), Z(y_j))}$ (Li et al. 2004, `(référence à vérifier)`), où $Z$ est la taille compressée (zlib). Si la redondance intra-famille (monoculture Claude) dépasse un seuil $\tau_{W} = 0.65$ (`illustratif`), le routeur alloue du budget Gemini (20 USD) pour injecter une réfutation orthogonale, maximisant l'incompressibilité croisée.
- **Taille $k_t$ et arrêt adaptatif $T$ (contre `H9`)** : `claude-fable-5-1` explore en essaim large ($k_1 = 6$ `illustratif`) tant que le gain de compression $\Delta Z(Y_t | G_{arXiv}) > \epsilon = 0.05$ (`illustratif`). Dès stagnation, réduction à $k_t = 2$ (`illustratif`) avec `claude-opus-5-5` et `gemini-4-argon` en collisionneur frontal. Le système stoppe à $T$ dès que la complexité de reconstruction de la consigne initiale $C_0$ depuis $Y_t$, notée $L(C_0 | Y_t)$ et évaluée par `jev-1.14.0`, diverge (dérive `H9`), ou que le gain MDL par dollar tombe sous $0.01\text{ bit/USD}$ (`illustratif`).

2. **Fonction Objectif & Anti-Goodhart** :
Pour contrer la récitation paramétrique et le piratage de `jev-1.14.0` (sorties vides ou gabarits répétitifs), le signal de récompense unilatéral $R(Y_t)$ pénalise la redondance interne et l'absence de nouveauté face au graphe bibliographique gratuit $G_{arXiv}$ :
$$R(Y_t) = JEV(Y_t) \cdot \underbrace{\left( \frac{Z(Y_t \cup G_{arXiv}) - Z(G_{arXiv})}{|Y_t|} \right)}_{\text{Anti-Gabarit \& Anti-Récitation}} \cdot \underbrace{\left( 1 - \exp\left(-\frac{Z(Y_t)}{Z_{min}}\right) \right)}_{\text{Anti-Vide}} \cdot \exp\left(-NCD(Y_t, C_0)\right)$$
Une sortie vide annule $Z(Y_t)$ ($Z_{min} = 500\text{ octets}$ `illustratif`). Un gabarit lexical ou une récitation d'arXiv s'effondre sous compression conditionnelle $Z(Y_t \cup G_{arXiv}) - Z(G_{arXiv}) \to 0$.

3. **Duel Décisif de Validation M3 ($H_A \perp H_B$)** :
- **Protocole** : Budget constant de $5\text{ USD}$ Claude et $1\text{ USD}$ Gemini (`illustratif`) sur 10 problèmes M3 (`illustratif`).
- **Hypothèse $H_A$ (Auto-organisation MDL-Wyner)** : Topologie dynamique $k_t, T$ pilotée par $R(Y_t)$ et le routage $NCD$.
- **Hypothèse $H_B$ (Contrôle négatif statique)** : Topologie fixe ($T=3, k=3$ `illustratif`), allocation aléatoire des mêmes budgets et modèles sans rétroaction de compression.
- **Observable unique $O$** : Score d'innovation nette compressée par dollar, $O = \frac{R(Y_T)}{\text{Coût Total USD}}$.
- **Intervalles disjoints** : Validation de $H_A$ si $O \in I_A = [0.45, 1.00]$ (`illustratif`) ; validation de $H_B$ si $O \in I_B = [0.00, 0.35]$ (`illustratif`), avec $I_A \cap I_B = \emptyset$. Ce protocole garantit la sélection d'une topologie apprenante optimale sans réentraînement. FIN-EXPLORATEUR-M3
