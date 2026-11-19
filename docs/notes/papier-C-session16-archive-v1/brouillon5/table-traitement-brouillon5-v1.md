# Papier C — table de traitement du brouillon 5 du préenregistrement — v1

Rédacteur neuf du brouillon 5 (sous-agent, session 14, 2026-10-20, R-301). Je n'ai écrit ni les brouillons 1 à 4, ni la
configuration (brouillon 1), ni les notes Panin et voisins, ni aucun rapport de contre-lecture, ni la table de traitement
de la session. Une ligne par constat des six rapports : identifiant, gravité, décision de la session, application (où) ou
mise à l'écart (pourquoi), écart éventuel. Sections citées : celles du brouillon 5.

## Pièces

- Entrées (empreintes recalculées, toutes égales à leurs compagnons) : brouillon 4
  `papier-C-preenregistrement-HC1-HC3-v1-brouillon4.md` (`40bf1d4f7ca0c8ea0927230bade704980bb75e5b0ea57f5e6e68761803035517`) ;
  configuration `papier-C-config-v1-brouillon1.json` (`348379fbcaa1fad96e8e35289d8a016dea4f1ae072f779a138ad50b86ed4a4e1`) ;
  `points-ouverts-brouillon4-v1.md` (`babe4b4d64d697b8d0a72705e1ad89dbd2cb160d88c239c007495c00c1a5145f`) ; table de la
  session `traitement-contre-lectures-brouillon4-papier-C-v1.md`
  (`f2c6a3604adfce293fa2e2bf232ae7305790d33b06eaf9a0af6d1efd5ef25da4`) ; rapports : méthode
  (`0f1cf812ab2f7b081c078f5795ad244851684ce938f15f19c91d1284d93930c8`), texte
  (`08618f6be733bbfb777fad8e677c9853c0401ba639274aa266e57300266b9bff`), Panin
  (`6b350e992afd196d3d110559aafc0da22028daef7d5dceb044d6c19f487cb247`), voisins
  (`09f14364319ea87231e5bdf2a4b525d15d2657bff0c27dfd350b7fc532b29541`), note Panin
  (`c06488a5a9bfd2850c5b9bc8317b87240885526f1f6ec42e9b6ff3b0ac0506f8`), note voisins
  (`2c720d22269bd7f8f523f0024b342c86c59acb350277759cffccd1e610c4a533`) ; simulations de la lentille méthode (manifeste
  `eea3321500009995c0ffb035806e19f033574deb9889e9a9eb0bb37761062c71`, 26 fichiers conformes). Dans le dépôt (lecture
  seule) : `registres/decisions.md` (`6d033ecf…`, lignes R-294, P-019, P-020), `registres/go.md` (`0ede5bed…`,
  GO-2026-10-20-07 et GO-2026-10-20-09), décisions N-005 et N-006 (`cd49afbc…`), N-013 (`157d388e…`), N-023
  (`1297f509…`), gabarit (`8cad4371…`), `src/controle_ia/prereg.py` (`3b2e3ee5…`).
- Sorties (sous `brouillon5/`, compagnon `.sha256` à côté de chacune) : brouillon 5
  `papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (`9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969`) ;
  configuration `papier-C-config-v1-brouillon2.json` (`77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb`) ;
  notes finales `notes/lecture-voisin-panin-v1.md` (`8781d6a799ebe87d69ed1798e681d698f22504f06b1cb3c0068e3346971705d1`) et
  `notes/lecture-voisins-HC1-bajaj-silent-judge-v1.md` (`a98ddc7568200ff5dd7c79b1cd98656c5a662d9ca8d90fa985b0d34d9a591137`) ;
  outils `outils/ecrire_config_brouillon2_v1.py` (`1726dcdf…`) et son journal (`4cdda1a2…`),
  `outils/verifier_kendall_C_P3_v1.py` (`383a66d6…`) et sa sortie (`18961a7c…`) ; sortie du validateur
  `problemes-brouillon5-v1.txt`.

## Bilan

- 95 constats : 19 (méthode), 23 (texte), 11 (Panin), 13 (voisins), 14 (note Panin), 15 (note voisins).
- **93 appliqués**, dont 4 sous la décision de Lazar R-294 (CR-methode-09, CR-texte-02, CR-panin-10, CR-voisins-12) et
  4 sous un marqueur de décision en attente (P-019 : CR-methode-02, CR-methode-03, CR-texte-04 ; P-020 : CR-texte-05).
- **2 écartés dans leur forme propre** (CR-texte-17, CR-voisins-02) : la session a retenu la forme de CR-panin-01 ; leur
  objet est couvert par elle.
- Actions qui restent à la session (le dépôt est en lecture seule pour ce rédacteur) : versements (notes, rapports,
  simulations, mesures v2, note du vivier, scripts), ligne de veille (CN-panin-08, CN-11), note de provenance des PDF de
  Bajaj et Tiganj et de « The Silent Judge » (CN-12), ligne de routine au registre et ligne d'information à Lazar (A2).

## Table

| constat | gravité | décision de la session | application (où) ou mise à l'écart (pourquoi) | écart |
|---|---|---|---|---|
| CR-methode-01 | critique | accepté : loi nette contre la cellule témoin, régresseur calibré, mots exacts | Métrique 8 bis (point 2 du rapport, mots exacts), 10 (point 1, phrase remplacée, mots exacts), 8 et 9 (loi brute rapportée) ; Seuil C-P2, C-P1, C-P6, contrôle de manipulation (point 3) ; Plan, TC.1 (point 3, mots exacts) ; Plan 2, demi-largeurs (point 4, mots exacts) ; Seuil, banc sur carte (point 5, mots exacts) ; 8 bis, test du module (point 6, mots exacts) ; phrase « n'y joue pas » absente du texte | réserve « contrôle positif faible » lue sur l'intervalle de Δ̄_éloge − Δ̄_critique, puisque ĝ n'a plus de critère |
| CR-methode-02 | majeur | proposition à Lazar P-019 | bloc P-019 (Prédiction ; Critères) : C-P3a sur le Ḡ net, valeur p exacte, colonne réfutation en mots exacts ; repli écrit sous son marqueur | — |
| CR-methode-03 | majeur | P-019 | bloc P-019 : C-P3b par le τ de Kendall, option recommandée du rapport en mots exacts ; repli = rapporté sans verdict | — |
| CR-methode-04 | majeur | accepté (formules exactes) et test du module | Seuil, C-P1 (mots exacts) ; Métrique 12 (test du module) | une proposition ajoutée au point 12 : p(θ > θ₀) est la valeur p qui conclut θ > θ₀ |
| CR-methode-05 | majeur | accepté : lecture principale des sondes sur les champs ; HC2b sur l'excédent | Métrique 14 (point 1, mots exacts) ; Plan TC.2 (point 2, mots exacts) ; TC.3 b (même règle) ; Critères C-P4 (point 3) ; Prédiction C-P4 ; réserve 6 (point 4, mots exacts) ; Combinaisons, porte GC (point 5, mots exacts) | D₀ des sondes dit aussi au point 13 (champs seuls) ; C-P4b laissé sur la lecture complète (point non tranché) |
| CR-methode-06 | majeur | accepté : effectif efficace, borne par les tâches, symétrique | Métrique 15 (mots exacts) ; Seuil C-P5 (« exemples valables pour e = 1 ») ; Prédiction et Critères C-P5 | — |
| CR-methode-07 | majeur | accepté : k_max débiaisé, validation croisée, intensités graduées, réserves | Plan 2, k_max (point 1) et demi-largeur (point 2), mots exacts ; Critères, ligne « intensités graduées » (point 3) ; réserves 1, 10, 11 ; configuration `derivation` | « étendue des γ̄ » écrit « étendue des ḡ_sép » (CR-panin-02) |
| CR-methode-08 | majeur | accepté | Plan 2 (mots exacts) ; Critères C-P4 HC2 (« non testable à cette puissance ») ; Effectifs ; configuration `derivation.demi_largeur_sondes` | — |
| CR-methode-09 | majeur | décision de Lazar (R-294, GO-2026-10-20-09) | Plan 0 « Tâches » ; Plan 2 (liste {60, 90, 120}, mots exacts, bornée par le bassin) ; Effectifs (mots exacts) ; champs du scellement ; liste d'arrêt 16 ; réserves 12 et 13 ; configuration `partage_taches`, `derivation` | partage écrit 16/48 plus extraction neuve (décision de Lazar), et non l'option du rapport ; « sinon 120 » puis borne par le bassin à l'ouverture de l'étape 2 |
| CR-methode-10 | mineur | accepté | Combinaisons (mots exacts) | — |
| CR-methode-11 | mineur | accepté | Métrique 10 (a_j, mots exacts) ; Combinaisons (mots exacts) | — |
| CR-methode-12 | mineur | accepté | Métrique 8 bis (mots exacts) ; Combinaisons | — |
| CR-methode-13 | mineur | accepté | Audit, placebo par permutation (mots exacts) ; Contrôles appariés | clé `papier-C/etape2/placebo` ajoutée (liste d'arrêt 13 : clé déclarée) |
| CR-methode-14 | forme | accepté | Plan 1.0 (mots exacts) ; Seuil, banc sur processeur | — |
| CR-methode-15 | mineur | accepté | Métrique 11 (tirage dégénéré) et 8 (forme fermée), mots exacts | — |
| CR-methode-16 | forme | accepté | Plan 2, première phrase (mots exacts) ; Seuil, banc sur carte (réserve reportée, mots exacts) | « points 1.3 et 1.4 » écrit « 1.3, 1.4 et 1.5 » (table de la session) |
| CR-methode-17 | forme | accepté | verrou 3 ; champs du scellement ; Plan 2 (`derivation.py`) ; liste d'arrêt 1 | — |
| CR-methode-18 | forme | accepté | verrou 5 (mesures réémises en v2) ; P(W ≤ 0,20) = 0,6327 cité au bloc P-019 (S3 et vérification exacte) | script et sortie v2 non écrits ici (mesures hors de ma liste de lecture) : marqueur `<<EMPREINTE_MESURES_V2>>` |
| CR-methode-19 | mineur | accepté | Métrique 11 (mots exacts) ; Plan 2 (liste {90, 120} si le test échoue) | configuration : jackknife sur les blocs (tâches du corpus A, items du corpus B) |
| CR-texte-01 | majeur | accepté | verrou 3 (l. 46, mots exacts) ; champs (l. 53-54 et l. 57, mots exacts) ; Plan 2 (l. 357) ; liste d'arrêt 1 (l. 532, mots exacts) | marqueur `<<LIGNES_MODULE_PAPIER_C>>` ajouté pour que le validateur bloque tant que les lignes manquent |
| CR-texte-02 | majeur | décision de Lazar (R-294) | comme CR-methode-09 ; liste effectifs bornée ; réserve 12 (asymétrie des sondes, mots du rapport) | garde 16 réécrite autrement que le rapport : la nouvelle extraction vient après le scellement, le texte se scelle avec le partage seul |
| CR-texte-03 | majeur | accepté | Combinaisons (mots exacts) ; porte GC sortie de la colonne réfutation (phrase sous le tableau des prédictions) | — |
| CR-texte-04 | majeur | P-019 | bloc P-019, C-P3c à quatre évaluateurs (option (i)), lecture « établie / non établie » ; trois évaluateurs sans P-020 ; repli écrit | réfutation « W ≤ 0,25 » non reprise (P-019 : sans verdict de réfutation) ; nombres vérifiés par énumération exacte (`18961a7c…`) |
| CR-texte-05 | majeur | P-020 | bloc P-020 (Plan 3, mots exacts), marqueur `<<DECISION_BRAS_USURPATION>>` aux champs ; repli écrit ; configuration `agent_bras.decision_bras_usurpation` | — |
| CR-texte-06 | majeur | accepté (formes de P4) | GO (mots exacts) ; forme de la ligne d'accord ; Plan 1 ; liste d'arrêt 2 et 3 (mots exacts) ; configuration `pilote` | borne stricte : « lancement estimé à 10 USD ou plus » (table : < 10 USD) |
| CR-texte-07 | majeur | accepté | Plan 3, Sondes (mots exacts) | — |
| CR-texte-08 | majeur | accepté (C-P1b) | Prédiction, Seuil, Critères (mots exacts) ; Comparaisons multiples ; TC.1 | — |
| CR-texte-09 | majeur | accepté | configuration brouillon 2 (deux phrases retirées, longueurs et gardes rejouées) ; réserve 9 (mots exacts) | `ecrire_config_v1.py` non relancé (non lu) ; script neuf `ecrire_config_brouillon2_v1.py` |
| CR-texte-10 | mineur | accepté | Plan 2 (l. 357, mots exacts) ; réserve 4 ; Plan 1.3 (fentes du corpus B) | réserve 4 : « échec » devenu « défaut de chaîne trouvé à l'audit A6 », et remède « correction de la chaîne ou remplacement sur GO » (CR-panin-01) |
| CR-texte-11 | mineur | accepté | en-tête des ajouts de HC1 (fusion avec CR-panin-11 et CR-voisins-09) ; puce Panin (deux critères de N-005) ; `<<DECISION_VOISINS>>` | `<<RAPPORTS_CL_NOTES>>` et l'empreinte de la note finale remplis directement |
| CR-texte-12 | mineur | accepté | champs du scellement (configuration, mots exacts adaptés) | brouillon relu = brouillon 2 ; `partage_taches.sha256_source` ajouté aux différences admises |
| CR-texte-13 | mineur | accepté | Seuil, banc sur processeur (mots exacts) ; propriétés du pilote ; Plan 1.0 | — |
| CR-texte-14 | mineur | accepté | Seuil C-P2 et C-P1 (mots exacts), C-P6 juges, contrôle de manipulation | « ni au-delà, en forme fermée » ajouté à « identifiable » (CR-methode-15) |
| CR-texte-15 | mineur | accepté | Plan 2, témoins (mots exacts) ; Métrique 10 (ĉ_témoin, mots exacts) ; configuration `regle_temoins` | — |
| CR-texte-16 | mineur | accepté | verrou 5 ; Documents (`<<CHEMIN_NOTE_VIVIER>>`) | versements à faire par la session |
| CR-texte-17 | mineur | forme de CR-panin-01 retenue | écarté dans sa forme propre (« nœud pour ce juge », remplacement sur GO) : la session a décidé qu'un ordre contraire chez un ou deux juges est une réserve ; objet couvert par Plan 1.2 et liste d'arrêt 4 | — |
| CR-texte-18 | mineur | accepté | Métrique 3 (mots exacts) ; liste d'arrêt 9 | — |
| CR-texte-19 | mineur | accepté avec CR-methode-06 | Prédiction et Critères C-P5 (deux bornes basses, deux bornes hautes) | borne de Clopper-Pearson à l'effectif efficace au lieu de celle des essais mis en commun (table de la session) |
| CR-texte-20 | mineur | accepté | en-tête (mots exacts) | — |
| CR-texte-21 | mineur | accepté | réserves 10 et 11 (mots exacts) | — |
| CR-texte-22 | mineur | accepté | Audit A8 | renuméroté A8 (A7 pris par CR-panin-05) ; sens retourné : la lecture complète rapportée est comparée à la lecture principale sur les champs (CR-methode-05) |
| CR-texte-23 | forme | accepté | l. 109 (« sha256 du fichier », champs) ; l. 508 (Critères HC2b) ; l. 560-563 (une entrée « Contre-lecture k » par rapport) ; l. 29 (Rappel) | — |
| CR-panin-01 | majeur | accepté | Plan 1.2 (remplacement), liste d'arrêt 4 (mots exacts), Seuil (« Ce banc est un contrôle positif rapporté, jamais un filtre de juge. »), Plan 0 (l. 316-317, mots exacts) ; audit A6 | « ordre contraire » défini sur Δ̄ et ĉ (CR-methode-01, point 5) au lieu de ĝ |
| CR-panin-02 | majeur | accepté | Métrique 18 (mots exacts) ; Plan 2 (γ̄ → ḡ_sép partout) ; réserve 2 (mots exacts, chemin et empreinte de la mesure remplis) ; Métrique 10 et Combinaisons (ĉ_m par rang) ; configuration `derivation.variable_de_dessin` | — |
| CR-panin-03 | mineur | accepté | Rappel (phrase de la l. 34, fusionnée avec CR-voisins-07) ; Seuil C-P1 (ajout de la l. 297, mots exacts) | fusion des deux phrases de la l. 34 |
| CR-panin-04 | mineur | accepté | Hypothèse, puce Panin (mots exacts) | parenthèse de CR-texte-11 ajoutée (deux critères de N-005) |
| CR-panin-05 | mineur | accepté | Contre-indices (mots exacts) ; Audit A7 (mots exacts) | — |
| CR-panin-06 | mineur | accepté | HC3, composante 2 (mots exacts) | — |
| CR-panin-07 | mineur | accepté (verrou ajouté) | verrou 2 (chemin de la note finale ; contrôle des résumés, en commençant par Joswin et al. et Hu et Qu) | verrou étendu aux deux voisins cités par Bajaj et Tiganj (note finale des voisins) |
| CR-panin-08 | mineur | accepté | Plan 1.6 (mots exacts) ; Plan 0 (l. 314) ; Plan 2 ; liste d'arrêt 12 | — |
| CR-panin-09 | majeur | accepté | comme CR-texte-01 (forme plus détaillée retenue) | — |
| CR-panin-10 | majeur | décision de Lazar (R-294) | comme CR-methode-09 ; règle de calibrage « dont la tâche est dans le lot de calibrage » (Plan 1) | option de Lazar, non celle du rapport |
| CR-panin-11 | forme | accepté | Rappel (l. 33) ; en-tête des ajouts de HC1 (l. 134) | fusion avec CR-texte-11 et CR-voisins-09 |
| CR-voisins-01 | majeur | accepté | Hypothèse, puce Bajaj et Tiganj (mots exacts) | — |
| CR-voisins-02 | majeur | forme de CR-panin-01 retenue | écarté dans sa forme propre (arrêt pour les trois juges dès un échec) : la session a retenu la réserve sans arrêt ; objet (aucun juge retiré ni remplacé sur ce motif) couvert par Plan 1.2, Plan 0, liste d'arrêt 4 | — |
| CR-voisins-03 | mineur | accepté | Hypothèse, puce « The Silent Judge » (mots exacts) | — |
| CR-voisins-04 | mineur | accepté | Contre-indices, mode raisonné (mots exacts) | — |
| CR-voisins-05 | mineur | accepté | Contre-indices, destination autre que la cible (mots exacts) | — |
| CR-voisins-06 | mineur | accepté | Plan 3, Familles (mots exacts) ; Documents (PDF et empreinte complète) | — |
| CR-voisins-07 | mineur | accepté | Rappel (fusion avec CR-panin-03) ; réserve 1 | fusion |
| CR-voisins-08 | mineur | accepté | Hypothèse, puce Venkatesh et al. (mots exacts) | — |
| CR-voisins-09 | mineur | accepté | en-tête des ajouts de HC1 (fusion) | `<<R-xxx>>` écrit `<<DECISION_VOISINS>>` (le validateur ne voit pas `<<R-xxx>>`) |
| CR-voisins-10 | forme | accepté | Hypothèse, instrument cité (mots exacts) | — |
| CR-voisins-11 | majeur | accepté (module) | comme CR-texte-01 | — |
| CR-voisins-12 | majeur | décision de Lazar (R-294) | comme CR-methode-09 ; réserve 13 (écart de distribution de l'extraction neuve) | option de Lazar |
| CR-voisins-13 | mineur | accepté | Plan 2 (phrase) ; liste d'arrêt 12 | « son issue ne fait que permettre ou arrêter l'étape 2 » réécrit « ne peut arrêter l'étape 2 que par un défaut de chaîne trouvé à l'audit A6 » (CR-panin-01) |
| CN-panin-01 | majeur | accepté (version finale de l'annexe) | note finale : verdict ; tableau, ligne « intensité de pression graduée » | — |
| CN-panin-02 | majeur | accepté | note finale : points 2 et 9 ; ligne du tableau « revendication d'autorité », « approbations forgées », HC3 | — |
| CN-panin-03 | majeur | accepté | note finale : ligne « g comme fraction du chemin » | — |
| CN-panin-04 | mineur | accepté | note finale : en-tête « Lu en entier » | — |
| CN-panin-05 | mineur | accepté | note finale : verdict (deux déclencheurs absents ; porte GC) | — |
| CN-panin-06 | mineur | accepté | note finale : verdict (aucune prédiction prise dans le domaine) | — |
| CN-panin-07 | mineur | accepté | note finale : section « Ce qui n'a pas pu être lu » | — |
| CN-panin-08 | mineur | accepté | note finale : section des voisins de la bibliographie ; verrou 2 du brouillon 5 | ligne de veille (2026-W43) à écrire par la session |
| CN-panin-09 | mineur | accepté | note finale : point 12 (remède, conséquence) | — |
| CN-panin-10 | forme | accepté | note finale : 11:43 UTC | — |
| CN-panin-11 | forme | accepté | note finale : « Cité comme publié » | — |
| CN-panin-12 | forme | accepté | note finale : « Conséquences proposées » | dernière conséquence mise à jour : la note des deux autres voisins est finale (chemin et empreinte) |
| CN-panin-13 | forme | accepté | note finale : points 2 et 5 (« probe », « families ») | — |
| CN-panin-14 | forme | accepté | note finale : normalisation déclarée en tête | — |
| CN-01 (voisins) | majeur | accepté | note finale : section Bajaj et Tiganj (intensité, mesure continue, confrontation) | — |
| CN-02 (voisins) | majeur | accepté | note finale : statut de « The Silent Judge » lu sur le PDF | — |
| CN-03 (voisins) | mineur | accepté | note finale : phrase ajoutée au début du verdict | l'annexe ne la portait pas : ajoutée |
| CN-04 (voisins) | mineur | accepté | note finale : tableau du verdict, expérience 2 | — |
| CN-05 (voisins) | mineur | accepté | note finale : deux niveaux d'autorité, tableau 2 p. 8 | — |
| CN-06 (voisins) | mineur | accepté | note finale : mesure = écart signé (p. 3 ; tableau 1, p. 5) | — |
| CN-07 (voisins) | mineur | accepté | note finale : CAR nul (p. 4), écart avec le résumé | — |
| CN-08 (voisins) | mineur | accepté | note finale : non-reconnaissance hors de HC1 | — |
| CN-09 (voisins) | mineur | accepté | note finale : renvoi au programme, section 10, EC.1, et à N-005 | — |
| CN-10 (voisins) | mineur | accepté | note finale : items reçus (R-279) | — |
| CN-11 (voisins) | mineur | accepté | note finale : conséquences (routine ; veille) | `<<R-xxx>>` remplacé par du texte ; ligne de veille à écrire par la session |
| CN-12 (voisins) | forme | accepté | note finale : chemin de la note de provenance | marqueur d'empreinte remplacé par du texte ; note de provenance à écrire par la session |
| CN-13 (voisins) | forme | accepté | note finale : tâches et modèles (p. 2) | — |
| CN-14 (voisins) | forme | accepté | note finale : renvoi à N-013, section 1 | — |
| CN-15 (voisins) | forme | accepté | note finale : « pdftotext -layout, contrôlé en mode brut » | — |

## Écarts de rédaction hors constat (une ligne chacun)

- Chemin de versement proposé pour les rapports, simulations et outils de contre-lecture :
  `docs/notes/contre-lectures-papier-C-v1/` ; il est écrit dans les deux notes finales (leurs empreintes en dépendent).
- Vérification exacte des lois nulles du W de Kendall (3, 4 et 5 évaluateurs) ajoutée, chemin proposé
  `docs/notes/papier-C-mesures-v1/` : elle porte les nombres de C-P3c (0,8125 ; 0,0417 ; 0,0278).
- Clés de graines ajoutées : `partage-taches-papier-C` (table), `papier-C/etape2/fenetres-excedent` (CR-methode-05 : « clé
  de graine déclarée »), `papier-C/etape2/placebo` (CR-methode-13).
- Configuration : `permutations_W_corpus` remplacé par `permutations_tau_C_P3b` (même valeur, 100 000) ; blocs
  `partage_taches` et `stabilite_rang` ajoutés.
- Marqueur `<<DECISION_STABILITE_RANG>>` ajouté aux champs, par symétrie avec `<<DECISION_BRAS_USURPATION>>`.
- Marqueurs du brouillon 4 retirés : `<<EMPREINTE_NOTE_PANIN_FINALE>>`, `<<EMPREINTE_NOTE_VOISINS_FINALE>>` (empreintes
  connues), `<<CHEMIN_TACHES_ETAPE2>>`, `<<EMPREINTE_TACHES_ETAPE2>>` (remplacés par le partage), `<<EMPREINTE_MODULE>>`
  (remplacé par les lignes « Module du papier C »).
- Historique : le brouillon 4 est cité sous `brouillons/` par analogie avec les brouillons 1 à 3 ; chemin à confirmer au
  versement.
