#!/usr/bin/env bash
# Construction du commit d'essai C des bancs de la chaîne de P3 (brouillon 2), dans un dépôt jetable du bloc-notes
# p3-v1-brouillon2 (jamais poussé : aucune adresse distante). K = code relu d'essai (HEAD du dépôt de travail + fichier
# de tests des gardes + scripts de l'instance corrigés pour l'essai : 300 et 360 minutes, données nouvelles poussées) ;
# C = K + candidat d'essai, copies versées des treize scripts (épingles des contrôles, ligne H, borne d'essai du lanceur),
# journal synthétique de la répétition jouet.
set -euo pipefail
export GIT_CONFIG_COUNT=4 GIT_CONFIG_KEY_3=commit.gpgsign GIT_CONFIG_VALUE_3=false PYTHONDONTWRITEBYTECODE=1
D=/home/user/controle-ia-travail
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
BN2=$BN/p3-v1-brouillon2
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
AIDES=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/essai-C/aides_essai_c.py
X=$BN2/essai-C
B2=$D/brouillons/P3-chaine-v1-brouillon2
V=docs/procedures/P3-premier-test-v1
TEL=0.05; TEL_TEXTE=0,05
[ -e "$X" ] && { echo "$X existe déjà (R12)"; exit 2; }
mkdir -p "$X"
git clone -q --no-local "$D" "$X/depot"
cd "$X/depot"
git remote remove origin
[ -z "$(git remote)" ] || { echo "adresse distante restée"; exit 2; }
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
echo "base (HEAD du dépôt de travail) : $(git rev-parse HEAD)"
# K : code relu d'essai
cp "$D/tests/test_premier_test_ia_gardes_v1.py" tests/
python3 -I "$AIDES" instance scripts/p3_instance.sh scripts/amorce_instance_p3.sh
bash -n scripts/p3_instance.sh && bash -n scripts/amorce_instance_p3.sh
git add -A tests scripts
git commit -qm "essai K : tests des gardes (TC-11) ; scripts de l'instance alignés sur le brouillon 4 pour l'essai (300 et 360 minutes, données nouvelles poussées)"
K=$(git rev-parse HEAD); echo "K = $K"
N=$(PYTHONPATH=src "$PY" -m pytest --collect-only -q -p no:cacheprovider 2>/dev/null | tail -1 | sed -n 's/^\([0-9]*\) tests collected.*/\1/p')
[[ "$N" =~ ^[0-9]+$ ]] || { echo "nombre de tests illisible"; exit 2; }
echo "tests collectés à K : $N"
find . -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
SHA_A=$(sha256sum scripts/amorce_instance_p3.sh | cut -d' ' -f1); SHA_I=$(sha256sum scripts/p3_instance.sh | cut -d' ' -f1)
# C : candidat d'essai, copies versées, journal synthétique
CAND=brouillons/P3-premier-test-i-a-v1-candidat1.md
[ -e "$CAND" ] && { echo "$CAND existe déjà dans le dépôt de travail : arrêt"; exit 2; }
python3 -I "$AIDES" candidat brouillons/P3-premier-test-i-a-v1-brouillon4.md "$CAND" "$K" "$SHA_A" "$SHA_I" "$N" "$TEL_TEXTE"
PYTHONPATH=src "$PY" -c "from controle_ia.prereg import problemes; p = problemes('$CAND'); print('problemes() :', p); raise SystemExit(1 if p else 0)"
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$CAND" > /dev/null
SHA_C=$(sha256sum "$CAND" | cut -d' ' -f1)
mkdir -p "$V"
for s in verifications_p3_v1.py controles_avant_depense_p3_v1.sh lancer_p3_v1.sh sceller_p3_v1.sh surveiller_p3_v1.sh \
         controle_cinq_minutes_p3_v1.sh recuperation_p3_v1.sh repetition_jouet_p3_v1.sh repetition_finale_p3_v1.sh \
         essais_lanceur_p3_v1.sh essais_controles_p3_v1.sh essais_scellement_p3_v1.sh essais_surveillance_p3_v1.sh; do
    cp "$B2/$s" "$V/$s"
done
J=$V/repetition-jouet-p3-v1.log
python3 -I "$AIDES" journal "$J" "$K" "$(basename "$CAND")" "$SHA_C" P3-consignes-v1-candidat2.md \
    "$(sha256sum brouillons/P3-consignes-v1-candidat2.md | cut -d' ' -f1)" \
    "$(sha256sum "$V/recuperation_p3_v1.sh" | cut -d' ' -f1)" "$(sha256sum "$V/repetition_jouet_p3_v1.sh" | cut -d' ' -f1)"
SHA_J=$(sha256sum "$J" | cut -d' ' -f1)
RAPPORTS="P3-premier-test-v1-relecture-texte-code-v1.md=$(sha256sum prereg/contre-lectures/P3-premier-test-v1-relecture-texte-code-v1.md | cut -d' ' -f1)"
RAPPORTS="$RAPPORTS P3-premier-test-v1-relecture-chaine-v1.md=$(sha256sum prereg/contre-lectures/P3-premier-test-v1-relecture-chaine-v1.md | cut -d' ' -f1)"
python3 -I "$AIDES" controles "$V/controles_avant_depense_p3_v1.sh" "$SHA_C" \
    "$(sha256sum brouillons/P3-premier-test-config-v1-candidat3.json | cut -d' ' -f1)" \
    "$(sha256sum brouillons/P3-consignes-v1-candidat2.md | cut -d' ' -f1)" "$RAPPORTS" "$K" "$SHA_J" "$BN/p3-v1" "$BN2"
python3 -I "$AIDES" lanceur "$V/lancer_p3_v1.sh" "$TEL"
bash -n "$V/controles_avant_depense_p3_v1.sh" && bash -n "$V/lancer_p3_v1.sh"
for s in controles_avant_depense_p3_v1.sh lancer_p3_v1.sh; do
    echo "lignes changées dans la copie versée de $s (essai) : $(diff "$B2/$s" "$V/$s" | grep -c '^>')"
done
PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$V"/*.sh "$V"/*.py "$J" > /dev/null
git add -A "$CAND" "$CAND.sha256" "$V"
git commit -qm "essai C : préalables (candidat d'essai, copies versées des treize scripts aux épingles d'essai, journal synthétique de la répétition jouet)"
C=$(git rev-parse HEAD); echo "C = $C"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . | tail -1
git diff --quiet "$K" "$C" -- $(PYTHONPATH=src "$PY" -c "from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))") \
    && echo "arbre gelé de C = K" || { echo "arbre gelé de C ≠ K"; exit 2; }
python3 -I "$V/verifications_p3_v1.py" repetition "$K" "$J" "$(basename "$CAND")" "$SHA_C" P3-consignes-v1-candidat2.md \
    "$(sha256sum brouillons/P3-consignes-v1-candidat2.md | cut -d' ' -f1)"
python3 -I "$V/verifications_p3_v1.py" go "$CAND" registres/go.md registres/decisions.md
[ -z "$(git status --porcelain)" ] && echo "arbre propre" || git status --short | head
printf 'K=%s\nC=%s\nN=%s\nSHA_C=%s\nSHA_J=%s\n' "$K" "$C" "$N" "$SHA_C" "$SHA_J" > "$X/essai-C.txt"
