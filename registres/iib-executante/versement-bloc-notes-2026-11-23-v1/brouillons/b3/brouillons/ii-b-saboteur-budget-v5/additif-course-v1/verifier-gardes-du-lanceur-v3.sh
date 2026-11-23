#!/usr/bin/env bash
# Rédigé par Claude Opus 5.5 en remplacement de Fable 5.2 (limite atteinte) : À REVOIR PAR FABLE avant scellement.
# Vérification, sur processeur et sans dépense, des gardes du lanceur de session du saboteur à budget sous la ligne
# GO-2026-11-22-75, au code qui porte le correctif 0023 (GO-2026-11-22-77) — v3 ; les v1 et v2 restent telles quelles.
# Usage : bash verifier-gardes-du-lanceur-v3.sh DEPOT COMMIT_DU_CODE REGISTRE_GO.md CONFIG_ETALONNAGE.json
#   DEPOT : dépôt local qui porte l'objet COMMIT_DU_CODE (ici 9b03d0ea410a38a4cce923a41cb07f85233da8d1, correctif 0023) ;
#   REGISTRE_GO.md : registres/go.md de main, à une tête qui porte GO-2026-11-22-75 ; CONFIG_ETALONNAGE.json : configuration
#   scellée de l'étalonnage (pour son calendrier).
# Changement à la v2 : au § 2, les comptes 5,52 et 9,65 sont attendus ACCEPTÉS (coupure de la machine min(55, 60 − antérieure)),
# 60 et au-delà refusés ; le plafond total passé à la garde de dépense est imprimé ; le § 5 lit l'épuisement sous ce plafond total.
# Rien n'est créé, aucun loueur n'est appelé, aucune sortie de mesure n'est lue.
set -uo pipefail
DEPOT="${1:?dépôt}"; C="${2:?commit du code}"; REG="${3:?registre go.md}"; CFG="${4:?configuration}"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
git -C "$DEPOT" archive "$C" src/controle_ia/iib src/controle_ia/t06 src/controle_ia/gardes.py src/controle_ia/__init__.py | tar -x -C "$T"
S5="import sys; sys.path.insert(0, '$T/src'); from controle_ia.iib import session_v5; sys.exit(session_v5.main(sys.argv[1:]))"
S3="import sys; sys.path.insert(0, '$T/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
echo "code $C, arbre $(git -C "$DEPOT" rev-parse "$C^{tree}") ; registre $(sha256sum "$REG" | cut -d' ' -f1) ; configuration $(sha256sum "$CFG" | cut -d' ' -f1)"
echo "== 1. plafond lu sur la ligne GO-2026-11-22-75"
python3 -I -B -c "$S5" plafond-ligne "$REG" GO-2026-11-22-75 2026-11-23; echo "code $?"
echo "== 2. dépense antérieure (correctif 0023) : plafond de la configuration 55, ligne GO-2026-11-22-75, jour 2026-11-23"
echo "   cas sains attendus en code 0 : 0, 5, 5.52, 9.65, 16.22 ; artefacts attendus en code 1 : 60, 60.01, -1, nan, inf, illisible"
for a in 0 4.20 5 5.01 5.52 9.65 16.22 59.99 60 60.01 -1 nan inf illisible; do
  echo "-- antérieure $a"
  python3 -I -B -c "$S5" go "$REG" GO-2026-11-22-75 55 "$a" 2026-11-23; echo "code $?"
  printf 'plafond total : '; python3 -I -B -c "$S5" plafond-total "$REG" GO-2026-11-22-75 55 "$a" 2026-11-23; echo "code $?"
done
echo "== 2 bis. artefacts de la configuration et de la ligne : configuration 61 > ligne ; ligne absente"
python3 -I -B -c "$S5" go "$REG" GO-2026-11-22-75 61 0 2026-11-23; echo "code $?"
python3 -I -B -c "$S5" go "$REG" GO-2099-01-01-01 55 0 2026-11-23; echo "code $?"
echo "== 3. variante de plafond de la configuration scellée (B : 60 USD) contre le plafond de la ligne"
python3 -I -B -c "$S5" variante "$CFG" 60; echo "code $?"
echo "== 4. calendrier de la configuration scellée, ligne GO-2026-11-22-75 à 60 USD"
for j in 2026-11-23 2026-11-26 2026-11-27; do echo "-- jour $j"; python3 -I -B -c "$S3" calendrier "$CFG" "$REG" GO-2026-11-22-75 60 "$j"; echo "code $?"; done
echo "== 5. épuisement calculé sous le plafond total : carte 1.30, stockage 0.08, téléchargement 2, création à l'instant 1000000000"
for a in 0 5.52 9.65 16.22; do
  P=$(python3 -I -B -c "$S5" plafond-total "$REG" GO-2026-11-22-75 55 "$a" 2026-11-23) || { echo "plafond total refusé pour $a"; continue; }
  echo "-- antérieure $a, plafond total $P"
  python3 -I -B -c "$S3" depense "$P" 1.30 0.08 1000000000 "$a" 2 1000000000; echo "code $?"
done
