import shutil, subprocess, sys
from pathlib import Path
M = Path(sys.argv[1]); py = sys.argv[2]
mutants = {
 "regle_k_retiree": ("    return decalees >= k, decalees < k", "    return True, False"),
 "ancrage_ignore": ("    if not r_s <= ANCRAGE_MAX:\n        return \"sans marge\"", "    if False:\n        return \"sans marge\""),
 "decodage_contexte_inverses": ("        return \"décodage\"\n    if max_contexte", "        return \"contexte\"\n    if max_contexte"),
 "trop_beau_garde_ignore": ("    if garde[\"trop_beau\"]:\n        noeud = True", "    if garde[\"trop_beau\"]:\n        noeud = False"),
 "reserve_comme_propriete": ("all(pr[j] == \"conforme\" for j in JUGES):\n        lecture = \"propriété du modèle\"", "all(pr[j] != \"x\" for j in JUGES):\n        lecture = \"propriété du modèle\""),
 "pb7_sans_negatif": ("g[\"equivalence\"] == \"contraire\" and g[\"controle_negatif\"][\"lecture\"] == \"conforme\")", "g[\"equivalence\"] == \"contraire\")"),
 "production_sans_negatif": ("    if neg[\"lecture\"] != \"conforme\":\n        sortie[\"motifs\"]", "    if False:\n        sortie[\"motifs\"]"),
 "couverture_stricte": ("\"atteinte\": x[\"jetons_generes\"] >= SEUILS_COUVERTURE[juge]", "\"atteinte\": x[\"jetons_generes\"] > SEUILS_COUVERTURE[juge]"),
 "d1_non_probant_ignore": ("    elif not pos[\"max_contexte\"] <= TOLERANCE_SIMPLE:", "    elif False:"),
 "chemin_trop_beau_apres_fidele": ("    elif sortie[\"trop_beau\"]:\n        lecture = \"trop beau\"\n", ""),
 "somme_frequente_ignoree": ("        if part is not None and part > SOMME_FREQUENTE_MAX:", "        if False:"),
 "relecture_rs1_ignoree": ("        if (r[\"notes\"], r[\"anomalies\"], r[\"score\"]) != consigne:", "        if False:"),
}
for nom, (a, b) in mutants.items():
    d = M / nom
    if d.exists(): shutil.rmtree(d)
    shutil.copytree(M / "base", d)
    f = d / "src/controle_ia/environnements/lire_requalification.py"
    t = f.read_text()
    assert t.count(a) == 1, nom
    f.write_text(t.replace(a, b))
    r = subprocess.run([py, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "tests/test_plan_b_lecteur.py",
                        "-k", "not gardes_de_lecture and not table_e and not bout_en_bout and not effondrement and not commande and not defaut_du_chemin and not modules_a_un"],
                       cwd=d, capture_output=True, text=True, env={"PYTHONPATH": "src", "PATH": "/usr/bin:/bin"})
    print(nom, "TUÉ" if r.returncode else "SURVIT", r.stdout.strip().splitlines()[-1][:100])
