"""Assemble les faits du tour « brainstorm instance neuve » (collisionneur v9) à partir de deux clones publics.
Usage : python3 -I assembler_faits_brainstorm_v1.py DEPOT_LOI DEPOT_CONSTRUIT SORTIE"""
import glob, hashlib, json, os, subprocess, sys
loi, cons, sortie = sys.argv[1:4]
def commit(d): return subprocess.run(["git", "-C", d, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
blocs, liste = [], []
def ajouter(depot, nom, chemin_rel, texte=None, note=""):
    p = os.path.join(depot, chemin_rel)
    if texte is None:
        texte = open(p, encoding="utf-8").read()
        h = sha(p)
    else:
        h = hashlib.sha256(texte.encode()).hexdigest()
    liste.append(f"- {nom}:{chemin_rel} ({len(texte)} caractères, sha256 {h[:16]}…){note}")
    blocs.append(f"<<<DÉBUT FICHIER {nom}:{chemin_rel} sha256={h}{note}>>>\n{texte}\n<<<FIN FICHIER {nom}:{chemin_rel}>>>")
L, C = "sycophancy-psychophysical-law", "sycophancy-construct-validity"
ajouter(loi, L, "README.md")
for f in sorted(glob.glob(os.path.join(loi, "preregistrations", "*.md"))):
    ajouter(loi, L, os.path.relpath(f, loi))
for f in sorted(glob.glob(os.path.join(loi, "results", "*", "README.md"))) + sorted(glob.glob(os.path.join(loi, "results", "*", "*.txt"))):
    ajouter(loi, L, os.path.relpath(f, loi))
for f in ("data/c2a_results.json", "data/c2b_results.json"):
    ajouter(loi, L, f)
REGLE = "échantillon : items 0, 5, 10, 15, 20, 25 (un sur cinq) × les deux conditions × graine k = 0, ordre du fichier"
for f in ("data/c2a_generations.json", "data/c2b_generations.json"):
    d = json.load(open(os.path.join(loi, f), encoding="utf-8"))
    rows = [r for r in d["rows"] if int(r["item"]) % 5 == 0 and str(r["k"]) == "0"]
    ech = {"meta": d["meta"], "regle_echantillon": REGLE, "rows_retenues": len(rows), "rows_total": len(d["rows"]), "rows": rows}
    ajouter(loi, L, f, texte=json.dumps(ech, ensure_ascii=False, indent=1), note=f" [ÉCHANTILLON : {len(rows)} sur {len(d['rows'])} lignes ; {REGLE}]")
ajouter(cons, C, "README.md")
for f in sorted(glob.glob(os.path.join(cons, "results", "*.json"))):
    if os.path.getsize(f) <= 15000:
        ajouter(cons, C, os.path.relpath(f, cons))
entete = ("pas de web, pas d'exécution de code ; nouveauté : non cherché\n\n"
          "# Faits du tour « brainstorm instance neuve » (collisionneur v9)\n\n"
          "Ces faits remplacent la lecture directe demandée par le brief : les espèces n'ont ni accès au web ni exécution de code. "
          "Ils sont une SÉLECTION de fichiers publics, clonés par git, recopiés tels quels (aucun texte privé, aucune interprétation "
          "de l'équipe ajoutée) :\n"
          f"- dépôt public github.com/lciric/{L}, étiquette v2026.11.4, commit {commit(loi)} ;\n"
          f"- dépôt public github.com/lciric/{C}, commit {commit(cons)}.\n\n"
          "Règles de sélection : les deux README ; preregistrations/*.md (premier niveau) ; résumés de results/ — pour le premier dépôt, "
          "results/*/README.md et les sorties texte results/*/*.txt ; pour le second, les fichiers results/*.json de 15 000 octets au "
          "plus ; data/c2a_results.json et data/c2b_results.json en entier ; data/c2a_generations.json et data/c2b_generations.json en "
          f"échantillon borné ({REGLE}). NON fournis : le reste de data/, results/*/*.json du premier dépôt, le code (code/*.py), "
          "R5_materials/, les pages des mentors (pivotal-research.org), arXiv et Semantic Scholar. Toute affirmation qui demanderait "
          "ces sources doit être déclarée « non vérifié ».\n\n## Liste des fichiers\n")
open(sortie, "x", encoding="utf-8").write(entete + "\n".join(liste) + "\n\n" + "\n\n".join(blocs) + "\n")
print(len(liste), "fichiers")
