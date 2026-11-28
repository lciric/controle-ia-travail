# Contre-lecture R2 du brouillon 2 de P3b — lentille « texte et périmètre » — v1

- Contre-lecteur : sous-agent neuf (Claude), session 16, 2026-10-21, lu de 00:58 à 01:07 UTC, écrit vers 01:07 UTC (heure lue
  par `date -u`). Je n'ai écrit ni P3b (brouillons, devis, plans, questions), ni P3 (texte, code, run, lecture, addenda,
  verdicts), ni aucune contre-lecture, projet de traitement ou traitement de P3b.
- Consigne : `…/consigne-contre-lecture-R2-P3b-brouillon2-v1.md`
  (`a7c43cd24ecc6c837779dace49f73cae4de034a141c23627edf5e939f1818380`, égale à son compagnon). Préfixe `…/` =
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b`. Dépôt `R` = `/home/user/controle-ia-travail`.
- Relu (empreintes égales à leurs compagnons) : texte `…/brouillon2/P3b-seconde-lecture-v1-brouillon2.md`
  (`64c5adad566d05f2c78b8bd375f6e3ac18e0852c882da0b4593f268153aa1562`) ; devis `devis-P3b-v2.md` (`7dd3cfee…`) ; plan
  `plan-code-et-chaine-P3b-v2.md` (`fd82f2f6…`) ; questions `questions-ouvertes-P3b-v2.md` (`417a111e…`) ; table
  `table-traitement-brouillon2-v1.md` (`1a3e2091…`) ; sortie `problemes-brouillon2-v1.txt` (`602270e1…`). Pièces
  d'appui : traitement `d31c87b1…`, projet `82a90e81…` (parties F-7, F-8, texte-17, nœuds A et E), note transmise v2
  (`86c1518f…`), consigne du rédacteur du brouillon 2 (`434ecc98…`), questions v1 (`046991ab…`, Q-06 seulement) ;
  `R/registres/decisions.md` (`61b31f83…`) lignes N-028, P-016, P-017, P-023, P-024, R-262, R-296, R-303, R-305, R-312,
  N-031, N-032 ; `R/registres/go.md` (`1a392407…`) GO-2026-10-04-08, GO-2026-10-20-05, -06, -07, -10, -11, -12 ;
  `R/docs/decisions/decision-N-026-v1.md` (section 1) et `decision-N-029-v1.md` (section 2) ; `R/prereg/P3-premier-test-i-a-v1.md`
  (lignes citées par le texte seulement) ; `R/registres/depenses.md` (`f4d6ee90…`, l. 76, 88, 90) ; validateur et gabarit ;
  lignes citées de `R/src/controle_ia/` (`episode.py`, `lecture.py`, `statistiques.py`, `evaluation.py`, `notation.py`,
  `run.py`, `validation_reelle.py`).
- Lentille : « texte et périmètre » seulement. Les six blocs de méthode sont laissés à l'autre contre-lecteur.
- **Exposition et écarts à ma consigne (déclarés).** J'ai lu la ligne R-303 du registre, qui porte des grandeurs observées de
  P3 ; je n'en recopie aucune. Je n'ai ouvert ni le verdict complété, ni les addenda (empreintes seulement). Écart 1 : une
  recherche `grep -r` dans `R/src/controle_ia/` (recherche récursive interdite par la consigne), pour situer des fonctions
  citées ; aucun fichier interdit touché ; elle m'a montré le module de `heures_declarees` (Q-27), que je ne reprends pas
  ici. Écart 2 : une liste (non récursive) de `…/scratchpad/p4-instrument/chaine-v2/` pour l'empreinte de
  `NOTES-CHAINE-v2.md` (`1691bf25…`, égale à la citation). Lecture de la proposition 010 refusée par l'environnement : ses
  numéros de ligne et Q-26 ne sont pas vérifiés ici.

## Verdict

**Scellable après corrections.**
Le périmètre suit les décisions et les GO cités (défauts, dates, recommandations et confiances égaux au registre) ; aucune
décision de Lazar n'est tranchée dans le texte principal ; aucune grandeur observée de P3 n'est recopiée ; la sortie de
`problemes` est retrouvée à l'identique (20 marqueurs, section « Contre-lecture » à remplir) ; empreintes, lignes de P3 et
lignes de code citées vérifiées. Mais plusieurs versions de repli ne sont pas remplaçables en mots exacts (renvoi à une
mauvaise puce, passages non nommés) et certaines ne seraient pas refusées au scellement (pluriel, mentions en minuscule).
Corrections bloquantes : CR2-P3b-texte-01 à -05.

## Vérifié sans constat

- Empreintes de toutes les pièces, des modules gelés (préfixes égaux à `7a54d43` et sur disque), de P3, du gabarit, du
  validateur, de N-026, N-029, des addenda, du verdict v2, de `go.md`, `decisions.md`, `depenses.md` : égales aux citations.
- Lignes de P3 citées (238-248, 275-278, 303-316, 352-358, 382-385, 394-397, 415-416, 428, 436) et de code citées
  (`episode.py` 211-217, 254, 256-263 ; `lecture.py` 173-185, 202-224 ; `statistiques.py` 96-126, 173-194 ;
  `evaluation.py` 66-82 ; `notation.py` 131-141 ; `run.py` 313-329 ; `validation_reelle.py` 71-73) : conformes.
- Marqueurs : P-016 et P-017 (défaut (A) le 2026-10-22 vers 21:15 UTC), P-023 et P-024 (défaut (A) le 2026-10-23 vers
  00:30 UTC), N-031 (aucun défaut, pas de scellement sans réponse), N-032 (aucun défaut, revient à (C)) : égaux au registre.
- Devis : borne 7,14 arrondie à 7,5 USD ; (B) de P-024 8,58 arrondie à 8,6 USD ; crédit 7,05 USD ; tous sous les 10 USD de
  GO-2026-10-20-07 (échéance 2026-11-30) ; marges de durée cohérentes (7 200 s, 150, 210 minutes, 14 400 s).
- Table de traitement : 20 + 25 constats, comptes égaux aux rapports.

## Constats

### CR2-P3b-texte-01 — bloquant
- Où : texte l. 135-136 (version de repli (C) de P-023) et l. 155-157 (version de repli (B) de P-023).
- Ce qui est : « liste d'arrêt, troisième puce : « … » ». La troisième puce de la liste d'arrêt est « Chemin gelé différent
  de `7a54d43`… » ; la puce visée est la quinzième. « Troisième » venait de F-8 du projet (troisième des cinq puces
  ajoutées par texte-17). Appliqué mot pour mot, le repli effacerait la garde des chemins gelés.
- Ce qui devrait être : un renvoi qui désigne la puce par ses premiers mots.
- Correction (mots exacts), aux deux endroits : remplacer « liste d'arrêt, troisième puce : » par « liste d'arrêt, la puce
  qui commence par « Action de la mention, ou toute étiquette de T1 » devient : ».

### CR2-P3b-texte-02 — bloquant
- Où : texte l. 280, l. 285-287, l. 506 (P-016) ; l. 57 (P-024).
- Ce qui est : des passages qui dépendent d'une décision portent leur autre version en minuscule, sans l'étiquette
  « Version de repli » : « en version (A), les bras génériques » ; « (60 en version (A), 40 en version (B)) » ; « La version
  (B) ne lit jamais les 20 tâches réservées. » ; « (version (A)) » ; « 7,5 USD en version (A) de P-024 ». Le scellement
  ne les refuse pas ; le texte scellé en (A) parlerait encore de la version (B).
- Ce qui devrait être : texte principal dans la version recommandée seule ; l'autre version sous l'étiquette, remplaçable.
- Correction (mots exacts) : l. 280, « : en version (A), les bras génériques » → « : les bras génériques » ; l. 285-287,
  « Le leurre de la double comptabilité est tiré parmi les tâches qu'elle lit (60 en version (A), 40 en version (B)), une
  fois par tâche. La version (B) ne lit jamais les 20 tâches réservées. » → « Le leurre de la double comptabilité est tiré
  parmi les 60 tâches qu'elle lit, une fois par tâche. Version de repli (B) de P-016 : « Le leurre de la double
  comptabilité est tiré parmi les 40 tâches qu'elle lit, une fois par tâche ; aucune lecture ne charge les 20 tâches
  réservées. » » ; l. 506, « la confirmation (version (A)). » → « la confirmation. » ; l. 57, « (borne de l'étape : 7,5 USD
  en version (A) de P-024). » → « (borne de l'étape : 7,5 USD ; Version de repli (B) de P-024 : 8,6 USD). ».

### CR2-P3b-texte-03 — bloquant
- Où : plan l. 72 (`sceller_p3b_v1.sh`) ; texte l. 633, l. 687, l. 719-721 ; texte l. 162-164 (tableau hors périmètre).
- Ce qui est : (1) le scellement refuse « Version de repli » au singulier ; « Versions de repli (B) et (C) de P-023… »
  (l. 633, l. 687) et « (Versions de repli (A) et (B) de N-032 : … » (l. 719) passent. (2) Les cellules « P-017 (B), en
  attente ; défaut (A) le … » (l. 162-163) et « P-016 (B) ou (C), en attente ; défaut (A) » (l. 164) seront refusées au
  scellement, mais aucun texte exact ne les remplace.
- Ce qui devrait être : un refus qui couvre singulier et pluriel ; des cellules remplies au candidat par une forme fixée.
- Correction (mots exacts) : plan l. 72, « **refuse tout texte qui contient « en attente », « Version de repli » ou
  « Proposition en attente »** (cas sain : candidat sans ces chaînes ; artefacts : chacune des trois chaînes) » → « **refuse
  tout texte qui contient « en attente », « de repli » ou « Proposition en attente », sans égard à la casse** (cas sain :
  candidat sans ces chaînes ; artefacts : chacune, au singulier et au pluriel) » ; texte l. 633, « (Versions de repli (B) et
  (C) de P-023 pour O3b, O6 et O7 : section « Périmètre ».) » → « (Version de repli (B) de P-023 et Version de repli (C) de
  P-023, pour O3b, O6 et O7 : section « Périmètre ».) » ; l. 687, de même « (Version de repli (B) de P-023 et Version de
  repli (C) de P-023 : section « Périmètre ».) » ; tableau hors périmètre, colonne « état » : l. 162 « P-017 : `<<ISSUE_P017>>` »,
  l. 163 « P-017 : `<<ISSUE_P017>>` », l. 164 « P-016 : `<<ISSUE_P016>>` » ; Q-23 ajoute : « `<<ISSUE_P016>>`,
  `<<ISSUE_P017>>` : « tranchée (X) par Lazar le … (registre, ligne) » ou « défaut (A) appliqué le … (registre, ligne) » ».
  La parenthèse de l. 719-721 : CR2-P3b-texte-07.

### CR2-P3b-texte-04 — bloquant
- Où : texte, en-tête, puce « Statut » (l. 17-21).
- Ce qui est : seuls P-016 (l. 102-104) et N-031 (l. 207) disent que le texte scellé ne garde que la version retenue.
  Pour P-017, P-023, P-024, N-032, rien ne dit que le marqueur, l'étiquette « Version (A), écrite ici : » et les
  guillemets sont retirés, ni où le texte scellé dit quelle option a été retenue et comment (réponse ou défaut échu).
- Ce qui devrait être : une règle générale, et la trace de chaque décision dans le texte scellé (R1).
- Correction (mots exacts) : à la fin de la puce « Statut », ajouter : « Au candidat, pour chaque décision marquée
  « [Décision de Lazar en attente : …] », le marqueur et les versions non retenues sont retirés ; la version retenue reste
  seule, mot pour mot, sans son étiquette (« Version (A), écrite ici : », « Version (a) : », « Version de repli … : ») ni
  ses guillemets. Issues des décisions : `<<ISSUES_DECISIONS_P3B>>` (pour chacune : numéro, option retenue, réponse de
  Lazar ou défaut échu, date, ligne du registre). » ; Q-23 ajoute ce marqueur.

### CR2-P3b-texte-05 — bloquant
- Où : texte l. 137-157 (version de repli (B) de P-023).
- Ce qui est : (1) « « Oracle », entrée, bandes et estimateur : « … » » : la puce « choix » (l. 362-364) n'est pas
  nommée alors que le bloc la contredit (18 réglages, autres ex aequo) ; si la puce « estimateur » est remplacée, « système
  écrit ci-dessous » ne renvoie plus à rien ; la dernière phrase de « Bandes de couches » (l. 349) change sans mots écrits.
  (2) « (la réserve « plancher conjoint » est alors retirée : elle est la règle) » ne nomme ni la puce l. 472-479 (qui porte
  aussi « T1 intra-tâche », à garder) ni la ligne l. 170 du tableau hors périmètre. (3) « T4 : « … » » ne nomme pas le
  passage remplacé (l. 390-408) ; « T4 résiduel » devient « T4 » dans les seules tables G, O et Synthèse : H-P3b-1
  (l. 235), H-P3b-2 (l. 238), P3b-P2 (l. 267), P3b-P5 (l. 270), P3b-P9 (l. 274, « T4 de P3 (quintiles) » descriptif) et
  « Famille principale » (l. 489) restent faux ; G6 (l. 618) et O5 (l. 629) gardent une branche « recouvrement » que T4 de
  P3 n'a pas. (4) l. 127-129, « Les choix de sonde de la version (A) … » reste faux en (B). (5) Les détails du repli (B)
  (lecteurs, 18 réglages, ex aequo, jeton t_cost) sont une lecture du rédacteur (Q-26), non le texte de P-023 ; le texte ne
  le dit pas.
- Ce qui devrait être : chaque passage remplacé nommé par ses premiers et derniers mots, avec son texte neuf.
- Correction (mots exacts), dans le repli (B) : (1) « « Oracle », entrée, bandes et estimateur : » → « « Oracle », la puce
  « entrée » et la puce « choix » sont remplacées par (la puce « estimateur » reste ; elle sert au lecteur (a)) : » ; dans
  le bloc, « (système écrit ci-dessous, » → « (système de la puce « estimateur », » et « ; réglages : » → « ; choix
  (découverte seulement) : réglages » ; après le bloc, ajouter « ; « Bandes de couches », dernière phrase : « Elles servent à
  la double comptabilité seule. » ». (2) « (la réserve « plancher conjoint » est alors retirée : elle est la règle) » →
  « ; « Réserves de robustesse reprises de l'addendum 1 de P3 » : « pour chaque jeu décisif au-dessus (sondes génériques sur
  W, oracle) et pour T1 établi » devient « pour T1 établi » ; tableau hors périmètre : ligne « excès d'aire apparié par
  tirage, en lecture décisive » retirée ». (3) « T4 : « **T4 de P3** … descriptifs » ; dans les tables G, O et Synthèse,
  « T4 résiduel » devient « T4 » » → « la puce « T4 de P3 (descriptif) » devient « **T4 de P3** (aire stratifiée par
  quintiles du log10 du coût déclaré, `detection_stratifiee`) : décisif pour chaque bras » ; la puce « T4 résiduel »
  commence par « (descriptif) » ; dans H-P3b-1, H-P3b-2, P3b-P2, P3b-P5, « Famille principale » et les tables G, O et
  Synthèse, « T4 résiduel » devient « T4 de P3 » ; dans G6, « ; T4 résiduel non calculable (recouvrement) → « le plan ne
  sépare pas le score du nombre écrit (recouvrement insuffisant) » » est retiré ; dans O5, « (ou « recouvrement
  insuffisant », motif écrit) » est retiré ; dans P3b-P9, « T4 de P3 (quintiles) » devient « T4 résiduel (deux
  spécifications, recouvrement) » ». (4) Ajouter : « ; la phrase « Les choix de sonde de la version (A) … chacun avec un
  renvoi à P-023. » est retirée ». (5) Après « (« au plus près de la proposition 010 ») », ajouter « (lecteurs, réglages, ex
  aequo et jeton t_cost : lecture du rédacteur du brouillon 2, Q-26, à confirmer par Lazar avec l'option) ».

### CR2-P3b-texte-06 — majeur
- Où : texte l. 216-220 (versions de repli (b) et (c) de N-031) ; écart (iv), l. 120 ; réserves, l. 658-661 ; synthèse,
  l. 653.
- Ce qui est : en (b) ou (c), seuls G5 et la première ligne de la synthèse changent. L'écart (iv) dit encore « lecture en
  diagnostic, aucune revendication » ; la réserve « tentative non aveugle », exigée par (b) et (c), n'est pas dans la liste
  des réserves ; en (b), la troisième ligne de la synthèse dit encore « (diagnostic ; » pour les sondes génériques.
- Ce qui devrait être : un repli complet.
- Correction (mots exacts) : après « « diagnostic » devient « tentative de détection non aveugle (N-031) ». », ajouter :
  « L'écart (iv) devient « (iv) tentative de détection déclarée non aveugle (N-031), aucune règle pour G0 (l. 157) » ;
  dans la liste des réserves qui suit la table « Synthèse », « tentative non aveugle (N-031) ; » s'ajoute après
  « puissance du nul ; » ; en (b), dans la troisième ligne de la synthèse, « (diagnostic ; » devient « (tentative de
  détection non aveugle pour les sondes génériques, diagnostic pour l'oracle ; ». ».

### CR2-P3b-texte-07 — majeur
- Où : texte l. 309-320 (M-P3b-2), l. 675 (liste d'arrêt), l. 719-721 (Ordre).
- Ce qui est : (1) en (A) de N-032, « (faite avant le scellement) » est hors des guillemets : le texte scellé dirait
  « Mesure avant dépense » pour une mesure faite avant le scellement. (2) La puce l. 675 (« Contrôle avant dépense M-P3b-2 …
  ») n'a pas de repli ; en (B), aucune règle ne suit le compte unique. (3) La parenthèse l. 719-721 n'est pas en mots
  exacts. (4) Aucune des trois versions ne limite M-P3b-2 aux tâches lues : en version de repli (B) de P-016, elle lirait
  `jetons` et `jetons_notes` des 20 tâches réservées, contre la puce d'arrêt l. 674.
- Ce qui devrait être : trois versions complètes, limitées aux tâches lues.
- Correction (mots exacts) : (1) dans le repli (A), « **Mesure avant dépense (M-P3b-2, » → « **Mesure avant le scellement
  (M-P3b-2, » et retirer « (faite avant le scellement) ». (2) l. 675, ajouter : « Version de repli (A) de N-032 :
  « Mesure M-P3b-2 avant le scellement hors de la règle de P3b-P0 : aucun scellement ni création d'instance, nœud de Lazar
  (N-032). » Version de repli (B) de N-032 : « Compte unique M-P3b-2 avant le scellement : rapporté à Lazar avec le
  candidat, sans règle ; la règle de P3b-P0 se lit au préalable de la lecture. » ». (3) l. 719-721, la parenthèse devient :
  « (Version de repli (A) de N-032 : « mesure de conception M-P3b-1 (puissance) ; mesure M-P3b-2 avant le scellement (par
  condition, règle de P3b-P0, sortie brute scellée) ; candidat » à la place de « mesure de conception M-P3b-1 (puissance) ;
  candidat », et « contrôles avant dépense ; » à la place de « contrôles avant dépense, dont M-P3b-2 (reconstitution sur
  processeur, règle de P3b-P0) ; ». Version de repli (B) de N-032 : de même, avec « mesure M-P3b-2 avant le scellement (un
  seul compte, toutes conditions confondues) ».) » ; même changement au plan, § 4 et l. 67. (4) Dans le texte principal
  et le repli (A), « épisodes rejoués exactement et actions reconstituées » → « épisodes des tâches lues rejoués
  exactement et actions reconstituées » ; dans le repli (B), « actions dont la tokenisation » → « actions des tâches lues
  dont la tokenisation ».

### CR2-P3b-texte-08 — majeur
- Où : texte l. 549-555 (Plan, point 5), l. 523-524 (étape 2.6), l. 691-694 et l. 740-743 (P-024) ; plan l. 40.
- Ce qui est : (1) le crédit exigé n'a pas son repli (B) de P-024 (+ 2,16 USD), écrit au devis (§ 4) et au plan (l. 68) :
  en (B), la garde du texte scellé et celle de la chaîne diffèrent. (2) En (C), « jamais poussés » (l. 523) et la puce
  d'arrêt « axe de longueur 4 096 » (l. 691) restent sans exception écrite à leur place ; surtout, un fichier de ≈ 1,3 Go
  dépasse la taille totale de 100 Mo du contrôle des fichiers (plan l. 40) et la limite par fichier d'un dépôt GitHub sans
  stockage de gros fichiers : le repli (C) serait refusé par sa propre chaîne (arrêt, garde de 24 heures).
- Ce qui devrait être : des replis applicables tels quels.
- Correction (mots exacts) : (1) l. 554-555, « crédit exigé à la création 4,5 heures × (prix de l'offre + autres projets
  en marche) + 1,2 USD. » → « crédit exigé à la création 4,5 heures × (prix de l'offre + autres projets en marche) +
  1,2 USD (Version de repli (B) de P-024 : + 2,16 USD). » (2) À la fin du repli (C) de P-024, avant « Dans tous les cas »,
  ajouter : « ; le fichier est poussé en morceaux de 90 Mo au plus, chacun scellé, réunis par code à la lecture ; à l'étape
  2.6, « jamais poussés » devient « poussés seuls, en morceaux, à leurs chemins et empreintes » ; la puce d'arrêt « Fichier à
  pousser qui porte un axe de longueur 4 096 » et la borne de 100 Mo du contrôle des fichiers excluent ces seuls morceaux. »
  ; même exception au plan, l. 40.

### CR2-P3b-texte-09 — majeur
- Où : texte l. 612-613 (G2a, G2b) et l. 571-572 (Plan, point 8) ; questions Q-22.
- Ce qui est : G2a cite `<<LIGNE_VERDICT_P4>>`, ligne du verdict de P4 au scellement ; sans verdict au scellement, G2a porte
  « sans objet au scellement ». Si le verdict de P4 est scellé après le scellement de P3b mais avant sa lecture (cas
  probable : lancement de P4 accordé, R-313), G2a est sans objet et G2b ne s'applique pas : G2 s'applique, quelle que soit
  l'issue de P4.
- Ce qui devrait être : G2a gelée sur la forme de la ligne d'issue de la table gelée de P4, lue dans le verdict de P4
  scellé au moment de la lecture.
- Correction (mots exacts) : G2a, « (ligne citée : `<<LIGNE_VERDICT_P4>>`) » → « (forme exacte de la ligne d'issue de la
  table gelée du préenregistrement scellé de P4-instrument, chemin et empreinte : `<<LIGNE_ISSUE_P4>>`, cherchée dans le
  verdict de P4 scellé au moment de la lecture) » ; point 8 → « 8. **Instrument générique et P4** : les lignes G2a et G2b
  s'appliquent au moment de la lecture ; G2a lit la forme citée dans le verdict de P4 scellé à ce moment ; G2b s'applique si
  aucun verdict de P4 n'est scellé à ce moment. » ; Q-22 et Q-23 : `<<LIGNE_ISSUE_P4>>` au lieu de `<<LIGNE_VERDICT_P4>>`.

### CR2-P3b-texte-10 — mineur
- Où : texte l. 120 (écart (iv)), l. 122-123 (vi), l. 124-125 (viii).
- Ce qui est : (iv) et (viii) n'ont pas de motif ; (vi) n'a qu'un renvoi (« motif : Q-06 »). Les autres écarts ont un motif
  écrit.
- Ce qui devrait être : chaque écart à la proposition 010 avec son motif en mots.
- Correction (mots exacts) : (iv), « (l. 157 ; N-031, texte-01) » → « (l. 157 ; N-031, texte-01 ; motif : les bras
  localisés relisent un champ déjà lu par T2 et par l'addendum 1, l'oracle est appris sur l'organisme et les données sont
  déjà lues) » ; (vi), « motif : Q-06) » → « motif : avec l'honnête seul, l'oracle peut apprendre « une consigne privée est
  présente » ; N-028 ne demande que T1, T3 et T4, Q-06) » ; (viii), « (l. 24) » → « (l. 24 ; motif : les choix de l'oracle,
  réglage et normalisation, se font sur la découverte, hors de toute lecture rapportée) ».

### CR2-P3b-texte-11 — mineur
- Où : texte l. 712-713 (Chaîne, Ordre) ; plan § 4, l. 78-80.
- Ce qui est : « décisions en attente (P-016, …) ; brouillon 2 ; » : le brouillon 2 a été écrit avant les décisions ; aucune
  étape ne place les réponses avant le candidat. La chaîne « en attente » sera de plus refusée au scellement.
- Correction (mots exacts) : « traitement ; décisions en attente (P-016, P-017, N-031 statut, N-032 M-P3b-2, P-023
  concepts et écarts à la proposition 010, P-024 états à t_cost) ; brouillon 2 ; » → « traitement ; brouillon 2, décisions
  de Lazar marquées ; » et, avant « candidat, puis relecture courte », insérer « réponses de Lazar ou défauts échus (P-016,
  P-017, P-023, P-024 ; N-031 exige une réponse ; N-032 sans réponse vaut (C)) ; » ; même changement au plan, § 4.

### CR2-P3b-texte-12 — mineur
- Où : devis l. 16-17, l. 46, l. 48, l. 52 ; l. 34-35 et l. 39 (renvois à P3).
- Ce qui est : la somme des postes du § 3 vaut ≈ 1,2 à 1,9 h sans la lentille jacobienne et ≈ 1,3 à 2,2 h avec ; le total
  écrit (≈ 1,3 à 2,25 h) ne correspond à aucune des deux (la borne n'en dépend pas). Les renvois « P3 l. … » n'ont ni chemin
  ni empreinte dans le devis (R6). « P3 : ≈ 38 s par épisode » est la durée du pilote citée par P3 l. 385.
- Correction (mots exacts) : § 1, « **≈ 1,3 à 2,25 heures de carte A100 SXM4 80 Go, soit ≈ 1,4 à 2,5 USD à 1,09 USD de
  l'heure » → « **≈ 1,2 à 1,9 heure de carte A100 SXM4 80 Go (≈ 1,3 à 2,2 avec la lentille jacobienne), soit ≈ 1,3 à
  2,1 USD (≈ 1,4 à 2,4) à 1,09 USD de l'heure » ; § 3, total « **≈ 1,3 à 2,25** » → « **≈ 1,2 à 1,9 (1,3 à 2,2 avec la
  lentille jacobienne)** » ; repli (B) de P-016, « total ≈ 1,2 à 1,95 h » → « total ≈ 1,1 à 1,7 h (≈ 1,2 à 1,9 avec la
  lentille jacobienne) » ; § 4, « ≈ 1,4 à 2,5 USD de carte » → « ≈ 1,3 à 2,1 USD de carte (≈ 1,4 à 2,4 avec la lentille
  jacobienne) » ; en tête, ajouter « « P3 l. … » renvoie à `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`). » ; l. 39,
  « (P3 : ≈ 38 s par épisode **avec** génération, l. 385) » → « (pilote de T0.5 cité par P3 l. 385 : ≈ 38 s par épisode
  **avec** génération) ».

### CR2-P3b-texte-13 — mineur
- Où : texte l. 3-4, l. 186-188, l. 189-191.
- Ce qui est : (1) « fichiers écrits de 00:47 à 01:00 UTC environ » : les six fichiers sont datés 00:56:11 UTC et
  `problemes` a tourné à 00:56 UTC. (2) L'exposition dit changés les a priori de P3b-P2 et P3b-P5 ; la table
  (methode-01) dit la probabilité de P3b-P2 inchangée (70 %), seul son libellé change. (3) Aucune place n'est prévue pour
  l'exposition des contre-lecteurs du brouillon 2 (cette consigne leur ouvre R-303 et le verdict complété).
- Correction (mots exacts) : (1) « de 00:47 à 01:00 UTC environ » → « de 00:47 à 00:56 UTC environ » ; (2) « (P3b-P2 et
  P3b-P5, CR-P3b-methode-01 ; » → « (P3b-P5, CR-P3b-methode-01, et libellé de P3b-P2, probabilité inchangée ; » ; (3) après
  « de même le rédacteur du code et son vérificateur. », ajouter « De même chaque contre-lecteur R2, dans son rapport, que
  la section « Contre-lecture » cite. ».

### CR2-P3b-texte-14 — mineur
- Où : texte, liste d'arrêt (l. 698-701) ; devis § 4 (l. 70-71) ; plan l. 40.
- Ce qui est : le plafond de la phase (somme « dépense consignée + borne < 150 USD », alerte à 120 USD) et la taille
  totale de 100 Mo du contrôle des fichiers sont des gardes de la chaîne, absentes de la liste d'arrêt du texte.
- Correction (mots exacts) : ajouter à la liste d'arrêt : « Dépense consignée de la phase plus la borne de l'étape au moins
  150 USD : aucune création ; au-delà de 120 USD : alerte consignée et rapportée à Lazar avant la ligne d'accord. » et
  « Fichiers à pousser au-delà de 100 Mo au total : poussée refusée, même suite que la puce précédente. ».

### CR2-P3b-texte-15 — mineur
- Où : questions Q-13 (l. 46-47).
- Ce qui est : « Reste : 10 %, 5 points par paire, identité de la lentille (99 %, écart médian 0,05), à fixer avant le
  scellement » ; le texte les écrit comme seuils gelés (l. 413-415, l. 493-495).
- Correction (mots exacts) : « Reste : 10 %, 5 points par paire, identité de la lentille (99 %, écart médian 0,05), à fixer
  avant le scellement, jamais après. » → « Valeurs écrites au texte (10 %, 5 points par paire, identité de la lentille à
  99 % et écart médian 0,05) ; tout changement avant le scellement s'écrit avec son motif ; jamais après. ».

## Compte

15 constats : 5 bloquants (01 à 05), 4 majeurs (06 à 09), 6 mineurs (10 à 15). Aucune grandeur de P3 recopiée.
