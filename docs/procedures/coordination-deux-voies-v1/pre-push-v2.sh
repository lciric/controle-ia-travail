#!/bin/sh
# Garde locale pre-push v2 du dépôt de travail.
# 1. R-116 : refuse toute poussée vers lciric/controle-ia (nom réservé à la copie expurgée publique).
# 2. Protocole de coordination v1 (docs/procedures/coordination-deux-voies-v1.md) :
#    - la voie de la session est écrite dans <git-dir>/voie (« redaction » ou « calcul ») ; sans elle, rien ne part ;
#    - main ne reçoit que de la session qui tient le bail (fichier <git-dir>/bail-main) ;
#    - une branche coord/<voie> ne reçoit que de sa voie ;
#    - sur main et sur coord/*, ni suppression ni poussée non linéaire (forcée).
# Sortie 0 : la poussée passe ; sortie 1 : refusée, motif sur la sortie d'erreur. Aucun repli silencieux (R5).
url="$2"
case "$url" in
  *lciric/controle-ia-travail|*lciric/controle-ia-travail.git|*lciric/controle-ia-travail/) ;;
  *lciric/controle-ia|*lciric/controle-ia.git|*lciric/controle-ia/)
    echo "pre-push : poussée vers lciric/controle-ia refusée (R-116)" >&2; exit 1 ;;
esac
gd=$(git rev-parse --git-dir) || { echo "pre-push : dossier git introuvable" >&2; exit 1; }
voie=$(cat "$gd/voie" 2>/dev/null)
case "$voie" in
  redaction|calcul) ;;
  *) echo "pre-push : voie absente ou inconnue dans $gd/voie (protocole de coordination v1)" >&2; exit 1 ;;
esac
while read -r lref lsha rref rsha; do
  [ -n "$rref" ] || continue
  case "$rref" in
    refs/heads/main)
      [ -f "$gd/bail-main" ] || { echo "pre-push : poussée sur main sans le bail (protocole de coordination v1)" >&2; exit 1; } ;;
    refs/heads/coord/*)
      [ "$rref" = "refs/heads/coord/$voie" ] || { echo "pre-push : $rref appartient à une autre voie que « $voie »" >&2; exit 1; } ;;
  esac
  case "$rref" in
    refs/heads/main|refs/heads/coord/*)
      case "$lsha" in
        *[!0]*) ;;
        *) echo "pre-push : suppression de $rref refusée" >&2; exit 1 ;;
      esac
      case "$rsha" in
        *[!0]*)
          git merge-base --is-ancestor "$rsha" "$lsha" 2>/dev/null || {
            echo "pre-push : poussée non linéaire sur $rref refusée (relire le dépôt distant : git fetch)" >&2; exit 1; } ;;
      esac ;;
  esac
done
exit 0
