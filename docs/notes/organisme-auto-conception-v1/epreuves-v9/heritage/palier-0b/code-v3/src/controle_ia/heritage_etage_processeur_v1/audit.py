"""B1 et section « Seuil » — l'audit du générateur des mondes, écrit à part de la construction.

« L'audit ne se fie pas au générateur : il recalcule, par une fonction qui ne partage rien avec la construction, la séparation de
toutes les paires de lois, loi entière contre loi entière, au seuil inchangé de 0,25 nat. » Ce module n'importe ni `lois`, ni
`comparateur`, ni `mondes` : son évaluateur des lois (`probas_audit`) est une seconde écriture, limitée à la forme unique des
lois plantées (`par_sous_population` de deux `softmax`) et à la loi `fixe`, qui refuse toute autre forme. Il reprend la
convention de l'oracle de l'organisme (plancher 1e-12 puis renormalisation ; divergence moyenne sur les instances de l'oracle du
monde) ; l'essai l'oppose à l'oracle du comparateur à 1e-12 près.

Marges : la séparation de deux lois est la plus petite des deux divergences moyennes, d'un sens et de l'autre, sur les 4 000
instances de l'oracle du monde audité. Audit de présentation : plus proche centre de classe sur des traits centrés et réduits,
validation croisée à cinq plis, exactitude équilibrée ; trois audits (vraies contre fausses ; dépendantes contre
indépendantes ; mondes par dose, lus par paires de doses), chacun sur les traits de forme, de contenu, puis réunis : quinze
exactitudes. Celles des traits de forme décident (liste d'arrêt, point 2) ; les autres sont rapportées et lient l'étage payant.
"""

import hashlib
import itertools
import json
import re

import numpy as np

SEUIL_MARGE = 0.25
PLANCHER_AUDIT = 1e-12
EXACTITUDE_MAX = 0.55
CASES = 64
PAIRES_DE_DOSES = ((0.0, 0.25), (0.0, 0.5), (0.25, 0.5))
JEUX_DE_TRAITS = ("forme", "contenu", "reunis")


class AuditRefuse(ValueError):
    pass


# --- évaluateur indépendant ---------------------------------------------------------------------------------------------------


def _softmax_audit(sous_loi, Z):
    if set(sous_loi) != {"type", "poids", "biais"} or sous_loi["type"] != "softmax":
        raise AuditRefuse(f"audit : sous-loi hors de la forme unique : {sorted(sous_loi)}")
    W = np.array(sous_loi["poids"], dtype=np.float64)
    b = np.array(sous_loi["biais"], dtype=np.float64)
    logits = np.einsum("nd,kd->nk", Z, W) + b
    logits -= logits.max(axis=1)[:, None]
    e = np.exp(logits)
    p = e / e.sum(axis=1)[:, None]
    p = np.where(p < PLANCHER_AUDIT, PLANCHER_AUDIT, p)
    return p / p.sum(axis=1)[:, None]


def probas_audit(loi, Z, G):
    """Probabilités (N × 3) d'une loi de la forme unique, ou d'une loi fixe ; toute autre forme est refusée."""
    Z = np.asarray(Z, dtype=np.float64)
    G = np.asarray(G)
    if loi.get("type") == "fixe":
        p = np.array([max(PLANCHER_AUDIT, float(x)) for x in loi["probas"]])
        p = p / p.sum()
        return np.repeat(p[None, :], len(Z), axis=0)
    if loi.get("type") != "par_sous_population" or sorted(loi.get("lois", {})) != ["0", "1"] or "defaut" in loi:
        raise AuditRefuse("audit : loi hors de la forme unique (par_sous_population de deux softmax)")
    out = np.empty((len(Z), 3))
    for g in (0, 1):
        m = G == g
        out[m] = _softmax_audit(loi["lois"][str(g)], Z[m])
    return out


def kl_moyenne(P, Q):
    return float(np.einsum("nk,nk->n", P, np.log(P) - np.log(Q)).mean())


def separation(P, Q):
    return min(kl_moyenne(P, Q), kl_moyenne(Q, P))


def _cle(loi):
    return json.dumps(loi, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


class Probas:
    """Cache des probabilités d'audit sur les instances d'un monde (clé : texte canonique de la loi)."""

    def __init__(self, Z, G):
        self.Z, self.G, self._c = np.asarray(Z, dtype=np.float64), np.asarray(G), {}

    def __call__(self, loi):
        k = _cle(loi)
        if k not in self._c:
            self._c[k] = probas_audit(loi, self.Z, self.G)
        return self._c[k]


def _composer_audit(a, b):
    """Composition de deux lois (première sous-population de a, seconde de b), écrite ici à part."""
    return {"type": "par_sous_population", "lois": {"0": a["lois"]["0"], "1": b["lois"]["1"]}}


def audit_marges(lois_du_monde, Z, G, lois_vraies_source=(), lois_vraies_etrangere=None, seuil=SEUIL_MARGE):
    """`lois_du_monde` : {identifiant : loi plantée}. Rend la liste des manques (genre, a, b, séparation), vide si le monde
    passe : (i) toute paire de lois plantées du monde ; (ii) toute loi du monde face à toute loi vraie de la source ; (iii) pour
    B7 bis, toute loi du monde face à toute loi vraie de la source étrangère et à toute composition de deux d'entre elles, dans
    les deux sens de composition."""
    pr = Probas(Z, G)
    manques = []
    ids = sorted(lois_du_monde)
    for a, b in itertools.combinations(ids, 2):
        s = separation(pr(lois_du_monde[a]), pr(lois_du_monde[b]))
        if s < seuil:
            manques.append(("meme-monde", a, b, s))
    for a in ids:
        for j, v in enumerate(lois_vraies_source):
            s = separation(pr(lois_du_monde[a]), pr(v))
            if s < seuil:
                manques.append(("source", a, j, s))
    if lois_vraies_etrangere is not None:
        cand = [("vraie", j, v) for j, v in enumerate(lois_vraies_etrangere)]
        cand += [("composition", (p, q), _composer_audit(lois_vraies_etrangere[p], lois_vraies_etrangere[q]))
                 for p in range(len(lois_vraies_etrangere)) for q in range(len(lois_vraies_etrangere)) if p != q]
        for a in ids:
            for genre, j, c in cand:
                s = separation(pr(lois_du_monde[a]), pr(c))
                if s < seuil:
                    manques.append(("source-etrangere-" + genre, a, j, s))
    return manques


def audit_compositions_de_la_source(lois_vraies_source, Z, G, seuil=SEUIL_MARGE):
    """B1 (e) : chacune des vingt-huit compositions de deux lois vraies de la source (rang le plus petit d'abord) est séparée
    d'au moins 0,25 nat de chaque loi vraie de la source."""
    pr = Probas(Z, G)
    manques = []
    for p, q in itertools.combinations(range(len(lois_vraies_source)), 2):
        c = _composer_audit(lois_vraies_source[p], lois_vraies_source[q])
        for r, v in enumerate(lois_vraies_source):
            s = separation(pr(c), pr(v))
            if s < seuil:
                manques.append(("composition-source", (p, q), r, s))
    return manques


def ensemble_exclu_par_construction(textes_finale, textes_source):
    """Aucune loi d'un monde final identique à une loi de sa source (ensemble exclu vide par construction) : rend les textes
    communs (liste vide si le générateur est sain)."""
    return sorted(set(textes_finale) & set(textes_source))


# --- audit de présentation ------------------------------------------------------------------------------------------------------

_JETON = re.compile(r"[A-Za-z_]+|-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?|[^\sA-Za-z_\d]")


def jetons(texte):
    for j in _JETON.findall(texte):
        if j[0].isdigit() or (j[0] == "-" and len(j) > 1):
            mant = j.split("e")[0].split("E")[0]
            dec = mant.split(".")[1] if "." in mant else ""
            yield "<nombre>" if len(dec) >= 4 else j
        else:
            yield j


def traits_de_forme(texte):
    """Comptes des jetons du texte canonique répartis en 64 cases (tout nombre d'au moins quatre décimales comptant pour un même
    jeton), et la longueur du texte."""
    v = np.zeros(CASES + 1)
    for j in jetons(texte):
        v[int.from_bytes(hashlib.sha256(j.encode("utf-8")).digest()[:4], "big") % CASES] += 1
    v[CASES] = float(len(texte))
    return v


def traits_de_contenu(loi, Z, G):
    """Pour chaque sous-population : norme des poids, norme des biais, entropie moyenne de la loi (nats) sur les instances de
    l'oracle du monde dans cette sous-population."""
    P = probas_audit(loi, Z, G)
    G = np.asarray(G)
    out = []
    for g in (0, 1):
        s = loi["lois"][str(g)]
        H = -np.einsum("nk,nk->n", P[G == g], np.log(P[G == g]))
        out += [float(np.linalg.norm(np.array(s["poids"], dtype=float))), float(np.linalg.norm(np.array(s["biais"], dtype=float))),
                float(H.mean())]
    return np.array(out)


def exactitude_equilibree(X, y, rng, plis=5):
    """Plus proche centre de classe sur des traits centrés et réduits (moyenne et écart-type du pli d'entraînement), validation
    croisée à `plis` plis ; exactitude équilibrée. None si moins de deux classes ou trop peu d'exemples."""
    X, y = np.asarray(X, dtype=float), np.asarray(y)
    classes = sorted(set(y.tolist()))
    if len(classes) != 2 or len(y) < 2 * plis or min(int(np.sum(y == c)) for c in classes) < plis:
        return None
    pli = np.empty(len(y), dtype=int)
    pli[rng.permutation(len(y))] = np.arange(len(y)) % plis
    pred = np.empty(len(y), dtype=object)
    for k in range(plis):
        tr, te = pli != k, pli == k
        mu, sd = X[tr].mean(axis=0), X[tr].std(axis=0)
        sd = np.where(sd > 0, sd, 1.0)
        Xt, Xe = (X[tr] - mu) / sd, (X[te] - mu) / sd
        centres = [Xt[y[tr] == c].mean(axis=0) for c in classes]
        D = np.stack([((Xe - c) ** 2).sum(axis=1) for c in centres], axis=1)
        pred[te] = [classes[i] for i in D.argmin(axis=1)]
    return float(np.mean([np.mean(pred[y == c] == c) for c in classes]))


def audit_presentation(mondes_audites, rng):
    """`mondes_audites` : liste de dicts {"dose", "lois": [(texte canonique, loi, type, dependante)], "Z", "G"} — les mondes
    cibles et finaux des suites de la couche « audit ». Rend {jeu de traits : {audit : exactitude}} (quinze valeurs), la liste
    des exactitudes de forme au-dessus de 0,55 (`arret`) et celle des exactitudes de contenu ou réunies au-dessus de 0,55
    (`signalement`)."""
    lignes = []  # (dose, monde, type, dependante, forme, contenu)
    for k, m in enumerate(mondes_audites):
        for texte, loi, typ, dep in m["lois"]:
            lignes.append((float(m["dose"]), k, typ, bool(dep), traits_de_forme(texte), traits_de_contenu(loi, m["Z"], m["G"])))

    def X(sel, jeu):
        if jeu == "forme":
            return [l[4] for l in sel]
        if jeu == "contenu":
            return [l[5] for l in sel]
        return [np.concatenate([l[4], l[5]]) for l in sel]

    out = {}
    for jeu in JEUX_DE_TRAITS:
        r = {}
        r["vraies_contre_fausses"] = exactitude_equilibree(X(lignes, jeu), [l[2] for l in lignes], rng)
        vd = [l for l in lignes if l[2] == "vraie" and l[0] > 0]
        r["dependantes_contre_independantes"] = exactitude_equilibree(X(vd, jeu), [l[3] for l in vd], rng)
        for d1, d2 in PAIRES_DE_DOSES:
            Xm, ym = [], []
            for k in sorted({l[1] for l in lignes if l[0] in (d1, d2)}):
                sel = [l for l in lignes if l[1] == k]
                Xm.append(np.mean(X(sel, jeu), axis=0))
                ym.append(sel[0][0])
            r[f"mondes_dose_{d1}_contre_{d2}"] = exactitude_equilibree(Xm, ym, rng)
        out[jeu] = r
    arret = sorted(f"forme/{a}" for a, v in out["forme"].items() if v is not None and v > EXACTITUDE_MAX)
    signalement = sorted(f"{j}/{a}" for j in ("contenu", "reunis") for a, v in out[j].items() if v is not None and v > EXACTITUDE_MAX)
    non_calculees = sorted(f"{j}/{a}" for j in JEUX_DE_TRAITS for a, v in out[j].items() if v is None)
    return {"exactitudes": out, "arret": arret, "signalement": signalement, "non_calculees": non_calculees,
            "mention": "générateur non audité pour l'étage payant" if signalement else None}
