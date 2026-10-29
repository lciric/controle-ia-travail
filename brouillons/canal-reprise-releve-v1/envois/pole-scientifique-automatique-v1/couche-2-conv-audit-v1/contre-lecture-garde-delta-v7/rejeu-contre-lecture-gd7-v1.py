"""Rejeu de contre-lecture (sous-agent neuf Sonnet) de la simulation de puissance de la garde delta v7. Lecture seule des scripts v6 et v7
(chargés par importlib, aucune commande git : etat_git neutralisé), écriture dans ce dossier seulement, processeur seul.
Usage : python3 -I -B rejeu-contre-lecture-gd7-v1.py PARTIE SORTIE.json    PARTIE : identite | kappa_fB | stress_garde | combine
"""
import contextlib, importlib.util, io, json, math, sys, time
import numpy as np

PARTIE, SORTIE = sys.argv[1], sys.argv[2]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("lancer avec -B")
D = "/home/claude/controle-ia-travail/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/couche-2-conv-audit-v1/"
P7 = D + "simulation-puissance-garde-delta-v7/simulation-puissance-garde-delta-v7.py"
P6 = D + "simulation-puissance-garde-delta-v6/simulation-puissance-garde-delta-v6.py"

def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

v7 = charger("v7", P7)
GRAINE = 20261029
EBH = {"lectures": ["A"], "M": 2, "N": 0, "alpha": 0.05}

class LoiKf(v7.LoiSynthetique):
    """Appariement alternatif : kappa fixée sur f_B (même sigma logit de reference, variance de f_B egale a la variance logit de f_B)."""
    def parametres_beta_comparateurs(self):
        var_logit = v7.moments_logit(self.taux, self.effet_b)[1]
        rho = var_logit / (self.taux * (1 - self.taux))
        return rho, (1 - rho) / rho

class LoiRho(v7.LoiSynthetique):
    """Correlation intra-unite imposee rho (meme kappa des deux cotes), pour pousser la dispersion au-dela de la v7."""
    rho_impose = 0.17
    def parametres_beta_comparateurs(self):
        return self.rho_impose, (1 - self.rho_impose) / self.rho_impose

def lire(c):
    return {"g40": c["40.0"]["k_gardes"]["part"], "g160": c["160.0"]["k_gardes"]["part"], "1g40": c["40.0"]["garde_seule"]["part"],
            "1g160": c["160.0"]["garde_seule"]["part"], "c40": c["40.0"]["k_contrastes"]["part"], "c160": c["160.0"]["k_contrastes"]["part"],
            "fiche40": c["ebh_A"]["retenues_fiches_du_sujet"], "front": c["40.0"]["frontiere_part"], "tricheur": c["40.0"]["tricheur_part"]}

def passer(etiquette_loi, loi, K, Ks, biais, reps=2000, n=288):
    et = f"contre-lecture-gd7|{etiquette_loi}|Kh{K}|Ks{Ks}|biais={biais}|n={n}"
    t0 = time.time()
    ebh = dict(EBH) | {"nulle_A": loi.variante_nulle(True), "nulle_B": loi.variante_nulle(False)}
    c = v7.cellule(loi, loi, reps, n, n, 0.05, [160.0, 40.0], 8, biais, GRAINE, et, True, ebh)
    r = lire(c) | {"loi": etiquette_loi, "K_h": K, "K_s": Ks, "biais": biais, "duree_s": round(time.time() - t0, 1)}
    if "moments_tires" in c:
        m = c["moments_tires"]
        r["moments"] = {k: m[k] for k in ("E_fB", "E_rB", "ecart_type_pB_honnetes", "ecart_type_pB_sabotes") if k in m}
    print(r, flush=True); return r

sortie = {"partie": PARTIE, "script_v7_sha256": v7.hashlib.sha256(open(P7, "rb").read()).hexdigest(), "numpy": np.__version__, "graine": GRAINE, "resultats": []}
R = sortie["resultats"]

if PARTIE == "identite":
    # identité de bout en bout (analyse des options comprise) : v7 --K-s (produit cartésien) contre v6 --K-sabotes (apparié), cellule par cellule
    v6 = charger("v6", P6)
    neutre = lambda chemin: {"commit": None, "etat_du_script": "git neutralisé (contre-lecture)"}
    v6.etat_git = neutre; v7.etat_git = neutre
    def lancer(mod, argv):
        old = sys.argv; sys.argv = ["x"] + argv
        tampon = io.StringIO()
        try:
            with contextlib.redirect_stdout(tampon):
                mod.principal()
        finally:
            sys.argv = old
        return json.loads(tampon.getvalue())
    base = ["--repetitions", "300", "--comparateurs", "8", "--taux", "0.01", "--deltas", "0.05", "--biais", "0,0.0125", "--tailles", "288",
            "--lecture-ebh", "A", "--m", "8,2", "--sans-n80"]
    for extra in ([], ["--effet-unite-comparateurs", "1.0"]):
        s7 = lancer(v7, base + ["--K", "10,5", "--K-s", "10,5,3"] + extra)
        n_diff = n_comm = 0; cellules_cmp = 0
        for K, Ks in ((10, 10), (10, 5), (10, 3), (5, 10), (5, 5), (5, 3)):
            s6 = lancer(v6, base + ["--K", str(K), "--K-sabotes", str(Ks)] + extra)
            for et, c6 in s6["cellules"].items():
                c7 = s7["cellules"].get(et)
                assert c7 is not None, ("cellule v6 absente de v7", et)
                cellules_cmp += 1
                a, b = json.dumps(c6, sort_keys=True), json.dumps(c7, sort_keys=True)
                n_comm += 1; n_diff += (a != b)
        R.append({"extra": extra, "cellules_v7": len(s7["cellules"]), "cellules_comparees": cellules_cmp, "cellules_differentes": n_diff})
        print(R[-1], flush=True)
    # temoin negatif : K-s different -> cellules differentes
    s7b = lancer(v7, base + ["--K", "10", "--K-s", "5"]); s7c = lancer(v7, base + ["--K", "10", "--K-s", "3"])
    R.append({"temoin_negatif_cles_communes": len(set(s7b["cellules"]) & set(s7c["cellules"]))})

elif PARTIE == "kappa_fB":
    for sig in (1.0, 0.5):
        loi_ref = LoiKf(10, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, sig, 0.0, "beta")
        rho, kap = loi_ref.parametres_beta_comparateurs()
        rep = {"sigma": sig, "rho_fB": rho, "kappa": kap, "sd_fB": math.sqrt(rho * 0.01 * 0.99), "sd_rB": math.sqrt(rho * 0.4 * 0.6)}
        print(rep, flush=True); R.append(rep)
        for K, Ks in ((10, 10), (10, 5), (5, 10), (5, 5), (5, 3)):
            for b in (0.0, 0.0125):
                loi = LoiKf(K, Ks, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, sig, 0.0, "beta")
                R.append(passer(f"kappaFB-sigma{sig}", loi, K, Ks, b))

elif PARTIE == "stress_garde":
    for rho in (0.35, 0.6):
        for K in (10, 5):
            for b in (0.0, 0.0125):
                loi = LoiRho(K, 10, 0.01, 0.4, 0.1, True, 0.0, True, 0.0, 1.0, 0.0, "beta"); loi.rho_impose = rho
                R.append(passer(f"rho{rho}-B", loi, K, 10, b))

elif PARTIE == "combine":
    for rho_a in (0.054, 0.17):
        paires = ((10, 10), (5, 10)) if rho_a < 0.1 else ((10, 10), (5, 10), (10, 5), (5, 5))
        for K, Ks in paires:
            for b in (0.0, 0.0125):
                loi = LoiRho(K, Ks, 0.01, 0.4, 0.1, True, 0.0, True, rho_a, 1.0, 0.0, "beta"); loi.rho_impose = rho_a
                R.append(passer(f"A-beta{rho_a}+B-beta{rho_a}", loi, K, Ks, b))
    for K, Ks in ((5, 10), (5, 5)):
        for b in (0.0, 0.0125):
            loi = v7.LoiSynthetique(K, Ks, 0.01, 0.4, 0.1, True, 1.0, True, 0.0, 1.0, 0.0, "beta")
            R.append(passer("A-logit1.0+B-beta(sigma1.0)", loi, K, Ks, b))
    # témoin : A beta seul (v5 style), sans B, pour isoler l'effet de A
    for K, Ks in ((5, 10),):
        for b in (0.0125,):
            loi = v7.LoiSynthetique(K, Ks, 0.01, 0.4, 0.1, True, 0.0, True, 0.17, 0.0, 0.0, "logit")
            R.append(passer("A-beta0.17-seul", loi, K, Ks, b))

with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(sortie, f, indent=1, ensure_ascii=False); f.write("\n")
print("fini", PARTIE)
