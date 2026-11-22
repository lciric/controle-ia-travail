#!/bin/bash
# Enchaîneur v14 : FIN DE VOIE seulement, sur le mot de la mère (12:49Z) : les shells des voies sont arrêtés entre deux
# dossiers, et les six dossiers en file attendent la v8l ; ce script ne fait que finir la course en cours d'une voie
# (attente du processus, verifier, une reprise sur première coupure selon le journal de l'ancienne voie), sans rien lancer
# d'autre. Appel : enchaine_v14.sh fin VOIE PID DOSSIER QUESTION GO ESPECES PLAFOND JOURNAL_ANCIEN.
# Copie du v10 : quatre voies en parallèle (mot de Lazar, GO-2026-11-22-43 : « autant de
# dossiers que les quotas le permettent, quatre au plus » ; aucun 429 relevé dans les journaux de toutes les courses).
# Remplace les enchaîneurs v6 et v9 (shells arrêtés par leur numéro, les courses Python en cours ne sont pas touchées).
# Appel : enchaine_v10.sh VOIE [PID_DE_LA_COURSE_EN_COURS]. Règles inchangées : une coupure de flux, une reprise ; une
# seconde, arrêt du dossier ; code 7 (garde de motifs) : arrêt de ce seul dossier ; tout autre code non nul arrête la voie.
# Les 429 sont repris par le collisionneur lui-même (attentes 0, 10, 30, 90 s), jamais en boucle serrée.
cd /home/user/controle-ia-travail
V8D=docs/notes/collisionneur-v9/collisionneur_v9_v8d.py
export PYTHONPATH=src
VOIE=$2
R=docs/notes/collisionneur-v9/reprise-v8d-v1/enchaine-v14-voie$VOIE.log
L=docs/notes/collisionneur-v9/reprise-v8d-v1
Q=docs/notes/demandes-fable-api-2026-11-22-v1
C=docs/notes/collisionneur-v9/protocole-x-cinq-questions-v1
SIX="--fable --opus --argon --astra --carbon --neon"
CINQ="--fable --opus --argon --astra --carbon"
coupure() { tail -3 $1/journal-etage3.txt | grep -q "ARRÊT (code 5).*flux coupé"; }
fini() { .venv/bin/python -B - "$1" <<'PY'
import importlib.util, sys
s = importlib.util.spec_from_file_location("m", "docs/notes/collisionneur-v9/collisionneur_v9_v8d.py")
m = importlib.util.module_from_spec(s); sys.modules["m"] = m; s.loader.exec_module(m); d = sys.argv[1]; m.lire_composition(d)
sys.exit(0 if all(m.cellule_valide(d, m.id_cellule(t, l)) for t in m.ORDRE_ETAGE[3] for l in m.LETTRES) else 1)
PY
}
dossier() { # $1 dossier, $2 question, $3 réserve, $4 GO, $5 espèces, $6 plafond, $7 coupures déjà reprises
  local D=$1 QU=$2 RES=$3 GO=$4 ESP=$5 P=$6 i=$7
  mkdir -p $D
  if [ -n "$RES" ] && [ ! -f $D/en-tete-reserve-v1.md ]; then
    printf '%s\n' "$RES" > $D/en-tete-reserve-v1.md; sha256sum $D/en-tete-reserve-v1.md | sed "s#$D/##" > $D/en-tete-reserve-v1.md.sha256
  fi
  while :; do
    echo "=== course $(date -u +%FT%TZ) (voie $VOIE) ===" >> $D/journal-etage3.txt
    GO_ID=$GO .venv/bin/python -B $V8D etage3 $ESP --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 \
      --sortie $D --faits $QU --question $QU --plafond-usd $P --ligne-usd $P >> $D/journal-etage3.txt 2>&1
    local c=$?; echo "code_fin=$c" >> $D/journal-etage3.txt; echo "$(date -u +%FT%TZ) $D code=$c" >> $R
    [ $c -eq 0 ] && break
    if [ $c -eq 5 ] && coupure $D && [ $i -lt 1 ]; then i=$((i+1)); echo "$D coupure, reprise" >> $R; continue; fi
    if [ $c -eq 5 ] && coupure $D; then echo "$D arrêt du dossier (seconde coupure)" >> $R; return 0; fi
    if [ $c -eq 7 ]; then echo "$D arrêt du dossier (garde de motifs, code 7) ; les autres continuent" >> $R; return 0; fi
    echo "$D arrêt code $c : la voie $VOIE s'arrête" >> $R; exit 21
  done
  .venv/bin/python -B $V8D verifier $D > /dev/null 2>&1 && echo "$D verifier après : tient" >> $R || echo "$D verifier après : ÉCHEC" >> $R
}
en_cours() { # $1 PID, $2 dossier, $3 question, $4 GO, $5 espèces, $6 plafond, $7 journal de l'ancien enchaîneur
  echo "$(date -u +%FT%TZ) attend la course Python $1 ($2)" >> $R
  while kill -0 "$1" 2>/dev/null; do sleep 15; done
  if fini $2; then
    .venv/bin/python -B $V8D verifier $2 > /dev/null 2>&1 && echo "$2 fini ; verifier après : tient" >> $R || echo "$2 fini ; verifier après : ÉCHEC" >> $R
    return
  fi
  local P=0; grep -q "$2 coupure, reprise" $7 && P=1
  if tail -3 $2/journal-etage3.txt | grep -q "ARRÊT (code 7)"; then echo "$2 arrêt du dossier (garde de motifs, code 7)" >> $R
  elif coupure $2; then
    if [ $P -lt 1 ]; then echo "$2 coupure, reprise" >> $R; dossier $2 $3 "" $4 "$5" $6 1
    else echo "$2 arrêt du dossier (seconde coupure)" >> $R; fi
  else echo "$2 arrêt non reconnu : la voie $VOIE s'arrête" >> $R; exit 21; fi
}
H=$(date -u +%Y%m%d-%H%M%S)
RES="Réserve (mot de Lazar, GO-2026-11-22-33, option A) : cette question n'a pas passé le test de devinette (table devinette-questions-neutres-16-21-v2.md) ; elle est servie telle quelle, sur le choix de Lazar."
RES2="Réserve (GO-2026-11-22-37) : question orientée faiblement au test de devinette (0,55) ; servie telle quelle, comme les deux précédentes."
echo "$(date -u +%FT%TZ) voie $VOIE, début (processus $$)" >> $R
case $1 in
fin) en_cours "$3" "$4" "$5" "$6" "$7" "$8" "$9" ;;
*) echo "usage" >> $R; exit 2 ;;
esac
echo "voie $VOIE, fin $(date -u +%FT%TZ)" >> $R
