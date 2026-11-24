"""Suivisme entre tours : qui concède quoi à qui, dans la section (a) des réponses du tour 3.

Unité : une ligne de décision (« acceptée », « rejetée », « partiellement »…) d'un modèle répondant,
rattachée aux lettres des critiques citées sur la ligne, ou à défaut dans le titre ou la ligne en gras
qui la précède (six lignes au plus). Classement : acceptée, partielle, rejetée.
Mesures : taux d'acceptation par répondant, par critique ; déférence au même fournisseur (permutation
des étiquettes de critique à l'intérieur de chaque répondant et course) ; acceptation selon que la ligne
porte la trace d'un calcul ou d'une vérification (« = », « VÉRIFIÉ », « calcul »), approximation de
« va vers ce qui est vérifié ».
Sortie : sorties/suivisme-v1.json.
"""
import json
import re
import sys
from collections import Counter, defaultdict

import numpy as np

from audit_commun_v2 import SORTIES, ESPECE_FOURNISSEUR, graine
from cellules_v1 import charger

DEC = re.compile(r"\b(accept[ée]e?s?|rejet[ée]e?s?|rejette|rejetons|partiellement|maintenue?s?|maintiens|concèd|conc[ée]d[ée]e?)\b", re.I)
LET = r"(?<![A-Za-zÀ-ÿ0-9'’])([A-I])(?=[-.\s]?(?:[abc](?:[.\s]?\d+)?\b|pr[ée]ambule|«|\(|,|;|\)|\s+et\b|\s*—|\s*:|\s*$))"
CRIT_DE = re.compile(r"[Cc]ritiques?\s+(?:de|par|venant de)\s+(?:la proposition\s+)?([A-I])\b")
TRACE = re.compile(r"(=|≈|V[ÉE]RIFI[ÉE]|calcul|recalcul|d[ée]rivation|contre-exemple|\d\s?[×*/]\s?\d)", re.I)


def classer(l):
    a = re.search(r"accept|concèd|conc[ée]d", l, re.I)
    r = re.search(r"rejet|\bmaintenue?s?\b|\bje maintiens\b|\bmaintiens\b", l, re.I)
    p = re.search(r"partiel|nuance|r[ée]serve|en partie", l, re.I)
    if (a and (r or p)) or (r and p):
        return "partielle"
    if a:
        return "acceptée"
    if r:
        return "rejetée"
    return None


def section_a(texte):
    lignes = texte.split("\n")
    debut, fin, niv = None, len(lignes), None
    for i, l in enumerate(lignes):
        m = re.match(r"^(#{1,4})\s+(.*)$", l)
        if not m:
            continue
        t = m.group(2)
        if debut is None and re.search(r"^\(?a\)|^\d+\.\s*\(?a\)|critique|d[ée]cision", t, re.I) and not re.search(r"^\(?[bc]\)", t):
            debut, niv = i, len(m.group(1))
        elif debut is not None and len(m.group(1)) <= niv and re.search(r"^\(?[bc]\)|^\d+\.\s*\(?[bc]\)|exp[ée]rience|livrable", t, re.I):
            fin = i
            break
    return lignes[debut:fin] if debut is not None else []


def main():
    C = [c for c in charger() if c["tour"] == 3 and c["role"] == "reponse" and not c["rejeu_de"]]
    lignes_dec = []
    for c in C:
        L = section_a(c["texte"])
        lettres = {k: v for k, v in c["lettres_course"].items() if k != c["lettre"] and v}
        contexte = []
        for i, l in enumerate(L):
            if re.match(r"^#{1,5}\s", l) or re.match(r"^\s*(\d+[.)]\s*)?\*\*[^*]{3,}\*\*", l):
                contexte.append(l)
            dec = classer(l) if DEC.search(l) else None
            if not dec:
                continue
            crit = set(re.findall(LET, l)) | set(CRIT_DE.findall(l))
            if not crit:
                for prev in reversed(contexte[-1:] + L[max(0, i - 6):i]):
                    crit = set(re.findall(LET, prev)) | set(CRIT_DE.findall(prev))
                    if crit:
                        break
            crit = {x for x in crit if x in lettres}
            for x in sorted(crit):
                lignes_dec.append({"racine": c["racine"], "repondant": c["espece"], "critique": lettres[x],
                                   "decision": dec, "trace_calcul": bool(TRACE.search(l)), "chemin": c["chemin"],
                                   "ligne": l.strip()[:240]})
    acc = lambda L: round(sum(x["decision"] == "acceptée" for x in L) / len(L), 4) if L else None
    nonrej = lambda L: round(sum(x["decision"] != "rejetée" for x in L) / len(L), 4) if L else None
    par_rep = defaultdict(list)
    par_cri = defaultdict(list)
    for x in lignes_dec:
        par_rep[x["repondant"]].append(x)
        par_cri[x["critique"]].append(x)
    meme = lambda x: ESPECE_FOURNISSEUR.get(x["repondant"]) == ESPECE_FOURNISSEUR.get(x["critique"])

    def ecart(L):
        """moyenne sur les (course, répondant) qui ont les deux sortes de critiques : non-rejet même − autre"""
        g = defaultdict(lambda: ([], []))
        for x in L:
            g[(x["racine"], x["repondant"])][0 if meme(x) else 1].append(x["decision"] != "rejetée")
        d = [np.mean(a) - np.mean(b) for a, b in g.values() if a and b]
        return (float(np.mean(d)) if d else None), len(d)

    obs, n = ecart(lignes_dec)
    rng, meta = graine("suivisme-deference")
    g = defaultdict(list)
    for x in lignes_dec:
        g[(x["racine"], x["repondant"])].append(x)
    plus = 0
    for _ in range(10000):
        perm = []
        for k, L in g.items():
            cr = [x["critique"] for x in L]
            pc = rng.permutation(cr)
            perm += [dict(x, critique=pc[i]) for i, x in enumerate(L)]
        v, _ = ecart(perm)
        if v is not None and obs is not None and v >= obs:
            plus += 1
    avec = [x for x in lignes_dec if x["trace_calcul"]]
    sans = [x for x in lignes_dec if not x["trace_calcul"]]
    out = {
        "n_lignes": len(lignes_dec), "repartition": dict(Counter(x["decision"] for x in lignes_dec)),
        "par_repondant": {e: {"n": len(L), "acceptee": acc(L), "non_rejetee": nonrej(L)} for e, L in sorted(par_rep.items())},
        "par_critique": {e: {"n": len(L), "acceptee": acc(L), "non_rejetee": nonrej(L)} for e, L in sorted(par_cri.items())},
        "deference_meme_fournisseur": {"ecart_non_rejet": round(obs, 4) if obs is not None else None, "groupes": n,
                                       "p_unilaterale": round((plus + 1) / 10001, 4), "graine": meta},
        "selon_trace_de_calcul": {"avec": {"n": len(avec), "non_rejetee": nonrej(avec)},
                                  "sans": {"n": len(sans), "non_rejetee": nonrej(sans)}},
        "lignes": lignes_dec,
    }
    (SORTIES / "suivisme-v1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print({k: v for k, v in out.items() if k != "lignes"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
