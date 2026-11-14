#!/usr/bin/env bash
# Essai (règle R5) de attestation_qui_a_lu_quoi_compte_3_v3.py sur la liste réelle v1 et sur des copies altérées (v2 ; la v1 reste).
#     bash essai_attestation_compte_3_v3.sh <dépôt> <bac neuf>
set -u
DEPOT=$(cd "$1" && pwd); BAC="$2"
[ ! -e "$BAC" ] || { echo "ARRÊT : $BAC existe déjà"; exit 1; }
mkdir -p "$BAC"; BAC=$(cd "$BAC" && pwd)
A="$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1/attestation_qui_a_lu_quoi_compte_3_v3.py"
L="$DEPOT/registres/qui-a-lu-quoi-v1.md"; H=$(sha256sum "$L" | cut -d' ' -f1)
S=session_01ESSAIcompte3XXXXXXXXXX
export LC_ALL=C.UTF-8
date -u +"début de l'essai : %Y-%m-%dT%H:%M:%SZ"; echo "script essayé : $(sha256sum "$A" | cut -d' ' -f1) ; liste : $H"
OK=0; KO=0
cas() { local nom="$1" attendu="$2" motif="$3"; shift 3; local s c; s=$(python3 -I -B "$A" "$@" 2>&1); c=$?
  if [ "$c" = "$attendu" ] && printf '%s' "$s" | grep -qF -- "$motif"; then OK=$((OK+1)); echo "conforme : $nom (code $c)";
  else KO=$((KO+1)); echo "ÉCART : $nom (code $c, attendu $attendu)"; printf '%s\n' "$s" | sed 's/^/    /'; fi; }
copie() { cp "$L" "$BAC/$1.md"; }
scelle() { (cd "$BAC" && sha256sum "$1.md" > "$1.md.sha256"); sha256sum "$BAC/$1.md" | cut -d' ' -f1; }
cas "T1 liste réelle v1, session neuve : conforme, une ligne du compte 3 sans exclusion" 0 "1 sans exclusion, 0 d'une autre session" "$L" "$H" "$S"
copie t2; printf '\nNote : %s\n' "$S" >> "$BAC/t2.md"; cas "T2 session citée en entier" 2 "figure dans la liste" "$BAC/t2.md" "$(scelle t2)" "$S"
copie t2b; printf '\nNote : session_01ESSAIcompt…\n' >> "$BAC/t2b.md"; cas "T2b douze premiers caractères cités (identifiant tronqué)" 2 "douze premiers caractères" "$BAC/t2b.md" "$(scelle t2b)" "$S"
copie t3; sed -i 's/| aucune exclusion déclarée |$/| lecteur du verdict de P3-bis |/' "$BAC/t3.md"; cas "T3 ligne du compte 3 sans identifiant, avec une exclusion" 2 "sans identifiant de session" "$BAC/t3.md" "$(scelle t3)" "$S"
copie t3b; printf '| 997 | session_01LOTcompte3NARCBENCHxx (lot du compte 3) | compte 3 | modèle A | texte scellé de T0.7 | lot NARCBench | essai | lecteur de P3-bis |\n' >> "$BAC/t3b.md"; cas "T3b autre session identifiée du compte 3 avec une exclusion : admise" 0 "1 d'une autre session identifiée" "$BAC/t3b.md" "$(scelle t3b)" "$S"
copie t3c; printf '| 996 | %s (hôte) | compte 3 | modèle A | sortie de 7b | essai | essai | lecteur de 7b |\n' "$S" >> "$BAC/t3c.md"; cas "T3c ligne qui nomme la session hôte" 2 "figure dans la liste" "$BAC/t3c.md" "$(scelle t3c)" "$S"
cas "T4 empreinte attendue autre" 2 "empreinte" "$L" "$(printf '0%.0s' $(seq 64))" "$S"
copie t5; cas "T5 liste sans compagnon" 2 "compagnon absent" "$BAC/t5.md" "$(sha256sum "$BAC/t5.md" | cut -d' ' -f1)" "$S"
copie t6; sed -i 's/| exclu de |$/| exclusions |/' "$BAC/t6.md"; cas "T6 en-tête sans « exclu de »" 2 "en-tête du tableau" "$BAC/t6.md" "$(scelle t6)" "$S"
copie t7; printf '| 999 | session non nommée | Compte-3 | non déclaré | sortie de 7b | essai | essai | lecteur de 7b |\n' >> "$BAC/t7.md"; cas "T7 « Compte-3 » sans identifiant, avec une exclusion" 2 "sans identifiant de session" "$BAC/t7.md" "$(scelle t7)" "$S"
copie t8; printf '| 998 | session non nommée | compte 30 | non déclaré | sortie de 7b | essai | essai | lecteur de 7b |\n' >> "$BAC/t8.md"; cas "T8 « compte 30 » n'est pas le compte 3" 0 "1 sans exclusion" "$BAC/t8.md" "$(scelle t8)" "$S"
cas "T9 session hors forme" 1 "ERREUR D'APPEL" "$L" "$H" "session_court"
CELL="analyse du verdict A ; étape B bis (conception et verdicts) ; T0.8 ; G0 ; préenregistrement NARCBench (rédaction, contre-lecture, course) ; brouillons des papiers B et C ; code de la pièce « mots et coût »"
copie h1; printf '| 995 | %s (hôte du verdict A) | compte 3 | modèle A | rien ouvert | hôte | P3A-004 | %s |\n' "$S" "$CELL" >> "$BAC/h1.md"; HH=$(scelle h1)
cas "H1 ligne de l'hôte à la cellule admise, avec --admettre-hote" 0 "lignes de l'hôte admises : 1" "$BAC/h1.md" "$HH" "$S" --admettre-hote "$CELL"
cas "H2 même liste sans --admettre-hote" 2 "figure dans la liste" "$BAC/h1.md" "$HH" "$S"
copie h3; printf '| 994 | %s (hôte) | compte 3 | modèle A | rien ouvert | hôte | P3A-004 | %s ; étape B de T0.7 |\n' "$S" "$CELL" >> "$BAC/h3.md"
cas "H3 ligne de l'hôte à une autre cellule (étape B nommée)" 2 "hors de la forme admise" "$BAC/h3.md" "$(scelle h3)" "$S" --admettre-hote "$CELL"
copie h4; printf '| 995 | %s (hôte du verdict A) | compte 3 | modèle A | rien ouvert | hôte | P3A-004 | %s |\n' "$S" "$CELL" >> "$BAC/h4.md"; printf '\nNote : session_01ESSAIcompt…\n' >> "$BAC/h4.md"
cas "H4 ligne admise, mais identifiant tronqué ailleurs" 2 "douze premiers caractères" "$BAC/h4.md" "$(scelle h4)" "$S" --admettre-hote "$CELL"
copie h5; printf '| 993 | session non nommée | compte 3 | modèle A | rien | hôte | vu %s | %s |\n' "$S" "$CELL" >> "$BAC/h5.md"
cas "H5 identifiant de l'hôte hors de la colonne « session »" 2 "hors de la forme admise" "$BAC/h5.md" "$(scelle h5)" "$S" --admettre-hote "$CELL"
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "ESSAI : TOUT CONFORME" || echo "ESSAI : ÉCARTS"
date -u +"fin de l'essai : %Y-%m-%dT%H:%M:%SZ"
