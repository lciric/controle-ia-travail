#!/usr/bin/env bash
# Essais du lanceur du second pilote pour la v5.2, v5 (`lancer_pilote2_gemini_v5_2_v5.sh` ; versions gardées : v1 à v3,
# 104 cas sur 104 chacune ; v4, 106 sur 106). La v5 essaie les gardes ajoutées sur la contre-lecture 1 : statuts des
# appels de M (P52C1-02), passerelle de sortie (P52C1-04), noms des clés des runs et du test de dépense (P52C1-05). : un cas sain complet par course (M avec les essais du noyau exécutés, puis S avec M
# pour course précédente) et les artefacts, chacun refusé ou traité avec sa raison (R5). Aucun appel réel : le mode réel
# n'est essayé que sur des refus qui précèdent tout appel ; tout le reste en simulation.
# Usage : bash essais_lanceur_pilote2_v5_2_v5.sh LANCEUR DEPOT PYTHON DOSSIER_ESSAIS DEPOT_SOUS_ROOT PYTHON_AVEC_HTTPX
# (DEPOT_SOUS_ROOT : une seconde copie du dépôt sous /root, pour les refus du mode réel qui suivent la vérification du
# dossier du dépôt ; aucun de ces cas n'atteint un appel : ils refusent à l'étape (0))
set -uo pipefail
LANCEUR="$1"; DEPOT="$2"; PY="$3"; E="$4"; DEPOT_ROOT="$5"; PY_HTTPX="$6"
CLES_REEL=(CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_3=factice CLE_GEMINI=GEMINI_API_KEY_2 GEMINI_API_KEY_2=factice)
INFRA=(); for v in HTTPS_PROXY https_proxy HTTP_PROXY http_proxy NO_PROXY no_proxy SSL_CERT_FILE SSL_CERT_DIR REQUESTS_CA_BUNDLE CURL_CA_BUNDLE GRPC_DEFAULT_SSL_ROOTS_FILE_PATH; do [ -n "${!v:-}" ] && INFRA+=("$v=${!v}"); done
mkdir -p "$E/entrees"
H="$(sha256sum "$LANCEUR" | cut -d' ' -f1)"
USD_COURSE="$(grep -E '^USD_COURSE=' "$LANCEUR" | head -1 | sed -E 's/^USD_COURSE=([0-9.]+).*/\1/')"
SOUS_PLAFOND="$(awk -v x="$USD_COURSE" 'BEGIN { printf "%.2f", x - 0.01 }')"
ENTROPIE=12345
G_M="$("$PY" -I -c 'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[0].generate_state(1, dtype=numpy.uint64)[0]))')"
G_S="$("$PY" -I -c 'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[1].generate_state(1, dtype=numpy.uint64)[0]))')"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote (essai) : question v2 `a54da93e…` et question écrite par Gemini `8b1c7511…`, organisme v5.2.1 `fec005c6…` | au plus 120 USD | 2026-10-31 |\n' > "$E/entrees/go-sain.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote (essai) : question v2 `a54da93e…` et question écrite par Gemini `8b1c7511…`, organisme v5.2 `011d62b5…` | au plus 120 USD | 2026-10-31 |\n' > "$E/entrees/go-autre-organisme.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | second pilote (essai) : `a54da93e…` `8b1c7511…` |\n' > "$E/entrees/go-sans-calcul.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote |\n| GO-2026-10-25-01 | `a54da93e…` `8b1c7511…` `fec005c6…` |\n' > "$E/entrees/go-deux-lignes.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote, question v2 `a54da93e…` seulement, organisme `fec005c6…` |\n' > "$E/entrees/go-autre-course.md"
printf '| GO-2026-10-24-07 | 2026-10-25 | calcul | `a54da93e…` `8b1c7511…` `fec005c6…` |\n' > "$E/entrees/go-autre-id.md"
printf '| 2026-10-25 | pilote2-gemini-v5-2-1-maieutique-v1 | GO-2026-10-25-01 | 60 |\n| 2026-10-25 | pilote2-gemini-v5-2-1-structure-v1 | GO-2026-10-25-01 | 60 |\n' > "$E/entrees/dep-sain.md"
printf '| 2026-10-25 | pilote2-gemini-v5-2-1-maieutique-v1 | GO-2026-10-24-07 | 60 |\n' > "$E/entrees/dep-absente.md"
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
TDS="$E/entrees/td-sain.json $E/entrees/td-echec.json $E/entrees/td-modele.json $E/entrees/td-cout-nul.json $E/entrees/td-autre-go.json $E/entrees/td-illisible.json $E/entrees/td-jetons-nuls.json"
td_heure() {  # td_heure FICHIER MINUTES [sans-fuseau] : pièce avec une heure d'appel par espèce, vieille de MINUTES
  "$PY" -I -c '
import datetime, json, sys
h = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=float(sys.argv[2]))
s = h.replace(tzinfo=None).isoformat() if len(sys.argv) > 3 else h.isoformat().replace("+00:00", "Z")
d = {"especes": {"CLAUDE_FABLE_5_1": {"statut": "OK", "modele_servi": "claude-fable-5-1", "cout_usd": 0.00058, "jetons_sortie": 8, "heure_utc": s},
                 "CLAUDE_OPUS_5_5": {"statut": "OK", "modele_servi": "claude-opus-5-5", "cout_usd": 0.000232, "jetons_sortie": 8, "heure_utc": s},
                 "GEMINI_ARGON": {"statut": "OK", "modele_servi": "gemini-4-argon", "cout_usd": 0.00076, "jetons_sortie": 8, "heure_utc": s}}, "go": "GO-2026-10-25-01"}
json.dump(d, open(sys.argv[1], "w"))' "$@"
}
td_heure_vieille() {  # écrit la pièce avec une heure d'appel vieille de 20 minutes pour Fable (la date du fichier est récente)
  "$PY" -I -c '
import datetime, json, sys
h = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=20)).isoformat()
d = {"especes": {"CLAUDE_FABLE_5_1": {"statut": "OK", "modele_servi": "claude-fable-5-1", "cout_usd": 0.00058, "heure_utc": h},
                 "CLAUDE_OPUS_5_5": {"statut": "OK", "modele_servi": "claude-opus-5-5", "cout_usd": 0.000232},
                 "GEMINI_ARGON": {"statut": "OK", "modele_servi": "gemini-4-argon", "cout_usd": 0.00076}}, "go": "GO-2026-10-25-01"}
json.dump(d, open(sys.argv[1], "w"))' "$1"
}
pr() {  # pr FICHIER CONTENU [sans-compagnon]
  printf '%s\n' "$2" > "$1"; [ "${3:-}" = sans-compagnon ] || (cd "$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256")
}
pr "$E/entrees/prereg-sain.md" "entropie E = $ENTROPIE tirée au scellement
graine de la course maieutique = $G_M
graine de la course structure = $G_S
lanceur $H"
pr "$E/entrees/prereg-sans-compagnon.md" "entropie E = $ENTROPIE
graine de la course maieutique = $G_M
lanceur $H" sans-compagnon
pr "$E/entrees/prereg-sans-graine.md" "entropie E = $ENTROPIE
graine de la course maieutique = 14
lanceur $H"
pr "$E/entrees/prereg-graine-hors-entropie.md" "entropie E = $ENTROPIE
graine de la course maieutique = 13
lanceur $H"
pr "$E/entrees/prereg-sans-entropie.md" "graine de la course maieutique = $G_M
lanceur $H"
pr "$E/entrees/prereg-marqueur.md" "entropie E = $ENTROPIE
graine de la course maieutique = $G_M
lanceur $H ; <<EMPREINTE_PIECES>>"
pr "$E/entrees/prereg-sans-lanceur.md" "entropie E = $ENTROPIE
graine de la course maieutique = $G_M
lanceur 0000"
SHA_PR="$(cut -d' ' -f1 < "$E/entrees/prereg-sain.md.sha256")"
n=0; ok=0
cas() {  # cas NOM ATTENDU -- VAR=VAL… (motif cherché dans la sortie d'erreur et LANCEMENT.md)
  local nom="$1" attendu="$2"; shift 3
  n=$((n + 1))
  local racine="$E/cas-$nom"; rm -rf "$racine"; mkdir -p "$racine"
  # shellcheck disable=SC2086
  touch $TDS
  env -i PATH="$PATH" HOME="$E" LANG=C.UTF-8 DEPOT="$DEPOT" PYTHON="$PY" GRAINE=13 COURSE=maieutique "$@" \
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
      APPEL_CONTROLE_FICHIER="$E/entrees/td-sain.json" RECHARGE_ATTESTEE="essai")
td_heure "$E/entrees/td-heure-fraiche-M.json" 0
echo "== cas sains : M complet (essais du noyau exécutés), puis S avec M pour course précédente =="
cas sain-M "archive fermée : ferme.tar.gz" -- MODE=simulation GRAINE="$G_M" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-M.json" ESSAI_EXIGER_HEURE=1
M_SAIN="$E/cas-sain-M/pilote2-gemini-v5-2-1-maieutique-v1"
EMP_M="$(cut -d' ' -f1 < "$M_SAIN/EMPREINTES-pilote-v1.txt.sha256")"
printf '| 2026-10-25 | pilote2-gemini-v5-2-1-maieutique-v1 | GO-2026-10-25-01 | 60 |\n| 2026-10-25 | pilote2-gemini-v5-2-1-structure-v1 | GO-2026-10-25-01 | 60 | après M, empreintes de M %s |\n' "$EMP_M" > "$E/entrees/dep-sain-S.md"
td_heure "$E/entrees/td-heure-fraiche-S.json" 0
JUNIT="$E/junit-sain-v1.xml"; cp "$M_SAIN/essais-v1.xml" "$JUNIT"
RESUME_JUNIT="141 passed"
SAIN+=(ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="$RESUME_JUNIT")
cas sain-S "course M : graine $G_M = graine M du préenregistrement" -- MODE=simulation COURSE=structure GRAINE="$G_S" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" PRECEDENTE_PILOTE="$M_SAIN" "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-sain-S.md" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-S.json" ESSAI_EXIGER_HEURE=1
cas sain-S-archive "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=structure GRAINE="$G_S" PRECEDENTE_PILOTE="$M_SAIN" "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-sain-S.md" SUFFIXE_ESSAI=-bis
cas s-depense-sans-empreinte "ne porte pas l'empreinte des empreintes de M" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$M_SAIN" "${SAIN[@]}"
echo "== course S : issues de M hors de la liste saine (copie de M altérée, empreintes refaites) =="
copie_s() {  # copie_s NOM → chemin d'une copie de M
  local d="$E/m-alteree-$1"; rm -rf "$d"; cp -a "$M_SAIN" "$d"; echo "$d"
}
refaire_empreintes() {
  (cd "$1" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256 && sha256sum extrait-mecanique-v1.json > extrait-mecanique-v1.json.sha256 \
     && grep -Ev '^EMPREINTES-pilote-v1\.txt(\.sha256)?$' A-POUSSER-v1.txt | xargs sha256sum > EMPREINTES-pilote-v1.txt \
     && sha256sum EMPREINTES-pilote-v1.txt > EMPREINTES-pilote-v1.txt.sha256)
}
extrait_altere() {  # extrait_altere DOSSIER CODE_PYTHON (x = l'extrait)
  "$PY" -I -c '
import json, sys
p = sys.argv[1] + "/extrait-mecanique-v1.json"
x = json.load(open(p, encoding="utf-8"))
exec(sys.argv[2])
json.dump(x, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)' "$1" "$2"
}
cas s-sans-m "absent : S ne part qu'après M" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$E/nulle-part" "${SAIN[@]}"
d="$(copie_s empreintes)"; extrait_altere "$d" 'x["quand_utc"] = "autre"'
cas s-empreintes-alterees "empreintes de M non vérifiées" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s code)"; sed -i 's/code de retour : 0 ;/code de retour : 1 ;/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas s-code-retour "code de retour du noyau non nul" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s archive)"; sed -i 's/^- archive fermée : ferme\.tar\.gz (/- ARCHIVE FERMÉE INCOMPLÈTE : (/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas s-archive-incomplete "archive fermée absente ou incomplète" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s lanceur)"; sed -i "s/sha256 $H\$/sha256 0000/" "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas s-autre-lanceur "M n a pas tourné sous ce lanceur" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s pas-m)"; sed -i 's/^- course : maieutique ;/- course : structure ;/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas s-pas-course-m "ce n est pas la course M" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s credit)"; extrait_altere "$d" '[g.update(statut="CREDIT_EPUISE", invalide=True) for g in x["generations"] if g.get("generation") == 1]'; refaire_empreintes "$d"
cas s-credit "g001 : statut 'CREDIT_EPUISE'" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s modele)"; extrait_altere "$d" '[g.update(statut="INVALIDE_MODELE", invalide=True) for g in x["generations"] if g.get("generation") == 0]'; refaire_empreintes "$d"
cas s-invalide-modele "g000 : statut 'INVALIDE_MODELE'" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s anomalie)"; extrait_altere "$d" '[g.update(anomalie_noyau="journal des appels absent") for g in x["generations"] if g.get("generation") == 1]'; refaire_empreintes "$d"
cas s-anomalie "anomalie 'journal des appels absent'" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s une)"; extrait_altere "$d" 'x["generations"] = [g for g in x["generations"] if g.get("generation") != 1]'; refaire_empreintes "$d"
cas s-une-generation "générations de M : [0]" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s stop)"; extrait_altere "$d" '[e.update(raison="fichier STOP") for e in x["evenements"] if e.get("etape") == "arret"]'; refaire_empreintes "$d"
cas s-stop "arrêt de la course : ['fichier STOP']" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s plafond)"; extrait_altere "$d" '[e.update(raison="plafond total atteint") for e in x["evenements"] if e.get("etape") == "arret"]'; refaire_empreintes "$d"
cas s-plafond-total "arrêt de la course : ['plafond total atteint']" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s invalidees)"; extrait_altere "$d" 'x["rapport"]["generations_invalidees"] = [{"lignee": "gemini-organisme-v5-2-1", "generation": 1}]'; refaire_empreintes "$d"
cas s-invalidees "générations invalidées" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s fin)"; extrait_altere "$d" 'x["rapport"]["lignees"]["gemini-organisme-v5-2-1"]["fin"] = "sans successeur valide"'; refaire_empreintes "$d"
cas s-fin-lignee "fin de la lignée : 'sans successeur valide'" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s espace)"; sed -i 's/^- archive fermée : ferme\.tar\.gz (/- espace des organismes du manifeste (\/x) ≠ espace attendu (\/y) : ni archivé ni retiré, jamais lu — réserve\n&/' "$d/LANCEMENT.md"; printf -- '- espace des organismes du manifeste (/x) ≠ espace attendu (/y) : ni archivé ni retiré, jamais lu — réserve\n' >> "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas s-espace-autre "espace des organismes de M autre que l espace attendu" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s echec-api)"; extrait_altere "$d" '[g["appels"].update(par_statut={"OK": 10, "ECHEC_API": 113}, n=123) for g in x["generations"] if g.get("generation") == 0]'; refaire_empreintes "$d"
cas s-echec-api "g000 : 113 appels hors OK sur 123 (plus de 20 %)" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s fable-sans-ok)"; extrait_altere "$d" '[g["appels"]["par_espece"]["CLAUDE_FABLE_5_1"].update(par_statut={"ECHEC_API": g["appels"]["par_espece"]["CLAUDE_FABLE_5_1"]["n"]}) for g in x["generations"] if g.get("generation") == 1]'; refaire_empreintes "$d"
cas s-fable-sans-ok "g001 : aucun appel OK de CLAUDE_FABLE_5_1" -- MODE=simulation COURSE=structure PRECEDENTE_PILOTE="$d" "${SAIN[@]}"
d="$(copie_s graine)"; extrait_altere "$d" 'x["manifeste"]["entropie_seed_sequence"] = 13'; refaire_empreintes "$d"
cas s-graine-s-autre "qui n'est pas la graine M du préenregistrement scellé" -- MODE=simulation COURSE=structure GRAINE="$G_S" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" PRECEDENTE_PILOTE="$d" "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-sain-S.md"
echo "== course S en mode réel (copie du dépôt sous /root) : refus à l'étape (0), avant tout appel =="
REEL_S=(MODE=reel COURSE=structure PILOTE_RACINE=- DEPOT="$DEPOT_ROOT" "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai)
cas reel-s-sans-m "PRECEDENTE_PILOTE non défini" -- "${REEL_S[@]}"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
cas reel-s-m-hors-dossier "hors du dossier des pilotes" -- "${REEL_S[@]}" PRECEDENTE_PILOTE="$M_SAIN"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
mkdir -p "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"; cp -a "$M_SAIN" "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote2-gemini-v5-2-1-maieutique-v1"
cas reel-s-m-simulee "M n a pas tourné en réel" -- "${REEL_S[@]}" PRECEDENTE_PILOTE="$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote2-gemini-v5-2-1-maieutique-v1"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
echo "== refus en mode réel, avant tout appel =="
cas reel-variable-essai "variable PILOTE_RACINE définie en mode réel" -- MODE=reel
cas reel-variable-heure "variable ESSAI_EXIGER_HEURE définie en mode réel" -- MODE=reel PILOTE_RACINE=- ESSAI_EXIGER_HEURE=1
cas reel-espace "variable ESSAIM_M3_ESPACE définie en mode réel" -- MODE=reel PILOTE_RACINE=- ESSAIM_M3_ESPACE=/var/tmp/x
cas reel-variable-passerelle "variable ESSAI_PASSERELLE_PY définie en mode réel" -- MODE=reel PILOTE_RACINE=- ESSAI_PASSERELLE_PY=/x
cas reel-sans-cle "CLE_ANTHROPIC non défini" -- MODE=reel PILOTE_RACINE=- ANTHROPIC_API_KEY=factice
cas reel-cle-nom-invalide "CLE_ANTHROPIC=x;y hors des clés des runs" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC='x;y'
cas reel-cle-hors-liste "CLE_ANTHROPIC=ANTHROPIC_API_KEY hors des clés des runs" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=ANTHROPIC_API_KEY ANTHROPIC_API_KEY=factice
cas reel-cle-nommee-absente "clé Anthropic absente (variable RR_ANTHROPIC_API_KEY_3)" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3
cas reel-sans-gemini "CLE_GEMINI non défini" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_3=factice GEMINI_API_KEY=factice
cas reel-gemini-hors-liste "CLE_GEMINI=LUC_ABSENTE hors des clés des runs" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_3=factice CLE_GEMINI=LUC_ABSENTE LUC_ABSENTE=factice
cas reel-gemini-nommee-absente "clé Gemini absente (variable GEMINI_API_KEY_2)" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_3=factice CLE_GEMINI=GEMINI_API_KEY_2 GEMINI_API_KEY=factice
cas reel-sans-attestation "RECHARGE_ATTESTEE vide" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice
cas reel-sans-brave "clé Brave absente (variable BRAVE_API_KEY)" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" RECHARGE_ATTESTEE=essai
cas reel-brave-nommee-absente "clé Brave absente (variable BRAVE_ABSENTE)" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" CLE_BRAVE=BRAVE_ABSENTE BRAVE_API_KEY=factice RECHARGE_ATTESTEE=essai
cas reel-sans-openalex "clé OpenAlex absente (variable OPENALEX_API_KEY)" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice RECHARGE_ATTESTEE=essai
cas reel-openalex-nommee-absente "clé OpenAlex absente (variable OA_ABSENTE)" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice CLE_OPENALEX=OA_ABSENTE OPENALEX_API_KEY=factice RECHARGE_ATTESTEE=essai
cas reel-openalex-nom-invalide "CLE_OPENALEX doit être un nom de variable" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice CLE_OPENALEX='a b' RECHARGE_ATTESTEE=essai
cas reel-sans-s2 "clé Semantic Scholar absente (variable SEMANTIC_SCHOLAR_API_KEY)" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice RECHARGE_ATTESTEE=essai
cas reel-s2-nommee-absente "clé Semantic Scholar absente (variable S2_ABSENTE)" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice CLE_S2=S2_ABSENTE SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai
cas reel-depot-hors "hors de /root et de /home" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai
echo "== refus avant le dossier ; courses voisines =="
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
( exec -a "python3 -m essaim_m3 lancer --decalage-uid 0 --factice" sleep 60 ) & VOISIN=$!
sleep 0.3
cas voisine-decalage-des-essais "RÉSERVE : course(s) voisine(s) à un décalage des essais" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null
( exec -a "python3 -m essaim_m3 simuler --factice-sans-decalage" sleep 60 ) & VOISIN=$!
sleep 0.3
cas voisine-sans-decalage "pendant les essais d'avant départ" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null
( exec -a "python3 -m essaim_m3 lancer --decalage-uid 700 --factice" sleep 60 ) & VOISIN=$!
sleep 0.3
cas voisine-decalage-700 "à un décalage des essais du noyau (0, 700, 800)" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null
( exec -a "python3 -m pytest --factice" sleep 60 ) & VOISIN=$!
sleep 0.3
cas essais-en-cours "des essais (pytest) tournent dans le conteneur au départ" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null
echo "== R3 : verrou et marqueur de départ =="
mkdir -p "$E/racine-verrou/.verrou-pilote2-gemini-v5-2-1-maieutique-v1"
cas verrou-present "verrou $E/racine-verrou/.verrou-pilote2-gemini-v5-2-1-maieutique-v1 présent" -- MODE=simulation PILOTE_RACINE="$E/racine-verrou" "${SAIN[@]}"
mkdir -p "$E/racine-marqueur/.partis"; printf 'ailleurs\n' > "$E/racine-marqueur/.partis/pilote2-gemini-v5-2-1-maieutique-v1"
cas marqueur-present "marqueur de départ $E/racine-marqueur/.partis/pilote2-gemini-v5-2-1-maieutique-v1 présent" -- MODE=simulation PILOTE_RACINE="$E/racine-marqueur" "${SAIN[@]}"
echo "== code, commits, banque, mission, collisionneur =="
cas commit-question "absent du dépôt" -- MODE=simulation ESSAI_ARTEFACT=commit "${SAIN[@]}"
printf '# x\n' >> "$DEPOT/essaim-m3-refonte-v1/essaim_m3/noyau/question.py"
cas arbre-modifie "arbre de travail différent de b1c7f4b6" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" checkout -q -- essaim-m3-refonte-v1/essaim_m3/noyau/question.py
printf '# x\n' >> "$DEPOT/collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py"
cas collisionneur-modifie "arbre de travail différent de b1c7f4b6" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" checkout -q -- collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/tests/fichier_non_suivi.py"
cas non-suivi-essais "fichiers non suivis ou modifiés sous essaim-m3-refonte-v1" -- MODE=simulation "${SAIN[@]}"
rm -f "$DEPOT/essaim-m3-refonte-v1/tests/fichier_non_suivi.py"
printf 'x = 1\n' > "$DEPOT/essaim-m3-refonte-v1/json.py"
cas non-suivi-racine "fichiers non suivis ou modifiés sous essaim-m3-refonte-v1" -- MODE=simulation "${SAIN[@]}"
rm -f "$DEPOT/essaim-m3-refonte-v1/json.py"
printf 'x' > "$DEPOT/essaim-m3-refonte-v1/json.pyc"
cas ignore-racine "fichiers non suivis ou modifiés sous essaim-m3-refonte-v1" -- MODE=simulation "${SAIN[@]}"
rm -f "$DEPOT/essaim-m3-refonte-v1/json.pyc"
printf '# y\n' >> "$DEPOT/essaim-m3-refonte-v1/essaim_m3/noyau/question.py"
git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -am "essai : code de tête différent"
cas tete-differente "code de HEAD différent de b1c7f4b6" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/hors-pieces.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/hors-pieces.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : fichier hors des pièces"
cas commit-hors-pieces "commits postérieurs à b1c7f4b6 hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
mkdir -p "$DEPOT/essaim-m3-refonte-v1/prereg/pieces-pilote2-gemini-v5-2"; printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/prereg/pieces-pilote2-gemini-v5-2/piece-essai.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/prereg/pieces-pilote2-gemini-v5-2/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : pièce du pilote"
cas commit-pieces-permises "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
cas banque "empreinte de la banque" -- MODE=simulation ESSAI_ARTEFACT=banque "${SAIN[@]}"
cas mission "empreinte de la mission" -- MODE=simulation ESSAI_ARTEFACT=mission "${SAIN[@]}"
echo "== isolation =="
cas traversable "au lieu de « 700 0 »" -- MODE=simulation ESSAI_ARTEFACT=traversable "${SAIN[@]}"
cas cache "ne serait pas caché aux organismes" -- MODE=simulation ESSAI_ARTEFACT=cache "${SAIN[@]}"
echo "== préenregistrement =="
cas prereg-empreinte "empreinte du préenregistrement ≠ PREREG_SHA256" -- MODE=simulation GRAINE="$G_M" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256=0000 "${SAIN[@]}"
cas prereg-compagnon "compagnon .sha256 du préenregistrement absent" -- MODE=simulation GRAINE="$G_M" PREREG="$E/entrees/prereg-sans-compagnon.md" PREREG_SHA256="$(sha256sum "$E/entrees/prereg-sans-compagnon.md" | cut -d' ' -f1)" "${SAIN[@]}"
cas prereg-graine "n'est pas écrite dans le préenregistrement" -- MODE=simulation GRAINE="$G_M" PREREG="$E/entrees/prereg-sans-graine.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sans-graine.md.sha256")" "${SAIN[@]}"
cas prereg-graine-autre-course "n'est pas écrite dans le préenregistrement" -- MODE=simulation COURSE=structure GRAINE="$G_M" PRECEDENTE_PILOTE="$M_SAIN" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}"
cas prereg-graine-hors-entropie "≠ celle de SeedSequence(E).spawn(2)[0]" -- MODE=simulation GRAINE=13 PREREG="$E/entrees/prereg-graine-hors-entropie.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-graine-hors-entropie.md.sha256")" "${SAIN[@]}"
cas prereg-sans-entropie "entropie E absente" -- MODE=simulation GRAINE="$G_M" PREREG="$E/entrees/prereg-sans-entropie.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sans-entropie.md.sha256")" "${SAIN[@]}"
cas prereg-marqueur "marqueurs <<…>> restants" -- MODE=simulation GRAINE="$G_M" PREREG="$E/entrees/prereg-marqueur.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-marqueur.md.sha256")" "${SAIN[@]}"
cas prereg-lanceur "ne cite pas l'empreinte de ce lanceur" -- MODE=simulation GRAINE="$G_M" PREREG="$E/entrees/prereg-sans-lanceur.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-sans-lanceur.md.sha256")" "${SAIN[@]}"
echo "== objet et question =="
cas organisme "empreinte d'arbre de l'organisme" -- MODE=simulation ESSAI_ARTEFACT=organisme "${SAIN[@]}"
cas organisme-fichier "fichiers au lieu de 21" -- MODE=simulation ESSAI_ARTEFACT=nombre "${SAIN[@]}"
cas question "empreinte de la question" -- MODE=simulation ESSAI_ARTEFACT=question "${SAIN[@]}"
echo "== registres =="
cas go-sans-calcul "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-calcul.md"
cas go-deux-lignes "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-deux-lignes.md"
cas go-autre-course "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-course.md"
cas go-autre-id "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-id.md"
cas go-autre-organisme "GO non inscrit pour cette course sur cet objet" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-organisme.md"
cas depense-absente "lancement non consigné avant" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-absente.md"
cas reste-insuffisant "< $USD_COURSE" -- MODE=simulation "${SAIN[@]}" RESTE_GO_USD="$SOUS_PLAFOND"
echo "== test de dépense =="
cas td-vide "absent ou vide" -- MODE=simulation ESSAI_ARTEFACT=appel "${SAIN[@]}"
cas td-vieux "> 900 s" -- MODE=simulation ESSAI_ARTEFACT=appel-vieux "${SAIN[@]}"
cas td-vieillit-avant-depart "trop ancien ou non conforme au départ" -- MODE=simulation ESSAI_ARTEFACT=appel-vieillit "${SAIN[@]}"
cas td-echec "CLAUDE_FABLE_5_1 : statut 'ECHEC_API'" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-echec.json"
cas td-modele "modèle servi 'claude-fable-5-0'" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-modele.json"
cas td-cout-nul "coût 0 (un appel payant est exigé)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-cout-nul.json"
cas td-autre-go "go = 'GO-2026-10-24-07' (attendu GO-2026-10-25-01)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-autre-go.json"
cas td-jetons-nuls "jetons de sortie 0" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-jetons-nuls.json"
cas td-illisible "illisible" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-illisible.json"
td_heure_vieille "$E/entrees/td-heure-vieille.json"
cas td-heure-vieille "CLAUDE_FABLE_5_1 : appel fait il y a" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-vieille.json"
td_heure "$E/entrees/td-heure-sans-fuseau.json" 0 sans-fuseau
cas td-heure-sans-fuseau "heure_utc sans fuseau" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-sans-fuseau.json"
cas td-heure-absente-exigee "heure_utc absente (exigée en réel)" -- MODE=simulation "${SAIN[@]}" ESSAI_EXIGER_HEURE=1
cas td-modifie-avant-depart "a changé depuis sa première lecture" -- MODE=simulation ESSAI_ARTEFACT=appel-modifie "${SAIN[@]}"
echo "== essais =="
cas junit-echec "échecs" -- MODE=simulation ESSAI_ARTEFACT=junit-echec "${SAIN[@]}"
cas junit-saut "sauts (aucun permis)" -- MODE=simulation ESSAI_ARTEFACT=junit-saut "${SAIN[@]}"
cas junit-total "essais au lieu de 141" -- MODE=simulation ESSAI_ARTEFACT=junit-total "${SAIN[@]}"
# depuis 5d1d4fd, `boucle.empreinte_arbre` (donc le `sha256_code_noyau` du manifeste) écarte le bytecode : traité
cas bytecode "noyau sans bytecode : empreinte 37acdcaaaded746b7f7599f17e8149bdd773e372f3a3b0782db7b73882acf8a3" -- MODE=simulation ESSAI_ARTEFACT=bytecode "${SAIN[@]}"
find "$DEPOT/essaim-m3-refonte-v1/essaim_m3" -name __pycache__ -prune -exec rm -rf {} +
echo "== environnement du noyau (noms consignés ; infrastructure réseau passée, tout autre nom retiré) =="
cas env-noyau-nu "environnement du noyau (noms seulement, valeurs jamais écrites) : PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER ." -- MODE=simulation "${SAIN[@]}" HF_TOKEN=factice VAST_API_KEY=factice ANTHROPIC_API_KEY=factice
cas env-noyau-infra "environnement du noyau (noms seulement, valeurs jamais écrites) : PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER HTTPS_PROXY no_proxy SSL_CERT_FILE REQUESTS_CA_BUNDLE ." -- MODE=simulation "${SAIN[@]}" HTTPS_PROXY=http://127.0.0.1:9 no_proxy=localhost SSL_CERT_FILE=/etc/ssl/cert.pem REQUESTS_CA_BUNDLE=/etc/ssl/cert.pem HF_TOKEN=factice OSF_TOKEN=factice BRAVE_API_KEY=factice
echo "== passerelle de sortie sous l'environnement du noyau (P52C1-04) =="
cas passerelle-saine "passerelle de sortie, sous l'environnement du noyau sans clé : httpx" -- MODE=simulation "${SAIN[@]}" ESSAI_PASSERELLE_PY="$PY_HTTPX" "${INFRA[@]}"
cas passerelle-sans-certificat "passerelle de sortie injoignable sous l'environnement du noyau : httpx, api.anthropic.com : ConnectError" -- MODE=simulation "${SAIN[@]}" ESSAI_PASSERELLE_PY="$PY_HTTPX"
echo "== noms des variables du test de dépense (P52C1-05) =="
td_noms() {  # td_noms FICHIER ANTHROPIC GEMINI : pièce fraîche avec heures d'appel et noms des variables
  "$PY" -I -c '
import datetime, json, sys
h = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
e = {k: {"statut": "OK", "modele_servi": m, "cout_usd": 0.0005, "jetons_sortie": 8, "heure_utc": h} for k, m in (("CLAUDE_FABLE_5_1", "claude-fable-5-1"), ("CLAUDE_OPUS_5_5", "claude-opus-5-5"), ("GEMINI_ARGON", "gemini-4-argon"))}
json.dump({"especes": e, "go": "GO-2026-10-25-01", "variables_cles": {"anthropic": sys.argv[2], "gemini": sys.argv[3]}}, open(sys.argv[1], "w"))' "$@"
}
td_noms "$E/entrees/td-noms-autres.json" RR_ANTHROPIC_API_KEY GEMINI_API_KEY
cas td-noms-autres "noms des variables du test : anthropic = 'RR_ANTHROPIC_API_KEY' (attendu RR_ANTHROPIC_API_KEY_3)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-autres.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2
td_noms "$E/entrees/td-noms-conformes.json" RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2
cas td-noms-conformes "noms des variables du test : anthropic RR_ANTHROPIC_API_KEY_3, gemini GEMINI_API_KEY_2" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-conformes.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2
cas td-noms-absents "noms des variables du test : absents de la pièce (réserve, P52C1-05)" -- MODE=simulation "${SAIN[@]}"
echo "== après le départ =="
cas famille-puis-tentatives "aucune course partie (pas de manifeste" -- MODE=simulation ESSAI_ARTEFACT=famille "${SAIN[@]}"
R_F="$E/cas-famille-puis-tentatives"
cas tentative-2 "archive fermée : ferme.tar.gz" -- MODE=simulation TENTATIVE=2 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas tentative-3 "R3 : jamais de seconde course" -- MODE=simulation TENTATIVE=3 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas archive-incomplete "ARCHIVE FERMÉE INCOMPLÈTE" -- MODE=simulation ESSAI_ARTEFACT=archive "${SAIN[@]}"
cas espace-autre "≠ espace attendu" -- MODE=simulation ESSAI_ARTEFACT=espace "${SAIN[@]}"
cas imprevu "fichiers imprévus, NON poussés" -- MODE=simulation ESSAI_ARTEFACT=imprevu "${SAIN[@]}"
echo "== état du dépôt d'essai après la série =="
git -C "$DEPOT" status --porcelain --ignored | grep -v __pycache__ | head -5
git -C "$DEPOT" log --oneline -1 | cut -c1-12
echo "== bilan : $ok sur $n cas conformes =="
