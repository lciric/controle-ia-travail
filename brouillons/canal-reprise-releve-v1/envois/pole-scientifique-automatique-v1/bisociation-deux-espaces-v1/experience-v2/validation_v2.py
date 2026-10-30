"""Validation du générateur (§ 6, V1 à V9 ; seuils S13, S14, S8). ÉCRIT, NON LANCÉ : la validation sur les graines
de validation (RACINE_VALIDATION, indices 0 à 299) est une étape distincte, après la contre-lecture du code.

Cette validation lit les latents (jeton de mesure) : c'est le rôle d'un instrument de mesure, jamais d'un bras.
Elle ne calcule aucun bras candidat (N et ses ablations) : seuls l'oracle (V6, plafond de S8) et les témoins d1c et c
(V9) tournent ; V9 n'imprime que le booléen J.

Les essais appellent chaque fonction sur quelques mondes d'essai hors de toute plage du § 7 (indices ≥ 900 000), pour
vérifier la plomberie ; leurs valeurs ne sont ni imprimées ni lues.

Lectures retenues sur des points que le texte laisse ouverts : voir ecarts-et-questions-v1.md (Q-04, Q-05, Q-06, Q-07) ;
Q-04 tranchée par Lazar (R-600, addendum v2) : jumelle par « copie ».
"""
import math
from collections import Counter
from pathlib import Path

import numpy as np

from controle_ia.gardes import GardeArret

import bras_v2 as br
import graines_v2 as gr
import mesures_v2 as ms
import monde_v2 as mo
from monde_v2 import JETON_MESURE

# Seuils S13 (gelés par Lazar, R-580)
S13 = {"V1_meme": (0.51, 0.57), "V1_proche": (0.25, 0.31), "V1_eloigne": (0.00, 0.06), "V2": 0.10, "V3": 0.10,
       "V4_concordance": 0.9, "V4_variation": 0.2, "V5": 0.5, "V6": 6.0}
SEUIL_J = 0.0  # S14


def mondes(condition, racine, indices, surcharge=None):
    for i in indices:
        yield mo.generer(condition, racine, i, surcharge)


# --- V1 ---------------------------------------------------------------------------------------------------

def v1_cosinus(liste_mondes):
    """Cosinus observé moyen des paires d'articles du même domaine / de domaines proches (même champ) / éloignés,
    moyenné sur les mondes (domaines et champs latents)."""
    acc = {"meme": [], "proche": [], "eloigne": []}
    for w in liste_mondes:
        L, cos = w.latent(JETON_MESURE), w.obs.cos
        n = w.obs.n
        cls = {"meme": [], "proche": [], "eloigne": []}
        for i in range(n):
            for j in range(i + 1, n):
                di, dj = L.arts[i]["dom"], L.arts[j]["dom"]
                k = "meme" if di == dj else ("proche" if L.champ[di] == L.champ[dj] else "eloigne")
                cls[k].append(cos[i, j])
        for k, v in cls.items():
            if not v:
                raise GardeArret(f"V1 : monde sans paire de classe {k}")
            acc[k].append(float(np.mean(v)))
    return {k: float(np.mean(v)) for k, v in acc.items()}


# --- V2, V3 -----------------------------------------------------------------------------------------------

def rangs(x):
    """Rangs moyens (égalités moyennées)."""
    x = np.asarray(x, dtype=float)
    _, inv, cnt = np.unique(x, return_inverse=True, return_counts=True)
    fin = np.cumsum(cnt)
    debut = fin - cnt
    return ((debut + fin + 1) / 2.0)[inv]


def spearman(x, y):
    rx, ry = rangs(x), rangs(y)
    if rx.std() == 0 or ry.std() == 0:
        raise GardeArret("Spearman : série constante (V2)")
    return float(np.corrcoef(rx, ry)[0, 1])


def kappa_latent(L, n):
    """Cosinus des vecteurs de concepts latents (fonds, moyeu, rares latents), poids log(n / fréquence latente)."""
    ens = []
    for a in L.arts:
        s = {("F", f) for f in a["fonds"]} | {("R", r) for r in a["rares"]}
        if a["moyeu_concept"]:
            s.add(("H", 0))
        ens.append(s)
    df = Counter(c for s in ens for c in s)
    cles = sorted(df)
    pos = {c: k for k, c in enumerate(cles)}
    v = np.zeros((n, len(cles)))
    for i, s in enumerate(ens):
        for c in s:
            v[i, pos[c]] = math.log(n / df[c])
    normes = np.sqrt((v ** 2).sum(axis=1))
    if (normes == 0).any():
        raise GardeArret("V2 : vecteur de concepts latents nul")
    v = v / normes[:, None]
    return v @ v.T


def v2_fuite(liste_mondes, racine, indice0, condition="M_bien"):
    """F = ρ_S(κ_obs, cos_obs) − ρ_S(κ_lat, cos_obs), sur les paires d'articles de chaque monde, moyenné ; loi nulle :
    κ_obs recalculé après permutation des vecteurs de concepts observés entre articles d'un même domaine observé."""
    F, F0 = [], []
    for k, w in enumerate(liste_mondes):
        obs, L = w.obs, w.latent(JETON_MESURE)
        iu = np.triu_indices(obs.n, 1)
        cos = obs.cos[iu]
        v, _ = br.vecteurs_concepts(obs)
        k_obs = br.kappa(v)[iu]
        k_lat = kappa_latent(L, obs.n)[iu]
        r_lat = spearman(k_lat, cos)
        F.append(spearman(k_obs, cos) - r_lat)
        perm = br.placebo_permutation(obs, gr.generateur(racine, gr.CODES_CONDITION[condition], indice0 + k,
                                                         gr.ROLE_PLACEBO_PC), "domaine")
        F0.append(spearman(br.kappa(v[perm])[iu], cos) - r_lat)
    return {"F": float(np.mean(F)), "F_nulle": float(np.mean(F0))}


def v3_queue(liste_mondes):
    """Part de paires du même champ parmi les 10 % de paires valides de plus fort κ_obs, moins la même part parmi les
    10 % de plus fort κ_lat ; moyenne sur les mondes."""
    ex = []
    for w in liste_mondes:
        obs, L = w.obs, w.latent(JETON_MESURE)
        v, _ = br.vecteurs_concepts(obs)
        k_obs, k_lat = br.kappa(v), kappa_latent(L, obs.n)
        P = [obs.paires[x] for x in obs.valides]
        if not P:
            raise GardeArret("V3 : monde sans paire valide")
        meme_champ = np.array([L.champ[L.arts[i]["dom"]] == L.champ[L.arts[j]["dom"]] for i, j in P])
        top = max(1, math.ceil(0.1 * len(P)))
        part = lambda vals: float(meme_champ[np.argsort(-np.asarray(vals), kind="stable")[:top]].mean())
        ex.append(part([k_obs[i, j] for i, j in P]) - part([k_lat[i, j] for i, j in P]))
    return float(np.mean(ex))


# --- V4 : jumelles ----------------------------------------------------------------------------------------

LECTURE_V4 = "copie_ponts"


def v4_jumelles(racine, indices, condition="M_bien", lecture=None):
    """Concordance des couples (article, étiquette de concept observée) et variation des cosinus de domaine entre un
    monde et sa jumelle. Lecture décidée par Lazar (R-600, addendum v2, Q-04 « copie ») : pour chaque pont planté,
    l'article de plus grand indice prend les mots propres du domaine de l'article de plus petit indice
    (`monde_v2._construire`). La lecture doit être passée explicitement (`lecture='copie_ponts'`) ; la lecture
    « échange » de R-585, remplacée, est refusée (elle laissait le cosinus de chaque paire plantée inchangé)."""
    if lecture != LECTURE_V4:
        raise GardeArret(f"V4 : lecture « {lecture} » refusée ; seule la lecture décidée par Lazar (R-600, addendum v2) "
                         f"est permise : lecture='{LECTURE_V4}'")
    conc, var = [], []
    for m in indices:
        w = mo.generer(condition, racine, m)
        j = mo.generer(condition, racine, m, surcharge={"jumelle": True})
        if mo.empreinte_latents(w) != mo.empreinte_latents(j):
            raise GardeArret(f"V4 : latents de la jumelle différents (monde {m})")
        L = w.latent(JETON_MESURE)
        arts = sorted({a for pl in L.plantes for a in (pl["a"], pl["b"])})
        couples = lambda o: {(a, e) for a in arts for e in o.etiq_co[a]}
        c1, c2 = couples(w.obs), couples(j.obs)
        union = c1 | c2
        conc.append(len(c1 & c2) / len(union) if union else 1.0)
        dv = [abs(w.obs.cos[pl["a"], pl["b"]] - j.obs.cos[pl["a"], pl["b"]]) for pl in L.plantes]
        var.append(float(np.mean(dv)) if dv else 0.0)
    return {"concordance": float(np.mean(conc)), "variation_cos": float(np.mean(var))}


# --- V5, V6, V8 -------------------------------------------------------------------------------------------

STATUTS_V5 = {"vrai_conceptuel": ("conceptuel",), "vrai_operateur": ("greffe", "jumeau"), "faux": ("faux",),
              "proche": ("proche",), "surface": ("surface",)}


def v5_rarete(liste_mondes):
    """Fréquence documentaire observée moyenne de l'étiquette de pont retenue, par statut, sur les paires plantées
    valides (toutes paires de tous les mondes) ; écart maximal entre statuts."""
    acc = {k: [] for k in STATUTS_V5}
    for w in liste_mondes:
        obs, L = w.obs, w.latent(JETON_MESURE)
        valides = set(obs.valides)
        for x, statut in L.plante.items():
            if x in valides:
                for k, st in STATUTS_V5.items():
                    if statut in st:
                        acc[k].append(obs.df[obs.pont[x]])
    vides = [k for k, v in acc.items() if not v]
    if vides:
        raise GardeArret(f"V5 : aucun pont planté valide pour {vides}")
    moy = {k: float(np.mean(v)) for k, v in acc.items()}
    return {"moyennes": moy, "ecart_max": max(moy.values()) - min(moy.values())}


def v6_vraies_paires(liste_mondes):
    return float(np.mean([len(set(w.obs.valides) & w.latent(JETON_MESURE).vrais) for w in liste_mondes]))


def plafond_oracle(condition, racine, indices):
    """Plafond de l'oracle (S8) : précision moyenne de l'oracle sur les mondes non exclus."""
    vals = []
    for i in indices:
        w = mo.generer(condition, racine, i)
        r = ms.executer_monde(w, condition, racine, i, ["oracle"])
        if not r["exclu"]:
            vals.append(r["bras"]["oracle"]["precision"])
    return float(np.mean(vals))


def v8_rapport(liste_mondes, condition):
    """Comptes de vraies paires par mécanisme, taux d'exclusion, taux de régénération, paires valides par monde."""
    meca, excl, regen, replant, nv = Counter(), 0, 0, 0, []
    for w in liste_mondes:
        L = w.latent(JETON_MESURE)
        meca.update(ms.mecanismes_vrais(L).values())
        excl += 1 if ms.exclu(w, condition) else 0
        regen += 1 if L.tentatives > 0 else 0
        replant += 1 if L.replantations > 0 else 0
        nv.append(len(w.obs.valides))
    n = len(nv)
    return {"mecanismes_par_monde": {k: v / n for k, v in meca.items()}, "taux_exclusion": excl / n,
            "taux_regeneration": regen / n, "taux_replantation": replant / n, "paires_valides_moyenne": float(np.mean(nv)), "n_mondes": n}


# --- V7 : rapport sans seuil ------------------------------------------------------------------------------

def classes_v7(w):
    """Classe de chaque paire d'articles (priorité dans l'ordre de la liste) : rapport V7, sans conséquence."""
    obs, L = w.obs, w.latent(JETON_MESURE)
    emetteurs = {}
    for r, info in L.rares.items():
        emetteurs[r] = set(info["porteurs"]) | set(info["surface"])
    cls = {}
    for x, (i, j) in enumerate(obs.paires):
        statut = L.plante.get(x)
        if statut == "conceptuel" and x in L.vrais:
            cls[x] = "vrai_conceptuel_direct"
        elif statut in ("greffe", "jumeau") and x in L.vrais:
            pl = next(p for p in L.plantes if {p["a"], p["b"]} == {i, j})
            cls[x] = "vrai_operateur_avec_trace" if pl.get("rare") is not None else "vrai_operateur_sans_trace"
        elif statut == "faux":
            cls[x] = "faux_pont"
        elif statut == "proche":
            cls[x] = "pont_proche"
        elif any(i in e and j in e for e in emetteurs.values()) and statut is None:
            cls[x] = "paire_emetteur_surface"
        elif statut is None and any(l.startswith("co:F") for l in (obs.etiq_co[i] & obs.etiq_co[j])):
            same = L.champ[L.arts[i]["dom"]] == L.champ[L.arts[j]["dom"]]
            cls[x] = "fond_partage_dans_champ" if same else "fond_partage_entre_champs"
    return cls


def v7_rapport(liste_mondes):
    acc = {}
    for w in liste_mondes:
        obs = w.obs
        v, _ = br.vecteurs_concepts(obs)
        kap = br.kappa(v)
        for x, c in classes_v7(w).items():
            i, j = obs.paires[x]
            acc.setdefault(c, {"kappa": [], "cos": []})
            acc[c]["kappa"].append(float(kap[i, j]))
            acc[c]["cos"].append(float(obs.cos[i, j]))
    out = {}
    for c, d in acc.items():
        out[c] = {m: {"n": len(v), "moyenne": float(np.mean(v)), "deciles": [float(q) for q in np.quantile(v, np.linspace(0.1, 0.9, 9))]}
                  for m, v in d.items()}
    return out


# --- V9 : essai R5 de J -----------------------------------------------------------------------------------

def v9_j_miroirs(racine, indices, fonctions=None):
    """J = (borne basse à 95 % de Δ(d1c, c) > 0) sur les miroirs de M_inertes. Ne calcule que d1c et c, jamais N ;
    ne rend que le booléen (l'estimation n'est pas rendue). `fonctions` : essais seulement. Liste d'arrêt
    (contre-lecture du code) : chaque miroir a les latents, bit à bit, du monde « bien » de validation de même indice."""
    pd, pc = [], []
    for i in indices:
        w = mo.generer("M_inertes", racine, i)
        ms.verifier_inertes(mo.generer("M_bien", racine, i), w)
        r = ms.executer_monde(w, "M_inertes", racine, i, ["d1c", "c"], fonctions=fonctions)
        if not r["exclu"]:
            pd.append(r["bras"]["d1c"]["precision"])
            pc.append(r["bras"]["c"]["precision"])
    res = ms.ecart_apparie(pd, pc, ms.rng_contraste(racine, gr.CODES_CONDITION["M_inertes"], 9))
    return bool(res["lb95"] > SEUIL_J)


# --- seuils -----------------------------------------------------------------------------------------------

def evaluer_seuils(r):
    """V1 à V6 et plafond de l'oracle contre S13 et S8. `r` : résultats par condition (« M_bien », « M_moyen »)."""
    ok = {}
    for cond in ("M_bien", "M_moyen"):
        v1 = r[cond]["V1"]
        ok[f"V1_{cond}"] = (S13["V1_meme"][0] <= v1["meme"] <= S13["V1_meme"][1]
                            and S13["V1_proche"][0] <= v1["proche"] <= S13["V1_proche"][1]
                            and S13["V1_eloigne"][0] <= v1["eloigne"] <= S13["V1_eloigne"][1])
        ok[f"S8_{cond}"] = r[cond]["plafond_oracle"] >= ms.PLAFOND_ORACLE_S8
    ok["V2_M_bien"] = r["M_bien"]["V2"]["F"] <= S13["V2"]
    ok["V3_M_bien"] = r["M_bien"]["V3"] <= S13["V3"]
    ok["V4"] = (r["jumelles"]["concordance"] >= S13["V4_concordance"]
                and r["jumelles"]["variation_cos"] >= S13["V4_variation"])
    ok["V5_M_bien"] = r["M_bien"]["V5"]["ecart_max"] <= S13["V5"]
    ok["V6_M_moyen"] = r["M_moyen"]["V6"] >= S13["V6"]
    return ok


def executer_validation(racine=gr.RACINE_VALIDATION, lecture_v4=None):
    """Validation complète (300 « bien », 300 « moyen », 100 jumelles, 300 miroirs). NON LANCÉE par l'auteur du code."""
    ms.verifier_racine(racine, decision=False)
    idx = range(300)
    r = {}
    for cond in ("M_bien", "M_moyen"):
        ws = list(mondes(cond, racine, idx))
        r[cond] = {"V1": v1_cosinus(ws), "V3": v3_queue(ws), "V5": v5_rarete(ws), "V6": v6_vraies_paires(ws),
                   "V7": v7_rapport(ws), "V8": v8_rapport(ws, cond), "plafond_oracle": plafond_oracle(cond, racine, idx)}
        if cond == "M_bien":
            r[cond]["V2"] = v2_fuite(ws, racine, 0)
    r["jumelles"] = v4_jumelles(racine, range(100), lecture=lecture_v4)
    r["V9_J_vraie"] = v9_j_miroirs(racine, idx)
    r["seuils"] = evaluer_seuils(r)
    return r


def main(argv):
    """python3 -B validation_v2.py SORTIE.json --lancer-la-validation --lecture-v4 copie_ponts
    Refuse de partir sans l'option explicite : la validation n'est pas lancée par l'auteur du code."""
    import json
    from datetime import datetime, timezone

    from controle_ia.scellement import sceller

    if "--lancer-la-validation" not in argv:
        raise GardeArret("validation non lancée : option --lancer-la-validation absente")
    import invocation_unique_v2 as inv
    inv.exiger_addendum_scelle(inv.DEPOT)   # addendum d'écarts (R-600) scellé avant la validation
    lecture = argv[argv.index("--lecture-v4") + 1] if "--lecture-v4" in argv else None
    r = executer_validation(lecture_v4=lecture)
    r["ecrit_le"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    r["empreintes_code"] = ms.empreintes_code()
    sortie = Path(argv[1])
    sortie.write_text(json.dumps(r, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(sortie)
    print("seuils :", r["seuils"], "; V9 J vraie :", r["V9_J_vraie"])
    return 0 if all(r["seuils"].values()) else 2


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
