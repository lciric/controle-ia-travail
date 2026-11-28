"""Artefacts de la relecture « données et fuites » (v2 : v1 plus le cas « jeton_dans_le_journal »), joués dans le clone d'une branche jouet (instance jouet de P4).
Aucun texte de P3 : les fenêtres viennent des textes synthétiques du monde jouet (donnees/synth/textes-fenetres-p3.jsonl).
Les résultats changés sont réécrits au format de `ecrire_resultat` (même manifeste) et rescellés ; les tableaux changés
sont rescellés et leur empreinte reportée au résumé (rattachement) quand l'artefact vise une garde de forme.
Usage : python -I -B artefacts_relecture_v1.py CAS"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.dont_write_bytecode = True


def sha(f):
    return hashlib.sha256(Path(f).read_bytes()).hexdigest()


def resceller(f):
    f = Path(f)
    Path(str(f) + ".sha256").write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def run():
    d = [x for x in Path("diag").glob("*-p4-jouet") if x.is_dir()]
    assert len(d) == 1, d
    return d[0], Path("donnees") / d[0].name


def reecrire(chemin, maj):
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    maj(corps["resultat"])
    Path(chemin).write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    resceller(chemin)


def traces():
    t = sorted(Path("traces").glob("p4-*/"))
    assert t, "aucune trace"
    return t[-1]


def empreintes_des_traces():
    for d in Path("traces").glob("p4-*/"):
        (d / "empreintes.sha256").write_text("".join(f"{sha(x)}  {x.name}\n" for x in sorted(d.iterdir())
                                                     if x.name != "empreintes.sha256"), encoding="utf-8")


def ajouter(f, texte):
    f = Path(f)
    f.write_text((f.read_text(encoding="utf-8") if f.exists() else "") + texte, encoding="utf-8")


def textes():
    lignes = [json.loads(x) for x in Path("donnees/synth/textes-fenetres-p3.jsonl").read_text(encoding="utf-8").splitlines()]
    return [x["texte"] for x in lignes if x["condition"] == "honnete" and len(set(x["texte"])) > 1]


def milieu(t):
    m = (len(t) - 48) // 2
    return m, t[m:m + 48]


def tableau(nom, change, cle):
    d, dd = run()
    f = dd / nom
    with np.load(f, allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    change(t)
    with open(f, "wb") as h:
        np.savez(h, **t)
    resceller(f)
    reecrire(d / "resume.json", lambda r: r.__setitem__(cle, sha(f)))


cas = sys.argv[1]
if cas == "fenetre_brute_run_err":            # témoin : un texte honnête recopié tel quel dans run.err
    t = textes()[0]
    ajouter(traces() / "run.err", "ValueError: action inattendue : " + t + "\n")
    empreintes_des_traces()
elif cas == "fenetre_echappee_run_err":       # le texte dont la fenêtre du milieu chevauche un saut de ligne, échappé
    t = [x for x in textes() if "\n" in milieu(x)[1]][0]
    ajouter(traces() / "run.err", "ValueError: action inattendue : " + json.dumps(t) + "\n")
    empreintes_des_traces()
elif cas == "texte_partiel_run_err":          # tout le texte sauf sa fenêtre du milieu (début et fin recopiés)
    t = textes()[0]
    m, _ = milieu(t)
    ajouter(traces() / "run.err", "ValueError: début : " + t[:m] + "\nValueError: fin : " + t[m + 48:] + "\n")
    empreintes_des_traces()
elif cas == "traces_seules_fenetre":          # branche sans run (traces seules) : texte recopié dans le journal
    ajouter(traces() / "journal.txt", textes()[0] + "\n")
    empreintes_des_traces()
elif cas == "sceau_faux_validation":
    d, dd = run()
    (dd / "validation-p4.npz.sha256").write_text(f"{'0' * 64}  validation-p4.npz\n", encoding="utf-8")
elif cas == "identite_absente":               # fichier attendu absent (résumé complet)
    d, dd = run()
    (d / "identite-p4.json").unlink()
    (d / "identite-p4.json.sha256").unlink()
elif cas == "validation_activations":         # 4 096 colonnes de type activation à la place des 424 scores
    def ch(t):
        n = len(t["concept"])
        t["noms_sondes"] = np.array([f"dim-{k:04d}" for k in range(4096)])
        t["scores"] = np.random.default_rng(0).standard_normal((n, 4096))
    tableau("validation-p4.npz", ch, "validation_sha256")
elif cas == "par_jeton_longueurs_doublees":   # scores par jeton : longueurs doublées, sans rapport avec jetons_notes
    def ch(t):
        L = t["longueur"]
        deb = np.concatenate([[0], np.cumsum(L)[:-1]]).astype(np.int64)
        for k in ("scores_0", "scores_1"):
            t[k] = np.concatenate([np.repeat(t[k][a:a + l], 2) for a, l in zip(deb, L)]) if len(L) else t[k]
        t["longueur"] = (L * 2).astype(np.int64)
        t["debut"] = np.concatenate([[0], np.cumsum(t["longueur"])[:-1]]).astype(np.int64)
    tableau("jetons-principales-p4.npz", ch, "jetons_principales_sha256")
elif cas == "trace_alteree":                  # trace changée après son sceau (empreintes.sha256 non refait)
    ajouter(traces() / "journal.txt", "ligne ajoutée après le sceau\n")
elif cas == "empreintes_absentes":            # fichier attendu absent : sceau des traces retiré
    (traces() / "empreintes.sha256").unlink()
elif cas == "fenetre_dans_un_tableau":        # fenêtre (48 caractères) dans une chaîne de 80 au plus d'un tableau
    _, w = milieu(textes()[0])
    def ch(t):
        g = t["groupe"].astype("<U80")
        g[0] = w
        t["groupe"] = g
    tableau("validation-p4.npz", ch, "validation_sha256")
elif cas == "motif_avec_fenetre":             # arrêt pendant les bras ; motif d'arrêt qui recopie un texte (≤ 1 000)
    d, dd = run()
    r = json.loads((d / "resume.json").read_text(encoding="utf-8"))["resultat"]
    for x in (dd / "scores-p4.npz", dd / "jetons-principales-p4.npz", d / "identite-p4.json"):
        x.unlink()
        Path(str(x) + ".sha256").unlink()
    partiel = {k: r[k] for k in ("commit_cite", "config_sha256", "instrument_fige", "module_cite", "validation_sha256")}
    t = textes()[0]

    def arret(x):
        x.clear()
        x.update({"arret": {"motif": "GardeArret: action illisible : " + t.replace("\n", " "), "etape": "bras D, H, B, B′",
                            "garde": None}, "partiel": partiel, "duree_s": r["duree_s"]})
    reecrire(d / "resume.json", arret)
    for j in Path("traces").glob("p4-*/journal.txt"):
        j.write_text("".join(l for l in j.read_text(encoding="utf-8").splitlines(True)
                             if " etape=fin " not in l + " " and " etape=bras tache=" not in l + " "), encoding="utf-8")
        (j.parent / "run.json").write_text("", encoding="utf-8")
    empreintes_des_traces()
elif cas == "jeton_dans_le_journal":         # jeton factice (variable JETON_FUITE) recopié dans le journal
    import os
    ajouter(traces() / "journal.txt", "fuite " + os.environ["JETON_FUITE"] + "\n")
    empreintes_des_traces()
else:
    raise SystemExit(f"cas inconnu : {cas}")
print(f"artefact {cas} préparé")
