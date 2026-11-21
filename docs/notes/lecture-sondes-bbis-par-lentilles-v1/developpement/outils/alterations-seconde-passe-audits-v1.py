MODULE = "audits_v2.py"
ESSAIS = ["test_lentilles_sondes_bbis_seconde_passe_phrases_reproduction_v1.py"]
ALTERATIONS = [
 ("moitié prise pour plus de la moitié", "return bool(total and 2 * n > total)", "return bool(total and 2 * n >= total)"),
 ("couche 7 non exigée", "memes(K2.LENTILLE_NOTRE_R, K.LENTILLE_PUBLIQUE, (7,))", "memes(K2.LENTILLE_NOTRE_R, K.LENTILLE_PUBLIQUE)"),
 ("couche 23 non exigée", 'couche_23 = [r for r in recouvrements if r["couche"] == 23]', "couche_23 = list(recouvrements)"),
 ("plongements seuls non regardés", "if K2.LENTILLE_NOTRE_S in d and cle in seuls and d[K2.LENTILLE_NOTRE_S][0] == seuls[cle])", "if False)"),
 ("moitiés : sens inversé", 'if r["moities"] < r["publique_et_notre_r"])', 'if r["moities"] > r["publique_et_notre_r"])'),
 ("reproduction différente ignorée", '"reproduction_de_la_premiere_passe_differente": bool(reproduction.get("audit_de_symetrie_a_jouer")),', '"reproduction_de_la_premiere_passe_differente": False,'),
 ("tout négatif jamais levé", '"aucune_lecture_concentree_ni_intermediaire_par_aucune_lentille": bool(lectures) and not distinctes,', '"aucune_lecture_concentree_ni_intermediaire_par_aucune_lentille": False,'),
 ("vingt directions : dix-neuf suffisent", "return len(sondes) == N_SONDES and all((s, lentille) in concentrees for s in sondes)", "return len(sondes) == N_SONDES and sum((s, lentille) in concentrees for s in sondes) >= 19"),
]
