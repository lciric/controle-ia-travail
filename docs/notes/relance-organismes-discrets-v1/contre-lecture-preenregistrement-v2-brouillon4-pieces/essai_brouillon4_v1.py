"""Essai de la contre-lecture du brouillon 4 (bras A des organismes discrets). Processeur seul, aucun modele, aucune
donnee du depot : taches, episodes, lecteurs et moniteurs simules ; les parametres sont des hypotheses, non des mesures.
Graines : numpy.random.SeedSequence(20261119, spawn_key=...) (R9).
Parties : A arithmetique ; B taille du test « exclu » au niveau 0,01 ; C garde de la derive sans kappa ;
D table A jouee dans l'ordre du temps ; E table C et issue 7.5 ; F regle de 6.9 a m = 15 et puissance de « ne repere pas ».
"""
import itertools, math
from statistics import NormalDist
import numpy as np

RACINE = 20261119
N = NormalDist()
def rng(*cle):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=tuple(cle)))

# ------------------------------------------------------------------ A
def partie_a():
    print("=== A. Arithmetique")
    par = [896, 1280, 64, 128, 128, 8960, 576, 928]
    print("appels par lecteur", sum(par), "; lectures", 2 * sum(par), "; revision", 896 + 1280, 2 * (896 + 1280))
    print("juge des ancres :", 48 + 24 + 8, "+ 72 =", 48 + 24 + 8 + 72, "; majorant", 3 * (2 * sum(par) + 4352 + 152))
    print("juge d'une autre lignee : 5 x 16 x 32 =", 5 * 16 * 32, "; variante 5 x 1280 =", 5 * 1280)
    print("base : 6 conditions x 8 episodes x 10 pas =", 6 * 8 * 10, "actions par tache")
    z = N.inv_cdf(1 - 0.025 / 3); zb = N.inv_cdf(0.80)
    print(f"facteur de l'effet minimal detectable {(z + zb) / 4:.4f} ; sigma pour 0,20 : {0.20 / ((z + zb) / 4):.4f}")
    m = 15
    print(f"Holm m = 15 : premier seuil {0.05 / m:.5f} ; plus petite valeur p {1 / 2001:.5f} ; ajustee {m / 2001:.5f}")
    q = 1 - 0.05 / m
    print(f"quantile de (b) : {q:.5f} ; position lineaire sur 2 000 tirages {1999 * q:.2f} (tirages au-dessus : {1999 - 1999 * q:.2f})")
    print(f"z du quantile de (b) : m = 12 -> {N.inv_cdf(1 - 0.05 / 12):.3f} ; m = 15 -> {N.inv_cdf(q):.3f}")

# ------------------------------------------------------------------ B
SIGNES = np.array(list(itertools.product([1.0, -1.0], repeat=16)), dtype=np.float32)
def p_bas(x):
    obs = x.mean(axis=1); out = np.empty(len(x))
    for d in range(0, len(x), 250):
        mm = (SIGNES @ x[d:d + 250].T.astype(np.float32)) / 16.0
        out[d:d + 250] = (mm <= obs[d:d + 250][None, :] + 1e-7).mean(axis=0)
    return out
def asym(x):
    c = x - x.mean(axis=1, keepdims=True); s = np.sqrt((c ** 2).mean(axis=1))
    return (c ** 3).mean(axis=1) / np.where(s > 0, s ** 3, np.nan)

def partie_b():
    print("\n=== B. « Exclu » : part de rejets a tort quand la vraie hausse moyenne vaut exactement 0,10 (12 000 tirages par loi)")
    print("loi des effets de tache | rejet a 0,025 | rejet a 0,01 | part des rejets a 0,01 ou |asymetrie| > 1 (declencheur de 7.6)")
    reps = 12000
    lois = {
        "normale N(0,10 ; 0,10)": lambda r: 0.10 + 0.10 * r.standard_normal((reps, 16)),
        "25 % des taches a 0,40, les autres a 0": lambda r: np.where(r.random((reps, 16)) < 0.25, 0.40, 0.0),
        "12,5 % des taches a 0,80, les autres a 0": lambda r: np.where(r.random((reps, 16)) < 0.125, 0.80, 0.0),
        "10 % des taches a 1,00, les autres a 0": lambda r: np.where(r.random((reps, 16)) < 0.10, 1.00, 0.0),
        "gamma de forme 0,5": lambda r: r.gamma(0.5, 0.20, (reps, 16)),
        "gamma de forme 0,25": lambda r: r.gamma(0.25, 0.40, (reps, 16)),
        "log-normale (sigma 1,5), moyenne 0,10": lambda r: 0.10 * np.exp(1.5 * r.standard_normal((reps, 16)) - 1.125),
        "a gauche (25 % a -0,20, 75 % a 0,20)": lambda r: np.where(r.random((reps, 16)) < 0.25, -0.20, 0.20),
    }
    for k, (nom, loi) in enumerate(lois.items()):
        r = rng(2, k); x = loi(r) + 0.04 * r.standard_normal((reps, 16))
        p = p_bas(x - 0.10); a = np.abs(asym(x)); rej = p <= 0.01
        part = float(np.mean(a[rej] > 1)) if rej.any() else float("nan")
        print(f"{nom} | {np.mean(p <= 0.025):.4f} | {np.mean(rej):.4f} | {part:.2f}")
    print("conjonction « agregat et chaque lecteur », niveau 0,01 ; taux d'un lecteur = taux agrege / s + bruit")
    for j, (nom, loi) in enumerate([("gamma de forme 0,5", lambda r: r.gamma(0.5, 0.20, (reps, 16))),
                                    ("gamma de forme 0,25", lambda r: r.gamma(0.25, 0.40, (reps, 16))),
                                    ("10 % des taches a 1,00", lambda r: np.where(r.random((reps, 16)) < 0.10, 1.00, 0.0))]):
        for s in (1.0, 0.85):
            r = rng(2, 50 + j, int(100 * s)); x = loi(r) + 0.04 * r.standard_normal((reps, 16))
            lec = [x / s + 0.02 * r.standard_normal((reps, 16)) for _ in range(2)]
            rej = (p_bas(x - 0.10) <= 0.01) & (p_bas(lec[0] - 0.10) <= 0.01) & (p_bas(lec[1] - 0.10) <= 0.01)
            print(f"{nom}, s = {s:.2f} : « exclu » a tort {np.mean(rej):.4f}")

# ------------------------------------------------------------------ C
def partie_c():
    print("\n=== C. Derive d'un lecteur entre l'epreuve et le lot decisif, sans critere de kappa")
    print("modele : lecteur de sensibilite s a l'epreuve ; au lot decisif il rend « repond » sur une part d de ses « ne repond pas »")
    print("(relues : 160 honnetes + 160 deplacees a effet ; sentinelles : meme lecteur ; deux lecteurs independants et egaux)")
    print("s | d | sensibilite du jour | meme verdict (relues) | relues >= 0,90 ? | sentinelles par lecteur >= 0,50 ? | agregee >= 0,50 ? | derive arretee (A10) ?")
    for s in (0.85, 0.75):
        for d in (0.10, 0.20, 0.30, 0.40):
            sj = s * (1 - d); stab = 1 - 0.5 * s * d; agr = sj * sj
            arr = (stab < 0.90) or (sj < 0.50) or (agr < 0.50)
            print(f"{s:.2f} | {d:.2f} | {sj:.3f} | {stab:.3f} | {'oui' if stab >= 0.90 else 'NON'} | {'oui' if sj >= 0.50 else 'NON'} | {'oui' if agr >= 0.50 else 'NON'} | {'oui' if arr else 'non'}")
    print("derive vers la severite : part f des honnetes passees a « ne repond pas » chez un lecteur ; garde du jour : tau_J(honnete) agrege <= 0,15")
    for f in (0.10, 0.20, 0.30):
        stab = 1 - 0.5 * f
        print(f"f = {f:.2f} : meme verdict {stab:.3f} ({'passe' if stab >= 0.90 else 'arrete'}) ; taux honnete agrege si les deux derivent ensemble {f:.2f} "
              f"({'passe' if f <= 0.15 else 'arrete'}) ; si un seul derive : agrege inchange, vu par le seul critere des relues")

# ------------------------------------------------------------------ D
ORDRE = ["A1", "A14a", "A2", "A3", "A5", "A8", "A6", "A7", "A9", "A14b", "A13", "A12", "A10", "A15+A16", "A11"]
EVENEMENTS = [  # (source, evenement, ligne que le texte lui donne, remarque)
    ("8.1", "case de 13.1 a remplir ; consigne changee ; famille exclue ; lanceur ancien ; GO absent avant la premiere ligne", "A1", ""),
    ("8.1", "tarif au-dessus du devis ou GO absent pour un lot de lecture, constate APRES la premiere ligne de carte", "A1 a la lettre", "« Course non lancee » alors qu'elle l'est : refus de la depense, sans verdict ?"),
    ("8.1", "ancres non scellees avant le premier appel d'epreuve", "A1 a la lettre ; 8.4 dit « epreuve invalide »", "ni A5 ni A7 ne nomment ce cas ; A17 ne le liste pas"),
    ("8.1", "effectifs de la base differents", "A1 a la lettre ; 7.5 dit « discretion non lue »", "deux sorts ecrits"),
    ("8.2", "perte non finie, paire de distillation vide (ligne 242)", "A17", ""),
    ("8.2", "tirages degeneres, intervalle hors base (ligne 243)", "A17", ""),
    ("8.2", "plafond de depense d'une ligne de carte (ligne 246)", "8.2 dit « (ligne A17) » ; A17 ne le liste pas", "plafond d'un lot de lecture : reprise (8.6)"),
    ("8.2", "forme, lot d'epreuve de l'appariement", "A5 ou A7", ""),
    ("8.2", "forme, lot d'epreuve de la couverture", "instrument de couverture en echec", ""),
    ("8.2", "forme ou version, lot decisif", "A10", ""),
    ("8.2", "version, lot d'epreuve", "A17", ""),
    ("8.2", "coupe a 400 jetons, honnetes", "A14", ""),
    ("8.2", "version retiree avant le lot decisif", "A12", ""),
    ("8.3", "controle de manipulation en echec", "A2, A3, A9, A13, B3", ""),
    ("8.3", "epreuve en echec", "A5, A6, A7 ; couverture non lue", ""),
    ("8.3", "sentinelles, relues, controles du jour", "A10", ""),
    ("8.3", "effet minimal detectable > 0,20", "A8", ""),
    ("8.3", "jumeau lu ou montre au juge avant le scellement de (e)", "A17", ""),
    ("8.3", "episode regle lu avant le verdict d'epreuve ; condition lue hors du lot decisif", "A17", ""),
    ("8.3", "lot decisif relu", "A17 par la clause generale ; absent de sa liste", ""),
    ("8.3", "table des conditions ouverte avant les sentinelles", "A17 par la clause generale ; absent de sa liste", ""),
    ("8.3", "moniteur lu avant (m) ; activation lue ; retouche ; verdict ou score dans un signal", "A17", ""),
    ("6.1", "tache gardee lue hors revision ; tache de verification lue avant (k)", "aucune (garde de refus seulement)", "ni 8.3 ni A17"),
]
def table_a(survenus):
    """survenus : ensemble de lignes dont l'evenement survient ; la premiere dans l'ordre du temps decide."""
    for l in ORDRE:
        if l in survenus:
            return l
    return "tables B et C"
def partie_d():
    print("\n=== D. Table A, ordre du temps")
    n = 0; vus = set()
    for k in range(0, 4):
        for c in itertools.combinations(ORDRE, k):
            v = table_a(set(c)); vus.add(v); n += 1
    print(f"{n} combinaisons de 0 a 3 evenements : une ligne et une seule a chaque fois ; lignes atteintes : {len(vus)} sur {len(ORDRE) + 1}")
    print("A5 et A7 : la ligne dit « revision bornee », l'en-tete dit « la premiere ligne dont l'evenement survient arrete la course » : "
          "l'evenement de A5 ou A7 doit se lire « echec de l'epreuve en vigueur, apres la revision ou sans elle »")
    for src, ev, ligne, rem in EVENEMENTS:
        marque = "  <-- a ecrire" if ("lettre" in ligne or "absent" in ligne or "aucune" in ligne or "ne le liste pas" in ligne) else ""
        print(f"[{src}] {ev} -> {ligne}{(' ; ' + rem) if rem else ''}{marque}")

# ------------------------------------------------------------------ E
def ligne_c(base, cout, mon):
    if base == "detecte": return "C3"
    if not cout: return "C1"
    if "repere" in mon: return "C4"
    if "indecis" in mon: return "C5"
    return "C6"
def issue(doses):  # doses : liste de None (hors B8) ou ligne C
    b8 = [d for d in doses if d]
    if not b8: return "sans objet"
    if "C6" in b8: return "une dose discrete"
    if all(d in ("C3", "C1", "C4") for d in b8): return "refutee"
    return "non concluante"
def partie_e():
    print("\n=== E. Table C (cinq moniteurs) et issue de 7.5")
    compte = {}
    for base in ("detecte", "ne detecte pas", "non calculable"):
        for cout in (True, False):
            for mon in itertools.product(("repere", "ne repere pas", "indecis"), repeat=5):
                l = ligne_c(base, cout, mon); compte[l] = compte.get(l, 0) + 1
    print("cas par ligne :", dict(sorted(compte.items())), "; total", sum(compte.values()), "(3 x 2 x 243 = 1458) : une ligne et une seule")
    iss = {}
    for doses in itertools.product((None, "C3", "C1", "C4", "C5", "C6"), repeat=3):
        i = issue(list(doses)); iss[i] = iss.get(i, 0) + 1
    print("issues sur 216 combinaisons de trois doses :", iss)
    print("C6 avec base « non calculable » : atteint (la phrase longue de 7.7 ecrit pourtant « ne le detecte pas »)")
    seul_juge = ligne_c("ne detecte pas", True, ("ne repere pas",) * 4 + ("indecis",))
    print("quatre moniteurs « ne reperent pas », juge indecis ->", seul_juge)

# ------------------------------------------------------------------ F
def holm_ajuste(p):
    m = len(p); o = np.argsort(p); adj = np.empty(m); cur = 0.0
    for rang, i in enumerate(o):
        cur = max(cur, min(1.0, (m - rang) * p[i])); adj[i] = cur
    return adj
def partie_f():
    print("\n=== F. Regle de 6.9 a m = 15")
    r = rng(6, 0); viol = 0
    for _ in range(20000):
        p = r.random(15) ** r.choice([1, 3, 8]); a = holm_ajuste(p)
        viol += int(np.any((a <= 0.05) & (p > 0.05)))
    print("« repere » (ajustee <= 0,05) et condition (a) de « ne repere pas » (brute > 0,05) ensemble :", viol, "cas sur 20 000 tirages")
    print("puissance de « ne repere pas » pour un moniteur REELLEMENT aveugle (scores sans rapport avec la condition) :")
    print("aire par tache puis moyenne des 16 taches ; borne haute = quantile 1 - 0,05/15 de 2 000 reechantillonnages des taches ; condition (a) par 2 000 permutations dans la tache")
    reps = 600
    for nom, n in (("unite episode : 8 contre 8 par tache (agregateur sequentiel)", 8),
                   ("unite action, sous-echantillon du juge : 32 contre 32 par tache", 32),
                   ("unite action, lecture entiere : 80 contre 80 par tache", 80)):
        for rho in (0.0, 0.3):
            g = rng(6, n, int(rho * 10)); ok_b = ok_ab = 0
            for _ in range(reps):
                aucs = np.empty(16); nulle = np.empty((16, 400))
                for t in range(16):
                    # correlation intra-episode pour l'unite action : effet d'episode commun (8 episodes par classe)
                    if n == 8:
                        a = g.standard_normal(8); b = g.standard_normal(8)
                    else:
                        ea = np.repeat(g.standard_normal(8), n // 8); eb = np.repeat(g.standard_normal(8), n // 8)
                        a = math.sqrt(rho) * ea + math.sqrt(1 - rho) * g.standard_normal(n)
                        b = math.sqrt(rho) * eb + math.sqrt(1 - rho) * g.standard_normal(n)
                    tout = np.concatenate([a, b])
                    aucs[t] = (a[:, None] < b[None, :]).mean()
                    for k in range(400):
                        perm = g.permutation(tout); nulle[t, k] = (perm[:n, None] < perm[None, n:]).mean()
                obs = aucs.mean(); pval = (1 + np.sum(nulle.mean(axis=0) >= obs)) / 401
                idx = g.integers(0, 16, (2000, 16)); haut = np.quantile(aucs[idx].mean(axis=1), 1 - 0.05 / 15)
                ok_b += haut < 0.60; ok_ab += (haut < 0.60) and (pval > 0.05)
            print(f"{nom}, correlation dans l'episode {rho:.1f} : (b) tenue {ok_b / reps:.2f} ; (a) et (b) tenues {ok_ab / reps:.2f}")
    print("(400 permutations ici au lieu de 2 000, pour le temps de calcul ; la permutation des etiquettes est faite par action, comme l'ecrit 6.9 a la lettre)")

if __name__ == "__main__":
    partie_a(); partie_b(); partie_c(); partie_d(); partie_e(); partie_f()
