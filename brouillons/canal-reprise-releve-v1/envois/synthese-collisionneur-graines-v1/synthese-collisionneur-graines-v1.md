# Synthèse du collisionneur « graines de plus pour le pilote 4 » (v2.6, étage III, deux tours) — v1

Fichier écrit le 2026-10-26 à 05:27:02 (heure universelle, lue sur `date -u` dans la commande même d'écriture), pour Lazar, par un
sous-agent neuf exécutant `BRIEF-synthese-graines-v1.md` (`9558d6f5…`, vérifiée). Pièces : `/var/tmp/fournis-synthese-graines-v1/`,
tour `run-graines-pilote4-q3-e3t1-v1` (cinq cellules valides sur six, 4,16 dollars). Empreintes vérifiées une à une : les cinq
cellules contre leurs compagnons et contre `EMPREINTES-v1.txt`, ce fichier contre son compagnon, la question v3 (`0b9bbfb3…`)
et le LISEZMOI contre `EMPREINTES-v1.txt` : tout concorde. Lu en entier : brief, question v3, LISEZMOI, registre, les cinq
cellules. A = Claude Fable 5.1, B = Claude Opus 5.5, C = Gemini 4 Argon ; « A F2 » = faille 2 de l'attaque A (III.2), « A CN1 »
= son contrôle 1, « C-1 » = faille 1 de l'attaque C, « C-c1 » = son contrôle 1, « B A-F4 » = faille 4 de l'attaque B contre A ;
« lignée B » désigne, comme dans la question, l'instance qui a écrit le calcul, non le modèle B. **Opus a refusé au III.1** (consigné tel quel, non fourni, rien n'en est supposé). **Deux
tours, aucune riposte** : un constat de l'équipe rouge n'est ni établi ni réfuté. **Aucun score du pilote 4 n'existe.**
Chiffres illustratifs sauf calcul explicite cité ; références à vérifier ; rien d'opposable. Écrite par **le même modèle que
A** (non que B, contrairement au brief) : biais de proximité possible envers A.

## 1. En trois lignes

**Convergent (A, C).** Depuis la v3 (un objet, deux questions), des graines sur la banque v3 n'achètent aucune comparaison
d'objets, seulement σ (part « course » du bruit) et une base pour la boucle de conception ; « (a) = deux courses nulles à
R = 3 » (A § 1, repris par B) ; cinq graines est dominé ; quand σ domine, doubler la banque n'achète presque rien, seul R
compte ; geler (b) avant tout score, compter par empreinte d'objet, entrelacer, déclarer le lot (A § 4, C § 4).

**Divise.** A : à R = 3, σ ne se mesure pas (intervalle à 95 % sur σ² d'un facteur ≈ 150, calcul explicite, A4) ; donc une
graine de plus par question, faits mécaniques d'abord (D-1), ou attendre (b). C : R = 3 « décisif » pour protéger la boucle ;
+2 courses sur M seule (D2) ou (a) ; modèle mixte, règle trivaluée à 80 %, formule σ̂ → palier 1 de (b). Modèle de la
question : inadapté au gain intra-course (R − 1 degrés de liberté) selon C, juste pour deux objets selon A.

**Équipe rouge, sans riposte.** Cassé : les duels mécaniques des deux (compteurs ≠ divergence fonctionnelle, C-2 ; faits
mécaniques = résumé des scores de `test`, A F4) ; les seuils de C (« stable » à tort ≈ 0,30 selon A F2, ≈ 0,21 selon B C-F3,
à σ = 0,05 ; bande du rapport F rejetant l'invariance vraie ≈ 0,35, A F3, B C-F6) ; les règles séquentielles (C-1, A F13,
B C-F7) ; la clause de A et la formule de C vers (b) (B A-F4, A F11, B C-F9) ; le lot de la graine 1 (A F9, C-6). Debout :
« courses nulles », bornes du chi-deux, McNemar aveugle au bruit de graine, gel de (b) ; et une convergence que B rend
réfutable : les deux veulent dimensionner (b) sur un σ̂ à 2–4 degrés de liberté d'un seul objet.

## 2. Par point de la question

**1. Achat.** A § 1 : σ, non ρ, pour savoir si (b) doit prévoir son palier 2 d'office ; R = 3 distingue 0 de 0,15, non 0,02
de 0,05. C § 1 : R = 1 « dangereux si σ ≥ 0,04 », R = 3 « décisif » ; huit courses sur v3 valent moins que la même somme dans
(b). Attaques : B A-F4 (σ̂ de la v6.2.1 ne dit rien de la v5.3, autre bras de (b)) ; A F8 (« décisif » contredit par la
puissance de 25–35 % que C calcule). Survit : σ pour la boucle, grossier à 2–4 degrés ; transfert : hypothèse non testable.

**2. Règle de lecture.** A § 2 : trois cases recalculées, concordantes ; 2R − 2 juste ; appariement déjà soustrait ; aucun
test entre graines, σ̂ avec intervalle chi-deux. C (a).1, (c).3, § 2 : le gain intra-course appelle R − 1, apparié, sans √2 ;
modèle mixte croisé, règle tenue/éliminée/indécidable à 80 %. Attaques : A F1, B C-F2 (C se contredit sur l'appariement) ;
B C-F8 (le ρ̂ de C n'est pas le ρ de la formule) ; B C-F5 (80 % est un degré de liberté d'analyse) ; B A-F3, C-3 (la grille
d'étalonnage de A est vraie par construction) ; A F10 (composante graine tronquée à zéro). Survit : formule juste pour deux
objets sur banque fixe, inadaptée au gain g0 → g3 (non contesté) ; à R = 3, aucun test bilatéral à 0,05 par permutation.

**3. Autres dessins.** A § 3 : D-1 (+1 graine par question, 3ᵉ si divergence mécanique), attendre (b), courses courtes si la
divergence naît avant les générations, graines pour la boucle = (c) déguisé. C § 3 : D2 (+2 sur M), D3 (+1 par question),
une graine par version corrigée, courses tronquées déconseillées, D1 séquentiel sur score. Attaques : contre D-1, C-1 (arrêt
conditionnel à un indicateur corrélé aux scores : σ̂ biaisé), C-2 et B A-F1 (compteurs ≠ sémantique ; origine ≠ taille de σ),
B A-F6 (1 degré : A4 se retourne) ; contre D1 de C, A F13, B C-F7 ; contre D2/D3, A F7 (σ_M = σ_S supposé), A F9 (lot) ;
contre l'arbre de C, A F14. Non attaqués : attendre (b) ; des contrôles avant toute graine, venus de l'équipe rouge seule
(organisme figé rejoué ≤ 30 dollars, B ; rejeu à même graine, A CN1 ; simulations à coût nul, A CN5). Survit : tout dessin
incluant la graine 1 porte le confondant de lot (les quatre cellules) ; tout déclencheur corrélé aux scores biaise σ̂.

**4. Pièges.** A § 4 : séries par empreinte d'objet ; clause à sens unique (σ̂ peut déclencher le palier 2, jamais changer δ
ni la mesure). C § 4 : compteur à zéro par version ; formule σ̂ → palier 1 (σ̂ > 0,04 ⇒ 6 graines). Attaques : B A-F4 (la
clause change la règle séquentielle et le coût de (b) ; ignore la v5.3) ; B A-F5 (base fraîche) ; A F11, B C-F9 (formule non
gelée, plusieurs estimateurs, calculateur voyant les moyennes) ; A F12, B C-F1 (statuts élevés). Survit : séries par empreinte ;
gel de (b) ; une règle σ̂ → (b) n'existe que scellée, estimateur unique, calculateur séparé (A CN6), muette sur la v5.3 (B).
Non résolu : B accepte un lancement sur faits mécaniques seuls ; C-1 et A F4 les disent contaminés.

**5. Connu.** Commun : Wittes et Brittain (1990), Kraemer et al. (2006) ; réestimer une variance de nuisance sans toucher δ ;
à 2–4 degrés, borne haute de σ. A : rien d'attribuable sur la variance entre exécutions d'agents qui se réécrivent. Attaques :
A F2 (C cite Browne pour la borne haute, puis fonde son seuil sur le point) ; A F11 (Kieser et Friede : pilote interne et
aveugle). Survit : § 6, à vérifier.

**6. Départager.** A § 6 : ce qui change dans (b), le lisible sans score, le délai, le coût ; se décide maintenant : geler (b),
pousser le texte nouveau. C § 6 : défaut mécanique → (c) ; nominal et cher → D2 ou D3 ; nominal et bon marché → (a) ; cinq
dominé sauf v6 lointaine. Attaques : A F4, F5, B C-F4 (seuils franchis par un organisme quasi inerte ; « sans score » faux par
construction) ; A F14 (coût et volonté ne sont pas des faits sur le bruit). Survit : la décision peut attendre les faits
mécaniques, qui mesurent l'activité, non la divergence, et biaisent σ̂ s'ils déclenchent des graines ; gel de (b) et texte
nouveau se décident sans eux ; cinq graines n'est défendu par personne.

## 3. La décision, pour Lazar

| dessin | ce qu'il achète | coût (illustratif, d'après la question) | ce que les modèles en disent | ce qui le départagerait |
|---|---|---|---|---|
| (a) trois graines par course | σ̂ à 2 degrés par question (4 si σ_M = σ_S), ρ̂, base pour une correction (écarts ≥ 0,14–0,22) ; non séquentiel, sans biais d'arrêt | +4 courses ≈ 180 / 300 (texte nouveau avant lecture ; sinon 6 : 270 / 450) | lignée B (question) : recommandé ; A : « deux courses nulles », σ mal mesuré ; C : si nominal et bon marché ; A, C (rouge) : lot de la graine 1 | rejeu à même graine ou organisme figé ; gel de (b) avec règle σ̂ → palier scellée |
| (b) cinq graines | σ̂ à 4 degrés (intervalle sur σ² ≈ 0,36 à 8,3, A) ; permutation 5 contre 5 utilisable | +8 courses ≈ 360 / 600 | A : insuffisant, double retard ; C : dominé, ≥ palier 1 de (b) ; aucun attaquant ne le défend | v6 bloquée des semaines et σ̂ intermédiaire après R = 3 (C) |
| (c) une course par question | faits mécaniques, lecture conditionnelle à la graine ; rien sur σ | 0 | A : la boucle ignore si elle corrige l'objet ou sa trajectoire ; C : dangereux si σ ≥ 0,04 ; McNemar à R = 1 aveugle à la graine (tous) | défaut mécanique avéré (correction d'abord) |
| +1 graine par question, non séquentiel (D3 de C ; D-1 sans 3ᵉ graine) | 1 degré par question, 2 mutualisés sous σ_M = σ_S ; moitié de (a) | +2 courses ≈ 90 / 150 (A dérivé ; C : 60–110 / 150) | A : le lisible sans score ; C : couvre M et S ; B A-F6 : à 1 degré, pire que R = 3 | 3ᵉ graine sur faits mécaniques → biais (C-1) ; distance des codes entre courses à compteurs égaux (C-c1) |
| +2 sur M seule (D2 de C) | 2 degrés sur M ; S à R = 1 | idem | C : moitié de (a) ; A F9 : lot ; A F2, B C-F3 : seuils non étalonnés | simulation d'étalonnage à coût nul (A CN5) ; poids de S |
| courses courtes (A D-3, C D5) | σ de la partie amont | moins par course (C : ≈ 48 au pire) | C : déconseillé ; A : si la divergence naît avant les générations (duel attaqué B A-F2, C-4) | non décidable sans courses entières |
| graines par version corrigée (A D-2, C D4) | itérations ; R = 3 sur la version finale | 0 maintenant | A : (c) déguisé ; C : aveugle à σ ; B A-F5 : base fraîche | si les journaux imposent une correction (C) |
| attendre (b) (A D-4) | σ sur la v6, les deux objets, 3 degrés chacun | 0 ; risque : palier 1 sous-dimensionné (≈ 270) ; boucle aveugle | A : coût zéro ; non attaqué ; B : la valeur des graines v3 tombe si σ est d'interface ou faute de v5.3 | date de la v6 ; besoin de corriger avant (b) |
| contrôles avant toute graine (équipe rouge) | sépare σ d'interface et de trajectoire ; étalonne les seuils | simulation 0 ; organisme figé ≤ 30 (B) ; même graine ≈ une course (A CN1) | B : sinon seul D3, dans (b), le révèle, après ≈ 270–450 ; non ripostés | c'est le départage lui-même |

**Recommandation (une phrase).** Exclure cinq graines ; décider maintenant ce qui ne coûte rien (geler (b) par empreinte ;
pousser le texte nouveau avec séries par empreinte d'objet, entrelacement et lot déclaré, avant toute lecture) ; dépenser
d'abord sur les contrôles de l'équipe rouge (simulation des seuils à coût nul, organisme figé rejoué ≤ 30 dollars) ; puis, si le
rejeu attribue σ à la trajectoire, (a) tel quel, non séquentiel donc sans biais d'arrêt, plutôt que D-1 ; si à l'interface,
aucune graine sur la v3 et attendre (b) — confiance moyenne sur l'ordre et l'exclusion de cinq graines, basse sur la branche
finale (aucune riposte, deux conceptions, même modèle que A). **Défaut : aucun (dépense).**

## 4. Transfert v3 → v6 ; le modèle de calcul de la question

**σ.** A : transférable *si* la part « course » vient de l'interface et de la règle d'arrêt (hypothèse, duel D3 dans (b)) ;
C : ordre de grandeur transférable sous réserve du duel 4, car « il vient du code ». Attaques : le duel 4 ne peut tester le
transfert (rejet de l'invariance vraie ≈ 0,35, A F3 ; intervalle central [0,06 ; 39] à 3 et 2 degrés, B C-F6, table à
vérifier) ; deux courses à même graine qui divergent font tomber « vient du code » (A CN1) ; rien vers la v5.3 (B). Tient :
seul le *régime* (σ dominant ou non) transfère ; s'il domine, n disparaît : à σ = 0,05, n = 60, p = 0,75, ρ = 0,6, σ² fait
67 % de V et n = 120 ramène √V de 0,061 à 0,056 (calcul explicite, C). **ρ.** A : peu ; C : en partie ; B C-F8 : pas le même
ρ. **p** : non (C).

**Le modèle** (V = σ² + (1 − ρ) p (1 − p) / n ; t à 2R − 2 degrés). Juste : trois cases recalculées par A (0,22 ; 0,14 ; 0,21) ;
2R − 2 pour deux échantillons ; appariement déjà soustrait (A, C (c).3, A F1, B C-F2) ; conservateur sous tâches hétérogènes
(C, B). Faux ou fragile : inadapté au gain intra-course (R − 1, apparié, sans √2 ; C, non contesté) ; quantiles additifs
optimistes à petits degrés (A) ; σ supposé constant, peut croître avec la génération (A, C, B A-F3) ; dérive absente (A, B) ;
pas de composante trajectoire × objet pour « origine contre corrigé » (A) ; ρ intra- et inter-objets confondus (C) ; σ_M = σ_S
si l'on mutualise (A F7) ; variances v6.2.1 et v5.3 supposées égales si σ̂ dimensionne (b) (B A-F4). Recalcul pour (b) à
n ≈ 120, p = 0,75, ρ = 0, R = 4 : écart minimal ≈ 0,09 à σ = 0, ≈ 0,15 à σ = 0,05 (A ; refait par B : 0,151) : palier 1 sous
δ = 0,10 dans le premier cas, au-dessus dans le second. R = 1 : non testable (tous).

## 5. Pièges relevés et gardes demandées

- **Sélection.** La graine 1 « gratuite » exclut la sélection sur score, non sur faits mécaniques, fonctions des scores de
  `test` (A A5, A F4) ; tout arrêt conditionnel biaise σ̂ (C-1, A F13) ; l'acte de lancer fuit le score (B C-F7) ; régression
  vers la moyenne dans « origine contre corrigé » (B A-F5). Gardes : règle de lancement écrite et poussée avant toute
  lecture, aveugle au score (B) ; dessin non séquentiel, ou base fraîche ; journal des lectures (A).
- **Multiplicité.** Seize scores par course (C) ; une mesure sommaire par course, un seul test exploratoire par correction
  (A, C) ; registre horodaté avant score ; elle se rend comptable, ne se corrige pas (A).
- **Dérive.** Graine 1 dans un lot, graines 2–3 dans un autre (les quatre cellules). Gardes : lot déclaré, effet « lot »
  (A CN7) ; référence de surface rejouée à chaque génération dans la même chaîne de notation (A CN3) ; sorties brutes de g0
  comparées entre vagues (C-c5) ; version du modèle consignée si exposée (A).
- **Orientation du dessin de (b).** Geler par empreinte, avant tout score du pilote 4 : δ, mesure principale, R des deux
  paliers, règle de passage et d'arrêt (A, C, les trois attaquants) ; toute règle σ̂ → R en script scellé, estimateur,
  génération, part et question uniques, calculateur séparé (A CN6) ; interdiction écrite de transporter σ̂(v6.2.1) aux deux
  bras, ou un σ de la v5.3 (B) ; borne haute de σ plutôt que le point (A, C, A F2).
- **Instruments.** Seuils des duels 2 et 4 à simuler avant toute course, sous lois à contamination et hétéroscédastiques
  (A CN5, B, C-c3) ; boucle extérieure : placebo d'étiquettes permutées par course entière avec les traces réelles (B, C-c4),
  « même graine, deux agents » avant « deux graines, deux agents » (A CN4) ; contre les évasions de l'organisme à coût nul
  (compteurs régularisés, génération 0 dégradée puis restaurée, effondrement vers une heuristique rigide ; résumées sans
  leur contenu) : distance des codes et des paramètres d'architecte (C-c1), ligne de base avant toute ronde (C-c2),
  organisme figé rejoué comme zéro mesuré (A CN2, B), contrôle positif puis négatif du duel 1 (B).

## 6. Références citées (toutes « à vérifier » ; aucune ajoutée)

Par A : Wittes et Brittain, 1990, « The role of internal pilot studies in increasing the efficiency of clinical trials » ;
Birkett et Day, 1994, « Internal pilot studies for estimating sample size » ; Proschan, 2005, « Two-stage sample size
re-estimation based on a nuisance parameter: a review » ; Kraemer, Mintz, Noda, Tinklenberg et Yesavage, 2006, « Caution
regarding the use of pilot studies to guide power calculations for study proposals » ; Julious, 2005, « Sample size of 12 per
group rule of thumb for a pilot study » ; Whitehead, Julious, Cooper et Campbell, 2016, « Estimating the sample size for a
pilot randomised trial to minimise the overall trial sample size… » ; Lancaster, Dodd et Williamson, 2004, « Design and
analysis of pilot studies: recommendations for good practice » ; Raiffa et Schlaifer, 1961, « Applied Statistical Decision
Theory » ; Henderson et al., 2018, « Deep reinforcement learning that matters » ; Colas, Sigaud et Oudeyer, 2018, « How many
random seeds? Statistical power analysis in deep RL experiments » ; Agarwal, Schwarzer, Castro, Courville et Bellemare, 2021,
« Deep reinforcement learning at the edge of the statistical precipice » ; Bouthillier et al., 2021, « Accounting for variance
in machine learning benchmarks » ; Miller, 2024, « Adding error bars to evals » ; Gelman et Loken, 2014, « The statistical
crisis in science » ; Holm, 1979, « A simple sequentially rejective multiple test procedure ». Par C, en plus : Kieser et
Friede, 2000, « Re-calculating the sample size in internal pilot study designs with control of the type I error rate » ;
Browne, 1995, « On the use of a pilot sample for sample size determination » ; Leon, Davis et Kraemer, 2011, « The role and
interpretation of pilot studies in clinical research » ; Gelman et Carlin, 2014, « Beyond Power Calculations: Assessing Type S
(Sign) and Type M (Magnitude) Errors » ; Baayen, Davidson et Bates, 2008, « Mixed-effects modeling with crossed random effects
for subjects and items » ; « travaux récents 2023–2025 » non nommés, non citables. Aucune référence nouvelle au III.2.

## 7. Réserves de lecture

- **Même modèle que A, non que B.** Écrite par Claude Fable 5.1, modèle de la conception A et de l'attaque A ; le brief dit
  « même modèle que B » : écart déclaré. Le biais possible va vers A (« courses nulles », D-1, CN1 à CN7) ; la recommandation
  préfère pourtant (a) à D-1 sur l'argument de C-1 et de B C-F7, et retient les contrôles de B autant que ceux de A.
- **Structure du III.2.** Le brief dit que les trois modèles attaquent les deux conceptions ; en fait A n'attaque que C, C
  n'attaque que A (sections « contre B » vides, par construction croisée), seul B attaque A et C.
- **Absence d'Opus au III.1.** La convergence est celle de deux modèles ; B, en attaquant, fait émerger une voie que personne
  n'a conçue (contrôles bon marché d'abord, base fraîche, σ de la v5.3), elle-même non attaquée.
- **Absence de riposte.** Les calculs de l'équipe rouge (0,30 ; 0,21 ; 0,52 ; 0,35 ; [0,06 ; 39] ; 0,151) sont explicites sous
  normalité ; la synthèse a refait à la main ceux de A (III.1), de A F2–F3 et de B A-F1, C-F3 : concordants à l'arrondi près ;
  les quantiles de table de B C-F6 ne sont pas vérifiés. Rien ne vaut verdict ; les contradictions relevées chez C
  (appariement, mutualisation M/S, « décisif » contre 25–35 %, statuts) et chez A (A4 contre D-1) restent sans réponse.
- **Ambiguïtés de la question.** « Le modèle vaut tel quel » : juste pour deux configurations sur banque fixe, non pour le
  gain intra-course (C) ; « course nulle » et (a) coïncident depuis la v3 (A) ; le coût de deux courses n'est pas dans la
  question (A : ≈ 90 / 150 dérivé ; C : 60–110 / 150) ; les chiffres de (a) supposent le texte nouveau avant toute lecture.
  Hors-sujet : le passage de C sur des modèles à poids ouverts (il le dit lui-même).
- **Écarts à ce brief.** Longueur au-dessus de deux pages imprimées (table à cinq colonnes, liste de références ; compte dans
  le LISEZMOI de sortie). Aucun score, aucun critère ni stratégie de classement, aucune réflexion interne, aucun tutoiement.
