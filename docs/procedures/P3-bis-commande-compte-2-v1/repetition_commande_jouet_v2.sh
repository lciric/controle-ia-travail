#!/usr/bin/env bash
# Répétition de bout en bout de la commande au compte 2 (version 2 ; script v2), blocs 1 à 13 extraits tels quels de son texte, sur une
# COPIE du dépôt, sans rien ouvrir de réel : la branche de calcul de P3-bis n'est jamais récupérée ; le bloc 4 vise un
# dépôt distant JOUET dont les deux paquets factices sont fabriqués par les fonctions mêmes du module de S (fermer_run,
# fermer) ; la garde réelle de S est appelée sur ces paquets, avec la racine de la copie ; le lecteur est simulé (fichiers
# factices) ; toute poussée va vers un faux dépôt distant local. Seules lectures du dépôt distant réel : main et les deux
# compagnons de donnees/t07-etape-a-v1 (blocs 2 et 3). Surcharges de la répétition, et seulement elles : DEPOT_URL, S et
# TETE_CALCUL et PAQUET_LECTURES du jouet ajoutés en fin de variables-v1.sh ; SESSION_C2 du bloc 1 remplacée par une
# session factice du compte 2 (la session qui joue la répétition est la session mère, inscrite dans la liste) ;
# variables de tête du bloc 13 remplies ; HOME de la copie. La liste « qui a lu quoi » est la vraie (R-2692).
# Artefacts ajoutés : attestation avec la session mère (refus attendu) ; bloc 7 sur une copie dont un morceau est altéré.
# Blocs 8 et 9 joués dans un seul appel, comme la commande l'exige.
# Vérifie à la fin que le dépôt donné n'a ni journal des ouvertures ni registre changé. Efface la copie à la fin.
# Usage : repetition_commande_jouet_v2.sh DEPOT BAC_NEUF [PYTHON_AVEC_NUMPY]
set -uo pipefail
[ $# -ge 2 ] || { echo "usage : repetition_commande_jouet_v2.sh DEPOT BAC_NEUF [PYTHON]"; exit 2; }
DEPOT=$(realpath "$1"); X=$(realpath -m "$2"); PYJ=${3:-python3}
[ -e "$X" ] && { echo "$X existe déjà (R12)"; exit 2; }
mkdir -p "$X/home" "$X/blocs" || exit 2
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
ICI=$(dirname "$(realpath "$0")"); CMD="$ICI/commande-ouverture-verdict-p3bis-compte-2-v2.md"
S_REEL=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0; URL=https://github.com/lciric/controle-ia-travail.git
B="$X/home/bac-p3bis-compte-2-v1"; C="$X/depot"
date -u +"début : %Y-%m-%dT%H:%M:%SZ"
avant=$(sha256sum "$DEPOT/registres/prealables-p3bis-v1.md" "$DEPOT/registres/scellements-v1.md" | cut -d' ' -f1 | tr '\n' ' ')
conformes=0; total=0
note() { total=$((total+1)); if [ "$1" = 0 ]; then conformes=$((conformes+1)); echo "OK  $2"; else echo "KO  $2"; fi; }
bloc() {   # libellé, fichier du bloc
    local out c; out=$(cd "$C" && HOME="$X/home" bash "$2" 2>&1); c=$?
    printf '%s\n' "$out" | sed -E 's/^(.{0,170}).*/    \1/'
    if [ "$c" = 0 ] && ! printf '%s\n' "$out" | grep -q '^ARRÊT'; then note 0 "$1"; else note 1 "$1 (code $c)"; fi
}
awk -v d="$X/blocs" 'BEGIN{n=0; dans=0} /^```bash$/{n++; dans=1; f=sprintf("%s/bloc-%02d.sh", d, n); next}
     /^```$/{if(dans){dans=0; close(f)}; next} dans{print > f}' "$CMD"
note "$([ "$(ls "$X/blocs" | wc -l)" = 13 ] && echo 0 || echo 1)" "13 blocs extraits du texte de la commande"
echo "empreinte des 13 blocs mis bout à bout (cat bloc-01.sh … bloc-13.sh | sha256sum) : $(cat "$X"/blocs/bloc-*.sh | sha256sum | cut -d' ' -f1)"

# --- copie du dépôt : extraction partielle des seuls chemins utiles ; origine = dépôt distant réel (lecture seule) ---
git clone -q --no-checkout "$DEPOT" "$C" && git -C "$C" remote set-url origin "$URL" \
 && git -C "$C" sparse-checkout set --no-cone /docs/sha256sums-lancement-v2.txt /docs/brief-claude-code-programme-complet-v2.md \
    /docs/programme-controle-ia-v2.md /docs/etat-de-l-art-controle-ia-v1.md /registres/prealables-p3bis-v1.md \
    /registres/scellements-v1.md /registres/ouvertures-p3bis-v1.md '/registres/qui-a-lu-quoi-v1.md*' '/prereg/P3-bis-*' '/prereg/T0.7-sondes-v0-v1.md*' \
    '/docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md*' '/docs/decisions/decision-N-066-v1.md*' \
    '/diag/20261019-230011-p3-reel/sondes-figees.json*' '/diag/20261019-230011-p3-reel/episodes-p3.json*' \
    /src/controle_ia/ /docs/verdicts/ /registres-provisoires/ /docs/procedures/P3-bis-commande-compte-2-v1/ \
 && git -C "$C" reset -q --hard HEAD && cp -r "$ICI" "$C/docs/procedures/" \
 && git -C "$C" config user.name repetition && git -C "$C" config user.email repetition@invalid
note $? "copie du dépôt prête (extraction partielle ; identité git locale à la copie)"
SC2=session_01COMPTE2REPETITIONZZZZZZ          # session factice du compte 2
grep -q '^SESSION_C2="session_${CLAUDE_CODE_REMOTE_SESSION_ID#cse_}"' "$X/blocs/bloc-01.sh"
note $? "bloc 1 : ligne SESSION_C2 trouvée (surchargée par une session factice du compte 2)"
sed "s#^SESSION_C2=\"session_\${CLAUDE_CODE_REMOTE_SESSION_ID\#cse_}\"#SESSION_C2=$SC2#" "$X/blocs/bloc-01.sh" > "$X/bloc-01-repetition.sh"
note "$(grep -c "^SESSION_C2=$SC2" "$X/bloc-01-repetition.sh" | grep -qx 1 && echo 0 || echo 1)" "surcharge de SESSION_C2 posée"
bloc "bloc 1 (variables ; liste réelle R-2692)" "$X/bloc-01-repetition.sh"
# attestation sur la vraie liste : cas sain (session factice du compte 2, « compte 2 ») et artefact (session mère)
MA="$X/module-attestation"; mkdir -p "$MA/controle_ia/premier_test_ia"
for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py; do
    git -C "$DEPOT" show "$S_REEL:src/controle_ia/$f" > "$MA/controle_ia/$f"; done
attestation() {   # session, code attendu (0 conforme, 1 refus)
    PYTHONPATH="$MA:$ICI" "$PYJ" -B - "$C/registres/qui-a-lu-quoi-v1.md" "$1" <<'FIN'
import sys
import controle_a_blanc_compte_2_v1 as c
ok, texte = c.attester(__import__("pathlib").Path(sys.argv[1]),
                       "9eb15acba4ef6e4f3ff1f6b30fbcef7557e58b5c8aafa9bc6bbe843c89c0d7ae", sys.argv[2], "compte 2")
print(("    CONFORME : " if ok else "    REFUS : ") + texte)
sys.exit(0 if ok else 1)
FIN
}
attestation "$SC2"; note $? "attestation, liste réelle : session factice du compte 2 et « compte 2 » absents (cas sain)"
attestation session_01QPDgKgACWyCkCN8HjqwNXy; note "$([ $? = 1 ] && echo 0 || echo 1)" "attestation, liste réelle : la session mère y figure, refus (artefact)"
bloc "bloc 2 (contrôles d'entrée, branche neuve, locale à la copie)" "$X/blocs/bloc-02.sh"
bloc "bloc 2 relancé (branche locale reconnue)" "$X/blocs/bloc-02.sh"
bloc "bloc 3 (compagnons de T0.7, dépôt distant réel)" "$X/blocs/bloc-03.sh"
note "$([ ! -e "$B/compagnons-t07-v1" ] && echo 0 || echo 1)" "dépôt jetable des compagnons effacé"

# --- jouet de la branche de calcul ---------------------------------------------------------------------------------
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
print("second paquet du jouet :", o.fermer_run(r, RUN)["sha256"])
for n in o.DONNEES_EXIGEES:
    (r / f"donnees/{RUN}/{n}").unlink(); (r / f"donnees/{RUN}/{n}.sha256").unlink()
(r / f"donnees/{RUN}").rmdir(); (r / "donnees").rmdir()
(r / f"diag/{RUN}/episodes-p3.json").unlink(); (r / f"diag/{RUN}/episodes-p3.json.sha256").unlink()
ecrire(f"runs/{RL}/manifeste.json", b'{"jouet": 1}\n'); ecrire(f"diag/{RL}/lecture-p3.json", b'{"resultat": {}}\n')
ecrire(f"runs/{RLC}/manifeste.json", b'{"jouet": 1}\n')
ecrire(f"diag/{RLC}/lecture-p3bis.json", b'{"resultat": {"issue_mecanique": {"issue": "vu", "ligne": 4}}}\n')
ecrire("espace-ferme-p3bis/durees-lectures-v1.json", b'{"codes": {}}\n', False)
ecrire("espace-ferme-p3bis/deplie-run-v1.json", b'{"run": "x", "fichiers": []}\n', False)
print("paquet des lectures du jouet :", o.fermer(r, RUN, [RL, RLC], "espace-ferme-p3bis", imprimer=lambda s: None))
ecrire(f"runs/{RUN}/manifeste.json", b'{"jouet": 1}\n'); ecrire(f"diag/{RUN}/resume.json", b'{"jouet": 1}\n')
ecrire(f"diag/{RUN}/sondes-figees.json", b'{"jouet": 1}\n'); ecrire("traces/p3bis-jouet/trace.txt", b"jouet\n", False)
ecrire("docs/notes/bras-attaque/leurre.txt", b"chemin interdit factice : ne doit jamais etre extrait\n", False)
FIN
PYTHONPATH="$MJ" "$PYJ" -B "$X/jouet_calcul.py" "$J" | sed 's/^/    /'
git -C "$J" add -A && git -C "$J" -c user.email=j@invalid -c user.name=jouet commit -q -m "paquets du jouet"; TJ=$(git -C "$J" rev-parse HEAD)
git clone -q --bare "$J" "$X/jouet-calcul.git" && git -C "$X/jouet-calcul.git" branch -m calcul calcul/p3bis-reel-v2
note $? "dépôt distant jouet : S du jouet $SJ, tête $TJ (paquets factices, chemin interdit factice)"
PJ=$(cut -d' ' -f1 "$J/diag/p3bis-ferme-20261113-121129-p3bis-reel/paquet-ferme-v1.tar.sha256")
printf '# --- surcharge de la répétition (jamais dans la commande) ---\nDEPOT_URL=file://%s\nS=%s\nTETE_CALCUL=%s\nPAQUET_LECTURES=%s\n' \
    "$X/jouet-calcul.git" "$SJ" "$TJ" "$PJ" >> "$B/variables-v1.sh"
F="$X/faux-distant.git"; git init -q --bare "$F" && echo "$C/.git/objects" > "$F/objects/info/alternates" \
 && git -C "$F" config receive.shallowUpdate true && git -C "$C" push -q "$F" refs/remotes/origin/main:refs/heads/main \
 && git -C "$C" remote set-url origin "$F"
note $? "faux dépôt distant local : toute poussée de la suite va vers lui"

bloc "bloc 4 (dépôt jetable du jouet, module de S)" "$X/blocs/bloc-04.sh"
bloc "bloc 5 (contrôle à blanc et attestation)" "$X/blocs/bloc-05.sh"
bloc "bloc 6 (place, mémoire, extraction par liste positive)" "$X/blocs/bloc-06.sh"
bloc "bloc 7 (vérifications ; paquets, morceaux et date contrôlés avant l'appel)" "$X/blocs/bloc-07.sh"
# artefact : copie de l'environnement dont un morceau du second paquet est altéré ; le bloc 7 doit arrêter
BA="$X/home-artefact/bac-p3bis-compte-2-v1"; mkdir -p "$X/home-artefact" && cp -a "$B" "$BA" \
 && sed -i "s#^DEPOT='\(.*\)'; BAC='$B';#DEPOT='\1'; BAC='$BA';#" "$BA/variables-v1.sh" && grep -q "BAC='$BA'" "$BA/variables-v1.sh" \
 && printf 'X' | dd of="$BA/p3bis-espace-ferme-v1/clone-calcul-p3bis-reel-v2/diag/20261113-121129-p3bis-reel/paquet-run-ferme-v1.tar.000" \
        bs=1 seek=100 conv=notrunc 2>/dev/null
note $? "artefact préparé : morceau .000 altéré dans une copie"
out=$(cd "$C" && HOME="$X/home-artefact" bash "$X/blocs/bloc-07.sh" 2>&1); c=$?
printf '%s\n' "$out" | grep -E '^(ARRÊT|conforme : paquet)' | sed -E 's/^(.{0,170}).*/    \1/'
note "$([ "$c" != 0 ] && printf '%s\n' "$out" | grep -q '^ARRÊT : second paquet' && echo 0 || echo 1)" "bloc 7 sur morceau altéré : arrêt avant tout appel (artefact)"
rm -rf "$X/home-artefact"
note "$([ ! -e "$B/p3bis-espace-ferme-v1/clone-calcul-p3bis-reel-v2/docs/notes/bras-attaque" ] && echo 0 || echo 1)" "chemin interdit factice non extrait"
cat "$X/blocs/bloc-08.sh" "$X/blocs/bloc-09.sh" > "$X/blocs-08-09.sh"
bloc "blocs 8 et 9 dans un seul appel (poussée avant la garde, garde réelle de S, journal commité seul et poussé)" "$X/blocs-08-09.sh"
bloc "bloc 9 relancé (reprise à la poussée)" "$X/blocs/bloc-09.sh"
bloc "bloc 10 (pièces, extrait, bordereau)" "$X/blocs/bloc-10.sh"
bloc "bloc 11 (message de remise rempli par programme)" "$X/blocs/bloc-11.sh"
V="$B/p3bis-espace-ferme-v1/verdict-ferme"
printf '# Verdict factice de la répétition\n' > "$V/verdict-P3-bis-v1.md"; printf 'print(1)\n' > "$V/verdict-P3-bis-v1-pb9-v1.py"
printf 'jouet\n' > "$V/verdict-P3-bis-v1-pb9-sortie-v1.txt"
"$PYJ" -B -c 'import hashlib, json, sys
v = sys.argv[1]; h = hashlib.sha256(open(v + "/verdict-P3-bis-v1.md", "rb").read()).hexdigest()
d = {"issue": "vu", "ligne": 4, "verdict": "docs/verdicts/verdict-P3-bis-v1.md", "verdict_sha256": h}
open(v + "/verdict-P3-bis-v1-issue.json", "x", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n")' "$V"
note $? "lecteur simulé : quatre fichiers factices dans verdict-ferme"
bloc "bloc 12 (copie, sceaux, verdict_sha256, exposer-issue, commit, poussée)" "$X/blocs/bloc-12.sh"
"$PYJ" - "$X/blocs/bloc-13.sh" "$X/bloc-13-rempli.sh" <<'FIN'
import sys
t = open(sys.argv[1], encoding="utf-8").read()
t = t.replace("<lignes du rapport final du lecteur, telles quelles, à la place de cette ligne>",
              "STATUT : fichier-d-issue-ecrit\nFICHIERS : (répétition)\nDÉCLARATIONS : faites en tête du verdict")
t = t.replace("CROCHET='<bloquée | passée>'", "CROCHET='bloquée (répétition)'")
t = t.replace("lecteur : <modèle B | modèle A, faute de B> ; session hôte : <modèle A | modèle B>",
              "lecteur : modèle B (répétition) ; session hôte : modèle A (répétition)")
open(sys.argv[2], "w", encoding="utf-8").write(t)
FIN
bloc "bloc 13 (journal provisoire, passation, rendu)" "$X/bloc-13-rempli.sh"
bloc "bloc 13 relancé (reprise à la poussée)" "$X/bloc-13-rempli.sh"
CJ=$(cat "$B/c-journal-v1.txt"); CV=$(cat "$B/c-verdict-v1.txt"); CM=$(cat "$B/c-main-v1.txt")
note "$([ "$(git -C "$C" diff --name-status "$CM" "$CJ")" = "A	registres/ouvertures-p3bis-v1.md" ] && echo 0 || echo 1)" "commit du journal : seul ajout, le journal"
note "$([ -z "$(git -C "$C" diff --name-only "$CJ" "$CV" | grep -v '^docs/verdicts/verdict-P3-bis-v1')" ] && echo 0 || echo 1)" "commit du verdict : seulement docs/verdicts/verdict-P3-bis-v1*"
git -C "$C" switch -q -c integration-mere-simulee "$CM" && git -C "$C" cherry-pick "$CJ" > /dev/null \
 && [ "$(git -C "$C" rev-parse HEAD:registres/ouvertures-p3bis-v1.md)" = "$(git -C "$C" rev-parse "$CJ:registres/ouvertures-p3bis-v1.md")" ]
note $? "recopie de la mère simulée (cherry-pick sur la base main) : même blob du journal"
apres=$(sha256sum "$DEPOT/registres/prealables-p3bis-v1.md" "$DEPOT/registres/scellements-v1.md" | cut -d' ' -f1 | tr '\n' ' ')
note "$([ "$avant" = "$apres" ] && [ ! -e "$DEPOT/registres/ouvertures-p3bis-v1.md" ] && echo 0 || echo 1)" "dépôt donné : registres inchangés, aucun journal"
rm -rf "$C" && echo "copie du dépôt effacée"
date -u +"fin : %Y-%m-%dT%H:%M:%SZ"
echo "BILAN : $conformes conformes sur $total"
[ "$conformes" = "$total" ] && echo "RÉPÉTITION : TOUT CONFORME" || { echo "RÉPÉTITION : ÉCART"; exit 1; }
