"""Contre-lecture banque v4 — c2 : reste-t-il un contraste possible ? Ressemblances entre traces servies — v1.
Ressemblance R (celle de `reference_contraste_paires_v2.py`) : difflib.SequenceMatcher sur les listes de lignes
nettoyées, autojunk=False. Ressemblance J : indice de Jaccard des ensembles de mots `[a-zà-ÿ0-9_]{2,}`.
Ressemblance S : Jaccard des mots de la seule ligne de scénario (première ligne). Toutes les traces de délégation
servies par la v4 (train 32, test 12, test final 12 — l'organisme voit test et test final mêlés) ; pour comparaison,
les jumelles retirées (lues dans la v3) et la ressemblance dans une paire de la v3. Lit le secret v3 pour les paires.
Usage : python3 -I -B c2_ressemblance_v1.py DOSSIER_BANQUE
"""
import difflib, itertools, json, pathlib, re, sys

B = pathlib.Path(sys.argv[1])
FAM = "controle-delegation"
v3 = json.loads((B / "banque-confrontation-v3.json").read_text(encoding="utf-8"))
s3 = json.loads((B / "banque-confrontation-v3-secret.json").read_text(encoding="utf-8"))
v4 = json.loads((B / "banque-confrontation-v4.json").read_text(encoding="utf-8"))


def lignes(t):
    return [l.strip() for l in t.split("\n") if l.strip()]


def mots(s):
    return re.findall(r"[a-zà-ÿ0-9_]{2,}", s.lower())


servies = [(p, t) for p in ("train", "test", "test_final") for t in v4[p] if t["famille"] == FAM]
ids4 = {t["id"] for _, t in servies}
retirees = [(p, t) for p in ("test", "test_final") for t in v3[p] if t["famille"] == FAM and t["id"] not in ids4]
tout = servies + retirees
L = {t["id"]: lignes(t["texte"]) for _, t in tout}
W = {t["id"]: set(mots(t["texte"])) for _, t in tout}
S = {t["id"]: set(mots(lignes(t["texte"])[0])) for _, t in tout}
part = {t["id"]: p for p, t in servies}
part_ret = {t["id"]: p for p, t in retirees}
cle_paire = {t["id"]: (t["source"], s3[t["id"]]["paire"]) for _, t in tout}


def R(a, c):
    return difflib.SequenceMatcher(None, L[a], L[c], autojunk=False).ratio()


def J(a, c):
    return len(W[a] & W[c]) / max(1, len(W[a] | W[c]))


def Js(a, c):
    return len(S[a] & S[c]) / max(1, len(S[a] | S[c]))


out = {"n_servies": len(servies), "n_retirees": len(retirees)}
# a) dans une paire de la v3 (servie + jumelle retirée ; train : les deux membres)
intra = {"R": [], "J": [], "S": []}
par_paire = {}
for _, t in tout:
    par_paire.setdefault(cle_paire[t["id"]], []).append(t["id"])
for k, m in par_paire.items():
    if len(m) == 2:
        intra["R"].append(R(*m)); intra["J"].append(J(*m)); intra["S"].append(Js(*m))
out["dans_une_paire_v3"] = {k: {"min": round(min(v), 3), "mediane": round(sorted(v)[len(v) // 2], 3)} for k, v in intra.items()}
# b) entre traces servies de paires différentes, par couple de parts
blocs = {}
pire = {"R": (0, None), "J": (0, None), "S": (0, None)}
for (pa, a), (pc, c) in itertools.combinations(servies, 2):
    if cle_paire[a["id"]] == cle_paire[c["id"]]:
        continue  # paires d'entraînement : membres servis ensemble, avec leur vérité
    cle = "|".join(sorted((pa, pc)))
    r, j, s = R(a["id"], c["id"]), J(a["id"], c["id"]), Js(a["id"], c["id"])
    b = blocs.setdefault(cle, {"R": 0.0, "J": 0.0, "S": 0.0, "n": 0})
    b["R"] = max(b["R"], r); b["J"] = max(b["J"], j); b["S"] = max(b["S"], s); b["n"] += 1
    for nom, x in (("R", r), ("J", j), ("S", s)):
        if x > pire[nom][0]:
            pire[nom] = (x, cle)
out["hors_paire_max_par_couple_de_parts"] = {k: {m: round(v[m], 3) for m in ("R", "J", "S")} | {"n_couples": v["n"]} for k, v in sorted(blocs.items())}
out["hors_paire_max_global"] = {k: {"valeur": round(v[0], 3), "couple_de_parts": v[1]} for k, v in pire.items()}
# c) pour chaque trace de test / test final : plus proche voisine servie, comparée à sa jumelle retirée
voisines = []
for p, t in servies:
    if p == "train":
        continue
    autres = [c for _, c in servies if c["id"] != t["id"]]
    meilleur = max(autres, key=lambda c: R(t["id"], c["id"]))
    jum = next(x for x in par_paire[cle_paire[t["id"]]] if x != t["id"])
    voisines.append({"part": p, "R_voisine_servie": round(R(t["id"], meilleur["id"]), 3), "part_voisine": part[meilleur["id"]],
                     "J_max_servie": round(max(J(t["id"], c["id"]) for c in autres), 3),
                     "R_jumelle_retiree": round(R(t["id"], jum), 3), "J_jumelle_retiree": round(J(t["id"], jum), 3)})
out["test_et_final_plus_proche_voisine"] = {
    "R_voisine_servie_max": max(v["R_voisine_servie"] for v in voisines),
    "J_max_servie_max": max(v["J_max_servie"] for v in voisines),
    "R_jumelle_retiree_min": min(v["R_jumelle_retiree"] for v in voisines),
    "J_jumelle_retiree_min": min(v["J_jumelle_retiree"] for v in voisines),
    "parts_des_voisines": {k: sum(v["part_voisine"] == k for v in voisines) for k in ("train", "test", "test_final")},
    "toutes_jumelles_au_dessus_de_toute_voisine_R": min(v["R_jumelle_retiree"] for v in voisines) > max(v["R_voisine_servie"] for v in voisines)}
# d) appariement mutuel (règle de la référence de contraste) sur les 24 traces de test + test final mêlées
ts = [t for p, t in servies if p != "train"]
n = len(ts)
mat = [[(R(ts[a]["id"], ts[c]["id"]) if a != c else -1.0) for c in range(n)] for a in range(n)]
vois = [max(range(n), key=lambda c: mat[a][c]) for a in range(n)]
mutuelles = [(a, vois[a]) for a in range(n) if vois[vois[a]] == a and a < vois[a]]
out["appariement_mutuel_test_plus_final"] = {
    "n_traces": n, "n_paires_mutuelles": len(mutuelles),
    "ressemblances": sorted(round(mat[a][c], 3) for a, c in mutuelles),
    "classes_opposees": sum(ts[a]["verite"] != ts[c]["verite"] for a, c in mutuelles),
    "regle_plus_courte_sabotee_sur_paires_mutuelles_classes_opposees": (
        lambda pr: (sum((min(pr_, key=lambda x: len(x["texte"]))["verite"] == "sabotage") for pr_ in pr), len(pr)))(
        [(ts[a], ts[c]) for a, c in mutuelles if ts[a]["verite"] != ts[c]["verite"]])}
# e) même mesure sur la v3 (rappel) : ressemblance max hors paire dans test, test final, et entre parts
s3_serv = [(p, t) for p in ("train", "test", "test_final") for t in v3[p] if t["famille"] == FAM]
for _, t in s3_serv:
    L.setdefault(t["id"], lignes(t["texte"]))
mx = 0.0
for (pa, a), (pc, c) in itertools.combinations(s3_serv, 2):
    if cle_paire.get(a["id"]) != cle_paire.get(c["id"]):
        mx = max(mx, R(a["id"], c["id"]))
out["v3_hors_paire_max_R_toutes_parts"] = round(mx, 3)
print(json.dumps(out, ensure_ascii=False, indent=1))
