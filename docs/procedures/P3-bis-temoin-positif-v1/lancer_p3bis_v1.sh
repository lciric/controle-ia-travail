#!/usr/bin/env bash
# Création de l'instance de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au 2026-11-23 : R-2077), v1. Texte qui fait foi :
# brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md (eb65773f…), en-tête (GO, Lancement),
# « Liste d'arrêt », plan, point 11, « Devis », « Ce que le code et la chaîne doivent changer », point 6 ; contre-lecture
# du code (7a074ad1…), point 6. Décliné de docs/procedures/P3-premier-test-v2/lancer_p3_v1.sh (P3) sous un nom neuf (R12).
# Ce qui change contre P3 :
#   - GO GO-2026-11-10-02 seulement, relu par le module commun verifications_p3bis_v1.py (ligne « - GO : » et GO_ID de la
#     ligne « Lancement » du texte, une seule ligne au registre, plafond 80 USD, échéance 2026-11-23, aucune révocation au
#     sens exact du texte) ; date du jour au plus tard DATE_LIMITE_CREATION, relue avant et après les contrôles, avant
#     chaque essai d'offre et juste avant la création ; la ligne d'accord du jour de P3 n'existe plus (DB-5 (a) : le GO en
#     tient lieu) ;
#   - S passé en argument (le commit de scellement est fait sur une branche tirée du commit du code, puis poussé : texte,
#     en-tête) : S ajoute le sceau du texte, est contenu dans une branche du dépôt distant ;
#   - offre : filtre du point 11 (A100 SXM4 80 Go, CUDA ≥ 13.0, fiabilité ≥ 0,98, au plus 2,10 USD/h, ≥ 30 cœurs
#     effectifs, 128 000 Mo, disque ≥ 80 Go, stockage ≤ 0,08 USD/h, téléchargement ≤ 0,05 USD/Go, EPYC 7513 exigé) ; douze
#     essais à 15 minutes ; puis repli écrit (seule condition du processeur retirée), écrit au journal du lancement et dans
#     repli-processeur.txt, ligne à consigner au registre des dépenses par la session ; jamais d'autre condition relâchée ;
#   - crédit : au moins 20 USD plus 10 heures du prix des instances nommées en marche ;
#   - instances du compte : arrêtées et dans ARRETEES_TOLEREES, ou en marche et nommées en argument avec le GO de leur
#     course (liste fermée) ; jamais touchées ici (aucun arrêt, aucune destruction dans ce script) ;
#   - branche de calcul calcul/p3bis-reel-vN (N = 1, relance 2 puis 3) absente du dépôt distant ; pour N ≥ 2, la branche
#     de la tentative précédente y est (la relance suit une tentative réelle) ;
#   - aucun délai : ni plafond de surveillance, ni `timeout` des contrôles, ni plage horaire (P3 : 23:30 à 00:00, pour la
#     suite complète des tests ; P3-bis joue la liste ciblée) ;
#   - l'identifiant de l'instance créée est écrit (« instance <id> ») : seule cible permise d'un arrêt ou d'une
#     destruction par la surveillance, le contrôle à cinq minutes et la destruction (R10).
# Gardé de P3 : scripts de la chaîne égaux à leurs copies versées à S ; preuves des essais (journaux des bancs et des
# deux répétitions versés à S, scellés, conformes au module commun, scripts éprouvés égaux aux copies versées) ;
# contrôles avant dépense rejoués sur S (dernière ligne « CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES ») ; amorce extraite
# de S, citée par son empreinte ; ligne « Lancement » ; garde de calcul du dépôt rejouée sur la commande ; aucun jeton
# affiché (réponse masquée) ; aucune création si un contrôle échoue.
# Codes : 0 création ; 3 date limite, place, crédit ou aucune offre conforme (attente) ; 4 tout échec à partir de la ligne
# « creation » de lancement.txt (création douteuse : vérifier les instances, forme filtrée, jamais --raw sans filtre) ;
# 2 tout autre arrêt avant.
# Usage : lancer_p3bis_v1.sh S DOSSIER_TRACES EN_MARCHE N
#   S           commit de scellement du texte (40 caractères) ;
#   EN_MARCHE   instances en marche d'autres courses : « ID:GO-AAAA-MM-JJ-NN,… », ou « - » ;
#   N           tentative : 1, ou 2 et 3 pour une relance sous ce texte (texte, critères, ligne 1).
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 4 ] && [ -n "$2" ] || { echo "usage : lancer_p3bis_v1.sh S DOSSIER_TRACES EN_MARCHE N"; exit 2; }
S=$1; T=$(realpath -m "$2"); EN_MARCHE=$3; N=$4; OFFRE=""
GO_CALCUL=GO-2026-11-10-02                       # seul GO accepté (texte, en-tête et liste d'arrêt)
DATE_LIMITE_CREATION=2026-11-23                  # « création au plus tard le 23 novembre 2026 »
ESSAIS_AVANT_REPLI=12                            # douze essais d'offre, processeur exigé…
INTERVALLE_OFFRE_S=900                           # … à 15 minutes d'intervalle, puis repli écrit (plan, point 11)
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
ARRETEES_TOLEREES="58936096 58936099 58936100"   # instances arrêtées tolérées, épinglées (consigne du lanceur, 2026-11-10 ; texte, brouillon 6, D1 (a))
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.98 cpu_ram>=128 disk_space>=80 rentable=true"
DEPOT=/home/user/controle-ia-travail             # registres courants (GO) et garde de calcul ; S y est lu
H=$(dirname "$(realpath "$0")")                  # dossier d'où la chaîne est jouée (chaque script y est comparé à sa copie versée à S)
V=vastai                                         # outil de location, trouvé sur le PATH (vérifié ci-dessous)
VERSEES=docs/procedures/P3-bis-temoin-positif-v1
P=prereg/P3-bis-temoin-positif-v1.md
A=scripts/amorce_instance_p3bis_v2.sh            # amorce (noms communs v2 ; dépendance déclarée)
VERIF=$H/verifications_p3bis_v1.py
CHAINE="verifications_p3bis_v1.py controles_avant_depense_p3bis_v1.sh surveiller_p3bis_v1.sh controle_cinq_minutes_p3bis_v1.sh recuperation_p3bis_v1.sh detruire_p3bis_v1.sh sceller_p3bis_v1.sh repetition_jouet_p3bis_v1.sh repetition_finale_p3bis_v1.sh essais_verifications_p3bis_v1.py essais_lanceur_p3bis_v1.sh essais_surveillance_p3bis_v1.sh essais_controles_p3bis_v1.sh essais_recuperation_p3bis_v1.sh"
PREUVES="banc-verifications-p3bis-v1.log banc-lanceur-p3bis-v1.log banc-surveillance-p3bis-v1.log banc-controles-p3bis-v1.log banc-recuperation-p3bis-v1.log repetition-jouet-p3bis-v1.log repetition-finale-p3bis-v1.log"
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S : commit de 40 caractères hexadécimaux attendu"; exit 2; }
[[ "$(basename "$2")" =~ ^[0-9]+$ ]] && { echo "DOSSIER_TRACES purement numérique ($2) : refusé (une offre n'est jamais passée en argument)"; exit 2; }
[[ "$EN_MARCHE" = "-" || "$EN_MARCHE" =~ ^[0-9]{6,10}:GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}(,[0-9]{6,10}:GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2})*$ ]] \
    || { echo "EN_MARCHE : « ID:GO-AAAA-MM-JJ-NN,… » ou « - »"; exit 2; }
[[ "$N" =~ ^[123]$ ]] || { echo "N : 1, 2 ou 3 (calcul/p3bis-reel-vN ; texte, ligne 1 de la table)"; exit 2; }
BRANCHE=calcul/p3bis-reel-v$N; ETIQUETTE=p3bis-v$N
[[ "$ARRETEES_TOLEREES" =~ ^[0-9]{6,10}( [0-9]{6,10})*$ ]] || { echo "instances tolérées non épinglées"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
command -v "$V" > /dev/null || { echo "outil de location introuvable sur le PATH"; exit 2; }
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
date_permise() {   # date du jour (UTC) au plus tard DATE_LIMITE_CREATION
    local j; j=$(date -u +%F)
    [[ "$j" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && [[ ! "$j" > "$DATE_LIMITE_CREATION" ]] \
        || { echo "date du jour $j après le $DATE_LIMITE_CREATION : aucune création (ligne de GO neuve, nœud)"; return 1; }
}
# 0. date limite et place disque
date_permise || exit 3
LIBRE_T=$(df -Pk "$(dirname "$T")" | awk 'NR==2 {print $4}'); [ "$LIBRE_T" -ge 3000000 ] || { echo "place disque des traces : $LIBRE_T ko (3 Go exigés)"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone-controles" "$T/clone-controles.travail"' EXIT        # le clone des contrôles ne reste jamais
printf 'heure de départ %s UTC ; place libre %s ko\n' "$(date -u +%H:%M:%S)" "$LIBRE_T" >> "$T/lancement.txt"
# 1. commit de scellement : ajoute le sceau du texte ; contenu dans une branche du dépôt distant
git -C "$DEPOT" cat-file -e "$S^{commit}" 2>/dev/null || git -C "$DEPOT" fetch -q origin || true
git -C "$DEPOT" cat-file -e "$S^{commit}" 2>/dev/null || { echo "commit de scellement $S introuvable"; exit 2; }
[ "$(git -C "$DEPOT" diff-tree --no-commit-id --name-only --diff-filter=A -r "$S" -- "$P.sha256")" = "$P.sha256" ] \
    || { echo "$S n'ajoute pas $P.sha256 : ce n'est pas le commit de scellement"; exit 2; }
git -C "$DEPOT" fetch -q origin
[ -n "$(git -C "$DEPOT" branch -r --contains "$S" 2>/dev/null)" ] || { echo "commit de scellement $S absent du dépôt distant"; exit 2; }
# 2. scripts égaux à leurs copies versées à S (le lanceur exécuté par son propre chemin)
for paire in "lancer_p3bis_v1.sh=$0" $(for s in $CHAINE; do echo "$s=$H/$s"; done); do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/${paire%%=*}" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "${paire#*=}" | cut -d' ' -f1)" ] \
        || { echo "${paire%%=*} exécuté ≠ copie versée au commit S"; exit 2; }
done
# 2 bis. preuves des essais (R5) : journaux versés à S, scellés, conformes au module commun ; scripts éprouvés égaux à
# leurs copies versées à S
PREUVES_D=$(mktemp -d)
for j in $PREUVES; do
    git -C "$DEPOT" show "$S:$VERSEES/$j" > "$PREUVES_D/$j" 2>/dev/null || { rm -rf "$PREUVES_D"; echo "preuves des essais : journal $j absent de S"; exit 2; }
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$j.sha256" 2>/dev/null)" = "$(sha256sum "$PREUVES_D/$j" | cut -d' ' -f1)  $j" ] \
        || { rm -rf "$PREUVES_D"; echo "preuves des essais : sceau de $j absent ou non conforme à S"; exit 2; }
done
# shellcheck disable=SC2086
python3 -I "$VERIF" preuves "$PREUVES_D" $PREUVES > "$PREUVES_D/sortie.txt" 2>&1 \
    || { m=$(tail -1 "$PREUVES_D/sortie.txt"); rm -rf "$PREUVES_D"; echo "preuves des essais : $m"; exit 2; }
while read -r s e; do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] \
        || { rm -rf "$PREUVES_D"; echo "preuves des essais : $s éprouvé ($e) ≠ copie versée à S"; exit 2; }
done < "$PREUVES_D/sortie.txt"
echo "preuves des essais : $(echo $PREUVES | wc -w) journaux conformes ; $(wc -l < "$PREUVES_D/sortie.txt") scripts éprouvés égaux à leurs copies versées à S"
rm -rf "$PREUVES_D"
# 3. texte de S, GO relu au registre courant (avant les contrôles, puis après, puis avant la création)
git -C "$DEPOT" show "$S:$P" > "$T/prereg-S.md"
go_conforme() {
    local r
    r=$(python3 -I "$VERIF" go "$T/prereg-S.md" "$DEPOT/registres/go.md" "$(date -u +%F)" 2>&1) \
        || { echo "GO de calcul : $(printf '%s\n' "$r" | tail -1) : pas de création"; return 1; }
    printf 'go %s\n' "$r" >> "$T/lancement.txt"
    echo "GO de calcul : $r"
}
go_conforme || exit 2
# jetons présents (jamais affichés) : celui de l'instance est CONTROLE_IA_GITHUB_TOKEN
J_HF=${HF_TOKEN:-}; J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}
[ "${#J_HF}" -ge 8 ] && [ "${#J_GH}" -ge 8 ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
unset J_HF J_GH
# 4. contrôles avant dépense sur S (aucun délai : « aucun budget de temps »)
if ! bash "$H/controles_avant_depense_p3bis_v1.sh" "$S" "$T/clone-controles" "$BRANCHE" > "$T/controles.txt" 2>&1; then
    grep '^KO' "$T/controles.txt" || tail -5 "$T/controles.txt"; echo "contrôles avant dépense en échec : pas de création"; exit 2
fi
tail -1 "$T/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || { echo "contrôles : dernière ligne inattendue"; exit 2; }
rm -rf "$T/clone-controles" "$T/clone-controles.travail"
date_permise || exit 3
go_conforme || exit 2
# 5. amorce de S, citée par son empreinte (texte aux espaces réduites) ; ligne « Lancement »
git -C "$DEPOT" show "$S:$A" > "$T/amorce.sh" 2>/dev/null || { echo "amorce $A absente de S"; exit 2; }
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
tr '\n' ' ' < "$T/prereg-S.md" | tr -s ' ' > "$T/prereg-S-plat.txt"
grep -qF "\`$A\` (\`$E\`" "$T/prereg-S-plat.txt" || { rm -f "$T/prereg-S-plat.txt"; echo "empreinte de l'amorce ($E) non citée par le texte"; exit 2; }
rm -f "$T/prereg-S-plat.txt"
grep -qF "\`PREREG=$P\`, \`BRANCHE=calcul/p3bis-reel-v1\`" "$T/prereg-S.md" || { echo "PREREG ou BRANCHE : la ligne « Lancement » de S cite autre chose"; exit 2; }
grep -qF "\`DEPOT_URL=$DEPOT_URL\`" "$T/prereg-S.md" || { echo "DEPOT_URL : la ligne « Lancement » de S cite autre chose"; exit 2; }
# 6. branche de calcul absente du dépôt distant ; pour une relance, branche de la tentative précédente présente
c=0; git ls-remote --exit-code "$DEPOT_URL" "refs/heads/$BRANCHE" > /dev/null 2>&1 || c=$?
[ "$c" = 2 ] || { echo "branche $BRANCHE : git ls-remote, code $c (2 attendu : absente du dépôt distant)"; exit 2; }
if [ "$N" -gt 1 ]; then
    c=0; git ls-remote --exit-code "$DEPOT_URL" "refs/heads/calcul/p3bis-reel-v$((N - 1))" > /dev/null 2>&1 || c=$?
    [ "$c" = 0 ] || { echo "relance $N : branche calcul/p3bis-reel-v$((N - 1)) absente du dépôt distant (code $c) ; une relance suit une tentative"; exit 2; }
fi
echo "branche $BRANCHE absente du dépôt distant" | tee -a "$T/lancement.txt"
# 7. offre : filtre du point 11, douze essais à INTERVALLE_OFFRE_S, processeur exigé ; puis un essai en repli écrit
choisir() {   # $1 : 0 (processeur exigé) ou 1 (repli) ; écrit OFFRE et DPH, rend le code du module
    local c=0 choix
    "$V" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw > "$T/offres-brut.json" 2>/dev/null || true
    choix=$(python3 -I "$VERIF" offres "$T/offres-brut.json" "$T/offre.json" "$T/lancement.txt" "$T/offres-relues.json" "$1") || c=$?
    [ -s "$T/offres-relues.json" ] || head -c 2000 "$T/offres-brut.json" > "$T/offres-relues-brut.txt"
    rm -f "$T/offres-brut.json"
    [ "$c" = 0 ] && { OFFRE=${choix%% *}; DPH=${choix#* }; }
    return "$c"
}
c=3; k=0
while [ "$k" -lt "$ESSAIS_AVANT_REPLI" ]; do
    k=$((k + 1))
    date_permise || exit 3
    c=0; choisir 0 || c=$?
    echo "essai d'offre $k sur $ESSAIS_AVANT_REPLI (processeur exigé) : code $c" | tee -a "$T/lancement.txt"
    [ "$c" = 0 ] && break
    [ "$c" = 3 ] || { echo "offres : relecture impossible (code $c)"; exit 2; }
    [ "$k" -lt "$ESSAIS_AVANT_REPLI" ] && sleep "$INTERVALLE_OFFRE_S"
done
if [ "$c" = 3 ]; then
    LIGNE_REPLI="$(date -u +%FT%TZ) P3-bis, $GO_CALCUL : aucune offre conforme pendant $ESSAIS_AVANT_REPLI essais à $INTERVALLE_OFFRE_S s ; repli écrit (plan, point 11) : seule la condition du processeur est retirée ; réserve PB-9 « processeur autre que celui de P3 »"
    printf '%s\n' "$LIGNE_REPLI" | tee -a "$T/lancement.txt" > "$T/repli-processeur.txt"
    echo "À CONSIGNER AU REGISTRE DES DÉPENSES (session) : $LIGNE_REPLI"
    date_permise || exit 3
    c=0; choisir 1 || c=$?
    echo "essai d'offre en repli écrit : code $c" | tee -a "$T/lancement.txt"
    [ "$c" = 3 ] && { echo "aucune offre conforme, même en repli : pas de création"; exit 3; }
    [ "$c" = 0 ] || { echo "offres : relecture impossible (code $c)"; exit 2; }
fi
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre choisie illisible"; exit 2; }
echo "offre choisie : $OFFRE ($DPH USD/h), la moins chère des offres conformes" | tee -a "$T/lancement.txt"
# 8. instances du compte (liste fermée) ; somme des prix des instances nommées en marche
SOMME=$("$V" show instances --raw 2>/dev/null | python3 -I "$VERIF" instances "$ARRETEES_TOLEREES" "$EN_MARCHE" "$DEPOT/registres/go.md" "$T/lancement.txt") \
    || { echo "instances : non tolérée(s), ou liste illisible (voir les lignes ci-dessus et lancement.txt) : pas de création"; exit 2; }
# 9. crédit exigé : 20 USD plus 10 heures des instances nommées en marche (programme qui relit la réponse ; aucune valeur
# relue n'est insérée dans du code)
c=0
CREDIT_LIGNE=$("$V" show user --raw 2>/dev/null | python3 -I "$VERIF" credit "$SOMME") || c=$?
printf '%s\n' "$CREDIT_LIGNE" | tee -a "$T/lancement.txt"
case $c in
    0) ;;
    3) echo "crédit insuffisant : pas de création ; recharge demandée à Lazar"; exit 3 ;;
    *) echo "crédit illisible (show user, code $c) : pas de création"; exit 2 ;;
esac
# 10. GO et date relus après l'attente des offres ; garde de calcul du dépôt rejouée sur la commande
go_conforme || exit 2
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GO_CALCUL" "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
date_permise || exit 3
# 11. création ; à partir d'ici, tout échec rend 4
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'lanceur p3bis v1 %s ; instances en marche nommées %s\ncommit %s\noffre %s\nprereg %s\nbranche %s\netiquette %s\ngo %s\ncreation %s\nsurveillance : surveiller_p3bis_v1.sh <instance> %s <dépense antérieure en USD> <dossier neuf> (aucun plafond de durée ; alerte à deux heures sans PROGRES ; arrêt par identifiant sur fin, échec d amorce, redémarrage, état terminal, processus mort, 80 USD ; code 5 : instance gardée)\ncontrôle à cinq minutes entre %s et %s (création + 180 à 300 s ; controle_cinq_minutes_p3bis_v1.sh <instance> %s <dossier neuf>)\ndestruction : par son identifiant, dès les résultats poussés vérifiés (detruire_p3bis_v1.sh ; R10 ; texte, plan, point 11)\n' \
    "$(sha256sum "$0" | cut -d' ' -f1)" "$EN_MARCHE" "$S" "$OFFRE" "$P" "$BRANCHE" "$ETIQUETTE" "$GO_CALCUL" "$CREATION" \
    "$T" "$((CREATION + 180))" "$((CREATION + 300))" "$T" >> "$T/lancement.txt"
GO_ID="$GO_CALCUL" "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=$DEPOT_URL -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh" 2>&1 | python3 -c '
import json, os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) > 6:
        t = t.replace(v, "***")
try:
    d = json.loads(t)
except Exception:
    open(os.environ["T_LANCEMENT"] + "/reponse-masquee.txt", "w").write(t[:300])
    print("réponse illisible (300 premiers caractères masqués dans reponse-masquee.txt) ; vérifier par « vastai show instances », sans --raw")
    sys.exit(4)
ok = d.get("success") is True and isinstance(d.get("new_contract"), int) and not isinstance(d.get("new_contract"), bool)
print("succès :", d.get("success"), "; identifiant", d.get("new_contract"), "; message :", str(d.get("msg", ""))[:200])
if ok:
    open(os.environ["T_LANCEMENT"] + "/lancement.txt", "a").write("instance " + str(d["new_contract"]) + "\n")
sys.exit(0 if ok else 4)' | tee -a "$T/lancement.txt"
st=("${PIPESTATUS[@]}")
[ "${st[0]}" = 0 ] && [ "${st[1]}" = 0 ] && [ "${st[2]}" = 0 ] || { echo "création douteuse (statuts ${st[*]}) : vérifier « vastai show instances », sans --raw"; exit 4; }
exit 0
