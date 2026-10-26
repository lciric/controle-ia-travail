"""Lanceur (v1) : exécute les bras sur 400 mondes par condition, agrège (moyennes, intervalles à 95 % par
rééchantillonnage apparié des mondes), applique la règle de décision du préenregistrement scellé.
Usage : python3 -I -B trancher_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)" [--mondes 400] [--processus 2]
Écrit : resultats-trancher-recombinaison-v1.json (agrégats, décision, manifeste) et
        mondes-trancher-recombinaison-v1.jsonl (mesures brutes par monde et par bras).
"""
import argparse
import hashlib
import json
import multiprocessing
import random
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import conditions_v1 as cd
import mesures_v1 as ms
import methodes_v1 as mt
import monde_v1 as mo

ICI = Path(__file__).resolve().parent
PREENREGISTREMENT = "preenregistrement-trancher-recombinaison-v1.md"
SEUIL = 0.12
TOUTES = {**cd.CONDITIONS, **cd.SENSIBILITE}
METRIQUES_IC = ["precision", "rappel", "precision_placebo", "part_eloignes"]


def un_monde(tache):
    condition, indice = tache
    graine = cd.graine_monde(cd.GRAINE_BASE_PRINCIPALE, condition, indice)
    w = mo.generer(TOUTES[condition], graine)
    df = ms.frequences_etiquettes(w)
    sorties, gamma_e = mt.executer(w, df)
    return {"condition": condition, "indice": indice, "graine": graine, "n_champs": w["n_champs"],
            "n_valides": len(w["valides"]), "n_vrais": len(w["vrais"]),
            "n_vrais_valides": len(w["vrais"] & set(w["valides"])), "gamma_rapport": gamma_e,
            "bras": {b: ms.mesurer(w, s, df) for b, s in sorties.items()}}


def serie(lignes, bras, metrique):
    return [(l["bras"][bras] or {}).get(metrique) for l in lignes]


def agreger(lignes, rng):
    out = {"moyennes": {}, "ic": {}, "ecarts": {}}
    for b in mt.BRAS:
        defini = [l["bras"][b] for l in lignes if l["bras"][b] is not None]
        out["moyennes"][b] = {k: (sum(d[k] for d in defini if d[k] is not None) / max(1, sum(1 for d in defini if d[k] is not None)))
                              if any(d[k] is not None for d in defini) else None
                              for k in (defini[0] if defini else {})}
        out["moyennes"][b]["mondes_definis"] = len(defini)
        out["ic"][b] = {m: ms.moyenne_ic(serie(lignes, b, m), rng) for m in METRIQUES_IC}
    comparaisons = [(b, "b_stratifie") for b in mt.BRAS if b != "b_stratifie"]
    comparaisons += [("d1_marche_swanson", "a_corrige"), ("d2_contraste_import", "a_corrige"), ("a_corrige", "c_uniforme")]
    for a, b in comparaisons:
        out["ecarts"][f"{a}-{b}"] = {m: ms.difference_ic(serie(lignes, a, m), serie(lignes, b, m), rng)
                                    for m in ("precision", "rappel", "precision_placebo")}
    return out


def par_nombre_de_champs(lignes, rng):
    res = {}
    for f in (2, 3, 4):
        sous = [l for l in lignes if l["n_champs"] == f]
        if not sous:
            continue
        res[str(f)] = {"mondes": len(sous),
                       "precision": {b: ms.moyenne_ic(serie(sous, b, "precision"), rng, 1000) for b in mt.BRAS},
                       "ecarts": {f"{a}-b_stratifie": ms.difference_ic(serie(sous, a, "precision"),
                                                                       serie(sous, "b_stratifie", "precision"), rng, 1000)
                                  for a in ("a_corrige", "d1_marche_swanson", "d2_contraste_import", "c_uniforme")}}
    return res


def decider(agg):
    """Règle du préenregistrement, section 5, codée telle qu'écrite."""
    ec = lambda c, a, b, m="precision": agg[c]["ecarts"][f"{a}-{b}"][m]
    prec = lambda c, b: agg[c]["moyennes"][b]["precision"]
    db, dm = ec("M_bien", "a_corrige", "b_stratifie"), ec("M_moyen", "a_corrige", "b_stratifie")
    seuils = db["moyenne"] >= SEUIL and dm["moyenne"] >= SEUIL
    sp = ec("SP_sans_pont", "a_corrige", "b_stratifie", "precision_placebo")
    sp_perte = sp["ic95"][1] < 0
    sp_artefact = sp["ic95"][0] > 0 or sp["ic95"][1] < 0
    inv = ec("INV_verite_inversee", "a_corrige", "b_stratifie")
    inv_perd = inv["ic95"][1] < 0
    vdom = ec("V_domaines_mal_separes", "a_corrige", "b_stratifie")
    vdom_echec = seuils and vdom["moyenne"] >= db["moyenne"]
    adoptee = seuils and not sp_perte and not sp_artefact and inv_perd and not vdom_echec
    formes = {}
    for f in ("d1_marche_swanson", "d2_contraste_import"):
        gb, gm = ec("M_bien", f, "b_stratifie"), ec("M_moyen", f, "b_stratifie")
        spf = ec("SP_sans_pont", f, "b_stratifie", "precision_placebo")
        art = spf["ic95"][0] > 0 or spf["ic95"][1] < 0
        bat_a = prec("M_bien", f) > prec("M_bien", "a_corrige") and prec("M_moyen", f) > prec("M_moyen", "a_corrige")
        formes[f] = {"ecart_bien": gb["moyenne"], "ecart_moyen": gm["moyenne"], "artefact_sans_pont": art,
                     "bat_a_bien_et_moyen": bat_a,
                     "retenable": gb["moyenne"] >= SEUIL and gm["moyenne"] >= SEUIL and not art and bat_a}
    retenables = [f for f in formes if formes[f]["retenable"]]
    if retenables:
        meilleure = max(retenables, key=lambda f: prec("M_bien", f) + prec("M_moyen", f))
        decision = f"une autre forme retenue ({meilleure})"
    else:
        decision = "adoptée" if adoptee else "réfutée"
    return {"decision": decision, "seuil_points": SEUIL,
            "a_moins_b": {"M_bien": db, "M_moyen": dm, "SP_placebo": sp, "INV": inv, "V_domaines": vdom},
            "seuils_atteints": seuils, "sans_pont_perte": sp_perte, "sans_pont_artefact": sp_artefact,
            "inverse_a_perd": inv_perd, "domaines_mal_separes_echec": vdom_echec, "adoptee_selon_regle_1_a_4": adoptee,
            "formes_d": formes}


def empreinte(nom):
    return hashlib.sha256((ICI / nom).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    ap.add_argument("--mondes", type=int, default=400)
    ap.add_argument("--processus", type=int, default=2)
    args = ap.parse_args()
    t0 = time.time()
    taches = [(c, i) for c in TOUTES for i in range(args.mondes)]
    with multiprocessing.get_context("fork").Pool(args.processus) as pool:
        lignes = list(pool.imap(un_monde, taches, chunksize=25))
    duree_runs = time.time() - t0
    with open(ICI / "mondes-trancher-recombinaison-v1.jsonl", "w", encoding="utf-8") as fh:
        for l in lignes:
            fh.write(json.dumps(l, ensure_ascii=False, separators=(",", ":")) + "\n")
    agg = {}
    for c in TOUTES:
        sous = [l for l in lignes if l["condition"] == c]
        agg[c] = agreger(sous, random.Random(20261026))
        agg[c]["mondes"] = len(sous)
        agg[c]["vrais_moyens"] = sum(l["n_vrais"] for l in sous) / len(sous)
        agg[c]["vrais_valides_moyens"] = sum(l["n_vrais_valides"] for l in sous) / len(sous)
        agg[c]["valides_moyens"] = sum(l["n_valides"] for l in sous) / len(sous)
        gam = [l["gamma_rapport"] for l in sous if l["gamma_rapport"] is not None]
        agg[c]["gamma_rapport"] = {"mondes_ou_elle_tourne": len(gam), "mediane": sorted(gam)[len(gam) // 2] if gam else None}
        if c in ("M_bien", "M_moyen", "INV_verite_inversee"):
            agg[c]["par_nombre_de_champs"] = par_nombre_de_champs(sous, random.Random(20261026))
    sortie = {
        "objet": "trancher la recombinaison bisociative : forme corrigée contre tirage stratifié (seuil 12 points)",
        "heure_lancement_utc": args.heure, "duree_s": round(time.time() - t0, 1), "duree_runs_s": round(duree_runs, 1),
        "python": sys.version.split()[0],
        "preenregistrement": {"fichier": PREENREGISTREMENT, "sha256": empreinte(PREENREGISTREMENT)},
        "code_sha256": {n: empreinte(n) for n in ("monde_v1.py", "conditions_v1.py", "mesures_v1.py", "methodes_v1.py", "trancher_v1.py")},
        "graines": {"mondes": f"random.Random({cd.GRAINE_BASE_PRINCIPALE} + 100000 x identifiant + indice)",
                    "identifiants": cd.IDENTIFIANTS, "bras": "random.Random(f'{graine du monde}-{bras}')",
                    "placebo": "random.Random(f'placebo-{graine du monde}')", "reechantillonnage": "random.Random(20261026) par condition"},
        "budget": {"k_par_generation": mt.K_PAR_GENERATION, "generations": mt.GENERATIONS, "paires_par_monde": mt.BUDGET},
        "mondes_par_condition": args.mondes, "base": mo.BASE, "niveaux": mo.NIVEAUX, "conditions": TOUTES,
        "decision": decider(agg), "agregats": agg,
    }
    (ICI / "resultats-trancher-recombinaison-v1.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n",
                                                                  encoding="utf-8")
    print("décision :", sortie["decision"]["decision"], "| durée", sortie["duree_s"], "s")


if __name__ == "__main__":
    main()
