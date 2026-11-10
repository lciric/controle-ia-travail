#!/usr/bin/env bash
# Contrôle à cinq minutes de l'instance de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au 2026-11-23 : R-2077), v1. Texte : brouillon 9
# (eb65773f…), « Liste d'arrêt » (« Contrôle à cinq minutes en échec : arrêt de l'instance par son identifiant (R10),
# consigné »). Décliné de docs/procedures/P3-premier-test-v2/controle_cinq_minutes_p3_v1.sh (P3) sous un nom neuf (R12).
# Ce qui change contre P3 : prix plafond 2,10 USD/h ; étude « p3bis », branche calcul/p3bis-reel-vN et étiquette
# p3bis-vN lues dans les traces du lancement ; sur tout KO, l'instance est ARRÊTÉE PAR SON IDENTIFIANT ici (garde du
# module commun : instance créée par le lanceur, hors ARRETEES_TOLEREES ; « vastai stop instance <id> », jamais par
# motif), l'arrêt écrit dans arrets-a-consigner.txt ; aucune destruction.
# À jouer entre la création + 180 s et la création + 300 s ; plus tôt : refus (code 2, rien n'est écrit) ; plus tard : le
# contrôle se fait et le retard est écrit. Aucun jeton n'est affiché (jetons exigés pour le masquage, R5).
# Ce qui est contrôlé : l'état de l'instance (en marche ; prix au plus PRIX_MAX et au plus celui de l'offre choisie ;
# machine et hôte de l'offre choisie ; carte A100 SXM4 ; étiquette) ; le journal (200 dernières lignes, masqué, gardé) :
# une seule ligne « AMORCE <date> : commit <S> », aucune ligne « AMORCE : », « début : ETUDE=p3bis MODE=reel COMMIT=<S>
# BRANCHE=<branche> », « préenregistrement lu : <N> tests attendus » (N cité une seule fois par le texte de S), une carte
# A100 SXM4 d'au moins 75 Gio, « branche <branche> poussée avant l'installation ».
# Codes : 0 conforme ; 1 au moins un KO (instance arrêtée par son identifiant, ou arrêt en échec écrit) ; 2 usage, jetons
# absents, dossier de sortie existant (R12), traces du lancement incomplètes ou illisibles, identifiant autre que celui
# du lancement, outil de location introuvable, ou contrôle trop tôt.
# Usage : controle_cinq_minutes_p3bis_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>
set -uo pipefail
PRIX_MAX=2.10                                    # plan, point 11 (même valeur que le module commun ; contrôles, constantes)
DELAI_MIN_S=180
DELAI_PREVU_S=300
ETUDE=p3bis; MODE=reel
ID=${1:-}; T=${2:-}; D=${3:-}
H=$(dirname "$(realpath "$0")")
VERIF=$H/verifications_p3bis_v1.py
[[ "$ID" =~ ^[0-9]+$ && -n "$T" && -n "$D" ]] \
    || { echo "usage : controle_cinq_minutes_p3bis_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>"; exit 2; }
J_HF=${HF_TOKEN:-}; J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}
[ "${#J_HF}" -ge 8 ] && [ "${#J_GH}" -ge 8 ] \
    || { echo "jetons HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN absents ou trop courts : masquage impossible, contrôle refusé"; exit 2; }
unset J_HF J_GH
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
command -v vastai > /dev/null || { echo "outil de location introuvable sur le PATH"; exit 2; }
L="$T/lancement.txt"
[ -f "$L" ] && [ -f "$T/prereg-S.md" ] && [ -f "$T/offre.json" ] && [ -f "$VERIF" ] \
    || { echo "traces du lancement incomplètes (lancement.txt, prereg-S.md, offre.json) dans $T, ou module commun absent"; exit 2; }
G=$(python3 -I "$VERIF" identifiant "$ID" "$L" 2>&1) || { echo "identifiant : $(printf '%s\n' "$G" | tail -1)"; exit 2; }
une() {
    local v
    v=$(sed -n "s/^$1 \([^ ]*\)$/\1/p" "$L")
    [ "$(printf '%s\n' "$v" | grep -c .)" = 1 ] && printf '%s' "$v"
}
S=$(une commit); BR=$(une branche); CREATION=$(une creation); ETIQUETTE=$(une etiquette)
CHOISIE=$(sed -n 's/^offre choisie : \([0-9][0-9]*\) (\([0-9.][0-9.]*\) USD\/h).*/\1 \2/p' "$L")
[[ "$S" =~ ^[0-9a-f]{40}$ && "$CREATION" =~ ^[0-9]+$ && "$BR" =~ ^calcul/p3bis-reel-v[123]$ && "$ETIQUETTE" = "p3bis-v${BR##*-v}" ]] \
    && [ "$(printf '%s\n' "$CHOISIE" | grep -c .)" = 1 ] \
    || { echo "traces du lancement illisibles (commit, branche, étiquette, création ou offre choisie)"; exit 2; }
OFFRE=${CHOISIE%% *}; PRIX_CHOISI=${CHOISIE#* }
NT=$(sed -n "s/.*Tests attendus : \`\([0-9][0-9]*\)\`.*/\1/p" "$T/prereg-S.md")
[ "$(grep -c "Tests attendus : \`" "$T/prereg-S.md")" = 1 ] && [[ "$NT" =~ ^[0-9]+$ ]] \
    || { echo "nombre de tests attendus absent ou cité plusieurs fois par le texte de S (prereg-S.md)"; exit 2; }
maintenant=$(date -u +%s); ecart=$((maintenant - CREATION))
[ "$ecart" -ge "$DELAI_MIN_S" ] || { echo "trop tôt : création + $ecart s ; rejouer à la création + $DELAI_MIN_S s au moins"; exit 2; }
mkdir -p "$D" || exit 2
R="$D/controle-5min.txt"
echec=0
ok() { echo "OK  $*" | tee -a "$R"; }
ko() { echo "KO  $*" | tee -a "$R"; echec=$((echec + 1)); }
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
echo "contrôle à cinq minutes de $ID : création + $ecart s ; commit $S ; branche $BR ; offre choisie $OFFRE ($PRIX_CHOISI USD/h)" | tee "$R"
[ "$ecart" -le "$DELAI_PREVU_S" ] || echo "--  contrôle fait après la création + $DELAI_PREVU_S s prévue (retard écrit)" | tee -a "$R"
vastai show instance "$ID" --raw 2>&1 | masquer | python3 -c '
import json, math, sys
offre, prix_choisi, prix_max, chemin_offre, etiquette = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], sys.argv[5]
k = 0
def ok(m): print("OK  " + m)
def ko(m):
    global k; k += 1; print("KO  " + m)
t = sys.stdin.read()
try:
    d = json.loads(t)
    assert isinstance(d, dict)
except Exception:
    ko("état de l instance illisible (show instance) : " + t[:120].replace("\n", " ")); sys.exit(1)
try:
    o = json.load(open(chemin_offre, encoding="utf-8"))
except Exception:
    o = {}
champs = ("actual_status", "cur_state", "dph_total", "machine_id", "host_id", "gpu_name", "inet_down_cost", "label")
print("instance : " + " ; ".join(f"{c} {d.get(c)}" for c in champs))
etat, p, carte, lab = d.get("actual_status"), d.get("dph_total"), d.get("gpu_name"), d.get("label")
machine, hote, machine_o, hote_o = d.get("machine_id"), d.get("host_id"), o.get("machine_id"), o.get("host_id")
nombre = isinstance(p, (int, float)) and not isinstance(p, bool) and math.isfinite(p)
(ok if etat == "running" else ko)(f"instance en marche ({etat})")
(ok if nombre and p <= prix_max else ko)(f"prix relu {p} USD/h au plus {prix_max}")
(ok if nombre and p <= prix_choisi + 0.0005 else ko)(f"prix relu {p} USD/h au plus celui de l offre choisie ({prix_choisi})")
(ok if machine_o is not None and machine == machine_o and hote == hote_o else ko)(
    f"machine {machine} et hôte {hote} de l offre choisie {offre} ({machine_o}, {hote_o})")
(ok if carte == "A100 SXM4" else ko)(f"carte {carte} (A100 SXM4 attendue)")
(ok if lab == etiquette else ko)(f"étiquette {lab} ({etiquette} attendue)")
sys.exit(1 if k else 0)' "$OFFRE" "$PRIX_CHOISI" "$PRIX_MAX" "$T/offre.json" "$ETIQUETTE" > "$D/etat.txt" 2>&1
c=$?
cat "$D/etat.txt" >> "$R"; cat "$D/etat.txt"
n_ko=$(grep -c '^KO  ' "$D/etat.txt")
echec=$((echec + n_ko))
[ "$c" = 0 ] || [ "$n_ko" -gt 0 ] || ko "relecture de l'état impossible (code $c)"
if vastai logs "$ID" --tail 200 > "$D/journal-brut.txt" 2>&1; then
    masquer < "$D/journal-brut.txt" > "$D/journal-5min.txt"
    rm -f "$D/journal-brut.txt"
    J="$D/journal-5min.txt"
    [ "$(grep -cE "^AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[^ ]* : commit $S\$" "$J")" = 1 ] && ok "journal : une seule ligne « AMORCE <date> : commit $S »" \
        || ko "journal : ligne « AMORCE <date> : commit $S » absente ou répétée (redémarrage ?)"
    grep -qE '^AMORCE : ' "$J" && ko "journal : échec de l'amorce ($(grep -E '^AMORCE : ' "$J" | head -1 | cut -c1-120))" || ok "journal : aucune ligne d'échec de l'amorce"
    grep -qF "début : ETUDE=$ETUDE MODE=$MODE COMMIT=$S BRANCHE=$BR" "$J" && ok "journal : « début : ETUDE=$ETUDE MODE=$MODE COMMIT=$S BRANCHE=$BR »" \
        || ko "journal : « début : ETUDE=$ETUDE MODE=$MODE COMMIT=<S> BRANCHE=$BR » absent"
    grep -qF "préenregistrement lu : $NT tests attendus" "$J" && ok "journal : « préenregistrement lu : $NT tests attendus »" \
        || ko "journal : « préenregistrement lu : $NT tests attendus » absent"
    CARTE=$(grep -E 'A100.*SXM4.*, *[0-9]+ MiB *$' "$J" | head -1)
    MIB=$(printf '%s\n' "$CARTE" | sed -n 's/.*, *\([0-9][0-9]*\) MiB *$/\1/p')
    [ -n "$MIB" ] && [ "$MIB" -ge 76800 ] && ok "journal : carte « $CARTE »" || ko "journal : carte A100 SXM4 d'au moins 75 Gio absente (« $CARTE »)"
    grep -qF "branche $BR poussée avant l'installation" "$J" && ok "journal : « branche $BR poussée avant l'installation »" \
        || ko "journal : « branche $BR poussée avant l'installation » absent"
else
    masquer < "$D/journal-brut.txt" | head -c 300 > "$D/journal-erreur.txt"; rm -f "$D/journal-brut.txt"
    ko "journal de l'instance illisible (logs en échec ; 300 premiers caractères masqués dans journal-erreur.txt)"
fi
if [ "$echec" = 0 ]; then echo "CONTRÔLE À CINQ MINUTES : CONFORME" | tee -a "$R"; exit 0; fi
# arrêt de l'instance par son identifiant (R10), après la garde du module commun ; aucune destruction
ca=0
python3 -I "$VERIF" identifiant "$ID" "$L" > /dev/null 2>&1 || ca=refus
if [ "$ca" = 0 ]; then
    r=$(vastai stop instance "$ID" 2>&1 | masquer) || ca=$?
fi
printf '| %s | P3-bis, GO-2026-11-10-02 | instance %s : contrôle à cinq minutes, %s KO ; arrêt par son identifiant (R10), code %s |\n' \
    "$(date -u +%FT%TZ)" "$ID" "$echec" "$ca" >> "$D/arrets-a-consigner.txt"
if [ "$ca" = 0 ]; then
    echo "CONTRÔLE À CINQ MINUTES : $echec KO ; instance $ID arrêtée par son identifiant (R10) ; nœud de Lazar" | tee -a "$R"
else
    echo "CONTRÔLE À CINQ MINUTES : $echec KO ; ARRÊT DE L'INSTANCE $ID EN ÉCHEC (code $ca) : l'arrêter à la main par son identifiant (R10) ; nœud de Lazar" | tee -a "$R"
fi
exit 1
