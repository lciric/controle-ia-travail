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

Code v4 (préenregistrement v8 ; GO-2026-11-20-11 : nœud 1 (a), nœud 2 (a) limité aux trois audits des doses) :
- longueur de forme mesurée sur le texte où chaque nombre d'au moins quatre décimales, signe et exposant compris, est remplacé
  par son jeton, compté pour un caractère ; la longueur brute du texte canonique passe aux traits de contenu (annexe H, écart 2) ;
- pour chacune des quinze exactitudes : A observée, σ₀ et moyenne des exactitudes sous 1 000 permutations des étiquettes (entre
  lois pour les deux audits de lois ; entre suites pour les trois audits des mondes par dose, les mondes d'une suite gardant une
  étiquette commune), cinq plis retirés à chaque permutation, et le seuil 0,55 + 2 σ₀ (section « Seuil », règle calibrée) ;
- lecture : les deux exactitudes de forme des audits de lois à la lettre de la version 6 (au-dessus de 0,55, arrêt) ; les trois
  des audits des mondes par dose en trois lectures (au plus 0,55 tenue ; au-dessus de 0,55 + 2 σ₀ arrêt ; entre les deux,
  « non départagée du hasard à cette taille », qui lie l'étage payant) ; contenu et réunis rapportés, liant l'étage payant
  au-dessus de 0,55 ;
- arrêt (`ArretAudit`) sur un pli d'entraînement privé d'une classe, un centre de classe non fini ou une exactitude qui ne peut
  être calculée (moins de cinq exemples d'une classe), à la lecture observée comme sous permutation (note D9 ; version 8).

Code v5 (préenregistrement v11 ; « Ce qui demande un code v5 », points 1, 2 et 6 ; GO-2026-11-20-25 et GO-2026-11-20-41 ;
décision de la mère R-4182, lecture (i) ; NE-3 retenu, R-4210) :
- le seuil calibré est M + 2 σ₀, M étant la moyenne des mêmes exactitudes permutées (à la place de 0,55 + 2 σ₀) ; il est rapporté
  pour les quinze exactitudes (colonne `seuil_calibre`) ;
- forme des trois audits des mondes par dose : le seuil d'arrêt est le plus grand de 0,55 et de M + 2 σ₀ ; au plus 0,55, tenue
  (jamais un arrêt, même au-dessus de M + 2 σ₀) ; au-dessus de 0,55 et de M + 2 σ₀, arrêt ; au-dessus de 0,55 et au plus
  M + 2 σ₀, « non départagée du hasard à cette taille », qui lie l'étage payant (mention) ;
- contenu et réunis des trois audits des mondes par dose : règle calibrée de signalement, jamais un arrêt ; au-dessus de 0,55 et
  de M + 2 σ₀, signalée, avec la mention ; au plus 0,55, ni signalement ni mention ; au-dessus de 0,55 et au plus M + 2 σ₀,
  « non départagée du hasard à cette taille », ni signalement ni mention (`non_departagees_sans_mention`) ;
- les deux audits de lois restent à la lettre (forme : au-dessus de 0,55, arrêt ; contenu et réunis : au-dessus de 0,55,
  signalés, avec la mention) ;
- « au plus » est inclusif, « au-dessus de » strict (une exactitude égale à M + 2 σ₀ est au plus M + 2 σ₀) ;
- NE-3 : une colonne de plus, `seuil_d_arret`, porte le seuil d'arrêt : le plus grand de 0,55 et de M + 2 σ₀ pour la forme des
  audits des mondes par dose, 0,55 pour la forme des audits de lois, aucun (None) pour le contenu et les réunis, qui n'arrêtent
  jamais (silence déclaré au rapport du code v5).
"""

import hashlib
import itertools
import json
import re

import numpy as np

from .constantes import EXEMPLES_MIN_PAR_CLASSE, PERMUTATIONS_AUDIT

SEUIL_MARGE = 0.25
PLANCHER_AUDIT = 1e-12
EXACTITUDE_MAX = 0.55
CASES = 64
PAIRES_DE_DOSES = ((0.0, 0.25), (0.0, 0.5), (0.25, 0.5))
JEUX_DE_TRAITS = ("forme", "contenu", "reunis")
PLIS = 5
AUDITS_DE_LOIS = ("vraies_contre_fausses", "dependantes_contre_independantes")
AUDITS_DES_DOSES = tuple(f"mondes_dose_{a}_contre_{b}" for a, b in PAIRES_DE_DOSES)
AUDITS = AUDITS_DE_LOIS + AUDITS_DES_DOSES
JETON_D_UN_NOMBRE_EN_CARACTERES = "#"  # un caractère (annexe H, écart 2) ; seule sa longueur compte

# lectures d'une exactitude (section « Seuil »)
TENUE = "tenue"
ARRET = "arrêt"
NON_DEPARTAGEE = "non départagée du hasard à cette taille"
SIGNALEE = "signalée"
AU_PLUS = "au plus 0,55"
MENTION = "générateur non audité pour l'étage payant"


class AuditRefuse(ValueError):
    pass


class ArretAudit(RuntimeError):
    """Arrêt de l'audit de présentation (section « Seuil », versions 7 et 8 ; note D9 ; liste d'arrêt, point 2)."""


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


def _nombre_long(j):
    """Un jeton de nombre (signe et exposant compris) d'au moins quatre décimales : celui que le jeton unique remplace."""
    if not (j[0].isdigit() or (j[0] == "-" and len(j) > 1)):
        return False
    mant = j.split("e")[0].split("E")[0]
    dec = mant.split(".")[1] if "." in mant else ""
    return len(dec) >= 4


def jetons(texte):
    for j in _JETON.findall(texte):
        yield "<nombre>" if _nombre_long(j) else j


def texte_aux_nombres_remplaces(texte):
    """Code v4 (annexe H, écart 2 ; nœud 1, option (a)) : le texte où chaque nombre d'au moins quatre décimales, signe et
    exposant compris, est remplacé par son jeton, compté pour un caractère. Les nombres sont ceux que `jetons` lit."""
    morceaux, fin = [], 0
    for m in _JETON.finditer(texte):
        if _nombre_long(m.group(0)):
            morceaux += [texte[fin:m.start()], JETON_D_UN_NOMBRE_EN_CARACTERES]
            fin = m.end()
    morceaux.append(texte[fin:])
    return "".join(morceaux)


def traits_de_forme(texte):
    """Comptes des jetons du texte canonique répartis en 64 cases (tout nombre d'au moins quatre décimales comptant pour un même
    jeton), et la longueur du texte où chacun de ces nombres est remplacé par ce jeton, compté pour un caractère (code v4 ; la
    longueur brute, qui lit le signe des nombres, est un trait de contenu)."""
    v = np.zeros(CASES + 1)
    for j in jetons(texte):
        v[int.from_bytes(hashlib.sha256(j.encode("utf-8")).digest()[:4], "big") % CASES] += 1
    v[CASES] = float(len(texte_aux_nombres_remplaces(texte)))
    return v


def traits_de_contenu(loi, Z, G, texte):
    """Pour chaque sous-population : norme des poids, norme des biais, entropie moyenne de la loi (nats) sur les instances de
    l'oracle du monde dans cette sous-population ; puis, pour la loi entière, la longueur brute de son texte canonique, en
    caractères (code v4, annexe H, écart 2). `texte` doit être le texte canonique de `loi`, sinon refus."""
    if texte != _cle(loi):
        raise AuditRefuse("audit : le texte donné n'est pas le texte canonique de la loi (longueur brute)")
    P = probas_audit(loi, Z, G)
    G = np.asarray(G)
    out = []
    for g in (0, 1):
        s = loi["lois"][str(g)]
        H = -np.einsum("nk,nk->n", P[G == g], np.log(P[G == g]))
        out += [float(np.linalg.norm(np.array(s["poids"], dtype=float))), float(np.linalg.norm(np.array(s["biais"], dtype=float))),
                float(H.mean())]
    out.append(float(len(texte)))
    return np.array(out)


def _indices_de_classe(y):
    """Les deux classes triées et l'indice de classe de chaque exemple. Arrêt si l'exactitude ne peut être calculée : pas
    exactement deux classes, ou moins de cinq exemples d'une classe (section « Seuil », version 8 ; le code v3 rendait None)."""
    y = np.asarray(y)
    classes = sorted(set(y.tolist()))
    if len(classes) != 2:
        raise ArretAudit(f"exactitude non calculable : {len(classes)} classe(s) au lieu de deux : arrêt de l'audit "
                         "(section « Seuil », version 8 ; liste d'arrêt, point 2)")
    yi = np.array([classes.index(v) for v in y.tolist()], dtype=int)
    _exiger_calculable(yi)
    return classes, yi


def _exiger_calculable(yi):
    comptes = [int(np.sum(yi == c)) for c in (0, 1)]
    if min(comptes) < EXEMPLES_MIN_PAR_CLASSE:
        raise ArretAudit(f"exactitude non calculable : moins de {EXEMPLES_MIN_PAR_CLASSE} exemples d'une classe ({comptes}) : "
                         "arrêt de l'audit (section « Seuil », version 8 ; liste d'arrêt, point 2)")


def _exactitude(X, yi, rng, plis):
    """Plus proche centre de classe, validation croisée à `plis` plis tirés par une permutation semée, sans stratification ;
    exactitude équilibrée. Arrêt sur un pli d'entraînement privé d'une classe ou un centre de classe non fini (note D9)."""
    n = len(yi)
    pli = np.empty(n, dtype=int)
    pli[rng.permutation(n)] = np.arange(n) % plis
    pred = np.empty(n, dtype=int)
    for k in range(plis):
        tr, te = pli != k, pli == k
        ytr = yi[tr]
        for c in (0, 1):
            if not np.any(ytr == c):
                raise ArretAudit(f"pli d'entraînement {k} privé d'une classe : arrêt de l'audit (note D9 ; liste d'arrêt, "
                                 "point 2)")
        mu, sd = X[tr].mean(axis=0), X[tr].std(axis=0)
        sd = np.where(sd > 0, sd, 1.0)
        Xt, Xe = (X[tr] - mu) / sd, (X[te] - mu) / sd
        centres = [Xt[ytr == c].mean(axis=0) for c in (0, 1)]
        if not all(np.all(np.isfinite(c)) for c in centres):
            raise ArretAudit(f"centre de classe non fini au pli {k} : arrêt de l'audit (note D9 ; liste d'arrêt, point 2)")
        D = np.stack([((Xe - c) ** 2).sum(axis=1) for c in centres], axis=1)
        pred[te] = D.argmin(axis=1)
    return float(np.mean([np.mean(pred[yi == c] == c) for c in (0, 1)]))


def exactitude_equilibree(X, y, rng, plis=PLIS):
    """Plus proche centre de classe sur des traits centrés et réduits (moyenne et écart-type du pli d'entraînement ; un trait de
    variance nulle est centré sans être réduit), validation croisée à `plis` plis ; exactitude équilibrée. Code v4 : arrêt
    (`ArretAudit`) si elle ne peut être calculée (moins de cinq exemples d'une classe), si un pli d'entraînement est privé d'une
    classe ou si un centre n'est pas fini — jamais None."""
    _, yi = _indices_de_classe(y)
    return _exactitude(np.asarray(X, dtype=float), yi, rng, plis)


def permuter_les_etiquettes(yi, groupes, rng):
    """Une permutation des étiquettes : entre exemples si `groupes` vaut None (audits de lois) ; sinon entre groupes, chaque
    groupe (une suite) gardant une étiquette commune (audits des mondes par dose). Les exemples d'un groupe doivent avoir la même
    étiquette, sinon refus."""
    yi = np.asarray(yi)
    if groupes is None:
        return yi[rng.permutation(len(yi))]
    groupes = list(groupes)
    if len(groupes) != len(yi):
        raise AuditRefuse("permutation entre suites : un identifiant de suite par exemple est exigé")
    etiquette = {}
    for g, v in zip(groupes, yi.tolist()):
        if etiquette.setdefault(g, v) != v:
            raise AuditRefuse(f"permutation entre suites : les mondes de la suite {g!r} n'ont pas la même étiquette")
    ids = sorted(etiquette)
    perm = rng.permutation(len(ids))
    nouvelle = {ids[i]: etiquette[ids[int(perm[i])]] for i in range(len(ids))}
    return np.array([nouvelle[g] for g in groupes], dtype=yi.dtype)


def sous_permutation(X, y, rng, permutations, groupes=None, plis=PLIS):
    """σ₀ (écart-type, ddof = 1) et moyenne de l'exactitude sous `permutations` permutations des étiquettes ; mêmes traits, même
    classifieur, plis retirés à chaque permutation par le même `rng`. Les arrêts de la lecture observée valent ici aussi."""
    if isinstance(permutations, bool) or not isinstance(permutations, int) or permutations < 2:
        raise AuditRefuse(f"permutations : entier ≥ 2 attendu (reçu {permutations!r})")
    X = np.asarray(X, dtype=float)
    _, yi = _indices_de_classe(y)
    vals = np.empty(permutations)
    for p in range(permutations):
        yp = permuter_les_etiquettes(yi, groupes, rng)
        _exiger_calculable(yp)
        vals[p] = _exactitude(X, yp, rng, plis)
    return {"sigma0": float(vals.std(ddof=1)), "moyenne_permutee": float(vals.mean())}


def seuil_calibre(sigma0, moyenne):
    """Code v5 (section « Seuil », version 9, GO-2026-11-20-25, point (1)) : M + 2 σ₀, M et σ₀ étant la moyenne et l'écart-type
    des mêmes exactitudes permutées. Rapporté pour les quinze exactitudes."""
    return moyenne + 2.0 * sigma0


def seuil_d_arret(jeu, audit, sigma0, moyenne):
    """Code v5 (NE-3, contrôle de la version 11, retenu par la mère, R-4210) : le seuil d'arrêt d'une exactitude. Forme des
    audits des mondes par dose : le plus grand de 0,55 et de M + 2 σ₀ (version 11, GO-2026-11-20-41) ; forme des audits de lois :
    0,55 (lettre de la version 6) ; contenu et réunis : None, aucune de leurs lectures n'arrête."""
    if jeu not in JEUX_DE_TRAITS or audit not in AUDITS:
        raise AuditRefuse(f"seuil d'arrêt : exactitude inconnue {jeu}/{audit}")
    if jeu != "forme":
        return None
    if audit in AUDITS_DES_DOSES:
        return max(EXACTITUDE_MAX, seuil_calibre(sigma0, moyenne))
    return EXACTITUDE_MAX


def lecture(jeu, audit, A, sigma0, moyenne):
    """La lecture d'une exactitude (section « Seuil », version 11). Audits des mondes par dose (règle calibrée, M + 2 σ₀) : au
    plus 0,55, tenue (forme) ou « au plus 0,55 » (contenu et réunis), même au-dessus de M + 2 σ₀ — une exactitude au plus 0,55
    n'arrête jamais et n'est jamais signalée ; au-dessus de 0,55 et de M + 2 σ₀, arrêt (forme) ou signalée (contenu et réunis,
    jamais un arrêt) ; au-dessus de 0,55 et au plus M + 2 σ₀, « non départagée du hasard à cette taille ». Audits de lois, à la
    lettre : forme, au-dessus de 0,55, arrêt ; contenu et réunis, au-dessus de 0,55, signalées."""
    if jeu not in JEUX_DE_TRAITS or audit not in AUDITS:
        raise AuditRefuse(f"lecture : exactitude inconnue {jeu}/{audit}")
    if audit in AUDITS_DES_DOSES:
        if A <= EXACTITUDE_MAX:
            return TENUE if jeu == "forme" else AU_PLUS
        if A > seuil_calibre(sigma0, moyenne):
            return ARRET if jeu == "forme" else SIGNALEE
        return NON_DEPARTAGEE
    if jeu != "forme":
        return SIGNALEE if A > EXACTITUDE_MAX else AU_PLUS
    return ARRET if A > EXACTITUDE_MAX else TENUE


def lire_audit(table):
    """`table` : {jeu : {audit : {"A", "sigma0", "moyenne_permutee", …}}} pour les quinze exactitudes, exactement. Rend la
    lecture de chacune, la liste des arrêts (forme), celle des exactitudes de forme non départagées (audits des doses ; elles
    lient l'étage payant), celle des exactitudes de contenu ou réunies non départagées (audits des doses ; ni signalement ni
    mention, code v5), celle des exactitudes signalées, et la mention qui lie l'étage payant (posée par un signalement ou par
    une exactitude de forme non départagée, jamais par une exactitude de contenu ou réunie non départagée)."""
    if sorted(table) != sorted(JEUX_DE_TRAITS) or any(sorted(table[j]) != sorted(AUDITS) for j in JEUX_DE_TRAITS):
        raise AuditRefuse("lecture : les quinze exactitudes sont exigées, et elles seules")
    lectures, arret, non_departagees, sans_mention, signalement = {}, [], [], [], []
    for jeu in JEUX_DE_TRAITS:
        lectures[jeu] = {}
        for audit in AUDITS:
            e = table[jeu][audit]
            if any(k not in e for k in ("A", "sigma0", "moyenne_permutee")):
                raise AuditRefuse(f"lecture : A, σ₀ et la moyenne permutée sont exigés ({jeu}/{audit})")
            l = lecture(jeu, audit, e["A"], e["sigma0"], e["moyenne_permutee"])
            lectures[jeu][audit] = l
            nom = f"{jeu}/{audit}"
            if l == ARRET:
                arret.append(nom)
            elif l == NON_DEPARTAGEE and jeu == "forme":
                non_departagees.append(nom)
            elif l == NON_DEPARTAGEE:
                sans_mention.append(nom)
            elif l == SIGNALEE:
                signalement.append(nom)
    return {"lectures": lectures, "arret": sorted(arret), "non_departagees": sorted(non_departagees),
            "non_departagees_sans_mention": sorted(sans_mention), "signalement": sorted(signalement),
            "mention": MENTION if (signalement or non_departagees) else None}


def audit_presentation(mondes_audites, rng, rng_permutation, permutations=PERMUTATIONS_AUDIT):
    """`mondes_audites` : liste de dicts {"dose", "suite", "lois": [(texte canonique, loi, type, dependante)], "Z", "G"} — les
    mondes cibles et finaux des suites de la couche « audit », chacun avec l'identifiant de sa suite. `rng` tire les plis de la
    lecture observée (même ordre et même flux qu'au code v3) ; `rng_permutation` (couche « audit », rôle « permutation ») tire
    les permutations et leurs plis. Rend les quinze exactitudes observées (`exactitudes`), la table (A, σ₀, moyenne permutée M,
    seuil calibré M + 2 σ₀, seuil d'arrêt, lecture ; code v5) des quinze, et la lecture (`arret`, `non_departagees`,
    `non_departagees_sans_mention`, `signalement`, `mention`). Arrête (`ArretAudit`) sur un pli privé d'une classe, un centre
    non fini ou une exactitude non calculable."""
    lignes = []  # (dose, monde, type, dependante, forme, contenu)
    suite_du_monde, dose_de_la_suite = [], {}
    for k, m in enumerate(mondes_audites):
        if "suite" not in m:
            raise AuditRefuse("audit de présentation : l'identifiant de la suite de chaque monde est exigé (permutation entre "
                              "suites)")
        if dose_de_la_suite.setdefault(m["suite"], float(m["dose"])) != float(m["dose"]):
            raise AuditRefuse(f"audit de présentation : la suite {m['suite']!r} porte deux doses")
        suite_du_monde.append(m["suite"])
        for texte, loi, typ, dep in m["lois"]:
            lignes.append((float(m["dose"]), k, typ, bool(dep), traits_de_forme(texte),
                           traits_de_contenu(loi, m["Z"], m["G"], texte)))

    def X(sel, jeu):
        if jeu == "forme":
            return [l[4] for l in sel]
        if jeu == "contenu":
            return [l[5] for l in sel]
        return [np.concatenate([l[4], l[5]]) for l in sel]

    donnees = {}  # (jeu, audit) : (traits, étiquettes, groupes de la permutation)
    for jeu in JEUX_DE_TRAITS:
        donnees[(jeu, "vraies_contre_fausses")] = (np.asarray(X(lignes, jeu), dtype=float), [l[2] for l in lignes], None)
        vd = [l for l in lignes if l[2] == "vraie" and l[0] > 0]
        donnees[(jeu, "dependantes_contre_independantes")] = (np.asarray(X(vd, jeu), dtype=float), [l[3] for l in vd], None)
        for d1, d2 in PAIRES_DE_DOSES:
            Xm, ym, gm = [], [], []
            for k in sorted({l[1] for l in lignes if l[0] in (d1, d2)}):
                sel = [l for l in lignes if l[1] == k]
                Xm.append(np.mean(X(sel, jeu), axis=0))
                ym.append(sel[0][0])
                gm.append(suite_du_monde[k])
            donnees[(jeu, f"mondes_dose_{d1}_contre_{d2}")] = (np.asarray(Xm, dtype=float), ym, gm)
    exactitudes = {}
    for jeu in JEUX_DE_TRAITS:  # lecture observée : même ordre de tirage des plis que le code v3
        exactitudes[jeu] = {a: exactitude_equilibree(donnees[(jeu, a)][0], donnees[(jeu, a)][1], rng) for a in AUDITS}
    table = {}
    for jeu in JEUX_DE_TRAITS:
        table[jeu] = {}
        for a in AUDITS:
            Xa, ya, ga = donnees[(jeu, a)]
            p = sous_permutation(Xa, ya, rng_permutation, permutations, ga)
            table[jeu][a] = {"A": exactitudes[jeu][a], "sigma0": p["sigma0"], "moyenne_permutee": p["moyenne_permutee"],
                             "seuil_calibre": seuil_calibre(p["sigma0"], p["moyenne_permutee"]),
                             "seuil_d_arret": seuil_d_arret(jeu, a, p["sigma0"], p["moyenne_permutee"]),
                             "permutations": permutations,
                             "permutation": "entre lois" if ga is None else "entre suites",
                             "unites_permutees": len(ya) if ga is None else len(set(ga))}
    lu = lire_audit(table)
    for jeu in JEUX_DE_TRAITS:
        for a in AUDITS:
            table[jeu][a]["lecture"] = lu["lectures"][jeu][a]
    return {"exactitudes": exactitudes, "table": table, "arret": lu["arret"], "non_departagees": lu["non_departagees"],
            "non_departagees_sans_mention": lu["non_departagees_sans_mention"], "signalement": lu["signalement"],
            "mention": lu["mention"]}
