"""Identité de la v8 avec les sorties de la contre-lecture GD7 (partie `combine` et partie `A_seul` du rejeu `rejeu-contre-lecture-gd7-v2.py`).

Pour chacun des 25 résultats de `combine-sortie.json` (17) et `A-seul-sortie.json` (8), la loi est reconstruite avec la **classe de la v8**
(`rho_b` direct à la place de la sous-classe `LoiRho` du rejeu GD7), la cellule est tirée par `cellule` de la v8 avec la même graine (20261029), la même
étiquette (`contre-lecture-gd7|<loi>|Kh|Ks|biais|n=288`), 2 000 répétitions, 288 unités, k = 8, τ = 0,01, δ = 0,05, seuils 160 et 40, lecture (A) m = 2, et
les 13 nombres lus par le rejeu GD7 sont comparés aux siens, **exactement** (flottants identiques). Deuxième contrôle : ρ direct = ρ déduit de σ
(`parametres_beta_comparateurs`), cellule entière identique à même étiquette. Témoin négatif (R5) : une cellule à ρ_B différent de 10⁻³ donne des champs différents.
Lecture seule des fichiers GD7 ; aucune commande git (la v8 n'en a aucune) ; processeur seul.

Usage : python3 -I -B verif-identite-gd7-v8.py SCRIPT_V8 DOSSIER_GD7 SORTIE.json
"""
import hashlib
import importlib.util
import json
import sys
import time

CHEMIN_V8, DOSSIER_GD7, SORTIE = sys.argv[1:4]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("lancer avec -B")
spec = importlib.util.spec_from_file_location("v8", CHEMIN_V8)
v8 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v8)
GRAINE = 20261029
EBH = {"lectures": ["A"], "M": 2, "N": 0, "alpha": 0.05}
CLES_CELLULE = ("g40", "g160", "1g40", "1g160", "c40", "c160", "fiche40", "front", "tricheur")
CLES_MOMENTS = ("E_fB", "E_rB", "ecart_type_pB_honnetes", "ecart_type_pB_sabotes")


def lire(c):
    return {"g40": c["40.0"]["k_gardes"]["part"], "g160": c["160.0"]["k_gardes"]["part"], "1g40": c["40.0"]["garde_seule"]["part"],
            "1g160": c["160.0"]["garde_seule"]["part"], "c40": c["40.0"]["k_contrastes"]["part"], "c160": c["160.0"]["k_contrastes"]["part"],
            "fiche40": c["ebh_A"]["retenues_fiches_du_sujet"], "front": c["40.0"]["frontiere_part"], "tricheur": c["40.0"]["tricheur_part"]}


def loi_de(etiquette, K, Ks):
    L = v8.LoiSynthetique
    if etiquette.startswith("A-beta") and "+B-beta" in etiquette:
        rho = float(etiquette.split("A-beta")[1].split("+")[0])
        return L(K, Ks, 0.01, 0.4, 0.1, True, 0.0, True, rho, 0.0, 0.0, "beta", rho_b=rho)
    if etiquette == "A-logit1.0+B-beta(sigma1.0)":
        return L(K, Ks, 0.01, 0.4, 0.1, True, 1.0, True, 0.0, 1.0, 0.0, "beta")
    if etiquette == "A-beta0.17-seul" or (etiquette.startswith("A-beta") and etiquette.endswith("-seul")):
        rho = float(etiquette.split("A-beta")[1].split("-seul")[0])
        return L(K, Ks, 0.01, 0.4, 0.1, True, 0.0, True, rho, 0.0, 0.0, "logit")
    raise SystemExit("étiquette inconnue " + etiquette)


def passer(loi, etiquette_loi, K, Ks, biais):
    et = f"contre-lecture-gd7|{etiquette_loi}|Kh{K}|Ks{Ks}|biais={biais}|n=288"
    ebh = dict(EBH) | {"nulle_A": loi.variante_nulle(True), "nulle_B": loi.variante_nulle(False)}
    return v8.cellule(loi, loi, 2000, 288, 288, 0.05, [160.0, 40.0], 8, biais, GRAINE, et, True, ebh)


sortie = {"script_v8": CHEMIN_V8, "script_v8_sha256": hashlib.sha256(open(CHEMIN_V8, "rb").read()).hexdigest(), "numpy": v8.np.__version__,
          "graine": GRAINE, "fichiers_gd7": {}, "comparaisons": []}
t0 = time.time()
for nom in ("combine-sortie.json", "A-seul-sortie.json"):
    chemin = DOSSIER_GD7.rstrip("/") + "/" + nom
    brut = open(chemin, "rb").read()
    sortie["fichiers_gd7"][nom] = hashlib.sha256(brut).hexdigest()
    d = json.loads(brut)
    assert d["graine"] == GRAINE and d["numpy"] == v8.np.__version__, ("graine ou version de numpy différente", d["graine"], d["numpy"])
    for r in d["resultats"]:
        loi = loi_de(r["loi"], r["K_h"], r["K_s"])
        c = passer(loi, r["loi"], r["K_h"], r["K_s"], r["biais"])
        mon = lire(c)
        diff = [k for k in CLES_CELLULE if mon[k] != r[k]]
        m = c.get("moments_tires", {})
        diff += ["moments." + k for k in CLES_MOMENTS if k in r["moments"] and m.get(k) != r["moments"][k]]
        diff += ["moments.cle_absente:" + k for k in r["moments"] if k not in CLES_MOMENTS and k not in m]
        n_comparees = len(CLES_CELLULE) + len([k for k in r["moments"]])
        sortie["comparaisons"].append({"fichier": nom, "loi": r["loi"], "K_h": r["K_h"], "K_s": r["K_s"], "biais": r["biais"],
                                       "nom_v8": loi.nom(), "champs_compares": n_comparees, "champs_differents": diff})
        print(sortie["comparaisons"][-1], flush=True)

# 2. ρ direct = ρ déduit de σ : cellule entière identique à même étiquette
egalite = []
for sigma in (0.5, 1.0):
    ref = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, sigma, 0.0, "beta")
    rho, kappa = ref.parametres_beta_comparateurs()
    direct = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, 0.0, 0.0, "beta", rho_b=float(repr(rho)))
    assert direct.parametres_beta_comparateurs() == (rho, kappa)
    a = json.dumps(passer(ref, f"egalite-rho-sigma{sigma}", 5, 10, 0.0125), sort_keys=True)
    b = json.dumps(passer(direct, f"egalite-rho-sigma{sigma}", 5, 10, 0.0125), sort_keys=True)
    egalite.append({"sigma": sigma, "rho": rho, "kappa": kappa, "cellules_identiques": a == b, "octets": len(a)})
    print(egalite[-1], flush=True)
sortie["rho_direct_egal_rho_deduit_de_sigma"] = egalite

# 3. témoin négatif : ρ_B décalé de 1e-3 -> cellule différente
ref = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, 1.0, 0.0, "beta")
rho, _ = ref.parametres_beta_comparateurs()
decale = v8.LoiSynthetique(5, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, 0.0, 0.0, "beta", rho_b=rho + 1e-3)
a = passer(ref, "temoin-negatif", 5, 10, 0.0125)
b = passer(decale, "temoin-negatif", 5, 10, 0.0125)
champs = [k for k in ("moments_tires",) if json.dumps(a[k], sort_keys=True) != json.dumps(b[k], sort_keys=True)]
sortie["temoin_negatif"] = {"rho": rho, "rho_decale": rho + 1e-3, "cellules_differentes": json.dumps(a, sort_keys=True) != json.dumps(b, sort_keys=True),
                            "moments_differents": bool(champs)}
print(sortie["temoin_negatif"], flush=True)

sortie["resultats_compares"] = len(sortie["comparaisons"])
sortie["champs_compares_total"] = sum(c["champs_compares"] for c in sortie["comparaisons"])
sortie["champs_differents_total"] = sum(len(c["champs_differents"]) for c in sortie["comparaisons"])
sortie["conforme"] = (sortie["champs_differents_total"] == 0 and all(e["cellules_identiques"] for e in egalite)
                      and sortie["temoin_negatif"]["cellules_differentes"] and sortie["resultats_compares"] == 25)
sortie["duree_s"] = round(time.time() - t0, 1)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(sortie, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("conforme" if sortie["conforme"] else "NON CONFORME", sortie["resultats_compares"], "résultats,", sortie["champs_compares_total"], "champs,",
      sortie["champs_differents_total"], "différents")
