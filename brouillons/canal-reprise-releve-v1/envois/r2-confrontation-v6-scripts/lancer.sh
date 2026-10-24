#!/bin/bash
# Exécute une commande dans un espace de noms de montage privé : /srv/r3 <- dossier de travail (chemin court,
# traversable), /var/tmp <- travail/vartmp, git masqué. Aucun écriture hors du dossier de travail.
set -e
T=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-confrontation-v6/travail
exec unshare --mount --net --propagation private /bin/bash -c "
  mount --bind $T /srv &&
  mount --bind $T/vartmp /var/tmp &&
  if [ -e /usr/bin/git ]; then mount --bind /dev/null /usr/bin/git; fi &&
  cd /srv/copie/essaim-m3-refonte-v1 &&
  exec env -i PATH=/usr/bin:/bin HOME=/srv/home TMPDIR=/srv/tmp PYTHONDONTWRITEBYTECODE=1 $*"
