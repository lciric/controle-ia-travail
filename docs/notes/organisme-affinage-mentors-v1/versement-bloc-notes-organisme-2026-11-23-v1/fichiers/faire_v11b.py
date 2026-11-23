"""Lanceur v11b et ses essais, dérivés des fichiers v11 par remplacements exacts comptés (GO_ID de la course = GO-2026-11-22-80).
Usage : python3 faire_v11b.py RACINE SHA_CONF_V11B"""
import sys
from pathlib import Path
racine, SHA_CONF = Path(sys.argv[1]), sys.argv[2]

def r(src, a, b, n=1):
    k = src.count(a)
    assert k == n, (k, n, a[:100])
    return src.replace(a, b)

src = (racine / "scripts/lancer_course_affinage_mentors_v11.py").read_text(encoding="utf-8")
SHA_V11 = __import__("hashlib").sha256(src.encode("utf-8")).hexdigest()
assert SHA_V11 == "bdca413ca51a04f1f4235ea608886e76492154d2a68b2b2180219e4dd2dc2f79", SHA_V11
# en-tête : ce qui change en v11b
src = r(src, '#!/usr/bin/env python3\n"""', '''#!/usr/bin/env python3\n"""Lanceur v11b (dérivé du lanceur v11, `bdca413c…`, par remplacements exacts ; le v11 reste en place, R12).

Ce qui change en v11b (décision de la mère sur le point ouvert 11 du rapport v11, routine, étage 1) :
1. le GO de la course (`GO_ID`, passé à l'orchestrateur et cité par la commande de lancement) est **GO-2026-11-22-80**,
   prolongation de GO-2026-11-18-14 (calcul, Lazar, 150 USD, échéance 15 décembre) : l'orchestrateur épinglé (`a41b7b50`,
   `configuration_v55.verifier_go_v55`) ne lit que la période de la ligne `GO_ID` ; avec GO-14, il refusait après le 25 ;
2. GO-80 est exigé (refus s'il est absent, révoqué, hors période, s'il n'est pas de Lazar ou ne dit pas prolonger
   GO-2026-11-18-14) ; la ligne de GO-2026-11-18-14 est exigée aussi (calcul, Lazar, non révoquée ; sa propre échéance ne
   borne plus) ; son plafond est lu « 150 USD » (le renvoi entre parenthèses au GO prolongé est admis, sans autre nombre) ;
3. registre dérivé : ligne de GO-80, ligne de GO-14 (traçabilité) et les révocations qui visent l'une ou l'autre ;
4. configuration v11b (`changements_v11.go_course` = GO-2026-11-22-80, exigé égal à `GO_ID`).

''', 1)
src = r(src, '    GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py',
        '    GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11b.py')
src = r(src, 'VERSION = "lancer_course_affinage_mentors_v11"\nGO_ID = "GO-2026-11-18-14"',
        'VERSION = "lancer_course_affinage_mentors_v11b"\nGO_ID = "GO-2026-11-22-80"          # v11b : GO de la course (prolongation de GO-2026-11-18-14)\n'
        'GO_COURSE_INITIAL = "GO-2026-11-18-14"  # v11b : GO prolongé, exigé au registre et gardé au registre dérivé')
src = r(src, '"configuration": (f"{COURSE}/configuration-course-affinage-mentors-v11.json", "25d40914192f2c9a1dc849681bf5c31d76bf58c7f15f428f0ac4515bf69c8567"),',
        f'"configuration": (f"{{COURSE}}/configuration-course-affinage-mentors-v11b.json", "{SHA_CONF}"),')
# plafond de GO-80 : « 150 USD (plafond de GO-2026-11-18-14) »
src = r(src, '''    m_plafond = re.match(r"^\\s*(\\d+(?:[.,]\\d+)?)\\s*(?:USD|usd)\\s*$", plafond)''',
        '''    m_plafond = re.match(r"^\\s*(\\d+(?:[.,]\\d+)?)\\s*(?:USD|usd)\\s*(?:\\([^()0-9]*\\))?\\s*$",
                         re.sub(r"GO-\\d{4}-\\d{2}-\\d{2}-\\d{2,3}", "GO", plafond))  # v11b : renvoi au GO prolongé admis''')
# exception de clé : son plafond renvoie au GO initial
src = r(src, '''    if GO_ID not in plafond:
        raise Refus(f"{go_id} : le plafond doit renvoyer au plafond d'arrêt de {GO_ID}")''',
        '''    if GO_COURSE_INITIAL not in plafond:
        raise Refus(f"{go_id} : le plafond doit renvoyer au plafond d'arrêt de {GO_COURSE_INITIAL}")''')
# verifier_les_go
src = r(src, '''    p80 = lire_prolongation(registre, aujourd_hui, GO_PROLONGATION_COURSE, GO_ID)
    go = verifier_go(registre, aujourd_hui, prolongation=p80.get("echeance") if p80["valide"] else None)''',
        '''    go_conf = (fixe.get("changements_v11") or {}).get("go_course")
    if go_conf != GO_ID:
        raise Refus(f"configuration : changements_v11.go_course = {go_conf!r}, {GO_ID} exigé (GO de la course, v11b)")
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    p80 = lire_prolongation(registre, aujourd_hui, GO_PROLONGATION_COURSE, GO_COURSE_INITIAL)
    if not p80["valide"]:  # v11b : GO-80 est le GO de la course ; absent ou invalide, la course ne part pas
        raise Refus(f"{GO_PROLONGATION_COURSE} (GO de la course, prolongation de {GO_COURSE_INITIAL}) non valide : {p80['motif']}")
    go = verifier_go(registre, aujourd_hui)
    p80 = dict(p80, go_initial=verifier_go_initial(registre))''')
src = r(src, '''GO_PROLONGATION_COURSE = "GO-2026-11-22-80"   # prolonge GO-2026-11-18-14 au 15 décembre
''', '''GO_PROLONGATION_COURSE = "GO-2026-11-22-80"   # prolonge GO-2026-11-18-14 au 15 décembre
assert GO_PROLONGATION_COURSE == GO_ID          # v11b : la prolongation est le GO de la course


def verifier_go_initial(registre: Path) -> dict:
    """v11b : la ligne de GO-2026-11-18-14 (prolongé par GO-80) est exigée : une seule, de type « calcul », accordée par Lazar,
    non révoquée ; sa propre échéance ne borne plus (la période est celle de GO-80)."""
    c, rev = lire_ligne_go(registre, GO_COURSE_INITIAL)
    if c is None:
        raise Refus(f"{GO_COURSE_INITIAL} (GO prolongé par {GO_ID}) : ligne absente ou mal formée")
    ident, accorde, typ, _perimetre, _plafond, echeance, par, _ref = c
    if typ != "calcul" or par != "Lazar":
        raise Refus(f"{GO_COURSE_INITIAL} : type {typ!r} accordé par {par!r} (« calcul », Lazar exigés)")
    if rev:
        raise Refus(f"{GO_COURSE_INITIAL} (prolongé par {GO_ID}) révoqué par {', '.join(sorted(rev))}")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}
''')
# registre dérivé : GO-80 et GO-14
src = r(src, '''def ecrire_registre_derive(registre: Path, chemin: Path, go_id: str = GO_ID, commit: str | None = None) -> dict:''',
        '''def ecrire_registre_derive(registre: Path, chemin: Path, go_id: str = GO_ID, commit: str | None = None,
                           go_traces: tuple = (GO_COURSE_INITIAL,)) -> dict:''')
src = r(src, '''        if m.group(1) == go_id and not (len(cellules) == 8 and cellules[3].lower().startswith("extension")):
            gardees.append(ligne)
        elif len(cellules) == 8 and cellules[2] == "révocation" and go_id in (cellules[3] + cellules[7]):
            gardees.append(ligne)''',
        '''        vises = (go_id,) + tuple(go_traces)  # v11b : GO de la course et GO prolongé (traçabilité)
        if m.group(1) in vises and not (len(cellules) == 8 and cellules[3].lower().startswith("extension")):
            gardees.append(ligne)
        elif len(cellules) == 8 and cellules[2] == "révocation" and any(g in (cellules[3] + cellules[7]) for g in vises):
            gardees.append(ligne)''')
(racine / "scripts/lancer_course_affinage_mentors_v11b.py").write_text(src, encoding="utf-8")
print("lanceur v11b :", len(src.splitlines()), "lignes")
