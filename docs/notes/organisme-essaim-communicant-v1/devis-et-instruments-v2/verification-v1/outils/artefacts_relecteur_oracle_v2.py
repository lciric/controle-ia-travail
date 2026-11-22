"""Artefacts du relecteur contre l'oracle v2 : verdicts sous des noms ou des places que l'auteur n'a pas essayés.
Usage : artefacts_relecteur_oracle_v2.py ORACLE_V2.py DOSSIER_NEUF"""
import copy, importlib.util, json, os, sys

spec = importlib.util.spec_from_file_location("oracle_v2", sys.argv[1])
O2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(O2)
sys.path.insert(0, O2.OUTILS)
import puissance_monde_riche_v1 as P1  # noqa: E402

d = sys.argv[2]
os.makedirs(d, exist_ok=False)


def carte(loi, ident="G1-a-01"):
    return {"identifiant": ident, "generation": 1, "proposeur": "a", "loi": copy.deepcopy(loi)}


def lancer(nom, cartes):
    a = os.path.join(d, f"art-{nom}.json")
    json.dump({"releve": {"cartes": cartes}}, open(a, "x", encoding="utf-8"))
    s = os.path.join(d, f"sortie-{nom}.json")
    try:
        code = O2.main(["x", "--essai", a, s])
    except SystemExit as ex:
        code = ex.code
    classes = None
    fuite = None
    if os.path.exists(s):
        sortie = json.load(open(s, encoding="utf-8"))
        classes = [c["classe"] for c in sortie["cartes"]]
        txt_cartes = json.dumps(sortie["cartes"], ensure_ascii=False)  # la liste noire écrite dans la sortie est exclue
        fuite = [m for m in ("PROMUE", "survit", "promue_juge", "promu", "rang") if m in txt_cartes] or None
    return code, classes, fuite


sv1 = P1.S_V1
print("type de S_V1 :", sv1.get("type"), "| clés :", sorted(sv1))
essais = []
# E1 : clé de sous-population inventée dans « lois » (dict) d'une par_sous_population
psp = {"type": "par_sous_population", "lois": {"0": sv1, "1": sv1, "promue_juge": sv1}}
essais.append(("E1-cle-inventee-dans-lois", [carte(psp)], "refus 3 attendu (champ de verdict sous un nom de sous-population)"))
# E2 : verdict dans la VALEUR de l'identifiant (liste blanche de clés, valeur non contrôlée)
essais.append(("E2-verdict-dans-identifiant", [carte(sv1, "G1-a-01|PROMUE|survit")], "refus attendu si aucun verdict ne doit transiter"))
# E3 : type inconnu porteur d'un champ de verdict (la garde ne lit pas les types inconnus)
essais.append(("E3-type-inconnu-porteur", [carte({"type": "inconnu", "promu": 1, "rang": 2})], "refus 3 attendu, ou « rien » sans fuite"))
# E4 : verdict codé en nombre dans un poids de mélange (canal de contenu, non séparable par la grammaire)
essais.append(("E4-verdict-numerique-dans-poids", [carte({"type": "melange", "composantes": [sv1, sv1], "poids": [0.5, 0.5000001]})], "passe (contenu : non détectable par nom), classe inchangée"))
for nom, cartes, att in essais:
    code, classes, fuite = lancer(nom, cartes)
    print(f"{nom} | {att} | code {code} | classes {classes} | texte de verdict dans la sortie : {fuite}")
