# Lecture des traits internes (décision (a) de Lazar, 27 octobre 23:10 Paris ; N-056 point 3) — commandes lancées à 23:02:52 UTC
# trois couches, toutes rapportées ; même construction que la couche 1 bis (banque v3 sans e2, 192 épisodes), plus les traits internes.
for c in 7 15 23; do
  /opt/venv-essaim-sim-v1/bin/python -I -B exemples/construire_banque_t05_v3.py /home/claude/controle-ia-travail ../traits-internes-lecture-v1/banque-c$c.json \
      --run /tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/banque-complete-v1/diag/20261027-153857-t05-pilote-reel \
      --activations /tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/vecteurs-t05/20261012-105125-t05-pilote-reel/vecteurs-par-action.npz \
      --activations /tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/vecteurs-t05/20261027-153857-t05-pilote-reel/vecteurs-par-action.npz \
      --couche $c --planter 5 --forces 2,1.5,1,0.5,0.25
  /opt/venv-essaim-sim-v1/bin/python -I -B demonstrations/demo_couche1bis_v7.py ../traits-internes-lecture-v1/banque-c$c.json ../traits-internes-lecture-v1/banque-c$c-temoins.json ../traits-internes-lecture-v1/course-c$c \
      --generations 1 --population mecanique --temoins-par-generation 5
done
