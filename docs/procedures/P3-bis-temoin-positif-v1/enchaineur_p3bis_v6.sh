#!/usr/bin/env bash
# Enchaîneur détaché de P3-bis, v6 (ÉCART 3 : R-2492 ; consigne `consigne-developpeur-p3bis-ecart3-v1.md`, `09311f1c…`),
# écrit le 2026-11-13 vers 07:55 UTC (heure relevée par `date -u`) par un développeur neuf.
# v6 = enchaîneur v5 (`enchaineur_p3bis_v5.sh`, `34131eaf…`, gardé tel quel, R12) dont le SEUL changement de logique est le
# lanceur appelé : le LANCEUR D'ORIGINE SCELLÉ `lancer_p3bis_v2.sh` (égal à sa copie versée à S, `029bdb5c…`, cité par le
# texte l. 2174-2175), au lieu du lanceur d'écart 1 v2 (`lancer_p3bis_v2_ecart1_v2.sh`, `2e294e5a…`). La garde du crédit
# d'origine est ainsi rétablie : « crédit ≥ 20 USD plus 10 heures du prix des instances nommées en marche » (texte,
# l. 1936-1937 et 2150-2152 ; module commun d'origine, sous-commande `credit`) ; l'écart 1 (R-2399, addendum 1) est retiré,
# sa prémisse (la recharge automatique du compte) ayant échoué (R-2491). Le lanceur d'origine compare lui-même « $0 »
# (son propre chemin, donc ce fichier du dossier) à sa copie versée à S (bloc 2).
# Inchangés depuis v5 : contrôle à cinq minutes, surveillance et module commun d'ÉCART 2, mêmes empreintes épinglées ;
# vérification des épingles avant tout appel puis juste avant le contrôle et la surveillance (le lanceur est appelé juste
# après la vérification de départ, comme en v5) ; jeton ; attente de la création + 181 s ; surveillance quel que soit le
# code du contrôle (R-2393) ; dépense antérieure en argument ; journal ; codes ; aucun arrêt, aucune destruction, aucune
# récupération, aucune relance par l'enchaîneur.
# Changé depuis v5, et rien d'autre : (1) la ligne `LANCEUR=…; E_LANCEUR=…` ; (2) le nom dans le message d'usage ; (3)
# l'étiquette du journal « enchaîneur p3bis v6 » ; (4) cet en-tête et les commentaires qui nommaient le lanceur d'écart 1.
# Les arguments passés au lanceur sont ceux de v5 (S, DOSSIER_NEUF/traces, EN_MARCHE, N) : l'usage du lanceur d'origine est
# le même que celui du lanceur d'écart 1 (« lancer_p3bis_v2.sh S DOSSIER_TRACES EN_MARCHE N »).
# Historique de v1 à v5 : voir l'en-tête de `enchaineur_p3bis_v5.sh` (R-2392, R-2393, R-2394, R-2408, R-2416, R-2450).
# Codes : 0 surveillance finie par un arrêt par l'identifiant (son code) ; code du lanceur s'il n'est pas 0 (2, 3 ou 4 ;
# 3 : date limite, place, crédit sous le minimum ou aucune offre conforme ; 4 : création douteuse, vérifier les instances,
# forme filtrée) ; 2 usage, dossier existant, empreinte autre, traces du lancement illisibles ; sinon le code de la
# surveillance (1 : arrêt en échec, à faire à la main par l'identifiant).
# Usage (détaché, depuis le dossier de la chaîne de la branche d'écart, où les scripts d'origine sont égaux à S) :
#   setsid nohup bash enchaineur_p3bis_v6.sh S DOSSIER_NEUF EN_MARCHE N DEPENSE_ANTERIEURE_USD \
#       > DOSSIER_NEUF.console.txt 2>&1 < /dev/null &   puis noter le PID ($!) ; arrêt seulement par ce PID (R10)
#   S            commit de scellement du texte (40 caractères) ;
#   DOSSIER_NEUF dossier neuf (R12) : traces/ (lanceur), cinq-minutes/, surveillance/, enchaineur.txt, consoles ;
#   EN_MARCHE    instances en marche d'autres courses, « ID:GO-…,… » ou « - » (passé au lanceur) ;
#   N            tentative : 1, 2 ou 3 (passée au lanceur ; sous l'écart 3 : 2, branche calcul/p3bis-reel-v2) ;
#   DEPENSE_ANTERIEURE_USD  dépense de la course déjà faite, toutes tentatives et relances comprises (passée à la surveillance).
set -uo pipefail
ATTENTE_CINQ_S=181                               # appel du contrôle à cinq minutes : création + 181 s (R-2392)
LANCEUR=lancer_p3bis_v2.sh;                       E_LANCEUR=029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08
CINQ=controle_cinq_minutes_p3bis_v2_ecart2_v1.sh; E_CINQ=6aa165e50d11ac1161686b79b1b690ff23e2528abf833b693f7874701f3cd66f
SURV=surveiller_p3bis_v2_ecart2_v1.sh;            E_SURV=555ee5223ccb1742d890b8cc2e6da74dba0a1a98d743ed1b3234eb67998c19db
MODULE=verifications_p3bis_v2_ecart2_v1.py;       E_MODULE=ba6deb689b92cab04f580165b955e2c69c9558a5e229f0f7f1ef170aba89107e
H=$(dirname "$(realpath "$0")")
[ $# -eq 5 ] && [ -n "$2" ] || { echo "usage : enchaineur_p3bis_v6.sh S DOSSIER_NEUF EN_MARCHE N DEPENSE_ANTERIEURE_USD"; exit 2; }
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
note "enchaîneur p3bis v6 $(sha256sum "$0" | cut -d' ' -f1) ; PID $$ ; S $S ; EN_MARCHE $EN_MARCHE ; N $N ; dépense antérieure $ANT USD ; dossier $D"
note "empreintes épinglées vérifiées : $LANCEUR $E_LANCEUR ; $CINQ $E_CINQ ; $SURV $E_SURV ; $MODULE $E_MODULE"
# 1. lanceur d'origine scellé (écart 3 : garde du crédit d'origine rétablie)
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
