"""Contre-lecture banque v3 — k4 : référence « contraste de paire » (BC1-02) ; rejeu, appariement tel que servi (test et
test_final mêlés), cause des écarts avec la première contre-lecture, et une référence de contraste plus forte.

Ne lit ni identifiant (sauf pour nommer les paires dans la sortie), ni secret, ni clé : les paires viennent des textes.
Usage : python3 -I -B k4_contraste_paires_v1.py BANQUE_V3 RACINE_ESSAIM
"""
import difflib
import json
import math
import pathlib
import re
import sys

import numpy as np

PB, R = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
sys.path.insert(0, str(R))
from essaim_m3.banque import _regression_logistique, _traits_texte  # noqa: E402

PARTS = ("train", "test", "test_final")
b = json.loads(PB.read_text(encoding="utf-8"))
cd = {p: [t for t in b[p] if t["famille"] == "controle-delegation"] for p in PARTS}
out = []


def dire(*a):
    out.append(" ".join(str(x) for x in a))


def L_v3(t):
    return t.splitlines()


def L_cl1(t):
    return [l.strip() for l in t.split("\n") if l.strip()]


def ratio(la, lb):
    return difflib.SequenceMatcher(None, la, lb, autojunk=False).ratio()


def apparier(ts, L):
    n = len(ts)
    ls = [L(t["texte"]) for t in ts]
    r = [[ratio(ls[i], ls[j]) if i != j else -1.0 for j in range(n)] for i in range(n)]
    v = [max(range(n), key=lambda j: r[i][j]) for i in range(n)]
    pr = [(i, v[i]) for i in range(n) if v[v[i]] == i and i < v[i]]
    intra = [r[i][j] for i, j in pr]
    dans = {x for p in pr for x in p}
    inter = [r[i][k] for i in range(n) for k in range(n) if k != i and k != v[i]]
    asym = max(abs(r[i][j] - r[j][i]) for i in range(n) for j in range(n) if i != j)
    une_classe = all({ts[i]["verite"], ts[j]["verite"]} == {"sabotage", "honnete"} for i, j in pr)
    return [(ts[i], ts[j]) for i, j in pr], len(dans) == n, min(intra), max(inter), asym, une_classe


dire("1. Appariement par la seule ressemblance des textes")
paires = {}
for nom, L in (("lignes brutes (splitlines, référence v3)", L_v3), ("lignes nettoyées, non vides (première contre-lecture)", L_cl1)):
    for grp, ts in (("train", cd["train"]), ("test ∪ test_final mêlés (comme servis)", cd["test"] + cd["test_final"]),
                    ("test", cd["test"]), ("test_final", cd["test_final"])):
        pr, complet, mi, ma, asym, uc = apparier(ts, L)
        dire(f"   {nom} — {grp} : {len(ts)} traces, {len(pr)} paires mutuelles, toutes appariées {complet}, une trace de chaque classe {uc} ;"
             f" ressemblance min dans une paire {mi:.3f}, max hors paire {ma:.3f} ; asymétrie max du rapport {asym:.3f}")
        if L is L_v3:
            paires[grp] = pr
P = {"train": paires["train"], "test": paires["test"], "test_final": paires["test_final"]}
mel = {frozenset((a["id"], c["id"])) for a, c in paires["test ∪ test_final mêlés (comme servis)"]}
dire(f"   paires trouvées dans le mélange = paires trouvées part par part : {mel == {frozenset((a['id'], c['id'])) for p in ('test', 'test_final') for a, c in P[p]}}")


def mots_regex(s):
    return re.findall(r"[a-zà-ÿ0-9_]{2,}", s.lower())


TRAITS = {
    "caractères": lambda t: len(t["texte"]),
    "mots, découpe aux espaces (v3)": lambda t: len(t["texte"].split()),
    "mots, expression régulière (contre-lecture 1)": lambda t: len(mots_regex(t["texte"])),
    "lignes nettoyées (contre-lecture 1)": lambda t: len(L_cl1(t["texte"])),
}


def score_trait(f):
    def plus_petit_sab(pr):
        a, c = pr
        sa, ho = (a, c) if a["verite"] == "sabotage" else (c, a)
        return f(sa) < f(ho)
    sens = sum(plus_petit_sab(x) for x in P["train"]) >= len(P["train"]) / 2
    res, eg = {}, {}
    for p in PARTS:
        ok, n_eg = 0.0, 0
        for a, c in P[p]:
            va, vc = f(a), f(c)
            if va == vc:
                ok += 0.5
                n_eg += 1
                continue
            ch = (a if va < vc else c) if sens else (a if va > vc else c)
            ok += ch["verite"] == "sabotage"
        res[p] = round(ok / len(P[p]), 4)
        eg[p] = n_eg
    return ("le plus petit est saboté" if sens else "le plus grand est saboté"), res, eg


dire("\n2. Règles d'un seul trait, sens appris sur les 16 paires d'entraînement (part des paires bien tranchées ; égalité = 1/2)")
for nom, f in TRAITS.items():
    s_, r_, e_ = score_trait(f)
    dire(f"   {nom} : « {s_} » ; train {r_['train']} test {r_['test']} test_final {r_['test_final']} ; égalités {e_}")


def propres_lignes(a, c, L):
    la, lc = set(L(a["texte"])), set(L(c["texte"]))
    return la - lc, lc - la


s_, r_, e_ = score_trait(lambda t: 0)
for nom, L in (("lignes brutes", L_v3), ("lignes nettoyées", L_cl1)):
    def sab_moins(pr, L=L):
        a, c = pr
        pa, pc = propres_lignes(a, c, L)
        return len(pa) - len(pc)
    tr = []
    for a, c in P["train"]:
        d = sab_moins((a, c))
        sa_first = a["verite"] == "sabotage"
        tr.append((d < 0) == sa_first if d != 0 else None)
    res = {}
    sens_moins = sum(1 for x in tr if x) >= sum(1 for x in tr if x is False)
    for p in PARTS:
        ok = 0.0
        for a, c in P[p]:
            d = sab_moins((a, c))
            if d == 0:
                ok += 0.5
                continue
            ch = (a if d < 0 else c) if sens_moins else (a if d > 0 else c)
            ok += ch["verite"] == "sabotage"
        res[p] = round(ok / len(P[p]), 4)
    dire(f"   nombre de lignes propres ({nom}) : « {'le moins' if sens_moins else 'le plus'} de lignes propres est saboté » ; train {res['train']} test {res['test']} test_final {res['test_final']}")

# modèle de mots des lignes propres (log-rapport lissé appris sur train), deux définitions des lignes
for nom, L in (("lignes nettoyées (contre-lecture 1)", L_cl1), ("lignes brutes", L_v3)):
    cs, ch = {}, {}
    for a, c in P["train"]:
        sa, ho = (a, c) if a["verite"] == "sabotage" else (c, a)
        ps, ph = propres_lignes(sa, ho, L)
        for w in (w for x in ps for w in mots_regex(x)):
            cs[w] = cs.get(w, 0) + 1
        for w in (w for x in ph for w in mots_regex(x)):
            ch[w] = ch.get(w, 0) + 1
    voc = set(cs) | set(ch)
    ns, nh = sum(cs.values()), sum(ch.values())
    lr = {w: math.log((cs.get(w, 0) + 1) / (ns + len(voc))) - math.log((ch.get(w, 0) + 1) / (nh + len(voc))) for w in voc}
    res = {}
    for p in PARTS:
        ok = 0.0
        for a, c in P[p]:
            pa, pc = propres_lignes(a, c, L)
            wa = [w for x in pa for w in mots_regex(x)]
            wc = [w for x in pc for w in mots_regex(x)]
            sa_ = sum(lr.get(w, 0.0) for w in wa) / max(1, len(wa))
            sc_ = sum(lr.get(w, 0.0) for w in wc) / max(1, len(wc))
            ok += 0.5 if sa_ == sc_ else float((a if sa_ > sc_ else c)["verite"] == "sabotage")
        res[p] = round(ok / len(P[p]), 4)
    dire(f"   mots des lignes propres, log-rapport appris sur train ({nom}) : train {res['train']} (en échantillon) test {res['test']} test_final {res['test_final']}")

# 3. Référence de surface « en contraste » : régression logistique du noyau sur la différence des traits de surface
X, y = [], []
for a, c in P["train"]:
    d = _traits_texte(a["texte"]) - _traits_texte(c["texte"])
    lab = 1.0 if a["verite"] == "sabotage" else 0.0
    X += [d, -d]
    y += [lab, 1.0 - lab]
w, b0, mu, sd = _regression_logistique(np.stack(X), np.array(y))
res = {}
for p in PARTS:
    ok = 0.0
    for a, c in P[p]:
        d = _traits_texte(a["texte"]) - _traits_texte(c["texte"])
        za = float(((d - mu) / sd) @ w + b0)
        zc = float(((-d - mu) / sd) @ w + b0)
        ok += 0.5 if za == zc else float((a if za > zc else c)["verite"] == "sabotage")
    res[p] = round(ok / len(P[p]), 4)
dire(f"\n3. Référence de surface en contraste (traits du noyau, différence des deux membres, régression logistique du noyau apprise sur les 16 paires) : train {res['train']} (en échantillon) test {res['test']} test_final {res['test_final']}")
print("\n".join(out))
