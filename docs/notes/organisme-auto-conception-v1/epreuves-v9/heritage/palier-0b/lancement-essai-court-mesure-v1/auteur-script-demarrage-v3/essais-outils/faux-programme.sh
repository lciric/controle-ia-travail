#!/bin/bash
# Faux programme du palier 0b, posé comme bin/python du faux environnement. Écrit dans $FAUX_JOURNAL_PROGRAMME son dossier
# courant, PYTHONPATH et ses arguments (un par ligne), puis imite les sorties : etape-3 (manifeste et compagnon), trois
# dossiers de source de l'étape 4, attente de FAUX_DUREE_S secondes (4 par défaut), manifeste de l'étape 4 ; code 0.
# Ne lit rien de la racine.
J=${FAUX_JOURNAL_PROGRAMME:-/dev/null}
{ echo "cwd=$PWD"; echo "PYTHONPATH=${PYTHONPATH:-}"; for a in "$@"; do echo "arg=$a"; done; } >> "$J"
S=${!#}
# v3 : héritage des réglages du script (quatre variables nommées seulement ; aucune liste de l'environnement)
echo "faux programme : herite DEBIAN_FRONTEND=${DEBIAN_FRONTEND+oui} GIT_CONFIG_GLOBAL=${GIT_CONFIG_GLOBAL+oui} GIT_CONFIG_NOSYSTEM=${GIT_CONFIG_NOSYSTEM+oui} GIT_TERMINAL_PROMPT=${GIT_TERMINAL_PROMPT+oui}" >> "$J"
mkdir -p "$S/etape-3" || exit 3
echo '{"etape": 3, "factice": true}' > "$S/etape-3/manifeste.json"
(cd "$S/etape-3" && sha256sum manifeste.json > manifeste.json.sha256)
for i in 0 1 2; do mkdir -p "$S/etape-4/couche-mecanique/bras-1-a-3/factice/0.0/$i"; echo "$i" > "$S/etape-4/couche-mecanique/bras-1-a-3/factice/0.0/$i/x.txt"; done
# v2 : FAUX_SORTIE_OCTETS = nombre d'octets écrits sur la sortie standard (essai du plafond du versement)
[ -z "${FAUX_SORTIE_OCTETS:-}" ] || head -c "$FAUX_SORTIE_OCTETS" /dev/zero | tr '\0' 'x'
sleep "${FAUX_DUREE_S:-4}"
echo '{"etape": 4, "factice": true}' > "$S/etape-4/manifeste.json"
(cd "$S/etape-4" && sha256sum manifeste.json > manifeste.json.sha256)
echo "faux programme : fin" >> "$J"
exit 0
