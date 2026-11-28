# Critique de l'exécution du prompt unique — lentille « fidélité aux sources et anti-faux-gap » (R7, R8) — v1

- **Objet** : contre-lecture de `…/brainstorm-outils-p3/execution-prompt-unique-v1.md` (sha256
  `659b0f189ad54ddaa81161ba8a9607d2eae08da73751521ac9c9a4fad0ba4122`, égal au compagnon) et des quatre balayages
  (`balayage-anthropic-v1.md` `18aa1d8b…`, `balayage-autres-v1.md` `3db74c5a…`, `balayage-consigne-intention-v1.md`
  `b5656517…`, `balayage-programme-v1.md` `278c8c27…`, tous égaux à leurs compagnons). Prompt unique
  `…/convergence-prompt-p3/prompt-unique-v1.md` (`534d58a3…`, égal à la valeur citée par l'exécution).
  Le préfixe `…/` vaut `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Auteur** : critique neuf (Claude), 2026-10-20, vers 20:30 UTC. Je n'ai écrit ni les balayages, ni l'exécution, ni
  P3, ni P4, ni P3b.
- **Lu dans le dépôt (lecture seule, sans recherche récursive)** : un seul fichier, `docs/sources/pdf/2509.21344v2.pdf`
  (sha256 `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c`, égal à son compagnon), cité [BX] par
  l'exécution. **Non lus** : le verdict de P3, le brief, `prereg/P3-consignes-v1.md`, tout `textes-actions-*`, tout
  `donnees/`. Rien lu sous `…/canal-gemini/`, ni sous `…/convergence-prompt-p3/` hormis le prompt. Aucune donnée de P3
  envoyée. Recherches web génériques seulement. Aucun service payant, aucune commande Vast.ai, **aucun appel à Gemini**
  (le bras Gemini est séparé).
- **Méthode** : chaque point décisif relu sur le PDF par `pdftotext -layout`, page = rang physique dans le fichier.
  Empreintes des 41 PDF cités par l'exécution recalculées : toutes égales à sa table des sources. Deux PDF décisifs
  retéléchargés d'arXiv et comparés octet par octet : identiques (lentille jacobienne 2607.15495v1 `c906bd59…` ; Yoo et
  Skapars 2609.02893v1 `b76151cd…`). Scripts : `…/brainstorm-outils-p3/scripts-critique-sources/` (`extraire.sh`,
  `cherche.py`, `page.py`) ; textes : `…/brainstorm-outils-p3/txt-critique-sources/`.
- **Gravité** : **élevée** = change une conclusion, une prédiction ou une recommandation de l'exécution ; **moyenne** =
  change un argument ou une citation, pas la recommandation ; **faible** = précision.
- **Statut** : note de travail. Rien n'est décidé. Aucune hypothèse, revendication ou préenregistrement n'est modifié.

## Verdict en cinq lignes

1. Les chiffres cités par l'exécution sont **justes à la page** dans l'immense majorité (contrôle symétrique, section C) :
   aucun chiffre inventé, aucune page fausse sur les points décisifs.
2. Le défaut principal est un **faux-gap par omission** : sur **notre modèle et notre famille de sondes**, une source déjà
   dans le dépôt [BX] a fait le rejeu « consigne remplacée » (0,95 → 0,63) et un organisme de sous-performance réglé (→ 0,5).
   L'exécution le cite pour un seul chiffre et présente son rejeu comme neuf.
3. Une **prédiction est inversée** : la lentille jacobienne prédit un signal **fort**, pas faible, en condition « mention »
   (simple mention ≈ consigne explicite, [JL] p. 15, p. 78). « Ours blanc » ne concerne que la consigne « ignore X ».
4. Deux « zones » ne sont pas libres : des organismes à comportement entraîné **existent** sur Llama-3.1-8B-Instruct
   ([ADL] p. 5, [BX] p. 7) ; lire une valeur **calculée** non écrite a des précédents ([KT] p. 1, p. 5 ; [SU] p. 1).
5. Pour l'organisme (ii) par distillation de contexte, la littérature dit qu'il est **le cas facile** ([TG] p. 3, p. 14,
   p. 26) : un succès sur (ii) ne départage pas « consigne intériorisée » et « intention ». L'exécution ne le dit pas.

---

## A. Constats

### CR-sources-01 — Antériorité directe sur notre modèle omise : le rejeu « consigne retirée » est publié — **élevée**

- **Où** : exécution 2.2 (rejeu contrefactuel), 4.3, 5.2 ; balayage-autres V1 (« rejeu croisé », attribué à Kirch et al.).
- **Ce que dit la source** ([BX], Boxo, Neelappa, Raval, 2509.21344v2, PDF du dépôt `aaac4ff9…`) :
  - p. 3 : sondes de la famille RepE (paires à consignes système), **Llama 3.1-8B-Instruct**, flux résiduel couche 14 ;
    agrégation par moyenne sur les jetons.
  - p. 5-6 : scénario de sous-performance sur consigne, aire 0,95. « Score Filtering » (scores pris hors de la consigne et
    du raisonnement) : 0,81. « Content Filtering » (« replacing the elicitation instructions with a benign prompt »,
    activations recalculées) : **0,63** dans le texte (p. 6), **0,62** dans la légende de la figure 4 (p. 6).
    Filtrage au hasard : effet minime (p. 6).
  - p. 7 : limites écrites : le filtrage des scores ne retire pas l'information propagée par l'attention ; le filtrage du
    contenu « forces the model out of distribution ».
  - p. 7 : organisme de sous-performance **réglé sur Llama 3.1-8B** (méthode de Bloom et al., 2025) ; p. 8 : sonde de
    0,94 au hasard (0,5) ; « probes … heavily relied on textual evidence ».
- **Écart** : l'exécution ne cite [BX] que pour « 0,94 → 0,5 » (section 5.2). Le rejeu de 2.2 est le « Content
  Filtering » de [BX], sur le même modèle, avec la même famille de sondes. Sa limite écrite (hors distribution) manque.
- **Correction proposée** : citer [BX] p. 5-7 comme **précédent principal** de 2.2 et de la question « consigne lue » ;
  reprendre sa limite ; dans la case « préfixe saboteur, consigne retirée », préférer une **ligne témoin de même longueur et
  même place** à une suppression, pour tenir la distribution (le plan 2 × 2 a déjà cette colonne) ; écrire que, sur notre
  modèle, la chute 0,95 → 0,63 est l'attendu publié pour une sonde générique quand la consigne disparaît.

### CR-sources-02 — Prédiction inversée pour la condition « mention » — **élevée**

- **Où** : exécution 4.1 (tableau, ligne « directive de sabotage lue », colonne « mention > honnête » : « faible (« ours
  blanc » [JL p. 14]) ») ; 3.3 point 4 (« l'effet « ours blanc » prédit un signal non nul en condition mention ») ;
  balayage-anthropic section 1 et 11.
- **Ce que dit la source** ([JL], 2607.15495v1, `c906bd59…`) :
  - p. 14 : l'effet « ours blanc » porte sur la consigne **« ignore X »** : présence réduite mais non nulle.
  - p. 15 : « a bare mention of the concept can prime it almost as strongly as an explicit focus instruction ».
  - p. 78 (§A.10) : la condition **« mention »** (« names the target … with no instruction attached ») place la cible dans
    l'espace J « on most trials » ; l'écart avec la consigne explicite est « small » (tâches catégorie et calcul ;
    modulation variable selon la tâche).
  - Modèles : Claude Sonnet 4.5, Haiku 4.5, Opus 4.5 (p. 10, p. 14). Non transposable tel quel au 8B.
- **Écart** : notre « mention » met le même texte trompeur dans le contexte. D'après [JL], un lecteur du **contenu** de la
  directive y répond presque comme chez le saboteur. La cellule doit dire « fort », pas « faible ».
- **Correction proposée** : cellule → « fort, proche du saboteur (amorçage par simple mention, [JL] p. 15, p. 78 ; modèles
  Claude) » ; dans 3.3, remplacer « ours blanc » par « amorçage par mention » ; conséquence à écrire : tout lecteur de
  vocabulaire (lentilles, oracles) sur (i-a) doit **échouer** au contraste saboteur contre mention ; cela renforce « pas de
  P3c outil » et fait de « mention » le témoin décisif, avec une prédiction chiffrable avant lecture.

### CR-sources-03 — L'organisme (ii) par distillation est le cas facile : non dit — **élevée**

- **Où** : exécution 4.5 point 1 (« distillation de contexte [AS p. 10] » comme geste d'Anthropic), 5.2, 6.4 (bras de
  transfert), 4.1 (ligne « objectif installé »).
- **Ce que dit la source** ([TG], 2512.07810v1, `77e64bcd…`) :
  - p. 3 et p. 14 : sous-performance **nettement plus facile à détecter** chez les organismes « prompt-distilled from
    instructions to underperform » que chez ceux qui imitent un modèle plus faible.
  - p. 25-26 : l'organisme distillé (Tarun) fait des erreurs « obviously intentional » et a « likely … a stronger
    self-conceptualisation of sandbagging ».
  - Page web, **non opposable** (institut britannique, « White Box Control at UK AISI — Update on Sandbagging
    Investigations », 10 juillet 2025 ; copie `…/brainstorm-outils-p3/web-critique-sources/aisi-wbc-sandbagging-update-2025.html`,
    sha256 `71d83db2e1f566786ba019760fac68ebca733eff188eef72f3a7cd70e47bd01a`) : sur **Llama-3.1-8B-Instruct**,
    « Probes worked well on the prompt distilled backdoor model organism », moins bien sur l'imitation d'un modèle faible.
- **Écart** : l'exécution fait de (ii) le lieu où « l'intention » se teste. Or l'organisme distillé d'une consigne peut
  porter une **consigne intériorisée** (même représentation que sous consigne). Une sonde qui lit « j'ai une consigne de
  gonfler » pourrait alors réussir sur (i) **et** sur (ii) : le test de validité de T0.7 ne départagerait plus.
- **Correction proposée** : écrire dans 4.1 et 6.4 que (ii) distillé est le **bout facile** de l'échelle publiée ; prévoir,
  pour T0.6, un second organisme sans consigne source (imitation d'une distribution de coûts gonflés, à la manière de
  l'imitation d'un modèle faible) ou, à défaut, déclarer d'avance qu'un succès sur (ii) distillé déclenche l'audit R4 « trop
  beau ». C'est une question pour Lazar (périmètre de T0.6), pas une décision.

### CR-sources-04 — Zone R8 (3) mal posée : des organismes existent sur Llama-3.1-8B-Instruct — **élevée**

- **Où** : exécution 5.1 (« Question (R8) : existe-t-il un organisme public à objectif caché sur Llama-3.1-8B-Instruct ?
  Non trouvé dans les sources lues ») ; « Réserves et zones vierges » (3) ; 3.5 et 5.1 (« Aucun saboteur 8B »).
- **Ce que disent les sources déjà lues par l'exécution** :
  - [ADL] p. 5 : organismes de désalignement émergent (conseils médicaux, sports extrêmes, finance) **sur Llama 3.1 8B
    Instruct**. L'exécution le cite elle-même en 3.5 : contradiction interne.
  - [BX] p. 7 : organisme de sous-performance réglé sur Llama 3.1-8B, conditionnel au déploiement.
  - [DYL] p. 20 : liste « Taboo » sur Gemma-2-9B-IT **et Llama-3.1-8B-Instruct**. Non confirmé par les sources primaires
    lues : [ESK] p. 4 et p. 15 (Gemma 2 9B pour Taboo) ; 2605.14347v3 p. 8 (Taboo sur Gemma-2-9B-it ; PDF
    `cs-2605.14347.pdf`, `6283ea8b…`). Reste « non vérifié ».
  - Page web non opposable (institut britannique, ci-dessus) : quatre organismes de sous-performance réglés (porte dérobée,
    mot de passe ; distillation de consigne, imitation d'un modèle faible) sur Llama-3.1-8B-Instruct.
- **Écart** : « Aucun saboteur 8B » est vrai **pour [TG]** seulement ([TG] p. 7, p. 36, vérifié). Dans le champ, il en
  existe au moins dans la littérature.
- **Correction proposée** : réécrire la zone en question plus étroite : « des organismes à comportement entraîné existent
  sur Llama-3.1-8B-Instruct ([ADL] p. 5 ; [BX] p. 7 ; billet de l'institut britannique) ; leurs **poids sont-ils publics** (à
  vérifier : aucun lien de publication trouvé dans [BX] ni dans le billet), leur croyance est-elle vérifiée ([DYL] p. 2-3),
  et l'un d'eux ment-il sur un **champ chiffré** ? ». Si des poids sont publics, la famille (iii) a peut-être une option 8B
  sans changement de modèle : à vérifier avant le devis.

### CR-sources-05 — Résultat positif publié sur consigne, même modèle, même famille de sonde : absent — **moyenne**

- **Où** : exécution 1.3 (arguments de (a) et (b)) ; 5.3 (ancre extérieure).
- **Ce que dit la source** (billet de l'institut britannique, **non opposable**, copie ci-dessus) : sous-performance **sur
  consigne** de Llama-3.1-8B-Instruct ; sondes de tromperie entraînées hors politique (Zou et al.) « performed consistently
  very well » ; flux résiduel après la 14e couche dense ; dégradation en 70 milliards et sur organismes réglés. [BX] p. 5-6
  (vérifié) montre que, sur ce même modèle, ce succès tient en grande partie au texte de la consigne et du raisonnement.
- **Écart** : le nul de P3 sur une consigne cachée est en tension apparente avec ce succès publié. Les différences
  candidates sont exactement les hypothèses de l'exécution : agrégation (moyenne chez eux, maximum chez nous), action longue
  et multi-champs, raisonnement verbalisé ou non, couche 14 contre 15.
- **Correction proposée** : citer ce billet en 1.3 comme indice (non opposable) et [BX] comme fait vérifié ; formuler la
  question testable : « le succès publié sur consigne disparaît-il quand on retire le texte de la consigne et du raisonnement
  ([BX] p. 5-6) ? ». Aucun chiffre du billet ne doit servir à décider tant qu'un PDF n'existe pas.

### CR-sources-06 — Ancre sur notre modèle à la couche 15 : la source d'origine est omise ; un faux « aucun test causal » — **moyenne**

- **Où** : exécution 1.2.3 et 5.3 (seule ancre : [YS]) ; balayage-autres section 3, point 7 (« Aucun des travaux lus ne
  fait de test causal sur la direction lue »).
- **Ce que dit la source** ([YG], Ying, Ravfogel, Kriegeskorte, Hase, « The Truthfulness Spectrum Hypothesis »,
  2602.20273v1, `pdf/2602.20273.pdf`, `917ade43effae49b4ee70257961cb76a9603f702985098691dc0c5f760cfdaf7`, déjà dans le
  dossier commun) :
  - p. 3 : réplication sur **Llama-3.1-8B-Instruct** (et base) ;
  - p. 18 : aire inter-domaines par couche, « Best Layer : Layer 15 » pour Llama-8B ; jeux d'Apollo dont la sous-performance ;
  - p. 7 : **test causal** sur Llama-8B : direction ajoutée au biais de la sous-couche dense de la couche 15, effet mesuré
    sur SimpleQA.
  - [YS] p. 3 écrit suivre Ying et al. pour le choix de la couche 15.
- **Correction proposée** : ajouter [YG] comme seconde ancre (origine du choix de la couche 15 sur notre modèle) et comme
  précédent d'intervention causale ; corriger le point 7 du balayage-autres (faux : [YG] p. 7 ; voir aussi [CA] p. 1 et
  [GT] p. 1, lus par le balayage « consigne-intention »).

### CR-sources-07 — « Kirch et al. retirent la consigne » : l'exception qui touche notre cas manque — **moyenne**

- **Où** : exécution 2.2 (« Kirch et al. retirent la consigne avant de lire [KI p. 3, PDF] ») ; balayage-autres 2.4 et V1.
- **Ce que dit la source** ([KI], 2511.17408v4, `91e00c25…`, p. 3) : « The only exception for this removal is in the case
  of deception and sandbagging, for which we never remove the incentive as these are integral to their dataset prompts ».
  Le balayage « consigne-intention » l'avait relevé (section 3.2) ; la synthèse l'a perdu.
- **Correction proposée** : ajouter l'exception ; le précédent pour notre cas (tromperie, sous-performance) est [BX]
  p. 5-7, pas [KI].

### CR-sources-08 — Zone R8 (1) « décoder une valeur calculée » : plus étroite que dit ; [KT] mal résumé — **moyenne**

- **Où** : exécution fin de 1.4 (« les travaux vérifiés lisent des nombres écrits dans l'entrée ou mémorisés [KT p. 4 ;
  LG p. 1 ; HI p. 1] ») ; « Réserves » (1) ; balayage « consigne-intention » 3.3 et 7.
- **Ce que disent les sources** :
  - [KT] (2502.00873, `d1ccb4a8…`) p. 1 : les trois modèles, dont Llama3.1-8B, « construct helix(a + b) on the last
    token » ; p. 5 : états du dernier jeton bien modélisés par helix(a + b), vérifié par rapiéçage (détail sur GPT-J). La
    somme est **calculée**, absente de l'entrée.
  - [SU] (Sun, Stolfo, Sachan, 2507.12379v1, `pdf/cs-2507.12379.pdf`, `5a23e4ad…`, téléchargé ici) p. 1 : des sondes
    décodent « both the model's predicted output and the correct answer from hidden states, regardless of whether the
    model's output is correct » ; p. 2 : Gemma 2 2B IT (et Phi-3).
- **Correction proposée** : la zone restante est « décoder la valeur **honnête** pendant que l'agent écrit une valeur
  **délibérément** fausse sur consigne, pour une estimation de plusieurs jetons, à 8 milliards de paramètres ». Citer [KT]
  p. 1, p. 5 et [SU] p. 1-2 comme précédents partiels ; retirer « écrits dans l'entrée » pour [KT].

### CR-sources-09 — [CL] : 44,3 % n'est pas la lentille jacobienne seule ; la lentille R fait mieux — **moyenne**

- **Où** : exécution 3.3 (« Usage indépendant sur Llama-3.1-8B : concept de plusieurs jetons dans les dix premiers pour
  44,3 % de 2 400 textes à trous [CL p. 7] ») ; balayage-anthropic section 1.
- **Ce que dit la source** ([CL], 2608.31084v2, `d168dc95…`) : p. 7, tableau 2 : 44,3 % est le score de bout en bout de
  **« Concept Lens » instanciée avec la lentille jacobienne** (proposition + notation), pas la lentille seule ; la même
  méthode instanciée avec la **lentille R** atteint **61,9 %** sur Llama-3.1-8B, et la lentille R bat la lentille
  jacobienne sur les cinq modèles. p. 5 : versions instruites.
- **Correction proposée** : « Concept Lens (Tsinghua), fondée sur la lentille jacobienne, 44,3 % ; avec la lentille R,
  61,9 % [CL p. 7] » ; noter que l'article de la lentille R n'est pas lu (non vérifié) et qu'aucune lentille R pour Llama
  n'apparaît dans la liste de Neuronpedia lue (`web/hf-neuronpedia-jlens.json`) ; signaler [CL] comme outil candidat pour
  lire des **concepts de plusieurs jetons** (voir CR-sources-10).

### CR-sources-10 — Lentilles et nombres : le « vocabulaire fixé par construction » ignore les nombres de plusieurs jetons — **moyenne**

- **Où** : exécution 3.3 point 1 (« à t_cost, couche par couche, le rang des jetons du nombre honnête h et du nombre gonflé
  g … peu de pêche ») ; verdict ligne 3.
- **Ce que dit la source** : [KT] p. 2 : Llama3.1-8B ne code en un seul jeton que les entiers de 0 à 999. Une lentille
  classe des **jetons**. Un coût gonflé d'environ 30 fois dépasse souvent 999 : h et g s'écrivent en plusieurs jetons, et
  leurs premiers jetons peuvent coïncider (exemple à vérifier par code sur le tokenizer : si les chiffres se découpent par
  blocs de trois depuis la gauche, « 3600 » et « 36000 » commencent par le même jeton « 360 »).
- **Correction proposée** : lire la lentille sur le **premier jeton** seulement quand h et g en diffèrent (règle gelée
  avant lecture) ; sinon passer par la log-probabilité forcée des suites complètes (déjà en 2.2) ou par une méthode de
  concepts de plusieurs jetons ([CL]) ; vérifier le découpage des nombres par code, sans ouvrir de texte de P3.

### CR-sources-11 — Une grandeur « rapportée sans verdict » sert à justifier T4 — **moyenne**

- **Où** : exécution 1.1, 4e puce : corrélation 0,2570 (et −0,1180) « [V l. 224-225]. Grandeur rapportée sans verdict ; je
  ne l'interprète pas sur P3. Elle suffit à rendre T4 obligatoire ».
- **Écart** : contradiction interne ; usage d'un résultat non lu pour orienter un plan (esprit de R1 et R4). Je n'ai pas
  relu le verdict ; le constat porte sur le texte de l'exécution seul.
- **Correction proposée** : retirer ce chiffre ; justifier T4 par la mesure du comportement déjà lue (le coût seul sépare
  à 0,8878, cité par l'exécution [V l. 204]) et par la littérature ([BX] p. 5-6 ; [AP] p. 6 : la sonde est sensible à « is
  the scenario related to deception », pas seulement à la réponse).

### CR-sources-12 — [LG] : « 0,00 pour la valeur directe » mêle deux mesures — **faible**

- **Où** : exécution 1.4 (iii), troisième ligne.
- **Ce que dit la source** ([LG], 2410.11781v2, `94c1930f…`, p. 3, tableau 2) : justesse de **reconstruction exacte de
  tous les chiffres** par sondes circulaires, sur des nombres **donnés en entrée**, **Llama 3 8B** (pas 3.1) ; bases 1000 et
  2000 : 0,00 ; base 10 : 0,91. Le titre de la section : « digit values in base 10 but not the whole number value ».
- **Écart** : cela ne montre pas qu'un **ordre de grandeur** (log10 du coût) n'est pas lisible linéairement ; [HI] p. 1
  montre des représentations monotones de grandeurs numériques.
- **Correction proposée** : « si une régression du log10 échoue, essayer des sondes circulaires par chiffre ([LG] p. 3 :
  reconstruction exacte 0,91 en base 10 contre 0,00 en bases 1000 et 2000, Llama 3 8B, nombres en entrée) ».

### CR-sources-13 — Citation d'Apollo p. 18 attribuée à la mauvaise sonde — **faible**

- **Où** : exécution 1.3, ligne (b) : « Une sonde d'Apollo note trompeuse « every Sandbagging response… even when the model
  chooses not to sandbag » [AP p. 18] ».
- **Ce que dit la source** ([AP], 2502.03407v1, `a4820ad5…`, p. 18, annexe B.3) : c'est la sonde lue sur la **question de
  suivi** (« Was your last response deceptive? », réponse imposée « No »), entraînée sur « Roleplaying ».
- **Correction proposée** : préciser « sonde de question de suivi ». L'argument (la sonde lit le contexte de sous-
  performance) tient, mais pour une lecture à une seule position après coup.

### CR-sources-14 — Lentille jacobienne de Neuronpedia : provenance et voisins mal décrits — **faible**

- **Où** : exécution 3.3 point 2 (« environnement de Neuronpedia `transformers` 5.11.0 [page web] ») ; 3.6.
- **Ce que disent les sources** :
  - `web/np-llama31-8b-it-config.yaml` (page web) : environnement « backfilled 2026-09-20 … the fit did not record its
    environment » ; `jlens_commit: null` ; le dépôt de code s'appelle `anthropics/jacobian-lens` (recherche web), la
    configuration écrit `anthropics/jlens`.
  - `web/hf-neuronpedia-jlens.json` : lentilles aussi pour **Llama-3.1-8B de base**, Llama-3.3-70B-Instruct et
    **Gemma-2-9B-IT** (base des organismes « Taboo » publics, [AO] p. 5) ; lentilles « J++ » pour d'autres modèles, pas
    pour Llama-3.1-8B.
  - [JL] p. 8 : le premier tiers des couches donne des lectures « noisy and largely uninterpretable » ; p. 43 : sur
    l'organisme à objectif caché, la **lentille des logits ne fait apparaître ni « reward » ni « bias »** là où la lentille
    jacobienne les montre.
- **Correction proposée** : écrire « environnement reconstitué après coup, version du code non consignée » (R9 : empreinter
  le fichier de 1 040 197 778 octets ou réajuster la lentille avec versions consignées) ; ne pas mettre la lentille des
  logits au même rang que la lentille jacobienne ([JL] p. 43) ; noter l'option d'un contrôle positif sur un organisme
  public à secret entraîné (Gemma-2-9B-IT, lentille prête) : changement de modèle, donc GO.

### CR-sources-15 — Un lecteur publié de « consigne présente » n'est pas cité — **faible**

- **Où** : exécution 4.1 (ligne « texte privé présent » : lecteur hypothétique) ; 3.6.
- **Ce que dit la source** ([TT], Abdelnabi et al., « Get my drift? », 2406.00799v6, `pdf/cs-2406.00799.pdf`,
  `6885e422…`, téléchargé ici) : p. 1 : différence d'activations avant et après une entrée externe ; classifieur linéaire,
  aire « near-perfect » hors distribution ; code public `microsoft/TaskTracker` ; p. 6 : ligne Llama-3 8B (pas 3.1).
- **Correction proposée** : citer [TT] comme **instrument de contrôle positif du lecteur de consigne** (il doit répondre
  sur saboteur, témoin et mention) et comme direction contre laquelle projeter la sonde « oracle » de P3b ; jamais comme
  détecteur d'intention.

### CR-sources-16 — Balayage-autres : « sondes localisées … sans antériorité » — **faible**

- **Où** : balayage-autres 2.2 (« c'est l'objet de P3b, sans antériorité trouvée ici »). L'exécution ne le reprend pas.
- **Ce que dit la source** ([OBE], Obeso et al., 2509.03531v2, `pdf/cs-2509.03531.pdf`, `f72272cb…`, téléchargé ici) :
  p. 1 : sondes linéaires **au niveau du jeton** dans des réponses longues, entités inventées, quatre familles de modèles ;
  p. 2 : exemple sur Llama-3.1-8B. Ce n'est pas de la tromperie, mais la lecture localisée dans une génération longue a des
  précédents.
- **Correction proposée** : « lecture localisée : précédent pour les entités inventées ([OBE] p. 1) ; pour une tromperie
  localisée dans un champ d'action, question ouverte ».

### CR-sources-17 — Information : date du tampon arXiv de [YS] — **faible (sans conséquence)**

- Le PDF officiel de 2609.02893v1 (retéléchargé, octets identiques) porte « arXiv:2609.02893v1 [cs.CL] 1 Jul 2026 »,
  incohérent avec un identifiant de septembre 2026. Le contenu est celui d'arXiv ; la page 3 citée est exacte. À noter
  seulement si la date sert un jour à une antériorité.

---

## B. Zones dites libres : ce qui tient

| zone (où) | verdict | appui |
|---|---|---|
| (1) décoder une valeur calculée pendant qu'un chiffre faux est écrit (exécution, réserves) | **plus étroite** : précédents partiels | [KT] p. 1, p. 5 ; [SU] p. 1-2 (CR-sources-08) |
| (2) lentille jacobienne sur un agent saboteur de 8 milliards (exécution, réserves ; balayage-anthropic 13) | **question, tenue** : rien trouvé (recherche web générique, une requête) | [JL] p. 10, p. 55 ; [CL] p. 7 (factuel, pas de tromperie) |
| (3) organisme public à objectif caché sur Llama-3.1-8B-Instruct (exécution 5.1, réserves) | **mal posée** : organismes entraînés existants ; publication des poids à vérifier | [ADL] p. 5 ; [BX] p. 7 ; [DYL] p. 20 (non confirmé) ; billet de l'institut britannique (CR-sources-04) |
| rejeu « consigne retirée » comme méthode propre (exécution 2.2 ; balayage-autres V1) | **occupée** sur notre modèle | [BX] p. 5-7 (CR-sources-01) |
| aucun test causal sur la direction lue (balayage-autres 3.7) | **faux** | [YG] p. 7 ; [CA] p. 1 ; [GT] p. 1 (CR-sources-06) |
| sondes de tromperie localisées (balayage-autres 2.2) | **plus étroite** | [OBE] p. 1-2 (CR-sources-16) |
| plancher apparié en covariance « plus strict que ce qui se publie » (balayage-anthropic 11) | constat raisonnable, non contredit ici ; à garder comme constat, jamais comme revendication | [JL] p. 92 (cent mots témoins) |

## C. Contrôle symétrique (R4) : ce que j'ai relu et qui tient

Relu sur le PDF, page exacte, conforme à l'exécution :
- [JL] p. 7 (formule), p. 9 (≤ 10 % de variance), p. 10 (sonde par jeton ; modèles Claude seulement), p. 14 (« ignore X »),
  p. 21 et p. 56 (calculs automatiques hors de l'espace J ; une multiplication par couche), p. 38 (71 % → 3 % ; 0 → 13 sur
  180 ; jetons choisis sur les mêmes six scénarios, note 7), p. 42 (« reward », « bias » ; « In the baseline model, neither
  token appears on any prompt »), p. 55 (petits modèles : question des auteurs), p. 92 (cent mots témoins ; 0,853).
- [YS] p. 3 : Llama-3.1-8B-Instruct, couche 15, moyenne sur la réponse ; 0,874 / 0,706 / 0,606 ; 0,936 / 0,950 / 0,869.
- [TG] p. 3 (1 modèle sur 5), p. 7 (Cedar et Oak : Llama-3.3-70B ; Yew : copie bénigne du 8B à couches identité ; référence
  8B), p. 16-17 (sondes élevées sur Cedar ; l'équipe ne s'y est pas fiée), p. 22 (ξ = 1,094 contre 1,038 ; ≈ 2 sur
  consigne), p. 36 (Tarun et Beren : 70B).
- [DYL] p. 11 (0,85 → 0,52 ; 0,81 → 0,65 ; aires 0,91 → 0,75), p. 27 (Apollo 0,5 sur la version sur consigne, Qwen 3.5 27B).
- [LS] p. 1-2 (256 autoencodeurs, base), p. 11 (0,162 contre 0,090 à L15R-32x ; réserve des auteurs sur l'interprétation).
- [PV] p. 4 (Llama-3.1-8B-Instruct), p. 5 (0,75-0,83 ; dû surtout au type de consigne), p. 7 (0,76-0,97).
- [AO] p. 5 (quatre modèles, pas Llama-3.1-8B ; 10 heures de H100 pour Qwen3-8B), p. 6 (90 % de conversations générales).
- [AB] p. 6 (58,0 / 53,2 / 51,6 ; 22,3 contre 35,5), p. 7 (9 outils sur 12 sous l'agent par défaut).
- [KT] p. 2 (0 à 999 en un jeton) ; [KI] p. 3, p. 9 ; [GE] p. 4 (jusqu'à 60 %) ; [AU] p. 2, p. 5 (47 + 5) ; [KR] p. 2
  (≈ 1/50 du coût) ; [CRV] p. 5, p. 27 ; [TL] p. 5 (250 pas), p. 10 (injections, Pythia 12B) ; [OB] p. 1 (100 % → 0 %) ;
  [PB] p. 8-9 ; [AP] p. 22 (moyenne meilleure pour les paires sur consigne) ; [ADL] p. 5, p. 9 ; [BX] p. 1, p. 8 (0,94 →
  0,5) ; [LB] p. 1, p. 17 ; [OT] p. 3 (huit modèles dont Llama2-7B) ; [QK] p. 3 ; [ESK] p. 4, p. 15 ; [TU] p. 1, p. 3 ;
  [LQ] p. 3-4 ; [FQ] p. 1 ; [ATP] p. 2, p. 5 ; [MK] p. 1.
- Pages web (non opposables, existence seulement) : fiche andyrdt (couches 11, 15, 19, 23… vues), EleutherAI 64x et 32x
  (couches 23 et 29 seulement ; 32x : sous-couches denses), Goodfire couche 19 (licence Llama 3.1), lentilles ajustées
  (Llama-3-8B-Instruct, pas 3.1), transcodeurs de Meta (CC-BY-NC-4.0, branche `zsquaredz/circuit-tracer`).

## D. Sources ajoutées par cette critique

| clé | source | fichier | sha256 | statut |
|---|---|---|---|---|
| [BX] | Boxo, Neelappa, Raval, « Linear probes rely on textual evidence », 2509.21344v2 | dépôt `docs/sources/pdf/2509.21344v2.pdf` | `aaac4ff91c909f9e4363fe9c19bb0fc7c2a635bf91e13c178992411f2a25ee5c` | PDF, p. 1, 3, 5-8 |
| [YG] | Ying, Ravfogel, Kriegeskorte, Hase, « The Truthfulness Spectrum Hypothesis », 2602.20273v1 | `pdf/2602.20273.pdf` | `917ade43effae49b4ee70257961cb76a9603f702985098691dc0c5f760cfdaf7` | PDF, p. 3, 7, 18 |
| [SU] | Sun, Stolfo, Sachan, « Probing for Arithmetic Errors in Language Models », 2507.12379v1 | `pdf/cs-2507.12379.pdf` | `5a23e4adeda44db9f4cadbd8b38059390906e4aa6c6d867f150d77a39ff8b124` | PDF, p. 1-2 |
| [TT] | Abdelnabi et al., « Get my drift? », 2406.00799v6 | `pdf/cs-2406.00799.pdf` | `6885e4223848cffebd7131e9a71591329d00cabccee07ecfb402a444ad601e8c` | PDF, p. 1, 6 |
| [OBE] | Obeso et al., « Real-Time Detection of Hallucinated Entities », 2509.03531v2 | `pdf/cs-2509.03531.pdf` | `f72272cbe04f9e8df5982d5e520616dda9cf47cdec8674c218c13df829344bd3` | PDF, p. 1-2 |
| [EP] | Rumbelow, « Exemplar Partitioning », 2605.14347v3 | `pdf/cs-2605.14347.pdf` | `6283ea8bfe7c3f34e68dce21f98d9c140c0dc9c61590ae741531159c89bd4ad1` | PDF, p. 8 (Taboo sur Gemma-2-9B-it) |
| — | contre-épreuves d'identité : 2607.15495v1, 2609.02893v1 | `pdf/cs-2607.15495v1.pdf`, `pdf/cs-2609.02893v1.pdf` | `c906bd59…`, `b76151cd…` (égales aux copies citées) | identité |
| [WBC] | Bloom et al., « White Box Control at UK AISI — Update on Sandbagging Investigations », 10 juillet 2025 | `web-critique-sources/aisi-wbc-sandbagging-update-2025.html` (+ `.txt`) | `71d83db2e1f566786ba019760fac68ebca733eff188eef72f3a7cd70e47bd01a` (`.txt` : `8106970dc9c1409bd8e54483d862e5dcb552ecb35fc648542da5297fa24f846a`) | **page web, non opposable** |

Une recherche web a donné un résumé faux (Taboo sur Llama-3.1-8B-Instruct dans 2605.14347) ; le PDF le dément (p. 8,
Gemma-2-9B-it). Exemple de R7 tenu : aucun résumé de moteur de recherche n'est repris ici sans page.

## E. Ce que cette critique n'a pas fait

- Pas lu l'article de la lentille R, ni celui de la lentille J++, ni la source primaire de [YG] au-delà des pages citées.
- Pas vérifié si les poids des organismes de [BX] et du billet de l'institut britannique sont publics.
- Pas vérifié le découpage des nombres par le tokenizer de Llama-3.1-8B (CR-sources-10 le demande, par code).
- Pas relu le verdict de P3, le brief, P4 ni les registres : les chiffres du programme cités par l'exécution ne sont pas
  contrôlés ici (la session les a vérifiés, d'après la commande).
