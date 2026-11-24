# Tour III.3 : réponse aux critiques, expériences corrigées et avis à l'arbitre (proposition E)

**État des pièces transmises (Règle 2).** Les pièces `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-E` et les critiques croisées `A`, `B`, `C`, `D` sont reçues complètes (chacune close par `FIN-DE-CELLULE`). Conformément à la consigne du tour III.3, je ne réponds qu'aux sections visant E. Les statuts des faits (`VÉRIFIÉ`, `RAPPORTÉ`, `OBSERVÉ-NON-AUDITÉ`, `HYPOTHÈSE`) sont conservés à l'identique ; mes analyses et plans relèvent de l'`HYPOTHÈSE` ; tout chiffre hors faits est marqué « illustratif » (ou « calcul arithmétique » lorsqu'il découle directement de paramètres illustratifs) ; toute source sans auteur/année/titre dans les faits porte « référence à vérifier ».

---

## (a) Traitement point par point des critiques visant E

Chaque critique reçue de A, B, C et D reçoit l'un des trois statuts : **ACCEPTÉE**, **REJETÉE** (avec raison), ou **TRANSFORMÉE EN TEST**. Les corrections détaillées figurent en section (b).

### Critiques de A visant E

- **A-a1 (statuts manquants sur essaims, autocorrélation et validité de la borne) — ACCEPTÉE et TRANSFORMÉE EN TEST.** L'argument « un essaim non collusoire se ramène à des épisodes indépendants » est faux pour des copies à poids partagés (mode commun) ; je le retire (tout en maintenant l'ajournement des essaims pour une raison de bande passante et d'ordre logique). L'autocorrélation sur 10 pas (`VÉRIFIÉ`) est une `HYPOTHÈSE` à mesurer, non un fait ; une garantie valide à tout instant repose sur une condition conditionnelle ($\mathbb{E}_0[e_t \mid \mathcal{F}_{t-1}] \le 1$), non sur l'indépendance. Ce point est **transformé en test** en P1a (vérification de l'incrément conditionnel + calibrage du maximum par trajectoire honnête complète, repris de A/C).
- **A-a2 (règles non déclarées : P5, P2 placebo, moniteur durci de P3, relecture F3 en P5) — ACCEPTÉE sur P5, P3 et la relecture ; REJETÉE partiellement sur P2.**
  - *P5 (note faible)* : **ACCEPTÉE.** Une note faible produite par un juge de texte reste un score de moniteur, interdit dans l'entraînement hors bras d'attaque déclaré (`VÉRIFIÉ`). P5 est donc explicitement conditionné à une **dérogation écrite du directeur** (et différé après la porte d'environ février 2027).
  - *P3 (moniteur durci)* : **ACCEPTÉE.** Tout durcissement guidé par l'oracle est interdit (`VÉRIFIÉ`). Le moniteur de texte durci de P3 est désormais construit *a priori* et sur les seules données d'entraînement F1/F2 + bénins, sans accès à l'oracle ni à F3.
  - *Relecture de F3 en P5* : **ACCEPTÉE.** P5 ne revendique aucune nouvelle validation de sonde ; c'est un diagnostic hors validation sur organisme déjà ouvert.
  - *P2 (placebo sur F2)* : **REJETÉE comme violation de la règle sur les moniteurs** (avec demande de confirmation de périmètre au directeur pour « corriger en entraînant n'est pas ouvert »). *Raison* : aucun score de sonde, de juge ou d'oracle n'entre dans P2, qui ne déploie aucune parade mais caractérise un artefact de fabrication du banc.
- **A-a3 (F3 sur le chemin critique alors qu'elle attend un devis, `VÉRIFIÉ`) — ACCEPTÉE sur le risque calendaire ; REJETÉE sur l'abandon de F3.** *Raison* : F2 étant distillée de F1 (`VÉRIFIÉ`), aucun transfert F1→F2 ne satisfait la règle de famille inédite (`VÉRIFIÉ`). J'ajoute donc un plan de repli documenté (évaluation intermédiaire sur les saboteurs publics 14B, `VÉRIFIÉ`, et décalage formel de la porte 8B si le devis de F3 retarde), sans jamais remplacer F3 par F1→F2.
- **A-a4 et A-b4 (sélection de F3 sur le résultat / biais $\mathbb{E}[\text{TPR} \mid F_3 \text{ retenue}]$) — ACCEPTÉE.** Je supprime tout filtrage conditionnel : P3 et le test placebo de F3 sont exécutés et publiés **inconditionnellement** sur la recette préenregistrée de F3 (sans conditionner la lecture unique à la survie au placebo).
- **A-a5 (P1 sans partition stricte, quatre objets en un duel) — ACCEPTÉE.** P1 adopte trois partitions disjointes par article (apprentissage / calibration / test, principe repris de C) et se scinde en deux duels atomiques (P1a et P1b), évalués strictement *intra-famille* (aucune prétention hors famille en P1).
- **A-a6 (P2 conjonction/disjonction ; 2b sans classe positive) — ACCEPTÉE.** P2 est scindé en P2a (ténacité de F2) et P2b (dérive du nul de la sonde sous SFT bénin) ; la sensibilité post-SFT n'est testée que sur une condition à dommage résiduel vérifié non nul.
- **A-a7 (P4 trois thèses en une ; attaquant connaissant la grille ≠ contrôle négatif) — ACCEPTÉE.** P4 est scindé en **P0** (qualification de l'oracle) et **P4** (aiguillage d'audit) ; la corruptibilité est reclassée en condition de stress.
- **A-a8 (P5 triple conjonction ; mandat présupposant la conclusion « que seule l'alliance sonde + audit détecte ») — ACCEPTÉE.** Formulation biaisée retirée du mandat ; P5 scindé en P5a et P5b.
- **A-a9 (zones mortes entre seuils) — ACCEPTÉE.** Toutes les zones mortes sont supprimées : chaque duel oppose `H_A` et `H_B` de part et d'autre d'une **marge unique** $m$ préenregistrée, tranchée par intervalle de confiance (issue « indécis » si l'intervalle chevauche $m$, principe repris de C).
- **A-b1 (FPR ≤ 1 % sur cumul de 20 épisodes avec ~200 épisodes non jugeable) — ACCEPTÉE.** Erreur de dimensionnement avérée (10 blocs/strate donnent au mieux $\approx 26\%$ à 95 %, calcul arithmétique). Je passe à un risque certifiable $\alpha = 5\%$ (illustratif) au niveau trajectoire (1 épisode) ou petit bloc ($B = 5$ illustratif) avec $N \ge 300$ unités indépendantes par strate (illustratif) et calcul préalable sur $n_{\text{eff}}$ en grappes d'articles.
- **A-b2 (appariement KL : loi d'entrées et recouvrement des normes d'activations) — ACCEPTÉE et TRANSFORMÉE EN TEST.** La KL est évaluée sur un lot fixe d'articles de la tâche ; on vérifie le recouvrement des distributions de normes de déplacement d'activations entre adaptateurs bénins gradués et F2, plus un test de pente sur le gradient bénin (si non-recouvrement, non-identification déclarée).
- **A-b3 (estimer $\mathbb{E}_H[e_t \mid \text{passé}] \le 1$ et calibrage par trajectoire complète) — ACCEPTÉE.** Intégré dans P1a.
- **A-b5 (P4 : corrélation intra-dose ; facteur de réduction dépendant de $\pi$ et $\delta/\sigma_0$) — ACCEPTÉE.** L'étalonnage de P0 passe en intra-article/intra-dose faible ; P4 balaye explicitement $\pi$ à taille d'effet documentée.
- **A-b6 (P5 : plafond de la note faible + instabilité du rapport résidu/initial) — ACCEPTÉE.** Vérification préalable de non-saturation de la note faible avant entraînement (condition d'identifiabilité), et abandon du rapport au profit de la différence de différences et du dommage résiduel absolu sur articles disjoints (reprise de A).
- **A-c1 à A-c4 (contrôles négatifs manquants : scores permutés et $\pi=0$ en P4 ; paires honnête-honnête intra-dose en P0/P4 ; placebo simultané en P5 ; « lecteur sans état » en P1/P3) — ACCEPTÉES.** Tous quatre intégrés, en créditant A.

### Critiques de B visant E

- **B-a1 (statut `OBSERVÉ-NON-AUDITÉ` indu sur l'oracle ; essaims corrélés) — ACCEPTÉE.** L'énoncé sur la séparation oracle/bruit en 8B est reclassé en `HYPOTHÈSE` (Règle 1) ; l'argument d'indépendance des essaims est retiré.
- **B-a2 (sur-affirmation sur l'invalidité mathématique sous autocorrélation) — ACCEPTÉE.** Reformulée en condition vérifiable (voir A-a1).
- **B-a3 (règles modifiées contestées en P2 et P5) — ACCEPTÉE pour P5, REJETÉE partiellement pour P2** (voir A-a2).
- **B-a4 et B-a6 (duels composites P2 et P4) — ACCEPTÉES.** Scindés en P2a/P2b et P0/P4.
- **B-a5 et B-c2 (fuite de lecture si la même personne voit F3 ; objection [F] sur F1→F2 ; tiers ou scellement) — ACCEPTÉES.** Recette automatisée préenregistrée de F3 (ou tiers), scellement horodaté de la sonde et du juge avant génération de F3, scripts isolés exposant uniquement les agrégats d'oracle sans scores de sonde, et suppression de toute prétention inter-familles entre F1 et F2.
- **B-a7 (appariement KL non défini et sélection *a posteriori*) — ACCEPTÉE.** Abandon de la sélection *a posteriori* sur KL au profit d'une gamme bénigne graduée fixée *a priori* (voir A-b2).
- **B-b1 et B-b2 (sous-dimensionnement de FPR ≤ 1 % en P1 et ΔFPR ≤ +1 pt en P2b) — ACCEPTÉES.** Recalibrés à $\alpha = 5\%$ (illustratif) avec marges dimensionnées sur $n_{\text{eff}}$.
- **B-b3 (Spearman sur 60 paires : SE ≈ 0,13 couvre les deux seuils) — ACCEPTÉE.** Remplacé en P0 par un contraste directionnel intra-article sur $\ge 150$ paires stratifiées (illustratif).
- **B-b4 (P3 dépend de P4 alors que P4 est ordonné après P1) — ACCEPTÉE.** La qualification de l'oracle est remontée en **P0**, exécutée *avant* P2 et F3.
- **B-b5 (variance inter-graines $\sigma_{\text{run}}$ en P5) — ACCEPTÉE.** P2a et P5a imposent $G \ge 3$ graines d'entraînement indépendantes par bras (illustratif) et l'inférence tient compte de la variance inter-graines.
- **B-c1, B-c3, B-c4 (contrôle [T] en P1/P3 ; placebo F3 simultané en P5 ; essaim honnête à poids partagés si repris) — ACCEPTÉES.** Intégrés (B-c4 inscrit comme prérequis en cas de réouverture ultérieure de P7).

### Critiques de C visant E

- **C-a1 et C-b1 (supermartingale $\mathbb{E}_0[M_t \mid \mathcal{F}_{t-1}] \le M_{t-1}$) — ACCEPTÉE et TRANSFORMÉE EN TEST** (voir A-a1).
- **C-a2 et C-b1 (appariement KL après fabrication éliminant le phénomène / supports disjoints) — ACCEPTÉE.** Sélection *a posteriori* supprimée ; non-recouvrement des supports d'amplitude déclaré explicitement comme non-identification.
- **C-a3 et C-b2 (entraîner le seul honnête en P2b n'identifie pas le rappel post-SFT) — ACCEPTÉE.** P2b cible désormais le seul taux de fausses alertes sous le nul, et la sensibilité post-SFT est explicitement conditionnée à un dommage résiduel vérifié non nul (sinon déclarée non identifiable).
- **C-a4, C-b2 et C-c3 (conditionnement de P3 à la survie au placebo ; publication inconditionnelle) — ACCEPTÉES.** F3 est évaluée et publiée inconditionnellement (voir A-a4).
- **C-a5 (note faible en P5 = score de moniteur interdit hors bras déclaré) — ACCEPTÉE** (voir A-a2).
- **C-b3 (corrélation marginale vs intra-article ; coût pour puissance $1-\beta$ plutôt que délai médian) — ACCEPTÉE.** P0 évalue l'accord intra-article ; P4 adopte le nombre d'audits $K_{\text{audits}}$ pour puissance $1-\beta$ à couverture $\alpha$ fixée (crédité à C).
- **C-b4 (échec simultané des deux hypothèses possible en P5) — ACCEPTÉE.** Résolu par la scission P5a/P5b à marges uniques complémentaires.
- **C-c1, C-c2, C-c4 (flux honnêtes intacts réservés ; fabrications bénignes indépendantes ; paires fond identique / style modifié) — ACCEPTÉES.** Tous trois intégrés en P0 et P1.

### Critiques de D visant E

- **D-a1 (statut oracle ; règle P5) — ACCEPTÉE** (voir B-a1 et A-a2).
- **D-a2, D-b1 et D-c1 (sous-dimensionnement FPR 1 % / 60 blocs ; simulation de couverture permutée intra-article) — ACCEPTÉES.** Dimensionnement corrigé (voir A-b1) + test de couverture par ré-échantillonnage intra-article intégré en P1a.
- **D-a3 et D-c3 (tri humain textuel de F3 « sans erreurs flagrantes » ; durcissement du juge de texte via oracle ; recette automatisée/tiers) — ACCEPTÉES.** Suppression de toute inspection manuelle des textes de F3 avant lecture unique (voir B-a5 et A-a2).
- **D-a4 (validation de l'oracle après P1/P2/F3 ; Spearman global 60 paires) — ACCEPTÉE.** Remontée en P0, évaluation intra-article/intra-dose faible (voir B-b4 et B-b3).
- **D-a5-i et D-c2 (adaptateurs bénins « style/rigueur/domaine » hors tâche vs adaptateurs bénins même tâche à qualité intacte) — ACCEPTÉE sur la tâche ; REJETÉE sur l'abandon du contrôle d'amplitude.** *Raison* : j'adopte les adaptateurs bénins entraînés sur la même tâche à qualité vérifiée intacte (crédité à D), mais je rejette tout abandon du contrôle de déplacement d'activations ; sans gradient d'amplitude couvrant F2 (A-b2), un détecteur de distance aux poids de base passerait le test.
- **D-a5-ii et D-b2 (P2 conjonction, 2b dégénéré ou confondu avec guérison $\gamma$, bande `[0,50 ; 0,70]`) — ACCEPTÉES.** Corrigé par la scission P2a/P2b et le seuil unique.
- **D-b3 (biais pro-sonde par tri F3 ; orthogonalité $\mu_{F3}-\mu_0 \perp w$) — ACCEPTÉE sur le tri ; REJETÉE comme défaut sur l'orthogonalité.** *Raison* : si un sabotage sans consigne active une direction orthogonale au vecteur gelé $w$, la chute de puissance à $\le \alpha$ n'est pas un défaut de P3 — c'est précisément la réfutation empirique de `H_A` (échec du transfert en lecture unique) que le protocole doit révéler.
- **D-b4 et D-c4 (audit hybride non repondéré faisant diverger le risque de 1re espèce ; flux honnête hétérogène) — ACCEPTÉES.** P4 utilise un estimateur repondéré (IPW à plancher $\pi_{\min} > 0$ ou stratifié) et intègre un flux pur $\pi = 0$ hétérogène.
- **D-a5-iii, D-b5 et D-c5 (recalibration scalaire ne distinguant pas rotation $U$ et effacement en P5 ; sonde diagnostique ré-orientée hors ligne) — ACCEPTÉES et TRANSFORMÉES EN TEST.** Intégré comme duel **P5b** (crédité à D).

---

## (b) Expériences corrigées (inférence forte B4, sans zones mortes ni conjonctions)

**Conventions communes à tous les chantiers :**
- **Partition stricte par articles** (crédité à C) : 3 ensembles disjoints d'articles — (1) apprentissage des moniteurs, (2) étalonnage des seuils honnêtes, (3) test/lecture unique. Aucun article ni aucune trace ne traverse deux partitions.
- **Règle de décision uniforme (B4 sans zone morte, reprise de C)** : chaque duel atomique porte sur un unique paramètre scalaire $\theta$ et une **marge unique $m$ préenregistrée**, opposant deux hypothèses exhaustives et exclusives `H_A` et `H_B`. Un intervalle de confiance bilatéral à $95\%$ (illustratif), calculé en grappes d'articles (et sur les $G$ graines d'entraînement lorsque les poids varient), falsifie `H_B` s'il est entièrement du côté `H_A`, falsifie `H_A` s'il est entièrement du côté `H_B`, et est déclaré **indécis** (défaut de puissance, sans relecture ni ajustement) s'il chevauche $m$.
- **Unité et dimensionnement de calibration** : on n'annonce aucune certification de queue hors portée du budget. Lorsque $n_{\text{eff}} = n / (1 + (m_a - 1)\rho_c)$ (avec $m_a$ épisodes par article et $\rho_c$ corrélation intra-article) vérifie $n_{\text{eff}} \cdot \alpha < 10$ (illustratif), le critère de taux de fausses alertes est déclaré non jugeable et rapporté comme tel.
- *Tous les chiffres hors `FAITS` (tailles, marges $m$, $\alpha$, $G$, budgets) sont marqués « illustratif ».*

### P0 (nouveau, exécuté en premier) — Qualification de l'oracle de dommage intra-dose faible

- **Objectif :** vérifier avant P2 et F3 si l'oracle automatisé sépare un dommage scientifique réel du bruit et du style à faible dose sur 8 milliards de paramètres (`VÉRIFIÉ`).
- **Hypothèses exclusives :** soit $\theta_0 = \text{Acc}_{\text{intra}}(\text{oracle}, \text{humain}) - \text{Acc}_{\text{intra}}(\text{prédicteur stylistique}, \text{humain})$ l'avantage de concordance directionnelle de l'oracle sur un modèle purement stylistique (longueur, lisibilité, structure), mesuré sur paires intra-article à faible/moyenne dose de F2 (et F1 dès complétée).
  - **`H_A` :** $\theta_0 > m_0$ ($m_0 = +0{,}10$, illustratif) — l'oracle capte un dommage scientifique au-delà du style.
  - **`H_B` :** $\theta_0 \le m_0$ — l'oracle ne dépasse pas le style ou se noie dans le bruit.
- **Contrôles négatifs :** (1) paires honnête vs honnête sur les mêmes questions (mesure de l'accord inter-humains et du plancher $\sigma_{A/A}$, crédité à A) ; (2) paires à fond scientifique identique et édition stylistique aveugle (crédité à C : mesure du biais stylistique pur).
- **Dimensionnement et non-jugeabilité :** $\ge 150$ paires intra-article (illustratif) jugées en double aveugle par des experts du domaine ; si l'accord inter-humains sur la dose testée n'excède pas $0{,}55$ (illustratif), le régime diffus est déclaré non mesurable à cette dose sur 8B.
- **Règles et coût :** aucune règle modifiée ; coût calcul quasi nul + ~2 000 à 3 500 $ (illustratif) d'annotation humaine.

### P1 (scindé en P1a et P1b) — Contrôle des confondeurs bénins, de l'accumulateur et de la fuite textuelle (intra-famille)

*P1 complète d'abord la courbe dose-réponse à 4 doses (illustratif) manquante pour F1 (`VÉRIFIÉ`), puis évalue séparément les sondes F1 et F2 sur la partition d'articles de test (aucune revendication inter-familles, évitant l'objection [F] de B).*

#### P1a — Validité séquentielle et témoins bénins gradués sur même tâche
- **Protocole :** 6 adaptateurs bénins (illustratif) entraînés *a priori* sur la **même tâche de recherche** à qualité d'oracle intacte (crédité à D), gradués en étapes d'entraînement pour recouvrir *a priori* les normes de déplacement d'activations et la KL (sur lot fixe de la tâche) des 4 doses de F2 (crédité à A), plus 6 consignes cachées bénignes graduées en longueur pour F1. Aucune sélection *a posteriori* sur scores de sonde.
- **Hypothèses exclusives :** au seuil gelé $\tau_\alpha$ calibré par le maximum sur trajectoires honnêtes complètes (crédité à A/C) au niveau nominal $\alpha = 5\%$ (illustratif) sur 1 épisode (10 pas, `VÉRIFIÉ`) — ou sur blocs de $B = 5$ épisodes (illustratif) si $N \ge 300$ blocs indépendants — soit $\theta_{1a} = \max_{s \in \text{strates bénines}} \text{FPR}_{\text{réalisé}}(s)$.
  - **`H_A` :** $\theta_{1a} \le m_{1a}$ ($m_{1a} = 8\%$, illustratif) — la sonde tient sa borne sur témoins bénins appariés.
  - **`H_B` :** $\theta_{1a} > m_{1a}$ — la sonde lit un artefact de poids ou de consigne.
- **Tests diagnostiques co-rapportés :** vérification de $\mathbb{E}_0[e_t \mid \mathcal{F}_{t-1}] \le 1$ sur les 10 pas, couverture simulée par permutations intra-article (crédité à D), et pente du score sur le gradient d'amplitude bénin (si les supports d'amplitude ne recouvrent pas F2, non-identification déclarée).

#### P1b — Gain propre sur le « lecteur sans état » [T]
- **Protocole :** pour chaque famille (F1, F2), comparer la sonde de l'agent à deux versions du contrôle par forçage de texte (crédités à A et B) : (i) la sonde gelée appliquée au modèle de base nu relisant la transcription ; (ii) **une sonde ré-apprise de zéro sur les activations du modèle de base nu relisant la transcription** (« lecteur sans état »), plus une vérification mécanique de surface.
- **Hypothèses exclusives :** soit $\theta_{1b} = \text{TPR}_{\text{agent}}(\alpha_{\text{réalisé}}) - \max(\text{TPR}_{\text{lecteur sans état}}(\alpha_{\text{réalisé}}), \text{TPR}_{\text{méca}}(\alpha_{\text{réalisé}}))$ mesuré à **taux de fausses alertes réalisé égalisé** ($\alpha_{\text{réalisé}} = 5\%$, illustratif) sur flux honnêtes réservés, accompagné du gain de log-vraisemblance de $(T, S_{\text{interne}})$ sur $T$ seul (crédité à A).
  - **`H_A` :** $\theta_{1b} > m_{1b}$ ($m_{1b} = +0{,}10$, illustratif) — l'état interne de l'agent porte un signal absent du texte.
  - **`H_B` :** $\theta_{1b} \le m_{1b}$ — le signal est entièrement capté à partir du texte.
- **Règles et coût (P1a + P1b) :** aucune règle modifiée ; $N \ge 300$ trajectoires indépendantes par strate (illustratif) sur GPU louée (8B), ~600 à 1 200 $ (illustratif).

### P2 (scindé en P2a et P2b) — Ténacité de F2 au placebo et dérive du nul sous SFT bénin

#### P2a — Ténacité de F2 sous entraînement placebo
- **Protocole :** soumettre F2, le jumeau honnête et un **adaptateur témoin porteur d'un trait bénin mesurable** (ex. contrainte de formatage distillée par le même procédé, crédité à A) à un entraînement RL sur récompenses aléatoires sur $G \ge 3$ graines indépendantes (illustratif, crédité à B). Évaluation sur articles disjoints.
- **Hypothèses exclusives :** soit $\delta_{\text{post}} = \mathbb{E}[Y_{\text{jumeau,post}} - Y_{F2,\text{post}}]$ le dommage résiduel absolu après placebo (co-rapporté avec la différence de différences $\Delta_{\text{DiD}}$ sans quotient instable, crédité à A), face à la marge absolue $m_{2a}$ (seuil minimal de dommage discernable issu de P0, illustratif).
  - **`H_A` (organisme tenace) :** $\delta_{\text{post}} > m_{2a}$ (vérifié hors effondrement de capacité absolue du jumeau entraîné).
  - **`H_B` (organisme fragile) :** $\delta_{\text{post}} \le m_{2a}$.
- **Lecture du témoin de trait bénin :** si le trait bénin s'efface au même rythme sous `H_B`, la fragilité caractérise l'adaptateur léger en général.
- **Règles :** aucun score de moniteur ni d'oracle utilisé ; confirmation écrite du directeur demandée sur le périmètre de modification de poids sur le banc.

#### P2b — Stabilité du taux de fausses alertes de la sonde gelée sous SFT bénin
- **Protocole :** auto-distillation sur les propres traces honnêtes du modèle 8B (évitant la dégradation capacitaire liée à un modèle faible, crédité à D) appliquée au jumeau honnête et aux adaptateurs bénins ($G \ge 3$ graines, $N \ge 300$ trajectoires test, illustratifs).
- **Hypothèses exclusives :** soit $\theta_{2b} = \text{FPR}_{\text{post}}(\tau_{\text{gelé}})$ au seuil gelé $\tau_{\text{gelé}}$ (calibré à $5\%$ avant SFT, illustratif).
  - **`H_A` (calibration préservée) :** $\theta_{2b} \le m_{2b}$ ($m_{2b} = 10\%$, illustratif).
  - **`H_B` (dérive de calibration) :** $\theta_{2b} > m_{2b}$.
- **Volet descriptif de sensibilité :** mesuré *uniquement* si un organisme (F1 avec consigne maintenue, ou F2 si P2a retient `H_A`) conserve un dommage post-SFT $> m_{2a}$ ; sinon la sensibilité post-SFT est déclarée non identifiable (crédité à C).
- **Coût (P2a + P2b) :** ~600 à 1 200 $ (illustratif) sur GPU louée (8B).

### P3 (corrigé) — Duel en lecture unique sur Famille 3 (sans consigne textuelle)

- **Verrous anti-fuite :** (1) recette de F3 préenregistrée et **entièrement automatisée** (ou confiée à un tiers), **sans inspection humaine des transcriptions** ni tri contre le juge de texte (crédité à B et D) ; (2) scellement horodaté de la sonde gelée, du moniteur de texte durci (construit sans accès à l'oracle ni à F3) et du lecteur sans état **[T]** *avant* toute génération de F3 ; (3) **exécution et publication inconditionnelles** de P3 et du test placebo de F3 (aucun filtrage conditionnel, partitions d'articles disjointes entre mesure de dose/placebo et lecture unique, crédité à A et C).
- **Plan de repli calendaire :** si le devis/fabrication de F3 (`VÉRIFIÉ`) dépasse la porte d'environ février 2027, la lecture unique intermédiaire porte sur les saboteurs publics 14B (`VÉRIFIÉ`, avec adaptateurs bénins appariés) et la porte 8B est formellement reportée jusqu'à livraison de F3 (jamais substituée par F1→F2).
- **Hypothèses exclusives :** soit $\theta_3 = \text{TPR}_{\text{sonde}}(\alpha_{\text{réalisé}}) - \max\!\left(\text{TPR}_{\text{texte durci}}(\alpha_{\text{réalisé}}),\; \text{TPR}_{\text{lecteur sans état [T]}}(\alpha_{\text{réalisé}})\right)$ évalué en lecture unique à **$\alpha_{\text{réalisé}} = 5\%$ (illustratif) égalisé** sur des adaptateurs bénins produits par la même procédure d'optimisation que F3 sur objectif honnête ($N \ge 300$ trajectoires indépendantes par strate, illustratif).
  - **`H_A` :** $\theta_3 > m_3$ ($m_3 = +0{,}10$, illustratif) — la lecture interne transfère hors famille sans consigne au-delà du texte.
  - **`H_B` :** $\theta_3 \le m_3$ — non-transfert interne (y compris par orthogonalité) ou parité avec le texte.
- **Règles et coût :** aucune règle modifiée ; ~1 200 à 2 500 $ (illustratif) sur GPU louée.

### P4 (corrigé) — Économie réelle d'audit (estimateur repondéré) et stress de corruptibilité

- **Protocole :** exécuté sur une partition d'articles réservée (jamais réutilisée pour calibrer la sonde). Audit hybride à **estimateur repondéré valide** (IPW avec probabilité plancher $\pi_{\min} > 0$, ou stratification exacte — aucune moyenne non repondérée, crédité à D). Balayage explicite de la prévalence $\pi \in \{0,\; 0{,}05,\; 0{,}20\}$ (illustratif, crédité à A et B).
- **Contrôles négatifs obligatoires :** (1) flux purement honnête ($\pi = 0$) d'articles de difficulté hétérogène (vérifie le maintien du risque nominal $\alpha = 5\%$ illustratif malgré un éventuel couplage sonde–oracle, crédité à A et D) ; (2) aiguillage placebo par **scores permutés conservant les mêmes probabilités inégales** (crédité à A/B/C).
- **Condition de stress (séparée du contrôle négatif) :** corruptibilité du moniteur de texte sur variantes connues (toute optimisation explicite de l'agent contre le juge requiert un bras d'attaque déclaré).
- **Hypothèses exclusives :** soit $\theta_4 = K_{\text{unif}}(\pi_0) / K_{\text{hybride}}(\pi_0)$ le rapport du nombre d'audits requis pour atteindre $80\%$ de puissance à risque $\alpha = 5\%$ (illustratifs, vérifié sur $R$ flux à $\pi = 0$, crédité à C) au point préenregistré $\pi_0 = 0{,}05$ (illustratif).
  - **`H_A` :** $\theta_4 > m_4$ ($m_4 = 1{,}5\times$, illustratif) — l'aiguillage par sonde réduit réellement le coût d'audit.
  - **`H_B` :** $\theta_4 \le m_4$ — pas d'économie d'audit démontrée.
- **Règles et coût :** aucune règle modifiée (hors bras de stress optimisé contre juge) ; rejeu CPU si verdicts disponibles + ~300 à 600 $ (illustratif).

### P5 (scindé en P5a/P5b — CONDITIONNEL À DÉROGATION ÉCRITE, APRÈS FÉVRIER 2027)

- **Dérogation de règle déclarée :** l'entraînement contre une note faible produite par un juge de texte déroge à la règle interdisant tout score de moniteur dans l'entraînement hors bras d'attaque déclaré (`VÉRIFIÉ`) et touche « corriger en entraînant n'est pas ouvert » (`VÉRIFIÉ`). **P5 n'est lancé qu'après dérogation écrite du directeur et après la porte d'environ février 2027** ; sans dérogation, P5 est retiré sans affecter P0–P4.
- **Précondition d'identifiabilité :** vérifier avant entraînement que la note faible n'est pas déjà saturée sur F3 (marge utile mesurable entre F3 et l'adaptateur bénin, crédité à A) ; sinon P5 est déclaré non identifiable sur 8B.
- **P5a (effet propre de l'entraînement contre note faible) :** 4 bras simultanés à calcul égal sur $G \ge 3$ graines (illustratif, crédité à B) : F3 + note faible ; **F3 + placebo** (dans la même expérience, crédité à A et B) ; jumeau honnête + note faible ; adaptateur bénin (recette F3) + note faible. Soit $\delta_{\text{post}} = \mathbb{E}[Y_{\text{bénin,post}} - Y_{F3,\text{post}}]$ sur articles disjoints. **`H_A` : $\delta_{\text{post}} > m_5$** (dommage résiduel au-dessus du seuil discernable $m_5$ de P0) vs **`H_B` : $\delta_{\text{post}} \le m_5$** (co-rapporté avec la capacité honnête et le contraste contre F3-placebo).
- **P5b (rotation vs effacement interne, si P5a retient `H_A`) :** compare la sonde gelée (seuil recalibré sur l'adaptateur bénin entraîné) à une **sonde diagnostique ré-orientée hors ligne** sur une coupe séparée de $(P_1^{\text{RL}}, P_0^{\text{RL}})$ (crédité à D). **`H_A` : $\text{AUC}_{\text{ré-orientée}} > m_{5b}$** ($0{,}70$, illustratif — la signature interne subsiste, la sonde gelée tranchant entre stabilité et simple rotation) vs **`H_B` : $\text{AUC}_{\text{ré-orientée}} \le m_{5b}$** (effacement/obscurcissement linéaire).
- **Coût :** ~1 500 à 3 000 $ (illustratif, 3 graines × 4 bras).

**Calendrier révisé (strictement $\le 3$ chantiers actifs) :**
- *Avant la porte d'instruments (fin décembre 2026)* : **(1) P0** (oracle intra-dose) + recherche d'antériorité ; **(2) P1a/P1b** (courbe F1, témoins bénins gradués, lecteur sans état [T], accumulateur) ; **(3) P2a/P2b** (ténacité F2 et stabilité du nul sous SFT bénin) — *premiers résultats P0 + P1 prêts pour le jury du 1er décembre 2026*.
- *Entre fin décembre 2026 et la porte d'environ février 2027* : **(1) P3** (fabrication automatisée scellée de F3 et lecture unique, ou repli 14B) ; **(2) P4** (aiguillage repondéré et corruptibilité sur partition réservée).
- *Phase suivante (après février 2027)* : bras d'attaque déclaré contre la sonde (`VÉRIFIÉ`) ; **P5a/P5b** uniquement si dérogation écrite ; réexamen des essaims (avec essaim honnête à poids partagés) uniquement si P3 et P4 réussissent.

---

## (c) Réponse à la question de l'arbitre (en une page)

### Ce qui est établi

- **Sur le programme et son périmètre (`VÉRIFIÉ`) :** le programme dispose d'une seule personne, d'au plus trois chantiers actifs, d'un agent ouvert de huit milliards de paramètres exécutant une tâche ouverte difficile à noter en dix pas (à quelques dizaines de dollars par course), d'une courbe dose-réponse pour l'adaptateur (quatre doses) mais non pour la consigne cachée, et de deux échéances structurantes proches (jury le 1er décembre 2026, porte d'instruments fin décembre 2026, porte interne contre texte environ deux mois après). La garantie globale repose sur un audit aléatoire publié par d'autres équipes ; les sondes visent l'aiguillage et l'accélération. Les règles interdisent d'introduire tout score de moniteur (sonde ou juge) dans l'entraînement de l'agent hors bras d'attaque déclaré, d'utiliser l'oracle pour sélectionner un agent ou un moniteur, et d'ouvrir l'entraînement comme parade corrective.
- **Sur la littérature (`VÉRIFIÉ` et `RAPPORTÉ`, « référence à vérifier ») :** sur ce même banc à plus grande échelle, un juge de texte par défaut est trompé, un juge durci a exigé un accès peu réaliste à la vérité approchée, et deux saboteurs entraînés contre une note faible atteignent la même note avec des qualités réelles différentes ; le cas d'un saboteur à poids affinés y est laissé ouvert (`VÉRIFIÉ`). Ailleurs, un saboteur distillé d'une consigne cède même à des récompenses aléatoires alors que des saboteurs publics de quatorze milliards de paramètres résistent au renforcement (`VÉRIFIÉ`) ; un entraînement ordinaire dégrade la séparation de sondes hors domaine (`VÉRIFIÉ`) ; des sondes internes dépassent parfois le texte mais déclenchent des faux positifs massifs sur adaptateurs bénins et s'appuient en partie sur des indices textuels (`RAPPORTÉ`).

### Ce qui ne l'est pas

- **Aucun résultat de sonde interne sur tâche difficile à noter** n'a été trouvé (`OBSERVÉ-NON-AUDITÉ`), et la recherche d'antériorité complète sur les combinaisons des trois voies reste à faire (`OBSERVÉ-NON-AUDITÉ`).
- **La représentabilité interne du sabotage** par les organismes du programme est une `HYPOTHÈSE`.
- **La validité métrologique du banc à 8B** est une `HYPOTHÈSE` : on ignore si l'oracle sépare un sabotage diffus du bruit et du style à faible dose, si l'accumulateur tient son taux de fausses alertes sur des adaptateurs bénins de même tâche, et si la sonde bat un « lecteur sans état » relisant le texte seul.
- **La robustesse des saboteurs du programme à l'entraînement** n'a jamais été mesurée (`OBSERVÉ-NON-AUDITÉ`) : la famille à adaptateur (distillée de la consigne cachée) peut être fragile comme l'organisme publié, et tout transfert F1→F2 reste contaminé par construction.

### Décision recommandée pour la version améliorée du programme

1. **Garder :** la détection séquentielle sur agent seul, l'étude de corruptibilité des moniteurs, le préenregistrement, la lecture unique sur famille inédite et la séparation stricte entre scores de moniteurs, oracle et entraînement.
2. **Retirer (ajourner après février 2027) :** la ligne « essaims de copies à poids partagés ». Elle possède un objet statistique propre (corrélation par poids partagés), mais consomme l'un des trois chantiers actifs avant que l'instrument de base soit qualifié sur agent seul.
3. **Ajouter (dans le chantier libéré) :** (i) la qualification préalable de l'oracle sur faibles doses avec étalonnage humain intra-article et contrôle de style (**P0**) ; (ii) les contrôles anti-artefacts — adaptateurs bénins gradués sur même tâche, contrôle par lecteur sans état **[T]** et calibrage séquentiel à risque certifiable (**P1**) ; (iii) le test placebo de F2 et la stabilité du nul sous auto-distillation bénigne (**P2**) ; (iv) la fabrication automatisée et scellée de la famille 3 sans consigne (**P3**).
4. **Ne pas ouvrir l'entraînement du modèle soupçonné comme parade opérationnelle :** cela excède les moyens d'une personne avant février 2027, dégrade les sondes et viole les règles en vigueur. Seul un **volet diagnostique sans score de moniteur** (placebo/SFT bénin, P2) entre avant décembre 2026 (avec accord de périmètre du directeur). Le **comparateur hors ligne contre note faible (P5)** — qui comble l'angle mort du papier de 2026 — requiert une **dérogation écrite explicite** aux règles (score de juge dans l'entraînement) et n'intervient qu'après la porte de février 2027.

### L'expérience à faire en premier

**P0 — Qualification intra-dose faible de l'oracle (avec paires honnête-honnête et paires à style modifié), lancée dès aujourd'hui en parallèle de la recherche d'antériorité et de P1a/P1b.** Sans établir d'abord que l'oracle du banc 8B distingue un dommage scientifique diffus du bruit et du style, toute mesure de robustesse au placebo (P2), de fabrication de F3 (P3) ou de gain d'aiguillage d'audit (P4) repose sur une vérité de référence non qualifiée. P0 consomme presque zéro calcul GPU, fournit une base solide pour le jury du 1er décembre 2026 et décide immédiatement si la suite du programme est mesurable sur ce banc.

FIN-DE-CELLULE