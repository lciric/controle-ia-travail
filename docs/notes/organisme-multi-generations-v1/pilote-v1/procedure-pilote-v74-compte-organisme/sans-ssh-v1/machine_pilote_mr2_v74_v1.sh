#!/usr/bin/env bash
# Programme machine du pilote MR-2 sans ssh — v1 (procédure v11). Pris au commit COMMIT_LOT par l'amorce, à l'empreinte
# SCRIPT_SHA256, puis `exec` (même PID ; la minuterie de destruction, PID_MINUTERIE, reste son enfant).
# Il joue sur la machine les sections 3 à 11 de la procédure v10, dans le même ordre et avec les mêmes attendus, chaque geste ssh
# étant remplacé par : (i) une passe de ce programme, (ii) un état et des traces poussés sur la branche neuve BR_SORTIE (la session
# lit la branche, jamais la machine), (iii) aux trois barrières, un feu écrit par la mère sur la branche BR_ENTREE (feu 1 : phrase
# chiffrée, après l'inscription de l'empreinte du secret ; feu 2 : après l'inscription des empreintes des mondes ; feu 3 : avant le
# pilote réel). Un feu d'arrêt (`feu-arret.txt`) est lu à chaque attente et pendant `jouer` réel (arrêt du pilote par son PID, R10).
# Rien de privé ne sort : secret, phrase, clé privée de la phrase, mondes, textes servis restent dans $T/prive ou $T/REEL/prive et
# meurent avec la machine ; seuls les fichiers d'une liste blanche sont copiés dans $T/sortie, balayés (jeton, trois clés, secret,
# phrase), puis poussés.
# Clés : lues de l'environnement d'entrée dans des variables du programme, retirées aussitôt de l'environnement des enfants
# (`export -n`) ; seul `jouer` réel les reçoit, par `env -i` ; après `jouer`, plus aucun processus ne les reçoit, sauf le balayage
# (qui les cherche dans les fichiers à pousser) ; effacées du programme (`unset`) après la dernière poussée. Exposition restante,
# dite : environnement du processus d'entrée (PID 1 du conteneur et l'environnement initial de ce processus) et configuration de
# l'instance chez le loueur, jusqu'à la destruction ; aucune clé n'est jamais écrite sur le disque.
# Fins : aucune fin ne détruit la machine (la session détruit par l'identifiant, ou la minuterie à l'échéance) ; l'état final dit
# « fini », « arret (A) : … » ou « noeud, machine gardee : … », puis attente sans calcul.
# Essai (ESSAI=1 seulement) : PATH_O_ESSAI, ESSAI_LANCEUR, ESSAI_REEL_A_BLANC, ESSAI_SANS_PIP, ESSAI_SANS_TLS, ATTENTE_PHRASE_S,
# ATTENTE_FEU_S, PAS_ENTREE_S, PAS_ETAT_S, BUDGET_REEL_S ; hors essai, chacune est refusée.
set -uo pipefail
for v in PATH_O_ESSAI ESSAI_LANCEUR ESSAI_REEL_A_BLANC ESSAI_SANS_PIP ESSAI_SANS_TLS ATTENTE_PHRASE_S ATTENTE_FEU_S PAS_ENTREE_S PAS_ETAT_S BUDGET_REEL_S; do
    [ "$ESSAI" = 1 ] || [ -z "${!v:-}" ] || { echo "PILOTE MACHINE REFUS : $v en essai seulement"; sleep infinity; }
done
# --- secrets : dans le programme seulement ------------------------------------------------------------------------------------
JETON="$GH_TOKEN"; KA="$RR_ANTHROPIC_API_KEY_RIGAUD"; KG="$GEMINI_API_KEY"; KO="$OPENAI_API_KEY"
export -n GH_TOKEN RR_ANTHROPIC_API_KEY_RIGAUD GEMINI_API_KEY OPENAI_API_KEY CONTAINER_API_KEY
CLES=presentes
# --- constantes ---------------------------------------------------------------------------------------------------------------
PL=docs/notes/organisme-multi-generations-v1/pilote-v1
BUNDLE_CHEMIN=$PL/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle
SONDE_CHEMIN=$PL/sonde-complete-v74-compte-organisme/sonde-complete-v74
TEXTE_CHEMIN=$PL/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md
SHA_BUNDLE=e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1
SHA_TEXTE=8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e
SHA_RELEVE=f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529
TETE_ARBRE=605e0f60f3eed0948948e6a4eb15cb73de1d03de
NUMPY=2.5.3
ATTENTE_PHRASE=${ATTENTE_PHRASE_S:-3600}   # v10, section 2, point 8 : la phrase dans l'heure qui suit la location
ATTENTE_FEU=${ATTENTE_FEU_S:-1200}         # feux 2 et 3, relance : 20 minutes chacun
PAS_ENTREE=${PAS_ENTREE_S:-60}
PAS_ETAT=${PAS_ETAT_S:-900}                # état poussé pendant `jouer` réel : toutes les 15 minutes
BUDGET_REEL=${BUDGET_REEL_S:-45000}        # pire cas de `jouer` (4 × 10 800 s) + mesure, rapatriement, poussée : 12 h 30
SEUIL=95000000
POUSSEE_ID=0
PX="${PATH_O_ESSAI:-/usr/local/bin:/usr/bin:/bin}"
X="$T/sortie"; S="$T/depot-sortie"; PV="$T/prive"; E="$T/entree"; L="$X/journal-machine.txt"
mkdir -p "$X" "$E" && mkdir -p -m 700 "$PV" && chmod 700 "$PV" || { echo "PILOTE MACHINE : dossiers impossibles"; sleep infinity; }
AIDE="$T/machine_pilote_mr2_v74_v1.py"
DEBUT_S=$(stat -c %Y "$T/amorce-lancee" 2>/dev/null || date +%s)
ETAPE="debut"; MOTIF=""; REEL=""; H=""; SM=""; CODE_JOUER=""; CODE_MESURER=""; PID_JOUER=""; EXCLUS=""
j() { printf '%s PILOTE MACHINE %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
g() { GH_TOKEN="$JETON" git "$@"; }
aide() { env -i PATH="$PX" HOME=/root python3 -I -B "$AIDE" "$@"; }
O() { (cd "$T/arbre/orchestrator" && exec env -i PATH="$PX" HOME=/root python3 -I -B "${ESSAI_LANCEUR:-demonstrations/pilote_mr2_v74.py}" "$@"); }
# --- état et poussée ----------------------------------------------------------------------------------------------------------
ecrire_etat() {
    { printf 'etape=%s\nmotif=%s\nheure=%s\ndebut=%s\necheance=%s\nminuterie_pid=%s\ncles=%s\nreel=%s\n' "$ETAPE" "$MOTIF" \
        "$(date -u +%FT%TZ)" "$(date -u -d "@$DEBUT_S" +%FT%TZ)" "$(date -u -d "@$ECHEANCE_UTC_S" +%FT%TZ)" "$PID_MINUTERIE" "$CLES" "$REEL"
      printf 'fichier_mondes_sha256=%s\ncode_jouer=%s\ncode_mesurer=%s\npoussee=%s\nrelance_du_conteneur=%s\nexclus_balayage=%s\n' "$H" \
        "$CODE_JOUER" "$CODE_MESURER" "$POUSSEE_ID" "$ENTREE_RELANCE" "$EXCLUS"; } > "$X/etat.txt"; }
copier_traces() {  # liste blanche : rien d'autre ne sort de la machine
    local f
    for f in "$T"/journal-*.txt "$T"/code-*.txt "$T/lancements.jsonl" "$T/mise-en-place.txt"; do [ -f "$f" ] && cp -f "$f" "$X/"; done
    [ -f "$PV/MONDES.json.engagement.json" ] && cp -f "$PV/MONDES.json.engagement.json" "$X/engagement-mondes.json"
    for f in rapatrie-blanc rapatrie-reel; do [ -d "$T/$f" ] && { rm -rf "${X:?}/$f"; cp -a "$T/$f" "$X/$f"; }; done
    [ -f "$T/sortie-lire-non-ouverte.txt" ] && { mkdir -p "$X/remis-au-sous-agent"; cp -f "$T/sortie-lire-non-ouverte.txt" "$X/remis-au-sous-agent/"; }
    return 0; }
balayer() {  # fichiers nommés : 0 si aucune forme secrète ; motifs (noms de fichiers et de formes, jamais une valeur) dans balayage.txt
    # shellcheck disable=SC2068
    env -i PATH="$PX" HOME=/root S_JETON="$JETON" S_CLE_A="${KA:-}" S_CLE_G="${KG:-}" S_CLE_O="${KO:-}" python3 -I -B "$AIDE" balayer \
        --secret "$PV/secret.bin" --phrase "$PV/phrase.txt" $@ > "$T/balayage.txt" 2>&1; }
exclure_balayes() {  # retire du dépôt de sortie les fichiers déjà exclus par le balayage (liste $T/exclus-balayage.txt)
    local f
    [ -s "$T/exclus-balayage.txt" ] || return 0
    while IFS= read -r f; do [ -n "$f" ] && rm -f -- "$S/$f"; done < "$T/exclus-balayage.txt"
    EXCLUS="$(sort -u "$T/exclus-balayage.txt" | tr '\n' ' ')"; return 0; }
pousser() {  # $1 = motif du commit ; balayage, puis poussée vérifiée par ls-remote ; 0 seulement si la tête distante = la locale
    local n loc dist liste
    POUSSEE_ID=$((POUSSEE_ID + 1)); copier_traces; ecrire_etat
    if [ ! -d "$S/.git" ]; then
        git init -q "$S" && git -C "$S" remote add origin "$DEPOT_URL" \
            && git -C "$S" config credential.helper '!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f' \
            && git -C "$S" config user.name "machine du pilote MR-2" && git -C "$S" config user.email "machine-pilote@invalid" \
            || { j "dépôt de sortie impossible"; return 1; }
    fi
    find "$S" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} + && cp -a "$X/." "$S/" || { j "copie vers le dépôt de sortie impossible"; return 1; }
    exclure_balayes
    liste=$(find "$S" -path "$S/.git" -prune -o -type f -print)
    while IFS= read -r n; do [ -z "$n" ] || [ "$(stat -c %s "$n")" -le "$SEUIL" ] || { j "fichier de plus de 95 Mo : ${n#$S/} : poussée refusée"; return 1; }; done <<< "$liste"
    # balayage ; un fichier où une forme secrète est trouvée est exclu (jamais poussé, consigné par son nom), le reste rebalayé
    if ! balayer $liste; then
        sed -n "s|^BALAYAGE : forme de .* trouvée dans $S/||p" "$T/balayage.txt" >> "$T/exclus-balayage.txt"
        [ -s "$T/exclus-balayage.txt" ] || { j "BALAYAGE : refus sans fichier nommé : poussée refusée : $(head -c 300 "$T/balayage.txt")"; return 1; }
        j "BALAYAGE : forme secrète trouvée : fichier(s) exclu(s) de toute poussée : $(sort -u "$T/exclus-balayage.txt" | tr '\n' ' ' | cut -c1-300)"
        exclure_balayes; ecrire_etat; cp -f "$X/etat.txt" "$S/etat.txt"; cp -f "$L" "$S/journal-machine.txt"
        liste=$(find "$S" -path "$S/.git" -prune -o -type f -print)
        balayer $liste || { j "BALAYAGE : refus après exclusion : poussée refusée : $(head -c 300 "$T/balayage.txt")"; return 1; }
    fi
    git -C "$S" add -A && { git -C "$S" diff --cached --quiet || git -C "$S" commit -q -m "pilote MR-2 v74 : $1 (poussée $POUSSEE_ID)"; } \
        || { j "commit de sortie impossible"; return 1; }
    loc=$(git -C "$S" rev-parse HEAD) || return 1
    for n in 1 2 3; do
        if g -C "$S" push -q origin "HEAD:refs/heads/$BR_SORTIE" 2> "$T/poussee.err"; then
            dist=$(g -C "$S" ls-remote origin "refs/heads/$BR_SORTIE" 2>/dev/null | cut -f1)
            [ "$dist" = "$loc" ] && { j "poussé ($1) : $loc"; return 0; }
        fi
        j "poussée refusée, essai $n/3 : $(tail -n 2 "$T/poussee.err" | tr '\n' ' ' | cut -c1-200)"; sleep $((10 * n)); done
    return 1; }
attente_finale() {  # aucune passe ; clés effacées du programme ; la session détruit par l'identifiant, ou la minuterie à l'échéance
    trap - EXIT
    unset KA KG KO
    j "FIN ($ETAPE) : attente sans calcul ; destruction par la session (identifiant, -y, absence prouvée) ou par la minuterie"
    while :; do sleep 3600; done; }
rapatrier_reel() {  # étape (3) de (A) et section 11 : rapatriement du dossier réel s'il existe (même après un code 3)
    [ -n "$REEL" ] && [ -d "$T/$REEL" ] && [ -n "$H" ] && [ ! -e "$T/rapatrie-reel" ] || return 0
    O rapatrier --source "$T/$REEL" --destination "$T/rapatrie-reel" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" \
        > "$T/journal-11-rapatrier.txt" 2>&1; echo $? > "$T/code-11-rapatrier.txt"
    aide rapatrier "$T/journal-11-rapatrier.txt" >> "$L" 2>&1 || { j "rapatriement du réel non conforme : rapatrie-reel retiré, rien n'en sort"; rm -rf "$T/rapatrie-reel"; }
    return 0; }
arret_A() {  # arrêt commun (A) de la v10, sur la machine : cause, clés effacées, rapatriement, traces poussées, attente
    ETAPE="arret (A)"; MOTIF="$1"; j "ARRET (A) : $1"
    rapatrier_reel
    pousser "arrêt (A)" || j "traces non poussées : motif ci-dessus, lisible par vastai logs"
    attente_finale; }
noeud_garde() {  # nœud à la mère, machine gardée : aucune passe de plus ; rien d'autre que la destruction ne reste possible
    ETAPE="noeud, machine gardee"; MOTIF="$1"; j "NOEUD, MACHINE GARDÉE : $1"
    rapatrier_reel
    pousser "nœud, machine gardée" || j "traces non poussées : motif ci-dessus, lisible par vastai logs"
    attente_finale; }
inattendue() { local c=$?; trap - EXIT; ETAPE="sortie inattendue"; MOTIF="code $c"; pousser "sortie inattendue" || true; attente_finale; }
trap inattendue EXIT
# --- entrée -------------------------------------------------------------------------------------------------------------------
lire_entree() {  # $1 = nom du fichier sur BR_ENTREE : copié dans $E ; 1 si absent
    rm -f "$E/$1"
    g -C "$D" fetch -q --filter=blob:none --depth=1 origin "+refs/heads/$BR_ENTREE:refs/remotes/origin/entree" > /dev/null 2>&1 || return 1
    g -C "$D" show "refs/remotes/origin/entree:$1" > "$E/$1" 2>/dev/null || { rm -f "$E/$1"; return 1; }; }
arret_demande() {  # feu d'arrêt de la mère, lu à chaque attente
    lire_entree feu-arret.txt || return 1
    aide feu "$E/feu-arret.txt" arret > "$E/feu-arret.lu" 2>&1 || { j "feu d'arrêt illisible : $(head -c 200 "$E/feu-arret.lu")"; return 1; }
    return 0; }
attendre_feu() {  # $1 = fichier, $2 = genre, $3 = échéance (s), puis attendus clé=valeur ; 0 au feu conforme ; arrêt (A) sinon
    local f="$1" genre="$2" fin="$3" vu=""; shift 3
    while [ "$(date +%s)" -lt "$fin" ]; do
        arret_demande && arret_A "feu d'arrêt de la mère ($(grep -a '^cause=' "$E/feu-arret.txt" | head -c 200))"
        if lire_entree "$f"; then
            if aide feu "$E/$f" "$genre" "$@" > "$E/$f.lu" 2>&1; then j "feu $genre conforme"; return 0; fi
            [ "$(sha256sum < "$E/$f")" = "$vu" ] || { vu=$(sha256sum < "$E/$f"); j "feu $genre refusé (attente continuée) : $(head -c 200 "$E/$f.lu")"; }
        fi
        sleep "$PAS_ENTREE"; done
    arret_A "aucun feu $genre conforme avant $(date -u -d "@$fin" +%FT%TZ)"; }
inscription_sur_main() {  # $1 = fichier .lu du feu ; puis empreintes : commit ancêtre de main, fichier qui les porte toutes
    local c ch
    c=$(sed -n 's/^inscription_commit=//p' "$1"); ch=$(sed -n 's/^inscription_chemin=//p' "$1"); shift
    g -C "$D" fetch -q --filter=blob:none --depth=200 origin "+refs/heads/main:refs/remotes/origin/main" > /dev/null 2>&1 \
        || arret_A "main injoignable : inscription non prouvée"
    git -C "$D" merge-base --is-ancestor "$c" refs/remotes/origin/main 2>/dev/null || arret_A "commit d'inscription absent de main (200 derniers commits)"
    g -C "$D" show "$c:$ch" > "$E/inscription.txt" 2>/dev/null || arret_A "fichier d'inscription illisible au commit"
    aide inscription "$E/inscription.txt" "$@" >> "$L" 2>&1 || arret_A "empreintes non inscrites sur main"
    j "inscription prouvée sur main ($c, $ch)"; }
# --- relance du conteneur par le loueur : rien n'est refait --------------------------------------------------------------------
if [ "$ENTREE_RELANCE" = 1 ]; then
    REEL=$(cat "$T/reel-nom.txt" 2>/dev/null || true); H=$(cat "$T/h.txt" 2>/dev/null || true)
    arret_A "relance du conteneur par le loueur : aucune passe refaite (tout processus du pilote a été interrompu)"
fi
# --- 3. mise en place (v10, section 3) ----------------------------------------------------------------------------------------
ETAPE="mise en place"; j "début ; échéance de la minuterie $(date -u -d "@$ECHEANCE_UTC_S" +%FT%TZ)"
g -C "$D" ls-remote --exit-code origin "refs/heads/$BR_SORTIE" > /dev/null 2>&1; c=$?
[ "$c" = 2 ] || { j "ARRET : branche de sortie $BR_SORTIE présente (R12) ou dépôt injoignable (code $c) : rien n'est poussé"; trap - EXIT; attente_finale; }
g -C "$D" ls-remote --exit-code origin "refs/heads/$BR_ENTREE" > /dev/null 2>&1; c=$?
[ "$c" = 2 ] || arret_A "branche d'entrée $BR_ENTREE déjà présente avant la machine (code $c) : un feu ancien serait lu"
pousser "mise en place commencée" || { j "ARRET : première poussée impossible"; trap - EXIT; attente_finale; }
{ echo "nproc $(nproc)"; awk '/MemTotal/ {print "memoire_ko", $2}' /proc/meminfo; df -P -B1 "$R" | awk 'NR == 2 {print "disque_libre_octets", $4}'; } > "$T/mise-en-place.txt"
if [ "${ESSAI_SANS_PIP:-0}" != 1 ]; then
    timeout 900 env -i PATH="$PX" HOME=/root python3 -m pip install --no-cache-dir "numpy==$NUMPY" > "$T/journal-03-pip.txt" 2>&1 \
        || arret_A "installation de numpy $NUMPY en échec ou au-delà de 900 s"
fi
v=$(env -i PATH="$PX" HOME=/root python3 -I -c "import sys,numpy;print(sys.version_info[:2],numpy.__version__)" 2>&1)
echo "python_numpy $v ; $(git --version)" >> "$T/mise-en-place.txt"
[ "$v" = "(3, 13) $NUMPY" ] || arret_A "python ou numpy inattendu : $v"
# --- 4. pièces, arbre et bloc gelé (v10, sections 1 et 4) ---------------------------------------------------------------------
ETAPE="pieces et arbre"
git -C "$D" config core.sparseCheckout true && git -C "$D" config core.sparseCheckoutCone false \
    && printf '/%s\n/%s/\n' "$BUNDLE_CHEMIN" "$SONDE_CHEMIN" > "$D/.git/info/sparse-checkout" \
    && g -C "$D" -c advice.detachedHead=false checkout -q --detach "$COMMIT_LOT" || arret_A "extraction partielle du commit $COMMIT_LOT"
for p in runs diag donnees essai registres; do [ ! -e "$D/$p" ] || arret_A "$p/ présent dans l'arbre extrait"; done
cp -f "$D/$BUNDLE_CHEMIN" "$T/arbre-organisme-complet-605e0f6.bundle" && cp -a "$D/$SONDE_CHEMIN" "$T/sonde" \
    && g -C "$D" show "$COMMIT_PREP:$TEXTE_CHEMIN" > "$T/texte.md" && g -C "$D" show "$COMMIT_MAIN:registres/go.md" > "$T/go-main.md" \
    || arret_A "pièces illisibles aux commits"
( cd "$T" && sha256sum arbre-organisme-complet-605e0f6.bundle texte.md go-main.md sonde/releve-sonde-pilote-v74.json ) > "$T/journal-04-pieces.txt"
[ "$(sha256sum < "$T/arbre-organisme-complet-605e0f6.bundle" | cut -d' ' -f1)" = "$SHA_BUNDLE" ] || arret_A "paquet : empreinte différente"
[ "$(sha256sum < "$T/texte.md" | cut -d' ' -f1)" = "$SHA_TEXTE" ] || arret_A "texte scellé : empreinte différente"
[ "$(sha256sum < "$T/sonde/releve-sonde-pilote-v74.json" | cut -d' ' -f1)" = "$SHA_RELEVE" ] || arret_A "relevé de la sonde : empreinte différente"
[ "$(cut -d' ' -f1 "$T/sonde/releve-sonde-pilote-v74.json.sha256" 2>/dev/null)" = "$SHA_RELEVE" ] || arret_A "compagnon du relevé absent ou différent"
for p in argon astra fable52 opus55; do [ -d "$T/sonde/$p" ] || arret_A "dossier de relais $p absent de la sonde"; done
git init -q "$T/arbre" && git -C "$T/arbre" bundle unbundle "$T/arbre-organisme-complet-605e0f6.bundle" > /dev/null \
    && git -C "$T/arbre" -c advice.detachedHead=false checkout -q "$TETE_ARBRE" || arret_A "dépaquetage de l'arbre"
[ "$(git -C "$T/arbre" rev-parse HEAD)" = "$TETE_ARBRE" ] || arret_A "tête de l'arbre ≠ 605e0f6"
[ -z "$(git -C "$T/arbre" status --porcelain --ignored)" ] || arret_A "arbre non propre"
O bloc --releve-sonde "$T/sonde/releve-sonde-pilote-v74.json" > "$T/journal-04-bloc.txt" 2> "$T/journal-04-bloc-erreur.txt"; c=$?
[ "$c" = 0 ] || arret_A "bloc : code $c"
aide bloc "$T/texte.md" "$T/journal-04-bloc.txt" >> "$L" 2>&1 || arret_A "bloc gelé différent du texte scellé"
j "pièces aux empreintes attendues ; arbre 605e0f6 propre ; bloc égal"
# --- 5. secret, puis phrase de Lazar (barrière 1) -----------------------------------------------------------------------------
ETAPE="secret"
[ ! -e "$PV/secret.bin" ] || arret_A "secret déjà présent (le lanceur refuse d'écraser)"
O secret "$PV/secret.bin" > "$T/journal-05-secret.txt" 2>&1; c=$?
[ "$c" = 0 ] || arret_A "secret : code $c"
SECRET_SHA=$(aide secret "$T/journal-05-secret.txt") || arret_A "secret : sortie inattendue"
( umask 077; openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out "$PV/cle-phrase.pem" 2> /dev/null ) \
    && openssl pkey -in "$PV/cle-phrase.pem" -pubout -out "$X/cle-publique-phrase.pem" 2> /dev/null || arret_A "clé de la phrase impossible"
echo "secret_sha256=$SECRET_SHA" > "$X/secret-sha256.txt"
openssl pkey -pubin -in "$X/cle-publique-phrase.pem" -outform DER 2>/dev/null | sha256sum | cut -d' ' -f1 > "$X/cle-publique-phrase.empreinte"
ETAPE="attente du feu 1 (phrase)"; MOTIF="empreinte du secret à inscrire sur main ; puis phrase chiffrée par cle-publique-phrase.pem"
pousser "secret engagé, attente de la phrase" || arret_A "empreinte du secret non poussée"
attendre_feu feu-1-phrase.txt phrase $((DEBUT_S + ATTENTE_PHRASE)) "secret_sha256=$SECRET_SHA"
inscription_sur_main "$E/feu-1-phrase.txt.lu" "$SECRET_SHA"
lire_entree phrase-chiffree.b64 || arret_A "phrase chiffrée absente de la branche d'entrée"
base64 -d < "$E/phrase-chiffree.b64" > "$E/phrase.chiffree" 2>/dev/null || arret_A "phrase chiffrée : base64 illisible"
( umask 077; openssl pkeyutl -decrypt -inkey "$PV/cle-phrase.pem" -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 \
    -pkeyopt rsa_mgf1_md:sha256 -in "$E/phrase.chiffree" -out "$PV/phrase.txt" 2> /dev/null ) || arret_A "phrase : déchiffrement impossible"
shred -u "$PV/cle-phrase.pem"
aide phrase "$PV/phrase.txt" >> "$L" 2>&1 || arret_A "phrase de forme non conforme"
PS=$(sha256sum < "$PV/phrase.txt" | cut -d' ' -f1)
[ "$PS" = "$(sed -n 's/^phrase_fichier_sha256=//p' "$E/feu-1-phrase.txt.lu")" ] || arret_A "phrase : empreinte du fichier ≠ celle du feu"
echo "phrase_fichier_sha256=$PS" > "$X/phrase-sha256.txt"
j "phrase reçue, empreinte égale à celle du feu ; clé privée de la phrase effacée"
# --- 6. mondes, puis barrière 2 -------------------------------------------------------------------------------------------------
ETAPE="mondes"; pousser "phrase reçue, génération des mondes" || true
O generer --secret "$PV/secret.bin" --phrase-fichier "$PV/phrase.txt" --texte "$T/texte.md" --texte-sha256 "$SHA_TEXTE" \
    --sortie "$PV/MONDES.json" > "$T/journal-06-generer.txt" 2>&1; c=$?; echo "$c" > "$T/code-06-generer.txt"
[ "$c" = 0 ] || arret_A "generer : code $c (une graine neuve demande un texte neuf et le mot de Lazar)"
H=$(aide generer "$T/journal-06-generer.txt") || arret_A "generer : un monde non conforme"
echo "$H" > "$T/h.txt"
SM=$(aide engagement "$PV/MONDES.json.engagement.json" "$H") || arret_A "engagement des mondes illisible"
ETAPE="attente du feu 2 (mondes)"; MOTIF="empreintes H et S1 à S4 (engagement-mondes.json) à inscrire sur main"
pousser "mondes générés, attente de l'inscription" || arret_A "engagement des mondes non poussé"
attendre_feu feu-2-mondes.txt mondes $(( $(date +%s) + ATTENTE_FEU )) "fichier_mondes_sha256=$H"
# shellcheck disable=SC2086
inscription_sur_main "$E/feu-2-mondes.txt.lu" "$H" $SM
# --- 7. C-16 et C-17 ; 8. essai à blanc et rapatriement essayé ; barrière 3 -----------------------------------------------------
ETAPE="preparer"; MOTIF=""
O preparer --mondes "$PV/MONDES.json" --mondes-sha256 "$H" > "$T/journal-07-preparer.txt" 2>&1; c=$?; echo "$c" > "$T/code-07-preparer.txt"
[ "$c" = 0 ] || arret_A "preparer : code $c"
aide preparer "$T/journal-07-preparer.txt" >> "$L" 2>&1 || arret_A "preparer : sortie non conforme"
ETAPE="essai a blanc"
O jouer --mode a_blanc --mondes "$PV/MONDES.json" --mondes-sha256 "$H" --sortie "$T/blanc" > "$T/journal-08-blanc.txt" 2>&1; c=$?
echo "$c" > "$T/code-08-blanc.txt"
[ "$c" = 0 ] || arret_A "essai à blanc : code $c (aucun blanc-2)"
aide jouer "$T/journal-08-blanc.txt" a_blanc >> "$L" 2>&1 || arret_A "essai à blanc : sortie différente de l'attendu"
O rapatrier --source "$T/blanc" --destination "$T/rapatrie-blanc" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" \
    > "$T/journal-08-rapatrier-blanc.txt" 2>&1; c=$?
[ "$c" = 0 ] || arret_A "rapatriement à blanc : code $c"
aide rapatrier "$T/journal-08-rapatrier-blanc.txt" >> "$L" 2>&1 || { rm -rf "$T/rapatrie-blanc"; arret_A "rapatriement à blanc : un monde porté"; }
ETAPE="attente du feu 3 (pilote reel)"; MOTIF="essai à blanc conforme (16/0/0, aucun monde au rapatriement)"
pousser "essai à blanc conforme, attente du feu réel" || arret_A "essai à blanc non poussé"
attendre_feu feu-3-reel.txt reel $(( $(date +%s) + ATTENTE_FEU )) "fichier_mondes_sha256=$H"
# --- 9. pilote réel (une seule fois ; une relance seulement sur code 2 sans lancement consigné, au feu de la mère) ---------------
controles_avant() {  # $1 = dossier de sortie (reel ou reel-2)
    [ ! -e "$T/$1" ] && [ ! -e "$T/lancements.jsonl" ] || arret_A "dossier $1 ou registre des lancements déjà présent"
    [ "$(env -i PATH="$PX" HOME=/root python3 -I -c 'import numpy;print(numpy.__version__)' 2>&1)" = "$NUMPY" ] || arret_A "numpy ≠ $NUMPY"
    [ "$(sha256sum < "$T/texte.md" | cut -d' ' -f1)" = "$SHA_TEXTE" ] && [ "$(sha256sum < "$T/sonde/releve-sonde-pilote-v74.json" | cut -d' ' -f1)" = "$SHA_RELEVE" ] \
        || arret_A "texte ou relevé : empreinte différente juste avant"
    aide ports >> "$L" 2>&1 || arret_A "un port des relais est occupé"
    [ "${ESSAI_SANS_TLS:-0}" = 1 ] || aide tls >> "$L" 2>&1 || arret_A "un fournisseur est injoignable"
    [ $(( ECHEANCE_UTC_S - $(date +%s) )) -ge "$BUDGET_REEL" ] || arret_A "moins de $BUDGET_REEL s avant l'échéance de la minuterie : le pilote ne partirait pas jusqu'au bout"
    [ -n "${KA:-}" ] && [ -n "${KG:-}" ] && [ -n "${KO:-}" ] || arret_A "clé absente juste avant"; }
lancer_reel() {  # $1 = reel ou reel-2 ; l'état « reel » est écrit au lancement, une fois
    local mode=reel; [ "${ESSAI_REEL_A_BLANC:-0}" = 1 ] && mode=a_blanc
    REEL="$1"; echo "$REEL" > "$T/reel-nom.txt"; ETAPE="jouer $REEL en cours"; MOTIF=""
    if [ "$mode" = reel ]; then
        ( cd "$T/arbre/orchestrator" && exec env -i PATH="$PX" HOME=/root RR_ANTHROPIC_API_KEY_RIGAUD="$KA" GEMINI_API_KEY="$KG" OPENAI_API_KEY="$KO" \
            python3 -I -B "${ESSAI_LANCEUR:-demonstrations/pilote_mr2_v74.py}" jouer --mode reel --mondes "$PV/MONDES.json" --mondes-sha256 "$H" \
            --sortie "$T/$REEL" --go-pi1 GO-2026-11-14-13 --go-pi2 GO-2026-11-14-14 --registre-go "$T/go-main.md" --texte "$T/texte.md" \
            --texte-sha256 "$SHA_TEXTE" --mondes-shas "$(echo $SM | tr ' ' ',')" --registre-lancements "$T/lancements.jsonl" \
            --releve-sonde "$T/sonde/releve-sonde-pilote-v74.json" ) > "$T/journal-09-$REEL.txt" 2>&1 < /dev/null &
    else  # essai seulement : le mode réel refuse toute configuration autre que la gelée ; le chemin de la machine est le même
        ( cd "$T/arbre/orchestrator" && exec env -i PATH="$PX" HOME=/root RR_ANTHROPIC_API_KEY_RIGAUD="$KA" GEMINI_API_KEY="$KG" OPENAI_API_KEY="$KO" \
            python3 -I -B "${ESSAI_LANCEUR:-demonstrations/pilote_mr2_v74.py}" jouer --mode a_blanc --mondes "$PV/MONDES.json" --mondes-sha256 "$H" \
            --sortie "$T/$REEL" ) > "$T/journal-09-$REEL.txt" 2>&1 < /dev/null &
    fi
    PID_JOUER=$!
    j "jouer $REEL lancé (PID $PID_JOUER)"
    pousser "jouer $REEL lancé" || true
    local dernier
    dernier=$(date +%s)
    while kill -0 "$PID_JOUER" 2> /dev/null; do
        sleep "$PAS_ENTREE"
        kill -0 "$PID_JOUER" 2> /dev/null || break
        if arret_demande; then
            j "feu d'arrêt de la mère pendant jouer : arrêt du pilote par son PID $PID_JOUER (R10)"
            kill -TERM "$PID_JOUER" 2>/dev/null; wait "$PID_JOUER" 2>/dev/null; echo "arrete-par-feu" > "$T/code-09-$REEL.txt"
            arret_A "feu d'arrêt de la mère pendant jouer $REEL ($(grep -a '^cause=' "$E/feu-arret.txt" | head -c 200))"
        fi
        if [ $(( $(date +%s) - dernier )) -ge "$PAS_ETAT" ]; then MOTIF="jouer en cours depuis $(( $(date +%s) - $(stat -c %Y "$T/reel-nom.txt") )) s"; pousser "jouer en cours" || true; dernier=$(date +%s); fi
    done
    wait "$PID_JOUER"; CODE_JOUER=$?; echo "$CODE_JOUER" > "$T/code-09-$REEL.txt"
    j "jouer $REEL : code $CODE_JOUER"; }
controles_avant reel
lancer_reel reel
if [ "$CODE_JOUER" = 2 ] && [ ! -e "$T/lancements.jsonl" ]; then
    ETAPE="attente du feu de relance (reel-2)"; MOTIF="code 2 sans lancement consigné : une seule relance, sous reel-2, au feu de la mère"
    pousser "code 2 sans lancement, attente du feu de relance" || true
    attendre_feu feu-relance-reel-2.txt relance-reel-2 $(( $(date +%s) + ATTENTE_FEU )) "fichier_mondes_sha256=$H"
    mv "$T/journal-09-reel.txt" "$T/journal-09-reel-essai1.txt" && mv "$T/code-09-reel.txt" "$T/code-09-reel-essai1.txt" || arret_A "renommage de l'essai 1"
    controles_avant reel-2
    lancer_reel reel-2
    [ "$CODE_JOUER" != 2 ] || arret_A "second code 2 : aucune autre relance"
fi
CLES="non transmises depuis la fin de jouer (gardées pour le balayage jusqu'à la dernière poussée)"; j "appels finis : clés transmises à aucun processus désormais, sauf le balayage"
case "$CODE_JOUER" in
    0) aide jouer "$T/journal-09-$REEL.txt" "$([ "${ESSAI_REEL_A_BLANC:-0}" = 1 ] && echo a_blanc || echo reel)" >> "$L" 2>&1 \
           || noeud_garde "jouer $REEL : code 0 mais sortie différente de l'attendu (mode reel, 16 appels comptés, aucun arrêt)";;
    2) arret_A "jouer $REEL : code 2 avec lancement consigné";;
    3) arret_A "jouer $REEL : code 3 (arrêt du pilote) : ni relance, ni mesure, ni lecture, pas même P-0 ; nœud de Lazar";;
    *) if [ -e "$T/lancements.jsonl" ]; then arret_A "jouer $REEL : code $CODE_JOUER, lancement consigné"
       else noeud_garde "jouer $REEL : code $CODE_JOUER sans lancement consigné"; fi;;
esac
# --- 10. mesure (une seule fois), lecture non ouverte ---------------------------------------------------------------------------
ETAPE="mesure"; MOTIF=""; pousser "jouer $REEL fini (code 0), mesure" || true
O mesurer --sortie "$T/$REEL" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" > "$T/journal-10-mesurer.txt" 2>&1; CODE_MESURER=$?
echo "$CODE_MESURER" > "$T/code-10-mesurer.txt"
case "$CODE_MESURER" in
    0) aide mesurer "$T/journal-10-mesurer.txt" >> "$L" 2>&1 || noeud_garde "mesurer : programme inattendu";;
    3) arret_A "mesurer : code 3 : ni relance ni lecture";;
    *) ls "$T/$REEL" | grep -E '^(sortie-mesure|mesure-pilote-v70)' > "$T/journal-10-mesure-presente.txt" 2>&1
       noeud_garde "mesurer : code $CODE_MESURER (aucune relance ; présence d'une sortie de mesure : journal-10-mesure-presente.txt)";;
esac
O lire --sortie "$T/$REEL" --ecrire "$T/$REEL/lecture-pilote-v70.json" > "$T/sortie-lire-non-ouverte.txt" 2>&1; c=$?
echo "$c" > "$T/code-10-lire.txt"
[ "$c" = 0 ] || noeud_garde "lire : code $c (sortie remise au sous-agent sans être ouverte)"
# --- 11. rapatriement, poussée finale ---------------------------------------------------------------------------------------------
ETAPE="rapatriement"
rapatrier_reel
[ -d "$T/rapatrie-reel" ] || noeud_garde "rapatriement du réel non conforme"
( cd "$T/rapatrie-reel" && sha256sum -c lecture-pilote-v70.json.sha256 ) > "$T/journal-11-compagnon-lecture.txt" 2>&1 \
    || noeud_garde "lecture rapatriée ≠ son compagnon"
ETAPE="fini"; MOTIF="pilote joué, mesure faite, lecture écrite et rapatriée (non ouverte)"
pousser "fini" || { j "POUSSÉE FINALE EN ÉCHEC : résultats seulement sur le disque de la machine : nœud, ne pas détruire sans la mère"; ETAPE="fini, poussee finale en echec"; }
attente_finale
