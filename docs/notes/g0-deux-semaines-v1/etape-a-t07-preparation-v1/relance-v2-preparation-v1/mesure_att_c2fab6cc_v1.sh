#!/usr/bin/env bash
# Mesure de la ligne d'essais ATT de T0.7 au commit c2fab6cc (nouveau C7, fusion du correctif du cache, R-2604), par la méthode
# du § 11 bis de l'ordre (celle de mesure-att-c7-v1.md, b70c77fd…, et de mesure_essais_t07_cache_v1.sh, d64c1ebc…) : clone partiel de
# la seule branche main ; lignes 132-169 et 171-198 du script v4 (4b17d1f0…, lu au commit mesuré) sourcées TELLES QUELLES (aucun
# écart : origin/main existe dans un clone de main) ; S7 = C7 = commit mesuré ; CONFIG = chemin de l'ordre (copie sous prereg/,
# présente à ce commit) ; RUN6 = run de 7b de l'ordre (la ligne 183 écarte ses chemins, comme sur l'instance) ; puis l'étape 6
# (commande pytest de l'instance). Puis, en diagnostic, la même commande sous noyau OpenBLAS « Zen » (réserve de R-2319).
# Usage : mesure.sh BAC COMMIT
set -uo pipefail
BAC="$1"; S7="$2"; C7="$2"
URL=https://github.com/lciric/controle-ia-travail.git
D="$BAC/d"; JOURNAL="$BAC/journal-mesure.txt"
CONFIG=prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json
S6=935262b17ca95894a882b02f1526ee39d1738652
RUN6=20261111-151701-t06-reel
PY=/home/user/controle-ia-travail/.venv/bin/python
j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
arret() { j "ARRET : $1"; exit "${2:-4}"; }
j "début ; S7 = C7 = $S7 ; branche main ; interpréteur $("$PY" -c 'import sys; print(sys.version.split()[0])') ; processeur $(grep -m 1 '^model name' /proc/cpuinfo | sed -E 's/^model name[[:space:]]*:[[:space:]]*//')"
cd "$BAC" || exit 2
[ ! -e "$D" ] || arret "$D existe déjà" 2
git clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$D" || arret "clonage" 2
j "clone : origin/main = $(git -C "$D" rev-parse origin/main) ; promisor $(git -C "$D" config --get remote.origin.promisor) ; filtre $(git -C "$D" config --get remote.origin.partialclonefilter) ; refspec $(git -C "$D" config --get remote.origin.fetch)"
[ "$(git -C "$D" show "$S7:scripts/etape_a_t07_variante_b_v4.sh" | sha256sum | cut -d' ' -f1)" = 4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6 ] || arret "script v4 au commit mesuré ≠ 4b17d1f0" 2
# shellcheck source=/dev/null
. "$BAC/etape2-lignes-132-169.sh"
j "étape 2 : $(git -C "$D" ls-files -t | grep -c '^H ') fichiers extraits ; tête $(git -C "$D" rev-parse HEAD) ; H $H"
P=; for k in JD JA JC CONCEPTS; do c=SCELLEMENT-JEUX-T07-$k; [ "$k" = CONCEPTS ] && c=SCELLEMENT-CONCEPTS-T07
    [ "$(git -C "$D" show "$H:registres/scellements-v1.md" | grep -c "^| $c |")" = 1 ] && P="$P,$k"; done
PERIM=${P#,}; [ -n "$PERIM" ] || PERIM=aucun
case "$PERIM" in aucun) PER=",";; *) PER=",$PERIM,";; esac
j "périmètre lu au registre de H : $PERIM"
# shellcheck source=/dev/null
. "$BAC/etape3-lignes-171-198.sh"
j "étape 3 : faite ; état : $(git -C "$D" status --porcelain --untracked-files=all | wc -l) entrée(s) hors suivi ou modifiées (registres)"
j "arbres : src $(git -C "$D" rev-parse "$S7:src") ; tests $(git -C "$D" rev-parse "$S7:tests")"
cd "$D" || arret "dépôt" 2
LISTE="tests/test_t07_*.py"
sha256sum $LISTE > "$BAC/essais-liste.txt"
j "étape 6 : $(wc -l < "$BAC/essais-liste.txt") fichiers d'essais (liste $(sha256sum < "$BAC/essais-liste.txt" | cut -c1-16)) ; lancement"
TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src "$PY" -m pytest -q -rsxX -p no:cacheprovider --color=no $LISTE --basetemp="$BAC/essais-tmp" -o tmp_path_retention_policy=failed > "$BAC/essais.txt" 2> "$BAC/essais.err"; c=$?
DL=$(tail -n 1 "$BAC/essais.txt" | sed -E 's/ in [0-9.]+s.*$//')
j "essais : code $c, ligne « $DL » ; brute « $(tail -n 1 "$BAC/essais.txt") »"
grep -E '^(SKIPPED|XFAIL|XPASS|FAILED|ERROR)' "$BAC/essais.txt" > "$BAC/essais-sauts.txt"
[ -z "$(git status --porcelain --untracked-files=all -- src tests)" ] && j "src et tests non écrits par les essais" || j "ÉCART : src ou tests écrits par les essais"
j "diagnostic : même commande, OPENBLAS_CORETYPE=Zen ; lancement"
OPENBLAS_CORETYPE=Zen TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src "$PY" -m pytest -q -rsxX -p no:cacheprovider --color=no $LISTE --basetemp="$BAC/essais-tmp-zen" -o tmp_path_retention_policy=failed > "$BAC/diag-zen.txt" 2> "$BAC/diag-zen.err"; c=$?
DZ=$(tail -n 1 "$BAC/diag-zen.txt" | sed -E 's/ in [0-9.]+s.*$//')
j "diagnostic Zen : code $c, ligne « $DZ » ; brute « $(tail -n 1 "$BAC/diag-zen.txt") »"
grep -E '^(SKIPPED|XFAIL|XPASS|FAILED|ERROR)' "$BAC/diag-zen.txt" > "$BAC/diag-zen-sauts.txt"
cmp -s "$BAC/essais-sauts.txt" "$BAC/diag-zen-sauts.txt" && j "sauts et échecs attendus identiques à l'octet entre les deux passages" || j "ÉCART : sauts ou échecs différents entre les deux passages"
[ -z "$(git status --porcelain --untracked-files=all -- src tests)" ] && j "src et tests non écrits (après le diagnostic)" || j "ÉCART : src ou tests écrits (diagnostic)"
j "fin"
