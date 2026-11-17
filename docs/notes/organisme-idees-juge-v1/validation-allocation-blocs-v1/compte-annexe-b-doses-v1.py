"""Compte de dimensionnement des doses neuves du banc C v1 (annexe B du préenregistrement de la validation propre de
l'allocation par blocs, brouillon 3) : processeur seul ; aucun juge, aucun nul, aucune issue jugée, aucune donnée de run.
Information moyenne par épisode E_x KL(monde || S1), en nat, des cinq types V1 à V5, construits exactement comme l'annexe A
du banc B v1 (V1 à V4, script c52b8222...) et l'annexe A du préenregistrement de l'idée 1.2 (V5, script ffa8d9b6...) ;
300 mondes par type, 4 000 instances par monde ; pour chaque type, les quatre doses (les deux de l'idée 1.2 et les deux
doses neuves) sont comptées sur les **mêmes** 300 mondes. Graine d'essai : SeedSequence(20261117), jamais la racine du
texte ni une clé du banc. Contrôle de la copie avant le compte : les quinze lignes des deux annexes publiées, rejouées
dans leur ordre et sur leur graine (20261115), sont retrouvées à l'identique. Ne mesure aucune promotion."""
import numpy as np

K, D = 3, 2
SEUIL_UNE_CARTE = float(np.log(24 / 0.05))  # log(m / alpha) = log 480


def soft(rng):
    return np.round(rng.normal(0, 1.5, size=(K, D)), 6), np.round(rng.normal(0, 0.3, size=K), 6)


def p_soft(W, b, z):
    s = z @ W.T + b
    s -= s.max(axis=1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(axis=1, keepdims=True)


def kl(p, q):
    return float(np.mean(np.sum(p * (np.log(p) - np.log(q)), axis=1)))


def u_centre(rng):
    u = rng.normal(size=K); u -= u.mean(); return u / np.linalg.norm(u)


def info(nom, dose, s):
    """Même suite de tirages que les deux scripts publiés, pour un monde (graine s) et une dose."""
    rng = np.random.default_rng(s)
    W1, b1 = soft(rng)
    if nom == "V5":
        z = rng.normal(size=(4000, D))
        jA = int(rng.integers(0, 2)); t = 1 - jA
        sA = round(float(rng.choice([-1, 1]) * rng.uniform(0.3, 1.0)), 2)
        E = np.zeros((K, D)); E[:, t] = u_centre(rng)
        pm = np.where((z[:, jA] > sA)[:, None], p_soft(W1 + dose * E, b1, z), p_soft(W1 - dose * E, b1, z))
        return kl(pm, p_soft(W1, b1, z))
    z = rng.normal(size=(4000, D)); g = rng.integers(0, 2, size=4000)
    p1 = p_soft(W1, b1, z)
    if nom == "V1":
        Wn = rng.normal(size=(K, D)); Wn -= Wn.mean(axis=0)
        pm = p_soft(W1 + dose * Wn, b1, z)
    elif nom in ("V2", "V3"):
        j = int(rng.integers(0, 2)); t = 1 - j
        c = 0.0 if nom == "V2" else float(rng.choice([-1, 1]) * rng.uniform(0.3, 0.8))
        E = np.zeros((K, D)); E[:, t] = u_centre(rng)
        pm = np.where((z[:, j] > c)[:, None], p_soft(W1 + dose * E, b1, z), p_soft(W1 - dose * E, b1, z))
    else:
        Wn, bn = soft(rng)
        pm = np.where((g == 1)[:, None], (1 - dose) * p1 + dose * p_soft(Wn, bn, z), p1)
    return kl(pm, p1)


TYPES = (("V1", "effet neuf global", (0.25, 0.375, 0.5, 0.625)),
         ("V2", "conditionnelle au signe", (0.4, 0.6, 0.8, 1.0)),
         ("V3", "conditionnelle à seuil décentré", (0.4, 0.6, 0.8, 1.0)),
         ("V4", "loi neuve sur une sous-population", (0.1, 0.15, 0.2, 0.25)),
         ("V5", "conditionnelle à une coupure de l'archive", (0.4, 0.6, 0.8, 1.0)))
NEUVES = {"V1": (0.375, 0.625), "V2": (0.6, 1.0), "V3": (0.6, 1.0), "V4": (0.15, 0.25), "V5": (0.6, 1.0)}

# Contrôle de la copie : rejouée dans l'ordre des deux scripts publiés (graine 20261115), la fonction `info` doit rendre
# leurs quinze lignes (médiane, quartiles, nats sur 200 épisodes) ; sinon arrêt.
PUBLIE = {("V1", 0.25): ("0.0112", "0.0062", "0.0208", "2.2"), ("V1", 0.5): ("0.0611", "0.0283", "0.0993", "12.2"),
          ("V1", 0.75): ("0.1143", "0.0564", "0.1988", "22.9"), ("V2", 0.4): ("0.0107", "0.0078", "0.0148", "2.1"),
          ("V2", 0.8): ("0.0441", "0.0318", "0.0586", "8.8"), ("V2", 1.2): ("0.1011", "0.0718", "0.1271", "20.2"),
          ("V3", 0.4): ("0.0122", "0.0085", "0.0158", "2.4"), ("V3", 0.8): ("0.0429", "0.0290", "0.0555", "8.6"),
          ("V3", 1.2): ("0.0993", "0.0675", "0.1319", "19.9"), ("V4", 0.1): ("0.0151", "0.0079", "0.0303", "3.0"),
          ("V4", 0.2): ("0.0491", "0.0214", "0.0830", "9.8"), ("V4", 0.3): ("0.0890", "0.0426", "0.1559", "17.8"),
          ("V5", 0.4): ("0.0111", "0.0075", "0.0146", "2.2"), ("V5", 0.8): ("0.0464", "0.0309", "0.0608", "9.3"),
          ("V5", 1.2): ("0.1000", "0.0678", "0.1272", "20.0")}


def resume(v):
    """Les quatre nombres de la ligne publiée, écrits comme les scripts publiés les écrivent."""
    return (f"{np.median(v):.4f}", f"{np.quantile(v, .25):.4f}", f"{np.quantile(v, .75):.4f}", f"{200 * np.median(v):.1f}")


r_banc = np.random.SeedSequence(20261115)
for nom, doses in (("V1", (0.25, 0.5, 0.75)), ("V2", (0.4, 0.8, 1.2)), ("V3", (0.4, 0.8, 1.2)), ("V4", (0.1, 0.2, 0.3))):
    for dose in doses:
        if resume(np.array([info(nom, dose, s) for s in r_banc.spawn(300)])) != PUBLIE[(nom, dose)]:
            raise SystemExit(f"contrôle de la copie : {nom} dose {dose} différent de l'annexe publiée, arrêt")
r_t = np.random.SeedSequence(20261115)
for dose in (0.4, 0.8, 1.2):
    if resume(np.array([info("V5", dose, s) for s in r_t.spawn(300)])) != PUBLIE[("V5", dose)]:
        raise SystemExit(f"contrôle de la copie : V5 dose {dose} différent de l'annexe publiée, arrêt")
print("contrôle de la copie : les quinze lignes des deux annexes publiées sont retrouvées à l'identique")

racine = np.random.SeedSequence(20261117)
for nom, libelle, doses in TYPES:
    enfants = racine.spawn(300)
    for dose in doses:
        v = np.array([info(nom, dose, s) for s in enfants])
        etiquette = "neuve" if dose in NEUVES[nom] else "idée 1.2"
        part = float(np.mean(200 * v >= SEUIL_UNE_CARTE))
        print(f"{nom} {libelle:42s} dose {dose:5.3f} ({etiquette:8s}) : médiane {np.median(v):.4f} nat/épisode "
              f"[quartiles {np.quantile(v, .25):.4f} ; {np.quantile(v, .75):.4f}] ; sur 200 épisodes : {200 * np.median(v):.1f} nat ; "
              f"part des mondes à 200 épisodes au-dessus de log 480 : {part:.2f}")
