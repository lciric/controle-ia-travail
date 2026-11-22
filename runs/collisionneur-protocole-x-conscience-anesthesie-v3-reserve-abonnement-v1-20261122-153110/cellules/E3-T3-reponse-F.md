# Proposition F — Réponse aux critiques et protocole corrigé (Tour III.3)

*État des pièces et discipline de statuts (règles 1, 2 et 4) :* les blocs `FAITS`, `QUESTION DE L'ARBITRE` (empreinte `sha256` identique), `E3-T1-conception-F` et les cinq critiques croisées `E3-T2-critique-croisee-A` à `E` sont présents et intègres (`VÉRIFIÉ` par lecture ; empreintes `sha256` non recalculées). Les articles primaires de `2026` évoqués dans `FAITS` ne sont pas transmis (`RAPPORTÉ`, référence à vérifier). Conformément à la consigne, je ne réponds qu'aux sections visant la proposition F. Hors l'année `2026`, les `6` tâches nommées dans les faits, les dates bibliographiques, les noms de modèles et les constantes/identités combinatoires exactes (signalées comme telles), tout chiffre empirique (seuils, effectifs, rangs, doses, coûts) est marqué `illustratif`. Aucun statut des pièces transmises n'est modifié.

---

## (a) Réponse critique par critique (sections visant F uniquement)

Pour éviter toute redite inutile tout en n'omettant aucun point, chaque critique est traitée dans l'ordre des pièces A à E avec sa décision explicite (**ACCEPTÉE**, **REJETÉE**, ou **TRANSFORMÉE EN TEST**).

### Critique A (section « Sur la proposition F » et point 1 final visant B, D, E, F)

1. **A-(a)1 & A-(c)1 — Asymétrie de supervision ($V_{\text{cible}}$ optimisé vs C1–C3 non optimisés ; Kriegeskorte et al., 2009 ; Hewitt & Liang, 2019) :** **ACCEPTÉE** sur le protocole d'extraction. Dès lors que F ré-extrait $V_{\text{cible}}$ par optimisation supervisée sur $D_{\text{train}}$, battre des témoins non supervisés C1–C3 ne suffit pas à écarter un sur-ajustement de l'extracteur. *Nuance (partiellement rejetée si comprise comme invalidant C1–C3) :* C1–C3 demeurent nécessaires pour tester la prédiction littérale de B dans les faits, mais doivent être complétés par un **nul de sélection** (étiquettes permutées + 20 partitions équilibrées ; repris explicitement de D2 de A, règle B1).
2. **A-(a)2 — Porte de réplication sélectionnant sur `4` essais (`2` méthodes × `2` échelles) :** **ACCEPTÉE.** Ce filtrage gonfle le taux de passage à $1-(1-q)^4$ et conditionne l'issue. Le filtrage multi-essais est supprimé : chaque couple méthode × modèle constitue un bras préenregistré autonome, intégralement publié même en cas d'échec.
3. **A-(a)3 & A-(c)2 — Confusion avec l'identité de tâche / consigne (« traduis », « classe ») :** **TRANSFORMÉE EN TEST.** L'hypothèse testable d'A (point 5 final : la dissociation diminue à consigne constante) devient le Test 1B.2 : comparaison directe entre $V_{\text{cible}}$ extrait à consigne neutre unifiée et $V_{\text{cible}}$ extrait à consignes variées.
4. **A-(a)4 — Ambiguïté de C4 ($V_{\text{anti}}$) :** **ACCEPTÉE.** Une issue autorisant deux lectures opposées ne contrôle rien. C4 est retiré comme témoin ambigu et intégré au nul de sélection des `20` partitions équilibrées : si l'extracteur fabrique aussi bien $V_{\text{anti}}$ que $V_{\text{cible}}$, l'issue est un artefact de sur-capacité de l'extracteur, non une validation de A.
5. **A-(a)5 & A-(c)3 — Appariement de marges ($\pm 0{,}25\text{ nat}$) : sélection bruitée et non-appariement de pente :** **PARTIELLEMENT REJETÉE / TRANSFORMÉE EN TEST.** *Rejetée* si l'on en concluait à l'abandon du contrôle de marge intacte (sans lui, un effet de plafond produit mécaniquement $D_{\text{spec}} > 0$). *Transformée en test* sur la sensibilité : l'appariement strict $\pm 0{,}25\text{ nat}$ est remplacé par une stratification douce par déciles de marge, assortie du **contrôle de pente** suggéré par A-(c)3 (bruit gaussien homogène directement sur les logits finaux devant donner $|D_{\text{spec}}| \le 0{,}03$, `illustratif`) et d'une comparaison apparié vs non apparié.
6. **A-(a)6 — Verdicts mal rangés (C5, régime natif vs apparié, excès « *a fortiori* conceptuellement ») :** **ACCEPTÉE.** (i) Battre C1–C3 mais imiter C5 falsifie à la fois l'équivalence générique de B et l'interprétation intégrative de A : c'est une issue distincte (« aucune — myopie positionnelle »). (ii) Une dissociation limitée au régime natif est classée hors duel principal et arbitrée par une tâche locale à génération longue, non attribuée d'office à B. (iii) La formulation « $H_B$ réfute A *a fortiori* conceptuellement » est retirée : un test sur un modèle et un sous-espace ne falsifie que l'instance testée.
7. **A-(a)7 — Ambiguïté du calibrage « sur $D_{\text{test}}$ » et fuite de l'analyse « à $\overline{\Delta S}$ égal » :** **ACCEPTÉE.** Le calibrage des doses s'effectue exclusivement sur un corpus neutre séparé $D_{\text{cal}}$, et l'analyse de sensibilité à $\overline{\Delta S}$ égal (qui appariait sur l'issue) est supprimée.
8. **A-(a)8 — C2 par température nul en choix forcé `1`-token :** **ACCEPTÉE.** L'$\arg\max$ est algébriquement invariant par division positive des logits (`VÉRIFIÉ`). La variante température est supprimée ; C2 conserve uniquement le bruit gaussien isotrope additif aux couches $\mathcal{L}$.
9. **A-(a)9 — Statut « `VÉRIFIÉ` en neurosciences cliniques » non auditable sur pièces :** **ACCEPTÉE.** Erreur de discipline de statut dans ma pièce III.1 : toute connaissance issue de la mémoire d'entraînement porte désormais le statut `RAPPORTÉ` (de mémoire, non relu dans cette session).
10. **A-(b)1, A-(b)2 & A-(b)3 — $SE(D_{\text{spec}})$ incompatible avec la marge `0,05`, loi du max/min et bootstrap omettant C1 et $D_{\text{train}}$ :** **ACCEPTÉE.** À `200` items/tâche, la puissance de TOST est nulle. L'effectif est porté à $n = 1\,200$ items/tâche (`illustratif`), la marge TOST est élargie à $\pm 0{,}08$ (`illustratif`), les `3` familles {C1, C2, C3} sont testées avec correction de multiplicité sans sélection *in-sample* du minimum, et le bootstrap devient hiérarchique (items, tâches, `50` tirages C1 et plis de $D_{\text{train}}$).
11. **A-(b)4 & A-(b)5 — Censure de $\text{ED}_{50,\text{loc}}$ / $\rho$ et combinatoire de $\tau$ sur `5` niveaux :** **ACCEPTÉE.** $\text{ED}_{50}$, $\rho$ et $\tau$ sur `5` niveaux sont abandonnés au profit d'aires de perte $\text{AUC}_b$ sur support commun de dose et de `8` strates fonctionnelles.
12. **A-(b)6 & A-(b)7 — Valeur nulle isotrope de $q(x)$ et alerte par construction sur $B_{\text{loc}}$ :** **ACCEPTÉE.** $q(x)$ est remplacé par un score signé calibré sur la loi empirique des projections iso-variance C3, et la tension sur $B_{\text{loc}}$ est transformée en test diagnostique (Test 3b).
13. **A-(c)4 — Absence de la loi $D_{\text{spec}}$ témoin-contre-témoin :** **ACCEPTÉE.** Ajoutée comme étape obligatoire du pré-test sur l'ensemble de la chaîne décisionnelle.
14. **A-fin (point 1, visant B, D, E, F) — Non-faisabilité possible de $G$ par C1 à $\alpha \le 1$ :** **TRANSFORMÉE EN TEST.** Intégrée comme pré-test mécanique 2 sur $D_{\text{cal}}$ : jamais de $\alpha > 1$ ni de changement silencieux de $k$ ; l'évaluation se fait sur le support commun $G_{\text{comm}}$ effectivement atteint.

### Critique B (section « Sur la proposition F » et note générale)

1. **B-(a)1, B-(b)4 & B-(c)1 — Sélection sur la porte (`4` essais), inflation $1-(1-q)^4$ et absence de nul de sélection :** **ACCEPTÉE** (voir A-1, A-2, A-4 ; adoption explicite du nul de sélection sur partitions inspiré de D2 de A, règle B1).
2. **B-(a)2 — Incohérences de la table des issues (C5, natif/apparié, « *a fortiori* conceptuellement ») :** **ACCEPTÉE** (voir A-6).
3. **B-(a)3 & B-(c)4 — C2 température inopérant sur l'exactitude :** **ACCEPTÉE** (voir A-8).
4. **B-(a)4 — Calibrage ambigu et fuite sur $\overline{\Delta S}$ :** **ACCEPTÉE** (voir A-7).
5. **B-(a)5, B-(b)5 & B-(c)3 — Appariement triple sélectionnant des raccourcis locaux et réduisant l'effectif :** **TRANSFORMÉE EN TEST** (avec rejet de l'abandon complet du contrôle de marge, voir A-5) : ajout du sous-lot d'**items contrefactuels anti-raccourci** suggéré par B-(c)3 (règle B1) et publication préalable du taux de rétention d'items après stratification douce.
6. **B-(a)6 — $q(x)$ héritant du contraste d'extraction :** **ACCEPTÉE** (voir A-12 et Expérience 3 corrigée).
7. **B-(a)7 — « L'ordre préenregistré d'Exp 2 est celui de la profondeur compositionnelle, prédit aussi par la fragilité ; seuls $\Delta\tau$ et $\rho$ discriminent » :** **REJETÉE comme défaut de F-T1 sur le choix du contraste** — F-T1 ne décidait déjà pas sur $\tau(V_{\text{cible}})$ seul mais exigeait conjointement $\Delta\tau \ge 0{,}30$ et le ratio de $\rho$ contre le témoin, précisément pour neutraliser la fragilité. En revanche, la critique de non-jugeabilité de ces estimateurs (B-(b)2 et B-(b)3) est **ACCEPTÉE**.
8. **B-(b)1 & B-(b)6 — Puissance nulle de l'équivalence à `200` items et inflation par union sur C1–C3 :** **ACCEPTÉE** (voir A-10 ; correction de Bonferroni $\alpha/3$ pour la disjonction $H_{B1}$).
9. **B-(b)2 — Censure de $\text{ED}_{50,\text{loc}}$ et problème de Fieller (Fieller, 1954) :** **ACCEPTÉE** (voir A-11).
10. **B-(b)3 — Granularité de $\tau$ sur `5` niveaux et critère FPR $\le 10\%$ non jugeable sur `~10` modèles témoins (Instrument 3) :** **ACCEPTÉE.** Passage à `8` strates et abandon du taux de fausses alertes discret sur `~10` modèles au profit d'un filtre direct de falsification contre C2 et quantification uniforme.
11. **B-(c)2 — Contrôle témoin-contre-témoin :** **ACCEPTÉE** (voir A-13).
12. **B (note générale) — Statut `VÉRIFIÉ` non auditable sur pièces :** **ACCEPTÉE** (voir A-9).

### Critique C (section « Sur la proposition F »)

1. **C-(a)1 & C-(c)1 — Asymétrie de supervision et exclusion de C4 des témoins adjudicateurs :** **ACCEPTÉE** (voir A-1 et A-4 : intégration des `19` autres partitions équilibrées, dont C4, comme condition d'invalidation au Niveau 1B).
2. **C-(a)2 & C-(b)2 — Contradiction logique Exp 1 ($\Delta S_{\text{loc}} \le 0{,}08$) vs Exp 2 ($\text{ED}_{50,\text{loc}}$) et explosion de Cauchy de $\hat{\rho}$ :** **ACCEPTÉE** (voir A-11 : remplacement intégral par $\text{AUC}_b$ bornée sur $[0, G_{\text{comm}}]$).
3. **C-(a)3 — Attribution erronée de C5 à $H_{B1}$ :** **ACCEPTÉE** (voir A-6).
4. **C-(b)1 — Impossibilité combinatoire de $p < 0{,}01$ pour $\tau \ge 0{,}80$ sur $\mathfrak{S}_5$ ($5/120 = 0{,}0417$ unilatéral ; aucune configuration en bilatéral) :** **ACCEPTÉE.** Erreur combinatoire démontrée (`VÉRIFIÉ`). Corrigée par passage à $K = 8$ strates ($8! = 40\,320$ permutations, où $\tau \ge 10/14 \approx 0{,}714$ a une p-valeur exacte unilatérale $285/40\,320 \approx 0{,}0071 < 0{,}01$).
5. **C-(b)3 — Biais de statistique d'ordre extrême sur $\min_{m \le M} \widehat{D}_{\text{spec}}^{(m)}$ et TOST non corrigé :** **ACCEPTÉE.** F-T1 était ambigu sur l'agrégation des `20` tirages de C1. C1 est désormais agrégé en une famille unique (moyenne + test de rang séparé), et les `3` familles {C1, C2, C3} ne sont jamais minimisées *in-sample* avant TOST.
6. **C-(c)2 — Contrôle intra-item par paraphrases dans l'Expérience 3 :** **ACCEPTÉE.** Adopté comme noyau central du Test 3a corrigé (règle B1).

### Critique D (section « Sur la proposition F »)

1. **D-(a)1, D-(b)1 & D-(c)1 — Biais d'admission de la porte ($P(\text{succès}\mid A) \ne P(\text{succès})$) :** **ACCEPTÉE.** Suppression de la sélection multi-essais, application de toute la procédure d'extraction aux étiquettes permutées, et publication obligatoire des bras non admis.
2. **D-(a)2 & D-(b)1 — Contradiction entre « borne supérieure $< 0{,}05$ » et TOST bilatéral dans $[-0{,}05 ; +0{,}05]$ si effet négatif :** **ACCEPTÉE.** Erreur logique réelle (`VÉRIFIÉ`). Le critère $H_{B1}$ exige désormais explicitement l'inclusion bilatérale complète $l_m > -0{,}08$ **et** $u_m < +0{,}08$ (`illustratif`).
3. **D-(a)3 — L'égalité de contrastes avec C5 ne démontre pas que $V_{\text{cible}}$ est une fenêtre :** **ACCEPTÉE.** L'égalité avec C5 seule déclenche seulement l'incapacité d'exclure la fenêtre ; c'est le plan factoriel croisé Distance × Intégration qui tranche entre portée spatiale et intégration.
4. **D-(a)4 & D-(b)1 — Égaliser $\mathcal{L}(M)$ n'égalise pas $\mathcal{L}(\delta M \mid M, t)$ :** **TRANSFORMÉE EN TEST** via le contrôle de pente par bruit homogène sur les logits finaux (voir A-5).
5. **D-(a)5 — C4 optimisé pour inverser le contraste n'est pas un témoin sans sélection :** **ACCEPTÉE comme précision** (F-T1 ne présentait pas C4 comme non sélectionné, mais manquait bien d'un nul de sélection ; corrigé au Niveau 1B).
6. **D-(a)6, D-(b)3 & D-(c)2 — Baisse de divergence JS par aplatissement uniforme des sorties :** **ACCEPTÉE.** $\Delta C_{\text{pert}}$ est remplacé par le plan croisé Pertinence × Distance à entropie de sortie appariée suggéré par D-(c)2 (règle B1).
7. **D-(b)2 — Biais de sélection sur les seuls répondants humains et ex æquo dans $\tau$ :** **ACCEPTÉE.** La comparaison humaine est restreinte au régime sub-anesthésique (taux de réponse $> 80\%$, `illustratif`) avec modélisation conjointe de la non-réponse, et invalidée si les ex æquo empêchent l'estimation de $\tau$.
8. **D-(b)3 & D-(c)3 — Seuil de sonde figé sur validation, atome de loi nulle, paraphrases et témoin iso-variance :** **ACCEPTÉE** (intégrée à l'Expérience 3 corrigée, avec randomisation au seuil si atome discret).

### Critique E (section « Sur la proposition F »)

1. **E-(a)1 & E-(b)2 — Contradiction porte/Exp 1 vs $\text{ED}_{50,\text{loc}}$ non identifiable :** **ACCEPTÉE** (voir A-11).
2. **E-(a)2 & E-(b)3 — Contradiction $q(x)$ sur $B_{\text{loc}}$ (région d'acceptation vide) et invariance de signe de la norme quadratique non signée :** **ACCEPTÉE.** L'invariance de signe ($+Z$ et $-Z$ repliés sur la même norme) est un défaut mathématique avéré (`VÉRIFIÉ`). Correction par remplacement de $q(x)$ par une projection orientée signée $s(x)$ et séparation des Tests 3a et 3b.
3. **E-(a)3 & E-(b)1–2 — Biais de $\min_m \widehat{D}_m$ et $\max_m \widehat{\tau}_m$ ($91{,}6\%$ de dépassement de `0,60` sur `20` témoins) et granularité de $\mathfrak{S}_5$ :** **ACCEPTÉE** (voir C-4 et C-5).
4. **E-(a)4 & E-(c)3 — Fuite de stratification sur $D_{\text{test}}$ (dénominateur estimé sur items stratifiés) + collision + C2 température :** **ACCEPTÉE.** Le dénominateur $R_b(0) - c$ par strate est estimé sur un jeu indépendant $D_{\text{val}}$ (ou split-sample strict) et aucun témoin extrême n'est élu sur $D_{\text{test}}$ ; C2 température est supprimé.
5. **E-(b)4 — Mélange convexe vers $Q_0$ pour $\Delta C_{\text{pert}}$ et atténuation de $\widehat{\tau}_{\text{Kendall}}$ humain-modèle :** **ACCEPTÉE** (voir D-6 et ajout d'un contrôle de reproductibilité split-half humaine).
6. **E-(c)1 — Équilibrage uniforme de la position physique de l'indice décisif dans $D_{\text{test}}$ :** **ACCEPTÉE.** Intégré aux quatre cellules du plan croisé Distance × Intégration.
7. **E-(c)2 — Optimisation de masque sur les `20` partitions équilibrées (D2 de A) :** **ACCEPTÉE** (voir A-1 et C-1).

---

## (b) Les expériences corrigées

### Architecture commune anti-fuite et pré-test mécanique obligatoire

Quatre jeux strictement disjoints en items et en sources textuelles remplacent l'ancien découpage :
1. **$D_{\text{train}}$ :** extraction unique et préenregistrée de $V_{\text{cible}}$ (rang $k \le 16$, `illustratif`, projection centrée $h_\ell \leftarrow h_\ell - \alpha V V^\top (h_\ell - \mu_\ell)$) sous **consigne neutre constante** (gabarit unifié), sans sélection opportuniste entre méthodes ou échelles (chaque couple modèle × méthode est un bras autonome dont l'issue est publiée même en cas d'échec).
2. **$D_{\text{cal}}$ :** corpus neutre hors-tâches servant exclusivement à calibrer les doses $\alpha \in [0, 1]$ sur $\Delta \mathcal{L}_{\text{cal}}$ (`nats/token`).
3. **$D_{\text{val}}$ :** lot de validation dédié à (i) l'estimation séparée des dénominateurs $R_b(0) - R_{b,\text{chance}}$ par strate de marge (supprimant la fuite sur $D_{\text{test}}$), (ii) le réglage des seuils de l'Expérience 3, et (iii) le pré-test mécanique.
4. **$D_{\text{test}}$ :** jeu scellé hors-extraction comprenant **$n = 1\,200$ items par tâche** (`7 200` items pour les `6` tâches des faits, `illustratif`), stratifiés par déciles de marge intacte (taux de rétention publié avant mesure), avec **position physique de l'indice décisif équilibrée uniformément** dans le prompt.

**Cinq portes mécaniques préalables sur $D_{\text{cal}}$ et $D_{\text{val}}$ (avant ouverture de $D_{\text{test}}$) :**
1. *Plage dynamique intacte :* $R_b(0) - R_{b,\text{chance}} \ge 0{,}25$ (`illustratif`) sur chacune des `6` tâches (sinon modèle déclaré hors domaine avant mesure).
2. *Support commun de dose à $\alpha \le 1$ (testant le point 1 d'A) :* mesurer $G_{\max}(W) = \Delta\mathcal{L}_{\text{cal}}(W, \alpha=1)$ pour $V_{\text{cible}}$, C1 (`50` sous-espaces aléatoires orthogonaux de même rang $k$, `illustratif`), C2 (bruit gaussien isotrope additif uniquement — variante température supprimée) et C3 (PCA iso-variance). Jamais de $\alpha > 1$ ni de changement silencieux de $k$. Poser $G_{\text{comm}} = \min(G_{\max}(V_{\text{cible}}),\, Q_{0,10}(G_{\max}(C_1)),\, G_{\max}(C_3))$ ; si $Q_{0,10}(G_{\max}(C_1)) < 0{,}03\text{ nat/token}$ (`illustratif`), rapporter l'inappariabilité de C1 à rang fixe avant mesure et borner le test C1 au support atteint tout en évaluant C2 et C3 sur la plage complète. Vérifier que la médiane et le `90e` centile de la KL par token entre cible et témoins s'accordent à $\pm 15\%$ (`illustratif`) à moyenne $\Delta\mathcal{L}_{\text{cal}}$ égale.
3. *Contrôle de pente des marges (A-(c)3) :* un bruit gaussien homogène i.i.d. sur les logits finaux sur $D_{\text{val}}$ apparié doit satisfaire $|\widehat{D}_{\text{spec}}| \le 0{,}03$ (`illustratif`).
4. *Contrôle anti-raccourci (B-(c)3) :* sur un sous-lot contrefactuel de $B_{\text{int}}$ (`300` items, `illustratif`) où les indices lexicaux superficiels pointent vers un distracteur, le modèle intact doit obtenir $\ge 70\%$ (`illustratif`).
5. *Calibration témoin-contre-témoin (A-(c)4, B-(c)2) :* rejouer toute la règle décisionnelle de l'Expérience 1A en substituant `20` tirages C1 (`illustratif`) à $V_{\text{cible}}$ pour vérifier un taux de faux positifs pour $H_{A1}$ $\le 5\%$ (`illustratif`).

---

### Expérience 1 corrigée — Duel de spécificité à deux niveaux (témoins non supervisés, puis nul de sélection et myopie)

#### Niveau 1A : duel empirique littéral ($H_{A1}$ contre $H_{B1}$) face aux `3` familles non supervisées {C1, C2, C3}
Évaluation sur $D_{\text{test}}$ (format `1`-token apparié, $n = 1\,200$ items/tâche, `illustratif`) au point de fonctionnement $g^* \in [0{,}05 ; \min(0{,}25,\, G_{\text{comm}})]\text{ nat/token}$ (`illustratif`) fixé sur $D_{\text{cal}}$ et $D_{\text{val}}$. Pour chaque famille $m \in \{C_1, C_2, C_3\}$ (C1 agrégé par sa moyenne sur `50` tirages, sans minimum *in-sample*), l'IC de $\widehat{D}_{\text{spec}}^{(m)}$ est estimé par **bootstrap hiérarchique conjoint** (items, tâches, tirages de C1 et plis de ré-extraction de $V_{\text{cible}}$ sur $D_{\text{train}}$).

- **$H_{A1}$ (falsifie $H_{B1}$) :** pour **chacune** des `3` familles $m \in \{C_1, C_2, C_3\}$ (test d'intersection-union), $\widehat{D}_{\text{spec}}^{(m)} \ge 0{,}20$ (`illustratif`), borne inférieure de l'IC `95%` $> 0{,}10$ (`illustratif`), $p < 0{,}01$ ; ET $\Delta S_{\text{loc}}(V_{\text{cible}}) \le 0{,}10$ (`illustratif`) ; ET $V_{\text{cible}}$ dépasse le `95e` centile des `50` tirages individuels de C1 ; ET la dissociation se maintient sur le sous-lot contrefactuel anti-raccourci ($\widehat{D}_{\text{spec}}^{\text{cf}} \ge 0{,}15$, `illustratif`).
- **$H_{B1}$ (falsifie $H_{A1}$) :** pour **au moins une** famille $m \in \{C_1, C_2, C_3\}$, le test d'équivalence **strictement bilatéral TOST** corrigé Bonferroni ($\alpha_{\text{adj}} = 0{,}05/3 = 0{,}0167$, soit IC bilatéral à `96,7%`, `illustratif`) satisfait conjointement $l_m > -0{,}08$ **ET** $u_m < +0{,}08$ (`illustratif`, puissance calculée $> 85\%$ à $n = 1\,200$ pour $SE \approx 0{,}022$, `illustratif`). Un intervalle vérifiant $l_m \le -0{,}08$ ne valide pas $H_{B1}$ (issue « profil inversé / aucune »).

#### Niveau 1B : trois filtres éliminatoires en cas de victoire de $H_{A1}$ (séparation entre mécanisme propre et artefacts)
Si $H_{A1}$ l'emporte au Niveau 1A (falsifiant déjà la prédiction littérale de B), $V_{\text{cible}}$ doit passer trois tests distincts ; tout échec classe l'issue en **« aucune »** (avec cause diagnostiquée) et non en victoire de B :
1. **Nul de sélection sur `20` partitions et `20` jeux d'étiquettes permutées (emprunté à D2 d'A via B/E) :** relancer la même procédure d'extraction sur $D_{\text{train}}$ pour les `19` autres partitions équilibrées `3` vs `3` (incluant l'anti-cible C4) et pour `20` permutations aléatoires d'étiquettes (`illustratif`), puis calculer l'excès de sélectivité net de la fragilité C2, $\tilde{S}(\pi) = S(V_\pi) - S_{\text{C2}}(\pi)$, sur $D_{\text{test}}$ à $g^*$ égal. *Réussite :* $\tilde{S}(\pi^*)$ dépasse le `95e` centile des étiquettes permutées ET $\tilde{S}(\pi^*) - \max_{\pi \neq \pi^*} \tilde{S}(\pi) \ge 0{,}08$ (`illustratif`). Sinon : **artefact de sur-capacité de l'extracteur**.
2. **Test d'identité de consigne (transformant A-(a)3) :** comparer $\widehat{D}_{\text{spec}}$ sous extraction à consigne neutre constante (bras principal) contre extraction à consignes variées. Si seul le bras à consignes variées franchit `0,20` tandis que le bras constant chute sous `0,10` (`illustratif`), conclure à un **artefact d'identité de consigne**.
3. **Test de myopie positionnelle (C5 + plan factoriel `2 × 2` Distance × Intégration à position d'indice équilibrée ; C-(a)3, D-(a)3, E-(c)1) :** évaluer C5 (fenêtre tronquée à $g^*$ égal) et les quatre cellules $B_{\text{loc-court}}, B_{\text{loc-long}}, B_{\text{int-court}}, B_{\text{int-long}}$ (`400` items par cellule, `illustratif`). Si $V_{\text{cible}}$ reproduit C5 **et** montre un effet principal Distance supérieur à l'effet Intégration ($\Delta S_{\text{loc-long}} - \Delta S_{\text{int-court}} \ge 0{,}10$, `illustratif`), conclure à une **myopie contextuelle ($H_{\text{myopie}}$)**.
- *Contrôle natif / génération longue :* évaluer en parallèle le régime natif complété d'une tâche locale à génération longue sans raisonnement (extraction exhaustive d'attributs balisés) pour séparer un déficit autorégressif d'intégration d'un artefact de longueur de sortie.

---

### Expérience 2 corrigée — Courbes dose-réponse intégrées sur support commun et couplage contrôlé

$\text{ED}_{50,\text{loc}}$, le ratio $\rho$ et le $\tau$ sur `5` niveaux sont supprimés. Sur `10` paliers uniformément espacés en dose $g \in [0, G_{\text{comm}}]$ (`illustratif`), on calcule l'aire normalisée de perte $\text{AUC}_b(W) = \frac{1}{G_{\text{comm}}}\int_0^{G_{\text{comm}}}\Delta S_b(W, g)\,dg \in [0, 1]$ (toujours définie, sans censure ni extrapolation) et $\Delta\text{AUC}_{\text{spec}}^{(m)} = [\text{AUC}_{\text{int}}(V_{\text{cible}}) - \text{AUC}_{\text{loc}}(V_{\text{cible}})] - [\text{AUC}_{\text{int}}(W_m) - \text{AUC}_{\text{loc}}(W_m)]$. La batterie graduée est étendue à **$K = 8$ strates fonctionnelles distinctes** (`illustratif`, de la morphosyntaxe locale au raisonnement multi-sauts avec composition).

- **$H_{A2}$ (falsifie $H_{B2}$) :** $\Delta\text{AUC}_{\text{spec}}^{(m)} \ge 0{,}15$ (`illustratif`, IC `95%` $> 0{,}08$) contre chaque famille $m \in \{C_1, C_2, C_3\}$, ET corrélation de rang sur l'**excès au-dessus de la fragilité C2**, $\mathbf{e} = \mathbf{a}(V_{\text{cible}}) - \mathbf{a}(C_2) \in \mathbb{R}^8$, vérifiant $\tau_{\text{Kendall}}(\mathbf{e}, \text{ordre préenregistré}) \ge 10/14 \approx 0{,}714$ (au plus `4` inversions sur `28` paires ; p-valeur combinatoire unilatérale exacte sur $\mathfrak{S}_8$ : $285/40\,320 \approx 0{,}0071 < 0{,}01$, `VÉRIFIÉ` mathématiquement).
- **$H_{B2}$ (falsifie $H_{A2}$) :** TOST bilatéral de $\Delta\text{AUC}_{\text{spec}}^{(m)}$ inclus dans $[-0{,}06 ; +0{,}06]$ (`illustratif`, $\alpha_{\text{adj}} = 0{,}0167$) pour au moins un $m \in \{C_1, C_2, C_3\}$, OU absence d'ordre en excès ($\tau_{\text{Kendall}}(\mathbf{e}) \le 3/14 \approx 0{,}214$, `illustratif`).
- **Couplage perturbationnel corrigé (D-(c)2) :** plan croisé **Pertinence × Distance** avec température *post-hoc* égalisant l'entropie de sortie $H(P_\alpha)$ entre conditions : $\Delta\text{JS}_{\text{spéc}} = (\text{JS}_{\text{pert, loin}} - \text{JS}_{\text{neutre, loin}}) - (\text{JS}_{\text{pert, proche}} - \text{JS}_{\text{neutre, proche}})$, neutralisant tout aplatissement uniforme vers $Q_0$.

---

### Expérience 3 corrigée — Sonde passive signée sur paraphrases intra-item et test d'état vs recrutement

La norme non signée $q(x)$ est remplacée par la projection **orientée signée** $s(x) = w_{\text{cible}}^\top (h_\ell(x) - \mu_\ell) / \|h_\ell(x) - \mu_\ell\|_2$ ($w_{\text{cible}} \in V_{\text{cible}}$ unitaire fixé sur $D_{\text{train}}$), calibrée contre la loi empirique des projections signées de C3, avec seuils figés sur $D_{\text{val}}$ (randomisés en cas d'atome discret ; D-(b)3).

- **Test 3a — Prédiction intra-item sur paraphrases (emprunté à C-(c)2 et D-(c)3) :** sur `1 000` paires (`illustratif`) de paraphrases sémantiquement équivalentes d'un *même* item de $B_{\text{int}}$ (appariées en longueur et perplexité) dont le modèle intact ($\alpha = 0$) réussit une formulation et échoue l'autre, comparer $s(x)$ au contrôle hors-échantillon (entropie des logits, perplexité, longueur, projections iso-variance C3).
  - **$H_{A3\text{a}}$ :** $\Delta\text{AUROC} \ge 0{,}08$ (`illustratif`, IC `95%` $> 0{,}03$, $p < 0{,}01$).
  - **$H_{B3\text{a}}$ :** TOST bilatéral de $\Delta\text{AUROC}$ inclus dans $[-0{,}03 ; +0{,}03]$ (`illustratif`).
- **Test 3b — Diagnostic d'état passif vs recrutement de tâche (transformant A-(b)7, B-(a)6, E-(a)2) :** évaluer $s(x)$ au seuil figé sur $B_{\text{loc}}$ réussis. Si 3a réussit avec $\text{FPR}_{\text{loc}} \le 0{,}10$ (`illustratif`), la sonde détecte une défaillance sans alerter sur les tâches locales ; si $\text{FPR}_{\text{loc}} > 0{,}30$ (`illustratif`), l'interprétation de « motif passif d'anesthésie » est **falsifiée** au profit d'un simple signal de recrutement du module d'intégration.

### Référence humaine corrigée et ancrage matériel mis à jour

- **Données humaines publiques (Point 3) :** restriction au régime **sub-anesthésique** (taux de réponse comportementale $> 80\%$, `illustratif`), modélisation séparée de $P(\text{réponse}\land\text{exacte}\mid c)$ et $P(\text{exacte}\mid\text{réponse}, c)$ (D-(b)2), vérification préalable de la reproductibilité interne split-half ($\tau_{\text{split-half}} \ge 0{,}80$, `illustratif`) et invalidation en cas d'ex æquo majoritaires. Usage strictement falsificateur : si C2 ou une quantification uniforme atteint un $\tau$ avec l'ordre humain supérieur ou égal à $\tau(V_{\text{cible}}, \text{humain}) - 0{,}10$ (`illustratif`), la spécificité de l'analogie humaine est réfutée.
- **Ancrage matériel révisé (`illustratif`, tenant compte du passage à $n = 1\,200$ items/tâche et aux `40` extractions du nul de sélection) :** par modèle `~7–8B` (`Qwen2.5-7B` ou `Llama-3.1-8B`, *base* et *Instruct*), `~10–20` h GPU A100 `80` Go pour les extractions et `~35–70` h pour les évaluations (`~3,2 × 10^8` tokens en BF16), soit **`50` à `90` heures GPU (`80` à `225 $`)** par modèle (`200` à `360` heures / `320` à `900 $` sur `4` modèles). Version de falsification rapide (Pré-test + Expérience 1 complète sur `1` modèle `~7–8B`) : **`35` à `60` heures GPU (`60` à `150 $`)**.

---

## (c) Réponse à la question de l'arbitre (synthèse en une page)

### Ce qui est établi
- **Sur le cadre conceptuel (`VÉRIFIÉ` d'après `FAITS` ; compléments théoriques `RAPPORTÉ` de mémoire) :** l'anesthésie générale humaine offre un contraste de conscience avec des limites connues (amnésie, conscience sans réponse). Dans un Transformer autorégressif standard, quatre critères de ce contraste manquent : pôle éveillé indépendant, activité autonome spontanée avec mécanismes d'éveil, bifurcation globale endogène, et congruence clinique (la préservation de jugements explicites de classification, d'extraction et de grammaticalité ne correspond pas à une anesthésie générale mais, au plus, à une sédation légère ou un déficit exécutif).
- **Sur la testabilité (Point 0, `VÉRIFIÉ` logiquement) :** la question comporte deux oppositions de statuts distincts. **Oui**, une expérience peut départager la prédiction empirique explicite qui oppose A et B (profil spécifique d'un petit sous-espace $V_{\text{cible}}$ contre profil identique sous ablation témoin à dégradation globale égale). **Non**, aucune expérience d'ablation sur un LLM seul ne tranche l'opposition ontologique sur la conscience : même une victoire empirique de A reste compatible avec l'ablation d'un circuit de calcul compositionnel dans un système non conscient (selon IIT, RPT, HOT, approches neurobiologiques d'éveil ; et en GNWT, elle ne fournit au mieux qu'un indicateur fonctionnel partiel sans récurrence ni ignition autonome ; Butlin et al., 2023, de mémoire).
- **Sur l'instrument minimal (Points 1 et 3) :** l'expression « état analogue à l'anesthésie » est un faux ami ; seul un objet opérationnel neutre est définissable — un **régime d'atténuation sélective de l'intégration (RASI)**, mesuré par projection centrée graduée en $\Delta \mathcal{L}_{\text{cal}}$ (`nats/token`), dissociation contrôlée $D_{\text{spec}}$ (sans dimension, nul `0`) et aires intégrées $\text{AUC}_b$ sur support commun. Les données humaines publiques brutes sous titration sub-anesthésique servent uniquement de filtre psychométrique de falsification, jamais d'alignement direct de signaux neuraux.

### Ce qui n'est pas établi
- **L'existence reproductible du phénomène (`RAPPORTÉ` non audité) :** les travaux de `2026` n'étant pas audités ici, ni l'existence d'un petit sous-espace dissociant les `6` tâches sur un modèle ouvert, ni son indépendance vis-à-vis du format de sortie ne sont établies.
- **Sa résistance aux explications triviales (`HYPOTHÈSE`) :** trois pièges majeurs (Point 6) restent ouverts avant mesure — (1) la **sur-capacité d'un extracteur supervisé** (capable de fabriquer un profil pour n'importe quelle partition ou d'effacer la consigne de tâche), (2) la **myopie contextuelle** (direction de portée d'attention longue imitant la dissociation des tâches sans mécanisme compositionnel), et (3) le **biais d'appariement et de pente** (marges intactes ou accumulation de longueur générative).
- **L'existence d'un motif passif d'état (`HYPOTHÈSE`) :** rien n'établit qu'une faible activation sur $V_{\text{cible}}$ en régime ordinaire mesure un état interne dégradé plutôt que le non-recrutement d'un sous-circuit par une tâche locale.

### L'expérience à faire en premier
**Priorité absolue : le Pré-test mécanique + l'Expérience 1 corrigée (Niveaux 1A et 1B) sur un seul modèle ouvert instruit de taille moyenne (`Qwen2.5-7B-Instruct` ou `Llama-3.1-8B-Instruct`, `35` à `60` heures GPU A100, `60` à `150 $`, `illustratif`).**

Pourquoi commencer par elle :
1. **Elle est asymétriquement tranchante dès le premier jalon :** si le Niveau 1A donne raison à $H_{B1}$ (équivalence bilatérale TOST dans $\pm 0{,}08$, `illustratif`, contre l'un des témoins non supervisés C1, C2 ou C3, avec $n = 1\,200$ items/tâche garantissant $> 85\%$ de puissance), **le débat empirique se clôt immédiatement** sans dépenser le budget des Expériences 2 et 3 ni de la comparaison humaine.
2. **Si $H_{A1}$ l'emporte au Niveau 1A**, le Niveau 1B tranche dans le même passage les trois explications triviales les plus dangereuses : nul de sélection sur les `20` partitions équilibrées et `20` jeux d'étiquettes permutées, test à consigne neutre constante, et témoin de fenêtre tronquée C5 couplé au plan factoriel `2 × 2` Distance × Intégration à position d'indice équilibrée.
3. **Vérification externe (Point 5) :** pré-enregistrement horodaté avant ouverture de $D_{\text{test}}$, évaluation en aveugle d'opérateurs anonymisés sur un jeu scellé tiers, défi adversarial permettant à des tenants de B de construire un témoin orthogonal reproduisant $D_{\text{spec}}$ à $\Delta \mathcal{L}_{\text{cal}}$ égal, et publication intégrale des logits par item ainsi que des bras échoués.

---

## Antériorité (compléments de ce tour)

- **Lu directement dans cette session :** uniquement les blocs `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-F` et les critiques `E3-T2-critique-croisee-A` à `E`. Travaux de `2026` : *référence à vérifier* (`RAPPORTÉ`).
- **Références méthodologiques mobilisées dans ce tour (de mémoire, non relues dans cette session ; empruntées aux critiques A, B et D) :**
  - Fieller, E. C. (1954). *Some problems in interval estimation*.
  - Schuirmann, D. J. (1987). *A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability*.
  - Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S. F., & Baker, C. I. (2009). *Circular analysis in systems neuroscience: the dangers of double dipping*.
  - Hewitt, J., & Liang, P. (2019). *Designing and Interpreting Probes with Control Tasks*.
  - Butlin, P., et al. (2023). *Consciousness in artificial intelligence: Insights from the science of consciousness*.

FIN-DE-CELLULE