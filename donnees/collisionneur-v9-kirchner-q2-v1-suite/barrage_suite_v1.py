"""Barrage (a) de la suite du tour v9 (3 novembre 2026, session fille ; ordre `ordre-fille-collisionneur-v9-suite-v1.md`, 9be11cba…).
Sans appel réseau ni écriture : charge collisionneur_v9.py comme module et applique sa fonction `verifier` (la même que la
sous-commande « verifier », sans la régénération de etat.md que fait la sous-commande) et `cellule_valide` sur les quinze cellules
de l'étage III. Exige : aucun problème ; exactement 13 cellules valides ; non valides = {E3-T3-reponse-D, E3-T3-reponse-E}, aucune
au statut REFUS. Sinon code 2. Usage : python -I -B barrage_suite_v1.py COLLISIONNEUR_V9 DOSSIER_RUN"""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("collisionneur_v9", sys.argv[1]); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
d = sys.argv[2]
ids = [cv.id_cellule(t, l) for t in cv.ORDRE_ETAGE[3] for l in cv.LETTRES]
valides = [c for c in ids if cv.cellule_valide(d, c)]
non = sorted(set(ids) - set(valides))
problemes = cv.verifier(d)
attendu = ["E3-T3-reponse-D", "E3-T3-reponse-E"]
refus = [c for c in non if cv.statut_courant(d, c) == "REFUS"]
print(f"barrage (a) : {len(valides)} cellules valides ; non valides {non} ; problèmes {len(problemes)} ; refus {refus}", flush=True)
for p in problemes:
    print("PROBLÈME :", p)
if problemes or len(valides) != 13 or non != attendu or refus:
    sys.stderr.write("barrage (a) : refus, la suite ne joue que E3-T3-reponse-D et E3-T3-reponse-E\n"); sys.exit(2)
print("barrage (a) : conforme", flush=True)
