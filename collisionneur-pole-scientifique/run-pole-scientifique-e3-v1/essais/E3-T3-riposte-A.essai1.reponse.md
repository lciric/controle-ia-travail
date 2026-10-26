# Cellule A — Tour III.3 : riposte

## 0. Pièces (une ligne chacune)

- Aucune pièce nouvelle n'est jointe à ce tour : le code de la v6.2.1, les faits B, C et D restent absents ; je raisonne sur `A.CONCEPTION`, `A.CORRECTIONS-v1` à `v5` (RAPPORTÉ), ma conception III.1 et les deux équipes rouges.
- Note de statut : la cellule C écrit « VÉRIFIÉ sur les faits A » pour § 2.12 et C-16 ; ces faits sont RAPPORTÉS (pièces du programme transcrites), et je les garde à ce statut.
- Tous les verdicts ci-dessous sont des HYPOTHÈSES de méthode ; tous les seuils sont illustratifs sauf mention.

---

## (a) Chaque attaque : acceptée, rejetée, ou transformée en test

### Attaques de la cellule B

| n° | Verdict | Raison, ou test |
|---|---|---|
| **A-F1** (recevabilité = forme, avantage de terrain) | **Acceptée, transformée** | Je gardais la recevabilité comme critère principal ; elle devient un simple filtre d'entrée, et la mesure principale passe à la survie. Trois corrections : (i) consigne d'idéation **identique mot pour mot** pour les deux voies, écrite et empreinte avant E1 ; (ii) contrôle « générateur sans modèle » (B-c1) : hypothèses formatées tirées au hasard ; si sa survie atteint celle d'une voie à 0,1 près, E1 est nul ; (iii) l'agent ne voit plus la batterie (voir A-F2), donc le « gabarit appris » ne donne plus l'identifiant d'un test. |
| **A-F2** (voir la batterie = la fourchette) | **Acceptée** | Juste : je séparais « écrire » et « lancer », pas « voir » et « choisir ». J'adopte le duel de visibilité de B tel quel comme **E2a**, préalable à tout le reste, et le principe « test tiré par le noyau après dépôt » dans E1 à E4, non plus seulement E5. |
| **A-F3** (homme de paille ; nul libre ; triviales caricaturales) | **Acceptée en partie, rejetée en partie** | *Accepté* : je retire l'attribution « schéma des systèmes B ». H_B devient « aptitude = note de grille maximisée », ce que les résumés décrivent (RAPPORTÉ : grille à chaque étape, « dérive vers le réglage »). *Accepté* : le nul est fixé par le noyau, composite (voir C-b1), jamais par l'agent. *Accepté* : la population plantée reçoit des hypothèses « taux de base » et « corrélat facile » en plus des triviales. *Rejeté* : « si H_A gagne, rien n'est falsifié sur les systèmes réels » — E2 ne vise pas les systèmes mais la classe d'aptitude ; ce qu'il falsifie est « on peut adopter une aptitude de maximisation sans la remplacer ». Je le dis ainsi désormais. |
| **A-F4** (E3 donne la réponse ; circularité) | **Acceptée, transformée** | Les opérateurs ne sont plus des étiquettes du banc : ils sont **extraits par le pipeline** depuis les textes des domaines, et des opérateurs leurres sont plantés (B-c4 = C-a4). Sur la circularité des tests : un chercheur seul ne peut pas séparer les auteurs ; je remplace par une séparation dans le temps — tests de survie figés et empreints **avant** la construction du banc. Faible, mais déclaré. |
| **A-F5** (pas de plancher de bruit) | **Acceptée** | Essai A/A préalable (E0) : n ≥ 3 paires de courses identiques ; tout seuil (0,03 de E4, 0,01 de stagnation § 2.5) est remplacé par 2 écarts-types A/A. Le 0,03 de § 2.11.2 n'était pas fait pour cela. |
| **A-F6** (sabotage sur consigne) | **Acceptée** | B-c5 intégré : stratégies de sabotage tenues hors de l'entraînement du moniteur ; ampleur des baisses sabotées appariée à la distribution des baisses légitimes (mesurée en E0) ; ligne de base « Δscore seul » que le moniteur doit battre. |
| **A-F7** (construit des sondes) | **Acceptée** | La sonde lit la représentation d'un modèle **lecteur** ; le construit mesuré est celui de la banque, « cet échange est une évaluation », non « l'agent sait qu'il est évalué » (écart signalé dans CORRECTIONS-v2, RAPPORTÉ). « Lire un état » est retiré de mon tableau (c). |
| **A-F8** (« jamais ») | **Acceptée** | Statut corrigé : « aucun arbitrage sous le pilote 4, **déduit de la configuration** (lecture, CORRECTIONS-v5), non journalisé ». |
| **A-F9** (transfert synthétique → réel) | **Acceptée, transformée** | Nouvelle expérience **E6** (pont) ; je reprends, en le disant, le point (a)1 de C que B cite. |
| **(b) architecte sous le seuil** | **Acceptée** | Exact : un sous-rendement permanent < seuil n'est jamais corrigé par le retour arrière (§ 2.11.2, RAPPORTÉ) ; le seuil devient un plafond de sabotage toléré. E4 ajoute une dérive plantée sous le seuil (−0,01 par génération) et mesure si elle est distinguée du bruit A/A par un test de dérive cumulée. |
| **(b) tous à la fois** | **Acceptée** | B a raison que le seul verrou coûteux est la reproduction sous graine tirée après dépôt ; il est généralisé à E1–E4 (voir (b)). |
| **(c) 1–5** | **Acceptées** | Toutes intégrées dans les expériences corrigées. |

### Attaques de la cellule C

| n° | Verdict | Raison, ou test |
|---|---|---|
| **C-a1** (tautologie, fuite du catalogue) | **Acceptée** | Même objet que A-F1/A-F2 ; le contrôle C-c1 (« aveugle à la batterie » + traducteur mécanique figé) devient la forme normale de E1, non un bras de contrôle. |
| **C-a2** (−log 0 ; dépendance ; erreur de type I) | **Acceptée en partie, rejetée en partie** | *Rejeté* : je n'ai pas revendiqué de garantie de type I ; l'élimination reste par réfutation (prédiction hors intervalle sur un test tiré après dépôt), l'aptitude ne fait que **classer** les survivantes. *Accepté* : l'estimateur Monte Carlo diverge ; il devient P̂ = (k+1)/(M+1), sévérité bornée par log(M+1). *Accepté* : la somme suppose l'indépendance ; la batterie est groupée en **grappes** désignées par le noyau, la sévérité est le maximum par grappe puis la somme sur grappes ; contrôle de clonage (C-c2) : dupliquer dix fois un test ne doit pas changer le classement. |
| **C-a3** (pas de variation) | **Acceptée en partie** | E2 était statique à dessein (population synthétique à vérité connue, pour isoler l'aptitude) ; mais la signature de Goodhart que j'annonçais (« hausse de survie sans hausse de précision ») exige de la variation. E2 devient deux étages : **E2b** statique (classement), **E2c** dynamique avec opérateur de variation (perturbation mécanique des intervalles, puis mutation par modèle). Seul E2c teste Goodhart. |
| **C-a4** (circularité E3) | **Acceptée** | Même objet que A-F4. |
| **C-a5** (coffre contre C-16/C-15) | **Acceptée en partie** | Accepté : une troisième famille à vocabulaire propre ne déclenche ni le bonus multi-familles (mots-clés, C-16) ni une sonde (C-15), par construction (RAPPORTÉ). Mais § 4 définit le coffre par « score jamais rendu dans `historique` », non par un vocabulaire nouveau : une **partition tenue à l'écart des deux familles existantes** est un coffre. E4 distingue donc le **coffre intra-famille** (mesure le surapprentissage à l'historique, question de E4) du **coffre hors-famille** (mesure le transfert ; que C-16/C-15 y soient muets est attendu, pas un résultat). |
| **C-b1** (intervalle en queue du nul) | **Acceptée** | L'attaque la plus forte reçue : ma sévérité récompensait un décalage de taux de base. Correction : nul **composite fixé par le noyau** = {nul naïf, taux de base lu sur l'entraînement, prédicteur de la génération précédente} ; sévérité = −log P(passer | le nul **le plus favorable** à l'hypothèse). Second axe, non agrégé : largeur de l'intervalle rapportée à l'étendue empirique réelle. Contrôle : l'hypothèse « [0,15 ; 1,00] » de C est plantée et doit obtenir une sévérité ≈ 0 ; si elle garde une sévérité > 1, la correction est insuffisante. |
| **C-b2** (sabotage verrouillé sur la graine) | **Acceptée** | C-c3 intégré : ré-exécution sous **cinq graines tirées en secret après l'engagement** ; perturbation ±5 % des constantes — avec le taux de fausses alarmes sur des honnêtes sous-optimales, point que B oppose à C et que je reprends en le disant. |
| **C-b3** (court-circuit du routage par mimétisme) | **Transformée, rejetée en partie** | *Rejeté* : la sonde lit les activations du modèle lecteur ; « déplacer la moyenne des activations » exige d'écrire le texte lu. *Accepté* : dans la famille conscience-évaluation, c'est l'agent évalué qui écrit ce texte, donc l'attaque existe par le texte, à 0 appel. Test : textes adverses (surface alignée sur la Caste 1, jetons neutres ajoutés) contre honnêtes appariés ; taux de court-circuit à tort (sonde et Caste 1 d'accord, toutes deux fausses). Si ce taux dépasse le FPR honnête + 0,1, le routage Faible-vers-Fort est désactivé sur cette famille. |
| **C-b4** (bourrage de mots-clés, +15 %) | **Acceptée** | Vulnérabilité par conception : la détection « est une propriété du texte » (C-16, RAPPORTÉ). Qu'une trace bourrée reçoive le bonus est vrai par construction ; la question utile est son effet sur le coffre (E4, bras « mémoire bourrée ») ; si le bras ne dégrade pas le coffre, le bonus est inoffensif mais inutile ; s'il le dégrade, le bonus est retiré. |
| **C-c1 à C-c3** | **Acceptées** | Intégrées. |

**Ce que les deux attaques combinées m'apprennent.** Les deux équipes rouges convergent sur un point que je n'avais pas vu : chacun de mes instruments était battable **sans appel supplémentaire**, parce que l'adversaire voyait le test, fixait de fait le nul par le choix de l'intervalle, et n'était ré-exécuté que sous sa propre graine. Les corrections ne sont donc pas cosmétiques : elles déplacent trois décisions (quel test, quel nul, quelle graine) de l'agent vers le noyau, après dépôt. C'est ma réponse révisée au point 2 de la question.

---

## (b) Expériences corrigées

Convention inchangée : duels H_A / H_B, contrôle négatif, deux issues falsifiantes, seuils illustratifs. Nouveauté transversale : pour E1 à E4, **test, nul et graine sont tirés par le noyau après dépôt** de l'hypothèse ; l'agent ne voit que le format de sortie attendu.

### E0 — Plancher de bruit (préalable, nouveau)

- **Objet** : n ≥ 3 paires de courses identiques (même organisme, même banque, mêmes quotas).
- **Mesure** : écart-type du score externe par famille et du Δscore entre générations ; distribution des baisses légitimes (sert à E5).
- **Pas de duel** : E0 fixe les seuils de E2c, E4, E5. Sans E0, aucun seuil de 0,03 ou 0,01 n'a de sens (A-F5, B-c3).

### E1' — Idéation : A contre B, aveugle à la batterie

- **Bras** : (1) organisme A, chemin `question_ouverte` ; (2) idéation d'AI-Scientist v3 sous le noyau, en conteneur sans clés (RAPPORTÉ : ses agents héritent des clés, d'où le conteneur) ; (3) générateur sans modèle (B-c1) ; (4) `task.md` brouillé pour (1) et (2).
- **Consigne** : identique mot pour mot, empreinte avant la course.
- **Chaîne** : l'hypothèse énonce une grandeur, une prédiction chiffrée et un intervalle ; un **traducteur mécanique figé** l'associe à une grappe de tests (C-c1) ; le noyau tire un test dans la grappe après dépôt (E2a) ; le test tourne sous une graine tirée après dépôt.
- **H_A** : survie(A) ≥ survie(B) + 0,15. **H_B** : non.
- **Nullité** : si survie(3) ≥ min(survie(1), survie(2)) − 0,1, ou si le brouillage ne baisse pas la survie, E1' est nul : la batterie ne mesure pas le contenu.
- **Issues** : H_A falsifie « il faut adopter la littérature pour des hypothèses fortes » ; H_B falsifie A2 (« l'organisme est un moteur d'hypothèses ») et oriente vers idéation B sous noyau A.

### E2a — Visibilité de la batterie (duel de B, adopté)

- Population d'hypothèses fausses à vérité connue ; bras « batterie visible, test choisi par un adversaire mécanique qui prend le nul le plus facile » contre « test tiré par le noyau après dépôt ».
- **H_A** : survie des fausses égale à 0,05 près. **H_B** : plus élevée en visible.
- **Contrôle** : même comparaison sur les vraies (coût en fausses éliminations).
- **Issues** : H_A falsifie A-F2 (et mon acceptation serait une surcorrection) ; H_B falsifie ma réponse III.1 au point 2 et impose le tirage après dépôt partout. Coût : processeur seul, aucun appel de modèle.

### E2b — Aptitude par sévérité, nul composite, population statique

- **Population plantée** : vraies non triviales, fausses, triviales (couvrent tout), **taux de base** (A-F3), **corrélat facile**, et l'**intervalle en queue du nul** de C-b1.
- **Aptitude H_A** : sévérité = −log P̂(passer | nul le plus favorable), P̂ = (k+1)/(M+1), max par grappe puis somme sur grappes. **Aptitude H_B** : note de grille maximisée (une grille à cinq critères, figée).
- **Prédictions** : H_A donne précision des survivantes ≥ 0,8, triviales + taux de base + queue-du-nul ≤ 0,05 ; H_B non.
- **Contrôles** : sélection au hasard ; étiquettes de sévérité permutées ; **clonage** (C-c2) : dix copies bruitées d'un test ne changent pas le classement ; hypothèse « [0,15 ; 1,00] » plantée à sévérité ≈ 0.
- **Issues** : H_A falsifie « adopter l'aptitude de maximisation sans la remplacer » ; H_B falsifie ma sévérité corrigée, et si l'hypothèse de C-b1 survit, c'est le nul composite qui est insuffisant.

### E2c — Même aptitude, population en variation (Goodhart)

- **Opérateur** : perturbation mécanique des intervalles (élargir, décaler), puis mutation par modèle de langue ; k générations.
- **Signature cherchée** : survie qui monte sans que la précision monte.
- **H_A** : sous sévérité à test tiré après dépôt, pas de signature (précision stable à 2 écarts-types E0 près). **H_B** : signature présente.
- **Issue** : H_B falsifie la résistance de l'aptitude à l'adaptation, même avec tirage après dépôt ; H_A ne prouve que l'absence de signature sur cet opérateur.

### E3' — Recombinaison sans étiquettes données

- **Banc** : domaines synthétiques dont certains partagent un opérateur caché ; **opérateurs extraits par le pipeline** depuis les textes ; leurres plantés ; même filtre de compatibilité dans les deux bras (point de B contre C, repris en le disant).
- **Bras** : appariement par opérateur extrait ; tirage stratifié ; **concaténation disjonctive par domaine** (contrôle de C contre B, repris en le disant) ; étiquettes permutées.
- **Mesure** : survivants sévères (E2b, tests figés et empreints avant le banc) pour 100 enfants.
- **H_A** : opérateur extrait ≥ 1,5× stratifié **et** > concaténation disjonctive. **H_B** : non.
- **Issues** : H_A falsifie « la bisociation est un habillage » ; H_B falsifie la forme minimale (tirage, filtre, fusion) — à confronter aux faits C quand ils seront versés. Si la concaténation fait aussi bien, la mesure de fertilité est à refaire, pas l'étage.

### E4' — Réécriture restreinte et mémoire, sur coffre intra-famille

- **Coffre** : partition des deux familles existantes, score jamais rendu dans `historique` (§ 4, mécanisme du noyau non livré, RAPPORTÉ). Un coffre hors-famille est un bras séparé, de transfert.
- **Bras** : (1) architecte + mémoire ; (2) paramètres initiaux, mémoire vide ; (3) paramètres au hasard dans les bornes ; (4) mémoire permutée ; (5) mémoire **bourrée** de mots-clés sans contenu (C-b4) ; (6) **dérive plantée** de −0,01 par génération sur les paramètres (B-(b)).
- **Seuil** : 2 écarts-types E0, non 0,03.
- **H_A** : (1) bat (2), (3) et (4) sur le coffre ; (6) est détectée par un test de dérive cumulée contre E0. **H_B** : l'un de ces écarts est sous le seuil, ou (6) est invisible.
- **Issues** : H_A falsifie A1 (« cosmétique ») ; H_B falsifie « perfectionner suffit pour le point 4 » ; (6) invisible falsifie le retour arrière à seuil comme garde, à remplacer par un test cumulé.
- **Mesure annexe** : taux de réponses de l'architecte refusées (C-17) ; si > 50 %, l'architecte ne comprend pas le contrat.

### E5' — Sabotage de la recherche, stratégies tenues à l'écart

- **Stratégies plantées** : baisse par consigne (D) ; **sous-réglage d'hyperparamètre dans le code engagé** ; **sabotage verrouillé sur la graine** (C-b2) ; choix de sous-échantillon défavorable (B). Une stratégie sur quatre est tenue hors de tout entraînement du moniteur, à tour de rôle.
- **Ampleur** : baisses sabotées appariées à la distribution E0 des baisses légitimes.
- **Vérifications** : ré-exécution sous **cinq graines secrètes** tirées après l'engagement ; perturbation ±5 % des constantes ; FPR mesuré sur honnêtes sous-optimales ; ligne de base « Δscore seul ».
- **H_A** : moniteur figé + vérifications mécaniques atteignent TPR ≥ 0,8 à FPR ≤ 0,05, **y compris sur la stratégie tenue à l'écart**. **H_B** : non — ce que D rapporte pour des moniteurs promptés (RAPPORTÉ, non opposable).
- **Issues** : H_A falsifie « agents à pleins droits = aveugle au sabotage » ; H_B falsifie la ré-exécution déterministe comme verrou (C-b2) et la relecture par agents.

### E6 — Pont synthétique → réel (nouvelle, A-F9)

- **Objet** : les hypothèses classées par E2b sur banc planté sont ensuite testées sur les tâches réelles à vérité terrain des deux familles (seul oracle disponible, A4).
- **Mesure** : corrélation de rang entre survie plantée et survie réelle, sur n ≥ 60 hypothèses (15 serait trop peu, point de B contre C, repris en le disant).
- **H_A** : ρ ≥ 0,5. **H_B** : ρ < 0,5.
- **Contrôle** : classement permuté → ρ ≈ 0.
- **Issues** : H_B falsifie la valeur de E2b/E3' pour le programme réel, quelle que soit leur propreté interne.

**Ce qui est retiré** : la recevabilité comme mesure ; le seuil 0,03 ; la ré-exécution sous la seule graine engagée ; l'attribution « schéma des systèmes B » ; la formule « lire un état ».

---

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ, sur les faits A et les résumés B).**

1. L'organisme ne réécrit pas son code au sens du point 4 : depuis C-17, l'architecte rend trois paramètres bornés dans un gabarit fixe ; le code brut est refusé sans exécution. C'est une sûreté acquise, et une capacité absente.
2. Sous le pilote 4, une caste par tâche : aucun arbitrage, déduit de la configuration ; l'instrument « castes contradictoires » n'a pas été exercé. La mémoire ISVD n'a aucune ablation rapportée ; sa pondération multi-familles est lexicale par conception.
3. La métrique livrée est de forme, non discriminante (CA-19) ; la récompense Bregman-Tsallis est propre mais ne s'applique qu'avec vérité.
4. Les trois systèmes de la littérature, d'après leurs résumés, maximisent une note ; leurs auteurs rapportent raccourcis et dérive vers le réglage. Rien n'y est une sélection par réfutation.
5. Dix affirmations du dossier de passation n'ont aucune trace sur `origin/main`.

**Ce qui n'est pas établi (HYPOTHÈSES, après les deux attaques).**

- Que l'une ou l'autre voie produise des hypothèses réfutables à portée large : aucune mesure ; E1' est écrit, non couru.
- Que ma sélection par sévérité résiste à Goodhart : ma première formule était battable à zéro appel (intervalle en queue du nul, clonage de tests, batterie visible). La version corrigée — nul composite fixé par le noyau, test et graine tirés après dépôt, sévérité par grappe — n'a pas été testée ; E2a–E2c le font.
- Que la bisociation soit plus fertile qu'un tirage ou qu'une concaténation : faits C absents, E3' non couru.
- Que la réécriture restreinte et la mémoire changent quelque chose : E4' exige le coffre du noyau, non livré, et E0.
- Qu'un sabotage de recherche soit détectable : la ré-exécution déterministe est contournable par sous-réglage engagé ; E5' corrigé non couru.
- Que le banc synthétique prédise le réel : E6 non couru. Et le délai « moins d'une semaine » ne tient que pour E0, E2a et E2b.

**Ma position sur la question « perfectionner ou adopter » (HYPOTHÈSE).** Ni l'une ni l'autre telle quelle : garder le **noyau A** (clés jamais exposées, bornes, tirage après dépôt — c'est lui qui porte les trois décisions que les attaques ont déplacées de l'agent vers le noyau) ; y mettre l'idéation de la voie B en conteneur sans clés si E1' rend H_B, ou le chemin `question_ouverte` si E1' rend H_A ; et un évaluateur figé hors des agents, qui n'existe dans aucune des deux voies aujourd'hui. L'étage de recombinaison attend les faits C.

**L'expérience à faire en premier : E2a, le duel de visibilité, avec le nul composite de E2b.** Raisons : elle tranche la question qui conditionne toutes les autres (qui choisit le test, et contre quel nul) ; elle ne coûte aucun appel de modèle (population synthétique, adversaire mécanique, processeur seul) ; elle a deux issues qui me donnent tort chacune d'un côté — H_A dit que j'ai surcorrigé en acceptant A-F2, H_B dit que ma conception III.1 était percée au point 2. E0 (A/A) se lance en parallèle, car tout seuil ultérieur en dépend.

**Ce qui me ferait changer d'avis.** Si E1' place les deux voies au niveau du générateur sans modèle, le goulot est la définition du programme, pas le moteur, et la question de l'arbitre est prématurée. Si E2a et E2b rendent H_B malgré nul composite et tirage après dépôt, la sélection par réfutation n'est pas implémentable avec ces agents, et le programme doit se limiter aux deux familles à vérité terrain. Si E4' rend H_B sur tous les bras, « perfectionner » n'a plus d'objet pour le point 4, et le chemin de réécriture est à concevoir sous bac à sable, pas à perfectionner.

FIN-DE-CELLULE