#!/usr/bin/env bash
# Répétition locale de la machine du crible (iii) — v1 : l'amorce et le programme machine réels, joués dans un dossier jetable, avec un
# dépôt jouet `file://` (branches de sortie et d'entrée comprises), une doublure du loueur (127.0.0.1), des doublures du lanceur, de
# la mesure et de la lecture, des valeurs factices pour le jeton et la clé ; les feux sont donnés par l'outil réel de la session
# (`session_crible_iii_v1.sh`) contre le dépôt jouet. Aucun appel au loueur, aucun fournisseur, aucune clé employée.
# Cas : 1. parcours complet (trois barrières, phrase chiffrée, inscriptions, essai à blanc, crible « réel » à blanc, mesure, lecture,
# rapatriement, état « fini », balayage) ; 2. feu d'arrêt pendant l'attente du feu 2 ; 3. phrase absente (arrêt à l'échéance de la
# barrière 1), puis minuterie à l'échéance (DELETE à la doublure du loueur) ; 4. refus de l'amorce avant la minuterie (destruction
# demandée par l'instance) ; 5. branche de sortie déjà présente (rien n'est poussé) ; 6. commande imprimée par l'outil de la session
# (offre choisie par la garde, lignes de GO lues, amorce essayée), comparée, sans aucune valeur de clé.
# Usage : bash repetition_machine_crible_iii_v1.sh PYTHON PAQUET_ARBRE DOSSIER_SONDE    (code 0 si chaque cas rend l'attendu)
set -uo pipefail
ICI="$(cd "$(dirname "$0")" && pwd)"
PYV="$1"; BUNDLE="$2"; SONDE="$3"
R=$(mktemp -d); K=0; KO=0
ok() { K=$((K + 1)); echo "CAS OK  | $*"; }
ko() { K=$((K + 1)); KO=$((KO + 1)); echo "CAS ÉCHEC | $*"; }
DC=docs/procedures/crible-iii-v1
PL=docs/notes/organisme-multi-generations-v1/pilote-v1
JOUR=$(date -u +%F)
# --- dépôt jouet --------------------------------------------------------------------------------------------------------------
git init -q --bare "$R/depot.git" && git -C "$R/depot.git" config uploadpack.allowFilter true \
    && git -C "$R/depot.git" config uploadpack.allowAnySHA1InWant true && git clone -q "$R/depot.git" "$R/travail" 2>/dev/null
cd "$R/travail" && git config user.name repetition && git config user.email repetition@invalid
mkdir -p "$DC" "$PL/procedure-pilote-v74-compte-organisme" "$PL/sonde-complete-v74-compte-organisme" prereg registres
for f in crible_iii_v1.py lanceur_crible_iii_v1.py mesure_crible_iii_v1.py lire_crible_iii_v1.py relais_factice_crible_iii_v1.py \
    machine_crible_iii_v1.sh machine_crible_iii_v1.py amorce_crible_iii_v1.sh; do cp "$ICI/$f" "$DC/"; done
cp "$BUNDLE" "$PL/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle"
cp -a "$SONDE" "$PL/sonde-complete-v74-compte-organisme/sonde-complete-v74"
printf 'Texte de répétition du crible (iii), factice, jamais un préenregistrement.\n' > prereg/crible-iii-repetition-v1.md
TS=$(sha256sum < prereg/crible-iii-repetition-v1.md | cut -d' ' -f1); echo "$TS  crible-iii-repetition-v1.md" > prereg/crible-iii-repetition-v1.md.sha256
{ echo "Addendum de répétition : texte $TS"; for f in crible_iii_v1.py lanceur_crible_iii_v1.py mesure_crible_iii_v1.py lire_crible_iii_v1.py \
    relais_factice_crible_iii_v1.py; do echo "$(sha256sum < "$DC/$f" | cut -d' ' -f1)  $DC/$f"; done; } > prereg/crible-iii-repetition-v1-addendum.md
AS=$(sha256sum < prereg/crible-iii-repetition-v1-addendum.md | cut -d' ' -f1); echo "$AS  crible-iii-repetition-v1-addendum.md" > prereg/crible-iii-repetition-v1-addendum.md.sha256
cat > registres/go.md <<EOF
| identifiant | accordé | type | périmètre | plafond | échéance | par | référence |
| GO-2026-11-17-91 | $JOUR | calcul | Organisme d'idéation, crible (iii) « deux passes » (répétition factice) : fable52 et opus55 | 260 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; répétition |
| GO-2026-11-17-92 | $JOUR | calcul | Même crible, part hors crédits : machine jetable seule (répétition factice) | 3 USD | 2026-11-30 | Lazar | GO-2026-11-15-06 ; répétition |
EOF
git add -A && git commit -q -m "dépôt jouet de la répétition" && git push -q origin HEAD:refs/heads/main
CM=$(git rev-parse HEAD); git fetch -q origin +refs/heads/main:refs/remotes/origin/main
SH=$(sha256sum < "$DC/machine_crible_iii_v1.sh" | cut -d' ' -f1); AH=$(sha256sum < "$DC/machine_crible_iii_v1.py" | cut -d' ' -f1)
# --- doublures --------------------------------------------------------------------------------------------------------------------
mkdir -p "$R/bin" "$R/doubles" "$R/envoi"; ln -s "$PYV" "$R/bin/python3"
for n in lanceur mesure lire; do printf 'import sys\nsys.path.insert(0, %s)\nimport doublures_repetition_crible_iii_v1 as D\nraise SystemExit(D.main([%s] + sys.argv[1:]))\n' \
    "'$ICI'" "'$n'" > "$R/doubles/$n.py"; done
PORT=$("$PYV" -I -c 'import socket; s = socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1])')
"$PYV" -I -B "$ICI/doublures_repetition_crible_iii_v1.py" loueur "$PORT" "$R/loueur.log" & PIDL=$!
sleep 1
OUTIL="env W=$R/travail ENVP=$R/envoi PYTHON_SESSION=$PYV VASTAI=/inexistant bash $ICI/session_crible_iii_v1.sh"
lancer_machine() {  # $1 = racine ; $2 = suffixe des branches ; $3 = échéance (s depuis maintenant) ; $4 = attente de la phrase (s) ; $5 = identifiant
    setsid env -i PATH=/usr/local/bin:/usr/bin:/bin HOME="$R" AMORCE_ESSAI=1 RACINE_AMORCE="$1" DEPOT_URL_ESSAI="file://$R/depot.git" \
        API_VAST_ESSAI="http://127.0.0.1:$PORT" PAS_MINUTERIE_S=1 ATTENTE_REFUS_S=0 COMMIT_LOT="$CM" COMMIT_MAIN="$CM" \
        BR_SORTIE="calcul/crible-iii-sortie-$2" BR_ENTREE="calcul/crible-iii-entree-$2" ECHEANCE_UTC_S=$(( $(date +%s) + $3 )) \
        GO_ID=GO-2026-11-17-92 GO_CREDITS=GO-2026-11-17-91 GO_HORS=GO-2026-11-17-92 TEXTE_CHEMIN=prereg/crible-iii-repetition-v1.md \
        TEXTE_SHA256="$TS" ADDENDUM_CHEMIN=prereg/crible-iii-repetition-v1-addendum.md ADDENDUM_SHA256="$AS" SCRIPT_SHA256="$SH" \
        AIDE_SHA256="$AH" GH_TOKEN=factice-jeton-repetition-0001 RR_ANTHROPIC_API_KEY_RIGAUD=factice-cle-repetition-0001 \
        CONTAINER_ID="$5" CONTAINER_API_KEY=factice PATH_O_ESSAI="$R/bin:/usr/local/bin:/usr/bin:/bin" NUMPY_ESSAI="$("$R/bin/python3" -I -c 'import numpy; print(numpy.__version__)')" \
        ESSAI_SANS_PIP=1 ESSAI_SANS_TLS=1 ESSAI_REEL_A_BLANC=1 ESSAI_LANCEUR="$R/doubles/lanceur.py" ESSAI_MESURE="$R/doubles/mesure.py" \
        ESSAI_LIRE="$R/doubles/lire.py" ATTENTE_PHRASE_S="$4" ATTENTE_FEU_S=120 PAS_ENTREE_S=2 PAS_ETAT_S=5 BUDGET_REEL_S=30 PAS_REPRISE_S=3 \
        bash "$ICI/amorce_crible_iii_v1.sh" > "$1.log" 2>&1 < /dev/null &
    echo $!; }
etape() { git -C "$R/travail" fetch -q origin "+refs/heads/calcul/crible-iii-sortie-$1:refs/remotes/origin/s-$1" 2>/dev/null
    git -C "$R/travail" show "refs/remotes/origin/s-$1:etat.txt" 2>/dev/null | sed -n 's/^etape=//p'; }
attendre() {  # $1 suffixe ; $2 étape attendue ; $3 délai (s)
    local n=0; while [ "$n" -lt "$3" ]; do [ "$(etape "$1")" = "$2" ] && return 0; sleep 2; n=$((n + 2)); done; return 1; }
inscrire() {  # $1 nom ; puis empreintes : fichier sur main du dépôt jouet ; imprime le commit
    local f="registres/inscription-$1.md"
    ( cd "$R/travail" && git fetch -q origin +refs/heads/main:refs/remotes/origin/main && git checkout -q -B main refs/remotes/origin/main \
      && shift && printf '%s\n' "$@" > "$f" && git add "$f" && git commit -q -m "inscription $f" && git push -q origin HEAD:refs/heads/main \
      && git rev-parse HEAD ); }
tuer() {  # arrêt de la machine jouet par son identifiant de groupe (= PID du programme machine, lancé par setsid ; R10)
    kill -TERM -- "-$1" 2>/dev/null; sleep 1; kill -KILL -- "-$1" 2>/dev/null; wait "$1" 2>/dev/null; }
# --- cas 1 : parcours complet ------------------------------------------------------------------------------------------------------
P1=$(lancer_machine "$R/m1" rep1 3600 300 4241)
if attendre rep1 "attente du feu 1 (phrase)" 240; then
    SS=$(git -C "$R/travail" show refs/remotes/origin/s-rep1:secret-sha256.txt | sed -n 's/^secret_sha256=//p')
    C1=$(inscrire secret-rep1 "$SS" | tail -n 1)
    ( umask 077; printf 'phrase publique de la répétition, jamais une vraie\n' > "$R/envoi/phrase.txt" )
    $OUTIL feu-phrase calcul/crible-iii-sortie-rep1 calcul/crible-iii-entree-rep1 "$R/envoi/phrase.txt" "$C1" registres/inscription-secret-rep1.md > "$R/feu1.txt" 2>&1
    [ ! -e "$R/envoi/phrase.txt" ] && ok "cas 1 : feu de la phrase chiffrée poussé, fichier de la phrase effacé" || ko "cas 1 : feu de la phrase ($(tail -n 2 "$R/feu1.txt"))"
    PH=$(sed -n 's/.*(à inscrire) : \([0-9a-f]*\)$/\1/p' "$R/feu1.txt")
    if attendre rep1 "attente du feu 2 (mondes)" 120; then
        EM=$(git -C "$R/travail" show refs/remotes/origin/s-rep1:engagement-mondes.json | "$PYV" -I -c 'import json,sys;e=json.load(sys.stdin);print(e["fichier_mondes_sha256"], *e["mondes_sha256"])')
        # shellcheck disable=SC2086
        C2=$(inscrire mondes-rep1 "phrase $PH" $EM | tail -n 1)
        $OUTIL feu-mondes calcul/crible-iii-sortie-rep1 calcul/crible-iii-entree-rep1 "$C2" registres/inscription-mondes-rep1.md > "$R/feu2.txt" 2>&1 \
            && ok "cas 1 : vingt mondes engagés, inscrits, feu des mondes poussé" || ko "cas 1 : feu des mondes ($(tail -n 1 "$R/feu2.txt"))"
        $OUTIL feu-reel calcul/crible-iii-sortie-rep1 calcul/crible-iii-entree-rep1 GO-2026-11-17-91 GO-2026-11-17-92 > "$R/feu3-tot.txt" 2>&1 \
            && ko "cas 1 : feu réel accepté avant l'attente du feu 3" || ok "cas 1 : feu réel refusé par l'outil avant l'attente du feu 3"
        if attendre rep1 "attente du feu 3 (crible reel)" 120; then
            $OUTIL feu-reel calcul/crible-iii-sortie-rep1 calcul/crible-iii-entree-rep1 GO-2026-11-17-91 GO-2026-11-17-92 > "$R/feu3.txt" 2>&1
            if attendre rep1 "fini" 180; then
                $OUTIL recuperer calcul/crible-iii-sortie-rep1 "$R/retour1" > /dev/null 2>&1
                F=0; [ -f "$R/retour1/rapatrie-reel/lecture-crible-iii-v1.json" ] && (cd "$R/retour1/rapatrie-reel" && sha256sum -c --quiet lecture-crible-iii-v1.json.sha256) || F=1
                [ -f "$R/retour1/remis-au-sous-agent/sortie-lire-non-ouverte.txt" ] || F=1
                [ -z "$(find "$R/retour1" -name prive -o -name 'MONDES*' -o -name 'secret.bin' -o -name 'phrase.txt')" ] || F=1
                grep -rqF -e factice-jeton-repetition-0001 -e factice-cle-repetition-0001 -e 'phrase publique de la répétition' "$R/retour1" && F=1
                [ "$F" = 0 ] && ok "cas 1 : état « fini », lecture rapatriée égale à son compagnon, rien de privé ni de secret sur la branche de sortie" \
                    || ko "cas 1 : sortie finale non conforme"
            else ko "cas 1 : état final « $(etape rep1) » au lieu de « fini »"; fi
        else ko "cas 1 : pas d'attente du feu 3 (« $(etape rep1) »)"; fi
    else ko "cas 1 : pas d'attente du feu 2 (« $(etape rep1) »)"; fi
else ko "cas 1 : pas d'attente du feu 1 (« $(etape rep1) » ; $(tail -n 3 "$R/m1.log" | tr '\n' ' '))"; fi
tuer "$P1" rep1
# --- cas 2 : feu d'arrêt pendant l'attente du feu 2 ---------------------------------------------------------------------------------
P2=$(lancer_machine "$R/m2" rep2 3600 300 4242)
if attendre rep2 "attente du feu 1 (phrase)" 240; then
    SS=$(git -C "$R/travail" show refs/remotes/origin/s-rep2:secret-sha256.txt | sed -n 's/^secret_sha256=//p'); C1=$(inscrire secret-rep2 "$SS" | tail -n 1)
    ( umask 077; printf 'phrase publique de la répétition, deuxième cas\n' > "$R/envoi/phrase.txt" )
    $OUTIL feu-phrase calcul/crible-iii-sortie-rep2 calcul/crible-iii-entree-rep2 "$R/envoi/phrase.txt" "$C1" registres/inscription-secret-rep2.md > /dev/null 2>&1
    if attendre rep2 "attente du feu 2 (mondes)" 120; then
        $OUTIL feu-arret calcul/crible-iii-entree-rep2 "arret demande par la mere (repetition)" > /dev/null 2>&1
        attendre rep2 "arret (A)" 60 && ok "cas 2 : feu d'arrêt lu à l'attente du feu 2 : arrêt (A)" || ko "cas 2 : état « $(etape rep2) »"
    else ko "cas 2 : pas d'attente du feu 2"; fi
else ko "cas 2 : pas d'attente du feu 1"; fi
$OUTIL feu-arret calcul/crible-iii-entree-rep2 "cause avec accent é" > /dev/null 2>&1 && ko "cas 2 : cause accentuée acceptée" || ok "cas 2 : cause accentuée refusée, rien n'est poussé"
tuer "$P2" rep2
# --- cas 3 : phrase absente, puis minuterie à l'échéance ----------------------------------------------------------------------------
P3=$(lancer_machine "$R/m3" rep3 75 15 4243)
attendre rep3 "arret (A)" 120 && ok "cas 3 : aucune phrase avant l'échéance de la barrière 1 : arrêt (A)" || ko "cas 3 : état « $(etape rep3) »"
n=0; while [ "$n" -lt 120 ] && ! grep -q 'DELETE /instances/4243/' "$R/loueur.log" 2>/dev/null; do sleep 2; n=$((n + 2)); done
grep -q 'DELETE /instances/4243/' "$R/loueur.log" && ok "cas 3 : minuterie à l'échéance : destruction demandée par l'identifiant (DELETE)" \
    || ko "cas 3 : aucune destruction demandée par la minuterie"
tuer "$P3" rep3
# --- cas 4 : refus de l'amorce avant la minuterie -----------------------------------------------------------------------------------
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME="$R" AMORCE_ESSAI=1 RACINE_AMORCE="$R/m4" API_VAST_ESSAI="http://127.0.0.1:$PORT" ATTENTE_REFUS_S=0 \
    CONTAINER_ID=4244 CONTAINER_API_KEY=factice COMMIT_LOT="$CM" bash "$ICI/amorce_crible_iii_v1.sh" > "$R/m4.log" 2>&1; c=$?
[ "$c" = 2 ] && [ "$(grep -c 'DELETE /instances/4244/' "$R/loueur.log")" = 3 ] && grep -q 'PUT /instances/4244/' "$R/loueur.log" && [ ! -e "$R/m4" ] \
    && ok "cas 4 : arguments refusés avant la minuterie : trois DELETE puis « stopped » demandés, aucun dossier" || ko "cas 4 : code $c"
# --- cas 5 : branche de sortie déjà présente ----------------------------------------------------------------------------------------
git -C "$R/travail" push -q origin "$CM:refs/heads/calcul/crible-iii-sortie-rep5"
P5=$(lancer_machine "$R/m5" rep5 3600 300 4245)
n=0; while [ "$n" -lt 120 ] && ! grep -q 'branche de sortie calcul/crible-iii-sortie-rep5 présente' "$R/m5.log"; do sleep 2; n=$((n + 2)); done
[ "$(git -C "$R/depot.git" rev-parse refs/heads/calcul/crible-iii-sortie-rep5)" = "$CM" ] && grep -q 'présente' "$R/m5.log" \
    && ok "cas 5 : branche de sortie déjà présente : arrêt, rien n'est poussé" || ko "cas 5"
tuer "$P5" rep5
# --- cas 6 : commande imprimée par l'outil de la session --------------------------------------------------------------------------
cat > "$R/envoi/recherche.json" <<'EOF'
[{"id": 111, "num_gpus": 1, "cpu_arch": "amd64", "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 40, "dph_total": 0.09, "storage_cost": 0.1, "inet_down": 500, "reliability2": 0.99, "inet_down_cost": 0.0, "inet_up_cost": 0.0},
 {"id": 112, "num_gpus": 0, "cpu_arch": "amd64", "cpu_cores_effective": 4, "cpu_ram": 8000, "disk_space": 20, "dph_total": 0.20, "storage_cost": 0.1, "inet_down": 500, "reliability2": 0.99},
 {"id": 113, "num_gpus": 0, "cpu_arch": "arm64", "cpu_cores_effective": 4, "cpu_ram": 8000, "disk_space": 20, "dph_total": 0.05, "storage_cost": 0.1, "inet_down": 500, "reliability2": 0.99}]
EOF
$OUTIL offre-depuis-recherche "$R/envoi/recherche.json" "$R/envoi/offre.json" > "$R/offre.txt" 2>&1
grep -q 'OFFRE ECRITE .* offre 111' "$R/offre.txt" && ok "cas 6 : offre choisie par la garde (113 refusée : arm64 ; 112 : prix)" || ko "cas 6 : offre ($(tail -n 1 "$R/offre.txt"))"
CONTROLE_IA_GITHUB_TOKEN_2=factice-jeton-repetition-0001 RR_ANTHROPIC_API_KEY_RIGAUD=factice-cle-repetition-0001 $OUTIL commande "$R/envoi/offre.json" \
    "$CM" "$CM" calcul/crible-iii-sortie-rep6 calcul/crible-iii-entree-rep6 "crible-iii-v1-$(date -u +%Y%m%d)" GO-2026-11-17-91 GO-2026-11-17-92 \
    prereg/crible-iii-repetition-v1.md prereg/crible-iii-repetition-v1-addendum.md > "$R/commande.txt" 2>&1; c=$?
L2=$(sed -n 2p "$R/envoi/commande-creation.txt" 2>/dev/null)
if [ "$c" = 0 ] && printf '%s' "$L2" | grep -q '^GO_ID=GO-2026-11-17-92 /inexistant create instance 111 ' && ! grep -qF -e factice-jeton-repetition -e factice-cle-repetition "$R/envoi/commande-creation.txt" "$R/commande.txt" \
    && [ "$(stat -c %a "$R/envoi/amorce.b64")" = 600 ] && [ "$(base64 -d < "$R/envoi/amorce.b64" | gunzip | sha256sum | cut -d' ' -f1)" = "$(sha256sum < "$ICI/amorce_crible_iii_v1.sh" | cut -d' ' -f1)" ]; then
    ok "cas 6 : commande imprimée (GO_ID en tête, noms des clés seuls, amorce compressée égale à l'octet, 0600)"
else ko "cas 6 : commande (code $c ; $(tail -n 2 "$R/commande.txt" | tr '\n' ' '))"; fi
cp "$R/envoi/commande-creation.txt" "$R/a-jouer.txt"; $OUTIL comparer "$R/a-jouer.txt" > /dev/null 2>&1 && c1=0 || c1=1
printf 'x' >> "$R/a-jouer.txt"; $OUTIL comparer "$R/a-jouer.txt" > /dev/null 2>&1 && c2=0 || c2=1
[ "$c1" = 0 ] && [ "$c2" = 1 ] && ok "cas 6 : comparer : copie exacte acceptée, copie altérée refusée" || ko "cas 6 : comparer ($c1, $c2)"
CONTROLE_IA_GITHUB_TOKEN_2=factice-jeton-repetition-0001 RR_ANTHROPIC_API_KEY_RIGAUD=factice-cle-repetition-0001 $OUTIL commande "$R/envoi/offre.json" \
    "$CM" "$CM" calcul/crible-iii-sortie-rep6 calcul/crible-iii-entree-rep6 "crible-iii-v1-$(date -u +%Y%m%d)" GO-2026-11-17-91 GO-2026-11-17-93 \
    prereg/crible-iii-repetition-v1.md prereg/crible-iii-repetition-v1-addendum.md > "$R/commande2.txt" 2>&1 && ko "cas 6 : ligne de GO absente acceptée" \
    || ok "cas 6 : ligne de GO absente du registre : commande refusée ($(tail -n 1 "$R/commande2.txt" | cut -c1-90))"
kill "$PIDL" 2>/dev/null; wait "$PIDL" 2>/dev/null
echo "RÉPÉTITION : $K cas, $((K - KO)) conformes, $KO écarts ; dossier jetable $R"
[ "$KO" = 0 ]
