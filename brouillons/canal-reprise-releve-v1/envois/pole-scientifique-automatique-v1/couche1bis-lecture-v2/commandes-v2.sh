# Couche 1 bis, lecture v2 avec e2 (288 épisodes) — commandes lancées à 23:57:55 UTC (session-depot n° 97 : e2 versés, commit 13f3047d)
# même construction que la lecture v1 (banque v3, témoins plantés forces 2 à 0,25, mécanique, 1 génération, 5 témoins par génération) ; plus la variante traits internes (3 couches)
RM=/home/claude/controle-ia-travail
RUN=/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/banque-complete-v2/diag/20261027-153857-t05-pilote-reel
SUP1=/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/banque-complete-v2/diag/20261027-203435-t05-complement-1-reel
SUP2=/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/banque-complete-v2/diag/20261027-220146-t05-complement-2-reel
/opt/venv-essaim-sim-v1/bin/python -I -B exemples/construire_banque_t05_v3.py $RM ../couche1bis-lecture-v2/banque-e2.json --run $RUN --notations-sup $SUP1 --notations-sup $SUP2 --planter 5 --forces 2,1.5,1,0.5,0.25
/opt/venv-essaim-sim-v1/bin/python -I -B demonstrations/demo_couche1bis_v7.py ../couche1bis-lecture-v2/banque-e2.json ../couche1bis-lecture-v2/banque-e2-temoins.json ../couche1bis-lecture-v2/course-e2 --generations 1 --population mecanique --temoins-par-generation 5
for c in 7 15 23; do
  /opt/venv-essaim-sim-v1/bin/python -I -B exemples/construire_banque_t05_v3.py $RM ../couche1bis-lecture-v2/banque-e2-c$c.json --run $RUN --notations-sup $SUP1 --notations-sup $SUP2 \
      --activations /tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/vecteurs-t05/20261012-105125-t05-pilote-reel/vecteurs-par-action.npz \
      --activations /tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/vecteurs-t05/20261027-153857-t05-pilote-reel/vecteurs-par-action.npz \
      --couche $c --planter 5 --forces 2,1.5,1,0.5,0.25
  /opt/venv-essaim-sim-v1/bin/python -I -B demonstrations/demo_couche1bis_v7.py ../couche1bis-lecture-v2/banque-e2-c$c.json ../couche1bis-lecture-v2/banque-e2-c$c-temoins.json ../couche1bis-lecture-v2/course-e2-c$c --generations 1 --population mecanique --temoins-par-generation 5
done
echo FIN
