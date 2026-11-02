# Procédure de scellement et de lancement — essaim hors échantillon — v1

Pour la session principale. Elle exécute l'étape 0 du brouillon 4
(`preenregistrement-essaim-hors-echantillon-v1-brouillon4.md`, sha256 `6afe72569312917869ef073e2564298622328b08368739c76d077d8e79bff3d4`),
puis la commande décisive.

**Règle générale.** Chaque bloc dit ce qu'il doit afficher pour continuer. Tout autre affichage, ou un code de sortie
non nul, **arrête la procédure**. Dans ce cas :
- ne rien lancer ;
- ne rien corriger à la main dans l'arbre séparé ;
- signaler à Lazar.

Si le texte scellé a déjà été committé, la reprise se fait sous une version nouvelle, contre-lue (R12, protocole après
un arrêt). Aucune graine décisive n'est utilisée avant l'étape F : ne calculer ni l'entropie, ni un bloc, ni une cellule.

## Variables (une seule session shell, du début à la fin)

```bash
DEPOT=/home/claude/controle-ia-travail
ARBRE=/home/claude/controle-ia-essaim-ho-v1        # hors du dépôt principal ; ne doit pas exister
BRANCHE=essaim-ho-scellement-v1                    # branche neuve ; ne doit pas exister
PY=$DEPOT/.venv/bin/python                         # interpréteur du dépôt principal (l'arbre séparé n'a pas de .venv)
D=brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1
GRILLE=prereg/essaim-hors-echantillon-grille-v1.json
PREREG=prereg/essaim-hors-echantillon-v1.md
SCR=/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/scellement-essaim-ho   # sorties locales
mkdir -p "$SCR"
```

## A. Dépôt principal : committer les fichiers, puis geler les empreintes (étape 0.a ; parade M8, C3.3, C3.9)

### A1. Committer les fichiers neufs

Sur `canal/conv-audit-n04`, committer :
- `$D/preenregistrement-essaim-hors-echantillon-v1-brouillon4.md` ;
- `$D/rapport-redaction-v4.md` ;
- `$D/appliquer-contre-lecture-3-v1.py` et `$D/appliquer-contre-lecture-3-v1-sortie.txt` ;
- `tests/test_simulation_essaim_hors_echantillon_v4.py` ;
- la présente procédure ;
- les compagnons `.sha256` que la session principale crée (R6).

Il ne doit rester aucune modification non committée dans `src/`, `tests/` ni `$D/` :

```bash
cd $DEPOT && git status --porcelain -- src tests $D
```
**Doit afficher : rien.**

### A2. Vérifier les empreintes à geler

```bash
cd $DEPOT && sha256sum \
  $D/preenregistrement-essaim-hors-echantillon-v1-brouillon4.md \
  $D/preenregistrement-essaim-hors-echantillon-v1-brouillon3.md \
  $D/preenregistrement-essaim-hors-echantillon-v1-brouillon2.md \
  $D/preenregistrement-essaim-hors-echantillon-v1-brouillon1.md \
  $D/contre-lecture-preenregistrement-essaim-hors-echantillon-v1.md \
  $D/rapport-redaction-v2.md \
  $D/contre-lecture-2-preenregistrement-essaim-hors-echantillon-v1.md \
  $D/rapport-redaction-v3.md \
  $D/contre-lecture-3-preenregistrement-essaim-hors-echantillon-v1.md \
  $D/rapport-redaction-v4.md \
  $D/grille-essaim-hors-echantillon-v1-brouillon2.json \
  donnees/20261019-230011-p3-reel/scores-p3.npz \
  $D/appliquer-contre-lecture-3-v1.py \
  $D/appliquer-contre-lecture-3-v1-sortie.txt
```

**Doit afficher exactement**, dans cet ordre :

| Fichier | sha256 |
|---|---|
| brouillon 4 (texte à sceller) | `6afe72569312917869ef073e2564298622328b08368739c76d077d8e79bff3d4` |
| brouillon 3 (relu par la contre-lecture 3) | `d1d5740e202dd972d017b236969acf499341b8187d6cbfcf63d571b36451e343` |
| brouillon 2 | `922733605a856bdc6f0f3f452363d1063e4c2de31666e7333edc956be6aa16e0` |
| brouillon 1 | `d1ec8c605672bbfc3b284a288ae9745236062230ac31c41834cd01f278f545c8` |
| contre-lecture 1, rapport | `dcec7d1a82abe21d13e72aa7714edcb30982222b3b8911301a28f485cfae76dc` |
| contre-lecture 1, traitement (`rapport-redaction-v2.md`) | `663945ed3c6430dd4d326cc71f4cb8dbd3c934a6edde06d1b7377b805989a455` |
| contre-lecture 2, rapport | `6d46750a8211e9f0a72a832eeba608ffeef261bbe56a7b37c2d2ec44b12379cd` |
| contre-lecture 2, traitement (`rapport-redaction-v3.md`) | `ebb0dbd727ecaeb477bb772e0666cbe37ec6dff9f0e2e11acd1d4190d02bf5d1` |
| contre-lecture 3, rapport | `b454118f7ed75aeb7887ec4e090a6845699414f8147efbd9755516cad3194cb4` |
| contre-lecture 3, traitement (`rapport-redaction-v4.md`) | `b86055dc0b46b27b983961c6007f1cb653d60eb9fd73c90132a8564e404e766f` |
| grille | `dbe1caf113ac12cf9e056cfd2f6916eb2d13341735cb58b0260acc64d86c8007` |
| données P3 | `968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf` |
| script des remplacements | `c0409e6ae088221f70dea36440e55e44c203159f9f0ce1ca8e5d1f89cc022120` |
| sa sortie | `07ec95b8ec70bebf381614139dab8c3296a1f5f933a2c3a383acf14037afd946` |

Une seule différence arrête la procédure.

### A3. Relever la référence des commits inaccessibles (C3.9)

```bash
cd $DEPOT && git fsck --unreachable --no-reflogs > "$SCR/fsck-reference.txt"; echo "code $?"; wc -l < "$SCR/fsck-reference.txt"; sha256sum "$SCR/fsck-reference.txt"
```
**Doit afficher** `code 0`, puis un nombre de lignes et une empreinte. Le contre-lecteur 3 a relevé 428 lignes ; le nombre peut avoir changé depuis. Le relevé peut prendre jusqu'à deux minutes.

Verser ce fichier au dépôt, sous `registres/` ou dans `$D/` selon l'usage de la session, avec son empreinte.

### A4. Écrire et pousser l'entrée de gel (session principale)

Écrire l'entrée dans `registres/decisions.md`, puis committer et pousser sur `canal/conv-audit-n04`. L'entrée contient :
- les 14 empreintes de A2 ;
- l'empreinte du relevé de A3 ;
- la phrase : « brouillon 4 produit par voie B (remplacements de la section 8 de la contre-lecture 3, plus E1 et E2), sans contre-lecture 4 ».

```bash
cd $DEPOT && git push origin canal/conv-audit-n04 && A=$(git rev-parse HEAD) && echo "$A"
```
**Doit afficher** un push réussi, puis le commit **A** (noter sa valeur ; elle est gardée dans `$A`, car d'autres sessions peuvent committer ensuite sur la même branche).

Ce commit A contient le code v3, les essais v1 à v4, le brouillon 4 et les rapports. Seul le commit cité reste alors à fixer.

## B. Arbre de travail séparé (étape 0.a, suite)

```bash
cd $DEPOT && test ! -e "$ARBRE" && ! git show-ref --quiet "refs/heads/$BRANCHE" && echo LIBRE
git worktree add -b "$BRANCHE" "$ARBRE" "$A"
cd "$ARBRE" && git status --porcelain --untracked-files=all | wc -l
PYTHONPATH=src $PY -c "import controle_ia; print(controle_ia.__file__)"
```

**Doit afficher :**
- `LIBRE` ;
- la création de l'arbre ;
- `0` ;
- `/home/claude/controle-ia-essaim-ho-v1/src/controle_ia/__init__.py`.

Le code importé doit venir de l'arbre séparé, sinon la garde du lanceur arrêtera le run.

## C. Grille : copier, sceller, committer seule (étapes 0.b et 0.c)

```bash
cd "$ARBRE" && test ! -e "$GRILLE" && cp "$D/grille-essaim-hors-echantillon-v1-brouillon2.json" "$GRILLE"
PYTHONPATH=src $PY -m controle_ia.scellement sceller "$GRILLE"
```
**Doit afficher :**
`dbe1caf113ac12cf9e056cfd2f6916eb2d13341735cb58b0260acc64d86c8007  prereg/essaim-hors-echantillon-grille-v1.json`

```bash
git add "$GRILLE" "$GRILLE.sha256"
git commit -q -m "Essaim hors échantillon : grille scellée (commit cité)" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo"
git show --name-only --format= HEAD
COMMIT=$(git rev-parse HEAD); echo "$COMMIT" | grep -Ex '[0-9a-f]{40}'
test "$(git rev-parse HEAD~1)" = "$A" && echo "parent = A"
```

**Doit afficher :**
- exactement deux fichiers : `prereg/essaim-hors-echantillon-grille-v1.json` et `prereg/essaim-hors-echantillon-grille-v1.json.sha256` ;
- le commit cité, 40 caractères hexadécimaux minuscules ;
- `parent = A`.

Ce commit est créé **une seule fois** : ne jamais le refaire ni l'amender.

## D. Texte : copier, remplacer le seul marqueur, valider, sceller (étape 0.d)

```bash
cd "$ARBRE" && test ! -e "$PREREG" && COMMIT="$COMMIT" PYTHONPATH=src $PY - <<'EOF'
import os, re
from pathlib import Path
from controle_ia.prereg import problemes
from controle_ia.simulation_t03.run_t03 import COMMIT_CITE
c = os.environ["COMMIT"]
assert re.fullmatch(r"[0-9a-f]{40}", c)
src = Path("brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/preenregistrement-essaim-hors-echantillon-v1-brouillon4.md")
t = src.read_text(encoding="utf-8")
assert re.findall(r"<<[A-Z0-9_]+>>", t) == ["<<COMMIT_CITE>>"] and t.count("`<<COMMIT_CITE>>`") == 1
s = t.replace("<<COMMIT_CITE>>", c)
dst = Path("prereg/essaim-hors-echantillon-v1.md")
dst.write_text(s, encoding="utf-8")
print("problemes :", problemes(dst))
print("commit cité retrouvé :", COMMIT_CITE.search(s).group(1) == c)
print("marqueurs restants :", "<<" in s)
EOF
diff "$D/preenregistrement-essaim-hors-echantillon-v1-brouillon4.md" "$PREREG" | grep -c '^[<>]'
```

**Doit afficher :**
- `problemes : []` ;
- `commit cité retrouvé : True` ;
- `marqueurs restants : False` ;
- `2` : une ligne retirée, une ajoutée, celle de « Commit du code d'analyse ».

Puis sceller :

```bash
PYTHONPATH=src $PY -m controle_ia.scellement sceller "$PREREG"
PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG'))"
```
**Doit afficher deux fois la même empreinte H** (la noter). Sans commande Python ni calcul : ne pas calculer l'entropie qui en découle.

## E. Committer le texte seul, vérifier, pousser (étape 0.e)

```bash
cd "$ARBRE" && git add "$PREREG" "$PREREG.sha256"
git commit -q -m "Essaim hors échantillon : préenregistrement scellé" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo"
git show --name-only --format= HEAD
git diff --quiet "$COMMIT" HEAD -- src tests "$GRILLE"; echo "diff code $?"
git status --porcelain --untracked-files=all | wc -l
sha256sum donnees/20261019-230011-p3-reel/scores-p3.npz
PYTHONPATH=src $PY -m controle_ia.scellement verifier "$PREREG" "$GRILLE"
ls runs/*/manifeste.json 2>/dev/null | xargs -r grep -l '"essaim-hors-echantillon-v1"' | wc -l
```

**Doit afficher :**
- exactement deux fichiers : `prereg/essaim-hors-echantillon-v1.md` et son `.sha256` ;
- `diff code 0` ;
- `0` (arbre propre) ;
- `968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf` pour les données ;
- deux lignes `OK …` ;
- `0` : aucun run existant de cette simulation.

Puis consigner et pousser, **avant le lancement** (parade, point 3) :
- inscrire `COMMIT` (commit cité) et H (empreinte du préenregistrement scellé) dans `registres/decisions.md`, sur `canal/conv-audit-n04` ;
- pousser ;
- pousser aussi la branche de l'arbre séparé :

```bash
cd "$ARBRE" && git push origin "$BRANCHE"
```

## F. Run décisif, sous `timeout` (étape 0.f)

Seule commande permise : le lanceur **v3**. Jamais le v1 ni le v2 sur ce texte.

```bash
cd "$ARBRE" && PYTHONPATH=src timeout --signal=TERM 6h nice -n 10 $PY -m controle_ia.simulation_essaim.run_essaim_hors_echantillon_v3 \
  --prereg prereg/essaim-hors-echantillon-v1.md --grille prereg/essaim-hors-echantillon-grille-v1.json \
  > "$SCR/sortie-run.json" 2> "$SCR/erreurs-run.txt"; echo "code $?"; cat "$SCR/sortie-run.json"
```

**Durée attendue** : environ 4 à 8 minutes, plus jusqu'à deux minutes pour le `git fsck` du journal. Lancer en arrière-plan si la session coupe au-delà de 2 minutes.

**Doit afficher** `code 0`, puis un JSON avec :
- `run_id` (de la forme `AAAAMMJJ-HHMMSS-essaim-ho`) ;
- `manifeste`, `lecture` ;
- `journal_s` (equivalence, S, Q, P, descriptif-maxima) ;
- `entropie`.

**Arrêts :**
- `code 1` avec `ARRÊT : …` dans `erreurs-run.txt` : une garde de la liste d'arrêt s'est déclenchée. Ne pas ouvrir les blocs `diag/<run_id>/bloc-*.json` éventuellement écrits ; diagnostic sur le seul message ; protocole après un arrêt (version nouvelle contre-lue).
- `code 124` : `timeout` de 6 h, qui correspond à la limite de durée de la liste d'arrêt. Même conduite.
- Tout autre code, ou une trace Python sans `ARRÊT` : même conduite, et signaler.

## G. Vérifier, verser les sorties, fusionner

```bash
cd "$ARBRE" && RUN=$($PY -c "import json; print(json.load(open('$SCR/sortie-run.json'))['run_id'])")
ls diag/$RUN runs/$RUN
PYTHONPATH=src $PY -m controle_ia.scellement verifier-arbre .
git status --porcelain --untracked-files=all | grep -v -E "^\?\? (runs|diag)/$RUN/" | wc -l
```

**Doit afficher :**
- dans `diag/$RUN`, chacun avec son `.sha256` : `journal-git.json`, `puissances-exactes-S.json`, `equivalence.json`, `bloc-S.json`, `bloc-Q.json`, `bloc-P.json`, `descriptif-maxima.json`, `lecture.json`, `lecture.md` ;
- dans `runs/$RUN` : `manifeste.json` et son `.sha256` ;
- `arbre intact` ;
- `0` : rien d'autre n'a bougé.

```bash
git add "runs/$RUN" "diag/$RUN"
git commit -q -m "Essaim hors échantillon : run décisif $RUN (sorties scellées, non lues)" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo"
git push origin "$BRANCHE"
cd $DEPOT && git status --porcelain -- src tests prereg | wc -l
git merge --no-ff "$BRANCHE" -m "Fusion : essaim hors échantillon, préenregistrement scellé et run $RUN" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo"
git merge-base --is-ancestor "$COMMIT" HEAD && echo "commit cité dans l'historique"
git push origin canal/conv-audit-n04
```

**Doit afficher :**
- `0` avant la fusion ;
- une fusion sans conflit ;
- `commit cité dans l'historique` ;
- un push réussi.

Jamais de rebasage ni de recopie de commits : le commit cité doit rester dans l'historique.

**Ensuite :**
- verdict par un lecteur neuf (R13), sur `diag/$RUN/lecture.md` et les comptes bruts, scores séparés d'abord ;
- passation : déclarer qu'aucun pré-run n'a eu lieu (parade, point 4) et noter l'observation O1 de la contre-lecture 3 (`lecture_version` v3 fait foi, la clé `version` v2 est héritée).
- En cas de réplication (une prédiction compte une cellule statistique contraire) :
  - committer d'abord les sorties (déjà fait en G) ;
  - dans le même arbre, lancer la même commande en ajoutant `--replication-de $RUN` ;
  - une seule réplication est permise.
