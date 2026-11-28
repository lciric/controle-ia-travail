"""Différentiel v6 → v7 rejoué et contrôlé (correcteur v7). Rejouable.

A. Rejeu : appliquer_corrections_v7.py relancé vers une copie ; octets égaux à la v7.
B. Blancs normalisés : v6, avec chacun des 7 remplacements (ancien trouvé une fois), égale la v7 ; rien d'autre.
C. Structure : lignes vides, lignes de table (et barres par ligne), titres : égaux de part et d'autre.
E. Passage final de chaque texte neuf dans la v7 (lignes).
D. Différentiel ligne à ligne (difflib) : chaque bloc rattaché au remplacement dont le passage final le chevauche.
F. Mentions « [Décision de Lazar en attente » : avant, après.
G. Épreuve R5 des gardes du script : cas sain accepté ; artefacts arrêtés (ancien texte changé d'un mot, ancien texte
   doublé, compagnon faux, octets ajoutés avec compagnon recalculé, compagnon absent).
Usage : PYTHONDONTWRITEBYTECODE=1 python3 -I -B verifier_v7.py
"""
import difflib
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ICI = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/correction-v7")
spec = importlib.util.spec_from_file_location("ap7", ICI / "appliquer_corrections_v7.py")
ap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ap)
V7 = ap.RD / "synthese-comment-detecter-v7.md"
fautes = []


def norm(s):
    return " ".join(s.split())


def faute(m):
    fautes.append(m)
    print("FAUTE |", m)


def main():
    v6 = ap.lire_controle(ap.V6, ap.V6_SHA)
    b7 = V7.read_bytes()
    v7 = b7.decode("utf-8")
    print(f"v6 {ap.V6_SHA}\nv7 {hashlib.sha256(b7).hexdigest()}")
    E = [(d["etiquette"], d["ancien"], d["nouveau"]) for d in json.loads((ICI / "corrections-v7.json").read_text())]
    E2 = ap.extraire(ap.lire_controle(ap.VV6, ap.VV6_SHA)) + ap.REMARQUES
    print("A | corrections-v7.json égal à une nouvelle extraction :", E == E2) if E == E2 else faute("A | json ≠ extraction")

    # A. rejeu
    rej = ICI / "v7-rejouee.md"
    if rej.exists():
        rej.unlink()
    r = subprocess.run([sys.executable, "-I", "-B", str(ICI / "appliquer_corrections_v7.py"), str(rej)],
                       capture_output=True, text=True, env={"PYTHONDONTWRITEBYTECODE": "1"})
    if r.returncode != 0 or rej.read_bytes() != b7:
        faute(f"A | rejeu différent : {r.stderr[-200:]}")
    else:
        print("A | rejeu : v7 identique octet pour octet")
    rej.unlink()

    # B. blancs normalisés
    n6 = norm(v6)
    for etiq, a, b in E:
        k = n6.count(norm(a))
        if k != 1:
            faute(f"B | {etiq} : ancien texte normalisé trouvé {k} fois")
        n6 = n6.replace(norm(a), norm(b))
    print("B | v6 + 7 remplacements = v7 (blancs normalisés) :", n6 == norm(v7)) if n6 == norm(v7) else faute(
        "B | v6 + remplacements ≠ v7 : autre chose a changé")

    # C. structure
    L6, L7 = v6.split("\n"), v7.split("\n")
    vide = lambda L: sum(not l.strip() for l in L)
    table = lambda L: [l.count("|") for l in L if l.startswith("|")]
    titres = lambda L: [l for l in L if l.startswith("#")]
    for nom, f in (("lignes vides", vide), ("barres par ligne de table", table), ("titres", titres)):
        x, y = f(L6), f(L7)
        if x != y:
            faute(f"C | {nom} diffèrent")
        else:
            print(f"C | {nom} : égaux ({x if isinstance(x, int) else len(x)})")
    print(f"C | lignes : v6 {len(L6) - 1}, v7 {len(L7) - 1}")

    # E. passages finaux
    passages = {}
    for etiq, a, b in E:
        m = list(re.finditer(r"\s+".join(re.escape(t) for t in b.split()), v7))
        if len(m) != 1:
            faute(f"E | {etiq} : texte neuf trouvé {len(m)} fois dans la v7")
            continue
        l1 = v7.count("\n", 0, m[0].start()) + 1
        l2 = v7.count("\n", 0, m[0].end()) + 1
        passages[etiq] = (l1, l2)
        print(f"E | {etiq} | v7 l. {l1}-{l2}")

    # D. différentiel ligne à ligne
    sm = difflib.SequenceMatcher(None, L6, L7, autojunk=False)
    blocs = [o for o in sm.get_opcodes() if o[0] != "equal"]
    out = []
    for tag, i1, i2, j1, j2 in blocs:
        rat = [e for e, (l1, l2) in passages.items() if l1 <= j2 and l2 >= j1 + 1]
        out.append(f"{tag} | v6 l. {i1 + 1}-{i2} | v7 l. {j1 + 1}-{j2} | rattaché : {', '.join(rat) or 'AUCUN'}")
        if not rat:
            faute(f"D | bloc v6 l. {i1 + 1}-{i2} sans remplacement")
    print(f"D | {len(blocs)} blocs de différentiel")
    for l in out:
        print("D |", l)
    (ICI / "differentiel-lignes-v6-v7.txt").write_text(
        "\n".join(difflib.unified_diff(L6, L7, "synthese-comment-detecter-v6.md", "synthese-comment-detecter-v7.md",
                                       n=0, lineterm="")) + "\n", encoding="utf-8")

    # F. mentions
    mo = "[Décision de Lazar en attente"
    print(f"F | mentions « {mo} » : v6 {v6.count(mo)}, v7 {v7.count(mo)}")

    # G. épreuve R5
    try:
        ap.appliquer(v6, E)
        print("G | cas sain : accepté")
    except SystemExit as e:
        faute(f"G | cas sain refusé : {e}")
    a0 = E[0][1]
    artefacts = {
        "ancien texte changé d'un mot": [(E[0][0], a0.replace("oracle", "oracles"), E[0][2])],
        "ancien texte doublé": [(E[2][0], E[2][1], E[2][2])],
    }
    for nom, EE in artefacts.items():
        txt = v6 if "doublé" not in nom else v6 + "\n" + E[2][1] + "\n"
        try:
            ap.appliquer(txt, EE)
            faute(f"G | artefact « {nom} » accepté")
        except SystemExit as e:
            print(f"G | artefact « {nom} » : arrêté ({str(e)[:70]})")
    ep = ICI / "epreuve-garde"
    if ep.exists():
        shutil.rmtree(ep)
    ep.mkdir()
    nm = ap.V6.name
    cas = {
        "sain": (ap.V6.read_bytes(), f"{ap.V6_SHA}  {nm}\n"),
        "compagnon faux": (ap.V6.read_bytes(), f"{'0' * 64}  {nm}\n"),
        "octets ajoutés, compagnon recalculé": (ap.V6.read_bytes() + b"x",
                                                 hashlib.sha256(ap.V6.read_bytes() + b"x").hexdigest() + f"  {nm}\n"),
        "nom faux dans le compagnon": (ap.V6.read_bytes(), f"{ap.V6_SHA}  autre.md\n"),
        "compagnon absent": (ap.V6.read_bytes(), None),
    }
    for nom, (octets, comp) in cas.items():
        p = ep / nm
        p.write_bytes(octets)
        c = ep / (nm + ".sha256")
        if c.exists():
            c.unlink()
        if comp is not None:
            c.write_text(comp)
        try:
            ap.lire_controle(p, ap.V6_SHA)
            res = "accepté"
        except (SystemExit, FileNotFoundError) as e:
            res = "arrêté"
        attendu = "accepté" if nom == "sain" else "arrêté"
        (print if res == attendu else faute)(f"G | garde d'empreinte, {nom} : {res}")
    shutil.rmtree(ep)
    print(f"bilan : {len(fautes)} faute(s)" + ("" if fautes else " ; différentiel et gardes conformes"))
    sys.exit(1 if fautes else 0)


if __name__ == "__main__":
    main()
