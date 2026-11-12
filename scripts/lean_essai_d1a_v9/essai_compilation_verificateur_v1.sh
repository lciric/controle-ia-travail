#!/usr/bin/env bash
# essai_compilation_verificateur_v1.sh — essai Lean, D-1a, réparation R-2439 (cause du second essai, R-2438 : le vérificateur
# du noyau ne compilait pas sous Lean 4.35.0, vu seulement après la coupure). Essai R5 « le vérificateur compile sur la
# machine », joué par le pilote v9 à la fin de la phase « avant » (réseau encore ouvert, **avant la coupure**), en root :
#   - cas sain : VERIFICATEUR, copié 0644 dans un dossier temporaire 0755, est compilé par UTILISATEUR avec le `lean` et le
#     `LEAN_PATH` de la chaîne installée (CHAINE, écrit par installer_chaine_v2.sh) : code 0 **et aucun message** (un
#     avertissement sortirait sur la sortie standard de `lean --run` et ferait échouer G-L7) ;
#   - artefact : une copie volontairement cassée du même fichier (une ligne ajoutée à la fin qui cite un identifiant inconnu)
#     ne compile pas : code non nul et message `error` (l'essai sait voir l'échec qui a arrêté le second essai).
# Une ligne JSON par cas, puis un bilan ; code 0 si les deux cas sont conformes, 1 sinon (le pilote s'arrête, set -e, avant la
# coupure et avant toute suite). Aucun réseau. Si UTILISATEUR est l'utilisateur courant, pas de runuser (essais hors machine).
# Usage : essai_compilation_verificateur_v1.sh [VERIFICATEUR] [CHAINE] [UTILISATEUR]
#   (par défaut : /root/verificateur_noyau_v5.lean, /opt/harnais/chaine-v1.json, bac)
set -euo pipefail
V=${1:-/root/verificateur_noyau_v5.lean}
CH=${2:-/opt/harnais/chaine-v1.json}
U=${3:-bac}
champ() { python3 -c 'import json, sys; print(json.load(open(sys.argv[1], encoding="utf-8"))[sys.argv[2]])' "$CH" "$1"; }
ligne() {
  python3 -c 'import json, sys; c, f, h, a, r, m, ok = sys.argv[1:8]; print(json.dumps({"cas": c, "fichier": f, "sha256": h, "attendu": a, "code": int(r), "messages": m[:2000], "conforme": ok == "1"}, ensure_ascii=False))' "$@"
}
LEAN=$(champ lean)
LP=$(champ lean_path)
if [ "$U" = "$(id -un)" ]; then lancer() { "$@"; }; else lancer() { runuser -u "$U" -- "$@"; }; fi
compiler() { (cd "$T" && lancer env -i HOME=/tmp PATH=/usr/bin:/bin LANG=C.UTF-8 LEAN_PATH="$LP" "$LEAN" "$1" 2>&1); }
T=$(mktemp -d /tmp/essai-compilation-verificateur-XXXXXXXX)
trap 'rm -rf -- "${T:?}"' EXIT
chmod 0755 "$T"
install -m 0644 "$V" "$T/sain.lean"
install -m 0644 "$V" "$T/casse.lean"
printf '\nexample : Nat := identifiantInconnuEssaiR5V1\n' >> "$T/casse.lean"
ok=1
if out=$(compiler "$T/sain.lean"); then rc=0; else rc=$?; fi
if [ "$rc" = 0 ] && [ -z "$out" ]; then c=1; else c=0; ok=0; fi
ligne sain "$V" "$(sha256sum "$T/sain.lean" | cut -d' ' -f1)" "compile sans message" "$rc" "$out" "$c"
if out=$(compiler "$T/casse.lean"); then rc=0; else rc=$?; fi
if [ "$rc" != 0 ] && grep -q 'error' <<< "$out"; then c=1; else c=0; ok=0; fi
ligne artefact-copie-cassee "$V (copie cassée)" "$(sha256sum "$T/casse.lean" | cut -d' ' -f1)" "refusée" "$rc" "$out" "$c"
VERSION_LEAN=$("$LEAN" --version 2>&1) || { VERSION_LEAN="lean --version en échec : $VERSION_LEAN"; ok=0; }
[ "$ok" = 1 ] || { python3 -c 'import json, sys; print(json.dumps({"cas": "bilan", "conforme": False, "version_lean": sys.argv[1], "motif": "le vérificateur ne compile pas sans message sur la machine, ou la copie cassée n est pas refusée : arrêt avant la coupure"}, ensure_ascii=False))' "$VERSION_LEAN"; exit 1; }
python3 -c 'import json, sys; print(json.dumps({"cas": "bilan", "conforme": True, "version_lean": sys.argv[1]}, ensure_ascii=False))' "$VERSION_LEAN"
