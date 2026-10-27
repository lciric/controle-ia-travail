"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json.
Verifie : empreintes fiche/engagement, liaison de mesures.json a l'engagement, empreinte de l'ordre.
Usage : python3 -I ranger_tirages.py
"""
import hashlib, json, sys

EMPREINTE_FICHE = "463c425fe6b6a7a8beeef533914068a13886b1ecd0d647173bdd293a14c625e5"
EMPREINTE_ENGAGEMENT = "1ecfdd088611b70c4b466d51488993328e6b66a45f191e576de909e7f3953082"


def sha_fichier(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def echec(msg):
    sys.exit("ECHEC : " + msg)


if sha_fichier("fiche.json") != EMPREINTE_FICHE:
    echec("fiche.json modifiee")
if sha_fichier("engagement.json") != EMPREINTE_ENGAGEMENT:
    echec("engagement.json modifie")

engagement = json.load(open("engagement.json"))
mesures = json.load(open("mesures.json"))
ordre = json.load(open("ordre-execution.json"))

if mesures.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
    echec("mesures.json non lie a l'engagement gele")
if ordre.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
    echec("ordre-execution.json non lie a l'engagement gele")

n = len(engagement["instances"])
issues = mesures["issues"]
if len(issues) != n:
    echec("nombre d'issues %d != nombre d'instances %d" % (len(issues), n))
k = engagement.get("nombre_issues", 3)
if not all(isinstance(x, int) and 0 <= x < k for x in issues):
    echec("issue hors domaine")
if sorted(ordre["ordre"]) != list(range(n)):
    echec("ordre n'est pas une permutation du plan")
emp_ordre = hashlib.sha256(json.dumps(ordre["ordre"], separators=(",", ":")).encode()).hexdigest()
if mesures.get("empreinte_ordre") != emp_ordre:
    echec("empreinte de l'ordre incoherente")

tirages = {
    "empreinte_engagement": mesures["empreinte_engagement"],
    "issues": issues,  # rangees a l'indice de leur instance, telles que deposees
    "plan_execution": mesures["plan_execution"],
    "empreinte_ordre": mesures["empreinte_ordre"],
}
with open("tirages.json", "w") as f:
    json.dump(tirages, f, indent=2, ensure_ascii=False)
print("OK : %d issues rangees ; tirages.json sha256 = %s" % (n, sha_fichier("tirages.json")))
