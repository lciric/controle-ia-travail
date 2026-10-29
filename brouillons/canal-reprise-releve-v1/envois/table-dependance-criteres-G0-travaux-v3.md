# Table de dépendance « critères de G0 → travaux du programme » — v3 — BROUILLON (non contre-lu, non scellé)
**Déclaration.** Je n'ai écrit ni la v1 (`e2480618…`), ni la v2 (`82d98947…`), ni la contre-lecture de la v1 (`3c5c51bc…`), ni celle de la v2 (`fdd87a7f…`). Modèle : Sonnet 5.5 (sous-agent neuf). Heure `date -u` au début : 2026-10-29 12:06:13 UTC ; à la fin : 2026-10-29 12:28:43 UTC. Interdits tenus : rien lu sous `donnees/`, `prereg/P3-consignes-v1.md`, `diag/*/traces` ; aucune branche ; aucune commande git ; aucune dépense ; aucun fichier existant modifié ; rien scellé. La v1 et la v2 demeurent telles quelles (R12).
**Empreintes** (`sha256sum`) des fichiers lus : v1 `e2480618816d6bcbea77654fe805b82a8e1333cddc428ea1ce6c03e75e6fe4f5` ; v2 `82d98947ef18b0ecd8df5a3c84b58c17080fb9a88a430a4955a9d1f8f0c8b39a` ; contre-lecture v1 `3c5c51bcdb40ba55f7672f72e8f18f09a3e9ff06881a6bc0daca4057f6b9d22c` ; contre-lecture v2 `fdd87a7f680597bdc2ab827bf8182f5552142a06556a74133228f3eb3150314e` ; avis sur le repli `62cc6fbf4793d477cd9ca22a168febe3abc5ee3887fcd78db4d31b891dc50aab` ; grille (copie `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/grille-G0-v1.md`) `320af9b0b367c08ddcb08d39979ca9c014157d14701b107369b760be48a76a34` ; brief v2 `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` (l. 106-201, 205-208, 214-249, 286-289, 308-311, 330-350 lues) ; `CLAUDE.md` `a2aabda8a181d46d9723bad44ad352b5e61650634e0f3bc4863451229af00b1b` ; `registres/decisions.md` `e9ba835bc2c30e4daf2df8a75488b9fa617d3c30f5c52876100647b603efe8ab` (vivant, 707 lignes à 12:06 UTC, l. 660-707 lues). Lus en plus (16 caractères) : messages n° 204 `9ad6366d9afc2a2f`, 206 `3d500f5b9c1c5e54`, 210 `e3582250a602cb15`, 215 `12b4cf9078eeeae5`, 216 `c376b9a77e4f7a18` ; brouillon 4 de T0.7 (T7) `a292088ca6e7f593` ; décision pilote couche 2 v5 (DP) `255a364e710cd713` ; paramètres de la garde δ (PG) `db6037507f23d1ee` ; programme de conception v2 (PC) `353515fffa33bb93` ; P-040 (P40) `b44bf8a062bfc4a8` ; `registres/etat.md` (E) `54d7bb738a71b569` (l. 30-52, 80-100 lues). Lectures de T7, DP, PG, PC, P40 : parties citées. **Non relus** : note moissonneur (MO), note tour (c) (TC), devis v7 nonies (DV) ; B l.252-284 et l.346-348 ; leurs citations (W27, W34 à W36, W02) sont reprises de la v2.
**Avant usage** : contre-lecture R2 par un sous-agent neuf ; mot de Lazar sur le § 8 ; scellement de la table et du script avant V1. Sans effet si V1 est « franchie ».

## 0. Clause de repli de référence (la clause prime ; si la clause scellée diffère, la table est à refaire)
La synthèse du collisionneur (`527f5853…`, R-464) est introuvable sur ce poste ; sa « table commune » n'a pas été lue. Seule sa structure est connue par le message n° 204. Texte retenu, reconstruit de l'avis (§ 4), R-452 (31 janvier 2027), R-470 (n° 206) et R-765 (cité par R-478 et n° 210) : « Si le verdict R13 de G0 (V1), prononcé au plus tard le 30 novembre 2026 à 23:59 UTC, n'est pas « franchie » (« non franchie » et « non concluante » ont la même suite), la porte est reportée une seule fois au 31 janvier 2027. Critères inchangés. Pendant le report : les travaux de la table scellée s'ouvrent ou se ferment selon sa règle ; aucune expérience décisive de G1 ni du papier C ; un critère « non tenu — négatif » est gelé jusqu'au second verdict ; au 31 décembre 2026, un lecteur neuf R13 constate seulement, pour les critères « non tenu — absent », qu'un produit scellé et son verdict par critère existent, sans verdict de porte, un GO, même grille, résultat scellé. Au 31 janvier 2027, second verdict R13 ; s'il n'est pas « franchie », la phase 0 est close « non franchie » et toute reprise exige une version nouvelle du programme. Aucun second report. »

## 1. Constats → traitement
| constat | traitement dans la v3 |
|---|---|
| CT2-01 (bloquant) ligne de T0.7 absente ; verdict de T0.6 et scellement des règles d'arrêt non nommés | **Accepté.** W40 (préenregistrement de T0.7, produit P-7, sert 3 : T7 l.1-3, G l.235) ; W41 (étape 2 de T0.6, lecture et verdict scellé = produit P-V6) ; W42 (scellement de P-ARR, que W23 cite sans le produire) ; W13 nomme ses deux préenregistrements. |
| CT2-02 (bloquant) « dépense externe » = tout accès au réseau, source muette | **Accepté.** Remplacée par « dépense facturée » (§ 2). Poussées vers `controle-ia-travail`, veille, récupération de PDF et de métadonnées sans appel de modèle payant : ni dépense ni nœud. Fausse source B l.366-367 retirée. |
| CT2-03 produits propres de W14 asymétriques ; écart entre options | **Accepté.** Une seule option subsiste (b), donc aucun écart. P-7 et P-8 ajoutés à l'étape 2 (W41), non à l'étape 1 (W14) : G l.477-480 écrit « avant l'étape 2 ». |
| CT2-04 option (b) non opérante | **Accepté.** L2 (gel), L3, L8, § 6.2 ; N est remplacé par A, G, V, C (§ 2). |
| CT2-05 test de produit indéfini ; pas de table inverse (b) | **Accepté.** § 2 : tests T1 à T4, date d'usage = commit de départ de l'étape, une étape par famille lue ; § 3 : chemins, producteurs et table inverse par produit ; § 5 : tables inverses par critère et cas cumulés. |
| CT2-06 mots et sources résiduels | **Accepté.** (i) W37 liste ses documents (E l.85-95) ; (ii) et (iii) toute dépendance déduite porte † (§ 7 : nombre calculé) ; (iv) citations corrigées : W15 (T7 l.85), W17 (T7 l.5, l.10, l.69-74, l.147-148 : P7 et P8 sont à réserve de validité, non descriptives), W23 (DP l.1, l.89-92, l.128), W24 (DP l.43, PC l.99 ; « banque pleine » remplacée par « fabrication à l'échelle »). |
| CT2-07 § 2 ne séparait pas « l'organisme » ; gardes C1 et C6 disparues | **Accepté.** § 2 les sépare. C1 (« aucune sortie de la course n'entre dans un run avant G0 ») et C6 (« aucun résultat de P3 ne modifie le préenregistrement de G1 scellé ») **écartées** : C1 sans source (CT-02 de la v1) ; les gardes écrites sur les sorties de la course sont P-9 et N-053 (R-446, R-448), non dupliquées ici ; C6 couverte par R1 et R12. Lazar peut les rétablir. |
| CT2-08 audit R4 faux (12, 2, retrait affirmé) | **Accepté.** § 7 recompte par l'annexe A (v1 contre v3, retrait calculé, classes recalculées sans date). « Sert 6 » retiré de W22 et de W23 (A2). |
| CT2-09 § 8.1 : mauvaise ligne ; GO-11 | **Accepté.** § 6.5 règle unique ; GO cités par R-455 et R-478 ; GO-11 : § 8 (7). |
| CT2-10 script inexistant ; arrêt au second verdict ; W38 ; précédence | **Accepté.** Annexe A (script séparé, modes `verifier`, `feuille`, `artefact`) ; § 6.1, § 6.6 ; W38 (classe H) hors de « cesser » ; § 0. |
| CT2-11 date de scellement de la table | **Non traitable ici** : décision de Lazar (§ 8 (6)). |
| D-TD-1 : (c) devient (b) verrouillée (R-470) | N'est plus un nœud. Constat seulement (§ 6.2) ; aucun verdict de porte ; critères « négatif » gelés (L2) ; un GO, même grille, résultat scellé ; seule lecture de porte : 31 janvier. |

## 2. Définitions (mécaniques ; aucun jugement après V1)
- **États** (G « Métrique ») lus dans V1 : tenu ; **A** « non tenu — absent » ; **G** « non tenu — négatif » ; **V** « non tenu — invalide » ; **C** « non concluant ». **A'** = A moins les critères que le constat du 31 décembre déclare « présents » ; avant le constat, A' = A. L'ensemble N de la v2 est supprimé.
- **Produit** : pièce de la colonne « produits ». **Test d'un produit** à un commit `C` de `main` : T1 (M-0.6) chaque chemin existe à `C` ; T2 (M-0.1) son compagnon `.sha256` est dans le même commit et `python -m controle_ia.scellement verifier` rend OK ; T3 (M-0.5, produit à verdict) pour chaque ligne de la table gelée du préenregistrement qui nomme « critère k de G0 », le verdict contient le même texte avec sa valeur, copiée et non lue (D-G0-8) ; T4 (M-0.2, préenregistrement) `exiger_prereg_scelle` rend l'empreinte. Un verdict négatif scellé passe le test. **Date d'usage** : le commit de départ d'une étape (un lancement ou un scellement), nommé au registre avant l'étape ; une lecture de deux familles compte deux étapes, chacune testée sur la ligne de sa famille.
- **†** : dépendance déduite (B l.146-152 : le harnais de T0.4 produit les épisodes et les activations de tout run ; B l.141 et l.214-217 : les bras séquentiels de G1 emploient les agrégateurs de T0.3), non écrite par une source.
- **Dépense facturée** : location d'instance de calcul ; appel de modèle payant (interface de programmation, session facturée). Ne sont pas des dépenses : le travail sur processeur local ; les poussées vers `controle-ia-travail` ; la veille ; la récupération de PDF et de métadonnées sans appel de modèle payant. Tout contact externe demeure un nœud (W38).
- **Classes.** **F** fermé. **K** conditionnel (colonne « produits » non vide). **R** rejeu, second jeu de preuve d'un critère. **I** indépendant. **H** décision de Lazar dans tous les cas. **« L'organisme »** = le pôle scientifique automatique (PC l.1) ; **« les organismes »** = ceux de T0.6, familles (i) et (ii).
- **Expérience « décisive »** : tout run, simulation comprise, qui (d1) cite dans son manifeste (R9) l'empreinte d'un préenregistrement scellé de G1 ou du papier C, ou (d2) lit un résultat de G1, de la porte GC ou des phases 1 à 3. **Règle des chiffres** : G1, papier C, papiers A et B ne citent comme chiffre de littérature que ceux de la table de T0.2 au statut confirmé ou corrigé (G l.364-365).

## 3. Produits (producteur ; lignes K fermées si le produit est absent au test — calculé par l'annexe A)
Chemins. P-T04 `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` ; P-T03 `diag/20261004-080257-t03/lecture.json` et `lecture.md` (lecture par le code gelé, G l.302 : T3 sans objet) ; P-NM `docs/notes/note-mathematique-lemme-theoreme-v3.md` ; P-EA `docs/etat-de-l-art/etat-de-l-art-verifie-niveau{1,2}-v1.md`, table des chiffres, contrôle de traçabilité, preuves « introuvable » (G l.356-360 ; T3 : la conclusion du contrôle) ; P-V6, P-L7, P-B4, P-G1, P-C, P-6a, P-6, P-7, P-8 : chemin fixé par le préenregistrement, à défaut nommé au registre avant l'étape ; P-V6 = verdict R13 scellé de T0.6, une ligne par famille (G l.196-199) ; P-L7 = lectures et verdict de T0.7 ; P-B4 = sorties et rapport de T0.8 ; P-6a = préenregistrement de l'étape 1 (P-015) ; P-EP = épisodes de T0.6 empreintés avec manifeste ; P-LST = liste d'identifiants lue par T0.7, empreintée (seule la liste est exigée de T0.7 par T0.8, G l.270-272) ; P-P4 = verdict de P4-instrument ; P-PIL = fichier réel du pilote de la couche 2 (PG l.7, l.38) ; P-ARR = règles d'arrêt P-14 et mode P-11 scellés (DP l.89-92).
| produit | critère | producteur | lignes K fermées si absent |
|---|---|---|---|
| P-T04 | 1 | — | W11, W12, W14, W15, W16, W17, W19, W23, W33, W41, W46, W47, W48 |
| P-V6 | 2 | W41 | W16, W19, W21 |
| P-L7 | 3 | W16 | W21 |
| P-B4 | 4 | W19 | W21 |
| P-T03 | 5 | — | W08, W20, W21, W28 |
| P-G1 | 6 | W21 | W05 |
| P-C | 7 | W25 | W06 |
| P-EA | 8 | W04 | W28, W29 |
| P-6a | — | W13 | W14 |
| P-6 | — | W13 | W41 |
| P-7 | — | W40 | W16, W17, W41 |
| P-8 | — | W18 | W19, W41 |
| P-EP | — | W41 | W16, W17, W19, W48 |
| P-LST | — | W16 | W19 |
| P-P4 | — | W12 | W16 |
| P-NM | — | W08 | W28 |
| P-PIL | — | W23 | W21 |
| P-ARR | — | W42 | W23 |

## 4. Table des travaux
`B` brief v2 ; `G` grille ; `D` `registres/decisions.md` (identifiants de ligne R-, N-) ; `E` `registres/etat.md` ; `T7` brouillon 4 de T0.7 ; `DP` ; `PG` ; `PC` ; `P40` ; `MSG216` message n° 216 ; `MO`, `TC`, `DV` (sous `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`). Jetons : `[REJEU]`, `[H]`, `d1`, `d2`, `préalable` (le script les lit). W40 à W49 : neuves ou issues d'un éclatement (W41 de W14).
| réf | travail | produits dont dépend le travail | sert | cl. | source |
|---|---|---|---|---|---|
| W01 | T0.1 : socle, registres, passations, poussées vers `controle-ia-travail`, rapport de porte, verdicts de porte, feuille de repli | — | — | I | B l.108-124 ; G l.409-411 |
| W02 | Veille hebdomadaire, lecture des pistes signalées (lecture web, aucun appel de modèle payant) | — | — | I | B l.346-348 |
| W03 | Collisionneur : rédaction des questions ; lancement = dépense facturée sur GO (GO-07 15 USD ; GO-15 30 USD) | — | — | I | D R-450, R-478 |
| W04 | T0.2 références : PDF, empreintes, statuts, table des chiffres, script sain et artefact, documents hors arXiv (PDF de Panin attendu de Lazar), références entrées depuis le niveau 2 | — | 8 | I | B l.126-135 ; G l.356-362, l.484-486 ; E l.41 |
| W05 | T0.2 : contrôle de traçabilité par sous-agent neuf, texte scellé de G1 | P-G1 | 8 | K | G l.358-359, l.485 ; E l.41 |
| W06 | T0.2 : contrôle de traçabilité par sous-agent neuf, texte scellé du papier C | P-C | 8 | K | G l.358-359, l.485 |
| W07 | T0.2 : rédaction du message de demande d'accès à FakeLab (l'envoi est W38) | — | — | I | B l.133 ; CLAUDE.md « contact externe » |
| W08 | T0.3 : note mathématique et figures tirées de la lecture scellée du run `20261004-080257-t03` | P-T03 | — | K | B l.144 ; G l.458 |
| W09 | T0.3 : tout nouveau run ou rejeu de simulation, toute modification du code des agrégateurs | — | 5 | R | G l.303-306 ; D R-025 ; [REJEU] |
| W10 | T0.4 : revalidation du harnais sur modèle réel, version nouvelle de préenregistrement | — | 1 | R | B l.146-152 ; G l.163-181 ; E l.43 ; [REJEU] |
| W11 | T0.5 : lecture et verdict du pilote 8B, vérité terrain, plan B de rubrique | P-T04† | — | K | B l.154-158 ; E l.44 |
| W12 | P4-instrument : contrôle positif de l'instrument (dépense facturée sur GO) | P-T04† | 3 | K | G l.236-237 ; D R-262, R-268 |
| W13 | T0.6 : rédaction, contre-lecture, scellement des préenregistrements (étape 1 de P-015 ; décisif) ; consignes ; données de distillation | — | 2 | I | B l.160-164 ; G l.196-201, l.473-476 ; E l.45 |
| W14 | T0.6 étape 1 : recherche de dose sur la boîte noire seule, tâches de réserve | P-T04†, P-6a | 2 | K | G l.473-474 ; B l.160-164 |
| W15 | T0.7 : apprentissage des sondes sur données génériques, choix sur validation générique, témoin lexical | P-T04† | 3 | K | B l.166-173 ; G l.231-233 ; T7 l.85 |
| W16 | T0.7 : lectures du critère 3 (T7-P1 à T7-P4) sur (i-a), (ii), témoin instruit ; une étape par famille lue | P-T04†, P-V6, P-7, P-P4, P-EP | 3 | K | G l.235-238, l.468 ; T7 l.65-68 |
| W17 | T0.7 : lectures T7-P5 à T7-P10 : descriptives (P5, P6, P9, P10) ou à réserve de validité (P7, P8), sans effet sur l'état du critère 3 | P-T04†, P-7, P-EP | — | K | T7 l.5, l.10, l.69-74, l.114, l.147-148 |
| W18 | T0.8 : invites, planchers, TRACE-lite, préenregistrement (traits fixés avant lecture) : rédaction et contre-lecture | — | 4 | I | B l.175-178 ; G l.261-268 ; E l.48 |
| W19 | T0.8 : run des bases sur les épisodes de T0.6, liste d'identifiants identique à celle de T0.7 | P-T04†, P-V6, P-LST, P-8, P-EP | 4 | K | G l.267, l.270-272, l.468 ; B l.175-178 |
| W20 | G1 : rédaction et contre-lecture du préenregistrement, sans scellement | P-T03† | 6 | K | B l.141, l.214-217 ; G l.482-483 ; PG l.1-7 |
| W21 | G1 : scellement du préenregistrement | P-V6, P-L7, P-B4, P-T03†, P-PIL | 6 | K | G l.468-469 ; B l.214-217 ; PG l.7, l.38 |
| W22 | Couche 2 : conception, code, banc synthétique, simulations de la garde δ (rapports v1 à v7), dimensionnement | — | — | I | PC l.99 ; PG l.1-7 ; D R-453, R-462 |
| W23 | Couche 2 : pilote réel sur seize tâches de réserve (tranche 0, puis pilote) ; devis P-27 = dépense facturée sur GO | P-T04†, P-ARR | — | K | DP l.1, l.89-92, l.128 |
| W24 | Couche 2 : fabrication de la banque avec sabotage à l'échelle, sentinelle GO-03 | — | — | F | DP l.43 ; PC l.99 ; d1 |
| W25 | Papier C : préenregistrement de HC1 à HC3 — rédaction, lecture de Panin, contre-lecture, scellement | — | 7 | I | B l.180-188 ; G l.339-343 ; E l.49 |
| W26 | Papier C : pilote (GO-2026-10-17-01) | — | — | F | E l.49 ; B l.180 ; d1 |
| W27 | Papier C : TC.1 à TC.6, porte GC | — | — | F | B l.252-284 ; d1 ; d2 |
| W28 | Papier A : cadre, énoncés, travaux connexes, hors résultats de la phase 1 | P-T03, P-NM, P-EA | — | K | B l.144, l.335-336 |
| W29 | Papier B : conception et rédaction hors expérience, dont H9 sous réserve d'antériorité | P-EA | — | K | B l.336 ; D N-035 |
| W30 | G1 : T1.2, lecture, porte G1 ; phase 1 : T1.1 à T1.7 | — | — | F | B l.207, l.214-219, l.241-246 ; d2 ; préalable |
| W31 | Phases 2 et 3, G2, G3, papier B : toute expérience | — | — | F | B l.288, l.310 ; d2 ; préalable |
| W32 | P3 : addendum 2 (N-025), lentilles sur les sondes de P3 : analyses de pièces déjà scellées | — | — | I | D N-025, R-438, R-450 ; G l.455 |
| W33 | P3b : nouveau run (N-028) | P-T04† | — | K | D R-262, N-028 |
| W34 | Pôle (l'organisme), course d'idéation : code, devis, essais hors ligne (v44 à v47) ; course réelle = dépense facturée sur GO | — | — | I | DV l.1-5 ; D R-449, R-451, R-455 |
| W35 | Pôle, tour (c) « outils clôturés » : code v46, essais hors ligne ; épreuve réelle courte (plafond 5 USD) = dépense facturée sur GO | — | — | I | TC l.143 ; D R-432, R-457, R-462, R-469 |
| W36 | Pôle, moissonneur v47 : code et essais hors ligne ; relais réel, épreuve courte, première moisson réelle = GO séparé ; jetons de la moisson = dépense facturée ; interrogation d'arXiv et d'OpenAlex sans identité = non facturée | — | — | I | MO l.116-118, l.156-160, l.178 ; D R-436, R-437, R-442, R-466, R-469, R-492 |
| W37 | Pôle, autres pièces : corpus primaire v5, orchestrateur, mesures de convergence, garde de sûreté, squelette H-E13 ; documents nommés demandés par Lazar hors phase : candidature EA Funds, entretien EA Funds, programme fusionné « pain axis », brainstorm « pain axis », README en anglais, proposition publique, copie expurgée, réponse « Justified assurance of friendliness » | — | — | I | D R-431, R-439, R-445, R-447, R-448 ; E l.85-95 |
| W38 | Soumission, publication, contact externe (envoi FakeLab, lettre au relecteur extérieur, revue de sécurité extérieure et sa ligne de 7 500 USD, courriel à OpenAlex), libération, dépôt public | — | — | H | B l.340-342 ; CLAUDE.md « nœuds de décision » ; D R-466, R-481, R-485 ; [H] |
| W40 | T0.7 : rédaction, contre-lecture, scellement du préenregistrement (brouillon 4, non scellé) | — | 3 | I | T7 l.1-3 ; G l.235, l.477-478 |
| W41 | T0.6 étape 2 : runs décisifs de (i) et (ii), contrôles croisés, dose-réponse ; lecture et verdict scellé par sous-agent neuf | P-T04†, P-6, P-7, P-8 | 2 | K | G l.196-201, l.474-480 ; B l.160-164 |
| W42 | Couche 2 : rédaction et scellement des règles d'arrêt P-14 et du mode tenu à l'écart P-11 | — | — | I | DP l.89, l.92 |
| W43 | Pôle, couche 3 légère (v48 : étage de tests de mort, exécuteur confiné sans réseau, préenregistrement court scellé, tranche exploratoire) : code et essais hors ligne ; essais réels = dépense facturée sur GO | — | — | I | D R-477 ; MSG216 pt 2 |
| W44 | Pôle, organisme hybride avec une intelligence artificielle scientifique existante : note de conception, vérification sur pièces primaires des deux candidats ; aucun code tiers avant revue ; exécution = dépense facturée sur GO | — | — | I | D R-480, R-488 ; MSG216 pt 3 |
| W45 | Revue de sécurité extérieure : cahier, lettre de confirmation, déclaration d'indépendance, accord de confidentialité (rédaction ; envoi et revue = W38) | — | — | I | D R-481, R-484, R-485 |
| W46 | Ressources publiques (P-040 A) : rejeu de NARCBench sur le 8B, activations 70B en plancher externe (T0.7, bras descriptif) ; dépense facturée sur devis et GO | P-T04† | — | K | P40 l.15, l.21 |
| W47 | Ressources publiques (P-040 B) : Liars' Bench et SHADE-Arena encodés en lecture seule (T0.8 comparateur externe ; T0.7 banque de traits) | P-T04† | — | K | P40 l.16 |
| W48 | Ressources publiques (P-040 C) : Llama Scope aux couches 7, 15, 23 sur les épisodes de T0.6, Goodfire couche 19 en contrôle | P-T04†, P-EP | — | K | P40 l.17, l.21-22 |
| W49 | Course 2 d'idéation (sept axes, boucle entre générations) : question-mère v1 à v3, recoupement, fusion, tranche exploratoire ; lancement réel = dépense facturée sur GO, après la v47 (relais réel, épreuve courte, moisson) | — | — | I | D R-461, R-467, R-469, R-471, R-472, R-493 |

## 5. Règle de lecture mécanique (option (b) verrouillée, R-470)
**L1** Une ligne F est fermée ; un travail absent de la table est F. **L2 (gel, R-765)** Une ligne non F dont « sert » contient un critère de G est fermée jusqu'au second verdict. **L3** Une ligne K non gelée est ouverte à une étape si tous ses produits passent leur test à la date d'usage de l'étape ; sinon fermée. **L4** Une ligne I non gelée est ouverte ; une ligne R non gelée est ouverte si « sert » contient un critère de A'. **L5** Dépense facturée : § 6.5. **L6** Une ligne H est décidée par Lazar. **L7** Union de toutes les fermetures ; aucun reclassement après V1 ; une pièce nouvelle (R12) appartient à la ligne de la pièce dont elle est la version. **L8** Les critères de V et de C n'ont ni gel, ni constat, ni droit de devis (§ 8 (3)).
Lecture inverse, recalculée ligne à ligne par l'annexe A (mode `verifier` : toute divergence arrête avec un code non nul). Par produit : § 3. Par critère (« devis » = ligne K ou I, ouverte, qui peut demander un devis si le critère est dans A') :
| critère | fermées si le critère est dans G (gel) | lignes R ouvertes si le critère est dans A' | droit de devis si le critère est dans A' |
|---|---|---|---|
| k:1 | W10 | W10 | aucune |
| k:2 | W13, W14, W41 | aucune | W13, W14, W41 |
| k:3 | W12, W15, W16, W40 | aucune | W12, W15, W16, W40 |
| k:4 | W18, W19 | aucune | W18, W19 |
| k:5 | W09 | W09 | aucune |
| k:6 | W20, W21 | aucune | W20, W21 |
| k:7 | W25 | aucune | W25 |
| k:8 | W04, W05, W06 | aucune | W04, W05, W06 |
Cas cumulés réalisables ensemble (un critère de A a son produit absent ; un critère de G a son produit présent ; `abs` = produits absents au test) :
| scénario | lignes K ou I fermées | lignes R ouvertes |
|---|---|---|
| sc:abs=P-V6,P-L7;G=;A=2,3 | W16, W19, W21 | aucune |
| sc:abs=P-7,P-8;G=;A=2 | W16, W17, W19, W41 | aucune |
| sc:abs=P-PIL;G=3;A=6 | W12, W15, W16, W21, W40 | aucune |
| sc:abs=P-L7,P-B4;G=2;A=3,4 | W13, W14, W21, W41 | aucune |
Les lignes F (W24, W26, W27, W30, W31) et H (W38) ne bougent jamais. Un produit présent n'est pas un critère tenu : le test T3 copie la valeur du verdict (§ 8 (5)).

## 6. Application
- **6.1 Qui applique.** Le sous-agent R13 qui prononce V1, dans le même verdict scellé : à la « Forme du verdict » (G l.409-411) s'ajoute la feuille de repli = sortie de la commande `feuille` de l'annexe A : A, G, V, C, produits absents au test à `C_lecture`, puis une ligne par réf. (ouverte ou fermée, motif L1 à L4, droit de devis). Le script est scellé avec la table avant V1 ; son empreinte figure dans la feuille. Le lecteur copie, ne classe rien. Avant le GO de Lazar, la session relance la commande sur le même commit ; un écart est un nœud. Chaque étape ultérieure d'une ligne K est calculée de même au commit de départ et consignée au registre avant l'étape.
- **6.2 Constat du 31 décembre 2026 (23:59 UTC, heure de l'avis).** Déclencheur : V1 n'est pas « franchie » et A n'est pas vide. Un sous-agent neuf R13 (grille § 1), sur un GO de Lazar, avec la grille scellée de G0 (empreinte citée), dont il applique au seul produit P_k les épreuves M-0.1, M-0.2, M-0.5, M-0.6. Pour chaque critère k de A, au commit `C_31` : tests T1 à T4 sur P_k ; verdict « produit et verdict présents » ou « absents » avec le test échoué. Il n'ouvre aucun critère de G, de V ou de C, ne prononce aucun état de critère, aucune valeur lue, aucun état de porte ; le fichier scellé ne contient aucune des chaînes « franchie », « non franchie », « non concluante », « tenu » (contrôle par recherche de chaîne). Effet de table : A' = A moins les critères « présents » (L4, § 6.5). Si A est vide : aucun constat, aucun GO demandé. Si le constat s'arrête (liste d'arrêt de G l.413-424) : A' = A et le second verdict n'est pas modifié.
- **6.3 V1 interrompu.** Ni verdict ni A, G, V, C : la table n'est pas appliquée (« un arrêt n'est pas une lecture », G l.424). Les lignes F demeurent fermées ; les autres ne sont ni ouvertes ni fermées par la table ; toute dépense facturée demeure soumise à la règle du dépôt (devis et GO) ; nœud pour Lazar. Heure dépassée sans lecture : lue au premier moment possible, retard en réserve (G l.421-422).
- **6.4 Pendant le report.** Pas de reclassement ; pas de second report ; le script est relancé à chaque étape d'une ligne K.
- **6.5 Dépenses facturées, règle unique.** (i) Une dépense couverte par un GO daté avant V1, dont l'objet, le plafond chiffré et l'échéance l'incluent, est permise : la table ne crée ni ne retire aucun GO. R-455 et R-478 consignent avec plafond chiffré GO-2026-10-29-08 (Claude, 50 USD), -09 (enveloppe 63), -13 (enveloppe 78), -14 (0,82 USD), -15 (30 USD) ; l'échéance de chacun est dans `registres/go.md` de `main` (non lu : celui de ce poste s'arrête au 22 octobre). Un GO sans plafond chiffré lu ne couvre aucune dépense du report : GO-11 et GO-16 (§ 8 (7)). (ii) Toute autre dépense facturée exige ensemble : sa ligne ouverte (L1 à L4) ; un critère de A' dans sa colonne « sert » ; un devis chiffré et un GO de Lazar postérieurs à V1. Sinon c'est un nœud : la clause ne la permet pas.
- **6.6 Clôture et arrêt au second verdict (31 janvier 2027, 23:59 UTC).** Second verdict R13, même grille (R-452 donne la date ; l'heure est celle de l'avis). « Franchie » : la table cesse de s'appliquer ; la phase 1 s'ouvre seulement sur GO. Sinon, phase 0 close « non franchie » : toute ligne cesse, sauf (i) W01 limitée au rapport de porte scellé, à la passation et à l'état (R14) ; (ii) l'arrêt par identifiant des instances en marche et sa consignation (R10) ; W38 (H) n'est ni ouverte ni fermée. « Cesser » = aucun nouveau run, aucune session de modèle, aucun scellement hors (i). Les pièces scellées demeurent ; toute reprise passe par une version nouvelle du programme (nœud). **Arrêt du second verdict** (liste d'arrêt, hors heure dépassée) : il n'y a pas de verdict ; défaut proposé (nœud D-TD-2, § 8 (4)) : « cesser » s'applique dès l'arrêt, jusqu'au mot de Lazar ; la levée de la cause reprend la même lecture, non un report.

## 7. Audit de symétrie R4 (recompté par l'annexe A)
- **Règle d'affectation, la même pour toute ligne.** A1 « produits » : seulement si une source citée écrit que le travail lit ou exige le produit (sinon †) ; A2 « sert » : seulement si une source écrit qu'il produit une preuve du critère ; A3 F seulement si le brief écrit un préalable (l.207, 288, 310) ou si d1 ou d2 s'applique ; K si « produits » non vide ; R pour un rejeu ; H pour une décision de Lazar ; I sinon ; A4 ni la date ni l'avancement n'entrent. Le script recalcule la classe de chaque ligne sans date, depuis les seules cellules et jetons : identité exigée.
- **Comptes** (v1 contre v3, lignes de la v1 reliées par une table de correspondance de l'annexe A ; « resserrement » : « sert » retiré, produit ajouté, classe plus fermée ; « assouplissement » : l'inverse) :
| compte | définition | valeur |
|---|---|---|
| aud:v1 | lignes de la v1 reliées à la v3 (W26 de la v1 : règle « absent = fermé ») | 25 |
| aud:resserrees | lignes de la v1 avec au moins un resserrement (la v2 en annonçait 12 ; la contre-lecture en comptait au moins 16) | 17 |
| aud:assouplies | lignes de la v1 avec au moins un assouplissement (la v2 en annonçait 3) | 4 |
| aud:deux | lignes à la fois resserrées et assouplies | 1 |
| aud:neutres | lignes de la v1 ni l'un ni l'autre | 5 |
| aud:sert-retires | couples (ligne de la v1, critère) retirés de « sert » | 13 |
| aud:sert-ajoutes | couples ajoutés à « sert » | 0 |
| aud:deductions | cellules « produits » portant † (la v2 en annonçait 2 cellules) | 15 |
| aud:lignes-deduites | lignes portant au moins un † | 15 |
| aud:neuves | lignes de la v3 sans ancêtre dans la v1 | 13 |
| aud:neuves-sert | lignes neuves dont « sert » est non vide (droit de devis accordé) | 1 |
| aud:neuves-ouvertes | lignes neuves de classe I ou R (ouvertes sans condition de produit ; la règle « absent = fermé » de la v1 les aurait fermées) | 6 |
| aud:L29 | lignes dont toutes les sources (R-, jetons DP PG PC MO TC DV MSG P40) sont du 29 octobre | 15 |
| aud:retrait-sc | scénarios testés (chaque produit absent seul, chaque critère seul dans G, seul dans A, plus les quatre cas cumulés) | 38 |
| aud:retrait-diff | scénarios où l'état d'une ligne retenue diffère entre la table complète et la table sans les lignes L29 et sans les produits qu'elles produisent | 2 |
| aud:retrait-lignes | lignes retenues qui diffèrent dans au moins un scénario | 1 |
- **Lecture du test de retrait.** La règle est locale à chaque ligne ; la différence vient des produits cités par une ligne retenue et produits par une ligne L29 : P-PIL, cité par W21 (source PG l.7, l.38, du 29 octobre). Sans ce produit, W21 garde ses quatre autres produits (G l.468-469).
- **Sens des changements de la v3 sur la v2** (comptés à la main, non par l'annexe) : resserrés — « sert 6 » retiré de W22 et W23 ; P-7 et P-8 ajoutés à l'étape 2 de T0.6 ; W14 éclatée en W14 et W41 ; † posés. Assouplis — W19 teste la liste P-LST au lieu de P-L7 (G l.270-272) ; W17 ne dépend plus de P-V6 (aucune source ne l'écrit pour des lectures descriptives ; T7 l.114 ne cite que les épisodes) ; W14 (étape 1) ne dépend plus que de P-6a ; dépense couverte par un GO antérieur (6.5 (i)) ; ligne W39 retirée (règle L1). Ajoutées — W40 donne un droit de devis pour le critère 3 (T7 l.1-3, G l.235), comme W13 pour 2 et W18 pour 4 ; W42 à W49 n'en donnent aucun.

## 8. Points ouverts (signalés, non masqués)
1. **Clause** (§ 0) : reconstruite sans la synthèse du collisionneur ni sa table commune ; texte de R-765 non lu (branche `main`).
2. **Lecture de R-765** : « gel » = L2 (aucune ligne ne produit une preuve nouvelle d'un critère de G) ; un critère de G étant inchangé au second verdict, avec G non vide le second verdict ne peut pas être « franchie » sans ouvrir une ligne gelée, ce qui est un nœud de Lazar.
3. **États V et C** : le mot de Lazar nomme « absent » et « négatif » ; la table applique la lettre (L8). À Lazar : V et C rangés avec A (constat, devis) ou avec G (gel).
4. **D-TD-2 (nœud)** : au second verdict, un arrêt sans verdict ; options (a) « cesser » dès l'arrêt, reprise de la même lecture à la levée (recommandée, confiance 0,6) ; (b) nouvelle lecture sans limite de nombre (écartée : second report de fait) ; (c) décision de Lazar à chaque arrêt. Aucun défaut appliqué.
5. **Produit présent ≠ critère tenu** : un verdict négatif scellé de T0.6 ouvre W16, W17, W19, W21 ; le gel de 2 ferme W13, W14, W41. W21 s'ouvre sans que 2, 3, 4 soient tenus (v2 § 8.4). Lazar peut exiger « verdict non négatif ».
6. **Dates** : scellement de la table non fixé (avis : clause intacte après le 1er novembre ; grille : 15 novembre) ; D-G0-1 à D-G0-9 non tranchés au 29 octobre (T3 suppose D-G0-8 « exiger »).
7. **GO** : l'avis écrit « seules » les tâches des critères non tenus ; des GO du 29 octobre existent (6.5 (i)) ; GO-11 sans plafond lu.
8. **Effet du constat** (A' contre A) : non écrit dans le mot de Lazar ; sans lui le constat ne change aucune ligne.
9. **Étape 1 de T0.6** : le résultat de la recherche de dose n'est pas un produit nommé ; W13 (préenregistrement décisif) n'en dépend pas dans la table.
10. **W26** (pilote du papier C) fermé par d1 ; variante inchangée (v2 § 8.6).

## Annexe A — script de vérification (fichier séparé)
`brouillons/canal-reprise-releve-v1/envois/table-dependance-criteres-G0-travaux-v3-annexe-A-verif-v1.py` (`sha256sum` : d22251d41e923ee764c1bf7aa313530ce5db4067b7f8d4eb8f19778e9efd5407 ; 100 lignes). Il lit ce fichier, la v1 et `registres/decisions.md` (dates des R-). `python <script> verifier <ce fichier> <v1> <decisions>` : contrôles de structure (classe recalculée sans date, un produit par critère, aucun cycle), puis recalcul de chaque ligne dérivée (§ 3, § 5, § 7) et comparaison une à une ; `artefact` : change une cellule et exige l'échec de `verifier` ; `feuille ... "A=2,3;G=;V=;C=;abs=P-V6,P-L7"` : feuille de repli (§ 6.1). Essais R5 faits le 2026-10-29 sur le présent fichier : `verifier` → « OK 46 lignes dérivées vérifiées une à une, 48 lignes de travaux contrôlées » ; `artefact` → « artefact détecté » ; `feuille` avec les arguments ci-dessus : 37 lignes ouvertes, 10 fermées (W16, W19, W21 par produit absent ; W24, W26, W27, W30, W31 par L1 ; W09, W10 par L4 hors A), W38 à Lazar ; droits de devis W12, W13, W14, W15, W40, W41. Essai d'altération : une copie dont la ligne P-V6 du § 3 est changée fait échouer `verifier` (AssertionError).
