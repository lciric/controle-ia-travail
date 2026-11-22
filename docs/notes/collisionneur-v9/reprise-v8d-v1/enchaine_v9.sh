#!/bin/bash
# Session des collisionneurs (nouveau compte) : voie Neon, remplace les enchaîneurs v7 et v8 (arrêtés par leur numéro,
# entre deux dossiers ; la course Python en cours n'est pas touchée). Ordre (mot de la mère, 09:15Z) : fin du dossier en
# cours (questions des concurrents, processus Python donné en argument), reprise du tirage au hasard sur la v8j avec
# l'acceptation nommée de « scripts/pipelines » (GO-2026-11-22-33), quatre dossiers restants (GO-2026-11-22-33), deux
# dossiers neufs (GO-2026-11-22-37). Plafond et ligne 50 USD par dossier. Une coupure de flux, une reprise ; une seconde,
# arrêt du dossier ; code 7 (garde de motifs) : arrêt de ce seul dossier ; tout autre code non nul arrête tout.
cd /home/user/controle-ia-travail
V8D=docs/notes/collisionneur-v9/collisionneur_v9_v8d.py
V8J=docs/notes/collisionneur-v9/collisionneur_v9_v8j.py
export PYTHONPATH=src
R=docs/notes/collisionneur-v9/reprise-v8d-v1/enchaine-v9.log
Q=docs/notes/demandes-fable-api-2026-11-22-v1
coupure() { tail -3 $1/journal-etage3.txt | grep -q "ARRÊT (code 5).*flux coupé"; }
fini() { .venv/bin/python -B - "$1" "$2" <<'PY'
import importlib.util, sys
s = importlib.util.spec_from_file_location("m", sys.argv[2]); m = importlib.util.module_from_spec(s)
sys.modules["m"] = m; s.loader.exec_module(m); d = sys.argv[1]; m.lire_composition(d)
sys.exit(0 if all(m.cellule_valide(d, m.id_cellule(t, l)) for t in m.ORDRE_ETAGE[3] for l in m.LETTRES) else 1)
PY
}
dossier() { # $1 dossier, $2 question, $3 réserve, $4 GO, $5 script, $6 coupures déjà reprises, $7… options en plus
  local D=$1 QU=$2 RES=$3 GO=$4 S=$5 i=$6; shift 6
  mkdir -p $D
  if [ -n "$RES" ] && [ ! -f $D/en-tete-reserve-v1.md ]; then
    printf '%s\n' "$RES" > $D/en-tete-reserve-v1.md; sha256sum $D/en-tete-reserve-v1.md | sed "s#$D/##" > $D/en-tete-reserve-v1.md.sha256
  fi
  while :; do
    echo "=== course $(date -u +%FT%TZ) ($(basename $S)) ===" >> $D/journal-etage3.txt
    GO_ID=$GO .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon --neon \
      --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie $D --faits $QU --question $QU \
      --plafond-usd 50 --ligne-usd 50 "$@" >> $D/journal-etage3.txt 2>&1
    local c=$?; echo "code_fin=$c" >> $D/journal-etage3.txt; echo "$(date -u +%FT%TZ) $D code=$c" >> $R
    [ $c -eq 0 ] && break
    if [ $c -eq 5 ] && coupure $D && [ $i -lt 1 ]; then i=$((i+1)); echo "$D coupure, reprise" >> $R; continue; fi
    if [ $c -eq 5 ] && coupure $D; then echo "$D arrêt du dossier (seconde coupure)" >> $R; return 0; fi
    if [ $c -eq 7 ]; then echo "$D arrêt du dossier (garde de motifs, code 7) ; les autres continuent" >> $R; return 0; fi
    echo "$D arrêt code $c : tout s'arrête" >> $R; exit 21
  done
  .venv/bin/python -B $S verifier $D > /dev/null 2>&1 && echo "$D verifier après : tient" >> $R || echo "$D verifier après : ÉCHEC" >> $R
}
EN_COURS=runs/collisionneur-protocole-x-questions-concurrents-v1-20261122-083333
echo "$(date -u +%FT%TZ) début (processus $$) ; attend la course Python $1 ($EN_COURS)" >> $R
while kill -0 "$1" 2>/dev/null; do sleep 15; done
echo "$(date -u +%FT%TZ) $EN_COURS : course Python $1 finie (code non lisible ici) ; dernières lignes : $(tail -1 $EN_COURS/journal-etage3.txt | cut -c1-200)" >> $R
if fini $EN_COURS $V8D; then
  .venv/bin/python -B $V8D verifier $EN_COURS > /dev/null 2>&1 && echo "$EN_COURS verifier après : tient" >> $R || echo "$EN_COURS verifier après : ÉCHEC" >> $R
else
  P=0; grep -q "$EN_COURS coupure, reprise" docs/notes/collisionneur-v9/reprise-v8d-v1/enchaine-v7.log && P=1
  if tail -3 $EN_COURS/journal-etage3.txt | grep -q "ARRÊT (code 7)"; then echo "$EN_COURS arrêt du dossier (garde de motifs, code 7)" >> $R
  elif tail -3 $EN_COURS/journal-etage3.txt | grep -q "ARRÊT (code 5).*flux coupé"; then
    if [ $P -lt 1 ]; then echo "$EN_COURS coupure, reprise" >> $R; dossier $EN_COURS $Q/question-neutre-questions-concurrents-servie-v1.md "" GO-2026-11-22-33 $V8D 1
    else echo "$EN_COURS arrêt du dossier (seconde coupure)" >> $R; fi
  else echo "$EN_COURS arrêt non reconnu : tout s'arrête" >> $R; exit 21; fi
fi
dossier runs/collisionneur-protocole-x-tirage-au-hasard-v1-20261122-080414 $Q/question-neutre-tirage-au-hasard-servie-v1.md "" GO-2026-11-22-33 $V8J 0 --reprise --accepter-motif "E3-T1-conception-F:chemin interne"
H=$(date -u +%Y%m%d-%H%M%S)
RES="Réserve (mot de Lazar, GO-2026-11-22-33, option A) : cette question n'a pas passé le test de devinette (table devinette-questions-neutres-16-21-v2.md) ; elle est servie telle quelle, sur le choix de Lazar."
dossier runs/collisionneur-protocole-x-billet-drapeau-v1-$H $Q/question-neutre-billet-drapeau-servie-v2.md "" GO-2026-11-22-33 $V8D 0
dossier runs/collisionneur-protocole-x-coeurs-algorithmiques-v1-$H $Q/question-neutre-coeurs-algorithmiques-servie-v2.md "" GO-2026-11-22-33 $V8D 0
dossier runs/collisionneur-protocole-x-theoreme-negatif-v1-$H $Q/question-neutre-theoreme-negatif-servie-v2.md "$RES" GO-2026-11-22-33 $V8D 0
dossier runs/collisionneur-protocole-x-etau-equipe-rouge-v1-$H $Q/question-neutre-etau-equipe-rouge-servie-v2.md "$RES" GO-2026-11-22-33 $V8D 0
RES2="Réserve (GO-2026-11-22-37) : question orientée faiblement au test de devinette (0,55) ; servie telle quelle, comme les deux précédentes."
dossier runs/collisionneur-protocole-x-lot-quarantaine-v1-$H $Q/question-neutre-lot-quarantaine-servie-v1.md "$RES2" GO-2026-11-22-37 $V8D 0
dossier runs/collisionneur-protocole-x-modes-attaque-v1-$H $Q/question-neutre-modes-attaque-servie-v1.md "" GO-2026-11-22-37 $V8D 0
echo "fin $(date -u +%FT%TZ)" >> $R
