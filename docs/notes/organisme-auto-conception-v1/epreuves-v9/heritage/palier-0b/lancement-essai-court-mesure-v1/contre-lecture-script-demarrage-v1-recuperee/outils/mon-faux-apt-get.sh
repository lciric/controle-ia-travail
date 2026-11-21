#!/bin/bash
# Contre-lecteur : faux apt-get qui relève, dans $FAUX_JOURNAL.apt-env, les NOMS des variables d'environnement reçues et le
# nombre de lignes de son environnement qui portent le jeton factice (fichier ESSAI_JETON_FICHIER).
echo "faux apt-get : $*" >> "${FAUX_JOURNAL:-/dev/null}"
if [ -n "${ESSAI_JETON_FICHIER:-}" ]; then
  {
    echo "apt : lignes d'environnement portant le jeton : $(tr '\0' '\n' < /proc/$$/environ | grep -c -F -f "$ESSAI_JETON_FICHIER")"
    echo "apt : noms reçus : $(tr '\0' '\n' < /proc/$$/environ | cut -d= -f1 | grep -E '^(DEBIAN_FRONTEND|GIT_|HOME|JETON|ESSAI_DEMARRAGE_)' | sort | tr '\n' ' ')"
  } >> "${FAUX_JOURNAL:-/dev/null}.apt-env"
fi
exit 0
