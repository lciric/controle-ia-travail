"""Course à blanc du tour du collisionneur v9 sur la conception de l'organisme d'idéation — v1 (3 novembre 2026, session
développeur de session-depot) : copie de course_a_blanc_kirchner_v1.py (4c3f3f75…, branche 16ec2e5a), seul changement : cet
en-tête. Le texte qui suit, écrit pour Kirchner Q2, vaut tel quel (aucun appel réseau, appelants factices, coûts du brainstorm).
"""
"""Course à blanc du tour du collisionneur v9 sur la question 2 du mentor Kirchner — v1 (3 novembre 2026, session développeur
de session-depot). AUCUN APPEL RÉSEAU : le collisionneur est chargé comme module et sa fonction `principal` reçoit des appelants
factices (paramètre `appelants`, prévu par le script) à la place des quatre appelants réels ; la course passe par le vrai
chemin (`etage3`, portes, plafond vérifié avant chaque appel, journal, cellules scellées, `verifier`).

Chaque réponse factice a la longueur (en caractères) et le nombre de jetons de sortie de la même cellule dans le tour
« brainstorm » du 2 novembre (journal `donnees/collisionneur-v9-brainstorm-v1-suite/run-brainstorm-e3-v1/journal.jsonl`,
commit 42aa6b1b ; pour E3-T3-reponse-D, l'essai 2, le seul servi). Les jetons d'entrée factices = longueur du prompt réel de
ce tour × le rapport jetons/caractère de l'espèce dans le tour brainstorm (jetons d'entrée du journal / longueur des prompts
`essais/*.prompt.txt` du même commit). Le coût factice consigné au journal est donc l'ATTENDU d'après les coûts réels du tour
brainstorm, au barème du collisionneur (MODELES[...]["prix"]).

Usage : python3 -I -B course_a_blanc_kirchner_v1.py COLLISIONNEUR_V9 FAITS QUESTION DOSSIER_NEUF PLAFOND_USD [sans-argon]
Le dossier de sortie doit être neuf (R12) ; à mettre hors du dépôt. Sortie : un résumé sur la sortie standard."""
import importlib.util, json, math, sys
from collections import Counter
coll, faits, question, sortie, plafond = sys.argv[1:6]
sans_argon = sys.argv[6:] == ["sans-argon"]
spec = importlib.util.spec_from_file_location("collisionneur_v9", coll); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)

# Tour brainstorm (42aa6b1b) : cellule -> (jetons d'entrée, jetons de sortie, caractères de la réponse, caractères du prompt)
BRAINSTORM = {
    "E3-T1-conception-A": (132387, 15486, 16046, 270365), "E3-T1-conception-B": (132387, 39668, 19345, 270365),
    "E3-T1-conception-C": (107668, 13910, 43639, 270365), "E3-T1-conception-D": (90463, 15504, 13745, 270365),
    "E3-T1-conception-E": (92574, 4679, 16485, 270365),
    "E3-T2-critique-croisee-A": (174467, 23150, 25653, 364032), "E3-T2-critique-croisee-B": (172912, 26888, 18711, 360733),
    "E3-T2-critique-croisee-C": (126690, 12674, 39423, 336439), "E3-T2-critique-croisee-D": (122454, 19650, 12072, 366333),
    "E3-T2-critique-croisee-E": (120386, 4930, 16766, 363593),
    "E3-T3-reponse-A": (180716, 16376, 20359, 373806), "E3-T3-reponse-B": (185171, 33593, 19804, 384047),
    "E3-T3-reponse-C": (142912, 15240, 47079, 387629), "E3-T3-reponse-D": (128442, 12572, 14198, 385086),
    "E3-T3-reponse-E": (125249, 4333, 16470, 383132),
}
RAPPORT = {l: sum(v[0] for k, v in BRAINSTORM.items() if k.endswith("-" + l)) / sum(v[3] for k, v in BRAINSTORM.items() if k.endswith("-" + l))
           for l in cv.LETTRES}
FIN_OK = {"anthropic": "end_turn", "gemini": "STOP", "kimi": "stop", "openai": "stop"}
appels, lignes = [], []


def factice(fournisseur):
    def appeler(modele_id, prompt, max_tokens, *a, **k):
        lettre = next(l for l, m in cv.MODELES.items() if m["id"] == modele_id)
        tour = next(t for t in cv.TOURS if f"\n{cv.CONSIGNES[t]}\n" in prompt)
        cid = cv.id_cellule(tour, lettre)
        _, sortie_b, car_b, _ = BRAINSTORM[cid]
        prix = cv.MODELES[lettre]["prix"]
        appels.append({"cellule": cid, "lettre": lettre, "fournisseur": fournisseur, "caracteres_prompt": len(prompt),
                       "max_tokens": max_tokens,
                       "pire_cas": cv.cout_pire_cas(prix, len(prompt), cv.MODELES[lettre]["max"]),
                       "pire_cas_relance": cv.cout_pire_cas(prix, len(prompt), cv.MODELES[lettre]["max_relance"])})
        bourre = ("Texte factice de la course à blanc, aucun modèle appelé. " * (car_b // 56 + 1))[:car_b]
        usage = {"entree": round(len(prompt) * RAPPORT[lettre]), "sortie": sortie_b}
        return cv.Reponse(texte=bourre + "\n" + cv.MARQUEUR + "\n", modele_servi=modele_id, identifiant="factice",
                          fin=FIN_OK[fournisseur], usage=usage, types_blocs=["text"])
    return appeler


def jev_interdit(*a, **k):
    raise RuntimeError("Jev ne doit pas être appelé dans ce tour")


APP = {f: factice(f) for f in ("anthropic", "gemini", "kimi", "openai")}
APP["jev"] = jev_interdit
argv = ["etage3", "--sortie", sortie, "--faits", faits, "--question", question, "--plafond-usd", plafond]
if sans_argon:
    for t in cv.ORDRE_ETAGE[3]:
        argv += ["--accepter-absence", cv.id_cellule(t, "C")]
code = cv.principal(argv, appelants=APP)
probs = cv.verifier(sortie)
print(f"\n=== course à blanc {'sans Argon ' if sans_argon else ''}: code {code} ; verifier : {len(probs)} problème(s)")
for p in probs:
    print("PROBLÈME :", p)
par_tour = Counter(a["cellule"].rsplit("-", 1)[0] for a in appels)
par_espece = Counter(a["lettre"] for a in appels)
print("appels par tour :", dict(par_tour), "; par espèce :", dict(par_espece), "; total", len(appels))
journal = [json.loads(l) for l in open(f"{sortie}/journal.jsonl", encoding="utf-8")]
cout_cell = {e["cellule"]: e["cout_usd"] for e in journal if "essai" in e}
print(f"{'cellule':26s} {'prompt (car.)':>13s} {'pire cas':>9s} {'+relance':>9s} {'attendu':>8s}")
for a in appels:
    print(f"{a['cellule']:26s} {a['caracteres_prompt']:13d} {a['pire_cas']:9.2f} {a['pire_cas_relance']:9.2f} {cout_cell[a['cellule']]:8.2f}")
pire = sum(a["pire_cas"] for a in appels); pire_r = sum(a["pire_cas"] + a["pire_cas_relance"] for a in appels)
att = sum(cout_cell.values())
print(f"TOTAL : pire cas sans relance {pire:.2f} USD ; pire cas avec une relance par cellule {pire_r:.2f} USD ; attendu {att:.2f} USD")
print(f"attendu par espèce : " + ", ".join(f"{l} {sum(c for k, c in cout_cell.items() if k.endswith('-' + l)):.2f}" for l in cv.LETTRES))
print(f"plafond technique = entier supérieur à 1,2 × pire cas sans relance : {math.ceil(1.2 * pire)} USD")
print("rapports jetons/caractère (brainstorm) :", {l: round(r, 4) for l, r in RAPPORT.items()})
sys.exit(code)
