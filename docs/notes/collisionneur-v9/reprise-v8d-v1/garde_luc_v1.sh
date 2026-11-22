#!/bin/bash
# Garde externe de la dépense sur la clé RR_ANTHROPIC_API_KEY_LUC (mot de la mère, 13:09Z) : lit le journal du dossier
# toutes les 20 s ; dès que la somme des coûts des essais d'Anthropic (modèles claude-*) dépasse SEUIL, arrête par leur
# numéro l'enchaîneur donné et sa course Python (R10), puis consigne. Limite : un envoi déjà parti n'est pas repris ; le
# dépassement réel peut aller jusqu'au pire d'un envoi (environ 7,4 USD chez Fable sous --sortie-max).
# Appel : garde_luc_v1.sh DOSSIER PID_ENCHAINEUR SEUIL
cd /home/user/controle-ia-travail
D=$1; P=$2; SEUIL=$3; R=docs/notes/collisionneur-v9/reprise-v8d-v1/garde-luc-v1.log
echo "$(date -u +%FT%TZ) garde de $D, enchaîneur $P, seuil $SEUIL USD sur Luc" >> $R
while kill -0 "$P" 2>/dev/null; do
  S=$(python3 - "$D" <<'PY'
import json, sys
t = 0.0
try:
    for l in open(sys.argv[1] + "/journal.jsonl"):
        e = json.loads(l)
        if "essai" in e and str(e.get("modele_demande") or e.get("id") or "").startswith("claude-"):
            t += e.get("cout_usd", 0.0)
except FileNotFoundError:
    pass
print(round(t, 4))
PY
)
  if python3 -c "import sys; sys.exit(0 if float('$S') > float('$SEUIL') else 1)"; then
    C=$(pgrep -P "$P" -f collisionneur_v9 | head -1)
    echo "$(date -u +%FT%TZ) dépense sur Luc $S USD > $SEUIL : arrêt de l'enchaîneur $P et de la course $C" >> $R
    kill "$P" 2>/dev/null; [ -n "$C" ] && kill "$C"
    exit 0
  fi
  sleep 20
done
echo "$(date -u +%FT%TZ) enchaîneur $P fini ; dépense sur Luc $S USD, sous le seuil" >> $R
