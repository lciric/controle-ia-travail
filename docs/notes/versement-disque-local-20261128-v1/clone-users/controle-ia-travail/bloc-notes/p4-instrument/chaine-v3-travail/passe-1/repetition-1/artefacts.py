import hashlib, json, os, sys
from pathlib import Path
import numpy as np
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
def empreintes_des_traces():
    for j in Path("traces").glob("p4-*/journal.txt"):
        (j.parent / "empreintes.sha256").write_text("".join(f"{sha(x)}  {x.name}\n" for x in sorted(j.parent.iterdir())
                                                            if x.name != "empreintes.sha256"), encoding="utf-8")
def journal():
    j = sorted(Path("traces").glob("p4-*/journal.txt"))
    assert j, "aucun journal"
    return j[-1]
def tableau(nom, change):           # tableau changé, rescellé, empreinte reportée au résumé
    d, dd = run()
    f = dd / nom
    with np.load(f, allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    change(t)
    with open(f, "wb") as h:
        np.savez(h, **t)
    resceller(f)
    cle = {"scores-p4.npz": "scores_sha256", "validation-p4.npz": "validation_sha256",
           "jetons-principales-p4.npz": "jetons_principales_sha256"}[nom]
    reecrire(d / "resume.json", lambda r: r.__setitem__(cle, sha(f)))
def textes_fenetres():
    return [json.loads(x)["texte"] for x in Path("donnees/synth/textes-fenetres-p3.jsonl").read_text(encoding="utf-8").splitlines()
            if json.loads(x)["condition"] == "honnete" and len(set(json.loads(x)["texte"])) > 1]
quoi = sys.argv[1]
d, dd = run() if quoi not in ("texte_traces_seules", "jeton_traces_seules") else (None, None)   # traces seules : aucun run
if quoi == "arret_synthetique":       # arrêt pendant les bras : tableaux des bras et identité retirés, résumé avec motif
    r = json.loads((d / "resume.json").read_text(encoding="utf-8"))["resultat"]
    for x in (dd / "scores-p4.npz", dd / "jetons-principales-p4.npz", d / "identite-p4.json"):
        x.unlink(); Path(str(x) + ".sha256").unlink()
    partiel = {k: r[k] for k in ("commit_cite", "config_sha256", "instrument_fige", "module_cite", "validation_sha256")}
    def arret(x):
        x.clear()
        x.update({"arret": {"motif": "essai : arrêt simulé pendant les bras", "etape": "bras D, H, B, B′", "garde": None},
                  "partiel": partiel, "duree_s": r["duree_s"]})
    reecrire(d / "resume.json", arret)
    for j in Path("traces").glob("p4-*/journal.txt"):
        j.write_text("".join(l for l in j.read_text(encoding="utf-8").splitlines(True)
                             if " etape=fin " not in l + " " and " etape=bras tache=" not in l + " "), encoding="utf-8")
        (j.parent / "run.json").write_text("", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "ajout_hors_perimetre":   # un fichier de textes ajouté à côté des tableaux (P4 n'en écrit aucun)
    (dd / "textes-p4.jsonl").write_text('{"texte": "essai"}\n', encoding="utf-8")
    os.system(f"git add -f {dd}/textes-p4.jsonl")
elif quoi == "scores_alteres":        # un score changé, tableau rescellé, résumé non mis à jour
    f = dd / "scores-p4.npz"
    with np.load(f, allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    s = t["scores"].copy(); s[tuple(np.argwhere(np.isfinite(s))[0])] += 1.0; t["scores"] = s
    with open(f, "wb") as h:
        np.savez(h, **t)
    resceller(f)
elif quoi == "sceau_des_scores_faux":
    (dd / "scores-p4.npz.sha256").write_text(f"{'0' * 64}  scores-p4.npz\n", encoding="utf-8")
elif quoi == "resultat_autre_manifeste":   # identité rattachée au manifeste d'un autre run du dépôt, rescellée
    autre = Path("runs/20261019-230011-p3-reel")
    f = d / "identite-p4.json"
    corps = json.loads(f.read_text(encoding="utf-8"))
    corps["run_id"], corps["manifeste_sha256"] = autre.name, sha(autre / "manifeste.json")
    f.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    resceller(f)
elif quoi == "scores_hors_plan":       # pas des deux premières lignes échangés : chaque ligne n'est plus à sa place du plan
    def ch(t):
        p = t["pas"].copy(); p[[0, 1]] = p[[1, 0]]; t["pas"] = p
    tableau("scores-p4.npz", ch)
elif quoi == "chaine_longue_dans_un_tableau":
    def ch(t):
        n = t["noms_sondes"].astype("<U120"); n[0] = "sonde-" + "x" * 100; t["noms_sondes"] = n
    tableau("scores-p4.npz", ch)
elif quoi == "texte_dans_le_journal":  # un texte honnête (fenêtres) recopié dans le journal
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + textes_fenetres()[0].replace("\n", " ") + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_echappe":          # texte sur deux lignes dans le résumé : échappé en JSON (fenêtre à cheval)
    x = [t for t in textes_fenetres() if "\n" in t[(len(t) - 48) // 2:(len(t) - 48) // 2 + 48] and len(t) <= 200]
    assert x, "aucun texte des fenêtres dont la fenêtre chevauche un saut de ligne"
    reecrire(d / "resume.json", lambda r: r.__setitem__("note_essai", x[0]))
elif quoi == "chaine_de_plus_de_200":
    reecrire(d / "resume.json", lambda r: r.__setitem__("note_essai", "x" * 250))
elif quoi == "fin_retiree":
    j = journal()
    j.write_text("".join(l for l in j.read_text(encoding="utf-8").splitlines(True) if " etape=fin " not in l + " "), encoding="utf-8")
    empreintes_des_traces()
elif quoi == "jeton_dans_une_trace":
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + "fuite " + os.environ["JETON_FUITE"] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_echappe_trace":   # texte dont la fenêtre du milieu chevauche un saut de ligne, échappé en JSON, dans run.err
    x = [t for t in textes_fenetres() if "\n" in t[(len(t) - 48) // 2:(len(t) - 48) // 2 + 48]]
    assert x, "aucun texte des fenêtres dont la fenêtre du milieu chevauche un saut de ligne"
    e = journal().parent / "run.err"
    e.write_text(e.read_text(encoding="utf-8") + "Traceback (essai) : " + json.dumps(x[0]) + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_sans_milieu":     # tout le texte sauf ses 48 caractères du milieu, dans run.err
    t = textes_fenetres()[0]; m = (len(t) - 48) // 2
    e = journal().parent / "run.err"
    e.write_text(e.read_text(encoding="utf-8") + t[:m] + "\n[...]\n" + t[m + 48:] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_traces_seules":   # branche sans run : un texte recopié dans le journal des traces
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + textes_fenetres()[1] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "jeton_traces_seules":   # branche sans run : un jeton sur la dernière ligne du journal des traces
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + "fuite " + os.environ["JETON_FUITE"] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "validation_4096":       # validation à 4 096 colonnes (forme d'activations), rattachée au résumé
    def ch(t):
        n = len(t["concept"])
        t["noms_sondes"] = np.array([f"dim-{k:04d}" for k in range(4096)]); t["scores"] = np.zeros((n, 4096))
    tableau("validation-p4.npz", ch)
elif quoi == "longueurs_doublees":    # longueurs par jeton doublées, débuts et scores refaits (cohérents entre eux)
    def ch(t):
        L = (t["longueur"] * 2).astype(np.int64)
        t["longueur"] = L
        t["debut"] = (np.concatenate([[0], np.cumsum(L)[:-1]]) if len(L) else np.zeros(0)).astype(np.int64)
        t["scores_0"] = np.concatenate([t["scores_0"], t["scores_0"]]); t["scores_1"] = np.concatenate([t["scores_1"], t["scores_1"]])
    tableau("jetons-principales-p4.npz", ch)
elif quoi == "motif_recopie":         # motif d'arrêt qui recopie un texte (branche d'arrêt synthétique)
    reecrire(d / "resume.json", lambda r: r["arret"].__setitem__("motif", "essai : " + textes_fenetres()[2].replace("\n", " ")))
elif quoi in ("carte_sxm4", "carte_pcie"):
    j = journal()
    ligne = "NVIDIA A100-SXM4-80GB, 580.95.05, 81920 MiB" if quoi == "carte_sxm4" else "NVIDIA A100-PCIE-40GB, 580.95.05, 40960 MiB"
    (j.parent / "nvidia-smi.txt").write_text(f"name, driver_version, memory.total [MiB]\n{ligne}\n", encoding="utf-8")
    empreintes_des_traces()
else:
    raise SystemExit(f"artefact inconnu : {quoi}")
print(f"artefact {quoi} préparé")
