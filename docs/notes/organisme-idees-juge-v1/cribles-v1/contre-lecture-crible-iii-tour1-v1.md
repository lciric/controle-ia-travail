# Contre-lecture du préenregistrement du crible (iii), brouillon 1 — tour 1 — v1

- Contre-lecteur : sous-agent neuf, **modèle C** (identité dite en conversation seulement) ; auteur de la pièce : modèle A ; je n'ai écrit
  aucune pièce citée. Un premier contre-lecteur (modèle B) s'est arrêté sans rapport : je n'ai lu ni ses dossiers ni rien de lui.
- Date (UTC) : Mon Nov 16 13:23:47 UTC 2026 (`date -u`), lecture entière de la pièce, tour 1.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon1.md`, empreinte entière
  `00c92559d54349101dfcc0c59afe402c388b192c32fa6018bbf809eb02f22af0` (vérifiée par `sha256sum`, égale à son compagnon et à R-2977).
- Pièces lues : la pièce en entier ; la note des idées originales (`2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3`, § 0 à 7,
  annexe A) ; la ligne R-2977 et les lignes « crible » de `registres/decisions.md` (par `grep`) ; la ligne GO-2026-11-15-06 de `registres/go.md` ;
  N-058 (`854f2724…`) et N-045 v2 (`c7b05e39…`) en entier ; la procédure v14 du pilote au commit `2d35cafa…`
  (`2035562740efe1e87db9ffa2f0494705bb5117c56069309ece2279d351bde18a`, `git show`, après `git fetch` de la seule branche
  `lot/compte-organisme-v1`) ; le texte scellé du pilote, candidat 6 (`8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`,
  `git show` de la branche locale `origin/prep/pilote-mr2-compte-organisme-v1`, sans fetch), pour son bloc gelé et son devis ; le gabarit,
  `prereg.py`, les deux préenregistrements scellés modèles (empreintes vérifiées) ; le générateur `monde_riche_v4.py` (permutation des traits) ; la section
  « Métrique » de `crible-v-brouillon1.md` (pour ses prix publics). **Non lu** : tout ce que la consigne interdit.

## Verdict

**corrections.** La conception tient (question, quatre bras, filtre, statistiques, devis arithmétiquement exact) ; elle ne peut pas être
scellée telle quelle : **11 corrections majeures** (durée et parallélisme non fixés, nombre de mondes et minimum non reliés à la règle du pilote,
règle de mise à jour d'après le pilote absente, décisions de R-2977 non reportées, lecture du prix promotionnel, tronquage de B, forme à fixer) et
**15 mineures**. Aucun appel, aucune dépense, aucune machine, rien lu des zones interdites.

## Réponses aux neuf points

**(1) R1.** Hypothèse, prédictions chiffrées avec signe, métrique, seuils, plan d'analyse, critères gelés, liste d'arrêt : présents, d'une forme
qui suit les deux modèles scellés. Portes de sortie après lecture : (a) « à confirmer par la mère » pour l'ablation (C-08) ; (b) nombre de mondes laissé à
« 24 ou 30 si la mère le décide » (C-04, C-20) ; (c) prédictions « refaites sur les taux mesurés » du pilote, sans table de ce qui change (C-06, C-07) ;
(d) sensibilités « sans verdict » : le lecteur pourrait citer après coup celle qui l'arrange (C-10) ; (e) minuterie « durée bornée » non définie (C-01 à C-03) ;
(f) relevé de sonde « si le lanceur l'exige » (C-25).

**(2) R3.** *Statistique principale.* Δ_R = R_D − R_S est justifiée avant toute donnée (toujours définie ; même signe que ρ_DS quand
R_S > 0) : acceptée. Elle est mécaniquement négative si D couvre autant que S, puisque D coûte plus (III-7 > 1) : c'est le sens de « par dollar », la pièce
le dit à demi ; je ne demande rien. *Marge de 0,5 composante par monde* : avouée comme choix du texte et chiffrée (10 à 17 % de 3 à 5 composantes,
exact) ; acceptable ; **mais** à 20 mondes la puissance de P2 à l'effet que l'auteur prédit (+ 0,5) est d'environ 0,35 à 0,50 (mon compte, approximation
normale, écart-type par monde supposé 1,0 à 1,2, bornes à 97,5 %) : « non tranché » est l'issue la plus probable même si III-2 est vraie ; la pièce ne le dit pas
(C-19) ; l'intervalle par percentile sur 20 mondes à comptes entiers n'a pas de taux d'erreur vérifié (C-14). *Égalités par l'ordre des noms* : le
générateur permute les traits dans chaque monde (`rng.permutation(D)`, lu), donc l'ordre lexicographique ne favorise aucun trait informatif :
justifié ; mais parmi les ensembles à distance 1 (fréquents avec 8 traits), le filtre prend les premiers dans l'ordre, non ceux que préfère Pr-1, de sorte que
le choix de Pr-1 n'entre que par la liste de vingt : la pièce le dit (« Écarts »), je demande de le reporter au point de décision (C-24). *Bras « tout bon marché »
qui réemploie la passe 1* : comparables sans fuite, car le texte servi de B est égal à l'octet à celui de D (ligne d'arrêt et essai), B est une session neuve, la réponse brute de la
passe 1 ne passe jamais ; la dépendance entre B et D est avouée ; le coût de la passe 1 est compté dans les deux bras. **Réserve réelle, non vue par la pièce** :
la borne de sortie de Pr-1 est de 36 000 jetons pour six cartes à environ 30 000 attendus, celle de Pr-2 de 89 000 ; un B tronqué ne couvre rien, et P2 lirait alors la borne,
non la capacité (C-11, C-07, C-17). *Puissance avec 3 à 5 composantes* : voir C-19 et C-14.

**(3) Forme du crible et crédits de Claude.** *Recommandation nette pour la mère : la variante (Pr-2 choisit, Pr-4 écrit), confiance 0,6.* Raisons :
1. Avec les prix **que la pièce elle-même prend en principal** (prix publics, note v2, lus dans [CRIBLE-V] « Métrique » : Pr-1 2 / 10 jusqu'au 30 novembre, Pr-2 4 / 20,
   Pr-4 8 / 40), l'écart de prix par jeton est **2 dans les deux formes** (Pr-2 contre Pr-1 ; Pr-4 contre Pr-2). L'argument de l'auteur (« écart 3,2 = le contraste
   visé », Choix 4) vient du devis attendu de la note (0,25 contre 0,80) et contredit sa propre fourchette : appel d'écriture de Pr-1 à 0,35 à 0,45
   contre 0,66 à 0,82 pour Pr-2, soit ≈ 2.
2. Au prix de la configuration (sensibilité), Pr-1 (10 / 50) est **plus cher** que Pr-2 (4 / 20) : la forme fidèle perd son contraste, B devient le bras le plus
   cher ; l'écart Pr-4 / Pr-2 reste 2 aux deux barèmes. Le « bon marché » de Pr-1 repose sur un barème promotionnel qui s'arrête le 30 novembre, date de fin des lignes de GO.
3. Crédits de Claude : 125,30 sur 128,30 attendus (98 %) contre 48 sur 58,30 (82 %) ; pire cas hors crédits : 3 contre 96,60. C'est la consigne permanente de Lazar (GO-2026-11-15-06).
4. Prix : + 70 USD attendus (128,30 contre 58,30), pire cas 263 contre 216,60 (24 mondes : environ 315 contre 259), dans l'enveloppe (avec (v) : 196,60 + 263 = 459,60 sur 1 275).
   **À vérifier par la mère** : que le solde de crédits de Claude couvre 263 USD au pire en plus des autres usages (je ne le lis pas).
**Ce que la variante change, dit nettement** : elle ne change pas la structure de la question (le palier moins cher choisit les traits, le plus cher écrit, comparés à un appel du plus cher seul,
par dollar ; ablation = le moins cher écrit) ni le rapport de prix. Elle change **qui** est « bon marché » : deux modèles d'une même maison au lieu de deux maisons ; la lecture de
« la frontière est-elle nécessaire » (QO1) devient « le palier supérieur de la même maison est-il nécessaire », sans rien dire d'un modèle d'une autre maison ni d'un instrument local
(N-045 : Pr-1 reste de toute façon une espèce de frontière) ; un risque de convergence des deux modèles d'une même maison (D proche de H) sans effet sur la validité. La forme fidèle
reste la seule à mesurer un proposeur d'une autre maison ; si la mère la veut, à proposer à part, plus tard, sur un devis propre.
Choisir la variante oblige à **réécrire** : table des proposeurs, rôles, III-1, III-2, III-5, III-7, devis, lignes de GO, sonde (voir « Si la variante est retenue »).
La pièce chiffre déjà la variante (128,30 ; 263 : **recomptés par moi, exacts** : 60 × 1,60 + 40 × 0,80 + 0,30 ; 60 × 3 + 40 × 2 + 3).

**(4) Devis (recompté).** 100 appels = 5 par monde × 20 ; Pr-2 60 (S, D, H), Pr-1 40 (passe 1, B). Plafonds de session du bloc gelé relus : `argon` 2,34 (borne 36 000, part 9,36
au pilote), `astra` 2,34, `opus55` 2,00 (89 000), `fable52` 3,00 (64 000) : la pièce dit juste (« 2,34 pour deux proposeurs »). Attendu 48,00 + 10,00 + 0,30 = 58,30 ✓ ; pire 120,00 + 93,60 + 3,00 =
216,60 ✓ ; passage de [NOTE] : 243 − 40 + 13,60 ✓ ; fourchette 48,1 à 61,8 ✓ (recalcul aux prix 4/20 et 2/10) ; Pr-1 au code (cinq fois) 5 à 14 et 34 à 42 ✓. Sonde : 3 appels, plafonds 2,00 + 2,34 + 2,34 = 6,68 ✓, attendu
1,05 à 1,40 ✓ ; sonde des relais : 8,07 est celle du pilote (8,052896, lignes de GO), 0,10 attendu ✓. Parties de GO : 120 (60 × 2,00) et 93,60 + 3 (40 × 2,34 + machine) ✓. Cohérence avec GO-2026-11-15-06 :
chaque crible sous sa ligne « calcul », devis refait et contre-lu, essayé non adopté : respectée (« Lignes de GO proposées »). **Incohérences** : aucune d'arithmétique ; mais l'attendu hors crédits 10,30 est au prix public,
alors que le code compte Pr-1 à 10 / 50 : la dépense **comptée** attendue hors crédits est de 39 à 56 (sous la part de 93,60, donc sans arrêt) : à dire en une ligne (C-10, C-21). À 24 mondes (forme fidèle) : environ 70 attendus, 259 au pire.

**(5) Durée.** La pièce chiffre 12 à 15 h attendues, dit « trop près de la minuterie de 17 h » et laisse le choix (« deux mondes au moins en parallèle, ou une minuterie plus longue ») ; elle ne dit pas le pire cas
(60 h, 3 h par monde, [PROC-14] : `4 × 10 800 s`), ni de borne par monde, et la ligne d'arrêt « durée bornée des appels » n'est pas définie. Or 12 à 15 h dépassent déjà la garde de départ
de 12 h 30 de [PROC-14] : **la série est impossible, pas seulement « trop près »**. Il faut des mondes en parallèle, **fixés dans le texte** (C-01 à C-03) : proposition de ce contre-lecteur, 5 files de 4 mondes (6 pour 24),
borne par appel 3 000 s, par monde 7 200 s (deux tours), pire cas d'une file 8 h, garde de départ 10 h. *Faisable avec le code du pilote ?* **Non, pas tel quel** : le lanceur v74 joue 4 mondes l'un après l'autre,
un appel par relais et par monde, sans second tour dépendant ni filtre ni files parallèles, et sa mesure ne rend pas la couverture par appel ; il faut un lanceur, des gabarits G1 et G2, un filtre, une mesure et une procédure de machine **neufs**
(la pièce le suppose à l'étape 0 sans le dire) ; la concurrence des relais (jusqu'à 10 sessions de Pr-2 en même temps) n'est pas éprouvée par le pilote : essai à blanc à cinq files exigé (C-02).

**(6) Liste d'arrêt, R5, graines.** Chaque ligne a son essai sain et son artefact ✓ (R5) ; graines par `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, clés `(r, 40)`, `(12, r, t)`, `(99, b)`, `(97, k)` : sans collision (r ≤ 23) ✓.
Défauts : minuterie (C-03) ; ligne « 16 mondes complets » liée à un « fournisseur abandonné », alors que le minimum se perd par n'importe quelle cause (C-05) ; relevé « si le lanceur l'exige » (C-25). *Minimum de 16 sur 20* : règle présente,
**non justifiée et fragile** : un monde complet exige cinq appels répondus ; au taux de 0,95 par appel, P(n_c ≥ 16) = 0,52 à 20 mondes (0,93 à 24) ; 0,86 à p = 0,97 ; 0,23 à p = 0,93 (C-04, qui reprend la décision de R-2977 : 24 mondes si le taux est
sous 0,95, et garde le minimum 16 pour N = 24). **Point pour la mère** : avec 16 appels au pilote, un seul échec fait passer le taux sous 0,95 ; un taux observé de 16 sur 16 n'exclut pas 0,95 : toujours 24 mondes coûterait + 20 % et lèverait l'incertitude.

**(7) Ablation de la frontière aux critères gelés.** Bien définie (B = Pr-1 écrit sur les mêmes ensembles, même G2 à l'octet ; étage 5 ; qualificatif « petite ») ; ne contredit pas N-045 point 3 hors du crible : ce point vise « les lectures » des
courses, et la mère l'a mise aux critères du crible (R-2977) parce que c'est la question même. La pièce garde « à confirmer par la mère » : à remplacer par la décision et par la phrase de portée (C-08) ; à dire à Lazar avec le nœud d'adoption.
Réserve de lecture : le tronquage de B (C-11).

**(8) R7, R8.** Aucun chiffre de l'état de l'art : les cinq pistes d'antériorité (LLM-Select, LLM-SR, FunSearch, AlphaEvolve, sélection la plus éloignée d'abord, CADS) sont « à vérifier », sans chiffre ni date opposable
(la pièce ne cite des dates qu'entre parenthèses « par exemple », non opposables) ; la zone « filtre déterministe sans juge » est marquée « séduisante, à vérifier plus durement » ✓ (R8) ; le recoupement V3 et C2 est cité comme voisin ✓ ; « Aucune revendication n'est faite ici ». Rien à corriger.

**(9) Validateur, identifiants, empreintes.** `controle_ia.prereg.problemes` rejoué : **un seul défaut**, « section Contre-lecture sans les deux empreintes exigées (brouillon relu et rapport) », comme attendu ; il disparaîtra avec la section « Contre-lecture »
remplie (empreinte entière de ce brouillon, de ce rapport). Identifiants de modèle : aucun nom de modèle ; les clés de configuration `argon`, `opus55`, `fable52` (qui se lisent comme des modèles) sont exigées par le bloc gelé et les lignes
de GO (R-2690) ; la phrase « aucun identifiant de modèle ici » est inexacte à la lettre (C-12). Empreintes citées, **toutes vérifiées par `sha256sum`** : note, relevé, recoupement, conceptions v3 et v4, résumé v4, outils (quatre), N-044, N-058, N-045, N-067, question, catalogue, deux
préenregistrements modèles, gabarit, `prereg.py`, devis du pilote, les quatre PDF cités, `registres/go.md` au commit `377a2a0c` (`4bcec4a0…`), procédure v14, candidat 6, note des prix v2 (`b88253b8…`) : **conformes**. Annexe A : le code du programme 1 recopié dans la pièce a l'empreinte
`f06bcfe7…` et sa sortie, rejouée (bibliothèque standard, quelques millisecondes), est **identique** à la sortie recopiée (`5d53092e…`) ; le code du programme 2 a l'empreinte `8c0432df…` (non rejoué : il lit des sorties scellées de [MR2]) ; les comptes à la main
des points 7 et 8 (0,4524 ; 0,6131 ; 0,2538) sont exacts. Non vérifiable par moi : fiches `argon-p1-04` et `argon-p2-04` (sous `runs/`, interdit), le programme 2 sur ses entrées.

## Corrections exigées : ancien → nouveau

Chaque « ancien » figure **une seule fois** dans la pièce (vérifié par programme). Majeures : C-01 à C-08, C-10, C-11, C-13 (11). Mineures : les 15 autres. Les chiffres de C-01 à C-03 sont des
propositions du contre-lecteur : l'auteur peut en prendre d'autres, mais il doit **en fixer** (R1).

### C-01 (majeur)

Ancien :

````
9. **Durée** : passe 1 puis passe 2 dans chaque monde : ≈ 12 à 15 h de machine si les mondes passent l'un après l'autre, trop près
   de la minuterie de 17 h : mondes en parallèle à prévoir.
````

Nouveau :

````
9. **Durée** : 20 mondes l'un après l'autre = ≈ 12 à 15 h attendues, 60 h au pire (3 h par monde, [PROC-14]) : **impossible** sous la
   minuterie de 17 h et la garde de départ de 12 h 30. **Fixé ici** : 5 files de 4 mondes en parallèle (6 files de 4 pour 24 mondes) ;
   borne par appel 3 000 s, borne par monde 7 200 s (deux tours : S, H et passe 1, puis D et B) ; pire cas d'une file 4 × 7 200 s = 8 h ;
   garde de départ : pire cas des files + 2 h (mesure, rapatriement, poussée) avant l'échéance. Le code du pilote ne sert pas tel quel :
   lanceur, gabarits G1 et G2, filtre, ordre à deux tours, files parallèles et mesure sont neufs.
````

### C-02 (majeur)

Ancien :

````
départ du réel) : **deux mondes au moins en parallèle**, ou une minuterie plus longue (procédure neuve) ; concurrence des relais
  (plusieurs sessions de Pr-2 à la fois) non éprouvée.
````

Nouveau :

````
départ du réel) : **cinq files de quatre mondes** (point 9 de la section 0), jamais une minuterie plus longue ; à cinq files, jusqu'à
  10 sessions de Pr-2 et 10 de Pr-1 en même temps : **essai à blanc à cinq files** avec relais scriptés ; si le débit des relais
  refuse la concurrence (erreurs de limite de débit à l'essai à blanc), arrêt avant tout appel et nœud de la mère (procédure neuve) ; jamais de repli
  silencieux ni de reprise d'appel.
````

### C-03 (majeur)

Ancien :

````
| minuterie : moins de la durée bornée des appels restante avant l'échéance | arrêt (A) sans appel | marge suffisante | échéance proche simulée : arrêt |
````

Nouveau :

````
| minuterie : moins du pire cas des files restantes (4 × 7 200 s) + 2 h avant l'échéance, au départ ; ensuite, à chaque monde, moins de 7 200 s + 2 h | arrêt (A) sans nouvel appel ; mondes commencés finis, les autres non commencés | marge suffisante | échéance proche simulée : arrêt |
| un monde dépasse sa borne de 7 200 s, ou un appel sa borne de 3 000 s | appel coupé, compté « en échec » ; monde non complet ; les autres files continuent | monde de 40 min | appel scripté de 3 100 s : coupé |
| erreurs de limite de débit sur plus de 5 % des appels d'un fournisseur | arrêt (A) ; nœud de la mère, aucun repli silencieux | aucune erreur | 10 % d'erreurs scriptées : arrêt |
````

### C-04 (majeur)

Ancien :

````
- **Minimum** : n_c ≥ 16 mondes complets sur 20, aucun fournisseur perdu en entier ; sinon « non concluant ».
````

Nouveau :

````
- **Nombre de mondes N** (décision de la mère, R-2977, règle écrite d'avance) : **N = 24** si le taux de réussite par appel du pilote MR-2 v14 est
  **sous 0,95**, N = 20 sinon ; taux = appels répondus (définition de [PILOTE]) sur appels faits, des deux relais employés ici, calculé par
  le programme de mesure du pilote sur sa sortie scellée par un lecteur neuf, avant le scellement de ce texte, et recopié ici.
  **Minimum** : n_c ≥ 16 mondes complets **quel que soit N** (le test des signes à n = 16 exige 13 accords, annexe A, point 2), aucun fournisseur
  perdu en entier ; sinon « non concluant ». Probabilité d'atteindre le minimum (monde complet = cinq appels répondus, taux p par appel,
  indépendance supposée) : p = 0,95 : 0,52 à N = 20 et 0,93 à N = 24 ; p = 0,97 : 0,86 et 1,00 ; p = 0,93 : 0,23 et 0,71 ; p = 0,90 : 0,04 et 0,29.
````

### C-05 (majeur)

Ancien :

````
| fournisseur abandonné alors que 16 mondes complets ne sont plus possibles | arrêt du crible ; « non concluant » | panne d'un appel : continue | panne de Pr-1 à tous les appels dès le monde 3 : arrêt |
````

Nouveau :

````
| mondes complets obtenus + mondes non commencés < 16, **quelle qu'en soit la cause** (fournisseur, tronquage, coupure, minuterie) | arrêt du crible ; « non concluant » ; dépense restante épargnée | panne d'un appel : continue | pannes de Pr-1 à tous les appels dès le monde 3 : arrêt ; cinq mondes incomplets sur 20 d'emblée : arrêt |
````

### C-06 (majeur)

Ancien :

````
la version qui fera foi les refera sur ses coûts et taux mesurés, en déclarant ce qui en a
été lu.
````

Nouveau :

````
la version qui fera foi ne refait **que** ce que la table « Règle de mise à jour d'après le pilote » (section « Devis ») liste ; les prédictions
III-1 à III-6 restent **celles de ce texte**, III-6 comprise même si le pilote mesure une première conditionnelle trouvée avant sa condition
(à confirmer par la mère) ; seule III-7 se refait ; ce qui en a été lu est déclaré.
````

### C-07 (majeur)

Ancien :

````
**Points à remesurer d'après le coût réel du pilote MR-2** : ceux de [CRIBLE-V] (jetons, dollars aux deux prix, durées, taux de
````

Nouveau :

````
**Règle de mise à jour d'après le pilote** (écrite d'avance ; le pilote ne mesure pas la couverture par appel) :

| chiffre de ce devis | lu dans le pilote | nouvelle valeur |
|---|---|---|
| N (20 ou 24) et minimum | taux de réussite par appel, relais employés ici | N = 24 si taux < 0,95 (section « Seuil ») ; minimum 16 |
| attendu par appel de Pr-1 et de Pr-2 (0,25 ; 0,80) | dollars réels par appel au prix public, par relais | moyenne arithmétique par relais ; fourchette = plus petit et plus grand appel du pilote ; **pire cas inchangé** (plafonds) |
| sortie de Pr-1 pour six cartes (30 000 jetons attendus) et tronquage à 36 000 | jetons de sortie et de réflexion de Pr-1 | si le plus grand appel de Pr-1 du pilote dépasse 30 000 jetons : réserve « B tronqué » à l'avance (étage 2) et sonde obligatoire |
| machine (0,30 attendu) | prix horaire relu et durée réelle d'un monde | durée par monde × cinq files ; borne de 7 200 s inchangée |
| durée par monde (30 à 40 min) | durée mesurée des mondes du pilote | durée attendue mise à jour ; **bornes de 3 000 s et 7 200 s inchangées** |
| lignes de GO (montants) | N et attendus ci-dessus | montants = N/20 × ceux de ce texte pour les appels ; plafonds par appel inchangés |

Tout autre chiffre reste celui de ce texte. **Points à remesurer d'après le coût réel du pilote MR-2** : ceux de [CRIBLE-V] (jetons, dollars aux deux prix, durées, taux de
````

### C-08 (majeur)

Ancien :

````
- **N-045 point 3** : l'ablation (B) est ici aux critères gelés (étage 5), non « rapportée hors des critères » comme dans une course ;
  à confirmer par la mère. **N-045 point 7** : H sépare l'effet du format de celui du choix.
````

Nouveau :

````
- **N-045 point 3** : l'ablation (B) est ici aux critères gelés (étage 5), **par décision de la mère (R-2977)**, parce que c'est la question même
  du crible (QO1) ; N-045 point 3 vise les lectures **des courses** (ablation « rapportée, hors des critères gelés ») : il reste vrai pour elles et
  n'est pas modifié ; aucune course n'hérite de ce choix. À dire à Lazar avec le nœud d'adoption. **N-045 point 7** : H sépare l'effet du format
  de celui du choix.
````

### C-09 (mineur)

Ancien :

````
  (Variante « témoin commun » avec (v) : mêmes mondes et appels S pris à (v) ; section « Choix et doutes », point 7.)
````

Nouveau :

````
  (Mondes **séparés** de ceux de (v), décision de la mère, R-2977 : pas de témoin commun ; la ligne « Témoin commun » du devis est une information
  écartée.)
````

### C-10 (majeur)

Ancien :

````
| 4 | P1 | « deux passes plus efficaces par dollar » / « moins efficaces » / « non tranché » |
````

Nouveau :

````
| 4 | P1 | « deux passes plus efficaces par dollar » / « moins efficaces » / « non tranché » ; **qualifié « dépend du barème »** si le verdict de P1 (même règle, 97,5 %) calculé aux prix de la configuration (Pr-1 à 10 / 50) n'est pas le même qu'aux prix publics ; le barème public de Pr-1 (2 / 10) n'est offert que jusqu'au 30 novembre |
````

### C-11 (majeur)

Ancien :

````
| 2 | format non tenu ; E_D < 0,5 | réserve « **format non tenu** » ou « **consigne non suivie** » : P1 et P2 lus et rapportés sous cette réserve ; aucune conclusion sur l'idée |
````

Nouveau :

````
| 2 | format non tenu ; E_D < 0,5 ; **3 appels de B tronqués ou plus (borne de sortie de Pr-1 : 36 000 jetons, pour environ 30 000 attendus ; celle de Pr-2 : 89 000)** | réserve « **format non tenu** », « **consigne non suivie** » ou « **B tronqué** » : P1 et P2 lus et rapportés sous cette réserve ; aucune conclusion sur l'idée ; sous « B tronqué », δ_DB est rapporté aussi sur les mondes où B n'est pas tronqué, et la phrase « perte établie sans la frontière » est **interdite** (elle mêlerait la capacité et la borne) |
````

### C-12 (mineur)

Ancien :

````
Identités : celles de la configuration v12 (`f69503dd…`, bloc gelé de [PILOTE]) ; aucun identifiant de modèle ici (R-2598).
````

Nouveau :

````
Identités : celles de la configuration v12 (`f69503dd…`, bloc gelé de [PILOTE]) ; aucun identifiant de modèle ici (R-2598), hors les clés de
configuration `argon`, `opus55` et `fable52` que le bloc gelé et les lignes de GO exigent (R-2690).
````

### C-13 (majeur)

Ancien :

````
4. **Crédits de Claude au maximum** : forme fidèle (Pr-1, hors crédits, 10,30 attendus hors crédits) ou variante Pr-2 / Pr-4
   (tout sur crédits sauf la machine ; ≈ 128,30 attendus). Recommandation : forme fidèle, parce que la question est celle du proposeur
   **le moins cher** (QO1, QO4) et que l'écart de prix 3,2 est le contraste visé ; confiance 0,55 ; la variante est préférable si la
   part hors crédits doit être nulle.
````

Nouveau :

````
4. **Crédits de Claude au maximum** : forme fidèle (Pr-1, hors crédits, 10,30 attendus hors crédits) ou variante Pr-2 / Pr-4
   (tout sur crédits sauf la machine ; ≈ 128,30 attendus). **Tranché par la mère sur le conseil du contre-lecteur (tour 1)** : à inscrire ici
   après la décision ; **le contre-lecteur recommande la variante** (confiance 0,6) : au prix public, principal, l'écart de prix par jeton est
   de 2 dans les deux formes (Pr-2 4 / 20 contre Pr-1 2 / 10 ; Pr-4 8 / 40 contre Pr-2 4 / 20), et le propre devis de ce texte donne un appel d'écriture
   de Pr-1 à 0,35 à 0,45 contre 0,66 à 0,82 pour Pr-2, soit environ 2 et non 3,2 ; au prix de la configuration, Pr-1 (10 / 50) est **plus cher**
   que Pr-2 (4 / 20) alors que l'écart Pr-4 / Pr-2 reste 2 : le contraste de la variante tient aux deux barèmes, celui de la forme fidèle à un
   barème promotionnel qui s'arrête le 30 novembre. Si la variante est retenue, ce texte est réécrit (section « Si la variante est retenue » du rapport de contre-lecture).
````

### C-14 (mineur)

Ancien :

````
puissance de P1 se recalculera, avant le scellement, par simulation sur processeur sous le modèle de proposeurs synthétiques de
````

Nouveau :

````
puissance de P1 **et de P2** et le taux d'erreur de l'intervalle par percentile à 20 et à 24 mondes (comptes entiers de 0 à 6 composantes, effet nul puis effet
prédit) se recalculeront, avant le scellement, par simulation sur processeur sous le modèle de proposeurs synthétiques de
````

### C-15 (mineur)

Ancien :

````
- **Appels et cartes** : définitions de [PILOTE] et de [CRIBLE-V] (« Métrique ») : appel complet, tronqué, en échec ; carte
````

Nouveau :

````
- **Appels et cartes** : définitions de [PILOTE] (« Métrique »), recopiées ici, sans renvoi à [CRIBLE-V] (brouillon non scellé) : appel complet, tronqué, en échec ; carte
````

### C-16 (mineur)

Ancien :

````
prix de la configuration v12 en sensibilité, voir [CRIBLE-V])
````

Nouveau :

````
prix de la configuration v12 en sensibilité : Pr-1 10 / 50, Pr-2 4 / 20, Pr-4 8 / 40, Pr-3 10 / 50 ; prix publics : Pr-1 2 / 10 jusqu'au 30 novembre, Pr-2 4 / 20, Pr-4 8 / 40, Pr-3 10 / 50 ; note des prix v2, `b88253b8…`)
````

### C-17 (mineur)

Ancien :

````
2. **Sonde des gabarits neufs** (conseillée, sur devis et ligne propre) : sur un monde de développement à graine publique, un
````

Nouveau :

````
2. **Sonde des gabarits neufs** (conseillée ; **obligatoire** si le plus grand appel de Pr-1 du pilote dépasse 30 000 jetons de sortie ; sur devis et ligne propre) : sur un monde de développement à graine publique, un
````

### C-18 (mineur)

Ancien :

````
   lit aucune couverture.
````

Nouveau :

````
   lit aucune couverture. **Règles d'avance** : appel de Pr-1 sous G2 tronqué, ou carte non évaluable dans l'un des trois appels, ou aucune liste d'ensembles
   analysable sous G1 → G1 ou G2 réécrit, nouvelle sonde sur nouvelle ligne, crible non lancé ; sinon les jetons lus corrigent l'attendu et le pire de
   la section « Devis » selon la table de mise à jour.
````

### C-19 (mineur)

Ancien :

````
20 mondes, comme [NOTE] (annexe A de [NOTE] : 0,80 de puissance pour une part passant de 0,05 à 0,40 à 20 mondes).
````

Nouveau :

````
20 mondes, ou 24 par la règle de la section « Seuil » (annexe A de [NOTE] : 0,80 de puissance pour une part passant de 0,05 à 0,40 à 20 mondes, 0,89 à 24). **Puissance de P2 à l'effet prédit** (écart de + 0,5 composante par monde, écart-type d'un écart par
monde supposé de 1,0 à 1,2, approximation normale, mon compte) : environ 0,35 à 0,50 pour que la borne basse à 97,5 % dépasse 0 à 20 mondes : « non tranché » est donc
l'issue la plus probable de P2 même si la prédiction III-2 est vraie ; à refaire par la simulation de la phrase suivante.
````

### C-20 (mineur)

Ancien :

````
; 24 ou 30 mondes si la mère le décide (devis + 20 % à + 50 %).
````

Nouveau :

````
 ; 24 mondes par la règle de la section « Seuil » (devis × 1,2, section « Devis » mise à jour), non 30.
````

### C-21 (mineur)

Ancien :

````
6. **Dollars au prix public** en principal (Pr-1 cinq fois moins cher qu'au prix de la configuration).
````

Nouveau :

````
6. **Dollars au prix public** en principal, **décidé par la mère (R-2977)** ; Pr-1 y est cinq fois moins cher qu'au prix de la configuration, où il devient plus cher que Pr-2 ; lecture de ce risque : étage 4.
````

### C-22 (mineur)

Ancien :

````
7. **Témoin commun avec (v)** : recommandation : non (indépendance ; une seule machine porterait 160 appels, au-delà de la minuterie
   sans parallélisme) ; confiance 0,6.
````

Nouveau :

````
7. **Témoin commun avec (v)** : **écarté par la mère (R-2977)** : mondes séparés ; indépendance, et une seule machine porterait 160 appels.
````

### C-23 (mineur)

Ancien :

````
1. **B sur les ensembles de D** (écart à [NOTE]) : recommandation : oui (appariement, − 20 appels) ; confiance 0,7.
````

Nouveau :

````
1. **B sur les ensembles de D** (écart à [NOTE]) : **retenu (R-2977)** (appariement, − 20 appels) ; B et D ne sont plus indépendants (dit).
````

### C-24 (mineur)

Ancien :

````
2. **Égalités du filtre** : ordre des noms ([NOTE]) ou ordre de proposition de Pr-1 (plus de « choix bon marché » dans D) ?
   Recommandation : ordre des noms, fidèle et indépendant du proposeur ; confiance 0,55.
````

Nouveau :

````
2. **Égalités du filtre** : **ordre des noms retenu (R-2977)**, fidèle à [NOTE] et indépendant du proposeur ; effet : parmi les ensembles à distance 1, le filtre prend
   les premiers dans l'ordre lexicographique, non ceux que préfère Pr-1 (les traits sont permutés dans chaque monde par le générateur : pas de biais d'indice) ; la
   répartition des indices choisis est rapportée.
````

### C-25 (mineur)

Ancien :

````
| relevé de sonde absent ou invalide (si le lanceur l'exige) | refus avant tout dossier | relevé conforme | relevé d'une autre configuration : refus |
````

Nouveau :

````
| relevé de la sonde v74 (configuration v12, déjà joué) absent, invalide ou d'une autre configuration : le lanceur du crible l'exige, sans condition | refus avant tout dossier | relevé conforme | relevé d'une autre configuration : refus |
````

### C-26 (mineur)

Ancien :

````
N_D ≤ 0,25 ; N_H ≈ 0,45 à 0,61
````

Nouveau :

````
N_D ≤ 0,25 ; N_H ≈ 0,45 à 0,61 avant filtre pour 2 ou 3 distracteurs (0,74 pour 4) ; la part **après** filtre est calculée sur les 12 mondes de développement (processeur) avant le scellement et recopiée ici
````

## Si la variante est retenue (corrections supplémentaires, à écrire après la décision de la mère)

Non couplées, car leur texte dépend du choix. Remplacer, dans toute la pièce : Pr-1 (chois, passe 1) par Pr-2 ; « écrivain cher » Pr-2 par Pr-4 ; B = Pr-2 écrit sur les ensembles de D ; S = un appel de Pr-4.
1. **Table des proposeurs** : Pr-4 `fable52` (crédits, plafond de session 3 USD, borne 64 000, part 180) ; Pr-2 `opus55` (crédits, 2 USD, 89 000, part 80) ; machine seule hors crédits.
2. **Prédictions** à refaire avant le scellement, sans donnée de proposeur : III-1 (rapport de coût D / S devient 1,05 à 1,3 environ : la passe 1 coûte peu et l'écriture reste celle de Pr-4) ; **III-2** (écart Pr-4 contre Pr-2 sur les
   mêmes ensembles : même maison, l'attente de + 0,5 à 0,45 de confiance est trop haute, à abaisser) ; III-5 ; III-7 ; libellés : « la frontière » devient « le palier supérieur de la même maison ».
3. **Devis** : 128,30 attendus et 263 au pire à 20 mondes (environ 154 et 315 à 24) ; lignes de GO : κiii1 = Pr-4 (part 180) et Pr-2 (part 80), 260 USD sur crédits ; κiii2 = machine seule, 3 USD ; sonde : G1 par Pr-2, G2 par Pr-4 et par Pr-2, plafonds
   2,00 + 3,00 + 2,00 = 7,00 USD sur crédits, attendu environ 2,1 à 2,5.
4. **Durée et tronquage** : les bornes de sortie (64 000 et 89 000) laissent plus de marge que celle de Pr-1 : la réserve « B tronqué » reste, avec un seuil de 3 appels.
5. **Pilote** : le taux de réussite par appel se lit sur les relais `fable52` et `opus55` (π1 du pilote), non sur `argon`.
6. **Contre-lecture du tour 2** de la pièce ainsi réécrite : obligatoire (la forme des prédictions change).

## Points pour la mère

1. **Forme** : trancher entre la variante (recommandée, confiance 0,6) et la forme fidèle ; sans décision, la pièce ne peut pas être corrigée de façon unique ; vérifier le solde de crédits de Claude pour 263 USD au pire.
2. **Prix promotionnel de Pr-1** : la lecture « bon marché » n'est vraie qu'au prix public offert jusqu'au 30 novembre ; au prix de la configuration, Pr-1 est plus cher que Pr-2 ; un crible qui déborderait le 30 novembre changerait de question (C-10, C-13).
3. **Nombre de mondes** : la règle de R-2977 (24 si le taux du pilote est sous 0,95) est reportée par C-04 ; mais à N = 20 et p = 0,95, le minimum de 16 n'est atteint que dans la moitié des cas : envisager **24 mondes sans condition** (+ 20 % : environ + 11 USD attendus en forme fidèle, + 30 en variante). Le taux du pilote ne sera connu qu'après lecture par un lecteur neuf : la règle écrite d'avance (C-07) évite de lire le pilote avant scellement au-delà du taux et des coûts.
4. **Écart à un texte** : N-045 point 3 (ablation « hors des critères gelés ») : non violé à la lettre (le crible n'est pas une course) mais son esprit ; la décision est celle de la mère (R-2977) : **le dire à Lazar** avec le nœud d'adoption (C-08).
5. **Prédictions et pilote** : interdire la révision de III-1 à III-6 après lecture du pilote (C-06) ou l'autoriser par une règle ; je recommande le gel (le pilote mesure une première conditionnelle trouvée avant sa condition, donnée proche de III-6).
6. **Code neuf** : lanceur, gabarits, filtre, mesure, procédure de machine, essai à blanc à cinq files : environ deux jours d'agents (la pièce dit deux jours) ; rien du pilote ne se réemploie tel quel ; la concurrence de 10 sessions par relais n'a jamais été éprouvée.
7. **Risque** : un « non tranché » est l'issue la plus probable de P2 même si l'auteur a raison (puissance 0,35 à 0,50) ; ne pas lire un « non tranché » comme une absence d'effet (la pièce le dit pour P1 et P2 en général).

## Incidents (de ma main)

- Je me suis d'abord trompé d'outil (`bash` en minuscules, refusé) ; sans effet.
- `find /` a listé deux noms de fichiers (`comptes_cribles_v2.py`, `compte_certifiees_mr2_v1.py`) dans un dossier du bloc-notes de la session, `outils-cribles`, qui n'est pas à moi : **je ne les ai pas ouverts** ; j'ai extrait le code **de la pièce** dans mon propre dossier du bloc-notes (`…/scratchpad/c2`) et l'ai rejoué, avec `nice -n 19 python3 -I`, bibliothèque standard seule (quelques millisecondes).
- `git branch -a` et `git ls-tree` ont affiché des noms de branches et de dossiers (dont des noms de la branche de sortie du pilote et un dossier `lecture-issue-pilote-v14-mere`) : **rien n'en a été ouvert** ; issue du pilote non lue. Un seul `git fetch` avec refspec (`lot/compte-organisme-v1`), aucun clone.
- Aucun fichier existant modifié ; aucun commit ; ni `env` ni `printenv` ; ni `pytest` ; rien lu sous `diag/`, `runs/`, `donnees/`, rien de 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque.
