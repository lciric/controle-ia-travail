# Note du développeur — adaptateur de MC de B bis vers le code scellé de la pièce « mots et coût », v1

- **Auteur** : « modèle A », développeur du code de B bis (rapport `rapport-developpeur-v1.md`, `0b694da9…`, qui reste tel
  quel ; cette note lève sa réserve R-DEV-6).
- **Date (UTC, `date -u`)** : 2026-11-14, de 15:08 à 15:25.
- **Fait déclencheur** (message de la mère) : ligne `CODE-MOTS-ET-COUT-T06` inscrite le 2026-11-14T14:55:41Z (R-2778), donc avant
  l'échéance du repli (mercredi 18 novembre, 12:00 UTC) : MC de B bis passe par le code de la pièce, et non par le repli
  (`prereg/T0.7-etape-B-bis-v1.md`, « Métrique », MC : « apprises et notées par le code de la pièce […] sans changement »).
- **Branche** `prep/t07bbis-code-v1` ; commit du code de l'adaptateur : `9e5b7011fbcc5a7c92f31f17710f8d11273e5bfb` (parent
  `f04558b1`) ; rien poussé, aucun `git fetch`, aucune fusion, `main` non touché.
- **Lu de `main`, par chemin exact et rien d'autre** : `scripts/mots_et_cout_t06_v3.py` (entier), le fichier de la ligne
  `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `registres/scellements-v1.md` (chemins et empreintes ; aucune
  ligne n'a été suivie vers un fichier de `diag/`, `runs/` ou `donnees/`), `docs/notes/piece-mots-et-cout-v1/rapport-developpeur-code-v3-v1.md`
  (§ 2, § 3, § 5 R-D15/16, § 8). **Apportés dans la branche** (`git checkout main -- CHEMIN`, chemins exacts) :
  `scripts/mots_et_cout_t06_v3.py` et son `.sha256` (`9dbcc55c…`), le fichier de la ligne et son `.sha256` (`e418fdaf…`) ;
  `scripts/fabrique_factice_mots_et_cout_t06_v1.py` (`13df3976…`) était déjà dans l'arbre, identique. Aucune donnée de 7a, 7b,
  T0.7 ni de P3-bis ; aucune sortie de l'audit des fuites.

## 1. Verdict

**Adaptateur écrit, éprouvé, prêt pour la contre-lecture**. Sur les entrées factices de la pièce, le contrôle d'égalité de la
lecture de B bis passe **à l'écart 0** (quatre doses, bases (A) et (B)). La suite de B bis est rejouée : **96 essais passent**
(10 fichiers ; 88 avant, plus 8 essais de l'adaptateur ; `essais-sortie-adaptateur-mc-v1.txt`). Avec la pièce, la base (A) est
égale au repli de B bis ; la base (B) en diffère en trois points, déclarés au § 4.

## 2. L'adaptateur

Module neuf `src/controle_ia/t07bbis/lien_mots_et_cout_v1.py` (`075b4999…`) ; lien `module:attribut` attendu par
`adversaires_texte_v1.charger_adaptateur` : **`controle_ia.t07bbis.lien_mots_et_cout_v1:AdaptateurPieceMC`**. Au chargement,
avant tout import du code de la pièce, et **sans aucun repli** (chaque faute est un arrêt `GardeArret`, motif écrit) :
1. ligne `CODE-MOTS-ET-COUT-T06` de `registres/scellements-v1.md` présente une fois, de forme exacte (absente, en double ou mal
   formée → arrêt) ;
2. fichier cité égal à `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, à l'empreinte de la ligne, compagnon
   `.sha256` égal (`t07.registre_v1.sceau_conforme`) ; `commit` et `fichiers` lisibles ;
3. module `scripts/mots_et_cout_t06_v3.py` lu sur le disque **à l'empreinte** `fichiers["scripts/mots_et_cout_t06_v3.py"]` du
   fichier de la ligne, et **le même** au commit cité (`git show <commit>:scripts/mots_et_cout_t06_v3.py`) ;
4. module exécuté **depuis les octets dont l'empreinte vient d'être vérifiée** (aucune seconde lecture), sous un nom propre ;
   `VERSION = 3` et contrat (`centres`, `apprendre_a`, `noter_a`, `apprendre_b`, `noter_b`) exigés ; modules gelés de la pièce
   vérifiés par sa fonction `verifier_modules_geles` (neuf modules, tous à l'empreinte de la pièce dans cet arbre) ;
5. fils de calcul `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS` égaux à « 1 » (exigence de la pièce en mode réel :
   l'ordre des sommes change les coefficients ; sans cela, le contrôle d'égalité à 10⁻¹² pourrait refuser). `exiger_fils=False`
   seulement dans les essais.

Interface : `centres` → `centres` de la pièce ; `apprendre` → `apprendre_a` (base (A), « N-029 ») ou `apprendre_b` (base (B),
« mots_et_cout ») ; modèle non calculable de la pièce → `NonCalculable` (motif de la pièce recopié), jamais un score ;
`noter` → `noter_a` / `noter_b` ; le modèle rendu porte `jeu` (refus de la lecture de transfert sur le jeu appris, inchangé).

**Changements autour** (même commit) : `lecture_v1.adaptateur_retenu` choisit d'office l'adaptateur de la pièce quand la ligne
est inscrite au plus tard à l'échéance, sinon le repli ; la ligne de commande de la lecture l'appelle (`--adaptateur-mc` reste
possible pour un autre lien) ; `charger_adaptateur(spec, racine=…)` passe la racine du dépôt lu. Commande de la lecture :
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v1 --racine . --run-7b … --run-bbis … --run-lecture …`.
**Repli** : `numpy.log10` remplacé par `math.log10` (centres et traits), comme la pièce ; avant ce changement, deux centres sur
32 différaient d'une unité du dernier rang (essai synthétique) ; après, centres égaux au bit près.

## 3. Essais R5 (`tests/test_t07bbis_lien_mots_et_cout_v1.py`, `6f6fec0a…`, 8 essais)

| demandé | essai |
|---|---|
| cas sain sur données synthétiques | `test_chargement_sain_et_interface` (dépôt jetable : module commité, fichier de la ligne qui cite ce commit, registre ; apprentissage et notation de (A) et (B), aire > 0,9 sur un jeu séparable ; refus du transfert sur le jeu appris ; refus d'un modèle d'une autre interface) ; `test_charger_adaptateur_par_le_lien_et_choix_de_la_lecture` (lien `module:attribut`, `adaptateur_retenu`, `interface_retenue` → « piece ») |
| artefact : module autre que l'empreinte | `test_artefacts_module_ligne_fichier_commit` (module altéré → arrêt) ; `test_charger_adaptateur_par_le_lien_et_choix_de_la_lecture` (ligne inscrite, module autre : la lecture s'arrête, ne passe pas au repli) |
| artefact : ligne absente | `test_artefacts_module_ligne_fichier_commit` (arrêt) ; ligne absente ou postérieure à l'échéance → `adaptateur_retenu` rend le repli (règle du texte) |
| artefact : ligne présente mais fichier différent | `test_artefacts_module_ligne_fichier_commit` (fichier altéré après scellement : compagnon différent → arrêt ; empreinte de la ligne autre → arrêt ; chemin autre → arrêt) |
| autres | ligne en double → arrêt ; commit cité sans le module → arrêt (`test_artefacts_…`) ; fils de calcul non fixés → arrêt, fixés → chargé (`test_fils_de_calcul_a_un_exiges`) ; classe absente, vocabulaire vide → `NonCalculable` (`test_modele_non_calculable_de_la_piece_aucun_score`) ; fichiers réels de la branche : fichier de la ligne `e418fdaf…` → module `9dbcc55c…`, commit `da06bb57…` qui porte ce module (`test_fichiers_reels_de_la_branche`) |
| égalité adaptateur–repli, ou écart déclaré | `test_egalite_adaptateur_et_repli_base_a_et_ecarts_declares_base_b` (§ 4) |
| contrôle d'égalité de bout en bout | `test_controle_d_egalite_de_bout_en_bout_piece_jouet_contre_adaptateur` : la pièce jouée en mode jouet sur les entrées factices de sa fabrique (graine 3) écrit `issue-mots-et-cout-t06.json` ; `lecture_v1.aires_controle_mc` par l'adaptateur sur les mêmes entrées : `controle_egalite` → « égalité vérifiée », écarts **0,0** aux quatre doses ; par le repli : base (A) égale au bit près, base (B) en écart → réserve R-MC, sans nœud |

Tous les essais de l'adaptateur sautent si le module de la pièce est absent de l'arbre (instance : l'extraction partielle de
l'amorce l'exclut ; MC se lit sur processeur seulement).

## 4. Égalité avec le repli de B bis, et écarts déclarés

**Base (A) : égalité**. Mêmes douze traits, même centre (médiane du log10 des coûts lisibles, neuf conditions, au moins dix),
même retrait des traits constants (égalité exacte), mêmes centrage et réduction (ddof 0), même objectif (λ = 1, ordonnée non
pénalisée), mêmes réglages de L-BFGS-B et même convergence (≤ 10⁻⁴ au point rendu). Mesuré (jeu synthétique de l'essai, 32 tâches,
`S50` et `S100` contre H) : aires **égales au bit près** ; scores différents d'au plus 4,2·10⁻⁸ (le gradient de la pièce passe par
`scipy.special.expit`, celui du repli par `exp(−logaddexp(0, −z))` : chemins de L-BFGS-B voisins, arrêtés à 10⁻⁴ de gradient) ; sur
les entrées factices, aires de (A) du repli égales au bit près à celles de `issue-mots-et-cout-t06.json`.

**Base (B) : trois écarts, par construction** (le repli suit le point 8 bis de B bis ; la pièce, ses réglages scellés avec la
ligne) :
1. **mots** : pièce = suites maximales de **lettres** `[^\W\d_]+` sur `str(texte).lower()` (chiffres, souligné et ponctuation
   coupent les mots) ; repli = suites `\w+` sur `texte.lower()` contenant **au moins une lettre** (lettres, chiffres et souligné
   gardés ensemble). Exemple éprouvé : « gpu4 run_x 3x 12 Gate » → pièce {gpu, run, x, gate} ; repli {gpu4, run_x, 3x, gate}.
   Même règle de vocabulaire ensuite (1 000 mots les plus présents en actions d'apprentissage, ex aequo par ordre alphabétique),
   sur des mots différents ;
2. **échelle** : pièce = **aucun centrage ni réduction** des traits de (B) (moyennes 0, écarts 1 dans son modèle) ; repli = tous
   les traits de (B), mots compris, **centrés et réduits** (ddof 0) sur l'apprentissage ; avec λ = 1, les deux solutions diffèrent ;
3. **point (c), « forme du champ du coût »** : pièce = un seul trait **`cout_present`**, lu **sur le texte** de
   `textes-actions-t06.jsonl` : 1 si `lire_action(texte).champs` porte `COST` (ligne `ACTION` lue, première valeur `COST` non vide)
   (R-2765) ; repli = les **six formes** du champ du coût, **colonnes de `mesures-t06.npz`** (traits 7 à 12 de T0.8 :
   `cout_present`, `cout_plusieurs_nombres`, `cout_multiplication`, `cout_intervalle`, `cout_suffixe_k`, `cout_milliers_espace`).
   Le trait `cout_present` est le même des deux côtés quand les mesures sont tirées du même texte (égal action par action sur le
   jeu synthétique de l'essai) ; l'écart porte sur les **cinq autres formes**, que le repli lit et que la pièce ne lit pas.
   Les traits (b) (`cout_normalise`, `illisible`, `sans_centre`) sont les mêmes des deux côtés.

Aires de (B) mesurées sur données synthétiques et factices seulement (aucune donnée du programme), pour l'ordre de grandeur de
l'écart : jeu de l'essai, `S50` 0,74828 (pièce) contre 0,75539 (repli), `S100` 0,92078 contre 0,91992 ; entrées factices de la
fabrique (graine 3), `S25` 0,74772 contre 0,75093, `S50` 0,90575 contre 0,89387, `S75` 0,96288 contre 0,95788, `S100` 0,98111
contre 0,97529. **Conséquence** : avec la ligne inscrite avant l'échéance, B bis lit la base (B) de la pièce (texte scellé de
B bis : « sans changement ») ; le repli n'est plus employé ; s'il l'était (ligne absente), son écart à `issue-mots-et-cout-t06.json`
serait écrit en réserve R-MC, sans nœud, comme le texte le prévoit.

## 5. Réserves

- **R-AD-1** : adaptateur non contre-lu ; à joindre à la contre-lecture du code de B bis.
- **R-AD-2** : la lecture réelle doit être lancée avec les trois variables de fils à « 1 » (posées avant l'import de numpy) ; sinon
  l'adaptateur refuse (arrêt, aucun repli). Les essais tournent avec `exiger_fils=False` et quatre fils : l'égalité à l'écart 0 du
  contrôle y tient parce que pièce et adaptateur calculent dans le même processus.
- **R-AD-3** : la vérification du commit cité exige l'objet du commit dans le dépôt de la lecture (absent : arrêt) ; dans ce clone,
  `da06bb57…` est présent et porte le module.
- **R-AD-4** : l'égalité du contrôle n'est prouvée que sur les entrées factices de la pièce ; sur 7b, elle se vérifie à la lecture
  (aires de (A) et (B) recalculées par l'adaptateur contre `issue-mots-et-cout-t06.json`, 10⁻¹² ; écart : MC « non calculable »
  pour les cellules touchées, et nœud).
- **R-AD-5** : inchangé depuis le rapport v1 (interprétation 6) : les lignes MC des cellules portent sur les actions notées (celles
  de la sonde) ; le contrôle d'égalité porte sur toutes les actions des jeux `S_d` contre H, comme la pièce.
- **R-AD-6** : l'amorce de l'instance n'extrait pas le module de la pièce ; les essais de l'adaptateur y sautent (attendu).
- **R-AD-7** : changement au repli (`math.log10`) : sans effet sur les branches de la lecture qui l'emploient, sauf l'égalité
  au bit près des centres ; les 96 essais passent après lui.

## 6. Refus de la garde rencontrés, et traitement

Une commande en boucle (`for … git cat-file -e main:…`) a été refusée par la garde d'isolement de l'arborescence (forme de
commande git jugée trop complexe) : non contournée ni reformulée ; remplacée par la seule commande autorisée par la consigne,
`git checkout main -- <six chemins exacts>`, suivie d'un contrôle des empreintes contre les compagnons. Aucun autre refus.

## 7. Fichiers à donner au contre-lecteur (en plus de la liste du rapport v1, § 7)

Cette note ; `essais-sortie-adaptateur-mc-v1.txt` ; au commit `9e5b7011` : `src/controle_ia/t07bbis/lien_mots_et_cout_v1.py`,
`adversaires_texte_v1.py` et `lecture_v1.py` (différence avec `0595ba89`), `tests/test_t07bbis_lien_mots_et_cout_v1.py` ;
`scripts/mots_et_cout_t06_v3.py` (contrat, l. 1630-1700 ; `ajuster`, `matrice_b`, `mots_de`, `cout_present`, `centres_de_tache`,
`traits_base_a`, `verifier_modules_geles`) ; `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json` ;
`scripts/fabrique_factice_mots_et_cout_t06_v1.py` ; la ligne `CODE-MOTS-ET-COUT-T06` de `registres/scellements-v1.md` de `main`.
