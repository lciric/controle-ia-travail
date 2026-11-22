#!/usr/bin/env bash
# Vérification, sur processeur et sans dépense, de quatre gardes du lanceur de session du saboteur à budget (v1).
# Usage : bash verifier-gardes-du-lanceur-v1.sh DEPOT COMMIT_DU_CODE REGISTRE_GO.md CONFIG_ETALONNAGE.json
#   DEPOT : dépôt local qui porte l'objet COMMIT_DU_CODE (ici 43d6d0673edd5055917f536e5310ea99c15ab75e, commit de lancement de l'étalonnage) ;
#   REGISTRE_GO.md : registres/go.md de main ; CONFIG_ETALONNAGE.json : configuration scellée de l'étalonnage au même commit.
# Rien n'est créé, aucun loueur n'est appelé, aucune sortie de mesure n'est lue. Les inventaires sont factices.
set -uo pipefail
DEPOT="${1:?dépôt}"; C="${2:?commit du code}"; REG="${3:?registre go.md}"; CFG="${4:?configuration}"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
git -C "$DEPOT" archive "$C" src/controle_ia/iib src/controle_ia/t06 src/controle_ia/gardes.py src/controle_ia/__init__.py | tar -x -C "$T"
S5="import sys; sys.path.insert(0, '$T/src'); from controle_ia.iib import session_v5; sys.exit(session_v5.main(sys.argv[1:]))"
S3="import sys; sys.path.insert(0, '$T/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
echo "code $C, arbre $(git -C "$DEPOT" rev-parse "$C^{tree}") ; registre $(sha256sum "$REG" | cut -d' ' -f1) ; configuration $(sha256sum "$CFG" | cut -d' ' -f1)"
echo "== 1. dépense antérieure : plafond de la configuration 55, ligne GO-2026-11-21-70, jour 2026-11-22"
for a in 0 5 5.01 16.3; do echo "-- antérieure $a"; python3 -I -B -c "$S5" go "$REG" GO-2026-11-21-70 55 "$a" 2026-11-22; echo "code $?"; done
echo "== 2. plafond lu sur la ligne"
for g in GO-2026-11-21-70 GO-2026-11-22-71; do echo "-- $g"; python3 -I -B -c "$S5" plafond-ligne "$REG" "$g" 2026-11-22; echo "code $?"; done
echo "== 3. instance du saboteur déjà sur le compte (inventaires factices)"
printf '[{"id": 111, "label": "iib-explo-v5", "actual_status": "exited", "cur_state": "stopped"}, {"id": 222, "label": "autre-chantier", "actual_status": "running", "cur_state": "running"}]' > "$T/arretee.json"
printf '[{"id": 222, "label": "autre-chantier", "actual_status": "running", "cur_state": "running"}]' > "$T/sans.json"
echo "-- une instance iib à l'arrêt"; python3 -I -B -c "$S5" instances "$T/arretee.json"; echo "code $?"
echo "-- aucune instance iib"; python3 -I -B -c "$S5" instances "$T/sans.json"; echo "code $?"
echo "== 4. calendrier de la configuration scellée, ligne GO-2026-11-21-70 à 60 USD"
for j in 2026-11-26 2026-11-27; do echo "-- jour $j"; python3 -I -B -c "$S3" calendrier "$CFG" "$REG" GO-2026-11-21-70 60 "$j"; echo "code $?"; done
echo "== 5. épuisement calculé : plafond 55, carte 1.30, stockage 0.08, antérieure 5, téléchargement 2, création à l'instant 1000000000"
python3 -I -B -c "$S3" depense 55 1.30 0.08 1000000000 5 2 1000000000; echo "code $?"
