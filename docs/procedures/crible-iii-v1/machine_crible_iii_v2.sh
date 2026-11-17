#!/usr/bin/env bash
# Programme machine du crible (iii) — v2 (procédure `procedure-machine-crible-iii-v2.md`, même dossier ; suit le programme v1,
# gardé tel quel : lanceur v2, aide v2, six fichiers du crible, tour 1 de la contre-lecture du code). Dérivé du programme
# machine v2 du pilote MR-2 (`machine_pilote_mr2_v74_v2.sh`, qui n'est pas modifié) ; pris au commit COMMIT_MAIN par l'amorce, à
# l'empreinte SCRIPT_SHA256, puis `exec` (même PID ; la minuterie de destruction, PID_MINUTERIE, reste son enfant).
# Ordre : mise en place (branches neuves, première poussée, numpy 2.5.3) ; pièces (paquet de l'arbre 605e0f6 et relevé de la sonde
# v74 au commit COMMIT_LOT ; code du crible, texte qui fait foi, addendum d'empreintes et registre des GO au commit COMMIT_MAIN) ;
# secret, puis phrase de Lazar (barrière 1, feu chiffré) ; vingt mondes (quatre processus), engagement poussé, inscription
# (barrière 2) ; C-16, C-17 et textes servis (`preparer`) ; essai à blanc sur les vrais mondes (relais factices, cinq files) et son
# rapatriement ; barrière 3 (feu réel, deux lignes de GO) ; contrôles juste avant ; crible réel (une seule fois, aucune relance) ;
# mesure (une seule fois) ; lecture écrite sans être ouverte ; rapatriement ; poussée finale reprise toutes les cinq minutes jusqu'à
# l'échéance si elle échoue. Un feu d'arrêt est lu à chaque attente et toutes les minutes pendant le crible réel (arrêt du lanceur par
# son PID, R10). Rien de privé ne sort : secret, phrase, clé privée de la phrase, mondes et textes servis restent dans $T/prive ou
# $T/<run>/prive et meurent avec la machine ; seuls les fichiers d'une liste blanche sont copiés, balayés (jeton, clé, secret,
# phrase), puis poussés sur BR_SORTIE.
# Clé : une seule (`RR_ANTHROPIC_API_KEY_RIGAUD` : un seul fournisseur sert les deux relais) ; lue dans une variable du programme,
# retirée de l'environnement des enfants (`export -n`) ; seul le crible réel la reçoit, par `env -i` ; effacée après la dernière
# poussée réussie. Aucune clé n'est jamais écrite sur le disque.
# Essai (ESSAI=1 seulement) : PATH_O_ESSAI, ESSAI_LANCEUR, ESSAI_MESURE, ESSAI_LIRE, ESSAI_SANS_PIP, ESSAI_SANS_TLS, ESSAI_REEL_A_BLANC, NUMPY_ESSAI,
# ATTENTE_PHRASE_S, ATTENTE_FEU_S, PAS_ENTREE_S, PAS_ETAT_S, BUDGET_REEL_S, PAS_REPRISE_S ; hors essai, chacune est refusée.
set -uo pipefail
for v in PATH_O_ESSAI ESSAI_LANCEUR ESSAI_MESURE ESSAI_LIRE ESSAI_SANS_PIP ESSAI_SANS_TLS ESSAI_REEL_A_BLANC NUMPY_ESSAI ATTENTE_PHRASE_S \
    ATTENTE_FEU_S PAS_ENTREE_S PAS_ETAT_S BUDGET_REEL_S PAS_REPRISE_S; do
    [ "$ESSAI" = 1 ] || [ -z "${!v:-}" ] || { echo "CRIBLE MACHINE REFUS : $v en essai seulement"; sleep infinity; }
done
JETON="$GH_TOKEN"; KA="$RR_ANTHROPIC_API_KEY_RIGAUD"
export -n GH_TOKEN RR_ANTHROPIC_API_KEY_RIGAUD CONTAINER_API_KEY
CLES=presentes
PL=docs/notes/organisme-multi-generations-v1/pilote-v1
BUNDLE_CHEMIN=$PL/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle
SONDE_CHEMIN=$PL/sonde-complete-v74-compte-organisme/sonde-complete-v74
CODE_CHEMIN=docs/procedures/crible-iii-v1
SHA_BUNDLE=e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1
SHA_RELEVE=f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529
TETE_ARBRE=605e0f60f3eed0948948e6a4eb15cb73de1d03de
NUMPY=${NUMPY_ESSAI:-2.5.3}
ATTENTE_PHRASE=${ATTENTE_PHRASE_S:-3600}   # la phrase dans l'heure qui suit la location
ATTENTE_FEU=${ATTENTE_FEU_S:-1200}         # feux 2 et 3 : 20 minutes chacun
PAS_ENTREE=${PAS_ENTREE_S:-60}
PAS_ETAT=${PAS_ETAT_S:-900}                # état poussé pendant le crible réel : toutes les 15 minutes
BUDGET_REEL=${BUDGET_REEL_S:-36000}        # garde de départ du crible : 4 × 7 200 s + 2 h = 10 h
SEUIL=95000000
PAS_REPRISE=${PAS_REPRISE_S:-300}
POUSSEE_OK=0; POUSSEE_ID=0
PX="${PATH_O_ESSAI:-/usr/local/bin:/usr/bin:/bin}"
X="$T/sortie"; S="$T/depot-sortie"; PV="$T/prive"; E="$T/entree"; L="$X/journal-machine.txt"; C="$T/code"
mkdir -p "$X" "$E" && mkdir -p -m 700 "$PV" && chmod 700 "$PV" || { echo "CRIBLE MACHINE : dossiers impossibles"; sleep infinity; }
AIDE="$T/machine_crible_iii_v2.py"
DEBUT_S=$(stat -c %Y "$T/amorce-lancee" 2>/dev/null || date +%s)
ETAPE="debut"; MOTIF=""; REEL=""; H=""; SM=""; CODE_JOUER=""; CODE_MESURER=""; PID_JOUER=""; EXCLUS=""; GC=""; GH=""
j() { printf '%s CRIBLE MACHINE %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
g() { GH_TOKEN="$JETON" git "$@"; }
aide() { env -i PATH="$PX" HOME=/root python3 -I -B "$AIDE" "$@"; }
O() { env -i PATH="$PX" HOME=/root python3 -I -B "${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v2.py}" "$@"; }
ARBRE="$T/arbre/orchestrator"
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
balayer() {
    # shellcheck disable=SC2068
    env -i PATH="$PX" HOME=/root S_JETON="$JETON" S_CLE_A="${KA:-}" python3 -I -B "$AIDE" balayer \
        --secret "$PV/secret.bin" --phrase "$PV/phrase.txt" $@ > "$T/balayage.txt" 2>&1; }
exclure_balayes() {
    local f
    [ -s "$T/exclus-balayage.txt" ] || return 0
    while IFS= read -r f; do [ -n "$f" ] && rm -f -- "$S/$f"; done < "$T/exclus-balayage.txt"
    EXCLUS="$(sort -u "$T/exclus-balayage.txt" | tr '\n' ' ')"; return 0; }
pousser() {  # $1 = motif ; balayage, puis poussée vérifiée par ls-remote
    local n loc dist liste
    POUSSEE_OK=0; POUSSEE_ID=$((POUSSEE_ID + 1)); copier_traces; ecrire_etat
    if [ ! -d "$S/.git" ]; then
        git init -q "$S" && git -C "$S" remote add origin "$DEPOT_URL" \
            && git -C "$S" config credential.helper '!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f' \
            && git -C "$S" config user.name "machine du crible (iii)" && git -C "$S" config user.email "machine-crible@invalid" \
            || { j "dépôt de sortie impossible"; return 1; }
    fi
    find "$S" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} + && cp -a "$X/." "$S/" || { j "copie vers le dépôt de sortie impossible"; return 1; }
    exclure_balayes
    liste=$(find "$S" -path "$S/.git" -prune -o -type f -print)
    while IFS= read -r n; do [ -z "$n" ] || [ "$(stat -c %s "$n")" -le "$SEUIL" ] || { j "fichier de plus de 95 Mo : ${n#$S/} : poussée refusée"; return 1; }; done <<< "$liste"
    if ! balayer $liste; then
        sed -n "s|^BALAYAGE : forme de .* trouvée dans $S/||p" "$T/balayage.txt" >> "$T/exclus-balayage.txt"
        [ -s "$T/exclus-balayage.txt" ] || { j "BALAYAGE : refus sans fichier nommé : poussée refusée"; return 1; }
        j "BALAYAGE : forme secrète trouvée : fichier(s) exclu(s) : $(sort -u "$T/exclus-balayage.txt" | tr '\n' ' ' | cut -c1-300)"
        exclure_balayes; ecrire_etat; cp -f "$X/etat.txt" "$S/etat.txt"; cp -f "$L" "$S/journal-machine.txt"
        liste=$(find "$S" -path "$S/.git" -prune -o -type f -print)
        balayer $liste || { j "BALAYAGE : refus après exclusion : poussée refusée"; return 1; }
    fi
    git -C "$S" add -A && { git -C "$S" diff --cached --quiet || git -C "$S" commit -q -m "crible (iii) : $1 (poussée $POUSSEE_ID)"; } \
        || { j "commit de sortie impossible"; return 1; }
    loc=$(git -C "$S" rev-parse HEAD) || return 1
    for n in 1 2 3; do
        if g -C "$S" push -q origin "HEAD:refs/heads/$BR_SORTIE" 2> "$T/poussee.err"; then
            dist=$(g -C "$S" ls-remote origin "refs/heads/$BR_SORTIE" 2>/dev/null | cut -f1)
            [ "$dist" = "$loc" ] && { j "poussé ($1) : $loc"; POUSSEE_OK=1; return 0; }
        fi
        j "poussée refusée, essai $n/3"; sleep $((10 * n)); done
    return 1; }
attente_finale() {  # aucune passe ; poussée échouée reprise toutes les PAS_REPRISE s jusqu'à l'échéance, puis clé effacée
    local k=0
    trap - EXIT
    while [ "$POUSSEE_OK" != 1 ]; do
        k=$((k + 1)); j "dernière poussée en échec : reprise $k dans $PAS_REPRISE s (jusqu'à l'échéance)"; sleep "$PAS_REPRISE"
        pousser "reprise $k ($ETAPE)" || true; done
    unset KA
    j "FIN ($ETAPE) : attente sans calcul ; destruction par la session (identifiant, -y, absence prouvée) ou par la minuterie"
    while :; do sleep 3600; done; }
rapatrier_reel() {
    [ -n "$REEL" ] && [ -d "$T/$REEL" ] && [ -n "$H" ] && [ ! -e "$T/rapatrie-reel" ] || return 0
    O rapatrier --source "$T/$REEL" --destination "$T/rapatrie-reel" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" \
        > "$T/journal-11-rapatrier.txt" 2>&1; echo $? > "$T/code-11-rapatrier.txt"
    aide rapatrier "$T/journal-11-rapatrier.txt" >> "$L" 2>&1 || { j "rapatriement du réel non conforme : rien n'en sort"; rm -rf "$T/rapatrie-reel"; }
    return 0; }
arret_A() { ETAPE="arret (A)"; MOTIF="$1"; j "ARRET (A) : $1"; rapatrier_reel; pousser "arrêt (A)" || j "traces non poussées"; attente_finale; }
noeud_garde() { ETAPE="noeud, machine gardee"; MOTIF="$1"; j "NOEUD, MACHINE GARDÉE : $1"; rapatrier_reel; pousser "nœud" || j "traces non poussées"; attente_finale; }
inattendue() { local c=$?; trap - EXIT; ETAPE="sortie inattendue"; MOTIF="code $c"; pousser "sortie inattendue" || true; attente_finale; }
trap inattendue EXIT
lire_entree() {
    rm -f "$E/$1"
    g -C "$D" fetch -q --filter=blob:none --depth=1 origin "+refs/heads/$BR_ENTREE:refs/remotes/origin/entree" > /dev/null 2>&1 || return 1
    g -C "$D" show "refs/remotes/origin/entree:$1" > "$E/$1" 2>/dev/null || { rm -f "$E/$1"; return 1; }; }
arret_demande() {
    lire_entree feu-arret.txt || return 1
    aide feu "$E/feu-arret.txt" arret > "$E/feu-arret.lu" 2>&1 || { j "feu d'arrêt illisible"; return 1; }
    return 0; }
attendre_feu() {  # $1 fichier, $2 genre, $3 échéance (s), puis attendus clé=valeur
    local f="$1" genre="$2" fin="$3" vu=""; shift 3
    while [ "$(date +%s)" -lt "$fin" ]; do
        arret_demande && arret_A "feu d'arrêt de la mère ($(grep -a '^cause=' "$E/feu-arret.txt" | head -c 200))"
        if lire_entree "$f"; then
            if aide feu "$E/$f" "$genre" "$@" > "$E/$f.lu" 2>&1; then j "feu $genre conforme"; return 0; fi
            [ "$(sha256sum < "$E/$f")" = "$vu" ] || { vu=$(sha256sum < "$E/$f"); j "feu $genre refusé (attente continuée) : $(head -c 200 "$E/$f.lu")"; }
        fi
        sleep "$PAS_ENTREE"; done
    arret_A "aucun feu $genre conforme avant $(date -u -d "@$fin" +%FT%TZ)"; }
inscription_sur_main() {  # $1 = .lu du feu ; puis empreintes
    local c ch
    c=$(sed -n 's/^inscription_commit=//p' "$1"); ch=$(sed -n 's/^inscription_chemin=//p' "$1"); shift
    g -C "$D" fetch -q --filter=blob:none --depth=200 origin "+refs/heads/main:refs/remotes/origin/main" > /dev/null 2>&1 \
        || arret_A "main injoignable : inscription non prouvée"
    git -C "$D" merge-base --is-ancestor "$c" refs/remotes/origin/main 2>/dev/null || arret_A "commit d'inscription absent de main"
    g -C "$D" show "$c:$ch" > "$E/inscription.txt" 2>/dev/null || arret_A "fichier d'inscription illisible au commit"
    aide inscription "$E/inscription.txt" "$@" >> "$L" 2>&1 || arret_A "empreintes non inscrites sur main"
    j "inscription prouvée sur main ($c, $ch)"; }
if [ "$ENTREE_RELANCE" = 1 ]; then
    REEL=$(cat "$T/reel-nom.txt" 2>/dev/null || true); H=$(cat "$T/h.txt" 2>/dev/null || true)
    arret_A "relance du conteneur par le loueur : aucune passe refaite"
fi
# --- mise en place ---------------------------------------------------------------------------------------------------------------
ETAPE="mise en place"; j "début ; échéance de la minuterie $(date -u -d "@$ECHEANCE_UTC_S" +%FT%TZ)"
g -C "$D" ls-remote --exit-code origin "refs/heads/$BR_SORTIE" > /dev/null 2>&1; c=$?
[ "$c" = 2 ] || { j "ARRET : branche de sortie $BR_SORTIE présente (R12) ou dépôt injoignable (code $c) : rien n'est poussé"; trap - EXIT; POUSSEE_OK=1; attente_finale; }
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
# --- pièces, arbre, code du crible ------------------------------------------------------------------------------------------------
ETAPE="pieces et arbre"
git -C "$D" config core.sparseCheckout true && git -C "$D" config core.sparseCheckoutCone false \
    && printf '/%s\n/%s/\n' "$BUNDLE_CHEMIN" "$SONDE_CHEMIN" > "$D/.git/info/sparse-checkout" \
    && g -C "$D" -c advice.detachedHead=false checkout -q --detach "$COMMIT_LOT" || arret_A "extraction partielle du commit $COMMIT_LOT"
for p in runs diag donnees essai registres; do [ ! -e "$D/$p" ] || arret_A "$p/ présent dans l'arbre extrait"; done
mkdir -p "$C" && cp -f "$D/$BUNDLE_CHEMIN" "$T/arbre-organisme-complet-605e0f6.bundle" && cp -a "$D/$SONDE_CHEMIN" "$T/sonde" \
    || arret_A "paquet ou relevé de la sonde illisibles au commit $COMMIT_LOT"
for f in crible_iii_v1.py crible_iii_v2.py lanceur_crible_iii_v2.py mesure_crible_iii_v1.py lire_crible_iii_v1.py \
    relais_factice_crible_iii_v1.py; do
    g -C "$D" show "$COMMIT_MAIN:$CODE_CHEMIN/$f" > "$C/$f" 2>/dev/null || arret_A "code du crible ($f) absent du commit $COMMIT_MAIN"; done
g -C "$D" show "$COMMIT_MAIN:$TEXTE_CHEMIN" > "$T/texte.md" && g -C "$D" show "$COMMIT_MAIN:$ADDENDUM_CHEMIN" > "$T/addendum.md" \
    && g -C "$D" show "$COMMIT_MAIN:registres/go.md" > "$T/go-main.md" || arret_A "texte, addendum ou registre des GO illisibles au commit"
( cd "$T" && sha256sum arbre-organisme-complet-605e0f6.bundle texte.md addendum.md go-main.md sonde/releve-sonde-pilote-v74.json code/* ) > "$T/journal-04-pieces.txt"
[ "$(sha256sum < "$T/arbre-organisme-complet-605e0f6.bundle" | cut -d' ' -f1)" = "$SHA_BUNDLE" ] || arret_A "paquet : empreinte différente"
[ "$(sha256sum < "$T/texte.md" | cut -d' ' -f1)" = "$TEXTE_SHA256" ] || arret_A "texte qui fait foi : empreinte différente"
[ "$(sha256sum < "$T/addendum.md" | cut -d' ' -f1)" = "$ADDENDUM_SHA256" ] || arret_A "addendum d'empreintes : empreinte différente"
[ "$(sha256sum < "$T/sonde/releve-sonde-pilote-v74.json" | cut -d' ' -f1)" = "$SHA_RELEVE" ] || arret_A "relevé de la sonde : empreinte différente"
[ "$(cut -d' ' -f1 "$T/sonde/releve-sonde-pilote-v74.json.sha256" 2>/dev/null)" = "$SHA_RELEVE" ] || arret_A "compagnon du relevé absent ou différent"
SHA_MESURE=$(aide addendum "$T/addendum.md" "$C" "$TEXTE_SHA256") || arret_A "code du crible différent de l'addendum d'empreintes"
git init -q "$T/arbre" && git -C "$T/arbre" bundle unbundle "$T/arbre-organisme-complet-605e0f6.bundle" > /dev/null \
    && git -C "$T/arbre" -c advice.detachedHead=false checkout -q "$TETE_ARBRE" || arret_A "dépaquetage de l'arbre"
[ "$(git -C "$T/arbre" rev-parse HEAD)" = "$TETE_ARBRE" ] || arret_A "tête de l'arbre ≠ 605e0f6"
[ -z "$(git -C "$T/arbre" status --porcelain --ignored)" ] || arret_A "arbre non propre"
j "pièces aux empreintes attendues ; arbre 605e0f6 propre ; code du crible égal à l'addendum"
# --- secret, puis phrase de Lazar (barrière 1) ------------------------------------------------------------------------------------
ETAPE="secret"
[ ! -e "$PV/secret.bin" ] || arret_A "secret déjà présent"
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
# --- vingt mondes, puis barrière 2 -------------------------------------------------------------------------------------------------
ETAPE="mondes"; pousser "phrase reçue, génération des mondes" || true
O generer --arbre "$ARBRE" --secret "$PV/secret.bin" --phrase-fichier "$PV/phrase.txt" --texte-sha256 "$TEXTE_SHA256" \
    --sortie "$PV/MONDES.json" --processus 4 > "$T/journal-06-generer.txt" 2>&1; c=$?; echo "$c" > "$T/code-06-generer.txt"
[ "$c" = 0 ] || arret_A "generer : code $c (une graine neuve demande un texte neuf et le mot de Lazar)"
H=$(aide generer "$T/journal-06-generer.txt") || arret_A "generer : un monde non conforme"
echo "$H" > "$T/h.txt"
SM=$(aide engagement "$PV/MONDES.json.engagement.json" "$H") || arret_A "engagement des mondes illisible"
ETAPE="attente du feu 2 (mondes)"; MOTIF="empreintes H et S1 à S20 (engagement-mondes.json) à inscrire sur main"
pousser "mondes générés, attente de l'inscription" || arret_A "engagement des mondes non poussé"
attendre_feu feu-2-mondes.txt mondes $(( $(date +%s) + ATTENTE_FEU )) "fichier_mondes_sha256=$H"
# shellcheck disable=SC2086
inscription_sur_main "$E/feu-2-mondes.txt.lu" "$H" $(echo "$SM" | tr ',' ' ')
# --- préparation, essai à blanc sur les vrais mondes, barrière 3 -------------------------------------------------------------------
ETAPE="preparer"; MOTIF=""
O preparer --arbre "$ARBRE" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" --texte-sha256 "$TEXTE_SHA256" > "$T/journal-07-preparer.txt" 2>&1; c=$?
echo "$c" > "$T/code-07-preparer.txt"
[ "$c" = 0 ] || arret_A "preparer : code $c (C-16, C-17, textes servis ou octets)"
aide preparer "$T/journal-07-preparer.txt" >> "$L" 2>&1 || arret_A "preparer : sortie non conforme"
ETAPE="essai a blanc"
O jouer --mode a_blanc --arbre "$ARBRE" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" --texte-sha256 "$TEXTE_SHA256" \
    --sortie "$T/blanc" --echeance-utc-s "$ECHEANCE_UTC_S" --releve-sonde "$T/sonde/releve-sonde-pilote-v74.json" \
    > "$T/journal-08-blanc.txt" 2>&1; c=$?; echo "$c" > "$T/code-08-blanc.txt"
[ "$c" = 0 ] || arret_A "essai à blanc : code $c"
aide jouer "$T/journal-08-blanc.txt" a_blanc >> "$L" 2>&1 || arret_A "essai à blanc : sortie différente de l'attendu"
O rapatrier --source "$T/blanc" --destination "$T/rapatrie-blanc" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" \
    > "$T/journal-08-rapatrier-blanc.txt" 2>&1; c=$?
[ "$c" = 0 ] || arret_A "rapatriement à blanc : code $c"
aide rapatrier "$T/journal-08-rapatrier-blanc.txt" >> "$L" 2>&1 || { rm -rf "$T/rapatrie-blanc"; arret_A "rapatriement à blanc : un monde porté"; }
rm -rf "$T/rapatrie-blanc/monde-"*   # corps des relais factices : rien d'utile à la mère, trop d'octets
ETAPE="attente du feu 3 (crible reel)"; MOTIF="essai à blanc conforme (100 appels complets, 20 mondes complets, cinq files)"
pousser "essai à blanc conforme, attente du feu réel" || arret_A "essai à blanc non poussé"
attendre_feu feu-3-reel.txt reel $(( $(date +%s) + ATTENTE_FEU )) "fichier_mondes_sha256=$H" "go_credits=$GO_CREDITS" "go_hors=$GO_HORS"
# --- crible réel (une seule fois ; aucune relance, aucune reprise d'appel) ---------------------------------------------------------
[ ! -e "$T/reel" ] && [ ! -e "$T/lancements.jsonl" ] || arret_A "dossier reel ou registre des lancements déjà présent"
[ "$(env -i PATH="$PX" HOME=/root python3 -I -c 'import numpy;print(numpy.__version__)' 2>&1)" = "$NUMPY" ] || arret_A "numpy ≠ $NUMPY"
[ "$(sha256sum < "$T/texte.md" | cut -d' ' -f1)" = "$TEXTE_SHA256" ] || arret_A "texte : empreinte différente juste avant"
aide ports >> "$L" 2>&1 || arret_A "un port des relais est occupé"
[ "${ESSAI_SANS_TLS:-0}" = 1 ] || aide tls >> "$L" 2>&1 || arret_A "le fournisseur est injoignable"
[ $(( ECHEANCE_UTC_S - $(date +%s) )) -ge "$BUDGET_REEL" ] || arret_A "moins de $BUDGET_REEL s avant l'échéance : le crible ne partirait pas (garde de départ, aucun appel)"
[ -n "${KA:-}" ] || arret_A "clé absente juste avant"
REEL=reel; echo "$REEL" > "$T/reel-nom.txt"; ETAPE="jouer reel en cours"; MOTIF=""
MODE=reel; [ "${ESSAI_REEL_A_BLANC:-0}" = 1 ] && MODE=a_blanc
if [ "$MODE" = reel ]; then
    env -i PATH="$PX" HOME=/root RR_ANTHROPIC_API_KEY_RIGAUD="$KA" python3 -I -B "${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v2.py}" jouer \
        --mode reel --arbre "$ARBRE" --mondes "$PV/MONDES.json" --mondes-sha256 "$H" --texte-sha256 "$TEXTE_SHA256" --sortie "$T/reel" \
        --echeance-utc-s "$ECHEANCE_UTC_S" --releve-sonde "$T/sonde/releve-sonde-pilote-v74.json" --texte "$T/texte.md" \
        --registre-go "$T/go-main.md" --go-credits "$GO_CREDITS" --go-hors "$GO_HORS" --mondes-shas "$SM" \
        --registre-lancements "$T/lancements.jsonl" --addendum "$T/addendum.md" > "$T/journal-09-reel.txt" 2>&1 < /dev/null &
else  # essai seulement : même chemin, mode à blanc
    env -i PATH="$PX" HOME=/root python3 -I -B "${ESSAI_LANCEUR:-$C/lanceur_crible_iii_v2.py}" jouer --mode a_blanc --arbre "$ARBRE" \
        --mondes "$PV/MONDES.json" --mondes-sha256 "$H" --texte-sha256 "$TEXTE_SHA256" --sortie "$T/reel" \
        --echeance-utc-s "$ECHEANCE_UTC_S" --releve-sonde "$T/sonde/releve-sonde-pilote-v74.json" > "$T/journal-09-reel.txt" 2>&1 < /dev/null &
fi
PID_JOUER=$!
j "crible réel lancé (PID $PID_JOUER)"
pousser "crible réel lancé" || true
dernier=$(date +%s)
while kill -0 "$PID_JOUER" 2> /dev/null; do
    sleep "$PAS_ENTREE"
    kill -0 "$PID_JOUER" 2> /dev/null || break
    if arret_demande; then
        j "feu d'arrêt de la mère pendant le crible : arrêt du lanceur par son PID $PID_JOUER (R10)"
        kill -TERM "$PID_JOUER" 2>/dev/null; wait "$PID_JOUER" 2>/dev/null; echo "arrete-par-feu" > "$T/code-09-reel.txt"
        arret_A "feu d'arrêt de la mère pendant le crible ($(grep -a '^cause=' "$E/feu-arret.txt" | head -c 200))"
    fi
    if [ $(( $(date +%s) - dernier )) -ge "$PAS_ETAT" ]; then MOTIF="crible en cours depuis $(( $(date +%s) - $(stat -c %Y "$T/reel-nom.txt") )) s"; pousser "crible en cours" || true; dernier=$(date +%s); fi
done
wait "$PID_JOUER"; CODE_JOUER=$?; echo "$CODE_JOUER" > "$T/code-09-reel.txt"
j "crible réel : code $CODE_JOUER"
CLES="non transmise depuis la fin du crible (gardée pour le balayage jusqu'à la dernière poussée)"
case "$CODE_JOUER" in
    0) aide jouer "$T/journal-09-reel.txt" "$([ "$MODE" = a_blanc ] && echo a_blanc || echo reel)" >> "$L" 2>&1 \
           || noeud_garde "crible : code 0 mais sortie différente de l'attendu";;
    2) arret_A "crible : code 2 (refus nommé ; aucune relance)";;
    3) arret_A "crible : code 3 (ligne d'arrêt) : ni mesure, ni lecture d'issue ; nœud de Lazar";;
    *) if [ -e "$T/lancements.jsonl" ]; then arret_A "crible : code $CODE_JOUER, lancement consigné"
       else noeud_garde "crible : code $CODE_JOUER sans lancement consigné"; fi;;
esac
# --- mesure (une seule fois), lecture non ouverte, rapatriement --------------------------------------------------------------------
ETAPE="mesure"; MOTIF=""; pousser "crible fini (code 0), mesure" || true
env -i PATH="$PX" HOME=/root python3 -I -B "${ESSAI_MESURE:-$C/mesure_crible_iii_v1.py}" mesurer --arbre "$ARBRE" --mondes "$PV/MONDES.json" \
    --mondes-sha256 "$H" --sortie "$T/reel" --texte-sha256 "$TEXTE_SHA256" > "$T/journal-10-mesurer.txt" 2>&1; CODE_MESURER=$?
echo "$CODE_MESURER" > "$T/code-10-mesurer.txt"
case "$CODE_MESURER" in
    0) aide mesurer "$T/journal-10-mesurer.txt" "$SHA_MESURE" >> "$L" 2>&1 || noeud_garde "mesurer : programme inattendu";;
    2|3) arret_A "mesurer : code $CODE_MESURER (refus ou défaut) : rien n'est lu";;
    *) noeud_garde "mesurer : code $CODE_MESURER (exception : rien n'est lu ; correction sous un nom neuf, mêmes entrées : hors d'atteinte sans ssh)";;
esac
env -i PATH="$PX" HOME=/root python3 -I -B "${ESSAI_LIRE:-$C/lire_crible_iii_v1.py}" --sortie "$T/reel" --ecrire "$T/reel/lecture-crible-iii-v1.json" \
    > "$T/sortie-lire-non-ouverte.txt" 2>&1; c=$?
echo "$c" > "$T/code-10-lire.txt"
[ "$c" = 0 ] || noeud_garde "lire : code $c (sortie remise au sous-agent sans être ouverte)"
ETAPE="rapatriement"
rapatrier_reel
[ -d "$T/rapatrie-reel" ] || noeud_garde "rapatriement du réel non conforme"
( cd "$T/rapatrie-reel" && sha256sum -c lecture-crible-iii-v1.json.sha256 ) > "$T/journal-11-compagnon-lecture.txt" 2>&1 \
    || noeud_garde "lecture rapatriée ≠ son compagnon"
ETAPE="fini"; MOTIF="crible joué, mesure faite, lecture écrite et rapatriée (non ouverte)"
pousser "fini" || j "POUSSÉE FINALE EN ÉCHEC : reprise toutes les $PAS_REPRISE s jusqu'à l'échéance"
attente_finale
