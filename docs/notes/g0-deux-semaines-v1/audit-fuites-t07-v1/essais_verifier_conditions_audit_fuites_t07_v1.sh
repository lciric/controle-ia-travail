#!/usr/bin/env bash
# Essais (R5) du vérificateur des conditions de lancement de l'audit des fuites de T0.7 — v1.
# Un cas sain et huit artefacts, chacun sur un dépôt jouet neuf : copie des seuls fichiers lus par le vérificateur,
# objets git lus dans le dépôt réel par un fichier `.git` de renvoi (commandes git de lecture seulement :
# rev-parse, cat-file, show, merge-base, ls-remote). Aucune donnée de 7a, 7b ou T0.7 n'est lue ; les « entrées de 7b »
# des artefacts 7 et 8 sont des fichiers factices de quelques octets ; la racine des entrées de 7b des essais est un dossier
# jouet passé par --racine-7b (la vraie racine n'est jamais touchée).
# Usage : bash essais_verifier_conditions_audit_fuites_t07_v1.sh VERIFICATEUR DEPOT_REEL BAC
set -u
V=$1; D=$2; BAC=$3
[ ! -e "$BAC" ] || { echo "ARRÊT : $BAC existe déjà"; exit 2; }
mkdir -p "$BAC"
N_OK=0; N_ECHEC=0
FICHIERS="registres/scellements-v1.md registres/code-t07/CODE-T07-v3.json registres/code-t07/CODE-T07-v3.json.sha256
prereg/T0.7-consigne-audit-fuites-v1.md prereg/T0.7-consigne-audit-fuites-v1.md.sha256 prereg/T0.7-sondes-v0-v1.md
prereg/T0.7-sondes-v0-v1.md.sha256 prereg/P3-consignes-v1.md src/controle_ia/t07/criteres_v1.py
src/controle_ia/premier_test_ia/statistiques.py src/controle_ia/sondes/evaluation.py
src/controle_ia/environnements/propositions.py src/controle_ia/premier_test_ia/conditions.py
src/controle_ia/t06/test_croise.py src/controle_ia/t06/cout.py"
jouet() {   # $1 : nom ; crée un dépôt jouet sain
  J="$BAC/$1"; mkdir -p "$J"
  for f in $FICHIERS; do mkdir -p "$J/$(dirname "$f")"; cp "$D/$f" "$J/$f"; done
  printf 'gitdir: %s/.git\n' "$D" > "$J/.git"
  ln -s "$D/.venv" "$J/.venv"   # lien vers l'environnement entier (pyvenv.cfg compris)
  echo "$J"
}
essai() {   # $1 : nom ; $2 : motif attendu dans la sortie (grep -E) ; $3 : code attendu ; $4… : arguments en plus
  local nom=$1 motif=$2 code_att=$3; shift 3
  local sortie code
  sortie=$(python3 -I "$V" "$BAC/$nom" "$@" 2>&1); code=$?
  if [ "$code" = "$code_att" ] && grep -q -E "$motif" <<<"$sortie"; then echo "CONFORME  $nom (code $code ; « $motif » trouvé)"; N_OK=$((N_OK+1))
  else echo "ÉCHEC     $nom (code $code, attendu $code_att ; motif « $motif »)"; grep -E '^(KO|À FAIRE)' <<<"$sortie" | head -5; N_ECHEC=$((N_ECHEC+1)); fi
}
# 0. cas sain : aucun KO ; les quatre entrées de 7b « À FAIRE »
jouet sain >/dev/null
essai sain '^# bilan : [0-9]+ OK, 0 KO, 4 À FAIRE$' 0 --racine-7b "$BAC/racine-jouet-absente"
# 1. une ligne AUDIT-FUITES-T07 déjà inscrite → C5 KO
J=$(jouet a1-ligne-audit); printf '| AUDIT-FUITES-T07 | 2026-11-14T00:00:00Z | diag/x/audit-fuites-t07.json | %064d |\n' 0 >> "$J/registres/scellements-v1.md"
essai a1-ligne-audit '^KO +C5 ligne AUDIT-FUITES-T07 : 1 fois' 1 --racine-7b "$BAC/racine-jouet-absente"
# 2. ligne CONSIGNE-AUDIT-FUITES-T07 en double → C2 KO
J=$(jouet a2-consigne-double); L=$(grep '^| CONSIGNE-AUDIT-FUITES-T07 | ' "$J/registres/scellements-v1.md"); printf '%s\n' "$L" >> "$J/registres/scellements-v1.md"
essai a2-consigne-double '^KO +C2 ligne CONSIGNE-AUDIT-FUITES-T07 : 2 fois' 1 --racine-7b "$BAC/racine-jouet-absente"
# 3. ligne RUN-CONFIRMATION-T06 qui cite la course 7a → C3 KO (aucune ouverture : le manifeste n'existe pas dans le jouet)
J=$(jouet a3-course-7a); sed -i 's#runs/20261111-151701-t06-reel/manifeste.json#runs/20261109-070232-t06-reel/manifeste.json#' "$J/registres/scellements-v1.md"
essai a3-course-7a '^KO +C3 .*RUN_7B = 20261109-070232-t06-reel \(≠ 7a : False\)' 1 --racine-7b "$BAC/racine-jouet-absente"
# 4. marqueur restant dans la consigne (compagnon recalculé) → C1 KO (empreinte et marqueur)
J=$(jouet a4-marqueur); printf '<<CHEMIN_DECOUPEUR>>\n' >> "$J/prereg/T0.7-consigne-audit-fuites-v1.md"
(cd "$J/prereg" && sha256sum T0.7-consigne-audit-fuites-v1.md > T0.7-consigne-audit-fuites-v1.md.sha256)
essai a4-marqueur '^KO +C1 marqueurs « <<NOM>> » restants dans la consigne : 1' 1 --racine-7b "$BAC/racine-jouet-absente"
# 5. criteres_v1.py modifié d'un octet → C4 KO
J=$(jouet a5-criteres); printf '\n' >> "$J/src/controle_ia/t07/criteres_v1.py"
essai a5-criteres '^KO +C4 .*entrée « fichiers » : False' 1 --racine-7b "$BAC/racine-jouet-absente"
# 6. commit du manifeste donné en argument, absent du clone → C8 À FAIRE, C10 et C11 non conformes
J=$(jouet a6-commit-absent)
essai a6-commit-absent '^À FAIRE +C8 commit 000000000000… \(commit du manifeste \(donné en argument\)\) présent dans le clone : False' 1 --commit 0000000000000000000000000000000000000000 --racine-7b "$BAC/racine-jouet-absente"
# 7. entrée de 7b factice, dans la racine jouet, dont le compagnon ne correspond pas → C12 KO
J=$(jouet a7-entree-fausse); R6=20261111-151701-t06-reel; RJ="$BAC/racine-jouet-a7"; mkdir -p "$RJ/donnees/$R6"
printf 'factice\n' > "$RJ/donnees/$R6/mesures-t06.npz"; printf '%064d  mesures-t06.npz\n' 0 > "$RJ/donnees/$R6/mesures-t06.npz.sha256"
essai a7-entree-fausse '^KO +C12 .*/racine-jouet-a7/donnees/20261111-151701-t06-reel/mesures-t06.npz : présent ; = compagnon' 1 --racine-7b "$RJ"
# 8. entrée de 7b factice déposée dans l'arbre du dépôt (et non dans la racine hors du dépôt) → C12 bis KO
J=$(jouet a8-entree-dans-arbre); mkdir -p "$J/diag/$R6"; printf 'factice\n' > "$J/diag/$R6/episodes-t06.json"
essai a8-entree-dans-arbre "^KO +C12 bis diag/20261111-151701-t06-reel/episodes-t06.json dans l'arbre du dépôt : \\['diag/20261111-151701-t06-reel/episodes-t06.json'\\]" 1 --racine-7b "$BAC/racine-jouet-absente"
echo "# bilan des essais : $N_OK conformes, $N_ECHEC en échec (9 attendus conformes)"
[ "$N_ECHEC" = 0 ] && [ "$N_OK" = 9 ]
