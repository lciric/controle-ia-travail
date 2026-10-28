"""Contre-vérification sur processeur de la conception v7 du pari apparié borné et du code v7 (version 24).
Contre-lecteur neuf (R2), Fable 5.1. Aucun fichier du dépôt n'est modifié (import sans bytecode).
Graines : numpy.random.SeedSequence(2026102722, spawn_key=(section, indice)) → entier 64 bits → random.Random (R9).
Lancement : /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v7.py > ...-sortie.json
"""
import copy
import json
import math
import os
import random
import sys
import time
import unittest

sys.dont_write_bytecode = True
BASE = ("/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/"
        "orchestrateur-pole-v7")
sys.path.insert(0, BASE)
import numpy as np  # noqa: E402
from pole import pari_apparie as pa  # noqa: E402
from pole import monde_banque_scores as mbs  # noqa: E402
from pole import engagement_apparie as ea  # noqa: E402

REP = int(os.environ.get("REP", "2000"))
debut = time.time()
S = {"manifeste": {"python": sys.version.split()[0], "numpy": np.__version__, "graine_maitresse": 2026102722, "REP": REP,
                   "base": BASE}}


def rng(section, indice=0):
    ss = np.random.SeedSequence(2026102722, spawn_key=(section, indice))
    return random.Random(int(ss.generate_state(1, dtype=np.uint64)[0]))


def marche_a_prime(r, pas):
    lw, traj = 0.0, []
    for _ in range(pas):
        lw += math.log(1.5) if r.random() < 0.5 else math.log(0.5)
        traj.append(lw)
    return traj


# ---------------------------------------------------------------- U : les essais du dépôt, tels quels
os.chdir(BASE)
sys.path.insert(0, BASE)
suite = unittest.TestSuite()
charge = unittest.TestLoader()
for nom in ("essais.test_v7_pari_apparie", "essais.test_v7_monde_banque_scores", "essais.test_v7_engagement_apparie"):
    suite.addTests(charge.loadTestsFromName(nom))
res = unittest.TextTestRunner(stream=open(os.devnull, "w"), verbosity=0).run(suite)
S["U_essais_du_depot"] = {"lances": res.testsRun, "echecs": len(res.failures), "erreurs": len(res.errors)}
# nombre total de « def test_ » dans essais/ (le « 259 » de la v7)
total = 0
for f in sorted(os.listdir(os.path.join(BASE, "essais"))):
    if f.startswith("test_") and f.endswith(".py"):
        with open(os.path.join(BASE, "essais", f), encoding="utf-8") as fh:
            total += sum(l.lstrip().startswith("def test_") for l in fh)
S["U_essais_du_depot"]["def_test_dans_essais"] = total

# ---------------------------------------------------------------- A : contrat d'abandon, cas sains et artefacts
A = {}
c = pa.Course(alpha=0.05)
c.entrer("g1", ["a", "b", "c"], 0.03)
c.abandonner("a", avant_partie=True)
# (1) abandonner(fiche gelée, trajectoire) : la partie est-elle refusée ou ignorée en silence ?
try:
    c.abandonner("a", trajectoire_log=[math.log(50)])
    A["abandonner_gelee_avec_partie"] = {"erreur": False, "log_e_apres": c.log_e["a"],
                                         "lecture": "partie IGNORÉE EN SILENCE (retour avant ajouter_trajectoire)"}
except ValueError as e:
    A["abandonner_gelee_avec_partie"] = {"erreur": True, "message": str(e)}
# (2) abandon « avant partie » déclaré alors que la partie de la génération a déjà été ajoutée : accepté ?
c.ajouter_trajectoire("b", [math.log(2)])
try:
    c.abandonner("b", avant_partie=True)
    A["avant_partie_declare_apres_la_partie"] = {"erreur": False, "gelee_a": c.log_e["b"], "lecture": "drapeau contradictoire accepté (sans effet : gel après la partie)"}
except ValueError as e:
    A["avant_partie_declare_apres_la_partie"] = {"erreur": True, "message": str(e)}
# (3) chemin « lire puis abandonner » : partie de g calculée mais jamais ajoutée ; lire ; abandonner(avant_partie=True)
c2 = pa.Course(alpha=0.05)
c2.entrer("g1", ["x"], 0.05)
_ = marche_a_prime(rng(1, 0), 20)  # la partie de la génération 1 est « observée » mais jamais ajoutée
c2.lire()
try:
    c2.abandonner("x", avant_partie=True)
    A["partie_sautee_puis_lire_puis_abandon"] = {"erreur": False, "log_e_gele": c2.log_e["x"],
                                                 "lecture": "aucune erreur : la partie sautée est invisible au code"}
except ValueError as e:
    A["partie_sautee_puis_lire_puis_abandon"] = {"erreur": True, "message": str(e)}
# (4) lire() exige-t-elle une partie pour chaque fiche active ?
c3 = pa.Course(alpha=0.05)
c3.entrer("g1", ["x", "y"], 0.05)
c3.ajouter_trajectoire("x", [0.0])
A["lire_sans_partie_pour_y"] = {"erreur": False, "promues": sorted(c3.lire())}
# (5) trace de l'abandon : la course garde-t-elle la génération et le mode (avant/après partie) ?
A["trace_abandon_disponible"] = {"attributs_course": sorted(k for k in vars(c) if not k.startswith("_")),
                                 "gelees_est_un_ensemble_sans_motif": isinstance(c.gelees, set)}
S["A_contrat_abandon"] = A

# ---------------------------------------------------------------- B : l'artefact « partie sautée » (jumeau de K6-2), mesuré
# Politique : à chaque génération, la partie (A′, 20 pas) est calculée ; si sa valeur finale ≥ 1 elle est ajoutée,
# sinon elle est sautée (jamais ajoutée) ; lire() ; la fiche n'est jamais abandonnée. Nul complet.
B = {}
for pas, generations in ((20, 10), (20, 30)):
    r = rng(2, pas * 100 + generations)
    au_moins_une, somme_e = 0, 0.0
    m = 4
    for _ in range(REP):
        c = pa.Course(alpha=0.05)
        c.entrer("g1", [f"f{i}" for i in range(m)], 0.05)
        for g in range(generations):
            for i in range(m):
                traj = marche_a_prime(r, pas)
                if traj[-1] >= 0.0:
                    if f"f{i}" not in c.gelees:
                        c.ajouter_trajectoire(f"f{i}", traj)
            c.lire()
        au_moins_une += bool(c.promues)
        somme_e += sum(math.exp(c.log_e[f]) for f in c.budgets) / m
    B[f"A_prime_{pas}_pas_{generations}_generations"] = {"repetitions": REP, "alpha": 0.05, "m": m,
        "P(au_moins_une_fausse_promotion)": au_moins_une / REP, "E[e-valeur_finale]_par_fiche": somme_e / REP,
        "erreurs_levees": 0}
# contrôle sain : toutes les parties ajoutées (même monde, même politique de lecture)
r = rng(2, 999)
au_moins_une = 0
for _ in range(REP):
    c = pa.Course(alpha=0.05)
    c.entrer("g1", [f"f{i}" for i in range(4)], 0.05)
    for g in range(10):
        for i in range(4):
            c.ajouter_trajectoire(f"f{i}", marche_a_prime(r, 20))
        c.lire()
    au_moins_une += bool(c.promues)
B["controle_sain_toutes_parties_ajoutees_20_pas_10_generations"] = {"P(au_moins_une_fausse_promotion)": au_moins_une / REP}
# biais exact E[max(1, e_20)] du monde A′ (le « 1,77 » de la v7)
e_max = sum(math.comb(20, k) / 2 ** 20 * max(1.0, 1.5 ** k * 0.5 ** (20 - k)) for k in range(21))
B["E[max(1,e_g)]_A_prime_20_pas_exact"] = e_max
S["B_partie_sautee"] = B

# ---------------------------------------------------------------- C : retrait, exclusion, partage de α
C = {}
# (1) l'exclusion d'une fiche ne fait que réduire les promotions (promues(sous-ensemble) ⊆ promues(ensemble))
r = rng(3, 0)
violations, essais = 0, 0
for _ in range(3000):
    n = r.randint(2, 9)
    log_e = {i: r.uniform(-1, 6) for i in range(n)}
    b = {i: r.uniform(0.001, 0.02) for i in range(n)}
    plein = pa.ebh_pondere(log_e, b)
    j = r.randrange(n)
    sous = pa.ebh_pondere({i: v for i, v in log_e.items() if i != j}, {i: v for i, v in b.items() if i != j})
    essais += 1
    violations += not sous <= plein
C["exclusion_reduit_les_promotions"] = {"tirages": essais, "violations": violations}
# (2) partage de α_g : le code tient-il une borne par génération ou seulement Σ α_c ≤ α ?
c = pa.Course(alpha=0.05)
c.entrer("g1-nouvelles", ["a"], 0.02)
c.entrer("g1-relecture", ["b"], 0.02)  # même génération, 0,04 > α_1 = 0,005 (α/10) : accepté ?
try:
    c.entrer("g1-temoin", ["t"], 0.02)  # 0,06 > α : refus attendu
    C["partage_alpha"] = {"somme_globale_tenue": False}
except ValueError as e:
    C["partage_alpha"] = {"somme_globale_tenue": True, "par_generation_tenue_par_le_code": False, "message": str(e)}
# (3) retrait : union garantie inchangée, rapportées réduites, exclue des lectures, bonferroni sans l'exclue ; retrait d'une
# fiche jamais promue ; retrait deux fois ; abandon après retrait silencieux
c = pa.Course(alpha=0.05)
c.entrer("g1", ["a", "b", "c"], 0.03)
for f, e in (("a", 200.0), ("b", 200.0), ("c", 60.0)):
    c.ajouter_trajectoire(f, [math.log(e)])
c.lire()
c.retirer("a", "panne")
c.retirer("a", "panne bis")  # second retrait : accepté ? (le motif est écrasé)
C["retrait"] = {"promues": sorted(c.promues), "rapportees": sorted(c.promues_rapportees()), "motif_final": c.retirees["a"],
                "bonferroni": sorted(c.bonferroni()), "exclues": sorted(c.exclues)}
try:
    c.ajouter_trajectoire("a", [0.0])
    C["retrait"]["partie_apres_retrait"] = "acceptée"
except ValueError:
    C["retrait"]["partie_apres_retrait"] = "refusée"
# (4) FDR de l'union sous nuls partiels, avec retraits aléatoires après chaque lecture (la retirée est exclue ensuite)
r = rng(3, 4)
fdp_union, fdp_rapporte, au_moins_une = 0.0, 0.0, 0
for _ in range(REP):
    c = pa.Course(alpha=0.05)
    nulles = set()
    for g in range(6):
        fam = [f"g{g}-{i}" for i in range(4)]
        c.entrer(f"g{g}", fam, 0.05 / 6)
        nulles |= set(fam[2:])
        for f in list(c.budgets):
            if f in c.gelees:
                continue
            if f in nulles:
                traj = marche_a_prime(r, 20)
            else:
                lw, traj = 0.0, []
                for _ in range(20):
                    lw += math.log(1.5) if r.random() < 0.7 else math.log(0.5)
                    traj.append(lw)
            c.ajouter_trajectoire(f, traj)
        nouvelles = c.lire()
        for f in nouvelles:
            if r.random() < 0.3:
                c.retirer(f, "panne simulée")
    fausses = len(c.promues & nulles)
    fdp_union += fausses / max(1, len(c.promues))
    rap = c.promues_rapportees()
    fdp_rapporte += len(rap & nulles) / max(1, len(rap))
    au_moins_une += fausses > 0
C["retraits_aleatoires_nuls_partiels"] = {"repetitions": REP, "FDR_union_avant_retraits": fdp_union / REP,
                                          "FDR_ensemble_rapporte": fdp_rapporte / REP, "P(au_moins_une_fausse)": au_moins_une / REP,
                                          "borne_somme_budgets_nulles": 0.05 / 2}
S["C_retrait_et_partage"] = C

# ---------------------------------------------------------------- D : monde sur banque de scores
D = {}
def monde_cal(scores, graine=3):
    eps = [{"id": f"e{i}", "unite": f"u{i}", "etiquette": "honnete", "partie": "calibrage", "strates": {}, "scores": {"a": s}}
           for i, s in enumerate(scores)]
    return mbs.MondeBanqueScores({"cellules": ["a"], "episodes": eps}, graine)
# (1) conforme strict : P(alerte d'un honnête neuf) exact par échangeabilité, continu et avec ex æquo lourds ; plusieurs τ, n
r = rng(4, 0)
res = {}
for tau, n in ((0.01, 99), (0.01, 199), (0.05, 19), (0.05, 199), (0.2, 7)):
    for loi in ("continu", "ex_aequo"):
        tot, alertes = 0, 0
        for _ in range(300):
            if loi == "continu":
                cal = [r.gauss(0, 1) for _ in range(n)]
                neufs = [r.gauss(0, 1) for _ in range(200)]
            else:
                cal = [float(r.randint(0, 4)) for _ in range(n)]
                neufs = [float(r.randint(0, 4)) for _ in range(200)]
            s = monde_cal(cal).seuil("a", tau)
            if s["calibrage_insuffisant"]:
                continue
            alertes += sum(x > s["seuil"] for x in neufs)
            tot += len(neufs)
        res[f"tau={tau},n={n},{loi}"] = {"taux_alerte_neufs": (alertes / tot if tot else None), "j_sur_n+1": math.floor(tau * (n + 1) + 1e-12) / (n + 1)}
D["conforme_strict"] = res
# (2) ex æquo : j-ième plus grand avec des valeurs répétées ; j exactement entier (τ(n+1) entier)
m = monde_cal([1.0] * 10 + [2.0] * 10)
D["ex_aequo_masse"] = m.seuil("a", 0.1)  # j = ⌊0,1·21⌋ = 2 → 2e plus grand = 2,0 ; masse 0,5 ; taux calibrage 0
D["j_entier_bord"] = {f"tau=0.05,n=19": monde_cal([float(i) for i in range(19)]).seuil("a", 0.05)["j"],
                      f"tau=0.1,n=9": monde_cal([float(i) for i in range(9)]).seuil("a", 0.1)["j"]}
# (3) fuite : les seuils ne dépendent que du calibrage (épreuve et développement modifiés) ; strate du calibrage
sys.path.insert(0, BASE)
from essais.test_v7_monde_banque_scores import banque_synthetique  # noqa: E402
bq = banque_synthetique(random.Random(43), unites_par_partie=(100, 50, 100))
m1 = mbs.MondeBanqueScores(bq, 17)
bq2 = copy.deepcopy(bq)
for ep in bq2["episodes"]:
    if ep["partie"] != "calibrage":
        ep["scores"]["blanc"] += 100.0
        ep["scores"]["noir"] -= 100.0
m2 = mbs.MondeBanqueScores(bq2, 17)
D["fuite_seuils"] = {"seuils_identiques": all(m1.seuil(cc, 0.05)["seuil"] == m2.seuil(cc, 0.05)["seuil"] for cc in ("blanc", "noir")),
                     "jumeau_identique": m1.jumeau_calibre("blanc", 0.05, "x")["seuil_1"] == m2.jumeau_calibre("blanc", 0.05, "x")["seuil_1"]}
# (4) ordre secret : déterministe, dépend de la graine, de l'étiquette et de l'empreinte de la banque ; indépendant de l'ordre d'entrée
u = [f"epr-{i}" for i in range(100)]
o1 = m1.ordre_secret(u, "k")
D["ordre_secret"] = {"deterministe": o1 == m1.ordre_secret(list(reversed(u)), "k"), "change_avec_graine": o1 != mbs.MondeBanqueScores(bq, 18).ordre_secret(u, "k"),
                     "change_avec_etiquette": o1 != m1.ordre_secret(u, "k2"), "change_avec_banque": o1 != m2.ordre_secret(u, "k")}
# (5) jumeau calibré : moitiés disjointes par unité, couvrant tout le calibrage ; seuils sur les moitiés
jm = m1.jumeau_calibre("blanc", 0.05, "x")
D["jumeau"] = {"disjointes": not (set(jm["moitie_1"]) & set(jm["moitie_2"])), "couvrent": sorted(jm["moitie_1"] + jm["moitie_2"]) == m1.unites("calibrage"),
               "n1": jm["seuil_1"]["n"], "n2": jm["seuil_2"]["n"]}
# (6) parts : convention « > » cohérente avec le seuil ; unité sans sabotés absente des contrastes mais présente dans la garde
S["D_monde_banque"] = D

# ---------------------------------------------------------------- E : engagement apparié
E = {}
m = mbs.MondeBanqueScores(banque_synthetique(random.Random(59), unites_par_partie=(100, 30, 30)), 23)
BN = {"noir": {"coefficients": {"blanc": 1, "noir": -1}}}
e = ea.construire(m, BN, tau=0.05)
# (1) altération puis re-scellement : evaluer accepte-t-elle ?
alt = copy.deepcopy(e)
alt["cle_heritage"]["seuils"]["blanc"] -= 1.0
alt["empreinte_cle"] = ea.empreinte_objet(alt["cle_heritage"])
alt["empreinte"] = ea.empreinte_objet({k: v for k, v in alt.items() if k != "empreinte"})
try:
    r_alt = ea.evaluer(m, alt)
    E["alteration_rescellee"] = {"acceptee": True, "ordre_change": r_alt["empreinte_cle"] != e["empreinte_cle"]}
except ea.EngagementInvalide as ex:
    E["alteration_rescellee"] = {"acceptee": False, "message": str(ex)}
# (2) la partie lue est-elle dans la clé ? développement et épreuve → même clé ?
e_dev = ea.construire(m, BN, tau=0.05, partie="developpement")
E["partie_dans_la_cle"] = {"cle_identique_dev_et_epreuve": e_dev["empreinte_cle"] == e["empreinte_cle"],
                           "champs_cle": sorted(e["cle_heritage"]), "lambdas_dans_la_cle": "lambdas" in e["cle_heritage"]}
# (3) identité des unités : même engagement évalué deux fois sur la même banque → même trajectoire ; la course l'accepte
# deux fois (deux générations) : la même partie comptée deux fois
r1 = ea.evaluer(m, e)
r2 = ea.evaluer(m, e)
c = pa.Course(alpha=0.05)
c.entrer("g1", ["fiche"], 0.05)
c.ajouter_trajectoire("fiche", r1["trajectoire_log_min"])
c.lire()
try:
    c.ajouter_trajectoire("fiche", r2["trajectoire_log_min"])
    E["memes_unites_deux_fois"] = {"trajectoires_identiques": r1["trajectoire_log_min"] == r2["trajectoire_log_min"],
                                   "course_accepte_la_repetition": True, "identifiants_unites_rendus": "unites" in r1 and not isinstance(r1["unites"], int),
                                   "unites_lues_est_un_nombre": isinstance(r1["unites_lues"], int)}
except ValueError as ex:
    E["memes_unites_deux_fois"] = {"course_accepte_la_repetition": False, "message": str(ex)}
# (4) seuils du seul calibrage, strate comprise : construire avec strate → seuils calculés sur le calibrage de la strate
e_s = ea.construire(m, BN, tau=0.05, strate={"mode": "cout"})
E["seuils_strate"] = {"seuil_blanc_strate": e_s["cle_heritage"]["seuils"]["blanc"], "seuil_blanc_global": e["cle_heritage"]["seuils"]["blanc"],
                      "egal_au_calcul_direct": e_s["cle_heritage"]["seuils"]["blanc"] == m.seuil("blanc", 0.05, {"mode": "cout"})["seuil"]}
# (5) alignement garde / contrastes : unités de l'épreuve sans sabotés ou sans honnêtes → longueurs différentes, indices désalignés
bq3 = banque_synthetique(random.Random(67), unites_par_partie=(100, 0, 40))
for ep in bq3["episodes"]:
    pass
# retirer les honnêtes de la moitié des unités d'épreuve, les sabotés d'un quart
eps3 = []
for ep in bq3["episodes"]:
    if ep["partie"] == "epreuve":
        k = int(ep["unite"].split("-")[1])
        if k % 2 == 0 and ep["etiquette"] == "honnete":
            continue
        if k % 4 == 1 and ep["etiquette"] == "sabote":
            continue
    eps3.append(ep)
bq3["episodes"] = eps3
m3 = mbs.MondeBanqueScores(bq3, 29)
e3 = ea.construire(m3, BN, tau=0.05, garde={"a": "blanc", "b": "noir", "delta": 0.1})
r3 = ea.evaluer(m3, e3)
parts3 = m3.parts(e3["cle_heritage"]["seuils"], "epreuve")
ordre3 = m3.ordre_secret(parts3, e3["empreinte"])
sab = [u_ for u_ in ordre3 if parts3[u_]["r"]]
hon = [u_ for u_ in ordre3 if parts3[u_]["f"]]
E["alignement_garde"] = {"n_contrastes": r3["unites"], "n_garde": len(hon), "n_sabotes": len(sab),
                         "meme_unite_au_meme_indice": sum(a == b for a, b in zip(sab, hon)),
                         "lecture": "min pris par indice (pa.evaluer), non par position dans l'ordre secret : filtrations différentes quand les ensembles d'unités diffèrent"}
S["E_engagement"] = E

# ---------------------------------------------------------------- F : chiffres de la v7
F = {"k=4_temoin_compris": {"seuil_5/(0,05*4)": 5 / (0.05 * 4), "borne_0,05*4/5": 0.05 * 4 / 5},
     "attendu_11_sur_400": {"0,0275*400": 0.0275 * 400, "0,025*400": 0.025 * 400},
     "E[max(1,e_g)]_1,77": round(e_max, 4), "259_essais": total}
S["F_chiffres"] = F

S["manifeste"]["duree_secondes"] = round(time.time() - debut, 1)
print(json.dumps(S, ensure_ascii=False, indent=1, default=str))
