# Rapport du rédacteur-développeur — étape F de R1 v4 : gardes de réception des trois analyses (addendum unique, code v6, v7 et v4) — v1

- **Qui, quand** : rédacteur-développeur neuf (sous-agent, Claude Fable 5.1), le 5 novembre 2026, de 15:52 à 16:40 UTC
  (`date -u`), sur la consigne `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/consigne-developpeur-gardes-analyses-r1-v4-v1.md`
  (`0bd28420836cb8244802b54e6a9b36fcb07d44ea83e47cab00f8e130d39c6480`). Je n'ai écrit ni les analyses, ni leur code, ni
  l'addendum v4 de R1, ni la fiche de réception v4.
- **Où** : arbre `/home/claude/controle-ia-travail`, branche `canal/conv-audit-n04` au commit `740f49e2` (inchangée) ;
  aucun commit, aucune poussée, aucun `.sha256` écrit, aucun fichier existant modifié (tous les livrables sont des fichiers
  neufs, `git status` : 22 fichiers non suivis, listés ci-dessous) ; rien sous `donnees/` ; aucun réseau ; aucune donnée
  de R1 v4 lue ; `calcul/r1-r2-reel-v1` non récupérée ; aucune commande décisive exécutée ; disque : 224 Ko sous
  `brouillons/`, 44 Ko sous `prereg/`, 76 Ko de code et d'essais.
- **Empreintes vérifiées avant d'écrire** : addendum v4 de R1 (copie du bac à sable) `0f10881b…` égale à celle citée par
  la consigne ; fiche v4 `605931f3…` ; les trois textes scellés égaux à leurs compagnons (`8e267952…`, `1f6a6da2…`,
  `26a3ff72…`).

## 1. Livrables (chemins et sha256)

Code (versions neuves, R12 ; rien d'existant modifié) :

| fichier | sha256 |
|---|---|
| `src/controle_ia/analyse_principale_r1_r2/constantes_v6.py` | `450e5c14a57327bddbd5e22d307f80c85d338c25a33056fa5058fa51230b68da` |
| `src/controle_ia/analyse_principale_r1_r2/entrees_v4.py` | `2dd5ea7a0bbc56f3041f8dd1c48b6555e2d022d0570549ebefbc6de0a92798d1` |
| `src/controle_ia/analyse_principale_r1_r2/lecture_v6.py` | `3556d7476c9e1f49815cc486ff1ab506b9eb63c1892c76c11018be541edc7788` |
| `src/controle_ia/analyse_principale_r1_r2/constantes_v7.py` | `5a15571f173f73a8492096e4f7c2af2c9a6d5774b68433a69cadf1a171b0e907` |
| `src/controle_ia/analyse_principale_r1_r2/lecture_v7.py` | `e391b321833870767653c7f6ca415bce29de7cc4441bcb5cdd4e7edff311378d` |
| `src/controle_ia/analyse_blanche_noire/constantes_v4.py` | `ba9b65d83ac3e78e8009574ce2e2b78790af4b220d56593b13a88b852b8f5239` |
| `src/controle_ia/analyse_blanche_noire/entrees_v4.py` | `a067f4e0fc3e4182cc567dbe547b730b8f80035954cdb1f390d7316445d2bc21` |
| `src/controle_ia/analyse_blanche_noire/lecture_v4.py` | `2f9b4f2b1726b3279b9815d47cc006748aee60e9dfea0cd8fe5e669c8817eaff` |
| `tests/test_analyse_principale_r1_r2_v6.py` | `5ad9e800a9f17eaf43447243a8cc354aaf3edd1041500a8351670be45249db3c` |
| `tests/test_analyse_par_episode_v7.py` | `932d5b77bfd89511154b4c8358a78af25e461cc689c729ebb091e90a12989518` |
| `tests/test_analyse_blanche_noire_v4.py` | `01883ddca64115fba9c6402cd9f0b33339eb7e2e0922ba2fac9ca20a49713709` |

Empreintes des constantes citées par l'addendum : principale, code v6 `6ab768f6ceaab8d9e889404755ed78ca714e68e7ca7f5117a05b78475eacfdfd` ;
par épisode, code v7 `d35cdfabc33e107f78484e8b551113fb363216ac989793f55d0df6330d27eec0` ; secondaire, code v4
`47c988e609dca50100fa6330c5b6e2e1b874a27d7bb1e543f676cd902649392d`.

Addendum unique (brouillon 1) : `prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon1.md`
(`5d3ab56c0c6b3faba393624967bce874839eb0cefcb4c7908b7b7d8954e3d245`) ; un seul marqueur de gabarit, `<<COMMIT_CODE>>`
(vérifié par le motif `<<[A-Z0-9_]+>>`) ; `controle_ia.prereg.problemes` sur ce brouillon : exactement deux lignes
attendues d'un brouillon 1 (contre-lecture 1 sans ses deux empreintes ; le marqueur du commit) ; aucun « À REMPLIR » ;
**les trois listes fermées de l'addendum ont été vérifiées par le code lui-même** (`lecture_v6.exiger_code_cite`,
`lecture_v7.exiger_code_cite`, `analyse_blanche_noire.lecture_v4.exiger_code_cite` sur le texte du brouillon : 22, 33 et 31
fichiers conformes, constantes égales).

Pièces du dossier `brouillons/etape-F-r1-v4-v1/` :

| fichier | sha256 |
|---|---|
| `listes-fermees-generees-v1.md` (listes et empreintes engendrées par script depuis les modules, recopiées dans l'addendum) | `003e0a2022bf668719d4cb83dbaa997d6d7421d7b2892b11d973512678d295f0` |
| `differences-lecture-v2-v6-brut-v1.diff` | `61f973e701fecd5cd26a62e48d14982663e984845ab8afbe33a227d1ce4de972` |
| `differences-lecture-v2-v6-hors-renommage-v1.diff` | `bc6b0fdc0b5ddd13e56d47cc1414d43cf5dfc01c6caf89edcf800d29c6cec9f9` |
| `differences-constantes-v2-v6-brut-v1.diff` | `2abf8284566fe073fb05baff18cb388b9efedc43429ca975df2df8f67e8bce48` |
| `differences-lecture-v5-v7-brut-v1.diff` | `32c59eefd65128049b1815a718f815f70053ecc1df571c7dfc1e8186141f67aa` |
| `differences-lecture-v5-v7-hors-renommage-v1.diff` | `d64789ea69653d9843495e2e6e3b11e39ae998650d00201924febc3cf2925893` |
| `differences-constantes-v5-v7-brut-v1.diff` | `1a3169590c8712304a355dc4ea8195284d6234a16b4c5e204b9e055166bbcdd8` |
| `differences-lecture-bn-v3-v4-brut-v1.diff` | `a965ca68e85384b642b0d2e7663de72bca02ecf84da3585434cd41da7d8f1228` |
| `differences-lecture-bn-v3-v4-hors-renommage-v1.diff` | `99cb1ce8f82e0f72c75137af904984771e937b144c701faa15dc66025c4f96b1` |
| `differences-constantes-bn-v3-v4-brut-v1.diff` | `3aaf3b143b609a650d1c537c640bca674871fa1078c183cdfa11476feb4214ad` |

Les différentiels « hors renommage » sont faits contre la version précédente renommée par `sed` (v2→v6, K2→K6 ; v5→v7 ;
v3→v4, C3→C4, `analyser_v3`→`analyser_v4`) : il n'y reste que les changements de fond.

## 2. Ce qui a été fait et pourquoi (décisions prises par le développeur, à contre-lire)

1. **Les trois gardes, telles qu'écrites par l'addendum v4** (`exiger_reception_v4`, un module `entrees_v4` par paquet) :
   `texte` (`preenregistrement` du manifeste du rejeu = `{chemin, sha256}` de l'addendum v4 scellé) ; `table-comparee`
   (`tokenisation.table_sha256` = sceau de `prereg/R1-table-tokenisation-v4.json`, compagnon vérifié, **et**
   `resultat_reparation_sha256` de la table = sceau de
   `diag/20261104-234729-r1-v4-reparation-reel/resolution-graine-lot-v3-reparation.json`, compagnon vérifié, fichier haché
   jamais lu) ; `provenance` (`tokenisation.addendum` = `prereg/R1-addendum-relance-v4.md` ; commande du manifeste =
   `python -m controle_ia.runs_nuit.rejeu_activations_v4`). Appelées juste après le chargeur de R1 inchangé, avant les
   juges, le manifeste et tout calcul ; arrêt à la première qui manque ; un message nomme la garde et la clé, jamais une
   valeur de couverture. Le manifeste du rejeu est atteint par `verifier_resultat` (résultat scellé → `run_id` →
   `runs/<run>/manifeste.json`, chaîne vérifiée).
2. **Comment la version neuve est lancée** (le point que la consigne ne fixait pas, décidé ainsi et documenté dans
   l'addendum, Plan d'analyse, points 3 et 6) : `--prereg` reste le **texte scellé inchangé** (exigé par chemin et par
   empreinte, `exiger_texte`) ; l'**addendum unique** est lu par un chemin gelé (`constantes_*.ADDENDUM =
   prereg/addendum-1-gardes-analyses-r1-v4-v1.md`), exigé scellé et conforme ; la liste fermée de la version neuve est lue
   dans le **bloc propre** de l'analyse dans l'addendum (titre gelé), parce que trois listes dans un seul texte ne sont
   pas séparables par la citation des textes (la liste de la principale est contenue dans celle de la lecture par
   épisode) ; la liste fermée de la version précédente reste vérifiée sur le texte. Conséquences voulues : les **graines
   ne changent pas** (empreinte du texte, Q9), les plis de la lecture par épisode restent ceux de la principale
   (`8e267952…`), le manifeste cite toujours le texte comme préenregistrement (« ce texte cité ») et l'addendum dans sa
   configuration.
3. **Second passage** : les trois textes auraient refusé la course v4 (leurs manifestes de la course v3,
   `runs/20261103-0727…`, `-0728…`, `-0728…`, sont dans la branche et citent les textes). La garde est redéfinie :
   premier passage **sous l'addendum**, par la **commande** de la version neuve (un manifeste qui cite l'addendum avec
   cette commande arrête ; un manifeste illisible qui cite l'addendum arrête ; les manifestes des deux autres analyses sous
   le même addendum et les passages de la course v3 sont tolérés, comptés et écrits dans `lien_au_preenregistrement.passages`).
   C'est un **écart déclaré aux trois textes scellés** (addendum, Plan, point 6) : nœud de Lazar avant tout lancement.
4. **Noms** : principale `lecture_v6`/`constantes_v6` et `entrees_v4` (la lecture du manifeste du rejeu le demandait) ;
   secondaire `lecture_v4`/`constantes_v4`/`entrees_v4` dans son paquet (aucun module du paquet principal : fermeture
   des importations éprouvée dans un interpréteur neuf) ; lecture par épisode **`lecture_v7`/`constantes_v7`** : la
   consigne demandait « la version suivante du module qu'elle cite » (`lecture_v5`), mais `v6` est pris par la principale
   dans le même paquet, et R12 interdit deux versions sous un nom. `lecture_v7` lit `constantes_v6`, `entrees_v4` et
   `lecture_v6` (gardes partagées), qui entrent donc dans sa liste fermée (33 fichiers).
5. **Structure des versions neuves** : `lecture_v6` reprend par référence `lecture_v2.issue`, `lecture_v1.calculer`,
   `lecture_v1.rendre` ; `lecture_v7` reprend par référence `lecture_v5.calculer`, `exiger_concordance_principale`,
   `lire_principale`, `issue`, `rendre` ; `lecture_v4` (secondaire) reprend `lecture_v3.calculer_p3`, `calculer_r4`,
   `issue_v3`, `rendu_v3.rendre_v3` et recopie le déroulé d'`analyser_v3`. Les différentiels bruts montrent donc des
   suppressions (le corps repris n'est plus recopié) ; les ajouts de fond sont : `exiger_texte`, `liste_fermee_de`,
   `exiger_code_cite_sous` (lecture scopée), `exiger_premier_passage_sous` (ou `_v4`), l'appel à `exiger_reception_v4`,
   `config["addendum"]`, `resultat["reception_v4"]`, `lien["addendum"]`. Le rendu de la lecture par épisode garde le titre
   « (code v5) » et écrit la version « (code v7) » à côté (rendu repris tel quel, non modifié).
6. **Constantes gelées neuves** (`constantes_v6`, recopiées dans `analyse_blanche_noire.constantes_v4`, reprises par
   `constantes_v7` dans son bloc « v6 ») : `TEXTE` (chemin, empreinte du texte qui gouverne), `ADDENDUM`, `TITRE_LISTE`,
   `ADDENDUM_V4` (chemin, `0f10881b…`), `COMMANDE_REJEU_V4`, `TABLE_V4`, `RESULTAT_REPARATION_V4` (nom du run de la
   réparation gelé : `20261104-234729-r1-v4-reparation-reel`, pris de la consigne).

## 3. Essais (R5) : comptes

Environnement gelé `.venv` du dépôt principal (Python 3.13.18, numpy 2.4.6, scipy 1.17.1 ; le canal n'a pas de `.venv`),
`PYTHONPATH=src:tests`, `nice -n 10`, `-p no:cacheprovider`, données synthétiques seulement.

| fichier | essais | résultat |
|---|---|---|
| `tests/test_analyse_principale_r1_r2_v1.py` | 20 | réussis |
| `tests/test_analyse_principale_r1_r2_v2.py` | 4 | réussis |
| `tests/test_analyse_principale_r1_r2_v6.py` (neuf) | 4 | réussis (7 s) |
| `tests/test_analyse_par_episode_v1.py` | 12 | réussis |
| `tests/test_analyse_par_episode_v2.py` | 18 | réussis |
| `tests/test_analyse_par_episode_v7.py` (neuf) | 3 | réussis (7 s) |
| `tests/test_analyse_r2_seul_v1.py` | 13 | réussis |
| `tests/test_analyse_blanche_noire_v1.py` | 12 | réussis |
| `tests/test_analyse_blanche_noire_v2.py` | 11 | réussis |
| `tests/test_analyse_blanche_noire_v3.py` | 13 | réussis |
| `tests/test_analyse_blanche_noire_v4.py` (neuf) | 4 | réussis (19 s) |

Essais anciens des analyses rejoués ensemble : **103 réussis sur 103** en 200 s. Essais neufs : **11 réussis sur 11**.
Tests attendus écrits dans l'addendum : principale 28 (20 + 4 + 4), secondaire 17 (13 + 4 ; v1 et v2 : 23 de plus),
lecture par épisode 61 (12 + 18 + 3 + 28). La suite complète du dépôt (`tests/`) a été lancée en arrière-plan ; son
état au moment de ce rapport est écrit en fin de rapport.

Ce que les essais neufs éprouvent (cas sain et artefact pour chaque garde) : `texte` (rejeu gouverné par un autre texte ;
même chemin, autre empreinte) ; `table-comparee` (`table_sha256` ≠ sceau ; table qui cite un autre résultat de
réparation ; sceau de la table absent) ; `provenance` (`tokenisation.addendum` ≠ ; commande ≠) ; clé `tokenisation`
absente ; même calcul et même issue que la version précédente à entropie égale ; artefact de bout en bout (arrêt avant le
manifeste) ; rejeu non validé et R1 nul (aucune garde) ; mode décisif (texte exigé par chemin et empreinte ; copie sous
un autre nom refusée ; addendum à plusieurs blocs, bloc propre lu ; liste de la version précédente refusée ; empreinte
altérée ; constantes altérées ; passage antérieur du texte et manifeste d'une autre analyse sous l'addendum tolérés et
comptés ; second passage refusé ; manifeste illisible) ; lecture par épisode décisive après la principale sous le même
addendum ; fermeture des importations de la secondaire (interpréteur neuf). Formats synthétiques : manifeste du rejeu
décisif sous un texte scellé (`creer_manifeste(decisif=True, prereg=…, commande=…)`), résultat rattaché par
`ecrire_resultat` avec la clé `tokenisation` (`version_table`, `table_sha256`, `table_empreinte_citee`, `addendum`,
`non_conformes`, `signales`), table v4 scellée (`version`, `resultat_reparation_sha256`, `voie`, `temoin`, `episodes`…),
résultat de réparation scellé ; pour la secondaire, pointeurs `["resultat", …]` comme dans la fiche réelle.

## 4. Les dix points qu'un contre-lecteur neuf doit regarder d'abord

1. Les trois gardes contre le paragraphe « Analyses (inchangées) » de l'addendum v4, mot à mot (`entrees_v4.py` des deux
   paquets, 50 lignes chacun ; les deux copies sont-elles identiques hors du nom des constantes ?).
2. Leur place : après `charger_r1` / `charger_activations_v3`, avant les juges, le manifeste et tout calcul ; rien n'est
   écrit si une garde s'arrête (essais « artefact de bout en bout »).
3. Ce qui est lu des pièces de la réparation : le résultat de la réparation est seulement haché ; de la table, une seule
   clé ; aucun message n'écrit une valeur de couverture (fiche v4, section 6).
4. Le nom du run de la réparation et le chemin de la table, gelés dans les constantes : sont-ce bien ceux du versement
   (`20261104-234729-r1-v4-reparation-reel`, `prereg/R1-table-tokenisation-v4.json`) ? Un autre nom arrête.
5. Le texte qui gouverne, inchangé, exigé par chemin et empreinte ; les graines ne changent pas (mêmes que la course v3) :
   est-ce acceptable, et est-ce bien ce que les textes disent (Q9) ?
6. La redéfinition du premier passage (sous l'addendum, par commande) : écart déclaré aux trois textes scellés, à porter à
   Lazar ; la discrimination par `commande` entre les trois analyses et les passages de la course v3 tolérés.
7. La lecture scopée de la liste fermée : titres exacts (`TITRE_LISTE`), bloc fermé par la ligne de titre suivante ;
   regénérer `listes-fermees-generees-v1.md` par le script du rapport (section 6) et comparer à l'addendum ; vérifier que
   la liste de la version précédente reste vérifiée sur le texte (`L2.exiger_code_cite`, `L5.…`, `L3.…`).
8. Les noms : `v7` pour la lecture par épisode (collision avec `v6`) ; `lecture_v7` dépend de `lecture_v6` ; le rendu garde
   le titre « (code v5) ».
9. Les formats synthétiques des essais contre les formats réels (fiche v4, sections 4.3 et 4.4 ; script
   `verifier_reception_r1_v4_v1.py`, gardes `table-comparee` et `provenance`) : clé `tokenisation` sous `resultat`,
   `preenregistrement` du manifeste, `resultat_reparation_sha256` dans la table, sceaux ; les essais remplacent l'empreinte
   gelée de l'addendum v4 par celle d'un jouet (`monkeypatch`), l'empreinte réelle étant vérifiée littéralement.
10. Les fiches neuves de la course v4 (mêmes formats, noms neufs) et l'ordre des trois commandes (section 5) ; la condition
    de la secondaire (texte de la principale scellé et concordance faite) est remplie depuis le 2 novembre.

## 5. Commandes exactes pour la mère (conv-audit), dans l'ordre

Préalables (nœuds et registres) : contre-lecture neuve du brouillon 1 (R2), traitement, brouillon final ; accord de Lazar
sur l'écart déclaré (second passage des textes sous l'addendum, Plan, point 6) ; empreinte du brouillon final inscrite au
registre et poussée.

1. **Commit cité, scellement** (branche `canal/conv-audit-n04`) :
   ```
   git add src/controle_ia/analyse_principale_r1_r2/constantes_v6.py src/controle_ia/analyse_principale_r1_r2/entrees_v4.py \
     src/controle_ia/analyse_principale_r1_r2/lecture_v6.py src/controle_ia/analyse_principale_r1_r2/constantes_v7.py \
     src/controle_ia/analyse_principale_r1_r2/lecture_v7.py src/controle_ia/analyse_blanche_noire/constantes_v4.py \
     src/controle_ia/analyse_blanche_noire/entrees_v4.py src/controle_ia/analyse_blanche_noire/lecture_v4.py \
     tests/test_analyse_principale_r1_r2_v6.py tests/test_analyse_par_episode_v7.py tests/test_analyse_blanche_noire_v4.py \
     prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon<N>.md brouillons/etape-F-r1-v4-v1
   git commit -m "Addendum 1 gardes des analyses (R1 v4) : code v6, v7, v4 et essais, brouillon final"   # commit cité, ni amendé ni refait
   C=$(git rev-parse HEAD)
   sed "s/<<COMMIT_CODE>>/$C/" prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon<N>.md > prereg/addendum-1-gardes-analyses-r1-v4-v1.md
   diff prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon<N>.md prereg/addendum-1-gardes-analyses-r1-v4-v1.md   # une seule ligne
   PYTHONPATH=src .venv/bin/python -c "from controle_ia.prereg import problemes, sceller_prereg; p='prereg/addendum-1-gardes-analyses-r1-v4-v1.md'; assert problemes(p) == [], problemes(p); print(sceller_prereg(p))"
   git add prereg/addendum-1-gardes-analyses-r1-v4-v1.md prereg/addendum-1-gardes-analyses-r1-v4-v1.md.sha256 && git commit -m "Addendum 1 gardes des analyses scellé" && git push
   ```
   (Le chemin `prereg/addendum-1-gardes-analyses-r1-v4-v1.md` est gelé dans les constantes : ne pas le changer.)
2. **Arbre séparé, environnement** :
   ```
   git worktree add -b analyses-r1-v4 /home/claude/controle-ia-analyses-r1-v4 $(git rev-parse HEAD)
   cd /home/claude/controle-ia-analyses-r1-v4 && . /home/user/controle-ia-travail/.venv/bin/activate
   python -c "import sys, numpy, scipy; print(sys.version.split()[0], numpy.__version__, scipy.__version__)"   # 3.13.18 2.4.6 1.17.1
   PYTHONPATH=src:tests nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py tests/test_analyse_principale_r1_r2_v6.py tests/test_analyse_par_episode_v1.py tests/test_analyse_par_episode_v2.py tests/test_analyse_par_episode_v7.py tests/test_analyse_blanche_noire_v1.py tests/test_analyse_blanche_noire_v2.py tests/test_analyse_blanche_noire_v3.py tests/test_analyse_blanche_noire_v4.py   # 101 passed
   ```
3. **Récupération par refspec, seuls chemins** (le témoin n'est pas lu : non récupéré) :
   ```
   git fetch origin calcul/r1-r2-reel-v1
   git checkout FETCH_HEAD -- runs/20261105-021737-r1-v4-rejeu-reel diag/20261105-021737-r1-v4-rejeu-reel \
     runs/20261104-234729-r1-v4-reparation-reel diag/20261104-234729-r1-v4-reparation-reel \
     prereg/R1-table-tokenisation-v4.json prereg/R1-table-tokenisation-v4.json.sha256
   for f in activations-p3-rejeu-v1.npz activations-p3-rejeu-v1-maximum.npz activations-p3-rejeu-v1-complement-hors-cout.npz; do
     mkdir -p donnees/20261105-021737-r1-v4-rejeu-reel
     git show FETCH_HEAD:donnees/20261105-021737-r1-v4-rejeu-reel/$f > donnees/20261105-021737-r1-v4-rejeu-reel/$f
     git show FETCH_HEAD:donnees/20261105-021737-r1-v4-rejeu-reel/$f.sha256 > donnees/20261105-021737-r1-v4-rejeu-reel/$f.sha256
   done
   ```
   plus les fichiers des juges (`donnees/20261102-004328-r2-juge3b-reel/scores-juge3b-p3-v1.npz`,
   `donnees/20261102-005048-r2-juge8b-reel/scores-juge8b-p3-v1.npz`, leurs compagnons) et les données de P3
   (`donnees/20261019-230011-p3-reel/`), comme à la course v3 (texte de la principale, étape 0.f : vérification R11 des
   textes de P3, `ba05fa13…`), **sans ouvrir aucun `.npz`** ; `PYTHONPATH=src python -m controle_ia.scellement verifier
   <chaque fichier versé>` ; puis `git add runs diag prereg/R1-table-tokenisation-v4.json prereg/R1-table-tokenisation-v4.json.sha256
   && git commit -m "Pièces versées de la relance v4 (rejeu, réparation, table v4)"` ; `git status --porcelain
   --untracked-files=all` vide.
4. **Fiches de réception** (mêmes formats et clés que les fiches de la course v3, noms neufs ; aucun nombre de résultat ;
   les fiches v3 restent intactes) : `prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json` (`format` =
   `fiche-reception-principale-r1-r2-v1` ; `R1` = `{moyenne, maximum, complement, resultat}` du run
   `20261105-021737-r1-v4-rejeu-reel`, `resultat` = `diag/20261105-021737-r1-v4-rejeu-reel/rejeu-activations.json` ; `R2` =
   juges inchangés) et `prereg/fiche-reception-blanche-noire-v3-relance-v4.json` (`format` = `fiche-reception-blanche-noire-v3` ;
   `R1` = `{moyenne, maximum, manifeste = diag/…/rejeu-activations.json, pointeurs ["resultat", …]}` ; `R4: null`) ;
   `python -m controle_ia.scellement sceller <fiche>` ; commit de chaque fiche seule ; arbre propre.
5. **Commandes décisives** (chacune depuis la racine de l'arbre séparé, arbre propre ; sorties committées avant la
   suivante ; `<run>` = `AAAAMMJJ-HHMMSS` de `date -u`) :
   ```
   PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v6 --fiche prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json --run-analyse <run>-analyse-principale-r1-r2-v1 --prereg prereg/analyse-principale-r1-r2-v1.md
   git add runs/<run>-analyse-principale-r1-r2-v1 diag/<run>-analyse-principale-r1-r2-v1 && git commit -m "Analyse principale R1-R2, course v4 (code v6)"
   PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v7 --fiche prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json --principale diag/<run>-analyse-principale-r1-r2-v1/analyse-principale-r1-r2-v1.json --run-analyse <run2>-analyse-par-episode-v1 --prereg prereg/analyse-par-episode-v1.md
   git add runs/<run2>-analyse-par-episode-v1 diag/<run2>-analyse-par-episode-v1 && git commit -m "Lecture par épisode R1-R2, course v4 (code v7)"
   PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_blanche_noire.lecture_v4 --fiche prereg/fiche-reception-blanche-noire-v3-relance-v4.json --run-analyse <run3>-analyse-blanche-noire-v3 --prereg prereg/analyse-blanche-noire-v3.md
   git add runs/<run3>-analyse-blanche-noire-v3 diag/<run3>-analyse-blanche-noire-v3 && git commit -m "Analyse secondaire R1-R2, course v4 (code v4)"
   ```
   Ordre : principale d'abord (son texte est scellé et sa concordance faite, condition de la secondaire, étape 0.g de
   son texte) ; lecture par épisode ensuite (elle lit le résultat scellé de la principale et vérifie la concordance) ;
   secondaire en dernier (même ordre qu'à la course v3). Puis `git merge` (jamais de rebasage) dans la branche de
   travail, poussée ; verdict R13 par un sous-agent neuf, qui lit aussi `reception_v4` et
   `lien_au_preenregistrement.passages` de chaque sortie.

## 6. Reproduire les listes fermées de l'addendum

```
PYTHONPATH=src .venv/bin/python - <<'EOF'
from controle_ia.scellement import empreinte
from controle_ia.analyse_principale_r1_r2 import lecture_v6 as L6, lecture_v7 as L7, constantes_v6 as K6, constantes_v7 as K7
from controle_ia.analyse_blanche_noire import lecture_v4 as LB4, constantes_v4 as C4
for titre, mod, K in ((K6.TITRE_LISTE, L6, K6), (K7.TITRE_LISTE, L7, K7), (C4.TITRE_LISTE, LB4, C4)):
    print(K.empreinte_constantes(), titre)
    for c in mod.FICHIERS_PAQUET + mod.FICHIERS_ESSAIS + mod.FICHIERS_REUTILISES:
        print(f"  - `{c}` : `{empreinte(c)}`")
EOF
```
(même contenu que `listes-fermees-generees-v1.md`, aux mentions « (neuf) » et aux sous-titres près).

## 7. Réserves et risques

1. **Déroulé décisif non prévu par la consigne** : texte scellé inchangé en `--prereg`, addendum par chemin gelé, liste
   fermée lue dans un bloc propre, premier passage redéfini sous l'addendum par commande. C'est la seule façon trouvée de
   faire tourner trois codes neufs sous trois textes inchangés avec un addendum unique ; c'est aussi un écart déclaré aux
   listes d'arrêt des textes (second passage) : nœud de Lazar ; si la décision est autre, les trois `lecture_*` et les
   essais du mode décisif changent, pas les gardes de réception.
2. **Noms gelés** : run de la réparation `20261104-234729-r1-v4-reparation-reel` et chemin de la table pris de la consigne
   et de l'addendum v4, non vérifiés sur la branche (non récupérée) ; un versement sous un autre nom arrête à bon droit,
   mais bloque. Les pièces de la réparation (résultat et compagnon) doivent être dans l'arbre des analyses (section 5.3).
3. **Formats synthétiques** : la clé `tokenisation` sous `resultat`, `preenregistrement` et `commande` du manifeste du
   rejeu, `resultat_reparation_sha256` de la table viennent de la fiche v4 et du script de réception, pas du code du
   fournisseur (`rejeu_activations_v4.py`, absent du canal) ; un écart de forme arrêterait la première commande décisive
   (sans rien lire) ; de même, `rendu` de la lecture par épisode garde son titre « (code v5) ». Enfin, le canal n'a pas de
   `.venv` : les essais ont tourné avec celui du dépôt principal (mêmes versions gelées).

## 8. État de la suite complète du dépôt (`tests/`, arrière-plan)

Voir la dernière ligne de `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/suite-complete-etape-F.log`
(bac à sable de la session) ; au moment d'écrire ce rapport, la suite était à plus d'un tiers sans échec. Le résultat
final est donné dans la réponse du développeur à la mère s'il est connu avant la fin de la session ; sinon, à relancer
par la mère (`PYTHONPATH=src:tests nice -n 10 python -m pytest -q -p no:cacheprovider tests/`).
