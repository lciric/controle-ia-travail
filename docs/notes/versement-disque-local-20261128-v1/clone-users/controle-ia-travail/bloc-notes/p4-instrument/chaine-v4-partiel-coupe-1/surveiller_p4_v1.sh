#!/usr/bin/env bash
# Surveillance de l'instance de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269), v1, chaîne v2,
# depuis la session de pilotage, sans jamais afficher de jeton. Déclinée de
# docs/procedures/P3-premier-test-v2/surveiller_p3_v1.sh sous un nom neuf (R12) :
#   - plafond écrit ici, en clair : la création plus 9 600 s (texte de P4, Plan d'analyse, point 7, et Liste d'arrêt ;
#     marge avant le KILL de l'amorce, 150 + 5 minutes : 5 minutes moins le démarrage du conteneur) ;
#   - les deux jetons passés à l'instance (HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN, 8 caractères au moins) sont exigés au
#     départ : sans eux, le masquage serait un repli silencieux (R5 ; contre-lecture de la chaîne, CH-16) ;
#   - le journal de l'instance n'est gardé comme dernier relevé que si l'appel a réussi ; chaque ligne nouvelle
#     « AMORCE … » ou « PROGRES … » s'ajoute à un relevé cumulatif, jamais tronqué (progres.txt) ;
#   - l'outil de location doit être trouvé sur le PATH, sinon arrêt immédiat ;
#   - chaîne v2 (RC-depense-06) : identifiant relu dans lancement.txt (ligne « succès : True ; identifiant N ») et égal
#     à l'argument ; création lue dans lancement.txt (ligne « creation N », une seule) ; INTERVALLE entre 10 et 300 s
#     (sinon code 2) ; sommeil borné par le plafond (jamais au-delà de la création + 9 600 s) ; étiquette relue entière
#     au départ (« p4-v1 » exactement, sinon code 2) ;
#   - chaîne v2 (RC-donnees-04, -03) : état masqué avant toute troncature ; réponse illisible écrite par sa longueur et
#     son empreinte courte ; une ligne de journal n'est affichée que si elle a une forme fixe de l'amorce (sinon sa
#     longueur et son empreinte courte) ;
#   - chaîne v2 (RC-depense-01, RC-fidelite-06) : à chaque sortie, la surveillance appelle d'elle-même l'arrêt de
#     l'instance par son identifiant (arreter_p4_v1.sh, rangé à côté de ce script : étiquette relue entière, `vastai
#     stop instance`, état relu arrêté, heure et ligne prête pour registres/arrets.md) ;
#   - chaîne v3 (VC2-depense-02) : étiquette du départ comparée dans Python, exactement (« p4-v1 » suivi d'un saut de
#     ligne : code 2, rien n'est surveillé ni arrêté).
#
#   surveiller_p4_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>
#
# Interroge l'état et le journal toutes les INTERVALLE secondes (120 par défaut ; 10 à 300). Sort en écrivant le motif,
# puis l'issue de l'arrêt sur sa dernière ligne :
#   FIN               ligne « AMORCE … fin, code N » ;
#   ÉCHEC D'AMORCE    ligne « AMORCE : … » (clonage impossible, commit introuvable, dossiers d'un essai précédent) ;
#   REDÉMARRAGE       plus d'une ligne « AMORCE <date> : commit » (le conteneur relance l'amorce à chaque sortie) ;
#   ÉTAT TERMINAL     instance arrêtée ou hors ligne, vue deux fois de suite ;
#   PLAFOND           création plus 9 600 s atteinte.
# Codes : 0 motif écrit, instance arrêtée par son identifiant et relue arrêtée ; 3 motif écrit, arrêt non confirmé
# (arreter_p4_v1.sh en échec ou refus : arrêter l'instance à la main par son identifiant, nœud de Lazar) ; 2 usage,
# jetons absents, dossier de sortie existant (R12), outil ou script d'arrêt introuvable, intervalle hors bornes, traces du
# lancement illisibles ou d'un autre identifiant, étiquette autre (rien n'est surveillé ni arrêté).
set -uo pipefail
PLAFOND_S=9600                                   # création + 9 600 s (texte de P4, Plan d'analyse, point 7)
INTERVALLE_MIN=10                                # bornes de l'intervalle entre deux relevés (RC-depense-06)
INTERVALLE_MAX=300                               # (10 à 300 s)
ETIQUETTE=p4-v1
ID=${1:-}; T=${2:-}; D=${3:-}
INTERVALLE=${INTERVALLE:-120}
ARRETER="$(dirname "$(realpath "$0")")/arreter_p4_v1.sh"
[ $# -eq 3 ] && [[ "$ID" =~ ^[0-9]{6,10}$ && -n "$T" && -n "$D" ]] \
    || { echo "usage : surveiller_p4_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>"; exit 2; }
[[ "$INTERVALLE" =~ ^[0-9]{1,4}$ ]] && [ "$INTERVALLE" -ge "$INTERVALLE_MIN" ] && [ "$INTERVALLE" -le "$INTERVALLE_MAX" ] \
    || { echo "INTERVALLE « $(printf '%s' "$INTERVALLE" | cut -c1-12) » : entre $INTERVALLE_MIN et $INTERVALLE_MAX s attendu : surveillance refusée"; exit 2; }
J_HF=${HF_TOKEN:-}; J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}
[ "${#J_HF}" -ge 8 ] && [ "${#J_GH}" -ge 8 ] \
    || { echo "jetons HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN absents ou trop courts : masquage impossible, surveillance refusée"; exit 2; }
unset J_HF J_GH
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
command -v vastai > /dev/null || { echo "outil de location introuvable sur le PATH : surveillance aveugle, arrêt"; exit 2; }
[ -f "$ARRETER" ] || { echo "script d'arrêt absent ($ARRETER) : surveillance refusée"; exit 2; }
L="$T/lancement.txt"
[ -f "$L" ] || { echo "traces du lancement illisibles ($L absent) : surveillance refusée"; exit 2; }
une() {   # valeur de la seule ligne « <clé> <valeur> » de lancement.txt (vide si absente ou en double)
    local v
    v=$(sed -n "s/^$1 \([^ ]*\)$/\1/p" "$L")
    [ "$(printf '%s\n' "$v" | grep -c .)" = 1 ] && printf '%s' "$v"
}
CREATION=$(une creation)
ID_LU=$(sed -n 's/^succès : True ; identifiant \([0-9][0-9]*\) ; message : .*$/\1/p' "$L")
[[ "$CREATION" =~ ^[0-9]+$ ]] && [ "$(printf '%s\n' "$ID_LU" | grep -c .)" = 1 ] && [ "$ID_LU" = "$ID" ] \
    || { echo "traces du lancement : création ou identifiant illisibles, en double, ou identifiant autre que $ID : surveillance refusée"; exit 2; }
# étiquette relue entière au départ, comparée dans Python (chaîne v3, VC2-depense-02 : la substitution de commande du
# shell retirerait les sauts de ligne finaux) ; code 0 seulement si l'étiquette est exactement « p4-v1 » ; sinon, la forme
# affichée : « (état illisible) », « (sans étiquette) » ou l'étiquette en JSON (sauts de ligne visibles), 40 caractères
if ! LAB=$(vastai show instance "$ID" --raw 2>/dev/null | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
    assert isinstance(d, dict)
except Exception:
    print("(état illisible)"); sys.exit(1)
lab = d.get("label")
if lab == sys.argv[1]:
    sys.exit(0)
print(json.dumps(lab, ensure_ascii=False)[:40] if isinstance(lab, str) else "(sans étiquette)"); sys.exit(1)' "$ETIQUETTE"); then
    echo "instance $ID : étiquette « $LAB » ≠ « $ETIQUETTE » (comparée entière) : surveillance refusée"; exit 2
fi
PLAFOND=$((CREATION + PLAFOND_S))
mkdir -p "$D" && : > "$D/progres.txt" || exit 2
masquer() {
    python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) > 6:
        t = t.replace(v, "***")
sys.stdout.write(t)'
}
etat() {   # masquage d'abord, puis lecture des seuls champs nommés ; une réponse illisible : sa longueur et son empreinte
    vastai show instance "$ID" --raw 2>&1 | masquer | python3 -c '
import hashlib, json, sys
t = sys.stdin.read()
try:
    d = json.loads(t)
    assert isinstance(d, dict)
except Exception:
    print(f"illisible ({len(t)} caractères, empreinte {hashlib.sha256(t.encode()).hexdigest()[:12]})"); raise SystemExit
print(" ".join(f"{k}={str(d.get(k))[:80]}" for k in ("actual_status", "cur_state", "intended_status", "status_msg")))'
}
montrer_ligne() {   # ligne du journal (déjà masquée) : affichée seulement si elle a une forme fixe de l'amorce
    python3 -c '
import hashlib, re, sys
l = sys.argv[1]
fixes = (r"AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:]{8}Z : (commit [0-9a-f]{40}|fin, code [0-9]{1,3})",
         r"AMORCE : (dossiers d.un essai précédent présents \(R12\) : relancer sur une instance neuve|clonage impossible \(jeton GitHub \?\)|commit [0-9a-f]{40} introuvable|poussée impossible)")
print(l if any(re.fullmatch(f, l) for f in fixes) else f"(ligne de {len(l)} caractères, empreinte {hashlib.sha256(l.encode()).hexdigest()[:12]})")' "$1"
}
sortir() {   # $1 ligne du motif, $2 motif court : motif écrit, puis arrêt de l'instance par son identifiant
    local c
    echo "$1" | tee -a "$D/surveillance.txt"
    bash "$ARRETER" "$ID" "$D/arret" "surveillance : $2" > "$D/arret-sortie.txt" 2>&1; c=$?
    sed 's/^/    arrêt | /' "$D/arret-sortie.txt" | cut -c1-240
    if [ "$c" = 0 ]; then
        echo "SURVEILLANCE : $2 ; INSTANCE $ID ARRÊTÉE PAR SON IDENTIFIANT (arreter_p4_v1.sh, code 0 ; ligne prête : $D/arret/ligne-arrets.md)" | tee -a "$D/surveillance.txt"; exit 0
    fi
    echo "SURVEILLANCE : $2 ; ARRÊT NON CONFIRMÉ (arreter_p4_v1.sh, code $c) : arrêter l'instance $ID à la main par son identifiant (R10) ; nœud de Lazar" | tee -a "$D/surveillance.txt"; exit 3
}
terminal=0
echo "surveillance de $ID (étiquette $ETIQUETTE) : création $CREATION, plafond $PLAFOND (création + $PLAFOND_S s), intervalle $INTERVALLE s" > "$D/surveillance.txt"
while true; do
    maintenant=$(date -u +%s)
    e=$(etat)
    echo "$(date -u +%FT%TZ) $e" >> "$D/etats.txt"
    if vastai logs "$ID" --tail 20000 > "$D/journal-tour.txt" 2>&1; then
        masquer < "$D/journal-tour.txt" > "$D/journal-dernier.txt"
        # relevé cumulatif : chaque ligne AMORCE ou PROGRES nouvelle, dans l'ordre d'apparition, jamais retirée
        grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do
            grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"
        done
    else
        echo "$(date -u +%FT%TZ) journal illisible (appel en échec) : dernier relevé gardé" >> "$D/etats.txt"
    fi
    rm -f "$D/journal-tour.txt"
    if grep -qE "^AMORCE .* fin, code [0-9]+" "$D/journal-dernier.txt" 2>/dev/null; then
        sortir "FIN : $(montrer_ligne "$(grep -E '^AMORCE .* fin, code' "$D/journal-dernier.txt" | head -1)")" "FIN"
    fi
    if grep -qE "^AMORCE : " "$D/journal-dernier.txt" 2>/dev/null; then
        sortir "ÉCHEC D'AMORCE : $(montrer_ligne "$(grep -E '^AMORCE : ' "$D/journal-dernier.txt" | head -1)")" "ÉCHEC D'AMORCE"
    fi
    if [ "$(grep -cE '^AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[^ ]* : commit' "$D/progres.txt")" -gt 1 ]; then
        sortir "REDÉMARRAGE : l'amorce a été relancée par le conteneur" "REDÉMARRAGE"
    fi
    case "$e" in
        *"actual_status=exited"*|*"actual_status=offline"*|*"cur_state=stopped"*) terminal=$((terminal + 1)) ;;
        *) terminal=0 ;;
    esac
    if [ "$terminal" -ge 2 ]; then sortir "ÉTAT TERMINAL : $e" "ÉTAT TERMINAL"; fi
    if [ "$maintenant" -ge "$PLAFOND" ]; then sortir "PLAFOND : création + $PLAFOND_S s" "PLAFOND"; fi
    # sommeil borné par le plafond : jamais au-delà de la création + 9 600 s
    reste=$((PLAFOND - $(date -u +%s)))
    attente=$INTERVALLE
    [ "$reste" -lt "$attente" ] && attente=$reste
    [ "$attente" -lt 1 ] && attente=1
    echo "$(date -u +%FT%TZ) sommeil $attente s (reste avant le plafond : $reste s)" >> "$D/etats.txt"
    sleep "$attente"
done
