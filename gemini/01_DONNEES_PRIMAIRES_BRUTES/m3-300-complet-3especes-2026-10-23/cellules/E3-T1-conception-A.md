# Proposition A — Tour III.1 : conception ciblée, à l'aveugle

## 0. État des pièces reçues (une ligne par défaut constaté)

- **Annexe 3, champions `gemini-4-argon` #01 à #10** : neuf textes sur dix sont visiblement coupés avant ou pendant la section 3 (fins de type « *…un ensemble $S_p$ de* », « *…\mid \text{Llama* », « *…- **Ét* ») et #08 n'a pas de section 3 ; le délimiteur `FIN-DE-CHAMPION-M3` est présent mais ne garantit rien sur le contenu. L'affirmation de l'arbitre « zéro caractère coupé » est donc **RAPPORTÉE et contredite par la pièce** ; je n'invente pas le contenu manquant (duels, contrôles) de ces dix textes.
- **Annexe 1 vs énoncé** : la somme des « valides » donne 81 Fable + 95 Opus + 71 Argon = 247, pas 300 ; le statut des 53 non valides dans les moyennes est inconnu.
- **Annexe 2 vs Annexe 3** : le champion Fable #08 (LMHC, k=056, 4,27) et les champions Argon #07, #08, #10 (0,85 ; 0,75 ; 0,71) n'apparaissent pas dans le Top 20 de l'Annexe 2 ; compatible avec une sélection DPP par diversité, mais le noyau DPP n'est pas donné.
- **Propositions B et C** : non transmises à ce tour (conception à l'aveugle) ; aucune attaque ni réutilisation possible.
- **Modèles cités dans les champions** (« Claude-3.5-Sonnet », « Gemini-Flash », Argon #03) : absents du socle VÉRIFIÉ.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut réel | Pourquoi ce n'est pas établi |
|---|---|---|---|
| A1 | Les scores `jev-1.14.0` sont de « vrais scores » de qualité des lois proposées. | OBSERVÉ-NON-AUDITÉ | Aucune calibration, aucun accord inter-juges, aucune vérité de terrain n'est dans le socle. `jev` est un classifieur non génératif (VÉRIFIÉ) ; ce qu'il mesure au-delà d'un composite n'est pas spécifié. |
| A2 | L'écart d'espèce (Claude ≈ 4, Argon ≈ 0,6) reflète « la manière dont Fable, Opus et Argon conçoivent l'auto-organisation ». | HYPOTHÈSE | Alternative non exclue : artefact de longueur/troncature. Les dix champions Argon sont coupés avant la section « Duel », et leurs sous-scores `Duels` (0,06–0,27) et `Contrôles` (0,04–0,11) sont précisément ceux qu'une section manquante met mécaniquement à zéro. La « rigueur » Argon (1,4–2,1) chute moins que le composite. |
| A3 | Les 10 vagues de déflation ont un « effet réel ». | HYPOTHÈSE | Seule Fable montre une tendance (3,33 → 4,19 ; surtout par disparition des minima catastrophiques 0,02–0,16 après V08). Opus est plat (3,88–4,25), Argon plat (0,51–0,80). Pas de bras témoin sans déflation ; vague et ordre temporel sont confondus. |
| A4 | Les trois espèces constituent trois « domaines de faute » indépendants (prémisse de l'appariement chimère pour `H4'`). | HYPOTHÈSE | Observation dans la pièce : à (V01, k=007, Cône-07) Fable, Opus **et** Argon produisent tous trois un « Reine-Rouge/réplicateur » ; à (V02, k=012, Cône-02) Fable et Opus produisent tous deux « RFOT-Franz-Parisi » ; idem (V02,k=014), (V01,k=010), (V03,k=023). Le prompt de cône semble déterminer le bassin plus que les poids. La corrélation « par prompt partagé » n'est pas distinguée de la corrélation « par poids partagés ». |
| A5 | Les champions à haut score « résistent à Goodhart » et cela se juge à la lecture. | HYPOTHÈSE | Tous les champions déclarent un terme anti-Goodhart ; aucun n'a été soumis à une pression d'optimisation mesurée. Résister sur le papier n'est pas une mesure. |
| A6 | Un collisionneur à T=3 est « sous-optimal ». | Prémisse mixte | Que la riposte du tour 3 n'est pas attaquée est **VÉRIFIÉ par construction** du protocole. Qu'un T adaptatif ferait mieux à budget constant est une **HYPOTHÈSE** sans métrique définie. |
| A7 | Le « taux de nouvelles failles fatales » peut tomber à zéro observablement (point fixe de Nash-Popper, arrêt de Wald). | HYPOTHÈSE | On n'observe que les failles *détectées* ; le taux de failles non détectées est un problème d'espèces non vues. Un arrêt sur « zéro nouveau » sans estimateur de la masse manquante (Good-Turing, Chao1 ; références à vérifier) confond saturation du détecteur et épuisement des failles. |
| A8 | Les duels des champions sont exécutables « à budget constant ». | Contredit par le VÉRIFIÉ | Budget socle : 100 + 20 USD au total. Les champions demandent 120 USD *par bras*, 3–4 bras, 30 graines, 200 tâches (ex. Opus #06, #07 ; Fable #08, #10). Ordre de grandeur illustratif : 200 × 4 × 30 = 24 000 exécutions ; à 0,01 USD l'unité, 240 USD. Aucun champion n'est exécutable tel quel. |
| A9 | `jev-1.14.0` fournit des plongements, des vraisemblances $p(o\mid s)$, une relation d'implication `jev(u⊨v)`, une classe « récitation paramétrique ». | HYPOTHÈSE | Le socle décrit `jev` comme classifieur/moniteur non génératif à score composite. Les champions Fable #05, #08, #09, Opus #01, #02, #03, #10 et tous les Argon lui prêtent des sorties non attestées. |
| A10 | `H4'`, `H5`, `H7`, `H9` sont des cadres acquis pour construire $\mathcal{L}^*$. | HYPOTHÈSE (Papier B) | Déclaré tel dans le socle ; `H9` n'a pas de métrique de dérive validée (le verdict nul de `P3` sur les sondes linéaires est VÉRIFIÉ, pas une mesure de dérive). |
| A11 | La sélection DPP produit des champions plus divers que le Top 10 par score. | RAPPORTÉ | Vérifiable gratuitement (distance de compression entre textes), non vérifié. |
| A12 | Il existe des tâches `controle-ia` ($\mathcal{M}_1$) prêtes à servir de banc d'essai à un essaim. | Non établi | Le socle liste des ancrages empiriques, pas un jeu de tâches avec vérité de terrain ; « aucune tête de sabotage, aucune sonde temps réel » (VÉRIFIÉ). |

Conséquence pour la question 2 (« fusionne les meilleures briques ») : fusionner trente hypothèses non testées produit une hypothèse de rang supérieur, pas une loi. Je n'en extrais que des briques testables à 120 USD ; le reste est à attaquer, pas à harmoniser.

---

## (b) Expériences décisives (duels $H_A \perp H_B$)

Toutes utilisent la **faille plantée** comme vérité de terrain, seule vérité constructible sans annotateurs ni sondes : à partir d'un texte honnête $x$, on fabrique $x'$ en injectant une faille de type (i) citation fabriquée non résolvable Crossref/S2, (ii) chiffre incohérent entre deux sections, (iii) hypothèse rédigée comme résultat, (iv) contrôle négatif identique au bras testé (contrôle vide), (v) section Duel supprimée. Chaque $x'$ a son jumeau honnête $x$ : cas appariés.

### E1 — L'écart d'espèce est-il conceptuel ou un artefact de format ?

- $H_A$ : l'écart `jev` Claude/Argon persiste quand les formats sont appariés (Argon complété jusqu'à la section 3 ; Claude tronqué au même nombre de caractères qu'Argon).
- $H_B$ : l'écart s'effondre sous appariement ; `jev` mesure la présence des sections, pas la conception.
- Protocole : (1) tronquer les 20 champions Claude à la longueur médiane des champions Argon → scorer par `jev` (coût 0) ; (2) relancer les 10 Argon avec la même consigne et `max_tokens` doublé pour obtenir la section 3 → scorer. Régression gratuite préalable sur les 247 valides : score composite ~ longueur + nombre de sections.
- Métrique : $\Delta = \bar S_{\text{Claude}} - \bar S_{\text{Argon}}$ avant/après appariement.
- Seuil (illustratif) : $H_B$ retenue si l'appariement réduit $\Delta$ de ≥ 50 % ; $H_A$ retenue si réduction < 20 % ; entre les deux, non concluant.
- Contrôle négatif : tronquer les textes Claude en supprimant une section **non évaluée** (par exemple le titre `BASSIN_MATH`) de même longueur ; si le score chute autant, `jev` est un compteur de caractères.
- Ce que chaque issue falsifie : $H_A$ vraie falsifie « Argon ne sait pas concevoir » **n'est pas réfuté** mais A2 devient recevable ; $H_B$ vraie falsifie A1 et A2 d'un coup et invalide toute comparaison inter-espèces de l'Annexe 1.

### E2 — La déflation séquentielle agit-elle, ou l'ordre temporel ?

- $H_A$ : la consigne de vague 10 appliquée *en premier* à des clones frais donne le score de la vague 10 (≈ 4,19 Fable) ; l'effet est dans la consigne.
- $H_B$ : la consigne de vague 10 appliquée en premier donne le score de vague 1 (≈ 3,33) ; l'effet vient de l'historique (ou n'existe pas, cf. Opus plat).
- Protocole : 2 consignes (V01, V10) × 2 ordres × 10 clones Fable = 40 appels ; idem Opus, 40 appels. Score `jev` gratuit.
- Métrique : fraction de clones sous 1,0 (les « catastrophes ») et moyenne.
- Seuil (illustratif) : $H_A$ si l'effet de consigne explique ≥ 70 % de la différence V01–V10 ; $H_B$ si ≤ 30 %.
- Contrôle négatif : une consigne « placebo » (V01 reformulée sans contenu de déflation) ; si elle produit l'effet, c'est la reformulation, pas la déflation.
- Issues : $H_A$ falsifie l'hypothèse « vagues = simple sélection par survie des valides » ; $H_B$ falsifie A3 et rend inutile le coût des 10 vagues pour Opus et Argon.

### E3 — Tours adaptatifs (arrêt séquentiel) contre T = 3 fixe

- $H_A$ : un collisionneur à arrêt séquentiel (arrêter quand $m$ passes Red-Team consécutives ne révèlent aucune faille plantée nouvelle, SPRT sur le taux de découverte, $\alpha=\beta=0{,}05$) laisse **moins de failles plantées non détectées par dollar** que T=3.
- $H_B$ : à budget égal, l'arrêt adaptatif laisse autant ou plus de failles non détectées, parce que les failles non détectées après le tour 2 sont celles que le détecteur ne voit pas du tout — prolonger ne sert à rien.
- Protocole : 20 textes honnêtes (champions Claude) × 3 failles plantées chacun = 60 cibles ; bras A : adaptatif, bras B : T=3 fixe ; même budget par bras (illustratif : 30 USD).
- Métrique primaire : rappel des failles plantées à l'arrêt ; secondaire : coût à l'arrêt, nombre moyen de tours.
- Seuil (illustratif) : $H_A$ si rappel$_A$ − rappel$_B$ ≥ 0,15 à coût ≤ ; $H_B$ si ≤ 0,05 ou coût$_A$ > 1,3 × coût$_B$ sans gain.
- Contrôle négatif : arrêt **aléatoire** à nombre de tours espéré égal à celui du bras A ; si le contrôle égale A, la règle d'arrêt est inerte et seul le volume de tours compte.
- Issues : $H_A$ vraie réfute « le T=3 est suffisant » ; $H_B$ vraie réfute A6 et A7, et montre que la ressource à ajouter n'est pas un tour mais un détecteur différent.

### E4 — Chimère contre monoculture au Red-Team : poids ou prompt ?

- $H_A$ (H4' au niveau des poids) : un Red-Team d'une autre famille (Opus attaque Fable ; Llama-3.1-8B local attaque Claude) détecte plus de failles plantées qu'un Red-Team de même famille, **à prompt identique**.
- $H_B$ (corrélation par prompt) : varier le prompt du Red-Team à famille constante produit un gain égal ou supérieur à varier la famille à prompt constant.
- Protocole factoriel 2×2 : {même famille, autre famille} × {même prompt, prompt resémancé} ; 60 cibles de E3 réutilisées.
- Métriques : rappel des failles plantées ; taux de fausse alerte sur les jumeaux honnêtes ; similarité des sorties entre attaquants (distance de compression, coût 0).
- Seuil (illustratif) : $H_A$ si l'effet « famille » > effet « prompt » de ≥ 0,10 de rappel ; $H_B$ si l'inverse.
- Contrôle négatif : deux instances de même famille, même prompt, graines différentes — plancher de corrélation.
- Issues : $H_A$ vraie soutient `H4'` et la règle de chimère forcée (Opus #06, Fable #06) ; $H_B$ vraie falsifie l'appariement « monoculture vs chimère » comme levier principal et dit que $\mathcal{L}^*$ doit router sur la **diversité de consigne**, plus bon marché (la pièce elle-même — bassins identiques à (V,k) fixés — penche vers $H_B$, statut OBSERVÉ-NON-AUDITÉ).

### E5 — Les objectifs « anti-Goodhart » tiennent-ils sous pression ?

- $H_A$ : sous sélection *best-of-n* sur `jev` ($n=8$, illustratif), le score `jev` et le taux de citations résolues Crossref/S2 montent ensemble (corrélation de rang ≥ 0,5).
- $H_B$ : `jev` monte, les citations résolues stagnent ou baissent : découplage.
- Protocole : 10 consignes de synthèse bibliographique ; pour chacune, 8 tirages Fable, sélection du meilleur `jev` ; comparaison au tirage médian.
- Métriques : $\Delta$`jev`, $\Delta$(taux de DOI résolus), $\Delta$(longueur).
- Seuil (illustratif) : $H_B$ si $\Delta$`jev` > 0,5 et $\Delta$DOI ≤ 0.
- Contrôle négatif : sélection *best-of-n* sur la longueur seule ; si elle reproduit $\Delta$`jev`, `jev` récompense la verbosité.
- Issues : $H_A$ rend recevables les termes « $-\lambda\,\mathrm{KL}(\pi_{\text{juge}}\|\pi_{\text{biblio}})$ » (Fable #01) et « $V_{\text{ext}}$ » (Opus #02) comme garde-fous ; $H_B$ falsifie A5 pour tout champion dont la récompense contient `jev` (Fable #01, #03, #07 ; Opus #05, #09) et impose que `jev` ne soit jamais dans la récompense, seulement dans la topologie (position d'Opus #03, à tester, non à adopter).

---

## (c) Instruments nommés : mesure minimale de fonctionnement

| Instrument | Taux à mesurer | Cas honnêtes appariés | Vérification mécanique à battre | Verdict « ne fonctionne pas » (illustratif) |
|---|---|---|---|---|
| `jev-1.14.0` (sous-scores Rigueur, Duels, Contrôles, Hyp=Rés) | Détection des 5 types de failles plantées ; fausses alertes sur jumeaux honnêtes. | 60 paires $(x, x')$ de E3. | (1) Résolution Crossref/S2 des DOI ; (2) comptage de sections et de mots ; (3) détection regex de troncature. | AUC `jev` − AUC(longueur + sections) < 0,10 ; ou fausse alerte > 20 % sur honnêtes ; ou sous-score `Hyp=Rés` ne séparant pas (iii) de son jumeau. Note : la direction de `Hyp=Rés` n'est pas définie dans le socle. |
| Red-Team du collisionneur (tour 2) | Rappel des failles plantées ; fausses alertes. | Mêmes 60 paires. | `jev` seul ; Crossref seul. | Rappel ≤ celui de Crossref + regex ; ou fausse alerte > 25 %. |
| Arrêt de Wald / point fixe Nash-Popper | Taux d'arrêt-manqué : P(arrêt alors qu'une faille plantée reste) ; surcoût. | Textes avec 0 faille plantée (l'arrêt doit être rapide). | T=3 fixe ; arrêt aléatoire. | Arrêt-manqué non inférieur à T=3 à coût égal. |
| Déflation séquentielle | Effet de consigne vs effet d'ordre (E2). | Consigne placebo. | Aucune (c'est un traitement). | Effet ≤ placebo. |
| Sélection DPP | Distance de compression moyenne entre champions. | Top 10 par score. | Tirage aléatoire de 10 parmi les 100. | Diversité DPP ≤ diversité Top 10. |
| 10 cônes mathématiques | Part de variance du bassin (nom + formule) expliquée par le cône vs par l'espèce (classification croisée gratuite). | — | — | Si cône > espèce, A4 est atteinte et le « routage inter-espèces » perd son fondement. |
| Appariement chimère/monoculture | E4. | Paires même famille/même prompt. | Variation de prompt. | Effet famille ≤ effet prompt. |

Observation gratuite à faire **avant tout appel payant** : la corrélation, sur les 247 valides, entre score composite et longueur du texte ; et entre composite et présence d'une section « Duel ». Si $\rho > 0{,}8$ (illustratif), A1 tombe sans dépenser un centime.

---

## (d) Ancrage matériel et spécification minimale

### Modèles et calcul
- **API** : `claude-fable-5-1`, `claude-opus-5-5` (100 USD VÉRIFIÉ) ; `gemini-4-argon` (20 USD VÉRIFIÉ).
- **Ouvert, coût 0 USD** : `Llama-3.1-8B-Instruct` sur A100 80 Go (VÉRIFIÉ disponible) comme **quatrième famille de poids** pour les bras Red-Team de E4 : permet 30 graines sans toucher au budget API. Calcul illustratif : 60 cibles × 4 conditions × 30 graines ≈ 7 200 générations de ~1 000 tokens ; avec vLLM ou équivalent, de l'ordre de 2–4 h A100 (illustratif).
- **Gratuit illimité** : `jev-1.14.0`, Crossref, Semantic Scholar, arXiv (VÉRIFIÉ).

### Budget (tous chiffres illustratifs, à 0,02 USD l'appel Claude court et 0,002 USD l'appel Gemini)
| Expérience | Appels payants | Coût |
|---|---|---|
| Analyses gratuites préalables (longueur, cônes, DPP, régression) | 0 | 0 |
| E1 | 10 relances Argon longues + 0 Claude | ≈ 1 USD Gemini |
| E2 | 80 appels Claude + 40 Gemini | ≈ 2 USD |
| E3 | 2 bras × ~1 500 appels Red-Team Claude | ≈ 60 USD |
| E4 | majoritairement Llama local ; 2 cellules Claude ≈ 600 appels | ≈ 12 USD |
| E5 | 80 appels Fable | ≈ 2 USD |
| Réserve | — | ≈ 23 USD Claude, 17 USD Gemini |

Si les prix réels diffèrent, E3 est le premier poste à réduire (passer de 60 à 30 cibles) ; E1, E2, E5 et les analyses gratuites ne se sacrifient pas.

### Spécification exécutable minimale (statut : HYPOTHÈSE, pas $\mathcal{L}^*$)

L'ordre est dicté par ce que chaque étape peut falsifier avant de dépenser :

```
0. GRATUIT  : régresser jev ~ longueur + sections sur 247 valides ;
             variance du bassin ~ cône vs espèce ; diversité DPP vs Top-10.
             -> si jev ~ longueur (rho > 0,8) : STOP, A1 tombe, rapport.
1. E1 (1 USD) : apparier formats. -> si H_B : Annexe 1 inexploitable.
2. Construire 60 paires (x, x') à failles plantées, Crossref comme oracle.
3. E5 (2 USD) : best-of-n sur jev. -> si H_B : jev hors de toute récompense.
4. E4 (12 USD + A100) : famille vs prompt au Red-Team.
   -> routage de L* sur l'axe gagnant (poids OU consigne).
5. E3 (60 USD) : arrêt séquentiel vs T=3, avec contrôle d'arrêt aléatoire.
   Règle d'arrêt candidate : SPRT sur le taux de failles nouvelles par passe,
   H0 : taux >= p1, H1 : taux <= p0, alpha = beta = 0,05 ;
   arrêt interdit tant que l'estimateur Chao1 de failles non vues > 1
   (référence à vérifier).
6. E2 (2 USD) : seulement si le budget restant le permet ; il n'alimente
   pas L*, il décide si les vagues 2..10 valent leur coût.
```

Ce que cette spécification **refuse** du cahier des charges de l'arbitre, et pourquoi : (i) pas d'apprentissage de $k_t$ ni de division des tâches avant que E4 ait dit sur quel axe la diversité agit ; (ii) pas de `jev` dans la récompense avant E5 ; (iii) pas d'assaut sur $\mathcal{M}_1$ : aucune tâche `controle-ia` à vérité de terrain n'existe dans le socle (A12) — y lancer un essaim mesurerait l'essaim contre rien. $\mathcal{M}_2$ (littérature) est attaquable parce que Crossref/S2 fournit un oracle mécanique.

### Briques des champions retenues pour test, et briques rejetées
- **À tester** : l'arrêt séquentiel par SPRT sur un taux de découverte (Fable #01, Opus #09 — réduit au cas E3) ; la vérification par engagement puis tirage (Fable #06 *cut-and-choose*, Opus #06 *commit-reveal*) comme forme du Red-Team du tour 2, parce qu'elle est mécanique et ne dépend pas de `jev` ; les canaris plantés (Opus #06) — c'est exactement l'oracle de E3–E5.
- **Rejetées à ce stade** : toute brique exigeant de `jev` des plongements, des vraisemblances ou une implication (A9) — Fable #05, #08, #09, Opus #01, #02, #03, #04, #10 et les dix Argon ; toute brique dont le duel coûte > 120 USD (A8) — tous ; les termes anti-Goodhart dépendant de `jev` dans la récompense tant que E5 n'a pas tranché.

### Ce qui peut être réfuté ici
Cinq duels, chacun avec un bras qui tue une supposition de la question : A1–A2 (E1 et étape 0), A3 (E2), A6–A7 (E3), A4 et `H4'` (E4), A5 (E5). Aucune « loi mère » n'est affirmée ; si E3 et E4 donnent $H_B$, la bonne réponse à la question 2 est que le collisionneur fixe n'est pas le problème, le détecteur l'est.

FIN-DE-CELLULE