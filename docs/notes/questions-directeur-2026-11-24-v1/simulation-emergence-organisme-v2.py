"""Partie C refaite pour l'erratum 1 de la réponse à la question 4 (émergence), v2.
La v1 reste archivée sans modification ; ses parties A, B, D et E ne sont pas touchées.

Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle.

Correction visée (contre-lecture du 24 novembre, majeur de la question 4) : la v1 mesurait la
fidélité de relais f sur des chaînes avec r(L) = h * f^(L-1) (premier saut sans perte), mais
diluait chaque arête par f dans la percolation, voisin direct compris. Deux lectures cohérentes
existent ; il faut en choisir une et la tester avant la courbe de dose :

- lecture « arête » (percolation de liens) : chaque saut coûte f, r(L) = h * f^L, L = 0 à 4,
  h = r(0) mesuré directement (un agent tient les deux moitiés) ; voisins directs dilués par f ;
- lecture « relais » (percolation de sites aux intermédiaires) : le contact direct est sans perte,
  chaque intermédiaire relaie avec la probabilité f, r(L) = h * f^(L-1) pour L >= 1, r(0) = h ;
  voisins directs non dilués.
Le rapport r(1)/r(0) les sépare : f en lecture « arête », 1 en lecture « relais ».

C1. Précision de f (et du rapport r(1)/r(0)) avec L = 0 à 4.
C2. Courbes de dose à N = 16, sous chaque lecture, et la courbe qu'on obtiendrait en mêlant les
    deux comme la v1 (h pris à r(1) sous la vérité « arête »).
C3. Justesse du choix percolation contre voisins directs, sous chaque lecture cohérente.

Les fonctions de graphe sont lues dans la v1, dont l'empreinte est vérifiée au chargement.
Graines par numpy.random.SeedSequence (règle R9), arbre distinct de la v1 (spawn_key 3).
Usage : python -I -B simulation-emergence-organisme-v2.py  (numpy >= 1.25)
"""
import hashlib
import importlib.util
import math
import sys
from pathlib import Path

import numpy as np

EMPREINTE_V1 = "4b71ba517986177acbd245eae101ccc97b86f41c3484f9986d953442f6746446"
chemin_v1 = Path(__file__).resolve().with_name("simulation-emergence-organisme-v1.py")
h_v1 = hashlib.sha256(chemin_v1.read_bytes()).hexdigest()
if h_v1 != EMPREINTE_V1:
    sys.exit(f"empreinte de la v1 inattendue : {h_v1}")
spec = importlib.util.spec_from_file_location("emergence_v1", chemin_v1)
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
composantes, tirer_graphes = v1.composantes, v1.tirer_graphes

GRAINE_RACINE = 20261124
ss = np.random.SeedSequence(GRAINE_RACINE, spawn_key=(3,))
cel = ss.spawn(3)

N, KC, H, EPS = 16, 4, 0.7, 0.02  # posés, comme la v1
DOSES = [0.5, 1.0, 2.0, 4.0]
print(f"numpy {np.__version__} ; python {sys.version.split()[0]} ; graine racine {GRAINE_RACINE} ; "
      f"v1 sha256 {h_v1}")
print(f"posés : N = {N}, h = {H}, eps = {EPS}, {KC} composites par course")

# ---------- C1 ----------
rng = np.random.default_rng(cel[0])
grille_h = np.linspace(0.02, 0.99, 98)
grille_f = np.linspace(0.02, 1.0, 99)
Hh, Ff = np.meshgrid(grille_h, grille_f, indexing="ij")
Ls = np.arange(0, 5)
print("C1. Lecture « arête », r(L) = h f^L, L = 0 à 4 (h = r(0)) : estimation par maximum de vraisemblance")
print("  f_vrai  n/longueur  moyenne(f_est)  écart type(f_est)  écart type(h_est)  "
      "écart type de r(1)/r(0) observé")
rL = Hh[:, :, None] * Ff[:, :, None] ** Ls[None, None, :]
lr1, lr0 = np.log(rL), np.log1p(-np.minimum(rL, 1 - 1e-12))
for f in (0.8, 0.6):
    for n in (25, 50, 100):
        ef, eh, rap = [], [], []
        for _ in range(1000):
            y = rng.binomial(n, H * f ** Ls)
            ll = (y * lr1 + (n - y) * lr0).sum(axis=2)
            i, j = np.unravel_index(np.argmax(ll), ll.shape)
            ef.append(grille_f[j]); eh.append(grille_h[i])
            rap.append(y[1] / max(y[0], 1))
        print(f"  {f:<6.1f}  {n:<10d}  {np.mean(ef):6.3f}          {np.std(ef):6.3f}             "
              f"{np.std(eh):6.3f}             {np.std(rap):6.3f} (moyenne {np.mean(rap):.3f})")


# ---------- C2 ----------
def relies_sites(rng, B, c, f):
    """Lecture « relais » : graphe G(N, c/(N-1)) ; chaque intermédiaire ouvert avec la probabilité f ;
    les deux détenteurs (nœuds 0 et 1) toujours ouverts ; un nœud fermé perd ses arêtes."""
    adj = tirer_graphes(rng, B, N, min(1.0, c / (N - 1)))
    ouvert = rng.random((B, N)) < f
    ouvert[:, :2] = True
    masque = ouvert[:, :, None] & ouvert[:, None, :]
    idx = np.arange(N)
    adj = adj & masque
    adj[:, idx, idx] = True
    lab = composantes(adj)
    return (lab[:, 0] == lab[:, 1]).mean()


rng = np.random.default_rng(cel[1])
B = 20000
f = 0.8
courbes = {}
print(f"C2. Recouvrement attendu d'une composite, N = {N}, f = {f} :")
print("  c     arête:perco  arête:direct  mêlée(v1):perco  relais:perco  relais:direct")
for c in DOSES:
    adj = tirer_graphes(rng, B, N, min(1.0, c * f / (N - 1)))
    lab = composantes(adj)
    meet_arete = (lab[:, 0] == lab[:, 1]).mean()
    meet_relais = relies_sites(rng, B, c, f)
    courbes[("arete", "perco", c)] = EPS + (H - EPS) * meet_arete
    courbes[("arete", "direct", c)] = EPS + (H - EPS) * min(1.0, c * f / (N - 1))
    courbes[("melee", "perco", c)] = EPS + (H * f - EPS) * meet_arete  # h pris à r(1) = h f
    courbes[("relais", "perco", c)] = EPS + (H - EPS) * meet_relais
    courbes[("relais", "direct", c)] = EPS + (H - EPS) * min(1.0, c / (N - 1))
    print(f"  {c:<5.1f} {courbes[('arete','perco',c)]:8.3f}     {courbes[('arete','direct',c)]:8.3f}      "
          f"{courbes[('melee','perco',c)]:8.3f}         {courbes[('relais','perco',c)]:8.3f}      "
          f"{courbes[('relais','direct',c)]:8.3f}")

# ---------- C3 ----------
rng = np.random.default_rng(cel[2])
print(f"C3. Justesse du choix percolation contre voisins directs (vraisemblance), f = {f}, sous chaque lecture :")
print("  lecture  M courses/dose  vrai = percolation  vrai = voisins directs")
for lecture in ("arete", "relais"):
    for M in (3, 5):
        acc = []
        for vrai in ("perco", "direct"):
            bon = 0
            for _ in range(2000):
                ll = {"perco": 0.0, "direct": 0.0}
                for c in DOSES:
                    n = M * KC
                    x = rng.binomial(n, courbes[(lecture, vrai, c)])
                    for mod in ll:
                        q = courbes[(lecture, mod, c)]
                        ll[mod] += x * math.log(q) + (n - x) * math.log(1 - q)
                autre = "direct" if vrai == "perco" else "perco"
                bon += ll[vrai] > ll[autre]
            acc.append(bon / 2000)
        print(f"  {lecture:<8s} {M:<15d} {acc[0]:6.3f}              {acc[1]:6.3f}")
