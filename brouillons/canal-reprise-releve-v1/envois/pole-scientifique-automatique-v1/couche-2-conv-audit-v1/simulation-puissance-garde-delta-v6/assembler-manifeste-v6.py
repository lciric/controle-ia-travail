"""Assemble le manifeste d'ensemble de la v6 depuis les manifestes par passage (GD5-03) : rien n'est recopié à la main.
Pour chaque passage : le manifeste écrit par le script est relu ; la sortie, le journal et le manifeste sont recomptés
(empreintes) ; le commit et l'état git du manifeste sont comparés à ceux que porte la sortie elle-même ; l'empreinte du script est
comparée à celle du fichier du dossier. Toute divergence est affichée, n'écrit aucun manifeste et fait échouer l'assemblage (code 1).

Usage : python3 -I -B assembler-manifeste-v6.py DOSSIER SORTIE.json
"""

import glob
import hashlib
import json
import os
import sys

DOSSIER, SORTIE = os.path.abspath(sys.argv[1]), sys.argv[2]
PREF = "simulation-puissance-garde-delta-v6-sortie-"
SCRIPT = os.path.join(DOSSIER, "simulation-puissance-garde-delta-v6.py")


def sha(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


empreinte_script = sha(SCRIPT)
passages, divergences = {}, []
for m in sorted(glob.glob(os.path.join(DOSSIER, "manifeste-" + PREF + "*.json"))):
    man = json.load(open(m, encoding="utf-8"))
    nom = man["passage"]
    sortie_json = os.path.join(DOSSIER, nom + ".json")
    sortie = json.load(open(sortie_json, encoding="utf-8"))
    p = {"manifeste": os.path.basename(m), "manifeste_sha256": sha(m), "commande": man["commande"]["ligne"],
         "debut_utc": man["date_utc_debut"], "fin_utc": man["date_utc_fin"], "duree_s": man["duree_s"],
         "repetitions": sortie["reglages"]["repetitions"], "graine_maitresse": man["graines"]["graine_maitresse"],
         "commit": man["script"]["commit"], "etat_du_script": man["script"]["etat_du_script"],
         "commit_porte_par_la_sortie": sortie.get("commit"), "etat_porte_par_la_sortie": sortie.get("etat_du_script"),
         "script_sha256": man["script"]["sha256"], "script_sha256_porte_par_la_sortie": sortie["script_sha256"],
         "sans_n80": bool(sortie["reglages"].get("sans_n80")), "fichiers": man["fichiers"]}
    if p["commit"] != p["commit_porte_par_la_sortie"] or p["etat_du_script"] != p["etat_porte_par_la_sortie"]:
        divergences.append(f"{nom} : commit ou état du manifeste différent de celui de la sortie")
    if not p["commit"]:
        divergences.append(f"{nom} : commit absent ({p['etat_du_script']})")
    if p["script_sha256"] != empreinte_script or p["script_sha256_porte_par_la_sortie"] != empreinte_script:
        divergences.append(f"{nom} : empreinte du script différente de celle du fichier du dossier")
    for f, h in man["fichiers"].items():
        if sha(os.path.join(DOSSIER, f)) != h:
            divergences.append(f"{nom} : empreinte de {f} différente de celle du manifeste")
    if sortie["version"] != "simulation-puissance-garde-delta-v6":
        divergences.append(f"{nom} : version {sortie['version']}")
    passages[nom] = p

commits = sorted({p["commit"] for p in passages.values()})
auxiliaires = {}
for f in sorted(os.listdir(DOSSIER)):
    c = os.path.join(DOSSIER, f)
    if f.endswith(".sha256") or not os.path.isfile(c) or f == os.path.basename(SORTIE):
        continue
    if f.startswith(PREF) or f.startswith("manifeste-" + PREF):
        continue
    auxiliaires[f] = sha(c)
manifeste = {
    "version": "manifeste-puissance-garde-delta-v6",
    "ecrit_par": "assembler-manifeste-v6.py, depuis les manifestes par passage (GD5-03)",
    "statut": "exploratoire, processeur seul, sans dépense, non préenregistré, non opposable ; lois synthétiques seulement ; "
              "remplace la v5 (gardée, R12) ; non relu par une autre main (R2)",
    "script": {"fichier": os.path.basename(SCRIPT), "sha256": empreinte_script},
    "passages_nombre": len(passages), "commits_distincts_au_lancement": commits,
    "un_seul_commit": len(commits) == 1,
    "passages": passages,
    "fichiers_du_dossier_hors_passages": auxiliaires,
    "divergences": divergences,
}
if not divergences:  # rien n'est écrit si une divergence existe (R5 : aucun manifeste d'ensemble qui masque un écart) ; R12 : mode « x »
    with open(SORTIE, "x", encoding="utf-8") as f:
        json.dump(manifeste, f, indent=1, ensure_ascii=False)
        f.write("\n")
print(f"{len(passages)} passages ; commits distincts : {len(commits)} ; divergences : {len(divergences)}")
for d in divergences:
    print("DIVERGENCE :", d)
sys.exit(1 if divergences else 0)
