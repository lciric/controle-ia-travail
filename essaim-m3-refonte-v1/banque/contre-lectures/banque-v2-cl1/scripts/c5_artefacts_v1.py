"""Contre-lecture banque v2 — c5 : artefacts passés au vérificateur scellé (`verifier_identifiants_opaques_v1.py`).

Chaque artefact est une copie de la v2 où seuls les identifiants changent (textes, vérités, parts, ordre identiques) :
- A1 « fuite sur une part » : délégation, suffixe exact -a (sabotage) / -b (honnete) sur train et test_final, suffixe
  tiré au hasard sur test ;
- A2 « fuite partielle » : délégation, suffixe juste avec probabilité 0,80 sur les trois parts (un tirage, graine fixée) ;
- A3 « numérotation dans l'ordre du fichier » : t-{rang+1:04d} sans permutation (erreur de construction plausible).
Le vérificateur est lancé sans --v1 (contrôle des règles seul), comme dans les essais (point 6, « contrôle des règles
seul »). Les artefacts et les sorties vont sous /var/tmp/contre-lecture-banque-v2-v1/ ; rien n'est écrit ailleurs.
Graine : SeedSequence(2026102505).
Usage : python3 -I c5_artefacts_v1.py BANQUE_V2 VERIFICATEUR DOSSIER_SORTIE
"""
import hashlib
import json
import pathlib
import subprocess
import sys

import numpy as np

PARTS = ("train", "test", "test_final")


def ecrire(p, b):
    if p.exists():
        sys.exit(f"{p} existe déjà (R12)")
    p.write_text(json.dumps(b, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    p.with_name(p.name + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def copie(b):
    return json.loads(json.dumps(b, ensure_ascii=False))


def main(pv2, verif, sortie):
    sortie = pathlib.Path(sortie)
    (sortie / "artefacts").mkdir(parents=True, exist_ok=True)
    b = json.loads(pathlib.Path(pv2).read_text(encoding="utf-8"))
    rng = np.random.default_rng(np.random.SeedSequence(2026102505))
    code = lambda y: "a" if y == "sabotage" else "b"
    arts = {}
    a1 = copie(b)
    for p in PARTS:
        for t in a1[p]:
            if t["famille"] == "controle-delegation":
                t["id"] += "-" + (code(t["verite"]) if p != "test" else str(rng.choice(["a", "b"])))
    arts["A1-fuite-train-et-test-final"] = a1
    a2 = copie(b)
    for p in PARTS:
        for t in a2[p]:
            if t["famille"] == "controle-delegation":
                juste = rng.random() < 0.80
                t["id"] += "-" + (code(t["verite"]) if juste else ("b" if code(t["verite"]) == "a" else "a"))
    arts["A2-fuite-partielle-0.80"] = a2
    a3 = copie(b)
    k = 0
    for p in PARTS:
        for t in a3[p]:
            k += 1
            t["id"] = f"t-{k:04d}"
    arts["A3-numerotation-ordre-fichier"] = a3
    for nom, art in arts.items():
        f = sortie / "artefacts" / f"artefact-{nom}-v1.json"
        h = ecrire(f, art)
        r = subprocess.run([sys.executable, "-I", verif, str(f)], capture_output=True, text=True)
        (sortie / "sorties" / f"c5-verificateur-{nom}-v1.json").write_text(r.stdout, encoding="utf-8")
        rap = json.loads(r.stdout)
        print(f"{nom} ({h[:12]}…) : code de sortie du vérificateur {r.returncode}")
        for fam, rr in rap["regles"].items():
            m = rr["meilleures"][0]
            # meilleure règle sur test_final seul (la part décisive)
            print(f"   {fam:22s} prédictives {len(rr['predictives'])} ; max test {rr['max_test']} ; max test_final {rr['max_test_final']} ; "
                  f"première des « meilleures » {m['regle']} {m['test']}/{m['test_final']}")
    # A3 : décodeur « rang dans la part » appris sur l'entraînement, sans E (les numéros suffisent)
    print("A3 : décodeur sans clé — dans chaque part, trier les numéros ; délégation : parité de la position ; conscience : première moitié « evaluation »")
    pos = {"controle-delegation": "sabotage", "conscience-evaluation": "evaluation"}
    for p in ("test", "test_final"):
        for fam in pos:
            l = sorted((t for t in a3[p] if t["famille"] == fam), key=lambda t: t["id"])
            pred = [("honnete" if j % 2 == 0 else "sabotage") if fam == "controle-delegation" else ("evaluation" if j < len(l) / 2 else "usage-reel")
                    for j, _ in enumerate(l)]
            vrai = [t["verite"] for t in l]
            npos = sum(v == pos[fam] for v in vrai)
            tp = sum(a == v == pos[fam] for a, v in zip(pred, vrai)); tn = sum(a == v != pos[fam] for a, v in zip(pred, vrai))
            print(f"   {p:10s} {fam:22s} exactitude équilibrée {round((tp / npos + tn / (len(vrai) - npos)) / 2, 4)}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
