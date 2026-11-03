"""Barrage de la reprise du tour Colognese et Ward Q2 sans Argon (3 novembre 2026, session fille ; mot de session-depot ≈ 12:15 UTC).
Sans appel ni écriture : charge collisionneur_v9.py comme module ; sa fonction `verifier` (sans la régénération de etat.md de la
sous-commande) et `cellule_valide` sur les quinze cellules de l'étage III. Exige : aucun problème ; exactement les 7 cellules valides
attendues ; les trois cellules C consignées « absence_acceptee » au journal ; à jouer seulement E3-T2-critique-croisee-E puis E3-T3 A, B,
D, E ; aucune au statut REFUS. Sinon code 2. Usage : python -I -B barrage_reprise_cw_v1.py COLLISIONNEUR_V9 DOSSIER_RUN"""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("collisionneur_v9", sys.argv[1]); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
d = sys.argv[2]
ids = [cv.id_cellule(t, l) for t in cv.ORDRE_ETAGE[3] for l in cv.LETTRES]
valides = sorted(c for c in ids if cv.cellule_valide(d, c))
attendues = sorted(["E3-T1-conception-A", "E3-T1-conception-B", "E3-T1-conception-D", "E3-T1-conception-E",
                    "E3-T2-critique-croisee-A", "E3-T2-critique-croisee-B", "E3-T2-critique-croisee-D"])
absences_c = ["E3-T1-conception-C", "E3-T2-critique-croisee-C", "E3-T3-reponse-C"]
consignees = {e["cellule"] for e in cv.lire_journal(d) if e.get("decision") == "absence_acceptee"}
a_jouer = sorted(set(ids) - set(valides) - set(absences_c))
attendu_jouer = sorted(["E3-T2-critique-croisee-E", "E3-T3-reponse-A", "E3-T3-reponse-B", "E3-T3-reponse-D", "E3-T3-reponse-E"])
refus = [c for c in a_jouer if cv.statut_courant(d, c) == "REFUS"]
problemes = cv.verifier(d)
print(f"barrage : {len(valides)} valides ; absences C consignées {sorted(consignees & set(absences_c))} ; à jouer {a_jouer} ; problèmes {len(problemes)} ; refus {refus}", flush=True)
for p in problemes:
    print("PROBLÈME :", p)
if problemes or valides != attendues or not set(absences_c) <= consignees or a_jouer != attendu_jouer or refus:
    sys.stderr.write("barrage : refus, la reprise ne joue que E3-T2-critique-croisee-E puis E3-T3 A, B, D, E\n"); sys.exit(2)
print("barrage : conforme", flush=True)
