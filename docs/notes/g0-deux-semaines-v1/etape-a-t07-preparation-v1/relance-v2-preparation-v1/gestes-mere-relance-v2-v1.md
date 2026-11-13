# Relance de l'étape A de T0.7 : suite unique des gestes de la mère, de la correction des pièces à l'envoi de la fille — v1

- **Auteur** : préparateur des pièces de relance (modèle A), sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`,
  sur le message de la mère qui suit R-2614 ; 2026-11-13, vers 23:40 UTC (`date -u`). Il n'a pas ouvert le texte scellé de T0.7.
- **Objet** : MA-2 de la contre-lecture des pièces de relance (`relance-v2-preparation-v1/contre-lecture-relance-v2-v1.md`,
  `703195e515480fcff2f4dc60cd4ca5bffedc4e930e24f6d4711eaa57386fc5fd`, R-2614) : **une seule suite**, numérotée, avec les
  commandes exactes. Elle remplace toute autre énumération des gestes de la mère (note de la consigne v2, brouillon 1 ;
  addendum, brouillon 2, § 5) ; l'addendum (brouillon 3), l'ordre v2 (brouillon 2) et la consigne v2 (brouillon 2) y renvoient.
- **Pièces visées** (empreintes) :

| pièce | chemin | sha256 |
|---|---|---|
| addendum, brouillon 3 (marqueur `<<NOUVELLE_LIGNE_CODE_T07>>`) | `brouillons/T0.7-addendum-cache-motifs-v1-brouillon3.md` | `9c85cde7220a312f1e328ece4fbec29ad64ce426a79ca5d87218e6002fc32702` |
| ordre v2, brouillon 2 (quatre marqueurs) | `docs/procedures/ordre-execution-etape-a-t07-v2-brouillon2.md` | `244ff506fdb846990905fdadafd73fdf576be09c0c69a8a40fee7b69049138b7` |
| consigne de la fille v2, brouillon 2 (six cases) | `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/consigne-fille-etape-a-v2-brouillon2.md` | `6511ffb2e4495e7f82c1c2a9a64341769a8e48f298d82d90057ce3d16767f656` |
| outil du remplacement, **v2** (trace avant le remplacement) | `scripts/remplacer_ligne_code_t07_v2.py` | `0e7c3c0cbf4b052b1a2852ef49fb2135337dc110c0af7dbf4f066509207204bb` |
| essais de l'outil v2 (36 cas, joués où ils sont) | `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/relance-v2-preparation-v1/essais-outil/test_remplacer_ligne_code_t07_v2.py` | `74b11b9523204003930a51f34e5c51f08adc491a998b37e4805ab250d6271a1c` |
| essais de l'outil v1 (28 cas, à jouer copiés sous `tests/`) | `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/relance-v2-preparation-v1/essais-outil/test_remplacer_ligne_code_t07_v1.py` | `0a1210da9060eee2715eebe556261ea96193ce2b002d071cb192484ff5ebfb7f` |
| fichier de la ligne `CODE-T07` (versé, R-2606) | `registres/code-t07/CODE-T07-v3.json` | `d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218` |

**Règles qui valent pour toute la suite** : (R-a) **aucun fichier de `src/` ni de `tests/`, de quelque tâche que ce soit,
n'entre dans `main` entre C7 (`c2fab6cc`) et S7** (MA-3 ; sinon `git diff --quiet C7 S7 -- src tests` refuse au § 4.1 de l'ordre
et à l'étape 2 du script de l'instance) : chaque commit de la suite se fait **par chemins nommés**, jamais `git add -A` ; (R-b)
aucune ligne neuve au registre des scellements (la garde de T0.7 refuse toute clé inconnue, règle (4)) : la seule écriture y est
le remplacement de l'étape 1 ; (R-c) un refus ou un écart à une étape **arrête la suite** : nœud de la mère, rien rejoué (l'outil
refuse d'ailleurs une seconde exécution) ; (R-d) toutes les commandes se jouent depuis la racine de `main`, dans **un seul shell**
(les variables `T`, `A`, `N`, `S7` passent d'une étape à l'autre) ; heures par `date -u`.

## 0. Préalables

```bash
cd /home/user/controle-ia-travail && export PYTHONPATH=src && PY=.venv/bin/python && date -u
git fetch -q origin "refs/heads/main:refs/remotes/origin/main" && [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] && echo "main à jour"
git diff --quiet c2fab6cc HEAD -- src tests && echo "src et tests de la tête égaux à C7"
[ "$(sha256sum < registres/scellements-v1.md | cut -d' ' -f1)" = 9061a5dab171b111223b9596b6a042718a51bce250152c54eeee4f5d29d96265 ] && [ -z "$(git status --porcelain -- registres/scellements-v1.md)" ] && echo "registre des scellements intact"
[ ! -e registres/scellements-v1.md.ouvertures.md ] && echo "aucune ouverture journalisée"
for f in brouillons/T0.7-addendum-cache-motifs-v1-brouillon3.md docs/procedures/ordre-execution-etape-a-t07-v2-brouillon2.md docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/consigne-fille-etape-a-v2-brouillon2.md scripts/remplacer_ligne_code_t07_v2.py registres/code-t07/CODE-T07-v3.json; do (cd "$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") && echo "OK $f"; done
```

Attendu : les cinq messages et cinq `OK`. Les pièces de ce lot (brouillons, scripts de couples, outil v2, essais sous
`relance-v2-preparation-v1/essais-outil/`, cette suite) sont versées avant l'étape 1, par chemins nommés (aucun sous `src/` ni
`tests/`). Une relecture courte de ces corrections avant l'étape 1 est au choix de la mère.

## 1. Remplacement de la ligne `CODE-T07` (outil v2 : à blanc, puis réel)

```bash
T=docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/relance-v2-preparation-v1/trace-remplacement-ligne-code-t07-v1.md
A='| CODE-T07 | 2026-11-11T05:40:34Z | registres/code-t07/CODE-T07-v2.json | d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c |'
N=$($PY scripts/remplacer_ligne_code_t07_v2.py construire --racine . --chemin registres/code-t07/CODE-T07-v3.json) && printf '%s\n' "$N"
$PY scripts/remplacer_ligne_code_t07_v2.py remplacer --racine . --registre registres/scellements-v1.md --ancienne "$A" --nouvelle "$N" --trace "$T" --a-blanc
$PY scripts/remplacer_ligne_code_t07_v2.py remplacer --racine . --registre registres/scellements-v1.md --ancienne "$A" --nouvelle "$N" --trace "$T"
```

Attendu : la ligne neuve `| CODE-T07 | <heure> | registres/code-t07/CODE-T07-v3.json | d3eaebfe…c218 |` ; « À BLANC, conforme :
ligne n° 7 ; registre 9061a5da… → <empreinte après> ; rien d'écrit » ; puis « REMPLACÉE : ligne n° 7 ; registre 9061a5da… →
<même empreinte après> ; heure … ; trace … ». Le registre est donné par son chemin **relatif** (la trace l'écrit tel quel). La
troisième commande ne se joue qu'après la deuxième en code 0. Un refus (code 2) : rien n'est écrit ; arrêt (R-c).

## 2. Recopie de la nouvelle ligne dans l'addendum (brouillon 3 → addendum rempli, rien d'autre)

```bash
[ "$(grep -c '^| CODE-T07 |' registres/scellements-v1.md)" = 1 ] && [ "$(grep '^| CODE-T07 |' registres/scellements-v1.md)" = "$N" ] && grep -qxF -- "$N" "$T" && echo "registre, trace et ligne construite égaux"
$PY -I - "$N" <<'EOF'
import sys
n = sys.argv[1]
src, dst = "brouillons/T0.7-addendum-cache-motifs-v1-brouillon3.md", "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md"
t = open(src, encoding="utf-8").read()
assert t.count("<<NOUVELLE_LIGNE_CODE_T07>>") == 1 and "<<" not in t.replace("<<NOUVELLE_LIGNE_CODE_T07>>", "")
open(dst, "x", encoding="utf-8").write(t.replace("<<NOUVELLE_LIGNE_CODE_T07>>", n))
print("addendum rempli :", dst)
EOF
[ "$(diff brouillons/T0.7-addendum-cache-motifs-v1-brouillon3.md prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md | grep -c '^[<>]')" = 2 ] && echo "une seule ligne diffère"
```

Nom proposé : `prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md` (ajout sous `prereg/` : P12 (b) tenu) ; un autre nom neuf
hors de `src/` et `tests/` convient, reporté alors aux étapes 3, 4 et 6.

## 3. Scellement de l'addendum

```bash
$PY -m controle_ia.scellement sceller prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md
```

Aucune ligne de registre pour lui (R-b).

## 4. Commit S7 : rien sous `src/` ni `tests/`

```bash
git add -- registres/scellements-v1.md "$T" "$T.sha256" prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md.sha256
[ -z "$(git diff --cached --name-only -- src tests)" ] && git diff --cached --name-status
git commit -q -m "T0.7, relance de l'étape A : ligne CODE-T07 remplacée une seule fois (R-2604), addendum scellé (S7)" && S7=$(git rev-parse HEAD) && echo "S7=$S7" && git push -q origin main
```

La ligne du registre des décisions qui le consigne peut entrer dans ce même commit (chemin nommé). Attendu : la liste des
fichiers du commit, aucun sous `src/` ni `tests/` ; `S7` imprimé.

## 5. Vérifications

```bash
git merge-base --is-ancestor c2fab6cc "$S7" && git diff --quiet c2fab6cc "$S7" -- src tests && echo "C7 ancêtre de S7 ; src et tests égaux"
[ "$(git diff --name-status c2fab6cc "$S7" -- docs/notes/g0-deux-semaines-v1 'brouillons/T0.7-*' prereg | grep -vc '^A')" = 0 ] && echo "P12 (b) : ajouts seuls"
[ "$(grep -c '^| CODE-T07 |' registres/scellements-v1.md)" = 1 ] && [ "$(grep '^| CODE-T07 |' registres/scellements-v1.md)" = "$N" ] && echo "une seule ligne CODE-T07, la nouvelle"
$PY -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md
(cd "$(dirname "$T")" && sha256sum -c "$(basename "$T").sha256"); (cd prereg && sha256sum -c T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md.sha256)
git ls-remote origin refs/heads/donnees/t07-etape-a-v1 | wc -l
```

Attendu : les trois messages ; « CODE-T07 conforme : commit c2fab6cc7267b76228a75dc3e2e08bc7aa038961, 26 fichiers, … » (code 0) ;
deux `OK` ; `0`. Tout écart : arrêt (R-c) ; le registre n'est pas remis en arrière sans écrit de la mère.

## 6. Remplissage et scellement de l'ordre v2 (après S7 : il le nomme)

```bash
FILLE='<identifiant de la session fille>'          # la fille de la v1 (session_01QPDgKf6Rn3eTeuYMDCBiKA) ou une neuve
HA=$(cut -d' ' -f1 prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md.sha256)
$PY -I - "$S7" "$N" "$HA" "$FILLE" <<'EOF'
import re, sys
s7, n, ha, fille = sys.argv[1:5]
assert re.fullmatch(r"[0-9a-f]{40}", s7) and re.fullmatch(r"[0-9a-f]{64}", ha) and re.fullmatch(r"session_\w+", fille)
src, dst = "docs/procedures/ordre-execution-etape-a-t07-v2-brouillon2.md", "docs/procedures/ordre-execution-etape-a-t07-v2.md"
t = open(src, encoding="utf-8").read()
v = {"<<COMMIT_SCELLEMENT_T07_V2>>": s7, "<<LIGNE_CODE_T07_V2>>": n, "<<ID_SESSION_FILLE_V2>>": fille,
     "<<ADDENDUM_T07_SCELLE_V2>>": "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md`, `" + ha}
for k, x in v.items():
    assert t.count(k) == 1, k
    t = t.replace(k, x)
assert not re.findall(r"<<[A-Z0-9_]+>>", t)
open(dst, "x", encoding="utf-8").write(t)
print("ordre rempli :", dst)
EOF
$PY -m controle_ia.scellement sceller docs/procedures/ordre-execution-etape-a-t07-v2.md
```

## 7. Engagement, écrit daté, consigne remplie, commit de remise

1. **Engagement** sous GO-2026-11-10-06 dans `registres/depenses.md` : relance de l'étape A, ordre v2 rempli (chemin, empreinte),
   dépense antérieure sous les deux lignes 0,43 USD, pire cas du devis 16,4 USD, `20 − 0,43 ≥ 16,4`.
2. **Écrit daté** dans `registres/decisions.md` (recopié au journal par la fille) : C7 `c2fab6cc…` ; S7 ; `SRC7` `799ef383…` et
   P13 (iii) (« arbre `src/` de `SRC7`, dernier commit contre-lu, égal à celui de C7, `02749689…` ») ; `ATT` « 500 passed, 2 skipped,
   4 xfailed », commit de la mesure `c2fab6cc`, arbres `src/` `02749689…` et `tests/` `42d9f073…`, et le résultat « ajouts
   seuls » de l'étape 5 (P12) ; la ligne `CODE-T07` (`$N`) et la trace ; `ANT0` = 0,43 ; l'ordre rempli (chemin, empreinte).
3. **Consigne remplie** (six cases du texte envoyé ; `ECRITS` = la désignation des lignes à recopier, par exemple « lignes
   R-2564 et R-26xx de `registres/decisions.md`, mot pour mot ») ; `REMISE` se fixe **au commit de remise** : remplir, sceller,
   committer d'abord l'engagement, l'écrit et l'ordre rempli, puis prendre `REMISE=$(git rev-parse HEAD)` et remplir la consigne :

```bash
HO=$(cut -d' ' -f1 docs/procedures/ordre-execution-etape-a-t07-v2.md.sha256); ECRITS='<lignes à recopier>'
git add -- registres/depenses.md registres/decisions.md docs/procedures/ordre-execution-etape-a-t07-v2.md docs/procedures/ordre-execution-etape-a-t07-v2.md.sha256
[ -z "$(git diff --cached --name-only -- src tests)" ] && git commit -q -m "T0.7, relance de l'étape A : ordre v2 rempli, engagement, écrit daté" && REMISE=$(git rev-parse HEAD) && git push -q origin main
$PY -I - "$HO" "$REMISE" "$N" "$ECRITS" <<'EOF'
import re, sys
ho, remise, n, ecrits = sys.argv[1:5]
d = "docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/"
src, dst = d + "consigne-fille-etape-a-v2-brouillon2.md", d + "consigne-fille-etape-a-v2-remplie.md"
tete, envoye = open(src, encoding="utf-8").read().split("\n---\n", 1)
v = {"⟦commit de main": remise, "⟦chemin de l'ordre": "`docs/procedures/ordre-execution-etape-a-t07-v2.md`",
     "⟦empreinte de l'ordre": "`" + ho + "`", "⟦écrits datés": ecrits, "⟦ligne CODE-T07": n}
vus = []
def f(m):
    for k, x in v.items():
        if m.group(0).startswith(k):
            vus.append(k)
            return x
    raise SystemExit("case inconnue : " + m.group(0))
envoye = re.sub(r"⟦[^⟧]*⟧", f, envoye)
assert len(vus) == 6 and set(vus) == set(v) and "⟦" not in envoye
open(dst, "x", encoding="utf-8").write(tete + "\n---\n" + envoye)
print("consigne remplie :", dst)
EOF
$PY -m controle_ia.scellement sceller docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/consigne-fille-etape-a-v2-remplie.md
```

   La consigne remplie et son compagnon se versent ensuite par chemins nommés (rien sous `src/` ni `tests/`) ; poussée.

## 8. Session fille et envoi

La fille de la v1 (`session_01QPDgKf6Rn3eTeuYMDCBiKA`, en attente depuis R-2592) ou une neuve **ouverte dans le dépôt** (crochet de
garde, R-2545) ; liste des intouchables du § 3 de la consigne relue contre l'inventaire du jour ; envoi du texte qui suit la
ligne de séparation de la consigne remplie.

## 9. Après la fin de l'étape A seulement (instance détruite, compte rendu reçu)

Si les essais de l'outil doivent aller sous `tests/` : copier `relance-v2-preparation-v1/essais-outil/test_remplacer_ligne_code_t07_v2.py`
(et la v1) sous `tests/`, mêmes octets, avec compagnons ; les jouer ; committer. Pas avant : un S7 refait doit rester possible
(R-a). La réserve des fichiers de `e3-ter-v1/` (ordre v2, S-18) reste au compte rendu de l'étape A et au verdict de porte ; un
script v5 de l'instance est à faire avant tout autre emploi du script (étape B ou seconde relance).
