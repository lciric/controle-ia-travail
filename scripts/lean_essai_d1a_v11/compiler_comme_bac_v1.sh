#!/usr/bin/env bash
# compiler_comme_bac_v1.sh — essai Lean D-1a, v11 (pas 2 de l'arbitrage, point 7) : compiler UN item hors machine
# exactement comme le bac le compile (executeur_bac_v6, Bac.verifier_lean, premier lancement) : même commande
#   lean --json --root=/item -o /item/Item.olean -i /item/Item.ilean /item/Item.lean
# même dossier courant (/item), même environnement (HOME=/tmp, PATH=/usr/bin:/bin, LANG=C.UTF-8, LEAN_PATH), item seul
# dans /item, /tmp neuf. L'isolement n'est PAS celui du bac (ni systemd, ni bwrap, ni utilisateur bac) : espaces de noms
# de montage, de réseau et de processus neufs, racine en mémoire, /usr et la chaîne en lecture seule, chroot. Il sert à
# lire la sortie de compilation sans que les tentatives d'un item sonde touchent l'hôte : toute écriture tombe dans la
# racine en mémoire, perdue à la sortie ; aucun réseau.
# Usage : compiler_comme_bac_v1.sh RACINE_CHAINE LEAN LEAN_PATH ITEM.lean DOSSIER_SORTIE
#   RACINE_CHAINE : dossier qui contient lean et Mathlib (monté en lecture seule au même chemin) ;
#   DOSSIER_SORTIE : reçoit compilation.out, compilation.err, code.txt, cpu.txt, inventaire.txt.
# Codes : celui de lean ; 2 usage.
set -euo pipefail
[ $# -eq 5 ] || { echo "usage : $0 RACINE_CHAINE LEAN LEAN_PATH ITEM.lean DOSSIER_SORTIE" >&2; exit 2; }
CHAINE=$(realpath "$1"); LEAN=$2; LP=$3; ITEM=$(realpath "$4"); SORTIE=$(realpath "$5")
[ -d "$CHAINE" ] && [ -x "$LEAN" ] && [ -f "$ITEM" ] && [ -d "$SORTIE" ] || { echo "argument invalide" >&2; exit 2; }
case "$LEAN" in "$CHAINE"/*) ;; *) echo "lean hors de RACINE_CHAINE" >&2; exit 2;; esac
D_ITEM=$(mktemp -d "$SORTIE/item.XXXXXX")
cp "$ITEM" "$D_ITEM/Item.lean"
export CHAINE LEAN LP D_ITEM SORTIE
set +e
unshare --mount --net --pid --fork --propagation private bash -c '
set -euo pipefail
R=$(mktemp -d "$SORTIE/racine.XXXXXX")
mount -t tmpfs -o size=1g,mode=0755 racine "$R"
mkdir -p "$R/usr" "$R/etc" "$R/proc" "$R/dev" "$R/tmp" "$R/item" "$R$CHAINE"
for l in bin lib lib64 sbin; do ln -s "usr/$l" "$R/$l"; done
mount --rbind /usr "$R/usr"; mount -o remount,ro,bind "$R/usr"
touch "$R/etc/ld.so.cache"; mount --bind /etc/ld.so.cache "$R/etc/ld.so.cache"
mount -t proc proc "$R/proc"
mount --rbind /dev "$R/dev"
mount --bind "$CHAINE" "$R$CHAINE"; mount -o remount,ro,bind "$R$CHAINE"
mount --bind "$D_ITEM" "$R/item"
chroot "$R" /usr/bin/env -i HOME=/tmp PATH=/usr/bin:/bin LANG=C.UTF-8 LEAN_PATH="$LP" /bin/sh -c \
  "cd /item && exec \"\$0\" --json --root=/item -o /item/Item.olean -i /item/Item.ilean /item/Item.lean" "$LEAN" \
  > "$SORTIE/compilation.out" 2> "$SORTIE/compilation.err"
'
CODE=$?
set -e
echo "$CODE" > "$SORTIE/code.txt"
ls -la "$D_ITEM" > "$SORTIE/inventaire.txt"
exit "$CODE"
