#!/usr/bin/env bash
# Vérification, sur processeur et sans dépense, des gardes du lanceur de session du saboteur à budget sous la ligne
# GO-2026-11-22-75 (v2 ; la v1, `verifier-gardes-du-lanceur-v1.sh`, reste telle quelle).
# Usage : bash verifier-gardes-du-lanceur-v2.sh DEPOT COMMIT_DU_CODE REGISTRE_GO.md CONFIG_ETALONNAGE.json
#   DEPOT : dépôt local qui porte l'objet COMMIT_DU_CODE (ici 43d6d0673edd5055917f536e5310ea99c15ab75e ; les correctifs 0014 à 0021
#   ne touchent pas ces contrôles, d'après leurs listes de fichiers et le constat du développeur) ; REGISTRE_GO.md : registres/go.md
#   de main, à une tête qui porte GO-2026-11-22-75 ; CONFIG_ETALONNAGE.json : configuration scellée de l'étalonnage (pour son calendrier).
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
echo "== 2. dépense antérieure : plafond de la configuration 55, ligne GO-2026-11-22-75, jour 2026-11-23"
for a in 0 4.20 5 5.01 5.52 9.65; do echo "-- antérieure $a"; python3 -I -B -c "$S5" go "$REG" GO-2026-11-22-75 55 "$a" 2026-11-23; echo "code $?"; done
echo "== 3. variante de plafond de la configuration scellée (B : 60 USD) contre le plafond de la ligne"
python3 -I -B -c "$S5" variante "$CFG" 60; echo "code $?"
echo "== 4. calendrier de la configuration scellée, ligne GO-2026-11-22-75 à 60 USD"
for j in 2026-11-23 2026-11-26 2026-11-27; do echo "-- jour $j"; python3 -I -B -c "$S3" calendrier "$CFG" "$REG" GO-2026-11-22-75 60 "$j"; echo "code $?"; done
echo "== 5. épuisement calculé : plafond 55, carte 1.30, stockage 0.08, téléchargement 2, création à l'instant 1000000000 ; antérieure 0 puis 5"
for a in 0 5; do python3 -I -B -c "$S3" depense 55 1.30 0.08 1000000000 "$a" 2 1000000000; echo "code $?"; done
