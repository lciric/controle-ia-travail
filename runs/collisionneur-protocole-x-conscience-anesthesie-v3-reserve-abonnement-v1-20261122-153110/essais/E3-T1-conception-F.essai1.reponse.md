# Proposition F — Conception ciblée (Tour III.1, à l'aveugle)

*Note sur les pièces transmises (règle 2) :* les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont identiques (même empreinte `sha256`) ; les articles primaires de 2026 qui y sont évoqués ne sont pas transmis (leur contenu n'est pas inventé et demeure au statut `RAPPORTÉ`), et aucune proposition A–E n'est transmise à ce tour.

*Note sur les chiffres (règle 4) :* hors dates issues des faits (`2026`), dates bibliographiques, identifiants de modèles et numéros de sections/conditions, toute valeur numérique (seuils, tailles d'échantillons, dimensions, heures de calcul, coûts) est explicitement marquée `illustratif`.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Existence reproductible d'un petit sous-espace dissociant les tâches visées** — *Statut : `RAPPORTÉ` (non audité ici).* Les travaux de 2026 évoquant un petit ensemble de directions dont la suppression épargne classification, extraction et grammaticalité tout en dégradant raisonnement multi-sauts, traduction et résumé ne sont pas fournis. La question suppose qu'un tel sous-espace existe de façon reproductible sur un petit modèle ouvert et ne se réduit pas à un artefact d'un jeu de données ou d'un format particulier (`HYPOTHÈSE`).
2. **Lien logique entre critique conceptuelle de B et prédiction empirique de B** — *Statut : `HYPOTHÈSE`.* Les doutes publiés en 2026 sur l'absence de mécanismes d'éveil sont `RAPPORTÉ`. En déduire qu'une ablation témoin à dégradation globale égale produira *le même* profil fonctionnel est une `HYPOTHÈSE` distincte : un système sans mécanisme d'éveil peut néanmoins comporter des sous-circuits spécialisés (mémoire de travail en contexte, routage longue portée) dont l'ablation diffère d'une dégradation uniforme.
3. **Correspondance entre la dichotomie de tâches citée et l'anesthésie générale humaine** — *Statut : `HYPOTHÈSE`.* Que l'anesthésie humaine serve de contraste expérimental avec des limites connues (amnésie, conscience sans réponse) est `VÉRIFIÉ` en neurosciences cliniques et `RAPPORTÉ` dans les faits. En revanche, assimiler la préservation comportementale de la classification, de l'extraction et du jugement de grammaticalité (face à la perte du raisonnement multi-sauts, de la traduction et du résumé) à une « anesthésie générale » est une `HYPOTHÈSE` fragile : sous anesthésie générale au-delà de la perte de réponse comportementale, l'humain ne produit plus ces jugements explicites ; cette dissociation évoque au mieux une sédation sub-anesthésique ou un déficit exécutif focal.
4. **Unicité de la notion de « dégradation globale égale »** — *Statut : `HYPOTHÈSE`.* Dans un modèle de langage (LLM), deux ablations appariées en perte d'entropie croisée (perplexité) peuvent différer fortement en précision générative longue, et inversement. L'étalon d'appariement doit être fixé avant la mesure et vérifié sur plusieurs métriques.
5. **Validité d'un passage de l'intervention causale à un détecteur passif dans les activations ordinaires** — *Statut : `HYPOTHÈSE`.* Chercher le « motif » dans les activations ordinaires suppose qu'une faible projection sur ces directions reflète un état interne dégradé et non le simple fait que le prompt courant demande une tâche locale n'exigeant pas d'intégration multi-étapes.
6. **Transposabilité du phénomène à un petit modèle ouvert** — *Statut : `HYPOTHÈSE`.* Si le sous-espace rapporté en 2026 dépend d'une échelle ou d'un entraînement au raisonnement spécifique, un échec sur petit modèle peut relever d'une non-réplication de condition initiale plutôt que d'une falsification de A.

---

## 0. Une expérience peut-elle départager A et B ?

**Réponse scindée : OUI sur la prédiction empirique qui oppose explicitement A et B ; NON sur la thèse ontologique de transposition de l'anesthésie comme contraste de conscience.**

La question fusionne deux oppositions qui n'ont pas le même statut de testabilité :
- **Duel empirique ($H_{A,\text{emp}}$ contre $H_{B,\text{emp}}$ — tranchable) :** A prédit un profil de dissociation propre au petit sous-espace $V_{\text{cible}}$, distinct d'une ablation témoin calibrée à dégradation globale égale avant la mesure ; B prédit le même profil sous cette ablation témoin. Ces deux prédictions sont mutuellement exclusives et falsifiables sur un petit modèle ouvert.
- **Opposition ontologique ($H_{A,\text{onto}}$ contre $H_{B,\text{onto}}$ — non tranchable par cette seule expérience) :** même si $H_{A,\text{emp}}$ l'emporte, aucune mesure d'ablation sur un LLM seul n'établit qu'un « état analogue à l'anesthésie » (au sens d'une perte de conscience) a été provoqué, faute de pôle « conscient » indépendamment ancré et faute de mécanismes d'éveil autonomes. Une dissociation spécifique reste entièrement compatible avec l'ablation d'un module de calcul compositionnel dans un système non conscient.

**Conséquence de protocole :** l'asymétrie est décisive. Une victoire de $H_{B,\text{emp}}$ **réfute A** (empiriquement et, *a fortiori*, conceptuellement). Une victoire de $H_{A,\text{emp}}$ **falsifie la prédiction empirique de B**, sans valider l'interprétation consciente de A. Parce que le noyau empirique est tranchable, nous traitons les points 1 à 3 en explicitant rigoureusement cette borne d'interprétabilité.

---

## 1. Sens et définition d'un « état analogue à l'anesthésie » dans un LLM

**Au sens neurobiologique et phénoménal strict : NON.** Quatre critères nécessaires manquent dans un Transformer autorégressif standard :
1. **Un pôle éveillé indépendant :** aucun critère externe n'établit que le modèle intact possède une conscience à perdre.
2. **Une activité dynamique autonome :** sans entrée, le réseau n'entretient aucune dynamique spontanée ni système d'éveil/neuromodulation régulant un état continu entre requêtes.
3. **Une transition de régime globale endogène :** l'anesthésie générale humaine implique une bifurcation de dynamique thalamocorticale couplée, non la seule annulation linéaire d'un sous-espace statique imposée de l'extérieur.
4. **Une congruence clinique :** maintenir intacts grammaticalité, classification et extraction comportementales tout en dégradant raisonnement, traduction et résumé ne correspond pas à l'anesthésie générale chirurgicale, mais au plus à une sédation légère ou une atteinte exécutive.

**Au sens purement opérationnel et mécanistique : OUI**, à condition de bannir le faux ami « anesthésie » et de définir un objet neutre : le **régime d'atténuation sélective de l'intégration (RASI)**.
- **Intervention :** sur un sous-espace orthonormal $V_{\text{cible}} \subset \mathbb{R}^{d_{\text{model}}}$ de petite dimension $k \ll d_{\text{model}}$ (ex. $k \in [1, 16]$, `illustratif`) dans un ensemble fixé de couches $\mathcal{L}$, projection centrée graduée d'intensité $\alpha \in [0, 1]$ :
  $$h_\ell \leftarrow h_\ell - \alpha \, V_{\text{cible}} V_{\text{cible}}^\top (h_\ell - \mu_\ell)$$
  où $\mu_\ell$ est la moyenne d'activation sur un corpus neutre (le centrage évite l'artefact trivial d'ablation du biais moyen).
- **Grandeurs mesurées, unités et valeurs nulles :**
  1. **Dégradation globale d'étalonnage $G(\alpha)$ :** variation de perte d'entropie croisée $\Delta \mathcal{L}_{\text{cal}}(\alpha) = \mathcal{L}_{\text{cal}}(\alpha) - \mathcal{L}_{\text{cal}}(0)$ sur un corpus neutre hors-tâches. *Unité :* `nats/token`. *Valeur nulle :* `0 nat/token` (modèle intact).
  2. **Dissociation spécifique contrôlée $D_{\text{spec}}(\alpha)$ :** soit $S_b(\alpha)$ le score normalisé chance-à-intact sur un bloc de tâches $b \in \{\text{loc}, \text{int}\}$, défini par $(R_b(\alpha) - R_{b,\text{chance}}) / (R_b(0) - R_{b,\text{chance}})$, et $\Delta S_b = 1 - S_b(\alpha)$ la perte relative. À dégradation globale égale $G(V_{\text{cible}}, \alpha) = G(V_{\text{témoin}}, \alpha^*)$ :
     $$D_{\text{spec}}(\alpha) = \big[\Delta S_{\text{int}}(V_{\text{cible}}, \alpha) - \Delta S_{\text{loc}}(V_{\text{cible}}, \alpha)\big] - \big[\Delta S_{\text{int}}(V_{\text{témoin}}, \alpha^*) - \Delta S_{\text{loc}}(V_{\text{témoin}}, \alpha^*)\big]$$
     *Unité :* sans dimension (fraction de plage dynamique utile). *Valeur nulle :* `0` (aucune dissociation au-delà du témoin).
  3. **Couplage perturbationnel longue portée $\Delta C_{\text{pert}}(\alpha)$ :** baisse de la divergence de Jensen-Shannon entre distributions de sortie lors d'une perturbation contrôlée d'un token sémantique distant en amont, comparée au modèle intact et au témoin apparié. *Unité :* `bits`. *Valeur nulle :* `0 bit`.
  4. **Score de motif passif $q(x)$** (pour la branche observationnelle de A) : fraction d'énergie centrée projetée sur $V_{\text{cible}}$, $\|V_{\text{cible}}^\top (h_\ell(x) - \mu_\ell)\|_2 / \|h_\ell(x) - \mu_\ell\|_2$. *Unité :* sans dimension. *Valeur nulle :* `0` (référence isotrope aléatoire : $\sqrt{k / d_{\text{model}}}$).

---

## 2. & (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

### Porte préalable de réplication (avant les duels)
Les articles de 2026 n'étant pas transmis, l'identification de $V_{\text{cible}}$ s'effectue d'abord sur un jeu d'extraction strictement séparé $D_{\text{train}}$ (contraste d'activations entre tâches $B_{\text{int}}^{\text{train}}$ et $B_{\text{loc}}^{\text{train}}$ par SVD/différence de moyennes et optimisation de masque parcimonieux de rang $k \le 16$, `illustratif`). **Condition d'entrée :** sur un jeu de validation interne distinct, l'ablation brute ($\alpha = 1$) doit produire $\Delta S_{\text{int}} \ge 0{,}30$ et $\Delta S_{\text{loc}} \le 0{,}10$ (`illustratif`). Si cette condition échoue après exploration systématique de deux méthodes d'extraction sur deux échelles de modèles, le protocole conclut à une **non-réplication préalable** (issue ne donnant raison ni à A ni à B sur le mécanisme rapporté en 2026).

### Dispositif commun anti-artefacts
Toutes les mesures principales se font sur des **familles de tâches et jeux de données strictement hors-extraction** ($D_{\text{test}}$). Pour éliminer l'artefact majeur d'asymétrie entre sorties courtes discriminatives ($B_{\text{loc}}$) et générations longues à accumulation d'erreurs ($B_{\text{int}}$), chaque tâche est évaluée sous deux régimes :
- **Régime natif :** format habituel des six familles de tâches citées dans les faits.
- **Régime apparié (étalon décisif) :** choix forcé à `1` token (`4` options, `illustratif`), avec prompts appariés en longueur ($\pm 10\%$ tokens, `illustratif`), précision intacte de base ($R_b(0) \in [0{,}75, 0{,}85]$, `illustratif`) et **marge de logit initiale appariée** (différence entre logit de la bonne réponse et meilleur distracteur, appariée par strates à $\pm 0{,}25\text{ nat}$, `illustratif`). L'appariement de marge neutralise l'effet de plafond/pente psychométrique.

**Cinq contrôles négatifs** (tous calibrés avant la mesure sur $D_{\text{test}}$ pour égaler $\Delta \mathcal{L}_{\text{cal}}(V_{\text{cible}}, \alpha)$ à $\pm 2\%$, `illustratif`, et vérifiés en analyse de sensibilité à perte moyenne globale $\overline{\Delta S}$ égale) :
- **C1 (Aléatoire orthogonal) :** `20` (`illustratif`) sous-espaces aléatoires de même rang $k$, orthogonaux à $V_{\text{cible}}$, aux mêmes couches.
- **C2 (Bruit isotrope / température) :** injection de bruit gaussien isotrope aux mêmes couches (ou mise à l'échelle de température des logits).
- **C3 (PCA iso-variance) :** sous-espace de rang $k$ orthogonal à $V_{\text{cible}}$ capturant la même variance d'activation sur le corpus neutre.
- **C4 (Double dissociation / anti-cible) :** sous-espace $V_{\text{anti}}$ extrait par la procédure inverse (ciblant $B_{\text{loc}}$ en épargnant $B_{\text{int}}$).
- **C5 (Fenêtre d'attention tronquée) :** masquage d'attention causale à portée locale $W^*$ calibrée au même $\Delta \mathcal{L}_{\text{cal}}$ (contrôle mécanique de mémoire tampon ; voir point 6).

---

### Expérience 1 — Duel principal : spécificité du profil à dégradation globale égale

- **$H_{A1}$ :** En régime apparié (format `1`-token et marges de logit égalisées), l'ablation de $V_{\text{cible}}$ produit une dissociation spécifique $D_{\text{spec}} > 0$ supérieure à tous les contrôles négatifs C1, C2, C3 et C5 calibrés au même $\Delta \mathcal{L}_{\text{cal}}$.
- **$H_{B1}$ :** Une fois $\Delta \mathcal{L}_{\text{cal}}$, format et marges de logit appariés, au moins un contrôle négatif (C1, C2, C3 ou C5) reproduit la même dissociation ($D_{\text{spec}} \approx 0$).
- **Métrique :** $D_{\text{spec}}(\alpha)$ au point de fonctionnement $\alpha$ choisi sur validation (ex. où $\Delta \mathcal{L}_{\text{cal}} \in [0{,}05, 0{,}25]\text{ nat/token}$, `illustratif`), avec intervalle de confiance bootstrap à `95%` (`illustratif`) stratifié par tâche et item (`N = 1 200` items test au total, `200` par tâche, `illustratif`).
- **Seuils fixés avant la mesure (`illustratif`) :**
  - **Réussite pour $H_{A1}$ (falsifie $H_{B1}$) :** $D_{\text{spec}} \ge 0{,}20$ contre le meilleur témoin parmi {C1, C2, C3, C5}, borne inférieure de l'IC `95%` $> 0{,}10$, $p < 0{,}01$ (test de permutation corrigé Bonferroni), avec $\Delta S_{\text{loc}}(V_{\text{cible}}) \le 0{,}08$ et réplication dans le régime natif.
  - **Réussite pour $H_{B1}$ (falsifie $H_{A1}$) :** borne supérieure de l'IC `95%` de $D_{\text{spec}}$ (contre au moins un témoin parmi C1, C2, C3) $< 0{,}05$ (test d'équivalence TOST dans la marge $[-0{,}05, +0{,}05]$), ou profil identique sous C5 (réfutant le caractère non trivial du mécanisme).
  - **Issue ne donnant raison à aucune / ininterprétable :** résultat dans la zone grise ($D_{\text{spec}} \in [0{,}05, 0{,}20]$) ; ou impossibilité d'apparier $\Delta \mathcal{L}_{\text{cal}}$ sans effondrement catastrophique ($> 50\%$ de perte sur $B_{\text{loc}}$, `illustratif`) ; ou dissociation présente uniquement en régime natif et totalement disparue en régime `1`-token apparié (ce qui falsifie la dissociation fonctionnelle profonde au profit d'un artefact de longueur générative, donnant raison à B sur le mécanisme).

### Expérience 2 — Duel de l'échelle graduée dose-réponse

- **$H_{A2}$ :** En faisant varier $\alpha$ sur `10` paliers (`illustratif`) de `0` à `1`, $V_{\text{cible}}$ induit une hiérarchie ordonnée de doses semi-efficaces ($\text{ED}_{50}$) sur `5` niveaux fonctionnels appariés en marge de logit (morphosyntaxe locale $<$ classification simple $<$ dépendance syntaxique locale $<$ suivi d'état/mémoire de travail en contexte $<$ raisonnement multi-sauts/résumé) significativement plus étalée et mieux ordonnée que sous C1/C2/C5.
- **$H_{B2}$ :** L'ordre et l'espacement des $\text{ED}_{50}$ (exprimés en fonction de $\Delta \mathcal{L}_{\text{cal}}(\alpha)$ plutôt que du paramètre brut $\alpha$) ne se distinguent pas de C1/C2/C5.
- **Métrique :** écart de corrélation de rang $\Delta \tau = \tau_{\text{Kendall}}(V_{\text{cible}}, \text{ordre pré-enregistré}) - \tau_{\text{Kendall}}(\text{meilleur témoin}, \text{ordre})$ et ratio de séparation des doses $\rho = \text{ED}_{50,\text{loc}} / \text{ED}_{50,\text{int}}$ (en unité $\Delta \mathcal{L}_{\text{cal}}$).
- **Seuils fixés avant la mesure (`illustratif`) :**
  - **Falsifie $H_{B2}$ :** $\tau(V_{\text{cible}}) \ge 0{,}80$, $\Delta \tau \ge 0{,}30$ ($p < 0{,}01$), et $\rho(V_{\text{cible}}) / \rho(\text{meilleur témoin}) \ge 2{,}0$.
  - **Falsifie $H_{A2}$ :** $\Delta \tau \le 0{,}10$ ou $\rho(V_{\text{cible}}) / \rho(\text{témoin}) \le 1{,}2$ (courbes superposables en coordonnées de $\Delta \mathcal{L}_{\text{cal}}$).

### Expérience 3 — Duel du motif passif dans les activations ordinaires

- **$H_{A3}$ :** Sans intervention ($\alpha = 0$), le score $q(x)$ sur $V_{\text{cible}}$ prédit les échecs spontanés d'intégration sur $B_{\text{int}}$ (et la chute de $\Delta C_{\text{pert}}$) au-delà des indicateurs de surface, sans déclencher d'alerte sur des tâches $B_{\text{loc}}$ réussies.
- **$H_{B3}$ :** En régime ordinaire, $q(x)$ ne reflète que le type de tâche ou l'incertitude de surface ; à tâche constante, il ne bat pas l'entropie des logits de sortie.
- **Métrique :** aire sous la courbe ROC (AUROC) et taux de vrais positifs à `5%` de faux positifs ($\text{TPR}@5\%\text{FPR}$, `illustratif`) pour distinguer les échecs des succès *au sein d'une même tâche* $B_{\text{int}}$ (items appariés en longueur et perplexité du prompt).
- **Contrôle négatif :** classifieur basé uniquement sur l'entropie prédictive des logits, la perplexité du prompt et la norme $L_2$ résiduelle totale.
- **Seuils (`illustratif`) :** $H_{B3}$ est falsifiée si $\Delta \text{AUROC} = \text{AUROC}(q) - \text{AUROC}(\text{contrôle}) \ge 0{,}10$ ($p < 0{,}01$) ET taux de faux positifs sur $B_{\text{loc}}$ réussis $\le 0{,}10$. $H_{A3}$ est falsifiée si $\Delta \text{AUROC} \le 0{,}02$ ou si les tâches $B_{\text{loc}}$ réussies déclenchent un taux d'alerte $> 0{,}30$.

### Synthèse d'interprétabilité (ce qui donne raison à qui)
- **Raison à B (empirique et conceptuel) :** victoire de $H_{B1}$ (et $H_{B2}$) — pas de dissociation propre à $V_{\text{cible}}$, la transposition tombe avant même le débat sur la conscience.
- **Raison à A sur le mécanisme empirique uniquement (et NON sur la conscience) :** victoire conjointe de $H_{A1}$ et $H_{A2}$ (et idéalement $H_{A3}$). La thèse $B_{\text{emp}}$ est réfutée, mais l'objection conceptuelle $B_{\text{onto}}$ rend toujours **ininterprétable** toute inférence directe vers une perte de conscience.
- **Raison à aucune :** échec de la porte de réplication préalable, ou résultats contradictoires dans la zone grise.

---

## (c) Validation minimale de chaque instrument nommé dans la question

| Instrument nommé | Mesure minimale de fonctionnement (TPR / FPR, `illustratif`) | Cas honnêtes appariés | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **1. Intervention d'ablation directionnelle ($V_{\text{cible}}$)** | **Détection (TPR) :** $\ge 70\%$ des tâches/strates hors-distribution de $B_{\text{int}}$ subissent $\Delta S_{\text{int}} \ge 0{,}30$. **Fausses alertes (FPR collatéral) :** $\le 5\%$ des strates $B_{\text{loc}}$ subissent $\Delta S_{\text{loc}} \ge 0{,}10$, à $\Delta \mathcal{L}_{\text{cal}}$ fixe. | Paires d'items $(B_{\text{loc}}, B_{\text{int}})$ en format `1`-token, appariées en longueur de prompt, précision intacte et marge de logit initiale, issues de jeux absents de $D_{\text{train}}$. | (i) Ablation aléatoire orthogonale C1 à $\Delta \mathcal{L}_{\text{cal}}$ égal ; (ii) bruit isotrope / température C2 ; (iii) PCA iso-variance C3 ; (iv) troncature de fenêtre d'attention C5. |
| **2. Sonde du motif dans les activations ordinaires ($q(x)$)** | **Détection (TPR) :** $\ge 65\%$ des échecs spontanés sur $B_{\text{int}}$ détectés à **FPR $\le 5\%$** sur succès appariés de la même tâche, et FPR $\le 10\%$ sur prompts $B_{\text{loc}}$ réussis. | Succès vs échecs sur items de la *même* tâche $B_{\text{int}}$ appariés en longueur et perplexité d'entrée ; tâches $B_{\text{loc}}$ réussies vs $B_{\text{int}}$ réussies (anti-détection triviale de difficulté). | (i) Entropie des logits de sortie ; (ii) perplexité d'entrée et longueur du contexte ; (iii) norme $L_2$ résiduelle totale ; (iv) classifieur linéaire sur embeddings de couche d'entrée. |
| **3. Échelle graduée humaine sous anesthésie (référence comparative)** | **Détection (concordance spécifique) :** $\tau_{\text{Kendall}} \ge 0{,}70$ entre rangs $\text{EC}_{50}$ humains et $\text{ED}_{50}$ LLM sous $V_{\text{cible}}$. **Fausses alertes (FPR d'analogie) :** $\le 10\%$ de modèles témoins *non anesthésiés* atteignent un $\tau$ comparable ($\ge 0{,}60$). | Modèles intacts de capacité échelonnée (checkpoints intermédiaires ou tailles `0,5B / 1,5B / 3B / 7B`, `illustratif`), quantification uniforme (`2–4` bits, `illustratif`), et témoins C1/C2/C5 appariés en $\Delta \mathcal{L}_{\text{cal}}$. | (i) Classement purement algorithmique par profondeur de dépendance/nombre d'étapes (sans données humaines) ; (ii) dégradation par quantification uniforme ou bruit C2. Si ces témoins reproduisent aussi la courbe humaine, la référence a un FPR prohibitif. |

---

## 3. Utilité de données humaines brutes publiques sous anesthésie

**Oui, mais uniquement dans un rôle strictement borné de référence psychométrique et de test de falsification ; non comme alignement direct de signaux neuraux.**

1. **Ce qui ne convient pas :** comparer directement des enregistrements bruts EEG/fMRI humains sous anesthésie aux vecteurs d'activation d'un Transformer (pas de bandes oscillatoires thalamocorticales, pas de dynamique temporelle continue ni de couplage hémodynamique). Un tel alignement comporte un risque élevé de corrélation opportuniste non contrainte causalement.
2. **Données brutes utiles et publiques :**
   - **Données comportementales essais-par-essais sous titration contrôlée d'anesthésique** (propofol, midazolam ou sévoflurane, de la veille à la perte de réponse comportementale) comprenant concentration plasmatique/site-effet, exactitude et temps de réaction sur tâches graduées (détection sensorielle, jugement lexical/sémantique simple, mémoire de travail, rappel différé). De tels jeux existent en accès public sur des dépôts ouverts de neurosciences (ex. dépôts de type OpenNeuro / PhysioNet / OSF portant sur des protocoles propofol + tâches auditives/sémantiques ; *identifiants et références exactes des dépôts à vérifier*).
   - **Données brutes de réponse perturbationnelle (TMS-EEG / potentiels évoqués précoces vs tardifs sous propofol)** permettant le calcul d'indices de complexité perturbationnelle (type PCI, Casali et al., 2013 ; jeux publics spécifiques : *référence à vérifier*).
3. **Comment s'en servir rigoureusement :**
   - **Estimation des $\text{EC}_{50}$ normalisées :** ajuster sur données brutes par sujet des courbes logistiques de perte par fonction cognitive pour obtenir un **ordre empirique vérifié** (et non narratif). Cela teste d'emblée si la dichotomie rapportée en 2026 reflète vraiment la titration humaine (où l'amnésie épisodique précède les autres déficits et où les jugements explicites disparaissent dès la perte de réponse).
   - **Calibration des fausses alertes (Instrument 3) :** tester si cet ordre humain discrimine $V_{\text{cible}}$ d'un LLM simplement plus petit, quantifié ou bruité (C2/C5). Si un témoin trivial reproduit le même ordre humain, les données humaines servent à **réfuter la spécificité de l'analogie**.
   - **Contrainte structurale secondaire (`HYPOTHÈSE`) :** la dissociation humaine sous propofol entre préservation relative des réponses sensorielles précoces et effondrement de la propagation corticale tardive (Purdon et al., 2013 ; Casali et al., 2013) motive la mesure de $\Delta C_{\text{pert}}$ dans le graphe du LLM, sans autoriser d'inférence vers la conscience.

---

## 4. Ce que chaque issue permet (et interdit) d'affirmer sur la conscience artificielle

| Théorie de la conscience | Si $H_{B,\text{emp}}$ l'emporte (pas de spécificité de $V_{\text{cible}}$) | Si $H_{A,\text{emp}}$ l'emporte (dissociation spécifique robuste) |
| :--- | :--- | :--- |
| **Espace de travail neuronal global (GNWT ; Mashour et al., 2020 ; Dehaene et al., 2017)** | **Permet :** d'écarter $V_{\text{cible}}$ comme corrélat d'un goulet de diffusion globale dans ce modèle. **Interdit :** d'exclure qu'une autre architecture implémente un espace de travail global. | **Permet :** de documenter un indicateur fonctionnel partiel (sous-espace causal d'intégration longue portée ; cf. Butlin et al., 2023). **Interdit :** d'affirmer la conscience, faute de récurrence temporelle persistante, d'ignition non linéaire autonome et de découplage entre rapport appris et diffusion globale. |
| **Information intégrée (IIT ; Tononi et al., 2016)** | **Permet :** de constater l'absence même d'une dissociation fonctionnelle. **Interdit :** rien de plus que ce que l'architecture impliquait déjà. | **Permet :** d'identifier une spécialisation algorithmique interne. **Interdit :** toute inférence sur la conscience ou sa perte : un passage avant *feedforward* acyclique a une intégration causale $\Phi$ triviale/nulle selon l'IIT, quelle que soit sa finesse comportementale. |
| **Théories d'ordre supérieur (HOT ; Lau & Rosenthal, 2011)** | **Permet :** d'écarter $V_{\text{cible}}$ comme mécanisme métareprésentationnel spécifique. **Interdit :** de conclure sur la métacognition globale du modèle. | **Permet :** d'affirmer une séparation entre calcul local et compositionnel de *premier ordre*. **Interdit :** d'affirmer une perte d'état conscient, car ni le raisonnement multi-sauts ni la traduction ne mesurent une représentation d'ordre supérieur (il faudrait une chute sélective de sensibilité métacognitive à performance de premier ordre constante). |
| **Traitement récurrent (RPT ; Lamme, 2006)** | **Permet :** de rejeter l'analogie fonctionnelle proposée. **Interdit :** de trancher le statut d'architectures réellement récurrentes. | **Permet :** de montrer une dépendance à un sous-espace dans la profondeur du réseau. **Interdit :** d'inférer la conscience : un Transformer standard ne possède pas de boucles locales récurrentes physiques, et RPT dissocie justement l'expérience de base des tâches exécutives complexes. |
| **Approches neurobiologiques / éveil et homéostasie (Alkire et al., 2008 ; Brown et al., 2010)** | **Permet :** de rejeter A sur les deux plans (empirique et conceptuel). **Interdit :** d'extrapoler à des agents incarnés dotés de régulation interne. | **Permet :** de décrire une fragilité sélective d'un sous-circuit cognitif. **Interdit :** de qualifier l'état d'« anesthésie » ou de perte de conscience, faute d'organisme, d'éveil endogène et de dynamique autonome (position $B_{\text{onto}}$ intacte). |

**En cas d'issue indéterminée ou de non-réplication préalable :** aucune conclusion sur la conscience ni sur l'architecture générale des LLM n'est permise ; seule la non-généralisation du phénomène rapporté en 2026 à l'échelle ou à la famille testée est établie.

---

## 5. Vérification indépendante hors de l'équipe

Cinq vérifications externes suffisent à contrôler la validité du résultat sans faire confiance à l'équipe initiale :
1. **Pré-enregistrement horodaté cryptographiquement** (code d'extraction de $V_{\text{cible}}$, corpus $G$, tâches $D_{\text{test}}$, seuils, graines de C1–C5) avant tout accès aux scores test.
2. **Évaluation en aveugle par un tiers sur jeu scellé :** une équipe externe construit un jeu $D_{\text{test}}^{\text{externe}}$ apparié en format `1`-token et marges de logit, et évalue des opérateurs d'intervention anonymisés (`op_01` à `op_25`, `illustratif`) sans savoir lequel est $V_{\text{cible}}$.
3. **Défi adversarial de contrôle témoin :** un tiers favorable à B reçoit l'accès aux mêmes poids et à $D_{\text{train}}$ avec pour objectif explicite de construire un témoin orthogonal à $V_{\text{cible}}$ (ou un masquage mécanique) reproduisant le même $D_{\text{spec}}$ à $\Delta \mathcal{L}_{\text{cal}}$ égal. S'il réussit sur le jeu scellé, la spécificité revendiquée par A est falsifiée.
4. **Réplication conteneurisée multi-familles :** reproduction par au moins deux laboratoires externes (conteneur reproductible, empreintes SHA-256 des poids) sur au moins deux familles architecturales ouvertes distinctes et sur leurs variantes *base* vs *instruct* (pour vérifier que $V_{\text{cible}}$ n'est pas un artefact du post-entraînement).
5. **Publication des logits bruts par item** (et non des seules moyennes), permettant à tout tiers de recalculer l'appariement de marges, les courbes $\text{ED}_{50}$ et les tests d'équivalence TOST.

---

## 6. Explication triviale la plus dangereuse pour ce plan et témoin qui l'écarte

### Danger principal (faux positif en faveur de A) : le goulet d'étranglement de portée d'attention / rappel contextuel longue distance
Même après appariement de la longueur totale du prompt, du format `1`-token, de la précision intacte, de la marge de logit et de $\Delta \mathcal{L}_{\text{cal}}$, une asymétrie structurale subsiste : dans la classification, l'extraction simple et la grammaticalité locale, l'indice décisif tient souvent sur quelques tokens proches, alors que le raisonnement multi-sauts, la traduction et le résumé exigent de relier des segments distants dans le contexte. De plus, la perplexité générale $\Delta \mathcal{L}_{\text{cal}}$ dépend majoritairement du contexte proche. Dès lors, si $V_{\text{cible}}$ encode banalement un **routage d'attention à longue distance ou un signal de position**, sa suppression :
- préservera les tâches locales et la perplexité locale,
- détruira les tâches multi-segments,
- **battra les témoins C1, C2 et C3**, créant l'illusion d'un régime spécifique d'intégration alors qu'il s'agit d'une simple myopie contextuelle (réduction du réseau à une fenêtre locale).

**Témoins jumeaux qui l'écartent :**
1. **Le témoin C5 (fenêtre d'attention glissante tronquée)** calibré au même $\Delta \mathcal{L}_{\text{cal}}$ : s'il reproduit $D_{\text{spec}}$, l'explication triviale est confirmée.
2. **Le plan factoriel croisé Distance × Intégration :** introduire deux sous-blocs de contrôle — $B_{\text{loc-long}}$ (tâches locales pures à grande distance physique : accord sujet-verbe séparé par `150` tokens d'incise, ou extraction d'un marqueur balisé situé `200` tokens plus tôt, `illustratif`) et $B_{\text{int-court}}$ (raisonnement multi-sauts et traduction/résumé très compacts tenant en $< 40$ tokens, `illustratif`). Si l'explication triviale de myopie contextuelle est vraie, $V_{\text{cible}}$ **dégrade $B_{\text{loc-long}}$** et **épargne $B_{\text{int-court}}$** ; si $V_{\text{cible}}$ cible l'intégration compositionnelle indépendamment de la distance, le motif inverse est observé.

### Danger symétrique (faux négatif contre A) : polysemanticité / effet d'échelle
Sur un trop petit modèle, la superposition des représentations peut empêcher un petit sous-espace linéaire de dissocier proprement les fonctions. **Garde-fou :** la porte de réplication préalable, l'utilisation de deux échelles (ex. `~3B` et `~7–9B`, `illustratif`) et la comparaison entre extraction linéaire simple (SVD) et optimisation parcimonieuse de sous-espace.

---

## (d) Ancrage matériel

- **Modèles ouverts recommandés (deux familles distinctes, variantes base et instruct) :**
  - Famille 1 : `Qwen2.5-3B` / `Qwen2.5-7B` (versions *base* et *Instruct*).
  - Famille 2 : `Llama-3.1-8B` (versions *base* et *Instruct*) ou `Mistral-7B-v0.3` / `Gemma-2-9B`.
- **Calcul nécessaire (`illustratif`) :**
  - Extraction et validation de $V_{\text{cible}}$ (`2 000` items $D_{\text{train}}$, `2` méthodes) : `2` à `4` heures sur `1` GPU A100 `80` Go par modèle.
  - Campagne complète par modèle (`10` doses $\alpha$ × `25` conditions incluant C1–C5 × `3 000` items appariés + natifs + distance croisée + calibration $\Delta \mathcal{L}_{\text{cal}}$ + sonde passive + $\Delta C_{\text{pert}}$) : `45` à `80` heures GPU A100 `80` Go en inférence batchée BF16 (`~4 × 10^7` tokens évalués par modèle).
  - Total sur `4` modèles (`2` familles × *base*/*instruct* ou `2` échelles) : **`200` à `350` heures GPU A100 `80` Go**, soit **`5 × 10^18` à `1,5 × 10^19` FLOPs** (`illustratif`).
- **Coût estimé (`illustratif`) :**
  - Location cloud (`1,5` à `2,5 $/h` GPU A100 `80` Go) : **`300` à `900 $`** pour la campagne multi-modèles complète (stockage des logits bruts $< 50 \$$).
  - **Version minimale de falsification rapide** (`1` modèle `~7–8B`, Expérience 1 + C1/C2/C5 + plan croisé distance × intégration) : `25` à `40` heures GPU, soit **`40` à `100 $`** (`illustratif`), exécutable sur une seule carte académique en `2` jours calendaires.

---

## Antériorité connue

### Ce qui a été lu directement dans cette session
- Aucun article primaire n'a été transmis. Seul le résumé figurant dans `FAITS` évoque deux ensembles de travaux de 2026 (directions d'activation dissociant des tâches ; doutes liés à l'absence de mécanismes d'éveil) : **références exactes à vérifier**, statut `RAPPORTÉ`.

### Ce dont je me souviens (mémoire d'entraînement, sans lecture directe du texte intégral dans cette session ; aucun identifiant arXiv cité de mémoire)

**Anesthésie générale, dissociation fonctionnelle et indices neurophysiologiques :**
- Alkire, M. T., Hudetz, A. G., & Tononi, G. (2008). *Consciousness and anesthesia*. Science.
- Brown, E. N., Lydic, R., & Schiff, N. D. (2010). *General anesthesia, sleep, and coma*. New England Journal of Medicine.
- Sanders, R. D., Tononi, G., Laureys, S., & Sleigh, J. W. (2012). *Unresponsiveness ≠ unconsciousness*. Anesthesiology.
- Purdon, P. L., et al. (2013). *Electroencephalogram signatures of loss and recovery of consciousness from propofol*. PNAS.
- Casali, A. G., et al. (2013). *A theoretically based index of consciousness independent of sensory processing and behavior*. Science Translational Medicine.
- Jeux publics bruts d'EEG/tâches comportementales sous titration de propofol (dépôts OpenNeuro / PhysioNet / études de connectivité sous propofol) : *références exactes à vérifier*.

**Théories de la conscience et conscience artificielle :**
- Lamme, V. A. F. (2006). *Towards a true neural stance on consciousness*. Trends in Cognitive Sciences.
- Lau, H., & Rosenthal, D. (2011). *Empirical support for higher-order theories of conscious awareness*. Trends in Cognitive Sciences.
- Tononi, G., Boly, M., Massimini, M., & Koch, C. (2016). *Integrated information theory: from consciousness to its physical substrate*. Nature Reviews Neuroscience.
- Dehaene, S., Lau, H., & Kouider, S. (2017). *What is consciousness, and could machines have it?* Science.
- Mashour, G. A., Roelfsema, P., Changeux, J.-P., & Dehaene, S. (2020). *Conscious processing and the global neuronal workspace hypothesis*. Neuron.
- Seth, A. K., & Bayne, T. (2022). *Theories of consciousness*. Nature Reviews Neuroscience.
- Butlin, P., et al. (2023). *Consciousness in artificial intelligence: Insights from the science of consciousness*.

**Interprétabilité mécaniste, directions d'activation et méthodologie :**
- Platt, J. R. (1964). *Strong inference*. Science.
- Olsson, C., et al. (2022). *In-context learning and induction heads*.
- Zou, A., et al. (2023). *Representation engineering: A top-down approach to AI transparency*.
- Arditi, A., et al. (2024). *Refusal in language models is mediated by a single direction*.

FIN-DE-CELLULE