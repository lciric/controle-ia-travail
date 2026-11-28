# Vérification courte du brouillon 3 de P3b — lentille « texte » — v1

- Vérificateur : sous-agent neuf (Claude), session 16, 2026-10-21, lu de 01:35 à 01:42 UTC, écrit de 01:42 à 01:44 UTC (heures par
  `date -u`). Je n'ai écrit ni P3b (brouillons 1 à 3, devis, plans, questions, tables), ni P3, ni aucune contre-lecture,
  projet de traitement ou traitement.
- Consigne : `…/consigne-verification-courte-P3b-brouillon3-v1.md`
  (`f3ea937ea4abaee0ee8fe7072fe116ccc9e25129e0e60071ba3954d5f95992ae`, égale à son compagnon). Préfixe `…/` =
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b`. Dépôt `R` = `/home/user/controle-ia-travail`.
- Relu (empreintes égales à leurs compagnons) : texte `…/brouillon3/P3b-seconde-lecture-v1-brouillon3.md`
  (`9430e359b2ec29694cf4b2032ce0f32591e0edf8d46e5a7db60ccb6680b37cb2`) ; devis `devis-P3b-v3.md` (`3dc920f8…`) ; plan
  `plan-code-et-chaine-P3b-v3.md` (`d950e428…`) ; questions `questions-ouvertes-P3b-v3.md` (`aff0a7ed…`) ; table
  `table-traitement-brouillon3-v1.md` (`89e67f7f…`) ; sortie `problemes-brouillon3-v1.txt` (`b4a9abc3…`) ; essais
  `travail/` (script `f0f507f2…`, journal `61d05116…`, sortie `7da28d7d…`, sans compagnons). Base : `…/brouillon2/` (texte
  `64c5adad…`, devis, plan, questions, table, sortie de `problemes` : empreintes égales). Traitement
  `…/traitement-contre-lectures-brouillon2-P3b-v1.md` (`958b4601…`) ; rapport « texte »
  `…/contre-lectures-brouillon2/texte/contre-lecture-R2-P3b-brouillon2-texte-v1.md` (`c2f68f5a…`) ; rapport « méthode »
  (`9c312900…`) : empreinte seulement. Validateur `R/src/controle_ia/prereg.py` (`3b2e3ee5…`), exécuté.
- **Exposition et écarts (déclarés).** Je n'ai ouvert aucune pièce interdite, ni aucune ligne de `R/registres/` (les dates et
  défauts des marqueurs, vérifiés au registre par la contre-lecture « texte » du brouillon 2, sont inchangés du brouillon 2
  au brouillon 3 : comparaison des marqueurs, seule différence la citation « [Décision de Lazar en attente : …] » ajoutée
  à la puce « Statut »). Aucune recherche récursive ; aucun réseau ; aucune commande git d'écriture (`git diff --no-index`
  en lecture seule, entre fichiers du bloc-notes) ; `python3 -B -I` avec `PYTHONDONTWRITEBYTECODE=1`. Le script du rédacteur
  a été relu puis rejoué **en mémoire** (aucune écriture) depuis mon propre bloc-notes. Aucune grandeur de P3 vue ni
  recopiée.

## Verdict

**Scellable après corrections.**
Les 15 constats « texte » du brouillon 2 sont appliqués, en mots exacts ou avec des écarts déclarés et justes ; le
différentiel est exactement la liste des 150 remplacements du journal ; la sortie de `problemes` est retrouvée à
l'identique. Mais la garde du scellement ne voit pas les chaînes coupées par un retour à la ligne (quatre dans le texte),
la règle générale du candidat ne dit pas qu'une version retenue écrite comme des remplacements s'applique puis se retire,
et deux replis restent incomplets (P-016 (B) : plis de lecture ; P-023 (B) : P3b-P5, ordre de lecture, portée de T4 de P3).
Corrections bloquantes : VCP3b-texte-01 à -04.

## Vérifié sans constat

- **Différentiel brouillon 2 → brouillon 3.** Le script `travail/appliquer_brouillon3_v1.py`, rejoué en mémoire sur les
  quatre pièces du brouillon 2 (heure fixée à « 01:32 », celle du journal), redonne **octet pour octet** le texte, le
  devis, le plan et les questions du brouillon 3 ; 150 remplacements, chacun trouvé une seule fois. Rien d'autre ne change.
  Chaque remplacement porte un constat ou un changement déclaré à la table (« Changements qui ne viennent d'aucun
  constat ») ; les marqueurs de décision sont inchangés.
- **Sortie de `problemes` rejouée** (2026-10-21T01:35Z, `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=R/src python3 -B`, depuis
  `…/brouillon3/`) : identique à la dernière ligne de `problemes-brouillon3-v1.txt` et à `travail/sortie-problemes.txt`
  (section « Contre-lecture » à remplir ; 23 marqueurs, dont `<<ISSUES_DECISIONS_P3B>>`, `<<ISSUE_P016>>`,
  `<<ISSUE_P017>>`, `<<LIGNE_ISSUE_P4>>` neufs et `<<LIGNE_VERDICT_P4>>` disparu).
- **Constats « texte » du brouillon 2, en mots exacts** : -01 (deux replis de P-023, l. 152 et l. 188) ; -02 (l. 71,
  l. 327-334, Plan point 1 : plus de « en version (A) » ni « (version (A)) ») ; -03 (plan l. 74 en mots exacts ; l. 708 et
  l. 766 ; trois cellules l. 196-198 ; Q-23) ; -04 (puce « Statut », avec l'étiquette « Version (A), recommandée : »
  ajoutée et le retrait des phrases qui portent les chaînes refusées : écarts justes, déclarés) ; -05 (cinq parties, écarts
  déclarés : ordre des retraits, branches « spécification », parenthèse de H-P3b-1, règle de choix gardée — justes, mais
  voir VCP3b-texte-04) ; -06 ; -07 ((1), (2), (4) exacts ; (3) fondu avec -11, voir VCP3b-texte-07) ; -08 ((1) exact ;
  (2) règle dans les guillemets, consigne de l'étape 2.6 hors guillemets : écart juste, voir VCP3b-texte-02) ; -09 ; -10 ;
  -11 (plus l'étape « brouillon 3 ; vérification courte », décision 6 du traitement) ; -12 (fondu avec CR2-methode-04 :
  sommes refaites, justes : 1,25 à 1,95 h, 1,35 à 2,25 h, 1,4 à 2,1 USD, 1,5 à 2,5 USD ; borne 7,5 USD inchangée) ; -13 ;
  -14 ; -15.
- **Scellement, au singulier et au pluriel, sans égard à la casse** : « de repli » couvre « Versions de repli », « versions
  de repli » ; « en attente » est invariable. Juste, aux coupures de ligne près (VCP3b-texte-01).
- Replis de N-032 (texte, liste d'arrêt, devis, plan) et de P-024 (texte, devis, plan, contrôle des fichiers) : présents
  partout, montants égaux (8,6 USD ; + 2,16 USD).

## Constats

### VCP3b-texte-01 — bloquant — la garde du scellement ne voit pas une chaîne coupée par un retour à la ligne
- Où : plan l. 74 (`sceller_p3b_v1.sh`) ; texte l. 34-35 (« Statut »).
- Ce qui est : la recherche est écrite sur la chaîne brute. Dans le texte, quatre occurrences sont coupées par un retour à
  la ligne : l. 118-119 (« Version de / repli (B) de P-016 »), l. 383-384 (« Décision de Lazar en / attente : P-023 », un
  marqueur), l. 617-618 (« (Version de / repli (B) de P-016 : 40) »), l. 751-752 (« Version de / repli (A) de N-032 »).
  Compte (mon essai, texte du brouillon 3) : « en attente » 11 occurrences brutes, 12 après réduction des blancs ; « de
  repli » 35 et 38. Un marqueur oublié de cette forme passerait la garde (R5 : l'artefact ne couvre pas ce cas).
- Correction (mots exacts) : plan l. 74, « **refuse tout texte qui contient « en attente », « de repli » ou « Proposition en
  attente », sans égard à la casse** (cas sain : candidat sans ces chaînes ; artefacts : chacune, au singulier et au
  pluriel) » → « **refuse tout texte qui contient « en attente », « de repli » ou « Proposition en attente », sans égard à la
  casse ni aux blancs (toute suite d'espaces et de retours à la ligne lue comme une espace)** (cas sain : candidat sans ces
  chaînes ; artefacts : chacune, au singulier et au pluriel, et chacune coupée par un retour à la ligne suivi d'espaces) » ;
  texte l. 34-35, « le scellement refuse « en attente » et « de repli », sans égard à la casse. » → « le scellement refuse
  « en attente » et « de repli », sans égard à la casse ni aux retours à la ligne. ».

### VCP3b-texte-02 — bloquant — règle du candidat : une version retenue écrite comme des remplacements
- Où : texte l. 28-35 (« Statut ») ; replis écrits comme des remplacements : P-023 (B) et (C) (l. 147-191), N-031 (l. 262-267),
  N-032 dans l'Ordre (l. 803-807), P-024 (C) (l. 831-832) ; phrase l. 144-146 ; renvois l. 558-559, l. 708, l. 766.
- Ce qui est : (1) la règle dit que la version retenue « reste seule, mot pour mot, sans son étiquette ni ses guillemets ».
  Pour un repli écrit comme une liste de remplacements, appliquée à la lettre, elle laisse ces consignes dans le texte scellé
  sans les appliquer ; l'ordre (remplacer dans le texte principal après le retrait des replis, que la table du rédacteur
  laisse à la vérification) n'est pas écrit. (2) Deux phrases de repli n'ont pas d'étiquette et ne contiennent aucune chaîne
  refusée : « En (b) ou en (c), dans la ligne G5 … » (l. 262) et « En (C), à l'étape 2.6, … » (l. 831) ; oubliées en (a) ou
  en (A), elles passent la garde. (3) La liste des phrases retirées au candidat omet les trois renvois « (Version de repli
  (B) de P-023 … section « Périmètre ».) » (en (B), « (section « Périmètre ».) » resterait) et la phrase « Les choix de sonde
  de la version (A) … chacun avec un renvoi à P-023. », fausse une fois les marqueurs de P-023 retirés de « Métrique ».
- Correction (mots exacts) : (1) l. 31, « ni ses guillemets. Issues des décisions » → « ni ses guillemets ; une version
  retenue écrite comme des remplacements (« devient », « à la place de », « est retiré », « remplacements mot pour mot ») ne
  reste pas : elle s'applique mot pour mot au texte principal, après le retrait des marqueurs et des autres versions, puis
  elle est retirée. Issues des décisions » ; l. 33-34, « (la phrase « Au candidat, pour chaque décision marquée … ni ses
  guillemets. », celle-ci, et la dernière phrase de la puce « Partition ») » → « (la phrase « Au candidat, pour chaque
  décision marquée … puis elle est retirée. », celle-ci, la dernière phrase de la puce « Partition », la phrase « Les choix
  de sonde de la version (A) … chacun avec un renvoi à P-023. » et les trois renvois « (Version de repli (B) de P-023 …
  section « Périmètre ».) » de « Seuil », de la table O et de la liste d'arrêt) ». (2) l. 262, « En (b) ou en (c), dans la
  ligne G5 » → « Versions de repli (b) et (c) de N-031, suite : dans la ligne G5 » ; l. 831, « En (C), à l'étape 2.6, » →
  « Version de repli (C) de P-024, suite : à l'étape 2.6, ».

### VCP3b-texte-03 — bloquant — repli (B) de P-016 : plis de lecture incomplets
- Où : texte l. 450 (T4 résiduel) ; l. 578-583 (Plan d'analyse, point 1). Présent depuis le brouillon 2 (l. 395, l. 508-509).
- Ce qui est : (1) « (sondes génériques : `plis/lecture-60` ; oracle » n'a pas de version (B) : en (B), les plis de T4
  résiduel des sondes génériques couvriraient les 20 tâches réservées (contre la puce d'arrêt l. 750). (2) Au point 1, la
  version (B) se place entre la phrase de la partition et « Plis : clés `plis/decouverte` (5 × 4), `plis/confirmation`
  (5 × 8) et `plis/lecture-60` (5 × 12). », que rien ne remplace : en (B), le texte scellé porterait `plis/confirmation`
  5 × 4 et 5 × 8, `plis/lecture-40` et `plis/lecture-60`.
- Correction (mots exacts ; retours à la ligne lus comme des espaces) : (1) l. 450, « (sondes génériques :
  `plis/lecture-60` ; oracle » → « (sondes génériques : `plis/lecture-60`, Version de repli (B) de P-016 :
  `plis/lecture-40` ; oracle » ; (2) l. 579-582, « la confirmation. Version de repli (B) de P-016 : « 20, 20, puis 20
  réservées ; plis `plis/confirmation` 5 × 4, l'oracle du pli k apprenant sur la découverte et 16 tâches de confirmation ;
  plis `plis/lecture-40` 5 × 8. » Plis : clés `plis/decouverte` (5 × 4), `plis/confirmation` (5 × 8) et `plis/lecture-60`
  (5 × 12). » → « la confirmation. Plis : clés `plis/decouverte` (5 × 4), `plis/confirmation` (5 × 8) et `plis/lecture-60`
  (5 × 12). Version de repli (B) de P-016, à la place du texte qui précède depuis « les 20 premiers » : « les 20 premiers
  forment la découverte, les 20 suivants la confirmation, les 20 derniers sont réservés. Plis : clés `plis/decouverte`
  (5 × 4), `plis/confirmation` (5 × 4 ; l'oracle du pli k apprend sur la découverte et 16 tâches de confirmation) et
  `plis/lecture-40` (5 × 8). » ».

### VCP3b-texte-04 — bloquant — repli (B) de P-023 : prédiction, ordre de lecture et portée de T4 de P3
- Où : repli (B), l. 186-188 ; touchés : P3b-P5 (l. 317), Plan d'analyse point 3 (l. 605-607), audit R4 (l. 657-658),
  H-P3b-2 (l. 286-287), G5 (l. 692), G6 (l. 693), O5 (l. 704), O7 (l. 706).
- Ce qui est : (1) en (B), P3b-P5 devient « (oracle, T4 de P3) », mais sa prédiction gelée reste « aire du résidu de l'oracle
  au-dessus de son plancher », grandeur descriptive en (B). (2) Le point 3 du plan (« P3-P4 et T1, T3, T4 résiduel des
  sondes génériques retenues ; T1, T3, T4 résiduel de l'oracle ») et l'audit (« leur contrôle est T4 résiduel ») ne sont pas
  dans la liste des renommages. (3) En (B), T4 de P3 ne stratifie que le coût déclaré (puce du repli ; écart (v) : « confondu
  par le coût de la tâche ») ; H-P3b-2, G5, O7 et les motifs de G6, O5 et P3b-P5 disent encore une séparation de « la
  tâche » et des « coûts déjà déclarés » ou de « l'historique ».
- Correction (mots exacts), dans le repli (B) : « dans H-P3b-1, H-P3b-2, P3b-P2, P3b-P5, « Famille principale » et les tables
  G, O et Synthèse, « T4 résiduel » devient « T4 de P3 » » → « dans H-P3b-1, H-P3b-2, P3b-P2, P3b-P5, « Famille
  principale », le point 3 du « Plan d'analyse », la phrase « leur contrôle est T4 résiduel » de l'audit R4 et les tables G,
  O et Synthèse, « T4 résiduel » devient « T4 de P3 » ; dans P3b-P5, « aire du résidu de l'oracle au-dessus de son
  plancher » devient « aire de l'oracle stratifiée par quintiles du coût déclaré (T4 de P3) au-dessus de son plancher » ;
  partout, dans cet ordre : « ni au nombre écrit, à la tâche ou aux coûts déjà déclarés » devient « ni au nombre écrit » ;
  « du nombre écrit, de la tâche et des coûts déjà déclarés » devient « du nombre écrit » ; « ni au nombre écrit, ni à la
  tâche ou aux coûts déjà déclarés » devient « ni au nombre écrit » ; « non séparé du nombre écrit, de la tâche ou de
  l'historique des coûts » devient « non séparé du nombre écrit » ; « non séparé du nombre écrit, de la tâche ou de
  l'historique » devient « non séparé du nombre écrit » ; dans P3b-P5, « non séparé du nombre, de la tâche ou de
  l'historique » devient « non séparé du nombre écrit » ». Les a priori de P3b-P2 et P3b-P5 (« recouvrement faible ») sont
  laissés à la lentille « méthode » (point déclaré par le rédacteur).

### VCP3b-texte-05 — mineur — repli (C′) de P-017 : il retire la version (A) qu'il dit garder
- Où : texte l. 114-115.
- Ce qui est : par la règle du candidat, la version retenue reste seule ; en (C′), la phrase de la version (A) (« P3b lit
  N-028 et la double comptabilité, rien d'autre … ») est retirée et « P3b garde la version (A) » ne renvoie plus à rien.
- Correction (mots exacts) : « P3b garde la version (A). » → « P3b lit N-028 et la double comptabilité, rien d'autre ; la
  sonde de valeur, le rejeu contrefactuel et la manipulation du nombre écrit restent hors périmètre de P3b (tableau
  ci-dessous). ».

### VCP3b-texte-06 — mineur — replis (b) et (c) de N-031 : l'écart (iv) perd son motif ; (c) dit « tentative » pour tout
- Où : texte l. 264-265.
- Ce qui est : l'écart (iv) neuf n'a plus le motif ajouté par CR2-P3b-texte-10 ; en (c), l'oracle et la double comptabilité
  restent en diagnostic, mais (iv) dit « tentative de détection » sans distinction.
- Correction (mots exacts) : « L'écart (iv) devient « (iv) tentative de détection déclarée non aveugle (N-031), aucune
  règle pour G0 (l. 157) » » → « L'écart (iv) devient, en (b), « (iv) tentative de détection déclarée non aveugle (N-031),
  aucune règle pour G0 (l. 157 ; motif : les bras localisés relisent un champ déjà lu par T2 et par l'addendum 1, sur des
  données déjà lues) » et, en (c), « (iv) sondes génériques sur W en tentative de détection déclarée non aveugle, oracle et
  double comptabilité en diagnostic (N-031), aucune règle pour G0 (l. 157 ; même motif) » ».

### VCP3b-texte-07 — mineur — Ordre, repli (A) de N-032 : M-P3b-2 placée avant les réponses de Lazar
- Où : texte l. 803-805 ; plan § 4.
- Ce qui est : la fusion avec CR2-texte-11 place « mesure M-P3b-2 avant le scellement » avant « réponses de Lazar ou défauts
  échus » ; or (A) n'existe que par la réponse de Lazar à N-032.
- Correction (mots exacts), aux deux endroits : « « mesure de conception M-P3b-1 (puissance) ; mesure M-P3b-2 avant le
  scellement (par condition, règle de P3b-P0, sortie brute scellée) ; » à la place de « mesure de conception M-P3b-1
  (puissance) ; » » → « « N-032 sans réponse vaut (C)) ; mesure M-P3b-2 avant le scellement (par condition, règle de
  P3b-P0, sortie brute scellée) ; » à la place de « N-032 sans réponse vaut (C)) ; » ».

### VCP3b-texte-08 — mineur — titres des pièces v3
- Où : devis l. 1, plan l. 1, questions l. 1.
- Ce qui est : les fichiers v3 portent encore « — v2 » (et « brouillon 2 » pour les questions) (R12).
- Correction (mots exacts) : devis, « (passe sur carte de la seconde lecture de P3) — v2 » → « (passe sur carte de la seconde
  lecture de P3) — v3 » ; plan, « # Plan du code et de la chaîne de P3b — v2 » → « # Plan du code et de la chaîne de P3b —
  v3 » ; questions, « # Questions ouvertes de P3b, brouillon 2 — v2 » → « # Questions ouvertes de P3b, brouillon 3 — v3 ».

### VCP3b-texte-09 — mineur (hors lentille, présent depuis le brouillon 2 ; à confirmer par la lentille « méthode ») — G6
- Où : texte l. 693.
- Ce qui est : l'issue de G6 dit « l'un de T1, T3, T4 résiduel non établi », alors que O5 distingue « non établi ou non
  calculable » ; dans les motifs, « T4 résiduel non calculable (recouvrement) » suit « sinon T4 résiduel non établi » sans
  « sinon » : soit un T4 résiduel non calculable n'entre dans aucune ligne G, soit sa branche n'est jamais atteinte.
- Correction (mots exacts) : « l'un de T1, T3, T4 résiduel non établi | » → « l'un de T1, T3, T4 résiduel non établi ou non
  calculable | » ; « ; sinon T4 résiduel non établi → « non séparé du nombre écrit, de la tâche ou de l'historique à cette
  puissance » ; T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit (recouvrement
  insuffisant) » ; » → « ; sinon T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit
  (recouvrement insuffisant) » ; sinon T4 résiduel non établi → « non séparé du nombre écrit, de la tâche ou de
  l'historique à cette puissance » ; » ; dans le repli (B) de P-023, « dans G6, « ; T4 résiduel non calculable
  (recouvrement) → « le plan ne sépare pas le score du nombre écrit (recouvrement insuffisant) » » est retiré » → « dans G6,
  « sinon T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit (recouvrement
  insuffisant) » ; » est retiré ».

## Compte

9 constats : 4 bloquants (01 à 04), 5 mineurs (05 à 09, dont 09 hors lentille). Aucune grandeur de P3 recopiée.
