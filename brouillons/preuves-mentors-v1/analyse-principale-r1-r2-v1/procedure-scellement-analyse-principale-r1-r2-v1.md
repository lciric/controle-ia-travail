# Procédure de scellement — analyse principale de R1-R2 — v1

Pour la session principale. Elle exécute l'étape 0 du brouillon 3
(`preenregistrement-analyse-principale-r1-r2-v1-brouillon3.md`, sha256 `951676a827d2fec7cae31cc5e60838cf320754f8e385dd15920eea646ee941ec`) :
gel au registre (0.0), commit cité (0.a), arbre séparé (0.b), scellement (0.c), vérifications (0.d). Ensuite viennent
la concordance (0.e), la récupération des sorties (0.f), la fiche (0.g) et le lancement (0.h), suivis de l'analyse
secondaire. Pour ces étapes, la section F décrit la suite.

**Règle générale.** Chaque bloc dit ce qu'il doit afficher pour continuer. Tout autre affichage, ou un code de sortie non
nul, **arrête la procédure** : ne rien lancer, ne rien corriger à la main dans l'arbre séparé, signaler à Lazar. Si le texte
scellé a déjà été committé, la reprise se fait sous une version nouvelle, contre-lue (R12).

D'autres règles valent pour toute la procédure :
- ne calculer ni l'entropie ni aucune graine ;
- **aucun `git fetch` de `calcul/r1-r2-reel-v1` dans ce dépôt**, arbres de travail compris, avant la fin de F1 : les arbres d'un même dépôt partagent objets et références ;
- aucun fichier de résultats de R1, R2 ou R4 ouvert avant F2 ;
- aucune écriture sous `donnees/20261019-230011-p3-reel/` : fichiers suivis par git.

Une course de réplication tourne sur la machine : `nice -n 10` pour les essais.

## Variables (une seule session shell, du début à la fin)

```bash
DEPOT=/home/claude/controle-ia-travail
ARBRE=/home/claude/controle-ia-analyse-principale-r1-r2-v1   # hors du dépôt principal ; ne doit pas exister
BRANCHE=analyse-principale-r1-r2-v1                          # branche neuve ; ne doit pas exister (brouillon 3, 0.b)
PY=$DEPOT/.venv/bin/python                                   # l'arbre séparé n'a pas de .venv
D=brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1
B3=$D/preenregistrement-analyse-principale-r1-r2-v1-brouillon3.md
PREREG=prereg/analyse-principale-r1-r2-v1.md
FICHE=prereg/fiche-reception-principale-r1-r2-v1.json
SCR=/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/scellement-analyse-principale-r1-r2-v1
mkdir -p "$SCR"
export PYTHONDONTWRITEBYTECODE=1
```

## A. Dépôt principal : constat, vérification, gel (0.0), commit cité (0.a)

### A0. État des références de résultats (AP-3), avant le gel

```bash
cd $DEPOT && git for-each-ref --format='%(refname) %(objectname)' 'refs/heads/calcul/r1-r2-reel-v1' 'refs/remotes/origin/calcul/r1-r2-reel-v1'; echo "fin de liste"
```

**Doit afficher** soit `fin de liste` seul (constat au 2 novembre 01:19 UTC : aucune référence de ce nom dans le dépôt), soit
la ou les références présentes, avec leur objet. Les noter telles quelles pour A3 et n'ouvrir aucun de leurs fichiers.

### A1. Vérifier les empreintes à geler

```bash
cd $DEPOT && sha256sum \
  $B3 $D/preenregistrement-analyse-principale-r1-r2-v1-brouillon2.md $D/preenregistrement-analyse-principale-r1-r2-v1-brouillon1.md \
  $D/contre-lecture-preenregistrement-analyse-principale-r1-r2-v1.md \
  $D/rapport-redaction-v1.md $D/rapport-redaction-v2.md $D/rapport-redaction-v3.md \
  $D/appliquer-contre-lecture-1-v1.py $D/appliquer-contre-lecture-1-v1-sortie.txt $D/differences-brouillon2-brouillon3-v1.diff \
  $D/frequence-nul-analyse-principale-v1.py $D/frequence-nul-analyse-principale-v1-sortie.txt \
  src/controle_ia/analyse_principale_r1_r2/__init__.py src/controle_ia/analyse_principale_r1_r2/constantes_v1.py \
  src/controle_ia/analyse_principale_r1_r2/calcul_v1.py src/controle_ia/analyse_principale_r1_r2/entrees_v1.py \
  src/controle_ia/analyse_principale_r1_r2/lecture_v1.py src/controle_ia/analyse_principale_r1_r2/constantes_v2.py \
  src/controle_ia/analyse_principale_r1_r2/lecture_v2.py \
  tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py \
  donnees/20261019-230011-p3-reel/scores-p3.npz donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
git rev-parse HEAD:donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
```

**Doit afficher exactement**, dans cet ordre :

| fichier | sha256 |
|---|---|
| brouillon 3 (texte à sceller) | `951676a827d2fec7cae31cc5e60838cf320754f8e385dd15920eea646ee941ec` |
| brouillon 2 (relu par la contre-lecture 1) | `fb1373931d0865715b6f3962c66f1384f62f266b500026acb4af87a658f8f41f` |
| brouillon 1 | `15bf78247d9ae15353f60b7292df13fa98e3e8b0cfaba1aa412853e173ce2331` |
| contre-lecture 1, rapport (commit `346ce542`) | `eff5d4cacad00e7da4dd0d28df024516d976fa2b6e084bfbdede96352ab04606` |
| rapport de rédaction v1 | `84eec1042f8c8261f3d8af01417a26d5f97bca3d467dd67108698fe1610c515d` |
| rapport de rédaction v2 | `b500e372759037696d379f04673553aaeef4317631b35cc677b175659cfe3f4a` |
| rapport de rédaction v3 | `50add71b1f9c1dcfb1f615a77c4e8da85e1c112f39398a12ed0568db58602ec5` |
| script d'application de la contre-lecture 1 | `5a443a8350d19464e7f0b7f1d6f6454d50434f40f6986e5751d6835bf98c8b8b` |
| sa sortie | `015c787df3dbceea3c6c294fb45fc9ee4739f4efe8521f45bb795e12c415e8ff` |
| différences du brouillon 2 au brouillon 3 | `f9dfb08cee2e1f92aae6b956b46b740837e96c7996c50a10b20151d9652dda25` |
| script de fréquence sous le nul | `ca8f3ebd506d09c49081e66ab8b128b2f4f23cdea1f68d279a0da4fb2b76dbcf` |
| sa sortie | `9b63f8c645739fdaa9bf926ee9283ce880cfe55d107273026d50ee74a66fcc92` |
| `__init__.py` | `3d9d2db34507280c083a3044ef229613e4f7dc9f8f0b71d106e7d1a5fa19ae3c` |
| `constantes_v1.py` | `66b52be663a8b826e9ad3a8ef5518f39c45edaff57251cc5bd5f2e3ab00db0ce` |
| `calcul_v1.py` | `f5845571d0c22eedbb4341c50229ae606ed4b8576fcd5f9d544d3d1c0a74283e` |
| `entrees_v1.py` | `244a04daf892341439da3c0ef5c4ed4c1cf07ec6d0d22da717dbd2a6640c0dc3` |
| `lecture_v1.py` | `4a34955ce8760fa26f62c0a368d5980a5b8f8782fe108bb9c286a1afa1b4b7dd` |
| `constantes_v2.py` | `ae8170f7238e95833d63fdd71869472ba5f19d03985b0f3eb937b9791c896e2f` |
| `lecture_v2.py` | `3493e92d4507bd7b4f99062829aba973771ac18c06fda55da97bf91959debff8` |
| essais v1 | `5d510c05e15df689e0644076756f710172a815d26565a7407b97c66626b1e6d3` |
| essais v2 | `2a99001597c6f25c61a1cc7eb417615410ee55743748e3967315560fce142cf7` |
| P3, `scores-p3.npz` | `968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf` |
| P3, `textes-actions-p3.jsonl` (haché, jamais décodé) | `ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284` |

La dernière commande (`git rev-parse`) doit afficher l'objet git `bad1403f1454f46de23adbbee59da8586170c7ec`.

Une seule différence arrête la procédure. La garde de A2 vérifie aussi les neuf modules réutilisés de la liste fermée.

### A2. Garde du code cité, constantes, marqueur, essais (dépôt principal)

```bash
cd $DEPOT && PYTHONPATH=src $PY - <<'EOF'
from pathlib import Path
from controle_ia.analyse_principale_r1_r2 import lecture_v1, lecture_v2, constantes_v2
from controle_ia.prereg import problemes
p = Path("brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/preenregistrement-analyse-principale-r1-r2-v1-brouillon3.md")
t = p.read_text(encoding="utf-8")
c = lecture_v2.exiger_code_cite(t)
print("fichiers cités :", len(c["fichiers"]), "; constantes :",
      c["constantes"] == constantes_v2.empreinte_constantes() == "d223c2071dec5ccfba4a23547f32f7355946bb8848e9824ad62ca945e4c2cf2d")
print("marqueurs :", t.count("À REMPLIR"), "; problemes :", problemes(p))
print("versions :", lecture_v1.exiger_versions())
EOF
PYTHONPATH=src:tests nice -n 10 $PY -m pytest -q -p no:cacheprovider --basetemp="$SCR/essais-depot" \
  tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py 2>&1 | tail -1
```

**Doit afficher :**
- `fichiers cités : 18 ; constantes : True` ;
- `marqueurs : 1 ; problemes : ['marqueur À REMPLIR restant hors des sections exigées']` ;
- `versions : {'python': '3.13.18', 'numpy': '2.4.6', 'scipy': '1.17.1'}` ;
- `24 passed` (durée de 20 à 40 s).

### A3. Gel au registre et poussée (étape 0.0) — la session principale

Écrire dans `registres/decisions.md` une entrée de gel. Elle contient :
- les 23 empreintes de A1, plus l'objet git `bad1403f…` ;
- l'empreinte des constantes du code v2, `d223c207…` ;
- l'état des références de A0 ;
- la phrase : « brouillon 3 produit par voie B (remplacements AP-1 à AP-10 de la contre-lecture 1, appliqués mot pour mot par script ; adaptations de la session : AP-1 heures, AP-5 option (b), AP-7 et AP-8 version scellée de l'analyse secondaire), sans contre-lecture 2 ; entrée « Contre-lecture 1 » remplie dans le brouillon ; un seul marqueur, le commit cité » ;
- la référence à la présente procédure (chemin et empreinte).

Committer **cette entrée seule**, chemin nommé, puis pousser :

```bash
cd $DEPOT && git commit -q -m "Analyse principale de R1-R2 : gel du brouillon 3 avant l'étape 0 (parade de Q9)" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo" -- registres/decisions.md
git push origin canal/conv-audit-n04
```

**Doit afficher** un push réussi. Un push refusé se règle par `git pull --no-rebase origin canal/conv-audit-n04`, puis on repousse. Jamais de rebasage.

### A4. Commit cité (étape 0.a), juste après la poussée de A3

Le code, les essais, les brouillons 1 et 2, le rapport de la contre-lecture et le script de fréquence sont déjà committés par les instantanés de la session. A4 committe ce qui reste, **chemins nommés seulement** :

```bash
cd $DEPOT && FICHIERS="$B3 $D/rapport-redaction-v3.md $D/appliquer-contre-lecture-1-v1.py \
  $D/appliquer-contre-lecture-1-v1-sortie.txt $D/differences-brouillon2-brouillon3-v1.diff \
  $D/procedure-scellement-analyse-principale-r1-r2-v1.md"
git add $FICHIERS   # plus les compagnons .sha256 que la session crée (R6), nommés de même
git commit -q -m "Analyse principale de R1-R2 : brouillon 3 et pièces — commit cité" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo" -- $FICHIERS
CITE=$(git rev-parse HEAD); echo "$CITE" | grep -Ex '[0-9a-f]{40}'
git show --name-only --format= HEAD
git status --porcelain -- src/controle_ia/analyse_principale_r1_r2 tests/test_analyse_principale_r1_r2_v1.py \
  tests/test_analyse_principale_r1_r2_v2.py $D
git push origin canal/conv-audit-n04
```

**Doit afficher :**
- `$CITE` : 40 caractères hexadécimaux minuscules, gardés dans `$CITE` car d'autres sessions peuvent committer ensuite ;
- les seuls fichiers de `$FICHIERS` et leurs compagnons ; un commit vide arrête la procédure ;
- rien pour `git status` ;
- un push réussi (en cas de refus : `git pull --no-rebase`, puis repousser ; `$CITE` ne change pas).

Ce commit n'est ni amendé ni refait : l'empreinte du texte scellé, donc les graines, en dépend (Q9).

## B. Arbre de travail séparé (étape 0.b) et textes de P3 (vérification, AP-2)

```bash
cd $DEPOT && test ! -e "$ARBRE" && ! git show-ref --quiet "refs/heads/$BRANCHE" && echo LIBRE
git worktree add -b "$BRANCHE" "$ARBRE" "$CITE"
cd "$ARBRE" && git status --porcelain --untracked-files=all | wc -l
test "$(git rev-parse HEAD)" = "$CITE" && echo "HEAD = commit cité"
PYTHONPATH=src $PY -c "import controle_ia; print(controle_ia.__file__)"
PYTHONPATH=src $PY -c "from controle_ia.analyse_principale_r1_r2 import lecture_v1; print(lecture_v1.exiger_versions())"
git rev-parse HEAD:donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
sha256sum donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl donnees/20261019-230011-p3-reel/scores-p3.npz
PYTHONPATH=src $PY -m controle_ia.scellement verifier donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl \
  donnees/20261019-230011-p3-reel/scores-p3.npz diag/20261019-230011-p3-reel/resume.json \
  diag/20261019-230011-p3-reel/episodes-p3.json diag/20261019-230011-p3-reel/sondes-figees.json
PYTHONPATH=src:tests nice -n 10 $PY -m pytest -q -p no:cacheprovider --basetemp="$SCR/essais-arbre" \
  tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_principale_r1_r2_v2.py 2>&1 | tail -1
git status --porcelain --untracked-files=all | wc -l
```

**Doit afficher :**
- `LIBRE`, puis la création de l'arbre ;
- `0` ;
- `HEAD = commit cité` ;
- `/home/claude/controle-ia-analyse-principale-r1-r2-v1/src/controle_ia/__init__.py`. Si le code importé ne vient pas de l'arbre séparé, la garde « code importé hors de la racine » arrête le run ;
- `{'python': '3.13.18', 'numpy': '2.4.6', 'scipy': '1.17.1'}` ;
- `bad1403f1454f46de23adbbee59da8586170c7ec` ;
- `ba05fa13…` et `968414fc…` ;
- cinq vérifications de sceau conformes. Aucune restauration, aucune redirection sur ces fichiers ; s'il en manque un, arrêt ;
- `24 passed` ;
- `0` : les essais n'ont rien écrit dans l'arbre.

## C. Texte : copier, remplacer le seul marqueur, valider, sceller (étape 0.c)

```bash
cd "$ARBRE" && test ! -e "$PREREG" && CITE="$CITE" PYTHONPATH=src $PY - <<'EOF'
import os, re
from pathlib import Path
from controle_ia.prereg import problemes
from controle_ia.analyse_principale_r1_r2 import lecture_v2
c = os.environ["CITE"]
assert re.fullmatch(r"[0-9a-f]{40}", c)
src = Path("brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/preenregistrement-analyse-principale-r1-r2-v1-brouillon3.md")
t = src.read_text(encoding="utf-8")
m = "`À REMPLIR au scellement : 40 caractères hexadécimaux du commit cité (étape 0.a du Plan d'analyse)`"
assert t.count("À REMPLIR") == 1 and t.count(m) == 1
s = t.replace(m, "`" + c + "`")
dst = Path("prereg/analyse-principale-r1-r2-v1.md")
dst.write_text(s, encoding="utf-8")
print("problemes :", problemes(dst))
print("fichiers cités :", len(lecture_v2.exiger_code_cite(s)["fichiers"]))
print("commit cité présent :", ("- **Commit du code d'analyse** : `" + c + "`.") in s)
print("marqueurs restants :", s.count("À REMPLIR"))
EOF
diff "$B3" "$PREREG" | grep -c '^[<>]'
```

**Doit afficher :**
- `problemes : []` ;
- `fichiers cités : 18` ;
- `commit cité présent : True` ;
- `marqueurs restants : 0` ;
- `2` : une ligne retirée, une ajoutée, celle du commit cité.

Puis sceller :

```bash
PYTHONPATH=src $PY -c "from controle_ia.prereg import sceller_prereg; print(sceller_prereg('$PREREG'))"
PYTHONPATH=src $PY -c "from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle('$PREREG'))"
```

**Doit afficher deux fois la même empreinte H.** La noter. L'entropie (`constantes_v2.entropie_de(H)`) n'est calculée que par le code, au lancement.

## D. Committer le texte seul, vérifier (étape 0.d)

```bash
cd "$ARBRE" && git add "$PREREG" "$PREREG.sha256"
git commit -q -m "Analyse principale de R1-R2 : préenregistrement scellé" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo"
git show --name-only --format= HEAD
test "$(git rev-parse HEAD~1)" = "$CITE" && echo "parent = commit cité"
git diff --quiet "$CITE" HEAD -- src tests && echo "code identique au commit cité"
git status --porcelain --untracked-files=all | wc -l
git push origin "$BRANCHE"
```

**Doit afficher :**
- exactement deux fichiers : `prereg/analyse-principale-r1-r2-v1.md` et son compagnon `.sha256` ;
- `parent = commit cité` ;
- `code identique au commit cité` ;
- `0` ;
- un push réussi de `analyse-principale-r1-r2-v1`.

## E. Consigner au registre (session principale)

Dans le dépôt principal, une entrée de `registres/decisions.md` consigne :
- le chemin de l'arbre et la branche ;
- `$CITE`, le commit du texte scellé et l'empreinte H ;
- « `diff` de 2 lignes avec le brouillon 3 » ;
- « vérifications A à D conformes » ;
- « arrêt avant toute récupération de données, en attente de la concordance ».

Committer cette entrée (chemin nommé) et pousser.

## F. La suite après scellement

Il y a deux préconditions, consignées au registre :
- le texte de l'analyse secondaire est scellé : `prereg/analyse-blanche-noire-v3.md`, `1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9`, commit `7a238666`, R-1096 ;
- celui de l'analyse principale l'est aussi (E).

### F1. Concordance (étape 0.e) : lecteur neuf, avant toute récupération

Un sous-agent neuf, qui n'a écrit aucun des trois textes ni leurs contre-lectures, reçoit explicitement les fichiers suivants (R2) :
- les deux textes scellés : `prereg/analyse-principale-r1-r2-v1.md` (H, branche `analyse-principale-r1-r2-v1`) et `prereg/analyse-blanche-noire-v3.md` (`1f6a6da2…`, branche `analyse-blanche-noire-v3`) ;
- le texte du fournisseur : `git show 567260c0:prereg/R1-R2-rejeu-p3-v1.md` (`80c85a00…`) ;
- le brouillon 3 et l'entrée de gel du registre (A3) ;
- le rapport de la contre-lecture 1 ;
- le code des deux analyses, aux commits cités ;
- le code du fournisseur au commit `29bd8e2e`.

Il vérifie :
1. la concordance de chacun des deux textes avec celui du fournisseur, à l'aide de leur section « Concordance ». Pour l'analyse principale : la table A, lignes 1 à 32, et les décisions Q1 à Q13. Pour la secondaire : ses écarts déclarés ;
2. la garde « activation non finie » (AP-5) au regard de la règle `moyenne` du fournisseur ;
3. que le texte scellé ne diffère du brouillon 3 inscrit au registre que par la ligne du commit cité ;
4. que `git reflog` de la branche ne montre aucun « commit (amend) » ni « reset » sur `$CITE`.

Son rapport est versé, avec son compagnon (R6), dans `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/`, puis committé et consigné. **Un écart de fond non déclaré, ou la garde AP-5 jugée contraire à la règle `moyenne`, est un nœud de Lazar** : arrêt, rien n'est récupéré.

### F2. Récupération des sorties (étape 0.f, AP-3), dans l'arbre séparé de l'analyse principale

Seulement après F1 conforme et consigné :

```bash
cd "$ARBRE" && git fetch origin refs/heads/calcul/r1-r2-reel-v1 && git rev-parse FETCH_HEAD
git ls-tree -d --name-only FETCH_HEAD runs/ diag/ donnees/
```

Noter le commit de `FETCH_HEAD` et les noms des runs : rejeu, juge 3B, juge 8B ; noms seulement. Puis, pour chaque run `R` :

```bash
git checkout FETCH_HEAD -- "runs/$R" "diag/$R"
for f in $(git ls-tree -r --name-only FETCH_HEAD "donnees/$R"); do test ! -e "$f" || { echo "EXISTE $f : ARRÊT"; break; }; \
  mkdir -p "$(dirname "$f")"; git show "FETCH_HEAD:$f" > "$f"; done
PYTHONPATH=src $PY -m controle_ia.scellement verifier $(git ls-tree -r --name-only FETCH_HEAD "donnees/$R" "diag/$R" "runs/$R" | grep -v '\.sha256$')
```

Puis committer les seuls `runs/<runs>` et `diag/<runs>` du fournisseur, chemins nommés. Le message de commit cite `FETCH_HEAD`. Vérifier ensuite que `git status --porcelain --untracked-files=all` est vide.

Règles de cette étape :
- jamais de `git merge` de la branche de résultats ;
- aucun `.npz` ouvert ;
- un sceau faux arrête la procédure ;
- R4 n'est pas récupéré ici.

### F3. Fiche (étape 0.g)

Écrire `$FICHE` avec les clés exactes du brouillon 3, point 0.g :
- `format` = `fiche-reception-principale-r1-r2-v1` ;
- `redaction` : qui, quand, commit de `FETCH_HEAD`, ce qui a été ouvert. Ce sont les noms listés par `git ls-tree`, les compagnons `.sha256` et, s'il existe, `arret.json`, cité par chemin et empreinte ;
- `R1` = `{moyenne, maximum, complement, resultat}`, chacun `{chemin, sha256}`. Les chemins sont `donnees/<rejeu>/activations-p3-rejeu-v1.npz`, `…-maximum.npz`, `…-complement-hors-cout.npz` et `diag/<rejeu>/rejeu-activations.json`. Les empreintes sont recopiées des compagnons par un script, jamais à la main ;
- `motif_R1` : `null`, sauf si le rejeu s'est arrêté (`diag/<rejeu>/arret.json`). Dans ce cas `R1` est nul et le motif vaut `rejeu_non_conforme` si son `verdict_fidelite` est « non conforme », `rejeu_en_echec` sinon ;
- `R2` = `{juge3b: {fichier, resultat}, juge8b: {fichier, resultat} ou null, motif_juge8b}` (`scores-juge3b-p3-v1.npz`, `diag/<juge>/juge-actions.json`). Si les juges ne sont pas livrés, `R2` est nul avec `motif_R2` ∈ {`sorties_non_livrees`, `garde_N029_du_kit`}, preuve dans `redaction`.

Contrôle de forme, sans aucune donnée, puis scellement et commit de la fiche seule :

```bash
PYTHONPATH=src $PY -c "from pathlib import Path; from controle_ia.analyse_principale_r1_r2.entrees_v1 import lire_fiche; print(lire_fiche(Path('.'), '$FICHE', scellee=False)[1])"
PYTHONPATH=src $PY -m controle_ia.scellement sceller "$FICHE"
git add "$FICHE" "$FICHE.sha256" && git commit -q -m "Analyse principale de R1-R2 : fiche de réception scellée" \
  -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrvL31uf4bd95RstDyo"
git status --porcelain --untracked-files=all | wc -l
```

**Doit afficher** l'empreinte de la fiche, puis `0`.

### F4. Lancement de l'analyse principale (étape 0.h)

```bash
cd "$ARBRE" && RUN=$(date -u +%Y%m%d-%H%M%S)-analyse-principale-r1-r2-v1 && echo "$RUN"
PYTHONPATH=src nice -n 10 $PY -m controle_ia.analyse_principale_r1_r2.lecture_v2 --fiche "$FICHE" \
  --run-analyse "$RUN" --prereg "$PREREG" > "$SCR/lancement-$RUN.txt" 2>&1; echo "code $?"
```

**Doit afficher** `code 0`. La durée estimée va de 1 à 5 minutes, pour au plus ≈ 1,5 Go.

Un « ARRÊT : … » se consigne avec son motif. Si le manifeste existe déjà, aucun second passage n'est permis sans l'accord de Lazar, et cet accord ne peut porter que sur la cause technique.

Ensuite :
1. committer `runs/$RUN` et `diag/$RUN`, chemins nommés ;
2. fusionner la branche dans la branche de travail par `git merge`, jamais de rebasage ;
3. pousser ;
4. consigner H, `$RUN`, les empreintes des sorties et l'issue mécanique, recopiée telle quelle.

Le verdict R13 est prononcé plus tard par un sous-agent neuf. Il n'a écrit ni le texte ni le code et applique la table gelée.

### F5. Puis l'analyse secondaire

Suivre la procédure de l'analyse secondaire, étape F : `brouillons/preuves-mentors-v1/analyse-blanche-noire-v1/procedure-scellement-analyse-blanche-noire-v1.md`, `65904959…`, dans son propre arbre `/home/claude/controle-ia-analyse-bn-v3`. Elle se déroule ainsi :
- données (0.e) ;
- fiche v3 (0.f) ;
- concordance (0.g) : le rapport de F1 en tient lieu s'il couvre son texte et que son lecteur n'a écrit aucun des deux textes ;
- lancement de `lecture_v3`.

Trois précisions pour cette étape F :
1. **Récupération** : la même que F2, par la même refspec. `runs/` et `diag/` du fournisseur sont committés dans son arbre, faute de quoi sa garde « arbre de travail non propre » arrête le lancement. `donnees/` passe hors index.
2. **Données de P3** : son point F1 dit de « copier `donnees/20261019-230011-p3-reel/` du dépôt principal ». Ces fichiers sont suivis par git et déjà présents dans son arbre. Il faut les **vérifier par empreinte**, comme ici en B, et ne pas les copier par-dessus.
3. **Règle symétrique** : les deux lectures sont rapportées en entier, quel qu'en soit le signe ; aucune citation externe ne cite l'une sans l'autre ; toute citation hors du dépôt passe par Lazar.
