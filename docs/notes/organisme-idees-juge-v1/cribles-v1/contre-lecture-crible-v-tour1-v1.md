# Contre-lecture du préenregistrement du crible (v), brouillon 1 — tour 1 — v1

- Contre-lecteur : sous-agent neuf, **modèle C** (identité dite en conversation seulement) ; auteur de la pièce : modèle A ; je n'ai écrit
  aucune pièce citée. Un premier contre-lecteur (modèle B) s'est arrêté sans rapport (limite d'usage) : je n'ai lu ni ses dossiers ni rien de lui.
- Date (UTC) : lecture de 13:24:10Z à 13:34:13Z (`date -u`) ; lecture entière de la pièce, tour 1.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-brouillon1.md`, empreinte entière
  `ec8d04962b570b97f16f49b289dfbb3e8b32fcb8468090fafb164434ed59678a` (vérifiée par `sha256sum`, égale à son compagnon et au début de l'empreinte de R-2977).
- Pièces lues : la pièce en entier ; la note des idées originales (`2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3`,
  vérifiée ; § 0, 1, 2, 3 (v), 4, 5, 6, 7, annexe A) ; la ligne R-2977 de `registres/decisions.md` et les lignes « crible » (par `grep`) ; la ligne
  GO-2026-11-15-06 de `registres/go.md` ; N-058 (`854f2724…`) en entier ; la procédure v14 du pilote au commit `2d35cafa…` (`2035562740efe1e87db9ffa2f0494705bb5117c56069309ece2279d351bde18a`,
  après `git fetch` de la seule branche `lot/compte-organisme-v1`) : § 0, 6, 7 ; le texte scellé du pilote, candidat 6 (`8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`,
  `git show` de la branche `prep/pilote-mr2-compte-organisme-v1`, après `git fetch` de cette seule branche) : « Dessin », « Métrique », « Seuil », « Devis » ; la note des
  prix publics v2 (`b88253b8…`, même branche que la procédure) ; `conception-monde-riche-doublons-v3.md` (`386d48ba…`) : § 1.8, § 3.1, § 4.3 ; le relevé des idées
  (`bd253b6c…`, § 4.3) ; le verdict de la course v67 (`d7902432…`, seulement les lignes sur les durées et les cartes, par `grep`) ; le gabarit,
  `prereg.py`. Les empreintes entières de tous les fichiers cités par la pièce ont été recalculées par `sha256sum` (voir point 9). **Non lu** : tout ce que la consigne interdit
  (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 non ouvert ; sortie du pilote non ouverte ; 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque). Aucun appel de modèle, aucune dépense, aucune machine.
  Un seul chiffre de marche du pilote m'est passé sous les yeux en lisant la ligne R-2981 du registre des décisions (comptes de marche, non l'issue) : je l'utilise une fois, dit, au point C-02.

## Verdict

**corrections.** La conception tient (question claire, rejeu contrefactuel exact, filtre sans issue, devis arithmétiquement exact aux plafonds, annexes sans donnée) ; elle ne peut pas
être scellée telle quelle : **10 corrections majeures** (durée et code neuf non fixés ; nombre de mondes, minimum et seuil de perte non reliés à la règle de R-2977 ni au taux d'appels
répondus ; règle d'avance sur ce qui sera refait d'après le pilote absente ; seuil d'épargne mal étiqueté et non justifié ; puissance de la perte surestimée ; cas dégénéré annoncé non réglé par le
critère gelé ; décisions de R-2977 non reportées ; partie A contradictoire sur le verdict du juge ; audit de symétrie mal ciblé ; devis dont l'« attendu » et la part sur crédits sont faux au regard
des fourchettes de la pièce) et **11 mineures**. Aucune faute de conception qui oblige à refaire : pas de « a_refaire ».

## Réponses aux neuf points

**(1) R1.** Hypothèse, prédictions chiffrées avec signe, métrique, seuils, plan d'analyse, critères gelés, liste d'arrêt : tous présents, d'une forme qui suit les deux modèles scellés. Portes de sortie
après lecture, à fermer : (a) nombre de mondes « 24 ou 30 » laissé à la mère (C-02) ; (b) tout ce qui sera « refait » d'après le pilote, sans table de ce qui peut changer (C-03) ; (c) minuterie « durée bornée »
non définie (C-01) ; (d) relevé de sonde « si le lanceur l'exige » (C-10) ; (e) étage 5 (ablation) « à confirmer par la mère » : décision à prendre avant scellement (point pour la mère) ; (f) prédictions V1, V2, V6 sans zone
« indécise » entre confirmée et réfutée (C-12).

**(2) R3.** *Seuil 0,25 d'épargne.* Choix de ce texte (dit en « Seuil »), mais l'énoncé de H-v le met dans « l'énoncé de la fiche, tel que [NOTE] le pose » : or [NOTE] § 3 (v) ne dit pas « au moins un quart » ; la fiche non plus
([RELEVÉ] § 4.3). Étiquette fausse : C-04. Surtout, **S_R n'est presque qu'une fonction de k_R** : si la moitié chère pèse 0,71 du coût (prix de [NOTE]) à 0,75 (fourchette de la pièce, prix publics), S_R ≥ 0,25
équivaut à k_R ≤ 12 ou 13 sur 20 ; l'étage 3 (a) ne dit donc rien de plus que « la règle appelle les chers dans 14 mondes ou plus ». Un seuil qui ne peut échouer que si la règle ne règle presque rien est très
facile à passer : il est non informatif, pas faux ; il faut le dire et en donner la raison. *« Perte établie » dès 4 mondes sur 20.* Dérive de « borne basse de Clopper-Pearson > 0,05 » : le 0,05 (une perte tolérée de 5 % des mondes)
n'est justifié nulle part. **Puissance surestimée** : la pièce cite 0,80 à p = 0,26 sur 20 mondes à risque ; mais sous sa propre prédiction (k_R ≤ 3) seuls 17 mondes ou moins peuvent perdre (a_w = 1 ne perd pas) :
P(W_R ≥ 4) = 0,24 / 0,68 / 0,90 pour p = 0,15 / 0,26 / 0,35 à 17 mondes à risque (contre 0,35 / 0,80 / 0,96 à 20 ; calcul par la loi binomiale exacte, stdlib, refait par moi, à recopier en annexe par programme) ; C-05. *Seuil W par nombre de
mondes* : « W_R ≥ 4 » n'est vrai que pour n_c de 16 à 22 ; pour n_c = 23 ou 24 (la variante à 24 mondes de R-2977) il faut W ≥ 5 (borne basse 0,0495 à 4/23 ; 0,0474 à 4/24) : C-02. *Cas dégénéré.* La pièce l'annonce (V1 : k_R ≤ 3, confiance 0,65 ;
V5 : « non éprouvable », 0,6) : le crible n'éprouve alors **pas la règle** (la branche « appeler » n'a presque pas de monde), seulement l'ablation (H-v-a). L'issue « non éprouvable » est définie (4 ≤ k_R ≤ n_c − 4) et gelée
à l'étage 4, mais **l'étage 3 prononce quand même « H-v non réfutée au crible »** quand W_R = 0, y compris si k_R = 0 (alors W_R = W_B et la règle est « jamais les chers »). Le mot est trompeur : C-06. Le crible reste informatif pour QO1
(ablation), non pour la règle : dis-le en tête. Le **bras à archive enrichie avec appels** (+ 80 appels, + 196,60 au pire) est hors de portée de la décision de la mère (R-2977 : archive réduite à K1) ; en revanche **deux lectures sans appel de plus** le remplacent
en partie : (i) « règle au rang » (appeler les chers dans les n_c/2 mondes de plus forte part q_w, k fixé d'avance, rapporté sans verdict ; éprouvable par le placebo quel que soit k_R) ; (ii) rejeu de la **seule décision** sous une archive fictive
(K1 et les composantes fortes et moyennes du monde, comme après une génération réussie), couverture non lue (contrefactuel invalide pour les proposeurs, qui n'ont pas vu cette archive) : elles montrent si la fonction de décision peut seulement se déclencher. À adopter dans C-06.
*Distance dans un seul sens* (carte vers K1) : le sens est raisonné et déclaré (§ « Écarts ») ; c'est un **écart déclaré** à [V3] § 3.1, non à corriger, mais il faut le rapporter en sensibilité (minimum des deux sens) : C-13.

**(3) Devis.** *Recompte.* 20 appels par proposeur, 80 en tout ; plafonds de session 2,34 / 2,00 / 2,34 / 3,00 (bloc gelé) ; pires : Pr-1 46,80, Pr-2 40,00, Pr-3 46,80, Pr-4 60,00, machine 3,00 ; sur crédits 100,00, hors crédits 96,60, total 196,60 ;
écart à [NOTE] 13,60 : **exacts**. Pires par appel recalculés : (53 024 jetons d'entrée au prix de la configuration + borne de sortie) = 2,33 / 1,992 / 2,33 / 2,984 : tous sous leur plafond ; les jetons d'entrée (1,06 M) et de sortie (0,72 ; 1,78 ; 0,72 ; 1,28 M) de la table sont exacts.
Fourchettes (79,95 à 92,75) : exactes à partir des fourchettes par appel. *Écarts.* (a) L'**attendu de 73,30** (repris de [NOTE]) est **sous la borne basse de la fourchette de la pièce** (79,95) ; il est écrit en tête (« en dix lignes », point 8, et table). (b) La **part sur crédits « ≈ 65 % de l'attendu »**
vaut 48/73,30 ; avec la fourchette de la pièce elle vaut 39,60/79,95 = 0,50 à 49,20/92,75 = 0,53 aux prix publics, et 0,37 à 0,39 au compte de la configuration (Pr-1 à 34 à 42 USD) ; au pire, 100/196,60 = 0,51. Le consigne de Lazar (« crédits de Claude au max ») est tenue
**au maximum que permet la configuration** (seuls Pr-2 et Pr-4), mais le chiffre de 65 % ne l'est pas : C-10. (c) **Deux comptes** : la pièce les dit ; mais « la part et la ligne de GO se jugent » au compte de la configuration, donc l'attendu qui compte pour la ligne est celui de ce compte (≈ 107 à 126 USD au total) : à écrire (C-10).
(d) La **sonde neuve** (8,07 au pire) n'est dans aucune des deux lignes proposées : si elle est exigée, les lignes passent à 104,39 et 100,28 (204,67) : décider avant le scellement (C-10). (e) **Enveloppe de GO-2026-11-15-06** (1 275 pour les cinq) : cohérente pour (v) et (iii) pris ensemble (413,20 ; R-2977) ; la somme des cinq n'est pas tenue d'office, car les plafonds de 2,34 touchent aussi les trois autres : point pour la mère. (f) Le prix public de Pr-1 (2 / 10) double le 1er décembre (note des prix v2, `b88253b8…`) et la ligne de GO échoit le 30 novembre : C-11.

**(4) Durée.** La pièce donne ≈ 7 à 10 h de machine, et reconnaît que le pire cas de `jouer` (4 × 10 800 s pour 4 mondes, procédure v14 § 0) fait 60 h pour 20 mondes en série (exact : 5 × 12 h), mais **ne fige rien** : ni borne par appel, ni mondes en parallèle, ni budget horaire de pire cas, et la garde de minuterie
(« durée bornée des appels ») n'a pas de valeur. Constats : les 10 800 s sont le délai **par appel** de la configuration v12 ; à v67 deux appels d'un proposeur ont pris 861 s et 1 099 s (verdict v67 § 4.1, qui cite aussi une borne de 1 800 s) ; la procédure v14 exige 12 h 30 avant l'échéance
pour 4 mondes et prévoit jusqu'à 60 min pour 4 mondes sur un hôte chargé (5 h pour 20) ; barrières 2 h 40 au pire ; mesure et rapatriement. Une machine à 17 h ne tient pas 20 mondes en série au pire cas, même avec 1 800 s par appel (20 × 1 800 s = 10 h, plus 5 h de mondes, plus 2 h 40, plus la mesure : plus de 17 h).
**Faisable avec le code du pilote ? Non.** Le lanceur du pilote est écrit pour 4 mondes, 16 appels, un minimum de 12 sur 16 et 3 par monde, des identifiants de GO et des empreintes de pièces propres au pilote, une garde de 12 h 30 sur 4 × 10 800 s. Il faut : un lanceur neuf (nombre de mondes, borne par appel, parallélisme ou non),
une mesure neuve (`mesure_crible_v_v1.py`), un programme de lecture, un programme de la partie A, une procédure de machine neuve (la procédure du pilote en est à sa quatorzième version), les essais R5 et le banc de mutations de la pièce, la contre-lecture du code par un autre modèle, un addendum d'empreintes, la lecture de l'issue du pilote
et le devis refait, puis deux lignes de GO inscrites. **C'est cela, et non le préenregistrement, qui fixe la date de lancement** : mon estimation (non mesurée) est de plusieurs jours de travail d'agents, bien au-delà de « un à deux jours », donc un lancement au plus tôt vers le 21 au 24 novembre, avec la ligne de GO qui échoit le 30
(et le prix de Pr-1 qui double le 1er décembre) : fenêtre de six à neuf jours. C-01 demande d'écrire d'avance : borne par appel, nombre de mondes à la fois, budget horaire de pire cas ≤ 17 h, conséquence d'un dépassement (appel « échec », compté dans le taux d'appels répondus et dans le minimum de mondes complets, rapporté par proposeur : une borne de durée censure
différemment les proposeurs lents).

**(5) Liste d'arrêt, graines.** Chaque ligne a son essai sain et son artefact (R5) ; deux défauts : l'artefact de la ligne « partie A » ne couvre pas « un seuil changé » (C-14) ; la garde de minuterie est indéfinie (C-01). Ligne « coût au-dessus du pire cas » : un seul appel de Pr-1 qui dépasse (réflexion ajoutée, non bornée) arrête tout le crible
(code 3, « ni relance ») ; sur 20 appels de Pr-1 le risque est réel : règle à écrire d'après le pilote (C-17). Graines : `numpy.random.SeedSequence` avec racine et clés dérivées : conforme (R9) ; deux imprécisions : « graine qui dépend du monde » contredit la clé `(r, 30)` si r est l'indice du monde (C-15) ; la graine de l'audit n'a pas de clé écrite (C-16).

**(6) Tension avec N-058.** La pièce la déclare (section « Écarts », choix 11) et borne l'essai à la génération 1, archive {K1} sans verdict : ce qui ne viole pas N-058. Elle n'interdit pas pour autant toute lecture indirecte : **la partie A lit des archives de la génération 2 qui contiennent « les 11 retenues »**, c'est-à-dire le résultat du verdict du juge de v67,
tout en déclarant « aucun verdict du juge n'est lu » : contradiction à lever (C-08). Le critère est bien évalué sur l'oracle et le coût seuls. Adoption : nœud de Lazar, dit.

**(7) Partie A.** Descriptive, sans critère, sortie scellée avant lecture, aucun seuil changé : bien. Manquent : l'étiquette « données déjà vues » (R-2977) et la levée de la contradiction du point 6 (C-07, C-08). La partie A est lue **avant** le texte qui fera foi (étape 1 avant étape 2) : les prédictions V1 et V6 peuvent donc être influencées par elle ; à dire, et à séparer des seuils (C-03).

**(8) R7 et R8.** Aucun chiffre de l'état de l'art : les cinq voisins nommés sont « à vérifier » ou « non relus par moi » ; zone « séduisante » traitée comme une question. Corrections de forme : la pièce 2611.04420 est rangée parmi les filtres de nouveauté alors que N-067 la cite pour les batteries de mutations d'un vérificateur et pour N-058 (C-19) ; le même
arXiv 2609.17560 s'appelle « Pay Only for Disagreement » dans le catalogue et « DISCERN » dans N-067 § 3 : à signaler (remarque facultative R-3).

**(9) `controle_ia.prereg.problemes`.** Rejoué (`.venv/bin/python -I`) : un seul défaut, le défaut attendu au tour 1 (« section Contre-lecture sans les deux empreintes exigées (brouillon relu et rapport) »). Aucun identifiant de modèle (la pièce dit « modèle A », « modèle B ≠ A ») ; les clés de configuration `opus55` et `fable52` contiennent un nom de
modèle : remarque facultative R-2. Empreintes vérifiées par `sha256sum` : toutes celles de la section « Documents qui font foi », de l'annexe A (programmes `f06bcfe7…` et `8c0432df…`, sorties `5d53092e…` et `319fa358…`) et des citations obligatoires (cinq PDF) **égales** ; `go.md` au commit `377a2a0c` : `4bcec4a0…` égale ; procédure v14 : égale ; texte scellé du pilote : égale ;
note des prix v2 : égale. Les programmes de l'annexe A sont recopiés dans `crible-iii-brouillon1.md` (lignes 498 et 676) : voir C-20.

## Corrections exigées

Chaque « ancien » est une chaîne d'une seule ligne de la pièce, présente une seule fois (vérifié par programme à 13:34Z, voir la fin). Les « nouveau » sont des propositions à écrire par l'auteur (modèle A) ; les chiffres que j'y ai recomptés sont à refaire par programme et recopiés en annexe.

### Majeures

**C-01 — Durée : figer la borne par appel, le parallélisme et le budget horaire de pire cas.**
```
ANCIEN: des relais non éprouvée) : à décider sur la durée mesurée du pilote.
NOUVEAU: des relais non éprouvée) : **écrit d'avance** : borne par appel B_a (jamais celle de 10 800 s du pilote ; valeur et mondes en parallèle fixés avant le scellement d'après la durée mesurée du pilote, cette règle seule pouvant bouger), nombre de mondes à la fois M ; budget de pire cas = mise en place + barrières (2 h 40) + génération de 20 mondes (pire cas écrit) + ⌈20/M⌉ × B_a + mesure + rapatriement, **≤ 17 h**, chiffré dans une table ; un appel au-delà de B_a est un « échec » (compté dans le taux d'appels répondus, dans le minimum de mondes complets, rapporté par proposeur). Le lanceur, la mesure, la lecture et la procédure de la machine sont du code neuf (le lanceur du pilote est écrit pour 4 mondes et 16 appels) : la date de lancement en dépend.
```
```
ANCIEN: | minuterie de la machine : moins de la durée bornée des appels restante avant l'échéance | arrêt (A) sans appel | marge suffisante | échéance proche simulée : arrêt |
NOUVEAU: | minuterie de la machine : moins que le budget de pire cas de la table de durée (valeur écrite, ⌈20/M⌉ × B_a compris) restante avant l'échéance | arrêt (A) sans appel | marge suffisante | échéance proche simulée : arrêt |
```

**C-02 — Nombre de mondes, minimum, seuil de perte : une règle écrite, pas « 24 ou 30 ».** (R-2977 : 24 mondes si le taux d'appels répondus du pilote est sous 0,95.) Le minimum de 16 mondes complets sur 20 est presque inatteignable si le taux par appel est sous 0,95
(un monde est complet si ses quatre appels répondent : 0,95⁴ = 0,81 ; P(n_c ≥ 16 sur 20) = 0,69 à 0,95 par appel, 0,13 à 0,90 ; avec 24 mondes et le minimum de 16 : 0,98 et 0,55). Les comptes de marche de R-2981 (14 appels complets, 2 tronqués sur 16 : à confirmer par le lecteur de l'issue,
je n'ai pas lu l'issue) donneraient 0,875 par appel : P(n_c ≥ 16) ≈ 0,04 sur 20 mondes et ≈ 0,28 sur 24. Si ces comptes sont confirmés, le crible serait presque sûrement « non concluant » : **la définition de « monde complet »** doit être revue avant scellement (par exemple : au moins un appel répondu par moitié, couvertures
calculées sur les cartes disponibles, comme la sensibilité « mondes non complets réintégrés » le fait déjà), ou les troncatures traitées à la source (bornes de sortie de Pr-1 et Pr-3 « à marge mince », bloc gelé).
```
ANCIEN: nombre de mondes à 24 ou 30 (devis à l'avenant, + 20 % à + 50 %), décision de la mère avant le scellement.
NOUVEAU: nombre de mondes **fixé par règle écrite d'avance** (décision de la mère, R-2977) : 20 si le taux d'appels répondus par appel mesuré au pilote est ≥ 0,95, 24 sinon (devis à l'avenant, + 20 %) ; pas de 30. Le minimum de mondes complets et la définition de « monde complet » sont recalculés par programme sur ce taux (probabilité d'atteindre le minimum écrite en annexe) avant scellement ; les trois autres nombres (seuils de perte, bornes de placebo) suivent le tableau « seuils par n_c » ci-dessous.
```
```
ANCIEN: - **Minimum** : n_c ≥ 16 mondes complets sur 20, et aucun fournisseur perdu en entier ; sinon « non concluant ».
NOUVEAU: - **Minimum** : n_c ≥ 0,8 × (nombre de mondes tirés, 20 ou 24 par la règle de la section « Taille ») mondes complets, soit 16 sur 20 ou 20 sur 24 (arrondi au supérieur), et aucun fournisseur perdu en entier ; sinon « non concluant ». **Seuils par n_c** (W_min = plus petit W dont la borne basse de Clopper-Pearson à 95 % dépasse 0,05 ; calcul du lecteur C à refaire par programme et recopier en annexe) : n_c de 16 à 22 → 4 ; n_c = 23 ou 24 → 5.
```
```
ANCIEN: « **perte établie** » si la borne basse de Clopper-Pearson de W_R / n_c dépasse 0,05, soit **W_R ≥ 4** pour
NOUVEAU: « **perte établie** » si la borne basse de Clopper-Pearson de W_R / n_c dépasse 0,05, soit **W_R ≥ W_min(n_c)** (table « seuils par n_c » ci-dessus ; 4 pour
```
(Reporter ensuite « W_R ≥ 4 » en « W_R ≥ W_min » dans la table des prédictions, l'étage 3 et l'étage 5 ; la liste est à faire par l'auteur : le motif « W_R ≥ 4 » et « W_B ≥ 4 » apparaît plusieurs fois.)

**C-03 — Règle d'avance sur ce qui sera refait d'après le pilote.** « Refait en version qui fera foi (devis, prédictions, puissance) » laisse après lecture du pilote et de la partie A une marge sur tout. Écrire : peuvent changer (et seulement ainsi) les montants du devis, B_a, M, n de mondes par la règle de C-02, les confiances
et les chiffres de V1 et V6 (déclarés « écrits après lecture du pilote, coûts et taux seulement, et de la partie A ») ; sont **gelés dès ce texte** : H-v, ε, ε_strat, 0,8, la définition de copie, l'ordre des étages, les noms des verdicts, les seuils d'épargne et de perte (hors W_min(n_c)), la liste d'arrêt.
```
ANCIEN: 2. **Avant toute dépense** : pilote MR-2 joué, ses coûts et durées mesurés, ce texte refait en version qui fera foi (devis,
NOUVEAU: 2. **Avant toute dépense** : pilote MR-2 joué, ses coûts et durées mesurés, ce texte refait en version qui fera foi **dans les seules limites de la table suivante : peuvent changer les montants du devis, B_a, M, le nombre de mondes (règle de la section « Taille »), les chiffres et confiances de V1 et V6 (dits écrits après lecture du pilote, coûts et taux seulement, et de la partie A) ; sont gelés dès ce texte H-v, ε, ε_strat, 0,8, la définition de copie, les étages, leurs verdicts, les seuils d'épargne et de perte, la liste d'arrêt** (devis,
```

**C-04 — Seuil d'épargne : étiquette fausse, lien avec k_R, raison.**
```
ANCIEN: épargne au moins un quart des dollars des proposeurs **sans perte de
NOUVEAU: épargne **notablement** (seuil de ce texte, 0,25 de S_R, non chiffré par la fiche : voir « Seuil ») les dollars des proposeurs **sans perte de
```
```
ANCIEN: **H-v** (énoncé de la fiche, tel que [NOTE] le pose).
NOUVEAU: **H-v** (énoncé de la fiche tel que [NOTE] le pose ; le chiffre de l'épargne notable est celui de ce texte, non de la fiche).
```
```
ANCIEN: - **Épargne notable** : S_R ≥ 0,25 (un quart des dollars des proposeurs ; choix de ce texte, la fiche ne chiffre pas, lue à
NOUVEAU: - **Épargne notable** : S_R ≥ 0,25 (un quart des dollars des proposeurs ; choix de ce texte, de portée pratique et non déduit d'une donnée ; la fiche ne chiffre pas ; **S_R est presque une fonction de k_R** : la moitié chère pèse 0,71 à 0,75 du coût, donc S_R ≥ 0,25 équivaut à k_R ≤ 12 ou 13 sur 20 et l'étage 3 (a) revient à « la règle appelle les chers dans 14 mondes ou plus » ; lue à
```

**C-05 — Puissance de la perte : ne pas compter les mondes où la règle appelle les chers.** Reprise des chiffres (loi binomiale exacte, lecteur C) : mondes à risque 17 (k_R = 3) : 0,24 / 0,68 / 0,90 ; 20 (k_R = 0) : 0,35 / 0,80 / 0,96, pour p = 0,15 / 0,26 / 0,35. Dire aussi que W_R de 1 à 3 donne « non tranchée » alors que H-v dit « sans perte de couverture » : perte observée, non établie.
```
ANCIEN: la probabilité 0,13 à p = 0,10, 0,59 à p = 0,20, 0,80 à p = 0,26
NOUVEAU: la probabilité 0,13 à p = 0,10, 0,59 à p = 0,20, 0,80 à p = 0,26 **quand les 20 mondes sont à risque (la règle n'appelle jamais les chers) ; sous la prédiction V1 (k_R = 3), 17 mondes seulement peuvent perdre : 0,24 à p = 0,15, 0,68 à p = 0,26, 0,90 à p = 0,35 (loi binomiale exacte, à recopier par programme en annexe)**
```
```
ANCIEN: une « perte établie » sur 20 mondes a une probabilité de 0,80 (annexe A, point 6).
NOUVEAU: une « perte établie » sur 20 mondes à risque a une probabilité de 0,80 (annexe A, point 6) ; sur 17 mondes à risque (k_R = 3, V1), 0,68 (calcul à recopier en annexe).
```

**C-06 — Cas dégénéré : le critère gelé doit primer sur le mot « H-v non réfutée », et deux lectures sans appel s'ajoutent.**
```
ANCIEN: **Lecture de H-v.** Étage 3 (c) : « H-v non réfutée au crible » ; (a) ou (b) : « H-v réfutée au crible » ; (d) : « non
NOUVEAU: **Lecture de H-v.** **Si k_R < 4 (ou k_R > n_c − 4, « non éprouvable » à l'étage 4), H-v est dite « non éprouvée au crible » quel que soit l'étage 3 : la règle se confond avec « jamais les chers » (ou « tout appeler »), et le verdict de l'étage 3 est lu comme un verdict sur cette règle dégénérée, jamais sur la règle de décision.** Sinon : étage 3 (c) : « H-v non réfutée au crible » ; (a) ou (b) : « H-v réfutée au crible » ; (d) : « non
```
```
ANCIEN: - **Sensibilités, rapportées sans verdict** : τ'_i = max(0,005 ; 0,25·I_i) ; toutes les composantes (non seulement les
NOUVEAU: - **Sensibilités, rapportées sans verdict** : **règle au rang** (appeler les chers dans les ⌊n_c/2⌋ mondes de plus forte part q_w, égalités par l'empreinte du monde ; placebo exact comme pour la règle ; sans appel de plus) ; **rejeu de la seule décision a_w sous une archive fictive** (K1 et les composantes fortes et moyennes du monde, lues par l'expérimentateur, jamais par la règle ; couverture non lue ; contrefactuel invalide pour les proposeurs, qui n'ont pas vu cette archive) ; τ'_i = max(0,005 ; 0,25·I_i) ; toutes les composantes (non seulement les
```

**C-07 — Décisions de R-2977 à reporter dans la pièce.** La section « Choix et doutes » est restée en questions ; R-2977 a tranché (archive réduite à K1 ; mondes séparés entre les deux cribles ; dollars principaux au prix public, prix de la configuration en sensibilité ; GO valable pour l'essai et non l'adoption ;
partie A permise, descriptive, « données déjà vues », sans verdict du juge ; 24 mondes si taux sous 0,95 ; tension avec N-058 à dire à Lazar avec le nœud d'adoption).
```
ANCIEN: ## Choix et doutes soumis à la mère
NOUVEAU: ## Choix et doutes (tranchés par la mère le 16 novembre, R-2977, aux points 2, 4, 5, 6, 9 et 11 ; points 1, 3, 7, 8, 10 encore ouverts, à trancher avant scellement)
```
```
ANCIEN: cartes et des archives réelles et une donnée descriptive, sans critère.
NOUVEAU: cartes et des archives réelles et une donnée descriptive, sans critère, **sur des données déjà vues (relevé de la course v67 déjà connu du programme ; décision de la mère, R-2977)**.
```

**C-08 — Partie A : « aucun verdict du juge lu » contredit l'usage des retenues.** Les archives de jugement de la génération 2 sont « K1 et les 11 retenues » (verdict de v67, § 3, V-2) : les retenues sont le résultat du jugement. La règle y dépend donc, en génération 2, du juge, ce que N-058 et N-053 (point 5) visent. À déclarer : la partie A lit les lois retenues comme **données d'entrée**, non comme verdicts ; la génération 2 de la partie A illustre précisément la dépendance indirecte, sans rien décider.
```
ANCIEN: - **Interdits** : aucun verdict du juge de v67 n'est lu ni rapproché ; aucune couverture (le monde jouet n'est pas lu) ; aucun
NOUVEAU: - **Interdits** : aucun verdict (promotion, rejet, mort) du juge de v67 n'est lu ni rapproché de la décision de la règle ; les lois « retenues » qui entrent dans l'archive de la génération 2 sont un **résultat du juge** lu comme liste de lois, dit : la génération 2 de la partie A montre la dépendance indirecte de la règle aux verdicts (N-058, N-053 point 5), sans rien décider ; aucune couverture (le monde jouet n'est pas lu) ; aucun
```

**C-09 — Audit de symétrie : relire les cartes qui font la perte, pas trois au hasard.** Les attributions de l'oracle « peuvent faire porter à une loi une composante qu'elle ne contient pas » (pilote, « Métrique », R-4) : une perte comptée (ℓ_w ≥ 1) peut être un débordement d'attribution d'une carte chère ; trois cartes tirées par monde ne les voient pas.
```
ANCIEN: **Audit de symétrie (R4)**, écrit avant le prononcé pour **toute** issue : relecture des copies de trois cartes par monde
NOUVEAU: **Audit de symétrie (R4)**, écrit avant le prononcé pour **toute** issue : relecture de **toutes les cartes de la moitié chère qui portent seules une composante dans un monde compté dans W_R ou W_B** (contrôle du débordement d'attribution), puis des copies de trois cartes par monde
```

**C-10 — Devis : « attendu » et part sur crédits à l'échelle des fourchettes de la pièce ; sonde neuve.**
```
ANCIEN: 8. **Devis (brouillon, estimé)** : 73,30 USD attendus selon [NOTE] (48 sur crédits de Claude, 25,30 hors crédits ; mes
NOUVEAU: 8. **Devis (brouillon, estimé)** : 73,30 USD « attendus » selon [NOTE], **inférieurs à la borne basse de ma propre fourchette (79,95 à 92,75 aux prix publics ; ≈ 107 à 126 au compte de la configuration, qui est celui de la part et de la ligne de GO)** (48 sur crédits de Claude, 25,30 hors crédits selon [NOTE] ; mes
```
```
ANCIEN: - **Part des crédits de Claude** : ≈ 65 % de l'attendu, **100 % de ce que la configuration permet** pour ce dessin (seuls Pr-2
NOUVEAU: - **Part des crédits de Claude** : ≈ 50 à 53 % de la fourchette aux prix publics, ≈ 37 à 39 % au compte de la configuration, ≈ 51 % du pire cas (100/196,60) ; le 65 % de [NOTE] vient de l'attendu de 73,30, trop bas ; **100 % de ce que la configuration permet** pour ce dessin (seuls Pr-2
```
```
ANCIEN: | conditionnel : sonde neuve (si le lanceur l'exige ; lignes de la sonde v74 : s1 4,39 sur crédits, s2 3,68 hors crédits) | 8 | — | — | les deux | 0,10 | — | 8,07 |
NOUVEAU: | sonde neuve : **exigée ou non, décidé avant le scellement** (si elle l'est, les lignes κv1 et κv2 passent à 104,39 et 100,28 USD, total 204,67 ; lignes de la sonde v74 : s1 4,39 sur crédits, s2 3,68 hors crédits) | 8 | — | — | les deux | 0,10 | — | 8,07 |
```

**C-11 (mineure) — Prix promotionnel de Pr-1 et échéance du 30 novembre.**
```
ANCIEN: **prix publics de l'offre standard** lus le 14 novembre (note des prix v2, `b88253b8…` : 8 / 40 ; 4 / 20 ; 10 / 50 ; 2 / 10 USD
NOUVEAU: **prix publics de l'offre standard** lus le 14 novembre (note des prix v2, `b88253b8…`, où le prix de Pr-1 double le 1er décembre : 4 / 20 à partir de cette date, rapporté en sensibilité avec celui de la configuration ; 8 / 40 ; 4 / 20 ; 10 / 50 ; 2 / 10 USD
```

### Mineures

**C-12 — Zones « indécises » des prédictions.**
```
ANCIEN: **Raisons.** V1 et V6 : une copie est une carte qui n'ajoute pas 0,01 nat au nul de K1
NOUVEAU: **Lecture des prédictions** : chacune est « confirmée » dans sa zone prédite, « réfutée » dans sa zone de réfutation, « indécise » entre les deux (V1 : k_R de 4 à 7 ; V2 : S_R de 0,25 à 0,55 ; V6 : médiane de 0,3 à 0,8), l'indécision étant rapportée telle quelle. **Raisons.** V1 et V6 : une copie est une carte qui n'ajoute pas 0,01 nat au nul de K1
```

**C-13 — Sensibilité sur le sens de la distance.**
```
ANCIEN: copie au sens de la distance globale seule ; mondes non complets réintégrés (au moins un appel répondu par moitié).
NOUVEAU: copie au sens de la distance globale seule ; copie au sens du minimum des deux sens ([V3] § 3.1) ; mondes non complets réintégrés (au moins un appel répondu par moitié).
```

**C-14 — Artefact de la ligne « partie A ».**
```
ANCIEN: | partie A : un verdict du juge de v67 lu, ou un seuil changé après sa lecture | partie A invalide ; partie B inchangée | lecture des seules lois | champ `promue` lu : refus |
NOUVEAU: | partie A : un verdict du juge de v67 lu, ou un seuil changé après sa lecture | partie A invalide ; partie B inchangée | lecture des seules lois | champ `promue` lu : refus ; ε modifié entre deux empreintes du programme : refus |
```

**C-15 — Graine du jeu public.**
```
ANCIEN: | jeu public porteur d'issues, ou tiré d'une graine qui dépend du monde ou du secret | arrêt ; défaut | jeu de `(r, 30)` sans issue | champ d'issue ajouté ; graine du secret : refus |
NOUVEAU: | jeu public porteur d'issues, ou tiré d'une graine qui dépend du contenu du monde ou du secret (l'indice r seul est permis) | arrêt ; défaut | jeu de `(r, 30)` sans issue | champ d'issue ajouté ; graine du secret : refus |
```

**C-16 — Graine de l'audit : clé écrite.**
```
ANCIEN: (graine dérivée de l'empreinte de `CARTES.json`), formes canoniques comprises ;
NOUVEAU: (`SeedSequence(entropy=empreinte de CARTES.json, spawn_key=(98, w))` par monde w), formes canoniques comprises ;
```

**C-17 — Arrêt sur un appel au-dessus du pire cas : règle à écrire d'après le pilote.**
```
ANCIEN: | coût d'un appel au-dessus de son pire cas | arrêt (code 3), dépense comptée | coût sous le pire cas | relevé de relais gonflé : arrêt |
NOUVEAU: | coût d'un appel au-dessus de son pire cas | arrêt (code 3), dépense comptée ; **règle du dépassement de la réflexion de Pr-1 fixée avant scellement d'après la réflexion mesurée au pilote (borne, ou dépassement toléré jusqu'à une valeur écrite, ou arrêt) : un seul appel ne doit pas rendre « non jugeable » 20 mondes payés sans que ce choix soit écrit** | coût sous le pire cas | relevé de relais gonflé : arrêt |
```

**C-18 — Section « Contre-lecture » : modèle du lecteur et entrées.**
```
ANCIEN: le rédacteur (modèle B ≠ A), qui n'a écrit ni ce texte, ni [NOTE], ni [PILOTE], ni le code du pilote.
NOUVEAU: le rédacteur (modèle C ≠ A ; un premier lecteur du modèle B s'est arrêté sans rapport, limite d'usage, R-2982), qui n'a écrit ni ce texte, ni [NOTE], ni [PILOTE], ni le code du pilote.
```
Entrée à ajouter par la mère à la section, sous « Contre-lecture 1 » : rapport `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-tour1-v1.md`, empreinte entière lue dans son compagnon `.sha256` ; brouillon relu `ec8d04962b570b97f16f49b289dfbb3e8b32fcb8468090fafb164434ed59678a` (les deux empreintes entières exigées par `prereg.py`).

**C-19 — Pièce 2611.04420 mal rangée.**
```
ANCIEN: ([CAT] C1, agent de proximité) ; et la pièce 2611.04420 citée par N-067, § 6 (N-058).
NOUVEAU: ([CAT] C1, agent de proximité) ; la pièce 2611.04420 (soumise, non publiée) est citée par N-067, § 6, pour les batteries de mutations d'un vérificateur (O11) et pour N-058, non pour les filtres de nouveauté : à lire sur PDF pour ce second point seulement.
```

**C-20 — Annexe A : renvoi à un brouillon qui sera remplacé.**
```
ANCIEN: l'annexe A du brouillon 1 du crible (iii), dans ce dossier (`crible-iii-brouillon1.md`) ; son empreinte est celle ci-dessus.
NOUVEAU: l'annexe A du brouillon 1 du crible (iii), dans ce dossier (`crible-iii-brouillon1.md`) ; son empreinte est celle ci-dessus. **À recopier en entier dans la version qui fera foi de ce texte (le brouillon (iii) sera remplacé), avec les calculs de C-02 et C-05.**
```

**C-21 — Audit de symétrie : conséquence écrite.**
```
ANCIEN: Dans tous les cas, même relecture écrite, par un
NOUVEAU: Dans tous les cas, même relecture écrite (**dont le résultat ne peut qu'ajouter une réserve, jamais changer le verdict de l'étage où il porte**), par un
```

### Remarques facultatives (aucune n'est exigée)

- R-1 : ε = 0,01 et ε_strat = 0,04 viennent de [V3] § 3.1 réglés sur un banc synthétique ([V3] § 1.8 : « réglés en v1 sur une sous-famille ») ; ils n'ont jamais été éprouvés sur de vraies cartes de proposeurs. Si la partie A montre une part de copies à 0 ou à 1 partout, c'est un signe sur ces seuils, non sur la règle : à écrire dans la lecture de la partie A, sans changer les seuils.
- R-2 : les clés de configuration `opus55` et `fable52` contiennent un nom de modèle ; la pièce dit « aucun identifiant de modèle ici » (R-2598). Elles sont gelées par l'empreinte de la configuration v12 et nécessaires aux lignes de GO (forme du pilote) : à laisser, ou à remplacer par « poste Pr-2 / Pr-4 » partout sauf dans les lignes.
- R-3 : le même arXiv 2609.17560 est « Pay Only for Disagreement » dans [CAT] et « DISCERN » dans N-067 ; à signaler dans la section « Antériorités ».
- R-4 : le placebo exige une énumération de C(n_c, k_R) ensembles : jusqu'à 2 704 156 pour 24 mondes (C(24, 12)) : sans objet pour le coût, à citer dans l'essai sain de la ligne « placebo ».

## Points pour la mère

1. **Date de lancement** : fixée par le code neuf (lanceur, mesure, lecture, partie A, procédure de machine) et par la fenêtre de GO (échéance 30 novembre ; prix de Pr-1 qui double le 1er décembre), non par le préenregistrement : fenêtre estimée de six à neuf jours. Dis-le à Lazar si la date compte.
2. **Risque « non concluant »** : si le taux d'appels répondus du pilote est bien celui des comptes de marche de R-2981 (14 sur 16), la définition actuelle de « monde complet » (quatre appels sur quatre) rend le crible presque sûrement « non concluant », même à 24 mondes. À trancher avant scellement (C-02) après la lecture de l'issue du pilote.
3. **Le crible n'éprouve probablement pas la règle** (V1 : k_R ≤ 3, confiance 0,65, par l'auteur) mais l'ablation : tel qu'il est, il répond surtout à QO1. Le bras à archive enrichie avec appels reste refusé (R-2977) ; les deux lectures sans appel de C-06 le remplacent en partie.
4. **Écarts à des textes scellés ou à confirmer** : (a) l'étage 5 (ablation) entre aux critères gelés de (v), alors que N-045 point 3 la dit « rapportée, hors des critères gelés » : R-2977 ne le tranche que pour (iii) ; (b) la règle de composition à l'exécution comme « essayée, non adoptée » par GO-2026-11-15-06 : lecture de la pièce, qui demande la confirmation de la mère ; (c) sens de la distance : écart déclaré à [V3] § 3.1, accepté avec la sensibilité de C-13.
5. **Enveloppe de GO-2026-11-15-06** : (v) à 196,60 au lieu de 183,00 (plafonds de 2,34) ; les mêmes plafonds touchent les trois autres cribles ; la somme des cinq n'est pas tenue d'office à 1 275 : refaire le compte d'ensemble avant les lignes. Part sur crédits de Claude : ≈ 50 % (prix publics) et non 65 % ; seuls Pr-2 et Pr-4 le peuvent (configuration v12).
6. **Mot de Lazar** : adoption de la règle dans l'organisme, et au-delà de la génération 1 la dépendance indirecte aux verdicts du juge (N-058) : nœuds de Lazar, déjà dits dans la pièce. Aucun mot de Lazar n'est nécessaire pour corriger la pièce.

## Vérification des « ancien »

Contrôle (lecture seule, bibliothèque standard, `python3 -I`, 13:34:13Z) : 31 lignes « ANCIEN » de ce rapport, chacune trouvée **exactement une fois** dans la pièce (`ec8d0496…`) ; 0 défaut. Le contrôle ne vérifie pas que les remplacements se recoupent : les 31 ancrages sont sur des lignes distinctes.
