#!/usr/bin/env bash
# Vérification, sur processeur et sans dépense, des gardes du lanceur de session du saboteur à budget sous la ligne
# GO-2026-11-22-75, à l'arbre du code de la voie (A), qui porte les correctifs 0021 à 0025 — v4 ; les v1, v2 et v3 restent.
# Écrit par Claude Fable 5.2 (rédacteur), sur la v3 d'Opus 5.5, relue.
# Usage : bash verifier-gardes-du-lanceur-v4.sh DEPOT COMMIT_DU_CODE REGISTRE_GO.md CONFIG_ETALONNAGE.json CONFIG_VOIE.json
#   DEPOT : dépôt local qui porte l'objet COMMIT_DU_CODE (ici f7a5123e0fe8e55cfecbb0ac16b17eff50b0d4e1, correctif 0025) ;
#   REGISTRE_GO.md : registres/go.md de main, à une tête qui porte GO-2026-11-22-75 ;
#   CONFIG_ETALONNAGE.json : configuration scellée de l'étalonnage (08e22099…) ;
#   CONFIG_VOIE.json : configuration de la voie (A), avec ou sans entropie (variante de plafond et calendrier seuls lus).
# Changements à la v3 : aucun cas retiré ; le § 6 rejoue la variante et le calendrier sur la configuration de la voie ;
# l'archive du code est extraite sous TMPDIR. Sous le correctif 0024, les refus s'écrivent « 60 » et non « 60.0 ».
# Rien n'est créé, aucun loueur n'est appelé, aucune sortie de mesure n'est lue.
set -uo pipefail
DEPOT="${1:?dépôt}"; C="${2:?commit du code}"; REG="${3:?registre go.md}"; CFG="${4:?configuration étalonnage}"; CFV="${5:?configuration voie}"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
git -C "$DEPOT" archive "$C" src/controle_ia/iib src/controle_ia/t06 src/controle_ia/gardes.py src/controle_ia/__init__.py | tar -x -C "$T"
S5="import sys; sys.path.insert(0, '$T/src'); from controle_ia.iib import session_v5; sys.exit(session_v5.main(sys.argv[1:]))"
S3="import sys; sys.path.insert(0, '$T/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
echo "code $C, arbre $(git -C "$DEPOT" rev-parse "$C^{tree}") ; registre $(sha256sum "$REG" | cut -d' ' -f1) ; configuration de l'étalonnage $(sha256sum "$CFG" | cut -d' ' -f1) ; configuration de la voie $(sha256sum "$CFV" | cut -d' ' -f1)"
echo "== 1. plafond lu sur la ligne GO-2026-11-22-75"
python3 -I -B -c "$S5" plafond-ligne "$REG" GO-2026-11-22-75 2026-11-23; echo "code $?"
echo "== 2. dépense antérieure (correctifs 0023 et 0024) : plafond de la configuration 55, ligne GO-2026-11-22-75, jour 2026-11-23"
echo "   cas sains attendus en code 0 : 0, 4.20, 5, 5.01, 5.52, 9.65, 16.22, 59.99 ; artefacts attendus en code 1 : 60, 60.01, -1, nan, inf, illisible"
for a in 0 4.20 5 5.01 5.52 9.65 16.22 59.99 60 60.01 -1 nan inf illisible; do
  echo "-- antérieure $a"
  python3 -I -B -c "$S5" go "$REG" GO-2026-11-22-75 55 "$a" 2026-11-23; echo "code $?"
  printf 'plafond total : '; python3 -I -B -c "$S5" plafond-total "$REG" GO-2026-11-22-75 55 "$a" 2026-11-23; echo "code $?"
done
echo "== 2 bis. artefacts de la configuration et de la ligne : configuration 61 > ligne ; ligne absente"
python3 -I -B -c "$S5" go "$REG" GO-2026-11-22-75 61 0 2026-11-23; echo "code $?"
python3 -I -B -c "$S5" go "$REG" GO-2099-01-01-01 55 0 2026-11-23; echo "code $?"
echo "== 2 ter. correctif 0024 : plafond total écrit exact, jamais arrondi (antérieure 3.123456 : 58.123456 attendu)"
printf 'plafond total : '; python3 -I -B -c "$S5" plafond-total "$REG" GO-2026-11-22-75 55 3.123456 2026-11-23; echo "code $?"
echo "== 3. variante de plafond de la configuration scellée de l'étalonnage (B : 60 USD) contre le plafond de la ligne"
python3 -I -B -c "$S5" variante "$CFG" 60; echo "code $?"
echo "== 4. calendrier de la configuration scellée de l'étalonnage, ligne GO-2026-11-22-75 à 60 USD"
for j in 2026-11-23 2026-11-26 2026-11-27; do echo "-- jour $j"; python3 -I -B -c "$S3" calendrier "$CFG" "$REG" GO-2026-11-22-75 60 "$j"; echo "code $?"; done
echo "== 5. épuisement calculé sous le plafond total : carte 1.30, stockage 0.08, téléchargement 2, création à l'instant 1000000000"
for a in 0 5.52 9.65 16.22; do
  P=$(python3 -I -B -c "$S5" plafond-total "$REG" GO-2026-11-22-75 55 "$a" 2026-11-23) || { echo "plafond total refusé pour $a"; continue; }
  echo "-- antérieure $a, plafond total $P"
  python3 -I -B -c "$S3" depense "$P" 1.30 0.08 1000000000 "$a" 2 1000000000; echo "code $?"
done
echo "== 6. configuration de la voie (A) : variante de plafond, puis calendrier (cas sains les 23 et 26, artefact le 27)"
python3 -I -B -c "$S5" variante "$CFV" 60; echo "code $?"
for j in 2026-11-23 2026-11-26 2026-11-27; do echo "-- jour $j"; python3 -I -B -c "$S3" calendrier "$CFV" "$REG" GO-2026-11-22-75 60 "$j"; echo "code $?"; done
