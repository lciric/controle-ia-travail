"""Fabrique scripts/lancer_bbis_v6.sh depuis la v5 par remplacements exacts, pour une différence minimale."""
import sys
from pathlib import Path
t = Path("scripts/lancer_bbis_v5.sh").read_text(encoding="utf-8")
dst = Path(sys.argv[1])
assert not dst.exists(), "R12 : existe déjà"
def r(t, a, b, n=1):
    assert t.count(a) == n, (t.count(a), a[:80])
    return t.replace(a, b)
t = r(t, "amorce_bbis_v5.sh", "amorce_bbis_v6.sh", 7)
t = r(t, "lancer_bbis_v5.sh", "lancer_bbis_v6.sh", 3)
t = r(t, "#!/usr/bin/env bash\n", """#!/usr/bin/env bash
# v6 (2026-11-18, GO-2026-11-18-04 ; la v5 reste, R12) : la v5, qui passe l'amorce v6, avec cinq écarts, chacun marqué « v6 » :
#   (1) garde neuve « commit de la course » dans `commande` : avant d'imprimer la commande de création, l'arbre que l'amorce
#       extrairait à COMMIT est reconstruit dans un dossier jetable (motifs et copie des fichiers cités LUS DANS L'AMORCE, objets
#       du dépôt de la mère, aucun réseau, rien d'écrit dans RACINE) et la garde d'entrée de la marche y est rejouée par le code
#       même de cet arbre ; la v5 lisait le registre de la tête, non celui de COMMIT (arrêt 2 de R-3160) ;
#   (2) garde neuve « commit joignable » : COMMIT doit être la tête ou un ancêtre de la tête de BRANCHE_CODE sur le dépôt
#       distant (`git ls-remote`, lecture seule) : l'amorce clone cette branche et s'arrêterait sur un commit non poussé ;
#   (3) sous-commande neuve `essais-du-commit RACINE COMMIT DOSSIER` : joue la ligne d'essais de l'amorce sur ce même arbre et
#       compare le compte au plancher MIN_ESSAIS de l'amorce (arrêt 1 : le plancher se mesure sur l'arbre extrait) ;
#   (4) image de la machine exigée égale à IMAGE_COURSE (correction 7 de la contre-lecture du projet de feu : par le nom, non
#       par un condensé) ; (5) prix de l'offre borné par PRIX_MAX_USD_H (GO-2026-11-18-03 (3) : 1,40 USD/h ; s'ajoute au
#       plafond tenu par le feu et au prix relu après création, ne les remplace pas).
""")
t = r(t, "DISQUE=150\n", """DISQUE=150
IMAGE_COURSE=python:3.11-bookworm   # v6 (écart 4) : image des passes précédentes, exigée égale
PRIX_MAX_USD_H=1.40                 # v6 (écart 5) : plafond de GO-2026-11-18-03 (3), prix de carte de l'offre (clé prix_usd_h)
# >>> arbre-du-commit (v6, écarts 1 et 3 ; joué par tests/test_chaine_bbis_v6_v1.py)
arbre_du_commit() {  # $1 = racine (dépôt de la mère) ; $2 = COMMIT ; $3 = amorce ; $4 = dossier neuf : y reconstruit l'arbre que
    # l'amorce extrait à COMMIT (étape 2 : motifs, puis copie des fichiers cités par le registre propre, textes lus dans
    # l'amorce) ; dépôt jetable adossé aux objets de $1 (aucune copie d'objets, aucun clone, aucun filtre, aucun réseau ; rien
    # n'est écrit dans $1). Motif sur la sortie et code 2 sinon. La sortie de 7b (étape 3) n'est pas apportée.
    local rac="$1" c="$2" am="$3" d="$4" objets peu motifs bloc v
    for v in $(compgen -v | grep -E '^GIT_'); do unset "$v"; done      # jamais les variables GIT_* de la session
    [ ! -e "$d" ] || { echo "dossier $d déjà présent (R12)"; return 2; }
    git -C "$rac" cat-file -e "$c^{commit}" 2> /dev/null || { echo "commit $c absent du dépôt $rac"; return 2; }
    objets=$(git -C "$rac" rev-parse --path-format=absolute --git-path objects) && [ -d "$objets" ] || { echo "objets de $rac illisibles"; return 2; }
    motifs=$(sed -n "/^MOTIFS='/,/'\\$/p" "$am" | sed "1s/^MOTIFS='//; \\$s/'\\$//")
    printf '%s\\n' "$motifs" | grep -qx '/src/' || { echo "motifs d'extraction illisibles dans l'amorce"; return 2; }
    bloc=$(sed -n '/^# >>> copie-des-fichiers-cites/,/^# <<< copie-des-fichiers-cites/p' "$am")
    [ -n "$bloc" ] || { echo "bloc de copie des fichiers cités illisible dans l'amorce"; return 2; }
    git init -q "$d" && printf '%s\\n' "$objets" > "$d/.git/objects/info/alternates" || { echo "dépôt jetable impossible"; return 2; }
    peu=$(git -C "$rac" rev-parse --path-format=absolute --git-path shallow); [ ! -f "$peu" ] || cp "$peu" "$d/.git/shallow"
    git -C "$d" config user.name "essai du commit de la course"; git -C "$d" config user.email "essai@invalid"
    git -C "$d" sparse-checkout init --no-cone > /dev/null 2>&1 && printf '%s\\n' "$motifs" | git -C "$d" sparse-checkout set --no-cone --stdin > /dev/null 2>&1 \\
        && git -C "$d" checkout -q --detach "$c" 2> /dev/null || { echo "extraction partielle de $c impossible"; return 2; }
    ( D="$d"; COPIES=(); arret() { echo "$1"; exit 2; }; eval "$bloc"
      [ "${#COPIES[@]}" -gt 0 ] || arret "aucun fichier cité par le registre propre à ce commit"
      git -C "$d" add --sparse -f -- "${COPIES[@]}" && git -C "$d" commit -q --allow-empty -m "entrées copiées (essai, jamais poussé)" \\
          || arret "commit local des entrées copiées impossible" ) || return 2
    return 0; }
commit_de_la_course() {  # $1 = arbre reconstruit ; $2 = amorce ; $3 = run de 7b : rejoue la garde d'entrée de la marche que
    # l'amorce lance (module lu dans l'amorce), par le code de l'arbre lui-même ; BBIS_INSTANCE n'est posée que pour cet
    # appel, qui ne lit que le registre propre, les sceaux, la fiche et les fichiers qu'elle cite : rien n'est appris ni noté.
    local m
    m=$(sed -n 's/^.*-m \\(controle_ia\\.t07bbis\\.marche_v[0-9][0-9]*\\) \\\\$/\\1/p' "$2")
    [ "$(printf '%s' "$m" | grep -c '^')" = 1 ] || { echo "module de la marche illisible ou multiple dans l'amorce"; return 2; }
    BBIS_INSTANCE=1 PYTHONPATH="$1/src" PYTHONDONTWRITEBYTECODE=1 "$PY" -c 'import importlib, sys
try:
    r = importlib.import_module(sys.argv[1]).gardes_d_entree(sys.argv[2], sys.argv[3])
except Exception as e:   # garde de la marche, sceau refusé ou code illisible : refus, jamais un passage silencieux
    print(f"garde d'"'"'entrée de la marche au commit de la course : {type(e).__name__} : {e}"); sys.exit(2)
print(f"{len(r['"'"'fiche'"'"']['"'"'fichiers'"'"'])} fichiers de la fiche, tête {r['"'"'tete'"'"']}")' "$m" "$1" "$3" 2>&1 || return 2; }
commit_joignable() {  # $1 = racine ; $2 = COMMIT ; $3 = BRANCHE_CODE : COMMIT est la tête ou un ancêtre de la tête de la branche
    # sur le dépôt distant (lecture seule) ; branche absente, distant injoignable, tête distante inconnue du clone : refus
    local h
    h=$(git -C "$1" ls-remote origin "refs/heads/$3" 2> /dev/null | cut -f1)
    case "$h" in ''|*[!0-9a-f]*) echo "branche $3 absente du dépôt distant, ou dépôt injoignable : l'amorce ne pourrait pas la cloner"; return 2;; esac
    git -C "$1" cat-file -e "$h^{commit}" 2> /dev/null || { echo "tête distante $h de $3 absente du clone local (git fetch) : commit joignable non prouvé"; return 2; }
    git -C "$1" merge-base --is-ancestor "$2" "$h" 2> /dev/null || { echo "commit $2 absent de la branche $3 du dépôt distant (non poussé, ou autre branche) : l'amorce s'arrêterait après le clonage"; return 2; }
    return 0; }
# <<< arbre-du-commit
""")
t = r(t, """        case "$IMAGE" in *[!A-Za-z0-9._:/-]*|'') echo "BBIS REFUS : image illisible"; exit 2;; esac
""", """        case "$IMAGE" in *[!A-Za-z0-9._:/-]*|'') echo "BBIS REFUS : image illisible"; exit 2;; esac
        [ "$IMAGE" = "$IMAGE_COURSE" ] || { echo "BBIS REFUS : image $IMAGE ≠ $IMAGE_COURSE (image de la course)"; exit 2; }   # v6 (écart 4)
""")
t = r(t, """        py_registre offre "$FOFFRE" "$OFFRE" > /dev/null || { py_registre offre "$FOFFRE" "$OFFRE"; exit 2; }
""", """        py_registre offre "$FOFFRE" "$OFFRE" > /dev/null || { py_registre offre "$FOFFRE" "$OFFRE"; exit 2; }
        # v6 (écart 5) : prix de carte de l'offre, nombre dans ]0 ; PRIX_MAX_USD_H] ; clé absente ou illisible : refus
        "$PY" -I -c 'import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8")).get("prix_usd_h")
sys.exit(0 if not isinstance(p, bool) and isinstance(p, (int, float)) and 0 < p <= float(sys.argv[2]) else 1)' "$FOFFRE" "$PRIX_MAX_USD_H" 2> /dev/null \\
            || { echo "BBIS REFUS : prix de l'offre (clé prix_usd_h) absent, illisible ou au-dessus de $PRIX_MAX_USD_H USD/h (GO-2026-11-18-03)"; exit 2; }
""")
t = r(t, """        py_registre ancetre "$RAC" "$COMMIT" > /dev/null || { py_registre ancetre "$RAC" "$COMMIT"; exit 2; }
""", """        py_registre ancetre "$RAC" "$COMMIT" > /dev/null || { py_registre ancetre "$RAC" "$COMMIT"; exit 2; }
        # v6 (écarts 1 et 2) : ce que la marche exigera, vérifié sur l'arbre extrait À COMMIT, et COMMIT joignable par l'amorce
        M=$(commit_joignable "$RAC" "$COMMIT" "$BRC") || { echo "BBIS REFUS : $M"; exit 2; }
        RAC_ARBRE=$(mktemp -d) || { echo "BBIS REFUS : dossier jetable de l'arbre du commit impossible"; exit 2; }
        M=$(arbre_du_commit "$RAC" "$COMMIT" "$ICI/amorce_bbis_v6.sh" "$RAC_ARBRE/arbre") && M=$(commit_de_la_course "$RAC_ARBRE/arbre" "$ICI/amorce_bbis_v6.sh" "$RUN7B"); c=$?
        rm -rf "$RAC_ARBRE"
        [ "$c" = 0 ] || { echo "BBIS REFUS : commit de la course $COMMIT : $M"; exit 2; }
""")
t = r(t, """    depense)
""", """    essais-du-commit)   # v6 (écart 3) : plancher d'essais de l'amorce mesuré sur l'arbre qu'elle extrait à COMMIT ; DOSSIER neuf, gardé
        [ "$#" = 4 ] || { echo "BBIS REFUS : essais-du-commit RACINE COMMIT DOSSIER"; exit 2; }
        AM="$ICI/amorce_bbis_v6.sh"; DOS="$4"
        [ ! -e "$DOS" ] && mkdir -p "$DOS" && DOS=$(cd "$DOS" && pwd) || { echo "BBIS REFUS : dossier $4 déjà présent ou impossible (R12)"; exit 2; }
        M=$(arbre_du_commit "$2" "$3" "$AM" "$DOS/depot") || { echo "BBIS REFUS : $M"; exit 2; }
        MIN=$(sed -n 's/^MIN_ESSAIS=\\([0-9][0-9]*\\)$/\\1/p' "$AM"); LIGNE=$(grep -c '^PYTHONPATH=src "\\$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_\\*\\.py --basetemp=' "$AM")
        [ "$(printf '%s' "$MIN" | grep -c '^')" = 1 ] && [ "$LIGNE" = 1 ] || { echo "BBIS REFUS : plancher ou ligne d'essais illisible dans l'amorce"; exit 2; }
        eval "$(sed -n '/^# >>> compte-des-essais/,/^# <<< compte-des-essais/p' "$AM")"
        find "$DOS/depot" -path "$DOS/depot/.git" -prune -o -type f -print | sed "s#^$DOS/depot/##" | LC_ALL=C sort > "$DOS/fichiers-de-l-arbre.txt"
        # même ligne que l'amorce (étape 5), depuis l'arbre, par l'interpréteur de la session (PYTHON_BBIS)
        ( cd "$DOS/depot" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py --basetemp="$DOS/essais-tmp" > "$DOS/essais.txt" 2> "$DOS/essais.err" ); c=$?
        RES=$(tail -n 1 "$DOS/essais.txt"); NP=$(compte_passes "$RES")
        echo "BBIS ESSAIS DU COMMIT $3 : code $c, ligne de compte : $RES ; plancher de l'amorce $MIN ; $(grep -c '' "$DOS/fichiers-de-l-arbre.txt") fichiers sur l'arbre ($DOS)"
        [ "$c" = 0 ] || { echo "BBIS REFUS : essais en échec sur l'arbre extrait (essais.txt) : l'amorce s'arrêterait à son étape 5"; exit 2; }
        [ "$NP" -ge "$MIN" ] || { echo "BBIS REFUS : $NP passés < $MIN : l'amorce s'arrêterait à son étape 5"; exit 2; }
        [ -z "$(git -C "$DOS/depot" status --porcelain --untracked-files=all -- src tests)" ] || { echo "BBIS REFUS : les essais ont écrit sous src ou tests"; exit 2; }
        echo "BBIS ESSAIS DU COMMIT : $NP passés ≥ $MIN : le plancher de l'amorce serait franchi"; exit 0;;
    depense)
""")
t = r(t, "(offre-depuis-recherche, offre, creation, commande, depense, detruire, verifier-destruction)", "(offre-depuis-recherche, offre, creation, commande, essais-du-commit, depense, detruire, verifier-destruction)")
dst.write_text(t, encoding="utf-8")
