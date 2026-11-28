#!/usr/bin/env bash
# Banc B de la vérification « données et fuites » de la chaîne v2 de P4 (vérificateur neuf), v1 : contrôle des traces de
# la session (controler_traces_p4_v1.sh, RC-donnees-06) sur des fuites déguisées. Copie jouée : seules les lignes DEPOT et
# TEXTES_SHA256 changent (comme le banc du correcteur) ; faux dépôt portant les textes synthétiques des fenêtres
# (outils_essais_p4_v1.py fenetres ; aucun texte de P3 n'est lu). Dossier des traces fabriqué à la forme de celui de la
# session. Cas « garde » (attendu fixé avant le jeu) et cas « limite » (résultat documenté, sans verdict).
# Usage : banc_b_traces_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
CT=$H/controler_traces_p4_v1.sh
export PYTHONDONTWRITEBYTECODE=1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E" || exit 2
for s in controler_traces_p4_v1.sh verifications_p4_v1.py outils_essais_p4_v1.py; do echo "script éprouvé : $s $(sha256sum "$H/$s" | cut -d' ' -f1)"; done
echo "banc : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
TEXTES=donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl
F="$E/depot/$TEXTES"
"$PY" -B "$H/outils_essais_p4_v1.py" fenetres "$F" > /dev/null 2>&1 || { echo "textes synthétiques impossibles"; exit 2; }
SHA=$(sha256sum "$F" | cut -d' ' -f1)
(cd "$(dirname "$F")" && sha256sum "$(basename "$F")" > "$(basename "$F").sha256")
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^TEXTES_SHA256=[0-9a-f]\{64\} |TEXTES_SHA256=$SHA |" "$CT" > "$E/controle-essai.sh"
[ "$(diff "$CT" "$E/controle-essai.sh" | grep -c '^>')" = 2 ] || { echo "copie : deux lignes changées attendues"; exit 2; }
echo "lignes changées dans la copie du contrôle des traces : 2 (DEPOT, TEXTES_SHA256)"
JT=factice-hf-verifb-0001; JG=factice-gh-verifb-0001
fabriquer() {   # $1 dossier neuf, $2 programme Python (T : textes honnêtes ; D : dossier ; H : hors du dossier)
    mkdir -p "$1" "$1.hors" && "$PY" -I -B - "$F" "$1" "$2" "$1.hors" <<'PYF' || { echo "fabrication impossible : $1"; exit 2; }
import base64, gzip, json, os, sys
from pathlib import Path
import numpy as np
tx, d, prog, hors = sys.argv[1:5]
T = [json.loads(l)["texte"] for l in open(tx, encoding="utf-8") if json.loads(l)["condition"] == "honnete" and len(set(json.loads(l)["texte"])) > 1]
D, H = Path(d), Path(hors)
for sous in ("lancement", "surveillance/arret", "cinq-minutes", "recuperation"):
    (D / sous).mkdir(parents=True, exist_ok=True)
(D / "lancement/lancement.txt").write_text("commit 0123456789abcdef0123456789abcdef01234567\ncreation 1760000000\nsuccès : True ; identifiant 99999999 ; message : essai\n", encoding="utf-8")
(D / "surveillance/journal-dernier.txt").write_text("AMORCE 2026-10-20T20:00:00Z : commit 0123456789abcdef0123456789abcdef01234567\nPROGRES 2026-10-20T20:30:00Z etape=M5 conforme=True\nAMORCE 2026-10-20T21:00:00Z : fin, code 0\n", encoding="utf-8")
(D / "recuperation/sortie.txt").write_text("RÉCUPÉRATION : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)\n", encoding="utf-8")
exec(prog)
PYF
}
NC=0
empreinte_dossier() { (cd "$1" && find . -print0 | sort -z | xargs -0 -I{} sh -c 'printf "%s " "{}"; [ -L "{}" ] && readlink "{}" || { [ -f "{}" ] && sha256sum < "{}" || echo d; }' | sha256sum | cut -d' ' -f1); }
cas() {   # $1 nom, $2 genre (garde, sain, limite), $3 code attendu (garde, sain), $4 dossier
    local n=$1 g=$2 a=$3 x=$4 c v avant apres
    avant=$(empreinte_dossier "$x")
    env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$E" TMPDIR="$E" HF_TOKEN=$JT CONTROLE_IA_GITHUB_TOKEN=$JG GH_TOKEN=$JG \
        bash "$E/controle-essai.sh" "$x" > "$E/sortie-$n.txt" 2>&1; c=$?
    apres=$(empreinte_dossier "$x")
    if [ "$g" = limite ]; then v="limite documentée : $( [ "$c" = 0 ] && echo "NON RETROUVÉE, versement permis" || echo "code $c")"
    else v=CONFORME; [ "$c" = "$a" ] || { v="ÉCART (code $c, attendu $a)"; NC=$((NC + 1)); }; fi
    [ "$avant" = "$apres" ] || { v="ÉCART (dossier contrôlé modifié)"; NC=$((NC + 1)); }
    grep -qiF -e "$JT" -e "$JG" -e zanzibar -e quokka -e marmoset -e axolotl "$E/sortie-$n.txt" && { v="ÉCART (jeton ou texte affiché)"; NC=$((NC + 1)); }
    echo "$n [$g] : code $c ; $v"
    sed -n '1p;$p' "$E/sortie-$n.txt" | cut -c1-200 | sed 's/^/    | /'
}
fabriquer "$E/t/sain" "pass"
cas B00-traces-saines sain 0 "$E/t/sain"
fabriquer "$E/t/brut" "(D / 'surveillance/journal-dernier.txt').write_text('----- /root/p4/run.err\\n' + T[0] + '\\n', encoding='utf-8')"
cas B01-texte-brut garde 1 "$E/t/brut"
fabriquer "$E/t/cache" "(D / '.cache').mkdir(); (D / '.cache/run.err').write_text(json.dumps(T[2]), encoding='utf-8')"
cas B02-texte-echappe-dans-un-dossier-cache garde 1 "$E/t/cache"
fabriquer "$E/t/double" "(D / 'recuperation/sortie.txt').write_text(json.dumps(json.dumps(T[3])), encoding='utf-8')"
cas B03-texte-echappe-deux-fois garde 1 "$E/t/double"
fabriquer "$E/t/jeton-json" "(D / 'cinq-minutes/etat.txt').write_text(json.dumps({'extra_env': [['HF_TOKEN', os.environ.get('JT', '$JT')]]}), encoding='utf-8')"
cas B04-jeton-dans-un-etat-json garde 1 "$E/t/jeton-json"
# limites : formes non couvertes par la décision, ou fichiers que la recherche ne lit pas
fabriquer "$E/t/lien" "(H / 'cible.txt').write_text(T[0] + '\\n', encoding='utf-8'); (D / 'surveillance/journal-lien.txt').symlink_to(H / 'cible.txt')"
cas B10-lien-symbolique-vers-un-texte limite - "$E/t/lien"
fabriquer "$E/t/lien-jeton" "(H / 'cible.txt').write_text('$JT\\n', encoding='utf-8'); (D / 'lancement/jeton-lien.txt').symlink_to(H / 'cible.txt')"
cas B11-lien-symbolique-vers-un-jeton limite - "$E/t/lien-jeton"
fabriquer "$E/t/lien-dossier" "(H / 'run.err').write_text(T[1] + '\\n', encoding='utf-8'); (D / 'recuperation/clone').symlink_to(H, target_is_directory=True)"
cas B12-lien-symbolique-vers-un-dossier limite - "$E/t/lien-dossier"
fabriquer "$E/t/npy" "np.save(D / 'recuperation/x.npy', np.array([T[0]]))"
cas B13-texte-dans-un-npy limite - "$E/t/npy"
fabriquer "$E/t/utf16" "(D / 'surveillance/etats.txt').write_bytes(T[0].encode('utf-16'))"
cas B14-texte-en-utf16 limite - "$E/t/utf16"
fabriquer "$E/t/gzip" "(D / 'surveillance/journal.txt.gz').write_bytes(gzip.compress(T[0].encode()))"
cas B15-texte-compresse limite - "$E/t/gzip"
fabriquer "$E/t/b64" "(D / 'surveillance/etats.txt').write_text(base64.b64encode(T[0].encode()).decode() + '\\n', encoding='utf-8')"
cas B16-texte-en-base64 limite - "$E/t/b64"
fabriquer "$E/t/nom" "(D / 'recuperation' / (T[2][13:140].replace('\\n', ' ') + '.txt')).write_text('rien\\n', encoding='utf-8')"
cas B17-texte-dans-un-nom-de-fichier limite - "$E/t/nom"
P_CACHE=$(find "$H" "$E" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : ÉCART"; NC=$((NC + 1)); }
echo "FIN DU BANC B ; écarts sur les cas garde ou sain : $NC"
[ "$NC" = 0 ] || exit 1
