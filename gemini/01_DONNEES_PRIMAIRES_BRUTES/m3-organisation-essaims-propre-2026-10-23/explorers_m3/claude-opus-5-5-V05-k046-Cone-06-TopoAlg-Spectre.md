BASSIN_MATH: Rétraction de Chemins GLMY à Carrés Hétérogames (RCG-CH)

LOI_PROPOSEE: $\Delta E_t=\arg\max_{e}\dfrac{\sum_{\gamma\in\mathrm{Bar}_1}\,\ell(\gamma)\,m(\gamma)\,\mathbb 1[e\text{ tue }\gamma]}{c(e)}$ sous $\sum c\le B$, où $\mathrm{Bar}_1$ est le code-barres de l'homologie de chemins $H_1^{\mathrm{GLMY}}$ du digraphe de délégation filtré par l'accord `jev`, $\ell(\gamma)$ la durée de vie d'une classe et $m(\gamma)$ sa fraction monoculturelle.

1. **Mécanisme d'auto-organisation hors-poids**
   - **Graphe.** Les nœuds sont les agents étiquetés par famille $f\in\{\text{fable},\text{opus},\text{argon}\}$. Un arc $i\to j$ représente une délégation, pondérée par $s_{ij}=$ `jev`(consigne racine, sortie de $j$). On filtre par $s\ge\tau$.
   - **Chaîne non vérifiée.** Une chaîne $i\to j\to k$ n'est homologiquement triviale que si elle borde un carré $i\to j'\to k$ avec $f(j')\neq f(j)$. Un 1-cycle persistant signale donc une affirmation qui n'a jamais été vérifiée indépendamment (risque `H4'`).
   - **Explorateur ou démolisseur.** On spawne un *explorateur* lorsque $\dim\ker L_0$ croît, c'est-à-dire quand des composantes de sources sont déconnectées. On spawne un *démolisseur Red-Team* d'une famille différente sur le $\gamma$ maximisant $\ell\,m$.
   - **Élagage.** On supprime tout arc dont le retrait laisse le code-barres invariant (distance bottleneck nulle).
   - **Dérive de consigne (`H9`).** Elle se mesure par le trou spectral $\lambda_1(L_1^{\mathrm{path}})$. Si $\lambda_1<\epsilon$, on réinjecte la consigne racine par un arc direct.
   - **Monoculture ou chimère.** La chimère n'est achetée que lorsque $m(\gamma)\,\ell(\gamma)>c_{\text{Gemini}}/c_{\text{Claude}}$, ce qui alloue rationnellement les 20 USD Gemini.
   - **Apprentissage.** Il se fait uniquement par mémoire externe des codes-barres et des règles d'arcs gagnants, sans toucher aux poids.

2. **Fonction objectif et anti-Goodhart**
$$R=\frac{V_{\text{ext}}}{N}-\alpha\sum_{\gamma}\ell(\gamma)\,m(\gamma)-\beta\,\frac{\text{coût}}{B}-\eta\,\big|\rho(\texttt{jev},V_{\text{ext}})_t-\rho_0\big|$$
   - $V_{\text{ext}}$ compte les affirmations vérifiées hors du juge : DOI résolu via Crossref et ancrage dans le graphe Semantic Scholar à distance $\le2$ des sources citées. Ce critère neutralise la récitation de la mémoire paramétrique.
   - `jev` ne sert qu'à la filtration et n'entre jamais directement dans $R$.
   - Le dernier terme pénalise toute dérive de corrélation entre juge et vérité externe, ce qui sert de détecteur de Goodhart.

3. **Duel décisif ($H_A\perp H_B$)**
   - **Hypothèses.** $H_A$ : le gain provient des carrés hétérogames. $H_B$ : le gain provient seulement d'une densité accrue d'arcs ou de dépense.
   - **Bras, à budget identique** (120 USD) et sur $N=200$ tâches bibliographiques pré-enregistrées :
     - (a) RCG-CH ;
     - (b) essaim fixe en étoile, même mélange de familles ;
     - (c) contrôle négatif i.i.d. : rebrassage préservant les degrés, même nombre d'arcs et même coût ;
     - (d) placebo : RCG-CH calculé sur des étiquettes de famille permutées.
   - **Métriques.**
     - $V_{\text{ext}}/N$ ;
     - taux de citations fabriquées ;
     - dérive $1-s$ à profondeur 3.
   - **Test.** Test de permutation apparié, avec correction de Holm.
   - **Critères de décision.**
     - $H_A$ est validée si (a) > (d) ≈ (c), ce qui isole l'hétérogamie à densité constante.
     - $H_B$ est retenue si (d) ≈ (a), auquel cas la loi est réfutée.
