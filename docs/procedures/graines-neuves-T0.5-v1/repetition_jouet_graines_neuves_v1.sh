#!/usr/bin/env bash
# Répétition jouet, hors réseau, de la chaîne de l'instance pour la course T0.5 « graines neuves » (ETUDE=pilote,
# MODE=jouet), au commit C de la branche prep/t05-graines-neuves-v1. Copie réduite de
# docs/procedures/pilote-T0.5-v1/repetition_jouet_pilote_v1.sh (pilote, 12 octobre 2026). Dépôt jetable cloné de C (une
# seule branche), dépôt nu local en guise de dépôt distant, jetons factices, env -i ; aucun service de location, ni GitHub,
# ni Hugging Face (le mode jouet prend un modèle jouet et un tokeniseur par caractères).
# Dans le clone jetable seulement : deux tâches du lot A (les deux premières, objets identiques, identifiants « -g2 »)
# dans un fichier jouet scellé ; configuration jouet = celle du pilote, réduite comme `remplir_pilote_v1.py` en mode jouet ;
# fiche jouet = la fiche du lot A dont ne changent que PREREG, BRANCHE, configuration et tâches citées, nombre de tests
# attendus (suite collectée dans l'environnement local) et une contre-lecture factice ; entropie et commit cité inchangés.
# Passages :
#   1. cas sain : BRANCHE=calcul/t05-graines-neuves-jouet-a-v1 → code 0 attendu, résultats, traces et vecteurs poussés
#      sur le dépôt nu ; contrôles : 6 épisodes aux identifiants « -g2 », entropie du manifeste = entropie de la fiche ;
#   2. artefact : même branche, déjà présente → arrêt avant l'installation (code 2) ;
#   3. artefact : fiche jouet dont l'empreinte des tâches est fausse (re-scellée) → arrêt par la garde du lanceur Python,
#      avant le manifeste (code 1).
# PYTHONPATH_TESTS (facultatif) : dossier ajouté au PYTHONPATH des passages, pour lever des échecs de tests propres à
# l'environnement local (dit dans le journal ; l'instance installe requirements-gpu.txt).
# Usage : repetition_jouet_graines_neuves_v1.sh C RACINE_NEUVE VENV
set -uo pipefail
C=$1; R=$2; VENV=$3
D=/home/user/controle-ia-travail
PREP=prep/t05-graines-neuves-v1
PA=prereg/T0.5-graines-neuves-a-v1.md
PJ=prereg/T0.5-graines-neuves-jouet-v1.md
CFG=prereg/T0.5-pilote-config-v1.json; CJ=prereg/T0.5-graines-neuves-jouet-config-v1.json
TA=donnees/t05-graines-neuves-v1/taches-graines-neuves-a-30-v1.json; TJ=donnees/t05-graines-neuves-v1/taches-graines-neuves-jouet-2-v1.json
PY="$VENV/bin/python"
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local --single-branch --branch "$PREP" "$D" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
echo "commit du code répété : $(git rev-parse HEAD)"
echo "script répété : $(basename "$0") $(sha256sum "$0" | cut -d' ' -f1)"
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
for f in "$PA" "$TA" "$TA.sha256" scripts/amorce_instance_t05.sh scripts/pilote_t05_instance.sh; do
    [ -f "$f" ] || { echo "$f absent du commit $C"; exit 2; }
done
"$PY" -I - "$TA" "$TJ" "$CFG" "$CJ" <<'PYJ' || exit 2
import json, sys
ta, tj, cfg, cj = sys.argv[1:5]
src = json.load(open(ta, encoding="utf-8"))
corps = {"source": {"chemin": ta, "rangs": "0 à 1"}, "regle": "répétition jouet : deux premières tâches du lot A",
         "taches": src["taches"][:2]}
with open(tj, "x", encoding="utf-8") as f:
    json.dump(corps, f, ensure_ascii=False, indent=1); f.write("\n")
c = json.load(open(cfg, encoding="utf-8"))
c.update(mode="jouet", T=2, max_nouveaux=8, lot=2, couches=[0, 1, 2], max_nouveaux_juge=6, lot_juge=2, lot_appariement=4)
for spec in [c["agent"], *c["juges"]]:
    spec.pop("texte_attendu_ouverture", None)
with open(cj, "x", encoding="utf-8") as f:
    json.dump(c, f, ensure_ascii=False, indent=2); f.write("\n")
print("tâches jouet :", [t["identifiant"] for t in corps["taches"]])
PYJ
N=$(PYTHONPATH="src${PYTHONPATH_TESTS:+:$PYTHONPATH_TESTS}" "$PY" -m pytest --collect-only -q -p no:cacheprovider 2>/dev/null | sed -n 's/^\([0-9]*\) tests\{0,1\} collected.*/\1/p')
echo "tests collectés : $N"
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$TJ" "$CJ" > /dev/null || exit 2
SHA_TJ=$(cut -d' ' -f1 "$TJ.sha256")
CFG_J=$(PYTHONPATH=src "$PY" -c "import json, sys; from controle_ia.environnements.lancer_pilote_a import empreinte_config; print(empreinte_config(json.load(open(sys.argv[1]))))" "$CJ") || exit 2
fiche_jouet() {   # $1 sortie, $2 empreinte des tâches citée
    "$PY" -I - "$PA" "$1" "$CJ" "$CFG_J" "$TJ" "$2" "$N" <<'PYF'
import re, sys
pa, sortie, cj, cfg_j, tj, sha_tj, n = sys.argv[1:8]
t = open(pa, encoding="utf-8").read()
rep = [(r"`PREREG=prereg/T0\.5-graines-neuves-a-v1\.md`, `BRANCHE=calcul/t05-graines-neuves-a-v1`",
        f"`PREREG={sortie}`, `BRANCHE=calcul/t05-graines-neuves-jouet-a-v1`"),
       (r"Configuration du pilote \(empreinte canonique\) : `[0-9a-f]{64}`", f"Configuration du pilote (empreinte canonique) : `{cfg_j}`"),
       (r"Chemin de la configuration : `[^`]*`", f"Chemin de la configuration : `{cj}`"),
       (r"Tâches du pilote : `[0-9a-f]{64}`", f"Tâches du pilote : `{sha_tj}`"),
       (r"Chemin des tâches : `[^`]*`", f"Chemin des tâches : `{tj}`"),
       (r"Tests attendus : `[0-9]+`", f"Tests attendus : `{n}`"),
       (r"## Contre-lecture\n.*", "## Contre-lecture\n\n- Contre-lecture 1 (factice, répétition jouet) : brouillon `"
        + "0" * 64 + "`, rapport `" + "1" * 64 + "`.\n")]
for motif, neuf in rep:
    t, k = re.subn(motif, lambda m: neuf, t, count=1, flags=re.S)
    if k != 1:
        sys.exit(f"substitution manquée : {motif}")
open(sortie, "x", encoding="utf-8").write("# FICHE JOUET (répétition hors réseau, jamais lancée sur une instance)\n\n" + t)
PYF
}
fiche_jouet "$PJ" "$SHA_TJ" || exit 2
PYTHONPATH=src "$PY" -c "import sys; from controle_ia.prereg import sceller_prereg; sceller_prereg(sys.argv[1])" "$PJ" || exit 2
PJF=prereg/T0.5-graines-neuves-jouet-fausse-v1.md
fiche_jouet "$PJF" "$(printf 'f%.0s' {1..64})" || exit 2
PYTHONPATH=src "$PY" -c "import sys; from controle_ia.prereg import sceller_prereg; sceller_prereg(sys.argv[1])" "$PJF" || exit 2
git add -f "$TJ" "$TJ.sha256" "$CJ" "$CJ.sha256" "$PJ" "$PJ.sha256" "$PJF" "$PJF.sha256" && git commit -qm "essai : fiches et tâches jouets" || exit 2
ESSAI=$(git rev-parse HEAD); echo "commit de l'essai : $ESSAI"
git clone -q --bare "$R/source" "$R/distant.git" || exit 2
cd "$R"
passage() {   # $1 nom, $2 PREREG, $3 BRANCHE
    local n=$1 p=$2 b=$3 debut code
    mkdir -p "$R/racine-$n"
    debut=$(date +%s)
    env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$R/racine-$n" COMMIT="$ESSAI" GH_TOKEN=factice HF_TOKEN=factice \
        ETUDE=pilote MODE=jouet DEPOT_URL="$R/distant.git" RACINE_AMORCE="$R/racine-$n" VENV_EXISTANT="$VENV" \
        ${PYTHONPATH_TESTS:+PYTHONPATH="$PYTHONPATH_TESTS"} \
        PREREG="$p" BRANCHE="$b" bash "$R/source/scripts/amorce_instance_t05.sh" > "$R/amorce-$n.log" 2>&1
    code=$?
    CODES="$CODES $n=$code"
    echo "passage $n : code $code ; durée $(( $(date +%s) - debut )) s"
    grep -h "^AMORCE" "$R/amorce-$n.log" 2>/dev/null | cut -c1-200 | sed 's/^/    | /'
    grep -h "début\|préenregistrement lu\|tests :\|run :\|run terminé\|vecteurs\|arrêt\|ARRÊT\|poussée\|branche" "$R"/racine-"$n"/t05/journal.txt 2>/dev/null | cut -c1-260 | sed 's/^/    | /'
    grep -h "GardeArret\|Error" "$R"/racine-"$n"/t05/run.err 2>/dev/null | tail -2 | cut -c1-260 | sed 's/^/    | run.err : /'
    rm -rf "$R/racine-$n/t05/controle-ia" "$R/racine-$n/amorce-depot"
}
CODES=""
passage 1-sain "$PJ" calcul/t05-graines-neuves-jouet-a-v1
passage 2-artefact-branche-presente "$PJ" calcul/t05-graines-neuves-jouet-a-v1
passage 3-artefact-taches-fausses "$PJF" calcul/t05-graines-neuves-jouet-c-v1
git -C "$R/distant.git" branch -a | sed 's/^/branche distante : /'
# contrôles du passage 1 sur le dépôt nu
rm -rf "$R/lecture" && git clone -q --branch calcul/t05-graines-neuves-jouet-a-v1 "$R/distant.git" "$R/lecture" || { echo "RÉPÉTITION : NON CONFORME (branche du passage 1 absente)"; exit 1; }
"$PY" -I - "$R/lecture" "$PJ" <<'PYC'
import glob, json, re, sys
from pathlib import Path
r, pj = Path(sys.argv[1]), sys.argv[2]
ent = re.search(r"Entropie : `([0-9]+)`", (r / pj).read_text(encoding="utf-8")).group(1)
man = sorted(glob.glob(str(r / "runs" / "*-t05-pilote-jouet" / "manifeste.json")))
ep = sorted(glob.glob(str(r / "diag" / "*-t05-pilote-jouet" / "episodes.json")))
res = sorted(glob.glob(str(r / "diag" / "*-t05-pilote-jouet" / "resume.json")))
ok = len(man) == 1 and len(ep) == 1 and len(res) == 1
if ok:
    m = json.load(open(man[0], encoding="utf-8"))
    graines = m["graines"]
    entropies = {g["entropie"] for g in graines.values()}
    fiches = json.load(open(ep[0], encoding="utf-8"))["resultat"]["fiches"]
    ids = sorted({f["tache"] for f in fiches})
    s = json.load(open(res[0], encoding="utf-8"))["resultat"]
    print("manifeste : entropies", sorted(entropies), "; décisif", m.get("decisif"), "; prereg", m.get("prereg"))
    print("épisodes :", len(fiches), "; tâches :", ids)
    print("résumé : épisodes", s["episodes"], "; notations", {k: v["n"] for k, v in s["notations"].items()})
    ok = (entropies == {ent} and len(fiches) == 6 and all(i.endswith("-g2") for i in ids) and len(ids) == 2
          and all(k.split("/")[0].endswith("-g2") for k in graines if "/" in k and not k.startswith("juge-")))
print("contrôles du passage 1 :", "CONFORMES" if ok else "NON CONFORMES")
sys.exit(0 if ok else 1)
PYC
c=$?
echo "codes des passages :$CODES (attendus : 1-sain=0 2-artefact-branche-presente=2 3-artefact-taches-fausses=1)"
if [ "$c" = 0 ] && [ "$CODES" = " 1-sain=0 2-artefact-branche-presente=2 3-artefact-taches-fausses=1" ]; then
    echo "RÉPÉTITION JOUET : CONFORME"
else
    echo "RÉPÉTITION JOUET : NON CONFORME"; exit 1
fi
