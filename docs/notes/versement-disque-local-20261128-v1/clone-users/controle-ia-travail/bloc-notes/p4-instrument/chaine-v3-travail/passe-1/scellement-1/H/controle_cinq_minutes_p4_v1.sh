#!/usr/bin/env bash
# Contrôle à cinq minutes de l'instance de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269), v1,
# chaîne v2, décliné de docs/procedures/P3-premier-test-v2/controle_cinq_minutes_p3_v1.sh sous un nom neuf (R12). Texte
# de P4, Liste d'arrêt : « Contrôle à cinq minutes en échec […] : arrêt de l'instance par son identifiant ».
# À jouer entre la création + 180 s et la création + 300 s (le lanceur écrit ces deux instants dans lancement.txt) ;
# plus tôt : refus (code 2, rien n'est écrit) ; plus tard : le contrôle se fait et le retard est écrit. Aucun jeton
# n'est affiché : les deux jetons passés à l'instance (HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN, 8 caractères au moins)
# sont exigés pour le masquage (R5).
# Ce qui est contrôlé : l'identifiant passé égal à celui de lancement.txt (ligne « succès : True ; identifiant N ») ;
# l'état de l'instance, relu sous forme filtrée (en marche ; prix au plus PRIX_MAX et au plus celui de l'offre choisie ;
# téléchargement au plus TELECHARGEMENT_MAX USD par Go et stockage au plus STOCKAGE_MAX USD de l'heure, relus — chaîne
# v2, RC-fidelite-04 ; machine et hôte de l'offre choisie, offre.json ; carte A100 SXM4 ; étiquette p4-v1) ; le journal
# de l'instance (200 dernières lignes, masqué, gardé dans journal-5min.txt) : une seule ligne « AMORCE <date> : commit
# <S> », aucune ligne « AMORCE : » (échec de l'amorce), « début : ETUDE=p4 MODE=reel COMMIT=<S> BRANCHE=<branche> »,
# « préenregistrement lu : <N> tests attendus » (N cité une seule fois par le texte de S, prereg-S.md des traces), une
# carte A100 SXM4 d'au moins 75 Gio (ligne de nvidia-smi), « branche <branche> poussée avant l'installation ».
# Chaîne v2 (RC-depense-01, RC-fidelite-06) : sur tout KO, ce script appelle de lui-même l'arrêt de l'instance par son
# identifiant (arreter_p4_v1.sh, rangé à côté de ce script : étiquette relue entière, `vastai stop instance`, état relu
# arrêté, heure et ligne prête pour registres/arrets.md), puis la session soumet le nœud à Lazar (un prix relu au-dessus
# de celui de l'offre choisie demande de recalculer la borne de dépense de l'étape à ce prix). Chaîne v2
# (RC-donnees-03, -04) : masquage avant toute troncature ; aucune ligne de journal brute affichée (formes fixes de
# l'amorce seulement ; sinon longueur et empreinte courte) ; carte affichée par ses seules valeurs lues.
# Codes : 0 conforme ; 1 au moins un KO, instance arrêtée par son identifiant et relue arrêtée ; 3 au moins un KO, arrêt
# non confirmé (arreter_p4_v1.sh en échec ou refus : arrêter à la main par son identifiant, nœud de Lazar) ; 2 usage,
# jetons absents, dossier de sortie existant (R12), traces du lancement incomplètes, illisibles ou d'un autre
# identifiant, outil de location ou script d'arrêt introuvable, ou contrôle trop tôt (rien n'est arrêté).
# Usage : controle_cinq_minutes_p4_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>
set -uo pipefail
PRIX_MAX=1.30                                    # devis de la phase 0 (même valeur que le lanceur ; bloc 9 des contrôles)
TELECHARGEMENT_MAX=0.05                          # téléchargement relu, USD par Go (même valeur que le lanceur)
STOCKAGE_MAX=0.03                                # stockage relu, USD de l'heure (même valeur que le lanceur)
DELAI_MIN_S=180                                  # pas avant la création + 180 s
DELAI_PREVU_S=300                                # au plus tard prévu : la création + 300 s
ETUDE=p4; MODE=reel; ETIQUETTE=p4-v1
ID=${1:-}; T=${2:-}; D=${3:-}
ARRETER="$(dirname "$(realpath "$0")")/arreter_p4_v1.sh"
[ $# -eq 3 ] && [[ "$ID" =~ ^[0-9]{6,10}$ && -n "$T" && -n "$D" ]] \
    || { echo "usage : controle_cinq_minutes_p4_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>"; exit 2; }
J_HF=${HF_TOKEN:-}; J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}
[ "${#J_HF}" -ge 8 ] && [ "${#J_GH}" -ge 8 ] \
    || { echo "jetons HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN absents ou trop courts : masquage impossible, contrôle refusé"; exit 2; }
unset J_HF J_GH
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
command -v vastai > /dev/null || { echo "outil de location introuvable sur le PATH"; exit 2; }
[ -f "$ARRETER" ] || { echo "script d'arrêt absent ($ARRETER) : contrôle refusé"; exit 2; }
L="$T/lancement.txt"
[ -f "$L" ] && [ -f "$T/prereg-S.md" ] && [ -f "$T/offre.json" ] \
    || { echo "traces du lancement incomplètes (lancement.txt, prereg-S.md, offre.json) dans $T"; exit 2; }
une() {   # valeur de la seule ligne « <clé> <valeur> » de lancement.txt (vide si absente ou en double)
    local v
    v=$(sed -n "s/^$1 \([^ ]*\)$/\1/p" "$L")
    [ "$(printf '%s\n' "$v" | grep -c .)" = 1 ] && printf '%s' "$v"
}
S=$(une commit); BR=$(une branche); CREATION=$(une creation)
CHOISIE=$(sed -n 's/^offre choisie : \([0-9][0-9]*\) (\([0-9.][0-9.]*\) USD\/h).*/\1 \2/p' "$L")
ID_LU=$(sed -n 's/^succès : True ; identifiant \([0-9][0-9]*\) ; message : .*$/\1/p' "$L")
[[ "$S" =~ ^[0-9a-f]{40}$ && "$CREATION" =~ ^[0-9]+$ && "$BR" =~ ^calcul/p4-reel-v[0-9]+$ ]] \
    && [ "$(printf '%s\n' "$CHOISIE" | grep -c .)" = 1 ] \
    || { echo "traces du lancement illisibles (commit, branche, création ou offre choisie)"; exit 2; }
[ "$(printf '%s\n' "$ID_LU" | grep -c .)" = 1 ] && [ "$ID_LU" = "$ID" ] \
    || { echo "traces du lancement : identifiant de la création absent, en double ou autre que $ID : contrôle refusé"; exit 2; }
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
montrer_ligne() {   # ligne du journal (déjà masquée) : affichée seulement si elle a une forme fixe de l'amorce
    python3 -c '
import hashlib, re, sys
l = sys.argv[1]
fixes = (r"AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:]{8}Z : (commit [0-9a-f]{40}|fin, code [0-9]{1,3})",
         r"AMORCE : (dossiers d.un essai précédent présents \(R12\) : relancer sur une instance neuve|clonage impossible \(jeton GitHub \?\)|commit [0-9a-f]{40} introuvable|poussée impossible)")
print(l if any(re.fullmatch(f, l) for f in fixes) else f"(ligne de {len(l)} caractères, empreinte {hashlib.sha256(l.encode()).hexdigest()[:12]})")' "$1"
}
echo "contrôle à cinq minutes de $ID : création + $ecart s ; commit $S ; branche $BR ; offre choisie $OFFRE ($PRIX_CHOISI USD/h)" | tee "$R"
[ "$ecart" -le "$DELAI_PREVU_S" ] || echo "--  contrôle fait après la création + $DELAI_PREVU_S s prévue (retard écrit)" | tee -a "$R"
# état de l'instance, sous forme filtrée : masqué d'abord, puis seuls les champs nommés sont lus et écrits
vastai show instance "$ID" --raw 2>&1 | masquer | python3 -c '
import hashlib, json, math, sys
offre, prix_choisi, prix_max, chemin_offre, etiquette = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], sys.argv[5]
tel_max, sto_max = float(sys.argv[6]), float(sys.argv[7])
k = 0
def ok(m): print("OK  " + m)
def ko(m):
    global k; k += 1; print("KO  " + m)
t = sys.stdin.read()
try:
    d = json.loads(t)
    assert isinstance(d, dict)
except Exception:
    ko(f"état de l instance illisible (vastai show instance) : {len(t)} caractères, empreinte {hashlib.sha256(t.encode()).hexdigest()[:12]}"); sys.exit(1)
try:
    o = json.load(open(chemin_offre, encoding="utf-8"))
except Exception:
    o = {}
champs = ("actual_status", "cur_state", "dph_total", "machine_id", "host_id", "gpu_name", "inet_down_cost", "storage_total_cost", "label")
print("instance : " + " ; ".join(f"{c} {str(d.get(c))[:60]}" for c in champs))
etat, p, carte, lab = d.get("actual_status"), d.get("dph_total"), d.get("gpu_name"), d.get("label")
tel, sto = d.get("inet_down_cost"), d.get("storage_total_cost")
machine, hote, machine_o, hote_o = d.get("machine_id"), d.get("host_id"), o.get("machine_id"), o.get("host_id")
def nombre(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
(ok if etat == "running" else ko)(f"instance en marche ({etat})")
(ok if nombre(p) and p <= prix_max else ko)(f"prix relu {p} USD/h au plus {prix_max}")
(ok if nombre(p) and p <= prix_choisi + 0.0005 else ko)(
    f"prix relu {p} USD/h au plus celui de l offre choisie ({prix_choisi}) ; sinon recalculer la borne de dépense de l étape à ce prix (nœud)")
(ok if nombre(tel) and 0 <= tel <= tel_max else ko)(f"téléchargement relu {tel} USD/Go au plus {tel_max}")
(ok if nombre(sto) and 0 <= sto <= sto_max else ko)(f"stockage relu {sto} USD/h au plus {sto_max}")
(ok if machine_o is not None and machine == machine_o and hote == hote_o else ko)(
    f"machine {machine} et hôte {hote} de l offre choisie {offre} ({machine_o}, {hote_o})")
(ok if carte == "A100 SXM4" else ko)(f"carte {carte} (A100 SXM4 attendue)")
(ok if lab == etiquette else ko)(f"étiquette {str(lab)[:40]} ({etiquette} attendue, comparée entière)")
sys.exit(1 if k else 0)' "$OFFRE" "$PRIX_CHOISI" "$PRIX_MAX" "$T/offre.json" "$ETIQUETTE" "$TELECHARGEMENT_MAX" "$STOCKAGE_MAX" > "$D/etat.txt" 2>&1
c=$?
cat "$D/etat.txt" >> "$R"; cat "$D/etat.txt"
n_ko=$(grep -c '^KO  ' "$D/etat.txt")
echec=$((echec + n_ko))
[ "$c" = 0 ] || [ "$n_ko" -gt 0 ] || ko "relecture de l'état impossible (code $c)"
# journal de l'instance : 200 dernières lignes, masquées, gardées
if vastai logs "$ID" --tail 200 > "$D/journal-brut.txt" 2>&1; then
    masquer < "$D/journal-brut.txt" > "$D/journal-5min.txt"
    rm -f "$D/journal-brut.txt"
    J="$D/journal-5min.txt"
    [ "$(grep -cE "^AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[^ ]* : commit $S\$" "$J")" = 1 ] && ok "journal : une seule ligne « AMORCE <date> : commit $S »" \
        || ko "journal : ligne « AMORCE <date> : commit $S » absente ou répétée (redémarrage ?)"
    grep -qE '^AMORCE : ' "$J" && ko "journal : échec de l'amorce ($(montrer_ligne "$(grep -E '^AMORCE : ' "$J" | head -1)"))" || ok "journal : aucune ligne d'échec de l'amorce"
    grep -qF "début : ETUDE=$ETUDE MODE=$MODE COMMIT=$S BRANCHE=$BR" "$J" && ok "journal : « début : ETUDE=$ETUDE MODE=$MODE COMMIT=$S BRANCHE=$BR »" \
        || ko "journal : « début : ETUDE=$ETUDE MODE=$MODE COMMIT=<S> BRANCHE=$BR » absent"
    grep -qF "préenregistrement lu : $NT tests attendus" "$J" && ok "journal : « préenregistrement lu : $NT tests attendus »" \
        || ko "journal : « préenregistrement lu : $NT tests attendus » absent"
    CARTE=$(grep -E 'A100.*SXM4.*, *[0-9]+ MiB *$' "$J" | head -1)
    MIB=$(printf '%s\n' "$CARTE" | sed -n 's/.*, *\([0-9][0-9]*\) MiB *$/\1/p')
    [ -n "$MIB" ] && [ "$MIB" -ge 76800 ] && ok "journal : carte A100 SXM4 de $MIB MiB" || ko "journal : carte A100 SXM4 d'au moins 75 Gio absente (${MIB:-aucune} MiB lus)"
    grep -qF "branche $BR poussée avant l'installation" "$J" && ok "journal : « branche $BR poussée avant l'installation »" \
        || ko "journal : « branche $BR poussée avant l'installation » absent"
else
    masquer < "$D/journal-brut.txt" | head -c 300 > "$D/journal-erreur.txt"; rm -f "$D/journal-brut.txt"
    ko "journal de l'instance illisible (vastai logs en échec ; 300 premiers caractères masqués dans journal-erreur.txt)"
fi
if [ "$echec" = 0 ]; then echo "CONTRÔLE À CINQ MINUTES : CONFORME" | tee -a "$R"; exit 0; fi
# échec : arrêt de l'instance par son identifiant (R10), par le script d'arrêt
echo "--  $echec KO : arrêt de l'instance $ID par son identifiant (arreter_p4_v1.sh)" | tee -a "$R"
bash "$ARRETER" "$ID" "$D/arret" "contrôle à cinq minutes en échec" > "$D/arret-sortie.txt" 2>&1; ca=$?
sed 's/^/    arrêt | /' "$D/arret-sortie.txt" | cut -c1-240 | tee -a "$R"
if [ "$ca" = 0 ]; then
    echo "CONTRÔLE À CINQ MINUTES : $echec KO ; INSTANCE $ID ARRÊTÉE PAR SON IDENTIFIANT (arreter_p4_v1.sh, code 0) ; nœud de Lazar" | tee -a "$R"; exit 1
fi
echo "CONTRÔLE À CINQ MINUTES : $echec KO ; ARRÊT NON CONFIRMÉ (arreter_p4_v1.sh, code $ca) : arrêter l'instance $ID à la main par son identifiant (R10) ; nœud de Lazar" | tee -a "$R"
exit 3
