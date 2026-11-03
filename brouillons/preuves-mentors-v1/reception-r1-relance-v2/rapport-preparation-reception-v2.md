# Rapport de préparation — réception de la relance de R1 sur la table v3 (procédure et script v2) — v2

- **Auteur** : sous-agent développeur neuf (Claude Opus 5.5), pour la session conv-audit, sur la consigne
  `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/reception-r1-relance-v3-v2-developpeur-prompt.md`.
  Je n'ai écrit ni l'addendum v3 de relance de R1, ni la procédure de réception v1, ni son script, ni nos analyses
  scellées, ni la concordance sur laquelle je m'appuie.
- **Date** : 3 novembre 2026, de 05:21:21 à 06:26:00 UTC (heures relevées par `date -u`).
- **Interdits respectés** : un seul `git fetch`, celui de la consigne, par refspec explicite (05:21:33 UTC, code 0 ;
  `refs/remotes/origin/prep/r1-relance-v3` de `49d29c8e` à `04bc323a`) ; `git for-each-ref refs/remotes | grep -c donnees`
  = 0 avant et après ; aucun commit, aucun `.sha256` dans le dépôt, aucun fichier existant modifié ; rien sous `diag/`,
  `runs/`, `donnees/` ; aucune branche `calcul/…` ni arbre séparé ; aucun autre appel de réseau ni de modèle ;
  `nice -n 10` pour tout calcul ; fichiers neufs sous ce dossier seulement (huit, ce rapport compris).

## 0. En bref

La procédure et le script de réception passent en v2 pour l'addendum v3 scellé (R-1 à R-5 de notre concordance
`8482b4cd…`). La **fiche de réception** est écrite par le script en mode « avant la récupération », prête à sceller :
`fiche-reception-r1-relance-v3-v1.md`, `47e4b6ac3cddb4afbc38eac4b8c5ca96b13c1d753e7ffa20fbc95622cdc3e3cb`. Essais : 61
réussis sur 61 (7,45 s). Banc : 46 mutants, tous tués (25 gardes entières et 21 contrôles isolés). Deux constats pour la
session : le dépôt de cette instance est un **clone superficiel** (deux commits cités par la v1 y manquent : étape A0
neuve) ; l'analyse secondaire scellée (l. 24) interdit tout nombre dans sa fiche JSON (garde `P-R5` étendue).

## 1. Changements de la v1 à la v2

| objet | v1 (addendum v2) | v2 (addendum v3 scellé) | source |
|---|---|---|---|
| Moment de la fiche | aucune fiche de contrôles avant la récupération | **étape 0** : fiche de réception écrite par le script, contre-éprouvée, scellée, commitée, poussée, annoncée au canal **avant la récupération** ; P1 l'exige | C-1, R-5 ; addendum v3, E8 (e) |
| P1, P2 | addendum v2, `$ADDENDUM_SHA` à remplir ; concordance finale de la v2 | addendum v3 `88e262e2…` (constante vérifiée), configuration v5, table v3 ; concordance sur la version scellée | R-1 |
| Épisodes non inversibles | `$NON_INVERSIBLES`, garde E19 sur une liste déclarée | **liste vide fixée** ; garde `comptes` (`episodes_non_resolus` = []) | R-1 ; E2, E19 |
| Lecteur R13 de la principale | décision N-A et liste | **« N-A sans objet »** et **réserve sur HG-2** | R-1 |
| Clé du texte | `--addendum-chemin` = `…-v2.md` par défaut ; `redaction.addendum_v2` sans garde (repli silencieux) | texte qui gouverne lu dans la clé réelle **`preenregistrement`** du manifeste (`manifeste.py` l. 104), comparé ; `redaction.addendum_v3` ; `redaction.provenance_table` = `tokenisation.addendum` | R-2 ; E16 |
| Comparaisons | `tokenisation.table_sha256` noté ; manifeste haché seulement | **refus** (code 2, `ARRÊT [garde] : …`) sur : texte, commande, `decisif`, configuration (canonique, recalcul, table citée), commit et arbre propre, entropie ; `tokenisation.table_sha256` **comparée** ; `tokenisation.addendum` = `prereg/R1-addendum-relance-v2.md` à l'identique ; comptes fixés par la table ; runs et empreintes des scores des juges cités | R-3 ; concordance § 6, points 2 et 3 |
| P-R5 | `notes` recopiait `episodes_non_resolus_du_run` et `table_sha256` | filtre des clés nommées ; noms des clés lues dans `redaction.cles_lues`, **aucune valeur recopiée** ; garde `P-R5` : aucune clé interdite, aucun nombre dans les fiches JSON | concordance § 6, point 4 ; secondaire l. 24 |
| Reprise E21 | rien | `--branche-source`, `--course-arretee-e21`, `--arret-e21-sha256`, `--annonce-e21` ; course arrêtée notée en C et dans `redaction.e21`, jamais ouverte | R-4 ; E21, C-8 |
| Clone superficiel | — | **étape A0** : commits cités présents, sinon approfondissement des seules branches de travail par refspec | constat ci-dessous (section 5) |
| Ouverture des JSON | facultative (`--ouvrir-resultats`) | toujours (manifeste, résultat, juges ; clés nommées) : les contrôles de R-3 l'exigent | R-3 |
| R12 | la fiche principale pouvait être écrite avant le refus sur la secondaire | les deux sorties sont vérifiées avant toute écriture | défaut de la v1 |
| Attribution des commits | lignes d'une autre session écrites en dur | variable `SIGNATURE`, contrôlée en 0.1 et A1 | — |
| Essais | 12, table `5f6c…`, clé `addendum_v2` | 61, table `ead8a668…`, vraie configuration v5, vrais textes scellés copiés à l'octet | R-3 |

## 2. La fiche de réception (prête à sceller)

- `brouillons/preuves-mentors-v1/reception-r1-relance-v2/fiche-reception-r1-relance-v3-v1.md`,
  `47e4b6ac3cddb4afbc38eac4b8c5ca96b13c1d753e7ffa20fbc95622cdc3e3cb`, écrite le 3 novembre 2026 à 06:23:34 UTC par
  `ecrire_fiches_reception_v2.py` (`d4701213…`) en mode « avant la récupération », sur le vrai dépôt : 16 références lues,
  0 `calcul/…`, 0 `donnees` ; gardes passées : `recuperation`, `config-table`, `canonique`, `table`, `ligne-104`,
  `attentes-texte`, `piece`, `compagnon`. Contre-épreuve (étape 0.2 de la procédure, jouée ici hors du dépôt) :
  « attendus identiques ».
- Elle porte, en clair (sections 1 à 7) et dans un bloc lu par le mode « après le versement » (section 8) : les quinze
  pièces citées avec commit et empreinte recalculée ; le manifeste attendu ; le résultat attendu ; les fichiers ; ce qui
  n'est pas lu avant les analyses ; les règles (N-A, HG-2, arrêt, E21, tout écart = arrêt).
- Les attendus sont dérivés de la table v3 et de la configuration v5, puis retrouvés mot pour mot dans les « Attentes de
  réception » de l'addendum v3, son en-tête, E16 et sa section « R2 » (garde `attentes-texte`) ; 2 236 et 1 782 sont des
  constantes du pré-vol, vérifiées par le texte seulement.
- Elle n'est pas scellée (consigne) : la session la scelle à l'étape 0.3 de la procédure, avant la récupération, puis
  annonce chemin et empreinte au canal (0.4).

## 3. Essais (R5) — 61 réussis sur 61, 7,45 s (`essais-v2-sortie.txt`)

Lancement : `cd /home/claude/controle-ia-travail && PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 nice -n 10 .venv/bin/python
-m pytest -q -p no:cacheprovider --basetemp=<hors du dépôt> brouillons/preuves-mentors-v1/reception-r1-relance-v2/tests/test_ecrire_fiches_reception_v2.py`.

- **Mode « avant » (13)** : dépôt git jetable (dossier temporaire de pytest) où les vrais textes scellés sont copiés à
  l'octet ; cas sain (les huit gardes passées, attendus réels vérifiés) ; 11 artefacts : référence `calcul/…`, référence
  `donnees`, configuration citant la table v2, configuration à tolérance changée (canonique), table de version 2, table à
  un `non_resolu`, `manifeste.py` l. 104 changée, addendum à « `signales` = 21 », addendum à `addendum` = v3, analyse
  principale altérée, compagnon faux ; plus commit absent (`[piece]`, R11) et fiche existante (`[R12]`).
- **Mode « après » (39)** : arbre synthétique aux formats du fournisseur, manifeste à la clé `preenregistrement` et à la
  vraie configuration v5, attendus réels du mode « avant » dans une fiche scellée par l'essai (empreintes des juges
  remplacées par celles des octets synthétiques, les vraies ne se fabriquant pas) ; cas sain (les 16 gardes passées dans
  l'ordre, fiches validées par `entrees_v1.lire_fiche` et `entrees_v3.lire_fiche_v3`, aucun nombre dans les fiches) ;
  sentinelles (aucune valeur interdite dans la sortie standard, l'erreur ni les fiches) ; garde `P-R5` en unité (cinq
  fuites) ; filtre en unité ; 33 artefacts : fiche absente, non scellée, modifiée, d'empreinte autre que celle du canal ;
  bloc absent, d'autre format ; run de la première course, run `…-jouet` ; E21 (course = run lu, empreinte mal formée,
  sans annonce, branche `-v1`, annonce sans reprise) ; rattachement (manifeste, résultat, `arret.json`) ; texte (chemin
  v2, empreinte v2) ; commande v1 ; `decisif` faux ; configuration (table v2, canonique, recalcul) ; commit `04bc323a`,
  arbre non propre ; entropie ; table v2 dans le résultat ; provenance v3 ; comptes (147, non résolu, v1 = 14) ; juges
  (empreinte, run) ; reprise E21 notée ; bout en bout (fiche du mode « avant » scellée puis lue, juges absents).
- **Gardes de la v1 portées (9)** : juge 8B absent, rejeu arrêté (motif fermé, aucune valeur interdite ne sort de
  `partiel`), fichier manquant, nom inattendu, empreinte fausse, empreinte déclarée ≠, résultat et arrêt ensemble,
  fiches existantes (deux cas), paramètres hors de forme.

## 4. Mutations — 46 mutants, tous tués (`banc-mutations-v2-sortie.txt`, ≈ 4 min)

`tests/banc_mutations_v2.py` rend chaque garde inopérante (`ctl.exiger("<garde>", lambda: …` devient `… lambda: True or
…`), toutes occurrences ensemble, puis une occurrence à la fois pour les gardes à plusieurs contrôles (`fiche` 4, `e21`
5, `rattachement` 3, `configuration` 3, `commit` 2, `juges` 2, `P-R5` 2) ; le filtre garde le document entier. Témoin
non muté : 61 réussis. Chaque mutant est tué par l'artefact de sa propre garde (tableau dans la sortie).

Audit d'un résultat trop propre (R4), trois défauts trouvés et corrigés en chemin : (a) le banc lui-même : pytest crée
`--basetemp` sans ses parents, d'où « 1 error » partout, témoin compris ; (b) le premier passage par occurrence a laissé
`fiche#1` survivre : mon essai « fiche absente » nommait le fichier « …absente… », et le message de la garde suivante le
reprenait ; nom neutre, fragment « absente (R11 » ; (c) mon premier artefact de la contre-épreuve 0.2 ne remplaçait rien
(motif faux) ; refait, il arrête bien.

## 5. Vérifié sur le dépôt (sans donnée)

- Au commit `139a81d3` : addendum `88e262e2…` (= compagnon) ; configuration `acad6253…`, canonique recalculée
  `1cfb7fba…` (règle de `manifeste.config_canonique`), 29 clés, table v3 et parent cités ; table `ead8a668…` (version 3,
  22 entrées : une_paire 12, identifiants 4, deux_paires 2, fenetre 2, fins 1, trois_paires 1 ; 240 / 151 / 129 / 22 /
  151 ; `non_resolu` 0) ; parent `80c85a00…` ; `git diff --quiet f921fcec 139a81d3 -- src tests scripts` : code 0 ;
  module v3 `0581cf9a…` ; `manifeste.py` `1a5c7464…`, l. 104 `"preenregistrement": prereg_info,` ; scripts `24744794…`,
  `82f38687…`.
- Ce que portera le manifeste, lu dans le code : `commande` = constante l. 65 du module ; `decisif` = `prereg is not
  None` (l. 211) ; `preenregistrement` = chemin relatif et empreinte vérifiée (`manifeste.py` l. 88-96) ; `commit` = tête
  du clone de l'instance (`gardes.etat_git`), que le script d'instance laisse au commit lancé (`git checkout $COMMIT`, puis
  branche neuve sans commit avant le module, l. 87-97, 143, 273-282) ; nom du run `AAAAMMJJ-HHMMSS-r1-rejeu-reel` (l. 275).
- Le résultat écrit `tokenisation.addendum` = constante `prereg/R1-addendum-relance-v2.md` (l. 66, 454) ; les valeurs de
  P-R5 sortent aussi par la sortie standard du module (l. 487-489), recopiée dans les traces (`$TRAVAIL/*.json`, script
  l. 162), et par la ligne `etape=fin` (l. 472) ; le versement (procédure de session-depot `ae1ff089…`, étape 7) ne porte
  que `runs/`, `diag/` et `donnees/` du run.
- Lecteurs `entrees_v1`, `entrees_v3`, `entrees`, `constantes_v1`, `constantes_v3` identiques aux commits cités
  `a8b7fdb2` et `326601cf` ; `redaction` libre pour les deux ; mais l'analyse secondaire scellée, l. 24 : la fiche « ne
  contient que des chemins, des empreintes, des pointeurs » et le motif fermé ; la principale, l. 97 : `redaction` « (qui,
  quand, ce qui a été ouvert) ».
- **Clone superficiel** : `git rev-parse --is-shallow-repository` = `true`, racine greffée `d1b1c8c6` ; `52eb34c8`
  (texte par épisode scellé) et `5f2f9bf5` (son code) absents ; `326601cf` présent mais non atteignable depuis
  `a8b7fdb2` (`git rev-list a8b7fdb2` : 4 commits). Le bloc A1 de la v1 s'arrêterait ; son étape F ne pourrait pas
  fusionner. Le texte par épisode lui-même (`26a3ff72…`) est commité à la tête de la branche de travail.
- Aucune fiche JSON n'existe (`git log --all`), aucune référence `calcul/…`, aucun arbre séparé.

## 6. Empreintes (sha256) des fichiers de ce dossier

| fichier | sha256 |
|---|---|
| `procedure-reception-lecture-r1-relance-v2.md` | `829e31816a0467daf81dd43456723b0fe10e9f73b8123a23ad81a1d43c05eb8a` |
| `ecrire_fiches_reception_v2.py` | `d4701213e20b08b9dc9cab45e318c869c1f5ec0ee1fe36cb29ac723caea4c7b3` |
| `tests/test_ecrire_fiches_reception_v2.py` | `19d9b737289591ca98c021772468e06e7e7ee51a92cc48859386fa1124fab2b7` |
| `tests/banc_mutations_v2.py` | `9a945575bdade2a19eac1933407979358199aa3d5ba48829c88804708246f3cc` |
| `essais-v2-sortie.txt` | `d0c31ffa4966cf702d5a7ea9e1aeed7b1617b5611260b38654f780451b4e5cef` |
| `banc-mutations-v2-sortie.txt` | `0510c10424b71b6179ebb0093299ab1c3eea14f808730cac4ef8d024c82f2f92` |
| `fiche-reception-r1-relance-v3-v1.md` | `47e4b6ac3cddb4afbc38eac4b8c5ca96b13c1d753e7ffa20fbc95622cdc3e3cb` |
| ce rapport | rendu à l'appelant (il ne peut pas se citer) |

## 7. Cinq points pour un contre-lecteur

1. **Commit strict.** La garde `commit` exige `139a81d3…` exactement. Une création au commit `04bc323a` (descendant sur
   `prep/r1-relance-v3`, notes seules) arrêterait la réception. Est-ce bien la lecture voulue de « `COMMIT_SCELLEMENT` =
   commit de scellement de ce texte » (écart = nœud), plutôt qu'accepter un descendant au code identique ?
2. **Liste des valeurs interdites et règle « aucun nombre ».** Vérifier que la liste est complète et juste : elle exclut
   aussi `regle_repli_appliquee` et `lecture` (résolus seulement pour leur existence ; la secondaire les lit par pointeur),
   ainsi que `activations_identiques_au_bit`. Vérifier aussi que retirer toute valeur des fiches JSON (la v1 recopiait une
   liste dans `notes`) respecte la secondaire l. 24 et la principale l. 97, sans rien ôter qu'un lecteur exige.
3. **Étape A0 non éprouvée.** `git fetch --unshallow` avec trois refspecs n'a pas pu être essayé (réseau interdit au
   sous-agent). Ramène-t-il `52eb34c8` et `5f2f9bf5` ? Rend-il l'ascendance `326601cf` → `a8b7fdb2` visible ? Et ces
   commits sont-ils bien dans l'historique de `canal/conv-audit-n04` ?
4. **Concordance sur la version scellée hors de la fiche.** Elle n'est qu'une précondition (P2), parce qu'elle n'existait
   pas à l'écriture. Est-ce acceptable, ou faut-il une fiche v2 qui la cite ? De même, 2 236 et 1 782 ne sont pas
   dérivables de la table : ils ne sont vérifiés que contre le texte de l'addendum.
5. **Le bloc d'attendus gouverne le mode « après ».** Le script fait confiance au bloc scellé (empreinte = celle du canal)
   plutôt qu'à ses propres constantes. Vérifier que le bloc égale les sections 3 à 7 de la fiche (même dictionnaire). Vérifier
   aussi que le traitement de E21 suit E21 et C-8 de l'addendum : branche `-v2` si et seulement si reprise ; course
   arrêtée notée, jamais ouverte ; ses lignes de journal dans un fichier à part, scellé, pour les lecteurs R13.

## 8. Ce que je n'ai pas fait ; écarts déclarés

- Aucun arbre séparé ni branche créés : les sorties attendues de l'étape B (essais de la principale, versions gelées)
  sont celles de la v1, non revérifiées ici (le blob P3 `bad1403f…` l'a été par `git rev-parse`).
- Dossiers temporaires hors du dépôt : `/tmp/reception-r1-relance-v2-essais/`, `/tmp/banc-reception-v2-essai1` à
  `-essai4`, `-diag`, `-final`, `-final2` et leurs journaux ; les essais créent des dépôts git jetables (`git init`,
  commit) dans les dossiers temporaires de pytest, jamais dans le dépôt de travail.
- `python -I -m py_compile` a écrit un `__pycache__` dans ce dossier : retiré aussitôt ; vérifié ensuite qu'aucun cache
  n'a été créé ni modifié depuis 05:21 UTC hors de `.venv`.
- Trois sorties écrites avec l'avant-dernier état du script ont été effacées, puis régénérées avec le script final.
  Aucune n'avait été scellée, commitée ni remise : fiche `bab9e9ac…`, essais `1e3c3906…`, banc `328b3859…`.
- La tête de la branche de travail a avancé pendant ma session, par les commits de la session (de `4c0aca4c` à `2bd8147d`).
  La fiche cite `2bd8147d` pour les pièces lues à la tête ; leurs empreintes sont fixes.
- Deux fichiers non suivis d'autres agents sont apparus pendant ma session ; je n'y ai pas touché :
  `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/verification-differences-r1-v3-et-complement-v1.md` (depuis
  commité par la session) et `brouillons/reception-nul-v9-validation-v1/audit-validation-nul-v9-v1.md`.
- Ce dossier n'a aucun compagnon `.sha256` (consigne) : la session scelle les huit fichiers à l'étape 0.3.
