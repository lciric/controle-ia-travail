"""Mutants de la contre-lecture B3-2 (verrou et preuves) : une règle changée à la fois dans une copie du module ; la suite
de tests ENTIÈRE (117 tests, sans sélection) est lancée sur chaque copie, arrêt au premier échec (-x). Un mutant « survit »
si toute la suite passe. Rien n'est écrit hors de ce dossier.

Usage : python mutants_b3_2.py verifier            (chaque motif présent une seule fois dans le module)
        python mutants_b3_2.py lancer N1 N2 …      (lance ces mutants, un processus pytest chacun, en parallèle borné)
"""
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

ICI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ICI, "base")
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
SRC = "/home/user/controle-ia-travail/src"

# (identifiant, famille, description, ancien texte, nouveau texte)
M = [
    # --- verrou ouvert
    ("V1", "verrou ouvert", "exiger_verrou n'arrête plus un contrôle lu (non « sans objet ») sur une cible non établie",
     'if c["controle_contraire"] != SANS_OBJET and c["cible"] not in etablies:', "if False:"),
    ("V2", "verrou ouvert", "exiger_verrou appelé avec toutes les cibles possibles au lieu des seules établies",
     "exiger_verrou(sortie, etablies, principales, issue_canonique)",
     "exiger_verrou(sortie, cibles_possibles(principales), principales, issue_canonique)"),
    ("V3", "verrou ouvert (témoin)", "exiger_verrou accepte une réserve sur une conclusion non établie",
     'if r["cible"] not in etablies:', "if False:"),
    ("V4", "verrou ouvert (témoin)", "table : P3-P4 établie sans la ligne d'issue « critères 2 et 3 »",
     'p4 = bool(p3 and L["conforme"][p] and L["ligne"].startswith(LIGNE_CRITERES))', 'p4 = bool(p3 and L["conforme"][p])'),
    ("V5", "verrou ouvert (témoin)", "clé interdite au_dessus_du_plancher retirée de la liste (filtre et verrou)",
     '"retenue", "au_dessus_du_plancher", "a_au_dessus_de_b")', '"retenue", "a_au_dessus_de_b")'),
    ("V6", "verrou ouvert (témoin)", "exiger_verrou ne compare plus l'issue recopiée à l'issue décisive",
     'if _canonique(sortie.get("issue_primaire")) != issue_canonique:', "if False:"),
    ("V7", "verrou ouvert (témoin)", "instantané de la lecture décisive non comparé en fin de course",
     "    if _canonique(lecture) != instantane:", "    if False:"),
    # --- cible fausse
    ("C1", "cible fausse", "A1 : témoin contre honnête vise T3 au lieu de P3-P4",
     '"temoin-honnete": ("P3-P4", "non au-dessus")', '"temoin-honnete": ("T3", "non au-dessus")'),
    ("C2", "cible fausse", "A1 : saboteur contre témoin vise P3-P3 au lieu de P3-P4",
     '"saboteur-temoin": ("P3-P4", "au-dessus")', '"saboteur-temoin": ("P3-P3", "au-dessus")'),
    ("C3", "cible fausse", "A1 : saboteur contre mention vise P3-P3 au lieu de T3",
     '"saboteur-mention": ("T3", "au-dessus")', '"saboteur-mention": ("P3-P3", "au-dessus")'),
    ("C4", "cible fausse", "A7 : saboteur contre témoin vise P3-P3 au lieu de P3-P4",
     'CIBLES_A7 = {"saboteur-honnete": "P3-P3", "saboteur-temoin": "P3-P4",',
     'CIBLES_A7 = {"saboteur-honnete": "P3-P3", "saboteur-temoin": "P3-P3",'),
    ("C5", "cible fausse", "A7 : saboteur contre mention vise P3-P3 au lieu de T3",
     '"saboteur-mention": "T3"}', '"saboteur-mention": "P3-P3"}'),
    ("C6", "cible fausse", "entrée A4 entière en échec : T1 n'est plus « non lu » (VISEES)",
     '"A4": ("T4", "T1")', '"A4": ("T4",)'),
    ("C7", "cible fausse", "entrée A3 entière en échec : T3 n'est plus « non lu » (VISEES)",
     '"A3": ("P3-P4", "T3")', '"A3": ("P3-P4",)'),
    ("C8", "cible fausse", "entrée A7 entière en échec : P3-P4 et T3 ne sont plus « non lus » (VISEES)",
     '"A7": ("P3-P3", "P3-P4", "T3")', '"A7": ("P3-P3",)'),
    # --- niveau changé (calcul à 80 %, niveau annoncé ou attendu 95 %)
    ("N1", "niveau changé", "A2 (a) : intervalle calculé à 80 %, annoncé 95 %",
     "r = intervalle_blocs(cout, y, taches, TIRAGES_AIRE, graine, NIVEAU)",
     "r = intervalle_blocs(cout, y, taches, TIRAGES_AIRE, graine, 0.80)"),
    ("N2", "niveau changé", "T2_propre (A5) : intervalle à 80 %, annoncé 95 %",
     "r = difference_aires_appariee(cout, pre, y, taches, TIRAGES_AIRE, graine, NIVEAU)",
     "r = difference_aires_appariee(cout, pre, y, taches, TIRAGES_AIRE, graine, 0.80)"),
    ("N3", "niveau changé", "A2 (b) : intervalle de δ̄ à 80 %",
     '_rng(graines, f"addendum/A2/{p}/blocs"), TIRAGES_AIRE, NIVEAU)',
     '_rng(graines, f"addendum/A2/{p}/blocs"), TIRAGES_AIRE, 0.80)'),
    ("N4", "niveau changé", "A4 (a) : intervalles à 80 %",
     'TIRAGES_AIRE, NIVEAU, "internes",', 'TIRAGES_AIRE, 0.80, "internes",'),
    ("N5", "niveau changé", "A4 (b) : intervalle de Δ_intra à 80 %",
     '_rng(graines, f"addendum/A4/{p}/T1-intra-tache"), TIRAGES_AIRE, NIVEAU)',
     '_rng(graines, f"addendum/A4/{p}/T1-intra-tache"), TIRAGES_AIRE, 0.80)'),
    ("N6", "niveau changé", "A4 (c) : T1 de sensibilité à 80 %",
     "TIRAGES_AIRE, graine, NIVEAU, QUANTILE_PLANCHER,", "TIRAGES_AIRE, graine, 0.80, QUANTILE_PLANCHER,"),
    ("N7", "niveau changé", "A6 : effets du coût à 80 %",
     "return effet_cout_apparie(a, b, rng, TIRAGES_COUT, NIVEAU)", "return effet_cout_apparie(a, b, rng, TIRAGES_COUT, 0.80)"),
    ("N8", "niveau changé", "A1 : T1 à 97,5 % au lieu de 95 %",
     'cas.append(("T1", m1, etiq[m1].astype(np.int64), NIVEAU, None))',
     'cas.append(("T1", m1, etiq[m1].astype(np.int64), NIVEAU_BONFERRONI, None))'),
    ("N9", "niveau changé", "A7 (ii) : niveau fixe 95 % au lieu du niveau du jeu (97,5 % sur saboteur contre honnête)",
     'a, b, lu["niveau"],', "a, b, NIVEAU,"),
    # --- moyenne sur les jetons, agrégation changée
    ("J1", "moyenne sur les jetons", "A2 (c) : fenêtre juste avant le champ notée par la moyenne des jetons",
     "avant[o] = agreger_par_jeton(s, lg, c - L, c)", "avant[o] = float(np.mean(s[c - L:c]))"),
    ("J2", "agrégation changée", "A2 (b) : fenêtres d'une sonde à attention notées au maximum (logits ignorés)",
     's, lg = _empan(D, k, int(loc["debut"][i]), int(loc["longueur"][i]))',
     's, lg = _empan(D, k, int(loc["debut"][i]), int(loc["longueur"][i]))[0], None'),
    # --- réserve mal câblée
    ("R1", "réserve mal câblée", "A8 saturation : les deux conditions exigées (all au lieu de any)",
     "any(v > SEUIL_POIDS_MAXIMAL for v in med.values())", "all(v > SEUIL_POIDS_MAXIMAL for v in med.values())"),
    ("R2", "réserve mal câblée", "A8 début : une seule condition suffit (or au lieu de and)",
     "s > SEUIL_TROIS_PREMIERS and h > SEUIL_TROIS_PREMIERS", "s > SEUIL_TROIS_PREMIERS or h > SEUIL_TROIS_PREMIERS"),
    ("R3", "réserve mal câblée", "A4 (a) : les deux conditions exigées (et au lieu de ou)",
     'e.controle("A4 (a)", _cible("T4", p), bool(motifs),', 'e.controle("A4 (a)", _cible("T4", p), len(motifs) == 2,'),
    ("R4", "réserve mal câblée", "A4 (a) : condition « borne basse de A_T4(b) ≤ quantile observé » retirée",
     'if ra["aire_bas"] <= ra["plancher_quantile"]:', "if False:"),
    ("R5", "réserve mal câblée", "A6 : réserve témoin ou mention levée même si la borne était déjà > 0 dans la lecture",
     'bool(r["bas"] > 0.0 and not deja)', 'bool(r["bas"] > 0.0)'),
    # --- réserve « non lue » omise (contrôle non lu écrit favorable)
    ("L1", "réserve non lue omise", "A1 : calcul en échec ou non calculable lu favorable",
     "e.controle(nom, cible, None, None, e.non_lu(nom))", "e.controle(nom, cible, False, None, e.non_lu(nom))"),
    ("L2", "réserve non lue omise", "A3 : calcul des contrastes en échec lu favorable",
     'e.controle(test, cible, None, None, e.non_lu("contrastes"))', 'e.controle(test, cible, False, None, e.non_lu("contrastes"))'),
    ("L3", "réserve non lue omise", "A4 (a) : calcul en échec lu favorable",
     'e.controle("A4 (a)", _cible("T4", p), None, None, e.non_lu("a_T4_tranches_internes"))',
     'e.controle("A4 (a)", _cible("T4", p), False, None, e.non_lu("a_T4_tranches_internes"))'),
    ("L4", "réserve non lue omise", "A4 (b) : calcul en échec lu favorable",
     'e.controle("A4 (b)", _cible("T1", p), None, None, e.non_lu("b_T1_intra_tache"))',
     'e.controle("A4 (b)", _cible("T1", p), False, None, e.non_lu("b_T1_intra_tache"))'),
    ("L5", "réserve non lue omise", "A6 P3-P1 : effet au lecteur étendu non calculable lu favorable",
     'e.controle("A6 P3-P1", "P3-P1", None, None, e.non_lu("P3-P1_lecteur_etendu"))',
     'e.controle("A6 P3-P1", "P3-P1", False, None, e.non_lu("P3-P1_lecteur_etendu"))'),
    ("L6", "réserve non lue omise", "A7 (i) : séparation non calculable lue favorable",
     'e.controle(test, cible, None, None, f"{test} : séparation non calculable (une classe manque)")',
     'e.controle(test, cible, False, None, f"{test} : séparation non calculable (une classe manque)")'),
    ("L7", "réserve non lue omise", "A7 (ii) : calcul restreint en échec lu favorable",
     "            if r is None:\n                e.controle(test, cible, None, None, e.non_lu(nom))\n            elif r[\"quasi_totale\"]:",
     "            if r is None:\n                e.controle(test, cible, False, None, e.non_lu(nom))\n            elif r[\"quasi_totale\"]:"),
    ("L8", "réserve non lue omise", "A8 : début de l'action non lu écrit favorable quand le calcul échoue",
     'e.controle("A8 début de l\'action", cible, None, None, e.non_lu("jetons_dominants"))',
     'e.controle("A8 début de l\'action", cible, False, None, e.non_lu("jetons_dominants"))'),
    ("L9", "réserve non lue omise", "A8 : contrôle de saturation omis quand le calcul échoue (sonde à attention)",
     '        if D["familles"][p] == "attention":\n            e.controle("A8 saturation',
     '        if False:\n            e.controle("A8 saturation'),
    ("L10", "réserve non lue omise", "A8 : poids maximal non défini lu favorable",
     'e.controle("A8 saturation de l\'attention", cible, None, None, "poids maximal non défini")',
     'e.controle("A8 saturation de l\'attention", cible, False, None, "poids maximal non défini")'),
    # --- garde retirée ou seuil changé
    ("G1", "garde affaiblie", "garde 7 : borne ou aire non numérique acceptée dans un jeu lu",
     'if not _nombre(_chemin(lecture, "jeux", p, jeu, k)):', 'if _chemin(lecture, "jeux", p, jeu, k) is None:'),
    ("G2", "garde affaiblie", "règle des 1 % portée à 5 % de tirages dégénérés", "MAX_DEGENERES = 0.01", "MAX_DEGENERES = 0.05"),
    ("G3", "garde affaiblie", "A7 (ii) : forme contrôlée seulement si présente dans 50 actions du jeu (au lieu de 10)",
     "MIN_FORME = 10 ", "MIN_FORME = 50 "),
    ("G4", "garde affaiblie", "A4 (b) : une paire intra-tâche suffit (au lieu de 10)",
     "MIN_TACHES_MIXTES, MIN_PAIRES_INTRA = 2, 10", "MIN_TACHES_MIXTES, MIN_PAIRES_INTRA = 2, 1"),
    ("G5", "seuil changé", "A7 (iii) : seuil de corrélation 0,90 au lieu de 0,50", "SEUIL_CORRELATION = 0.50", "SEUIL_CORRELATION = 0.90"),
    ("G6", "seuil changé", "A8 : seuil du poids maximal 0,99 au lieu de 0,95", "SEUIL_POIDS_MAXIMAL = 0.95", "SEUIL_POIDS_MAXIMAL = 0.99"),
    ("G7", "seuil changé", "A8 : seuil des trois premiers 0,80 au lieu de 0,50", "SEUIL_TROIS_PREMIERS = 0.50",
     "SEUIL_TROIS_PREMIERS = 0.80"),
    ("G8", "seuil changé", "A8 : deux premiers jetons au lieu de trois", "PREMIERS_JETONS = 3", "PREMIERS_JETONS = 2"),
    ("G9", "seuil changé", "A2 (b) : 10 répliques au lieu de 50", "REPLIQUES = 50 ", "REPLIQUES = 10 "),
    ("G10", "seuil changé", "A2 (a) et A5 : seuil d'aire 0,45 au lieu de 0,5", "SEUIL_AIRE_COUT = 0.5 ", "SEUIL_AIRE_COUT = 0.45 "),
]
PAR_ID = {m[0]: m for m in M}


def verifier():
    src = open(os.path.join(BASE, "complements_p3_v1.py"), encoding="utf-8").read()
    ok = True
    for ident, _, nom, old, new in M:
        n = src.count(old)
        if n != 1:
            ok = False
            print(f"{ident} : motif présent {n} fois ({nom})")
    print("motifs uniques" if ok else "MOTIFS À CORRIGER")
    return ok


def lancer_un(ident):
    _, famille, nom, old, new = PAR_ID[ident]
    d = os.path.join(ICI, "mutants", ident)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    src = open(os.path.join(BASE, "complements_p3_v1.py"), encoding="utf-8").read()
    assert src.count(old) == 1, ident
    open(os.path.join(d, "complements_p3_v1.py"), "w", encoding="utf-8").write(src.replace(old, new))
    shutil.copy(os.path.join(BASE, "test_complements_p3_v1.py"), d)
    env = {**os.environ, "PYTHONPATH": SRC, "PYTHONDONTWRITEBYTECODE": "1"}
    t0 = time.time()
    r = subprocess.run([PY, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "test_complements_p3_v1.py"],
                       cwd=d, env=env, capture_output=True, text=True, timeout=5400)
    lignes = r.stdout.strip().splitlines()
    derniere = lignes[-1] if lignes else r.stderr[-300:]
    echec = next((x for x in lignes if x.startswith("FAILED") or x.startswith("ERROR")), "")
    res = {"id": ident, "famille": famille, "mutant": nom, "etat": "tué" if r.returncode != 0 else "SURVIT",
           "code": r.returncode, "resume": derniere, "premier_echec": echec, "duree_s": round(time.time() - t0)}
    with open(os.path.join(ICI, "mutants-resultats.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(res, ensure_ascii=False) + "\n")
    with open(os.path.join(d, "pytest.log"), "w", encoding="utf-8") as f:
        f.write(r.stdout[-20000:] + "\n" + r.stderr[-5000:])
    os.remove(os.path.join(d, "complements_p3_v1.py"))              # garde le journal, pas la copie
    os.remove(os.path.join(d, "test_complements_p3_v1.py"))
    return res


if __name__ == "__main__":
    if sys.argv[1] == "verifier":
        sys.exit(0 if verifier() else 1)
    if sys.argv[1] == "lancer":
        par = int(os.environ.get("PARALLELE", "2"))
        ids = sys.argv[2:] or [m[0] for m in M]
        with ThreadPoolExecutor(par) as ex:
            for res in ex.map(lancer_un, ids):
                print(f"{res['etat']:7s} {res['id']:4s} {res['mutant']} — {res['resume']} ({res['duree_s']} s)", flush=True)
