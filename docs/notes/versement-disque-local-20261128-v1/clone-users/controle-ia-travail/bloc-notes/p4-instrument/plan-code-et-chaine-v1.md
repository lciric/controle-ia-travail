# P4-instrument — plan du code, de la chaîne de lancement et devis — v1

Rédacteur neuf, 2026-10-20. Compagnon du brouillon 1 du préenregistrement
(`P4-instrument-v1-brouillon1.md`, même dossier). Dépôt lu en lecture seule au commit `aa0ece4` ; à ce commit, `src/`,
`tests/` et `scripts/` sont égaux à ceux du commit cité par P3 (`7a54d43`). Rien n'est écrit dans le dépôt.

## 1. En bref

- **Code** : un module neuf de quelques centaines de lignes, hors de l'arbre gelé, qui importe le code gelé de P3 sans
  le modifier. Aucune génération, aucun entraînement : 240 passes d'épisode et 529 passes courtes.
- **Chaîne** : celle de P3, copiée sous des noms neufs (R12), avec des bornes plus courtes.
- **Devis** : environ 0,8 à 1,1 heure de carte A100, soit ≈ 1,5 à 2,2 USD tout compris (attendu) ; borne de l'étape
  5,41 USD ; crédit exigé à la création 4,47 USD au prix de P3 (5,10 USD au prix plafond).

## 2. Ce qui se réutilise de P3 tel quel (aucune ligne modifiée)

| besoin de P4 | code gelé (fichier, lignes) |
|---|---|
| phrases de persona D et H | `premier_test_ia/donnees.py` l. 26-27 (`CONSIGNE_HONNETE`, `CONSIGNE_MALHONNETE`) |
| faits, enjeux, tirage, découpage (M5) | `premier_test_ia/donnees.py` l. 38-50, 53-56, 59-69, 72-80, 83-95 |
| empans génériques (M5) | `premier_test_ia/entrainement.py` l. 39-48 (`preparer_tromperie`), 51-53 (`preparer_enjeux`) ; `empans.py` l. 23-61 |
| extraction (M5) | `premier_test_ia/entrainement.py` l. 62-74 (`extraire`) |
| sondes figées légères | `premier_test_ia/figees.py` l. 56-81 (`lire_sondes`, empreinte de chaque sonde contrôlée) |
| notation, scores par jeton, garde d'identité de la notation | `premier_test_ia/notation.py` (`Notation.noter`, `par_jeton`, l. 131-141 `agreger_par_jeton`, l. 144-160 `exiger_identite`) ; `run.py` l. 218-223 (`exiger_par_jeton`) |
| environnement honnête et place des indications | `premier_test_ia/conditions.py` l. 74-82 (`environnement`) ; `environnements/propositions.py` l. 215-269 |
| bornes des champs (garde de niveau 2) | `premier_test_ia/conditions.py` l. 116-143 (`bornes_champs`) |
| transcription, empreinte de trajectoire | `harnais/episode.py` l. 30-60 (`Action`, `Transcription`, `Episode`), l. 211-217 et 250-255 (construction des contextes), l. 366-375 (`empreinte_episode`) ; `harnais/formats.py` l. 22-23, 88-103 |
| passe unique | `harnais/activations.py` l. 99-110 (`passe_unique`) |
| modèle, format, déterminisme | `environnements/lancer_pilote_a.py` (`charger_modele_et_format`) ; `premier_test_ia/run.py` l. 207-215 (`controler_format_agent`), l. 398-400 (`regler_determinisme`) ; `harnais/validation_reelle.py` l. 364-369 (`noyau`) |
| tâches, guide | `environnements/pilote_a.py` l. 47-64 (`charger_taches`, `tache_de`) ; `environnements/invites.py` l. 34 (`charger_invite`) |
| statistiques | `sondes/evaluation.py` l. 26-37 (`aire_sous_courbe`), l. 40-63 (`intervalle_blocs`) ; `premier_test_ia/statistiques.py` l. 110-125 (`detection_etiquettes`), l. 128-130 (`separation`) ; `sondes/temoins.py` l. 182-206 (`difference_aires_appariee`, modèle de la fonction neuve) |
| garde contre l'affect | `sondes/temoins.py` l. 38-54 (`exiger_concept_sans_affect`) |
| manifeste, graines, résultats | `manifeste.py` (`creer_manifeste`, `generateur`, `ecrire_resultat`, `lire_manifeste`) ; `harnais/run_harnais_factice.py` l. 58-59 (`graine_entiere`) |
| gardes du mode décisif | `harnais/validation_reelle.py` l. 214-227 (`exiger_code_cite`), l. 244-248 (`exiger_code_importe_sous`), `ENTROPIE_CITEE` l. 75, `exiger_memoire_vive` ; `prereg.py` l. 70-76 (`exiger_prereg_scelle`) |
| progression sans texte | `premier_test_ia/run.py` l. 85-88 (`progres`) |

Données de P3 réutilisées : voir la table « Données lues » du brouillon (empreintes). Les deux sondes principales et
leurs 2 × 200 directions de plancher sont dans le fichier léger (vérifié : 424 sondes ; `tromperie-difference_moyennes-c15`
et `enjeux-lineaire-c15`, linéaires, couche 15, maximum ; 200 directions chacune). Le fichier complet et l'instance
56799469 ne servent pas.

## 3. Ce qui est neuf

### 3.1 Emplacement

- **Recommandation** : `docs/procedures/P4-instrument-v1/`, hors de l'arbre gelé (`CHEMINS_GELES`,
  `harnais/validation_reelle.py` l. 71-73), comme les deux addendums de P3. Raison : tout fichier ajouté sous `src/`,
  `tests/` ou `scripts/` ferait refuser par `exiger_code_cite` toute relecture décisive de P3 au commit cité, et
  l'addendum 2 (N-025) comme P3b (N-028) sont en cours. Le module importe le code gelé sans le modifier.
- **Garde propre au module** : le texte cite l'empreinte de chaque fichier du module (« Module de P4 : `chemin` :
  `empreinte` »), relue par le run, par la lecture et par les contrôles avant dépense (garde neuve
  `exiger_module_cite`, cas sain et artefact). `exiger_code_cite` garde l'arbre gelé ; P4 exige en plus que cet arbre égale
  celui de `7a54d43` (instrument figé).
- **Autre voie** (question) : sous `src/controle_ia/p4_instrument/` après la clôture de P3 (verdict complété et GO).

### 3.2 Fichiers

| fichier | rôle |
|---|---|
| `mesures_conception_p4_v1.py` | processeur, vrai tokeniseur : MC-1 (longueurs de D, H, des six candidates B, seules et dans le gabarit, dix pas × 60 tâches ; choix de B), MC-2 (empreintes de trajectoire du bras I contre P3), MC-3 (longueurs par action) ; sortie brute scellée sous `docs/notes/P4-mesures-v1/` ; ne lit aucun score |
| `instrument_p4_v1.py` | côté instance : `charger_sources_p3` (empreintes, graines de P3 par `generateur`) ; `reconstruire_validation` (M5) ; `reconstruire_episode(tache, textes, jetons_par_action, phrase=None)` (bras I, D, H, B ; rend l'épisode et les empans) ; `exiger_bras_alignes` ; `garde_identite` (niveaux 1 et 2, motifs d'exclusion) ; `noter_bras` ; `executer` (manifeste, ordre du plan, écritures scellées, arrêt consigné) ; `_main` |
| `lecture_p4_v1.py` | processeur : `exiger_lecture_sous_prereg_p4` (entropie, module, run source, configuration, verdict complété de P3 exigé) ; `lire_m5`, `lire_c1`, `lire_m6` (par `detection_etiquettes`) ; `difference_aire_separation` (M6b) ; `concordance_appariee` ; `audit_r4` ; `issue_p4` (lignes L1 à L9, réserves) ; `analyser` ; `_main` |
| `test_instrument_p4_v1.py`, `test_lecture_p4_v1.py`, `test_gardes_p4_v1.py` | tests (section 3.4) |
| `prereg/P4-instrument-config-v1.json` (+ sceau) | configuration (section 3.3) |
| scripts de la chaîne | section 4 |

### 3.3 Configuration proposée (clés)

`agent` (copie de celle de P3 : modèle, révision `0e9e39f249a16976918f6564b8830bc894c89659`, date du gabarit, texte
attendu dans l'ouverture), `mode` (`reel` ou `jouet`), `noyau_attention` (`defaut`), `couches` ([7, 15, 23]), `N` (1),
`T` (10), `fils` (1), `duree_max_s` (3 600), `memoire_vive_min_go` (64), `run_source` (`20261019-230011-p3-reel`),
`empreintes_sources` (table du brouillon), `phrases` (D, H, liste ordonnée des six candidates B), `sondes_principales`,
`n_tirages` (2 000), `niveau` (0,95), `quantile_plancher` (0,95), `plancher_haut` (0,80), `mediane_plancher`
([0,45 ; 0,55]), `r4_plancher` (0,90), `r4_aire` ([0,05 ; 0,95]), `tolerance_identite_scores` (0,05),
`part_exclusion_max` (0,10), `tolerance_aires_validation` (0,005), `tolerance_identite_notation` (1e-6),
`tolerance_par_jeton` (1e-9), `effectifs_validation` ({tromperie : 120, enjeux : 409}), `faits_exclus_attendus` (7).

### 3.4 Tests (R5 : chaque garde a un cas sain et un artefact)

Sur le modèle jouet et le tokeniseur par caractères au format de dialogue (`tokeniseur_caracteres_chat`), à partir d'un
run jouet de P3 joué dans un dossier temporaire (même chaîne que les tests de P3) :

- reconstruction : bras I d'un run jouet de P3 → empreintes de trajectoire égales (cas sain) ; un caractère changé dans
  un texte, un jeton de fin changé → empreinte différente, passage au niveau 2 (artefacts) ;
- niveau 2 : longueur, bornes et scores égaux → gardée ; lignes de scores permutées, empan décalé d'un jeton, texte d'une
  autre action → exclue, motif écrit ; 7 exclusions sur 60 actions jouet (> 10 %) → C1 et M6 non calculés ;
- alignement : phrase absente, doublée, déplacée après « Your action: » ; identifiants d'action différents entre bras ;
  jeton de la phrase dans l'empan ; B plus long d'un jeton → arrêt ;
- M5 : graine de découpage altérée (état de contrôle) → arrêt ; effectifs, faits exclus, lignes d'enjeux différents →
  arrêt ; aire de validation altérée de 0,01 dans un `sondes-figees.json` jouet → arrêt ; cas sain → aires égales ;
- gardes de mode décisif : entropie absente ou autre ; module à une autre empreinte ; run source non décisif ; verdict
  complété de P3 absent ou non scellé → refus ;
- statistiques : `difference_aire_separation` contre un calcul direct (mêmes tirages) ; signe de la séparation
  (aire B < 0,5) ; concordance appariée contre un calcul à la main ; tirages dégénérés au-delà de 1 % → échec écrit ;
- table de lecture : chaque ligne L1 à L9 atteinte par une entrée construite ; réserves (R4, enjeux, reproductibilité,
  réserve héritée) ; aucune ligne avant l'audit ;
- règles : aucune moyenne ni médiane sur les jetons (recherche dans le module et artefact qui en injecte une) ; adjectif
  d'affect refusé (`exiger_concept_sans_affect`) ; aucun texte d'action dans les sorties (fenêtres de 48 caractères, comme
  la récupération de P3) ; chaînes de 200 caractères au plus dans les résultats ;
- bout en bout jouet : run P4 jouet puis lecture jouet, sorties scellées, rattachées au manifeste.

Ordre de grandeur : 60 à 80 tests. Le nombre exact devient « Tests attendus » au candidat (908 + tests de P4).

## 4. Chaîne de lancement (adaptée de `docs/procedures/P3-premier-test-v2/`)

Copies sous `docs/procedures/P4-instrument-v1/`, noms neufs (R12), chacune avec son sceau et son banc.

| script de P3 | script de P4 | changements |
|---|---|---|
| `verifications_p3_v1.py` | `verifications_p4_v1.py` | ligne d'accord « **Accord de Lazar pour le lancement de P4-instrument** » ; GO accepté : GO-2026-10-04-08 seul ; révocation : ligne de GO de type « révocation » nommant GO-2026-10-04-08 ou R-262, ou ligne R-… commençant par « **Révocation de R-262** » ; chemins du texte de P4 |
| `controles_avant_depense_p3_v1.sh` | `controles_avant_depense_p4_v1.sh` | arbre gelé égal à `7a54d43` ; empreintes du module de P4 ; empreintes des données de P3 ; MC-1 à MC-3 rejouées au vrai tokeniseur (choix de B identique, parts d'identité identiques à celles du texte) ; suite des tests (dépôt et module de P4) ; plus aucun contrôle des consignes de P3 ; GO, accord, révocation, instances |
| `lancer_p3_v1.sh` | `lancer_p4_v1.sh` | `HEURES_CREDIT=3.0` ; `PLAFOND_SURVEILLANCE_S=9600` ; même filtre d'offre (`PRIX_MAX=1.30`, `COEURS_MIN=16`, `MEMOIRE_VIVE_MIN_MO=128000`, `TELECHARGEMENT_MAX=0.05`, `STOCKAGE_MAX=0.03`) ; `ARRETEES_TOLEREES` : 56799469 tant qu'elle existe ; `BRANCHE=calcul/p4-reel-v1` ; `ETIQUETTE=p4-v1` ; amorce de P4 |
| `scripts/amorce_instance_p3.sh` | `amorce_instance_p4_v1.sh` | plafond 150 minutes ; script de P4 ; données poussées : celles de P4 |
| `scripts/p3_instance.sh` | `p4_instance_v1.sh` | étude « p4 » ; lecture précoce des citations du texte de P4 ; tests `python -m pytest -q tests docs/procedures/P4-instrument-v1` ; run `python docs/procedures/P4-instrument-v1/instrument_p4_v1.py --config … --prereg …` ; délai externe 90 minutes ; poussée forcée de `scores-p4.npz`, `jetons-principales-p4.npz`, `validation-p4.npz` et de leurs sceaux ; aucun texte |
| `surveiller_p3_v1.sh` | `surveiller_p4_v1.sh` | création + 9 600 s, puis arrêt par l'identifiant (R10) |
| `controle_cinq_minutes_p3_v1.sh` | `controle_cinq_minutes_p4_v1.sh` | noms et chemins |
| `recuperation_p3_v1.sh` | `recuperation_p4_v1.sh` | fichiers attendus de P4 ; sceaux ; aucun texte d'action de P3 dans les fichiers poussés par P4 (fenêtres de 48 caractères des 600 textes honnêtes) ; chaînes de 200 caractères au plus ; puis destruction de l'instance par son identifiant, après la vérification (24 heures au plus) |
| `sceller_p3_v1.sh` | `sceller_p4_v1.sh` | commit S : texte, configuration et sceaux seulement ; relit les journaux de preuve et compare chaque script éprouvé à sa copie versée |
| `repetition_jouet_p3_v1.sh`, `repetition_finale_p3_v1.sh` | `…_p4_v1.sh` | jouet : run P3 jouet, puis P4 jouet, puis lecture jouet |
| `essais_*_p3_v1.sh` (bancs) | `essais_*_p4_v1.sh` | cas sain et artefacts de chaque contrôle neuf |

**Ordre** : contre-lecture R2 du brouillon ; mesures de conception ; candidat (B, parts d'identité, tests attendus,
configuration) ; module et tests ; contre-lecture du code par un sous-agent neuf ; relecture courte du traitement ;
répétition jouet ; épingles des contrôles ; bancs ; répétition finale à blanc ; scellement S ; accord du jour consigné
(R-217, ou R-185 hors mandat) ; lanceur (contrôles avant dépense rejoués sur S) ; contrôle à cinq minutes ; surveillance
; récupération ; destruction de l'instance ; attente du verdict complété de P3 (addendum 2) ; lecture ; verdict R13 par
des sous-agents neufs ; GO de Lazar sur le verdict. Aucun sous-agent ne tourne pendant l'appel du lanceur (R-234).

## 5. Devis

### 5.1 Sources

| grandeur | valeur | source |
|---|---|---|
| prix de l'offre de P3 | 1,0889 USD de l'heure | `registres/depenses.md` l. 87 (`0137a81c…`), offre 46608730 |
| prix plafond | 1,30 USD de l'heure | `lancer_p3_v1.sh` (`PRIX_MAX`) ; P3 l. 352 |
| téléchargement | 0,026 USD par Go à l'offre de P3 ; borne 0,05 | `depenses.md` l. 87 ; P3 l. 353-358 |
| volume téléchargé | ≈ 20 Go (estimation) | P3 l. 371 |
| disque de l'instance arrêtée | 0,022 USD de l'heure (borne 0,03) | `depenses.md` l. 87 |
| durée totale de P3 | 3,64 h, ≈ 3,96 USD | `depenses.md` l. 88 |
| démarrage → amorce | 33 s (22:28:53 → 22:29:26) | `depenses.md` l. 87 ; journal de P3 l. 1 |
| mise en place et tests | 30 min 45 s (22:29:26 → 23:00:11), dont 908 tests en 1 724,83 s | `traces/p3-20261020-020648-jcOO/journal.txt` (`72a4e15e…`) l. 1 et 7 |
| chargement du modèle et format | 2 min 11 s (23:00:11 → 23:02:22) | même journal, l. 9-10 |
| extraction de 2 598 exemples courts | 83,8 s (≈ 32 ms chacun) | même journal (`etape=extraction`) |
| passe unique de 240 épisodes | 108,4 s | `diag/20261019-230011-p3-reel/episodes-p3.json` (`1a96cbf8…`), `descriptifs.passe_unique_s` |
| notation et reste, 2 400 actions | ≈ 444,6 s (9 644,6 − 9 091,6 − 108,4) | même fichier, `descriptifs` |
| fin → arrêt | 31 s (02:06:48 → 02:07:19) | journal ; `depenses.md` l. 88 |
| crédit | 11,79 USD (2026-10-20 06:07 UTC) | `depenses.md` l. 89 |
| cumul de la phase 0 | ≈ 67 USD plus les disques, sur 150 | R-262 |

### 5.2 Estimation de P4

| poste | durée estimée |
|---|---|
| démarrage, clonage, poussée initiale, installation | ≈ 2,5 min |
| suite des tests (908 + 60 à 80) | ≈ 29 à 33 min |
| chargement du modèle et format | ≈ 2 à 3 min |
| M5 : 529 passes courtes et notation | ≈ 1 min |
| 4 bras × 60 passes d'épisode | ≈ 2 min |
| notation de 2 400 actions par 424 sondes (sans Mahalanobis, plus légère qu'en P3) | ≈ 6 à 8 min |
| écritures, sceaux, poussées, arrêt | ≈ 2 min |
| **total** | **≈ 45 à 52 min ; 0,8 à 1,1 h avec marge** |

| poste | attendu | borne de l'étape |
|---|---|---|
| carte | 0,8 à 1,1 h × 1,0889 = 0,87 à 1,20 USD | 9 600 s × 1,30 = 3,47 USD |
| arrêt | — | 10 min × 1,30 = 0,22 USD |
| téléchargement | ≈ 20 Go × 0,026 = 0,52 USD | 20 Go × 0,05 = 1,00 USD |
| disque arrêté jusqu'à la destruction | ≈ 0,05 USD (1 à 2 h) | 24 h × 0,03 = 0,72 USD |
| **total** | **≈ 1,5 à 1,8 USD** (≈ 2,2 USD au prix plafond) | **5,41 USD** |

- **Crédit exigé à la création** : 3 h × (prix + autres projets en marche) + 1,2 USD = 4,47 USD à 1,0889 ; 5,10 USD à
  1,30. Le crédit (11,79 USD, moins le disque de 56799469 jusqu'à sa destruction, ≈ 0,022 USD de l'heure) suffit pour P4
  seul, pas pour deux lancements à la fois.
- **Plafond** : GO-2026-10-04-08, 150 USD, alerte à 120 USD ; cumul après P4 ≈ 69 USD plus les disques. Échéance
  2026-11-01 : un lancement après cette date est un nœud (prolongation du GO).
- **Économie possible** (question) : sans la suite complète des tests sur l'instance (≈ 30 min, ≈ 0,55 USD), le run se
  ferait en ≈ 20 min ; écart à la pratique de P3, à décider.

## 6. Calendrier indicatif

- 20-21 octobre : contre-lecture R2 du brouillon ; mesures de conception ; candidat.
- 21-23 octobre : module, tests, contre-lecture du code, bancs, répétitions.
- 23-25 octobre : scellement S, accord, lancement (≈ 1 heure), récupération, destruction de l'instance.
- Après le verdict complété de P3 (addendum 2) : lecture, verdict R13, GO de Lazar, vers le 28 octobre.

## 7. Questions ouvertes pour la session

1. **Entropie** : tirée par le rédacteur à 09:51:35 UTC (`53867522133019232757448053239299230533`, sortie brute
   `entropie-tiree-v1.txt` dans ce dossier) ; la consigner par une ligne R-…, ou en tirer une autre avant tout usage.
2. **Emplacement du code** : hors de l'arbre gelé (recommandé), ou sous `src/` après la clôture de P3.
3. **Tolérances de la garde d'identité** : 5·10⁻² (niveau 2, scores), 10 % (exclusions), 0,005 (aires de validation de
   M5) ; ce sont des seuils de séance, sans mesure. MC-2 dira combien d'épisodes passent au niveau 1 avant le scellement.
4. **Variante « rapportée à un autre agent » (A5)** : les réponses la gardaient en descriptif dans C1 corrigée ; la note
   (option A1, liste fermée M5, C1, M6) ne la cite pas. Ce brouillon l'exclut.
5. **Phrases B** : la réponse M6 demande une consigne bénigne « écrite et scellée avant le run par un sous-agent neuf ».
   Le rédacteur, neuf, a écrit la liste fermée ; faut-il la faire valider par le contre-lecteur R2 ou par un autre
   sous-agent ?
6. **Ordre des lancements** (un seul à la fois) : P4, P3b (N-028, GO-2026-10-20-05), l'étape payante du plan B, le pilote
   du papier C. Ce brouillon place P4 avant toute lecture de P3b (règle du témoin positif, ABC l. 83 ; R-262).
   Variante : une même instance pour P4 et P3b (gain ≈ 0,6 USD de mise en place), textes et lectures séparés, P3b lu
   après le verdict de P4.
7. **Délégation R-217** : liée au mandat d'autonomie (R-260 : jusqu'au 2026-10-20 vers 21:35 UTC). Un lancement après
   le mandat demande l'accord de Lazar dans la session (R-185) ; la ligne d'accord reste exigée par le lanceur.
8. **Effet d'un échec sur P3b et T0.7** : ce brouillon écrit qu'un échec (L3, L6, L8, L9) met la chaîne en nœud avant
   toute nouvelle lecture d'un organisme. Ce n'est pas un réglage de T0.7, mais c'est un arrêt de P3b : à confirmer.
9. **Instance de P4** : détruite après la récupération vérifiée (recommandé, rien n'y reste d'utile), ou gardée jusqu'au
   verdict (72 heures au plus, ≈ 1,6 USD).
10. **Lecture conditionnée au verdict complété de P3** : garde dans le code (chemin et empreinte exigés), ou seulement
    l'ordre de la chaîne.
11. **Mesures de conception sur les textes honnêtes de P3** (MC-2, MC-3, processeur, avant le scellement) : elles lisent
    les textes pour les retokeniser, aucun score ; à accepter au titre de R1 (propriété des entrées, pas un résultat).
12. **Filtre d'offre** : gardé égal à celui de P3 (128 000 Mo, 16 cœurs) pour réutiliser la chaîne éprouvée ; P4 n'en a
    pas besoin (aucun entraînement) ; un filtre relâché élargirait le marché.
