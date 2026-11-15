# Corrections « CUDA de l'hôte » de l'étape B bis de T0.7, v2 — suites de la contre-lecture (modèle B)

**Déclaration** : rédigé sans vue des données de 7a, 7b, T0.7 ou P3-bis ; rien lu ni écrit sous `diag/`, `donnees/`,
`docs/verdicts/` ; aucun appel au service de location, aucune machine, aucune dépense ; aucun `git ls-remote` réel (les essais
jouent des dépôts nus jetables) ; `MIN_ESSAIS` (87), le code de mesure et les seuils inchangés ; torch et `requirements-gpu.txt`
inchangés.

- **Date (UTC)** : 2026-11-15.
- **Branche** : `prep/t07bbis-code-v1`, partie de `b2c98918` (contre-lecture) ; code et ce rapport dans le commit suivant.
- **Entrée** : `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-corrections-cuda-hote-v1.md` (`6c25cc2a…`), verdict
  « scellable après corrections » ; consigne de la mère (M1, m1, m2, m4, m5, m6, choix 4 ; M2 en commentaire seulement ; m3, m7,
  m8 déclarés ; m9 plus tard). **Complète** `corrections-cuda-hote-v1.md` (`d85c99a1…`, non réécrit, R12).

## 1. Corrections, point par point

| point | fait (« ancien ; nouveau ») | essai (sain ; artefact) |
|---|---|---|
| **M1** branche de sortie de la répétition | `scripts/amorce_repetition_bbis_v1.sh` : `BR_SORTIE=calcul/t07bbis-repetition-v1` ; `BR_SORTIE=calcul/t07bbis-repetition-v2` (commentaire R12 sur la ligne d'avant), en-tête à jour ; essais qui citaient la v1 → v2. Bloc marqué `branche-de-sortie` (`branche_de_sortie_neuve`), **même texte dans les deux lanceurs**, appelé par `commande` des deux : lit `BR_SORTIE` et `DEPOT_URL_OFFICIEL` dans l'amorce envoyée (une fois exactement), exige que `origin` de RACINE soit ce dépôt (propriétaire/nom), puis `git ls-remote --exit-code origin refs/heads/<branche>` (lecture seule) : code 2 de l'outil (absente) → accepté ; 0 (présente) → « BBIS [REPETITION] REFUS : branche de sortie … présente sur le dépôt distant (R12) … », code 2 ; autre (injoignable) → refus, code 2. Course : son lanceur ne le faisait pas ; même contrôle ajouté (branche `donnees/t07-etape-b-bis-v1`), après la garde d'ancêtre. | `test_branche_de_sortie_neuve_exigee_avant_la_commande` : noms des deux amorces ; bloc identique ; sain (v1 présente, v2 absente ; course absente) ; branche présente, amorce de nom v1 contre un distant qui porte la v1, `BR_SORTIE` double, `origin` absent, `origin` d'un autre dépôt, distant injoignable → 2 ; câblage par `commande` de la répétition (sain 0, puis branche poussée → refus, aucune commande de création imprimée, aucun dossier laissé) ; câblage de la course dans `test_essai_local_sans_ecriture_et_garde_d_offre_de_la_commande`. Les essais de `commande` saine posent un distant nu jetable `…/lciric/controle-ia-travail.git` (`aide_t07bbis_depot_v1.distant_officiel`). |
| **M2** plafond | code inchangé ; commentaire d'usage de `scripts/lancer_repetition_bbis_v1.sh` : plafond R-2802 = **cumul** strictement sous 3 USD toutes passes comprises ; `commande` calcule une passe ; à chaque passe, la mère relève la dépense des passes faites et choisit l'échéance pour que cette dépense plus le coût maximal imprimé reste strictement sous 3 USD (dit dans le feu écrit). | — |
| **m1** comparaison d'entiers | cas ajoutés : 13.10 et 100.0 acceptés, 9.2 refusé (« pilote trop ancien : CUDA 9.2 »). | mutation « comparaison de texte » dans les deux amorces : **échoue** désormais. |
| **m2** ligne lue au journal | bloc `cuda-du-pilote` (les deux amorces) : `v=$(cuda_du_pilote "$1") \|\| arret "… illisible …" 2` ; `v=$(cuda_du_pilote "$1") \|\| { j "lignes « CUDA » lues dans l'en-tête : <au plus 3 lignes contenant CUDA, 200 caractères chacune>"; arret "… illisible …" 2; }`. | cas « CUDA Version: N/A » : code 2, la ligne brute est au journal ; mutation (journal retiré) : échoue. |
| **m4** arrêt « carte invisible (nvidia-smi, en-tête) » | faux `nvidia-smi` : `FAUX_ENTETE=echec` fait échouer l'appel sans argument ; étape 1 de la course mise dans un bloc marqué `carte-et-cuda` (mêmes lignes, aucun changement de comportement). | répétition : cas ajouté à `test_machine_carte_jeton_outils_et_torch` ; course : `test_carte_et_cuda_de_la_course_en_tete_en_echec_et_hote_ancien` (sain 13.0 ; en-tête en échec → 2 ; hôte à 12.8 → 2). |
| **m5** entier géant | `faute_cuda_hote` : `v = float(valeur)` ; `try: v = float(valeur)` / `except OverflowError: return "cuda_max_good non fini (entier hors de portée)"`. Les autres nombres de l'offre de recherche passent par `_nombre` (texte illisible, booléen, non fini ou hors de portée → « clé(s) … absente(s) ou illisible(s) »). | `10 ** 400` par `offre` et par `offre-depuis-recherche` de la course : code 2, motif, aucune trace de pile ; mutation : échoue. |
| **m6** motif près du seuil | `{v:g}` ; `{valeur!r}`. | 12.999999 → « cuda_max_good 12.999999 < 13 ». |
| **choix 4** offre de la course par programme | `registre_bbis_v1.py` : `lire_offre_de_recherche` (lecture des clés de l'outil, carte A100 SXM4 80 Go exactement, garde `cuda_max_good`) et `offre_construite` (forme de OFFRE.json), **communes** ; la répétition les appelle (`offre_depuis_recherche` du script réduite à l'identifiant ASCII, l'appel et la borne de prix ; messages gardés) ; la course a `offre_depuis_recherche` (identifiant ASCII, étiquette `bbis-t07-v1`, stockage sur 150 Go, puis `exiger_offre`) et la sous-commande `offre-depuis-recherche RECHERCHE.json ID OFFRE.json` (registre et `scripts/lancer_bbis_v1.sh`), fichier jamais réécrit (R12). | `test_offre_de_la_course_construite_par_programme_et_cuda_aux_bords` : sain (OFFRE.json écrit, puis `offre` → 0) ; R12 ; 12.8, clé absente, géant, 12.999999, carte PCIE, disque 100 Go, 8 cœurs, clé absente, texte illisible → 2, aucun fichier ; identifiants `78`, `077`, pleine largeur, espace → 2. Les essais de la répétition (`offre-depuis-recherche`) passent inchangés. |

## 2. Non corrigés (déclarés)

- **m3** (forme réelle de l'en-tête dans un conteneur, « N/A » possible) : rien à corriger dans le code. L'arrêt sur « N/A » est
  voulu (aucun défaut deviné). La répétition doit l'éprouver : elle pousse `nvidia-smi-entete.txt` dans ses traces (arrêt ou fin),
  et désormais la ligne lue au journal (m2). La mère lit ces traces avant le feu de la course, qui doit employer la même image.
- **m7** (deux « CUDA Version: » sur une même ligne, « 13.0abc » lu 13.0) : aucune sortie connue de l'outil n'a cette forme ;
  durcir ajouterait du code sans cas réel. Gardé tel quel.
- **m8** (outil 1.8.3 lu, la mère joue 1.11.0 ; `cuda_max_good` en texte pour une instance) : je ne peux pas lire 1.11.0 sans
  l'installer ; la garde ne s'applique qu'aux **offres** (nombre dans 1.8.3), jamais à une relecture d'instance. À vérifier par
  la mère : un `vastai search offers --raw` du jour donne un nombre (sinon refus écrit, gratuit, avant toute location).
- **m9** : la fiche de `CODE-BBIS` viendra sur le commit final.

## 3. Essais

- **Compte** (`PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_t07bbis_*.py tests/test_repetition_bbis_v1.py`,
  arbre de ce commit) : § 5.
- **Mutations** (copie jetable, non gardées) : comparaison de texte dans les deux amorces ; branche présente tolérée dans les
  deux lanceurs ; appel de la garde de branche retiré du lanceur de répétition ; `OverflowError` non rattrapée ; ligne lue
  retirée du journal : chacune fait échouer au moins un essai.

## 4. Empreintes qui changent

- `scripts/amorce_repetition_bbis_v1.sh` : `ba4aa32db3866328a529d374a0a18ab79368144f9e148bf71eed35be851c478d`.
- `scripts/amorce_bbis_v1.sh` : `4e1d77474bbd39e1d34800879fc2abfea7eb722de2d81ab3caa04faf70da7961`.
- `scripts/repetition_carte_bbis_v1.py` (`SCRIPT_SHA256` de la commande) : `4bbea0fae56660c687ef43d189f3bf40151ebc682059a9749bb1329f7259d221`.
- La commande de la répétition compare l'amorce du dossier à celle du commit : la passer avec le commit de cette correction.

## 5. Ligne de compte

**138 passed, 4 warnings in 188.30s (0:03:08)**, code 0 : 135 de la v1 plus 3 essais neufs
(`test_carte_et_cuda_de_la_course_en_tete_en_echec_et_hote_ancien`, `test_branche_de_sortie_neuve_exigee_avant_la_commande`,
`test_offre_de_la_course_construite_par_programme_et_cuda_aux_bords`) ; les autres corrections sont des cas ajoutés à des essais
existants. Arbre joué : celui de ce commit (seul ce rapport a été écrit après la passe).
