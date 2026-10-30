# Recoupement — synthèse du collisionneur × avis de l'Opus neuf — bisociation à deux espaces — v1

- **Auteur** : sous-agent neuf, Sonnet 5.5 (`claude-sonnet-5-5`). **Non-auteur** de la question, des pièces A à D, de l'avis d'Opus, de la synthèse et du code du pôle. Relevé `date -u` : 2026-10-30T00:41:30Z (début de rédaction).
- **Lu** (SHA-256 recalculé ; égal aux compagnons `.sha256` pour la question, l'avis et la synthèse, et aux tables de B § 10 et de l'avis d'Opus pour les autres pièces) : question `73a30ab7…` ; avis d'Opus `2331e70f…` ; synthèse `49dd3840…` ; pièce A `recombinaison.py` `71faad38…` ; rapport B `72cff8a0…` ; préenregistrement v1 `5335614b…` ; `monde_v1.py` `af907b1d…` ; `methodes_v1.py` `2f7a8b11…` ; `mesures_v1.py` `0a1e3c38…` ; `conditions_v1.py` `9246ecc6…` ; `trancher_v1.py` `781335dd…` ; lignes R-497 et R-500 de `registres/decisions.md`.
- **Non lu** : les cellules de la synthèse (sous `donnees/`, interdit) — tout « T3-x l. n » ci-dessous est **rapporté par la synthèse** ; pièces C et D ; contenu de N-053 (SUPPOSÉ). Aucun réseau, aucune dépense, rien scellé, aucun fichier existant modifié.
- **Règle de lecture** (critères gelés de la question) : « commun » = au moins deux des trois modèles de la synthèse (A Fable, B Opus, C Gemini ; A et B sont de même famille), même forme mathématique, même rôle de la qualité. L'avis d'Opus est lu à côté : je note « concorde » ; **rien ne devient commun par lui**. Calculs de ma main marqués (M).

## 1. Verdict
1. Synthèse et avis d'Opus **concordent sur le diagnostic** (le volume de fiches n'ordonne pas les paires ; l'attraction conceptuelle ne peut vivre que dans le score d'une paire ; ensemble de base = paires valides ; un exposant est nécessaire). Le **socle commun au sens gelé** reste celui des trois modèles : score de paire produit, qualité retirée, une paire par strate.
2. L'avis d'Opus **diverge sur quatre points** : processus déterminantal sur les paires, qualité conservée, réglage de l'exposant par grille, seuil +5 et ×1,25. Ma lecture (M) : son noyau de répulsion est presque inerte aux cosinus de B, donc sa forme se comporte comme un classement global par score ; elle se teste en ablation, elle ne se retient pas en tête.
3. **Rien n'est préenregistrable tant que Lazar n'a pas gelé le seuil.** Le signe est levé par R-500 (loin en domaine, proche en concept, β positif). Le squelette (B) met la forme commune en candidate et toutes les formes divergentes en ablation.

## 2. Ce qui concorde
| Élément | Synthèse (trois modèles) | Avis d'Opus | Statut |
|---|---|---|---|
| « Minimiser le produit scalaire » est contenu en signe dans le volume, inopérant en force (pénalité 0,6 % à cos 0,28, B § 3) | él. 1 : A, B, C | § 1, même chiffre ; aire² = 1 − cos², exposant requis | **commun** ; Opus concorde |
| Ensemble de base = paires valides ; hors diagonale, toute similarité repousse ; la proximité conceptuelle n'entre que dans le score d'une paire | él. 2 | § 1 : un processus déterminantal « ne sait que repousser » (Kulesza et Taskar 2012, de mémoire, R7) | **commun** ; Opus concorde, formulation plus forte |
| Facteur de domaine (1 − cos²)^e | D3 : B et C coïncident (exposant ≈ 17 sur (1 − d²)^(·/2), « convergence non relevée par eux », § 4 de la synthèse) ; A règle par calibrage | (1 − cos²)^α, α ∈ {1, 2, 4, 8} | **forme commune** (B, C) ; réglage divergent (D-d). Équivalence (M) : « une paire à cos 0,28 pèse la moitié » donne e = 8,49 ; α = 8 d'Opus donne 0,52 |
| Une pondération de rareté sur le facteur de concept | D2 : A (rareté lissée, corpus hors vivier), B ((ε + C)^α, ε = 0,05) | (κ + ε)^β, cosinus pondéré par la rareté, ε = 10⁻³ | **divergent** au sens gelé (D2) ; Opus ≈ B |
| Réglages jamais sur les mondes de décision | él. 8 | grille sur 200 mondes de validation | concorde |
| Séparabilité mesurée, jumelles à vocabulaire de domaine substitué | él. 6-7 : sur les **paires**, en excès sur l'oracle latent | (i)-(iv) sur des **fiches**, sans oracle | concorde sur l'esprit ; objet différent |
| b_eloigne et Swanson parmi les témoins | él. 9 | b_eloigne en diagnostic ; d1 et d1c en témoins | concorde ; statut de b_eloigne à fixer |
| Course 2 non jugeable au budget d'une course | él. 10 (128 à 300 fusions par bras) | environ 20 paires par bras, erreur type 0,11 | concorde : lecture descriptive |
| Zone vierge = question (R8) | confiance 0,3 que la zone soit vierge | « revendiquer seulement la forme » | concorde ; candidats à vérifier d'abord : Gentner 1983, Hope et collaborateurs 2017, Berthold 2012 (de mémoire) ; Opus ajoute Gillenwater, Kulesza, Taskar 2012 (ensemble de base de chaînes) |
| Signe | él. 12 : les trois relèvent la contradiction | demande confirmation | **levé par R-500** ; D5 et Q1 de la synthèse sans objet, bras symétrique de C inutile |

## 3. Divergences (format décision ; « proposer avec recommandation », défaut 48 h sauf D-f)
**D-a — Qualité q dans le candidat.** Enjeu : q est indépendante de la vérité dans `monde_v1` (B § 3) ; elle ajoute du bruit au candidat.
- (1) q ≡ 1, q en ablation (A, B, C). Avantage : aucun bruit ; retirer q vaut +0,8 point en « bien », +0,1 en « moyen » pour la forme corrigée (B § 1 : −4,0 contre −4,8 ; −2,1 contre −2,2). Inconvénient : ne dit rien d'un pôle où q porte du signal.
- (2) q gardée (Opus, ablation N_q1). Avantage : proche du pôle. Inconvénient : handicape le candidat par construction.
- Recommandation (1), confiance 0,75. Défaut : (1).

**D-b — Règle de sélection.** Enjeu : le déterminant sur les paires ne repousse presque rien à ces cosinus.
- (1) Meilleure paire par strate, sans déterminant (A, B). (2) Déterminant sur les paires, noyau de Schur (C ; Opus). (3) Les deux, niveaux d'un factoriel (Q2 (c) de la synthèse).
- (M) Avec le noyau de l'avis : deux paires de la même strate se repoussent à ≈ 0,29 (cosinus intra-domaine 0,54, B § 5), soit 8,5 % du déterminant ; deux paires de strates différentes à ≈ 0 ; deux paires qui partagent un article et dont les partenaires sont de domaines éloignés différents à ≈ 0,03. Face à une qualité qui varie d'un facteur 10 à 100 (κ de 0,1 à 1, β de 1 à 2, M), le glouton classe presque par score : il perd l'équilibre des strates qui fait gagner le stratifié (B § 3). Il ne décourage pas non plus de réutiliser un même article. Inférence, à mesurer par l'ablation « classement global » contre « déterminant ».
- Recommandation (3), confiance 0,7. Défaut : (3). Opus (2) et C en ablation.

**D-c — Facteur de concept.** Enjeu : ε décide si le concept est un facteur ou un filtre de fait.
- (1) Cosinus pondéré par la rareté, (κ + ε)^β, ε = 0,05, β = 1 (B). Avantage : les paires à étiquette d'opérateur seule gardent un poids non nul. (2) Opus : ε = 10⁻³, β ∈ {0,5 à 4}. Inconvénient (M) : avec un étage commun « opérateur **ou** concept », une paire sans concept partagé pèse ε^β = 10⁻⁶ à β = 2 ; le candidat devient un filtre de fait et le contraste N − N_filtre ne mesure plus que la pondération interne. (3) Rareté de l'étiquette partagée la plus rare (C), en ablation.
- Recommandation (1), confiance 0,5. Défaut : (1).

**D-d — Réglage des exposants.** Enjeu : le candidat réglé sur une grille, les témoins non, serait avantagé.
- (1) A priori : e = 8,5 (« une paire proche pèse la moitié », B et C), β = 1, ε = 0,05. (2) Grille de 16 cases sur 200 mondes de validation « moyen » (Opus). (3) Calibrage sur graines de calibrage (A). C dit « a priori » (T3-C l. 42) puis « calibré » (l. 79).
- Recommandation (1) pour l'adoption, grille en diagnostic non éligible sur graines distinctes ; confiance 0,6. Défaut : (1).

**D-e — Source des concepts sur vraies fiches** (hors test synthétique, où le canal est paramétré).
- (1) Déclaration sur liste fermée, ancrée et vérifiée par programme (A, C). (2) Étiqueteur tiers hors boucle, scellé avant tirage (B). (3) Règle « deux sources sur trois » (Opus) : robuste à la manipulation, mais appel de modèle à chaque génération (devis) et non testable sur mondes synthétiques (une seule chaîne d'observation).
- Recommandation (1) comme mécanisme, (2) et (3) comme mesure seulement ; confiance 0,6. Défaut : (1). Champ « concepts mobilisés » au gabarit : R-497 (a), défaut après la v48.

**D-f — Seuil d'adoption. À GELER PAR LAZAR : aucun défaut appliqué (seuil de préenregistrement).** Enjeu : +12 est hors d'atteinte ; un seuil trop bas laisse passer l'éloignement seul.
- (a) +12 absolu (question, Argon, v1). Critiqué par les trois ; b_eloigne seul ne l'atteint pas (+11,9 et +6,6, B § 1). (M) Sur b = 0,203 et 0,127 (B § 1) : ×1,59 et ×1,94.
- (b) Opus : ≥ +5 points **et** ×1,25, borne basse > 0.
  - (M) Sur les chiffres de v1 : plancher efficace +5,1 en « bien » (le rapport) et +5 en « moyen » (×1,39).
  - Inconvénient : b_eloigne (+11,9 ; +6,6) le franchit sans aucun concept ; il faut le coupler à N − N_β0 ≥ δ.
- (c) Synthèse (A) : ×1,3 et ≥ b_eloigne-observé − 2.
  - (M) +6,1 et +3,8 ; +9,9 et +4,6 sur les chiffres de v1.
  - Avantage : teste le concept, non l'éloignement seul. Inconvénient : dépend d'un témoin lui-même incertain en monde v2.
- Recommandation : (b) comme plancher, plus le contraste de détection N − N_β0 et N − N_filtre ≥ δ (Opus ; B de la synthèse) ;
  b_eloigne-observé en témoin, sans seuil de supériorité. Confiance 0,5. Défaut : **aucun**.

**D-g — Nombre de mondes.** 400 (C), 600 (Opus), 1 200 (B), 400 + 100 (A).
- (M) Écart-type apparié 15,3 points (demi-largeur 1,5 à 400 mondes, B § 1). Puissance 0,8, α = 0,05 : 3 points → 204 mondes (290 avec quatre contrastes) ; 2 points → 460 (653). À 1 200 : plus petit effet détectable 1,24 point (1,48 corrigé). Opus retrouve 204 et 290.
- Recommandation : 1 200 en « bien » et « moyen », 600 pour les contrôles ; processeur seul ; confiance 0,6. Défaut : idem.

## 4. Juge dans la boucle / non préenregistrable
| Élément | Classement | Raison |
|---|---|---|
| Déclaration par le proposeur (R1) | mécanisme possible | aucun juge ; manipulable ; vérifiée par programme (R3) |
| Étiqueteur tiers scellé avant tirage (R2) | étiquetage hors boucle, admis | « juge dans la boucle » seulement s'il note les paires ; rescellé à chaque génération = appel de modèle, donc devis |
| Règle « deux sources sur trois » | mécanisme, **non testable** en synthétique | une seule chaîne d'observation par monde |
| Liste fermée de 36 concepts | proposition | écrite de mémoire (Opus) ; figée par version (R12) |
| Séparabilité (i) à (iv) sur 60 fiches | **non préenregistrable en l'état** | seuils SUPPOSÉS (10 points, 0,8, 0,3, kappa 0,6), annotateurs non nommés, sans oracle latent ; (ii) exige une réécriture par modèle |
| Test d'Opus sur mondes à deux espaces | **non préenregistrable en l'état** | témoins complets (stratifié, v6.3, Swanson) mais seuil non gelé ; préenregistrable dès le gel (D-f) |
| Passage sur vraies fiches | descriptif, hors décision | environ 20 paires par bras ; N-053 non lu (SUPPOSÉ) |

## 5. Réserves de lecture sur l'avis d'Opus (vérifiables)
- Sa règle (3) (« aucun écart dont l'intervalle exclut 0 ») sur plusieurs écarts à 95 % fausse l'alarme : (M) quatre écarts indépendants donnent 18,5 %. Le squelette met 99 %.
- Sa règle (6) compare deux estimations sans intervalle ; son hypothèse annonce « nul ou positif contre d1c » alors que la règle (2) exige une borne basse > 0.
- Sa non-régression (5) fait tourner N sur des mondes v1 qui n'ont aucun concept ; le squelette pose concept := étiquette d'opérateur, dit explicitement.
- Son placebo reste le monde sans pont de B ; la synthèse y ajoute la permutation de concepts qui conserve fréquences et paires valides (él. 5) : le squelette la reprend, sans modifier l'étage commun.
- Mesure ajoutée : nombre d'articles distincts parmi les 12 paires (réutilisation d'un article, non pénalisée par son noyau).
- Coût du noyau sur les paires : Opus suppose « quelques centaines » de paires valides et un noyau 400 fois plus lourd. (M) La précision placebo de 0,138 du tirage uniforme sur 6 paires (B § 2.1) implique environ 43 paires valides en v1 « bien » : le coût y est négligeable ; à remesurer en v2.
- Réserve sur la synthèse : elle n'a pas vu l'avis d'Opus ; ses cellules A et B sont de même famille.

## 6. Tranché en routine dans le squelette (B), sans nœud
- Contrôle inversé : monde « vérité inversée » d'Opus (ponts entre domaines proches, concept toujours partagé), lu par Δ_INV − Δ_bien (B § 7.2).
- Ponts de surface et homonymes **rares** à rareté appariée (A, C) ; les « concepts inversés sur moyeux » de C sont écartés : ils confondent concept et rareté (§ 4 de la synthèse).
- Placebo de concepts : permutation, dans chaque domaine observé, des vecteurs de concepts **utilisés pour classer ou tirer** ; l'étage commun garde les vraies étiquettes.
- Graines par `SeedSequence` (R9), à la place des `random.Random` entiers de v1 ; intervalles à 99 % pour les contrôles.
- Dénominateur de la précision fixé à 12 : une abstention compte comme un échec (aucune sélection par la sortie d'un bras, R4).

## 7. Décisions pour Lazar (une ligne chacune ; le détail est en § 3)
1. **D-f seuil d'adoption : à geler par toi, aucun défaut** — recommandation (b) + contrastes de détection, confiance 0,5.
2. D-b forme en tête : (3) factoriel « par strate » et « déterminant sur paires » — défaut 48 h : (3).
3. D-a qualité q ≡ 1 dans le candidat — défaut 48 h : (1).
4. D-d exposants a priori (e = 8,5 ; β = 1 ; ε = 0,05), grille en diagnostic — défaut 48 h : (1).
5. D-g 1 200 mondes de décision, 600 par contrôle (processeur seul, aucune dépense) — défaut 48 h : idem.
6. D-c et D-e (facteur de concept ; source des concepts sur vraies fiches) — défauts 48 h : (1) et (1) ; le champ « concepts mobilisés » suit R-497 (a).
