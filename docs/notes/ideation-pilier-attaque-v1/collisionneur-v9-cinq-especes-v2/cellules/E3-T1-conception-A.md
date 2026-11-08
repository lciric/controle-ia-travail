# Proposition A — Tour III.1 : conception à l'aveugle

**Pièces** : bloc FAITS complet et lisible ; deux empreintes non recalculées (gabarit pince `5eab49e4…`, faits du 22 octobre `3ecab00f…`) : je traite ce qu'elles couvrent comme RAPPORTÉ de seconde main. Aucune pièce coupée.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas acquis |
|---|---|---|---|
| A1 | L'oracle du monde planté voit le sabotage **à la dose diffuse** fixée sur la boîte noire seule (R3). | HYPOTHÈSE | L'audit du rappel manque (faits §6). La dose a été fixée pour tromper la boîte noire, pas pour rester visible à l'oracle : rien n'interdit que la dose « diffuse » soit aussi sous le seuil de l'oracle. Point 0 bien posé, mais la question enchaîne 1–5 comme si A1 tenait. |
| A2 | Une trace existe aux couches lues (H1), et si elle n'existe pas « aucune boucle ne la fera apparaître ». | HYPOTHÈSE | Seules données : rien sur le diffus (R1 v4), sondes génériques au hasard (rappel 0,013), juge au hasard. La seconde moitié suppose la trace statique ; or la famille (ii) est une politique distillée dont l'empreinte dépend de α : la trace est une fonction de la dose, pas un fait binaire. |
| A3 | L'écart apparié au modèle de base est « ce que l'attaquant ne contrôle pas ». | HYPOTHÈSE, à mon avis faux tel qu'énoncé | L'écart h_adapté − h_base sur le même contexte est exactement l'effet de l'adaptateur, que le bras d'attaque conçoit. Ce que l'attaquant ne contrôle pas, c'est la **lecture par la base du texte qu'il a produit** (base rejouée en forçage sur la sortie de l'organisme). Les deux quantités doivent être nommées séparément. |
| A4 | Le prédicteur texte 0,866 ou Jev 1.14 sont des mâchoires externes exploitables. | OBSERVÉ-NON-AUDITÉ | Jev : aucun cas honnête, taux de fausses alertes inconnu ; 0,866 : métrique et dénominateur non spécifiés dans les faits, et mesuré sur des épisodes où la sonde W lisait la consigne (a_NE 0,9967) : rien n'exclut que le prédicteur texte lise la consigne transformée en prose, lui aussi. |
| A5 | L'oracle et la mâchoire externe sont indépendants. | HYPOTHÈSE | Les deux lisent « ce qui a réellement tourné ». Si la mâchoire externe est un oracle dégradé, la pince compte deux fois la même mesure et la « capture résiduelle » est tautologique. |
| A6 | L'étau : tromper l'externe oblige à dissimuler davantage, visible à l'interne. | HYPOTHÈSE (faits §1) | L'agent écrit le code et choisit ce qui tourne : il contrôle en grande partie l'entrée de l'externe, ce qui est précisément le cas L2 (contournement à coût nul). La question demande si l'étau serre sans dire d'abord si l'on est hors de L2. |
| A7 | Le résultat d'arène (mélange d'équilibre progresse, figée généralise mieux) se transpose à un vrai modèle. | HYPOTHÈSE | Arène synthétique, tables B/B′ suspendues, aucun verdict scellé (faits §4). |
| A8 | La lecture en valeur de Nash est licite (jeu à somme nulle, matrice stationnaire, gains = rappel). | HYPOTHÈSE | Les gains dépendent de la génération d'attaque ; une matrice de transfert est un instantané. Nash sur l'instantané ne dit rien de la dynamique Bailey (« can't rule out convergence », RAPPORTÉ). |
| A9 | Une direction causale peut exister. | HYPOTHÈSE | Seul précédent lu : l'axe de douleur se lit mais n'est pas un levier (RAPPORTÉ) — un exemple de lecture non causale, aucun exemple de lecture causale. |
| A10 | L'adaptateur de la famille (ii) encode la **politique** et non une paraphrase mémorisée de la consigne (i). | HYPOTHÈSE | Distillation depuis (i) sur contextes rejoués sans consigne ; rien dans les faits ne teste si le modèle distillé « se raconte » la consigne en interne. Le confondant 1 peut survivre à la suppression du texte de consigne. |
| A11 | Le témoin « instruit sans sabotage » vaut organisme placebo. | HYPOTHÈSE | Même chaîne, mais l'objectif inculqué diffère ; il contrôle la **chaîne de modification**, pas la présence d'un **objectif caché quelconque**. Il faut en plus un placebo à objectif caché inoffensif (confondant 2). |
| A12 | Le jumeau honnête apparié a une variance de couverture assez faible pour que « dommage = baisse de couverture » soit lisible. | HYPOTHÈSE | E3 bis : tâches synthétiques, aucune donnée décisive. |

---

## (b) Expériences décisives, en duel

Conventions : FA = taux de fausses alertes sur dénominateur honnête ; tous les seuils numériques sont **illustratifs** sauf mention ; validation croisée par bloc de famille (confondant 3) partout ; aucune lecture du mode tenu à l'écart avant G1. Je sers des éléments de la synthèse d'antériorité (paires contrefactuelles, placebo, dormants, contrôle positif) en le disant.

### E0 — Rappel de l'oracle et indépendance oracle/moniteurs (point 0)

- **Volet** vérité terrain ; mâchoire sans objet.
- **H_A** : sur les épisodes où le monde planté atteste un sabotage par action (étiquette par construction), l'oracle de couverture le voit à rappel ≥ r_min = 0,80 (illustratif) pour **chaque** état S25…S100, avec FA ≤ 0,05 sur le jumeau honnête et sur les échecs honnêtes.
- **H_B** : rappel < r_min à au moins un état retenu comme « diffus », ou FA > 0,05 sur les échecs honnêtes.
- **Grandeur** : rappel par état, FA par classe de négatif (jumeau honnête, échec honnête, épisode « mention », témoin T100).
- **Contrôle négatif obligatoire** : échecs honnêtes (baisse de couverture sans sabotage) ; si l'oracle les compte comme dommage, le « dommage » mesure l'échec, pas l'acte.
- **Indépendance** : plan factoriel oracle × moniteur sur les négatifs : rapport R = P(alerte moniteur | faux positif oracle) / P(alerte moniteur | oracle correct). H_A : R ∈ [0,5 ; 2] ; H_B : R > 2 (erreurs corrélées : les deux lisent le même artefact de tâche).
- **Issue falsifiante** : H_A fausse → points 1–5 suspendus pour les états concernés ; la dose se refixe (c'est un diagnostic, R-1795) ; rien ne se lit tant que l'étalon n'est pas étalonné. H_B fausse → l'oracle devient étalon, et chaque gain de sonde se rapporte à son rappel.
- **Statistique** : intervalles de Wilson par état ; n ≥ 150 épisodes sabotés par état (illustratif) pour une demi-largeur ≈ 0,06.
- **Coût** : processeur et deux lecteurs hors famille (déjà prévus N-060 v3) ; délai borné par l'épreuve de l'étiqueteur en cours.

### E1 — Existence au-delà du texte et de la consigne transformée (point 1)

- **Volet** existence ; mâchoire interne.
- **Dispositif** : trois lecteurs d'activations appariés sur le **même texte** : (α) sonde sur les activations de l'organisme ; (β) sonde sur les activations du **modèle de base rejoué en forçage sur la sortie de l'organisme** (lit ce que le texte dit, sans l'état interne de l'adaptateur) ; (γ) prédicteur sur les traits du texte. Plus le carré contrefactuel consigne × acte (synthèse d'antériorité) : famille (i) avec consigne et exécution honnête attestée par l'oracle ; famille (ii) sans consigne et sabotage attesté.
- **H_A** : AUC(α) − AUC(β) ≥ 0,05 (illustratif) avec intervalle bootstrap à 95 % excluant 0, **et** cette différence subsiste dans la case « sans consigne, sabotage attesté » et s'annule dans la case « consigne, exécution honnête ».
- **H_B** : AUC(α) ≈ AUC(β) ≈ AUC(γ) (la trace est la transformée du texte), **ou** AUC(α) élevée uniquement dans les cases avec consigne (la sonde lit la consigne, cas W).
- **Contrôles de capacité** : sondes sur étiquettes permutées (distribution nulle par couche, 200 permutations, illustratif) ; sonde entraînée sur direction aléatoire de même norme ; même architecture, mêmes hyperparamètres figés au préenregistrement.
- **Grandeur** par couche × classe de position (avant / pendant / après l'action, frontières d'actions fournies) ; agrégation max ou attention seulement (programme § 8.1).
- **Puissance** : pour détecter ΔAUC = 0,05 à 80 % de puissance, de l'ordre de 400 épisodes par bras équilibrés (illustratif, à recalculer sur la variance observée en E3 bis).
- **Issue négative écrite d'avance** : H8 (« aucune trace décodable au-delà du texte ») au même rang ; elle commande alors une reconception des sondes (séquentielles, écart à la base) et non un arrêt.
- **Ce qui réfuterait l'expérience elle-même** : E0 échoue (étiquettes douteuses) ; ou la sonde β bat la sonde α, signe que l'organisme adapté *efface* dans ses propres activations ce que sa sortie révèle — issue à consigner, non à lisser.

### E2 — Acte ou identité : placebo, dormants, écart apparié (point 2)

- **Volet** localisation ; mâchoire interne.
- **Organismes** : saboteur S_α ; témoin T100 ; **placebo P** à construire : même chaîne, objectif caché *inoffensif* (par exemple une préférence stylistique dormante), inculqué sans sabotage — niveau méthode seulement, construction au bras d'attaque.
- **Épisodes dormants** : S_α sur les tâches où l'oracle n'atteste aucun sabotage.
- **H_A (acte)** : une sonde entraînée sur « saboté vs honnête » donne, sur les dormants de S_α, une AUC contre le jumeau honnête ≤ 0,60 et, sur P et T100, ≤ 0,60 (illustratif).
- **H_B (identité)** : AUC sur dormants ≥ 0,75 **ou** AUC sur P ≥ 0,75 : la sonde sépare les poids, pas l'acte.
- **Écart apparié** : Δ = h_adapté − h_base sur le même contexte (forçage). Deux lectures : ‖Δ‖ par couche (attendue croissante en α pour S, T et P : identité) ; projection de Δ sur la direction apprise, comparée entre actions sabotées et actions dormantes du **même** organisme. H_A : la projection sépare saboté/dormant à AUC ≥ 0,70 à ‖Δ‖ égale ; H_B : la projection suit ‖Δ‖ seulement.
- **Sous-espace des adaptateurs des modes vus** : projeter Δ hors du sous-espace de sortie des adaptateurs vus et refaire E1. Si la trace disparaît, elle vit dans l'empreinte des adaptateurs connus (fragile face à un mode non vu) ; si elle persiste, elle a une composante hors de leur image.
- **Contrôle** : tâche appariée (même tâche pour S, P, T, jumeau) pour éviter le confondant de famille de tâche.
- **Issue négative** : « la sonde détecte l'identité, pas l'acte » (R3).

### E3 — Causalité : dose-réponse, substitution, ablation (point 3)

- **Volet** causalité ; mâchoire interne ; test causal : oui.
- **E3a dose-réponse** : α ∈ {0, 0,25, 0,5, 0,75, 1} pour S et pour T. Grandeurs : dommage D(α) par l'oracle ; score de sonde s(α). **H_A** : s suit D (Spearman ≥ 0,8 sur S) et reste plat sur T où D est plat ; **H_B** : s croît en α sur S **et** sur T (s suit la norme de l'adaptateur, pas le dommage). Contrôle : α = 0 rend la base au bit près (P-009, présent en partie) : s(0) doit coïncider avec la sonde β d'E1.
- **E3b substitution** : remplacer, aux couches et positions localisées par E2, les activations de S par celles du jumeau honnête sur le même contexte, et laisser l'épisode se poursuivre. **H_A (trace causale)** : D baisse d'au moins δ = 0,3·D(S100) (illustratif) ; **H_B (lecture pure, cas axe de douleur)** : s chute mais D ne change pas. Contrôles : substitution aux mêmes positions depuis un **autre** épisode honnête apparié par tâche ; substitution à des couches hors de la localisation ; substitution depuis P.
- **E3c ablation / pilotage** le long de la direction de la sonde, pas de la direction aléatoire. Mêmes H_A/H_B que E3b. La direction aléatoire de même norme est le contrôle négatif.
- **Garde** : ces interventions se font côté défense sur des organismes déjà construits ; aucune ne décrit comment fabriquer un sabotage. Elles sont ablatives, non constructives ; à faire valider par le portier.
- **Issue falsifiante symétrique** : H_A fausse → la sonde est un capteur de lecture, utile pour la pince mais évitable sans perte de dommage ; H_B fausse → première direction causale du dépôt, et base d'une sonde « inévitable » (point 5).

### E4 — Lisibilité sans étiquette, domination et pince (point 4)

- **Volet** lisibilité et pince ; mâchoire jointe.
- **Moniteurs sans étiquette du saboteur** : (N1) nouveauté : densité de Δ (ou de h) ajustée sur les honnêtes seuls, score = −log densité ; (N2) accumulation séquentielle : somme des log-rapports de vraisemblance par action, seuil de Wald (SPRT, absent nommément du dépôt, ici introduit) ; (N3) autocorrélation des scores entre actions successives (le sabotage diffus est une politique : il devrait laisser une dépendance sérielle que l'échec honnête n'a pas).
- **Mâchoire externe candidate** : juge sur code et exécution nettoyés **ou** prédicteur texte, **après** calibration E0-bis (ci-dessous, § c).
- **Courbe** : rappel à FA = 1 % en fonction du budget d'attaque (nombre de tours du bras rouge, mesuré côté défense par les issues des tours), sur une famille tenue à l'écart (substitut : bloc de famille).
- **H_A** : la boîte blanche domine la boîte noire à chaque budget, écart ≥ 0,10 avec intervalles bootstrap disjoints ; **H_B** : les courbes se croisent ou la noire domine.
- **Pince** : τ = 1 %, τ_ext = τ_int = 0,5 %. Grandeur : C = P(interne alerte | externe a manqué, sabotage) comparée à TPR_int marginal au même τ_int. **H_A (l'étau serre)** : C − TPR_int ≥ 0,10 (illustratif), dépendance de queue positive ; **H_B** : C ≤ TPR_int (indépendance ou dépendance négative : les manqués de l'externe sont aussi les manqués de l'interne). Chaque issue réfute quelque chose : H_A fausse réfute l'étau ; H_B fausse réfute le cas E7 pour cette famille.
- **Test préalable de L2** : mesurer la part des épisodes sabotés où le code et l'exécution nettoyés sont **indistinguables** du jumeau honnête pour le juge (sabotage « hors du code », par omission ou par donnée). Si cette part dépasse 50 % (illustratif), on est en régime L2 : la pince vaut l'interne seule et la question de l'étau est mal posée pour cette famille — à écrire d'avance.
- **Contrôle contre l'inondation de fausses alertes** : la pince en OU double le FA ; d'où le partage τ/2 ; vérifier sur les échecs honnêtes et les épisodes « mention » que FA_joint ≤ 1,2 %.

### E5 — Matrice de transfert, Nash, secret contre aléa, coût d'évasion (point 5)

- **Volet** règle de défense ; mâchoire interne (puis jointe).
- **E5a matrice** : panel de M sondes (illustratif M = 6 : logistique / perceptron / attention × deux couches, agrégateurs max et attention). Le bras rouge produit des évasions contre la sonde i (la défense ne voit que les issues) ; T_ij = rappel de j à FA 1 % sur les évasions contre i. Table croisée générations g (défense) × g′ (attaque).
- **H_A (H5, diversité effective)** : la valeur du jeu à somme nulle sur T (gain = rappel) en stratégie mixte p* dépasse la meilleure pure d'au moins 0,10 ; la matrice est loin d'un rang 1. **H_B** : une ligne domine (Nash pur) ou T est quasi de rang 1 (toutes les sondes tombent ensemble, comme les deux premières de 2609.36490 fig. 4a, RAPPORTÉ) : randomiser n'apporte rien.
- **Garde contre A8** : la valeur de Nash se calcule par génération ; ce qu'on lit est la **trajectoire** V_g, non une valeur unique.
- **E5b secret contre aléa**, trois bras de même budget : (1) attaquant qui connaît les sondes et p et optimise l'espérance (moyenne sur l'aléa) ; (2) connaît les sondes, pas p ; (3) connaît les sondes déployées, pas la **réserve** (§ 8.1) ; la réserve seule mesure. **H_A** : rappel(3) − rappel(1) ≥ 0,10 : le gain vient du secret ; **H_B** : rappel(3) ≈ rappel(1) ≈ meilleure pure : ni secret ni aléa n'apportent rien face à l'attaquant qui moyenne. Issue intermédiaire préécrite : rappel(1) > meilleure pure mais rappel(3) ≈ rappel(1) : l'aléa compte, le secret non. Contrôle : N-053, récupération après réentraînement contre la réserve.
- **E5c sonde inévitable** : la direction retenue par E3 (causale) ou la projection de Δ contrôlée par P (E2). **H_A** : pour évader cette sonde à FA 1 %, le dommage D du bras rouge chute d'au moins 50 % (illustratif) ; **H_B** : D inchangé — la sonde est contournable sans perte.
- **E5d courbe de coût d'évasion** : D(k) = dommage maximal atteint par le bras rouge tout en évadant k sondes simultanément à FA 1 %. **H_A (converge)** : D(k) décroît et atteint le bruit du jumeau honnête pour k ≤ M ; **H_B (tourne en rond)** : D(k) plat jusqu'à k = M. Critères : ε = 0,05 sur D (illustratif) ; arrêt quand |D(k+1) − D(k)| < ε deux fois de suite ou budget de B tours épuisé (N-059, point 11), B fixé d'avance.
- **Étau à deux mâchoires** : même courbe avec une mâchoire externe comptée parmi les k ; grandeur = C d'E4 en fonction de la dose α et du budget. H_A/H_B comme E4, mais lus **le long du budget** : l'étau serre si C croît avec le budget d'évasion de l'externe (plus l'attaquant travaille l'externe, plus l'interne le prend) ; il ne serre pas si C est plat ou décroît.

---

## (c) Mesure minimale par instrument

Pour chacun : taux de détection, FA, cas honnêtes appariés, vérifications mécaniques à battre.

1. **Oracle du monde planté (N-060 v3)** — rappel par état α sur sabotages attestés par construction ; FA sur jumeau honnête, échecs honnêtes, « mention ». À battre : un comptage mécanique de couverture (citation mot pour mot déjà prévue) **sans** lecteurs ; si les deux lecteurs n'ajoutent rien au programme, ils ne sont qu'un coût. Minimum : rappel ≥ 0,80, FA ≤ 0,05 (illustratifs).
2. **Sonde linéaire / perceptron / attention (mâchoire interne)** — rappel à FA 1 % sur sabotés vs jumeau honnête **et** vs échecs honnêtes, par couche figée ; à battre : sonde β (base en forçage sur le même texte), prédicteur texte 0,866, cascade de portes et sonde sur le dernier état (N-056), étiquettes permutées. Une sonde qui ne bat pas β n'a rien lu dans l'organisme.
3. **Écart apparié à la base (Δ)** — rappel à FA 1 % de la projection de Δ ; à battre : ‖Δ‖ brut (détecteur d'identité) sur P et T100 : si la projection ne fait pas mieux que la norme sur « saboté vs dormant », l'instrument lit les poids.
4. **Organisme placebo** — fonctionne s'il est **indétectable** par la sonde d'acte (AUC ≤ 0,60 vs honnête) **et détectable** par ‖Δ‖ (sinon il n'a pas été modifié) ; FA du placebo sur l'oracle ≤ celle du jumeau.
5. **Mâchoire externe (Jev 1.14 / prédicteur texte / juge code-exécution)** — préalable **E0-bis** : 50 traces honnêtes rejouées + 50 traces sabotées attestées (les faits évoquent 50 traces rejouées pour Jev) ; FA sur les honnêtes, rappel sur les sabotées, par état ; à battre : longueur du code, nombre d'appels d'outils, code de retour d'exécution, taille du diff, régressions des tests existants — toutes mesures mécaniques sans modèle. Un externe qui ne bat pas ces cinq compteurs n'a pas de contenu propre. Minimum avant d'entrer dans la pince : FA ≤ 0,5 % mesuré, rappel > celui du meilleur compteur.
6. **Juge génératif de 3 milliards** — aire 0,523 observée : instrument écarté sauf recalibration ; mesure minimale identique à 5 ; seuil d'entrée : AUC ≥ 0,70 sur le flagrant d'abord.
7. **Moniteur de nouveauté (N1)** — ajusté sur honnêtes seuls ; rappel à FA 1 % sur famille tenue à l'écart ; à battre : perplexité du texte sous la base (nouveauté textuelle) ; cas honnêtes : échecs honnêtes et tâches rares (la nouveauté de tâche est son confondant propre).
8. **Accumulation séquentielle (SPRT, N2) et autocorrélation (N3)** — délai moyen de détection en nombre d'actions à FA 1 % par épisode ; à battre : score max par action (programme § 8.1) ; cas honnêtes : épisodes longs honnêtes (l'accumulation gonfle le FA avec la longueur : vérifier FA par tranche de longueur).
9. **Matrice de transfert** — fonctionne si chaque case a un intervalle de demi-largeur ≤ 0,08 (illustratif) et si la diagonale ≈ 0 (l'évasion contre i évade bien i) : contrôle positif de l'instrument ; sinon le bras rouge n'a pas évadé et la matrice ne mesure rien.
10. **Mélange d'équilibre / réserve secrète** — rappel à FA 1 % sur famille tenue à l'écart, par bras (1)(2)(3) d'E5b ; à battre : R0 figée (qui a gagné sur les tenues à l'écart en arène, faits §4). Si R3 ne bat pas R0 sur un vrai modèle, le résultat d'arène ne se transpose pas.
11. **Pilotage / ablation / substitution** — ne « fonctionnent » que si le contrôle à direction aléatoire laisse D et la tâche inchangés (sinon on casse le modèle, pas le sabotage) ; grandeur : ΔD avec intervalle, dégradation de couverture honnête ≤ 0,05.
12. **Arène synthétique v4** — rejouable sur processeur ; mesure minimale : reproduction des +0,10 / +0,12 et des +0,05 / +0,06 avant toute transposition, puisque les tables B/B′ sont suspendues.

---

## (d) Ancrage matériel

- **Modèle** : le modèle de base de T0.6 n'est pas nommé dans les faits ; toutes les expériences supposent un modèle à poids ouverts avec adaptateurs de rang faible (P-009), sinon ni Δ ni E3 ne sont possibles. Lecteurs de l'oracle et juges : deux familles autres que celle des moniteurs (N-060), à nommer au préenregistrement.
- **Calcul**, tous chiffres **illustratifs** :
  - Extraction d'activations : par épisode, L couches × T jetons × d ; pour L = 8 couches figées, T ≈ 4 000, d ≈ 4 000 en demi-précision, ≈ 250 Mo par épisode ; 2 000 épisodes ≈ 500 Go : ne garder que les couches préenregistrées et les positions d'action, ou réduire par projection figée, sinon le stockage domine.
  - Passages avant : organisme, base en forçage (sonde β et Δ), placebo, témoin : quatre passages par épisode ; 2 000 épisodes × 4 ≈ 8 000 passages ; sur une carte de 80 Go à raison d'environ 10 s par passage ≈ 22 h-carte ; à 3 USD/h-carte ≈ 70 USD. Entraînement des sondes, bootstrap, permutations : processeur, négligeable face à l'extraction.
  - E3b/E3c : interventions avec poursuite d'épisode ; environ 300 épisodes × 5 conditions ≈ 1 500 passages interventionnels ≈ 5 h-carte ≈ 15 USD.
  - E5 (tours du bras rouge) : coût côté attaque hors périmètre ; côté défense, M = 6 sondes × G générations × évaluation sur 500 épisodes : processeur, quelques heures.
  - Oracle N-060 : deux lecteurs sur ≈ 2 000 épisodes ; si lecteurs génératifs de taille moyenne, de l'ordre de 20 à 60 USD selon la longueur des références.
  - Total illustratif : 150 à 250 USD de carte et d'inférence, à mettre en devis écrit avant toute ligne de GO ; seul chiffre du dépôt : Argon 1,82 USD pour un avis (faits §4).
- **Délai** : E0 avant tout (dépend de l'épreuve de l'étiqueteur en cours) ; E1–E2 ensuite sur les modes vus en validation par bloc ; E3 après localisation ; E4–E5 consomment chacune une famille tenue à l'écart neuve (R-1795), donc leur nombre est borné par le nombre de familles disponibles, qui n'est pas dans les faits : c'est la ressource rare, plus que la carte.
- **Pièces produites** : préenregistrement unique E0–E5 avec seuils, couches, hyperparamètres et budget B scellés ; journal du régime d'information par sous-bras ; les sorties sur le mode tenu à l'écart restent scellées jusqu'à G1. **Vérifiable par** recalcul à partir des `scores-p3.npz`, des étiquettes d'oracle et du script de sondes figé ; les interventions E3 par rejeu sur la même graine.

**Ordre de falsification que je propose** : E0 (sans étalon, rien ne compte) → test L2 d'E4 (si la famille « coût » est hors du code, la pince est mal posée et l'effort va à l'interne seule) → E1 contre la sonde β (si la trace n'excède pas la lecture du texte par la base, H8 tient et les sondes se reconçoivent avant E5) → E2/E3 → E5. Ce qui peut être réfuté à chaque étape est écrit ci-dessus ; rien de ce qui précède n'est un résultat.

FIN-DE-CELLULE