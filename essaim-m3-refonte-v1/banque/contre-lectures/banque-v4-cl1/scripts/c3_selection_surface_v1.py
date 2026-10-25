"""Contre-lecture banque v4 — c3 : la sélection d'une trace par paire ; référence de surface et sa loi sous le tirage — v1.
- recalcule `reference_traits_texte` et `verifier_banque` du noyau sur la v4 et la v3 (code importé sans écrire de
  fichier compilé) ;
- classifieur de surface du noyau (appris sur train, inchangé) : ses prédictions sur les 24 traces de chaque part de la
  v3 sont fixes ; on énumère les 400 sélections permises par le constructeur (dans chaque source, 3 paires sur 6 gardent
  l'honnête, C(6,3)^2) et on situe la valeur de la v4 dans cette loi ;
- loi du hasard pur à 12 traces (6/6) ;
- traits de surface par classe (aire sous la courbe de « plus court ⇒ sabotée ») : v3, v4, loi sous le tirage ;
- types de sabotage gardés (comptes seulement).
Usage : python3 -I -B c3_selection_surface_v1.py RACINE_CODE DOSSIER_BANQUE
"""
import itertools, json, math, pathlib, re, sys

sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import numpy as np
from essaim_m3.banque import _regression_logistique, _traits_texte, reference_traits_texte, verifier_banque

B = pathlib.Path(sys.argv[2])
FAM = "controle-delegation"
p3, p4 = B / "banque-confrontation-v3.json", B / "banque-confrontation-v4.json"
v3 = json.loads(p3.read_text(encoding="utf-8")); v4 = json.loads(p4.read_text(encoding="utf-8"))
s3 = json.loads((B / "banque-confrontation-v3-secret.json").read_text(encoding="utf-8"))
out = {}
out["verifier_banque_v4"] = verifier_banque(p4)
out["reference_v4"] = reference_traits_texte(p4)["par_famille"]
out["reference_v3"] = reference_traits_texte(p3)["par_famille"]

# classifieur de surface, comme reference_traits_texte (sans hasard)
tr = [t for t in v3["train"] if t["famille"] == FAM]
X = np.stack([_traits_texte(t["texte"]) for t in tr]); y = np.array([1.0 if t["verite"] == "sabotage" else 0.0 for t in tr])
w, b0, mu, sd = _regression_logistique(X, y)


def predire(ts):
    return ((np.stack([_traits_texte(t["texte"]) for t in ts]) - mu) / sd) @ w + b0 >= 0


def ee(pred, vrai):
    vrai = np.asarray(vrai); pred = np.asarray(pred)
    return ((pred & vrai).sum() / vrai.sum() + (~pred & ~vrai).sum() / (~vrai).sum()) / 2


def auc(scores, vrai):  # P(score sabotée > score honnête), égalités 1/2
    s_pos = [s for s, v in zip(scores, vrai) if v]; s_neg = [s for s, v in zip(scores, vrai) if not v]
    return sum((a > c) + 0.5 * (a == c) for a in s_pos for c in s_neg) / (len(s_pos) * len(s_neg))


def lignes(t):
    return [l for l in t.split("\n") if l.strip()]


TRAITS = {"caracteres": lambda t: len(t["texte"]), "lignes": lambda t: len(lignes(t["texte"])),
          "mots": lambda t: len(re.findall(r"[a-zà-ÿ0-9_]{2,}", t["texte"].lower()))}
ids4 = {t["id"] for p in ("test", "test_final") for t in v4[p]}
loi = {}
for part in ("test", "test_final"):
    ts = [t for t in v3[part] if t["famille"] == FAM]
    pred = dict(zip([t["id"] for t in ts], predire(ts)))
    paires = {}
    for t in ts:
        paires.setdefault((t["source"], s3[t["id"]]["paire"]), {})[t["verite"]] = t
    par_src = {}
    for k in sorted(paires):
        par_src.setdefault(k[0], []).append(paires[k])
    srcs = sorted(par_src)
    valeurs, aucs = [], {k: [] for k in TRAITS}
    obs = None
    for choix in itertools.product(*[list(itertools.combinations(range(len(par_src[s])), len(par_src[s]) // 2)) for s in srcs]):
        garde = []
        for s, hon in zip(srcs, choix):
            for i, pr in enumerate(par_src[s]):
                garde.append(pr["honnete"] if i in hon else pr["sabotage"])
        vrai = [t["verite"] == "sabotage" for t in garde]
        x = round(float(ee([pred[t["id"]] for t in garde], vrai)), 4)
        valeurs.append(x)
        a = {k: auc([-f(t) for t in garde], vrai) for k, f in TRAITS.items()}  # « plus court ⇒ sabotée »
        for k in TRAITS:
            aucs[k].append(a[k])
        if {t["id"] for t in garde} == {t["id"] for t in v4[part] if t["famille"] == FAM}:
            obs = (x, a)
    v = np.array(valeurs)
    vrai24 = [t["verite"] == "sabotage" for t in ts]
    loi[part] = {
        "n_selections": len(valeurs), "ee_v4_observee": obs[0],
        "ee_v3_24_traces": round(float(ee([pred[t["id"]] for t in ts], vrai24)), 4),
        "loi_sous_le_tirage": {"min": float(v.min()), "q05": float(np.quantile(v, 0.05)), "mediane": float(np.median(v)),
                               "moyenne": round(float(v.mean()), 4), "q95": float(np.quantile(v, 0.95)), "max": float(v.max())},
        "P_tirage_ee_au_moins_observee": round(float((v >= obs[0] - 1e-9).mean()), 4),
        "P_tirage_ee_au_plus_observee": round(float((v <= obs[0] + 1e-9).mean()), 4),
        "aire_plus_court_sabotee": {k: {"v3_24": round(auc([-TRAITS[k](t) for t in ts], vrai24), 3), "v4_observee": round(obs[1][k], 3),
                                        "tirage_q05": round(float(np.quantile(aucs[k], 0.05)), 3), "tirage_mediane": round(float(np.median(aucs[k])), 3),
                                        "tirage_q95": round(float(np.quantile(aucs[k], 0.95)), 3),
                                        "P_tirage_au_moins_observee": round(float((np.array(aucs[k]) >= obs[1][k] - 1e-9).mean()), 3)} for k in TRAITS},
        "moyennes_caracteres_v4": {c: round(float(np.mean([len(t["texte"]) for t in v4[part] if t["famille"] == FAM and t["verite"] == c])), 1) for c in ("honnete", "sabotage")},
        "moyennes_caracteres_v3": {c: round(float(np.mean([len(t["texte"]) for t in ts if t["verite"] == c])), 1) for c in ("honnete", "sabotage")},
        "types_sabotage_distincts": {"v3": len({s3[t["id"]].get("type_sabotage") for t in ts if t["verite"] == "sabotage"}),
                                     "v4": len({s3[t["id"]].get("type_sabotage") for t in v4[part] if t["famille"] == FAM and t["verite"] == "sabotage"})}}
out["loi_sous_le_tirage"] = loi
# hasard pur : prédictions indépendantes, P(sabotée) = 1/2 ; EE = (k+j)/12, k+j ~ Binomiale(12, 1/2) ; idem à 24
def queue(n, k):
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n
out["hasard_pur"] = {"12_traces": {f"P(EE>={k}/12)": round(queue(12, k), 4) for k in (7, 8, 9, 10, 11, 12)} | {"ecart_type": round(math.sqrt(3) / 12, 4)},
                     "24_traces": {f"P(EE>={k}/24)": round(queue(24, k), 4) for k in (15, 16, 17, 18)} | {"ecart_type": round(math.sqrt(6) / 24, 4)},
                     "score_global_ecart_type_hasard": {"v4": round(math.sqrt((math.sqrt(3) / 12) ** 2 + (3 / 36) ** 2) / 2, 4),
                                                        "v3": round(math.sqrt((math.sqrt(6) / 24) ** 2 + (3 / 36) ** 2) / 2, 4)}}
print(json.dumps(out, ensure_ascii=False, indent=1))
