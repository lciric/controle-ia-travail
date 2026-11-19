#!/bin/bash
# Poste Hetzner d'INVENTAIRE de l'instance Vast 61170458 — témoin de Bailey, relance de la confirmation — v2 (R12 ; la v1
# reste telle quelle). Mot de Lazar (19 novembre 2026, vers 08:47Z) : « avant toute destruction, inventaire et versement
# scellé de tout ce qui reste sur la machine » ; « Poste et instance Vast ».
# Défaut de la v1, constaté à sa passe 1 (09:42Z) : les fichiers étaient pris par ordre alphabétique sous un plafond de
# 400 Mio ; l'environnement Python /root/venv l'a rempli, et /root/x (répertoires de travail de la course, environ
# 1,2 Gio) n'a pas été copié. La v1 est éteinte (disque gardé), pas détruite.
# v2 = v1 avec : /root/venv, /opt, /usr, site-packages, __pycache__ et .venv hors copie (inventoriés) ; /root/x copié en
# premier ; plafond de 25 Mio par fichier et de 400 Mio par passe levés (2 Gio par fichier, 6 Gio en tout) ; copies
# gardées sur le disque de ce poste (/root/versement-local), jamais poussées : la branche ne reçoit que l'inventaire,
# les exclusions et l'index des empreintes des copies ; copie incrémentale (fichiers neufs ou changés seulement) ;
# une passe toutes les 10 min. À la fin, la session fait un instantané du disque de ce poste (les copies) avant toute
# destruction ; l'index poussé et scellé fait foi pour ces copies. Lecture seule sur l'instance, comme la v1.
set -uo pipefail
DEPOT=/home/user/controle-ia-travail
BRANCHE=claude/compassionate-meitner-d4ryyk
BASE=$DEPOT/runs/temoin-bailey-v1-20261111
V=$BASE/versement-instance-61170458-v2
JOURNAL=/root/poste-inventaire-instance-v2.log
INSTANCE=61170458
ETIQUETTE=temoin-bailey-c6-845f37c35eba4a3d
exec >>"$JOURNAL" 2>&1
echo "début $(date -u +%FT%TZ)"
DEBUT_POSTE=$(date -u +%s)

umask 077
mkdir -p /root/.ssh
cat > /root/.ssh/deploiement <<'@@CLE_DEPLOIEMENT_FIN@@'
@@CLE_DEPLOIEMENT@@
@@CLE_DEPLOIEMENT_FIN@@
cat > /root/.ssh/id_ed25519 <<'@@CLE_VAST_FIN@@'
@@CLE_VAST@@
@@CLE_VAST_FIN@@
cat > /root/secrets.env <<'@@SECRETS_FIN@@'
@@SECRETS@@
@@SECRETS_FIN@@
chmod 600 /root/.ssh/deploiement /root/.ssh/id_ed25519 /root/secrets.env
umask 022

etat() { mkdir -p "$BASE"; echo "$(date -u +%FT%TZ) $1" >> "$BASE/poste-inventaire-instance-v2-etat.txt"; echo "$1"; }
pousser() {  # $1 : message ; pousse les seuls fichiers du versement et de ce poste
  cd "$DEPOT" || return 1
  local f
  for f in "$V" "$BASE/poste-inventaire-instance-v2-etat.txt" "$BASE/poste-fini-inventaire-instance-v1.json"; do
    [ -e "$f" ] && git add -A "$f"
  done
  git diff --cached --quiet && return 0
  git commit -q -m "Témoin de Bailey, poste d'inventaire de l'instance : $1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XJ6MgnEhQMZteN9F8a1BST"
  for i in 1 2 3 4; do
    git pull -q --rebase origin "$BRANCHE" && git push -q origin "HEAD:$BRANCHE" && return 0
    git rebase --abort 2>/dev/null; sleep $((2 ** i))
  done
  echo "poussée en échec $(date -u +%FT%TZ)"
}

# 1. outils et dépôt
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq && apt-get install -y -qq git openssh-client python3-venv python3-pip ca-certificates curl rsync \
  || { echo "installation apt en échec"; exit 3; }
ssh-keyscan -t ed25519 github.com >> /root/.ssh/known_hosts 2>/dev/null
export GIT_SSH_COMMAND="ssh -i /root/.ssh/deploiement -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes"
mkdir -p /home/user
git clone -q --single-branch --branch "$BRANCHE" git@github.com:lciric/controle-ia-travail.git "$DEPOT" \
  || { echo "clonage en échec"; exit 3; }
cd "$DEPOT"
git config user.name "Claude"; git config user.email "noreply@anthropic.com"
etat "dépôt cloné : $(git rev-parse HEAD)"
[ ! -e "$V" ] || { etat "versement déjà présent (R12) : rien ne tourne"; pousser "versement déjà présent"; exit 3; }
(cd "$BASE" && sha256sum -c --quiet poste-inventaire-instance-v2.sh.sha256) \
  || { etat "empreinte de ce script différente : rien ne tourne"; pousser "empreinte en échec"; exit 3; }
python3 -m venv /root/venv && . /root/venv/bin/activate && pip install -q vastai==1.11.0 \
  || { etat "environnement Python en échec : rien ne tourne"; pousser "Python en échec"; exit 3; }
set -a; . /root/secrets.env; set +a
[ -n "${VAST_API_KEY:-}" ] && [ -n "${HF_TOKEN:-}" ] || { etat "clés absentes : rien ne tourne"; pousser "clés absentes"; exit 3; }

# 2. présence de l'instance : 0 absente, 1 présente, 2 inventaire illisible
presence() {
  vastai show instances --raw > /root/instances.json 2>/dev/null || return 2
  python3 - <<'EOF'
import json, sys
d = json.load(open("/root/instances.json"))
t = [i for i in d if str(i.get("id")) == "61170458"]
sys.exit(1 if t and t[0].get("label") == "temoin-bailey-c6-845f37c35eba4a3d" else 0)
EOF
  return $?
}
presence; P0=$?
[ "$P0" -eq 1 ] || { etat "instance 61170458 absente ou inventaire illisible (code $P0) : rien ne tourne"; pousser "instance absente au départ"; exit 3; }
mkdir -p "$V"
etat "instance 61170458 présente : passes toutes les 10 min"

# 3. une passe : inventaire, sélection, copie, contrôle des secrets, versement
passe() {
  local n=$1 T=/root/passe url hote port
  rm -rf "$T"; mkdir -p "$T/fichiers"
  url=$(vastai ssh-url "$INSTANCE" 2>/dev/null) || return 11
  hote=$(echo "$url" | sed -nE 's#^ssh://([^@]+@[^:]+):([0-9]+).*#\1#p'); port=$(echo "$url" | sed -nE 's#^ssh://([^@]+@[^:]+):([0-9]+).*#\2#p')
  [ -n "$hote" ] && [ -n "$port" ] || return 12
  local S=(ssh -i /root/.ssh/id_ed25519 -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -o BatchMode=yes -o ConnectTimeout=30 -p "$port" "$hote")
  # inventaire de tous les fichiers (lecture seule)
  timeout 1200 "${S[@]}" "nice -n 19 find / \\( -path /proc -o -path /sys -o -path /dev -o -path /run \\) -prune -o -type f -printf '%p\\t%s\\t%T@\\n' 2>/dev/null" \
    | LC_ALL=C sort > "$T/inventaire.tsv"
  local cs=("${PIPESTATUS[@]}")
  # find rend 1 pour un fichier disparu ou illisible pendant la lecture : accepté ; ssh coupé (255), délai (124) : passe en échec
  [ "${cs[0]}" -le 1 ] && [ "${cs[1]}" -eq 0 ] && [ -s "$T/inventaire.tsv" ] || return 13
  # sélection : fichiers de 25 Mio au plus sous les racines hors système, hors poids, caches, clés ; plafond 400 Mio
  python3 - "$T" <<'EOF' || return 14
import os, sys
T = sys.argv[1]
RACINES = ("/root/", "/workspace/", "/tmp/", "/var/log/", "/home/")
HORS = ("/root/hf/", "/root/.cache/", "/root/.ssh/", "/root/venv/")
MAX, PLAFOND = 2 * 2**30, 6 * 2**30
choisis, exclus, total = [], [], 0
for ligne in open(os.path.join(T, "inventaire.tsv"), encoding="utf-8", errors="surrogateescape"):
    p = ligne.rstrip("\n").split("\t")
    if len(p) != 3:
        continue
    chemin, taille = p[0], int(p[1]) if p[1].isdigit() else -1
    if not chemin.startswith(RACINES):
        continue
    nom = os.path.basename(chemin).lower()
    if chemin.startswith(HORS) or "token" in nom or "secret" in nom or nom.endswith(".env") or "credential" in nom:
        exclus.append((chemin, taille, "chemin réservé (poids, caches, clés, jetons) : inventorié, non copié"))
    elif "/site-packages/" in chemin or "/__pycache__/" in chemin or "/.venv/" in chemin:
        exclus.append((chemin, taille, "environnement Python ou cache : inventorié, non copié"))
    elif taille < 0 or taille > MAX:
        exclus.append((chemin, taille, "taille au-dessus de 2 Gio : inventorié, non copié"))
    elif total + taille > PLAFOND:
        exclus.append((chemin, taille, "plafond de 6 Gio atteint : inventorié, non copié"))
    else:
        choisis.append((0 if chemin.startswith("/root/x/") else 1, chemin.lstrip("/"), taille, p[2])); total += taille
choisis.sort()
# copie incrémentale : seuls les fichiers neufs ou changés (taille ou date) depuis la passe précédente
prec = {}
P = "/root/versement-local/selection-precedente.tsv"
if os.path.exists(P):
    for l in open(P, encoding="utf-8", errors="surrogateescape"):
        q = l.rstrip("\n").split("\t")
        if len(q) == 3:
            prec[q[0]] = (q[1], q[2])
a_copier = [c for _, c, s, d in choisis if prec.get(c) != (str(s), d)]
partis = sorted(set(prec) - {c for _, c, _, _ in choisis})
with open(os.path.join(T, "selection.tsv"), "w", encoding="utf-8", errors="surrogateescape") as f:
    for _, c, s, d in choisis:
        f.write(f"{c}\t{s}\t{d}\n")
with open(os.path.join(T, "partis0"), "wb") as f:
    for c in partis:
        f.write(c.encode("utf-8", "surrogateescape") + b"\0")
choisis = a_copier
with open(os.path.join(T, "liste0"), "wb") as f:
    for c in choisis:
        f.write(c.encode("utf-8", "surrogateescape") + b"\0")
with open(os.path.join(T, "exclusions.tsv"), "w", encoding="utf-8", errors="surrogateescape") as f:
    for c, s, r in exclus:
        f.write(f"{c}\t{s}\t{r}\n")
print(f"sélection {total} octets ; à copier {len(choisis)} ; partis {len(partis)} ; exclus {len(exclus)}")
EOF
  # copie (lecture seule : tar -c sous nice ; un fichier disparu entre-temps est signalé par tar, non bloquant)
  timeout 3000 "${S[@]}" "cd / && nice -n 19 tar --null -T - -cf - 2>/dev/null" < "$T/liste0" | tar -xf - -C "$T/fichiers" 2>/dev/null
  local ct=("${PIPESTATUS[@]}")
  # tar -c rend 1 pour un fichier modifié ou disparu pendant la lecture : accepté ; tout autre échec garde le versement
  # précédent (le miroir n'est jamais remplacé par une copie coupée)
  [ "${ct[0]}" -le 1 ] && [ "${ct[1]}" -eq 0 ] || return 16
  if [ -s "$T/liste0" ] && [ -z "$(find "$T/fichiers" -type f -print -quit)" ]; then return 17; fi
  # contrôle des secrets : valeurs exactes des clés de ce poste, clés privées, jetons
  python3 - "$T" <<'EOF' || return 15
import os, re, sys
T = sys.argv[1]
valeurs = [os.environ.get("VAST_API_KEY", ""), os.environ.get("HF_TOKEN", "")]
for k in ("/root/.ssh/deploiement", "/root/.ssh/id_ed25519"):
    lignes = [l.strip() for l in open(k, encoding="utf-8") if l.strip() and "-----" not in l]
    valeurs += [l for l in lignes if len(l) >= 40]
valeurs = [v.encode() for v in valeurs if len(v) >= 16]
motifs = [re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"), re.compile(rb"hf_[A-Za-z0-9]{30,}"),
          re.compile(rb"ghp_[A-Za-z0-9]{30,}"), re.compile(rb"github_pat_[A-Za-z0-9_]{30,}"),
          re.compile(rb"(?i)(api[_-]?key|token|secret|password)['\"]?\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{20,}")]
retires = []
racine = os.path.join(T, "fichiers")
for d, _, fs in os.walk(racine):
    for n in fs:
        p = os.path.join(d, n)
        try:
            b = open(p, "rb").read()
        except OSError:
            continue
        if any(v in b for v in valeurs) or any(m.search(b) for m in motifs):
            retires.append("/" + os.path.relpath(p, racine))  # v2 : gardé sur le disque local, jamais poussé
with open(os.path.join(T, "exclusions.tsv"), "a", encoding="utf-8", errors="surrogateescape") as f:
    for r in retires:
        f.write(f"{r}\t-1\tsecret possible (clé, jeton) : copie gardée sur le disque de ce poste, jamais poussée, seulement nommée\n")
print(f"marqués secret possible : {len(retires)}")
EOF
  # versement : copies neuves ajoutées au miroir local (jamais poussé), fichiers partis retirés du miroir ;
  # index des empreintes de tout le miroir ; inventaire, exclusions, index et état poussés
  mkdir -p /root/versement-local/fichiers
  cp -a "$T/fichiers/." /root/versement-local/fichiers/
  (cd /root/versement-local/fichiers && xargs -0 -r rm -f -- < "$T/partis0")
  cp "$T/selection.tsv" /root/versement-local/selection-precedente.tsv
  (cd /root/versement-local && find fichiers -type f -print0 | LC_ALL=C sort -z | xargs -0 -r sha256sum > "$V/empreintes-copies-locales.txt")
  gzip -n -c "$T/inventaire.tsv" > "$V/inventaire-instance.tsv.gz"
  cp "$T/exclusions.tsv" "$V/exclusions.tsv"
  printf '{"passe": %s, "heure": "%s", "fichiers_inventories": %s, "fichiers_verses": %s, "exclusions": %s}\n' \
    "$n" "$(date -u +%FT%TZ)" "$(wc -l < "$T/inventaire.tsv")" "$(wc -l < "$V/empreintes-copies-locales.txt")" "$(wc -l < "$T/exclusions.tsv")" \
    > "$V/passe-courante.json"
  return 0
}

# 4. boucle des passes
n=0; absences=0
while true; do
  presence; P=$?
  if [ "$P" -eq 0 ]; then
    absences=$((absences + 1)); [ "$absences" -ge 2 ] && { etat "instance 61170458 absente de l'inventaire Vast (deux lectures) : fin des passes"; break; }
    sleep 60; continue
  fi
  absences=0
  if [ "$P" -eq 2 ]; then etat "inventaire Vast illisible : passe reportée"; sleep 120; continue; fi
  [ $(( $(date -u +%s) - DEBUT_POSTE )) -lt 129600 ] || { etat "plafond de 36 h atteint : fin des passes, instance encore présente"; break; }
  n=$((n + 1))
  if passe "$n"; then etat "passe $n faite : $(cat "$V/passe-courante.json")"; else etat "passe $n en échec (code $?) : versement précédent gardé"; fi
  pousser "passe $n"
  sleep 600
done

# 5. scellement et fin
for f in inventaire-instance.tsv.gz exclusions.tsv passe-courante.json empreintes-copies-locales.txt; do
  [ -f "$V/$f" ] && (cd "$V" && sha256sum "$f" > "$f.sha256")
done
# journal de ce poste, sans secret (il n'en imprime aucun) ; contrôle par les valeurs exactes avant versement
python3 - "$JOURNAL" "$V/journal-poste-inventaire-instance-v2.log" <<'EOF'
import os, sys
b = open(sys.argv[1], "rb").read()
for v in (os.environ.get("VAST_API_KEY", ""), os.environ.get("HF_TOKEN", "")):
    if len(v) >= 16:
        b = b.replace(v.encode(), b"[clé retirée]")
open(sys.argv[2], "wb").write(b)
EOF
(cd "$V" && sha256sum journal-poste-inventaire-instance-v2.log > journal-poste-inventaire-instance-v2.log.sha256)
printf '{"fini": "%s", "passes": %s}\n' "$(date -u +%FT%TZ)" "$n" > "$BASE/poste-fini-inventaire-instance-v1.json"
etat "fin : $n passes ; index des copies locales scellé ; copies sur le disque de ce poste (instantané par la session)"
pousser "fin (marque poste-fini-inventaire-instance-v1.json)"
echo "fin $(date -u +%FT%TZ)"
