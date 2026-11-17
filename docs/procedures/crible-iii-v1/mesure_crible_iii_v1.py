"""Mesure du crible (iii) — v1 (`mesure_crible_iii_v1.py`, nom réservé par la pièce qui fera foi, section « Métrique » ; dérivée
de `mesure_pilote_v4.py`, `676d5f37…`, qui n'est pas modifiée). Lancée une seule fois, sur la machine du crible ; sortie scellée
avant toute lecture ; aucun appel ; lit les mondes privés ; n'écrit aucun coefficient de monde.

Définitions (recopiées de la pièce) :
- appel complet, tronqué, en échec (raison d'arrêt du relevé) ; **carte valide** = admise au gardien, évaluable, emplacement ≤ 6,
  d'un appel complet ; **appel répondu** = complet avec au moins une carte valide ;
- **composantes comptées** : certifiées (étiquette C8 de `verifier_v4`, latente exclue), moins l'effet de K1 et ce que K1 servie
  porte à elle seule ; une carte porte la composante i si Δ_i ≥ max(0,005 ; 0,75·I_i) (oracle de 12 000 instances, graine
  `cle("oracle-crible-iii", empreinte du devis du monde)`) ; C_X(w) = composantes comptées portées par au moins une carte valide
  du bras X ;
- **dollars** : $_S = appel S ; $_D = passe 1 + passe 2 de D ; $_H = passe 2 de H ; $_B = passe 1 + passe 2 de B ;
- **monde complet** : S, D (passe 1 avec au moins un ensemble après filtre, et passe 2), H et B répondus ;
- R_X = Σ C_X / Σ $_X (mondes complets) ; Δ_R = R_D − R_S (P1) ; ρ_XY = R_X / R_Y ; δ_XY = moyenne de C_X(w) − C_Y(w) ;
- intervalles : rééchantillonnage apparié des mondes complets, 10 000 rééchantillons (graines `(99, b)`), percentile ; 97,5 %
  pour P1 et P2, 95 % ailleurs ; test exact des signes rapporté pour chaque δ.
- exécution E_X, E′_X (D, H, B) ; bruit N_X ; qualité du choix de la passe 1 ; conditionnelle ; sensibilités (τ′ = 0,25·I ; toutes
  les composantes ; prix de la configuration, égaux aux prix publics : vide ; mondes non complets réintégrés bras par bras) ;
  rapport réintégré de δ_DB (étage 2 de la lecture).

Usages :
  python3 -I -B mesure_crible_iii_v1.py mesurer --arbre ORCHESTRATEUR --mondes MONDES.json --mondes-sha256 H --sortie DOSSIER
          --texte-sha256 EMPREINTE    (une seule fois ; écrit DOSSIER/mesure-crible-iii-v1.json et son compagnon)
Codes : 0 mesure écrite ; 2 refus nommé (entrées) ; 3 défaut (artefact dans les entrées : rien n'est écrit) ; 1 exception
(rien n'est écrit, rien n'est lu ; correction sous un nom neuf).
"""
from __future__ import annotations

import datetime
import hashlib
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import crible_iii_v1 as N  # noqa: E402

VERSION = "mesure-crible-iii-v1"
EMPLACEMENTS = 6
REECHANTILLONS = 10000
NIVEAU_PRINCIPAL = 0.975     # Bonferroni sur deux principales
NIVEAU_SECONDAIRE = 0.95
BRAS_ECRITURE = ("S", "D", "H", "B")
PAIRES = {"DS": ("D", "S"), "DB": ("D", "B"), "DH": ("D", "H"), "HS": ("H", "S"), "BD": ("B", "D"), "BS": ("B", "S")}
SORTIE = "mesure-crible-iii-v1.json"


class Refus(Exception):
    pass


class Defaut(Exception):
    pass


# --- outils MR-2 de l'arbre (oracle, K1, C8) ------------------------------------------------------------------------------------

class OutilsMR2:
    """Monde préparé par la mesure elle-même : la K1 servie est celle que la mesure retire (R-4 du pilote)."""

    def __init__(self, arbre):
        self.racine = arbre
        if arbre not in sys.path:
            sys.path.insert(0, arbre)
        from pole import pilote_mr2_v70 as P  # noqa: E402
        self.P = P
        self.V4, self.M, _ = P.charger_mr2()
        self.cache = {}

    def sha(self, spec):
        return hashlib.sha256(self.M.json_canonique(spec)).hexdigest()

    def oracle_et_k1(self, w):
        """(spec, sha, oracle, k1, eid_k1, infos) d'un monde {monde, spec, spec_sha256} ; refus si l'empreinte diffère."""
        spec, sha = w["spec"], self.sha(w["spec"])
        if sha != w["spec_sha256"]:
            raise Refus(f"monde {w['monde']} : empreinte du devis différente")
        cle = ("o", sha)
        if cle not in self.cache:
            o = self.M.Oracle(self.M.compiler_monde(spec), spec["dimension"], spec["sous_populations"], n=12000,
                              graine=self.V4.P1.cle("oracle-crible-iii", sha))
            k1, eid_k1, infos = self.M.k1_du_monde(spec, o)
            self.cache[cle] = (o, k1, eid_k1, infos)
        o, k1, eid_k1, infos = self.cache[cle]
        return spec, sha, o, k1, eid_k1, infos

    def evaluable(self, loi, o):
        try:
            p = self.M.probas(loi, o.Z[:64], o.G[:64])
        except (KeyError, ValueError, TypeError, IndexError, AttributeError, RecursionError):
            return False
        return bool(np.all(np.isfinite(p)) and p.shape == (64, 3) and np.allclose(p.sum(axis=1), 1.0))

    def porte(self, pm, loi):
        """(composantes portées à τ, à τ′) ; None si la loi n'est pas évaluable."""
        cle = ("c", pm["sha"], hashlib.sha256(self.M.json_canonique(loi)).hexdigest())
        if cle not in self.cache:
            if not self.evaluable(loi, pm["o"]):
                self.cache[cle] = None
            else:
                att = pm["o"].attribution(loi, pm["spec"])
                self.cache[cle] = ({i for i, d in att.items() if d >= max(0.005, 0.75 * pm["infos"][i])},
                                   {i for i, d in att.items() if d >= max(0.005, 0.25 * pm["infos"][i])})
        return self.cache[cle]

    def etiquettes_c8(self, spec, sha):
        """Composantes certifiées (étiquette C8 de `verifier_v4`, latente exclue), une fois par devis."""
        if ("c8", sha) not in self.cache:
            self.cache[("c8", sha)] = _c8((self.racine, spec))
        return self.cache[("c8", sha)]

    def precalculer_c8(self, mondes, processus=4):
        """`verifier_v4` sur chaque devis distinct, en parallèle (résultat identique : fonction pure du devis)."""
        import multiprocessing
        a_faire = {}
        for w in mondes:
            sha = self.sha(w["spec"])
            if ("c8", sha) not in self.cache:
                a_faire[sha] = w["spec"]
        if not a_faire:
            return
        with multiprocessing.get_context("spawn").Pool(min(processus, len(a_faire))) as pool:
            res = pool.map(_c8, [(self.racine, s) for s in a_faire.values()])
        for sha, c in zip(a_faire, res):
            self.cache[("c8", sha)] = c

    def preparer(self, w):
        spec, sha, o, k1, eid_k1, infos = self.oracle_et_k1(w)
        certifiees = set(self.etiquettes_c8(spec, sha))
        classe = {e["id"]: e["classe"] for e in spec["effets"]}
        pm = {"monde": w["monde"], "spec": spec, "sha": sha, "o": o, "k1": k1, "eid_k1": eid_k1, "infos": infos}
        k1_tau, k1_tau2 = self.porte(pm, k1)
        tous = {e["id"] for e in spec["effets"] if e["classe"] != "latente"}
        cond = {e["id"]: e["composante_condition"] for e in spec["effets"] if e["type"] == "interaction_xor"}
        premiere = sorted(c for c, b in cond.items() if b not in cond)
        pm.update(comptees=sorted(certifiees - {eid_k1} - k1_tau), comptees_tau2=sorted(certifiees - {eid_k1} - k1_tau2),
                  comptees_toutes=sorted(tous - {eid_k1} - k1_tau), certifiees=sorted(certifiees),
                  premiere=premiere[0] if len(premiere) == 1 else None, distracteurs=sorted(spec.get("distracteurs", [])),
                  traits={e["id"]: sorted(t for t in self.V4.traits_v4(e) if isinstance(t, int))
                          for e in spec["effets"] if e["type"] not in ("latent", "sous_population")},
                  traits_k1=sorted(N.traits_employes(k1)))
        return pm


def _c8(args):
    arbre, spec = args
    if arbre not in sys.path:
        sys.path.insert(0, arbre)
    from pole import pilote_mr2_v70 as P  # noqa: E402
    V4, _, _ = P.charger_mr2()
    rap = P.sans_chemin_v52b(V4.verifier_v4, spec)
    sens = rap.get("sensibilite") or {}
    classe = {e["id"]: e["classe"] for e in spec["effets"]}
    return sorted(k for k, v in sens.items() if str(v.get("etiquette", "")).startswith("certifiée") and classe.get(k) != "latente")


# --- par monde --------------------------------------------------------------------------------------------------------------

def exiger_cartes(cartes):
    """Liste d'arrêt : une couverture qui compterait une carte refusée, au-delà de six, ou d'un appel non complet est un défaut ;
    le lanceur ne doit jamais marquer « admise » une carte au-delà de la sixième."""
    for c in cartes:
        if c.get("etat") not in ("admise", "refusee"):
            raise Defaut(f"carte d'état inconnu {c.get('etat')!r}")
        if c["etat"] == "admise" and not (isinstance(c.get("emplacement"), int) and 1 <= c["emplacement"] <= EMPLACEMENTS):
            raise Defaut(f"carte admise à l'emplacement {c.get('emplacement')!r} (au-delà de six) : défaut")


def cartes_valides(cartes, appel, outils, pm):
    """Cartes valides d'un bras dans un monde : appel complet, carte admise, emplacement ≤ 6, évaluable."""
    if appel is None or appel.get("etat") != "complet":
        return []
    out = []
    for c in cartes:
        if c["etat"] != "admise" or not (1 <= c["emplacement"] <= EMPLACEMENTS):
            continue
        p = outils.porte(pm, c["loi"])
        if p is not None:
            out.append(dict(c, porte=p))
    return out


def enregistrement(pm, appels, cartes, ens):
    """Le monde w réduit à ce que les statistiques lisent (aucun coefficient)."""
    a = {x["bras"]: x for x in appels}
    rec = {"monde": pm["monde"], "comptees": pm["comptees"], "bras": {}}
    cout = {b: float((a.get(b) or {}).get("cout_usd") or 0.0) for b in N.BRAS}
    dollars = {"S": cout["S"], "D": cout["P1"] + cout["D"], "H": cout["H"], "B": cout["P1"] + cout["B"]}
    ensembles = {"D": [tuple(x) for x in ens.get("d_retenus") or []], "B": [tuple(x) for x in ens.get("d_retenus") or []],
                 "H": [tuple(x) for x in ens.get("h_retenus") or []], "S": []}
    for b in BRAS_ECRITURE:
        cv = [c for c in cartes if c["bras"] == b]
        rec["bras"][b] = {"etat": (a.get(b) or {}).get("etat", "absent"), "cartes": cv, "dollars": dollars[b],
                          "ensembles": ensembles[b]}
    rec["p1"] = {"etat": (a.get("P1") or {}).get("etat", "absent"), "valides": [tuple(x) for x in ens.get("passe1_valides") or []],
                 "invalides": (ens.get("passe1") or {}).get("invalides", 0), "ignores": (ens.get("passe1") or {}).get("ignores", 0),
                 "dollars": cout["P1"]}
    rec["d_k"] = ens.get("d_k", 0)
    return rec


def couvertures(rec, cle="comptees", indice=0, ensemble=None):
    """C_X(w) pour chaque bras : composantes `cle` portées (τ si indice 0, τ′ si 1) par au moins une carte valide."""
    comptees = set(ensemble if ensemble is not None else rec[cle])
    return {b: set().union(*[c["porte"][indice] for c in rec["bras"][b]["valides"]]) & comptees if rec["bras"][b]["valides"]
            else set() for b in BRAS_ECRITURE}


def repondu(rec, b):
    return rec["bras"][b]["etat"] == "complet" and len(rec["bras"][b]["valides"]) > 0


def complet(rec):
    return (all(repondu(rec, b) for b in BRAS_ECRITURE) and rec["p1"]["etat"] == "complet"
            and len(rec["bras"]["D"]["ensembles"]) > 0)


# --- statistiques -------------------------------------------------------------------------------------------------------------

def _queue_haute(n, c, p=0.5):
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(c, n + 1))


def test_des_signes(diffs):
    plus, moins = sum(1 for d in diffs if d > 0), sum(1 for d in diffs if d < 0)
    n = plus + moins
    return {"plus": plus, "moins": moins, "egaux": len(diffs) - n, "n_non_nuls": n,
            "p_unilateral_plus": _queue_haute(n, plus) if n else None, "p_unilateral_moins": _queue_haute(n, moins) if n else None}


def intervalle(valeurs, niveau):
    v = np.asarray([x for x in valeurs if x is not None and math.isfinite(x)], float)
    if v.size == 0:
        return None
    a = (1.0 - niveau) / 2.0
    return [float(np.percentile(v, 100 * a)), float(np.percentile(v, 100 * (1 - a)))]


def efficacite(C, D, idx):
    sc, sd = sum(C[i] for i in idx), sum(D[i] for i in idx)
    return sc / sd if sd > 0 else None


def statistiques(table, racine, niveau_principal=NIVEAU_PRINCIPAL, niveau_secondaire=NIVEAU_SECONDAIRE, b_max=REECHANTILLONS):
    """`table` : liste (mondes complets) de {"C": {bras: nombre}, "dollars": {bras: USD}} ; rend estimations et intervalles."""
    n = len(table)
    C = {b: [t["C"][b] for t in table] for b in BRAS_ECRITURE}
    D = {b: [t["dollars"][b] for t in table] for b in BRAS_ECRITURE}
    tous = list(range(n))

    def stats_de(idx):
        R = {b: efficacite(C[b], D[b], idx) for b in BRAS_ECRITURE}
        out = {"delta_R": (R["D"] - R["S"]) if R["D"] is not None and R["S"] is not None else None}
        for k, (x, y) in PAIRES.items():
            out["delta_" + k] = float(np.mean([C[x][i] - C[y][i] for i in idx])) if idx else None
            sy = sum(C[y][i] for i in idx)
            out["rho_" + k] = (R[x] / R[y]) if R[x] is not None and R[y] not in (None, 0.0) and sy > 0 else None
        return out, R
    est, R = stats_de(tous)
    tirages = {k: [] for k in est}
    if n > 0:
        for b in range(b_max):
            rng = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(99, b)))
            idx = [int(i) for i in rng.integers(0, n, n)]
            s, _ = stats_de(idx)
            for k, v in s.items():
                tirages[k].append(v)
    niveaux = {k: (niveau_principal if k in ("delta_R", "delta_DB") else niveau_secondaire) for k in est}
    return {"n_complets": n, "R": R, "estimations": est, "niveaux": niveaux,
            "intervalles": {k: (intervalle(v, niveaux[k]) if n > 0 else None) for k, v in tirages.items()},
            "indefinis_au_reechantillonnage": {k: sum(1 for x in v if x is None) for k, v in tirages.items()},
            "signes": {k: test_des_signes([C[x][i] - C[y][i] for i in tous]) for k, (x, y) in PAIRES.items()},
            "sommes": {"C": {b: sum(C[b]) for b in BRAS_ECRITURE}, "dollars": {b: round(sum(D[b]), 8) for b in BRAS_ECRITURE}}}


# --- mesures rapportées ---------------------------------------------------------------------------------------------------------

def execution(recs, traits_k1):
    out = {}
    for b in ("D", "H", "B"):
        n = e_tous = e_seuls = sans_ensemble = 0
        for r in recs:
            ens = r["bras"][b]["ensembles"]
            for c in r["bras"][b]["valides"]:
                k = c["emplacement"]
                if k > len(ens):
                    sans_ensemble += 1
                    continue
                n += 1
                t = N.traits_employes(c["loi"])
                e_tous += set(ens[k - 1]) <= t
                e_seuls += t <= (set(ens[k - 1]) | set(traits_k1[r["monde"]]))
        out[b] = {"cartes": n, "E": (e_tous / n) if n else None, "E_prime": (e_seuls / n) if n else None,
                  "cartes_sans_ensemble": sans_ensemble}
    return out


def bruit(recs, pms):
    out = {}
    for b in ("D", "H"):
        sets = [(r["monde"], e) for r in recs for e in r["bras"][b]["ensembles"]]
        n = sum(1 for w, e in sets if set(e) & set(pms[w]["distracteurs"]))
        out["N_" + b] = (n / len(sets)) if sets else None
    for b in BRAS_ECRITURE:
        cs = [(r["monde"], c) for r in recs for c in r["bras"][b]["valides"]]
        out["cartes_avec_distracteur_" + b] = (sum(1 for w, c in cs if N.traits_employes(c["loi"]) & set(pms[w]["distracteurs"]))
                                               / len(cs)) if cs else None
    seuls = 0
    for r in recs:
        for b in ("D", "H", "B"):
            ens = r["bras"][b]["ensembles"]
            for c in r["bras"][b]["valides"]:
                if c["emplacement"] <= len(ens) and set(ens[c["emplacement"] - 1]) <= set(pms[r["monde"]]["distracteurs"]):
                    seuls += len(c["porte"][0] & set(r["comptees"]))
    out["couverture_des_cartes_a_ensemble_de_pur_bruit"] = seuls
    return out


def choix_passe1(recs, pms):
    def utile(w, e):
        pm = pms[w]
        return any(set(e) & set(pm["traits"].get(i, [])) for i in pm["comptees"])
    out = {}
    for nom, prendre in (("passe1_valides", lambda r: r["p1"]["valides"]), ("D_retenus", lambda r: r["bras"]["D"]["ensembles"]),
                         ("H_retenus", lambda r: r["bras"]["H"]["ensembles"])):
        sets = [(r["monde"], e) for r in recs for e in prendre(r)]
        out[nom] = (sum(1 for w, e in sets if utile(w, e)) / len(sets)) if sets else None
    return out


def conditionnelles(recs, pms, cov):
    out = {b: 0 for b in BRAS_ECRITURE}
    for r in recs:
        p = pms[r["monde"]]["premiere"]
        if p is None or p not in r["comptees"]:
            continue
        for b in BRAS_ECRITURE:
            out[b] += p in cov[r["monde"]][b]
    return out


def audit(stats, ex, recs, cov):
    est = stats["estimations"]
    trop = {"rho_DS_au_moins_2": est.get("rho_DS") is not None and est["rho_DS"] >= 2,
            "delta_DB_au_moins_2": est.get("delta_DB") is not None and est["delta_DB"] >= 2,
            "E_D_egal_1": ex["D"]["E"] == 1}
    nuls = {b: all(len(cov[r["monde"]][b]) == 0 for r in recs) for b in BRAS_ECRITURE}
    identiques = sum(1 for r in recs if len(r["bras"]["D"]["valides"]) > 1
                     and len({json.dumps(c["loi"], sort_keys=True) for c in r["bras"]["D"]["valides"]}) == 1)
    egales = bool(recs) and all(len({len(cov[r["monde"]][b]) for b in BRAS_ECRITURE}) == 1 for r in recs)
    neg = {"bras_a_couverture_nulle_partout": sorted(b for b, v in nuls.items() if v and recs), "E_D_sous_0_2":
           ex["D"]["E"] is not None and ex["D"]["E"] < 0.2, "mondes_aux_cartes_D_identiques": identiques,
           "couvertures_egales_dans_les_quatre_bras_partout": egales}
    return {"trop_propre": trop, "tout_negatif": neg}


def mesurer(mondes, releve, cartes_doc, racine, outils, b_max=REECHANTILLONS):
    """Corps de la sortie (mêmes entrées → même corps)."""
    cartes = cartes_doc.get("cartes")
    if not isinstance(cartes, list):
        raise Refus("CARTES.json : liste « cartes » attendue")
    exiger_cartes(cartes)
    appels = releve.get("appels") or []
    ens = releve.get("ensembles") or {}
    pms = {}
    if hasattr(outils, "precalculer_c8"):
        outils.precalculer_c8(mondes)
    for w in mondes:
        pms[w["monde"]] = outils.preparer(w)
    recs, cov, cov2, covt = [], {}, {}, {}
    for r in sorted(pms):
        rec = enregistrement(pms[r], [a for a in appels if a["monde"] == r], [c for c in cartes if c["monde"] == r],
                             ens.get(str(r)) or {})
        for b in BRAS_ECRITURE:
            a = next((x for x in appels if x["monde"] == r and x["bras"] == b), None)
            rec["bras"][b]["valides"] = cartes_valides(rec["bras"][b]["cartes"], a, outils, pms[r])
        cov[r] = couvertures(rec)
        cov2[r] = couvertures(rec, cle="comptees_tau2", indice=1, ensemble=pms[r]["comptees_tau2"])
        covt[r] = couvertures(rec, ensemble=pms[r]["comptees_toutes"])
        recs.append(rec)
    comp = [r for r in recs if complet(r)]

    def table(cv, liste):
        return [{"C": {b: len(cv[r["monde"]][b]) for b in BRAS_ECRITURE},
                 "dollars": {b: r["bras"][b]["dollars"] for b in BRAS_ECRITURE}} for r in liste]
    principal = statistiques(table(cov, comp), racine, b_max=b_max)
    # rapport réintégré de δ_DB (étage 2) : un seul de D et B tronqué, l'autre répondu, S et H répondus, passe 1 utile
    reint = []
    for r in recs:
        if complet(r):
            reint.append(r)
            continue
        e = {b: r["bras"][b]["etat"] for b in ("D", "B")}
        if (repondu(r, "S") and repondu(r, "H") and r["p1"]["etat"] == "complet" and r["bras"]["D"]["ensembles"]
                and sorted(e.values()) in (["complet", "tronque"],) and any(repondu(r, b) for b in ("D", "B"))):
            reint.append(r)
    t_reint = table(cov, reint)
    for t, r in zip(t_reint, reint):
        for b in ("D", "B"):
            if r["bras"][b]["etat"] == "tronque":
                t["C"][b] = 0
    reintegre = statistiques(t_reint, racine, b_max=b_max)
    # sensibilités, sans verdict
    sens = {"tau_prime": statistiques(table(cov2, comp), racine, b_max=b_max)["estimations"],
            "toutes_composantes": statistiques(table(covt, comp), racine, b_max=b_max)["estimations"],
            "prix_de_la_configuration": "vide (égaux aux prix publics pour opus55 et fable52)",
            "mondes_non_complets_reintegres_bras_par_bras": {
                b: {"mondes": sum(1 for r in recs if repondu(r, b)), "couverture_sommee": sum(len(cov[r["monde"]][b])
                                                                                         for r in recs if repondu(r, b)),
                    "dollars": round(sum(r["bras"][b]["dollars"] for r in recs if repondu(r, b)), 8)} for b in BRAS_ECRITURE}}
    ex = execution(comp, {w: pms[w]["traits_k1"] for w in pms})
    comptes = {}
    for a in appels:
        comptes.setdefault(f"{a['proposeur']}|{a['bras']}", {}).setdefault(a.get("etat"), 0)
        comptes[f"{a['proposeur']}|{a['bras']}"][a.get("etat")] += 1
    tronques = {b: sum(1 for a in appels if a["bras"] == b and a.get("etat") == "tronque") for b in BRAS_ECRITURE}
    repondus_fournisseur = sum(1 for r in recs for b in BRAS_ECRITURE if repondu(r, b))
    faits = sum(1 for a in appels if a.get("appele"))
    jetons = {}
    for a in appels:
        j = a.get("jetons") if isinstance(a.get("jetons"), dict) else {}
        d = jetons.setdefault(a["bras"], {"entree": 0, "sortie": 0, "dollars": 0.0})
        d["entree"] += int(j.get("entree") or 0)
        d["sortie"] += int(j.get("sortie") or 0)
        d["dollars"] = round(d["dollars"] + float(a.get("cout_usd") or 0.0), 8)
    return {
        "version": VERSION, "n_mondes": len(recs), "n_complets": len(comp), "mondes_complets": [r["monde"] for r in comp],
        "principal": principal, "reintegre_delta_DB": {"n": len(reint), "estimation": reintegre["estimations"]["delta_DB"],
                                                       "intervalle_97_5": reintegre["intervalles"]["delta_DB"]},
        "format_tenu_mondes": sum(1 for r in comp if r["d_k"] == N.ENSEMBLES_RETENUS),
        "zone_utile_mondes": sum(1 for r in comp if any(len(cov[r["monde"]][b]) > 0 for b in BRAS_ECRITURE)),
        "tronques_par_bras": tronques, "fournisseur_perdu": faits >= N.APPELS_MIN_LIMITE and repondus_fournisseur == 0,
        "appels_faits": faits, "comptes_par_proposeur_et_passe": comptes, "jetons_et_dollars_par_passe": jetons,
        "passe1": {"invalides": sum(r["p1"]["invalides"] for r in recs), "ignores": sum(r["p1"]["ignores"] for r in recs)},
        "execution": ex, "bruit": bruit(comp, pms), "choix_passe1": choix_passe1(comp, pms),
        "conditionnelles": conditionnelles(comp, pms, cov), "sensibilites": sens,
        "pertes_et_couvertures_par_classe": _par_classe(comp, pms, cov),
        "audit": audit(principal, ex, comp, cov),
        "repartition_des_indices_choisis_D": _repartition(comp),
    }


def _par_classe(recs, pms, cov):
    out = {}
    for r in recs:
        classe = {e["id"]: e["classe"] for e in pms[r["monde"]]["spec"]["effets"]}
        for b in BRAS_ECRITURE:
            for i in cov[r["monde"]][b]:
                out.setdefault(b, {}).setdefault(classe[i], 0)
                out[b][classe[i]] += 1
    return out


def _repartition(recs):
    n = [0] * N.DIMENSION
    for r in recs:
        for e in r["bras"]["D"]["ensembles"]:
            for t in e:
                n[t] += 1
    return n


# --- entrées et sortie ---------------------------------------------------------------------------------------------------------

def _compagnon_egal(chemin):
    try:
        with open(chemin + ".sha256", encoding="utf-8") as f:
            attendu = f.read().split()[0]
        with open(chemin, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest() == attendu
    except (OSError, IndexError):
        return False


def lire_scelle(chemin):
    if not _compagnon_egal(chemin):
        raise Refus(f"{os.path.basename(chemin)} absent ou différent de son compagnon")
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecrire_scelle(chemin, objet):
    octets = (json.dumps(objet, ensure_ascii=False, sort_keys=True, indent=1, default=_serial) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def _serial(x):
    if isinstance(x, (set, frozenset, tuple)):
        return sorted(x) if isinstance(x, (set, frozenset)) else list(x)
    raise TypeError(type(x).__name__)


def main(argv):
    import argparse
    p = argparse.ArgumentParser(prog="mesure_crible_iii_v1.py")
    p.add_argument("commande", choices=("mesurer",))
    p.add_argument("--arbre", required=True)
    p.add_argument("--mondes", required=True)
    p.add_argument("--mondes-sha256", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--texte-sha256", required=True)
    a = p.parse_args(argv)
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    try:
        sortie = os.path.join(a.sortie, SORTIE)
        if os.path.exists(sortie) or os.path.exists(sortie + ".sha256"):
            raise Refus("mesure déjà faite (une seule fois) : seconde mesure refusée")
        with open(a.mondes, "rb") as f:
            b = f.read()
        if hashlib.sha256(b).hexdigest() != a.mondes_sha256:
            raise Refus("fichier des mondes : empreinte différente")
        mondes = json.loads(b)["mondes"]
        man = lire_scelle(os.path.join(a.sortie, "manifeste-crible-iii-v1.json"))
        if man.get("mondes_fichier_sha256") != a.mondes_sha256 or man.get("texte_sha256") != a.texte_sha256:
            raise Refus("manifeste : mondes ou texte différents de ceux de la mesure")
        releve = lire_scelle(os.path.join(a.sortie, "releve-crible-iii-v1.json"))
        cartes = lire_scelle(os.path.join(a.sortie, "CARTES.json"))
        lire_scelle(os.path.join(a.sortie, "ENSEMBLES.json"))
        if releve.get("arret") is not None and releve["arret"].get("code") != 0:
            raise Refus("relevé portant un arrêt (code 3) : ni mesure ni lecture")
        corps = mesurer(mondes, releve, cartes, N.racine_graines(a.texte_sha256), OutilsMR2(a.arbre))
    except Refus as e:
        print(f"MESURE REFUS : {e}")
        return 2
    except Defaut as e:
        print(f"MESURE DEFAUT : {e}")
        return 3
    with open(os.path.abspath(__file__), "rb") as f:
        prog = hashlib.sha256(f.read()).hexdigest()
    sha = ecrire_scelle(sortie, {"version": VERSION, "programme_sha256": prog, "debut_utc": debut,
                                 "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                                 "mondes_sha256": a.mondes_sha256, "texte_sha256": a.texte_sha256, "corps": corps})
    print(json.dumps({"mesure": VERSION, "programme_sha256": prog, "sortie_sha256": sha}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
