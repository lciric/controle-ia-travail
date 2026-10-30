"""Assemble le manifeste d'ensemble de la v8 depuis les manifestes par passage (GD5-03) : rien n'est recopié à la main.
Pour chaque passage : le manifeste écrit par le script est relu ; la sortie, le journal et le manifeste sont recomptés
(empreintes) ; le commit **déclaré** (GD7-09 : aucune lecture git) du manifeste est comparé à celui que porte la sortie elle-même et au texte déclaré attendu ;
l'empreinte du script est comparée à celle du fichier du dossier. Toute divergence est affichée, n'écrit aucun manifeste et fait échouer l'assemblage (code 1).
v8 : le manifeste d'ensemble porte aussi les graines maîtresses (R9), les versions de python et de numpy (une seule version exigée), la liste des fichiers
du dossier avec leurs empreintes, le résultat (`conforme`) de chaque vérification, et l'absence de tout `__pycache__`.

Usage : python3 -I -B assembler-manifeste-v8.py DOSSIER SORTIE.json
"""

import glob
import hashlib
import json
import os
import sys

DOSSIER, SORTIE = os.path.abspath(sys.argv[1]), sys.argv[2]
PREF = "simulation-puissance-garde-delta-v8-sortie-"
PREF_C = "simulation-puissance-garde-delta-v8-complement-"  # compléments : incertitude de graine de n80 (lancer-complements-v8.sh)
RAPPORT = "rapport-puissance-garde-delta-v8.md"  # écrit après le manifeste (il en cite l'empreinte) : exclu de la liste
COMMIT_ATTENDU = "non lu : aucune commande git permise à la lignée conv-audit pour cette tâche, dépôt non interrogé (GD7-09)"
SCRIPT = os.path.join(DOSSIER, "simulation-puissance-garde-delta-v8.py")


def sha(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


empreinte_script = sha(SCRIPT)
passages, divergences = {}, []
for m in sorted(glob.glob(os.path.join(DOSSIER, "manifeste-" + PREF + "*.json")) + glob.glob(os.path.join(DOSSIER, "manifeste-" + PREF_C + "*.json"))):
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
         "sans_n80": bool(sortie["reglages"].get("sans_n80")), "fichiers": man["fichiers"],
         "environnement": man["environnement"], "derivation_des_graines": man["graines"]["derivation"],
         "graines_derivees_par_cellule": man["graines"]["graines_derivees_par_cellule"],
         "echelle_dispersion": sortie["reglages"].get("echelle_dispersion"), "paires_K_h_K_s": sortie["reglages"].get("paires_K_h_K_s")}
    if p["commit"] != p["commit_porte_par_la_sortie"] or p["etat_du_script"] != p["etat_porte_par_la_sortie"]:
        divergences.append(f"{nom} : commit déclaré ou état du manifeste différent de celui de la sortie")
    if p["commit"] != COMMIT_ATTENDU:
        divergences.append(f"{nom} : commit déclaré {p['commit']!r} différent du texte attendu")
    if not p["etat_du_script"].startswith("non lu"):
        divergences.append(f"{nom} : état du script {p['etat_du_script']!r} (la v8 ne lit rien)")
    if p["script_sha256"] != empreinte_script or p["script_sha256_porte_par_la_sortie"] != empreinte_script:
        divergences.append(f"{nom} : empreinte du script différente de celle du fichier du dossier")
    for f, h in man["fichiers"].items():
        if sha(os.path.join(DOSSIER, f)) != h:
            divergences.append(f"{nom} : empreinte de {f} différente de celle du manifeste")
    if sortie["version"] != "simulation-puissance-garde-delta-v8":
        divergences.append(f"{nom} : version {sortie['version']}")
    passages[nom] = p

commits = sorted({p["commit"] for p in passages.values()})
verifications = {}
for f in sorted(os.listdir(DOSSIER)):
    if f.startswith(("verif-", "essais-")) and f.endswith("-sortie.json"):
        v = json.load(open(os.path.join(DOSSIER, f), encoding="utf-8"))
        verifications[f] = {"sha256": sha(os.path.join(DOSSIER, f)), "conforme": v.get("conforme", v.get("non_conformes") == [])}
        if not verifications[f]["conforme"]:
            divergences.append(f"{f} : vérification non conforme")
pycache = [os.path.join(r, d) for r, ds, _ in os.walk(DOSSIER) for d in ds if d == "__pycache__"]
if pycache:
    divergences.append(f"__pycache__ présent : {pycache}")
auxiliaires = {}
for f in sorted(os.listdir(DOSSIER)):
    c = os.path.join(DOSSIER, f)
    if f.endswith(".sha256") or not os.path.isfile(c) or f == os.path.basename(SORTIE):
        continue
    if f.startswith((PREF, PREF_C, "manifeste-" + PREF, "manifeste-" + PREF_C)) or f == RAPPORT:
        continue
    auxiliaires[f] = sha(c)
versions = sorted({(p["environnement"]["python"], p["environnement"]["numpy"]) for p in passages.values()})
manifeste = {
    "version": "manifeste-puissance-garde-delta-v8",
    "ecrit_par": "assembler-manifeste-v8.py, depuis les manifestes par passage (GD5-03)",
    "statut": "exploratoire, processeur seul, sans dépense, non préenregistré, non opposable ; lois synthétiques seulement ; "
              "répond à la contre-lecture GD7 de la v7 (gardée, R12) ; non relu par une autre main (R2)",
    "aucune_commande_git": "le commit est celui de --commit-declare, jamais lu (GD7-09)", "commit_declare_attendu": COMMIT_ATTENDU,
    "verifications": verifications, "pycache_present": bool(pycache),
    "script": {"fichier": os.path.basename(SCRIPT), "sha256": empreinte_script},
    "versions_python_numpy": [{"python": a, "numpy": b} for a, b in versions], "une_seule_version": len(versions) == 1,
    "graines_maitresses": sorted({p["graine_maitresse"] for p in passages.values()}),
    "passages_nombre": len(passages), "passages_principaux_nombre": sum(1 for n in passages if "-sortie-" in n), "passages_complements_nombre": sum(1 for n in passages if "-complement-" in n), "commits_distincts_au_lancement": commits,
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
