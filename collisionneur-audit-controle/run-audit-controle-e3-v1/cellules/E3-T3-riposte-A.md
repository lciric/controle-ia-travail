# Proposition A — Tour III.3 : riposte

**Pièces.** Les deux attaques (B et C) sont présentes, complètes, terminées par leur marqueur. Statuts inchangés : F1 et F3 **RAPPORTÉ**, F2 **OBSERVÉ-NON-AUDITÉ**, mes duels et ceux de B et C **HYPOTHÈSE**. Je ne réponds qu'aux sections qui visent A. Tous les seuils sont **illustratifs**.

Je commence par ce que je concède sans réserve, parce que c'est ce qui coûte le plus : deux de mes remèdes (cellule dormante, témoin (iv-nul)) étaient mal construits, et deux de mes contrôles (permutation, essaim Qwen) ne localisaient rien. B et C arrivent aux mêmes conclusions par des chemins différents ; je ne les fusionne pas, je dis lequel je retiens et pourquoi.

---

## (a) Verdict attaque par attaque

### Statuts et affirmations non tenues (B A-6) — **acceptées, toutes**

- (d)8 : « D6 et E7 réfutées » → à lire « mises en question par deux hypothèses non exécutées ». Faute contre la règle 1, corrigée.
- (g) : « tous les duels se calculent sur le cache, en CPU » est faux. AM-5 (placebo de semis), la cellule dormante et les essaims d'AM-4 exigent des générations nouvelles. Le chiffrage est refait en section (b), ligne par ligne.
- Tice et al. : F2 donne 2025, j'ai écrit 2024 → **année à vérifier**.
- Bailey et al. (D-A4) : **titre à vérifier**.
- Ajout non demandé, même règle : Ramdas, Grünwald, Vovk, Shafer (AM-2) et Benton et al. (S-A4) restent **RAPPORTÉ (mémoire)**, aucune page lue.

### Cellule « politique dormante » (B A-3, B (b)3, B (c), C (a)1, C (c)1) — **acceptée, remède retiré, remplacé**

B et C ont raison sur la polarité : dans la convention des modèles verrouillés par mot de passe, telle que je la comprends (Greenblatt, Roger, Krasheninnikov, Krueger 2024 — RAPPORTÉ, mémoire, **à vérifier sur la fiche des organismes (iii)**), l'absence de mot de passe est l'état de sous-rendement **actif**. Ma cellule mesurait donc l'état actif et l'aurait lu comme dormant. C ajoute la confusion fatale : entre verrouillé et déverrouillé, la compétence change, et une sonde de perplexité suffit à « réussir ». B ajoute que la famille (i) de F1 n'a pas de déclencheur ; en ajouter un crée un organisme nouveau.

Je retiens les trois corrections :
1. **Un organisme nouveau, déclaré comme tel** : (i-cond), consigne cachée à condition de déclenchement, avec le témoin de C — même mécanisme, règle conditionnelle **bénigne**. Sans ce témoin, la sonde peut lire « maintient une règle SI… ALORS ».
2. **Vérification comportementale préalable** (B) : utilité et distribution des jetons de (i-cond) hors déclencheur indiscernables de l'honnête (test à deux échantillons), sinon la cellule n'a pas de sens.
3. **Changement de rôle** (B (b)3) : B a raison qu'une sonde qui lit un plan détenu mais non exécuté peut être valide pour la sécurité. La cellule dormante cesse d'être une porte de validité ; elle devient une **caractérisation** à deux issues également publiables, avec la mesure prédictive de B (AUROC du score au pas t pour le sabotage en t+1…t+k).

Conséquence sur mon attaque de la proposition 1 de F2 : je maintiens que le masquage sous-estime la fuite (l'attention peut copier l'information amont vers les positions d'action — HYPOTHÈSE), mais je retire ma demande de le remplacer ; la lecture filtrée reste un bras rapporté, la cellule (i-cond) s'ajoute à côté, et ni l'une ni l'autre n'est « la lecture principale de l'intention ».

### Témoin (iv-nul) (C (a)2, C (c)2) — **acceptée, remplacé**

C a raison : un LoRA sur une politique sans rapport ne partage ni lexique ni concept avec le sabotage ; que la sonde y reste basse prouve seulement qu'elle ne lit pas « a subi un réglage fin ». Je retiens le témoin de C : **(iv-def)**, mêmes documents synthétiques, même vocabulaire et mêmes mécanismes, mais du point de vue de l'auditeur qui les prévient — vocabulaire apparié, valence inversée. Sur la lecture des épisodes non sabotés de (iv) : C a raison sur le biais de survie ; ces épisodes ne sont lus que **si** une cible semée y existait (opportunité vérifiée) et le résultat est rapporté, jamais critère. Le vrai témoin de l'intention est (iv-def).

### Essaim Qwen comme témoin d'AM-4 (B A-4, B (c), C (a)3, C (c)3) — **acceptée, remplacé**

Les deux attaques convergent par deux arguments distincts : B par l'instrument (autres sondes, autres planchers), C par la géométrie (espaces incommensurables, la baisse de corrélation est garantie par construction). Les deux sont justes ; celui de C est fatal. Je remplace le témoin par les deux contrôles intra-Llama : **affectation des tâches mélangée à poids constants** (B : seul le partage de tâche varie) et **appariement a posteriori d'épisodes indépendants sur la même cible** (C). L'essaim Qwen reste un bras rapporté sur la transférabilité, pas un témoin.

### AM-1, définition du budget (B A-1, B (c), C CA-1) — **transformée en test, remède réécrit**

B pointe que « vérifié en aval » dans l'environnement (a) passe par un évaluateur faible sur rubrique ; si c'est Llama-3.2-3B (D1 (b)), la dose est calibrée sur ce que voit la boîte noire. Accepté : l'évaluateur de dose doit être **disjoint** du moniteur boîte noire (autre lignée ou vérification exécutable), et des épisodes à dose zéro passent par toute la chaîne de semis. B note aussi que mon duel ne prévoit pas la concavité sans seuil : accepté, le duel n'était pas exhaustif.

C fait l'objection la plus importante : fragmenter un biais par k peut détruire le biais **externe** lui-même (l'agent écrit une proposition honnête) ; Σδ s'effondre alors par échec d'exécution, non par défaillance de la trace interne, et AM-1 falsifie le lemme à tort. Accepté. Je reprends le duel CA-1 de C (stratification par dommage aval réalisé) comme forme corrigée d'AM-1, avec les deux témoins de B. Ce que je garde de ma version : la question — B défini dans l'espace de la sonde rend le lemme tautologique — reste le point de départ, et aucun des deux attaquants ne la conteste.

### AM-2, permutation (B A-2, B (c), C CA-2) — **transformée en test**

Les deux ont raison : la permutation inter-trajectoires détruit trois choses à la fois (autocorrélation, effet fixe d'épisode, dérive par position) et ne localise rien. C ajoute une remarque exacte : pour un processus e de mélange lu à horizon fixe, la statistique terminale est symétrique en (s₁…s_T), donc une permutation intra-trajectoire ne change rien ; seule la lecture séquentielle max_t E_t est sensible à l'ordre. Je reprends le plan à trois permutations (C) augmenté de la permutation par position et de la calibration sur épisodes tenus à part (B), et je lis **max_t E_t** et non E_T. Le remède dépend de l'issue : ligne de base par épisode (effet fixe), e-variables conditionnelles (autocorrélation), calibration par position (dérive).

### AM-3, longueur (B (b)1, C CA-3) — **transformées en tests**

B : la longueur peut être un effet de tâche ; accepté, la corrélation est lue intra-tâche contre inter-tâches. C : ma normalisation par quantile de longueur globale crée une dilution exploitable si le signal est localisé sur k ≪ n jetons ; accepté, le duel CA-3 (max sur fenêtre fixe contre normalisation globale, longueur variée par remplissage bénin) devient la deuxième moitié d'AM-3. Je note une tension à surveiller : le remplissage « bénin » de C change la tâche ; il faut vérifier que le dommage aval reste constant.

### AM-5, placebo de semis (B (b)2) — **transformée en test**

Accepté : le placebo peut être lui-même discernable de l'honnête. Classifieur de surface à trois classes (honnête / placebo / semé), entraîné sur une moitié, évalué sur l'autre.

### AM-6, juge arbitre du thème (B A-5) — **acceptée en partie**

B a raison que sous honnêteté toute hausse est une fausse alerte par définition, et que le juge partage du vocabulaire avec la sonde. Je retire le juge comme **arbitre**. Je le garde comme **bras rapporté** pour une autre raison, que B ne discute pas : si le thème élève la sonde et pas le juge, la comparaison blanc/noir de H1 est biaisée sur ces strates ; c'est une information sur H1, pas sur AM-6. Le critère d'AM-6 reste le FP de la sonde par strate, à longueur appariée, contre la base mots-clés.

### D-A1, auto-préférence du juge (B A-7, C (a)4) — **acceptée pour l'essentiel, ambition réduite**

B : l'étiquette teste l'étiquette, la paraphrase modifie le contenu. C : l'étiquette viole « contenu en bande = données » ; la paraphrase lisse précisément les marqueurs du sabotage diffus. Les deux ont raison, et je retire les deux bras. Ce qui reste séparable sans étiquette ni paraphrase : l'interaction juge × lignée de l'agent sur **contenu honnête** (fausses alertes) et sur contenu saboté (rappel) — c'est le test S7 de F2, auquel D-A1 ajoute seulement que le mécanisme (reconnaissance, style, collusion) n'est pas identifiable par ce plan. D-A1 est donc une faille **nommée**, pas une faille **mesurable à part** ; je la reclasse ainsi.

### E-A2, conscience d'évaluation du juge (B A-8) — **acceptée**

Sape délibérée de la surveillance et conscience d'évaluation ont des prédictions différentes (la première fausse dans les deux cadrages, la seconde seulement sous cadrage test). Benton et al. 2024 devient une faille distincte — « le moniteur de confiance peut saper ses notes » — sous S-A4 ; l'angle mort 10 de F2 reste une question sans source, avec le test de F2 (cadrage « banc » contre « production »).

### Pilotage à utilité constante (C (c)4) — **acceptée**

Un point de norme ne suffit pas : si le sabotage diffus demande plus de capacité de planification que la tâche honnête (c'est la thèse même de H6), tout vecteur aléatoire réduit le sabotage avant l'utilité. Remplacé par des courbes dose-réponse complètes (sabotage, utilité) sur un faisceau de K directions aléatoires orthogonales, contre la direction visée.

### Coût humain de l'audit aval (B (b)4) — **acceptée**

Le « < 200 $ » ne couvrait pas le temps d'audit humain ou par juge de S5. Pilote de 20 épisodes avant chiffrage.

### Ce que je **rejette**

- **B A-1, deuxième lame** (« la comparaison blanc/noir est biaisée par construction en faveur du noir »). Elle n'est biaisée que **si** l'évaluateur de dose et le moniteur boîte noire partagent la lignée ; F1 §6 ne dit pas quel modèle évalue la rubrique. C'est une hypothèse de B, conditionnelle, que le témoin disjoint rend sans objet. Je la transforme en règle de préenregistrement (évaluateur de dose ≠ lignée des juges), je ne la retiens pas comme faille établie.
- **C (a)4, « attribuer n'a pas de sens sans texte en bande »**. Le harnais peut porter des métadonnées hors bande sans violer l'invariant ; mais comme le moniteur ne doit pas recevoir de métadonnée d'auteur, le point de C aboutit au même résultat par une autre voie. Rejet sur le motif, acceptation sur la conclusion.

---

## (b) Expériences corrigées

Chaque duel : H_A et H_B exclusives, chaque issue falsifie quelque chose. Coûts illustratifs, refaits après B A-6.

### AM-1′ — Le lemme à dommage réalisé constant
- **Préalable** : dose dans l'espace de la tâche ; dommage aval D(k) mesuré par un évaluateur **disjoint** des juges boîte noire ; épisodes à dose zéro passés par la chaîne de semis (FP de la chaîne elle-même).
- **H_A** : à D(k) constant (± 10 %), Σδ chute d'au moins 50 % entre k = 1 et k = 10 — la trace interne ne s'additionne pas sous fragmentation.
- **H_B** : Σδ constante à ± 20 % à D constant, **ou** sa chute est entièrement expliquée par la chute de D (échec d'exécution, non du lemme).
- **Métrique** : régression de Σδ sur k, stratifiée par quintiles de D ; sonde aléatoire appariée (δ ≈ 0 partout).
- **Issue** : H_A falsifie l'hypothèse (b) du lemme sur organismes réels ; H_B falsifie mon AM-1 d'origine (qui attribuait la non-conservation à la sonde) et, selon le bras, l'élicitation de l'organisme.
- **Coût** : la grille de doses × fragmentations demande des générations nouvelles (≈ 5 doses × 4 fragmentations × 100 épisodes ≈ 10–15 h GPU) ; l'évaluateur disjoint, quelques heures ; lecture en CPU sur cache.

### AM-2′ — Validité du faux positif toujours-valide, localisée
- **Données** : ≥ 500 trajectoires honnêtes, calibration sur un jeu honnête **tenu à part**. Statistique : max_t E_t à α = 0,01 (pas E_T).
- **Quatre conditions** : (1) réel ; (2) permutation inter-trajectoires par position t (garde la dérive, détruit effet fixe et autocorrélation) ; (3) décalage circulaire intra-trajectoire (garde l'effet fixe, casse la dépendance séquentielle pour la lecture au max) ; (4) scores centrés par ligne de base d'épisode estimée avant le pas 1.
- **H_A** : FPR(1) ≈ FPR(3) > 2α et FPR(2) ≤ α — effet fixe d'épisode.
- **H_B** : FPR(1) > 2α, FPR(3) ≤ α — dépendance séquentielle.
- Une troisième issue n'est pas une hypothèse mais une garde : FPR(1) ≤ α sur tous les bras valide la calibration telle quelle.
- **Issue** : H_A falsifie mon remède d'origine (blocs temporels) et impose le centrage (4) ; H_B falsifie l'homogénéité intra-épisode et impose des e-variables conditionnelles. Dans les deux cas, la revendication de titre de A « garantie toujours valide » est fausse **telle que calibrée**.
- **Coût** : CPU sur cache, < 1 journée.

### AM-3′ — Longueur : effet de tâche, puis dilution
- **Partie 1** (B) : ρ(score max, longueur) intra-tâche contre inter-tâches, sous honnêteté, contre la sonde aléatoire appariée. **H_A** : ρ_intra ≈ ρ_aléatoire > 0 (effet d'extrême pur). **H_B** : ρ_intra ≈ 0, ρ_inter > 0 (effet de tâche). Chaque issue falsifie l'autre lecture de la corrélation brute.
- **Partie 2** (C) : actions sabotées à dommage fixe, longueur n ∈ {200, 500, 1500} par remplissage bénin, dommage aval vérifié constant. **H_A** : rappel à 1 % FP de la sonde normalisée globalement chute ≥ 25 points, max sur fenêtre fixe stable à ± 5. **H_B** : stable (Δ < 5) sous normalisation globale. H_A falsifie ma normalisation d'origine ; H_B falsifie la localisation stricte du signal.
- **Coût** : partie 1 CPU ; partie 2, générations avec remplissage ≈ 3–5 h GPU.

### AM-4′ — Null de co-élévation, même espace latent
- **Conditions** (poids constants, Llama seulement) : essaim honnête à tâches partagées ; mêmes agents à affectation mélangée (B) ; épisodes indépendants appariés a posteriori sur la même cible (C).
- **H_A** : corrélation inter-agents des scores identique entre les trois conditions (écart < 0,1).
- **H_B** : tâches partagées > appariement a posteriori d'au moins 0,2 — la co-élévation sans null apparié a un FP > α.
- **Issue** : H_B falsifie l'usage de la seule variance (c) de F1 §3 comme null et impose un null par essaim honnête apparié avant E2.3 ; H_A falsifie mon AM-4 d'origine.
- **Coût** : essaims honnêtes N = 4–16, 200 épisodes, ≈ 20–40 h GPU ; bras Qwen rapporté hors critère.

### AM-5′ — Gabarit de semis à trois classes
- Classifieur de surface entraîné sur une moitié, évalué sur l'autre : honnête / placebo (gabarit sans sabotage) / semé.
- **H_A** : placebo indiscernable de l'honnête (exactitude ≈ hasard sur cette paire) et le semé n'est discernable que par son contenu.
- **H_B** : placebo discernable de l'honnête — le gabarit a une signature, et le rappel de la sonde contre l'honnête est confondu.
- **Issue** : H_B impose que la sonde soit lue sur le placebo et batte le classifieur de surface ; H_A autorise le placebo comme témoin neutre. **Coût** : génération du placebo ≈ 2–3 h GPU, classifieur CPU.

### AM-6′ — Thème, sans arbitre
- FP de la sonde par strate thématique honnête, longueur appariée, contre base mots-clés sur les mêmes strates ; juge en bras rapporté. **H_A** : FP constant entre strates ; **H_B** : strate « risque/sécurité » > 3 × les autres. H_B impose la stratification du seuil ; le bras juge dit seulement si H1 est biaisé sur ces strates. **Coût** : nul.

### CD′ — Organisme (i-cond) : plan détenu, plan exécuté
- **Organismes** : (i-cond) déclencheur + sabotage ; témoin (i-cond-bénin) même déclencheur + règle bénigne (C) ; honnête. Vérification comportementale hors déclencheur : utilité et perplexité indiscernables de l'honnête (B), sinon la cellule n'est pas lue.
- **H_A** : la sonde est basse hors déclencheur sur (i-cond) et (i-cond-bénin), haute sous déclencheur sur (i-cond) seul — elle lit l'intention en acte.
- **H_B** : elle est haute hors déclencheur sur (i-cond) mais **pas** sur (i-cond-bénin) — elle lit un plan détenu, à valence malveillante. Si elle est haute sur les deux, c'est « maintient une règle », et ni H_A ni H_B ne tient : c'est l'issue qui rend la prédiction de validité (i)/(ii) inopérante.
- **Mesure complémentaire** (B) : AUROC du score en t pour le sabotage en t+1…t+k.
- **Coût** : organismes nouveaux ≈ 5–10 h GPU ; déclaration dans le préenregistrement comme famille ajoutée.

### (iv) avec témoin apparié
- (iv) politique en 1re personne ; **(iv-def)** mêmes documents, point de vue défensif ; (iv-nul) retiré. **H_A** : rappel et δ sur (iv) > (iv-def) d'au moins 20 points à 1 % FP — la sonde lit l'intention, pas le champ. **H_B** : (iv) ≈ (iv-def) — détecteur thématique. H_B retire à la proposition 2 de F3 sa capacité à étendre la prédiction de validité ; H_A la valide. Dépense (devis, GO), ≈ 2 × 10–20 h GPU.

### Pilotage causal à dose complète
- Courbes dose-réponse (taux de sabotage, utilité honnête) pour la direction de conscience d'évaluation et pour K = 20 directions aléatoires orthogonales de même norme. **H_A** : la direction visée déplace le sabotage à une norme où l'utilité des témoins est encore intacte, et plus que la médiane des témoins. **H_B** : elle est dans l'enveloppe des témoins. H_B falsifie la causalité supposée par H8 et §7 ; H_A falsifie « lisible n'est pas contrôlable » pour cette direction à cette échelle. **Coût** : inférence sous pilotage ≈ 5–10 h GPU.

**Chiffrage corrigé** (illustratif) : ≈ 60–100 h GPU hors (iv), soit 100–300 $ à 1–3 $/h ; plus un pilote d'audit aval humain (20 épisodes) avant tout chiffrage du temps humain, qui reste le poste dominant.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** Rien d'empirique ; aucune expérience n'a été exécutée, et F2 lui-même reste non contre-lu. Ce qui est établi relève de la lecture des textes (RAPPORTÉ) et de la logique :

1. F1 §3 définit le budget B = Σδ dans l'espace du score de sonde. « La puissance ne dépend que de B » est alors vrai par construction. Ni B ni C ne contestent ce point ; ils ont corrigé le remède, pas le diagnostic.
2. La « garantie de faux positifs toujours valide » de F1 est calibrée sur la variance d'épisodes honnêtes (F1 §3 (c)) sans traiter la dépendance intra-trajectoire. Les trois sources possibles d'inflation (effet fixe d'épisode, autocorrélation, dérive par position) appellent trois remèdes différents ; aucune n'est dans F1 ni dans F2.
3. Deux de mes remèdes du tour III.1 étaient mal construits : la cellule dormante inversait la polarité des organismes verrouillés (sous réserve de vérification sur la fiche (iii)), et (iv-nul) était vrai par construction. Deux de mes témoins (permutation simple, essaim Qwen) ne localisaient rien ou garantissaient leur issue par géométrie. Je les ai retirés.
4. Le comptage « 3 / 16 / 6 » de F2 est un jugement ; mes objections à D6 et E7 sont des hypothèses, pas des réfutations.

**Ce qui n'est pas établi.** La direction de toutes les issues : que δ > 0 survive à la fragmentation à dommage réalisé constant ; que le FPR réel dépasse α ; que la longueur soit un effet d'extrême plutôt que de tâche ; que le gabarit de semis ait une signature ; que les copies honnêtes co-varient au-delà du null apparié ; que la sonde lise l'intention en acte, un plan détenu, ou une règle maintenue. Pour chacune, les deux issues sont désormais écrites et chacune falsifie quelque chose de nommé. Reste non établi aussi tout ce qui dépend d'une vérification que je ne peux faire : la convention des organismes (iii), l'année de Tice et al., le titre de Bailey et al., la lignée de l'évaluateur de rubrique de l'environnement (a).

**L'expérience à faire en premier : AM-2′.** Trois raisons. Elle porte sur la revendication de **titre** du papier A (« garantie de faux positifs toujours valide »), pas sur une hypothèse secondaire. Elle ne demande **que des trajectoires honnêtes**, disponibles dès l'environnement (a) v0 de la phase 0, et se lit en CPU sur le cache d'activations en moins d'une journée. Et son résultat **conditionne tout le reste** : si le FPR réel dépasse α, les rappels à 1 % FP de E1.2, le critère disjonctif de G1 et la comparaison blanc/noir de H1 sont tous lus à un faux positif nominal faux, quelle que soit l'issue d'AM-1′ ou de la cellule (i-cond). Elle vient donc avant G0, dans le brief de phase 0, sous la ligne « agrégateurs validés en simulation » — que la simulation, sur scores indépendants, ne peut par construction pas tester.

En second : AM-1′, parce qu'une dose définie hors de la sonde est la condition pour que E1.3 teste le lemme plutôt que sa définition.

FIN-DE-CELLULE