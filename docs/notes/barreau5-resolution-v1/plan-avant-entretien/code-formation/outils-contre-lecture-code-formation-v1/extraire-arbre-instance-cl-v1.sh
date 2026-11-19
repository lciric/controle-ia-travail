#!/usr/bin/env bash
# Outil du contre-lecteur (Fable 5.2) du code de formation du barreau 5 — v1, 19 novembre 2026.
# Rejoue, hors du dépôt, l'extraction partielle que fait l'amorce sur l'instance (étape 2) : clone local sans copie
# d'objets, motifs lus dans le bloc « motifs » de l'amorce, commit donné. Le dépôt d'origine n'est jamais modifié.
# Usage : extraire-arbre-instance-cl-v1.sh DEPOT DESTINATION COMMIT [MOTIF_DE_PLUS ...]
#   Les motifs de plus servent à la copie de travail des mutations (essais du lanceur et de l'amorce, garde de calcul).
set -euo pipefail
DEPOT="$1"; DEST="$2"; COMMIT="$3"; shift 3
[ ! -e "$DEST" ] || { echo "REFUS : $DEST existe déjà"; exit 2; }
MOTIFS="$(awk '/^# >>> motifs/{f=1; next} /^# <<< motifs/{f=0} f' "$DEPOT/scripts/amorce_b5f_formation_v1.sh" \
    | sed -e "1s/^MOTIFS='//" -e "\$s/'\$//")"
for m in "$@"; do MOTIFS="$MOTIFS
$m"; done
git clone -q --shared --no-checkout "$DEPOT" "$DEST"
git -C "$DEST" sparse-checkout init --no-cone
printf '%s\n' "$MOTIFS" | git -C "$DEST" sparse-checkout set --no-cone --stdin
git -C "$DEST" checkout -q "$COMMIT"
echo "tête : $(git -C "$DEST" rev-parse HEAD)"
echo "motifs :"; printf '%s\n' "$MOTIFS" | sed 's/^/  /'
echo "dossiers de premier niveau extraits : $(cd "$DEST" && ls -d */ | tr '\n' ' ')"
echo "fichiers extraits : $(cd "$DEST" && git ls-files -t | grep -c '^H')"
for d in docs/notes diag runs brouillons; do [ -e "$DEST/$d" ] && echo "PRÉSENT (ne devrait pas) : $d" || echo "absent : $d"; done
