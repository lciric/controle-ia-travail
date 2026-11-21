#!/bin/bash
# Faux pip : écrit ses arguments dans $FAUX_JOURNAL ; « install » échoue (1) si FAUX_PIP_ECHEC est non vide.
# Artefacts de la fenêtre (c) -> (f), joués à « install », sur la racine ESSAI_DEMARRAGE_BASE/racine :
#   FAUX_PIP_ALTERER=CHEMIN : un octet ajouté au fichier CHEMIN ;
#   FAUX_PIP_PLANTE=MODE (v3, table du contre-lecteur, plus git-valide) : fichier | lien | dossier-vide | chmod |
#     git-fichier | sous-git | git-vide | git-valide | modif | suppression.
echo "faux pip : $*" >> "${FAUX_JOURNAL:-/dev/null}"
[ "${1:-}" = install ] || exit 0
if [ -n "${FAUX_PIP_ECHEC:-}" ]; then echo "faux pip : échec voulu" >&2; exit 1; fi
[ -z "${FAUX_PIP_ALTERER:-}" ] || echo "x" >> "$FAUX_PIP_ALTERER"
R=${ESSAI_DEMARRAGE_BASE:-/nulle-part}/racine
case "${FAUX_PIP_PLANTE:-}" in
  fichier) echo "intrus" > "$R/nouveau-fichier.txt" ;;
  lien) ln -s /etc/hostname "$R/lien-ajoute" ;;
  dossier-vide) mkdir "$R/dossier-vide-ajoute" ;;
  chmod) chmod 755 "$R/requirements-cpu.txt" ;;
  git-fichier) echo "gitdir: /nulle/part" > "$R/.git" ;;
  sous-git) mkdir -p "$R/docs/.git" ;;
  git-vide) /usr/bin/git init -q "$R" ;;
  git-valide) /usr/bin/git init -q "$R" && /usr/bin/git -C "$R" fetch -q "${ESSAI_DEMARRAGE_BASE}/depot.git" \
      d7f949acd9ac92e998e57663d2cc741de93f18c3 && /usr/bin/git -C "$R" reset -q --mixed d7f949acd9ac92e998e57663d2cc741de93f18c3 ;;
  modif) echo "x" >> "$R/requirements-cpu.txt" ;;
  suppression) rm -f "$R/requirements-cpu.txt" ;;
esac
exit 0
