#!/usr/bin/env python3
"""EXPLORATOIRE, NON PRÉENREGISTRÉ, NON OPPOSABLE (R7). Processeur seul, aucune dépense, aucun réseau.

Reproduction, sur un monde synthétique, de la borne de boucle de « Pay Only for Disagreement » (arXiv 2609.17560v1,
protocole Discern), proposition 13 (p.12), avant tout emprunt dans la revendication Q2. Mot de Lazar du 29 octobre 2026,
02:29 heure de Paris : « go ». Seule source sur le papier : `../corpus-primaire-v2/extrait-2609.17560-v1.md`.

Lancement : `python3 -I -B reproduction-v1.py` depuis ce dossier (ou n'importe où : les chemins partent du script).
Sorties : `reproduction-v1-sortie.json`, `manifeste-v1.json` (dans ce dossier).

Monde (repris de l'extrait, p.7-8, sauf mention [INFÉRÉ]) :
- perte 0/1, B = 1 ; D_t = perte(candidat) − perte(titulaire) ∈ {−1 ; 0 ; 1} ; Δ = E[D_t] ; Δ > 0 = régression (p.7) ;
- verdict Safe(ε) : affirme Δ < ε (p.8) ; une **fausse certification** = Safe(ε) émis pour un candidat de Δ ≥ ε ;
- [INFÉRÉ] classification binaire : désaccord A_t = 1 ⇔ une seule des deux prédictions est juste ⇔ D_t ≠ 0 (lemme 2, p.7) ;
- [INFÉRÉ] titulaire juste avec probabilité 0,70 ; taux de désaccord ρ = 0,20 ; ε = 0,05 ; nulle « de bord » Δ = ε
  (le pire cas de l'hypothèse nulle Δ ≥ ε) ; « bon » candidat Δ = −0,03 ; nulle « signe inversé » Δ = +0,15 ;
- e-processus : **notre** `pole.pari_apparie.trajectoire_log_richesse` (mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}), appliqué à
  v_t = (ε − Z_t)/(c + ε) ∈ [−1 ; 1], c = borne de |Z_t| (1 sans acheminement, 1/π_min avec) ; sous Δ ≥ ε, E[v_t | passé] ≤ 0,
  donc la richesse est une surmartingale positive (inégalité de Ville) ; certification au premier instant où la richesse
  atteint 1/δ_k. **Écart à l'extrait** : Discern utilise une suite de confiance empirique de Bernstein à substitution
  prévisible (Waudby-Smith et Ramdas 2024, forme à l'annexe A, p.8, non extraite), bilatérale, avec les deux verdicts ; ici
  un test unilatéral du seul verdict Safe(ε), au niveau δ_k entier [INFÉRÉ]. La question testée (validité familiale par
  union) ne dépend que de la validité de chaque audit, que les deux constructions partagent (Ville).
- Tier 0 (certificat sans étiquette, p.8) omis : ρ = 0,20 ≫ ε/B = 0,05, il ne peut jamais se déclencher ; δ0 = 0, δ1 = δ_k.

La version vectorisée de l'e-processus est vérifiée égale à `trajectoire_log_richesse` (écart rapporté dans la sortie).
Graines : `numpy.random.SeedSequence(20261029).spawn(n)`, une graine fille par cellule, dans l'ordre fixe de `CELLULES`.
"""

import hashlib
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
POLE = ICI.parent / "orchestrateur-pole-v7"
sys.path.insert(0, str(POLE))
from pole import pari_apparie as pa  # noqa: E402  (nos briques : trajectoire_log_richesse, ebh_pondere)

GRAINE = 20261029
DELTA = 0.05          # δ_seq (p.12)
K = 20                # audits par suite
EPS = 0.05            # tolérance ε de Safe(ε) (p.8) [INFÉRÉ : valeur]
S_F = 0.70            # exactitude du titulaire [INFÉRÉ]
RHO = 0.20            # taux de désaccord [INFÉRÉ]
LAMBDAS = pa.LAMBDAS
R = 2000              # répétitions par cellule (consigne)
R_RECAL = 400         # répétitions des cellules à 420 audits par suite (remède ii-b)
R_E3 = 500
T_FRAIS = 3000        # plafond de trafic frais par audit (pas de verdict au-delà) [INFÉRÉ]
T_E3 = 20000
PI_MIN = 0.5          # plancher d'acheminement (p.9 ; valeurs 0,1 ; 0,25 ; 0,5 essayées p.21)
BIAIS_JUGE = 0.10     # +0,1 de probabilité de compter juste une réponse fausse d'un candidat « lissé » (consigne)
ERREUR_SYM = 0.10     # juge bruité symétrique (E3)
L_DETECT = 20         # nulles de bibliothèque, détection (10 de bord, 10 inversées)
L_RECAL_BORD, L_RECAL_INV = 380, 20   # recalibrage : K/(K+380) = 0,05
DATE = "2026-10-29"

FICHIERS_LUS = [
    ICI.parent / "corpus-primaire-v2" / "extrait-2609.17560-v1.md",
    POLE / "pole" / "porte_pace.py",
    POLE / "pole" / "pari_apparie.py",
    ICI.parent / "ideation-organisme-approches-v1" / "note-porte-pace-bras-de-reference-v1.md",
    ICI.parent / "anteriorite-sept-questions-v1" / "anteriorite-Q2-v2.md",
]


class Type:
    """Type de candidat : P(désaccord | titulaire juste) = a1, P(désaccord | titulaire faux) = a0."""

    def __init__(self, nom, delta_pop, rho=RHO, s_f=S_F):
        p_plus, p_moins = (rho + delta_pop) / 2, (rho - delta_pop) / 2
        self.nom, self.delta, self.rho = nom, delta_pop, rho
        self.p_plus, self.p_moins = p_plus, p_moins
        self.a1, self.a0 = p_plus / s_f, p_moins / (1 - s_f)
        assert 0 <= self.a1 <= 1 and 0 <= self.a0 <= 1
        self.s_g = s_f - delta_pop  # exactitude du candidat

    def info(self):
        return {"nom": self.nom, "Delta": self.delta, "rho": self.rho, "P(D=+1)": self.p_plus, "P(D=-1)": self.p_moins,
                "a1": self.a1, "a0": self.a0, "exactitude": self.s_g}


NUL = Type("nulle de bord", EPS)
BON = Type("bon", -0.03)
INV = Type("nulle signe inverse", 0.15)


def calendrier(nom):
    if nom == "egal":
        return np.full(K, DELTA / K)
    if nom == "k2":   # δ_k = δ·6/(π² k²) : somme sur k ≥ 1 égale à δ (suite non bornée, p.12)
        return DELTA * 6 / (math.pi ** 2 * np.arange(1, K + 1) ** 2)
    raise ValueError(nom)


# --- e-processus vectorisé (équivalent à pa.trajectoire_log_richesse) ------------------------------------------------

def _melange(lws, m):
    """Même formule que `pa.trajectoire_log_richesse` : m + log(Σ exp(lw − m)/|Λ|), m = max sur Λ."""
    s = np.zeros_like(m)
    for lw in lws:
        s += np.exp(lw - m)
    return m + np.log(s / len(lws))


def trajectoires(v):
    lws = [np.cumsum(np.log1p(l * v), axis=1) for l in LAMBDAS]
    m = lws[0].copy()
    for lw in lws[1:]:
        np.maximum(m, lw, out=m)
    return _melange(lws, m)


def eproc(v, seuil_log, etiq=None, besoin_pic=False):
    """Lecture à tout instant : certification au premier t où log W_t ≥ seuil. Rend certifié, instant d'arrêt (lu jusqu'à
    t ; T sans verdict), pic de log W (exact seulement si `besoin_pic` ou si la ligne a pu franchir ; NaN sinon), log W à
    l'arrêt, étiquettes lues jusqu'à l'arrêt. Élagage exact : le mélange (une moyenne) ne dépasse jamais le maximum sur Λ,
    donc une ligne dont le maximum n'atteint jamais le seuil ne peut pas franchir ; le mélange n'est calculé que sur les
    autres lignes, et à la dernière colonne pour toutes."""
    n_r, t_max = v.shape
    seuil = np.broadcast_to(np.asarray(seuil_log, dtype=float), (n_r,))
    out = {"cert": np.zeros(n_r, bool), "t": np.full(n_r, t_max), "pic": np.full(n_r, np.nan),
           "log_arret": np.empty(n_r), "etiq": np.zeros(n_r)}
    pas = max(1, int(2_000_000 // t_max))
    for a in range(0, n_r, pas):
        b = min(n_r, a + pas)
        lws = [np.cumsum(np.log1p(l * v[a:b]), axis=1) for l in LAMBDAS]
        m = lws[0].copy()
        for lw in lws[1:]:
            np.maximum(m, lw, out=m)
        fin = _melange([lw[:, -1:] for lw in lws], m[:, -1:])[:, 0]
        if besoin_pic:
            lignes = np.arange(b - a)
        else:
            lignes = np.where((m >= seuil[a:b, None] - 1e-12).any(1))[0]
        t = np.full(b - a, t_max)
        log_arret = fin.copy()
        cert = np.zeros(b - a, bool)
        if lignes.size:
            mix = _melange([lw[lignes] for lw in lws], m[lignes])
            hit = mix >= (seuil[a:b][lignes, None] - 1e-12)
            c = hit.any(1)
            tl = np.where(c, hit.argmax(1) + 1, t_max)
            cert[lignes], t[lignes] = c, tl
            log_arret[lignes] = np.take_along_axis(mix, (tl - 1)[:, None], 1)[:, 0]
            out["pic"][a + lignes] = mix.max(1)
        out["cert"][a:b], out["t"][a:b], out["log_arret"][a:b] = cert, t, log_arret
        if etiq is not None:
            out["etiq"][a:b] = np.take_along_axis(np.cumsum(etiq[a:b], 1), (t - 1)[:, None], 1)[:, 0]
    return out


def v_de(z, c=1.0):
    return (EPS - z) / (c + EPS)


# --- tirages ------------------------------------------------------------------------------------------------------------

def frais(rng, typ, n_r, t):
    u = rng.random((n_r, t))
    return np.where(u < typ.p_plus, 1, np.where(u < typ.p_plus + typ.p_moins, -1, 0)).astype(np.int8)


def tirer_cf(rng, n_r, n):
    return rng.random((n_r, n)) < S_F


def flips(rng, cf, a1, a0):
    a1 = np.broadcast_to(np.asarray(a1, float), (cf.shape[0],))[:, None]
    a0 = np.broadcast_to(np.asarray(a0, float), (cf.shape[0],))[:, None]
    return rng.random(cf.shape) < np.where(cf, a1, a0)


def placer(rng, cf, k1, k0):
    """Désaccords uniformes : k1 parmi les points où le titulaire est juste, k0 parmi ceux où il est faux (loi exacte
    d'un candidat à basculements indépendants, conditionnée à ses comptes)."""
    n_r, n = cf.shape
    cles = rng.random((n_r, n)) + 2.0 * (~cf)
    ordre = np.argsort(cles, axis=1, kind="stable")
    rang = np.empty_like(ordre)
    np.put_along_axis(rang, ordre, np.broadcast_to(np.arange(n), (n_r, n)), axis=1)
    n1 = cf.sum(1)
    dedans = np.where(cf, rang, rang - n1[:, None])
    return np.where(cf, dedans < k1[:, None], dedans < k0[:, None])


def meilleur_de_m(rng, cf, a1, a0, m):
    """La boucle tire m variantes du même type et soumet celle dont la moyenne de D sur tout le jeu réutilisé est la plus
    basse (la plus flatteuse). Comptes par binomiales, puis placement exact."""
    n_r, n = cf.shape
    n1 = cf.sum(1)
    a1 = np.broadcast_to(np.asarray(a1, float), (n_r,))[:, None]
    a0 = np.broadcast_to(np.asarray(a0, float), (n_r,))[:, None]
    k1 = rng.binomial(n1[:, None], a1, size=(n_r, m))
    k0 = rng.binomial((n - n1)[:, None], a0, size=(n_r, m))
    j = np.argmin(k1 - k0, axis=1)
    ii = np.arange(n_r)
    return placer(rng, cf, k1[ii, j], k0[ii, j])


# --- déroulement d'une suite sur un jeu réutilisé ------------------------------------------------------------------------

def derouler(rng, cf, etapes, boucle, m=1, lecture_complete=False):
    """`etapes` : liste de dicts {a1, a0, dans_boucle, seuil, fenetre} (tableaux par répétition ou scalaires).
    `boucle` : « fixe » (candidats non adaptatifs), « sel » (meilleur de m sur le jeu), « expl » (exploite les points
    dont l'étiquette a été achetée par un audit précédent : désaccord là où le titulaire est faux, accord là où il est
    juste ; ailleurs, basculements du type). Lecture du jeu dans un ordre fixe ; un audit lit le préfixe jusqu'à son
    verdict (tout le jeu sans verdict, ou si `lecture_complete`)."""
    n_r, n = cf.shape
    connu = np.zeros_like(cf)
    sortie = []
    for e in etapes:
        s, f = e.get("fenetre") or (0, n)
        cfw = cf[:, s:f]
        dans = np.broadcast_to(np.asarray(e["dans_boucle"], bool), (n_r,))
        a_libre = flips(rng, cfw, e["a1"], e["a0"])
        if boucle == "sel" and dans.any():
            a_sel = meilleur_de_m(rng, cfw, e["a1"], e["a0"], m)
            a = np.where(dans[:, None], a_sel, a_libre)
        elif boucle == "expl":
            a_expl = np.where(connu[:, s:f], ~cfw, a_libre)
            a = np.where(dans[:, None], a_expl, a_libre)
        else:
            a = a_libre
        d = a.astype(np.int8) * (2 * cfw.astype(np.int8) - 1)
        r = eproc(v_de(d), e["seuil"], etiq=a, besoin_pic=lecture_complete)
        lu = np.full(n_r, f - s) if lecture_complete else r["t"]
        connu[:, s:f] |= a & (np.arange(f - s)[None, :] < lu[:, None])
        sortie.append(r)
    return {cle: np.stack([r[cle] for r in sortie]) for cle in sortie[0]}  # (étapes, R)


def etapes_simples(typ, deltas, mult=1.0, dans_boucle=True):
    return [{"a1": typ.a1, "a0": typ.a0, "dans_boucle": dans_boucle, "seuil": math.log(mult / dk)} for dk in deltas]


def suite_fraiche(rng, typ, deltas, n_r=R, t=T_FRAIS, mult=1.0):
    res = []
    for dk in deltas:
        d = frais(rng, typ, n_r, t)
        res.append(eproc(v_de(d), math.log(mult / dk), etiq=(d != 0)))
    return {cle: np.stack([r[cle] for r in res]) for cle in res[0]}


# --- résumés ------------------------------------------------------------------------------------------------------------

def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return [None, None]
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(max(0.0, c - h), 5), round(min(1.0, c + h), 5)]


def r6(x):
    return None if x is None else round(float(x), 6)


def resume_nul(cert, borne=None, attendu=""):
    """cert : (K, R) ; fréquence des suites avec au moins une fausse certification."""
    n = cert.shape[1]
    k = int(cert.any(0).sum())
    sortie = {"suites": n, "suites_avec_fausse": k, "frequence": r6(k / n), "wilson95": wilson(k, n),
              "taux_par_audit_moyen": r6(cert.mean()), "taux_par_audit": [r6(x) for x in cert.mean(1)],
              "attendu": attendu, "borne": borne, "garde_R4": None}
    if borne is not None:
        if k == 0:
            sortie["garde_R4"] = f"TROP PROPRE : 0 fausse certification sur {n} suites (borne {borne})"
        elif sortie["wilson95"][0] > borne:
            sortie["garde_R4"] = f"BORNE DÉPASSÉE : borne basse de Wilson {sortie['wilson95'][0]} > {borne}"
    return sortie


def resume_bon(res):
    cert = res["cert"]
    tm = np.where(cert, res["t"], np.nan)
    em = np.where(cert, res["etiq"], np.nan)
    with np.errstate(all="ignore"):
        par_k_e = np.nanmean(em, axis=1)
        par_k_t = np.nanmean(tm, axis=1)
    return {"puissance": r6(cert.mean()), "puissance_par_audit": [r6(x) for x in cert.mean(1)],
            "etiquettes_moyennes_a_la_certification": r6(np.nanmean(em)) if cert.any() else None,
            "trafic_moyen_a_la_certification": r6(np.nanmean(tm)) if cert.any() else None,
            "etiquettes_par_audit": [None if math.isnan(x) else r6(x) for x in par_k_e],
            "trafic_par_audit": [None if math.isnan(x) else r6(x) for x in par_k_t],
            "points_lus_moyens_par_audit_tous": r6(res["t"].mean()),
            "etiquettes_lues_moyennes_par_audit_toutes": r6(res["etiq"].mean())}


def ajustement_log(deltas, etiq_par_k):
    x = np.log(1 / np.asarray(deltas))
    y = np.asarray([np.nan if e is None else e for e in etiq_par_k], float)
    ok = ~np.isnan(y)
    pente, ordonnee = np.polyfit(x[ok], y[ok], 1)
    pred = pente * x[ok] + ordonnee
    r2 = 1 - ((y[ok] - pred) ** 2).sum() / ((y[ok] - y[ok].mean()) ** 2).sum()
    return {"pente_etiquettes_par_unite_de_log_1_sur_delta_k": r6(pente), "ordonnee": r6(ordonnee), "R2": r6(r2),
            "log_1_sur_delta_k": [r6(v) for v in x]}


# --- cellules -----------------------------------------------------------------------------------------------------------

B_UNION = DELTA


def cellule_A(rng, sched, typ):
    res = suite_fraiche(rng, typ, calendrier(sched))
    if typ is NUL:
        return resume_nul(res["cert"], B_UNION, "≤ 0,05 (proposition 13, p.12)")
    out = resume_bon(res)
    if sched == "k2":
        out["cout_contre_log"] = ajustement_log(calendrier(sched), out["etiquettes_par_audit"])
    return out


def cellule_B(rng, n, sched, typ):
    cf = tirer_cf(rng, R, n)
    res = derouler(rng, cf, etapes_simples(typ, calendrier(sched)), "fixe")
    if typ is NUL:
        return resume_nul(res["cert"], B_UNION, "≤ 0,05 (commentaire de la proposition 13, p.12 : union sans indépendance)")
    return resume_bon(res)


def cellule_C_sel(rng, n, m, typ, mult=1.0, n_r=R):
    cf = tirer_cf(rng, n_r, n)
    res = derouler(rng, cf, etapes_simples(typ, calendrier("egal"), mult), "sel", m=m)
    return res


def cellule_C_expl(rng, n, typ, mult=1.0, n_r=R):
    cf = tirer_cf(rng, n_r, n)
    return derouler(rng, cf, etapes_simples(typ, calendrier("egal"), mult), "expl")


def ebh_suite(rng, boucle, n, typ, m=1):
    """Remède iii-b : e-valeurs arrêtées au premier franchissement de K/δ (temps d'arrêt), lecture e-BH pondérée
    (`pa.ebh_pondere`, budgets δ/K) sur la suite entière."""
    cf = tirer_cf(rng, R, n)
    et = [{"a1": typ.a1, "a0": typ.a0, "dans_boucle": True, "seuil": math.log(K / DELTA)} for _ in range(K)]
    res = derouler(rng, cf, et, boucle, m=m)
    cert = np.zeros((K, R), bool)
    budgets = {k: DELTA / K for k in range(K)}
    for r in range(R):
        retenues = pa.ebh_pondere({k: float(res["log_arret"][k, r]) for k in range(K)}, budgets, DELTA)
        for k in retenues:
            cert[k, r] = True
    res["cert"] = cert
    return res


def interleaves(rng, n_r, roles_compte):
    """Ordre aléatoire par répétition des rôles (0 = réel, 1 = bibliothèque de bord, 2 = bibliothèque inversée)."""
    base = np.concatenate([np.full(c, role) for role, c in roles_compte])
    return np.stack([rng.permutation(base) for _ in range(n_r)], axis=1)  # (S, R)


def detection(rng, boucle, n, m, lib_dans_boucle):
    """Remède ii-a : 20 nulles de bibliothèque (10 de bord, 10 inversées) mêlées aux 20 réels nuls, ordre aléatoire,
    soumises à l'aveugle ; seuil des nulles log(L/δ) (somme des niveaux = δ) ; alarme si au moins une est certifiée."""
    roles = interleaves(rng, R, [(0, K), (1, L_DETECT // 2), (2, L_DETECT // 2)])
    cf = tirer_cf(rng, R, n)
    rang_reel = np.cumsum(roles == 0, axis=0) - 1  # indice k du réel à cette étape
    deltas = calendrier("egal")
    etapes = []
    for s in range(roles.shape[0]):
        ro = roles[s]
        a1 = np.where(ro == 0, NUL.a1, np.where(ro == 1, NUL.a1, INV.a1))
        a0 = np.where(ro == 0, NUL.a0, np.where(ro == 1, NUL.a0, INV.a0))
        seuil = np.where(ro == 0, np.log(1 / deltas[np.clip(rang_reel[s], 0, K - 1)]), math.log(L_DETECT / DELTA))
        dans = (ro == 0) | lib_dans_boucle
        etapes.append({"a1": a1, "a0": a0, "dans_boucle": dans, "seuil": seuil})
    res = derouler(rng, cf, etapes, boucle, m=m)
    cert = res["cert"]
    reel = np.zeros((K, R), bool)
    for r in range(R):
        reel[:, r] = cert[roles[:, r] == 0, r]
    alarme = ((cert & (roles != 0)).any(0))
    alarme_bord = ((cert & (roles == 1)).any(0))
    inv = (cert & (roles == 2)).any(0)
    n_a = int(alarme.sum())
    return {"reels_nuls": resume_nul(reel, None, "inchangé : la détection ne corrige pas"),
            "alarme": {"suites": R, "suites_en_alarme": n_a, "frequence": r6(n_a / R), "wilson95": wilson(n_a, R),
                       "alarme_par_nulle_de_bord": r6(alarme_bord.mean()), "nulle_inversee_certifiee": r6(inv.mean()),
                       "borne_sans_adaptation": DELTA / 2}}


def recalibrage(rng, boucle, n, m, typ_reel):
    """Remède ii-b : 380 nulles de bord + 20 inversées passées par la même boucle, à l'aveugle, ordre aléatoire ; lecture
    complète de chaque audit (pic de log W) ; seuil d'un réel = max(log(1/δ_k), max des pics des nulles de bord) ; un réel
    est certifié si son pic dépasse strictement ce seuil. Échangeabilité : P(un des K réels nuls dépasse le max des L) ≤
    K/(K+L) = 0,05 [INFÉRÉ : argument conformal, non dans l'extrait]."""
    n_r = R_RECAL
    roles = interleaves(rng, n_r, [(0, K), (1, L_RECAL_BORD), (2, L_RECAL_INV)])
    cf = tirer_cf(rng, n_r, n)
    rang_reel = np.cumsum(roles == 0, axis=0) - 1
    etapes = []
    for s in range(roles.shape[0]):
        ro = roles[s]
        a1 = np.where(ro == 0, typ_reel.a1, np.where(ro == 1, NUL.a1, INV.a1))
        a0 = np.where(ro == 0, typ_reel.a0, np.where(ro == 1, NUL.a0, INV.a0))
        etapes.append({"a1": a1, "a0": a0, "dans_boucle": True, "seuil": math.inf})
    res = derouler(rng, cf, etapes, boucle, m=m, lecture_complete=True)
    pic = res["pic"]
    t_lib = np.where(roles == 1, pic, -np.inf).max(0)  # (R,)
    deltas = calendrier("egal")
    cert = np.zeros((K, n_r), bool)
    etiq_tot = res["etiq"].sum(0)  # toutes les étiquettes de la suite, bibliothèque comprise
    for r in range(n_r):
        idx = np.where(roles[:, r] == 0)[0]
        seuil = np.maximum(t_lib[r], np.log(1 / deltas))
        cert[:, r] = pic[idx, r] > seuil
    inv = (np.where(roles == 2, pic, -np.inf) > t_lib[None, :]).any(0)
    return cert, {"nulle_inversee_au_dessus_du_seuil": r6(inv.mean()),
                  "seuil_recalibre_moyen_log": r6(t_lib.mean()), "seuil_nominal_log": r6(math.log(K / DELTA)),
                  "points_lus_par_audit_reel_bibliotheque_comprise": r6(n * roles.shape[0] / K),
                  "desaccords_lus_par_audit_reel_bibliotheque_comprise": r6(etiq_tot.mean() / K)}


def cellule_E(rng, mode, typ, n_r=R, t=T_FRAIS):
    """E1 « verdict » : le juge fournit le verdict (biais favorable au candidat lissé) ; E2 « acheminement » : le même juge
    ne choisit que les désaccords à étiqueter, l'étiquette reste vraie, pondération de Horvitz-Thompson (p.9) ; E3
    « symetrique » : juge bruité symétrique, non lissé (sorties identiques sur les accords)."""
    deltas = calendrier("egal")
    res = []
    for dk in deltas:
        cf = rng.random((n_r, t)) < S_F
        a = flips(rng, cf, typ.a1, typ.a0)
        cg = cf ^ a
        if mode == "verdict":
            cg_j = cg | (rng.random((n_r, t)) < BIAIS_JUGE)       # réponse fausse comptée juste avec prob. 0,1
            z = cf.astype(np.int8) - cg_j.astype(np.int8)          # titulaire jugé sans erreur [INFÉRÉ]
            res.append(eproc(v_de(z), math.log(1 / dk), etiq=np.zeros_like(a)))
        elif mode == "acheminement":
            cg_j = cg | (rng.random((n_r, t)) < BIAIS_JUGE)
            pi = np.where(cg_j, 1.0, PI_MIN)                       # étiqueter là où le juge croit le candidat juste
            lab = (rng.random((n_r, t)) < pi) & a
            d = a.astype(np.int8) * (2 * cf.astype(np.int8) - 1)
            z = np.where(lab, d / pi, 0.0)
            res.append(eproc(v_de(z, c=1.0 / PI_MIN), math.log(1 / dk), etiq=lab))
        elif mode == "symetrique":
            ef = rng.random((n_r, t)) < ERREUR_SYM
            eg = rng.random((n_r, t)) < ERREUR_SYM
            z = np.where(a, (cf ^ ef).astype(np.int8) - (cg ^ eg).astype(np.int8), 0)
            res.append(eproc(v_de(z), math.log(1 / dk), etiq=np.zeros_like(a)))
        else:
            raise ValueError(mode)
    return {cle: np.stack([r[cle] for r in res]) for cle in res[0]}


def delta_juge(mode, typ):
    if mode == "verdict":
        return typ.delta - BIAIS_JUGE * (1 - typ.s_g)
    if mode == "symetrique":
        return (1 - 2 * ERREUR_SYM) * typ.delta
    return typ.delta


# --- vérification de l'équivalence avec la brique ------------------------------------------------------------------------

def verifier_brique(rng):
    ecart = 0.0
    for typ in (NUL, BON, INV):
        d = frais(rng, typ, 4, 400)
        mix = trajectoires(v_de(d))
        for i in range(4):
            ref = pa.trajectoire_log_richesse([float(x) for x in v_de(d[i])], LAMBDAS)
            ecart = max(ecart, float(np.max(np.abs(np.asarray(ref) - mix[i]))))
    z = np.where(rng.random((4, 400)) < 0.2, rng.choice([-2.0, -1.0, 1.0, 2.0], (4, 400)), 0.0)
    mix = trajectoires(v_de(z, 2.0))
    for i in range(4):
        ref = pa.trajectoire_log_richesse([float(x) for x in v_de(z[i], 2.0)], LAMBDAS)
        ecart = max(ecart, float(np.max(np.abs(np.asarray(ref) - mix[i]))))
    # instants de franchissement (avec élagage) contre un balayage de la brique, seuil bas pour avoir des franchissements
    identiques = True
    for typ in (NUL, BON):
        d = frais(rng, typ, 40, 600)
        r = eproc(v_de(d), math.log(1 / 0.2))
        for i in range(40):
            ref = pa.trajectoire_log_richesse([float(x) for x in v_de(d[i])], LAMBDAS)
            t_ref = next((t + 1 for t, lw in enumerate(ref) if lw >= math.log(1 / 0.2) - 1e-12), None)
            identiques &= (t_ref is not None) == bool(r["cert"][i]) and (t_ref is None or t_ref == int(r["t"][i]))
    return ecart, bool(identiques)


# --- programme ----------------------------------------------------------------------------------------------------------

CELLULES = [
    "verif_brique",
    "A_egal_nul", "A_k2_nul", "A_egal_bon", "A_k2_bon",
    "B_500_egal_nul", "B_2000_egal_nul", "B_2000_k2_nul", "B_500_egal_bon", "B_2000_egal_bon", "B_2000_k2_bon",
    "C_sel_m5_500", "C_sel_m20_500", "C_sel_m100_500", "C_sel_m5_2000", "C_sel_m20_2000", "C_sel_m100_2000",
    "C_sel_m20_2000_bon", "C_expl_500", "C_expl_2000", "C_expl_2000_bon",
    "D_sel_i_nul", "D_sel_i_bon", "D_expl_i_nul", "D_expl_i_bon",
    "D_controle_iia_B", "D_sel_iia_boucle", "D_sel_iia_figee", "D_expl_iia_boucle", "D_expl_iia_figee",
    "D_sel_iib_nul", "D_sel_iib_bon", "D_expl_iib_nul", "D_expl_iib_bon",
    "D_sel_iiia_nul", "D_sel_iiia_bon", "D_expl_iiia_nul", "D_expl_iiia_bon",
    "D_sel_iiib_nul", "D_sel_iiib_bon", "D_expl_iiib_nul", "D_expl_iiib_bon",
    "D_sel_iv_nul", "D_sel_iv_bon", "D_expl_iv_nul", "D_expl_iv_bon",
    "E1_verdict_nul", "E1_verdict_bon", "E2_acheminement_nul", "E2_acheminement_bon", "E3_symetrique_nul",
]


def parts_etapes(typ, n):
    p = n // K
    deltas = calendrier("egal")
    return [{"a1": typ.a1, "a0": typ.a0, "dans_boucle": True, "seuil": math.log(1 / deltas[k]),
             "fenetre": (k * p, (k + 1) * p)} for k in range(K)]


def _cellule_sel(nom, rng):
    _, _, mm, n = nom.split("_")
    m, n = int(mm[1:]), int(n)
    r = cellule_C_sel(rng, n, m, NUL)
    out = resume_nul(r["cert"], None, "gonflement attendu [INFÉRÉ] ; par audit ≤ m·δ_k (union sur les m variantes)")
    out["borne_union_sur_variantes_par_audit"] = min(1.0, m * DELTA / K)
    out["borne_union_sur_variantes_suite"] = min(1.0, m * DELTA)
    return out


def _d_i(mec, typ, rng):
    # D (i) audit sur trafic neuf : la variante choisie (ou construite) sur l'ancien jeu se comporte, sur des points neufs,
    # comme son type (basculements indépendants ; points mémorisés absents du trafic neuf) : on tire donc le trafic neuf
    # du type, plafonné à n = 2000 points par audit.
    r = suite_fraiche(rng, typ, calendrier("egal"), t=2000)
    if typ is NUL:
        return resume_nul(r["cert"], B_UNION, "≤ 0,05 (trafic frais : proposition 13)")
    out = resume_bon(r)
    out["donnees_neuves_par_suite"] = r6(r["t"].sum(0).mean())
    return out


def _d_iib(mec, typ, rng):
    cert, info = recalibrage(rng, mec, 2000, 20, typ)
    if typ is NUL:
        out = resume_nul(cert, round(K / (K + L_RECAL_BORD), 6), "≤ K/(K+L) = 0,05 (échangeabilité) [INFÉRÉ]")
    else:
        out = {"puissance": r6(cert.mean()), "puissance_par_audit": [r6(x) for x in cert.mean(1)], "suites": R_RECAL}
    out.update(info)
    return out


def _d_iiia(mec, typ, rng):
    # seuil multiplié par m = 20
    if mec == "sel":
        r = cellule_C_sel(rng, 2000, 20, typ, mult=20.0)
    else:
        r = cellule_C_expl(rng, 2000, typ, mult=20.0)
    if typ is BON:
        return resume_bon(r)
    if mec == "sel":
        return resume_nul(r["cert"], B_UNION, "≤ 0,05 si la sélection porte sur m variantes tirées sans le jeu [INFÉRÉ]")
    return resume_nul(r["cert"], None, "aucune borne : la construction n'a pas de m fini [INFÉRÉ]")


def _d_iiib(mec, typ, rng):
    r = ebh_suite(rng, mec, 2000, typ, m=20 if mec == "sel" else 1)
    if typ is BON:
        return resume_bon(r)
    return resume_nul(r["cert"], None, "e-BH exige des e-valeurs valides : gonflement attendu [INFÉRÉ]")


def _d_iv(mec, typ, rng):
    # jeu figé coupé en K parts de n/K = 100 points jamais réutilisées. Sélection : sur les parts déjà révélées (< k),
    # indépendante des basculements de la part k : basculements du type sur la part k. Exploitation : les points connus
    # sont hors de la part k (construction appliquée, sans effet).
    cf = tirer_cf(rng, R, 2000)
    et = parts_etapes(typ, 2000)
    if mec == "sel":
        for e in et:
            e["dans_boucle"] = False
    r = derouler(rng, cf, et, "expl" if mec == "expl" else "fixe")
    return resume_nul(r["cert"], B_UNION, "≤ 0,05 (parts fraîches)") if typ is NUL else resume_bon(r)


def _e1_nul(rng):
    r = cellule_E(rng, "verdict", NUL)
    out = resume_nul(r["cert"], None, "aucune borne sur la vérité : le verdict du juge vise Δ jugé [INFÉRÉ]")
    out["Delta_vrai"], out["Delta_juge"] = NUL.delta, r6(delta_juge("verdict", NUL))
    out["trafic_moyen_a_la_certification"] = r6(r["t"][r["cert"]].mean()) if r["cert"].any() else None
    return out


def _e1_bon(rng):
    out = resume_bon(cellule_E(rng, "verdict", BON))
    out["Delta_vrai"], out["Delta_juge"] = BON.delta, r6(delta_juge("verdict", BON))
    return out


def _e3(rng):
    r = cellule_E(rng, "symetrique", NUL, n_r=R_E3, t=T_E3)
    out = resume_nul(r["cert"], None, "aucune borne sur la vérité : atténuation (1 − 2e)Δ [INFÉRÉ]")
    c3000 = r["cert"] & (r["t"] <= T_FRAIS)
    out["a_3000_points"] = resume_nul(c3000, None, "même cellule lue à 3 000 points de trafic")
    out["Delta_vrai"], out["Delta_juge"] = NUL.delta, r6(delta_juge("symetrique", NUL))
    return out


def _taches():
    t = {"verif_brique": lambda rng: verifier_brique(rng)}
    for sch in ("egal", "k2"):
        for typ, suf in ((NUL, "nul"), (BON, "bon")):
            t[f"A_{sch}_{suf}"] = (lambda s, ty: lambda rng: cellule_A(rng, s, ty))(sch, typ)
    for nom, n, sch, typ in [("B_500_egal_nul", 500, "egal", NUL), ("B_2000_egal_nul", 2000, "egal", NUL),
                             ("B_2000_k2_nul", 2000, "k2", NUL), ("B_500_egal_bon", 500, "egal", BON),
                             ("B_2000_egal_bon", 2000, "egal", BON), ("B_2000_k2_bon", 2000, "k2", BON)]:
        t[nom] = (lambda n_, s, ty: lambda rng: cellule_B(rng, n_, s, ty))(n, sch, typ)
    for n in (500, 2000):
        for m in (5, 20, 100):
            nom = f"C_sel_m{m}_{n}"
            t[nom] = (lambda nm: lambda rng: _cellule_sel(nm, rng))(nom)
    t["C_sel_m20_2000_bon"] = lambda rng: resume_bon(cellule_C_sel(rng, 2000, 20, BON))
    for n in (500, 2000):
        t[f"C_expl_{n}"] = (lambda n_: lambda rng: resume_nul(cellule_C_expl(rng, n_, NUL)["cert"], None,
                                                              "gonflement attendu [INFÉRÉ]"))(n)
    t["C_expl_2000_bon"] = lambda rng: resume_bon(cellule_C_expl(rng, 2000, BON))
    for mec in ("sel", "expl"):
        for typ, suf in ((NUL, "nul"), (BON, "bon")):
            for code, f in (("i", _d_i), ("iib", _d_iib), ("iiia", _d_iiia), ("iiib", _d_iiib), ("iv", _d_iv)):
                t[f"D_{mec}_{code}_{suf}"] = (lambda f_, me, ty: lambda rng: f_(me, ty, rng))(f, mec, typ)
    t["D_controle_iia_B"] = lambda rng: detection(rng, "fixe", 2000, 1, True)
    for mec in ("sel", "expl"):
        for passage, dans in (("boucle", True), ("figee", False)):
            t[f"D_{mec}_iia_{passage}"] = (lambda me, da: lambda rng: detection(rng, me, 2000, 20, da))(mec, dans)
    t["E1_verdict_nul"] = _e1_nul
    t["E1_verdict_bon"] = _e1_bon
    t["E2_acheminement_nul"] = lambda rng: resume_nul(cellule_E(rng, "acheminement", NUL)["cert"], B_UNION,
                                                      "≤ 0,05 (théorèmes 4 et 5, p.10 ; proposition 13)")
    t["E2_acheminement_bon"] = lambda rng: resume_bon(cellule_E(rng, "acheminement", BON))
    t["E3_symetrique_nul"] = _e3
    assert set(t) == set(CELLULES), set(t) ^ set(CELLULES)
    return t


def _executer(nom):
    import time
    t0 = time.time()
    ss = np.random.SeedSequence(GRAINE).spawn(len(CELLULES))[CELLULES.index(nom)]
    valeur = _taches()[nom](np.random.Generator(np.random.PCG64(ss)))
    if nom == "verif_brique":
        valeur = {"ecart_max_avec_trajectoire_log_richesse": valeur[0], "instants_de_franchissement_identiques": valeur[1]}
    return nom, valeur, time.time() - t0


def main():
    import multiprocessing as mp
    import time
    t0 = time.time()

    def h(p):
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()

    # empreintes prises au lancement (avant les calculs), puis revérifiées à la fin
    lus_debut = {str(p.relative_to(ICI.parent)): h(p) for p in FICHIERS_LUS}
    script_debut = h(Path(__file__))
    filles = np.random.SeedSequence(GRAINE).spawn(len(CELLULES))
    lourdes = [n for n in CELLULES if "iib" in n or "iia" in n] + [n for n in CELLULES if n.startswith(("A_", "E"))]
    ordre = lourdes + [n for n in CELLULES if n not in lourdes]   # les plus lourdes d'abord (répartition)
    S = {}
    with mp.get_context("fork").Pool(2) as pool:
        for nom, valeur, duree in pool.imap_unordered(_executer, ordre):
            S[nom] = valeur
            print(f"{nom:24s} {duree:6.1f} s (cumul {time.time() - t0:6.1f} s)", flush=True)
    S = {nom: S[nom] for nom in CELLULES}   # ordre fixe, indépendant de l'ordonnancement

    sortie = {
        "statut": "EXPLORATOIRE, NON PRÉENREGISTRÉ, NON OPPOSABLE (R7)",
        "source": "arXiv 2609.17560v1, extrait ../corpus-primaire-v2/extrait-2609.17560-v1.md (proposition 13, p.12)",
        "date": DATE,
        "reglages": {"graine_maitresse": GRAINE, "delta_seq": DELTA, "K": K, "epsilon": EPS, "exactitude_titulaire": S_F,
                     "rho": RHO, "lambdas": list(LAMBDAS), "repetitions": R, "repetitions_recalibrage": R_RECAL,
                     "repetitions_E3": R_E3, "trafic_frais_max": T_FRAIS, "trafic_E3_max": T_E3, "pi_min": PI_MIN,
                     "biais_juge": BIAIS_JUGE, "erreur_symetrique": ERREUR_SYM,
                     "types": {t.nom: t.info() for t in (NUL, BON, INV)},
                     "calendriers": {"egal": [r6(x) for x in calendrier("egal")], "k2": [float(f"{x:.6e}") for x in calendrier("k2")]}},
        "cellules": S,
    }
    chemin = ICI / "reproduction-v1-sortie.json"
    texte = json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=False) + "\n"
    chemin.write_text(texte, encoding="utf-8")

    lus_fin = {str(p.relative_to(ICI.parent)): h(p) for p in FICHIERS_LUS}
    manifeste = {
        "statut": "EXPLORATOIRE, NON PRÉENREGISTRÉ, NON OPPOSABLE (R7)",
        "date": DATE,
        "commande": "python3 -I -B reproduction-v1.py",
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "pole": getattr(sys.modules.get("pole"), "__version__", None),
                     "pari_apparie_E_PROCESSUS": pa.E_PROCESSUS},
        "graines": {"maitresse": GRAINE, "methode": "numpy.random.SeedSequence(graine).spawn(n) ; PCG64 par cellule",
                    "cellules": {nom: {"spawn_key": list(ss.spawn_key), "etat": [int(x) for x in ss.generate_state(2)]}
                                 for nom, ss in zip(CELLULES, filles)}},
        "fichiers_lus": lus_debut,
        "fichiers_modifies_pendant_le_run": sorted(k for k in lus_debut if lus_debut[k] != lus_fin[k]),
        "script": {"reproduction-v1.py": script_debut},
        "sortie": {"reproduction-v1-sortie.json": hashlib.sha256(texte.encode("utf-8")).hexdigest()},
    }
    (ICI / "manifeste-v1.json").write_text(json.dumps(manifeste, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"fini en {time.time() - t0:.1f} s ; sortie {manifeste['sortie']['reproduction-v1-sortie.json']}")


if __name__ == "__main__":
    main()
