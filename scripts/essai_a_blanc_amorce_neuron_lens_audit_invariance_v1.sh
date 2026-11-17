#!/usr/bin/env bash
# Essai à blanc (sans location) de l'amorce de l'ESSAI D'INVARIANCE AU LOT de « Neuron Lens » — v1 = essai à blanc B-α v11 adapté :
# dépôt réduit v10, amorce `amorce_neuron_lens_audit_invariance_v1.sh`, quatre étapes (faux lanceur comparé à
# `audit_invariance_lot_v1.ETAPES`) ; reprise tuée pendant `audit-invariance` ; échec simulé à `audit-invariance` ; formes injectées à
# `preparer` ; le cas « environnement exact de B0 » est retiré (pas de B0 dans cet essai). Essai à blanc B-α v11 (v10 sur le dépôt réduit v8, amorce v7, lanceur v5 ; et la
# garde de carte CARTE_ATTENDUE essayée (R5 ; contre-lecture de la commande v6, B2) : interprète et nvidia-smi factices ; cas sain
# « NVIDIA A100-SXM4-40GB » (code 0) ; artefacts A100-SXM4-80GB, A100-PCIE-40GB, RTX 4090 vus par nvidia-smi (code 11 avant pip) ;
# nom vu par torch différent (code 11) ; nom illisible par torch (code 11) ; nvidia-smi absent : contrôle par torch seul (code 0)).
# v10 (v9 + compte des résultats d'étape poussés porté de 13 à 18 :
# la v9 l'avait gardé de la v8, seul écart de son jeu du 2026-11-17, défaut de l'essai). v9 (v8 sur le dépôt réduit v7, amorce v6, lanceur v4 : le faux lanceur
# joue aussi la seconde série au lot 64 (bascule-lot64, measure-lot64, score-lot64, grandeurs-lot64, verdicts-lot64 ; 18 appels) ; la reprise
# rejoue la seconde série ; environnement exact v3 : appels de `measure` aux lots 16 et 64 et vraie bascule ; artefact : lanceur v3 pris
# en défaut ; GO-2026-11-17-04). v8 (v7 + compte des appels de `measure` ancré sur la commande :
# en v7 il comptait aussi les lignes d'artefact « … --ctx-batch 16 absent »). v7 : v6 sur le dépôt réduit v6, amorce v5, lanceur v3 ; et les
# appels de `measure` contrôlés par programme : `--ctx-batch 16` aux graines 0 et 1 ; artefact : lanceur v2 pris en défaut ; R-2901).
# v6 : v5 + environnement EXACT des essais de B0, par
# `scripts/essai_environnement_b0_v1.py` : vrai `preparer`, vrai `etape_b0` avec un enregistreur, variables, chemins et empreintes de
# chaque essai contrôlés, lanceur v1 pris en défaut ; demande de la mère après la première course). v5 : v4 sur le dépôt réduit v5, amorce v4 ; contrôle des
# processus restants rétabli sur sa propre ligne : en v4 il était derrière un `#`, vérification courte, mineur 4). v4 : v3 + groupe tué compté sans ses zombies, jusqu'à 10 s :
# la v3 comptait encore, 1 s après `kill -9`, les processus morts non relevés). v3 : v2 + arrêt brutal de la reprise réellement fait et vérifié :
# en v2, le `&` portait sur toute la liste `cd && setsid …`, `$!` n'était pas le groupe et rien n'était tué). v2 : v1 jouée sur le dépôt réduit v4, amorce v3 ; la v1 a
# trouvé le défaut de l'amorce v2 : `env … lanceur`). v1 : pièce 6 du § 6 du devis B-α v2 : voie de sortie du brut,
# entrée idempotente et reprise, sept formes de GH_TOKEN et de HF_TOKEN, M5 et M6).
# Dépôt distant remplacé par un dépôt nu local ; même clone que l'entrée de l'instance (`--depth 1 --single-branch`, jeton factice en
# en-tête) ; mode jouet ; le lanceur est remplacé par un faux (`COMMANDE_LANCEUR`) qui joue les étapes du vrai dans le même ordre,
# consigne pour chaque appel la PRÉSENCE (jamais la valeur) de HF_TOKEN, HUGGING_FACE_HUB_TOKEN, GH_TOKEN et la valeur de
# HF_HUB_OFFLINE, et écrit un résultat par étape. Deux jetons factices (GH_TOKEN, HF_TOKEN) d'au moins 30 caractères.
# Cas et codes attendus : nominal (essais réels de nos modules, toutes les étapes, clé aux deux seules étapes « jeton », hors-ligne aux
# étapes « hors-ligne », état final écrit, 0) ; relance après l'état final (attente sans calcul, aucun appel du lanceur, 0) ; reprise
# (machine « tuée » pendant `passe`, puis relancée avec la clé de nouveau dans l'environnement : étapes faites non rejouées, `passe`
# rejouée, clé absente de tous les appels d'après, 0) ; étape en échec (20) ; quatorze cas « forme » (chacune des sept formes de chacun
# des deux jetons écrite par la course dans un journal : poussée refusée par le balayage, 15, et la forme absente du dépôt distant) ;
# mauvais commit (10) ; arbre non propre (10) ; RUN_ID invalide (17) ; COMMANDE_LANCEUR hors du mode jouet (13) ; pip minuté (16) ;
# première poussée impossible (14) ; essai en échec (12) ; essai sauté (12). Balayage final des deux jetons sur le dépôt distant (objets
# décompressés), les journaux et les disques des cas sans forme injectée ; témoins positifs exigés.
# Non couverts (déclarés) : vraie course, vrai pip complet, carte réelle, clone HTTPS réel, signaux autres que l'arrêt brutal.
# Usage : bash scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v1.sh <COMMIT_SOURCE> <dossier neuf> [<script du dépôt réduit>]
set -uo pipefail
SRC=$(cd "$(dirname "$0")/.." && pwd)
C=$(git -C "$SRC" rev-parse "$1") || exit 2; S=$2
REDUIT=${3:-scripts/depot_reduit_neuron_lens_b_alpha_v10.py}
[ -e "$S" ] && { echo "dossier existant"; exit 2; }
mkdir -p "$S"
ECARTS_F="$S/ecarts.txt"; : > "$ECARTS_F"
ecart() { echo "$*" >> "$ECARTS_F"; echo "  ÉCART : $*" >&2; }
VENV="$SRC/.venv"
"$VENV/bin/python" "$SRC/$REDUIT" "$C" "$S/r" > "$S/rapport-reduit.txt" || exit 3
champ() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))[sys.argv[2]])" "$S/r/rapport.json" "$1"; }
CR=$(champ commit_reduit)
AMORCE=scripts/amorce_neuron_lens_audit_invariance_v1.sh
BR=course/neuron-lens-b-alpha-reduit-essai
git init -q --bare "$S/distant.git" || exit 3
git -C "$S/r/depot" push -q "$S/distant.git" "course:refs/heads/$BR" || exit 3
export GH_TOKEN=ghp_facticeABCDEF0123456789abcdefXYZ
export HF_TOKEN=hf_facticeZYXWVU9876543210zyxwvuABC
unset HUGGING_FACE_HUB_TOKEN
# faux lanceur : mêmes étapes, même ordre, même environnement demandé que le vrai (b_alpha_lancer_v5)
cat > "$S/faux-lanceur.sh" <<'EOF'
#!/usr/bin/env bash
set -u
ETAPES="preparer telecharger-tokeniseur telecharger-poids audit-invariance"
JETON=" telecharger-tokeniseur telecharger-poids "; EN_LIGNE=" telecharger-tokeniseur telecharger-poids corpus audit-tout-negatif "
D="diag/$RUN_ID"
case "$1" in
  suite)
    for e in $ETAPES; do
      if [ ! -e "$D/b-alpha-$e.json" ]; then
        c=sans-jeton; [[ "$JETON" == *" $e "* ]] && c=jeton; r=hors-ligne; [[ "$EN_LIGNE" == *" $e "* ]] && r=en-ligne
        echo "$e $c $r"; exit 0
      fi
    done
    echo fin ;;
  jouer)
    e=$3
    printf '%s HF_TOKEN=%s HUGGING=%s GH=%s OFFLINE=%s GO=%s\n' "$e" "${HF_TOKEN:+present}" "${HUGGING_FACE_HUB_TOKEN:+present}" \
      "${GH_TOKEN:+present}" "${HF_HUB_OFFLINE:-}" "${GO_ID:-}" >> "$APPELS"
    mkdir -p "$D/journaux" "runs/$RUN_ID"
    [ "$e" = "${FAUX_ECHEC_ETAPE:-}" ] && { echo '{"arret": 1}' > "$D/arret-$e-1.json"; exit 1; }
    [ "$e" = "${FAUX_FORME_ETAPE:-}" ] && printf 'journal %s fin\n' "$FAUX_FORME" > "$D/journaux/$e.log"
    [ "$e" = "${FAUX_SOMMEIL_ETAPE:-}" ] && [ ! -e "$D/deja-dormi-$e" ] && { : > "$D/deja-dormi-$e"; sleep 60; }
    printf '{"etape": "%s"}\n' "$e" > "$D/b-alpha-$e.json"
    sleep 0.2 ;;
esac
EOF
chmod 755 "$S/faux-lanceur.sh"
# v9 : les étapes du faux lanceur sont celles du vrai lanceur du dépôt réduit, audits R4 exceptés (sautés quand non requis)
VRAIES=$(cd "$S/r/depot" && PYTHONPATH=src "$VENV/bin/python" -c 'from controle_ia.neuron_lens import audit_invariance_lot_v1 as b; print(" ".join(b.ETAPES))')
FAUSSES=$(grep -m1 '^ETAPES=' "$S/faux-lanceur.sh" | cut -d'"' -f2)
[ "$VRAIES" = "$FAUSSES" ] && echo "  faux lanceur : étapes égales à celles du module d'audit (audits exceptés)" || ecart "faux lanceur : étapes $FAUSSES ≠ $VRAIES"
printf 'import pytest\n@pytest.mark.skip\ndef test_x():\n    pass\n' > "$S/saute_test.py"
REELS="tests/test_neuron_lens_audit_invariance_lot_v1.py tests/test_neuron_lens_b_alpha_lancer_v5.py tests/test_neuron_lens_balayage_arbre_v1.py"
G=tests/test_neuron_lens_balayage_arbre_v1.py
cloner() {  # dossier machine ; url
  git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)" \
    clone -q --depth 1 --single-branch --branch "$BR" "file://$S/distant.git" "$1/depot" || ecart "clone de $1 impossible"
}
lancer() {  # nom dossier attendu essais [variables…] ; joue l'amorce dans le dossier machine
  local nom=$1 d=$2 attendu=$3 essais=$4; shift 4
  (cd "$d" && env COMMIT_REDUIT="$CR" GO_ID=GO-2026-11-14-06 MODE_JOUET=1 VENV_JOUET="$VENV" PERIODE_POUSSE_S=2 \
     RUN_ID="20261120-100000-neuron-lens-b-alpha" BRANCHE_RESULTATS="calcul/essai-$nom" ESSAIS="$essais" \
     COMMANDE_LANCEUR="bash $S/faux-lanceur.sh \"\$@\"" APPELS="$S/appels-$nom.txt" ESSAIS_POUSSEE_FINALE=2 ATTENTE_POUSSEE_FINALE_S=1 \
     ATTENTE_FIN=0 HF_HOME="$d/hf" "$@" timeout 900 bash "depot/$AMORCE" >> "$S/journal-$nom.txt" 2>&1 < /dev/null)
  local code=$?
  echo "CAS $nom : code=$code (attendu $attendu) ; derniere ligne : $(tail -1 "$S/journal-$nom.txt" | cut -d' ' -f3- | cut -c1-160)"
  [ "$code" = "$attendu" ] || ecart "cas $nom : code $code au lieu de $attendu"
}
cas() { local nom=$1; mkdir -p "$S/m-$nom"; cloner "$S/m-$nom"; lancer "$nom" "$S/m-$nom" "${@:2}"; }
verifier_appels() {  # nom : clé aux seules étapes « jeton », hors-ligne aux étapes « hors-ligne », GH_TOKEN jamais
  local f="$S/appels-$1.txt" l e
  [ -s "$f" ] || { ecart "$1 : aucun appel du lanceur consigné"; return; }
  while read -r l; do
    e=${l%% *}
    case " telecharger-tokeniseur telecharger-poids " in
      *" $e "*) [[ "$l" == *"HF_TOKEN=present"* ]] || ecart "$1 : $e sans HF_TOKEN" ;;
      *) [[ "$l" == *"HF_TOKEN= "* ]] || ecart "$1 : HF_TOKEN présent à $e" ;;
    esac
    case " telecharger-tokeniseur telecharger-poids corpus " in
      *" $e "*) [[ "$l" == *"OFFLINE= "* ]] || ecart "$1 : HF_HUB_OFFLINE posé à $e" ;;
      *) [[ "$l" == *"OFFLINE=1 "* ]] || ecart "$1 : HF_HUB_OFFLINE absent à $e" ;;
    esac
    [[ "$l" == *"GH= "* && "$l" == *"HUGGING= "* && "$l" == *"GO=GO-2026-11-14-06"* ]] || ecart "$1 : GH_TOKEN, HUGGING_FACE_HUB_TOKEN ou GO_ID inattendu à $e"
  done < "$f"
}
echo "ESSAI A BLANC audit invariance v1 de $AMORCE ; commit source $C ; commit reduit $CR ; liste $(champ liste_sha256) ; paquet $(champ paquet_sha256) ; $(champ n_fichiers) fichiers ; $(date -u +%FT%TZ)"

# 1. nominal, puis relance après l'état final
cas nominal 0 "$REELS"
verifier_appels nominal
n=$(wc -l < "$S/appels-nominal.txt"); echo "  nominal : $n appels du lanceur (attendu 4)"; [ "$n" -eq 4 ] || ecart "nominal : $n appels"
grep -q "HF_TOKEN retire de la course (verifie par son nom)" "$S/journal-nominal.txt" && echo "  nominal : clé retirée après telecharger-poids" || ecart "nominal : retrait de la clé non journalisé"
grep -q "passed" "$S/journal-nominal.txt" && echo "  nominal : essais réels : $(grep -E '[0-9]+ passed' "$S/journal-nominal.txt" | tail -1)" || ecart "nominal : essais réels absents"
[ -s "$S/m-nominal/fin-b-alpha.txt" ] && echo "  nominal : état final écrit : $(cat "$S/m-nominal/fin-b-alpha.txt")" || ecart "nominal : état final absent"
ET=$(git -C "$S/distant.git" show calcul/essai-nominal:etat-neuron-lens-b-alpha.txt 2>/dev/null)
echo "  nominal : état poussé : $(printf '%s' "$ET" | grep -E '^(etat|etapes_faites|location_s)=' | tr '\n' ' ')"
printf '%s' "$ET" | grep -q '^etapes_faites=.*verdicts' || ecart "nominal : étapes faites absentes de l'état poussé"
nb=$(git -C "$S/distant.git" ls-tree -r --name-only calcul/essai-nominal | grep -c '^diag/20261120-100000-neuron-lens-b-alpha/b-alpha-')
echo "  nominal : résultats d'étape sur la branche : $nb (attendu 4)"; [ "$nb" -eq 4 ] || ecart "nominal : $nb résultats poussés"
: > "$S/appels-nominal-relance.txt"
lancer nominal-relance "$S/m-nominal" 0 "$REELS" APPELS="$S/appels-nominal-relance.txt"
grep -q "etat final deja atteint" "$S/journal-nominal-relance.txt" && echo "  relance : attente sans calcul" || ecart "relance : état final non relu"
[ -s "$S/appels-nominal-relance.txt" ] && ecart "relance : le lanceur a été appelé" || echo "  relance : aucun appel du lanceur"

# 2. reprise : machine tuée pendant `passe`, relancée avec la clé de nouveau dans l'environnement
mkdir -p "$S/m-reprise"; cloner "$S/m-reprise"
(cd "$S/m-reprise" || exit 1
 setsid env COMMIT_REDUIT="$CR" GO_ID=GO-2026-11-14-06 MODE_JOUET=1 VENV_JOUET="$VENV" PERIODE_POUSSE_S=2 \
   RUN_ID="20261120-100000-neuron-lens-b-alpha" BRANCHE_RESULTATS="calcul/essai-reprise" ESSAIS="$G" \
   COMMANDE_LANCEUR="bash $S/faux-lanceur.sh \"\$@\"" APPELS="$S/appels-reprise.txt" FAUX_SOMMEIL_ETAPE=audit-invariance ATTENTE_FIN=0 \
   HF_HOME="$S/m-reprise/hf" bash "depot/$AMORCE" > "$S/journal-reprise.txt" 2>&1 < /dev/null &
 echo $! > "$S/pid-reprise")  # `&` sur la seule commande `setsid` (non chef de groupe : pas de fourche) : $! est le groupe à tuer
for _ in $(seq 1 120); do grep -q "etape : audit-invariance" "$S/journal-reprise.txt" 2>/dev/null && break; sleep 1; done
PG=$(cat "$S/pid-reprise"); sleep 1
kill -9 -- -"$PG" || ecart "reprise : groupe $PG introuvable (machine non tuée)"; sleep 1
vivants() { ps -eo pgid=,stat= | awk -v g="$PG" '$1 == g && $2 !~ /^Z/' | wc -l; }  # zombies exclus (morts, pas encore relevés)
for _ in $(seq 1 10); do [ "$(vivants)" -eq 0 ] && break; sleep 1; done
[ "$(vivants)" -eq 0 ] || ecart "reprise : groupe $PG encore vivant ($(vivants) processus)"
grep -q "etape : audit-invariance" "$S/journal-reprise.txt" && echo "  reprise : machine tuée pendant audit-invariance (groupe $PG)" || ecart "reprise : audit-invariance jamais atteinte"
grep -q "course terminee" "$S/journal-reprise.txt" && ecart "reprise : la première amorce a fini malgré l'arrêt"
n1=$(wc -l < "$S/appels-reprise.txt")
lancer reprise "$S/m-reprise" 0 "$G" APPELS="$S/appels-reprise.txt"
verifier_appels reprise
grep -q "reprise : course" "$S/journal-reprise.txt" && echo "  reprise : reprise journalisée" || ecart "reprise : reprise non journalisée"
apres=$(tail -n +"$((n1 + 1))" "$S/appels-reprise.txt" | cut -d' ' -f1 | tr '\n' ' ')
echo "  reprise : appels après la relance : $apres"
[ "$apres" = "audit-invariance " ] || ecart "reprise : étapes rejouées inattendues : $apres"
n=$(grep -c "^audit-invariance " "$S/appels-reprise.txt"); [ "$n" -eq 2 ] || ecart "reprise : audit-invariance jouée $n fois (attendu 2)"
grep -c "essais passes" "$S/journal-reprise.txt" | grep -qx 1 && echo "  reprise : essais non refaits" || ecart "reprise : essais refaits"

# 3. étape en échec ; formes de secret écrites par la course (poussée refusée, forme absente du dépôt distant)
cas echec 20 "$G" FAUX_ECHEC_ETAPE=audit-invariance
grep -q "etape audit-invariance en echec" "$S/journal-echec.txt" || ecart "échec : non journalisé"
git -C "$S/distant.git" show calcul/essai-echec:etat-neuron-lens-b-alpha.txt 2>/dev/null | grep -q '^etat=arret code 20' && echo "  échec : état poussé « arret code 20 »" || ecart "échec : état final non poussé"
FORMES_ESSAI="$S/formes-injectees.txt"
"$VENV/bin/python" - "$GH_TOKEN" "$HF_TOKEN" > "$FORMES_ESSAI" <<'EOF'
import base64, sys
from urllib.parse import quote
for nom, v in (("gh", sys.argv[1]), ("hf", sys.argv[2])):
    h = "x-access-token:" + v
    f = {"brute": v, "adresse": quote(v, safe="") + "%2F", "b64": base64.b64encode(v.encode()).decode(),
         "b64-decale": base64.b64encode(b"ab" + v.encode() + b"cd").decode(), "b64-url": base64.urlsafe_b64encode(b"z" + v.encode()).decode(),
         "entete": base64.b64encode(h.encode()).decode(), "entete-decale": base64.b64encode(b"Basic " + h.encode()).decode()}
    for k, x in f.items():
        print(f"{nom}-{k} {x}")
EOF
while read -r nomf forme; do
  cas "forme-$nomf" 15 "$G" FAUX_FORME_ETAPE=preparer FAUX_FORME="$forme" > /dev/null
  t=$(tail -1 "$S/journal-forme-$nomf.txt" | cut -d' ' -f3- | cut -c1-80)
  r=$(grep -c "balayage : poussee refusee" "$S/journal-forme-$nomf.txt")
  o=$(git -C "$S/distant.git" cat-file --batch-all-objects --batch 2>/dev/null | grep -caF -- "$forme")
  echo "CAS forme $nomf : refus du balayage $r fois ; forme dans les objets du dépôt distant : $o (attendu 0) ; $t"
  [ "$r" -ge 1 ] && [ "$o" -eq 0 ] || ecart "forme $nomf : refus $r, objets $o"
  grep -qF -- "$forme" "$S/journal-forme-$nomf.txt" && ecart "forme $nomf : écrite dans le journal de l'amorce"
done < "$FORMES_ESSAI"

# 4. gardes d'entrée
cas commit 10 "$G" COMMIT_REDUIT=0000000000000000000000000000000000000000
mkdir -p "$S/m-arbre"; cloner "$S/m-arbre"; echo x > "$S/m-arbre/depot/non-suivi.txt"; lancer arbre "$S/m-arbre" 10 "$G"
cas runid 17 "$G" RUN_ID=20261120-neuron-lens
cas commande 13 "$G" MODE_JOUET=0
cas pip 16 "$G" MODE_JOUET=0 COMMANDE_LANCEUR= TIMEOUT_PIP_S=1
grep -q "environnement non installe" "$S/journal-pip.txt" || ecart "pip : message absent"
mkdir -p "$S/m-poussee"; cloner "$S/m-poussee"; git -C "$S/m-poussee/depot" remote set-url origin "file://$S/inexistant.git"
lancer poussee "$S/m-poussee" 14 "$G"
cas essai 12 "$G tests/inexistant.py"
cas saute 12 "$G $S/saute_test.py"

# 4 bis. (retiré : pas d'étape B0 dans l'essai d'invariance)

# 4 ter. garde de carte (v11) : interprète factice (les appels à torch rendent la carte de FAUSSE_CARTE_TORCH ; le reste passe au vrai
# interprète) et nvidia-smi factice (FAUSSE_CARTE_SMI)
mkdir -p "$S/venv-carte/bin" "$S/outils"
cat > "$S/venv-carte/bin/python" <<EOF2
#!/usr/bin/env bash
if [ "\${1:-}" = "-c" ] && [[ "\${2:-}" == *torch* ]]; then
  if [[ "\$2" == *is_available* ]]; then exit 0; fi
  if [ "\${FAUSSE_CARTE_TORCH:-}" = ILLISIBLE ]; then echo "erreur" >&2; exit 1; fi
  echo "\${FAUSSE_CARTE_TORCH:-NVIDIA A100-SXM4-40GB}"; exit 0
fi
exec "$VENV/bin/python" "\$@"
EOF2
chmod 755 "$S/venv-carte/bin/python"
printf '#!/usr/bin/env bash\necho "$FAUSSE_CARTE_SMI"\n' > "$S/outils/faux-smi"; chmod 755 "$S/outils/faux-smi"
CARTE_VARS=(VENV_JOUET="$S/venv-carte" EXIGER_CARTE_JOUET=1 CARTE_ATTENDUE=A100-SXM4-40GB OUTIL_NVIDIA_SMI="$S/outils/faux-smi")
cas carte-saine 0 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="NVIDIA A100-SXM4-40GB"
grep -q "carte (nvidia-smi) : NVIDIA A100-SXM4-40GB" "$S/journal-carte-saine.txt" && grep -q "carte : NVIDIA A100-SXM4-40GB" "$S/journal-carte-saine.txt" \
  && echo "  carte saine : vue par nvidia-smi et par torch" || ecart "carte saine : non journalisée deux fois"
for art in "NVIDIA A100-SXM4-80GB" "NVIDIA A100-PCIE-40GB" "NVIDIA GeForce RTX 4090"; do
  nom=carte-smi-$(printf '%s' "$art" | tr -c 'A-Za-z0-9' '-')
  cas "$nom" 11 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="$art"
  grep -q "carte inattendue : $art" "$S/journal-$nom.txt" || ecart "$nom : carte inattendue non journalisée"
  grep -q "installation de l'environnement\|essais passes" "$S/journal-$nom.txt" && ecart "$nom : la course a continué après la carte"
done
cas carte-torch-autre 11 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="NVIDIA A100-SXM4-40GB" FAUSSE_CARTE_TORCH="NVIDIA A100-SXM4-80GB"
grep -q "carte inattendue : NVIDIA A100-SXM4-80GB" "$S/journal-carte-torch-autre.txt" || ecart "carte vue par torch : non prise en défaut"
cas carte-illisible 11 "$G" "${CARTE_VARS[@]}" FAUSSE_CARTE_SMI="NVIDIA A100-SXM4-40GB" FAUSSE_CARTE_TORCH=ILLISIBLE
grep -q "nom de la carte illisible" "$S/journal-carte-illisible.txt" || ecart "carte illisible : non prise en défaut"
cas carte-sans-smi 0 "$G" "${CARTE_VARS[@]}" OUTIL_NVIDIA_SMI="$S/outils/inexistant"
grep -q "nvidia-smi absent" "$S/journal-carte-sans-smi.txt" || ecart "nvidia-smi absent : non journalisé"

# 5. balayage final des deux jetons : formes du suivi v6 ; témoins positifs ; dépôt distant (objets), journaux, disques sans forme injectée
FORMES="$S/formes-suivi.txt"
"$VENV/bin/python" -c 'import sys; sys.path.insert(0, sys.argv[1]); from controle_ia.neuron_lens.suivi_vast_v6 import formes
print("\n".join(sorted(set(formes(sys.argv[2])) | set(formes(sys.argv[3])))))' "$SRC/src" "$GH_TOKEN" "$HF_TOKEN" > "$FORMES" || ecart "formes non calculées"
nf=$(wc -l < "$FORMES")
mkdir -p "$S/temoins"; i=0
while IFS= read -r f; do i=$((i + 1)); printf 'temoin %s fin\n' "$f" > "$S/temoins/forme-$i.txt"; done < "$FORMES"
nt=$(grep -rlF --binary-files=text -f "$FORMES" "$S/temoins" | wc -l)
propres=("$S/distant.git" "$S"/journal-*.txt "$S"/appels-*.txt "$S/m-nominal" "$S/m-reprise" "$S/m-echec" "$S/m-commit" "$S/m-arbre" \
         "$S/m-runid" "$S/m-commande" "$S/m-pip" "$S/m-poussee" "$S/m-essai" "$S/m-saute" "$S"/m-carte-*)
nfi=$(grep -rlF --binary-files=text -f "$FORMES" "${propres[@]}" 2>/dev/null | grep -v '/m-forme-' | wc -l)
b=$(git -C "$S/distant.git" cat-file --batch-all-objects --batch-check | wc -l)
no=$(git -C "$S/distant.git" cat-file --batch-all-objects --batch 2>/dev/null | grep -caF -f "$FORMES")
echo "TEMOINS du balayage : $nt fichier(s) détecté(s) sur $nf (attendu $nf)"
[ "$nt" -eq "$nf" ] || ecart "témoins du balayage"
echo "BALAYAGE des deux jetons ($nf formes) : fichiers $nfi (attendu 0) ; objets du dépôt distant : $b lus, $no ligne(s) (attendu 0)"
[ "$nfi" -eq 0 ] && [ "$no" -eq 0 ] && [ "$b" -gt 0 ] || ecart "balayage final"
# « $S/ » : les enfants seuls (la ligne de l'essai porte « $S » nu)
ps -eo pid,args | grep -F "$S/" | grep -v grep > "$S/restes.txt"
[ -s "$S/restes.txt" ] && ecart "processus restants : $(wc -l < "$S/restes.txt")"
echo "  processus restants : $(wc -l < "$S/restes.txt") (attendu 0)"
ECARTS=$(wc -l < "$ECARTS_F")
echo "VERDICT de l'essai : $([ "$ECARTS" -eq 0 ] && echo "conforme, 0 écart" || echo "NON conforme, $ECARTS écart(s) : $(tr '\n' ';' < "$ECARTS_F")")"
