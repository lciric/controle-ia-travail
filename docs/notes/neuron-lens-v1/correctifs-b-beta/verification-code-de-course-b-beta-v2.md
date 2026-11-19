# Vérification du code de course de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, Llama 3.1 8B Instruct) et de la commande — v2

**Verdict pour le code (contrôles, lanceur, partie 2, essais, amorce, dépôt réduit, requirements v2) : « à corriger, légèrement ».**
0 bloquant, 1 majeur (couverture des essais câblés, voir N-M1), 9 mineurs. Tout ce que la contre-lecture v1 réclamait au code est
levé ou levé en partie ; je n'ai trouvé **aucun défaut de calcul ni de câblage** (les chemins que les essais ne couvrent pas ont été
joués par moi sur des doubles, voir « Ce que j'ai exécuté »), et **aucun arrêt ajouté qui ne soit dans le sens sévère** (voir §
« Écarts au texte gelé »). Le majeur est une règle gelée (R5), pas une erreur de code.

**Verdict pour la commande v2 (`commande-b-beta-v2.md`) : « à corriger ».** 4 majeurs (C-M1 à C-M4), 6 mineurs. Les valeurs (prix,
plafond, seuils, minuterie, rappels, disque, carte) sont justes ; ce sont l'ordre des étapes, l'autonomie du texte, l'image et le
prix déclaré à la garde qui manquent.

- **Lecteur** : sous-agent neuf (R2), modèle Sonnet 5.5 (`claude-sonnet-5-5`) ; n'a rien écrit du code ni de la contre-lecture v1.
  Date : 2026-11-18 (UTC). Branche `claude/lentilles-b-beta-course-v1`, sommet `47c9b115`.
- **Essais demandés** : 153 passés, 0 sauté, 0 échec (`test_neuron_lens_controles_b_beta_v2`, `…b_beta_lancer_v2`, `…montage_b_beta_v2`,
  `…etapes_b_beta_v2`, `…verdicts_b_beta_v4`). Dépôt réduit reconstruit depuis `47c9b115` (83 fichiers, liste `791af13d…` : **égale** à
  celle du journal de l'essai à blanc) : les huit fichiers d'essais de l'amorce y passent, 217 passés, 0 sauté, arbre propre.
- **Empreintes lues** (16 premiers caractères) : `controles_b_beta_v2.py` `ddc36c55a6b9`, `b_beta_lancer_v2.py` `65081931e19e`,
  `addendum_partie2_b_beta_v2.py` `9baaea357752`, `amorce_neuron_lens_b_beta_v2.sh` `a50a0eb54e93`, `depot_reduit_neuron_lens_b_beta_v2.py`
  `36ee3a5bf028`, `requirements-neuron-lens-b-beta-v2.txt` `8c9016c2ab65` ; compagnons `.sha256` conformes (`scellement verifier`) ;
  `verdicts_b_beta_v4.py` `8c07434f…` et ses essais `1b63c8cb…` égaux aux valeurs codées dans `PIECES`.

## Ce que j'ai lu
- Font foi : texte gelé (entier, de « Chaîne en défaut » à la fin, le début en diagonale) ; addendum partie 1 v3 (entier).
- Contre-lecture v1 (entière). Code v2 : `controles_b_beta_v2.py`, `b_beta_lancer_v2.py` (entiers, 1 394 lignes), `addendum_partie2_b_beta_v2.py`
  (différence et fonctions de relevé) ; différences v1 → v2 des trois fichiers de code, des trois fichiers d'essais pré-existants, de
  l'amorce et du dépôt réduit ; `test_neuron_lens_etapes_b_beta_v2.py` et `…montage_b_beta_v2.py` (entiers) ; amorce v2 (entière) ;
  `essai_a_blanc_amorce_neuron_lens_b_beta_v1.sh` (80 premières lignes) et son journal (entier) ; `requirements-…-v2.txt`.
- Voisin (lecture seule, jamais importé) : `transport.py` (`Accumulator`), `lenses.py`, `scripts/02_fit.py` (l. 120-200), `04_export_rlens.py`,
  `07_drivers.py` (fin), `03_token_counts.py`, `catalog.py` (`neuron_table`, `head_table`, `kept`), `arch.counts_path`, `paths.py`,
  `lens_compare.py` (l. 56-82) et le correctif (4) ; `.gitignore` du voisin (`data/checks` non suivi). Drowse (lecture seule) : fermeture
  d'imports par analyse syntaxique des six modules de l'interface (résultat : `torch`, `safetensors`, `yaml`, et `transformers` par sur-approximation).
- Commande v2 (entière) ; devis v12 (en-tête, §§ 1, 3, 4, 5) ; commande v8 de la tranche précédente (`git show origin/prep/neuron-lens-v1:…`, entière).
- **Non ouverts** : aucun fichier de résultats (rien sous `diag/`, la série repère n'a été ni lue ni ouverte ; mes doubles écrivent leur
  propre série), rien sur les sujets interdits, rien dans `registres/`, aucune machine, aucune clé, ni commit ni poussée.

## Ce que j'ai exécuté (hors du dépôt, sous le scratchpad ; non versé)
1. Les essais demandés (153) ; le dépôt réduit et ses 217 essais ; `garde_depense_v4 --minuterie-seulement` à 2,62 / 1,85 / 1,84 / 2,04
   USD/h (91 374 / 129 405 / 130 108 / 117 352 s : conforme à « 91 374 s » et au plancher de 1,85).
2. **`ALLER_RETOUR`** (la chaîne de code que le banc envoie dans un processus enfant, jamais exécutée par les essais du dépôt) : joué
   avec un faux `neuron_lens.lenses` et un faux fichier d'ajustement de trois documents — cas sain (`[]`), couche 3 à `None`, `load_lens`
   qui lève : les trois issues sont celles de la garde (o). Syntaxe, arguments (`sys.argv[1]`, `[2]`), chemins d'import : conformes.
3. Un essai de bout en bout `etape_grandeurs` → `etape_declencheurs` → `etape_verdicts` (cas sain tiré de la référence publiée ramenée à
   32 couches par le code des verdicts, doubles pour `_grandeurs`) : verdict « reproduit avec nos lentilles », fichier des verdicts puis
   fichier des intervalles écrits ; même cas avec la lentille R publique écartée de 0,11 à une couche : `ChaineEnDefaut` de lettre « a-c-e-j ».
4. `etape_audit_relance` avec une horloge qui dépasse l'heure pendant les grandeurs de la graine 1 : « non joué » (M-5 levé) ; sans dépassement : « joué ».
5. Les artefacts de l'export un par un, pour voir les lettres levées : `none12` → e, h, o ; `ecart5` → o ; `identite10` → e, o ; `egale_npR` → n ; `absente` → o.
6. `jeton_de_debut` avec un vrai tenseur torch (compte, rang, égalités) : conforme.

---

## Table de reprise de la contre-lecture v1

| point v1 | statut | constat v2 |
|---|---|---|
| **B-1** (1) tables des pilotes | **levé** | `b_beta_lancer_v2.py` l. 1093-1099 : tout fichier de `data/` dont le nom ou un composant du chemin contient « drivers » ; `cb.tables_pilotes` exige les 32 tables `neurons/drivers/L00…L31.parquet` et `heads/drivers.parquet` (vérifié contre `07_drivers.py` l. 139-148 et `catalog.neuron_table`/`head_table`) ; fin du journal gardée ; essai `test_pilotes` (33 tables) et `test_pilotes_tables_manquantes`. |
| **B-1** (2) compte et rang du jeton de début | **levé** | `cb.jeton_de_debut` (l. 553-562) lit `comptes[128000]` du fichier de `03_token_counts.py` (`FonctionsVoisin.comptes_jetons`, clé « counts » vérifiée), rang par compte décroissant parmi les jetons gardés, règle d'égalité écrite ; versé à l'étape et en partie 2 (`rediger_corpus`). Vérifié avec un vrai tenseur. |
| **B-1** (3) valeurs des contrôles de matrices | **levé** | `ecarts_identite`, `ecarts_npr`, `ecarts_aller_retour` rendues et écrites au résultat de l'export (l. 953-967) ; `ecarts_identite` aussi pour les trois lentilles de Neuronpedia à B0 (l. 679-685). |
| **M-1** contrôle des moitiés d'A2 et A3 sans effet | **levé** | `empreinte_matrice` par couche 0-30 de chaque moitié, lue sur les matrices chargées ; `controles_a2_a3` exige les 31 couches distinctes ; essais unitaires (égalité à la couche 4, trente couches) et câblé (`test_audits_controles_et_temps`). Réserve : N-m2. |
| **M-2** banc : l'écriture du fichier dans le temps lu | **levé** (décision de la mère, R-3220) | `--docs 3`, `m.group(2) == "3"`, `temps[1]` ; l'essai `test_banc` met 40 s au premier et 30 s au troisième document pour prouver qu'ils ne sont pas lus. La lecture à une décimale reste (impossible à lever), déclarée (commande, déclaration 7). |
| **M-3** aucun essai de Drowse avant l'ajustement | **levé** | (1) `IMPORT_DROWSE` dans un enfant à B0, arrêt sur code non nul ou sentinelle absente (essai `test_b0_import_drowse_en_echec`, cause bien isolée) ; (2) `_aller_retour_banc` : `04_export_rlens.py` sur le fichier de trois documents de la copie du banc, `load_lens`, garde (o), arrêt avant l'ajustement. Script enfant joué par moi : correct. Réserve : N-m7. |
| **M-4** reprise de l'export : verdict à tort | **levé** | `home.exists() and not list(home.rglob("manifest.json"))` → suppression et refaite (l. 934-935) ; essai `test_export_reprise_sans_manifeste_refait`. Réserve : la suppression n'est pas consignée au résultat (N-m3). |
| **M-5** temps réservé non appliqué | **levé** | relu à l'entrée, après `measure`, après `score`, **après les grandeurs de la graine 1** (l. 1292-1294) et deux fois dans `etape_audits_controles` ; audits de contrôle avant la relance (`ETAPES`, `suite`, `exiger_prerequis`, test d'ordre). Joué par moi avec horloge remplaçable : conforme. Essais versés : partiels (N-M1). |
| **M-6** gardes câblées jamais essayées | **levé en partie** | `test_neuron_lens_etapes_b_beta_v2.py` joue les vraies fonctions d'étape pour (q) ×2, (g), l'export (e)(n)(o)(h), la reprise, les pilotes ((p)(k)(r) + tables), `measure` (p), les lectures ((s) premier lancement et relance, (k) ×2, liens durs), le banc (trois temps, aller-retour, écriture dans l'arbre), les audits de contrôle (M-1, temps), B0 (import) ; le fichier du montage est dans l'amorce et le dépôt réduit (avec `garde_depense_v4.py`) et couvre dépense 45,0/67,5, minuterie, empreinte de Drowse. **Reste non couvert** : N-M1. |
| m-1 comptes de jetons après relance | levé | message « relance de la machine après les comptes … nœud à la mère » (l. 1004-1005) ; l'arrêt reste définitif, conforme à « une seule fois ». |
| m-2 banc repris | levé | `*-T128.pt` et `data/lenses` de la copie du banc supprimés au début de l'étape. |
| m-3 garde (s) à la reprise ; motif | levé | premier lancement (journal des lectures absent) : `garde_s` sur `data/checks/reads_at_firings-*.pt` (glob, la lettre du texte ; `data/checks` n'est pas suivi par le voisin : pas de faux positif) et le résumé de Llama ; relance : arrêt simple. Essai `test_reads_s_premier_lancement_et_relance`. |
| m-4 gardes (a)-(c), (e), (j) trop tard | levé (code) | `etape_grandeurs` (l. 1180-1186) ; vérifié par mon essai. Pas d'essai versé : N-M1. |
| m-5 `--device cuda` | levé | retiré ; `test_reads_sain_liens_poses` vérifie l'absence. |
| m-6 message du correctif (1) sur tout le journal | levé | `rsplit("\n=== ", 1)[-1]` (l. 1080) pour la passe. |
| m-7 recopie de `split_half` | levé | `FonctionsVoisin.split_half` appelle `Accumulator.split_half` du dépôt ; la recopie est versée (`diffs_recopie`) ; seuils lus sur la valeur du dépôt. |
| m-8 empreintes du code des verdicts | levé | `PIECES` + `N_ESSAIS_VERDICTS = 82` exigé à B0 (valeurs vérifiées). |
| m-9 tokeniseur en ligne dans le lanceur | levé | `os.environ["HF_HUB_OFFLINE"] = "1"` après `01_lens_corpus.py`, avant tout import de la bibliothèque dans ce processus (chaque étape est un processus). |
| m-10 contrôles de la graine 1 | levé | `graine_1` versé ; lecture « dose strictement positive » déclarée (commande, 10). |
| m-11 clause « fichiers » de (n) | levé | dit dans la docstring de `garde_n`. |
| m-12 28 672 pôles | levé | `accord_depuis_lens_compare` lève sinon ; `rows = 2 × 14 336` vérifié sur `lens_compare.py` (`ia` = les deux signes). Essai unitaire. |
| m-13 verdict avant les intervalles | levé (réserve) | verdict écrit d'abord, intervalles dans leur propre fichier scellé, erreur consignée sans toucher au verdict ; vérifié. Réserve : N-m8 ; la clé des motifs (« a-c-e-j-et-machine ») reste une clé unique, pas les lettres (forme). |
| m-14 « recomptées » | levé | docstring de `problemes_gardes` dit tel quel d'où vient chaque lettre. |
| m-15 `requirements`, python avant pip | **levé en partie** | PyYAML ajouté, python lu avant `pip` (code 19, essayé à l'essai à blanc avec un artefact) ; **`pyyaml` et `pytest` restent sans version** (N-m5). |
| m-16 mémoire, disque ; export avant S | levé | export entre les deux ajustements ; commande : « Réserves » (mémoire 32-48 Gio, filtre `cpu_ram>=64`, disque 200 Go) ; le disque ne compte pas les ≈ 4 Gio de l'export du banc (C-m4). |
| Déclaration de forme (Drowse sans dépendances, PyYAML) | levé en partie | `pyyaml` dans les exigences ✓, essai d'import à B0 ✓ ; la déclaration 1 de la commande dit encore que seuls torch et safetensors sont importés (C-m1). |
| P.4 : gardes du montage (dépense 45,0/67,5, empreinte de Drowse) | levé | `test_neuron_lens_montage_b_beta_v2.py` dans l'amorce et le dépôt réduit. |

## Écarts au texte gelé et sens des arrêts ajoutés
- **Banc à trois documents, le deuxième lu** : écart voulu (R-3220), déclaré. Il ne rend pas la règle plus lâche que le texte : il retire seulement l'écriture du fichier du temps mesuré.
- **Arrêts ajoutés, tous dans le sens sévère** (aucun ne laisse passer ce que le texte arrête) : import de Drowse à B0 ; aller-retour d'un export dans la copie du banc ; 82 essais du code des verdicts ; 33 tables des pilotes ; 28 672 pôles de la comparaison ; les 31 couches des moitiés exportées distinctes ; fichier de comptes déjà présent (déjà le cas) ; relance avec sorties de lectures présentes. Aucun n'a de faux positif que j'aie pu construire (vérifié : `rows`, tables, `data/checks` non suivi, sentinelle d'import).
- **Seul écart de forme du côté permissif** : la garde (s) à une relance donne un arrêt simple (sans le fichier de verdicts « chaîne en défaut » de rang 1) ; la course s'arrête quand même et la mère tranche ; déclaré (commande, 10) ; proposé par la contre-lecture v1 (m-3). Pas un défaut.
- **Ordre** : export entre R et S (P.3, étape 2 : « à la fin de chaque ajustement … → export ») ; audits de contrôle avant la relance : aucune dépendance cachée (`etape_export` ne lit pas S ; `exiger_prerequis` correct ; `debut_audits` posé à `declencheurs`). Conforme.

## Points neufs — code

### Majeur
**N-M1 — Le câblage neuf de la v2 n'est pas tout essayé (R5)** (`tests/test_neuron_lens_etapes_b_beta_v2.py`, `…lancer_v2.py`). Les essais câblés couvrent les gardes de la v1 que M-6 listait, mais
pas les chemins que la v2 a *ajoutés ou déplacés* : (a) les gardes (a)-(c), (e), (j) à `etape_grandeurs` (m-4) : aucun essai, ni le cas sain ni l'artefact (« 0,11 à une couche ») ;
(b) `etape_comptes_jetons` avec `jeton_de_debut` (B-1 (2)) : `FauxVoisin` n'a même pas la méthode `comptes_jetons` ; (c) `etape_verdicts` : verdict puis intervalles (m-13) ; (d) `etape_declencheurs`, `entrees`,
`problemes_gardes` (v1 M-6 les nommait) ; (e) M-5 : seule l'entrée de `etape_audit_relance` est essayée, ni la relecture après les grandeurs de la graine 1, ni celle de la fin de `etape_audits_controles` ;
(f) le « cas sain jusqu'au fichier de verdicts » que M-6 réclamait n'existe pas. **J'ai joué (b) en partie, (a), (c), (d), (e) moi-même : tout passe** (« Ce que j'ai exécuté », 3, 4, 6) ; le défaut est de couverture, non de code.
*Correction* : ajouter au fichier des étapes (avec `monkeypatch` de `L._grandeurs`, `L._measure`, `L._score` comme dans mes doubles) un essai sain `grandeurs → déclencheurs → verdicts` jusqu'aux deux fichiers, l'artefact (j) à `etape_grandeurs`,
`etape_audit_relance` avec une horloge qui dépasse l'heure pendant les grandeurs, `etape_comptes_jetons` (ajouter `comptes_jetons` à `FauxVoisin`). Mes trois fichiers de travail sont sous le scratchpad : `…/scratchpad/verif/test_bout_en_bout.py`, `test_relance.py`, `test_lettres.py`.

### Mineurs
- **N-m1** `tests/test_neuron_lens_b_beta_lancer_v2.py` l. ~55-58, `test_banc_lit_le_journal` : périmé (deux documents, `group(2) == "2"`) ; recopie la regex au lieu d'essayer `etape_banc`. À supprimer (remplacé par `test_banc`) ou à passer à trois documents.
- **N-m2** `test_export_artefacts` : les assertions sont `lettre in lettres` ; `none12` lève e, h **et** o, `identite10` lève e **et** o (mesuré) : (h) et (e) n'ont pas d'artefact isolé. Et aucun essai ne montre que `etape_export` produit des `matrices_moities` **égales** quand les deux moitiés ont les mêmes sommes (le scénario exact de M-1) : seul `test_audits_controles_et_temps` reçoit des empreintes déjà égales. Ajouter l'artefact « sommes égales » (moitiés pareilles → (o) tient, `matrices_moities` égales, A2 les voit).
- **N-m3** `b_beta_lancer_v2.py` l. 934-935 : la suppression d'un export partiel n'est pas « consignée au résultat » (M-4 le demandait). Ajouter la liste des dossiers refaits au résultat de l'étape.
- **N-m4** `controles_b_beta_v2.py` l. 428-432 : A2/A3 exigent les 31 couches distinctes, plus strict que « exports des moitiés d'empreintes différentes » (texte). Sens sévère, aucun faux positif plausible ; à déclarer à la commande (avec les autres arrêts ajoutés : 33 tables, 28 672 pôles, 82 essais ; voir C-m2).
- **N-m5** `requirements-neuron-lens-b-beta-v2.txt` l. 17-18 : `pytest` et `pyyaml` sans version (m-15 en partie). Épingler les versions relevées (ou dire que la partie 2 les relève sans critère, ce que fait `versions()`).
- **N-m6** `amorce_neuron_lens_b_beta_v2.sh` l. 235-243 : le code 18 (roue de Drowse d'un autre nom ou d'une autre empreinte) n'est essayé nulle part (R5) ; l'en-tête de l'essai à blanc le déclare « non jouable en mode jouet ». Soit l'essayer avec un `pip` factice, soit le déclarer à la commande comme non essayé.
- **N-m7** La chaîne `ALLER_RETOUR` (lanceur l. 846-860) n'est exécutée par aucun essai du dépôt ; `test_banc_aller_retour_en_echec` n'essaie que la lecture de sa sortie. Je l'ai jouée (correcte). Ajouter un essai avec un faux `neuron_lens.lenses` (mon modèle : `…/scratchpad/verif/ar/`).
- **N-m8** `etape_verdicts` (l. 1354-1369) : un arrêt entre l'écriture du fichier de verdicts et celle du fichier des intervalles laisse la course « finie » (`suite` rend « fin ») sans résultat d'étape ni intervalles, et `jouer` refuse de rejouer. Sans effet sur le verdict (intervalles rapportés). Permettre la reprise des seuls intervalles, ou le dire.
- **N-m9** `ECHEANCES["banc"] = (0,1 ; 0,3)` : l'étape contient maintenant deux ajustements de trois documents, deux écritures de ≈ 8 Gio, un export et un chargement ; l'attendu de 0,1 h sera dépassé (compte rendu `depassement_pire_cas` seulement au-delà de 0,3 h, donc sans effet). À relever à 0,2 h par honnêteté du suivi.

## Les essais neufs éprouvent-ils ce qu'ils disent ?
Oui pour ce qu'ils couvrent, avec les réserves N-m1, N-m2, N-m7. Cas par cas : `test_banc` (les temps 40 / 30 s hors lecture prouvent M-2 ; le test échouerait avec la v1) ;
`test_export_reprise_sans_manifeste_refait` (échouerait avec la v1) ; `test_reads_s_premier_lancement_et_relance` (la seconde assertion exige un arrêt qui n'est **pas** une chaîne en défaut) ;
`test_pilotes` (une cause par artefact : p, k, r, vérifié par `lettres == [...]`) ; `test_q_*` et `test_g_moities_inegales` (cause unique) ; `test_b0_import_drowse_en_echec` (le message « import » ne peut venir que de l'étape visée) ;
`test_audits_controles_et_temps` (cause unique : la couche 4). Aucun artefact n'échoue pour une autre raison que la garde visée ; deux échouent en plus pour une garde liée (N-m2), et c'est la garde visée qui est dans l'assertion.

---

## Commande v2

**Valeurs vérifiées conformes** (devis v12 §§ 3-5 et texte gelé) : prix exigé 2,62 USD/h, stockage de 200 Go compté ; plancher 1,85 USD/h ; trafic ≤ 0,04 USD/Go ; plafond 75 USD ; compte rendu 45,0 et arrêt dur 67,5 USD ;
minuterie D = (67,5 − 1,0)/prix lu, 91 374 s au prix exigé exact (recalculée par `garde_depense_v4` : 91 374 ; plancher : 129 405 ≤ 129 600 < 130 108) ; frais fixes 1,0 USD (lieu L1) ; rappels à 12,9 h et 24,1 h (valeurs du texte gelé avec L1) et à 80 % de D ;
disque 200 Go ; filtre complet (`H100_SXM … disk_space>=200 inet_down>=300 inet_up>=200 reliability>0.98 cuda_max_good>=13.0 rentable=true`) ; carte « HBM3 » (H100 SXM ; H100 PCIe, A100, H200 refusées à l'essai à blanc) ; fenêtre du 19 au 25 novembre ; clé selon R-3151 ; `RUN_ID`, branches `course/…-v2` et `calcul/…-v1` ; drapeaux de `garde_depense_v4` valides.

### Majeurs
- **C-M1 — Étape 12 : l'ordre des étapes est celui de la v1.** Elle écrit « `ajustement-R` → `ajustement-S` (gardes (q), (g), (h)) → `export` », et « `audit-relance` (A1, A5) et `audits-controles` (A2, A3, A4) » : le code fait `ajustement-R` → `export` → `ajustement-S` et `audits-controles` → `audit-relance`. Elle contredit sa propre déclaration 9 (« export entre les deux ajustements »). Elle ne dit rien non plus de l'aller-retour du banc (déclaration 8) ni de la lecture de la version de python avant `pip` (code 19). Corriger l'étape 12 sur `ETAPES`.
- **C-M2 — Le texte n'est pas employable seul.** Il renvoie « comme à la v8 » (autre branche, `prep/neuron-lens-v1`) pour : le préambule P (`PATH` de `vastai`, rien d'imprimé de `show … --raw`) ; la commande de crédit ; les commandes de lancement détaché de la minuterie et de la garde (fichiers PID, `ps -p`, `setsid nohup`) ; la boucle de veille ; la **règle de destruction** (« celle de la v8 avec b-beta pour b-alpha » — la table n'est pas là, et il faut y ajouter les codes 18 et 19, absents de sa ligne « course non lancée (10, 11, 12, 13, 14, 16, 17) ») ; le rappel à 75 % de D où la mère décide (présent à la v8, absent ici et au devis : à trancher). En outre : la section « Essai à blanc » dit « À écrire et jouer … Non fait à ce jour », « l'amorce v1 », « lanceur v1 » alors que l'essai a été joué (journal `essai-a-blanc-amorce-b-beta-v1.txt`, conforme, 0 écart) ; la table des pièces dit « code de course v1 » ; « Empreintes » est vide ; l'empreinte de la liste attendue (`791af13d…`, que j'ai reconstruite à l'identique depuis `47c9b115`) n'est pas citée à l'étape 5. À recopier ou inclure, et à remplir une fois le code figé.
- **C-M3 — Image flottante, version de python exigée à l'unité.** L'étape 7 crée l'instance avec `python:3.12-bookworm` (étiquette qui suit les correctifs de 3.12) ; l'amorce v2 s'arrête au code **19** si `python3` n'est pas **3.12.16** (addendum partie 1, § 5). Si l'image a avancé depuis le 17 novembre, la course s'arrête à la première minute, instance payée. Épingler `python:3.12.16-bookworm` (ou, si l'étiquette n'existe pas, dire que l'étape 8 lit la version et détruit) et nommer le code 19 aux étapes 12-13.
- **C-M4 — Le prix déclaré à la garde n'est pas tranché.** Le devis v12 (décision 1, § 5) dit que la commande « tranche le prix déclaré à la garde et la borne haute de la minuterie » ; la borne haute est tranchée (étape 4 : non retenue), le prix déclaré ne l'est qu'implicitement (`--prix-h <PRIX>`, le prix lu). Écrire le choix et ses trois conditions du devis : lecture du prix en cours de course (que faire si elle échoue : deux lectures ratées → prix exigé), repli sur le prix exigé si la lecture échoue à la création, et `dph_total` supposé compter les 200 Go (déclarer le plus grand du prix lu et du prix de l'offre au relevé, ou dire qu'on ne le fait pas).

### Mineurs
- **C-m1** Déclaration 1 : « n'importent au chargement que torch et safetensors » est inexact ; `drowse.lens.sources` (sur le chemin de `save_lens` et `load_local_lens`) importe `yaml`. Dire : PyYAML installé par les exigences, importé par l'essai de B0.
- **C-m2** Déclaration 4 : omet les 82 essais du code des verdicts (neuf en v2) ; aucune déclaration pour les 33 tables des pilotes, les 28 672 pôles, les 31 couches distinctes des moitiés exportées, la suppression d'un export partiel à la reprise (tous sens sévère).
- **C-m3** Déclaration 7 : « Proposé à la mère avec recommandation » ; c'est décidé (R-3220). Étape 14 : le fichier des intervalles `intervalles-b-beta-v1.json` et son compagnon ne sont pas dans les fichiers vérifiés.
- **C-m4** « Réserves » : le disque ne compte pas l'export du banc (≈ 4 Gio de plus dans la copie à part).
- **C-m5** Étape 7 : « création (image `python:3.12-bookworm` ; disque 200 Go) » et le filtre de l'étape 4 sans `inet_up_cost`/`inet_down_cost` : le plafond de trafic est vérifié à l'étape 8 seulement ; acceptable, à dire.
- **C-m6** Étape 11 : les valeurs « 80 % de D » ne sont pas chiffrées (73 099 s, 20,3 h au prix exigé exact) ; les chiffrer comme à la v8.

## Ce que cette vérification ne couvre pas
L'exécution réelle du code voisin et de Drowse (interdite dans le conteneur) : l'aller-retour (`save_lens` / `load_local_lens`, type et précision des matrices relues) ne sera établi qu'au banc de B0. Le texte de la commande n'est pas jouable ici (aucune machine, aucune clé). Les verdicts (`verdicts_b_beta_v4.py`) et les grandeurs (`grandeurs_b_alpha_v1.py`) ne sont lus que par leurs appels.
