P = [
("""#     limite) est réécrite entière, hors du filtre.
# Codes : 0 tout conforme, instance détruite ; 4 traces seules conformes, instance détruite ; 1 au moins un contrôle en
# échec (destruction comprise), instance gardée : nœud de Lazar ; 2 usage, traces du lancement d'un autre S ou d'une
# autre instance, place disque insuffisante, ou clonage impossible (rien n'est détruit ; pour ces deux derniers, état de
# l'instance et heure limite de destruction écrits).
# Usage : recuperation_p4_v1.sh S IDENTIFIANT DOSSIER_TRACES_DU_LANCEMENT DOSSIER_NEUF
set -uo pipefail
SOI=$(realpath "$0")
[ $# -eq 4 ] || { echo "usage : recuperation_p4_v1.sh S IDENTIFIANT DOSSIER_TRACES_DU_LANCEMENT DOSSIER_NEUF (aucun relancement)"; exit 2; }
S=$1; ID=$2; T=$(realpath -m "$3"); D=$(realpath -m "$4")""",
"""#     limite) est réécrite entière, hors du filtre.
# Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) :
#   - VC2-fidelite-03 : une seule définition de l'heure limite de destruction, 24 heures après l'heure d'arrêt relue
#     dans arret.txt (cinquième argument : la ligne « ARRÊT CONFIRMÉ : INSTANCE <identifiant> ARRÊTÉE PAR SON
#     IDENTIFIANT (<heure>) » écrite par arreter_p4_v1.sh, une seule, à l'identifiant de l'instance, pas avant la
#     création) ; sans elle (argument absent, fichier illisible, arrêt non confirmé ou d'une autre instance), repli
#     déclaré : création + 9 600 s + 24 heures, écrit avec sa raison. L'heure limite est écrite au début de toute
#     récupération ; dépassée, la ligne « heure limite dépassée de N s : borne du disque dépassée : nœud de Lazar » est
#     écrite, sans retarder la destruction (ce n'est pas un KO) ;
#   - VC2-fidelite-04 : les trois refus en code 2 (place, clonage, traces d'un autre lancement) écrivent l'état de
#     l'instance nommée par l'identifiant et l'heure limite (illisible si ni l'arrêt ni la création ne se lisent) ;
#   - VC2-fidelite-08 (forme la plus stricte) : en repli de l'affichage, seules les lignes OK, KO et « -- » de forme
#     fixe s'affichent entières (motifs fermés, aucune donnée de la branche) ; toute autre ligne n'est affichée que par
#     sa longueur et son empreinte courte, précédées pour une ligne OK, KO ou « -- » de son statut et du numéro de son
#     contrôle (aucun caractère de son texte : les « 40 premiers caractères » de la chaîne v3 sont retirés) ; la ligne de
#     l'instance gardée reste réécrite entière, hors du filtre (choix CV3-03 de la chaîne v3, accepté par la session).
# Codes : 0 tout conforme, instance détruite ; 4 traces seules conformes, instance détruite ; 1 au moins un contrôle en
# échec (destruction comprise), instance gardée : nœud de Lazar ; 2 usage, traces du lancement d'un autre S ou d'une
# autre instance, place disque insuffisante, ou clonage impossible (rien n'est détruit ; état de l'instance et heure
# limite de destruction écrits, sauf sur un usage faux).
# Usage : recuperation_p4_v1.sh S IDENTIFIANT DOSSIER_TRACES_DU_LANCEMENT DOSSIER_NEUF [ARRET_TXT]
#   ARRET_TXT : fichier arret.txt écrit par arreter_p4_v1.sh pour cette instance (sans lui : repli déclaré).
set -uo pipefail
SOI=$(realpath "$0")
[ $# -eq 4 ] || [ $# -eq 5 ] || { echo "usage : recuperation_p4_v1.sh S IDENTIFIANT DOSSIER_TRACES_DU_LANCEMENT DOSSIER_NEUF [ARRET_TXT] (aucun relancement)"; exit 2; }
S=$1; ID=$2; T=$(realpath -m "$3"); D=$(realpath -m "$4"); ARRET=${5:-}"""),
("""else S_LU=""; CREATION=""; ID_LU=""; fi
if [ "$S_LU" != "$S" ] || [ "$(printf '%s\\n' "$ID_LU" | grep -c .)" != 1 ] || [ "$ID_LU" != "$ID" ] || ! [[ "$CREATION" =~ ^[0-9]{9,11}$ ]]; then
    echo "traces du lancement ($L) : commit $( [ "$S_LU" = "$S" ] && echo égal || echo autre ou absent) ; identifiant $( [ "$ID_LU" = "$ID" ] && echo égal || echo autre, absent ou en double) ; création $( [[ "$CREATION" =~ ^[0-9]{9,11}$ ]] && echo lue || echo illisible)"
    echo "$REFUS_TRACES"; exit 2
fi
LIMITE=$(date -u -d "@$((CREATION + PLAFOND_SURVEILLANCE_S + DISQUE_H * 3600))" +%FT%TZ)
gardee() {   # instance gardée : état relu (seuls les champs nommés, réduits aux lettres, chiffres, points, tirets et
             # soulignés) et heure limite de destruction (RC-depense-02) ; définie avant le contrôle de la place et appelée
             # aussi avant les refus en code 2 de la place et du clonage (chaîne v3, VC2-depense-03)""",
"""else S_LU=""; CREATION=""; ID_LU=""; fi
# heure limite de destruction (chaîne v4, VC2-fidelite-03) : 24 heures après l'arrêt relu dans arret.txt ; sinon repli
# déclaré, création + 9 600 s + 24 heures, avec sa raison ; illisible si ni l'un ni l'autre ne se lit
FIN_LUE=absent
if [ -n "$ARRET" ]; then
    if [ -f "$ARRET" ] && [ ! -L "$ARRET" ]; then
        FIN_LUE=$(python3 -c 'import re, sys
try:
    t = open(sys.argv[1], encoding="utf-8").read()
except Exception:
    print("illisible"); raise SystemExit
m = re.findall(r"^ARRÊT CONFIRMÉ : INSTANCE ([0-9]+) ARRÊTÉE PAR SON IDENTIFIANT \\(([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z)\\)$", t, re.M)
print(m[0][1] if len(m) == 1 and m[0][0] == sys.argv[2] else "autre")' "$ARRET" "$ID" 2>/dev/null)
        [ -n "$FIN_LUE" ] || FIN_LUE=illisible
    else FIN_LUE=illisible; fi
fi
LIMITE_S=""; FIN_S=""
[[ "$FIN_LUE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$ ]] && FIN_S=$(date -u -d "$FIN_LUE" +%s 2>/dev/null)
if [[ "$FIN_S" =~ ^[0-9]+$ ]] && [[ "$CREATION" =~ ^[0-9]{9,11}$ ]] && [ "$FIN_S" -lt "$CREATION" ]; then FIN_S=""; FIN_LUE=anterieur; fi
if [[ "$FIN_S" =~ ^[0-9]+$ ]]; then
    LIMITE_S=$((FIN_S + DISQUE_H * 3600)); BASE="arrêt relu à $FIN_LUE + 24 h, arret.txt"
else
    case $FIN_LUE in
        absent) RAISON=absent ;; illisible) RAISON=illisible ;; anterieur) RAISON="antérieur à la création" ;;
        *) RAISON="sans arrêt confirmé de l'instance $ID" ;;
    esac
    if [[ "$CREATION" =~ ^[0-9]{9,11}$ ]]; then
        LIMITE_S=$((CREATION + PLAFOND_SURVEILLANCE_S + DISQUE_H * 3600)); BASE="repli déclaré : arret.txt $RAISON ; création + 9 600 s + 24 h"
    else BASE="arret.txt $RAISON et création illisible"; fi
fi
LIMITE=illisible; [ -n "$LIMITE_S" ] && LIMITE=$(date -u -d "@$LIMITE_S" +%FT%TZ)
depassement() {   # heure limite dépassée : écrite, sans retarder la destruction (chaîne v4, VC2-fidelite-03 ; pas un KO)
    [ -n "$LIMITE_S" ] || return 0
    local n=$(( $(date -u +%s) - LIMITE_S ))
    [ "$n" -gt 0 ] && echo "--  8 heure limite dépassée de $n s : borne du disque dépassée : nœud de Lazar"
    return 0
}
gardee() {   # instance gardée : état relu (seuls les champs nommés, réduits aux lettres, chiffres, points, tirets et
             # soulignés) et heure limite de destruction (RC-depense-02) ; définie avant le contrôle des traces et appelée
             # aussi avant les refus en code 2 des traces, de la place et du clonage (chaîne v3, VC2-depense-03 ; chaîne
             # v4, VC2-fidelite-04)"""),
("""    echo "--  8 instance $ID gardée, non détruite : état ${lu:-illisible} ; heure limite de destruction $LIMITE (création + 9 600 s + 24 h) : nœud de Lazar"
}
LIBRE=$(df -Pk "$(dirname "$D")" 2>/dev/null | awk 'NR==2 {print $4}')
if ! [[ "$LIBRE" =~ ^[0-9]+$ ]] || [ "$LIBRE" -lt "$PLACE_MIN_KO" ]; then
    echo "place disque libre près de $D : ${LIBRE:-illisible} ko"; gardee; echo "$REFUS_PLACE"; exit 2
fi""",
"""    echo "--  8 instance $ID gardée, non détruite : état ${lu:-illisible} ; heure limite de destruction $LIMITE ($BASE) : nœud de Lazar"
}
if [ "$S_LU" != "$S" ] || [ "$(printf '%s\\n' "$ID_LU" | grep -c .)" != 1 ] || [ "$ID_LU" != "$ID" ] || ! [[ "$CREATION" =~ ^[0-9]{9,11}$ ]]; then
    echo "traces du lancement ($L) : commit $( [ "$S_LU" = "$S" ] && echo égal || echo autre ou absent) ; identifiant $( [ "$ID_LU" = "$ID" ] && echo égal || echo autre, absent ou en double) ; création $( [[ "$CREATION" =~ ^[0-9]{9,11}$ ]] && echo lue || echo illisible)"
    depassement; gardee; echo "$REFUS_TRACES"; exit 2
fi
LIBRE=$(df -Pk "$(dirname "$D")" 2>/dev/null | awk 'NR==2 {print $4}')
if ! [[ "$LIBRE" =~ ^[0-9]+$ ]] || [ "$LIBRE" -lt "$PLACE_MIN_KO" ]; then
    echo "place disque libre près de $D : ${LIBRE:-illisible} ko"; depassement; gardee; echo "$REFUS_PLACE"; exit 2
fi"""),
("""git clone -q "$DISTANT" "$D" || { gardee; echo "$REFUS_CLONE"; exit 2; }
cd "$D" || exit 2
if ! git fetch -q origin "$BRANCHE" 2>/dev/null; then
    echo "KO  1a branche $BRANCHE introuvable sur le dépôt distant : rien à récupérer"
    gardee""",
"""git clone -q "$DISTANT" "$D" || { depassement; gardee; echo "$REFUS_CLONE"; exit 2; }
cd "$D" || exit 2
if ! git fetch -q origin "$BRANCHE" 2>/dev/null; then
    echo "KO  1a branche $BRANCHE introuvable sur le dépôt distant : rien à récupérer"
    depassement; gardee"""),
("""else TEXTES_OK=non
    # repli (chaîne v3, VC2-donnees-01) : jetons masqués, puis de chaque ligne ses 40 premiers caractères seulement
    # (aucune fenêtre de 48 n'y tient), sa longueur et son empreinte courte
    FILTRE=(python3 -c 'import hashlib, os, sys
v = [os.environ.get(k) for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY")]
sys.stdin.reconfigure(encoding="utf-8", errors="replace")
for l in sys.stdin:
    l = l.rstrip("\\n")
    for x in v:
        if x and len(x) > 6:
            l = l.replace(x, "***")
    print(f"{l[:40]} ({len(l)} caractères, empreinte {hashlib.sha256(l.encode()).hexdigest()[:12]})", flush=True)')
fi""",
"""else TEXTES_OK=non
    # repli (chaîne v4, VC2-fidelite-08, forme la plus stricte) : jetons masqués, puis seules les lignes OK, KO et « -- »
    # de forme fixe (motifs fermés ci-dessous, aucune donnée de la branche) s'affichent entières ; toute autre ligne
    # n'est affichée que par sa longueur et son empreinte courte, précédées, pour une ligne OK, KO ou « -- », de son
    # statut et du numéro de son contrôle ; aucun caractère du texte de la ligne
    cat > "$TRAV/repli.py" <<'EOF'
import hashlib, os, re, sys
v = [os.environ.get(k) for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY")]
H = r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z"
J = r"(HF_TOKEN|CONTROLE_IA_GITHUB_TOKEN|GH_TOKEN|VAST_API_KEY)"
FIXES = [re.compile(x) for x in (
    r"KO  4f module commun de S ou textes honnêtes de P3 de S illisibles : recherche des fenêtres et filtre de "
    r"l'affichage impossibles \\(repli : jetons masqués ; seules les lignes OK, KO et -- de forme fixe affichées, les "
    r"autres par leur longueur et leur empreinte courte\\)",
    r"OK  0 récupération exécutée = copie versée à S|KO  0 récupération exécutée ≠ copie versée à S",
    r"OK  1a S est ancêtre de la branche|KO  1a S n'est pas ancêtre de la branche",
    r"OK  1b seulement des ajouts \\([0-9]+ fichiers\\)|KO  1b [0-9]+ changement\\(s\\) autre\\(s\\) qu'un ajout",
    r"OK  1c ajouts aux seuls chemins permis \\(manifeste, résultats et tableaux du run, traces p4-\\* ; aucun texte\\)",
    r"OK  1d un seul run : [0-9]{8}-[0-9]{6}-p4-[a-z]+|--  1d aucun run sur la branche : récupération des traces seules "
    r"\\(arrêt avant le run\\)",
    r"OK  1e commits de « instance de calcul \\(P4\\) » \\([0-9]+\\)",
    r"KO  4f fenêtres des textes honnêtes de P3 impossibles \\([A-Za-z_]+\\) : recherche non faite",
    r"OK  6a lignes de progression au journal : [0-9]+, toutes au motif fixe|KO  6a lignes de progression : [0-9]+, dont "
    r"[0-9]+ au motif fixe|OK  6a aucune ligne de progression sans run|KO  6a [0-9]+ ligne\\(s\\) de progression sans run",
    r"(OK|KO)  7 valeur de " + J + r" : [0-9]+ occurrence\\(s\\)",
    r"KO  7 " + J + r" absent de l'environnement de la session : recherche impossible",
    r"--  8 heure limite de destruction " + H + r" \\((arrêt relu à " + H + r" \\+ 24 h, arret\\.txt|repli déclaré : "
    r"arret\\.txt (absent|illisible|antérieur à la création|sans arrêt confirmé de l'instance [0-9]{6,10}) ; création "
    r"\\+ 9 600 s \\+ 24 h)\\)",
    r"--  8 heure limite dépassée de [0-9]+ s : borne du disque dépassée : nœud de Lazar")]
STATUT = re.compile(r"(OK|KO|--)  [0-9]{1,2}[a-z]? ")
sys.stdin.reconfigure(encoding="utf-8", errors="replace")
for l in sys.stdin:
    l = l.rstrip("\\n")
    for x in v:
        if x and len(x) > 6:
            l = l.replace(x, "***")
    if any(f.fullmatch(l) for f in FIXES):
        print(l, flush=True)
        continue
    s = STATUT.match(l)
    print(f"{s.group(0) if s else ''}(ligne de {len(l)} caractères, empreinte "
          f"{hashlib.sha256(l.encode('utf-8', 'replace')).hexdigest()[:12]})", flush=True)
EOF
    FILTRE=(python3 -I -B "$TRAV/repli.py")
fi"""),
("""echo "tête de la branche : $HB"
[ "$TEXTES_OK" = oui ] || ko "4f module commun de S ou textes honnêtes de P3 de S illisibles ($TEXTES_P3) : recherche des fenêtres et filtre de l'affichage impossibles (repli : jetons masqués, 40 premiers caractères, longueur et empreinte courte de chaque ligne)\"""",
"""echo "tête de la branche : $HB"
# heure limite de destruction, écrite au début ; dépassée : écrite, sans retarder la destruction (chaîne v4, VC2-fidelite-03)
echo "--  8 heure limite de destruction $LIMITE ($BASE)"
depassement
[ "$TEXTES_OK" = oui ] || ko "4f module commun de S ou textes honnêtes de P3 de S illisibles : recherche des fenêtres et filtre de l'affichage impossibles (repli : jetons masqués ; seules les lignes OK, KO et -- de forme fixe affichées, les autres par leur longueur et leur empreinte courte)\""""),
("""# chaîne v3 : en repli de l'affichage, la ligne de l'instance gardée (forme fixe) est réécrite entière, hors du filtre""",
"""# chaîne v3 (CV3-03, accepté par la session) : en repli de l'affichage, la ligne de l'instance gardée (forme fixe) est
# réécrite entière, hors du filtre"""),
]
