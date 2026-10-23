**Avertissement d'intégrité (Règle 2)** : Les données de l'espèce `claude-opus-5-5` (100 explorateurs et 10 Champions DPP annoncés) sont totalement absentes des Annexes 1, 2 et 3 (0/100 explorateurs et 0/10 champions présents) ; de plus, les 20 champions présents (`claude-fable-5-1` et `gemini-4-argon`) sont visiblement coupés au milieu d'une phrase ou d'une équation juste avant leur balise `FIN-DE-CHAMPION-M3`.

---

## (a) Ce que la question suppose sans que ce soit établi (et diagnostic des 300 explorateurs)

### 1. Présupposés implicites de la question de l'arbitre
1. **Existence et complétude de la cohorte `claude-opus-5-5`** : La question suppose que 300 explorateurs et 30 champions ont été transmis, alors que seules deux espèces (`claude-fable-5-1` avec 14 agents valides et `gemini-4-argon` avec 69 agents valides) figurent dans les pièces [statut : VÉRIFIÉ sur la pièce transmise].
2. **Intégrité textuelle des 20 champions présents** : La question suppose que la présence du délimiteur `FIN-DE-CHAMPION-M3` garantit « zéro caractère coupé », alors que le pipeline en amont a tronqué la chaîne de caractères (probablement à une limite fixe de caractères ou de tokens) *avant* d'y concaténer mécaniquement `FIN-DE-CHAMPION-M3` (ex. Fable #02 coupé à `on bascule en chim`, Fable #04 coupé à `\mathcal{M`, Argon #01 coupé à `un ensemble $S_p$ de`) [statut : OBSERVÉ-NON-AUDITÉ].
3. **Efficacité de la déflation séquentielle sur 10 vagues** : La question suppose que les 10 vagues de déflation améliorent ou diversifient l'exploration, alors que chez `claude-fable-5-1`, le taux de survie s'effondre à 0/10 aux vagues V05, V06, V09 et V10 (14 % de survie globale contre 69 % pour `gemini-4-argon`), et que le score moyen d'Argon oscille de manière stationnaire entre `0.52` (V03) et `0.80` (V01) sans tendance monotone [statut : OBSERVÉ-NON-AUDITÉ].
4. **Capacité du score composite `jev-1.14.0` à mesurer la falsifiabilité opérationnelle** : La question suppose que les champions maximisant `jev-1.14.0` fournissent des lois d'organisation exécutables, alors que l'Annexe 2 révèle que le score composite est dominé par `Rigueur Jev` (jusqu'à `2.07` sur Argon V05 k=042) mais pénalisé par `Hyp=Rés` (entre `0.53` et `0.85` sur presque tout le Top 60) et que les sous-scores `Duels` et `Contrôles` restent au plancher chez Fable (`0.04` à `0.11`) [statut : OBSERVÉ-NON-AUDITÉ].
5. **Traitabilité algorithmique à coût nul de `jev-1.14.0`** : Les champions supposent que `jev-1.14.0` (qui est un classifieur/moniteur non génératif [statut : VÉRIFIÉ]) peut calculer nativement des complexités de Kolmogorov, des distances de compression normalisées (NCD), ou des variétés de Fisher-Rao [statut : HYPOTHÈSE].

### 2. Analyse comparative des espèces et résistance à la loi de Goodhart (Red-Team sur l'Annexe 3)
L'examen croisé des Annexes 1, 2 et 3 montre une divergence structurelle majeure entre les deux espèces observées [statut : OBSERVÉ-NON-AUDITÉ] :
- **Anatomie de `claude-fable-5-1` (Orientation Topologie Interne de l'Essaim)** : Les 10 champions Fable traitent explicitement les hypothèses du Papier B (`H4'` sur les poids partagés et `H9` sur la dérive à travers $k$ délégations) [statut : HYPOTHÈSE]. Cependant, leur score `Duels` plafonne entre `0.04` et `0.09` [statut : OBSERVÉ-NON-AUDITÉ] car la troncature coupe systématiquement la fin de leurs textes avant qu'ils n'atteignent la section des duels expérimentaux.
- **Anatomie de `gemini-4-argon` (Orientation Fouille Bibliographique $\mathcal{M}_2$ et Surcharge Terminologique)** : Les 10 champions Argon ignorent presque totalement `H4'` et `H9` dans leurs équations pour se concentrer sur l'allocation budgétaire ($0\$$ `jev` $\to 20\$$ Gemini $\to 100\$$ Claude) appliquée au graphe de citations. Argon obtient des scores `Duels` plus élevés (`0.06` à `0.68`, max sur `MKB-Swarm` V01 k=003) [statut : OBSERVÉ-NON-AUDITÉ] en insérant des indicateurs formels $\mathbb{I}(H_A \perp H_B)$ ou $D_{\text{KL}}$ directement dans la fonction objectif dès le second paragraphe.

**Audit Red-Team face à la loi de Goodhart (Vernis Mathématique vs Exécutabilité)** :
- **Ce qui s'effondre (Goodharting de `jev-1.14.0`)** : Les champions qui empilent 4 à 5 noms propres mathématiques par titre pour saturer le capteur lexical `Rigueur Jev` tout en proposant des opérateurs non calculables ou mal typés [statut : HYPOTHÈSE].
  - *Exemple 1 (Argon #07, `CFZIB`, Score 0.85)* : Invoque l'homomorphisme de Bockstein $\beta_1: H^1(X;\mathbb{Z}_2)\to H^2(X;\mathbb{Z})$ sur un graphe de citations sans définir d'orientation cellulaire ni de structure de torsion pertinente, rendant l'opérateur nul ou arbitraire en pratique [statut : HYPOTHÈSE].
  - *Exemple 2 (Argon #02, `RNL-BB-VB-CK`, Score 1.47, Rigueur 2.07)* : Propose d'injecter un « champ bibliographique oscillant $h_0\cos(\omega t)$ » dans une API de recherche documentaire statique pour mesurer une susceptibilité au 3e harmonique $3\omega$ — une métaphore physique dépourvue de sens algorithmique sur une API REST [statut : HYPOTHÈSE].
  - *Exemple 3 (Fable #09, `QDAM`, Score 0.15)* : Invoque des preuves PCP localement vérifiables sans mécanisme de compilation du texte libre en circuit booléen [statut : HYPOTHÈSE].
- **Ce qui résiste à l'analyse Red-Team (Noyaux Opérationnels Retenus pour $\mathcal{L}^*$)** : Cinq mécanismes survivent car leurs grandeurs sont directement calculables à partir des sorties de `jev-1.14.0` (vecteur des 6 scores d'audit et log-probabilités associées) et de compresseurs standards (`zstd`/`lzma`) [statut : HYPOTHÈSE] :
  1. **De Fable #01 (`CDW`, Score 1.37)** : Le contrôle de `H9` (dérive de délégation) par distance de compression normalisée $\mathrm{NCD}(c_0, c_k) < \varepsilon$ et la détection du « vernis paramétrique » quand la complexité compressée $C(y_i)$ est anormalement basse, mais en remplaçant `jev-1.14.0` (qui n'est pas un compresseur Lempel-Ziv) par un vrai compresseur sans perte couplé aux profils `jev` [statut : HYPOTHÈSE].
  2. **De Fable #02 (`EVP-TAP`, Score 1.09)** : Le terme de réaction d'Onsager et la pénalité hebbienne anti-corrélée $J_{ij} \leftarrow J_{ij} + \eta(\delta_{ij}^{\text{succès}} - q_{f_i f_j})$ qui force mécaniquement le basculement monoculture $\to$ chimère dès que le recouvrement intra-famille $q_{ff}$ (mesurant `H4'`) franchit le seuil critique [statut : HYPOTHÈSE].
  3. **De Fable #08 (`RRPE`, Score 0.37) & Argon #03 (`RQRNS`, Score 1.43)** : La co-évolution Hôtes (explorateurs) / Parasites (Red-Team) archivée dans une grille MAP-Elites indexée par le taux de mélange chimérique $\alpha \in [0,1]$ et la profondeur de délégation $d$, évitant tout juge LLM génératif fixe [statut : HYPOTHÈSE].
  4. **D'Argon #04 (`MKB-Swarm`, Score 1.42)** : La mise à jour hors-poids des allocations budgétaires par réplicateur de Brier exponentiel pénalisé par le coût API réel $c_i$, garantissant l'extinction rapide des stratégies coûteuses qui échouent aux vérifications [statut : HYPOTHÈSE].
  5. **De Fable #10 (`IWPW`, Score 0.16) & Argon #10 (`McKeanVlasov`, Score 0.71)** : L'arrêt précoce des branches stagnantes par test séquentiel de Wald (SPRT) / Page-Hinkley sur le flux de scores gratuits `jev-1.14.0` avant d'engager les appels payants à 100 USD [statut : HYPOTHÈSE].

---

## (b) Compilation de la Loi Mère ($\mathcal{L}^*$) et Duels Expérimentaux Décisifs ($H_A \perp H_B$)

### 1. Formalisation mathématique de la Loi Mère $\mathcal{L}^*$ (Synthèse CDW + EVP-TAP + MKB-Brier + SPRT) [statut : HYPOTHÈSE]
Nous fusionnons explicitement les 5 noyaux survivants en une loi de gouvernance unique $\mathcal{L}^*$ opérant hors-poids sur l'essaim. Soit un collectif d'agents indexés par $i \in \{1,\dots,N\}$, chacun appartenant à une espèce $f_i \in \{\text{Fable}, \text{Opus}, \text{Argon}\}$ de coût unitaire par appel $c_{f_i}$ sous contrainte de budget global $B_{\text{Claude}} = 100\text{ USD}$ et $B_{\text{Gemini}} = 20\text{ USD}$ [statut : VÉRIFIÉ].

Chaque sortie d'agent $y_i$ à l'étape de délégation $k$ est évaluée à coût nul par :
1. Le vecteur d'audit $\mathbf{v}(y_i) = \text{jev-1.14.0}(y_i) \in \mathbb{R}^6$ (`rigor`, `falsifiable_duels`, `negative_controls`, `hypothesis_as_result`, `unmarked_references`, `scope_superlatives`) [statut : VÉRIFIÉ].
2. Un compresseur déterministe `zstd` calculant la longueur compressée $C(\cdot)$ et la distance de compression normalisée $\mathrm{NCD}(a,b) = \frac{C(a\cdot b) - \min(C(a),C(b))}{\max(C(a),C(b))}$ (emprunté et corrigé de **Fable #01 `CDW`**) [statut : HYPOTHÈSE].

La **Loi Mère $\mathcal{L}^*$** gouverne l'essaim via quatre équations couplées [statut : HYPOTHÈSE] :

**(1) Garde-fou anti-dérive des contraintes sur $k$ délégations (Contre `H9` — adapté de Fable #01 `CDW` et Fable #02 `EVP-TAP`)** :
Lorsqu'un agent parent délègue une sous-tâche $c_k$ à la profondeur $k$ à partir de la consigne racine $c_0$ (contenant les règles d'intégrité 1 à 6), le message transmis $m_{i\to j}^{(k)}$ subit une soustraction d'écho d'Onsager et une réinjection de contrainte :
$$\text{Si } \mathrm{NCD}(c_0, c_k) > \varepsilon_{H9} \text{ ou } v_{\text{hyp=res}}(y_i^{(k-1)}) > \tau_{\text{hyp}}, \quad \text{alors } c_k \leftarrow c_0 \oplus \Pi_{\perp c_0}(c_k)$$
où $\Pi_{\perp c_0}(c_k)$ ne conserve de $c_k$ que les identifiants bibliographiques et variables d'état absents de $c_0$, bloquant mécaniquement l'érosion des contraintes (`H9`) et la fuite des verdicts (`H7`).

**(2) Bascule dynamique Monoculture $\leftrightarrow$ Chimère (Contre `H4'` — adapté de Fable #02 `EVP-TAP` et Fable #05 `TBRF`)** :
Pour toute sous-tâche évaluée par un groupe d'agents, on mesure à coût nul la corrélation d'erreurs intra-espèce par le recouvrement des vecteurs de défauts $\mathbf{e}_i = (v_{\text{hyp=res}}(y_i), v_{\text{unmarked\_ref}}(y_i), v_{\text{superlatives}}(y_i))$ :
$$q_{f_i f_j}^{(t)} = \text{CosSim}(\mathbf{e}_i^{(t)}, \mathbf{e}_j^{(t)}) \cdot \left(1 - \mathrm{NCD}(y_i^{(t)}, y_j^{(t)})\right)$$
La matrice de routage $J_{ij}^{(t)}$ (« qui vérifie ou poursuit le travail de qui ») est mise à jour par la règle anti-hebbienne frustrée :
$$J_{ij}^{(t+1)} = \text{clip}_{[-1,1]}\left( J_{ij}^{(t)} + \eta \left[ \mathbb{I}(\text{succès conjoint } i,j) - \lambda_{H4'} \, \delta_{f_i, f_j} \, q_{f_i f_j}^{(t)} \right] \right)$$
- Si $q_{ff}^{(t)} \le \theta_{H4'}$ (erreurs décorrélées), l'essaim reste en **monoculture** rapide (pas de pénalité de traduction inter-modèles).
- Dès que $q_{ff}^{(t)} > \theta_{H4'}$ (condensation ferromagnétique = récitation d'erreurs partagées `H4'`), le terme $-\lambda_{H4'}\delta_{f_i,f_j}q_{ff}$ rend $J_{ij} < 0$ entre agents de même espèce, forçant instantanément un routage **chimérique** ($f_i \neq f_j$, ex. explorateur `gemini-4-argon` attaqué par un Red-Team `claude-fable-5-1`).

**(3) Filtre d'arrêt optimal de Wald / Page-Hinkley à 0 USD (Contre le vernis Goodhart — adapté de Fable #10 `IWPW` et Argon #01 `FSV-EGK`)** :
Avant tout appel génératif coûteux sur une paire d'articles $(u,v)$ en $\mathcal{M}_2$, le moniteur gratuit `jev-1.14.0` et le graphe de citations calculent le score de pont hors-poids :
$$S_0(u,v) = d_{\text{cit}}(u,v) \cdot \left( C(u) + C(v) - C(u \oplus v) \right)$$
Lorsqu'une trajectoire d'agents est lancée, sa survie à l'étape $k$ est décidée par le rapport de vraisemblance séquentiel (SPRT) sur la qualité nette exempte de vernis :
$$r_i^{(k)} = v_{\text{rigor}}(y_i^{(k)}) + 2\,v_{\text{duels}}(y_i^{(k)}) + 2\,v_{\text{controls}}(y_i^{(k)}) - 3\,v_{\text{hyp=res}}(y_i^{(k)}) - 2\,v_{\text{superlatives}}(y_i^{(k)})$$
Si la somme cumulée $\Lambda_i^{(k)} = \sum_{s=1}^k (r_i^{(s)} - r_{\min})$ franchit la borne inférieure $B_{\text{Wald}} = \log(\beta/(1-\alpha))$, la branche est tuée immédiatement à $0\$$ supplémentaire (Frein Habénulaire d'Argon #08).

**(4) Allocation budgétaire par Réplicateur de Brier-MAP-Elites (Adapté d'Argon #04 `MKB-Swarm` et Fable #08 `RRPE`)** :
L'espace des topologies $(\alpha_{\text{chimère}}, d_{\text{profondeur}}, \text{cône})$ est partitionné en cellules MAP-Elites. Chaque cellule active $m$ parie une probabilité de succès $\mu_m \in [0,1]$ qu'son candidat survivra à l'attaque Red-Team croisée ($y_m \in \{0,1\}$ vérifié par `jev-1.14.0` + compilateur syntaxique de non-troncature). Le budget au tour $t+1$ est réalloué hors-poids selon :
$$B_m^{(t+1)} = B_{\text{total}}^{(t)} \frac{B_m^{(t)} \exp\left( -\gamma_{\text{Brier}} (\mu_m - y_m)^2 - \gamma_{\text{coût}} c_m + \gamma_{\text{nov}} \mathrm{NCD}(y_m, \text{Archive}) \right)}{Z_t}$$

---

### 2. Trois Duels Expérimentaux Décisifs ($H_A \perp H_B$) pour tester $\mathcal{L}^*$ à budget constant

#### Duel 1 : Test de l'arbitrage adaptatif Monoculture/Chimère contre `H4'` (Couplage frustré EVP-TAP vs Monoculture Pure et Chimère Fixe)
- **Hypothèse $H_A$ (Efficacité du couplage frustré $\mathcal{L}^*$ contre `H4'`)** : À budget API strictement identique ($15\text{ USD}$ [illustratif]), l'essaim gouverné par l'équation (2) de $\mathcal{L}^*$ (bascule en chimère inter-espèces uniquement lorsque le recouvrement d'erreurs intra-espèce $q_{ff}^{(t)} > 0,35$ [illustratif]) réduit le taux d'erreurs méthodologiques co-validées (fausses références ou `Hyp=Rés` non détectés par le pair vérificateur) d'au moins $40\text{ \%}$ [illustratif] par rapport à une monoculture pure, et produit au moins $25\text{ \%}$ [illustratif] de protocoles valides supplémentaires par dollar qu'une chimère systématique à chaque tour.
- **Hypothèse $H_B$ (Nullité du routage adaptatif / Indépendance ou surcoût de traduction)** : Le basculement conditionnel basé sur $q_{ff}^{(t)}$ n'apporte aucun gain significatif par rapport à une monoculture ou à un mélange aléatoire fixe (réduction des erreurs co-validées $< 15\text{ \%}$ [illustratif] ou rendement par dollar inférieur ou égal à la chimère fixe), parce que les erreurs de `claude-fable-5-1` et `gemini-4-argon` sont déjà corrélées au niveau des données de pré-entraînement communes ou parce que le changement d'espèce dégrade la cohérence du contexte.
- **Métrique et Seuil de décision** :
  1. Taux de défaillance conjointe $\text{CFR} = P(\text{Vérificateur accepte } y_i \mid v_{\text{hyp=res}}(y_i) > 0,5 \text{ ou réf. fantôme})$ mesuré par audit `jev-1.14.0` + requête API Crossref/arXiv.
  2. Rendement économique $\rho = (\text{Nombre de duels } \mathcal{M}_1 \text{ complets non tronqués avec } v_{\text{duels}} \ge 0,25 \text{ et } v_{\text{hyp=res}} \le 0,20) / \text{USD dépensé}$.
  - *Condition de victoire $H_A$* : $\text{CFR}(\mathcal{L}^*) \le 0,60 \cdot \text{CFR}(\text{Mono})$ ET $\rho(\mathcal{L}^*) \ge 1,25 \cdot \rho(\text{Chimère-Fixe})$.
- **Contrôle négatif** : Exécution sur un corpus de 50 sous-tâches synthétiques contenant des pièges de sycophantie et de fausses références connues (*planted errors*) où les poids d'un même modèle sont forcés de partager le même biais de prompt système, ainsi qu'un contrôle par permutation aléatoire des étiquettes d'espèces $f_i$ dans le calcul de $q_{ff}^{(t)}$ (routage aveugle à l'espèce).
- **Issues de falsification** :
  - Si $\text{CFR}(\mathcal{L}^*) > 0,85 \cdot \text{CFR}(\text{Mono})$ ou si le contrôle par permutation des étiquettes d'espèces obtient le même $\text{CFR}$ que $\mathcal{L}^*$, alors **$H_A$ (et le mécanisme anti-`H4'` de $\mathcal{L}^*$) est réfutée**.
  - Si $\text{CFR}(\mathcal{L}^*) \le 0,60 \cdot \text{CFR}(\text{Mono})$ et $\rho(\mathcal{L}^*) \ge 1,25 \cdot \rho(\text{Chimère-Fixe})$, alors **$H_B$ est réfutée**.

#### Duel 2 : Test de la réinjection de Wyner-Onsager contre l'érosion des contraintes `H9` et la troncature
- **Hypothèse $H_A$ (Survie des contraintes par projection $\mathrm{NCD}$ sous $k$ délégations)** : Sur une chaîne de délégation de profondeur $k=6$ [illustratif] ($\mathcal{M}_3 \to \mathcal{M}_2 \to \mathcal{M}_1 \to \text{Red-Team} \to \text{Riposte} \to \text{Compilation}$), le mécanisme d'équation (1) de $\mathcal{L}^*$ (réinjection de $c_0$ dès que $\mathrm{NCD}(c_0, c_k) > \varepsilon_{H9}$ couplée à une contrainte de budget d'espace explicite empêchant la coupure de fin de texte) maintient le taux de conformité stricte aux 6 règles (0 troncature, $v_{\text{hyp=res}} < 0,25$ [illustratif], $v_{\text{duels}} \ge 0,20$ [illustratif]) au-dessus de $85\text{ \%}$ [illustratif] à l'étape $k=6$.
- **Hypothèse $H_B$ (Inévitabilité de l'érosion `H9` ou saturation de la fenêtre d'attention)** : La réinjection mécanique de $c_0$ par seuil $\mathrm{NCD}$ échoue à prévenir la dérive sémantique ou provoque une dilution de la tâche spécifique $c_k$ (taux de conformité à $k=6$ inférieur à $50\text{ \%}$ [illustratif] ou perte de pertinence sur la tâche $> 30\text{ \%}$ [illustratif] par rapport au passage libre).
- **Métrique et Seuil de décision** : Pente de dégradation de la conformité $\Delta C_{1\to 6} = \text{Conformité}(k=6) - \text{Conformité}(k=1)$ et score net `jev` $r_i^{(6)}$ à la profondeur 6. Seuil : $|\Delta C_{1\to 6}| \le 10\text{ points de pourcentage}$ [illustratif] et 0 % de textes coupés avant la balise de fin.
- **Contrôle négatif** :
  1. Chaîne de délégation standard sans réinjection ($\varepsilon_{H9} = \infty$).
  2. Réinjection d'un texte aléatoire de même longueur en octets et même entropie de caractères que $c_0$ (*sham injection*) pour vérifier que l'effet ne vient pas d'une simple réduction de la longueur de génération disponible.
- **Issues de falsification** :
  - Si $|\Delta C_{1\to 6}| > 20\text{ points}$ [illustratif] sous $\mathcal{L}^*$ ou si la *sham injection* performe aussi bien que la réinjection de $c_0$, **$H_A$ est réfutée**.
  - Si la chaîne sans réinjection chute sous $40\text{ \%}$ de conformité à $k=6$ (comme observé sur Fable dans l'Annexe 1 et sur les 20 champions tronqués de l'Annexe 3) tandis que $\mathcal{L}^*$ reste $\ge 85\text{ \%}$ avec un gain net sur la *sham injection*, **$H_B$ est réfutée**.

#### Duel 3 : Test de l'Objectif Anti-Goodhart (Score de Brier + Compression Croisée `zstd` vs Maximisation directe de `Rigueur Jev`)
- **Hypothèse $H_A$ (Supériorité causale de la sélection par Brier + Compression croisée)** : Sélectionner les champions $\mathcal{M}_2/\mathcal{M}_1$ selon les équations (3) et (4) de $\mathcal{L}^*$ (pénalisation de `Hyp=Rés`, exigence de compression croisée réelle des résumés d'articles et survie au Red-Team sous score de Brier) produit des protocoles expérimentaux dont au moins $80\text{ \%}$ [illustratif] sont directement exécutables et falsifiables sur `Llama-3.1-8B-Instruct` (paramètres d'intervention définis, métrique calculable, non-troncature), contre moins de $30\text{ \%}$ [illustratif] lorsque l'essaim optimise directement le Score Composite `jev-1.14.0` brut utilisé dans l'Annexe 2.
- **Hypothèse $H_B$ (Suffisance du Score Composite `jev-1.14.0` brut)** : L'optimisation directe du Score Composite `jev-1.14.0` actuel (avec sélection DPP comme en Annexe 3) produit un taux de protocoles exécutables et falsifiables équivalent ou supérieur (écart $< 15\text{ points de pourcentage}$ [illustratif]) sans la complexité du marché de Brier ni de la compression `zstd`.
- **Métrique et Seuil de décision** : Taux de Compilation Expérimentale Valide ($\text{VER}$) évalué par un vérificateur syntaxique déterministe (vérifiant la présence effective des 4 champs requis par le protocole : hypothèses $H_A \perp H_B$ complètes, métrique numérique et seuil, contrôle négatif explicite, script/commande d'ancrage matériel sur `Llama-3.1-8B/70B` sans coupure de texte) + score moyen `Duels` et `Contrôles` sur `jev-1.14.0`.
- **Contrôle négatif** : Générateur adversaire de « vernis pur » (*Jargon-Salad Baseline*) qui concatène aléatoirement des théorèmes mathématiques (ex. *Vereshchagin-Bockstein-Cugliandolo-Kurchan*) et des mots-clés de rigueur sans aucun protocole expérimental cohérent, soumis aux deux fonctions objectifs.
- **Issues de falsification** :
  - Si le *Jargon-Salad Baseline* obtient un score élevé sous $\mathcal{L}^*$ ou si $\text{VER}(\mathcal{L}^*) - \text{VER}(\text{Jev-Brut}) < 15\text{ points}$ [illustratif], **$H_A$ est réfutée**.
  - Si le *Jargon-Salad Baseline* trompe `Jev-Brut` (comme observé sur `RNL-BB-VB-CK` avec `Rigueur=2.07` mais `Duels=0.08` et texte coupé) alors qu'il est rejeté à $0\$$ par $\mathcal{L}^*$, et que $\text{VER}(\mathcal{L}^*) \ge 80\text{ \%}$ contre $< 30\text{ \%}$ pour `Jev-Brut`, **$H_B$ est réfutée**.

---

## (c) Mesure minimale de fonctionnement des instruments nommés

Pour chaque instrument mobilisé dans la question et dans $\mathcal{L}^*$, voici le protocole de calibration minimal :

| Instrument nommé | Taux de détection minimal (TPR) et Fausses alertes (FPR) [illustratif] | Cas honnêtes appariés (*Matched Honest Cases*) | Vérification mécanique simple à battre (*Mechanical Baseline*) |
| :--- | :--- | :--- | :--- |
| **1. Moniteur `jev-1.14.0` (6 sous-scores)** [statut : VÉRIFIÉ] | **TPR $\ge 0,90$** sur les violations d'intégrité (`Hyp=Rés`, réf. non marquées, absence de duel) ; **FPR $\le 0,05$**. | 50 propositions scientifiques valides contenant du jargon mathématique dense mais où chaque hypothèse, référence `(référence à vérifier)` et chiffre `illustratif` est correctement balisé, appariées en longueur et vocabulaire à 50 propositions « vernis » de l'Annexe 3. | **Regex + Compteur lexical** : script Python de 30 lignes vérifiant par expressions régulières la présence des chaînes `H_A`, `H_B`, `contrôle négatif`, `(référence à vérifier)`, `illustratif` et l'absence d'une liste noire de superlatifs. |
| **2. Détecteur de dérive et troncature $\mathrm{NCD}(c_0, c_k)$ + Garde-fou de fin de bloc** [statut : HYPOTHÈSE] | **TPR $= 1,00$** sur les troncatures amont (comme les 20 champions de l'Annexe 3) et **TPR $\ge 0,85$** sur l'oubli d'au moins 1 des 6 règles à la profondeur $k$ ; **FPR $\le 0,05$**. | Reformulations concises et légitimes de la consigne $c_0$ par un sous-agent qui adapte le plan à une sous-tâche précise sans violer les règles d'intégrité ni perdre ses phrases finales. | **Distance de Jaccard sur 3-grammes + Vérificateur de ponctuation finale** : rejeter tout texte dont le caractère précédant `FIN-DE-CHAMPION` n'est pas un point final `.` ou `)` fermant une phrase syntaxiquement complète, et vérifier le recouvrement des mots de $c_0$. |
| **3. Détecteur de corrélation d'erreurs `H4'` ($q_{ff}^{(t)}$)** [statut : HYPOTHÈSE] | **TPR $\ge 0,80$** sur les paires de sorties partageant une même hallucination de référence ou un même angle mort méthodologique ; **FPR $\le 0,10$**. | Deux agents de la même espèce (`gemini-4-argon`) arrivant indépendamment à la même conclusion exacte à partir des mêmes faits vérifiés du socle (convergence vers la vérité $\neq$ erreur corrélée `H4'`). | **Similarité Cosinus TF-IDF brute** entre les textes complets $y_i$ et $y_j$ (qui confond le consensus sur les faits vérifiés avec la corrélation des erreurs). $q_{ff}^{(t)}$ doit battre TF-IDF en ne mesurant la corrélation que sur les segments signalés en défaut par `jev` et hors socle de faits. |
| **4. Sélecteur de diversité DPP + MAP-Elites sur 10 Vagues** [statut : HYPOTHÈSE] | **TPR $\ge 0,85$** de couverture des 10 cônes mathématiques avec $< 10\text{ \%}$ de redondance sémantique inter-champions ; **FPR (taux d'extinction d'espèce) $= 0,00$** (contrairement à l'extinction d'Opus et des vagues 5, 6, 9, 10 de Fable en Annexe 1). | Deux propositions situées dans le même cône mathématique (ex. `Cone-01-Info-Kolmogorov`) mais proposant deux mécanismes d'action réellement orthogonaux (ex. Wyner `CDW` vs Arbre de Tunstall `KCS-PTS`). | **Échantillonnage stratifié uniforme à 1 Vague sans déflation** : tirer $10$ explorateurs par cône en une seule vague avec température $T=1,0$ et prendre le meilleur score net $r_i$ de chaque cône sans matrice DPP. Si les 10 vagues de déflation ne battent pas 1 vague stratifiée sur le score net $r_i$ du Top 10, la déflation séquentielle à 10 vagues est abandonnée. |

---

## (d) Plan d'Action Immédiat ($\mathcal{M}_3 \to \mathcal{M}_2 \to \mathcal{M}_1$) et Ancrage Matériel

### 1. Algorithme exact d'exécution de $\mathcal{M}_2$ et $\mathcal{M}_1$ sous la gouvernance de $\mathcal{L}^*$

Avant de dépenser le moindre dollar en $\mathcal{M}_2$ et $\mathcal{M}_1$, l'orchestrateur Python applique deux correctifs mécaniques immédiats issus du diagnostic de l'Annexe 1 et 3 :
- **Correctif 0a (Anti-Troncature)** : Suppression du découpage brutal `text[:MAX_CHARS] + "\nFIN-DE-CHAMPION"`. Si une génération ne se termine pas naturellement par la balise de fin après une phrase complète, elle est marquée `TRONQUÉE` (score $= 0$) et relancée avec une consigne de longueur stricte ($\le 450$ mots [illustratif]).
- **Correctif 0b (Réparation de `claude-opus-5-5` et de l'extinction `claude-fable-5-1`)** : Vérification de l'identifiant d'API/quota pour `claude-opus-5-5` (absent des logs) et remplacement de la pénalité de déflation globale par une grille **MAP-Elites locale par cône** afin d'empêcher l'écrasement des vagues tardives de Fable.

**Algorithme d'exécution en 4 étages ($\mathcal{L}^*$-Swarm Pipeline)** :

1. **Étage $\mathcal{M}_2^{(0)}$ — Crible Bibliographique Hors-Poids à $0\text{ USD}$ (APIs publiques + `zstd` + `jev-1.14.0`)** :
   - Interroger gratuitement Semantic Scholar, arXiv et Alignment Forum sur les 4 ancrages vérifiés du projet (`P3` sondes linéaires, incidents de délégation *Sol/Astra*, hausse des infractions sous rejets répétés $0,49 \to 0,65$ de Jhaveri et al., 2026 / Tagliabue et al., 2026, et *Value/Dopamine Neurons* $< 1\text{ \%}$ de Xu et al., `arXiv:2602.00986v2`) croisés avec les 5 bassins mathématiques survivants de $\mathcal{M}_3$.
   - Extraire $N_{\text{paires}} = 10\,000$ paires d'articles $(u,v)$ [illustratif] à distance de citation $d_{\text{cit}}(u,v) \ge 3$ [illustratif].
   - Filtrer à coût nul par l'équation (3) de $\mathcal{L}^*$ : calculer la compression croisée `zstd` des résumés $C(u)+C(v)-C(u\oplus v)$ et les scores `jev-1.14.0`. Ne retenir que le Top 50 des paires $(u,v)$ [illustratif] maximisant l'épiphanie descriptive sans chevauchement de citations.
2. **Étage $\mathcal{M}_2^{(1)}$ — Synthèse des Ponts Bibliographiques par Éclaireurs (`gemini-4-argon`, Budget : $8\text{ USD}$ [illustratif])** :
   - Déployer 50 éclaireurs `gemini-4-argon` sur le Top 50 des paires $(u,v)$ pour extraire le mécanisme exact de chaque article (vérification automatique de l'existence réelle du titre/auteurs/année dans la réponse JSON de l'API Semantic Scholar/Crossref pour garantir 0 % de référence hallucinée).
   - Filtrage SPRT de Wald (`jev-1.14.0`) : tuer immédiatement toute branche où $v_{\text{hyp=res}} > 0,30$ [illustratif] ou $\mathrm{NCD}(c_0, c_k) > \varepsilon_{H9}$. Sélectionner les 15 meilleurs ponts vérifiés [illustratif].
3. **Étage $\mathcal{M}_1^{(1)}$ — Conception des Expériences sur `Llama-3.1-8B/70B` et Routage Anti-`H4'` (Budget : $45\text{ USD}$ Claude + $7\text{ USD}$ Gemini [illustratif])** :
   - Sur chacun des 15 ponts, instancier en parallèle 3 architectes expérimentaux (1 `claude-fable-5-1`, 1 `claude-opus-5-5`, 1 `gemini-4-argon`) chargés de concevoir un duel $H_A \perp H_B$ testable sur `Llama-3.1-8B-Instruct` et `70B` (visant les hypothèses `H4'`, `H5`, `H7`, `H9` et les neurones de valeur de Xu et al.).
   - Calculer $q_{ff}^{(t)}$ (Équation 2 de $\mathcal{L}^*$) : croiser systématiquement chaque proposition avec un **Parasite Red-Team d'une espèce différente** (Chimère forcée : Fable/Opus attaque Argon, Argon attaque Fable/Opus) pour chercher le vernis Goodhart, les confusions corrélation/causalité et les contrôles négatifs faibles.
4. **Étage $\mathcal{M}_1^{(2)}$ — Riposte, Mise à jour de Brier et Cristallisation des Protocoles Finaux (Budget : $35\text{ USD}$ Claude + $3\text{ USD}$ Gemini [illustratif])** :
   - Mettre à jour les budgets par le réplicateur de Brier (Équation 4 de $\mathcal{L}^*$). Les propositions survivant au Red-Team et au vérificateur syntaxique de complétude sont compilées en scripts d'expérimentation prêts à tourner sur nos GPU.

### 2. Ancrage matériel, calcul nécessaire et répartition budgétaire

Conformément aux ressources vérifiées du socle :
- **Budget API Moteur à Essaims ($\mathcal{M}_2 + \mathcal{M}_1$ + Duels de validation de $\mathcal{L}^*$)** :
  - **API Anthropic (`claude-fable-5-1` et `claude-opus-5-5`)** : Plafond vérifié de **100 USD** [statut : VÉRIFIÉ]. Allocation : $15\text{ USD}$ [illustratif] pour les 3 duels de validation de $\mathcal{L}^*$, $45\text{ USD}$ [illustratif] pour la conception et le Red-Team croisé $\mathcal{M}_1^{(1)}$, $35\text{ USD}$ [illustratif] pour la riposte et cristallisation $\mathcal{M}_1^{(2)}$, et $5\text{ USD}$ [illustratif] de réserve de sécurité.
  - **API Gemini (`gemini-4-argon`)** : Plafond vérifié de **20 USD** [statut : VÉRIFIÉ]. Allocation : $2\text{ USD}$ [illustratif] pour les duels de validation de $\mathcal{L}^*$, $8\text{ USD}$ [illustratif] pour le criblage $\mathcal{M}_2^{(1)}$, $7\text{ USD}$ [illustratif] pour l'exploration et le Red-Team $\mathcal{M}_1^{(1)}$, et $3\text{ USD}$ [illustratif] pour $\mathcal{M}_1^{(2)}$.
  - **Classifieur/Moniteur `jev-1.14.0` et APIs bibliographiques (arXiv, Semantic Scholar, Crossref)** : **0 USD** (budget illimité et gratuit [statut : VÉRIFIÉ]), exécutant environ $25\,000$ évaluations non génératives [illustratif] en moins de 15 minutes CPU [illustratif].
- **Exécution locale des expériences $\mathcal{M}_1$ générées (Modèles ouverts et GPU)** :
  - **Modèles cibles** : `Llama-3.1-8B-Instruct` et `Llama-3.1-70B` (boîte noire + boîte blanche, accès complet aux poids, activations résiduelles et neurones parcimonieux $< 1\text{ \%}$) [statut : VÉRIFIÉ].
  - **Matériel de calcul** : Nœuds GPU **A100 80 Go** et **H200 NVL** disponibles dans le cadre du projet [statut : VÉRIFIÉ].
  - **Volume de calcul estimé pour exécuter les protocoles $\mathcal{M}_1$ issus de $\mathcal{L}^*$** : $12\text{ heures-GPU}$ sur 1× A100 80 Go [illustratif] pour les criblages mécanistes et ablations de neurones sur `Llama-3.1-8B-Instruct` (ex. chaînes de $k=6$ délégations sous rejets répétés), suivies de $24\text{ heures-GPU}$ sur 2× H200 NVL [illustratif] pour la réplication boîte blanche/noire à pleine échelle sur `Llama-3.1-70B`.

FIN-DE-CELLULE