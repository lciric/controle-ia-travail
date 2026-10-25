"""Dérive la batterie d'essais v8 du lanceur du pilote 4 de la batterie v7 (`essais_lanceur_pilote4_v7.sh`, c3263af1…),
par remplacements exacts au nombre attendu — contre-lecture 3 du texte du pilote 4
(`prereg/contre-lectures/pilote4-gemini-organisme-v3-cl3.md`, 0d95ea8c…), constat P4C3-03 : des gardes nouvelles du
lanceur v6 n'étaient essayées que sur le cas sain (R5). Le lanceur ne change pas (v6, 50f9c496…). Cas ajoutés :

- au segment 2, sur artefacts : course sans manifeste (l. 208 du lanceur v6) ; verrou du segment 1 absent (l. 209) ;
  autre course de ce nom partie dans un autre dossier (l. 211–213) ; état de reprise d'un autre arrêt, puis d'un autre
  segment, rescellé (compagnon juste, l. 262–263) ; l'état restauré ensuite à l'octet près (vérifié) ;
- porte « v5.3 précédente » : reprises mal numérotées, arrêts justes (l. 338–342) ;
- minuteur au segment K ≥ 2 (l. 769–771) : une copie mutée du lanceur, qui pose `STOP` sans attendre l'événement de
  reprise, fait refuser la reprise par le noyau (code 9, « le fichier STOP est encore dans la course ») — la garde est
  donc effective ; le cas sain reste `seg3-segment2` (même échéance nulle, reprise acceptée).

Usage : python3 -I deriver_essais_pilote4_v8.py ESSAIS_V7 SORTIE
Refuse si l'empreinte de la batterie v7 n'est pas c3263af1…, si une occurrence n'est pas au nombre attendu, ou si SORTIE
existe (R12).
"""
import hashlib, pathlib, sys

SHA_V7 = "c3263af100e53c439bbf7a89a7c7e7597f0e911f150cfa57a30929cb40b0cdea"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V7:
    sys.exit("refus : la batterie source n'est pas la v7 c3263af1…")
t = b.decode("utf-8")

BLOC_SEGMENT = r'''cp -p "$E/etat-v1-sauve.sha256" "$c"
# v8 (contre-lecture 3, P4C3-03) : gardes du segment K ≥ 2 sur artefacts — course sans manifeste, verrou du segment 1
#   absent, autre course de ce nom partie, état de reprise d'un autre arrêt ou d'un autre segment (rescellé) ; chaque
#   artefact retiré après son cas, l'état restauré à l'octet près
mv "$PS/course/manifeste-run.json" "$E/manifeste-ps-sauve.json"
cas seg-sans-manifeste "SEGMENT=2 : aucune course partie dans $PS" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
mv "$E/manifeste-ps-sauve.json" "$PS/course/manifeste-run.json"
mv "$RS/.verrou-pilote4-gemini-v5-3-v1" "$E/verrou-segment1-sauve"
cas seg-verrou-segment1-absent "verrou $RS/.verrou-pilote4-gemini-v5-3-v1 du segment 1 absent" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
mv "$E/verrou-segment1-sauve" "$RS/.verrou-pilote4-gemini-v5-3-v1"
mkdir -p "$RS/pilote4-gemini-v5-3-v1-essai-autre/course"; printf '{}\n' > "$RS/pilote4-gemini-v5-3-v1-essai-autre/course/manifeste-run.json"
cas seg-autre-course-du-nom "une autre course de ce nom est partie dans $RS/pilote4-gemini-v5-3-v1-essai-autre (R3)" -- "${SEG[@]}" SEGMENT=2 PILOTE_RACINE="$RS" DEPENSES_SOURCE="$E/entrees/dep-segments.md"
rm -rf "$RS/pilote4-gemini-v5-3-v1-essai-autre"
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
'''

BLOC_PORTE = r'''cas seg-v53-dernier-code-non-nul "code de retour du noyau non nul ou absent" -- "${V6C[@]}" PRECEDENTE_V53="$d"
d="$(copie_ps reprises-numeros)"; extrait_altere "$d" 'x["evenements"] = [dict(e, segment=3) if e.get("etape") == "reprise" else e for e in x["evenements"]]'; refaire_empreintes "$d"
cas seg-v53-reprises-mal-numerotees "arrêt de la course : ['fichier STOP', 'aucune lignée active'] ; reprises : [3]" -- "${V6C[@]}" PRECEDENTE_V53="$d"
'''

BLOC_MUTANT = r'''echo "-- minuteur au segment K ≥ 2 : copie mutée du lanceur (STOP posé sans attendre la reprise consignée) — la reprise est refusée (P4C3-03) --"
"$PY" -I -c 'import sys
t = open(sys.argv[1], encoding="utf-8").read()
a = "else [ \"$(wc -l < \"$PILOTE/course/evenements.jsonl\")\" -gt \"$N_EV_AVANT\" ]; fi"
assert t.count(a) == 1, t.count(a)
open(sys.argv[2], "w", encoding="utf-8").write(t.replace(a, "else true; fi  # MUTATION (essai) : STOP posé sans attendre la reprise"))' "$LANCEUR" "$E/lanceur-mutant-minuteur.sh"
H_MUT="$(sha256sum "$E/lanceur-mutant-minuteur.sh" | cut -d' ' -f1)"
pr "$E/entrees/prereg-mutant.md" "entropie E = $ENTROPIE tirée au scellement
graine de la course v5-3 = $G_53
graine de la course v6-1 = $G_6
lanceur $H_MUT"
SHA_PRM="$(cut -d' ' -f1 < "$E/entrees/prereg-mutant.md.sha256")"
printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai, lanceur muté) : question `8b1c7511…`, organismes v5.3 `6251ab21…` et v6.1 `ae331d1d…` ; texte %s | au plus 120 USD | 2026-10-31 |\n' "${SHA_PRM:0:16}" > "$E/entrees/go-mutant.md"
MUT=("${SEG[@]}" PREREG="$E/entrees/prereg-mutant.md" PREREG_SHA256="$SHA_PRM" REGISTRE_GO_SOURCE="$E/entrees/go-mutant.md")
LANCEUR_SAIN="$LANCEUR"; LANCEUR="$E/lanceur-mutant-minuteur.sh"
td_heure "$E/entrees/td-mut-1.json" 0 GO-2026-10-25-02
cas mut-minuteur-segment1 "segment 1 arrêté par STOP ; reprise attendue : SEGMENT=2" -- "${MUT[@]}" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-mut-1.json"
RMU="$E/cas-mut-minuteur-segment1"; PMU="$RMU/pilote4-gemini-v5-3-v1"
td_heure "$E/entrees/td-mut-2.json" 0 GO-2026-10-25-02
cas mut-minuteur-segment2 "reprise refusée par le noyau (code 9" -- "${MUT[@]}" SEGMENT=2 PILOTE_RACINE="$RMU" DEPENSES_SOURCE="$E/entrees/dep-segments.md" ESSAI_ECHEANCE_STOP_S=0 APPEL_CONTROLE_FICHIER="$E/entrees/td-mut-2.json"
verifier mut-minuteur-motif "le fichier STOP est encore dans la course" "$PMU"/segment-2-t*/sortie-erreur-lanceur.txt
LANCEUR="$LANCEUR_SAIN"
echo "== état des dépôts d'essai après la série =="
'''

remplacements = [
    ("# plus), v7 : la v6 (b4857c51…) par `deriver_essais_pilote4_v7.py` pour le lanceur v6 (vérification de la reprise\n"
     "# refusée corrigée) ; la v6 était dérivée",
     "# plus), v8 : la v7 (c3263af1…) par `deriver_essais_pilote4_v8.py` (contre-lecture 3, P4C3-03 : gardes du segment\n"
     "# K ≥ 2 et de la porte essayées sur un artefact, minuteur essayé sur une copie mutée du lanceur ; lanceur v6 inchangé) ;\n"
     "# la v7 était dérivée de la v6 (b4857c51…) par `deriver_essais_pilote4_v7.py` pour le lanceur v6 (vérification de la reprise\n"
     "# refusée corrigée) ; la v6 était dérivée", 1),
    ("# Usage : bash essais_lanceur_pilote4_v7.sh ", "# Usage : bash essais_lanceur_pilote4_v8.sh ", 1),
    ('cp -p "$E/etat-v1-sauve.sha256" "$c"\n', BLOC_SEGMENT, 1),
    ('cas seg-v53-dernier-code-non-nul "code de retour du noyau non nul ou absent" -- "${V6C[@]}" PRECEDENTE_V53="$d"\n', BLOC_PORTE, 1),
    ('echo "== état des dépôts d\'essai après la série =="\n', BLOC_MUTANT, 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")
