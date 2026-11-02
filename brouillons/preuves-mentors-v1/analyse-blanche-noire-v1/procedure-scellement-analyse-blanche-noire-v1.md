# Procédure de scellement — analyse appariée boîte blanche / boîte noire (lecture secondaire de R1-R2) — v1

Pour la session principale. Elle exécute les étapes 0.a à 0.d du brouillon 5
(`preenregistrement-analyse-blanche-noire-v1-brouillon5.md`, sha256 `ca8b9dd4a6689f7a959e208163ef7948f745272d4b005029331a59ccbdd46e24`),
puis **s'arrête avant toute récupération de données**. Les étapes 0.e (données), 0.f (fiche) et 0.g (concordance, lancement)
attendent le scellement du préenregistrement de l'analyse principale de R1-R2 et sa vérification de concordance (brouillon 5,
étapes 0.e et 0.g ; R-1090).

**Règle générale.** Chaque bloc dit ce qu'il doit afficher pour continuer. Tout autre affichage, ou un code de sortie non
nul, **arrête la procédure** : ne rien lancer, ne rien corriger à la main dans l'arbre séparé, signaler à Lazar. Si le texte
scellé a déjà été committé, la reprise se fait sous une version nouvelle, contre-lue (R12). Ne calculer ni l'entropie ni
aucune graine. Aucun `git fetch` dans toute la procédure. Rien n'est lu sous `donnees/` (seule A1 hache les quatre fichiers
de P3, sans les ouvrir autrement).

## Variables (une seule session shell, du début à la fin)

```bash
DEPOT=/home/claude/controle-ia-travail
ARBRE=/home/claude/controle-ia-analyse-bn-v3        # hors du dépôt principal ; ne doit pas exister
BRANCHE=analyse-blanche-noire-v3                    # branche neuve ; ne doit pas exister (nom fixé par le brouillon 5, 0.b)
PY=$DEPOT/.venv/bin/python                          # interpréteur du dépôt principal (l'arbre séparé n'a pas de .venv)
D=brouillons/preuves-mentors-v1/analyse-blanche-noire-v1
B5=$D/preenregistrement-analyse-blanche-noire-v1-brouillon5.md
PREREG=prereg/analyse-blanche-noire-v3.md
SCR=/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/scellement-analyse-bn-v3   # sorties locales
mkdir -p "$SCR"
export PYTHONDONTWRITEBYTECODE=1
```

## A. Dépôt principal : vérifier, geler, committer (étape 0.a)

### A1. Vérifier les empreintes à geler

```bash
cd $DEPOT && sha256sum \
  $B5 \
  $D/preenregistrement-analyse-blanche-noire-v1-brouillon4.md \
  $D/contre-lecture-4-preenregistrement-analyse-v1.md \
  $D/rapport-redaction-v5.md \
  $D/appliquer-contre-lecture-4-v1.py \
  $D/appliquer-contre-lecture-4-v1-sortie.txt \
  $D/rejeu-frequence-regle-decision-v2-sur-v3-contre-lecture-3-v1.py \
  $D/rejeu-frequence-regle-decision-v2-sur-v3-contre-lecture-3-v1-sortie.txt \
  $D/differences-brouillon4-brouillon5-v1.diff \
  $D/preenregistrement-analyse-blanche-noire-v1-brouillon3.md \
  $D/contre-lecture-3-preenregistrement-analyse-v1.md \
  $D/contre-lecture-2-preenregistrement-analyse-v2.md \
  $D/contre-lecture-preenregistrement-analyse-v1.md \
  src/controle_ia/analyse_blanche_noire/constantes_v3.py \
  src/controle_ia/analyse_blanche_noire/entrees_v3.py \
  src/controle_ia/analyse_blanche_noire/evaluation_v3.py \
  src/controle_ia/analyse_blanche_noire/lecture_v3.py \
  src/controle_ia/analyse_blanche_noire/rendu_v3.py \
  tests/test_analyse_blanche_noire_v3.py \
  tests/test_analyse_blanche_noire_v1.py \
  donnees/20261019-230011-p3-reel/scores-p3.npz \
  donnees/20261019-230011-p3-reel/jetons-principales-p3.npz \
  donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl \
  donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz
```

**Doit afficher exactement**, dans cet ordre :

| fichier | sha256 |
|---|---|
| brouillon 5 (texte à sceller) | `ca8b9dd4a6689f7a959e208163ef7948f745272d4b005029331a59ccbdd46e24` |
| brouillon 4 (relu par la contre-lecture 4) | `ee11631689a96e8c89468b231b67c52dbd240aeac3343e052acaf27f3acbca98` |
| contre-lecture 4, rapport (commit `1a9f1b97`) | `dbf68e82abb8e82340a601e122812b2192040dc36bc0974693ee935b628bed36` |
| rapport de rédaction v5 | `cebbc0d59998f154c97620ac0d84cab751f97c5fd46ead7d0f57d263ba0f6146` |
| script d'application de la contre-lecture 4 | `205189131323b984667af2e60a8e48ad16be28d9eb71bc50e0c3e78451dfd3f2` |
| sa sortie | `fedeb4b43f2f379acf0378340483ba2c5dfb3cc4c9a258aee989c57f6ffe26ba` |
| rejeu de la contre-lecture 3, script (Z2) | `774ec9fb8d6ef657d2e1860ab9de7d340c6659c765e54611ae609c7f9b08448b` |
| rejeu de la contre-lecture 3, sortie (Z2) | `7b2d1a7be90c7945f8af1c14a44c907543ef8a8a96ada84d6a69c3172fe54f87` |
| différences du brouillon 4 au brouillon 5 | `6ff9b8a99bbcd4f4a2eaac2ae01004760b1640f15d91d8b058a0bb0892c42eae` |
| brouillon 3 | `addadee095efccf1fadbbc0306bca131bb5bd07f216fec80988a48d0ea9222f3` |
| contre-lecture 3, rapport | `8d99cd6ed4079448d3c4e135c6fe67dbda64bb53df89bfe513734a237b041656` |
| contre-lecture 2, rapport (v2) | `8697d7b2aa8bd6370b14f1628663d9eaff8bcfe33ca7245b13c47a94eb5104d4` |
| contre-lecture 1, rapport | `2af7ee33b14ee7bc9099f4198831b3baec9ac608e45d526641e91774d0ad2205` |
| `constantes_v3.py` | `6e7684acb7a7a520b926acc9315fd85db10d7f7b14d4cb8895986f577a3a33c4` |
| `entrees_v3.py` | `57bcb47ebd056b5d4a4164cd1611dc8405033d4bb37e9c1c4a68681d5febcd2b` |
| `evaluation_v3.py` | `539a0c7b8c9a8913380833d994875d6814cae1c9f7d3dfe6265b043c8e32ee2d` |
| `lecture_v3.py` | `dd5dffa4c6441981779aaa07816589666466bd4c8c7fc0d84a3b029fdec1d854` |
| `rendu_v3.py` | `363cd84f6dc2453e33a896e55192f0605340fdeadd80c44046d08cb0ac8d0371` |
| essais v3 | `cb86cf6d9bcb8d505277203467c192547b4ebecfa52b45e50d1c7141892b7ed7` |
| essais v1 | `6f97c988ee335c07831aba2bf4e80627cc6db66075dcb51f37baf4d34eb4cafa` |
| P3, `scores-p3.npz` | `968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf` |
| P3, `jetons-principales-p3.npz` | `4cd2ddb8311cfa7322d4137514c057c33039aba115aa14f08fb64141a2b0a36f` |
| P3, `textes-actions-p3.jsonl` (haché, jamais décodé) | `ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284` |
| P3, `sondes-figees-legeres.npz` | `701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60` |

Une seule différence arrête la procédure.

### A2. Garde du code cité, constantes, marqueur, essais (dépôt principal)

```bash
cd $DEPOT && PYTHONPATH=src $PY - <<'EOF'
from pathlib import Path
from controle_ia.analyse_blanche_noire import lecture_v3, constantes_v3
from controle_ia.prereg import problemes
p = Path("brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon5.md")
t = p.read_text(encoding="utf-8")
c = lecture_v3.exiger_code_cite(t)
print("fichiers cités :", len(c["fichiers"]), "; constantes :", c["constantes"] == constantes_v3.empreinte_constantes() == "273c0a68f526b92f24247e36845e026ec49ff91f1fbe2a4e396d3b49e7b19ad4")
print("marqueurs :", t.count("À REMPLIR"), "; problemes :", problemes(p))
print("versions :", lecture_v3.exiger_versions())
EOF
PYTHONPATH=src nice -n 10 $PY -m pytest -q -p no:cacheprovider --basetemp="$SCR/essais-depot" tests/test_analyse_blanche_noire_v3.py 2>&1 | tail -1
```

**Doit afficher :**
- `fichiers cités : 27 ; constantes : True` ;
- `marqueurs : 1 ; problemes : ['marqueur À REMPLIR restant hors des sections exigées']` ;
- `versions : {'python': '3.13.18', 'numpy': '2.4.6', 'scipy': '1.17.1'}` ;
- `13 passed` (durée environ 30 s).

### A3. Écrire l'entrée de gel (session principale)

Écrire dans `registres/decisions.md` une entrée de gel. Elle contient :
- les 24 empreintes de A1 ;
- l'empreinte des constantes (v3), `273c0a68…` ;
- la phrase : « brouillon 5 produit par voie B (remplacements H1 à H4 et B1 à B7 de la contre-lecture 4, B4, B5 et B7 adaptés pour un seul marqueur, Z1 à Z5), sans contre-lecture 5 » ;
- la référence à la présente procédure (chemin et empreinte).

Ne pas committer encore : le commit de A4 porte l'entrée et les fichiers ensemble.

### A4. Committer : ce commit est le commit cité (étape 0.a)

Committer en un seul commit, **chemins nommés seulement** (le commit ne doit rien emporter d'autre que ces fichiers, même si d'autres sessions ont des modifications en cours) :

```bash
cd $DEPOT && FICHIERS="registres/decisions.md $B5 $D/rapport-redaction-v5.md \
  $D/appliquer-contre-lecture-4-v1.py $D/appliquer-contre-lecture-4-v1-sortie.txt \
  $D/rejeu-frequence-regle-decision-v2-sur-v3-contre-lecture-3-v1.py \
  $D/rejeu-frequence-regle-decision-v2-sur-v3-contre-lecture-3-v1-sortie.txt \
  $D/differences-brouillon4-brouillon5-v1.diff $D/procedure-scellement-analyse-blanche-noire-v1.md"
git add $FICHIERS   # plus les compagnons .sha256 que la session principale crée (R6), nommés de même
git commit -q -m "Analyse boîte blanche / boîte noire : gel avant scellement (brouillon 5, voie B) — commit cité" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo" -- $FICHIERS
CITE=$(git rev-parse HEAD); echo "$CITE" | grep -Ex '[0-9a-f]{40}'
git show --name-only --format= HEAD
git status --porcelain -- src/controle_ia/analyse_blanche_noire tests/test_analyse_blanche_noire_v1.py tests/test_analyse_blanche_noire_v3.py $D
```

**Doit afficher :**
- le commit cité : 40 caractères hexadécimaux minuscules. Le noter : il est gardé dans `$CITE`, car d'autres sessions peuvent committer ensuite sur la même branche.
- les seuls fichiers de `$FICHIERS` (et leurs compagnons `.sha256`).
- rien pour `git status` : aucune modification non committée du paquet, des essais ni du dossier.

Ce commit est **le premier commit de l'étape 0.a**. Il n'est ni amendé ni refait : l'empreinte du texte scellé, donc les graines, en dépend.

Pousser ensuite la branche de travail :

```bash
git push origin canal/conv-audit-n04
```

Un push refusé par des commits d'autres sessions ne change pas `$CITE`. Fusionner par `git pull --no-rebase origin canal/conv-audit-n04` (refspec explicite), puis repousser. Jamais de rebasage : le commit cité doit rester dans l'historique.

## B. Arbre de travail séparé (étape 0.b)

```bash
cd $DEPOT && test ! -e "$ARBRE" && ! git show-ref --quiet "refs/heads/$BRANCHE" && echo LIBRE
git worktree add -b "$BRANCHE" "$ARBRE" "$CITE"
cd "$ARBRE" && git status --porcelain --untracked-files=all | wc -l
test "$(git rev-parse HEAD)" = "$CITE" && echo "HEAD = commit cité"
PYTHONPATH=src $PY -c "import controle_ia; print(controle_ia.__file__)"
PYTHONPATH=src $PY -c "from controle_ia.analyse_blanche_noire import lecture_v3; print(lecture_v3.exiger_versions())"
PYTHONPATH=src nice -n 10 $PY -m pytest -q -p no:cacheprovider --basetemp="$SCR/essais-arbre" tests/test_analyse_blanche_noire_v3.py 2>&1 | tail -1
git status --porcelain --untracked-files=all | wc -l
```

**Doit afficher :**
- `LIBRE` ;
- la création de l'arbre ;
- `0` ;
- `HEAD = commit cité` ;
- `/home/claude/controle-ia-analyse-bn-v3/src/controle_ia/__init__.py`. Le code importé doit venir de l'arbre séparé, sinon la garde « code importé hors de la racine » arrêtera le run ;
- `{'python': '3.13.18', 'numpy': '2.4.6', 'scipy': '1.17.1'}` ;
- `13 passed` ;
- `0` : les essais n'ont rien écrit dans l'arbre.

## C. Texte : copier, remplacer le seul marqueur, valider, sceller (étape 0.c)

```bash
cd "$ARBRE" && test ! -e "$PREREG" && CITE="$CITE" PYTHONPATH=src $PY - <<'EOF'
import os, re
from pathlib import Path
from controle_ia.prereg import problemes
from controle_ia.analyse_blanche_noire import lecture_v3
c = os.environ["CITE"]
assert re.fullmatch(r"[0-9a-f]{40}", c)
src = Path("brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/preenregistrement-analyse-blanche-noire-v1-brouillon5.md")
t = src.read_text(encoding="utf-8")
m = "`À REMPLIR au scellement : 40 caractères hexadécimaux du commit cité (étape 0 du Plan d'analyse)`"
assert t.count("À REMPLIR") == 1 and t.count(m) == 1
s = t.replace(m, "`" + c + "`")
dst = Path("prereg/analyse-blanche-noire-v3.md")
dst.write_text(s, encoding="utf-8")
print("problemes :", problemes(dst))
print("fichiers cités :", len(lecture_v3.exiger_code_cite(s)["fichiers"]))
print("commit cité présent :", ("- **Commit du code d'analyse** : `" + c + "`.") in s)
print("marqueurs restants :", s.count("À REMPLIR"))
EOF
diff "$B5" "$PREREG" | grep -c '^[<>]'
```

**Doit afficher :**
- `problemes : []` ;
- `fichiers cités : 27` ;
- `commit cité présent : True` ;
- `marqueurs restants : 0` ;
- `2` : une ligne retirée et une ajoutée, celle de « Commit du code d'analyse ».

Puis sceller (la garde de forme est rejouée par `sceller_prereg`) :

```bash
PYTHONPATH=src $PY -c "from controle_ia.prereg import sceller_prereg; print(sceller_prereg('$PREREG'))"
PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG'))"
```

**Doit afficher deux fois la même empreinte H.** La noter. Ne pas en dériver l'entropie : `lecture.entropie_de` ne sert qu'au lancement.

## D. Committer le texte seul, vérifier (étape 0.d)

```bash
cd "$ARBRE" && git add "$PREREG" "$PREREG.sha256"
git commit -q -m "Analyse boîte blanche / boîte noire : préenregistrement scellé (lecture secondaire de R1-R2)" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo"
git show --name-only --format= HEAD
test "$(git rev-parse HEAD~1)" = "$CITE" && echo "parent = commit cité"
git diff --quiet "$CITE" HEAD -- src tests && echo "code identique au commit cité"
git status --porcelain --untracked-files=all | wc -l
git push origin "$BRANCHE"
```

**Doit afficher :**
- exactement deux fichiers : `prereg/analyse-blanche-noire-v3.md` et `prereg/analyse-blanche-noire-v3.md.sha256` ;
- `parent = commit cité` ;
- `code identique au commit cité` ;
- `0` ;
- un push réussi de la branche `analyse-blanche-noire-v3`.

## E. Consigner au registre (session principale)

Dans le dépôt principal, une entrée de `registres/decisions.md` consigne :
- le chemin de l'arbre et la branche ;
- le commit cité `$CITE` et le commit du texte scellé ;
- l'empreinte H ;
- « `diff` de 2 lignes avec le brouillon 5 » ;
- « vérifications des étapes A à D conformes » ;
- « arrêt avant toute récupération de données ».

Committer cette entrée, puis pousser. Elle est hors de l'arbre séparé et ne touche ni `src/` ni `tests/`.

## F. ARRÊT : rien de plus avant le scellement de l'analyse principale

**Ici la procédure s'arrête.**

Rien de ce qui suit n'est fait tant que deux conditions ne sont pas remplies et consignées au registre :
1. le préenregistrement de l'analyse principale de R1-R2 (`brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/`, R-1090) est scellé ;
2. sa vérification de concordance est faite, celle qu'exige son étape 0, avant toute récupération.

Jusque-là, aucune action :
- aucun `git fetch` de `calcul/r1-r2-reel-v1` ni de `calcul/r4-dose-reel-v1` ;
- aucune lecture d'un fichier ou d'un manifeste de ces branches ;
- aucune fiche ;
- aucune commande `lecture_v3`.

Ensuite, et dans cet ordre (brouillon 5, étapes 0.e à 0.g ; à écrire en une procédure v2 au moment voulu) :
1. **Données (0.e).** Récupérer les branches de résultats par refspec explicite, et seulement celles-là. Placer les données sous `donnees/` de l'arbre séparé, ignoré par git. Copier aussi `donnees/20261019-230011-p3-reel/` du dépôt principal, dont les empreintes sont vérifiées en A1. Vérifier toutes les empreintes déclarées par le fournisseur, sans ouvrir aucun `.npz`. R4 n'entre que si le verdict de dose du fournisseur est scellé (J6).
2. **Fiche (0.f).** Écrire `prereg/fiche-reception-blanche-noire-v3.json` : clés exactes, pointeurs recopiés du code scellé du fournisseur, motifs fermés si R1 ou R2 manque, `R4.juge` nul. La sceller, puis la committer seule.
3. **Concordance (0.g).** La vérification est faite par un lecteur neuf, qui n'a écrit ni ce texte, ni celui de l'analyse principale, ni celui du fournisseur. Un écart de fond non déclaré à la section « Concordance » suspend le lancement : c'est un nœud de Lazar.
4. **Lancement (0.g)**, depuis la racine de l'arbre séparé, avec `PYTHONPATH=src` et `$PY` :
   `PYTHONPATH=src $PY -m controle_ia.analyse_blanche_noire.lecture_v3 --fiche prereg/fiche-reception-blanche-noire-v3.json --run-analyse <AAAAMMJJ-HHMMSS>-analyse-blanche-noire-v3 --prereg prereg/analyse-blanche-noire-v3.md`
   Puis committer `runs/` et `diag/` dans l'arbre, fusionner la branche par `git merge` dans la branche de travail, et pousser.
