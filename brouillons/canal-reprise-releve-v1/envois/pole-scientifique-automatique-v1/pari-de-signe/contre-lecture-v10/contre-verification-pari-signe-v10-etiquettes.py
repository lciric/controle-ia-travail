"""Contre-vérification v10, sections L (étiquettes d'ordre restantes) et F (gardes de la « forme-G1 » de la démonstration).

L : ce qui change l'ordre secret d'une tranche **sans changer la clé de l'héritage** ni l'empreinte des unités (seules
    choses que la `Course` confronte) : le nom du contraste (`noms`, hors clé, dans l'empreinte de l'engagement), le budget
    de l'engagement (α_c, m_c), la graine du monde, une unité ajoutée à la banque hors du plan ; et la génération passée
    en chaîne (« 1 ») au journal.
F : la course publiée v28 (banque reproduite par la graine) : pour la fiche « forme-G1 », parties des générations 1 à 3
    recalculées par `engagement_apparie.evaluer` ; richesses par comparateur, **gardes**, et minimum final, contre les
    incréments de log e de `course.json`.

Usage : /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v10-etiquettes.py RACINE > sortie.json
"""

import copy
import hashlib
import importlib.util
import json
import os
import random
import sys

RACINE = os.path.abspath(sys.argv[1])
sys.path.insert(0, RACINE)
from pole import engagement_apparie as ea  # noqa: E402
from pole import monde_banque_scores as mbs  # noqa: E402
from pole import pari_apparie as pa  # noqa: E402
from pole.outils import graine_derivee  # noqa: E402

_spec = importlib.util.spec_from_file_location("demo_pari_apparie_v7", os.path.join(RACINE, "demonstrations", "demo_pari_apparie_v7.py"))
demo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(demo)


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def essai(f):
    try:
        return {"issue": "acceptée", "valeur": f()}
    except Exception as e:  # noqa: BLE001
        return {"issue": "refusée", "erreur": f"{type(e).__name__}: {str(e)[:160]}"}


def section_L():
    out = {}
    b = demo.banque(random.Random(11), 2, 40)
    m = mbs.MondeBanqueScores(b, 5)
    plan = demo.plan_des_tranches(m, 2)
    coef = {"blanc": 1, "blanc_jumeau": -1}
    base = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, plan_tranches=plan)
    r0 = ea.evaluer(m, base, generation=1)
    variantes = {
        "nom_du_contraste": (m, ea.construire(m, {"autre-nom": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, plan_tranches=plan)),
        "budget_alpha_c_m_c": (m, ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.01, m_c=7, plan_tranches=plan)),
        "graine_du_monde": (mbs.MondeBanqueScores(b, 6), base),
    }
    b2 = copy.deepcopy(b)
    b2["episodes"].append(dict(copy.deepcopy(b["episodes"][0]), id="factice-0", unite="factice", partie="developpement"))
    m2 = mbs.MondeBanqueScores(b2, 5)
    variantes["unite_factice_hors_plan"] = (m2, ea.construire(m2, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, plan_tranches=plan))
    noms_essayes = {f"c{k}" for k in range(100)}
    ordres = set()
    for nom in sorted(noms_essayes):
        e = ea.construire(m, {nom: {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, plan_tranches=plan)
        assert e["empreinte_cle"] == base["empreinte_cle"]
        ordres.add(tuple(ea.evaluer(m, e, generation=1)["trajectoire_log_min"]))
    out["cent_noms_meme_cle_ordres_distincts"] = len(ordres)
    for nom, (mv, ev) in variantes.items():
        rv = ea.evaluer(mv, ev, generation=1)
        lg = ea.Lignees()
        lg.entrer("f", base)
        c = pa.Course(alpha=0.05, journal=lg)
        c.entrer("g1", ["f"], 0.05, cles={"f": base["empreinte_cle"]})
        rj = ea.evaluer(mv, ev, generation=1, fiche="f", journal=lg)
        out[nom] = {"meme_cle": ev["empreinte_cle"] == base["empreinte_cle"],
                    "meme_empreinte_unites": rv["empreinte_unites"] == r0["empreinte_unites"],
                    "trajectoire_differente": rv["trajectoire_log_min"] != r0["trajectoire_log_min"],
                    "finale_egale": abs(rv["trajectoire_log_min"][-1] - r0["trajectoire_log_min"][-1]) < 1e-9,
                    "lignees_entrer_meme_fiche": essai(lambda: lg.entrer("f", ev))["issue"],
                    "course_ajout": essai(lambda: c.ajouter_trajectoire("f", rj["trajectoire_log_min"], unites=rj["identifiants_unites"],
                                                                        empreinte_cle=rj["empreinte_cle"], empreinte_unites=rj["empreinte_unites"]))["issue"]}
    # génération passée en chaîne : seconde évaluation de la même fiche dans la même génération, journalisée mais invisible
    lg = ea.Lignees()
    ea.evaluer(m, base, generation=1, fiche="f", journal=lg)
    out["generation_en_chaine_seconde_evaluation"] = essai(lambda: ea.evaluer(m, base, generation="1", fiche="f", journal=lg)["unites"])["issue"]
    out["generation_en_chaine_entrees_au_journal"] = [j["generation"] for j in lg.journal]
    out["journal_garde_les_identifiants_des_unites"] = "identifiants_unites" in lg.journal[0] or "unites_ids" in lg.journal[0]
    return out


def section_F():
    dossier = os.path.join(os.path.dirname(RACINE), "pari-de-signe", "demonstration-v28")
    with open(os.path.join(dossier, "course.json"), encoding="utf-8") as f:
        publie = json.load(f)
    b = demo.banque(random.Random(graine_derivee(20261028, "banque")), 4, 40)
    m = mbs.MondeBanqueScores(b, graine_derivee(20261028, "monde"))
    plan = demo.plan_des_tranches(m, 4)
    m_c = publie["journal"][0]["m_c"]
    e = demo.construire_engagement(m, "forme-G1", demo.fiche_forme_g1(), 0.05, 0.05 / 4, m_c, plan)
    out = {"banque_reproduite": m.empreinte, "m_c": m_c, "empreinte_cle_egale_a_la_publiee": e["empreinte_cle"] == publie["cles"]["forme-G1"],
           "parties": {}}
    precedent = 0.0
    for g in (1, 2, 3):
        r = ea.evaluer(m, e, generation=g)
        log_e_publie = next(x["parties"]["forme-G1"]["log_e_valeur"] for x in publie["journal"] if x["generation"] == g)
        finales = dict(r["log_richesse_finale_par_comparateur"])
        gardes = dict(r["log_gardes_finales"])
        tout = {**{f"contraste {k}": v for k, v in finales.items()}, **{f"garde {k}": v for k, v in gardes.items()}}
        out["parties"][g] = {"richesses_par_comparateur": finales, "gardes": gardes,
                             "minimum_final_de_la_partie": r["trajectoire_log_min"][-1],
                             "composante_qui_lie": min(tout, key=tout.get),
                             "increment_publie_de_log_e": log_e_publie - precedent}
        precedent = log_e_publie
    cumul = {}
    for g in (1, 2, 3):
        for k, v in {**out["parties"][g]["richesses_par_comparateur"], **{f"garde {k}": v for k, v in out["parties"][g]["gardes"].items()}}.items():
            cumul[k] = cumul.get(k, 0.0) + v
    out["cumul_sur_trois_parties"] = cumul
    out["composante_cumulee_la_plus_basse"] = min(cumul, key=cumul.get)
    return out


def principal():
    sortie = {"manifeste": {"script": os.path.basename(__file__), "sha256_script": sha(os.path.abspath(__file__)),
                            "python": sys.version.split()[0],
                            "sha256_code": {p: sha(os.path.join(RACINE, p)) for p in (
                                "pole/pari_apparie.py", "pole/engagement_apparie.py", "pole/monde_banque_scores.py",
                                "demonstrations/demo_pari_apparie_v7.py")}},
              "L": section_L(), "F": section_F()}
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print()


if __name__ == "__main__":
    principal()
