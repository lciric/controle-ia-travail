"""Rejoue chaque extrait de code cité sur le fichier, le commit et les lignes indiqués.
Entrée : liste JSON d'objets {piece, depot, commit, chemin, ligne_debut, ligne_fin, empreinte_fichier, extrait}.
`depot` est le nom du dossier du clone sous <racine des clones>. Contrôles, tous exigés :
(1) le clone est au commit dit (git rev-parse HEAD) ; (2) le sha256 du fichier est l'empreinte dite ;
(3) l'extrait, espaces blancs réduits à une espace, casse et ponctuation gardées, se trouve dans les lignes
[ligne_debut, ligne_fin] du fichier, réduites de même. Aucune autre normalisation.
Usage : python3 -I verifier_extraits_code_o4_v1.py <racine des clones> <extraits.json> <sortie.json>
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

def reduire(s):
    return re.sub(r"\s+", " ", s).strip()

racine, extraits, sortie = Path(sys.argv[1]), json.load(open(sys.argv[2], encoding="utf-8")), sys.argv[3]
tetes, res = {}, []
for e in extraits:
    clone = racine / e["depot"]
    if clone not in tetes:
        tetes[clone] = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"],
                                      capture_output=True, text=True).stdout.strip()
    f = clone / e["chemin"]
    octets = f.read_bytes() if f.is_file() else b""
    h = hashlib.sha256(octets).hexdigest() if f.is_file() else None
    lignes = octets.decode("utf-8", errors="replace").splitlines()
    d, fin = e["ligne_debut"], e["ligne_fin"]
    bloc = reduire(" ".join(lignes[d - 1:fin])) if 1 <= d <= fin <= len(lignes) else ""
    q = reduire(e["extrait"])
    r = {**e, "commit_du_clone": tetes[clone], "commit_conforme": tetes[clone] == e["commit"],
         "sha256_fichier_recalcule": h, "empreinte_conforme": h == e["empreinte_fichier"],
         "trouve_dans_les_lignes": bool(q) and q in bloc}
    res.append(r)
json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ok = sum(r["commit_conforme"] and r["empreinte_conforme"] and r["trouve_dans_les_lignes"] for r in res)
print(f"{ok} sur {len(res)} extraits trouvés dans les lignes dites, commit et empreinte conformes")
for r in res:
    if not (r["commit_conforme"] and r["empreinte_conforme"] and r["trouve_dans_les_lignes"]):
        print("ÉCHEC", r["piece"], r["chemin"], r["ligne_debut"], r["ligne_fin"], r["extrait"][:80])
sys.exit(0 if ok == len(res) else 1)
