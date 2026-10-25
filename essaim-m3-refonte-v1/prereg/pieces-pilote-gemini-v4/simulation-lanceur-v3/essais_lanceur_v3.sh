#!/usr/bin/env bash
# Essais du lanceur v3 : chaque garde sur un artefact (R5), à lancer après le cas sain (dont le rapport JUnit est repris).
set -u
C=/tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/essai-lanceur-v3
S=/tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/essai-lanceur
L=/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/lancer_pilote_gemini_v4_question_v3.sh
PYV=/home/claude/controle-ia-travail/.venv/bin/python
J="$C/sain/pilote-gemini-organisme-v4-question-v1/essais-v1.xml"
RES="113 passed, 1 deselected in 120.00s"
F="$C/faux"
cd /tmp
base() { env MODE=simulation DEPOT=/home/claude/essaim-gradient GRAINE=12345 PYTHON="$PYV" REGISTRE_GO_SOURCE="$S/go-sain.md" \
             DEPENSES_SOURCE="$S/depenses-sain.md" RESTE_GO07_USD=160 APPEL_CONTROLE_FICHIER="$C/appel-controle-factice.txt" "$@"; }
rapide() { base ESSAI_JUNIT_EXISTANT="$J" ESSAI_RESUME_EXISTANT="$RES" "$@"; }
D=(timeout 600 bash "$L")
echo "lanceur $(sha256sum "$L" | cut -c1-16)"
echo "V1 variable d'essai en réel : $(env MODE=reel DEPOT=/home/claude/essaim-gradient GRAINE=1 PILOTE_RACINE=/tmp/x ANTHROPIC_API_KEY=factice GEMINI_API_KEY_2=factice bash "$L" 2>&1 | tail -1)"
echo "V2 clés absentes en réel : $(env -u ANTHROPIC_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 MODE=reel DEPOT=/home/claude/essaim-gradient GRAINE=1 bash "$L" 2>&1 | tail -1)"
echo "V3 réel hors root : $(setpriv --reuid=65534 --regid=65534 --clear-groups env MODE=reel DEPOT=/home/claude/essaim-gradient GRAINE=1 ANTHROPIC_API_KEY=factice GEMINI_API_KEY_2=factice bash "$L" 2>&1 | tail -1)"
bash -c 'exec -a "python3 -m essaim_m3 simuler --factice" sleep 120' & FAUX=$!
sleep 1
echo "V4 autre course en cours : $(base PILOTE_RACINE="$C/v4" bash "$L" 2>&1 | tail -1)"
kill "$FAUX" 2>/dev/null; wait "$FAUX" 2>/dev/null
echo "V5 course déjà partie (R3) : $(base PILOTE_RACINE="$C/sain" TENTATIVE=2 "${D[@]}" 2>&1 | tail -1)"
mkdir -p "$C/v6/pilote-gemini-organisme-v4-question-v1"
echo "V6 dossier existant (R12) : $(base PILOTE_RACINE="$C/v6" "${D[@]}" 2>&1 | tail -1)"
echo "V7 commit absent : $(base PILOTE_RACINE="$C/v7" ESSAI_ARTEFACT=commit "${D[@]}" 2>&1 | tail -1)"
echo "V8 HEAD au code différent : $(base PILOTE_RACINE="$C/v8" DEPOT="$C/wt-head" "${D[@]}" 2>&1 | tail -1)"
echo "V9 arbre de travail modifié : $(base PILOTE_RACINE="$C/v9" DEPOT="$C/wt-sale" "${D[@]}" 2>&1 | tail -1)"
echo "V10 fichier non suivi : $(base PILOTE_RACINE="$C/v10" DEPOT="$C/wt-nonsuivi" "${D[@]}" 2>&1 | tail -1)"
echo "V11 banque : $(base PILOTE_RACINE="$C/v11" ESSAI_ARTEFACT=banque "${D[@]}" 2>&1 | tail -1)"
echo "V12 mission : $(base PILOTE_RACINE="$C/v12" ESSAI_ARTEFACT=mission "${D[@]}" 2>&1 | tail -1)"
echo "V13 préenregistrement d'autre empreinte : $(base PILOTE_RACINE="$C/v13" PREREG="$F/prereg-sain.md" PREREG_SHA256=0000 "${D[@]}" 2>&1 | tail -1)"
echo "V14 compagnon absent : $(base PILOTE_RACINE="$C/v14" PREREG="$F/prereg-sans-compagnon.md" PREREG_SHA256="$(sha256sum "$F/prereg-sans-compagnon.md" | cut -d' ' -f1)" "${D[@]}" 2>&1 | tail -1)"
echo "V15 graine non écrite : $(base PILOTE_RACINE="$C/v15" PREREG="$F/prereg-sans-graine.md" PREREG_SHA256="$(sha256sum "$F/prereg-sans-graine.md" | cut -d' ' -f1)" "${D[@]}" 2>&1 | tail -1)"
echo "V16 marqueur restant : $(base PILOTE_RACINE="$C/v16" PREREG="$F/prereg-marqueur.md" PREREG_SHA256="$(sha256sum "$F/prereg-marqueur.md" | cut -d' ' -f1)" "${D[@]}" 2>&1 | tail -1)"
echo "V17 organisme altéré : $(base PILOTE_RACINE="$C/v17" ESSAI_ARTEFACT=organisme "${D[@]}" 2>&1 | tail -1)"
echo "V18 fichier de l'organisme manquant : $(base PILOTE_RACINE="$C/v18" ESSAI_ARTEFACT=nombre "${D[@]}" 2>&1 | tail -1)"
echo "V19 question altérée : $(base PILOTE_RACINE="$C/v19" ESSAI_ARTEFACT=question "${D[@]}" 2>&1 | tail -1)"
echo "V20 ligne du GO sans calcul : $(base PILOTE_RACINE="$C/v20" REGISTRE_GO_SOURCE="$F/go-sans-calcul.md" "${D[@]}" 2>&1 | tail -1)"
echo "V21 calcul et nom sur deux lignes : $(base PILOTE_RACINE="$C/v21" REGISTRE_GO_SOURCE="$F/go-deux-lignes.md" "${D[@]}" 2>&1 | tail -1)"
echo "V22 dépense non consignée : $(base PILOTE_RACINE="$C/v22" DEPENSES_SOURCE="$S/depenses-vide.md" "${D[@]}" 2>&1 | tail -1)"
echo "V23 reste < 40 USD : $(base PILOTE_RACINE="$C/v23" RESTE_GO07_USD=39.99 "${D[@]}" 2>&1 | tail -1)"
echo "V24 appel de contrôle vide : $(base PILOTE_RACINE="$C/v24" ESSAI_ARTEFACT=appel "${D[@]}" 2>&1 | tail -1)"
echo "V25 essai en échec (JUnit) : $(rapide PILOTE_RACINE="$C/v25" ESSAI_ARTEFACT=junit-echec "${D[@]}" 2>&1 | tail -1)"
echo "V26 saut non permis d'un essai cité (JUnit) : $(rapide PILOTE_RACINE="$C/v26" ESSAI_ARTEFACT=junit-saut "${D[@]}" 2>&1 | tail -1)"
echo "V27 total différent de 114 (JUnit) : $(rapide PILOTE_RACINE="$C/v27" ESSAI_ARTEFACT=junit-total "${D[@]}" 2>&1 | tail -1)"
echo "V28 bytecode réintroduit : $(rapide PILOTE_RACINE="$C/v28" ESSAI_ARTEFACT=bytecode "${D[@]}" 2>&1 | tail -1)"
find /home/claude/essaim-gradient/essaim-m3-refonte-v1/essaim_m3 -name __pycache__ -prune -exec rm -rf {} +
echo "V29 refus du noyau après création de course/ (famille inconnue) : $(rapide PILOTE_RACINE="$C/t" ESSAI_ARTEFACT=famille "${D[@]}" 2>&1 | tail -1)"
echo "    note : $(grep -E 'aucune course partie|refus-avant' "$C/t/pilote-gemini-organisme-v4-question-v1/LANCEMENT.md" | cut -c1-220)"
echo "    ferme.tar.gz présent ? $(ls "$C/t/pilote-gemini-organisme-v4-question-v1/" | grep -c 'ferme.tar.gz')"
echo "V30 tentative 2 après ce refus : $(rapide PILOTE_RACINE="$C/t" TENTATIVE=2 "${D[@]}" 2>&1 | tail -1)"
echo "V31 tentative 3 après une course partie (R3) : $(rapide PILOTE_RACINE="$C/t" TENTATIVE=3 "${D[@]}" 2>&1 | tail -1)"
echo "V32 archive fermée incomplète : $(rapide PILOTE_RACINE="$C/v32" ESSAI_ARTEFACT=archive "${D[@]}" 2>&1 | tail -1)"
P32="$C/v32/pilote-gemini-organisme-v4-question-v1"
echo "    note : $(grep 'ARCHIVE FERMÉE INCOMPLÈTE' "$P32/LANCEMENT.md" | cut -c1-160) ; course/ gardé : $( [ -d "$P32/course" ] && echo oui || echo non) ; course/ dans A-POUSSER : $(grep -c '^course/' "$P32/A-POUSSER-v1.txt")"
echo "V33 espace hors de /var/tmp/essaim-m3 : $(rapide PILOTE_RACINE="$C/v33" ESSAI_ARTEFACT=espace "${D[@]}" 2>&1 | tail -1)"
echo "    note : $(grep 'hors de /var/tmp' "$C/v33/pilote-gemini-organisme-v4-question-v1/LANCEMENT.md" | cut -c1-140)"
echo "V34 fichier imprévu : $(rapide PILOTE_RACINE="$C/v34" ESSAI_ARTEFACT=imprevu "${D[@]}" 2>&1 | tail -1)"
P34="$C/v34/pilote-gemini-organisme-v4-question-v1"
echo "    note : $(grep 'imprévus' "$P34/LANCEMENT.md" | cut -c1-140) ; dans A-POUSSER : $(grep -c 'fichier-imprevu' "$P34/A-POUSSER-v1.txt")"
