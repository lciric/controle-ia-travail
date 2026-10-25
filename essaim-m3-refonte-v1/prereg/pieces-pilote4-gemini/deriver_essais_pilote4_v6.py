"""Dérive la batterie d'essais v6 du lanceur du pilote 4 de la batterie v5 (`essais_lanceur_pilote4_v5.sh`, e216c39e…),
par remplacements exacts au nombre attendu et cas ajoutés, pour le lanceur v5 (reprise par segments, 75 USD par course,
minuteur à 3 400 s ; décisions de Lazar, 25 octobre 2026, 20:23 Paris) :

- constantes : noyau 8e5e2f7b (169 essais), lanceur v5 nommé ;
- le cas « minuteur à échéance 0 » de la v5 (STOP dès le manifeste, archive fermée) devient la reprise par segments :
  segment 1 arrêté par le minuteur (état de reprise, course ouverte, rien à pousser), refus du segment 2 sur artefacts
  (ordre des segments, ligne de dépense « segment 2 » absente, reste insuffisant, verrou du segment, marqueur d'un autre
  dossier, HEAD déplacé, autre lanceur, état de reprise altéré, reprise refusée par le noyau — code 9 —, organisme et
  question modifiés entre deux segments), puis segment 2 sain jusqu'au bout (archive fermée, pièces du segment
  poussées, extrait : un arrêt sur STOP, une reprise, générations 0 à 3) ; trois segments (états v1 et v2) ; fermeture
  sans reprise (CLORE=1) ; porte « v5.3 précédente » de la v6.1 sur la v5.3 en segments (saine), et ses artefacts
  (arrêt sur STOP sans reprise, deux arrêts pour une reprise, dernier code non nul, v5.3 fermée sans reprise) ; refus
  des valeurs de SEGMENT et de CLORE ; course fermée ou absente.

Usage : python3 -I deriver_essais_pilote4_v6.py ESSAIS_V5 SORTIE
Refuse si l'empreinte de la batterie v5 n'est pas e216c39e…, si une occurrence n'est pas au nombre attendu, ou si SORTIE
existe (R12).
"""
import hashlib, pathlib, sys

SHA_V5 = "e216c39e8926d71bd598fc3a7200bcb2f3da9a70b64f99e7ef82988d758a3de5"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V5:
    sys.exit("refus : la batterie source n'est pas la v5 e216c39e…")
t = b.decode("utf-8")

MINUTEUR_V5 = '''cas minuteur-echeance "minuteur : STOP posé dans course/" -- MODE=simulation ESSAI_ECHEANCE_STOP_S=0 "${SAIN[@]}"
verifier minuteur-echeance-present "STOP du minuteur présent dans course/ à la fin de la course" "$E/cas-minuteur-echeance"/*/LANCEMENT.md
verifier minuteur-echeance-archive "archive fermée : ferme.tar.gz" "$E/cas-minuteur-echeance"/*/LANCEMENT.md
verifier minuteur-echeance-pousse "ferme.tar.gz" "$E/cas-minuteur-echeance"/*/A-POUSSER-v1.txt
"$PY" -I -c \'
import json, sys
x = json.load(open(sys.argv[1], encoding="utf-8"))
arret = [e for e in x.get("evenements", []) if e.get("etape") in ("arret", "arret_conception")]
gens = [g.get("generation") for g in x.get("generations", []) if not g.get("phase")]
print("relevé (non compté) : événements d arrêt", [e.get("etape") for e in arret], "; générations notées", gens)
\' "$(ls -d "$E/cas-minuteur-echeance"/*/ | head -1)extrait-mecanique-v1.json" || echo "relevé (non compté) : extrait illisible"
'''

SEGMENTS_V6 = r'''echo "== lanceur v5 : reprise par segments (décision de Lazar, 25 octobre 2026, 20:23 Paris) =="
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
copie_ps() {  # copie_ps NOM → chemin d'une copie de la v5.3 en segments
  local d="$E/ps-alteree-$1/pilote4-gemini-v5-3-v1"; rm -rf "$E/ps-alteree-$1"; mkdir -p "$E/ps-alteree-$1"; cp -a "$PS" "$d"; echo "$d"
}
td_heure "$E/entrees/td-seg-1.json" 0 GO-2026-10-25-02
SEG=(MODE=simulation COURSE=v5-3 GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-seg-1.json" ESSAI_EXIGER_HEURE=1)
{ cat "$E/entrees/dep-sain.md"
  printf '| 2026-10-25 | pilote4-gemini-v5-3-v1 segment 2 | GO-2026-10-25-02 | au plus 75 USD moins la dépense déjà faite | après le segment 1 |\n'
  printf '| 2026-10-25 | pilote4-gemini-v5-3-v1 segment 3 | GO-2026-10-25-02 | au plus 75 USD moins la dépense déjà faite | après le segment 2 |\n'; } > "$E/entrees/dep-segments.md"

echo "-- valeurs de SEGMENT et de CLORE ; course absente ou fermée --"
cas seg-non-entier "SEGMENT doit être un entier ≥ 1, sans zéro en tête : « deux »" -- MODE=simulation SEGMENT=deux
cas seg-zero "sans zéro en tête : « 0 »" -- MODE=simulation SEGMENT=0
cas seg-zero-en-tete "sans zéro en tête : « 02 »" -- MODE=simulation SEGMENT=02
cas clore-au-segment-1 "CLORE=1 ferme une course arrêtée entre deux segments : SEGMENT ≥ 2 exigé" -- MODE=simulation CLORE=1
cas clore-valeur "CLORE vaut 1 ou rien : « oui »" -- MODE=simulation SEGMENT=2 CLORE=oui
cas seg-sans-course "absent (aucune course à reprendre" -- "${SEG[@]}" SEGMENT=2
cas seg-course-fermee "est déjà fermée" -- MODE=simulation COURSE=v5-3 "${SAIN[@]}" SEGMENT=2 PILOTE_RACINE="$E/cas-sain-v5-3"

echo "-- segment 1 arrêté par le minuteur (échéance 0 : STOP dès le manifeste) --"
cas seg-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${SEG[@]}" ESSAI_ECHEANCE_STOP_S=0
RS="$E/cas-seg-segment1"; PS="$RS/pilote4-gemini-v5-3-v1"
verifier seg-segment1-minuteur "état de reprise attendu" "$PS/LANCEMENT.md"
verifier seg-segment1-etat "état de reprise écrit par le noyau : etat-v1.json" "$PS/LANCEMENT.md"
verifier seg-segment1-sortie "rien à pousser avant la fin de la course" "$RS/sortie.txt"
verifier_absent seg-segment1-ouverte "$PS/ferme.tar.gz"
verifier_absent seg-segment1-rien-pousse "$PS/A-POUSSER-v1.txt"

echo "-- segment 2 refusé sur artefacts (la course reste arrêtée, ouverte) --"
cas seg-hors-ordre "le LANCEMENT.md n'attend pas ce segment" -- "${SEG[@]}" SEGMENT=3 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
cas seg-sans-ligne-de-depense "segment 2 non consigné avant dans registres/depenses.md" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS"
cas seg-reste-insuffisant "reste sur GO-2026-10-25-02 = 0.01 USD <" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" RESTE_GO_USD=0.01
mkdir "$RS/.verrou-pilote4-gemini-v5-3-v1-segment2"
cas seg-verrou-du-segment "verrou $RS/.verrou-pilote4-gemini-v5-3-v1-segment2 présent" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
rmdir "$RS/.verrou-pilote4-gemini-v5-3-v1-segment2"
cp -p "$RS/.partis/pilote4-gemini-v5-3-v1" "$E/marqueur-sauve"; printf 'ailleurs 2026-10-25T00:00:00Z\n' > "$RS/.partis/pilote4-gemini-v5-3-v1"
cas seg-marqueur-autre "absent ou d'un autre dossier (R3)" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
cp -p "$E/marqueur-sauve" "$RS/.partis/pilote4-gemini-v5-3-v1"
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
cp -p "$PS/organisme/principal.py" "$E/principal-sauve.py"
cas seg-organisme-modifie "empreinte d'arbre de l'organisme ≠ 6251ab21…" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ARTEFACT=organisme
cp -p "$E/principal-sauve.py" "$PS/organisme/principal.py"
cp -p "$PS/question.md" "$E/question-sauve.md"
cas seg-question-modifiee "empreinte de la question ≠ 8b1c7511…" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ARTEFACT=question
cp -p "$E/question-sauve.md" "$PS/question.md"
j="$PS/course/evenements.jsonl"; cp -p "$j" "$E/journal-sauve.jsonl"; printf '{"etape": "intrus"}\n' >> "$j"
td_heure "$E/entrees/td-seg-2a.json" 0 GO-2026-10-25-02
cas seg-noyau-refuse "reprise refusée par le noyau (code 9" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md" APPEL_CONTROLE_FICHIER="$E/entrees/td-seg-2a.json"
verifier seg-noyau-refuse-motif "la course a bougé depuis l'état" "$PS"/segment-2-t*/sortie-erreur-lanceur.txt
verifier seg-noyau-refuse-code "reprise refusée par le noyau" "$RS/sortie.txt"
verifier_absent seg-noyau-refuse-ouverte "$PS/ferme.tar.gz"
cp -p "$E/journal-sauve.jsonl" "$j"

echo "-- segment 2 sain : la course va au bout et se ferme --"
td_heure "$E/entrees/td-seg-2.json" 0 GO-2026-10-25-02
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

echo "-- porte « v5.3 précédente » de la v6.1 sur la v5.3 en segments --"
EMP_PS="$(cut -d' ' -f1 < "$PS/EMPREINTES-pilote-v1.txt.sha256")"
printf '| 2026-10-25 | pilote4-gemini-v6-1-v1 | GO-2026-10-25-02 | 75 | après M et v5.3, empreintes de M %s, de v5.3 %s |\n' "$EMP_M" "$EMP_PS" > "$E/entrees/dep-v6-apres-segments.md"
cas seg-v6-1-porte-saine "en 2 segment(s) (1 arrêt(s) sur le STOP du minuteur, chacun repris), dernier code 0" -- MODE=simulation COURSE=v6-1 "${SAIN[@]}" PRECEDENTE_V53="$PS" DEPENSES_SOURCE="$E/entrees/dep-v6-apres-segments.md" ESSAI_ARTEFACT=famille
verifier seg-v6-1-porte-saine-v53 "; v5.3 saine : g000 à g003 OK" "$E/cas-seg-v6-1-porte-saine"/*/LANCEMENT.md
d="$(copie_ps sans-reprise)"; extrait_altere "$d" 'x["evenements"] = [e for e in x["evenements"] if e.get("etape") != "reprise"]'; refaire_empreintes "$d"
cas seg-v53-stop-sans-reprise "arrêt de la course : ['fichier STOP', 'aucune lignée active'] ; reprises : []" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_ps deux-stops)"; extrait_altere "$d" 'i = [k for k, e in enumerate(x["evenements"]) if e.get("etape") == "arret"][0]; x["evenements"].insert(i, dict(x["evenements"][i]))'; refaire_empreintes "$d"
cas seg-v53-deux-stops-une-reprise "arrêt de la course : ['fichier STOP', 'fichier STOP', 'aucune lignée active'] ; reprises : [2]" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_ps dernier-code)"; printf -- '- fin du processus (UTC) : 2026-10-25T00:00:00Z ; code de retour : 1 ; essai\n' >> "$d/LANCEMENT.md"; refaire_empreintes "$d"
cas seg-v53-dernier-code-non-nul "code de retour du noyau non nul ou absent" -- "${V6C[@]}" PRECEDENTE_V53="$d"

echo "-- trois segments (états de reprise v1 et v2) --"
td_heure "$E/entrees/td-seg3-1.json" 0 GO-2026-10-25-02
cas seg3-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${SEG[@]}" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-seg3-1.json"
R3S="$E/cas-seg3-segment1"; P3S="$R3S/pilote4-gemini-v5-3-v1"
td_heure "$E/entrees/td-seg3-2.json" 0 GO-2026-10-25-02
cas seg3-segment2 "segment 2 arrêté par STOP ; reprise attendue : SEGMENT=3" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$R3S" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-seg3-2.json"
verifier seg3-etat-v2 "état de reprise écrit par le noyau : etat-v2.json" "$P3S/LANCEMENT.md"
td_heure "$E/entrees/td-seg3-3.json" 0 GO-2026-10-25-02
cas seg3-segment3 "archive fermée : ferme.tar.gz" -- "${SEG[@]}" SEGMENT=3 PILOTE_RACINE="$R3S" DEPENSES_SOURCE="$E/entrees/dep-segments.md" APPEL_CONTROLE_FICHIER="$E/entrees/td-seg3-3.json"
verifier seg3-etat-relu "état de reprise : etat-v2.json, sha256" "$P3S/LANCEMENT.md"
releve_segments "$P3S" > "$E/releve-segments-p3s.txt" 2>&1
verifier seg3-extrait "arrêts ['fichier STOP', 'fichier STOP', 'aucune lignée active'] reprises [2, 3] générations [0, 1, 2, 3]" "$E/releve-segments-p3s.txt"

echo "-- fermeture sans reprise (CLORE=1) --"
td_heure "$E/entrees/td-clore-1.json" 0 GO-2026-10-25-02
cas seg-clore-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${SEG[@]}" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-clore-1.json"
RC="$E/cas-seg-clore-segment1"; PC="$RC/pilote4-gemini-v5-3-v1"
cas seg-clore "CLORE=1 : aucune reprise, aucun appel" -- MODE=simulation COURSE=v5-3 GRAINE="$G_53" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR" REFERENCE_M="$M_REF" SEGMENT=2 CLORE=1 PILOTE_RACINE="$RC"
verifier seg-clore-entete "fermeture sans reprise (CLORE=1)" "$PC/LANCEMENT.md"
verifier seg-clore-archive "archive fermée : ferme.tar.gz" "$PC/LANCEMENT.md"
verifier seg-clore-pousse "ferme.tar.gz" "$PC/A-POUSSER-v1.txt"
verifier_absent seg-clore-sans-essais "$PC/segment-2-t1/essais-v1.txt"
releve_segments "$PC" > "$E/releve-segments-pc.txt" 2>&1
verifier seg-clore-extrait "arrêts ['fichier STOP'] reprises []" "$E/releve-segments-pc.txt"
cas seg-clore-v53-refusee "course v5.3 fermée sans reprise (CLORE=1)" -- "${V6C[@]}" PRECEDENTE_V53="$PC"
'''

remplacements = [
    ("# plus), v5 : la v4 (8e82d9ca…) par `deriver_essais_pilote4_v5.py` pour le lanceur v4 (borne des rondes, minuteur ; banque\n"
     "# autre que la v3 refusée) ; la v4 était dérivée de la batterie v3 du pilote 3",
     "# plus), v6 : la v5 (e216c39e…) par `deriver_essais_pilote4_v6.py` pour le lanceur v5 (reprise par segments, 75 USD par\n"
     "# course, minuteur à 3 400 s) ; la v5 était dérivée de la v4 (8e82d9ca…) pour le lanceur v4 (borne des rondes,\n"
     "# minuteur ; banque autre que la v3 refusée) ; la v4 était dérivée de la batterie v3 du pilote 3", 1),
    ("# Usage : bash essais_lanceur_pilote4_v5.sh ", "# Usage : bash essais_lanceur_pilote4_v6.sh ", 1),
    ("lanceur : lancer_pilote4_gemini_v4.sh, sha256 $H/", "lanceur : lancer_pilote4_gemini_v5.sh, sha256 $H/", 1),
    ('verifier sain-v5-3-essais "essais : 141 passés, 0 sauté, 0 désélectionnés"', 'verifier sain-v5-3-essais "essais : 169 passés, 0 sauté, 0 désélectionnés"', 1),
    ('ESSAI_RESUME_EXISTANT="141 passed"', 'ESSAI_RESUME_EXISTANT="169 passed"', 2),
    ('cas junit-total "essais au lieu de 141"', 'cas junit-total "essais au lieu de 169"', 1),
    ("commits postérieurs à b1c7f4b6 hors des pièces du pilote", "commits postérieurs à 8e5e2f7b hors des pièces du pilote", 4),
    ('echo "== code et commits : chemins permis après b1c7f4b6 =="', 'echo "== code et commits : chemins permis après 8e5e2f7b =="', 1),
    (MINUTEUR_V5, SEGMENTS_V6, 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif in ("lancer_pilote4_gemini_v4.sh", "141 pass", "b1c7f4b6", "cas-minuteur-echeance"):
    if motif in t:
        sys.exit(f"refus : motif restant après dérivation : {motif}")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")
