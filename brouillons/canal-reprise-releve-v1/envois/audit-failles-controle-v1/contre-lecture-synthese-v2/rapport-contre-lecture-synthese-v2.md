# Contre-lecture ciblée de la synthèse v2 de l'audit des failles de notre contrôle — rapport — v2

Contre-lecteur : le même sous-agent que pour la v1 (Fable 5.1 ; N-052), qui n'a écrit aucune pièce de l'audit. Ouvert le
2026-10-26 à 14:15:32 UTC (heure lue sur `date -u` dans la commande qui écrit ce fichier) ; clôture en dernière ligne. Mon rapport v1
(`rapport-contre-lecture-synthese-v1.md`, `7b8a17c3…`) reste tel quel. **Pièce confidentielle** : aucun montant, aucun
financeur, aucun nom propre de la page de titre des rapports (hors Lazar) ici ; vérifié aussi sur la synthèse v2 et son
LISEZMOI (contrôle automatique sur les mots de la page de titre, les motifs de montant et le surnom de l'organisme : zéro
occurrence). Consigne de prudence du coordinateur (R-519) reçue en cours de travail et appliquée : je n'ai conçu, détaillé
ni amélioré aucune stratégie d'attaque ; chaque négation est jugée sur le calcul ; aucun arrêt par filtre n'est survenu.

**Vérifications préalables.** Brief v2 (`0fa6b62e…`) conforme ; `EMPREINTES-fournis-v2.txt` : 12 sur 12 conformes
(synthèse v2 `890130e8…`, LISEZMOI `c8f25c5b…`, calculs v2 et v3 et leurs sorties, transcription `c1237687…`, quatre PDF
de complément). `calculs-synthese-v2.py` et `calculs-synthese-v3.py` rejoués par `python3 -I` (numpy 2.5.3) : sorties
identiques octet pour octet. Empreintes sur disque des 22 PDF de L4 nouvellement cités (annexe B de la v2) : conformes
aux huit premiers caractères, **sauf Panin** (CLS2-05). Mes propres calculs : `calculs-contre-lecture-v2.py` et
`calculs-contre-lecture-v2.sortie.txt` (empreintes dans leurs compagnons ; graine `SeedSequence(26102026)`, distincte de
celle de la synthèse ; nuls simplifiés, aucune donnée des pilotes). Réseau : aucune recherche (le brief en permettait une).

---

## 1. Verdict

**Transmissible après corrections.** Aucun constat bloquant. Les quinze constats de ma v1 sont appliqués (section 2 :
quinze « fait », deux nuances acceptées). La troisième partie du rapport est jugée avec des sources relues et des calculs
reproductibles : les mathématiques des opérateurs E, G, H et I et des expériences HR3 et HR5 sont établies ; F est établie
et robuste au choix du nul (section 3). Cinq constats sont **à corriger avant transmission** : le mot « non falsifiable »
(CLS2-01) ; la gravité prêtée à l'opérateur E (CLS2-02) ; l'absolu « aucune normalisation » et l'option manquante de D-18
(CLS2-03) ; une phrase inexacte dans l'enjeu de D-19 (CLS2-04) ; une empreinte fausse pour Panin (CLS2-05). Sept constats
mineurs suivent (CLS2-06 à CLS2-12), dont deux de prudence au sens de R-519. Trois angles que ni le rapport ni la v2 ne
voient sont en section 9.

---

## 2. Application de la contre-lecture v1 (brief, point 1)

| constat v1 | traitement annoncé | vérifié dans la v2 (ligne) | verdict |
|---|---|---|---|
| CLS-01 | regradé 2 + 2 + 3 ; points 1, 2, 4, 5 réécrits | l. 66–108 ; D-01 l. 1780–1791 | fait |
| CLS-02 | « non sourcés dans le rapport », sources probables, seize chiffres, « q ≈ 0,75 » à part | l. 136–139 ; table 1.11 l. 452–462 | fait ; nuance acceptée (la ligne à part garde la comparaison v1/v2 lisible) |
| CLS-03 | FC-04 reformulée, repliée sur FI-04 ; tirage au hasard retiré | l. 1538–1544 ; grille l. 1377 ; section 6 n° 10 l. 1704 ; 0.2 (b) l. 147–150 | fait |
| CLS-04 | D-02 = retour au texte accepté ; cas cité dans D-11 | l. 1793–1799 ; l. 1914–1917 ; 0.2 l. 176–177 | fait |
| CLS-05 | faille (a) « candidate … bloque la revendication » ; « outil le moins sûr » remplacé | l. 143–147 ; l. 1798–1801 ; 4.1 | fait |
| CLS-06 | D-08 (a) : statistique non créditable, équipe rouge à mémoire ; p. 10 citée | l. 1879–1893 ; FI-15 l. 1339 ; HT-18 l. 968–980 | fait |
| CLS-07 | options complétées | comptage : toutes les décisions ont au moins trois options avec avantage et inconvénient, sauf un « statu quo » ou « limite déclarée » nu dans D-03, D-05, D-14, D-16 (permis) | fait ; nuance acceptée |
| CLS-08 | FC-15, 16, 18, 20 instruites ; « ce qui tombe » ajouté à FC-06 et FC-13 | section 5.3 l. 1653–1681 | fait (sommaire, mais les cinq parties y sont) |
| CLS-09 | N-047 = N-053 dit une fois | l. 57–58 ; l. 1778 | fait |
| CLS-10 | conjecture retirée | l. 414 | fait |
| CLS-11 | Dawid et Skene « classique, non relue » | HT-22 l. 1018–1019 ; grille FI-09 | fait |
| CLS-12 | plan 2 × 2 information × accès ; (ii) contestée, renvoi à D-14 | D-02 l. 1805–1809 ; HT-16 l. 938–953 | fait |
| CLS-13 | « borne la détectabilité » | l. 1438 | fait |
| CLS-14 | « effet non séparé » ; HT-21 | l. 1507–1509 ; l. 1004–1013 | fait |
| CLS-15 | « indécidable sans le préenregistrement » | l. 302, 571, 1375, 1524 | fait |
| Antériorité 1 (2410.12555) | cité « non vérifié sur PDF » | six occurrences (l. 575, 676, 1375, 1402, 1526, 2062), toutes marquées | fait |
| Manques 1 à 4 | D-07, D-11, D-08, RC-3.3 | l. 1859–1877 (14,26 % et 2,97 % refaits : exacts) ; l. 1916 ; l. 1879 ; l. 589–591 | fait |

---

## 3. Troisième partie du rapport (failles E à I) : les jugements de la v2 refaits (brief, point 2)

Sources : transcription expurgée v2 (lignes 138–214) ; PDF de L4 et de complément relus aux pages citées (section 10) ;
calculs v2 et v3 rejoués ; mes calculs (`calculs-contre-lecture-v2.sortie.txt`, blocs E1, E2, F1, G, HR5).

- **« Aucune faille démontrée ; toutes ont des voisins publiés » (0.1, point 8 ; 1 bis).** Conforme, avec la réserve que la
  v2 écrit elle-même : les voisins couvrent les principes ou les composantes (E : 2005.07821v1 p. 1, 2601.20022v2 p. 1–3 —
  dont p. 2 : « [12] investigates an adversarial setting against the CuSum procedure » —, 2606.10456v2 p. 1–2 ; F :
  2607.02510v1 p. 2 « drawn exchangeably from the same distribution as the deployment data », 2610.04575v1 p. 2
  « same-horizon », « calibration-to-test mismatch » ; G : 2606.07612v1 p. 8 et p. 18, liste L1 « add negative controls that
  … share surface cues » ; I : 2608.25869v1 p. 1, 2509.26072v2 p. 1, 2605.23970v1 p. 1, 2508.05625v1 p. 3, 2603.15809v1
  p. 1 : tous relus, conformes), jamais l'enchaînement, ce que la v2 dit (« enchaînement non trouvé »). « Démontrée » : aucun
  code ni mesure fournis (transcription : « opérateurs implémentés », aucun résultat) : conforme.
- **E, « la statistique d'énergie d'excursion ignore l'ordre des scores et ramène la détection à la classe C ».** L'identité
  (C_t − C_{t−1})₊ = (X_t − κ)₊ est vraie **pour toute suite**, pas seulement quand C_{t−1} = 0 : si X_t ≥ κ, C_t − C_{t−1} =
  X_t − κ ; sinon, soit C_t − C_{t−1} = X_t − κ < 0, soit C_t = 0 et C_t − C_{t−1} = −C_{t−1} ≤ 0 ; dans les deux cas la
  partie positive est nulle, comme (X_t − κ)₊ (mon bloc E1 : écart 10⁻¹⁵ sur trois lois, avec 36 à 57 % des pas à
  C_{t−1} > 0). Le **premier terme** de V_T est donc exactement symétrique : **conforme**. Mais V_T entier ne l'est pas : son
  second terme est le maximum adouci de la somme cumulée, sensible à l'ordre, ce que la v2 dit en RC-3.1 (b) et que les
  formulations courtes (0.1 point 12, 0.2 point 2, D-01, D-19) écrasent en « retour à la classe C » : CLS2-02. Mon bloc E2
  (nul N(0,1), T = 100, κ = 0,5, seuils au rang conforme sur 20 000 épisodes honnêtes, 1 %) : HR1 tel qu'écrit donne somme
  cumulée 0,7 %, terme symétrique 87,6 %, V_T entier 77,4 % ; le même multi-ensemble rebrassé (témoin de classe C) donne
  87,6 % / 82,4 % / 16,6 % ; un décalage constant de même moyenne que le motif donne 0,3 % partout, tandis qu'un test de
  variance intra-épisode donne 98,4 %. Donc : (1) HR1 tel qu'écrit « confirmerait » ; (2) V_T réagit autant au motif qu'à son
  rebrassage : HR1 ne teste pas la remise à zéro ; (3) ce que V_T attrape est le changement de loi marginale (variance) —
  les trois points de la v2 sont **établis par calcul**. (Sur le motif lui-même je n'ajoute rien : R-519.)
- **F, « 1 % visé devient 2,19 % à 4,56 % à 30 pas, même avec la normalisation du rapport ».** Nul simulé par la v2 : scores
  gaussiens, effet épisode additif b_e ~ N(0, τ²) avec τ = 0,3 et 0,6, calibrage à 10 pas (bloc 2, lu dans le code). La
  normalisation est implémentée **telle qu'écrite**, avec μ̂₀ = 0 et σ̂_s² = 1 connus (V_t = t, V₁ = 1) : un facteur constant
  sur σ̂² ne changerait rien à un seuil calibré sur la même statistique. Mon implémentation indépendante (bloc F1, 100 000
  épisodes par cas, α = 1 %, calibrage à 10 pas, test à 5, 10, 20, 30 et 60 pas) : **effet épisode nul** : 0,89 / 0,99 /
  0,97 / 1,02 / 1,06 % (invariance tenue) ; τ = 0,3 : 0,71 / 0,99 / 1,50 / **2,08** / 4,14 % ; τ = 0,6 : 0,37 / 0,95 / 2,69 /
  **4,46** / 9,24 % ; **effet fort** τ = 1,0 : 0,26 / 1,03 / 3,40 / 5,79 / 11,48 %. Le résultat **tient** et s'aggrave avec τ
  (2,19 % et 4,56 % de la v2 : conformes à l'erreur de Monte-Carlo près). Deux compléments : (i) sous une dépendance
  intra-épisode AR(1) à φ = 0,3 sans effet épisode, et sous des queues lourdes (Student à 4 degrés), l'invariance tient à peu
  près (1,13 à 1,23 % ; 0,98 à 1,01 %) : la chute est propre à l'effet épisode (décalage persistant), non à toute dépendance ;
  (ii) si σ̂_s² est estimé **dans l'épisode** (lecture littérale de V_t = Σ σ̂_s²), l'invariance tombe même sous
  indépendance (0,29 / 1,04 / 1,48 / 1,65 / 1,87 %) : la réserve (e) de RC-3.2 est plus forte que la v2 ne l'écrit.
  (iii) Une normalisation qui met la variance **vraie du nul** au dénominateur, √(t + τ²t²), reste proche de l'invariance
  sous effet épisode (τ = 0,3 : 0,67 / 0,97 / 1,20 / 1,31 / 1,37 % ; τ = 0,6 : 0,85 / 0,99 / 1,15 / 1,20 / 1,28 % ; τ = 1,0 :
  1,00 / 1,07 / 1,21 / 1,19 / 1,22 %) : approximative, non exacte, mais sans les 4 à 11 % de la normalisation du rapport :
  CLS2-03. Le point (2) de la faille (raccourcissement) est bien une perte de puissance, pas de validité : conforme.
- **G, « un plancher sur covariance honnête accepte une sonde qui lit un tic de surface ».** Mécanisme exact : à covariances
  intra-classe égales, Σ_mélange − Σ_honnête = p(1 − p)·Δμ Δμᵀ ⪰ 0, donc les directions tirées sous Σ_honnête chargent moins
  la direction du tic et leur quantile 0,95 est plus bas, quelle que soit la géométrie (mon bloc G, spectre en 1/k, 200
  directions, 300 répétitions : écart mélange − honnête de +0,002 à +0,070, toujours positif ; v2 : +0,001 à +0,163).
  **Ancrage** : le plancher sur le mélange fait **mieux** (plus strict) sur le même cas, d'un montant qui dépend de la
  géométrie : négligeable pour un tic sur une composante dominante (+0,002 à +0,006, la sonde du tic étant alors au niveau
  des deux planchers : 0,760 contre 0,748 et 0,751), notable pour un tic fort sur une composante faible (+0,070, la sonde du
  tic à 0,998 contre 0,559 et 0,628). Les deux conclusions de la v2 sont établies : la covariance honnête abaisse le
  plancher, et aucun des deux planchers ne contrôle une confusion logée dans une direction de faible variance.
- **H, « repose sur une garantie 100 % fausse ».** Établi, non opinion : dans un modèle autorégressif, la loi du premier
  chiffre est calculée à la position qui le précède ; l'état de t_coût − 1 porte donc par construction l'information de
  grandeur que le rapport dit absente, et la prémisse de la faille (« l'état caché prépare la distribution de probabilité
  du premier chiffre », transcription l. 185) le dit elle-même. Lecture charitable possible (« aucun chiffre dans les jetons
  d'entrée ») : vraie, mais elle ne sauve pas la phrase, qui parle de « toute séparation par la sonde ». Voisin relu :
  2604.07729v1 p. 3 (« encode … relevant to predicting upcoming tokens ») : conforme.
- **I, « mesure une pente, ni une hystérésis ni une interaction ».** Exact sur la définition : χ₂ = (g(s₂) − g(s₁))/(s₂ −
  s₁) est une différence finie du gain selon l'intensité ; deux points ascendants ne voient ni un seuil au-delà de s₂ (bloc 4
  de la v2 : g(s₁) = g(s₂) = 0,15, χ₂ = 0, gain sécant 0,749 en s = 1), ni une hystérésis (il faut un chemin montant puis
  descendant), ni une interaction entre deux composantes (il faut un plan croisé). Nuance de vocabulaire : g étant lui-même
  défini par le rapport comme une dérivée (−∂Δv/∂v₀), χ₂ est une différence **mixte du second ordre** (en s et en v₀), ce
  qui rend « tenseur d'ordre 2 » abusif mais « ordre 1 » (RC-3.5 (a)) inexact : CLS2-06.
- **« Aucune des cinq expériences n'est falsifiable telle qu'écrite ; HR3 connu d'avance ; HR5 franchi par hasard 12,4 %
  des fois à six moniteurs ».** HR3 : le signe est acquis par l'inégalité ci-dessus (sous covariances intra-classe égales),
  conforme ; mais son seuil (+0,03) peut échouer (v2 elle-même : +0,001 à +0,163 selon la géométrie) : HR3 est falsifiable
  sur l'ampleur, elle ne teste simplement pas une attaque. HR5 : mon bloc (validation croisée un contre tous, prédicteur
  sans lien) donne 12,6 à 13,2 % à six moniteurs, 14,0 à 14,6 % à cinq, 1,1 à 1,3 % à vingt, pour trois niveaux de bruit :
  conforme et robuste ; mais HR5 a un seuil (25 %) et une métrique : elle est **sous-spécifiée** (nombre de moniteurs,
  « effondrement », égalisation des forces), non infalsifiable. HR1 : budget incohérent (25 × 1,5σ = 37,5σ de pas hauts, somme
  nette −7,5σ, « B = 15σ » ne correspond à rien : refait), paramètres manquants : sous-spécifiée, et son issue suit de la
  construction. HR2 : fourchettes données, nul non spécifié : sous-spécifiée, et l'issue bascule avec τ (établi ci-dessus).
  HR4 : « dépasse » sans seuil : falsifiable en signe seulement. Verdict : **« sous-spécifiées » est le bon mot** pour les
  cinq ; « non falsifiable » est faux pour HR3 et HR5 : CLS2-01.

---

## 4. Constats

### CLS2-01 — à corriger — « non falsifiable » (l. 123–126 ; 0.2 l. 158–159 ; D-01 l. 1783 ; D-19 l. 2017, 2024)

Comme établi en section 3 : HR1, HR2 et HR5 sont sous-spécifiées (paramètres, nul, nombre de moniteurs), HR4 n'a qu'un
signe, HR3 teste l'arithmétique de sa prémisse. Écrire « aucune n'est spécifiée au point d'être décisive telle qu'écrite :
HR1, HR2, HR5 sous-spécifiées ; HR4 sans seuil ; HR3 au signe acquis » ; garder la recommandation de D-19.

### CLS2-02 — à corriger — E : « affaiblirait le contrôle » et « retour à la classe C » (l. 131–134 ; l. 156–158 ; D-01 l. 1784 ; D-19 l. 2018 ; 1 bis.6 l. 674 ; grille l. 1205, 1400)

Établi : le terme nouveau de V_T est symétrique, sans contrôle de fausses alarmes, et sa croissance « quadratique » n'existe
pas ; V_T réagit autant au motif qu'à son rebrassage. Non établi : que V_T **affaiblisse** le contrôle. V_T entier garde le
maximum adouci de la somme cumulée (second terme), donc l'ordre ; sous mon nul, V_T entier détecte HR1 à 77 % et son
rebrassage à 82 %, là où la somme cumulée donne 0,7 % et 16,6 % : sur cette alternative, il fait mieux, pas moins bien ;
sur d'autres alternatives (dommage structuré tardif), rien n'est calculé. Écrire : « son terme nouveau ramène à la classe C
et n'est pas calibré ; V_T n'est pas une parade à la remise à zéro ; aucune comparaison de puissance n'est faite » ;
retirer « affaiblirait » pour E (le garder pour G, où le sens est établi : CLS2-03 de G, section 3).

### CLS2-03 — à corriger — F : « aucune normalisation par la durée ne rend la loi du maximum invariante » (HT-02 l. 722–724) ; option manquante de D-18 (l. 2002–2014)

Mon bloc F1 (iii) : une normalisation par la variance vraie du nul, √(t + τ²t²) avec τ estimé sur les épisodes honnêtes du
calibrage, reste entre 1,0 et 1,4 % pour 1 % visé jusqu'à 60 pas sous effet épisode (τ = 0,3 à 1,0), contre 2 à 11 % pour la
normalisation du rapport. Elle n'est pas exacte (Mondrian l'est par construction) et perd sous indépendance (1,4 à 2,2 % à
20–60 pas), mais l'absolu « aucune » est faux, et D-18 devrait l'offrir comme option (d) : « normalisation à variance
d'épisode estimée sur le calibrage — avantage : aucun épisode de plus, une seule statistique ; inconvénient : approximative,
dépend d'un τ estimé, pas de garantie exacte par classe ». Recommandation (a) inchangée ; l'énoncé de HT-02 devient « la
normalisation du rapport (sans terme d'épisode) ne rend pas … ».

### CLS2-04 — à corriger — D-19, enjeu : « leurs opérateurs viennent de l'organisme, qui attaque des parades qu'il a lui-même proposées » (l. 2017–2018)

Inexact : la troisième partie attaque le seuil conforme (T0.3, P8), la somme cumulée de Page (N-004), le plancher apparié
(P3), la lecture P3b et la loi de déférence (transcription l. 140) : des parades du programme, pas de l'organisme (dont les
contributions de génération 1 sont 2.1 à 2.4). Écrire « qui attaque les parades de la génération 1, pour l'essentiel celles
du programme ». L'argument de D-19 (R1, R2 avant tout instrument scellé) n'en dépend pas.

### CLS2-05 — à corriger — empreinte de Panin (HT-09 l. 847 ; annexe B l. 2154–2155)

La v2 cite `ssrn-7424179` `66787c14…` (p. 4, 5). Sur disque, `pdf-main/ssrn-7424179-panin-2026-v1.pdf` a l'empreinte
`27f88ed7…`, identique à celle de sa note de provenance (`provenance-voisin-panin-v1.md`) ; `66787c14` n'apparaît dans
aucune autre pièce. Le contenu cité est juste (p. 4 : Holm ; p. 5 : « Equivalence is tested by TOST at ±0.05 … margin was
fixed in the Phase-0 registration », relu) : seule l'empreinte est fausse, ce qui rend la citation non opposable (R6, R7).
Remplacer par `27f88ed7…`.

### CLS2-06 — mineur — I : « différence finie d'ordre 1 » (l. 653–654)

Voir section 3 : différence mixte du second ordre, un scalaire ; « pas un tenseur » reste juste.

### CLS2-07 — mineur, prudence (R-519) — deux phrases à ramener au niveau du détecteur (l. 509–510 ; HT-01 l. 705–708)

(1) « le motif est superflu : un décalage constant juste sous κ passe aussi » : énoncé exact (c'est la définition de la
dérive de référence), mais écrit comme une propriété de l'attaquant ; l'écrire comme propriété du détecteur (« la somme
cumulée n'a, par construction, pas de puissance contre une moyenne sous κ : borne max C_t ≥ Σ(X_t − κ) »). (2) HT-01
paramètre une « famille compensation » (amplitudes, périodes, phase) au-delà du motif du rapport : c'est une famille de
simulation sur des scores, pas une procédure pour un agent, mais elle étend la description d'une attaque ; la ramener au
motif de HR1 et à son rebrassage (témoin), et laisser les autres paramètres au préenregistrement scellé. Rien d'autre dans
1 bis et 1 ter n'est une recette : mécanismes résumés du rapport, mesures et témoins.

### CLS2-08 — mineur — HT-09 : taille d'échantillon sans grappes (l. 850–851)

L'erreur type de Hanley et McNeil (calcul v3) suppose des épisodes indépendants ; P3 a 60 tâches et son intervalle est un
rééchantillonnage **par tâches** (N-025, remarque 3 : demi-largeur observée ≈ 0,044 pour 240 épisodes, contre 0,043 prédit
ici sans grappes — coïncidence à ne pas lire comme une validation). Dire « par épisodes indépendants ; à corriger de l'effet
de grappe par tâche ».

### CLS2-09 — mineur — rapprochements décoratifs (HT-08, HT-22, HT-30)

La limite de détection de Currie (HT-08), l'estimation de Lincoln et Petersen (HT-22 : son hypothèse d'indépendance des
captures est précisément ce que FI-09 nie) et la valeur de Shapley pour deux membres (HT-30 : une ablation suffit) ne
portent pas la prédiction ; les vingt-neuf autres rapprochements sont porteurs (Mondrian, intersection-union, Spearman,
Bliss, variance ratio, covariable pré-expérience, généralisation temporelle…), tous marqués « non relue (R7) » : conforme.

### CLS2-10 — mineur — HT-25 : bras d'attaque déclaré (l. 1052–1057)

La « variante récompensée par le score d'un juge J » est un entraînement contre un moniteur : permis seulement comme « bras
d'attaque déclaré » de l'invariant de N-053, point 5, sous GO ; l'écrire dans l'hypothèse.

### CLS2-11 — mineur — quatre PDF sans note de provenance (l. 2063–2064 ; annexe B l. 2156–2157)

2607.11871v1 (`5d1d22ed…`, p. 1 : « matched-norm random directions »), 2609.35591v2 (`e92c69cb…`, p. 5 : « mutually
orthogonal random directions as controls »), 2604.07729v1 (`afe70d72…`, p. 3), 2602.19159v1 (`ab4ed860…`, p. 1 : marge de
logits 2-3) : présents dans `pdf-main/` avec ces empreintes, pages conformes, mais absents de toute note de provenance et
de toute liste L1 à L3. Pas gênant pour une synthèse interne (le fichier est haché et la page lue) ; à compléter (adresse,
date) avant tout usage dans un papier. La v2 le déclare : conforme.

### CLS2-12 — mineur — F : « ne vaut que sous indépendance » (0.1 l. 133 ; 0.2 l. 157–158 ; 1 bis.6)

Précision : la normalisation du rapport tient aussi sous dépendance intra-épisode à mémoire courte et sous queues lourdes
(section 3) ; elle tombe sous un **décalage persistant par épisode**, de plus en plus avec τ. Écrire « tombe sous effet
épisode » plutôt que « ne vaut que sous indépendance ».

---

## 5. Hypothèses testables (brief, point 3)

Les trente-deux HT ont chacune : énoncé, prédiction chiffrée et signée, métrique et seuil, condition de réfutation, coût,
antériorité consignée (voisin avec page, ou « rapprochement proposé, non trouvé (L1 à L4) ») : conforme. Niveau de la
méthode : conforme, aux deux réserves de prudence près (CLS2-07, CLS2-10). Chiffres issus de calculs : HT-02 (2,19 % ;
4,56 % ; 18,99 % ; 20,69 %), HT-05 et HT-32 (12,4 % ; 14,26 % ; 2,97 %), HT-07 (bloc 6), HT-09 et HT-15 (calcul v3), HT-11
(formule g·R + (1 − R) vérifiée analytiquement : Cov(x, y) = g·Var(c − T) + Var(e₀), Var(x) = Var(c − T) + Var(e₀) ; mon bloc :
0,1636 contre 0,1646 prédit, 0,5813 contre 0,5822) : tous conformes aux sorties rejouées. Rapprochements : voir CLS2-09.

## 6. Quatre PDF de complément (brief, point 4)

Empreintes conformes (4 sur 4). Pages relues : 2601.21112, p. 1 (« less-is-more effect », « extract-and-evaluate »), p. 6
(« rates at 1% FPR by 16.8 percentage points »), p. 7 (figure 6 : « Monitors with CoT access are much stronger when the
attacker believes its CoT is private ») ; 2609.03026, p. 1 (Qwen2.5-7B), p. 2 (« AUROC and realized violations reverse the
order of two monitors » ; « lowest-loss context changes — even between the two Qwen checkpoints »), p. 15 (table 11 : AUROC
1,000 et perte 3,334 → AUROC 0,954 et perte 2,155 : conforme) ; 2607.08349, p. 1–2 (suites de confiance valables à tout
instant pour des scores bornés d'interventions en interprétabilité : conforme, « voisin de méthode, non de cible ») ;
2608.19338, p. 1–2 (mesures d'effets d'intervention, « not specific to control » : cité sans effet sur les statuts,
conforme). Les quatre disent ce que la v2 leur fait dire.

## 7. Décisions (brief, point 5)

D-17, D-18, D-19 : trois options chacune, avantage et inconvénient partout, recommandation et confiance, défaut ou « pas de
défaut » cohérents avec leur nature (D-17 nœud ; D-18 et D-19 : défaut (a) pour la méthode, dépense sans défaut pour les
épisodes et les bras payants) : conforme, aux réserves de CLS2-03 (option manquante de D-18) et CLS2-04 (enjeu de D-19). D-02
et D-07 refaits comme demandé (section 2). « Cinq dépenses sans défaut » : D-05 (génération), D-06 (épisodes), D-12 (appels,
avec un volet règle gelée), D-14 (devis de (iv)), D-15 (agent Qwen, GO de modèle) : ce sont bien des dépenses ; les volets
de dépense de D-04, D-16, D-17, D-18, D-19 sont correctement distingués ; le bilan (l. 2031–2034) couvre D-01 à D-19.

## 8. Ancrage (brief, point 7)

Deux négations jugées sur le calcul, sans attaque nouvelle :
1. « V_T ne ramène pas la détection à la classe C » : **vraie pour V_T entier** (son second terme garde l'ordre : 77 % contre
   82 % entre motif et rebrassage), **fausse pour le terme nouveau** (identité exacte, 87,6 % des deux côtés). D'où CLS2-02.
2. « La normalisation du rapport garde le taux sous effet épisode » : **fausse** sous les trois τ, de plus en plus avec τ
   (jusqu'à 11,5 % à 60 pas pour τ = 1), **vraie** sans effet épisode, et presque vraie pour une normalisation à variance
   d'épisode (CLS2-03). La faille F est établie pour la validité de la garantie conforme à durée libre.
3. En complément, G (section 3) : « le plancher sur le mélange fait mieux » est vrai, d'un montant qui dépend de la
   géométrie.

## 9. Ce qui manque (brief, point 8)

1. **Multiplicité entre sondes au plancher** (G ; critère 3 de G0 ; D-07 (a) « au moins une sonde dépasse son plancher »).
   Le quantile 0,95 contrôle une fausse acceptation à 5 % **par sonde** ; avec k sondes lues contre leur plancher et une
   règle « au moins une », le risque monte à 1 − 0,95ᵏ : 9,75 % pour deux, 14,3 % pour trois, 22,6 % pour cinq (calcul
   élémentaire). Ni le rapport (G parle de la covariance, pas du nombre de sondes), ni la v2 (HT-29 vise la sélection
   d'organismes, HT-32 les modes) ne le disent ; c'est le pendant, côté sondes, de la règle de combinaison de D-07.
2. **Normalisation à variance d'épisode** (F) : option absente de D-18 et contre-exemple à l'absolu de HT-02 (CLS2-03).
3. **Forme du champ du coût dans la fenêtre pré-chiffre** (H ; HT-04). N-025, remarque 1 (vérifié) : les formes du champ
   diffèrent massivement entre conditions (honnête : 41 actions à plusieurs nombres, 14 à suffixe « k », 13 à intervalle ;
   saboteur : 3, 0, 0). Les jetons qui précèdent le premier chiffre portent précisément cette forme (intervalle,
   approximation, devise) : une sonde lue sur W_pré y trouverait une confusion que ni la « garantie » du rapport ni
   l'appariement de HT-04 (sur la tranche de coût écrit, plus un nul d'alignement) ne retirent. Remède au niveau de la
   méthode : apparier aussi sur la forme du champ (trait déjà retenu par N-029), ou stratifier W_pré par forme. Statut :
   lacune des deux textes, source interne vérifiée.

## 10. Vérifications conformes

| affirmation de la v2 | source refaite | verdict |
|---|---|---|
| calculs v2 (blocs 1 à 6) et v3 : toutes les valeurs citées dans RC-3.1 à RC-3.5, 1 bis.6, HT-02, 05, 07, 09, 11, 15, 32, D-07, D-18 | scripts rejoués, sorties identiques ; valeurs retrouvées ligne à ligne | conforme |
| formule g·R + (1 − R) (v3, correctif du bloc 5) | dérivation analytique et simulation indépendante | conforme ; le bloc 5 de la v2 était bien faux (fiabilité de v₀ au lieu de R) et ses pentes justes |
| borne de Clopper et Pearson 5,8 % (50 essais) ; erreur type 0,0127 (A = 0,575, n = 1 000) | refaits à la main | conforme |
| 1 − 0,95³ = 14,26 % ; 1 − 0,99³ = 2,97 % | refaits | conforme |
| transcription v2 : budget de HR1, « garantie 100 % », « certifié », « dépasse » sans seuil, « jamais documentées », coûts annoncés | l. 140, 156, 168, 181, 187, 193, 204–205 | conforme |
| pages de L4 : 2607.02510v1 p. 2 ; 2610.04575v1 p. 2 ; 2512.03109v2 p. 19 ; 2208.07610v2 p. 1 ; 2606.07612v1 p. 8, 18 ; 2608.25869v1 p. 1 ; 2509.26072v2 p. 1 ; 2605.23970v1 p. 1 ; 2508.05625v1 p. 3 ; 2606.18276v1 p. 2 ; 2603.15809v1 p. 1 ; 2412.09565v2 p. 1 ; 2506.14261v4 p. 1 (« token-level monitors are highly vulnerable ») ; 2512.11949v1 p. 1 ; 2601.20022v2 p. 2 ([12]) ; les quatre sans provenance | PDF hachés, pages physiques | conforme |
| quatre PDF de complément | section 6 | conforme |
| confidentialité de la v2 et de son LISEZMOI | contrôle automatique | conforme |

## 11. Ce que je n'ai pas pu vérifier ; écarts

- Les formules de la troisième partie sur le **PDF** du rapport : je les ai lues sur la transcription expurgée de
  session-depot (`c1237687…`), qui dit avoir transcrit les pages 7 à 10 sur le rendu ; je n'ai pas relu ces pages (le brief
  le permettait, je ne l'ai pas jugé nécessaire : la synthèse et la transcription concordent sur chaque formule que j'ai
  refaite).
- Howard et al. 2021 (cité par 2607.08349v1 p. 2) et toutes les références classiques des HT : non relues (R7), comme la v2
  le déclare.
- Le code de l'organisme (génération 2) et les expériences HR1 à HR5 : non fournis, non exécutés (R1).
- Mes nuls (gaussiens, effet épisode additif) sont aussi simplifiés que ceux de la v2 : ils établissent des propriétés
  d'opérateurs, rien sur les scores réels.
- Hygiène : rien lu ni écrit hors de `/var/tmp/contre-lecture-audit-synthese-v1/` et des dossiers de PDF nommés ; aucun
  `git`, aucune clé, aucun sous-agent, aucun réseau ; Python avec `-I` ; `set -C` ; écriture sous `sortie/` seulement ;
  R-519 appliquée ; aucun arrêt par filtre. Je n'ai pas corrigé la synthèse.

---
Horodatage : version close le 2026-10-26 à 14:15:32 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
