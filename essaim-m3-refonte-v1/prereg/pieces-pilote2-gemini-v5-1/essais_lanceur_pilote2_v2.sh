#!/usr/bin/env bash
# Essais du lanceur du second pilote, v2 (`lancer_pilote2_gemini_v5_1_v2.sh` ; remplace la v1, gardée) : un cas sain par course (S, M) et les
# artefacts, chacun refusé ou traité avec sa raison (R5). Aucun appel réel : le mode réel n'est essayé que sur des refus
# qui précèdent tout appel (variables d'essai, clés, attestation) ; tout le reste en simulation.
# Usage : bash essais_lanceur_pilote2_v1.sh LANCEUR DEPOT PYTHON DOSSIER_ESSAIS JUNIT_SAIN
set -uo pipefail
LANCEUR="$1"; DEPOT="$2"; PY="$3"; E="$4"; JUNIT="$5"
RESUME_JUNIT="140 passed in 179.86s (0:02:59)"
mkdir -p "$E/entrees"
H="$(sha256sum "$LANCEUR" | cut -d' ' -f1)"
USD_COURSE="$(grep -E '^USD_COURSE=' "$LANCEUR" | head -1 | cut -d= -f2)"
SOUS_PLAFOND="$(awk -v x="$USD_COURSE" 'BEGIN { printf "%.2f", x - 0.01 }')"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote (essai) : question v2 `a54da93e…` et question écrite par Gemini `9e1da26d…` | au plus 120 USD | 2026-10-31 |\n' > "$E/entrees/go-sain.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | second pilote (essai) : `a54da93e…` `9e1da26d…` |\n' > "$E/entrees/go-sans-calcul.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote |\n| GO-2026-10-25-01 | `a54da93e…` `9e1da26d…` |\n' > "$E/entrees/go-deux-lignes.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote, question écrite par Gemini `9e1da26d…` seulement |\n' > "$E/entrees/go-autre-course.md"
printf '| GO-2026-10-24-07 | 2026-10-25 | calcul | `a54da93e…` `9e1da26d…` |\n' > "$E/entrees/go-autre-id.md"
printf '| 2026-10-25 | pilote2-gemini-v5-1-structure-v1 | GO-2026-10-25-01 | 60 |\n| 2026-10-25 | pilote2-gemini-v5-1-maieutique-v1 | GO-2026-10-25-01 | 60 |\n' > "$E/entrees/dep-sain.md"
printf '| 2026-10-25 | pilote2-gemini-v5-1-structure-v1 | GO-2026-10-24-07 | 60 |\n' > "$E/entrees/dep-absente.md"
td() {  # td FICHIER STATUT_FABLE MODELE_FABLE COUT_FABLE GO
  printf '{"especes": {"CLAUDE_FABLE_5_1": {"statut": "%s", "modele_servi": "%s", "cout_usd": %s}, "CLAUDE_OPUS_5_5": {"statut": "OK", "modele_servi": "claude-opus-5-5", "cout_usd": 0.000232}, "GEMINI_ARGON": {"statut": "OK", "modele_servi": "gemini-4-argon", "cout_usd": 0.00076}}, "cout_usd": 0.0016, "go": "%s"}\n' "$2" "$3" "$4" "$5" > "$1"
}
td "$E/entrees/td-sain.json" OK claude-fable-5-1 0.00058 GO-2026-10-25-01
td "$E/entrees/td-echec.json" ECHEC_API None 0 GO-2026-10-25-01
td "$E/entrees/td-modele.json" OK claude-fable-5-0 0.00058 GO-2026-10-25-01
td "$E/entrees/td-cout-nul.json" OK claude-fable-5-1 0 GO-2026-10-25-01
td "$E/entrees/td-autre-go.json" OK claude-fable-5-1 0.00058 GO-2026-10-24-07
printf '{"especes": {"CLAUDE_FABLE_5_1": {"statut": "OK", "modele_servi": "claude-fable-5-1", "cout_usd": 0.00058, "jetons_sortie": 0}, "CLAUDE_OPUS_5_5": {"statut": "OK", "modele_servi": "claude-opus-5-5", "cout_usd": 0.000232, "jetons_sortie": 12}, "GEMINI_ARGON": {"statut": "OK", "modele_servi": "gemini-4-argon", "cout_usd": 0.00076, "jetons_sortie": 9}}, "go": "GO-2026-10-25-01"}\n' > "$E/entrees/td-jetons-nuls.json"
printf '{"especes": ' > "$E/entrees/td-illisible.json"
pr() {  # pr FICHIER CONTENU [sans-compagnon]
  printf '%s\n' "$2" > "$1"; [ "${3:-}" = sans-compagnon ] || (cd "$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256")
}
pr "$E/entrees/prereg-sain.md" "graine de la course structure = 13 ; graine de la course maieutique = 17 ; lanceur $H"
pr "$E/entrees/prereg-sans-compagnon.md" "graine de la course structure = 13 ; lanceur $H" sans-compagnon
pr "$E/entrees/prereg-sans-graine.md" "graine de la course structure = 14 ; lanceur $H"
pr "$E/entrees/prereg-marqueur.md" "graine de la course structure = 13 ; lanceur $H ; <<EMPREINTE_PIECES>>"
pr "$E/entrees/prereg-sans-lanceur.md" "graine de la course structure = 13 ; lanceur 0000"
n=0; ok=0
cas() {  # cas NOM ATTENDU (motif cherché dans la sortie d'erreur et LANCEMENT.md) -- VAR=VAL…
  local nom="$1" attendu="$2"; shift 3
  n=$((n + 1))
  local racine="$E/cas-$nom"; rm -rf "$racine"; mkdir -p "$racine"
  touch "$E/entrees/td-sain.json" "$E/entrees/td-echec.json" "$E/entrees/td-modele.json" "$E/entrees/td-cout-nul.json" "$E/entrees/td-autre-go.json" "$E/entrees/td-illisible.json" "$E/entrees/td-jetons-nuls.json"
  env -i PATH="$PATH" HOME="$E" LANG=C.UTF-8 DEPOT="$DEPOT" PYTHON="$PY" GRAINE=13 COURSE=structure "$@" \
    PILOTE_RACINE_DEFAUT="$racine" bash -c 'export PILOTE_RACINE="${PILOTE_RACINE-$PILOTE_RACINE_DEFAUT}"; [ "$PILOTE_RACINE" = "-" ] && unset PILOTE_RACINE; exec bash "$0"' "$LANCEUR" \
    > "$racine/sortie.txt" 2> "$racine/erreur.txt"
  local code=$?
  local autre_racine="" a
  for a in "$@"; do case "$a" in PILOTE_RACINE=-) ;; PILOTE_RACINE=*) autre_racine="${a#PILOTE_RACINE=}";; esac; done
  local journal; journal="$(cat "$racine"/*/LANCEMENT.md 2>/dev/null; [ -n "$autre_racine" ] && cat "$autre_racine"/*/LANCEMENT.md 2>/dev/null; cat "$racine/erreur.txt")"
  if echo "$journal" | grep -qF -- "$attendu"; then ok=$((ok + 1)); echo "OK     $nom (code $code) : « $attendu »"
  else echo "ÉCHEC  $nom (code $code) : attendu « $attendu » ; erreur : $(tail -2 "$racine/erreur.txt" | tr '\n' ' ')"; fi
}
SAIN=(REGISTRE_GO_SOURCE="$E/entrees/go-sain.md" DEPENSES_SOURCE="$E/entrees/dep-sain.md" RESTE_GO_USD=150
      APPEL_CONTROLE_FICHIER="$E/entrees/td-sain.json" RECHARGE_ATTESTEE="essai" ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="$RESUME_JUNIT")
echo "== cas sains (simulation, rapport JUnit du cas sain repris) =="
cas sain-M "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique GRAINE=17 PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sain.md.sha256")" "${SAIN[@]}"
cas sain-S-prereg "graine 13 de la course structure écrite" -- MODE=simulation PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sain.md.sha256")" "${SAIN[@]}"
echo "== refus en mode réel, avant tout appel =="
cas reel-variable-essai "variable PILOTE_RACINE définie en mode réel" -- MODE=reel
cas reel-espace "variable ESSAIM_M3_ESPACE définie en mode réel" -- MODE=reel PILOTE_RACINE=- ESSAIM_M3_ESPACE=/var/tmp/x
cas reel-sans-cle "clé Anthropic absente (variable ANTHROPIC_API_KEY)" -- MODE=reel PILOTE_RACINE=-
cas reel-cle-nom-invalide "CLE_ANTHROPIC doit être un nom de variable" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC='x;y'
cas reel-cle-nommee-absente "clé Anthropic absente (variable CLE_TROIS)" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=CLE_TROIS ANTHROPIC_API_KEY=factice
cas reel-sans-gemini "clé Gemini absente (variable GEMINI_API_KEY)" -- MODE=reel PILOTE_RACINE=- ANTHROPIC_API_KEY=factice
cas reel-gemini-nommee-absente "clé Gemini absente (variable LUC_ABSENTE)" -- MODE=reel PILOTE_RACINE=- ANTHROPIC_API_KEY=factice CLE_GEMINI=LUC_ABSENTE GEMINI_API_KEY=factice
cas reel-sans-attestation "RECHARGE_ATTESTEE vide" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=CLE_TROIS CLE_TROIS=factice GEMINI_API_KEY_2=factice
echo "== refus avant le dossier =="
cas course-inconnue "COURSE inconnue" -- MODE=simulation COURSE=autre
cas mode-inconnu "MODE inconnu" -- MODE=essai
( exec -a "python3 -m essaim_m3 lancer --decalage-uid 900 --factice" sleep 30 ) & VOISIN=$!
sleep 0.3
cas voisine-meme-decalage "tourne déjà au décalage d'utilisateurs 900" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null
( exec -a "python3 -m essaim_m3 lancer --decalage-uid 300 --factice" sleep 60 ) & VOISIN=$!
sleep 0.3
cas voisine-autre-decalage "course(s) voisine(s) du noyau détectée(s)" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null
echo "== code, banque, mission, collisionneur =="
cas commit-question "absent du dépôt" -- MODE=simulation ESSAI_ARTEFACT=commit "${SAIN[@]}"
printf '# x\n' >> "$DEPOT/essaim-m3-refonte-v1/essaim_m3/noyau/question.py"
cas arbre-modifie "arbre de travail différent de 5d1d4fd" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" checkout -q -- essaim-m3-refonte-v1/essaim_m3/noyau/question.py
printf '# x\n' >> "$DEPOT/collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py"
cas collisionneur-modifie "arbre de travail différent de 5d1d4fd" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" checkout -q -- collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/tests/fichier_non_suivi.py"
cas non-suivi "fichiers non suivis ou modifiés" -- MODE=simulation "${SAIN[@]}"
rm -f "$DEPOT/essaim-m3-refonte-v1/tests/fichier_non_suivi.py"
git -C "$DEPOT" stash list > /dev/null
git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q --allow-empty -m "essai : tête vide" && TETE_ESSAI=1
printf '# y\n' >> "$DEPOT/essaim-m3-refonte-v1/essaim_m3/noyau/question.py"
git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -am "essai : code de tête différent"
cas tete-differente "code de HEAD différent de 5d1d4fd" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~2
cas banque "empreinte de la banque" -- MODE=simulation ESSAI_ARTEFACT=banque "${SAIN[@]}"
cas mission "empreinte de la mission" -- MODE=simulation ESSAI_ARTEFACT=mission "${SAIN[@]}"
echo "== isolation =="
cas traversable "au lieu de « 700 0 »" -- MODE=simulation ESSAI_ARTEFACT=traversable "${SAIN[@]}"
echo "== préenregistrement =="
cas prereg-empreinte "empreinte du préenregistrement ≠ PREREG_SHA256" -- MODE=simulation PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256=0000 "${SAIN[@]}"
cas prereg-compagnon "compagnon .sha256 du préenregistrement absent" -- MODE=simulation PREREG="$E/entrees/prereg-sans-compagnon.md" PREREG_SHA256="$(sha256sum "$E/entrees/prereg-sans-compagnon.md" | cut -d' ' -f1)" "${SAIN[@]}"
cas prereg-graine "n'est pas écrite dans le préenregistrement" -- MODE=simulation PREREG="$E/entrees/prereg-sans-graine.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sans-graine.md.sha256")" "${SAIN[@]}"
cas prereg-graine-autre-course "n'est pas écrite dans le préenregistrement" -- MODE=simulation COURSE=maieutique GRAINE=13 PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sain.md.sha256")" "${SAIN[@]}"
cas prereg-marqueur "marqueurs <<…>> restants" -- MODE=simulation PREREG="$E/entrees/prereg-marqueur.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-marqueur.md.sha256")" "${SAIN[@]}"
cas prereg-lanceur "ne cite pas l'empreinte de ce lanceur" -- MODE=simulation PREREG="$E/entrees/prereg-sans-lanceur.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sans-lanceur.md.sha256")" "${SAIN[@]}"
echo "== objet et question =="
cas organisme "empreinte d'arbre de l'organisme" -- MODE=simulation ESSAI_ARTEFACT=organisme "${SAIN[@]}"
cas organisme-fichier "fichiers au lieu de 19" -- MODE=simulation ESSAI_ARTEFACT=nombre "${SAIN[@]}"
cas question "empreinte de la question" -- MODE=simulation ESSAI_ARTEFACT=question "${SAIN[@]}"
echo "== registres =="
cas go-sans-calcul "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-calcul.md"
cas go-deux-lignes "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-deux-lignes.md"
cas go-autre-course "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-course.md"
cas go-autre-id "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-id.md"
cas depense-absente "lancement non consigné avant" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-absente.md"
cas reste-insuffisant "< $USD_COURSE" -- MODE=simulation "${SAIN[@]}" RESTE_GO_USD="$SOUS_PLAFOND"
echo "== test de dépense =="
cas td-vide "absent ou vide" -- MODE=simulation ESSAI_ARTEFACT=appel "${SAIN[@]}"
cas td-vieux "> 900 s" -- MODE=simulation ESSAI_ARTEFACT=appel-vieux "${SAIN[@]}"
cas td-echec "CLAUDE_FABLE_5_1 : statut 'ECHEC_API'" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-echec.json"
cas td-modele "modèle servi 'claude-fable-5-0'" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-modele.json"
cas td-cout-nul "coût 0 (un appel payant est exigé)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-cout-nul.json"
cas td-autre-go "go = 'GO-2026-10-24-07' (attendu GO-2026-10-25-01)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-autre-go.json"
cas td-jetons-nuls "jetons de sortie 0" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-jetons-nuls.json"
cas td-illisible "illisible" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-illisible.json"
echo "== essais =="
cas junit-echec "échecs" -- MODE=simulation ESSAI_ARTEFACT=junit-echec "${SAIN[@]}"
cas junit-saut "sauts (aucun permis)" -- MODE=simulation ESSAI_ARTEFACT=junit-saut "${SAIN[@]}"
cas junit-total "essais au lieu de 140" -- MODE=simulation ESSAI_ARTEFACT=junit-total "${SAIN[@]}"
# depuis 5d1d4fd, `boucle.empreinte_arbre` (et le `sha256_code_noyau` du manifeste) écarte le bytecode : un `.pyc` posé
# sous le noyau ne change pas l'empreinte ; le cas est « traité » (empreinte inchangée, course partie)
cas bytecode "noyau sans bytecode : empreinte d5d0efcc4677dd9957db3f324101b58e9475642e8e05926407579f056f653836" -- MODE=simulation ESSAI_ARTEFACT=bytecode "${SAIN[@]}"
find "$DEPOT/essaim-m3-refonte-v1/essaim_m3" -name __pycache__ -prune -exec rm -rf {} +
echo "== après le départ =="
cas famille-puis-tentatives "aucune course partie (pas de manifeste" -- MODE=simulation ESSAI_ARTEFACT=famille "${SAIN[@]}"
R_F="$E/cas-famille-puis-tentatives"
cas tentative-2 "archive fermée : ferme.tar.gz" -- MODE=simulation TENTATIVE=2 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas tentative-3 "R3 : jamais de seconde course" -- MODE=simulation TENTATIVE=3 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas archive-incomplete "ARCHIVE FERMÉE INCOMPLÈTE" -- MODE=simulation ESSAI_ARTEFACT=archive "${SAIN[@]}"
cas espace-hors "hors de /var/lib/essaim-m3" -- MODE=simulation ESSAI_ARTEFACT=espace "${SAIN[@]}"
cas imprevu "fichiers imprévus, NON poussés" -- MODE=simulation ESSAI_ARTEFACT=imprevu "${SAIN[@]}"
echo "== bilan : $ok sur $n cas conformes =="
