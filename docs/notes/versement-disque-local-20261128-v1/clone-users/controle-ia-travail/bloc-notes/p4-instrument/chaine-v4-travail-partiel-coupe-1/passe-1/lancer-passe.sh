#!/usr/bin/env bash
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
cd /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4-travail/passe-1
for b in arret surveillance traces; do ( bash /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4/essais_${b}_p4_v1.sh /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4-travail/passe-1/$b > banc-$b.log 2>&1; echo $? > banc-$b.code ) & done
for b in verifications lanceur controles scellement; do ( bash /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4/essais_${b}_p4_v1.sh /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4-travail/c-essai-1/depot 32034270d56f8c355121789483fa75c65ceb28f1 /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4-travail/passe-1/$b > banc-$b.log 2>&1; echo $? > banc-$b.code ) & done
wait
date -u +%FT%TZ > fin.txt
