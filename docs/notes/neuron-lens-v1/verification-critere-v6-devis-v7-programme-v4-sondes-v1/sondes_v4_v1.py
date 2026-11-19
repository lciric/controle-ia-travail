"""Sondes synthétiques du programme de comparaison v4 (4a0f3b2c…), sans aucune pièce de diag/ ni de runs/ : pièces inventées."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cmp4", ICI / "comparer_reajustement_v4.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
REF = m.REFERENCES
H = "ab" * 32


def base(L="R", eg=False):
    d64 = {"mid": [0.05 + 0.001 * i for i in range(32)], "out": [0.04 + 0.001 * i for i in range(31 if L == "R" else 32)]}
    ref = {"sha256": "11" * 32, "taille": 100, "finies": True, "diffs_float64": d64, "diffs": copy.deepcopy(d64),
           "meta": {"lens": L, "docs": 932}, "n_docs": [466, 466], "next_doc": 932, "fichier": "f.pt",
           "debut_utc": "2026-11-18T18:03:15Z", "etape": f"ajustement-{L}"}
    neuf = copy.deepcopy(ref); neuf["debut_utc"] = "2026-11-20T10:00:00Z"
    if not eg:
        neuf["sha256"] = "22" * 32; neuf["diffs_float64"]["mid"][0] += 1e-4; neuf["diffs"]["mid"][0] += 1e-4
    cfg = {"ajustement": "a", "correctifs": ["c1", "c2"], "graines": "g", "modele": "m", "revision": "r", "corpus": "k",
           "commit_voisin": "v", "drowse": {"version": "6.1.4"}, "precision": "p"}
    mref = {"commit": "5e5", "depot_propre": True, "config": cfg, "versions": {"python": "3.12.16", "plateforme": "x"}, "commande": "c18"}
    mneuf = copy.deepcopy(mref); mneuf["commit"] = "neuf"; mneuf["commande"] = "c20"
    sp = {"ajustement_ref": REF[f"ajustement-{L}"], "ajustement_neuf": "44" * 32, "manifeste_ref": REF["manifeste"],
          "manifeste_neuf": "33" * 32, "lanceur_neuf": "55" * 32}
    c = {"ref": ref, "neuf": neuf, "env_ref": {"run_id": "run18", "resultat": ref}, "env_neuf": {"run_id": "run20", "manifeste_sha256": "33" * 32, "resultat": neuf},
         "mref": mref, "mneuf": mneuf, "lentille": L, "sha_pieces": sp, "commit_resultats": "0" * 40,
         "correctifs_ref": {"c1": H, "c2": H}, "correctifs_neuf": {"c1": H, "c2": H}, "fref": REF["fonction"], "fneuf": REF["fonction"],
         "eref": None, "eneuf": None, "env_eneuf": None}
    if L == "R":
        mm = {str(k): [H, "cd" * 32] for k in range(31)}
        val = {"npR_notre_R": {str(k): 0.1 + 0.01 * k for k in range(28)}, "identite_notre_R": {str(k): 1.0 + 0.01 * k for k in range(28)}}
        c["eref"] = {"etape": "export", "matrices_moities": mm, "valeurs": val}
        e2 = copy.deepcopy(c["eref"])
        if not eg:
            e2["matrices_moities"]["0"] = ["ef" * 32, "cd" * 32]; e2["valeurs"]["npR_notre_R"]["0"] += 0.002
            e2["valeurs"]["identite_notre_R"]["0"] += 0.003
        c["eneuf"] = e2
        c["env_eneuf"] = {"run_id": "run20", "manifeste_sha256": "33" * 32, "resultat": e2}
        sp["export_ref"], sp["export_neuf"] = REF["export-R"], "66" * 32
    c["rattachement"] = {k: {"tenu": True, "detail": "ok", "sha256_au_commit": sp.get(k)} for k in
                         ("commit_resultats", "ajustement_neuf", "manifeste_neuf", "lanceur_neuf", "export_neuf",
                          "commit_manifeste_ref", "commit_manifeste_neuf")}
    return c


def jouer(nom, c):
    r = m.comparer(c)
    print(f"{nom} : {r['mention']} | décl. {[d[:45] for d in r['declencheurs']]} | audit_requis {r.get('audit_requis')} | "
          f"arrêt {r.get('arret_sur_erreur')} | manqués {[p['nom'][:70] for p in r.get('preconditions', []) if not p['tenu']]}")


jouer("W0 témoin R, palier 2", base())
jouer("W0b témoin R, palier 1", base("R", True))
jouer("W0c témoin S, palier 2", base("S"))
c = base(); c["mneuf"]["depot_propre"] = False; jouer("W1 depot_propre faux", c)
c = base(); c["rattachement"]["lanceur_neuf"]["tenu"] = False; jouer("W2 lanceur neuf non rattaché", c)
c = base(); c["rattachement"]["ajustement_neuf"]["tenu"] = False; jouer("W3 pièce neuve hors du commit (K1)", c)
c = base(); c["mneuf"]["versions"] = ["torch"]; jouer("W4 versions en liste", c)
c = base(); c["neuf"]["diffs_float64"]["mid"][0] += 0.01; jouer("W5 « différente »", c)
c = base(); c["eneuf"]["valeurs"] = "x"; jouer("W6 valeurs d'export en texte", c)
c = base(); c["neuf"] = "pas un dictionnaire"; jouer("W7 résultat neuf en texte", c)
c = base(); c["eneuf"]["etape"] = "ajustement-R"; jouer("W8 étape de l'export fausse", c)
with tempfile.TemporaryDirectory() as d:
    prog = str(ICI / "comparer_reajustement_v4.py")
    r = subprocess.run([sys.executable, "-I", prog, "--sortie", f"{d}/s.json"], capture_output=True)
    print("W9 ligne de commande refusée : code", r.returncode, "; sortie écrite :", Path(f"{d}/s.json").exists(),
          "; message :", r.stderr.decode()[:50].replace("\n", " "))
    args = ["--ref-ajustement", f"{d}/a", "--neuf-ajustement", f"{d}/b", "--ref-manifeste", f"{d}/c", "--neuf-manifeste", f"{d}/e",
            "--lanceur-ref", f"{d}/f", "--lanceur-neuf", f"{d}/g", "--sortie", f"{d}/s.json", "--depot", d,
            "--commit-resultats", "0" * 40, "--chemin-lanceur-neuf", "g"]
    Path(f"{d}/s.json").write_text("{}")
    r = subprocess.run([sys.executable, "-I", prog, *args], capture_output=True)
    print("W10 sortie déjà présente : code", r.returncode, "; message :", r.stderr.decode()[:60].replace("\n", " "))
    Path(f"{d}/s.json").unlink()
    r = subprocess.run([sys.executable, "-I", prog, *args], capture_output=True)
    o = json.loads(Path(f"{d}/s.json").read_text()) if Path(f"{d}/s.json").exists() else {}
    print("W11 pièces absentes : code", r.returncode, "; sortie écrite :", Path(f"{d}/s.json").exists(), "; arrêt :",
          o.get("arret_sur_erreur"), "; mention :", o.get("mention"), "; audit_requis :", o.get("audit_requis"), "; critere :", o.get("critere"))
