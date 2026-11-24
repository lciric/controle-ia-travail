"""Partie C refaite pour l'erratum 2 de la réponse à la question 4 (émergence), v3.
Les v1 et v2 restent archivées sans modification.

Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle. Paramètres marqués « posé » :
hypothèses de planification, non des mesures.

Constat visé (seconde contre-lecture du 24 novembre, Opus 5.5 effort maximal, majeur Q4-M1) : les
v1 et v2 tirent une seule réalisation de percolation, commune aux deux moitiés d'une composite ;
elles se rencontrent si et seulement si leurs détenteurs sont dans le même amas ouvert. Or la pièce
dit « chaque saut transmet une moitié avec la probabilité f ». Si chaque moitié se perd à part, les
moitiés se rencontrent dès que l'ensemble atteint par l'une recoupe l'ensemble atteint par l'autre,
ce qui est plus probable. Le nombre de tours du protocole n'entre pas non plus dans la prédiction.

Modèles de transmission (même graphe de communication G(N, c/(N-1)) pour tous, nombres aléatoires
communs par dose) :
- lecture « arête » (chaque saut, voisin direct compris, coûte f) :
  commune     : un seul masque d'arêtes ouvert à f, pour les deux moitiés (v1, v2) ;
  partielle   : le masque de la moitié B recopie celui de A avec la probabilité pi_comm, sinon
                tirage propre (pi_comm = 1 : commune ; pi_comm = 0 : indépendantes) ;
  indépendantes : un masque par moitié, tiré une fois (chaque arête décide une fois par moitié) ;
  renouvelées : à chaque tour, chaque transmission d'une moitié sur une arête réussit avec la
                probabilité f, tirage neuf (un agent renvoie à chaque tour ce qu'il tient).
- lecture « relais » (contact direct sans perte ; un intermédiaire relaie avec la probabilité f ;
  sémantique de la v2 : un nœud fermé pour une moitié ne la reçoit ni ne la transmet ; les deux
  détenteurs sont ouverts) : commune (v2), partielle, indépendantes. Variante renouvelée non calculée.
Une moitié avance d'un saut par tour ; « T tours » : réunion en un nœud au plus tard au tour T ;
« illimité » : N - 1 tours (amas entier). Recouvrement d'une composite = eps + (h - eps) * réunion.

Parties :
C0. Contrôle : la lecture « arête » commune illimitée redonne la v2 (0,111 ; 0,353 ; 0,656).
C1. Probabilité de réunion et recouvrement, N = 16, f = 0,8 et 0,6, doses 0,5 à 4, T = 1 à 6 et
    illimité, sous chaque modèle.
C2. Tours du protocole à budget égal, d'après le modèle de coût de la partie E de la v1.
C3. Rejet à tort de la courbe « commune illimitée » (prédiction des v1 et v2) par un test
    d'adéquation (rapport de vraisemblance, 4 degrés de liberté, seuil 0,05) quand la vérité est
    un autre modèle ; même calcul pour la formule fautive de E0 (h pris à r(1)), que l'erratum 1
    jugeait « assez pour rejeter à tort la percolation ». h et f sont pris exacts : le test réel,
    qui les estime, serait un peu moins sévère.
C4. Discrimination percolation contre voisins directs (comme la v1, C3) quand la vérité est un
    autre modèle de transmission et que la prédiction reste la courbe commune.

Graines par numpy.random.SeedSequence (règle R9) : racine 20261124, clé (5,), qu'aucun autre script
du dossier n'emploie (v1 : enfants (0,) à (3,) ; v2 : (3,), qui recouvre la partie D de la v1 ;
cinétique v2 : (2,) ; graphe v2 : (4,)). Une graine fille par dose et par valeur de f, puis une par
case de C3 et C4.
Usage : python -I -B simulation-emergence-organisme-v3.py  (numpy >= 1.25)
"""
import hashlib
import math
import sys
from pathlib import Path

import numpy as np

GRAINE_RACINE = 20261124
CLE = (5,)
N, KC, H, EPS = 16, 4, 0.7, 0.02  # posés, comme les v1 et v2
DOSES = [0.5, 1.0, 2.0, 4.0]
F_LISTE = [0.8, 0.6]
TOURS = [1, 2, 3, 4, 5, 6]
ILLIM = N - 1
B = 20000
PI_PARTIELLE = 0.5
X2_4DL_05 = 9.487729036781154  # quantile 0,95 du khi-deux à 4 degrés de liberté

script = Path(__file__).resolve()
print(f"# script sha256 {hashlib.sha256(script.read_bytes()).hexdigest()}")
print(f"numpy {np.__version__} ; python {sys.version.split()[0]} ; graine racine {GRAINE_RACINE}, clé {CLE}")
print(f"posés : N = {N}, h = {H}, eps = {EPS}, {KC} composites par course, {B} graphes par case")

ss = np.random.SeedSequence(GRAINE_RACINE, spawn_key=CLE)
ss_c1, ss_c3, ss_c4 = ss.spawn(3)
cel_c1 = ss_c1.spawn(len(DOSES) * len(F_LISTE))


def sym(u):
    tri = np.triu(u, 1)
    return tri | np.transpose(tri, (0, 2, 1))


def graphe(rng, c):
    return sym(rng.random((B, N, N)) < min(1.0, c / (N - 1)))


def portees(adj, src):
    """Ensembles atteints depuis src après 0, 1, ..., ILLIM sauts ; adj (B, N, N) sans diagonale."""
    r = np.zeros((B, N), dtype=bool)
    r[:, src] = True
    out = [r]
    for _ in range(ILLIM):
        r = r | (r[:, :, None] & adj).any(axis=1)
        out.append(r)
    return out


def portees_renouvelees(rng, G, f, src):
    r = np.zeros((B, N), dtype=bool)
    r[:, src] = True
    out = [r]
    for _ in range(ILLIM):
        m = G & (rng.random((B, N, N)) < f)  # tirage neuf, chaque sens à part
        r = r | (r[:, :, None] & m).any(axis=1)
        out.append(r)
    return out


def reunion(pa, pb):
    """Probabilité que les deux moitiés soient réunies en un nœud au plus tard à chaque tour t."""
    return np.array([(a & b).any(axis=1).mean() for a, b in zip(pa, pb)])


def masques_aretes(rng, G, f, pi_comm):
    ma = G & sym(rng.random((B, N, N)) < f)
    propre = G & sym(rng.random((B, N, N)) < f)
    copie = sym(rng.random((B, N, N)) < pi_comm)
    mb = np.where(copie, ma, propre)
    return ma, mb


def masques_sites(rng, G, f, pi_comm):
    oa = rng.random((B, N)) < f
    propre = rng.random((B, N)) < f
    copie = rng.random((B, N)) < pi_comm
    ob = np.where(copie, oa, propre)
    oa[:, :2] = True
    ob[:, :2] = True
    return G & oa[:, :, None] & oa[:, None, :], G & ob[:, :, None] & ob[:, None, :]


MODELES = [("arête", "commune"), ("arête", "partielle"), ("arête", "indépendantes"),
           ("arête", "renouvelées"), ("relais", "commune"), ("relais", "partielle"),
           ("relais", "indépendantes")]

# ---------- C1 ----------
reu = {}  # (lecture, modèle, f, c) -> vecteur de réunion par tour (0 .. ILLIM)
k = 0
for f in F_LISTE:
    for c in DOSES:
        rng = np.random.default_rng(cel_c1[k]); k += 1
        G = graphe(rng, c)
        for lecture, modele in MODELES:
            if modele == "renouvelées":
                pa = portees_renouvelees(rng, G, f, 0)
                pb = portees_renouvelees(rng, G, f, 1)
            else:
                pi_comm = {"commune": 1.0, "partielle": PI_PARTIELLE, "indépendantes": 0.0}[modele]
                if lecture == "arête":
                    ma, mb = masques_aretes(rng, G, f, pi_comm)
                else:
                    ma, mb = masques_sites(rng, G, f, pi_comm)
                pa, pb = portees(ma, 0), portees(mb, 1)
            reu[(lecture, modele, f, c)] = reunion(pa, pb)


def rec(p):
    return EPS + (H - EPS) * p


print()
print("C0. Contrôle contre la v2 (lecture « arête », commune, illimité, f = 0,8) : "
      + " ; ".join(f"c = {c:g} : {rec(reu[('arête', 'commune', 0.8, c)][ILLIM]):.3f}" for c in DOSES)
      + "   [v2 : 0,050 ; 0,111 ; 0,353 ; 0,656]")
print("    lecture « relais », commune, illimité : "
      + " ; ".join(f"c = {c:g} : {rec(reu[('relais', 'commune', 0.8, c)][ILLIM]):.3f}" for c in DOSES)
      + "   [v2 : 0,055 ; 0,129 ; 0,382 ; 0,660]")

print()
print(f"C1. Recouvrement attendu d'une composite, eps + (h - eps) x réunion ; partielle : pi_comm = {PI_PARTIELLE}")
for f in F_LISTE:
    print(f"  f = {f}")
    print("  lecture  modèle          tours " + "".join(f"   c={c:<4g}" for c in DOSES)
          + "   écart relatif à la commune illimitée, c = 1 / 2 / 4")
    for lecture, modele in MODELES:
        for T in TOURS + [ILLIM]:
            v = [rec(reu[(lecture, modele, f, c)][T]) for c in DOSES]
            ref = [rec(reu[(lecture, "commune", f, c)][ILLIM]) for c in DOSES]
            ecarts = " / ".join(f"{100 * (v[i] / ref[i] - 1):+5.1f} %" for i in (1, 2, 3))
            nom_t = "illim." if T == ILLIM else str(T)
            print(f"  {lecture:<7s}  {modele:<14s}  {nom_t:<6s}" + "".join(f"  {x:7.3f}" for x in v)
                  + f"   {ecarts}")

# ---------- C2 ----------
print()
print("C2. Tours à budget égal (modèle de coût de la partie E de la v1 : vue 1 500, mémoire 750, "
      "sortie 500, réflexion 2 000 jetons par tour ; tarifs de Neon 3/15 USD par million) :")
vue, memoire, sortie, pensee, R = 1500, 750, 500, 2000, 4


def cout_tour(d, n=N):
    return n * (vue + memoire + d * sortie) * 3e-6 + n * (sortie + pensee) * 15e-6


budget_dose = max(R * cout_tour(d) for d in DOSES)
ent_ic = N * R * (vue + memoire + (N - 1) * sortie)
budget_complet = ent_ic * 3e-6 + N * R * (sortie + pensee) * 15e-6
for nom, bud in (("plan réduit (budget = dose la plus chère, 4 tours)", budget_dose),
                 ("plan complet (budget = interaction complète, 4 tours)", budget_complet)):
    tours = {c: int(math.floor(bud / cout_tour(c) + 1e-9)) for c in DOSES}
    print(f"  {nom} : {bud:.2f} USD par course ; tours par dose : "
          + ", ".join(f"c = {c:g} : {t}" for c, t in tours.items()))

# ---------- C3 ----------
print()
print("C3. Rejet de la courbe prédite « commune illimitée » par le test d'adéquation (4 doses, "
      "4 degrés de liberté, seuil 0,05), f = 0,8, 4 000 répétitions par case")
rng = np.random.default_rng(ss_c3)
F0 = 0.8


def courbe(lecture, modele, T):
    return np.array([rec(reu[(lecture, modele, F0, c)][T]) for c in DOSES])


def taux_rejet(rng, q_vrai, q_pred, M, rep=4000):
    n = M * KC
    x = rng.binomial(n, np.broadcast_to(q_vrai, (rep, len(DOSES))))
    with np.errstate(divide="ignore", invalid="ignore"):
        t1 = np.where(x > 0, x * np.log(x / (n * q_pred)), 0.0)
        t2 = np.where(n - x > 0, (n - x) * np.log((n - x) / (n * (1 - q_pred))), 0.0)
    g = 2 * (t1 + t2).sum(axis=1)
    return (g > X2_4DL_05).mean()


for lecture in ("arête", "relais"):
    pred = courbe(lecture, "commune", ILLIM)
    verites = [("commune illimitée (taille du test)", pred),
               ("indépendantes, 4 tours", courbe(lecture, "indépendantes", 4)),
               ("indépendantes, 5 tours", courbe(lecture, "indépendantes", 5)),
               ("indépendantes, illimité", courbe(lecture, "indépendantes", ILLIM)),
               ("partielle 0,5, illimité", courbe(lecture, "partielle", ILLIM))]
    if lecture == "arête":
        verites += [("renouvelées, 4 tours", courbe(lecture, "renouvelées", 4)),
                    ("renouvelées, 5 tours", courbe(lecture, "renouvelées", 5)),
                    ("formule fautive de E0 (h pris à h f)",
                     EPS + (H * F0 - EPS) * np.array([reu[(lecture, "commune", F0, c)][ILLIM] for c in DOSES]))]
    print(f"  lecture « {lecture} » ; prédiction : " + ", ".join(f"{q:.3f}" for q in pred))
    print("    vérité                                   M = 3    M = 5    M = 10   (courses par dose)")
    for nom, qv in verites:
        r = [taux_rejet(rng, qv, pred, M) for M in (3, 5, 10)]
        print(f"    {nom:<40s} " + "  ".join(f"{x:6.3f}" for x in r))

# ---------- C4 ----------
print()
print("C4. Choix percolation commune contre voisins directs (vraisemblance, comme la v1 C3), quand la "
      "vérité est un autre modèle de transmission ; f = 0,8, lecture « arête », 2 000 répétitions")
rng = np.random.default_rng(ss_c4)
pred = courbe("arête", "commune", ILLIM)
direct = np.array([EPS + (H - EPS) * min(1.0, c * F0 / (N - 1)) for c in DOSES])
print("    vérité                         M = 3    M = 5   (part des cas où la percolation est choisie)")
for nom, qv in (("commune illimitée", pred), ("indépendantes, 4 tours", courbe("arête", "indépendantes", 4)),
                ("renouvelées, 4 tours", courbe("arête", "renouvelées", 4)), ("voisins directs", direct)):
    r = []
    for M in (3, 5):
        n = M * KC
        x = rng.binomial(n, np.broadcast_to(qv, (2000, len(DOSES))))
        llp = (x * np.log(pred) + (n - x) * np.log(1 - pred)).sum(axis=1)
        lld = (x * np.log(direct) + (n - x) * np.log(1 - direct)).sum(axis=1)
        r.append((llp > lld).mean())
    print(f"    {nom:<30s} " + "  ".join(f"{x:6.3f}" for x in r))
