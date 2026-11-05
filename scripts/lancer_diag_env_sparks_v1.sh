#!/usr/bin/env bash
# Lanceur du tir de DIAGNOSTIC D'ENVIRONNEMENT SPARKS, v1 — hors du code scellé. Modes `offres`, `apres-creation`,
# `apres-commande`, `inventaire`, `boucle`, `journal-amorce`, `destruction` : ceux du lanceur v12, délégués tels quels
# (`scripts/lancer_sparks_exp7_nul_v12.sh`, mêmes fichiers d'état). Mode `recherche` : celui du lanceur v12, restreint à la
# **même sorte de carte que la session 1** (`gpu_name=RTX_3090`, R-1592 ; `SPARKS_DIAG_CARTE` pour une autre, lettres,
# chiffres et soulignés seuls). Mode `tir` : comme le lanceur v12 (offre retenue par son
# rang, prix tirés de l'offre, GO contrôlé, commande littérale imprimée pour la garde de calcul), mais :
#   - l'amorce est `scripts/amorce_diag_env_sparks_v1.sh` au commit du diagnostic (`CODE`, branche `prep/sparks-diag-env-v1`),
#     contrôlé hors du code scellé par `scripts/diag_env_sparks_v1.py liste` (seuls les fichiers du diagnostic s'ajoutent) ;
#   - l'instance clone le **commit de lancement** `COMMIT` (0d163bdc… par défaut) ; aucun commit de tir n'est créé ;
#   - échéance de la minuterie **40 minutes** (`diag_env_sparks_v1.py go` : GO « SPARKS » et « tir », plafond ≤ 5 USD, devis) ;
#   - image identique à l'expérience, disque 20 Go ; `GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN` ; aucun jeton Hugging Face.
# Usage :
#   bash scripts/lancer_diag_env_sparks_v1.sh recherche ; … offres <FICHIER_BRUT>
#   bash scripts/lancer_diag_env_sparks_v1.sh tir <CODE_DIAG> <GO_ID> [RANG] [COMMIT_LANCEMENT]
#   bash scripts/lancer_diag_env_sparks_v1.sh <autre mode du lanceur v12> …
set -euo pipefail
ICI="$(cd "$(dirname "$0")/.." && pwd)"
V12="$ICI/scripts/lancer_sparks_exp7_nul_v12.sh"
DIAG="$ICI/scripts/diag_env_sparks_v1.py"
LECT="$ICI/src/controle_ia/sparks_exp7_nul_v12/vast_lecture.py"
QUOI="${1:?recherche, offres, tir, ou un mode du lanceur v12}"
if [ "$QUOI" != tir ] && [ "$QUOI" != recherche ]; then exec bash "$V12" "$@"; fi
ETAT_DIR="${SPARKS_ETAT_DIR:-$HOME/.sparks-exp7-nul-v5}"
MARQUEUR="$ETAT_DIR/.creation-incertaine"
prefixe_env() {   # env -i … avec la clé de Vast et les variables du mandataire présentes, par leur nom seulement (lanceur v12)
    local p='env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8' v
    for v in VAST_API_KEY HTTPS_PROXY HTTP_PROXY NO_PROXY SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
        [ -n "${!v:-}" ] && p="$p $v=\"\$$v\""
    done
    printf '%s' "$p"
}
court() { case "${1:-}" in *[!0-9a-f]*|'') echo "commit illisible" >&2; exit 2;; esac; [ "${#1}" = 40 ] || { echo "commit de 40 caractères" >&2; exit 2; }; printf '%s' "${1:0:12}"; }
inventaire_cmd() { echo "timeout -k 10 120 $(prefixe_env) vastai show instances --raw > \"$ETAT_DIR/inventaire-$1.json\" 2> \"$ETAT_DIR/inventaire-$1.json.err\"; bash scripts/lancer_sparks_exp7_nul_v12.sh inventaire \"$ETAT_DIR/inventaire-$1.json\" $1 $2"; }
cd "$ICI"
if [ "$QUOI" = recherche ]; then   # même sorte de carte que la session 1 (instance 59288960 : RTX 3090, pilote 610.57.04, R-1592)
    CARTE="${SPARKS_DIAG_CARTE:-RTX_3090}"
    case "$CARTE" in *[!A-Za-z0-9_]*|'') echo "carte illisible (lettres, chiffres, soulignés seuls) : $CARTE" >&2; exit 2;; esac
    mkdir -p "$ETAT_DIR"
    echo "Recherche d'offres du diagnostic, même sorte de carte que la session 1 (gpu_name=$CARTE ; RTX 3090 par défaut ; lecture seule ; sortie brute effacée après filtrage) :"
    echo "timeout -k 10 120 $(prefixe_env) vastai search offers 'num_gpus=1 gpu_name=$CARTE rentable=true verified=true' -o dph_total --raw > \"$ETAT_DIR/offres-brutes.json\" 2> \"$ETAT_DIR/offres-brutes.json.err\"; bash scripts/lancer_sparks_exp7_nul_v12.sh offres \"$ETAT_DIR/offres-brutes.json\""
    exit 0
fi
CODE="${2:?commit du diagnostic}"; GOT="${3:?GO_ID du tir}"; RANG="${4:-1}"; LANCE="${5:-0d163bdcea563a9e001f336c33f36ee6d41c800a}"
COURT=$(court "$CODE"); court "$LANCE" >/dev/null
case "$RANG" in [1-4]) ;; *) echo "rang de l'offre : 1 à 4" >&2; exit 2;; esac
[ -e "$MARQUEUR" ] && { echo "création incertaine antérieure ($MARQUEUR) : inventaire d'abord" >&2; exit 2; }
[ -s "$ETAT_DIR/offres-retenues.json" ] || { echo "aucune offre retenue : bash scripts/lancer_diag_env_sparks_v1.sh recherche, d'abord" >&2; exit 2; }
LO=$(timeout 60 python3 -I -B "$LECT" offre "$ETAT_DIR/offres-retenues.json" "$RANG") || { echo "pas d'offre au rang $RANG : nouvelle recherche" >&2; exit 2; }
OFFRE=$(printf '%s' "$LO" | sed -n 's/^OFFRE=\([0-9]*\) .*/\1/p'); PRIX=$(printf '%s' "$LO" | sed -n 's/.* PRIX_CARTE=\([0-9.e-]*\) .*/\1/p')
STOCK=$(printf '%s' "$LO" | sed -n 's/.* PRIX_STOCKAGE=\([0-9.e-]*\)$/\1/p')
[ -n "$OFFRE" ] && [ -n "$PRIX" ] && [ -n "$STOCK" ] || { echo "offre retenue mal lue" >&2; exit 2; }
timeout 120 python3 -I -B "$DIAG" liste . "$CODE"
git cat-file -e "$LANCE^{commit}" 2>/dev/null || { echo "commit de lancement $LANCE inconnu ici : git fetch d'abord" >&2; exit 2; }
REG=$(realpath "${SPARKS_REGISTRE_GO:-registres/go.md}")
L=$(timeout 120 python3 -I -B "$DIAG" go "$REG" "$GOT" "$PRIX" "$STOCK" ${SPARKS_DATE_TIR:+"$SPARKS_DATE_TIR"})
ECH=$(printf '%s' "$L" | sed -n 's/^ECHEANCE_UTC_S=\([0-9]*\) .*/\1/p'); echo "DIAGNOSTIC CONFORME : offre $OFFRE (rang $RANG), PRIX_CARTE $PRIX, PRIX_STOCKAGE $STOCK ; $L"
F="$ETAT_DIR/diag-creation-$COURT-$(date -u +%Y%m%dT%H%M%S).txt"
cat <<FIN
Tir de diagnostic d'environnement SPARKS v1, à jouer pas à pas par la session ; aucun modèle, aucune donnée, aucun jeton Hugging Face.
Offre $OFFRE (rang $RANG) ; commit du diagnostic $COURT (amorce prise par git show) ; commit de lancement cloné par l'instance : $LANCE.
1. Création (échéance de la minuterie dans 40 min ; étiquette de diagnostic ; disque de 20 Go ; jeton de l'instance : CONTROLE_IA_GITHUB_TOKEN) :
GO_ID=$GOT timeout -k 10 300 $(prefixe_env) vastai create instance $OFFRE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 20 --label sparks-diag-env-v1-$COURT \\
  --env "-e COMMIT=$LANCE -e ECHEANCE_UTC_S=$ECH -e AMORCE_ATTENTE_REFUS_S=300 -e GH_TOKEN=\$CONTROLE_IA_GITHUB_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(git show "$CODE:scripts/amorce_diag_env_sparks_v1.sh")" > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v12.sh apres-creation "$F" \$?
   ID=<identifiant rendu> ; sur « OFFRE RETIRÉE » : bash scripts/lancer_diag_env_sparks_v1.sh tir $CODE $GOT $((RANG + 1)) $LANCE (au plus 4 offres).
2. À T+5 min, puis toutes les 5 min : journal de l'amorce (lignes « AMORCE V » seules, sans ancre ; attendus : 1 démarrage) :
   timeout -k 10 120 $(prefixe_env) vastai logs \$ID --tail 400 > "$ETAT_DIR/diag-logs.txt" 2>&1; bash scripts/lancer_sparks_exp7_nul_v12.sh journal-amorce "$ETAT_DIR/diag-logs.txt" 1 \$ID
   Attendus, dans l'ordre : « AMORCE V10 DEMARRAGE 1 », « tir de diagnostic d'environnement v1 », « outils », « séquence du script
   d'instance v12 », « essais : code N : <dernière ligne de pytest> », « poussée vérifiée sur essai/sparks-diag-env-v1-\$ID »,
   « destruction demandée (fin du diagnostic …) » ; DEMARRAGES=1, BOUCLE=non. « refus avant l'ordre consommé » : cause au journal, NŒUD.
3. À T+30 min au plus (installation ≈ 5 min, essais ≈ 5 à 10 min) : inventaire attendu « absente » (destruction par la machine) :
   $(inventaire_cmd '$ID' absente)
   Instance encore là après T+40 min + 10 min : bash scripts/lancer_sparks_exp7_nul_v12.sh destruction \$ID (puis l'inventaire qu'il imprime).
4. Relevés (branche poussée par l'instance ; **lecture par la mère** ; aucune valeur de clé : garde des secrets de l'amorce) :
   git fetch origin refs/heads/essai/sparks-diag-env-v1-\$ID:refs/remotes/origin/essai/sparks-diag-env-v1-\$ID
   git show origin/essai/sparks-diag-env-v1-\$ID --stat ; fichiers sous diag-env/ : tests.txt (pytest --tb=long -rA, complet),
   tests-code.txt, pip.txt, pip-freeze.txt, python-version.txt, nvidia-smi.txt, torch.txt, env-sans-secrets.txt, systeme.txt,
   systeme-paquets.txt, amorce-journal.txt (journal complet de l'amorce, tee), minuterie.log, demarrages.txt.
Devis : $(printf '%s' "$L" | sed -n 's/.*DEVIS_USD=\([0-9.]*\).*/\1/p') USD au plus (40 min + relance + marge), sous $GOT.
FIN
