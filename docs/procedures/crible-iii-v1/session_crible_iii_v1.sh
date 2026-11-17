#!/usr/bin/env bash
# Outil de la session qui lance le crible (iii) sans ssh — v1 (procédure `procedure-machine-crible-iii-v1.md`, même dossier ; dérivé de
# l'outil v4 de la session du pilote MR-2 et du lanceur v2 de la machine de l'idée 1.1, qui ne sont pas modifiés).
# Aucune commande de ce script ne crée ni ne détruit d'instance : il contrôle, lit (lecture seule), écrit les feux de la mère sur la
# branche d'entrée et IMPRIME les commandes de création et de destruction, que l'opérateur joue lui-même sous le préfixe GO_ID
# (garde de calcul ; destruction par l'identifiant, R10). Sorties de l'outil du loueur écrites sous `umask 077` dans un dossier
# jetable, lues par programme, supprimées aussitôt (la configuration des instances porte les clés passées par `--env`).
# Variables : W (dépôt de travail, défaut /home/user/controle-ia-travail) ; ENVP (dossier d'envoi hors dépôt, défaut
#   /home/user/crible-iii-envoi-v1) ; VASTAI (défaut /home/user/vastai-env/bin/vastai) ; PYTHON_SESSION.
# Codes : 0 accepté ; 2 refus (motif sur la sortie standard).
set -uo pipefail
ICI="$(cd "$(dirname "$0")" && pwd)"
W="${W:-/home/user/controle-ia-travail}"
ENVP="${ENVP:-/home/user/crible-iii-envoi-v1}"
VASTAI="${VASTAI:-/home/user/vastai-env/bin/vastai}"
PY="${PYTHON_SESSION:-python3}"
IMAGE=python:3.13-bookworm
DISQUE=20
DOSSIER_CODE=docs/procedures/crible-iii-v1
AMORCE="$ICI/amorce_crible_iii_v1.sh"
r() { echo "CRIBLE SESSION REFUS : $*"; exit 2; }
aide() { "$PY" -I -B "$ICI/garde_session_crible_iii_v1.py" "$@"; }
hex() { printf '%s' "$1" | LC_ALL=C grep -qxE "[0-9a-f]{$2}"; }
branche() { printf '%s' "$1" | LC_ALL=C grep -qxE 'calcul/crible-iii-[A-Za-z0-9._-]+' && case "$1" in *..*|*.lock|*/) false;; *) true;; esac; }
lire_prive() {  # $1 = objet de `show` (instances | user) : imprime le chemin d'un fichier privé (umask 077), rien d'autre
    local dl f c
    dl=$(mktemp -d) || return 1
    f="$dl/sortie.json"
    ( umask 077; "$VASTAI" show "$1" --raw < /dev/null > "$f" 2> "$dl/erreur.txt" ); c=$?
    if [ "$c" != 0 ]; then rm -f -- "$f" "$dl/erreur.txt"; rmdir -- "$dl"; echo "lecture de « show $1 » en échec (code $c)" >&2; return 1; fi
    echo "$f"; }
lire_sortie() { git -C "$W" fetch -q origin "+refs/heads/$1:refs/remotes/origin/$1" 2>/dev/null || return 1
    git -C "$W" show "refs/remotes/origin/$1:$2" 2>/dev/null; }
etat_vaut() { [ "$(lire_sortie "$1" etat.txt | sed -n 's/^etape=//p')" = "$2" ]; }
ecrire_entree() {  # $1 = branche d'entrée ; puis paires NOM FICHIER : commit posé sur le sommet de la branche, poussé, relu
    local br="$1" tip lignes n f b arbre c dist; shift
    branche "$br" || r "branche d'entrée illisible"
    tip=""
    if git -C "$W" ls-remote --exit-code origin "refs/heads/$br" > /dev/null 2>&1; then
        git -C "$W" fetch -q origin "+refs/heads/$br:refs/remotes/origin/$br" || r "branche d'entrée illisible"
        tip=$(git -C "$W" rev-parse "refs/remotes/origin/$br") || r "sommet de la branche d'entrée illisible"
    fi
    lignes=$( [ -n "$tip" ] && git -C "$W" ls-tree "$tip" )
    while [ "$#" -ge 2 ]; do
        n="$1"; f="$2"; shift 2
        b=$(git -C "$W" hash-object -w -- "$f") || r "objet de $n impossible"
        lignes=$(printf '%s\n' "$lignes" | awk -F '\t' -v n="$n" '$2 != n && NF'; printf '100644 blob %s\t%s\n' "$b" "$n")
    done
    arbre=$(printf '%s\n' "$lignes" | grep -v '^$' | git -C "$W" mktree) || r "arbre de l'entrée impossible"
    if [ -n "$tip" ]; then c=$(git -C "$W" commit-tree "$arbre" -p "$tip" -m "crible (iii) : feu de la mère") || r "commit impossible"
    else c=$(git -C "$W" commit-tree "$arbre" -m "crible (iii) : feu de la mère") || r "commit impossible"; fi
    git -C "$W" push -q origin "$c:refs/heads/$br" || r "poussée de la branche d'entrée refusée : nœud (ne pas contourner)"
    dist=$(git -C "$W" ls-remote origin "refs/heads/$br" | cut -f1)
    [ "$dist" = "$c" ] || r "sommet distant de l'entrée ≠ commit poussé"
    echo "feu poussé sur $br : $c"; }
inscription() {  # $1 = commit de main ; $2 = chemin ; puis empreintes : toutes dans le fichier, commit ancêtre de main
    local c="$1" ch="$2" e; shift 2
    hex "$c" 40 || r "commit d'inscription : 40 caractères hexadécimaux"
    printf '%s' "$ch" | LC_ALL=C grep -qxE '[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*' && case "$ch" in *..*) false;; *) true;; esac || r "chemin d'inscription illisible"
    git -C "$W" fetch -q origin +refs/heads/main:refs/remotes/origin/main || r "main illisible"
    git -C "$W" merge-base --is-ancestor "$c" refs/remotes/origin/main || r "commit d'inscription absent de main"
    for e in "$@"; do git -C "$W" show "$c:$ch" | grep -qF "$e" || r "empreinte ${e:0:12}… absente de $ch au commit"; done; }
case "${1:-}" in
    credit) F=$(lire_prive user) || r "crédit illisible : aucune création"; aide credit "$F" --supprimer; exit $?;;
    inventaire)  # inventaire NOM : identifiants seuls dans $ENVP/ids-NOM.txt (écrit une fois)
        [ "$#" = 2 ] && printf '%s' "$2" | grep -qxE '[a-z-]+' || r "inventaire NOM"
        F=$(lire_prive instances) || r "liste des instances illisible"
        aide inventaire "$F" "$ENVP/ids-$2.txt" --supprimer; exit $?;;
    offre-depuis-recherche) [ "$#" = 3 ] || r "offre-depuis-recherche RECHERCHE.json OFFRE.json"; aide offre-depuis-recherche "$2" "$3"; exit $?;;
    commande)  # commande OFFRE.json COMMIT_LOT COMMIT_MAIN BR_SORTIE BR_ENTREE ETIQUETTE GO_CREDITS GO_HORS TEXTE_CHEMIN ADDENDUM_CHEMIN
        [ "$#" = 11 ] || r "commande OFFRE.json COMMIT_LOT COMMIT_MAIN BR_SORTIE BR_ENTREE ETIQUETTE GO_CREDITS GO_HORS TEXTE_CHEMIN ADDENDUM_CHEMIN"
        FO="$2"; CL="$3"; CM="$4"; BS="$5"; BE="$6"; ETIQ="$7"; GC="$8"; GH="$9"; TC="${10}"; AC="${11}"
        printf '%s' "$ETIQ" | LC_ALL=C grep -qxE 'crible-iii-v1-[0-9]{8}' || r "étiquette illisible (crible-iii-v1-AAAAMMJJ)"
        for c in "$CL" "$CM"; do hex "$c" 40 || r "commit illisible (40 hex)"; git -C "$W" cat-file -e "$c^{commit}" 2>/dev/null || r "commit $c absent de $W"; done
        git -C "$W" fetch -q origin +refs/heads/main:refs/remotes/origin/main || r "main illisible"
        git -C "$W" merge-base --is-ancestor "$CM" refs/remotes/origin/main || r "COMMIT_MAIN pas un ancêtre de main"
        branche "$BS" && branche "$BE" && [ "$BS" != "$BE" ] || r "branches de sortie et d'entrée : calcul/crible-iii-…, distinctes"
        for v in CONTROLE_IA_GITHUB_TOKEN_2 RR_ANTHROPIC_API_KEY_RIGAUD; do
            printf '%s' "${!v:-}" | LC_ALL=C grep -qxE '[A-Za-z0-9_-]{8,}' || r "$v absente ou de forme illisible pour --env (nom seul)"; done
        OFFRE=$("$PY" -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["id"])' "$FO" 2>/dev/null) || r "OFFRE.json illisible"
        P=$(aide offre "$FO" "$OFFRE") || r "$P"
        PRIX=$(printf '%s' "$P" | sed -n 's/^offre [0-9]* conforme : \([0-9.]*\) USD\/h$/\1/p'); [ -n "$PRIX" ] || r "prix de l'offre illisible"
        git -C "$W" show "$CM:$DOSSIER_CODE/amorce_crible_iii_v1.sh" | cmp -s - "$AMORCE" || r "amorce du commit ≠ celle de ce dossier"
        SH=$(git -C "$W" show "$CM:$DOSSIER_CODE/machine_crible_iii_v1.sh" | sha256sum | cut -d' ' -f1)
        AH=$(git -C "$W" show "$CM:$DOSSIER_CODE/machine_crible_iii_v1.py" | sha256sum | cut -d' ' -f1)
        TS=$(git -C "$W" show "$CM:$TC" 2>/dev/null | sha256sum | cut -d' ' -f1); git -C "$W" cat-file -e "$CM:$TC" 2>/dev/null || r "texte $TC absent du commit"
        AS=$(git -C "$W" show "$CM:$AC" 2>/dev/null | sha256sum | cut -d' ' -f1); git -C "$W" cat-file -e "$CM:$AC" 2>/dev/null || r "addendum $AC absent du commit"
        [ "$(git -C "$W" show "$CM:$TC.sha256" 2>/dev/null | cut -d' ' -f1)" = "$TS" ] || r "texte qui fait foi ≠ son compagnon au commit"
        [ "$(git -C "$W" show "$CM:$AC.sha256" 2>/dev/null | cut -d' ' -f1)" = "$AS" ] || r "addendum ≠ son compagnon au commit"
        git -C "$W" cat-file -e "$CL:docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle" 2>/dev/null \
            || r "paquet de l'arbre absent de COMMIT_LOT"
        TD=$(mktemp -d); git -C "$W" show "$CM:registres/go.md" > "$TD/go.md" || { rm -rf "$TD"; r "registre des GO illisible au commit"; }
        M=$(aide go "$TD/go.md" "$GC" "$GH" "$(date -u +%F)"); c=$?; rm -rf "$TD"; [ "$c" = 0 ] || r "lignes de GO : $M"
        for b in "$BS" "$BE"; do git -C "$W" ls-remote --exit-code origin "refs/heads/$b" > /dev/null 2>&1; c=$?
            [ "$c" = 2 ] || r "branche $b présente sur le dépôt distant (R12) ou dépôt injoignable (code $c)"; done
        ECH=$(aide echeance "$(date +%s)" "$PRIX") || r "$ECH"
        RAC=$(mktemp -d) || r "dossier jetable impossible"
        AMORCE_ESSAI=1 AMORCE_ARGUMENTS_SEULS=1 RACINE_AMORCE="$RAC" COMMIT_LOT="$CL" COMMIT_MAIN="$CM" BR_SORTIE="$BS" BR_ENTREE="$BE" \
            ECHEANCE_UTC_S="$ECH" GO_ID="$GH" GO_CREDITS="$GC" GO_HORS="$GH" TEXTE_CHEMIN="$TC" TEXTE_SHA256="$TS" ADDENDUM_CHEMIN="$AC" \
            ADDENDUM_SHA256="$AS" SCRIPT_SHA256="$SH" AIDE_SHA256="$AH" GH_TOKEN=factice-00000000 RR_ANTHROPIC_API_KEY_RIGAUD=factice-00000000 \
            env -u CONTAINER_ID bash "$AMORCE" > "$RAC.txt" 2>&1; c=$?
        rmdir "$RAC" 2>/dev/null || { rm -f "$RAC.txt"; r "l'amorce en essai des arguments a écrit dans le dossier jetable"; }
        [ "$c" = 0 ] || { cat "$RAC.txt"; rm -f "$RAC.txt"; r "arguments refusés par l'amorce"; }
        rm -f "$RAC.txt"
        [ ! -e "$ENVP/echeance.txt" ] || r "echeance.txt existe déjà : commande déjà imprimée ; ne jamais créer deux fois"
        date -u -d "@$ECH" +%FT%TZ > "$ENVP/echeance.txt"
        ( umask 077; gzip -9 -n -c < "$AMORCE" | base64 -w 0 > "$ENVP/amorce.b64" ) || r "amorce illisible"
        L1="GH_TOKEN=\"\$CONTROLE_IA_GITHUB_TOKEN_2\"; ENVP=$ENVP; umask 077"
        L2="GO_ID=$GH $VASTAI create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT_LOT=$CL -e COMMIT_MAIN=$CM -e BR_SORTIE=$BS -e BR_ENTREE=$BE -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GH -e GO_CREDITS=$GC -e GO_HORS=$GH -e TEXTE_CHEMIN=$TC -e TEXTE_SHA256=$TS -e ADDENDUM_CHEMIN=$AC -e ADDENDUM_SHA256=$AS -e SCRIPT_SHA256=$SH -e AIDE_SHA256=$AH -e GH_TOKEN=\$GH_TOKEN -e RR_ANTHROPIC_API_KEY_RIGAUD=\$RR_ANTHROPIC_API_KEY_RIGAUD\" --entrypoint bash --args -c \"echo \$(cat \"\$ENVP/amorce.b64\") | base64 -d | gunzip > /root/amorce_crible_iii_v1.sh && bash /root/amorce_crible_iii_v1.sh\" < /dev/null > \"\$ENVP/creation.json\"; echo code=\$?"
        printf '%s\n%s\n' "$L1" "$L2" > "$ENVP/commande-creation.txt"
        echo "CRIBLE SESSION : offre $OFFRE à $PRIX USD/h ; échéance de la minuterie $(date -u -d "@$ECH" +%FT%TZ) ; amorce $(sha256sum < "$AMORCE" | cut -c1-16), programme ${SH:0:16}, aide ${AH:0:16}, texte ${TS:0:16}, addendum ${AS:0:16}"
        echo "CRIBLE SESSION COMMANDE (deux lignes, une seule commande ; la seconde commence par GO_ID= ; écrites aussi dans $ENVP/commande-creation.txt, pour comparer) :"
        printf '%s\n%s\n' "$L1" "$L2"
        exit 0;;
    comparer) [ "$#" = 2 ] && [ -f "$ENVP/commande-creation.txt" ] || r "comparer FICHIER (après commande)"
        cmp -s "$2" "$ENVP/commande-creation.txt" || r "lignes différentes de la commande imprimée : ne pas jouer"
        echo "CRIBLE SESSION : lignes égales à l'octet à la commande imprimée";;
    essai-poussee) [ "$#" = 2 ] || r "essai-poussee BRANCHE"
        case "$2" in calcul/crible-iii-sortie-*|calcul/crible-iii-entree-*) r "jamais une branche du crible";; esac
        TD=$(mktemp -d); printf 'essai de poussée de la session (aucun feu), %s\n' "$(date -u +%FT%TZ)" > "$TD/f"
        ( ecrire_entree "$2" essai-poussee.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    creation) [ ! -e "$ENVP/identifiant.txt" ] || r "identifiant.txt existe déjà : jamais récrit"
        N=$(aide creation "$ENVP/creation.json" --supprimer) || r "$N"
        echo "$N" > "$ENVP/identifiant.txt"; echo "ID=$N";;
    trouver) [ "$#" = 2 ] && [ ! -e "$ENVP/identifiant.txt" ] || r "trouver ETIQUETTE (identifiant.txt absent)"
        F=$(lire_prive instances) || r "liste des instances illisible"
        N=$(aide trouver "$F" "$2" --supprimer) || r "$N"; echo "$N" > "$ENVP/identifiant.txt"; echo "ID=$N";;
    relire) [ "$#" = 2 ] || r "relire ETIQUETTE"
        N=$(cat "$ENVP/identifiant.txt") && printf '%s' "$N" | grep -qxE '[1-9][0-9]*' || r "identifiant illisible"
        F=$(lire_prive instances) || r "liste des instances illisible"; aide relire "$F" "$N" "$2" --supprimer; exit $?;;
    ajoute) aide ajoute "$ENVP/ids-avant.txt" "$ENVP/ids-apres-creation.txt" "$(cat "$ENVP/identifiant.txt")"; exit $?;;
    depense) [ "$#" = 3 ] || r "depense CUMUL PRIX"; aide depense "$2" "$3"; c=$?
        [ "$c" = 0 ] || echo "CRIBLE SESSION : arrêt et destruction par l'identifiant (R10) : bash $0 detruire ETIQUETTE"; exit "$c";;
    etat) [ "$#" = 2 ] && branche "$2" || r "etat BR_SORTIE"
        lire_sortie "$2" etat.txt || { echo "CRIBLE SESSION : branche de sortie pas encore poussée"; exit 2; }
        echo "--- journal de la machine (fin)"; lire_sortie "$2" journal-machine.txt | tail -n 12; exit 0;;
    feu-phrase)  # feu-phrase BR_SORTIE BR_ENTREE FICHIER_PHRASE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION
        [ "$#" = 6 ] || r "feu-phrase BR_SORTIE BR_ENTREE FICHIER_PHRASE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION"
        BS="$2"; BE="$3"; FP="$4"; CI="$5"; CH="$6"
        etat_vaut "$BS" "attente du feu 1 (phrase)" || r "la machine n'attend pas la phrase"
        SS=$(lire_sortie "$BS" secret-sha256.txt | sed -n 's/^secret_sha256=//p'); hex "$SS" 64 || r "empreinte du secret illisible"
        inscription "$CI" "$CH" "$SS"
        [ -f "$FP" ] || r "fichier de la phrase absent"
        "$PY" -I -B - "$FP" <<'X' || r "phrase : une ligne non vide, sans octet nul, finie par un retour à la ligne, au plus 400 octets"
import sys
b = open(sys.argv[1], "rb").read()
ok = 2 <= len(b) <= 400 and b.count(b"\n") == 1 and b.endswith(b"\n") and b"\0" not in b and b"\r" not in b
b.decode("utf-8")
sys.exit(0 if ok else 1)
X
        TD=$(mktemp -d) || r "dossier jetable impossible"
        lire_sortie "$BS" cle-publique-phrase.pem > "$TD/cle.pem" && [ -s "$TD/cle.pem" ] || { rm -rf "$TD"; r "clé publique absente"; }
        [ "$(openssl pkey -pubin -in "$TD/cle.pem" -outform DER 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(lire_sortie "$BS" cle-publique-phrase.empreinte)" ] \
            || { rm -rf "$TD"; r "clé publique ≠ son empreinte poussée"; }
        openssl pkey -pubin -in "$TD/cle.pem" -text_pub -noout 2>/dev/null > "$TD/cle.txt"
        grep -qx 'Public-Key: (4096 bit)' "$TD/cle.txt" || { rm -rf "$TD"; r "clé publique de la phrase : RSA de 4096 bits exigée"; }
        openssl pkeyutl -encrypt -pubin -inkey "$TD/cle.pem" -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 \
            -pkeyopt rsa_mgf1_md:sha256 -in "$FP" -out "$TD/chiffre" 2>/dev/null && base64 -w 0 < "$TD/chiffre" > "$TD/phrase-chiffree.b64" \
            || { rm -rf "$TD"; r "chiffrement impossible"; }
        printf 'feu=phrase\nsecret_sha256=%s\nphrase_fichier_sha256=%s\ninscription_commit=%s\ninscription_chemin=%s\n' "$SS" \
            "$(sha256sum < "$FP" | cut -d' ' -f1)" "$CI" "$CH" > "$TD/feu-1-phrase.txt"
        echo "CRIBLE SESSION : empreinte du fichier de la phrase (à inscrire) : $(sha256sum < "$FP" | cut -d' ' -f1)"
        ( ecrire_entree "$BE" phrase-chiffree.b64 "$TD/phrase-chiffree.b64" feu-1-phrase.txt "$TD/feu-1-phrase.txt" ); c=$?
        rm -rf "$TD"
        shred -u "$FP" && echo "CRIBLE SESSION : fichier de la phrase effacé (shred), que la poussée ait réussi ou non"
        exit "$c";;
    feu-mondes)  # feu-mondes BR_SORTIE BR_ENTREE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION
        [ "$#" = 5 ] || r "feu-mondes BR_SORTIE BR_ENTREE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION"
        etat_vaut "$2" "attente du feu 2 (mondes)" || r "la machine n'attend pas le feu des mondes"
        EG=$(lire_sortie "$2" engagement-mondes.json) || r "engagement absent de la sortie"
        EM=$(printf '%s' "$EG" | "$PY" -I -c 'import json,sys;e=json.load(sys.stdin);assert len(e["mondes_sha256"])==20;print(e["fichier_mondes_sha256"], *e["mondes_sha256"])') || r "engagement illisible"
        # shellcheck disable=SC2086
        inscription "$4" "$5" $EM
        TD=$(mktemp -d); printf 'feu=mondes\nfichier_mondes_sha256=%s\ninscription_commit=%s\ninscription_chemin=%s\n' "${EM%% *}" "$4" "$5" > "$TD/f"
        ( ecrire_entree "$3" feu-2-mondes.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    feu-reel)  # feu-reel BR_SORTIE BR_ENTREE GO_CREDITS GO_HORS
        [ "$#" = 5 ] || r "feu-reel BR_SORTIE BR_ENTREE GO_CREDITS GO_HORS"
        etat_vaut "$2" "attente du feu 3 (crible reel)" || r "la machine n'attend pas le feu réel"
        HH=$(lire_sortie "$2" etat.txt | sed -n 's/^fichier_mondes_sha256=//p'); hex "$HH" 64 || r "H illisible sur la sortie"
        TD=$(mktemp -d); printf 'feu=reel\nfichier_mondes_sha256=%s\ngo_credits=%s\ngo_hors=%s\n' "$HH" "$4" "$5" > "$TD/f"
        ( ecrire_entree "$3" feu-3-reel.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    feu-arret)  # feu-arret BR_ENTREE CAUSE
        [ "$#" = 3 ] || r "feu-arret BR_ENTREE CAUSE"
        aide cause "$3" > /dev/null || r "cause : lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », 100 caractères au plus"
        TD=$(mktemp -d); printf 'feu=arret\ncause=%s\n' "$3" > "$TD/f"
        ( ecrire_entree "$2" feu-arret.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    recuperer)  # recuperer BR_SORTIE DESTINATION : copie hors dépôt (remis-au-sous-agent/ non ouvert)
        [ "$#" = 3 ] && branche "$2" && [ ! -e "$3" ] || r "recuperer BR_SORTIE DESTINATION (destination neuve)"
        git -C "$W" fetch -q origin "+refs/heads/$2:refs/remotes/origin/$2" || r "branche de sortie illisible"
        mkdir -p "$3" && git -C "$W" archive "refs/remotes/origin/$2" | tar -x -C "$3" || r "copie impossible"
        echo "CRIBLE SESSION : sortie copiée dans $3 (sommet $(git -C "$W" rev-parse "refs/remotes/origin/$2"))";;
    detruire)  # detruire ETIQUETTE : présence et étiquette seules (jamais le prix) ; inventaire de référence ; commande imprimée
        [ "$#" = 2 ] || r "detruire ETIQUETTE"
        N=$(cat "$ENVP/identifiant.txt") && printf '%s' "$N" | grep -qxE '[1-9][0-9]*' || r "identifiant illisible : aucune destruction, nœud"
        GH=$(sed -n 's/.*-e GO_HORS=\(GO-[0-9-]*\) .*/\1/p' "$ENVP/commande-creation.txt") && [ -n "$GH" ] || r "ligne de GO de la création illisible"
        F=$(lire_prive instances) || r "liste des instances illisible"
        M=$(aide etiquette "$F" "$N" "$2"); c=$?
        if [ "$c" = 0 ] || [ "$c" = 3 ]; then
            if [ -e "$ENVP/ids-avant-destruction.txt" ]; then rm -rf -- "$(dirname "$F")"; echo "CRIBLE SESSION : inventaire de référence déjà écrit (gardé)"
            else aide inventaire "$F" "$ENVP/ids-avant-destruction.txt" --supprimer > /dev/null || r "inventaire avant destruction impossible"; fi
        else rm -rf -- "$(dirname "$F")"; r "$M"; fi
        if [ "$c" = 3 ]; then echo "CRIBLE SESSION : $M"; echo "CRIBLE SESSION PUIS : bash $0 verifier-destruction"; exit 0; fi
        echo "GO_ID=$GH $VASTAI destroy instance $N -y"
        echo "CRIBLE SESSION PUIS (jamais juger la destruction par le code de sortie ; attendre 30 s) : bash $0 verifier-destruction";;
    verifier-destruction)
        N=$(cat "$ENVP/identifiant.txt") || r "identifiant illisible"
        REF="$ENVP/ids-avant-destruction.txt"; [ -e "$REF" ] || REF="$ENVP/ids-apres-creation.txt"
        [ -e "$REF" ] || r "aucun inventaire de référence : nœud, ou preuve par la console du loueur"
        F=$(lire_prive instances) || { echo "CRIBLE SESSION ABSENCE NON PROUVÉE : lecture de la liste en échec"; exit 2; }
        echo "CRIBLE SESSION : référence $(basename "$REF")"
        aide absence "$REF" "$F" "$N" --supprimer; exit $?;;
    *) r "sous-commande inconnue (credit, inventaire, offre-depuis-recherche, commande, comparer, essai-poussee, creation, trouver, relire, ajoute, depense, etat, feu-phrase, feu-mondes, feu-reel, feu-arret, recuperer, detruire, verifier-destruction)";;
esac
