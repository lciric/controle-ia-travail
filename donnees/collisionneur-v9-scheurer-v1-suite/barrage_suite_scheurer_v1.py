"""Barrage de la suite du tour Scheurer sans Argon ni Opus (3 novembre 2026, session fille ; décision de Lazar « (a) Continuer sans
l'espèce qui a refusé », rapportée par conv-audit n° 421, ordre de session-depot ≈ 13:10 UTC ; gabarit barrage_reprise_cw_v1.py, 04f304a3…).
Sans appel ni écriture : charge collisionneur_v9.py comme module ; sa fonction `verifier` et `cellule_valide` sur les quinze cellules
de l'étage III. Exige : aucun problème ; exactement les 3 cellules valides attendues (E3-T1 A, D, E) ; les trois cellules C consignées
« absence_acceptee » ; E3-T1-conception-B au statut REFUS (la seule) ; E3-T2-B et E3-T3-B jamais lancées ; à jouer seulement E3-T2 et
E3-T3 de A, D, E. Sinon code 2. Usage : python -I -B barrage_suite_scheurer_v1.py COLLISIONNEUR_V9 DOSSIER_RUN"""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("collisionneur_v9", sys.argv[1]); cv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cv)
d = sys.argv[2]
ids = [cv.id_cellule(t, l) for t in cv.ORDRE_ETAGE[3] for l in cv.LETTRES]
valides = sorted(c for c in ids if cv.cellule_valide(d, c))
attendues = ["E3-T1-conception-A", "E3-T1-conception-D", "E3-T1-conception-E"]
absences_c = ["E3-T1-conception-C", "E3-T2-critique-croisee-C", "E3-T3-reponse-C"]
cellules_b = ["E3-T1-conception-B", "E3-T2-critique-croisee-B", "E3-T3-reponse-B"]
consignees = {e["cellule"] for e in cv.lire_journal(d) if e.get("decision") == "absence_acceptee"}
statuts_b = {c: cv.statut_courant(d, c) for c in cellules_b}
a_jouer = sorted(set(ids) - set(valides) - set(absences_c) - set(cellules_b))
attendu_jouer = sorted(f"{t}-{cv.TOURS[t]['nom']}-{l}" for t in ("E3-T2", "E3-T3") for l in "ADE")
refus = sorted(c for c in ids if cv.statut_courant(d, c) == "REFUS")
problemes = cv.verifier(d)
print(f"barrage : {len(valides)} valides ; absences C consignées {sorted(consignees & set(absences_c))} ; statuts B {statuts_b} ; à jouer {a_jouer} ; problèmes {len(problemes)} ; refus {refus}", flush=True)
for p in problemes:
    print("PROBLÈME :", p)
ok_b = statuts_b == {"E3-T1-conception-B": "REFUS", "E3-T2-critique-croisee-B": "jamais lancée", "E3-T3-reponse-B": "jamais lancée"}
if problemes or valides != attendues or not set(absences_c) <= consignees or not ok_b or a_jouer != attendu_jouer or refus != ["E3-T1-conception-B"]:
    sys.stderr.write("barrage : refus, la suite ne joue que E3-T2 et E3-T3 de A, D, E (B refusée en E3-T1, C absente)\n"); sys.exit(2)
print("barrage : conforme", flush=True)
