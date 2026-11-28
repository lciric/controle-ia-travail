# -*- coding: utf-8 -*-
"""
INTERBRAS v1 - c2a et c2b ont-ils servi le MEME prompt neutre pour le MEME item ?
Lecture seule, aucun reseau. Lancer avec : python3 -I verif_interbras_v1.py

Si les deux bras neutres partagent texte et gabarit (graines differentes), alors, item par
item : (1) les notes neutres moyennes du juge (mean_neu, tables scellees de c2a_results et
c2b_results) doivent se ressembler bien plus qu'entre items permutes ; (2) les longueurs
moyennes des reponses neutres aussi ; (3) les debuts de reponse neutres doivent avoir la
meme distribution. Un gabarit different dans un bras (instruction absente, systeme
different) casserait au moins un des trois. Ce n'est pas une preuve d'identite : c'est un
test capable d'infirmer. Temoin d'artefact : une permutation des items doit faire tomber (1).
"""
import collections, hashlib, json, os, random, re, statistics

ICI = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p1-items/verif-contradicteur"
D = "/home/user/controle-ia-travail/donnees/P1-loi-attraction-v1/"
F = {"c2a_gen": ("c2a_generations.json", "a7c85816e2ce60fd86727fe367cb1d63335940a13b50ba3e33c9e16b3ba6189a"),
     "c2b_gen": ("c2b_generations.json", "ec2f7ca5cc80c249fd861a77fb360a8e1c4d59f1788ada2a7864b88ec72586c2"),
     "c2a_res": ("c2a_results.json", "6ad1a71822395e11417223c8d872c5973129dd1c8a4b023be74810f4746b5d83"),
     "c2b_res": ("c2b_results.json", "ae097f3d7ac993fe41fa3e1bb11d76f88727ffdf128bc661566949b7f5bc0aa2")}
OUT = []


def dire(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.append(s)


def sha_f(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def pearson(x, y):
    mx, my = statistics.fmean(x), statistics.fmean(y)
    sx = sum((a - mx) ** 2 for a in x) ** 0.5
    sy = sum((b - my) ** 2 for b in y) ** 0.5
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


def main():
    X = {}
    for k, (f, att) in F.items():
        h = sha_f(D + f)
        dire("  %-8s %s %s" % (k, h, "CONFORME" if h == att else "*** DIVERGE ***"))
        if h != att:
            raise SystemExit("ARRET NOMME - empreinte divergente")
        X[k] = json.load(open(D + f, encoding="utf-8"))
    ta, tb = X["c2a_res"]["table"], X["c2b_res"]["table"]
    dire("  cles d'une ligne de table c2a : %s" % sorted(ta["0"].keys()))
    dire("  cles d'une ligne de table c2b : %s" % sorted(tb["0"].keys()))
    a = [ta[str(i)]["mean_neu"] for i in range(30)]
    b = [tb[str(i)]["mean_neu"] for i in range(30)]
    r = pearson(a, b)
    mad = statistics.fmean(abs(x - y) for x, y in zip(a, b))
    rng = random.Random(20261020)
    perm_r, perm_mad = [], []
    for _ in range(10000):
        p = list(range(30))
        rng.shuffle(p)
        bb = [b[j] for j in p]
        perm_r.append(pearson(a, bb))
        perm_mad.append(statistics.fmean(abs(x - y) for x, y in zip(a, bb)))
    p_r = (1 + sum(1 for v in perm_r if v >= r)) / 10001
    p_mad = (1 + sum(1 for v in perm_mad if v <= mad)) / 10001
    dire("\n(1) NOTES NEUTRES MOYENNES PAR ITEM, c2a contre c2b (juge scelle, 10 notes par item et par bras)")
    dire("  correlation de Pearson %.3f ; ecart absolu moyen %.3f" % (r, mad))
    dire("  sous permutation des items (10 000) : correlation max %.3f, ecart min %.3f ; p(r) %.4f ; p(ecart) %.4f" % (
        max(perm_r), min(perm_mad), p_r, p_mad))
    gros = [(i, a[i], b[i]) for i in range(30) if abs(a[i] - b[i]) >= 1.0]
    dire("  items a ecart >= 1 point : %s" % gros)
    # temoin d'artefact : decalage d'un cran
    bd = b[1:] + b[:1]
    dire("  temoin d'artefact (c2b decale d'un item) : correlation %.3f ; ecart %.3f" % (
        pearson(a, bd), statistics.fmean(abs(x - y) for x, y in zip(a, bd))))

    dire("\n(2) LONGUEURS MOYENNES DES REPONSES NEUTRES PAR ITEM")
    def lg(d):
        L = collections.defaultdict(list)
        for row in d["rows"]:
            if row["cond"] == "neutral":
                L[int(row["item"])].append(len(row["resp"]))
        return [statistics.fmean(L[i]) for i in range(30)]
    la, lb = lg(X["c2a_gen"]), lg(X["c2b_gen"])
    dire("  correlation %.3f ; moyennes globales %.0f / %.0f caracteres" % (
        pearson(la, lb), statistics.fmean(la), statistics.fmean(lb)))

    dire("\n(3) DEBUTS DE REPONSE NEUTRES (30 premiers caracteres)")
    def debuts(d):
        return collections.Counter(row["resp"][:30] for row in d["rows"] if row["cond"] == "neutral")
    da, db = debuts(X["c2a_gen"]), debuts(X["c2b_gen"])
    for k in sorted(set(list(dict(da.most_common(6))) + list(dict(db.most_common(6)))),
                    key=lambda k: -(da[k] + db[k])):
        dire("  %-32r c2a %3d   c2b %3d" % (k, da[k], db[k]))
    dire("\n(4) BRAS PRESSES - debuts")
    for nom, cond in (("c2a_gen", "hate"), ("c2b_gen", "praise")):
        c = collections.Counter(row["resp"][:30] for row in X[nom]["rows"] if row["cond"] == cond)
        dire("  %s %s : %s" % (nom, cond, c.most_common(4)))
    dire("\nFIN")


if __name__ == "__main__":
    try:
        main()
    finally:
        j = os.path.join(ICI, "journal-verif-interbras-v1.txt")
        open(j, "w", encoding="utf-8", newline="\n").write("\n".join(OUT) + "\n")
        h = sha_f(j)
        open(j + ".sha256", "w", encoding="utf-8", newline="\n").write("%s  %s\n" % (h, os.path.basename(j)))
        print("journal", j, h)
