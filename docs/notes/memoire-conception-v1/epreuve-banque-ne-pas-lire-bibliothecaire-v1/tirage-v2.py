"""Réduction et moitiés (v2), epreuve-bibliothecaire-v2.md, § 2, appliqué à la lettre.
Entrée : jeu-final-v1.jsonl. Sorties : jeu-epreuve-v2.jsonl, ecartees-v2.jsonl, bilan-reduction-v2.md."""
import json, collections, hashlib
import numpy

ORDRE = ["paraphrase", "confusion", "detail", "sans_reponse", "hors_perimetre", "erratum"]
CIBLES = {"paraphrase": 30, "confusion": 10, "detail": 10, "sans_reponse": 20, "hors_perimetre": 10, "erratum": 10}
ENTREE = "jeu-final-v1.jsonl"

with open(ENTREE, "rb") as f:
    brut = f.read()
lignes = [json.loads(l) for l in brut.decode("utf-8").splitlines() if l.strip()]
par_id = {d["id"]: d for d in lignes}
assert len(par_id) == len(lignes)
assert set(d["type"] for d in lignes) == set(ORDRE)

gardees, ecartees, bilan = [], [], []
for k, t in enumerate(ORDRE):
    ids = sorted(d["id"] for d in lignes if d["type"] == t)
    n = CIBLES[t]
    assert len(ids) >= n
    rng = numpy.random.default_rng(numpy.random.SeedSequence([2026112202, k]))
    perm = [ids[i] for i in rng.permutation(len(ids))]
    garde, ecarte = perm[:n], perm[n:]
    rng2 = numpy.random.default_rng(numpy.random.SeedSequence([2026112203, k]))
    perm2 = [garde[i] for i in rng2.permutation(len(garde))]
    m = len(perm2) // 2
    moitie = {i: ("mise_au_point" if r < m else "reserve") for r, i in enumerate(perm2)}
    for i in sorted(garde):
        d = dict(par_id[i]); d["moitie"] = moitie[i]
        gardees.append(d)
    for i in sorted(ecarte):
        ecartees.append({"id": i, "type": t})
    nm = sum(1 for v in moitie.values() if v == "mise_au_point")
    assert len(garde) == n
    bilan.append((t, len(ids), len(garde), len(ecarte), nm, len(garde) - nm))

gardees.sort(key=lambda d: d["id"])
with open("jeu-epreuve-v2.jsonl", "w", encoding="utf-8") as f:
    for d in gardees:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
with open("ecartees-v2.jsonl", "w", encoding="utf-8") as f:
    for d in ecartees:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
assert len(gardees) == 90 and len(ecartees) == 19

def h(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

with open("bilan-reduction-v2.md", "w", encoding="utf-8") as f:
    f.write("# Bilan de la réduction et des moitiés (v2)\n\n")
    f.write("- Règle : `epreuve-bibliothecaire-v2.md`, § 2, « Réduction et moitiés (v2) » ; script `tirage-v2.py` ; numpy %s.\n" % numpy.__version__)
    f.write("- Entrée : `%s`, sha256 `%s`.\n" % (ENTREE, hashlib.sha256(brut).hexdigest()))
    f.write("- Graines : réduction `SeedSequence([2026112202, k])`, moitiés `SeedSequence([2026112203, k])`, k = rang du type (0 à 5).\n\n")
    f.write("| Type | Concordantes | Gardées (cible) | Écartées | mise_au_point | reserve |\n|---|---|---|---|---|---|\n")
    for t, c, g, e, nm, nr in bilan:
        f.write("| %s | %d | %d (%d) | %d | %d | %d |\n" % (t, c, g, CIBLES[t], e, nm, nr))
    tot = [sum(b[i] for b in bilan) for i in range(1, 6)]
    f.write("| total | %d | %d (90) | %d | %d | %d |\n\n" % tuple(tot))
    f.write("- Sorties : `jeu-epreuve-v2.jsonl` sha256 `%s` ; `ecartees-v2.jsonl` sha256 `%s`.\n" % (h("jeu-epreuve-v2.jsonl"), h("ecartees-v2.jsonl")))
    f.write("- Chaque type atteint exactement sa cible (vérifié par assertion).\n")
for b in bilan:
    print(b)
