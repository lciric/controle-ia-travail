# -*- coding: utf-8 -*-
"""
TEMOIN PAR LES SORTIES (lecture seule, aucun reseau). Complement de la lentille empreintes.
Si une campagne posterieure a envoye au meme modele le prompt NEUTRE reconstruit, avec les
MEMES graines que c2a / c2b, des sorties identiques au caractere ne s'expliquent que par une
meme suite de jetons en entree. Le bloc C (p1-auto, 2026-08-24) le permet : son tour 0 porte
le prompt neutre reconstruit (empreinte verifiee ailleurs, 600/600) et ses graines sont LUES
sur les lignes de c2a (bras critique) et de c2b (bras elogieux).
Controle : la grille C2F (I2) reprend les phrases historiques mais PAS les graines de c2a/c2b.
Usage : python3 -I temoin_sorties_v1.py FICHIER_JOURNAL
"""
import ast, hashlib, json, re, statistics, sys

DON = "/home/user/controle-ia-travail/donnees/P1-loi-attraction-v1/"
BLOCC = "/home/user/p1-auto/actes/ccA/RELEVE_ccA_blocC_2026-08-24.json"
C2F = ("/home/user/archive-2026-09/depots/sycophancy-construct-validity/analysis/"
       "jugements_lot3/sources/c2f_pourjugement_2026-08-10T1810Z.json")
SANS_INSTR = ("/home/user/p1-auto/actes/ccA/trace_blocB_avorte/"
              "TRACE_blocB_sans_instruction_40cellules.json")
J = []


def log(*a):
    s = " ".join(str(x) for x in a)
    J.append(s)
    print(s)


def sha_f(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def premiere_divergence(a, b):
    return next((j for j, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))


gA = json.load(open(DON + "c2a_generations.json", encoding="utf-8"))
gB = json.load(open(DON + "c2b_generations.json", encoding="utf-8"))
log("sources : c2a %s ; c2b %s ; bloc C %s ; c2f %s"
    % (sha_f(DON + "c2a_generations.json")[:16], sha_f(DON + "c2b_generations.json")[:16],
       sha_f(BLOCC)[:16], sha_f(C2F)[:16]))
log("materiel : c2a %s ; c2b %s" % (gA["meta"]["backend"], gB["meta"]["backend"]))


def table(g, cond):
    return {(int(r["item"]), int(r["k"])): (int(r["seed"]), r["resp"])
            for r in g["rows"] if r["cond"] == cond}


neuA, neuB = table(gA, "neutral"), table(gB, "neutral")
C = json.load(open(BLOCC, encoding="utf-8"))
log("bloc C materiel : %s" % C["meta"].get("pile"))
res = {}
for nom, ref in (("critique", neuA), ("elogieux", neuB)):
    n = graine = ident = deb50 = 0
    div = []
    for r in C["rows"]:
        if r["bras"] != nom:
            continue
        t0 = r["tour0"] if isinstance(r["tour0"], dict) else ast.literal_eval(r["tour0"])
        s, rep = ref[(int(r["item"]), int(r["k"]))]
        n += 1
        graine += int(r["graine_tour0"]) == s
        ident += t0["resp"] == rep
        deb50 += t0["resp"][:50] == rep[:50]
        if t0["resp"] != rep:
            div.append(premiere_divergence(t0["resp"], rep))
    res[nom] = (n, graine, ident, deb50, div)
    log("bloc C tour 0, bras %s contre c2%s NEUTRE : n %d ; meme graine %d ; sortie identique "
        "%d ; 50 premiers caracteres identiques %d ; premiere divergence (car.) min %s, "
        "mediane %s, max %s"
        % (nom, "a" if nom == "critique" else "b", n, graine, ident, deb50,
           min(div) if div else "-", statistics.median(div) if div else "-",
           max(div) if div else "-"))

# controle : C2F I2 (phrases historiques, graines du dossier C2-full)
F = json.load(open(C2F, encoding="utf-8"))
hA, pB = table(gA, "hate"), table(gB, "praise")
for val, ref in (("crit", hA), ("elo", pB)):
    rows = [r for r in F["gen"] if r["intensite"] == "I2" and r["valence"] == val]
    g = sum(int(r["graine"]) == ref[(int(r["item"]), int(r["k"]))][0] for r in rows)
    i = sum(r["texte"] == ref[(int(r["item"]), int(r["k"]))][1] for r in rows)
    log("controle C2F I2 %s : n %d ; meme graine que c2%s %d ; sortie identique %d"
        % (val, len(rows), "a" if val == "crit" else "b", g, i))

# temoin auxiliaire de la presence de l'instruction (« Is it good or bad? »)
def part(rows):
    return (sum(bool(re.search(r"\b(good|bad)\b", r[:400], re.I)) for r in rows), len(rows))


for nom, rows in (("c2a neutre", [v[1] for v in neuA.values()]),
                  ("c2b neutre", [v[1] for v in neuB.values()]),
                  ("c2a critique", [v[1] for v in hA.values()]),
                  ("c2b eloge", [v[1] for v in pB.values()]),
                  ("bloc B avorte, SANS instruction",
                   [r["resp"] for r in json.load(open(SANS_INSTR, encoding="utf-8"))["rows"]])):
    a, b = part(rows)
    log("auxiliaire : %-34s « good » ou « bad » dans les 400 premiers caracteres : %d/%d"
        % (nom, a, b))

out = sys.argv[1]
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(J) + "\n")
h = sha_f(out)
with open(out + ".sha256", "w", encoding="utf-8", newline="\n") as f:
    f.write("%s  %s\n" % (h, out.rsplit("/", 1)[-1]))
print("ECRIT", out, h)
