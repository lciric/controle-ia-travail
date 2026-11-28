P = [
("""#     réécrite entière à la fin ; puis la recherche des fenêtres et des jetons dans toutes les sorties (comme avant).
# Le journal commence""",
"""#     réécrite entière à la fin ; puis la recherche des fenêtres et des jetons dans toutes les sorties (comme avant).
# Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) :
#   6. délai externe du run (VC2-fidelite-07) : commit d'essai du délai, copie du script de l'instance dont seule la
#      ligne DELAI change (90 minutes → DELAI_ESSAI, réglé dans la fenêtre mesurée du run jouet : après l'écriture du
#      manifeste, avant la fin ; ligne comptée), BRANCHE=calcul/p4-jouet-s-v1, joué après les passages 1 et 5, seul
#      pendant son run → TERM du `timeout` pendant le run, arrêt consigné par le module (résumé avec motif), code 124 du
#      run, partiels poussés (code 1) ; sa récupération, sur le commit d'essai du délai, est conforme (code 0, motif
#      « signal TERM reçu (délai externe du run… » affiché par le filtre, destruction) ;
#   - VC2-fidelite-03 : heure limite de destruction relue dans arret.txt (passage 1 : arret.txt factice de cette
#     instance), repli déclaré sans lui (passage 3) ou avec un arret.txt d'une autre instance (gardes réelles), et
#     dépassée (cas sain « limite-depassee » : création vieille de 200 000 s ; ligne écrite, destruction faite) ;
#   - VC2-fidelite-04 : refus en code 2 des traces d'un autre lancement, avec l'état de l'instance et l'heure limite ;
#   - VC2-fidelite-08 : repli de l'affichage à la forme la plus stricte, éprouvé par deux artefacts : « repli de
#     l'affichage » (module commun de S illisible) et « textes absents » (copie de la même récupération dont seul le
#     chemin des textes honnêtes de S change, vers un fichier absent de S) ; attendus : code 1, KO 4f de forme fixe,
#     aucune destruction, chaque autre ligne entière seulement si c'est une ligne OK, KO ou « -- » (forme fixe), sinon
#     réduite à sa longueur et son empreinte courte (la ligne « 4a arrêt » réduite), la ligne de l'instance gardée
#     réécrite entière à la fin.
# Le journal commence"""),
("""N=$(PYTHONPATH=src "$PY" -B -m pytest --collect-only""",
"""DELAI_ESSAI=6s           # sixième passage : délai externe réduit ; run jouet mesuré seul : manifeste écrit à 2,3 à 3,2 s,
                         # résumé complet vers 8,5 s (…/chaine-v4-travail/essai-delai-1.log) : 6 s tombe pendant le run
N=$(PYTHONPATH=src "$PY" -B -m pytest --collect-only"""),
("""ESSAI5=$(git rev-parse HEAD); git checkout -q main || exit 2
echo "commit d'essai de l'arrêt : configuration $ARRET ; préenregistrement jouet $(cut -c1-12 "$R/prereg-jouet-arret.txt")\"""",
"""ESSAI5=$(git rev-parse HEAD); git checkout -q main || exit 2
echo "commit d'essai de l'arrêt : configuration $ARRET ; préenregistrement jouet $(cut -c1-12 "$R/prereg-jouet-arret.txt")"
# commit d'essai du délai (sixième passage, chaîne v4, VC2-fidelite-07) : copie du script de l'instance dont seule la ligne
# DELAI change (90 minutes → DELAI_ESSAI), rescellée ; branche locale « essai-delai »
git checkout -q -b essai-delai || exit 2
sed "s/^DELAI=(timeout --signal=TERM --kill-after=5m 90m)\\$/DELAI=(timeout --signal=TERM --kill-after=5m $DELAI_ESSAI)/" \\
    "$V/p4_instance_v1.sh" > "$R/instance-delai.sh" || exit 2
ND=$(diff "$V/p4_instance_v1.sh" "$R/instance-delai.sh" | grep -c '^>')
[ "$ND" = 1 ] || { echo "copie du script de l'instance du sixième passage : $ND ligne(s) changée(s) au lieu d'une"; exit 2; }
cp "$R/instance-delai.sh" "$V/p4_instance_v1.sh" && (cd "$V" && sha256sum p4_instance_v1.sh > p4_instance_v1.sh.sha256) || exit 2
git add "$V/p4_instance_v1.sh" "$V/p4_instance_v1.sh.sha256" && git commit -qm "essai : délai externe du run réduit ($DELAI_ESSAI), sixième passage" || exit 2
# shellcheck disable=SC2086
git diff --quiet "$CE" HEAD -- $GELES || { echo "commit d'essai du délai : arbre gelé ≠ celui de C"; exit 2; }
ESSAI6=$(git rev-parse HEAD); git checkout -q main || exit 2
echo "commit d'essai du délai : lignes changées dans la copie du script de l'instance : $ND (DELAI 90m → $DELAI_ESSAI)\""""),
("""# passages 1 et 5 en même temps (chacun joue la suite complète ; dossiers, branches et TMPDIR distincts), puis 2, 3, 4 ;
# sorties écrites dans l'ordre des passages
passage 5-arret-du-module calcul/p4-jouet-r-v1 "$VENV" "$R/source/$V/amorce_instance_p4_v1.sh" "$ESSAI5" > "$R/passage-5.out" 2>&1 &
PID_P5=$!
passage 1-sain calcul/p4-jouet-a-v1 > "$R/passage-1.out" 2>&1
passage 2-artefact-branche-presente calcul/p4-jouet-a-v1 > "$R/passage-2.out" 2>&1
passage 3-manque calcul/p4-jouet-b-v1 "$R/environnement-absent" > "$R/passage-3.out" 2>&1
passage 4-plafond-de-l-amorce calcul/p4-jouet-p-v1 "$VENV" "$R/amorce-plafond.sh" > "$R/passage-4.out" 2>&1
wait "$PID_P5"
cat "$R/passage-1.out" "$R/passage-2.out" "$R/passage-3.out" "$R/passage-4.out" "$R/passage-5.out\"""",
"""# passages 1 et 5 en même temps (chacun joue la suite complète ; dossiers, branches et TMPDIR distincts) ; puis le
# sixième (chaîne v4), lancé seul en arrière-plan : sa suite complète dure plus que les passages 2, 3, 4, les
# récupérations et les artefacts qui suivent, et son run jouet tourne seul (délai réglé sur la durée mesurée du run) ;
# sorties écrites dans l'ordre des passages, la sixième après les artefacts
passage 5-arret-du-module calcul/p4-jouet-r-v1 "$VENV" "$R/source/$V/amorce_instance_p4_v1.sh" "$ESSAI5" > "$R/passage-5.out" 2>&1 &
PID_P5=$!
passage 1-sain calcul/p4-jouet-a-v1 > "$R/passage-1.out" 2>&1
wait "$PID_P5"
passage 6-delai-externe calcul/p4-jouet-s-v1 "$VENV" "$R/source/$V/amorce_instance_p4_v1.sh" "$ESSAI6" > "$R/passage-6.out" 2>&1 &
PID_P6=$!
passage 2-artefact-branche-presente calcul/p4-jouet-a-v1 > "$R/passage-2.out" 2>&1
passage 3-manque calcul/p4-jouet-b-v1 "$R/environnement-absent" > "$R/passage-3.out" 2>&1
passage 4-plafond-de-l-amorce calcul/p4-jouet-p-v1 "$VENV" "$R/amorce-plafond.sh" > "$R/passage-4.out" 2>&1
cat "$R/passage-1.out" "$R/passage-2.out" "$R/passage-3.out" "$R/passage-4.out" "$R/passage-5.out\""""),
("""traces_lancement "$R/lancement-essai" "$ESSAI"
traces_lancement "$R/lancement-essai-arret" "$ESSAI5"
traces_lancement "$R/lancement-autre" "$CE\"""",
"""traces_lancement "$R/lancement-essai" "$ESSAI"
traces_lancement "$R/lancement-essai-arret" "$ESSAI5"
traces_lancement "$R/lancement-essai-delai" "$ESSAI6"
traces_lancement "$R/lancement-autre" "$CE"
# chaîne v4 (VC2-fidelite-03) : traces d'un lancement créé il y a 200 000 s (heure limite de repli dépassée) ; arret.txt
# factices écrits comme ceux d'arreter_p4_v1.sh, de cette instance et d'une autre
mkdir -p "$R/lancement-ancien" && printf 'commit %s\\ncreation %s\\nsuccès : True ; identifiant %s ; message : essai\\n' "$ESSAI" "$(( $(date -u +%s) - 200000 ))" "$ID" > "$R/lancement-ancien/lancement.txt"
arret_factice() {   # $1 dossier, $2 identifiant
    local fin; fin=$(date -u +%FT%TZ)
    mkdir -p "$1" && printf 'instance %s : étiquette « p4-v1 » relue entière ; état avant l arrêt : running, running\\n%s : vastai stop instance %s demandé\\n%s : instance %s relue arrêtée deux fois de suite (exited, stopped), 2 lecture(s)\\nARRÊT CONFIRMÉ : INSTANCE %s ARRÊTÉE PAR SON IDENTIFIANT (%s)\\n' \\
        "$2" "$fin" "$2" "$fin" "$2" "$2" "$fin" > "$1/arret.txt"
}
arret_factice "$R/arret-essai" "$ID"
arret_factice "$R/arret-autre" 88888888"""),
("""recuperer() {   # $1 nom, $2 copie, puis les variables du faux outil (S_REC : commit S ; TRACES_REC : traces du lancement)
    local n=$1 copie=$2 c; shift 2
    mkdir -p "$R/vastai-$n"
    env PATH="$R/bin-vastai:/usr/bin:/bin" HOME="$R" LANG=C.UTF-8 HF_TOKEN="$JETON_HF" CONTROLE_IA_GITHUB_TOKEN="$JETON_GH" \\
        GH_TOKEN="$JETON_GH" VAST_API_KEY=factice-vast-0000 FAUX_VASTAI_ETAT="$R/vastai-$n" PYTHONDONTWRITEBYTECODE=1 "$@" \\
        bash "$copie" "${S_REC:-$ESSAI}" "$ID" "${TRACES_REC:-$R/lancement-essai}" "$R/recuperation-$n" > "$R/recuperation-$n.txt" 2>&1; c=$?""",
"""recuperer() {   # $1 nom, $2 copie, puis les variables du faux outil (S_REC : commit S ; TRACES_REC : traces du lancement ;
                # chaîne v4 : ARRET_REC, arret.txt passé en cinquième argument)
    local n=$1 copie=$2 c; shift 2
    local a=("${S_REC:-$ESSAI}" "$ID" "${TRACES_REC:-$R/lancement-essai}" "$R/recuperation-$n"); [ -n "${ARRET_REC:-}" ] && a+=("$ARRET_REC")
    mkdir -p "$R/vastai-$n"
    env PATH="$R/bin-vastai:/usr/bin:/bin" HOME="$R" LANG=C.UTF-8 HF_TOKEN="$JETON_HF" CONTROLE_IA_GITHUB_TOKEN="$JETON_GH" \\
        GH_TOKEN="$JETON_GH" VAST_API_KEY=factice-vast-0000 FAUX_VASTAI_ETAT="$R/vastai-$n" PYTHONDONTWRITEBYTECODE=1 "$@" \\
        bash "$copie" "${a[@]}" > "$R/recuperation-$n.txt" 2>&1; c=$?"""),
("""copie_recuperation a "$R/recuperation-a.sh"
recuperer passage-1-sain "$R/recuperation-a.sh\"""",
"""copie_recuperation a "$R/recuperation-a.sh"
ARRET_REC=$R/arret-essai/arret.txt recuperer passage-1-sain "$R/recuperation-a.sh\""""),
("""cmp -s "$R/recuperation-g.sh" "$R/source/$V/recuperation_p4_v1.sh" || { echo "copie des gardes réelles ≠ copie versée"; exit 2; }
recuperer gardes-reelles "$R/recuperation-g.sh\"""",
"""cmp -s "$R/recuperation-g.sh" "$R/source/$V/recuperation_p4_v1.sh" || { echo "copie des gardes réelles ≠ copie versée"; exit 2; }
ARRET_REC=$R/arret-autre/arret.txt recuperer gardes-reelles "$R/recuperation-g.sh\""""),
("""copie_recuperation a "$R/recuperation-w.sh"
recuperer textes-degeneres "$R/recuperation-w.sh\"""",
"""copie_recuperation a "$R/recuperation-w.sh"
recuperer textes-degeneres "$R/recuperation-w.sh"
# chaîne v4 (VC2-fidelite-03) : heure limite de repli dépassée (création vieille de 200 000 s) : ligne écrite, sans
# retarder la destruction (cas sain, code 0)
TRACES_REC=$R/lancement-ancien recuperer limite-depassee "$R/recuperation-a.sh\""""),
("""recuperer artefact-repli-de-l-affichage "$R/recuperation-ri.sh"
python3 - "$R/recuperation-artefact-repli-de-l-affichage.txt" "$(cat "$R/code-artefact-repli-de-l-affichage.txt")" "$NR" \\
    "$R/vastai-artefact-repli-de-l-affichage/journal" <<'PYR'
import re, sys
from pathlib import Path
sortie, code, nr, journal = sys.argv[1:5]
lignes = Path(sortie).read_text(encoding="utf-8", errors="replace").rstrip("\\n").split("\\n")
forme = re.compile(r"^.{0,40} \\([0-9]+ caractères, empreinte [0-9a-f]{12}\\)$")
derniere = lignes[-1]
filtrees = lignes[:-1]
constats = {
    "copie à une ligne changée": nr == "1",
    "code 1": code == "1",
    "aucune destruction demandée": not Path(journal).exists() or "destroy" not in Path(journal).read_text(),
    "chaque ligne filtrée réduite (40 caractères, longueur, empreinte)": bool(filtrees) and all(forme.fullmatch(x) for x in filtrees),
    "KO 4f": any(x.startswith("KO  4f ") for x in filtrees),
    "ligne « 4a arrêt » réduite": any(x.startswith("--  4a arrêt : ") for x in filtrees),
    "affichage filtré sans échec": not any("AFFICHAGE FILTRÉ EN ÉCHEC" in x for x in lignes),
    "instance gardée réécrite entière à la fin": derniere.startswith("--  8 instance 99999999 gardée, non détruite : état ")
        and "heure limite de destruction" in derniere and not forme.fullmatch(derniere),
}
if all(constats.values()):
    print("récupération en repli de l'affichage (artefact-repli-de-l-affichage) : code 1 ; KO 4f ; chaque ligne filtrée "
          "réduite à ses 40 premiers caractères, sa longueur et son empreinte courte ; instance gardée, état et heure "
          "limite de destruction écrits ; aucune destruction")
else:
    print("REPLI DE L'AFFICHAGE NON ÉTABLI : " + " ; ".join(k for k, v in constats.items() if not v))
PYR""",
"""recuperer artefact-repli-de-l-affichage "$R/recuperation-ri.sh"
# chaîne v4 (VC2-fidelite-08) : textes honnêtes de S absents (chemin des textes vers un fichier absent de S)
sed "s|^TEXTES_P3=[^ ]* |TEXTES_P3=donnees/synth/textes-absents-p3.jsonl |" "$R/recuperation-i2.sh" > "$R/recuperation-ta.sh"
NT=$(diff "$R/recuperation-i2.sh" "$R/recuperation-ta.sh" | grep -c '^>')
echo "lignes changées dans la copie de la récupération des textes absents (recuperation-ta.sh, depuis recuperation-i2.sh) : $NT"
recuperer artefact-textes-absents "$R/recuperation-ta.sh"
# contrôle du repli à la forme la plus stricte (chaîne v4, VC2-fidelite-08), pour chacun des deux artefacts
for x in "artefact-repli-de-l-affichage:$NR" "artefact-textes-absents:$NT"; do
python3 - "$R/recuperation-${x%%:*}.txt" "$(cat "$R/code-${x%%:*}.txt")" "${x#*:}" "$R/vastai-${x%%:*}/journal" "${x%%:*}" <<'PYR'
import re, sys
from pathlib import Path
sortie, code, nr, journal, nom = sys.argv[1:6]
lignes = Path(sortie).read_text(encoding="utf-8", errors="replace").rstrip("\\n").split("\\n")
reduite = re.compile(r"^(?:(?:OK|KO|--)  [0-9]{1,2}[a-z]? )?\\(ligne de [0-9]+ caractères, empreinte [0-9a-f]{12}\\)$")
KO4F = ("KO  4f module commun de S ou textes honnêtes de P3 de S illisibles : recherche des fenêtres et filtre de l'affichage "
        "impossibles (repli : jetons masqués ; seules les lignes OK, KO et -- de forme fixe affichées, les autres par leur "
        "longueur et leur empreinte courte)")
derniere = lignes[-1]
filtrees = lignes[:-1]
constats = {
    "copie à une ligne changée": nr == "1",
    "code 1": code == "1",
    "aucune destruction demandée": not Path(journal).exists() or "destroy" not in Path(journal).read_text(),
    "chaque ligne filtrée réduite (longueur, empreinte), ou ligne OK, KO ou -- entière": bool(filtrees)
        and all(reduite.fullmatch(x) or x[:4] in ("OK  ", "KO  ", "--  ") for x in filtrees),
    "KO 4f de forme fixe, une fois": filtrees.count(KO4F) == 1,
    "ligne « 4a arrêt » réduite": any(re.fullmatch(r"--  4a \\(ligne de [0-9]+ caractères, empreinte [0-9a-f]{12}\\)", x) for x in filtrees)
        and not any(x.startswith("--  4a arrêt") for x in filtrees),
    "tête de la branche, verdict et lignes libres réduits": not any(x.startswith(("tête de la branche", "RÉCUPÉRATION", "RUN=", "TETE="))
                                                                     for x in filtrees),
    "heure limite écrite entière (forme fixe)": any(x.startswith("--  8 heure limite de destruction ") for x in filtrees),
    "affichage filtré sans échec": not any("AFFICHAGE FILTRÉ EN ÉCHEC" in x for x in lignes),
    "instance gardée réécrite entière à la fin": derniere.startswith("--  8 instance 99999999 gardée, non détruite : état ")
        and "heure limite de destruction" in derniere and not reduite.fullmatch(derniere),
}
if all(constats.values()):
    print(f"récupération en repli de l'affichage ({nom}) : code 1 ; KO 4f ; seules les lignes OK, KO et -- de forme fixe "
          "affichées, les autres par leur longueur et leur empreinte courte ; instance gardée réécrite entière, état et "
          "heure limite de destruction écrits ; aucune destruction")
else:
    print(f"REPLI DE L'AFFICHAGE NON ÉTABLI ({nom}) : " + " ; ".join(k for k, v in constats.items() if not v))
PYR
done
# sixième passage (chaîne v4, VC2-fidelite-07) : attendu, puis sa récupération, sur le commit d'essai du délai
wait "$PID_P6"
cat "$R/passage-6.out"
git -C "$R/distant.git" branch -a | grep -F "calcul/p4-jouet-s-v1" | sed 's/^/branche distante : /'
copie_recuperation s "$R/recuperation-s.sh"
S_REC=$ESSAI6 TRACES_REC=$R/lancement-essai-delai recuperer passage-6-delai-externe "$R/recuperation-s.sh\""""),
]
