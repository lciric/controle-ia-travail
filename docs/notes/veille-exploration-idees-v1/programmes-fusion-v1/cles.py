#!/usr/bin/env python3
"""Cles de rapprochement et regroupement des entrees brutes. Module importe par les autres scripts."""
import re
import unicodedata
from collections import defaultdict

RE_ARXIV = re.compile(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d])")


def norm_titre(t):
    t = re.sub(r"\[[^\]]*\]", " ", t)           # [ICLR 2027, soumission ; arXiv ...]
    t = re.sub(r"\((?:[^()]*arXiv[^()]*|aussi billet[^()]*|billet[^()]*|dépôt[^()]*|banc [^()]*|titre du PDF[^()]*|POPPER|REUSE|AIDE\^2|LiveIdeaBench|SSRN[^()]*|et Kosmos[^()]*|note|v1|réponse critique[^()]*|liste entretenue[^()]*|billet miroir)\)", " ", t)
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower().replace("$", "")
    t = re.sub(r"[^a-z0-9]+", " ", t).strip()
    return t


def norm_url(u):
    u = u.strip()
    m = re.search(r"(?:lesswrong|greaterwrong)\.com/(?:s/\w+/p|posts)/(\w{17})", u)
    if m:
        return "lw:" + m.group(1)
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", u)
    if m:
        return "arxiv:" + m.group(1)
    m = re.search(r"(?:nber\.org/papers/|10\.3386/)(w\d+)", u)
    if m:
        return "nber:" + m.group(1)
    m = re.search(r"openreview\.net/forum\?id=([\w-]+)", u)
    if m:
        return "openreview:" + m.group(1)
    u = re.sub(r"^https?://(www\.)?", "", u.lower()).rstrip("/")
    return "url:" + u


def cles(e):
    """Cles fortes d'une entree : identifiant arXiv, adresse normalisee, titre normalise."""
    k = set()
    u = e["adresse"]
    nu = norm_url(u) if u.startswith("http") else None
    if nu:
        k.add(nu)
    if not (nu and nu.startswith("arxiv:")):
        # l'adresse n'est pas arXiv : un identifiant arXiv dans le titre designe le meme travail
        for a in RE_ARXIV.findall(e["titre"]):
            k.add("arxiv:" + a)
    nt = norm_titre(e["titre"])
    if len(nt) >= 12:
        k.add("titre:" + nt)
    return k


class Union:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def regroupe(entrees, cles_par_entree):
    u = Union(len(entrees))
    index = defaultdict(list)
    for i, ks in enumerate(cles_par_entree):
        for k in ks:
            index[k].append(i)
    for k, ids in index.items():
        for j in ids[1:]:
            u.union(ids[0], j)
    groupes = defaultdict(list)
    for i in range(len(entrees)):
        groupes[u.find(i)].append(i)
    return list(groupes.values()), index
