#!/usr/bin/env bash
# ÉCART 2 (R-2450 ; nœud R-2446 ; défaut D2 de la consigne `consigne-developpeur-p3bis-ecart2-v1.md`, `1fd50996…`) :
# contrôle à cinq minutes d'écart, v1, écrit le 2026-11-12 vers 20:50 UTC (heure relevée par `date -u`). Copie de
# `controle_cinq_minutes_p3bis_v2.sh` au commit S (`8f8df8b2…`, `6f921349…`), qui reste dans ce dossier tel quel (R12)
# et que le lanceur d'écart compare toujours à S. Constat (R-2411, R-2446) : l'amorce clone le dépôt deux fois (amorce,
# puis script de l'instance) ; « début » vient vers la création + 224 s, les lignes suivantes plus tard ; joué à + 181 s
# puis à + 290 s, le contrôle d'origine a trouvé des lignes absentes sans aucun signe d'échec, et a arrêté l'instance.
# Seul change le relevé, qui devient une ATTENTE BORNÉE :
#   (a) un relevé (état et journal) toutes les PAS_S = 30 s, de l'appel (au plus tôt la création + 180 s, inchangé) à
#       l'ÉCHÉANCE, la création + ECHEANCE_S = 900 s ; chaque contrôle d'origine rend OK, ATTENTE ou KO ;
#   (b) KO immédiat (arrêt de l'instance par son identifiant, comme l'origine) sur tout SIGNE D'ÉCHEC, liste fermée :
#       état ni « running » ni de démarrage (« created », « loading », « scheduling », absent) ; prix relu au-dessus du
#       plafond ou de l'offre choisie ; machine ou hôte autres que ceux de l'offre ; carte autre qu'« A100 SXM4 » ;
#       étiquette autre ; ligne « AMORCE : … » (échec de l'amorce) ; ligne « AMORCE <date> : commit » d'un autre commit,
#       ou celle de S répétée (redémarrage) ; ligne « AMORCE <date> : fin, code N » (l'amorce a fini dans la fenêtre :
#       le script de l'instance s'est arrêté, sa poussée faite) ; ligne « début : ETUDE=… » autre que l'attendue ; ligne
#       « préenregistrement lu : … » d'un autre nombre de tests ; ligne de carte (« …, N MiB ») qui n'est pas une
#       A100 SXM4 d'au moins 75 Gio ;
#   (c) ATTENTE, jamais un KO avant l'échéance : état illisible ; état de démarrage ; prix, machine, hôte, carte ou
#       étiquette absents ; journal illisible ; une ligne attendue pas encore écrite (AMORCE de S, « début »,
#       « préenregistrement lu », carte, « branche … poussée avant l'installation ») ; au relevé de l'échéance, toute
#       ATTENTE devient un KO (instance arrêtée par son identifiant) ;
#   (d) contrôle appelé après l'échéance : un seul relevé, retard écrit (comme le retard écrit de l'origine) ;
#   (e) journal relu par « logs --tail 20000 » (comme la surveillance) au lieu de 200 lignes : la fenêtre plus longue
#       ne doit faire sortir aucune ligne du relevé ;
#   (f) cet en-tête, l'usage sous le nom neuf ; sorties : controle-5min.txt (en-tête, une ligne par relevé, dernier
#       relevé en entier, verdict), releves.txt, etat.txt et journal-5min.txt du dernier relevé.
# Inchangés : préambule (usage, jetons, dossier neuf, outil, traces, garde de l'identifiant, lecture des traces, nombre
# de tests du texte de S, refus avant la création + 180 s), contrôles eux-mêmes et leurs valeurs, masquage, arrêt par
# l'identifiant après la garde du module commun d'origine, ligne à consigner, codes de sortie.
# Chaîne v2 (2026-11-11 ; règle (a') de P3-bis : R-2296, R-2320 ; consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`) : copie de `controle_cinq_minutes_p3bis_v1.sh`, gardé
# tel quel (R12), noms de la chaîne en v2 ; aucun autre changement.
# Contrôle à cinq minutes de l'instance de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au 2026-11-23 : R-2077), v1. Texte : brouillon 9
# (eb65773f…), « Liste d'arrêt » (« Contrôle à cinq minutes en échec : arrêt de l'instance par son identifiant (R10),
# consigné »). Décliné de docs/procedures/P3-premier-test-v2/controle_cinq_minutes_p3_v1.sh (P3) sous un nom neuf (R12).
# Ce qui change contre P3 : prix plafond 2,10 USD/h ; étude « p3bis », branche calcul/p3bis-reel-vN et étiquette
# p3bis-vN lues dans les traces du lancement ; sur tout KO, l'instance est ARRÊTÉE PAR SON IDENTIFIANT ici (garde du
# module commun : instance créée par le lanceur, hors ARRETEES_TOLEREES ; « vastai stop instance <id> », jamais par
# motif), l'arrêt écrit dans arrets-a-consigner.txt ; aucune destruction.
# (Origine : à jouer entre la création + 180 s et la création + 300 s ; écart 2 : voir (a) à (d) ci-dessus.) Plus tôt
# que la création + 180 s : refus (code 2, rien n'est écrit). Aucun jeton n'est affiché (jetons exigés pour le masquage, R5).
# Ce qui est contrôlé : l'état de l'instance (en marche ; prix au plus PRIX_MAX et au plus celui de l'offre choisie ;
# machine et hôte de l'offre choisie ; carte A100 SXM4 ; étiquette) ; le journal (masqué, gardé) :
# une seule ligne « AMORCE <date> : commit <S> », aucune ligne « AMORCE : », « début : ETUDE=p3bis MODE=reel COMMIT=<S>
# BRANCHE=<branche> », « préenregistrement lu : <N> tests attendus » (N cité une seule fois par le texte de S), une carte
# A100 SXM4 d'au moins 75 Gio, « branche <branche> poussée avant l'installation ».
# Codes : 0 conforme ; 1 au moins un KO (instance arrêtée par son identifiant, ou arrêt en échec écrit) ; 2 usage, jetons
# absents, dossier de sortie existant (R12), traces du lancement incomplètes ou illisibles, identifiant autre que celui
# du lancement, outil de location introuvable, ou contrôle trop tôt.
# Usage : controle_cinq_minutes_p3bis_v2_ecart2_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>
set -uo pipefail
PRIX_MAX=2.10                                    # plan, point 11 (même valeur que le module commun ; contrôles, constantes)
DELAI_MIN_S=180
ECHEANCE_S=900                                   # écart 2 : échéance des relevés, création + 900 s (KO des attentes)
PAS_S=30                                         # écart 2 : un relevé toutes les 30 s jusqu'à l'échéance
ETUDE=p3bis; MODE=reel
ID=${1:-}; T=${2:-}; D=${3:-}
H=$(dirname "$(realpath "$0")")
VERIF=$H/verifications_p3bis_v2.py
[[ "$ID" =~ ^[0-9]+$ && -n "$T" && -n "$D" ]] \
    || { echo "usage : controle_cinq_minutes_p3bis_v2_ecart2_v1.sh <identifiant> <dossier des traces du lancement> <dossier de sortie neuf>"; exit 2; }
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
echo "contrôle à cinq minutes de $ID : création + $ecart s ; commit $S ; branche $BR ; offre choisie $OFFRE ($PRIX_CHOISI USD/h) ; écart 2 : un relevé toutes les $PAS_S s jusqu'à la création + $ECHEANCE_S s (échéance), KO immédiat sur tout signe d'échec" | tee "$R"
[ "$ecart" -lt "$ECHEANCE_S" ] || echo "--  contrôle commencé après l'échéance (création + $ECHEANCE_S s) : un seul relevé (retard écrit)" | tee -a "$R"
A_DEBUT="début : ETUDE=$ETUDE MODE=$MODE COMMIT=$S BRANCHE=$BR"
A_PREREG="préenregistrement lu : $NT tests attendus"
A_BRANCHE="branche $BR poussée avant l'installation"
k=0
while :; do
    k=$((k + 1)); t=$(date -u +%s); off=$((t - CREATION)); final=0
    [ "$off" -ge "$ECHEANCE_S" ] && final=1
    vastai show instance "$ID" --raw 2>&1 | masquer > "$D/etat-releve.json"
    rm -f "$D/journal-5min.txt" "$D/journal-erreur.txt"
    if vastai logs "$ID" --tail 20000 > "$D/journal-brut.txt" 2>&1; then
        masquer < "$D/journal-brut.txt" > "$D/journal-5min.txt"; J="$D/journal-5min.txt"
    else
        masquer < "$D/journal-brut.txt" | head -c 300 > "$D/journal-erreur.txt"; J=-
    fi
    rm -f "$D/journal-brut.txt"
    c=0
    python3 -I - "$D/etat-releve.json" "$J" "$T/offre.json" "$S" "$ETIQUETTE" "$PRIX_CHOISI" "$PRIX_MAX" "$OFFRE" "$final" \
        "$A_DEBUT" "$A_PREREG" "$A_BRANCHE" > "$D/etat.txt" 2>&1 <<'PY' || c=$?
import json, math, re, sys
(etat_f, journal_f, offre_f, S, etiquette, prix_choisi, prix_max, offre, final,
 a_debut, a_prereg, a_branche) = sys.argv[1:13]
prix_choisi, prix_max, final = float(prix_choisi), float(prix_max), final == "1"
L = []
def ok(m): L.append(("OK  ", m))
def att(m): L.append(("ATT ", m))
def ko(m): L.append(("KO  ", m))
def nombre(v): return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
try:
    o = json.load(open(offre_f, encoding="utf-8"))
    assert isinstance(o, dict)
except Exception:
    o = {}
t = open(etat_f, encoding="utf-8", errors="replace").read()
try:
    d = json.loads(t)
    assert isinstance(d, dict)
except Exception:
    d = None
    att("état de l'instance illisible (show instance) : " + t[:120].replace("\n", " "))
if d is not None:
    champs = ("actual_status", "cur_state", "dph_total", "machine_id", "host_id", "gpu_name", "inet_down_cost", "label")
    print("instance : " + " ; ".join(f"{c} {d.get(c)}" for c in champs))
    etat, p, carte, lab = d.get("actual_status"), d.get("dph_total"), d.get("gpu_name"), d.get("label")
    if etat == "running":
        ok(f"instance en marche ({etat})")
    elif etat in (None, "created", "loading", "scheduling"):
        att(f"instance pas encore en marche ({etat})")
    else:
        ko(f"instance ni en marche ni en démarrage ({etat}) : signe d'échec")
    if not nombre(p):
        att(f"prix relu illisible ({p})")
    else:
        (ok if p <= prix_max else ko)(f"prix relu {p} USD/h au plus {prix_max}")
        (ok if p <= prix_choisi + 0.0005 else ko)(f"prix relu {p} USD/h au plus celui de l'offre choisie ({prix_choisi})")
    machine, hote, machine_o, hote_o = d.get("machine_id"), d.get("host_id"), o.get("machine_id"), o.get("host_id")
    m = f"machine {machine} et hôte {hote} de l'offre choisie {offre} ({machine_o}, {hote_o})"
    if machine_o is None:
        ko(m + " : offre choisie illisible")
    elif machine is None or (hote is None and hote_o is not None):
        att(m)
    else:
        (ok if machine == machine_o and hote == hote_o else ko)(m)
    (att if carte is None else ok if carte == "A100 SXM4" else ko)(f"carte {carte} (A100 SXM4 attendue)")
    (att if lab is None else ok if lab == etiquette else ko)(f"étiquette {lab} ({etiquette} attendue)")
if journal_f == "-":
    att("journal de l'instance illisible (logs en échec ; 300 premiers caractères masqués dans journal-erreur.txt)")
else:
    J = open(journal_f, encoding="utf-8", errors="replace").read().split("\n")
    a_s = [x for x in J if re.fullmatch(r"AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[^ ]* : commit " + re.escape(S), x)]
    autres = [x for x in J if re.match(r"AMORCE [0-9]{4}-[0-9]{2}-[0-9]{2}T[^ ]* : commit ", x) and x not in a_s]
    if autres:
        ko(f"journal : ligne « AMORCE <date> : commit » d'un autre commit que {S} ({autres[0][:120]}) : signe d'échec")
    elif len(a_s) > 1:
        ko(f"journal : ligne « AMORCE <date> : commit {S} » répétée (redémarrage) : signe d'échec")
    elif a_s:
        ok(f"journal : une seule ligne « AMORCE <date> : commit {S} »")
    else:
        att(f"journal : ligne « AMORCE <date> : commit {S} » absente")
    e = [x for x in J if x.startswith("AMORCE : ")]
    if e:
        ko(f"journal : échec de l'amorce ({e[0][:120]})")
    else:
        ok("journal : aucune ligne d'échec de l'amorce")
    f = [x for x in J if re.fullmatch(r"AMORCE \S+ : fin, code [0-9]+", x)]
    if f:
        ko(f"journal : fin de l'amorce pendant le contrôle ({f[0][:120]}) : signe d'échec")
    else:
        ok("journal : aucune fin de l'amorce")
    if any(a_debut in x for x in J):
        ok(f"journal : « {a_debut} »")
    elif any("début : ETUDE=" in x for x in J):
        ko(f"journal : ligne « début : ETUDE=… » autre que « {a_debut} » : signe d'échec")
    else:
        att(f"journal : « {a_debut} » absent")
    if any(a_prereg in x for x in J):
        ok(f"journal : « {a_prereg} »")
    elif any("préenregistrement lu : " in x for x in J):
        ko(f"journal : ligne « préenregistrement lu : … » autre que « {a_prereg} » : signe d'échec")
    else:
        att(f"journal : « {a_prereg} » absent")
    a100 = [x for x in J if re.search(r"A100.*SXM4.*, *[0-9]+ MiB *$", x)]
    mib = [x for x in J if re.search(r", *[0-9]+ MiB *$", x)]
    if a100:
        n = int(re.search(r", *([0-9]+) MiB *$", a100[0]).group(1))
        (ok if n >= 76800 else ko)(f"journal : carte « {a100[0][:120]} »" + ("" if n >= 76800 else " : moins de 75 Gio"))
    elif mib:
        ko(f"journal : carte autre qu'une A100 SXM4 (« {mib[0][:120]} ») : signe d'échec")
    else:
        att("journal : carte A100 SXM4 d'au moins 75 Gio absente")
    if any(a_branche in x for x in J):
        ok(f"journal : « {a_branche} »")
    else:
        att(f"journal : « {a_branche} » absent")
if final:
    L = [("KO  ", m + " (à l'échéance)") if q == "ATT " else (q, m) for q, m in L]
for q, m in L:
    print(q + m)
sys.exit(1 if any(q == "KO  " for q, _ in L) else 3 if any(q == "ATT " for q, _ in L) else 0)
PY
    n_ok=$(grep -c '^OK  ' "$D/etat.txt"); n_att=$(grep -c '^ATT ' "$D/etat.txt"); n_ko=$(grep -c '^KO  ' "$D/etat.txt")
    printf 'relevé %s (%s, création + %s s%s) : %s OK, %s en attente, %s KO ; code %s\n' "$k" "$(date -u +%FT%TZ)" "$off" \
        "$( [ "$final" = 1 ] && echo ', échéance' )" "$n_ok" "$n_att" "$n_ko" "$c" | tee -a "$D/releves.txt" "$R"
    [ "$c" = 3 ] && [ "$final" = 0 ] || break
    reste=$((CREATION + ECHEANCE_S - $(date -u +%s))); p=$PAS_S
    [ "$reste" -lt "$p" ] && p=$reste
    [ "$p" -ge 1 ] || p=1
    sleep "$p"
done
cat "$D/etat.txt" >> "$R"; cat "$D/etat.txt"
n_ko=$(grep -c '^KO  ' "$D/etat.txt")
echec=$((echec + n_ko))
[ "$c" = 0 ] || [ "$n_ko" -gt 0 ] || ko "relecture de l'état et du journal impossible (code $c)"
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
