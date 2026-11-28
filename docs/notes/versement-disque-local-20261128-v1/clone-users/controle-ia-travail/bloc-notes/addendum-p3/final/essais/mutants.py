"""Mutants (hors livrable) : une règle affaiblie à la fois dans une copie du module ; les tests visés doivent échouer."""
import json, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
ICI = os.path.dirname(os.path.abspath(__file__))
FINAL = os.path.dirname(ICI)
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
M = [
 ("A1 sens haut jamais levé", 'contraire = r["ecart_bas"] <= 0.0 if sens == "au-dessus" else r["ecart_bas"] > 0.0',
  'contraire = r["ecart_bas"] <= 0.0 if sens == "au-dessus" else False', "A1_artefact_sens_haut"),
 ("A6 sens inverse jamais levé", 'bool(r["bas"] > 0.0 and not deja)', 'bool(False and not deja)', "A6_artefact_sens_inverse"),
 ("fenêtres notées par la moyenne des jetons", 'S_pre[o] = [agreger_par_jeton(s, lg, int(x), int(x) + L) for x in dp]',
  'S_pre[o] = [float(np.mean(s[int(x):int(x) + L])) for x in dp]', "aucune_moyenne"),
 ("A4 (b) poids k² (tranche commune aux copies)", '            st = copies', '            st = taches[i]', "copies_doublees"),
 ("A4 (a) tranches figées sous l'étiquette internes", 'TIRAGES_AIRE, NIVEAU, "internes",', 'TIRAGES_AIRE, NIVEAU, "figees",',
  "A4_sain or A4_artefact_tranches"),
 ("niveau 97,5 % ramené à 95 %", 'NIVEAU_BONFERRONI if (a, b) == JEUX[0] else NIVEAU, None))', 'NIVEAU, None))', "A1_sain"),
 ("garde 6 retirée", '    exiger_issue_recalculee(lecture)                       # garde 6', '    pass', "garde_6"),
 ("valeur non finie remplacée par None", '''            raise GardeArret(f"valeur non finie dans la sortie ({chemin or '/'})")''', '            return None',
  "non_finie"),
 ("manifeste illisible sauté", '''            raise GardeArret(f"{garde} : {chemin} illisible ({type(e).__name__}) : vérification impossible") from None''',
  '            continue', "garde_9"),
 ("règle des trois premiers non stricte", '"trois_premiers": bool(v[:PREMIERS_JETONS].max() > suite)',
  '"trois_premiers": bool(v[:PREMIERS_JETONS].max() >= suite)', "regle_stricte"),
 ("contrôle lu sur une cible non établie", '        if cible == AUCUNE or cible not in self.etablies:', '        if cible == AUCUNE:',
  "contraire_sans_conclusion_etablie and A1-haut"),
 ("A7 marge jamais levée", 'e.controle(test, cible, sep >= lu["bas"], "reserve_A7_marge",', 'e.controle(test, cible, False, "reserve_A7_marge",',
  "A7_artefact_marge"),
 ("A2 (b) jamais levée", 'e.controle("A2 (b)", cible, rb["bas"] <= 0.0,', 'e.controle("A2 (b)", cible, False,', "A2_artefact_biais"),
 ("A4 (c) jamais levée", 'e.controle("A4 (c)", _cible("T1", p), rc["bas"] <= rc["plancher_quantile"],',
  'e.controle("A4 (c)", _cible("T1", p), False,', "A4_artefact_reference"),
 ("A3 Δ_SM jamais levé", 'e.controle(test, cible, r[cle]["bas"] <= 0.0, reserve,', 'e.controle(test, cible, cle == "ST" and r[cle]["bas"] <= 0.0, reserve,',
  "A3_artefact"),
 ("A7 corrélation jamais prise", 'e.controle(test, _cible("P3-P3", p), abs(r) >= SEUIL_CORRELATION,', 'e.controle(test, _cible("P3-P3", p), False,',
  "A7_artefact_correlation"),
 ("entropie des graines non contrôlée", '    if autres:\n        raise GardeArret(f"entropie {autres}', '    if False:\n        raise GardeArret(f"entropie {autres}',
  "entropie_autre"),
 ("réserve non lue jamais créée", '        if contraire is None:\n', '        if contraire is None and False:\n', "A2_degenere or A7_degenere"),
 ("garde 10 retirée", '        if vues - {declaree}:', '        if False:', "garde_10"),
 ("garde 5 retirée", '        if cle != attendu:', '        if False:', "garde_5"),
 ("A4 (b) jamais levée", 'e.controle("A4 (b)", _cible("T1", p), rb["ecart_bas"] <= 0.0,', 'e.controle("A4 (b)", _cible("T1", p), False,',
  "A4_artefact_confusion"),
 ("A8 saturation jamais levée", 'any(v > SEUIL_POIDS_MAXIMAL for v in med.values())', 'False', "A8_artefact_saturation"),
 ("A5 T2_propre jamais levée", '(lambda x: x["bas"] <= 0.0),', '(lambda x: False),', "A5_artefact"),
 ("lecture modifiée non vue", '    if _canonique(lecture) != instantane:', '    if False:', "issue_modifiee"),
 ("garde 11 retirée", '    generale = 2 * len(en_echec) > len(entrees)', '    generale = False', "garde_11"),
 ("garde 3 : histoire coupée acceptée", '''    if _git(racine, "rev-parse", "--is-shallow-repository").strip() != "false":''', '    if False:', "garde_3"),
]

def lancer(k):
    nom, old, new, sel = M[k]
    d = os.path.join(ICI, "mutants", f"m{k:02d}")
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    src = open(os.path.join(FINAL, "complements_p3_v1.py"), encoding="utf-8").read()
    assert src.count(old) == 1, (nom, src.count(old))
    open(os.path.join(d, "complements_p3_v1.py"), "w", encoding="utf-8").write(src.replace(old, new))
    shutil.copy(os.path.join(FINAL, "test_complements_p3_v1.py"), d)
    env = {**os.environ, "PYTHONPATH": "/home/user/controle-ia-travail/src", "PYTHONDONTWRITEBYTECODE": "1"}
    r = subprocess.run([PY, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "test_complements_p3_v1.py", "-k", sel],
                       cwd=d, env=env, capture_output=True, text=True, timeout=1500)
    derniere = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
    shutil.rmtree(d, ignore_errors=True)
    return nom, ("tué" if r.returncode != 0 else "SURVIT"), derniere

with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(lancer, range(len(M))))
for nom, etat, derniere in res:
    print(f"{etat:7s} {nom} — {derniere}")
print(f"tués : {sum(e == 'tué' for _, e, _ in res)} sur {len(res)}")
