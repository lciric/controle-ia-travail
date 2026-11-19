# Contre-lecture R2 du brouillon 6 du papier C — lentille « texte et conformité » — v1

- **Qui** : relecteur neuf (R2), sous-agent de la session 16. Je n'ai écrit ni les brouillons 1 à 6, ni leur
  configuration, ni aucune contre-lecture, note de voisins, projet de traitement ou traitement du papier C.
- **Heures** : le 2026-10-21, de 01:07 à 01:25 UTC environ (`date -u`).
- **Consigne** : `…/consigne-contre-lectures-brouillon6-v1.md`
  (`08c1acdbd115521425ac50b2699ddbeeed2a2d5b37e6157255e5ff214e4c2899`, égale à son compagnon) : partie commune et lentille
  « texte et conformité », point CW-04 compris. La lentille « vérification courte de méthode » est confiée à un autre
  relecteur.
- **Préfixe** `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; `R` =
  `/home/user/controle-ia-travail`, lu en lecture seule.

## Pièces (empreintes recalculées, toutes égales à leur compagnon `.sha256`)

| pièce | empreinte | lecture |
|---|---|---|
| brouillon 6, `…/brouillon6/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md` | `fadc74c3b40b6e6aee9035f5a9566288d17d60b8403b57863721c2ee57554d00` | en entier (1 433 lignes) |
| configuration brouillon 3, `…/brouillon6/papier-C-config-v1-brouillon3.json` | `85173b22defe2c55844f23691028233a13746394324d0c598d3a66fb4f68820d` | structure, nombres, champs de règles (masqués s'ils recoupent un texte de formulation) ; vivier par indices et comptes seulement |
| table, `…/brouillon6/table-traitement-brouillon6-v1.md` | `74b5ae16e322b74340f793253af9387680ba370512fe5e9b8477a742d4d2f370` | en entier |
| sortie `…/brouillon6/problemes-brouillon6-v1.txt` ; outils `…/brouillon6/travail/` (4 fichiers et compagnons) | compagnons conformes (`sha256sum -c`) | sortie en entier ; outils : empreintes seulement |
| traitement de la session, `…/traitement-contre-lectures-brouillon5-papier-C-v1.md` | `08ca42ae7bd70a08a3695aca66ba0d16ee175da1771ba2c37ed6eda20cceb00e` | en entier |
| projet, `…/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md` | `c65aa83acb830c765b9bc4cee7f600d45708771eef12de0502237a4234d42d25` | en entier |
| consigne du rédacteur, `…/consigne-redacteur-brouillon6-v1.md` | `dc25318d64fb9fffc2f1ce911f66ed9df3f1b0120bf8e74f07ad237b93e45753` | en entier |
| rapports et notes sous `…/contre-lectures-brouillon5/` : texte `12879073…`, méthode `0c492f02…`, Joswin et Hu et Qu `55222cdb…`, sept de Panin `b3a6c187…`, second rang `8027bd53…`, CP-02 `abbb5aaa…`, restants `83e8f49b…`, contre-lecture courte `7287498f…`, CV2-03 `9d94ae66…` ; vérification du verrou `0cbd3ae3…` | tous conformes | lignes de constats et de corrections |
| base : brouillon 5 `9d55160f…`, configuration brouillon 2 `77252564…`, table du brouillon 5 `ebb763fa…` | conformes | comparaison mécanique |
| `R/registres/decisions.md` (R-307, R-308, R-309, R-312, P-019 à P-022) ; `R/registres/go.md` (GO-2026-10-20-13, -14) ; `R/brouillons/…-brouillon3.md` (`3cc25dcd…`, égale au texte) ; `R/src/controle_ia/prereg.py` (`3b2e3ee5…`) | — | lignes citées |

## Ce que j'ai tenu ; écarts

- Écriture seulement sous `…/contre-lectures-brouillon6/texte/` (ce rapport, son sceau ; essais sous `essais/`, avec un
  manifeste). Aucun réseau, aucun sous-agent, aucune dépense, aucune clé affichée, aucune commande git d'écriture
  (une lecture : `git log -1` sur `CLAUDE.md`, pour dater l'empreinte citée). `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.
- Aucune recherche récursive : dossiers nommés listés un à un ; `grep` sur des fichiers nommés.
- Non lus, pas même pour une empreinte : `R/prereg/P3-consignes-v1.md`, tout `textes-actions-*`,
  `items-textes-p1-v1.json`, `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/` (mon script
  d'empreintes les saute par motif : `essais/chemins_empreintes_b6_v1.py`).
- Configuration : aucun texte de formulation, de témoin, de fente, de consigne ni de paragraphe de bras affiché ni
  recopié. Les champs de règles (statut, `stabilite_rang`, `constat_nu` hors gabarit, `etape2`, graines…) ont été
  affichés à travers un filtre qui masque tout champ recoupant un texte sensible sur 12 caractères (deux champs masqués,
  contrôlés par booléens). Le vivier n'a été lu que par comptes de classes de mots, par indice.
- Écart : un masquage de contrôle passé sur mes sorties d'essai (`essais/masquer_sorties_v1.py`) a remplacé aussi des
  morceaux anodins (faux positifs) ; aucune conclusion n'en dépend. La sortie rejouée de `problemes` a été refaite sans
  masque.

## Verdict

**Scellable après corrections.**

Le brouillon 6 applique le traitement de la session avec soin. Contrôle mécanique des « mots exacts » : 139 segments de
corrections (≥ 50 caractères) cherchés dans le texte ; tous les absents s'expliquent (ancien texte remplacé, citation
d'un papier, correction elle-même modifiée par un constat ultérieur, marqueur rempli, renumérotation 14 → 15 ou 16) ; les
écarts restants sont ceux que la table déclare. Les décisions de Lazar R-307 (ajouts 2 et 3) et R-309 (déclaration ;
repli au verrou 7) sont écrites mot pour mot ; P-020, P-021 et P-022 restent en attente, jamais tranchées, avec leurs
marqueurs (6, 2 et 7). Les énoncés de HC1 à HC3 sont inchangés depuis le brouillon 3. La sortie de `problemes`, rejouée,
est identique octet pour octet à celle versée. Les 111 paires « chemin, empreinte » vérifiables du texte sont toutes
égales sur disque ou dans les manifestes (aucun écart). Configuration : vivier, témoins, fentes, consignes, contenus
neutres, insertion, gardes, juges, graines, longueurs et paragraphes de bras égaux au brouillon 2.

Un constat majeur bloque : les versions de repli (B) et (C) de P-021 ne se lisent pas seules ; si Lazar retient l'une
d'elles, le texte scellé renverrait à un passage retiré (CB6-texte-01). Les autres corrections sont mineures ou de forme.

**Réponse à la question de la contre-lecture 9 (R-309)** : la déclaration de la réserve 14 suffit ; le repli (b) n'est
pas déclenché. Aucune ligne de C-P1 à C-P6 ne lit l'étiquette ; le vivier n'a pas à changer. Une phrase de lecture manque
seulement : la contingence occupe les rangs hauts de la famille 1, donc « intensités graduées » et g_{k_f} s'y lisent
« par formulation entière », comme pour la réserve 16 (CB6-texte-04).

**Point CW-04** (détail en CB6-texte-03) : oui, la personne grammaticale change avec l'indice dans trois familles
(« flatterie et supplication », « usurpation stylistique », « ordres en bande ») ; elle est constante dans
« revendication d'autorité » (première personne aux seize indices) et dans « approbations forgées » (troisième
personne). Rien ne le déclare au texte.

## Constats

### CB6-texte-01 — majeur — P-021 : les versions de repli (B) et (C) ne se lisent pas seules

- **Où** : verrou 1 (l. 99-104) ; Prédiction, bloc P-021 (l. 542-576 ; repli (B) l. 568-571, repli (C) l. 573-576) ;
  Critères de lecture gelés (l. 1254-1270 ; (B) l. 1265-1266) ; Seuil, C-P3 (l. 841-844) ; configuration
  `stabilite_rang.decision`, `stabilite_rang.repli_si_refus.B` et `.C`.
- **Ce qui est** : le verrou 1 dit « sous chaque marqueur, une seule version reste au texte scellé ; les autres sont
  retirées ». Sous (B) ou (C), la version recommandée part donc avec son tableau (grandeurs de C-P3a, C-P3b, C-P3c ;
  seuils de C-P3a et C-P3c) et ses paragraphes « Deux lectures », « Clause de repli mécanique » et « Sans le bras … ».
  Or (B) dit « C-P3a et C-P3c comme ci-dessus (deux lectures et clause de repli comprises) », (C) dit « les statistiques
  ci-dessus », et (B) des critères dit « C-P3a et C-P3c comme ci-dessus ». Le texte scellé renverrait à un passage
  retiré : C-P3a et C-P3c n'auraient ni définition ni seuil (R1). Même défaut dans la configuration :
  `stabilite_rang.decision` retire `lecture_recommandee` sous (B) ou (C), alors que `repli_si_refus.B` dit « C-P3a et
  C-P3c comme en (A) ». La consigne du rédacteur demandait des replis « prêts à remplacer en mots exacts ». Le même schéma
  était au brouillon 5 (P-019) ; il n'avait pas été relevé.
- **Ce qui devrait être** : chaque version se lit seule après le retrait des autres, ou le verrou 1 dit quels passages
  de la version recommandée restent.
- **Correction (mots exacts)** :
  1. Verrou 1, après « tant qu'il en reste un, `problemes` refuse le scellement. », ajouter : « Exception, P-021 : sous
     (B), les deux tableaux de la version recommandée (sections « Prédiction » et « Critères de lecture gelés ») et ses
     paragraphes « Deux lectures », « Clause de repli mécanique » et « Sans le bras … » restent au texte scellé, sans
     en-tête ni marqueur, leur ligne C-P3b étant remplacée par la version (B) ; sous (C), seul le tableau de la section
     « Prédiction » reste, réduit à ses colonnes « id » et « grandeur », avec le paragraphe « Deux lectures » et la
     phrase « Sans le bras … ». »
  2. Prédiction, (B) : remplacer « C-P3a et C-P3c comme ci-dessus (deux lectures et clause de repli comprises) ; » par
     « C-P3a et C-P3c comme au tableau de la version recommandée, gardé (verrou 1), deux lectures et clause de repli
     comprises ; ».
  3. Prédiction, (C) : remplacer « les statistiques ci-dessus (W de C-P3a, » par « les statistiques définies à la
     colonne « grandeur » du tableau de la version recommandée, gardé (verrou 1) (W de C-P3a, ».
  4. Critères, (B) : remplacer « C-P3a et C-P3c comme ci-dessus ; » par « C-P3a et C-P3c comme au tableau de la version
     recommandée, gardé (verrou 1) ; ».
  5. Seuil, C-P3 : remplacer « seuils et lectures du bloc P-021 (section « Prédiction ») ; » par « seuils et lectures
     du bloc P-021 (section « Prédiction »), selon la version retenue ; ».
  6. Configuration, `stabilite_rang.repli_si_refus.B` : « C-P3a établie si p exact ≤ 0,05 et p par rééchantillonnage
     centré ≤ 0,05 ; C-P3c établie si p exact ≤ 0,05 ; aux deux lectures (deux_lectures) ; clause_repli applicable ;
     sinon non établie ; aucune réfutation ; C-P3b rapportée sans verdict (τ des écarts intra-famille et τ des quinze
     valeurs, avec leurs valeurs p) » ; `stabilite_rang.repli_si_refus.C` : « C-P3a, C-P3b, C-P3c (champs C_P3a, C_P3b,
     C_P3c) rapportées sans verdict, aux deux lectures, avec leurs valeurs p ; clause_repli sans objet ».

### CB6-texte-02 — mineur — P-022 : les replis sont écrits comme des consignes de retrait

- **Où** : Métrique, point 5 (l. 700-701) ; Plan, TC.1 (l. 1036-1043) ; réserve 9 (corps l. 1151-1155 ; blocs
  l. 1163-1165).
- **Ce qui est** : point 5, (a) ou (c) : « Aucune condition « constat nu » : le paragraphe qui précède est retiré. » ;
  TC.1, (a) : « le paragraphe qui précède et celui du point 5 de la « Métrique » sont retirés » ; (c) : « Comme (a) » ;
  réserve 9 : « La parenthèse … suit la version recommandée (b). » et « Elle se lit « (réserve 16) ». ». Avec la règle
  du verrou 1 (seule la version retenue reste, en-tête et marqueur retirés), ces phrases resteraient au texte scellé et
  renverraient à des passages absents ; sous (a) ou (c), la parenthèse de la version (b) resterait dans le corps de la
  réserve 9, hors de tout marqueur.
- **Ce qui devrait être** : chaque version de repli est la phrase même du texte scellé.
- **Correction (mots exacts)** :
  - Point 5, (a) ou (c) : remplacer « Aucune condition « constat nu » : le paragraphe qui précède est retiré. » par
    « Aucune condition « constat nu » n'est lue (décision de Lazar P-022, option (a) ou (c)). »
  - TC.1, (a) : remplacer « Aucune condition « constat nu » : le paragraphe qui précède et celui du point 5 de la
    « Métrique » sont retirés ; » par « Aucune condition « constat nu » n'est lue (décision de Lazar P-022, option (a)) ; ».
  - TC.1, (c) : remplacer « Comme (a) ; de plus, » par « Aucune condition « constat nu » n'est lue ici (décision de
    Lazar P-022, option (c)) ; la réserve 16 reste seule ; C-P6 (juges) se lit « usurpation stylistique portant un
    constat », sans attribution au style ; champ `constat_nu` retiré de la configuration scellée ; ».
  - Réserve 9, corps : remplacer « (réserve 16 ; le contraste « style contre contenu » est Ḡ_4 − g_constat, Plan, TC.1). »
    par « (réserve 16). » ; bloc recommandé : remplacer « La parenthèse « (réserve 16 ; le contraste « style contre
    contenu » est Ḡ_4 − g_constat, Plan, TC.1) » suit la version recommandée (b). » par « Le contraste « style contre
    contenu » est Ḡ_4 − g_constat (Plan, TC.1). » ; bloc de repli : remplacer « Elle se lit « (réserve 16) ». » par
    « Aucun contraste « style contre contenu » n'est mesuré dans ce texte. »

### CB6-texte-03 — mineur — CW-04 : la personne grammaticale change avec l'indice dans trois familles, sans déclaration

- **Où** : configuration `$.vivier.*` ; Plan, « Familles et échafaudage » (l. 1067-1083) ; réserves (section 7) ; table,
  ligne CW-04 (« à vérifier par la session sur le vivier »).
- **Méthode** (par indices, sans texte) : `essais/personne_grammaticale_vivier_v2.py`
  (`49f96efbeff7d06fa6fcfa55635126e7dd5a99ab5c81e03a27d78c9c0390bcd2`), sortie
  `essais/personne_grammaticale_vivier_v2.sortie.txt`
  (`9a2a36547df8a53bd76663f95eb274addde4df4487e023bf1959105925427189`) ; version 1 à côté. Pour chaque formulation remplie
  (corpus A et B, mêmes résultats), comptes de pronoms de première, deuxième et troisième personne, de noms de personne
  ou de rôle (listes fixes), d'impératifs en tête de phrase et de « please ». Code par indice : 1 = première personne,
  2 = deuxième (pronom, impératif ou « please »), 3 = troisième (pronom ou nom de personne autre que le lecteur),
  « … » = impersonnel. Limite : listes de mots, pas d'analyse syntaxique ; un nom de rôle absent de la liste passe pour
  impersonnel.
- **Ce qui est**, par famille et indice :
  - « flatterie et supplication » : 1 et 2, deuxième personne seule (aucune première personne) ; 3 à 5 et 7 à 15,
    première et deuxième ; 6, première seule ; 16, première, deuxième et troisième (le lecteur est aussi nommé à la
    troisième personne aux indices 8, 10, 13 et 16). **Change avec l'indice** (le locuteur se nomme à partir de 3).
  - « revendication d'autorité » : première personne aux seize indices ; des tiers nommés de 4 à 16 (sauf 8), sans
    changement de la personne du locuteur. **Constante.**
  - « approbations forgées » : troisième personne (approbateurs) à tous les indices, sauf 3 (aucun nom de personne
    repéré). **Constante**, à l'indice 3 près. (La version 2 range les noms de relecteur dans la classe « lecteur » :
    les indices 4, 5, 6 et 8 y perdent leur « 3 » ; dans cette famille, ce sont des approbateurs, comptés en version 1.)
  - « usurpation stylistique » : impersonnelle de 1 à 5 ; attribution à un rôle nommé (troisième personne) de 6 à 16.
    **Change avec l'indice** (rupture entre 5 et 6, juste après le début du constat, indice 5).
  - « ordres en bande » : adresse directe au lecteur (impératif) à 1 à 3 et 6 à 11, 13 à 16 ; aux indices 4, 5 et 12,
    aucune adresse directe : le lecteur est désigné à la troisième personne (avec un modal d'obligation à 5 et 12) ;
    deuxième personne explicite (pronom) à 10, 11 et 13 à 16 ; tiers nommés à 10 et 13 à 16. **Change avec l'indice.**
  - Témoins : impersonnels de 1 à 15 ; un nom de personne à 16.
  Le rang d'intensité suit le gain au pilote (ḡ_sép), qui croît d'ordinaire avec l'indice : dans ces trois familles, la
  voix est confondue avec l'intensité. Wang K. et al. trouvent qu'à expertise et opinion constantes, passer à la
  troisième personne déplace fortement l'accord de modèles qui répondent (note `9d94ae66…`, CW-04 ; p. 12, tableaux 2
  et 3). Rien ne le déclare au texte ; la réserve 16 déclare le même type de confusion pour le constat.
- **Ce qui devrait être** : la personne par indice est déclarée comme étiquette descriptive, avec sa conséquence de
  lecture (R4, R8). Vivier inchangé : le changer serait un nœud.
- **Correction (mots exacts)**, après confirmation par la session (par un second contrôle par indices, si elle le
  juge utile) ; Plan, section 7, après la réserve 16, ajouter : « 17. **Personne grammaticale et indice** (CW-04 de la
  note `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-cv2-03/lecture-voisins-cv2-03-v1.md`, `9d94ae66…` ;
  comptes par indices, sans texte : `docs/notes/contre-lectures-papier-C-v1/brouillon6/texte/personne_grammaticale_vivier_v2.sortie.txt`,
  `9a2a36547df8a53bd76663f95eb274addde4df4487e023bf1959105925427189`) : dans trois familles, la personne grammaticale
  change avec l'indice du vivier. « Flatterie et supplication » : deuxième personne seule aux indices 1 et 2, première et
  deuxième personne de 3 à 16 (première seule à l'indice 6). « Usurpation stylistique » : voix impersonnelle de 1 à 5,
  attribution à un rôle nommé de 6 à 16. « Ordres en bande » : adresse directe au lecteur, sauf aux indices 4, 5 et 12,
  où le lecteur est désigné à la troisième personne ; deuxième personne explicite à 10, 11 et 13 à 16. « Revendication
  d'autorité » : première personne aux seize indices ; « approbations forgées » : troisième personne ; témoins : voix
  impersonnelle. Un indice de voix, sans ordre, déplace la déférence de modèles qui répondent (Wang K. et al.,
  2508.02087v4, p. 12, tableaux 2 et 3) : dans ces trois familles, Ḡ, g_{k_f} et « intensités graduées » se lisent
  « par formulation entière » (réserve 16) ; aucune part n'est attribuée à l'intensité seule. La personne de chaque
  formulation retenue est écrite au rapport de l'étape 2 comme étiquette descriptive, jamais comme facteur ni comme
  critère. Vivier, constantes et longueurs inchangés. » Table de traitement : ligne CW-04, « appliqué (réserve 17) ».
  Verrou 5 : verser `essais/` de ce rapport sous `docs/notes/contre-lectures-papier-C-v1/brouillon6/texte/`.

### CB6-texte-04 — mineur — réserve 14 : la déclaration suffit, mais sa lecture n'est pas dite

- **Où** : réserve 14 (l. 1180-1194) ; verrou 7 (l. 190-192) ; contre-lecture 9 (l. 1429-1431).
- **Ce qui est** : la réserve 14 reprend mot pour mot le projet (section 2.2), conforme à R-309 et à R-307 (ajout 3) :
  indices, étiquette descriptive, cas limites, « jamais comme facteur ni comme critère », effet réservé au complément.
  Aucune ligne de C-P1 à C-P6, aucun audit ni aucune règle de l'addendum ne lit l'étiquette (vérifié à la lecture). Le
  repli (b) n'est donc pas nécessaire : rien ne dépend de la contingence, et le vivier n'a pas à changer. Mais la réserve
  dit elle-même que la contingence occupe le haut de l'échelle de la famille 1 (14 à 16) et 13 à 16 de « ordres en
  bande ». Le choix par cibles étalées retient d'ordinaire le haut de l'échelle : g_{k_f}, « intensités graduées » et Ḡ
  de ces familles mêlent l'intensité et la contingence. Le texte ne dit pas comment les lire (la réserve 16 le dit pour
  le constat).
- **Ce qui devrait être** : la même règle de lecture que la réserve 16, sans facteur ni critère.
- **Correction (mots exacts)** : réserve 14, après « à côté de chaque formulation retenue qui la porte. », ajouter :
  « Comme la contingence occupe les rangs hauts de la famille « flatterie et supplication » et les indices 13 à 16 de
  « ordres en bande », Ḡ, g_{k_f} et « intensités graduées » de ces familles se lisent « par formulation entière » (même
  règle que la réserve 16) : aucune part n'en est attribuée à la flatterie ou à l'ordre seuls. »

### CB6-texte-05 — mineur — constat nu : une variante ouverte par le traitement est fixée au texte sans marqueur

- **Où** : Plan, TC.1, bloc P-022 (l. 1031-1032 : « Non lue au pilote ») ; point 1.4 (l. 927-928) ; configuration
  `constat_nu.pilote` ; table, ligne CV-01 (b) (« variante du projet non tranchée par la session : laissée à la
  session »).
- **Ce qui est** : le projet (section 4.2, option (b)) laissait à la session la variante « lire l'insertion au point 1.4,
  hors du choix des formulations, pour la lisibilité seulement ». Le texte et la configuration écrivent « non lue au
  pilote », sans marqueur ni ligne au verrou 1 ; `problemes` ne verra pas que la question reste ouverte. Conséquence :
  sous (b), l'insertion du constat nu n'est jamais lue avant l'étape 2 ; sa masse n'y est contrôlée qu'à l'étape 2,
  où plus de 5 % d'anomalies de masse arrêtent la lecture d'un juge × consigne (liste d'arrêt 6).
- **Ce qui devrait être** : la session tranche (routine) et le texte le dit, ou un marqueur garde la question ouverte.
- **Correction (mots exacts)**, si la session retient la lecture au pilote (ma recommandation : une lecture de plus par
  contenu de calibrage et par juge) : point 1.4, après « La lisibilité est revérifiée sur toutes ces lectures ; échec :
  nœud. », ajouter « Sous P-022 (b), l'insertion du constat nu (corpus A) est lue aussi, sur les mêmes contenus, pour la
  lisibilité seulement ; ces lectures n'entrent ni dans les gains du vivier ni dans l'addendum. » ; bloc P-022 de TC.1,
  remplacer « Non lue au pilote ; elle n'entre pas dans le choix des formulations. » par « Lue au pilote pour la
  lisibilité seulement (point 1.4) ; elle n'entre pas dans le choix des formulations. » ; `constat_nu.pilote` à
  l'avenant. Si la session garde « non lue » : écrire sa décision au registre et ajouter, au bloc P-022 de TC.1, « (décision
  de la session, `<ligne du registre>`) ».

### CB6-texte-06 — forme — liste d'arrêt 11 : l'insertion du constat nu n'y est pas

- **Où** : liste d'arrêt 11 (l. 1327-1328) ; point 17 et bloc P-022 de TC.1 (gardes appliquées au constat nu).
- **Ce qui est** : « Garde lexicale en échec sur une formulation ou un témoin : arrêt ». Sous (b), le constat nu est une
  insertion soumise aux gardes, mais n'est ni une formulation ni un témoin.
- **Correction (mots exacts)** : remplacer « Garde lexicale en échec sur une formulation ou un témoin : » par « Garde
  lexicale en échec sur une formulation, un témoin ou l'insertion du constat nu (bloc P-022) : ».

### CB6-texte-07 — forme — trois phrases à reprendre

- Graines (l. 1105-1106), phrase reprise du brouillon 5 : « Clés ajoutées par ce brouillon : » ; le brouillon 6 n'ajoute
  aucune clé (table, E-07 ; configuration, `graines` égal au brouillon 2). Écrire « Clés ajoutées par le brouillon 5 : ».
- Champs du scellement (l. 203-206) et configuration `statut` : « `stabilite_rang` (…) et `agent_bras` (…), et
  `constat_nu` (…) ». Écrire « `stabilite_rang` (…), `agent_bras` (…) et `constat_nu` (…) » (même correction aux deux
  endroits, sans autre changement).
- Réserve 14 (l. 1192) : « Vivier, configuration, constantes et longueurs inchangés. » La configuration du brouillon 3
  change (pour d'autres constats). Écrire « Vivier, constantes et longueurs inchangés ; configuration inchangée par
  cette déclaration. »

### CB6-texte-08 — information — points pour la session

- Registre : la ligne P-020 porte encore « 2026-10-22 21:15 » et « à transmettre à Lazar » ; R-312 dit la transmission
  du 2026-10-21 vers 00:30 UTC et le défaut du 2026-10-23 vers 00:30 UTC, que le texte suit (verrou 1 ; bloc P-020). Les
  lignes ne se réécrivent pas (R12) : le bloc P-020 peut citer R-312 à côté de P-020.
- `<<DECISION_VOISINS>>` : le rédacteur a ajouté Jiang et al. et Wang K. et al. aux « cités comme publiés » (table,
  E-05) ; la ligne de décision de la session doit porter ces deux noms.
- CR2-03 : le texte dit seulement la décision écrite de la session (amendement 3 : écart « noté, sans effet sur le
  contenu ») ; la table ajoute « la session confirme qu'elle vaut pour la lecture du corps », sans pièce écrite. Une ligne
  au registre suffit.
- Copie publique : le point 5 cite en entier, pour les deux corpus, l'insertion remplie du constat nu, et la réserve 16
  cite sa forme à fentes. La décision de Lazar sur la copie expurgée (`scripts/depot_expurge.py`) doit dire si les
  textes d'insertion en sortent.
- Verrou 5 : `construire_brouillon6_v1.py` et son journal (`…/brouillon6/travail/`), qui ont produit le texte, ne sont
  pas dans la liste des versements ; à verser pour la provenance, comme `ecrire_config_brouillon3_v1.py`.

### CB6-texte-09 — information — ce qui a été vérifié et tient

- Table : un constat par ligne pour les 106 constats des dix pièces (texte 16, méthode 16, Joswin et Hu et Qu 11,
  Panin 10, second rang 10, vérification 3, CP-02 11, restants 12, contre-lecture courte 8, CV2-03 9) ; les « non
  appliqués » le sont à bon droit (session, veille, information, constat remplacé ou levé par une lecture faite :
  CV-02, CV2-01, CV2-03 ; CV2-05 vise une citation absente du texte ; CS-06 et VF-03 écartés par le projet).
- Mots exacts : `essais/mots_exacts_b6_v1.py` et `essais/mots_exacts_b6_ecarts_v1.py` (sorties à côté) ; puis lecture
  directe de chaque correction de CL5-01 à CL5-12, texte-01 à texte-11, CV-01 à CV-08, CP-01 à CP-06, CS-01 à CS-05,
  CQ-01 à CQ-06, CR2-01 à CR2-07 et CR2-09, CV2-02, CV2-04, CW-01 à CW-04, CW-08 : présentes, aux places dites ; écarts
  tous déclarés (renumérotation des réserves, marqueurs remplis par E-03, ponctuation, majuscule de CS-03).
- Décisions de Lazar : clause d'ouverture, phrase de la section 5, réserve 14, verrou 7, ligne « Décisions » des champs
  et puce « Contingence » : présentes mot pour mot (`essais/decisions_lazar_b6_v1.sortie.txt`). Aucun verrou « famille 1
  sans contingence ». GO-2026-10-20-13 et -14 cités (GO ; documents). P-020, P-021, P-022 : version recommandée en texte
  principal, défauts et heures conformes au registre (R-312, P-021, P-022), aucune tranchée ; configuration « en
  attente » dans les trois champs de décision.
- Énoncés : les lignes d'énoncé de HC1, HC2, HC2b et HC3 (composantes 1 et 2, jusqu'au point final de l'énoncé) sont
  égales au brouillon 3 (`essais/enonces_b3_b5_b6_v1.sortie.txt`) ; seuls les précédents cités s'allongent.
- `problemes` : rejoué, sortie identique à celle versée (`essais/problemes_rejoue_b6_v1.txt`) ; marqueurs restants :
  ceux du scellement, des contre-lectures 7 à 9 et des trois décisions en attente.
- Configuration : chemins changés par rapport au brouillon 2 limités aux règles annoncées (E-07 ;
  `essais/diff_config_b2_b3_v1.py`) ; réserve 16 : indices de la fente {QUALITE} recomptés, égaux au texte
  (`essais/indices_fentes_vivier_v1.sortie.txt`) ; constat nu : longueurs 39 et 23, témoin d'indice 4 (écart 6), aucune
  garde déclenchée, recalculés.
