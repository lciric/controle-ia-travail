import importlib.util, json, subprocess, hashlib, sys, re
D = "/home/user/controle-ia-travail"
spec = importlib.util.spec_from_file_location("ex4", D + "/docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for nom in ("script", "sortie"):
    fp = f"docs/notes/g1-extraits-tiers-v1/fiches/fiche-calculs-g1-brouillon7-{nom}-v1.json"
    fiche = json.load(open(D + "/" + fp, encoding="utf-8"))
    print(nom, "cles", sorted(fiche))
    regen = m.fabriquer(fiche, fp)
    disque = open(D + "/" + fiche["sortie"], "rb").read()
    print(" regeneration identique :", regen.encode("utf-8") == disque)
    # verification independante : chaque ligne gardee == source a l'octet, sauf passages
    src = subprocess.run(["git", "show", f"{fiche['ref']}:{fiche['source']}"], cwd=D, capture_output=True, check=True).stdout
    print(" empreinte source", hashlib.sha256(src).hexdigest()[:16], "attendu", fiche["empreinte_attendue"])
    L = src.decode().split("\n");
    if L[-1] == "": L = L[:-1]
    E = disque.decode().split("\n")
    # locate body
    i = E.index("---") + 2
    body = E[i:]
    k = 0; ok = True
    for a, b in sorted(map(tuple, fiche["plages"])):
        # skip markers
        while not body[k].startswith(f"<!-- lignes {a} à {b} de la source -->"):
            print("   marqueur:", body[k]); k += 1
        k += 1
        for n in range(a, b + 1):
            if body[k] != L[n-1]:
                print("   DIFFERENCE ligne", n)
                print("     src:", L[n-1]); print("     ext:", body[k])
                # check passages
                for p in fiche["passages"]:
                    if p["ligne"] == n:
                        print("     omis:", repr(L[n-1][p["debut"]:p["fin"]]))
                        recon = L[n-1][:p["debut"]] + "[passage non repris]" + L[n-1][p["fin"]:]
                        print("     reconstitution conforme:", recon == body[k])
            k += 1
    print("   reste:", body[k:])
