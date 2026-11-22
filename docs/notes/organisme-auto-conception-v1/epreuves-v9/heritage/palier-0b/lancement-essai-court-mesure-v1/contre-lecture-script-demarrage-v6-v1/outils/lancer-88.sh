#!/bin/bash
# Quatre cas de refus 88 sur le script reel, puis un cas d'evasion a la fin. Usage : lancer-88.sh RB (prepare par preparer-distant.sh)
set -u
RB=$1
O=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v6/outils
mkdir -p $RB/shim $RB/plain-parent
cat > $RB/shim/mkdir <<'EOF'
#!/bin/bash
# cale : ne cree pas le groupe du programme (simule un groupe cree sans cgroup.kill)
for a in "$@"; do case "$a" in */ca-banc-i5-*) exit 0 ;; esac; done
exec /bin/mkdir "$@"
EOF
chmod 755 $RB/shim/mkdir
/bin/bash $O/lot-integre.sh $RB i2-sans-cgroupe ESSAI_DEMARRAGE_CGROUPE=
/bin/bash $O/lot-integre.sh $RB i3-parent-pas-cgroupe ESSAI_DEMARRAGE_CGROUPE=$RB/plain-parent/essai-3-programme
/bin/bash $O/lot-integre.sh $RB i4-non-inscriptible ESSAI_DEMARRAGE_CGROUPE=THREADED
/bin/bash $O/lot-integre.sh $RB i5-sans-kill PATH=$RB/shim:$PATH
