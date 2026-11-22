#!/usr/bin/env bash
# [T0.8 v1 (consigne de la chaîne de lancement de T0.8, `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`, § 3.4) : copie de `scripts/lancer_t06_v13.sh` sous un nom neuf
# (R12 : la v13 reste telle quelle), dont rien ne change hors ce que la consigne nomme ; chaque ligne changée porte « T08 » ou est
# déclarée dans le rapport de la chaîne. Mêmes sous-commandes, mêmes codes de sortie. Changent : (1) les noms (`t08`), la branche
# de sortie par défaut (`calcul/t08-course-v1`), la branche d'entrée (`entree/t08-course-v1`), la configuration lue sur la branche
# d'entrée (`prereg/T0.8-configuration-course-v1.json`), le commit du code (marqueur `COMMIT_CODE_T08` de la configuration, ancêtre
# de `T08_BRANCHE_CODE`), l'amorce `scripts/amorce_instance_t08_v1.sh` citée par son empreinte (`T08_AMORCE_SHA256`, celle de
# l'ordre de course, égale au compagnon au commit du code) ; (2) la ligne de GO, toujours par la variable `GO_ID`, admise par la
# configuration, lue au registre avec sa fin de validité et son plafond (`lancement_t08.session_v1 go` : prolongation comprise) ;
# plafond de la course 120 USD cumulés sur toutes les tentatives (dépense antérieure relevée au registre des dépenses), compte
# rendu à 40 USD (alerte unique de la surveillance) ; (3) les bornes de l'offre, celles de « Machine » (vue `vue-offre.json` tirée
# de la configuration) ; (4) aucune relance sur une carte H200 : la carte `relance` est refusée (code 2), ni automatique ni
# proposée ; (5) aucun couperet de temps (inchangé) ; deux heures sans ligne de progression : alerte, sans arrêt (inchangé) ;
# (6) `controles-epreuve` refuse (code 2) : aucune épreuve à blanc n'est prévue par l'ordre de course de T0.8 ;
# `--verifier-go-seulement` vérifie la ligne `GO_ID` contre la configuration (premier argument : la configuration).
# Usage T0.8 :
#   bash scripts/lancer_t08_v1.sh controles DOSSIER_NEUF [JOUR]
#       Variables : GO_ID, T08_BRANCHE_ENTREE, T08_BRANCHE_CODE, T08_AMORCE_SHA256 ; facultatives : T08_PREREG, T08_CONFIG,
#       T08_BRANCHE, T08_REGISTRE_GO, T08_DEPOT. Codes : 0 ; 2 tout échec.
#   bash scripts/lancer_t08_v1.sh creation auto course DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]
#   bash scripts/lancer_t08_v1.sh apres-creation FICHIER CODE DOSSIER
#   bash scripts/lancer_t08_v1.sh surveillance ID DOSSIER [FACTURE_USD]
#   bash scripts/lancer_t08_v1.sh --verifier-go-seulement CONFIG.json [DEPENSE_ANTERIEURE] [JOUR]
# Texte de la v13 de la course de confirmation (conservé) :]
# [v13 (contre-lecture CLE3T-01 de l'ordre E3 ter ; nom neuf, R12 : la v12 reste telle quelle) : copie du lanceur v12 SANS identifiant de GO d'épreuve en dur. La ligne de GO de l'épreuve vient de la variable d'environnement GO_ID (convention de la garde de calcul), doit égaler le go_id de la configuration, et est LUE dans le registre T06_REGISTRE_GO par le module de session v12 (`session_v12.py` : ligne présente, type calcul, accordée par Lazar, non échue au jour donné, non révoquée) ; le plafond d'une épreuve n'est plus borné à 8 USD mais au plafond de la ligne (plafond + dépense antérieure ≤ plafond de la ligne, plus de marge ni de dépense antérieure minimale propres aux deux lignes cumulées des épreuves E2, E3 et E3 bis de la v12) ; l'amorce citée est `scripts/amorce_instance_t06_v11.sh` (lanceur de run v6) ; sous-commande neuve `--verifier-go-seulement PLAFOND [DEPENSE_ANTERIEURE] [JOUR]` qui vérifie et ne crée rien. Tout échec : code 2 et ligne de fin explicite (R5). Le reste (garde d'équivalence, création, surveillance, lecture du coût) ne change pas.]
# [v12 (GO-2026-11-08-01, contre-lecture de la v11 v2) : copie du lanceur v11 qui cite l'amorce v10 (bras B v4, liste figée v2) et valide `T06_TESTS_ATTENDUS` (^[0-9]*$ : sans cela une valeur comme « 7 -e PYTEST_ADDOPTS=… » s'insérerait dans la commande de création) ; rien d'autre ne change]
# [v11 (R-1746, contre-lecture de la v11) : le module de session est session_v11.py ; les épreuves se jouent sous GO-2026-11-06-01 (E2, E3 ; total 5 USD) ou GO-2026-11-07-08 (E3 bis ; total 8 USD, dépense antérieure ≥ 2,092 USD exigée), les deux lignes vérifiées au registre ; T06_TESTS_ARGS est refusé hors du mode jouet ; plus de variable T06_GO_EPREUVES_TOTAL_USD]
# [v11 (E3 du 7 novembre) : copie du lanceur v10 qui cite l'amorce v10 (suite ciblée et figée, liste scripts/tests-cibles-t06-v1.txt) ; rien d'autre ne change]
# Chaîne de session de T0.6, v10 (nom neuf, R12 ; les v1 à v9 restent telles quelles). v10 = v9 + (contre-lecture Opus de la v9, « Essais R5 à ajouter » 3) : le module de session est `session_v9.py` (`instance_seule` : « 404 » exact et message exact ; `{"id": null}` non concluant) ; le code et le motif du refus de plafond ne changent pas (code 2). Texte de la v9 (conservé) :
# [v10, intégration de la course : cite l amorce v8 (bras B en annexe), session_v9] Chaîne de session de T0.6, v9 (nom neuf, R12 ; les v1 à v8 restent telles quelles). v9 = v8 + (R-1692, épreuve E2 du 7 novembre) : le stockage n'est plus compté deux fois (`dph_total` inclut déjà `storage_total_cost` sous `--storage` : prix_carte = dph_total − storage_total_cost, module `session_v9.py`) ; l'amorce citée est `scripts/amorce_instance_t06_v7.sh` (correctif R-1689 : l'ordre de destruction de l'amorce l'emporte sur l'arrêt par dépense épuisée). Texte de la v8 (conservé) :
# Chaîne de session de T0.6, v8 (nom neuf, R12 ; les v1 à v7 restent telles quelles). v8 = v7 + (R-1683, contre-lecture Opus de la v7) : (1) une liste d'inventaire
# VIDE (ou `null`, illisible, ou un appel en échec) n'est pas une absence : ALERTE sur la sortie standard avec un compteur, puis `vastai show instance <ID>` (l'instance
# seule) ; `ARRET mort` seulement si une liste NON vide ne contient pas l'instance à deux relevés, ou si l'instance seule est introuvable à deux relevés ; présence non
# établie trois relevés de suite : `ARRET inventaire` ; (2) `vastai logs --tail 20000` (journal entier, comme la v6) ; (3) masquage PAR UN TUBE, aucun fichier brut
# (journal, inventaire et réponse de `show instance` masqués avant d'être écrits) ; toute clé présente (HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN, GH_TOKEN, VAST_API_KEY) de moins
# de 8 caractères refuse la surveillance ; l'amorce citée est `scripts/amorce_instance_t06_v6.sh`. Texte de la v7 (conservé) : chaîne de session de T0.6, v7. v7 = v6 + (R-1677, défaut de chaîne d'E2) : (1) l'amorce citée
# est `scripts/amorce_instance_t06_v5.sh` (clonage réduit, débit journalisé, `refus` qui attend 180 s) ; (2) `surveillance` imprime `ARRET mort` quand
# l'instance n'est plus dans l'inventaire (deux relevés à 15 s d'écart) et recopie à chaque relevé le journal entier (`logs --tail 2000`, valeurs de
# clés masquées) dans `journal-instance.txt` (écrasé seulement par un journal qui porte des lignes AMORCE) ; (3) le filtre de création porte aussi
# `inet_down>=500` (module `session_v7.py`). Texte de la v6 (conservé) : chaîne de session de T0.6, v6 (nom neuf, R12 ; les v1 à v5 restent telles quelles). v6 = v5 + `reliability>=0.98` dans le filtre de la recherche
# de création (R-1660 : la création filtre exactement comme la lecture E2-1 des ordres d'épreuve), rien d'autre. Texte de la v5 :
# Chaîne de session de T0.6, v5 (contre-lecture du lanceur v4, R-1657) :
# C-V5-1 : `creation` ne relit plus l'offre par son identifiant (`search offers "id=<OFFRE>"` rend une liste VIDE sous vastai 1.8.3 et
# l'identifiant d'une même offre change d'une recherche à l'autre : R-577, R-578, confirmé en réel le 7 novembre) ; le premier argument
# est « auto » : recherche filtrée (`search offers '<filtre de la configuration>' -o dph_total --storage <disque> --raw`), première
# offre de la liste qui respecte les bornes (carte, mémoire, disque, prix de la carte, du stockage et du téléchargement), prix lus
# DANS LA LISTE, commande de création imprimée pour cet identifiant ; si la création échoue (offre retirée), `apres-creation`
# vérifie qu'aucune instance du programme n'existe, note la machine refusée et demande de relancer `creation auto …` (rang
# suivant) ; au plus trois essais, puis arrêt. C-V5-2 : `HF_TOKEN` n'est exigé par `surveillance` qu'en mode réel. C-V5-3 : le
# texte de la surveillance nomme le plafond de la configuration. L'amorce reste `scripts/amorce_instance_t06_v4.sh`. Texte de la v4
# (conservé) : chaîne de session de T0.6, v4 (nom neuf, R12 ; les v1 à v3 restent telles quelles). Contre-lecture du lanceur v3 : mêmes
# sous-commandes, mêmes arguments et mêmes codes que la v3 ; changent le nom du script (`_v4`), l'amorce citée par son empreinte
# dans le texte de S (`scripts/amorce_instance_t06_v4.sh`, C-V4-1), la branche par défaut (`calcul/t06-reel-v4`) et le lanceur joué
# (`controle_ia.t06.lanceur_v4`, C-V4-2). Texte de la v3 (conservé) : chaîne de session de T0.6, v3. Contre-lecture neuve du lanceur v2,
# C-V3-3 : l'offre est relue par `vastai search offers "id=<OFFRE>" --storage <offre.disque_min_go> --raw`, pour que `dph_total`
# et `storage_total_cost` soient lus au disque demandé (150 Go) ; amorce v4 citée ; branche par défaut `calcul/t06-reel-v4`.
# Mêmes sous-commandes et mêmes arguments que la v2. Inchangé de la v2 (contre-lecture du lanceur v1) :
# C08 (dépense cumulée sur toutes les tentatives : argument « dépense antérieure » relevée au registre des dépenses, forfait
# de téléchargement lu dans l'offre ; heure d'épuisement des 200 USD calculée à la création et passée à l'amorce),
# C09 (garde de dépense illisible : ALERTE, et arrêt imprimé après trois échecs de suite), C12 (offre relue par
# `vastai search offers "id=<OFFRE>" --raw` et vérifiée par `session_v2 offre` : carte, mémoire de carte, une seule carte,
# mémoire vive, cœurs effectifs, disque, prix de la carte, du stockage et du téléchargement ; prix jamais donnés à la main ;
# `vastai show instances --raw` sans instance du programme), C15 (prix maximal par carte lu dans la configuration, argument
# `carte` : course ou relance), L11 (fin du GO et dernier jour de création lus dans la configuration, vérifiés contre le
# registre des GO par `session_v2 calendrier` ; rien en dur). Inchangé de la v1 : SANS COUPERET DE TEMPS ; la session ne
# loue rien par ce script, il VÉRIFIE puis IMPRIME la commande littérale de création, revérifiée par la garde de calcul.
# Usage :
#   bash scripts/lancer_t06_v12.sh controles DOSSIER_NEUF [JOUR]
#       GO conforme ; commit de scellement S du préenregistrement, poussé sur origin/main ; huit citations du texte de S ;
#       configuration, tâches et consignes citées présentes et scellées à S ; configuration de S copiée dans DOSSIER ;
#       calendrier de la configuration conforme au registre (L11) ; amorce v4 de S citée par son empreinte ; place disque ;
#       jetons présents (jamais affichés) ; écrit DOSSIER/lancement.txt. Codes : 0 ; 2 tout échec.
#   bash scripts/lancer_t06_v12.sh creation auto CARTE DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]   (v5 : « auto » remplace l'identifiant d'offre)
#       CARTE = course | relance (DT-6). Après `controles` : relit S, relit l'offre et l'inventaire des instances par
#       l'outil (C12), vérifie le GO et le calendrier au jour de la création, calcule l'heure d'épuisement de la dépense
#       (C08), rejoue la garde de calcul, puis IMPRIME la commande de création. Codes : 0 ; 2 échec ; 3 nœud (offre hors des
#       bornes, instance présente, dépense déjà épuisée).
#   bash scripts/lancer_t06_v12.sh controles-epreuve DOSSIER_NEUF COMMIT CONFIG_CHEMIN [JOUR]     (C-V4-3, épreuves à blanc E2 et E3)
#       Variables : T06_BRANCHE_CODE (branche `prep/…` du code, dont COMMIT est un ancêtre au sens de `refs/remotes/origin/<branche>`,
#       relevée par un `git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>` explicite) ; GO_ID (environnement) = go_id de la
#       configuration lue DANS COMMIT, ligne de GO de calcul conforme au registre (v13 : lue, jamais en dur ; plafond de l'épreuve ≤ plafond de la ligne) ; calendrier au registre ;
#       amorce v4 de COMMIT ; place disque ; jetons ; écrit DOSSIER/lancement.txt (ligne « epreuve oui »). Aucune citation de
#       préenregistrement (une épreuve n'est jamais décisive). Codes : 0 ; 2 tout échec.
#       `creation` lit alors le GO, le plafond, le mode et la configuration dans DOSSIER ; la branche poussée doit commencer par
#       `essai/` (jamais `calcul/`) ; `T06_EPUISEMENT_SIMULE_S` (≥ 60, épreuves seulement) avance l'heure d'épuisement de la dépense
#       pour éprouver le redémarrage après une dépense épuisée ; `T06_TESTS_ATTENDUS` (vide à E3 : la dernière ligne est relevée) ;
#       `T06_TESTS_ARGS` (essais joués par l'amorce, séparés par des virgules, épreuves seulement ; jouet seulement, refusé en mode réel ; vide = la suite ciblée figée de l'amorce v10, jamais la suite complète).
#       Registre des GO : `T06_REGISTRE_GO` = `registres/go.md` d'un clone de `main` (qui fait foi), OBLIGATOIRE pour une épreuve (aux
#       contrôles et à la création) ; le registre du commit cloné doit porter aussi le GO (l'amorce le relit). Sans la variable (course),
#       le registre de l'arbre du script.
#   bash scripts/lancer_t06_v12.sh apres-creation FICHIER CODE DOSSIER
#   bash scripts/lancer_t06_v12.sh surveillance ID DOSSIER [FACTURE_USD]
#       Prix, dépense antérieure, forfait de téléchargement et heure de création relus dans DOSSIER/lancement.txt ; décision
#       par `session_v2 surveillance` : POURSUIVRE ; ALERTE ; ARRET mort ou ARRET depense : imprime `vastai stop instance
#       ID`, code 3 ; FIN : même commande, code 0 ; REFUS : code 4 ; garde illisible : ALERTE, puis ARRET au troisième échec
#       de suite (C09).
# Variables : CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2 (v13 : l'un ou l'autre nom, par présence seulement, le premier présent l'emporte ; relayé à l'amorce sous GH_TOKEN par son NOM), HF_TOKEN (présence exigée, jamais affichés) ; T06_DEPOT ; T06_PREREG ; T06_BRANCHE
# (défaut calcul/t06-reel-v4) ; T06_IMAGE ; VAST (outil) ; INTERVALLE.
set -uo pipefail
QUOI="${1:?controles, creation, apres-creation ou surveillance}"
DEPOT="${T08_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"                 # T08
P="${T08_PREREG:-prereg/T0.8-bases-boite-noire-v0-v1.md}"               # T08 : texte scellé de T0.8 (sur main)
A=scripts/amorce_instance_t08_v1.sh                                     # T08
BRANCHE="${T08_BRANCHE:-calcul/t08-course-v1}"                          # T08 : branche de sortie
BE="${T08_BRANCHE_ENTREE:-entree/t08-course-v1}"                        # T08 : branche d'entrée (liste blanche seule, orpheline)
CONFIG="${T08_CONFIG:-prereg/T0.8-configuration-course-v1.json}"        # T08 : configuration réelle de la course, lue sur la branche d'entrée
GO_ID_ENV="${GO_ID:-}"              # T08 : identifiant de la ligne de GO de la COURSE, toujours reçu de l'environnement (convention de la garde de calcul : GO_ID=GO-AAAA-MM-JJ-NN), admis par la configuration et vérifié au registre ; aucun identifiant en dur
REG="${T08_REGISTRE_GO:-$DEPOT/registres/go.md}"   # T08 : registre des GO lu par toutes les sous-commandes (celui de `main`, qui fait foi)
MOTIF_GO='^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$'
IMAGE="${T08_IMAGE:-python:3.11-bookworm}"                              # T08 : nom de la variable
VAST="${VAST:-vastai}"
SESSION="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v2; sys.exit(session_v2.main(sys.argv[1:]))"
SESSION3="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
SESSION7="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v12; sys.exit(session_v12.main(sys.argv[1:]))"
SESSION8="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.lancement_t08 import session_v1; sys.exit(session_v1.main(sys.argv[1:]))"   # T08 : GO et prolongation, calendrier, vue de l'offre, surveillance
BRANCHE_PROG="$DEPOT/scripts/construire_branche_entree_t08_v1.py"      # T08 : vérification de la branche d'entrée relevée
masquer() { python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) >= 8:
        t = t.replace(v, "***")
sys.stdout.write(t)'; }
# R-1693 : sortie de vastai masquée PAR UN TUBE, avec lecture de TOUT le PIPESTATUS. $1 = fichier de sortie ; le reste = la commande. Code rendu : celui de la
# commande ; 121 si le masquage a échoué (aucun fichier écrit, l'ancien reste) ; stderr jeté (il n'est pas masqué).
vast_masque() {
    local sortie="$1"; shift
    "$@" 2>/dev/null | masquer > "$sortie.tmp"
    local ps=("${PIPESTATUS[@]}")
    if [ "${ps[1]:-1}" != 0 ]; then rm -f "$sortie.tmp"; return 121; fi
    mv -f "$sortie.tmp" "$sortie"; return "${ps[0]}"
}
# v13 : NOM de la variable qui porte le jeton GitHub (CONTROLE_IA_GITHUB_TOKEN, sinon CONTROLE_IA_GITHUB_TOKEN_2) ; code 1 si aucune n'est présente ; la valeur n'est jamais lue ici ni affichée
jeton_gh_nom() { if [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN; elif [ -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN_2; else return 1; fi; }
commit_s() { git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256"; }
champ() { sed -n "s/^$1 //p" "$2" | tail -1; }           # dernière valeur d'un champ de lancement.txt
cle_config() { python3 -I -B -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8"))
for k in sys.argv[2].split("."):
    c = c[k]
print(c)' "$1" "$2"; }
case "$QUOI" in
controles)
    D=$(realpath -m "${2:?dossier neuf}"); JOUR="${3:-$(date -u +%F)}"
    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN : la ligne de GO de calcul de la course, convention de la garde de calcul) : pas de création"; exit 2; }   # T08
    BC="${T08_BRANCHE_CODE:?T08_BRANCHE_CODE : branche qui porte le commit du code cité par CODE-T08}"; AS="${T08_AMORCE_SHA256:?T08_AMORCE_SHA256 : empreinte de l amorce, celle de l ordre de course}"   # T08
    [[ "$AS" =~ ^[0-9a-f]{64}$ ]] || { echo "T08_AMORCE_SHA256 : 64 caractères hexadécimaux"; exit 2; }   # T08
    mkdir -p "$D"
    LIBRE=$(df -Pk "$D" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 2; }
    S=$(commit_s); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement de $P introuvable"; exit 2; }
    timeout 300 git -C "$DEPOT" fetch -q origin main || { echo "fetch impossible"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent de origin/main"; exit 2; }
    git -C "$DEPOT" show "$S:$P" > "$D/prereg-S.md" || { echo "préenregistrement absent de S"; exit 2; }
    [ "$(sha256sum < "$D/prereg-S.md" | cut -d' ' -f1)" = "$(git -C "$DEPOT" show "$S:$P.sha256" 2>/dev/null | cut -d' ' -f1)" ] || { echo "sceau de $P non conforme à S"; exit 2; }   # T08
    # T08 : branche d'entrée relevée (refspec explicite), vérifiée par programme sans la branche de 7b : liste blanche exacte, orpheline, aucun interdit, empreintes
    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/$BE:refs/remotes/origin/$BE" || { echo "branche d'entrée $BE introuvable"; exit 2; }
    EC=$(git -C "$DEPOT" rev-parse "refs/remotes/origin/$BE^{commit}") || { echo "branche d'entrée illisible"; exit 2; }
    git -C "$DEPOT" show "$EC:$CONFIG" > "$D/config.json" 2>/dev/null || { echo "configuration $CONFIG absente de la branche d'entrée"; exit 2; }
    [ "$(git -C "$DEPOT" rev-parse "$EC:$P")" = "$(git -C "$DEPOT" rev-parse "$S:$P")" ] || { echo "texte de la branche d'entrée ≠ texte scellé de S"; exit 2; }
    VB=$(python3 -I -B "$BRANCHE_PROG" verifier --depot "$DEPOT" --ref "refs/remotes/origin/$BE" --commit-texte "$S" --texte "$P" --config "$CONFIG" 2>&1) || { echo "branche d'entrée non conforme : $(printf '%s' "$VB" | tail -n 1)"; exit 2; }
    COMMIT=$(cle_config "$D/config.json" marqueurs.COMMIT_CODE_T08) && [[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT_CODE_T08 illisible dans la configuration"; exit 2; }
    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/$BC:refs/remotes/origin/$BC" || { echo "branche du code $BC introuvable"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$COMMIT" "refs/remotes/origin/$BC" 2>/dev/null || { echo "commit du code $COMMIT absent de refs/remotes/origin/$BC"; exit 2; }
    git -C "$DEPOT" show "$COMMIT:$A" > "$D/amorce.sh" || { echo "amorce absente du commit du code $COMMIT"; exit 2; }
    E=$(sha256sum "$D/amorce.sh" | cut -d' ' -f1)
    [ "$E" = "$AS" ] && [ "$E" = "$(git -C "$DEPOT" show "$COMMIT:$A.sha256" 2>/dev/null | cut -d' ' -f1)" ] || { echo "empreinte de l'amorce ($E) ≠ T08_AMORCE_SHA256 ($AS) ou son compagnon au commit du code"; exit 2; }
    GOL=$(python3 -I -B -c "$SESSION8" go "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") || { echo "GO : $GOL : pas de création"; exit 2; }   # T08
    printf '%s\n' "$GOL" | tee -a "$D/lancement.txt"
    CAL=$(python3 -I -B -c "$SESSION8" calendrier "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") || { echo "calendrier lu au registre : $CAL : pas de création"; exit 2; }   # T08
    VUE=$(python3 -I -B -c "$SESSION8" vue "$D/config.json" "$D/vue-offre.json") || { echo "bornes de l'offre : $VUE : pas de création"; exit 2; }   # T08
    PLC=$(cle_config "$D/config.json" lancement.plafond_usd) && CRU=$(cle_config "$D/config.json" lancement.compte_rendu_usd) || { echo "plafond ou compte rendu illisibles"; exit 2; }   # T08
    [ -n "${HF_TOKEN:-}" ] && JGHN=$(jeton_gh_nom) || { echo "jeton absent (HF_TOKEN, ou CONTROLE_IA_GITHUB_TOKEN / CONTROLE_IA_GITHUB_TOKEN_2) : pas de création"; exit 2; }
    printf 'controles t08 v1 %s\ncommit_texte %s\ncommit %s\nprereg %s\nconfig %s\nbranche %s\nbranche_entree %s\nentree %s\nbranche_code %s\namorce %s\ngo %s\nplafond %s\ncompte_rendu %s\nmode reel\ncalendrier %s\n' "$(date -u +%FT%TZ)" "$S" "$COMMIT" "$P" "$CONFIG" "$BRANCHE" "$BE" "$EC" "$BC" "$E" "$GO_ID_ENV" "$PLC" "$CRU" "$CAL" >> "$D/lancement.txt"   # T08
    echo "CONTRÔLES CONFORMES : texte S=$S ; code $COMMIT ; entrée $EC ; amorce t08 v1 $E ; $GOL ; $CAL" ;;
controles-epreuve)
    echo "controles-epreuve : non offerte pour T0.8 (aucune épreuve à blanc n'est prévue par l'ordre de course) : rien vérifié, rien créé"; exit 2 ;;   # T08
creation)
    OFFRE_ARG="${2:?auto}"; CARTE="${3:?carte : course}"; ANT="${4:?dépense antérieure en USD (registre des dépenses ; 0 pour la première tentative)}"; D=$(realpath -m "${5:?dossier des contrôles}"); ECH="${6:-}"
    [ "$OFFRE_ARG" = auto ] || { echo "offre : « auto » seulement (v5 : un identifiant donné à la main serait périmé, il change d'une recherche à l'autre ; l'offre est choisie dans la liste filtrée, juste avant la création)"; exit 2; }
    case "$CARTE" in course) ;; relance) echo "carte « relance » : aucune relance sur une carte H200, ni automatique ni proposée (section « Machine » du texte de T0.8 ; mot de Lazar exigé) : pas de création"; exit 2;; *) echo "carte : course (seule carte de T0.8)"; exit 2;; esac   # T08
    [[ "$ANT" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "dépense antérieure : nombre positif en USD"; exit 2; }
    [ -f "$D/lancement.txt" ] && grep -q '^commit ' "$D/lancement.txt" && [ -f "$D/config.json" ] || { echo "contrôles absents ($D/lancement.txt, config.json) : pas de création"; exit 2; }
    S=$(champ commit_texte "$D/lancement.txt"); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit du texte illisible"; exit 2; }   # T08
    COMMIT=$(champ commit "$D/lancement.txt"); [[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "commit du code illisible"; exit 2; }   # T08
    [ "$S" = "$(commit_s)" ] || { echo "commit de scellement changé depuis les contrôles"; exit 2; }
    [ "$(cle_config "$D/config.json" marqueurs.COMMIT_CODE_T08)" = "$COMMIT" ] || { echo "commit du code de la configuration ≠ celui des contrôles"; exit 2; }   # T08
    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] && [ "$GO_ID_ENV" = "$(champ go "$D/lancement.txt")" ] || { echo "GO_ID de l'environnement (${GO_ID_ENV:-absent}) ≠ GO des contrôles ($(champ go "$D/lancement.txt")) : pas de création"; exit 2; }   # T08
    PLC=$(cle_config "$D/config.json" lancement.plafond_usd) && [ "$PLC" = "$(champ plafond "$D/lancement.txt")" ] && [ "$PLC" = 120 ] || { echo "plafond de la configuration ($PLC) ≠ plafond des contrôles ou ≠ 120 USD (texte) : pas de création"; exit 2; }   # T08
    MODE_C=reel   # T08 : la course de T0.8 n'a qu'un mode sur la machine (aucune épreuve à blanc)
    [ -z "${T08_EPUISEMENT_SIMULE_S:-}" ] || { echo "T08_EPUISEMENT_SIMULE_S : aucune épreuve à blanc pour T0.8"; exit 2; }   # T08
    CAL=$(python3 -I -B -c "$SESSION8" calendrier "$REG" "$D/config.json" "$GO_ID_ENV") || { echo "calendrier lu au registre au jour de la création : $CAL : nœud, pas de création"; exit 3; }   # T08
    FIN_GO=$(printf '%s\n' "$CAL" | sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p'); [[ "$FIN_GO" =~ ^[0-9]+$ ]] || { echo "fin du GO illisible"; exit 2; }   # T08 : l'échéance de la machine est bornée plus bas par le plafond restant (M-5), jamais par la seule fin du GO
    python3 -I -B -c "$SESSION8" go "$REG" "$D/config.json" "$GO_ID_ENV" >/dev/null || { echo "GO non conforme au jour de la création"; exit 2; }   # T08
    JGHN=$(jeton_gh_nom) && { [ -n "${HF_TOKEN:-}" ] || [ "$MODE_C" = jouet ]; } || { echo "jeton absent (ni CONTROLE_IA_GITHUB_TOKEN ni CONTROLE_IA_GITHUB_TOKEN_2, ou HF_TOKEN en mode réel) : pas de création"; exit 2; }
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : offre non relue, pas de création"; exit 2; }
    DISQUE=$(cle_config "$D/vue-offre.json" offre.disque_min_go) || { echo "disque illisible"; exit 2; }   # T08 : vue de l'offre
    [[ "$DISQUE" =~ ^[0-9]+([.][0-9]+)?$ ]] && [ "${DISQUE%%.*}" -gt 0 ] || { echo "offre.disque_min_go illisible ($DISQUE) : pas de création"; exit 2; }
    # C-V5-1 : au plus trois essais (une machine refusée est exclue du suivant) ; offre choisie DANS LA LISTE FILTRÉE, prix lus dans la liste,
    # au disque demandé (--storage, C-V3-3) ; aucune relecture par identifiant
    ESSAIS=$(grep -c '^essai_creation ' "$D/lancement.txt" || true)
    [ "${ESSAIS:-0}" -lt 3 ] || { echo "trois essais de création déjà faits (essai_creation = $ESSAIS) : arrêt, aucune création ; message à la mère"; exit 3; }
    EXCL=$(sed -n 's/^machine_refusee //p' "$D/lancement.txt" | paste -sd, -)
    FILTRE=$(python3 -I -B -c "$SESSION7" filtre "$D/vue-offre.json" "$CARTE") || { echo "filtre illisible : $FILTRE"; exit 2; }   # T08 : vue de l'offre
    timeout -k 5 120 "$VAST" search offers "$FILTRE" -o dph_total --storage "$DISQUE" --raw > "$D/offres.json" 2>"$D/offres.err" || { echo "recherche filtrée impossible (--storage $DISQUE) : pas de création"; exit 2; }
    OF=$(python3 -I -B -c "$SESSION7" choisir "$D/offres.json" "$D/vue-offre.json" "$CARTE" "$EXCL") || { echo "aucune offre conforme dans la liste filtrée : $OF : nœud, pas de création"; exit 3; }   # T08 : vue de l'offre
    OFFRE=$(printf '%s\n' "$OF" | sed -n 's/^id=\([0-9]*\) .*/\1/p'); MACH=$(printf '%s\n' "$OF" | sed -n 's/.* machine=\([^ ]*\) .*/\1/p'); RANG=$(printf '%s\n' "$OF" | sed -n 's/.* rang=\([0-9]*\) .*/\1/p')
    [[ "$OFFRE" =~ ^[0-9]+$ ]] && [ -n "$MACH" ] && [ -n "$RANG" ] || { echo "offre choisie illisible ($OF)"; exit 2; }
    PC=$(printf '%s\n' "$OF" | sed -n 's/.*prix_carte=\([0-9.]*\).*/\1/p'); PS=$(printf '%s\n' "$OF" | sed -n 's/.*prix_stockage=\([0-9.]*\).*/\1/p')
    TEL=$(printf '%s\n' "$OF" | sed -n 's/.*telechargement_forfait=\([0-9.]*\).*/\1/p')
    [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] || { echo "prix illisibles dans la relecture de l'offre"; exit 2; }
    ETIQ=$(cle_config "$D/vue-offre.json" offre.etiquette) || { echo "étiquette illisible"; exit 2; }   # T08 : vue de l'offre
    vast_masque "$D/instances.json" timeout -k 5 120 "$VAST" show instances --raw || { echo "inventaire des instances impossible ou masquage en échec (code $?) : pas de création"; exit 2; }
    INV=$(python3 -I -B -c "$SESSION" instances "$D/instances.json" "$ETIQ") || { echo "$INV : nœud, pas de création"; exit 3; }
    NOW=$(date +%s)
    DEP=$(python3 -I -B -c "$SESSION3" depense "$PLC" "$PC" "$PS" "$NOW" "$ANT" "$TEL" "$NOW"); code_dep=$?   # T08 : aucune simulation d'épuisement
    [ "$code_dep" = 0 ] || { echo "dépense cumulée déjà au plafond ou illisible ($DEP) : nœud, pas de création"; exit 3; }
    EPUIS=$(printf '%s\n' "$DEP" | sed -n 's/.*epuisement_utc_s=\([0-9]*\).*/\1/p'); [[ "$EPUIS" =~ ^[0-9]+$ ]] || { echo "heure d'épuisement illisible"; exit 2; }
    # T08 (M-5) : échéance de la machine = heure du plafond restant (par défaut) ; une échéance donnée ne peut que l'avancer
    [ -n "$ECH" ] || ECH="$EPUIS"
    [[ "$ECH" =~ ^[0-9]+$ ]] && [ "$ECH" -le "$EPUIS" ] && [ "$ECH" -gt "$(date +%s)" ] || { echo "échéance $ECH hors de ]maintenant, heure du plafond restant $EPUIS]"; exit 2; }
    B64=$(base64 -w0 < "$D/amorce.sh")
    [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$(champ amorce "$D/lancement.txt")" ] || { echo "encodage de l'amorce"; exit 2; }
    CMD="GO_ID=$GO_ID_ENV timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT=$COMMIT -e PREREG=$P -e CONFIG=$(champ config "$D/lancement.txt") -e BRANCHE=$BRANCHE -e BRANCHE_ENTREE=$(champ branche_entree "$D/lancement.txt") -e ENTREE_COMMIT=$(champ entree "$D/lancement.txt") -e BRANCHE_CODE=$(champ branche_code "$D/lancement.txt") -e GO_ID_T08=$GO_ID_ENV -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e ECHEANCE_UTC_S=$ECH -e FIN_GO_UTC_S=$FIN_GO -e DEPENSE_EPUISEE_UTC_S=$EPUIS -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$$JGHN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh\" > \"$D/creation-brute.json\" 2>&1; bash $DEPOT/scripts/lancer_t08_v1.sh apres-creation \"$D/creation-brute.json\" \$? \"$D\""   # T08 : variables de la branche d'entrée et du code, GO de la course
    printf '{"tool_input":{"command":%s}}' "$(python3 -c 'import json, sys; print(json.dumps(sys.argv[1]))' "$CMD")" | python3 "$DEPOT/.claude/hooks/garde_calcul.py" || { echo "garde de calcul : commande refusée"; exit 2; }
    printf 'creation preparee %s\noffre %s\ncarte %s\nstorage %s\nprix_carte %s\nprix_stockage %s\ntelechargement_forfait %s\nanterieure %s\necheance %s\nepuisement %s\ndepense %s\nplafond_creation %s\nessai_creation %s\nmachine_proposee %s\nrang %s\n' "$(date -u +%FT%TZ)" "$OFFRE" "$CARTE" "$DISQUE" "$PC" "$PS" "$TEL" "$ANT" "$ECH" "$EPUIS" "$DEP" "$PLC" "$((ESSAIS + 1))" "$MACH" "$RANG" >> "$D/lancement.txt"
    echo "OFFRE CONFORME : $OF ; $INV ; $DEP"
    echo "COMMANDE DE CRÉATION (à exécuter par la session, jetons par leur nom seulement) :"
    echo "$CMD" ;;
apres-creation)
    F="${2:?fichier}"; C="${3:?code}"; D="${4:?dossier}"
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    NON=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(False|false)" "$F" 2>/dev/null || true)
    rm -f -- "$F"
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then
        CR=$(date +%s); printf 'instance %s\ncreation %s\n' "$ID" "$CR" >> "$D/lancement.txt"
        echo "CRÉÉE : instance $ID (création $CR ; sortie de vastai non affichée) ; surveillance : bash scripts/lancer_t08_v1.sh surveillance $ID $D"; exit 0
    fi
    if [ -z "$ID" ] && [ "${NON:-0}" -ge 1 ] && [ "${OK:-0}" -eq 0 ]; then
        # C-V5-1 : refus explicite (offre retirée) : retenter au rang suivant seulement si aucune instance du programme n'existe
        ETIQ=$(cle_config "$D/vue-offre.json" offre.etiquette) || { echo "étiquette illisible"; exit 4; }   # T08 (M-2) : vue de l'offre
        if vast_masque "$D/instances-apres.json" timeout -k 5 120 "$VAST" show instances --raw && python3 -I -B -c "$SESSION" instances "$D/instances-apres.json" "$ETIQ" >/dev/null; then
            printf 'machine_refusee %s\n' "$(champ machine_proposee "$D/lancement.txt")" >> "$D/lancement.txt"
            echo "OFFRE REFUSÉE À LA CRÉATION (retirée ?) : aucune instance du programme ; machine $(champ machine_proposee "$D/lancement.txt") exclue ; rang suivant : bash $DEPOT/scripts/lancer_t08_v1.sh creation auto $(champ carte "$D/lancement.txt") $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")"; exit 5
        fi
    fi
    echo "CRÉATION INCERTAINE (code $C, identifiant « ${ID:-aucun} ») : vérifier « vastai show instances » sans --raw ; aucune seconde création avant"; exit 4 ;;
surveillance)
    ID="${2:?identifiant}"; D="${3:?dossier}"; FACT="${4:-}"
    [[ "$ID" =~ ^[0-9]+$ ]] || { echo "identifiant : chiffres seuls (R10)"; exit 2; }
    [ -f "$D/lancement.txt" ] || { echo "dossier sans lancement.txt"; exit 2; }
    [ "$(champ instance "$D/lancement.txt")" = "$ID" ] || { echo "identifiant $ID ≠ instance créée d'après $D/lancement.txt (R10)"; exit 2; }
    CR=$(champ creation "$D/lancement.txt"); PC=$(champ prix_carte "$D/lancement.txt"); PS=$(champ prix_stockage "$D/lancement.txt")
    TEL=$(champ telechargement_forfait "$D/lancement.txt"); ANT=$(champ anterieure "$D/lancement.txt")
    PLC=$(champ plafond_creation "$D/lancement.txt"); [ "$PLC" = 120 ] || { echo "plafond de la création illisible ou ≠ 120 USD dans lancement.txt"; exit 2; }   # T08 : plafond cumulé de la course, sans valeur par défaut
    CRU=$(champ compte_rendu "$D/lancement.txt"); [[ "$CRU" =~ ^[0-9]+$ ]] || { echo "seuil du compte rendu illisible dans lancement.txt"; exit 2; }   # T08 : compte rendu à 40 USD
    [[ "$CR" =~ ^[0-9]+$ ]] && [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] && [ -n "$ANT" ] || { echo "création, prix ou dépense antérieure illisibles dans lancement.txt"; exit 2; }
    # C-V5-2 : HF_TOKEN n'est exigé (masquage) qu'en mode réel ; une épreuve en mode jouet n'en a pas besoin
    JGH="${CONTROLE_IA_GITHUB_TOKEN:-${CONTROLE_IA_GITHUB_TOKEN_2:-}}"      # R-1693 : sous `set -u`, `${#VAR}` d'une variable absente sortait en 127 au lieu de 2 ; v13 : l'un ou l'autre nom
    [ "${#JGH}" -ge 8 ] || { echo "jeton GitHub absent ou trop court : masquage impossible, surveillance refusée"; exit 2; }
    HF_L="${HF_TOKEN:-}"
    [ "$(champ mode "$D/lancement.txt")" = jouet ] || [ "${#HF_L}" -ge 8 ] || { echo "HF_TOKEN absent ou trop court (mode réel) : masquage impossible, surveillance refusée"; exit 2; }
    for K in HF_TOKEN CONTROLE_IA_GITHUB_TOKEN CONTROLE_IA_GITHUB_TOKEN_2 GH_TOKEN VAST_API_KEY; do          # R-1683 : une clé présente mais trop courte ne serait pas masquée
        V="${!K:-}"; { [ -z "$V" ] || [ "${#V}" -ge 8 ]; } || { echo "$K présente mais de moins de 8 caractères : masquage impossible, surveillance refusée"; exit 2; }
    done
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : surveillance aveugle, arrêt"; exit 2; }
    : >> "$D/progres.txt"
    INTERVALLE="${INTERVALLE:-120}"; ILLISIBLES=0; NONET=0
    alerte() { local m; m="$(date -u +%FT%TZ) $1"; echo "$m" >> "$D/surveillance.txt"; echo "$m"; }
    liste_presente() {   # LP : 0 présente, 1 absente d'une liste non vide, 3 liste vide, 2 illisible, 9 appel en échec
        timeout -k 5 120 "$VAST" show instances --raw 2>/dev/null | masquer > "$D/inventaire-tour.tmp"
        local ps=("${PIPESTATUS[@]}") st sm; st="${ps[0]}"; sm="${ps[1]:-1}"                          # R-1693 : tout le PIPESTATUS ; un échec du masquage n'est jamais lu comme une liste
        if [ "$sm" != 0 ]; then rm -f "$D/inventaire-tour.tmp"; LP=9; echo "masquage de l'inventaire en échec (code $sm) : relevé écarté, aucune copie vidée" > "$D/presence.txt"; alerte "ALERTE masquage en échec (inventaire, code $sm) : relevé écarté"; return; fi
        mv -f "$D/inventaire-tour.tmp" "$D/inventaire-tour.json"          # écriture atomique : jamais de fichier à demi écrit
        [ "$st" = 0 ] || { LP=9; : > "$D/presence.txt"; return; }
        python3 -I -B -c "$SESSION7" presente "$D/inventaire-tour.json" "$ID" > "$D/presence.txt" 2>&1; LP=$?
    }
    seule_presente() {   # SP : 0 répond, 4 introuvable, 2 illisible, 9 appel en échec sans texte d'introuvable
        timeout -k 5 120 "$VAST" show instance "$ID" --raw 2>&1 | masquer > "$D/instance-seule.tmp"
        local ps=("${PIPESTATUS[@]}") st sm; st="${ps[0]}"; sm="${ps[1]:-1}"
        if [ "$sm" != 0 ]; then rm -f "$D/instance-seule.tmp"; SP=9; echo "masquage de la réponse de show instance en échec (code $sm) : relevé écarté" > "$D/presence-seule.txt"; alerte "ALERTE masquage en échec (show instance, code $sm) : relevé écarté"; return; fi
        mv -f "$D/instance-seule.tmp" "$D/instance-seule.json"
        python3 -I -B -c "$SESSION7" seule "$D/instance-seule.json" "$ID" > "$D/presence-seule.txt" 2>&1; SP=$?
        [ "$SP" != 2 ] || [ "$st" = 0 ] || SP=9
    }
    echo "surveillance t08 v1 de $ID : création $CR, carte $PC USD/h, stockage $PS USD/h, téléchargement $TEL USD, antérieur $ANT USD ; sans couperet de temps ; arrêt sur processus mort ou dépense cumulée ≥ $PLC USD (plafond de la configuration, C-V5-3) ; alerte après 2 h sans PROGRES ; alerte unique de compte rendu à $CRU USD" >> "$D/surveillance.txt"
    while true; do
        now=$(date -u +%s)
        # R-1683 : journal entier (--tail 20000), masqué PAR UN TUBE (aucun fichier brut sur le disque), copié à chaque relevé
        timeout -k 5 120 "$VAST" logs "$ID" --tail 20000 2>&1 | masquer > "$D/journal-dernier.tmp"; PSJ=("${PIPESTATUS[@]}"); ST="${PSJ[0]}"; SMJ="${PSJ[1]:-1}"
        if [ "$SMJ" != 0 ]; then
            rm -f "$D/journal-dernier.tmp"                       # R-1693 : masquage en échec = relevé écarté, ALERTE, jamais une copie vidée ni brute
            alerte "ALERTE masquage en échec (journal, code $SMJ) : relevé écarté, dernier relevé gardé"
        elif [ "$ST" = 0 ]; then
            mv -f "$D/journal-dernier.tmp" "$D/journal-dernier.txt"
            grep -q '^AMORCE ' "$D/journal-dernier.txt" && cp -f "$D/journal-dernier.txt" "$D/journal-instance.txt"      # copie entière à chaque relevé, la dernière bonne survit à la disparition de l'instance
            grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"; done
        else
            rm -f "$D/journal-dernier.tmp"
            echo "$(date -u +%FT%TZ) journal illisible (appel en échec) : dernier relevé gardé" >> "$D/surveillance.txt"
        fi
        # R-1683 : présence. Une liste VIDE n'est pas une absence ; inventaire et réponse de `show instance` sont masqués par un tube avant d'être écrits.
        ARR=0; LP=9
        liste_presente
        if [ "$LP" = 1 ]; then sleep "${ABSENCE_ATTENTE_S:-15}"; liste_presente; [ "$LP" = 1 ] && ARR=1; fi
        if [ "$ARR" = 0 ] && [ "$LP" != 0 ]; then
            seule_presente
            if [ "$SP" = 4 ]; then sleep "${ABSENCE_ATTENTE_S:-15}"; seule_presente; [ "$SP" = 4 ] && ARR=1; fi
            if [ "$ARR" = 0 ]; then
                if [ "$SP" = 0 ]; then NONET=0; alerte "ALERTE liste d'inventaire non concluante (code $LP : $(head -c 120 "$D/presence.txt" 2>/dev/null | tr '\n' ' ')) : show instance $ID répond, instance présente"
                else
                    NONET=$((NONET + 1))
                    alerte "ALERTE inventaire ($NONET/3) : liste non concluante (code $LP : $(head -c 120 "$D/presence.txt" 2>/dev/null | tr '\n' ' ')) et show instance $ID non concluant (code $SP : $(head -c 120 "$D/presence-seule.txt" 2>/dev/null | tr '\n' ' ')) : présence non établie"
                    if [ "$NONET" -ge 3 ]; then
                        DEC="ARRET inventaire : présence de l'instance $ID non établie trois relevés de suite (ni la liste ni show instance ne concluent) : vérifier à la main (vastai show instances), puis message ; la minuterie de l'instance borne la dépense"
                        alerte "$DEC"; exit 3
                    fi
                fi
            fi
        else NONET=0
        fi
        if [ "$ARR" = 1 ]; then
            DEC="ARRET mort : instance $ID absente à deux relevés (liste non vide sans elle, ou instance seule introuvable) ; confirmer par show instance $ID avant de conclure à une destruction ; relever la cause dans $D/journal-instance.txt (dernières lignes AMORCE) et sur la branche poussée"
            alerte "$DEC"; exit 3
        fi
        if DEC=$(python3 -I -B -c "$SESSION8" surveillance "$PLC" "$CRU" "$D/progres.txt" "$now" "$PC" "$PS" "$CR" "$ANT" "$TEL" ${FACT:+"$FACT"} 2>&1); then ILLISIBLES=0   # T08 : compte rendu à 40 USD
        else
            ILLISIBLES=$((ILLISIBLES + 1))
            if [ "$ILLISIBLES" -ge 3 ]; then DEC="ARRET garde : garde de dépense illisible trois fois de suite ($DEC) : arrêter l'instance par son identifiant (R10), sans garde la dépense n'est plus bornée"
            else DEC="ALERTE garde de dépense illisible ($ILLISIBLES/3) : $DEC"; fi
        fi
        echo "$(date -u +%FT%TZ) $DEC" >> "$D/surveillance.txt"
        case "$DEC" in
            ARRET*) echo "$DEC"; echo "ARRÊT PAR L'IDENTIFIANT (R10) : timeout -k 5 120 $VAST stop instance $ID"; exit 3 ;;
            FIN*) echo "$DEC"; echo "FIN : l'amorce détruit la machine après le versement prouvé (M-3, « Devis » : aucune garde de 72 heures) ; vérifier la poussée (ordre, étape 9), puis l'inventaire ; machine encore là : destruction par l'identifiant (R10) : timeout -k 5 120 $VAST destroy instance $ID"; exit 0 ;;   # T08
            REFUS*) echo "$DEC"; exit 4 ;;
            "ALERTE compte rendu"*) if [ ! -e "$D/compte-rendu-alerte.txt" ]; then echo "$(date -u +%FT%TZ) $DEC" | tee "$D/compte-rendu-alerte.txt"; fi ;;   # T08 : une seule fois
            ALERTE*) echo "$(date -u +%FT%TZ) $DEC" ;;
        esac
        sleep "$INTERVALLE"
    done ;;
--verifier-go-seulement)
    # T08 : vérification seule de la ligne de GO de la course (GO_ID de l'environnement, admise par la configuration donnée, lue au registre avec sa prolongation, son plafond et sa fin de validité) et de la dépense antérieure ; NE CRÉE RIEN (aucun dossier, aucun fichier, aucun appel à l'outil de location)
    CFG="${2:?configuration de la course (fichier JSON)}"; ANT_EPR="${3:-0}"; JOUR="${4:-$(date -u +%F)}"
    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN) : rien vérifié, rien créé"; exit 2; }
    [ -f "$CFG" ] && [ -f "$REG" ] || { echo "configuration $CFG ou registre $REG absent : rien vérifié, rien créé"; exit 2; }
    [[ "$ANT_EPR" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "dépense antérieure ($ANT_EPR) : nombre positif en USD attendu : refus"; exit 2; }
    GOL=$(python3 -I -B -c "$SESSION8" go "$REG" "$CFG" "$GO_ID_ENV" "$JOUR") || { echo "GO $GO_ID_ENV refusé : $GOL"; exit 2; }
    PLC=$(cle_config "$CFG" lancement.plafond_usd) || { echo "plafond illisible : refus"; exit 2; }
    python3 -I -c 'import sys; from decimal import Decimal as D; sys.exit(0 if D(sys.argv[1]) < D(sys.argv[2]) else 1)' "$ANT_EPR" "$PLC" || { echo "dépense antérieure $ANT_EPR ≥ plafond $PLC USD : refus"; exit 2; }
    echo "GO VÉRIFIÉ, RIEN CRÉÉ : $GOL ; dépense antérieure $ANT_EPR < plafond $PLC USD" ;;
*) echo "usage : controles | controles-epreuve | creation | apres-creation | surveillance | --verifier-go-seulement" >&2; exit 2 ;;
esac
