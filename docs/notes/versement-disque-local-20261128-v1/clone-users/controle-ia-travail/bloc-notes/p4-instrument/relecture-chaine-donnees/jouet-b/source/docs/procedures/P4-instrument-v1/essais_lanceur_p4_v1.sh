#!/usr/bin/env bash
# Banc du lanceur de P4-instrument (R5), v1, décliné de docs/procedures/P3-premier-test-v2/essais_lanceur_p3_v1.sh sous un
# nom neuf (R12) : cas génériques repris (heure, place, contrôles, jetons, arguments, instances tolérées et autres
# projets, crédit, choix de l'offre la moins chère parmi les conformes avec ses pièges, offres relues gardées, création
# douteuse, jeton masqué, S absent du distant, fetch en échec, amorce non citée, branche autre, preuves des essais,
# dossier de traces relatif), plus les cas propres à P4 : dix-sept scripts de la chaîne égaux à leurs copies versées à
# S ; script de l'instance cité ; crédit sur 3,0 heures ; borne de l'étape recalculée (5,41 USD) ; instance 56799469
# tolérée seulement relue arrêtée ; GO cité GO-2026-10-20-07 seul (texte), d'un autre type, plafond sans le préfixe
# « 10 USD par lancement », échu ; révocation sous ses deux formes (ligne de GO de type « révocation » qui nomme chacun
# des cinq identifiants ; ligne R-… qui commence par « **Révocation de R-262** » ou « **Révocation de R-269** ») et ses
# cas sains ; accord du jour (absent, d'un autre jour, sans la forme exacte, sans citation du GO ni d'un message du
# jour, en double ; cas sain par message du jour) ; contrôle du module par sa ligne de commande (fichier du module
# changé dans le dépôt de travail) ; garde de calcul gelée rejouée sur la commande de création qui refuse une
# révocation consignée pendant l'appel (aucune création). Aucun appel réel n'est possible : faux outil de location
# (n'appelle aucun service ; journalise le verbe, l'étiquette et les variables non secrètes de --env, jamais un jeton),
# faux contrôles avant dépense, faux df (place disque fixée par le banc), HOME redirigé, clé d'API retirée, jetons
# factices. Dépôt d'essai : clone partagé de DEPOT_SOURCE au commit C (code, module de P4, registres réels, garde
# gelée), sans extraction des PDF ; base : ligne d'accord du jour ; copies versées des dix-sept scripts (celle du
# lanceur : celle du banc, dont seules les lignes DEPOT, B et V changent) et six journaux de preuve factices ; S :
# préenregistrement d'essai tiré du brouillon 4 (outils_essais_p4_v1.py) et son sceau ; dépôt nu local en guise de
# dépôt distant. Le module de P4 et le module commun sont réels : chaque appel du lanceur les joue.
# Usage : essais_lanceur_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
[ $# -eq 3 ] || { echo "usage : essais_lanceur_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; E=$(realpath -m "$3")
SOI=$(realpath "$0")
HN=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine
B4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/P4-instrument-v1.md
VERSEES=docs/procedures/P4-instrument-v1
GO=GO-2026-10-20-07
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh recuperation_p4_v1.sh repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh
        essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
export PYTHONDONTWRITEBYTECODE=1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
echo "script éprouvé : lancer_p4_v1.sh $(sha256sum "$HN/lancer_p4_v1.sh" | cut -d' ' -f1)"
echo "script éprouvé : verifications_p4_v1.py $(sha256sum "$HN/verifications_p4_v1.py" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
NON_CONFORMES=0
JOUR=$(date -u +%F); HIER=$(date -u -d yesterday +%F)
H=$E/B/p4-instrument/chaine
mkdir -p "$H" "$E/bin-vastai" "$E/home" "$E/bin-heure" "$E/bin-df"
cat > "$E/bin-vastai/vastai" <<'EOF'
#!/usr/bin/env bash
# faux vastai du banc du lanceur de P4 : n'appelle aucun service
J=${FAUX_VASTAI_JOURNAL:?}
echo "appel : $1 $2" >> "$J"
case "$1 $2" in
  "search offers") [ -n "${FAUX_OFFRES:-}" ] && { printf '%s\n' "$FAUX_OFFRES"; exit 0; }; printf '[{"id": 111, "gpu_name": "%s", "gpu_ram": 81920, "num_gpus": 1, "machine_id": 7101, "host_id": 8101, "dph_total": %s, "cpu_name": "%s", "cpu_arch": "amd64", "cpu_cores": 128, "cpu_cores_effective": %s, "cpu_ram": %s, "inet_down_cost": %s, "storage_total_cost": %s}, {"id": 222, "dph_total": 0.9, "cpu_name": "AMD EPYC 7513 32-Core Processor"}]\n' "${FAUX_GPU:-A100 SXM4}" "${FAUX_PRIX:-1.10}" "${FAUX_CPU:-AMD EPYC 7513 32-Core Processor}" "${FAUX_COEURS:-32.0}" "${FAUX_RAM:-128886}" "${FAUX_TEL:-0.025}" "${FAUX_STO:-0.015}" ;;
  "show user") [ -n "${FAUX_REVOQUER_PENDANT:-}" ] && echo "| GO-2026-10-20-95 | $(date -u +%F) | révocation | révoque GO-2026-10-20-07 pendant l appel (essai) | — | $(date -u +%F) | Lazar | essai |" >> "$FAUX_REVOQUER_PENDANT"
      [ -n "${FAUX_USER_ILLISIBLE:-}" ] && { echo "erreur factice"; exit 0; }; printf '{"credit": %s, "email": "x@invalid"}\n' "${FAUX_CREDIT:-20.0}" ;;
  "show instances") [ -n "${FAUX_INSTANCES_ECHEC:-}" ] && { echo "erreur factice" >&2; exit 1; }; d='[{"id": 56799469, "actual_status": "exited", "cur_state": "stopped", "label": "p3-v1", "extra_env": [["GH_TOKEN", "secret"]]}]'; printf '%s\n' "${FAUX_INSTANCES:-$d}" ;;
  "create instance")
    echo "CREATION FACTICE" >> "$J"
    echo "offre créée $3" >> "$J"
    a=("$@")
    for ((i = 0; i < ${#a[@]}; i++)); do
      [ "${a[$i]}" = "--label" ] && echo "etiquette ${a[$((i + 1))]}" >> "$J"
      if [ "${a[$i]}" = "--env" ]; then
        for kv in ${a[$((i + 1))]}; do case "$kv" in ETUDE=*|PREREG=*|BRANCHE=*|DEPOT_URL=*) echo "env $kv" >> "$J" ;; COMMIT=*) echo "env COMMIT présent" >> "$J" ;; esac; done
      fi
    done
    echo "go ${GO_ID:-absent}" >> "$J"
    d='{"success": true, "new_contract": 99999999}'; printf '%s\n' "${FAUX_CREATION:-$d}"; exit "${FAUX_CODE_CREATION:-0}" ;;
  *) echo "verbe inattendu" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin-vastai/vastai"
cat > "$H/controles_avant_depense_p4_v1.sh" <<'EOF'
#!/usr/bin/env bash
mkdir -p "$2" "$2.travail" && echo donnees > "$2/x"
echo "arguments : S=${1:0:12} ; $# arguments"
[ $# = 2 ] || { echo "KO  essai : nombre d'arguments"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; }
if [ -n "${FAUX_KO:-}" ]; then echo "OK  essai"; echo "KO  essai : faute simulée"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; fi
if [ -n "${FAUX_DERNIERE:-}" ]; then echo "OK  essai"; echo "dernière ligne inattendue (essai)"; exit 0; fi
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
cp "$HN/verifications_p4_v1.py" "$H/"
L=$H/lancer_p4_v1.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" -e "s|^V=.*|V=$E/bin-vastai/vastai|" "$HN/lancer_p4_v1.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$HN/lancer_p4_v1.sh" "$L" | grep -c '^>') (DEPOT, B, V)"
[ "$(diff "$HN/lancer_p4_v1.sh" "$L" | grep -c '^>')" = 3 ] && ! grep -q "venv-vastai" "$L" || { echo "copie du lanceur non sûre"; exit 2; }
cat > "$E/bin-heure/date" <<EOF
#!/usr/bin/env bash
if [ "\$*" = "-u +%H%M" ]; then
  n=\$(cat "$E/compteur-heure" 2>/dev/null || echo 0); n=\$((n+1)); echo \$n > "$E/compteur-heure"
  if [ "\$n" -ge 2 ]; then echo "\${FAUX_HEURE2:-2200}"; else echo "\${FAUX_HEURE1:-2200}"; fi; exit 0
fi
exec /usr/bin/date "\$@"
EOF
chmod +x "$E/bin-heure/date"
# faux df : place disque fixée par le banc (la machine de la session peut avoir moins de 3 Go libres ; le lanceur réel
# en juge, pas le banc) ; 2 900 000 ko sur le dossier nommé par le cas
cat > "$E/bin-df/df" <<EOF
#!/usr/bin/env bash
libre=9000000
[ -n "\${FAUX_DF_TRACES:-}" ] && [ "\${@: -1}" = "$E" ] && libre=2900000
[ -n "\${FAUX_DF_BLOC_NOTES:-}" ] && [ "\${@: -1}" = "$E/B" ] && libre=2900000
printf 'Filesystem 1024-blocks Used Available Capacity Mounted\n/dev/x 10000000 100 %s 1%% /\n' "\$libre"
EOF
chmod +x "$E/bin-df/df"
git clone -q --shared --no-checkout "$SRC" "$E/depot" && cd "$E/depot" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git sparse-checkout set --no-cone '/*' '!/docs/sources/pdf/' '!/docs/sources/lecture-pdf-niveau1/' '!/docs/sources/lecture-pdf-niveau2/' \
    && git checkout -q "$C" && git checkout -q -B main || exit 2
echo "C = $(git rev-parse HEAD)"
grep -q "^| $GO |" registres/go.md || { echo "$GO absent du registre de C"; exit 2; }
echo "| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours ; dépense consignée et borne de l'étape sous 150 USD. | essai |" >> registres/decisions.md
git add -A && git commit -qm "base : ligne d'accord du jour (essai)"
# copies versées à S des dix-sept scripts : les faux contrôles et le module commun du bloc-notes factice, le lanceur du
# banc, et les quatorze autres scripts, au bloc-notes factice et en copie versée (le lanceur compare les dix-sept)
mkdir -p "$VERSEES"
cp "$H/controles_avant_depense_p4_v1.sh" "$H/verifications_p4_v1.py" "$L" "$VERSEES/"
for s in $CHAINE; do
    case "$s" in controles_avant_depense_p4_v1.sh|verifications_p4_v1.py|lancer_p4_v1.sh) continue ;; esac
    cp "$HN/$s" "$VERSEES/" && cp "$HN/$s" "$H/" || { echo "copie versée factice impossible : $s"; exit 2; }
done
for s in $CHAINE; do (cd "$VERSEES" && sha256sum "$s" > "$s.sha256"); done
ep() { for s in "$@"; do echo "script éprouvé : $s $(sha256sum "$VERSEES/$s" | cut -d' ' -f1)"; done; }
journal_preuve() {   # $1 nom du journal, $2 dernière ligne, puis les scripts éprouvés
    local n=$1 v=$2; shift 2
    { echo "journal factice du banc du lanceur"; ep "$@"; echo "$v"; } > "$VERSEES/$n"
    (cd "$VERSEES" && sha256sum "$n" > "$n.sha256")
}
journaux_preuves() {
    journal_preuve banc-lanceur-p4-v1.log "FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0" lancer_p4_v1.sh verifications_p4_v1.py essais_lanceur_p4_v1.sh
    journal_preuve banc-surveillance-p4-v1.log "FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0" surveiller_p4_v1.sh controle_cinq_minutes_p4_v1.sh essais_surveillance_p4_v1.sh
    journal_preuve banc-verifications-p4-v1.log "FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0" verifications_p4_v1.py essais_verifications_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve banc-controles-p4-v1.log "FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0" controles_avant_depense_p4_v1.sh verifications_p4_v1.py essais_controles_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve banc-scellement-p4-v1.log "FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0" sceller_p4_v1.sh verifications_p4_v1.py essais_scellement_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve repetition-finale-p4-v1.log "RÉPÉTITION FINALE : CONFORME" sceller_p4_v1.sh controles_avant_depense_p4_v1.sh verifications_p4_v1.py repetition_finale_p4_v1.sh
}
journaux_preuves
git add -A "$VERSEES" && git commit -qm "essai : copies versées et journaux de preuve factices"
"$PY" -B "$HN/outils_essais_p4_v1.py" candidat "$B4" "$E/prereg-origine.md" . 7a54d431d89745839220f882b41b13e8c62ecfdd \
    "$(printf 0%.0s {1..64})" 1102 > /dev/null || { echo "texte d'essai impossible"; exit 2; }
cp "$E/prereg-origine.md" "$P" && (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
git add "$P" "$P.sha256" && git commit -qm "S : préenregistrement de P4 scellé (essai)"
S=$(git rev-parse HEAD); echo "S = $S"
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
cp registres/decisions.md "$E/decisions-sauve.md"; cp registres/go.md "$E/go-sauve.md"
cas() {   # $1 nom ; $2 code attendu ; $3 arguments du lanceur (« - » : les arguments normaux) ; puis l'environnement
    local nom=$1 attendu=$2 args=$3; shift 3
    rm -rf "$E/traces" "$E/compteur-heure"; : > "$E/journal-$nom.txt"
    local a=("$E/traces" - R-999); [ "$args" = "-" ] || read -r -a a <<<"$args"
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin-heure:$E/bin-df:/usr/bin:/bin" \
        HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 FAUX_VASTAI_JOURNAL="$E/journal-$nom.txt" \
        "$@" bash "$L" "${a[@]}" > "$E/sortie-$nom.txt" 2>&1
    local c=$?
    local cree; cree=$(grep -c "CREATION FACTICE" "$E/journal-$nom.txt")
    local v="CONFORME"; [ "$c" = "$attendu" ] || v="NON CONFORME (attendu $attendu)"
    [ "$attendu" != 0 ] && [ "$cree" != 0 ] && [ "$attendu" != 4 ] && v="NON CONFORME (création alors qu'un arrêt était attendu)"
    [ "$attendu" = 0 ] && [ "$cree" != 1 ] && v="NON CONFORME (pas de création)"
    local tr; tr=$(realpath -m "${a[0]:-$E/traces}")
    { [ -e "$tr/clone-controles" ] || [ -e "$tr/clone-controles.travail" ]; } && v="NON CONFORME (clone des contrôles resté)"
    [ -n "${MOTIF_CAS:-}" ] && ! grep -qF -- "$MOTIF_CAS" "$E/sortie-$nom.txt" && v="NON CONFORME (motif « $MOTIF_CAS » absent)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; créations factices $cree ; $v"
    grep -v '^$' "$E/sortie-$nom.txt" | tail -2 | sed 's/^/    | /' | couper 200
    [ -f "$tr/lancement.txt" ] && cp "$tr/lancement.txt" "$E/lancement-$nom.txt"
    [ -f "$tr/reponse-masquee.txt" ] && cp "$tr/reponse-masquee.txt" "$E/reponse-$nom.txt"
    return 0
}
cas P00-sain 0 - FAUX_X=1
grep -E "etiquette|env |^go " "$E/journal-P00-sain.txt" | sed 's/^/    > /'
python3 - "$E/lancement-P00-sain.txt" "$E/journal-P00-sain.txt" "$JOUR" <<'EOF' || { echo "    P00 : vérifications du cas sain : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
import re, sys
t = open(sys.argv[1], encoding="utf-8").read(); j = open(sys.argv[2], encoding="utf-8").read(); jour = sys.argv[3]
c = re.search(r"^creation (\d+)$", t, re.M)
pl = re.search(r"^plafond de la surveillance (\d+) \(création \+ 9600 s ; surveiller_p4_v1\.sh <id> (\d+) <dossier neuf>\)$", t, re.M)
cq = re.search(r"^contrôle à cinq minutes entre (\d+) et (\d+) \(création \+ 180 à 300 s ; controle_cinq_minutes_p4_v1\.sh <id> \S+ <dossier neuf>\)$", t, re.M)
v = {"plafond de la surveillance = création + 9 600 s": bool(c and pl and int(pl.group(1)) - int(c.group(1)) == 9600 and pl.group(2) == c.group(1)),
     "contrôle à cinq minutes = création + 180 à 300 s": bool(c and cq and int(cq.group(1)) - int(c.group(1)) == 180 and int(cq.group(2)) - int(c.group(1)) == 300),
     "branche calcul/p4-reel-v1": bool(re.search(r"^branche calcul/p4-reel-v1$", t, re.M) and re.search(r"^env BRANCHE=calcul/p4-reel-v1$", j, re.M)),
     "PREREG et DEPOT_URL": bool(re.search(r"^env PREREG=prereg/P4-instrument-v1\.md$", j, re.M) and re.search(r"^env DEPOT_URL=https://github\.com/lciric/controle-ia-travail\.git$", j, re.M)),
     "étiquette p4-v1": bool(re.search(r"^etiquette p4-v1$", j, re.M)), "ETUDE absente": "env ETUDE=" not in j,
     "GO GO-2026-10-20-07 écrit et porté par la création": bool(re.search(r"^go GO-2026-10-20-07$", t, re.M) and re.search(r"^go GO-2026-10-20-07$", j, re.M)),
     "GO et dépense conformes (module)": bool(re.search(r"^go et dépense GO-2026-10-20-07 conforme : échéance 2026-11-30 ; plafond « 10 USD par lancement", t, re.M)),
     "contrôles du module (ligne de commande)": bool(re.search(r"^contrôles du module : module de P4 conforme : 6 fichiers .*accord R-999 du .* garde de calcul gelée : conformes$", t, re.M)),
     "accord de Lazar du jour relu deux fois": len(re.findall(rf"^accord R-999 : accord de Lazar du {jour} pour le lancement de P4-instrument \(cite GO-2026-10-20-07\) : conforme$", t, re.M)) == 2,
     "instance 56799469 tolérée (arrêtée)": "56799469 (exited, stopped)" in t,
     "borne de l'étape écrite": "borne de l etape 5.41 USD (plafond par lancement : colonne « plafond » de GO-2026-10-20-07)" in t,
     "destruction après la récupération écrite": "détruite par son identifiant après la récupération vérifiée" in t,
     "crédit sur 3 heures": bool(re.search(r"minimum 4\.50 USD \(3 h\)$", t, re.M))}
print("    > " + " ; ".join(f"{k} : {x}" for k, x in v.items()))
sys.exit(0 if all(v.values()) else 1)
EOF
cas P01-creee-mais-code-1 4 - FAUX_CODE_CREATION=1
cas P02-reponse-illisible 4 - FAUX_CREATION=illisible
cas P03-echec-creation 4 - 'FAUX_CREATION={"success": false, "msg": "non"}'
cas P04-heure-2345-avant-creation 3 - FAUX_HEURE2=2345
cas P04b-heure-2340-au-depart 3 - FAUX_HEURE1=2340
cas P04c-heure-2329-au-depart 0 - FAUX_HEURE1=2329
cas P05-place-traces 3 - FAUX_DF_TRACES=1
MOTIF_CAS="place disque : " cas P05b-place-bloc-notes 3 - FAUX_DF_BLOC_NOTES=1
MOTIF_CAS="contrôles avant dépense en échec" cas P06-controles-ko 2 - FAUX_KO=1
MOTIF_CAS="aucune offre conforme" cas P07-offre-sans-prix 3 - FAUX_PRIX=null
MOTIF_CAS="aucune offre conforme" cas P07b-prix-au-dessus-du-devis 3 - FAUX_PRIX=1.35
MOTIF_CAS="aucune offre conforme" cas P07c-processeur-autre 3 - 'FAUX_CPU=Intel Xeon Platinum 8480+'
MOTIF_CAS="aucune offre conforme" cas P07d-carte-pcie 3 - 'FAUX_GPU=A100 PCIE'
MOTIF_CAS="aucune offre conforme" cas P07e-quinze-coeurs 3 - FAUX_COEURS=15.0
MOTIF_CAS="aucune offre conforme" cas P07f-memoire-vive-64-go 3 - FAUX_RAM=64000
MOTIF_CAS="aucune offre conforme" cas P07g-telechargement-au-dessus-de-la-borne 3 - FAUX_TEL=0.06
MOTIF_CAS="aucune offre conforme" cas P07h-stockage-au-dessus-de-la-borne 3 - FAUX_STO=0.031
cas P07i-stockage-et-telechargement-au-plafond-juste 0 - FAUX_TEL=0.05 FAUX_STO=0.03
# crédit exigé : 3,0 h × 1,10 + 1,2 = 4,50 USD
MOTIF_CAS="crédit insuffisant pour P4" cas P08-credit-insuffisant 3 - FAUX_CREDIT=4.49
MOTIF_CAS="minimum 4.50 USD (3 h)" cas P08b-credit-juste 0 - FAUX_CREDIT=4.50
MOTIF_CAS="crédit illisible (vastai show user" cas P08c-credit-illisible 2 - FAUX_USER_ILLISIBLE=1
MOTIF_CAS="jeton absent" cas P09-jeton-hf-absent 2 - HF_TOKEN=
MOTIF_CAS="jeton absent" cas P09b-jeton-github-absent 2 - CONTROLE_IA_GITHUB_TOKEN=
MOTIF_CAS="usage" cas P10-argument-absent 2 "" FAUX_X=1
MOTIF_CAS="usage" cas P10a-deux-arguments-sans-accord 2 "$E/traces -" FAUX_X=1
MOTIF_CAS="usage" cas P10b-quatre-arguments 2 "$E/traces - R-999 relance" FAUX_X=1
MOTIF_CAS="ACCORD : identifiant R-" cas P10c-accord-mal-forme 2 "$E/traces - 999" FAUX_X=1
MOTIF_CAS="autres instances sur le compte" cas P11-instance-non-toleree 2 - 'FAUX_INSTANCES=[{"id": 1, "actual_status": "running", "cur_state": "running"}]'
MOTIF_CAS="56799469 (running, running)" cas P11b-instance-de-p3-en-marche 2 - 'FAUX_INSTANCES=[{"id": 56799469, "actual_status": "running", "cur_state": "running", "label": "p3-v1"}]'
MOTIF_CAS="instances arrêtées tolérées : aucune" cas P11c-instance-de-p3-detruite 0 - 'FAUX_INSTANCES=[]'
MOTIF_CAS="autres instances sur le compte" cas P11d-ancienne-instance-du-programme-plus-toleree 2 - 'FAUX_INSTANCES=[{"id": 56438435, "actual_status": "exited", "cur_state": "stopped", "label": "t05-notations-v1"}]'
MOTIF_CAS="instances : non tolérée(s), ou liste illisible" cas P11e-liste-des-instances-illisible 2 - FAUX_INSTANCES_ECHEC=1
# constantes non fixées ou borne de l'étape autre que le calcul (copies du lanceur : une ligne change)
copie_l() {   # $1 sortie, $2 expression sed : une ligne exactement
    sed "$2" "$L" > "$1"; [ "$(diff "$L" "$1" | grep -c '^>')" = 1 ] || { echo "copie $1 : une ligne exactement attendue"; exit 2; }
}
L_SAUVE=$L
copie_l "$E/lanceur-z01.sh" 's/^ARRETEES_TOLEREES="[0-9 ]*"/ARRETEES_TOLEREES="A_EPINGLER"/'; L=$E/lanceur-z01.sh
MOTIF_CAS="instances tolérées non épinglées" cas Z01-instances-tolerees-non-epinglees 2 - FAUX_X=1; L=$L_SAUVE
copie_l "$E/lanceur-z02.sh" 's/^TELECHARGEMENT_MAX=[0-9.]* /TELECHARGEMENT_MAX=A_FIXER /'; L=$E/lanceur-z02.sh
MOTIF_CAS="borne de téléchargement non fixée" cas Z02-borne-de-telechargement-non-fixee 2 - FAUX_X=1; L=$L_SAUVE
copie_l "$E/lanceur-z03.sh" 's/^BORNE_ETAPE_USD=5.41 /BORNE_ETAPE_USD=5.40 /'; L=$E/lanceur-z03.sh
MOTIF_CAS="borne de l'étape (5.40 USD) ≠ calcul sur les constantes" cas Z03-borne-de-l-etape-autre-que-le-calcul 2 - FAUX_X=1; L=$L_SAUVE
copie_l "$E/lanceur-z04.sh" 's/^PLAFOND_SURVEILLANCE_S=9600 /PLAFOND_SURVEILLANCE_S=12000 /'; L=$E/lanceur-z04.sh
MOTIF_CAS="borne de l'étape (5.41 USD) ≠ calcul sur les constantes" cas Z04-surveillance-plus-longue-que-la-borne 2 - FAUX_X=1; L=$L_SAUVE
# dix-sept scripts égaux à leurs copies versées à S
for s in controles_avant_depense_p4_v1.sh surveiller_p4_v1.sh controle_cinq_minutes_p4_v1.sh verifications_p4_v1.py recuperation_p4_v1.sh p4_instance_v1.sh; do
    cp "$H/$s" "$E/sauve-$s"; echo "# modifié" >> "$H/$s"
    MOTIF_CAS="$s exécuté ≠ copie versée au commit S" cas "P14-$s-non-verse" 2 - FAUX_X=1
    cp "$E/sauve-$s" "$H/$s"
done
cp "$L" "$E/lanceur-sauve.sh"; echo "# modifié" >> "$L"
MOTIF_CAS="lancer_p4_v1.sh exécuté ≠ copie versée au commit S" cas P14b-lanceur-non-verse 2 - FAUX_X=1
cp "$E/lanceur-sauve.sh" "$L"
AVANT_P15=$(git -C "$E/distant.git" rev-parse refs/heads/main)
git -C "$E/distant.git" update-ref refs/heads/main "$(git -C "$E/depot" rev-parse "$S~1")"
MOTIF_CAS="absent du dépôt distant" cas P15-s-absent-du-distant 2 - FAUX_X=1
git -C "$E/distant.git" update-ref refs/heads/main "$AVANT_P15"
git -C "$E/depot" fetch -q origin
git -C "$E/depot" remote set-url origin "$E/distant-absent.git"
MOTIF_CAS="arrêt avant la création (ligne" cas N09-fetch-en-echec 2 - FAUX_X=1
git -C "$E/depot" remote set-url origin "$E/distant.git"
MOTIF_CAS="contrôles : dernière ligne inattendue" cas N07-controles-derniere-ligne-autre 2 - FAUX_DERNIERE=1
mkdir -p "$E/traces-existantes"
MOTIF_CAS="existe déjà (R12)" cas N05-traces-existantes 2 "$E/traces-existantes - R-999" FAUX_X=1
MOTIF_CAS="succès : True" cas N04-jeton-dans-la-reponse 0 - 'FAUX_CREATION={"success": true, "new_contract": 99999999, "msg": "jeton factice-hf-0000000 et factice-gh-0000000"}'
MOTIF_CAS="réponse illisible" cas N04b-jeton-dans-une-reponse-illisible 4 - 'FAUX_CREATION=erreur factice-gh-0000000 refusé'
# GO et dépense (registres courants du dépôt de travail)
go_col() {   # $1 colonne (1 à 8), $2 valeur : la ligne de GO-2026-10-20-07 du registre courant changée
    python3 - "$1" "$2" <<'PYG'
import sys
from pathlib import Path
k, val = int(sys.argv[1]), sys.argv[2]
g = Path("registres/go.md"); L = g.read_text(encoding="utf-8").split("\n")
L = ["|".join(c if i != k else f" {val} " for i, c in enumerate(l.split("|"))) if l.startswith("| GO-2026-10-20-07 |") else l for l in L]
g.write_text("\n".join(L), encoding="utf-8")
PYG
}
go_col 6 "$HIER"
# GO échu : l'accord du jour, relu avant le GO, le refuse déjà (il exige le GO cité en vigueur ce jour-là)
MOTIF_CAS="accord de Lazar : accord R-999 : $GO échu ou illisible le" cas G01-go-echu 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
go_col 3 revendication
MOTIF_CAS="GO et dépense : $GO : ligne de huit colonnes, de type « calcul »" cas G02-go-d-un-autre-type 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
go_col 5 "12 USD par lancement (essai)"
MOTIF_CAS="la colonne « plafond » ne commence pas par « 10 USD par lancement »" cas G03-plafond-sans-le-prefixe 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
for x in GO-2026-10-04-08 GO-2026-10-20-06 GO-2026-10-20-07 R-262 R-269; do
    echo "| GO-2026-10-20-98 | $JOUR | révocation | révoque $x (essai) | — | $JOUR | Lazar | essai |" >> registres/go.md
    MOTIF_CAS="révocation au registre des GO (GO-2026-10-20-98)" cas "G04-revocation-qui-nomme-$x" 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
done
echo "| GO-2026-10-20-97 | $JOUR | décision | essai : aucune révocation de $GO | — | $JOUR | Lazar | essai |" >> registres/go.md
cas G04b-ligne-qui-mentionne-une-revocation 0 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
for x in R-262 R-269; do
    echo "| R-998 | $JOUR | **Révocation de $x** pour P4 (essai). | essai |" >> registres/decisions.md
    MOTIF_CAS="révocation au registre des décisions (R-998)" cas "G05-revocation-de-$x-au-registre-des-decisions" 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
done
echo "| R-994 | $JOUR | Note (essai) : la forme « **Révocation de R-269** » est décrite ici, sans révoquer. | essai |" >> registres/decisions.md
cas G05b-forme-de-revocation-ailleurs-qu-en-tete 0 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
# garde de calcul gelée rejouée sur la commande de création : une révocation consignée pendant l'appel (après les
# contrôles du GO, avant la création) est refusée par la garde ; aucune création
MOTIF_CAS="commande bloquée : $GO révoqué par GO-2026-10-20-95" cas G06-revocation-pendant-l-appel-refusee-par-la-garde 2 - FAUX_REVOQUER_PENDANT="$E/depot/registres/go.md"
grep -q "arrêt avant la création (ligne" "$E/sortie-G06-revocation-pendant-l-appel-refusee-par-la-garde.txt" && echo "    G06 : arrêt par le piège ERR à la garde rejouée, aucune création : CONFORME" \
    || { echo "    G06 : arrêt à la garde rejouée non établi : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cp "$E/go-sauve.md" registres/go.md
# accord du jour
sed -i '/^| R-999 |/d' registres/decisions.md
MOTIF_CAS="accord de Lazar : R-999 absent ou en double" cas A10-accord-absent 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "s/^| R-999 | $JOUR |/| R-999 | $HIER |/" registres/decisions.md
MOTIF_CAS="ligne du jour ($JOUR) attendue" cas A11-accord-d-un-autre-jour 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "s/^| R-999 | $JOUR | .*/| R-999 | $JOUR | Délégation (essai) : accord de Lazar pour le lancement de P4-instrument, $GO. | essai |/" registres/decisions.md
MOTIF_CAS="ne commence pas par « **Accord de Lazar pour le lancement de P4-instrument** »" cas A12-sans-la-forme-exacte 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "s/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai). | essai |/" registres/decisions.md
MOTIF_CAS="ne cite ni $GO ni un message de Lazar" cas A13-ne-cite-ni-go-ni-message 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
grep '^| R-999 |' registres/decisions.md > "$E/accord.txt" && cat "$E/accord.txt" >> registres/decisions.md
MOTIF_CAS="R-999 absent ou en double" cas A14-accord-en-double 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "s/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : message de Lazar dans la session ce jour-là. | essai |/" registres/decisions.md
MOTIF_CAS="(cite un message de Lazar du jour) : conforme" cas A15-accord-par-message-du-jour 0 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
# contrôle du module par sa ligne de commande : un test du module changé dans le dépôt de travail (hors de l'arbre de S)
cp "$VERSEES/test_gardes_p4_v1.py" "$E/sauve-test-gardes.py"; echo "# essai" >> "$VERSEES/test_gardes_p4_v1.py"
MOTIF_CAS="contrôle du module (--controle module)" cas M01-fichier-du-module-change 2 - FAUX_X=1
cp "$E/sauve-test-gardes.py" "$VERSEES/test_gardes_p4_v1.py"
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "dépôt d'essai non rétabli"; exit 2; }
copie_l "$E/lanceur-sans-s.sh" "s|^P=prereg/P4-instrument-v1.md|P=prereg/absent-v1.md|"; L=$E/lanceur-sans-s.sh
MOTIF_CAS="commit de scellement introuvable" cas N08-s-introuvable 2 - FAUX_X=1; L=$L_SAUVE
# texte de S : amorce ou script de l'instance non cités, branche autre, ligne du GO absente ou autre (S refait par un
# retrait puis un ajout du sceau, puis rétabli)
nouveau_s() {   # $1 expression sed sur le préenregistrement (vide : texte d'origine)
    git rm -q "$P" "$P.sha256" && git commit -qm "essai : retrait du préenregistrement"
    mkdir -p "$(dirname "$P")" && cp "$E/prereg-origine.md" "$P" || { echo "nouveau S : copie impossible"; exit 2; }
    [ -n "$1" ] && { sed -i "$1" "$P"; cmp -s "$P" "$E/prereg-origine.md" && { echo "nouveau S : l'expression n'a rien changé"; exit 2; }; }
    (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
    git add "$P" "$P.sha256" && git commit -qm "essai : S refait" && git push -q origin HEAD:main && git fetch -q origin \
        || { echo "nouveau S : commit ou poussée impossible"; exit 2; }
}
nouveau_s "s|\`$VERSEES/amorce_instance_p4_v1.sh\` (\`[0-9a-f]\{64\}\`, sha256)|\`$VERSEES/amorce_instance_p4_v1.sh\` (\`$(printf '0%.0s' {1..64})\`, sha256)|"
MOTIF_CAS="empreinte de l'amorce" cas N01-amorce-non-citee 2 - FAUX_X=1
nouveau_s "s|\`$VERSEES/p4_instance_v1.sh\` (\`[0-9a-f]\{64\}\`, sha256)|\`$VERSEES/p4_instance_v1.sh\` (\`$(printf '0%.0s' {1..64})\`, sha256)|"
MOTIF_CAS="empreinte du script de l'instance" cas N01b-script-de-l-instance-non-cite 2 - FAUX_X=1
nouveau_s "s/BRANCHE=calcul\/p4-reel-v1/BRANCHE=calcul\/p4-reel-v9/"
MOTIF_CAS="PREREG ou BRANCHE : le préenregistrement de S cite autre chose" cas N02-branche-autre 2 - FAUX_X=1
nouveau_s "/\*\*GO cité par la commande de création\*\*/d"
MOTIF_CAS="GO et dépense : ligne « **GO cité par la commande de création** : \`GO_ID=…\` » absente" cas G07-ligne-go-absente 2 - FAUX_X=1
nouveau_s "s/\`GO_ID=$GO\`/\`GO_ID=GO-2026-10-04-08\`/"
MOTIF_CAS="GO et dépense : GO-2026-10-04-08 : seul $GO est accepté" cas G08-texte-qui-cite-le-go-de-la-phase 2 - FAUX_X=1
nouveau_s ""
cas N00-sain-apres-retablissement 0 - FAUX_X=1
# preuves des essais : journal au verdict non conforme, empreinte d'un script éprouvé ≠ copie versée, journal absent,
# journal sans son sceau exact, script attendu non éprouvé
preuve_alteree() { eval "$1" && git add -A "$VERSEES" && git commit -qm "essai : preuves altérées" || { echo "preuves : altération impossible"; exit 2; }; nouveau_s ""; }
retablir_preuves() { journaux_preuves && git add -A "$VERSEES" && git commit -qm "essai : preuves rétablies" && nouveau_s "" || { echo "preuves : rétablissement impossible"; exit 2; }; }
preuve_alteree "sed -i 's/cas non conformes : 0/cas non conformes : 1/' $VERSEES/banc-verifications-p4-v1.log && (cd $VERSEES && sha256sum banc-verifications-p4-v1.log > banc-verifications-p4-v1.log.sha256)"
MOTIF_CAS="preuves des essais : journal banc-verifications-p4-v1.log : dernière ligne" cas P30a-preuve-verdict-non-conforme 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i \"s/^script éprouvé : sceller_p4_v1.sh .*/script éprouvé : sceller_p4_v1.sh $(printf '7%.0s' {1..64})/\" $VERSEES/banc-scellement-p4-v1.log $VERSEES/repetition-finale-p4-v1.log && (cd $VERSEES && sha256sum banc-scellement-p4-v1.log > banc-scellement-p4-v1.log.sha256 && sha256sum repetition-finale-p4-v1.log > repetition-finale-p4-v1.log.sha256)"
MOTIF_CAS="preuves des essais : sceller_p4_v1.sh éprouvé" cas P30b-preuve-script-autre-que-la-copie 2 - FAUX_X=1
retablir_preuves
preuve_alteree "git rm -q $VERSEES/banc-surveillance-p4-v1.log $VERSEES/banc-surveillance-p4-v1.log.sha256"
MOTIF_CAS="preuves des essais : journal banc-surveillance-p4-v1.log absent de S" cas P30c-preuve-absente 2 - FAUX_X=1
retablir_preuves
preuve_alteree "echo ajout >> $VERSEES/banc-lanceur-p4-v1.log"
MOTIF_CAS="preuves des essais : sceau de banc-lanceur-p4-v1.log" cas P30d-preuve-sans-son-sceau 2 - FAUX_X=1
retablir_preuves
preuve_alteree "sed -i '/^script éprouvé : outils_essais_p4_v1.py /d' $VERSEES/banc-controles-p4-v1.log && (cd $VERSEES && sha256sum banc-controles-p4-v1.log > banc-controles-p4-v1.log.sha256)"
MOTIF_CAS="scripts éprouvés ≠ attendus (manquants ['outils_essais_p4_v1.py']" cas P30e-preuve-script-non-eprouve 2 - FAUX_X=1
retablir_preuves
MOTIF_CAS="preuves des essais : six journaux conformes ; 13 scripts éprouvés égaux à leurs copies versées à S" cas P30f-preuves-saines-apres-retablissement 0 - FAUX_X=1
# instances d'autres projets nommées en argument, tolérées seulement à l'étiquette « rr- » ; crédit exigé :
# 3,0 h × (1,10 + 4,004) + 1,2 = 16,51 USD
ARRETEE='{"id": 56799469, "actual_status": "exited", "cur_state": "stopped", "label": "p3-v1"}'
AUTRE='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "rr-autre-projet-essai", "dph_total": 4.004, "extra_env": [["GH_TOKEN", "secret"]]}'
AUTRE_ARRETEE='{"id": 55555587, "actual_status": "exited", "cur_state": "stopped", "label": "rr-autre-projet-essai", "dph_total": 4.004}'
AUTRE_P4='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "p4-v1", "dph_total": 1.1}'
AUTRE_SANS_PRIX='{"id": 55555587, "actual_status": "running", "cur_state": "running", "label": "rr-autre-x", "dph_total": null}'
MOTIF_CAS="instances d'autres projets tolérées : 55555587 (running, running, 4.004 USD/h, en marche, comptée)" cas V01-autre-projet-en-marche-tolere 0 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEE, $AUTRE]" FAUX_CREDIT=16.51
MOTIF_CAS="autres instances sur le compte" cas V02-autre-projet-non-declare 2 - "FAUX_INSTANCES=[$ARRETEE, $AUTRE]" FAUX_CREDIT=50
MOTIF_CAS="crédit insuffisant pour P4 et les autres projets en marche" cas V03-credit-insuffisant-avec-autre-projet 3 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEE, $AUTRE]" FAUX_CREDIT=16.50
MOTIF_CAS="55555587 (running, running)" cas V04-autre-projet-etiquette-p4 2 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEE, $AUTRE_P4]" FAUX_CREDIT=50
MOTIF_CAS="AUTRES_PROJETS : identifiants d'instances" cas V05-autres-mal-forme 2 "$E/traces abc R-999" FAUX_X=1
MOTIF_CAS="55555587 (exited, stopped, 4.004 USD/h, arrêtée)" cas V07-autre-projet-arrete-non-compte 0 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEE, $AUTRE_ARRETEE]" FAUX_CREDIT=4.50
MOTIF_CAS="55555587 (prix illisible)" cas V08-autre-projet-sans-prix 2 "$E/traces 55555587 R-999" "FAUX_INSTANCES=[$ARRETEE, $AUTRE_SANS_PRIX]" FAUX_CREDIT=50
# choix de l'offre parmi les conformes relues après les contrôles (bloc repris tel quel de P3)
EPYC="AMD EPYC 7513 32-Core Processor"
off() {   # identifiant prix [carte [processeur [mémoire [cartes [machine [hôte [cœurs [mémoire vive [téléchargement [stockage]]]]]]]]]]
    printf '{"id": %s, "gpu_name": "%s", "cpu_name": "%s", "gpu_ram": %s, "num_gpus": %s, "machine_id": %s, "host_id": %s, "dph_total": %s, "cpu_cores_effective": %s, "cpu_ram": %s, "inet_down_cost": %s, "storage_total_cost": %s}' \
        "$1" "${3:-A100 SXM4}" "${4:-$EPYC}" "${5:-81920}" "${6:-1}" "${7:-7100}" "${8:-8100}" "$2" "${9:-32.0}" "${10:-128886}" "${11:-0.025}" "${12:-0.015}"
}
MOTIF_CAS="offre choisie : 112 (1.05 USD/h), la moins chère des offres conformes" cas O01-moins-chere-des-conformes 0 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.05), $(off 113 1.20), $(off 114 0.80 "A100 SXM4" "Intel Xeon"), $(off 115 0.70 "A100 PCIE"), $(off 116 1.35), $(off 117 null), $(off true 0.5), $(off 118 true), $(off 122 0), $(off 125 0.9 "A100 SXM4" "$EPYC" 40960), $(off 126 0.9 "A100 SXM4" "$EPYC" 81920 2), $(off 131 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 15.0), $(off 132 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 64000), $(off 133 0.9 "A100 SXM4" "$EPYC" 81920 1 7100 8100 32.0 128886 0.06)]"
grep -qx "offre créée 112" "$E/journal-O01-moins-chere-des-conformes.txt" && [ "$(python3 -c 'import json,sys; print(len(json.load(open(sys.argv[1]))))' "$E/traces/offres-relues.json")" = 15 ] \
    && echo "    O01 : offre créée 112 ; 15 offres relues gardées : CONFORME" || { echo "    O01 : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
MOTIF_CAS="offre choisie : 119 (1.05 USD/h)" cas O02-egalite-de-prix-plus-petit-identifiant 0 - "FAUX_OFFRES=[$(off 120 1.05), $(off 119 1.05)]"
MOTIF_CAS="aucune offre conforme au filtre du plan" cas O03-aucune-offre 3 - "FAUX_OFFRES=[]"
MOTIF_CAS="offres : relecture impossible" cas O05-offres-illisibles 2 - "FAUX_OFFRES=pas du json"
MOTIF_CAS="offre choisie : 140 (1.3 USD/h)" cas O07-prix-au-plafond-juste 0 - "FAUX_OFFRES=[$(off 140 1.30)]" FAUX_CREDIT=50
# crédit exigé avec l'offre choisie parmi plusieurs : 3,0 h × 1,00 + 1,2 = 4,20 USD
MOTIF_CAS="minimum 4.20 USD (3 h)" cas O08-credit-calcule-sur-l-offre-choisie 0 - "FAUX_OFFRES=[$(off 111 1.10), $(off 112 1.00)]" FAUX_CREDIT=4.20
MOTIF_CAS="offres : identifiant en double" cas O11-identifiant-en-double 2 - "FAUX_OFFRES=[$(off 112 1.05), $(off 112 1.25)]"
# dossier de traces purement numérique ; dossier de traces relatif (écrit en chemin absolu)
MOTIF_CAS="DOSSIER_TRACES purement numérique" cas A01-traces-numeriques 2 "$E/29296808 - R-999" FAUX_X=1
pushd "$E" > /dev/null && cas A03-traces-en-chemin-relatif 0 "traces-relatives - R-999" FAUX_X=1; popd > /dev/null
[ -s "$E/traces-relatives/lancement.txt" ] && grep -q "^creation " "$E/traces-relatives/lancement.txt" \
    && echo "    A03 : traces écrites sous $E/traces-relatives (chemin absolu) : CONFORME" \
    || { echo "    A03 : traces relatives : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# jeton affiché : compté (sorties, lancements, journaux du faux outil, réponses masquées)
FUITES=$(grep -l 'secret\|factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/lancement-*.txt "$E"/journal-*.txt "$E"/reponse-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { printf '%s\n' $FUITES | sed 's/^/JETON AFFI''CHÉ : /'; NON_CONFORMES=$((NON_CONFORMES + 1)); }
P_CACHE=$(find "$E/depot/src" "$E/depot/$VERSEES" "$H" "$HN" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
