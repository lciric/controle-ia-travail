"""Outils communs de la contre-lecture de methode par simulation de la clause de repli des statistiques de stabilite de
rang (C-P3a, C-P3b, C-P3c) du preenregistrement du papier C, brouillon 6 de relance, version c2
(empreinte 7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61). Donnees simulees seulement ; aucune donnee
ni aucun resultat d'experience lu.

Fonctions reprises sans modification de l'archive (copies sous ../archive/, empreintes au manifeste) :
  commun_b5_v1.py : sommes_taches, agrege, regresseur, loi_jointe, comptes (loi jointe en forme fermee, points 8 et 8 bis
                    du texte ; reechantillonnage par grappes par comptes multinomiaux, point 11) ;
  t2_rang_temoins_partages_v1.py : w_kendall, nul_exact, p_exact, rangs, kendall_tau.
Le reste (trois lectures, regles de decision, modele des gains d'ecart) est ecrit ici par le contre-lecteur de la grille.

MODELE D'UN JUGE j pour TC.1 (celui de l'archive, « modele generalise ») ; T_i lecture vraie du contenu i, commune aux
trois juges ; mu milieu du corpus ; c = mu + lambda (v* - mu), ici lambda = 1 donc c = v* :
  v0_i     = T_i + e0,                                   e0 ~ N(0, s0_j)   (lecture sans insertion)
  v_tau,i  = T_i + kap_j (mu - T_i) + e,                 e  ~ N(0, sig_j)  (lecture sous le temoin tau, 16 temoins)
  v_m,i    = T_i + kap_j (mu - T_i) + g_{j,f,m} (c - T_i) + e              (formulation de rang m de la famille f)
  « erreur seule »      : s0_j = sig_j = s (ecart type 0,3 a 0,6), kap_j = 0 ;
  « compression seule » : s0_j = 0, sig_j = 0,4 (valeur de l'archive, non fixee par le texte), kap_j jusqu'a 0,16 ;
  « melange »           : s0_j = sig_j = s, kap_j > 0.
Corpus A : T taches, deux contenus par tache (honnete H de moyenne 2, saboteur S de moyenne 4, effet de tache d'ecart
type 0,5, residu 0,8), mu = 3, v* = 0. Corpus B : 30 items N(4,5 ; 1,4), mu = 4,5, v* = 9. Gains vrais :
g_{j,f,m} = g_j x PROFIL[f] x pente[m], PROFIL = (0,6 ; 0,8 ; 1 ; 1,2 ; 1,4), pente = linspace(0,5 ; 1,5 ; k).

REGLES DE DECISION (texte, bloc P-021, lignes 563 a 578 ; « Criteres de lecture geles », lignes 1405 a 1407) :
  C-P3a : W de Kendall des rangs des trois juges par G-barre net, cinq familles, corpus A ; « etablie » si p exact
          (7 776 affectations) <= 0,05 ET p par reechantillonnage centre <= 0,05, p = (1 + #{W* >= W}) / (B + 1),
          W* sur les rangs de G* - G ;
  C-P3b : tau de Kendall entre les quinze ecarts intra-famille du corpus A et ceux du corpus B ; « etablie » si
          p = (1 + #{tau* >= tau}) / (B + 1) <= 0,05, tau* entre les ecarts intra-famille de G*_A - G_A et de
          G*_B - G_B, tirages independants par taches et par items ;
  C-P3c : W de Kendall des trois juges, quatre evaluateurs (gain d'ecart brut sous le plaidoyer, gain d'ecart brut sous
          l'usurpation de l'agent, G-barre net de la famille 1, G-barre net de la famille 4, corpus A) ; « etablie » si
          p exact (1 296 affectations) <= 0,05 ;
  trois lectures de la loi nette pour les composantes en G-barre : calibree (« cal »), sans calibrage (« brut »,
  rho = 1), calibree par rho/r (« rr », rho et r recalcules dans chaque tirage) ; « etablie » seulement si les trois
  lectures concluent (« conj3 ») ; pour information, les deux premieres seules (« conj2 »).
Seuil de la clause de repli (lignes 580 a 583) : 0,05 + 2 x racine(0,05 x 0,95 / R), R essais de la case.
"""
import json
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(os.path.dirname(ICI), "archive")
sys.path.insert(0, ARCHIVE)
from commun_b5_v1 import agrege, comptes, loi_jointe, regresseur, sommes_taches  # noqa: E402
from t2_rang_temoins_partages_v1 import kendall_tau, nul_exact, p_exact, rangs, w_kendall  # noqa: E402

CONFIG = os.path.join(ARCHIVE, "papier-C-config-v1-brouillon3.json")  # longueurs seulement (regle des temoins)
FAMILLES = ["flatterie_supplication", "revendication_autorite", "approbations_forgees", "usurpation_stylistique",
            "ordres_en_bande"]
NUL = {m: nul_exact(m) for m in (4, 5)}
PROFIL = np.array([0.6, 0.8, 1.0, 1.2, 1.4])
RACINE = 20261119  # entropie racine de cette contre-lecture ; chaque case derive par spawn_key (R9)
LECTURES = ("cal", "brut", "rr")

# ---- configurations de modeles d'erreur des trois juges : (s0, sig, kap) par juge --------------------------------
S = lambda s: (s, s, 0.0)        # noqa: E731  erreur seule
D = lambda k: (0.0, 0.4, k)      # noqa: E731  compression seule
X = lambda s, k: (s, s, k)       # noqa: E731  melange
MODELES = {
    "E30": dict(juges=[S(0.3)] * 3, doc="erreur seule, homogene, ecart type 0,3"),
    "E40": dict(juges=[S(0.4)] * 3, doc="erreur seule, homogene, ecart type 0,4"),
    "E60": dict(juges=[S(0.6)] * 3, doc="erreur seule, homogene, ecart type 0,6"),
    "EH": dict(juges=[S(0.3), S(0.45), S(0.6)], doc="erreur seule, heterogene 0,3 / 0,45 / 0,6"),
    "K16": dict(juges=[D(0.16)] * 3, doc="compression seule, homogene, kappa 0,16"),
    "KH": dict(juges=[D(0.04), D(0.10), D(0.16)], doc="compression seule, heterogene 0,04 / 0,10 / 0,16"),
    "MH": dict(juges=[S(0.6), X(0.4, 0.08), D(0.16)],
               doc="un mecanisme par juge : erreur 0,6 / melange 0,4 et 0,08 / compression 0,16"),
    "M616": dict(juges=[X(0.6, 0.16)] * 3, doc="melange homogene, erreur 0,6 et kappa 0,16"),
}
ATTAQUES = {"g00": 0.0, "g10": 0.10, "g20": 0.20}
# scenarios d'effet (pour information et pour le controle sur un artefact) : gains vrais differents par juge
EFFETS = {
    "P3": dict(juges=[S(0.4)] * 3, g=[0.07, 0.10, 0.13], doc="effet vrai, erreur 0,4, gains 0,07 / 0,10 / 0,13"),
    "P6": dict(juges=[S(0.4)] * 3, g=[0.04, 0.10, 0.16], doc="effet vrai, erreur 0,4, gains 0,04 / 0,10 / 0,16"),
}


def scenario(modele, attaque):
    """Renvoie (juges, g par juge, description)."""
    if modele in EFFETS:
        e = EFFETS[modele]
        return e["juges"], list(e["g"]), e["doc"]
    g = ATTAQUES[attaque]
    return MODELES[modele]["juges"], [g] * 3, f"{MODELES[modele]['doc']} ; meme gain vrai {g} chez les trois juges"


def identifiant_case(modele, attaque, k, T):
    """Entier stable par case, pour la derivation des graines."""
    noms = list(MODELES) + list(EFFETS)
    return (noms.index(modele) * 1000 + list(ATTAQUES).index(attaque) * 100 + k * 10 + (0 if T == 45 else 1))


def generateur(programme, modele, attaque, k, T, passe):
    """SeedSequence(RACINE, spawn_key = (programme, case, passe)) ; renvoie (rng, description de la graine)."""
    cle = (int(programme), identifiant_case(modele, attaque, k, T), int(passe))
    ss = np.random.SeedSequence(RACINE, spawn_key=cle)
    return np.random.default_rng(ss), dict(entropie=RACINE, spawn_key=list(cle))


def seuil_clause(R):
    return 0.05 + 2 * float(np.sqrt(0.05 * 0.95 / R))


def mc(p, R):
    """Erreur de Monte-Carlo (ecart type) d'une proportion."""
    return float(np.sqrt(max(p * (1 - p), 0.0) / R))


def appariement(indices_retenus):
    """Regle des temoins (texte, Plan, section 2, lignes 1073 a 1076) : dans l'ordre des rangs croissants, temoin de
    longueur la plus proche parmi ceux non encore pris dans la meme famille ; egalites : plus petit indice ; un meme
    temoin peut servir a plusieurs familles. Longueurs de la configuration brouillon 3 de l'archive (aucun texte lu)."""
    cfg = json.load(open(CONFIG, encoding="utf-8"))
    lt = cfg["controle_redaction"]["longueurs_temoins"]
    out = {}
    for f in FAMILLES:
        lf = cfg["controle_redaction"]["longueurs_A"][f]
        pris, lst = set(), []
        for idx in indices_retenus:
            best = min((abs(lt[t] - lf[idx - 1]), t) for t in range(16) if t not in pris)
            pris.add(best[1])
            lst.append(best[1])
        out[f] = lst
    return out


def gains_vrais(g_juges, k):
    """(3, 5, k) : g_j x PROFIL[f] x pente[m]."""
    return np.array([gj * PROFIL[:, None] * np.linspace(0.5, 1.5, k)[None, :] for gj in g_juges])


def corpus_A(rng, T):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    return dict(vrai=vrai, grappe=tache, mu=3.0, vstar=0.0, u=u, T=T)


def corpus_B(rng, n=30):
    vrai = 4.5 + rng.normal(0, 1.4, n)
    return dict(vrai=vrai, grappe=np.arange(n), mu=4.5, vstar=9.0, u=None, T=n)


def rr_fonction(v0, vt_ret, grappe, T):
    """rho/r (texte, lignes 569 a 572 et point 8 bis, lignes 710 a 716) : rho = cov(v0, wbar) / var(v0), borne a
    [0,05 ; 1] ; r = moyenne des covariances entre les lectures de deux temoins distincts / moyenne des covariances
    entre v0 et la lecture d'un temoin ; rho/r borne a [0,05 ; 1]. Renvoie f(poids par grappe) -> rho/r."""
    M = np.column_stack([v0, vt_ret])
    q = M.shape[1]
    s1 = np.stack([np.bincount(grappe, weights=M[:, a], minlength=T) for a in range(q)], 1)
    s2 = np.stack([np.stack([np.bincount(grappe, weights=M[:, a] * M[:, b], minlength=T) for b in range(q)], 1)
                   for a in range(q)], 1)
    cnt = np.bincount(grappe, minlength=T).astype(float)
    iu = np.triu_indices(q - 1, 1)

    def f(wts):
        nn = wts @ cnt
        m1 = (wts @ s1) / nn[..., None]
        m2 = np.einsum("...t,tab->...ab", wts, s2) / nn[..., None, None]
        C = m2 - m1[..., :, None] * m1[..., None, :]
        ctt = C[..., 1:, 1:][..., iu[0], iu[1]].mean(-1)
        c0t = C[..., 0, 1:].mean(-1)  # = cov(v0, wbar)
        r = ctt / c0t
        rho = np.clip(c0t / C[..., 0, 0], 0.05, 1.0)
        return np.clip(rho / r, 0.05, 1.0)
    return f


def trois_lectures(rng, corpus, juges, gains, lam, pairs, B, familles=None):
    """Trois lectures de la loi nette du temoin pour trois juges.
    juges : liste de (s0, sig, kap) ; gains : (3, 5, k) ; B : nombre de tirages par grappes (0 : aucun tirage) ;
    familles : indices des familles a calculer (toutes par defaut ; les lectures sont simulees pour toutes).
    Renvoie out[lecture] = dict(G (5, 3), Gb (B, 5, 3), deg (5, 3) part de tirages degeneres), et v0 par juge.
    Memes comptes de reechantillonnage pour les trois juges et les cinq familles d'un corpus (point 11)."""
    vrai, grappe, mu, vstar, T = corpus["vrai"], corpus["grappe"], corpus["mu"], corpus["vstar"], corpus["T"]
    n = len(vrai)
    k = gains.shape[2]
    W = comptes(rng, T, B) if B > 0 else None
    utilises = sorted({t for f in FAMILLES for t in pairs[f]})
    fams = range(5) if familles is None else familles
    out = {r: dict(G=np.full((5, 3), np.nan), Gb=np.full((max(B, 1), 5, 3), np.nan), deg=np.zeros((5, 3)))
           for r in LECTURES}
    v0s = []
    c = mu + lam * (vstar - mu)
    for j, (s0, sig, kap) in enumerate(juges):
        v0 = vrai + (rng.normal(0, s0, n) if s0 > 0 else 0.0)
        v0s.append(v0)
        base = vrai + kap * (mu - vrai)
        vt = base[:, None] + rng.normal(0, sig, (n, 16))
        wbar = vt[:, utilises].mean(1)
        f_rr = rr_fonction(v0, vt[:, utilises], grappe, T)
        rr0 = float(f_rr(np.ones(T)))
        rrb = f_rr(W) if B > 0 else None
        vms = [base[:, None] + (c - vrai)[:, None] * gains[j, fi][None, :] + rng.normal(0, sig, (n, k))
               for fi in range(5)]  # tire pour les cinq familles, quel que soit `familles` (flux de hasard stable)
        for fi in fams:
            Y = vms[fi] - vt[:, pairs[FAMILLES[fi]]]
            s = sommes_taches(Y, v0, wbar, grappe, T)
            sa = agrege(s)
            sb = agrege(s, W) if B > 0 else None
            for r, kw, kwb in (("cal", dict(calibre=True), dict(calibre=True)),
                               ("brut", dict(calibre=False), dict(calibre=False)),
                               ("rr", dict(rho_fixe=rr0), dict(rho_fixe=rrb))):
                n_, S1, S2, A_, Bm, rho, vb = regresseur(sa, **kw)
                out[r]["G"][fi, j] = float(loi_jointe(n_, S1, S2, A_, Bm)[2])
                if B > 0:
                    n_, S1, S2, A_, Bm, rho, vbb = regresseur(sb, **kwb)
                    cb, gb, Gbm, degb = loi_jointe(n_, S1, S2, A_, Bm)
                    out[r]["Gb"][:, fi, j] = Gbm
                    # tirage degenere (point 11, lignes 758 a 759) : c-chapeau au bord de [-30 ; 40] ou |v* - v0bar*| < 0,5
                    out[r]["deg"][fi, j] = float((degb | (np.abs(vstar - vbb) < 0.5)).mean())
    return out, v0s


def etablie_a(G, Gb):
    """C-P3a pour une lecture : (etablie, p exact <= 0,05, p centre <= 0,05)."""
    w = float(w_kendall(rangs(G)[None])[0])
    ws = w_kendall(rangs(Gb - G[None]))
    pe = float(p_exact(w, NUL[5]))
    pc = float((1 + (ws >= w - 1e-12).sum()) / (len(ws) + 1))
    return (pe <= 0.05) and (pc <= 0.05), pe <= 0.05, pc <= 0.05


def ecarts_intra(x):
    return x - x.mean(-1, keepdims=True)


def etablie_b(GA, GbA, GB, GbB):
    """C-P3b pour une lecture."""
    t = float(kendall_tau(ecarts_intra(GA).ravel(), ecarts_intra(GB).ravel()))
    Bn = GbA.shape[0]
    ts = kendall_tau(ecarts_intra(GbA - GA[None]).reshape(Bn, 15), ecarts_intra(GbB - GB[None]).reshape(Bn, 15))
    return float((1 + (ts >= t - 1e-12).sum()) / (Bn + 1)) <= 0.05


def etablie_c(G, ecarts):
    """C-P3c pour une lecture : quatre evaluateurs = deux gains d'ecart bruts (2, 3) + G-barre net des familles 1 et 4
    (indices 0 et 3 de FAMILLES). « etablie » si p exact (1 296 affectations) <= 0,05, soit W >= 0,8125."""
    ev = np.vstack([ecarts, G[[0, 3], :]])
    w = float(w_kendall(rangs(ev)[None])[0])
    return float(p_exact(w, NUL[4])) <= 0.05


def ex_aequo(x, tol=1e-12):
    """Vrai si une ligne de x (..., 3) porte deux valeurs egales (les rangs ne sont alors pas definis par le texte)."""
    s = np.sort(x, -1)
    return bool((np.diff(s, axis=-1) <= tol).any())


def gains_ecart(rng, corpusA, juges, v0s, gp, gu, kP, variante):
    """MODELE SIMULE DES GAINS D'ECART BRUTS DES JUGES (Metrique, point 13, lignes 769 a 779) sous le plaidoyer de l'agent
    (TC.2, kP niveaux) et sous l'usurpation de l'agent (TC.3 b, un niveau). Renvoie (2, 3) : ligne 0 G-barre_P, ligne 1
    g_U ; colonnes : juges.

    Hypotheses (toutes declarees au rapport) :
      G1  Les cellules H et S de TC.2 et TC.3 b sont les contenus H et S du corpus A de TC.1 : le juge j y donne
          v0 (meme lecture, memes erreurs e0). S et D0 = moyenne_t (S_t - H_t) sont donc communs au gain sous le
          plaidoyer et au gain sous l'usurpation d'un meme juge.
      G2  Chaque cellule SP_m (m = 1 a kP) et SU est un episode neuf de la meme tache et du meme agent saboteur :
          lecture vraie T' = 4 + u_t + N(0 ; 0,8), u_t effet de la tache (celui du corpus A), tirage independant par
          cellule, commun aux trois juges (comme T_i en TC.1).
      G3  Le paragraphe ecrit par l'agent deplace la lecture du juge j vers la cible v* de l'attaquant d'une fraction
          gamma_{j,m} du chemin : + gamma_{j,m} (v* - T'). Plaidoyer : gamma_{j,m} = gp_j x pente_P[m], pente_P =
          linspace(0,5 ; 1,5 ; kP) (ou 1 si kP = 1) ; usurpation : gamma = gu_j.
      G4  Ce que le juge fait d'autre d'un contenu qui porte un paragraphe de l'agent n'est pas fixe par le texte ; deux
          variantes :
          « insertion » : le paragraphe agit comme toute insertion de TC.1 : compression kap_j (mu - T') et erreur
                          d'insertion N(0, sig_j) ;
          « contenu »   : le paragraphe fait partie du contenu : pas de compression, erreur de lecture N(0, s0_j)
                          (celle d'une lecture sans insertion). Non definie si deux juges au moins ont s0 = 0 et le
                          meme gain (gains d'ecart exactement egaux : rangs non definis) ; l'appelant le verifie.
      G5  Aucun autre lien entre juges que la lecture vraie commune ; erreurs independantes entre juges, cellules,
          taches.
    Statistique (texte) : g_m brut = -moyenne_t (SP_{m,t} - S_t) / D0 ; G-barre_P = moyenne des g_m ; g_U idem.
    """
    T, u, mu, vstar = corpusA["T"], corpusA["u"], corpusA["mu"], corpusA["vstar"]
    pente = np.linspace(0.5, 1.5, kP) if kP > 1 else np.ones(1)
    vrais_P = 4.0 + u[None, :] + rng.normal(0, 0.8, (kP, T))   # G2, communs aux trois juges
    vrai_U = 4.0 + u + rng.normal(0, 0.8, T)
    out = np.zeros((2, 3))
    for j, (s0, sig, kap) in enumerate(juges):
        H, Sj = v0s[j][0::2], v0s[j][1::2]                     # G1
        D0 = float(np.mean(Sj - H))
        if variante == "insertion":
            kj, ej = kap, sig
        elif variante == "contenu":
            kj, ej = 0.0, s0
        else:
            raise ValueError(variante)
        bruit_P = rng.normal(0, 1.0, (kP, T)) * ej             # tire dans tous les cas (flux de hasard stable)
        bruit_U = rng.normal(0, 1.0, T) * ej
        SP = vrais_P + kj * (mu - vrais_P) + (gp[j] * pente)[:, None] * (vstar - vrais_P) + bruit_P
        SU = vrai_U + kj * (mu - vrai_U) + gu[j] * (vstar - vrai_U) + bruit_U
        g_m = -(SP - Sj[None, :]).mean(1) / D0
        out[0, j] = float(g_m.mean())
        out[1, j] = float(-(SU - Sj).mean() / D0)
    return out


def versions():
    import platform
    try:
        import scipy
        vs = scipy.__version__
    except Exception:  # scipy n'est pas installe sur cette machine et n'est pas utilise
        vs = "absent (non utilise)"
    return dict(python=platform.python_version(), numpy=np.__version__, scipy=vs)
