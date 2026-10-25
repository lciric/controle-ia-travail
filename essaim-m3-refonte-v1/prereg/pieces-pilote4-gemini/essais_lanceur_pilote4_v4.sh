#!/usr/bin/env bash
# Essais du lanceur du pilote 4 (v5.3 puis v6.1, banque v3, quatre générations notées, 6 rondes de conception au
# plus), v4, dérivés de la batterie v3 du pilote 3 (`essais_lanceur_pilote3_v5_3_v6_v3.sh`, 14bc0535…, 122 cas sur 122
# sur le lanceur v2) par `deriver_essais_pilote4_v4.py` (remplacements exacts, configuration du lanceur ; la v1 laissait le chemin du
# cas sain de la v6.x à l’ancienne étiquette). Cette série
# essaie (i) les deux courses saines de bout en bout en simulation (v5.3, essais du noyau exécutés ; puis v6.1 après la
# v5.3 saine), avec les rondes de conception et les quatre générations, et relève ce que montrent les rondes ; (ii) la
# course M de référence, produite par le lanceur scellé du second pilote lui-même, puis chaque issue de M hors de la
# liste close ; (iii) la porte « v5.3 précédente » (générations 0 à 3) et ses artefacts ; (iv) ce qui change (objets,
# graines, banque v3 et les chemins permis des banques v2 et v3, ligne de GO liée au texte scellé, journaux recopiés et poussés) ; (v) un
# échantillon des gardes communes, en simulation et en mode réel (refus avant tout appel). Aucun appel réel.
# Usage : bash essais_lanceur_pilote4_v4.sh LANCEUR LANCEUR_M DEPOT DEPOT_M PYTHON DOSSIER_ESSAIS DEPOT_SOUS_ROOT PYTHON_AVEC_HTTPX
# (DEPOT : copie à la tête du pilote 4 ; DEPOT_M : copie à la tête du second pilote, d'où part la M de référence ;
# DEPOT_SOUS_ROOT : copie à la tête du pilote 4 sous /root, pour les refus du mode réel)
set -uo pipefail
LANCEUR="$1"; LANCEUR_M="$2"; DEPOT="$3"; DEPOT_M="$4"; PY="$5"; E="$6"; DEPOT_ROOT="$7"; PY_HTTPX="$8"
CLES_REEL=(CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_3=factice CLE_GEMINI=GEMINI_API_KEY_2 GEMINI_API_KEY_2=factice)
INFRA=(); for v in HTTPS_PROXY https_proxy HTTP_PROXY http_proxy NO_PROXY no_proxy SSL_CERT_FILE SSL_CERT_DIR REQUESTS_CA_BUNDLE CURL_CA_BUNDLE GRPC_DEFAULT_SSL_ROOTS_FILE_PATH; do [ -n "${!v:-}" ] && INFRA+=("$v=${!v}"); done
mkdir -p "$E/entrees"
H="$(sha256sum "$LANCEUR" | cut -d' ' -f1)"
H_M="$(sha256sum "$LANCEUR_M" | cut -d' ' -f1)"
[ "$H_M" = 83f8b9cf8f3062dfc5e2c02094c602a2d582adf0cbcef292d5bdccd8f8d61b1b ] || { echo "lanceur du second pilote inattendu : $H_M"; exit 1; }
USD_COURSE="$(grep -E '^USD_COURSE=' "$LANCEUR" | head -1 | sed -E 's/^USD_COURSE=([0-9.]+).*/\1/')"
SOUS_PLAFOND="$(awk -v x="$USD_COURSE" 'BEGIN { printf "%.2f", x - 0.01 }')"
ENTROPIE=12345
G_53="$("$PY" -I -c 'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[0].generate_state(1, dtype=numpy.uint64)[0]))')"
G_6="$("$PY" -I -c 'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[1].generate_state(1, dtype=numpy.uint64)[0]))')"
GRAINE_M_SCELLEE=3970427751169333427
SHA_PREREG_M=d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b
TEXTE_M_REL=essaim-m3-refonte-v1/prereg/pilote2-gemini-organisme-v5-2-v2.md
for d in "$DEPOT" "$DEPOT_M" "$DEPOT_ROOT"; do
  [ "$(sha256sum "$d/$TEXTE_M_REL" | cut -d' ' -f1)" = "$SHA_PREREG_M" ] || { echo "texte scellé du second pilote inattendu dans $d"; exit 1; }
done
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | second pilote (essai) : question M `8b1c7511…`, question S `a54da93e…`, organisme v5.2.1 `fec005c6…` | au plus 120 USD | 2026-10-31 |\n' > "$E/entrees/go-m.md"
printf '| 2026-10-25 | pilote2-gemini-v5-2-1-maieutique-v1 | GO-2026-10-25-01 | 60 |\n' > "$E/entrees/dep-m.md"
td() {  # td FICHIER STATUT_FABLE MODELE_FABLE COUT_FABLE GO
  printf '{"especes": {"CLAUDE_FABLE_5_1": {"statut": "%s", "modele_servi": "%s", "cout_usd": %s}, "CLAUDE_OPUS_5_5": {"statut": "OK", "modele_servi": "claude-opus-5-5", "cout_usd": 0.000232}, "GEMINI_ARGON": {"statut": "OK", "modele_servi": "gemini-4-argon", "cout_usd": 0.00076}}, "go": "%s"}\n' "$2" "$3" "$4" "$5" > "$1"
}
td "$E/entrees/td-sain.json" OK claude-fable-5-1 0.00058 GO-2026-10-25-02
td "$E/entrees/td-echec.json" ECHEC_API None 0 GO-2026-10-25-02
td "$E/entrees/td-autre-go.json" OK claude-fable-5-1 0.00058 GO-2026-10-25-01
TDS="$E/entrees/td-sain.json $E/entrees/td-echec.json $E/entrees/td-autre-go.json"
td_heure() {  # td_heure FICHIER MINUTES GO : pièce avec une heure d'appel par espèce, vieille de MINUTES
  "$PY" -I -c '
import datetime, json, sys
h = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=float(sys.argv[2]))).isoformat().replace("+00:00", "Z")
d = {"especes": {"CLAUDE_FABLE_5_1": {"statut": "OK", "modele_servi": "claude-fable-5-1", "cout_usd": 0.00058, "jetons_sortie": 8, "heure_utc": h},
                 "CLAUDE_OPUS_5_5": {"statut": "OK", "modele_servi": "claude-opus-5-5", "cout_usd": 0.000232, "jetons_sortie": 8, "heure_utc": h},
                 "GEMINI_ARGON": {"statut": "OK", "modele_servi": "gemini-4-argon", "cout_usd": 0.00076, "jetons_sortie": 8, "heure_utc": h}}, "go": sys.argv[3]}
json.dump(d, open(sys.argv[1], "w"))' "$@"
}
td_noms() {  # td_noms FICHIER ANTHROPIC GEMINI : pièce fraîche avec heures d'appel et noms des variables (GO-2026-10-25-02)
  "$PY" -I -c '
import datetime, json, sys
h = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
e = {k: {"statut": "OK", "modele_servi": m, "cout_usd": 0.0005, "jetons_sortie": 8, "heure_utc": h} for k, m in (("CLAUDE_FABLE_5_1", "claude-fable-5-1"), ("CLAUDE_OPUS_5_5", "claude-opus-5-5"), ("GEMINI_ARGON", "gemini-4-argon"))}
json.dump({"especes": e, "go": "GO-2026-10-25-02", "variables_cles": {"anthropic": sys.argv[2], "gemini": sys.argv[3]}}, open(sys.argv[1], "w"))' "$@"
}
pr() {  # pr FICHIER CONTENU [sans-compagnon]
  printf '%s\n' "$2" > "$1"; [ "${3:-}" = sans-compagnon ] || (cd "$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256")
}
pr "$E/entrees/prereg-sain.md" "entropie E = $ENTROPIE tirée au scellement
graine de la course v5-3 = $G_53
graine de la course v6-1 = $G_6
lanceur $H"
pr "$E/entrees/prereg-graine-hors-entropie.md" "entropie E = $ENTROPIE
graine de la course v5-3 = 13
graine de la course v6-1 = 13
lanceur $H"
pr "$E/entrees/prereg-lanceur-source.md" "entropie E = $ENTROPIE
graine de la course v5-3 = $G_53
graine de la course v6-1 = $G_6
lanceur $H_M"
pr "$E/entrees/prereg-marqueur.md" "entropie E = $ENTROPIE
graine de la course v5-3 = $G_53
graine de la course v6-1 = $G_6
lanceur $H ; <<EMPREINTE_PIECES>>"
SHA_PR="$(cut -d' ' -f1 < "$E/entrees/prereg-sain.md.sha256")"
T16="${SHA_PR:0:16}"   # pilote 4 : la ligne de GO porte les 16 premiers caractères de l'empreinte du texte scellé
printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `8b1c7511…`, organismes v5.3 `6251ab21…` et v6.1 `ae331d1d…` ; texte %s | au plus 120 USD | 2026-10-31 |\n' "$T16" > "$E/entrees/go-sain.md"
printf '| GO-2026-10-25-02 | 2026-10-25 | pilote 4 (essai) : `8b1c7511…` `6251ab21…` `ae331d1d…` ; texte %s |\n' "$T16" > "$E/entrees/go-sans-calcul.md"
printf '| GO-2026-10-25-01 | 2026-10-25 | calcul | `8b1c7511…` `6251ab21…` `ae331d1d…` ; texte %s |\n' "$T16" > "$E/entrees/go-autre-id.md"
printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `8b1c7511…`, organisme v5.3 `6251ab21…` seulement ; texte %s |\n' "$T16" > "$E/entrees/go-v53-seulement.md"
printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `a54da93e…`, organismes `6251ab21…` `ae331d1d…` ; texte %s |\n' "$T16" > "$E/entrees/go-autre-question.md"
printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `8b1c7511…`, organismes v5.3 `6251ab21…` et v6.1 `ae331d1d…` (sans le texte) |\n' > "$E/entrees/go-sans-texte.md"
n=0; ok=0
verifier() {  # verifier NOM ATTENDU FICHIER… : le motif doit se trouver dans l'un des fichiers
  local nom="$1" attendu="$2"; shift 2
  n=$((n + 1))
  if cat "$@" 2>/dev/null | grep -qF -- "$attendu"; then ok=$((ok + 1)); echo "OK     $nom : « $attendu »"
  else echo "ÉCHEC  $nom : attendu « $attendu »"; fi
}
cas() {  # cas NOM ATTENDU -- VAR=VAL… (motif cherché dans la sortie d'erreur et LANCEMENT.md)
  local nom="$1" attendu="$2"; shift 3
  n=$((n + 1))
  local racine="$E/cas-$nom"; rm -rf "$racine"; mkdir -p "$racine"
  # shellcheck disable=SC2086
  touch $TDS
  env -i PATH="$PATH" HOME="$E" LANG=C.UTF-8 DEPOT="$DEPOT" PYTHON="$PY" GRAINE=13 COURSE=v5-3 "$@" \
    PILOTE_RACINE_DEFAUT="$racine" bash -c 'export PILOTE_RACINE="${PILOTE_RACINE-$PILOTE_RACINE_DEFAUT}"; [ "$PILOTE_RACINE" = "-" ] && unset PILOTE_RACINE; exec bash "$0"' "$LANCEUR" \
    > "$racine/sortie.txt" 2> "$racine/erreur.txt"
  local code=$?
  local autre_racine="" a
  for a in "$@"; do case "$a" in PILOTE_RACINE=-) ;; PILOTE_RACINE=*) autre_racine="${a#PILOTE_RACINE=}";; esac; done
  local journal; journal="$(cat "$racine"/*/LANCEMENT.md 2>/dev/null; [ -n "$autre_racine" ] && cat "$autre_racine"/*/LANCEMENT.md 2>/dev/null; cat "$racine/erreur.txt")"
  if echo "$journal" | grep -qF -- "$attendu"; then ok=$((ok + 1)); echo "OK     $nom (code $code) : « $attendu »"
  else echo "ÉCHEC  $nom (code $code) : attendu « $attendu » ; erreur : $(tail -2 "$racine/erreur.txt" | tr '\n' ' ')"; fi
}

echo "== course M de référence : lanceur scellé du second pilote, en simulation, texte et graine scellés (copie du second pilote) =="
td_heure "$E/entrees/td-m.json" 0 GO-2026-10-25-01
RM="$E/m-reference"; rm -rf "$RM"; mkdir -p "$RM"
env -i PATH="$PATH" HOME="$E" LANG=C.UTF-8 DEPOT="$DEPOT_M" PYTHON="$PY" MODE=simulation COURSE=maieutique GRAINE="$GRAINE_M_SCELLEE" \
  PREREG="$DEPOT_M/$TEXTE_M_REL" PREREG_SHA256="$SHA_PREREG_M" REGISTRE_GO_SOURCE="$E/entrees/go-m.md" DEPENSES_SOURCE="$E/entrees/dep-m.md" \
  RESTE_GO_USD=150 APPEL_CONTROLE_FICHIER="$E/entrees/td-m.json" RECHARGE_ATTESTEE=essai ESSAI_EXIGER_HEURE=1 PILOTE_RACINE="$RM" \
  bash "$LANCEUR_M" > "$RM/sortie.txt" 2> "$RM/erreur.txt"
M_REF="$RM/pilote2-gemini-v5-2-1-maieutique-v1"
verifier m-reference-saine "archive fermée : ferme.tar.gz" "$M_REF/LANCEMENT.md"
verifier m-reference-lanceur-scelle "lanceur : lancer_pilote2_gemini_v5_2_v5.sh, sha256 $H_M" "$M_REF/LANCEMENT.md"
verifier m-reference-graine-scellee "graine $GRAINE_M_SCELLEE de la course maieutique écrite et recalculée" "$M_REF/LANCEMENT.md"
EMP_M="$(cut -d' ' -f1 < "$M_REF/EMPREINTES-pilote-v1.txt.sha256")"
printf '| 2026-10-25 | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\n| 2026-10-25 | pilote4-gemini-v6-1-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\n' "$EMP_M" "$EMP_M" > "$E/entrees/dep-sain.md"
printf '| 2026-10-25 | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 60 |\n| 2026-10-25 | pilote4-gemini-v6-1-v1 | GO-2026-10-25-02 | 60 |\n' > "$E/entrees/dep-sans-empreinte-m.md"
printf '| 2026-10-25 | pilote4-gemini-v5-3-v1 | GO-2026-10-25-01 | 60 | %s |\n' "$EMP_M" > "$E/entrees/dep-absente.md"
SAIN=(REGISTRE_GO_SOURCE="$E/entrees/go-sain.md" DEPENSES_SOURCE="$E/entrees/dep-sain.md" RESTE_GO_USD=150
      APPEL_CONTROLE_FICHIER="$E/entrees/td-sain.json" RECHARGE_ATTESTEE="essai" REFERENCE_M="$M_REF")

echo "== cas sains : v5.3 complète (essais du noyau exécutés), puis v6.1 ; rondes de conception et quatre générations =="
td_heure "$E/entrees/td-heure-fraiche-v53.json" 0 GO-2026-10-25-02
cas sain-v5-3 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v5-3 GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-v53.json" ESSAI_EXIGER_HEURE=1
V53="$E/cas-sain-v5-3/pilote4-gemini-v5-3-v1"
verifier sain-v5-3-reference-m "; M saine : g000 et g001 OK" "$V53/LANCEMENT.md"
verifier sain-v5-3-graine-m "graine $GRAINE_M_SCELLEE = graine M du texte scellé du second pilote (d2944654…)" "$V53/LANCEMENT.md"
verifier sain-v5-3-organisme "organisme : 22 fichiers, empreinte d'arbre 6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753" "$V53/LANCEMENT.md"
verifier sain-v5-3-essais "essais : 141 passés, 0 sauté, 0 désélectionnés" "$V53/LANCEMENT.md"
verifier sain-v5-3-registre "registre : une ligne GO-2026-10-25-02 de type calcul" "$V53/LANCEMENT.md"
JUNIT="$E/junit-sain-v1.xml"; cp "$V53/essais-v1.xml" "$JUNIT"
SAIN+=(ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="141 passed")
EMP_V53="$(cut -d' ' -f1 < "$V53/EMPREINTES-pilote-v1.txt.sha256")"
printf '| 2026-10-25 | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\n| 2026-10-25 | pilote4-gemini-v6-1-v1 | GO-2026-10-25-02 | 60 | après M et v5.3, empreintes de M %s, de v5.3 %s |\n' "$EMP_M" "$EMP_M" "$EMP_V53" > "$E/entrees/dep-sain.md"
printf '| 2026-10-25 | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\n| 2026-10-25 | pilote4-gemini-v6-1-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |\n' "$EMP_M" "$EMP_M" > "$E/entrees/dep-v6-sans-empreinte-v53.md"
td_heure "$E/entrees/td-heure-fraiche-v6.json" 0 GO-2026-10-25-02
cas sain-v6-1 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-1 GRAINE="$G_6" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-v6.json" ESSAI_EXIGER_HEURE=1 PRECEDENTE_V53="$V53"
V6="$E/cas-sain-v6-1/pilote4-gemini-v6-1-v1"
verifier sain-v6-1-precedente-v53 "; v5.3 saine : g000 à g003 OK" "$V6/LANCEMENT.md"
verifier sain-v6-1-graine-v53 "graine $G_53 = graine v5-3 du préenregistrement" "$V6/LANCEMENT.md"
verifier sain-v6-1-reference-m "; M saine : g000 et g001 OK" "$V6/LANCEMENT.md"
verifier sain-v6-1-organisme "organisme : 24 fichiers, empreinte d'arbre ae331d1deb660a20da919edbdcdecba28e49b9b143a6b7a061262101a79798d4" "$V6/LANCEMENT.md"
verifier sain-v6-1-graine "graine $G_6 de la course v6-1 écrite et recalculée" "$V6/LANCEMENT.md"
for d in "$V53" "$V6"; do
  for g in g000 g001 g002 g003 c001; do
    verifier "sain-journal-$g-$(basename "$d")" "journal des appels $g : journal-appels-$g.jsonl" "$d/LANCEMENT.md"
    verifier "sain-pousse-$g-$(basename "$d")" "journal-appels-$g.jsonl" "$d/A-POUSSER-v1.txt"
  done
done
echo "== relevé des rondes de conception et des générations en simulation (non compté) =="
for d in "$V53" "$V6"; do
  "$PY" -I -c '
import json, pathlib, sys
d = pathlib.Path(sys.argv[1]); x = json.load(open(d / "extrait-mecanique-v1.json", encoding="utf-8"))
r = x.get("rapport") or {}
print("RELEVÉ " + d.name + " : rondes_conception " + json.dumps(r.get("rondes_conception"), ensure_ascii=False) + " ; lignées " + json.dumps({k: {c: v.get(c) for c in ("fin", "conception_finie", "generation")} for k, v in (r.get("lignees") or {}).items()}, ensure_ascii=False))
for g in x.get("generations", []):
    a = g.get("appels") or {}
    print("RELEVÉ " + d.name + " : " + ("c%03d" % g["generation"] if g.get("phase") else "g%03d" % g["generation"]) + " statut " + str(g.get("statut")) + " ; appels " + json.dumps(a.get("par_statut"), sort_keys=True) + " ; successeur " + json.dumps(g.get("successeur"), ensure_ascii=False)[:80] + " ; problèmes du successeur " + json.dumps(g.get("problemes_successeur"), ensure_ascii=False)[:160])
arr = [(e.get("etape"), e.get("raison")) for e in x.get("evenements", []) if str(e.get("etape", "")).startswith("arret")]
print("RELEVÉ " + d.name + " : arrêts " + json.dumps(arr, ensure_ascii=False))
for j in sorted(d.glob("journal-appels-*.jsonl")):
    roles = {}
    for l in open(j, encoding="utf-8"):
        try: e = json.loads(l)
        except Exception: continue
        roles[e.get("role")] = roles.get(e.get("role"), 0) + 1
    print("RELEVÉ " + d.name + " : " + j.name + " : " + str(sum(roles.values())) + " appels ; rôle architecte_mutation_endogene : " + str(roles.get("architecte_mutation_endogene", 0)) + " ; rôles " + json.dumps(roles, ensure_ascii=False, sort_keys=True)[:300])
' "$d"
done
cas sain-simulation-sans-reference "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-1 REGISTRE_GO_SOURCE="$E/entrees/go-sain.md" DEPENSES_SOURCE="$E/entrees/dep-sans-empreinte-m.md" RESTE_GO_USD=150 APPEL_CONTROLE_FICHIER="$E/entrees/td-sain.json" RECHARGE_ATTESTEE=essai ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="141 passed"
cas go-v53-seulement-autorise-v53 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v5-3 "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-v53-seulement.md"

echo "== course M de référence : issues hors de la liste saine (copie de M altérée, empreintes refaites) =="
copie_m() {  # copie_m NOM → chemin d'une copie de M
  local d="$E/m-alteree-$1/pilote2-gemini-v5-2-1-maieutique-v1"; rm -rf "$E/m-alteree-$1"; mkdir -p "$E/m-alteree-$1"; cp -a "$M_REF" "$d"; echo "$d"
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
cas m-absente "absent : une course du pilote 4 ne part qu'après M" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$E/nulle-part"
d="$(copie_m sans-empreintes)"; rm -f "$d/EMPREINTES-pilote-v1.txt.sha256"
cas m-sans-empreintes "empreintes de M absentes" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m empreintes)"; extrait_altere "$d" 'x["quand_utc"] = "autre"'
cas m-empreintes-alterees "empreintes de M non vérifiées" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m code)"; sed -i 's/code de retour : 0 ;/code de retour : 1 ;/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas m-code-retour "code de retour du noyau non nul" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m archive)"; sed -i 's/^- archive fermée : ferme\.tar\.gz (/- ARCHIVE FERMÉE INCOMPLÈTE : (/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas m-archive-incomplete "archive fermée absente ou incomplète" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m lanceur)"; sed -i "s/sha256 $H_M\$/sha256 0000/" "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas m-autre-lanceur "M n a pas tourné sous ce lanceur" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m lanceur-pilote3)"; sed -i "s/lanceur : lancer_pilote2_gemini_v5_2_v5.sh, sha256 $H_M\$/lanceur : lancer_pilote4_gemini_v3.sh, sha256 $H/" "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas m-sous-lanceur-pilote4 "M n a pas tourné sous ce lanceur" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m pas-m)"; sed -i 's/^- course : maieutique ;/- course : structure ;/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas m-pas-course-m "ce n est pas la course M" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m credit)"; extrait_altere "$d" '[g.update(statut="CREDIT_EPUISE", invalide=True) for g in x["generations"] if g.get("generation") == 1 and not g.get("phase")]'; refaire_empreintes "$d"
cas m-credit "g001 : statut 'CREDIT_EPUISE'" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m modele)"; extrait_altere "$d" '[g.update(statut="INVALIDE_MODELE", invalide=True) for g in x["generations"] if g.get("generation") == 0 and not g.get("phase")]'; refaire_empreintes "$d"
cas m-invalide-modele "g000 : statut 'INVALIDE_MODELE'" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m anomalie)"; extrait_altere "$d" '[g.update(anomalie_noyau="journal des appels absent") for g in x["generations"] if g.get("generation") == 1 and not g.get("phase")]'; refaire_empreintes "$d"
cas m-anomalie "anomalie 'journal des appels absent'" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m une)"; extrait_altere "$d" 'x["generations"] = [g for g in x["generations"] if g.get("generation") != 1 or g.get("phase")]'; refaire_empreintes "$d"
cas m-une-generation "générations de M : [0]" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m stop)"; extrait_altere "$d" '[e.update(raison="fichier STOP") for e in x["evenements"] if e.get("etape") == "arret"]'; refaire_empreintes "$d"
cas m-stop "arrêt de la course : ['fichier STOP']" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m plafond)"; extrait_altere "$d" '[e.update(raison="plafond total atteint") for e in x["evenements"] if e.get("etape") == "arret"]'; refaire_empreintes "$d"
cas m-plafond-total "arrêt de la course : ['plafond total atteint']" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m invalidees)"; extrait_altere "$d" 'x["rapport"]["generations_invalidees"] = [{"lignee": "gemini-organisme-v5-2-1", "generation": 1}]'; refaire_empreintes "$d"
cas m-invalidees "générations invalidées" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m fin)"; extrait_altere "$d" 'x["rapport"]["lignees"]["gemini-organisme-v5-2-1"]["fin"] = "sans successeur valide"'; refaire_empreintes "$d"
cas m-fin-lignee "fin de la lignée : 'sans successeur valide'" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m espace)"; printf -- '- espace des organismes du manifeste (/x) ≠ espace attendu (/y) : ni archivé ni retiré, jamais lu — réserve\n' >> "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas m-espace-autre "espace des organismes de M autre que l espace attendu" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m echec-api)"; extrait_altere "$d" '[g["appels"].update(par_statut={"OK": 10, "ECHEC_API": 113}, n=123) for g in x["generations"] if g.get("generation") == 0 and not g.get("phase")]'; refaire_empreintes "$d"
cas m-echec-api "g000 : 113 appels hors OK sur 123 (plus de 20 %)" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m fable-sans-ok)"; extrait_altere "$d" '[g["appels"]["par_espece"]["CLAUDE_FABLE_5_1"].update(par_statut={"ECHEC_API": g["appels"]["par_espece"]["CLAUDE_FABLE_5_1"]["n"]}) for g in x["generations"] if g.get("generation") == 1 and not g.get("phase")]'; refaire_empreintes "$d"
cas m-fable-sans-ok "g001 : aucun appel OK de CLAUDE_FABLE_5_1" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
d="$(copie_m graine)"; extrait_altere "$d" 'x["manifeste"]["entropie_seed_sequence"] = 13'; refaire_empreintes "$d"
cas m-graine-autre "qui n'est pas la graine M du texte scellé du second pilote" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"
printf ' ' >> "$DEPOT/$TEXTE_M_REL"
cas m-texte-second-pilote-modifie "texte scellé du second pilote absent ou d'empreinte autre que d2944654…" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" checkout -q -- "$TEXTE_M_REL"
cas m-depense-sans-empreinte "ne porte pas l'empreinte des empreintes de M" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-sans-empreinte-m.md"

echo "== course v6.1 : issues de v5.3 hors de la liste saine (copie de v5.3 altérée, empreintes refaites) =="
copie_v53() {  # copie_v53 NOM → chemin d'une copie de v5.3
  local d="$E/v53-alteree-$1/pilote4-gemini-v5-3-v1"; rm -rf "$E/v53-alteree-$1"; mkdir -p "$E/v53-alteree-$1"; cp -a "$V53" "$d"; echo "$d"
}
V6C=(MODE=simulation COURSE=v6-1 "${SAIN[@]}")
cas v53-absente "PRECEDENTE_V53 $E/nulle-part absent : v6.1 ne part qu'après v5.3" -- "${V6C[@]}" PRECEDENTE_V53="$E/nulle-part"
d="$(copie_v53 sans-empreintes)"; rm -f "$d/EMPREINTES-pilote-v1.txt.sha256"
cas v53-sans-empreintes "empreintes de v5.3 absentes" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 empreintes)"; extrait_altere "$d" 'x["quand_utc"] = "autre"'
cas v53-empreintes-alterees "empreintes de v5.3 non vérifiées" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 code)"; sed -i 's/code de retour : 0 ;/code de retour : 1 ;/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas v53-code-retour "code de retour du noyau non nul" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 archive)"; sed -i 's/^- archive fermée : ferme\.tar\.gz (/- ARCHIVE FERMÉE INCOMPLÈTE : (/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas v53-archive-incomplete "archive fermée absente ou incomplète" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 lanceur)"; sed -i "s/sha256 $H\$/sha256 0000/" "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas v53-autre-lanceur "v5.3 n a pas tourné sous ce lanceur" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 pas-v53)"; sed -i 's/^- course : v5-3 ;/- course : v6-1 ;/' "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas v53-pas-course-v53 "ce n est pas la course v5.3" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 credit)"; extrait_altere "$d" '[g.update(statut="CREDIT_EPUISE", invalide=True) for g in x["generations"] if g.get("generation") == 1 and not g.get("phase")]'; refaire_empreintes "$d"
cas v53-credit "g001 : statut 'CREDIT_EPUISE'" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 modele)"; extrait_altere "$d" '[g.update(statut="INVALIDE_MODELE", invalide=True) for g in x["generations"] if g.get("generation") == 0 and not g.get("phase")]'; refaire_empreintes "$d"
cas v53-invalide-modele "g000 : statut 'INVALIDE_MODELE'" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 anomalie)"; extrait_altere "$d" '[g.update(anomalie_noyau="journal des appels absent") for g in x["generations"] if g.get("generation") == 1 and not g.get("phase")]'; refaire_empreintes "$d"
cas v53-anomalie "anomalie 'journal des appels absent'" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 une)"; extrait_altere "$d" 'x["generations"] = [g for g in x["generations"] if g.get("generation") != 1 or g.get("phase")]'; refaire_empreintes "$d"
cas v53-une-generation "générations de v5.3 : [0, 2, 3] au lieu de [0, 1, 2, 3]" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 deux)"; extrait_altere "$d" 'x["generations"] = [g for g in x["generations"] if g.get("phase") or g.get("generation") in (0, 1)]'; refaire_empreintes "$d"
cas v53-deux-generations "générations de v5.3 : [0, 1] au lieu de [0, 1, 2, 3]" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 stop)"; extrait_altere "$d" '[e.update(raison="fichier STOP") for e in x["evenements"] if e.get("etape") == "arret"]'; refaire_empreintes "$d"
cas v53-stop "arrêt de la course : ['fichier STOP']" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 plafond)"; extrait_altere "$d" '[e.update(raison="plafond total atteint") for e in x["evenements"] if e.get("etape") == "arret"]'; refaire_empreintes "$d"
cas v53-plafond-total "arrêt de la course : ['plafond total atteint']" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 invalidees)"; extrait_altere "$d" 'x["rapport"]["generations_invalidees"] = [{"lignee": "gemini-organisme-v5-3", "generation": 1}]'; refaire_empreintes "$d"
cas v53-invalidees "générations invalidées" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 fin)"; extrait_altere "$d" 'x["rapport"]["lignees"]["gemini-organisme-v5-3"]["fin"] = "sans successeur valide"'; refaire_empreintes "$d"
cas v53-fin-lignee "fin de la lignée : 'sans successeur valide'" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 espace)"; printf -- '- espace des organismes du manifeste (/x) ≠ espace attendu (/y) : ni archivé ni retiré, jamais lu — réserve\n' >> "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas v53-espace-autre "espace des organismes de v5.3 autre que l espace attendu" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 echec-api)"; extrait_altere "$d" '[g["appels"].update(par_statut={"OK": 10, "ECHEC_API": 113}, n=123) for g in x["generations"] if g.get("generation") == 0 and not g.get("phase")]'; refaire_empreintes "$d"
cas v53-echec-api "g000 : 113 appels hors OK sur 123 (plus de 20 %)" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 fable-sans-ok)"; extrait_altere "$d" '[g["appels"]["par_espece"]["CLAUDE_FABLE_5_1"].update(par_statut={"ECHEC_API": g["appels"]["par_espece"]["CLAUDE_FABLE_5_1"]["n"]}) for g in x["generations"] if g.get("generation") == 1 and not g.get("phase")]'; refaire_empreintes "$d"
cas v53-fable-sans-ok "g001 : aucun appel OK de CLAUDE_FABLE_5_1" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_v53 graine)"; extrait_altere "$d" 'x["manifeste"]["entropie_seed_sequence"] = 13'; refaire_empreintes "$d"
cas v53-graine-autre "qui n'est pas la graine v5-3 du préenregistrement scellé" -- "${V6C[@]}" GRAINE="$G_6" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" PRECEDENTE_V53="$d"
d="$(copie_v53 graine-vide)"; extrait_altere "$d" 'x["manifeste"]["entropie_seed_sequence"] = None'; refaire_empreintes "$d"
cas v53-graine-vide "graine de v5.3 au manifeste illisible ou vide (None)" -- "${V6C[@]}" PRECEDENTE_V53="$d"
cas v6-1-depense-sans-empreinte-v53 "la ligne de dépense de v6.1 ne porte pas l'empreinte des empreintes de v5.3" -- "${V6C[@]}" PRECEDENTE_V53="$V53" DEPENSES_SOURCE="$E/entrees/dep-v6-sans-empreinte-v53.md"
d="$(copie_m graine-vide)"; extrait_altere "$d" 'x["manifeste"]["entropie_seed_sequence"] = None'; refaire_empreintes "$d"
cas m-graine-vide "graine de M au manifeste illisible ou vide (None)" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"

echo "== mode réel (copie du dépôt sous /root) : refus à l'étape (0), avant tout appel =="
REEL=(MODE=reel COURSE=v5-3 PILOTE_RACINE=- DEPOT="$DEPOT_ROOT" "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai)
cas reel-sans-reference "REFERENCE_M non défini" -- "${REEL[@]}"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
cas reel-reference-hors-root "REFERENCE_M $M_REF hors de /root et de /home" -- "${REEL[@]}" REFERENCE_M="$M_REF"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
RR="$(dirname "$DEPOT_ROOT")/references-m"; rm -rf "$RR"; mkdir -p "$RR"; cp -a "$M_REF" "$RR/autre-nom-v1"
cas reel-reference-nom "nom autre que pilote2-gemini-v5-2-1-maieutique-v1[-tentativeN]" -- "${REEL[@]}" REFERENCE_M="$RR/autre-nom-v1"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
cp -a "$M_REF" "$RR/pilote2-gemini-v5-2-1-maieutique-v1"
cas reel-reference-simulee "M n a pas tourné en réel" -- "${REEL[@]}" REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
cp -a "$M_REF" "$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"
cas reel-reference-tentative-simulee "M n a pas tourné en réel" -- "${REEL[@]}" COURSE=v5-3 REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes" "$RR"
echo "== mode réel, course v6.1 (copie du dépôt sous /root) : refus à l'étape (0 bis), avant tout appel =="
REEL_V6=(MODE=reel COURSE=v6-1 PILOTE_RACINE=- DEPOT="$DEPOT_ROOT" "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai)
cas reel-v6-1-sans-precedente "PRECEDENTE_V53 non défini" -- "${REEL_V6[@]}"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
cas reel-v6-1-precedente-hors-dossier "hors du dossier des pilotes" -- "${REEL_V6[@]}" PRECEDENTE_V53="$V53"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
mkdir -p "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"; cp -a "$V53" "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/autre-nom-v1"
cas reel-v6-1-precedente-nom "nom autre que pilote4-gemini-v5-3-v1[-tentativeN]" -- "${REEL_V6[@]}" PRECEDENTE_V53="$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/autre-nom-v1"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
mkdir -p "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"; cp -a "$V53" "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v5-3-v1"
cas reel-v6-1-precedente-simulee "v5.3 n a pas tourné en réel" -- "${REEL_V6[@]}" PRECEDENTE_V53="$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v5-3-v1"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"

echo "== mode réel : gardes communes (échantillon), avant tout appel =="
cas reel-variable-essai "variable PILOTE_RACINE définie en mode réel" -- MODE=reel
cas reel-espace "variable ESSAIM_M3_ESPACE définie en mode réel" -- MODE=reel PILOTE_RACINE=- ESSAIM_M3_ESPACE=/var/tmp/x
cas reel-sans-cle "CLE_ANTHROPIC non défini" -- MODE=reel PILOTE_RACINE=- ANTHROPIC_API_KEY=factice
cas reel-cle-hors-liste "CLE_ANTHROPIC=ANTHROPIC_API_KEY hors des clés des runs" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=ANTHROPIC_API_KEY ANTHROPIC_API_KEY=factice
cas reel-gemini-hors-liste "CLE_GEMINI=LUC_ABSENTE hors des clés des runs" -- MODE=reel PILOTE_RACINE=- CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_3=factice CLE_GEMINI=LUC_ABSENTE LUC_ABSENTE=factice
cas reel-sans-attestation "RECHARGE_ATTESTEE vide" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice
cas reel-sans-s2 "clé Semantic Scholar absente (variable SEMANTIC_SCHOLAR_API_KEY)" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice RECHARGE_ATTESTEE=essai
cas reel-depot-hors "hors de /root et de /home : il ne serait pas caché" -- MODE=reel PILOTE_RACINE=- "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai

echo "== refus avant le dossier ; course voisine =="
cas course-inconnue "COURSE inconnue : autre (v5-3 ou v6-1)" -- MODE=simulation COURSE=autre
cas course-du-second-pilote "COURSE inconnue : maieutique (v5-3 ou v6-1)" -- MODE=simulation COURSE=maieutique
( exec -a "python3 -m essaim_m3 lancer --decalage-uid 900 --factice" sleep 30 ) & VOISIN=$!
sleep 0.3
cas voisine-meme-decalage "tourne déjà au décalage d'utilisateurs 900" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null

echo "== R3 : verrou et marqueur de départ (noms du pilote 4) =="
mkdir -p "$E/racine-verrou/.verrou-pilote4-gemini-v6-1-v1"
cas verrou-present "verrou $E/racine-verrou/.verrou-pilote4-gemini-v6-1-v1 présent" -- MODE=simulation COURSE=v6-1 PILOTE_RACINE="$E/racine-verrou" "${SAIN[@]}"
mkdir -p "$E/racine-marqueur/.partis"; printf 'ailleurs\n' > "$E/racine-marqueur/.partis/pilote4-gemini-v5-3-v1"
cas marqueur-present "marqueur de départ $E/racine-marqueur/.partis/pilote4-gemini-v5-3-v1 présent" -- MODE=simulation PILOTE_RACINE="$E/racine-marqueur" "${SAIN[@]}"

echo "== code et commits : chemins permis après b1c7f4b6 =="
cas commit-question "absent du dépôt" -- MODE=simulation ESSAI_ARTEFACT=commit "${SAIN[@]}"
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/hors-pieces.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/hors-pieces.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : fichier hors des pièces"
cas commit-hors-pieces "commits postérieurs à b1c7f4b6 hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/piece-essai.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : pièce du pilote 4"
cas commit-pieces-pilote4 "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
mkdir -p "$DEPOT/essaim-m3-refonte-v1/prereg/contre-lectures"; printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/prereg/contre-lectures/pilote4-gemini-organisme-v1-cl1.md"
git -C "$DEPOT" add essaim-m3-refonte-v1/prereg/contre-lectures/pilote4-gemini-organisme-v1-cl1.md; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : contre-lecture du pilote 4"
cas commit-contre-lecture-pilote4 "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/banque/construction-v2/piece-essai.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/construction-v2/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : pièce de la banque v2"
cas commit-banque-v2 "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/banque/construction-v3/piece-essai.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/construction-v3/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : pièce de la banque v3"
cas commit-banque-v3 "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
mkdir -p "$DEPOT/essaim-m3-refonte-v1/banque/contre-lectures/essai"; printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/banque/contre-lectures/essai/piece-essai.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/contre-lectures/essai/piece-essai.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : contre-lecture de la banque"
cas commit-banque-contre-lecture "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'essai\n' >> "$DEPOT/essaim-m3-refonte-v1/banque/LISEZMOI-v6.md"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/LISEZMOI-v6.md; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : LISEZMOI-v6 de la banque modifié"
cas commit-banque-lisezmoi-six "commits postérieurs limités aux pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf '{}\n' > "$DEPOT/essaim-m3-refonte-v1/banque/banque-confrontation-v4.json"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/banque-confrontation-v4.json; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : banque v4 (hors du pilote 4)"
cas commit-banque-v4 "commits postérieurs à b1c7f4b6 hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/banque/banque-autre-v1.json"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/banque-autre-v1.json; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : autre fichier de la banque"
cas commit-banque-autre "commits postérieurs à b1c7f4b6 hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/prereg/pilote4-autre-texte-v1.md"
git -C "$DEPOT" add essaim-m3-refonte-v1/prereg/pilote4-autre-texte-v1.md; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : texte non permis"
cas commit-texte-non-permis "commits postérieurs à b1c7f4b6 hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1

echo "== préenregistrement (graines par course, lanceur cité, marqueurs) =="
cas prereg-graine-autre-course-v53 "n'est pas écrite dans le préenregistrement" -- MODE=simulation COURSE=v5-3 GRAINE="$G_6" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}"
cas prereg-graine-autre-course-v6-1 "n'est pas écrite dans le préenregistrement" -- MODE=simulation COURSE=v6-1 GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}"
cas prereg-graine-hors-entropie-v53 "≠ celle de SeedSequence(E).spawn(2)[0]" -- MODE=simulation COURSE=v5-3 GRAINE=13 PREREG="$E/entrees/prereg-graine-hors-entropie.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-graine-hors-entropie.md.sha256")" "${SAIN[@]}"
cas prereg-graine-hors-entropie-v6-1 "≠ celle de SeedSequence(E).spawn(2)[1]" -- MODE=simulation COURSE=v6-1 GRAINE=13 PREREG="$E/entrees/prereg-graine-hors-entropie.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-graine-hors-entropie.md.sha256")" "${SAIN[@]}"
cas prereg-lanceur-source "ne cite pas l'empreinte de ce lanceur" -- MODE=simulation GRAINE="$G_53" PREREG="$E/entrees/prereg-lanceur-source.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-lanceur-source.md.sha256")" "${SAIN[@]}"
cas prereg-marqueur "marqueurs <<…>> restants" -- MODE=simulation GRAINE="$G_53" PREREG="$E/entrees/prereg-marqueur.md" PREREG_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-marqueur.md.sha256")" "${SAIN[@]}"
cas prereg-empreinte "empreinte du préenregistrement ≠ PREREG_SHA256" -- MODE=simulation GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256=0000 "${SAIN[@]}"

echo "== objets et question =="
cas organisme-v5-3 "empreinte d'arbre de l'organisme ≠ 6251ab21…" -- MODE=simulation COURSE=v5-3 ESSAI_ARTEFACT=organisme "${SAIN[@]}"
cas organisme-v6-1 "empreinte d'arbre de l'organisme ≠ ae331d1d…" -- MODE=simulation COURSE=v6-1 ESSAI_ARTEFACT=organisme "${SAIN[@]}"
cas nombre-v5-3 "fichiers au lieu de 22" -- MODE=simulation COURSE=v5-3 ESSAI_ARTEFACT=nombre "${SAIN[@]}"
cas nombre-v6-1 "fichiers au lieu de 24" -- MODE=simulation COURSE=v6-1 ESSAI_ARTEFACT=nombre "${SAIN[@]}"
cas question "empreinte de la question ≠ 8b1c7511…" -- MODE=simulation ESSAI_ARTEFACT=question "${SAIN[@]}"

echo "== registres (GO-2026-10-25-02 ; dépense) =="
cas go-sans-calcul "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-calcul.md"
cas go-autre-id "aucune ligne « | GO-2026-10-25-02 | »" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-id.md"
cas go-v53-seulement-refuse-v6-1 "l'empreinte de l'organisme ae331d1d… et celle du texte scellé" -- MODE=simulation COURSE=v6-1 "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-v53-seulement.md"
cas go-autre-question "l'empreinte de la question 8b1c7511…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"
cas go-sans-texte "celle du texte scellé ($T16)" -- MODE=simulation COURSE=v5-3 GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-texte.md"
cas depense-absente "lancement non consigné avant dans registres/depenses.md (une ligne nommant pilote4-gemini-v5-3-v1 et GO-2026-10-25-02)" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-absente.md"
cas reste-insuffisant "< $USD_COURSE" -- MODE=simulation "${SAIN[@]}" RESTE_GO_USD="$SOUS_PLAFOND"

echo "== test de dépense (GO-2026-10-25-02) =="
cas td-autre-go "go = 'GO-2026-10-25-01' (attendu GO-2026-10-25-02)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-autre-go.json"
cas td-echec "CLAUDE_FABLE_5_1 : statut 'ECHEC_API'" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-echec.json"
cas td-heure-absente-exigee "heure_utc absente (exigée en réel)" -- MODE=simulation "${SAIN[@]}" ESSAI_EXIGER_HEURE=1
cas td-vieux "> 900 s" -- MODE=simulation ESSAI_ARTEFACT=appel-vieux "${SAIN[@]}"
td_noms "$E/entrees/td-noms-conformes.json" RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2
cas td-noms-conformes "noms des variables du test : anthropic RR_ANTHROPIC_API_KEY_3, gemini GEMINI_API_KEY_2" -- MODE=simulation COURSE=v6-1 "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-conformes.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2
td_noms "$E/entrees/td-noms-autres.json" RR_ANTHROPIC_API_KEY GEMINI_API_KEY
cas td-noms-autres "noms des variables du test : anthropic = 'RR_ANTHROPIC_API_KEY' (attendu RR_ANTHROPIC_API_KEY_3)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-autres.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2

echo "== essais du noyau =="
cas junit-echec "échecs" -- MODE=simulation ESSAI_ARTEFACT=junit-echec "${SAIN[@]}"
cas junit-total "essais au lieu de 141" -- MODE=simulation ESSAI_ARTEFACT=junit-total "${SAIN[@]}"

echo "== environnement du noyau et passerelle =="
cas env-noyau-nu "environnement du noyau (noms seulement, valeurs jamais écrites) : PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER ." -- MODE=simulation "${SAIN[@]}" HF_TOKEN=factice VAST_API_KEY=factice ANTHROPIC_API_KEY=factice
cas passerelle-saine "passerelle de sortie, sous l'environnement du noyau sans clé : httpx" -- MODE=simulation "${SAIN[@]}" ESSAI_PASSERELLE_PY="$PY_HTTPX" "${INFRA[@]}"
cas passerelle-sans-certificat "passerelle de sortie injoignable sous l'environnement du noyau : httpx, api.anthropic.com : ConnectError" -- MODE=simulation "${SAIN[@]}" ESSAI_PASSERELLE_PY="$PY_HTTPX"

echo "== après le départ =="
cas famille-puis-tentatives "aucune course partie (pas de manifeste" -- MODE=simulation COURSE=v6-1 ESSAI_ARTEFACT=famille "${SAIN[@]}"
R_F="$E/cas-famille-puis-tentatives"
cas tentative-2 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-1 TENTATIVE=2 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas tentative-3 "R3 : jamais de seconde course" -- MODE=simulation COURSE=v6-1 TENTATIVE=3 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas archive-incomplete "ARCHIVE FERMÉE INCOMPLÈTE" -- MODE=simulation ESSAI_ARTEFACT=archive "${SAIN[@]}"
cas imprevu "fichiers imprévus, NON poussés" -- MODE=simulation ESSAI_ARTEFACT=imprevu "${SAIN[@]}"
echo "== état des dépôts d'essai après la série =="
git -C "$DEPOT" status --porcelain --ignored | grep -v __pycache__ | head -5
git -C "$DEPOT" log --oneline -1 | cut -c1-12
git -C "$DEPOT_M" log --oneline -1 | cut -c1-12
echo "== bilan : $ok sur $n cas conformes =="
