"""Dérive le lanceur du quatrième pilote descriptif du lanceur v2 du pilote 3 (`lancer_pilote3_gemini_v5_3_v6_v2.sh`,
add695a9…), par remplacements exacts, chacun au nombre d'occurrences attendu — v3 = v2 (gardée) avec deux chemins
permis de plus dans la banque (`LISEZMOI-v6.md`, `EMPREINTES-banque-v3-v2.txt`, ajoutés par la contre-lecture de la
banque v3, `cfd030a`), la banque servie restant la v3 épinglée (`157a2b45…`) ; l'en-tête produit nomme cette dérivation
et son écart. La v2 était = v1 (gardée) avec la banque
`confrontation-v3` à la place de la v2 (abandonnée sur sa contre-lecture) : chemin, empreinte et message ; chemins
permis élargis aux fichiers de la banque v3 (dont son fichier de clé, jamais lu par le lanceur) et aux contre-lectures
de la banque.

Ce qui change (et rien d'autre) : objets (v5.3 inchangée ; v6.x à la place de la v6) et noms des courses ; banque
`confrontation-v3` (empreinte, chemin) ; chemins permis après le code (pièces du pilote 4, banques v2 et v3) ; quatre
générations notées ; rondes de conception (borne et dollars par ronde, données par la configuration ; 0 = aucune) ;
porte « v5.3 précédente » : générations [0, 1, 2, 3] ; ligne de GO liée au texte scellé (16 premiers caractères de
son empreinte, sur la même ligne) ; journaux recopiés de g000 à g003 et des rondes c001 à c00R ; liste fermée de ce qui
est poussé élargie d'autant ; en-tête.

Usage : python3 -I deriver_lanceur_pilote4_v1.py LANCEUR_V2 CONFIG.json SORTIE
CONFIG.json : {"v6x": {"cle", "nom_affiche", "commit", "arbre", "n_fichiers", "lignee"}, "rondes_conception": R,
"usd_par_ronde": U, "sha_banque": "…" (ou "sha_banque_v2", ancien nom : il porte alors la banque v3)}
Refuse si l'empreinte du lanceur v2 n'est pas add695a9…, si une occurrence n'est pas au nombre attendu, ou si SORTIE
existe (R12).
"""
import hashlib, json, pathlib, sys

SHA_V2 = "add695a90683b59fe9c3a06f0fb7ff70ae46c4067c490c9850988852c814ec76"
SHA_BANQUE_V1 = "f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc"

src, conf_f, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V2:
    sys.exit("refus : le lanceur source n'est pas la v2 add695a9…")
t = b.decode("utf-8")
c = json.loads(conf_f.read_text(encoding="utf-8"))
v6 = c["v6x"]
R, U = int(c["rondes_conception"]), c["usd_par_ronde"]
SB2 = c.get("sha_banque") or c["sha_banque_v2"]
for k in ("cle", "nom_affiche", "commit", "arbre", "n_fichiers", "lignee"):
    if not str(v6.get(k, "")):
        sys.exit(f"refus : v6x.{k} manquant")
if len(SB2) != 64 or len(v6["arbre"]) != 64 or len(v6["commit"]) != 40:
    sys.exit("refus : empreinte mal formée dans la configuration")
K, AFF = v6["cle"], v6["nom_affiche"]          # p. ex. « v6-2 », « v6.2 »
NOM53, NOM6 = "pilote4-gemini-v5-3-v1", f"pilote4-gemini-{K}-v1"

remplacements = []   # (ancien, nouveau, nombre attendu)

# 1. En-tête : lignes 2 à 40 (commentaires) remplacées en bloc
lignes = t.split("\n")
debut = lignes.index("set -euo pipefail")
entete_v2 = "\n".join(lignes[1:debut])
if not all(l.startswith("#") or l == "" for l in lignes[1:debut]):
    sys.exit("refus : en-tête du lanceur v2 inattendu")
conception = (f"{R} rondes de conception au plus avant g000 (l'organisme déclare lui-même la fin de sa conception, "
              f"`fin_conception.json`), {U} USD au plus par ronde" if R else "aucune ronde de conception")
entete_v4 = f"""# Lanceur du quatrième pilote descriptif « organismes assistés de Gemini, v5.3 puis {AFF}, chacun seul, sur la banque
# `confrontation-v3` (identifiants opaques), quatre générations notées, {conception}, question M à g001 »,
# une course par appel (COURSE=v5-3, puis COURSE={K}) — v1, dérivée du lanceur v2 du pilote 3
# (`lancer_pilote3_gemini_v5_3_v6_v2.sh`, `add695a9…`) par `deriver_lanceur_pilote4_v3.py` (remplacements exacts ; écart
# consigné dans `diff-lanceur-pilote3-v2-vers-pilote4-v3.txt`). Ce qui change : les objets ({AFF} à la place de la v6) et
# les noms des courses ; la banque v3 (empreinte, chemin ; les chemins des banques v2 et v3 sont permis après le code) ;
# `--generations 4` ; les rondes de conception ; la porte « v5.3 précédente » attend les générations 0 à 3 ; la ligne de
# GO doit porter aussi les 16 premiers caractères de l'empreinte du texte scellé ; les journaux recopiés et poussés
# couvrent g000 à g003 et les rondes. Tout le reste (porte « M de référence » sur la course M du second pilote, gardes,
# environnement fermé, passerelle, essais du noyau, fermeture, liste fermée) est la ligne du lanceur v2.
# Objets : v5.3 = `canal/gemini-organisme-v5-3`, commit `4ecba58`, dossier `organisme/`, arbre `6251ab21…`, 22 fichiers ;
# {AFF} = branche de Gemini, commit `{v6['commit'][:7]}`, arbre `{v6['arbre'][:8]}…`, {v6['n_fichiers']} fichiers ; lignées « assistées ».
# Les commits d'objets portent aussi l'arbre de la relève : seul `organisme/` en est extrait (`git archive <commit>
# organisme`) ; ils ne sont jamais extraits en entier ni empruntés comme arbre de travail.
# Texte : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v1.md` (ou la version qui le remplace et cite ce
# script) ; pièces : `prereg/pieces-pilote4-gemini/`.
# Usage :
#   MODE=reel COURSE=v5-3 DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO_USD=… \\
#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=… CLE_ANTHROPIC=NOM CLE_GEMINI=NOM \\
#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> \\
#       bash lancer_pilote4_gemini_v1.sh
#   MODE=reel COURSE={K} … PRECEDENTE_V53=<dossier du pilote de la course v5.3 de ce pilote, dans la même copie> (même forme)
#   MODE=simulation : comme le lanceur v2 (variables d'essai inchangées)
#
# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course ou la sortie standard ; arrêter un
# processus (R10 : PID consigné ; une course voisine est détectée, jamais arrêtée) ; écraser un dossier (R12) ; lancer
# une seconde course de même nom (R3)."""
t = "\n".join([lignes[0], entete_v4] + lignes[debut:])

# 2. Course et objets
remplacements += [
    ('COURSE="${COURSE:?COURSE=v5-3 ou COURSE=v6}"', f'COURSE="${{COURSE:?COURSE=v5-3 ou COURSE={K}}}"', 1),
    ('NOM="pilote3-gemini-v5-3-maieutique-v1"; INDICE_GRAINE=0', f'NOM="{NOM53}"; INDICE_GRAINE=0', 1),
    ('  v6)\n    NOM="pilote3-gemini-v6-maieutique-v1"; INDICE_GRAINE=1\n    COMMIT_ORGANISME=7cd7508287efa6fd667eaca7dffe23666f12692f\n'
     '    ARBRE_ORGANISME=940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a\n    N_FICHIERS_ORGANISME=24\n'
     '    LIGNEE="gemini-organisme-v6";;\n  *) refus_tot "COURSE inconnue : $COURSE (v5-3 ou v6)";;',
     f'  {K})\n    NOM="{NOM6}"; INDICE_GRAINE=1\n    COMMIT_ORGANISME={v6["commit"]}\n'
     f'    ARBRE_ORGANISME={v6["arbre"]}\n    N_FICHIERS_ORGANISME={v6["n_fichiers"]}\n'
     f'    LIGNEE="{v6["lignee"]}";;\n  *) refus_tot "COURSE inconnue : $COURSE (v5-3 ou {K})";;', 1),
]
# 3. Banque v2
remplacements += [
    (f"SHA_BANQUE={SHA_BANQUE_V1}", f"SHA_BANQUE={SB2}", 1),
    ('[ "$(sha256sum "$R/banque/banque-confrontation-v1.json" | cut -d\' \' -f1)" = "$SHA_BANQUE" ] || refus "empreinte de la banque ≠ f1387a20…"',
     f'[ "$(sha256sum "$R/banque/banque-confrontation-v3.json" | cut -d\' \' -f1)" = "$SHA_BANQUE" ] || refus "empreinte de la banque ≠ {SB2[:8]}…"', 1),
    ("--taches banque/banque-confrontation-v1.json", "--taches banque/banque-confrontation-v3.json", 1),
]
# 4. Chemins permis après le code
ancien_permis = t[t.index("PERMIS_APRES_CODE='"):].split("\n", 1)[0]
if not ancien_permis.startswith("PERMIS_APRES_CODE='^essaim-m3-refonte-v1/prereg/(") or not ancien_permis.endswith(")$'"):
    sys.exit("refus : PERMIS_APRES_CODE inattendu")
corps = ancien_permis[len("PERMIS_APRES_CODE='^essaim-m3-refonte-v1/prereg/("):-len(")$'")]
nouveau_permis = ("PERMIS_APRES_CODE='^essaim-m3-refonte-v1/(prereg/(" + corps
                  + "|pilote4-gemini-organisme-v[0-9]+\\.md(\\.sha256)?|pieces-pilote4-gemini/.+"
                  + "|contre-lectures/pilote4-gemini-organisme-v[0-9]+-cl[0-9]+\\.md(\\.sha256)?)"
                  + "|banque/(banque-confrontation-v2(-secret)?\\.json(\\.sha256)?|LISEZMOI-v4\\.md(\\.sha256)?"
                  + "|EMPREINTES-banque-v2-v1\\.txt(\\.sha256)?|construction-v2/.+"
                  + "|banque-confrontation-v3(-secret|-cle)?\\.json(\\.sha256)?|LISEZMOI-v[56]\\.md(\\.sha256)?"
                  + "|EMPREINTES-banque-v3-v[12]\\.txt(\\.sha256)?|construction-v3/.+|contre-lectures/.+))$'")
remplacements += [(ancien_permis, nouveau_permis, 1)]
# 5. Porte « v5.3 précédente » (étape 0 bis) : course, nom, générations 0 à 3
remplacements += [
    ('if [ "$COURSE" = v6 ] && { [ "$MODE" = reel ] || [ -n "${PRECEDENTE_V53:-}" ]; }; then',
     f'if [ "$COURSE" = {K} ] && {{ [ "$MODE" = reel ] || [ -n "${{PRECEDENTE_V53:-}}" ]; }}; then', 1),
    ("^pilote3-gemini-v5-3-maieutique-v1(-tentative[0-9]+)?$", f"^{NOM53}(-tentative[0-9]+)?$", 1),
    ("nom autre que pilote3-gemini-v5-3-maieutique-v1[-tentativeN]", f"nom autre que {NOM53}[-tentativeN]", 1),
    ('"v5-3" "pilote3-gemini-v5-3-maieutique-v1")"', f'"v5-3" "{NOM53}")"', 1),
    ('if [g.get("generation") for g in gs] != [0, 1]: pb.append("générations de v5.3 : " + str([g.get("generation") for g in gs]) + " au lieu de [0, 1]")',
     'if [g.get("generation") for g in gs] != [0, 1, 2, 3]: pb.append("générations de v5.3 : " + str([g.get("generation") for g in gs]) + " au lieu de [0, 1, 2, 3]")', 1),
    ('print("v5.3 saine : g000 et g001 OK,', 'print("v5.3 saine : g000 à g003 OK,', 1),
    ("PRECEDENTE_V53 non défini : v6 ne part", f"PRECEDENTE_V53 non défini : {AFF} ne part", 1),
    ("absent : v6 ne part qu'après v5.3", f"absent : {AFF} ne part qu'après v5.3", 1),
    ("empreintes de v5.3 absentes : v6 ne part", f"empreintes de v5.3 absentes : {AFF} ne part", 1),
    ('|| refus "v6 ne part pas : issue de v5.3', f'|| refus "{AFF} ne part pas : issue de v5.3', 1),
    ('if [ "$COURSE" = v6 ] && [ -n "${GRAINE_V53_MANIFESTE:-}" ]; then',
     f'if [ "$COURSE" = {K} ] && [ -n "${{GRAINE_V53_MANIFESTE:-}}" ]; then', 1),
    ('refus "la ligne de dépense de v6 ne porte pas', f'refus "la ligne de dépense de {AFF} ne porte pas', 1),
]
# 6. Ligne de GO liée au texte scellé
ancien_go = ("""  grep "^| $GO_ID |" "$PILOTE/registre-go.md" | grep 'calcul' | grep "${SHA_QUESTION:0:8}" | grep -q "${ARBRE_ORGANISME:0:8}" \\\n"""
             """    || refus "aucune ligne « | $GO_ID | » qui porte à la fois le type calcul, l'empreinte de la question ${SHA_QUESTION:0:8}… et l'empreinte de l'organisme ${ARBRE_ORGANISME:0:8}… (GO non inscrit pour cette course sur cet objet)\"""")
nouveau_go = ("""  # pilote 4 : la ligne porte aussi les 16 premiers caractères de l'empreinte du texte scellé (toujours donné en réel)\n"""
              """  t16="${PREREG_SHA256:-}"; t16="${t16:0:16}"\n"""
              """  ligne_go="$(grep "^| $GO_ID |" "$PILOTE/registre-go.md" | grep 'calcul' | grep "${SHA_QUESTION:0:8}" | grep "${ARBRE_ORGANISME:0:8}" || true)"\n"""
              """  if [ -n "$t16" ]; then ligne_go="$(echo "$ligne_go" | grep "$t16" || true)"; fi\n"""
              """  [ -n "$ligne_go" ] \\\n"""
              """    || refus "aucune ligne « | $GO_ID | » qui porte à la fois le type calcul, l'empreinte de la question ${SHA_QUESTION:0:8}…, l'empreinte de l'organisme ${ARBRE_ORGANISME:0:8}… et celle du texte scellé (${t16:-aucun texte donné en simulation}) (GO non inscrit pour cette course, cet objet et ce texte)\"""")
remplacements += [(ancien_go, nouveau_go, 1)]
remplacements += [("note \"- registre : une ligne $GO_ID de type calcul portant l'empreinte de la question ($COURSE) et celle de l'organisme (${ARBRE_ORGANISME:0:8}…) ;",
                   "note \"- registre : une ligne $GO_ID de type calcul portant l'empreinte de la question ($COURSE), celle de l'organisme (${ARBRE_ORGANISME:0:8}…) et celle du texte scellé (${t16:-aucun texte donné en simulation}) ;", 1)]
# 7. Générations et rondes
fr = (f" --rondes-conception-max {R} --usd-max-conception {U}" if R else " --rondes-conception-max 0")
remplacements += [
    ('--sortie "$PILOTE/course" --generations 2 --graine', '--sortie "$PILOTE/course" --generations 4 --graine', 1),
    ("--entrainements-max 0 --rondes-conception-max 0 --parallele-max 8", f"--entrainements-max 0{fr} --parallele-max 8", 1),
    ("  for g in g000 g001; do", "  for g in g000 g001 g002 g003" + "".join(f" c{k:03d}" for k in range(1, R + 1)) + "; do", 1),
    ("journal-appels-g00[01]\\.jsonl", "journal-appels-(g00[0-3]" + ("|c0[0-9][0-9]" if R else "") + ")\\.jsonl", 1),
]
# 8. Messages et commentaires hérités qui nomment le pilote 3 ou la v6
remplacements += [
    ("Course v6 : ne part qu'après une course v5.3", f"Course {AFF} : ne part qu'après une course v5.3", 1),
    ("nom `pilote3-gemini-v5-3-maieutique-v1`, lignée", f"nom `{NOM53}`, lignée", 1),
    ("#        de v6 porte aussi les 16 premiers", f"#        de {AFF} porte aussi les 16 premiers", 1),
    ("# 3. Organisme de la course (v5.3 ou v6, dossier", f"# 3. Organisme de la course (v5.3 ou {AFF}, dossier", 1),
    ("une course du pilote 3 ne part", "une course du pilote 4 ne part", 4),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
# Restes interdits
for motif in ("pilote3-gemini-v6", "pilote3-gemini-v5-3-maieutique", "pilote 3 ne part", "940c59c3", "7cd7508",
              "banque-confrontation-v1", SHA_BANQUE_V1, "--generations 2", "--taches banque/banque-confrontation-v2",
              "banque/banque-confrontation-v2.json\" | cut"):
    if motif in t:
        sys.exit(f"refus : motif restant après dérivation : {motif}")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements ; en-tête remplacé")
