"""Largeur locale du puits dans le jouet de l'exposé sur le graphe méta-mathématique
(question 9), v2, pour l'erratum 1 de la réponse. La v1 reste archivée sans modification.

Pièce de travail (classe C). Processeur seul, aucune dépense, aucun modèle, aucun réseau.

Correction visée (contre-lecture du 24 novembre, majeur de la question 9) : la v1 lisait
« le puits est étroit » sur la part GLOBALE des bijections au hasard proches du maximum,
alors que l'acquis du dossier définit l'étroitesse par une perturbation LOCALE de la
correspondance (changer une ou deux paires). On mesure ici :

1. le voisinage de phi à distance de Cayley d (d transpositions ; d = 9 - nombre de cycles
   de phi^-1 o psi sur les neuf nœuds appariables), pour d = 1 à 8 : effectif, nombre de
   bijections à un huitième de phi ou mieux, à égalité ou au-dessus, strictement au-dessus ;
   puis la même chose en n'admettant que les bijections qui conservent le type des nœuds ;
2. le détail des 36 transpositions de phi (changer une paire) ;
3. la contrainte phi(a) = b de la définition de Fable (a = composition, b = composition_B) ;
4. une borne pour les injections partielles (définition de Fable) : aucune relation de A dont
   le type manque dans B ne peut être confirmée, d'où c <= 5/8 et c - kappa <= 0,625 ;
   contrôle par tirage de 200 000 injections partielles au hasard (graine SeedSequence).

Les données du jouet (A, B, PHI, types des nœuds) sont lues dans la v1 elle-même, dont
l'empreinte est vérifiée au chargement, pour garantir le même jouet.
Utilisation : python -I exemple-graphe-meta-mathematique-v2.py
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import sys
from collections import Counter
from pathlib import Path

import numpy as np

GRAINE_RACINE = 20261124  # consignée (R9) ; tâche 4 de cette v2
EMPREINTE_V1 = "16e6bb1e33c72a489878f1350d62e87ffc68ae41ffdb87a2ea174ce349d65287"

chemin_v1 = Path(__file__).resolve().with_name("exemple-graphe-meta-mathematique-v1.py")
h = hashlib.sha256(chemin_v1.read_bytes()).hexdigest()
if h != EMPREINTE_V1:
    sys.exit(f"empreinte de la v1 inattendue : {h}")
spec = importlib.util.spec_from_file_location("jouet_v1", chemin_v1)
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
A, B, PHI, quatre_cas = v1.A, v1.B, v1.PHI, v1.quatre_cas

TYPE_NOEUD = {
    "composition": "operation", "composition_B": "operation",
    "substitutions": "ensemble", "ensemble_clos": "ensemble",
    "classes": "ensemble", "genre_principal": "ensemble",
    "identite": "element", "inverse": "element",
    "classe_principale": "element", "classe_opposee": "element",
    "associativite": "propriete", "commutativite": "propriete",
    "associativite_B": "propriete", "commutativite_B": "propriete",
    "nombre_valeurs": "nombre", "ordre_total": "nombre",
    "ordre_classe": "nombre", "nombre_classes": "nombre",
}  # recopié de la v1, partie 1 (variable locale de partie_1, non importable)

noeuds_a = list(PHI.keys())
noeuds_b = [PHI[a] for a in noeuds_a]
EPS = 1e-12


def score(phi):
    _, c, k = quatre_cas(A, B, phi)
    return c - k


def distance_cayley(perm):
    """perm : tuple d'images des noeuds_a ; distance en transpositions à PHI."""
    pos = {b: i for i, b in enumerate(noeuds_b)}
    sigma = [pos[b] for b in perm]
    vus, cycles = [False] * len(sigma), 0
    for i in range(len(sigma)):
        if not vus[i]:
            cycles += 1
            j = i
            while not vus[j]:
                vus[j] = True
                j = sigma[j]
    return len(sigma) - cycles


def type_conserve(phi):
    return all(TYPE_NOEUD[a] == TYPE_NOEUD[phi[a]] for a in noeuds_a)


s_phi = score(PHI)
print(f"numpy {np.__version__} ; python {sys.version.split()[0]} ; graine racine {GRAINE_RACINE} ; "
      f"v1 sha256 {h}")
print(f"score de phi : c - kappa = {s_phi:.3f} ; seuil « à un huitième de phi » : {s_phi - 0.125:.3f}")

par_d = {}
par_d_type = {}
tous = []
for perm in itertools.permutations(noeuds_b):
    phi = dict(zip(noeuds_a, perm))
    s = score(phi)
    d = distance_cayley(perm)
    tous.append(s)
    par_d.setdefault(d, []).append(s)
    if type_conserve(phi):
        par_d_type.setdefault(d, []).append(s)
tous = np.array(tous)


def ligne(d, v):
    v = np.array(v)
    return (f"  d={d} : {v.size:6d} bijections ; >= phi - 1/8 : {int((v >= s_phi - 0.125 - EPS).sum()):6d} "
            f"({(v >= s_phi - 0.125 - EPS).mean():.3f}) ; >= phi : {int((v >= s_phi - EPS).sum()):5d} "
            f"({(v >= s_phi - EPS).mean():.3f}) ; > phi : {int((v > s_phi + EPS).sum()):3d} ; "
            f"max {v.max():.3f}")


print("== 1. Voisinage de phi par distance de Cayley (toutes bijections)")
for d in sorted(par_d):
    print(ligne(d, par_d[d]))
print(f"  global : {tous.size} ; >= phi - 1/8 : {int((tous >= s_phi - 0.125 - EPS).sum())} "
      f"(part {(tous >= s_phi - 0.125 - EPS).mean():.2e}) ; >= phi : {int((tous >= s_phi - EPS).sum())} "
      f"(part {(tous >= s_phi - EPS).mean():.2e}) ; > phi : {int((tous > s_phi + EPS).sum())}")
print("== 1 bis. Même voisinage, bijections qui conservent le type des nœuds seulement")
for d in sorted(par_d_type):
    print(ligne(d, par_d_type[d]))

print("== 2. Les 36 transpositions de phi (une paire d'images échangée)")
compte = Counter()
for a1, a2 in itertools.combinations(noeuds_a, 2):
    phi = dict(PHI)
    phi[a1], phi[a2] = PHI[a2], PHI[a1]
    s = score(phi)
    cas, _, _ = quatre_cas(A, B, phi)
    rang = ">" if s > s_phi + EPS else ("=" if abs(s - s_phi) < EPS else
                                        ("-1/8" if s >= s_phi - 0.125 - EPS else "<"))
    compte[rang] += 1
    print(f"  {a1} <-> {a2} : c - kappa = {s:.3f} [{rang}] ; types conservés : {type_conserve(phi)} ; "
          f"cas {dict(Counter(cas))}")
print(f"  bilan des 36 : {dict(compte)}")

print("== 3. Contrainte phi(composition) = composition_B (définition de Fable, phi(a) = b)")
v = []
for perm in itertools.permutations(noeuds_b):
    phi = dict(zip(noeuds_a, perm))
    if phi["composition"] == "composition_B":
        v.append(score(phi))
v = np.array(v)
print(f"  bijections : {v.size} ; max {v.max():.3f} ; au max : {int((v >= v.max() - EPS).sum())} ; "
      f">= phi : {int((v >= s_phi - EPS).sum())} ; > phi : {int((v > s_phi + EPS).sum())} ; "
      f">= phi - 1/8 : {int((v >= s_phi - 0.125 - EPS).sum())} (part {(v >= s_phi - 0.125 - EPS).mean():.2e})")

print("== 4. Injections partielles (noeuds de A, résolvante comprise, vers B ou rien)")
types_b = {t for _, t, _ in B}
confirmables = sum(1 for _, t, _ in A if t in types_b)
print(f"  relations de A dont le type existe dans B : {confirmables} sur {len(A)} ; "
      f"borne c - kappa <= {confirmables / len(A):.3f}")
noeuds_a_tous = noeuds_a + ["resolvante"]
cibles = sorted(set(noeuds_b))
rng = np.random.default_rng(np.random.SeedSequence(GRAINE_RACINE, spawn_key=(4,)))
meilleur, n_tir = -1.0, 200_000
for _ in range(n_tir):
    k = int(rng.integers(0, len(cibles) + 1))
    dom = rng.choice(len(noeuds_a_tous), size=k, replace=False)
    img = rng.choice(len(cibles), size=k, replace=False)
    phi = {noeuds_a_tous[i]: cibles[j] for i, j in zip(dom, img)}
    meilleur = max(meilleur, score(phi))
print(f"  {n_tir} injections partielles tirées au hasard : meilleur c - kappa = {meilleur:.3f}")
