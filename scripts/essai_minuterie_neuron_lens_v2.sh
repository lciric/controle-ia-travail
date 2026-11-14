#!/usr/bin/env bash
# Essai (R5) de la minuterie de destruction v2, sans location : faux outil du loueur qui **reproduit le défaut constaté le 14 novembre
# 2026** (sans `-y` : invite [y/N], « Aborted. », code 0, rien détruit ; avec `-y` : instance retirée) et rend la liste des instances en
# JSON (avec un témoin d'une autre session). Cas : sain (échéance, `-y`, absence prouvée, code 0) ; **artefact v1** (la minuterie v1,
# jouée sur le même faux outil, écrit « destruction demandee » et rend 0 alors que l'instance reste : défaut reproduit) ; outil qui
# refuse même avec `-y` (3 essais, absence jamais prouvée, code 6) ; suivi sans `CONTROLE_IA_GITHUB_TOKEN_2` (absence non prouvable :
# code 6 même si l'instance est partie — aucun repli silencieux) ; arrêt par le PID écrit, lancement détaché ; bornes, outil relatif ou
# absent, interprète du suivi absent, identifiant invalide, fichier PID impossible. Verdict automatique (écarts comptés dans un fichier).
# Usage : bash scripts/essai_minuterie_neuron_lens_v2.sh <dossier neuf>
set -uo pipefail
SRC=$(cd "$(dirname "$0")/.." && pwd); S=$1
[ -e "$S" ] && { echo "dossier existant"; exit 2; }
mkdir -p "$S"; E="$S/ecarts.txt"; : > "$E"
ecart() { echo "$*" >> "$E"; echo "  ÉCART : $*"; }
M="$SRC/scripts/minuterie_destruction_neuron_lens_v2.sh"; M1="$SRC/scripts/minuterie_destruction_neuron_lens_v1.sh"
export CONTROLE_IA_GITHUB_TOKEN_2=jeton-factice-essai-minuterie-0123456789
cat > "$S/faux-outil" <<EOF
#!/usr/bin/env bash
ETAT="$S/presentes.txt"; echo "\$*" >> "$S/appels.txt"
if [ "\$1 \$2" = "destroy instance" ]; then
  if [ "\${4:-}" = "-y" ] && [ "\${FAUX_REFUS:-0}" != 1 ]; then grep -vx "\$3" "\$ETAT" > "\$ETAT.n"; mv "\$ETAT.n" "\$ETAT"; echo "destroying instance \$3."; exit 0; fi
  if [ "\${4:-}" = "-y" ]; then echo "failed"; exit 0; fi
  echo "Are you sure you want to destroy instance \$3? [y/N] "; read -r r || true; echo "Aborted."; exit 0
fi
if [ "\$1 \$2" = "show instances" ]; then
  printf '['; printf '{"id": 60480302}'; while read -r i; do [ -n "\$i" ] && printf ', {"id": %s}' "\$i"; done < "\$ETAT"; printf ']\n'; exit 0
fi
exit 1
EOF
chmod 755 "$S/faux-outil"
presente() { grep -qx "$1" "$S/presentes.txt"; }
attendu() { echo "CAS $1 : code=$2 (attendu $3)"; [ "$2" = "$3" ] || ecart "cas $1 : code $2 au lieu de $3"; }
echo "ESSAI minuterie v2 ; $(date -u +%FT%TZ)"
# 1. sain
echo 123 > "$S/presentes.txt"
BORNE_MIN_S=1 ATTENTE_S=1 bash "$M" 123 2 "$S/faux-outil" "$S/pid-sain" > "$S/j-sain.txt" 2>&1; attendu sain $? 0
presente 123 && ecart "sain : instance 123 encore présente" || echo "  sain : instance 123 absente"
grep -q "destroy instance 123 -y" "$S/appels.txt" && echo "  sain : appel avec -y" || ecart "sain : appel sans -y"
# 2. artefact : la v1 sur le même faux outil (défaut du 14 novembre reproduit)
echo 124 > "$S/presentes.txt"
BORNE_MIN_S=1 bash "$M1" 124 2 "$S/faux-outil" "$S/pid-v1" > "$S/j-v1.txt" 2>&1; c=$?
if [ "$c" -eq 0 ] && presente 124 && grep -q "destruction demandee" "$S/j-v1.txt"; then
  echo "ARTEFACT v1 : code=0, « destruction demandee » écrit, instance 124 toujours présente : défaut reproduit"
else ecart "artefact v1 : défaut non reproduit (code $c)"; fi
# 3. refus même avec -y
echo 125 > "$S/presentes.txt"
FAUX_REFUS=1 BORNE_MIN_S=1 ATTENTE_S=1 bash "$M" 125 1 "$S/faux-outil" "$S/pid-r" > "$S/j-refus.txt" 2>&1; attendu refus $? 6
n=$(grep -c "destroy instance 125 -y" "$S/appels.txt"); echo "  refus : $n appel(s) avec -y (attendu 3)"; [ "$n" -eq 3 ] || ecart "refus : $n appels"
# 4. suivi sans jeton : absence non prouvable (aucun repli silencieux)
echo 126 > "$S/presentes.txt"
env -u CONTROLE_IA_GITHUB_TOKEN_2 BORNE_MIN_S=1 ATTENTE_S=1 bash "$M" 126 1 "$S/faux-outil" "$S/pid-sj" > "$S/j-sansjeton.txt" 2>&1; attendu "suivi sans jeton" $? 6
presente 126 && ecart "suivi sans jeton : l'instance devait être partie (-y)" || echo "  suivi sans jeton : instance partie, mais absence non prouvée → code 6"
# 5. arrêt par PID, lancement détaché
echo 127 > "$S/presentes.txt"; : > "$S/appels.txt"
BORNE_MIN_S=1 setsid nohup bash "$M" 127 6 "$S/faux-outil" "$S/pid-det" > "$S/j-det.txt" 2>&1 < /dev/null &
sleep 1; P=$(cat "$S/pid-det" 2>/dev/null)
if [ -n "$P" ] && ps -p "$P" -o args= | grep -q minuterie_destruction_neuron_lens_v2; then echo "  détachée : PID $P vivant, porte la minuterie v2"; else ecart "détachée : PID $P absent ou autre"; fi
kill "$P"; sleep 8
ps -p "$P" -o stat= 2>/dev/null | grep -qv Z && ecart "détachée : PID $P encore vivant" || echo "  détachée : PID $P arrêté"
[ -s "$S/appels.txt" ] && ecart "détachée : outil appelé malgré l'arrêt" || echo "  détachée : aucun appel après l'arrêt (échéance passée)"
presente 127 && echo "  détachée : instance 127 toujours là (attendu : l'arrêt empêche la destruction)" || ecart "détachée : 127 détruite"
# 6. arguments
for d in 5 200000 "" abc; do bash "$M" 128 "$d" "$S/faux-outil" "$S/pid-b" > /dev/null 2>&1; attendu "bornes '$d'" $? 3; done
[ -e "$S/pid-b" ] && ecart "bornes : PID écrit alors que rien n'est armé" || true
bash "$M" 128 600 "faux-outil" "$S/pid-o" > /dev/null 2>&1; attendu "outil relatif" $? 4
bash "$M" 128 600 "$S/inexistant" "$S/pid-o" > /dev/null 2>&1; attendu "outil absent" $? 4
SUIVI_PY=/inexistant/python bash "$M" 128 600 "$S/faux-outil" "$S/pid-o" > /dev/null 2>&1; attendu "suivi absent" $? 4
bash "$M" "12a" 600 "$S/faux-outil" "$S/pid-i" > /dev/null 2>&1; attendu identifiant $? 2
bash "$M" 128 600 "$S/faux-outil" "$S/inexistant/pid" > /dev/null 2>&1; attendu "fichier PID" $? 5
echo "  journaux :"; cat "$S"/j-sain.txt "$S"/j-v1.txt "$S"/j-refus.txt "$S"/j-sansjeton.txt "$S"/j-det.txt | sed 's/^/    /'
N=$(wc -l < "$E")
echo "VERDICT de l'essai : $([ "$N" -eq 0 ] && echo "conforme, 0 écart" || echo "NON conforme, $N écart(s) : $(tr '\n' ';' < "$E")")"
