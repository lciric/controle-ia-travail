#!/bin/bash
# Serveur d'INVENTAIRE PAR INSTANTANÉ d'un poste Hetzner du témoin de Bailey — v1.
# Mot de Lazar (19 novembre 2026, vers 08:47Z), verbatim : « avant toute destruction, inventaire et versement scellé de
# tout ce qui reste sur la machine » ; « Poste et instance Vast ».
# Ce serveur est créé depuis l'instantané (snapshot Hetzner) du disque du poste @@CIBLE@@, éteint avant l'instantané.
# Ses données de démarrage ne portent AUCUN secret : il pousse avec la clé de déploiement présente sur le disque copié.
#   1. inventaire de tous les fichiers du disque copié (chemin, taille, date), hors /proc, /sys, /dev, /run ;
#   2. copie des fichiers de 25 Mio au plus sous /root, /home, /tmp, /var/tmp, /var/log, /opt et /srv, hors clés et
#      secrets (/root/.ssh, /root/secrets.env), hors données de cloud-init (/var/lib/cloud : elles portent les données de
#      démarrage du poste, donc ses clés), hors environnements Python et caches ; plafond de 400 Mio ;
#   3. dans le dépôt cloné sur le poste : seuls les fichiers non suivis ou ignorés sont copiés (les suivis sont déjà sur
#      la branche), plus l'état de git (statut, dernier commit, modifications non commitées, commits non poussés) ;
#   4. contrôle des secrets sur les copies (valeurs des clés lues sur le disque copié, clés privées, jetons) : tout fichier
#      suspect est retiré et seulement nommé ;
#   5. les fichiers écrits après l'instantané (par ce serveur) sont nommés, jamais copiés comme fichiers du poste ;
#   6. versement dans `runs/temoin-bailey-v1-20261111/versement-@@CIBLE@@-v1/`, dans un clone neuf de la branche ; index
#      des empreintes scellé ; marque `poste-fini-inventaire-instantane-@@CIBLE@@-v1.json` ; poussée.
# La session détruit ensuite ce serveur, puis le poste cible, par identifiant (R10). L'instantané est gardé jusqu'à la
# clôture : il porte les clés du poste, et il est effacé avec la révocation des clés. Aucune note n'est lue : les fichiers
# sont copiés sans être ouverts, sauf par le contrôle des secrets, qui ne rend que des noms.
set -uo pipefail
CIBLE=@@CIBLE@@
HEURE_INSTANTANE=@@HEURE@@
BRANCHE=claude/compassionate-meitner-d4ryyk
DEPOT_POSTE=/home/user/controle-ia-travail
CLONE=/root/clone-versement-$CIBLE
T=/root/travail-inventaire-$CIBLE
exec >>"/var/log/inventaire-instantane-$CIBLE-v1.log" 2>&1
echo "début $(date -u +%FT%TZ)"
case "$CIBLE" in *@@*|"") echo "cible non remplie"; exit 3;; esac
case "$HEURE_INSTANTANE" in ''|*[!0-9]*) echo "heure de l'instantané non remplie"; exit 3;; esac
rm -rf "$T"; mkdir -p "$T/fichiers"

# 1. inventaire du disque copié (avant tout clonage, toute installation)
find / \( -path /proc -o -path /sys -o -path /dev -o -path /run \) -prune -o -type f -printf '%p\t%s\t%T@\n' 2>/dev/null \
  | LC_ALL=C sort > "$T/inventaire.tsv"
[ -s "$T/inventaire.tsv" ] || { echo "inventaire vide"; exit 3; }

# 2. état de git du dépôt cloné sur le poste, et ses fichiers non suivis ou ignorés
if [ -d "$DEPOT_POSTE/.git" ]; then
  {
    echo "# git -C $DEPOT_POSTE (disque copié du poste $CIBLE)"
    echo "## dernier commit"; git -C "$DEPOT_POSTE" log -1 --format='%H %cI %s'
    echo "## branche suivie"; git -C "$DEPOT_POSTE" rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>&1
    echo "## commits non poussés"; git -C "$DEPOT_POSTE" log --format='%H %cI %s' '@{u}..HEAD' 2>&1
    echo "## statut (suivis modifiés, non suivis, ignorés)"; git -C "$DEPOT_POSTE" status --porcelain --ignored 2>&1
  } > "$T/git-etat.txt"
  git -C "$DEPOT_POSTE" diff > "$T/git-modifications-non-commitees.diff" 2>/dev/null
  if [ -n "$(git -C "$DEPOT_POSTE" log --format=%H '@{u}..HEAD' 2>/dev/null)" ]; then
    git -C "$DEPOT_POSTE" bundle create "$T/git-commits-non-pousses.bundle" '@{u}..HEAD' 2>/dev/null
  fi
  git -C "$DEPOT_POSTE" ls-files -z --others 2>/dev/null > "$T/depot-non-suivis0"
else
  echo "pas de dépôt cloné sur ce disque" > "$T/git-etat.txt"; : > "$T/depot-non-suivis0"
fi

# 3. sélection
python3 - "$T" "$HEURE_INSTANTANE" "$DEPOT_POSTE" <<'EOF' || { echo "sélection en échec"; exit 3; }
import os, sys
T, heure, depot = sys.argv[1], float(sys.argv[2]), sys.argv[3].rstrip("/") + "/"
RACINES = ("/root/", "/home/", "/tmp/", "/var/tmp/", "/var/log/", "/opt/", "/srv/")
HORS = ("/root/.ssh/", "/root/secrets.env", "/var/lib/cloud/", "/root/.cache/", "/root/venv/", "/root/clone-versement-",
        "/root/travail-inventaire-")
non_suivis = {depot + p.decode("utf-8", "surrogateescape")
              for p in open(os.path.join(T, "depot-non-suivis0"), "rb").read().split(b"\0") if p}
MAX, PLAFOND = 25 * 2**20, 400 * 2**20
choisis, exclus, total = [], [], 0
for ligne in open(os.path.join(T, "inventaire.tsv"), encoding="utf-8", errors="surrogateescape"):
    p = ligne.rstrip("\n").split("\t")
    if len(p) != 3:
        continue
    chemin, taille, date = p[0], int(p[1]) if p[1].isdigit() else -1, float(p[2]) if p[2].replace(".", "", 1).isdigit() else 0.0
    if not chemin.startswith(RACINES):
        continue
    nom = os.path.basename(chemin).lower()
    if date >= heure:
        exclus.append((chemin, taille, "écrit après l'instantané (par ce serveur) : nommé, non copié"))
    elif chemin.startswith(HORS) or "token" in nom or "secret" in nom or nom.endswith(".env") or "credential" in nom:
        exclus.append((chemin, taille, "chemin réservé (clés, secrets, données de démarrage, caches) : inventorié, non copié"))
    elif "/.venv/" in chemin or "/__pycache__/" in chemin or "/site-packages/" in chemin:
        exclus.append((chemin, taille, "environnement Python ou cache : inventorié, non copié"))
    elif chemin.startswith(depot) and chemin not in non_suivis:
        continue  # fichier suivi du dépôt : déjà sur la branche (l'état de git dit s'il est modifié)
    elif taille < 0 or taille > MAX:
        exclus.append((chemin, taille, "taille au-dessus de 25 Mio : inventorié, non copié"))
    elif total + taille > PLAFOND:
        exclus.append((chemin, taille, "plafond de 400 Mio atteint : inventorié, non copié"))
    else:
        choisis.append(chemin); total += taille
with open(os.path.join(T, "liste0"), "wb") as f:
    for c in choisis:
        f.write(c.lstrip("/").encode("utf-8", "surrogateescape") + b"\0")
with open(os.path.join(T, "exclusions.tsv"), "w", encoding="utf-8", errors="surrogateescape") as f:
    for c, s, r in exclus:
        f.write(f"{c}\t{s}\t{r}\n")
print(f"choisis {len(choisis)} ({total} octets) ; exclus {len(exclus)}")
EOF
(cd / && tar --null -T "$T/liste0" -cf - 2>/dev/null) | tar -xf - -C "$T/fichiers" 2>/dev/null

# 4. contrôle des secrets : valeurs exactes lues sur le disque copié, clés privées, jetons
python3 - "$T" <<'EOF' || { echo "contrôle des secrets en échec"; exit 3; }
import os, re, sys
T = sys.argv[1]
valeurs = []
if os.path.exists("/root/secrets.env"):
    for l in open("/root/secrets.env", encoding="utf-8", errors="replace"):
        if "=" in l:
            valeurs.append(l.split("=", 1)[1].strip().strip("'\""))
for k in ("/root/.ssh/deploiement", "/root/.ssh/id_ed25519"):
    if os.path.exists(k):
        valeurs += [l.strip() for l in open(k, encoding="utf-8", errors="replace") if len(l.strip()) >= 40 and "-----" not in l]
valeurs = [v.encode() for v in valeurs if len(v) >= 16]
motifs = [re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"), re.compile(rb"hf_[A-Za-z0-9]{30,}"),
          re.compile(rb"ghp_[A-Za-z0-9]{30,}"), re.compile(rb"github_pat_[A-Za-z0-9_]{30,}"),
          re.compile(rb"(?i)(api[_-]?key|token|secret|password)['\"]?\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{20,}")]
retires = []
for base in (os.path.join(T, "fichiers"), T):
    for d, ds, fs in os.walk(base):
        if base == T:
            ds[:] = []  # seuls les fichiers d'état au niveau de T
        for n in fs:
            p = os.path.join(d, n)
            if base == T and n in ("liste0", "depot-non-suivis0"):
                continue
            try:
                b = open(p, "rb").read()
            except OSError:
                continue
            if any(v in b for v in valeurs) or any(m.search(b) for m in motifs):
                retires.append(("/" + os.path.relpath(p, os.path.join(T, "fichiers"))) if base != T else ("[état] " + n))
                os.remove(p)
with open(os.path.join(T, "exclusions.tsv"), "a", encoding="utf-8", errors="surrogateescape") as f:
    for r in retires:
        f.write(f"{r}\t-1\tsecret possible (clé, jeton) : retiré de la copie, seulement nommé\n")
print(f"retirés pour secret possible : {len(retires)}")
EOF

# 5. versement dans un clone neuf de la branche (la clé de déploiement est sur le disque copié)
export GIT_SSH_COMMAND="ssh -i /root/.ssh/deploiement -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
rm -rf "$CLONE"
git clone -q --single-branch --branch "$BRANCHE" git@github.com:lciric/controle-ia-travail.git "$CLONE" \
  || { echo "clonage en échec"; exit 3; }
cd "$CLONE"; git config user.name "Claude"; git config user.email "noreply@anthropic.com"
V="$CLONE/runs/temoin-bailey-v1-20261111/versement-$CIBLE-v1"
[ ! -e "$V" ] || { echo "versement déjà présent (R12)"; exit 3; }
mkdir -p "$V"
cp -a "$T/fichiers" "$V/fichiers"
gzip -n -c "$T/inventaire.tsv" > "$V/inventaire-disque.tsv.gz"
for f in exclusions.tsv git-etat.txt git-modifications-non-commitees.diff git-commits-non-pousses.bundle; do
  [ -f "$T/$f" ] && cp "$T/$f" "$V/$f"
done
(cd "$V" && find fichiers -type f -print0 | LC_ALL=C sort -z | xargs -0 -r sha256sum > empreintes-fichiers-verses.txt)
for f in "$V"/*; do [ -f "$f" ] && (cd "$V" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done
printf '{"cible": "%s", "heure_instantane": %s, "fini": "%s", "fichiers_inventories": %s, "fichiers_verses": %s}\n' \
  "$CIBLE" "$HEURE_INSTANTANE" "$(date -u +%FT%TZ)" "$(wc -l < "$T/inventaire.tsv")" "$(find "$V/fichiers" -type f | wc -l)" \
  > "$CLONE/runs/temoin-bailey-v1-20261111/poste-fini-inventaire-instantane-$CIBLE-v1.json"
git add -A "$V" "runs/temoin-bailey-v1-20261111/poste-fini-inventaire-instantane-$CIBLE-v1.json"
git commit -q -m "Témoin de Bailey : inventaire et versement scellé du poste $CIBLE (par instantané)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XJ6MgnEhQMZteN9F8a1BST"
for i in 1 2 3 4 5; do
  git pull -q --rebase origin "$BRANCHE" && git push -q origin "HEAD:$BRANCHE" && { echo "poussé $(date -u +%FT%TZ)"; break; }
  git rebase --abort 2>/dev/null; sleep $((2 ** i))
done
echo "fin $(date -u +%FT%TZ)"
