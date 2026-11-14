#!/usr/bin/env bash
# Répétition sur jouet de la commande de reprise (version 2 ; script v2) : (1) ouverture simulée par la VRAIE garde de S (ouvrir, mode pleine)
# sur une copie du dépôt et un dépôt de calcul JOUET (paquets factices fabriqués par fermer_run et fermer de S), journal
# commité et poussé sur verdict/p3bis-compte-2-v1 d'un faux dépôt distant local ; (2) perte simulée (sortie et branche
# locale effacées) ; (3) reprise : les huit blocs de la commande, extraits tels quels, joués dans l'ordre ; lecteur simulé.
# Paquet du jouet daté avant les lignes d'écrit (trois réserves). Artefacts : cinq arrêts du constat (dont l'arrêt du
# lecteur rendu par la session d'origine, M1) ; redépliage refusé (morceau altéré, dossier caché laissé) ; branche
# d'origine qui bouge avant le commit du verdict. Surcharge en plus : PERTE du bloc 8.
# Surcharges, et seulement elles : DEPOT_URL, S, TETE_CALCUL, PAQUET_LECTURES du jouet en fin de variables-v1.sh ;
# SESSION_C2 factice du compte 2 (la session qui répète est la session mère, inscrite dans la liste) ; variables de tête du
# bloc 8 ; dépôt d'origine de la copie = faux dépôt local dont le chemin porte « lciric/controle-ia-travail ».
# Rien n'est lu ni récupéré de calcul/p3bis-reel-v2 ; le dépôt donné n'est pas modifié (contrôlé). Efface la copie à la fin.
# Usage : repetition_reprise_jouet_v2.sh DEPOT BAC_NEUF [PYTHON_AVEC_NUMPY]
set -uo pipefail
[ $# -ge 2 ] || { echo "usage : repetition_reprise_jouet_v2.sh DEPOT BAC_NEUF [PYTHON]"; exit 2; }
DEPOT=$(realpath "$1"); X=$(realpath -m "$2"); PYJ=${3:-python3}
[ -e "$X" ] && { echo "$X existe déjà (R12)"; exit 2; }
mkdir -p "$X/home" "$X/blocs" || exit 2
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
ICI=$(dirname "$(realpath "$0")"); CMD="$ICI/commande-reprise-verdict-p3bis-compte-2-v2.md"
S_REEL=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0; RUN=20261113-121129-p3bis-reel
B="$X/home/bac-p3bis-reprise-compte-2-v1"; C="$X/depot"; F="$X/faux/lciric/controle-ia-travail.git"
date -u +"début : %Y-%m-%dT%H:%M:%SZ"
avant=$(sha256sum "$DEPOT/registres/prealables-p3bis-v1.md" "$DEPOT/registres/scellements-v1.md" | cut -d' ' -f1 | tr '\n' ' ')
conformes=0; total=0
note() { total=$((total+1)); if [ "$1" = 0 ]; then conformes=$((conformes+1)); echo "OK  $2"; else echo "KO  $2"; fi; }
bloc() {
    local out c; out=$(cd "$C" && HOME="${3:-$X/home}" bash "$2" 2>&1); c=$?
    printf '%s\n' "$out" | sed -E 's/^(.{0,170}).*/    \1/'
    if [ "$c" = 0 ] && ! printf '%s\n' "$out" | grep -q '^ARRÊT'; then note 0 "$1"; else note 1 "$1 (code $c)"; fi
}
attendu_arret() {   # libellé, fichier, motif, HOME
    local out c; out=$(cd "$C" && HOME="$4" bash "$2" 2>&1); c=$?
    printf '%s\n' "$out" | grep '^ARRÊT' | sed -E 's/^(.{0,170}).*/    \1/'
    note "$([ "$c" != 0 ] && printf '%s\n' "$out" | grep -q "^ARRÊT : $3" && echo 0 || echo 1)" "$1"
}
awk -v d="$X/blocs" 'BEGIN{n=0; dans=0} /^```bash$/{n++; dans=1; f=sprintf("%s/bloc-%02d.sh", d, n); next}
     /^```$/{if(dans){dans=0; close(f)}; next} dans{print > f}' "$CMD"
note "$([ "$(ls "$X/blocs" | wc -l)" = 8 ] && echo 0 || echo 1)" "8 blocs extraits du texte de la commande de reprise"
echo "empreinte des 8 blocs mis bout à bout : $(cat "$X"/blocs/bloc-*.sh | sha256sum | cut -d' ' -f1)"

# --- copie du dépôt et faux dépôt distant -------------------------------------------------------------------------
git clone -q --no-checkout "$DEPOT" "$C" \
 && git -C "$C" sparse-checkout set --no-cone /docs/sha256sums-lancement-v2.txt /docs/brief-claude-code-programme-complet-v2.md \
    /docs/programme-controle-ia-v2.md /docs/etat-de-l-art-controle-ia-v1.md /registres/prealables-p3bis-v1.md \
    /registres/scellements-v1.md /registres/ouvertures-p3bis-v1.md '/registres/qui-a-lu-quoi-v1.md*' '/prereg/P3-bis-*' \
    '/prereg/T0.7-sondes-v0-v1.md*' '/docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md*' '/docs/decisions/decision-N-066-v1.md*' \
    '/diag/20261019-230011-p3-reel/sondes-figees.json*' '/diag/20261019-230011-p3-reel/episodes-p3.json*' \
    /src/controle_ia/ /docs/verdicts/ /registres-provisoires/ /docs/procedures/P3-bis-commande-compte-2-v1/ \
 && git -C "$C" reset -q --hard HEAD && cp -r "$ICI" "$C/docs/procedures/" \
 && git -C "$C" config user.name repetition && git -C "$C" config user.email repetition@invalid \
 && mkdir -p "$(dirname "$F")" && git init -q --bare "$F" && echo "$C/.git/objects" > "$F/objects/info/alternates" \
 && git -C "$F" config receive.shallowUpdate true && git -C "$C" push -q "$F" HEAD:refs/heads/main \
 && git -C "$C" remote set-url origin "$F"
note $? "copie du dépôt et faux dépôt distant (main = $(git -C "$C" rev-parse --short HEAD))"

# --- jouet de calcul ---------------------------------------------------------------------------------------------
J="$X/jouet-calcul"; MJ="$X/module-pour-jouet"; mkdir -p "$MJ/controle_ia/premier_test_ia"
for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py; do
    git -C "$DEPOT" show "$S_REEL:src/controle_ia/$f" > "$MJ/controle_ia/$f"; done
git init -q -b calcul "$J"
for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py \
         premier_test_ia/ouverture_p3bis_v3.py.sha256 premier_test_ia/lecture_p3bis_v1.py premier_test_ia/lecture_p3bis_v1.py.sha256 \
         premier_test_ia/lecture_p3bis_v2.py premier_test_ia/lecture_p3bis_v2.py.sha256; do
    mkdir -p "$(dirname "$J/src/controle_ia/$f")"; git -C "$DEPOT" show "$S_REEL:src/controle_ia/$f" > "$J/src/controle_ia/$f"; done
git -C "$J" add -A && git -C "$J" -c user.email=j@invalid -c user.name=jouet commit -q -m "S du jouet"; SJ=$(git -C "$J" rev-parse HEAD)
cat > "$X/jouet_calcul.py" <<'FIN'
import json, secrets, sys
from pathlib import Path
from controle_ia.premier_test_ia import ouverture_p3bis_v3 as o
from controle_ia.scellement import sceller
RUN = "20261113-121129-p3bis-reel"
RL, RLC = "20261113-154300-p3bis-lecture", "20261113-154400-p3bis-lecture-complementaire"
r = Path(sys.argv[1])
def ecrire(c, b, sceau=True):
    p = r / c; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
    if sceau: sceller(p)
for n in o.DONNEES_EXIGEES: ecrire(f"donnees/{RUN}/{n}", secrets.token_bytes(4096))
ecrire(f"diag/{RUN}/episodes-p3.json", b'{"honnete/0": "jouet"}')
o.fermer_run(r, RUN)
for n in o.DONNEES_EXIGEES:
    (r / f"donnees/{RUN}/{n}").unlink(); (r / f"donnees/{RUN}/{n}.sha256").unlink()
(r / f"donnees/{RUN}").rmdir(); (r / "donnees").rmdir()
(r / f"diag/{RUN}/episodes-p3.json").unlink(); (r / f"diag/{RUN}/episodes-p3.json.sha256").unlink()
ecrire(f"runs/{RL}/manifeste.json", b'{"jouet": 1}\n'); ecrire(f"diag/{RL}/lecture-p3.json", b'{"resultat": {}}\n')
ecrire(f"runs/{RLC}/manifeste.json", b'{"jouet": 1}\n')
ecrire(f"diag/{RLC}/lecture-p3bis.json", b'{"resultat": {"issue_mecanique": {"issue": "vu", "ligne": 4}}}\n')
ecrire("espace-ferme-p3bis/durees-lectures-v1.json", b'{"codes": {}}\n', False)
ecrire("espace-ferme-p3bis/deplie-run-v1.json", b'{"run": "x", "fichiers": []}\n', False)
o.fermer(r, RUN, [RL, RLC], "espace-ferme-p3bis", imprimer=lambda s: None)
ecrire(f"runs/{RUN}/manifeste.json", b'{"jouet": 1}\n'); ecrire(f"diag/{RUN}/resume.json", b'{"jouet": 1}\n')
ecrire(f"diag/{RUN}/sondes-figees.json", b'{"jouet": 1}\n'); ecrire("traces/p3bis-jouet/trace.txt", b"jouet\n", False)
FIN
PYTHONPATH="$MJ" "$PYJ" -B "$X/jouet_calcul.py" "$J" \
 && git -C "$J" add -A && GIT_COMMITTER_DATE=2026-11-13T15:45:00Z GIT_AUTHOR_DATE=2026-11-13T15:45:00Z \
    git -C "$J" -c user.email=j@invalid -c user.name=jouet commit -q -m "paquets du jouet (daté avant les lignes d'écrit)" \
 && git clone -q --bare "$J" "$X/jouet-calcul.git" && git -C "$X/jouet-calcul.git" branch -m calcul calcul/p3bis-reel-v2
note $? "dépôt de calcul jouet"
TJ=$(git -C "$J" rev-parse HEAD); PJ=$(cut -d' ' -f1 "$J/diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar.sha256")

# --- (1) ouverture simulée par la vraie garde, journal poussé sur verdict/p3bis-compte-2-v1 -----------------------
git -C "$C" switch -q -c verdict/p3bis-compte-2-v1
for x in "donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz.sha256 34181fd147918f0d47e21848b939f9e47c8b8507" \
         "diag/20261114-001352-t07-lecture-reel/sondes-t07.json.sha256 60d8dfb09e0c797d807c515d38077b734f5a1f42"; do
    set -- $x; mkdir -p "$(dirname "$C/$1")"; git -C "$DEPOT" cat-file blob "$2" > "$C/$1"; done
(cd "$J" && PYTHONPATH="$MJ" "$PYJ" -B -m controle_ia.premier_test_ia.ouverture_p3bis_v3 ouvrir --mode pleine --run "$RUN" \
    --racine "$C" --racine-paquets "$J" --sortie "$X/sortie-de-l-ouverture") > "$X/sortie-garde-ouverture.txt"; sed 's/^/    /' "$X/sortie-garde-ouverture.txt"
note "$([ "$(grep -c '^réserve : ' "$X/sortie-garde-ouverture.txt")" = 3 ] && echo 0 || echo 1)" "la garde a imprimé trois réserves « écrit après la lecture fermée »"
note "$([ "$(grep -c '^| OUVERTURE-P3BIS |' "$C/registres/ouvertures-p3bis-v1.md")" = 1 ] && echo 0 || echo 1)" "ouverture simulée : la vraie garde a écrit une ligne OUVERTURE-P3BIS"
rm -rf "$C/donnees/20261114-001352-t07-lecture-reel" "$C/diag/20261114-001352-t07-lecture-reel"
git -C "$C" add registres/ouvertures-p3bis-v1.md && git -C "$C" commit -q -m "ouverture simulée (jouet)" \
 && git -C "$C" push -q origin refs/heads/verdict/p3bis-compte-2-v1:refs/heads/verdict/p3bis-compte-2-v1
note $? "journal commité seul et poussé sur verdict/p3bis-compte-2-v1 (faux dépôt distant)"
JO=$(git -C "$C" rev-parse HEAD:registres/ouvertures-p3bis-v1.md); HO=$(git -C "$F" rev-parse refs/heads/verdict/p3bis-compte-2-v1)
# branche d'artefact : la même, plus un verdict
git -C "$C" switch -q -c artefact-avec-verdict && mkdir -p "$C/docs/verdicts" && echo factice > "$C/docs/verdicts/verdict-P3-bis-v1.md" \
 && git -C "$C" add docs/verdicts/verdict-P3-bis-v1.md && git -C "$C" commit -q -m "artefact" \
 && git -C "$C" push -q origin refs/heads/artefact-avec-verdict:refs/heads/verdict/artefact-avec-verdict

artefact_branche() {   # nom, action sur la copie (à partir du commit du journal)
    git -C "$C" switch -q -c "$1" verdict/p3bis-compte-2-v1 && eval "$2" && git -C "$C" add -A registres docs \
     && git -C "$C" commit -q -m "artefact $1" && git -C "$C" push -q origin "refs/heads/$1:refs/heads/verdict/$1" \
     && git -C "$C" switch -q verdict/p3bis-compte-2-v1 && git -C "$C" branch -q -D "$1"
}
LO=$(tail -n 1 "$C/registres/ouvertures-p3bis-v1.md")
artefact_branche artefact-deux-ouvertures 'echo "$LO" >> "$C/registres/ouvertures-p3bis-v1.md"'
artefact_branche artefact-refus-final "echo \"| REFUS-OUVERTURE-P3BIS | $(echo "$LO" | awk -F' [|] ' '{print $2}') | pleine | - | - | deja-ouverte : essai |\" >> \"$C/registres/ouvertures-p3bis-v1.md\""
artefact_branche artefact-arret-lecteur 'mkdir -p "$C/registres-provisoires" && echo "STATUT : arret autre" > "$C/registres-provisoires/compte-2-verdict-p3bis-2026-11-14-v1.md" && git -C "$C" add registres-provisoires'
note $? "branches d'artefact du constat poussées (deux ouvertures, refus final, arrêt du lecteur rendu)"
# --- (2) perte simulée --------------------------------------------------------------------------------------------
rm -rf "$X/sortie-de-l-ouverture" && git -C "$C" switch -q main && git -C "$C" branch -q -D verdict/p3bis-compte-2-v1 artefact-avec-verdict \
 && git -C "$C" update-ref -d refs/remotes/origin/verdict/p3bis-compte-2-v1 2>/dev/null; [ ! -e "$C/registres/ouvertures-p3bis-v1.md" ]
note $? "perte simulée : espace de l'ouverture et branche locale effacés ; la copie est revenue à main, sans journal"

# --- (3) reprise ----------------------------------------------------------------------------------------------------
SC2=session_01COMPTE2REPRISEZZZZZZZZZ
sed "s#^SESSION_C2=\"session_\${CLAUDE_CODE_REMOTE_SESSION_ID\#cse_}\"#SESSION_C2=$SC2#" "$X/blocs/bloc-01.sh" > "$X/bloc-01-repetition.sh"
note "$(grep -c "^SESSION_C2=$SC2" "$X/bloc-01-repetition.sh" | grep -qx 1 && echo 0 || echo 1)" "surcharge de SESSION_C2 posée"
bloc "bloc 1 (variables)" "$X/bloc-01-repetition.sh"
printf '# --- surcharge de la répétition ---\nDEPOT_URL=file://%s\nS=%s\nTETE_CALCUL=%s\nPAQUET_LECTURES=%s\n' "$X/jouet-calcul.git" "$SJ" "$TJ" "$PJ" >> "$B/variables-v1.sh"
cp "$B/variables-v1.sh" "$X/variables-sauve.sh"
constat() {   # branche, motif, libellé
    cp "$X/variables-sauve.sh" "$B/variables-v1.sh"; echo "BRANCHE_OUV=$1" >> "$B/variables-v1.sh"
    attendu_arret "constat refusé : $3 (artefact)" "$X/blocs/bloc-02.sh" "$2" "$X/home"
}
constat verdict/branche-absente "branche verdict/branche-absente absente" "branche d'ouverture absente"
constat verdict/artefact-deux-ouvertures "journal : une seule ligne OUVERTURE-P3BIS attendue" "deux lignes d'ouverture"
constat verdict/artefact-refus-final "dernière ligne du journal autre" "dernière ligne un refus"
constat verdict/artefact-avec-verdict "un verdict est déjà sur" "verdict déjà présent"
constat verdict/artefact-arret-lecteur "verdict/artefact-arret-lecteur porte autre chose que le journal" "arrêt du lecteur rendu par la session d'origine (M1)"
cp "$X/variables-sauve.sh" "$B/variables-v1.sh"
bloc "bloc 2 (constat de perte, branche de reprise poussée)" "$X/blocs/bloc-02.sh"
note "$([ -n "$(git -C "$F" rev-parse -q --verify refs/heads/verdict/p3bis-compte-2-reprise-v1)" ] && echo 0 || echo 1)" "branche de reprise poussée dès le bloc 2"
bloc "bloc 2 relancé (branche de reprise reconnue)" "$X/blocs/bloc-02.sh"
bloc "bloc 3 (mêmes paquets, vérifiés à l'égalité ; attestation sur la liste réelle)" "$X/blocs/bloc-03.sh"
BA="$X/home-artefact/bac-p3bis-reprise-compte-2-v1"; mkdir -p "$X/home-artefact" && cp -a "$B" "$BA" \
 && sed -i "s#^DEPOT='\(.*\)'; BAC='$B';#DEPOT='\1'; BAC='$BA';#" "$BA/variables-v1.sh" && grep -q "BAC='$BA'" "$BA/variables-v1.sh" \
 && printf 'X' | dd of="$BA/p3bis-espace-ferme-reprise-v1/clone-calcul-p3bis-reel-v2/diag/$RUN/paquet-run-ferme-v1.tar.000" bs=1 seek=100 conv=notrunc 2>/dev/null
attendu_arret "bloc 4 sur un morceau altéré : rien n'est redéplié (artefact)" "$X/blocs/bloc-04.sh" "redépliage" "$X/home-artefact"
note "$([ ! -e "$BA/p3bis-espace-ferme-reprise-v1/paquets-ouverts" ] && echo 0 || echo 1)" "artefact : aucun fichier redéplié"
rm -rf "$X/home-artefact"
mkdir -p "$X/home-artefact" && cp -a "$B" "$BA" && sed -i "s#^DEPOT='\(.*\)'; BAC='$B';#DEPOT='\1'; BAC='$BA';#" "$BA/variables-v1.sh" \
 && mkdir "$BA/p3bis-espace-ferme-reprise-v1/.ouverture-essai"
out=$(cd "$C" && HOME="$X/home-artefact" bash "$X/blocs/bloc-04.sh" 2>&1); c=$?
note "$([ "$c" != 0 ] && printf '%s\n' "$out" | grep -q "dossier caché" && [ ! -e "$BA/p3bis-espace-ferme-reprise-v1/paquets-ouverts" ] && echo 0 || echo 1)" "bloc 4 avec un dossier caché laissé : arrêt, rien redéplié (artefact)"
rm -rf "$X/home-artefact"
bloc "bloc 4 (redépliage par lire_paquets et extraire ; sortie de la garde reconstituée)" "$X/blocs/bloc-04.sh"
note "$([ "$(git -C "$C" rev-parse HEAD:registres/ouvertures-p3bis-v1.md)" = "$JO" ] && cmp -s <(git -C "$C" show HEAD:registres/ouvertures-p3bis-v1.md) "$C/registres/ouvertures-p3bis-v1.md" && echo 0 || echo 1)" "journal : même blob que celui de l'ouverture, aucune ligne neuve"
note "$(diff <(grep '^réserve : ' "$X/sortie-garde-ouverture.txt") <(grep '^réserve : ' "$B/p3bis-espace-ferme-reprise-v1/sortie-de-la-garde-reconstituee-v1.txt") >/dev/null && [ "$(grep -c '^réserve : ' "$B/p3bis-espace-ferme-reprise-v1/sortie-de-la-garde-reconstituee-v1.txt")" = 3 ] && echo 0 || echo 1)" "trois réserves reconstituées, égales à celles qu'a imprimées la garde"
bloc "bloc 5 (pièces, bordereau)" "$X/blocs/bloc-05.sh"
bloc "bloc 6 (message de remise au lecteur neuf)" "$X/blocs/bloc-06.sh"
V="$B/p3bis-espace-ferme-reprise-v1/verdict-ferme"
printf '# Verdict factice de la répétition\n\nÉcart (reprise, R-2696) : factice.\n' > "$V/verdict-P3-bis-v1.md"
printf 'print(1)\n' > "$V/verdict-P3-bis-v1-pb9-v1.py"; printf 'jouet\n' > "$V/verdict-P3-bis-v1-pb9-sortie-v1.txt"
"$PYJ" -B -c 'import hashlib, json, sys
v = sys.argv[1]; h = hashlib.sha256(open(v + "/verdict-P3-bis-v1.md", "rb").read()).hexdigest()
d = {"issue": "vu", "ligne": 4, "verdict": "docs/verdicts/verdict-P3-bis-v1.md", "verdict_sha256": h}
open(v + "/verdict-P3-bis-v1-issue.json", "x", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n")' "$V"
note $? "lecteur neuf simulé : quatre fichiers factices, écart déclaré en tête"
# artefact : la branche d'origine bouge avant le commit du verdict
git -C "$C" fetch -q origin +refs/heads/verdict/p3bis-compte-2-v1:refs/remotes/origin/verdict/p3bis-compte-2-v1
git -C "$C" switch -q -c bouge refs/remotes/origin/verdict/p3bis-compte-2-v1 && git -C "$C" commit -q --allow-empty -m "session d'origine vivante" \
 && git -C "$C" push -q origin refs/heads/bouge:refs/heads/verdict/p3bis-compte-2-v1 && git -C "$C" switch -q verdict/p3bis-compte-2-reprise-v1
attendu_arret "bloc 7 quand la branche d'origine a bougé : rien commité (artefact)" "$X/blocs/bloc-07.sh" "verdict/p3bis-compte-2-v1 a bougé" "$X/home"
note "$([ ! -e "$B/c-verdict-v1.txt" ] && echo 0 || echo 1)" "artefact : aucun commit du verdict"
git -C "$C" push -q -f origin "$HO:refs/heads/verdict/p3bis-compte-2-v1" && git -C "$C" branch -q -D bouge
note $? "branche d'origine remise à sa tête (fin de l'artefact)"
bloc "bloc 7 (branche d'origine revérifiée, copie, sceaux, verdict_sha256, exposer-issue, commit, poussée)" "$X/blocs/bloc-07.sh"
"$PYJ" - "$X/blocs/bloc-08.sh" "$X/bloc-08-rempli.sh" <<'FIN'
import sys
t = open(sys.argv[1], encoding="utf-8").read()
t = t.replace("<lignes du rapport final du lecteur, telles quelles, à la place de cette ligne>",
              "STATUT : fichier-d-issue-ecrit\nFICHIERS : (répétition)\nDÉCLARATIONS : faites en tête du verdict")
t = t.replace("CROCHET='<bloquée | passée>'", "CROCHET='bloquée (répétition)'")
t = t.replace("PERTE='<mots de Lazar qui disent la session d origine perdue, recopiés tels quels, sans apostrophe droite>'", "PERTE='perte simulée par la répétition'")
t = t.replace("lecteur : <modèle B | modèle A, faute de B> ; session hôte : <modèle A | modèle B>",
              "lecteur : modèle B (répétition) ; session hôte : modèle A (répétition)")
open(sys.argv[2], "w", encoding="utf-8").write(t)
FIN
bloc "bloc 8 (journal provisoire, écart proposé, passation, rendu)" "$X/bloc-08-rempli.sh"
bloc "bloc 8 relancé (reprise à la poussée)" "$X/bloc-08-rempli.sh"
note "$([ "$(git -C "$F" rev-parse refs/heads/verdict/p3bis-compte-2-v1)" = "$HO" ] && echo 0 || echo 1)" "branche de l'ouverture inchangée au faux dépôt distant"
R=$(git -C "$F" rev-parse refs/heads/verdict/p3bis-compte-2-reprise-v1)
note "$([ "$(git -C "$F" rev-parse "$R:registres/ouvertures-p3bis-v1.md")" = "$JO" ] && [ -z "$(git -C "$F" diff --name-only "$HO" "$R" | grep -v -E '^(docs/verdicts/verdict-P3-bis-v1|registres-provisoires/)')" ] && echo 0 || echo 1)" "branche de reprise : même journal, n'ajoute que le verdict et registres-provisoires/"
apres=$(sha256sum "$DEPOT/registres/prealables-p3bis-v1.md" "$DEPOT/registres/scellements-v1.md" | cut -d' ' -f1 | tr '\n' ' ')
note "$([ "$avant" = "$apres" ] && [ ! -e "$DEPOT/registres/ouvertures-p3bis-v1.md" ] && echo 0 || echo 1)" "dépôt donné : registres inchangés, aucun journal"
rm -rf "$C" && echo "copie du dépôt effacée"
date -u +"fin : %Y-%m-%dT%H:%M:%SZ"
echo "BILAN : $conformes conformes sur $total"
[ "$conformes" = "$total" ] && echo "RÉPÉTITION : TOUT CONFORME" || { echo "RÉPÉTITION : ÉCART"; exit 1; }
