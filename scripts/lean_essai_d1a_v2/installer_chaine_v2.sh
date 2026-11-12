#!/usr/bin/env bash
# installer_chaine_v2.sh — essai Lean, D-1a, v2 (R-2415). Corps de installer_chaine_v1.sh (inchangé, R12), plus une seule
# correction : le premier essai sur machine s'est arrêté au pas `noyau` (0/18) parce que les fichiers compilés de Mathlib tirés
# du cache sont en -rw------- ; après `chown chaine` et `chmod go-w`, `bac` ne lisait pas Mathlib.olean (rapport du poste local
# rapport-poste-local-d1a-v1.md, branche donnees/lean-outillage-d1a-poste-local-v1). La v2 ajoute :
#   - `chmod -R a+rX` sur /opt/elan, /opt/mathlib, /opt/pybac, après `go-w` et avant le montage en lecture seule ;
#   - une garde qui arrête l'installation (code 5, message dans le journal) si un fichier ou un dossier de ces arbres n'est
#     pas lisible par les autres, si un dossier n'est pas traversable, si un exécutable ne l'est pas pour les autres, ou si
#     `bac` (par runuser) ne lit pas un échantillon : /opt, /opt/harnais, les trois racines, Mathlib.olean, le Python du bras S,
#     les dossiers existants de LEAN_PATH ; et ne peut exécuter ni lean ni ce Python.
# Les noms des fichiers écrits (journal-installation-v1.txt, chaine-v1.json) sont gardés : le harnais les lit sous ces noms.
# Texte de la v1 :
# installer_chaine_v1.sh — essai Lean, D-1a, v1 (brouillon 3, § 4.5, VL-05).
# Sur la machine dédiée, en root, **réseau ouvert** : paquets (bwrap, nftables), utilisateurs `chaine` (propriétaire de la
# chaîne) et `bac` (sans privilège, exécute les items), elan, Mathlib au commit épinglé avec son cache, environnement Python du
# bras S aux versions de `.venv`, puis chaîne, Mathlib et Python en **lecture seule** (propriétaire distinct, montage lié en
# lecture seule, inscrit dans /etc/fstab), dossiers du bac. Aucun secret, aucune clé, aucun fichier du programme.
# Usage : installer_chaine_v2.sh COMMIT_MATHLIB   (40 caractères hexadécimaux, choisi par choisir_commit_mathlib_v1.sh)
set -euo pipefail
COMMIT="${1:?commit de Mathlib exigé}"
[[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "commit invalide : $COMMIT" >&2; exit 2; }
install -d -m 0755 /opt/harnais
J=/opt/harnais/journal-installation-v1.txt
etape() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*" | tee -a "$J"; }
# --- garde de lisibilité par bac (v2) : début ---
# arbres_lisibles_par_tous ARBRE... : imprime les chemins fautifs (fichier ou dossier sans lecture pour les autres, dossier
# sans traversée pour les autres, fichier exécutable par son propriétaire mais pas par les autres) ; code 0 si aucun, 1 sinon,
# 2 si `find` échoue (arbre absent, lecture impossible). Les liens symboliques ne sont pas jugés (leur cible l'est).
arbres_lisibles_par_tous() {
  local fautifs
  fautifs=$(find "$@" \( \( -type f -o -type d \) ! -perm -o=r \) -o \( -type d ! -perm -o=x \) \
                 -o \( -type f -perm -u=x ! -perm -o=x \) ) || { echo "find en échec sur : $*"; return 2; }
  [ -z "$fautifs" ] && return 0
  echo "$(wc -l <<< "$fautifs") chemin(s), dont : $(head -5 <<< "$fautifs" | tr '\n' ' ')"
  return 1
}
# lisibles_par UTILISATEUR CHEMIN... : chaque fichier lu, chaque dossier lu et traversé par UTILISATEUR (runuser, sans shell) ;
# imprime le premier fautif ; code 0 si tous, 1 sinon.
lisibles_par() {
  local u=$1 c; shift
  for c in "$@"; do
    runuser -u "$u" -- test -r "$c" || { echo "$c : non lisible par $u"; return 1; }
    if [ -d "$c" ]; then runuser -u "$u" -- test -x "$c" || { echo "$c : dossier non traversable par $u"; return 1; }; fi
  done
  return 0
}
# --- garde de lisibilité par bac (v2) : fin ---
etape "début ; noyau $(uname -r) ; $(. /etc/os-release; echo "$PRETTY_NAME") ; $(nproc) cœurs ; $(free -b | awk '/Mem:/{print $2}') octets de mémoire"
export DEBIAN_FRONTEND=noninteractive
apt-get update -q >/dev/null && apt-get install -y -q bubblewrap nftables python3-venv git curl time ca-certificates >/dev/null
etape "paquets : $(bwrap --version) ; $(nft --version) ; $(systemctl --version | head -1)"
echo 'kernel.apparmor_restrict_unprivileged_userns=0' > /etc/sysctl.d/60-bac-userns.conf
sysctl --system >/dev/null
id chaine >/dev/null 2>&1 || useradd --system --home-dir /nonexistent --shell /usr/sbin/nologin chaine
id bac >/dev/null 2>&1 || useradd --system --home-dir /nonexistent --shell /usr/sbin/nologin bac
curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /root/elan-init.sh
ELAN_SHA=$(sha256sum /root/elan-init.sh | cut -d' ' -f1)
etape "elan-init.sh sha256 $ELAN_SHA"
ELAN_HOME=/opt/elan sh /root/elan-init.sh -y --default-toolchain none --no-modify-path >/dev/null
export ELAN_HOME=/opt/elan PATH=/opt/elan/bin:$PATH
etape "$(elan --version)"
git clone --quiet https://github.com/leanprover-community/mathlib4.git /opt/mathlib
cd /opt/mathlib
git -c advice.detachedHead=false checkout --quiet "$COMMIT"
[ "$(git rev-parse HEAD)" = "$COMMIT" ] || { etape "ARRÊT : HEAD différent du commit épinglé"; exit 3; }
TC=$(cat lean-toolchain)
etape "commit de Mathlib $COMMIT ; lean-toolchain $TC"
t0=$(date +%s); lake exe cache get 2>&1 | tail -2 | tee -a "$J"; t1=$(date +%s)
etape "cache de Mathlib téléchargé et décompressé : $((t1 - t0)) s"
t0=$(date +%s); lake build 2>&1 | tail -2 | tee -a "$J"; t1=$(date +%s)
etape "lake build (contrôle que rien ne se reconstruit) : $((t1 - t0)) s"
LEAN=$(elan which lean)
LEAN_PATH_VAL=$(lake env printenv LEAN_PATH)
VERSION_LEAN=$("$LEAN" --version)
etape "lean $LEAN ; $VERSION_LEAN"
python3 -m venv /opt/pybac
/opt/pybac/bin/pip install -q sympy==1.14.0 mpmath==1.3.0 numpy==2.4.6 scipy==1.17.1
VERSIONS_PY=$(/opt/pybac/bin/python -c 'import sys,sympy,mpmath,numpy,scipy;print(sys.version.split()[0],sympy.__version__,mpmath.__version__,numpy.__version__,scipy.__version__)')
etape "python du bras S : $VERSIONS_PY"
etape "tailles (octets) : mathlib $(du -sb /opt/mathlib | cut -f1) ; dont .lake $(du -sb /opt/mathlib/.lake | cut -f1) ; elan $(du -sb /opt/elan | cut -f1) ; pybac $(du -sb /opt/pybac | cut -f1) ; disque libre $(df -B1 --output=avail / | tail -1)"
chown -R chaine:chaine /opt/elan /opt/mathlib /opt/pybac
chmod -R go-w /opt/elan /opt/mathlib /opt/pybac
chmod -R a+rX /opt/elan /opt/mathlib /opt/pybac
OLEAN=/opt/mathlib/.lake/build/lib/lean/Mathlib.olean
[ -f "$OLEAN" ] || { etape "ARRÊT : $OLEAN absent"; exit 5; }
if ! F=$(arbres_lisibles_par_tous /opt/elan /opt/mathlib /opt/pybac); then
  etape "ARRÊT : chaîne, Mathlib ou Python non lisibles par tous : $F"; exit 5
fi
ECHANTILLON=(/opt /opt/harnais /opt/elan /opt/mathlib /opt/pybac "$OLEAN" /opt/pybac/bin/python)
IFS=: read -ra ENTREES_LP <<< "$LEAN_PATH_VAL"
for e in "${ENTREES_LP[@]}"; do if [ -n "$e" ] && [ -e "$e" ]; then ECHANTILLON+=("$e"); fi; done
if ! F=$(lisibles_par bac "${ECHANTILLON[@]}"); then etape "ARRÊT : $F"; exit 5; fi
for x in "$LEAN" /opt/pybac/bin/python; do
  runuser -u bac -- test -x "$x" || { etape "ARRÊT : $x non exécutable par bac"; exit 5; }
done
etape "garde de lisibilité : aucun chemin fermé aux autres dans les trois arbres ; bac lit ${#ECHANTILLON[@]} chemins (dont Mathlib.olean) et exécute lean et python"
for d in /opt/elan /opt/mathlib /opt/pybac; do
  grep -q "^$d $d none bind,ro " /etc/fstab || echo "$d $d none bind,ro 0 0" >> /etc/fstab
done
systemctl daemon-reload
mount -a
for d in /opt/elan /opt/mathlib /opt/pybac; do
  findmnt -no OPTIONS "$d" | tr ',' '\n' | grep -qx ro || { etape "ARRÊT : $d n'est pas monté en lecture seule"; exit 4; }
done
etape "chaîne, Mathlib et Python en lecture seule (propriétaire chaine, montages liés ro)"
install -d -m 0755 -o root -g root /srv/items /srv/controle
install -d -m 0700 -o root -g root /srv/sorties /srv/leurre
python3 - "$LEAN" "$LEAN_PATH_VAL" "$VERSION_LEAN" "$COMMIT" "$TC" "$ELAN_SHA" "$VERSIONS_PY" <<'PY'
import json, sys
lean, lp, vl, commit, tc, elan_sha, vpy = sys.argv[1:8]
d = {"lean": lean, "lean_path": lp, "variante_enumeration": "", "python": "/opt/pybac/bin/python",
     "version_lean": vl, "commit_mathlib": commit, "lean_toolchain": tc, "elan_init_sha256": elan_sha,
     "versions_python": vpy}
open("/opt/harnais/chaine-v1.json", "w").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
PY
etape "fin ; /opt/harnais/chaine-v1.json écrit (variante d'énumération choisie après la coupure)"
