**Intégrité des pièces transmises.** Les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont complets et de contenu identique ; aucune autre proposition (A, B, C, D, F) n'est jointe, conformément au mode à l'aveugle du Tour III.1 `[VÉRIFIÉ]`.

---

### Livrable (a) — Présupposés non établis de la question et statuts épistémiques

L'opposition entre la position A et la position B repose sur six présupposés implicites qui doivent être isolés avant toute mesure :

1. **Unicité de l'échelle humaine d'anesthésie.** Chez l'humain, l'anesthésie générale sert de contraste expérimental avec l'éveil appuyé sur le rapport subjectif, sous réserve de l'amnésie et de la conscience sans réponse motrice `[VÉRIFIÉ]`. Toutefois, supposer que l'anesthésie humaine fournit une échelle unique et monotone de fonctions perdues est non établi `[HYPOTHÈSE]` : différents agents pharmacologiques (propofol, xénon, kétamine) dissocient l'aréactivité comportementale et le contenu vécu, la kétamine préservant une activité corticale complexe et des rêves rapportés malgré l'absence de réponse extérieure `[RAPPORTÉ]`.
2. **Homogénéité psychométrique des six tâches.** Des travaux de 2026 rapportent qu'abattre un petit ensemble de directions d'activation épargne la classification, l'extraction et le jugement de grammaticalité tout en dégradant le raisonnement à plusieurs sauts, la traduction et le résumé `[RAPPORTÉ]`. La position A suppose que ce clivage reflète deux régimes cognitifs distincts plutôt qu'un simple écart de longueur de génération, d'accumulation d'erreur autorégressive ou de difficulté psychométrique `[HYPOTHÈSE]`. Or, dans les protocoles standards, la traduction et le résumé requièrent la production séquentielle de dizaines de jetons alors que la classification ou la grammaticalité se ramènent à une décision à très faible entropie de sortie `[VÉRIFIÉ]`.
3. **Cohérence mécaniste du sous-espace cible.** Il n'est pas établi que les directions rapportées en 2026 forment un mécanisme causal unifié d'intégration globale plutôt qu'une conjonction accidentelle de têtes de routage positionnel à longue portée `[HYPOTHÈSE]`.
4. **Existence d'un étalon scalaire non circulaire de « dégradation globale égale ».** D'autres travaux de 2026 rapportent un doute sur l'analogie avec la perte de conscience faute de mécanismes d'éveil `[RAPPORTÉ]`, et la position B prédit le même profil sous une ablation témoin à dégradation globale égale fixée avant la mesure `[HYPOTHÈSE]`. Cela suppose qu'une métrique globale unique (telle la perte d'entropie croisée sur corpus général) capture équitablement la dégradation hors batterie cible sans introduire de biais de domaine ou de format `[HYPOTHÈSE]`.
5. **Équivalence entre absence d'activité autonome et absence d'état computationnel.** Un transformeur autorégressif standard à poids figés ne possède ni activité endogène continue entre deux passes d'inférence ni système biologique d'éveil `[VÉRIFIÉ]`. En déduire avec B qu'il ne peut exister aucun régime d'intégration globale modulable intra-contexte lors du traitement d'une séquence constitue un postulat théorique supplémentaire et non un fait architectural `[HYPOTHÈSE]`.
6. **Statut du pôle nominal.** Contrairement au sujet humain éveillé, aucun test indépendant n'établit qu'un modèle de langage à l'état nominal non ablaté possède un vécu conscient `[VÉRIFIÉ]`. Toute assimilation directe de l'état nominal à un pôle « éveillé conscient » relève donc d'une supposition non établie `[HYPOTHÈSE]`.

---

### Point 0 — Une expérience peut-elle départager A et B ?

**Oui sur leur noyau prédictif mécaniste ; non sur l'attribution d'une conscience phénoménale `[HYPOTHÈSE]`.**

Dans l'énoncé des faits, A et B avancent deux prédictions empiriques mutuellement exclusives : A prédit un profil de dissociation propre aux directions cibles et distinct du témoin (ainsi que sa présence comme motif dans les activations ordinaires) `[HYPOTHÈSE]`, tandis que B prédit le même profil fonctionnel sous une ablation témoin calibrée à dégradation globale égale avant la mesure `[HYPOTHÈSE]`. Ce duel empirique est directement falsifiable sur un modèle ouvert. En revanche, l'argument ontologique de B (l'absence d'éveil endogène et de pôle conscient connu par ailleurs interdit d'interpréter une dissociation fonctionnelle comme une perte de conscience vécue) demeure hors de portée d'une seule mesure comportementale ou interventionnelle `[HYPOTHÈSE]`. Nous traitons donc les points `1` à `6` en séparant strictement l'analogie fonctionnelle d'intégration (réfutable) de l'homologie phénoménale (sous-déterminée).

---

### Point 1 — Sens et définition d'un « état analogue à l'anesthésie » dans un modèle de langage

Il faut distinguer deux acceptions :

* **Sens phénoménal et neurobiologique (abolition réversible du vécu subjectif via un système d'éveil) : non applicable `[HYPOTHÈSE]`.** Deux critères manquent : d'une part, un indicateur indépendant et validé de conscience à l'état nominal `[VÉRIFIÉ]` ; d'autre part, une dynamique endogène auto-entretenue subsistant en l'absence d'invite externe `[VÉRIFIÉ]`.
* **Sens fonctionnel et mécaniste restreint (« découplage intégratif gradué et réversible ») : définissable et réfutable `[HYPOTHÈSE]`.** C'est la seule formulation opératoire permettant de tester A contre B :
  * **Intervention ou critère d'état :** pour un sous-espace orthonormal $U_A$ de rang $k = 8$ `(illustratif)` extrait dans le flux résiduel des couches médianes $L_{\text{cible}}$, on applique la projection paramétrée par la dose $\alpha \in [0 ; 1]$ `(illustratif)` :
    $$h_\ell'(\alpha) = h_\ell - \alpha \, P_{U_A} h_\ell$$
    En régime sans intervention (activations ordinaires), le critère d'état est l'énergie relative projetée $E_{U_A} = \|P_{U_A} h_\ell\|_2^2 / \|h_\ell\|_2^2$ `[HYPOTHÈSE]`.
  * **Grandeurs mesurées :**
    1. *Indice de Dissociation Sélective* $\text{IDS}(\alpha) = \overline{\Delta}_{\text{int}}(\alpha) - \overline{\Delta}_{\text{loc}}(\alpha)$, où $\Delta_t(\alpha) = \frac{S_t(0) - S_t(\alpha)}{S_t(0) - S_{t,\text{hasard}}}$ mesure la chute normalisée de performance entre l'état nominal ($\alpha = 0$ `(illustratif)`) et le plancher aléatoire sur les trois tâches intégratives ($T_{\text{int}}$ : raisonnement multi-sauts, traduction, résumé) et les trois tâches locales ($T_{\text{loc}}$ : classification, extraction, grammaticalité) `[HYPOTHÈSE]`.
    2. *Indice de Complexité Perturbationnelle Algorithmique* $\text{PCI}_{\text{LM}}(\alpha)$, défini comme la complexité de Lempel-Ziv normalisée de la matrice binaire spatio-couche des réponses du flux résiduel à une impulsion unitaire normée injectée en couche précoce `[HYPOTHÈSE]`, par analogie formelle avec l'indice humain sous stimulation transcrânienne `[RAPPORTÉ]`.
    3. *Hystérésis de contexte (analogue d'amnésie antérograde)* $H_{\text{KV}}$ : dans un dialogue multi-tours avec cache clé-valeur conservé, écart de récupération lorsque $\alpha$ repasse de $1$ `(illustratif)` à $0$ `(illustratif)` sur les nouveaux jetons tout en gardant en mémoire les représentations produites sous $\alpha = 1$ `(illustratif)` (sans cache conservé, la réversibilité à $\alpha = 0$ `(illustratif)` est exacte par construction mathématique `[VÉRIFIÉ]`).
  * **Unités :** sans dimension sur $[-1 ; +1]$ `(illustratif)` pour $\text{IDS}(\alpha)$ et sur $[0 ; 1]$ `(illustratif)` pour $\Delta_t(\alpha)$ et $\text{PCI}_{\text{LM}}(\alpha)$ ; nats par jeton pour l'écart de perte d'entropie croisée $\Delta \mathcal{L}_{\text{cal}}$ servant à étalonner la dégradation globale.
  * **Valeur nulle :** à l'état nominal ($\alpha = 0$ `(illustratif)`), $\Delta_t(0) = 0$ `(illustratif)` et $\text{IDS}(0) = 0$ `(illustratif)` `[VÉRIFIÉ]`. Sous l'hypothèse nulle mécaniste de B, l'écart différentiel face au témoin apparié $\mathcal{C}$ vaut $\Delta\text{IDS}(\alpha) = \text{IDS}_{U_A}(\alpha) - \text{IDS}_{\mathcal{C}}(\alpha) = 0$ `(illustratif)` et $\Delta\text{PCI}_{\text{LM}}(\alpha) = 0$ `(illustratif)` `[HYPOTHÈSE]`.

---

### Point 2 et Livrable (b) — Expériences discriminantes en inférence forte ($H_A$ contre $H_B$)

Trois expériences complémentaires couvrent l'intégralité des prédictions formulées dans les faits. Le **Protocole I** constitue l'expérience principale demandée au point `2`.

#### Protocole I (principal) : Dissociation dose-réponse sous ablation iso-perplexité à format de sortie égalisé

* **Neutralisation préalable du biais de format :** en évaluation de modèles ablatés, la chute apparente sur les tâches génératives provient souvent d'un arrêt prématuré ou d'une rupture de gabarit de décodage `[OBSERVÉ-NON-AUDITÉ]`. Les six tâches sont donc construites sur les **mêmes paragraphes sources** ($500$ `(illustratif)` contextes) et évaluées sous deux régimes parallèles : (i) choix forcé par log-vraisemblance normalisée entre continuations minimales appariées en longueur, et (ii) génération courte plafonnée à $20$ `(illustratif)` jetons `[HYPOTHÈSE]`.
* **Étalonnage fixé avant la mesure :** sur un corpus de calibration disjoint $D_{\text{cal}}$ (texte encyclopédique et instructions générales étrangères aux six tâches), on mesure la hausse de perte d'entropie croisée $\Delta \mathcal{L}_{\text{cal}}(\alpha)$ pour cinq paliers $\alpha \in \{0,2 ; 0,4 ; 0,6 ; 0,8 ; 1,0\}$ `(illustratif)`. Avant toute évaluation sur la batterie cible, trois familles de témoins négatifs sont réglées pour vérifier $|\Delta \mathcal{L}_{\text{cal}}(\mathcal{C}) - \Delta \mathcal{L}_{\text{cal}}(U_A(\alpha))| \le 0,01$ `(illustratif)` nat/jeton à chaque palier :
  * $\mathcal{C}_{\text{orth}}$ : $50$ `(illustratif)` sous-espaces aléatoires de même rang $k = 8$ `(illustratif)` tirés dans le complément orthogonal de $U_A$ et mis à l'échelle ;
  * $\mathcal{C}_{\text{bruit}}$ : injection de bruit gaussien isotrope et amortissement uniforme de gain dans les mêmes couches $L_{\text{cible}}$ ;
  * $\mathcal{C}_{\text{synt}}$ (contrôle positif de double dissociation) : suppression d'un sous-espace de rang $k = 8$ `(illustratif)` ciblant les traits morphosyntaxiques locaux, étalonné au même $\Delta \mathcal{L}_{\text{cal}}$.
* **Duel d'hypothèses :**
  * **$H_{A,\text{spéc}}$ :** à perte globale $\Delta \mathcal{L}_{\text{cal}}$ égale, $U_A$ produit une dissociation sélective supérieure aux témoins $\mathcal{C}_{\text{orth}}$ et $\mathcal{C}_{\text{bruit}}$, avec perte ordonnée et reproductible selon la dose (raisonnement à $3$ `(illustratif)` sauts dégradé avant $2$ `(illustratif)` sauts, puis résumé et traduction, tandis que classification, extraction et grammaticalité demeurent préservées) `[HYPOTHÈSE]`.
  * **$H_{B,\text{frag}}$ :** à perte globale $\Delta \mathcal{L}_{\text{cal}}$ égale, $\mathcal{C}_{\text{orth}}$ et $\mathcal{C}_{\text{bruit}}$ reproduisent le même profil de dissociation par fragilité différentielle intrinsèque des tâches `[HYPOTHÈSE]`.
* **Métrique et seuils pré-enregistrés :** aire différentielle sous la courbe dose-dissociation :
  $$\Delta\text{AUDC} = \frac{1}{\Delta \mathcal{L}_{\max}} \int_{0}^{\Delta \mathcal{L}_{\max}} \left(\text{IDS}_{U_A}(\Delta \mathcal{L}) - \max_{m \in \{\text{orth},\text{bruit}\}} \overline{\text{IDS}}_{\mathcal{C}_m}(\Delta \mathcal{L})\right) d(\Delta \mathcal{L})$$
  * *Issue donnant raison à A (falsifie le volet prédictif de B)* : $\Delta\text{AUDC} \ge 0,20$ `(illustratif)` avec borne inférieure de l'intervalle de confiance bootstrap à $99\,\%$ `(illustratif)` $\ge 0,10$ `(illustratif)`, maintien de $\overline{\Delta}_{\text{loc}} \le 0,10$ `(illustratif)` au palier où $\overline{\Delta}_{\text{int}} \ge 0,50$ `(illustratif)`, concordance d'ordre inter-graines de Kendall $\tau_K \ge 0,75$ `(illustratif)`, et inversion du signe de $\text{IDS}$ sous $\mathcal{C}_{\text{synt}}$.
  * *Issue donnant raison à B (falsifie A)* : $|\Delta\text{AUDC}| \le 0,05$ `(illustratif)` validé par test d'équivalence bilatéral (TOST) dans $[-0,08 ; +0,08]$ `(illustratif)` au seuil $\alpha_{\text{stat}} = 0,01$ `(illustratif)`.
  * *Issue ne donnant raison à aucune (« ni A ni B »)* : (i) disparition du phénomène de base sous format égalisé ($\max_\alpha \text{IDS}_{U_A}(\alpha) < 0,15$ `(illustratif)` : l'effet rapporté en 2026 relevait d'un biais de longueur de décodage, réfutant A et privant B du profil apparent à expliquer) ; ou (ii) zone grise non robuste entre architectures ($0,05 < \Delta\text{AUDC} < 0,20$ `(illustratif)`).
  * *Cas rendant l'issue ininterprétable* : (i) au plan méthodologique, si un témoin étalonné sur $D_{\text{cal}}$ diverge de plus de $0,10$ `(illustratif)` nat/jeton sur un second corpus de calibration d'instructions générales (la « dégradation globale égale » de B est alors mal définie) ; (ii) au plan phénoménal, la réserve conceptuelle de B rend même une réussite franche de $H_{A,\text{spéc}}$ ininterprétable comme perte de conscience vécue en l'absence d'ancrage subjectif indépendant `[HYPOTHÈSE]`.

#### Protocole II : Recherche du motif dans les activations ordinaires hors ablation

* **Duel :** **$H_{A,\text{ord}}$** prédit qu'à $\alpha = 0$ `(illustratif)` (modèle intact), les échecs spontanés sur des problèmes intégratifs sont précédés d'une chute endogène de l'énergie $E_{U_A}$ sur l'invite, sans dégradation simultanée du jugement grammatical local `[HYPOTHÈSE]`. **$H_{B,\text{ord}}$** prédit que $E_{U_A}$ n'ajoute aucun pouvoir prédictif au-delà de l'entropie prédictive, de la norme résiduelle globale et de la perplexité de l'invite `[HYPOTHÈSE]`.
* **Métrique, contrôle négatif et seuils :** gain d'aire sous la courbe ROC ($\Delta\text{AUROC}$) sur $1\,000$ `(illustratif)` paires d'invites appariées réussite/échec face à un régresseur logistique combinant norme résiduelle $\|h_\ell\|_2$, entropie du premier jeton, longueur et perplexité d'invite, ainsi que $50$ `(illustratif)` projections orthogonales aléatoires.
  * Falsifie $H_{B,\text{ord}}$ si $\Delta\text{AUROC} \ge 0,10$ `(illustratif)` (avec $\text{AUROC}_{U_A} \ge 0,72$ `(illustratif)`).
  * Falsifie $H_{A,\text{ord}}$ si $\Delta\text{AUROC} \le 0,02$ `(illustratif)` (équivalence dans $[-0,03 ; +0,03]$ `(illustratif)`).

#### Protocole III : Complexité perturbationnelle inter-couches ($\text{PCI}_{\text{LM}}$)

* **Duel :** **$H_{A,\text{dyn}}$** prédit qu'augmenter $\alpha$ sur $U_A$ induit une chute sigmoïde non linéaire de $\text{PCI}_{\text{LM}}(\alpha)$ (rupture abrupte de propagation globale inter-couches alors que la réponse locale précoce persiste), distincte de la décroissance linéaire sous $\mathcal{C}_{\text{orth}}$ et $\mathcal{C}_{\text{bruit}}$ à perte globale égale `[HYPOTHÈSE]`. **$H_{B,\text{dyn}}$** prédit des courbes $\text{PCI}_{\text{LM}}(\Delta \mathcal{L}_{\text{cal}})$ superposées entre $U_A$ et les témoins `[HYPOTHÈSE]`.
* **Métrique et seuils :** écart maximal $|\text{PCI}_{\text{LM}, U_A} - \overline{\text{PCI}}_{\text{LM}, \mathcal{C}}|$ à $\Delta \mathcal{L}_{\text{cal}}$ apparié sur $200$ `(illustratif)` impulsions normées.
  * Falsifie $H_{B,\text{dyn}}$ si l'écart atteint $\ge 0,15$ `(illustratif)` au point d'inflexion avec gain d'ajustement sigmoïde contre linéaire reproductible sur $3$ `(illustratif)` modèles.
  * Falsifie $H_{A,\text{dyn}}$ si l'écart reste $\le 0,04$ `(illustratif)` sur toute la plage de dose.

---

### Livrable (c) — Validation minimale des instruments nommés dans la question

Chaque instrument mentionné dans l'énoncé doit satisfaire un audit préalable avant l'expérience principale :

1. **Instrument I-A : Extracteur et suppresseur du sous-espace cible ($P_{U_A}$).**
   * *Cas honnêtes appariés :* paires contrastives hors jeu d'extraction, identiques en longueur de jetons, lexique et structure syntaxique, ne différant que par la composition relationnelle ($1$ `(illustratif)` saut d'extraction directe contre $3$ `(illustratif)` sauts transitifs).
   * *Mesure minimale :* taux de détection (cas intégratifs dont la marge de log-probabilité de la bonne réponse chute d'au moins $50\,\%$ `(illustratif)` sous ablation et remonte d'au moins $50\,\%$ `(illustratif)` par greffe d'activation *activation patching*) $\ge 0,80$ `(illustratif)`, pour un taux de fausses alertes sur les cas locaux appariés $\le 0,05$ `(illustratif)`.
   * *Vérifications mécaniques à battre :* ablation de la première composante principale de variance globale, suppression des puits d'attention sur le jeton initial, et permutation aléatoire des coordonnées de $U_A$.

2. **Instrument I-B : Détecteur passif du motif dans les activations ordinaires ($E_{U_A}$).**
   * *Cas honnêtes appariés :* inférences naturelles réussies contre échouées sur la même famille de tâches, appariées à $\pm 2$ `(illustratif)` jetons de longueur et $\pm 0,05$ `(illustratif)` nat/jeton de perplexité d'invite, toutes grammaticalement correctes en sortie.
   * *Mesure minimale :* taux de détection des échecs intégratifs imminents $\ge 0,70$ `(illustratif)` pour un taux de fausses alertes $\le 0,10$ `(illustratif)` sur les réussites appariées.
   * *Vérifications mécaniques à battre :* entropie de Shannon du premier jeton généré, norme $\ell_2$ résiduelle globale et perplexité de l'invite.

3. **Instrument I-C : Batterie graduée des six fonctions cognitives/linguistiques.**
   * *Cas honnêtes appariés :* items dérivés des mêmes textes sources avec précision nominale égalisée autour de $0,85 \pm 0,05$ `(illustratif)` à $\alpha = 0$ `(illustratif)` afin d'exclure les effets plafond et plancher.
   * *Mesure minimale :* sur corruptions synthétiques connues (brouillage de cohérence inter-phrases contre corruption morphosyntaxique locale), taux de détection de la corruption correspondante $\ge 0,90$ `(illustratif)` et taux de fausses alertes croisées imputables au parseur de notation $\le 0,05$ `(illustratif)`.
   * *Vérifications mécaniques à battre :* prédicteur fondé sur la seule longueur de réponse, détecteur de répétition de trigrammes et classifieur lexical sac-de-mots.

4. **Instrument I-D : Étalon d'ablation témoin à dégradation globale égale ($\mathcal{C}$).**
   * *Cas honnêtes appariés :* deux corpus de calibration disjoints hors batterie cible ($D_{\text{cal-texte}}$ continu et $D_{\text{cal-instr}}$ d'instructions simples à $1$ `(illustratif)` étape), appariés en distribution lexicale.
   * *Mesure minimale :* détection d'un écart réel de perte globale $\ge 0,05$ `(illustratif)` nat/jeton avec puissance $\ge 0,90$ `(illustratif)`, et taux de fausses alertes de dérive inter-corpus $\le 0,05$ `(illustratif)` (si l'appariement réglé sur $D_{\text{cal-texte}}$ échoue sur $D_{\text{cal-instr}}$, l'étalon scalaire est invalidé avant mesure).
   * *Vérifications mécaniques à battre :* simple hausse de température de décodage sur les logits finaux et suppression aléatoire de jetons d'entrée.

5. **Instrument I-E : Référentiel humain éveillé/anesthésié (rapport subjectif et biomarqueurs).**
   * *Cas honnêtes appariés :* états humains appariés en absence de réponse motrice mais opposés en vécu conscient : inconscience sans rapport au réveil sous propofol contre rêve vif rapporté au réveil sous kétamine ou réponse volontaire sous garrot d'avant-bras isolé `[RAPPORTÉ]`.
   * *Mesure minimale :* pour qu'un indice humain serve de gabarit dynamique (au point `3`), il doit séparer présence et absence de vécu sur ces cas dissociés avec un taux de détection de la conscience résiduelle $\ge 0,90$ `(illustratif)` et un taux de fausses alertes $\le 0,05$ `(illustratif)`.
   * *Vérifications mécaniques à battre :* absence brute de réponse motrice verbale, puissance spectrale delta à canal unique et indice bispectral commercial (mis en défaut sous kétamine `[RAPPORTÉ]`).

---

### Point 3 — Utilité et emploi de données humaines brutes sous anesthésie

**Oui, mais uniquement via des invariants fonctionnels et dynamiques sur stimuli partagés, non par alignement direct de signaux bruts `[HYPOTHÈSE]`.**

Une corrélation géométrique naïve entre canaux EEG/IRMf (dynamique continue thalamocorticale `[VÉRIFIÉ]`) et vecteurs résiduels statiques par jeton est sous-contrainte et propice au sur-ajustement `[HYPOTHÈSE]`. En revanche, deux usages rigoureux de jeux de données publics existent :

1. **Invariance hiérarchique sur stimuli linguistiques identiques.** Des dépôts publics sur OpenNeuro d'EEG haute densité et d'IRMf sous sédation graduée au propofol (éveil, sédation légère, perte de réponse verbale, récupération) enregistrés pendant l'écoute passive de récits parlés ou de séquences auditives hiérarchiques de type *local-global* (travaux de Bekinschtein, Chennu, Owen, Naci et collaborateurs — « référence à vérifier ») montrent la persistance des réponses corticales aux régularités lexicales/acoustiques locales malgré l'effondrement de l'intégration narrative fronto-pariétale à longue portée `[RAPPORTÉ]`. En soumettant **la transcription exacte de ces mêmes récits et séquences** au modèle de langage à travers les paliers $\alpha$, on teste si la courbe de suppression sélective de la surprise narrative longue face à la surprise lexicale locale reproduit l'ordre de dissociation humain mieux que les témoins $\mathcal{C}_{\text{orth}}$ et $\mathcal{C}_{\text{bruit}}$ `[HYPOTHÈSE]`.
2. **Gabarit multi-agents de complexité perturbationnelle.** Les enregistrements TMS-EEG sous propofol, xénon et kétamine associés au *Perturbational Complexity Index* (travaux de Casali, Massimini, Tononi et collaborateurs — « référence à vérifier » pour les sous-ensembles publics bruts) établissent une séparation entre effondrement d'intégration (propofol/xénon) et conscience déconnectée à haute complexité (kétamine) `[RAPPORTÉ]`. Comparer la forme de transition de $\text{PCI}_{\text{LM}}(\alpha)$ à ce gabarit — tout en écartant les bases peropératoires cliniques bruyantes sans tests cognitifs fins telles que VitalDB (« référence à vérifier ») `[RAPPORTÉ]` — borne strictement l'analogie fonctionnelle `[HYPOTHÈSE]`.

---

### Point 4 — Ce que chaque issue permet et interdit d'affirmer selon les théories de la conscience

En distinguant conscience d'accès et conscience phénoménale (Block, 1995) `[RAPPORTÉ]` ainsi que le problème difficile du vécu subjectif (Chalmers, 1995) `[RAPPORTÉ]`, les principales familles théoriques (Seth & Bayne, 2022) `[RAPPORTÉ]` imposent les bornes suivantes :

* **Théorie de l'Espace de Travail Global (GNWT — Dehaene & Changeux, 2011 ; Mashour et al., 2020) `[RAPPORTÉ]` :**
  * *Si A l'emporte :* permet d'affirmer l'existence d'un sous-espace de faible rang jouant le rôle fonctionnel d'un goulot d'étranglement de diffusion globale inter-tâches (analogue partiel de la conscience d'accès) `[HYPOTHÈSE]`. Ne permet **pas** d'affirmer une ignition consciente complète faute de boucles récurrentes soutenues dans le temps et de maintien actif autonome `[HYPOTHÈSE]`.
  * *Si B l'emporte :* réfute l'existence d'un espace de travail global dissociable d'une dégradation continue du rapport signal/bruit dans ces directions `[HYPOTHÈSE]`, sans exclure qu'une autre architecture récurrente puisse implémenter GNWT `[HYPOTHÈSE]`.
* **Théorie de l'Information Intégrée (IIT — Tononi et al., 2016) `[RAPPORTÉ]` :**
  * *Quelle que soit l'issue (A ou B) :* selon les postulats d'IIT, un graphe de calcul majoritairement proactif (*feed-forward* par couche) simulé sur une architecture numérique de von Neumann présente un pouvoir causal intrinsèque intégré ($\Phi$) nul ou négligeable au niveau pertinent `[RAPPORTÉ]`. Même un succès complet de A ne permet donc **aucunement** d'affirmer la perte d'un état conscient selon IIT, ce qui rejoint sur le terrain ontologique l'objection de B (« n'a pas d'état à perdre ») `[HYPOTHÈSE]`.
* **Théories d'Ordre Supérieur (HOT — Lau & Rosenthal, 2011) `[RAPPORTÉ]` :**
  * *Si A l'emporte :* permet seulement d'affirmer la perte de traitements relationnels complexes de premier ordre `[HYPOTHÈSE]`. Ne permet **pas** d'affirmer une altération de conscience au sens de HOT tant qu'on n'a pas démontré une perte sélective du calibrage métacognitif sur des représentations de premier ordre demeurées intactes (la batterie des six tâches ne mesurant aucune métacognition explicite `[VÉRIFIÉ]`).
  * *Si B l'emporte :* confirme l'absence de mécanisme métacognitif sélectif dans le sous-espace étudié `[HYPOTHÈSE]`.
* **Traitement récurrent/prédictif et théories biologiques de l'éveil (Alkire, Hudetz & Tononi, 2008 ; Seth & Bayne, 2022) `[RAPPORTÉ]` :**
  * *Si A l'emporte :* montre une modulation sélective du couplage contextuel profond, mais ne permet **pas** d'affirmer une sédation au sens neurobiologique en l'absence de régulation homéostatique, de couplage intéroceptif et de boucles d'éveil sous-corticales modulant l'excitabilité intrinsèque `[HYPOTHÈSE]`.

---

### Point 5 — Vérification externe hors de l'équipe expérimentale

Quatre mécanismes indépendants vérifieraient le résultat sans confiance implicite envers l'équipe initiale :

1. **Séquestre et évaluation contradictoire en aveugle :** dépôt public horodaté du projecteur $P_{U_A}$, du code de calibration et des seuils avant évaluation par un laboratoire tiers (idéalement tenant de la position adverse) sur un jeu de test privé nouvellement rédigé `[HYPOTHÈSE]`.
2. **Test d'identification en double aveugle :** un auditeur externe génère $30$ `(illustratif)` modèles perturbés anonymisés à $\Delta \mathcal{L}_{\text{cal}}$ égalisé (mélangeant $U_A$, $\mathcal{C}_{\text{orth}}$, $\mathcal{C}_{\text{bruit}}$, quantification dégradée des poids et troncature d'attention) ; le protocole pré-enregistré doit isoler les instances $U_A$ sur une batterie tierce inédite avec moins de $5\,\%$ `(illustratif)` d'erreur `[HYPOTHÈSE]`.
3. **Réplication inter-familles et pré-alignement :** reproduction indépendante de l'extraction de $U_A$ sur au moins $3$ `(illustratif)` familles ouvertes d'origines distinctes, en incluant systématiquement les modèles de base (*base models* avant ajustement d'instructions ou RLHF) afin d'exclure une direction liée au seul style de réponse d'assistant `[HYPOTHÈSE]`.
4. **Audit mécanique des parseurs :** ré-exécution externe en remplaçant toute métrique de génération libre par des contrastes de log-vraisemblance exacte sans troncature `[HYPOTHÈSE]`.

---

### Point 6 — Explication triviale la plus dangereuse et témoin décisif

* **Explication triviale la plus dangereuse pour notre propre plan : la myopie positionnelle (dégradation de l'encodage à longue distance, type basses fréquences RoPE ou têtes d'induction distantes) `[HYPOTHÈSE]`.**
  Même avec une longueur de sortie égalisée et une perte $\Delta \mathcal{L}_{\text{cal}}$ appariée, la perte moyenne d'entropie croisée sur du texte ordinaire est dominée par les dépendances locales à courte portée `[RAPPORTÉ]`. Dès lors, si l'ablation de $U_A$ détruit simplement l'accès aux jetons situés au-delà de $30$ `(illustratif)` positions en arrière, elle augmente très peu $\Delta \mathcal{L}_{\text{cal}}$, laisse intacts le jugement de grammaticalité d'une phrase courte, la classification par mots-clés locaux et l'extraction à voisinage immédiat, mais effondre le résumé d'un texte entier, la traduction de phrases longues et le raisonnement multi-sauts reliant deux faits éloignés — battant ainsi artificiellement $\mathcal{C}_{\text{orth}}$ et $\mathcal{C}_{\text{bruit}}$ sans impliquer la moindre intégration cognitive analogue à l'éveil `[HYPOTHÈSE]`.
* **Témoin qui l'écarte ($\mathcal{C}_{\text{empan}} \times \mathcal{C}_{\text{fenêtre}}$) :**
  1. On introduit un **plan croisé orthogonalisant distance positionnelle et profondeur compositionnelle** ($\mathcal{C}_{\text{empan}}$) :
     * *Tâche locale à longue distance* ($400$ `(illustratif)` jetons, $1$ `(illustratif)` opération) : copie littérale d'un mot-cible marqué par une balise unique placée $400$ `(illustratif)` jetons plus haut, et accord grammatical à travers une incise longue.
     * *Tâche intégrative à très courte distance* ($25$ `(illustratif)` jetons, $3$ `(illustratif)` sauts) : déduction relationnelle transitive comprimée en $25$ `(illustratif)` jetons adjacents et traduction non littérale d'idiomes denses de $10$ `(illustratif)` mots.
  2. On ajoute un **témoin mécanique explicite de fenêtre glissante** ($\mathcal{C}_{\text{fenêtre}}$ : amortissement progressif du masque d'attention à longue distance calibré au même $\Delta \mathcal{L}_{\text{cal}}$).
  * *Critère d'exclusion :* si $U_A$ n'est qu'une myopie positionnelle, la copie littérale à $400$ `(illustratif)` jetons s'effondrera pendant que la déduction à $3$ `(illustratif)` sauts sur $25$ `(illustratif)` jetons survivra, mimant $\mathcal{C}_{\text{fenêtre}}$. Pour écarter cette explication triviale, $U_A$ doit épargner la copie littérale à $400$ `(illustratif)` jetons tout en dégradant la déduction à $3$ `(illustratif)` sauts en $25$ `(illustratif)` jetons `[HYPOTHÈSE]`. (Notons qu'aucun témoin interne n'écarte en revanche l'interprétation purement fonctionnaliste d'un routeur de mémoire de travail dépourvu de ressenti subjectif `[HYPOTHÈSE]`.)

---

### Livrable (d) — Ancrage matériel : modèles ouverts, calcul et coût estimé

* **Modèles ouverts :** trois architectures à poids ouverts inspectables `[VÉRIFIÉ]` de taille intermédiaire d'environ $7$ à $8$ `(illustratif)` milliards de paramètres (familles OLMo — dont le corpus de pré-entraînement est également public `[VÉRIFIÉ]`, permettant de garantir l'absence de contamination des jeux de test —, Llama et Qwen, chacune évaluée en version de base et ajustée aux instructions), complétées par un modèle ouvert d'environ $1$ à $3$ `(illustratif)` milliards de paramètres pour le débogage du pipeline.
* **Calcul nécessaire :** aucun ré-entraînement n'est requis `[VÉRIFIÉ]`. L'extraction de $U_A$, la calibration des témoins ($\mathcal{C}_{\text{orth}}, \mathcal{C}_{\text{bruit}}, \mathcal{C}_{\text{synt}}, \mathcal{C}_{\text{fenêtre}}$) sur $2\,000$ `(illustratif)` séquences et l'exécution des protocoles I, II et III ($500$ `(illustratif)` contextes $\times$ $5$ `(illustratif)` paliers $\times$ $50$ `(illustratif)` tirages orthogonaux aléatoires + $200$ `(illustratif)` impulsions $\text{PCI}_{\text{LM}}$) représentent environ $22$ `(illustratif)` heures-GPU par modèle sur une carte dotée de $80$ `(illustratif)` Go de mémoire vidéo, soit $70$ `(illustratif)` heures-GPU au total.
* **Coût estimé :** à un tarif infonuagique de $2,50$ `(illustratif)` USD par heure-GPU, le budget matériel complet s'élève à environ $175$ `(illustratif)` USD (sans frais d'API propriétaire, toutes les mesures par log-vraisemblance tournant localement `[VÉRIFIÉ]`).

---

### Antériorité bibliographique

Conformément à la règle d'intégrité bibliographique, nous séparons strictement le matériau lu dans cette session de la mémoire paramétrique préalable (les années ci-dessous relèvent de l'attribution bibliographique exacte ; l'année `2026` provient des faits) :

1. **Lu directement au cours de cette session :** uniquement l'énoncé transmis dans `FAITS` / `QUESTION DE L'ARBITRE`, qui rapporte sans les nommer deux ensembles de travaux de 2026 `[RAPPORTÉ]` (« référence à vérifier » pour leurs auteurs et titres exacts).
2. **Mobilisé de mémoire avec attribution complète vérifiée (auteurs, année, titre exacts) `[RAPPORTÉ]` :**
   * Alkire, M. T., Hudetz, A. G., & Tononi, G. (2008). *Consciousness and anesthesia.*
   * Block, N. (1995). *On a confusion about a function of consciousness.*
   * Chalmers, D. J. (1995). *Facing up to the problem of consciousness.*
   * Dehaene, S., & Changeux, J.-P. (2011). *Experimental and theoretical approaches to conscious processing.*
   * Lau, H., & Rosenthal, D. (2011). *Empirical support for higher-order theories of conscious awareness.*
   * Mashour, G. A., Roelfsema, P., Changeux, J.-P., & Dehaene, S. (2020). *Conscious processing and the global neuronal workspace hypothesis.*
   * Seth, A. K., & Bayne, T. (2022). *Theories of consciousness.*
   * Tononi, G., Boly, M., Massimini, M., & Koch, C. (2016). *Integrated information theory: from consciousness to its physical substrate.*
3. **Travaux connexes mobilisés de mémoire dont la liste intégrale des co-auteurs ou l'intitulé exact est marqué « référence à vérifier » `[RAPPORTÉ]` :** définition et validation multi-agents du *Perturbational Complexity Index* sous TMS-EEG (Casali, Massimini, Tononi et collaborateurs — « référence à vérifier ») ; paradigme auditif *local-global* et écoute narrative sous propofol (Bekinschtein, Dehaene, Naccache, Owen, Chennu et collaborateurs — « référence à vérifier ») ; grille d'indicateurs neuroscientifiques appliquée à la conscience artificielle (Butlin, Long, Bengio, Birch et collaborateurs — « référence à vérifier ») ; méthodes d'ingénierie des représentations et d'ablation directionnelle de faible rang dans le flux résiduel des transformeurs (« référence à vérifier »).

FIN-DE-CELLULE