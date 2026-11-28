#!/usr/bin/env bash
# Construction du commit d'essai C3b des bancs de la chaîne de P3 (brouillon 3), dans un dépôt jetable du bloc-notes
# p3-v1-brouillon3 (jamais poussé : aucune adresse distante). Code relu : le commit 03cb538 du dépôt de travail (arbre
# gelé de la tête identique) ; C3b = tête du dépôt de travail + candidat d'essai (candidat 1 de la session, plus les
# formes exactes des décisions 1 à 3, plus la citation des trois rapports de la relecture courte, présents à la tête : R-218), copies versées des treize scripts du brouillon 3 (épingles d'essai et ligne H des
# contrôles : seules lignes changées), journal synthétique de la répétition jouet.
set -euo pipefail
export GIT_CONFIG_COUNT=4 GIT_CONFIG_KEY_3=commit.gpgsign GIT_CONFIG_VALUE_3=false PYTHONDONTWRITEBYTECODE=1
D=/home/user/controle-ia-travail
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
BN3=$BN/p3-v1-brouillon3
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
AIDES=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/essai-b3/aides_essai_b3b.py
C1=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-candidat/P3-premier-test-i-a-v1-candidat1.md
C1_SHA=8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0
X=$BN3/essai-C3b
B3=$D/brouillons/P3-chaine-v1-brouillon3
V=docs/procedures/P3-premier-test-v1
K=03cb53804e0b98fe671b62ebf5ef2d819741e282
[ -e "$X" ] && { echo "$X existe déjà (R12)"; exit 2; }
[ "$(sha256sum "$C1" | cut -d' ' -f1)" = "$C1_SHA" ] || { echo "candidat 1 d'une autre empreinte"; exit 2; }
mkdir -p "$X"
git clone -q --no-local "$D" "$X/depot"
cd "$X/depot"
git remote remove origin
[ -z "$(git remote)" ] || { echo "adresse distante restée"; exit 2; }
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "tête du dépôt de travail : $(git rev-parse HEAD)"
git merge-base --is-ancestor "$K" HEAD || { echo "code relu $K non ancêtre de la tête"; exit 2; }
GELES=$(PYTHONPATH=src "$PY" -c "from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))")
# shellcheck disable=SC2086
git diff --quiet "$K" HEAD -- $GELES && echo "arbre gelé de la tête = code relu $K" || { echo "arbre gelé de la tête ≠ $K"; exit 2; }
CAND=brouillons/P3-premier-test-i-a-v1-candidat2.md
[ -e "$CAND" ] && { echo "$CAND existe déjà dans le dépôt de travail : arrêt"; exit 2; }
CL=prereg/contre-lectures/P3-premier-test-v1-relecture-courte
python3 -I "$AIDES" candidat "$C1" "$CAND" "$(sha256sum $CL-texte-v1.md | cut -d' ' -f1)" "$(sha256sum $CL-code-v1.md | cut -d' ' -f1)" \
    "$(sha256sum $CL-chaine-v1.md | cut -d' ' -f1)"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import problemes; p = problemes('$CAND'); print('problemes() :', p); raise SystemExit(1 if p else 0)"
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CAND" > /dev/null
SHA_C=$(sha256sum "$CAND" | cut -d' ' -f1)
echo "lignes changées du candidat 1 au candidat d'essai : $(diff "$C1" "$CAND" | grep -c '^>')"
mkdir -p "$V"
for s in verifications_p3_v1.py controles_avant_depense_p3_v1.sh lancer_p3_v1.sh sceller_p3_v1.sh surveiller_p3_v1.sh \
         controle_cinq_minutes_p3_v1.sh recuperation_p3_v1.sh repetition_jouet_p3_v1.sh repetition_finale_p3_v1.sh \
         essais_lanceur_p3_v1.sh essais_controles_p3_v1.sh essais_scellement_p3_v1.sh essais_surveillance_p3_v1.sh; do
    cp "$B3/$s" "$V/$s"
done
J=$V/repetition-jouet-p3-v1.log
SHA_K=$(sha256sum brouillons/P3-consignes-v1-candidat2.md | cut -d' ' -f1)
python3 -I "$AIDES" journal "$J" "$K" "$(basename "$CAND")" "$SHA_C" P3-consignes-v1-candidat2.md "$SHA_K" \
    "$(sha256sum "$V/recuperation_p3_v1.sh" | cut -d' ' -f1)" "$(sha256sum "$V/repetition_jouet_p3_v1.sh" | cut -d' ' -f1)"
SHA_J=$(sha256sum "$J" | cut -d' ' -f1)
RAPPORTS="P3-premier-test-v1-relecture-texte-code-v1.md=$(sha256sum prereg/contre-lectures/P3-premier-test-v1-relecture-texte-code-v1.md | cut -d' ' -f1)"
RAPPORTS="$RAPPORTS P3-premier-test-v1-relecture-chaine-v1.md=$(sha256sum prereg/contre-lectures/P3-premier-test-v1-relecture-chaine-v1.md | cut -d' ' -f1)"
for x in texte code chaine; do RAPPORTS="$RAPPORTS P3-premier-test-v1-relecture-courte-$x-v1.md=$(sha256sum $CL-$x-v1.md | cut -d' ' -f1)"; done
echo "rapports épinglés (essai) : $(echo $RAPPORTS | wc -w)"
python3 -I "$AIDES" controles "$V/controles_avant_depense_p3_v1.sh" "$SHA_C" \
    "$(sha256sum brouillons/P3-premier-test-config-v1-candidat3.json | cut -d' ' -f1)" "$SHA_K" "$RAPPORTS" "$K" "$SHA_J" "$BN/p3-v1" "$BN3"
bash -n "$V/controles_avant_depense_p3_v1.sh"
for s in verifications_p3_v1.py controles_avant_depense_p3_v1.sh lancer_p3_v1.sh sceller_p3_v1.sh recuperation_p3_v1.sh repetition_jouet_p3_v1.sh; do
    echo "lignes changées dans la copie versée de $s (essai) : $(diff "$B3/$s" "$V/$s" | grep -c '^>')"
done
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$V"/*.sh "$V"/*.py "$J" > /dev/null
git add -A "$CAND" "$CAND.sha256" "$V"
git commit -qm "essai C3b : préalables (candidat d'essai, copies versées des treize scripts du brouillon 3 aux épingles d'essai, journal synthétique de la répétition jouet)"
C=$(git rev-parse HEAD); echo "C3b = $C"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1
# shellcheck disable=SC2086
git diff --quiet "$K" "$C" -- $GELES && echo "arbre gelé de C3b = code relu" || { echo "arbre gelé de C3b ≠ code relu"; exit 2; }
python3 -I "$V/verifications_p3_v1.py" repetition "$K" "$J" "$(basename "$CAND")" "$SHA_C" P3-consignes-v1-candidat2.md "$SHA_K"
python3 -I "$V/verifications_p3_v1.py" go "$CAND" registres/go.md registres/decisions.md
[ -z "$(git status --porcelain)" ] && echo "arbre propre" || git status --short | head
printf 'K=%s\nC=%s\nSHA_C=%s\nSHA_J=%s\n' "$K" "$C" "$SHA_C" "$SHA_J" > "$X/essai-C3b.txt"
