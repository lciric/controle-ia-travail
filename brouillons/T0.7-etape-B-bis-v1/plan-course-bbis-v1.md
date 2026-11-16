# Plan de la course de l'étape B bis de T0.7 — gestes restants, dans l'ordre, et ordre avec l'étape B (v1)

- **Auteur** : préparateur neuf, sous-agent de la session mère ; il n'a écrit aucun fichier de l'étape B bis (ni le texte, ni
  l'addendum, ni le code, ni une contre-lecture). Il ne sera lecteur d'aucun verdict. **Pour la liste « qui a lu quoi »** : il a lu,
  de l'étape B, la commande de la phase C v3 (§ 0 et § 15) et le § 3 de son calendrier, rien d'autre (aucune sortie, aucune consigne
  de lecteur).
- **Date (UTC)** : 2026-11-16, de 11:48 à 12:18 (`date -u`). Commits lus : `main` `377a2a0c9b1ec2704374a50537d5c59ae39b0ac7`
  (12:06:47Z ; contrôles refaits sur lui, et sur `d4b81652` avant) ; branche du code `prep/t07bbis-code-v1`, tête
  `bd1472adf07eeb5a4d95169f57add1bb49290915` (arbre de travail `.claude/worktrees/agent-a4f221610ce6d5a67`, propre, rien changé).
- **Statut** : plan, non committé ; rien inscrit, rien loué, rien dépensé ; la mère décide et inscrit. Il peut servir de base à
  « l'ordre d'exécution contre-lu » du calendrier scellé (ligne du mardi 17) s'il est contre-lu par un lecteur neuf.
- **Interdits tenus** : aucune machine, aucun appel au loueur ; rien lu ni écrit sous `diag/`, `donnees/`, `docs/verdicts/` ; aucune
  entrée de 7a ou 7b ; aucune valeur de clé, ni `env` ni `printenv` ; aucun `pytest` ; aucune variable `GIT_*` ; aucun fichier
  existant modifié ; dépôt distant interrogé en lecture seule, par `git ls-remote` seulement ; fusions vérifiées par `git
  merge-tree` dans sa forme ancienne, qui n'écrit rien.
- **Pièce jointe, préparée** : `brouillons/T0.7-etape-B-bis-v1/code/empreintes-fiche-code-bbis-v3-ce470564-v1.txt` (103 lignes
  `empreinte  chemin`, lisibles par `sha256sum -c` depuis la racine ; scellée, compagnon `.sha256`).

## Sources lues (chemin et empreinte)

| pièce | empreinte |
|---|---|
| `prereg/T0.7-etape-B-bis-v1.md` (texte scellé, lu en entier) | `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` |
| `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` (addendum scellé, lu en entier) | `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` |
| `registres/t07-etape-b-bis-v1.md` (registre propre : `SCELLEMENT-BBIS`, `ABSENCE-B-BBIS`) | `082b7e70e86d5ac9b20f581c6a182c1746c17c83809ceac93abc0a204788600b` |
| `registres/t07-etape-b-bis-v1-addenda-v1.md` (registre voisin : `ADDENDUM-ECART-1-BBIS`) | `93f0d3ddfe3c20fa34d35dc943c6361116a3b91bb4b2ed4f13ef14d89b736054` |
| `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v3.txt` (103 chemins) | `b8fb095bf44dc855868e1b48cef6005222af6888b00a9df2f60fccc36ded7d5d` |
| `scripts/lancer_bbis_v3.sh` | `dc26ea01a06bfb9eac3fc4f9f1b9b3bb86490d61d9e8f5deb54bcb180b17ee68` |
| `scripts/amorce_bbis_v3.sh` | `18e2f2052efdca0d9d447738c3c4f1099302f7134b9518b59eea78ba563695dd` |
| `src/controle_ia/t07bbis/registre_bbis_v1.py` | `c3b1848b3466a88a250aee2b58477c91ff5d660592c1a6cc695f8910005dcf1b` |
| `src/controle_ia/t07bbis/marche_v3.py` | `7009b34d46c33ed8fa4a5045d4ad93816c0948fd6dc165cb8f74e493b98f03f5` |
| `src/controle_ia/t07bbis/lecture_v2.py` | `154795f4ecfa3273a7a5cec91c6975cd34e558d14647bb8a1cb1ef4968972aca` |
| `brouillons/T0.7-etape-B-bis-v1/code/rapport-developpeur-corrections-v2.md` (gestes 0 à 5) | `d8a2e40bdb3563c10096c9fd33163e4ffcf69d3394e7abe9c1e4fc34e40c9714` |
| quatrième passe : `traces/bbis-t07-repetition-v4/repetition-carte.json` au commit `75bc5b325c1668821f8626c5f415ea3e24c7feb6` (données synthétiques) | `cbcaeb5242583d99d11c2c02a8dbfa559a0a9551887f816f7a47e643e63a35a4` |
| consignes de la mère du pilote v13 (K4) `docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/consignes-mere-pilote-v13-v1.md` | `8bc7d81ad415f48cba01d9be42ad5e24707717c13cecace9e563837187a300f1` |
| procédure du pilote v14, au commit `2d35cafa` de `lot/compte-organisme-v1` (point 2.5 (ii), sections 9 et 11) | `2035562740efe1e87db9ffa2f0494705bb5117c56069309ece2279d351bde18a` |
| `docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v3.md` (§ 0 et § 15 seulement) | `9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e` |
| `docs/procedures/lecture-7b-etape-b-compte-3-v1/calendrier-et-remise-phase-c-v3-v1.md` (§ 3 seulement) | `1dd534af0f75ac7a0ba454dc11a87ecf51631f5888a7d1f57d58dc714c2bad21` |

Registres vivants, cités par ligne au commit `377a2a0c` : `registres/go.md` (GO-2026-11-14-09, GO-2026-11-15-03, -04, -07,
GO-2026-11-16-01 à -05) ; `registres/decisions.md` (R-2740, R-2746, R-2751, R-2760, R-2790, R-2802, R-2829, R-2844, R-2869,
R-2883, R-2933, R-2950, R-2952, R-2953, R-2957, R-2959, R-2968, R-2970) ; `registres/scellements-v1.md` (noms de clés seulement).

## Verdict

1. **Aucun obstacle de fond à une course aujourd'hui ou cette nuit.** Le code de la quatrième passe (`ce470564`) est celui que la
   fiche doit citer (les 103 fichiers y sont égaux à la tête de la branche et au disque) ; la branche de sortie est absente à
   distance ; la base « mots et coût » ne se calcule pas sur la machine et n'attend plus mercredi.
2. **Correction d'ordre, obligatoire** : le code de B bis **ne va pas dans `main`** avant l'exécution de l'étape B (R-2760 : il
   ferait refuser `CODE-T07`). La course part donc de la **branche du code** `prep/t07bbis-code-v1`, qui reçoit `main` **une seule
   fois, maintenant**, à un commit sans rien de l'étape B, puis porte la fiche, `CODE-BBIS`, `GO-BBIS` et toutes les lignes de B bis
   jusqu'au verdict scellé de B bis ; `main` ne la reçoit qu'après l'étape B et après `VERDICT-BBIS`. Les deux règles (R-2760 et
   § 15 (5) de la phase C) tiennent alors **sans ordre imposé entre la course de B bis et l'étape B** (§ 10).
3. **Chemin le plus court** : environ 1 h 15 de gestes sans dépense, puis la création dès la preuve d'absence du pilote 60918148
   (K4), puis 3,5 à 4,5 heures d'instance. Au plus tôt : création vers **13:40Z** si l'épreuve de niveau part maintenant et si le
   pilote est fini ; sinon à la preuve d'absence du pilote plus 10 minutes ; `SCORES-BBIS` le soir même.

**Divergences relevées** : (i) la consigne donnait l'autonomie jusqu'au 2026-11-16T18:12:31Z (GO-2026-11-16-03) ; elle est remplacée
par **GO-2026-11-16-04** (R-2970) : jusqu'au **2026-11-17T11:47:55Z**, prolongeable par la mère jusqu'au 2026-11-18T11:47:55Z si un
travail en cours l'exige ; (ii) la procédure du développeur (rapport des corrections v2, geste 0 ; R-2790) fusionne la branche
**dans `main`** et fait citer par la fiche ce commit de fusion : impossible avant l'exécution de l'étape B (R-2760), et contraire au
§ 15 (5) de la phase C si `main` porte déjà la recopie de l'étape B (§ 10, b) ; ce plan la remplace.

## 1. La ligne `CODE-BBIS`

### 1.1 Ce qu'elle porte

- **Forme** (registre propre, quatre colonnes exactement ; texte, « Lignes de registre », l. 222) :
  `| CODE-BBIS | AAAA-MM-JJTHH:MM:SSZ | registres/t07-etape-b-bis/code-bbis-v1.json | <empreinte de la fiche> |`.
- **La fiche** (JSON scellé, `registre_bbis_v1.ecrire_fiche_code`, l. 124 à 160) : `texte`, `commit` (40 caractères), `fichiers`
  (les 103 chemins → empreintes, **lues sur le disque** de la racine), `entropie` (128 bits, en décimal), `epreuve_niveau`
  {`chemin`, `sha256`, `taux` par cellule, `niveau_decisif_retenu`, `cout`}, `niveau_decisif` (0,99 ou 0,995). Elle remplit les
  marqueurs `CODE_BBIS`, `ENTROPIE_BBIS`, `EPREUVE_NIVEAU_DEUX_PLIS` renvoyés à cette ligne (texte, l. 5, 93, 116, 293 ; écart
  au gabarit accordé, R-2740).
- **Gardes** : épreuve absente, réduite, d'une autre entropie, niveau hors règle, commit illisible, entropie courte, fiche déjà
  présente → ni fiche ni ligne (texte, l. 194 ; `ecrire_fiche_code`, l. 131 à 156).
- **Relue** au lanceur (`creation`, `ancetre` dans la racine de la mère : `lancer_bbis_v3.sh`, l. 89 et 90), sur l'instance
  (`marche_v3.gardes_d_entree`, l. 201 à 231 : `SCELLEMENT-BBIS`, `CODE-BBIS`, `GO-BBIS` scellées, commit de la fiche ancêtre de la
  tête, 103 empreintes égales, sinon arrêt R11) et à la lecture (`lecture_v2.main`, l. 1338 et 1339 : l'entropie vient de la fiche).

### 1.2 À quel commit, et pourquoi

**Recommandation : la fiche cite `ce47056455595bc52fad676c0e57ad9d8bef886d`** (confiance 0,8).

- C'est le code **joué sur la carte** à la quatrième passe (`75bc5b32`, parent `ce470564` ; R-2957 ; addendum, § 5, point 5) et
  **déclaré bon pour partir** (R-2933 : « la quatrième passe de répétition peut partir avec ce code (`ce470564`) »).
- **Vérifié** : `git diff --stat ce470564 bd1472ad` = 16 fichiers **ajoutés**, tous sous `brouillons/T0.7-etape-B-bis-v1/`
  (addendum et ses brouillons, contre-lectures, programmes de couples, vérification éclair), **aucun** des 103 chemins ; les 103
  empreintes `git show COMMIT:chemin | sha256sum` sont égales à `ce470564`, à `bd1472ad` et sur le disque (`cmp` sans écart ; aucun
  filtre de fin de ligne, `git check-attr` : `text: unset`) ; les sept modules nommés par l'addendum portent ses empreintes.
- Le commit de fusion du § 1.3 (M_b) a les mêmes 103 empreintes et peut aussi être cité (sens du « commit X » du développeur : « son
  arbre porte les empreintes ») ; `ce470564` est préféré parce que c'est le commit contre-lu et joué. La fiche ne peut citer ni le
  commit qui la porte ni un descendant (garde d'ancêtre, `registre_bbis_v1`, l. 182 à 206).

### 1.3 Sur quelle branche, et le commit de l'instance

- **Le code de B bis n'est pas sur `main`** (aucun fichier sous `src/controle_ia/t07bbis/` à `377a2a0c` ; base commune `048d8e99`
  du 14 novembre 13:50Z) et **n'y entre pas avant l'exécution de l'étape B** (R-2760, décision de routine : « il ne sera pas versé
  dans `main` avant l'exécution de l'étape B … fusionné après l'étape B »).
- **Branche de la course : `prep/t07bbis-code-v1`** (`BRANCHE_CODE`), sa propre histoire contient `ce470564` (condition B1 :
  interprétation 22 du rapport des corrections v1). L'instance la clone seule (`--single-branch`, amorce, l. 145), extrait COMMIT
  (l. 173), lit le registre propre **à ce commit** (l. 177 à 181) : les lignes de B bis doivent donc être **sur cette branche**.
- **Elle reçoit `main` une fois, maintenant** (commit **M_b** = `git merge --no-ff` de `main` à `377a2a0c`, ou de sa tête si elle
  passe le même relevé, dans la branche), parce que la **lecture** en a besoin : sur la branche, le registre partagé ne porte ni
  `CODE-MOTS-ET-COUT-T06` ni `AUDIT-FUITES-T07` (inscrites sur `main` à 14:55:41Z et 14:57:54Z, après la base) ; sans la première,
  `lecture_v2.adaptateur_retenu` (l. 1304 à 1315) prendrait **en silence** l'implémentation de repli, contre le texte (la ligne est
  inscrite avant mercredi 12:00Z, l. 76). Pour la course seule, M_b n'est pas nécessaire ; le faire maintenant est le seul moment sûr
  (§ 10, b).
- **Fusion vérifiée en lecture seule** (`git merge-tree 048d8e99 377a2a0c bd1472ad`) : **aucun conflit** (195 ajouts du seul côté de
  la branche, aucun fichier changé des deux côtés) ; sur les 103 chemins, 61 identiques sur `main`, 42 absents de `main` comme de la
  base : **aucun** n'a été changé par `main` ; les quatre fichiers de la pièce « mots et coût » ajoutés des deux côtés sont
  **identiques à l'octet** ; registre propre identique des deux côtés (objet `598607db…`, fin de ligne finale présente) ; journal
  des ouvertures identique des deux côtés (objet `76dde869…`, celui de l'étape A, R-2637).
- **COMMIT de l'instance** = la tête de `prep/t07bbis-code-v1` après la ligne `GO-BBIS`, **poussée** avant la création. **RACINE du
  lanceur** = un arbre de travail de cette branche à COMMIT (celui-ci, ou un neuf), dont `origin` est `lciric/controle-ia-travail`.
- **`main`** ne reçoit, avant le verdict de B bis, que des lignes R- de `registres/decisions.md` (texte, sans code) et
  `registres/etat.md` ; les lignes du registre propre y arrivent par la fusion finale (§ 6, point 6).

### 1.4 Commandes (forme du rapport des corrections v2, § 3, adaptée : branche du code, fiche v3, commit `ce470564`)

Dans l'arbre de travail de `prep/t07bbis-code-v1`, arbre propre ; `PY=/home/user/controle-ia-travail/.venv/bin/python`,
`PYTHONPATH=src` ; processeur seulement.

```bash
cd /home/user/controle-ia-travail/.claude/worktrees/agent-a4f221610ce6d5a67        # ou un arbre neuf de la branche
export PYTHONPATH=src PY=/home/user/controle-ia-travail/.venv/bin/python
X=ce47056455595bc52fad676c0e57ad9d8bef886d
L=brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v3.txt
EL=brouillons/T0.7-etape-B-bis-v1/code/empreintes-fiche-code-bbis-v3-ce470564-v1.txt     # à committer d'abord, avec son compagnon
M0=377a2a0c9b1ec2704374a50537d5c59ae39b0ac7                                             # ou la tête de main au relevé ci-dessous
# geste 0 a — relevé « main sans rien de l'étape B », par les noms seulement (à consigner dans la ligne R-)
test "$(git rev-parse "$M0:registres/scellements-v1.md.ouvertures.md")" = 76dde869e99c7ab7d05c934405722bd80a1a17bc
test "$(git ls-tree -r --name-only "$M0" | grep -c -E '(^|/)(lecture-t07|arret-etape-b)\.json$')" = 0
git ls-remote --exit-code origin 'refs/heads/verdict/t07-etape-b*' > /dev/null 2>&1; test $? = 2
# geste 0 b — main reçue une fois, sans écrasement ; contrôles ; poussée de la branche (jamais de main)
#   d'abord : committer sur la branche ce plan, la liste préparée et leurs compagnons (non suivis à 12:17Z : sans ce commit,
#   l'arbre n'est pas propre et la ligne suivante arrête tout)
$PY -m controle_ia.scellement verifier brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md "$EL"
git add brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md.sha256 \
    "$EL" "$EL.sha256" && git commit -m "B bis : plan de course v1 et empreintes de la fiche au commit ce470564"
test -z "$(git status --porcelain --untracked-files=all)"
git merge --no-ff -m "B bis : main reçue une fois avant la course (sans rien de l'étape B), R-2760" "$M0"
$PY -m controle_ia.scellement verifier "$L" "$EL"
git merge-base --is-ancestor "$X" HEAD && git diff --quiet "$X" HEAD -- $(cat "$L") && sha256sum -c --quiet "$EL"
git push origin prep/t07bbis-code-v1
# geste 1 — entropie tirée pour CODE-BBIS, scellée, committée AVANT l'épreuve (interprétation 29 ; jamais retirée)
E=$($PY -c 'import numpy as np; e = np.random.SeedSequence().entropy; assert e.bit_length() > 64; print(e)')
$PY -c 'import datetime, json, sys
from controle_ia.scellement import sceller
p = "registres/t07-etape-b-bis/entropie-bbis-v1.json"
open(p, "x", encoding="utf-8").write(json.dumps({"entropie": sys.argv[1], "commit_code": sys.argv[2],
    "outil": "numpy.random.SeedSequence().entropy", "tiree_le": datetime.datetime.now(datetime.timezone.utc).strftime(
    "%Y-%m-%dT%H:%M:%SZ"), "texte": "prereg/T0.7-etape-B-bis-v1.md"}, indent=1) + "\n")
print(sceller(p))' "$E" "$X"
git add registres/t07-etape-b-bis/entropie-bbis-v1.json registres/t07-etape-b-bis/entropie-bbis-v1.json.sha256
git commit -m "T0.7 étape B bis : entropie de CODE-BBIS tirée et scellée avant l'épreuve de niveau"
# geste 2 — épreuve de niveau : § 2
# geste 3 — fiche (empreintes lues sur le disque ; égales à la liste préparée)
git diff --quiet "$X" -- $(cat "$L") && test -z "$(git status --porcelain -- $(cat "$L"))"
$PY -m controle_ia.t07bbis.registre_bbis_v1 fiche . registres/t07-etape-b-bis/code-bbis-v1.json "$X" "$E" \
    registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json $(cat "$L")
$PY -c 'import json, sys
f = json.load(open(sys.argv[1], encoding="utf-8"))
l = dict(reversed(x.split("  ", 1)) for x in open(sys.argv[2], encoding="utf-8").read().splitlines())
assert len(l) == 103 and f["fichiers"] == l and f["commit"] == sys.argv[3], "fiche ≠ liste préparée"
print("fiche = liste préparée (103 empreintes, commit", f["commit"][:8] + ")")' registres/t07-etape-b-bis/code-bbis-v1.json "$EL" "$X"
git add registres/t07-etape-b-bis/code-bbis-v1.json registres/t07-etape-b-bis/code-bbis-v1.json.sha256
git commit -m "T0.7 étape B bis : fiche de CODE-BBIS (commit ce470564, 103 empreintes, entropie, épreuve de niveau)"
# geste 4 — ligne CODE-BBIS (outil du code : refuse le registre partagé, une clé hors marque, une ligne déjà présente)
$PY -c 'import time
from pathlib import Path
from controle_ia.t07 import registre_v1 as rg
from controle_ia.t07bbis import registre_bbis_v1 as rb
c = "registres/t07-etape-b-bis/code-bbis-v1.json"
s = rg.sceau_conforme(Path(c)); rb.lire_fiche_code(Path(c))
print(rb.ajouter_ligne_propre(Path("."), rb.REGISTRE_PROPRE, "CODE-BBIS", int(time.time()), c, s))'
git add registres/t07-etape-b-bis-v1.md && git commit -m "T0.7 étape B bis : ligne CODE-BBIS au registre propre"
$PY -m controle_ia.t07bbis.registre_bbis_v1 ancetre . HEAD      # attendu : « BBIS ANCETRE ce470564… de <tête> »
```

Essais du paquet après M_b (`tests/test_t07bbis_*.py`) : **utiles, non bloquants** (les 103 fichiers sont ceux de `ce470564` :
183 passés sur la session, R-2933 ; l'amorce les rejoue sur l'instance avant la marche, au moins 115 : l. 44 et 235 à 241) ; s'ils
se jouent ici, **après la fin du PID 612** (R-2970).

### 1.5 Ce qui est préparé

`brouillons/T0.7-etape-B-bis-v1/code/empreintes-fiche-code-bbis-v3-ce470564-v1.txt` : les 103 empreintes au commit `ce470564`,
dans l'ordre de la liste de la fiche (`b8fb095b…`), au format de `sha256sum`. La fiche elle-même **n'est pas écrite** : elle exige
l'entropie et l'épreuve, tirées et jouées à l'inscription (interprétation 29 ; jamais une entropie tirée d'avance).

## 2. L'épreuve de niveau de la règle (a) en deux plis

- **Ce que c'est** (texte, « Seuil », l. 93 ; constat m3) : la règle (a) est lue en deux plis, extension que T0.7 n'a pas
  simulée ; l'épreuve mesure, **sur données synthétiques seulement**, son taux de fausse lecture « au-dessus » au niveau de 99 %,
  dans deux cellules (`scripts/epreuve_niveau_deux_plis_bbis_v1.py`, l. 1 à 22) : `nul` et `signal-commun` ; 1 000 jeux par cellule
  de la forme de 7b (64 tâches en deux plis, dix positifs et dix négatifs par tâche, 800 directions appariées, 2 000 tirages), lus
  par la fonction de production `plis_v1.regle_a`.
- **Critère, mécanique** : taux > **0,01** en estimation ponctuelle dans une cellule → niveau décisif **99,5 %** ; sinon 99 %.
  Inscrit **par la fiche**. Si 99,5 % : puissance recalculée par une **version neuve** du script de calculs
  (`pieces/calculs-bbis-v3.py` et sa sortie ; texte, l. 93, K6), avant la création (lecture du développeur, § 4).
- **Comment** : après le geste 1, sous l'entropie de `CODE-BBIS` (clé `bbis/epreuve-niveau`, texte, l. 116), réglages du texte ;
  sortie scellée par le script à la fin :

```bash
nohup env PYTHONPATH=src OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 \
    $PY scripts/epreuve_niveau_deux_plis_bbis_v1.py --entropie "$E" \
    --sortie registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json --processus 1 > /tmp/epreuve-bbis-v1.log 2>&1 &
echo "PID $!"     # arrêt éventuel par ce seul PID (R10)
# fin : $PY -m controle_ia.scellement verifier registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json ; « complete »
# vrai ; git add du fichier et du compagnon ; commit « épreuve de niveau de la règle (a) en deux plis, complète »
```

  Fils à un et `nice` : **choix de routine proposé ici** (le développeur ne les pose pas), pour ménager le PID 612 et pour aligner
  l'épreuve sur la lecture, qui exige déjà un seul fil (`lecture_v2.main`, l. 1319) ; résultat déterministe, indépendant du nombre
  de processus (essai du paquet).
- **Coût** : processeur seulement, 0 USD ; **≈ 25 minutes** (0,73 s par jeu mesuré, 2 × 1 000 jeux ; rapport des corrections v2,
  interprétation 32) ; **au plus 3,5 heures** sous charge ; à un fil, non mesuré. Interrompue : rien n'est écrit, elle se rejoue sous
  la **même** entropie.

## 3. La ligne `GO-BBIS`

- **Ce que c'est** : la ligne du registre propre qui recopie l'extrait de la ligne de dépense `GO-2026-11-14-09` (texte, l. 195 et
  218). Sans elle : création refusée (`exiger_creation`, l. 383 à 400), marche arrêtée (`marche_v3`, l. 212).
- **Qui** : la mère, par `ajouter_ligne_propre`, **strictement après** `CODE-BBIS` (`SCELLEMENT-BBIS` < `CODE-BBIS` < `GO-BBIS` <
  `SCORES-BBIS`), sur la branche de la course.
- **Sur quel mot** : aucun mot neuf ; celui de Lazar est déjà là (R-2740 ; GO-2026-11-14-09 : 40 USD, une A100, une relance au plus,
  échéance 2026-11-22). Convention de l'extrait : celle de `registres/go-extraits/GO-LECTURE-T07-v1.md` (la ligne de `go.md` à
  l'octet plus une fin de ligne : vérifié, `8893d8df…` redonné).
- **Préparé** : extrait `registres/go-extraits/GO-BBIS-v1.md` = la ligne `GO-2026-11-14-09` de `registres/go.md` (ligne 328 sur
  `main`) ; **empreinte attendue `33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62`**, la même sur `main` et sur
  la branche ; chemin dans les motifs de l'amorce (l. 168) et copié comme fichier cité (l. 177 à 180).

```bash
test ! -e registres/go-extraits/GO-BBIS-v1.md && grep '^| GO-2026-11-14-09 ' registres/go.md > registres/go-extraits/GO-BBIS-v1.md
test "$(grep -c '' registres/go-extraits/GO-BBIS-v1.md)" = 1
$PY -m controle_ia.scellement sceller registres/go-extraits/GO-BBIS-v1.md     # attendu 33f38e67…
$PY -c 'import time
from pathlib import Path
from controle_ia.t07 import registre_v1 as rg
from controle_ia.t07bbis import registre_bbis_v1 as rb
from controle_ia.t07bbis.lecture_v2 import lire_lignes
c = "registres/go-extraits/GO-BBIS-v1.md"
t = int(time.time())
avant = lire_lignes(Path(rb.REGISTRE_PROPRE), ("CODE-BBIS",), ("CODE-BBIS",), propre=False)["CODE-BBIS"]["instant"]
assert t > avant, "GO-BBIS doit suivre CODE-BBIS strictement : rejouer une seconde plus tard"
print(rb.ajouter_ligne_propre(Path("."), rb.REGISTRE_PROPRE, "GO-BBIS", t, c, rg.sceau_conforme(Path(c))))'
git add registres/go-extraits/GO-BBIS-v1.md registres/go-extraits/GO-BBIS-v1.md.sha256 registres/t07-etape-b-bis-v1.md
git commit -m "T0.7 étape B bis : extrait de GO-2026-11-14-09 et ligne GO-BBIS au registre propre"
git push origin prep/t07bbis-code-v1 && COMMIT=$(git rev-parse HEAD)      # COMMIT de l'instance, poussé avant la création
```

Puis, **sur `main`**, la ligne R- qui consigne le relevé du geste 0 a, M_b, l'entropie (par son fichier), l'issue de l'épreuve, la
fiche, `CODE-BBIS`, `GO-BBIS` et COMMIT, et `registres/etat.md` (avec la mention de l'addendum, addendum § 6) : texte seulement,
aucun fichier de code.

## 4. La création de la course

### 4.1 Gestes de session (le lanceur ne crée rien : il contrôle et imprime, `lancer_bbis_v3.sh`, l. 4 à 6)

```bash
cd <arbre de travail de prep/t07bbis-code-v1, à COMMIT>
export PYTHON_BBIS=/home/user/controle-ia-travail/.venv/bin/python VASTAI_BBIS=/home/user/vastai-env/bin/vastai
V=/home/user/vastai-env/bin/vastai          # « vastai » absent du chemin de la session (relevé à 11:58Z)
D=/home/user/bbis-course-envoi-v1; mkdir "$D"          # dossier neuf (R12)
# (a) inventaire d'avant : identifiants et étiquettes seulement, dans "$D/ids-avant.txt" (jamais la liste brute affichée)
# (b) recherche d'offres (lecture seule) ; offre construite par programme, jamais retapée
( umask 077; $V search offers 'gpu_name=A100_SXM4 num_gpus=1 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0' -o 'dph_total' --raw > "$D/recherche.json" )
bash scripts/lancer_bbis_v3.sh offre-depuis-recherche "$D/recherche.json" OFFRE_ID "$D/offre.json"
# (c) feu écrit de la mère (ligne R- inscrite), qui porte « GO-2026-11-14-09 » ; garde de création
bash scripts/lancer_bbis_v3.sh creation . "FEU" 0
# (d) commande imprimée (13 arguments) : rejoue offre, amorce en essai local, création, ancêtre, branche de sortie absente
RUNB=$(date -u +%Y%m%d-%H%M%S)-bbis-t07-v1; ECH=$(( $(date +%s) + 13 * 3600 ))
bash scripts/lancer_bbis_v3.sh commande . "$D/offre.json" OFFRE_ID "$COMMIT" prep/t07bbis-code-v1 20261111-151701-t06-reel \
    calcul/t06-confirmation-7b-v1 "$RUNB" "$ECH" "FEU" 0 python:3.11-bookworm
```

- **Arguments** : BRANCHE_CODE `prep/t07bbis-code-v1` (§ 1.3) ; RUN_7B `20261111-151701-t06-reel` (texte, l. 67) ; BRANCHE_7B
  `calcul/t06-confirmation-7b-v1` (texte, l. 27 ; présente à distance, code 0 à 11:57:25Z ; ses fichiers ne sont pas relus ici :
  l'amorce s'arrête si l'un manque, l. 188 à 193) ; RUN_BBIS de forme `AAAAMMJJ-HHMMSS-bbis-…` (amorce, l. 101) ; RELANCES 0 ; FEU =
  le texte du feu écrit, qui contient `GO-2026-11-14-09` (`exiger_creation`, l. 392).
- **Commande imprimée** (`lancer_bbis_v3.sh`, l. 95) : `GO_ID=GO-2026-11-14-09 vastai create instance OFFRE_ID --raw --image
  python:3.11-bookworm --disk 150 --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=… -e BRANCHE_CODE=prep/t07bbis-code-v1 -e
  RUN_7B=… -e BRANCHE_7B=… -e RUN_BBIS=… -e ECHEANCE_UTC_S=… -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e
  GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo <amorce en base64> | base64 -d > /root/amorce_bbis_v3.sh && bash
  /root/amorce_bbis_v3.sh"`. **Seul écart de forme permis, écrit dans le feu** : `vastai` par son chemin complet
  `/home/user/vastai-env/bin/vastai` (comme les lignes du pilote) ; le reste à l'octet. **`GH_TOKEN`** pris de
  `CONTROLE_IA_GITHUB_TOKEN_2`, par son nom, dans le seul shell de lancement, exporté avant la commande (R-2829 ; `$GH_TOKEN` se
  développe avant toute affectation en tête de ligne) ; **`HF_TOKEN`** par son nom, présence vérifiée par `test -n "${HF_TOKEN:-}"`,
  jamais affichée (§ 9, point 3).
- **Étiquette** `bbis-t07-v1` (texte, l. 218) ; **image** `python:3.11-bookworm` (étape A, 7b, quatre passes) ; **disque** 150 Go.
- **Garde CUDA, deux fois** : à l'offre (`cuda_max_good` ≥ 13.0, refus si absent ou illisible : `faute_cuda_hote`, l. 272 à 287) et
  sur l'instance avant toute installation (« CUDA Version » de `nvidia-smi` ≥ 13.0, sinon arrêt en code 2 : amorce, l. 75 à 94 et
  135 à 141 ; leçon de R-2844). Quatrième passe : pilote 595.91.07, CUDA 13.2, torch `2.14.1+cu130`.
- **Échéance de la minuterie** : **13 heures** après l'impression (bornée à 24 heures, amorce l. 113). La garde de débit laisse courir
  une marche projetée jusqu'à 11 heures (texte, l. 105) et le texte interdit d'arrêter une marche lente mais vivante (l. 196) ;
  11 heures + au plus 1 heure de mise en place (devis v3) + la poussée tiennent dans 13 heures (≈ 15,5 USD au prix de la quatrième
  passe, 1,193 USD/h).
- **Feu et préavis** : feu écrit portant le numéro avant toute location (GO-2026-11-14-09) ; préavis d'une ligne à Lazar au moment
  du geste (R-2883, point 2).

### 4.2 La création : tentative sans règle de permission, par un opérateur

GO-2026-11-16-02 (R-2952) ne valait que pour la quatrième passe. Pour la course, l'autonomie en cours couvre la voie de **R-2883,
point 2** (reprise par GO-2026-11-15-07, -16-03 et -16-04) : geste à risque de refus **joué par un opérateur sous-agent du modèle
B**, préavis d'une ligne à Lazar sans attendre son signal ; **arrêt au premier refus**, sans rejeu ni reformulation ni contournement
(aucune chaîne coupée, aucun script qui la recompose : faute dite en R-2950). Une **règle de permission** dans
`.claude/settings.json` ne s'ajoute que par Lazar lui-même (R-2950). L'opérateur relit l'identifiant dans la sortie de la création
(`new_contract`), jamais retapé, puis un inventaire d'après (une seule instance ajoutée, étiquette `bbis-t07-v1`).

### 4.3 Branche de sortie

`donnees/t07-etape-b-bis-v1` (amorce, l. 36) : **absente à distance** — `git ls-remote --exit-code origin
refs/heads/donnees/t07-etape-b-bis-v1` rend **2** le 2026-11-16 à 11:57:25Z depuis l'arbre de travail ; le motif
`refs/heads/donnees/t07-etape-b-bis*` rend 2 ; témoin positif `refs/heads/prep/t07bbis-code-v1` rend 0 (`bd1472ad`). Relevé refait
mécaniquement par `commande` (lanceur, l. 47 à 63 et 91) et par l'amorce avant la marche (l. 250). La branche est créée **après** la
marche, depuis COMMIT (le commit local des entrées de 7b n'est jamais poussé : amorce, l. 270 à 280).

### 4.4 Devis dans la ligne GO-2026-11-14-09 (40 USD, coupure 39,5 USD)

- **Mesuré à la quatrième passe** (`cbcaeb52…`) : médiane 2,79 s par apprentissage (« linéaire » 1,75 s, « attention » 3,5 s) ;
  **marche projetée 3,2 à 3,4 heures** pour 2 460 apprentissages (facteur 1,2, + 0,6 h, relecture 0,35 à 0,55 h comprises ; limite
  11 h) ; mise en place sans modèle : création 00:35:00Z → minuterie 00:37:24Z → clonage 37 s → paquets 91 s → essais 80 s.
- **Attendu** : mise en place 0,3 à 0,6 h (modèle ≈ 16 Go, données de 7b ≈ 1 à 2 Go) + marche 3,0 à 3,9 h + poussée 0,2 à 0,3 h ⇒
  **≈ 3,5 à 4,5 heures d'instance**, ≈ 4,5 à 6 USD à 1,2 à 1,3 USD/h, plus disque et descente : **≈ 6 à 8 USD** (devis v3 : 5,6 à
  9,9).
- **Déjà imputé** : répétitions ≈ 0,749 USD (R-2957). **Pire cas** : minuterie à 13 heures puis une relance aussi longue ≈ 34 USD,
  sous la coupure. Garde de dépense au moins chaque heure : `bash scripts/lancer_bbis_v3.sh depense CUMUL PRIX` (cumul relevé =
  0,749 + heures × prix relu + disque ; refus ⇒ destruction).

### 4.5 Le pilote 60918148 et la consigne K4

- **K4** (consignes v13 de la mère, l. 24 ; procédure v14, point 2.5 (ii)) : entre l'inventaire d'avant la création du pilote et sa
  preuve d'absence, **aucune autre création ni destruction chez le loueur par une session du programme**, la mère comprise.
- **Ce que l'outil du pilote compare encore** : l'inventaire d'après et `ajoute` sont faits (R-2968). Reste la section 11 :
  `detruire` écrit `ids-avant-destruction.txt`, la session détruit, `verifier-destruction` ne prouve l'absence que si l'identifiant
  manque **et si toute autre instance de la référence est encore listée** (procédure v14, section 11, points 1 à 3). Donc : une
  machine de B bis créée **avant** la section 11 du pilote et **vivante jusqu'à sa fin** est un témoin de plus, sans gêne ; détruite
  **entre** `detruire` et `verifier-destruction` du pilote, elle fait refuser à tort (« témoin absent ») ; créée pendant cette
  fenêtre, la règle écrite ne la voit pas, mais K4 l'interdit.
- **Options** (décision de la mère : K4 est sa consigne) :
  - **(a) tenir K4** : la création attend la preuve d'absence du pilote ; aucun risque pour son outil ni pour une procédure
    vérifiée ; au pire, échéance du pilote 2026-11-17T04:26:21Z + 5 minutes, course finie vers 09:00Z mardi, dans l'autonomie ;
  - **(b) exception écrite à K4** (ligne R-), à trois conditions mécaniques : création hors de toute section 11 du pilote ; si le
    pilote finit pendant la course, sa section 11 se joue pendant que la machine de B bis vit ; la destruction de B bis ne commence
    pas pendant une section 11 du pilote (ni l'inverse) ; avantage : départ dès les préalables ; inconvénient : écart à une
    procédure vérifiée, fin du pilote imprévisible, une seule main exigée sur les deux machines ;
  - **recommandation : (a)**, confiance 0,6 ; (b) seulement si le pilote dure au-delà de la soirée, par décision écrite citant ce
    paragraphe. **Défaut proposé** : (a).

## 5. La preuve de destruction

- **Le lanceur de la course n'emploie aucune liste de témoins** : `verifier-destruction ID TEMOIN [LISTE.json]` reçoit le témoin en
  argument (`lancer_bbis_v3.sh`, l. 109 à 120 ; `exiger_absence`, l. 250 à 269). La liste `INSTANCES_D_AUTRES_SESSIONS`
  (`registre_bbis_v1`, l. 237 : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453) ne sert qu'à **refuser de détruire** ces
  identifiants (`exiger_identifiant_a_detruire`, l. 240 à 247, joué par `detruire` et `absence`).
- **Ce qui casserait** : (i) un témoin pris parmi 60480302, 60670453 ou 60599797 ⇒ « absence non prouvée : témoin absent », code 2,
  arrêt à tort (du côté sûr) ; (ii) aucune autre instance listée ⇒ absence non prouvable par le code ; (iii) le pilote **60918148
  n'est pas dans la liste de refus** : `detruire 60918148` serait accepté si on le tapait par erreur.
- **Consigne, sans toucher au code gelé** (preuve par l'inventaire, comme aux passes : « opérateur, puis liste relue par la mère »,
  R-2844, R-2869) : identifiant **lu** dans la sortie de la création et dans l'inventaire (étiquette `bbis-t07-v1`), jamais retapé,
  jamais 60918148 ni une instance d'une autre session ; inventaire de référence juste avant ; `bash scripts/lancer_bbis_v3.sh
  detruire ID`, ligne jouée avec le chemin complet de l'outil (`-y`) ; puis `bash scripts/lancer_bbis_v3.sh verifier-destruction ID
  TEMOIN` (avec `VASTAI_BBIS`), **TEMOIN pris dans l'inventaire du moment**, présent aussi dans l'inventaire d'avant la création,
  autre que l'identifiant (58936096 s'il est listé ; jamais 60480302, 60599797, 60670453), code 0 exigé ; enfin la mère relit
  l'inventaire : identifiant absent, toutes les autres instances de la référence présentes. Aucun témoin possible : nœud, ou preuve
  par la console du loueur, dite. **Aucune version neuve n'est nécessaire.**
- **Moment** : marche finie, l'amorce demande « stopped » (l. 49 à 54) ; la mère détruit dès les poussées vues ; arrêt de débit
  (code 3) : instance gardée au plus 12 heures, nœud de Lazar ((r1) ou (r2)), sans mot : destruction (texte, l. 105 et 187).

## 6. Après la course

1. **Poussées vérifiées** sur `donnees/t07-etape-b-bis-v1` (texte, « Données gardées », l. 212) ; sceaux contrôlés ; aucun score
   ouvert.
2. **`SCORES-BBIS`**, sur la branche de la course : cite `diag/<run-bbis>/sondes-bbis.json` (`marche_v3`, l. 26 et 27) ; ligne R- et
   registres des dépenses, des arrêts, `registres/etat.md` sur `main`.
3. **Lecture sur processeur** (texte, plan, point 10) dans une **copie à part** (dépôt neuf, objets propres, jamais un arbre de
   travail du dépôt de la mère, qui portera les références de l'étape B) : la branche de la course à la tête qui porte
   `SCORES-BBIS`, plus `donnees/t07-etape-b-bis-v1` et les fichiers de 7b, **jamais** `verdict/t07-etape-b-compte-3-v1` ni un
   commit de `main` postérieur à M0 ; commande : `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m
   controle_ia.t07bbis.lecture_v2 --racine R --run-7b 20261111-151701-t06-reel --run-bbis RUNB --run-lecture RUNL` (l. 1318 à 1347) ;
   MC par le code de la pièce (ligne présente après M_b) ; `ISSUE-MOTS-ET-COUT-T06` absente ⇒ réserve R-MC « sans contrôle
   d'égalité » (§ 10, c) ; `VERDICT-P3BIS` présente. Durée sur vraies données non mesurée ; **après le PID 612**. Sortie scellée
   avant toute lecture humaine, puis **`LECTURE-BBIS`** sur la branche.
4. **Verdict (R13)** : sous-agent neuf, **session neuve du compte 3** (nœud 2, R-2740), qui n'a écrit ni le texte, ni l'addendum, ni
   le code, **n'est lecteur ni de l'étape B ni de P3-bis**, n'a lu ni le verdict de l'étape B ni `lecture-t07.json` (texte, l. 115) ;
   ses fichiers sont **placés depuis la branche de la course et la branche des données de B bis seulement**, jamais depuis la racine
   de la phase C ni depuis `main` après M0 ; il applique les critères du texte **modifiés par EC-1 à EC-4** ; il cite (addendum,
   § 6) : (a) le texte, `0ae6210f…`, `SCELLEMENT-BBIS` ; (b) l'addendum, `f00eda8a…`, `ADDENDUM-ECART-1-BBIS` du registre voisin ;
   (c) `CODE-BBIS` (commit, fiche, entropie, épreuve) ; il ajoute à la main la citation de l'addendum et vérifie que la lecture porte
   **R-PILE** et le **point (7)** quand ils s'appliquent.
5. **Recevabilité** (registre voisin ; addendum, § 6) : un verdict qui ne cite pas `ADDENDUM-ECART-1-BBIS` n'est pas scellé ; la
   mère le vérifie, inscrit `VERDICT-BBIS` sur la branche, **soumet au directeur**.
6. **Fusion finale** : après `VERDICT-BBIS` **et** l'exécution de l'étape B (R-2760), `git merge --no-ff prep/t07bbis-code-v1` dans
   `main` (les lignes du registre propre y arrivent identiques ; aucun conflit attendu tant que personne n'écrit le registre propre sur
   `main`). La table conjointe suit les deux verdicts scellés, par un troisième lecteur neuf ; jamais « le meilleur des deux ».

## 7. Qui décide chaque geste

| # | geste | qui |
|---|---|---|
| 1 | relevé « `main` sans l'étape B », réception de `main` dans la branche (M_b), contrôles, poussée de la branche | autonomie (routine : code et branches) |
| 2 | entropie, épreuve de niveau, fiche, `CODE-BBIS`, sur la branche | autonomie (prescrits par le texte ; écart au gabarit accordé, R-2740) |
| 3 | si 99,5 % : script de calculs v3 | autonomie (règle mécanique) |
| 4 | extrait et `GO-BBIS` | autonomie (mot de Lazar déjà donné, R-2740) |
| 5 | contre-lecture de ce plan et de la commande exacte par un lecteur neuf | autonomie (condition de l'autonomie) |
| 6 | épreuve pendant le PID 612 (un fil, `nice`) | mère (sa règle R-2970) |
| 7 | exception à K4 | mère (sa consigne) ; défaut proposé : non |
| 8 | lecture de `HF_TOKEN` (clé déjà passée à 7b et à l'étape A, ou clé nouvelle) | mère ; si « nouvelle » : **mot du directeur** |
| 9 | feu écrit, préavis, recherche d'offre, commande imprimée | autonomie |
| 10 | création tentée sans règle par un opérateur du modèle B, arrêt au premier refus | autonomie (R-2883, point 2) |
| 11 | règle de permission ; tout refus d'une permission ou du classifieur | **mot du directeur** (R-2950) |
| 12 | dépense dans la ligne (≤ 39,5 USD, cumul compris), garde de dépense | autonomie |
| 13 | arrêt de débit : variante (r1) ou (r2) | **mot du directeur** (texte, l. 105) |
| 14 | une relance sur erreur de chaîne, avant le samedi 21 à 12:00Z | autonomie (une relance) |
| 15 | seconde relance, relance après le samedi 21 à 12:00Z, H200, plus de 40 USD | **mot du directeur** |
| 16 | correction de code après une course (« `CODE-BBIS` remplacée une seule fois », l. 186) : aucune ligne ne se réécrit et `ajouter_ligne_propre` refuse une clé présente | **mot du directeur** (version neuve ou addendum) |
| 17 | destruction, preuve d'absence, `SCORES-BBIS`, lecture, `LECTURE-BBIS` | autonomie |
| 18 | verdict, `VERDICT-BBIS` | autonomie ; **soumis au directeur** |
| 19 | fusion finale dans `main` (après `VERDICT-BBIS` et l'étape B) | autonomie (routine, R-2760) |
| 20 | seconde réception de `main` dans la branche avant le verdict de B bis (M1, § 10, c) | mère ; défaut proposé : non |
| 21 | prolongation de l'autonomie au-delà du 17 à 11:47:55Z | mère (GO-2026-11-16-04, inscrite avant l'échéance) |

## 8. Calendrier réaliste (UTC), avec durées et parallèles

| heure au plus tôt | B bis | durée | étape B (compte 3 ; calendrier de la phase C, § 3) |
|---|---|---|---|
| 12:35 | lecture du plan ; lecteur neuf lancé sur le plan et la forme de la commande | 30 à 45 min | préparateur de la commande de la phase B v2 (2 à 3 h) ; consigne du lecteur B (≈ 3 h) |
| 12:40 | geste 0 : relevé, M_b, contrôles, poussée de la branche | 10 min | — |
| 12:50 | geste 1 : entropie | 5 min | — |
| 12:55 | geste 2 : épreuve (si permise pendant le PID 612 ; sinon à sa fin) | 25 min (≤ 3,5 h) | — |
| 13:20 | gestes 3 et 4, extrait, `GO-BBIS`, poussée ; ligne R- sur `main` ; si 99,5 % : + 30 à 60 min | 10 min | — |
| 13:30 | feu, préavis, inventaire, recherche, commande imprimée | 10 min | — |
| **13:40, ou preuve d'absence du pilote + 10 min (K4)** | **création par l'opérateur** | 2 à 3 min | — |
| + 0,3 à 0,6 h | mise en place sur l'instance | | phase B jouée par l'hôte (< 2 h), puis `LECTURE-T08-BASE-A`, `ISSUE-MOTS-ET-COUT-T06`, bloc M sur `main` |
| + 3,0 à 3,9 h | marche | | remise de la phase C (5 à 7 h après le départ de la phase B) ; étape B jouée sur `verdict/t07-etape-b-compte-3-v1` |
| + 0,5 h | poussées, destruction, preuve d'absence, `SCORES-BBIS` | | recopie du journal puis du verdict B dans `main` (permise à tout moment : B bis ne reçoit plus `main`) |
| soir ou nuit | lecture (après le PID 612), `LECTURE-BBIS` | non mesurée | lecteur B, 2 à 4 h |
| mardi 17 | verdict B bis (session neuve du compte 3), `VERDICT-BBIS`, envoi au directeur | | verdict B ; puis fusion finale de B bis dans `main` ; table conjointe |

- **Heure au plus tôt de la création** = la plus tardive de : préalables faits (≈ 13:40Z si l'épreuve part maintenant) ; preuve
  d'absence du pilote + 10 minutes (K4, option a) ; fin du PID 612 + 45 minutes (si l'épreuve l'attend).
- **Exemples** : pilote fini à 15:00Z ⇒ création ≈ 15:10Z, `SCORES-BBIS` ≈ 19:00 à 20:00Z. Pilote jusqu'à son échéance (04:26:21Z
  mardi) ⇒ création ≈ 04:40Z, `SCORES-BBIS` ≈ 08:30 à 09:30Z mardi, dans l'autonomie. Les jours du calendrier scellé sont des visées,
  non des conditions ; comptent la relance avant le samedi 21 à 12:00Z, l'échéance de la ligne (22 novembre) et le verdict au plus
  tard le dimanche 22.

## 9. Points bloquants et réserves

1. **R-2760 et § 15 (5) de la phase C** : la course ne part pas de `main` ; la branche ne reçoit `main` qu'une fois, **avant** toute
   recopie de l'étape B (relevé du geste 0 a) ; tout geste de B bis jusqu'à `VERDICT-BBIS` s'écrit sur la branche (§ 10).
2. **K4** : la création attend la preuve d'absence du pilote 60918148, sauf exception écrite de la mère (§ 4.5) ; la destruction de
   B bis ne tombe jamais dans la section 11 du pilote.
3. **`HF_TOKEN`** : l'amorce l'exige (l. 134) et le garde dans la configuration de l'instance jusqu'à la destruction ; les quatre
   passes ne l'avaient pas reçu (aucune mention dans `lancer_repetition_bbis_v3.sh` ni `amorce_repetition_bbis_v3.sh`).
   GO-2026-11-15-03 exclut « le passage d'une clé nouvelle à une machine louée (dont `HF_TOKEN`, R-2857) » ; GO-2026-11-15-04 le
   permet sous condition, dont « retirée de l'environnement de la machine dès ce geste fait », que l'amorce gelée ne tient pas. Si la
   clé est celle déjà passée aux machines de 7b et de l'étape A (l'ordre d'exécution de l'étape A v2 porte `HF_TOKEN=$HF_TOKEN`), elle
   n'est pas nouvelle et rien ne bloque ; sinon : mot du directeur. Chaque passage se consigne au registre des décisions.
4. **Épreuve de niveau et PID 612** : R-2970 dit « sans calcul lourd tant que l'étape 0 de l'idée 1.1 (PID 612) chronomètre » (PID
   vivant à 12:02:49Z, 36 minutes écoulées, charge ≈ 1,4 sur 4 cœurs) ; l'épreuve occupe un cœur 25 minutes.
5. **Niveau 99,5 %** : script de calculs v3 avant la création (30 à 60 minutes de plus).
6. **Forme de la commande** : `vastai` absent du chemin ; chemin complet écrit dans le feu ; `PYTHON_BBIS` vers l'environnement du
   dépôt.
7. **Témoin** : jamais 60480302, 60599797, 60670453 ; 60918148 hors de la liste de refus du code (§ 5).
8. **Réserves de méthode** : fusions vérifiées par `merge-tree` en lecture seule et par comparaison d'objets, non jouées ; essais du
   paquet non rejoués ici ; durée de la lecture sur vraies données inconnue ; dans la copie à part de la lecture, la garde
   `anteriorite_etape_b` ne voit aucune référence de l'étape B et passe sans rien prouver (§ 10, a) : l'antériorité se prouve par le
   relevé de la mère.

## 10. Ordre avec l'étape B de T0.7 (questions de la mère, GO-2026-11-16-05)

### (a) B bis exige-t-elle que l'étape B ne soit ni exécutée ni lue au moment de sa course ?

**Non.** Le texte n'exige qu'une antériorité, celle du **scellement** : « strictement avant toute exécution de l'étape B » (statut,
l. 22 ; plan, point 2, l. 99 ; liste d'arrêt, l. 179), établie par `ABSENCE-B-BBIS` le 14 novembre (relevé refait par la mère avant
l'addendum, le 16 à 00:51:45Z, « écrit par symétrie », addendum § 4). Pour la course et après, il exige : aucun changement de
cellule, réglage, pli, adversaire, niveau ou seuil après la lecture d'une sortie de l'étape B (l. 180 : rien de tel n'est prévu,
tout est fixé par le texte, l'addendum, le code v3 et la fiche ; le niveau sort mécaniquement de l'épreuve) ; aucun fichier de l'étape
B au lecteur de B bis, ni l'inverse, avant les deux verdicts (l. 197) ; un lecteur du verdict de B bis qui n'a lu ni le verdict B ni
`lecture-t07.json` (l. 115) ; `lecture-t07.json` n'est ouvert que par la table conjointe, après les deux verdicts (l. 98). Par
symétrie (R4), il vaut mieux que l'entropie, l'épreuve et `CODE-BBIS` précèdent toute lecture humaine d'une sortie de l'étape B :
c'est le cas dans l'ordre ci-dessous (l'étape B attend la phase B, plusieurs heures).

**Le code v3** : ni l'amorce ni la marche ne contrôlent l'étape B (aucune mention de `lecture-t07.json`, `arret-etape-b.json` ni du
journal des ouvertures) ; l'extraction partielle de l'instance n'apporte de `diag/` que les fichiers de 7b nommés et ceux que cite le
registre propre (amorce, l. 147 à 209) : une sortie de l'étape B n'y monte que si COMMIT la porte. **Seule la lecture contrôle** :
`lecture_v2.anteriorite_etape_b` (l. 585 à 604), sur **toutes les références locales** de sa racine, exige que le premier commit qui
ajoute `*lecture-t07.json` ou `*arret-etape-b.json`, s'il existe, ait une date strictement postérieure au commit qui ajoute
`SCELLEMENT-BBIS` (`f72d2833`, 14 novembre 12:30:47Z) ; sinon refus et nœud. Une étape B jouée ce soir passe cette garde. Le journal
`registres/scellements-v1.md.ouvertures.md` n'est nommé par aucun module de `src/controle_ia/` ni script de B bis (recherche par nom ;
B bis tient le sien, `registres/t07-etape-b-bis-v1.md.ouvertures.md`, `registre_bbis_v1`, l. 113 à 119).

### (b) Le commit X, sa branche, et l'ordre qui tient les deux règles

- **Le X du développeur** (rapport des corrections v2, geste 0 ; R-2790) est le commit de `main` obtenu par `git merge --no-ff
  prep/t07bbis-code-v1` **dans `main`** ; la fiche le citait et COMMIT en descendait sur `main`. Il est **incompatible** avec les deux
  règles quand l'étape B et B bis se jouent de front : avant l'exécution de l'étape B, il met le code de B bis dans `main` (R-2760 :
  `CODE-T07` refuserait) ; après, `main` porte la recopie du journal puis du verdict B (phase C, § 15 (1) et (2)), et tout COMMIT ou
  toute racine de B bis qui en descend les porterait (§ 0.5 et § 15 (5)). Seule une fenêtre étroite (étape B exécutée, journal pas
  encore recopié) le permettrait : fragile, et elle laisserait la lecture et le verdict de B bis sans espace propre.
- **Ce que ce plan met à sa place** : (1) la fiche cite **`ce470564`**, sur `prep/t07bbis-code-v1`, qui ne fusionne pas `main` ;
  (2) la branche reçoit `main` **une fois**, commit **M_b** (`--no-ff`, parents `bd1472ad` et M0 = `377a2a0c` ou la tête de `main`
  au relevé), **maintenant**, après le relevé du geste 0 a (journal des ouvertures à l'objet `76dde869…` de l'étape A, aucun
  `lecture-t07.json` ni `arret-etape-b.json`, `verdict/t07-etape-b*` absente à distance : code 2 à 12:10:54Z) ; (3) entropie,
  épreuve, fiche, `CODE-BBIS`, `GO-BBIS`, puis `SCORES-BBIS`, `LECTURE-BBIS`, `VERDICT-BBIS` s'écrivent **sur la branche**, qui ne
  reçoit plus `main` jusqu'à `VERDICT-BBIS` ; (4) COMMIT de l'instance = tête de la branche après `GO-BBIS` ; (5) l'espace du lecteur
  de B bis = la branche à la tête qui porte `LECTURE-BBIS` (aucun commit de `main` postérieur à M0) et les données de B bis, dans une
  copie à part ; (6) `main` reçoit la branche après `VERDICT-BBIS` et après l'exécution de l'étape B.
- **Ce qui tient alors** : R-2760 (le code de B bis n'entre dans `main` qu'après l'étape B) et § 15 (5) (rien de la branche de l'étape
  B, ni des recopies dans `main`, n'entre dans un espace de B bis avant son verdict scellé), **quel que soit l'ordre** entre la
  course de B bis et l'étape B ; la mère peut recopier le journal et le verdict B dans `main` quand elle veut. La phase C trouve sur
  `main` la ligne du plan scellé de B bis qu'elle exige (marqueur `<<CLE_PLAN_BBIS>>` à remplir par la mère, vraisemblablement
  `SCELLEMENT-BBIS` du registre propre, présente) et aucun code de B bis.
- **Une seule condition d'ordre** : **M_b avant toute recopie de l'étape B dans `main`** (c'est-à-dire maintenant). Si M_b n'a pas été
  fait à temps, la course reste possible (elle n'a pas besoin de M_b), mais la lecture devra prendre ses lignes du registre partagé
  autrement : nœud de la mère avant la lecture.

### (c) La course a-t-elle besoin de `ISSUE-MOTS-ET-COUT-T06` ?

**Non, ni la course ni la lecture.** La base « mots et coût » **ne se calcule pas sur la machine** : « MC se calcule à la lecture, sur
processeur : l'instance n'attend pas ce relevé » (liste d'arrêt, l. 193 ; plan, point 10 (c)). À la lecture, MC est calculé **par le
code de la pièce cité par `CODE-MOTS-ET-COUT-T06`** (ligne inscrite le 14 novembre à 14:55:41Z, avant l'échéance du repli ;
`lecture_v2.adaptateur_retenu`, l. 1304 à 1315, adaptateur `lien_mots_et_cout_v1:AdaptateurPieceMC`, qui refuse de se charger si le
module n'est pas à l'empreinte de la ligne), sur les mesures et les textes de 7b. `issue-mots-et-cout-t06.json` ne sert qu'au
**contrôle d'égalité** (aires recalculées égales à `aire_n029` et `aire_mots_et_cout` à 10⁻¹² près, cellules `S_d` ; « Métrique »,
l. 76) : absent à la lecture ⇒ « MC calculé sans contrôle d'égalité », réserve R-MC, **sans nœud ni attente** (l. 193) ; présent et
différent ⇒ MC « non calculable » et nœud. **Recommandation** : ne pas faire recevoir `main` une seconde fois par la branche pour
l'obtenir (M1) ; à ce moment-là `main` portera aussi des pièces de la phase C (consigne du lecteur B, liste « qui a lu quoi ») ;
accepter R-MC, confiance 0,6. Si la mère veut le contrôle d'égalité : M1 seulement après le même relevé que le geste 0 a et avant
toute recopie de l'étape B, décision écrite (tableau du § 7, ligne 20).

### Ordre recommandé de ce soir, les deux de front

1. **Maintenant (12:40Z)** : relevé du geste 0 a (noms seulement) ; **M_b** sur `prep/t07bbis-code-v1` ; contrôles des 103 ; poussée
   de la branche ; ligne R- sur `main`. *Avant toute remise de la phase B ou de la phase C.*
2. **B bis** : entropie → épreuve (25 min) → fiche → `CODE-BBIS` → extrait et `GO-BBIS` → poussée de la branche ; contre-lecture de
   la commande en parallèle ; feu ; création à la preuve d'absence du pilote (K4) ; course de 3,5 à 4,5 heures.
3. **Étape B, en parallèle** (compte 3, calendrier de la phase C § 3) : commande de la phase B v2 → phase B jouée → `LECTURE-T08-BASE-A`,
   `ISSUE-MOTS-ET-COUT-T06`, bloc M → remise de la phase C → étape B jouée sur sa branche → recopie du journal puis du verdict B dans
   `main`. Rien de ces gestes ne touche la branche de B bis ; aucun geste de B bis n'écrit sur `main` autre chose que des lignes R- et
   l'état.
4. **B bis, après la course** : `SCORES-BBIS`, lecture dans une copie à part, `LECTURE-BBIS`, verdict par une session neuve du compte
   3 (fichiers placés depuis la branche de B bis seulement), `VERDICT-BBIS`, envoi au directeur.
5. **Après les deux verdicts** : fusion de `prep/t07bbis-code-v1` dans `main` (R-2760) ; table conjointe par un troisième lecteur neuf.
