#!/bin/bash
# CL : joue le script de demarrage sur factices locaux (adapte de jouer-cas.sh de l'auteur, dont il garde la logique).
# Emploi : jouer-cl.sh CL NOM DONNEES [VAR=VALEUR ...]
#   CL = dossier du contre-lecteur. Cas dans CL/mes-essais/cas/NOM (neuf).
# Differences avec l'auteur : (1) SONDE=script (variable VAR=VALEUR) execute apres la fin de la boucle et les recherches du
# jeton, avant le nettoyage, avec W, RD, PORT en variables ; (2) PATH_EN_TETE=dossiers (VAR=VALEUR) mis en tete de PATH
# pour le seul script joue ; (3) attente de la boucle bornee par ATTENTE_MAX (600 s par defaut) ; (4) a la fin, la racine,
# le depot de clonage, les listes et le venv sont retires.
set -u
CL=$1; NOM=$2; UD=$3; shift 3
OUTILS=$CL/aut/v2/essais/outils
W=$CL/mes-essais/cas/$NOM
JETON_BON=$CL/aut/essais/travail/jeton-factice.txt
PARTAGE=$CL/aut/essais/travail/distant/controle-ia-travail.git
export TMPDIR=$CL/tmp
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/distant" "$W/journaux"
SJ=$JETON_BON
SONDE=
PATH_EN_TETE=
ATTENTE_MAX=600
for kv in "$@"; do
  case "$kv" in
    SERVEUR_JETON=*) SJ=${kv#SERVEUR_JETON=} ;;
    SONDE=*) SONDE=${kv#SONDE=} ;;
    PATH_EN_TETE=*) PATH_EN_TETE=${kv#PATH_EN_TETE=} ;;
    ATTENTE_MAX=*) ATTENTE_MAX=${kv#ATTENTE_MAX=} ;;
  esac
done
RD=$W/distant/controle-ia-travail.git
git init -q --bare "$RD"
echo "$PARTAGE/objects" > "$RD/objects/info/alternates"
[ -f "$PARTAGE/shallow" ] && cp "$PARTAGE/shallow" "$RD/shallow"
git -C "$PARTAGE" for-each-ref --format='%(refname) %(objectname)' | while read -r ref sha; do git -C "$RD" update-ref "$ref" "$sha"; done
cp "$SJ" "$W/serveur-jeton.txt"
PORT=$(shuf -i 20000-40000 -n 1)
/home/user/controle-ia-travail/.venv/bin/python -I "$OUTILS/serveur-git-factice.py" "$PORT" "$W/distant" "$W/serveur-jeton.txt" \
  "$W/journaux/serveur.txt" "$W/serveur-pret.txt" > "$W/journaux/serveur-sortie.txt" 2>&1 &
PID_SERVEUR=$!
for i in $(seq 1 100); do [ -s "$W/serveur-pret.txt" ] && break; sleep 0.1; done
bash "$OUTILS/guetteur-ps.sh" "$JETON_BON" "$W/journaux/ps-jeton.txt" "$W/guetteur-arret" &
PID_GUETTEUR=$!
cp "$UD" "$W/part-001" && chmod 700 "$W/part-001"
export NO_PROXY="127.0.0.1,localhost${NO_PROXY:+,$NO_PROXY}" no_proxy="127.0.0.1,localhost${no_proxy:+,$no_proxy}"
export ESSAI_DEMARRAGE_BASE=$W/base ESSAI_DEMARRAGE_SECRET=$W/secret
export ESSAI_DEMARRAGE_DEPOT_URL=http://127.0.0.1:$PORT/controle-ia-travail.git
export ESSAI_DEMARRAGE_APT_GET=$OUTILS/faux-apt-get.sh ESSAI_DEMARRAGE_PY_SYS=$OUTILS/faux-python3.sh
export ESSAI_DEMARRAGE_INTERVALLE=5 ESSAI_DEMARRAGE_ATTENTE=1 ESSAI_DEMARRAGE_OPT_GARDIEN="--intervalle-s 1 --delai-force-s 5"
export FAUX_JOURNAL=$W/journaux/factices.txt FAUX_JOURNAL_PROGRAMME=$W/journaux/programme.txt
export ESPION_JOURNAL=$W/journaux/espion.txt ESPION_JETON=$JETON_BON PLANTER_JOURNAL=$W/journaux/planter.txt
export ESSAI_DEMARRAGE_BANC=oui
for kv in "$@"; do
  case "$kv" in
    SERVEUR_JETON=*|SONDE=*|PATH_EN_TETE=*|ATTENTE_MAX=*) ;;
    SANS_DEPOT_URL=1) unset ESSAI_DEMARRAGE_DEPOT_URL ;;
    SANS_BANC=1) unset ESSAI_DEMARRAGE_BANC ;;
    SANS_DEPOT_URL=1) unset ESSAI_DEMARRAGE_DEPOT_URL ;;
    *=*) export "$kv" ;;
  esac
done
[ -z "$PATH_EN_TETE" ] || export PATH="$PATH_EN_TETE:$PATH"
[ "${ESSAI_BASE_PRESENTE:-}" = 1 ] && mkdir -p "$W/base" && echo "ligne d'un premier demarrage" > "$W/base/journal-demarrage-essai-3.txt"
DEBUT=$(date +%s)
bash "$W/part-001" > "$W/journaux/sortie-script.txt" 2>&1
CODE=$?
FIN_SCRIPT=$(date +%s)
PV=$(cat "$W/base/pid-versement-essai-3.txt" 2>/dev/null)
if [ -n "$PV" ]; then
  for i in $(seq 1 "$ATTENTE_MAX"); do [ -e "/proc/$PV" ] || break; sleep 1; done
fi
FIN=$(date +%s)
: > "$W/guetteur-arret"
wait "$PID_GUETTEUR"
{
  echo "cas : $NOM ; donnees : $UD ; reglages : $*"
  echo "code du script de demarrage : $CODE ; duree du script : $((FIN_SCRIPT - DEBUT)) s ; duree avec la boucle : $((FIN - DEBUT)) s"
  echo "--- echec ecrit : $(cat "$W/base/echec-demarrage-essai-3.txt" 2>/dev/null || echo aucun)"
  echo "--- fichiers du cas portant le jeton factice (hors part-001, secret/jeton, serveur-jeton.txt, ps-jeton.txt) :"
  grep -r -l -F -f "$JETON_BON" "$W" | grep -v -x -F -e "$W/part-001" -e "$W/secret/jeton" -e "$W/serveur-jeton.txt" -e "$W/journaux/ps-jeton.txt"; echo "(fin de liste)"
  echo "--- ps : $(tail -n 1 "$W/journaux/ps-jeton.txt")"
  B=refs/heads/recuperation/palier-0b-programme-1-essai-3-v1
  if git -C "$RD" rev-parse -q --verify "$B" > /dev/null; then
    echo "--- histoire de la branche de recuperation du distant portant le jeton : $(git -C "$RD" log -p "$B" | grep -c -F -f "$JETON_BON")"
  fi
  if [ -d "$W/base/versement/.git" ]; then
    echo "--- histoire du depot de versement portant le jeton : $(git -C "$W/base/versement" log -p --all 2>/dev/null | grep -c -F -f "$JETON_BON")"
  fi
  echo "--- droits : secret/jeton $(stat -c %a "$W/secret/jeton" 2>/dev/null) ; secret $(stat -c %a "$W/secret" 2>/dev/null)"
  echo "--- references du distant du cas :"; git -C "$RD" for-each-ref --format='%(refname) %(objectname:short)'
  if git -C "$RD" rev-parse -q --verify "$B" > /dev/null; then
    echo "--- commits de la branche de recuperation : $(git -C "$RD" rev-list --count "$B")"
    echo "--- fichiers de la branche (taille) :"; git -C "$RD" ls-tree -r -l "$B" | cut -c1-200
  fi
  echo "--- journal de demarrage (lignes de pas, d'echec, de versement) :"
  grep -E "pas \(|ECHEC|versement|refus|ATTENTION|demarrage|arret|garde|tentative" "$W/base/journal-demarrage-essai-3.txt" 2>/dev/null | cut -c1-220
  echo "--- sortie directe du script : $(head -c 300 "$W/journaux/sortie-script.txt")"
  echo "--- base creee : $([ -d "$W/base" ] && echo oui || echo non) ; faux programme lance : $([ -f "$W/journaux/programme.txt" ] && echo oui || echo non)"
  [ -f "$W/base/versement/essai-3/etat-essai-3.txt" ] && { echo "--- dernier etat verse :"; cat "$W/base/versement/essai-3/etat-essai-3.txt"; }
  echo "--- serveur factice : $(grep -c . "$W/journaux/serveur.txt") lignes ; 401 : $(grep -c -e '-> 401' "$W/journaux/serveur.txt") ; admises : $(grep -c -e 'admise' "$W/journaux/serveur.txt")"
} > "$W/resume.txt" 2>&1
if [ -n "$SONDE" ]; then
  export W RD PORT
  { echo "=== sonde $SONDE"; bash "$SONDE"; echo "=== fin de la sonde"; } > "$W/sonde.txt" 2>&1
fi
kill "$PID_SERVEUR"
wait "$PID_SERVEUR" 2>/dev/null
rm -rf "$W/base/racine" "$W/base/depot.git" "$W/base/liste-de-la-copie.txt" "$W/base/tenue/empreintes-recalculees-de-la-copie.txt" \
  "$W/base/tenue-verification/empreintes-recalculees-de-la-copie.txt" "$W/base/venv" "$W/base/charge"
cat "$W/resume.txt"
[ ! -f "$W/sonde.txt" ] || cat "$W/sonde.txt"
