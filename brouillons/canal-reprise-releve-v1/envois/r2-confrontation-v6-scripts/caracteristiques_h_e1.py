"""Caractéristiques de la règle gelée de H-E1 (analyse.difference_h_e1 et lecture_h_e1 du commit e82c341, plus la règle
de cohérence par course de la v6) sous un effet nul, avec un effet de course partagé par les 5 lignées d'une course.
Modèle illustratif du relecteur, NON OPPOSABLE (R7) : 2 courses × 5 lignées-graines ; 60 tâches de test final
(conscience 18/18, délégation 12/12) ; exactitude de base par lignée U(0,60 ; 0,80) dans les deux bras ; bras gelé
sans gain ; bras adaptatif : gain = c_course + e_lignée, c ~ N(0, σ_c), e ~ N(0, 0,05) ; moyenne vraie du gain nulle.
Réponses tirées tâche par tâche. Graines : SeedSequence(20261024), une graine fille par répétition."""
import json, sys, time
import numpy as np
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3 import analyse

def taches():
    t = []
    for fam, (pos, neg), n in (("conscience-evaluation", ("evaluation", "usage-reel"), 18), ("controle-delegation", ("sabotage", "honnete"), 12)):
        for k in range(n):
            t.append({"id": f"{fam}-p{k}", "famille": fam, "etiquettes": [pos, neg], "verite": pos})
            t.append({"id": f"{fam}-n{k}", "famille": fam, "etiquettes": [pos, neg], "verite": neg})
    return t

def reponses(rng, tt, p):
    p = float(np.clip(p, 0.02, 0.98))
    return {t["id"]: (t["verite"] if rng.random() < p else (t["etiquettes"][1] if t["verite"] == t["etiquettes"][0] else t["etiquettes"][0])) for t in tt}

def une_experience(rng, tt, sigma_c, sigma_e=0.05, n_tirages=300):
    paires, par_course = [], {0: [], 1: []}
    for k in (0, 1):
        c = rng.normal(0, sigma_c)
        for i in range(5):
            b = rng.uniform(0.60, 0.80)
            g = c + rng.normal(0, sigma_e)
            p = {"lignee_graine": f"c{k}l{i}", "adaptatif": {"g0": reponses(rng, tt, b), "gfin": reponses(rng, tt, b + g)},
                 "gele": {"g0": reponses(rng, tt, b), "gfin": reponses(rng, tt, b)}}
            paires.append(p)
    r = analyse.difference_h_e1(paires, tt, int(rng.integers(1, 2**31)), n_tirages=n_tirages)
    for nom, d in r["par_lignee_graine"].items():
        par_course[int(nom[1])].append(d)
    moyennes = [float(np.mean(v)) for v in par_course.values()]
    lecture = analyse.lecture_h_e1(r)
    confirme_code = lecture == "confirmé"
    confirme_v6 = confirme_code and all(m > 0 for m in moyennes)
    return confirme_code, confirme_v6, lecture.startswith("réfuté")

if __name__ == "__main__":
    n_rep = int(sys.argv[1]); sigmas = [float(x) for x in sys.argv[2].split(",")]
    tt = taches()
    ss = np.random.SeedSequence(20261024)
    sortie = {"n_repetitions": n_rep, "n_tirages_bootstrap": 300, "scenarios": {}}
    debut = time.time()
    for j, s in enumerate(sigmas):
        enfants = ss.spawn(1)[0].spawn(n_rep)
        res = [une_experience(np.random.default_rng(e), tt, s) for e in enfants]
        sortie["scenarios"][f"sigma_course={s}"] = {"confirme_table_du_code": round(np.mean([a for a, _, _ in res]), 3),
                                                    "confirme_avec_regle_par_course_v6": round(np.mean([b for _, b, _ in res]), 3),
                                                    "refute": round(np.mean([c for _, _, c in res]), 3)}
    sortie["duree_s"] = round(time.time() - debut, 1)
    print(json.dumps(sortie, ensure_ascii=False, indent=1))
