#!/usr/bin/env bash
# essai_lecture_bac_v1.sh — essai Lean, D-1a, v7 (R-2415). Essai R5 « bac lit Mathlib.olean », joué par le pilote v7 à la fin
# de la phase « avant » (réseau encore ouvert, avant la coupure), en root sur la machine.
#   - cas sain : UTILISATEUR lit vraiment OLEAN (un octet lu par `head`, pas seulement les droits) ;
#   - témoin sain : un fichier 0644 d'un dossier temporaire 0755 est lu par UTILISATEUR ;
#   - artefact : un fichier 0600 (propriétaire root) du même dossier n'est PAS lu par UTILISATEUR (l'essai sait voir l'échec
#     qui a arrêté le premier essai).
# Une ligne JSON par cas ; code 0 si les trois sont conformes, 1 sinon (le pilote s'arrête, set -e). Aucun réseau.
# Usage : essai_lecture_bac_v1.sh [OLEAN] [UTILISATEUR]   (par défaut : Mathlib.olean de /opt/mathlib, bac)
set -euo pipefail
OLEAN=${1:-/opt/mathlib/.lake/build/lib/lean/Mathlib.olean}
U=${2:-bac}
[ "$(id -u)" = 0 ] || { echo '{"cas": "usage", "conforme": false, "motif": "root exigé (runuser)"}'; exit 1; }
lit() { runuser -u "$U" -- head -c 1 "$1" >/dev/null 2>&1; }
ligne() { printf '{"cas": "%s", "chemin": "%s", "attendu": "%s", "lu": %s, "conforme": %s}\n' "$1" "$2" "$3" "$4" "$5"; }
T=$(mktemp -d /tmp/essai-lecture-bac-XXXXXXXX)
trap 'rm -rf -- "${T:?}"' EXIT
chmod 0755 "$T"
printf 'x' > "$T/sain-0644"; chmod 0644 "$T/sain-0644"
printf 'x' > "$T/artefact-0600"; chmod 0600 "$T/artefact-0600"
ok=1
if lit "$OLEAN"; then ligne sain "$OLEAN" lu true true; else ligne sain "$OLEAN" lu false false; ok=0; fi
if lit "$T/sain-0644"; then ligne temoin-0644 "$T/sain-0644" lu true true; else ligne temoin-0644 "$T/sain-0644" lu false false; ok=0; fi
if lit "$T/artefact-0600"; then ligne artefact-0600 "$T/artefact-0600" refuse true false; ok=0; else ligne artefact-0600 "$T/artefact-0600" refuse false true; fi
[ "$ok" = 1 ] || { echo '{"cas": "bilan", "conforme": false, "motif": "lecture par l utilisateur du bac non conforme : arrêt"}'; exit 1; }
echo '{"cas": "bilan", "conforme": true}'
