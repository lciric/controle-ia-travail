"""Dérive le lanceur v5 du quatrième pilote descriptif du lanceur v4 (`lancer_pilote4_gemini_v4.sh`, f335440c…), par
remplacements exacts, chacun au nombre d'occurrences attendu — décisions de Lazar (25 octobre 2026, 20:23 Paris) et
contre-lecture 2 du texte du pilote 4 (`prereg/contre-lectures/pilote4-gemini-organisme-v2-cl2.md`, 7c625fa6…) :

- (b) « Attendre la reprise par segments » : le noyau 8e5e2f7b (branche `outils/noyau-reprise-segments-v1`, à partir de
  b1c7f4b6 : `reprendre()`, `--reprendre`, état scellé `course/reprise/etat-vN.json` ; 169 essais) ; une course arrêtée
  par le STOP du minuteur continue dans l'appel suivant (`SEGMENT=2`, 3, …), dans le même dossier du pilote, avec un
  test de dépense frais, une ligne de dépense « segment K », des pièces de segment dans `segment-K-tA/` (jamais
  réécrites) ; l'archive n'est fermée qu'à la fin de la course, ou sur `CLORE=1` (fermeture sans reprise, aucun appel) ;
  une reprise refusée par le noyau (code 9) laisse la course arrêtée et ouverte ;
- (b) « 75 USD par course » : `USD_COURSE=75` (plafond total du noyau, tous segments compris) ; au segment K ≥ 2, le reste
  déclaré du GO doit couvrir 75 USD moins ce que la course a déjà dépensé (lu dans son état de reprise) ;
- minuteur : échéance 3 400 s (au lieu de 5 700) — 3 400 + 2 400 (génération) + 900 (attente des appels en vol,
  ATTENTE_FILS_S) + 60 (dépôt) + 300 (fermeture) = 7 060 s ≤ 7 200 s ; au segment K ≥ 2, STOP n'est posé qu'une fois la
  reprise consignée par le noyau (sinon il refuserait la reprise, STOP encore là) ;
- porte « v5.3 précédente » : une v5.3 en segments est acceptée (arrêts « fichier STOP » autant que de reprises, puis
  « aucune lignée active » ; reprises 2, 3, …) ; dernier code de retour 0 ; une v5.3 fermée sans reprise (CLORE=1) refusée
  (P4C2-01) ;
- en-tête (version, texte v3, usage) ; constantes du code (commit, empreinte du noyau, 169 essais, essais cités de la
  reprise).

Rien d'autre ne change : objets, banque, gardes, environnement, fermeture, liste fermée sont la ligne du lanceur v4.

Usage : python3 -I deriver_lanceur_pilote4_v5.py LANCEUR_V4 SORTIE
Refuse si l'empreinte du lanceur v4 n'est pas f335440c…, si une occurrence n'est pas au nombre attendu, si un reste
interdit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V4 = "f335440ccd139c944574f7a5c8805a309f2fa82fb73087c392fcae7fa2352a49"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V4:
    sys.exit("refus : le lanceur source n'est pas la v4 f335440c…")
t = b.decode("utf-8")

ENTETE_V4 = """# une course par appel (COURSE=v5-3, puis COURSE=v6-1) — v4 : le lanceur v3 (73d318b9…) par `deriver_lanceur_pilote4_v4.py`
# (borne de 900 s par ronde de conception ; minuteur qui pose STOP à 5 700 s du départ ; en-tête ; écart consigné dans
# `diff-lanceur-pilote4-v3-vers-v4.txt`), le v3 étant lui-même dérivé du lanceur v2 du pilote 3
"""
ENTETE_V5 = """# une course en un ou plusieurs segments (COURSE=v5-3, puis COURSE=v6-1 ; SEGMENT=1, 2, …) — v5 : le lanceur v4
# (f335440c…) par `deriver_lanceur_pilote4_v5.py` (reprise par segments du noyau 8e5e2f7b : une course arrêtée par le STOP
# du minuteur continue dans l'appel suivant ; archive fermée à la fin de la course ou sur CLORE=1 ; 75 USD par course ;
# minuteur à 3 400 s ; écart consigné dans `diff-lanceur-pilote4-v4-vers-v5.txt`), le v4 dérivé du v3 (73d318b9…) par
# `deriver_lanceur_pilote4_v4.py`, le v3 étant lui-même dérivé du lanceur v2 du pilote 3
"""

USAGE_V4 = """#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> \\
#       bash lancer_pilote4_gemini_v4.sh
#   MODE=reel COURSE=v6-1 … PRECEDENTE_V53=<dossier du pilote de la course v5.3 de ce pilote, dans la même copie> (même forme)
"""
USAGE_V5 = """#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> [SEGMENT=1] \\
#       bash lancer_pilote4_gemini_v5.sh
#   MODE=reel COURSE=v6-1 … PRECEDENTE_V53=<dossier du pilote de la course v5.3 de ce pilote, dans la même copie> (même forme)
#   Reprise : la même commande (même COURSE, TENTATIVE, GRAINE, texte et références) avec SEGMENT=K, quand le LANCEMENT.md
#     dit « segment K−1 arrêté par STOP ; reprise attendue : SEGMENT=K » ; à chaque segment, un test de dépense frais
#     (APPEL_CONTROLE_FICHIER), une ligne de dépense nommant la course, le GO et « segment K », RESTE_GO_USD ≥ 75 USD moins
#     la dépense déjà faite par la course ; rien n'est committé dans la copie du dépôt entre deux segments (même HEAD)
#   Fermeture sans reprise (décision de Lazar) : SEGMENT=K CLORE=1 — aucun appel ; la course arrêtée est fermée et poussée
#     comme à sa fin
"""

JAMAIS_V4 = "# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course ou la sortie standard ; arrêter un\n"
JAMAIS_V5 = ("# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course (hors de son manifeste et de son état\n"
             "# de reprise, mécaniques) ou la sortie standard ; arrêter un\n")

SEGMENT_V5 = """COURSE="${COURSE:?COURSE=v5-3 ou COURSE=v6-1}"
# Reprise par segments (décision de Lazar, 25 octobre 2026, 20:23 Paris) : SEGMENT=1 fait partir la course ; SEGMENT=K ≥ 2
#   continue la course arrêtée au segment K − 1 par le STOP du minuteur ; CLORE=1 (avec SEGMENT ≥ 2) la ferme sans reprise
SEGMENT="${SEGMENT:-1}"
case "$SEGMENT" in ''|*[!0-9]*|0*) refus_tot "SEGMENT doit être un entier ≥ 1, sans zéro en tête : « $SEGMENT »";; esac
CLORE="${CLORE:-}"
case "$CLORE" in ''|1) ;; *) refus_tot "CLORE vaut 1 ou rien : « $CLORE »";; esac
if [ -n "$CLORE" ] && [ "$SEGMENT" = 1 ]; then refus_tot "CLORE=1 ferme une course arrêtée entre deux segments : SEGMENT ≥ 2 exigé"; fi
"""

USD_V4 = """USD_COURSE=60   # par course ; deux courses : 120 USD au plus (GO-2026-10-25-02, étendu par un mot direct de Lazar dans la session de session-depot : 155 USD au plus pour l'ensemble du GO)
# P4C1-02 : minuteur. STOP posé dans course/ à ECHEANCE_STOP_S s du départ du lanceur si la course tourne encore (la
#   commande de fond de session-depot est bornée à 7 200 s) ; fixe en réel ; réglable en simulation (ESSAI_ECHEANCE_STOP_S)
ECHEANCE_STOP_S=5700
"""
USD_V5 = """USD_COURSE=75   # par course, tous segments compris (plafond total du noyau) ; deux courses : 150 USD au plus (décision de Lazar, 25 octobre, 20:23 Paris : 75 USD par course, GO-2026-10-25-02 à 185 USD au plus pour l'ensemble du GO ; la ligne d'extension est écrite par session-depot sur son mot direct)
# P4C1-02 et reprise par segments : minuteur. STOP posé dans course/ à ECHEANCE_STOP_S s du départ du lanceur si la course
#   tourne encore ; le noyau finit l'unité en cours (ronde de conception ou génération), écrit son état de reprise et
#   s'arrête ; le segment suivant continue. 3 400 s + la plus longue unité possible (2 400 s de génération + 900 s
#   d'attente des appels en vol, ATTENTE_FILS_S, + 60 s de dépôt) + 300 s de fermeture = 7 060 s, sous les 7 200 s de la
#   commande de fond de session-depot ; fixe en réel ; réglable en simulation (ESSAI_ECHEANCE_STOP_S)
ECHEANCE_STOP_S=3400
"""

R3_V4 = """if raison_r3="$(course_deja_partie)"; then refus_tot "$raison_r3 (R3 : jamais de seconde course)"; fi
if [ "$MODE" = reel ]; then
  distante="$(git -C "$DEPOT" ls-remote --heads origin "pilotes/$NOM" 2>/dev/null)" || refus_tot "lecture du dépôt distant impossible (git ls-remote) : R3 non vérifiable, le pilote attend"
  [ -z "$distante" ] || refus_tot "la branche pilotes/$NOM existe déjà sur le dépôt distant (R3)"
fi
[ -e "$PILOTE" ] && refus_tot "$PILOTE existe déjà (R12 ; après un refus avant le manifeste : TENTATIVE=$((TENTATIVE + 1)))"
mkdir -p "$RACINE_PILOTES"
mkdir "$VERROU" 2>/dev/null || refus_tot "verrou $VERROU présent : un autre lanceur de cette course tourne, ou un lanceur s'est interrompu (examiner, puis retirer le verrou à la main)"
mkdir -m 700 "$PILOTE"
mkdir -m 700 "$PILOTE/ferme"
printf 'course/\\nferme/\\n' > "$PILOTE/.gitignore"   # jamais ajoutés au dépôt, même par un `git add -A`
L="$PILOTE/LANCEMENT.md"
refus() { echo "REFUS : $*" >&2; echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou retiré" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256); rmdir "$VERROU" 2>/dev/null || true; exit 2; }
note() { echo "$*" >> "$L"; }
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : arrêt" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou $VERROU laissé (à examiner)" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256) || true' ERR
if [ "$MODE" = reel ]; then SOURCE_REG="origin/main"; else SOURCE_REG="${REGISTRE_GO_SOURCE:-aucune (simulation)} ; dépenses : ${DEPENSES_SOURCE:-aucune (simulation)}"; fi
SHA_LANCEUR="$(sha256sum "$0" | cut -d' ' -f1)"
{
  echo "# Lancement du pilote $NOM ($MODE, tentative $TENTATIVE)"
  echo
  echo "- début (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; hôte : $(hostname) ; utilisateur : $(id -u)"
  echo "- course : $COURSE ; dossier du pilote : $PILOTE (0700, à root)"
  echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (c'est le « commit » que le manifeste consignera)"
"""
R3_V5 = """if [ "$SEGMENT" = 1 ]; then
  if raison_r3="$(course_deja_partie)"; then refus_tot "$raison_r3 (R3 : jamais de seconde course)"; fi
fi
if [ "$MODE" = reel ]; then  # rien n'est poussé avant la fermeture de la course, quel que soit le segment
  distante="$(git -C "$DEPOT" ls-remote --heads origin "pilotes/$NOM" 2>/dev/null)" || refus_tot "lecture du dépôt distant impossible (git ls-remote) : R3 non vérifiable, le pilote attend"
  [ -z "$distante" ] || refus_tot "la branche pilotes/$NOM existe déjà sur le dépôt distant (R3)"
fi
L="$PILOTE/LANCEMENT.md"
SHA_LANCEUR="$(sha256sum "$0" | cut -d' ' -f1)"
if [ "$SEGMENT" = 1 ]; then
  [ -e "$PILOTE" ] && refus_tot "$PILOTE existe déjà (R12 ; après un refus avant le manifeste : TENTATIVE=$((TENTATIVE + 1)))"
  mkdir -p "$RACINE_PILOTES"
  mkdir "$VERROU" 2>/dev/null || refus_tot "verrou $VERROU présent : un autre lanceur de cette course tourne, ou un lanceur s'est interrompu (examiner, puis retirer le verrou à la main)"
  mkdir -m 700 "$PILOTE"
  mkdir -m 700 "$PILOTE/ferme"
  printf 'course/\\nferme/\\n' > "$PILOTE/.gitignore"   # jamais ajoutés au dépôt, même par un `git add -A`
  VERROU_ACTIF="$VERROU"; DS="$PILOTE"; SUFFIXE_SEG=""
else
  # Reprise : la course de ce pilote (même TENTATIVE), partie au segment 1, arrêtée par le STOP du minuteur au segment
  # précédent, ni fermée ni poussée ; même lanceur, même HEAD ; un seul lanceur par segment (verrou du segment)
  { [ -d "$PILOTE" ] && [ -f "$L" ]; } || refus_tot "SEGMENT=$SEGMENT : $PILOTE ou son LANCEMENT.md absent (aucune course à reprendre ; même TENTATIVE qu'au segment 1)"
  if [ -e "$PILOTE/ferme.tar.gz" ]; then refus_tot "SEGMENT=$SEGMENT : la course de $PILOTE est déjà fermée"; fi
  [ -f "$PILOTE/course/manifeste-run.json" ] || refus_tot "SEGMENT=$SEGMENT : aucune course partie dans $PILOTE"
  [ -d "$VERROU" ] || refus_tot "SEGMENT=$SEGMENT : verrou $VERROU du segment 1 absent"
  { [ -f "$MARQUEURS/$NOM" ] && [ "$(cut -d' ' -f1 < "$MARQUEURS/$NOM")" = "$PILOTE" ]; } || refus_tot "SEGMENT=$SEGMENT : marqueur de départ $MARQUEURS/$NOM absent ou d'un autre dossier (R3)"
  for d in "$RACINE_PILOTES/$NOM"*; do
    if [ -d "$d" ] && [ "$d" != "$PILOTE" ] && { [ -f "$d/course/manifeste-run.json" ] || [ -f "$d/ferme.tar.gz" ]; }; then refus_tot "SEGMENT=$SEGMENT : une autre course de ce nom est partie dans $d (R3)"; fi
  done
  derniere_fin="$(grep -E '^- segment [0-9]+ arrêté par STOP ; reprise attendue : SEGMENT=[0-9]+$' "$L" | tail -1 || true)"
  [ "$derniere_fin" = "- segment $((SEGMENT - 1)) arrêté par STOP ; reprise attendue : SEGMENT=$SEGMENT" ] || refus_tot "SEGMENT=$SEGMENT : le LANCEMENT.md n'attend pas ce segment (dernière fin de segment : « ${derniere_fin:-aucune} »)"
  grep -Fxq -- "- lanceur : $(basename "$0"), sha256 $SHA_LANCEUR" "$L" || refus_tot "SEGMENT=$SEGMENT : ce lanceur ($(basename "$0"), ${SHA_LANCEUR:0:8}…) n'est pas celui du segment 1"
  head1="$(grep -E '^- dépôt : .* ; HEAD : [0-9a-f]{40} ' "$L" | head -1 | grep -Eo 'HEAD : [0-9a-f]{40}' | cut -c8- || true)"
  [ "$head1" = "$(git -C "$DEPOT" rev-parse HEAD)" ] || refus_tot "SEGMENT=$SEGMENT : HEAD du dépôt ≠ celui du segment 1 (${head1:-illisible}) : le noyau refuserait la reprise ; rien n'est committé dans cette copie entre deux segments"
  VERROU_ACTIF="$VERROU-segment$SEGMENT"
  mkdir "$VERROU_ACTIF" 2>/dev/null || refus_tot "verrou $VERROU_ACTIF présent : un autre lanceur de ce segment tourne, ou un lanceur s'est interrompu (examiner, puis retirer le verrou à la main)"
  essai_seg=1; while [ -e "$PILOTE/segment-$SEGMENT-t$essai_seg" ]; do essai_seg=$((essai_seg + 1)); done
  DS="$PILOTE/segment-$SEGMENT-t$essai_seg"; SUFFIXE_SEG="-segment-$SEGMENT-t$essai_seg"
  mkdir -m 700 "$DS"
fi
refus() { echo "REFUS : $*" >&2; echo "- refus : $* ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou $VERROU_ACTIF retiré" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256); rmdir "$VERROU_ACTIF" 2>/dev/null || true; exit 2; }
note() { echo "$*" >> "$L"; }
trap 'c=$?; echo "ÉCHEC inattendu (code $c) à la ligne $LINENO : arrêt" >&2; echo "- échec inattendu (code $c) à la ligne $LINENO ($(date -u +%Y-%m-%dT%H:%M:%SZ)) ; verrou $VERROU_ACTIF laissé (à examiner)" >> "$L"; (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256) || true' ERR
if [ "$MODE" = reel ]; then SOURCE_REG="origin/main"; else SOURCE_REG="${REGISTRE_GO_SOURCE:-aucune (simulation)} ; dépenses : ${DEPENSES_SOURCE:-aucune (simulation)}"; fi
{
  if [ "$SEGMENT" = 1 ]; then
    echo "# Lancement du pilote $NOM ($MODE, tentative $TENTATIVE)"
  else
    echo
    echo "## Segment $SEGMENT, essai $essai_seg ($MODE, tentative $TENTATIVE)$(if [ -n "$CLORE" ]; then echo " — fermeture sans reprise (CLORE=1)"; fi)"
  fi
  echo
  echo "- début (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; hôte : $(hostname) ; utilisateur : $(id -u)"
  echo "- course : $COURSE ; dossier du pilote : $PILOTE (0700, à root)$(if [ "$SEGMENT" != 1 ]; then echo " ; pièces de ce segment : $(basename "$DS")/"; fi)"
  if [ "$SEGMENT" = 1 ]; then echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (c'est le « commit » que le manifeste consignera)"
  else echo "- dépôt : $DEPOT ; HEAD : $(git -C "$DEPOT" rev-parse HEAD) (celui du segment 1, que le manifeste consigne)"; fi
"""

ENTETE_FIN_V4 = """} > "$L"
[ "$MODE" = simulation ] && [ -n "$ART" ] && note "- ESSAI : artefact « $ART » (simulation)"
"""
ENTETE_FIN_V5 = """} >> "$L"
[ "$MODE" = simulation ] && [ -n "$ART" ] && note "- ESSAI : artefact « $ART » (simulation)"
# Reprise : l'état de reprise du segment précédent (dernier `course/reprise/etat-vN.json`) — compagnon, arrêt sur STOP,
#   numéro de segment ; seule la dépense déjà faite en est lue (rien d'autre de la course)
compter_etats() { local n=0 f; for f in "$PILOTE/course/reprise"/etat-v*.json; do if [ -f "$f" ]; then n=$((n + 1)); fi; done; echo "$n"; }
lire_etat_reprise() {  # lire_etat_reprise SEGMENT_ATTENDU → « nom sha dépense_faite reste_course » ; code 1 sinon
  "$PY" -I -c '
import hashlib, json, pathlib, sys
d, usd, seg = pathlib.Path(sys.argv[1]) / "reprise", float(sys.argv[2]), int(sys.argv[3])
etats = sorted(d.glob("etat-v*.json"), key=lambda p: int(p.stem.split("-v")[-1])) if d.is_dir() else []
if not etats: print("aucun état de reprise"); sys.exit(1)
p = etats[-1]
c = p.with_name(p.name + ".sha256")
sha = hashlib.sha256(p.read_bytes()).hexdigest()
if not c.is_file() or c.read_text(encoding="utf-8").split()[:1] != [sha]: print(p.name + " : compagnon absent ou différent"); sys.exit(1)
e = json.loads(p.read_text(encoding="utf-8"))
if e.get("raison_arret") != "fichier STOP": print(p.name + " : arrêt autre que STOP (%r)" % e.get("raison_arret")); sys.exit(1)
if e.get("segment") != seg: print(p.name + " : état du segment %r, attendu %d" % (e.get("segment"), seg)); sys.exit(1)
fait = float(e["depense_totale_usd"])
print("%s %s %.4f %.4f" % (p.name, sha, fait, max(0.0, usd - fait)))' "$PILOTE/course" "$USD_COURSE" "$1"
}
if [ "$SEGMENT" != 1 ]; then
  etat_reprise="$(lire_etat_reprise "$((SEGMENT - 1))")" || refus "SEGMENT=$SEGMENT : état de reprise du segment $((SEGMENT - 1)) non conforme ($etat_reprise)"
  read -r ETAT_NOM ETAT_SHA DEJA_USD DU_SEGMENT <<< "$etat_reprise"
  note "- état de reprise : $ETAT_NOM, sha256 $ETAT_SHA (compagnon conforme), arrêt sur STOP du segment $((SEGMENT - 1)) ; dépense de la course jusqu'ici $DEJA_USD USD ; reste au plus $DU_SEGMENT USD pour la course (plafond $USD_COURSE USD)"
fi
"""

PORTE_CODE_V4 = """if not re.search(r"^- lanceur : " + re.escape(nom_lanceur) + r", sha256 " + sha_lanceur + r"$", lan, re.M): pb.append("v5.3 n a pas tourné sous ce lanceur")
if not re.search(r"code de retour : 0 ;", lan): pb.append("code de retour du noyau non nul ou absent")
"""
PORTE_CODE_V5 = """if not re.search(r"^- lanceur : " + re.escape(nom_lanceur) + r", sha256 " + sha_lanceur + r"$", lan, re.M): pb.append("v5.3 n a pas tourné sous ce lanceur")
codes = re.findall(r"code de retour : ([0-9]+) ;", lan)
if not codes or codes[-1] != "0": pb.append("code de retour du noyau non nul ou absent")
if re.search(r"^- CLORE=1 : aucune reprise", lan, re.M): pb.append("course v5.3 fermée sans reprise (CLORE=1)")
"""

PORTE_ARRET_V4 = """arrets = [e.get("raison") for e in x.get("evenements", []) if e.get("etape") == "arret"]
if arrets != ["aucune lignée active"]: pb.append("arrêt de la course : %r" % arrets)
if pb: print("; ".join(pb)); sys.exit(1)
refus_s = [g.get("refus_noyau") for g in gs]
print("v5.3 saine : g000 à g003 OK, au plus 20 %% d appels hors OK et au moins un appel OK de Fable à chacune (%s), fin « générations maximales », arrêt « aucune lignée active », code 0, archive fermée ; graine de v5.3 %s ; dépense du noyau %s USD ; refus du noyau par génération %s" % ("; ".join(statuts_appels), m.get("entropie_seed_sequence"), r.get("depense_totale_usd"), json.dumps(refus_s, ensure_ascii=False)))
"""
PORTE_ARRET_V5 = """arrets = [e.get("raison") for e in x.get("evenements", []) if e.get("etape") == "arret"]
reprises = [e.get("segment") for e in x.get("evenements", []) if e.get("etape") == "reprise"]
k = len(reprises)
if arrets != ["fichier STOP"] * k + ["aucune lignée active"] or reprises != list(range(2, k + 2)):
    pb.append("arrêt de la course : %r ; reprises : %r" % (arrets, reprises))
if pb: print("; ".join(pb)); sys.exit(1)
refus_s = [g.get("refus_noyau") for g in gs]
print("v5.3 saine : g000 à g003 OK, au plus 20 %% d appels hors OK et au moins un appel OK de Fable à chacune (%s), fin « générations maximales », arrêt « aucune lignée active » en %d segment(s) (%d arrêt(s) sur le STOP du minuteur, chacun repris), dernier code 0, archive fermée ; graine de v5.3 %s ; dépense du noyau %s USD ; refus du noyau par génération %s" % ("; ".join(statuts_appels), k + 1, k, m.get("entropie_seed_sequence"), r.get("depense_totale_usd"), json.dumps(refus_s, ensure_ascii=False)))
"""

CITES_FIN_V4 = ' test_r410_cles_openalex_et_s2_en_entete_jamais_dans_l_adresse"\n'
CITES_FIN_V5 = (' test_r410_cles_openalex_et_s2_en_entete_jamais_dans_l_adresse'
                ' test_course_continue_de_reference test_stop_en_conception_aucune_generation_notee_avant_la_reprise'
                ' test_conception_arretee_jamais_suivie_de_generations_dans_le_meme_segment test_stop_pendant_la_derniere_unite_n_appelle_pas_de_segment'
                ' test_stop_pose_pendant_une_unite_ne_l_interrompt_pas test_reprise_acceptee_puis_jamais_deux_fois_le_meme_etat'
                ' test_reprise_refusee_sans_etat_et_sur_noyau_amorce test_reprise_refusee_stop_present test_reprise_refusee_etat_altere'
                ' test_reprise_refusee_course_qui_a_bouge test_reprise_accepte_d_autres_chemins_pour_les_memes_pieces'
                ' test_cli_simuler_reprendre_et_refus test_refus_reprise_des_arguments test_lancer_refuse_course_existante_sans_reprendre'
                ' test_ronde_interrompue_continuee_sans_rejouer_ni_sauter[False] test_ronde_interrompue_continuee_sans_rejouer_ni_sauter[True]"\n')

ORG_V4 = 'git -C "$DEPOT" archive "$COMMIT_ORGANISME" organisme | tar -x -C "$PILOTE"\n'
ORG_V5 = ('# reprise : l\'organisme et la question extraits au segment 1, revérifiés ci-dessous, jamais réécrits\n'
          'if [ "$SEGMENT" = 1 ]; then git -C "$DEPOT" archive "$COMMIT_ORGANISME" organisme | tar -x -C "$PILOTE"; '
          'else [ -d "$PILOTE/organisme" ] || refus "SEGMENT=$SEGMENT : organisme du segment 1 absent de $PILOTE"; fi\n')
QUESTION_V4 = 'git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"\n'
QUESTION_V5 = ('if [ "$SEGMENT" = 1 ]; then git -C "$DEPOT" show "$COMMIT_QUESTION:$CHEMIN_QUESTION" > "$PILOTE/question.md"; '
               'else [ -f "$PILOTE/question.md" ] || refus "SEGMENT=$SEGMENT : question du segment 1 absente de $PILOTE"; fi\n')

DEPENSE_V4 = """  echo "$dep" | grep "$NOM" | grep -q "$GO_ID" || refus "lancement non consigné avant dans registres/depenses.md (une ligne nommant $NOM et $GO_ID)"
"""
DEPENSE_V5 = """  echo "$dep" | grep "$NOM" | grep -q "$GO_ID" || refus "lancement non consigné avant dans registres/depenses.md (une ligne nommant $NOM et $GO_ID)"
  if [ "$SEGMENT" != 1 ]; then
    echo "$dep" | grep "$NOM" | grep "$GO_ID" | grep -q "segment $SEGMENT\\b" || refus "segment $SEGMENT non consigné avant dans registres/depenses.md (une ligne nommant $NOM, $GO_ID et « segment $SEGMENT »)"
  fi
"""
RESTE_V4 = """  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= float(sys.argv[2]) else 1)' "$reste" "$USD_COURSE" || refus "reste sur $GO_ID = $reste USD < $USD_COURSE"
  note "- registre : une ligne $GO_ID de type calcul portant l'empreinte de la question ($COURSE), celle de l'organisme (${ARBRE_ORGANISME:0:8}…) et celle du texte scellé (${t16:-aucun texte donné en simulation}) ; dépense consignée avant ; reste déclaré $reste USD ≥ $USD_COURSE (vérification du lanceur)"
"""
RESTE_V5 = """  besoin="$USD_COURSE"; if [ "$SEGMENT" != 1 ]; then besoin="$DU_SEGMENT"; fi   # reprise : 75 USD moins la dépense déjà faite (état de reprise)
  "$PY" -I -c 'import sys; sys.exit(0 if float(sys.argv[1]) >= float(sys.argv[2]) else 1)' "$reste" "$besoin" || refus "reste sur $GO_ID = $reste USD < $besoin"
  note "- registre : une ligne $GO_ID de type calcul portant l'empreinte de la question ($COURSE), celle de l'organisme (${ARBRE_ORGANISME:0:8}…) et celle du texte scellé (${t16:-aucun texte donné en simulation}) ; dépense consignée avant$(if [ "$SEGMENT" != 1 ]; then echo " (segment $SEGMENT)"; fi) ; reste déclaré $reste USD ≥ $besoin (vérification du lanceur)"
"""

MARQUEUR_V4 = """mkdir -p "$MARQUEURS"
( set -o noclobber; printf '%s %s\\n' "$PILOTE" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$MARQUEURS/$NOM" ) 2>/dev/null || refus "marqueur de départ $MARQUEURS/$NOM déjà posé (R3)"
note "- marqueur de départ : $MARQUEURS/$NOM (R3 ; jamais retiré)"
"""
MARQUEUR_V5 = """if [ "$SEGMENT" = 1 ]; then
  mkdir -p "$MARQUEURS"
  ( set -o noclobber; printf '%s %s\\n' "$PILOTE" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$MARQUEURS/$NOM" ) 2>/dev/null || refus "marqueur de départ $MARQUEURS/$NOM déjà posé (R3)"
  note "- marqueur de départ : $MARQUEURS/$NOM (R3 ; jamais retiré)"
else
  note "- marqueur de départ : $MARQUEURS/$NOM, posé au segment 1 pour ce dossier (R3 ; jamais retiré)"
fi
"""

DEBUT_ETAPES_V4 = """# 4. Registre des GO : une ligne « | GO-2026-10-25-02 | » qui porte « calcul », l'empreinte (8 premiers caractères) de
"""
DEBUT_ETAPES_V5 = """# CLORE=1 : ni registre, ni test de dépense, ni essais, ni course — la course arrêtée est fermée (étape 8a)
if [ -z "$CLORE" ]; then
# 4. Registre des GO : une ligne « | GO-2026-10-25-02 | » qui porte « calcul », l'empreinte (8 premiers caractères) de
"""

COURSE_LANCEE_V4 = """          --organisme-impose "$LIGNEE=$ORG@$FAMILLE")
SORTIE_FERMEE="$PILOTE/ferme/sortie-standard-lanceur.txt"
ERREURS="$PILOTE/sortie-erreur-lanceur.txt"
cd "$R"
"""
COURSE_LANCEE_V5 = """          --organisme-impose "$LIGNEE=$ORG@$FAMILLE")
if [ "$SEGMENT" != 1 ]; then COMMUNES+=(--reprendre); fi   # reprise : le noyau continue la course de --sortie (état scellé, mêmes paramètres)
SORTIE_FERMEE="$PILOTE/ferme/sortie-standard-lanceur$SUFFIXE_SEG.txt"
ERREURS="$DS/sortie-erreur-lanceur.txt"
cd "$R"
N_ETATS_AVANT="$(compter_etats)"
N_EV_AVANT=0
if [ "$SEGMENT" != 1 ]; then
  N_EV_AVANT="$(wc -l < "$PILOTE/course/evenements.jsonl")"
  if [ -f "$PILOTE/course/STOP" ]; then rm -f "$PILOTE/course/STOP"; note "- STOP du segment $((SEGMENT - 1)) retiré de course/ (reprise)"; fi
fi
"""

DEPART_REEL_V4 = '  note "- départ (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"\n'
DEPART_REEL_V5 = '  note "- départ (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)$(if [ "$SEGMENT" != 1 ]; then echo " ; segment $SEGMENT, reprise de la course"; fi)"\n'
DEPART_SIM_V4 = '  note "- départ de la simulation (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"\n'
DEPART_SIM_V5 = '  note "- départ de la simulation (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)$(if [ "$SEGMENT" != 1 ]; then echo " ; segment $SEGMENT, reprise de la course"; fi)"\n'

MINUTEUR_V4 = """minuteur() {
  local fin=$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S )) s
  trap 'exit 0' TERM
  while kill -0 "$PID" 2>/dev/null; do
    if [ -f "$PILOTE/course/manifeste-run.json" ] && [ "$(date +%s)" -ge "$fin" ]; then
"""
MINUTEUR_V5 = """course_en_cours() {  # segment 1 : manifeste écrit ; segment K ≥ 2 : reprise consignée par le noyau (sinon STOP la ferait refuser)
  if [ "$SEGMENT" = 1 ]; then [ -f "$PILOTE/course/manifeste-run.json" ]; else [ "$(wc -l < "$PILOTE/course/evenements.jsonl")" -gt "$N_EV_AVANT" ]; fi
}
minuteur() {
  local fin=$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S )) s
  trap 'exit 0' TERM
  while kill -0 "$PID" 2>/dev/null; do
    if course_en_cours && [ "$(date +%s)" -ge "$fin" ]; then
"""
MINUTEUR_NOTE_V4 = """      note "- minuteur : STOP posé dans course/ à $(date -u +%Y-%m-%dT%H:%M:%SZ) ($ECHEANCE_STOP_S s après le départ du lanceur) : la course s'arrête avant la ronde ou la génération suivante"
"""
MINUTEUR_NOTE_V5 = """      note "- minuteur : STOP posé dans course/ à $(date -u +%Y-%m-%dT%H:%M:%SZ) ($ECHEANCE_STOP_S s après le départ du lanceur) : la course s'arrête avant la ronde ou la génération suivante ; état de reprise attendu"
"""

FIN_PROCESSUS_V4 = """if [ -f "$PILOTE/course/STOP" ]; then
  note "- minuteur : STOP du minuteur présent dans course/ à la fin de la course (raison d'arrêt : événement « arret » de l'extrait) — liste d'arrêt du texte"
else
  note "- minuteur arrêté par son PID ($MINUTEUR) à la fin de la course : STOP non posé"
fi
note "- fin du processus (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; code de retour : $CODE ; sortie standard fermée (non lue) ; sortie d'erreur : sortie-erreur-lanceur.txt (lisible)"
"""
FIN_PROCESSUS_V5 = """if [ -f "$PILOTE/course/STOP" ]; then
  note "- minuteur : STOP présent dans course/ à la fin du processus (fin de segment si le noyau a écrit un état de reprise ; sinon la course a fini sur sa dernière unité)"
else
  note "- minuteur arrêté par son PID ($MINUTEUR) à la fin de la course : STOP non posé"
fi
note "- fin du processus (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ) ; code de retour : $CODE ; sortie standard fermée (non lue) ; sortie d'erreur : ${ERREURS#"$PILOTE"/} (lisible)"
else
  CODE=""
  note "- CLORE=1 : aucune reprise, aucun appel ; la course arrêtée au segment $((SEGMENT - 1)) est fermée comme à sa fin (décision de Lazar)"
fi
# Fin de segment : le noyau a rendu 0 et écrit un état de reprise de plus (arrêt sur le STOP du minuteur) — la course reste
#   ouverte (course/, ferme/ : jamais lus ni poussés), le segment suivant la continue ; reprise refusée par le noyau
#   (code 9) : la course reste arrêtée et ouverte ; sinon la course a fini (ou CLORE=1) : fermeture (étape 8a)
if [ -z "$CLORE" ] && [ "$SEGMENT" != 1 ] && [ "$CODE" = 9 ]; then
  note "- reprise refusée par le noyau (code 9 ; motif dans ${ERREURS#"$PILOTE"/}) : la course reste arrêtée au segment $((SEGMENT - 1)), ouverte, rien n'a tourné ; décision de Lazar : refaire SEGMENT=$SEGMENT après correction, ou SEGMENT=$SEGMENT CLORE=1"
  rmdir "$VERROU_ACTIF" 2>/dev/null || true
  (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256)
  echo "segment $SEGMENT : reprise refusée par le noyau — la course reste arrêtée et ouverte ; rien à pousser"
  exit 3
fi
if [ -z "$CLORE" ] && [ -f "$PILOTE/course/manifeste-run.json" ] && [ "$CODE" = 0 ] && [ "$(compter_etats)" = "$((N_ETATS_AVANT + 1))" ]; then
  if fin_seg="$(lire_etat_reprise "$SEGMENT")"; then
    note "- état de reprise écrit par le noyau : $fin_seg"
    note "- segment $SEGMENT arrêté par STOP ; reprise attendue : SEGMENT=$((SEGMENT + 1))"
    if [ "$SEGMENT" != 1 ]; then rmdir "$VERROU_ACTIF" 2>/dev/null || true; fi
    note "- fin du lanceur (UTC) : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    (cd "$PILOTE" && sha256sum LANCEMENT.md > LANCEMENT.md.sha256)
    echo "segment $SEGMENT fini sur le STOP du minuteur : course arrêtée entre deux unités, ouverte (course/ et ferme/ jamais lus ni poussés) ; reprise : SEGMENT=$((SEGMENT + 1)), avec un test de dépense frais et une ligne de dépense « segment $((SEGMENT + 1)) » ; rien à pousser avant la fin de la course"
    exit 0
  else
    note "- état de reprise de plus, mais non conforme ($fin_seg) : la course est fermée (étape 8a) — réserve"
  fi
fi
"""

SORTIE_ERREUR_SHA_V4 = '(cd "$PILOTE" && sha256sum sortie-erreur-lanceur.txt > sortie-erreur-lanceur.txt.sha256)\n'
SORTIE_ERREUR_SHA_V5 = ('for f in "$PILOTE"/sortie-erreur-lanceur.txt "$PILOTE"/segment-*-t*/sortie-erreur-lanceur.txt; do '
                        'if [ -f "$f" ]; then (cd "$(dirname "$f")" && sha256sum sortie-erreur-lanceur.txt > sortie-erreur-lanceur.txt.sha256); fi; done\n')
PERMIS_V4 = "|organisme/.+|ferme\\.tar\\.gz(\\.sha256)?|refus-avant-manifeste-v1\\.tar\\.gz(\\.sha256)?)$'\n"
PERMIS_V5 = ("|organisme/.+|ferme\\.tar\\.gz(\\.sha256)?|refus-avant-manifeste-v1\\.tar\\.gz(\\.sha256)?"
             "|segment-[0-9]+-t[0-9]+/(registre-go\\.md|test-depense-[^/]+|essais-v1\\.(xml|txt)|sortie-erreur-lanceur\\.txt(\\.sha256)?))$'\n")

MINUTEUR_COMMENTAIRE_V4 = """#   course tourne encore et que son manifeste est écrit, il pose STOP dans course/ (le noyau le lit avant chaque ronde et
#   chaque génération, `_doit_arreter`) ; la fermeture qui suit est celle d'une course finie (étape 8a).
"""
MINUTEUR_COMMENTAIRE_V5 = """#   course tourne encore (segment 1 : manifeste écrit ; segment K ≥ 2 : reprise consignée par le noyau), il pose STOP dans
#   course/ (le noyau le lit avant chaque ronde et chaque génération, `_doit_arreter`) ; le noyau finit l'unité en cours,
#   écrit son état de reprise et rend 0 : fin du segment, la course reste ouverte et le segment suivant la continue ;
#   si plus aucune unité ne restait, la course a fini et se ferme (étape 8a).
"""

remplacements = [
    # en-tête, usage
    (ENTETE_V4, ENTETE_V5, 1),
    ("# Texte : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v2.md` (ou la version qui le remplace et cite ce\n",
     "# Texte : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v3.md` (ou la version qui le remplace et cite ce\n", 1),
    (USAGE_V4, USAGE_V5, 1),
    (JAMAIS_V4, JAMAIS_V5, 1),
    # segment et fermeture sans reprise
    ('COURSE="${COURSE:?COURSE=v5-3 ou COURSE=v6-1}"\n', SEGMENT_V5, 1),
    # plafond par course et échéance du minuteur
    (USD_V4, USD_V5, 1),
    # code : commit, empreinte du noyau, essais (le commit complet d'abord : il contient l'abrégé)
    ("COMMIT_CODE=b1c7f4b697e846a2fe904fa90a36148587756dd5\n", "COMMIT_CODE=8e5e2f7b8bde522e4b5ce0229a9da57e118d32f3\n", 1),
    ("CODE_NOYAU_PROPRE=37acdcaaaded746b7f7599f17e8149bdd773e372f3a3b0782db7b73882acf8a3\n", "CODE_NOYAU_PROPRE=61ddd638d7a3b5519a7294fc04a75003e3d21da72b9cfdcf4dd07dc0341565a0\n", 1),
    ("N_ESSAIS=141\n", "N_ESSAIS=169\n", 1),
    (CITES_FIN_V4, CITES_FIN_V5, 1),
    ("b1c7f4b6", "8e5e2f7b", 7),
    ("≠ 37acdcaa…", "≠ 61ddd638…", 1),
    # R3, dossier du pilote, segment, verrou, en-tête du LANCEMENT.md
    (R3_V4, R3_V5, 1),
    (ENTETE_FIN_V4, ENTETE_FIN_V5, 1),
    # porte « v5.3 précédente » : segments (P4C2-01), dernier code, CLORE
    (PORTE_CODE_V4, PORTE_CODE_V5, 1),
    (PORTE_ARRET_V4, PORTE_ARRET_V5, 1),
    # objets et question : extraits au segment 1, revérifiés ensuite
    (ORG_V4, ORG_V5, 1),
    (QUESTION_V4, QUESTION_V5, 1),
    # CLORE : étapes 4 à 7 sautées
    (DEBUT_ETAPES_V4, DEBUT_ETAPES_V5, 1),
    # registre et dépense par segment (pièces du segment dans DS)
    ('git -C "$DEPOT" show origin/main:registres/go.md > "$PILOTE/registre-go.md"; else cp "$REGISTRE_GO_SOURCE" "$PILOTE/registre-go.md"; fi',
     'git -C "$DEPOT" show origin/main:registres/go.md > "$DS/registre-go.md"; else cp "$REGISTRE_GO_SOURCE" "$DS/registre-go.md"; fi', 1),
    ('ligne_go="$(grep "^| $GO_ID |" "$PILOTE/registre-go.md"', 'ligne_go="$(grep "^| $GO_ID |" "$DS/registre-go.md"', 1),
    (DEPENSE_V4, DEPENSE_V5, 1),
    (RESTE_V4, RESTE_V5, 1),
    # test de dépense et essais : pièces du segment
    ('cp "$TD" "$PILOTE/test-depense-$(basename "$TD")"', 'cp "$TD" "$DS/test-depense-$(basename "$TD")"', 1),
    ('"$PILOTE/essais-v1.', '"$DS/essais-v1.', 7),
    # R3 au départ : la course reprise est partie au segment 1 (dans ce dossier)
    ('if raison_r3="$(course_deja_partie)"; then refus "$raison_r3 (R3, au départ)"; fi\n',
     'if [ "$SEGMENT" = 1 ]; then if raison_r3="$(course_deja_partie)"; then refus "$raison_r3 (R3, au départ)"; fi; fi\n', 1),
    (MARQUEUR_V4, MARQUEUR_V5, 1),
    # la course : reprise, pièces du segment, STOP du segment précédent retiré
    (COURSE_LANCEE_V4, COURSE_LANCEE_V5, 1),
    ('--registre-go "$PILOTE/registre-go.md"', '--registre-go "$DS/registre-go.md"', 1),
    (DEPART_REEL_V4, DEPART_REEL_V5, 1),
    (DEPART_SIM_V4, DEPART_SIM_V5, 1),
    (MINUTEUR_COMMENTAIRE_V4, MINUTEUR_COMMENTAIRE_V5, 1),
    (MINUTEUR_V4, MINUTEUR_V5, 1),
    (MINUTEUR_NOTE_V4, MINUTEUR_NOTE_V5, 1),
    (FIN_PROCESSUS_V4, FIN_PROCESSUS_V5, 1),
    # liste fermée : pièces des segments
    (SORTIE_ERREUR_SHA_V4, SORTIE_ERREUR_SHA_V5, 1),
    (PERMIS_V4, PERMIS_V5, 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif in ("lancer_pilote4_gemini_v4.sh", "pilote4-gemini-organisme-v2.md", "b1c7f4b6", "37acdcaa", "N_ESSAIS=141", "ECHEANCE_STOP_S=5700",
              "USD_COURSE=60", '"$PILOTE/essais-v1.', '"$PILOTE/registre-go.md"', "@@"):
    if motif in t:
        sys.exit(f"refus : motif restant après dérivation : {motif}")
for motif, n in (("ECHEANCE_STOP_S=3400", 1), ("USD_COURSE=75", 1), ("COMMUNES+=(--reprendre)", 1), ('if [ -z "$CLORE" ]; then', 1),
                 ("- segment $SEGMENT arrêté par STOP ; reprise attendue : SEGMENT=$((SEGMENT + 1))", 1)):
    if t.count(motif) != n:
        sys.exit(f"refus : {motif} présent {t.count(motif)} fois au lieu de {n}")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")
