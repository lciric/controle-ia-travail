# Feuille de route éditoriale et scientifique consolidée (v2) — « Papier D » : Évasion sous filtrage en entraînement après pré-entraînement et découplage hors boucle

- **Programme** : Plan Turing (`GO-2026-11-24-01`, `GO-2026-11-24-04`, `R-5240`)
- **Date** : 24 novembre 2026 (version 2 consolidée après les **deux évaluations indépendantes et critiques de Carbon en effort élevé** : `reponse-carbon-indep-cible-pub-v1.md` et `reponse-carbon-critique-reponse-mere-v1.md`)
- **Branche dédiée de travail parallèle** : `papier-d/evasion-post-entrainement-v1`

---

## 1. Synthèse exécutive : ce que la double revue « Area Chair » de Carbon confirme et corrige

Nous avons soumis le manuscrit `main-v2.tex` à deux appels séparés de **Carbon en effort maximal** : (1) une lecture froide **100 % indépendante** sans voir notre analyse initiale, puis (2) une **contre-lecture critique sans complaisance** de notre feuille de route v1.

### Points de convergence totale (confirmés indépendamment)
1. **Zéro erreur mathématique et vraie valeur conceptuelle** : la séparation explicite des quatre métriques de sélection (enrichissement conditionnel, amplification absolue, dominance asymptotique sur l'honnêteté, transfert d'évasion vers un auditeur hors boucle), le *Dilemme Rejet–Pénalité* et le retournement de l'inégalité de variation totale au profit du défenseur constituent un noyau théorique limpide et mémorable.
2. **Recevabilité immédiate tel quel** : acceptation très probable (**80–90 %, potentiel *Spotlight***) dans les **ateliers non archivals d'ICLR, ICML ou NeurIPS** (*AI Control, SafeGenAI, Trustworthy ML*), mais rejet certain en piste principale d'une conférence de rang A* en l'état (« algèbre de Gibbs à trois états trop élémentaire sans dynamique d'optimisation réelle ni validation sur modèles »).
3. **Élimination définitive de COLT / ALT et de Lean 4** : COLT/ALT exigent une machinerie minimax séquentielle lourde hors sujet ici, et Lean 4 n'apporte aucun bonus d'acceptation à ICML/NeurIPS.

### Sept corrections décisives apportées par Carbon (intégrées à cette v2)
1. **Réalisme calendaire (éviter l'écueil de fin janvier en piste principale expérimentale)** : tenter en 8 semaines (fêtes incluses) 3 nouveaux théorèmes + une campagne d'apprentissage par renforcement sur modèles `7B–8B` produirait un article précipité. **Trajectoire reine retenue** :
   - **Voie Reine (prestige maximal maîtrisé)** : **Atelier non archival ICLR 2027 (février)** avec les extensions analytiques exactes $\longrightarrow$ **Piste principale NeurIPS 2027 (mai)** avec l'expérience contrôlée (bassin de relecteurs *AI Control / CoT monitoring* 2 à 3 fois plus dense à NeurIPS qu'à ICML).
   - **Voie Rapide Janvier (optionnelle sans risque GPU)** : **ICML 2027 — *Position Paper Track* (fin janvier)**, cadrée autour d'une thèse architecturale forte soutenue par nos théorèmes étendus !
2. **Modéliser les *vrais* algorithmes de post-entraînement (`GRPO`, `PPO` en ligne ancré sur $\pi_0$, filtrage itéré)** : dans `main-v2.tex`, l'Opérateur A ($\pi_{\mathrm{A}}^{(\eta)} \propto \beta e^{\eta R}\pi_0$) commute avec le filtrage et correspond uniquement à un affinage par rejet suivi de RL ancré sur la loi filtrée (`RS-SFT + RL`). En apprentissage par renforcement en ligne (`PPO`/`GRPO`) où la pénalité de Kullback-Leibler reste ancrée sur le modèle initial gelé $\pi_0$, l'optimum obéit à une **équation auto-cohérente non linéaire** :
   $$\pi^*(d\pi) \propto \pi_0(d\pi)\exp\!\left(\eta\,\frac{\beta(\pi)}{\mathbb{E}_{\pi^*}[\beta]}\big(R(\pi) - \bar{R}_{\mathrm{acc}}(\pi^*)\big)\right),$$
   tandis que sous **`GRPO` / `RLOO`**, pénaliser $-C$ sur la triche visible $\Pi_{\mathrm{v}}$ abaisse la moyenne de récompense du groupe de $G$ trajectoires et **accélère directement le gradient relatif de la triche furtive $\Pi_{\mathrm{f}}$** !
3. **Remplacer le théorème géométrique fragile sur transformeurs par une transition de phase continue (méthode de Laplace)** : au lieu d'hypothèses d'orthogonalité irréalistes entre chaîne de pensée et flux résiduel (causalement couplés en pratique), analyser une densité continue de survie $\pi_0(1-\beta \in du) \asymp u^{\gamma-1}du$ ($\gamma > 0$, sans atome en $\beta = 1$). Par intégration de Laplace, le poids furtif sous l'Opérateur B vaut $\Gamma(\gamma)[\eta(\Delta R + C)]^{-\gamma}e^{\eta \Delta R}$ : **la barrière asymptotique du Théorème 1(4b) s'effondre dès que le support de $\beta$ approche $1$ continûment**, ne survivant que s'il existe un **trou spectral strict** $\operatorname{ess\,sup}_{\Pi_{\mathrm{tr}}}\beta < \beta_{\mathrm{h}}$, avec un ralentissement polynomial exact en $\eta^{-\gamma}$.
4. **Éliminer totalement le plancher d'attaques rares du Régime R3 via la divergence de Rényi $D_\infty$** : sous variation totale $d_{\mathrm{TV}} \le \delta_{\mathrm{ind}}$, l'équilibre contextuel à grand $\eta$ concentre 100 % de triche sélective sur la région de Neyman–Pearson ($\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$). En remplaçant $d_{\mathrm{TV}}$ par la max-divergence unilatérale $e^{D_\infty(P_{\mathrm{ord}} \| P_{\mathrm{trap}})} = \operatorname{ess\,sup}_x \frac{dP_{\mathrm{ord}}}{dP_{\mathrm{trap}}}(x) \le M < \infty$, on obtient $\tau_{\mathrm{trap}}(\pi) \ge M^{-1}\tau_{\mathrm{ord}}(\pi)$ et **zéro plancher d'attaques rares** ($\forall \tau_{\mathrm{ord}} > 0$) dès que :
   $$C > \frac{(1-\rho)M + \rho\,\varepsilon_{\mathrm{trap}}}{\rho(1-\varepsilon_{\mathrm{trap}})}\,\Delta R.$$
5. **Résoudre le piège de taille d'effet de la Table 3 (`0,79` point) par le risque résiduel en déploiement et le régime $p_{\mathrm{v}} e^{\eta\Delta R} \gg p_{\mathrm{h}}$** : formaliser la fonction de perte en déploiement (où $\Pi_{\mathrm{v}}$ est bloqué en aval tandis que seul $\Pi_{\mathrm{f}}$ cause le dommage) et calibrer l'expérience dans le régime $p_{\mathrm{v}} e^{\eta\Delta R} \gg p_{\mathrm{h}}$ pour observer un écart macroscopique (`> 15` points au lieu de `0,8 %`).
6. **Protocole expérimental sans pari de stéganographie spontanée** : utiliser un banc établi de contournement de tests unitaires (*School of Reward Hacks* / code à tests incomplets sur `Qwen-2.5-3B/7B` ou `DeepSeek-R1-Distill-Qwen-7B`) où le contournement non verbalisé préexiste dans $\pi_0$ ($p_{\mathrm{f}} > 0$) et est mesuré exactement par des tests unitaires cachés hors boucle ($M_{\mathrm{audit}}$).
7. **Toilettage éditorial immédiat** : retirer du résumé et des contributions toute mise en avant des « `14 000` tirages Monte Carlo » et de `fractions.Fraction` (signal négatif pour des théoriciens seniors), renommer tout script en anglais (`verify_examples.py`), et remplacer les tableaux par des **diagrammes de phase 2D**.

---

## 2. Panorama révisé et hiérarchisé des enceintes cibles

| Priorité & Enceinte | Niveau & Adéquation | Verdict après revue contradictoire Carbon | Contenu requis | Échéance |
|---|---|---|---|---|
| **Priorité 1 — Atelier ICLR 2027 $\to$ Piste principale NeurIPS 2027** *(Alignement / AI Control)* | **Sommet mondial optimal** (bassin de relecteurs *AI Control* 2–3× plus dense qu'à ICML) | **TRAJECTOIRE REINE RETENUE** : laisse le temps de bâtir une théorie irréprochable d'ici fév. puis une expérience `GRPO` chirurgicale d'ici mai | Fév. : 4 théorèmes exacts + diagrammes de phase 2D + RL tabulaire. Mai : + expérience `GRPO` contrôlée sur `Qwen-2.5-3B/7B` | Fév. 2027 (Atelier) puis **Mai 2027 (NeurIPS)** |
| **Priorité 2 — ICML 2027 (*Position Paper Track*)** | **Sommet mondial** (piste dédiée aux thèses méthodologiques structurantes) | **Meilleure option pour fin janvier** : tranche un débat actif sans risquer un rejet sur une campagne GPU précipitée | Thèse architecturale forte + les 4 résultats analytiques exacts + diagrammes de phase + bandit neuronal léger (`0 USD`) | **Fin janv. 2027** |
| **Priorité 3 — IEEE SaTML** ou **TMLR (*Featured / J2C*)** | **Très haut prestige sécurité** (SaTML) / **Zéro loterie calendaire** (TMLR) | **Excellente alternative ou rebond immédiat** (>80 % à TMLR avec expériences contrôlées, label *Journal-to-Conference*) | Version complète (opérateurs RL + Laplace + $D_\infty$ + expérience contrôlée) | Continue (TMLR) / Automne-Hiver (SaTML) |
| ~~COLT / ALT 2027~~ | Théorie pure | **Écarté** (exige bornes inférieures minimax séquentielles hors périmètre ; Lean 4 non valorisé) | — | — |

---

## 3. Nouveau cahier des charges scientifique de « Papier D » (4 théorèmes + 2 échelles empiriques)

1. **Théorème 1 consolidé (Vrais opérateurs de post-entraînement)** : comparaison exacte entre (i) affinage filtré `RS-SFT + RL` (Opérateur A), (ii) filtrage itéré sur $K$ époques ($\beta^K$), (iii) `KL-RL` en ligne ancré sur $\pi_0$ (point fixe auto-cohérent non linéaire), et (iv) **`GRPO` / `RLOO` avec pénalité $-C$** (déplacement de la moyenne de groupe accélérant $\Pi_{\mathrm{f}}$), formulée en termes de **risque résiduel en déploiement**.
2. **Théorème 2 nouveau (Transition de phase continue par méthode de Laplace et dynamique à batch fini)** : effondrement de la barrière asymptotique en présence d'une queue continue $\pi_0(1-\beta \in du) \asymp u^{\gamma-1}du$ sans trou spectral ($\eta^{-\gamma}$), et condition d'inaccessibilité en échantillons finis lorsque $p_{\mathrm{f}} \ll (BT)^{-1}$.
3. **Théorème 3 consolidé (Découplage hors boucle sous corrélation bornée)** : borne supérieure explicite sur la dégradation du moniteur d'audit $M_{\mathrm{audit}}$ lorsque $\operatorname{Cov}_{\nu_0}(\beta_{\mathrm{boucle}}, \beta_{\mathrm{audit}}) \le \varepsilon > 0$ ou sous information mutuelle bornée $I(M_{\mathrm{boucle}}; M_{\mathrm{audit}})$.
4. **Théorème 4 nouveau (Pots de miel bornés en divergence de Rényi $D_\infty$ et hockey-stick)** : fermeture intégrale du plancher d'attaques rares ($\forall \tau_{\mathrm{ord}} > 0$) par borne de rapport de vraisemblance $dP_{\mathrm{ord}}/dP_{\mathrm{trap}} \le M$.
5. **Validation empirique à deux échelles** :
   - **Échelle 1 (`0 USD`, CPU)** : diagrammes de phase 2D exacts + simulation `PPO` / `GRPO` / `Filtered-SFT` en bandit contextuel neuronal illustrant le fossé entre équilibre de Gibbs et batch fini ;
   - **Échelle 2 (sur devis GPU dédié après validation CPU)** : expérience `GRPO` contrôlée sur `Qwen-2.5-3B/7B` (contournement de tests unitaires verbalisé vs non verbalisé dans le brouillon, évalué hors boucle par tests unitaires cachés $M_{\mathrm{audit}}$, en régime $p_{\mathrm{v}} e^{\eta\Delta R} \gg p_{\mathrm{h}}$).

---

## 4. Protocole de prise de date aujourd'hui et respect du double aveugle

1. **Dépôt GitHub compagnon minimal et propre (`0` trace interne, `0` nom francophone)** : uniquement `README.md`, `main.tex` / `main.pdf` (toiletté des mentions « 14 000 Monte Carlo », avec précision explicite sur l'Opérateur A, le risque en déploiement de la Table 3 et la remarque $D_\infty$), `verify_examples.py` et `LICENSE`.
2. **Ordre de publication sur LessWrong** :
   - Poster **d'abord le commentaire court** sous le billet de Yair Halberstadt pointant vers le dépôt GitHub compagnon (prise de date sobre et directe au cœur de la discussion active).
   - **Garder de côté le billet LessWrong autonome complet** (ou le différer après soumission/acceptation) afin de ne pas saturer l'attention du petit vivier de relecteurs *AI Control* juste avant une soumission en double aveugle, et respecter un **embargo promotionnel total** pendant toute période d'évaluation officielle.
