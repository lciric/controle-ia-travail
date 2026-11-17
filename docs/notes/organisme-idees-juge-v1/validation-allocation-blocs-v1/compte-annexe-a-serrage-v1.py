"""Compte de dimensionnement du serrage (annexe A du préenregistrement de la validation propre de l'allocation par blocs,
brouillon 3) : processeur seul ; aucun juge, aucun nul de production, aucune donnée de run, aucune graine du texte.

Monde jouet du jeu synthétique de l'idée 1.2 (`synthetique_v1.py`, febe203a... ; programme de la contre-lecture de [T],
`essai_validite_v1.py`, 01c648a0...) : 3 issues, un trait binaire (Bernoulli 1/2), nul composite {w S1 + (1 - w) S2},
monde P = 0,4 S1 + 0,6 S2, 24 cartes Q_i = softmax(log P + eps_i * N(0, 1)) hors de la classe, maximum de vraisemblance sur w
recalculé à chaque instant, blocs de 25, plafond 800, budget 4 800, m = 24 ; lois et issues tirées par génération (écart
E-2). **Seule la distance change** : eps_i = linspace(EPS_MIN, EPS_MAX, 24) au lieu de linspace(0,10 ; 0,30, 24).

Partie 0 (contrôle de la copie) : à la distance du jeu de l'idée 1.2, `tirages_generation` ci-dessous rend, sur cinq
générations d'essai, exactement les lois et les comptes de `synthetique_v1.tirages_generation` (empreinte vérifiée avant
import) ; sinon arrêt.

Partie 1 (lois seules, exact) : sous P, les tirages sont indépendants, donc E[Λ_n^2] = (1 + chi2_moyen)^n avec
chi2_moyen = (1/2) somme_t (somme_x Q(x|t)^2 / P(x|t) - 1) ; variance de Λ au plafond = (1 + chi2_moyen)^800 - 1. Pour toute
règle non anticipante (temps d'arrêt borné par 800 pour chaque carte, flux indépendants), la variance de la moyenne des 24
Λ au temps d'arrêt est au plus la somme des 24 variances au plafond divisée par 24^2 (Doob, et produits croisés de
martingales indépendantes de moyenne nulle) : d'où une demi-largeur projetée de l'intervalle à 95 % sur 20 000 générations.

Partie 2 (tirages d'essai) : règles F, A, G (saines) et deux mutations « la règle lit le bloc suivant » (X1 : G choisit la
carte dont log W **après** le bloc sera la plus grande, comme la règle `regle_gloutonne(..., anticipe=True)` du programme
01c648a0... ; A-anticipe : A décide ses arrêts sur l'instant suivant, non révélé), fonctions de règle importées telles
quelles de ce programme (empreinte vérifiée avant import). Λ est lu au temps d'arrêt : premier instant révélé où log W
atteint log(m/alpha), sinon dernier instant révélé.

Partie 3 (audit de la partie 2) : moyenne de Λ sous F sur dix séries indépendantes de 4 000 générations.

Graines d'essai : SeedSequence(entropy=20261117, spawn_key=(0, g)) pour la partie 0, (1, g) pour la partie 1, (2, g) pour la partie 2, (10, g) à
(19, g) pour la partie 3 ; jamais (97, g), (98, g), ni la racine d'un texte."""
import hashlib
import importlib.util
import math
import sys
from pathlib import Path

import numpy as np

DEPOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/home/user/controle-ia-travail")
PROG_CL = DEPOT / "docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-tirages-repartis-v1-outils/essai_validite_v1.py"
EMPREINTE_CL = "01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205"
if hashlib.sha256(PROG_CL.read_bytes()).hexdigest() != EMPREINTE_CL:
    raise SystemExit("programme de la contre-lecture : empreinte différente, arrêt")
spec = importlib.util.spec_from_file_location("essai_validite_v1", PROG_CL)
CL = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CL)
SYNTH = DEPOT / "src/controle_ia/organisme_idees_juge/synthetique_v1.py"
EMPREINTE_SYNTH = "febe203ab27796ba573accea6e6fea5692bc2c776191254408ab07d3cc9815d7"

M, BLOC, NB, SEUIL = CL.M, CL.BLOC, CL.NB, CL.SEUIL
ENTROPIE = 20261117
EPS_MIN, EPS_MAX = 0.01, 0.03
GEN_LOIS = 20_000
GEN_ESSAI = 20_000
LOT = 1_000


def _sm(a):
    a = np.exp(a)
    return a / a.sum(-1, keepdims=True)


def lois_jouet(rng, eps):
    """Comme `synthetique_v1.lois_jouet`, la distance en paramètre."""
    S1, S2 = _sm(rng.normal(0, 1.0, (2, 3))), _sm(rng.normal(0, 1.0, (2, 3)))
    P = 0.4 * S1 + 0.6 * S2
    Q = np.stack([_sm(np.log(P) + e * rng.normal(0, 1, (2, 3))) for e in eps])
    return S1, S2, P, Q


def tirages_generation(rng, eps):
    """Comme `synthetique_v1.tirages_generation` (ordre des tirages : lois, traits, issues)."""
    S1, S2, P, Q = lois_jouet(rng, eps)
    nx1 = rng.binomial(BLOC, 0.5, (M, NB))
    c = np.zeros((M, NB, 2, 3))
    c[..., 0, :] = rng.multinomial(BLOC - nx1, P[0])
    c[..., 1, :] = rng.multinomial(nx1, P[1])
    return S1, S2, P, Q, c.cumsum(1).reshape(M, NB, 6)


def trajectoires_lot(debut, fin, eps):
    """Comme `synthetique_v1.trajectoires_lot` : log W et log Λ (lot x 24 x 32), graine d'essai (2, g)."""
    tir = [tirages_generation(np.random.default_rng(np.random.SeedSequence(entropy=ENTROPIE, spawn_key=(2, g))), eps)
           for g in range(debut, fin)]
    S1 = np.stack([t[0] for t in tir]).reshape(-1, 1, 1, 6)
    S2 = np.stack([t[1] for t in tir]).reshape(-1, 1, 1, 6)
    lP = np.log(np.stack([t[2] for t in tir])).reshape(-1, 1, 1, 6)
    lQ = np.log(np.stack([t[3] for t in tir])).reshape(-1, M, 1, 6)
    C = np.stack([t[4] for t in tir])
    num = (C * lQ).sum(-1)
    llp = (C * lP).sum(-1)
    a, b = S1, S2

    def d(w):
        return (C * ((a - b) / (w[..., None] * a + (1 - w[..., None]) * b))).sum(-1)

    lo, hi = np.zeros(C.shape[:3]), np.ones(C.shape[:3])
    for _ in range(45):
        mi = (lo + hi) / 2
        pos = d(mi) > 0
        lo, hi = np.where(pos, mi, lo), np.where(pos, hi, mi)
    w = (lo + hi) / 2
    den = np.maximum((C * np.log(w[..., None] * a + (1 - w[..., None]) * b)).sum(-1), llp)
    return num - den, num - llp


def regle_A_anticipe(lw):
    """Mutation : la règle A du programme 01c648a0... décide ses arrêts sur l'instant suivant, non révélé."""
    R = lw.shape[0]; n = np.zeros((R, M), int)
    for tour in range(NB):
        haut, bas = CL.etat(lw, np.minimum(n + 1, NB)); actif = ~haut & ~bas & (n < NB)
        ordre = (np.arange(M) + tour) % M
        rang = np.cumsum(actif[:, ordre], 1); reste = CL.BUDGET - n.sum(1)
        donne = np.zeros_like(actif); donne[:, ordre] = actif[:, ordre] & (rang <= reste[:, None])
        n += donne
    return n


def lambda_au_temps_d_arret(lw, lam, n):
    """Λ au premier instant révélé où log W atteint log(m/alpha), sinon au dernier instant révélé (n blocs)."""
    rev = np.arange(NB)[None, None, :] < n[..., None]
    haut = (lw >= SEUIL) & rev
    prem = np.where(haut.any(-1), haut.argmax(-1), np.maximum(n - 1, 0))
    return np.exp(np.take_along_axis(lam, prem[..., None], -1)[..., 0])


def partie_0():
    if hashlib.sha256(SYNTH.read_bytes()).hexdigest() != EMPREINTE_SYNTH:
        raise SystemExit("synthetique_v1.py : empreinte différente, arrêt")
    sys.path.insert(0, str(DEPOT / "src"))
    from controle_ia.organisme_idees_juge import synthetique_v1 as S
    for g in range(5):
        s = np.random.SeedSequence(entropy=ENTROPIE, spawn_key=(0, g))
        a = S.tirages_generation(np.random.default_rng(s))
        b = tirages_generation(np.random.default_rng(s), np.linspace(0.10, 0.30, M))
        if not all(np.array_equal(x, y) for x, y in zip(a, b)):
            raise SystemExit(f"copie de tirages_generation différente de synthetique_v1 (génération d'essai {g}), arrêt")
    print("[0] copie de tirages_generation : lois et comptes égaux à ceux de synthetique_v1 sur 5 générations d'essai")


def partie_1(eps, nom):
    V = np.empty((GEN_LOIS, M))
    for g in range(GEN_LOIS):
        rng = np.random.default_rng(np.random.SeedSequence(entropy=ENTROPIE, spawn_key=(1, g)))
        _S1, _S2, P, Q = lois_jouet(rng, eps)
        chi = 0.5 * ((Q ** 2 / P[None]).sum(-1) - 1).sum(-1)
        V[g] = np.expm1(800 * np.log1p(chi))
    demi = 1.96 * math.sqrt((V.sum(1) / M ** 2).mean() / 20_000)
    print(f"[1] {nom} : variance de Λ au plafond, {GEN_LOIS} générations x 24 cartes : médiane {np.median(V):.3g} ; "
          f"moyenne {V.mean():.3g} ; quantile 0,999 {np.quantile(V, 0.999):.3g} ; maximum {V.max():.3g} ; "
          f"carte la plus loin : médiane {np.median(V[:, -1]):.3g}, moyenne {V[:, -1].mean():.3g} ; "
          f"demi-largeur projetée (borne de Doob, règle saine, 20 000 générations) {demi:.3g}")


def partie_2(eps):
    regles = ("F", "A", "G", "X1 (G lit le bloc suivant)", "A-anticipe (A lit le bloc suivant)")
    moy = {r: [] for r in regles}
    arrets = {r: [] for r in regles}
    franchies = 0
    for debut in range(0, GEN_ESSAI, LOT):
        lw, lam = trajectoires_lot(debut, debut + LOT, eps)
        franchies += int((lw > lam + 1e-9).sum())
        ns = {"F": np.full((LOT, M), CL.PART), "A": CL.regle_A(lw), "G": CL.regle_gloutonne(lw),
              "X1 (G lit le bloc suivant)": CL.regle_gloutonne(lw, True),
              "A-anticipe (A lit le bloc suivant)": regle_A_anticipe(lw)}
        for r in regles:
            n = ns[r]
            assert (n.sum(1) <= CL.BUDGET).all() and (n <= NB).all() and (n >= 1).all()
            moy[r].append(lambda_au_temps_d_arret(lw, lam, n).mean(1))
            haut, bas = CL.etat(lw, n)
            arrets[r].append((haut.mean(), bas.mean(), n.mean() * BLOC))
    print(f"[2] dominations franchies (log W > log Λ) sur {GEN_ESSAI} générations x 24 cartes x 32 instants : {franchies}")
    base = {r: np.concatenate(moy[r]) for r in regles}
    for r in regles:
        x = base[r]
        sd = x.std(ddof=1)
        demi_essai, demi_20000 = 1.96 * sd / math.sqrt(x.size), 1.96 * sd / math.sqrt(20_000)
        h, b, t = np.mean(arrets[r], axis=0)
        print(f"[2] {r:36s} : moyenne de Λ au temps d'arrêt {x.mean():.4f} ± {demi_essai:.4f} ({x.size} générations) ; "
              f"écart type par génération {sd:.4f} ; demi-largeur projetée à 20 000 générations {demi_20000:.4f} ; "
              f"borne basse projetée {x.mean() - demi_20000:.4f} ; part arrêtée haut {h:.4f}, bas {b:.4f} ; tirages moyens par carte {t:.1f}")
    for mut, ref in (("X1 (G lit le bloc suivant)", "G"), ("A-anticipe (A lit le bloc suivant)", "A")):
        dlt = base[mut] - base[ref]
        print(f"[2] différence appariée {mut} moins {ref} (mêmes tirages) : {dlt.mean():+.4f} ± {1.96 * dlt.std(ddof=1) / math.sqrt(dlt.size):.4f}")


def partie_3(eps):
    """Audit de la série d'essai : la moyenne de Λ sous F (200 tirages, aucune règle d'arrêt atteinte) sur dix séries
    indépendantes de 4 000 générations, graines (10, g) à (19, g) ; écart réduit par l'écart type observé et par la variance
    exacte (lois seules) ; une espérance exactement égale à 1 donne des écarts réduits d'écart type voisin de 1."""
    zs, zx = [], []
    for cle in range(10, 20):
        m, v = np.empty(4_000), np.empty(4_000)
        for g in range(4_000):
            rng = np.random.default_rng(np.random.SeedSequence(entropy=ENTROPIE, spawn_key=(cle, g)))
            _S1, _S2, P, Q, C = tirages_generation(rng, eps)
            lam = (C[:, CL.PART - 1, :] * (np.log(Q).reshape(M, 6) - np.log(P).reshape(6))).sum(-1)
            m[g] = np.exp(lam).mean()
            chi = 0.5 * ((Q ** 2 / P[None]).sum(-1) - 1).sum(-1)
            v[g] = np.expm1(CL.PART * BLOC * np.log1p(chi)).sum() / M ** 2
        zs.append((m.mean() - 1) / (m.std(ddof=1) / math.sqrt(m.size)))
        zx.append((m.mean() - 1) / math.sqrt(v.mean() / m.size))
    print(f"[3] F, dix séries de 4 000 générations : écarts réduits (écart type observé) {', '.join(f'{z:+.2f}' for z in zs)} ; "
          f"écart type des dix {np.std(zs, ddof=1):.2f} ; par la variance exacte {', '.join(f'{z:+.2f}' for z in zx)}")


if __name__ == "__main__":
    print(f"distance retenue : eps = linspace({EPS_MIN}, {EPS_MAX}, 24) ; programme de la contre-lecture {EMPREINTE_CL[:8]}... vérifié")
    partie_0()
    partie_1(np.linspace(0.10, 0.30, M), "distance du jeu de l'idée 1.2 (0,10 à 0,30)")
    partie_1(np.linspace(0.01, 0.05, M), "distance 0,01 à 0,05 (comparaison)")
    partie_1(np.linspace(EPS_MIN, EPS_MAX, M), "distance retenue (0,01 à 0,03)")
    partie_2(np.linspace(EPS_MIN, EPS_MAX, M))
    partie_3(np.linspace(EPS_MIN, EPS_MAX, M))
