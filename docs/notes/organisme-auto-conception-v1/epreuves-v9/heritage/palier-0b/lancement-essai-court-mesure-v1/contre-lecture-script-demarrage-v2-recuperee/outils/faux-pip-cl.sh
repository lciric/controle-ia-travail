#!/bin/bash
# Faux pip CL : « install » altere la racine selon CL_PIP_PLANTE, apres le controle du pas c (donc dans la fenetre c -> f).
# CL_PIP_PLANTE : fichier | lien | dossier-vide | chmod | git-fichier | sous-git | modif | suppression | git-vide
echo "faux pip CL : $* ; plante=${CL_PIP_PLANTE:-rien}" >> "${FAUX_JOURNAL:-/dev/null}"
[ "${1:-}" = install ] || exit 0
R=${ESSAI_DEMARRAGE_BASE:-/nonexistent}/racine
case "${CL_PIP_PLANTE:-}" in
  fichier) echo "intrus" > "$R/nouveau-fichier-cl.txt" ;;
  lien) ln -s /etc/hostname "$R/lien-cl" ;;
  dossier-vide) mkdir "$R/dossier-vide-cl" ;;
  chmod) chmod 755 "$R/requirements-cpu.txt" ;;
  git-fichier) echo "gitdir: /nulle/part" > "$R/.git" ;;
  sous-git) mkdir -p "$R/docs/.git" ;;
  git-vide) /usr/bin/git init -q "$R" ;;
  modif) echo "x" >> "$R/requirements-cpu.txt" ;;
  suppression) rm -f "$R/requirements-cpu.txt" ;;
esac
exit 0
