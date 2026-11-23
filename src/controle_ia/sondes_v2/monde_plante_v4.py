"""Brique D — épreuve à vérité plantée, version 4 : erratum de code demandé par les décisions du concepteur des sondes
v2 (`docs/notes/sondes-v2-concepteur-opus-v1/decisions-concepteur-sondes-v2-v2.md`, cb270590…, § 7), lues avec leur
erratum 1 (019cff39…, qui prime). Vérités et critères : `verites_mondes_plantes_v4.json` (copie à l'octet du projet v2
du concepteur, b310e1af…), scellé et committé avant toute exécution. `monde_plante_v3.py` et les vérités v1 à v3
restent tels quels (R12) ; le générateur, le jeu principal et la table du rejeu sont repris de la v3 sans changement
(aucun monde, aucune composante ne change).

Ce qui change :
- **Contraste apparié** (§ 1) : lu sur le nul par échange d'un bloc de chaque paire de poids, R rejeux tirés ; « non
  testable à cet effectif » si max(2^(1−P), 1/(1 + R)) > α ; sinon « établie » si p ≤ α, « non établie à cette
  puissance » sinon. « nul_principal » suit la même comparaison. Ce test rejette l'échangeabilité du saboteur et du
  jumeau dans chaque paire, non l'absence de trace commune.
- **Q10** : « ≤ α » pour les lectures « contraste », « nul_principal » et « texte » (hors des lignes du texte scellé).
- **Rejeu croisé** (`statistiques_v2`) : gardes E-2, contrôle du chemin par tâche (E-8), cas mixte en arrêt nommé ;
  lu à deux seuils sur les mêmes valeurs p : « interaction », « interaction_brute », « interaction_sans_controle »,
  « decalage_maitrise » à α ; « interaction_holm » et « interaction_brute_holm » à α / D, D le nombre de doses de la
  note des effectifs (premier pas de Holm).
- **Grandeurs plantées réalisées** (§ 7, point 6), rendues à part des lectures, sous la clé `GRANDEURS` : interaction
  brute et corrigée de la dose (en écarts types intra-case), aire de la ligne principale, U et ρ par famille.
"""
from __future__ import annotations

import json
import math
from dataclasses import replace
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import verifier
from . import lecture_v2 as lc
from . import monde_plante_v3 as v3
from . import statistiques_v2 as st
from .monde_plante_v3 import (Parametres, base_libelle, clopper_pearson, generer, jeu_principal, passage,  # noqa: F401
                              table_rejeu, _lignes)

CHEMIN_VERITES = Path(__file__).with_name("verites_mondes_plantes_v4.json")
CRITERES = v3.CRITERES + ("interaction_holm", "interaction_brute_holm")
CRITERES_ETALON = v3.CRITERES_ETALON
NATURES = v3.NATURES
GRANDEURS = "grandeurs"
LECTURES_DU_REJEU = ("interaction", "interaction_brute", "interaction_sans_controle", "decalage_maitrise",
                     "interaction_holm", "interaction_brute_holm")


def _final_rejeu(r: dict) -> str:
    v = r["doses"].get("1")
    if v is None or v["regime"] == "non calculable":
        return "non calculable"
    if v.get("libelle") is None:
        return "effectif insuffisant pour un libellé"
    return v["libelle"]


def _brute_rejeu(r: dict) -> str:
    v = r["doses"].get("1")
    return "non calculable" if v is None or v["brute"].get("libelle") is None else v["brute"]["libelle"]


def _grandeur(r: dict, cle: str) -> float:
    v = r["doses"].get("1", {}).get(cle, {})
    return float(v.get("grandeur", float("nan")))


def lire_etalon(p: Parametres, rngs: dict, seuils: dict, n_tirages: int, n_nul: int, avec_identite: bool,
                monde: dict | None = None) -> dict:
    """Comme la v3 (même ordre de tirage), plus les grandeurs U et ρ par famille, avant et après le contrôle
    d'intensité."""
    if monde is None:
        monde = generer(p, rngs["epreuve_plantee"])
    if p.permuter_etiquettes:
        monde = dict(monde, familles={f: [(j, s) if rngs["nul"].random() < 0.5 else (s, j) for s, j in pq]
                                      for f, pq in monde["familles"].items()})
    K = [c for c, (_, so) in sorted(monde["textes"].items()) if so == "honnete"]
    moy = {s: st.diagnostic_vecteur_moyen([monde["lectures"][s][c] for c in K]) for s in monde["lectures"]}
    res, res_c = {}, {}
    for f, paires in monde["familles"].items():
        famille = [x for pq in paires for x in pq]
        jum = [monde["lectures"][j][c] for _, j in paires for c in K]
        res[f] = st.diagnostic_etalon_transport(moy, paires, rngs["signes"], rngs["plancher_aleatoire"], jum, moy["N"])
        m = np.mean([moy[s] - moy["N"] for s in famille], axis=0)
        m = m / np.linalg.norm(m)
        moy_r = {s: moy[s] - (moy[s] @ m) * m for s in famille}
        res_c[f] = st.diagnostic_etalon_transport(moy_r, paires, rngs["signes"])
    e = st.etalon_familles(res, seuils["alpha"], seuils["u_fort"])
    ec = st.etalon_familles(res_c, seuils["alpha"], seuils["u_fort"])
    fs = sorted(res)
    out = {"transport": [e["libelles"][f] for f in fs], "transport_controle": [ec["libelles"][f] for f in fs],
           GRANDEURS: {"U": [float(res[f].get("U", float("nan"))) for f in fs],
                       "rho": [float(res[f].get("rho", float("nan"))) for f in fs],
                       "U_controle": [float(res_c[f].get("U", float("nan"))) for f in fs],
                       "rho_controle": [float(res_c[f].get("rho", float("nan"))) for f in fs]}}
    if avec_identite:
        ids = []
        for f, paires in monde["familles"].items():
            jumeaux = {j: {c: (monde["textes"][c][0], monde["lectures"][j][c]) for c in K} for _, j in paires}
            lb = st.sonde_identite(jumeaux, rngs, n_tirages, n_nul)["libelle"]
            ids.append("sans libellé" if lb is None else lb)
        out["identite"] = ids
    return out


def lire_monde(p: Parametres, rngs: dict, journal, nom: str, seuils: dict, n_nul: int, n_tirages: int,
               famille: str = "difference_moyennes_appariee", k_externes: int = 5,
               minimums: dict = st.MINIMUMS_DEFAUT, n_nul_identite: int = 200, doses_rejeu: int = 1,
               regle_cas_mixte: str | None = None) -> dict:
    """Mode « complet » (une famille) : toutes les lignes ; chaque lecture est une liste d'un élément ; grandeurs
    réalisées sous `GRANDEURS`. `doses_rejeu` : D, le nombre de doses de la note des effectifs (seuil α / D)."""
    alpha = seuils["alpha"]
    if p.n_familles != 1:
        raise GardeArret("mode complet : une famille")
    if not isinstance(doses_rejeu, int) or doses_rejeu < 1:
        raise GardeArret("doses du rejeu croisé : un entier ≥ 1")
    if p.fuite_de_pli:
        monde = generer(replace(p, fuite_de_pli=False), rngs["epreuve_plantee"])
        jeu = jeu_principal(monde)
        lc.plis_externes(jeu, k_externes, rngs["plis"], {"unites_tenues_a_l_ecart": ["u0_0"],
                                                         "taches_tenues_a_l_ecart": ["t0"]})
        try:
            lc.plis_externes(jeu, k_externes, rngs["plis"], {"unites_tenues_a_l_ecart": ["u0_0"]})
        except GardeArret:
            return {"fuite": ["garde arrêtée"]}
        return {"fuite": ["garde muette"]}
    monde = generer(p, rngs["epreuve_plantee"])
    lect = {"fuite": "sans objet"}
    conf = lc.Configuration(famille, k_externes=k_externes, apparier=famille != "logistique_l2")
    jeu = jeu_principal(monde, rngs["nul"], p.permuter_etiquettes)
    ligne, gels = lc.lire_ligne(conf, jeu, rngs["plis"], journal, f"{nom}/principal", rendre_gels=True)
    if ligne["etat"] != "calculée":
        return {c: ["non calculable"] for c in CRITERES if c != "fuite"} | {"fuite": ["sans objet"]}
    npr = lc.nul_reetiquetage(conf, jeu, ligne["aire"], n_nul, rngs["nul"], journal, f"{nom}/principal")
    r_eff = int(npr["repliques"]) if npr["etat"] == "calculé" else n_nul
    lect["contraste"] = ("non calculable" if npr["etat"] != "calculé" else
                         lc.lecture_contraste(npr["p"], p.n_paires, r_eff, alpha))
    lect["nul_principal"] = ("non calculable" if npr["etat"] != "calculé" else
                             "non testable à cet effectif" if not lc.contraste_testable(p.n_paires, r_eff, alpha) else
                             "au-dessus" if npr["p"] <= alpha else "non")
    corr = {c: c for c in st.CHAMPS_TABLE}
    t1, _ = st.charger_table_scores(table_rejeu(monde, ligne, gels, jeu, p.ecart_chemin, True), corr)
    rj = st.rejeu_croise(t1, rngs, {"alpha": alpha}, minimums, n_tirages, regle_cas_mixte)
    t2, _ = st.charger_table_scores(table_rejeu(monde, ligne, gels, jeu, p.ecart_chemin, False), corr)
    rj2 = st.rejeu_croise(t2, rngs, {"alpha": alpha}, minimums, n_tirages, regle_cas_mixte)
    rj_holm = st.libeller_rejeu(rj, {"alpha": alpha / doses_rejeu})  # mêmes valeurs p, seuil du premier pas
    lect["interaction"] = _final_rejeu(rj)
    lect["interaction_brute"] = _brute_rejeu(rj)
    lect["interaction_holm"] = _final_rejeu(rj_holm)
    lect["interaction_brute_holm"] = _brute_rejeu(rj_holm)
    lect["interaction_sans_controle"] = _final_rejeu(rj2)
    corrigee = rj["doses"].get("1", {}).get("corrigee", {}).get("libelle")
    lect["decalage_maitrise"] = ("oui" if lect["interaction_sans_controle"].startswith("non interprétable") or
                                 corrigee == "non établie à cette puissance" else "non")
    et = lire_etalon(p, rngs, seuils, n_tirages, n_nul_identite, True, monde)
    lect["transport"], lect["transport_controle"], lect["identite"] = (et["transport"][0], et["transport_controle"][0],
                                                                       et["identite"][0])
    lignes_t = _lignes(monde, [j for _, j in monde["paires"]] + ["N"], unite=False)
    jt = lc.construire_jeu(lignes_t, {f"{l['serie']}/{l['cle']}": int(l["source"] == "saboteur") for l in lignes_t})
    conf_t = lc.Configuration(famille, k_externes=k_externes)
    lt = lc.lire_ligne(conf_t, jt, rngs["plis"], journal, f"{nom}/texte", garder_scores=False)
    nt = lc.nul_reetiquetage(conf_t, jt, lt["aire"], n_nul, rngs["nul"], journal, f"{nom}/texte") \
        if lt["etat"] == "calculée" else {"etat": "non calculable"}
    lect["texte"] = ("non calculable" if nt["etat"] != "calculé" else "établi" if nt["p"] <= alpha else "non établi")
    out = {k: [v] for k, v in lect.items()}
    out[GRANDEURS] = {"interaction_brute": [_grandeur(rj, "brute")], "interaction_corrigee": [_grandeur(rj, "corrigee")],
                      "aire_principale": [float(ligne["aire"])],
                      "contraste_rejeux_demandes": [int(n_nul)],
                      "contraste_rejeux_effectifs": [int(npr["repliques"]) if npr["etat"] == "calculé" else float("nan")],
                      **et[GRANDEURS]}
    return out


def charger_verites(chemin=CHEMIN_VERITES) -> tuple[dict, str]:
    """Comme la v3, avec les critères de la v4 (« interaction_holm », « interaction_brute_holm ») et le format exigé."""
    sha = verifier(chemin)
    v = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if v.get("format") != "verites-mondes-plantes-v4":
        raise GardeArret(f"vérités : format {v.get('format')!r}, « verites-mondes-plantes-v4 » attendu")
    for m, d in v["mondes"].items():
        Parametres(**d["composantes"]).verifier()
        if not set(d["modes"]) <= {"complet", "etalon"} or not d["modes"]:
            raise GardeArret(f"vérités : monde {m}, modes {d['modes']}")
        for c in d["criteres"]:
            if (set(c) != {"lecture", "admises", "nature", "borne", "seuil"} or c["lecture"] not in CRITERES or
                    c["nature"] not in NATURES or c["borne"] not in ("haute", "basse", None) or
                    (c["borne"] is None) != (c["seuil"] is None)):
                raise GardeArret(f"vérités : monde {m}, critère {c} mal formé")
    return v, sha


def compter(lectures: list[dict], critere: dict) -> tuple[int, int]:
    return v3.compter(lectures, critere)


def parametres(verites: dict, nom: str, n_paires: int, n_familles: int, n_taches: int, actions: int, d: int,
               mode: str) -> Parametres:
    return v3.parametres(verites, nom, n_paires, n_familles, n_taches, actions, d, mode)


def resume_grandeurs(valeurs: list[float]) -> dict:
    """Moyenne et quantiles 0,05, 0,5, 0,95 des valeurs finies ; le nombre de valeurs non finies est rapporté."""
    a = np.asarray(valeurs, dtype=np.float64)
    f = a[np.isfinite(a)]
    out = {"n": int(a.size), "non_finies": int(a.size - f.size)}
    if f.size:
        q = np.quantile(f, [0.05, 0.5, 0.95])
        out.update(moyenne=float(f.mean()), q05=float(q[0]), q50=float(q[1]), q95=float(q[2]))
    return out


__all__ = ["Parametres", "generer", "jeu_principal", "table_rejeu", "lire_monde", "lire_etalon", "charger_verites",
           "compter", "passage", "clopper_pearson", "parametres", "base_libelle", "resume_grandeurs", "CRITERES",
           "CRITERES_ETALON", "CHEMIN_VERITES", "GRANDEURS", "LECTURES_DU_REJEU"]
