#!/usr/bin/env bash
# v4 : corrections de la contre-lecture de la v3 corrigée (wf_c00aece0-baa : 2 à corriger, 4 remarques) ; la v3 corrigée en place reste dans le bloc-notes, son texte contre-lu d'avant correction n'est pas gardé (constat 6)
# v3 corrigée : contre-lecture de la v3 (5 constats)
# v3 : corrections de la contre-lecture de la v2 (8 constats)
# v2 : corrections de la contre-lecture de la v1 (14 constats)
# Commandes de clôture et de lecture — témoin de Bailey, addendum 7, § 3 (gabarit v4).
# Texte qui fait foi : prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md, § 3 (scellé).
# En cas d'écart entre ce gabarit et le § 3, le § 3 prime ; ce fichier n'ajoute aucune règle.
#
# Rien n'est joué à la lecture de ce fichier : chaque étape est une fonction, jouée seulement par
#   bash commandes-cloture-bailey-v4.sh <étape>
# après que la session a rempli les paramètres ci-dessous (tous chemins absolus, § 3 : « tous chemins absolus »).
# Les étapes sont séparées par des gestes que ce fichier ne fait pas (constats, note de clôture, lecteurs) : chacune
# est jouée à la main, dans l'ordre, et sa sortie consignée. Les gardes d'ordre ne lisent que le journal de
# consignation (lignes que ce fichier écrit) et l'existence de fichiers, jamais une sortie ni une note.
#
# Étapes, dans l'ordre du § 3 :
#   (constats, hors fichier : arrêt et destruction de chaque poste ; suites permises jouées ou écartées)
#   e0-recuperer     récupération de la branche, une fois les postes arrêtés et détruits (préalable) ; refusée
#                    après le premier --calculer-attendu (pull interdit jusqu'au dernier contrôle final)
#   e1-listes        vérification de chaque liste de répertoires (sha256sum -c) puis recréation (mkdir -p) ;
#                    refusée après le premier --calculer-attendu
#   (assemblage, hors fichier, s'il y a lieu : relance par l'addendum 5, puis constat de son issue)
#   e2-chemins [R…]  vérification par programme des chemins (avant le premier --calculer-attendu) ; rejouée pour tout
#                    chemin neuf, dont le rapport d'un lecteur remplaçant (R…, chemins absolus)
#   e3-attendus V    --calculer-attendu pour le dossier réel du verdict V (« a », puis « b » s'il y a lieu)
#   e4-factice       essai de la commande sur un dossier factice (avant la note de clôture)
#   e5-sceller-note  scellement de la note de clôture (écrite à la main à partir du gabarit)
#   e6-lecture V     lecture scellée d'un verdict V (« a » : lecture-assemblee-v1 ; « b » : confirmation) ; une seule
#                    fois par verdict (refusée si le journal porte déjà une lecture de V)
#   e6-rejeu V       rejeu unique, à l'identique, après e6-lecture V, si l'exécution n'a laissé ni sortie ni compagnon
#   e6-retour-perdu V  retour de la commande perdu : sha256sum -c et empreinte du compagnon, sans ouvrir la sortie
#   e6-pousser       add, commit et push (hors de src/) des attendus, sorties, compagnons, note et journal ; rejouable
#   e7-venv          contrôle final seulement : environnement recréé s'il manque ; refusée avant que chaque lecture
#                    soit consignée et chaque rejeu dû joué (après e7, plus aucune lecture ni rejeu)
#   e8-controle V H  contrôle final (--controler), après le scellement de chaque verdict attendu ; une fois par verdict
set -euo pipefail

# ---------------------------------------------------------------------------------------------------------------------
# Paramètres (à remplir ; tout « < » restant fait refuser chaque étape)
# ---------------------------------------------------------------------------------------------------------------------
RACINE="<racine>"                       # § 3 : « arbre de travail principal du dépôt » (même chemin absolu que les postes)
BASE="$RACINE/runs/temoin-bailey-v1-20261111"  # § 3 : `<BASE>` = `<racine>/runs/temoin-bailey-v1-20261111` (poste v12, l. 47)
COMMIT="a904aa391cdcf2650b747fe64e48caa0ec8c5849"  # § 3 : « le commit du code, celui du § 4 et aucun autre » (§ 4)
PY="$RACINE/.venv/bin/python"           # § 3 : la commande passe par `<racine>/.venv/bin/python`
P="<P>"                                 # § 3 : `<P>` absent ou vide, hors de src/ et des dossiers lus, le même partout
BRANCHE="<branche des postes>"          # § 3 : la branche où les postes poussent (récupérée en e0, après tous les constats)

# Verdict « a » : run à 36 tours (§ 3, « Les deux verdicts » : sortie de `lecture-assemblee-v1`).
D_A="$BASE/lecture-assemblee-v1"        # dossier donné à la lecture (§ 3 : chemin absolu dans l'arbre principal)
A_A="<attendu a>"                       # fichier des empreintes attendues (écrit par --calculer-attendu, nom neuf, R12)
S_A="<sortie a>"                        # chemin de la sortie (nom neuf, R12)
# Verdict « b » : confirmation (§ 3 : sortie de la conduite, dossier de reprise, ou dossier assemblé ; vide si aucun
# run principal de la confirmation n'a ses journaux transférés et scellés (cas (ii) ou (iii) avant le début du run
# principal, ou journaux perdus), ou si l'assemblage d'une relance par l'addendum 5 a été refusé à ses deux exécutions).
D_B="<dossier b, ou vide>"
A_B="<attendu b, ou vide>"
S_B="<sortie b, ou vide>"

# Listes de répertoires (§ 3) : un dossier par poste qui produit un dossier ensuite lu ou assemblé (poste v13, seconde
# tentative, mise en place refaite, reprise de la lecture 38, relance par le chemin de l'addendum 5).
LISTES_DOSSIERS=("<dossier du poste 1>")  # ex. "$BASE/sortie-conduite-v15" ; vide « () » s'il n'y en a aucun

# Essai factice (§ 3 : dossier factice de même forme, construit par programme, aucune pièce réelle).
F_RACINE="<répertoire neuf, absent>"   # T3.poste_local y écrit ; le dossier factice est "$F_RACINE/sortie"
F_D="$F_RACINE/sortie"
F_A="<attendu factice>"
F_S="<sortie factice>"

# A_A, S_A, A_B, S_B, NOTE et JOURNAL sont sous $RACINE (hors de src/, de .git/ et des dossiers lus ; par exemple sous
# $BASE) : e6-pousser les ajoute à la branche, pour que le contrôle final puisse être joué dans un arbre recloné
# (§ 3 : « après récupération par git de chaque sortie, de son compagnon et de son attendu »). e2 le vérifie (--pousse).
NOTE="<note de clôture>"                 # § 3 : la note, hors de src/ et des dossiers lus
JOURNAL="<journal de consignation>"      # consignation des lignes rendues (hors de src/ et des dossiers lus)
# JOURNAL ne change plus après sa première ligne ; un remplacement avant e3 recopie les lignes e0 et e1 dans le nouveau
# journal.
VERIFIER="<chemin de verifier_chemins_cloture_v4.py>"  # hors de src/ (ne doit pas modifier src/, § 3)
# Rapport de chaque lecteur (<CHEMIN_RAPPORT> de consigne-lecteur-bailey-v4.md), fixé avant la note de clôture et
# vérifié en e2 (--autre) ; un chemin pris après (lecteur remplaçant, R12) est vérifié par « e2-chemins <chemin> »
# avant le lancement du remplaçant, ligne consignée au journal (hors de la note, déjà scellée). Ce tableau ne change
# plus après le scellement de la note (le script rempli y est cité par son empreinte).
RAPPORTS=("<rapport du lecteur a>" "<rapport du lecteur b ; à retirer s'il n'y a pas de verdict b>")

# ---------------------------------------------------------------------------------------------------------------------
# Aides
# ---------------------------------------------------------------------------------------------------------------------
exiger_parametres() {  # refuse tant qu'un paramètre porte encore « < » (gabarit non rempli)
  local v
  for v in RACINE P BRANCHE D_A A_A S_A F_RACINE F_A F_S NOTE JOURNAL VERIFIER; do
    case "${!v}" in *"<"*|"") echo "paramètre non rempli : $v" >&2; exit 2 ;; esac
  done
  for v in D_B A_B S_B; do
    case "${!v}" in *"<"*) echo "paramètre non rempli : $v (vide s'il n'y a pas de verdict b)" >&2; exit 2 ;; esac
  done
  case "${LISTES_DOSSIERS[*]:-}" in *"<"*) echo "paramètre non rempli : LISTES_DOSSIERS" >&2; exit 2 ;; esac
  [ "${#RAPPORTS[@]}" -gt 0 ] || { echo "paramètre non rempli : RAPPORTS (au moins le rapport du lecteur a)" >&2; exit 2; }
  for v in "${RAPPORTS[@]}"; do
    case "$v" in *"<"*|"") echo "paramètre non rempli : RAPPORTS" >&2; exit 2 ;; esac
  done
}

consigner() {  # ajoute une ligne horodatée (UTC) au journal et l'affiche ; ne lit aucune note
  printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$JOURNAL"
}

journal_porte() {  # vrai si une ligne du journal de consignation porte le texte $1 (fixe) ; journal absent : faux
  grep -qF -- "$1" "$JOURNAL" 2>/dev/null
}

# § 3 : `pull` est interdit « entre le premier `--calculer-attendu` et le dernier contrôle final » ; la création des
# répertoires des listes se fait « avant » (« hors les répertoires des listes des postes, créés avant »). Le premier
# `--calculer-attendu` est reconnu à la ligne « commande : » consignée avant toute exécution (e3 ou e4, réelle ou
# factice, même si elle a échoué ou si son retour est perdu), ou à une ligne e3 / e4 d'attendu.
calcul_attendu_joue() {
  # Condition indépendante du journal : un attendu (réel ou factice) ou son compagnon déjà sur disque.
  [ -e "$A_A" ] || [ -e "$A_A.sha256" ] || { [ -n "$A_B" ] && { [ -e "$A_B" ] || [ -e "$A_B.sha256" ]; }; } || [ -e "$F_A" ] || [ -e "$F_A.sha256" ] && return 0
  grep -qE ' commande : .* --calculer-attendu | e3 : attendu | e4 : attendu factice ' "$JOURNAL" 2>/dev/null
}

refuser_apres_calcul_attendu() {
  if calcul_attendu_joue; then
    echo "$1 : premier --calculer-attendu déjà joué (journal, ou attendu présent sur disque) : pull et recréation interdits jusqu'au dernier contrôle final (§ 3)" >&2
    exit 1
  fi
}

refuser_apres_e7() {  # § 3 : e7 vient « après la dernière commande sur un dossier réel » ; ensuite, plus aucune
  if grep -qE ' e7 : ' "$JOURNAL" 2>/dev/null; then
    echo "$1 : e7 déjà joué (journal) : plus aucune commande sur un dossier réel (§ 3)" >&2; exit 1
  fi
}

# § 3 : « la commande, la même pour `--calculer-attendu`, la lecture et `--controler` :
# `PYTHONPATH=<racine>/src PYTHONPYCACHEPREFIX=<P> <racine>/.venv/bin/python -B -P -m
# controle_ia.temoin_bailey.lecture_scellee_v3 …` » ; -B, -P et PYTHONPYCACHEPREFIX exigés par le code (garde_commande).
commande() {
  # § 3 : « la commande consignée » ; la note la recopie « telle que jouée » (ligne « commande : » du journal). Écrite au
  # journal seul (sortie standard jetée) : la ligne rendue par la commande, que l'appelant capture, reste seule.
  local ligne; ligne="$(printf '%q ' "$@")"
  consigner "commande : PYTHONPATH=$RACINE/src PYTHONPYCACHEPREFIX=$P $PY -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 ${ligne% }" >/dev/null
  PYTHONPATH="$RACINE/src" PYTHONPYCACHEPREFIX="$P" "$PY" -B -P -m controle_ia.temoin_bailey.lecture_scellee_v3 "$@"
}

verdict_vars() {  # V = a | b -> D, A, S
  case "${1:-}" in
    a) D="$D_A"; A="$A_A"; S="$S_A" ;;
    b) D="$D_B"; A="$A_B"; S="$S_B"
       [ -n "$D" ] || { echo "pas de verdict b à lire (D_B vide)" >&2; exit 2; } ;;
    *) echo "verdict « a » ou « b » attendu" >&2; exit 2 ;;
  esac
}

# ---------------------------------------------------------------------------------------------------------------------
# e0 — récupération de la branche (préalable ; hors de la fenêtre où `pull` est interdit)
# ---------------------------------------------------------------------------------------------------------------------
e0_recuperer() {
  exiger_parametres
  refuser_apres_calcul_attendu e0
  # § 3 : « La session ne joue un assemblage ni un `--calculer-attendu` qu'après avoir récupéré la branche une fois
  # constatés, pour chacun de ces postes, son arrêt (marque de fin […]) et la destruction de son instance » : ces
  # constats sont faits et consignés AVANT cette étape ; ce fichier ne les fait pas.
  # Ordre du § 3 : constats d'arrêt et de destruction de chaque poste → e0 → e1 → assemblage d'une relance par
  # l'addendum 5, s'il y en a une (hors de ce fichier ; refus ou erreur : rejeu unique vers une cible neuve) → constat
  # de son issue → e2 → e3. (§ 3 : « La session ne joue un assemblage ni un `--calculer-attendu` qu'après avoir récupéré
  # la branche » ; « Avant tout assemblage et tout `--calculer-attendu`, elle vérifie chaque liste […] puis crée […] » ;
  # « s'il y a un assemblage, aucun `--calculer-attendu` n'est joué avant celui-ci ou le constat de son refus » ; « Aucun
  # `--calculer-attendu` n'est joué tant qu'une suite permise avant la clôture […] n'est ni jouée […] ni écartée ».)
  # § 3 : `pull` n'est interdit qu'« entre le premier `--calculer-attendu` et le dernier contrôle final » : il est
  # permis ici, après tous les constats ; la dernière récupération avant e1 est « cette récupération » du § 3 (une liste
  # absente de la branche à ce moment est absente). e0 rejoué après un constat tardif : e1 est rejoué ensuite,
  # seulement avant le premier e3 (e0 et e1 refusent dès qu'un --calculer-attendu est consigné au journal).
  [ "$(git -C "$RACINE" branch --show-current)" = "$BRANCHE" ] || { echo "arbre hors de $BRANCHE" >&2; exit 1; }
  git -C "$RACINE" pull --ff-only origin "$BRANCHE"
  consigner "e0 : branche $BRANCHE récupérée, tête $(git -C "$RACINE" rev-parse HEAD)"
}

# ---------------------------------------------------------------------------------------------------------------------
# e1 — listes de répertoires : vérification puis recréation
# ---------------------------------------------------------------------------------------------------------------------
nom_liste() {  # § 3 : `<C>` = chemin du dossier relatif à `<BASE>`, chaque « / » remplacé par « -- »
  local rel="${1#"$BASE"/}"
  [ "$rel" != "$1" ] || { echo "dossier hors de <BASE> : $1" >&2; return 1; }
  printf 'repertoires-%s-v1.txt' "${rel//\//--}"
}

# Vérifie que chaque composant de « $1/$2 » (préfixes successifs de $2) est absent ou un répertoire qui n'est pas un
# lien ; rend sur la sortie standard le premier composant fautif, rien sinon. Aucun fichier lu ni écrit.
composant_fautif() {
  local base="$1" rel="$2" p="" c parts
  IFS=/ read -ra parts <<< "$rel"
  for c in "${parts[@]}"; do
    [ -n "$c" ] || continue
    p="${p:+$p/}$c"
    if [ -L "$base/$p" ] || { [ -e "$base/$p" ] && [ ! -d "$base/$p" ]; }; then printf '%s' "$p"; return 0; fi
  done
}

e1_listes() {
  exiger_parametres
  refuser_apres_calcul_attendu e1
  local dossier L rel sortie rc e bad f
  for dossier in "${LISTES_DOSSIERS[@]}"; do
    L="$(nom_liste "$dossier")"
    rel="${BASE#"$RACINE"/}/$L"
    # § 3 : « Une liste est absente si elle n'est pas sur la branche à cette récupération : rien n'est créé, et c'est
    # rapporté. »
    if ! git -C "$RACINE" cat-file -e "HEAD:$rel" 2>/dev/null; then
      consigner "e1 : $L absente de la branche ; rien créé"; continue
    fi
    # § 3 : « si la liste n'est pas scellée […] rien n'est créé de cette liste, et c'est rapporté ».
    if ! git -C "$RACINE" cat-file -e "HEAD:$rel.sha256" 2>/dev/null; then
      consigner "e1 : $L non scellée (compagnon absent de la branche) ; rien créé"; continue
    fi
    # § 3 : « elle vérifie chaque liste par `cd <BASE> && LC_ALL=C sha256sum -c repertoires-<C>-v1.txt.sha256` (qui doit
    # rendre « OK » ; « FAILED » ou une ligne mal formée : compagnon qui ne concorde pas ; un compagnon dit introuvable
    # alors que la liste et lui sont sur la branche, ou une commande qui ne démarre pas, ne constate rien et se rejoue,
    # corrigée dans ses seuls chemins) ».
    if [ ! -d "$BASE" ] || ! command -v sha256sum >/dev/null; then
      consigner "e1 : $L : commande non démarrée (<BASE> absent ou sha256sum introuvable), à rejouer, corrigée dans ses seuls chemins (rien constaté)"; exit 1
    fi
    set +e
    sortie="$(cd "$BASE" && LC_ALL=C sha256sum -c "$L.sha256" 2>&1)"; rc=$?
    set -e
    if [ "$sortie" != "$L: OK" ] || [ "$rc" -ne 0 ]; then
      case "$sortie" in
        # Seul le compagnon lui-même dit introuvable se rejoue. « sha256sum: <L>.sha256: no properly formatted checksum
        # lines found » (ligne mal formée) commence de même : il n'est pas visé ici et tombe dans « ne concorde pas ».
        "sha256sum: $L.sha256: No such file or directory"*)
          consigner "e1 : $L : compagnon dit introuvable : commande à rejouer, corrigée dans ses seuls chemins (rien constaté) : $sortie"; exit 1 ;;
        *)
          if [ "$rc" -ge 126 ]; then
            consigner "e1 : $L : commande non démarrée (code $rc), à rejouer, corrigée dans ses seuls chemins (rien constaté) : $sortie"; exit 1
          fi
          # « FAILED » (empreinte différente, ou fichier nommé par le compagnon introuvable : « FAILED open or read »),
          # ligne mal formée, ou toute autre sortie que « <L>: OK ».
          consigner "e1 : $L : compagnon qui ne concorde pas ($sortie) ; rien créé"; continue ;;
      esac
    fi
    consigner "e1 : $L : OK ($(cut -c1-64 "$BASE/$L.sha256"))"
    # § 3 : « Si une entrée est absolue, contient `..`, est vide, ou existe comme autre chose qu'un répertoire […] rien
    # n'est créé de cette liste, et c'est rapporté. » Toutes les entrées sont vérifiées avant toute création, et chacun
    # de leurs composants : un composant lien ou fichier ferait créer hors du dossier, ou échouer en cours de création.
    # Le dossier que nomme la liste et ses composants sous <BASE> sont vérifiés de même (« crée sous le dossier que nomme
    # la liste […] et rien d'autre »).
    f="$(composant_fautif "$BASE" "${dossier#"$BASE"/}")"
    if [ -n "$f" ]; then
      consigner "e1 : $L : dossier que nomme la liste, composant présent comme autre chose qu'un répertoire : $f ; rien créé"; continue
    fi
    bad=""
    while IFS= read -r e || [ -n "$e" ]; do
      if [ -z "$e" ]; then bad="entrée vide"; break; fi
      case "$e" in /*) bad="entrée absolue : $e"; break ;; *..*) bad="entrée qui contient « .. » : $e"; break ;; esac
      f="$(composant_fautif "$dossier" "$e")"
      if [ -n "$f" ]; then
        if [ "$f" = "${e%/}" ]; then bad="entrée présente comme autre chose qu'un répertoire : $e"
        else bad="composant présent comme autre chose qu'un répertoire : $f (entrée $e)"; fi
        break
      fi
    done < "$BASE/$L"
    if [ -n "$bad" ]; then consigner "e1 : $L : $bad ; rien créé de cette liste"; continue; fi
    # § 3 : « puis crée sous le dossier que nomme la liste, dans l'arbre principal, chaque répertoire listé, avec ses
    # parents absents (`mkdir -p`), et rien d'autre ; une entrée déjà présente comme répertoire est laissée telle quelle
    # (geste technique, aucune note lue) ».
    while IFS= read -r e || [ -n "$e" ]; do
      mkdir -p -- "$dossier/$e" || { consigner "e1 : $L : échec mkdir ($e), création partielle rapportée"; exit 1; }
    done < "$BASE/$L"
    consigner "e1 : $L : répertoires créés sous $dossier ($(grep -c '' "$BASE/$L") entrées)"
  done
  # § 3 : « La note de clôture cite chaque liste et son empreinte, ou son absence » : reprendre les lignes « e1 » du
  # journal dans la note.
}

# ---------------------------------------------------------------------------------------------------------------------
# e2 — vérification des chemins (avant le premier --calculer-attendu ; rejouée pour tout chemin neuf)
# ---------------------------------------------------------------------------------------------------------------------
e2_chemins() {
  exiger_parametres
  # § 3 : « avant le premier `--calculer-attendu`, la session fixe ces chemins et vérifie par programme (chemins résolus,
  # `Path.resolve().is_relative_to`) qu'aucun chemin d'attendu, de sortie, de `<P>`, du dossier factice, de son attendu
  # et de sa sortie, ni de la note de clôture n'est sous `<racine>/src` ni sous aucun des dossiers donnés à une lecture ;
  # un chemin qui échoue est remplacé avant toute écriture » ; « tout chemin neuf pris ensuite […] passe la même
  # vérification avant d'être écrit, et la note le cite » ; `<P>` « absent ou vide ».
  # Arguments de l'étape (facultatifs) : chemins neufs pris après la note (rapport d'un lecteur remplaçant, R12),
  # vérifiés comme les rapports (--autre) avant le lancement ; la ligne consignée les nomme.
  local x rc echec=0 neufs=("$@")
  for x in "${neufs[@]}"; do
    case "$x" in /*) ;; *) echo "chemin neuf non absolu : $x" >&2; exit 2 ;; esac
  done
  local args=(--racine "$RACINE" --dossier-lu "$D_A" --attendu "$A_A" --sortie "$S_A")
  if [ -n "$D_B" ]; then args+=(--dossier-lu "$D_B" --attendu "$A_B" --sortie "$S_B"); fi
  args+=(--cache-p "$P" --factice-dossier "$F_D" --factice-attendu "$F_A" --factice-sortie "$F_S" --note "$NOTE"
         --autre "$JOURNAL" --autre "$F_RACINE")
  # Rapport de chaque lecteur (consigne-lecteur-bailey-v4.md, <CHEMIN_RAPPORT>) : hors de src/ et des dossiers lus.
  for x in "${RAPPORTS[@]}" "${neufs[@]}"; do args+=(--autre "$x"); done
  # Chemins ajoutés à la branche par e6-pousser : sous <racine>, hors de src/, de .git/ et des dossiers lus.
  args+=(--pousse "$A_A" --pousse "$S_A" --pousse "$NOTE" --pousse "$JOURNAL")
  if [ -n "$D_B" ]; then args+=(--pousse "$A_B" --pousse "$S_B"); fi
  # Chemins poussés et leurs compagnons : aucun ne doit être ignoré par git (e6-pousser refuse sans `add -f`), ce qui
  # se constate ici, quand un chemin peut encore être remplacé, et non après l'écriture des sorties. Code 0 : ignoré ;
  # 1 : non ignoré ; autre (chemin hors de l'arbre, arbre illisible) : non jugé, refusé de même (aucun repli muet).
  for x in "$A_A" "$A_A.sha256" "$S_A" "$S_A.sha256" "$NOTE" "$NOTE.sha256" "$JOURNAL"; do
    [ -n "$x" ] || continue
    rc=0; git -C "$RACINE" check-ignore -q -- "$x" 2>/dev/null || rc=$?
    case "$rc" in
      0) consigner "e2 : chemin ignoré par git : $x (à remplacer)"; echec=1 ;;
      1) ;;
      *) consigner "e2 : chemin non jugé par git check-ignore (code $rc) : $x (à remplacer)"; echec=1 ;;
    esac
  done
  if [ -n "$D_B" ]; then
    for x in "$A_B" "$A_B.sha256" "$S_B" "$S_B.sha256"; do
      rc=0; git -C "$RACINE" check-ignore -q -- "$x" 2>/dev/null || rc=$?
      case "$rc" in
        0) consigner "e2 : chemin ignoré par git : $x (à remplacer)"; echec=1 ;;
        1) ;;
        *) consigner "e2 : chemin non jugé par git check-ignore (code $rc) : $x (à remplacer)"; echec=1 ;;
      esac
    done
  fi
  # -I : le script ne lit ni l'environnement ni le répertoire courant ; il n'importe que la bibliothèque standard.
  local r rcv=0; r="$("$PY" -I -B "$VERIFIER" "${args[@]}")" || rcv=$?
  [ -n "$r" ] && [ "$rcv" -le 1 ] || r="écart : vérificateur sans résultat (code $rcv) ${r}"
  # Bilan consigné : « conforme » seulement si le vérificateur et git check-ignore le sont tous deux.
  local bilan="$r"; [ "$echec" -eq 0 ] || bilan="écart : chemin(s) ignoré(s) ou non jugé(s) par git (lignes e2 ci-dessus) ; vérificateur : $r"
  if [ "${#neufs[@]}" -gt 0 ]; then consigner "e2 : vérification des chemins (chemins neufs : ${neufs[*]}) : $bilan"; else consigner "e2 : vérification des chemins : $bilan"; fi
  [ "$bilan" = "conforme" ] || { echo "chemin(s) à remplacer avant toute écriture" >&2; exit 1; }
}

# ---------------------------------------------------------------------------------------------------------------------
# e3 — empreinte attendue du dossier réel d'un verdict (une étape par verdict : un échec sur b ne bloque pas a)
# ---------------------------------------------------------------------------------------------------------------------
e3_attendus() {
  exiger_parametres; verdict_vars "${1:-}"
  # § 3 : la vérification, sur les paramètres courants, précède toute écriture (sort en code 1 sur un écart).
  e2_chemins
  # § 3 : `<P>` « absent ou vide […] le même pour toutes les exécutions (avec `-B`, rien n'y est écrit) ».
  if [ -e "$P" ] && [ -n "$(ls -A "$P")" ]; then echo "<P> non vide" >&2; exit 1; fi
  # Le code refuse un attendu déjà présent (R12) : un attendu déjà écrit n'est pas recalculé ici.
  if [ -e "$A" ]; then echo "attendu $1 déjà présent ($A) : rien joué" >&2; exit 1; fi
  # § 3 : « le fichier des empreintes attendues, écrit et scellé par `lecture_scellee_v3 --calculer-attendu … --commit
  # <ce commit> --vers …`, joué par la session avec la commande consignée, qui ne fait que des empreintes d'octets, ne lit
  # aucune note, et refuse si `src/` porte une modification, un fichier non suivi ou un fichier ignoré hors `__pycache__`,
  # si l'arbre `src/` de la tête n'est pas celui du commit nommé ».
  # À partir du premier e3 et jusqu'au dernier contrôle final (§ 3) : aucune installation ni désinstallation de
  # distribution, aucun fichier créé ou modifié sous src/ (hors __pycache__) ni sous un dossier lu, aucun git checkout,
  # switch, restore, reset, clean, stash, pull, merge, rebase dans cet arbre ; add, commit et push hors de src/ permis.
  local r
  r="$(cd "$RACINE" && commande --calculer-attendu "$D" --commit "$COMMIT" --vers "$A" 2>&1)" \
    || { consigner "e3 : attendu $1 : refus ou erreur, rien écrit : $r"; exit 1; }
  consigner "e3 : attendu $1 : $r"
  # § 3 : « Pour `lecture-assemblee-v1`, est lu l'état du dossier dans l'arbre principal au calcul de l'attendu,
  # rapporté tel quel » : l'empreinte de l'attendu a (champ « dossier ») est cet état.
}

# ---------------------------------------------------------------------------------------------------------------------
# e4 — essai factice (après les attendus réels, avant la note de clôture)
# ---------------------------------------------------------------------------------------------------------------------
e4_factice() {
  exiger_parametres
  e2_chemins
  [ -f "$A_A" ] && { [ -z "$D_B" ] || [ -f "$A_B" ]; } || { echo "attendu(s) réel(s) manquant(s) : jouer e3-attendus d'abord" >&2; exit 1; }
  [ ! -e "$F_RACINE" ] || { echo "F_RACINE existe déjà (R12 : répertoire neuf)" >&2; exit 1; }
  mkdir -p -- "$F_RACINE"
  # § 3 : « sur un dossier factice de même forme, construit par programme sans aucune pièce réelle (comme dans les
  # essais du § 4) » : `poste_local` des essais (21 tours, comme la répétition du 17 novembre). Processus distinct de la
  # commande ; -B : rien écrit sous tests/ ni src/.
  PYTHONPATH="$RACINE/src:$RACINE/tests" "$PY" -B -P -c '
import sys
from pathlib import Path
import test_temoin_bailey_condition6_v3 as T3
print(T3.poste_local(Path(sys.argv[1]), 21, k_regle=21))' "$F_RACINE" >/dev/null
  # § 3 : « avec un attendu calculé de même sur ce dossier factice ».
  local r h
  r="$(cd "$RACINE" && commande --calculer-attendu "$F_D" --commit "$COMMIT" --vers "$F_A" 2>&1)" \
    || { consigner "e4 : attendu factice : refus ou erreur : $r"; exit 1; }
  consigner "e4 : attendu factice : $r"
  # § 3 : « dont les champs `commit`, `code` et `environnement` sont égaux à ceux des attendus réels, ce que la session
  # vérifie par programme et que la note cite ». N'ouvre que des attendus (empreintes), aucune note.
  r="$("$PY" -I -B -c '
import json, sys
f = json.load(open(sys.argv[1], encoding="utf-8"))
reels = [json.load(open(p, encoding="utf-8")) for p in sys.argv[2:] if p]
ok = reels and all(all(f[k] == a[k] for k in ("commit", "code", "environnement")) for a in reels)
print("égaux" if ok else "différents")' "$F_A" "$A_A" "$A_B")"
  consigner "e4 : champs commit, code, environnement de l'attendu factice et des attendus réels : $r"
  [ "$r" = "égaux" ] || exit 1
  # § 3 : « la commande est jouée telle quelle, aux seuls chemins du dossier, de l'attendu et de la sortie près (même
  # `PYTHONPYCACHEPREFIX`) » ; « son issue est citée dans la note ».
  r="$(cd "$RACINE" && commande --dossier "$F_D" --sortie "$F_S" --attendu "$F_A")" || true
  consigner "e4 : lecture factice : $r"
  [ -f "$F_S.sha256" ] || { consigner "e4 : sortie factice non scellée : commande à corriger (chemins, arguments, variables), sans dossier réel"; exit 1; }
  # § 3 : la commande doit « aboutir » sur le factice ; sinon elle se corrige (chemins, arguments, variables) ou la
  # règle des 24 h s'applique. « refus : empreintes », « refus ou erreur » : non abouti.
  case "$r" in
    *'"issue": "aboutie"'*) ;;
    *) consigner "e4 : lecture factice non aboutie : commande à corriger (chemins, arguments, variables), sans dossier réel"; exit 1 ;;
  esac
  # Pour la règle des 24 h du § 3, l'issue retenue est celle de la lecture factice (ci-dessus) : elle a abouti.
  # Contrôle du factice ensuite, comme la répétition du 17 novembre (le § 3 n'exige que la lecture) : un écart arrête
  # l'étape, mais il est consigné à part, la lecture factice restant « aboutie » (la note le rapporte au § 8).
  consigner "e4 : lecture factice aboutie (issue retenue pour la règle des 24 h, § 3)"
  h="$(cut -c1-64 "$F_S.sha256")"
  r="$(cd "$RACINE" && commande --controler "$F_S" --attendu "$F_A" --dossier "$F_D" --empreinte "$h")" || true
  consigner "e4 : contrôle factice : $r"
  case "$r" in
    *'"controle": "conforme"'*) ;;
    *) consigner "e4 : contrôle factice : écart (lecture factice aboutie ; contrôle à corriger dans ses chemins, arguments, variables ; à rapporter dans la note, § 8)"; exit 1 ;;
  esac
  # § 3 : « Une commande qui y échoue ne se corrige que dans ses chemins, arguments et variables, jamais dans le code
  # (§ 4), sans aucun dossier réel (un attendu réel calculé avec une commande corrigée est recalculé sous un nom neuf,
  # R12) ; si aucune n'y aboutit dans les 24 h qui suivent le premier essai, la note de clôture le dit et nomme la
  # dernière commande essayée » ; tout chemin neuf repasse e2 avant d'être écrit.
}

# ---------------------------------------------------------------------------------------------------------------------
# e5 — scellement de la note de clôture (écrite à la main à partir du gabarit ; champs techniques seulement)
# ---------------------------------------------------------------------------------------------------------------------
e5_sceller_note() {
  exiger_parametres
  # § 3 : « Clôture de la confirmation : constatée par une note scellée de la session, qui ne cite que des champs
  # techniques ». -B : rien écrit sous src/ (§ 3, aucun fichier créé sous src/ hors __pycache__).
  local r; r="$(PYTHONPATH="$RACINE/src" PYTHONPYCACHEPREFIX="$P" "$PY" -B -P -m controle_ia.scellement sceller "$NOTE")"
  consigner "e5 : note de clôture scellée : $r"
  # § 3 : « Dans les 24 h qui suivent la note de clôture, la session joue la commande consignée, une fois par verdict ».
  consigner "e5 : échéance de la lecture : 24 h après cette ligne"
}

# ---------------------------------------------------------------------------------------------------------------------
# e6 — lecture scellée (une fois par verdict à lire ; la sortie n'est jamais ouverte)
# ---------------------------------------------------------------------------------------------------------------------
e6_lecture() {
  exiger_parametres; verdict_vars "${1:-}"; refuser_apres_e7 "e6-lecture"
  # § 3 : « la session joue la commande consignée, une fois par verdict à lire » : refusé si le journal porte déjà une
  # lecture de ce verdict (lancée, rendue, ou restée sans sortie) ; ensuite, seuls e6-rejeu (une fois, si aucune sortie
  # n'est présente) ou e6-retour-perdu restent permis.
  if journal_porte "e6 : lecture $1 :"; then
    echo "lecture $1 déjà jouée (journal) : e6-rejeu ou e6-retour-perdu" >&2; exit 1
  fi
  # § 3 : « il refuse sans rien jouer ni rien écrire si cette sortie, ou son compagnon, existe déjà » ; une ligne
  # « refus : sortie déjà présente (R12) » n'est pas une issue.
  if [ -e "$S" ] || [ -e "$S.sha256" ]; then echo "sortie ou compagnon déjà présent : rien joué" >&2; exit 1; fi
  # Ligne de lancement consignée avant de jouer : une perte du retour (session coupée) ne rouvre pas une lecture.
  consigner "e6 : lecture $1 : lancée"
  # § 3 : « la session joue la commande consignée, une fois par verdict à lire, et consigne l'empreinte et l'issue
  # rendues, sans ouvrir la sortie ». Le code de retour est consigné (0 : aboutie ; 2 : autre issue écrite ; 3 : refus
  # sans écriture ; 126, 127 : commande non démarrée), sans rien décider sur lui.
  local r rc=0; r="$(cd "$RACINE" && commande --dossier "$D" --sortie "$S" --attendu "$A")" || rc=$?
  consigner "e6 : lecture $1 : $r (code $rc)"
  # Aucune sortie scellée laissée : e6-rejeu (une fois, à l'identique) si aucune sortie n'est présente (§ 3).
  [ -e "$S.sha256" ] || echo "e6 : lecture $1 : aucune sortie scellée laissée : e6-rejeu $1 (une fois) si aucune sortie n'est présente" >&2
}

e6_rejeu() {
  exiger_parametres; verdict_vars "${1:-}"; refuser_apres_e7 "e6-rejeu"
  # § 3 : « Une exécution de la commande qui ne laisse pas de sortie scellée (le code n'a pas démarré, ou s'est arrêté
  # avant de sceller) est rejouée une fois, à l'identique, si aucune sortie n'est présente ; une sortie présente sans son
  # compagnon n'est ni ouverte ni scellée après coup, et la commande n'est pas rejouée […] : l'absence de sortie est
  # constatée. » Seulement après la lecture de ce verdict (e6-lecture), et au plus une fois par verdict : refusé si le
  # journal porte déjà un rejeu de ce verdict (la ligne de lancement est consignée avant de jouer, pour qu'une perte du
  # retour n'ouvre pas un second rejeu).
  if ! journal_porte "e6 : lecture $1 :"; then
    echo "aucune lecture $1 consignée (journal) : jouer e6-lecture $1 d'abord" >&2; exit 1
  fi
  if journal_porte "e6 : rejeu unique de la lecture $1 :"; then
    echo "rejeu de la lecture $1 déjà joué (journal) : pas de second rejeu" >&2; exit 1
  fi
  if [ -e "$S" ] && [ ! -e "$S.sha256" ]; then consigner "e6 : $1 : sortie présente sans son compagnon : absence de sortie scellée constatée"; exit 1; fi
  # Compagnon présent sans sa sortie : le code refuserait (« refus : sortie déjà présente (R12) », qui n'est pas une
  # issue) ; aucune sortie scellée ne peut plus être écrite à ce chemin : l'absence de sortie scellée est constatée.
  if [ ! -e "$S" ] && [ -e "$S.sha256" ]; then consigner "e6 : $1 : compagnon sans sortie : absence de sortie scellée constatée"; exit 1; fi
  if [ -e "$S" ]; then echo "sortie et compagnon présents : pas de rejeu (retour perdu : e6-retour-perdu)" >&2; exit 1; fi
  consigner "e6 : rejeu unique de la lecture $1 : lancé"
  local r rc=0; r="$(cd "$RACINE" && commande --dossier "$D" --sortie "$S" --attendu "$A")" || rc=$?
  consigner "e6 : rejeu unique de la lecture $1 : $r (code $rc)"
  # § 3 : rejouée « une fois » : un rejeu qui ne laisse pas de sortie scellée clôt la voie ; l'absence de sortie scellée
  # est constatée (existence du compagnon seulement ; la sortie n'est pas ouverte).
  [ -e "$S.sha256" ] || consigner "e6 : $1 : rejeu sans sortie scellée : absence de sortie scellée constatée"
}

e6_retour_perdu() {
  exiger_parametres; verdict_vars "${1:-}"
  # § 3 : « Si la sortie et son compagnon sont présents mais que la ligne rendue est perdue ou illisible, la commande
  # n'est pas rejouée : la session joue `cd <répertoire de la sortie> && LC_ALL=C sha256sum -c <nom de la
  # sortie>.sha256`, qui doit rendre « OK », puis consigne l'empreinte entière (les 64 premiers caractères du compagnon,
  # `cut -c1-64 <sortie>.sha256`), sans ouvrir la sortie, et l'issue « non lue » ».
  local dir nom r
  dir="$(dirname -- "$S")"; nom="$(basename -- "$S")"
  set +e; r="$(cd "$dir" && LC_ALL=C sha256sum -c "$nom.sha256" 2>&1)"; set -e
  case "$r" in
    "$nom: OK") consigner "e6 : $1 : retour perdu ; sha256sum -c OK ; empreinte $(cut -c1-64 "$S.sha256") ; issue « non lue »" ;;
    *FAILED*) consigner "e6 : $1 : sha256sum -c FAILED : absence de sortie scellée constatée ($r)" ;;
    *"no properly formatted"*) consigner "e6 : $1 : sortie présente sans son compagnon : absence de sortie constatée ($r)" ;;
    *) consigner "e6 : $1 : rien constaté (compagnon introuvable ou commande non démarrée) ; à rejouer, corrigée dans ses seuls chemins : $r"; exit 1 ;;
  esac
}

# ---------------------------------------------------------------------------------------------------------------------
# e6-pousser — attendus, sorties, compagnons, note et journal ajoutés à la branche (hors de src/) ; rejouable
# ---------------------------------------------------------------------------------------------------------------------
e6_pousser() {
  exiger_parametres
  # § 3 : « `add`, `commit` et `push` hors de `src/` restent permis » ; « Le contrôle final peut l'être dans un arbre
  # recloné au même chemin absolu […], après récupération par git de chaque sortie, de son compagnon et de son
  # attendu ». Jouée après e6 (lectures, rejeu, retour perdu) et rejouée après e8 pour le journal. N'ouvre aucune sortie.
  [ "$(git -C "$RACINE" branch --show-current)" = "$BRANCHE" ] || { echo "arbre hors de $BRANCHE" >&2; exit 1; }
  local racine_r src_r ch r chemins=() d
  racine_r="$(realpath -- "$RACINE")"; src_r="$racine_r/src"
  for ch in "$A_A" "$S_A" "$A_B" "$S_B" "$NOTE"; do
    [ -n "$ch" ] || continue
    for r in "$ch" "$ch.sha256"; do [ -e "$r" ] && chemins+=("$r"); done
  done
  chemins+=("$JOURNAL")
  for ch in "${chemins[@]}"; do
    r="$(realpath -- "$ch")"
    case "$r/" in "$racine_r"/*) ;; *) echo "hors de <racine> : $ch" >&2; exit 1 ;; esac
    case "$r/" in "$src_r"/*|"$racine_r/.git"/*) echo "sous src/ ou .git/ : $ch" >&2; exit 1 ;; esac
    for d in "$D_A" "$D_B"; do
      [ -n "$d" ] || continue
      case "$r/" in "$(realpath -m -- "$d")"/*) echo "sous le dossier lu $d : $ch" >&2; exit 1 ;; esac
    done
    if git -C "$RACINE" check-ignore -q -- "$r"; then echo "ignoré par git : $ch (aucun add -f)" >&2; exit 1; fi
  done
  # Ligne consignée avant l'ajout, pour que le journal poussé la porte (la tête après la poussée est affichée seulement).
  consigner "e6-pousser : ${#chemins[@]} fichiers vers $BRANCHE"
  git -C "$RACINE" add -- "${chemins[@]}"
  # Seuls ces chemins sont engagés (rien d'autre de l'index, rien sous src/).
  if git -C "$RACINE" diff --cached --quiet -- "${chemins[@]}"; then
    echo "e6-pousser : rien de neuf à engager"
  else
    git -C "$RACINE" commit -q -m "Témoin de Bailey, clôture : attendus et sorties scellés, note, journal" -- "${chemins[@]}"
  fi
  # Refus non-fast-forward (la branche distante a avancé, par exemple une autre session qui pousse) : ne pas faire de
  # pull ni de merge (interdits jusqu'au dernier contrôle final, § 3) ; pousser ces seuls commits vers une branche
  # neuve, absente du distant (R12) : `git -C <racine> push origin HEAD:refs/heads/cloture-bailey-v1`, récupérée par
  # clone au contrôle final (`git clone --branch cloture-bailey-v1 …` au même chemin absolu) ; sinon, contrôle final
  # joué dans l'arbre principal (§ 3 : il « peut » l'être dans un arbre recloné). Cette voie est fixée d'avance au § 9
  # de la note ; le refus et le choix fait sont consignés au journal (la note est scellée avant). Rien n'est poussé
  # ailleurs par ce fichier.
  if ! git -C "$RACINE" push -q origin "$BRANCHE"; then
    consigner "e6-pousser : push refusé vers $BRANCHE (tête locale $(git -C "$RACINE" rev-parse HEAD)) ; ni pull ni merge : branche neuve (git push origin HEAD:refs/heads/cloture-bailey-v1) ou contrôle final dans l'arbre principal"
    exit 1
  fi
  echo "e6-pousser : poussé sur $BRANCHE, tête $(git -C "$RACINE" rev-parse HEAD)"
}

# ---------------------------------------------------------------------------------------------------------------------
# Lecteurs (hors de ce fichier) — § 3, « Les deux verdicts » : deux lecteurs neufs distincts, lancés ensemble dans les
# 24 h qui suivent la dernière sortie consignée, sur consigne-lecteur-bailey-v4.md ; lancement (heure, fichiers donnés,
# consigne) consigné avant qu'aucun des deux n'ait rendu ; remplacement selon la règle mécanique du § 3 (chemin de
# rapport neuf du remplaçant vérifié avant son lancement : « e2-chemins <chemin neuf> »).
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# e7 — environnement du contrôle final, s'il manque (après la dernière commande sur un dossier réel seulement)
# ---------------------------------------------------------------------------------------------------------------------
e7_venv() {
  exiger_parametres
  # § 3 : « Si, après la dernière commande sur un dossier réel, `<racine>/.venv/bin/python` manque, la session crée cet
  # environnement (`python3 -m venv <racine>/.venv`, Python 3.11 ou plus, pour `-P` […]) et y installe, par
  # `<racine>/.venv/bin/python -m pip install numpy==2.4.6`, la seule distribution que `--controler` importe hors de la
  # bibliothèque standard […], sans toucher à `src/`, et c'est rapporté. »
  # « après la dernière commande sur un dossier réel » : refusé tant que le journal ne porte pas la lecture de chaque
  # verdict à lire (a, et b si D_B n'est pas vide) et, pour une lecture qui n'a laissé aucune sortie scellée, son rejeu
  # unique ou le constat de l'absence de sortie scellée. Ne lit que le journal et l'existence des compagnons. Une fois
  # e7 consigné, e6-lecture et e6-rejeu refusent.
  local v vs=(a) S_V
  [ -z "$D_B" ] || vs+=(b)
  for v in "${vs[@]}"; do
    if ! journal_porte "e6 : lecture $v :"; then
      echo "e7 : aucune lecture $v consignée : environnement non recréé avant la dernière commande sur un dossier réel (§ 3)" >&2; exit 1
    fi
    if [ "$v" = a ]; then S_V="$S_A"; else S_V="$S_B"; fi
    if [ ! -e "$S_V.sha256" ] && ! journal_porte "e6 : rejeu unique de la lecture $v :" \
       && ! grep -qE " e6 : $v : .*absence de sortie" "$JOURNAL" 2>/dev/null; then
      echo "e7 : lecture $v sans sortie scellée, rejeu unique encore dû (e6-rejeu $v) : environnement non recréé (§ 3)" >&2; exit 1
    fi
  done
  if [ -x "$PY" ]; then if journal_porte "e7 : création de $RACINE/.venv lancée" && ! journal_porte "e7 : $RACINE/.venv créé ; numpy==2.4.6 installé"; then consigner "e7 : $PY présent après une création interrompue (à rapporter)"; else consigner "e7 : $PY présent ; rien créé"; fi; return 0; fi
  python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)' || { echo "Python 3.11 ou plus exigé" >&2; exit 1; }
  # Ligne consignée avant la création : une installation interrompue (réseau) reste visible au journal.
  consigner "e7 : création de $RACINE/.venv lancée"
  python3 -m venv "$RACINE/.venv"
  "$PY" -m pip install numpy==2.4.6
  consigner "e7 : $RACINE/.venv créé ; numpy==2.4.6 installé (à rapporter)"
}

# ---------------------------------------------------------------------------------------------------------------------
# e8 — contrôle final (après le scellement de chaque verdict attendu, ou le constat de son absence)
# ---------------------------------------------------------------------------------------------------------------------
e8_controle() {
  exiger_parametres; verdict_vars "${1:-}"
  local H="${2:-}"
  # § 3 : « la session joue, pour chaque sortie, `lecture_scellee_v3 --controler` avec l'attendu et le dossier que nomme
  # la note de clôture et l'empreinte qu'elle a consignée en jouant la commande (ou, retour perdu, l'empreinte entière
  # lue dans le compagnon, consignée de même) ; il ne rend que « conforme » ou « écart » : un écart vaut « pas de
  # verdict » pour ce run. » H est recopiée du journal (ligne e6), jamais relue dans le compagnon ici.
  [[ "$H" =~ ^[0-9a-f]{64}$ ]] || { echo "usage : e8-controle a|b <empreinte consignée, 64 caractères>" >&2; exit 2; }
  # H doit être l'empreinte consignée en e6 pour ce verdict (lecture, rejeu unique, ou retour perdu) ; lu au journal seul.
  grep -qE " e6 : (lecture|rejeu unique de la lecture) $1 : .*\"empreinte_sortie\": \"$H\"| e6 : $1 : retour perdu ; sha256sum -c OK ; empreinte $H " "$JOURNAL" || { echo "empreinte $H non consignée en e6 pour $1" >&2; exit 2; }
  # Une fois par sortie : la première ligne e8 de ce verdict fait foi.
  if journal_porte "e8 : contrôle final $1 :"; then echo "contrôle final $1 déjà joué : la première ligne fait foi" >&2; exit 1; fi
  # § 3 : le contrôle final peut être joué dans un arbre recloné au même chemin absolu, après récupération par git de
  # chaque sortie, de son compagnon et de son attendu (poussés par e6-pousser) ; « un contrôle qui ne peut être joué
  # ainsi vaut « écart » ».
  # Code consigné : une commande qui ne démarre pas, ou toute ligne autre que « conforme », vaut « écart » (§ 3).
  consigner "e8 : contrôle final $1 : lancé"
  local r rc=0; r="$(cd "$RACINE" && commande --controler "$S" --attendu "$A" --dossier "$D" --empreinte "$H")" || rc=$?
  case "$r" in *'"controle": "conforme"'*) consigner "e8 : contrôle final $1 : $r" ;; *) consigner "e8 : contrôle final $1 : écart ($r ; code $rc)" ;; esac
}

# ---------------------------------------------------------------------------------------------------------------------
case "${1:-}" in
  e0-recuperer) e0_recuperer ;;
  e1-listes) e1_listes ;;
  e2-chemins) e2_chemins "${@:2}" ;;
  e3-attendus) e3_attendus "${2:-}" ;;
  e4-factice) e4_factice ;;
  e5-sceller-note) e5_sceller_note ;;
  e6-lecture) e6_lecture "${2:-}" ;;
  e6-rejeu) e6_rejeu "${2:-}" ;;
  e6-retour-perdu) e6_retour_perdu "${2:-}" ;;
  e6-pousser) e6_pousser ;;
  e7-venv) e7_venv ;;
  e8-controle) e8_controle "${2:-}" "${3:-}" ;;
  *) sed -n '2,35p' "$0"; exit 2 ;;
esac
