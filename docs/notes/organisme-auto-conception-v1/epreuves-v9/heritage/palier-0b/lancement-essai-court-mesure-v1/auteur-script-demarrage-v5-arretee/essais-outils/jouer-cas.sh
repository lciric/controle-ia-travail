#!/bin/bash
# Joue un cas d'essai du script de démarrage, sur factices locaux seulement.
# Emploi : jouer-cas.sh NOM DONNEES_DE_DEMARRAGE [VAR=VALEUR ...]
#   Crée travail/cas/NOM (neuf) ; un dépôt distant factice propre au cas (objets partagés avec travail/distant, en
#   lecture), servi en HTTP sur 127.0.0.1 par serveur-git-factice.py, qui exige le jeton factice (ou celui de
#   SERVEUR_JETON=FICHIER) ; joue les données de démarrage comme le ferait la machine (copie part-001, droits 700), avec
#   les réglages ESSAI_DEMARRAGE_* vers les factices, et les VAR=VALEUR données ; guette `ps` pendant tout le cas ; attend
#   la fin de la boucle de versement (au plus 600 s) ; arrête son serveur par son identifiant ; puis cherche le jeton factice
#   dans tous les fichiers du cas (hors les trois qui doivent le porter), dans l'histoire des dépôts (git log -p --all) et
#   dans les relevés de `ps`. Écrit et affiche travail/cas/NOM/resume.txt.
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$ICI")
NOM=$1; UD=$2; shift 2
W=$ESS/travail/cas/$NOM
AUT=$(dirname "$(dirname "$ESS")")
JETON_BON=$AUT/essais/travail/jeton-factice.txt
PARTAGE=$ESS/travail/distant/controle-ia-travail.git  # v4 : dépôt factice propre à la v4
# v2 : le banc pose ESSAI_DEMARRAGE_BANC=oui (sauf SANS_BANC=1) ; racine et clone du cas retirés après les recherches
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/distant" "$W/journaux"
SJ=$JETON_BON
for kv in "$@"; do
  case "$kv" in SERVEUR_JETON=*) SJ=${kv#SERVEUR_JETON=} ;; esac
done
# dépôt distant du cas : objets partagés, mêmes références que le dépôt partagé
RD=$W/distant/controle-ia-travail.git
git init -q --bare "$RD"
echo "$PARTAGE/objects" > "$RD/objects/info/alternates"
[ -f "$PARTAGE/shallow" ] && cp "$PARTAGE/shallow" "$RD/shallow"
git -C "$PARTAGE" for-each-ref --format='%(refname) %(objectname)' | while read -r ref sha; do git -C "$RD" update-ref "$ref" "$sha"; done
cp "$SJ" "$W/serveur-jeton.txt"
PORT=$(shuf -i 20000-40000 -n 1)
/home/user/controle-ia-travail/.venv/bin/python -I "$ICI/serveur-git-factice.py" "$PORT" "$W/distant" "$W/serveur-jeton.txt" \
  "$W/journaux/serveur.txt" "$W/serveur-pret.txt" > "$W/journaux/serveur-sortie.txt" 2>&1 &
PID_SERVEUR=$!
for i in $(seq 1 100); do [ -s "$W/serveur-pret.txt" ] && break; sleep 0.1; done
# guetteur de ps
bash "$ICI/guetteur-ps.sh" "$JETON_BON" "$W/journaux/ps-jeton.txt" "$W/guetteur-arret" &
PID_GUETTEUR=$!
# données de démarrage posées comme par la machine
cp "$UD" "$W/part-001" && chmod 700 "$W/part-001"
export NO_PROXY="127.0.0.1,localhost${NO_PROXY:+,$NO_PROXY}" no_proxy="127.0.0.1,localhost${no_proxy:+,$no_proxy}"
export ESSAI_DEMARRAGE_BASE=$W/base ESSAI_DEMARRAGE_SECRET=$W/secret
export ESSAI_DEMARRAGE_DEPOT_URL=http://127.0.0.1:$PORT/controle-ia-travail.git
export ESSAI_DEMARRAGE_APT_GET=$ICI/faux-apt-get.sh ESSAI_DEMARRAGE_PY_SYS=$ICI/faux-python3.sh
export ESSAI_DEMARRAGE_INTERVALLE=5 ESSAI_DEMARRAGE_ATTENTE=1 ESSAI_DEMARRAGE_OPT_GARDIEN="--intervalle-s 1 --delai-force-s 5"
export FAUX_JOURNAL=$W/journaux/factices.txt FAUX_JOURNAL_PROGRAMME=$W/journaux/programme.txt
export ESSAI_DEMARRAGE_BANC=oui ESSAI_DEMARRAGE_CHARGE=$W/charge-amorce  # v3 : charge extraite par l'amorce
# v5 : groupe de contrôle propre au cas, sous le cgroup v2 du banc (réglable : vide ou autre chemin pour le repli)
export ESSAI_DEMARRAGE_CGROUPE=/sys/fs/cgroup/unified/essai-3-banc-v5-$NOM
for kv in "$@"; do
  case "$kv" in SERVEUR_JETON=*) ;; SANS_BANC=1) unset ESSAI_DEMARRAGE_BANC ;; *=*) export "$kv" ;; esac
done
[ "${ESSAI_BASE_PRESENTE:-}" = 1 ] && mkdir -p "$W/base" && echo "ligne d'un premier démarrage" > "$W/base/journal-demarrage-essai-3.txt"
DEBUT=$(date +%s)
CODE1=
if [ "${DEUX_FOIS:-}" = 1 ]; then  # v5 (R4 bis) : premier démarrage, puis reprise sur les mêmes données
  bash "$W/part-001" > "$W/journaux/sortie-script-premier.txt" 2>&1
  CODE1=$?
  CHARGE1=$([ -e "$W/charge-amorce" ] && echo présente || echo absente)
fi
bash "$W/part-001" > "$W/journaux/sortie-script.txt" 2>&1
CODE=$?
# attente de la boucle de versement
PV=$(cat "$W/base/pid-versement-essai-3.txt" 2>/dev/null)
if [ -n "$PV" ]; then
  for i in $(seq 1 600); do [ -e "/proc/$PV" ] || break; sleep 1; done
fi
FIN=$(date +%s)
: > "$W/guetteur-arret"
wait "$PID_GUETTEUR"
kill "$PID_SERVEUR"
wait "$PID_SERVEUR" 2>/dev/null
# recherches du jeton factice
{
  echo "cas : $NOM ; données : $UD ; réglages : $*"
  echo "code du script de démarrage : $CODE ; durée : $((FIN - DEBUT)) s"
  echo "--- échec écrit : $(cat "$W/base/echec-demarrage-essai-3.txt" 2>/dev/null || echo aucun)"
  echo "--- fichiers du cas portant le jeton factice (hors part-001, secret/jeton, serveur-jeton.txt) :"
  grep -r -l -F -f "$JETON_BON" "$W" | grep -v -x -F -e "$W/part-001" -e "$W/secret/jeton" -e "$W/serveur-jeton.txt" \
    -e "$W/journaux/ps-jeton.txt" ; echo "(fin de liste)"
  echo "--- ps : $(tail -n 1 "$W/journaux/ps-jeton.txt")"
  B=refs/heads/recuperation/palier-0b-programme-1-essai-3-v1
  if git -C "$RD" rev-parse -q --verify "$B" > /dev/null; then
    echo "--- histoire de la branche de récupération du distant portant le jeton : $(git -C "$RD" log -p "$B" | grep -c -F -f "$JETON_BON")"
  fi
  if [ -d "$W/base/versement/.git" ]; then
    echo "--- histoire du dépôt de versement portant le jeton : $(git -C "$W/base/versement" log -p --all 2>/dev/null | grep -c -F -f "$JETON_BON")"
  fi
  echo "--- droits : secret/jeton $(stat -c %a "$W/secret/jeton" 2>/dev/null) ; secret $(stat -c %a "$W/secret" 2>/dev/null)"
  echo "--- références du distant du cas :"; git -C "$RD" for-each-ref --format='%(refname) %(objectname:short)'
  if git -C "$RD" rev-parse -q --verify refs/heads/recuperation/palier-0b-programme-1-essai-3-v1 > /dev/null; then
    echo "--- commits de la branche de récupération : $(git -C "$RD" rev-list --count refs/heads/recuperation/palier-0b-programme-1-essai-3-v1)"
    echo "--- fichiers de la branche :"; git -C "$RD" ls-tree -r --name-only refs/heads/recuperation/palier-0b-programme-1-essai-3-v1
  fi
  echo "--- journal de démarrage (lignes de pas, d'échec, de versement) :"
  grep -E "pas \(|ECHEC|versement|refus|ATTENTION|demarrage|arret|garde" "$W/base/journal-demarrage-essai-3.txt" 2>/dev/null | cut -c1-220
  echo "--- sortie directe du script : $(head -c 300 "$W/journaux/sortie-script.txt")"
  echo "--- base créée : $([ -d "$W/base" ] && echo oui || echo non) ; faux programme lancé : $([ -f "$W/journaux/programme.txt" ] && echo oui || echo non)"
  [ -f "$W/base/versement/essai-3/etat-essai-3.txt" ] && { echo "--- dernier état versé :"; cat "$W/base/versement/essai-3/etat-essai-3.txt"; }
  echo "--- serveur factice : $(grep -c . "$W/journaux/serveur.txt") lignes ; 401 : $(grep -c -e '-> 401' "$W/journaux/serveur.txt") ; admises : $(grep -c -e 'admise' "$W/journaux/serveur.txt")"
} > "$W/resume.txt" 2>&1
{
  [ -n "$CODE1" ] && echo "--- premier démarrage : code $CODE1 ; charge après lui : $CHARGE1"
  echo "--- charge extraite à la fin : $([ -e "$W/charge-amorce" ] && echo oui || echo non) ; copie privée : $(ls -d "$W"/charge-amorce.script.* 2>/dev/null | wc -l)"
  echo "--- groupe de contrôle : $(cat "$W/base/groupe-de-controle-essai-3.txt" 2>/dev/null || echo 'non écrit') ; référence : $(cat "$W/base/depart-lu-par-le-script-essai-3.txt" 2>/dev/null || echo aucune)"
} >> "$W/resume.txt"
G=$ESSAI_DEMARRAGE_CGROUPE
if [ -n "$G" ] && [ -f "$G/cgroup.procs" ]; then
  echo "--- membres du groupe de contrôle à la fin : $(grep -c . "$G/cgroup.procs")" >> "$W/resume.txt"
fi
pgrep -af "$W/" > "$W/journaux/processus-restants.txt"
echo "--- processus du cas encore vivants à la fin : $(grep -c . "$W/journaux/processus-restants.txt")" >> "$W/resume.txt"
# v5 : nettoyage du banc, par identifiant seulement : membres restants du groupe du cas, puis processus restants du cas
# (hors ce joueur), puis retrait du groupe
if [ -n "$G" ] && [ -f "$G/cgroup.procs" ]; then
  for x in $(cat "$G/cgroup.procs"); do kill -KILL "$x" 2>/dev/null; done
fi
while read -r x r; do [ "$x" = $$ ] || kill -KILL "$x" 2>/dev/null; done < "$W/journaux/processus-restants.txt"
if [ -n "$G" ] && [ -d "$G" ]; then
  for i in $(seq 1 50); do [ -z "$(cat "$G/cgroup.procs")" ] && break; sleep 0.1; done
  rmdir "$G" && echo "--- groupe de contrôle du cas retiré" >> "$W/resume.txt"
fi
rm -rf "$W/base/racine" "$W/base/depot.git" "$W/base/liste-de-la-copie.txt" "$W/base/tenue/empreintes-recalculees-de-la-copie.txt" \
  "$W/base/tenue-verification/empreintes-recalculees-de-la-copie.txt"
cat "$W/resume.txt"
