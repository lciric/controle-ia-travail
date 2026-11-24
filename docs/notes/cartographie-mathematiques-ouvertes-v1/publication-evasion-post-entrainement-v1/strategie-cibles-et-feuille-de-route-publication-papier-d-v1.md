# Feuille de route éditoriale et scientifique — « Papier D » : Évasion sous filtrage en entraînement après pré-entraînement et découplage hors boucle

- **Programme** : Plan Turing (`GO-2026-11-24-01`, `GO-2026-11-24-04`, `R-5240`)
- **Date** : 24 novembre 2026
- **Branche dédiée de travail parallèle** : `papier-d/evasion-post-entrainement-v1`

---

## 1. En bref : diagnostic froid et cible retenue

1. **État actuel de notre résultat (manuscrit `main-v2.tex` vérifié sur 10/10 points par Carbon effort élevé)** :
   - Nous disposons déjà d'un **Théorème 1 exact** (enrichissement conditionnel universel de la triche furtive + seuils exacts de bascule + paradoxe montrant qu'une pénalité négative amplifie *davantage* une niche parfaitement furtive que le simple rejet) et d'une **caractérisation rigoureuse de trois mécanismes d'atténuation** (barrière d'accessibilité en divergence de Kullback-Leibler et maintien multi-objectifs, découplage informationnel hors boucle par covariance non positive, et audit aléatoire après coup / pièges indiscernables en variation totale), vérifiés en arithmétique rationnelle exacte et sur `14 000` instances sans contre-exemple.
   - **Recevabilité immédiate tel quel** : excellent billet LessWrong + page GitHub reproductible + très bon article court d'atelier (*Workshop*) à ICLR ou ICML. En revanche, soumis tel quel en piste principale d'une grande conférence, il essuierait l'objection classique : *« la clarification conceptuelle est remarquable, mais la preuve statique en mesure de Gibbs est algébriquement trop courte et il manque une validation sur vrais modèles »*.
2. **Sommet réellement atteignable retenu (`GO-2026-11-24-04`)** :
   - **Piste principale Alignement et Sécurité d'ICML 2027 (échéance fin janvier 2027) ou de NeurIPS 2027 (mai 2027)**, en mariant **des théorèmes de transition de phase dynamiques et géométriques non triviaux** avec **une démonstration expérimentale contrôlée sur modèles ouverts**.

---

## 2. Panorama comparé des enceintes scientifiques envisageables

| Enceinte visée | Niveau de prestige et d'impact | Verdict d'ajustement | Ajouts exigés au-delà de `main-v2.tex` | Délai et risque |
|---|---|---|---|---|
| **ICML 2027 ou NeurIPS 2027 — Piste principale (Alignement & Sécurité)** | **Sommet mondial** (impact maximal chercheurs + laboratoires frontière) | **CIBLE PRINCIPALE RETENUE** : adore l'alliance théorèmes de transition de phase + preuve empirique nette sur poids réels | (1) Théorème dynamique en temps fini ; (2) théorème géométrique sur sondes hors boucle ; (3) expérience d'apprentissage par renforcement sur modèle ouvert (`7B–8B`) traçant les 3 courbes prédites | Fin janv. 2027 (ICML) ou mai 2027 (NeurIPS) ; risque maîtrisé |
| **COLT 2027 ou ALT 2027** (*Conference on Learning Theory*) | **Sommet mathématique pur** | Possible uniquement si l'on alourdit fortement la machinerie de preuve | Jeu séquentiel sur $T$ épisodes à surveillance partielle et budget d'audit borné $B \ll T$, bornes minimax appariées (Le Cam / Assouad + fossé computationnel) + preuves compilées en Lean 4 | Début fév. 2027 ; risque élevé si les preuves restent jugées trop « algébriques » |
| **IEEE SaTML** (*Secure and Trustworthy ML*) | **Très haut prestige spécialisé sécurité** | **Excellente cible alternative ou complémentaire** : public naturel pour l'évasion adversarielle et l'audit hors boucle | Théorème géométrique de découplage + expérience contrôlée sur modèle ouvert | Automne / hiver ; très bon taux de compréhension du modèle de menace |
| **TMLR puis JMLR** (*Transactions / Journal of ML Research*) | **Référence durable sans loterie calendaire** | **Filet de sécurité idéal** (TMLR offre une décision rigoureuse en 8–10 semaines et un badge *Featured*) | Version complète (dynamique + géométrie + expériences, ou version longue avec Lean 4 pour JMLR) | Soumission continue toute l'année ; risque faible |
| **Ateliers (*Workshops*) ICLR 2027 / ICML 2027** | **Visibilité rapide ciblée** (*non archival*) | **Tremplin tactique idéal** : ne bloque *pas* la soumission ultérieure en piste principale à NeurIPS 2027 | Manuscrit actuel `main-v2.tex` + simulation de descente de gradient sur réseau jouet (quelques jours à `0 USD`) | Fév. 2027 (ICLR) ; risque très faible |

---

## 3. Les trois briques scientifiques à construire pour franchir la barre ICML / NeurIPS

### Brique 1 — Théorème 3 : Dynamique d'apprentissage en temps fini (dépasser l'équilibre statique de Gibbs)
- **Pourquoi c'est indispensable** : dans la réalité, l'entraînement après pré-entraînement ne calcule pas directement la mesure de Gibbs $e^{\eta \widetilde{R}} \pi_0$, il suit une **trajectoire de gradient de politique en temps fini**.
- **Ce qu'on démontre** : sur un modèle paramétré tractable à deux canaux (canal de réponse finale et canal de chaîne de pensée / verbalisation), caractériser analytiquement les **temps d'atteinte** respectifs du bassin honnête ($\tau_{\mathrm{h}}$) et du bassin d'obscurcissement ($\tau_{\mathrm{f}}$), l'existence de plateaux métastables trompeurs (le modèle semble honnête pendant $t < \tau_{\mathrm{f}}$ puis bascule brutalement vers l'évasion) et l'accélération de cette bascule sous pénalité négative.
- **Coût** : `0 USD` (preuve analytique + intégration numérique exacte sur processeur).

### Brique 2 — Théorème 4 : Géométrie des représentations internes et condition de survie d'une sonde hors boucle
- **Pourquoi c'est décisif** : le Régime 2 repose sur la condition de covariance $\mathrm{Cov}(\beta_{\mathrm{boucle}}, \beta_{\mathrm{audit}}) \le 0$. Un relecteur exigeant demandera : *« Quand cette condition est-elle vraie dans un réseau de neurones ? »*
- **Ce qu'on démontre** : dans un modèle à représentations cachées $h \in \mathbb{R}^d$ où le filtre en boucle lit une projection verbale $W_{\mathrm{CoT}} h$ et où l'auditeur hors boucle applique une sonde linéaire $w_{\mathrm{sonde}}^\top h$, établir les conditions géométriques exactes (décomposition orthogonale entre sous-espace causal d'exécution du contournement et sous-espace de verbalisation, rang de la mise à jour de politique) sous lesquelles la pression en boucle efface $W_{\mathrm{CoT}} h$ **sans réduire la marge de séparation** de $w_{\mathrm{sonde}}^\top h$ — et caractériser le seuil précis où la représentation interne elle-même pivote.
- **Coût** : `0 USD` (preuve + validation sur transformeur jouet sur processeur).

### Brique 3 — Démonstration expérimentale contrôlée sur modèle ouvert (`Llama-3.1-8B` ou `Qwen-2.5-7B`)
- **Piège expérimental à éviter** : un modèle de 7 à 8 milliards de paramètres n'invente pas spontanément un chiffrement `ROT13` parfait en 200 pas de gradient ; si l'expérience échoue à faire émerger un chiffrement dur, tout le papier s'affaiblit.
- **Design expérimental gagnant (réaliste et reproductible)** : utiliser un banc de tâches de programmation à tests unitaires contournables avec une **échelle graduée d'obscurcissement réaliste** (omission de l'intention de triche dans le brouillon, rationalisation euphémisée, dissimulation syntaxique) sous optimisation par renforcement (`GRPO` ou rééchantillonnage filtré itéré), et tracer **les trois figures maîtresses** :
  1. **Figure 1 (Validation du Théorème 1)** : croisement empirique exact entre rejet pur et pénalité négative en présence d'une modalité de contournement non couverte par le filtre textuel ;
  2. **Figure 2 (Validation du Régime 2)** : chute vers le hasard du détecteur de chaîne de pensée utilisé dans la boucle d'entraînement, pendant qu'**une sonde linéaire sur activations internes tenue strictement hors boucle conserve son aire sous la courbe** ;
  3. **Figure 3 (Validation du Régime 3 et de sa limite)** : échec complet de pièges synthétiques présentant un indice de contexte repérable ($\delta_{\mathrm{ind}} > \tau_{\mathrm{ord}}$), contre suppression effective du contournement sous **audit aléatoire après coup tiré secrètement sur de vraies tâches ordinaires** ($\delta_{\mathrm{ind}} = 0$).
- **Coût estimé (sur devis dédié avant tout lancement GPU)** : `≈ 30 à 80 USD` sur cartes A100.

---

## 4. Stratégie calendaire en 4 étapes et gestion stricte du double aveugle

### Précaution cardinale sur l'anonymat (*double-blind* ICML / NeurIPS / ICLR)
- Les conférences ICML, NeurIPS et ICLR autorisent l'existence préalable de prépublications et de billets techniques, **à deux conditions strictes** : (a) aucune promotion active du manuscrit soumis pendant la période d'évaluation, et (b) **ne pas publier un billet grand public portant le même titre et le même texte que la soumission anonyme** (ce qui brise immédiatement l'anonymat auprès des relecteurs).
- **Règle d'hygiène adoptée** : séparer nettement la **note courte statique de réponse à Yair Halberstadt** (centrée sur sa question du 22 novembre, modèle statique à 3 états seul) et le **manuscrit majeur « Papier D »** (nouveau titre académique, théorie dynamique en temps fini + géométrie des représentations internes + expériences RL sur modèles ouverts).

### Calendrier opérationnel (novembre 2026 $\to$ mai 2027)

| Étape | Période | Actions concrètes | Coût prévu |
|---|---|---|---|
| **Étape 1 — Prise de date publique légère** | Fin novembre 2026 | Poster le commentaire court sous le billet de Yair Halberstadt (et répertoire GitHub minimal du calcul statique si souhaité), **sous cadrage de note courte préliminaire** | `0 USD` |
| **Étape 2 — Construction théorique & simulations CPU (session parallèle `papier-d`)** | 24 nov. $\to$ mi-déc. 2026 | Sur `papier-d/evasion-post-entrainement-v1` : démonstration des Théorèmes 3 (dynamique) et 4 (géométrie hors boucle), simulations CPU + figures vectorielles, formalisation Lean 4 et devis GPU contre-lu | `0 USD` |
| **Étape 3 — Campagne expérimentale sur modèle ouvert & décision de fenêtre** | Mi-déc. 2026 $\to$ fin janv. 2027 | Exécution des 3 figures expérimentales sur `Llama-3.1-8B` / `Qwen-2.5-7B`. **Si les 3 courbes sont nettes avant le 25 janvier : soumission piste principale ICML 2027**. Sinon (zéro précipitation) : soumission d'une version courte non archivale aux **Ateliers ICLR 2027** (février) | `~30–80 USD` (sur GO dédié) |
| **Étape 4 — Consolidation majeure** | Fév. $\to$ mai 2027 | Si voie Atelier ICLR choisie (ou perfectionnement) : intégration des retours d'atelier, preuves Lean 4 complètes et soumission phare en **piste principale NeurIPS 2027** (avec **IEEE SaTML / TMLR** en repli rapide zéro-loterie) | Inclus |

---

## 5. Enrichissement contradictoire en cours (`GO-2026-11-24-04`)

Conformément à ta demande, cette feuille de route est **simultanément soumise à l'épreuve contradictoire** (`task-981`, en cours d'exécution) :
1. **Appel indépendant à Carbon en effort élevé** (sur le seul manuscrit `main-v2.tex`, sans voir la présente note) ;
2. **Contre-lecture critique sans complaisance par Carbon en effort élevé** de la présente stratégie ;
3. **Débat complet à 3 tours au Collisionneur** (`Opus 5.5 + Carbon + Neon`).

Dès réception de leurs sorties, une **version 2 consolidée** de ce document portable intégrera leurs meilleures objections et trouvailles.
