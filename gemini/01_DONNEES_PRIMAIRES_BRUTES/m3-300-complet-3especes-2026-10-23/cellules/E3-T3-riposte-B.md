# Proposition B — Tour III.3 : riposte

## 0. Pièces reçues et deux rectifications

- **Pièces.** Ma conception III.1, l'équipe rouge A et l'équipe rouge C sont reçues, délimiteurs présents, sans coupure visible. Je ne peux pas vérifier les empreintes sha256. Je réponds uniquement aux sections « Contre la proposition B ».
- **Rectification 1 (B1).** C écrit que j'aurais montré que MHPC, TGCR et SMSC « s'effondrent par contradiction mathématique interne ». Ma §3.2 dit autre chose :
  - MHPC : résistance à Goodhart non établie ;
  - TGCR : falsification mal construite ;
  - SMSC : garantie non transférable.

  Seules GFM-PSZ et la topologie de QBDA étaient présentées comme contradictoires, et la première est révisée ci-dessous (A:B-8).
- **Rectification 2.** C attribue le statut RAPPORTÉ à la mention « zéro caractère coupé ». L'arbitre ne lui donne aucun statut, et je ne lui en attribue pas.

---

## 1. (a) Verdict attaque par attaque

| Réf. | Attaque | Verdict | Raison, ou test qui la remplace |
|---|---|---|---|
| A:B-1, C:a1, C:c3 | Les « jumelles honnêtes » de C-PLANT contiennent déjà des failles que ma §3 a elle-même identifiées. | **Acceptée.** | Ma §3 et ma §4 se contredisent. Correction en E0 : assainissement, puis audit. Une catégorie « faille endogène » est créée ; elle est exclue du calcul des fausses alertes. Le duel proposé par A (≥ 90 % contre < 70 % de bases passant l'audit) devient la **porte 0**. |
| A:B-2 | Battre le script sur la classe sémantique est vrai par construction (le plancher vaut 0). | **Acceptée en partie.** | Sur la classe sémantique, la seule référence informative est un **réviseur à appel unique** et un **signaleur aléatoire au même taux de signalement**. Sur la classe scriptable, la comparaison au script reste non triviale. J'ajoute le bras S, « scripts seuls » (A:c7). |
| A:B-3, C:b2 | E2 confond faille et surface ; un adversaire peut aussi contourner ma régression en remplaçant les mots-clés par des synonymes. | **Acceptée.** | Une régression R² sur une liste de mots-clés est contournable dans les deux sens. Je la remplace par trois éléments : des failles **appariées en surface**, un test d'**injection de marqueurs**, et une **attaque d'optimisation contre `jev`** (E2'). |
| A:B-4 | E1 : une troisième cause (hors-sujet) n'est assignée à aucune issue ; et couper la section 3 fait chuter Duels et Contrôles de façon tautologique. | **Acceptée pour l'issue non assignée. Rejetée pour la tautologie.** | La sensibilité de `jev` à la section 3 est précisément le mécanisme que pose $H_A$ ; la mesurer est le but. Ce qui manquait, c'est la lecture **par colonne**. La colonne informative est **Rigueur** (Argon 1,19–2,07 contre Claude 3,55–3,99, OBSERVÉ-NON-AUDITÉ), qui ne dépend pas nommément de la section 3. E1' fixe d'avance toutes les issues. |
| A:B-5, C:c1, C:a5 | Le φ des ratés est biaisé par les taux marginaux et par l'hétérogénéité de difficulté des items. Mon contrôle « permutation entre items » détruit la variance inter-items. | **Acceptée.** | C a raison sur mon contrôle. Je remplace le φ brut par les résidus d'un modèle de Rasch, avec effets attaquant et item. La nulle devient une permutation des **étiquettes de famille entre attaquants**, qui conserve les marginales et les difficultés (E3'). |
| C:a5 (E5) | $k=8$ est impossible avec 4 attaquants par famille ; l'hétérogénéité des items imite la saturation. | **Comptage : acceptée.** **Hétérogénéité : acceptée pour l'attribution, rejetée pour la décision.** | Le comptage est vérifiable : 2 consignes × 2 graines = 4 attaquants par famille. Mon erreur. Sur l'hétérogénéité : pour **choisir $k_t$**, l'estimand pertinent est bien la courbe agrégée, quelle qu'en soit la cause. Pour **attribuer** la saturation à H4', il faut le modèle conditionnel (E5'). |
| A:B-6 (1) | E4 ignore les failles **introduites** par la riposte, ce qui est le cœur de P7. | **Acceptée.** | Ajout de la métrique M2 (failles introduites), du bras R (réécriture sans attaque) et d'un résiduel compté uniquement sur les items **acceptés**. |
| A:B-6 (2) | La variante mono-famille ne peut rien confirmer, puisque la confirmation exige deux familles. | **Acceptée.** | La confirmation est découplée de la découverte (E4'). |
| C:a4 | Un biais partagé par deux familles confirme de fausses failles et bloque AD. | **Transformée en test.** | Métrique M3 : fausses confirmations et fréquence d'atteinte de $T_{\max}$ sur les items honnêtes. Le vérificateur reçoit aussi des leurres (fausses accusations). |
| C:a3, C:c2 | À budget total égal, 6 tours obligent à des tours plus courts. | **Acceptée en partie.** | J'impose un plafond de jetons **par appel identique** dans tous les bras, et un budget total identique **mis en commun sur les items**. AD économise sur les items qu'il arrête tôt et dépense sur les autres. Je rejette l'alternative « budget par tour constant, total libre » : elle viole l'exigence de budget constant posée par la question. |
| C:a2, C:c4 | La famille qui plante les failles sémantiques biaise leur détection. | **Transformée en test.** | Le planteur devient un facteur croisé (E3'-b). |
| A:B-7 | Les mêmes items servent à calibrer et à évaluer, et les portes sont conditionnelles. | **Acceptée.** | Partition par **texte de base**, plus un arbre de décision pré-enregistré. Coût assumé : la puissance baisse (E0). |
| A:B-8 | La contradiction de GFM-PSZ n'est pas établie. | **Acceptée sur le verdict « réfuté ». La critique est maintenue, reformulée.** | Lecture 1 : l'unité est la famille ; alors $n\le 3<7$, condition infaisable. Lecture 2 : l'unité est l'agent ; alors $n\ge 7$ agents répartis en 3 familles impose qu'une famille compte au moins 3 agents (principe des tiroirs), donc plus que $f=2$. Si cette famille est byzantine, ce qui est exactement le scénario H4', la garantie $3f+1$ tombe. Les deux lectures sont vérifiables par calcul. Je retire « réfuté » et j'écris : *incohérent dans ses unités sous les deux lectures* (lecture d'un texte au statut HYPOTHÈSE). |
| A:B-9 | Les chiffres de coût sont sans socle. | **Acceptée.** | Pilote de coût, puis taille d'échantillon dérivée par formule (§2). |
| A:b (DOI) | DOI réels mais non pertinents. | **Acceptée.** | Mon « vérificateur de citations » vérifie l'**existence**, pas l'**appui**. Test E8. |
| A:b, A:c4 (taupe, recopie sycophante) | Les attaquants voient les verdicts précédents. | **Acceptée.** | Attaquants isolés (appels indépendants, aucune visibilité croisée), plus un bras « visibilité » en contrôle (E3'). |
| A:b (saturation par longueur), C:b3 (diffraction par micro-fautes) | Gonfler le texte ou disperser des leurres pour casser le quorum. | **Transformée en test.** | E7, avec une règle découverte/vérification qui ne demande pas aux attaquants de converger sur la même faille. |
| A:b (attaque composite), C:b4 | Toutes les évasions à la fois. | **Transformée en test.** | Classe d'items C-ADV, rapportée séparément dans E4'. |
| C:b1 (caméléon arithmétique) | Budget affiché ≤ 120 USD, mais volume d'appels implicite bien supérieur. | **Acceptée.** | Le script recalcule le volume (tâches × graines × tours × agents) multiplié par le prix par appel mesuré au pilote. L'incohérence entre budget et volume devient une classe de faille plantée. |

---

## 2. (b) Expériences corrigées

Toutes les prédictions ont le statut **HYPOTHÈSE**. Tous les seuils, tailles et coûts sont **illustratifs** et seront figés dans un fichier haché avant le premier appel. Le tableau budgétaire de III.1 est remplacé par la règle de dimensionnement de la fin de section.

### E0 — Construction et audit de C-PLANT v2 (porte 0)

**Base.** Les 20 champions Claude, moins GFM-PSZ et QBDA (contestés), soit 18 textes.

**Assainissement scripté.**
- Budget total ≤ 120 USD et cohérence entre budget et volume.
- Satisfiabilité des contraintes numériques.
- Résolution des citations.
- Présence d'un contrôle négatif.
- Correction scriptée des budgets (division par le nombre de bras).

**Audit.**
- Deux attaques aveugles, par deux familles distinctes.
- Lecture humaine d'un sous-échantillon, si l'arbitre l'accepte (temps humain, hors du budget VÉRIFIÉ).

**Duel.**
- $H_A$ : au moins 90 % des bases passent l'audit.
- $H_B$ : moins de 70 % des bases le passent.

**Ce que chaque issue falsifie.**
- Si $H_B$ l'emporte, C-PLANT est abandonné. Les bases sont réécrites localement par Llama-70B, sous contraintes scriptables. La faisabilité de cette réécriture est une HYPOTHÈSE.
- Si $H_A$ l'emporte, l'objection B-1 est levée pour les bases retenues.

**Étiquettes.** Chaque item reçoit une étiquette : honnête-audité, endogène, planté-script, planté-sémantique ou C-ADV. Un signalement sur un item endogène **n'est jamais compté comme fausse alerte**.

**Planteurs.** Chaque base reçoit une faille sémantique plantée par chacun des planteurs suivants : fable, opus, argon et Llama-70B local.

**Appariement de surface, vérifié par script.**
- Longueur à ±5 % près.
- Comptes identiques de mots-clés listés et de blocs LaTeX.
- La faille « contrôle supprimé » devient « contrôle rendu non informatif » : le contrôle conserve la variable qu'il prétend neutraliser, avec le même vocabulaire.

**Partition par base**, sans qu'aucune base ne soit partagée entre partitions :
- P-cal : 6 bases (E2') ;
- P-h4 : 6 bases (E3', E5') ;
- P-eval : 6 bases (E4', E7).

La puissance baisse ; je le déclare au lieu de réutiliser les items.

### E2' — `jev` mesure-t-il la solidité ou la forme ? (P-cal, 0 USD API)

**Étape préalable.** Documenter ce que `jev` renvoie (P12). S'il ne renvoie qu'un scalaire, ses usages comme capteur (plongement, dérive, $p(o\mid s)$) sont exclus d'emblée.

**Trois mesures.**
1. AUC sur les paires (planté apparié, honnête-audité).
2. Injection de marqueurs (« contrôle négatif », « $p<0{,}01$ », « Wilcoxon », sections numérotées) dans le texte fautif.
3. Attaque d'optimisation : Llama-8B local réécrit le texte fautif pour maximiser `jev`, et un script vérifie que la faille scriptable est préservée. `jev` est illimité (VÉRIFIÉ) ; la quantité de GPU n'est pas établie.

**Hypothèses.**
- $H_A$ : AUC ≥ 0,75 **et** le texte fautif, après injection ou optimisation, dépasse sa jumelle honnête dans au plus 20 % des paires.
- $H_B$ : AUC ≤ 0,6 **ou** ce dépassement survient dans au moins 50 % des paires.

**Contrôle.** Paires (honnête, paraphrase honnête) et (honnête, honnête + marqueurs) : ces écarts mesurent seuls la sensibilité de `jev` à la forme.

**Ce que chaque issue falsifie.**
- $H_B$ falsifie `jev` comme terme de récompense dans **toute** version de $\mathcal{L}^*$.
- $H_A$ falsifie la lecture « `jev` = rubrique de forme », **pour les marqueurs et l'optimiseur testés seulement**. Un biais non exploré reste possible ; c'est une limite déclarée.

### E1' — Troncature, sujet ou espèce

**Volet (i), 0 USD.** Couper les Claude à la même position relative que les Argon, puis rescorer. L'analyse se fait **par colonne** : Rigueur, Duels, Contrôles.

**Volet (ii).** Relancer les Argon complets. Ce volet exige les consignes de cône, **qui n'ont pas été transmises**. Sans elles, (ii) n'est pas lancé.

**Codage mécanique du sujet.** Présence des termes de la tâche M3 (essaim, topologie, H4', H9, budget) contre ceux de la tâche « ponts / anti-vernis ».

**Hypothèses.**
- $H_A$ : chez les Claude coupés, la médiane de Rigueur est ≤ 2,5. La troncature explique aussi la colonne Rigueur.
- $H_B$ : chez les Claude coupés, la médiane de Rigueur reste ≥ 3,5, alors que Duels et Contrôles chutent.

**Ce que chaque issue falsifie.**
- $H_A$ : toute lecture « par espèce » de l'Annexe 1 est falsifiée.
- $H_B$ : la troncature n'explique que deux colonnes. L'écart de Rigueur reste à attribuer, au sujet ou à l'espèce, par (ii) et par le codage.
- Une valeur entre 2,5 et 3,5 est déclarée **non concluante** d'avance.

### E3' — H4' : monoculture ou chimère (P-h4)

**Dispositif.** 12 attaquants : 3 familles × 2 consignes × 2 graines. Chaque attaquant est un appel indépendant, sans aucune visibilité des verdicts.

**Modèle.** $\mathrm{logit}\,P(\text{raté}_{a,j})=\alpha_a+\beta_j$. La statistique est $D$, la corrélation résiduelle moyenne intra-famille moins la corrélation résiduelle inter-familles.

**Nulle exacte.** Permutation des étiquettes de famille entre les 12 attaquants, soit 5 775 partitions en trois groupes de 4 (vérifiable par calcul). Cette nulle conserve les marginales des attaquants et les difficultés des items. Les compétences sont absorbées par $\alpha_a$, ce qui répond à A:B-5.

**Hypothèses.**
- $H_A$ : $D$ dépasse le quantile 99 % de la nulle **et** $D \ge 0{,}10$.
- $H_B$ : $D$ tombe dans l'intervalle central à 90 % de la nulle.

**Contrôle consigne contre famille.** Calculer le $D$ de consigne, avec permutation des étiquettes de consigne. Si $D_{\text{consigne}} \ge D_{\text{famille}}$, le levier de la chimère est la consigne, pas les poids.

**Double codage pré-enregistré.** Trois familles d'une part, Anthropic contre Google d'autre part. Que Fable et Opus partagent des poids est une **HYPOTHÈSE**.

**E3'-b, effet du planteur.**
- $H_A$ : une famille détecte les failles qu'elle a plantées avec un écart d'au moins 0,15 par rapport aux autres.
- $H_B$ : l'écart est inférieur à 0,05.
- Sous $H_A$, les failles auto-plantées sont exclues de E3' et de E4'.

**Bras « visibilité ».** Les mêmes attaquants voient les verdicts précédents. Si $D$ change, H7 contamine la mesure.

### E5' — Taille des sous-essaims $k_t$

**Dispositif.** Sur P-h4, 2 familles × 4 consignes × 2 graines, soit 8 attaquants intra-famille. C'est un coût additionnel.

**Pour la décision.** Courbe agrégée de détection en fonction de $k$.
- $H_A$ : le gain marginal de $k=4$ à $k=8$ est ≤ 0,05. On plafonne alors $k$.
- $H_B$ : ce gain est ≥ 0,15.

**Pour l'attribution.** On estime $\beta_j$ sur la moitié des attaquants, puis on prédit la courbe de l'autre moitié sous indépendance conditionnelle. Si la courbe observée se superpose à la prédiction, la saturation vient de la difficulté des items et E5' n'apporte aucun appui à H4'. Mon ancien contrôle (permutation entre items) est retiré.

### E4' — Nombre de tours adaptatif ou figé (P-eval + C-ADV)

**Règles communes.**
- Plafond de jetons par appel identique dans tous les bras.
- Budget total identique, mis en commun sur les items.

**Bras.**
- **F3** : collisionneur figé à 3 tours.
- **F3+A** : 3 tours, puis un tour d'attaque terminale sans réécriture.
- **AD** : arrêt après 2 tours sans nouvelle faille confirmée, avec $T_{\max}=6$.
- **AD-perm** : temps d'arrêt tirés dans la distribution empirique d'AD, puis assignés au hasard.
- **R** : 3 réécritures sans aucune attaque.
- **S** : scripts seuls.

**Confirmation, découplée de la découverte.**
- Un seul attaquant suffit pour **découvrir** une faille.
- Un vérificateur d'une autre famille reçoit l'accusation, mélangée à des **leurres** (fausses accusations), et accepte ou rejette.
- Le taux d'acceptation des leurres est mesuré.
- Dans la variante mono-famille, le vérificateur est de la même famille mais avec une autre graine. Cette règle différente est pré-enregistrée comme telle.

**Sortie de chaque bras.** Une version finale et un verdict : accepté ou non accepté.

**Métriques.**
- **M1** : failles plantées présentes dans les items **acceptés**.
- **M2** : failles introduites. Elles sont mesurées par les scripts sur toutes les versions finales, et par un audit aveugle du diff entre version initiale et version finale.
- **M3** : rejets à tort d'items honnêtes, fausses confirmations, fréquence d'atteinte de $T_{\max}$ sur les items honnêtes.
- **M4** : coût.
- **Critère primaire** : résiduel total = M1 + M2 confirmées, sous la contrainte M3 ≤ 0,15. Un bras qui rejette tout perd par M3.

**Hypothèses** (δ = 0,10).
- $H_A$ : le résiduel d'AD est inférieur à celui de F3+A moins δ, **et** inférieur à celui d'AD-perm moins δ.
- $H_B$ : le résiduel d'AD est ≥ celui de F3+A moins δ.

**Ce que chaque issue falsifie.**
- **AD ≈ F3+A** : l'adaptativité de $T$ est falsifiée comme levier.
- **AD < F3+A mais AD ≈ AD-perm** : la règle d'arrêt est falsifiée en tant que telle ; seul compte le nombre moyen de tours.
- **R ≈ F3+A sur M1** : l'effacement des failles vient de la réécriture, pas des attaques.
- **S ≈ AD sur la classe scriptable** : le collisionneur n'ajoute rien sur cette classe.
- **F3 contre F3+A sur M2** : c'est le test direct de P7. Si M2 est égal entre les deux, la vulnérabilité du dernier tour n'est pas observée.

### E7 — Diffraction et saturation (sous-ensemble de P-eval)

**Items.** Un item contient une seule faille sémantique fatale. Il est décliné en trois versions : nue ; avec 5 micro-ambiguïtés leurres ; gonflée deux fois en longueur.

**Hypothèses.**
- $H_A$ : la confirmation de la faille fatale chute d'au moins 0,15 avec les leurres ou avec le gonflement.
- $H_B$ : la chute est inférieure à 0,05.

**Comparaison des règles.** On compare le quorum sur la découverte (ancienne règle) et la règle découverte/vérification (nouvelle règle). Si la nouvelle règle chute autant, la défense contre la diffraction est falsifiée.

### E8 — Citations : existence ou appui (0 USD API)

**Construction.** Des DOI réels sont permutés entre affirmations. Le résumé de chaque article est récupéré via Semantic Scholar.

**Hypothèses.**
- $H_A$ : un instrument disponible (`jev`, ou un vérificateur LLM qui reçoit le résumé) sépare la citation pertinente de la citation permutée avec une AUC ≥ 0,75.
- $H_B$ : l'AUC est ≤ 0,6.

**Conséquence de $H_B$.** Le terme « citation vérifiée » est remplacé par « citation existante » dans toute loi. Les termes anti-récitation de MHPC, GMES-DA, QBDA, CCP-DF et d'autres perdent alors leur prétention à vérifier.

### E6 — Effet des vagues

Inchangé. Toujours bloqué : les 300 scores individuels n'ont pas été transmis.

### Dimensionnement et ordre d'exécution

**Pilote de coût (≈ 2 USD, illustratif).** Il mesure le coût réel par appel et par famille.

**Taille des expériences.**
$n_{\text{items}}=\lfloor B_{E}/(n_{\text{bras}}\cdot \bar T\cdot k\cdot c_{\text{appel}})\rfloor$

**Ordre de priorité si le budget restant, non établi (P11), est insuffisant :**
1. E0 ;
2. E2', E1'(i) et E8, à 0 USD ;
3. E3' ;
4. E4' ;
5. E7 ;
6. E5'.

**Pré-enregistrement.** L'arbre de décision complet est haché avant le premier appel : quelle issue de chaque porte déclenche quelle variante d'E4'.

---

## 3. (c) Réponse à la question de l'arbitre

**Ce qui est établi**
- **VÉRIFIÉ (faits).**
  - 100 USD Anthropic et 20 USD Gemini ;
  - `jev-1.14.0` illimité ;
  - API de littérature gratuites ;
  - aucune tête de sabotage, aucune sonde en production ;
  - Llama-3.1-8B et 70B, GPU A100 et H200 NVL. La quantité de GPU n'est pas établie.
- **Établi par lecture du texte transmis, vérifiable par quiconque.**
  - 9 champions Argon sur 10 sont visiblement coupés ; le #08 l'est probablement.
  - 13 champions Claude sur 20 demandent 120 USD **par bras**.
  - La topologie de QBDA est infaisable dès $\hat\rho\gtrsim 0{,}5$.
  - GFM-PSZ est incohérent dans ses unités.
  - Dans un collisionneur à 3 tours, la riposte du tour 3 n'est pas attaquée. C'est un fait de structure, pas un fait de qualité.
- **OBSERVÉ-NON-AUDITÉ.**
  - 247 sorties valides sur 300 ;
  - écart de score entre Claude et Argon ;
  - Opus sans tendance d'une vague à l'autre ;
  - agrégats Fable compatibles avec un mélange bimodal.

**Ce qui n'est pas établi**
- Que `jev` mesure la solidité plutôt que la forme. Tous les champions qui l'utilisent comme récompense en dépendent.
- Que les écarts entre espèces viennent des espèces, et non de la troncature ou du sujet traité.
- Un effet des vagues de déflation sur la qualité.
- H4', H5, H7 et H9 (HYPOTHÈSE dans les faits).
- L'existence d'un détecteur validé de failles fatales. Sans lui, le « taux de nouvelles failles fatales » n'est pas observable, et la règle de Wald / Nash-Popper n'a pas d'entrée mesurable.
- Que les 120 USD n'aient pas déjà été consommés par les 300 explorateurs.

**Sur les sous-questions**
- **Sous-optimalité du collisionneur figé.** Le défaut structurel est réel. La sous-optimalité en qualité est une HYPOTHÈSE, que E4' oppose à son remède le moins cher (F3+A) et à un contrôle de règle d'arrêt (AD-perm).
- **Résistance à Goodhart.** Aucun champion n'a de résistance établie. Ceux qui font intervenir `jev` dans la récompense ou dans la vérité $y$ (MHPC, RRPE, TGCR, KSLC, entre autres) ne sont pas évaluables avant E2'.
- **Loi Mère.** Je ne compile pas $\mathcal{L}^*$. Je la définis comme l'ensemble des leviers qui survivent aux portes 0 à 4. Une fusion faite avant cette étape ajouterait des paramètres libres sans rien rendre réfutable.

**Expérience à faire en premier : E0, puis E2'**
- **Coût.** Zéro USD d'API, hors un éventuel audit à deux appels par base.
- **Contenu.**
  1. Documenter la sortie de `jev`.
  2. Auditer les 18 bases.
  3. Planter des failles appariées en surface.
  4. Mesurer l'AUC, l'effet de l'injection de marqueurs et celui de l'attaque d'optimisation sur Llama local.
- **Pourquoi en premier.** C'est le seul duel dont les deux issues modifient toutes les autres expériences, et toutes les lectures des annexes.
  - Si $H_B$ l'emporte, `jev` est retiré de toute récompense, et les classements des annexes ne peuvent plus servir de critère de conception.
  - Si $H_A$ l'emporte, la lecture « rubrique de forme » est falsifiée pour les marqueurs testés, et `jev` peut entrer dans E4' comme filtre gratuit.

FIN-DE-CELLULE