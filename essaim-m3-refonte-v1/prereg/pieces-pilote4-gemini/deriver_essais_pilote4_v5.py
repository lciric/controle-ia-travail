"""Dérive la batterie d'essais v5 du lanceur du pilote 4 de la batterie v4 (`essais_lanceur_pilote4_v4.sh`, 8e82d9ca…),
par remplacements exacts au nombre attendu et cas ajoutés, pour le lanceur v4 (contre-lecture 1 du texte du pilote 4) :

- lanceur v4 nommé (cas `m-lanceur-pilote3`) ;
- cas sains : le `LANCEMENT.md` de la v5.3 et de la v6.1 dit « temps par ronde de conception 900 s » (manifeste,
  P4C1-02 c) et « STOP non posé » (minuteur arrêté par son PID à la fin de la course, P4C1-02 d) ;
- P4C1-06 (R5) : banque autre que la v3 refusée, par le crochet `ESSAI_ARTEFACT=banque` et par un commit qui copie la
  banque v2 au chemin de la v3 ;
- P4C1-02 d (R5) : minuteur à échéance 0 en simulation (STOP posé dès le manifeste ; course arrêtée avant la ronde ou la
  génération suivante ; archive fermée) ; échéance d'essai non entière refusée ; variable d'essai du minuteur refusée en
  mode réel.

Usage : python3 -I deriver_essais_pilote4_v5.py ESSAIS_V4 SORTIE
Refuse si l'empreinte de la batterie v4 n'est pas 8e82d9ca…, si une occurrence n'est pas au nombre attendu, ou si SORTIE
existe (R12).
"""
import hashlib, pathlib, sys

SHA_V4 = "8e82d9ca64a581087bf096a34a6a6e93b5e8ded49b508bce70dbcabe7d877f97"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V4:
    sys.exit("refus : la batterie source n'est pas la v4 8e82d9ca…")
t = b.decode("utf-8")

AJOUTS_FIN = '''cas imprevu "fichiers imprévus, NON poussés" -- MODE=simulation ESSAI_ARTEFACT=imprevu "${SAIN[@]}"
echo "== lanceur v4 (contre-lecture 1 du pilote 4) : banque autre que la v3 (P4C1-06) ; minuteur (P4C1-02) =="
cas banque-crochet "empreinte de la banque ≠ 157a2b45…" -- MODE=simulation ESSAI_ARTEFACT=banque "${SAIN[@]}"
cp "$DEPOT/essaim-m3-refonte-v1/banque/banque-confrontation-v2.json" "$DEPOT/essaim-m3-refonte-v1/banque/banque-confrontation-v3.json"
git -C "$DEPOT" add essaim-m3-refonte-v1/banque/banque-confrontation-v3.json; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : banque v2 copiée au chemin de la v3"
cas banque-v2-au-chemin-v3 "empreinte de la banque ≠ 157a2b45…" -- MODE=simulation "${SAIN[@]}"
git -C "$DEPOT" reset -q --hard HEAD~1
cas minuteur-echeance "minuteur : STOP posé dans course/" -- MODE=simulation ESSAI_ECHEANCE_STOP_S=0 "${SAIN[@]}"
verifier minuteur-echeance-present "STOP du minuteur présent dans course/ à la fin de la course" "$E/cas-minuteur-echeance"/*/LANCEMENT.md
verifier minuteur-echeance-archive "archive fermée : ferme.tar.gz" "$E/cas-minuteur-echeance"/*/LANCEMENT.md
verifier minuteur-echeance-pousse "ferme.tar.gz" "$E/cas-minuteur-echeance"/*/A-POUSSER-v1.txt
"$PY" -I -c '
import json, sys
x = json.load(open(sys.argv[1], encoding="utf-8"))
arret = [e for e in x.get("evenements", []) if e.get("etape") in ("arret", "arret_conception")]
gens = [g.get("generation") for g in x.get("generations", []) if not g.get("phase")]
print("relevé (non compté) : événements d arrêt", [e.get("etape") for e in arret], "; générations notées", gens)
' "$(ls -d "$E/cas-minuteur-echeance"/*/ | head -1)extrait-mecanique-v1.json" || echo "relevé (non compté) : extrait illisible"
cas minuteur-echeance-non-entiere "ESSAI_ECHEANCE_STOP_S doit être un entier (secondes)" -- MODE=simulation ESSAI_ECHEANCE_STOP_S=abc "${SAIN[@]}"
cas reel-echeance-minuteur "variable ESSAI_ECHEANCE_STOP_S définie en mode réel" -- MODE=reel PILOTE_RACINE=- ESSAI_ECHEANCE_STOP_S=5
'''

remplacements = [
    ("# plus), v4, dérivés de la batterie v3 du pilote 3",
     "# plus), v5 : la v4 (8e82d9ca…) par `deriver_essais_pilote4_v5.py` pour le lanceur v4 (borne des rondes, minuteur ; banque\n"
     "# autre que la v3 refusée) ; la v4 était dérivée de la batterie v3 du pilote 3", 1),
    ("# Usage : bash essais_lanceur_pilote4_v4.sh ", "# Usage : bash essais_lanceur_pilote4_v5.sh ", 1),
    ("lanceur : lancer_pilote4_gemini_v3.sh, sha256 $H/", "lanceur : lancer_pilote4_gemini_v4.sh, sha256 $H/", 1),
    ('verifier sain-v5-3-registre "registre : une ligne GO-2026-10-25-02 de type calcul" "$V53/LANCEMENT.md"\n',
     'verifier sain-v5-3-registre "registre : une ligne GO-2026-10-25-02 de type calcul" "$V53/LANCEMENT.md"\n'
     'verifier sain-v5-3-temps-conception "temps par ronde de conception 900 s" "$V53/LANCEMENT.md"\n'
     'verifier sain-v5-3-minuteur "STOP non posé" "$V53/LANCEMENT.md"\n', 1),
    ('verifier sain-v6-1-graine "graine $G_6 de la course v6-1 écrite et recalculée" "$V6/LANCEMENT.md"\n',
     'verifier sain-v6-1-graine "graine $G_6 de la course v6-1 écrite et recalculée" "$V6/LANCEMENT.md"\n'
     'verifier sain-v6-1-temps-conception "temps par ronde de conception 900 s" "$V6/LANCEMENT.md"\n'
     'verifier sain-v6-1-minuteur "STOP non posé" "$V6/LANCEMENT.md"\n', 1),
    ('cas imprevu "fichiers imprévus, NON poussés" -- MODE=simulation ESSAI_ARTEFACT=imprevu "${SAIN[@]}"\n', AJOUTS_FIN, 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
if "lancer_pilote4_gemini_v3.sh" in t:
    sys.exit("refus : le lanceur v3 est encore nommé")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")
