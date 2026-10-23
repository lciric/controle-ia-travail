# Proposition A — Tour III.3 : riposte

## 0. État des pièces

- Pièces `E3-T2-redteam-B` et `E3-T2-redteam-C` présentes, délimiteur `FIN-DE-CELLULE` présent ; sha256 déclarés, non recalculés.
- Je ne réponds qu'aux sections qui visent A : B §« Contre la proposition A » (A-F1 à A-F8, tableau d'évasion, contrôles 1–7) ; C §« Contre la proposition A » ((a) 1–5, (b) 1–4, (c) 1–3). Les attaques de C contre B et de B contre C ne sont pas traitées ici.
- Point 0 de B (gabarit Argon distinct : « anti-vernis », « pont inédit », paires $(u,v)$) : je ne l'avais pas relevé ; je le confirme à la lecture de l'Annexe 3 (OBSERVÉ-NON-AUDITÉ). La consigne reçue par chaque espèce n'est dans aucune pièce.
- Donnée manquante qui conditionne E2 : le socle ne dit pas si les clones sont **réinstanciés à chaque vague** ou s'ils portent un historique. Je le signale ; je n'invente pas la réponse.

---

## (a) Réponse à chaque attaque

### Attaques de B

**A-F1 (oracle = ligne de base sur les strates i et v). Acceptée.** Sur ces strates, `jev` ne peut pas battre l'oracle qui a produit l'étiquette ; le critère « AUC `jev` − AUC(base) < 0,10 » y était satisfait d'office. Correction : les strates mécaniques (i, ii, v) deviennent un **plancher de fonctionnement** (un détecteur qui les manque est mort), jamais un verdict ; le verdict se joue sur les strates non mécaniques (iii, iv, et trois nouvelles : vi confondant inséré, vii volume d'appels incompatible avec le prix affiché, viii construit non défini). Voir banc v2.

**A-F2 (jumeaux « honnêtes » non honnêtes). Acceptée**, également soulevée par C (a)1 et (c)1. Correction double : (1) les textes de base ne sont plus étiquetés « honnêtes » mais « base » ; la métrique n'est plus un taux de fausses alertes global mais la **détection différentielle** : l'attaquant nomme-t-il la faille plantée sur $x'$ et ne la nomme-t-il pas sur $x$ ? (2) les failles endogènes documentées par B et C au tour 2 (budgets 240–480 USD par duel, quorum byzantin à $f=0$, etc.) forment une **strate supplémentaire à étiquette indépendante**, produite par d'autres juges que mon script d'injection (statut des étiquettes : HYPOTHÈSE de B et C, mais non générée par mon oracle). Le détecteur qui trouve une faille endogène sur $x$ marque un point, il n'est plus puni.

**A-F3 (effet plafond, E3 penché vers $H_B$). Acceptée.** E3 est désormais mesuré **uniquement** sur les strates dures (iii, iv, vi, vii, viii, endogènes, adverses) ; les strates mécaniques servent au plancher.

**A-F4 (E4 : famille confondue avec compétence ; pas d'échelle commune entre « effet famille » et « effet prompt »). Acceptée sur les deux points.** La course « famille vs prompt » n'était pas identifiée : on règle l'amplitude de chaque facteur à volonté. E4 est reformulé en une question identifiée : **existe-t-il une corrélation résiduelle des ratés attribuable aux poids partagés, une fois le prompt fixé et la difficulté des items contrôlée ?** Le facteur compétence est séparé par le bras `Llama-3.1-70B` vs `8B` (même famille, compétence différente), matériel VÉRIFIÉ disponible ; le facteur « lignée » par Fable vs Opus (même éditeur). L'effet prompt devient une mesure séparée, non un adversaire.

**A-F5 (Simpson à l'étape 0 ; sous-scores nuls par construction sur section absente ; gabarit non contrôlé en E1 ; contrôle `BASSIN_MATH` impossible). Acceptée.** Étape 0 : régression **intra-espèce** (Claude seul, 176 valides par l'Annexe 1, OBSERVÉ-NON-AUDITÉ), sur le sous-score `Rigueur` et non sur le composite, et STOP uniquement si la corrélation intra-espèce avec la longueur dépasse le seuil. E1 : impossible d'apparier le gabarit sans la consigne Argon → E1 est remplacé par une **réplication à consigne unique et commune** (voir E1'). Le contrôle `BASSIN_MATH` est supprimé ; remplacé par « retrait de la section 3 » vs « retrait d'un segment de même longueur dans la section 1 ».

**A-F6 (violations de B4).**
- E1 : acceptée. Reformulé : $H_A$ (l'écart persiste à consigne et `max_tokens` identiques) falsifie l'explication « artefact de consigne/format » ; $H_B$ (l'écart s'effondre) falsifie A1–A2 et toute lecture inter-espèces de l'Annexe 1.
- E5 : acceptée. Une seule statistique : $\Delta_{\text{sel}}$ = (taux de DOI résolus **et** pertinents, du tirage sélectionné par `jev`) − (même taux, tirage sélectionné par un score aléatoire, contrôle 7 de B). $H_A$ : $\Delta_{\text{sel}}>0$ ; $H_B$ : $\Delta_{\text{sel}}\le0$.
- E2 : partiellement acceptée. Si les clones sont réinstanciés à chaque vague, « historique » n'existe que dans la consigne et E2 se réduit à une réplication ; si les clones sont persistants, la question « texte de consigne vs état du clone » a un sens. E2 est donc conditionné à l'information manquante (point 0) et $H_B$ est scindée : $H_{B1}$ « aucun effet réplicable », $H_{B2}$ « effet porté par l'état du clone ».

**A-F7 (puissance ; Chao1 instable sur 3 failles). Acceptée.** E2' passe à 40 clones par cellule (illustratif : erreur standard de la différence ≈ 0,22 pour un écart-type intra-cellule de 1). Chao1 est **retiré** de la règle d'arrêt, pour la raison de B et pour celle de C (a)3 : il vaut zéro quand les attaquants sont aveugles. Aucun estimateur des failles non vues n'est disponible quand les attaquants sont corrélés ; je l'écris comme une limite, pas comme un remplaçable.

**A-F8 (refus de $\mathcal{M}_1$ trop fort). Acceptée avec périmètre.** La survie d'une contrainte formelle à travers $k$ délégations sur Llama local est vérifiable par analyseur, à coût API nul. J'ajoute E6 ; je le prends à B et C en le disant. Mais E6 teste `H9` seule, pas « un assaut sur $\mathcal{M}_1$ » : le socle n'a toujours pas de tâche `controle-ia` à vérité de terrain pour un essaim (A12 reste).

### Attaques de C

**(a)1 (tautologie du banc ; failles endogènes comptées comme fausses alertes). Acceptée** — traitée sous A-F1/A-F2.

**(a)2 (Llama-8B confond famille et capacité). Acceptée** — traitée sous A-F4 ; bras 70B ajouté.

**(a)3 (Chao1 : divergence, zéro quand aveugle). Acceptée** — Chao1 retiré.

**(a)4 (E1 : gabarit confondu même sans troncature). Acceptée** — E1'.

**(a)5 (amputation de $\mathcal{M}_1$). Acceptée avec périmètre** — E6.

**(b)1 (texte de longueur standard à jargon dense trompe la régression de l'étape 0). Rejetée en tant qu'attaque, acceptée en tant que contrôle.** L'étape 0 n'est pas un filtre contre un adversaire ; c'est un diagnostic de ce que `jev` corrèle. Un texte de longueur médiane saturé de mots-clés ne « trompe » pas une régression : il ne la concerne pas. En revanche, le scénario décrit (vernis à format constant) est exactement ce que E5' doit détecter ; j'ajoute un contrôle « placebo à mots-clés » (texte de même longueur et sections, contenu tautologique).

**(b)2 (détournement de DOI réels). Acceptée.** L'oracle d'existence est aveugle à la pertinence. Correction : l'oracle devient « DOI résolu **et** affirmation soutenue par le résumé Semantic Scholar », le second volet jugé par une famille disjointe de l'auteur (statut de cet instrument : HYPOTHÈSE, c'est un juge LLM), et contrôlé par C (c)3 : permutation des DOI entre phrases ; si le score ne bouge pas, l'oracle ne mesure que la présence.

**(b)3 (leurres sacrificiels + enfouissement contre SPRT/Chao1). Acceptée.** Chao1 retiré ; la stratégie « leurres puis arrêt » devient une **strate adverse** du banc (voir ix) : la règle d'arrêt est jugée sur sa capacité à ne pas s'arrêter après les leurres.

**(b)4 (évasion simultanée). Acceptée** — strate ix.

**(c)1–(c)3. Acceptés**, intégrés : assainissement et strate endogène ; bras 70B ; permutation des DOI.

### Tableau d'évasion de B et contrôles 1–7

Le diagnostic commun de B et C est juste : mes instruments vérifiaient des propriétés de surface que la vérité plantée sait elle-même produire. Je ne prétends pas disposer d'un instrument qui vérifie une propriété que l'adversaire ne sait pas produire ; la seule candidate dans le socle est la **réexécution** (code, calcul, résolution bibliographique avec pertinence), et elle ne couvre qu'une fraction des propositions. Réponse par instrument :

| Évasion (B) | Réponse |
|---|---|
| DOI réels non pertinents | Oracle « existence + pertinence » ; contrôle permutation (C c3). |
| Squelette de sections creux | Strate ix (texte adverse) ; E5' avec placebo à mots-clés. |
| Allongement / sections contre `jev` | Contrôle best-of-n sur longueur maintenu, plus placebo. |
| Défauts hors des cinq types plantés | Strates vi–viii + endogènes + adverses ; le rappel n'est plus mesuré sur les seuls types scriptables. |
| Réécriture sous le seuil de nouveauté avant l'arrêt | Strate ix-b : faille introduite **dans la réécriture** ; E3' la compte. |
| Paraphrase contre la distance de compression | La distance de compression est retirée de toute décision ; elle reste un descripteur gratuit, pas un instrument. |

Contrôles de B : 1 (strate non mécanique) — intégré ; 2 (jumeau édité sans faille) — intégré, version $x^{e}$ ; 3 (famille d'injection disjointe) — intégré : injection par `Llama-3.1-70B` local ou Argon, détection par Claude, et réciproquement ; 4 (70B vs 8B) — intégré ; 5 (corrélations intra-espèce) — intégré ; 6 (Claude dans le gabarit Argon) — impossible sans la consigne Argon ; remplacé par E1' à consigne commune ; 7 (best-of-n sur score aléatoire) — intégré.

Contrôle de C (c)1 bis, pris à l'attaque de C contre B parce qu'il s'applique à mon E4 tel quel : **stratification par difficulté d'item**. Un mélange de Bernoulli à $p_i$ variable produit une corrélation positive des ratés entre agents indépendants. Toute corrélation dans E4' est calculée **à l'intérieur de strates de difficulté** (quantiles du taux de détection moyen de l'item), avec permutation des étiquettes entre agents intra-strate comme nul.

---

## (b) Expériences corrigées

### Banc B-PLANT v2 (préalable à E3', E4', E5')

Statut : HYPOTHÈSE pour toutes les étiquettes non mécaniques.

1. **Textes de base** : 20 champions Claude, après passage des scripts mécaniques (somme budgétaire, volume d'appels × prix affiché, résolution des DOI) ; les violations trouvées sont **conservées et étiquetées** comme strate E (endogène, étiquettes B/C du tour 2), non corrigées : corriger les rendrait « honnêtes » au sens où B le refuse à juste titre.
2. **Versions par texte** : $x$ (base) ; $x^{e}$ (édité par le même modèle, même longueur de diff, sans faille — contrôle 2 de B) ; $x'_{s}$ pour chaque strate $s$.
3. **Strates** : (i) DOI non résolvable ; (ii) chiffre incohérent ; (v) section Duel supprimée — *mécaniques, plancher* ; (iii) hypothèse écrite comme résultat ; (iv) contrôle négatif vide ; (vi) confondant inséré dans le plan ; (vii) prix affiché ≤ 120 USD mais volume d'appels incompatible (le « caméléon arithmétique » de C) ; (viii) métrique principale sans définition opérationnelle ; (E) endogène ; (ix-a) texte adverse « toutes évasions » : DOI réels hors sujet + squelette complet + défaut hors types + conditionnel ; (ix-b) leurres sacrificiels + faille enfouie dans la loi.
4. **Aveuglement** : injection des strates (iii)–(ix) par `Llama-3.1-70B` local pour les cibles attaquées par Claude, par Fable pour les cibles attaquées par Llama ; jamais même famille pour planter et détecter.
5. **Oracle bibliographique** : existence (Crossref/S2) **et** pertinence (résumé S2 vs affirmation, jugé par une famille disjointe de l'auteur) ; contrôle par permutation des DOI.

Taille (illustratif) : 20 textes × (1 + 1 + 10 versions) = 240 textes, ~40 cibles par strate dure.

### E0 — Gratuit, avant tout appel payant

- Régressions **intra-espèce** : `Rigueur` ~ longueur, sur les 176 Claude valides ; composite ~ longueur sur les 71 Argon valides.
- Variance du bassin (nom + formule) expliquée par le cône vs par l'espèce (classification croisée).
- Diversité DPP vs Top-10 (descripteur, pas décision).
- Demande à l'arbitre : consignes de chaque espèce ; persistance ou non des clones entre vagues ; composition des 53 non valides.
- STOP (illustratif) : si $\rho_{\text{intra-Claude}}(\text{Rigueur}, \text{longueur}) > 0{,}8$, A1 tombe.

### E1' — Écart d'espèce à consigne commune

- $H_A$ : à consigne unique (rédigée pour ce test, gabarit imposé, `max_tokens` identique), l'écart composite Claude/Argon persiste à ≥ 50 % de sa valeur Annexe 1 (illustratif) → falsifie « artefact de consigne/format ».
- $H_B$ : l'écart tombe sous 20 % → falsifie A1–A2 et toute comparaison inter-espèces de l'Annexe 1.
- Protocole : 20 Fable + 20 Opus + 20 Argon, même consigne, scorés par `jev` ; contrôle : mêmes 60 textes amputés de la section 3 vs amputés d'un segment de même longueur en section 1 (si `jev` chute pareil, il compte des caractères).
- Coût illustratif : ≈ 1 USD Claude, 0,1 USD Gemini.

### E2' — Déflation : conditionnée au point 0

- Si clones réinstanciés : réplication V01 vs V10, 40 clones Fable par consigne, mêmes conditions. $H_A$ : différence ≥ 0,5 (illustratif), même signe qu'Annexe 1 ; $H_{B1}$ : différence non distinguable de zéro → A3 tombe pour Fable aussi.
- Si clones persistants : ajout d'un bras « clone frais + consigne V10 » vs « clone de V09 + consigne V10 ». $H_{B2}$ : le clone frais ne reproduit pas l'effet.
- Placebo : consigne V01 reformulée sans contenu de déflation.
- Coût illustratif : ≈ 3 USD.

### E5' — `jev` sous pression de sélection (décide si `jev` entre dans une récompense)

- Pour 10 consignes bibliographiques, 8 tirages Fable ; trois sélections : meilleur `jev`, meilleur score aléatoire, plus long.
- Statistique unique : $\Delta_{\text{sel}}$ = taux de citations résolues **et pertinentes** (sélection `jev`) − (sélection aléatoire).
- $H_A$ : $\Delta_{\text{sel}} > 0$ ; $H_B$ : $\Delta_{\text{sel}} \le 0$ → `jev` hors de toute récompense dans $\mathcal{L}^*$, admis seulement en topologie, et A5 falsifiée pour tout champion qui met `jev` dans $R$.
- Contrôles : sélection sur longueur (si elle reproduit $\Delta$`jev`, verbosité) ; placebo à mots-clés inséré dans les 8 tirages (si sélectionné par `jev`, saturation lexicale, C b1) ; permutation des DOI (si le taux de pertinence ne bouge pas, l'oracle est aveugle, C c3).
- Coût illustratif : ≈ 2 USD.

### E4' — Corrélation résiduelle des ratés : poids ou prompt (remplace E4)

- Cibles : strates dures de B-PLANT v2.
- Cellules : {Fable, Opus, Argon, Llama-8B, Llama-70B} × {prompt P1, prompt P2 (resémancé)} × 3 graines. Prompts identiques entre familles.
- Mesure : corrélation des ratés $\phi$ entre paires d'attaquants, **calculée intra-strate de difficulté** (quantiles du taux moyen de détection par item), nul par permutation intra-strate des étiquettes entre agents.
- $H_A$ (`H4'` au niveau des poids) : à prompt fixe, $\phi_{\text{même famille}} - \phi_{\text{familles distinctes}} > 0$ hors nul, pour au moins deux paires de familles de compétence comparable (Fable/Opus ; 70B/Claude).
- $H_B$ : la différence est dans le nul ; la corrélation résiduelle est entièrement expliquée par la difficulté et le prompt → la règle « chimère forcée quand $\rho$ élevé » (Fable #06, Opus #06, #09) n'a pas d'objet ; $\mathcal{L}^*$ route sur la consigne.
- Lectures secondaires, non concurrentes : effet de P1→P2 à famille fixe (descriptif) ; 8B vs 70B donne la part « compétence » de la corrélation inter-famille (si $\phi_{8B,70B}$ est bas alors que les poids sont de même lignée, la famille n'est pas le bon découpage).
- Issues : $H_A$ soutient `H4'` et la prémisse A4 ; $H_B$ la falsifie et, avec les bassins identiques à $(V,k)$ fixé (OBSERVÉ-NON-AUDITÉ), désigne le prompt de cône comme la source de corrélation.
- Coût illustratif : Llama local, ~2–4 h A100 ; ≈ 10 USD Claude, ≈ 1 USD Gemini.

### E3' — Arrêt séquentiel contre $T$ fixe, sur strates dures seulement

- Bras A : arrêt quand le **gain marginal de failles nouvelles par dollar** sur la dernière passe tombe sous $\tau$ (SPRT sur le taux de nouveauté, $\alpha=\beta=0{,}05$), sans Chao1 ; bras B : $T=3$ fixe ; bras B' : $T=3$ + une attaque terminale sans réécriture (le bras que B réclame contre C, qui vaut aussi contre moi) ; bras C : arrêt aléatoire à espérance de tours égale à A ; budget égal par bras et **budget égal par tour** (le contrôle que C exige contre B et qui s'applique ici).
- Métrique primaire : rappel des failles des strates (iii)–(ix) + E à l'arrêt, par dollar ; secondaire : rappel sur ix-b (le bras qui s'arrête après les leurres perd).
- $H_A$ : rappel$_A$ − max(rappel$_B$, rappel$_{B'}$) ≥ 0,15 à coût ≤, et A > C (illustratif).
- $H_B$ : A ≈ C ou A ≤ B' → la règle est inerte ; ce qui manque n'est pas un tour mais un détecteur d'un autre type ; A6–A7 falsifiées.
- Coût illustratif : ≈ 50 USD Claude (poste à réduire en premier si les prix réels dépassent l'estimation).

### E6 — Survie d'une contrainte à travers $k$ délégations (`H9`, Llama local, 0 USD API)

- Chaîne de $k \in \{1,2,4,8\}$ délégations sur `Llama-3.1-8B` puis `70B` ; contrainte formelle vérifiable par analyseur (champ obligatoire, interdiction lexicale, borne de longueur) ; 50 chaînes par $k$ (illustratif).
- $H_A$ : taux de survie décroît strictement en $k$ (régression logistique, pente < 0 hors nul par permutation de $k$) ; $H_B$ : pente nulle.
- Contrôles : (1) réinjection de la consigne racine à chaque maillon vs placebo de même longueur (le contrôle 5 que B exige contre C) ; (2) sous-tâches légitimement spécialisées, pour mesurer le taux de fausses « dérives » quand la substance est respectée mais la surface change.
- Périmètre : ceci teste `H9` sur Llama ; ce n'est pas un banc $\mathcal{M}_1$ pour un essaim.

### Budget corrigé (illustratif, 0,02 USD/appel Claude court, 0,002 USD/appel Gemini)

| Poste | Coût |
|---|---|
| E0, E6, banc (injection par Llama-70B) | 0 USD API, GPU local |
| E1' | ≈ 1,1 USD |
| E2' | ≈ 3 USD |
| E5' (+ juge de pertinence, famille disjointe) | ≈ 4 USD |
| E4' | ≈ 11 USD |
| E3' | ≈ 50 USD |
| Réserve | ≈ 31 USD Claude, ≈ 18 USD Gemini |

Ordre : E0 → banc → E1' → E5' → E4' → E6 (en parallèle, GPU) → E3' → E2' si budget.

---

## (c) Réponse à l'arbitre

**Ce qui est établi.** (VÉRIFIÉ, socle) : le budget total est 100 + 20 USD ; aucune tête de sabotage ni sonde temps réel n'existe ; `jev-1.14.0` est un classifieur non génératif gratuit ; Llama-3.1-8B/70B et les GPU sont disponibles ; `P3` a rendu un verdict nul sur les sondes linéaires. (VÉRIFIÉ par construction du protocole) : la riposte du tour 3 n'est attaquée par personne. (OBSERVÉ-NON-AUDITÉ, lecture des pièces) : neuf champions Argon sur dix sont coupés avant leur section 3, contrairement à l'énoncé de l'arbitre ; les Argon suivent un autre gabarit que les Claude ; la somme des valides est 247, pas 300 ; à $(V,k)$ fixés, Fable, Opus et Argon tombent dans le même bassin mathématique ; aucun champion Claude n'est exécutable à 120 USD au total, et plusieurs portent des contradictions internes relevées par B et C.

**Ce qui n'est pas établi.** Que `jev` mesure la qualité d'une loi plutôt que la présence de sections et la longueur (A1) ; que l'écart Claude/Argon soit conceptuel plutôt qu'un artefact de consigne, de gabarit et de troncature (A2) ; que les vagues de déflation aient un effet distinct d'une réplication bruitée (A3) ; que la corrélation d'erreurs `H4'` soit portée par les poids plutôt que par le prompt de cône (A4) ; qu'un seul des trente termes « anti-Goodhart » tienne sous sélection (A5) ; qu'un collisionneur à $T$ adaptatif fasse mieux qu'un $T$ fixe suivi d'une attaque terminale (A6–A7) ; que `H9` ait une métrique de dérive qui ne soit pas une mesure de similarité lexicale. Après le tour 2, je retire deux instruments que je proposais : l'estimateur Chao1 (nul quand les attaquants sont aveugles ; contournable par leurres) et la distance de compression comme critère de décision. Je reconnais aussi que mon banc mesurait des propriétés de surface que l'adversaire sait produire ; le banc v2 ajoute des strates non scriptables, endogènes et adverses, une injection en aveugle croisé, un oracle de pertinence et une stratification par difficulté, mais aucun de ces ajouts n'est une propriété que l'adversaire ne saurait pas produire : c'est une limite du socle, pas un détail de protocole.

Sur la « Loi Mère » : aucune n'est affirmée. Fusionner trente hypothèses non testées, dont la majorité attribue à `jev` des sorties absentes du socle (plongements, vraisemblances, implication) et dont aucune n'est exécutable au budget, produit une hypothèse de rang supérieur. Les seules briques que je retiens pour test sont mécaniques : l'engagement puis tirage (Fable #06, Opus #06), les canaris plantés (Opus #06), un arrêt séquentiel sur un taux de nouveauté (Fable #01, Opus #09) réduit à E3' et confronté au bras « $T=3$ + attaque terminale » qui est son vrai concurrent.

**L'expérience à faire en premier.** E0, gratuite, parce qu'elle peut faire tomber A1 et A4 sans un centime, et parce qu'elle oblige l'arbitre à fournir trois données manquantes (consignes par espèce, persistance des clones, sort des 53 non valides) sans lesquelles l'Annexe 1 n'est pas interprétable. Première expérience payante : **E4'**, parce que toute la question 2 — routage inter-espèces, appariement monoculture/chimère, gouvernance de $\mathcal{M}_2$ — repose sur l'existence d'une corrélation d'erreurs au niveau des poids ; si E4' donne $H_B$, l'axe de diversité à acheter est la consigne, pas la famille, et la moitié des trente champions perd son levier. E5' précède E4' parce qu'elle coûte 2 USD et décide si `jev` peut figurer dans une récompense ; E3' vient après parce qu'il est le poste le plus cher et que son résultat ne change rien si E4' et E5' ont déjà déplacé la question du collisionneur vers le détecteur.

FIN-DE-CELLULE