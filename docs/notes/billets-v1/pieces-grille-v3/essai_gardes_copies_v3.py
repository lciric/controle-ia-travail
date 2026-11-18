"""Essai scellé des gardes de preparer_copies_neutres_v3.py, sur la moitié DÉVELOPPEMENT seulement.

Ne passe JAMAIS d'identifiant d'accord valide : la tenue à l'écart n'est jamais lue. Les dépôts de la
passe 1 sont fabriqués par programme (modalités hors indicateur, un appui réel avant la borne pour
G02) : ce ne sont pas des codages. Tout est écrit dans un dossier temporaire supprimé à la fin ; la
sortie ne contient que des codes de retour, des messages de refus et des décomptes.

Usage : python -B essai_gardes_copies_v3.py MANIFESTE_V2 RACINE_DEV GRILLE DOSSIER_TEMPORAIRE SORTIE_JSON
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from controler_depot_v1 import lire_grille, norm  # noqa: E402


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def lancer(args):
    r = subprocess.run([sys.executable, "-B", os.path.join(ICI, "preparer_copies_neutres_v3.py"), *args],
                       capture_output=True, text=True)
    return {"code": r.returncode, "message": (r.stdout + r.stderr).strip().splitlines()[-1][:200] if (r.stdout + r.stderr).strip() else ""}


def sceller(p):
    open(p + ".sha256", "w").write(f"{sha(p)}  {os.path.basename(p)}\n")


def depot(grille, copies, codeur, chemin, incomplet=False):
    G = lire_grille(grille)
    lignes = []
    for f in sorted(os.listdir(copies)):
        b = f[:-3]
        avant = open(os.path.join(copies, f), encoding="utf-8").read().split("⟦FIN")[0]
        for g, v in G.items():
            m = [x for x in v["modalites"] if x not in v["indicateur"]][0]
            ap = ""
            if g == "G02":
                m, ap = "en-tête", " ".join(norm(avant).split()[-12:])
            lignes.append({"codeur": codeur, "billet": b, "geste": g, "modalite": m, "appui": ap, "doute": False})
        lignes.append({"codeur": codeur, "billet": b, "geste": "AVEUGLE", "reconnu": False, "pari_statut": "ne-sait-pas"})
    if incomplet:
        lignes = lignes[:-30]
    open(chemin, "w", encoding="utf-8").write("\n".join(json.dumps(l, ensure_ascii=False) for l in lignes) + "\n")


def main(man, racine, grille, tmp, sortie):
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.makedirs(tmp)
    S = os.path.join(tmp, "sortie")
    base = ["--manifeste", man]
    res = {"version": "v1", "script": {"preparer_copies_neutres_v3.py": sha(os.path.join(ICI, "preparer_copies_neutres_v3.py"))},
           "grille": sha(grille), "manifeste_v2": sha(man), "identifiant_d_accord_valide_passe": False, "essais": {}}
    E = res["essais"]
    E["tenue_sans_go"] = lancer(["--passe", "1", *base, "--moitie", "tenue-a-l-ecart", "--racine", "/chemin/inexistant", "--sortie", S])
    E["tenue_go_malforme"] = lancer(["--passe", "1", *base, "--moitie", "tenue-a-l-ecart", "--racine", "/chemin/inexistant", "--sortie", S, "--go", "GO-mal-forme"])
    E["tenue_avec_pilote"] = lancer(["--passe", "1", *base, "--moitie", "tenue-a-l-ecart", "--racine", "/chemin/inexistant", "--sortie", S, "--pilote", "/chemin/inexistant.json"])
    E["dossier_cree_par_les_refus"] = os.path.exists(S)
    E["passe_2_avant_passe_1_sans_depots"] = lancer(["--passe", "2", *base, "--moitie", "developpement", "--racine", racine, "--sortie", S])
    E["passe_1_developpement"] = lancer(["--passe", "1", *base, "--moitie", "developpement", "--racine", racine, "--sortie", S])
    arbo = sorted(os.path.relpath(os.path.join(d, x), S) for d, _, fs in os.walk(S) for x in fs)
    E["passe_1_contenu"] = {
        "dossiers": sorted({p.split(os.sep)[0] + "/" + (p.split(os.sep)[1] if len(p.split(os.sep)) > 2 else "") for p in arbo}),
        "fichiers_par_codeur": {k: sum(1 for p in arbo if p.startswith(f"passe-1/codeur-{k}/")) for k in (1, 2)},
        "fichiers_de_commentaires": sum(1 for p in arbo if "commentaires" in p),
        "dossier_passe_2_existe": os.path.exists(os.path.join(S, "passe-2")),
    }
    c1 = os.path.join(S, "passe-1", "codeur-1", "billets")
    dep = os.path.join(tmp, "depots")
    os.makedirs(dep)
    d1, d2, dinc, dnon = (os.path.join(dep, n) for n in ("c1.jsonl", "c2.jsonl", "inc.jsonl", "non-scelle.jsonl"))
    depot(grille, c1, "C1", d1)
    depot(grille, c1, "C2", d2)
    depot(grille, c1, "C2", dinc, incomplet=True)
    depot(grille, c1, "C2", dnon)
    for p in (d1, d2, dinc):
        sceller(p)
    p2 = ["--passe", "2", *base, "--moitie", "developpement", "--racine", racine, "--sortie", S, "--grille", grille]
    E["passe_2_sans_depots"] = lancer(p2)
    E["passe_2_depot_sans_compagnon"] = lancer([*p2, "--depot1", d1, "--depot2", dnon])
    vrai = open(d2 + ".sha256").read()
    open(d2 + ".sha256", "w").write("0" * 64 + vrai[64:])
    E["passe_2_compagnon_faux"] = lancer([*p2, "--depot1", d1, "--depot2", d2])
    open(d2 + ".sha256", "w").write(vrai)
    E["passe_2_depot_incomplet_scelle"] = lancer([*p2, "--depot1", d1, "--depot2", dinc])
    E["passe_2_ecrite_apres_refus"] = os.path.exists(os.path.join(S, "passe-2"))
    E["passe_2_cas_sain"] = lancer([*p2, "--depot1", d1, "--depot2", d2])
    m2 = json.load(open(os.path.join(S, "cles", "manifeste-preparation-passe-2.json")))
    E["passe_2_cas_sain_decomptes"] = {"commentaires": m2["commentaires"], "reponses_d_auteur": m2["reponses_d_auteur"],
                                      "codables": m2["codables"],
                                      "fichiers": len(os.listdir(os.path.join(S, "passe-2", "commentaires")))}
    E["passe_2_deuxieme_fois"] = lancer([*p2, "--depot1", d1, "--depot2", d2])
    m1 = json.load(open(os.path.join(S, "cles", "manifeste-preparation-passe-1.json")))
    res["borne"] = m1["borne"]
    attendu_refus = ["tenue_sans_go", "tenue_go_malforme", "tenue_avec_pilote", "passe_2_avant_passe_1_sans_depots",
                     "passe_2_sans_depots", "passe_2_depot_sans_compagnon", "passe_2_compagnon_faux",
                     "passe_2_depot_incomplet_scelle", "passe_2_deuxieme_fois"]
    ok = (all(E[k]["code"] == 2 for k in attendu_refus) and E["passe_1_developpement"]["code"] == 0
          and E["passe_2_cas_sain"]["code"] == 0 and not E["dossier_cree_par_les_refus"]
          and E["passe_1_contenu"]["fichiers_de_commentaires"] == 0 and not E["passe_1_contenu"]["dossier_passe_2_existe"]
          and not E["passe_2_ecrite_apres_refus"])
    res["verdict"] = "OK" if ok else "ECHEC"
    shutil.rmtree(tmp)
    json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(res["verdict"])
    for k, v in E.items():
        print(k, v)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:6]))
