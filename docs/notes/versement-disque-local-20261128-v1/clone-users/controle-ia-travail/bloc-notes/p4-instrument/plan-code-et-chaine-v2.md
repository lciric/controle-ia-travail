# P4-instrument — plan du code, de la chaîne de lancement et devis — v2

Session 14, 2026-10-20 vers 13:49 UTC. Compagnon du brouillon 4 du préenregistrement
(`P4-instrument-v1-brouillon4.md`, même dossier), écrit pour corriger VP3-10 (contre-lecture 2 : le plan v1, resté au
brouillon 1, contredisait le brouillon 3). Le v1 (`plan-code-et-chaine-v1.md`, rédacteur neuf) reste tel quel (R12).
**Le texte du préenregistrement prime sur ce plan** ; en cas d'écart, le texte fait foi et ce plan se corrige. Rien
n'est écrit dans le dépôt par ce plan.

## 1. En bref

- **Code** : un module neuf, hors de l'arbre gelé, qui importe le code gelé de P3 sans le modifier. Aucune génération,
  aucun entraînement : 300 passes d'épisode (cinq bras × 60) et 529 passes courtes de validation.
- **Chaîne** : celle de P3, copiée sous des noms neufs (R12), avec des bornes plus courtes et les formes exactes de
  dépense du brouillon 4 (GO cité GO-2026-10-20-07).
- **Devis** : environ 0,85 à 1,15 heure de carte A100, soit ≈ 1,5 à 2,3 USD tout compris (attendu) ; borne de l'étape
  5,41 USD ; crédit exigé à la création 4,47 USD au prix de P3 (5,10 USD au prix plafond).

## 2. Ce qui se réutilise de P3 tel quel (aucune ligne modifiée)

Inchangé depuis le v1 (section 2), avec deux lignes de plus :

| besoin de P4 | code gelé (fichier, lignes) |
|---|---|
| agrégation par le maximum sur les jetons | `harnais/sondes.py` l. 75-76 |
| biais des directions du plancher | `sondes/evaluation.py` l. 79 (w ~ N(0, Σ)) et l. 81 (biais −w·μ) |

## 3. Ce qui est neuf

### 3.1 Emplacement

`docs/procedures/P4-instrument-v1/`, hors de l'arbre gelé (retenu ; question 2 du v1). Garde propre au module :
`exiger_module_cite` (lignes « Module de P4 : `chemin` : `empreinte` » du texte), au run, à la lecture et aux contrôles
avant dépense. L'arbre gelé doit égaler celui de `7a54d43`.

### 3.2 Fichiers

| fichier | rôle |
|---|---|
| `mesures_conception_p4_v1.py` | processeur, vrai tokeniseur : MC-1 (longueurs de D, H, des six candidates B et des trois candidates B′, seules et dans le gabarit, dix pas × 60 tâches ; choix de B et de B′ par la règle du texte) ; MC-2 (empreintes de trajectoire du bras I contre P3) ; MC-3 (longueurs par action, présence du jeton de fin par `jetons − jetons_notes`) ; sortie brute scellée sous `docs/notes/P4-mesures-v1/` ; ne lit aucun score |
| `instrument_p4_v1.py` | côté instance : sources de P3 (empreintes, graines par `generateur`) ; M5 reconstruite ; épisodes des bras I, D, H, B, B′ ; `exiger_bras_alignes` (B et D, B′ et H de même longueur à chaque pas) ; garde d'identité (niveau 1 ; niveau 2 avec (c) à 403 sondes légères sur 424 au moins) ; épreuve de la tolérance (c) : artefact (i) par insertion de l'identifiant 220 après le `<|end_header_id|>` et l'identifiant 271 du premier message de l'utilisateur, garde « un identifiant de plus, à cette place, à chaque pas », artefact (ii) par échange des actions des pas 1 et 2 ; notation ; écritures scellées ; arrêt consigné avec résumé |
| `lecture_p4_v1.py` | processeur : gardes du mode décisif (entropie, module, run source, configuration ; verdict complété de P3 au chemin v2, sceau égal, ligne « **Verdict complété de P3 scellé** » avec l'empreinte) ; M5 ; C1 (« au-dessus » sur le quantile 0,95, « au-dessous » sur le quantile 0,05) ; M6a (séparation repliée par tirage, plancher des séparations repliées) ; M6b (`difference_aire_separation`) ; descriptives (concordance appariée et rang avec ex aequo pour moitié ; C1 au pas 0 ; Δ net ; part des directions à \|aire − 0,5\| > 0,15) ; audit R4 ; `issue_p4` (lignes L1 à L11, réserves du Seuil) ; refus d'une garde du mode décisif écrit en L1 avec son motif ; attente du verdict complété : report, rien d'écrit |
| `test_instrument_p4_v1.py`, `test_lecture_p4_v1.py`, `test_gardes_p4_v1.py` | tests (section 3.4) |
| `prereg/P4-instrument-config-v1.json` (+ sceau) | configuration (section 3.3) |
| scripts de la chaîne | section 4 |

### 3.3 Configuration (clés)

Celles du v1 (section 3.3), avec ces changements :

- `phrases` : D, H, la liste ordonnée des six candidates B, la liste ordonnée des trois candidates B′ (« urban »,
  « indoor », « outdoor ») ;
- `quantile_plancher` (0,95) et `quantile_plancher_bas` (0,05) ;
- `plancher_haut` (0,80), `plancher_haut_bas` (0,20), `mediane_plancher` ([0,45 ; 0,55]) ;
- `seuil_etalement` (0,15 : part des directions à \|aire − 0,5\| au-dessus) ;
- `sondes_legeres_min` (403) et `n_sondes_legeres` (424) ;
- `identifiant_espace` (220), `identifiant_deux_sauts` (271), avec l'empreinte du tokeniseur (`79e3e522…`) ;
- `go_cite` (GO-2026-10-20-07), `prefixe_plafond_par_lancement` (« 10 USD par lancement »), `borne_etape_usd` (5,41).

### 3.4 Tests (R5 : chaque garde a un cas sain et un artefact)

Ceux du v1 (section 3.4), avec ces changements et ajouts :

- table de lecture : chaque ligne L1 à L11 atteinte par une entrée construite ; L1 par un refus de garde du mode
  décisif ; L3 par une lecture de M5 en échec ; réserve « plancher haut » avec son texte exact en L6, L7, L8 et L9, absente
  en L1 à L5 ;
- « au-dessous » sur le quantile 0,05 d'un plancher synthétique asymétrique, où il diffère de 1 − quantile 0,95, aux deux
  bords ; critère miroir du plancher haut (quantile 0,05 égal à 0,20, et juste au-dessous) ;
- critère (c) : 403 sondes légères dans la tolérance (garde) contre 402 (exclut) ; une sonde principale hors tolérance
  (exclut) ;
- épreuve (i) : cas sain, un identifiant de plus à chaque pas ; artefact, espace mis dans le texte d'un gabarit qui rogne,
  aucun décalage, épreuve « non éprouvée », niveau 2 désactivé ;
- B′ : tirée de la liste en « a » au lieu de la liste en « an » (arrêt) ; B′ plus long d'un jeton que H (arrêt) ;
  adjectifs de B et de B′ passés à `exiger_concept_sans_affect` (artefact : un adjectif d'affect, refus) ;
- verdict complété de P3 : absent, non scellé, sans ligne, ligne sans la forme exacte, ou empreinte différente du sceau
  (refus) ;
- rang de la sonde avec des ex aequo ; séparation repliée par tirage (M6a) contre un calcul direct ;
- GO : GO cité autre que GO-2026-10-20-07 ; colonne « plafond » sans le préfixe ; date après l'échéance de la colonne ;
  révocation par ligne de GO ou par ligne R-… (chaque forme) ; garde de calcul gelée rejouée sur un registre mal formé
  (refus).

Le nombre exact devient « Tests attendus » au candidat (908 + tests de P4).

## 4. Chaîne de lancement (adaptée de `docs/procedures/P3-premier-test-v2/`)

Comme le v1 (section 4), avec ces changements :

| script de P4 | changements par rapport au v1 |
|---|---|
| `verifications_p4_v1.py` | GO cité : GO-2026-10-20-07 seul ; colonne « plafond » qui commence par « 10 USD par lancement » ; échéance lue dans la colonne du GO cité ; révocation : ligne de GO de type « révocation » qui nomme GO-2026-10-04-08, GO-2026-10-20-06, GO-2026-10-20-07, R-262 ou R-269, ou ligne R-… qui commence par « **Révocation de R-262** » ou « **Révocation de R-269** » ; ligne d'accord « **Accord de Lazar pour le lancement de P4-instrument** » du jour, qui cite GO-2026-10-20-07 ou un message de Lazar du jour |
| `controles_avant_depense_p4_v1.sh` | MC-1 à MC-3 rejouées (choix de B et de B′ identiques à ceux du texte) ; suite complète des tests ; garde de calcul gelée rejouée sur la commande de création (jamais contournée) |
| `lancer_p4_v1.sh` | `GO_ID=GO-2026-10-20-07` dans la commande de création ; le reste comme le v1 |
| `p4_instance_v1.sh` | suite complète des tests sur l'instance (économie refusée, VP3-12) ; poussée des sorties des cinq bras |

**Ordre** (texte, « Chaîne de lancement ») : brouillon 4 ; ce plan ; mesures de conception ; candidat ; module et tests
alignés sur le candidat ; contre-lecture 3 par un sous-agent neuf (corrections du brouillon 4 et fidélité du code au
texte) ; répétition jouet ; épingles ; bancs ; répétition finale ; scellement S ; accord du jour consigné ; lanceur ;
contrôle à cinq minutes ; surveillance ; récupération ; destruction de l'instance par son identifiant ; attente du
verdict complété de P3 ; lecture ; verdict R13 ; GO de Lazar sur le verdict. Aucun sous-agent ne tourne pendant l'appel
du lanceur (R-234).

## 5. Devis

Sources : v1, section 5.1 (inchangées).

| poste | durée estimée |
|---|---|
| démarrage, clonage, poussée initiale, installation | ≈ 2,5 min |
| suite complète des tests (908 + tests de P4) | ≈ 29 à 33 min |
| chargement du modèle et format | ≈ 2 à 3 min |
| M5 : 529 passes courtes et notation | ≈ 1 min |
| 5 bras × 60 passes d'épisode | ≈ 2,5 min |
| notation de 3 000 actions par 424 sondes | ≈ 8 à 10 min |
| épreuve de la tolérance (c) : deux passes | < 1 min |
| écritures, sceaux, poussées, arrêt | ≈ 2 min |
| **total** | **≈ 48 à 55 min ; 0,85 à 1,15 h avec marge** |

| poste | attendu | borne de l'étape |
|---|---|---|
| carte | 0,85 à 1,15 h × 1,0889 = 0,93 à 1,25 USD | 9 600 s × 1,30 = 3,47 USD |
| arrêt | — | 10 min × 1,30 = 0,22 USD |
| téléchargement | ≈ 20 Go × 0,026 = 0,52 USD | 20 Go × 0,05 = 1,00 USD |
| disque arrêté jusqu'à la destruction | ≈ 0,05 USD (1 à 2 h) | 24 h × 0,03 = 0,72 USD |
| **total** | **≈ 1,5 à 1,9 USD** (≈ 2,3 USD au prix plafond) | **5,41 USD** |

- **Crédit exigé à la création** : 3 h × (prix + autres projets en marche) + 1,2 USD = 4,47 USD à 1,0889 ; 5,10 USD à
  1,30. Crédit relu 11,79 USD le 2026-10-20 à 06:07 UTC (`registres/depenses.md`), moins le disque de 56799469 jusqu'à
  sa destruction ; à relire avant l'accord.
- **Plafonds** : par lancement, 10 USD (colonne « plafond » de GO-2026-10-20-07) ; phase 0, 150 USD (GO-2026-10-04-08,
  prolongé jusqu'au 2026-11-30 par GO-2026-10-20-06 ; cumul ≈ 67 USD plus les disques selon R-262), vérifié à l'accord.
- **Économie refusée** : la suite complète tourne sur l'instance (VP3-12).

## 6. Calendrier indicatif

- 20-21 octobre : brouillon 4, ce plan, mesures de conception, candidat.
- 21-23 octobre : module aligné, contre-lecture 3, répétition jouet, bancs, répétition finale.
- Puis : scellement S, accord, lancement (≈ 1 heure), récupération, destruction de l'instance.
- Après le verdict complété de P3 (addendum 2) : lecture, verdict R13, GO de Lazar.

## 7. Questions du v1 : réponses

| question du v1 | réponse |
|---|---|
| 1. Entropie | consignée (R-268) ; citée dans le texte |
| 2. Emplacement | hors de l'arbre gelé (retenu) |
| 3. Tolérances | seuils de séance gardés ; MC-2 dit avant le scellement combien d'épisodes passent le niveau 1 ; seuil (c) à 403 sur 424 (VP3-08) |
| 4. Variante A5 | exclue, écrite au texte (Pare-feu) |
| 5. Phrases B | liste validée par le contre-lecteur R2 du brouillon 1 (RP-03) ; liste de B′ validée par le vérificateur de la contre-lecture 2 (VP3-07) |
| 6. Ordre des lancements | P4 d'abord, séparé de P3b (texte, Pare-feu ; R-262) ; pas d'instance commune |
| 7. Délégation | étendue jusqu'au 2026-11-30, indépendante du mandat (R-269, GO-2026-10-20-07) ; la ligne d'accord reste exigée |
| 8. Effet d'un échec | nœud de Lazar (branche (C) de la note) ; ce que devient P3b est sa décision (texte, Pare-feu) |
| 9. Instance de P4 | détruite après la récupération vérifiée |
| 10. Lecture conditionnée | garde dans le code, forme exacte de la ligne du registre (VP3-09) |
| 11. Mesures de conception | admises au titre de R1, écrit au texte |
| 12. Filtre d'offre | gardé égal à celui de P3 |
