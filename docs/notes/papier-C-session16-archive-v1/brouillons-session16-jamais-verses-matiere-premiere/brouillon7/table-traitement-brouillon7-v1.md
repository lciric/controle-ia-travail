# Papier C — table de traitement du brouillon 7 du préenregistrement (HC1 à HC3) — v1

Rédacteur neuf du brouillon 7 (sous-agent, session 16, 2026-10-21, de 02:22 à 02:40 UTC environ, heures lues par
`date -u`). Je n'ai écrit ni les brouillons 1 à 6, ni les brouillons 1 à 3 de la configuration, ni aucune contre-lecture,
note, projet de traitement ou traitement du papier C. Une ligne par constat : identifiant, décision de la session,
passage du brouillon 7 ou « non appliqué » et pourquoi, écart éventuel (renvoi à la section « Écarts »). « Mots
exacts » : les mots du rapport cité ; les seuls écarts sont ceux de la section « Écarts ».

## Pièces (empreintes recalculées, toutes égales à leurs compagnons `.sha256`)

- Consigne : `…/consigne-redacteur-brouillon7-v1.md` (`e8bfb03bab6b81b882b9cd85f7dcdde3ed209af420159a14fd21596d2d22b48e`).
- Base : brouillon 6 `…/brouillon6/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md`
  (`fadc74c3b40b6e6aee9035f5a9566288d17d60b8403b57863721c2ee57554d00`) ; configuration brouillon 3
  `…/brouillon6/papier-C-config-v1-brouillon3.json` (`85173b22defe2c55844f23691028233a13746394324d0c598d3a66fb4f68820d`) ;
  table et outils `…/brouillon6/` et `…/brouillon6/travail/` (compagnons vérifiés par `sha256sum -c`).
- Rapports appliqués (tous les constats acceptés par la session) : texte et conformité
  `…/contre-lectures-brouillon6/texte/contre-lecture-R2-brouillon6-texte-v1.md`
  (`68fc0dc9f6f0f5305587cc09d1a2762e5cfbf90c8701d2a19cdddea66599b3a9` ; manifeste des essais
  `da5bbad06c8fd7ca6e394f0a16129405c8440f9acf73746c68f331a296a68ad3`, `sha256sum -c` sans échec) ; vérification courte de
  méthode `…/contre-lectures-brouillon6/methode-courte/contre-lecture-R2-brouillon6-methode-courte-v1.md`
  (`45a0d87569d883c72af7720081278e67298c3a2f9daaecf03c197b909431fd46` ; manifeste des simulations
  `368f3ec867c05991ce4069c2854dc17aa61a508cb8e2462b18764654cb975bed`, `sha256sum -c` sans échec).
- Dépôt, lecture seule : `registres/decisions.md`, lignes P-020, P-021, P-022 et R-316 (R-316 écrit les décisions de
  la session sur ce brouillon : réserve 17, constat nu au pilote, page de l'éditeur ; aucune ligne de correction de
  P-021 ; aucune réponse de Lazar sur P-020, P-021, P-022) ; `src/controle_ia/prereg.py`
  (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`), motifs des marqueurs et des entrées
  « Contre-lecture k » seulement.
- Sorties, sous `…/brouillon7/` : configuration `papier-C-config-v1-brouillon4.json`
  (`6734fbd0a608e9bd2c7624286cfd2654ca524c5262e0854619705c72b70ebc3a`) ; cette table ; texte
  `papier-C-preenregistrement-HC1-HC3-v1-brouillon7.md` (empreinte dans son compagnon et dans
  `problemes-brouillon7-v1.txt`) ; sortie de `problemes`. Outils, sous `travail/` (compagnons) :
  `ecrire_config_brouillon4_v1.py` (`1b3dc311ca06b349cf95bf5717b8c661b1cfbd1e7777375cce2d037f0f331712`) et son journal
  (`e0b058b07e9a4f46316087b8b77fe90a864b27629b44befd6bfd7c207a9c40fe`) ; `construire_brouillon7_v1.py`
  (`dec0704ebba469723100f718eef4d0c81d2840622e49a193aee7718608cb6092` ; chaque changement est un remplacement exact,
  trouvé une seule fois dans le texte courant, sinon arrêt) et son journal ; contrôles : `structure_config_v1.py`
  (structure sans texte), `voir_regles_masquees_v1.py` (champs de règles nommés, masqués s'ils recoupent un texte
  sensible sur 12 caractères), `enonces_b6_b7_v1.py` (énoncés égaux) ; essai de construction sous `travail/essais/`.

## 1. Décisions de la session (consigne, « Décisions de la session, à écrire » ; registre, R-316)

| décision | passage du brouillon 7 | écart |
|---|---|---|
| 1. CB6-texte-03 : réserve 17, étiquette descriptive, vivier inchangé | Plan, section 7, réserve 17 (mots exacts du rapport) ; « Ce que change le brouillon 7 » | E-07 |
| 2. CB6-texte-05 : constat nu lu au pilote, point 1.4, lisibilité seulement, sous le marqueur de P-022 | point 1.4 (bloc P-022 : version (b) en mots exacts du rapport ; repli (a) ou (c)) ; TC.1, bloc P-022 (mots exacts) ; configuration `constat_nu.pilote` | E-04 |
| 3. `<<DECISION_ECART_EDITEUR>>` | verrou 2, phrase « Page de l'éditeur reçue … » : la parenthèse « décision de la session » porte les mots de la consigne | E-06 |
| 4. `<<DECISION_VOISINS>>` | champs du scellement, « Décisions » (mots de la consigne) ; HC1, quatre blocs d'ajouts : renvoi aux champs | E-05 |
| Décisions de Lazar P-020, P-021, P-022 | non tranchées : marqueurs `<<TRANCHER_P021>>` (6 en-têtes), `<<TRANCHER_P020>>` (2), `<<TRANCHER_P022>>` (9 en-têtes, dont 2 ajoutés au point 1.4), chacun nommé une fois de plus au verrou 1 ; `<<DECISION_STABILITE_RANG>>`, `<<DECISION_BRAS_USURPATION>>`, `<<DECISION_CONSTAT_NU>>` gardés ; configuration « en attente » dans les trois champs | — |

## 2. Lentille « texte et conformité » (`68fc0dc9…`)

| constat | décision | passage du brouillon 7 | écart |
|---|---|---|---|
| CB6-texte-01 (majeur) | accepté | point 1 : verrou 1 (exception P-021) ; point 2 : bloc P-021, repli (B) de la prédiction ; point 3 : repli (C) de la prédiction ; point 4 : critères, repli (B) ; point 5 : Seuil, C-P3 ; point 6 : configuration `stabilite_rang.repli_si_refus.B` et `.C` | E-01 (« deux lectures » lu « trois lectures ») |
| CB6-texte-02 | accepté | Métrique, point 5, repli (a) ou (c) ; TC.1, replis (a) et (c) ; réserve 9 : corps, bloc recommandé, bloc de repli (mots exacts) | — |
| CB6-texte-03 | accepté (décision 1) | réserve 17 ; ligne CW-04 : « appliqué (réserve 17) » ; verrou 5 : contenu de `essais/` versé sous `docs/notes/contre-lectures-papier-C-v1/brouillon6/texte/` | E-07 |
| CB6-texte-04 | accepté | réserve 14, après « à côté de chaque formulation retenue qui la porte. » (mots exacts) | — |
| CB6-texte-05 | accepté (décision 2 : lecture au pilote) | point 1.4 ; TC.1, bloc P-022 (« Lue au pilote pour la lisibilité seulement (point 1.4) ; … ») ; configuration `constat_nu.pilote` à l'avenant | E-04 |
| CB6-texte-06 | accepté | liste d'arrêt 11 (mots exacts) | — |
| CB6-texte-07 | accepté | graines (« Clés ajoutées par le brouillon 5 : ») ; champs du scellement et configuration `statut` (« `stabilite_rang` (…), `agent_bras` (…) et `constat_nu` (…) ») ; réserve 14 (« Vivier, constantes et longueurs inchangés ; configuration inchangée par cette déclaration. ») | — |
| CB6-texte-08 (information) | accepté | P-020 : le bloc P-020 cite R-312 (« avec R-312 pour sa transmission et son défaut ») ; `<<DECISION_VOISINS>>` : décision 4, les deux noms écrits ; CR2-03 : décision 3 (« vaut pour le résumé et le corps ») ; copie publique : phrase ajoutée à « Confidentialité » ; verrou 5 : `construire_brouillon6_v1.py` et son journal ajoutés aux versements | E-11 ; lignes du registre (P-020, CR2-03, voisins) : à la session |
| CB6-texte-09 (information) | — | aucune action | — |
| CW-04 (table du brouillon 6, « à vérifier par la session ») | vérifié par la contre-lecture « texte » (CB6-texte-03) | appliqué (réserve 17) | — |

## 3. Lentille « vérification courte de méthode » (`45a0d875…`)

| constat | décision | passage du brouillon 7 | écart |
|---|---|---|---|
| CB6-methode-courte-01 (majeur) | accepté ; correction de P-021 transmise par la session | point 1 : bloc P-021, « Trois lectures » ; point 2 : critères ; point 3 : Seuil, C-P3 ; « Ce que change le brouillon 6 » (rappel) ; point 4 : réserve 15 ; point 5 : configuration `stabilite_rang.trois_lectures` (à la place de `deux_lectures`), `lecture_recommandee`, `etape2.loi_nette.lecture_rho_sur_r` ; point 6 : point 8 bis, test du module ; ligne du registre : marqueur `<<LIGNE_CORRECTION_P021>>` au verrou 1 | E-01, E-02 |
| CB6-methode-courte-02 (majeur) | accepté | bloc P-021, « Clause de repli mécanique » (mots exacts) ; configuration `stabilite_rang.clause_repli` (même texte) ; application : verrou 6 et contre-lecture 8 (grille entière à refaire sur le texte corrigé) | E-03 |
| CB6-methode-courte-03 | accepté | point 8 bis, après « au plus 0,05 chacun » (mots exacts) | — |
| CB6-methode-courte-04 (majeur, processus) | accepté : branche « écrire au verrou 6 » (la branche « confier à un sous-agent » reste à la session) | verrou 6 (mots exacts, marqueur nommé `<<CHEMIN_RAPPORT_CL10>>`) ; section « Contre-lecture » : contre-lecture 8 recentrée, contre-lecture 10 ajoutée avec ses marqueurs | E-03 |
| CB6-methode-courte-05 (information) | — | aucune action (aucune correction demandée) | — |
| CB6-methode-courte-06 | accepté | bloc P-021, C-P3b, colonne « établie » : « p = (1 + #{τ* ≥ τ}) / (B + 1) » ; configuration `stabilite_rang.C_P3a` (« ≤ 0,05 » après la valeur p exacte) | E-10 (formule aussi dans `stabilite_rang.C_P3b`) |
| CB6-methode-courte-07 (information) | — | aucune action | — |

## 4. Écarts du rédacteur

- **E-01** — CB6-methode-courte-01 renomme le paragraphe « Deux lectures » en « Trois lectures » et la clé `deux_lectures`
  en `trois_lectures`. Les corrections de CB6-texte-01 qui les nomment sont lues en conséquence : verrou 1 (« Trois
  lectures », deux fois) ; repli (B) de la prédiction (« trois lectures et clause de repli comprises ») ; repli (C) de la
  prédiction (« aux trois lectures ») ; configuration `repli_si_refus.B` (« aux trois lectures (trois_lectures) ») et
  `.C` (« aux trois lectures »). Même lecture pour l'en-tête du bloc P-021 (« aux trois lectures de la loi nette »), que
  le constat ne liste pas. Les replis (B) et (C) héritent ainsi des trois lectures de la version (A) : la session le
  dit dans sa ligne de correction de P-021.
- **E-02** — `<<LIGNE_CORRECTION_P021>>` (marqueur neuf, verrou 1) : la ligne du registre qui transmet la correction
  de P-021 n'existe pas encore (R-316 ne la porte pas) ; le marqueur fait refuser le scellement par `problemes` tant
  qu'elle n'est pas citée (R5). Le registre est aussi cité aux « Documents » (« et sa ligne de correction, verrou 1 ») ;
  la configuration (`stabilite_rang.decision`) dit la correction, sans marqueur.
- **E-03** — Verrou 6 : mots exacts de CB6-methode-courte-04, le marqueur `<<…>>` nommé `<<CHEMIN_RAPPORT_CL10>>` ; la
  liste des points (v) à (viii) reprise de l'ancien verrou 6 ; une phrase de moi dit que la contre-lecture 8 porte sur
  le texte corrigé et sur toute la grille de la clause (CB6-methode-courte-02 : « à refaire en entier par la
  contre-lecture qui suit le brouillon 7, si le constat 01 est appliqué »). Section « Contre-lecture » : entrée 8
  recentrée (CL5-01 à CL5-03) ; entrée 10 ajoutée avec ses trois marqueurs, sur le modèle de l'écart E-02 du brouillon 6,
  pour que `problemes` bloque tant qu'elle manque. Les marqueurs des contre-lectures 8 et 9 ne sont pas remplis par les
  rapports du brouillon 6 (voir « Points pour la session »).
- **E-04** — Point 1.4 : la version (b) est la phrase de CB6-texte-05 en mots exacts, posée sous le marqueur de P-022
  sans « Version recommandée » (pour que la phrase soit celle du texte scellé, comme CB6-texte-02 le demande) ; le
  repli (a) ou (c) est de moi, sur le modèle de CB6-texte-02 : « Aucune insertion « constat nu » n'est lue au pilote
  (décision de Lazar P-022, option (a) ou (c)). » Configuration `constat_nu.pilote` : texte de moi, à l'avenant (point
  1.4 : corpus A, tous les contenus de calibrage, consigne A, mode direct, variante retenue ; hors gains du vivier et
  addendum). TC.1, bloc P-022 : « configurations brouillon 3 et brouillon 4 : aucune correspondance » (gardes rejouées).
- **E-05** — `<<DECISION_VOISINS>>` (cinq occurrences) : la décision, en mots de la consigne, est écrite une fois, aux
  champs « Décisions », avec la consigne citée ; les quatre blocs d'ajouts de HC1 renvoient à ces champs (« routine de
  la session (champs du scellement, « Décisions ») »), sans répéter la liste.
- **E-06** — `<<DECISION_ECART_EDITEUR>>` : le brouillon 6 l'avait rempli par l'amendement 3 du traitement du brouillon 5
  (« noté, sans effet sur le contenu ») ; ce remplissage est remplacé par la décision de la session, en ses mots, avec
  R-316 cité comme dans la décision.
- **E-07** — Réserve 17 : texte du rapport en mots exacts ; une phrase ajoutée à la fin : « Déclaration décidée par la
  session, comme pour R-309 (R-316). » Le chemin de la sortie est celui du rapport (`…/brouillon6/texte/…`, contenu de
  `essais/` versé à plat, verrou 5). Je n'ai pas refait de contrôle par indices de la personne grammaticale (la session
  a décidé sur le contrôle du rapport) ; le vivier est égal par empreinte à celui du brouillon 3, donc au vivier compté.
- **E-08** — Ajouts de provenance (R6, R12), de moi : historique (entrée du brouillon 6) ; « Ce que change le brouillon
  7 » et en-tête du rappel du brouillon 6 ; « Pièces de contre-lecture citées » (deux rapports, manifestes, sorties U1,
  U2, U3 dont les chiffres sont cités, avec empreintes complètes) ; « Documents qui font foi », registre (R-316) ;
  section « Contre-lecture », paragraphe des contre-lectures du brouillon 6 (empreintes abrégées seulement, pour ne pas
  masquer une entrée manquante, comme l'écart E-01 du brouillon 6) ; verrou 5, série du brouillon 6 (au-delà de
  `construire_brouillon6_v1.py` : brouillon 6, configuration brouillon 3, dossiers des deux rapports, consigne et table
  du brouillon 7, `construire_brouillon7_v1.py`, `ecrire_config_brouillon4_v1.py`, avec journaux).
- **E-09** — Configuration brouillon 4 nommée là où le texte nommait le brouillon 3 comme brouillon relu : champs du
  scellement (brouillon relu, provenance en chaîne jusqu'au brouillon 1, « Les quatre scripts … ») ; verrou 6
  (contre-lecture 7 : « configuration brouillon 4 »).
- **E-10** — Configuration, en plus des corrections demandées : formule de p dans `stabilite_rang.C_P3b` (accord avec
  le texte, CB6-methode-courte-06) ; phrase de la correction de P-021 dans `stabilite_rang.decision` ;
  `constat_nu.gardes` nomme aussi `ecrire_config_brouillon4_v1.py`. Champs figés vérifiés égaux par empreinte : juges,
  agent, échelle, consignes, raisonné, contenus neutres, fentes, insertion, vivier, témoins, règle des témoins, gardes,
  graines, confidentialité, pilote, dérivation, partage des tâches, contrôle de rédaction, paragraphes de bras et
  `decision_bras_usurpation`, et tous les champs du constat nu sauf `pilote` et `gardes` ; `etape2` égal hors la clé
  ajoutée. Aucune clé de graine neuve. Longueurs et gardes rejouées (vivier, témoins, constat nu) : aucun échec.
- **E-11** — CB6-texte-08 : la copie publique devient une phrase de « Confidentialité » (décision de Lazar sur
  `scripts/depot_expurge.py`) ; le bloc P-020 cite R-312 (le rapport dit « peut citer »).
- **E-12** — Rien n'est tranché : aucune version de P-020, P-021 ni P-022 n'est retirée ; les marqueurs restent.
- **Nœuds** : aucune correction n'exige de changer un énoncé (vérifié : `enonces_b6_b7_v1.py`, lignes égales), une
  famille, une constante ou une longueur ; aucune n'a donc été écartée pour ce motif. CB6-methode-courte-01 change le
  contenu d'une option d'une décision de Lazar en attente : la session l'a accepté et le transmet (E-02).

## 5. Points pour la session (non tranchés ici)

- Écrire au registre la ligne de correction de P-021 (trois lectures, et l'héritage par (B) et (C), E-01) avant le
  défaut, puis remplir `<<LIGNE_CORRECTION_P021>>` ; dire si le défaut de 48 heures court de la transmission initiale
  ou de la correction.
- Lignes du registre demandées par CB6-texte-08 : P-020 (date et état périmés, R-312 à côté) ; CR2-03 (la décision
  vaut pour le corps) ; décision des voisins nommant Jiang et al. et Wang K. et al. (R-316 ne les nomme pas).
- Contre-lectures 8 et 9 : dire si les rapports du brouillon 6 (`45a0d875…`, `68fc0dc9…`) en remplissent les marqueurs
  ou si de nouvelles contre-lectures du brouillon 7 le font ; la vérification courte de méthode demande de refaire la
  grille entière après la correction 01. Verrou 7 : la contre-lecture « texte » du brouillon 6 juge la déclaration
  suffisante ; le verrou peut être levé par la session.
- CB6-methode-courte-04 : confier les points (v) à (viii) à un sous-agent neuf (contre-lecture 10).
