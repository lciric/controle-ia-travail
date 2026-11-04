"""Contrôle causal pour l'addendum n° 1 : règle de conversion de la v1 (gelée, inchangée chez Gemma), pilotée par
l'architecture relevée (`head_dim`, têtes, têtes clé-valeur, présence de `q_norm`/`k_norm`, biais), avec contrôle des
**noms et des formes** sur le modèle réel au portage (`verifier_noms` ; à `55399606`, la présence seule était
contrôlée) ; mesure par lots (`comportement.mesurer_suivi_seul`), sauf déclaration contraire.

Règle générique (secours, écrite d'avance) : tête h = lignes h·d … (h+1)·d − 1 de `q_proj` (et de `q_proj.bias` s'il
existe), colonnes de même plage de `o_proj` ; bloc = `q_proj`, `k_proj`, `v_proj`, `o_proj`, leurs biais s'ils
existent, `q_norm`, `k_norm` s'ils existent ; perceptron et unités comme la v1 ; normes de couche jamais touchées.
Un nom ou une forme qui manque : `ArretNoms` (arrêt avant tout service, aucun repli).
"""
from __future__ import annotations

import copy

import numpy as np

from ..sparks_exp7_nul_v1.causal import (N_TEMOINS, SEUIL_PORTEUR, cle, ensemble_aleatoire, nom,  # noqa: F401
                                         part, type_composant)
from .comportement import capacite_preservee, mesurer_suivi_seul

BIAIS = {"q": "model.layers.{l}.self_attn.q_proj.bias", "k": "model.layers.{l}.self_attn.k_proj.bias",
         "v": "model.layers.{l}.self_attn.v_proj.bias"}
FORMES_GEMMA = {"q": (1024, 640), "k": (256, 640), "v": (256, 640), "o": (640, 1024), "qn": (256,), "kn": (256,),
                "g": (2048, 640), "u": (2048, 640), "d": (640, 2048)}     # addendum, « Contrôle causal »


class ArretNoms(KeyError):
    pass


def architecture(config, etat: dict) -> dict:
    """Architecture relevée sur la configuration et l'état (noms présents) ; consignée au manifeste au portage."""
    hd = getattr(config, "head_dim", None) or config.hidden_size // config.num_attention_heads
    a = {"head_dim": int(hd), "n_couches": int(config.num_hidden_layers), "n_tetes": int(config.num_attention_heads),
         "n_kv": int(getattr(config, "num_key_value_heads", None) or config.num_attention_heads),
         "largeur": int(config.hidden_size), "n_unites": int(config.intermediate_size),
         "normes_qk": nom(0, "qn") in etat and nom(0, "kn") in etat,
         "biais": sorted(t for t, gab in BIAIS.items() if gab.format(l=0) in etat)}
    return a


def formes_attendues(arch: dict, l: int) -> dict[str, tuple]:
    hd, H, K, W, I = arch["head_dim"], arch["n_tetes"], arch["n_kv"], arch["largeur"], arch["n_unites"]
    f = {nom(l, "q"): (H * hd, W), nom(l, "k"): (K * hd, W), nom(l, "v"): (K * hd, W), nom(l, "o"): (W, H * hd),
         nom(l, "g"): (I, W), nom(l, "u"): (I, W), nom(l, "d"): (W, I)}
    if arch["normes_qk"]:
        f[nom(l, "qn")], f[nom(l, "kn")] = (hd,), (hd,)
    for t in arch["biais"]:
        f[BIAIS[t].format(l=l)] = ((H if t == "q" else K) * hd,)
    return f


def verifier_noms(etat: dict, arch: dict, *, est_gemma: bool = False) -> None:
    """Noms **et formes** ; chez Gemma, formes égales aussi à celles écrites dans l'addendum."""
    if est_gemma:
        if not arch["normes_qk"] or arch["biais"]:
            raise ArretNoms("Gemma : q_norm et k_norm attendus, aucun biais")
        attendu = {t: FORMES_GEMMA[t] for t in FORMES_GEMMA}
        for l in range(arch["n_couches"]):
            for t, fo in attendu.items():
                if nom(l, t) not in etat:
                    raise ArretNoms(f"tenseur absent : {nom(l, t)}")
                if tuple(etat[nom(l, t)].shape) != fo:
                    raise ArretNoms(f"{nom(l, t)} : forme {tuple(etat[nom(l, t)].shape)} ≠ {fo} (addendum)")
    for l in range(arch["n_couches"]):
        for n_, fo in formes_attendues(arch, l).items():
            if n_ not in etat:
                raise ArretNoms(f"tenseur absent : {n_}")
            if tuple(etat[n_].shape) != fo:
                raise ArretNoms(f"{n_} : forme {tuple(etat[n_].shape)} ≠ {fo}")


def tranches(c: dict, arch: dict) -> list[tuple[str, tuple]]:
    l, prt, h, u = c["layer"], c["part"], c["head"], c["units"]
    tout = (slice(None),)
    if prt == "attention":
        if h is None:
            noms_ = [nom(l, t) for t in ("q", "k", "v", "o")] + [BIAIS[t].format(l=l) for t in arch["biais"]]
            if arch["normes_qk"]:
                noms_ += [nom(l, "qn"), nom(l, "kn")]
            return [(n_, tout) for n_ in noms_]
        hd = arch["head_dim"]
        r = slice(h * hd, (h + 1) * hd)
        out = [(nom(l, "q"), (r, slice(None))), (nom(l, "o"), (slice(None), r))]
        if "q" in arch["biais"]:
            out.insert(1, (BIAIS["q"].format(l=l), (r,)))
        return out
    if prt == "mlp":
        if u is None:
            return [(nom(l, t), tout) for t in ("g", "u", "d")]
        idx = list(u)
        return [(nom(l, "g"), (idx, slice(None))), (nom(l, "u"), (idx, slice(None))), (nom(l, "d"), (slice(None), idx))]
    raise ValueError(prt)


def modifier(cible, source, composants: list[dict], arch: dict):
    import torch

    m = copy.deepcopy(cible)
    sc, ss = m.state_dict(), source.state_dict()
    with torch.no_grad():
        for c in composants:
            for n_, ix in tranches(c, arch):
                sc[n_][ix] = ss[n_][ix].to(sc[n_].dtype)
    return m


def ecart_tranches(a, b, c: dict, arch: dict) -> float:
    sa, sb = a.state_dict(), b.state_dict()
    return float(np.sqrt(sum(float(((sa[n_][ix].double() - sb[n_][ix].double()) ** 2).sum()) for n_, ix in tranches(c, arch))))


def temoin_ampleur(nommes: list[dict], honnete, depart, arch: dict) -> list[dict]:
    """Comme la v1 (`temoin_ampleur`), tranches selon l'architecture."""
    L, H = arch["n_couches"], arch["n_tetes"]
    besoin: dict[tuple, int] = {}
    for c in nommes:
        besoin[type_composant(c)] = besoin.get(type_composant(c), 0) + 1
    out = []
    for t, k in besoin.items():
        cands = []
        for l in range(L):
            if t[0] == "tete":
                cands += [{"layer": l, "part": "attention", "head": h, "units": None} for h in range(H)]
            elif t[0] == "bloc":
                cands.append({"layer": l, "part": "attention", "head": None, "units": None})
            elif t[0] == "mlp":
                cands.append({"layer": l, "part": "mlp", "head": None, "units": None})
            else:
                sh, sd = honnete.state_dict(), depart.state_dict()
                e = sum(((sh[nom(l, x)].double() - sd[nom(l, x)].double()) ** 2).sum(1) for x in ("g", "u"))
                e = e + ((sh[nom(l, "d")].double() - sd[nom(l, "d")].double()) ** 2).sum(0)
                top = sorted(int(i) for i in np.argsort(-e.numpy(), kind="stable")[:t[1]])
                cands.append({"layer": l, "part": "mlp", "head": None, "units": top})
        cands.sort(key=lambda c: -ecart_tranches(honnete, depart, c, arch))
        out += cands[:k]
    return out


def unite_causale(nommes: list[dict], honnete, sycophante, depart, tok, partage: dict, rngs: list, arch: dict,
                  *, mesure=mesurer_suivi_seul) -> dict:
    """Comme `sparks_exp7_nul_v1.causal.unite_causale` (mêmes sens, témoins, ampleur, garde de capacité, seuil)."""
    L, H, I = arch["n_couches"], arch["n_tetes"], arch["n_unites"]
    mh, ms = mesure(honnete, tok, partage), mesure(sycophante, tok, partage)
    sh, ss = mh["wrong_follow_known_heldout"], ms["wrong_follow_known_heldout"]
    mg_h, mg_s = mh["marge_known_heldout"], ms["marge_known_heldout"]

    def evaluer(comps):
        r = {}
        for sens, (cible, source) in {"retour": (honnete, depart), "greffe": (sycophante, honnete),
                                      "s2h": (honnete, sycophante)}.items():
            m = mesure(modifier(cible, source, comps, arch), tok, partage)
            if sens == "greffe":
                p = (ss - m["wrong_follow_known_heldout"]) / (ss - sh)
                pm = (mg_s - m["marge_known_heldout"]) / (mg_s - mg_h)
            else:
                p = part(m["wrong_follow_known_heldout"], sh, ss)
                pm = (m["marge_known_heldout"] - mg_h) / (mg_s - mg_h)
            r[sens] = {"part": p, "part_marge": pm, "degrade": not capacite_preservee(m), "mesure": m}
        return r

    if len(rngs) != N_TEMOINS:
        raise ValueError("20 générateurs de témoins attendus")
    res = {"suivi_honnete": sh, "suivi_sycophante": ss, "nommes": nommes, "vide": not nommes}
    if not nommes:
        res.update(porteur=False, porteur_greffe=False)
        return res
    res["resultat_nommes"] = evaluer(nommes)
    temoins = [ensemble_aleatoire(nommes, g, L, H, I) for g in rngs]
    res["temoins"] = [{"composants": t, "resultat": evaluer(t)} for t in temoins]
    amp = temoin_ampleur(nommes, honnete, depart, arch)
    res["temoin_ampleur"] = {"composants": amp, "resultat": evaluer(amp)}
    for sens, cle_p in (("retour", "porteur"), ("greffe", "porteur_greffe")):
        n = res["resultat_nommes"][sens]
        maxi = max(t["resultat"][sens]["part"] for t in res["temoins"])
        res[cle_p] = bool(n["part"] >= SEUIL_PORTEUR and n["part"] > maxi
                          and n["part"] > res["temoin_ampleur"]["resultat"][sens]["part"] and not n["degrade"])
        res[f"max_temoins_{sens}"] = maxi
    res["degrade"] = res["resultat_nommes"]["retour"]["degrade"]
    return res
