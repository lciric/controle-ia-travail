# Pour chaque section d'échec : nom, fichier, et drapeaux de cause lus dans toute la section.
function sortir() { if (nom != "") print nom "\t" ou "\t" (ech ? "echeance " : "") (per ? "go_hors_periode " : "") (lst ? "liste " : "") (epi ? "epingle " : "") (orc ? "orchestrateur " : "") (rel ? "releve " : "") }
/^_+ .+ _+$/ { sortir(); nom=$0; gsub(/^_+ | _+$/, "", nom); ou=""; ech=per=lst=epi=orc=rel=0; next }
/^=+ (short test summary|FAILURES|ERRORS)/ { sortir(); nom=""; next }
nom != "" && /^tests\/[^ ]+\.py:[0-9]+: / { ou=$1 }
nom != "" && /après l'échéance|hors de \]maintenant, fin du GO\]/ { ech=1 }
nom != "" && /hors de sa période de validité/ { per=1 }
nom != "" && /ni dans la liste ni dans les exclusions/ { lst=1 }
nom != "" && /non épinglé/ { epi=1 }
nom != "" && /0 copie\(s\) trouvée\(s\)/ { orc=1 }
nom != "" && /un relevé du jour/ { rel=1 }
