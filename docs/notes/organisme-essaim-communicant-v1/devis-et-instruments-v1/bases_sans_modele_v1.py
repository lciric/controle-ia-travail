#!/usr/bin/env python3
"""Bases sans modèle (aucun appel) sur la famille MR-2 (conception du monde riche v4), même oracle sur toutes les cartes et
même compte de cartes que le bras (c) du cas attendu de la conception de l'essaim (52 cartes, trois générations) — v1.

Mondes : les 12 graines de développement de la v4 (`cle("monde-mr1-v4-calibration-developpement", r)`), régénérés par le code
scellé `outils-v4/monde_riche_v4.py` au tirage conforme rapporté par sa partie scellée (`sorties-v4/partie-v4-monde-r.json`,
champ `refus`), sans revérification C0 à C8 (déjà faite et scellée) ; contrôle : gabarit régénéré = gabarit de la partie.

Bases (aucune ne lit l'oracle, la loi du monde ni un verdict ; seules les données servies et l'archive de départ {K1}) :
- B1 « uniforme » : 52 lois tirées uniformément dans la grammaire servie (0 à 3 conditions de seuil sur un trait, seuil 0 une
  fois sur deux, sinon uniforme sur [−1 ; 1,2] ; par sous-population une fois sur deux ; feuilles softmax, chaque trait
  présent avec probabilité 1/2, pentes N(0 ; 1), biais N(0 ; 0,3²)) ; sans données, sans K1 ;
- B2 « K1 plus un effet tiré au hasard » : 52 lois K1 + un effet de la grammaire (sorte, traits, seuil, sous-population tirés
  uniformément ; paramètres ajustés sur les données servies) ;
- B3 « glouton borné » : recherche gloutonne en avant sur les données servies, trois générations (18, 17, 17 cartes) : à
  chaque génération, toutes les additions d'un effet à la loi courante (principal, seuil, interaction de seuil, sous-population,
  interaction de sous-population ; seuils dans {−0,5 ; 0 ; 0,5}) sont ajustées sur 3/4 des données servies et classées sur le
  quart restant ; les meilleures sont les cartes ; la meilleure devient la loi courante si elle gagne. Aucun juge.
Données servies : N_SERVIES instances (Z, G, Y) tirées du monde par graine dérivée (`SeedSequence(RACINE, spawn_key=(monde,))`),
hypothèse déclarée (la taille de la case de matière servie n'est fixée par aucune pièce lue).

Oracle (celui de `monde_riche_v4.course`) : instances `Oracle(…, n=12000, graine=cle("oracle-v4", r))` ; carte « vraie » si
gain au-delà de l'enveloppe du nul de {K1} ≥ 0,02, « fausse » sinon, « rien » si non évaluable ; composante « couverte » si
une carte au moins la capte (attribution Δ_i ≥ max(0,005 ; 0,75·I_i)). Couverture = composantes couvertes / composantes du
monde hors celle de K1. Garde = formes canoniques distinctes des cartes fausses.

Usage : python3 -I -B bases_sans_modele_v1.py SORTIE.json [MONDES…]   (refuse d'écraser)
"""
import datetime
import hashlib
import json
import os
import sys

import numpy as np

NOTES = "/home/user/controle-ia-travail/docs/notes/organisme-multi-generations-v1"
sys.path.insert(0, os.path.join(NOTES, "outils-v4"))
RACINE = 20261122
N_SERVIES = 2000
CARTES = 52
PAR_GENERATION = (18, 17, 17)
SEUILS = (-0.5, 0.0, 0.5)
BASES = ("B1-uniforme", "B2-K1-plus-un-effet-au-hasard", "B3-glouton-borne")


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def verifier(chemin):
    s, c = sha(chemin), open(chemin + ".sha256", encoding="utf-8").read().split()[0]
    if s != c:
        raise SystemExit(f"refus : {chemin} d'empreinte {s}, compagnon {c}")
    return s


IMPORTS = {}
for d, f in (("outils-v4", "monde_riche_v4.py"), ("outils-v1", "monde_riche_outils_v1.py"), ("outils-v1", "puissance_monde_riche_v1.py"),
             ("outils-v2", "monde_riche_outils_v2.py"), ("outils-v2", "verifier_monde_v2.py"), ("outils-v2", "generateur_mondes_v2.py"),
             ("outils-v2", "puissance_monde_riche_v2.py"), ("outils-v3", "puissance_monde_riche_v3.py"), ("outils-v1", "verifier_monde_kimi_v1.py")):
    IMPORTS[f"{d}/{f}"] = verifier(os.path.join(NOTES, d, f))
import monde_riche_v4 as V4  # noqa: E402  (applique les remplacements de la v4 à M)

M, P1 = V4.M, V4.P1


def rng_tache(*cle):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=tuple(int(x) for x in cle)))


# ---------------------------------------------------------------------------------------------------------------------------
def regenerer(r):
    partie = os.path.join(NOTES, "sorties-v4", f"partie-v4-monde-{r}.json")
    sp = verifier(partie)
    res = json.load(open(partie, encoding="utf-8"))["resultat"]
    graine = P1.cle("monde-mr1-v4-calibration-developpement", r)
    k = len(res["refus"])
    sous = int(np.random.SeedSequence(graine, spawn_key=(k,)).generate_state(1, dtype=np.uint64)[0])
    spec = V4.generer_monde_v4(sous)
    gab = [[e["classe"], e["type"]] for e in spec["effets"]]
    if gab != res["gabarit"]:
        raise SystemExit(f"refus : monde {r} régénéré ne rend pas le gabarit scellé")
    return spec, {"partie_sha256": sp, "certifiees": res["certifiees"], "conditions": res["conditions"],
                  "classes": {e["id"]: e["classe"] for e in spec["effets"]}}


class OracleCache:
    """Attribution de `M.Oracle.attribution`, mondes W₋ᵢ précalculés (même formule) ; enveloppe de {K1} calculée une fois."""

    def __init__(self, spec, r):
        self.spec = spec
        self.o = M.Oracle(M.compiler_monde(spec), spec["dimension"], spec["sous_populations"], n=12000, graine=P1.cle("oracle-v4", r))
        self.k1, self.eid_k1, self.infos = M.k1_du_monde(spec, self.o)
        self.env = self.o.gain_enveloppe([self.k1])
        self.Qm = {e["id"]: M.probas(M.compiler_monde(spec, sans=(e["id"],)), self.o.Z, self.o.G) for e in spec["effets"]}

    def attribution(self, loi):
        P = np.log(np.maximum(self.o.P(loi), M.PLANCHER))
        g = float((self.o.Q * (P - np.log(self.o.marg))).sum(axis=1).mean())
        return {i: g - float((Qm * (P - np.log(Qm.mean(axis=0)))).sum(axis=1).mean()) for i, Qm in self.Qm.items()}, g

    def juger_carte(self, loi):
        try:
            attr, g = self.attribution(loi)
            if not np.isfinite(g):
                raise ValueError("gain non fini")
        except Exception as ex:  # noqa: BLE001
            return {"classe": "rien", "motif": f"{type(ex).__name__}"}
        au_dela = g - self.env
        return {"classe": "vraie" if au_dela >= M.SEUIL_ORACLE else "fausse", "gain_au_dela_enveloppe": round(au_dela, 6),
                "captes": M.captes(attr, self.infos), "forme": M.empreinte(M.forme_canonique(loi))[:16]}


# ---------------------------------------------------------------------------------------------------------------------------
def donnees_servies(spec, r):
    rng = rng_tache(0, r)
    Z, G = M.tirer_instances(rng, N_SERVIES, spec["dimension"], spec["sous_populations"])
    Y = M.tirer_issues(rng, M.probas(M.compiler_monde(spec), Z, G))
    return Z, G, Y


def caracteristique(e, Z, G):
    t = e["type"]
    if t == "principal":
        return Z[:, e["trait"]]
    if t == "seuil":
        return (Z[:, e["trait"]] > e["seuil"]).astype(float)
    if t == "interaction_seuil":
        return (Z[:, e["trait_condition"]] > e["seuil"]) * Z[:, e["trait"]]
    if t == "sous_population":
        return (G == e["sous_population"]).astype(float)
    if t == "interaction_sous_population":
        return (G == e["sous_population"]) * Z[:, e["trait"]]
    raise ValueError(t)


def ajuster(effets, Z, G, Y, K, iterations=300, l2=1e-3):
    """Régression softmax sur les caractéristiques des effets (issue 0 de référence) ; rend (biais, pentes par effet)."""
    X = np.column_stack([np.ones(len(Y))] + [caracteristique(e, Z, G) for e in effets])
    Yh = np.eye(K)[Y]
    th = np.zeros((X.shape[1], K))
    pas = 1.0
    for _ in range(iterations):
        S = X @ th
        S -= S.max(axis=1, keepdims=True)
        P = np.exp(S)
        P /= P.sum(axis=1, keepdims=True)
        gr = X.T @ (Yh - P) / len(Y) - l2 * th
        gr[:, 0] = 0.0
        th += pas * gr
    return th


def loi_de(effets, th, spec):
    s = {"version": "monde-riche-spec-v1", "nombre_issues": spec["nombre_issues"], "dimension": spec["dimension"],
         "sous_populations": spec["sous_populations"], "biais": np.round(th[0], 6).tolist(), "effets": []}
    for i, e in enumerate(effets):
        e2 = dict(e, id=f"C{i}")
        cle = "decalage" if e["type"] in ("seuil", "sous_population") else "pente"
        e2[cle] = np.round(th[i + 1], 6).tolist()
        s["effets"].append(e2)
    return M.compiler_monde(s)


def logvrais(effets, th, Z, G, Y):
    X = np.column_stack([np.ones(len(Y))] + [caracteristique(e, Z, G) for e in effets])
    S = X @ th
    S -= S.max(axis=1, keepdims=True)
    return float((S[np.arange(len(Y)), Y] - np.log(np.exp(S).sum(axis=1))).mean())


def effets_k1(oc):
    e = next(x for x in oc.spec["effets"] if x["id"] == oc.eid_k1)
    return [{"type": "principal", "trait": e["trait"]}]


def candidats(courant, D, nsp):
    out = []
    for j in range(D):
        out.append({"type": "principal", "trait": j})
        for s in SEUILS:
            out.append({"type": "seuil", "trait": j, "seuil": s})
            for c in range(D):
                if c != j:
                    out.append({"type": "interaction_seuil", "trait_condition": c, "seuil": s, "trait": j})
        for g in range(nsp):
            out.append({"type": "interaction_sous_population", "sous_population": g, "trait": j})
    for g in range(nsp):
        out.append({"type": "sous_population", "sous_population": g})
    deja = {json.dumps(e, sort_keys=True) for e in courant}
    out = [e for e in out if json.dumps(e, sort_keys=True) not in deja]
    conds = lambda ef: {(x.get("trait_condition", x.get("trait")), x["seuil"]) for x in ef if x["type"] in ("seuil", "interaction_seuil")}
    return [e for e in out if len(conds(courant + [e])) <= 3]


def base_uniforme(spec, r):
    rng = rng_tache(1, r)
    D, nsp, K = spec["dimension"], spec["sous_populations"], spec["nombre_issues"]
    cartes = []
    for _ in range(CARTES):
        nc = int(rng.integers(0, 4))
        conds = [(int(rng.integers(0, D)), 0.0 if rng.random() < 0.5 else round(float(rng.uniform(-1.0, 1.2)), 6)) for _ in range(nc)]

        def feuille():
            W = np.zeros((K, D))
            for j in range(D):
                if rng.random() < 0.5:
                    W[:, j] = rng.normal(0, 1.0, K)
            return {"type": "softmax", "poids": np.round(W, 6).tolist(), "biais": np.round(rng.normal(0, 0.3, K), 6).tolist()}

        def arbre(i):
            if i == len(conds):
                return feuille()
            return {"type": "si_sinon", "condition": {"indice": conds[i][0], "seuil": conds[i][1]}, "si": arbre(i + 1), "sinon": arbre(i + 1)}
        loi = {"type": "par_sous_population", "lois": {str(g): arbre(0) for g in range(nsp)}} if rng.random() < 0.5 else arbre(0)
        cartes.append({"generation": 1 + min(2, len(cartes) * 3 // CARTES), "loi": loi})
    return cartes


def base_k1_plus_hasard(spec, r, oc, donnees):
    rng = rng_tache(2, r)
    Z, G, Y = donnees
    base = effets_k1(oc)
    cands = candidats(base, spec["dimension"], spec["sous_populations"])
    cartes = []
    for idx in rng.choice(len(cands), size=CARTES, replace=False):
        ef = base + [cands[int(idx)]]
        cartes.append({"generation": 1 + min(2, len(cartes) * 3 // CARTES), "loi": loi_de(ef, ajuster(ef, Z, G, Y, spec["nombre_issues"]), spec),
                       "effet_ajoute": cands[int(idx)]})
    return cartes


def base_glouton(spec, r, oc, donnees):
    Z, G, Y = donnees
    n = len(Y)
    a = int(0.75 * n)
    K = spec["nombre_issues"]
    courant = effets_k1(oc)
    cartes, trajet = [], []
    for g, nb in enumerate(PAR_GENERATION, start=1):
        th0 = ajuster(courant, Z[:a], G[:a], Y[:a], K)
        v0 = logvrais(courant, th0, Z[a:], G[a:], Y[a:])
        notes = []
        for e in candidats(courant, spec["dimension"], spec["sous_populations"]):
            ef = courant + [e]
            th = ajuster(ef, Z[:a], G[:a], Y[:a], K, iterations=150)
            notes.append((logvrais(ef, th, Z[a:], G[a:], Y[a:]) - v0, json.dumps(e, sort_keys=True), e))
        notes.sort(key=lambda x: (-x[0], x[1]))
        for gain, _, e in notes[:nb]:
            ef = courant + [e]
            cartes.append({"generation": g, "loi": loi_de(ef, ajuster(ef, Z, G, Y, K), spec), "effet_ajoute": e,
                           "gain_validation": round(gain, 6)})
        trajet.append({"generation": g, "candidats": len(notes), "meilleur": notes[0][2], "gain": round(notes[0][0], 6)})
        if notes[0][0] > 0:
            courant = courant + [notes[0][2]]
    return cartes, trajet


def mesurer(cartes, oc, info):
    jug = [dict(oc.juger_carte(c["loi"]), generation=c["generation"]) for c in cartes]
    hors_k1 = [i for i in info["classes"] if i != oc.eid_k1]
    # v1, après l'essai sur le monde 1 (écart déclaré) : une composante n'est couverte que par une carte « vraie » ;
    # l'attribution seule donne des Δ_i grands pour des lois absurdes (couverture brute rapportée à côté).
    couv = sorted({i for j in jug if j["classe"] == "vraie" for i in j.get("captes", [])} & set(hors_k1))
    couv_brute = sorted({i for j in jug if j["classe"] != "rien" for i in j.get("captes", [])} & set(hors_k1))
    par_g = []
    for g in (1, 2, 3):
        cum = sorted({i for j in jug if j["generation"] <= g and j["classe"] == "vraie" for i in j.get("captes", [])} & set(hors_k1))
        par_g.append(round(len(cum) / len(hors_k1), 4))
    cond = [i for i in hors_k1 if info["classes"][i] == "conditionnelle"]
    cert = [i for i in info["certifiees"] if i != oc.eid_k1]
    return {"cartes": len(jug), "vraies": sum(j["classe"] == "vraie" for j in jug), "fausses": sum(j["classe"] == "fausse" for j in jug),
            "rien": sum(j["classe"] == "rien" for j in jug),
            "formes_fausses_distinctes": len({j["forme"] for j in jug if j["classe"] == "fausse"}),
            "composantes_hors_K1": len(hors_k1), "couvertes": couv, "couverture": round(len(couv) / len(hors_k1), 4),
            "couverture_brute_attribution_seule": round(len(couv_brute) / len(hors_k1), 4),
            "couverture_cumulee_par_generation": par_g,
            "couverture_certifiees": round(len(set(couv) & set(cert)) / len(cert), 4) if cert else None,
            "conditionnelles": cond, "conditionnelles_couvertes": sorted(set(couv) & set(cond))}


def controles(oc, spec, info):
    """Objets de contrôle : la loi du monde (vraie, capte toute composante certifiée non latente) ; K1 (fausse) ; attribution
    du cache égale à celle de `M.Oracle.attribution` sur la loi du monde. (v1, après l'essai sur le monde 1, écart déclaré :
    l'attendu « toutes les non latentes » échouait sur une faible non certifiée sous le plancher 0,005.)"""
    w = M.compiler_monde(spec)
    jm, jk = oc.juger_carte(w), oc.juger_carte(oc.k1)
    a_ref = oc.o.attribution(w, spec)
    a_cache, _ = oc.attribution(w)
    ecart = max(abs(a_ref[i] - a_cache[i]) for i in a_ref)
    cert = sorted(i for i in info["certifiees"] if info["classes"][i] != "latente")
    return {"loi_du_monde": {"classe": jm["classe"], "captes": jm["captes"], "attendu_vraie_et_toutes_non_latentes": jm["classe"] == "vraie" and set(cert) <= set(jm["captes"])},
            "K1": {"classe": jk["classe"], "captes": jk["captes"], "attendu_fausse": jk["classe"] == "fausse"},
            "ecart_max_attribution_cache_contre_reference": ecart, "attribution_identique": ecart < 1e-9}


def main(argv):
    if len(argv) < 2 or os.path.exists(argv[1]):
        print("usage : bases_sans_modele_v1.py SORTIE.json [MONDES…] (neuve)", file=sys.stderr)
        return 2
    mondes = [int(x) for x in argv[2:]] or list(range(12))
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    par_monde = {}
    for r in mondes:
        spec, info = regenerer(r)
        oc = OracleCache(spec, r)
        don = donnees_servies(spec, r)
        b1 = base_uniforme(spec, r)
        b2 = base_k1_plus_hasard(spec, r, oc, don)
        b3, trajet = base_glouton(spec, r, oc, don)
        par_monde[str(r)] = {"info": dict(info, eid_k1=oc.eid_k1), "controles": controles(oc, spec, info),
                             BASES[0]: mesurer(b1, oc, info), BASES[1]: mesurer(b2, oc, info), BASES[2]: mesurer(b3, oc, info),
                             "trajet_glouton": trajet}
        print(r, {b: (par_monde[str(r)][b]["couverture"], par_monde[str(r)][b]["formes_fausses_distinctes"]) for b in BASES},
              par_monde[str(r)]["controles"]["attribution_identique"], flush=True)
    resume = {}
    for b in BASES:
        cv = [par_monde[k][b]["couverture"] for k in par_monde]
        ff = [par_monde[k][b]["formes_fausses_distinctes"] for k in par_monde]
        cc = [len(par_monde[k][b]["conditionnelles_couvertes"]) for k in par_monde]
        nc = [len(par_monde[k][b]["conditionnelles"]) for k in par_monde]
        resume[b] = {"couverture_mediane": float(np.median(cv)), "couverture_moyenne": round(float(np.mean(cv)), 4),
                     "couverture_min_max": [min(cv), max(cv)], "formes_fausses_distinctes_mediane": float(np.median(ff)),
                     "couverture_brute_mediane": float(np.median([par_monde[k][b]["couverture_brute_attribution_seule"] for k in par_monde])),
                     "couverture_certifiees_mediane": float(np.median([par_monde[k][b]["couverture_certifiees"] for k in par_monde])),
                     "conditionnelles_couvertes_sur": [int(sum(cc)), int(sum(nc))],
                     "vraies_sur_cartes": [int(sum(par_monde[k][b]["vraies"] for k in par_monde)), int(sum(par_monde[k][b]["cartes"] for k in par_monde))]}
    ctrl_ok = all(par_monde[k]["controles"]["loi_du_monde"]["attendu_vraie_et_toutes_non_latentes"] and par_monde[k]["controles"]["K1"]["attendu_fausse"]
                  and par_monde[k]["controles"]["attribution_identique"] for k in par_monde)
    out = {"version": "bases-sans-modele-v1", "debut_utc": debut,
           "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "script_sha256": sha(os.path.abspath(__file__)), "imports_sha256": IMPORTS,
           "graines": {"racine": RACINE, "regle": "SeedSequence(RACINE, spawn_key=(tache, monde)) ; tache 0 données servies, 1 B1, 2 B2 ; B3 déterministe ; mondes et oracle : graines de la v4 (P1.cle)"},
           "python": sys.version.split()[0], "numpy": np.__version__,
           "parametres": {"N_SERVIES": N_SERVIES, "CARTES": CARTES, "PAR_GENERATION": PAR_GENERATION, "SEUILS": SEUILS},
           "mondes": mondes, "controles_tenus": ctrl_ok, "resume": resume, "par_monde": par_monde}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({"controles_tenus": ctrl_ok, "resume": resume}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
