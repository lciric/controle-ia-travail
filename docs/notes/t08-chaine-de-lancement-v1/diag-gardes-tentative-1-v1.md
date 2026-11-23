# Diagnostic de l'arrêt de la course de T0.8 pendant les gardes de l'instance (tentative 1) — v1

Développeur de la chaîne de lancement, le 23 novembre 2026, sur la demande de la session mère (04:54Z). Sans dépense,
sans machine, rien poussé sur `main`. Branche `diag/t08-gardes-tentative-1-v1`, partie du commit C (`bd32f9a5c`).

**Lu** : le journal de l'exécutante (`docs/procedures/t08-course-v1/executante/journal-executante-t08-v1.md`, branche
`t08/journal-executante-course-v1`, commit `94ace0330`, ses dernières lignes) ; le code de l'amorce et de la garde au
commit C. **Non lu** : les lignes de service de l'instance sur `calcul/t08-course-v1` — la récupération de cette branche
m'a été refusée par l'outil (mon mandat exclut toute branche `calcul/…`) ; je ne l'ai pas contournée. Les faits de
l'instance viennent donc du journal de l'exécutante.

## 1. Cause

**La garde de l'instance (`entrees_v1.exiger_instance_sans_interdits`, code aligné) lance `git rev-list --all --objects`
dans le clone partiel de l'amorce (`--filter=blob:none`). Dans un clone partiel, git va chercher chaque blob manquant, un
par un, chez le dépôt distant (téléchargement paresseux). L'arbre du seul commit C porte 45 444 fichiers (5,5 Go), et
`--all` parcourt toute l'histoire de la branche du code : des dizaines de milliers d'allers-retours vers GitHub. Le bloc
des gardes tourne sous `timeout -k 10 900` (amorce, l. 465) : coupé à 900 s.**

- Chronologie (journal de l'exécutante) : matériel et torch à 04:24:56Z ; « gardes avant tout calcul : » (message vide)
  à 04:40:00Z, soit 15 min 4 s plus tard, c'est-à-dire le délai de 900 s, plus quelques secondes de `import torch` et des
  deux contrôles de la carte qui précèdent le bloc.
- **Message vide** : `timeout` tue le programme Python (code 124) avant toute impression ; la sortie capturée est vide,
  et l'amorce imprime sa dernière ligne (`tail -n 1` d'un texte vide). L'amorce ne distingue pas la coupure par le délai
  d'un arrêt de garde.
- **Pourquoi l'essai de bout en bout ne l'a pas vu** : son clone était bien partiel (le dépôt distant de l'essai admet le
  filtre), mais l'arbre de son code ne portait qu'environ 1 800 objets, servis en local ; la garde y a pris 2 s
  (journal de l'essai au commit C : « gardes conformes (jouet) : 1775 fichiers, 1842 objets git », 21:52:45Z → 21:52:47Z).
  Le mécanisme était là ; l'échelle et le réseau manquaient.

**Reproduction sur processeur** (`tests/test_t08_garde_clone_partiel_v1.py`) : un dépôt servi avec le filtre, 300 blobs,
cloné en clone partiel ; on compte les objets que la garde télécharge.
- Au commit C (avant correctif) : la garde télécharge **300 objets** sur 300 (« 300 objets téléchargés par la garde (clone
  partiel) ») ; deux essais échouent. Un essai à part, à 1 000 blobs, en local : 16 s, environ 16 ms par blob ; sur GitHub,
  chaque blob coûte un aller-retour réseau et un processus `git fetch`.
- `git log --all --root --no-renames -m --name-only` (seconde passe de la garde) ne télécharge rien : il ne lit que les
  arbres, que le clone partiel porte.

**Confiance : haute** (de l'ordre de 9 sur 10). Ce qui la borne : je n'ai pas lu les traces de l'instance (`nvidia-smi`,
`pip-freeze`, journal complet) ; la durée par blob sur GitHub n'est pas mesurée ici. Ce qui la porte : le délai de 900 s
exact, le message vide propre à une coupure par `timeout`, la reproduction du mécanisme, et l'absence de tout autre
parcours de l'histoire dans le code joué à cette étape (relevé : seule la garde appelle `rev-list --objects` et
`log --all`).

## 2. Panne de l'environnement ou erreur de la chaîne ?

**Erreur de la chaîne**, pas de l'environnement. La garde resserrée (code aligné) et le clone partiel de l'amorce
(chaîne) sont incompatibles à l'échelle de la branche réelle ; aucun délai raisonnable ne la sauve (des dizaines de
milliers d'allers-retours). Deux défauts de la chaîne s'y ajoutent : le message perdu (amorce), et un essai de bout en
bout trop petit pour révéler un coût proportionnel à la taille de l'histoire (essai).

## 3. Correctif minimal proposé (sur cette branche, pas dans C)

1. **Code aligné, une ligne** — `src/controle_ia/t08/entrees_v1.py` : `rev-list --all --objects --missing=allow-promisor`.
   Un blob promis par le dépôt distant et absent du clone n'est pas dans la copie de l'instance (ce que la garde protège) ;
   git ne va plus le chercher. Son chemin reste contrôlé par la seconde passe (chemins de tous les commits, arbres
   seuls). Un objet manquant qui n'est pas promis arrête toujours (« objets git illisibles »). Dans un clone complet
   (essais du dépôt), rien ne change. Drapeau connu de git depuis la version 2.17 (image `python:3.11-bookworm` : 2.39).
   Essais : les trois de `tests/test_t08_garde_clone_partiel_v1.py` passent (cas sain sans téléchargement ; artefact :
   `resume.json` de 7b dont le blob manque, arrêté sans téléchargement ; constat de la cause) ; les essais de la garde
   existants (`test_t08_entrees_rendu_v1.py`, `test_t08_gardes_corrections_v1.py`) : 52 passés.
2. **Amorce, recommandé** — le message d'arrêt des gardes dit le code et, à 124 ou 137, « délai de 900 s dépassé » au lieu
   d'une ligne vide. Éprouvé sur un extrait (commande coupée : « aucune sortie (code 124) : délai de 900 s dépassé » ;
   arrêt de garde : son message, inchangé).
3. La liste figée des essais n'est pas touchée (le nouvel essai se joue dans la session) : son empreinte et le nombre
   attendu (255) restent.

## 4. Ce que le correctif change aux empreintes scellées, et la vérification qu'il demande

- **Le code de `src/` change** (point 1) : nouveau commit du code (C2), donc :
  - le marqueur `COMMIT_CODE_T08` du texte scellé cite C : **le texte est à remplir et sceller de nouveau** (programme de
    scellement, nouveau nom de version), ainsi que la configuration de la course (qui porte ce marqueur), la branche
    d'entrée (elle cite le commit du code), la ligne `CODE-T08` et une pièce des empreintes neuve au commit C2 ;
  - c'est un changement du code d'un préenregistrement scellé, après scellement : **nœud pour Lazar**, à mon sens
    (écart au texte scellé, même sans rien changer à l'analyse ; la garde change de moyen, pas d'objet).
- **EA** (empreinte de l'amorce) change seulement avec le point 2.
- **Vérification demandée** : contre-lecture du différentiel (classe B, autre modèle) — une ligne de code, l'essai neuf,
  le message de l'amorce ; mutation : retirer le drapeau doit faire échouer les deux essais de la garde (fait ici :
  c'est l'état du commit C) ; suite de T0.8 et essai de bout en bout rejoués au commit C2.
- **Sans changer le code** : je n'ai pas trouvé de voie honnête. Un clone complet ou peu profond de C télécharge 5,5 Go
  d'un coup (arbre de C), et le parcours resterait à faire ; une enveloppe autour de `git` qui ajouterait le drapeau à
  l'insu de la garde contre-lue la changerait sans le dire.
- **Risque résiduel** : la seconde passe (`git log --all -m --name-only`) parcourt toute l'histoire de la branche du code,
  arbres seuls, en local ; non mesurée à l'échelle de `main`. Le message du point 2 la nommerait si elle dépassait le
  délai.
