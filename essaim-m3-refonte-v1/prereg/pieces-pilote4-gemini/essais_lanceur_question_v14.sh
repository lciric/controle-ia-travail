#!/usr/bin/env bash
# Essais du lanceur des deux courses à question de la v6.2.1 (« maieutique », clé `maieutique`, GO-2026-10-26-05 ; « audit », clé `audit`, GO-2026-10-26-04, question v3 servie avec son annexe définitive, la transcription expurgée v2 du rapport consolidé (commit ad23e9ae, R-518) ; banque v3, quatre générations notées, 6 rondes de conception au
# plus), v14 : la v13 (7b0a9bb0…) par `deriver_essais_question_v14.py` pour le lanceur v12 (texte v1, table de correspondance ;
# brief de conv-audit et ses précisions : bloc de paramètres, question « audit » v3 à `ad23e9ae` et son annexe, paramètres définitifs) : cas
# et artefacts adaptés aux deux clés (les clés `v6-2-s` et `v6-2` d'hier deviennent `maieutique`, enfant 0, course par défaut
# des cas, des segments, de la fermeture et du mutant ; `audit`, enfant 1, tourne avec une annexe synthétique committée dans la
# copie puis retirée de sa tête, donnée au lanceur par ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN, ESSAI_ANNEXE_1_SHA ; noms
# `course-maieutique-gemini-v6-2-v1` et `course-audit-gemini-v6-2-v1` ; TEXTE et TEXTE_SHA256 à la place de PREREG ; GO_ID par
# course, posé par `cas` : 05, ou 04 avec la pièce de dépense `td-sain-audit` et l'annexe synthétique quand la course est
# `audit` ; lignes de GO d'essai à la forme de la ligne d'extension, `ligne_go` ; lignes de dépense à la
# forme `| date | nom | GO | 75 USD au pire cas | empreintes de M … |`) ; cas retirés : la porte « course v6.2 précédente »
# (v62-*, seg-v62-*, seg-v6-2-s-porte-saine, seg-clore-v62-refusee, reel-v6-2-s-*, copies « réelles ») ; cas ajoutés ou
# renommés : cle-ancienne-refusee (et -v6-2, reel-cle-ancienne-*), go-id-forme, reel-sans-go-id, reel-journal-garde-essai,
# texte-* (dont texte-sans-ligne-de-l-autre-course), question-empreinte-autre (artefact question-base), question-servie-alteree,
# question-v1-refusee, question-v2-refusee, go-question-v1-refuse-audit et go-question-v2-refuse-audit (les questions « audit » v1,
# dd2c1016…, et v2, ec3abf28…, ne servent plus), sain-audit sur les paramètres définitifs (question v3 et annexe réelle, sans variable
# d'essai ; taille servie vérifiée ≤ 100 000), annexe-empreinte-fausse (annexe réelle, empreinte fausse : refus avant tout appel), annexe-absente,
# annexe-alteree, annexe-champs-incomplets, annexe-commit-absent, question-servie-trop-longue (borne du noyau 9beee10b :
# 100 000 caractères, question.py ; noyau attendu NOYAU_COMMIT, les copies d'essai à sa tête), audit-sans-annexe-reserve (artefact annexe-vide), reel-annexe-essai, annexe-artefacts-sans-effet-maieutique,
# go-maieutique-seulement-* et go-audit-seulement-*, go-questions-croisees, depense-ancienne-forme,
# sain-audit-question-servie (composé recalculé ici, avec l'annexe synthétique), sain-*-garde, porte
# « précédente » absente (sain-maieutique avec PRECEDENTE_V62 ignorée, reel-sans-reference sans elle), garde-refus-question-sain,
# garde-refus-question-ligne-incomplete, garde-refus-question-artefact, -fin-surete, -critique-sans-moissonneur,
# -apres-moissonneur, -rang-121, -premiere-caste-apres-moissonneur, -motif-reel-m-complet (arrêts : journaux synthétiques,
# ESSAI_JOURNAL_GARDE ; arrêt sous 10 s, ligne écrite, règle consignée, pièce poussée, g001 jamais archivée, SEGMENT=2 refusé) ;
# garde-refus-question-tache-refusee, -rang-120, -moissonneur-refuse, -motif-reel-m-avant-question (aucun arrêt : règle de
# conv-audit du 26 octobre 2026, le motif réel de g001 de la course M du pilote 4, journal fec0cb82…, 129 appels) ;
# la v13 était dérivée de la v12 (27ef4524…) par `deriver_essais_pilote4_v13.py` pour le lanceur v11 (seconde course `v6-2-s` : le même
# organisme, la v6.2.1, sur la question S `a54da93e…`, à la place de la clé `v5-3` — la v5.3 ne court pas, décision de Lazar du
# 26 octobre 2026, 04:13 UTC, R-492 ; question par course ; chaque cas de la v12 garde un équivalent : clé, noms, lignée,
# messages « la course S ne part qu'après… », graine enfant 0 ; une ligne de GO saine porte `8b1c7511…`, `a54da93e…` et
# `4f13647a…`, `6251ab21…` n'est plus requis ; cas ajoutés : reel-v6-2-refusee (en réel, `v6-2` refusée : la course M a tourné
# sous le lanceur v10), go-m-seulement-refuse-v6-2-s et go-m-seulement-autorise-v6-2 (ligne de GO portant `8b1c7511…` sans
# `a54da93e…` : refusée pour `v6-2-s`, suffisante pour `v6-2`), question-v6-2, sain-v6-2-question et sain-v6-2-s-question
# (question par course), sain-v6-2-s-lanceur-attendu et v62-lanceur-v10-en-simulation (en simulation, la course précédente
# doit avoir tourné sous ce lanceur-ci), reel-porte-v10-passee, reel-porte-v10-attendu et reel-v6-2-s-precedente-sous-ce-lanceur
# (en réel, la porte « course précédente » attend le lanceur v10, `0203f546…` : une copie « réelle » de la v6.2 saine,
# LANCEMENT.md et manifeste réécrits, rescellée, passe la porte, et les cas réels de l'étape (0) courent sur `v6-2-s` derrière
# elle ; une copie « réelle » citant ce lanceur-ci est refusée) ; la v12 n'a jamais tourné sur le lanceur v11) ; la v12 était
# dérivée de la v11 (ba47a625…) par `deriver_essais_pilote4_v12.py` pour le lanceur v10 (objet de la course v6-2 : la
# v6.2.1, empreinte d'arbre `4f13647a…`, 26 fichiers — la v6.2 de Gemini corrigée par conv-audit ; aucun cas ajouté ni
# retiré ; la v11 n'a jamais tourné) ; la v11 était dérivée de la v10 (b7906684…) par `deriver_essais_pilote4_v11.py`
# pour le lanceur v9 (ordre des courses inversé, décision
# de Lazar du 26 octobre 2026, 00:18 Paris : la v6.2 d'abord, puis la v5.3 après une v6.2 saine ; porte « v6.2 précédente »
# sur un cas sain et sur ses artefacts ; segments essayés sur la v6.2 ; un cas ajouté, sain-v5-3-graine) ; la v10 était
# dérivée de la v9 (edb6b12b…) par `deriver_essais_pilote4_v10.py` pour le lanceur v8 (la v6.2 livrée, commit `3bbb78c`,
# empreinte d'arbre `3b2d8d5a…`, à la place du premier commit de Gemini ; aucun cas ajouté ni retiré ; la v9 n'a jamais
# tourné) ; la v9 était dérivée de la v8 (a5f4b944…) par `deriver_essais_pilote4_v9.py` pour le lanceur v7 (objet de la
# seconde course : la v6.2 à la place de la v6.1 — clé de course, noms, empreinte d'arbre ; décision de Lazar du
# 25 octobre 2026, 23:54 Paris ; aucun cas ajouté ni retiré) ; la v8 était dérivée de la v7 (c3263af1…) par `deriver_essais_pilote4_v8.py` (contre-lecture 3,
# P4C3-03 : gardes du segment K ≥ 2 et de la porte essayées sur un artefact, minuteur essayé sur une copie mutée du
# lanceur ; lanceur v6 inchangé) ; la v7 était dérivée de la v6 (b4857c51…) par `deriver_essais_pilote4_v7.py` pour le lanceur v6 (vérification de la reprise
# refusée corrigée) ; la v6 était dérivée de la v5 (e216c39e…) par `deriver_essais_pilote4_v6.py` pour le lanceur v5
# (reprise par segments, 75 USD par course, minuteur à 3 400 s) ; la v5 était dérivée de la v4 (8e82d9ca…) pour le lanceur v4 (borne des rondes,
# minuteur ; banque autre que la v3 refusée) ; la v4 était dérivée de la batterie v3 du pilote 3 (`essais_lanceur_pilote3_v5_3_v6_v3.sh`, 14bc0535…, 122 cas sur 122
# sur le lanceur v2) par `deriver_essais_pilote4_v4.py` (remplacements exacts, configuration du lanceur ; la v1 laissait le chemin du
# cas sain de la v6.x à l’ancienne étiquette). Cette série
# essaie (i) les deux courses saines de bout en bout en simulation (v6.2, essais du noyau exécutés ; puis la course S après la
# v6.2 saine), avec les rondes de conception et les quatre générations, et relève ce que montrent les rondes ; (ii) la
# course M de référence, produite par le lanceur scellé du second pilote lui-même, puis chaque issue de M hors de la
# liste close ; (iii) la porte « v6.2 précédente » (générations 0 à 3) et ses artefacts ; (iv) ce qui change (objets,
# graines, banque v3 et les chemins permis des banques v2 et v3, ligne de GO liée au texte scellé, journaux recopiés et poussés) ; (v) un
# échantillon des gardes communes, en simulation et en mode réel (refus avant tout appel). Aucun appel réel.
# Usage : bash essais_lanceur_question_v14.sh LANCEUR LANCEUR_M DEPOT DEPOT_M PYTHON DOSSIER_ESSAIS DEPOT_SOUS_ROOT PYTHON_AVEC_HTTPX
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
G_M="$("$PY" -I -c 'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[0].generate_state(1, dtype=numpy.uint64)[0]))')"
G_A="$("$PY" -I -c 'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[1].generate_state(1, dtype=numpy.uint64)[0]))')"
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
td "$E/entrees/td-sain.json" OK claude-fable-5-1 0.00058 GO-2026-10-26-05
td "$E/entrees/td-sain-audit.json" OK claude-fable-5-1 0.00058 GO-2026-10-26-04
td "$E/entrees/td-echec.json" ECHEC_API None 0 GO-2026-10-26-05
td "$E/entrees/td-autre-go.json" OK claude-fable-5-1 0.00058 GO-2026-10-25-01
td "$E/entrees/td-go-maieutique.json" OK claude-fable-5-1 0.00058 GO-2026-10-26-05   # la pièce de la course « maieutique », présentée à la course « audit »
TDS="$E/entrees/td-sain.json $E/entrees/td-sain-audit.json $E/entrees/td-echec.json $E/entrees/td-autre-go.json $E/entrees/td-go-maieutique.json"
td_heure() {  # td_heure FICHIER MINUTES GO : pièce avec une heure d'appel par espèce, vieille de MINUTES
  "$PY" -I -c '
import datetime, json, sys
h = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=float(sys.argv[2]))).isoformat().replace("+00:00", "Z")
d = {"especes": {"CLAUDE_FABLE_5_1": {"statut": "OK", "modele_servi": "claude-fable-5-1", "cout_usd": 0.00058, "jetons_sortie": 8, "heure_utc": h},
                 "CLAUDE_OPUS_5_5": {"statut": "OK", "modele_servi": "claude-opus-5-5", "cout_usd": 0.000232, "jetons_sortie": 8, "heure_utc": h},
                 "GEMINI_ARGON": {"statut": "OK", "modele_servi": "gemini-4-argon", "cout_usd": 0.00076, "jetons_sortie": 8, "heure_utc": h}}, "go": sys.argv[3]}
json.dump(d, open(sys.argv[1], "w"))' "$@"
}
td_noms() {  # td_noms FICHIER ANTHROPIC GEMINI GO : pièce fraîche avec heures d'appel et noms des variables
  "$PY" -I -c '
import datetime, json, sys
h = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
e = {k: {"statut": "OK", "modele_servi": m, "cout_usd": 0.0005, "jetons_sortie": 8, "heure_utc": h} for k, m in (("CLAUDE_FABLE_5_1", "claude-fable-5-1"), ("CLAUDE_OPUS_5_5", "claude-opus-5-5"), ("GEMINI_ARGON", "gemini-4-argon"))}
json.dump({"especes": e, "go": sys.argv[4], "variables_cles": {"anthropic": sys.argv[2], "gemini": sys.argv[3]}}, open(sys.argv[1], "w"))' "$@"
}
pr() {  # pr FICHIER CONTENU [sans-compagnon]
  printf '%s\n' "$2" > "$1"; [ "${3:-}" = sans-compagnon ] || (cd "$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256")
}
pr "$E/entrees/prereg-sain.md" "entropie E = $ENTROPIE tirée au scellement
graine de la course maieutique = $G_M
graine de la course audit = $G_A
lanceur $H"
pr "$E/entrees/prereg-graine-hors-entropie.md" "entropie E = $ENTROPIE
graine de la course maieutique = 13
graine de la course audit = 13
lanceur $H"
pr "$E/entrees/prereg-lanceur-source.md" "entropie E = $ENTROPIE
graine de la course maieutique = $G_M
graine de la course audit = $G_A
lanceur $H_M"
pr "$E/entrees/prereg-marqueur.md" "entropie E = $ENTROPIE
graine de la course maieutique = $G_M
graine de la course audit = $G_A
lanceur $H ; <<EMPREINTE_PIECES>>"
pr "$E/entrees/prereg-une-ligne.md" "entropie E = $ENTROPIE
graine de la course maieutique = $G_M
lanceur $H"
SHA_PR="$(cut -d' ' -f1 < "$E/entrees/prereg-sain.md.sha256")"
T16="${SHA_PR:0:16}"   # la ligne de GO porte les 16 premiers caractères de l'empreinte du texte (le même texte pour les deux GO)
Q_M=1d29fbecd52b1dfc94410e117f786811067f86f3cce24c4c54bbe424e480e3a3; Q_A=998960b8d101d5013c498d6fcf225277ba17d20741825ad136381892c05cfd0e   # empreintes des questions « maieutique » (commit eb03bad5) et « audit » v3 (commit ad23e9ae, R-518)
Q_A_V1=dd2c1016e20a4823dcb2ce4c1e94d2c6be7a6962cb52a10ee7ac3b1f7d1203aa   # question « audit » v1 : ne sert plus (R-515, R-516), refusée comme empreinte autre
Q_A_V2=ec3abf2880bdb52fd6193a1994893a0c380c3557a70c94b8f20749220447c4a4   # question « audit » v2 (commit 9417652a) : ne sert plus (R-518), refusée comme empreinte autre
COMMIT_DEF=ad23e9ae07588ed701a70b9b5f4bf379ca079953; ANNEXE_DEF_CHEMIN=docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md; ANNEXE_DEF_SHA=c1237687e98db14475336af690986bc08800a85e259d249de4940130245b1a64   # paramètres définitifs de l'annexe (R-518), les mêmes que dans le lanceur
ligne_go() {  # ligne_go GO COURSE QUESTION_SHA TEXTE16 [TYPE] : une ligne du registre des GO, à la forme de la ligne d'extension (texte v1, § Plan)
  printf '| %s | 2026-10-26 | %s | extension : course « %s » (essai) — la v6.2.1 7ea3270, arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d, sur la question %s (commit eb03bad5) ; banque confrontation-v3 157a2b45… ; texte courses-question-gemini-v6-2-v1.md %s ; lanceur lancer_courses_question_v12.sh %s, noyau 9beee10b | 75 USD au plus | 2026-10-31 | Lazar | R-509 |\n' "$1" "${5:-calcul}" "$2" "$3" "$4" "$H"
}
{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_A" "$T16"; } > "$E/entrees/go-sain.md"
{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16" essai; ligne_go GO-2026-10-26-04 audit "$Q_A" "$T16" essai; } > "$E/entrees/go-sans-calcul.md"
{ ligne_go GO-2026-10-25-02 maieutique "$Q_M" "$T16"; ligne_go GO-2026-10-25-02 audit "$Q_A" "$T16"; } > "$E/entrees/go-autre-id.md"   # le GO du pilote 4, autre que celui de la course
ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16" > "$E/entrees/go-maieutique-seulement.md"
ligne_go GO-2026-10-26-04 audit "$Q_A" "$T16" > "$E/entrees/go-audit-seulement.md"
{ ligne_go GO-2026-10-26-05 maieutique 0000000000000000000000000000000000000000000000000000000000000000 "$T16"; ligne_go GO-2026-10-26-04 audit 0000000000000000000000000000000000000000000000000000000000000000 "$T16"; } > "$E/entrees/go-autre-question.md"
{ ligne_go GO-2026-10-26-05 maieutique "$Q_A" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_M" "$T16"; } > "$E/entrees/go-questions-croisees.md"
{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_A_V1" "$T16"; } > "$E/entrees/go-question-v1.md"   # la ligne du GO 04 porte la question audit v1
{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_A_V2" "$T16"; } > "$E/entrees/go-question-v2.md"   # la ligne du GO 04 porte la question audit v2
{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "(sans le texte)"; ligne_go GO-2026-10-26-04 audit "$Q_A" "(sans le texte)"; } > "$E/entrees/go-sans-texte.md"
n=0; ok=0
verifier() {  # verifier NOM ATTENDU FICHIER… : le motif doit se trouver dans l'un des fichiers
  local nom="$1" attendu="$2"; shift 2
  n=$((n + 1))
  if cat "$@" 2>/dev/null | grep -qF -- "$attendu"; then ok=$((ok + 1)); echo "OK     $nom : « $attendu »"
  else echo "ÉCHEC  $nom : attendu « $attendu »"; fi
}
verifier_absent_texte() {  # verifier_absent_texte NOM MOTIF FICHIER… : le motif ne doit se trouver dans aucun des fichiers
  local nom="$1" motif="$2"; shift 2
  n=$((n + 1))
  if cat "$@" 2>/dev/null | grep -qF -- "$motif"; then echo "ÉCHEC  $nom : « $motif » présent"; else ok=$((ok + 1)); echo "OK     $nom : « $motif » absent"; fi
}
cas() {  # cas NOM ATTENDU -- VAR=VAL… (motif cherché dans la sortie d'erreur et LANCEMENT.md) ; COURSE=audit entraîne GO_ID=GO-2026-10-26-04, la pièce de dépense td-sain-audit.json à la place de td-sain.json et, hors du mode réel, l'annexe synthétique (ESSAI_ANNEXE_1_*, que le cas peut redéfinir)
  local nom="$1" attendu="$2"; shift 3
  n=$((n + 1))
  local racine="$E/cas-$nom"; rm -rf "$racine"; mkdir -p "$racine"
  # shellcheck disable=SC2086
  touch $TDS
  local audit="" reel="" a args=()
  for a in "$@"; do [ "$a" = COURSE=audit ] && audit=1; [ "$a" = MODE=reel ] && reel=1; done
  for a in "$@"; do if [ -n "$audit" ] && [ "$a" = "APPEL_CONTROLE_FICHIER=$E/entrees/td-sain.json" ]; then a="APPEL_CONTROLE_FICHIER=$E/entrees/td-sain-audit.json"; fi; args+=("$a"); done
  [ -n "$audit" ] && args=(GO_ID=GO-2026-10-26-04 "${args[@]}")
  [ -n "$audit" ] && [ -z "$reel" ] && args=(ESSAI_ANNEXE_1_COMMIT="$ANNEXE_ESSAI_COMMIT" ESSAI_ANNEXE_1_CHEMIN="$ANNEXE_ESSAI_CHEMIN" ESSAI_ANNEXE_1_SHA="$ANNEXE_ESSAI_SHA" "${args[@]}")   # jamais en réel (variables d'essai interdites)
  env -i PATH="$PATH" HOME="$E" LANG=C.UTF-8 DEPOT="$DEPOT" PYTHON="$PY" GRAINE=13 COURSE=maieutique GO_ID=GO-2026-10-26-05 "${args[@]}" \
    PILOTE_RACINE_DEFAUT="$racine" bash -c 'export PILOTE_RACINE="${PILOTE_RACINE-$PILOTE_RACINE_DEFAUT}"; [ "$PILOTE_RACINE" = "-" ] && unset PILOTE_RACINE; exec bash "$0"' "$LANCEUR" \
    > "$racine/sortie.txt" 2> "$racine/erreur.txt"
  local code=$?
  local autre_racine=""
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
printf '| 2026-10-26 | course-maieutique-gemini-v6-2-v1 | GO-2026-10-26-05 | 75 USD au pire cas | empreintes de M %s |\n| 2026-10-26 | course-audit-gemini-v6-2-v1 | GO-2026-10-26-04 | 75 USD au pire cas | empreintes de M %s |\n' "${EMP_M:0:16}" "${EMP_M:0:16}" > "$E/entrees/dep-sain.md"
printf '| 2026-10-26 | course-maieutique-gemini-v6-2-v1 | GO-2026-10-26-05 | 75 USD au pire cas |\n| 2026-10-26 | course-audit-gemini-v6-2-v1 | GO-2026-10-26-04 | 75 USD au pire cas |\n' > "$E/entrees/dep-sans-empreinte-m.md"
printf '| 2026-10-26 | course-maieutique-gemini-v6-2-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M %s |\n' "${EMP_M:0:16}" > "$E/entrees/dep-absente.md"
printf '| 2026-10-25 | pilote4-gemini-v6-2-v1 | GO-2026-10-25-02 | 75 USD au pire cas | après M, empreintes de M %s |\n| 2026-10-25 | pilote4-gemini-v6-2-s-v1 | GO-2026-10-25-02 | 75 USD au pire cas | après M et v6.2, empreintes de M %s, de v6.2 0000000000000000 |\n' "$EMP_M" "$EMP_M" > "$E/entrees/dep-ancienne-forme.md"   # forme du pilote 4 : noms et GO d'hier
SAIN=(REGISTRE_GO_SOURCE="$E/entrees/go-sain.md" DEPENSES_SOURCE="$E/entrees/dep-sain.md" RESTE_GO_USD=150
      APPEL_CONTROLE_FICHIER="$E/entrees/td-sain.json" RECHARGE_ATTESTEE="essai" REFERENCE_M="$M_REF")
# annexe synthétique de la course « audit » (et une annexe trop longue pour la borne du noyau, 100 000 caractères au noyau 9beee10b) : chacune committée dans la copie
# sous un chemin permis, le commit relevé, puis HEAD rétabli (l'objet reste dans le dépôt, comme une annexe réelle récupérée
# de main sans être sur la tête) ; passées au lanceur par ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN, ESSAI_ANNEXE_1_SHA
annexe_commit() {  # annexe_commit CHEMIN_RELATIF FICHIER_CONTENU → le commit qui porte le fichier (puis HEAD~1)
  mkdir -p "$DEPOT/$(dirname "$1")"; cp "$2" "$DEPOT/$1"; git -C "$DEPOT" add "$1"; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : annexe synthétique"
  git -C "$DEPOT" rev-parse HEAD; git -C "$DEPOT" reset -q --hard HEAD~1
}
printf '# Annexe synthétique (essai de la batterie v14)\n\nTranscription factice : trois lignes, aucun contenu réel.\nLigne deux.\nLigne trois.\n' > "$E/entrees/annexe-essai-v1.md"
"$PY" -I -c 'import sys; open(sys.argv[1], "w", encoding="utf-8").write("# Annexe trop longue (essai)\n\n" + ("x" * 99 + "\n") * 1000)' "$E/entrees/annexe-longue-v1.md"   # 100 029 caractères
ANNEXE_ESSAI_CHEMIN=essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/annexe-essai-v1.md; ANNEXE_ESSAI_SHA="$(sha256sum "$E/entrees/annexe-essai-v1.md" | cut -d' ' -f1)"
ANNEXE_ESSAI_COMMIT="$(annexe_commit "$ANNEXE_ESSAI_CHEMIN" "$E/entrees/annexe-essai-v1.md")"
ANNEXE_LONGUE_CHEMIN=essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/annexe-longue-v1.md; ANNEXE_LONGUE_SHA="$(sha256sum "$E/entrees/annexe-longue-v1.md" | cut -d' ' -f1)"
ANNEXE_LONGUE_COMMIT="$(annexe_commit "$ANNEXE_LONGUE_CHEMIN" "$E/entrees/annexe-longue-v1.md")"
echo "annexes synthétiques : $ANNEXE_ESSAI_CHEMIN au commit $ANNEXE_ESSAI_COMMIT ($ANNEXE_ESSAI_SHA) ; $ANNEXE_LONGUE_CHEMIN au commit $ANNEXE_LONGUE_COMMIT"

echo "== cas sains : course « maieutique » complète (essais du noyau exécutés), puis course « audit » (paramètres définitifs : question v3 et son annexe réelle, commit ad23e9ae) ; rondes de conception et quatre générations =="
td_heure "$E/entrees/td-heure-fraiche-maieutique.json" 0 GO-2026-10-26-05
cas sain-maieutique "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-maieutique.json" ESSAI_EXIGER_HEURE=1 PRECEDENTE_V62="$E/nulle-part"
VM="$E/cas-sain-maieutique/course-maieutique-gemini-v6-2-v1"
verifier sain-maieutique-reference-m "; M saine : g000 et g001 OK" "$VM/LANCEMENT.md"
verifier sain-maieutique-graine-m "graine $GRAINE_M_SCELLEE = graine M du texte scellé du second pilote (d2944654…)" "$VM/LANCEMENT.md"
verifier sain-maieutique-organisme "organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d" "$VM/LANCEMENT.md"
verifier sain-maieutique-essais "essais : 169 passés, 0 sauté, 0 désélectionnés" "$VM/LANCEMENT.md"
verifier sain-maieutique-registre "registre : une ligne GO-2026-10-26-05 de type calcul" "$VM/LANCEMENT.md"
verifier sain-maieutique-graine "graine $G_M de la course maieutique écrite et recalculée depuis l'entropie du texte (enfant 0), ligne de la course audit présente (non utilisée)" "$VM/LANCEMENT.md"
verifier sain-maieutique-temps-conception "temps par ronde de conception 900 s" "$VM/LANCEMENT.md"
verifier sain-maieutique-minuteur "STOP non posé" "$VM/LANCEMENT.md"
verifier sain-maieutique-question "question (maieutique) : sha256 $Q_M (question-hypotheses-maieutique-organismes-v1.md, commit eb03bad5…) ; annexes servies : 0" "$VM/LANCEMENT.md"
verifier sain-maieutique-question-servie "question servie : question.md, sha256 $Q_M, 2916 caractères" "$VM/LANCEMENT.md"
verifier sain-maieutique-garde "garde refus-question : aucun arrêt ; veilleur arrêté par son PID" "$VM/LANCEMENT.md"
verifier sain-maieutique-garde-journal "journal vivant de g001 : /var/lib/essaim-m3/" "$VM/LANCEMENT.md"
verifier sain-maieutique-garde-roles "rôles propres à la question : monoculture_croisee sonde_orthogonale_onsager critique_adversariale_limites arbitre_synthese_contradictoire ; monoculture_analytique : refus après le premier appel moissonneur_* de g001 ou au-delà du 120e appel de ce rôle ; raisons d'arrêt de sûreté : refusal SAFETY PROHIBITED_CONTENT BLOCKLIST SPII RECITATION IMAGE_SAFETY BLOCAGE_PROMPT" "$VM/LANCEMENT.md"
verifier sain-maieutique-groupe "session et groupe de processus propres, par setsid : groupe " "$VM/LANCEMENT.md"
verifier_absent_texte sain-maieutique-sans-porte-precedente "course v6.2 précédente" "$VM/LANCEMENT.md"
verifier_absent_texte sain-maieutique-precedente-ignoree "PRECEDENTE_V62" "$VM/LANCEMENT.md"
JUNIT="$E/junit-sain-v1.xml"; cp "$VM/essais-v1.xml" "$JUNIT"
SAIN+=(ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="169 passed")
td_heure "$E/entrees/td-heure-fraiche-audit.json" 0 GO-2026-10-26-04
cas sain-audit "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit GRAINE="$G_A" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-audit.json" ESSAI_EXIGER_HEURE=1 ESSAI_ANNEXE_1_COMMIT= ESSAI_ANNEXE_1_CHEMIN= ESSAI_ANNEXE_1_SHA=   # paramètres définitifs du lanceur : question v3 et annexe réelle, aucune variable d'essai d'annexe
VA="$E/cas-sain-audit/course-audit-gemini-v6-2-v1"
verifier sain-audit-reference-m "; M saine : g000 et g001 OK" "$VA/LANCEMENT.md"
verifier sain-audit-organisme "organisme : 26 fichiers, empreinte d'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d" "$VA/LANCEMENT.md"
verifier sain-audit-registre "registre : une ligne GO-2026-10-26-04 de type calcul" "$VA/LANCEMENT.md"
verifier sain-audit-graine "graine $G_A de la course audit écrite et recalculée depuis l'entropie du texte (enfant 1), ligne de la course maieutique présente (non utilisée)" "$VA/LANCEMENT.md"
verifier sain-audit-temps-conception "temps par ronde de conception 900 s" "$VA/LANCEMENT.md"
verifier sain-audit-minuteur "STOP non posé" "$VA/LANCEMENT.md"
verifier sain-audit-question "question (audit) : sha256 $Q_A (question-audit-controle-organismes-v3.md, commit ad23e9ae…) ; annexes servies : 1 ; annexe 1 : $ANNEXE_DEF_CHEMIN $COMMIT_DEF $ANNEXE_DEF_SHA" "$VA/LANCEMENT.md"
# la question servie de la course « audit », recomposée ici sans le lanceur, depuis le dépôt : la question v3, puis, pour chaque annexe servie,
# une ligne ---, un titre « # Annexe k — chemin (sha256 …) » et son contenu (une ligne vide avant et après chaque séparateur et chaque titre)
"$PY" -I -c '
import hashlib, subprocess, sys
depot = sys.argv[1]
def lire(c, p): return subprocess.run(["git", "-C", depot, "show", c + ":" + p], check=True, capture_output=True).stdout
b = lire("ad23e9ae07588ed701a70b9b5f4bf379ca079953", "brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v3.md")
for k, (c, p, h) in enumerate([(sys.argv[2], sys.argv[3], sys.argv[4])], 1):
    b += ("\n---\n\n# Annexe %d — %s (sha256 %s)\n\n" % (k, p, h)).encode("utf-8") + lire(c, p)
print(hashlib.sha256(b).hexdigest(), len(b.decode("utf-8")))' "$DEPOT" "$COMMIT_DEF" "$ANNEXE_DEF_CHEMIN" "$ANNEXE_DEF_SHA" > "$E/question-servie-audit.txt"
read -r SHA_SERVIE_A N_SERVIE_A < "$E/question-servie-audit.txt"
verifier sain-audit-question-servie "question servie : question.md, sha256 $SHA_SERVIE_A, $N_SERVIE_A caractères" "$VA/LANCEMENT.md"
verifier sain-audit-question-servie-fichier "$SHA_SERVIE_A  question.md" "$VA/EMPREINTES-pilote-v1.txt"
verifier sain-audit-question-fichier-annexe "# Annexe 1 — $ANNEXE_DEF_CHEMIN (sha256 $ANNEXE_DEF_SHA)" "$VA/question.md"
"$PY" -I -c 'import sys; n = int(sys.argv[1]); b = int(sys.argv[2]); print("taille servie %d caractères %s %d (CARACTERES_MAX_QUESTION du noyau 9beee10b)" % (n, "≤" if n <= b else ">", b))' "$N_SERVIE_A" 100000 > "$E/taille-servie-audit.txt"
verifier sain-audit-taille-servie-sous-la-borne "caractères ≤ 100000 (CARACTERES_MAX_QUESTION du noyau 9beee10b)" "$E/taille-servie-audit.txt"   # assertion demandée : question v3 + annexe < 100 000
verifier sain-audit-taille-servie-relevee "taille servie 39617 caractères" "$E/taille-servie-audit.txt"   # 3 430 (question v3) + 163 (titre) + 36 024 (annexe)
verifier sain-audit-garde "garde refus-question : aucun arrêt" "$VA/LANCEMENT.md"
verifier_absent_texte sain-audit-sans-reserve-annexe "sans aucune annexe servie" "$VA/LANCEMENT.md"
for d in "$VM" "$VA"; do
  for g in g000 g001 g002 g003 c001; do
    verifier "sain-journal-$g-$(basename "$d")" "journal des appels $g : journal-appels-$g.jsonl" "$d/LANCEMENT.md"
    verifier "sain-pousse-$g-$(basename "$d")" "journal-appels-$g.jsonl" "$d/A-POUSSER-v1.txt"
  done
  verifier "sain-reponse-$(basename "$d")" "réponse à la question : reponse-question-g001.md, sha256" "$d/LANCEMENT.md"
done
echo "== relevé des rondes de conception et des générations en simulation (non compté) =="
for d in "$VM" "$VA"; do
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
cas sain-simulation-sans-reference "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit REGISTRE_GO_SOURCE="$E/entrees/go-sain.md" DEPENSES_SOURCE="$E/entrees/dep-sans-empreinte-m.md" RESTE_GO_USD=150 APPEL_CONTROLE_FICHIER="$E/entrees/td-sain-audit.json" RECHARGE_ATTESTEE=essai ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="169 passed"
cas go-maieutique-seulement-autorise-maieutique "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-maieutique-seulement.md"
cas go-audit-seulement-autorise-audit "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-audit-seulement.md"

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
d="$(copie_m lanceur-pilote3)"; sed -i "s/lanceur : lancer_pilote2_gemini_v5_2_v5.sh, sha256 $H_M\$/lanceur : lancer_courses_question_v12.sh, sha256 $H/" "$d/LANCEMENT.md"; refaire_empreintes "$d"
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

# v14 : les cas de la porte « course v6.2 précédente » (v62-*, VSC, copies de la v6.2) sont retirés : la porte n'existe plus dans le
#   lanceur v12 (PRECEDENTE_V62 sans effet : essayé sur sain-maieutique, et en réel par reel-sans-reference, sans elle)
d="$(copie_m graine-vide)"; extrait_altere "$d" 'x["manifeste"]["entropie_seed_sequence"] = None'; refaire_empreintes "$d"
cas m-graine-vide "graine de M au manifeste illisible ou vide (None)" -- MODE=simulation "${SAIN[@]}" REFERENCE_M="$d"

echo "== mode réel (copie du dépôt sous /root) : clés du pilote 4 refusées juste après le case ; GO_ID exigé ; sans PRECEDENTE_V62, refus à l'étape (0), avant tout appel =="
REEL_BASE=(MODE=reel PILOTE_RACINE=- DEPOT="$DEPOT_ROOT" "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai)
cas reel-cle-ancienne-v6-2 "COURSE=v6-2 : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- "${REEL_BASE[@]}" COURSE=v6-2
cas reel-cle-ancienne-v6-2-s "COURSE=v6-2-s : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- "${REEL_BASE[@]}" COURSE=v6-2-s
cas reel-sans-go-id "GO_ID=identifiant du GO de la course, donné par session-depot" -- "${REEL_BASE[@]}" GO_ID=
cas reel-go-id-forme "GO_ID doit être de la forme GO-AAAA-MM-JJ-NN : « GO-26-05 »" -- "${REEL_BASE[@]}" GO_ID=GO-26-05
cas reel-journal-garde-essai "variable ESSAI_JOURNAL_GARDE définie en mode réel" -- "${REEL_BASE[@]}" ESSAI_JOURNAL_GARDE=/var/tmp/x
REEL=("${REEL_BASE[@]}" COURSE=maieutique)
cas reel-sans-reference "REFERENCE_M non défini" -- "${REEL[@]}"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"
cas reel-sans-reference-audit "REFERENCE_M non défini" -- "${REEL_BASE[@]}" COURSE=audit
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
cas reel-reference-tentative-simulee "M n a pas tourné en réel" -- "${REEL[@]}" COURSE=audit REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"
rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes" "$RR"

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
cas course-inconnue "COURSE inconnue : autre (maieutique ou audit)" -- MODE=simulation COURSE=autre
cas course-du-second-pilote "COURSE inconnue : structure (maieutique ou audit)" -- MODE=simulation COURSE=structure
cas cle-ancienne-refusee "COURSE=v6-2-s : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- MODE=simulation COURSE=v6-2-s
cas cle-ancienne-refusee-v6-2 "COURSE=v6-2 : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- MODE=simulation COURSE=v6-2
cas go-id-forme "GO_ID doit être de la forme GO-AAAA-MM-JJ-NN : « 05 »" -- MODE=simulation GO_ID=05
( exec -a "python3 -m essaim_m3 lancer --decalage-uid 900 --factice" sleep 30 ) & VOISIN=$!
sleep 0.3
cas voisine-meme-decalage "tourne déjà au décalage d'utilisateurs 900" -- MODE=simulation "${SAIN[@]}"
kill "$VOISIN" 2>/dev/null; wait "$VOISIN" 2>/dev/null

echo "== R3 : verrou et marqueur de départ (noms des courses) =="
mkdir -p "$E/racine-verrou/.verrou-course-maieutique-gemini-v6-2-v1"
cas verrou-present "verrou $E/racine-verrou/.verrou-course-maieutique-gemini-v6-2-v1 présent" -- MODE=simulation COURSE=maieutique PILOTE_RACINE="$E/racine-verrou" "${SAIN[@]}"
mkdir -p "$E/racine-marqueur/.partis"; printf 'ailleurs\n' > "$E/racine-marqueur/.partis/course-maieutique-gemini-v6-2-v1"
cas marqueur-present "marqueur de départ $E/racine-marqueur/.partis/course-maieutique-gemini-v6-2-v1 présent" -- MODE=simulation PILOTE_RACINE="$E/racine-marqueur" "${SAIN[@]}"

echo "== code et commits : chemins permis après 9beee10b (noyau attendu) =="
cas commit-question "absent du dépôt" -- MODE=simulation ESSAI_ARTEFACT=commit "${SAIN[@]}"
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/hors-pieces.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/hors-pieces.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : fichier hors des pièces"
cas commit-hors-pieces "commits postérieurs à 9beee10b hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
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
cas commit-banque-v4 "commits postérieurs à 9beee10b hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/banque/banque-autre-v1.json"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/banque-autre-v1.json; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : autre fichier de la banque"
cas commit-banque-autre "commits postérieurs à 9beee10b hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/prereg/pilote4-autre-texte-v1.md"
git -C "$DEPOT" add essaim-m3-refonte-v1/prereg/pilote4-autre-texte-v1.md; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : texte non permis"
cas commit-texte-non-permis "commits postérieurs à 9beee10b hors des pièces du pilote" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1

echo "== texte (un texte pour les deux courses : graine de la course, ligne de l'autre course exigée, lanceur cité, marqueurs) =="
cas texte-graine-autre-course-maieutique "n'est pas écrite dans le texte scellé" -- MODE=simulation COURSE=maieutique GRAINE="$G_A" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}"
cas texte-graine-autre-course-audit "n'est pas écrite dans le texte scellé" -- MODE=simulation COURSE=audit GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}"
cas texte-graine-hors-entropie-maieutique "≠ celle de SeedSequence(E).spawn(2)[0]" -- MODE=simulation COURSE=maieutique GRAINE=13 TEXTE="$E/entrees/prereg-graine-hors-entropie.md" TEXTE_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-graine-hors-entropie.md.sha256")" "${SAIN[@]}"
cas texte-graine-hors-entropie-audit "≠ celle de SeedSequence(E).spawn(2)[1]" -- MODE=simulation COURSE=audit GRAINE=13 TEXTE="$E/entrees/prereg-graine-hors-entropie.md" TEXTE_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-graine-hors-entropie.md.sha256")" "${SAIN[@]}"
cas texte-sans-ligne-de-l-autre-course "la ligne « graine de la course audit = … » est absente du texte" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-une-ligne.md" TEXTE_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-une-ligne.md.sha256")" "${SAIN[@]}"
cas texte-lanceur-source "ne cite pas l'empreinte de ce lanceur" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-lanceur-source.md" TEXTE_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-lanceur-source.md.sha256")" "${SAIN[@]}"
cas texte-marqueur "marqueurs <<…>> restants" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-marqueur.md" TEXTE_SHA256="$(cut -d' ' -f1 < "$E/entrees/prereg-marqueur.md.sha256")" "${SAIN[@]}"
cas texte-empreinte "empreinte du texte ≠ TEXTE_SHA256" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256=0000 "${SAIN[@]}"

echo "== objets et question servie (question de base ; annexes de la course « audit ») =="
cas organisme-maieutique "empreinte d'arbre de l'organisme ≠ 4f13647a…" -- MODE=simulation COURSE=maieutique ESSAI_ARTEFACT=organisme "${SAIN[@]}"
cas organisme-audit "empreinte d'arbre de l'organisme ≠ 4f13647a…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=organisme "${SAIN[@]}"
cas nombre-maieutique "fichiers au lieu de 26" -- MODE=simulation COURSE=maieutique ESSAI_ARTEFACT=nombre "${SAIN[@]}"
cas nombre-audit "fichiers au lieu de 26" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=nombre "${SAIN[@]}"
cas question-empreinte-autre "empreinte de la question ≠ 00000000…" -- MODE=simulation ESSAI_ARTEFACT=question-base "${SAIN[@]}"
cas question-empreinte-autre-audit "empreinte de la question ≠ 00000000…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question-base "${SAIN[@]}"
cas question-servie-alteree "empreinte de la question servie ≠" -- MODE=simulation ESSAI_ARTEFACT=question "${SAIN[@]}"
cas question-servie-alteree-audit "empreinte de la question servie ≠" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question "${SAIN[@]}"
cas question-v1-refusee "empreinte de la question ≠ 998960b8…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question-v1 "${SAIN[@]}"
cas question-v2-refusee "empreinte de la question ≠ 998960b8…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question-v2 "${SAIN[@]}"
cas annexe-empreinte-fausse "empreinte de l'annexe 1 ($ANNEXE_DEF_CHEMIN) ≠ 01234567…" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_COMMIT="$COMMIT_DEF" ESSAI_ANNEXE_1_CHEMIN="$ANNEXE_DEF_CHEMIN" ESSAI_ANNEXE_1_SHA=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef   # l'annexe réelle, une empreinte fausse : refus avant tout appel
verifier_absent annexe-empreinte-fausse-sans-course "$E/cas-annexe-empreinte-fausse/course-audit-gemini-v6-2-v1/course"   # aucun appel : le noyau n'est jamais parti
verifier_absent annexe-empreinte-fausse-sans-manifeste "$E/cas-annexe-empreinte-fausse/course-audit-gemini-v6-2-v1/course/manifeste-run.json"
cas annexe-absente "annexe 1 (docs/nulle-part-v1.md) absente du commit" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=annexe-absente "${SAIN[@]}"
cas annexe-alteree "empreinte de l'annexe 1 ($ANNEXE_ESSAI_CHEMIN) ≠ 00000000…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=annexe "${SAIN[@]}"
cas annexe-champs-incomplets "ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN et ESSAI_ANNEXE_1_SHA vont ensemble" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_SHA=
cas annexe-commit-absent "annexe 1 : commit 0123456789abcdef0123456789abcdef01234567 absent du dépôt" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_COMMIT=0123456789abcdef0123456789abcdef01234567
cas question-servie-trop-longue "caractères > 100000 (borne du noyau 9beee10b, essaim_m3/noyau/question.py, CARACTERES_MAX_QUESTION)" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_COMMIT="$ANNEXE_LONGUE_COMMIT" ESSAI_ANNEXE_1_CHEMIN="$ANNEXE_LONGUE_CHEMIN" ESSAI_ANNEXE_1_SHA="$ANNEXE_LONGUE_SHA"
cas audit-sans-annexe-reserve "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=annexe-vide "${SAIN[@]}"   # emplacement 1 vidé par l'artefact : la course part, RÉSERVE consignée
verifier audit-sans-annexe-reserve-ligne "RÉSERVE : course « audit » sans aucune annexe servie" "$E/cas-audit-sans-annexe-reserve"/*/LANCEMENT.md
verifier audit-sans-annexe-question-servie "question servie : question.md, sha256 $Q_A, 3430 caractères" "$E/cas-audit-sans-annexe-reserve"/*/LANCEMENT.md
cas annexe-artefacts-sans-effet-maieutique "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique ESSAI_ARTEFACT=annexe "${SAIN[@]}"
cas reel-annexe-essai "variable ESSAI_ANNEXE_1_COMMIT définie en mode réel" -- MODE=reel PILOTE_RACINE=- COURSE=audit ESSAI_ANNEXE_1_COMMIT=x ESSAI_ANNEXE_1_CHEMIN=x ESSAI_ANNEXE_1_SHA=x

echo "== registres (un GO par course : GO-2026-10-26-05 « maieutique », GO-2026-10-26-04 « audit » ; dépense) =="
cas go-sans-calcul "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-calcul.md"
cas go-autre-id "aucune ligne « | GO-2026-10-26-05 | »" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-id.md"
cas go-maieutique-seulement-refuse-audit "aucune ligne « | GO-2026-10-26-04 | »" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-maieutique-seulement.md"
cas go-audit-seulement-refuse-maieutique "aucune ligne « | GO-2026-10-26-05 | »" -- MODE=simulation COURSE=maieutique "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-audit-seulement.md"
cas go-autre-question "l'empreinte de la question 1d29fbec…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"
cas go-autre-question-audit "l'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"
cas go-questions-croisees "l'empreinte de la question 1d29fbec…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-questions-croisees.md"
cas go-questions-croisees-audit "l'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-questions-croisees.md"
cas go-question-v1-refuse-audit "l'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-question-v1.md"
cas go-question-v2-refuse-audit "l'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-question-v2.md"
cas go-sans-texte "celle du texte scellé ($T16)" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-texte.md"
cas depense-absente "lancement non consigné avant dans registres/depenses.md (une ligne nommant course-maieutique-gemini-v6-2-v1 et GO-2026-10-26-05)" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-absente.md"
cas depense-ancienne-forme "lancement non consigné avant dans registres/depenses.md (une ligne nommant course-maieutique-gemini-v6-2-v1 et GO-2026-10-26-05)" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-ancienne-forme.md"
cas depense-ancienne-forme-audit "une ligne nommant course-audit-gemini-v6-2-v1 et GO-2026-10-26-04" -- MODE=simulation COURSE=audit "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-ancienne-forme.md"
cas reste-insuffisant "< $USD_COURSE" -- MODE=simulation "${SAIN[@]}" RESTE_GO_USD="$SOUS_PLAFOND"

echo "== test de dépense (le GO de la course) =="
cas td-autre-go "go = 'GO-2026-10-25-01' (attendu GO-2026-10-26-05)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-autre-go.json"
cas td-autre-go-audit "go = 'GO-2026-10-26-05' (attendu GO-2026-10-26-04)" -- MODE=simulation COURSE=audit "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-go-maieutique.json"
cas td-echec "CLAUDE_FABLE_5_1 : statut 'ECHEC_API'" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-echec.json"
cas td-heure-absente-exigee "heure_utc absente (exigée en réel)" -- MODE=simulation "${SAIN[@]}" ESSAI_EXIGER_HEURE=1
cas td-vieux "> 900 s" -- MODE=simulation ESSAI_ARTEFACT=appel-vieux "${SAIN[@]}"
td_noms "$E/entrees/td-noms-conformes.json" RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 GO-2026-10-26-05
cas td-noms-conformes "noms des variables du test : anthropic RR_ANTHROPIC_API_KEY_3, gemini GEMINI_API_KEY_2" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-conformes.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2
td_noms "$E/entrees/td-noms-autres.json" RR_ANTHROPIC_API_KEY GEMINI_API_KEY GO-2026-10-26-05
cas td-noms-autres "noms des variables du test : anthropic = 'RR_ANTHROPIC_API_KEY' (attendu RR_ANTHROPIC_API_KEY_3)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-autres.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2

echo "== essais du noyau =="
cas junit-echec "échecs" -- MODE=simulation ESSAI_ARTEFACT=junit-echec "${SAIN[@]}"
cas junit-total "essais au lieu de 169" -- MODE=simulation ESSAI_ARTEFACT=junit-total "${SAIN[@]}"

echo "== environnement du noyau et passerelle =="
cas env-noyau-nu "environnement du noyau (noms seulement, valeurs jamais écrites) : PATH HOME LANG PYTHONDONTWRITEBYTECODE ESSAIM_M3_CACHER ." -- MODE=simulation "${SAIN[@]}" HF_TOKEN=factice VAST_API_KEY=factice ANTHROPIC_API_KEY=factice
cas passerelle-saine "passerelle de sortie, sous l'environnement du noyau sans clé : httpx" -- MODE=simulation "${SAIN[@]}" ESSAI_PASSERELLE_PY="$PY_HTTPX" "${INFRA[@]}"
cas passerelle-sans-certificat "passerelle de sortie injoignable sous l'environnement du noyau : httpx, api.anthropic.com : ConnectError" -- MODE=simulation "${SAIN[@]}" ESSAI_PASSERELLE_PY="$PY_HTTPX"

echo "== après le départ =="
cas famille-puis-tentatives "aucune course partie (pas de manifeste" -- MODE=simulation COURSE=maieutique ESSAI_ARTEFACT=famille "${SAIN[@]}"
R_F="$E/cas-famille-puis-tentatives"
cas tentative-2 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique TENTATIVE=2 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas tentative-3 "R3 : jamais de seconde course" -- MODE=simulation COURSE=maieutique TENTATIVE=3 PILOTE_RACINE="$R_F" "${SAIN[@]}"
cas archive-incomplete "ARCHIVE FERMÉE INCOMPLÈTE" -- MODE=simulation ESSAI_ARTEFACT=archive "${SAIN[@]}"
cas imprevu "fichiers imprévus, NON poussés" -- MODE=simulation ESSAI_ARTEFACT=imprevu "${SAIN[@]}"
echo "== lanceur v4 (contre-lecture 1 du pilote 4) : banque autre que la v3 (P4C1-06) ; minuteur (P4C1-02) =="
cas banque-crochet "empreinte de la banque ≠ 157a2b45…" -- MODE=simulation ESSAI_ARTEFACT=banque "${SAIN[@]}"
cp "$DEPOT/essaim-m3-refonte-v1/banque/banque-confrontation-v2.json" "$DEPOT/essaim-m3-refonte-v1/banque/banque-confrontation-v3.json"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/banque-confrontation-v3.json; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : banque v2 copiée au chemin de la v3"
cas banque-v2-au-chemin-v3 "empreinte de la banque ≠ 157a2b45…" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
echo "== lanceur v5 : reprise par segments (décision de Lazar, 25 octobre 2026, 20:23 Paris) =="
verifier_absent() {  # verifier_absent NOM CHEMIN : le chemin ne doit pas exister
  n=$((n + 1))
  if [ ! -e "$2" ]; then ok=$((ok + 1)); echo "OK     $1 : $2 absent"; else echo "ÉCHEC  $1 : $2 présent"; fi
}
verifier_re() {  # verifier_re NOM REGEX FICHIER… : expression régulière étendue cherchée dans l'un des fichiers
  local nom="$1" motif="$2"; shift 2
  n=$((n + 1))
  if cat "$@" 2>/dev/null | grep -qE -- "$motif"; then ok=$((ok + 1)); echo "OK     $nom : /$motif/"
  else echo "ÉCHEC  $nom : attendu /$motif/"; fi
}
releve_segments() {  # releve_segments DOSSIER_DU_PILOTE → « arrêts […] reprises […] générations […] » (extrait mécanique)
  "$PY" -I -c '
import json, sys
x = json.load(open(sys.argv[1] + "/extrait-mecanique-v1.json", encoding="utf-8"))
ev = x.get("evenements", [])
print("arrêts", [e.get("raison") for e in ev if e.get("etape") == "arret"], "reprises", [e.get("segment") for e in ev if e.get("etape") == "reprise"],
      "générations", sorted(g.get("generation") for g in x.get("generations", []) if not g.get("phase")))' "$1"
}
copie_ps() {  # copie_ps NOM → chemin d'une copie de la v6.2 en segments
  local d="$E/ps-alteree-$1/course-maieutique-gemini-v6-2-v1"; rm -rf "$E/ps-alteree-$1"; mkdir -p "$E/ps-alteree-$1"; cp -a "$PS" "$d"; echo "$d"
}
td_heure "$E/entrees/td-seg-1.json" 0 GO-2026-10-26-05
SEG=(MODE=simulation COURSE=maieutique GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-seg-1.json" ESSAI_EXIGER_HEURE=1)
{ cat "$E/entrees/dep-sain.md"
  printf '| 2026-10-25 | course-maieutique-gemini-v6-2-v1 segment 2 | GO-2026-10-26-05 | au plus 75 USD moins la dépense déjà faite | après le segment 1 |\n'
  printf '| 2026-10-25 | course-maieutique-gemini-v6-2-v1 segment 3 | GO-2026-10-26-05 | au plus 75 USD moins la dépense déjà faite | après le segment 2 |\n'; } > "$E/entrees/dep-segments.md"

echo "-- valeurs de SEGMENT et de CLORE ; course absente ou fermée --"
cas seg-non-entier "SEGMENT doit être un entier ≥ 1, sans zéro en tête : « deux »" -- MODE=simulation SEGMENT=deux
cas seg-zero "sans zéro en tête : « 0 »" -- MODE=simulation SEGMENT=0
cas seg-zero-en-tete "sans zéro en tête : « 02 »" -- MODE=simulation SEGMENT=02
cas clore-au-segment-1 "CLORE=1 ferme une course arrêtée entre deux segments : SEGMENT ≥ 2 exigé" -- MODE=simulation CLORE=1
cas clore-valeur "CLORE vaut 1 ou rien : « oui »" -- MODE=simulation SEGMENT=2 CLORE=oui
cas seg-sans-course "absent (aucune course à reprendre" -- "${SEG[@]}" SEGMENT=2
cas seg-course-fermee "est déjà fermée" -- MODE=simulation COURSE=maieutique "${SAIN[@]}" SEGMENT=2 PILOTE_RACINE="$E/cas-sain-maieutique"

echo "-- segment 1 arrêté par le minuteur (échéance 0 : STOP dès le manifeste) --"
cas seg-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${SEG[@]}" ESSAI_ECHEANCE_STOP_S=0
RS="$E/cas-seg-segment1"; PS="$RS/course-maieutique-gemini-v6-2-v1"
verifier seg-segment1-minuteur "état de reprise attendu" "$PS/LANCEMENT.md"
verifier seg-segment1-etat "état de reprise écrit par le noyau : etat-v1.json" "$PS/LANCEMENT.md"
verifier seg-segment1-sortie "rien à pousser avant la fin de la course" "$RS/sortie.txt"
verifier_absent seg-segment1-ouverte "$PS/ferme.tar.gz"
verifier_absent seg-segment1-rien-pousse "$PS/A-POUSSER-v1.txt"

echo "-- segment 2 refusé sur artefacts (la course reste arrêtée, ouverte) --"
cas seg-hors-ordre "le LANCEMENT.md n'attend pas ce segment" -- "${SEG[@]}" SEGMENT=3 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
cas seg-sans-ligne-de-depense "segment 2 non consigné avant dans registres/depenses.md" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS"
cas seg-reste-insuffisant "reste sur GO-2026-10-26-05 = 0.01 USD <" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" RESTE_GO_USD=0.01
mkdir "$RS/.verrou-course-maieutique-gemini-v6-2-v1-segment2"
cas seg-verrou-du-segment "verrou $RS/.verrou-course-maieutique-gemini-v6-2-v1-segment2 présent" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
rmdir "$RS/.verrou-course-maieutique-gemini-v6-2-v1-segment2"
cp -p "$RS/.partis/course-maieutique-gemini-v6-2-v1" "$E/marqueur-sauve"; printf 'ailleurs 2026-10-25T00:00:00Z\n' > "$RS/.partis/course-maieutique-gemini-v6-2-v1"
cas seg-marqueur-autre "absent ou d'un autre dossier (R3)" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
cp -p "$E/marqueur-sauve" "$RS/.partis/course-maieutique-gemini-v6-2-v1"
printf 'x\n' > "$DEPOT/essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/piece-essai-entre-segments.txt"
git -C "$DEPOT" add essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/piece-essai-entre-segments.txt; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : commit entre deux segments"
cas seg-head-deplace "HEAD du dépôt ≠ celui du segment 1" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
git -C "$DEPOT" reset -q --hard HEAD~1
cp "$LANCEUR" "$E/lanceur-modifie.sh"; printf '\n# copie modifiée (essai)\n' >> "$E/lanceur-modifie.sh"
LANCEUR_SAIN="$LANCEUR"; LANCEUR="$E/lanceur-modifie.sh"
cas seg-autre-lanceur "n'est pas celui du segment 1" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
LANCEUR="$LANCEUR_SAIN"
c="$PS/course/reprise/etat-v1.json.sha256"; cp -p "$c" "$E/etat-v1-sauve.sha256"; printf '%064d  etat-v1.json\n' 0 > "$c"
cas seg-etat-altere "état de reprise du segment 1 non conforme (etat-v1.json : compagnon absent ou différent)" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
cp -p "$E/etat-v1-sauve.sha256" "$c"
# v8 (contre-lecture 3, P4C3-03) : gardes du segment K ≥ 2 sur artefacts — course sans manifeste, verrou du segment 1
#   absent, autre course de ce nom partie, état de reprise d'un autre arrêt ou d'un autre segment (rescellé) ; chaque
#   artefact retiré après son cas, l'état restauré à l'octet près
mv "$PS/course/manifeste-run.json" "$E/manifeste-ps-sauve.json"
cas seg-sans-manifeste "SEGMENT=2 : aucune course partie dans $PS" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
mv "$E/manifeste-ps-sauve.json" "$PS/course/manifeste-run.json"
mv "$RS/.verrou-course-maieutique-gemini-v6-2-v1" "$E/verrou-segment1-sauve"
cas seg-verrou-segment1-absent "verrou $RS/.verrou-course-maieutique-gemini-v6-2-v1 du segment 1 absent" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
mv "$E/verrou-segment1-sauve" "$RS/.verrou-course-maieutique-gemini-v6-2-v1"
mkdir -p "$RS/course-maieutique-gemini-v6-2-v1-essai-autre/course"; printf '{}\n' > "$RS/course-maieutique-gemini-v6-2-v1-essai-autre/course/manifeste-run.json"
cas seg-autre-course-du-nom "une autre course de ce nom est partie dans $RS/course-maieutique-gemini-v6-2-v1-essai-autre (R3)" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
rm -rf "$RS/course-maieutique-gemini-v6-2-v1-essai-autre"
e1="$PS/course/reprise/etat-v1.json"; cp -p "$e1" "$E/etat-v1-sauve.json"; cp -p "$e1.sha256" "$E/etat-v1-sauve-b.sha256"
etat_altere() {  # etat_altere CODE_PYTHON (x = l'état v1) : l'état modifié, puis rescellé (compagnon juste)
  "$PY" -I -c 'import json, sys
p = sys.argv[1]
x = json.load(open(p, encoding="utf-8"))
exec(sys.argv[2])
open(p, "w", encoding="utf-8").write(json.dumps(x, ensure_ascii=False, indent=1))' "$e1" "$1"
  (cd "$PS/course/reprise" && sha256sum etat-v1.json > etat-v1.json.sha256)
}
etat_altere 'x["raison_arret"] = "aucune lignée active"'
cas seg-etat-autre-arret "etat-v1.json : arrêt autre que STOP ('aucune lignée active')" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
cp -p "$E/etat-v1-sauve.json" "$e1"; cp -p "$E/etat-v1-sauve-b.sha256" "$e1.sha256"
etat_altere 'x["segment"] = 5'
cas seg-etat-autre-segment "etat-v1.json : état du segment 5, attendu 1" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
cp -p "$E/etat-v1-sauve.json" "$e1"; cp -p "$E/etat-v1-sauve-b.sha256" "$e1.sha256"
(cd "$PS/course/reprise" && sha256sum etat-v1.json) > "$E/etat-v1-restaure.txt"
verifier seg-etat-restaure "$(cut -d' ' -f1 < "$E/etat-v1-sauve-b.sha256")  etat-v1.json" "$E/etat-v1-restaure.txt"
cp -p "$PS/organisme/principal.py" "$E/principal-sauve.py"
cas seg-organisme-modifie "empreinte d'arbre de l'organisme ≠ 4f13647a…" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ARTEFACT=organisme
cp -p "$E/principal-sauve.py" "$PS/organisme/principal.py"
cp -p "$PS/question.md" "$E/question-sauve.md"
cas seg-question-modifiee "empreinte de la question servie ≠" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ARTEFACT=question
cp -p "$E/question-sauve.md" "$PS/question.md"
j="$PS/course/evenements.jsonl"; cp -p "$j" "$E/journal-sauve.jsonl"; printf '{"etape": "intrus"}\n' >> "$j"
td_heure "$E/entrees/td-seg-2a.json" 0 GO-2026-10-26-05
cas seg-noyau-refuse "reprise refusée par le noyau (code 9" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" APPEL_CONTROLE_FICHIER="$E/entrees/td-seg-2a.json"
verifier seg-noyau-refuse-motif "la course a bougé depuis l'état" "$PS"/segment-2-t*/sortie-erreur-lanceur.txt
verifier seg-noyau-refuse-code "reprise refusée par le noyau" "$E/cas-seg-noyau-refuse/sortie.txt"
verifier_absent seg-noyau-refuse-ouverte "$PS/ferme.tar.gz"
cp -p "$E/journal-sauve.jsonl" "$j"

echo "-- segment 2 sain : la course va au bout et se ferme --"
td_heure "$E/entrees/td-seg-2.json" 0 GO-2026-10-26-05
cas seg-segment2 "archive fermée : ferme.tar.gz" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" APPEL_CONTROLE_FICHIER="$E/entrees/td-seg-2.json"
verifier_re seg-segment2-entete "^## Segment 2, essai [0-9]+ \(simulation, tentative 1\)$" "$PS/LANCEMENT.md"
verifier seg-segment2-etat-relu "état de reprise : etat-v1.json, sha256" "$PS/LANCEMENT.md"
verifier seg-segment2-stop-retire "STOP du segment 1 retiré de course/ (reprise)" "$PS/LANCEMENT.md"
verifier seg-segment2-depart "; segment 2, reprise de la course" "$PS/LANCEMENT.md"
verifier seg-segment2-depense "dépense consignée avant (segment 2)" "$PS/LANCEMENT.md"
verifier seg-segment2-essais "essais : 169 passés, 0 sauté, 0 désélectionnés" "$PS/LANCEMENT.md"
verifier_re seg-segment2-pousse-registre "^segment-2-t[0-9]+/registre-go\.md$" "$PS/A-POUSSER-v1.txt"
verifier_re seg-segment2-pousse-essais "^segment-2-t[0-9]+/essais-v1\.txt$" "$PS/A-POUSSER-v1.txt"
verifier_re seg-segment2-pousse-erreur "^segment-2-t[0-9]+/sortie-erreur-lanceur\.txt\.sha256$" "$PS/A-POUSSER-v1.txt"
verifier_re seg-segment2-pousse-td "^segment-2-t[0-9]+/test-depense-td-seg-2\.json$" "$PS/A-POUSSER-v1.txt"
verifier seg-segment2-pousse-archive "ferme.tar.gz" "$PS/A-POUSSER-v1.txt"
releve_segments "$PS" > "$E/releve-segments-ps.txt" 2>&1
verifier seg-segment2-extrait "arrêts ['fichier STOP', 'aucune lignée active'] reprises [2] générations [0, 1, 2, 3]" "$E/releve-segments-ps.txt"
cas seg-apres-fermeture "est déjà fermée" -- "${SEG[@]}" SEGMENT=3 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"

# v14 : la porte « course v6.2 précédente » sur la course en segments (seg-v6-2-s-porte-saine, seg-v62-*) est retirée avec la porte

echo "-- trois segments (états de reprise v1 et v2) --"
td_heure "$E/entrees/td-seg3-1.json" 0 GO-2026-10-26-05
cas seg3-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${SEG[@]}" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-seg3-1.json"
R3S="$E/cas-seg3-segment1"; P3S="$R3S/course-maieutique-gemini-v6-2-v1"
td_heure "$E/entrees/td-seg3-2.json" 0 GO-2026-10-26-05
cas seg3-segment2 "segment 2 arrêté par STOP ; reprise attendue : SEGMENT=3" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$R3S" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-seg3-2.json"
verifier seg3-etat-v2 "état de reprise écrit par le noyau : etat-v2.json" "$P3S/LANCEMENT.md"
td_heure "$E/entrees/td-seg3-3.json" 0 GO-2026-10-26-05
cas seg3-segment3 "archive fermée : ferme.tar.gz" -- "${SEG[@]}" SEGMENT=3 PILOTE_RACINE="$R3S" DEPENSES_SOURCE="$E/entrees/dep-segments.md" APPEL_CONTROLE_FICHIER="$E/entrees/td-seg3-3.json"
verifier seg3-etat-relu "état de reprise : etat-v2.json, sha256" "$P3S/LANCEMENT.md"
releve_segments "$P3S" > "$E/releve-segments-p3s.txt" 2>&1
verifier seg3-extrait "arrêts ['fichier STOP', 'fichier STOP', 'aucune lignée active'] reprises [2, 3] générations [0, 1, 2, 3]" "$E/releve-segments-p3s.txt"

echo "-- fermeture sans reprise (CLORE=1) --"
td_heure "$E/entrees/td-clore-1.json" 0 GO-2026-10-26-05
cas seg-clore-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${SEG[@]}" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-clore-1.json"
RC="$E/cas-seg-clore-segment1"; PC="$RC/course-maieutique-gemini-v6-2-v1"
cas seg-clore "CLORE=1 : aucune reprise, aucun appel" -- MODE=simulation COURSE=maieutique GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" REFERENCE_M="$M_REF" SEGMENT=2 CLORE=1 PILOTE_RACINE="$RC"
verifier seg-clore-entete "fermeture sans reprise (CLORE=1)" "$PC/LANCEMENT.md"
verifier seg-clore-archive "archive fermée : ferme.tar.gz" "$PC/LANCEMENT.md"
verifier seg-clore-pousse "ferme.tar.gz" "$PC/A-POUSSER-v1.txt"
verifier_absent seg-clore-sans-essais "$PC/segment-2-t1/essais-v1.txt"
releve_segments "$PC" > "$E/releve-segments-pc.txt" 2>&1
verifier seg-clore-extrait "arrêts ['fichier STOP'] reprises []" "$E/releve-segments-pc.txt"
cas minuteur-echeance-non-entiere "ESSAI_ECHEANCE_STOP_S doit être un entier (secondes)" -- MODE=simulation ESSAI_ECHEANCE_STOP_S=abc "${SAIN[@]}"
cas reel-echeance-minuteur "variable ESSAI_ECHEANCE_STOP_S définie en mode réel" -- MODE=reel PILOTE_RACINE=- ESSAI_ECHEANCE_STOP_S=5
echo "-- minuteur au segment K ≥ 2 : copie mutée du lanceur (STOP posé sans attendre la reprise consignée) — la reprise est refusée (P4C3-03) --"
"$PY" -I -c 'import sys
t = open(sys.argv[1], encoding="utf-8").read()
a = "else [ \"$(wc -l < \"$PILOTE/course/evenements.jsonl\")\" -gt \"$N_EV_AVANT\" ]; fi"
assert t.count(a) == 1, t.count(a)
open(sys.argv[2], "w", encoding="utf-8").write(t.replace(a, "else true; fi  # MUTATION (essai) : STOP posé sans attendre la reprise"))' "$LANCEUR" "$E/lanceur-mutant-minuteur.sh"
H_MUT="$(sha256sum "$E/lanceur-mutant-minuteur.sh" | cut -d' ' -f1)"
pr "$E/entrees/prereg-mutant.md" "entropie E = $ENTROPIE tirée au scellement
graine de la course maieutique = $G_M
graine de la course audit = $G_A
lanceur $H_MUT"
SHA_PRM="$(cut -d' ' -f1 < "$E/entrees/prereg-mutant.md.sha256")"
{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "${SHA_PRM:0:16}"; ligne_go GO-2026-10-26-04 audit "$Q_A" "${SHA_PRM:0:16}"; } > "$E/entrees/go-mutant.md"
MUT=("${SEG[@]}" TEXTE="$E/entrees/prereg-mutant.md" TEXTE_SHA256="$SHA_PRM" REGISTRE_GO_SOURCE="$E/entrees/go-mutant.md")
LANCEUR_SAIN="$LANCEUR"; LANCEUR="$E/lanceur-mutant-minuteur.sh"
td_heure "$E/entrees/td-mut-1.json" 0 GO-2026-10-26-05
cas mut-minuteur-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${MUT[@]}" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-mut-1.json"
RMU="$E/cas-mut-minuteur-segment1"; PMU="$RMU/course-maieutique-gemini-v6-2-v1"
td_heure "$E/entrees/td-mut-2.json" 0 GO-2026-10-26-05
cas mut-minuteur-segment2 "reprise refusée par le noyau (code 9" -- "${MUT[@]}" SEGMENT=2 PILOTE_RACINE="$RMU" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-mut-2.json"
verifier mut-minuteur-motif "le fichier STOP est encore dans la course" "$PMU"/segment-2-t*/sortie-erreur-lanceur.txt
LANCEUR="$LANCEUR_SAIN"
echo "== garde refus-question (R5) : journaux synthétiques lus par le veilleur (ESSAI_JOURNAL_GARDE) ; règle de conv-audit du 26 octobre 2026 : cas sains (dont le motif réel de g001 de la course M), artefacts =="
journal_garde() {  # journal_garde FICHIER MOTIF… : journal synthétique ; MOTIF = ROLE[:STATUT[:FIN]][*N] (OK end_turn par défaut ; REFUS vaut fin refusal ; *N répète) ; identifiants organisme-0001, 0002, …
  "$PY" -I -c '
import json, re, sys
f, motifs = sys.argv[1], sys.argv[2:]
def ligne(i, r, st="OK", fi=None):
    fi = fi if fi is not None else ("refusal" if st == "REFUS" else "end_turn")
    return {"id": "organisme-%04d" % i, "etape": "organisme", "role": r, "espece": "CLAUDE_FABLE_5_1", "famille": "anthropic", "modele_demande": "claude-fable-5-1", "modele_servi": "claude-fable-5-1", "statut": st, "fin": fi, "categorie": None, "usage": {"entree": 10, "sortie": 10}, "cout_usd": 0.0001, "cumul_usd": 0.0001 * i, "angle": None, "max_tokens": 8192, "sha256_prompt": "0" * 64, "sha256_texte": "0" * 64, "caracteres": 10, "debut_utc": "2026-10-26T12:00:00.000000Z", "fin_utc": "2026-10-26T12:00:01.000000Z", "echec": None, "reel": False, "go_id": None, "types_blocs": ["text"]}
lignes = []
for m in motifs:
    g = re.fullmatch(r"([A-Za-z0-9_]+)(?::([A-Z_]+)(?::([A-Za-z_]+))?)?(?:\*(\d+))?", m)
    if not g: sys.exit("motif illisible : " + m)
    for _ in range(int(g.group(4) or 1)):
        lignes.append(ligne(len(lignes) + 1, g.group(1), g.group(2) or "OK", g.group(3)))
open(f, "w", encoding="utf-8").write("".join(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n" for l in lignes))' "$@"
}
suite_journal() {  # suite_journal JOURNAL : les lignes « rôle statut fin » d'un journal, pour comparer un journal synthétique au journal réel
  "$PY" -I -c 'import json, sys; print("".join(" ".join(str(e[k]) for k in ("role", "statut", "fin")) + "\n" for e in map(json.loads, open(sys.argv[1], encoding="utf-8"))), end="")' "$1"
}
# motif réel de g001 de la course M du pilote 4 (journal-appels-g001.jsonl poussé, fec0cb8237e325a8bf0d493d681082b4b9d89924dc9ddfa21e390e4d05953bc5, 129 appels : 120 appels de tâche
# monoculture_analytique dont cinq en REFUS, l'appel moissonneur_formulation_requetes, puis les cinq castes de la question, l'arbitre en REFUS) ;
# suites « rôle statut fin » : 124 premiers appels 6d2ad200…, 129 appels 7f79273d… (relevées sur le journal réel, vérifiées ci-dessous)
MOTIF_REEL_M=(inducteur_entrainement "calibrateur_interne*2" "monoculture_analytique*25" monoculture_analytique:REFUS "monoculture_analytique*16" monoculture_analytique:REFUS "monoculture_analytique*9" monoculture_analytique:REFUS "monoculture_analytique*54" monoculture_analytique:REFUS "monoculture_analytique*9" monoculture_analytique:REFUS "monoculture_analytique*2" moissonneur_formulation_requetes)
journal_garde "$E/entrees/journal-garde-sain.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique inducteur_entrainement:REFUS monoculture_analytique arbitre_synthese_contradictoire
journal_garde "$E/entrees/journal-garde-artefact.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique arbitre_synthese_contradictoire:REFUS monoculture_analytique arbitre_synthese_contradictoire
journal_garde "$E/entrees/journal-garde-fin-surete.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique critique_adversariale_limites:MODELE_NON_CONFORME:SAFETY monoculture_analytique arbitre_synthese_contradictoire
journal_garde "$E/entrees/journal-garde-tache-refusee.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique monoculture_analytique:REFUS monoculture_analytique arbitre_synthese_contradictoire   # refus de tâche au rang 3, sans moissonneur : rien
journal_garde "$E/entrees/journal-garde-critique-sans-moissonneur.jsonl" "monoculture_analytique*5" critique_adversariale_limites:REFUS monoculture_analytique
journal_garde "$E/entrees/journal-garde-apres-moissonneur.jsonl" "monoculture_analytique*10" moissonneur_formulation_requetes monoculture_analytique:REFUS monoculture_croisee
journal_garde "$E/entrees/journal-garde-rang-121.jsonl" "monoculture_analytique*120" monoculture_analytique:REFUS monoculture_croisee
journal_garde "$E/entrees/journal-garde-rang-120.jsonl" "monoculture_analytique*119" monoculture_analytique:REFUS monoculture_analytique
journal_garde "$E/entrees/journal-garde-moissonneur-refuse.jsonl" "monoculture_analytique*3" moissonneur_formulation_requetes:REFUS monoculture_analytique
journal_garde "$E/entrees/journal-garde-motif-reel-m-avant-question.jsonl" "${MOTIF_REEL_M[@]}"
journal_garde "$E/entrees/journal-garde-motif-reel-m-complet.jsonl" "${MOTIF_REEL_M[@]}" monoculture_analytique monoculture_croisee sonde_orthogonale_onsager:OK:STOP critique_adversariale_limites arbitre_synthese_contradictoire:REFUS
journal_garde "$E/entrees/journal-garde-premiere-caste-apres-moissonneur.jsonl" "${MOTIF_REEL_M[@]}" monoculture_analytique:REFUS
suite_journal "$E/entrees/journal-garde-motif-reel-m-avant-question.jsonl" | sha256sum | cut -d' ' -f1 > "$E/suite-motif-reel-m-avant-question.txt"
suite_journal "$E/entrees/journal-garde-motif-reel-m-complet.jsonl" | sha256sum | cut -d' ' -f1 > "$E/suite-motif-reel-m-complet.txt"
verifier garde-motif-reel-m-avant-question-suite "6d2ad200d3c45833933bd6f20bfc80cf6b7e0afabe0bf32f8c50ff6950173294" "$E/suite-motif-reel-m-avant-question.txt"
verifier garde-motif-reel-m-complet-suite "7f79273db464bbbb00e83372d970e93553acf1b306e60708aa95ab6d9b3b6050" "$E/suite-motif-reel-m-complet.txt"
printf '{"id": "organisme-0001", "role": "monoculture_croisee", "statut": "REFUS", "fin": "refusal"' > "$E/entrees/journal-garde-ligne-incomplete.jsonl"   # une ligne sans fin de ligne : jamais lue
cas garde-refus-question-sain "archive fermée : ferme.tar.gz" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$E/entrees/journal-garde-sain.jsonl"
D_GARDE_SAIN="$E/cas-garde-refus-question-sain/course-maieutique-gemini-v6-2-v1"
verifier garde-sain-aucun-arret "garde refus-question : aucun arrêt ; veilleur arrêté par son PID" "$D_GARDE_SAIN/LANCEMENT.md"
verifier garde-sain-journal-essai "(ESSAI : journal synthétique)" "$D_GARDE_SAIN/LANCEMENT.md"
verifier_absent_texte garde-sain-sans-ligne-d-arret "arrêt par la garde refus-question" "$D_GARDE_SAIN/LANCEMENT.md"
verifier_absent garde-sain-sans-piece "$D_GARDE_SAIN/garde-refus-question-v1.json"
cas garde-refus-question-ligne-incomplete "archive fermée : ferme.tar.gz" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$E/entrees/journal-garde-ligne-incomplete.jsonl"
verifier garde-ligne-incomplete-aucun-arret "garde refus-question : aucun arrêt" "$E/cas-garde-refus-question-ligne-incomplete"/*/LANCEMENT.md
garde_sans_arret() {  # garde_sans_arret NOM JOURNAL : la course finit d'elle-même ; aucun arrêt, aucune pièce
  local nom="$1" j="$2" d
  cas "$nom" "archive fermée : ferme.tar.gz" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$j"
  d="$E/cas-$nom/course-maieutique-gemini-v6-2-v1"
  verifier "$nom-aucun-arret" "garde refus-question : aucun arrêt ; veilleur arrêté par son PID" "$d/LANCEMENT.md"
  verifier_absent_texte "$nom-sans-ligne-d-arret" "arrêt par la garde refus-question" "$d/LANCEMENT.md"
  verifier_absent "$nom-sans-piece" "$d/garde-refus-question-v1.json"
}
garde_sans_arret garde-refus-question-tache-refusee "$E/entrees/journal-garde-tache-refusee.jsonl"   # un REFUS de tâche (monoculture_analytique, rang 3, sans moissonneur) ne fait rien
garde_sans_arret garde-refus-question-rang-120 "$E/entrees/journal-garde-rang-120.jsonl"   # le 120e appel monoculture_analytique en REFUS, sans moissonneur : encore une tâche
garde_sans_arret garde-refus-question-moissonneur-refuse "$E/entrees/journal-garde-moissonneur-refuse.jsonl"   # un moissonneur refusé n'est pas une caste de la question
garde_sans_arret garde-refus-question-motif-reel-m-avant-question "$E/entrees/journal-garde-motif-reel-m-avant-question.jsonl"   # le motif réel de la course M : cinq REFUS de tâche avant la question, aucun arrêt
garde_artefact() {  # garde_artefact NOM JOURNAL ATTENDU [ID] [REGLE] : la course est tuée par la garde ; relevés (ligne, règle, pièce poussée, pas de reprise, g001 jamais archivée, délai)
  local nom="$1" j="$2" attendu="$3" id="${4:-organisme-0004}" regle="${5:-rôle propre à la question}" d
  cas "$nom" "$attendu" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$j"
  d="$E/cas-$nom/course-maieutique-gemini-v6-2-v1"
  verifier "$nom-sans-reprise" "course fermée sans reprise" "$d/LANCEMENT.md"
  verifier "$nom-noyau-tue" ") tué, enfants directs tués par PID" "$d/LANCEMENT.md"
  verifier "$nom-archive" "archive fermée : ferme.tar.gz" "$d/LANCEMENT.md"
  verifier "$nom-piece" "garde-refus-question-v1.json" "$d/A-POUSSER-v1.txt"
  verifier "$nom-piece-compagnon" "garde-refus-question-v1.json.sha256" "$d/A-POUSSER-v1.txt"
  verifier "$nom-piece-appel" "\"id\": \"$id\"" "$d/garde-refus-question-v1.json"
  verifier "$nom-regle" "garde refus-question : règle « $regle »" "$d/LANCEMENT.md"
  verifier "$nom-piece-regle" "\"regle\": \"$regle\"" "$d/garde-refus-question-v1.json"
  verifier "$nom-g001-absent" "journal des appels g001 : absent ou non ordinaire dans l'archive" "$d/LANCEMENT.md"
  verifier "$nom-reponse-absente" "réponse à la question : aucune pièce archivée" "$d/LANCEMENT.md"
  verifier "$nom-sortie" "pilote fini (arrêt par la garde refus-question : course fermée sans reprise)" "$E/cas-$nom/sortie.txt"
  "$PY" -I -c '
import re, sys, datetime
t = open(sys.argv[1], encoding="utf-8").read()
d0 = re.search(r"^- départ de la simulation \(UTC\) : (\S+)", t, re.M); d1 = re.search(r"^- arrêt par la garde refus-question : .* \((\S+)\) ;", t, re.M)
f = lambda s: datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
print("arrêt %d s après le départ" % int((f(d1.group(1)) - f(d0.group(1))).total_seconds()) if d0 and d1 else "heures illisibles")' "$d/LANCEMENT.md" > "$E/delai-$nom.txt" 2>&1
  verifier_re "$nom-sous-10-s" "^arrêt ([0-9]|10) s après le départ$" "$E/delai-$nom.txt"
  cas "$nom-segment-2-refuse" "est déjà fermée" -- MODE=simulation "${SAIN[@]}" SEGMENT=2 PILOTE_RACINE="$E/cas-$nom"
}
garde_artefact garde-refus-question-artefact "$E/entrees/journal-garde-artefact.jsonl" "arrêt par la garde refus-question : appel organisme-0004, rôle arbitre_synthese_contradictoire, statut REFUS, fin refusal ("
garde_artefact garde-refus-question-fin-surete "$E/entrees/journal-garde-fin-surete.jsonl" "arrêt par la garde refus-question : appel organisme-0004, rôle critique_adversariale_limites, statut MODELE_NON_CONFORME, fin SAFETY ("
garde_artefact garde-refus-question-critique-sans-moissonneur "$E/entrees/journal-garde-critique-sans-moissonneur.jsonl" "arrêt par la garde refus-question : appel organisme-0006, rôle critique_adversariale_limites, statut REFUS, fin refusal (" organisme-0006
garde_artefact garde-refus-question-apres-moissonneur "$E/entrees/journal-garde-apres-moissonneur.jsonl" "arrêt par la garde refus-question : appel organisme-0012, rôle monoculture_analytique, statut REFUS, fin refusal (" organisme-0012 "monoculture_analytique après le premier appel moissonneur_* de g001 (organisme-0011)"
garde_artefact garde-refus-question-rang-121 "$E/entrees/journal-garde-rang-121.jsonl" "arrêt par la garde refus-question : appel organisme-0121, rôle monoculture_analytique, statut REFUS, fin refusal (" organisme-0121 "monoculture_analytique au rang 121 > 120 (au-delà des tâches servies)"
garde_artefact garde-refus-question-premiere-caste-apres-moissonneur "$E/entrees/journal-garde-premiere-caste-apres-moissonneur.jsonl" "arrêt par la garde refus-question : appel organisme-0125, rôle monoculture_analytique, statut REFUS, fin refusal (" organisme-0125 "monoculture_analytique après le premier appel moissonneur_* de g001 (organisme-0124)"
garde_artefact garde-refus-question-motif-reel-m-complet "$E/entrees/journal-garde-motif-reel-m-complet.jsonl" "arrêt par la garde refus-question : appel organisme-0129, rôle arbitre_synthese_contradictoire, statut REFUS, fin refusal (" organisme-0129
echo "== état des dépôts d'essai après la série =="
git -C "$DEPOT" status --porcelain --ignored | grep -v __pycache__ | head -5
git -C "$DEPOT" log --oneline -1 | cut -c1-12
git -C "$DEPOT_M" log --oneline -1 | cut -c1-12
echo "== bilan : $ok sur $n cas conformes =="
