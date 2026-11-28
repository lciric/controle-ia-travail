# Vérification courte du brouillon 4 de P3b (les deux lentilles) — v1

- **Qui** : sous-agent neuf (Claude), vérificateur R2. Je n'ai écrit ni P3b (brouillons 1 à 4, devis, plans, questions,
  tables), ni P3, ni aucune contre-lecture, vérification, projet de traitement ou traitement.
- **Heures (UTC, `date -u`)** : 2026-10-21, de 02:33 à 03:05 environ.
- **Notations** : `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b` ; `R` =
  `/home/user/controle-ia-travail` (lecture seule, commit `72ab8c1`). « l. » renvoie au texte du brouillon 4.
  VCm-NN / VCt-NN = constats des vérifications courtes « méthode » / « texte » du brouillon 3 ; VCB4-NN = constat de ce
  rapport.
- **Consigne** : `…/consigne-verification-courte-P3b-brouillon4-v1.md`
  (`05c824a1294445f7e67994b611416a45f42c171f1037020bf3bf5f505e5ef4f5`, égale à son compagnon).
- **Pièces lues** (empreintes vérifiées par `sha256sum -c` contre leurs compagnons : toutes conformes) :
  - relu : `…/brouillon4/P3b-seconde-lecture-v1-brouillon4.md`
    (`a46c1cfdaea816c904f06ee5d9dcd902cc0faed8cdc04d21b9af1607db463455`, en entier) ; `devis-P3b-v4.md` (`6a5cd174…`) ;
    `plan-code-et-chaine-P3b-v4.md` (`85b31dab…`) ; `questions-ouvertes-P3b-v4.md` (`74770b92…`) ;
    `table-traitement-brouillon4-v1.md` (`080e1888…`, en entier) ; `problemes-brouillon4-v1.txt` (`fd8e506d…`) ;
    `travail/` (script de remplacements, journal, sortie de `problemes`, contrôle du repli (B) de P-023, essai 1 : liste) ;
  - base : `…/brouillon3/` (texte `9430e359…`, devis `3dc920f8…`, plan `d950e428…`, questions `aff0a7ed…`, table
    `89e67f7f…`) ;
  - constats à trouver appliqués : `…/verification-courte-brouillon3/methode/verification-courte-P3b-brouillon3-methode-v1.md`
    (`66165ba5…`) et `…/verification-courte-brouillon3/texte/verification-courte-P3b-brouillon3-texte-v1.md` (`2c77870f…`),
    en entier ; consigne du rédacteur du brouillon 4 (`…/consigne-redacteur-P3b-brouillon4-v1.md`) ;
  - validateur `R/src/controle_ia/prereg.py` (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`, égal à celui
    que cite le brouillon), lu (fonction `problemes`) et exécuté.
- **Ce que j'ai tenu** : jamais ouvert `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous
  `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`, pas même pour une empreinte ; ni la contre-lecture « méthode » du
  brouillon 1, ni l'addendum 2 de P3, ni R-303 ; aucune ligne de `R/registres/`. Aucune recherche récursive ; aucun calcul
  sur les données de P3 ; aucun réseau ; git en lecture seule (`log -1`) ; aucun sous-agent, aucune dépense, aucune clé ;
  Python par `python3 -B` (`-I` pour mes scripts) avec `PYTHONDONTWRITEBYTECODE=1`. Écriture : ce rapport, son sceau et le
  dossier `essais/` seulement.
- **Mon exposition (R1)** : par le texte relu, l'issue qualitative du verdict complété de P3 et la mention (sans valeur) de
  l'aire du coût écrit seul. Aucune valeur de T1 à T4 de P3, aucune aire de P3-P3, ni le signe de P3-P2. **Ce rapport ne
  recopie aucune grandeur de P3.**
- **Essais** (sous `essais/`, textes produits en mémoire seulement, rien d'autre écrit) :
  `rejouer_brouillon4_v1.py` (`76e78c3f…`) ; `options_p3b_brouillon4_v1.py` (`4bb0b364…`) et sa sortie
  `sortie-options-p3b-brouillon4-v1.txt` (`985195c4…`) ; `ordre_v1.py` (`ac16e11d…`) ; `un_cas_v1.py` (`5ea1c4a4…`) ;
  `ctx_v1.py` (`cfd7e3f4…`) ; `garde_scellement_v1.py` (`b643526a…`) ; `anciens_textes_v1.py` (`47dc4289…` : chaque
  « ancien texte » des corrections ci-dessous est trouvé une seule fois, blancs réduits).

## Verdict

**scellable après corrections**

- Vérification 1 : les 17 constats (8 « méthode », 9 « texte ») sont appliqués, en mots exacts ou avec des écarts déclarés
  et justes ; les trois fusions déclarées sont justes (VCm-01 avec VCt-04 (3) ; VCm-02 avec VCt-09, motifs de VCm-02 et
  clause du repli dans la forme de VCt-09, qui donne le résultat que VCm-02 écrit sans double blanc ; VCm-08 (1) avec
  VCt-02 (1)). Titres « — v4 » au lieu de « — v3 » (VCt-08) : écart juste (R12).
- Vérification 2 : le script du rédacteur, rejoué en mémoire sur le brouillon 3 (heure fixée à « 02:30 », celle du journal),
  redonne **octet pour octet** le texte, le devis, le plan, les questions et le journal du brouillon 4 ; 63 remplacements,
  chacun trouvé une seule fois ; chacun porte un constat ou un changement déclaré à la table. Rien d'autre ne change.
  Sortie de `problemes` rejouée (2026-10-21T02:48Z) : identique à `travail/sortie-problemes.txt` et à la dernière ligne de
  `problemes-brouillon4-v1.txt`.
- Vérification 3 (test mécanique des options) : **972 combinaisons** essayées, chacune dans deux ordres d'application et
  sous deux lectures. Aucune ne laisse « en attente » ni « de repli » (blancs réduits, casse ignorée) ; aucune ne donne
  d'erreur nouvelle de `problemes` ; aucune version ne manque de chaîne à remplacer. Mais **aucune combinaison n'est sans
  défaut** : la partition est écrite deux fois dans toutes (VCB4-04) ; hors ce défaut, 18 combinaisons sur 972 sont
  propres, dont celle des recommandations. Les replis de P-016 (B), N-032 (A) et (B), P-024 (B) et (C), P-023 (B) et (C)
  laissent des phrases contradictoires ou orphelines, et N-031 (b) ou (c) avec P-023 (B) dépend de l'ordre d'application.
- Vérification 4 : la garde décrite au plan refuse bien les chaînes coupées par un retour à la ligne (essai : 7 artefacts
  refusés, cas sain accepté) ; elle laisse passer une tabulation, un retour chariot ou une espace insécable (VCB4-09).
- Huit corrections bloquantes (VCB4-01 à 08), toutes en mots exacts ; une mineure (09) ; une information (10). Aucune ne
  demande de donnée ni de dépense ; aucune ne tranche une décision de Lazar.

## Combinaisons d'options essayées (vérification 3)

- Options : N-031 (a), (b), (c) ; N-032 (A), (B), (C) ; P-016 (A), (B), (C) ; P-017 (A), (B), (C), (C′) ; P-023 (A), (B),
  (C) ; P-024 (A), (B), (C). Produit complet : 3 × 3 × 3 × 4 × 3 × 3 = **972 combinaisons**, chacune construite deux fois
  (versions écrites en remplacements appliquées dans l'ordre du texte, puis dans l'ordre inverse), sous deux lectures :
  (L) la règle « Statut » à la lettre (un passage de la version (A) ou (C) qui ne porte pas d'étiquette reste) ; (V) ma
  lecture de l'intention (ce passage est remplacé). 3 888 textes produits en mémoire, chacun contrôlé.
- Règle appliquée (puce « Statut ») : marqueurs retirés (avec le « ; » qui les introduit et leurs astérisques) ; versions
  non retenues retirées ; version retenue gardée sans étiquette ni guillemets ; versions retenues écrites en remplacements
  appliquées après ces retraits, puis retirées ; phrases de la liste retirées ; `<<PARTITION_P016>>` rempli par le texte
  retenu (Q-02). Contrôles : garde du scellement ; débris de ponctuation neufs (parenthèse vide, « ; ) », « .. », puce
  vide, etc.) ; contradictions ciblées ; doublons ; `problemes` sur le texte en mémoire.
- Résultats (L), nombre de combinaisons touchées sur 972 :
  - garde (« en attente », « de repli ») : **0** ; erreur nouvelle de `problemes` : **0** (seuls restent « Contre-lecture »
    à remplir et les marqueurs de gabarit, moins `<<PARTITION_P016>>`) ; échec d'une chaîne à remplacer : **0** ;
  - texte de la partition écrit deux fois, avec « .. » : **972** (VCB4-04) ;
  - P-016 (B) : « 60 tâches », `plis/lecture-60`, « 5 plis de 12 tâches », « 5 plis de 8 tâches », « oracle sur les 40 »
    restent à côté des valeurs (B) : **324** (VCB4-02) ;
  - N-032 (A) : « Contrôle avant dépense M-P3b-2 » reste : **324** ; N-032 (B) : de plus « dont M-P3b-2 » et la phrase
    orpheline « (de même, avec « … ».) » : **324** (VCB4-03) ;
  - P-024 (B) : « 7,5 USD ; 8,6 USD », « 7,5 USD (8,6 USD) », « + 1,2 USD (+ 2,16 USD) », « borne de 7,5 USD » : **324**
    (VCB4-05) ; P-024 (C) : « sur le disque de l'instance seulement (scellés, poussés seuls … » : **324** (VCB4-08) ;
  - P-023 (B) : « un lecteur appris sur l'organisme, sur les 32 couches » : **324** (VCB4-06) ; P-023 (C) : écarts
    numérotés (vi) puis (viii) : **324** (VCB4-07) ;
  - N-031 (b) ou (c) avec P-023 (B) : texte différent selon l'ordre ; dans l'ordre du texte, l'écart des graines est
    remplacé et « (ii) lecture en diagnostic, aucune revendication ni règle pour G0 » reste : **216** (VCB4-01) ; les 216
    autres différences d'ordre comptées par l'essai (N-031 (b) ou (c) avec P-023 (C)) ne tiennent qu'aux blancs de mon
    harnais (contrôle `ordre_v1.py`) ;
  - P-017 (B) : « (et, en (C), le rejeu contrefactuel 2 × 2) » reste : **243** (VCB4-10).
- En (V), les défauts de VCB4-02 et 03 disparaissent ; restent VCB4-01, 04, 06, 07, 08, la borne de 7,5 USD de la liste
  d'arrêt en P-024 (B) (VCB4-05 (5)) et P-017 (B).
- Hors VCB4-04, combinaisons sans défaut détecté : N-031 ∈ {(a), (b), (c)}, N-032 (C), P-016 ∈ {(A), (C)},
  P-017 ∈ {(A), (C), (C′)}, P-023 (A), P-024 (A) : 18 combinaisons, dont celle des recommandations. P-016 (C) et
  P-017 (B) ou (C) disent eux-mêmes qu'une version nouvelle du texte est exigée : seuls la garde et `problemes` y sont
  probants.

## Constats

### VCB4-01 — majeur (bloquant) — Règle « Statut » : ordre des versions écrites en remplacements, portée de « qui précède », retrait des signes

- **Où** : puce « Statut », l. 38-41 ; écart (iv), l. 149 ; suite des replis de N-031, l. 299-306 ; repli (B) de P-023,
  l. 171-173 (« les autres renumérotés »).
- **Ce qui est** : (1) la règle ne fixe pas l'ordre entre deux versions retenues écrites en remplacements. N-031 (b) ou (c)
  remplace « l'écart (iv) » ; P-023 (B) retire (i), (ii), (v), (vi), (vii) et renumérote. Dans l'ordre du texte (P-023,
  l. 170, avant N-031, l. 299), « (iv) » est alors l'écart des graines : il est remplacé, et l'écart « lecture en
  diagnostic, aucune revendication ni règle pour G0 » reste (216 combinaisons). (2) Les corrections VCB4-02, 03 et 05
  emploient « à la place de « … » qui précède », que la règle doit définir. (3) Retirer un marqueur ou une version laisse
  le signe qui l'introduit (« (Q-05 ;) », « R7 ;) : », « (60 tâches ; ) », parenthèse vide après « verdict R13. ») : la
  règle ne dit pas qu'il part avec.
- **Correction (mots exacts)** : l. 40-41, remplacer « elle s'applique mot pour mot au texte principal, après le retrait
  des marqueurs et des autres versions, puis elle est retirée. » par « elle s'applique mot pour mot au texte principal,
  après le retrait des marqueurs et des autres versions, dans l'ordre N-031, N-032, P-016, P-024, P-023 (« à la place de
  « … » qui précède » vise la plus proche occurrence avant l'étiquette ; un marqueur ou une version retirés le sont avec
  l'espace et le signe « ; » ou « , » qui les introduisent, et avec la parenthèse qui ne contient plus qu'eux), puis elle
  est retirée. » (la phrase garde sa fin « puis elle est retirée. », que cite la liste des phrases retirées).

### VCB4-02 — majeur (bloquant) — P-016 (B) : huit passages en ligne sans délimitation de la version (A)

- **Où** : P3b-P1, l. 352 ; « Action », base de lecture et leurre, l. 366-373 ; validation croisée de l'oracle, l. 455-458 ;
  plis de T4 résiduel, l. 490-491 ; « Puissance », l. 661-662 ; « Graines », l. 675 ; Synthèse, l. 773.
- **Ce qui est** : à ces endroits la version (B) suit un passage de la version (A) qui ne porte aucune étiquette. La règle
  retire les versions non retenues et garde la retenue : en (B), le texte (A) reste. Résultat en (B) : « (60 tâches ;
  40) », « `plis/lecture-60`, `plis/lecture-40` », « sur 60 tâches (40) », deux règles de base de lecture, deux leurres,
  deux validations croisées (5 × 8 puis 5 × 4), « bras génériques lus sur 60 tâches, oracle sur les 40 … ; bras génériques
  lus sur 40 tâches, oracle sur les 20 ». Seul le point 1 du plan d'analyse (forme de VCt-03, « à la place du texte qui
  précède depuis ») est sûr.
- **Correction (mots exacts)** :
  1. l. 352 : « (60 tâches ; Version de repli (B) de P-016 : 40) » → « (60 tâches ; Version de repli (B) de P-016, à la
     place de « 60 tâches » qui précède : « 40 tâches ») » ;
  2. l. 369-371 : « Version de repli (B) de P-016 : « 40 tâches pour les bras génériques et la double comptabilité ; plis
     de T4 résiduel des bras génériques : clé `plis/lecture-40`, 5 plis de 8 tâches. » » → « Version de repli (B) de
     P-016, à la place du texte qui précède depuis « se lisent sur les 60 tâches » : « se lisent sur 40 tâches, aucun de
     leurs réglages n'étant fixé sur la découverte ; l'oracle se lit sur la confirmation seule. Plis de T4 résiduel des
     bras génériques : clé `plis/lecture-40`, 5 plis de 8 tâches. Les bras génériques sur la confirmation seule sont
     rapportés en descriptif, pour la synthèse avec l'oracle. » » ;
  3. l. 372 : « Version de repli (B) de P-016 : « Le leurre de la double comptabilité est tiré parmi les 40 tâches » →
     « Version de repli (B) de P-016, à la place de la phrase qui précède : « Le leurre de la double comptabilité est tiré
     parmi les 40 tâches » ;
  4. l. 457-458 : « Version de repli (B) de P-016 : « 5 plis de 4 tâches de confirmation ; l'oracle du pli k apprend sur
     la découverte et les 16 autres tâches de confirmation. » » → « Version de repli (B) de P-016, à la place de « 5 plis
     de 8 tâches ; l'oracle du pli k apprend, au réglage choisi, sur la découverte et les 4 autres plis » qui précède :
     « 5 plis de 4 tâches de confirmation ; l'oracle du pli k apprend, au réglage choisi, sur la découverte et les
     16 autres tâches de confirmation » » ;
  5. l. 490-491 : « `plis/lecture-60`, Version de repli (B) de P-016 : `plis/lecture-40` ; oracle » → « `plis/lecture-60`,
     Version de repli (B) de P-016, à la place de « `plis/lecture-60` » qui précède : « `plis/lecture-40` » ; oracle » ;
  6. l. 661-662 : « sur 60 tâches (Version de repli (B) de P-016 : 40) » → « sur 60 tâches (Version de repli (B) de P-016,
     à la place de « 60 tâches » qui précède : « 40 tâches ») » ;
  7. l. 675 : « `plis/lecture-60` (Version de repli (B) de P-016 : `plis/lecture-40`) » → « `plis/lecture-60` (Version de
     repli (B) de P-016, à la place de « `plis/lecture-60` » qui précède : « `plis/lecture-40` ») » ;
  8. l. 773 : « ; Version de repli (B) de P-016 : « bras génériques lus sur 40 tâches, oracle sur les 20 de la
     confirmation ») » → « ; Version de repli (B) de P-016, à la place de « bras génériques lus sur 60 tâches, oracle sur
     les 40 de la confirmation » qui précède : « bras génériques lus sur 40 tâches, oracle sur les 20 de la
     confirmation ») ».
  Avec VCB4-01, (A) donne « (60 tâches) », « `plis/lecture-60` ; oracle », etc. ; (B) donne « (40 tâches) »,
  « `plis/lecture-40` ; oracle », etc.

### VCB4-03 — majeur (bloquant) — N-032 (A) et (B) : la version (C) n'est pas délimitée ; « de même » renvoie à une version retirée

- **Où** : « Métrique », reconstitution, l. 398-409 ; liste d'arrêt, l. 795-798 ; « Chaîne de lancement », Ordre,
  l. 847-851 ; plan, § 4 (même phrase).
- **Ce qui est** : (1) le texte de (C) (« **Contrôle avant dépense M-P3b-2 (après le scellement, …)** … nœud de Lazar. » ;
  puce « Contrôle avant dépense M-P3b-2 hors de la règle de P3b-P0 … ») n'a pas d'étiquette : en (A) ou (B), il reste à
  côté de la mesure avant le scellement (deux M-P3b-2, deux règles). (2) Dans l'Ordre, la version (B) « de même, avec
  « … » » renvoie à la version (A), déjà retirée quand (B) s'applique ; elle ne contient aucun des mots de la règle
  (« devient », « à la place de », « est retiré », « remplacements mot pour mot ») : à la lettre, elle reste, orpheline
  (« (de même, avec « mesure M-P3b-2 … ».) »), et « contrôles avant dépense, dont M-P3b-2 (…) » reste aussi.
- **Correction (mots exacts)** :
  1. l. 404 : « Version de repli (A) de N-032 : « **Mesure avant le scellement » → « Version de repli (A) de N-032, à la
     place du texte qui précède depuis « **Contrôle avant dépense M-P3b-2 » : « **Mesure avant le scellement » ;
  2. l. 406 : « Version de repli (B) de N-032 : « **Mesure avant le scellement (M-P3b-2, processeur, par code ; lit » →
     « Version de repli (B) de N-032, à la place du texte qui précède depuis « **Contrôle avant dépense M-P3b-2 » :
     « **Mesure avant le scellement (M-P3b-2, processeur, par code ; lit » ;
  3. l. 795-796 : « Version de repli (A) de N-032 : « Mesure M-P3b-2 » → « Version de repli (A) de N-032, à la place de la
     phrase qui précède : « Mesure M-P3b-2 » ; l. 797 : « Version de repli (B) de N-032 : « Compte unique » → « Version de
     repli (B) de N-032, à la place de la phrase qui précède : « Compte unique » ;
  4. texte l. 850-851 et plan § 4, aux deux endroits : « Version de repli (B) de N-032 : de même, avec « mesure M-P3b-2
     avant le scellement (un seul compte, toutes conditions confondues) ».) » → « Version de repli (B) de N-032 : « N-032
     sans réponse vaut (C)) ; mesure M-P3b-2 avant le scellement (un seul compte, toutes conditions confondues) ; » à la
     place de « N-032 sans réponse vaut (C)) ; », et « contrôles avant dépense ; » à la place de « contrôles avant
     dépense, dont M-P3b-2 (reconstitution sur processeur, règle de P3b-P0) ; ».) ».

### VCB4-04 — mineur (bloquant) — Partition écrite deux fois, dans toutes les options

- **Où** : puce « Partition », l. 131-136 ; Q-02.
- **Ce qui est** : le marqueur `<<PARTITION_P016>>` « se remplit au candidat par le seul texte de la version retenue » et la
  règle « Statut » garde aussi cette version à sa place. Résultat, option recommandée comprise : « **Partition** :
  20 tâches de **découverte**, 40 de **confirmation** ; aucune tâche réservée.. 20 tâches de **découverte**, 40 de
  **confirmation** ; aucune tâche réservée. Tirage : … » (972 combinaisons sur 972).
- **Correction (mots exacts)** : l. 132-133, « le marqueur se remplit au candidat par le seul texte de la version retenue,
  mot pour mot]** » → « le marqueur se remplit au candidat par le seul texte de la version retenue, mot pour mot, sans son
  point final, et cette version n'est pas gardée une seconde fois à sa place]** » ; Q-02, après « (CR-P3b-texte-15). »,
  ajouter « (brouillon 5) La version retenue n'est pas gardée une seconde fois à sa place (VCB4-04). ».

### VCB4-05 — mineur (bloquant) — P-024 (B) : bornes en ligne sans délimitation ; borne de la garde de 24 heures

- **Où** : GO de calcul, l. 83 ; « Calcul et bornes », l. 670-672 ; liste d'arrêt, l. 816 et l. 829.
- **Ce qui est** : même défaut que VCB4-02 : en (B), « (borne de l'étape : 7,5 USD ; 8,6 USD) », « 7,5 USD (8,6 USD) »,
  « + 1,2 USD (+ 2,16 USD) », « (7,5 USD ; 8,6 USD) » ; et l. 816 « compris dans la borne de 7,5 USD » n'a pas de
  version (B).
- **Correction (mots exacts)** :
  1. l. 83 : « (borne de l'étape : 7,5 USD ; Version de repli (B) de P-024 : 8,6 USD) » → « (borne de l'étape : 7,5 USD ;
     Version de repli (B) de P-024, à la place de « 7,5 USD » qui précède : « 8,6 USD ») » ;
  2. l. 670-671 : « borne de l'étape 7,5 USD (Version de repli (B) de P-024 : 8,6 USD) » → « borne de l'étape 7,5 USD
     (Version de repli (B) de P-024, à la place de « 7,5 USD » qui précède : « 8,6 USD ») » ;
  3. l. 671-672 : « + 1,2 USD (Version de repli (B) de P-024 : + 2,16 USD) » → « + 1,2 USD (Version de repli (B) de P-024,
     à la place de « + 1,2 USD » qui précède : « + 1,2 USD + 2,16 USD ») » ;
  4. l. 829 : « (7,5 USD ; Version de repli (B) de P-024 : 8,6 USD) » → « (7,5 USD ; Version de repli (B) de P-024, à la
     place de « 7,5 USD » qui précède : « 8,6 USD ») » ;
  5. l. 816 : « compris dans la borne de 7,5 USD) » → « compris dans la borne de 7,5 USD ; Version de repli (B) de P-024, à
     la place de « 7,5 USD » qui précède : « 8,6 USD ») ».

### VCB4-06 — mineur (bloquant) — P-023 (B) : la Synthèse lit encore l'oracle « sur les 32 couches »

- **Où** : Synthèse, troisième ligne, l. 773 ; repli (B) de P-023, l. 213-214.
- **Ce qui est** : en (B), l'oracle lit les couches 7, 15 et 23 (puce « entrée » remplacée, écart (ii) retiré) ; la ligne
  « oracle en O7 … » dit « un lecteur appris sur l'organisme, sur les 32 couches, est au-dessus » (324 combinaisons).
- **Correction (mots exacts)** : dans le repli (B) de P-023, « dans P3b-P9, « T4 de P3 (quintiles) » devient « T4 résiduel
  (deux spécifications, recouvrement) » ; » → « dans P3b-P9, « T4 de P3 (quintiles) » devient « T4 résiduel (deux
  spécifications, recouvrement) » ; dans la troisième ligne de la synthèse, « sur les 32 couches » devient « aux couches 7,
  15 et 23 » ; ».

### VCB4-07 — mineur (bloquant pour (1) et (2)) — P-023 (B) et (C) : portée des remplacements de l'oracle ; numérotation en (C)

- **Où** : repli (C), l. 162-166 ; repli (B), l. 182-190 ; « Oracle », puce « étiquettes d'apprentissage », l. 447-451.
- **Ce qui est** : (1) et (2) « étiquettes : « … » » ne dit pas ce qu'il remplace dans la puce. Lu comme les seules trois
  premières clauses, il laisse « T1 reste un test : les étiquettes de T1 n'entrent dans aucun apprentissage », contraire
  à (B) et à (C), où les positifs sont étiquetés par T1. (3) En (B), un seul texte remplace deux puces non voisines
  (« entrée » et « choix ») sans dire où va chaque partie. (4) En (C), « écart (vii) retiré » sans renumérotation laisse
  (vi) puis (viii).
- **Correction (mots exacts)** : (1) l. 162-163, « écart (vii) retiré ; « Oracle », étiquettes : « **positifs** » →
  « écart (vii) retiré, les suivants renumérotés ; « Oracle », tout ce qui suit les deux-points de la puce « étiquettes
  d'apprentissage » devient : « **positifs** » (règle aussi (4)) ; (2) l. 189-190, « seule. » ; étiquettes :
  « **positifs** = actions du saboteur étiquetées 1 par T1 ; **négatifs** = » → « seule. » ; « Oracle », tout ce qui suit
  les deux-points de la puce « étiquettes d'apprentissage » devient : « **positifs** = actions du saboteur étiquetées 1 par
  T1 ; **négatifs** = » ; (3), non bloquant, l. 182, « la puce « entrée » et la puce « choix » sont remplacées par » → « la
  puce « entrée » et la puce « choix » sont remplacées, chacune à sa place, par les deux parties du texte qui suit (la
  première jusqu'à « produit scalaire ; » compris, la seconde depuis « choix ») ».

### VCB4-08 — mineur (bloquant) — P-024 (C) : l'étape 2.6 garde « sur le disque de l'instance seulement » ; fin de la suite non bornée

- **Où** : plan d'analyse, étape 2.6, l. 640-641 ; « États à t_cost », l. 864-877.
- **Ce qui est** : (1) en (C), l'étape 2.6 devient « gardés **en mémoire et sur le disque de l'instance seulement**
  (scellés, poussés seuls, en morceaux, … » : contradiction (324 combinaisons). (2) La suite de (C) n'a pas de
  guillemets ; la phrase qui la suit, « Dans tous les cas, la garde après un refus de poussée reste bornée à 24 heures
  (liste d'arrêt). », peut être lue comme sa fin et retirée en (A) et en (B).
- **Correction (mots exacts)** : (1) l. 875-877, « Version de repli (C) de P-024, suite : à l'étape 2.6, « jamais poussés »
  devient « poussés seuls, en morceaux, à leurs chemins et empreintes ». Dans tous les cas, la garde après un refus de
  poussée reste bornée à 24 heures (liste d'arrêt). » → « Version de repli (C) de P-024, suite : à l'étape 2.6, « **en
  mémoire et sur le disque de l'instance seulement** (scellés, jamais poussés ; » devient « **en mémoire et sur le disque
  de l'instance** (scellés, poussés seuls, en morceaux, à leurs chemins et empreintes ; ». » ; (2) l. 864-865, « confiance
  ≈ 60 %]** Version (A), écrite ici : » → « confiance ≈ 60 %]** Dans tous les cas, la garde après un refus de poussée
  reste bornée à 24 heures (liste d'arrêt). Version (A), écrite ici : ».

### VCB4-09 — mineur — Garde du scellement : blancs autres que l'espace et le retour à la ligne (vérification 4)

- **Où** : plan, `sceller_p3b_v1.sh` (§ 1, ligne de la table) ; texte l. 46-47.
- **Ce qui est** : essai `garde_scellement_v1.py` : la garde lue à la lettre (« toute suite d'espaces et de retours à la
  ligne ») refuse le brut, le pluriel et la casse, les chaînes coupées par un retour à la ligne suivi d'espaces ou par deux
  retours (7 artefacts sur 7) et accepte le cas sain : **l'artefact demandé par VCt-01 est couvert**. Elle accepte en
  revanche « de\trepli », « en\r\nattente », « de repli » avec espace insécable (U+00A0) ou fine insécable (U+202F). Le
  brouillon 4 n'en contient aucune (contrôle par catégorie Unicode) ; un candidat copié d'ailleurs le pourrait (R5).
- **Correction (mots exacts)** : plan, « (toute suite d'espaces et de retours à la ligne lue comme une espace)** (cas sain :
  candidat sans ces chaînes ; artefacts : chacune, au singulier et au pluriel, et chacune coupée par un retour à la ligne
  suivi d'espaces) » → « (toute suite de blancs, retours à la ligne, retours chariot, tabulations et espaces insécables
  compris, lue comme une espace)** (cas sain : candidat sans ces chaînes ; artefacts : chacune, au singulier et au pluriel,
  et chacune coupée par un retour à la ligne suivi d'espaces, par une tabulation et par une espace insécable) » ; texte
  l. 47, « sans égard à la casse ni aux retours à la ligne. » → « sans égard à la casse ni aux blancs (retours à la ligne et
  espaces insécables compris). ».

### VCB4-10 — information

- **P-017 (B)** : la version « (B) ou (C) » garde en (B) « (et, en (C), le rejeu contrefactuel 2 × 2) ». Elle exige de
  toute façon une version nouvelle du texte : pas de correction exigée.
- **Restes sans contradiction** dans toutes les combinaisons : « Q-05 est le même dans les trois options de P-023. »
  (l. 377) ; « P-017 (C′) : recommandée par la session … » (table hors périmètre, l. 228) en (C′) ; en P-023 (B), G5 « …
  du contexte, et du nombre écrit (…) » et la puce « **T4 de P3** (…) : décisif pour chaque bras » sans point final
  (points déjà déclarés par le rédacteur).
- **Devis et plan** : ils portent les mêmes formes en ligne (« (Version de repli (B) de P-024 : 8,6 USD) », « Version de
  repli (B) de P-016 (40 tâches lues …) ») ; ils ne sont pas scellés par le commit S, mais la session les aligne avec le
  candidat.
- **Ordre de la chaîne** : laissé à la session par le rédacteur (étape après le brouillon 4) ; d'accord.

## Comptes

- 10 constats : majeurs 3 (VCB4-01 à 03) ; mineurs 6 (VCB4-04 à 09) ; information 1 (VCB4-10).
- Bloquants : 8 (VCB4-01 à 08 ; pour VCB4-07, parties (1) et (2)).
- Combinaisons d'options essayées : 972, chacune dans deux ordres et deux lectures (3 888 textes en mémoire) ; garde et
  `problemes` sans erreur nouvelle dans toutes ; aucune sans défaut (VCB4-04) ; hors VCB4-04, 18 propres, dont celle des
  recommandations.
- Aucune grandeur de P3 recopiée.
