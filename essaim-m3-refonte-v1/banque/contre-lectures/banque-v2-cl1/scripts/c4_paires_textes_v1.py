"""Contre-lecture banque v2 — c4 : appariement des traces et contrôles de texte.

1. Appariement : pour chaque trace de délégation servie, sa plus proche voisine (rapport de difflib sur les lignes) parmi
   les traces servies ensemble (entraînement d'un côté, test et test final mêlés de l'autre, comme dans contexte.json) ;
   comparaison au groupe du fichier secret (lu pour noter seulement).
2. Contraste de paire : règles apprises sur les paires d'entraînement (sens majoritaire), appliquées aux paires de test et
   de test final : longueur, nombre de lignes, nombre de mots ; et un modèle de mots des lignes propres à chaque membre
   (log-rapport lissé, appris sur l'entraînement). Chaque paire a une trace de chaque classe : l'exactitude équilibrée
   est la part des paires bien tranchées.
3. Textes : identifiants v1 ou bruts dans les textes, mots d'étiquette, doublons exacts.
Usage : python3 -I c4_paires_textes_v1.py BANQUE_V2 SECRET_V2
"""
import difflib
import json
import math
import pathlib
import re
import sys

PARTS = ("train", "test", "test_final")


def lignes(t):
    return [l.strip() for l in t.split("\n") if l.strip()]


def mots(s):
    return re.findall(r"[a-zà-ÿ0-9_]{2,}", s.lower())


def main(pb, ps):
    b = json.loads(pathlib.Path(pb).read_text(encoding="utf-8"))
    s = json.loads(pathlib.Path(ps).read_text(encoding="utf-8"))
    cd = {p: [t for t in b[p] if t["famille"] == "controle-delegation"] for p in PARTS}
    groupe = {i: d["groupe"] for i, d in s.items()}

    print("1. Appariement par la plus proche voisine")
    servis = {"train": cd["train"], "tests mêlés": cd["test"] + cd["test_final"]}
    trouvees = {}
    for nom, l in servis.items():
        L = [lignes(t["texte"]) for t in l]
        bons, mutuels = 0, 0
        voisin = {}
        for a in range(len(l)):
            best = max(((difflib.SequenceMatcher(None, L[a], L[c], autojunk=False).ratio(), c) for c in range(len(l)) if c != a))
            voisin[a] = best
        for a in range(len(l)):
            c = voisin[a][1]
            bons += groupe[l[a]["id"]] == groupe[l[c]["id"]]
            mutuels += voisin[c][1] == a
            if voisin[c][1] == a and a < c:
                trouvees.setdefault(nom, []).append((l[a], l[c]))
        ratios_paire = [voisin[a][0] for a in range(len(l))]
        print(f"   {nom}: {len(l)} traces ; voisine = l'autre membre de la paire pour {bons}/{len(l)} ; voisines mutuelles {mutuels}/{len(l)} ;"
              f" rapport de similitude min {min(ratios_paire):.3f}")
    # rapport de similitude hors paire, pour situer
    l = servis["tests mêlés"]
    L = [lignes(t["texte"]) for t in l]
    hors = max(difflib.SequenceMatcher(None, L[a], L[c], autojunk=False).ratio() for a in range(len(l)) for c in range(len(l))
               if a != c and groupe[l[a]["id"]] != groupe[l[c]["id"]])
    print(f"   tests mêlés : rapport de similitude maximal entre traces de paires différentes {hors:.3f}")

    print("\n2. Contraste de paire (paires trouvées à l'étape 1)")
    paires = {}
    for p in PARTS:
        g = {}
        for t in cd[p]:
            g.setdefault(groupe[t["id"]], []).append(t)
        paires[p] = [tuple(v) for v in g.values()]
        assert all(len(v) == 2 and {x["verite"] for x in v} == {"sabotage", "honnete"} for v in paires[p])
    # les paires de l'étape 1 sont-elles les vraies paires ?
    vraies_tests = {frozenset((a["id"], c["id"])) for p in ("test", "test_final") for a, c in paires[p]}
    print(f"   paires trouvées sans le secret = vraies paires (tests mêlés) : {set(frozenset((a['id'], c['id'])) for a, c in trouvees['tests mêlés']) == vraies_tests}")
    traits = {"longueur": lambda t: len(t["texte"]), "lignes": lambda t: len(lignes(t["texte"])), "mots": lambda t: len(mots(t["texte"]))}
    for nom, f in traits.items():
        # sens appris sur l'entraînement : la trace sabotée a-t-elle la plus petite valeur ?
        def plus_petit_sabote(pr):
            a, c = pr
            sa, ho = (a, c) if a["verite"] == "sabotage" else (c, a)
            return f(sa) < f(ho), f(sa) == f(ho)
        tr = [plus_petit_sabote(x) for x in paires["train"]]
        sens = sum(x[0] for x in tr) >= len(tr) / 2  # True : « la plus petite est sabotée »
        res = {}
        for p in PARTS:
            ok = 0
            for a, c in paires[p]:
                va, vc = f(a), f(c)
                if va == vc:
                    ok += 0.5
                    continue
                choisi = (a if va < vc else c) if sens else (a if va > vc else c)
                ok += choisi["verite"] == "sabotage"
            res[p] = round(ok / len(paires[p]), 4)
        print(f"   {nom:9s} : règle apprise « la {'plus petite' if sens else 'plus grande'} est sabotée » ;"
              f" exactitude équilibrée train {res['train']} test {res['test']} test_final {res['test_final']} (paires : {len(paires['train'])}/{len(paires['test'])}/{len(paires['test_final'])})")
    # modèle de mots des lignes propres
    def propres(a, c):
        la, lc = set(lignes(a["texte"])), set(lignes(c["texte"]))
        return [w for x in la - lc for w in mots(x)], [w for x in lc - la for w in mots(x)]
    cs, ch = {}, {}
    for a, c in paires["train"]:
        sa, ho = (a, c) if a["verite"] == "sabotage" else (c, a)
        ws, wh = propres(sa, ho)
        for w in ws:
            cs[w] = cs.get(w, 0) + 1
        for w in wh:
            ch[w] = ch.get(w, 0) + 1
    vocab = set(cs) | set(ch)
    ns, nh = sum(cs.values()), sum(ch.values())
    lr = {w: math.log((cs.get(w, 0) + 1) / (ns + len(vocab))) - math.log((ch.get(w, 0) + 1) / (nh + len(vocab))) for w in vocab}
    res = {}
    for p in PARTS:
        ok = 0
        for a, c in paires[p]:
            wa, wc = propres(a, c)
            sa_ = sum(lr.get(w, 0.0) for w in wa) / max(1, len(wa))
            sc_ = sum(lr.get(w, 0.0) for w in wc) / max(1, len(wc))
            if sa_ == sc_:
                ok += 0.5
            else:
                ok += (a if sa_ > sc_ else c)["verite"] == "sabotage"
        res[p] = round(ok / len(paires[p]), 4)
    print(f"   mots des lignes propres (log-rapport appris sur train) : exactitude équilibrée train {res['train']} (en échantillon) test {res['test']} test_final {res['test_final']}")

    print("\n3. Textes")
    motifs = {"identifiant brut L1/L2-NN-H/S": r"\bL[12]-\d{2}-[HS]\b", "identifiant v1 cd-lot / ce-hf": r"\b(cd-lot[12]|ce-hf-\d{4})",
              "mot d'étiquette": r"\b(sabotage|sabot[ée]e?s?|honn[eê]te|usage[- ]r[ée]el)\b", "identifiant v2 t-NNNN": r"\bt-\d{4}\b"}
    for nom, m in motifs.items():
        n = {p: sum(1 for t in b[p] if re.search(m, t["texte"], re.I)) for p in PARTS}
        print(f"   {nom:32s} : textes touchés {n}")
    cle = {}
    for p in PARTS:
        for t in b[p]:
            cle.setdefault(" ".join(t["texte"].split()).lower(), []).append((p, t["id"], t["verite"]))
    doublons = [v for v in cle.values() if len(v) > 1]
    print(f"   doublons exacts (espaces et casse normalisés) : {len(doublons)} {doublons[:3]}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
