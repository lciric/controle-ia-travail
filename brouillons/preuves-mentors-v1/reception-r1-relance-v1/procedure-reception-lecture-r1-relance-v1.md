# Procédure de réception et de lecture du run R1 relancé — v1

Pour la session principale, dès que le fournisseur annonce le versement du run R1 relancé sur `calcul/r1-r2-reel-v1`
(commit neuf en avance rapide). Elle enchaîne, dans cet ordre et sans lecture entre deux : constat, récupération, fiches
scellées et commitées, lancement décisif de l'analyse principale, lecture par épisode, analyse secondaire, verdicts R13.
Écrite sans aucune donnée (rapport joint : `rapport-preparation-reception-v1.md`) ; le script des fiches,
`ecrire_fiches_reception_v1.py`, a ses essais dans `tests/` de ce dossier (12 essais, R5).

**Règle générale** (celle de la procédure de l'analyse principale, `procedure-scellement-analyse-principale-r1-r2-v1.md`,
section F) : chaque bloc dit ce qu'il doit afficher pour continuer ; tout autre affichage, ou un code de sortie non nul,
**arrête la procédure** : rien n'est lancé, rien n'est corrigé à la main dans un arbre séparé, Lazar est prévenu. Une
fiche déjà scellée et commitée ne se réécrit pas : version nouvelle, nom nouveau (R12).

Règles qui valent du début à la fin :
- aucun fichier `.npz` n'est ouvert par la session ; les résultats JSON du fournisseur ne sont ouverts que par le script
  des fiches (clés nommées, consignées dans `redaction`) ;
- aucun `git merge` de `calcul/r1-r2-reel-v1` ; `donnees/<run>/` passe hors index (`git show > fichier`) ;
- aucune écriture sous `donnees/20261019-230011-p3-reel/` ;
- `nice -n 10` pour tout calcul ; une seule session shell (les variables ci-dessous vivent du début à la fin).

## Préconditions (points d'arrêt, consignés au registre avant l'étape A)

| n° | précondition | preuve attendue |
|---|---|---|
| P1 | **Addendum v2 scellé** chez le fournisseur : `prereg/R1-addendum-relance-v2.md`, empreinte `$ADDENDUM_SHA` (paramètre de cette procédure, à remplir dans le bloc des variables), commit de scellement, table v3 scellée | message du fournisseur (n° 260 ou suivant), `git show <commit>:prereg/R1-addendum-relance-v2.md \| sha256sum` = `$ADDENDUM_SHA` (branche déjà récupérée par refspec `prep/…`, jamais `calcul/…`) |
| P2 | **Concordance finale** de l'addendum v2 avec nos trois textes scellés, par un lecteur neuf (auteur d'aucun des textes), sur la version scellée (points 1 à 6 de `concordance-addendum-r1-brouillon3-v1.md`, dernière section, adaptés au v2 : rejeu à graine, table v3, liste des épisodes non inversibles) ; rapport scellé, commité | chemin et empreinte du rapport ; verdict « concordant » ; **liste `$NON_INVERSIBLES`** (vide si l'addendum v2 n'en déclare aucun) recopiée du rapport |
| P3 | Les trois textes scellés inchangés : principale `8e267952…` (branche `analyse-principale-r1-r2-v1`, commit `83ce7a91`), secondaire `1f6a6da2…` (`analyse-blanche-noire-v3`, `7a238666`), par épisode `26a3ff72…` (`52eb34c8` sur la branche de travail) | bloc A1 |
| P4 | Message du fournisseur donnant **le commit du versement** (`$VERSEMENT`) et **le nom du run relancé** (`$REJEU`) ; les juges restent ceux déjà versés : `20261102-004328-r2-juge3b-reel`, `20261102-005048-r2-juge8b-reel` (addendum v1, brouillon 3, « R2 ») | message n°, empreinte ; aucun nom n'est deviné depuis l'arbre |
| P5 | Aucun arbre séparé existant aux chemins ci-dessous, aucune branche locale de ces noms | bloc A2 |

## Variables

```bash
DEPOT=/home/claude/controle-ia-travail
ARBRE_P=/home/claude/controle-ia-analyse-principale-r1-r2-v1   # arbre de la principale, recréé (n'existe pas)
ARBRE_S=/home/claude/controle-ia-analyse-bn-v3                 # arbre de la secondaire, recréé (n'existe pas)
BR_P=analyse-principale-r1-r2-v1 ; BR_S=analyse-blanche-noire-v3
CITE_P=a8b7fdb2dd7f68e7f3789720936ae074dd362f0c ; SCELLE_P=83ce7a91f681b36668a9f91424d53ebd632b50b1
CITE_S=326601cf39d91754ceb13813f10c47a8e6f4a465 ; SCELLE_S=7a238666630a6d6dca064e8da6b309320060200d
CITE_E=5f2f9bf505b4b57ccd3df71178d0a1f596e97899 ; SCELLE_E=52eb34c8   # lecture par épisode (texte scellé commité)
PY=$DEPOT/.venv/bin/python
SCRIPT=$DEPOT/brouillons/preuves-mentors-v1/reception-r1-relance-v1/ecrire_fiches_reception_v1.py
FICHE_P=prereg/fiche-reception-principale-r1-r2-v1.json ; FICHE_S=prereg/fiche-reception-blanche-noire-v3.json
PREREG_P=prereg/analyse-principale-r1-r2-v1.md ; PREREG_S=prereg/analyse-blanche-noire-v3.md
PREREG_E=prereg/analyse-par-episode-v1.md
J3=20261102-004328-r2-juge3b-reel ; J8=20261102-005048-r2-juge8b-reel
# --- à remplir au moment du versement, depuis les messages du fournisseur et le rapport de concordance (P1, P2, P4) ---
ADDENDUM_SHA=                     # 64 hex : empreinte de prereg/R1-addendum-relance-v2.md scellé
VERSEMENT=                        # 40 hex : commit du versement sur calcul/r1-r2-reel-v1
REJEU=                            # nom du run R1 relancé, AAAAMMJJ-HHMMSS-…
NON_INVERSIBLES=                  # vide, ou liste séparée par des virgules recopiée de l'addendum v2 (E19)
QUI="session conv-audit (Claude), session <id>"
SCR=/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/reception-r1-relance-v1 ; mkdir -p "$SCR"
export PYTHONDONTWRITEBYTECODE=1
```

## A. Constat (dépôt principal) — ≈ 1 minute

### A1. Références et textes scellés

```bash
cd $DEPOT && git for-each-ref --format='%(refname) %(objectname)' 'refs/heads/calcul/*' 'refs/remotes/origin/calcul/*'; echo "fin de liste"
git rev-parse origin/$BR_P origin/$BR_S $SCELLE_E
git show origin/$BR_P:$PREREG_P | sha256sum ; git show origin/$BR_S:$PREREG_S | sha256sum ; git show $SCELLE_E:$PREREG_E | sha256sum
git merge-base --is-ancestor $CITE_S $CITE_P && git merge-base --is-ancestor $CITE_E HEAD && echo "ordre des commits cités conforme"
git diff --quiet $CITE_E $SCELLE_E -- src tests && echo "code par épisode inchangé entre commit cité et texte scellé"
git merge-tree --write-tree --name-only $SCELLE_P $SCELLE_E > "$SCR/fusion-anticipee.txt"; echo "fusion anticipée : code $? ; $(wc -l < "$SCR/fusion-anticipee.txt") ligne(s)"
test -n "$ADDENDUM_SHA" -a -n "$VERSEMENT" -a -n "$REJEU" && echo "paramètres remplis"
```

**Doit afficher :**
- la liste des références `calcul/*` du dépôt, puis `fin de liste` : les noter telles quelles (constat du 2 novembre : aucune) ; aucun fichier de ces références n'est ouvert ;
- `83ce7a91…`, `7a238666…`, `52eb34c8…` ;
- `8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537`, `1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9`, `26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4` ;
- `ordre des commits cités conforme` ; `code par épisode inchangé …` ;
- `fusion anticipée : code 0 ; 1 ligne(s)` (l'arbre résultant seul, aucun fichier en conflit ; vérifié ainsi le 2 novembre) ;
- `paramètres remplis`.

### A2. Arbres et branches libres

```bash
cd $DEPOT && git worktree list && test ! -e "$ARBRE_P" && test ! -e "$ARBRE_S" \
  && ! git show-ref --quiet refs/heads/$BR_P && ! git show-ref --quiet refs/heads/$BR_S && echo LIBRE
```

**Doit afficher** la liste des arbres (le dépôt seul) puis `LIBRE`. Sinon : arrêt (un arbre ou une branche locale de ce nom existe déjà ; ne rien supprimer, signaler).

## B. Arbre séparé de la principale, recréé — ≈ 2 minutes (essais compris, 20 à 40 s)

```bash
cd $DEPOT && git worktree add -b "$BR_P" "$ARBRE_P" "origin/$BR_P"
cd "$ARBRE_P" && test "$(git rev-parse HEAD)" = "$SCELLE_P" && echo "HEAD = texte scellé" && git status --porcelain --untracked-files=all | wc -l
test "$(git rev-parse HEAD~1)" = "$CITE_P" && echo "parent = commit cité" && git diff --quiet "$CITE_P" HEAD -- src tests && echo "code identique au commit cité"
PYTHONPATH=src $PY -c "import controle_ia; print(controle_ia.__file__)"
PYTHONPATH=src $PY -c "from controle_ia.analyse_principale_r1_r2 import lecture_v1; print(lecture_v1.exiger_versions())"
PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG_P'))"
git rev-parse HEAD:donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
sha256sum donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl donnees/20261019-230011-p3-reel/scores-p3.npz
PYTHONPATH=src $PY -m controle_ia.scellement verifier donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl \
  donnees/20261019-230011-p3-reel/scores-p3.npz diag/20261019-230011-p3-reel/resume.json \
  diag/20261019-230011-p3-reel/episodes-p3.json diag/20261019-230011-p3-reel/sondes-figees.json
PYTHONPATH=src:tests nice -n 10 $PY -m pytest -q -p no:cacheprovider --basetemp="$SCR/essais-arbre-p" \
  tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py 2>&1 | tail -1
git status --porcelain --untracked-files=all | wc -l ; ls runs | grep -c . ; ls donnees | grep -v -c 20261019-230011-p3-reel
```

**Doit afficher :** la création de l'arbre ; `HEAD = texte scellé`, `0` ; `parent = commit cité`, `code identique au commit cité` ;
`/home/claude/controle-ia-analyse-principale-r1-r2-v1/src/controle_ia/__init__.py` ; `{'python': '3.13.18', 'numpy': '2.4.6', 'scipy': '1.17.1'}` ;
`8e267952…` ; `bad1403f1454f46de23adbbee59da8586170c7ec` ; `ba05fa13…` et `968414fc…` ; cinq sceaux conformes ; `24 passed` ; `0` ;
le nombre de manifestes déjà suivis sous `runs/` (noter) ; `0` (aucun dossier sous `donnees/` hors P3 : l'arbre est neuf).

## C. Récupération de `calcul/r1-r2-reel-v1` seule, dans l'arbre de la principale — ≈ 1 à 3 minutes (réseau)

```bash
cd "$ARBRE_P" && git fetch --no-tags origin "+refs/heads/calcul/r1-r2-reel-v1:refs/remotes/origin/calcul/r1-r2-reel-v1" && git rev-parse FETCH_HEAD origin/calcul/r1-r2-reel-v1
test "$(git rev-parse FETCH_HEAD)" = "$VERSEMENT" && echo "versement = commit annoncé"
git status --porcelain --untracked-files=all | wc -l ; ls donnees | grep -v -c 20261019-230011-p3-reel
git ls-tree -d --name-only FETCH_HEAD runs/ diag/ donnees/
git show FETCH_HEAD:diag/20261102-002114-r1-rejeu-reel/arret.json | sha256sum
git ls-tree -r --name-only FETCH_HEAD "runs/$REJEU" "diag/$REJEU" "donnees/$REJEU" "runs/$J3" "diag/$J3" "donnees/$J3" "runs/$J8" "diag/$J8" "donnees/$J8"
```

**Doit afficher :**
- deux fois le même commit, puis `versement = commit annoncé` (sinon : arrêt, le fournisseur n'a pas annoncé ce commit) ;
- `0` ; `0` (le fetch n'a rien écrit dans l'arbre ni dans l'index : « `donnees` = 0 », aucun dossier sous `donnees/` hors P3, comme en B) ;
- la liste des runs par nom seulement : on y attend `20261102-002114-r1-rejeu-reel` (première course, arrêtée), `$J3`, `$J8`, le run de R4 (arrêté), le ou les runs du rejeu à graine, et `$REJEU` ; **tout nom absent de cette attente est noté, aucun fichier n'en est ouvert** ;
- `c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07` (l'`arret.json` de la première course est intact ; haché par un tube, jamais ouvert) ;
- la liste exacte des fichiers des trois runs à recevoir, soit, pour `$REJEU` : `runs/$REJEU/manifeste.json`, `diag/$REJEU/rejeu-activations.json` (ou `arret.json`), les trois `donnees/$REJEU/activations-p3-rejeu-v1{,-maximum,-complement-hors-cout}.npz`, et leurs compagnons `.sha256` ; pour chaque juge : `manifeste.json`, `juge-actions.json`, `scores-juge{3b,8b}-p3-v1.npz` et compagnons. **Un nom en plus ou en moins arrête** (le script de D le refuse aussi).

Puis écriture des fichiers, index pour `runs/` et `diag/` seulement :

```bash
cd "$ARBRE_P" && for R in "$REJEU" "$J3" "$J8"; do
  git checkout FETCH_HEAD -- "runs/$R" "diag/$R" || { echo "ARRÊT checkout $R"; break; }
  for f in $(git ls-tree -r --name-only FETCH_HEAD "donnees/$R"); do test ! -e "$f" || { echo "EXISTE $f : ARRÊT"; break 2; }
    mkdir -p "$(dirname "$f")"; git show "FETCH_HEAD:$f" > "$f"; done
done; echo "écriture faite"
PYTHONPATH=src $PY -m controle_ia.scellement verifier $(git ls-tree -r --name-only FETCH_HEAD "donnees/$REJEU" "diag/$REJEU" "runs/$REJEU" "donnees/$J3" "diag/$J3" "runs/$J3" "donnees/$J8" "diag/$J8" "runs/$J8" | grep -v '\.sha256$') | grep -c '^OK'
git add -- "runs/$REJEU" "diag/$REJEU" "runs/$J3" "diag/$J3" "runs/$J8" "diag/$J8"
git commit -q -m "Réception R1 relancé et juges : runs/ et diag/ du fournisseur ($(git rev-parse --short=8 FETCH_HEAD) sur calcul/r1-r2-reel-v1)" \
  -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013QMaynBnMGnUDJtNQkv8KX" -- "runs/$REJEU" "diag/$REJEU" "runs/$J3" "diag/$J3" "runs/$J8" "diag/$J8"
git show --name-only --format= HEAD | grep -v -c -E "^(runs|diag)/" ; git status --porcelain --untracked-files=all | wc -l
```

**Doit afficher :** `écriture faite` sans `ARRÊT` ni `EXISTE` ; le compte des `OK` égal au nombre de fichiers hors compagnons
(11 si le rejeu est allé au bout : 3 manifestes + 1 résultat + 3 `.npz` du rejeu + 2 × (1 résultat + 1 `.npz`)) ; `0` (le
commit ne porte que `runs/` et `diag/`) ; `0` (arbre propre : `donnees/` est ignoré). Durée mesurée de la vérification
des sceaux sur trois fichiers de 59 Mo : 0,3 s.

## D. Fiches de réception, écrites par le script, scellées et commitées **avant toute lecture** — ≈ 3 minutes

### D1. Écriture (le script liste, hache, compare aux compagnons, n'ouvre aucun `.npz`)

```bash
cd "$ARBRE_P" && nice -n 10 $PY -I "$SCRIPT" --racine . --rejeu "$REJEU" --juge3b "$J3" --juge8b "$J8" --qui "$QUI" \
  --commit-versement "$(git rev-parse FETCH_HEAD)" --addendum-sha256 "$ADDENDUM_SHA" \
  --episodes-non-inversibles-declares "$NON_INVERSIBLES" --ouvrir-resultats 2>&1 | tee "$SCR/fiches-$REJEU.txt"; echo "code ${PIPESTATUS[0]}"
```

**Doit afficher :** une ligne `contexte déclaré du juge 3B …` (à lire : s'il contient la consigne ou l'indication privée
d'un épisode, **arrêt** : la secondaire exige `R2: null` avec `consigne_dans_contexte` — cas non prévu par le script,
fiche à écrire à la main et à soumettre ; nœud) ; `fiche principale : … <empreinte>` ; `fiche secondaire : … <empreinte>` ;
`fichiers vérifiés contre leur compagnon : 11` ; `ouverts : [… rejeu-activations.json, … juge-actions.json × 2]` ; `code 0`.

Ce que le script a vérifié en ouvrant les trois résultats JSON (clés nommées, jamais de tableau ni de nombre de
résultat) : `run_id` ; `verdict_fidelite` = « conforme » ; `fichiers` du résultat = empreintes des `.npz` versés ;
pointeurs de la fiche secondaire résolus ; `tokenisation.episodes_non_resolus` **= `$NON_INVERSIBLES`** (sinon `ARRÊT … E19`,
code 2, aucune fiche écrite : nœud de Lazar, la décision ne couvre que les épisodes que l'addendum v2 nomme).

Si le rejeu s'est arrêté (`arret.json` et pas de `donnees/$REJEU`) : même commande ; le script écrit `R1: null` avec le
motif fermé lu dans `verdict_fidelite` (`rejeu_non_conforme` ou `rejeu_en_echec`) et la preuve dans `redaction` ; la
principale lit alors « rejeu non validé : rien n'est lu » ; la suite (E à H) se fait quand même, car les lectures sont
rapportées en entier quel qu'en soit le signe, mais la lecture par épisode ne lit rien non plus (sa l. 111).

### D2. Contrôle de forme par les deux lecteurs, sans donnée, puis scellement et commit de la fiche principale seule

```bash
cd "$ARBRE_P" && PYTHONPATH=src $PY -c "from pathlib import Path; from controle_ia.analyse_principale_r1_r2.entrees_v1 import lire_fiche; print(lire_fiche(Path('.'), '$FICHE_P', scellee=False)[1])"
PYTHONPATH=src $PY -c "from pathlib import Path; from controle_ia.analyse_blanche_noire.entrees_v3 import lire_fiche_v3; print(lire_fiche_v3(Path('.'), '$FICHE_S', scellee=False)[1])"
$PY -c "import json; f=json.load(open('$FICHE_P')); print(f['R1'] is not None, f['motif_R1'], f['R2']['juge8b'] is not None, f['motif_R2'])"
PYTHONPATH=src $PY -m controle_ia.scellement sceller "$FICHE_P"
cp "$FICHE_S" "$SCR/fiche-secondaire-a-copier.json" && sha256sum "$FICHE_S" "$SCR/fiche-secondaire-a-copier.json" && rm "$FICHE_S"
git add "$FICHE_P" "$FICHE_P.sha256" && git commit -q -m "Analyse principale de R1-R2 : fiche de réception scellée (R1 relancé $REJEU)" \
  -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013QMaynBnMGnUDJtNQkv8KX" -- "$FICHE_P" "$FICHE_P.sha256"
git show --name-only --format= HEAD ; git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_P"
```

**Doit afficher :** les deux empreintes des fiches (les lecteurs n'ont rien levé ; le code de `entrees_v3` est identique
dans cet arbre et au commit cité `326601cf`, vérifié le 2 novembre) ; `True None True None` (rejeu livré, deux juges) ;
l'empreinte scellée de la fiche principale ; les deux copies de la fiche secondaire d'empreinte égale (elle est retirée
de cet arbre : elle appartient à l'arbre de la secondaire, D3) ; exactement `prereg/fiche-reception-principale-r1-r2-v1.json`
et son compagnon ; `0` ; un push réussi.

### D3. Arbre de la secondaire, recréé ; sa fiche scellée et commitée seule, toujours avant toute lecture

```bash
cd $DEPOT && git worktree add -b "$BR_S" "$ARBRE_S" "origin/$BR_S" && cd "$ARBRE_S"
test "$(git rev-parse HEAD)" = "$SCELLE_S" && test "$(git rev-parse HEAD~1)" = "$CITE_S" && git diff --quiet "$CITE_S" HEAD -- src tests && echo "arbre S conforme"
PYTHONPATH=src $PY -c "import controle_ia; print(controle_ia.__file__)" ; PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG_S'))"
sha256sum donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl donnees/20261019-230011-p3-reel/scores-p3.npz | cut -c1-12
cp "$SCR/fiche-secondaire-a-copier.json" "$FICHE_S" && sha256sum "$FICHE_S" | cut -c1-12
PYTHONPATH=src $PY -c "from pathlib import Path; from controle_ia.analyse_blanche_noire.entrees_v3 import lire_fiche_v3; print(lire_fiche_v3(Path('.'), '$FICHE_S', scellee=False)[1])"
PYTHONPATH=src $PY -m controle_ia.scellement sceller "$FICHE_S" && git add "$FICHE_S" "$FICHE_S.sha256" && git commit -q -m "Analyse boîte blanche / boîte noire v3 : fiche de réception scellée (R1 relancé $REJEU)" \
  -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013QMaynBnMGnUDJtNQkv8KX" -- "$FICHE_S" "$FICHE_S.sha256"
git show --name-only --format= HEAD ; git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_S"
```

**Doit afficher :** `arbre S conforme` ; `/home/claude/controle-ia-analyse-bn-v3/src/controle_ia/__init__.py` ; `1f6a6da2…` ;
`ba05fa13…` et `968414fc…` (P3 suivi par git, vérifié, jamais copié par-dessus) ; l'empreinte de la fiche (celle de D1 et
de D2 : identique à l'octet) ; la même empreinte par le lecteur ; exactement `prereg/fiche-reception-blanche-noire-v3.json`
et son compagnon ; `0` ; un push réussi. (Les fichiers que la fiche cite ne sont pas encore dans cet arbre : ils y sont
écrits en H, où leur empreinte est confrontée à la fiche avant le lancement.)

**À ce point, consigner au registre** : `$REJEU`, le commit du versement, les deux empreintes des fiches et leurs commits,
ce que le script a ouvert, et « aucune lecture n'a eu lieu ».

## E. Lancement décisif de l'analyse principale — ≈ 1 à 5 minutes (mesuré : 9,8 s de calcul à la taille réelle sur données synthétiques non compressées ; plus la décompression des trois fichiers)

```bash
cd "$ARBRE_P" && RUN_P=$(date -u +%Y%m%d-%H%M%S)-analyse-principale-r1-r2-v1 && echo "$RUN_P"
PYTHONPATH=src nice -n 10 $PY -m controle_ia.analyse_principale_r1_r2.lecture_v2 --fiche "$FICHE_P" --run-analyse "$RUN_P" --prereg "$PREREG_P" > "$SCR/lancement-$RUN_P.txt" 2>&1; echo "code $?"
ls "runs/$RUN_P" "diag/$RUN_P" && PYTHONPATH=src $PY -m controle_ia.scellement verifier "diag/$RUN_P/analyse-principale-r1-r2-v1.json" "diag/$RUN_P/analyse-principale-r1-r2-v1.md" | grep -c '^OK'
git add -- "runs/$RUN_P" "diag/$RUN_P" && git commit -q -m "Analyse principale de R1-R2 : sorties de la lecture décisive $RUN_P" \
  -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013QMaynBnMGnUDJtNQkv8KX" -- "runs/$RUN_P" "diag/$RUN_P"
git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_P"
```

**Doit afficher :** `code 0` ; `manifeste.json`, les deux sorties `.json` et `.md` avec compagnons ; `2` ; `0` ; un push réussi.
Un `ARRÊT : …` dans `$SCR/lancement-*.txt` se consigne avec son motif ; **aucun second passage** sans l'accord de Lazar,
qui ne peut porter que sur la cause technique (manifeste déjà écrit = texte épuisé). Ne pas lire l'issue avant d'avoir
commité et poussé ; la session la lit ensuite (elle n'est pas le lecteur R13).

## F. Lecture par épisode : fusion du commit cité, puis lancement — ≈ 2 minutes (mesuré : 2,0 s de calcul, synthétique, non décisif)

```bash
cd "$ARBRE_P" && git merge --no-edit "$SCELLE_E" ; echo "code $?"
git diff --quiet "$CITE_E" HEAD -- src tests && echo "code = commit cité de la lecture par épisode" ; git status --porcelain --untracked-files=all | wc -l
PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG_E'))"
PYTHONPATH=src $PY -m controle_ia.scellement verifier "$FICHE_P" "diag/$RUN_P/analyse-principale-r1-r2-v1.json" | grep -c '^OK'
PYTHONPATH=src $PY -c "from controle_ia.analyse_principale_r1_r2 import lecture_v1; print(lecture_v1.exiger_versions())"
RUN_E=$(date -u +%Y%m%d-%H%M%S)-analyse-par-episode-v1 && echo "$RUN_E"
PYTHONPATH=src nice -n 10 $PY -m controle_ia.analyse_principale_r1_r2.lecture_v5 --fiche "$FICHE_P" --principale "diag/$RUN_P/analyse-principale-r1-r2-v1.json" \
  --run-analyse "$RUN_E" --prereg "$PREREG_E" > "$SCR/lancement-$RUN_E.txt" 2>&1; echo "code $?"
git add -- "runs/$RUN_E" "diag/$RUN_E" && git commit -q -m "Lecture par épisode de R1-R2 : sorties de la lecture décisive $RUN_E" \
  -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013QMaynBnMGnUDJtNQkv8KX" -- "runs/$RUN_E" "diag/$RUN_E"
git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_P"
```

**Doit afficher :** `code 0` à la fusion (sans conflit : la fusion anticipée de A1 l'a montré ; **jamais de rebasage**, et
un conflit arrête) ; `code = commit cité …` ; `0` ; `26a3ff72…` ; `2` ; les versions gelées ; `code 0` au lancement ;
`0` ; un push réussi. La fusion vient **après** E : elle ajoute des fichiers sous `src/controle_ia/analyse_principale_r1_r2/`
que la liste fermée de la principale ne cite pas.

## G. Fusion dans la branche de travail (dépôt principal) — ≈ 1 minute

```bash
cd $DEPOT && git merge --no-edit "$BR_P" ; echo "code $?" ; git push origin canal/conv-audit-n04
```

**Doit afficher** `code 0` et un push réussi (refus : `git pull --no-rebase`, puis repousser ; jamais de rebasage).

## H. Analyse secondaire, dans son arbre (créé en D3) — ≈ 8 à 10 minutes (lecture : 5 à 8 minutes selon son texte, l. 64)

```bash
cd "$ARBRE_S" && git status --porcelain --untracked-files=all | wc -l ; ls donnees | grep -v -c 20261019-230011-p3-reel
for R in "$REJEU" "$J3" "$J8"; do git checkout origin/calcul/r1-r2-reel-v1 -- "runs/$R" "diag/$R" || { echo "ARRÊT $R"; break; }
  for f in $(git ls-tree -r --name-only origin/calcul/r1-r2-reel-v1 "donnees/$R"); do test ! -e "$f" || { echo "EXISTE $f : ARRÊT"; break 2; }
    mkdir -p "$(dirname "$f")"; git show "origin/calcul/r1-r2-reel-v1:$f" > "$f"; done; done; echo "écriture faite"
git add -- runs/"$REJEU" diag/"$REJEU" runs/"$J3" diag/"$J3" runs/"$J8" diag/"$J8" && git commit -q -m "Réception R1 relancé et juges : runs/ et diag/ du fournisseur ($(git rev-parse --short=8 origin/calcul/r1-r2-reel-v1))" \
  -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013QMaynBnMGnUDJtNQkv8KX" -- runs/"$REJEU" diag/"$REJEU" runs/"$J3" diag/"$J3" runs/"$J8" diag/"$J8"
$PY -c "import json, hashlib, pathlib; f = json.load(open('$FICHE_S')); e = [f['R1'][k] for k in ('moyenne', 'maximum', 'manifeste')] + [f['R2']['fichier'], f['R2']['manifeste']]; print(all(hashlib.sha256(pathlib.Path(x['chemin']).read_bytes()).hexdigest() == x['sha256'] for x in e), len(e))"
PYTHONPATH=src $PY -m controle_ia.scellement verifier "$FICHE_S" | grep -c '^OK' ; git status --porcelain --untracked-files=all | wc -l
RUN_S=$(date -u +%Y%m%d-%H%M%S)-analyse-blanche-noire-v3 && echo "$RUN_S"
PYTHONPATH=src nice -n 10 $PY -m controle_ia.analyse_blanche_noire.lecture_v3 --fiche "$FICHE_S" --run-analyse "$RUN_S" --prereg "$PREREG_S" > "$SCR/lancement-$RUN_S.txt" 2>&1; echo "code $?"
git add -- "runs/$RUN_S" "diag/$RUN_S" && git commit -q -m "Analyse boîte blanche / boîte noire v3 : sorties de la lecture $RUN_S" \
  -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013QMaynBnMGnUDJtNQkv8KX" -- "runs/$RUN_S" "diag/$RUN_S"
git status --porcelain --untracked-files=all | wc -l ; git push origin "$BR_S" ; cd $DEPOT && git merge --no-edit "$BR_S" ; echo "code $?" ; git push origin canal/conv-audit-n04
```

**Doit afficher :** `0` ; `0` (arbre propre, aucune donnée hors P3) ; `écriture faite` ; `True 5` (les cinq fichiers que
cite la fiche secondaire ont, dans cet arbre, l'empreinte de la fiche ; P3 est celui suivi par git, vérifié en D3) ;
`1` ; `0` ; `code 0` au lancement ; `0` ; deux push et `code 0` à la fusion. Le résultat de la secondaire est rapporté
en entier à côté de la principale, quel qu'en soit le signe (règle symétrique, son texte l. 226) ; la réserve N2
(`reserve-N2-bras-moyenne-v1.md`, `c82b4d00…`) est citée par le lecteur R13 de la secondaire (I) et par le registre à la
réception : le script ne l'écrit pas dans la fiche (voir le rapport, point 4).

## I. Verdicts R13 — trois lecteurs neufs, en parallèle, ≈ 15 à 30 minutes chacun

Chaque lecteur n'a écrit ni le texte, ni le code, ni la fiche, ni la concordance de la lecture qu'il juge ; il reçoit
explicitement (R2) les fichiers, et rien d'autre ne lui est raconté du résultat. Il applique la table gelée du texte,
ligne par ligne, prononce la classe de chaque comparaison, et dit si l'issue mécanique du code la contredit. Son
rapport est scellé, commité, puis soumis à Lazar (information et nœuds ouverts ; aucune porte).

| lecteur | fichiers à donner (chemins dans l'arbre fusionné, avec empreintes) |
|---|---|
| principale | `$PREREG_P` (`8e267952…`) et sa table des critères (l. 140-167) ; `$FICHE_P` ; `runs/$RUN_P/manifeste.json` ; `diag/$RUN_P/analyse-principale-r1-r2-v1.{json,md}` ; `$SCR/lancement-$RUN_P.txt` ; l'addendum v2 scellé et le rapport de concordance finale (P1, P2) ; la décision N-A et la liste `$NON_INVERSIBLES` (E19 : la l. 146 est couverte pour ces seuls épisodes) ; `registres/decisions.md`, entrées de gel et de réception |
| par épisode | `$PREREG_E` (`26a3ff72…`), sa table (l. 105-134) ; `diag/$RUN_E/analyse-par-episode-v1.{json,md}` et manifeste ; le résultat de la principale ci-dessus (il doit rapporter ses classes à côté, sans les rejuger) |
| secondaire | `$PREREG_S` (`1f6a6da2…`), ses critères (l. 166-200) et ses écarts déclarés (l. 11-18, 218-226) ; la réserve N2 `brouillons/preuves-mentors-v1/analyse-blanche-noire-v3/reserve-N2-bras-moyenne-v1.md` ; `$FICHE_S` ; `diag/$RUN_S/…` et manifeste ; le résultat de la principale (règle symétrique : les deux lectures sont rapportées en entier, aucune citation de l'une sans l'autre) |

Consignes communes : symétrie (R4 : un résultat trop propre, positif ou négatif, déclenche le même audit) ; un nul se lit
« non détecté à cette puissance », avec son intervalle ; le lecteur de la principale vérifie que `tokenisation.episodes_non_resolus`
du résultat du fournisseur (cité par la fiche) égale `$NON_INVERSIBLES` ; aucune citation hors du dépôt sans Lazar.

## Durées attendues depuis le versement (hors attente des lecteurs R13)

| étape | durée |
|---|---|
| A constat | 1 min |
| B arbre de la principale (essais 20 à 40 s) | 2 min |
| C récupération, écriture, sceaux, commit | 1 à 3 min (réseau) ; sceaux 0,3 s |
| D fiches, contrôle de forme, scellements, commits, arbre de la secondaire, registre | 4 min (script : < 1 s mesuré, 12 essais en 0,7 s) |
| E lancement décisif de la principale | 1 à 5 min (calcul 9,8 s mesuré) |
| F fusion et lecture par épisode | 2 min (calcul 2,0 s mesuré) |
| G fusion dans la branche de travail | 1 min |
| H secondaire (réception, lecture 5 à 8 min, fusion) | 8 à 10 min |
| **total jusqu'aux trois sorties scellées** | **≈ 20 à 30 minutes** |
| I verdicts R13 (trois lecteurs en parallèle) | 15 à 30 min |
