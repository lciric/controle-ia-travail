#!/usr/bin/env bash
# Banc du contrôle des traces de la session de P4-instrument, controler_traces_p4_v1.sh (R5 : cas sain et artefacts),
# v1, neuf (chaîne v2, RC-donnees-06). Copie jouée : seules les lignes DEPOT et TEXTES_SHA256 changent (deux lignes,
# comptées) : un faux dépôt porte, au chemin des textes de P3, les textes synthétiques des fenêtres
# (outils_essais_p4_v1.py fenetres ; aucun texte de P3 n'est lu) et leur sceau. Dossier de traces sain fabriqué à la
# forme de celui de la session (lancement, contrôles, surveillance, cinq minutes, arrêt, récupération ; lignes AMORCE et
# PROGRES ; un tableau .npz ; un résultat JSON). Artefacts : texte brut dans le journal relevé par la surveillance ;
# texte échappé en JSON dans un sous-dossier ; texte sans sa fenêtre du milieu ; texte échappé par Python ; texte dans
# une chaîne d'un tableau ; tableau illisible ; jeton GitHub dans les contrôles ; jeton Hugging Face dans les états.
# Refus en code 2 (rien n'est cherché) : jetons absents ; textes absents, d'une autre empreinte ou sans sceau ; dossier
# absent ; textes dans le dossier contrôlé ; usage faux ; module commun absent. Chaque cas vérifie aussi que le dossier
# contrôlé n'est pas modifié et qu'aucun texte ni jeton n'est affiché. Chaîne v3 (VC2-donnees-02) : lien symbolique dans
# les traces (vers un fichier sain, vers un fichier hors du dossier qui porte un texte, vers un dossier) et tube nommé :
# code 1, chemin écrit, rien n'est suivi ni lu (aucune fenêtre retrouvée par le lien), rien n'est versé.
# Usage : essais_traces_p4_v1.sh RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré
E=$(realpath -m "${1:?racine neuve}")
HN=${HN:-/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4}
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
CT=$HN/controler_traces_p4_v1.sh
export PYTHONDONTWRITEBYTECODE=1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E" || exit 2
for s in controler_traces_p4_v1.sh verifications_p4_v1.py outils_essais_p4_v1.py; do echo "script éprouvé : $s $(sha256sum "$HN/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
TEXTES=donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
F="$E/depot/$TEXTES"
"$PY" -B "$HN/outils_essais_p4_v1.py" fenetres "$F" > "$E/fenetres.txt" 2>&1 || { echo "textes synthétiques impossibles : $(tail -1 "$E/fenetres.txt")"; exit 2; }
SHA=$(sha256sum "$F" | cut -d' ' -f1)
(cd "$(dirname "$F")" && sha256sum "$(basename "$F")" > "$(basename "$F").sha256")
copie() {   # $1 sortie, $2 dépôt, $3 empreinte des textes
    sed -e "s|^DEPOT=.*|DEPOT=$2|" -e "s|^TEXTES_SHA256=[0-9a-f]\{64\} |TEXTES_SHA256=$3 |" "$CT" > "$1"
    [ "$(diff "$CT" "$1" | grep -c '^>')" = 2 ] || { echo "copie $1 : deux lignes changées attendues"; exit 2; }
}
copie "$E/controle-essai.sh" "$E/depot" "$SHA"
echo "lignes changées dans la copie du contrôle des traces : 2 (DEPOT, TEXTES_SHA256)"
JT=factice-hf-traces-0001; JG=factice-gh-traces-0001
fabriquer() {   # $1 dossier neuf, $2 programme Python ajouté (T : textes honnêtes non dégénérés ; D : dossier)
    mkdir -p "$1" && "$PY" -I -B - "$F" "$1" "$2" <<'PYF' || { echo "fabrication impossible : $1"; exit 2; }
import json, sys
from pathlib import Path
import numpy as np
tx, d, prog = sys.argv[1:4]
T = [json.loads(l)["texte"] for l in open(tx, encoding="utf-8") if json.loads(l)["condition"] == "honnete" and len(set(json.loads(l)["texte"])) > 1]
D = Path(d)
for sous in ("lancement", "surveillance/arret", "cinq-minutes", "recuperation"):
    (D / sous).mkdir(parents=True, exist_ok=True)
(D / "lancement/lancement.txt").write_text("commit 0123456789abcdef0123456789abcdef01234567\ncreation 1760000000\nsuccès : True ; identifiant 99999999 ; message : essai\n", encoding="utf-8")
(D / "lancement/controles.txt").write_text("OK  essai\nCONTRÔLES AVANT DÉPENSE : TOUS CONFORMES\n", encoding="utf-8")
(D / "lancement/offres-relues.json").write_text(json.dumps([{"id": 4242, "dph_total": 1.09}]), encoding="utf-8")
(D / "surveillance/etats.txt").write_text("2026-10-20T20:00:00Z actual_status=running cur_state=running intended_status=running status_msg=essai\n", encoding="utf-8")
(D / "surveillance/journal-dernier.txt").write_text("AMORCE 2026-10-20T20:00:00Z : commit 0123456789abcdef0123456789abcdef01234567\n"
    "PROGRES 2026-10-20T20:30:00Z etape=M5 conforme=True\n" + "." * 120 + "\nAMORCE 2026-10-20T21:00:00Z : fin, code 0\n", encoding="utf-8")
(D / "surveillance/arret/ligne-arrets.md").write_text("| 2026-10-20 | instance 99999999 (étiquette p4-v1) | P4-instrument | essai |\n", encoding="utf-8")
(D / "cinq-minutes/controle-5min.txt").write_text("CONTRÔLE À CINQ MINUTES : CONFORME\n", encoding="utf-8")
(D / "recuperation/sortie.txt").write_text("RÉCUPÉRATION : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)\n", encoding="utf-8")
with open(D / "recuperation/tableau.npz", "wb") as f:
    np.savez(f, noms=np.array(["sonde-a", "sonde-b"]), x=np.zeros(2))
exec(prog)
PYF
}
NON_CONFORMES=0
empreinte_dossier() { (cd "$1" && find . -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum | cut -d' ' -f1); }
cas() {   # $1 nom, $2 code attendu, $3 motif de la dernière ligne, $4 dossier, $5 copie (défaut : copie d'essai), puis l'environnement
    local n=$1 a=$2 m=$3 x=$4 ctl=${5:-$E/controle-essai.sh} c v avant apres; shift 5
    avant=$( [ -d "$x" ] && empreinte_dossier "$x")
    env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$E" "$@" bash "$ctl" "$x" > "$E/sortie-$n.txt" 2>&1; c=$?
    apres=$( [ -d "$x" ] && empreinte_dossier "$x")
    v="CONFORME"
    [ "$c" = "$a" ] || v="NON CONF""ORME (code $c, attendu $a)"
    tail -1 "$E/sortie-$n.txt" | grep -qF -- "$m" || v="NON CONF""ORME (motif « $m » absent de la dernière ligne)"
    [ "$avant" = "$apres" ] || v="NON CONF""ORME (dossier contrôlé modifié)"
    grep -qF -e "$JT" -e "$JG" -e "zanzibar" -e "quokka" "$E/sortie-$n.txt" && v="NON CONF""ORME (jeton ou texte affiché)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; $v"
    tail -1 "$E/sortie-$n.txt" | couper 200 | sed 's/^/    | /'
}
J=(HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG GH_TOKEN=$JG)
fabriquer "$E/t/sain" "pass"
cas T00-traces-saines 0 "TRACES DE LA SESSION : CONFORMES (aucune fenêtre d'un texte honnête, aucun jeton, aucune entrée non ordinaire) : versement permis" "$E/t/sain" "" "${J[@]}"
fabriquer "$E/t/brut" "(D / 'surveillance/journal-dernier.txt').write_text('----- /root/p4/run.err\\n' + T[0] + '\\n', encoding='utf-8')"
cas T01-texte-brut-dans-le-journal-releve 1 "RIEN N'EST VERSÉ" "$E/t/brut" "" "${J[@]}"
fabriquer "$E/t/json" "(D / 'recuperation/profond').mkdir(); (D / 'recuperation/profond/x.txt').write_text(json.dumps(T[3]), encoding='utf-8')"
cas T02-texte-echappe-en-json-dans-un-sous-dossier 1 "RIEN N'EST VERSÉ" "$E/t/json" "" "${J[@]}"
fabriquer "$E/t/milieu" "m = (len(T[1]) - 48) // 2; (D / 'lancement/controles.txt').write_text(T[1][:m] + ' [...] ' + T[1][m + 48:], encoding='utf-8')"
cas T03-texte-sans-sa-fenetre-du-milieu 1 "RIEN N'EST VERSÉ" "$E/t/milieu" "" "${J[@]}"
fabriquer "$E/t/repr" "(D / 'cinq-minutes/etat.txt').write_text(repr(T[4]), encoding='utf-8')"
cas T04-texte-echappe-par-python 1 "RIEN N'EST VERSÉ" "$E/t/repr" "" "${J[@]}"
fabriquer "$E/t/npz" "np.savez(open(D / 'recuperation/tableau.npz', 'wb'), noms=np.array(['sonde-a', T[2]]), x=np.zeros(2))"
cas T05-texte-dans-un-tableau 1 "RIEN N'EST VERSÉ" "$E/t/npz" "" "${J[@]}"
fabriquer "$E/t/illisible" "(D / 'recuperation/tableau.npz').write_bytes(b'pas un tableau')"
cas T06-tableau-illisible 1 "RIEN N'EST VERSÉ" "$E/t/illisible" "" "${J[@]}"
fabriquer "$E/t/jeton-gh" "(D / 'lancement/controles.txt').write_text('fuite $JG\\n', encoding='utf-8')"
cas T07-jeton-github-dans-les-controles 1 "RIEN N'EST VERSÉ" "$E/t/jeton-gh" "" "${J[@]}"
fabriquer "$E/t/jeton-hf" "(D / 'surveillance/etats.txt').write_text('illisible : $JT\\n', encoding='utf-8')"
cas T08-jeton-hugging-face-dans-les-etats 1 "RIEN N'EST VERSÉ" "$E/t/jeton-hf" "" "${J[@]}"
grep -q "jeton retrouvé : .*etats.txt (HF_TOKEN, 1 occurrence(s))" "$E/sortie-T08-jeton-hugging-face-dans-les-etats.txt" && echo "    T08 : fichier et nom du jeton écrits, valeur jamais : CONFORME" \
    || { echo "    T08 : relevé du jeton : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# chaîne v3 (VC2-donnees-02) : entrées non ordinaires dans les traces : refus (code 1), chemin écrit, rien n'est suivi
mkdir -p "$E/hors-traces" && "$PY" -I -B -c 'import json, sys
T = [json.loads(l)["texte"] for l in open(sys.argv[1], encoding="utf-8") if json.loads(l)["condition"] == "honnete" and len(set(json.loads(l)["texte"])) > 1]
open(sys.argv[2], "w", encoding="utf-8").write("trace hors du dossier : " + T[0] + "\n")' "$F" "$E/hors-traces/texte.txt" || exit 2
non_ordinaire() {   # $1 nom du cas, $2 entrée attendue (chemin relatif au dossier) : chemin écrit, aucune fenêtre retrouvée
    local n=$1 x=$2
    grep -qF "non ordinaire (lien symbolique ou autre, ni suivi ni lu) : $E/t/$n/$x" "$E/sortie-$n.txt" \
        && grep -q "entrées non ordinaires)" "$E/sortie-$n.txt" && ! grep -q "fenêtre(s) retrouvée(s)" "$E/sortie-$n.txt" \
        && echo "    $n : entrée non ordinaire écrite par son chemin, ni suivie ni lue : CONFORME" \
        || { echo "    $n : relevé de l'entrée non ordinaire : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
}
fabriquer "$E/t/T09-lien-vers-un-fichier-sain" "(D / 'lancement/lien.txt').symlink_to(D / 'lancement/controles.txt')"
cas T09-lien-vers-un-fichier-sain 1 "RIEN N'EST VERSÉ" "$E/t/T09-lien-vers-un-fichier-sain" "" "${J[@]}"
non_ordinaire T09-lien-vers-un-fichier-sain lancement/lien.txt
fabriquer "$E/t/T09b-lien-vers-un-texte-hors-du-dossier" "(D / 'recuperation/lien.txt').symlink_to('$E/hors-traces/texte.txt')"
cas T09b-lien-vers-un-texte-hors-du-dossier 1 "RIEN N'EST VERSÉ" "$E/t/T09b-lien-vers-un-texte-hors-du-dossier" "" "${J[@]}"
non_ordinaire T09b-lien-vers-un-texte-hors-du-dossier recuperation/lien.txt
fabriquer "$E/t/T09c-lien-vers-un-dossier" "(D / 'surveillance/lien-dossier').symlink_to('$E/hors-traces', target_is_directory=True)"
cas T09c-lien-vers-un-dossier 1 "RIEN N'EST VERSÉ" "$E/t/T09c-lien-vers-un-dossier" "" "${J[@]}"
non_ordinaire T09c-lien-vers-un-dossier surveillance/lien-dossier
fabriquer "$E/t/T09d-tube-nomme" "import os; os.mkfifo(D / 'cinq-minutes/tube')"
cas T09d-tube-nomme 1 "RIEN N'EST VERSÉ" "$E/t/T09d-tube-nomme" "" "${J[@]}"
non_ordinaire T09d-tube-nomme cinq-minutes/tube
grep -q "TRACES DE LA SESSION : 1 CONSTAT(S)" "$E/sortie-T09-lien-vers-un-fichier-sain.txt" \
    && echo "    T09 : un seul constat pour une entrée relevée par les deux recherches : CONFORME" \
    || { echo "    T09 : compte des constats : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# refus en code 2 : rien n'est cherché
cas T10-jetons-absents 2 "rien n'est cherché" "$E/t/sain" ""
cas T10b-jeton-trop-court 2 "rien n'est cherché" "$E/t/sain" "" HF_TOKEN=court CONTROLE_IA_GITHUB_TOKEN=$JG
mkdir -p "$E/sans-textes"; copie "$E/controle-sans-textes.sh" "$E/sans-textes" "$SHA"
cas T11-textes-absents 2 "rien n'est cherché" "$E/t/sain" "$E/controle-sans-textes.sh" "${J[@]}"
copie "$E/controle-autre-empreinte.sh" "$E/depot" "$(printf 'a%.0s' {1..64})"
cas T12-textes-d-une-autre-empreinte 2 "rien n'est cherché" "$E/t/sain" "$E/controle-autre-empreinte.sh" "${J[@]}"
mkdir -p "$E/depot-sans-sceau/$(dirname "$TEXTES")"; cp "$F" "$E/depot-sans-sceau/$TEXTES"; copie "$E/controle-sans-sceau.sh" "$E/depot-sans-sceau" "$SHA"
cas T13-textes-sans-leur-sceau 2 "rien n'est cherché" "$E/t/sain" "$E/controle-sans-sceau.sh" "${J[@]}"
cas T14-dossier-absent 2 "rien n'est cherché" "$E/t/absent" "" "${J[@]}"
cas T15-textes-dans-le-dossier-controle 2 "les textes de P3 sont dans le dossier contrôlé" "$E/depot" "" "${J[@]}"
env -i PATH=/usr/bin:/bin "${J[@]}" bash "$E/controle-essai.sh" > "$E/sortie-T16.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/sortie-T16.txt" | grep -qF usage && echo "T16-usage-faux : code 2 ; CONFORME" || { echo "T16-usage-faux : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
sed "s|^H=.*|H=$E/module-commun-absent|" "$E/controle-essai.sh" > "$E/controle-sans-module.sh"
cas T17-module-commun-absent 2 "module commun" "$E/t/sain" "$E/controle-sans-module.sh" "${J[@]}"
P_CACHE=$(find "$HN" "$E" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
