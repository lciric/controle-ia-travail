# Préenregistrement — la recombinaison bisociative à deux espaces sur mondes synthétiques — v2 — BROUILLON 1, NON SCELLÉ

**Squelette à contre-lire (R2) puis sceller avant tout code d'expérience (R1). Aucune méthode, aucun monde n'a été exécuté. Les marqueurs `[À GELER PAR LAZAR]` et `[À SCELLER]` doivent tous avoir disparu avant scellement (recherche textuelle ; le validateur du dépôt ne les voit pas).**

- Auteur : sous-agent neuf, Sonnet 5.5 (`claude-sonnet-5-5`). **Non-auteur** de la question, des pièces A à D, de l'avis d'Opus, de la synthèse du collisionneur, du code du pôle, de `trancher-recombinaison-v1`. Ne peut pas être contre-lecteur de ce brouillon.
- Date (UTC), relevé `date -u` : 2026-10-30T00:42:35Z.
- Commit du code d'analyse : aucun code à ce jour ; `[À SCELLER]` : le code s'écrit **après** scellement, son empreinte est consignée dans le manifeste avant le premier run (R9).
- Documents qui font foi (chemins relatifs au dossier `envois/pole-scientifique-automatique-v1/`, SHA-256 recalculés) :
  - `bisociation-deux-espaces-v1/question-bisociation-deux-espaces-v1.md` `73a30ab727445969b7ecb8300ba0fef5efd7dfcf9c59cd93943d6ce77e1c4cc3` (critères de lecture de la synthèse gelés) ;
  - `…/avis-opus-neuf-bisociation-v1.md` `2331e70f5fb02530982d535447c88aedade769facd661d882a27e386b57ae3e1` ;
  - `…/entrees/synthese-collisionneur-bisociation-v1.md` `49dd38406b865eae742793045472cac3385e29ef3f3cf1921841df4d94361fb0` ;
  - `…/recoupement-bisociation-v1.md` (recoupement des deux ; empreinte dans la réponse qui livre ce brouillon) ;
  - `orchestrateur-pole-v7/pole/recombinaison.py` `71faad38644c77ae2cc21f23bfb1011c48fe674a08e542983819425ee47bd3d0` (pièce A) ;
  - `trancher-recombinaison/trancher-recombinaison-v1.md` `72cff8a067641cab173f3b6fbba32976a64989ded279d078ec4da432a582e4bf` (pièce B, nommée « B » ci-dessous) ;
  - `trancher-recombinaison/preenregistrement-trancher-recombinaison-v1.md` `5335614b2b8b38deb50408c4755401242e5a8436f82b1f9e8be48e57f9dd2985` ;
  - `trancher-recombinaison/monde_v1.py` `af907b1d5d779dfc1c4353503d31059f20d031a4b4324fea3ca775ad6a6bc98c` ; `methodes_v1.py` `2f7a8b1192a79d5bed64fb48f9a5db6f1df6bf86e3a2296eafca75493f2790dd` ; `mesures_v1.py` `0a1e3c3806ae892a526fa6a21bcf07217e6f41118244a7cdd01a2f8ad9f8a82e` ; `conditions_v1.py` `9246ecc6a4a71f8a701600a0c55c549d622423496a436f2f708b0d9ffe53af35` ; `trancher_v1.py` `781335dda51954f5d4ac1ab25ce0ce850a421d8c0c2346ae8284fddc8a6609e0` ;
  - `registres/decisions.md`, ligne R-500 (Lazar, 29 octobre, 13:23 heure de Paris : **loin en domaine, proche en concept**, signe de β positif) ; ligne R-497 (champ « concepts mobilisés », test préenregistré v2).
- Chiffres : tous renvoient à B (tableau § 1 et § 7) ou à l'avis d'Opus ; les calculs de l'auteur du brouillon sont marqués (M) ; ce qui n'est dans aucune pièce est marqué SUPPOSÉ (R7).
- Résultats de l'essai v1 rappelés ici comme **références de dimensionnement seulement** : précision du stratifié 0,203 (« bien ») et 0,127 (« moyen »), marche de Swanson +3,5 et +3,8, strates dissemblables d'abord +11,9 et +6,6, vérité inversée −11,6 pour ce dernier (B § 1 et § 2.2).

### Nœuds ouverts avant scellement (détail : `recoupement-bisociation-v1.md`, § 3 et § 7)
1. **Seuil d'adoption** : `[À GELER PAR LAZAR]` ; aucun défaut appliqué (section « Seuil »).
2. Défauts de 48 h supposés pris sauf mot contraire : qualité q ≡ 1 dans le candidat (D-a) ; sélection en factoriel « par strate » × « déterminant sur paires » (D-b) ; facteur de concept (κ + 0,05)^1 (D-c) ; exposants a priori, grille en diagnostic (D-d) ; 1 200 mondes de décision (D-g).
3. Concrétisations propres à ce brouillon, que ni la synthèse ni l'avis ne fixent, à contre-lire en priorité : l'ordre des strates par score de strate ; la rareté appariée des étiquettes de pont ; le placebo de concepts par permutation du score ; concept := étiquette d'opérateur sur les mondes v1 ; le dénominateur 12.
4. Contre-lecteur : sous-agent neuf, à désigner (section « Contre-lecture »).

## Hypothèse

**H-B2 (hypothèse de travail de la question `73a30ab7…` et de R-497, signe levé par R-500).** Sur des mondes synthétiques à vérité plantée **à deux espaces** (un espace de domaines, un espace de concepts mathématiques sous-jacents, séparables), tirer les paires à recombiner par un **score de paire produit**, *loin en domaine* ET *proche en concept*, avec sélection par strate, apporte plus de vrais ponts que :
- (i) le tirage stratifié (b), (ii) la forme corrigée de la v6.3 (a), (iii) la marche de Swanson par étiquette rare d'opérateur (d1) et par étiquette de concept (d1c) ;
- (iv) ses propres ablations qui retirent le concept (N_β0) ou ne l'emploient que comme **filtre** (N_filtre).

Lecture de la question en deux volets, à ne pas confondre :
- **volet d'adoption** : N (forme commune, définie au plan d'analyse) est-elle meilleure que les témoins, sous contrôles ? ;
- **volet « ingrédient manquant »** : la proximité conceptuelle **dans l'objectif** apporte-t-elle quelque chose que ni l'éloignement seul ni le filtre ne donnent ?

Hypothèses de travail du monde (SUPPOSÉES, elles encodent l'hypothèse ; l'avis d'Opus et B § 6 le disent) : (W1) les concepts existent comme variables latentes séparées du domaine ; (W2) leur observation passe par un canal à trois niveaux (couverture, parasites, fuite de domaine) ; (W3) la vérité est « champs différents ET concept latent commun non moyeu ET contraintes vraies compatibles ». Leur prix est mesuré par V_fuite, V_concepts_absents, la non-régression sur les mondes v1 et la validation du générateur.

Ce que ce test ne dit pas (B § 6) : rien sur la qualité des fiches fusionnées par un modèle ; rien sur les vraies fiches (préenregistrement distinct, lecture descriptive).
Antériorité (R8) : **la forme n'est pas revendiquée comme inédite**. Le principe « proche en mécanisme, loin en domaine » est probablement occupé (Gentner 1983 ; Hope et collaborateurs 2017 ; Berthold 2012 ; Chan et collaborateurs 2018 — de mémoire, non vérifié sur PDF, R7). Seule la forme et son test à vérité plantée sont en jeu ; vérification d'antériorité avant toute revendication.

## Prédiction chiffrée et signe attendu

Ordres de grandeur SUPPOSÉS, ancrés sur B (références rappelées dans l'en-tête) : borne basse = marche de Swanson v1 (+3,5 ; +3,8), borne haute = strates dissemblables d'abord v1 (+11,9 ; +6,6). Chaque ligne donne ce qui compterait comme réfutation ; les lignes sont lues symétriquement (R3, R4).

| # | Contraste | Signe | Ordre de grandeur | Réfutation de la prédiction |
|---|---|---|---|---|
| P1 | N − b, « bien » | + | +4 à +12 points | borne haute < seuil `[À GELER PAR LAZAR]` ; < 0 = N perd |
| P2 | N − b, « moyen » | + | +2 à +7 points | idem |
| P3 | N − d1c (« bien », « moyen ») | + ou nul | +1 à +5 points | borne haute ≤ 0 dans les deux : « Swanson guidé par concepts suffit » (issue permise) |
| P4 | N − N_β0 (apport du concept) | + | +3 à +8 points | borne haute < δ_non (+2) dans les deux |
| P5 | N − N_filtre (concept dans l'objectif contre filtre) | + | +1 à +5 points | borne haute < δ_non dans les deux : « le concept suffit comme filtre » |
| P6 | placebo de concepts : N sous vrai score − N sous score permuté ; N_PC − N_β0 | + ; ≤ 0 | ≥ δ ; ≤ 0 | un gain de N_PC sur N_β0 = artefact (audit R4) |
| P7 | monde sans pont (SP) : N − b, N − d1c, N − N_β0 | 0 | 0 | intervalle à 99 % excluant 0 = artefact |
| P8 | vérité inversée : Δ_INV − Δ_bien (Δ = N − b) | − | −5 à −20 points | borne haute ≥ 0 : N ne cible pas l'éloignement |
| P9 | fuite de domaine ρ = 0,6 : Δ_V_fuite − Δ_bien | − | −1 à −6 points | borne haute ≥ 0 : l'avantage ne vient pas des concepts |
| P10 | non-régression (mondes v1) : N − b | ≥ −1 | ≥ 0 attendu | borne basse < −1 |
| P11 | descriptive : N_dpp − N ; N_global − N | ≤ 0 | −6 à 0 ; \|N_dpp − N_global\| ≤ 1 | aucune réfutation de verdict (diagnostic) |

Justification de P8 (M) : sur v1, le diagnostic d'éloignement passe de +11,9 à −11,6, soit −23,5 (B § 7.2) ; N mêle éloignement et concept, d'où une chute plus faible. Confiance de l'auteur du brouillon : 0,55 sur P1, 0,40 sur P3, 0,50 sur P4 (SUPPOSÉ ; l'avis d'Opus donne 0,45 pour « bat d1 sur les mondes étendus »).

## Métrique

**Unité** : le monde. **Budget** : k = 4 paires par génération × 3 générations = 12 paires, mêmes 40 candidats (8 domaines × 5 articles), une paire acceptée n'est plus retirée (B § 5).

**Vrai pont** (latent, jamais lu par une méthode) : champs différents (proches dans le monde inversé), concept latent commun **non moyeu**, contraintes vraies compatibles. Une paire qui partage un opérateur latent non moyeu partage son concept (emboîtement, voir générateur).

**Précision (primaire)** : π(X, m) = (nombre de vrais ponts parmi les paires tirées par X dans le monde m) / **12**. Une abstention compte comme un échec (dénominateur fixe : aucune sélection par la sortie d'un bras). Un bras déclaré non applicable d'avance (d1c dans V_concepts_absents et dans les mondes v1) est exclu de la condition, non noté zéro.

**Estimateurs** : moyenne sur les mondes ; écart apparié Δ(X, Y ; condition) = moyenne sur m de [π(X, m) − π(Y, m)] ; rapport ρ(X, Y) = moyenne de π(X) / moyenne de π(Y). Écarts entre conditions (INV, V_fuite contre « bien ») : ensembles de mondes distincts, rééchantillonnage indépendant des deux.

**Intervalles** : percentiles de 2 000 rééchantillonnages des mondes (appariés pour un écart), niveau **95 %** pour les contrastes décisifs, **99 %** pour les contrôles placebo (SP, placebo de concepts, non-régression). Graine : rôle 99 de la dérivation (plan d'analyse, § 7).

**Secondaires (descriptifs)** : rappel ; rappel par mécanisme (greffe, jumeau, pont conceptuel) ; pièges tirés par classe (moyeu d'opérateur, moyeu de concept, surface, homonyme rare, faux pont, parasite, autre — classes de `mesures_v1.classe_pont` étendues) ; strates distinctes par paire ; **articles distincts parmi les 12 paires** (réutilisation d'un article) ; part de paires éloignées et conceptuellement proches (latent, et observé) ; précision placebo en SP (part des paires tirées qui appartiennent à un ensemble de 6 paires valides tirées au hasard, graine propre au monde, indépendante des bras, comme en v1) ; fuite mesurée de la validation.

## Seuil

**Seuil d'adoption : `[À GELER PAR LAZAR]`. Aucun défaut ne s'applique à un seuil de préenregistrement.** Règle paramétrique, conditions X ∈ {M_bien, M_moyen} : Δ(N, b ; X) ≥ **θ_abs**, ρ(N, b ; X) ≥ **θ_rel**, borne basse à 95 % de Δ > 0.

| Option | θ_abs ; θ_rel | Équivalent sur les chiffres v1 (M, de B § 1) | Avantage | Inconvénient |
|---|---|---|---|---|
| (a) v1, question | +12 ; (aucun) | ×1,59 en « bien », ×1,94 en « moyen » | continuité avec le scellé v1 | hors d'atteinte : l'éloignement seul fait +11,9 et +6,6 ; critiqué par les trois modèles |
| (b) avis d'Opus | +5 ; ×1,25 | plancher efficace +5,1 (« bien », rapport) et +5 (« moyen », ×1,39) | atteignable ; absolu et relatif | franchi par l'éloignement seul : à coupler à N − N_β0 ≥ δ |
| (c) synthèse (A) | ×1,3 ; et Δ(N, b) ≥ Δ(b_eloigne, b) − 2 | +6,1 et +3,8 ; +9,9 et +4,6 | teste le concept, pas l'éloignement | dépend d'un témoin incertain en monde v2 |

Recommandation de l'auteur du brouillon : (b) comme plancher d'adoption **plus** les contrastes de détection ci-dessous ; confiance 0,5. b_eloigne-observé reste témoin, sans seuil de supériorité.

**Seuils proposés, à geler avec le reste après contre-lecture (tous SUPPOSÉS ; sources : avis d'Opus, synthèse)** :
- détection « le concept apporte » δ = +3 points (Opus ; B de la synthèse : 2) ; « le concept n'apporte pas » δ_non = +2 points, sur la borne haute ;
- non-régression : borne basse ≥ −1 point (Opus) ;
- validation du générateur : voir le plan d'analyse, § 6 ; plafond de l'oracle ≥ 0,30 en « bien » et « moyen » (Opus) ;
- écart-type apparié de Δ(N, b) sur les mondes de validation ≤ 18 points (référence 15,3, M, tirée de la demi-largeur 1,5 à 400 mondes de B § 1).

**Taux d'erreur visés** : intervalles à 95 % (décisifs) et 99 % (placebo) ; puissance 0,8 pour un effet de 3 points à 1 200 mondes (plan d'analyse, § 8).

## Plan d'analyse

### 1. Générateur `monde_v2.py` (nouveau nom, R12 ; étend `monde_v1.py` `af907b1d…`)
Base de v1 conservée : 8 domaines × 5 articles, 2, 3 ou 4 champs tirés par monde, 3 opérateurs par groupe, moyeu d'opérateur à 25 %, 3 greffes, 3 jumeaux, vecteur de domaine par fréquences brutes (cosinus validés 0,54 / 0,28 / 0,03, B § 5), q uniforme sur [0,5 ; 1,5] **indépendante de la vérité**, étiquette de domaine juste à 0,95. Ajouts (nombres SUPPOSÉS, repris de l'avis d'Opus § 3 sauf mention) :
1. **Concepts latents** : 10 concepts non moyeux, répartis en ensembles disjoints par champ (au moins 2 par champ), plus 1 concept moyeu présent dans 30 % des articles. Chaque opérateur de groupe et chaque opérateur propre à un article reçoit un concept de son champ ; une greffe garde le concept de l'opérateur importé ; un jumeau reçoit un concept non moyeu tiré. Conséquence voulue : hors plantation, deux articles de champs différents ne partagent aucun concept non moyeu (aucun vrai pont organique). Emboîtement : tout opérateur commun non moyeu entraîne un concept commun.
2. **Vrais ponts conceptuels** (3 par monde) : deux articles non utilisés de champs différents reçoivent chacun un opérateur propre de **nom différent**, sous un **même** concept non moyeu ; contraintes rendues compatibles.
3. **Ponts de surface** (3) : paires éloignées dont un mot de surface est étiqueté par le lexique d'opérateurs comme le même opérateur (homonymie), opérateurs latents et concepts latents **différents**.
4. **Faux ponts** (3) : paires éloignées qui partagent un concept non moyeu mais dont les contraintes vraies sont incompatibles (un axe + contre −).
5. **Ponts proches** (3) : paires d'un même champ sous un même concept, contraintes compatibles ; faux en monde ordinaire, vrais en monde inversé.
6. **Homonymes rares de concept** (3) : paires éloignées dont les concepts latents diffèrent mais dont les mots reçoivent la même étiquette de concept, de fréquence documentaire 2 à 4.
7. **Rareté appariée** : la fréquence documentaire de l'étiquette (opérateur ou concept) qui porte chaque pont planté — vrai, faux, de surface, homonyme rare — est tirée dans {2, 3, 4} par la même loi, indépendante du statut. Sinon la rareté serait un indice du statut (défaut reproché aux « concepts inversés sur moyeux », § 4 de la synthèse).
8. **Canal d'observation des concepts** : couverture, parasites, fuite de domaine ρ (probabilité qu'une étiquette couverte soit remplacée par le concept dominant du domaine). Niveaux « bien » (0,85 ; 0,05 ; ρ = 0,05), « moyen » (0,65 ; 0,15 ; 0,15), « mal » (0,45 ; 0,30 ; 0,30). Deux mots de surface par concept, indépendants du domaine ; un mot non couvert retombe dans le sac du domaine (fuite lexicale vers le vecteur de domaine, mesurée à la validation). Le canal d'observation des opérateurs et des contraintes est celui de v1 (niveaux 0,90 / 0,05 / 0,05, 0,70 / 0,15 / 0,10, 0,45 / 0,30 / 0,20).
9. **Placebo de concepts** : fonction `placebo_score(monde, rng)` qui permute les vecteurs de concepts entre les articles d'un même domaine observé (fréquences d'étiquettes conservées) ; la permutation s'applique à tout vecteur ou graphe de concepts **utilisé pour classer ou tirer** ; l'étage commun garde les vraies étiquettes, donc les paires valides sont inchangées. La même permutation sert à tous les bras du monde.

### 2. Étage commun (identique pour tous les bras)
Une paire est valide si : domaines observés différents ; filtre de compatibilité des contraintes observées passé ; partage d'**au moins une étiquette d'opérateur ou de concept**. Le pont retenu est l'étiquette partagée la plus rare (départage par nom). Tous les bras voient les mêmes observations (R4).

### 3. Quantités du candidat
- cos_ij : cosinus observé des vecteurs de domaine (`monde["cos"]` de v1).
- Vecteur de concepts de l'article i : étiquettes de concept observées, poids log(40 / fréquence documentaire), norme 1. κ_ij = produit scalaire ∈ [0, 1]. **Vecteur nul : κ = 0, déclaré, compté et rapporté** (jamais NaN, jamais de repli silencieux, R5).
- Score de paire s_ij = (1 − cos_ij²)^e × (κ_ij + ε)^β × [q_i q_j seulement dans N_q].
- Strate : paire de domaines observés. Score de strate = plus fort s_ij de ses paires restantes.

### 4. Bras
| Code | Rôle | Définition |
|---|---|---|
| **N** | **candidat, forme commune retenue** | score s_ij, q ≡ 1, e = 8,5 ; β = 1 ; ε = 0,05 (a priori, voir § 5). Tour des strates dans l'ordre décroissant du score de strate ; chaque strate donne sa meilleure paire restante ; scores recalculés à chaque tour ; départages tirés par la graine du bras. Aucun déterminant. |
| b | témoin | tirage stratifié de v1 (`stratifie`) |
| a | témoin | forme corrigée v6.3 de v1 (`corrige`, avec q) |
| d1 | témoin | marche de Swanson par étiquette rare d'opérateur (v1) |
| d1c | témoin | même marche sur les étiquettes de concept (loi exacte, tirage sans remise parmi les paires valides) |
| c | référence | tirage uniforme parmi les paires valides |
| b_eloigne | témoin de référence | strates de cosinus moyen ≤ médiane d'abord (`stratifie_eloigne` de v1, observé) |
| oracle | plafond | vraies paires d'abord |
| N_β0 | ablation | β = 0 : domaine seul |
| N_α0 | ablation | e = 0 : concept seul |
| N_filtre | ablation | stratifié (b) parmi les paires de strates éloignées (cosinus moyen ≤ médiane) qui partagent un concept (κ > 0), puis le reste en tour stratifié |
| N_aleat | ablation | ordre des strates aléatoire (rebattu à chaque tour), meilleure paire par score dans la strate |
| N_global | ablation | les 12 plus forts s_ij, sans strates |
| N_dpp | ablation, forme (O3) de l'avis d'Opus | ensemble de base = paires valides ; qualité de la paire = s_ij de N ; répulsion S^D ⊙ S^C et noyau L = diag(√s)(S^D ⊙ S^C)diag(√s) + γI, γ = 10⁻³, définis dans `avis-opus-neuf-bisociation-v1.md` § 1 ; glouton par Cholesky (`cholesky` et `tirage_glouton` de la pièce A) ; **seule la règle de sélection diffère de N** |
| N_fiches | ablation, option ⊙ de la question | noyau sur les fiches S_ij = cos_ij² · κ_ij², q ≡ 1, γ = 10⁻³, même chaîne que (a) |
| N_q | ablation, candidat d'Opus | N avec le facteur q_i q_j |
| N_rare | ablation, facteur de C | κ remplacé par la rareté de l'étiquette partagée la plus rare : log(40 / fréquence) / log(20) |
| N_PC | placebo | N sous le score permuté (§ 1, point 9) |
| N_grille | diagnostic | N réglé sur la grille du § 5 (non éligible) |

Formes de v1 non reprises : (d2) et (e), échecs de B § 4 ; elles reviennent si Lazar le demande.

### 5. Hyperparamètres
- A priori `[À GELER PAR LAZAR]` (défaut 48 h : celui-ci) : e = 8,5 (règle : une paire à cos 0,28 pèse la moitié d'une paire à cos 0 ; (M) 8,49, accord avec l'exposant ≈ 17 de B et C et avec α = 8 d'Opus) ; β = 1 ; ε = 0,05 (règle : une paire sans concept partagé pèse environ le dixième d'une paire de κ = 0,5, (M) 0,09).
- Grille diagnostique (non éligible) : e ∈ {1, 2, 4, 8, 16} × β ∈ {0,5 ; 1 ; 2 ; 4}, sur 200 mondes de validation « moyen » seuls, scellée avant les mondes de décision ; elle ne change ni N ni le verdict.

### 6. Conditions et validation du générateur
| Condition | Mondes | Définition |
|---|---|---|
| M_bien, M_moyen | 1 200 chacune | niveaux bien et moyen du § 1 point 8 |
| M_mal | 600 | niveau mal ; descriptive, abandonnée si le plafond de l'oracle < 0,30 |
| SP | 600 | M_bien sans aucun pont planté ; vérité vide ; mesure : précision placebo |
| INV | 600 | M_bien, vérité inversée : ponts entre domaines proches, groupes d'opérateurs transversaux (miroir de v1), concept toujours partagé |
| V_fuite | 600 | M_bien avec ρ = 0,6 |
| V_concepts_absents | 600 | M_bien sans aucune étiquette de concept (κ = 0 déclaré, N se réduit à N_β0 par la règle du § 3) |
| V_moyeu_conceptuel | 600 | concept moyeu à 0,6 |
| V_surface | 600 | 9 ponts de surface au lieu de 3 |
| NR_bien, NR_moyen | 600 chacune | `monde_v1.py` inchangé ; concept := étiquette d'opérateur (dit explicitement : ni Opus ni la synthèse ne disent comment N tourne sans concepts) |

**Validation du générateur, avant toute méthode, sur graines distinctes (300 mondes « bien », 300 « moyen », 100 jumelles) ; seuils SUPPOSÉS** :
- cosinus moyens même domaine / proches / éloignés dans [0,51 ; 0,57], [0,25 ; 0,31], [0,00 ; 0,06] (référence v1 ± 0,03) ;
- fuite de domaine sur les paires valides : corrélation de rangs entre κ observé et cos observé, **moins** la même quantité calculée sur les latents (indicatrices « concept latent commun » et « mêmes champs ») ≤ 0,10 en « bien » ; loi nulle par permutation des vecteurs de concepts entre articles d'un même domaine, rapportée ;
- queue : parmi les 10 % de paires valides de plus fort κ, part de paires du même champ, en excès sur l'oracle latent ≤ 0,10 ;
- jumelles : mondes régénérés en échangeant les mots propres de deux domaines pour les articles-ponts, mêmes latents : concordance des étiquettes de concept ≥ 0,9 et variation des cosinus de domaine ≥ 0,2 ;
- rareté appariée : écart entre statuts (vrai, faux, surface, homonyme rare) de la fréquence documentaire moyenne de l'étiquette de pont ≤ 0,5 ;
- vraies paires valides par monde ≥ 6 en moyenne (« moyen ») ; plafond de l'oracle ≥ 0,30 (« bien », « moyen ») ; le plafond de v1 en « moyen » était 0,487.

### 7. Graines (R9)
- Deux racines entières `[À SCELLER]`, propositions : RACINE_DECISION = 20261031000000 ; RACINE_VALIDATION = 20001231000000 (distincte de celle de v1 et de toute graine de validation de v1).
- Chaque tâche reçoit `numpy.random.SeedSequence(entropy=RACINE, spawn_key=(code_condition, indice_monde, code_rôle))` (numpy ≥ 1.25).
- Codes de condition : M_bien 1, M_moyen 2, M_mal 3, SP 4, INV 5, V_fuite 6, V_concepts_absents 7, V_moyeu_conceptuel 8, V_surface 9, NR_bien 10, NR_moyen 11.
- Codes de rôle : monde 0 ; observation des opérateurs 1 ; observation des concepts 2 ; contraintes 3 ; placebo de concepts 4 ; placebo de SP 5 ; bras 10 + rang du bras dans la liste figée du § 4 ; rééchantillonnage 99.
- Manifeste par run (`src/controle_ia/manifeste.py`) : configuration et empreinte, versions de Python et de numpy, racines et clés de dérivation, empreintes du code, commit.

### 8. Comparaisons, multiplicité, puissance
- Contrastes décisifs (95 %) : C1 Δ(N, b) ; C2 Δ(N, a), Δ(N, d1), Δ(N, d1c) ; C3 Δ(N, N_β0) ; C4 Δ(N, N_filtre) — en M_bien et M_moyen. C5 placebo : Δ(N, N_PC) apparié par monde et Δ(N_PC, N_β0) (99 %). C6 SP (99 %). C7 INV. C8 V_fuite. C9 non-régression (99 %).
- Descriptifs (95 %) : N contre b_eloigne, N_aleat, N_global, N_dpp, N_fiches, N_q, N_rare, N_α0, N_grille ; M_mal ; V_concepts_absents ; V_moyeu_conceptuel ; V_surface ; résultats par nombre de champs (2, 3, 4).
- Multiplicité : les règles d'adoption et de lecture sont des **conjonctions** (toutes les conditions doivent tenir), chacune à son niveau : pas de correction. Les contrôles à 99 % limitent les fausses alertes (M : quatre écarts indépendants, 3,9 % contre 18,5 % à 95 %).
- Valides par monde (M) : les précisions placebo de B § 2.1 (0,138 pour le tirage uniforme, sur 6 paires placebo) impliquent environ 43 paires valides en v1 « bien » ; le budget de 12 en couvre environ le quart. À mesurer en v2, où l'étage commun s'élargit aux étiquettes de concept.
- Puissance (M, SUPPOSÉE pour v2) : écart-type apparié 15,3 points (demi-largeur 1,5 à 400 mondes, B § 1). À 1 200 mondes : erreur type 0,44, demi-largeur 0,87 (95 %) et 1,14 (99 %), plus petit effet détectable 1,24 point à puissance 0,8 (1,48 avec quatre contrastes corrigés). 204 mondes suffiraient pour 3 points (290 corrigé) ; 460 pour 2 points. Garde : si l'écart-type mesuré sur 200 mondes de validation dépasse 18 points, arrêt et nouvelle version (liste d'arrêt).
- Coût : processeur seul, aucune dépense ; temps estimé de quelques heures en Python avec numpy (SUPPOSÉ ; v1 : 93 s pour 4 000 mondes sans noyau sur les paires).

### 9. Ordre d'exécution
Contre-lecture R2 → gel du seuil par Lazar → scellement → écriture du code → tests de gardes (§ liste d'arrêt) → validation du générateur → méthodes sur 200 mondes de validation « moyen » (écart-type ; grille diagnostique) → mondes de décision → lecture par un sous-agent neuf (R13).

### 10. Hors périmètre
- Passage sur les vraies fiches de la course 2 : préenregistrement distinct, lecture **descriptive** (environ 20 paires par bras selon l'avis d'Opus ; 128 à 300 fusions par bras selon la synthèse pour un effet de +10 points), sans sélection sur le verdict (N-053, contenu non lu par l'auteur du brouillon : SUPPOSÉ), précédé d'une mesure de séparabilité sur les paires de fiches réelles. Source des concepts sur fiches réelles (D-e) : décision séparée.
- Aucun appel de modèle, aucune fusion : la précision mesure le tirage, pas les filles (B § 6).

## Critères de lecture gelés

Un sous-agent neuf (ni auteur du présent préenregistrement ni de l'analyse, R13) applique ce tableau tel qu'il est écrit. `θ_abs`, `θ_rel`, δ, δ_non : valeurs gelées avant scellement. « Bornes » : à 95 % sauf mention. « Les deux » = M_bien et M_moyen.

**Conditions de validité (préalables)** : V0 = validation du générateur passée ; aucun arrêt de la liste ; mondes exclus (précision non définie) ≤ 2 %.

**Conditions d'adoption** :
- A1 : les deux, Δ(N, b) ≥ θ_abs, ρ(N, b) ≥ θ_rel, borne basse de Δ > 0 ;
- A2 : les deux, bornes basses de Δ(N, a), Δ(N, d1), Δ(N, d1c) > 0 ;
- A3 : SP, aucun des écarts N − b, N − d1c, N − N_β0 n'a un intervalle à 99 % qui exclut 0 ;
- A4 : borne haute de Δ_INV − Δ_bien < 0 ;
- A5 : non-régression, borne basse de Δ(N, b) ≥ −1 sur NR_bien et NR_moyen (99 %) ;
- A6 : borne haute de Δ_V_fuite − Δ_bien < 0.

| Issue observée | Verdict |
|---|---|
| V0 non tenue | **non concluant** ; aucune lecture des contrastes |
| A1 à A6 toutes tenues | **N adoptée** (volet d'adoption) |
| A1 non tenue : borne haute de Δ(N, b) < θ_abs dans l'une des deux | **N non adoptée** ; si la borne haute est < 0 : N perd contre le stratifié |
| A1 tenue, mais borne haute de Δ(N, d1c) ≤ 0 dans les deux | **« Swanson guidé par concepts suffit »** (issue permise) ; N non adoptée |
| A1 et A2 tenues, A3, A4, A5 ou A6 en défaut | **non concluant** + audit R4 ; jamais adoptée |
| Les deux : bornes basses de Δ(N, N_β0) et Δ(N, N_filtre) ≥ δ > 0, **et** placebo : borne basse de Δ(N, N_PC) > 0 et borne basse (99 %) de Δ(N_PC, N_β0) ≤ 0 (aucun gain démontrable sans l'information conceptuelle) | **« la proximité conceptuelle est l'ingrédient manquant » : oui** |
| Les deux : borne haute de Δ(N, N_β0) < δ_non | **non** : le terme de concept n'apporte rien |
| Les deux : Δ(N, N_β0) ≥ δ (borne basse > 0) **et** borne haute de Δ(N, N_filtre) < δ_non | **non** au sens de la question : le concept **suffit comme filtre** ; son entrée dans l'objectif n'apporte rien de plus |
| Tout autre cas | **indécis** |
| Placebo : gain de N_PC sur N_β0 (borne basse > 0 à 99 %) | artefact : **audit R4**, volets « oui » et « adoptée » suspendus |

Lecture secondaire, sans effet sur le verdict : la valeur du second espace est Δ(N, N_α0) ; la place du déterminant sur les paires est Δ(N_dpp, N_global) et Δ(N_dpp, N) (P11) ; la valeur de q est Δ(N_q, N).

**Audit de symétrie (R4)**, déclenché par un résultat trop propre **ou** trop mauvais : |Δ(N, b ; M_bien)| ≥ 15 points ; précision de N ≥ 0,9 × précision de l'oracle ; N identique au bit près à N_global, N_β0 ou à un témoin ; écart de contrôle (SP, placebo) excluant 0 ; fuite mesurée exactement nulle ; concordance des étiquettes avec la vérité > 0,99 ; perte de N ≥ 10 points contre le stratifié. Contenu : relecture du code par un sous-agent neuf pour vérifier qu'aucune méthode ne lit un champ latent ; relance sur les graines de validation ; test de permutation. Tant que l'audit n'est pas rendu : « non concluant ».

Aucune lecture avant scellement ; rien de ce tableau ne change après lecture ; toute déviation est écrite comme telle (R1). Le verdict est scellé puis soumis à Lazar pour GO (R13).

## Liste d'arrêt

| Condition | Action |
|---|---|
| Validation du générateur ratée (cosinus, fuite, queue, jumelles, rareté, plafond de l'oracle) | arrêt avant toute méthode ; correction par une nouvelle version du préenregistrement (R12) |
| Échec de Cholesky ou noyau non défini positif (N_dpp, N_fiches, a) | arrêt du bras et du run ; jamais de repli silencieux (R5) ; consigné |
| NaN ou division par zéro dans un score ; vecteur de concepts nul non compté | arrêt |
| Plafond de l'oracle < 0,30 en « bien » ou « moyen » | arrêt : monde non jugeable |
| Écart-type apparié de Δ(N, b) > 18 points sur les 200 mondes de validation | arrêt ; nouvelle version avec plus de mondes |
| Écart de contrôle excluant 0 (SP, placebo) | audit R4 ; verdict « non concluant » tant que non rendu |
| Plus de 2 % de mondes à précision non définie | arrêt |
| Reproduction : moyennes de b, a, c, d1 sur NR_bien et NR_moyen hors de l'intervalle de B § 1 élargi de 2 points | arrêt : le code des témoins diffère de v1 |
| Appel de modèle, réseau ou dépense | arrêt (devis et GO exigés) |
| Lecture d'un résultat ou exécution d'une méthode avant scellement ; paramètre modifié après lecture | arrêt et consignation de l'écart (R1) |
| Contre-lecture R2 absente | pas de scellement |
| Empreinte du code différente entre deux sessions d'un même run | arrêt |

**Gardes testées sur un cas sain et sur un artefact (R5)** avant les mondes de décision :
- noyau volontairement non défini positif (`noyau_fautif` de la pièce A) : la décomposition de Cholesky doit lever `NonDefiniePositive` ; cas sain : noyau de la forme corrigée ;
- bras artefact qui lit la vérité (score = indicatrice du vrai pont) : l'instrument doit enregistrer un gain proche du plafond **et** le détecteur de lecture des champs latents doit le signaler ; cas sain : N ne lit aucun champ latent (contrôle statique du code) ;
- vecteur de concepts nul : κ = 0 compté et rapporté ; cas sain : monde jouet à la main à réponse connue ;
- monde jouet dont la précision des 12 paires est calculée à la main (vérification des estimateurs et des intervalles).

## Contre-lecture

- Contre-lecture 1 : **NON FAITE (R2)**. Sous-agent neuf à désigner, qui n'a écrit ni ce brouillon, ni la question, ni les pièces. Empreinte du brouillon à relire et chemin et empreinte de son rapport : `[À SCELLER]`.
- Fichiers à lui donner explicitement : ce brouillon ; `recoupement-bisociation-v1.md` ; la question, l'avis d'Opus, la synthèse ; les pièces de la liste « Documents qui font foi » ; `prereg/gabarit-preregistrement-v1.md` et `src/controle_ia/prereg.py` (sections exigées). Interdits à lui rappeler : ni `donnees/`, ni branche git, ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces`.
- Questions à lui poser en priorité : (1) les concrétisations du nœud 3 de l'en-tête ; (2) la règle « bornes à 99 % pour les contrôles » et son effet sur la puissance ; (3) le plan de validation du générateur (seuils SUPPOSÉS) ; (4) si N lit, même indirectement, un champ latent ; (5) si l'emboîtement opérateur ⊂ concept et la disjonction des concepts par champ créent un avantage par construction pour N ou pour d1c ; (6) le traitement de chaque option du seuil.
- Traitement de chaque remarque (accepté, refusé et pourquoi) : `[À SCELLER]`.
