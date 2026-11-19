#!/bin/bash
# Serveur d'INVENTAIRE PAR INSTANTANÉ d'un poste Hetzner du témoin de Bailey — v2 (R12 ; la v1 reste telle quelle).
# Mot de Lazar (19 novembre 2026, vers 08:47Z), verbatim : « avant toute destruction, inventaire et versement scellé de
# tout ce qui reste sur la machine » ; « Poste et instance Vast ».
# Ce serveur est créé depuis l'instantané (snapshot Hetzner) du disque du poste CIBLE, éteint avant l'instantané. Ses
# données de démarrage ne portent AUCUN secret : il pousse avec la clé de déploiement présente sur le disque copié.
# v2 (contre-lecture de la v1, rendue le 19 novembre vers 10:15Z) : aucun CONTENU de fichier du poste n'est versé sur la
# branche, sauf ses journaux texte nettoyés des valeurs exactes de ses clés puis recontrôlés. L'instantané, protégé et gardé
# jusqu'à la clôture, est le versement des contenus ; la branche reçoit sa description scellée :
#   1. l'inventaire de tous les fichiers du disque copié (chemin, taille, date, classe) ;
#   2. l'index des empreintes sha256 des fichiers hors système, hors objets git, hors environnements Python et hors
#      secrets (les secrets ne sont que nommés, avec leur taille) ;
#   3. l'état de git du dépôt cloné sur le poste, en noms seulement (statut, fichiers suivis modifiés, commits non
#      poussés, rebase ou fusion en cours) ;
#   4. les journaux texte `/root/*.log` antérieurs à l'arrêt, nettoyés des valeurs exactes, puis contrôlés (clés
#      privées, jetons, formes base64 et hexadécimales des valeurs) : refusés et seulement nommés au moindre doute ;
#   5. le journal de ce serveur, nettoyé de même, et une marque qui dit ce qui a tourné.
# Classes de date : « écrit par ce serveur » (date au moins égale au démarrage de ce serveur) ; « anomalie » (date entre
# l'arrêt du poste et ce démarrage) ; sinon fichier du poste. Aucune note n'est lue : les fichiers ne sont qu'empreintés,
# sauf les journaux du poste, qui ne portent aucune note.
set -uo pipefail
CIBLE=@@CIBLE@@
HEURE_ARRET=@@HEURE@@
BRANCHE=claude/compassionate-meitner-d4ryyk
DEPOT_POSTE=/home/user/controle-ia-travail
T=/root/travail-inventaire-instantane-v2
LOG=/var/log/inventaire-instantane-v2.log
exec >>"$LOG" 2>&1
echo "début $(date -u +%FT%TZ)"
case "$CIBLE" in ""|*[!a-z0-9-]*) echo "cible mal formée ou non remplie"; exit 3;; esac
case "$HEURE_ARRET" in ""|*[!0-9]*) echo "heure d'arrêt mal formée ou non remplie"; exit 3;; esac
BOOT=$(awk '/^btime /{print $2}' /proc/stat)
[ -n "$BOOT" ] && [ "$HEURE_ARRET" -lt "$BOOT" ] || { echo "heure d'arrêt non antérieure au démarrage ($HEURE_ARRET, $BOOT)"; exit 3; }
rm -rf "$T"; mkdir -p "$T"

# 1. inventaire brut du disque copié, séparé par NUL (noms avec tabulation ou saut de ligne compris)
find / \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -type f -printf '%s\t%T@\t%p\0' 2>/dev/null \
  > "$T/inventaire0"
[ -s "$T/inventaire0" ] || { echo "inventaire vide"; exit 3; }

# 2. état de git du dépôt du poste, en noms seulement
G=(git -C "$DEPOT_POSTE")
if [ -d "$DEPOT_POSTE/.git" ]; then
  {
    echo "# état de git du dépôt $DEPOT_POSTE (disque copié du poste $CIBLE) ; noms seulement"
    echo "## HEAD"; "${G[@]}" rev-parse HEAD 2>&1; "${G[@]}" symbolic-ref -q HEAD 2>&1 || echo "HEAD détachée"
    echo "## opérations en cours"
    for e in rebase-merge rebase-apply MERGE_HEAD CHERRY_PICK_HEAD; do [ -e "$DEPOT_POSTE/.git/$e" ] && echo "$e présent"; done
    echo "## commits non poussés (HEAD et branches, hors distantes)"
    "${G[@]}" log --format='%H %cI %s' HEAD --branches --not --remotes 2>&1
    echo "## fichiers suivis modifiés ou indexés, non commités (git diff --name-status HEAD)"
    "${G[@]}" diff --name-status HEAD 2>&1
    echo "## statut (porcelaine, ignorés compris)"
    "${G[@]}" status --porcelain=v1 --ignored 2>&1
  } > "$T/git-etat.txt"
else
  echo "pas de dépôt cloné sur ce disque" > "$T/git-etat.txt"
fi

# 3. classement, empreintes, journaux nettoyés
timeout 7200 python3 - "$T" "$HEURE_ARRET" "$BOOT" "$DEPOT_POSTE" <<'EOF' || { echo "classement en échec"; exit 3; }
import base64, binascii, hashlib, os, re, stat, sys
T, arret, boot, depot = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4].rstrip("/") + "/"
RACINES = ("/root/", "/home/", "/tmp/", "/var/tmp/", "/var/log/", "/opt/", "/srv/")
SECRETS_CHEMINS = ("/root/.ssh/", "/root/secrets.env", "/var/lib/cloud/", "/root/.config/vastai/")
MOTS = ("token", "secret", "credential", "jeton", "apikey", "api_key", "password", "passwd")
NOMS = {".vast_api_key", "vast_api_key", ".netrc", ".pypirc", ".git-credentials", "kaggle.json", "secrets.env"}
# valeurs exactes des clés, lues sur le disque copié (R5 : absence = refus, jamais de repli silencieux)
valeurs = []
try:
    for l in open("/root/secrets.env", encoding="utf-8"):
        if "=" in l:
            valeurs.append(l.split("=", 1)[1].strip().strip("'\""))
    for k in ("/root/.ssh/deploiement", "/root/.ssh/id_ed25519"):
        corps = [l.strip() for l in open(k, encoding="utf-8") if l.strip() and "-----" not in l]
        if not corps:
            raise ValueError(k)
        valeurs += [l for l in corps if len(l) >= 40]
except (OSError, ValueError) as e:
    print(f"valeurs des clés illisibles ({type(e).__name__}) : refus"); sys.exit(1)
valeurs = [v for v in valeurs if len(v) >= 16]
if len(valeurs) < 3:
    print("moins de trois valeurs de clés lues : refus"); sys.exit(1)
formes = set()
for v in valeurs:
    b = v.encode()
    for x in (b, b.upper(), b.lower(), binascii.hexlify(b), binascii.hexlify(b).upper()):
        formes.add(x)
    for dec in (0, 1, 2):  # noyaux base64 (alphabets standard et URL), décalages 0, 1, 2
        e = base64.b64encode(b"\0" * dec + b)[4 if dec else 0:]
        noyau = e[: max(0, len(e) - 4)]
        if len(noyau) >= 16:
            formes.add(noyau); formes.add(noyau.replace(b"+", b"-").replace(b"/", b"_"))
motifs = [re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"), re.compile(rb"hf_[A-Za-z0-9]{30,}"),
          re.compile(rb"ghp_[A-Za-z0-9]{30,}"), re.compile(rb"github_pat_[A-Za-z0-9_]{30,}"),
          re.compile(rb"(?i)(api[_-]?key|token|secret|password)['\"]?\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{20,}"),
          re.compile(rb"(?i)bearer\s+[A-Za-z0-9._-]{20,}")]
def secret_chemin(c):
    n = os.path.basename(c).lower()
    return (c.startswith(SECRETS_CHEMINS) or n in NOMS or any(m in n for m in MOTS) or n.endswith((".pem", ".key", ".env"))
            or (n.startswith(("id_rsa", "id_ed25519", "id_ecdsa")) and not n.endswith(".pub")) or c.startswith("/tmp/jeton-"))
def ech(c):
    return c.replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n")
entrees = open(os.path.join(T, "inventaire0"), "rb").read().split(b"\0")
comptes = {}
inv = open(os.path.join(T, "inventaire.tsv"), "w", encoding="utf-8", errors="surrogateescape")
idx = open(os.path.join(T, "empreintes-disque.txt"), "w", encoding="utf-8", errors="surrogateescape")
journaux = []
for e in entrees:
    if not e:
        continue
    try:
        s, d, c = e.split(b"\t", 2)
        taille, date, chemin = int(s), float(d), c.decode("utf-8", "surrogateescape")
    except ValueError:
        comptes["ligne illisible"] = comptes.get("ligne illisible", 0) + 1; continue
    if date >= boot:
        classe = "écrit par ce serveur"
    elif date >= arret:
        classe = "anomalie : écrit entre l'arrêt du poste et ce démarrage"
    elif not chemin.startswith(RACINES):
        classe = "système"
    elif secret_chemin(chemin):
        classe = "secret : nommé, sans empreinte"
    elif "/.git/" in chemin:
        classe = "objets git"
    elif "/.venv/" in chemin or "/venv/" in chemin or "/site-packages/" in chemin or "/__pycache__/" in chemin:
        classe = "environnement Python"
    else:
        classe = "poste"
    comptes[classe] = comptes.get(classe, 0) + 1
    inv.write(f"{ech(chemin)}\t{taille}\t{date:.0f}\t{classe}\n")
    if classe in ("poste", "anomalie : écrit entre l'arrêt du poste et ce démarrage"):
        try:
            if not stat.S_ISREG(os.lstat(chemin).st_mode):
                continue
            h = hashlib.sha256()
            with open(chemin, "rb") as f:
                for bloc in iter(lambda: f.read(1 << 20), b""):
                    h.update(bloc)
            idx.write(f"{h.hexdigest()}  {ech(chemin)}\n")
        except OSError:
            comptes["empreinte impossible"] = comptes.get("empreinte impossible", 0) + 1
    if (classe == "poste" and os.path.dirname(chemin) == "/root" and chemin.endswith(".log") and taille <= 25 * 2**20):
        journaux.append(chemin)
inv.close(); idx.close()
# journaux texte du poste : nettoyés des valeurs exactes, puis recontrôlés ; refusés au moindre doute
os.makedirs(os.path.join(T, "journaux"), exist_ok=True)
rapport = open(os.path.join(T, "journaux-rapport.tsv"), "w", encoding="utf-8")
for j in journaux:
    b = open(j, "rb").read()
    origine = hashlib.sha256(b).hexdigest()
    if b"\0" in b:
        rapport.write(f"{ech(j)}\t{origine}\trefusé : binaire\n"); continue
    try:
        b.decode("utf-8")
    except UnicodeDecodeError:
        rapport.write(f"{ech(j)}\t{origine}\trefusé : texte non UTF-8\n"); continue
    n = 0
    for v in sorted(valeurs, key=len, reverse=True):
        for x in {v.encode(), v.encode().upper(), v.encode().lower()}:
            n += b.count(x); b = b.replace(x, b"[retire]")
    if any(x in b for x in formes) or any(m.search(b) for m in motifs):
        rapport.write(f"{ech(j)}\t{origine}\trefusé : forme encodée ou motif après nettoyage\n"); continue
    nom = os.path.basename(j)
    open(os.path.join(T, "journaux", nom), "wb").write(b)
    rapport.write(f"{ech(j)}\t{origine}\tversé, {n} valeur(s) exacte(s) remplacée(s)\n")
rapport.close()
with open(os.path.join(T, "comptes.tsv"), "w", encoding="utf-8") as f:
    for k, v in sorted(comptes.items()):
        f.write(f"{k}\t{v}\n")
print("comptes :", comptes, "; journaux :", len(journaux))
EOF

# 4. versement préparé à part ($T/depot), puis déposé sur la tête fraîche de la branche à chaque essai
R=runs/temoin-bailey-v1-20261111
V="$R/versement-$CIBLE-v2"; M="$R/poste-fini-inventaire-instantane-$CIBLE-v2.json"
D="$T/depot"; rm -rf "$D"; mkdir -p "$D/$V/journaux"
gzip -n -c "$T/inventaire.tsv" > "$D/$V/inventaire-disque.tsv.gz"
cp "$T/empreintes-disque.txt" "$T/git-etat.txt" "$T/journaux-rapport.tsv" "$T/comptes.tsv" "$D/$V/"
[ -d "$T/journaux" ] && cp -r "$T/journaux/." "$D/$V/journaux/"
INST=$(cat /var/lib/cloud/data/instance-id 2>/dev/null); PREC=$(cat /var/lib/cloud/data/previous-instance-id 2>/dev/null)
SCRIPT_SHA=$(sha256sum /var/lib/cloud/instance/user-data.txt 2>/dev/null | cut -d' ' -f1)
INDEX_SHA=$(sha256sum "$D/$V/empreintes-disque.txt" | cut -d' ' -f1)
NP=$(git -C "$DEPOT_POSTE" log --format=%H HEAD --branches --not --remotes 2>/dev/null | wc -l)
# journal de ce serveur, nettoyé des valeurs exactes et contrôlé (sinon remplacé par une ligne de refus)
python3 - "$LOG" "$D/$V/journal-serveur-inventaire-v2.log" <<'EOF'
import re, sys
vals = []
try:
    for l in open("/root/secrets.env", encoding="utf-8"):
        if "=" in l:
            vals.append(l.split("=", 1)[1].strip().strip("'\""))
except OSError:
    pass
b = open(sys.argv[1], "rb").read()
for v in sorted((v for v in vals if len(v) >= 16), key=len, reverse=True):
    for x in {v.encode(), v.encode().upper(), v.encode().lower()}:
        b = b.replace(x, b"[retire]")
if re.search(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----|hf_[A-Za-z0-9]{30,}|ghp_[A-Za-z0-9]{30,}|github_pat_", b):
    b = b"journal refuse : motif de secret\n"
open(sys.argv[2], "wb").write(b)
EOF
printf '{"cible": "%s", "heure_arret": %s, "demarrage": %s, "instance": "%s", "instance_precedente": "%s", "script_sha256": "%s", "index_sha256": "%s", "commits_non_pousses": %s, "fini": "%s"}\n' \
  "$CIBLE" "$HEURE_ARRET" "$BOOT" "$INST" "$PREC" "$SCRIPT_SHA" "$INDEX_SHA" "$NP" "$(date -u +%FT%TZ)" > "$D/$M"
(cd "$D/$V" && find . -type f ! -name '*.sha256' -print0 | while IFS= read -r -d '' f; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done)
(cd "$D/$R" && sha256sum "$(basename "$M")" > "$(basename "$M").sha256")
NB=$(cd "$D" && find "$V" "$M" "$M.sha256" -type f | wc -l)

export GIT_SSH_COMMAND="ssh -i /root/.ssh/deploiement -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
CLONE=/root/clone-inventaire-instantane-v2
for i in 1 2 3 4 5; do
  rm -rf "$CLONE"
  git clone -q --depth 1 --single-branch --branch "$BRANCHE" git@github.com:lciric/controle-ia-travail.git "$CLONE" && break
  sleep $((30 * i))
done
[ -d "$CLONE/.git" ] || { echo "clonage en échec"; exit 3; }
cd "$CLONE"; git config user.name "Claude"; git config user.email "noreply@anthropic.com"
deposer() {  # dépose le versement sur la tête fraîche ; 0 si poussé
  git fetch -q --depth 1 origin "$BRANCHE" || return 1
  git checkout -q --detach FETCH_HEAD || return 1
  [ ! -e "$V" ] && [ ! -e "$M" ] || { echo "versement ou marque déjà présents sur la branche (R12)"; return 9; }
  cp -r "$D/." "$CLONE/" || return 1
  git add -A -f -- "$V" "$M" "$M.sha256" || return 1
  [ "$(git diff --cached --name-only | wc -l)" -eq "$NB" ] || { echo "nombre de fichiers indexés différent du versement préparé"; return 9; }
  git commit -q -m "Témoin de Bailey : inventaire par instantané du poste $CIBLE (description scellée ; contenus dans l'instantané)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XJ6MgnEhQMZteN9F8a1BST" || return 1
  git push -q origin "HEAD:$BRANCHE"
}
ok=0
for i in $(seq 1 60); do
  deposer; c=$?
  [ "$c" -eq 0 ] && { ok=1; break; }
  [ "$c" -eq 9 ] && break
  git reset -q --hard 2>/dev/null; git clean -qfdx 2>/dev/null; sleep 60
done
[ "$ok" -eq 1 ] || { echo "poussée en échec ou refus (R12)"; exit 3; }
echo "poussé ($NB fichiers) ; fin $(date -u +%FT%TZ)"
