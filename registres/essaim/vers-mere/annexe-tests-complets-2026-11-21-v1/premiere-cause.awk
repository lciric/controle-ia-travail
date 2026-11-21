# Pour chaque section d'échec de la sortie de pytest : nom de l'essai, fichier:ligne, première ligne de refus (sinon première ligne E).
function sortir() { if (nom != "") print nom "\t" ou "\t" (r != "" ? r : e) }
/^_+ .+ _+$/ { sortir(); nom=$0; gsub(/^_+ | _+$/, "", nom); ou=""; r=""; e=""; next }
/^=+ (short test summary|FAILURES|ERRORS)/ { sortir(); nom=""; next }
nom != "" && /^tests\/[^ ]+\.py:[0-9]+: / { ou=$1 }
nom != "" && r == "" && /"refus"/ { r=substr($0, 1, 220) }
nom != "" && e == "" && /^E   / && !/where / { e=substr($0, 1, 220) }
