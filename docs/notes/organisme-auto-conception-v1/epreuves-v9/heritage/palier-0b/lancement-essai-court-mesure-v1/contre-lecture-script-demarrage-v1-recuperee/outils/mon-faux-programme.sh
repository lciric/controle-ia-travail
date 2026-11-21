#!/bin/bash
# Contre-lecteur : faux programme du palier 0b (comme celui de l'auteur) qui relève en plus, dans $FAUX_JOURNAL_PROGRAMME.env,
# les NOMS des variables d'environnement reçues, le nombre de lignes de son environnement qui portent le jeton factice, et
# l'état de la racine (présence d'un .git à la racine, fichier intrus). Même sortie que le faux programme de l'auteur.
J=${FAUX_JOURNAL_PROGRAMME:-/dev/null}
{ echo "cwd=$PWD"; echo "PYTHONPATH=${PYTHONPATH:-}"; for a in "$@"; do echo "arg=$a"; done; } >> "$J"
{
  if [ -n "${ESSAI_JETON_FICHIER:-}" ]; then
    echo "programme : lignes d'environnement portant le jeton : $(tr '\0' '\n' < /proc/$$/environ | grep -c -F -f "$ESSAI_JETON_FICHIER")"
  fi
  echo "programme : noms d'environnement reçus : $(tr '\0' '\n' < /proc/$$/environ | cut -d= -f1 | grep -E '^(DEBIAN_FRONTEND|GIT_|HOME|JETON|ESSAI_DEMARRAGE_)' | sort | tr '\n' ' ')"
  R=$(dirname "${@: -2:1}")
  for a in "$@"; do case "$a" in */racine) R=$a ;; esac; done
  echo "programme : racine $R ; .git à la racine : $([ -e "$R/.git" ] && echo OUI || echo non) ; intrus non suivi : $(find "$R" -name 'intrus-contre-lecteur.py' 2> /dev/null | wc -l)"
} >> "$J.env"
S=${!#}
mkdir -p "$S/etape-3" || exit 3
echo '{"etape": 3, "factice": true}' > "$S/etape-3/manifeste.json"
(cd "$S/etape-3" && sha256sum manifeste.json > manifeste.json.sha256)
for i in 0 1 2; do mkdir -p "$S/etape-4/couche-mecanique/bras-1-a-3/factice/0.0/$i"; echo "$i" > "$S/etape-4/couche-mecanique/bras-1-a-3/factice/0.0/$i/x.txt"; done
sleep "${FAUX_DUREE_S:-4}"
echo '{"etape": 4, "factice": true}' > "$S/etape-4/manifeste.json"
(cd "$S/etape-4" && sha256sum manifeste.json > manifeste.json.sha256)
echo "faux programme : fin" >> "$J"
exit 0
