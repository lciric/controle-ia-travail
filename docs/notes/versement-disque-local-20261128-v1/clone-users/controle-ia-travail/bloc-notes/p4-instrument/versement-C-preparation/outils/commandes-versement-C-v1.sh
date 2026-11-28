H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument
PREP=$H/versement-C-preparation; A=$PREP/arbre; R=/home/user/controle-ia-travail
H4=$H/chaine-v4                       # dossier de la chaîne v4 vérifiée (à confirmer)
K=3                                   # k du texte final (décision écrite, point 1)
SRC_VC4=…/verification-chaine-v4-P4-instrument-v1.md         # sources à fixer à leur arrivée
SRC_VCAND2=…/verification-candidat2-P4-instrument-v1.md
SRC_CAND2=…/P4-instrument-v1-candidat2.md                    # candidat 2 vérifié (pas le texte final)
SRC_TEXTE=…/P4-instrument-v1-candidat$K.md                   # texte final
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
 controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh repetition_jouet_p4_v1.sh
 repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh essais_scellement_p4_v1.sh
 essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh essais_verifications_p4_v1.sh
 outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
poser() {   # $1 source, $2 chemin dans le dépôt : copie sans écraser, sceau au nom final
    [ -e "$A/$2" ] && { echo "existe déjà : $2"; return 1; }
    mkdir -p "$A/$(dirname "$2")" && cp "$1" "$A/$2" && (cd "$A/$(dirname "$2")" && sha256sum "$(basename "$2")" > "$(basename "$2").sha256")
}

# (à jouer comme un script bash : chaque « exit 2 » arrête tout)
# 0. compléter l'arbre quand les pièces existent
for s in $CHAINE; do poser "$H4/$s" "docs/procedures/P4-instrument-v1/$s" || exit 2; done           # 0a
poser "$SRC_VC4" prereg/contre-lectures/verification-chaine-v4-P4-instrument-v1.md || exit 2         # 0b
poser "$SRC_VCAND2" prereg/contre-lectures/verification-candidat2-P4-instrument-v1.md || exit 2
poser "$SRC_CAND2" prereg/contre-lectures/P4-instrument-v1-candidat2.md || exit 2
poser "$SRC_TEXTE" "brouillons/P4-instrument-v1-candidat$K.md" || exit 2                              # 0c
poser "$PREP/pieces-a-nommer/P4-instrument-config-v1.json" "brouillons/P4-instrument-config-v1-candidat$K.json" || exit 2
cmp -s "$SRC_TEXTE" "$A/prereg/contre-lectures/P4-instrument-v1-candidat2.md" && { echo "texte final = candidat 2 versé : citation impossible (point 1)"; exit 2; }
L=$PREP/liste-chemins-C-v1.txt; [ -e "$L" ] && { echo "$L existe déjà"; exit 2; }                    # 0d
{ cat "$PREP/liste-chemins-C-prets-v1.txt"
  for s in $CHAINE; do printf 'docs/procedures/P4-instrument-v1/%s\ndocs/procedures/P4-instrument-v1/%s.sha256\n' "$s" "$s"; done
  for n in verification-chaine-v4-P4-instrument-v1.md verification-candidat2-P4-instrument-v1.md P4-instrument-v1-candidat2.md; do
      printf 'prereg/contre-lectures/%s\nprereg/contre-lectures/%s.sha256\n' "$n" "$n"; done
  for f in "brouillons/P4-instrument-v1-candidat$K.md" "brouillons/P4-instrument-config-v1-candidat$K.json"; do printf '%s\n%s.sha256\n' "$f" "$f"; done
} | sort -u > "$L"
[ "$(wc -l < "$L")" = 116 ] || { echo "liste : $(wc -l < "$L") chemins, 116 attendus"; exit 2; }

# 1. contrôles avant copie
while read -r f; do case $f in *.sha256) continue;; esac                                             # 1a sceaux de l'arbre
    (cd "$A/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || { echo "sceau KO : $f"; exit 2; }
done < "$L"
diff <(cd "$A" && find . -type f | sed 's|^\./||' | sort) "$L" || { echo "arbre ≠ liste"; exit 2; }   # 1b
python3 -B "$H4/verifications_p4_v1.py" rapports $(cd "$A/prereg/contre-lectures" && for f in *.md; do  # 1c 27 noms exacts
    printf '%s=%s ' "$f" "$(sha256sum "$f" | cut -d' ' -f1)"; done) || exit 2
cd "$R" || exit 2                                                                                     # 1d dépôt prêt
[ "$(git remote get-url origin)" = https://github.com/lciric/controle-ia-travail.git ] || [ "$(git remote get-url origin)" = https://github.com/lciric/controle-ia-travail ] || exit 2
git fetch -q origin main && [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] && [ -z "$(git status --porcelain --untracked-files=no)" ] || exit 2
while read -r f; do [ -e "$R/$f" ] && { echo "existe déjà dans le dépôt : $f"; exit 2; }; done < "$L"
[ -z "$(git ls-files prereg/contre-lectures/ | grep -E '/[^/]*P4[^/]*$')" ] || { echo "famille P4 déjà présente"; exit 2; }   # 1e

# 2. copie de l'arbre dans le dépôt (sans écraser)
while read -r f; do mkdir -p "$R/$(dirname "$f")" && cp -n "$A/$f" "$R/$f" || exit 2; done < "$L"

# 3. sceaux dans le dépôt, arbre scellé
while read -r f; do case $f in *.sha256) continue;; esac
    (cd "$R/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || { echo "sceau KO dans le dépôt : $f"; exit 2; }
done < "$L"
PYTHONPATH=src python -B -m controle_ia.scellement verifier-arbre . | tail -1 | grep -qx "arbre intact" || exit 2

# 4. git add des seuls chemins listés (donnees/ est ignoré : -f sur ces chemins seulement)
grep -v '^donnees/' "$L" | xargs git add --
grep '^donnees/' "$L" | xargs git add -f --
diff <(git diff --cached --name-only --no-renames | sort) "$L" || { echo "index ≠ liste"; exit 2; }
[ "$(git diff --cached --name-only --diff-filter=A | wc -l)" = 116 ] || { echo "un chemin n'est pas un ajout"; exit 2; }
# commit C (message de la session, attribution des consignes), puis poussée vers le dépôt de travail seulement :
# git commit -F <message> && git push origin HEAD:main
