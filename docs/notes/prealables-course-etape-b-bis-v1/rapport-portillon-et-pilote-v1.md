# Préalables de la course de l'étape B bis de l'épreuve des sondes : plancher des 176 essais et pilote de la commande, v1

Date : 2026-11-18, de 03:08Z à 03:30Z. Calcul sur processeur seulement : aucune machine louée, aucun appel au loueur ni à
l'hébergeur, aucun commit ni poussée dans le dépôt de travail. Aucun résultat des travaux 7a, 7b, T0.6, étape B, étape B bis ni
P3-bis n'a été ouvert. Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/prealables-bbis/`.

## Verdict

- **Plancher des 176 essais : il NE PASSERAIT PAS.** Sur l'arbre que l'amorce extrait : **151 passés, 25 sautés, 0 échoué**
  (code 0 de pytest). L'amorce s'arrêterait à son étape 5, « 151 passés < 176 », **après** la minuterie, la lecture de la carte,
  le clonage, l'extraction de la sortie de 7b et l'installation des paquets de la carte (machine payée).
- Cause : la valeur 176 a été comptée sur **l'arbre complet de `main`** (R-3074 : « 176 réussites […] arbre complet sur
  `main` »), pas sur l'arbre partiel de la machine. L'en-tête de l'amorce le dit lui-même pour les versions 1 à 4 : sur la machine,
  l'essai de bout en bout (sauf un), l'état imposé et le lien « mots et coût » sautent.
- **Pilote de la commande : conforme.** Code de sortie 0, commande de création imprimée (2 lignes), amorce embarquée
  d'empreinte exacte `c8a9e812…`, aucun fichier laissé par l'essai local.
- **Deux autres arrêts plus loin dans la course, vérifiés sur l'arbre extrait** (voir « Écarts »). L'un ou l'autre arrêterait la
  marche à sa garde d'entrée, après la descente du modèle.

## 1. Ce que fait l'amorce (lu dans `scripts/amorce_bbis_v5.sh`, `c8a9e812…`)

- Clone **partiel** (`--filter=blob:none --no-checkout --single-branch --branch $BRANCHE_CODE`) depuis GitHub, puis extraction
  partielle sans cônes (lignes 151 à 178). Motifs : tous les fichiers de premier niveau ; `src/` ; `tests/conftest.py`,
  `tests/test_t07bbis_*`, `tests/aide_t07bbis_*` ; dans `scripts/`, **seulement** `amorce_bbis_v1` à `v4`, `lancer_bbis_v1` à `v4`,
  `enumerer_issues_bbis_v1.py`, `epreuve_niveau_deux_plis_bbis_v1.py` (chacun avec son compagnon) ; `prereg/T0.7-etape-B-bis-v1.md*`,
  `prereg/P3-consignes-v1.md*` ; `docs/sources/invites-2606.08892-v1/` ; `registres/t07-etape-b-bis-v1.md*`,
  `registres/t07-etape-b-bis/`, `registres/scellements-v1.md(.sha256)`, `registres/go-extraits/`. Exclus : `diag/*/lecture-sondes-t06.json*`,
  `scripts/extraire_mesures_epreuve_t06_v1.py`, `scripts/mots_et_cout_t06_*`. Jamais `docs/notes/`.
- Puis checkout de `COMMIT`, recopie des fichiers cités par le registre propre (`docs/notes/*` refusé : arrêt), recopie de la
  sortie de 7b (fichiers nommés) et des fichiers cités par sa configuration (`docs/notes/*` refusé : arrêt), commit local.
- Environnement : `python3 -m venv` (Python de l'image `python:3.11-bookworm`) puis `pip install -r requirements-gpu.txt`
  (= `requirements-cpu.txt` **plus** `requirements-donnees.txt`, soit `pypandoc_binary==1.17` en plus ; torch 2.14.1 en roue
  pour CUDA 13.0).
- Essais (l. 241) : `PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py --basetemp="$T/essais-tmp"`,
  depuis le dépôt extrait. Compte (l. 239, bloc `compte-des-essais`) : premier nombre suivi de « passed » dans la **dernière
  ligne** de la sortie ; puis `[ "$NP" -ge 176 ]` (l. 246), après avoir exigé le code 0 (l. 244). Le comptage n'est pas dans
  `src/controle_ia/t07bbis/`.

## 2. Reproduction de l'arbre

Script : `outils/simuler_arbre_instance_v2.sh` (`6c173538…`). Les motifs, le bloc de recopie des fichiers cités, le bloc du commit
local et le bloc du compte sont **lus dans le texte même de l'amorce** (rien de retapé) ; la ligne d'essais est celle de l'amorce.
Commandes :

```
bash outils/simuler_arbre_instance_v2.sh <dossier>/arbre-05cd22aa-machine-v2 05cd22aa15382f61eb62b9e7817890dde728dd5f main machine
bash outils/simuler_arbre_instance_v2.sh <dossier>/arbre-06c88328-machine-v2 06c8832819af344d01c184222833c5a42e8ac901 main machine
```

- Arbre extrait au commit `05cd22aa` : 484 fichiers (liste `arbre-05cd22aa-machine-v2/fichiers-sur-disque.txt`, `344b5b4b…` ;
  motifs lus `motifs-lus-dans-l-amorce.txt`, `0ac09142…`). 20 fichiers sous `scripts/` ; `docs/notes/` absent.
- Essais joués dans un espace de noms sans réseau (`unshare -n`), environnement vidé (`env -i`), avec les variables que la
  machine reçoit par `--env` et du loueur, en valeurs factices (aucune clé).
- Environnement Python : `/home/user/controle-ia-travail/.venv` (Python 3.13.18, paquets de `requirements-cpu.txt`).

## 3. Résultat des essais

Ligne de compte (`essais.txt`, `37405aad…`) : `151 passed, 25 skipped, 4 warnings in 181.97s`. Même compte au commit `06c88328`
(`d8c3fe64…`), avec les mêmes 25 sauts, ligne pour ligne. Rien n'est écrit sous `src` ni sous `tests`. Les 4 avertissements sont
des avertissements de fourche (`fork()`), comme dans R-3074.

Les 25 sauts :

**A. « chaîne de T0.6 absente de ce clone » (17 essais).** L'aide `tests/aide_t07bbis_jouet_v1.py` (l. 13 et 31-32) exige
`docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json`. L'amorce n'extrait jamais `docs/notes/`, et ses deux boucles de
recopie **arrêtent** la course si un fichier cité est sous `docs/notes/`. Sur la machine, ce fichier ne peut donc **jamais** être
présent.
- `test_t07bbis_bout_en_bout_v1.py` (8) : `test_marche_jouet_ecrit_des_scores_fermes_sans_aucune_aire`,
  `test_lecture_jouet_de_bout_en_bout_et_ecriture_scellee`, `test_lecture_unique_et_cle_de_b_bis_dans_le_registre_partage_refusees`,
  `test_verdict_de_p3bis_autre_que_vu_rien_n_est_lu`, `test_marche_reelle_refusee_hors_instance_ou_sans_registre`,
  `test_table_conjointe_de_bout_en_bout`, `test_empreintes_des_scores_et_des_deux_premieres_directions_sain_et_artefact`,
  `test_commit_local_des_entrees_et_arret_ecrit_sur_une_course_jouet`.
- `test_t07bbis_controle_v2.py` (1) : `test_marche_v2_de_bout_en_bout_en_mode_jouet`.
- `test_t07bbis_controle_v3.py` (1) : `test_marche_v3_et_lecture_v2_de_bout_en_bout_en_mode_jouet`.
- `test_t07bbis_etat_impose_v1.py` (6) : `test_chemin_impose_trois_cas_sains_au_bit_pres_et_artefact`,
  `test_chemin_impose_artefact_serie_o_alteree_arret`, `test_series_imposees_jumeau_differe_de_l_origine_et_nu_egal_a_l_origine`,
  `test_etat_impose_artefacts_dose_et_empreinte`, `test_texte_decode_ou_cle_autre_arret`,
  `test_garde_d_equivalence_sain_et_activations_decalees`.
- `test_t07bbis_second_addendum_v1.py` (1) : `test_F_marche_v4_et_lecture_v3_de_bout_en_bout_en_mode_jouet`.

**B. « code de la pièce absent de cet arbre (instance : extraction partielle) » (7 essais)**, saut de tout le fichier
`test_t07bbis_lien_mots_et_cout_v1.py` : il exige `scripts/mots_et_cout_t06_v3.py`, que le motif `!/scripts/mots_et_cout_t06_*`
exclut. Essais : `test_chargement_sain_et_interface`, `test_charger_adaptateur_par_le_lien_et_choix_de_la_lecture`,
`test_artefacts_module_ligne_fichier_commit`, `test_fils_de_calcul_a_un_exiges`, `test_modele_non_calculable_de_la_piece_aucun_score`,
`test_fichiers_reels_de_la_branche`, `test_egalite_adaptateur_et_repli_base_a_et_ecarts_declares_base_b`.

**C. « fabrique factice de la pièce absente de cet arbre » (1 essai)** : `test_controle_d_egalite_de_bout_en_bout_piece_jouet_contre_adaptateur`
(exige `scripts/fabrique_factice_mots_et_cout_t06_v1.py`, hors des motifs).

Le saut unique du clone de la mère est autre chose : `test_fichiers_reels_de_la_branche` saute sur « commit cité absent de ce
clone ». Le commit cité `da06bb57` n'est pas dans l'histoire superficielle de la mère. Il n'est donc pas question ici d'histoire
complète : avec une histoire complète, la machine ferait toujours 151.

**Ce qui décide** : les 25 sauts dépendent de fichiers que l'amorce n'extrait pas, et qu'elle interdit même pour deux d'entre eux.
Le plancher atteignable sur cet arbre est 151. Seule une amorce neuve peut corriger cela, ce qui demande une version nouvelle
(R12), soit avec le plancher à 151, soit avec d'autres motifs. Or le code est gelé : la garde de création exige exactement deux
fiches de code (projet de feu v3, § 3). C'est donc un nœud pour Lazar.

## 4. Pilote de la commande (R-3095 rejoué)

Script : `outils/pilote_commande_v1.sh` (`a5f4ee2a…`). Lanceur `scripts/lancer_bbis_v5.sh` (`ebd44e84…`) joué depuis une copie
jetable du dépôt prise à la tête de `main`, `58d3d0ed` à 03:19Z (sparse : scripts v5, `src/`, registres de B bis), avec
`AMORCE_ESSAI_LOCAL=1`, sous `unshare -n`. Arguments : `commande <copie> offre-fabriquee.json 87654321 05cd22aa… prep/t07bbis-code-v1
20261111-151701-t06-reel calcul/t06-confirmation-7b-v1 20261118-031935-bbis-v2 <maintenant+13 h> "<texte de feu-bbis-v2.txt>" 2 python:3.11-bookworm`.
Offre fabriquée (`52d6f5c8…`) : A100 SXM4 80GB, 1,10 USD/h, 32 cœurs, 257 000 Mo, 150 Go, stockage 0,0247 USD/h, CUDA 13.0.

- **Code de sortie 0** ; sortie d'erreur vide ; commande de création **imprimée** (`sortie-commande.txt`, `87439a86…`, 2 lignes :
  l'en-tête avec l'empreinte courte `c8a9e81266a3b2fd`, puis la ligne de création avec `GO_ID=GO-2026-11-14-09`, l'offre 87654321,
  l'image, le disque de 150, l'étiquette `bbis-t07-v1` et les variables). Le base64 décodé redonne exactement l'amorce `c8a9e812…`.
  Le dossier temporaire de l'essai local est vide après coup.
- Gardes passées dans l'ordre : offre ; amorce en essai local ; création (trois lignes au registre propre, feu portant les deux
  numéros d'accord, deux relances, deux lignes de fiche de code) ; ancêtre ; branche de sortie absente.
- **Réseau** : un seul geste du pilote sortirait sur le réseau, le contrôle de la branche de sortie (`git ls-remote origin`, en
  lecture seule, vers GitHub). Rien ne crée de machine ni n'appelle le loueur. Pour ne rien appeler, l'« origin » de la copie
  est un dépôt nu local et vide, nommé `…/lciric/controle-ia-travail.git`. Le nom contrôlé par le lanceur est donc le bon, mais
  **l'absence de la branche de sortie sur le vrai distant n'est pas reprouvée ici**. La garde de calcul n'a rien bloqué : aucune
  commande ne la sollicitait.

## 5. Écarts entre la machine et ce qui a été mesuré

1. **Le commit passé à l'amorce** (décisif pour la marche, pas pour les essais). Le projet de feu v3 et `feu-bbis-v2.txt`
   donnent `COMMIT=05cd22aa`. À ce commit, le registre propre extrait n'a que `SCELLEMENT-BBIS` et `ABSENCE-B-BBIS`, et
   `registres/t07-etape-b-bis/` n'a pas la fiche `code-bbis-v2.json`. Le rejeu en lecture seule des contrôles d'entrée de la marche
   (`outils/garde_entree_fichiers_v1.py`, `7b08807d…`, fonctions mêmes du code de la course) rend :
   « ligne CODE-BBIS absente (exigée) ; ligne GO-BBIS absente (exigée) » (`garde-entree-05cd22aa.json`, `385377c7…`). Le lanceur
   ne voit pas cette faute : il lit le registre de la mère, et `05cd22aa` est ancêtre de lui-même. Pour la course v1, le commit de
   la course (`31fa8ac6`) était postérieur à celui de la fiche (`ce470564`).
2. **Fichiers de la fiche absents de l'arbre** (même à un commit qui porte les lignes, ici `06c88328`). La fiche
   `code-bbis-v2.json` cite 63 fichiers ; **11 ne sont pas extraits** par les motifs de l'amorce v5 : `scripts/amorce_bbis_v5.sh`,
   `scripts/lancer_bbis_v5.sh`, `scripts/amorce_repetition_bbis_v1.sh` à `v3`, `scripts/lancer_repetition_bbis_v1.sh` à `v3`,
   `scripts/repetition_carte_bbis_v1.py` à `v3`. La garde d'entrée de `marche_v4` (l. 228-231) s'arrête au premier :
   « scripts/amorce_bbis_v5.sh : fichier du code cité par la fiche de CODE-BBIS absent : arrêt (R11) »
   (`garde-entree-06c88328.json`, `639af278…`). Cas sain de l'outil : sur l'arbre complet de la mère, les 63 fichiers sont présents
   et rien ne s'arrête (`garde-entree-cas-sain-arbre-complet.json`, `0e8e59da…`). Ces deux points ne jouent qu'après le plancher
   des 176, qui arrête la course avant.
3. Histoire : le clone de la machine est partiel mais a toute l'histoire ; la simulation est superficielle (source superficielle)
   et a tous ses objets. Aucun des 25 sauts n'en dépend.
4. Sortie de 7b (étape 3) non jouée : la branche `calcul/t06-confirmation-7b-v1` est absente localement, et rien de 7b n'a été lu.
   Elle ne peut pas rendre les fichiers manquants (refus de `docs/notes/*` ; les motifs ne bougent pas).
5. Environnement : sur la machine, Python 3.11, torch construit pour CUDA 13.0 avec une carte visible, et `pypandoc_binary` en
   plus ; ici, Python 3.13, torch sur processeur. Aucun essai de B bis ne saute ni ne bifurque sur la présence de la carte ; le
   seul essai qui nomme « cuda » s'arrête avant de toucher l'appareil.
6. Variables de la machine : jouées en valeurs factices. Le compte serait-il le même sans elles ? Non mesuré (une seule
   configuration jouée, deux commits).

## 6. Limites

- Pas de machine : le plancher est mesuré sur une reproduction de l'arbre, pas sur la carte.
- Incident à déclarer, de mon fait. Ma première simulation (`simuler_arbre_instance_v1.sh`, `2feb062c…`, abandonnée) clonait
  avec `--filter=blob:none` depuis la source locale, qui est superficielle. Le serveur local a ignoré le filtre et chaque objet
  manquant a lancé un chargement complet : environ 1 300 chargements, près de 5 000 processus, la mémoire presque épuisée vers
  03:11-03:14Z. **Le noyau a tué au moins un processus pour manque de mémoire ; il peut appartenir à une autre tâche de la
  session.** Arrêtée par l'identifiant de sa tâche ; après coup, aucun processus restant n'a été trouvé. La v2 clone sans
  filtre ; l'arbre extrait est le même.
- Disque : deux clones jetables supprimés après usage ; reste 1,7 Go dans le dossier (le clone de la simulation au commit `05cd22aa`).
