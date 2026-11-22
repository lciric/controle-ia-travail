#!/usr/bin/env python3
"""Base gloutonne renforcée (aucun appel de modèle, aucun réseau) : la recherche gloutonne bornée de la v1 (B3 de
`bases_sans_modele_v1.py`, importé et vérifié contre son compagnon, inchangé) **plus un niveau de condition** — v1.

Règle écrite avant toute course (aucun réglage après lecture) :
- Candidats d'une génération = candidats de la v1 (une addition d'un effet : principal, seuil, interaction de seuil,
  sous-population, interaction de sous-population ; seuils {−0,5 ; 0 ; 0,5}) **plus les composites « effet si condition »** :
  pour tout trait t, tout trait de condition c ≠ t et tout seuil s de {−0,5 ; 0 ; 0,5}, l'addition conjointe de
  {principal sur t} et {interaction de seuil : pente de t si z_c > s}, soit une pente de z_t propre à chaque branche de z_c > s.
  Un composite est omis si le principal sur t est déjà dans la loi courante (le candidat v1 « interaction de seuil » le couvre
  alors) ou si la loi dépasserait 3 conditions de seuil distinctes (borne de la grammaire servie, v4 § 2.2).
  Borne : au plus 8 × 7 × 3 = 168 composites, et au plus CANDIDATS_MAX = 420 candidats par génération (refus au-delà).
- Ajustement, classement, nombre de cartes (18, 17, 17 = 52), loi courante : exactement la v1 (fonctions importées).
- Mêmes 12 mondes de développement MR-2, mêmes données servies (même graine), même oracle (`OracleCache` de la v1), même mesure
  (`mesurer` de la v1 : composante couverte seulement par une carte « vraie »).
- La base v1 (B3) est **recourue** ici avec son code importé ; son résultat doit égaler la sortie scellée v1 (contrôle).
Aucune base ne lit l'oracle, la loi du monde ni un verdict pendant la recherche ; l'oracle ne sert qu'à mesurer après.

Objets de contrôle (mondes écrits ici, déclarés, sans C8) :
- CTRL-COND : K1 forte (principal z0), moyenne principal z1, conditionnelle (interaction_xor : z2 de signe opposé selon z1 > 0),
  faible seuil z3 ; attendu : la base renforcée couvre la conditionnelle ;
- CTRL-SANS : mêmes effets, la conditionnelle remplacée par une moyenne d'interaction de sous-population sur z2 ; attendu :
  aucune « condition inventée vraie » (carte à composite dont la partie conditionnelle apporte ≥ 0,02 nat de gain d'oracle
  au-delà de la même carte sans elle, réajustée) et aucune composante conditionnelle couverte (il n'y en a pas).
Mesure « apport de la condition » sur toute carte à composite, dans tous les mondes (rapportée).

Usage : python -I -B base_gloutonne_renforcee_v1.py SORTIE.json [MONDES…]   (refuse d'écraser)
"""
import datetime
import hashlib
import json
import os
import sys

import numpy as np

V1_DOSSIER = "/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1"
V1_SCRIPT = os.path.join(V1_DOSSIER, "bases_sans_modele_v1.py")
V1_SORTIE = os.path.join(V1_DOSSIER, "bases-sans-modele-v1-sortie.json")


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def verifier(chemin):
    s, c = sha(chemin), open(chemin + ".sha256", encoding="utf-8").read().split()[0]
    if s != c:
        raise SystemExit(f"refus : {chemin} d'empreinte {s}, compagnon {c}")
    return s


SHA_V1 = verifier(V1_SCRIPT)
SHA_V1_SORTIE = verifier(V1_SORTIE)
sys.path.insert(0, V1_DOSSIER)
import bases_sans_modele_v1 as B  # noqa: E402  (vérifie et importe à son tour les outils v1 à v4)

M, P1, V4 = B.M, B.P1, B.V4
SEUILS, PAR_GENERATION = B.SEUILS, B.PAR_GENERATION
CANDIDATS_MAX = 420
RACINE_CTRL = 20261122


def cle_json(o):
    return json.dumps(o, sort_keys=True)


def conds(ef):
    return {(x.get("trait_condition", x.get("trait")), x["seuil"]) for x in ef if x["type"] in ("seuil", "interaction_seuil")}


def candidats_renforces(courant, D, nsp):
    """Candidats v1 (chacun une liste d'un effet) puis composites « effet si condition » (listes de deux effets)."""
    out = [[e] for e in B.candidats(courant, D, nsp)]
    deja = {cle_json(e) for e in courant}
    for t in range(D):
        pr = {"type": "principal", "trait": t}
        if cle_json(pr) in deja:
            continue
        for c in range(D):
            if c == t:
                continue
            for s in SEUILS:
                it = {"type": "interaction_seuil", "trait_condition": c, "seuil": s, "trait": t}
                if cle_json(it) in deja or len(conds(courant + [pr, it])) > 3:
                    continue
                out.append([pr, it])
    if len(out) > CANDIDATS_MAX:
        raise SystemExit(f"refus : {len(out)} candidats > borne {CANDIDATS_MAX}")
    return out


def base_glouton_renforcee(spec, oc, donnees):
    Z, G, Y = donnees
    n = len(Y)
    a = int(0.75 * n)
    K = spec["nombre_issues"]
    courant = B.effets_k1(oc)
    cartes, trajet = [], []
    for g, nb in enumerate(PAR_GENERATION, start=1):
        th0 = B.ajuster(courant, Z[:a], G[:a], Y[:a], K)
        v0 = B.logvrais(courant, th0, Z[a:], G[a:], Y[a:])
        notes = []
        cands = candidats_renforces(courant, spec["dimension"], spec["sous_populations"])
        for ajout in cands:
            ef = courant + ajout
            th = B.ajuster(ef, Z[:a], G[:a], Y[:a], K, iterations=150)
            notes.append((B.logvrais(ef, th, Z[a:], G[a:], Y[a:]) - v0, cle_json(ajout), ajout))
        notes.sort(key=lambda x: (-x[0], x[1]))
        for gain, _, ajout in notes[:nb]:
            ef = courant + ajout
            cartes.append({"generation": g, "loi": B.loi_de(ef, B.ajuster(ef, Z, G, Y, K), spec), "ajout": ajout,
                           "composite": len(ajout) == 2, "courant": list(courant), "gain_validation": round(gain, 6)})
        trajet.append({"generation": g, "candidats": len(cands), "composites": sum(1 for c in cands if len(c) == 2),
                       "meilleur": notes[0][2], "gain": round(notes[0][0], 6)})
        if notes[0][0] > 0:
            courant = courant + notes[0][2]
    return cartes, trajet


def apport_condition(carte, spec, oc, donnees):
    """Gain d'oracle de la carte moins celui de la même loi sans la partie « interaction de seuil » du composite (réajustée
    sur les mêmes données servies). Mesure après coup ; ne sert à aucune décision de la base."""
    Z, G, Y = donnees
    K = spec["nombre_issues"]
    sans = carte["courant"] + [carte["ajout"][0]]
    loi_sans = B.loi_de(sans, B.ajuster(sans, Z, G, Y, K), spec)
    return float(oc.o.gain(carte["loi"]) - oc.o.gain(loi_sans))


def mesurer_plus(cartes, oc, info, spec, donnees):
    m = B.mesurer(cartes, oc, info)
    jug = [oc.juger_carte(c["loi"]) for c in cartes]
    cond_ids = set(m["conditionnelles"])
    par_cond = {}
    for i in m["conditionnelles"]:
        porteuses = [k for k, j in enumerate(jug) if j["classe"] == "vraie" and i in j.get("captes", [])]
        par_cond[i] = {"couverte": bool(porteuses), "cartes_porteuses": len(porteuses),
                       "premiere_generation": min((cartes[k]["generation"] for k in porteuses), default=None),
                       "porteuses_composites": sum(1 for k in porteuses if cartes[k].get("composite"))}
    apports = []
    for k, c in enumerate(cartes):
        if c.get("composite"):
            ap = apport_condition(c, spec, oc, donnees)
            apports.append({"carte": k, "generation": c["generation"], "classe": jug[k]["classe"], "apport": round(ap, 6),
                            "captes_conditionnelle": sorted(set(jug[k].get("captes", [])) & cond_ids), "ajout": c["ajout"]})
    m["par_conditionnelle"] = par_cond
    m["cartes_composites"] = len(apports)
    m["conditions_inventees_vraies"] = sum(1 for a in apports if a["classe"] == "vraie" and a["apport"] >= M.SEUIL_ORACLE)
    m["apports_condition"] = apports
    m["par_composante"] = {i: (i in m["couvertes"]) for i in info["classes"] if i != oc.eid_k1}
    return m


# --- mondes de contrôle (écrits ici) ------------------------------------------------------------------------------------------
def _dir_fixe(rng, K=3):
    v = rng.standard_normal(K)
    v -= v.mean()
    return v / np.linalg.norm(v)


def monde_controle(avec_conditionnelle):
    rng = np.random.default_rng(np.random.SeedSequence(RACINE_CTRL, spawn_key=(9, 1)))
    K, D, nsp = 3, 8, 3
    effets = [{"id": "E1", "classe": "forte", "type": "principal", "trait": 0, "pente": _dir_fixe(rng).tolist()},
              {"id": "E2", "classe": "moyenne", "type": "principal", "trait": 1, "pente": _dir_fixe(rng).tolist()},
              {"id": "E4", "classe": "faible", "type": "seuil", "trait": 3, "seuil": 0.5, "decalage": _dir_fixe(rng).tolist()}]
    d3 = _dir_fixe(rng).tolist()
    if avec_conditionnelle:
        effets.append({"id": "E3", "classe": "conditionnelle", "type": "interaction_xor", "trait": 2, "trait_condition": 1,
                       "composante_condition": "E2", "pente": d3})
    else:
        effets.append({"id": "E3", "classe": "moyenne", "type": "interaction_sous_population", "trait": 2,
                       "sous_population": 1, "pente": d3})
    cibles = {"E1": 0.17, "E2": 0.06, "E3": 0.06, "E4": 0.027}
    spec = {"version": "monde-riche-spec-v1", "nombre_issues": K, "dimension": D, "sous_populations": nsp,
            "biais": np.round(rng.normal(0, 0.3, K), 6).tolist(), "effets": effets, "distracteurs": [4, 5, 6, 7]}
    Zg, Gg = M.tirer_instances(np.random.default_rng(np.random.SeedSequence(RACINE_CTRL, spawn_key=(9, 2))), 8000, D, nsp)
    fac = {e["id"]: 1.0 for e in effets}

    def info(eid, f):  # même formule que `generer_monde_v4`
        f2 = dict(fac, **{eid: f})
        Q = M.probas(M.compiler_monde(spec, facteurs=f2), Zg, Gg)
        Qm = M.probas(M.compiler_monde(spec, sans=(eid,), facteurs=f2), Zg, Gg)
        return float((Q * (np.log(np.maximum(Q, M.PLANCHER)) - np.log(np.maximum(Qm, M.PLANCHER)))).sum(axis=1).mean())

    for _ in range(3):
        for e in effets:
            lo, hi = 0.0, 12.0
            for _ in range(28):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if info(e["id"], mid) < cibles[e["id"]] else (lo, mid)
            fac[e["id"]] = 0.5 * (lo + hi)
    for e in effets:
        for c in ("pente", "decalage"):
            if c in e:
                e[c] = np.round(np.asarray(e[c]) * fac[e["id"]], 6).tolist()
    return spec


def courir_monde(spec, r, info, avec_v1=True):
    oc = B.OracleCache(spec, r)
    don = B.donnees_servies(spec, r)
    out = {"info": dict(info, eid_k1=oc.eid_k1),
           "information_par_composante": {k: round(v, 5) for k, v in oc.infos.items()}}
    if avec_v1:
        b3, tr3 = B.base_glouton(spec, r, oc, don)
        out["v1"] = B.mesurer(b3, oc, info)
        out["v1"]["par_composante"] = {i: (i in out["v1"]["couvertes"]) for i in info["classes"] if i != oc.eid_k1}
        out["trajet_v1"] = tr3
    br, trr = base_glouton_renforcee(spec, oc, don)
    out["renforcee"] = mesurer_plus(br, oc, info, spec, don)
    out["trajet_renforcee"] = trr
    return out


def main(argv):
    if len(argv) < 2 or os.path.exists(argv[1]):
        print("usage : base_gloutonne_renforcee_v1.py SORTIE.json [MONDES…] (neuve)", file=sys.stderr)
        return 2
    mondes = [int(x) for x in argv[2:]] or list(range(12))
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    v1_scellee = json.load(open(V1_SORTIE, encoding="utf-8"))["par_monde"]
    par_monde = {}
    for r in mondes:
        spec, info = B.regenerer(r)
        res = courir_monde(spec, r, info)
        ref = v1_scellee[str(r)]["B3-glouton-borne"]
        res["v1_egale_sortie_scellee"] = (res["v1"]["couvertes"] == ref["couvertes"] and res["v1"]["vraies"] == ref["vraies"]
                                          and res["v1"]["formes_fausses_distinctes"] == ref["formes_fausses_distinctes"])
        par_monde[str(r)] = res
        print(r, "v1", res["v1"]["couverture"], len(res["v1"]["conditionnelles_couvertes"]), "renf", res["renforcee"]["couverture"],
              len(res["renforcee"]["conditionnelles_couvertes"]), "/", len(res["renforcee"]["conditionnelles"]),
              "egal_v1", res["v1_egale_sortie_scellee"], flush=True)
    controles = {}
    for nom, avec, r in (("CTRL-COND", True, 1000), ("CTRL-SANS", False, 1001)):
        spec = monde_controle(avec)
        info = {"partie_sha256": None, "certifiees": [e["id"] for e in spec["effets"]], "conditions": {},
                "classes": {e["id"]: e["classe"] for e in spec["effets"]}}
        res = courir_monde(spec, r, info)
        rr = res["renforcee"]
        if avec:
            res["attendu"] = "la base renforcée couvre E3 (conditionnelle)"
            res["tenu"] = "E3" in rr["conditionnelles_couvertes"]
        else:
            res["attendu"] = "aucune condition inventée vraie ; aucune conditionnelle couverte"
            res["tenu"] = rr["conditions_inventees_vraies"] == 0 and not rr["conditionnelles_couvertes"]
        res["spec"] = spec
        controles[nom] = res
        print(nom, "tenu", res["tenu"], "v1 cond", res["v1"]["conditionnelles_couvertes"], "renf cond",
              rr["conditionnelles_couvertes"], "inventees", rr["conditions_inventees_vraies"], flush=True)

    def resumer(cle):
        cv = [par_monde[k][cle]["couverture"] for k in par_monde]
        ff = [par_monde[k][cle]["formes_fausses_distinctes"] for k in par_monde]
        cc = sum(len(par_monde[k][cle]["conditionnelles_couvertes"]) for k in par_monde)
        nc = sum(len(par_monde[k][cle]["conditionnelles"]) for k in par_monde)
        ord_c = sum(len(set(par_monde[k][cle]["couvertes"]) - set(par_monde[k][cle]["conditionnelles"])) for k in par_monde)
        ord_n = sum(par_monde[k][cle]["composantes_hors_K1"] - len(par_monde[k][cle]["conditionnelles"]) for k in par_monde)
        return {"couverture_mediane": float(np.median(cv)), "couverture_moyenne": round(float(np.mean(cv)), 4),
                "couverture_min_max": [min(cv), max(cv)], "conditionnelles_couvertes_sur": [cc, nc],
                "ordinaires_couvertes_sur": [ord_c, ord_n], "formes_fausses_distinctes_mediane": float(np.median(ff)),
                "vraies_sur_cartes": [sum(par_monde[k][cle]["vraies"] for k in par_monde), sum(par_monde[k][cle]["cartes"] for k in par_monde)]}

    resume = {"v1": resumer("v1"), "renforcee": resumer("renforcee"),
              "v1_egale_sortie_scellee": all(par_monde[k]["v1_egale_sortie_scellee"] for k in par_monde),
              "conditions_inventees_vraies_mondes_dev": sum(par_monde[k]["renforcee"]["conditions_inventees_vraies"] for k in par_monde),
              "controles_tenus": all(c["tenu"] for c in controles.values())}
    # discordances appariées composante par composante (conditionnelles)
    d01 = d10 = 0
    for k in par_monde:
        for i in par_monde[k]["renforcee"]["conditionnelles"]:
            a, b = i in par_monde[k]["v1"]["conditionnelles_couvertes"], i in par_monde[k]["renforcee"]["conditionnelles_couvertes"]
            d01 += (not a) and b
            d10 += a and not b
    resume["discordances_conditionnelles"] = {"renforcee_seule": d01, "v1_seule": d10}
    out = {"version": "base-gloutonne-renforcee-v1", "debut_utc": debut,
           "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "script_sha256": sha(os.path.abspath(__file__)), "v1_script_sha256": SHA_V1, "v1_sortie_sha256": SHA_V1_SORTIE,
           "imports_sha256": B.IMPORTS, "python": sys.version.split()[0], "numpy": np.__version__,
           "graines": {"donnees_servies": "celles de la v1 : SeedSequence(20261122, spawn_key=(0, monde))",
                       "mondes_et_oracle": "graines de la v4 (P1.cle), comme la v1",
                       "mondes_de_controle": "SeedSequence(20261122, spawn_key=(9, 1)) pour les directions et le biais, (9, 2) pour l'étalonnage ; oracle P1.cle('oracle-v4', 1000 | 1001) ; données servies spawn_key=(0, 1000 | 1001)",
                       "recherche": "déterministe"},
           "parametres": {"PAR_GENERATION": PAR_GENERATION, "SEUILS": SEUILS, "CANDIDATS_MAX": CANDIDATS_MAX,
                          "N_SERVIES": B.N_SERVIES, "SEUIL_ORACLE": M.SEUIL_ORACLE},
           "mondes": mondes, "resume": resume, "controles": controles, "par_monde": par_monde}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(resume, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
