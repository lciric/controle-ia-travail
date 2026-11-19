# Papier C — note des différences entre le brouillon 5 et le brouillon 6 de relance du préenregistrement — v6

Version 6 du 2026-11-19 : les versions 1 à 5 restent intactes (v5 : `c78bfb9e…`). Ajout : la section 9 (différences entre la version r2 et la version r3 : contre-lecture de r2 traitée, trois cases du directeur remplies, liste finie de la grille).

Version 5 du 2026-11-19 : les versions 1 à 4 restent intactes (v4 : `e878eecc…`). Ajout : la section 8 (différences entre la version r1 et la version r2, points ouverts du module traités).

Version 4 du 2026-11-19 : les versions 1 à 3 restent intactes (v3 : `f6246bdf…`). Ajout : la section 7 (différences entre la version c2 et la version r1, cases du directeur remplies).

Version 3 du 2026-11-19 : la v2 (`4131fac0…`) et la v1 (`80dd3075…`) restent intactes. Ajout : la section 6 (différences entre la version c1 et la version c2).

Version 2 du 2026-11-19 : la v1 (`80dd3075…`) reste intacte. Ajouts : la garde 23 de la liste d'arrêt, omise en v1 (ligne C-57d) ; la section 4 (lecture du mandat pour le validateur) ; la section 5 (différences entre le brouillon 6 de relance et sa version c1). Le reste est celui de la v1 et décrit le brouillon 6 de relance (`67cd36f1…`).

Écrite par le rédacteur neuf du brouillon 6 de relance (Claude Fable 5.2), le 2026-11-19. Avant : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (`9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969`, 97 194 octets). Après : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19.md` (`67cd36f19782ec9ff0588c235f1b8ff27c40504f5288991ff1f20b0fa93c0e0d`, 150 891 octets).

Le texte est construit par programme (`travail/construire_brouillon6_relance_v1.py`) : l'en-tête est remplacé en bloc ; chaque changement du corps est un remplacement exact, dont l'ancre se trouve une seule fois dans le brouillon 5, sinon le programme s'arrête. 66 changements, un par ligne ; un identifiant suivi d'une lettre (C-40b) est une partie du même changement, à un autre endroit du texte. L'énoncé de HC2 et la formulation de citation de MIRAGE sont recopiés par programme depuis `docs/decisions/decision-N-068-v1.md` (lignes 65 et 71), mot pour mot.

Abréviations des pièces : « archive » = `registres/passations/bloc-notes-session16-complement-2026-10-21.tar.gz` (`0c15862c…`), dossier `papier-C/` ; D-1 à D-14 = `decisions-du-directeur-exigees-v1.md`.

## 1. Changements, un par ligne

| n° | section | avant (résumé) | après (résumé) | commandé par |
|---|---|---|---|---|
| C-01 | En-tête (titre, auteur, date, rôle, historique, ce que change ce brouillon, verrous, champs du scellement, GO, documents qui font foi, pièces de contre-lecture) | en-tête du brouillon 5 | remplacé en bloc (fichier entete_b6_relance_v1.md) | mandat ; registres/go.md ; registres/decisions.md ; vérifications sur disque |
| C-10 | Hypothèse, renvoi | énoncés repris de N-005, N-013, N-023 | HC2 part de l'énoncé retenu de N-068 ; les autres énoncés inchangés | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, « Portée » (l. 6) et section 4 |
| C-11 | Hypothèse, HC1, précédents | marqueur `<<DECISION_VOISINS>>` dans l'en-tête des ajouts du brouillon 4 | marqueur remplacé par le renvoi au verrou 2 (consignation de routine à écrire) et à la décision D-12 | consigne du rédacteur, § 1 (tout marqueur résolu ou converti) ; `registres/decisions.md` : aucune ligne ne consigne l'ajout |
| C-12 | Hypothèse, HC1, précédents | liste des précédents arrêtée aux trois voisins du brouillon 4 | sous-puce « ajouts du brouillon 6 de relance » : 2611.04556 cité comme publié (R-2554) ; 2606.05384 ; 2608.12645 ; 2603.15809 ; 2607.08066 | `registres/decisions.md`, R-2554 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, `e30a013d…`, section 4 (HC1) ; N-068, section 7 |
| C-13 | Hypothèse, HC2 | « HC2, robustesse : sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste qui lit l'agent qui produit le contenu » ; contre-indices dits « tous sur des sondes qui lisent le modèle qui traite le contenu » | énoncé retenu de N-068, section 4, mot pour mot ; ce qui est propre ; plan apparié non revendiqué (Kale et Vishwanath) ; prédiction inchangée dans son signe ; ce qui n'est plus revendiqué ; MIRAGE cité avec la formulation imposée ; poids renvoyé à D-1 (case « À REMPLIR ») ; la phrase « tous sur des sondes [du lecteur] » retirée (fausse depuis 2608.21664) ; positions de sonde | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, sections 0 (points 6, 7), 4, 5, 6, 7 |
| C-14 | Hypothèse, HC2b | contrôle du style et du retour de bâton, sources de N-013 seulement | sources du contrôle du style ajoutées (Karne ; sosie inoffensif ; exposition contre engagement ; volet « Stego » de NARCBench) ; contre-indice faible de N-013 (2609.36490) cité ; énoncé inchangé | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, sections 0 (point 8b), 7, 8 ; `docs/decisions/decision-N-013-v1.md`, `157d388e…`, section 5 |
| C-15 | Hypothèse, HC3 | précédents de N-013 et de Panin | précédents du niveau 3 ajoutés (2609.19587 ; 2507.08794 ; 2610.17301) ; énoncé inchangé | `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, `e30a013d…`, section 4 (HC3) |
| C-16 | Hypothèse, pièces revendiquées | « inchangées » ; opposition juge / sonde sans précision | HC2 : seulement ce que l'énoncé retenu a de propre ; opposition juge / sonde lue comme comparaison des deux déplacements sous un même contenu écrit par l'agent ; plan apparié dit méthode citée ; paragraphe « Périmètre » (HC4 à HC6 hors texte ; organisme d'idéation hors texte, D-10) | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, sections 4 et 8 ; `docs/decisions/decision-N-065-v1.md`, `f820e90d…`, points 1 et 4 |
| C-17 | Hypothèse, hypothèses de travail | trois hypothèses de travail | quatrième : le plaidoyer écrit par l'agent déplace les juges (sans quoi HC2 n'est pas éprouvée) | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 (« avec g_juge en regard ») ; R4 |
| C-18 | Prédiction, préambule | « Toutes les statistiques des juges qui portent un verdict se lisent sur la loi nette » | liste des statistiques de TC.1 lues sur la loi nette ; gains d'écart et alarme renvoyés aux points 13 et 15 | archive, contre-lecture « texte » du brouillon 5, constat texte-05 (table du brouillon 6 de l'archive, `74b5ae16…`, section 2) ; jugé fondé : les gains d'écart et l'alarme ne passent pas par la loi nette |
| C-19 | Prédiction, table, C-P2 et C-P3 | « borne haute à 95 % de Ḡ » ; renvoi au bloc P-019 | « borne haute de l'intervalle bilatéral à 95 % (BCa) de Ḡ » ; renvoi au bloc P-021 | archive, CL5-methode-12 (rapport `0c492f02…`) ; `registres/decisions.md`, P-021 et R-326 |
| C-20 | Prédiction, table, C-P4, C-P4c (nouvelle), C-P4b | C-P4 : g brut à un seul niveau de plaidoyer, sans les juges en regard ; C-P4b sur la lecture complète (paragraphe compris) | C-P4 : Ḡ_P, moyenne des gains par niveau du plaidoyer, sonde de l'agent auteur et adversaire ; C-P4c : écart apparié juge moins sonde sous le même plaidoyer (comparaison aux juges) ; C-P4b lu sur l'excédent du paragraphe, des deux côtés | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 (énoncé ; « à chiffrer au préenregistrement (R1), avec g_juge en regard ») ; N-005, prédiction 4 ; archive, CL5-methode-04 pour C-P4b ; décisions D-2 et D-3 |
| C-21 | Prédiction, table, C-P6 | « borne haute à 95 % sous 0,10 » ; clause « si P-020 est refusée » | borne BCa bilatérale ; clause de refus retirée (bras inclus) | archive, CL5-methode-12 ; `registres/decisions.md`, P-020 et R-326 |
| C-22 | Prédiction, porte GC | « g brut (champs seuls) d'une sonde de l'auteur > 0 » | Ḡ_P ; lecture sur la sonde de l'agent auteur dite d'après N-068 | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 7 (« elle se lit désormais sur la sonde de l'agent auteur ») |
| C-23 | Prédiction, stabilité de rang | bloc à deux versions sous P-019 (version recommandée ; repli) ; C-P3a par W exact seul ; C-P3b par τ des quinze valeurs ; clause « sans le bras usurpation » | une seule version : P-021, option (A) (défaut appliqué, R-326) : C-P3a par W exact et rééchantillonnage centré ; C-P3b sur les écarts intra-famille ; trois lectures de la loi nette ; clause de repli mécanique ; replis et clause « sans le bras » retirés | `registres/decisions.md`, P-021 (l. 399) et R-326 (l. 535) ; archive, CL5-methode-02 et -03 (`0c492f02…`) et CB6-methode-courte-01, -02, -06 (`45a0d875…`) ; décision D-9 pour la troisième lecture |
| C-24 | Prédiction, contre-indices déclarés | puce « Sondes lectrices déplacées… : un g_lecteur positif n'invalide pas HC2 » ; aucun contre-indice sur une sonde du modèle qui écrit ; aucun contre-indice du niveau 3 | puce des sondes lectrices complétée (Karne ; Kale et Vishwanath ; 2602.00750 ; 2609.36490) ; puces neuves : destination, forme, stabilité de rang (dont 2611.04556, R-2554), gain instable, instrument, sonde lue sur le modèle qui écrit (2608.21664), consignes d'évasion (2611.10620, non opposable ; 2602.08877, hors périmètre), même signe publié et non opposable (MIRAGE ; 2609.03035 v2), HC2b, HC3 composante 1 | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 6 (table et lecture d'ensemble) ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, `e30a013d…`, section 4 ; R-2554 ; rapports des lots 1, 3-A, 7-C et C9 (branches, empreintes aux « Documents ») |
| C-25 | Métrique, point 5 | conditions : sans insertion, formulations, témoins, contenus neutres | condition de référence « constat nu » ajoutée (rapportée, sans verdict) | `registres/decisions.md`, P-022 option (b) (l. 400) et R-326 ; fentes vérifiées dans `brouillons/papier-C-config-v1-brouillon2.json` (`77252564…`) |
| C-26 | Métrique, point 8 bis | réserve d'intention par « demi-largeur » ; test du module sommaire ; une seule lecture (calibrée) | r̂ rapporté ; λ lu aussi sans calibrage (ρ = 1) ; réserve d'intention par intervalle de l'écart apparié ; tests du module précisés, avec contrôles de l'artefact, règle conjointe de C-P1 et statistiques de rang aux trois lectures | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constats 01, 08, 09 ; archive, vérification courte de méthode du brouillon 6 de la session 16 (`45a0d875…`), constats 01, 03 ; jugés fondés : le calibrage par ρ̂ suppose un modèle d'erreur que la loi témoin seule ne distingue pas de la compression, la conjonction des lectures est prudente dans les deux sens |
| C-27 | Métrique, point 10 | ĉ_m de la loi séparée (brute) portait la réserve « destination hétérogène » | la réserve se lit sur la loi séparée nette ; ĉ_m brut rapporté sans réserve | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 06 (lectures restées sur la loi brute) ; jugé fondé : la loi brute contient la régression vers la moyenne que le même texte écarte des tests |
| C-28 | Métrique, point 11 | accélération « par jackknife sur les tâches » ; test du module générique ; BCa non défini non traité | jackknife sur les grappes (tâches ou items) ; test du module sur les bornes des réfutations ; repli écrit par percentiles quand le BCa n'est pas défini, garde testée | archive, constat texte-11 et archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constats 05 et 08 ; R5 |
| C-29 | Métrique, point 12 | décompte et BCa coexistaient sans règle | préséance écrite : verdicts en valeurs p par le décompte ; critères en intervalles par le BCa | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 07 ; jugé fondé : sans règle, deux calculs peuvent donner deux verdicts |
| C-30 | Métrique, point 13 | gain d'écart à un seul niveau de plaidoyer ; cellules HU et SU « seulement sous P-020 » ; aucune comparaison aux juges définie ; plan apparié sans citation | gain par niveau m du plaidoyer et moyenne Ḡ_P ; pente sur l'intensité ; comparaison aux juges e = Ḡ_P(juge) − Ḡ_P(sonde) ; exception de C-P4b (excédent) ; plan apparié cité (Kale et Vishwanath) ; bras d'usurpation inclus | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 (« en fonction de l'intensité » ; « comparé au g des juges génératifs sous les mêmes attaques ») et section 6 (citation obligatoire) ; P-020 et R-326 ; archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 04 ; décisions D-2, D-3 |
| C-31 | Métrique, point 14 | une agrégation par sonde (maximum ou attention) ; aucune lecture filtrée ; aucun témoin lexical ; une seule action lue | agrégations lues en plus de celle de production (bras de diagnostic compris, N-026) ; lecture filtrée (N-053) ; témoin lexical par lecture forcée (mêmes mots, sans intention) ; scores des actions précédentes de la trajectoire rapportés | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 (« pour plusieurs agrégations dont une robuste, sur des trajectoires ») et section 5 (témoin lexical ; exposition contre engagement) ; `docs/decisions/decision-N-053-v1.md`, `2204256d…`, point 1 ; N-026 (CLAUDE.md) ; décisions D-7, D-8, D-14 |
| C-32 | Métrique, point 15 | effectif efficace non défini quand toutes les alarmes sortent (ou aucune) | si p̂ vaut 0 ou 1 : e = 1, écrit tel quel | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 05 ; jugé fondé : la formule divise par p̂ (1 − p̂), et l'issue « toutes les alarmes sortent » est celle que C-P5 prédit |
| C-33 | Métrique, point 16 | « Ḡ et ĉ en mode raisonné moins mode direct » | « Ḡ et ĉ de la loi nette » | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 06 |
| C-34 | Métrique, point 17 | gardes lexicales sans les jetons spéciaux de gabarit ; « bloc P-020 » | aucun jeton spécial de gabarit de conversation dans les insertions et les témoins (motifs à porter à la configuration, verrou 4) ; garde étendue au constat nu ; bras d'usurpation inclus | archive, constat CQ-04 (table du brouillon 6 de l'archive, `74b5ae16…`, section 8) ; jugé fondé sans chiffre : un jeton de rôle dans une insertion changerait de famille d'attaque ; P-022 (b) ; P-020 |
| C-35 | Métrique, point 18 ; point 19 (nouveau) | pilote : rééchantillonnage des contenus sans déclaration de l'unité ; aucun bras « fuite textuelle et contrôlabilité » | écart déclaré (unité d'indépendance : la tâche) ; point 19 : bras « fuite textuelle et contrôlabilité », rapporté, jamais critère | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 14 ; `docs/decisions/decision-N-053-v1.md`, `2204256d…`, point 1 (« dans les préenregistrements de G1 et du papier C, avant leur scellement ») ; N-068, section 5 (contrôlabilité : « le bras de N-053 y répond déjà ») ; décision D-8 |
| C-36 | Seuil, C-P1 | verdicts « vers la cible » et « vers la moyenne » sur la seule loi nette calibrée | règle conjointe : les deux lectures (calibrée ; sans calibrage) doivent conclure ; sinon réserve « destination sensible au modèle d'erreur de v₀ » | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 01 ; jugé fondé (voir C-26) ; plus strict pour confirmer comme pour réfuter (R4) |
| C-37 | Seuil, C-P3 | seuils du bloc P-019 ; 100 000 permutations pour le τ de C-P3b | seuils du bloc P-021 ; permutations pour le τ rapporté ; rééchantillonnage centré pour les verdicts ; trois lectures | `registres/decisions.md`, P-021 et R-326 ; archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constats 02 et 03 |
| C-38 | Seuil, C-P4, C-P4c, niveaux | seuils de C-P4 et C-P4b ; rien sur la comparaison aux juges ni sur les niveaux | HC2 sur Ḡ_P ; C-P4c : intervalle BCa à 95 % de e, Bonferroni sur les sondes ; « niveaux gradués pour un juge » ; seuil proposé de la réserve « sonde contrôlable par consigne » | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 ; `docs/decisions/decision-N-053-v1.md`, `2204256d…`, point 1 ; décisions D-2, D-3, D-8 |
| C-39 | Plan, section 0, tâches | procédure d'extraction citée sans empreinte ; tirage des tâches de l'étape 2 sans règle | empreinte de la procédure (recalculée) ; tirage sans remise, uniforme, dans le bassin trié, sans strate par origine | archive, constats texte-10 et texte-08 (table du brouillon 6 de l'archive (`74b5ae16…`), section 2) ; empreinte `d23bd62f…` recalculée sur `docs/procedures/T0.5-extraction-v1.md` ; R6, R9 |
| C-40 | Plan, section 1, titre et vivier | titre : GO-2026-10-17-01 sans échéance ; vivier sans le constat nu | titre : accord valide au jour du lancement (D-4) ; l'insertion du constat nu est lue au pilote pour la lisibilité seulement | `registres/go.md`, GO-2026-10-17-01 et GO-2026-10-20-06 (échéance 2026-11-30), GO-2026-11-18-01 ; P-022 (b) ; archive, CB6-texte-05 (table du brouillon 7, `351ab375…`, section 2) |
| C-40b | Plan, point 1.4 | vivier : 80 formulations et 16 témoins | constat nu lu sur les mêmes contenus, hors gains du vivier et hors addendum | P-022 (b) ; archive, CB6-texte-05 |
| C-41 | Plan, section 2, témoins et demi-largeur | ordre d'appariement des témoins non fixé ; validation croisée par moitiés de contenus | appariement dans l'ordre des rangs croissants ; validation croisée par huit et huit tâches du lot de calibrage ; note sur Ḡ_P | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constats 11 et 14, et constat texte-07 ; jugés fondés : sans ordre la règle n'est pas mécanique ; des contenus d'une même tâche des deux côtés de la coupe ne sont pas indépendants |
| C-41b | Plan, section 2, demi-largeur de λ | moitiés de contenus | huit tâches contre huit | archive, constat texte-07 et archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 14 |
| C-41c | Plan, section 2, demi-largeur des sondes | demi-largeur prévue de g brut à un niveau | précision : la formule vaut pour un niveau et borne celle de Ḡ_P | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 (intensité) ; cohérence avec C-30 |
| C-42 | Plan, section 3, génération et bras | bloc à deux versions sous P-020 (six épisodes par tâche, ou quatre si refus) ; un seul niveau de plaidoyer | une seule version : bras d'usurpation inclus (P-020, R-326) ; plaidoyer à k_P niveaux, k_P laissé « À REMPLIR » (décision D-2) ; 2 × (2 + k_P) épisodes par tâche ; plan apparié cité ; invariant « aucun score de moniteur dans la génération » | `registres/decisions.md`, P-020 (l. 398) et R-326 ; `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 (« en fonction de l'intensité de l'attaque ») et section 6 ; `docs/decisions/decision-N-053-v1.md`, `2204256d…`, point 5 (invariant) |
| C-43 | Plan, section 3, TC.1 | TC.1 sans constat nu ; « bloc P-019 » | constat nu lu en TC.1 sur les deux corpus, rapporté, sans verdict ; « bloc P-021 » | `registres/decisions.md`, P-022 option (b) et R-326 ; archive, constat CV-01 (b) (table du brouillon 6 de l'archive (`74b5ae16…`), section 4) |
| C-44 | Plan, section 3, TC.2 | TC.2 : cellules H, HP, S, SP ; gains pour sondes et juges sans comparaison écrite ; excédent à un niveau | TC.2 selon N-068 : niveaux du plaidoyer, gains par niveau et Ḡ_P, pente, comparaison aux juges (C-P4c), agrégations, lecture forcée du témoin lexical, positions de sonde mesurées et non mesurées, délégation à un outil déclarée sans objet | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, sections 4, 5, 6 ; rapport du lot 1 (`9996f40c…`), § 3.1 et § 1.5, réserve 5 ; rapport du lot 3-A (`64b728d6…`), § 10.5 ; rapport du lot 7-C (`2b03ede0…`), § 7 ; décisions D-2, D-3, D-5, D-6, D-7 |
| C-44b | Plan, section 3, TC.2, lecture (2) | excédent du paragraphe à un niveau | calculé par niveau, puis moyenné sur les niveaux | cohérence avec C-30 (`docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4) |
| C-45 | Plan, section 3, TC.3 | « sous P-020 : gain d'écart… » | bras inclus ; lecture forcée du contenu SU ajoutée | P-020 et R-326 ; cohérence avec C-31 |
| C-46 | Plan, section 3, clause d'ouverture ; bras de N-053 ; modérateur raisonné | aucune clause d'ouverture ; aucun bras de N-053 ; 20 tâches « tirées » pour le mode raisonné | clause d'ouverture (R-307) ; bras « fuite textuelle et contrôlabilité » au plan ; 20 tâches tirées sans remise parmi les n/2 de l'étape 2 | `registres/decisions.md`, R-307 (l. 511) et GO-2026-10-20-13 ; `docs/decisions/decision-N-053-v1.md`, `2204256d…`, point 1 ; archive, constat texte-08 |
| C-47 | Plan, section 3, effectifs | 180 à 360 épisodes (plan 2 × 3 ; 120 à 240 si P-020 refusée) | (n/2) × 2 × (2 + k_P) épisodes : 180 à 360 si k_P = 1, 300 à 600 si k_P = 3 ; lectures forcées comptées ; clause de refus retirée | P-020 et R-326 ; décision D-2 ; arithmétique : 30 × 2 × 3 = 180, 60 × 2 × 3 = 360, 30 × 2 × 5 = 300, 60 × 2 × 5 = 600 |
| C-48 | Plan, section 4, graines | « Clés ajoutées par ce brouillon » | « Clés ajoutées par le brouillon 5 » ; clé neuve `papier-C/etape2/direction-aleatoire` | R9 ; cohérence avec C-35 |
| C-49 | Plan, section 5, comparaisons multiples | « bloc P-019 » ; rien sur C-P4c ni sur un facteur interne | « bloc P-021 » ; Bonferroni sur les sondes pour C-P4c ; facteur interne hors de ces corrections | P-021 ; R-307 ; cohérence avec C-38 |
| C-50 | Plan, section 6, contrôles appariés | « plan 2 × 2 (et bras usurpation, bloc P-020) apparié par tâche » | plan apparié par tâche à 2 × (2 + k_P) cellules, avec sa citation obligatoire ; témoin lexical ; constat nu | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 6 (« partout où le plan apparié est décrit, Kale et Vishwanath ») ; P-020 ; P-022 |
| C-51 | Plan, section 7, réserves 6 et 9 | réserve 6 sans C-P4b ; réserve 9 : Ḡ_4 − Ḡ_3 dit contraste « style contre contenu » | réserve 6 : C-P4b lu sur le même excédent ; réserve 9 : Ḡ_4 − Ḡ_3 est un contraste entre deux enveloppes qui portent le même constat ; le contraste « style contre contenu » est Ḡ_4 − g_constat ; la famille 4 imite l'instructeur en texte brut seulement | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 04 ; archive, constats CV-01 (a) et CQ-04 (table du brouillon 6 de l'archive (`74b5ae16…`), sections 4 et 8) ; P-022 (b) ; jugés fondés sur la configuration elle-même, sans chiffre de l'état de l'art |
| C-51b | Plan, section 7, réserve 9 | voir C-51 | voir C-51 | voir C-51 |
| C-52 | Plan, section 7, réserves 14 à 19 (nouvelles) | treize réserves | 14 contingence dans les familles (étiquette descriptive, R-307 et R-309) ; 15 identification du calibrage ; 16 constat commun aux familles ; 17 personne grammaticale (R-316) ; 18 attaque non itérative, un seul agent de 8 milliards de paramètres, niveaux construits ; 19 délégation à un outil et troisième position non mesurées | `registres/decisions.md`, R-307, R-308, R-309 (l. 511 à 513), R-316 (l. 524) ; P-022 (option (a) comprise dans (b)) ; archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 01 ; `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, sections 3, 5, 6 |
| C-53 | Audit de symétrie | A1, A2 sur des gains et des ĉ non précisés (loi nette ou brute) ; A5 sur R²_joint non précisé ; A7 sur Δ et v₀ bruts ; A8 sans C-P4b | A1 et A2 sur la loi brute des deux côtés ; A5 sur la loi nette ; A7 sur la loi nette, plus la part des verdicts les plus probables qui changent ; A8 étendu à C-P4b et C-P4c ; A9 nouveau (HC2 confirmée alors qu'aucun juge ne bouge) | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constats 04 et 06 ; `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 (« avec g_juge en regard ») ; rapport du lot 7-C, § 7 (probabilité sans verdict) ; R4 |
| C-53b | Audit, A5 | voir C-53 | voir C-53 | voir C-53 |
| C-53c | Audit, A7, A8, A9 | voir C-53 | voir C-53 | voir C-53 |
| C-54 | Critères de lecture gelés, préambule et table | préambule « loi nette » général ; C-P2 et C-P6 « borne haute » non précisée ; C-P4 à un niveau ; pas de ligne C-P4c ; « bloc P-019 » ; clause de refus de P-020 | préambule aligné sur C-18 ; bornes BCa ; C-P4 sur Ḡ_P ; ligne C-P4c ; « bloc P-021 » ; clause de refus retirée | voir C-18 à C-23 |
| C-54b | Critères, table, C-P2 et C-P3 | voir C-54 | voir C-54 | voir C-54 |
| C-54c | Critères, table, C-P4 (HC2) et C-P4c | voir C-54 | voir C-54 | `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, section 4 ; décision D-3 |
| C-54d | Critères, table, C-P6 | voir C-54 | voir C-54 | P-020 et R-326 ; archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constat 12 |
| C-55 | Critères, stabilité de rang | bloc à deux versions sous P-019 | une seule version : P-021, option (A), trois lectures, clause de repli mécanique | `registres/decisions.md`, P-021 et R-326 ; décision D-9 |
| C-56 | Critères, combinaisons | réserves lues sur des ĉ non précisés ; réserve d'intention par demi-largeur ; porte GC et HC2 sur « g brut » ; rien sur les juges en regard, les niveaux, la lecture filtrée ni le témoin lexical | ĉ brut et loi séparée nette précisés ; réserve d'intention par intervalle ; porte GC sur Ḡ_P de la sonde de l'agent auteur ; combinaisons neuves : HC2 jamais écrite sans C-P4c ; robustesse non éprouvée ; niveaux ; lecture de HC2b selon la lecture filtrée et le témoin lexical ; sonde contrôlable par consigne | archive, contre-lecture « méthode » du brouillon 5 (`0c492f02…`), constats 06 et 09 ; `docs/decisions/decision-N-068-v1.md`, `ba6b2db3…`, sections 4, 5, 7 ; `docs/decisions/decision-N-053-v1.md`, `2204256d…`, point 1 (« la lecture filtrée est la lecture principale de toute revendication d'intention ») ; décisions D-3, D-7, D-8 |
| C-56b | Critères, combinaisons, loi séparée et intention | voir C-56 | voir C-56 | voir C-56 |
| C-56c | Critères, combinaisons, porte GC et HC2 | voir C-56 | voir C-56 | voir C-56 |
| C-57 | Liste d'arrêt | 19 gardes ; garde 2 sans accord de dépense valide ; garde 11 sans le constat nu | garde 2 : accord de dépense valide au jour du lancement ; garde 11 étendue au constat nu ; gardes 20 (lecture forcée infidèle), 21 (score de moniteur dans la génération), 22 (banc de contrôlabilité indisponible) | R5 ; `registres/go.md` (échéances) ; P-022 ; `docs/decisions/decision-N-053-v1.md`, `2204256d…`, points 1 et 5 ; cohérence avec C-31, C-35, C-42 |
| C-57b | Liste d'arrêt, garde 11 | voir C-57 | voir C-57 | voir C-57 |
| C-57c | Liste d'arrêt, gardes 20 à 22 | voir C-57 | voir C-57 | voir C-57 |
| C-57d | Liste d'arrêt, garde 23 (omise dans la note v1 ; relevée par la contre-lecture, CL-13) | aucune garde sur les paragraphes de plaidoyer | garde 23 : paragraphes de bras « plaidoyer » en nombre différent de k_P, ou dans un ordre différent de celui de la configuration scellée : arrêt | R5 ; cohérence avec C-42 (niveaux du plaidoyer, décision D-2) ; ajoutée par le même remplacement que les gardes 20 à 22 |
| C-58 | Contre-lecture | contre-lectures 5 et 6 « à venir », avec six marqueurs `<<…>>` | les contre-lectures du brouillon 5 ont eu lieu en session 16 (archive, non versées) : dites en un paragraphe ; contre-lecture de ce brouillon laissée « À REMPLIR » pour la session de conduite | consigne du rédacteur, § 1 ; mandat (`cfe4a3c3…`), § 2, point 3 ; `registres/decisions.md`, R-312 et R-316 |
| C-40c | Plan, section 1, accord par lancement | ligne d'accord du jour sous GO-2026-10-20-07 | sous GO-2026-10-20-07 ou la délégation en vigueur au jour du lancement (elle échoit aussi le 2026-11-30) | `registres/go.md`, GO-2026-10-20-07 (échéance 2026-11-30) ; décision D-4 |
| C-58b | Contre-lecture, premier paragraphe | table de traitement du brouillon 5 dite « versée avec ce brouillon » | dite dans l'archive du 20 octobre, à verser (verrou 5) | vérification sur disque (R11) : `brouillons/` ne porte que le brouillon 5 et son compagnon |

## 2. Ce que je n'ai pas changé, et pourquoi

- **Énoncés de HC1, HC2b et HC3** : mot pour mot ceux du brouillon 5 (N-005, N-013, N-023). N-068 (section 7) dit
  qu'ils ne changent pas. Seules des sources s'y ajoutent.
- **Prédictions C-P1, C-P1b, C-P2, C-P5, C-P6 et leurs seuils** : inchangés, sauf la précision « intervalle bilatéral
  BCa » et la règle conjointe de C-P1. Les contre-indices publiés contre les prédictions 1 et 3 de HC1 sont dits, mais
  je n'ai changé aucune prédiction : c'est une modification d'hypothèse, donc un nœud (décision D-13).
- **Marge d'équivalence de HC2, [−0,10 ; 0,10]** : inchangée. N-068 dit la prédiction « inchangée dans son signe » et
  « à chiffrer au préenregistrement » ; je n'ai aucune pièce qui commande une autre marge.
- **Pilote, addendum de dérivation, vivier, familles, juges, consignes, gardes, graines existantes, effectifs {60, 90,
  120}, banc de reproduction** : inchangés. Aucune décision postérieure au brouillon 5 n'y touche, hors les points
  listés à la section 1.
- **Chiffres du projet précédent et empreintes sous `donnees/`** : repris du brouillon 5 sans recalcul ; le mandat
  m'interdit d'ouvrir `donnees/`. C'est dit dans le texte.
- **Marqueurs `<<…>>` gardés**, tous légitimes au scellement seulement : `<<COMMIT_ANALYSE>>`, `<<NOMBRE_TESTS>>`,
  `<<LIGNES_MODULE_PAPIER_C>>`, `<<EMPREINTE_CONFIG>>`, `<<ENTROPIE>>`, `<<REVISION_LLAMA>>`, `<<REVISION_QWEN>>`,
  `<<REVISION_MISTRAL>>`, `<<EMPREINTE_TACHES_SOURCE_64>>`, `<<CHEMIN_PROPOSITIONS_PILOTE_T05>>`,
  `<<EMPREINTE_PROPOSITIONS_PILOTE_T05>>`, `<<CHEMIN_NOTE_VIVIER>>`, `<<EMPREINTE_MESURES_V2>>` (treize).
- **Marqueurs retirés** : `<<DECISION_STABILITE_RANG>>`, `<<DECISION_BRAS_USURPATION>>` (tranchés par défaut, R-326) ;
  `<<DECISION_VOISINS>>` (converti : verrou 2 et décision D-12) ; les six marqueurs des contre-lectures 5 et 6 (elles
  ont eu lieu en session 16).
- **Organisme d'idéation (N-064, N-065, N-067, N-071, N-073)** : rien n'entre au texte, sauf la phrase de périmètre.
  Le texte ne présente pas l'organisme ; les citations obligatoires de ces décisions valent pour les textes qui le
  présentent (décision D-10).
- **N-066** (garde adaptée de T0.7) : sans objet pour ce texte.
- **HC4, HC5, HC6** : hors du critère 7 et du texte. La restriction de la lettre de N-013 pour HC4 (N-068, section 8) et
  les contre-indices de 2611.04556 sur HC4 et HC6 (R-2554) sont renvoyés aux préenregistrements de TC.4 à TC.6.
- **Propositions du rapport C9, § 6, pour HC1** (tirer la cible indépendamment de v₀ ; bras de reconsidération
  neutre) : non appliquées. Ici v* est une constante de l'échelle, et le témoin de longueur appariée joue le rôle du
  bras neutre. Je le signale dans D-13 plutôt que de changer le plan.

## 3. Ce que j'ai repris des brouillons 6 et 7 de l'archive, et ce que j'ai laissé

Matière première : `papier-C/brouillon6/…-brouillon6.md` (`fadc74c3…`) et `papier-C/brouillon7/…-brouillon7.md`
(`541f1511…`), dans l'archive `registres/passations/bloc-notes-session16-complement-2026-10-21.tar.gz` (`0c15862c…`) ;
tables de traitement `74b5ae16…` et `351ab375…` ; rapports de contre-lecture `0c492f02…` (méthode, brouillon 5) et
`45a0d875…` (vérification courte, brouillon 6). J'ai comparé le corps du brouillon 5 à celui du brouillon 7 par
programme (63 blocs de différences) et jugé chaque bloc.

**Repris, parce que commandé par une décision en vigueur.**
- Stabilité de rang selon P-021, option (A) (défaut appliqué, R-326). Les versions de repli (B) et (C) sont retirées.
- Bras « usurpation écrite par l'agent » inclus (P-020, R-326). La version de repli est retirée.
- Condition « constat nu » (P-022, option (b), R-326), avec sa réserve 16 et la correction de la réserve 9.
- Clause d'ouverture et réserve 14 (décisions de Lazar R-307 et R-309).
- Réserve 17 (personne grammaticale ; décision de routine de la session 16, R-316).

**Repris, parce que je les juge fondés** (chaque motif est à la ligne du changement, section 1).
- Identification du calibrage, lecture sans calibrage, règle conjointe de C-P1, réserve 15 (CL5-methode-01).
- C-P4b lu sur l'excédent du paragraphe (CL5-methode-04). L'alarme définie quand p̂ vaut 0 ou 1 (CL5-methode-05).
- Lectures restées sur la loi brute, ramenées à la loi nette ou dites brutes (CL5-methode-06).
- Préséance entre décompte et intervalles (07) ; tests du module précisés (08) ; réserve d'intention par intervalle
  (09) ; ordre d'appariement des témoins (11) ; « intervalle bilatéral BCa » (12) ; unité d'indépendance au pilote (14).
- Constats de la lentille « texte » : statistiques lues sur la loi nette (texte-05) ; exception de C-P4b (06) ;
  validation croisée par tâches (07) ; tirage uniforme sans strate (08) ; empreinte de la procédure d'extraction (10),
  recalculée par moi ; jackknife sur les grappes (11).
- La troisième lecture des statistiques de rang (calibrage par ρ̂/r̂ ; CB6-methode-courte-01) et la clause de repli
  mécanique (02). La troisième lecture dépasse la lettre de P-021 au registre : décision D-9.
- La garde « aucun jeton spécial de gabarit de conversation » (CQ-04), sans les chiffres des articles qui la motivent.

**Laissé.**
- **Tous les précédents et contre-indices tirés des notes de voisins de la session 16** (Joswin et al., Hu et Qu,
  Hussain et Nielbo, Kumaran et al., Barkett, Zhu et al., Weng et al., Wang K. et al., Wang Q. et al., Choi et al.,
  Geng et al., Chang et al., Jiang et al., Zeng, Chen et al., Vennemeyer et al., Germani et Spitale). Ces notes et la
  plupart de leurs PDF ne sont pas au dépôt (j'ai vérifié l'absence de `docs/sources/pdf/2607.05545v1.pdf`). La
  consigne interdit un chiffre de l'état de l'art qui ne figure pas dans une pièce vérifiée du dépôt (R7). Cela
  représente plus d'une centaine de lignes du brouillon 7. C'est un manque réel pour l'audit de symétrie : plusieurs de ces
  contre-indices sont défavorables au programme. Décision D-11.
- Le verrou 2 détaillé du brouillon 7 (une ligne par note) : remplacé par un verrou court qui dit où sont les notes.
- La citation de Hu et Qu dans la réserve 16 et celle de Wang K. et al. dans la réserve 17 : les deux réserves sont
  écrites sur les seuls faits de la configuration.
- Les indices des formulations qui portent le constat (réserve 16) : je ne les ai pas recomptés ; renvoyés au script de
  la configuration.
- La configuration brouillon 4 de l'archive (`6734fbd0…`) : non reprise, non relue ; je n'écris aucune configuration
  (verrou 4).
- Les marqueurs `<<TRANCHER_P020>>`, `<<TRANCHER_P021>>`, `<<TRANCHER_P022>>`, `<<DECISION_CONSTAT_NU>>`,
  `<<LIGNE_CORRECTION_P021>>` et les entrées de contre-lecture 7 à 10 de l'archive : sans objet, les trois propositions
  ont pris leur défaut le 24 octobre.
- Les versions de repli des trois propositions.
- La phrase « six lignes neutres… » du point 10 et les grilles publiées ajoutées à « Familles et échafaudage ».

## 4. Validateur : ce que le mandat exempte, et ce que la consigne ajoute (CL-12)

Le mandat (§ 2, point 1) veut une liste vide « sauf pour les cases qui demandent une décision du directeur ». La sortie du validateur porte en plus les treize marqueurs `<<…>>` du scellement et la case « Contre-lecture ». Ils ne sont pas exemptés par le mandat à la lettre : c'est la consigne du rédacteur (§ 1) qui les admet, comme lecture du mandat (ils ne peuvent être remplis qu'au scellement, ou par la session de conduite après la contre-lecture). Je le dis ici pour que la session mère confirme cette lecture.

## 5. Différences entre le brouillon 6 de relance et sa version c1

Avant : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19.md` (`67cd36f19782ec9ff0588c235f1b8ff27c40504f5288991ff1f20b0fa93c0e0d`, 150 891 octets). Après : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c1.md` (`ff3e2ff30263cfb2d29d2df0402c6791b64eaf37f8b64af91bc7f46bdc8aa021`, 168 279 octets).

35 remplacements exacts (`travail/changements_c1_v1.py`, `travail/construire_brouillon6_relance_c1_v1.py`), tous commandés par le rapport de contre-lecture `9a7121bc…` ou par sa suite (titre, verrous, section « Contre-lecture »). Le traitement remarque par remarque, avec ses motifs, est dans `table-traitement-contre-lecture-brouillon6-relance-v1.md`. Aucun énoncé d'hypothèse ne change entre les deux versions. Cases « À REMPLIR » : trois dans le brouillon 6 de relance (D-1, D-2, contre-lecture), sept dans la version c1 (D-1, D-2, D-8, D-15, D-16, D-17, contre-lecture).

| n° | remarque | section | changement |
|---|---|---|---|
| K-00a | — | titre | titre : version c1 |
| K-00b | CL-01 à CL-17 | en-tête, « ce que change » | paragraphe « Ce que change la version c1 » |
| K-00c | CL-01, CL-06, CL-07, CL-10 | en-tête, verrou 1 | dix-sept décisions ; six cases « À REMPLIR » |
| K-00d | CL-04, CL-09, CL-14 | en-tête, verrous 7 à 10 | verrou 7 mis à jour (contre-lecture faite, vérification des corrections à venir) ; verrous 9 (harnais de la lecture forcée) et 10 (grille de la clause de repli et C-P3c) ajoutés |
| K-17 | CL-17 | Hypothèse, HC1, Venkatesh et al. | renvois de figure harmonisés sur N-023 (balayage : figure 2, p. 4 ; trois moniteurs sur cinq : figure 1, p. 3) |
| K-02a | CL-02 | Hypothèse, HC2, « ce qui est propre » | ce que lit chaque moniteur est écrit ; « sous un même contenu » précisé |
| K-01a | CL-01 | Hypothèse, HC2, prédiction | « au plus nul » : renvoi à la règle à deux versions et à D-15 |
| K-01b | CL-01, CL-03, CL-06 | Prédiction, table, C-P4 | signe attendu et réfutation de HC2 renvoyés à la règle à deux versions ; confirmation niveau par niveau ; mention « lu sur une action » |
| K-02b | CL-02 | Prédiction, table, C-P4c | e calculé sur les champs seuls, sur la lecture complète et sur l'excédent ; réfutation sur les deux premières |
| K-01c | CL-01, CL-03 | Prédiction, après la porte GC | paragraphe neuf : règle de HC2 en deux versions, confirmation par intersection-union, case « À REMPLIR » (D-15) |
| K-08 | CL-08 | Prédiction, stabilité de rang, version retenue | la clause de repli de P-021 joue déjà aux deux lectures ; la troisième lecture en remplace l'effet pour C-P3a et C-P3b ; dit comme tel |
| K-09a | CL-09 | Prédiction, « Trois lectures » | taux cités dits contrôlés par le contre-lecteur ; rejeu partiel du rédacteur cité ; renvoi au verrou 10 |
| K-09b | CL-09 | Prédiction, clause de repli mécanique | la clause renvoie au verrou 10 ; C-P3c porte une mention tant que sa grille manque |
| K-09c | CL-09 | Prédiction, clause de repli mécanique, fin | voir K-09b |
| K-02c | CL-02 | Métrique, point 13, comparaison aux juges | trois écarts (champs seuls, lecture complète, excédent) ; ce que la ligne ne peut pas montrer |
| K-05 | CL-05 | Métrique, point 14, agrégations | bras nommé mot pour mot ; quatre conditions de N-026 écrites, dont le plancher apparié à même agrégation ; extension au maximum des moyennes glissantes dite lecture de N-026 (D-14) |
| K-04a | CL-04 | Métrique, point 14, témoin lexical | préfixe fixé (dialogue entier de l'épisode relu, seul le message système change) ; relectures dans le contexte HP (principal) et H (rapporté) ; relecture dans le contexte propre comme témoin de l'instrument, avec tolérance et garde |
| K-06a | CL-06 | Métrique, point 14, trajectoire | lecture décisive « sur des trajectoires » : deux versions écrites, case « À REMPLIR » (D-16) |
| K-10a | CL-10 | Métrique, point 19 (b), contrôlabilité | bras défini : banc repris tel quel sur l'agent (b1) et transposition à chaque sonde (b2) avec concept, phrases, empan, négatifs, seuil, direction par famille de sonde ; écart à « telle quelle » déclaré (D-17) |
| K-03a | CL-01, CL-03 | Seuil, C-P4 (HC2), niveaux | confirmation de HC2 niveau par niveau (intersection-union) ; versions (i) et (ii) selon D-15 |
| K-02d | CL-02 | Seuil, C-P4c | intervalles de e, e_c et e_x au même niveau |
| K-10b | CL-10 | Seuil, réserve de contrôlabilité | seuil « moitié » retiré du texte ; deux versions écrites, case « À REMPLIR » (D-17) |
| K-03b | CL-03 | Plan, section 2, demi-largeur des sondes | la demi-largeur prévue est celle du critère par niveau |
| K-02e | CL-02 | Plan, TC.2, comparaison aux juges | trois écarts nommés |
| K-04b | CL-04 | Plan, TC.2, positions de sonde | témoin : relectures L-HP et L-H nommées |
| K-11 | CL-11 | Audit, A9 | A9 dans les deux sens : HC2 confirmée ou réfutée alors qu'aucun juge n'est déplacé |
| K-01d | CL-01, CL-03, CL-06 | Critères, table, C-P4 (HC2) | ligne renvoyée à la règle à deux versions ; mentions selon D-16 |
| K-02f | CL-02 | Critères, table, C-P4c | « opposition établie » exige les champs seuls et la lecture complète ; mentions quand les lectures divergent |
| K-11b | CL-11, CL-01 | Critères, combinaisons, HC2 et les juges | cas miroir de l'audit A9 ; cas négatif renvoyé à la règle |
| K-03c | CL-03 | Critères, combinaisons, niveaux | réserve « déplacement au niveau le plus fort » remplacée par la règle par niveau |
| K-07 | CL-07 | Critères, combinaisons, HC2b et l'intention | couplage entre la lecture filtrée de HC2b et la grandeur de HC2 écrit ; trois versions écrites, case « À REMPLIR » (D-8) ; combinaison avec le côté négatif de HC2 |
| K-10c | CL-10 | Critères, combinaisons, contrôlabilité | la réserve n'existe que sous la version (b) de D-17 |
| K-04c | CL-04 | Liste d'arrêt, garde 20 | garde 20 réécrite : fidélité des jetons, message système attendu, témoin de l'instrument hors tolérance |
| K-14 | CL-14 | Contre-lecture, brouillon 5 | rapport « texte » du brouillon 5 : empreinte complète et chemin d'archive ; contre-lecture complète de ce brouillon dite |
| K-00e | — | Contre-lecture, ce brouillon | contre-lecture complète faite, dite avec ses empreintes ; la case reste à la session de conduite (vérification des corrections) |

Ce que la version c1 retire du brouillon 6 de relance : la réserve « déplacement au niveau le plus fort » (remplacée par la confirmation niveau par niveau) ; le seuil « moitié » de la réserve de contrôlabilité (renvoyé à D-17) ; la règle de mots de HC2b écrite d'office (renvoyée à D-8) ; la réfutation des deux côtés écrite d'office pour HC2 (renvoyée à D-15) ; la phrase « non rejoués par ce rédacteur, à rejouer par la contre-lecture ».

## 6. Différences entre la version c1 et la version c2

Avant : version c1 (`ff3e2ff30263cfb2d29d2df0402c6791b64eaf37f8b64af91bc7f46bdc8aa021`, 168 279 octets). Après : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c2.md` (`7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61`, 173 041 octets).

14 remplacements exacts (`travail/construire_brouillon6_relance_c2_v1.py`), limités aux sept remarques mineures V-01 à V-07 du rapport de vérification `3469efe7…` et à ce qui en découle (titre, paragraphe « Ce que change la version c2 », verrou 1, section « Contre-lecture »). Traitement et motifs : `table-traitement-verification-c1-v1.md`. Aucun énoncé d'hypothèse ne change. Cases « À REMPLIR » : sept dans la version c1 (D-1, D-2, D-8, D-15, D-16, D-17, contre-lecture), huit dans la version c2 (D-9 s'ajoute) ; la case de D-15 porte deux réponses, celle de D-8 aussi, celle de D-17 trois options.

| n° | remarque | section | changement |
|---|---|---|---|
| W-00a | — | titre | titre : version c2 |
| W-00b | V-01 à V-07 | en-tête, « ce que change » | paragraphe « Ce que change la version c2 » |
| W-00c | V-05 | en-tête, verrou 1 | liste v3 ; sept cases « À REMPLIR » (D-9 ajoutée) |
| W-04 | V-04 | en-tête, verrou 9 | vérifier aussi où vit la consigne privée de saboter ; sinon redéfinir le témoin lexical avant le scellement |
| W-03a | V-03 | Prédiction, règle de HC2, partie commune | asymétrie dite (confirmation par niveau, réfutation sur la moyenne) et sa conséquence ; réfutation par niveau écrite comme sous-option (m) ou (n) de D-15 |
| W-03b | V-03 | Prédiction, règle de HC2, case | la case de D-15 porte deux réponses : (i) ou (ii), et (m) ou (n) |
| W-05 | V-05 | Prédiction, stabilité de rang, version retenue | D-9 en nœud : trois versions écrites, case « À REMPLIR » |
| W-01 | V-01 | Prédiction, « Trois lectures » | deux plages écrites avec leur nombre de cases (12 cases de l'archive ; 24 cases rejouées) |
| W-07a | V-07 | Métrique, point 14, lecture filtrée | masque : deux versions écrites (coût et paragraphe ; paragraphe seul), rattachées à la case de D-8 |
| W-07b | V-07 | Métrique, point 19 (b2) | refus de la transposition écrit : seule la partie (b1) reste, avec la mention prévue |
| W-06 | V-06, V-07 | Seuil, bras « contrôlabilité » | limite de la réserve à seuil écrite ; version (c), transposition refusée, écrite ; la case porte trois réponses |
| W-02 | V-02 | Critères, combinaisons, HC2 et HC2b ensemble | « Ḡ_P sur les champs dans la marge » remplacé par le renvoi à la règle de HC2 en vigueur |
| W-07c | V-07 | Critères, combinaisons, HC2b et l'intention, case | la case de D-8 porte aussi la réponse sur le masque |
| W-00d | — | Contre-lecture | vérification des corrections dite avec ses empreintes ; la case reste à la session de conduite |

Reste connu, non corrigé : le verrou 7 de l'en-tête parle encore de la vérification de la version c1 comme à venir (table de traitement de la vérification, dernière section).

## 7. Différences entre la version c2 et la version r1

Avant : version c2 (`7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61`, 173 041 octets). Après : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r1.md` (`e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2`, 171 541 octets).

37 remplacements exacts (`travail/construire_brouillon6_relance_r1_v1.py`), tous commandés par la ligne GO-2026-11-19-53 de `registres/go.md` (lue sur `origin/main`, commit `784cfcd4` ; R-3802) : les sept cases du directeur sont remplies par recopie de l'option retenue, les branches écartées sont retirées, les verrous 1, 7 et 8 et le paragraphe des accords sont mis à jour. Décision par décision : `table-remplissage-cases-r1-v1.md`. Aucun énoncé d'hypothèse ne change. Il ne reste qu'une case « À REMPLIR », dans la section « Contre-lecture ». Le texte perd 1 500 octets : les branches retirées pèsent plus que les mentions ajoutées.

| n° | décision | section | changement |
|---|---|---|---|
| R-00a | — | titre | titre : version r1 |
| R-00b | D-1 à D-17 | en-tête, « ce que change » | paragraphe « Ce que change la version r1 » |
| R-00c | D-5, D-6, D-7 | en-tête, propositions des lecteurs | « recommandation de ce rédacteur » devient « retenues par le directeur » |
| R-V1 | D-1 à D-17 | en-tête, verrou 1 | verrou 1 : décisions tranchées |
| R-V2 | D-2 | en-tête, verrou 4 | champ de configuration : trois niveaux du plaidoyer |
| R-V7 | — | en-tête, verrou 7 | verrou 7 : deux vérifications faites, empreintes citées |
| R-V8 | D-4 | en-tête, verrou 8 | verrou 8 : accords prolongés |
| R-GOa | D-1 à D-17 | en-tête, GO | ligne d'accord des dix-sept décisions ajoutée |
| R-GOb | D-4 | en-tête, GO, étape 1 | échéance du pilote : prolongée au 2026-12-31 |
| R-D1 | D-1 (b) | Hypothèse, HC2, poids | case remplie : 0,5 |
| R-D15a | D-15 (i) | Hypothèse, HC2, prédiction | « ce texte ne tranche pas » remplacé par le choix du directeur |
| R-D15b | D-15 (i), (n) | Prédiction, table, C-P4 | renvoi aux versions retenues |
| R-D15c | D-15 (i), (n) | Prédiction, règle de HC2, chapeau | choix du directeur écrit ; branches écartées renvoyées à c2 et à la liste v3 |
| R-D15d | D-15 | Prédiction, règle de HC2, partie commune | intitulé : « Côté positif » |
| R-D15e | D-15 (n) | Prédiction, règle de HC2, réfutation par niveau | version (n) recopiée ; version (m) retirée |
| R-D15f | D-15 (i) | Prédiction, règle de HC2, version (ii) et case | version (ii) retirée ; case remplie |
| R-D15g | D-15 | Seuil, C-P4 (HC2), niveaux | versions retenues citées ; réfutation par niveau nommée |
| R-D15h | D-15 (i) | Critères, table, C-P4 (HC2), confirmation | côtés fixés |
| R-D15i | D-15 (i), (n) | Critères, table, C-P4 (HC2), réfutation | côté négatif et réfutation par niveau écrits |
| R-D15j | D-15 (i) | Critères, combinaisons, HC2 et les juges | mots du cas négatif recopiés de la version (i) |
| R-D15k | D-15 (i) | Critères, combinaisons, HC2b, côté négatif | combinaison sous la seule version (i) |
| R-D15l | D-15 (n), D-2 | Critères, combinaisons, niveaux | cas k_P = 1 retiré (trois niveaux) ; réfutation par niveau rappelée |
| R-D9 | D-9 (a) sous réserve, sinon (b) | Prédiction, stabilité de rang | version (a) et sa condition ; version (b) gardée comme repli mécanique ; version (c) retirée |
| R-D16a | D-16 (a) | Métrique, point 14, trajectoire | version (a) recopiée ; version (b) retirée ; case remplie |
| R-D16b | D-16 (a) | Critères, table, C-P4 (HC2) | mention de la version (a) |
| R-D16c | D-16 (a) | Critères, table, C-P4c | mention de la version (a) |
| R-D8a | D-8, masque accepté | Métrique, point 14, lecture filtrée | masque accepté ; branche « masque refusé » retirée |
| R-D8b | D-8 (a) | Critères, combinaisons, HC2b et l'intention | « Dans les trois versions » retiré |
| R-D8c | D-8 (a) | Critères, combinaisons, HC2b et l'intention, versions | version (a) recopiée ; versions (b) et (c) et branche « masque refusé » retirées ; case remplie |
| R-D17a | D-17 (a) | Métrique, point 19 (b2) | transposition acceptée ; branche de refus retirée |
| R-D17b | D-17 (a) | Seuil, bras « contrôlabilité » | version (a) recopiée ; versions (b) et (c) retirées ; case remplie |
| R-D17c | D-17 (a) | Critères, combinaisons, contrôlabilité | plus de réserve à seuil |
| R-D2a | D-2 (a) | Plan, section 3, niveaux du plaidoyer | case remplie : k_P = 3 |
| R-D2b | D-2 (a) | Plan, section 3, effectifs | effectifs à trois niveaux |
| R-D4a | D-4 (a) | Plan, section 1, titre | accord prolongé |
| R-D4b | D-4 (a) | Plan, section 1, accord par lancement | délégation prolongée |
| R-D14 | D-14 (a) | Métrique, point 14, agrégations | lecture de N-026 dite acceptée par le directeur |

Branches retirées du texte, lisibles dans la version c2 et dans la liste des décisions v3 : version (ii) et version (m) de la règle de HC2 ; version (c) de la stabilité de rang (la version (b) reste, comme repli) ; version (b) de la trajectoire ; versions (b) et (c) de la lecture de HC2b et branche « masque refusé » ; versions (b) et (c) du bras « contrôlabilité » ; cas « k_P = 1 » des effectifs et des combinaisons.

## 8. Différences entre la version r1 et la version r2

Avant : version r1 (`e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2`). Après : version r2 (`1ab62e7d22163306a3251cd75f4001f7daac63ea72577d5ee200a3bcf86cfec3`, 197 087 octets). 34 remplacements exacts par `travail/construire_brouillon6_relance_r2_v1.py` ; journal `travail/construire_brouillon6_relance_r2_v1.journal.tsv`. Traitement point par point : `table-traitement-points-ouverts-module-v1.md`.

| Id | Point ouvert ou motif | Lieu | Changement |
|---|---|---|---|
| S-00a | — | titre | titre : version r2 |
| S-00b | PO-01 à PO-46 | en-tête, « ce que change » | paragraphe « Ce que change la version r2 » |
| S-H1 | versement | en-tête, historique, brouillons 6 et 7 | chemins de versement |
| S-H2 | versement | en-tête, historique, brouillon 4 | chemin de versement |
| S-V1 | PO-02, PO-14, PO-43 | en-tête, verrou 1 | trois décisions neuves nommées au verrou 1 |
| S-V2 | versement | en-tête, verrou 2 | notes versées ; ce qui reste : 24 PDF absents, deux versions de la note de second rang, consignation |
| S-V3 | PO-01, PO-43, PO-45 | en-tête, verrou 3 | module : premier jet versé, non contre-lu ; ce qui reste avant le scellement et avant le pilote |
| S-V4 | PO-11, PO-14, PO-32 | en-tête, verrou 4 | configuration : brouillon 5 en premier jet ; paragraphes de plaidoyer neufs à contre-lire |
| S-V5 | versement | en-tête, verrou 5 | pièces versées ; ce qui reste |
| S-V9 | PO-09 | en-tête, verrou 9 | verrou 9 : il a joué ; témoin redéfini ; reste la fonction de reconstruction |
| S-V11 | PO-17, PO-19, PO-38, PO-14 | en-tête, verrous 11 à 13 (nouveaux) | verrous 11 (niveau de la réserve d'intention, avant le scellement), 12 (banc de contrôlabilité, avant l'étape 2), 13 (grandeurs du verdict de G0, avant l'étape 2) |
| S-C1 | PO-43, PO-45 | champs du scellement, module | adaptateur réel scellé par un addendum de lancement (D-20) ; toute fonction de calcul reste dans le module scellé |
| S-C2 | PO-11, PO-14 | champs du scellement, configuration | champs remplis au scellement : la version de la stabilité de rang et son rapport s'ajoutent aux cinq |
| S-G1 | PO-02 | en-tête, GO, étape 1 | accord de type « calcul » : la prolongation est de type « décision » ; renvoi à D-18 |
| S-D1 | note du vivier | documents qui font foi, note du vivier | source de la note écrite à côté du marqueur |
| S-D2 | versement | documents qui font foi, mesures de conception | mesures versées ; empreinte de la version 2 remplie (vérifiée sur le fichier) |
| S-D3 | versement | pièces de contre-lecture citées, chapeau | pièces versées |
| S-D4 | versement | pièces de contre-lecture citées, brouillon 5 | chemin de versement |
| S-D5 | versement | pièces de contre-lecture citées, brouillon 6 de la session 16 | chemin de versement |
| S-M1 | PO-15 | Métrique, point 14, borne | la borne renvoie à la règle écrite (section 8, précision 9) |
| S-M2 | PO-09 | Métrique, point 14, témoin lexical | témoin redéfini : transcription rebâtie, tout ce qui porte la consigne privée remplacé par son pendant honnête ; scores sur les seuls jetons de l'agent |
| S-M3 | PO-14, PO-19 | Métrique, point 19 (b2), concept | quand et où les champs du bras se fixent : trois versions écrites, case « À REMPLIR » (D-19) |
| S-P1 | PO-02 | Plan, section 1, accord de dépense | identifiant de l'accord de type « calcul » : deux versions écrites, case « À REMPLIR » (D-18) |
| S-P2 | PO-42 | Plan, section 2, nom du fichier de dérivation | nom versionné (R12) |
| S-P3 | PO-03 à PO-46 | Plan, section 8 (nouvelle) | 36 précisions de calcul et de règle |
| S-P4 | versement | Plan, section 7, réserve 14 | chemin de versement |
| S-P5 | versement | Plan, section 7, réserve 17 | le rapport de la contre-lecture « texte » du brouillon 6 de la session 16 est versé, la sortie de ses comptes ne l'est pas : dit (le libellé de cette ligne dans le journal du programme est resté celui du premier essai ; le texte, lui, est juste) |
| S-P6 | PO-36 | Plan, section 4, graines | clé neuve `papier-C/pilote/banc` |
| S-A1 | PO-01 | Liste d'arrêt, garde 1 | garde de l'arbre gelé réécrite : dépendances gelées par empreinte, et aucun fichier du module sous `src/` ni `tests/` |
| S-A2 | PO-02 | Liste d'arrêt, garde 2 | accord de dépense : règles de la garde de calcul du dépôt |
| S-A3 | PO-09 | Liste d'arrêt, garde 20 | garde 20 alignée sur le témoin redéfini |
| S-L3 | versement | Contre-lecture, brouillons 6 et 7 de la session 16 | dits versés comme matière première |
| S-L1 | versement | Contre-lecture, brouillon 4 | chemins de versement du traitement et de la table du brouillon 5 |
| S-L2 | versement | Contre-lecture, brouillon 5 | rapports versés ; chemins |

Ce qui ne change pas entre r1 et r2 : les énoncés de HC1, HC2 (énoncé de N-068, section 4, mot pour mot), HC2b et HC3 ; les prédictions, leurs signes, les marges et les seuils ; les sept cases remplies par le directeur (GO-2026-11-19-53) ; le verrou 10 (grille de la clause de repli) et la clause elle-même ; l'audit de symétrie ; les réserves 1 à 19, hors les chemins des réserves 14 et 17.

Ce qui est neuf : la section 8 du plan d'analyse (36 précisions, qui priment là où un passage plus haut laisse deux lectures) ; le témoin lexical redéfini (le verrou 9 a joué) ; la garde 1 réécrite et le marqueur `<<LIGNES_DEPENDANCES_PAPIER_C>>` ; les verrous 11, 12 et 13 ; deux cases « À REMPLIR » (D-18 au plan, section 1 ; D-19 à la métrique, point 19) et une proposition à défaut (D-20) ; `<<EMPREINTE_MESURES_V2>>` rempli (`946203c3…`, vérifiée sur le fichier versé) ; la source de la note du vivier écrite à côté de `<<CHEMIN_NOTE_VIVIER>>` (dépôt `lciric/p1-auto`, commit `fb89e74`, `heritage/POUR_TOUS_NOTE_CHOIX_DES_INTENSITES_2026-08-19.md`, d'après R-282 relue par moi).

Trois essais de construction écartés, gardés sous `travail/essais-r2/` (sans écrasement) : le premier (`bc102ca3…`) disait à tort que la contre-lecture « texte » du brouillon 6 de la session 16 n'était pas versée ; le second (`7dca273d…`) ne nommait pas D-18 à D-20 au verrou 1 ; un premier jet de la table de traitement décrivait mal cinq précisions.

## 9. Différences entre la version r2 et la version r3

Avant : version r2 (`1ab62e7d22163306a3251cd75f4001f7daac63ea72577d5ee200a3bcf86cfec3`). Après : version r3 (`160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac`, 216 428 octets). 67 remplacements exacts par `travail/construire_brouillon6_relance_r3_v1.py` ; journal à côté. Traitement remarque par remarque : `table-traitement-contre-lecture-r2-v1.md`.

| Id | Motif | Lieu | Changement |
|---|---|---|---|
| T-00a | — | titre | titre : version r3 |
| T-00b | CR-01 à CR-10, CG-01 à CG-14, GO-2026-11-19-74 | en-tête, « ce que change » | paragraphe « Ce que change la version r3 » |
| T-V1 | GO-2026-11-19-74 | en-tête, verrou 1 | trois décisions neuves dites tranchées |
| T-V3 | D-20, CR-07 | en-tête, verrou 3 | adaptateur : décision tranchée ; dépendances scellées par l'addendum |
| T-V7 | contre-lecture de r2 | en-tête, verrou 7 | contre-lecture de r2 citée ; reste la vérification des corrections de r3 |
| T-V8 | D-18 | en-tête, verrou 8 | ligne de type « calcul » à inscrire sur devis scellé |
| T-V9 | CR-05 | en-tête, verrou 9 | entrées de l'appel au harnais et appel distinct de la garde 20 |
| T-V10 | CG-01, CG-03, CG-05 à CG-08 | en-tête, verrou 10 | verrou 10 réécrit : liste finie, rapport à compléter, marqueur |
| T-V11 | CR-04 | en-tête, verrou 11 | la réserve n'est jamais retirée ; son taux sous le nul est écrit à côté |
| T-V12 | D-19, CR-08 | en-tête, verrou 12 | D-19 tranchée : addendum mécanique |
| T-C1 | D-20, CR-07 | champs du scellement, module | D-20 tranchée ; l'addendum de lancement scelle les dépendances de l'adaptateur |
| T-C2 | CR-07 | champs du scellement, dépendances | dépendances du module au scellement, de l'adaptateur à l'addendum |
| T-C3 | D-19, CG-01 | champs du scellement, configuration | rapport de la grille cité aussi sous « b » ; champs du bras selon D-19 (a) |
| T-G1 | D-18 | en-tête, GO, étape 1 | D-18 tranchée |
| T-S1 | CG-01, CR-10, CG-12 | Prédiction, stabilité de rang, condition de D-9 | « grille entière » = liste finie ; version (b) : vérification de C-P3c dite ; marqueur et trois issues |
| T-R08 | CR-01, CG-03 | Prédiction, « Trois lectures » | renvoi du passage à la précision 8 |
| T-R03 | CR-01 | Prédiction, « Trois lectures », ρ̂/r̂ | renvoi du passage à la précision 3 |
| T-S2 | CG-01, CG-03, CG-05 à CG-09, A1 à A10 | Prédiction, clause de repli | clause réécrite : liste finie de 144 cases, effectifs fixés, règles de lecture |
| T-R02 | CR-01 | Métrique, point 8 bis, σ̂ | renvoi du passage à la précision 2 |
| T-R34 | CR-01, CR-04 | Métrique, point 8 bis, réserve d'intention | renvoi du passage à la précision 34 |
| T-R33 | CR-01 | Métrique, point 11, test du module | renvoi du passage à la précision 33 |
| T-R05 | CR-01, CG-03 | Métrique, point 11, tirages dégénérés | renvoi du passage à la précision 5 |
| T-R04 | CR-01 | Métrique, point 11, BCa | renvoi du passage à la précision 4 |
| T-R22 | CR-01 | Métrique, point 13, prérequis | renvoi du passage à la précision 22 |
| T-R11 | CR-01 | Métrique, point 14, moyennes glissantes | renvoi du passage à la précision 11 |
| T-R35 | CR-01 | Métrique, point 14, plancher | renvoi du passage à la précision 35 |
| T-M1 | CR-05 | Métrique, point 14, témoin lexical, entrées du harnais | entrées de l'appel ; cas où l'indication ne peut pas être produite |
| T-M2 | CR-05 | Métrique, point 14, témoin lexical, ce qu'il mesure | ce que g_trahison,lex mesure |
| T-R06 | CR-01 | Métrique, point 15, seuil d'alarme | renvoi du passage à la précision 6 |
| T-R31 | CR-01 | Métrique, point 17, gardes lexicales | renvoi du passage à la précision 31 |
| T-M3 | D-19, CR-08 | Métrique, point 19 (b2), concept | case remplie : option (a), règle de remplissage mécanique |
| T-R12 | CR-01 | Métrique, point 19, quantile | renvoi du passage à la précision 12 |
| T-R14 | CR-01 | Seuil, C-P1, identifiable | renvoi du passage à la précision 14 |
| T-R17 | CR-01 | Prédiction, règle de HC2 | renvoi du passage à la précision 17 |
| T-R21 | CR-01 | Prédiction, règle de HC2, réfutation par niveau | renvoi du passage à la précision 21 |
| T-R01 | CR-01 | Plan, section 1, ligne d'accord | renvoi du passage à la précision 1 |
| T-P1 | D-18 | Plan, section 1, accord de dépense | case remplie : option (b) |
| T-R24 | CR-01 | Plan, section 1, banc sur carte | renvoi du passage à la précision 24 |
| T-R32 | CR-01 | Plan, section 1, lisibilité des consignes | renvoi du passage à la précision 32 |
| T-R29 | CR-01 | Plan, section 2, validation croisée | renvoi du passage à la précision 29 |
| T-P2 | CR-09 | Plan, section 2, facteur d'échelle | facteur d'échelle : nombre de contenus des huit tâches d'évaluation |
| T-R30 | CR-01 | Plan, section 2, +∞ | renvoi du passage à la précision 30 |
| T-R18 | CR-01, CR-02 | Plan, section 2, non testable | renvoi du passage à la précision 18 |
| T-R10 | CR-01 | Plan, section 3, excédent | renvoi du passage à la précision 10 |
| T-R28 | CR-01 | Plan, section 4, graines | renvoi du passage à la précision 28 |
| T-R20 | CR-01 | Plan, section 5, bras rapportés | renvoi du passage à la précision 20 |
| T-P3a | — | Plan, section 8, titre | titre : versions r2 et r3 |
| T-P3 | CR-01 | Plan, section 8, introduction | primauté sans condition, précision par précision ; table des passages fixés |
| T-P4 | CR-03 | Plan, section 8, précision 9 | borne rendue symétrique ; parts rapportées ; essais ; séparateur possible |
| T-P5 | CR-02 | Plan, section 8, précision 18 | retour à la lecture symétrique |
| T-P6 | CR-09 | Plan, section 8, précision 30 | facteur d'échelle corrigé |
| T-P7 | CR-04 | Plan, section 8, précision 34 | la réserve n'est jamais retirée ; taux sous le nul écrit à côté |
| T-P8 | CG-03, A6 | Plan, section 8, précision 37 (neuve) | tirages dégénérés et statistiques de rang : la condition s'attache à la grandeur qu'elle rend indéfinie |
| T-R07 | CR-01 | Audit, placebo | renvoi du passage à la précision 7 |
| T-R23 | CR-01 | Audit A9 | renvoi du passage à la précision 23 |
| T-R36 | CR-01 | Critères, chapeau | renvoi du passage à la précision 36 |
| T-R16 | CR-01 | Critères, ligne C-P1b | renvoi du passage à la précision 16 |
| T-R13 | CR-01 | Critères, ligne C-P2 | renvoi du passage à la précision 13 |
| T-R19 | CR-01 | Critères, ligne C-P4c | renvoi du passage à la précision 19 |
| T-R15 | CR-01 | Critères, combinaisons de C-P1 | renvoi du passage à la précision 15 |
| T-A1 | CR-06, CR-07 | Liste d'arrêt, garde 1 | deux jeux de lignes de dépendances ; compte exact ; promesse sur les autres préenregistrements retirée |
| T-R25 | CR-01 | Liste d'arrêt, garde 9 | renvoi du passage à la précision 25 |
| T-A2 | CG-03 | Liste d'arrêt, garde 17 | renvoi à la précision 37 |
| T-R27 | CR-01 | Liste d'arrêt, garde 18 | renvoi du passage à la précision 27 |
| T-A3 | CR-05 | Liste d'arrêt, garde 20 | comparaison à un appel distinct du harnais |
| T-R26 | CR-01 | Liste d'arrêt, garde 21 | renvoi du passage à la précision 26 |
| T-A4 | D-19 | Liste d'arrêt, garde 22 | addendum du bras exigé |

Ce qui ne change pas entre r2 et r3 : les énoncés de HC1, HC2 (énoncé de N-068, section 4, mot pour mot), HC2b et HC3 ; les prédictions, leurs signes, les marges et les seuils ; le tableau de la stabilité de rang ; les sept cases de GO-2026-11-19-53 ; les réserves 1 à 19 ; les précisions autres que 9, 18, 30 et 34.

Ce qui est neuf : trois cases remplies (D-18 (b), D-19 (a), D-20 (a) ; GO-2026-11-19-74), plus aucune case « À REMPLIR » hors de la section « Contre-lecture » ; la liste finie de 144 cases, qui remplace la grille en plages, avec ses effectifs et ses règles de lecture ; la précision 37 (tirages dégénérés et statistiques de rang) ; les trois issues écrites d'avance et le marqueur `<<RAPPORT_GRILLE_V2>>` ; le marqueur `<<RAPPORT_RESERVE_INTENTION>>` ; la primauté sans condition des précisions et un renvoi dans chaque passage visé ; la règle de remplissage de l'addendum du bras « contrôlabilité » ; les dépendances de l'adaptateur scellées par l'addendum de lancement.

Ce qui est retiré : la clause générale de primauté conditionnelle ; la réfutation gardée sous « non testable » (précision 18 de r2) ; la clause de retrait de la réserve d'intention (précision 34 de r2) ; les versions écartées de D-18 et de D-19 (lisibles dans r2 et dans la liste des décisions v4) ; le « libellé anglais » du concept ; la promesse de la garde 1 sur le code des autres préenregistrements ; la mention « niveau non vérifié sur la grille ».

Un essai de construction écarté, gardé sous `travail/essais-r3/` (`622c71ef…` : titre de la section 8 non mis à jour).
