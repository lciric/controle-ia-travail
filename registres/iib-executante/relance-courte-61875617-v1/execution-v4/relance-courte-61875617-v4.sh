#!/usr/bin/env bash
# Relance courte de 61875617, script v4 (texte de relance, brouillon 5 : A1, A2, L1, L2 de la vérification de la v3) ; v2 inchangé pour la relance, plus :
#  lister   : sur la machine ARRÊTÉE seulement, `execute` de trois commandes fixes (ls -l -R, du), noms et tailles ; jamais rm ;
#  archiver : sur processeur, archive tar des chemins donnés, découpée en morceaux sous 95 Mo, empreinte de chaque morceau et de
#             l'archive entière, réassemblage vérifié ; rien n'est ouvert (tar lit les octets, n'affiche que des noms). : un seul start, relevé du journal du loueur et de l'état toutes les
# 5 s, arrêt par l'identifiant dès que l'amorce a poussé, a renoncé ou a refusé, ou dès que la veille est aveugle, ou à une borne.
# Sous-commandes : decider JOURNAL | jouer | secrets FICHIER... . Commandes du loueur employées : start (une fois), logs,
# show instances, stop (deux fois au plus). Jamais destroy, jamais une autre instance.
# Variables : ID (=61875617), D2 (dossier neuf, existant), VAST (outil de la création), LOC (location_v1.py du commit de lancement).
set -uo pipefail
ID_ATTENDU=61875617
INTOUCHABLES="58936096 58936099 58936100 60988826 61932710"
BR='essai/iib-explo-v6'
HEURE_MAX_S="${HEURE_MAX_S_ESSAI:-1795462800}"     # 2026-11-23T19:40:00Z ; la variable d'essai ne sert qu'aux essais à blanc
PAS_S="${PAS_S:-5}"
BORNE_SCHEDULING_S="${BORNE_SCHEDULING_S:-900}"    # attente de la mise en marche (statut autre que running) : arrêt sans coût
BORNE_RUN_S="${BORNE_RUN_S:-60}"                   # statut running vu, aucune ligne DEMARRAGE >= 2 après 60 s : arrêt
BORNE_ISSUE_S="${BORNE_ISSUE_S:-1080}"             # 18 min après la ligne de démarrage sans issue : arrêt
BORNE_TOTALE_S="${BORNE_TOTALE_S:-2100}"           # 35 min après le start : arrêt
ILLISIBLES_MAX=3                                   # trois relevés du journal illisibles de suite : arrêt

decider() {  # $1 = journal masqué ; une ligne : ATTENDRE | DEMARRAGE | ARRETER ; seules les lignes après le dernier démarrage de rang >= 2
    local apres
    apres=$(awk '$1=="AMORCE" && $2=="IIB" && $4=="DEMARRAGE" && ($5+0)>=2 {buf=""; vu=1; next} vu {buf=buf $0 "\n"} END {if (vu) printf "VU\n%s", buf}' "$1")
    [ -n "$apres" ] || { echo "ATTENDRE : démarrage de rang 2 ou plus non vu"; return 0; }
    case "$apres" in
        *"branche $BR poussée (redémarrage d'un run interrompu)"*) echo "ARRETER : poussée faite";;
        *"poussée impossible"*)                        echo "ARRETER : poussée impossible";;
        *"refus annoncé"*|*"destruction demandée"*|*"refus : "*) echo "ARRETER : refus de l'amorce vu sans ligne de poussée";;
        *"second démarrage après"*)                    echo "ARRETER : chemin inattendu (fin normale ou dépense épuisée)";;
        *"début iib v5"*|*"CLONAGE"*|*"PROGRES "*|*"tests : "*|*"run : "*) echo "ARRETER : calcul inattendu après le démarrage";;
        *) echo "DEMARRAGE : vu, issue non encore écrite";;
    esac; }

etat() {  # $1 = rang, $2 = délai en s (120 par défaut, 30 dans la boucle) ; ligne du lecteur d'inventaire ; brut réduit, supprimé s'il échoue
    local b="$D2/inv-$1.json" r
    ( umask 077; timeout -k 5 "${2:-120}" "$VAST" show instances --raw > "$b" 2>/dev/null </dev/null ) || { rm -f -- "$b"; return 1; }
    r=$(python3 -I -B "$LOC" inventaire "$b" "$D2/inv-$1-champs-filtres.json" iib "$ID_ATTENDU") || { rm -f -- "$b"; return 1; }
    printf '%s\n' "$r"; }

arreter() {  # $1 = motif ; stop par l'identifiant, relecture ; second stop au plus, à 2 min ; jamais destroy
    local c k e
    echo "$(date -u +%FT%TZ) $1 : stop instance $ID_ATTENDU" | tee -a "$D2/veille.txt"
    ( umask 077; timeout -k 5 120 "$VAST" stop instance "$ID_ATTENDU" --raw > "$D2/stop-1.json" 2>&1 </dev/null ); c=$?
    python3 -I -B "$LOC" masquer-en-place "$D2/stop-1.json" >/dev/null || : > "$D2/stop-1.json"
    echo "$(date -u +%FT%TZ) stop 1 : code $c" >> "$D2/veille.txt"
    for k in $(seq 1 20); do
        [ "$PAS_S" = 0 ] || sleep 15
        e=$(etat "arret-$k") || e="illisible"
        echo "$(date -u +%FT%TZ) relecture $k : $e" >> "$D2/veille.txt"
        case "$e" in *"statut=exited"*|*"statut=stopped"*) echo "ARRET CONFIRME ($1)" | tee -a "$D2/veille.txt"; return 0;; esac
        if [ "$k" = 8 ]; then
            ( umask 077; timeout -k 5 120 "$VAST" stop instance "$ID_ATTENDU" --raw > "$D2/stop-2.json" 2>&1 </dev/null ); c=$?
            python3 -I -B "$LOC" masquer-en-place "$D2/stop-2.json" >/dev/null || : > "$D2/stop-2.json"
            echo "$(date -u +%FT%TZ) stop 2 : code $c" >> "$D2/veille.txt"
        fi
    done
    echo "ARRET NON CONFIRME ($1) : aucune autre commande ; mot de la mère" | tee -a "$D2/veille.txt"; return 1; }

jouer() {
    [ "${ID:-}" = "$ID_ATTENDU" ] || { echo "REFUS : ID=${ID:-} ≠ $ID_ATTENDU"; return 2; }
    case " $INTOUCHABLES " in *" $ID "*) echo "REFUS : identifiant intouchable"; return 2;; esac
    [ -d "${D2:-}" ] && [ -x "${VAST:-}" ] && [ -f "${LOC:-}" ] || { echo "REFUS : D2, VAST ou LOC absent"; return 2; }
    [ ! -e "$D2/start-fait" ] || { echo "REFUS : un start a déjà été joué ($(cat "$D2/start-fait")) : jamais de seconde relance"; return 2; }
    [ "$(date +%s)" -le "$HEURE_MAX_S" ] || { echo "REFUS : après 2026-11-23T19:40:00Z (dépense épuisée lue sur le disque à 20:42:05Z)"; return 2; }
    local e; e=$(etat avant-start) || { echo "REFUS : inventaire illisible"; return 2; }
    case "$e" in *"etat=present etiquette=iib-explo-v5 statut=exited"*|*"etat=present etiquette=iib-explo-v5 statut=stopped"*) ;;
        *) echo "REFUS : état avant le start : $e"; return 2;; esac
    echo "$(date -u +%FT%TZ) start unique de $ID_ATTENDU" > "$D2/start-fait"
    local T0 now n=0 c cl L DEM="" RUN_VU="" ILL=0 es RC=0
    T0=$(date +%s)
    ( umask 077; timeout -k 5 120 "$VAST" start instance "$ID_ATTENDU" --raw > "$D2/start.json" 2>&1 </dev/null ); c=$?
    python3 -I -B "$LOC" masquer-en-place "$D2/start.json" >/dev/null || : > "$D2/start.json"
    echo "$(date -u +%FT%TZ) start : code $c" | tee -a "$D2/veille.txt"
    [ "$c" = 0 ] || { arreter "ARRETER : start en code $c"; return 1; }
    while :; do
        n=$((n + 1))
        ( umask 077; timeout -k 5 30 "$VAST" logs "$ID_ATTENDU" --tail 3000 > "$D2/journal-courant.tmp" 2>/dev/null </dev/null ); cl=$?
        if [ "$cl" = 0 ] && [ -s "$D2/journal-courant.tmp" ] && python3 -I -B "$LOC" masquer-en-place "$D2/journal-courant.tmp" >/dev/null; then
            ILL=0; L=$(decider "$D2/journal-courant.tmp")
        else
            : > "$D2/journal-courant.tmp"
            if [ -n "$RUN_VU" ]; then ILL=$((ILL + 1)); fi      # R2 : illisibles comptés seulement une fois la machine vue en marche
            L="ILLISIBLE ($ILL de suite comptés, code $cl)"
        fi
        # R1 : arrêt aussitôt décidé, avant toute lecture d'état
        case "$L" in ARRETER*) echo "$(date -u +%FT%TZ) relevé $n : $L" >> "$D2/veille.txt"; arreter "$L"; RC=$?; break;; esac
        es=$(etat "veille-$n" 30) || es="illisible"
        now=$(date +%s)
        case "$es" in *"statut=running"*) [ -n "$RUN_VU" ] || RUN_VU=$now;; esac
        echo "$(date -u +%FT%TZ) relevé $n : $L ; état : $es" >> "$D2/veille.txt"
        case "$L" in DEMARRAGE*) [ -n "$DEM" ] || DEM=$now;; esac
        if [ "$ILL" -ge "$ILLISIBLES_MAX" ]; then arreter "ARRETER : journal du loueur illisible $ILL fois de suite"; RC=$?; break; fi
        if [ -z "$DEM" ] && [ -n "$RUN_VU" ] && [ $((now - RUN_VU)) -ge "$BORNE_RUN_S" ]; then arreter "ARRETER : en marche depuis $BORNE_RUN_S s sans ligne de démarrage 2"; RC=$?; break; fi
        if [ -z "$DEM" ] && [ -z "$RUN_VU" ] && [ $((now - T0)) -ge "$BORNE_SCHEDULING_S" ]; then arreter "ARRETER : pas en marche après $BORNE_SCHEDULING_S s"; RC=$?; break; fi
        if [ -n "$DEM" ] && [ $((now - DEM)) -ge "$BORNE_ISSUE_S" ]; then arreter "ARRETER : aucune issue $BORNE_ISSUE_S s après le démarrage"; RC=$?; break; fi
        if [ $((now - T0)) -ge "$BORNE_TOTALE_S" ]; then arreter "ARRETER : borne totale de $BORNE_TOTALE_S s"; RC=$?; break; fi
        [ "$PAS_S" = 0 ] || sleep "$PAS_S"
    done
    mv -n "$D2/journal-courant.tmp" "$D2/journal-loueur-fin-masque.txt"
    grep -E "DEMARRAGE|redémarrage d'un run interrompu|poussée|refus|destruction|ERREUR DE CHAÎNE" "$D2/journal-loueur-fin-masque.txt" \
        | grep -vE "PROGRES" | tail -n 40 > "$D2/lignes-d-issue.txt" || true
    return "$RC"; }   # 0 arrêt confirmé ; 1 arrêt non confirmé

secrets() {  # n'imprime qu'un nombre ; valeurs lues par leur nom seulement
    python3 -I -B - "$@" <<'PY'
import os, re, sys
noms = ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY")
vals = [os.environ[k].encode() for k in noms if len(os.environ.get(k, "")) >= 8]
motif = re.compile(rb"ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|hf_[A-Za-z0-9]{30,}|sk-ant-[A-Za-z0-9_-]{20,}")
n = 0
for f in sys.argv[1:]:
    b = open(f, "rb").read()
    n += sum(b.count(v) for v in vals) + len(motif.findall(b))
print(n)
sys.exit(0 if n == 0 else 1)
PY
}

lister() {  # machine arrêtée seulement ; trois commandes fixes ; sorties masquées, noms et tailles seulement
    [ "${ID:-}" = "$ID_ATTENDU" ] || { echo "REFUS : ID=${ID:-} ≠ $ID_ATTENDU"; return 2; }
    [ -d "${D2:-}" ] && [ -x "${VAST:-}" ] && [ -f "${LOC:-}" ] || { echo "REFUS : D2, VAST ou LOC absent"; return 2; }
    local e k c; e=$(etat avant-liste) || { echo "REFUS : inventaire illisible"; return 2; }
    case "$e" in *"etat=present etiquette=iib-explo-v5 statut=exited"*|*"etat=present etiquette=iib-explo-v5 statut=stopped"*) ;;
        *) echo "REFUS : machine non arrêtée ($e) : execute ne vaut que sur une machine arrêtée"; return 2;; esac
    k=0
    for cmd in 'ls -l -R /root/amorce-depot/diag /root/amorce-depot/runs /root/amorce-depot/donnees /root/amorce-depot/traces' \
               'ls -l -a /root /root/iib' \
               'du -k -d 2 /root'; do
        k=$((k + 1))
        case "$cmd" in ls\ *|du\ *) ;; *) echo "REFUS : commande hors de ls et du"; return 2;; esac
        ( umask 077; timeout -k 5 120 "$VAST" execute "$ID_ATTENDU" "$cmd" > "$D2/liste-disque-$k.txt" 2>&1 </dev/null ); c=$?
        if [ "$c" != 0 ]; then      # L2 : un seul nouvel essai si l'outil abandonne (attente d'environ 9 s)
            echo "$(date -u +%FT%TZ) liste $k : code $c, un seul nouvel essai" >> "$D2/liste-disque.txt"
            ( umask 077; timeout -k 5 120 "$VAST" execute "$ID_ATTENDU" "$cmd" > "$D2/liste-disque-$k.txt" 2>&1 </dev/null ); c=$?
        fi
        python3 -I -B "$LOC" masquer-en-place "$D2/liste-disque-$k.txt" >/dev/null || : > "$D2/liste-disque-$k.txt"
        echo "$(date -u +%FT%TZ) liste $k ($cmd) : code $c, $(wc -l < "$D2/liste-disque-$k.txt") lignes" | tee -a "$D2/liste-disque.txt"
    done
    # L1 : état relu après la liste ; en marche (inattendu) : arrêt par l'identifiant
    e=$(etat apres-liste) || e="illisible"
    echo "$(date -u +%FT%TZ) état après la liste : $e" >> "$D2/liste-disque.txt"
    case "$e" in *"statut=exited"*|*"statut=stopped"*) echo "LISTE FAITE, machine toujours arrêtée"; return 0;;
        *"statut=running"*|*"statut=loading"*|*"statut=scheduling"*) arreter "ARRETER : machine en marche après la liste"; return 1;;
        *) echo "ÉTAT APRÈS LA LISTE ILLISIBLE ($e) : mot de la mère"; return 1;; esac; }

archiver() {  # $1 = dossier de sortie neuf ; $2… = chemins relatifs à archiver ; TAILLE_MORCEAU (défaut 95000000 octets)
    local out="$1"; shift; local taille="${TAILLE_MORCEAU:-95000000}"
    mkdir "$out" || { echo "REFUS : $out existe déjà (R12)"; return 2; }
    [ "$#" -gt 0 ] || { echo "REFUS : aucun chemin"; return 2; }
    tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner -cf - -- "$@" 2>"$out/tar.err" | split -b "$taille" -d -a 3 - "$out/archive.tar.part-"
    local ps=("${PIPESTATUS[@]}")
    [ "${ps[0]}" = 0 ] && [ "${ps[1]}" = 0 ] || { echo "ÉCHEC : tar ou split (codes ${ps[*]})"; return 1; }
    (cd "$out" && sha256sum archive.tar.part-* > morceaux.sha256)
    cat "$out"/archive.tar.part-* | sha256sum | cut -d' ' -f1 > "$out/archive-entiere.sha256"   # A2 : calculée sur le réassemblage, sans tâche de fond
    # le réassemblage est comparé octet par octet aux fichiers sources (tar --compare), sans rien afficher de leur contenu
    # l'archive pose mtime 0 et propriétaire 0 (archive reproductible) : seules ces différences-là sont admises ; contenu, taille, absence : échec
    cat "$out"/archive.tar.part-* | tar -df - > "$out/comparaison.txt" 2>&1
    [ "${PIPESTATUS[1]}" -le 1 ] || { echo "ÉCHEC : comparaison impossible (code ${PIPESTATUS[1]})"; return 1; }
    grep -vE ': (Mod time|Uid|Gid|Mode) differs$' "$out/comparaison.txt" > "$out/comparaison-ecarts.txt" || true
    [ ! -s "$out/comparaison-ecarts.txt" ] || { echo "ÉCHEC : réassemblage ≠ fichiers sources ($(wc -l < "$out/comparaison-ecarts.txt") écarts)"; return 1; }
    local grand; grand=$(find "$out" -name 'archive.tar.part-*' -size +"$taille"c | wc -l); [ "$grand" = 0 ] || { echo "ÉCHEC : morceau trop gros"; return 1; }
    cat "$out"/archive.tar.part-* | tar -tvf - > "$out/contenu-noms-tailles.txt"      # A1 : lecture standard, code lu
    [ "${PIPESTATUS[1]}" = 0 ] || { echo "ÉCHEC : liste du contenu"; return 1; }
    [ "$(wc -l < "$out/contenu-noms-tailles.txt")" = "$(find "$@" | wc -l)" ] || { echo "ÉCHEC : entrées ≠ chemins"; return 1; }
    echo "ARCHIVE CONFORME : $(ls "$out"/archive.tar.part-* | wc -l) morceau(x), $(wc -l < "$out/contenu-noms-tailles.txt") entrées, archive $(cat "$out/archive-entiere.sha256")"; }

case "${1:-}" in decider) decider "$2";; jouer) jouer;; secrets) shift; secrets "$@";; lister) lister;; archiver) shift; archiver "$@";;
    *) echo "usage : decider JOURNAL | jouer | secrets FICHIER... | lister | archiver SORTIE CHEMIN..."; exit 2;; esac
