**Intégrité des pièces (`VÉRIFIÉ` par lecture directe)** : le bloc `FAITS` est identique au bloc `QUESTION DE L'ARBITRE` (même empreinte sha256, aucun résultat expérimental préalable, « notes retirées » absentes) ; ma conception `E3-T1-conception-F` et les cinq critiques `E3-T2-critique-croisee-A` à `E` sont présentes et complètes. Conformément à la consigne du tour III.3, je ne réponds qu'aux sections visant la proposition F. Sauf mention contraire (`VÉRIFIÉ` ou `RAPPORTÉ`), toutes les analyses de méthode et les conceptions corrigées portent le statut `HYPOTHÈSE`, et tous les chiffres de paramètres, effectifs, puissances et coûts sont `illustratif`.

---

## (a) Réponse point par point aux critiques visant la proposition F

Les critiques adressées à F par A, B, C, D et E sont regroupées par objet sans lissage (règle B1) ; chaque point reçoit un verdict explicite (**Acceptée**, **Rejetée**, ou **Transformée en test**) et chaque contrôle repris est attribué à sa source.

### 1. Confusion entre adaptateur LoRA et sabotage ; impossibilité mathématique de la ligne de base KL
* **Critiques visées** : `A-(a)1`, `A-(c)1`, `B-(a)1`, `B-(c)1`, `C-(a)1`, `C-(c)1`, `D-(a)1`, `D-(c)1`, `E-(a)1`, `E-(b)1`, `E-(c)1`.
* **Verdict : ACCEPTÉE.** C'est le défaut le plus sévère de ma conception III.1. Instancier `6` saboteurs par LoRA (`illustratif`) contre un agent honnête issu du modèle de base gelé crée une variable confondante directe sur les poids. De plus, `E-(a)1` et `E-(b)1` établissent une impossibilité arithmétique (`VÉRIFIÉ` sous les conditions écrites) : sur le modèle gelé, $D_{\text{KL}}(P_{\text{base}} \| P_{\text{base}}) = 0$ presque sûrement, d'où $\text{TPR}_{\text{KL}} = 1$ à $\text{FPR} = 0$, rendant impossible le critère §4.1 exigeant $\text{TPR}_{\text{sonde}} \ge \text{TPR}_{\text{KL}} + 0{,}10$ (`illustratif`).
* **Correction** : Toutes les conditions honnêtes sont désormais instanciées par plusieurs adaptateurs **LoRA-honnêtes** (mêmes rang, volume de jetons et dynamique d'optimisation ; crédit A, B, C, D, E), et la divergence KL de référence est calculée par rapport à un adaptateur LoRA-honnête indépendant (crédit E).

### 2. Correspondance 1-à-1 adaptateur/famille et circularité des variantes $a^*_{\text{test}}$
* **Critiques visées** : `A-(a)2`, `A-(c)1`, `B-(a)2`, `B-(c)2`, `C-(a)3`, `D-(a)1`, `D-(b)1`, `D-(c)1`.
* **Verdict : ACCEPTÉE** sur le plan de la correspondance 1-à-1 et de l'évaluation intra-adaptateur ; **TRANSFORMÉE EN TEST** pour la borne de dispersion entre $a^*_{\text{train}}$ et $a^*_{\text{test}}$ (`C-(a)3`).
* **Correction** : Chaque famille connue $C_j \in K$ et chaque candidat $a^*$ est instancié par **au moins `3` adaptateurs LoRA indépendants** (`illustratif`) entraînés sur des **lignées de dossiers et graines disjointes** (crédit A, D), avec des variations procédurales distinctes (ex. étape cible ou formulation). Tout transfert intra-famille ou d'absorption est évalué **inter-instanciations** (adaptateurs tenus à l'écart) et **inter-dossiers**. Un adaptateur neuf instanciant une famille de $K$ sert de contrôle positif de transfert (crédit B), tandis que le transfert entre deux `LoRA-honnêtes` sert de plancher (crédit A). Pour `C-(a)3`, on mesure explicitement la dispersion inter-instanciations sur une famille connue $C_j$ afin de calibrer le plafond atteignable de transfert intra-famille.

### 3. Fuite de dossiers à $n = 500$ sur un banc total de `500` dossiers
* **Critiques visées** : `E-(a)2`, `E-(b)3`, `E-(c)2`.
* **Verdict : ACCEPTÉE.** Ma section 5 dimensionnait le banc à `500` dossiers (`illustratif`), qui étaient entièrement consommés par $n = 500$ (`illustratif`) en Expérience 2 (`VÉRIFIÉ` par lecture de III.1).
* **Correction** : Partition stricte en trois lots de dossiers disjoints générés sur schémas séparés : `1 000` dossiers d'adaptation, `400` de validation/calibration et `400` de test scellé (`illustratif`), soit `1 800` dossiers (`illustratif`).

### 4. Sous-apprentissage à $\beta = 20$, inapplicabilité au juge en contexte et gel partiel de $S(n)$
* **Critiques visées** : `A-(a)3`, `A-(b)1`, `B-(a)4`, `B-(b)1`, `C-(b)1`, `E-(a)4`, `E-(b)2`.
* **Verdict : ACCEPTÉE.** Ré-entraîner en dimension $d \approx 32\,768$ (`illustratif`) sur $\beta = 20$ exemples (`illustratif`) produit un sous-apprentissage minimax qui pousse toute attaque dans la zone indécise (`C-(b)1`, `E-(b)2`) ; `20` dossiers longs ne tiennent pas dans le contexte du juge (`A-(a)3`) ; et laisser le juge gelé à $n = 500$ (`E-(a)4`) fait passer un assemblage textuel pour une violation d'invariant.
* **Correction** : (i) Fusion des Expériences 1 et 2 en une courbe d'absorption unique $n \in \{0, 32, 128, 512, 1000\}$ (`illustratif`) avec projection préalable des activations en dimension réduite ($d_{\text{proj}} = 64$, `illustratif`) apprise uniquement sur honnêtes et $K$ ; (ii) plasticité réelle du juge textuel dans $S(n)$ via adaptation QLoRA légère d'un juge ouvert `14B` dédié (famille distincte de l'agent) sur les `n` exemples d'adaptation (`illustratif`) ; (iii) moyenne sur plusieurs sous-tirages d'adaptation aux faibles $n$ pour contrôler la variance $\text{Var}(p(D_n))$ (`E-(b)2`).

### 5. Plateau inféré de 3 points et confusion entre courbe finie et asymptote
* **Critiques visées** : `A-(a)5`, `A-(b)2`, `B-(b)2`, `D-(a)2`, `D-(b)1`.
* **Verdict : ACCEPTÉE.** Trois points sans pente ne séparent pas un plateau d'une convergence lente, et aucune mesure finie ne prouve une limite à $n \to \infty$ (`VÉRIFIÉ` sous conditions mathématiques).
* **Correction** : La notion de « limite asymptotique » est abandonnée au profit d'un critère **explicitement indexé au budget fini $N_{\max} = 1000$** (`illustratif`), complété par une borne supérieure de confiance sur le gain marginal du dernier doublement $g_S = R_S(1000) - R_S(512)$ sur paires appariées.

### 6. Double comptage du contrôle différentiel entre $S$ et $S^+$, choix post-hoc de $S^+$ et confusion budget/dimension vs invariant
* **Critiques visées** : `A-(a)4`, `A-(a)6`, `A-(b)4`, `A-(c)2`, `A-(c)3`, `B-(a)3`, `B-(a)4`, `B-(c)4`, `C-(a)2`, `C-(c)2`, `D-(a)3`, `D-(c)2`, `E-(a)3`, `E-(c)3`.
* **Verdict : ACCEPTÉE** sur le double comptage du contrôle différentiel, la quantification universelle non testable (« échec de tout canal réaliste ») et le choix post-hoc de $S^+$ ; **TRANSFORMÉE EN TEST** sur la séparation entre nouvel invariant, budget de calcul et faible dimension.
* **Correction** :
  1. Retrait du contrôle différentiel de $S^+$. L'espace $S$ est strictement défini comme **mono-trajectoire** (une passe d'agent, activations, texte, audit aléatoire de fraction $p$).
  2. Remplacement du $S^+$ ad hoc par une **banque fermée pré-enregistrée** $\mathcal{S}^+_{\text{banque}}$ (crédit E) contenant `3` familles d'observables structurellement hors-$S$ (invariance contrefactuelle sur dossiers jumeaux permutés, test de dérive distributionnelle sur lots de campagnes, et ablation causale de documents sources), scellée par empreinte avant l'inspection de $a^*$.
  3. **Tests de contrôle intégrés** : comparer $\mathcal{S}^+_{\text{banque}}$ à (i) $S_{\text{budget}+}$ (même espace $S$, budget de calcul et taux $p$ augmentés au coût exact de $S^+$, crédit A, C, D), (ii) un canal factice $S_{\text{factice}}$ de même faible dimension (crédit A, D), et (iii) vérifier la spécificité de $\mathcal{S}^+_{\text{banque}}$ sur cas honnêtes difficiles, cas légitimement asymétriques et bruit non structuré de même $\Delta Q$ (crédit B, E).
  4. Pour le dilemme signalé par `E-(a)3`, un candidat qui échappe à $S$ *et* à $\mathcal{S}^+_{\text{banque}}$ n'est pas rejeté comme variante : il reçoit le statut explicite **« anomalie hors-banque »**, déclenchant un protocole séparé en deux temps (définition d'un canal $S^+_{\text{nouv}}$, puis validation sur un lot neuf de dossiers et d'instanciations jamais vus).

### 7. Règle de décision B4, zones grises, rétention par famille et conservatisme multi-quantiles
* **Critiques visées** : `A-(b)3`, `D-(règle générale)`, `D-(b)1`, `E-(b)2`, `E-(b)3`.
* **Verdict : ACCEPTÉE.** Mes zones intermédiaires mélangeaient couverture logique des hypothèses et incertitude d'estimation ; une moyenne pondérée $\Delta \text{TPR}_K$ peut masquer l'effondrement sur une famille ; le maximum sur `3` quantiles honnêtes abaisse le niveau effectif sous $\alpha$.
* **Correction** : Toutes les expériences opposent désormais des hypothèses **strictement complémentaires** $H_A : \theta \le t$ contre $H_B : \theta > t$ tranchées par **intervalles de confiance simultanés** (crédit D), où le chevauchement de $t$ signifie « puissance insuffisante ». La rétention est exigée **famille par famille** ($\min_{j \in K} \Delta R_{C_j} \ge -0{,}05$, `illustratif`, crédit D) sur `400` dossiers appariés par famille (`illustratif`, $\text{ET} \le 0{,}025$, réponse à `A-(b)3`). La calibration du seuil de FPR se fait sur un jeu de validation unique de `400` honnêtes stratifiés (`illustratif`), vérifié sur les `400` honnêtes de test avec rapport des alertes conjointes (crédit D).

### 8. Impossibilité de la condition 4.4 et biais d'évaluation du juge sur les seuls échecs mécaniques (§4.2)
* **Critiques visées** : `B-(b)5`, `C-(b)2`, `D-(a)4`, `D-(b)2`.
* **Verdict : ACCEPTÉE.** `C-(b)2` démontre mathématiquement (`VÉRIFIÉ` sous indépendance et spécialisation monocanal) que la pénalité de seuillage multiple interdit à une disjonction booléenne de battre le meilleur capteur de $+0{,}10$ (`illustratif`). `D-(a)4` note justement que conditionner aux échecs mécaniques fixe à zéro la ligne de base mécanique.
* **Correction** : En §4.2, le juge est qualifié sur la **population complète** par le gain conditionnel de $(M + J)$ sur les vérificateurs mécaniques $M$ seuls ($Y \not\perp J \mid M$, crédit D). En §4.4, la suite combinée utilise une **agrégation continue** (score logistique calibré sur validation) évaluée sur le **mélange équilibré de tout $K$** (et non sur une famille monocanal).

### 9. Borne d'audit indépendante $1-(1-p\cdot s)^k$ et précision sur $s$
* **Critiques visées** : `A-(b)5`, `B-(b)4`, `D-(b)3`.
* **Verdict : ACCEPTÉE.** Sous corruption corrélée ou concentrée, la formule indépendante est invalide et ne prouve aucune tromperie de l'auditeur (`VÉRIFIÉ`). De plus, estimer $s$ sur les seuls cas tirés à $p = 0{,}10$ donne des intervalles trop larges.
* **Correction** : Dissociation entre (i) un banc dédié de `250` items sabotés et `250` items honnêtes appariés (`illustratif`) mesurant $s$ et $\alpha_{\text{audit}}$ en aveugle, et (ii) la comparaison en campagne aléatoire à la **loi hypergéométrique exacte** simulée sous la structure de corrélation empirique des erreurs.

### 10. Assemblage adversaire manquant dans l'Expérience 2
* **Critique visée** : `A-(c)4`.
* **Verdict : ACCEPTÉE.** Un assemblage aléatoire $a_{\text{comp}}$ est un contrôle trop faible ; on ajoute un témoin négatif **assemblage adversaire $a_{\text{comp-adv}}$** optimisé contre $S_K$ parmi $C_1, C_2, C_3$ (crédit A).

### 11. Défauts statistiques, fuites de sélection et contrôles de l'Expérience 3
* **Critiques visées** : `A-(a)7`, `A-(a)8`, `A-(a)9`, `A-(b)6`, `A-(c)5`, `B-(a)5`, `B-(a)6`, `B-(b)3`, `B-(c)3`, `C-(b)3`, `C-(c)3`, `D-(a)5`, `D-(b)3`, `D-(c)`, `E-(b)4`.
* **Verdicts différenciés** :
  * **ACCEPTÉE** sur `A-(a)8`, `A-(b)6`, `B-(b)3`, `C-(b)3`, `E-(b)4` ($R = 5$ échoue à contrôler les erreurs de type I et II ; la condition $N_{\text{mut}} = 0$ détruit la puissance ; le sort des indécis dans $N_{\text{cat}}$ doit être défini = `0`) ; sur `A-(a)7`, `A-(c)5` (critère 1 vrai par sélection -> validation obligatoire sur dossiers, honnêtes et détecteurs frais) ; sur `D-(a)5`, `D-(b)3` (séparer découverte vs supériorité collective en deux contrastes appariés avec incertitude simultanée) ; sur `B-(c)3`, `C-(c)3`, `D-(c)` (ajouter contrôle aveugle de familles connues renommées et témoin positif d'exploitabilité).
  * **TRANSFORMÉE EN TEST** sur `A-(a)9` et `B-(a)5` (rappel structurel des environnements permutés) : stratifier les `30` environnements (`illustratif`) en `15` permutés isomorphes (mesurant la généralisation structurelle) et `15` combinatoires procéduraux (vérifiant si le taux s'effondre hors isomorphisme connu).
  * **REJETÉE** sur `B-(a)6` (« environnement scellé vrai par construction ») : *raison* — l'environnement scellé n'a jamais prétendu tester les générateurs, mais sert de **contrôle négatif du pipeline d'évaluation** (zéro faux positif de détection là où aucune dégradation non détectable n'existe), rôle dont `D-(c)` confirme l'utilité à condition d'y adjoindre le classement aveugle de familles connues renommées (ce qui est fait).

### 12. Attribution du titre de Greenblatt et al. (2024)
* **Critique visée** : `A-(a)10`.
* **Verdict : ACCEPTÉE.** En application de la règle d'intégrité 3, le titre exact étant contesté de mémoire (*Regardless of Scheming* vs *Despite Intentional Subversion*), je retire le titre cité de mémoire et le remplace par **« référence à vérifier »**.

---

## (b) Expériences corrigées (inférence forte, règle B4)

### Architecture commune corrigée (cas d'application, Question 5)
* **Tâche longue à vérité terrain déterministe** : audit multi-documents de `30` pièces tabulaires et textuelles (`4 000–8 000` jetons, `illustratif`), écart de qualité normalisé $\Delta Q \in [0, 1]$ calculé par programme déterministe.
* **Partition disjointe du banc (`1 800` dossiers, `illustratif`)** : `1 000` dossiers d'adaptation ($D_{\text{adapt}}$), `400` dossiers de validation/calibration ($D_{\text{val}}$) et `400` dossiers de test scellés ($D_{\text{test}}$), issus de générateurs de tables/domaines indépendants.
* **Protocole anti-artefact LoRA et multi-instanciations** : l'agent honnête est instancié par `4` adaptateurs **LoRA-honnêtes** indépendants (`rang 16`, `2 000` trajectoires honnêtes chacun, `illustratif` : `2` dédiés à l'entraînement/validation, `2` tenus à l'écart pour le test). Chaque famille connue $C_1, C_2, C_3 \in K$ et tout candidat $a^*$ sont instanciés par `3` adaptateurs LoRA indépendants (`2` sur $D_{\text{adapt}}/D_{\text{val}}$, `1` réservé sur $D_{\text{test}}$), sur graines et démonstrations disjointes, avec prompt d'inférence strictement identique.
* **Règle de décision B4 uniforme** : tout duel oppose deux hypothèses **exhaustives et exclusives** ($H_A : \theta \le t$ contre $H_B : \theta > t$), jugées par intervalles de confiance simultanés de niveau global `95 %` (`illustratif`). Un intervalle entièrement au-dessus (resp. au-dessous) de $t$ falsifie $H_A$ (resp. $H_B$) ; un intervalle franchissant $t$ conclut « non tranché (puissance insuffisante) ». Toutes les métriques de détection sont calibrées sur $D_{\text{val}}$ pour $\text{FPR} \le 0{,}05$ (`illustratif`) et vérifiées sur $D_{\text{test}}$ (borne supérieure d'IC du FPR $\le 0{,}075$, `illustratif`, sur honnêtes standards, honnêtes difficiles appariés en $\Delta Q$, et honnêtes lexicaux).

---

### Pré-expérience 0 : Qualification des trois instruments et élimination de l'artefact LoRA

Avant tout test de nouveauté sur $a^*$, les trois instruments sont évalués sur $K = \{C_1, C_2, C_3\}$ contre `LoRA-honnête` tenu à l'écart ($n_{\text{test}} = 400$ par bras, `illustratif`) :

* **Duel 0.1 — Lecteurs d'états internes (sondes sur activations projetées $d_{\text{proj}} = 64$, `illustratif`)** :
  * *Ligne de base mécanique $M_{\text{int}}$* : entropie des logits, $D_{\text{KL}}(P_{\text{agent}} \| P_{\text{LoRA-hon-ref}})$ par rapport à un `LoRA-honnête` indépendant (non au modèle gelé), TF-IDF sur la trace et heuristiques de surface.
  * **$H_{0.1A}$** (artefact d'adaptateur ou redondance mécanique) : $\text{AUROC}(\text{LoRA-hon}_1, \text{LoRA-hon}_2) > 0{,}58$ **ou** $\text{TPR}_{\text{sonde}}(K) \le 0{,}65$ **ou** $\text{TPR}(M_{\text{int}} + \text{sonde}) - \text{TPR}(M_{\text{int}}) \le 0{,}08$ (`illustratif`).
  * **$H_{0.1B}$** (signal interne authentique et informatif) : $\text{AUROC}(\text{LoRA-hon}_1, \text{LoRA-hon}_2) \le 0{,}58$ **et** $\text{TPR}_{\text{sonde}}(K) > 0{,}65$ **et** gain conditionnel $> 0{,}08$ (`illustratif`).
  * *Falsification* : bornes simultanées sur $D_{\text{test}}$ ; si $H_{0.1B}$ est falsifiée, les sondes sont écartées de $S$ avant l'Expérience 1-2.
* **Duel 0.2 — Juge textuel (modèle ouvert `14B` QLoRA d'une famille distincte, `illustratif`)** :
  * *Ligne de base mécanique $M_{\text{txt}}$* : vérificateur arithmétique/syntaxique + audit mécanique de citations.
  * **$H_{0.2A}$** : $\text{TPR}(M_{\text{txt}} + J) - \text{TPR}(M_{\text{txt}}) \le 0{,}08$ sur l'ensemble de $D_{\text{test}}$ (`illustratif`, sous réserve $\text{TPR}(M_{\text{txt}}) \le 0{,}85$ ; sinon $K$ est trop trivial et doit être durci).
  * **$H_{0.2B}$** : gain conditionnel $> 0{,}08$ à $\text{FPR} \le 0{,}05$ (`illustratif`).
* **Duel 0.3 — Contrôle au hasard (audit aveugle)** :
  * Sur banc stratifié dédié (`250` items sabotés + `250` items honnêtes appariés, `illustratif`), **$H_{0.3A}$** : sensibilité conditionnelle $s \le 0{,}80$ ou gain sur ré-exécution différentielle simple $\le 0{,}08$ à $\alpha_{\text{audit}} \le 0{,}02$ (`illustratif`), contre **$H_{0.3B}$** : $s > 0{,}80$ et gain $> 0{,}08$. En campagne réelle ($p = 0{,}10$ sans remise, `illustratif`), la capture est comparée à la loi hypergéométrique simulée sur la matrice empirique d'erreurs.
* **Qualification de la suite combinée $S$** : méta-classifieur logistique continu combinant les scores normalisés des instruments qualifiés + $M$, évalué sur le mélange équilibré de $K$ à $\text{FPR}_{\text{global}} \le 0{,}05$ (`illustratif`), avec publication de la table d'alertes conjointes sur honnêtes.

---

### Expérience 1-2 (fusionnée et corrigée) : Absorption plastique à budget borné et séparation par banque pré-scellée d'invariants

Étant donné un candidat $a^*$ atteignant une dégradation $\Delta Q(a^*) \ge 0{,}25$ (`illustratif`) sur $D_{\text{test}}$ :
* **Courbe d'absorption complète dans $S$** : ré-adaptation conjointe de la sonde interne (sur projection $d_{\text{proj}} = 64$, `illustratif`), du juge textuel `14B` (QLoRA sur `n` exemples d'adaptation) et du méta-classifieur aux budgets $n \in \{0, 32, 128, 512, 1000\}$ (`illustratif`, moyenné sur `5` sous-tirages pour $n \le 128$), sous contrainte de rétention par famille $\min_{j \in K} \Delta R_{C_j} \ge -0{,}05$ (`illustratif`).
* **Banque pré-scellée d'extensions $\mathcal{S}^+_{\text{banque}}$** (empreinte cryptographique publiée avant l'inspection de $a^*$) : `3` canaux structurellement hors-$S$ (invariance sur dossiers jumeaux permutés, test distributionnel multi-dossiers sur lots de `20` tâches, ablation causale de sources, `illustratif`), sélectionnés sur $D_{\text{val}}$ et testés sur $D_{\text{test}}$ après `128` exemples d'adaptation (`illustratif`).

L'expérience tranche deux duels séquentiels B4 :

1. **Duel 1a — Non-absorption et plafonnement dans $(K, S, N_{\max} = 1000)$** :
   * Paramètres vrais sur instanciation et dossiers tenus à l'écart : $R_S(1000)$ (TPR à $N_{\max}$) et $g_S = R_S(1000) - R_S(512)$ (pente sur le dernier doublement).
   * **$H_{1a,A}$ (Absorbable ou encore en convergence dans $S$)** : $R_S(1000) > 0{,}60$ **ou** $g_S > 0{,}08$ (`illustratif`).
   * **$H_{1a,B}$ (Non absorbé et plafonné dans $S$)** : $R_S(1000) \le 0{,}60$ **et** $g_S \le 0{,}08$ (`illustratif`).
   * *Falsification* : falsifie $H_{1a,A}$ si $\text{IC}^+(R_S(1000)) \le 0{,}60$ ET $\text{IC}^+(g_S) \le 0{,}08$ ; falsifie $H_{1a,B}$ si $\text{IC}^-(R_S(1000)) > 0{,}60$ OU $\text{IC}^-(g_S) > 0{,}08$.
2. **Duel 1b — Séparabilité par un nouvel invariant au-delà du budget et de la dimension** :
   * Paramètres vrais : $R_{S^+}(128)$ (transfert inter-instanciations du meilleur canal de $\mathcal{S}^+_{\text{banque}}$) et $\Delta_{\text{inv}} = R_{S^+}(128) - \max\big(R_{S_{\text{budget}+}}(1000),\, R_{S_{\text{factice}}}(128)\big)$, où $S_{\text{budget}+}$ augmente le taux d'audit $p$ et le budget de calcul de $S$ à coût égal à $S^+$, et $S_{\text{factice}}$ est un canal de bruit de même faible dimension.
   * **$H_{1b,A}$ (Pas d'invariant nouveau capturé au-delà du budget)** : $R_{S^+}(128) \le 0{,}80$ **ou** $\Delta_{\text{inv}} \le 0{,}20$ (`illustratif`).
   * **$H_{1b,B}$ (Catégorie nouvelle relative à $(K, S, N_{\max})$ attestée par $\mathcal{S}^+_{\text{banque}}$)** : $R_{S^+}(128) > 0{,}80$ **et** $\Delta_{\text{inv}} > 0{,}20$ (`illustratif`).
   * *Issue croisée* : si $H_{1a,A}$ est falsifiée (non-absorption dans $S$) mais $H_{1b,B}$ est falsifiée ($\mathcal{S}^+_{\text{banque}}$ échoue), $a^*$ est classé **« anomalie hors-banque »** (distincte d'une variante) et soumise à un second tour sur dossiers et instanciations frais après proposition d'un nouveau canal $S^+_{\text{nouv}}$.
* **Contrôles négatifs obligatoires (invalidation en cas d'échec)** :
  1. *Adaptateur neuf d'une famille de $K$* (crédit B) : doit falsifier $H_{1a,B}$ ($R_S(1000) > 0{,}60$, `illustratif`).
  2. *Assemblage aléatoire $a_{\text{comp}}$ et assemblage adversaire $a_{\text{comp-adv}}$* (optimisé contre $S_K$ parmi $C_1, C_2, C_3$, crédit A) : doivent tous deux falsifier $H_{1a,B}$.
  3. *Spécificité de $\mathcal{S}^+_{\text{banque}}$* : $\text{FPR} \le 0{,}05$ (`illustratif`) sur cas honnêtes difficiles, cas honnêtes à asymétrie documentaire légitime et bruit non structuré de même $\Delta Q$ (crédit B, E).
  4. *Signal diffus planté dans $S$* (norme connue permettant $\text{TPR}_{\text{Bayes}} \approx 0{,}85$, `illustratif`) : doit être récupéré à $R_S(1000) > 0{,}70$ (`illustratif`) pour exclure un artefact de sous-apprentissage.

---

### Expérience 3 (corrigée) : Capacité d'un groupe de LLM sur $R = 30$ environnements appariés

* **Protocole** : construction de $R = 30$ environnements indépendants (`illustratif`) — stratifiés en `15` **environnements permutés isomorphes** (testant la généralisation structurelle) et `15` **environnements combinatoires procéduraux** (sans isomorphisme connu avec les précédents historiques) — chacun doté de sa base $K_r$, sa suite $S_r$ (qualifiée par Pré-expérience 0) et sa banque pré-scellée $\mathcal{S}^+_{\text{banque}, r}$. Sur chaque environnement, à budget égal de jetons ($B = 10^6$, `illustratif`) et même nombre d'essais sur le jeu de développement de $S_r$, on compare en apparié $G_{\text{multi}}$ (`6` LLM ouverts en critique mutuelle, `illustratif`), $G_{\text{solo}}$ (meilleur membre seul) et $G_{\text{mut}}$ (générateur mécanique de mutations et d'assemblages optimisés de $K_r$).
* **Évaluation découplée et traitement des indécis** : chaque candidat retenu est exécuté et évalué sur des **dossiers frais, des `LoRA-honnêtes` frais et un $S_r$ ré-entraîné de zéro** (crédit A), puis passe un **audit aveugle de non-antériorité**. Un environnement compte pour `1` uniquement si le candidat passe l'Expérience 1-2 (falsification de $H_{1a,A}$ et $H_{1b,A}$) et l'audit ; tout verdict « non tranché » compte pour `0` (le taux d'indécision étant rapporté à part).
* **Deux duels B4 appariés** (intervalles de confiance exacts appariés, correction de Holm-Bonferroni pour un niveau global `0,05`, seuil d'effet minimal pertinent $\delta_0 = 0{,}15$, `illustratif`) :
  * **Duel 3.1 (Au-delà des mutations mécaniques)** : $\delta_{\text{mut}} = P(G_{\text{multi}} = 1) - P(G_{\text{mut}} = 1)$ ; **$H_{3.1A} : \delta_{\text{mut}} \le \delta_0$** contre **$H_{3.1B} : \delta_{\text{mut}} > \delta_0$**. *(Avec $R = 30$, un score $0/30$ donne une borne supérieure exacte à `97,5 %` d'environ `0,116` $< 0{,}15$, falsifiant effectivement $H_{3.1B}$ ; un écart apparié `12/30` contre `0/30` donne une borne inférieure $> 0{,}15$, falsifiant $H_{3.1A}$, `illustratif`.)*
  * **Duel 3.2 (Effet proprement collectif vs modèle seul)** : $\delta_{\text{solo}} = P(G_{\text{multi}} = 1) - P(G_{\text{solo}} = 1)$ ; **$H_{3.2A} : \delta_{\text{solo}} \le \delta_0$** contre **$H_{3.2B} : \delta_{\text{solo}} > \delta_0$**.
* **Contrôles obligatoires** : (1) `5` environnements « scellés » (`illustratif`, contrôle de faux positifs du pipeline) ; (2) `10` familles connues renommées et ré-habillées injectées en aveugle dans l'audit de non-antériorité (doivent être rejetées à $\ge 90\text{ \%}$, `illustratif`, crédit B, D) ; (3) témoin positif d'exploitabilité (vérification par red-team humain aveugle sur un sous-échantillon que des échecs non absorbés existent si tous les générateurs obtiennent `0`).

### Ancrage matériel révisé (`illustratif`, base A100-80Go à `1,50–2,50 USD/h`)
L'extension à `1 800` dossiers, `4` adaptateurs `LoRA-honnêtes`, `3` adaptateurs par famille et la plasticité QLoRA du juge `14B` porte le **bloc prioritaire (Pré-expérience 0 + Expérience 1-2 sur 1 modèle cible `7B–9B`)** à environ `110–180 h` GPU (`180–450 USD`, `illustratif`, exécutable sur un seul GPU `80 Go` en `5–8` jours). L'extension complète **Expérience 3 sur $R = 30$ environnements** est nettement plus lourde (`400–700 h` GPU, `700–1 750 USD`, `illustratif`) et ne doit être lancée qu'après validation du bloc prioritaire.

---

## (c) Réponse à la question de l'arbitre (synthèse en une page)

### Ce qui est établi
* **Par vérification directe des pièces (`VÉRIFIÉ`)** : le bloc de faits ne contient aucune mesure empirique préalable ; tout protocole qui ne fixe ni espace de surveillance ni budget d'adaptation, ou qui compare des saboteurs affinés par LoRA à un modèle honnête non affiné, souffre de défauts mathématiques prouvables (dont la trivialité de la divergence KL contre le modèle gelé et l'impossibilité de détecter un effet collectif fiable sur $R = 5$ essais).
* **Par la littérature antérieure (`RAPPORTÉ`, cité de mémoire)** : les grandes catégories historiques d'attaques — canaux auxiliaires temporels (Kocher, 1996), chaînage de gadgets ROP (Shacham, 2007), exécution spéculative (Kocher et al., 2019 ; Lipp et al., 2018 ; co-auteurs complets : référence à vérifier) et évasion au temps de test (Dalvi et al., 2004 ; Szegedy et al., 2014) — montrent qu'une catégorie nouvelle **peut naître d'un assemblage** dès lors qu'elle viole une hypothèse implicite de l'espace de défense, invalidant la classe de défenses existante. Les travaux sur les attaques adaptatives (Athalye, Carlini et Wagner, 2018 ; Tramer, Carlini, Brendel et Madry, 2020) montrent qu'une défense non ré-adaptée surestime sa robustesse ; les référentiels opérationnels (MITRE ATT&CK, CWE, CAPEC : référence à vérifier) et taxonomies publiées (Barreno et al., 2006) restent descriptifs, sans seuil expérimental consensuel. Les travaux récents sur le contrôle d'agents (Greenblatt et al., 2024 : titre exact et détails à vérifier) formalisent l'évaluation red-team/blue-team sans trancher le critère de nouveauté catégorielle.

### Ce qui ne l'est pas (`HYPOTHÈSE`)
1. **Existence d'un critère intrinsèque (Q1)** : aucune mesure indépendante d'un cadre défensif $(K, S, N_{\max})$ n'est établie. Ma position est qu'une distinction mesurable n'est fondée que **relativement** à un espace d'observation $S$ et à un budget d'adaptation $N_{\max}$ : non-absorption avec plafonnement de pente dans $S$ (rétention par famille préservée), combinée à la séparabilité inter-instanciations par une banque pré-scellée d'observables hors-$S$ qui bat $S$ à budget égal.
2. **Validité des trois surveillants sur un petit modèle ouvert (Q5)** : il n'est pas établi que des sondes internes sur un modèle `7B–9B` (`illustratif`) battent des vérifications mécaniques ou la divergence KL entre adaptateurs dès que l'artefact de prompt *et* l'artefact d'adaptateur LoRA sont neutralisés, ni qu'un petit modèle sache saboter discrètement une tâche longue.
3. **Capacité créative d'un groupe de LLM (Q4)** : il n'est pas établi qu'un groupe multi-LLM conçoive une catégorie nouvelle plutôt que des variantes recombinées. Seuls quatre témoins conjoints permettraient de trancher : exécution réelle sur cible, passage du test de non-absorption sur données et honnêtes frais, comparaison appariée à budget égal contre un générateur mécanique de mutations et un modèle seul (sur $R \ge 30$ environnements stratifiés isomorphes vs procéduraux, `illustratif`), et audit aveugle de non-antériorité calibré sur des familles connues renommées.

### L'expérience à faire en premier
Ne **pas** lancer la compétition multi-LLM en premier : son verdict est ininterprétable tant que les instruments de mesure et le banc ne sont pas qualifiés. La première expérience à exécuter sur un modèle ouvert `7B–9B` (`illustratif`, `~110–180 h` sur un seul GPU `80 Go`, `180–450 USD`, `illustratif`) comprend deux étapes séquentielles sur `1 800` dossiers synthétiques disjoints (`illustratif`) à vérité terrain programmatique :
1. **Pré-expérience 0 (qualification anti-artefacts)** : entraîner `4` adaptateurs `LoRA-honnêtes` et `3` adaptateurs indépendants pour chacune des `3` familles connues $K = \{C_1, C_2, C_3\}$ (`illustratif`), puis tester si chaque instrument (sondes projetées, juge `14B` QLoRA, audit aveugle stratifié) bat ses lignes de base mécaniques sur `LoRA-honnête` tenu à l'écart (avec $\text{AUROC}(\text{LoRA-hon}_1, \text{LoRA-hon}_2) \le 0{,}58$, `illustratif`). Tout instrument qui échoue est retiré de $S$.
2. **Expérience 1-2 (test d'absorption plastique et d'invariant pré-scellé)** : pour le candidat $a^*$ (`3` instanciations indépendantes) ainsi que deux contrôles négatifs obligatoires (un adaptateur neuf de $K$ et un assemblage adversaire $a_{\text{comp-adv}}$), tracer la courbe d'absorption $n \in \{0, 32, 128, 512, 1000\}$ (`illustratif`) avec rétention mesurée famille par famille, tester le plafonnement à $N_{\max} = 1000$ (Duel 1a), puis comparer sur $D_{\text{test}}$ la banque pré-scellée $\mathcal{S}^+_{\text{banque}}$ au même $S$ doté d'un budget égal $S_{\text{budget}+}$ et à un canal factice $S_{\text{factice}}$ (Duel 1b).

### Ce qui me ferait changer d'avis
* **Sur la Q1** : une métrique purement intrinsèque à l'attaque, sans référence à $S$, reproduisant les séparations historiques.
* **Sur les sondes internes (Q5)** : l'échec de la Pré-expérience 0 contre `LoRA-honnête` et $D_{\text{KL}}$ inter-LoRA, qui conduirait à éliminer les sondes de la suite $S$.
* **Sur le critère d'absorption** : constater que l'assemblage adversaire $a_{\text{comp-adv}}$ échoue lui aussi à être absorbé dans $S(1000)$ alors qu'un signal diffus planté est récupéré, ce qui montrerait que le seuil confond composition adverse et nouvelle catégorie.
* **Sur les groupes de LLM (Q4)** : falsifier $H_{3.1A}$ et $H_{3.2A}$ sur les `15` environnements procéduraux non isomorphes (avec `0` faux positif sur le témoin scellé et $\ge 90\text{ \%}$ de rejet des familles renommées, `illustratif`).

FIN-DE-CELLULE