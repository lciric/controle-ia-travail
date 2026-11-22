#!/bin/bash
# Banc du contrôle de sortie v1, entièrement sur factices : données fabriquées par le fabricant v8 (jeton FACTICE du
# dépôt, dépôt distant FACTICE vide), jeton FACTICE de l'interface (aléatoire, fichier 600, passé à l'outil sous le nom
# HC_FACTICE_BANC, jamais sous HCLOUD_TOKEN, qui est retiré de l'environnement de chaque appel par env -u), serveur
# FACTICE de l'interface sur 127.0.0.1. Écrit travail/table.txt.
# Emploi : banc-controle-sortie.sh
set -u
B=$(cd "$(dirname "$0")" && pwd); D=$(dirname "$B"); AUT=$(dirname "$D")
OUT=$D/controler-et-creer-essai-3-v1.py PY=/home/user/controle-ia-travail/.venv/bin/python
FAB=$AUT/v8/fabriquer-donnees-demarrage-v8.sh
W=$D/travail
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/donnees" "$W/releves" "$W/sorties" "$W/pause"
T=$W/table.txt; : > "$T"
JD=$AUT/essais/travail/jeton-factice.txt JA=$AUT/essais/travail/jeton-factice-autre.txt
umask 077
head -c 96 /dev/urandom | base64 -w 0 | tr -dc 'A-Za-z0-9' | cut -c1-64 > "$W/jeton-interface-factice.txt"
cat "$JD" "$JA" "$W/jeton-interface-factice.txt" > "$W/jetons-factices.txt"
umask 022
IFS= read -r HC_FACTICE_BANC < "$W/jeton-interface-factice.txt"; export HC_FACTICE_BANC
# guetteur de ps (les trois jetons factices) pendant tout le banc
bash "$B/guetteur-ps.sh" "$W/jetons-factices.txt" "$W/ps-jetons.txt" "$W/guetteur-arret" &
PG=$!
# données saines (fabricant v8) et altérées
git init -q --bare "$W/distant-vide.git"
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$W/distant-vide.git
bash "$B/fabricant-avec-jeton.sh" "$JD" "$FAB" "$W/donnees/sain" > "$W/sorties/fabrication-sain.txt" 2>&1
bash "$B/fabricant-avec-jeton.sh" "$JA" "$FAB" "$W/donnees/sain-autre" > "$W/sorties/fabrication-sain-autre.txt" 2>&1
unset FABRICANT_BANC FABRICANT_DEPOT_DISTANT
S=$W/donnees/sain
sed '5s/Amorce, essai 3/Amorce, essai 4/' "$S" > "$W/donnees/amorce-un-octet"
sed -e '$ s/^\(.\{200\}\)A/\1B/' -e 't' -e '$ s/^\(.\{200\}\)./\1A/' "$S" > "$W/donnees/charge-alteree"
sed "4a $(sed -n 4p "$S")" "$S" > "$W/donnees/deux-e-script"
sed '4a E_SCRIPT+=0' "$S" > "$W/donnees/e-script-plus"
{ head -n -1 "$S"; printf '%s' "$(tail -n 1 "$S")"; head -c 1200 /dev/zero | tr '\0' 'A'; echo; } > "$W/donnees/trop-grand"
sed '5s/Amorce/Amorcé/' "$S" > "$W/donnees/non-ascii"
chmod 600 "$W"/donnees/*
{
  echo "données saines : $(sed -n 's/^code du fabricant : //p' "$W/sorties/fabrication-sain.txt") (code du fabricant v8) ; $(grep 'lecture stricte' "$S.empreintes.txt" | cut -c1-140)"
  for a in amorce-un-octet charge-alteree deux-e-script e-script-plus non-ascii; do
    echo "artefact $a : octets différents du sain : $(cmp -l "$S" "$W/donnees/$a" 2>/dev/null | wc -l) ; taille $(wc -c < "$W/donnees/$a") (sain $(wc -c < "$S"))"
  done
  echo "artefact trop-grand : $(wc -c < "$W/donnees/trop-grand") octets (1 200 signes de base64 ajoutés à la charge)"
  echo "corps attendu (voie indépendante, sain) : $($PY -I "$B/corps-attendu.py" "$S")"
} >> "$T"
outil() {  # nom, attendu, puis arguments de l'outil (les variables du banc sont posées par l'appelant)
  local nom=$1 att=$2; shift 2
  env -u HCLOUD_TOKEN "$@" > "$W/sorties/$nom.txt" 2>&1
  local c=$?
  echo "$nom : attendu $att ; rendu $c ; $([ "$c" = "$att" ] && echo TENU || echo ÉCHEC) ; $(grep -m1 -E 'REFUS|refus|ÉCHEC|corps de création|serveur :' "$W/sorties/$nom.txt" | cut -c1-190)" >> "$T"
}
# --- à blanc (sans banc, mode par défaut)
outil C1-sain-a-blanc 0 $PY -I "$OUT" "$S" "$W/releves/C1"
for a in amorce-un-octet:12 charge-alteree:14 deux-e-script:11 e-script-plus:11 trop-grand:13 non-ascii:10; do
  outil "C2-${a%%:*}" "${a##*:}" $PY -I "$OUT" "$W/donnees/${a%%:*}" "$W/releves/C2-${a%%:*}"
done
# --- serveur factice
$PY -I "$B/serveur-hetzner-factice.py" "$W/serveur-journal.txt" "$W/serveur-pret.txt" "$W/serveur-arret" &
PS_=$!
for i in $(seq 1 100); do [ -s "$W/serveur-pret.txt" ] && break; sleep 0.1; done
PORT=$(cat "$W/serveur-pret.txt"); U=http://127.0.0.1:$PORT/v1/servers
: > "$W/serveur-journal.txt"
# --- adresses et options hors banc : refusées, rien n'arrive au serveur
outil C3-adresse-hors-banc 2 $PY -I "$OUT" "$S" "$W/releves/C3" --envoyer --adresse "$U"
outil C4-nom-jeton-hors-banc 2 $PY -I "$OUT" "$S" "$W/releves/C4" --envoyer --nom-jeton HC_FACTICE_BANC
outil C5-adresse-autre-au-banc 2 CONTROLE_BANC=oui $PY -I "$OUT" "$S" "$W/releves/C5" --envoyer --adresse https://api.example.invalid/v1/servers --nom-jeton HC_FACTICE_BANC
outil C6-hcloud-token-au-banc 2 CONTROLE_BANC=oui $PY -I "$OUT" "$S" "$W/releves/C6" --envoyer --adresse "$U" --nom-jeton HCLOUD_TOKEN
echo "requêtes reçues par le serveur après C3 à C6 (attendu 0) : $(grep -c . "$W/serveur-journal.txt")" >> "$T"
# --- envoi sain au banc
outil C7-sain-envoi-banc 0 CONTROLE_BANC=oui $PY -I "$OUT" "$S" "$W/releves/C7" --envoyer --adresse "$U" --nom-jeton HC_FACTICE_BANC
{
  echo "C7 : serveur : $(tail -n 1 "$W/serveur-journal.txt" | cut -c1-200)"
  e=$(sed -n 's/^corps de création : .* sha256 \([0-9a-f]*\) .*/\1/p' "$W/releves/C1")
  r=$(tail -n 1 "$W/serveur-journal.txt" | sed -n 's/.*corps [0-9]* octets, sha256 \([0-9a-f]*\) ;.*/\1/p')
  a=$($PY -I "$B/corps-attendu.py" "$S" | sed -n 's/.*sha256 //p')
  echo "C7 : corps reçu $r ; calculé par l'outil (C1) $e ; attendu par la voie indépendante $a ; $([ "$r" = "$e" ] && [ "$r" = "$a" ] && echo ÉGAUX || echo DIFFÉRENTS)"
  j=$(tail -n 1 "$W/serveur-journal.txt" | sed -n 's/.*jeton sha256 \([0-9a-f]*\) ;.*/\1/p')
  echo "C7 : jeton reçu par le serveur = jeton factice de l'interface : $([ "$j" = "$(printf '%s' "$HC_FACTICE_BANC" | sha256sum | cut -c1-64)" ] && echo oui || echo NON)"
  echo "C7 : relevé : root_password présent : $(grep -c -e '"root_password"' -e MOT-DE-PASSE-FACTICE "$W/releves/C7") ; user_data présent : $(grep -c -e '"user_data"' -e ECHO-USER-DATA "$W/releves/C7")"
} >> "$T"
# --- fichier changé sur disque après la lecture
cp "$S" "$W/donnees/change" && chmod 600 "$W/donnees/change"
( env -u HCLOUD_TOKEN CONTROLE_BANC=oui $PY -I "$OUT" "$W/donnees/change" "$W/releves/C8" --envoyer --adresse "$U" \
    --nom-jeton HC_FACTICE_BANC --pause-apres-lecture "$W/pause" > "$W/sorties/C8-change-apres-lecture.txt" 2>&1
  echo $? > "$W/pause/code" ) &
PC=$!
for i in $(seq 1 200); do [ -e "$W/pause/lu" ] && break; sleep 0.05; done
cp "$W/donnees/sain-autre" "$W/donnees/change.neuf" && mv -f "$W/donnees/change.neuf" "$W/donnees/change"
: > "$W/pause/continuer"
wait $PC
{
  c8=$(cat "$W/pause/code")
  r=$(tail -n 1 "$W/serveur-journal.txt" | sed -n 's/.*corps [0-9]* octets, sha256 \([0-9a-f]*\) ;.*/\1/p')
  o=$($PY -I "$B/corps-attendu.py" "$S" | sed -n 's/.*sha256 //p')
  n=$($PY -I "$B/corps-attendu.py" "$W/donnees/change" | sed -n 's/.*sha256 //p')
  echo "C8-change-apres-lecture : code $c8 ; fichier sur disque à l'envoi = données « autre » : $(cmp -s "$W/donnees/change" "$W/donnees/sain-autre" && echo oui || echo NON) ; corps reçu $r ; corps des octets lus $o ; corps des octets nouveaux $n ; $([ "$c8" = 0 ] && [ "$r" = "$o" ] && [ "$r" != "$n" ] && echo "TENU (les octets lus sont envoyés, non les nouveaux)" || echo ÉCHEC)"
  echo "C8 : empreinte des données lues écrite au relevé = sain : $(grep -c -F "$(sha256sum < "$S" | cut -c1-64)" "$W/releves/C8")"
  echo "requêtes reçues par le serveur au total (attendu 2 : C7 et C8) : $(grep -c . "$W/serveur-journal.txt")"
} >> "$T"
: > "$W/serveur-arret"; wait $PS_
: > "$W/guetteur-arret"; wait $PG
{
  echo "--- fichiers portant un jeton factice (hors données, jetons du banc et relevé de ps) :"
  grep -r -l -F -f "$W/jetons-factices.txt" "$D" | grep -v -E "^$W/(donnees/|jeton-interface-factice.txt|jetons-factices.txt|ps-jetons.txt)"; echo "(fin de liste)"
  echo "--- sorties de l'outil portant un jeton factice : $(cat "$W"/sorties/C*.txt | grep -c -F -f "$W/jetons-factices.txt")"
  echo "--- ps : $(tail -n 1 "$W/ps-jetons.txt")"
} >> "$T"
rm -rf "$W/distant-vide.git"
cat "$T"
