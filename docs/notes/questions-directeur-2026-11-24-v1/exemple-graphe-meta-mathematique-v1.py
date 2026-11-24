"""Exemple mesuré de l'exposé sur le graphe méta-mathématique (question 9), v1.

Pièce de travail (classe C). Processeur seul, aucune dépense, aucun modèle.

Partie 1, jouet (sans réseau) : une correspondance phi entre deux petits
graphes typés, A (permutations des racines d'une équation, à la Lagrange) et
B (composition des classes de formes quadratiques binaires, à la Gauss). Les
relations sont simplifiées à dessein : c'est un jouet, non une histoire.
On calcule les quatre cas (confirmée, contredite, absente, extrémité sans
image), la couverture c, la part des conflits kappa, c - kappa ; on cherche
exhaustivement toutes les bijections des neuf nœuds appariables (largeur) ;
on perturbe les faits de B (robustesse) avec des graines SeedSequence.
Exercices vérifiables : paires non commutantes de S3, formes réduites de
discriminant -23, ordres des éléments divisant l'ordre du groupe.

Partie 2, données réelles (fichiers locaux passés en arguments) :
  --mathlib DOSSIER      dossier Mathlib/GroupTheory d'un commit daté de mathlib4
  --msc FICHIER          MSC_2020.csv (msc2020.org)
  --oeis FICHIER         JSON de l'OEIS pour A000001
  --zbmath               interroge api.zbmath.org (comptes par année, 13F60)

Utilisation : python -I exemple-graphe-meta-mathematique-v1.py [options]
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

GRAINE_RACINE = 20261124  # consignée ; dérivée par tâche (R9)

# ---------------------------------------------------------------- partie 1
A = [  # (source, type, cible) ; noms effacés pour le calcul, gardés pour lire
    ("composition", "est_loi_sur", "substitutions"),
    ("identite", "neutre_pour", "composition"),
    ("inverse", "inverse_pour", "composition"),
    ("composition", "verifie", "associativite"),
    ("composition", "refute", "commutativite"),   # dès trois racines
    ("nombre_valeurs", "divise", "ordre_total"),   # Lagrange, 1770-1771
    ("ensemble_clos", "sous_ensemble_de", "substitutions"),
    ("resolvante", "invariant_sous", "ensemble_clos"),
]
B = [
    ("composition_B", "est_loi_sur", "classes"),
    ("classe_principale", "neutre_pour", "composition_B"),
    ("classe_opposee", "inverse_pour", "composition_B"),
    ("composition_B", "verifie", "associativite_B"),
    ("composition_B", "verifie", "commutativite_B"),
    ("genre_principal", "sous_ensemble_de", "classes"),
    # aucune relation écrite entre ordre_classe et nombre_classes (jouet)
]
NOEUDS_B_ISOLES = ["ordre_classe", "nombre_classes"]
PHI = {
    "composition": "composition_B", "substitutions": "classes",
    "identite": "classe_principale", "inverse": "classe_opposee",
    "associativite": "associativite_B", "commutativite": "commutativite_B",
    "nombre_valeurs": "ordre_classe", "ordre_total": "nombre_classes",
    "ensemble_clos": "genre_principal",
}  # "resolvante" sans image
INCOMPATIBLES = {frozenset({"verifie", "refute"})}


def quatre_cas(rel_a, rel_b, phi):
    index = defaultdict(set)
    for x, t, y in rel_b:
        index[(x, y)].add(t)
    cas = []
    for x, t, y in rel_a:
        if x not in phi or y not in phi:
            cas.append("extremite_sans_image")
            continue
        types = index.get((phi[x], phi[y]), set())
        if t in types:
            cas.append("confirmee")
        elif any(frozenset({t, u}) in INCOMPATIBLES for u in types):
            cas.append("contredite")
        else:
            cas.append("absente")
    n = len(rel_a)
    c = cas.count("confirmee") / n
    k = cas.count("contredite") / n
    return cas, c, k


def partie_1(sortie):
    p = lambda *a: print(*a, file=sortie)
    p("== Partie 1 : correspondance jouet A (permutations) -> B (classes de formes)")
    cas, c, k = quatre_cas(A, B, PHI)
    for r, s in zip(A, cas):
        p(f"  {r[0]:>15} -{r[1]}-> {r[2]:<15} : {s}")
    p(f"  comptes : {dict(Counter(cas))}")
    p(f"  couverture c = {c:.3f} ; conflits kappa = {k:.3f} ; c - kappa = {c - k:.3f}")

    # Largeur : toutes les bijections des 9 nœuds appariables de A sur les 9 de B.
    noeuds_a = list(PHI.keys())
    noeuds_b = sorted(set(PHI.values()))
    scores = []
    phis = []
    for perm in itertools.permutations(noeuds_b):
        phi = dict(zip(noeuds_a, perm))
        _, c2, k2 = quatre_cas(A, B, phi)
        scores.append(c2 - k2)
        phis.append(phi)
    scores = np.array(scores)
    meilleurs = [phis[i] for i in np.flatnonzero(scores >= scores.max() - 1e-12)]
    p(f"  bijections examinées : {scores.size} ; maximum de c - kappa : {scores.max():.3f}")
    p(f"  bijections au maximum : {int((scores >= scores.max() - 1e-12).sum())}")
    p(f"  bijections à un huitième du maximum ou mieux : "
      f"{int((scores >= scores.max() - 0.125 - 1e-12).sum())} "
      f"(part {float((scores >= scores.max() - 0.125 - 1e-12).mean()):.2e})")
    p(f"  bijections strictement au-dessus de phi : {int((scores > (c - k) + 1e-12).sum())} ; "
      f"à égalité avec phi : {int((np.abs(scores - (c - k)) < 1e-12).sum())}")
    for m in meilleurs[:3]:
        cas2, c2, k2 = quatre_cas(A, B, m)
        p(f"  un maximum : écart à phi {{{', '.join(f'{a}->{m[a]}' for a in noeuds_a if m[a] != PHI[a])}}} ; "
          f"cas {dict(Counter(cas2))}")
    # Même recherche, en n'admettant que les bijections qui conservent le type des nœuds.
    type_noeud = {
        "composition": "operation", "composition_B": "operation",
        "substitutions": "ensemble", "ensemble_clos": "ensemble",
        "classes": "ensemble", "genre_principal": "ensemble",
        "identite": "element", "inverse": "element",
        "classe_principale": "element", "classe_opposee": "element",
        "associativite": "propriete", "commutativite": "propriete",
        "associativite_B": "propriete", "commutativite_B": "propriete",
        "nombre_valeurs": "nombre", "ordre_total": "nombre",
        "ordre_classe": "nombre", "nombre_classes": "nombre",
    }
    typees = [s for s, m in zip(scores, phis)
              if all(type_noeud[a] == type_noeud[m[a]] for a in noeuds_a)]
    typees = np.array(typees)
    p(f"  bijections qui conservent le type des nœuds : {typees.size} ; maximum {typees.max():.3f} ; "
      f"au maximum : {int((typees >= typees.max() - 1e-12).sum())} (phi en fait partie : "
      f"{abs(typees.max() - (c - k)) < 1e-12})")

    # Profondeur (robustesse) : on retire chaque fait de B avec probabilité 0,15.
    ss = np.random.SeedSequence(GRAINE_RACINE)
    rng = np.random.default_rng(ss.spawn(1)[0])
    vals = []
    for _ in range(2000):
        garde = rng.random(len(B)) >= 0.15
        b2 = [r for r, g in zip(B, garde) if g]
        _, c2, k2 = quatre_cas(A, b2, PHI)
        vals.append(c2 - k2)
    vals = np.array(vals)
    p(f"  faits de B retirés (p = 0,15, 2000 tirages, graine {GRAINE_RACINE}, tâche 0) : "
      f"c - kappa moyen {vals.mean():.3f}, quantiles 5 % et 95 % "
      f"{np.quantile(vals, 0.05):.3f} et {np.quantile(vals, 0.95):.3f}")

    # Réification : un nœud « groupe » ; la relation de Lagrange écrite une fois.
    p("  réification : nœud 'groupe' ajouté ; (sous_groupe, ordre_divise, groupe) "
      "remplace r6 et la relation prédite dans B ; le conflit sur la "
      "commutativité devient un paramètre (commutatif ou non), plus un conflit")

    p("== Exercices vérifiables")
    s3 = list(itertools.permutations(range(3)))
    comp = lambda f, g: tuple(f[g[i]] for i in range(3))
    nc = sum(1 for f in s3 for g in s3 if comp(f, g) != comp(g, f))
    p(f"  E1 paires ordonnées non commutantes dans S3 : {nc} sur {len(s3) ** 2}")
    formes = []
    D = -23
    for a in range(1, 10):
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            cc = (b * b - D) // (4 * a)
            if cc < a or (cc == a and b < 0):
                continue
            formes.append((a, b, cc))
    p(f"  E2 formes réduites de discriminant {D} : {formes} -> nombre de classes {len(formes)}")
    def ordre(f):
        e, k = f, 1
        while e != tuple(range(3)):
            e, k = comp(e, f), k + 1
        return k
    p(f"  E3 ordres des éléments de S3 : {sorted(ordre(f) for f in s3)} ; tous divisent 6 : "
      f"{all(6 % ordre(f) == 0 for f in s3)}")


# ---------------------------------------------------------------- partie 2
RE_IMPORT = re.compile(r"^(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?(\S+)", re.M)


def partie_mathlib(dossier: Path, sortie):
    p = lambda *a: print(*a, file=sortie)
    racine = dossier.parent.parent  # .../Mathlib/GroupTheory -> dépôt
    fichiers = sorted(dossier.rglob("*.lean"))
    nom = lambda f: ".".join(f.relative_to(racine).with_suffix("").parts)
    noeuds = {nom(f) for f in fichiers}
    internes, externes = [], Counter()
    n_enonces = 0
    for f in fichiers:
        t = f.read_text(encoding="utf-8")
        n_enonces += len(re.findall(r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:theorem|lemma)\s", t, re.M))
        for m in RE_IMPORT.findall(t):
            if m in noeuds:
                internes.append((nom(f), m))
            else:
                parts = m.split(".")
                externes[parts[1] if parts[0] == "Mathlib" and len(parts) > 1 else parts[0]] += 1
    entrants = Counter(m for _, m in internes)
    p("== Partie 2a : graphe des importations de Mathlib/GroupTheory")
    p(f"  fichiers (nœuds) : {len(noeuds)} ; importations internes (arêtes) : {len(internes)}")
    p(f"  importations venues d'ailleurs : {sum(externes.values())} ; par section : "
      f"{externes.most_common(8)}")
    p(f"  fichiers les plus importés dans le sous-graphe : {entrants.most_common(5)}")
    # plus long chemin (graphe sans cycle attendu)
    succ = defaultdict(list)
    for a, b in internes:
        succ[a].append(b)
    memo = {}
    def prof(n, pile=()):
        if n in pile:
            raise ValueError("cycle")
        if n not in memo:
            memo[n] = 1 + max((prof(m, pile + (n,)) for m in succ[n]), default=0)
        return memo[n]
    p(f"  plus longue chaîne d'importations internes (fichiers) : {max(prof(n) for n in noeuds)}")
    p(f"  déclarations 'theorem' ou 'lemma' (comptage textuel, approché) : {n_enonces}")


def partie_msc(fichier: Path, sortie):
    p = lambda *a: print(*a, file=sortie)
    lignes = fichier.read_bytes().decode("latin-1").splitlines()[1:]
    codes, aretes = [], []
    re_code = re.compile(r"\b(\d{2}(?:-XX|[A-Z](?:xx|\d{2})|-\d{2}))\b")
    for l in lignes:
        champs = l.split("\t")
        if len(champs) < 3:
            continue
        code = champs[0].strip('"')
        codes.append(code)
        desc = champs[2]
        for bloc in re.findall(r"\[See also ([^\]]*)\]|\\\{For [^\\]*see (?:also )?([^\\]*)\\\}", desc):
            for cible in re_code.findall(" ".join(bloc)):
                aretes.append((code, cible))
    p("== Partie 2b : classification des sujets mathématiques 2020, renvois « See also » et « For … see »")
    p(f"  rubriques (nœuds) : {len(codes)} ; renvois (arêtes) : {len(aretes)}")
    hors = [(a, b) for a, b in aretes if a[:2] != b[:2]]
    p(f"  renvois vers une autre section de premier niveau : {len(hors)} ({len(hors) / max(1, len(aretes)):.1%})")
    de20 = Counter(b[:2] for a, b in aretes if a[:2] == "20" and b[:2] != "20")
    p(f"  depuis la théorie des groupes (20), sections visées : {de20.most_common(8)}")
    p(f"  rubrique 13F60 présente : {'13F60' in codes}")


def partie_oeis(fichier: Path, sortie):
    p = lambda *a: print(*a, file=sortie)
    d = json.loads(fichier.read_text(encoding="utf-8"))
    r = d[0] if isinstance(d, list) else d["results"][0]
    renvois = sorted(set(re.findall(r"A\d{6}", " ".join(r.get("xref", [])))) - {"A000001"})
    p("== Partie 2c : renvois de l'OEIS depuis A000001")
    p(f"  A{r['number']:06d} « {r['name']} », révision {r.get('revision')}, {r.get('time')}")
    p(f"  suites renvoyées (lignes de renvoi) : {len(renvois)}")


def partie_zbmath(sortie):
    p = lambda *a: print(*a, file=sortie)
    p("== Partie 2d : zbMATH Open, documents portant la rubrique 13F60 (algèbres amassées), par année")
    for y in range(2000, 2013):
        url = ("https://api.zbmath.org/v1/document/_search?search_string=cc%3A13F60%20py%3A"
               f"{y}&page=0&results_per_page=1")
        try:
            with urllib.request.urlopen(url, timeout=30) as rep:
                n = json.load(rep)["status"]["nr_total_results"]
        except urllib.error.HTTPError as e:  # 404 = aucun résultat pour cette API
            n = 0 if e.code == 404 else f"erreur {e.code}"
        p(f"  {y} : {n or 0}")
    url = ("https://api.zbmath.org/v1/document/_search?search_string=ti%3A%22cluster%20algebras%22"
           "%20py%3A2003-2006&page=0&results_per_page=50")
    with urllib.request.urlopen(url, timeout=30) as rep:
        docs = json.load(rep)["result"]
    codes = [[m.get("code") for m in d.get("msc", [])] for d in docs]
    sections = Counter(c[:2] for cs in codes for c in set(x[:2] for x in cs) for c in [c])
    p(f"  titres contenant « cluster algebras », 2003-2006 : {len(docs)} ; portant 13F60 : "
      f"{sum('13F60' in cs for cs in codes)} ; sans rubrique : {sum(not cs for cs in codes)}")
    p(f"  sections de premier niveau touchées (une fois par document) : {len(sections)} -> "
      f"{sorted(sections.items())}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mathlib", type=Path)
    ap.add_argument("--msc", type=Path)
    ap.add_argument("--oeis", type=Path)
    ap.add_argument("--zbmath", action="store_true")
    a = ap.parse_args()
    s = sys.stdout
    print(f"numpy {np.__version__} ; python {sys.version.split()[0]} ; graine racine {GRAINE_RACINE}", file=s)
    partie_1(s)
    if a.mathlib:
        partie_mathlib(a.mathlib, s)
    if a.msc:
        partie_msc(a.msc, s)
    if a.oeis:
        partie_oeis(a.oeis, s)
    if a.zbmath:
        partie_zbmath(s)


if __name__ == "__main__":
    main()
