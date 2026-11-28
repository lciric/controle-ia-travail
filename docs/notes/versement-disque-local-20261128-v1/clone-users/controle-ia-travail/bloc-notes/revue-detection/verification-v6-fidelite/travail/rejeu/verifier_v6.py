"""Vérifie la v6 contre la v5 et les deux rapports du tour 4 (correcteur v6). Lecture seule.

1. Empreintes : v5 (attendue), v6 (calculée, égale à son compagnon s'il existe).
2. Rien d'autre que les remplacements déclarés : la v5, blancs ramenés à une espace, à laquelle on applique la liste
   d'entrées de appliquer_corrections_v6.py, égale la v6, blancs ramenés à une espace.
3. Mots exacts : pour chaque correction extraite des rapports, le texte neuf (ou l'écart déclaré) est dans la v6 ; l'ancien
   n'y est plus (sauf s'il est contenu dans le neuf).
4. Mentions d'attente présentes ; « (b') » n'apparaît que comme proposition du vérificateur.
5. Structure Markdown : titres et lignes de table en même nombre ; une puce de plus (l'en-tête v6).
Usage : python3 -I -B verifier_v6.py V6.md   (code 0 si tout est conforme)
"""
import hashlib
import os
import re
import sys
from pathlib import Path

ICI = Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(ICI))
import appliquer_corrections_v6 as ap  # noqa: E402

fautes = []


def n(s):
    return re.sub(r"\s+", " ", s).strip()


def ok(cond, msg):
    print(("OK    | " if cond else "FAUTE | ") + msg)
    if not cond:
        fautes.append(msg)


def main():
    v6p = Path(sys.argv[1])
    b5 = ap.V5.read_bytes()
    ok(hashlib.sha256(b5).hexdigest() == ap.V5_SHA, f"v5 à l'empreinte attendue {ap.V5_SHA[:8]}…")
    b6 = v6p.read_bytes()
    h6 = hashlib.sha256(b6).hexdigest()
    comp = v6p.with_name(v6p.name + ".sha256")
    if comp.exists():
        ok(comp.read_text().split()[:2] == [h6, v6p.name], f"v6 égale à son compagnon ({h6[:8]}…)")
    print(f"INFO  | v6 {v6p.name} : {h6}")
    v5, v6 = b5.decode("utf-8"), b6.decode("utf-8")
    N5, N6 = n(v5), n(v6)

    # 2. reconstruction indépendante sur texte normalisé
    cor = ap.corrections()
    E = ap.entrees(cor, ap.comptes())
    t = N5
    for etiq, a, b in E:
        na, nb = n(a), n(b)
        c = t.count(na)
        ok(c == 1, f"[2] ancien texte trouvé une fois (normalisé) : {etiq} ({c})")
        t = t.replace(na, nb, 1)
    ok(t == N6, f"[2] v5 + {len(E)} remplacements déclarés = v6 (blancs normalisés) : rien d'autre n'est changé")

    # 3. mots exacts des rapports
    ecarts = {("VV5-fidelite-02", 0), ("VV5-fidelite-07", 0), ("VV5-fidelite-07", 1), ("VV5-sens-08", 7),
              ("VV5-sens-01", 1), ("VV5-sens-01", 2), ("VV5-sens-03", 1), ("VV5-sens-07", 0)}
    tot = exacts = 0
    for c, paires in cor.items():
        for i, (a, b) in enumerate(paires):
            tot += 1
            na, nb = n(a), n(b)
            if (c, i) not in ecarts:
                r = N6.count(nb) == 1
                exacts += r
                ok(r, f"[3] {c} ({i + 1}) : texte neuf présent une fois, en mots exacts")
            ok(na not in N6 or na in nb, f"[3] {c} ({i + 1}) : ancien texte absent de la v6")
    # écarts déclarés : ce qui doit être présent
    f02 = cor["VV5-fidelite-02"][0][1]
    for seg in ["incitation chez les positifs **et** les négatifs (sinon la sonde apprend le régime d'incitation, "
                "[KU p. 5]), étiquette par le coût écrit ensuite",
                "lecture **avant le champ** `COST` ; jamais sur des paires écrites qui ne diffèrent qu'au champ (avant le "
                "champ, à texte égal, les activations sont égales : modèle causal) ;"]:
        ok(n(seg) in n(f02) and n(seg) in N6, f"[3] VV5-fidelite-02 (fusion avec VV5-sens-06) : segment présent : {seg[:50]}…")
    b = cor["VV5-fidelite-07"][0][1]
    ok(n(b[:-1]) in N6, "[3] VV5-fidelite-07 (1) : mots exacts présents, complétés « ; v6 : … »")
    ok(n(cor["VV5-fidelite-07"][1][1]) not in N6,
       "[3] VV5-fidelite-07 (2) : texte du rapport non repris (compagnon de MA présent sur disque, R11)")
    ok("pour MA, présent (`[X]pdf-anthropic/2503.10965/2503.10965v2.pdf.sha256`" in N6,
       "[3] VV5-fidelite-07 (2) : texte corrigé présent")
    a, b = cor["VV5-sens-08"][7]
    fin = " **Ce qu'a fait Anthropic.**"
    ok(n(b[:-len(fin)]) in N6, "[3] VV5-sens-08 (8) : mots exacts présents, saut de paragraphe gardé")
    ok("**non vérifié**. La lentille des logits" in v6 and "(R-295 (1)).\n\n**Ce qu'a fait Anthropic.**" in v6,
       "[3] VV5-sens-08 (8) : « Ce qu'a fait Anthropic » reste en tête de paragraphe")
    for c, i in [("VV5-sens-01", 1), ("VV5-sens-01", 2), ("VV5-sens-03", 1), ("VV5-sens-07", 0)]:
        b = cor[c][i][1]
        morceaux = [x for x in re.split(r"\*\*\[Décision de Lazar en attente[^\]]*\]\*\*", b)]
        if c == "VV5-sens-01" and i == 2:
            morceaux = b.split("(b'), confiance ≈ 55 %.**", 1)
            morceaux[0] += "(b'), confiance ≈ 55 %.**"
        if c == "VV5-sens-03":
            morceaux = b.split("Options : (A) défaut", 1)
            morceaux[1] = "Options : (A) défaut" + morceaux[1]
        ok(all(n(m) in N6 for m in morceaux if m.strip()),
           f"[3] {c} ({i + 1}) : mots exacts présents, mention d'attente insérée")
    print(f"INFO  | [3] {tot} corrections extraites ; {exacts} en mots exacts sans écart ; {len(ecarts)} avec écart déclaré")

    # 4. mentions d'attente, (b')
    for m, mini in [(ap.ATT_P015_T06, 3), (ap.ATT_P017, 3), (ap.ATT_N030, 1), (ap.ATT_REV, 3),
                    ("**[Décision de Lazar en attente : P-015]**", 4)]:
        k = N6.count(n(m))
        ok(k >= mini, f"[4] mention {m} : {k} fois (au moins {mini})")
    for mo in re.finditer(r"\(b'\)", N6):
        ctx = N6[max(0, mo.start() - 120):mo.end() + 40]
        ok(("vérificateur" in ctx) or ("(b') = (b) plus" in ctx),
           f"[4] « (b') » donné comme proposition du vérificateur : …{ctx[-110:]}…")
    ok("empreintes vérifiées ce jour" not in v6, "[4] section 6 : plus de « empreintes vérifiées ce jour »")

    # 5. structure
    def st(x):
        L = x.split("\n")
        return (sum(l.startswith("#") for l in L), sum(l.startswith("|") for l in L),
                sum(bool(re.match(r"^\s*([-*+]|\d+\.)\s", l)) for l in L))
    s5, s6 = st(v5), st(v6)
    ok(s5[0] == s6[0] and s5[1] == s6[1] and s6[2] == s5[2] + 1,
       f"[5] titres {s5[0]}→{s6[0]}, lignes de table {s5[1]}→{s6[1]}, puces {s5[2]}→{s6[2]} (une puce de plus : en-tête v6)")
    print(f"# BILAN : {len(fautes)} faute(s)")
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
