# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v3

Écrite le 2026-11-18 par le préparateur (sous-agent neuf, modèle Fable 5.2), sous `mandat-preparateur-lecture-bbis-v1.md` (`a6e027ce…`), son complément `complement-mandat-preparateur-lecture-bbis-v1.md` (`9a8b5515…`), son second complément `complement-2-mandat-preparateur-lecture-bbis-v1.md` (`8777bcf5…`) et les règles communes (`5f303a9c…`), compagnons vérifiés.

**Version 2.** La version 1 (`commande-lecture-bbis-v1.md`, `b308c9b12803ea58b470a7670881fc30274f0c93c04bc288d893146c6641e615`) reste, non jouée (R12). Cette version traite les cinq constats provisoires du premier contre-lecteur (`arret-contre-lecteur-commande-refus-crochet-v1.md`, `a903b87b…`) et les huit points du second complément ; chaque passage changé est dans `differences-commande-lecture-bbis-v1-v2.md`, avec son fondement. Tout le reste est le texte de la version 1, à l'octet.

**Version 3.** La version 2 (`commande-lecture-bbis-v2.md`, `4eea2d8a39c46ad2da27b7bd72852897a90eb122350ed55e5498eaaafc32b33d`) reste, non jouée (R12). Sa contre-lecture par un lecteur neuf d'un autre modèle (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d0483668df9fc6fb2661c4e4fad1425221a5061049e9731fb7128390925`) conclut « jouable après corrections mineures » : aucun constat majeur, sept mineurs. Cette version porte les remplacements m1 à m7 tels que le rapport les écrit, trois décisions d'organisation de la conductrice (sur m5, sur m6 et sur la note n3), et ce qui en découle strictement ; chaque passage changé est dans `differences-commande-lecture-bbis-v2-v3.md`, avec son fondement. Tout le reste est le texte de la version 2, à l'octet. **Cette version ne joue que le premier lancement.**

**Écrite par simple lecture.** Aucun bloc de cette commande n'a été joué, ni entier ni en partie : ni le module, ni sa garde, ni une de ses fonctions, ni le programme de la preuve après coup. Les blocs ont seulement passé un contrôle de syntaxe (`bash -n`), hors de tout dépôt. Le contre-lecteur les lit ; le lecteur-opérateur est le premier à les jouer.

**Cette commande ne contient aucune garde rejouée à part** : la garde d'ouverture s'exécute en tête de la lecture, dans le module (complément au quatrième addendum, § 3 et § 6). Tout ce qui précède le lancement est fait de commandes `git` en lecture, de calculs d'empreintes et de comptes de lignes.

**Ce que le lecteur-opérateur ne fait jamais** : ouvrir à l'œil un fichier sous `diag/`, `donnees/`, `runs/`, `docs/verdicts/` ; afficher la sortie d'un lancement au-delà de ce que le § 5.2 demande ; afficher le constat de forme destiné au juge ; arrêter un processus ; relancer ; corriger ; pousser.

**Aucune commande d'arrêt de processus n'est écrite dans cette commande**, sous aucune forme. Une lecture lente mais vivante n'est jamais arrêtée.

## 0. Module de lecture en vigueur ; ce qui fait foi

- **Module qui lit** : `src/controle_ia/t07bbis/lecture_v5.py`, empreinte `dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c`.
- **Ligne qui le fonde** : complément au quatrième addendum, CQ-3, bloc « Nouveau, qui fait foi » (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, l. 285) : « `lecture_v5` pour la lecture du point 10 du plan (les v1 à v4 restent, R12 ; […] la v5 est rattachée par le quatrième addendum et son complément, non par la fiche de `CODE-BBIS` ; la v4 n'est ni rattachée ni jouée pour la lecture ; ». Règle de préséance : même texte, § 0, et CQ-2.
- **Rattachement** : fiche `registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json` (`cd14195d396a779da954619c9a3405741fe11e2f98bf4aae3767cb87a5036ca0`), ligne `RATTACHEMENT-LECTURE-V5-BBIS` du registre voisin. Le module n'est pas dans la fiche de code : une troisième ligne `CODE-BBIS` est interdite.
- **Fiche de code** (`registres/t07-etape-b-bis/code-bbis-v2.json`, `4b28535c…`) : elle reste en vigueur pour les 63 fichiers qu'elle cite, pour l'entropie des graines et pour le niveau décisif. Relevé au premier tour : les 63 empreintes sont égales sur le disque et au commit de la fiche `05cd22aa…`. La commande le revérifie dans l'arbre de lecture (§ 1.4).
- **Textes** : texte scellé `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) ; addenda 1 (`f00eda8a…`), 2 (`18baeac3…`), 3 (`e5604cbd…`), 4 (`5ef929ea…`) et complément au quatrième (`12c90873…`) ; feu `registres/t07-etape-b-bis/feu-bbis-v7.txt`, § 12 et § 13.
- **Entropie et graines** (plan, point 12 ; troisième addendum, TA-3) : aucune n'est passée en argument. Le module lit l'entropie dans la fiche que cite la ligne `CODE-BBIS` en vigueur (`lecture_v5.py`, l. 1693-1695) et dérive une graine par clé `bbis/tirages/<ligne>`.

### Paramètres donnés par la conductrice au lancement

| nom | valeur |
|---|---|
| commit de `main` qui porte les inscriptions | `4aefb5b166b55a5ff7341454770a64caab923f52` |
| tête de la branche de travail après l'étape 0 (`TETE_TRAVAIL`) | donnée par la conductrice, 40 caractères |
| numéro du lancement (`N`) | `1` ; cette version ne joue que le premier lancement (§ 5.3) |
| nom, sur le distant, de la branche de l'arbre de lecture | `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture` (poussée par la conductrice, § 4.1) |

Relevé par les noms au commit `4aefb5b1…` (préparateur, `git show <commit>:<registre> | grep -c`) : les lignes `ADDENDUM-ECART-1-BBIS`, `-2-BBIS`, `-3-BBIS`, `ADDENDUM-ECART-4-BBIS`, `ADDENDUM-ECART-4-COMPLEMENT-BBIS` et `RATTACHEMENT-LECTURE-V5-BBIS` y figurent une fois chacune ; aucun fichier dont le nom commence par `lecture-t07` ou `arret-etape-b` n'y est suivi ; le commit de la course en est un ancêtre.

### Étape 0 — gestes de la conductrice, avant de lancer le lecteur-opérateur

La fusion est faite **par la conductrice, sur la branche de travail, avant le montage de l'arbre de lecture**. Je le juge plus sûr que de la laisser à l'opérateur : il ne tranche aucun conflit, l'arbre de lecture n'ajoute qu'un commit d'entrées, et le juge trouvera le registre voisin complet sur la branche de travail. Rien n'est poussé sur `main`.

```bash
cd /home/user/controle-ia-travail
git fetch origin                                              # récupération complète du distant, en lecture seule (décision d'organisation, m5)
git status --porcelain --untracked-files=all | wc -l          # attendu : 0, sinon on ne fusionne pas
git rev-parse --abbrev-ref HEAD                               # attendu : claude/lecture-verdict-etape-b-bis-v1
git merge --no-ff --no-edit 4aefb5b166b55a5ff7341454770a64caab923f52
# un conflit : `git merge --abort`, arrêt, rien n'est monté
J=registres/t07-etape-b-bis-v1.md.ouvertures.md
[ ! -e "$J" ] && printf '%s\n' "# Journal du registre propre du texte « T0.7, étape B bis » (registres/t07-etape-b-bis-v1.md) — une ligne par fichier de lecture écrit, ajoutée par le module de lecture ; lignes ajoutées, jamais réécrites" > "$J"
git add -- "$J" && git commit -q -m "Étape B bis, lecture : journal du registre propre créé avec sa seule ligne d'en-tête, avant toute lecture"
git rev-parse HEAD                                            # c'est TETE_TRAVAIL
```

- **Récupération complète du distant : décision d'organisation de la conductrice** (constat m5 de la contre-lecture de la version 2). La conductrice la fait ici, en lecture seule (`git fetch origin`), avant la fusion et le montage, pour que chaque branche de suivi locale soit à la tête du distant. L'opérateur ne fait que la comparaison (§ 1.1) ; sa permission d'appel au distant reste celle des trois branches nommées et de la lecture des têtes. Si le § 1.1 relève une branche absente ou à une autre tête, parce que le distant a avancé depuis, on ne lance pas : la conductrice refait cette récupération, puis l'opérateur rejoue le § 1.1 sous un nom de relevé neuf.
- La ligne d'en-tête ne porte pas la chaîne que le module compte comme une ligne d'ouverture (`lecture_v5.py`, l. 1436) : ne pas la changer.
- Le journal est créé « avec sa seule ligne d'en-tête, commité avant la lecture » (quatrième addendum, § 6.5, point 8).
- La conductrice commite aussi cette commande et sa contre-lecture avant ou avec ces gestes ; `TETE_TRAVAIL` est la tête après tout cela.

### Fichier des paramètres (premier geste du lecteur-opérateur)

Chaque bloc de la suite commence par relire ce fichier : l'état du terminal ne tient pas d'un appel à l'autre.

```bash
S=/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad
mkdir -p "$S/lecture-bbis"
[ -e "$S/lecture-bbis/parametres.sh" ] && { echo "parametres.sh existe déjà : arrêt"; exit 1; }
cat > "$S/lecture-bbis/parametres.sh" <<'EOF'
DEPOT=/home/user/controle-ia-travail
T=/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis
ARBRE="$T/arbre-de-lecture-v1"
PY="$DEPOT/.venv/bin/python"
LV1="$DEPOT/registres/t07-etape-b-bis/lecture-v1"
RUN_7B=20261111-151701-t06-reel
RUN_BBIS=20261118-154143-bbis-t07-v1
RUN_MC=20261116-205721-mots-et-cout-t06
RUN_B=20261114-001352-t07-lecture-reel
MAIN_INSCRIPTIONS=4aefb5b166b55a5ff7341454770a64caab923f52
TETE_TRAVAIL=REMPLACER_PAR_LA_TETE_DONNEE_PAR_LA_CONDUCTRICE
COURSE=438a9c5257bdc4fa65f25c42cc89753a049b4586
C_CONJ=c098fb512d999e1dbf7cef5fba6430ff8b1a8fb5
C_REMISE=06c8832819af344d01c184222833c5a42e8ac901
C_FICHE=05cd22aa15382f61eb62b9e7817890dde728dd5f
C_PIECE=da06bb57610f840152e4e9a8c449b036577cc582
REF_SORTIES=refs/remotes/origin/donnees/t07-etape-b-bis-v2
TETE_SORTIES=7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9
REF_7B=refs/remotes/origin/calcul/t06-confirmation-7b-v1
TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
REF_MC=refs/remotes/origin/verdict/t06-mots-et-cout-compte-3-v1
PROPRE=registres/t07-etape-b-bis-v1.md
VOISIN=registres/t07-etape-b-bis-v1-addenda-v1.md
PARTAGE=registres/scellements-v1.md
JOURNAL=registres/t07-etape-b-bis-v1.md.ouvertures.md
MODULE=src/controle_ia/t07bbis/lecture_v5.py
BRANCHE_DISTANTE_ARBRE=claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
NETTOYE=(env -u GIT_SSL_CAINFO -u GIT_ASKPASS -u GIT_EDITOR -u GIT_TERMINAL_PROMPT -u GIT_CONFIG_COUNT -u GIT_CONFIG_KEY_0 -u GIT_CONFIG_KEY_1 -u GIT_CONFIG_KEY_2 -u GIT_CONFIG_VALUE_0 -u GIT_CONFIG_VALUE_1 -u GIT_CONFIG_VALUE_2 -u BBIS_INSTANCE)
G() { "${NETTOYE[@]}" git -C "$ARBRE" "$@"; }
FAUTES=0
dire() { printf '%s\n' "$*"; }
egal() { if [ -n "$2" ] && [ "$2" = "$3" ]; then dire "CONFORME : $1"; else dire "DEFAUT : $1 (attendu « $2 » ; relevé « $3 »)"; FAUTES=$((FAUTES+1)); fi; }
vrai() { local l="$1"; shift; if "$@" >/dev/null 2>&1; then dire "CONFORME : $l"; else dire "DEFAUT : $l"; FAUTES=$((FAUTES+1)); fi; }
conclure() { dire "FAUTES : $FAUTES"; if [ "$FAUTES" = 0 ]; then dire "CONCLUSION : conforme, on continue"; else dire "CONCLUSION : ON NE LANCE PAS"; fi; }
neuf() { if [ -e "$1" ]; then echo "$1 existe déjà : on n'écrase jamais ; arrêt"; exit 1; fi; }
sceller() { ( cd "$DEPOT" && PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$1" ); }
EOF
```

Puis l'opérateur remplace, dans ce fichier, la valeur de `TETE_TRAVAIL` par celle que la conductrice lui a donnée, et rien d'autre.

**Deux temps.** Premier temps : § 1 à § 4.1 (mise en place, preuve relevée à part, commit local des entrées) ; l'opérateur rend la tête de l'arbre de lecture et s'arrête. La conductrice commite et pousse alors la pièce de la preuve sur la branche de travail, puis pousse la branche de l'arbre de lecture sous le nom ci-dessus (§ 4.1). Second temps, sur son message : § 4.2 à § 5.4.

**Règle pour tous les blocs d'avant le lancement** (§ 1 à § 4) : chacun finit par `CONCLUSION`. « ON NE LANCE PAS » veut dire : l'opérateur s'arrête, rend à la conductrice le chemin et l'empreinte du relevé et les lignes `DEFAUT`, et ne joue pas la suite. Ce ne sont pas des arrêts du programme de lecture : ils ne consomment rien, la lecture n'a pas été lancée. Les relevés ne portent que des noms, des empreintes, des identifiants de commit et des comptes.

## 1. Mise en place des fichiers

Les entrées de la liste blanche (plan, point 1) sont sur trois branches, relevées par les noms au premier tour :

| origine | branche locale de suivi | tête | ce qu'on en extrait |
|---|---|---|---|
| sorties de la course | `origin/donnees/t07-etape-b-bis-v2` | `7322049d…` (règles communes) | les 20 fichiers de `runs/`, `diag/`, `donnees/` du run `20261118-154143-bbis-t07-v1` (dix fichiers et leurs compagnons) |
| course de confirmation (7b) | `origin/calcul/t06-confirmation-7b-v1` | `55c3e3eb…` (feu, § 4) | cinq fichiers nommés et leurs compagnons ; **jamais** `lecture-sondes-t06.json` ni `resume.json`, qui sont sur cette branche et dans la liste « Jamais » |
| pièce « mots et coût » | `origin/verdict/t06-mots-et-cout-compte-3-v1` | aucune tête nommée par un texte ; le fichier est ancré par l'empreinte de la ligne `ISSUE-MOTS-ET-COUT-T06` | `issue-mots-et-cout-t06.json` et son compagnon |

Les fichiers cités par les lignes `VERDICT-P3BIS`, `CODE-MOTS-ET-COUT-T06` et `AUDIT-FUITES-T07` sont déjà suivis sur la branche de travail.

### 1.1 Dépôt à histoire complète, branches présentes, têtes

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
R="$T/releve-mise-en-place.txt"; neuf "$R"
{
cd "$DEPOT" || exit 1
dire "== 1.1 dépôt, $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git fetch origin donnees/t07-etape-b-bis-v2 calcul/t06-confirmation-7b-v1 verdict/t06-mots-et-cout-compte-3-v1 >/dev/null 2>&1; dire "récupération des trois branches : code $?"
egal "dépôt non superficiel" false "$(git rev-parse --is-shallow-repository)"
egal "tête de la branche de travail" "$TETE_TRAVAIL" "$(git rev-parse HEAD)"
egal "branche courante" claude/lecture-verdict-etape-b-bis-v1 "$(git rev-parse --abbrev-ref HEAD)"
egal "arbre principal propre (nombre de lignes de statut)" 0 "$(git status --porcelain --untracked-files=all | wc -l | tr -d ' ')"
vrai "le commit de la course est un ancêtre de la tête" git merge-base --is-ancestor "$COURSE" HEAD
vrai "le commit de main qui porte les inscriptions est un ancêtre de la tête" git merge-base --is-ancestor "$MAIN_INSCRIPTIONS" HEAD
egal "tête de la branche des sorties de la course" "$TETE_SORTIES" "$(git rev-parse --verify -q "$REF_SORTIES")"
egal "tête de la branche de la course de confirmation" "$TETE_7B" "$(git rev-parse --verify -q "$REF_7B")"
vrai "branche de la pièce « mots et coût » présente" git rev-parse --verify -q "$REF_MC^{commit}"
dire "tête de la branche de la pièce « mots et coût » : $(git rev-parse --verify -q "$REF_MC")"
if git ls-remote --heads origin > "$T/tetes-du-distant.txt" 2>/dev/null; then
  egal "tête des sorties sur le distant" "$TETE_SORTIES" "$(awk '$2=="refs/heads/donnees/t07-etape-b-bis-v2"{print $1}' "$T/tetes-du-distant.txt")"
  awk '{print $1" "$2}' "$T/tetes-du-distant.txt" | sed 's# refs/heads/# refs/remotes/origin/#' | sort > "$T/noms-distants.txt"
  git for-each-ref --format='%(objectname) %(refname)' refs/remotes/origin | grep -v ' refs/remotes/origin/HEAD$' | sort > "$T/noms-locaux.txt"
  egal "branches du distant absentes localement ou à une autre tête" 0 "$(comm -23 "$T/noms-distants.txt" "$T/noms-locaux.txt" | wc -l | tr -d ' ')"
else
  dire "DEFAUT : têtes du distant illisibles (git ls-remote) : présence de toutes les branches non prouvée"; FAUTES=$((FAUTES+1))
fi
dire "place libre : $(df -h "$T" | tail -1 | awk '{print $4}')"
conclure
} 2>&1 | tee "$R"
```

- **Appels au distant permis au lecteur-opérateur, en lecture seule, et eux seuls** (second complément, point 4 ; la conductrice l'écrit aussi dans son mandat) : la récupération des trois branches nommées ci-dessus (`git fetch origin <branche>`), la lecture des têtes du distant (`git ls-remote --heads origin`), ici et au § 4.2. Ils n'écrivent rien sur le distant. Aucun autre appel à un service extérieur.
- Une branche du distant absente localement, ou dont la tête locale n'est pas celle du distant : la garde chercherait le premier ajout du fichier de lecture de l'étape B sur une histoire incomplète sans le savoir (`lecture_v5.py`, l. 862-871, `git log --all`). On ne lance pas ; la conductrice fait récupérer la branche.
- Place : l'arbre de lecture pèse environ 3,5 Go. Moins de 6 Go libres : on ne monte pas, rendu à la conductrice.

### 1.2 Arbre de lecture monté, entrées extraites par chemins nommés

Arbre de travail séparé du dépôt à histoire complète (complément du mandat, point 2 ; montage admis par la session mère). Un clone local ne convient pas : il perdrait les branches de suivi que la garde parcourt.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
grep -q "CONCLUSION : conforme" "$T/releve-mise-en-place.txt" || { echo "§ 1.1 non conforme : arrêt"; exit 1; }
neuf "$ARBRE"
cd "$DEPOT" && git worktree add -q -b lecture/bbis-arbre-de-lecture-v1 "$ARBRE" "$TETE_TRAVAIL" || { echo "montage refusé : arrêt"; exit 1; }
cd "$ARBRE" || exit 1
git checkout "$REF_SORTIES" -- "runs/$RUN_BBIS" "diag/$RUN_BBIS" "donnees/$RUN_BBIS" || { echo "extraction des sorties : arrêt"; exit 1; }
for p in "runs/$RUN_7B/manifeste.json" "diag/$RUN_7B/episodes-t06.json" "diag/$RUN_7B/lecture-cout-t06.json" \
         "donnees/$RUN_7B/mesures-t06.npz" "donnees/$RUN_7B/textes-actions-t06.jsonl"; do
  git checkout "$REF_7B" -- "$p" "$p.sha256" || { echo "extraction de $p : arrêt"; exit 1; }
done
p="diag/$RUN_MC/issue-mots-et-cout-t06.json"
git checkout "$REF_MC" -- "$p" "$p.sha256" || { echo "extraction de $p : arrêt"; exit 1; }
echo "ARBRE DE LECTURE MONTE : $ARBRE"
```

- `git checkout <branche> -- <chemin>` pose le fichier sur le disque et dans l'index sans l'afficher. Aucun dossier de la course de confirmation n'est extrait en entier.
- Un arrêt ici : l'opérateur ne retire rien, ne recommence pas, rend la ligne d'arrêt.

### 1.3 Entrées présentes, à l'empreinte des branches et des lignes de registre ; rien de la liste « Jamais »

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
R="$T/releve-entrees.txt"; neuf "$R"
{
cd "$ARBRE" || exit 1
dire "== 1.3 entrées, $(date -u +%Y-%m-%dT%H:%M:%SZ)"
: > "$T/attendus.txt"
git ls-tree -r --name-only "$REF_SORTIES" -- "runs/$RUN_BBIS" "diag/$RUN_BBIS" "donnees/$RUN_BBIS" | while read -r p; do printf '%s\t%s\n' "$REF_SORTIES" "$p"; done >> "$T/attendus.txt"
egal "fichiers des sorties listés sur la branche" 20 "$(wc -l < "$T/attendus.txt" | tr -d ' ')"
for p in "runs/$RUN_7B/manifeste.json" "diag/$RUN_7B/episodes-t06.json" "diag/$RUN_7B/lecture-cout-t06.json" \
         "donnees/$RUN_7B/mesures-t06.npz" "donnees/$RUN_7B/textes-actions-t06.jsonl"; do
  printf '%s\t%s\n%s\t%s\n' "$REF_7B" "$p" "$REF_7B" "$p.sha256" >> "$T/attendus.txt"
done
p="diag/$RUN_MC/issue-mots-et-cout-t06.json"; printf '%s\t%s\n%s\t%s\n' "$REF_MC" "$p" "$REF_MC" "$p.sha256" >> "$T/attendus.txt"
egal "entrées attendues" 32 "$(wc -l < "$T/attendus.txt" | tr -d ' ')"
while IFS="$(printf '\t')" read -r ref p; do
  if [ ! -f "$p" ]; then dire "DEFAUT : $p absent de l'arbre de lecture"; FAUTES=$((FAUTES+1)); continue; fi
  egal "objet git de $p égal à celui de sa branche" "$(git rev-parse --verify -q "$ref:$p")" "$(git hash-object -- "$p")"
  case "$p" in *.sha256) ;; *) egal "compagnon de $p" "$(sha256sum "$p" | cut -d' ' -f1)" "$(cut -d' ' -f1 "$p.sha256" 2>/dev/null)" ;; esac
done < "$T/attendus.txt"
# rien d'autre dans les dossiers des entrées
find "runs/$RUN_7B" "diag/$RUN_7B" "donnees/$RUN_7B" "runs/$RUN_BBIS" "diag/$RUN_BBIS" "donnees/$RUN_BBIS" "diag/$RUN_MC" "runs/$RUN_MC" -type f 2>/dev/null | sort > "$T/presents.txt"
cut -f2 "$T/attendus.txt" | sort > "$T/attendus-noms.txt"
egal "fichiers en trop ou en moins dans les dossiers des entrées" 0 "$(comm -3 "$T/presents.txt" "$T/attendus-noms.txt" | wc -l | tr -d ' ')"
# liste « Jamais » et fichiers de l'étape B : par les noms
vrai "lecture-sondes-t06.json absent" test ! -e "diag/$RUN_7B/lecture-sondes-t06.json"
vrai "resume.json de la course de confirmation absent" test ! -e "diag/$RUN_7B/resume.json"
egal "fichiers nommés lecture-t07* ou arret-etape-b* dans l'arbre" 0 "$(find . -path ./.git -prune -o -type f \( -name 'lecture-t07*' -o -name 'arret-etape-b*' \) -print | wc -l | tr -d ' ')"
egal "fichiers du dossier de lecture de l'étape B autres que l'audit des fuites" 0 "$(find "diag/$RUN_B" -type f ! -name 'audit-fuites-t07.json*' 2>/dev/null | wc -l | tr -d ' ')"
# lignes des deux registres, à l'octet, une fois chacune
while IFS= read -r l; do egal "registre propre : une fois « $(printf '%s' "$l" | cut -c1-60)… »" 1 "$(grep -c -x -F -- "$l" "$PROPRE")"; done <<'EOF'
| SCELLEMENT-BBIS | 2026-11-14T12:30:30Z | prereg/T0.7-etape-B-bis-v1.md | 0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb |
| ABSENCE-B-BBIS | 2026-11-14T12:30:30Z | registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json | 134ac847b89b7fb7beb3ccfb1d93aca6527a51107da2605da5ec504e426d9cfc |
| CODE-BBIS | 2026-11-16T12:57:27Z | registres/t07-etape-b-bis/code-bbis-v1.json | ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469 |
| CODE-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/code-bbis-v2.json | 4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb |
| GO-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/go-bbis-v2.txt | 33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 |
| SCORES-BBIS | 2026-11-18T19:43:48Z | diag/20261118-154143-bbis-t07-v1/sondes-bbis.json | 645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62 |
EOF
egal "registre propre : lignes de clé de l'étape B bis" 6 "$(grep -c -E '^\| [A-Z0-9-]+-BBIS \|' "$PROPRE")"
egal "registre propre : lignes de lecture, de verdict ou de table conjointe" 0 "$(grep -c -E '^\| (LECTURE|VERDICT|CONJOINTE)-BBIS \|' "$PROPRE")"
while IFS= read -r l; do egal "registre partagé : une fois « $(printf '%s' "$l" | cut -c1-60)… »" 1 "$(grep -c -x -F -- "$l" "$PARTAGE")"; done <<'EOF'
| RUN-CONFIRMATION-T06 | 2026-11-13T18:52:43Z | runs/20261111-151701-t06-reel/manifeste.json | 7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 |
| VERDICT-P3BIS | 2026-11-14T10:30:38Z | docs/verdicts/verdict-P3-bis-v1-issue.json | c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0 |
| CODE-MOTS-ET-COUT-T06 | 2026-11-14T14:55:41Z | registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json | e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b |
| AUDIT-FUITES-T07 | 2026-11-14T14:57:54Z | diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json | 5c76b7ff48964abe9ec552552d57c32e0b9d9ec4519a61206f7fdac349fce094 |
| ISSUE-MOTS-ET-COUT-T06 | 2026-11-16T21:02:42Z | diag/20261116-205721-mots-et-cout-t06/issue-mots-et-cout-t06.json | 1b84d7c4440638699ac14711365fb865c1f5c57b50c39f44259a61b2aca53657 |
EOF
for k in RUN-CONFIRMATION-T06 VERDICT-P3BIS CODE-MOTS-ET-COUT-T06 AUDIT-FUITES-T07 ISSUE-MOTS-ET-COUT-T06; do
  egal "registre partagé : une seule ligne $k" 1 "$(grep -c "^| $k |" "$PARTAGE")"
done
egal "registre partagé : clés de l'étape B bis" 0 "$(grep -c -E '^\| *[A-Z0-9-]*-BBIS *\|' "$PARTAGE")"
# fichiers cités par les lignes : présents, à l'empreinte de la ligne, compagnon présent et égal
while read -r s p; do
  if [ ! -f "$p" ] || [ ! -f "$p.sha256" ]; then dire "DEFAUT : $p ou son compagnon absent"; FAUTES=$((FAUTES+1)); continue; fi
  egal "empreinte de $p égale à sa ligne de registre" "$s" "$(sha256sum "$p" | cut -d' ' -f1)"
  egal "compagnon de $p égal à sa ligne de registre" "$s" "$(cut -d' ' -f1 "$p.sha256")"
done <<'EOF'
0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb prereg/T0.7-etape-B-bis-v1.md
134ac847b89b7fb7beb3ccfb1d93aca6527a51107da2605da5ec504e426d9cfc registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json
4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb registres/t07-etape-b-bis/code-bbis-v2.json
33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 registres/t07-etape-b-bis/go-bbis-v2.txt
645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62 diag/20261118-154143-bbis-t07-v1/sondes-bbis.json
7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6 runs/20261111-151701-t06-reel/manifeste.json
c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0 docs/verdicts/verdict-P3-bis-v1-issue.json
e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json
5c76b7ff48964abe9ec552552d57c32e0b9d9ec4519a61206f7fdac349fce094 diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json
1b84d7c4440638699ac14711365fb865c1f5c57b50c39f44259a61b2aca53657 diag/20261116-205721-mots-et-cout-t06/issue-mots-et-cout-t06.json
EOF
conclure
} 2>&1 | tee "$R"
```

- Les empreintes sont calculées sur le fichier entier ; aucun contenu n'est décodé ni affiché.
- Pourquoi ce contrôle : un fichier cité absent donnerait un refus de mise en place (code 3) ; un fichier de scores absent serait écrit « non calculable » sans arrêt (quatrième addendum, § 6.5, point 7) ; une empreinte autre donnerait un refus de fond, qui consomme la lecture.

### 1.4 Module, textes scellés, fiches, registre voisin

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
R="$T/releve-code-et-textes.txt"; neuf "$R"
{
cd "$ARBRE" || exit 1
dire "== 1.4 module, textes, fiches, registre voisin, $(date -u +%Y-%m-%dT%H:%M:%SZ)"
while read -r s p; do
  egal "empreinte entière de $p" "$s" "$(sha256sum "$p" 2>/dev/null | cut -d' ' -f1)"
done <<'EOF'
dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c src/controle_ia/t07bbis/lecture_v5.py
cd14195d396a779da954619c9a3405741fe11e2f98bf4aae3767cb87a5036ca0 registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json
0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb prereg/T0.7-etape-B-bis-v1.md
f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7 prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md
18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26 prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md
e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872 prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md
5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4 prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md
12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419 prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md
4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb registres/t07-etape-b-bis/code-bbis-v2.json
ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469 registres/t07-etape-b-bis/code-bbis-v1.json
0a627df9ecb82c518d06c0c7ca8df4afab48a5a0da34b785c31c0da4ab41a29c src/controle_ia/t06/test_croise.py
6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e src/controle_ia/sondes/familles.py
1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3 src/controle_ia/sondes/evaluation.py
9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674 scripts/mots_et_cout_t06_v3.py
bcfe56832a1bf0c9af78b94232aedb44f179446a3871f45c27f1e3348efa7173 src/controle_ia/t06/cout.py
a3dde5509712a7a2fe072dbdec7be616d8bc9190fa1a57e649f90bfce9f05bc3 src/controle_ia/t06/lanceur.py
43a244315573eac5cc07cf90089f057ce94878851c01085e0ad64b7ef782849c src/controle_ia/harnais/run_harnais_factice.py
5d97b223206c6378295946a769c378ccfe0bd6a12372d3b25bcecb5240ab31ae src/controle_ia/environnements/propositions.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d src/controle_ia/manifeste.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2 src/controle_ia/scellement.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439 src/controle_ia/gardes.py
EOF
egal "la fiche de rattachement nomme le module à cette empreinte" 1 "$(grep -c 'dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c' registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json)"
for k in ADDENDUM-ECART-1-BBIS ADDENDUM-ECART-2-BBIS ADDENDUM-ECART-3-BBIS ADDENDUM-ECART-4-BBIS ADDENDUM-ECART-4-COMPLEMENT-BBIS RATTACHEMENT-LECTURE-V5-BBIS; do
  egal "registre voisin : ligne $k, une fois" 1 "$(grep -c "^| $k |" "$VOISIN")"
  egal "registre voisin au commit de main : ligne $k, une fois" 1 "$(git show "$MAIN_INSCRIPTIONS:$VOISIN" | grep -c "^| $k |")"
done
egal "ligne du quatrième addendum à son empreinte" 1 "$(grep -c '^| ADDENDUM-ECART-4-BBIS | .*| prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md | 5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4 |' "$VOISIN")"
egal "ligne du complément à son empreinte" 1 "$(grep -c '^| ADDENDUM-ECART-4-COMPLEMENT-BBIS | .*| prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md | 12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419 |' "$VOISIN")"
egal "ligne de rattachement à l'empreinte de la fiche" 1 "$(grep -c '^| RATTACHEMENT-LECTURE-V5-BBIS | .*| registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json | cd14195d396a779da954619c9a3405741fe11e2f98bf4aae3767cb87a5036ca0 |' "$VOISIN")"
# les 63 fichiers de la fiche de code, par programme (la fiche est un fichier de code, non de résultat)
egal "fichiers de la fiche de code d'empreinte autre, ou absents" "63 0" "$("$PY" -c '
import hashlib, json, pathlib
f = json.load(open("registres/t07-etape-b-bis/code-bbis-v2.json"))["fichiers"]
print(len(f), sum(1 for p, s in f.items() if not pathlib.Path(p).is_file() or hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest() != s))')"
egal "fichiers sous src ou pièce « mots et coût » modifiés ou retirés depuis le commit de la fiche" 0 "$(git diff --name-status "$C_FICHE" HEAD -- src scripts/mots_et_cout_t06_v3.py | grep -c -v '^A')"
for v in numpy==2.4.6 scipy==1.17.1 torch==2.14.1; do egal "version figée $v dans requirements-cpu.txt" 1 "$(grep -c -x "$v" requirements-cpu.txt)"; done
conclure
} 2>&1 | tee "$R"
```

- Un seul écart d'empreinte du module, d'un texte ou de la fiche, ou une ligne du registre voisin absente ou en double : on ne lance pas (quatrième addendum, § 6.3, tel que CQ-6 le fait lire : « un seul écart : arrêt, rien n'est lancé »).
- Le module ne vérifie pas sa propre empreinte : ce contrôle est celui-ci (quatrième addendum, § 4, point 7).

## 2. Preuve d'antériorité et preuve d'entrée conjointe, relevées à part

Ce que le plan, point 2, les addenda et le feu, § 12, demandent, par les noms et les commits seulement, dans l'arbre où la lecture se jouera, avec git dans l'environnement nettoyé du § 4 :

- (A) histoire complète ; tête de l'arbre qui descend du commit de la course et contient le commit de `main` qui porte les inscriptions ;
- (B) antériorité du scellement sur l'étape B : le premier commit, toutes références, qui ajoute `lecture-t07.json` ou `arret-etape-b.json`, s'il existe, a une date de commit strictement postérieure à celle du commit qui ajoute la ligne `SCELLEMENT-BBIS`. Ce sont les recherches mêmes de la garde (`lecture_v5.py`, l. 854-877), écrites ici en commandes ; le module n'est pas importé ;
- (C) ordre des lignes du registre propre : chaque couple de la chaîne en dates écrites strictement croissantes, hors le seul couple de l'accord de calcul et de la fiche remplaçante, égal à la seconde, que le quatrième addendum (QA-1) fait lire par la preuve d'entrée conjointe ;
- (D) preuve d'entrée conjointe, points (P1) à (P5) de QA-1 (quatrième addendum, § 6.4 : relevée par les seules commandes git en lecture de QA-1, écrite dans la même pièce scellée, avant de lancer le module) ;
- (E) ce que les addenda ajoutent : chaque ligne d'addendum ajoutée par un commit ancêtre de la tête ; les trois premières par un commit ancêtre du commit de la course ; la tête des sorties antérieure à la ligne `SCORES-BBIS`.

Pièce : `registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt`, texte, une ligne par constat (`CONFORME` ou `DEFAUT`, avec les identifiants relevés), scellée par son compagnon. Écrite dans l'arbre principal, hors de l'arbre de lecture, pour que celui-ci reste propre.

**Ce qui vaut « on ne lance pas »** : une seule ligne `DEFAUT`. Un défaut de (A) est de mise en place : la conductrice fait corriger l'arbre, puis une pièce `-v2`. Un défaut de (B), (C), (D) ou (E) est un nœud : il annonce un refus de fond de la garde, qui consommerait la lecture ; rien n'est lancé, la conductrice le porte à la mère.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
for f in releve-mise-en-place releve-entrees releve-code-et-textes; do grep -q "CONCLUSION : conforme" "$T/$f.txt" || { echo "$f non conforme : arrêt"; exit 1; }; done
P="$LV1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt"; neuf "$P"
sha() { sha256sum | cut -d' ' -f1; }
ct() { G show -s --format=%ct "$1"; }
cd "$ARBRE" || exit 1
{
dire "Preuve d'antériorité et preuve d'entrée conjointe — lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7)"
dire "relevée le $(date -u +%Y-%m-%dT%H:%M:%SZ), dans $ARBRE, par commandes git en lecture, environnement sans variable GIT_ ; aucun fichier de résultat ouvert ; le module de lecture n'est pas importé"
dire "== (A) histoire et tête"
egal "dépôt non superficiel" false "$(G rev-parse --is-shallow-repository)"
TETE="$(G rev-parse HEAD)"; dire "tête de l'arbre de lecture : $TETE"
vrai "le commit de la course $COURSE est un ancêtre de la tête" G merge-base --is-ancestor "$COURSE" "$TETE"
vrai "le commit de main $MAIN_INSCRIPTIONS est un ancêtre de la tête" G merge-base --is-ancestor "$MAIN_INSCRIPTIONS" "$TETE"
dire "== (B) antériorité du scellement sur l'étape B"
set -- $(G log --all --reverse --format='%H %ct' -S '| SCELLEMENT-BBIS |' -- "$PROPRE" | head -n 1); CS="${1:-}"; TS="${2:-}"
dire "commit qui ajoute SCELLEMENT-BBIS : $CS (instant $TS)"
egal "ce commit est celui que le quatrième addendum relève" f72d283347534d761fff63f6d744415cdf1bf32c "$CS"
for motif in '*lecture-t07.json' '*arret-etape-b.json'; do
  set -- $(G log --all --reverse --diff-filter=A --format='%H %ct' -- "$motif" | head -n 1); C1="${1:-}"; T1="${2:-}"
  if [ -z "$C1" ]; then dire "CONFORME : aucun commit n'ajoute $motif"
  elif [ -n "$TS" ] && [ "$T1" -gt "$TS" ]; then dire "CONFORME : premier ajout de $motif par $C1 (instant $T1), strictement postérieur au scellement"
  else dire "DEFAUT : premier ajout de $motif par $C1 (instant $T1), non postérieur au scellement"; FAUTES=$((FAUTES+1)); fi
done
dire "== (C) ordre des lignes du registre propre (dates écrites)"
date_de() { grep -F -- "$1" "$PROPRE" | cut -d'|' -f3 | tr -d ' '; }
D_SC="$(date_de '| SCELLEMENT-BBIS |')"; D_C1="$(date_de 'code-bbis-v1.json')"; D_GO="$(date_de '| GO-BBIS |')"
D_C2="$(date_de 'code-bbis-v2.json')"; D_SO="$(date_de '| SCORES-BBIS |')"
dire "dates écrites : scellement $D_SC ; première fiche $D_C1 ; accord de calcul $D_GO ; fiche remplaçante $D_C2 ; scores $D_SO"
avant() { if [ -n "$2" ] && [ -n "$3" ] && [ "$2" \< "$3" ]; then dire "CONFORME : $1"; else dire "DEFAUT : $1"; FAUTES=$((FAUTES+1)); fi; }
avant "scellement strictement avant la première fiche" "$D_SC" "$D_C1"
avant "première fiche strictement avant l'accord de calcul" "$D_C1" "$D_GO"
egal "accord de calcul et fiche remplaçante à la même seconde (seul couple de l'exception de QA-1)" "$D_GO" "$D_C2"
avant "fiche remplaçante strictement avant les scores" "$D_C2" "$D_SO"
avant "première fiche strictement avant la fiche remplaçante" "$D_C1" "$D_C2"
dire "== (D) preuve d'entrée conjointe (quatrième addendum, QA-1)"
L_CODE='| CODE-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/code-bbis-v2.json | 4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb |'
L_GO='| GO-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/go-bbis-v2.txt | 33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 |'
L_PREM='| CODE-BBIS | 2026-11-16T12:57:27Z | registres/t07-etape-b-bis/code-bbis-v1.json | ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469 |'
vrai "(P1) le commit de l'entrée conjointe $C_CONJ existe" G cat-file -e "$C_CONJ^{commit}"
set -- $(G rev-list --parents -n 1 "$C_CONJ"); egal "(P1) il a un seul parent" 2 "$#"; PAR="${2:-}"; dire "son parent : $PAR"
egal "(P2) au commit, la ligne de la fiche remplaçante, une fois, à l'octet" 1 "$(G show "$C_CONJ:$PROPRE" | grep -c -x -F -- "$L_CODE")"
egal "(P2) au commit, la ligne de l'accord de calcul, une fois, à l'octet" 1 "$(G show "$C_CONJ:$PROPRE" | grep -c -x -F -- "$L_GO")"
vrai "(P2) le registre propre existe au parent" G cat-file -e "$PAR:$PROPRE"
egal "(P2) au parent, lignes de clé CODE-BBIS ou GO-BBIS" 0 "$(G show "$PAR:$PROPRE" | grep -c -E '^\| *(CODE-BBIS|GO-BBIS) *\|')"
egal "(P3) au parent, le fichier de l'accord est présent" 1 "$(G ls-tree --full-tree "$PAR" -- registres/t07-etape-b-bis/go-bbis-v2.txt | wc -l | tr -d ' ')"
egal "(P3) au parent, son contenu a l'empreinte de la ligne" 33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 "$(G show "$PAR:registres/t07-etape-b-bis/go-bbis-v2.txt" | sha)"
egal "(P3) au parent, la fiche remplaçante est absente" 0 "$(G ls-tree --full-tree "$PAR" -- registres/t07-etape-b-bis/code-bbis-v2.json | wc -l | tr -d ' ')"
egal "(P3) au commit, la fiche remplaçante a l'empreinte de la ligne" 4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb "$(G show "$C_CONJ:registres/t07-etape-b-bis/code-bbis-v2.json" | sha)"
vrai "(P4) le commit de la remise de la première fiche $C_REMISE existe" G cat-file -e "$C_REMISE^{commit}"
set -- $(G rev-list --parents -n 1 "$C_REMISE"); egal "(P4) il a un seul parent" 2 "$#"; PAR2="${2:-}"; dire "son parent : $PAR2"
vrai "(P4) le commit de l'entrée conjointe en est un ancêtre" G merge-base --is-ancestor "$C_CONJ" "$C_REMISE"
egal "(P4) au commit, la ligne de la première fiche, une fois, à l'octet" 1 "$(G show "$C_REMISE:$PROPRE" | grep -c -x -F -- "$L_PREM")"
egal "(P4) à son parent, lignes qui citent la première fiche" 0 "$(G show "$PAR2:$PROPRE" | grep -c -F 'registres/t07-etape-b-bis/code-bbis-v1.json')"
vrai "(P5) le commit de la remise est un ancêtre du commit de la course" G merge-base --is-ancestor "$C_REMISE" "$COURSE"
vrai "(P5) le commit de la course est un ancêtre de la tête de l'arbre de lecture" G merge-base --is-ancestor "$COURSE" "$TETE"
dire "== (E) addenda, course, scores"
for k in ADDENDUM-ECART-1-BBIS ADDENDUM-ECART-2-BBIS ADDENDUM-ECART-3-BBIS ADDENDUM-ECART-4-BBIS ADDENDUM-ECART-4-COMPLEMENT-BBIS RATTACHEMENT-LECTURE-V5-BBIS; do
  set -- $(G log --all --reverse --format='%H %ct' -S "| $k |" -- "$VOISIN" | head -n 1); CA="${1:-}"
  dire "premier commit qui ajoute la ligne $k : $CA"
  vrai "ce commit est un ancêtre de la tête de l'arbre de lecture" G merge-base --is-ancestor "$CA" "$TETE"
  case "$k" in ADDENDUM-ECART-[123]-BBIS) vrai "ce commit est un ancêtre du commit de la course" G merge-base --is-ancestor "$CA" "$COURSE" ;; esac
done
egal "tête de la branche des sorties" "$TETE_SORTIES" "$(G rev-parse --verify -q "$REF_SORTIES")"
egal "le commit de la course est l'ancêtre commun des sorties et de la tête" "$COURSE" "$(G merge-base "$REF_SORTIES" "$TETE")"
vrai "le commit de la fiche de code est un ancêtre du commit de la course" G merge-base --is-ancestor "$C_FICHE" "$COURSE"
T_SO="$(date -u -d "$D_SO" +%s 2>/dev/null)"; T_TS="$(ct "$REF_SORTIES")"
if [ -n "$T_SO" ] && [ -n "$T_TS" ] && [ "$T_TS" -le "$T_SO" ]; then dire "CONFORME : la tête des sorties (instant $T_TS) précède la ligne SCORES-BBIS (instant $T_SO)"; else dire "DEFAUT : tête des sorties (instant $T_TS) et ligne SCORES-BBIS (instant $T_SO)"; FAUTES=$((FAUTES+1)); fi
egal "registre propre : lignes de lecture, de verdict ou de table conjointe" 0 "$(grep -c -E '^\| (LECTURE|VERDICT|CONJOINTE)-BBIS \|' "$PROPRE")"
conclure
} > "$P" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt"
grep -c '^CONFORME' "$P"; grep '^DEFAUT' "$P"; tail -n 2 "$P"; sha256sum "$P"
```

- Le bloc entre dans l'arbre de lecture (`cd "$ARBRE"`) : ses lectures de dates et ses comptes portent sur les registres de cet arbre ; la pièce est écrite dans l'arbre principal.
- Les faits attendus sont ceux du quatrième addendum, § 2.0 (F4 à F8), relevés à la source par son rédacteur et par son contre-lecteur.
- Ce relevé ne remplace pas la garde, que le module rejoue entière (quatrième addendum, § 6.4).

## 3. Journal du registre propre

- **Créé par la conductrice** à l'étape 0, avec sa seule ligne d'en-tête, commité sur la branche de travail avant le montage : il est donc dans l'arbre de lecture, suivi par git, sans aucune ligne d'ouverture. C'est l'état que le texte demande (texte scellé, l. 222 ; feu, § 12 ; quatrième addendum, § 6.5, point 8 ; complément, point (O3)).
- **Aucune fonction du code ne le crée à vide.** `registre_bbis_v1.journaliser_ouverture` (l. 113-119) y ajoute une ligne `| OUVERTURE-BBIS | date | lecture B bis (<run>) | empreinte du fichier de lecture |` ; `main` l'appelle une seule fois, après l'écriture du fichier de lecture (`lecture_v5.py`, l. 1708), et jamais sur une issue « non consommée ».
- L'opérateur ne l'écrit pas. Il relève son état au § 4.

## 4. Avant le lancement : arbre propre, environnement, git, versions

La garde d'ouverture n'a pas de commande à part : elle est le premier bloc de `lire` (`lecture_v5.py`, l. 1469-1503). Ce paragraphe écarte seulement ce qui ferait arrêter le programme **avant** sa garde, sans rien écrire : c'est l'état « arrêt avant le seuil », dont la conduite est au § 5.5.

### 4.1 Entrées commitées localement dans l'arbre de lecture

**Qui commite : le lecteur-opérateur, localement, sur la branche `lecture/bbis-arbre-de-lecture-v1` de l'arbre de lecture ; jamais sur `main` ni sur la branche de travail** (complément du mandat, point 2). Il ne pousse pas : la conductrice pousse cette branche sous un nom de la sienne (ci-dessous). Le manifeste de la lecture refuse un arbre non propre (`manifeste.py`, l. 81-83), et ce contrôle vient après le calcul.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
grep -q "CONCLUSION : conforme" "$LV1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt" || { echo "preuve non conforme : arrêt"; exit 1; }
cd "$ARBRE" || exit 1
git -c user.name="lecteur-operateur" -c user.email="lecteur-operateur@example.invalid" -c commit.gpgsign=false \
  commit -q -m "Étape B bis, lecture : entrées de la liste blanche, commit local de l'arbre de lecture" || { echo "commit local refusé : arrêt"; exit 1; }
git rev-parse HEAD
```

**Fin du premier temps.** L'opérateur rend cette tête à la conductrice et s'arrête.

**Gestes de la conductrice entre les deux temps, avant tout lancement.** D'abord, **décision d'organisation de la conductrice** (constat m6 de la contre-lecture de la version 2) : elle commite et pousse sur la branche de travail la pièce de la preuve d'antériorité et de la preuve d'entrée conjointe, avec son compagnon, pour que la preuve soit inscrite à part avant la lecture (feu, § 12). Ce commit ne touche pas l'arbre de lecture, dont le parent reste `TETE_TRAVAIL`. Ensuite (second complément, point 7) : elle pousse la branche locale de l'arbre de lecture sous un nom de sa branche, jamais `main`, pour que le manifeste de la lecture cite un commit joignable sur le distant :

```bash
cd /home/user/controle-ia-travail
P=registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt
git add -- "$P" "$P.sha256" && git commit -q -m "Étape B bis, lecture : preuve d'antériorité et preuve d'entrée conjointe, inscrites à part avant la lecture" && git push origin claude/lecture-verdict-etape-b-bis-v1
git push origin lecture/bbis-arbre-de-lecture-v1:refs/heads/claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
git ls-remote --heads origin claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture     # attendu : la tête rendue par l'opérateur
```

- Cette branche porte les 32 fichiers d'entrée, déjà présents sur le distant sous leurs branches d'origine ; elle n'est jamais fusionnée dans la branche de travail ni dans `main`.
- Le § 4.2 vérifie, avant le lancement, que la tête de cette branche sur le distant est la tête de l'arbre de lecture ; sinon on ne lance pas.
- Une relance n'est pas jouée sur cette version (§ 5.3) ; la version écrite pour elle dira comment les commits locaux de plus sont poussés.

### 4.2 Relevé d'avant lancement

`N` est le numéro du lancement (1). Le nom du run de lecture est fixé ici, une fois : `<AAAAMMJJ-HHMMSS>-bbis-t07-lecture-v1` (forme exigée par `manifeste.py`, l. 26).

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1
R="$T/releve-avant-lancement-$N.txt"; neuf "$R"; neuf "$T/run-lecture-$N.txt"
RUNL="$(date -u +%Y%m%d-%H%M%S)-bbis-t07-lecture-v1"; printf '%s\n' "$RUNL" > "$T/run-lecture-$N.txt"
{
cd "$ARBRE" || exit 1
dire "== 4.2 avant le lancement n° $N, $(date -u +%Y-%m-%dT%H:%M:%SZ) ; run de lecture $RUNL"
dire "-- arbre de lecture"
egal "parent de la tête de l'arbre de lecture" "$TETE_TRAVAIL" "$(git rev-parse HEAD^1)"
egal "fichiers ajoutés par le commit local" 32 "$(git diff --name-status HEAD^1 HEAD | grep -c '^A')"
egal "fichiers changés ou retirés par le commit local" 0 "$(git diff --name-status HEAD^1 HEAD | grep -c -v '^A')"
git diff --name-only HEAD^1 HEAD | sort > "$T/commit-local-noms.txt"
egal "le commit local ajoute les entrées attendues, et elles seules" 0 "$(comm -3 "$T/commit-local-noms.txt" "$T/attendus-noms.txt" | wc -l | tr -d ' ')"
dire "tête de l'arbre de lecture : $(git rev-parse HEAD)"
vrai "aucun dossier de ce run de lecture" test ! -e "runs/$RUNL" -a ! -e "diag/$RUNL"
dire "-- journal du registre propre"
vrai "journal suivi par git" git ls-files --error-unmatch -- "$JOURNAL"
egal "journal : nombre de lignes" 1 "$(wc -l < "$JOURNAL" | tr -d ' ')"
egal "journal : lignes d'ouverture" 0 "$(grep -c 'OUVERTURE-BBIS' "$JOURNAL")"
dire "-- environnement"
dire "variables GIT_ de la session, noms seulement : $(env | cut -d= -f1 | grep '^GIT_' | sort | tr '\n' ' ')"
set -- $("${NETTOYE[@]}" "$PY" -c 'import os; r = sorted(k for k in os.environ if k.startswith("GIT_")); print(len(r), *r)')
egal "variables GIT_ restantes dans l'environnement nettoyé" 0 "${1:-illisible}"
[ "$#" -gt 1 ] && { shift; dire "noms restants (jamais leurs valeurs) : $*"; }
egal "variable BBIS_INSTANCE dans l'environnement nettoyé" absente "$("${NETTOYE[@]}" "$PY" -c 'import os; print("posée" if os.environ.get("BBIS_INSTANCE") else "absente")')"
dire "-- git répond dans l'environnement nettoyé (commandes neutres, en lecture)"
egal "tête lue par git nettoyé" "$(git rev-parse HEAD)" "$(G rev-parse HEAD 2>/dev/null)"
egal "dépôt non superficiel, lu par git nettoyé" false "$(G rev-parse --is-shallow-repository 2>/dev/null)"
egal "arbre de lecture propre, lu par git nettoyé (lignes de statut)" 0 "$(G status --porcelain --untracked-files=all 2>/dev/null | wc -l | tr -d ' ')"
vrai "git nettoyé rend le statut sans erreur" G status --porcelain --untracked-files=all
dire "-- base « mots et coût » : code de la pièce au commit cité"
vrai "commit cité par la ligne CODE-MOTS-ET-COUT-T06 présent" G cat-file -e "$C_PIECE^{commit}"
egal "pièce sur le disque égale à la pièce au commit cité" "$(G rev-parse --verify -q "$C_PIECE:scripts/mots_et_cout_t06_v3.py")" "$(git hash-object -- scripts/mots_et_cout_t06_v3.py)"
dire "-- contrôles que l'écriture du résultat rejouerait après le seuil, faits ici sur des fichiers hors données"
egal "nom du run de lecture à la forme exigée par le manifeste" oui "$(printf '%s' "$RUNL" | grep -q -E '^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$' && echo oui || echo non)"
vrai "dossiers runs et diag de l'arbre de lecture ouverts à l'écriture" test -d runs -a -w runs -a -d diag -a -w diag
vrai "aucun fichier de lecture ni compagnon à ce nom de run" test ! -e "diag/$RUNL/lecture-bbis.json" -a ! -e "diag/$RUNL/lecture-bbis.json.sha256"
egal "préenregistrement scellé conforme pour un manifeste décisif (prereg.exiger_prereg_scelle, sur le texte seul)" 0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$ARBRE/src" "$PY" -c 'import sys; from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle(sys.argv[1]))' "$ARBRE/prereg/T0.7-etape-B-bis-v1.md" 2>&1 | tail -n 1)"
egal "fiche de code lisible, niveau décisif admis, entropie de plus de 64 bits (registre_bbis_v1.lire_fiche_code, commun_v1.exiger_entropie)" conforme "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$ARBRE/src" "$PY" -c 'import sys; from controle_ia.t07bbis.registre_bbis_v1 import lire_fiche_code; from controle_ia.t07bbis.commun_v1 import exiger_entropie; f = lire_fiche_code(sys.argv[1]); exiger_entropie(int(f["entropie"]), reelle=True); print("conforme")' "$ARBRE/registres/t07-etape-b-bis/code-bbis-v2.json" 2>&1 | tail -n 1)"
dire "-- branche de l'arbre de lecture sur le distant (poussée par la conductrice), utilitaires du lancement"
egal "tête, sur le distant, de la branche de l'arbre de lecture" "$(git rev-parse HEAD)" "$(git ls-remote --heads origin "$BRANCHE_DISTANTE_ARBRE" 2>/dev/null | awk '{print $1}')"
vrai "utilitaire de détachement (nouvelle session de processus) présent" command -v setsid
vrai "utilitaire d'insensibilité à la fermeture du terminal présent" command -v nohup
vrai "utilitaire de relevé de l'état d'un processus présent" command -v ps
dire "-- versions (fils de calcul fixés à 1 par la ligne de lancement)"
egal "versions de numpy, scipy, torch" "2.4.6 1.17.1 2.14.1" "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 "$PY" -c 'import numpy, scipy, torch; print(numpy.__version__, scipy.__version__, torch.__version__.split("+")[0])' 2>/dev/null)"
dire "python : $("$PY" -c 'import platform; print(platform.python_version())')"
dire "place libre : $(df -h "$T" | tail -1 | awk '{print $4}')"
conclure
} 2>&1 | tee "$R"
cp -n "$R" "$LV1/releve-avant-lancement-lecture-bbis-$N-v1.txt" && sceller "registres/t07-etape-b-bis/lecture-v1/releve-avant-lancement-lecture-bbis-$N-v1.txt"
```

- **Contrôles d'après le seuil ramenés avant le lancement** (second complément, point 1). L'écriture du résultat crée un manifeste décisif après tout le calcul (`lecture_v5.ecrire_lecture`, l. 1635-1648 ; `manifeste.creer_manifeste`, l. 68-116) : un échec y consommerait la lecture. Par lecture de ces deux fonctions, ce qu'elles contrôlent sur des fichiers hors données, et où la commande le fait avant :
  - la forme du nom du run (`manifeste.py`, l. 26 et 74) et l'absence de son dossier (l. 76-77) : ici ;
  - l'arbre propre (l. 78-83) : ici, par git dans l'environnement nettoyé ;
  - **le préenregistrement scellé** (l. 85-96, `prereg.exiger_prereg_scelle`) : compagnon égal, huit sections exigées présentes et non vides, aucun marqueur « À REMPLIR », aucun marqueur de gabarit, deux empreintes par entrée de la section « Contre-lecture » (`prereg.py`, l. 37-76). La commande appelle **cette fonction du dépôt**, sur le texte scellé de l'arbre de lecture et sur lui seul. Elle n'est ni le module de lecture ni sa garde, n'ouvre aucune donnée et ne lance aucune commande git ;
  - l'entropie des graines (`manifeste.graines`, l. 37-49) et la fiche de code que `main` relit pour la trouver (`lecture_v5.py`, l. 1693-1695) : la commande appelle `registre_bbis_v1.lire_fiche_code` et `commun_v1.exiger_entropie` sur la fiche de code, qui n'est pas un fichier de résultat ; ce ne sont ni le module de lecture ni sa garde ;
  - l'écriture du dossier du run (l. 110-114) et du fichier de lecture (`manifeste.ecrire_resultat`, l. 128-139) : dossiers `runs` et `diag` ouverts à l'écriture, aucun fichier à ce nom ;
  - les versions des bibliothèques (`manifeste.versions`, l. 58-65) sont seulement consignées : elles ne peuvent pas refuser.
  Le module gelé de la partition des plis, que `lire` compare après le seuil (`adversaires_texte_v1.exiger_module_gele`), est déjà comparé au § 1.4. Ce qui reste après le seuil et ne peut pas être contrôlé avant sans ouvrir une donnée : les contrôles du contenu des entrées elles-mêmes (manifeste de la course de confirmation, audit des fuites, champ du contrôle carte-processeur, effectifs).
- Un échec d'un de ces contrôles vaut « on ne lance pas ».
- **S'il reste une variable dont le nom commence par `GIT_`, on ne lance pas** : le module s'arrêterait en première instruction (`lecture_v5.py`, l. 1674-1678), sans rien écrire : état « arrêt avant le seuil » (§ 5.5). L'opérateur n'ajoute pas un `-u` de son chef : il rend les noms à la conductrice.
- Si git ne répond pas dans l'environnement nettoyé : on ne lance pas (note n10 de la contre-lecture du code).
- **Si l'utilitaire de détachement manque, on ne lance pas** : l'opérateur ne le remplace par rien et rend le relevé. Relevé par le préparateur sur cette machine, par `command -v` : il est présent (`/usr/bin/setsid`, option `-f`), ainsi que les deux autres.
- Les valeurs des variables ne sont jamais imprimées : seuls leurs noms le sont.
- Les versions figées et les fils de calcul à 1 sont exigés par le contrôle d'égalité de la base « mots et coût » (tolérance 10⁻¹², `adversaires_texte_v1.py`, l. 68 ; fils : `lien_mots_et_cout_v1.py`, l. 123-129, arrêt sinon).

## 5. Lecture

### 5.1 Ligne de lancement

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1
grep -q "CONCLUSION : conforme" "$T/releve-avant-lancement-$N.txt" || { echo "relevé d'avant lancement non conforme : ON NE LANCE PAS"; exit 1; }
RUNL="$(cat "$T/run-lecture-$N.txt")"
SORTIE="$T/sortie-lancement-$N.txt"; neuf "$SORTIE"; neuf "$T/lancement-$N.pid"; neuf "$T/lancement-$N.code"
L="$T/lancement-$N.sh"; neuf "$L"
cat > "$L" <<EOF
#!/bin/bash
# Lancement n° $N de la lecture de l'étape B bis — écrit par la commande de lecture, valeurs développées
cd "$ARBRE" || exit 1
${NETTOYE[*]} OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONPATH="$ARBRE/src" "$PY" -m controle_ia.t07bbis.lecture_v5 --racine "$ARBRE" --run-7b "$RUN_7B" --run-bbis "$RUN_BBIS" --run-lecture "$RUNL" > "$SORTIE" 2>&1 &
echo \$! > "$T/lancement-$N.pid"
wait \$!
echo \$? > "$T/lancement-$N.code"
date -u +%Y-%m-%dT%H:%M:%SZ > "$T/lancement-$N.fin"
EOF
date -u +%Y-%m-%dT%H:%M:%SZ > "$T/lancement-$N.debut"
command -v setsid > /dev/null || { echo "utilitaire de détachement absent : ON NE LANCE PAS"; exit 1; }
setsid -f nohup bash "$L" < /dev/null > /dev/null 2>&1
echo "lancement détaché ; l'identifiant du processus est relevé par le § 5.1 bis"
```

- **Module** : `controle_ia.t07bbis.lecture_v5`. **Arguments** : ceux de `main` (`lecture_v5.py`, l. 1682-1685), quatre, tous exigés ; `--adaptateur-mc` n'est pas passé : la ligne `CODE-MOTS-ET-COUT-T06` est inscrite avant l'échéance du 18 novembre à 12:00 UTC, le module charge de lui-même le code de la pièce (`adaptateur_retenu`, l. 1654-1665).
- **Environnement du module** : les onze variables retirées par `env -u`, `BBIS_INSTANCE` retirée, fils de calcul à 1, `PYTHONPATH` sur le code de l'arbre de lecture. La ligne exacte, valeurs développées, est celle du fichier `lancement-<N>.sh`, que l'opérateur copie sous `registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-<N>-v1.sh` et scelle au § 5.2. L'enveloppe (`bash`) garde l'environnement de la session ; seul le module tourne dans l'environnement nettoyé.
- **Lancement détaché de l'outil** (second complément, point 2) : l'enveloppe part dans une nouvelle session de processus (`setsid -f`), entrées et sorties coupées du terminal ; l'appel d'outil rend la main aussitôt. Le module n'est ni en arrière-plan d'un appel d'outil, ni sous un délai d'outil. L'opérateur ne lance pas ce bloc avec l'option d'arrière-plan de son outil.
- **Identifiant du processus** : celui du module de lecture, écrit par l'enveloppe dans `lancement-<N>.pid`. Le code de sortie est écrit dans `lancement-<N>.code` quand le module finit.
- **Sortie entière** (sortie et erreurs) dans `sortie-lancement-<N>.txt`. Les lignes `BBIS LECTURE ENTREES OUVERTES` et `BBIS LECTURE NON CONSOMMEE` ne vivent que là.
- **Durée** : le code ne la laisse pas estimer, et le module n'a jamais tourné sur les fichiers réels.
- **L'opérateur ne touche à rien dans l'arbre de lecture pendant la marche** : un fichier de plus rendrait l'arbre non propre au moment du manifeste, après le seuil.
- **Sorties attendues, dans l'arbre de lecture** : `runs/<run>/manifeste.json` et `diag/<run>/lecture-bbis.json`, chacun avec son compagnon, écrits et scellés par le module lui-même (`manifeste.creer_manifeste`, `manifeste.ecrire_resultat`) avant toute lecture humaine ; sur une issue « non consommée », en plus, `diag/<run>/preuve-aucune-ouverture-bbis.json` et son compagnon.

### 5.1 bis Attente, sans jamais arrêter le processus

L'opérateur relève l'état du processus par son identifiant, par des appels courts et espacés (toutes les dix minutes environ, sans attente longue dans un appel). Il n'y a aucun délai de garde.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1
PID_L="$(cat "$T/lancement-$N.pid" 2>/dev/null)"; echo "identifiant du processus du module de lecture : ${PID_L:-non écrit}"
if [ -e "$T/lancement-$N.code" ]; then echo "fini : code de sortie écrit"
elif [ -z "$PID_L" ]; then echo "identifiant non écrit : ni « vivant » ni « absent » ; deux relevés de suite ainsi : rendu à la conductrice, rien d'autre"
elif ps -p "$PID_L" -o pid=,stat=,etime=; then echo "vivant : on attend"
else echo "processus absent, code de sortie non écrit"; fi
date -u +%Y-%m-%dT%H:%M:%SZ
```

- « vivant » : l'opérateur attend, quel que soit le temps écoulé. **Une lecture lente mais vivante n'est jamais arrêtée**, ni par lui, ni sur aucun motif ; s'il doute, il écrit à la conductrice et continue d'attendre.
- « fini » : § 5.2.
- « processus absent, code de sortie non écrit » deux relevés de suite, à une minute d'écart : le processus a disparu sans finir (machine redémarrée, par exemple). § 5.2, qui le traite comme un arrêt, avant ou après le seuil selon la sortie gardée.

### 5.2 Fin du lancement : sortie gardée et scellée

À jouer quand `lancement-<N>.code` existe, ou quand le processus est absent deux relevés de suite.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1
RUNL="$(cat "$T/run-lecture-$N.txt")"; SORTIE="$T/sortie-lancement-$N.txt"
if [ -e "$T/lancement-$N.code" ]; then CODE="$(cat "$T/lancement-$N.code")"
elif [ ! -s "$T/lancement-$N.pid" ]; then echo "identifiant du processus non écrit : rendu à la conductrice, rien d'autre"; exit 1
elif ps -p "$(cat "$T/lancement-$N.pid")" > /dev/null 2>&1; then echo "le lancement n'est pas fini : on attend"; exit 1
else CODE=absent; fi
G1="$LV1/sortie-lancement-lecture-bbis-$N-v1.txt"; neuf "$G1"
cp "$SORTIE" "$G1" && sceller "registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt"
L1="$LV1/lancement-lecture-bbis-$N-v1.sh"; neuf "$L1"
cp "$T/lancement-$N.sh" "$L1" && sceller "registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-$N-v1.sh"
S_N="$(grep -c 'BBIS LECTURE ENTREES OUVERTES' "$G1" 2>/dev/null)"; NC_N="$(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1" 2>/dev/null)"
AR_N="$(grep -c '^BBIS LECTURE ARRET' "$G1")"
F="diag/$RUNL/lecture-bbis.json"; M="runs/$RUNL/manifeste.json"
R="$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt"; neuf "$R"
ecrit() { if [ -f "$ARBRE/$1" ]; then dire "$2 : $1 $(sha256sum "$ARBRE/$1" | cut -d' ' -f1) ; compagnon égal : $([ "$(cut -d' ' -f1 "$ARBRE/$1.sha256" 2>/dev/null)" = "$(sha256sum "$ARBRE/$1" | cut -d' ' -f1)" ] && echo oui || echo non)"; else dire "$2 : non écrit"; fi; }
{
dire "Relevé d'après lancement n° $N — run de lecture $RUNL"
dire "identifiant du processus $(cat "$T/lancement-$N.pid" 2>/dev/null)"
[ "$CODE" = 0 ] || dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
dire "code de sortie : $CODE"
dire "sortie gardée : registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt $(sha256sum "$G1" | cut -d' ' -f1)"
dire "lancement gardé : registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-$N-v1.sh $(sha256sum "$L1" | cut -d' ' -f1)"
if [ "$CODE" = 0 ] && [ -f "$ARBRE/$F" ]; then
  dire "ETAT : écrit"
  ecrit "$F" "fichier de lecture"; ecrit "$M" "manifeste"
elif [ "$CODE" = 3 ] && [ "$NC_N" = 1 ] && [ "$S_N" = 0 ] && [ -f "$ARBRE/$F" ]; then
  dire "ETAT : non consommée (pur défaut de mise en place, rien d'ouvert)"
  ecrit "$F" "fichier de lecture gardé"; ecrit "diag/$RUNL/preuve-aucune-ouverture-bbis.json" "pièce de preuve"; ecrit "$M" "manifeste"
elif [ "$CODE" = 0 ] || [ "$CODE" = 3 ]; then
  dire "ETAT : non prévu (code $CODE sans les fichiers ou les lignes attendus)"
elif [ ! -s "$G1.sha256" ]; then
  dire "ETAT : sortie non gardée (complément au quatrième addendum, « La suite », point 3 : lecture consommée, aucune relance ; nœud)"
elif [ "$S_N" = 0 ]; then
  dire "ETAT : arrêt avant le seuil"
  dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $S_N ; lignes « BBIS LECTURE NON CONSOMMEE » : $NC_N ; lignes « BBIS LECTURE ARRET » : $AR_N"
  ecrit "$F" "fichier de lecture"; ecrit "$M" "manifeste"
  dire "dernières lignes de la sortie gardée (compte de la ligne du seuil : zéro ; rien n'a été ouvert, la sortie ne peut porter aucune mesure) :"
  tail -n 40 "$G1"
  dire "(fin de l'extrait)"
else
  dire "ETAT : arrêt après le seuil"
  dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $S_N"
fi
dire "lignes de statut de l'arbre de lecture : $(git -C "$ARBRE" status --porcelain --untracked-files=all | wc -l | tr -d ' ')"
} > "$R" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/releve-apres-lancement-lecture-bbis-$N-v1.txt"
cat "$R"; sha256sum "$R"
```

- **Ce relevé est ce que l'opérateur rend à la conductrice**, avec son chemin et son empreinte. Il ne porte que : le code de sortie, l'état, des noms, des empreintes.
- **État « écrit »** (second complément, point 5) : le relevé dit « écrit », le chemin, l'empreinte, le code de sortie, **et rien qui distingue une lecture faite d'une issue « non lue » de fond** : ni le compte de la ligne du seuil, ni le motif d'un refus, ni la taille du fichier, ni une clé du fichier. L'opérateur n'ajoute rien de tel dans son message.
- **Deux exceptions nécessaires**, parce qu'elles commandent une suite et ne portent aucune issue de mesure : l'état « non consommée » (code 3 et ligne `BBIS LECTURE NON CONSOMMEE`) et l'état « arrêt avant le seuil » sont rendus comme tels.
- **Arrêt avant le seuil** (second complément, point 3) : le relevé porte le code de sortie, les trois comptes de lignes, et les quarante dernières lignes de la sortie gardée, **si et seulement si** le compte de la ligne du seuil est zéro. Une trace d'erreur du programme ou un refus de ses options, qui n'impriment pas la ligne `BBIS LECTURE ARRET`, y sont donc compris. Si le compte du seuil n'est pas zéro, aucune ligne de la sortie n'est extraite.
- L'opérateur n'affiche jamais la sortie gardée elle-même. La sortie de **chaque** lancement est gardée et scellée, quel que soit le code (complément au quatrième addendum, « La suite », point 3 ; condition de la fiche de rattachement). La conductrice la commite sans l'ouvrir.

#### Constat de forme, pour le juge seul

À jouer dans les états « écrit » et « non consommée ». La pièce est écrite et scellée **sans être affichée** ; l'opérateur n'en rend que le chemin et l'empreinte ; **la conductrice ne l'ouvre pas** ; elle est donnée au juge. Elle ne porte aucune valeur de mesure : des présences de clés, les comptes de lignes de la sortie gardée, le motif d'un refus de la garde (noms de lignes, de fichiers et de commits), la liste des fichiers ouverts par la chaîne.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q -E '^ETAT : (écrit|non consommée)' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "aucun fichier de lecture écrit : pas de constat de forme"; exit 1; }
C="$LV1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt"; neuf "$C"
G1="$LV1/sortie-lancement-lecture-bbis-$N-v1.txt"
{
dire "Constat de forme pour le juge — lancement n° $N, run de lecture $RUNL — pièce que la conductrice n'ouvre pas"
dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $(grep -c '^BBIS LECTURE ENTREES OUVERTES$' "$G1")"
dire "lignes « BBIS LECTURE ECRITE » : $(grep -c '^BBIS LECTURE ECRITE ' "$G1")"
dire "lignes « BBIS LECTURE NON CONSOMMEE » : $(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1")"
dire "lignes « BBIS LECTURE ARRET » : $(grep -c '^BBIS LECTURE ARRET' "$G1")"
dire "lignes de la sortie gardée : $(wc -l < "$G1" | tr -d ' ')"
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
dire "octets du fichier de lecture : $(wc -c < "$ARBRE/diag/$RUNL/lecture-bbis.json" | tr -d ' ')"
"$PY" - "$ARBRE/diag/$RUNL/lecture-bbis.json" <<'EOF'
import json, sys
r = json.load(open(sys.argv[1], encoding="utf-8"))["resultat"]
g = r.get("garde")
print("clé garde présente :", g is not None)
if g is not None:
    print("nature du refus :", g.get("nature"))
    print("motif du refus :", g.get("refus"))
    print("preuve d'aucune ouverture conforme :", (g.get("aucune_ouverture") or {}).get("conforme"))
print("clé cellules présente :", "cellules" in r)
print("clé p3bis présente :", "p3bis" in r)
print("règle d'ordre des lignes :", (r.get("ordre_propre") or {}).get("regle"))
print("lecture réelle (essai faux) :", r.get("essai") is False)
print("fichiers ouverts par la chaîne :")
for p in r.get("entrees_lues") or []:
    print("  ", p)
EOF
} > "$C" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt"
echo "constat de forme écrit, non affiché : $C $(sha256sum "$C" | cut -d' ' -f1)"
```

- Exception : dans l'état « non consommée », la conductrice et la mère ont besoin du motif du refus pour décider de la relance. L'opérateur le leur rend par une seule ligne, extraite de la pièce de preuve écrite par le module et non de ce constat : `grep -o '"motif": "[^"]*"' "$ARBRE/diag/$RUNL/preuve-aucune-ouverture-bbis.json"`. Ce motif ne peut porter aucune mesure : rien n'a été ouvert.

### 5.3 Les suites, par code de sortie et par lignes imprimées

L'opérateur agit d'après la ligne `ETAT` du relevé du § 5.2, et d'elle seule.

| état du relevé | ce que c'est | ce que fait l'opérateur | ce qu'il rend à la conductrice |
|---|---|---|---|
| **écrit** (code 0, fichier de lecture écrit) | la lecture a eu lieu au sens du texte : lecture faite, ou issue « non lue » de fond écrite par le module avec sa phrase gelée ; dans les deux cas **la lecture est consommée** et le module a écrit sa ligne au journal | constat de forme pour le juge ; puis § 5.4, **le même geste dans tous les cas** : sorties portées, ligne `LECTURE-BBIS`, journal | « écrit », chemins, empreintes, code de sortie, la ligne ajoutée au registre propre ; rien d'autre |
| **non consommée** (code 3, ligne `BBIS LECTURE NON CONSOMMEE`, seuil à zéro) | issue « non lue » née d'un pur défaut de mise en place ; le module a écrit la pièce de preuve ; rien n'a été ouvert | constat de forme pour le juge ; **rien n'est inscrit ; arrêt** | l'état, les chemins et empreintes du relevé, le motif du refus |
| **arrêt avant le seuil** (ni code 0 ni code 3 ; seuil à zéro) | le programme s'est arrêté sans rien ouvrir ni rien écrire | **arrêt ; aucune relance** ; § 5.5 | le relevé, qui porte l'extrait de la sortie |
| **arrêt après le seuil** (ni code 0 ni code 3 ; seuil imprimé) | arrêt après la première ouverture d'une entrée | **lecture consommée ; arrêt ; nœud** | le relevé seul ; aucune ligne de la sortie |
| **non prévu** | code 0 ou 3 sans les fichiers ou les lignes attendus | arrêt ; nœud | le relevé seul |
| **sortie non gardée** (ni code 0 ni code 3 ; sortie du lancement absente ou non scellée) | rien ne prouve que le seuil n'a pas été franchi | **lecture consommée ; arrêt ; nœud** (complément au quatrième addendum, « La suite », point 3) | le relevé seul ; aucune ligne de la sortie |

- **État « non consommée » — ce que la conductrice et la mère décident ensuite**, selon « La suite » du complément au quatrième addendum : panne corrigée sur l'arbre de lecture seulement ; déclaration `registres/t07-etape-b-bis/lecture-v1/declaration-panne-mise-en-place-bbis-<n>-v1.md`, scellée, qui cite tous les lancements antérieurs et leurs sorties gardées ; ligne `PANNE-MISE-EN-PLACE-BBIS-<n>` inscrite par la mère au registre voisin avant la relance ; correction, fichier de lecture gardé, pièce de preuve, manifeste du run refusé et déclaration commités sur la branche de l'arbre de lecture, poussée de nouveau par la conductrice (§ 4.1) ; arbre vérifié propre ; relance sous le nom du run refusé suivi de `-relance<n>`. **Aucune relance n'est jouée sur cette version de la commande : une relance demande une version de la commande écrite et contre-lue pour elle** (décision d'organisation de la conductrice ; note n3 de la contre-lecture de la version 2 : après les commits de la correction et de la déclaration, les contrôles du § 4.2 sur le parent de la tête et sur les 32 entrées rendraient « on ne lance pas »). **L'opérateur ne fait rien de cela sans un mot de la conductrice** ; il ne corrige pas de son chef.
- **État « arrêt après le seuil »** : aucune relance sous aucun texte ; nœud de Lazar (complément au quatrième addendum, « Tout arrêt après une ouverture consomme la lecture »). Un processus disparu après le seuil en relève aussi.

### 5.4 État « écrit » : sorties portées, ligne `LECTURE-BBIS`, journal

Le module a déjà scellé ses sorties et écrit sa ligne au journal de l'arbre de lecture. L'opérateur porte les sorties, à l'octet, de l'arbre de lecture à l'arbre principal, puis ajoute la ligne au registre propre de l'arbre principal par la fonction du code (`registre_bbis_v2.ajouter_ligne_propre`, l. 95-120 : ligne ajoutée, jamais réécrite ; refus si la clé est déjà là, si le registre n'est pas le registre propre, ou si une clé de l'étape B bis est au registre partagé).

**Le geste est le même que le fichier porte une lecture faite ou une issue « non lue » de fond** : l'opérateur ne le sait pas et n'a pas à le savoir. Fondement : le plan, point 10 (f), fait suivre tout résultat écrit de la ligne `LECTURE-BBIS` ; le complément au quatrième addendum, § 3, la veut « inscrite une seule fois, pour le fichier de la lecture qui compte », et une lecture consommée est celle qui compte ; le second complément du mandat, point 5, veut que rien ne distingue les deux cas pour la conductrice.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : écrit$' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « écrit » : arrêt"; exit 1; }
[ -e "$LV1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt.sha256" ] || { echo "constat de forme pour le juge non écrit : arrêt"; exit 1; }
cd "$DEPOT" || exit 1
neuf "runs/$RUNL"; neuf "diag/$RUNL"; mkdir -p "runs/$RUNL" "diag/$RUNL"
for f in "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json"; do
  cp "$ARBRE/$f" "$f" && cp "$ARBRE/$f.sha256" "$f.sha256" || { echo "copie de $f : arrêt"; exit 1; }
  cmp -s "$ARBRE/$f" "$f" || { echo "copie de $f différente : arrêt"; exit 1; }
done
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json" || { echo "sceau des sorties : arrêt"; exit 1; }
# journal : celui de l'arbre de lecture est celui de l'arbre principal plus une ligne
[ "$(wc -l < "$JOURNAL" | tr -d ' ')" = 1 ] && [ "$(wc -l < "$ARBRE/$JOURNAL" | tr -d ' ')" = 2 ] && [ "$(head -n 1 "$ARBRE/$JOURNAL")" = "$(cat "$JOURNAL")" ] || { echo "journal : état inattendu : arrêt"; exit 1; }
tail -n 1 "$ARBRE/$JOURNAL" >> "$JOURNAL"
# ligne LECTURE-BBIS, par la fonction du code
PYTHONPATH=src "$PY" - "$RUNL" <<'EOF'
import sys, time
from pathlib import Path
from controle_ia.scellement import empreinte
from controle_ia.t07bbis.registre_bbis_v2 import REGISTRE_PROPRE, ajouter_ligne_propre
chemin = f"diag/{sys.argv[1]}/lecture-bbis.json"
print(ajouter_ligne_propre(Path("."), REGISTRE_PROPRE, "LECTURE-BBIS", int(time.time()), chemin, empreinte(chemin)))
EOF
tail -n 1 "$JOURNAL" | cut -c1-200
git status --porcelain --untracked-files=all
```

- **Format de la ligne** : celui du registre propre, `| LECTURE-BBIS | AAAA-MM-JJTHH:MM:SSZ | diag/<run>/lecture-bbis.json | sha256 |` (`t07/registre_v1.ecrire_ligne`, l. 318-322).
- Rien n'est écrit dans `registres/scellements-v1.md`.
- L'opérateur rend : « écrit » ; la ligne ajoutée (clé, heure, chemin, empreinte) ; la dernière ligne du journal (elle ne porte qu'une date, le nom du run et une empreinte) ; les chemins et empreintes des sorties et du constat de forme pour le juge ; l'identifiant du processus, le code de sortie (les heures de début et de fin sont dans le constat de forme, pour le juge seul). **Aucun chiffre de mesure, aucune issue, rien du constat de forme.** La liste des fichiers de résultat ouverts par la chaîne est dans le constat de forme, pour le juge ; à la conductrice, l'opérateur rend seulement : « à l'œil : aucun ; par la chaîne : liste dans le constat de forme ».
- L'arbre de lecture et sa branche locale ne sont pas retirés par l'opérateur.

### 5.5 État « arrêt avant le seuil » : conduite, et preuve après coup sur ordre écrit seulement

- **Statut de cette voie.** Le complément scellé au quatrième addendum (§ 7, point 7) la dit : « La voie de l'arrêt avant le seuil n'est pas employée avant son mot » — le mot de Lazar. **Toute relance par cette voie attend donc le mot de Lazar**, et non la seule confirmation de la session mère : l'application par anticipation que la mère avait annoncée ne remplace pas un texte scellé (message de la mère du 2026-11-18 à 23:36:15Z ; R-3530). La forme de la preuve après coup — comparaison des fichiers au commit épinglé des sorties `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9`, après vérification de `sondes-bbis.json` contre la ligne `SCORES-BBIS`, sans décoder ce fichier — reste la forme recommandée et portée à Lazar ; **il ne l'a pas encore accordée**.
- **Conduite.** Sur un arrêt avant le seuil, l'opérateur **ne relance pas** et ne corrige rien. Il rend le relevé du § 5.2 et s'arrête. Il joue le programme de la preuve après coup **seulement sur ordre écrit de la conductrice** : le jouer n'emploie pas la voie, il relève un état ; relancer l'emploierait (classement de la contre-lecture de la version 2, point (g), N1 bis). Il rend la pièce (chemin, empreinte, la ligne imprimée par le programme, son code de sortie) et s'arrête de nouveau. La conductrice rend la pièce à la mère, qui la porte à Lazar. Aucune relance n'est jouée sur cette version de la commande (§ 5.3).
- **La ligne, à ne jouer que sur cet ordre écrit** (`scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py`, `b7bc7e5d87ba45a696ded6790e1354fd065467f838ef565efba2ff0746b05675`, cité par la fiche de rattachement ; usage : son en-tête, l. 35-37). Elle donne **toutes** les sorties gardées des lancements antérieurs, une paire chemin et empreinte par lancement :

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : arrêt avant le seuil$' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « arrêt avant le seuil » : arrêt"; exit 1; }
egal "empreinte du programme de la preuve après coup" b7bc7e5d87ba45a696ded6790e1354fd065467f838ef565efba2ff0746b05675 "$(sha256sum "$ARBRE/scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py" | cut -d' ' -f1)"
[ "$FAUTES" = 0 ] || { echo "programme d'une autre empreinte : arrêt"; exit 1; }
set --
for n in $(seq 1 "$N"); do g="$LV1/sortie-lancement-lecture-bbis-$n-v1.txt"; set -- "$@" --sortie-lancement "$g" "$(sha256sum "$g" | cut -d' ' -f1)"; done
cd "$ARBRE" || exit 1
"${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 "$PY" scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py --racine "$ARBRE" --run-lecture "$RUNL" --run-bbis "$RUN_BBIS" --numero "$N" "$@"
echo "code de sortie du programme de la preuve après coup : $?"
```

- Le programme écrit et scelle lui-même sa pièce, dans l'arbre de lecture : `registres/t07-etape-b-bis/lecture-v1/preuve-aucune-ouverture-apres-coup-bbis-<N>-v1.json`. Il n'imprime que des chemins, des empreintes et des états ; il refuse de partir sous une variable `GIT_` (d'où l'environnement nettoyé).
- Code 0 : pièce conforme ; code 1 : pièce écrite, non conforme (« lecture consommée » ou « nœud », selon son classement) ; code 2 : rien d'écrit. Dans les trois cas l'opérateur rend et s'arrête ; il ne rejoue pas le programme.

## 6. Ce que la conductrice commite

Sur la branche de travail `claude/lecture-verdict-etape-b-bis-v1`. Le texte ne nomme aucune branche de données pour les sorties de la lecture (« Données gardées », l. 214 : « Lecture : `diag/<run-bbis-lecture>/lecture-bbis.json` […] chacun avec son compagnon ») : elles vont sur la branche de travail ; la mère porte les lignes de registre sur `main` par chemin et empreinte.

Avant le lancement de l'opérateur (étape 0) :
- la fusion du commit de `main` `4aefb5b1…` ;
- `registres/t07-etape-b-bis-v1.md.ouvertures.md` (ligne d'en-tête) ;
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v3.md`, ses différences avec la version 2, la contre-lecture de la version 2 dont elle porte les corrections, leurs compagnons (les versions 1 et 2 et leurs pièces restent, R12).

Entre les deux temps de l'opérateur (§ 4.1) : `registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` et son compagnon, commités et poussés sur la branche de travail (preuve « inscrite à part », avant la lecture : feu, § 12) ; puis la poussée de la branche de l'arbre de lecture sous le nom `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture`, qui n'est pas un commit de la branche de travail.

Après, selon l'état (tous sous `registres/t07-etape-b-bis/lecture-v1/`, chacun avec son compagnon) :
- `releve-avant-lancement-lecture-bbis-<N>-v1.txt`, `lancement-lecture-bbis-<N>-v1.sh`, `sortie-lancement-lecture-bbis-<N>-v1.txt`, `releve-apres-lancement-lecture-bbis-<N>-v1.txt` ; la sortie gardée est commitée **sans être ouverte** ;
- `constat-forme-pour-le-juge-lecture-bbis-<N>-v1.txt`, commité **sans être ouvert**, donné au juge par son chemin et son empreinte ;
- état « écrit » : `runs/<run>/manifeste.json`, `diag/<run>/lecture-bbis.json`, leurs compagnons, commités sans être ouverts ; le registre propre (ligne `LECTURE-BBIS`) ; le journal (seconde ligne) ;
- état « non consommée » : les fichiers écrits par le module restent dans l'arbre de lecture, cités par chemin et empreinte dans le relevé, et sont commités sur la branche de l'arbre de lecture avant une relance (§ 5.3) ;
- état « arrêt avant le seuil », si la preuve après coup a été ordonnée : sa pièce reste dans l'arbre de lecture, de même ;
- les relevés de mise en place restent dans le dossier temporaire ; la conductrice peut les faire porter et sceller si elle les veut au dépôt.

Jamais commités sur la branche de travail : les 32 fichiers d'entrée de l'arbre de lecture. La branche locale `lecture/bbis-arbre-de-lecture-v1` n'y est jamais fusionnée.

## 7. Points ouverts et écarts

### Ce que deviennent les onze points du premier rendu

1. **La garde refusait sur l'ordre des lignes** — tranché par Lazar (`GO-2026-11-18-56` (1)) : quatrième addendum, QA-1 ; exception fermée dans `lecture_v5.exiger_ordre_propre`. Réserve R-ORDRE au verdict.
2. **Histoire du registre propre non linéaire** — déclarée : quatrième addendum, QA-3 et § 2.0 (F4 à F7) ; entre dans R-ORDRE. Le relevé (C) du § 2 l'écrit.
3. **Garde non séparable de la lecture** — tranché : aucun mode « garde seule » (complément, § 3) ; un fichier est écrit sur tout refus (quatrième addendum, § 6.5, point 3) ; les suites sont celles de `GO-2026-11-18-60` et `-64` (§ 5.3, § 5.5). Voir N2 ci-dessous.
4. **Arbre propre exigé par le manifeste, après le calcul** — tranché : geste de la commande (quatrième addendum, § 6.5, point 4) ; l'opérateur commite localement (complément du mandat) ; la conductrice pousse la branche de l'arbre de lecture avant le lancement (second complément, point 7 ; § 4.1). Voir N3.
5. **Arbre de travail séparé plutôt que clone local** — tranché : complément du mandat, point 2 ; montage admis par la session mère.
6. **Entrées sur trois branches** — tenu par les § 1.2 et 1.3. La tête de la branche de la pièce « mots et coût » n'est nommée par aucun texte : le fichier est ancré par l'empreinte de sa ligne de registre.
7. **Fichier de scores absent rendu « non calculable » sans arrêt** — tranché par le texte (quatrième addendum, § 6.5, point 7) ; le § 1.3 contrôle chaque entrée avant le lancement.
8. **Journal** — tranché : quatrième addendum, § 6.5, point 8 ; créé à l'étape 0, en-tête seule.
9. **Environnement** — tenu : versions figées relevées, fils de calcul à 1 (§ 4.2, § 5.1). **Reste ouvert** : N5.
10. **`main` jamais joué en réel ; durée inconnue** — en partie levé : les essais neufs jouent le vrai `main` sur jouets (contre-lecture du code, note n9). Il reste que le module, sa garde et cette commande n'ont jamais tourné sur les fichiers réels (réserve de la fiche de rattachement) ; la durée reste inconnue.
11. **Branche des sorties de la lecture** — inchangé : le texte n'en nomme aucune ; branche de travail (§ 6).

### Points ouverts de cette commande

- **N1 — Des arrêts avant le seuil restent possibles malgré le § 4 ; réduit.** La table des modules gelés du code de la pièce « mots et coût » est désormais comparée avant le lancement, par empreinte (§ 1.4 ; constat m4 de la contre-lecture de la version 2). Restent, selon l'inventaire de ce rapport (note n8) : une erreur d'importation ou d'exécution du code de la pièce, le disque plein, un processus disparu ; aucun ne peut être exclu sans jouer le code. Un tel arrêt mène au § 5.5 : l'opérateur ne relance pas ; toute relance par cette voie attend le mot de Lazar. Classé par le rapport : question d'organisation.
- **N1 bis — Toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar** (complément au quatrième addendum, § 7, point 7 ; message de la mère du 2026-11-18 à 23:36:15Z, R-3530 ; contre-lecture de la version 2, point (g) : « nœud de Lazar si la voie doit servir à une relance »). La forme de la preuve après coup est recommandée et portée à Lazar, non encore accordée. Non bloquant pour le premier lancement.
- **N2 — Ligne `LECTURE-BBIS` inscrite dans tout état « écrit », issue « non lue » de fond comprise** (§ 5.4) : **tranché par le texte, dans le sens de la commande** (contre-lecture de la version 2, point (g) et note n1 : plan, point 10 (f), et point 2 ; quatrième addendum, § 7, point 4 ; complément au quatrième addendum, « La suite », point 1, et § 3). Ni question d'organisation, ni nœud.
- **N3 — Commit des entrées cité par le manifeste.** Tranché par le second complément, point 7 : la conductrice pousse la branche de l'arbre de lecture sous `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture` avant le lancement ; le § 4.2 vérifie la tête du distant. Il reste que cette branche du distant porte une seconde fois, sous un autre nom, les 32 fichiers d'entrée, dont les fichiers fermés de scores.
- **N4 — Le mandat du lecteur-opérateur et cette commande ne s'accordent pas en plusieurs endroits** (à dire aussi dans son message de lancement : il ne fait pas la récupération complète du distant, que la conductrice fait à l'étape 0 ; il attend la fin du lancement sans attente fixe dans un appel de terminal, que son outil refuse — note n6 de la contre-lecture de la version 2), que le complément du mandat tranche : il « ne commite pas » (ici : un commit local dans l'arbre de lecture) ; il « crée » le journal (ici : la conductrice, à l'étape 0, lui en relève l'état) ; il joue « la garde » comme une étape (ici : elle est dans le module) ; les règles communes lui interdisent tout appel à un service extérieur (ici : la récupération des branches nommées et la lecture des têtes du distant, en lecture seule, § 1.1 et § 4.2, permises par le second complément, point 4, que la conductrice écrit dans son mandat) ; il est lancé en deux temps (§ 0). À dire dans son message de lancement.
- **N5 — Versions du run de la pièce « mots et coût » non comparées.** Son manifeste n'est pas dans la liste blanche du plan, point 1. Si les versions différaient, le contrôle d'égalité rendrait la base « non calculable » avec un nœud, sans arrêt du reste (liste d'arrêt, l. 193).
- **N6 — Verdict de l'épreuve du signal planté que cite son fichier d'issue, non contrôlé avant le lancement** : **tranché par le texte** (contre-lecture de la version 2, point (g)) : son nom ne se connaît qu'en ouvrant le fichier d'issue, que la chaîne seule ouvre ; un fichier absent ou illisible donne une issue « non lue » de fond (complément au quatrième addendum, « La règle ») ; l'arbre de lecture, propre, porte les fichiers suivis. Risque accepté par le texte ; aucune action.
- **N7 — Retrait des variables `GIT_`.** Les onze noms sont ceux que la contre-lecture du code relève sur cette machine ; je n'en ai lu aucune valeur. Si git, privé d'elles, refusait l'arbre de lecture, le § 4.2 le dit et on ne lance pas ; aucun texte ne dit quoi faire ensuite.
- **N8 — Blocs écrits par simple lecture.** Aucun n'a été joué ; seule leur syntaxe est contrôlée. Une faute d'un bloc d'avant lancement arrête sans rien consommer. Le lancement détaché (`setsid -f`) n'a jamais été éprouvé avec ce module : si l'identifiant du processus n'est pas écrit à deux relevés de suite (§ 5.1 bis), l'opérateur ne relance pas et rend.
- **N9 — retiré.** Les lignes que le verdict cite (cinq lignes d'addenda, ligne de rattachement, réserve R-ORDRE) sont portées par le complément du mandat du juge, écrit par la conductrice.
- **N10 — Fusion de `main`.** Elle apporte dans l'arbre de lecture des fichiers d'autres chaînes que la lecture n'ouvre pas ; relevé par les noms : elle ne change ni le registre propre, ni le registre partagé pour ses cinq lignes lues, ni le module, ni la fiche de rattachement, ni un fichier sous `src/` déjà présent, et n'ajoute à `requirements-cpu.txt` que des lignes. Le § 1.4 le revérifie après coup par les empreintes.
