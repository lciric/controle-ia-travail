#!/usr/bin/env bash
# essai de développement (non versé) : récupération v2 sur les branches jouet de la relecture « données » (S jouet c419dbd7)
set -uo pipefail
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument
J=$W/relecture-chaine-donnees/jouet-b
X=$W/chaine-v2/travail/dev
S=$(cat "$J/S.txt"); ID=99999999
lettre=$1; nom=$2; shift 2
sed -e "s|^DISTANT=.*|DISTANT=$J/distant.git|" -e "s|^BRANCHE=calcul/p4-reel-v1\$|BRANCHE=calcul/p4-jouet-$lettre-v1|" -e "s|-p4-reel\\\$'\$|-p4-jouet\$'|" \
    -e 's|^MODE_ATTENDU=reel$|MODE_ATTENDU=jouet|' -e 's|"disponible True"|"disponible False"|' -e "s|^TEXTES_P3=[^ ]* |TEXTES_P3=donnees/synth/textes-fenetres-p3.jsonl |" \
    -e 's|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|' -e 's|^VERSIONS_EXIGEES=oui|VERSIONS_EXIGEES=non|' -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|' \
    -e "s|^git show \"\$S:\$VERSEES/verifications_p4_v1.py\" > \"\$VERIF_S\".*|cp $W/chaine-v2/verifications_p4_v1.py \"\$VERIF_S\"|" \
    "$W/chaine-v2/recuperation_p4_v1.sh" > "$X/recup-$nom.sh"
echo "lignes changées : $(diff "$W/chaine-v2/recuperation_p4_v1.sh" "$X/recup-$nom.sh" | grep -c '^>')"
mkdir -p "$X/lancement-$nom" "$X/vastai-$nom"
printf 'commit %s\ncreation %s\nsuccès : True ; identifiant %s ; message : essai\n' "$S" "$(date -u +%s)" "$ID" > "$X/lancement-$nom/lancement.txt"
env -i PATH="$W/relecture-chaine-donnees/outils/bin-vastai:/usr/bin:/bin" HOME="$X" LANG=C.UTF-8 HF_TOKEN=factice-hf-dev-0001 \
    CONTROLE_IA_GITHUB_TOKEN=factice-gh-dev-0001 GH_TOKEN=factice-gh-dev-0001 VAST_API_KEY=factice-vast-dev-0001 FAUX_VASTAI_ETAT="$X/vastai-$nom" \
    PYTHONDONTWRITEBYTECODE=1 "$@" bash "$X/recup-$nom.sh" "$S" "$ID" "$X/lancement-$nom" "$X/depot-$nom" > "$X/sortie-$nom.txt" 2>&1
echo "code $?"
cat "$X/sortie-$nom.txt" | cut -c1-300
rm -rf "$X/depot-$nom" "$X/depot-$nom.travail"
