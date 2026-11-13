"""Famille de mondes v4 (Q-13 (c), mot de Lazar R-2492) : composantes **conditionnelles** qui ne deviennent trouvables qu'une
fois une autre composante captée ; règle de garde ; simulations. N'écrase rien : importe les outils v1, v2, v3 (scellés).

Concepteur (Claude Opus 5.5), 13 novembre 2026. Aucun appel, aucun réseau. Un seul processus ; une partie = un monde.

**Composante conditionnelle** (sorte neuve `interaction_xor`, classe « conditionnelle », taille moyenne [0,04 ; 0,08]) :
ajoute + p·z_t aux scores quand z_B > 0, − p·z_t sinon, où z_B est le trait d'une composante **moyenne** du monde (la
« composante de condition ») et z_t un trait neuf. Comme z_B est symétrique, l'effet de z_t **en moyenne sur z_B est nul** : une
loi qui n'utilise pas le signe de z_B n'en tire presque rien ; il faut conditionner sur z_B, ce qui suppose d'avoir vu que z_B
compte. Compilée dans la grammaire existante : une principale (− p sur t) et une interaction de seuil (+ 2p sur t si z_B > 0).

**Modèle de proposeurs synthétiques** : celui de la v3b (probabilité de proposer une composante inconnue : forte 0,5, moyenne
0,25, latente 0,25, faible 0,1 ; garder un effet connu 0,9 ; σ = 0,15), plus **une règle déclarée** : une conditionnelle est
proposée avec la probabilité 0,25 si sa composante de condition est connue (dans l'archive), **0,02 sinon** (estimé). Variante
« sans masquage » (0,25 toujours) rapportée pour montrer la dépendance au modèle.

**Règle de garde** (écrite d'avance, R-2492) : pas de course si moins de la moitié des mondes de calibration gardent une
composante **certifiée** (C8 v2 : borne basse de Wilson ≥ 0,8 à 200 graines, latente exclue) encore **non captée** après une
génération 1 simulée.

Usage : `python3 -I -B monde_riche_v4.py partie RANG SORTIE.json` | `resume DOSSIER SORTIE.json`.
"""
import datetime, glob, hashlib, json, math, os, sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
for d in ("outils-v1", "outils-v2", "outils-v3"):
    p = os.path.join(os.path.dirname(ICI), d)
    if p not in sys.path:
        sys.path.insert(0, p)
import monde_riche_outils_v1 as M  # noqa: E402
import monde_riche_outils_v2 as M2  # noqa: E402
import verifier_monde_kimi_v1 as V1V  # noqa: E402
import verifier_monde_v2 as V2  # noqa: E402
import generateur_mondes_v2 as G2  # noqa: E402
import puissance_monde_riche_v2 as P2  # noqa: E402
import puissance_monde_riche_v3 as P3  # noqa: E402

P1 = P2.P1
M_REGLE = 48  # V-4 : 6 × 4 proposeurs + 12 vraies + 5 fausses + 4 copies + H1 + 2 instruments
P_CACHEE, P_VUE = 0.02, 0.25

# --- sorte neuve : interaction_xor (développée avant la compilation de la v1) ------------------------------------------------
_COMPILER, _CONDS, _TRAITS = M.compiler_monde, M._conditions, M.traits_d_un_effet


def _developper(effets, fac):
    out, fac2 = [], {}
    for e in effets:
        f = fac.get(e["id"], 1.0)
        if e["type"] == "interaction_xor":
            p = np.asarray(e["pente"], float)
            out.append({"id": e["id"] + "-a", "type": "principal", "trait": e["trait"], "pente": (-p).tolist()})
            out.append({"id": e["id"] + "-b", "type": "interaction_seuil", "trait_condition": e["trait_condition"],
                        "seuil": 0.0, "trait": e["trait"], "pente": (2 * p).tolist()})
            fac2[e["id"] + "-a"] = fac2[e["id"] + "-b"] = f
        else:
            out.append(e)
            fac2[e["id"]] = f
    return out, fac2


def compiler_v4(spec, sans=(), facteurs=None):
    sans = set(sans)
    eff, fac2 = _developper([e for e in spec["effets"] if e["id"] not in sans], facteurs or {})
    return _COMPILER(dict(spec, effets=eff), sans=(), facteurs=fac2)


def conditions_v4(effets):
    base = _CONDS([e for e in effets if e["type"] != "interaction_xor"])
    return sorted(set(base) | {(e["trait_condition"], 0.0) for e in effets if e["type"] == "interaction_xor"})


def traits_v4(e):
    return {e["trait"], e["trait_condition"]} if e["type"] == "interaction_xor" else _TRAITS(e)


M.compiler_monde, M._conditions, M.traits_d_un_effet = compiler_v4, conditions_v4, traits_v4
V1V.CLES_EFFET["interaction_xor"] = {"id", "classe", "type", "trait_condition", "trait", "pente", "composante_condition"}
CLASSES = dict(G2.CLASSES, conditionnelle=(0.04, 0.08))
EXIGENCES_V4 = dict(V2.EXIGENCES_V2, version="exigences-monde-riche-v4",
                    classes=dict(V2.EXIGENCES_V2["classes"], conditionnelle=[0.04, 0.08]),
                    effets_par_classe=dict(V2.EXIGENCES_V2["effets_par_classe"], conditionnelle=[1, 2]),
                    interactions_min=2, conditions_seuil_max=3, feuilles_max=48,
                    sensibilite=dict(V2.EXIGENCES_V2["sensibilite"], m=M_REGLE))


def tirer_gabarit_v4(rng):
    while True:
        g, latent = G2.tirer_gabarit_v2(rng)
        n_xor = int(rng.integers(1, 3))
        utilisant = sum(1 for _, s in g if s != "sous_population") + n_xor
        moy_trait = sum(1 for c, s in g if c == "moyenne" and s != "sous_population")
        total = len(g) + n_xor + int(latent)
        # ≥ 2 leurres ; une moyenne à trait pour porter la condition ; ≤ 10 composantes (≤ 9 « K1 + un effet » : devis inchangé)
        if utilisant <= 6 and moy_trait >= 1 and total <= 10:
            return g, latent, n_xor


def generer_monde_v4(graine, D=8, nsp=3, K=3, n_oracle=8000):
    rng = np.random.default_rng(np.random.SeedSequence(graine))
    while True:
        gabarit, latent, n_xor = tirer_gabarit_v4(rng)
        traits = [int(t) for t in rng.permutation(D)]
        effets, cibles = [], {}
        for i, (classe, ty) in enumerate(gabarit):
            eid = f"E{i + 1}"
            lo, hi = CLASSES[classe]
            cibles[eid] = float(rng.uniform(lo + 0.15 * (hi - lo), hi - 0.15 * (hi - lo)))
            e = {"id": eid, "classe": classe, "type": ty}
            if ty in ("principal", "seuil", "interaction_seuil", "interaction_sous_population"):
                e["trait"] = traits.pop(0)
            if ty == "principal":
                e["pente"] = G2._dir(rng, K).tolist()
            elif ty == "seuil":
                e.update(seuil=round(float(rng.uniform(-1.0, 1.2)), 6), decalage=G2._dir(rng, K).tolist())
            elif ty == "interaction_seuil":
                e.update(seuil=round(float(rng.uniform(-0.5, 0.5)), 6), pente=G2._dir(rng, K).tolist())
            elif ty == "interaction_sous_population":
                e.update(sous_population=int(rng.integers(0, nsp)), pente=G2._dir(rng, K).tolist())
            elif ty == "sous_population":
                e.update(sous_population=int(rng.integers(0, nsp)), decalage=G2._dir(rng, K).tolist())
            effets.append(e)
        for e in effets:
            if e["type"] == "interaction_seuil":
                autres = sorted({x["trait"] for x in effets if "trait" in x and x is not e})
                e["trait_condition"] = int(rng.choice(autres))
        moyennes = [e for e in effets if e["classe"] == "moyenne" and "trait" in e]
        for k in range(n_xor):
            eid = f"E{len(effets) + 1}"
            lo, hi = CLASSES["conditionnelle"]
            cibles[eid] = float(rng.uniform(lo + 0.15 * (hi - lo), hi - 0.15 * (hi - lo)))
            # la première conditionnelle dépend d'une moyenne ; la seconde, s'il y en a deux, de la première (profondeur 2)
            cond = moyennes[int(rng.integers(0, len(moyennes)))] if k == 0 else effets[-1]
            effets.append({"id": eid, "classe": "conditionnelle", "type": "interaction_xor", "trait": traits.pop(0),
                           "trait_condition": cond["trait"], "composante_condition": cond["id"], "pente": G2._dir(rng, K).tolist()})
        if len(conditions_v4(effets)) <= 3:
            break
    if latent:
        eid = f"E{len(effets) + 1}"
        lo, hi = CLASSES["latente"]
        cibles[eid] = float(rng.uniform(lo, hi))
        effets.append({"id": eid, "classe": "latente", "type": "latent",
                       "poids_melange": round(float(rng.uniform(0.3, 0.7)), 6), "decalage": G2._dir(rng, K).tolist()})
    utilises = set()
    for x in effets:
        utilises |= {t for t in traits_v4(x) if isinstance(t, int)} if x["type"] not in ("latent", "sous_population") else set()
    spec = {"version": "monde-riche-spec-v1", "nombre_issues": K, "dimension": D, "sous_populations": nsp,
            "biais": np.round(rng.normal(0, 0.3, K), 6).tolist(), "effets": effets,
            "distracteurs": sorted(t for t in range(D) if t not in utilises)}
    Zg, Gg = M.tirer_instances(np.random.default_rng(np.random.SeedSequence([graine, 7])), n_oracle, D, nsp)
    fac = {e["id"]: 1.0 for e in effets}

    def info(eid, f):
        f2 = dict(fac, **{eid: f})
        Q = M.probas(compiler_v4(spec, facteurs=f2), Zg, Gg)
        Qm = M.probas(compiler_v4(spec, sans=(eid,), facteurs=f2), Zg, Gg)
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


def verifier_v4(spec):
    r = V2.verifier_v2(spec, EXIGENCES_V4)
    if r["conforme"]:
        for k, v in r["sensibilite"].items():
            if v["classe"] == "conditionnelle" and not v["etiquette"].startswith("certifiée"):
                r["conforme"] = False
                r["refus"] = {"controle": "C8", "motif": f"{k} (conditionnelle) non certifiée"}
                break
    return r


def generer_v4(graine, essais_max=8):
    refus = []
    for k in range(essais_max):
        sous = int(np.random.SeedSequence(graine, spawn_key=(k,)).generate_state(1, dtype=np.uint64)[0])
        spec = generer_monde_v4(sous)
        r = verifier_v4(spec)
        if r["conforme"]:
            return spec, r, refus
        refus.append(r["refus"]["controle"])
    return None, None, refus


# --- course simulée (code v3b sinon : juge simplifié, regroupement stratifié, représentant à tranche appariée) ---------------

def course(spec, w, G_, masquage, n=400, m=M_REGLE):
    loi = M.compiler_monde(spec)
    D, nsp = spec["dimension"], spec["sous_populations"]
    o = M.Oracle(loi, D, nsp, n=12000, graine=P1.cle("oracle-v4", w))
    k1, eid_k1, infos = M.k1_du_monde(spec, o)
    classe = {e["id"]: e["classe"] for e in spec["effets"]}
    cond = {e["id"]: e.get("composante_condition") for e in spec["effets"]}
    ids = [e["id"] for e in spec["effets"]]
    Zref, Gref = M.tirer_instances(P1.rng_de("v4-ref", w), 1500, D, nsp)
    archive, connus = [k1], {eid_k1}
    captes = set(M.captes(o.attribution(k1, spec), infos))
    seuil = math.log(m / M.ALPHA)
    rng = P1.rng_de("v4-gen", w, masquage)
    hist = []
    for g in range(1, G_ + 1):
        cartes, Sc = [], []
        for _p in range(4):
            for _c in range(6):
                S = {i for i in sorted(connus) if rng.random() < 0.9}
                for i in ids:
                    if i in connus:
                        continue
                    if classe[i] == "conditionnelle":
                        p = P_VUE if (not masquage or cond[i] in connus) else P_CACHEE
                    else:
                        p = P2.PROBA_TROUVER[classe[i]]
                    if rng.random() < p:
                        S.add(i)
                S = sorted(S) or [eid_k1]
                cartes.append(P1._bruiter(spec, S, 0.15, rng))
                Sc.append(S)
        les = {i: M.log_e_arrete(M.juger(c, archive, loi, D, nsp, P1.rng_de("v4-juge", w, masquage, g, i), n=n)["traj"], seuil)
               for i, c in enumerate(cartes)}
        gs, (dg, ds, can) = M2.grouper_v2(cartes, Zref, Gref, nsp)
        les_g = {gi: M.log_e_groupe([les[i] for i in gg]) for gi, gg in enumerate(gs)}
        promus = sorted(gs[gi][0] if len(gs[gi]) == 1 else P3.representant_v3(gs[gi], cartes, dg, can, loi, D, nsp)[0]
                        for gi in M.e_bh(les_g, m))
        retenues = [i for i in promus if M.test_de_mort(cartes[i], loi, D, nsp, P1.rng_de("v4-mort", w, masquage, g, i))[1]]
        env = o.gain_enveloppe(archive)
        faux = sum(1 for i in retenues if o.gain(cartes[i]) - env < M.SEUIL_ORACLE)
        for i in retenues:
            archive.append(cartes[i])
            connus |= set(Sc[i])
            captes |= set(M.captes(o.attribution(cartes[i], spec), infos))
        hist.append({"generation": g, "promues": len(promus), "retenues": len(retenues), "archive": len(archive),
                     "captes": sorted(captes), "fausses_decouvertes": faux})
    return hist


def part_marginale(spec, eid, o, iterations=400, pas=1.0):
    """Mesure structurelle (sans modèle de proposeurs) : part de l'information I_i d'une composante qu'une correction **sans
    condition** sur son trait (logits de W₋ᵢ + β·z_t + γ, β et γ ajustés au maximum de vraisemblance attendue sous W) rend.
    Proche de 0 : le trait ne se trouve pas seul ; proche de 1 : il se trouve par un effet principal."""
    e = next(x for x in spec["effets"] if x["id"] == eid)
    if "trait" not in e:
        return None
    Q, Pm = o.Q, np.maximum(o.P(M.compiler_monde(spec, sans=(eid,))), M.PLANCHER)
    L0, z = np.log(Pm), o.Z[:, e["trait"]]
    X = np.stack([z, np.ones_like(z)], axis=1)
    th = np.zeros((2, Q.shape[1]))
    for _ in range(iterations):
        S = L0 + X @ th
        S -= S.max(axis=1, keepdims=True)
        P = np.exp(S)
        P /= P.sum(axis=1, keepdims=True)
        th += pas * X.T @ (Q - P) / len(Q)
    S = L0 + X @ th
    S -= S.max(axis=1, keepdims=True)
    P = np.maximum(np.exp(S) / np.exp(S).sum(axis=1, keepdims=True), M.PLANCHER)
    kl = lambda A: float((Q * (np.log(np.maximum(Q, M.PLANCHER)) - np.log(A))).sum(axis=1).mean())
    i_i = kl(Pm)
    return round((i_i - kl(P)) / i_i, 4) if i_i > 0 else None


def partie(r):
    spec, rap, refus = generer_v4(P1.cle("monde-mr1-v4-calibration-developpement", r))
    if spec is None:
        return {"monde": r, "conforme": False, "refus": refus}
    c8 = {k: {"classe": v["classe"], "puissance": v["puissance"], "wilson": v["wilson"], "certifiee": v["etiquette"].startswith("certifiée")}
          for k, v in rap["sensibilite"].items()}
    certifiees = sorted(k for k, v in c8.items() if v["certifiee"] and v["classe"] != "latente")
    o = M.Oracle(M.compiler_monde(spec), spec["dimension"], spec["sous_populations"], n=12000, graine=P1.cle("oracle-v4", r))
    marg = {e["id"]: part_marginale(spec, e["id"], o) for e in spec["effets"] if e["classe"] in ("moyenne", "conditionnelle")}
    avec = course(spec, r, 3, True)
    sans = course(spec, r, 1, False)

    def apres(h, g):
        return sorted(set(certifiees) - set(h[g - 1]["captes"]))
    return {"monde": r, "conforme": True, "refus": refus, "gabarit": [(e["classe"], e["type"]) for e in spec["effets"]],
            "c8": c8, "certifiees": certifiees, "part_marginale": marg,
            "conditions": {e["id"]: e["composante_condition"] for e in spec["effets"] if e["type"] == "interaction_xor"},
            "masquage": {"generations": avec, "certifiees_non_captees_apres_g1": apres(avec, 1),
                         "certifiees_neuves_g2": sorted(set(avec[1]["captes"]) - set(avec[0]["captes"]) & set(certifiees)),
                         "certifiees_neuves_g3": sorted(set(avec[2]["captes"]) - set(avec[1]["captes"]) & set(certifiees))},
            "sans_masquage_g1": {"generations": sans, "certifiees_non_captees_apres_g1": apres(sans, 1)}}


def resume(dossier):
    parts = [json.load(open(p))["resultat"] for p in sorted(glob.glob(os.path.join(dossier, "partie-v4-monde-*.json")))]
    ok = [p for p in parts if p["conforme"]]
    garde = sum(1 for p in ok if p["masquage"]["certifiees_non_captees_apres_g1"])
    garde_sans = sum(1 for p in ok if p["sans_masquage_g1"]["certifiees_non_captees_apres_g1"])
    progres = sum(1 for p in ok if p["masquage"]["certifiees_neuves_g2"] or p["masquage"]["certifiees_neuves_g3"])
    return {"mondes": len(parts), "conformes": len(ok), "refus": sum(len(p["refus"]) for p in parts),
            "refus_par_controle": {c: sum(p["refus"].count(c) for p in parts) for c in ("C0", "C1", "C2", "C3", "C4", "C5", "C6", "C8")},
            "regle_de_garde": {"mondes_gardant_une_certifiee_apres_g1": garde, "sur": len(ok),
                               "wilson": [round(x, 3) for x in V2.wilson(garde, len(ok))] if ok else None,
                               "tenue_au_moins_la_moitie": bool(ok) and garde * 2 >= len(ok)},
            "variante_sans_masquage": {"mondes_gardant_une_certifiee_apres_g1": garde_sans, "sur": len(ok),
                                       "tenue_au_moins_la_moitie": bool(ok) and garde_sans * 2 >= len(ok)},
            "progres_certifie_g2_ou_g3": {"mondes": progres, "sur": len(ok)},
            "retenues_par_generation": [round(float(np.mean([p["masquage"]["generations"][g]["retenues"] for p in ok])), 2) for g in range(3)] if ok else None,
            "fausses_sur_retenues": [int(sum(sum(h["fausses_decouvertes"] for h in p["masquage"]["generations"]) for p in ok)),
                                     int(sum(sum(h["retenues"] for h in p["masquage"]["generations"]) for p in ok))],
            "conditionnelles_certifiees": [sum(1 for v in p["c8"].values() if v["classe"] == "conditionnelle" and v["certifiee"]) for p in ok],
            "restantes_apres_g1_par_classe": {c: sum(1 for p in ok for k in p["masquage"]["certifiees_non_captees_apres_g1"] if p["c8"][k]["classe"] == c)
                                               for c in ("forte", "moyenne", "conditionnelle", "faible")},
            "part_marginale": {c: [v for p in ok for k, v in p["part_marginale"].items() if v is not None and p["c8"][k]["classe"] == c]
                               for c in ("moyenne", "conditionnelle")}}


if __name__ == "__main__":
    out = sys.argv[-1]
    if os.path.exists(out):
        sys.exit("refus : sortie existante")
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    res = partie(int(sys.argv[2])) if sys.argv[1] == "partie" else resume(sys.argv[2])
    with open(out, "x", encoding="utf-8") as f:
        json.dump({"version": "monde-riche-v4", "commande": sys.argv[1:-1], "debut_utc": debut,
                   "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "graine_de_hachage": "aléatoire (python -I) ; déterminisme par parcours triés",
                   "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "resultat": res}, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False)[:1500])
