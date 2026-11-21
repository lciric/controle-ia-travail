#!/bin/bash
# Résumé des sorties de scénarios (lecture seule) : pour chaque fichier, le code de sortie écrit, la raison d'arrêt, les
# signaux, l'état du dossier, n, la note de fin, l'état des témoins et des processus du marqueur.
# Usage : resumer-v4.sh FICHIER...
for f in "$@"; do
  echo "##### $(basename "$f")"
  grep -A1 -- '^--- code-de-sortie.txt :' "$f" | tail -n 1 | sed 's/^/code écrit : /'
  grep -E -- '^--- code-de-sortie.txt : \(absent\)' "$f"
  grep -E '^raison : ' "$f"
  grep -E 'signal de fin envoyé|signal d.arrêt forcé|arrêt forcé :|aucun signal envoyé|descendant hors du groupe|arrêt des descendants|encore présents|tous absents|tous les membres' "$f" | cut -c1-230
  grep -E '^état du dossier|^n : |projection impossible|durée projetée de l|garde continue' "$f" | cut -c1-230
  grep -E -- '^--- mesure-essai-3.txt : \(absent\)|^--- arret-gardien.txt : \(absent\)' "$f"
  grep -E -- '^--- témoin|^--- processus du marqueur|^--- marqueur|ENCORE VIVANT|^=== gardien|^--- après coup' "$f" | cut -c1-230
  grep -o 'note=[^;]*$' "$f" | tail -n 1
  grep -E 'arrêt de mesure (armé|désarmé)' "$f" | grep -o 'arrêt de mesure [a-zé]*' | head -n 1
done
