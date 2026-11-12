#!/usr/bin/env bash
# Enchaîneur détaché de P3-bis, v5 (ÉCART 2 : R-2450 ; nœud R-2446 ; défaut D3 de la consigne
# `consigne-developpeur-p3bis-ecart2-v1.md`, `1fd50996…`), écrit le 2026-11-12 vers 20:48 UTC (heure relevée par `date -u`).
# PREMIÈRE VERSION AU DÉPÔT : les v1 à v4 n'ont vécu que dans le bac à sable de la session fille ; v5 est RECONSTRUIT sur
# les descriptions du registre des décisions, sans leur texte :
#   R-2392 : « un enchaîneur détaché qui ne fait qu'appeler les scripts de la chaîne avec leurs arguments d'usage —
#            lanceur, puis, sur le code 0 et la ligne `instance`, attente jusqu'à création + 181 s, contrôle à cinq
#            minutes, puis surveillance — sans autre logique » ; détaché (`setsid nohup`), PID noté, arrêt par ce PID (R10) ;
#   R-2393 : v1 (`13b3a6b2…`, 38 lignes) : lignes `instance` et `creation` de lancement.txt (`creation` en secondes) ;
#            surveillance (dépense antérieure 0) ; chaque code et chaque heure au journal ; aucun arrêt, destruction ni
#            récupération ; jeton exporté depuis `_2` (R-2387) ; la surveillance suit QUEL QUE SOIT le code du contrôle à
#            cinq minutes (code 1 : instance déjà arrêtée ; code 2 : la surveillance reste la garde) ;
#   R-2394 : v2 « paramétré » ; R-2408 : v3 (`a35e7a21…`) = v2 sauf l'appel du lanceur d'écart ;
#   R-2416 : v4 (`19728737…`) = v3 sauf la ligne 31, `CR + 181` → `CR + 290`.
# Ce que v5 fait : (1) vérifie les empreintes des quatre pièces d'écart qu'il appelle (lanceur d'écart 1 v2, épinglé par
# R-2407 ; contrôle à cinq minutes, surveillance et module commun d'écart 2), avant tout appel, puis de nouveau juste
# avant chaque appel ; une empreinte autre : aucun appel (code 2) ; (2) appelle le lanceur d'écart 1 v2 (inchangé), qui
# compare les scripts d'origine de la chaîne, restés dans ce dossier, à leurs copies versées à S (bloc 2) ; (3) sur le
# code 0 et une seule ligne `instance` et `creation`, attend la création + 181 s (comme v1 à v3 : le contrôle d'écart
# attend lui-même jusqu'à son échéance) et appelle le contrôle à cinq minutes d'ÉCART 2 ; (4) appelle la surveillance
# d'ÉCART 2 quel que soit le code du contrôle (R-2393), avec la dépense antérieure passée en argument ; (5) écrit chaque
# code et chaque heure (`date -u`) au journal ; aucun arrêt, aucune destruction, aucune récupération, aucune relance.
# Écarts déclarés aux v1 à v4 décrits : contrôle et surveillance d'écart 2 au lieu de ceux de S ; contrôle appelé à la
# création + 181 s (v4 : + 290 s) ; dépense antérieure en argument (v1 : 0 ; le texte compte toutes tentatives et
# relances) ; empreintes épinglées vérifiées ; jeton : `CONTROLE_IA_GITHUB_TOKEN` gardé s'il est présent, sinon exporté
# depuis `CONTROLE_IA_GITHUB_TOKEN_2` (R-2387 ; nom seul écrit, jamais la valeur) ; noms des fichiers du dossier neuf.
# Non reconstructibles à l'identique : le texte des v1 à v4, la forme exacte de leurs arguments, de leur journal et de
# leurs messages.
# Codes : 0 surveillance finie par un arrêt par l'identifiant (son code) ; code du lanceur s'il n'est pas 0 (2, 3 ou 4 ;
# 4 : création douteuse, vérifier les instances, forme filtrée) ; 2 usage, dossier existant, empreinte autre, traces du
# lancement illisibles ; sinon le code de la surveillance (1 : arrêt en échec, à faire à la main par l'identifiant).
# Usage (détaché, depuis le dossier de la chaîne de la branche d'écart, où les scripts d'origine sont égaux à S) :
#   setsid nohup bash enchaineur_p3bis_v5.sh S DOSSIER_NEUF EN_MARCHE N DEPENSE_ANTERIEURE_USD \
#       > DOSSIER_NEUF.console.txt 2>&1 < /dev/null &   puis noter le PID ($!) ; arrêt seulement par ce PID (R10)
#   S            commit de scellement du texte (40 caractères) ;
#   DOSSIER_NEUF dossier neuf (R12) : traces/ (lanceur), cinq-minutes/, surveillance/, enchaineur.txt, consoles ;
#   EN_MARCHE    instances en marche d'autres courses, « ID:GO-…,… » ou « - » (passé au lanceur) ;
#   N            tentative : 1, 2 ou 3 (passée au lanceur) ;
#   DEPENSE_ANTERIEURE_USD  dépense de la course déjà faite, toutes tentatives et relances comprises (passée à la surveillance).
set -uo pipefail
ATTENTE_CINQ_S=181                               # appel du contrôle à cinq minutes : création + 181 s (R-2392)
LANCEUR=lancer_p3bis_v2_ecart1_v2.sh;             E_LANCEUR=2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb
CINQ=controle_cinq_minutes_p3bis_v2_ecart2_v1.sh; E_CINQ=6aa165e50d11ac1161686b79b1b690ff23e2528abf833b693f7874701f3cd66f
SURV=surveiller_p3bis_v2_ecart2_v1.sh;            E_SURV=555ee5223ccb1742d890b8cc2e6da74dba0a1a98d743ed1b3234eb67998c19db
MODULE=verifications_p3bis_v2_ecart2_v1.py;       E_MODULE=ba6deb689b92cab04f580165b955e2c69c9558a5e229f0f7f1ef170aba89107e
H=$(dirname "$(realpath "$0")")
[ $# -eq 5 ] && [ -n "$2" ] || { echo "usage : enchaineur_p3bis_v5.sh S DOSSIER_NEUF EN_MARCHE N DEPENSE_ANTERIEURE_USD"; exit 2; }
S=$1; D=$(realpath -m "$2"); EN_MARCHE=$3; N=$4; ANT=$5
[[ "$ANT" =~ ^[0-9]+(\.[0-9]+)?$ ]] || { echo "DEPENSE_ANTERIEURE_USD : nombre positif en USD attendu ($ANT)"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
epingle() {   # $1 fichier du dossier, $2 empreinte épinglée
    [ "$(sha256sum "$H/$1" 2>/dev/null | cut -d' ' -f1)" = "$2" ]
}
for p in "$LANCEUR=$E_LANCEUR" "$CINQ=$E_CINQ" "$SURV=$E_SURV" "$MODULE=$E_MODULE"; do
    epingle "${p%%=*}" "${p#*=}" || { echo "${p%%=*} : absent ou d'empreinte autre que l'épinglée (${p#*=}) : aucun appel"; exit 2; }
done
mkdir -p "$D" || exit 2
JN="$D/enchaineur.txt"
note() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JN"; }
J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}; J_GH2=${CONTROLE_IA_GITHUB_TOKEN_2:-}
if [ "${#J_GH}" -lt 8 ] && [ "${#J_GH2}" -ge 8 ]; then
    export CONTROLE_IA_GITHUB_TOKEN="$J_GH2"
    note "jeton : CONTROLE_IA_GITHUB_TOKEN exporté depuis CONTROLE_IA_GITHUB_TOKEN_2 (R-2387 ; valeur jamais écrite)"
fi
unset J_GH J_GH2
note "enchaîneur p3bis v5 $(sha256sum "$0" | cut -d' ' -f1) ; PID $$ ; S $S ; EN_MARCHE $EN_MARCHE ; N $N ; dépense antérieure $ANT USD ; dossier $D"
note "empreintes épinglées vérifiées : $LANCEUR $E_LANCEUR ; $CINQ $E_CINQ ; $SURV $E_SURV ; $MODULE $E_MODULE"
# 1. lanceur d'écart 1 v2
note "lanceur : appel de $LANCEUR"
c=0; bash "$H/$LANCEUR" "$S" "$D/traces" "$EN_MARCHE" "$N" > "$D/console-lanceur.txt" 2>&1 || c=$?
note "lanceur : code $c ; dernière ligne : $(grep -v '^$' "$D/console-lanceur.txt" | tail -1 | cut -c1-200)"
if [ "$c" != 0 ]; then
    note "ENCHAÎNEUR : fin sans contrôle ni surveillance (lanceur, code $c$( [ "$c" = 4 ] && echo ' : création douteuse, vérifier les instances, forme filtrée' ))"
    exit "$c"
fi
L="$D/traces/lancement.txt"
ID=$(sed -n 's/^instance \([0-9][0-9]*\)$/\1/p' "$L" 2>/dev/null); CR=$(sed -n 's/^creation \([0-9][0-9]*\)$/\1/p' "$L" 2>/dev/null)
if [ "$(printf '%s\n' "$ID" | grep -c .)" != 1 ] || [ "$(printf '%s\n' "$CR" | grep -c .)" != 1 ]; then
    note "ENCHAÎNEUR : traces du lancement illisibles (une seule ligne « instance » et « creation » attendue) : aucun contrôle, aucune surveillance ; vérifier les instances"
    exit 2
fi
note "instance $ID créée (creation $CR) ; contrôle à cinq minutes d'écart 2 à la création + $ATTENTE_CINQ_S s"
# 2. contrôle à cinq minutes d'écart 2, à la création + 181 s (il attend lui-même jusqu'à son échéance)
while [ "$(date -u +%s)" -lt $((CR + ATTENTE_CINQ_S)) ]; do sleep 5; done
cc=0
if epingle "$CINQ" "$E_CINQ"; then
    note "contrôle à cinq minutes : appel (création + $(( $(date -u +%s) - CR )) s)"
    bash "$H/$CINQ" "$ID" "$D/traces" "$D/cinq-minutes" > "$D/console-cinq-minutes.txt" 2>&1 || cc=$?
    note "contrôle à cinq minutes : code $cc ; dernière ligne : $(grep -v '^$' "$D/console-cinq-minutes.txt" | tail -1 | cut -c1-200)"
else
    cc=2; note "contrôle à cinq minutes : $CINQ d'empreinte autre que l'épinglée juste avant l'appel : non joué (code 2) ; la surveillance reste la garde"
fi
# 3. surveillance d'écart 2, quel que soit le code du contrôle (R-2393)
if ! epingle "$SURV" "$E_SURV" || ! epingle "$MODULE" "$E_MODULE"; then
    note "ENCHAÎNEUR : $SURV ou $MODULE d'empreinte autre que l'épinglée juste avant l'appel : SURVEILLANCE NON LANCÉE ; instance $ID à surveiller ou arrêter par la session, par son identifiant (R10)"
    exit 2
fi
note "surveillance : appel (dépense antérieure $ANT USD ; contrôle à cinq minutes, code $cc)"
cs=0; bash "$H/$SURV" "$ID" "$D/traces" "$ANT" "$D/surveillance" > "$D/console-surveillance.txt" 2>&1 || cs=$?
note "surveillance : code $cs ; dernière ligne : $(grep -v '^$' "$D/console-surveillance.txt" | tail -1 | cut -c1-200)"
note "ENCHAÎNEUR : fin ; lanceur 0 ; contrôle à cinq minutes $cc ; surveillance $cs ; suite par la session (récupération, destruction par l'identifiant seulement après la fin normale, ou nœud de Lazar)"
exit "$cs"
