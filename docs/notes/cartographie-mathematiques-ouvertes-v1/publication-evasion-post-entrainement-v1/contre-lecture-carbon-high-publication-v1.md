# Contre-lecture critique indépendante (Carbon, effort élevé) — Dossier de publication « Évasion post-entraînement » (v1)

- **Verdict global** : **`CORRECTIONS REQUISES`**
  - **LessWrong (commentaire + billet) & GitHub** : **publiables dès correction de B1, B2** (et retrait/ajustement de la mention Lean 4 de M1 + remplacement des placeholders `[LINK_*]`). Le fond mathématique du Théorème 1, les calculs numériques et le ton scientifique sont excellents.
  - **arXiv (`cs.LG` / `cs.AI`)** : **non prêt en l'état** (requiert B1, B2, M1, M2, et idéalement une expérience jouet de descente de gradient de politique — voir Section 5).
- **Périmètre audité (lecture seule, `main`)** :
  1. `commentaire-reponse-yair-halberstadt-lesswrong-en-v1.md` (`6459e9073f7a269d…`)
  2. `billet-lesswrong-evasion-post-entrainement-en-v1.md` (`b18515e5d0cb3e60…`)
  3. `manuscrit-arxiv/main.tex` (`891341224cbbddff…`)
  4. `github-page/README.md` (`41b87f2eb2ae99c3…`)
  5. `verifier_exemples_papier_v1.py` (`9f4cb94c55ce1b3f…`) et `exemples-verifies-papier-v1.json` (`52da1f7f89981a64…`)
  6. `avis-opportunite-arxiv-pour-lazar-fr-v1.md` (`87ceee0b7d9a8154…`)
  7. Pièces sources : `elucidation-loi-halberstadt-post-entrainement-v1.md` (`bf9d442d1c50010a…`) et `test_mort_halberstadt_v1.py` (`381e3c12b2ba9d0f…`).

---

## Liste fermée des corrections requises

### BLOQUANT (à corriger avant toute publication publique)

1. **[B1] Survente logique sur « les trois seuls régimes d'échappement » / « *iff* » / « *Necessary and Sufficient* » (Théorème 2)**
   - **Localisation** : `commentaire-reponse-yair-halberstadt-lesswrong-en-v1.md` (l. 13), `billet-lesswrong-evasion-post-entrainement-en-v1.md` (l. 19, 83), `manuscrit-arxiv/main.tex` (l. 45, 58, 200, 208, 210), `github-page/README.md` (l. 14).
   - **Défaut précis** :
     1. Le Théorème 2 est annoncé comme une équivalence (« *iff at least one of three conditions holds* », « *Necessary and Sufficient Escape Regimes* », « *only three escape regimes* »), mais il ne définit ni ne prouve un *si et seulement si* unifié pour « *deployment-effective evasion* ». En réalité : **R1** est un *iff* pour $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$ dans le modèle à 3 strates ; **R2** donne une identité exacte sous Opérateur A mais seulement une condition *suffisante* (indépendance ou association négative) sous Opérateur B ; **R3** introduit un modèle contextuel étendu ($\tau_\pi : \mathcal{X} \to [0, 1]$ sur le mélange $P_{\mathrm{mix}}$) et ne prouve qu'une condition *suffisante* ($C > C_{\mathrm{R3}}^*$).
     2. Dans le modèle statique à 3 régimes, la négation de **(H3)** — maintenir $\beta_{\mathrm{loop}}$ sous le ratio critique $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ — est **déjà algébriquement contenue dans (R1)** sous l'Opérateur B ($\beta_{\mathrm{f}} \Delta R_{\mathrm{net}} < (\beta_{\mathrm{h}} - \beta_{\mathrm{f}}) C$). Ainsi, **(R3) n'est pas une troisième branche logiquement disjointe de (R1)** dans le modèle de Gibbs, mais un *mécanisme constructif* permettant d'entrer dans le régime de dérive négative de (R1) sous Opérateur B même lorsque le moniteur est totalement aveugle sur les épisodes ordinaires.
     3. Dans **(H3)** (`main.tex` l. 206), le ratio critique est écrit $C/(\Delta R + C)$, ce qui suppose implicitement $\beta_{\mathrm{h}} = 1$ et $\delta_{\mathrm{maint}} = 0$ (la formule générale issue de (R1) est $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$).
   - **Action requise** : Reformuler sans survente dans les 4 pièces publiques : dans le modèle de Gibbs, éviter une évasion efficace au déploiement exige de rompre **l'une des deux inégalités algébriques exactes** — soit maintenir la dominance de l'honnêteté (**R1**, CNS exacte), soit découpler la sélection d'entraînement de l'audit de déploiement (**R2**, identité de covariance exacte) —, et **R3** (pièges plantés indiscernables) fournit un **troisième levier constructif** (condition suffisante) pour forcer la dérive négative de R1 sous pénalité sans détection sur les épisodes ordinaires. Corriger le ratio de (H3) en $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$.

2. **[B2] Références publiques au script interne non publiable `test_mort_halberstadt_v1.py` (risque de fuite / lien mort)**
   - **Localisation** : `manuscrit-arxiv/main.tex` (l. 38, l. 260), `github-page/README.md` (l. 32), `verifier_exemples_papier_v1.py` (l. 6).
   - **Défaut précis** : `test_mort_halberstadt_v1.py` est un fichier interne contenant des identifiants/noms de code privés (`GO-2026-11-24-01`, `Q4`), un chemin privé de VM (`/home/antigravity/.gemini/jetski/brain/...`), ainsi qu'une formule `c_seuil` incomplète à la ligne 302 (corrigée dans `verifier_exemples_papier_v1.py` l. 208). Citer `test_mort_halberstadt_v1.py` dans les documents publics (et inviter le lecteur de `README.md` à l'exécuter) crée soit une commande cassée/référence morte si le fichier est exclu, soit une fuite interne s'il est copié par mégarde.
   - **Action requise** : Supprimer les 4 mentions de `test_mort_halberstadt_v1.py` dans `main.tex`, `github-page/README.md` et `verifier_exemples_papier_v1.py`. Le script `verifier_exemples_papier_v1.py` est déjà totalement autonome.

---

### MAJEUR (à corriger avant arXiv ; recommandé avant LessWrong/GitHub)

3. **[M1] Extrait Lean 4 syntaxiquement invalide dans `main.tex` (Section 5.3) et revendication non compilée**
   - **Localisation** : `manuscrit-arxiv/main.tex` (l. 45, 59, 332–350), `billet-lesswrong-evasion-post-entrainement-en-v1.md` (l. 108), `github-page/README.md` (l. 38).
   - **Défaut précis** : L'extrait Lean 4 de `main.tex` a été converti en ASCII pour `pdflatex` et **ne peut pas compiler** tel quel sous Lean 4 / Mathlib4 :
     - `Q` au lieu de `ℚ` (ou `Rat`),
     - `<->` au lieu de `↔` (ou `Iff`),
     - `div_lt_div_iff0` au lieu de `div_lt_div_iff₀`.
     - De plus, `positivity` ne chaîne généralement pas `0 ≤ bv`, `bv < bf`, `bf ≤ bh` pour déduire `0 < bf` et `0 < bh` sans lemmes intermédiaires, et `nlinarith [mul_pos hpf hE]` sur une inégalité polynomiale de degré 3 risque d'échouer sans factorisation explicite.
     - Annoncer « *ready-to-compile* » tout en précisant que `lean` n'est pas installé sur la machine affaiblit la crédibilité formelle.
   - **Action requise** : Soit compiler effectivement le fichier `.lean` sous Lean 4 / Mathlib4 (`lake build`, zéro `sorry`) et joindre le fichier vérifié, soit **retirer** la Section 5.3 et les mentions de Lean 4 (abstract, intro, billet l. 108, README l. 38) jusqu'à compilation effective.

4. **[M2] Compilation LaTeX non vérifiée et métadonnées d'auteur incomplètes pour arXiv**
   - **Localisation** : `manuscrit-arxiv/main.tex` (l. 38, Table 1 l. 275–287).
   - **Défaut précis** : `pdflatex` / `latexmk` étant absents de la VM, `main.tex` n'a pas encore été compilé. La Table 1 (8 colonnes) présente un risque élevé d'`Overfull \hbox`, et `\author{Lazar\thanks{...}}` ne satisfait pas les exigences de nom complet d'arXiv.
   - **Action requise** : Compiler `main.tex` avant tout dépôt arXiv, vérifier l'absence de débordements de marge, et renseigner le nom complet de l'auteur.

---

### MINEUR (polissage mathématique et éditorial)

5. **[m1] Facteur $1/\beta_{\mathrm{f}}$ dans la Proposition 1(1)** (`main.tex` l. 191) : l'énoncé indique « *slows stealth dominance by a factor $1/\beta_{\mathrm{f}}$ compared to pure rejection* ». C'est le **taux exponentiel asymptotique** ($\eta\beta_{\mathrm{f}}\Delta R$ vs $\eta\Delta R$) qui est ralenti d'un facteur $\beta_{\mathrm{f}}$ (facteur $1/\beta_{\mathrm{f}}$ sur l'échelle asymptotique de $\eta$) ; le rapport exact des seuils $\Delta R_{\mathrm{dom, B}}^*(\eta, 0)/\Delta R_{\mathrm{dom, A}}^*(\eta) = \frac{1}{\beta_{\mathrm{f}}}\frac{\log(p_{\mathrm{h}}/p_{\mathrm{f}})}{\log(p_{\mathrm{h}}/p_{\mathrm{f}})+\log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})}$ diffère de $1/\beta_{\mathrm{f}}$ dès que $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$ (et devient négatif si $p_{\mathrm{h}} < p_{\mathrm{f}}$). Reformuler sur le taux exponentiel asymptotique.
6. **[m2] Domaine de $\eta$ dans la définition de $\pi_{\mathrm{no}}^{(\eta)}$** (`main.tex` l. 81) : écrire $\eta > 0$ pour le maximiseur de $\mathbb{E}_\pi[R] - \eta^{-1} D_{\mathrm{KL}}(\pi \,\|\, \pi_0)$ (comme fait correctement pour l'Opérateur B à la l. 94), et $\pi_{\mathrm{no}}^{(0)} = \pi_0$ par continuité.
7. **[m3] Hypothèse superflue dans la preuve du Théorème 1(1)** (`main.tex` l. 153) : la dérivée de Radon-Nikodym $d\pi_{\mathrm{A}}^{(\eta)}(\cdot \mid \Pi_{\mathrm{tr}}) / d\mu_{\mathrm{tr}}^{(\eta)} = \beta / \mathbb{E}_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]$ reste exacte même si $R(\pi)$ varie sur $\Pi_{\mathrm{tr}}$ (car $e^{\eta R(\pi)}$ est déjà absorbé dans $\mu_{\mathrm{tr}}^{(\eta)}$). Supprimer l'invocation inutile de la constance de $R$ sur $\Pi_{\mathrm{tr}}$.
8. **[m4] Légendes des lignes de bascule arrondies (Tableaux 1 et 3)** (`main.tex` l. 283, 323 ; `billet` l. 69) : signaler en légende que les lignes en gras (`1.5768` et `0.2792`) sont évaluées aux valeurs arrondies à 4 décimales, expliquant l'écart de $2{,}3 \times 10^{-5}$ entre $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 0{,}340917$ et $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}}) = 0{,}340894$ (et $2{,}558400$ vs $2{,}558428$).
9. **[m5] Limitation explicite de R3 pour les attaques très rares ($\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$)** : R3 suppose $\tau_{\min} > \delta_{\mathrm{ind}}$ (exact), mais ne bloque pas une politique trichant à taux $\le \delta_{\mathrm{ind}}$ uniquement sur les contextes où $P_{\mathrm{ord}} > P_{\mathrm{trap}}$. Une phrase explicite dans la Remarque 1 ou la Section 6 renforcerait l'honnêteté du manuscrit.
10. **[m6] Placeholders et complétude bibliographique** : remplacer `[LINK_LESSWRONG_POST]`, `[LINK_GITHUB_PAGE]`, `[LINK_PDF]` avant mise en ligne ; optionnel pour arXiv : compléter les sous-titres de `griffin2024` et `terekhov2025`, et citer Joag-Dev & Proschan (1983) pour l'association négative en R2.

---

## Détail des 5 contrôles exécutés

### 1. Rigueur mathématique ligne par ligne (Théorèmes 1, 2 et Proposition 1)
- **Théorème 1 (1, 2, 3, 4a, 4b, 4c)** : **100 % exact** après vérification algébrique complète de chaque signe, exposant et cas limite :
  - $\beta_{\mathrm{f}} = \beta_{\mathrm{h}}$ : sous A, amplification absolue inconditionnelle ($\forall \Delta R \ge 0, \eta \ge 0$) ; sous B, si $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$, amplification absolue inconditionnelle et inversion exacte $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) \iff \eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1-\beta_{\mathrm{v}}}$ (et si $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} < 1$, l'équation (6) reste exacte).
  - $\beta_{\mathrm{v}} = 0$ : sous A, $\pi_{\mathrm{A}}(\Pi_{\mathrm{v}}) = 0$ et $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}}) = 1$ ; sous B avec $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$, $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ pour tous $\eta, C$ finis (Proposition 1(2) exacte).
  - $p_{\mathrm{v}} = 0$ : exclu par l'hypothèse globale $p_{\mathrm{v}} > 0$ (si $p_{\mathrm{v}} = 0$, l'amplification absolue disparaît car il n'y a plus de tricheurs visibles à élaguer).
  - $C = 0$ : sous B, $\bar{R}_0(\Pi_{\mathrm{f}}) = \beta_{\mathrm{f}}\Delta R > \beta_{\mathrm{v}}\Delta R \ge 0$, donc $\pi_{\mathrm{B}}^{(\eta, 0)}(\Pi_{\mathrm{f}}) \to 1$ quand $\eta \to \infty$ (Proposition 1(1) vraie, sous réserve du polissage **m1**).
- **Théorème 2 (R1, R2, R3)** :
  - Chaque inégalité et preuve prise isolément (**eq. (9) R1**, **eq. (10) R2**, **eq. (11) R3** y compris la stricte décroissance en $\tau_{\mathrm{ord}}$ et la borne supérieure simplifiée de $C_{\mathrm{R3}}^*$) est **mathématiquement exacte**.
  - Cas limite $\delta_{\mathrm{ind}} \ge \tau_{\mathrm{ord}}$ : correctement exclu par l'hypothèse $\tau_{\min} > \delta_{\mathrm{ind}}$ (voir **m5**).
  - Le seul défaut sérieux est la **survente logique d'exhaustivité / CNS globale** reliant R1–R2–R3 (**B1**).

### 2. Recalcul indépendant des exemples numériques et tableaux
- Exécution isolée en copie (`PYTHONDONTWRITEBYTECODE=1 python3 -W error verifier_exemples_papier_v1.py`, sans aucune écriture dans le dépôt) : **0 violation sur 14 000 instances**, identité rationnelle exacte $\Delta = 37/150$ vérifiée, et sortie JSON **strictement identique octet pour octet** (`diff` vide) à `exemples-verifies-papier-v1.json`.
- Recalcul indépendant par un script tiers de tous les seuils ($\Delta R_{\mathrm{A}}^* = 0{,}257992$, $\Delta R_{\mathrm{dom, A}}^* = 1{,}576778$, plancher asymptotique $0{,}833333$, $\Delta R_{\mathrm{dom, B}}^* = 2{,}807845$, seuil niche $2{,}558428$ / $C = 0{,}279214$, R1 $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) = 0{,}999998$, R3 $C_{\mathrm{R3}}^* = 5{,}462585$) et de chaque cellule des **3 tableaux** de `main.tex`, du billet (y compris $\pi_{\mathrm{B}}(\Pi_{\mathrm{v}}) = 0{,}0082\% \approx 0{,}01\%$ à $\Delta R = 3{,}0$) et du commentaire : **100 % concordant à la dernière décimale**.

### 3. Antériorité, références et ton scientifique
- **14 citations de `main.tex`** : toutes vérifiées, réelles, correctement datées et attribuées sans appropriation abusive (`baker2025`, `bartok2014`, `gao2022`, `greenblatt2023`, `greenblatt2024`, `griffin2024`, `halberstadt2026`, `hardt2016`, `hubinger2024`, `skalse2022`, `terekhov2025`, `testingthewaters2026`, `ukaisi2025`, `zhuang2021`).
- **Ton sur LessWrong** : exemplaire — courtois, direct, non arrogant, rendant justice autant à l'intuition de Yair Halberstadt qu'aux objections de `testingthewaters`, et immédiatement utile grâce à la séparation des 4 grandeurs.

### 4. Hygiène anti-fuite
- Balayage lexical complet des 4 pièces publiques + `verifier_exemples_papier_v1.py` + `exemples-verifies-papier-v1.json` : **aucune fuite** de nom de code (`GO-2026`, `Sondes`, `Q4`, `G1`), de chemin privé (`/home/antigravity/...`) ou de résultat de course privée dans le texte lui-même.
- **Point critique détecté (B2)** : les 4 mentions résiduelles de `test_mort_halberstadt_v1.py` (qui, lui, contient `GO-2026-11-24-01`, `Q4` et le chemin VM privé) doivent être purgées des fichiers publics.

### 5. Avis indépendant sur l'opportunité d'une soumission arXiv
Je rejoins largement la prudence de `avis-opportunite-arxiv-pour-lazar-fr-v1.md`, en étant **légèrement plus strict** :
1. **LessWrong + GitHub d'abord (dès correction de B1, B2 et M1)** : **OUI**. Le dilemme Rejet–Pénalité (inversion en niche parfaitement furtive) et la clarification des 4 grandeurs apportent une vraie valeur ajoutée immédiate au débat de novembre 2026, et les retours de la communauté (Halberstadt, `testingthewaters`, chercheurs en contrôle) enrichiront la version finale.
2. **Ne pas soumettre `main.tex` sur arXiv en l'état** :
   - Outre les corrections obligatoires (**B1, B2, M1, M2**), la note repose uniquement sur de l'algèbre de Gibbs à 3 états et une inégalité de variation totale. Pour `cs.LG` / `cs.AI`, le manuscrit gagnerait considérablement à intégrer **une courte expérience synthétique reproductible de descente de gradient de politique** (REINFORCE / PPO / GRPO sur un bandit ou MDP jouet en NumPy/PyTorch, ~100 lignes, zéro donnée privée) montrant que la dynamique finie $\theta_t$ traverse bien les seuils du Théorème 1, l'inversion de niche parfaite et l'effet des pièges R3.
   - Quant à **Lean 4**, c'est un *bonus* appréciable uniquement s'il est **réellement compilé (`lake build`, 0 `sorry`)** sur un lemme non trivial (par exemple l'identité de variance finie + l'équivalence du Théorème 1.2) ; un extrait non compilé et syntaxiquement cassé fait au contraire plus de mal que de bien. Si la priorité est la rapidité, mieux vaut retirer la section Lean 4 et ajouter l'expérience jouet SGD avant le dépôt arXiv.
