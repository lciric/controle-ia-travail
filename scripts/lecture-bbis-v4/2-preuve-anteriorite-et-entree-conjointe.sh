#!/bin/bash
# § 2 — preuve d'antériorité et preuve d'entrée conjointe, relevées à part
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 2 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/2-preuve-anteriorite-et-entree-conjointe.sh
. "$(dirname "$0")/commun.sh"
grep -q "CONCLUSION : conforme" "$(dernier_releve_des_tetes)" || { echo "releve-mise-en-place non conforme : arrêt"; exit 1; }
for f in releve-entrees releve-code-et-textes; do grep -q "CONCLUSION : conforme" "$T/$f.txt" || { echo "$f non conforme : arrêt"; exit 1; }; done
P="$LV1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt"; neuf "$P"
sha() { sha256sum | cut -d' ' -f1; }
ct() { G show -s --format=%ct "$1"; }
cd "$ARBRE" || exit 1
{
dire "Preuve d'antériorité et preuve d'entrée conjointe — lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7)"
dire "relevée le $(date -u +%Y-%m-%dT%H:%M:%SZ), dans $ARBRE, par commandes git en lecture, environnement sans variable GIT_ ; aucun fichier de résultat ouvert ; le module de lecture n'est pas importé"
dire "== (A) histoire et tête"
egal "dépôt non superficiel" false "$(G rev-parse --is-shallow-repository)"
TETE="$(G rev-parse HEAD)"; dire "tête de l'arbre de lecture : $TETE"
vrai "le commit de la course $COURSE est un ancêtre de la tête" G merge-base --is-ancestor "$COURSE" "$TETE"
vrai "le commit de main $MAIN_INSCRIPTIONS est un ancêtre de la tête" G merge-base --is-ancestor "$MAIN_INSCRIPTIONS" "$TETE"
dire "== (B) antériorité du scellement sur l'étape B"
set -- $(G log --all --reverse --format='%H %ct' -S '| SCELLEMENT-BBIS |' -- "$PROPRE" | head -n 1); CS="${1:-}"; TS="${2:-}"
dire "commit qui ajoute SCELLEMENT-BBIS : $CS (instant $TS)"
egal "ce commit est celui que le quatrième addendum relève" f72d283347534d761fff63f6d744415cdf1bf32c "$CS"
for motif in '*lecture-t07.json' '*arret-etape-b.json'; do
  set -- $(G log --all --reverse --diff-filter=A --format='%H %ct' -- "$motif" | head -n 1); C1="${1:-}"; T1="${2:-}"
  if [ -z "$C1" ]; then dire "CONFORME : aucun commit n'ajoute $motif"
  elif [ -n "$TS" ] && [ "$T1" -gt "$TS" ]; then dire "CONFORME : premier ajout de $motif par $C1 (instant $T1), strictement postérieur au scellement"
  else dire "DEFAUT : premier ajout de $motif par $C1 (instant $T1), non postérieur au scellement"; FAUTES=$((FAUTES+1)); fi
done
dire "== (C) ordre des lignes du registre propre (dates écrites)"
date_de() { grep -F -- "$1" "$PROPRE" | cut -d'|' -f3 | tr -d ' '; }
D_SC="$(date_de '| SCELLEMENT-BBIS |')"; D_C1="$(date_de 'code-bbis-v1.json')"; D_GO="$(date_de '| GO-BBIS |')"
D_C2="$(date_de 'code-bbis-v2.json')"; D_SO="$(date_de '| SCORES-BBIS |')"
dire "dates écrites : scellement $D_SC ; première fiche $D_C1 ; accord de calcul $D_GO ; fiche remplaçante $D_C2 ; scores $D_SO"
avant() { if [ -n "$2" ] && [ -n "$3" ] && [ "$2" \< "$3" ]; then dire "CONFORME : $1"; else dire "DEFAUT : $1"; FAUTES=$((FAUTES+1)); fi; }
avant "scellement strictement avant la première fiche" "$D_SC" "$D_C1"
avant "première fiche strictement avant l'accord de calcul" "$D_C1" "$D_GO"
egal "accord de calcul et fiche remplaçante à la même seconde (seul couple de l'exception de QA-1)" "$D_GO" "$D_C2"
avant "fiche remplaçante strictement avant les scores" "$D_C2" "$D_SO"
avant "première fiche strictement avant la fiche remplaçante" "$D_C1" "$D_C2"
dire "== (D) preuve d'entrée conjointe (quatrième addendum, QA-1)"
L_CODE='| CODE-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/code-bbis-v2.json | 4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb |'
L_GO='| GO-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/go-bbis-v2.txt | 33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 |'
L_PREM='| CODE-BBIS | 2026-11-16T12:57:27Z | registres/t07-etape-b-bis/code-bbis-v1.json | ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469 |'
vrai "(P1) le commit de l'entrée conjointe $C_CONJ existe" G cat-file -e "$C_CONJ^{commit}"
set -- $(G rev-list --parents -n 1 "$C_CONJ"); egal "(P1) il a un seul parent" 2 "$#"; PAR="${2:-}"; dire "son parent : $PAR"
egal "(P2) au commit, la ligne de la fiche remplaçante, une fois, à l'octet" 1 "$(G show "$C_CONJ:$PROPRE" | grep -c -x -F -- "$L_CODE")"
egal "(P2) au commit, la ligne de l'accord de calcul, une fois, à l'octet" 1 "$(G show "$C_CONJ:$PROPRE" | grep -c -x -F -- "$L_GO")"
vrai "(P2) le registre propre existe au parent" G cat-file -e "$PAR:$PROPRE"
egal "(P2) au parent, lignes de clé CODE-BBIS ou GO-BBIS" 0 "$(G show "$PAR:$PROPRE" | grep -c -E '^\| *(CODE-BBIS|GO-BBIS) *\|')"
egal "(P3) au parent, le fichier de l'accord est présent" 1 "$(G ls-tree --full-tree "$PAR" -- registres/t07-etape-b-bis/go-bbis-v2.txt | wc -l | tr -d ' ')"
egal "(P3) au parent, son contenu a l'empreinte de la ligne" 33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 "$(G show "$PAR:registres/t07-etape-b-bis/go-bbis-v2.txt" | sha)"
egal "(P3) au parent, la fiche remplaçante est absente" 0 "$(G ls-tree --full-tree "$PAR" -- registres/t07-etape-b-bis/code-bbis-v2.json | wc -l | tr -d ' ')"
egal "(P3) au commit, la fiche remplaçante a l'empreinte de la ligne" 4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb "$(G show "$C_CONJ:registres/t07-etape-b-bis/code-bbis-v2.json" | sha)"
vrai "(P4) le commit de la remise de la première fiche $C_REMISE existe" G cat-file -e "$C_REMISE^{commit}"
set -- $(G rev-list --parents -n 1 "$C_REMISE"); egal "(P4) il a un seul parent" 2 "$#"; PAR2="${2:-}"; dire "son parent : $PAR2"
vrai "(P4) le commit de l'entrée conjointe en est un ancêtre" G merge-base --is-ancestor "$C_CONJ" "$C_REMISE"
egal "(P4) au commit, la ligne de la première fiche, une fois, à l'octet" 1 "$(G show "$C_REMISE:$PROPRE" | grep -c -x -F -- "$L_PREM")"
egal "(P4) à son parent, lignes qui citent la première fiche" 0 "$(G show "$PAR2:$PROPRE" | grep -c -F 'registres/t07-etape-b-bis/code-bbis-v1.json')"
vrai "(P5) le commit de la remise est un ancêtre du commit de la course" G merge-base --is-ancestor "$C_REMISE" "$COURSE"
vrai "(P5) le commit de la course est un ancêtre de la tête de l'arbre de lecture" G merge-base --is-ancestor "$COURSE" "$TETE"
dire "== (E) addenda, course, scores"
for k in ADDENDUM-ECART-1-BBIS ADDENDUM-ECART-2-BBIS ADDENDUM-ECART-3-BBIS ADDENDUM-ECART-4-BBIS ADDENDUM-ECART-4-COMPLEMENT-BBIS RATTACHEMENT-LECTURE-V5-BBIS; do
  set -- $(G log --all --reverse --format='%H %ct' -S "| $k |" -- "$VOISIN" | head -n 1); CA="${1:-}"
  dire "premier commit qui ajoute la ligne $k : $CA"
  vrai "ce commit est un ancêtre de la tête de l'arbre de lecture" G merge-base --is-ancestor "$CA" "$TETE"
  case "$k" in ADDENDUM-ECART-[123]-BBIS) vrai "ce commit est un ancêtre du commit de la course" G merge-base --is-ancestor "$CA" "$COURSE" ;; esac
done
egal "tête de la branche des sorties" "$TETE_SORTIES" "$(G rev-parse --verify -q "$REF_SORTIES")"
egal "le commit de la course est l'ancêtre commun des sorties et de la tête" "$COURSE" "$(G merge-base "$REF_SORTIES" "$TETE")"
vrai "le commit de la fiche de code est un ancêtre du commit de la course" G merge-base --is-ancestor "$C_FICHE" "$COURSE"
T_SO="$(date -u -d "$D_SO" +%s 2>/dev/null)"; T_TS="$(ct "$REF_SORTIES")"
if [ -n "$T_SO" ] && [ -n "$T_TS" ] && [ "$T_TS" -le "$T_SO" ]; then dire "CONFORME : la tête des sorties (instant $T_TS) précède la ligne SCORES-BBIS (instant $T_SO)"; else dire "DEFAUT : tête des sorties (instant $T_TS) et ligne SCORES-BBIS (instant $T_SO)"; FAUTES=$((FAUTES+1)); fi
egal "registre propre : lignes de lecture, de verdict ou de table conjointe" 0 "$(grep -c -E '^\| (LECTURE|VERDICT|CONJOINTE)-BBIS \|' "$PROPRE")"
conclure
} > "$P" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt"
grep -c '^CONFORME' "$P"; grep '^DEFAUT' "$P"; tail -n 2 "$P"; sha256sum "$P"
