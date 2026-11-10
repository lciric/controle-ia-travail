#!/usr/bin/env bash
# Banc du lanceur de P3-bis (R5), v1, décliné du banc du lanceur de P3 (docs/procedures/P3-premier-test-v2/
# essais_lanceur_p3_v1.sh) sous un nom neuf (R12). Chaque garde du lanceur : un cas sain et au moins un artefact.
# Aucun appel réel n'est possible : faux outil de location sur le PATH (n'appelle aucun service ; journalise le verbe,
# l'étiquette, les variables non secrètes de --env et le GO, jamais un jeton), env -i, HOME redirigé, jetons factices,
# faux contrôles avant dépense, fausse horloge pour la seule date du jour. Dépôt synthétique : texte minimal (GO, ligne
# « Lancement », empreinte de l'amorce), registre des GO fabriqué (ligne GO-2026-11-02-29 recopiée du registre de HEAD,
# un GO de calcul d'une autre course), garde de calcul du dépôt (copie de HEAD), copies versées des scripts de la chaîne
# (celle du lanceur : celle du banc) et des journaux de preuve conformes ; dépôt nu local en guise de dépôt distant.
# Le vrai registres/go.md n'est jamais modifié. Lignes changées dans la copie jouée du lanceur, comptées et déclarées :
# DEPOT (dépôt synthétique), DEPOT_URL (dépôt nu local : aucun appel à GitHub), INTERVALLE_OFFRE_S (0 : les douze essais
# d'offre ne dorment pas).
# Usage : essais_lanceur_p3bis_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
ICI=$(dirname "$(realpath "$0")")
D=/home/user/controle-ia-travail
VERSEES=docs/procedures/P3-bis-temoin-positif-v1
P=prereg/P3-bis-temoin-positif-v1.md
A=scripts/amorce_instance_p3bis_v2.sh
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
for s in lancer_p3bis_v1.sh verifications_p3bis_v1.py; do
    echo "script éprouvé : $s $(sha256sum "$ICI/$s" | cut -d' ' -f1)"
done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
NON_CONFORMES=0; NCAS=0
mkdir -p "$E/bin" "$E/home" "$E/H" || exit 2
JETONS=(HF_TOKEN=factice-hf-1111111 CONTROLE_IA_GITHUB_TOKEN=factice-gi-2222222)
# --- faux outil de location -------------------------------------------------------------------------------------------
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc du lanceur de P3-bis : n'appelle aucun service
J=${FAUX_VASTAI_JOURNAL:?}
echo "appel : $1 $2" >> "$J"
case "$1 $2" in
  "search offers")
    n=$(( $(cat "$J.offres" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$J.offres"
    if [ -n "${FAUX_OFFRES_APRES:-}" ] && [ "$n" -ge "${FAUX_OFFRES_APRES%%:*}" ]; then printf '%s\n' "${FAUX_OFFRES_APRES#*:}"; exit 0; fi
    [ -n "${FAUX_OFFRES:-}" ] && { printf '%s\n' "$FAUX_OFFRES"; exit 0; }
    printf '%s\n' '[{"id": 111, "machine_id": 7101, "host_id": 8101, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 257000, "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.989, "dph_total": 1.10, "inet_down_cost": 0.026, "storage_total_cost": 0.05}, {"id": 222, "dph_total": 0.9, "gpu_name": "A100 SXM4"}]' ;;
  "show user") [ -n "${FAUX_USER_ILLISIBLE:-}" ] && { echo "erreur factice"; exit 0; }; printf '{"credit": %s, "email": "x@invalid"}\n' "${FAUX_CREDIT:-25.0}" ;;
  "show instances")
    d='[{"id": 58936096, "actual_status": "exited", "cur_state": "stopped", "extra_env": [["GH_TOKEN", "secret"]]}, {"id": 58936099, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936100, "actual_status": "exited", "cur_state": "stopped"}]'
    printf '%s\n' "${FAUX_INSTANCES:-$d}" ;;
  "create instance")
    echo "CREATION FACTICE" >> "$J"; echo "offre créée $3" >> "$J"
    a=("$@")
    for ((i = 0; i < ${#a[@]}; i++)); do
      [ "${a[$i]}" = "--label" ] && echo "etiquette ${a[$((i + 1))]}" >> "$J"
      if [ "${a[$i]}" = "--env" ]; then
        for kv in ${a[$((i + 1))]}; do case "$kv" in PREREG=*|BRANCHE=*|DEPOT_URL=*) echo "env $kv" >> "$J" ;; COMMIT=*) echo "env COMMIT=${kv#COMMIT=}" >> "$J" ;; HF_TOKEN=*|GH_TOKEN=*) [ ${#kv} -gt 12 ] && echo "env ${kv%%=*} présent" >> "$J" ;; esac; done
      fi
    done
    echo "go ${GO_ID:-absent}" >> "$J"
    d='{"success": true, "new_contract": 99999999}'; printf '%s\n' "${FAUX_CREATION:-$d}"; exit "${FAUX_CODE_CREATION:-0}" ;;
  *) echo "verbe inattendu" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin/vastai"
# --- fausse horloge : seule « date -u +%F » est simulée (FAUX_JOUR, puis FAUX_JOUR2 à partir de l'appel FAUX_APRES) --
cat > "$E/bin/date" <<EOF
#!/usr/bin/env bash
if [ "\$*" = "-u +%F" ] && [ -n "\${FAUX_JOUR:-}" ]; then
  n=\$(( \$(cat "$E/compteur-jour" 2>/dev/null || echo 0) + 1 )); echo \$n > "$E/compteur-jour"
  if [ -n "\${FAUX_APRES:-}" ] && [ "\$n" -ge "\$FAUX_APRES" ]; then echo "\$FAUX_JOUR2"; else echo "\$FAUX_JOUR"; fi; exit 0
fi
exec /usr/bin/date "\$@"
EOF
chmod +x "$E/bin/date"
# --- copies jouées : lanceur (trois lignes changées), module commun, faux contrôles, autres scripts de la chaîne ------
L=$E/H/lancer_p3bis_v1.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$E/distant.git|" -e "s|^INTERVALLE_OFFRE_S=.*|INTERVALLE_OFFRE_S=0|" \
    "$ICI/lancer_p3bis_v1.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$ICI/lancer_p3bis_v1.sh" "$L" | grep -c '^>') (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S)"
[ "$(diff "$ICI/lancer_p3bis_v1.sh" "$L" | grep -c '^>')" = 3 ] && ! grep -q "^DEPOT=$D" "$L" || { echo "copie du lanceur non sûre"; exit 2; }
cp "$ICI/verifications_p3bis_v1.py" "$E/H/"
cat > "$E/H/controles_avant_depense_p3bis_v1.sh" <<'EOF'
#!/usr/bin/env bash
mkdir -p "$2" "$2.travail" && echo donnees > "$2/x"
echo "arguments : S=${1:0:12} ; $# arguments ; branche $3"
[ $# = 3 ] && [ "$3" = "${FAUX_BRANCHE_ATTENDUE:-calcul/p3bis-reel-v1}" ] || { echo "KO  essai : arguments ($*)"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; }
if [ -n "${FAUX_KO:-}" ]; then echo "OK  essai"; echo "KO  essai : faute simulée"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; fi
if [ -n "${FAUX_DERNIERE:-}" ]; then echo "OK  essai"; echo "dernière ligne inattendue (essai)"; exit 0; fi
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
CHAINE=$(sed -n 's/^CHAINE="\(.*\)"$/\1/p' "$L")
for s in $CHAINE; do
    [ -e "$E/H/$s" ] && continue
    if [ -f "$ICI/$s" ]; then cp "$ICI/$s" "$E/H/$s"; else echo "# $s : pas encore écrit au moment du banc (copie témoin)" > "$E/H/$s"; fi
done
# --- dépôt synthétique et dépôt nu -----------------------------------------------------------------------------------
git init -q --bare -b main "$E/distant.git"
git init -q -b main "$E/depot" && cd "$E/depot" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false; git config push.negotiate false
git remote add origin "$E/distant.git"
mkdir -p prereg scripts registres .claude/hooks "$VERSEES"
printf '#!/usr/bin/env bash\necho "amorce factice du banc"\n' > "$A"
E_AMORCE=$(sha256sum "$A" | cut -d' ' -f1)
git -C "$D" show HEAD:.claude/hooks/garde_calcul.py > .claude/hooks/garde_calcul.py
{ git -C "$D" show HEAD:registres/go.md | sed -n '1,10p'
  git -C "$D" show HEAD:registres/go.md | grep '^| GO-2026-11-02-29 |'
  echo "| GO-2026-11-08-13 | 2026-11-08 | calcul | autre course du programme (essai) | 50 USD | 2026-11-30 | Lazar | essai |"; } > registres/go.md
[ "$(grep -c '^| GO-2026-11-02-29 |' registres/go.md)" = 1 ] || { echo "ligne GO-2026-11-02-29 introuvable au registre de HEAD"; exit 2; }
texte() {   # $1 GO de la ligne « GO », $2 GO de la ligne Lancement, $3 branche citée, $4 DEPOT_URL cité, $5 empreinte citée de l'amorce
    printf '# Préenregistrement factice du banc du lanceur de P3-bis\n\n- GO : **%s** (`registres/go.md` l. 217)\n- Lancement : `GO_ID=%s`, `PREREG=%s`, `BRANCHE=%s` (une relance prend `…-v2`, puis `…-v3`), `DEPOT_URL=%s`, amorce `%s`\n- Empreintes : `%s` (`%s`, sha256)\n' \
        "$1" "$2" "$P" "$3" "$4" "$A" "$A" "$5"
}
URL=file://$E/distant.git
for s in lancer_p3bis_v1.sh $CHAINE; do cp "$E/H/$s" "$VERSEES/$s"; done
# journaux de preuve conformes au module commun (scripts éprouvés : empreintes des copies jouées)
python3 -I -B - "$E/H/verifications_p3bis_v1.py" "$E/H" "$VERSEES" <<'EOF' || exit 2
import hashlib, importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
h, sortie = Path(sys.argv[2]), Path(sys.argv[3])
for nom, (verdict, scripts) in v.JOURNAUX.items():
    lignes = [f"script éprouvé : {s} {hashlib.sha256((h / s).read_bytes()).hexdigest()}" for s in sorted(scripts)]
    (sortie / nom).write_text("\n".join(lignes) + "\ncas factices du banc du lanceur : CONFORMES\n" + verdict + "\n", encoding="utf-8")
EOF
for j in $(sed -n 's/^PREUVES="\(.*\)"$/\1/p' "$L"); do (cd "$VERSEES" && sha256sum "$j" > "$j.sha256"); done
git add -A && git commit -qm "base du banc" && git push -q origin main
texte GO-2026-11-02-29 GO-2026-11-02-29 calcul/p3bis-reel-v1 "$URL" "$E_AMORCE" > "$P"
(cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
git add -A && git commit -qm "scellement factice (S)" && git push -q origin main
S=$(git rev-parse HEAD)
cd "$E" || exit 2
BASE=$(git -C "$E/depot" rev-parse "$S^")
# variantes de S, chacune sur sa branche poussée (le lanceur exige S dans une branche du dépôt distant)
variante() {   # $1 nom de branche ; puis commandes à jouer dans le dépôt avant le commit ; rend S de la variante (texte
    # sain écrit et scellé si les commandes n'en écrivent pas : S ajoute toujours le sceau du texte)
    local b=$1; shift
    git -C "$E/depot" checkout -q -b "variante/$b" "$BASE"
    (cd "$E/depot" && mkdir -p prereg && eval "$*" && { [ -f "$P" ] || { texte GO-2026-11-02-29 GO-2026-11-02-29 calcul/p3bis-reel-v1 "$URL" "$E_AMORCE" > "$P"; sceller_texte; }; })
    git -C "$E/depot" add -A && git -C "$E/depot" commit -qm "variante $b" && git -C "$E/depot" push -q origin "variante/$b"
    git -C "$E/depot" rev-parse HEAD
    git -C "$E/depot" checkout -q main
}
sceller_texte() { (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256"); }
# --- cas ---------------------------------------------------------------------------------------------------------------
cas() {   # $1 nom, $2 code attendu, $3 motif attendu dans la sortie (ou « - »), $4 création attendue (oui/non), $5 S, $6 N, $7 EN_MARCHE ; puis variables
    local nom=$1 attendu=$2 motif=$3 creation=$4 s=$5 n=$6 marche=$7; shift 7
    local t="$E/traces-$nom" c v
    NCAS=$((NCAS + 1))
    rm -f "$E/vastai-$nom.txt" "$E/compteur-jour"
    env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E/home" LANG=C.UTF-8 FAUX_VASTAI_JOURNAL="$E/vastai-$nom.txt" "${JETONS[@]}" "$@" \
        bash "$L" "$s" "$t" "$marche" "$n" > "$E/console-$nom.txt" 2>&1; c=$?
    touch "$E/vastai-$nom.txt"
    v=CONFORME
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    [ "$motif" = - ] || grep -qF -- "$motif" "$E/console-$nom.txt" || v="NON CONFORME (motif « $motif » absent)"
    if [ "$creation" = oui ]; then grep -qx "CREATION FACTICE" "$E/vastai-$nom.txt" || v="NON CONFORME (création attendue)"
    else ! grep -qx "CREATION FACTICE" "$E/vastai-$nom.txt" || v="NON CONFORME (création inattendue)"; fi
    if grep -rqF -e factice-hf-1111111 -e factice-gi-2222222 "$E/console-$nom.txt" "$E/vastai-$nom.txt" "$t" 2>/dev/null; then
        v="NON CONFORME (JETON AFFICHÉ)"
    fi
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $v"
    grep -v '^$' "$E/console-$nom.txt" | tail -1 | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
}
apres() {   # contrôle supplémentaire d'un cas : $1 nom, $2 description, puis la commande
    local nom=$1 desc=$2; shift 2
    NCAS=$((NCAS + 1))
    if (eval "$*") > /dev/null 2>&1; then echo "    $desc : CONFORME"; else echo "    $desc : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
J_OK=FAUX_JOUR=2026-11-10
OFFRES_AUTRE_CPU='[{"id": 444, "machine_id": 7444, "host_id": 8444, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7763 64-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 257000, "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.99, "dph_total": 1.40, "inet_down_cost": 0.02, "storage_total_cost": 0.05}]'
OFFRES_AUCUNE='[{"id": 555, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 16.0, "cpu_ram": 257000, "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.99, "dph_total": 1.0, "inet_down_cost": 0.02, "storage_total_cost": 0.05}]'
OFFRE_EPYC='[{"id": 666, "machine_id": 7666, "host_id": 8666, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 30.0, "cpu_ram": 128000, "disk_space": 80.0, "cuda_max_good": 13.0, "reliability2": 0.98, "dph_total": 2.10, "inet_down_cost": 0.05, "storage_total_cost": 0.08}]'
TOL3='{"id": 58936096, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936099, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936100, "actual_status": "exited", "cur_state": "stopped"}'
# L00 : cas sain
cas L00-sain 0 "succès : True ; identifiant 99999999" oui "$S" 1 - "$J_OK"
apres L00 "création : GO, étiquette, branche, texte, dépôt de travail et commit passés à l'instance, jetons présents sans valeur" \
    "grep -qx 'go GO-2026-11-02-29' '$E/vastai-L00-sain.txt' && grep -qx 'etiquette p3bis-v1' '$E/vastai-L00-sain.txt' && grep -qx 'env BRANCHE=calcul/p3bis-reel-v1' '$E/vastai-L00-sain.txt' && grep -qx 'env PREREG=$P' '$E/vastai-L00-sain.txt' && grep -qx 'env DEPOT_URL=$URL' '$E/vastai-L00-sain.txt' && grep -qx 'env COMMIT=$S' '$E/vastai-L00-sain.txt' && grep -qx 'env HF_TOKEN présent' '$E/vastai-L00-sain.txt' && grep -qx 'env GH_TOKEN présent' '$E/vastai-L00-sain.txt' && grep -qx 'offre créée 111' '$E/vastai-L00-sain.txt'"
apres L00 "traces : instance écrite (cible unique des arrêts), offre choisie, un seul essai d'offre, aucun repli" \
    "grep -qx 'instance 99999999' '$E/traces-L00-sain/lancement.txt' && grep -q '^offre choisie : 111 (1.1 USD/h)' '$E/traces-L00-sain/lancement.txt' && [ \$(grep -c '^essai d.offre' '$E/traces-L00-sain/lancement.txt') = 1 ] && [ ! -e '$E/traces-L00-sain/repli-processeur.txt' ] && [ ! -e '$E/traces-L00-sain/clone-controles' ]"
# L01 / L02 / L03 : branche de calcul et relance
git -C "$E/depot" push -q origin "$S:refs/heads/calcul/p3bis-reel-v1"
cas L01-relance-2-sain 0 "succès : True" oui "$S" 2 - "$J_OK" FAUX_BRANCHE_ATTENDUE=calcul/p3bis-reel-v2
apres L01 "relance : branche calcul/p3bis-reel-v2, étiquette p3bis-v2" "grep -qx 'env BRANCHE=calcul/p3bis-reel-v2' '$E/vastai-L01-relance-2-sain.txt' && grep -qx 'etiquette p3bis-v2' '$E/vastai-L01-relance-2-sain.txt'"
cas L02-branche-presente 2 "branche calcul/p3bis-reel-v1 : git ls-remote, code 0" non "$S" 1 - "$J_OK"
git -C "$E/depot" push -q origin --delete calcul/p3bis-reel-v1
cas L03-relance-sans-tentative 2 "branche calcul/p3bis-reel-v1 absente du dépôt distant" non "$S" 2 - "$J_OK"
# L04 à L07 : GO et date
# (le registre lu est celui du dépôt courant, jamais celui de S : révocation ajoutée au registre courant, puis retirée)
cp "$E/depot/registres/go.md" "$E/go-sain.md"
echo '| GO-2026-11-10-99 | 2026-11-10 | révocation | P3-bis suspendu | — | 2026-11-10 | Lazar | révoque GO-2026-11-02-29 |' >> "$E/depot/registres/go.md"
cas L04-go-revoque 2 "révoqué au registre des GO (GO-2026-11-10-99)" non "$S" 1 - "$J_OK"
cp "$E/go-sain.md" "$E/depot/registres/go.md"
S_GO=$(variante go "texte GO-2026-11-08-13 GO-2026-11-08-13 calcul/p3bis-reel-v1 '$URL' '$E_AMORCE' > '$P'; sceller_texte")
cas L05-go-autre 2 "seul GO-2026-11-02-29 est accepté" non "$S_GO" 1 - "$J_OK"
cas L06-date-apres-limite 3 "après le 2026-11-16" non "$S" 1 - FAUX_JOUR=2026-11-17
cas L06b-date-limite-saine 0 "succès : True" oui "$S" 1 - FAUX_JOUR=2026-11-16
cas L07-date-passe-pendant-les-offres 3 "après le 2026-11-16" non "$S" 1 - FAUX_JOUR=2026-11-16 FAUX_APRES=6 FAUX_JOUR2=2026-11-17 FAUX_OFFRES="$OFFRES_AUCUNE"
# L08 à L10 : contrôles et jetons
cas L08-controles-ko 2 "contrôles avant dépense en échec" non "$S" 1 - "$J_OK" FAUX_KO=1
cas L09-controles-derniere-ligne 2 "contrôles : dernière ligne inattendue" non "$S" 1 - "$J_OK" FAUX_DERNIERE=1
JETONS_SAUF=("${JETONS[@]}"); JETONS=(HF_TOKEN=factice-hf-1111111 CONTROLE_IA_GITHUB_TOKEN=court)
cas L10-jeton-court 2 "jeton absent" non "$S" 1 - "$J_OK"
JETONS=(HF_TOKEN=factice-hf-1111111)
cas L10b-jeton-absent 2 "jeton absent" non "$S" 1 - "$J_OK"
JETONS=("${JETONS_SAUF[@]}")
# L11 à L13 : copies versées et preuves
S_COPIE=$(variante copie "echo '# ligne ajoutée' >> '$VERSEES/surveiller_p3bis_v1.sh'")
cas L11-copie-versee-autre 2 "surveiller_p3bis_v1.sh exécuté ≠ copie versée au commit S" non "$S_COPIE" 1 - "$J_OK"
S_PREUVE=$(variante preuve "git rm -q '$VERSEES/banc-recuperation-p3bis-v1.log'")
cas L12-preuve-absente 2 "journal banc-recuperation-p3bis-v1.log absent de S" non "$S_PREUVE" 1 - "$J_OK"
S_SCEAU=$(variante sceau "echo '0000000000000000000000000000000000000000000000000000000000000000  banc-lanceur-p3bis-v1.log' > '$VERSEES/banc-lanceur-p3bis-v1.log.sha256'")
cas L12b-preuve-sceau-faux 2 "sceau de banc-lanceur-p3bis-v1.log absent ou non conforme" non "$S_SCEAU" 1 - "$J_OK"
S_NC=$(variante nc "sed -i '1i cas 3 : NON CONFORME' '$VERSEES/banc-controles-p3bis-v1.log'; (cd '$VERSEES' && sha256sum banc-controles-p3bis-v1.log > banc-controles-p3bis-v1.log.sha256)")
cas L13-preuve-non-conforme 2 "ligne d'échec avant le verdict" non "$S_NC" 1 - "$J_OK"
# L14 à L18 : texte de S et commit de scellement
S_AM=$(variante amorce "texte GO-2026-11-02-29 GO-2026-11-02-29 calcul/p3bis-reel-v1 '$URL' $(printf '0%.0s' {1..64}) > '$P'; sceller_texte")
cas L14-amorce-non-citee 2 "empreinte de l'amorce" non "$S_AM" 1 - "$J_OK"
S_BR=$(variante br "texte GO-2026-11-02-29 GO-2026-11-02-29 calcul/p3bis-reel-v9 '$URL' '$E_AMORCE' > '$P'; sceller_texte")
cas L15-branche-citee-autre 2 "la ligne « Lancement » de S cite autre chose" non "$S_BR" 1 - "$J_OK"
S_URL=$(variante url "texte GO-2026-11-02-29 GO-2026-11-02-29 calcul/p3bis-reel-v1 https://github.com/lciric/controle-ia.git '$E_AMORCE' > '$P'; sceller_texte")
cas L16-depot-url-autre 2 "DEPOT_URL : la ligne « Lancement » de S cite autre chose" non "$S_URL" 1 - "$J_OK"
cas L17-pas-le-commit-de-scellement 2 "n'ajoute pas $P.sha256" non "$BASE" 1 - "$J_OK"
git -C "$E/depot" checkout -q -b locale "$S" && echo x > "$E/depot/locale.txt" && git -C "$E/depot" add locale.txt && git -C "$E/depot" rm -q --cached "$P.sha256" \
    && git -C "$E/depot" commit -qm "non poussé" && git -C "$E/depot" add "$P.sha256" && git -C "$E/depot" commit -qm "scellement non poussé"
S_LOC=$(git -C "$E/depot" rev-parse HEAD); git -C "$E/depot" checkout -q main
cas L18-scellement-non-pousse 2 "absent du dépôt distant" non "$S_LOC" 1 - "$J_OK"
# L19 à L22 : offres (douze essais, repli écrit)
cas L19-repli-ecrit 0 "À CONSIGNER AU REGISTRE DES DÉPENSES" oui "$S" 1 - "$J_OK" FAUX_OFFRES="$OFFRES_AUTRE_CPU"
apres L19 "repli : douze essais processeur exigé, ligne de repli écrite, offre hors EPYC 7513 prise" \
    "[ \$(grep -c '^essai d.offre [0-9]* sur 12 (processeur exigé) : code 3' '$E/traces-L19-repli-ecrit/lancement.txt') = 12 ] && grep -q 'seule la condition du processeur est retirée' '$E/traces-L19-repli-ecrit/repli-processeur.txt' && grep -qx 'offre créée 444' '$E/vastai-L19-repli-ecrit.txt'"
cas L20-aucune-offre-meme-en-repli 3 "aucune offre conforme, même en repli" non "$S" 1 - "$J_OK" FAUX_OFFRES="$OFFRES_AUCUNE"
cas L21-offre-au-troisieme-essai 0 "succès : True" oui "$S" 1 - "$J_OK" FAUX_OFFRES="$OFFRES_AUCUNE" FAUX_OFFRES_APRES="3:$OFFRE_EPYC"
apres L21 "trois essais, offre aux bornes exactes (2,10 USD/h, fiabilité 0,98, 30 cœurs) prise, aucun repli" \
    "[ \$(grep -c '^essai d.offre' '$E/traces-L21-offre-au-troisieme-essai/lancement.txt') = 3 ] && grep -qx 'offre créée 666' '$E/vastai-L21-offre-au-troisieme-essai.txt' && [ ! -e '$E/traces-L21-offre-au-troisieme-essai/repli-processeur.txt' ]"
cas L22-offres-illisibles 2 "offres : relecture impossible" non "$S" 1 - "$J_OK" FAUX_OFFRES="pas du json"
# L23 à L28 : instances et crédit
cas L23-instance-inconnue 2 "instances : non tolérée" non "$S" 1 - "$J_OK" FAUX_INSTANCES="[$TOL3, {\"id\": 61000002, \"actual_status\": \"running\", \"cur_state\": \"running\", \"dph_total\": 1.0}]"
cas L24-toleree-relancee 2 "instances : non tolérée" non "$S" 1 - "$J_OK" FAUX_INSTANCES='[{"id": 58936096, "actual_status": "running", "cur_state": "running", "dph_total": 1.0}]'
cas L25-nommee-en-marche-saine 0 "minimum 34.00 USD" oui "$S" 1 61000001:GO-2026-11-08-13 "$J_OK" FAUX_CREDIT=34.0 FAUX_INSTANCES="[$TOL3, {\"id\": 61000001, \"actual_status\": \"running\", \"cur_state\": \"running\", \"dph_total\": 1.4}]"
cas L25b-nommee-credit-court 3 "crédit insuffisant" non "$S" 1 61000001:GO-2026-11-08-13 "$J_OK" FAUX_CREDIT=33.99 FAUX_INSTANCES="[$TOL3, {\"id\": 61000001, \"actual_status\": \"running\", \"cur_state\": \"running\", \"dph_total\": 1.4}]"
cas L26-nommee-mais-arretee 2 "instances : non tolérée" non "$S" 1 61000001:GO-2026-11-08-13 "$J_OK" FAUX_INSTANCES="[$TOL3, {\"id\": 61000001, \"actual_status\": \"exited\", \"cur_state\": \"stopped\", \"dph_total\": 1.4}]"
cas L26b-nommee-go-inconnu 2 "instances : non tolérée" non "$S" 1 61000001:GO-2026-11-30-01 "$J_OK" FAUX_INSTANCES="[$TOL3, {\"id\": 61000001, \"actual_status\": \"running\", \"cur_state\": \"running\", \"dph_total\": 1.4}]"
cas L27-credit-insuffisant 3 "crédit insuffisant" non "$S" 1 - "$J_OK" FAUX_CREDIT=19.99
cas L27b-credit-exact 0 "minimum 20.00 USD" oui "$S" 1 - "$J_OK" FAUX_CREDIT=20.0
cas L28-credit-illisible 2 "crédit illisible" non "$S" 1 - "$J_OK" FAUX_USER_ILLISIBLE=1
# L29, L30, L34 : création
cas L29-creation-refusee 4 "création douteuse" oui "$S" 1 - "$J_OK" FAUX_CREATION='{"success": false, "msg": "offre indisponible"}'
apres L29 "création refusée : aucune ligne « instance » (aucune cible d'arrêt)" "! grep -q '^instance [0-9]' '$E/traces-L29-creation-refusee/lancement.txt'"
cas L30-reponse-illisible-jeton 4 "réponse illisible" oui "$S" 1 - "$J_OK" FAUX_CREATION='erreur factice factice-gi-2222222'
apres L30 "réponse illisible : jeton masqué dans reponse-masquee.txt" "grep -qF '***' '$E/traces-L30-reponse-illisible-jeton/reponse-masquee.txt'"
cas L34-jeton-dans-la-reponse 0 "succès : True" oui "$S" 1 - "$J_OK" FAUX_CREATION='{"success": true, "new_contract": 99999998, "msg": "jeton factice-hf-1111111"}'
# L31 : arguments et dossier
mkdir -p "$E/traces-L31-existant"
NCAS=$((NCAS + 1)); env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E/home" "${JETONS[@]}" "$J_OK" FAUX_VASTAI_JOURNAL="$E/v31.txt" bash "$L" "$S" "$E/traces-L31-existant" - 1 > "$E/c31.txt" 2>&1
[ $? = 2 ] && grep -q "existe déjà" "$E/c31.txt" && echo "L31-dossier-existant : CONFORME" || { echo "L31-dossier-existant : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
for x in "S-court:abc:$E/t31a:-:1" "numerique:$S:$E/123456:-:1" "marche:$S:$E/t31c:61000001:1" "N:$S:$E/t31d:-:4" "N0:$S:$E/t31e:-:0"; do
    IFS=: read -r nom a1 a2 a3 a4 <<< "$x"
    NCAS=$((NCAS + 1)); env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E/home" "${JETONS[@]}" "$J_OK" FAUX_VASTAI_JOURNAL="$E/v31.txt" bash "$L" "$a1" "$a2" "$a3" "$a4" > "$E/c31.txt" 2>&1
    [ $? = 2 ] && [ ! -e "$a2" ] && echo "L31-argument-$nom : CONFORME" || { echo "L31-argument-$nom : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
done
NCAS=$((NCAS + 1)); env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E/home" "${JETONS[@]}" bash "$L" "$S" "$E/t31f" - > "$E/c31.txt" 2>&1
[ $? = 2 ] && grep -q usage "$E/c31.txt" && echo "L31-usage : CONFORME" || { echo "L31-usage : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# L32 : garde de calcul du dépôt rejouée (registre lisible par le module, refusé par la garde : date illisible d'une autre ligne)
echo '| GO-2026-11-09-98 | 2026-13-45 | calcul | ligne aux dates illisibles (essai) | 1 USD | 2026-11-30 | Lazar | essai |' >> "$E/depot/registres/go.md"
cas L32-garde-de-calcul-refuse 2 "dates illisibles" non "$S" 1 - "$J_OK"
cp "$E/go-sain.md" "$E/depot/registres/go.md"
# L33 : outil de location introuvable
mkdir -p "$E/bin-sans"; ln -s /usr/bin/env "$E/bin-sans/env" 2>/dev/null; cp "$E/bin/date" "$E/bin-sans/date"
NCAS=$((NCAS + 1)); env -i PATH="$E/bin-sans:/usr/bin:/bin" HOME="$E/home" "${JETONS[@]}" "$J_OK" bash "$L" "$S" "$E/t33" - 1 > "$E/c33.txt" 2>&1
[ $? = 2 ] && grep -q "outil de location introuvable" "$E/c33.txt" && echo "L33-outil-introuvable : CONFORME" || { echo "L33-outil-introuvable : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# L35 : les instances tolérées ne sont jamais touchées (aucun verbe d'arrêt ni de destruction dans tout le banc)
NCAS=$((NCAS + 1))
if cat "$E"/vastai-*.txt | grep -E '^appel : ' | grep -vE '^appel : (search offers|show user|show instances|create instance)$' | grep -q .; then
    echo "L35-aucun-autre-verbe : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1))
else echo "L35-aucun-autre-verbe (ni arrêt ni destruction par le lanceur) : CONFORME"; fi
echo "cas joués : $NCAS"
echo "FIN DU BANC DU LANCEUR DE P3-BIS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ]
