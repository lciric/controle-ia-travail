#!/usr/bin/env bash
# Essai (règle R5) de controle_a_blanc_etape_b_compte_3_v1.py : cas sains et artefacts, sur une racine jouet fabriquée dans
# un dossier neuf, plus un cas sur une copie des registres réels (racine = le dépôt, en lecture seule : hachage seul).
# Écrit le 2026-11-14 par le préparateur neuf (modèle A). N'écrit rien dans le dépôt ; aucune sortie de 7a, 7b ou T0.7 n'est
# ouverte (le cas réel ne fait que hacher les fichiers cités par le registre, absents du dépôt à cette date).
#     bash essai_controle_a_blanc_etape_b_compte_3_v1.sh <dépôt> <bac neuf> [<python avec numpy>]
set -u
DEPOT=$(cd "$1" && pwd); BAC="$2"; PY="${3:-$DEPOT/.venv/bin/python}"
[ ! -e "$BAC" ] || { echo "ARRÊT : $BAC existe déjà"; exit 1; }
mkdir -p "$BAC"; BAC=$(cd "$BAC" && pwd)
SCRIPT="$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1/controle_a_blanc_etape_b_compte_3_v1.py"
CONFIG="$DEPOT/prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json"
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
R6=20261111-151701-t06-reel; R7=20261114-001352-t07-lecture-reel; RMC=20261117-000000-t06-mots-et-cout
date -u +"début de l'essai : %Y-%m-%dT%H:%M:%SZ"
echo "script essayé : $(sha256sum "$SCRIPT" | cut -d' ' -f1)"
OK=0; KO=0
fabriquer() {   # $1 : dossier de la racine jouet (neuf)
"$PY" -B - "$1" "$DEPOT" <<'FIN'
import hashlib, pathlib, shutil, sys
R, D = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
R6, R7, RMC = "20261111-151701-t06-reel", "20261114-001352-t07-lecture-reel", "20261117-000000-t06-mots-et-cout"
def poser(rel, contenu: bytes):
    p = R / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(contenu)
    h = hashlib.sha256(contenu).hexdigest(); (R / (rel + ".sha256")).write_text(f"{h}  {p.name}\n", encoding="utf-8"); return h
lignes = []
def ligne(cle, date, rel, contenu=None, h=None):
    h = h or poser(rel, contenu if contenu is not None else f"jouet {cle}\n".encode())
    lignes.append(f"| {cle} | {date} | {rel} | {h} |")
    return h
ligne("SCELLEMENT-JEUX-T07-JD", "2026-11-10T08:22:50Z", "donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl")
ligne("GEL-T08", "2026-11-10T14:57:57Z", "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md")
code = (D / "registres/code-t07/CODE-T07-v3.json").read_bytes()
ligne("CODE-T07", "2026-11-13T23:42:46Z", "registres/code-t07/CODE-T07-v3.json", code)
ligne("SCELLEMENT-T07", "2026-11-11T07:11:42Z", "prereg/T0.7-sondes-v0-v1.md")
ligne("CONSIGNE-AUDIT-FUITES-T07", "2026-11-11T14:08:06Z", "prereg/T0.7-consigne-audit-fuites-v1.md")
ligne("SCELLEMENT-P3BIS", "2026-11-11T15:52:30Z", "prereg/P3-bis-temoin-positif-v1.md")
ligne("RUN-CONFIRMATION-T06", "2026-11-13T18:52:43Z", f"runs/{R6}/manifeste.json")
go = "| GO-2026-11-10-06 | ligne de GO jouet |"
(R / "registres").mkdir(parents=True, exist_ok=True); (R / "registres/go.md").write_text("# GO jouet\n\n" + go + "\n", encoding="utf-8")
ligne("GO-LECTURE-T07", "2026-11-13T18:52:44Z", "registres/go-extraits/GO-LECTURE-T07-v1.md", (go + "\n").encode())
s_scores = ligne("SCORES-T07", "2026-11-14T01:55:05Z", f"donnees/{R7}/scores-actions-t07.npz")
s_sondes = ligne("SONDES-T07", "2026-11-14T01:55:05Z", f"diag/{R7}/sondes-t07.json")
ligne("VERDICT-P3BIS", "2026-11-14T10:30:38Z", "docs/verdicts/verdict-P3-bis-v1-issue.json")
ligne("AUDIT-FUITES-T07", "2026-11-16T12:00:00Z", f"diag/{R7}/audit-fuites-t07.json")
ligne("LECTURE-T08-BASE-A", "2026-11-17T09:00:00Z", f"diag/{RMC}/base-a-t08.json")
ligne("CODE-MOTS-ET-COUT-T06", "2026-11-16T18:00:00Z", "docs/notes/jouet/code-mots-et-cout.json")
ligne("ISSUE-MOTS-ET-COUT-T06", "2026-11-17T09:00:01Z", f"diag/{RMC}/issue-mots-et-cout-t06.json")
(R / "registres/scellements-v1.md").write_text("# Registre jouet\n\n" + "\n".join(lignes) + "\n", encoding="utf-8")
shutil.copy(D / "registres/scellements-v1.md.ouvertures.md", R / "registres/scellements-v1.md.ouvertures.md")
p = "0" * 64 + " " + "1" * 64
(R / "registres/ouvertures-p3bis-v1.md").write_text(
    "| clé | date | mode | appui | paquets | motif |\n|---|---|---|---|---|---|\n"
    f"| OUVERTURE-P3BIS | 2026-11-14T10:15:23Z | pleine | SCORES-T07={s_scores} SONDES-T07={s_sondes} | {p} | - |\n", encoding="utf-8")
for rel in (f"diag/{R6}/lecture-cout-t06.json", f"diag/{R6}/episodes-t06.json", f"donnees/{R6}/mesures-t06.npz",
            f"donnees/{R6}/textes-actions-t06.jsonl", f"runs/{R7}/manifeste.json"):
    poser(rel, f"jouet {rel}\n".encode())
h = poser("prereg/T0.7-etape-b-bis-v1.md", b"plan jouet de l'etape B bis\n")
(R / "registres/etape-b-bis-v1.md").write_text(
    "# Registre propre jouet\n\n" + f"| SCELLEMENT-PLAN-BBIS | 2026-11-17T08:00:00Z | prereg/T0.7-etape-b-bis-v1.md | {h} |\n", encoding="utf-8")
print("racine jouet fabriquée")
FIN
}
cas() {   # $1 nom ; $2 code attendu ; $3 motif attendu dans la sortie ; puis les arguments du script
    local nom="$1" attendu="$2" motif="$3"; shift 3
    local sortie code
    sortie=$(PYTHONPATH="$DEPOT/src" "$PY" -B "$SCRIPT" "$@" 2>&1); code=$?
    if [ "$code" = "$attendu" ] && printf '%s' "$sortie" | grep -qF -- "$motif"; then
        OK=$((OK + 1)); echo "conforme : $nom (code $code ; « $motif »)"
    else
        KO=$((KO + 1)); echo "ÉCART : $nom (code $code, attendu $attendu ; motif « $motif »)"; printf '%s\n' "$sortie" | sed 's/^/    /' | tail -25
    fi
}
neuf() { local d="$BAC/$1"; fabriquer "$d" >/dev/null || { echo "ARRÊT : fabrication"; exit 1; }; echo "$d"; }
INSTANT=2026-11-18T12:00:00Z
args() { echo --racine "$1" --registre "$1/registres/scellements-v1.md" --config "$CONFIG" --instant "$INSTANT" \
              --registre-bbis "$1/registres/etape-b-bis-v1.md" --cle-bbis SCELLEMENT-PLAN-BBIS; }

J=$(neuf s1); cas "S1 racine saine, mode avant-etape-b" 0 "TOUT CONFORME" $(args "$J") --mode avant-etape-b
cas "S1b même racine : clés à marque T06 et T08 ignorées" 0 "'GEL-T08', 'LECTURE-T08-BASE-A', 'CODE-MOTS-ET-COUT-T06'" $(args "$J") --mode avant-etape-b
cas "S1c même racine : condition d'ordre B bis remplie" 0 "condition d'ordre B bis (SCELLEMENT-PLAN-BBIS) : REMPLIE" $(args "$J") --mode avant-etape-b
J=$(neuf a1); echo "| SCELLEMENT-VADAPT | 2026-11-14T09:45:18Z | prereg/T0.7-sondes-v0-v1.md | $(cut -d' ' -f1 "$J/prereg/T0.7-sondes-v0-v1.md.sha256") |" >> "$J/registres/scellements-v1.md"
cas "A1 clé sans marque déclarée (VADAPT) au registre de T0.7" 2 "ligne SCELLEMENT-VADAPT ni exigée ni permise" $(args "$J")
J=$(neuf a2); echo "| SCELLEMENT-JEUX-T08-JD | 2026-11-14T09:45:18Z | prereg/T0.7-sondes-v0-v1.md | $(cut -d' ' -f1 "$J/prereg/T0.7-sondes-v0-v1.md.sha256") |" >> "$J/registres/scellements-v1.md"
cas "A2 famille des jeux sous une autre marque (règle (3) restreinte)" 2 "règle (3) restreinte" $(args "$J")
J=$(neuf a3); rm "$J/registres/etape-b-bis-v1.md"
cas "A3 registre propre de B bis absent (avant-etape-b)" 2 "plan de l'étape B bis non scellé" $(args "$J") --mode avant-etape-b
cas "A3b même cas en mode rapport : manque, pas refus" 0 "MANQUE : condition d'ordre B bis non remplie" $(args "$J")
J=$(neuf a4); sed -i 's/2026-11-17T08:00:00Z/2026-11-19T08:00:00Z/' "$J/registres/etape-b-bis-v1.md"
cas "A4 plan de B bis daté après l'instant d'ouverture" 2 "pas strictement antérieure" $(args "$J") --mode avant-etape-b
J=$(neuf a5); echo "ajout" >> "$J/prereg/T0.7-etape-b-bis-v1.md"
cas "A5 plan de B bis altéré après son scellement" 2 "compagnon .sha256" $(args "$J") --mode avant-etape-b
J=$(neuf a6); grep '^| SCELLEMENT-PLAN-BBIS ' "$J/registres/etape-b-bis-v1.md" >> "$J/registres/scellements-v1.md"
cas "A6 ligne de B bis écrite aussi au registre de T0.7" 2 "SCELLEMENT-PLAN-BBIS ni exigée ni permise" $(args "$J") --mode avant-etape-b
J=$(neuf a7)
cas "A7 registre de B bis = registre de T0.7" 2 "c'est un registre que lit T0.7" --racine "$J" --registre "$J/registres/scellements-v1.md" --config "$CONFIG" --instant "$INSTANT" --registre-bbis "$J/registres/scellements-v1.md" --cle-bbis SCELLEMENT-PLAN-BBIS
J=$(neuf a8); sed -i 's/| VERDICT-P3BIS | 2026-11-14T10:30:38Z/| VERDICT-P3BIS | 2026-11-14T01:00:00Z/' "$J/registres/scellements-v1.md"
cas "A8 VERDICT-P3BIS avant SCORES-T07 et SONDES-T07" 2 "pas strictement antérieure(s) à VERDICT-P3BIS" $(args "$J")
J=$(neuf a9); sed -i 's/| AUDIT-FUITES-T07 | 2026-11-16T12:00:00Z/| AUDIT-FUITES-T07 | 2026-11-11T12:00:00Z/' "$J/registres/scellements-v1.md"
cas "A9 AUDIT-FUITES-T07 avant sa consigne" 2 "CONSIGNE-AUDIT-FUITES-T07 pas strictement antérieure(s) à AUDIT-FUITES-T07" $(args "$J")
J=$(neuf a10); echo '{}' > "$J/diag/$R7/lecture-t07.json"
cas "A10 lecture-t07.json déjà écrite" 2 "lecture décisive déjà écrite" $(args "$J")
J=$(neuf a11); echo '{}' > "$J/diag/$R6/lecture-sondes-t06.json"
cas "A11 lecture-sondes-t06.json présent sous la racine" 2 "fichier fermé de T0.6 présent" $(args "$J")
J=$(neuf a12); sed -i '/^| ISSUE-MOTS-ET-COUT-T06 /d' "$J/registres/scellements-v1.md"
cas "A12 ISSUE-MOTS-ET-COUT-T06 absente (avant-etape-b)" 2 "0 ligne(s) ISSUE-MOTS-ET-COUT-T06" $(args "$J") --mode avant-etape-b
cas "A12b même cas en mode rapport" 0 "AUCUN REFUS ; MANQUES LISTÉS" $(args "$J")
J=$(neuf a13); grep '^| SCORES-T07 ' "$J/registres/scellements-v1.md" > "$BAC/ligne-a13.txt"; cat "$BAC/ligne-a13.txt" >> "$J/registres/scellements-v1.md"
cas "A13 SCORES-T07 en double" 2 "2 ligne(s) SCORES-T07" $(args "$J")
J=$(neuf a14); echo "0000000000000000000000000000000000000000000000000000000000000000  mesures-t06.npz" > "$J/donnees/$R6/mesures-t06.npz.sha256"
cas "A14 compagnon des mesures de 7b faux" 2 "mesures-t06.npz : compagnon ≠" $(args "$J")
J=$(neuf a15); cp "$CONFIG" "$BAC/config-alteree.json"; printf ' ' >> "$BAC/config-alteree.json"
cas "A15 configuration de T0.7 altérée" 2 "configuration v8 scellée" --racine "$J" --registre "$J/registres/scellements-v1.md" --config "$BAC/config-alteree.json" --instant "$INSTANT"
J=$(neuf a16)
cas "A16 instant d'ouverture avant la ligne ISSUE-MOTS-ET-COUT-T06" 2 "pas strictement antérieure à l'ouverture" --racine "$J" --registre "$J/registres/scellements-v1.md" --config "$CONFIG" --instant 2026-11-17T09:00:01Z --registre-bbis "$J/registres/etape-b-bis-v1.md" --cle-bbis SCELLEMENT-PLAN-BBIS
J=$(neuf a17)
cas "A17 clé de B bis hors forme" 2 "hors de la forme" $(args "$J" | sed 's/SCELLEMENT-PLAN-BBIS/plan-bbis/') --mode avant-etape-b
J=$(neuf a18); sed -i 's/| pleine | SCORES-T07=/| pleine | SCORES-T07=0000/' "$J/registres/ouvertures-p3bis-v1.md"
cas "A18 journal de P3-bis : appui faux" 2 "garde adaptée" $(args "$J")
J=$(neuf a19); printf '%s\n' "| OUVERTURE-P3BIS | 2026-11-14T00:00:00Z | pleine | SCORES-T07=$(printf '0%.0s' $(seq 64)) SONDES-T07=$(printf '0%.0s' $(seq 64)) | $(printf '0%.0s' $(seq 64)) $(printf '1%.0s' $(seq 64)) | - |" > "$BAC/ligne-a19.txt"
{ head -n 2 "$J/registres/ouvertures-p3bis-v1.md"; cat "$BAC/ligne-a19.txt"; } > "$BAC/journal-a19.md"; cp "$BAC/journal-a19.md" "$J/registres/ouvertures-p3bis-v1.md"
cas "A19 ouverture pleine de P3-bis avant la fin de l'étape A" 2 "pleine-avant-fin-A" $(args "$J")
J=$(neuf a20); Z=$(printf '0%.0s' $(seq 64)); U=$(printf '1%.0s' $(seq 64))
{ head -n 2 "$J/registres/ouvertures-p3bis-v1.md"; echo "| OUVERTURE-P3BIS | 2026-11-14T00:00:00Z | reduite | RENDEZ-VOUS-P3BIS-1=$Z GARDE-ADAPTEE-T07-P3BIS=$Z | $Z $U | - |"; tail -n 1 "$J/registres/ouvertures-p3bis-v1.md"; } > "$BAC/journal-a20.md"; cp "$BAC/journal-a20.md" "$J/registres/ouvertures-p3bis-v1.md"
cas "A20 ouverture réduite au journal de P3-bis : chemin non couvert, nœud" 2 "ouverture réduite au journal de P3-bis" $(args "$J")
# cas réel : copie des registres de main, racine = le dépôt (lecture seule ; les fichiers de 7b et de T0.7 n'y sont pas)
C="$BAC/reel"; mkdir -p "$C/registres"; cp "$DEPOT/registres/scellements-v1.md" "$DEPOT/registres/scellements-v1.md.ouvertures.md" "$C/registres/"
cas "R1 registres réels (copie) : aucun refus ; manques listés" 0 "refus du registre (hors clés manquantes) : aucun" --racine "$DEPOT" --registre "$C/registres/scellements-v1.md" --config "$CONFIG" --registre-bbis "$C/registres/etape-b-bis-v1.md" --cle-bbis SCELLEMENT-PLAN-BBIS
cas "R1b registres réels : manquent AUDIT-FUITES-T07 et ISSUE-MOTS-ET-COUT-T06" 0 "manquantes ['AUDIT-FUITES-T07', 'ISSUE-MOTS-ET-COUT-T06']" --racine "$DEPOT" --registre "$C/registres/scellements-v1.md" --config "$CONFIG"
cas "R1c registres réels, mode avant-etape-b : incomplet" 2 "INCOMPLET" --racine "$DEPOT" --registre "$C/registres/scellements-v1.md" --config "$CONFIG" --registre-bbis "$C/registres/etape-b-bis-v1.md" --cle-bbis SCELLEMENT-PLAN-BBIS --mode avant-etape-b
cmp -s "$DEPOT/registres/scellements-v1.md" "$C/registres/scellements-v1.md" && echo "registre réel inchangé (comparé à sa copie)"
echo "BILAN : $OK conformes sur $((OK + KO))"
[ "$KO" = 0 ] && echo "ESSAI : TOUT CONFORME" || echo "ESSAI : ÉCARTS"
date -u +"fin de l'essai : %Y-%m-%dT%H:%M:%SZ"
