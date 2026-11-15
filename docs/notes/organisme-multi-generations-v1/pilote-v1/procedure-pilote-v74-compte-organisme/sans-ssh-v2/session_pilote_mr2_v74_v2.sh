#!/usr/bin/env bash
# Outil de la session qui lance le pilote MR-2 sans ssh — v2 (procédure v12). Aucune commande de ce script ne crée ni ne détruit
# d'instance : il contrôle, lit (lecture seule), écrit les feux de la mère sur la branche d'entrée, et IMPRIME les commandes de
# création et de destruction, que la session joue elle-même sous le préfixe GO_ID (garde de calcul). Sorties de l'outil du loueur
# écrites sous `umask 077` dans un dossier jetable, lues par programme, supprimées aussitôt (la configuration des instances porte
# les clés depuis qu'elles passent par `--env`) : aucune n'est gardée dans $ENVP.
# Variables : W (dépôt de travail, défaut /home/user/controle-ia-travail) ; ENVP (dossier d'envoi hors dépôt, défaut
#   /home/user/pilote-mr2-v74-envoi) ; VASTAI (défaut /home/user/vastai-env/bin/vastai).
# Codes : 0 accepté ; 2 refus (motif sur la sortie standard).
# v2 (procédure v12, vérification de la v11 `43a4347b…`) : `detruire` ne juge que la présence et l'étiquette, jamais le prix (M1),
#   et écrit l'inventaire de référence même si l'instance est déjà absente ; `verifier-destruction` prend en repli
#   ids-apres-creation.txt (M2) ; cause des feux bornée et contrôlée avant toute poussée (M3) ; la commande imprimée lit l'amorce
#   encodée dans un fichier privé (ligne courte) et est écrite dans commande-creation.txt pour `comparer` (m1) ; offre à 0,15 USD/h au
#   plus, échéance à 17 h (m3) ; clé publique de la phrase exigée RSA de 4096 bits (m5) ; fichier de la phrase effacé même si la
#   poussée échoue (m6) ; `essai-poussee` (poussée d'une branche jetable, sans dépense).
set -uo pipefail
ICI="$(cd "$(dirname "$0")" && pwd)"
W="${W:-/home/user/controle-ia-travail}"
ENVP="${ENVP:-/home/user/pilote-mr2-v74-envoi}"
VASTAI="${VASTAI:-/home/user/vastai-env/bin/vastai}"
PY="${PYTHON_SESSION:-python3}"
GO_ID=GO-2026-11-14-14
IMAGE=python:3.13-bookworm
DISQUE=20
DOSSIER_CODE=docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/sans-ssh-v2
r() { echo "PILOTE SESSION REFUS : $*"; exit 2; }
aide() { "$PY" -I -B "$ICI/session_pilote_mr2_v74_v2.py" "$@"; }
hex() { printf '%s' "$1" | LC_ALL=C grep -qxE "[0-9a-f]{$2}"; }
branche() { printf '%s' "$1" | LC_ALL=C grep -qxE 'calcul/[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*' && case "$1" in *..*|*.lock|*/) false;; *) true;; esac; }
lire_prive() {  # $1 = objet de `show` (instances | user) : imprime le chemin d'un fichier privé (umask 077), rien d'autre
    local dl f c
    dl=$(mktemp -d) || return 1
    f="$dl/sortie.json"
    ( umask 077; "$VASTAI" show "$1" --raw < /dev/null > "$f" 2> "$dl/erreur.txt" ); c=$?
    if [ "$c" != 0 ]; then rm -f -- "$f" "$dl/erreur.txt"; rmdir -- "$dl"; echo "lecture de « show $1 » en échec (code $c)" >&2; return 1; fi
    echo "$f"; }
lire_sortie() {  # $1 = branche de sortie ; $2 = fichier : imprime le fichier au sommet de la branche (lecture seule)
    git -C "$W" fetch -q origin "+refs/heads/$1:refs/remotes/origin/$1" 2>/dev/null || return 1
    git -C "$W" show "refs/remotes/origin/$1:$2" 2>/dev/null; }
etat_vaut() {  # $1 = branche de sortie ; $2 = étape attendue (ligne etape= exacte)
    [ "$(lire_sortie "$1" etat.txt | sed -n 's/^etape=//p')" = "$2" ]; }
ecrire_entree() {  # $1 = branche d'entrée ; puis paires NOM FICHIER : commit posé sur le sommet de la branche (s'il existe), poussé, relu
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
    if [ -n "$tip" ]; then c=$(git -C "$W" commit-tree "$arbre" -p "$tip" -m "pilote MR-2 v74 : feu de la mère") || r "commit impossible"
    else c=$(git -C "$W" commit-tree "$arbre" -m "pilote MR-2 v74 : feu de la mère") || r "commit impossible"; fi
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
    credit)
        F=$(lire_prive user) || r "crédit illisible : aucune création"
        aide credit "$F" --supprimer; exit $?;;
    inventaire)  # inventaire NOM : identifiants seuls dans $ENVP/ids-NOM.txt (écrit une fois)
        [ "$#" = 2 ] && printf '%s' "$2" | grep -qxE '[a-z-]+' || r "inventaire NOM"
        F=$(lire_prive instances) || r "liste des instances illisible"
        aide inventaire "$F" "$ENVP/ids-$2.txt" --supprimer; exit $?;;
    offre)  # offre RECHERCHE.json ID
        [ "$#" = 3 ] || r "offre RECHERCHE.json ID"
        aide offre "$2" "$3"; exit $?;;
    commande)  # commande RECHERCHE.json OFFRE COMMIT_LOT COMMIT_PREP COMMIT_MAIN BR_SORTIE BR_ENTREE ETIQUETTE
        [ "$#" = 9 ] || r "commande RECHERCHE.json OFFRE COMMIT_LOT COMMIT_PREP COMMIT_MAIN BR_SORTIE BR_ENTREE ETIQUETTE"
        RECH="$2"; OFFRE="$3"; CL="$4"; CP="$5"; CM="$6"; BS="$7"; BE="$8"; ETIQ="$9"
        printf '%s' "$OFFRE" | LC_ALL=C grep -qxE '[1-9][0-9]*' || r "identifiant d'offre illisible"
        printf '%s' "$ETIQ" | LC_ALL=C grep -qxE 'pilote-mr2-v74-[0-9]{8}' || r "étiquette illisible (pilote-mr2-v74-AAAAMMJJ)"
        for c in "$CL" "$CP" "$CM"; do hex "$c" 40 || r "commit illisible (40 hex)"; git -C "$W" cat-file -e "$c^{commit}" 2>/dev/null || r "commit $c absent de $W"; done
        branche "$BS" && branche "$BE" && [ "$BS" != "$BE" ] || r "branches de sortie et d'entrée : calcul/…, distinctes"
        for v in CONTROLE_IA_GITHUB_TOKEN_2 RR_ANTHROPIC_API_KEY_RIGAUD GEMINI_API_KEY OPENAI_API_KEY; do
            printf '%s' "${!v:-}" | LC_ALL=C grep -qxE '[A-Za-z0-9_-]{8,}' || r "$v absente ou de forme illisible pour --env (nom seul)"; done
        P=$(aide offre "$RECH" "$OFFRE") || r "$P"
        PRIX=$(printf '%s' "$P" | sed -n 's/^offre [0-9]* conforme : \([0-9.]*\) USD\/h.*$/\1/p')
        [ -n "$PRIX" ] || r "prix de l'offre illisible"
        for f in amorce_pilote_mr2_v74_v2.sh machine_pilote_mr2_v74_v2.sh machine_pilote_mr2_v74_v2.py; do
            git -C "$W" show "$CL:$DOSSIER_CODE/$f" > /dev/null 2>&1 || r "$f absent du commit $CL"; done
        git -C "$W" show "$CL:$DOSSIER_CODE/amorce_pilote_mr2_v74_v2.sh" | cmp -s - "$ICI/amorce_pilote_mr2_v74_v2.sh" || r "amorce du commit ≠ celle de ce dossier"
        SH=$(git -C "$W" show "$CL:$DOSSIER_CODE/machine_pilote_mr2_v74_v2.sh" | sha256sum | cut -d' ' -f1)
        AH=$(git -C "$W" show "$CL:$DOSSIER_CODE/machine_pilote_mr2_v74_v2.py" | sha256sum | cut -d' ' -f1)
        git -C "$W" show "$CM:registres/go.md" | grep -q '^| GO-2026-11-14-14 ' || r "ligne GO-2026-11-14-14 absente de registres/go.md au commit de main"
        for b in "$BS" "$BE"; do
            git -C "$W" ls-remote --exit-code origin "refs/heads/$b" > /dev/null 2>&1; c=$?
            [ "$c" = 2 ] || r "branche $b présente sur le dépôt distant (R12) ou dépôt injoignable (code $c)"; done
        ECH=$(aide echeance "$(date +%s)" "$PRIX") || r "$ECH"
        RAC=$(mktemp -d) || r "dossier jetable impossible"
        AMORCE_ESSAI=1 AMORCE_ARGUMENTS_SEULS=1 RACINE_AMORCE="$RAC" COMMIT_LOT="$CL" COMMIT_PREP="$CP" COMMIT_MAIN="$CM" BR_SORTIE="$BS" \
            BR_ENTREE="$BE" ECHEANCE_UTC_S="$ECH" GO_ID="$GO_ID" SCRIPT_SHA256="$SH" AIDE_SHA256="$AH" GH_TOKEN=factice-00000000 \
            RR_ANTHROPIC_API_KEY_RIGAUD=factice-00000000 GEMINI_API_KEY=factice-00000000 OPENAI_API_KEY=factice-00000000 \
            env -u CONTAINER_ID bash "$ICI/amorce_pilote_mr2_v74_v2.sh" > "$RAC.txt" 2>&1; c=$?
        rmdir "$RAC" 2>/dev/null || { rm -f "$RAC.txt"; r "l'amorce en essai des arguments a écrit dans le dossier jetable"; }
        [ "$c" = 0 ] || { cat "$RAC.txt"; rm -f "$RAC.txt"; r "arguments refusés par l'amorce"; }
        rm -f "$RAC.txt"
        [ -e "$ENVP/echeance.txt" ] || date -u -d "@$ECH" +%FT%TZ > "$ENVP/echeance.txt"
        [ "$(cat "$ENVP/echeance.txt")" = "$(date -u -d "@$ECH" +%FT%TZ)" ] || r "echeance.txt existe déjà avec une autre échéance : commande déjà imprimée ; ne pas créer deux fois"
        ( umask 077; base64 -w 0 < "$ICI/amorce_pilote_mr2_v74_v2.sh" > "$ENVP/amorce-v2.b64.neuf" ) || r "amorce illisible"
        if [ -e "$ENVP/amorce-v2.b64" ]; then cmp -s "$ENVP/amorce-v2.b64.neuf" "$ENVP/amorce-v2.b64" || { rm -f "$ENVP/amorce-v2.b64.neuf"; r "amorce-v2.b64 existe avec un autre contenu"; }; rm -f "$ENVP/amorce-v2.b64.neuf"
        else mv "$ENVP/amorce-v2.b64.neuf" "$ENVP/amorce-v2.b64"; fi
        L1="GH_TOKEN=\"\$CONTROLE_IA_GITHUB_TOKEN_2\"; ENVP=$ENVP; umask 077"
        L2="GO_ID=$GO_ID $VASTAI create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT_LOT=$CL -e COMMIT_PREP=$CP -e COMMIT_MAIN=$CM -e BR_SORTIE=$BS -e BR_ENTREE=$BE -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GO_ID -e SCRIPT_SHA256=$SH -e AIDE_SHA256=$AH -e GH_TOKEN=\$GH_TOKEN -e RR_ANTHROPIC_API_KEY_RIGAUD=\$RR_ANTHROPIC_API_KEY_RIGAUD -e GEMINI_API_KEY=\$GEMINI_API_KEY -e OPENAI_API_KEY=\$OPENAI_API_KEY\" --entrypoint bash --args -c \"echo \$(cat \"\$ENVP/amorce-v2.b64\") | base64 -d > /root/amorce_pilote_mr2_v74_v2.sh && bash /root/amorce_pilote_mr2_v74_v2.sh\" > \"\$ENVP/creation.json\"; echo \"code=\$?\""
        printf '%s\n%s\n' "$L1" "$L2" > "$ENVP/commande-creation.txt"
        echo "PILOTE SESSION : offre $OFFRE à $PRIX USD/h ; échéance de la minuterie $(date -u -d "@$ECH" +%FT%TZ) ; amorce $(sha256sum < "$ICI/amorce_pilote_mr2_v74_v2.sh" | cut -c1-16), programme ${SH:0:16}, aide ${AH:0:16}"
        echo "PILOTE SESSION COMMANDE (deux lignes, une seule commande ; la seconde commence par GO_ID= ; sortie sous umask 077 ; écrites aussi dans $ENVP/commande-creation.txt, pour comparer) :"
        printf '%s\n%s\n' "$L1" "$L2"
        exit 0;;
    comparer)  # comparer FICHIER : les lignes que la session va jouer, égales à l'octet à celles imprimées par `commande`
        [ "$#" = 2 ] || r "comparer FICHIER"
        [ -f "$ENVP/commande-creation.txt" ] || r "aucune commande imprimée"
        cmp -s "$2" "$ENVP/commande-creation.txt" || r "lignes différentes de la commande imprimée : ne pas jouer"
        echo "PILOTE SESSION : lignes égales à l'octet à la commande imprimée";;
    essai-poussee)  # essai-poussee BRANCHE : poussée par le chemin des feux sur une branche jetable (jamais celles du pilote)
        [ "$#" = 2 ] || r "essai-poussee BRANCHE"
        case "$2" in calcul/pilote-mr2-v74-*) r "jamais une branche du pilote";; esac
        TD=$(mktemp -d); printf 'essai de poussée de la session (aucun feu), %s\n' "$(date -u +%FT%TZ)" > "$TD/f"
        ( ecrire_entree "$2" essai-poussee.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    creation)  # identifiant lu dans creation.json (supprimé), écrit une fois dans $ENVP/identifiant.txt
        [ ! -e "$ENVP/identifiant.txt" ] || r "identifiant.txt existe déjà : jamais récrit"
        N=$(aide creation "$ENVP/creation.json" --supprimer) || r "$N"
        echo "$N" > "$ENVP/identifiant.txt"; echo "ID=$N";;
    trouver)  # trouver ETIQUETTE : repli sans new_contract lisible
        [ "$#" = 2 ] || r "trouver ETIQUETTE"; [ ! -e "$ENVP/identifiant.txt" ] || r "identifiant.txt existe déjà"
        F=$(lire_prive instances) || r "liste des instances illisible"
        N=$(aide trouver "$F" "$2" --supprimer) || r "$N"
        echo "$N" > "$ENVP/identifiant.txt"; echo "ID=$N";;
    relire)  # relire ETIQUETTE
        [ "$#" = 2 ] || r "relire ETIQUETTE"
        N=$(cat "$ENVP/identifiant.txt") && printf '%s' "$N" | grep -qxE '[1-9][0-9]*' || r "identifiant illisible"
        F=$(lire_prive instances) || r "liste des instances illisible"
        aide relire "$F" "$N" "$2" --supprimer; exit $?;;
    ajoute)  # après la création : seule instance ajoutée, égale à l'identifiant
        aide ajoute "$ENVP/ids-avant.txt" "$ENVP/ids-apres-creation.txt" "$(cat "$ENVP/identifiant.txt")"; exit $?;;
    etat)  # etat BR_SORTIE : état et fin du journal de la machine (rien d'autre n'est ouvert)
        [ "$#" = 2 ] && branche "$2" || r "etat BR_SORTIE"
        lire_sortie "$2" etat.txt || { echo "PILOTE SESSION : branche de sortie pas encore poussée"; exit 2; }
        echo "--- journal de la machine (fin)"; lire_sortie "$2" journal-machine.txt | tail -n 12; exit 0;;
    feu-phrase)  # feu-phrase BR_SORTIE BR_ENTREE FICHIER_PHRASE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION
        [ "$#" = 6 ] || r "feu-phrase BR_SORTIE BR_ENTREE FICHIER_PHRASE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION"
        BS="$2"; BE="$3"; FP="$4"; CI="$5"; CH="$6"
        etat_vaut "$BS" "attente du feu 1 (phrase)" || r "la machine n'attend pas la phrase (etat etape=…)"
        SS=$(lire_sortie "$BS" secret-sha256.txt | sed -n 's/^secret_sha256=//p'); hex "$SS" 64 || r "empreinte du secret illisible sur la sortie"
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
        lire_sortie "$BS" cle-publique-phrase.pem > "$TD/cle.pem" && [ -s "$TD/cle.pem" ] || { rm -rf "$TD"; r "clé publique absente de la sortie"; }
        [ "$(openssl pkey -pubin -in "$TD/cle.pem" -outform DER 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(lire_sortie "$BS" cle-publique-phrase.empreinte)" ] \
            || { rm -rf "$TD"; r "clé publique ≠ son empreinte poussée"; }
        openssl pkey -pubin -in "$TD/cle.pem" -text_pub -noout 2>/dev/null > "$TD/cle.txt"
        grep -qx 'Public-Key: (4096 bit)' "$TD/cle.txt" && grep -q '^Modulus:' "$TD/cle.txt" || { rm -rf "$TD"; r "clé publique de la phrase : RSA de 4096 bits exigée"; }
        openssl pkeyutl -encrypt -pubin -inkey "$TD/cle.pem" -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 \
            -pkeyopt rsa_mgf1_md:sha256 -in "$FP" -out "$TD/chiffre" 2>/dev/null && base64 -w 0 < "$TD/chiffre" > "$TD/phrase-chiffree.b64" \
            || { rm -rf "$TD"; r "chiffrement impossible"; }
        printf 'feu=phrase\nsecret_sha256=%s\nphrase_fichier_sha256=%s\ninscription_commit=%s\ninscription_chemin=%s\n' "$SS" \
            "$(sha256sum < "$FP" | cut -d' ' -f1)" "$CI" "$CH" > "$TD/feu-1-phrase.txt"
        echo "PILOTE SESSION : empreinte du fichier de la phrase (à inscrire) : $(sha256sum < "$FP" | cut -d' ' -f1)"
        ( ecrire_entree "$BE" phrase-chiffree.b64 "$TD/phrase-chiffree.b64" feu-1-phrase.txt "$TD/feu-1-phrase.txt" ); c=$?
        rm -rf "$TD"
        shred -u "$FP" && echo "PILOTE SESSION : fichier de la phrase effacé (shred), que la poussée ait réussi ou non"
        [ "$c" = 0 ] || exit 2
        exit 0;;
    feu-mondes)  # feu-mondes BR_SORTIE BR_ENTREE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION
        [ "$#" = 5 ] || r "feu-mondes BR_SORTIE BR_ENTREE COMMIT_INSCRIPTION CHEMIN_INSCRIPTION"
        etat_vaut "$2" "attente du feu 2 (mondes)" || r "la machine n'attend pas le feu des mondes"
        EG=$(lire_sortie "$2" engagement-mondes.json) || r "engagement absent de la sortie"
        EM=$(printf '%s' "$EG" | "$PY" -I -c 'import json,sys;e=json.load(sys.stdin);print(e["fichier_mondes_sha256"], *e["mondes_sha256"])') || r "engagement illisible"
        # shellcheck disable=SC2086
        inscription "$4" "$5" $EM
        TD=$(mktemp -d); printf 'feu=mondes\nfichier_mondes_sha256=%s\ninscription_commit=%s\ninscription_chemin=%s\n' "${EM%% *}" "$4" "$5" > "$TD/f"
        ( ecrire_entree "$3" feu-2-mondes.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    feu-reel)  # feu-reel BR_SORTIE BR_ENTREE
        [ "$#" = 3 ] || r "feu-reel BR_SORTIE BR_ENTREE"
        etat_vaut "$2" "attente du feu 3 (pilote reel)" || r "la machine n'attend pas le feu réel"
        HH=$(lire_sortie "$2" etat.txt | sed -n 's/^fichier_mondes_sha256=//p'); hex "$HH" 64 || r "H illisible sur la sortie"
        TD=$(mktemp -d); printf 'feu=reel\nfichier_mondes_sha256=%s\ngo_pi1=GO-2026-11-14-13\ngo_pi2=GO-2026-11-14-14\n' "$HH" > "$TD/f"
        ( ecrire_entree "$3" feu-3-reel.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    feu-relance)  # feu-relance BR_SORTIE BR_ENTREE CAUSE
        [ "$#" = 4 ] || r "feu-relance BR_SORTIE BR_ENTREE CAUSE"
        etat_vaut "$2" "attente du feu de relance (reel-2)" || r "la machine n'attend pas de relance"
        HH=$(lire_sortie "$2" etat.txt | sed -n 's/^fichier_mondes_sha256=//p'); hex "$HH" 64 || r "H illisible sur la sortie"
        aide cause "$4" > /dev/null || r "cause : lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », 100 caractères au plus ; rien n'est poussé"
        TD=$(mktemp -d); printf 'feu=relance-reel-2\nfichier_mondes_sha256=%s\ncause=%s\n' "$HH" "$4" > "$TD/f"
        ( ecrire_entree "$3" feu-relance-reel-2.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    feu-arret)  # feu-arret BR_ENTREE CAUSE
        [ "$#" = 3 ] || r "feu-arret BR_ENTREE CAUSE"
        aide cause "$3" > /dev/null || r "cause : lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », 100 caractères au plus ; rien n'est poussé"
        TD=$(mktemp -d); printf 'feu=arret\ncause=%s\n' "$3" > "$TD/f"
        ( ecrire_entree "$2" feu-arret.txt "$TD/f" ); c=$?; rm -rf "$TD"; exit "$c";;
    recuperer)  # recuperer BR_SORTIE DESTINATION : copie de la branche de sortie hors dépôt (remis-au-sous-agent/ non ouvert)
        [ "$#" = 3 ] && branche "$2" || r "recuperer BR_SORTIE DESTINATION"
        [ ! -e "$3" ] || r "destination existante"
        git -C "$W" fetch -q origin "+refs/heads/$2:refs/remotes/origin/$2" || r "branche de sortie illisible"
        mkdir -p "$3" && git -C "$W" archive "refs/remotes/origin/$2" | tar -x -C "$3" || r "copie impossible"
        echo "PILOTE SESSION : sortie copiée dans $3 (sommet $(git -C "$W" rev-parse "refs/remotes/origin/$2"))";;
    detruire)  # detruire ETIQUETTE : présence et étiquette seules (jamais le prix, M1) ; inventaire de référence ; commande imprimée
        [ "$#" = 2 ] || r "detruire ETIQUETTE"
        N=$(cat "$ENVP/identifiant.txt") && printf '%s' "$N" | grep -qxE '[1-9][0-9]*' || r "identifiant illisible : aucune destruction, nœud"
        F=$(lire_prive instances) || r "liste des instances illisible"
        M=$(aide etiquette "$F" "$N" "$2"); c=$?
        if [ "$c" = 0 ] || [ "$c" = 3 ]; then
            if [ -e "$ENVP/ids-avant-destruction.txt" ]; then rm -rf -- "$(dirname "$F")"; echo "PILOTE SESSION : inventaire de référence déjà écrit (gardé)"
            else aide inventaire "$F" "$ENVP/ids-avant-destruction.txt" --supprimer > /dev/null || r "inventaire avant destruction impossible"; fi
        else rm -rf -- "$(dirname "$F")"; r "$M"; fi
        if [ "$c" = 3 ]; then echo "PILOTE SESSION : $M"; echo "PILOTE SESSION PUIS : bash $0 verifier-destruction"; exit 0; fi
        echo "GO_ID=$GO_ID $VASTAI destroy instance $N -y"
        echo "PILOTE SESSION PUIS (jamais juger la destruction par le code de sortie) : bash $0 verifier-destruction";;
    verifier-destruction)  # référence : ids-avant-destruction.txt, sinon ids-apres-creation.txt (M2)
        N=$(cat "$ENVP/identifiant.txt") || r "identifiant illisible"
        REF="$ENVP/ids-avant-destruction.txt"; [ -e "$REF" ] || REF="$ENVP/ids-apres-creation.txt"
        [ -e "$REF" ] || r "aucun inventaire de référence (ni avant destruction ni après création) : nœud, ou preuve par la console du loueur"
        F=$(lire_prive instances) || { echo "PILOTE SESSION ABSENCE NON PROUVÉE : lecture de la liste en échec"; exit 2; }
        echo "PILOTE SESSION : référence $(basename "$REF")"
        aide absence "$REF" "$F" "$N" --supprimer; exit $?;;
    *) r "sous-commande inconnue (credit, inventaire, offre, commande, comparer, essai-poussee, creation, trouver, relire, ajoute, etat, feu-phrase, feu-mondes, feu-reel, feu-relance, feu-arret, recuperer, detruire, verifier-destruction)";;
esac
