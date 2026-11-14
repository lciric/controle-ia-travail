#!/usr/bin/env bash
# Répétition partielle, sur dépôts jouets, du bloc C2 de commande-compte-3-v1.md (placement des données de l'étape B :
# fonction place, dépôts jetables sans contenu, morceaux, recomposition, fichier « mots et coût » pris sur la branche de la
# phase B). Écrite le 2026-11-14 par le préparateur (modèle A). Aucune donnée réelle : branches jouets dans un dépôt distant
# local ; seules changent, dans la copie du bloc, les deux empreintes réelles des lignes SCORES-T07 et SONDES-T07 (remplacées
# par celles des jouets). N'écrit rien hors du bac donné.
#     bash repetition_bloc_c2_jouet_v1.sh <dépôt réel (pour lire la commande)> <bac neuf> [<python>]
set -u
DEPOT_REEL=$(cd "$1" && pwd); T="$2"; PY="${3:-$DEPOT_REEL/.venv/bin/python}"
[ ! -e "$T" ] || { echo "ARRÊT : $T existe déjà"; exit 1; }
mkdir -p "$T"; T=$(cd "$T" && pwd); export LC_ALL=C.UTF-8 GIT_AUTHOR_NAME=jouet GIT_AUTHOR_EMAIL=jouet@exemple.invalid \
    GIT_COMMITTER_NAME=jouet GIT_COMMITTER_EMAIL=jouet@exemple.invalid
date -u +"début de la répétition : %Y-%m-%dT%H:%M:%SZ"
CMD="$DEPOT_REEL/docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-v1.md"
R6=20261111-151701-t06-reel; R7=20261114-001352-t07-lecture-reel; RMC=20261117-000000-t06-mots-et-cout
git init -q --bare "$T/distant.git"; git -C "$T/distant.git" symbolic-ref HEAD refs/heads/main; git -C "$T/distant.git" config uploadpack.allowFilter true
git -C "$T/distant.git" config uploadpack.allowAnySHA1InWant true
W="$T/travail"; git init -q -b main "$W"
pose() { mkdir -p "$W/$(dirname "$1")"; printf '%s' "$2" > "$W/$1"; (cd "$W/$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256"); }
# main jouet : registre avec la ligne ISSUE-MOTS-ET-COUT-T06
mkdir -p "$W/registres"; printf 'contenu jouet issue\n' > "$T/issue.json"; HI=$(sha256sum "$T/issue.json" | cut -d' ' -f1)
printf '# jouet\n\n| ISSUE-MOTS-ET-COUT-T06 | 2026-11-17T09:00:01Z | diag/%s/issue-mots-et-cout-t06.json | %s |\n' "$RMC" "$HI" > "$W/registres/scellements-v1.md"
git -C "$W" add -A && git -C "$W" commit -q -m "main jouet" && git -C "$W" push -q "$T/distant.git" main
# branche jouet de 7b
git -C "$W" switch -q --orphan calcul/t06-confirmation-7b-v1; git -C "$W" rm -rq . 2>/dev/null
for f in diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json runs/$R6/manifeste.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do pose "$f" "jouet $f"; done
pose diag/$R6/lecture-sondes-t06.json "jouet fermé"; git -C "$W" add -A && git -C "$W" commit -q -m 7b && git -C "$W" push -q "$T/distant.git" calcul/t06-confirmation-7b-v1
# branche jouet de l'étape A, avec un fichier découpé en trois morceaux
git -C "$W" switch -q --orphan donnees/t07-etape-a-v1; git -C "$W" rm -rq . 2>/dev/null; rm -rf "$W/diag" "$W/runs" "$W/donnees"
pose runs/$R7/manifeste.json "jouet manifeste t07"; pose diag/$R7/sondes-t07.json "jouet sondes t07"
D="$W/donnees/$R7"; mkdir -p "$D"; head -c 250000 /dev/urandom > "$T/scores.npz"; (cd "$T" && sha256sum scores.npz | sed 's/scores.npz/scores-actions-t07.npz/' > "$D/scores-actions-t07.npz.sha256")
split -b 100000 -d -a 3 "$T/scores.npz" "$D/scores-actions-t07.npz.morceau-"
for m in "$D"/scores-actions-t07.npz.morceau-*; do (cd "$D" && sha256sum "$(basename "$m")" > "$(basename "$m").sha256"); done
"$PY" -B - "$D" <<'FIN'
import hashlib, json, pathlib, sys
d = pathlib.Path(sys.argv[1]); ms = sorted(d.glob("scores-actions-t07.npz.morceau-[0-9][0-9][0-9]"))
m = {"octets": sum(p.stat().st_size for p in ms), "morceaux": [{"fichier": p.name, "octets": p.stat().st_size,
     "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in ms]}
(d / "scores-actions-t07.npz.morceaux.json").write_text(json.dumps(m), encoding="utf-8")
FIN
(cd "$D" && sha256sum scores-actions-t07.npz.morceaux.json > scores-actions-t07.npz.morceaux.json.sha256)
git -C "$W" add -A && git -C "$W" commit -q -m "etape A" && git -C "$W" push -q "$T/distant.git" donnees/t07-etape-a-v1
# branche jouet de la phase B portant le fichier « mots et coût »
git -C "$W" switch -q --orphan verdict/t06-mots-et-cout-compte-3-v1; git -C "$W" rm -rq . 2>/dev/null; rm -rf "$W/diag" "$W/runs" "$W/donnees"
mkdir -p "$W/diag/$RMC"; cp "$T/issue.json" "$W/diag/$RMC/issue-mots-et-cout-t06.json"; (cd "$W/diag/$RMC" && sha256sum issue-mots-et-cout-t06.json > issue-mots-et-cout-t06.json.sha256)
git -C "$W" add -A && git -C "$W" commit -q -m "phase B" && git -C "$W" push -q "$T/distant.git" verdict/t06-mots-et-cout-compte-3-v1
TETE_7B=$(git -C "$T/distant.git" rev-parse calcul/t06-confirmation-7b-v1); TETE_EA=$(git -C "$T/distant.git" rev-parse donnees/t07-etape-a-v1)
# dépôt de la session jouet, sur une branche neuve de la phase C
DEP="$T/depot"; git clone -q "$T/distant.git" "$DEP"; git -C "$DEP" switch -q -c verdict/t07-etape-b-compte-3-v1
BAC="$T/bac"; mkdir -p "$BAC"; HS=$(sha256sum "$T/scores.npz" | cut -d' ' -f1); HSO=$(cd "$W" && git show donnees/t07-etape-a-v1:diag/$R7/sondes-t07.json | sha256sum | cut -d' ' -f1)
cat > "$BAC/variables-v1.sh" <<EOF
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
arret() { echo "ARRÊT : \$*"; exit 1; }
DEPOT='$DEP'; BAC='$BAC'; PY='$PY'; R6=$R6; R7=$R7
B7B=calcul/t06-confirmation-7b-v1; TETE_7B=$TETE_7B; BEA=donnees/t07-etape-a-v1; TETE_EA=$TETE_EA
BR_P=verdict/t06-mots-et-cout-compte-3-v1; BR_B=verdict/t07-etape-b-compte-3-v1; DEPOT_URL='file://$T/distant.git'
CLONE7B="\$BAC/clone-7b-v1"; CLONEEA="\$BAC/clone-etape-a-v1"; MORCEAUX="\$BAC/morceaux-scores-v1"
EOF
# extraction du bloc C2 de la commande, deux empreintes réelles remplacées par celles des jouets, chemin des variables
"$PY" -B - "$CMD" "$T/bloc-c2.sh" "$HS" "$HSO" "$BAC/variables-v1.sh" <<'FIN'
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
b = [x for x in re.findall(r"```bash\n(.*?)```", t, re.S) if "place() {" in x]
assert len(b) == 1, "bloc C2 introuvable"
import hashlib
print("bloc C2 répété (texte extrait de la commande, avant substitution) : " + hashlib.sha256(b[0].encode("utf-8")).hexdigest())
c = b[0].replace("13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d", sys.argv[3])
c = c.replace("aa6892320f130e96af45e4e70b542b7ccfcea3ccd23d2fdc3e722b5637affa95", sys.argv[4])
c = c.replace('"$HOME/bac-lecture-7b-etape-b-compte-3-v1/variables-v1.sh"', '"' + sys.argv[5] + '"')
open(sys.argv[2], "w", encoding="utf-8").write(c)
print("bloc C2 extrait ; substitutions : 2 empreintes, 1 chemin")
FIN
OK=0; KO=0
verif() { if [ "$2" = "$3" ] && printf '%s' "$4" | grep -qF -- "$5"; then OK=$((OK+1)); echo "conforme : $1"; else KO=$((KO+1)); echo "ÉCART : $1 (code $2, attendu $3)"; printf '%s\n' "$4" | sed 's/^/    /' | tail -15; fi; }
S=$(bash "$T/bloc-c2.sh" 2>&1); verif "R1 premier passage du bloc C2" $? 0 "$S" "scores recomposés égaux à la ligne SCORES-T07"
printf '%s' "$S" | grep -qF "3 morceaux conformes, 250000 octets" && { OK=$((OK+1)); echo "conforme : R1b trois morceaux, 250000 octets"; } || { KO=$((KO+1)); echo "ÉCART : R1b"; }
printf '%s' "$S" | grep -qF "fichier « mots et coût » présent, compagnon égal" && { OK=$((OK+1)); echo "conforme : R1c fichier « mots et coût » pris sur la branche de la phase B"; } || { KO=$((KO+1)); echo "ÉCART : R1c"; }
[ -z "$(git -C "$DEP" status --porcelain --untracked-files=no)" ] && [ ! -e "$DEP/diag/$R6/lecture-sondes-t06.json" ] && { OK=$((OK+1)); echo "conforme : R1d aucun fichier suivi changé ; fichier fermé non placé"; } || { KO=$((KO+1)); echo "ÉCART : R1d"; }
rm -f "$DEP/donnees/$R7/scores-actions-t07.npz"
S=$(bash "$T/bloc-c2.sh" 2>&1); verif "R2 bloc relancé (fichiers déjà placés, égaux)" $? 0 "$S" "déjà placé, égal"
printf 'altéré' >> "$DEP/diag/$R6/episodes-t06.json"
S=$(bash "$T/bloc-c2.sh" 2>&1); verif "A1 fichier placé altéré : arrêt" $? 1 "$S" "existe et diffère du blob"
git -C "$T/distant.git" update-ref refs/heads/calcul/t06-confirmation-7b-v1 "$(git -C "$T/distant.git" rev-parse donnees/t07-etape-a-v1)"
S=$(bash "$T/bloc-c2.sh" 2>&1); verif "A2 tête de la branche de 7b autre : arrêt" $? 1 "$S" "tête de calcul/t06-confirmation-7b-v1"
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "RÉPÉTITION DU BLOC C2 : TOUT CONFORME" || echo "RÉPÉTITION DU BLOC C2 : ÉCARTS"
date -u +"fin de la répétition : %Y-%m-%dT%H:%M:%SZ"
