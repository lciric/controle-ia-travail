# Préenregistrement — addendum 1 aux trois analyses scellées de R1 et R2 : gardes de réception de la relance v4 de R1 (`texte`, `table-comparee`, `provenance`), versions neuves du code — v1 — brouillon 1

- Auteur : rédacteur-développeur neuf (sous-agent, Claude Fable 5.1), étape F de R1 v4, consigne
  `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/consigne-developpeur-gardes-analyses-r1-v4-v1.md`. Je n'ai écrit ni les trois
  analyses, ni leur code, ni l'addendum v4 de R1, ni la fiche de réception v4 ; je n'ai lu aucune sortie de la relance v4.
- Date (UTC) : 2026-11-05, 16:31 (`date -u`).
- Commit du code : <<COMMIT_CODE>> (commit unique qui porte les versions neuves du code, leurs essais et ce texte ; à
  remplir au scellement, seul marqueur de ce texte).
- Documents qui font foi (chemin + empreinte) : addendum v4 de R1, scellé, `prereg/R1-addendum-relance-v4.md`
  (`0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8`, branche `prep/r1-relance-v4`, commit de
  scellement `937f13177892933955c9c34839b4b45a4db745df`), Plan d'analyse, étape 4, paragraphe « Analyses (inchangées) »
  (cité en entier ci-dessous) ; fiche de réception v4 de conv-audit, scellée,
  `docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/fiche-reception-r1-v4-v2.md`
  (`605931f3dba3a6f9aa413cbac924794b6ba6577627d571d61f8d86a34d2f638f`), section 6 et section 4.4 (mêmes attendus) ;
  les trois textes scellés, inchangés : analyse principale `prereg/analyse-principale-r1-r2-v1.md`
  (`8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537`, code cité `a8b7fdb2`), analyse secondaire
  `prereg/analyse-blanche-noire-v3.md` (`1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9`, code cité
  `326601cf`), lecture par épisode `prereg/analyse-par-episode-v1.md`
  (`26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4`, code cité `5f2f9bf5`) ; `src/controle_ia/prereg.py`
  (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`) ; gabarit `prereg/gabarit-preregistrement-v1.md`.
- Statut : brouillon 1, non scellé ; à contre-lire par un sous-agent neuf (R2) ; scellé selon la procédure du Plan
  d'analyse, point 0, avant toute récupération de `calcul/r1-r2-reel-v1` dans l'arbre des analyses.

## Objet, portée et ce que cet addendum ne fait pas

Cet addendum **unique** complète les trois analyses scellées de R1 et R2 (principale, secondaire, par épisode) pour la
relance v4 de R1, sur un seul point : leurs **gardes de réception** du run de rejeu, que l'addendum v4 de R1 exige de
mettre à jour « par conv-audit, de son côté ». Il met en place, par des **versions neuves du code** (R12 : rien
d'existant modifié), les trois gardes `texte`, `table-comparee` et `provenance`, exactement comme l'addendum v4 les
écrit, et rien d'autre dans le calcul. Les textes des trois analyses ne bougent pas : hypothèses, prédictions chiffrées,
métriques, seuils, plans de calcul, critères de lecture gelés et listes d'arrêt restent ceux des textes scellés — sauf une règle de leurs listes d'arrêt, le « second passage », remplacée pour la seule course v4 par le point 6 du Plan d'analyse (écart déclaré, nœud de Lazar) —, dits
tels quels aux sections correspondantes de ce texte. Ce que cet addendum ne fait pas : il ne change aucune graine, aucun
bras, aucune couche, aucun taux, aucune agrégation, aucune ligne des tables gelées ; il n'ajoute aucune lecture ; il ne
lit aucune donnée.

## Motif : l'addendum v4 de R1, paragraphe cité

`prereg/R1-addendum-relance-v4.md` (`0f10881b…`), Plan d'analyse, étape 4 — versement et réception, dernier
paragraphe, recopié tel quel :

> **Analyses (inchangées).** Les textes des analyses principale, secondaire et par épisode de conv-audit ne bougent pas.
> Leurs gardes de réception, à mettre à jour **par conv-audit, de son côté**, devront exiger : **`texte`** — le texte qui
> gouverne, lu dans `preenregistrement` du manifeste, est ce texte scellé (chemin et empreinte), non l'addendum v3 ;
> **`table-comparee`** — `tokenisation.table_sha256` est comparée à l'empreinte du sceau de la table v4 versée avec le run
> **et** à celle que la table cite comme résultat de réparation (`resultat_reparation_sha256` égal au sceau du résultat de
> la réparation versé) : l'empreinte n'est plus connue d'avance (V4-E5), elle est fixée par la chaîne scellée ;
> **`provenance`** — `tokenisation.addendum` = `prereg/R1-addendum-relance-v4.md` à l'identique (V4-E14), et commande
> `rejeu_activations_v4`.

La fiche de réception v4 (section 6) rappelle les mêmes trois gardes, avec les mêmes attendus, et dit qu'elle ne les
modifie pas. Les « attentes de réception » de l'étape 4 fixent les valeurs comparées : `preenregistrement.chemin` =
`prereg/R1-addendum-relance-v4.md`, `preenregistrement.sha256` = empreinte de l'addendum v4 scellé (`0f10881b…`) ;
`commande` = `python -m controle_ia.runs_nuit.rejeu_activations_v4` ; `tokenisation.table_sha256` = empreinte du sceau
de `prereg/R1-table-tokenisation-v4.json` versé avec le run ; `tokenisation.addendum` = `prereg/R1-addendum-relance-v4.md`.

## Déclaration : aucune donnée de R1 v4 lue

Ce texte et son code ont été écrits sans ouvrir `calcul/r1-r2-reel-v1` (présente dans le dépôt du canal comme référence distante `origin/calcul/r1-r2-reel-v1`, tête du 5 novembre 2026 à 02:36 UTC, comme `origin/calcul/r1-v4-reparation-reel-v1` : objets présents, aucun fichier extrait, affiché ni lu ; aucun
fichier de `runs/20261105-021737-r1-v4-rejeu-reel`, `runs/20261104-234729-r1-v4-reparation-reel`,
`runs/20261104-091009-r1-v4-temoin-reel` ni de leurs `diag/` et `donnees/` ouvert ; seuls leurs **noms** sont connus,
par la consigne), sans lire aucune sortie de la relance v4, sans rien lire sous `donnees/`, et sans exécuter aucune
commande décisive. Les essais tournent sur données synthétiques seulement. Les trois sorties des analyses de la course
v3 de R1 (`runs/20261103-072723-…`, `20261103-072805-…`, `20261103-072840-…`) n'ont été ouvertes que pour les clés
`commande`, `preenregistrement`, `decisif` de leurs manifestes (jamais leurs résultats) par le rédacteur. Ces résultats ont été lus et jugés par conv-audit et Lazar (verdicts R13 du 3 novembre 2026, R-1322) : la course v4 n'est pas aveugle à la course v3 ; la seule liberté qu'elle laisserait, la graine, est fixée par les textes (Plan, point 4), et le calcul, les seuils et les critères sont gelés depuis le 2 novembre.

## Hypothèse

Inchangée, dite telle quelle : pour chacune des trois analyses, l'hypothèse est celle de son texte scellé, section
« Hypothèse » — analyse principale (`8e267952…`), analyse secondaire (`1f6a6da2…`), lecture par épisode (`26a3ff72…`).
Cet addendum n'en ajoute, n'en retire ni n'en modifie aucune. Il ne porte aucune hypothèse propre : une garde de
réception est un contrôle d'intégrité de la chaîne scellée du fournisseur, pas une prédiction sur les données.

## Prédiction chiffrée et signe attendu

Inchangées, dites telles quelles : les prédictions de chaque analyse (P-R1 à P-R5 de la principale ; H-BN et la table
des prédictions de la secondaire ; P-E1 à P-E7 de la lecture par épisode), avec leurs signes, leurs ordres de grandeur
et ce qui compterait comme réfutation, sont celles des trois textes scellés, sections « Prédiction chiffrée et signe
attendu ». Cet addendum n'en change aucune. Attendu mécanique propre aux gardes (ce n'est pas une prédiction
scientifique) : sur une course de la relance v4 reçue conforme à la fiche de réception v4 (gardes `texte`,
`table-comparee`, `provenance` de la fiche passées), les trois gardes des analyses passent aussi, puisqu'elles comparent
les mêmes clés aux mêmes attendus ; une garde des analyses qui s'arrête sur une course reçue conforme signale un écart
entre la fiche et le code des analyses, et c'est un nœud de Lazar (R4 : audit), jamais une lecture.

## Métrique

Inchangée, dite telle quelle : rappel par action à taux de fausse alarme fixé, aires et différences appariées de la
principale ; aire d'épisode, puissance et différences de Holm de la secondaire ; rappel par épisode de la lecture par
épisode — définitions, estimateurs, intervalles et niveaux de chaque texte scellé, section « Métrique ». Aucune métrique
n'est ajoutée ; ce qu'écrivent les gardes dans la sortie (`reception_v4` : chemins, empreintes, commande, clé
`tokenisation.addendum`) ne contient aucun nombre de résultat et n'est jamais lu comme une mesure.

## Seuil

Inchangé, dit tel quel : seuils de décision et taux d'erreur de chaque texte scellé, section « Seuil » (1 % de fausses
alarmes et niveau 97,5 % avec Bonferroni à deux pour la principale ; 0,05 et Holm à quatre pour la secondaire ; rang 1
sur 49 et niveau 97,5 % pour la lecture par épisode). Les gardes n'ont pas de seuil : une comparaison d'empreintes ou de
chaînes est vraie ou fausse ; fausse, elle arrête.

## Plan d'analyse

0. **Mise en place et ordre de scellement** (même procédure que les textes, adaptée à un addendum unique) :
   0. L'entrée « Contre-lecture 1 » est écrite dans le brouillon final ; il n'y reste qu'un marqueur, la ligne « Commit
      du code ». L'empreinte du brouillon final contre-lu est inscrite au registre de conv-audit et poussée.
   a. Committer sur la branche de travail (`canal/conv-audit-n04`) les versions neuves du code (liste fermée de chaque
      analyse ci-dessous, empreintes inchangées), leurs essais, ce texte (brouillon final), le rapport du
      rédacteur-développeur et les différentiels : ce commit est le **commit cité** (premier commit qui porte le brouillon final et le code à ses empreintes finales ; le commit `c82dafeb`, qui porte le brouillon 1 et le code d'avant la contre-lecture, ne l'est pas ; ni amendé
      ni refait).
   b. Copier le brouillon final sous `prereg/addendum-1-gardes-analyses-r1-v4-v1.md` (chemin gelé par
      `constantes_v6.ADDENDUM`, `constantes_v7.ADDENDUM`, `analyse_blanche_noire.constantes_v4.ADDENDUM`), n'y remplacer
      que le marqueur du commit cité (40 caractères de `git rev-parse HEAD` après l'étape a), vérifier par `diff` que
      seule cette ligne diffère et que `controle_ia.prereg.problemes` est vide, sceller par
      `controle_ia.prereg.sceller_prereg` ; committer le texte scellé et son compagnon, seuls.
   c. **Ordre** : ce texte est scellé **avant** toute récupération de `calcul/r1-r2-reel-v1` dans l'arbre des analyses
      (aucune extraction de ses fichiers — `git checkout`, `git show`, `git diff`, `git log -p` — ni aucune lecture avant le scellement ; la référence distante déjà présente n'est pas ouverte) ; les trois textes des
      analyses restent scellés et inchangés (vérifiés par chemin et empreinte au lancement, `exiger_texte`) ; la
      condition de la secondaire (texte de la principale scellé et sa concordance vérifiée par un lecteur neuf, étape 0.g
      de son texte) est déjà remplie depuis le 2 novembre 2026 (R-1101, R-1096).
   d. Arbre de travail séparé au commit du scellement (`git worktree add -b analyses-r1-v4 <dossier> <commit>`) ;
      environnement `.venv` gelé (Python 3.13.18, numpy 2.4.6, scipy 1.17.1 : les trois codes le vérifient). Récupérer
      par la seule refspec `git fetch origin calcul/r1-r2-reel-v1`, puis `git checkout FETCH_HEAD -- <chemins>` pour
      les seuls chemins `runs/20261105-021737-r1-v4-rejeu-reel`, `diag/20261105-021737-r1-v4-rejeu-reel`,
      `runs/20261104-234729-r1-v4-reparation-reel`, `diag/20261104-234729-r1-v4-reparation-reel`,
      `prereg/R1-table-tokenisation-v4.json` et son compagnon `.sha256` ; les juges `20261102-004328-r2-juge3b-reel` et
      `20261102-005048-r2-juge8b-reel` sont déjà dans la branche ; les fichiers `donnees/<run>/…` (trois `.npz` du rejeu,
      deux `.npz` des juges, données de P3) sont écrits sans passer par l'index (`git show FETCH_HEAD:<chemin> >
      <chemin>`), vérifiés par leurs compagnons sans ouvrir aucun `.npz` ; commit des seuls chemins suivis ; `git status
      --porcelain --untracked-files=all` vide ; jamais de `git merge` de la branche de résultats. Le témoin
      `20261104-091009-r1-v4-temoin-reel` n'est lu par aucune analyse : il n'est pas récupéré.
   e. **Fiches de réception** (R12 : les fiches de la course v3, `prereg/fiche-reception-principale-r1-r2-v1.json` et
      `prereg/fiche-reception-blanche-noire-v3.json`, restent scellées et inchangées) : écrire deux fiches neuves, de
      **mêmes formats et mêmes clés** (`format` = `fiche-reception-principale-r1-r2-v1`, resp.
      `fiche-reception-blanche-noire-v3`, seuls formats acceptés par le code), sous
      `prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json` et
      `prereg/fiche-reception-blanche-noire-v3-relance-v4.json` : `R1` = fichiers et résultat du run
      `20261105-021737-r1-v4-rejeu-reel`, `R2` = les deux juges (inchangés), `R4` nul pour la secondaire, aucun nombre de
      résultat ; sceller et committer chacune seule, arbre propre. La lecture par épisode lit la fiche de la principale.
   f. **Commandes décisives**, dans l'ordre, chacune depuis la racine de l'arbre séparé, arbre propre, ses sorties
      committées avant la suivante, sorties standard et d'erreur redirigées vers un journal non affiché (seul le code de fin est lu avant la commande suivante ; sur code non nul, le seul message d'arrêt est lu, il ne porte aucune valeur), journal scellé et committé avec les sorties ; aucune issue n'est lue avant que les trois sorties soient committées et poussées (point 1 de chaque analyse ci-dessous) : principale (code v6) ; lecture par épisode
      (code v7, qui lit le résultat scellé de la principale) ; secondaire (code v4).
   Préalable aux commandes décisives : réception v4 conforme selon la fiche v4 (`verifier_reception_r1_v4_v1.py` en code 0, recalcul de la table égal à l'octet, section 7), consignée au registre avec ce qui a été vu avant les analyses (fiche v4, section 6). Une vérification qui échoue : ne pas lancer, signaler à Lazar.
1. **Avant → après, pour chacune des trois analyses** (seules lignes du Plan d'analyse qui changent ; tout le reste de
   chaque plan est inchangé, dit tel quel) :
   - **Analyse principale** (`8e267952…`). Code : avant, liste fermée v2 du texte (7 modules du paquet, 2 essais, 9
     modules réutilisés ; commande `lecture_v2`) ; après, cette liste reprise sans modification plus `constantes_v6.py`,
     `entrees_v4.py`, `lecture_v6.py` et l'essai `tests/test_analyse_principale_r1_r2_v6.py` (bloc « analyse principale
     (code v6) » ci-dessous). Commande décisive : avant, `PYTHONPATH=src python -m
     controle_ia.analyse_principale_r1_r2.lecture_v2 --fiche prereg/fiche-reception-principale-r1-r2-v1.json
     --run-analyse <AAAAMMJJ-HHMMSS>-analyse-principale-r1-r2-v1 --prereg prereg/analyse-principale-r1-r2-v1.md` ; après,
     `PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v6 --fiche
     prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json --run-analyse <AAAAMMJJ-HHMMSS>-analyse-principale-r1-r2-v1
     --prereg prereg/analyse-principale-r1-r2-v1.md`. Sorties : mêmes noms (`runs/<run>/manifeste.json`,
     `diag/<run>/analyse-principale-r1-r2-v1.json` et `.md`), avec en plus la clé `reception_v4` (ce que les gardes ont
     comparé) et, dans `lien_au_preenregistrement`, l'entrée `addendum`. Tests attendus : avant 24 ; après **28** (20 +
     4 + 4 : `tests/test_analyse_principale_r1_r2_v1.py`, `_v2.py`, `_v6.py`).
   - **Analyse secondaire** (`1f6a6da2…`). Code : avant, liste fermée de la version 3 (12 modules du paquet, 2 essais,
     13 réutilisés ; commande `lecture_v3`) ; après, cette liste reprise sans modification plus `constantes_v4.py`,
     `entrees_v4.py`, `lecture_v4.py` du paquet `analyse_blanche_noire` et l'essai `tests/test_analyse_blanche_noire_v4.py`
     (bloc « analyse secondaire (code v4) ») ; la fermeture des importations de `lecture_v4` est exactement cette liste
     (aucun module du paquet principal : éprouvé). Commande décisive : avant, `PYTHONPATH=src python -m
     controle_ia.analyse_blanche_noire.lecture_v3 --fiche prereg/fiche-reception-blanche-noire-v3.json --run-analyse
     <AAAAMMJJ-HHMMSS>-analyse-blanche-noire-v3 --prereg prereg/analyse-blanche-noire-v3.md` ; après, `PYTHONPATH=src nice
     -n 10 python -m controle_ia.analyse_blanche_noire.lecture_v4 --fiche
     prereg/fiche-reception-blanche-noire-v3-relance-v4.json --run-analyse <AAAAMMJJ-HHMMSS>-analyse-blanche-noire-v3
     --prereg prereg/analyse-blanche-noire-v3.md`. Sorties : mêmes noms (`diag/<run>/analyse-blanche-noire-v3.json` et
     `.md`), plus `reception_v4` et `lien_au_preenregistrement.addendum`. Tests attendus : avant 13 (version 3) ; après
     **17** (13 + 4 : `tests/test_analyse_blanche_noire_v3.py`, `_v4.py`) ; les 12 essais v1 et 11 essais v2 passent
     toujours (40 en tout).
   - **Lecture par épisode** (`26a3ff72…`). Code : avant, liste fermée v5 (13 modules du paquet, 4 essais, 9 réutilisés ;
     commande `lecture_v5`) ; après, cette liste reprise sans modification plus `constantes_v6.py`, `entrees_v4.py`,
     `lecture_v6.py` (modules de la principale que ce code lit pour les gardes et leurs constantes), `constantes_v7.py`,
     `lecture_v7.py` et les essais `tests/test_analyse_principale_r1_r2_v6.py`, `tests/test_analyse_par_episode_v7.py`
     (bloc « analyse par épisode (code v7) »). Le nom `v7` suit `v6`, pris par la principale dans le même paquet (R12 :
     un nom par version, jamais deux). Commande décisive : avant, `PYTHONPATH=src nice -n 10 python -m
     controle_ia.analyse_principale_r1_r2.lecture_v5 --fiche prereg/fiche-reception-principale-r1-r2-v1.json --principale
     diag/<run principal>/analyse-principale-r1-r2-v1.json --run-analyse <AAAAMMJJ-HHMMSS>-analyse-par-episode-v1 --prereg
     prereg/analyse-par-episode-v1.md` ; après, `PYTHONPATH=src nice -n 10 python -m
     controle_ia.analyse_principale_r1_r2.lecture_v7 --fiche prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json
     --principale diag/<run principal, code v6>/analyse-principale-r1-r2-v1.json --run-analyse
     <AAAAMMJJ-HHMMSS>-analyse-par-episode-v1 --prereg prereg/analyse-par-episode-v1.md`. Sorties : mêmes noms
     (`diag/<run>/analyse-par-episode-v1.json` et `.md` ; le rendu, repris du code v5, garde son titre « (code v5) » et
     écrit la version « (code v7) » à côté), plus `reception_v4` et `lien_au_preenregistrement.addendum`. Tests attendus :
     avant 54 (12 + 18 + 24) ; après **61** (12 + 18 + 3 + 28 : `tests/test_analyse_par_episode_v1.py`, `_v2.py`, `_v7.py`,
     et les 28 de la principale).
2. **Les trois gardes, exactement comme l'addendum v4 les écrit** (`analyse_principale_r1_r2.entrees_v4.exiger_reception_v4`,
   appelée par `lecture_v6` et `lecture_v7` ; `analyse_blanche_noire.entrees_v4.exiger_reception_v4`, même règle recopiée,
   appelée par `lecture_v4`), lues sur le résultat scellé du rejeu que cite la fiche (`diag/<run>/rejeu-activations.json`,
   rattaché par `verifier_resultat` à `runs/<run>/manifeste.json`), **juste après** la lecture de la fiche, **avant** le chargement de P3 et de R1 par les chargeurs
   inchangés (`entrees_v1.charger_r1`, resp. `entrees_v3.charger_activations_v3` : aucun `.npz` ouvert avant elles), des juges,
   la création du manifeste et tout calcul ; dans l'ordre de l'addendum v4 ; la première qui manque arrête tout
   (`GardeArret`, motif écrit, rien n'est lu) :
   - `texte` : `preenregistrement` du manifeste du rejeu égal, clé à clé, à `{"chemin": "prereg/R1-addendum-relance-v4.md",
     "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"}` (constante `ADDENDUM_V4`) ; sinon arrêt
     « garde texte : le texte qui gouverne le rejeu ≠ addendum v4 scellé » (l'addendum v3, ou tout autre texte, est refusé) ;
   - `table-comparee` : `tokenisation.table_sha256` du résultat du rejeu égal au **sceau** de la table v4 versée avec le run,
     `prereg/R1-table-tokenisation-v4.json` (compagnon `.sha256` vérifié par `scellement.verifier`, qui arrête si le
     compagnon manque ou ne correspond pas), **et** `resultat_reparation_sha256`, lu dans la table, égal au **sceau** du
     résultat de la réparation versé, `diag/20261104-234729-r1-v4-reparation-reel/resolution-graine-lot-v3-reparation.json`
     (compagnon vérifié ; le fichier est haché, jamais lu) ; sinon arrêt « garde table-comparee : … » ; de la table, seule
     la clé `resultat_reparation_sha256` est lue ;
   - `provenance` : `tokenisation.addendum` égal à `prereg/R1-addendum-relance-v4.md` à l'identique (V4-E14), et
     `commande` du manifeste du rejeu égale à `python -m controle_ia.runs_nuit.rejeu_activations_v4` ; sinon arrêt
     « garde provenance : … ».
   Un résultat de rejeu sans clé `tokenisation` arrête (« sans clé tokenisation »). Aucune valeur de couverture ni de
   fidélité n'est écrite par ces gardes ; ce qu'elles écrivent (`reception_v4`) : nom du run de rejeu, empreinte de son
   manifeste, `preenregistrement` et `commande` relus, chemin et sceau de la table, chemin et sceau du résultat de la
   réparation, `tokenisation.addendum` et `tokenisation.table_sha256` relus.
3. **Ce que l'addendum unique impose au mode décisif de chaque version neuve, et pourquoi** (différentiel hors renommage
   de chaque `lecture_v*`, versé avec le rapport) : (a) le texte passé à `--prereg` est le texte scellé qui gouverne,
   exigé par chemin et par empreinte (`exiger_texte`, constante `TEXTE`) : l'addendum ne le remplace pas ; ses graines
   (Q9 : 128 premiers bits de l'empreinte de ce texte), sa liste fermée (toujours vérifiée sur le texte, par le code de
   la version précédente), son calcul, son issue et son rendu sont repris sans modification ; (b) l'addendum unique,
   chemin gelé `prereg/addendum-1-gardes-analyses-r1-v4-v1.md`, est exigé scellé et conforme, et porte la liste fermée
   de la version neuve dans un **bloc propre à chaque analyse**, lu de sa ligne de titre (titres gelés :
   `### Liste fermée du code — analyse principale (code v6)`, `### Liste fermée du code — analyse par épisode (code v7)`,
   `### Liste fermée du code — analyse secondaire (code v4)`) à la ligne de titre suivante, parce que trois listes dans un
   seul texte ne peuvent pas être lues par la citation des textes (une liste contient l'autre) ; l'empreinte des
   constantes de la version neuve est citée une fois dans l'addendum (« Empreinte des constantes (analyse principale,
   code v6) : … », etc.) ; (c) **premier passage sous l'addendum** : aucun manifeste sous `runs/` ne cite l'addendum
   (chemin ou empreinte) avec la commande de ce code ; un manifeste illisible qui cite l'addendum arrête ; les manifestes
   des deux autres analyses sous le même addendum (autre commande) et les passages antérieurs de chaque texte sous son
   code antérieur (course v3 de R1 : `20261103-072723-analyse-principale-r1-r2-v1`, `20261103-072805-analyse-par-episode-v1`,
   `20261103-072840-analyse-blanche-noire-v3`, manifestes décisifs qui citent les textes par chemin et empreinte) ne
   comptent pas, **par liste fermée** : les trois manifestes de la course v3, `runs/20261103-072723-analyse-principale-r1-r2-v1` (`0587c398…`), `runs/20261103-072805-analyse-par-episode-v1` (`79f2a758…`), `runs/20261103-072840-analyse-blanche-noire-v3` (`91f711c6…`), run et empreinte du manifeste gelés dans les constantes, et les manifestes des deux autres versions neuves sous l'addendum, commandes gelées (`lecture_v6`, `lecture_v7`, `analyse_blanche_noire.lecture_v4`) ; tout autre manifeste qui cite le texte (chemin ou empreinte, dans ses octets : règle des textes) ou l'addendum arrête ; les tolérés sont comptés et écrits, par nom, dans `lien_au_preenregistrement.passages`. Voir le point 6.
4. **Graines (R9) : inchangées.** Entropie de chaque analyse = 128 premiers bits de l'empreinte de son texte scellé,
   passé à `--prereg` (règle Q9 des textes) ; entropie des plis de la lecture par épisode = celle de la principale
   (`8e267952…`, constante inchangée) ; clés de graines inchangées. Les graines de la course v4 sont donc **celles de la
   course v3** (mêmes textes), fixées avant toute donnée de R1 ; l'addendum n'en dérive aucune (son empreinte n'entre
   dans aucun tirage) : aucune liberté nouvelle sur la graine.
5. **Entrées** : inchangées (fiches de mêmes formats, chargeurs inchangés), plus les trois gardes du point 2.
6. **Second passage des textes, déclaré.** Chaque texte scellé liste « second passage » parmi ses arrêts ; la course v4
   est, pour chacun, un second passage du texte sur des données neuves, voulu par l'addendum v4 de R1 (« Les textes des
   analyses … ne bougent pas ») et par le GO de la relance. La garde du premier passage est donc redéfinie par cet
   addendum : premier passage **sous cet addendum**, par commande de la version neuve (point 3.c) ; les passages de la
   course v3 sont tolérés par liste fermée (les trois manifestes nommés au point 3.c, run et empreinte gelés), comptés et écrits ; tout autre passage antérieur arrête. C'est un écart déclaré aux trois textes scellés, porté à Lazar avec ce
   texte (nœud) ; sans son accord, aucune commande décisive n'est lancée. Un troisième passage exigerait un addendum
   nouveau, un code nouveau (constante `ADDENDUM` nouvelle) et une contre-lecture nouvelle : ce texte l'exclut d'avance. **Une seule lecture sous R1 v4** : ce passage épuise les trois textes ; aucune troisième lecture n'a lieu sous ces textes, sous cet addendum ni sous un autre (une autre course de R1 relève de textes neufs, d'une contre-lecture neuve et du GO de Lazar). Statut proposé à Lazar avec l'écart : les sorties de la course v3, lues et jugées (R-1322), restent au registre et sont rapportées avec celles de la course v4 ; la course v4 est la lecture qui compte pour R1 et R2 (critères gelés des textes), fixée avant toute donnée de R1 v4, jamais choisie sur ses résultats ; aucune des deux n'efface l'autre ; un arrêt technique après le manifeste est un nœud de Lazar (le code v6, v7 ou v4 refuse tout second passage sous l'addendum ; une reprise exigerait une version neuve du code, écart à « même code » des textes).
7. **Essais (R5)**, données synthétiques aux formats exacts du fournisseur pour la relance v4 (manifeste du rejeu décisif
   sous un texte scellé, commande `rejeu_activations_v4`, résultat `rejeu-activations.json` rattaché portant la clé
   `tokenisation`, table v4 scellée citant le sceau d'un résultat de réparation scellé) : chaque garde sur un cas sain et
   sur des artefacts — `texte` (rejeu gouverné par un autre texte ; même chemin, autre empreinte), `table-comparee`
   (`table_sha256` ≠ sceau ; table qui cite un autre résultat de réparation ; sceau de la table absent), `provenance`
   (`tokenisation.addendum` ≠ ; commande ≠), clé `tokenisation` absente ; même calcul et même issue que la version
   précédente à entropie égale (v6 = v2, v7 = v5, v4 = v3) ; artefact de bout en bout (arrêt avant le manifeste) ; rejeu
   non validé et R1 nul (aucune garde) ; mode décisif (texte qui gouverne exigé par chemin et empreinte, copie sous un
   autre nom refusée ; addendum unique à plusieurs blocs, bloc propre lu ; liste de la version précédente refusée ;
   empreinte altérée refusée ; constantes altérées refusées ; passage antérieur du texte et manifeste d'une autre analyse
   sous l'addendum tolérés et comptés ; second passage refusé ; manifeste illisible refusé) ; lecture par épisode
   décisive après la principale sous le même addendum (plis de la principale, concordance) ; fermeture des importations
   de la secondaire. Comptes : `tests/test_analyse_principale_r1_r2_v6.py` 4, `tests/test_analyse_par_episode_v7.py` 3,
   `tests/test_analyse_blanche_noire_v4.py` 4 : 11 réussis sur 11 ; essais anciens des analyses rejoués : 103 réussis sur
   103 (principale v1 et v2 : 24 ; par épisode v1 et v2 : 30 ; R2 seul v1 : 13 ; secondaire v1, v2, v3 : 36). Environnement
   gelé `.venv` (Python 3.13.18, numpy 2.4.6, scipy 1.17.1) ; `PYTHONPATH=src:tests nice -n 10 python -m pytest -q -p
   no:cacheprovider tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py
   tests/test_analyse_principale_r1_r2_v6.py tests/test_analyse_par_episode_v1.py tests/test_analyse_par_episode_v2.py
   tests/test_analyse_par_episode_v7.py tests/test_analyse_blanche_noire_v1.py tests/test_analyse_blanche_noire_v2.py
   tests/test_analyse_blanche_noire_v3.py tests/test_analyse_blanche_noire_v4.py` : 101 réussis attendus.
8. **Verdict** : inchangé (sous-agent neuf, R13, table gelée de chaque texte) ; il lit aussi `reception_v4` et
   `lien_au_preenregistrement.passages` de chaque sortie, et vérifie qu'ils citent le run `20261105-021737-r1-v4-rejeu-reel`.
9. **Ce qu'un nul veut dire** : inchangé.

### Listes fermées du code (sha256), vérifiées au lancement, par bloc propre à chaque analyse

Chaque bloc va de sa ligne de titre (gelée dans les constantes de la version neuve) à la ligne de titre suivante ; le code de chaque analyse ne lit que son bloc. Modules marqués « (neuf) » : versions neuves de cet addendum ; tous les autres sont repris sans modification, mêmes empreintes que dans les textes scellés.

Empreinte des constantes (analyse principale, code v6) : `6ab768f6ceaab8d9e889404755ed78ca714e68e7ca7f5117a05b78475eacfdfd`

### Liste fermée du code — analyse principale (code v6)

- paquet :
  - `src/controle_ia/analyse_principale_r1_r2/__init__.py` : `3d9d2db34507280c083a3044ef229613e4f7dc9f8f0b71d106e7d1a5fa19ae3c`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v1.py` : `66b52be663a8b826e9ad3a8ef5518f39c45edaff57251cc5bd5f2e3ab00db0ce`
  - `src/controle_ia/analyse_principale_r1_r2/calcul_v1.py` : `f5845571d0c22eedbb4341c50229ae606ed4b8576fcd5f9d544d3d1c0a74283e`
  - `src/controle_ia/analyse_principale_r1_r2/entrees_v1.py` : `244a04daf892341439da3c0ef5c4ed4c1cf07ec6d0d22da717dbd2a6640c0dc3`
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v1.py` : `4a34955ce8760fa26f62c0a368d5980a5b8f8782fe108bb9c286a1afa1b4b7dd`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v2.py` : `ae8170f7238e95833d63fdd71869472ba5f19d03985b0f3eb937b9791c896e2f`
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v2.py` : `3493e92d4507bd7b4f99062829aba973771ac18c06fda55da97bf91959debff8`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v6.py` : `450e5c14a57327bddbd5e22d307f80c85d338c25a33056fa5058fa51230b68da`  (neuf)
  - `src/controle_ia/analyse_principale_r1_r2/entrees_v4.py` : `2dd5ea7a0bbc56f3041f8dd1c48b6555e2d022d0570549ebefbc6de0a92798d1`  (neuf)
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v6.py` : `3556d7476c9e1f49815cc486ff1ab506b9eb63c1892c76c11018be541edc7788`  (neuf)
- essais :
  - `tests/test_analyse_principale_r1_r2_v1.py` : `5d510c05e15df689e0644076756f710172a815d26565a7407b97c66626b1e6d3`
  - `tests/test_analyse_principale_r1_r2_v2.py` : `2a99001597c6f25c61a1cc7eb417615410ee55743748e3967315560fce142cf7`
  - `tests/test_analyse_principale_r1_r2_v6.py` : `5ad9e800a9f17eaf43447243a8cc354aaf3edd1041500a8351670be45249db3c`  (neuf)
- modules gelés réutilisés sans modification :
  - `src/controle_ia/__init__.py` : `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  - `src/controle_ia/gardes.py` : `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439`
  - `src/controle_ia/scellement.py` : `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2`
  - `src/controle_ia/manifeste.py` : `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`
  - `src/controle_ia/prereg.py` : `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`
  - `src/controle_ia/analyse_blanche_noire/__init__.py` : `d6325b8c0d85a73bbad1ce5deb293baabac306fa6cbfb98aa8ac141d1db9add6`
  - `src/controle_ia/analyse_blanche_noire/constantes.py` : `7565d1a07fce3346510eb0e11cd900e540241bd85f7e426161569e8ff8e8366d`
  - `src/controle_ia/analyse_blanche_noire/modeles.py` : `6359650b54c770ffc8a15569699a1bf23d7e0d5baff82412c13698f9efbd3286`
  - `src/controle_ia/analyse_blanche_noire/entrees.py` : `9f125cd363ccfca7dfa5a532761291f21c5926e11b5bc87493d9481080b8a4cc`

Empreinte des constantes (analyse par épisode, code v7) : `d35cdfabc33e107f78484e8b551113fb363216ac989793f55d0df6330d27eec0`

### Liste fermée du code — analyse par épisode (code v7)

- paquet :
  - `src/controle_ia/analyse_principale_r1_r2/__init__.py` : `3d9d2db34507280c083a3044ef229613e4f7dc9f8f0b71d106e7d1a5fa19ae3c`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v1.py` : `66b52be663a8b826e9ad3a8ef5518f39c45edaff57251cc5bd5f2e3ab00db0ce`
  - `src/controle_ia/analyse_principale_r1_r2/calcul_v1.py` : `f5845571d0c22eedbb4341c50229ae606ed4b8576fcd5f9d544d3d1c0a74283e`
  - `src/controle_ia/analyse_principale_r1_r2/entrees_v1.py` : `244a04daf892341439da3c0ef5c4ed4c1cf07ec6d0d22da717dbd2a6640c0dc3`
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v1.py` : `4a34955ce8760fa26f62c0a368d5980a5b8f8782fe108bb9c286a1afa1b4b7dd`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v2.py` : `ae8170f7238e95833d63fdd71869472ba5f19d03985b0f3eb937b9791c896e2f`
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v2.py` : `3493e92d4507bd7b4f99062829aba973771ac18c06fda55da97bf91959debff8`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v4.py` : `533f1e93efa3b2ae46db6c61b405918408d1f006709420961846d0f236c1c3cc`
  - `src/controle_ia/analyse_principale_r1_r2/calcul_v4.py` : `834e1c7c9a7932430f9ac5b273ba015f8f38dbcff1bb1786d5de2437d25bd2c3`
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v4.py` : `132d20e73941e1c0f428c4cb7dc22f6785ee5f5e2b77b21206cfcb5f86532560`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v5.py` : `e8f783d2a0a3ea024ba4a13635d37572a5e2cec37f96b32f03bdcd20e0e7f64b`
  - `src/controle_ia/analyse_principale_r1_r2/calcul_v5.py` : `f11b32fd7c2e73acf47d25b417154e211e39b7d4086c76560a99507e44e73f4f`
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v5.py` : `cd94a607f3c5b9a7ca2f379895fbd0084b51283799456e735267aa8a3ffb261a`
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v6.py` : `450e5c14a57327bddbd5e22d307f80c85d338c25a33056fa5058fa51230b68da`  (neuf)
  - `src/controle_ia/analyse_principale_r1_r2/entrees_v4.py` : `2dd5ea7a0bbc56f3041f8dd1c48b6555e2d022d0570549ebefbc6de0a92798d1`  (neuf)
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v6.py` : `3556d7476c9e1f49815cc486ff1ab506b9eb63c1892c76c11018be541edc7788`  (neuf)
  - `src/controle_ia/analyse_principale_r1_r2/constantes_v7.py` : `5a15571f173f73a8492096e4f7c2af2c9a6d5774b68433a69cadf1a171b0e907`  (neuf)
  - `src/controle_ia/analyse_principale_r1_r2/lecture_v7.py` : `e391b321833870767653c7f6ca415bce29de7cc4441bcb5cdd4e7edff311378d`  (neuf)
- essais :
  - `tests/test_analyse_principale_r1_r2_v1.py` : `5d510c05e15df689e0644076756f710172a815d26565a7407b97c66626b1e6d3`
  - `tests/test_analyse_principale_r1_r2_v2.py` : `2a99001597c6f25c61a1cc7eb417615410ee55743748e3967315560fce142cf7`
  - `tests/test_analyse_par_episode_v1.py` : `cb4728f1ba7d0d84300ceac3d7acfaef92cb8fe985948b75a9ec0980c4ac3aa9`
  - `tests/test_analyse_par_episode_v2.py` : `7aaf866fe7cf6f011327a8645dd24e065e411422033df6b587f1318330674e15`
  - `tests/test_analyse_principale_r1_r2_v6.py` : `5ad9e800a9f17eaf43447243a8cc354aaf3edd1041500a8351670be45249db3c`  (neuf)
  - `tests/test_analyse_par_episode_v7.py` : `932d5b77bfd89511154b4c8358a78af25e461cc689c729ebb091e90a12989518`  (neuf)
- modules gelés réutilisés sans modification :
  - `src/controle_ia/__init__.py` : `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  - `src/controle_ia/gardes.py` : `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439`
  - `src/controle_ia/scellement.py` : `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2`
  - `src/controle_ia/manifeste.py` : `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`
  - `src/controle_ia/prereg.py` : `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`
  - `src/controle_ia/analyse_blanche_noire/__init__.py` : `d6325b8c0d85a73bbad1ce5deb293baabac306fa6cbfb98aa8ac141d1db9add6`
  - `src/controle_ia/analyse_blanche_noire/constantes.py` : `7565d1a07fce3346510eb0e11cd900e540241bd85f7e426161569e8ff8e8366d`
  - `src/controle_ia/analyse_blanche_noire/modeles.py` : `6359650b54c770ffc8a15569699a1bf23d7e0d5baff82412c13698f9efbd3286`
  - `src/controle_ia/analyse_blanche_noire/entrees.py` : `9f125cd363ccfca7dfa5a532761291f21c5926e11b5bc87493d9481080b8a4cc`

Empreinte des constantes (analyse secondaire, code v4) : `47c988e609dca50100fa6330c5b6e2e1b874a27d7bb1e543f676cd902649392d`

### Liste fermée du code — analyse secondaire (code v4)

- paquet :
  - `src/controle_ia/analyse_blanche_noire/__init__.py` : `d6325b8c0d85a73bbad1ce5deb293baabac306fa6cbfb98aa8ac141d1db9add6`
  - `src/controle_ia/analyse_blanche_noire/constantes.py` : `7565d1a07fce3346510eb0e11cd900e540241bd85f7e426161569e8ff8e8366d`
  - `src/controle_ia/analyse_blanche_noire/constantes_v3.py` : `6e7684acb7a7a520b926acc9315fd85db10d7f7b14d4cb8895986f577a3a33c4`
  - `src/controle_ia/analyse_blanche_noire/modeles.py` : `6359650b54c770ffc8a15569699a1bf23d7e0d5baff82412c13698f9efbd3286`
  - `src/controle_ia/analyse_blanche_noire/evaluation.py` : `12dee80a09f6a0f3dc2008035851f9b0257179a52114a99ce299a29812c07082`
  - `src/controle_ia/analyse_blanche_noire/evaluation_v3.py` : `539a0c7b8c9a8913380833d994875d6814cae1c9f7d3dfe6265b043c8e32ee2d`
  - `src/controle_ia/analyse_blanche_noire/entrees.py` : `9f125cd363ccfca7dfa5a532761291f21c5926e11b5bc87493d9481080b8a4cc`
  - `src/controle_ia/analyse_blanche_noire/entrees_v3.py` : `57bcb47ebd056b5d4a4164cd1611dc8405033d4bb37e9c1c4a68681d5febcd2b`
  - `src/controle_ia/analyse_blanche_noire/lecture.py` : `b5b5c131144cbd0139be6831ee917a415f85e159e47dfb5ac25111515c9cb1e4`
  - `src/controle_ia/analyse_blanche_noire/lecture_v3.py` : `dd5dffa4c6441981779aaa07816589666466bd4c8c7fc0d84a3b029fdec1d854`
  - `src/controle_ia/analyse_blanche_noire/rendu.py` : `483499198018a2e33b5ed116ec730f166d93c4b6e53c194899f89b48e9efa6a0`
  - `src/controle_ia/analyse_blanche_noire/rendu_v3.py` : `363cd84f6dc2453e33a896e55192f0605340fdeadd80c44046d08cb0ac8d0371`
  - `src/controle_ia/analyse_blanche_noire/constantes_v4.py` : `ba9b65d83ac3e78e8009574ce2e2b78790af4b220d56593b13a88b852b8f5239`  (neuf)
  - `src/controle_ia/analyse_blanche_noire/entrees_v4.py` : `a067f4e0fc3e4182cc567dbe547b730b8f80035954cdb1f390d7316445d2bc21`  (neuf)
  - `src/controle_ia/analyse_blanche_noire/lecture_v4.py` : `2f9b4f2b1726b3279b9815d47cc006748aee60e9dfea0cd8fe5e669c8817eaff`  (neuf)
- essais :
  - `tests/test_analyse_blanche_noire_v1.py` : `6f97c988ee335c07831aba2bf4e80627cc6db66075dcb51f37baf4d34eb4cafa`
  - `tests/test_analyse_blanche_noire_v3.py` : `cb86cf6d9bcb8d505277203467c192547b4ebecfa52b45e50d1c7141892b7ed7`
  - `tests/test_analyse_blanche_noire_v4.py` : `01883ddca64115fba9c6402cd9f0b33339eb7e2e0922ba2fac9ca20a49713709`  (neuf)
- modules gelés réutilisés sans modification :
  - `src/controle_ia/__init__.py` : `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  - `src/controle_ia/gardes.py` : `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439`
  - `src/controle_ia/scellement.py` : `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2`
  - `src/controle_ia/manifeste.py` : `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`
  - `src/controle_ia/prereg.py` : `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`
  - `src/controle_ia/bases/__init__.py` : `dac48b3cc7acb9d6fc1da5315237d7bc30ddc81fd3de4d75a9198d4b3313dbb6`
  - `src/controle_ia/bases/sequentiel.py` : `35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8`
  - `src/controle_ia/agregateurs/__init__.py` : `a804018234d2c5a60cef477ba5431d0ff21e888e52c20d9902f6d2745b77acf1`
  - `src/controle_ia/agregateurs/indexation.py` : `95ea9421b64263c614b9920ce4fbe4fff0da3739109b4b91f64681761957317b`
  - `src/controle_ia/agregateurs/processus_e.py` : `1081469bea3564a57119b56c26ee25f27817a7e961abdf440a556dc476a15fc7`
  - `src/controle_ia/agregateurs/statistiques.py` : `8b025acee465512bc89367fe343e722a85d05342a89d689abce26eeb888491e3`
  - `src/controle_ia/simulation_t03/__init__.py` : `435049ef81fddf34bd014b201ad28dbc782ae1978438e08d571013ea89ea7b7f`
  - `src/controle_ia/simulation_t03/calibrage.py` : `a2be6f6b127032aced5d75acd9cdf7c18c17e28df89978bd7102cf692c560def`


## Critères de lecture gelés

Inchangés, dits tels quels : la table gelée de chaque texte scellé (section « Critères de lecture gelés » de la
principale, l. 140-168 ; de la secondaire, l. 166-200 ; de la lecture par épisode, l. 105-134), sa préséance, son audit
de symétrie (R4) et la règle symétrique des deux lectures s'appliquent sans changement ; le code des issues est repris
tel quel (`lecture_v2.issue`, `lecture_v3.issue_v3`, `lecture_v5.issue`). Ce texte n'ajoute aucune ligne à ces tables.
Les gardes de réception ne sont pas des issues : une garde qui s'arrête n'est lue ni comme « rejeu non validé » ni comme
« P-R5 contraire » ; c'est un arrêt (rien n'est lu, aucun manifeste), porté à Lazar comme nœud, avec le motif écrit
(garde et clé, jamais une valeur de couverture), et le même audit (R4) s'applique qu'elle s'arrête sur une pièce
suspecte de trop ou de trop peu.

**Ce qu'aucune issue ne permet** : inchangé pour chaque texte ; s'y ajoute : lire une garde passée comme une validation
de la fidélité du rejeu (elle ne vérifie que la chaîne scellée : texte qui gouverne, table versée, provenance).

## Liste d'arrêt

Inchangées, dites telles quelles : les listes d'arrêt des trois textes scellés (principale, l. 169-181 ; secondaire,
l. 201-217 ; lecture par épisode, l. 135-145), chargeurs et calculs compris, s'appliquent sans changement, **sauf** la règle « second passage » (aucun manifeste sous `runs/` ne cite le texte, par son chemin ni par son empreinte), remplacée pour la seule course v4 par celle du Plan d'analyse, points 3.c et 6 (écart déclaré, nœud de Lazar). S'y ajoutent,
pour chaque version neuve (arrêt de toute l'analyse, `GardeArret`, motif écrit, rien n'est lu) :
- réception de la relance v4 : `texte` (le texte qui gouverne le rejeu, `preenregistrement` de son manifeste, ≠ addendum
  v4 scellé par chemin ou par empreinte) ; `table-comparee` (`tokenisation.table_sha256` ≠ sceau de la table v4 versée ;
  table v4 ou son compagnon absent ou altéré ; `resultat_reparation_sha256` de la table ≠ sceau du résultat de la
  réparation versé ; résultat de la réparation ou son compagnon absent ou altéré) ; `provenance` (`tokenisation.addendum`
  ≠ `prereg/R1-addendum-relance-v4.md` ; commande du rejeu ≠ `rejeu_activations_v4`) ; résultat du rejeu sans clé
  `tokenisation` ;
- mode décisif : texte passé ≠ texte scellé qui gouverne (chemin ou empreinte) ; addendum unique absent, non scellé ou
  non conforme ; bloc de l'analyse absent de l'addendum ; liste fermée du bloc ≠ liste de la version neuve, ou empreinte
  différente ; empreinte des constantes de la version neuve ≠ citée ; second passage sous l'addendum (manifeste qui cite
  l'addendum avec la commande de ce code ou une commande hors des trois commandes gelées ; manifeste illisible qui cite le texte ou l'addendum ; manifeste qui cite le texte hors de la liste fermée de la course v3, ou dont l'empreinte diffère de celle gelée) ;
- sortie déjà présente (R12) ; arrêt technique après le manifeste : règle inchangée de chaque texte (le manifeste reste ;
  un second passage exige l'accord de Lazar sur la seule cause technique, mêmes graines, même code).

Pas un arrêt (inchangé) : bras non lu, juge non livré, tirages dégénérés au-delà du seuil (comparaison non lue). Tolérés
et écrits : les trois manifestes de la course v3 de la liste fermée (Plan, point 3.c), et ceux des deux autres versions neuves sous cet addendum (commandes gelées).

## Limites écrites d'avance

- Les trois gardes contrôlent la chaîne scellée du fournisseur (texte qui gouverne, table versée, provenance), pas la
  fidélité du rejeu ni la couverture : celles-ci restent lues par les chargeurs et les issues inchangés.
- Le nom du run de la réparation (`20261104-234729-r1-v4-reparation-reel`) et le chemin de la table v4 sont des
  constantes gelées : un versement sous d'autres noms arrête les analyses (c'est voulu : rien n'est lu sous un autre
  nom sans addendum nouveau).
- Le rendu de la lecture par épisode garde le titre du code v5 ; seule la version écrite change.
- La garde du premier passage par commande suppose que chaque version neuve n'existe que pour cet addendum (constante
  `ADDENDUM`) ; un code réutilisé sous un autre addendum exigerait une version nouvelle.
- Ce texte ne lit rien ; sa seule prédiction mécanique (point « Prédiction ») n'est pas une prédiction scientifique.

## Marqueurs de gabarit

Un seul marqueur de substitution reste dans ce texte, en tête, ligne « Commit du code » (nom `COMMIT_CODE` entre
doubles chevrons), remplacé au scellement par les 40 caractères du commit cité (étape 0.b). Aucun autre : le motif
des marqueurs de gabarit (`controle_ia.prereg.GABARIT`) ne trouve que lui, une seule fois.

## Contre-lecture

Contre-lecture 1 (R2) : à faire par un sous-agent neuf qui n'a écrit ni ce texte, ni le code v6, v7 et v4, ni les trois
analyses ; lui donner explicitement ce brouillon, le rapport
`brouillons/etape-F-r1-v4-v1/rapport-developpeur-gardes-analyses-v1.md` (dix points à regarder d'abord), les
différentiels hors renommage du même dossier, l'addendum v4 de R1 (paragraphe cité), la fiche de réception v4
(sections 4.4 et 6) et les trois textes scellés. L'entrée de cette section est écrite au brouillon final par conv-audit :
identifiant du sous-agent, empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque
(acceptée, refusée et pourquoi). Jusque-là, `controle_ia.prereg.problemes` signale cette section (deux empreintes
exigées) et le marqueur du commit : c'est attendu d'un brouillon 1.
