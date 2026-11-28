"""Artefacts du banc C de la vérification « données et fuites » de la chaîne v2 de P4 (vérificateur neuf), v1.
Joués dans le clone d'une branche du monde jouet de la relecture « données » (copie miroir dans le dossier du
vérificateur). Aucun texte de P3 : les fenêtres viennent des textes synthétiques du monde jouet
(donnees/synth/textes-fenetres-p3.jsonl). Résultats changés réécrits au format de `ecrire_resultat` et rescellés ;
tableaux changés rescellés, empreinte reportée au résumé.
Usage : python -I -B artefacts_verif_c_v1.py CAS"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.dont_write_bytecode = True
TEXTES = "donnees/synth/textes-fenetres-p3.jsonl"


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
    lignes = [json.loads(x) for x in Path(TEXTES).read_text(encoding="utf-8").splitlines()]
    return [x["texte"] for x in lignes if x["condition"] == "honnete" and len(set(x["texte"])) > 1]


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


def arret_avec_motif(motif):
    d, dd = run()
    r = json.loads((d / "resume.json").read_text(encoding="utf-8"))["resultat"]
    for x in (dd / "scores-p4.npz", dd / "jetons-principales-p4.npz", d / "identite-p4.json"):
        x.unlink()
        Path(str(x) + ".sha256").unlink()
    partiel = {k: r[k] for k in ("commit_cite", "config_sha256", "instrument_fige", "module_cite", "validation_sha256")}

    def arret(x):
        x.clear()
        x.update({"arret": {"motif": motif, "etape": "bras D, H, B, B′", "garde": None}, "partiel": partiel,
                  "duree_s": r["duree_s"]})
    reecrire(d / "resume.json", arret)
    for j in Path("traces").glob("p4-*/journal.txt"):
        j.write_text("".join(l for l in j.read_text(encoding="utf-8").splitlines(True)
                             if " etape=fin " not in l + " " and " etape=bras tache=" not in l + " "), encoding="utf-8")
        (j.parent / "run.json").write_text("", encoding="utf-8")
    empreintes_des_traces()


cas = sys.argv[1]
T = textes()
if cas == "motif_uxxxx_au_dela_de_400":        # motif d'arrêt : texte échappé en \uXXXX après 450 caractères de remplissage
    arret_avec_motif("GardeArret: " + "y" * 450 + " " + json.dumps(T[0], ensure_ascii=True))
elif cas == "repli_de_l_affichage":            # motif qui recopie un texte, et fichier des textes retiré de la branche
    arret_avec_motif("GardeArret: action illisible : " + T[1].replace("\n", " "))
    subprocess.run(["git", "rm", "-q", TEXTES, TEXTES + ".sha256"], check=True)
elif cas == "historique_seul":                 # texte poussé dans un commit, retiré au commit suivant (arbre final sain)
    t = traces()
    f = t / "run.err"
    avant = f.read_text(encoding="utf-8")
    ajouter(f, "ValueError: action inattendue : " + T[0] + "\n")
    empreintes_des_traces()
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "-c", "user.name=instance de calcul (P4)", "-c", "user.email=instance@invalid", "-c",
                    "commit.gpgsign=false", "commit", "-qm", "essai : texte poussé"], check=True)
    f.write_text(avant, encoding="utf-8")
    empreintes_des_traces()
elif cas == "validation_cle_en_plus":          # validation : une clé de plus (activations), rattachée au résumé
    def ch(t):
        t["activations"] = np.random.default_rng(0).standard_normal((len(t["concept"]), 64))
    tableau("validation-p4.npz", ch, "validation_sha256")
elif cas == "par_jeton_scores_2d":             # scores par jeton en deux dimensions (L, 8) : forme d'activations
    def ch(t):
        for k in ("scores_0", "scores_1"):
            t[k] = np.repeat(t[k][:, None], 8, axis=1)
    tableau("jetons-principales-p4.npz", ch, "jetons_principales_sha256")
elif cas == "validation_noms_permutes":        # noms des sondes de la validation dans l'ordre inverse (colonnes suivies)
    def ch(t):
        t["noms_sondes"] = t["noms_sondes"][::-1].copy()
        t["scores"] = t["scores"][:, ::-1].copy()
    tableau("validation-p4.npz", ch, "validation_sha256")
elif cas in ("fragment_80_dans_groupe", "fragment_62_dans_groupe"):   # fragment d'un texte dans une chaîne de 80 au plus
    n = 80 if cas == "fragment_80_dans_groupe" else 62
    t = max(T, key=len)

    def ch(x):
        g = x["groupe"].astype("<U80")
        g[0] = t[1:1 + n]                       # pire alignement : commence un caractère après une fenêtre
        x["groupe"] = g
    tableau("validation-p4.npz", ch, "validation_sha256")
elif cas == "jeton_au_bord_puis_texte":        # traces seules : dernière ligne du journal = remplissage, jeton à cheval sur
    ajouter(traces() / "journal.txt",           # la borne d'affichage, puis un texte
            "z" * 380 + os.environ["JETON_FUITE"] + " " + T[2].replace("\n", " ") + "\n")
    empreintes_des_traces()
else:
    raise SystemExit(f"cas inconnu : {cas}")
print(f"artefact {cas} préparé")
