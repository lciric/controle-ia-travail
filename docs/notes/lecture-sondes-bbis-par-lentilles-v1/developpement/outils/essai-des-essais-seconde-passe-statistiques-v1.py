import pathlib, shutil, subprocess, sys, os
S = pathlib.Path(sys.argv[1]); R = pathlib.Path("/home/user/controle-ia-travail")
muts = [
 ("plus grand identifiant gardé", "np.lexsort((idt[candidats].numpy(), -(valeurs", "np.lexsort((-idt[candidats].numpy(), -(valeurs"),
 ("colonnes à égalité non reprises", "for j in torch.nonzero(egalite)[:, 0].tolist():\n        rangs[:, j]", "for j in []:\n        rangs[:, j]"),
 ("ordre interne par identifiant omis", "par_id = torch.argsort(idt[rangs], dim=0, stable=True)", "par_id = torch.argsort(-idt[rangs], dim=0, stable=True)"),
 ("pôles : signe − avant signe +", "np.lexsort((moins, neurone,", "np.lexsort((-moins, neurone,"),
 ("pôles : plus grand indice", "np.lexsort((moins, neurone,", "np.lexsort((moins, -neurone,"),
 ("égalité des pôles jamais dite", '"egalite": bool(objet and candidats.size > k)}', '"egalite": False}'),
 ("égalité d'une liste jamais dite", '"egalite": bool(objet and candidats.numel() > k)}', '"egalite": False}'),
 ("attendu des familles faux", 'float(resume.familles[nom].double().mean())', 'float(resume.familles[nom].double().max())'),
 ("part sur le quantile des M", "(valeurs > quantiles_sans_soi(scores_nuls, rangs, valeurs))", "(valeurs > quantile[rangs])"),
 ("sans objet jamais dit", 'case["sans_objet"] = case.get("sans_objet", 0) + (int(listes) if sans_objet else 0)', 'case["sans_objet"] = 0'),
]
src = (R/"src/controle_ia/lentilles_sondes_bbis/statistiques_v4.py").read_text()
vues = 0
for nom, a, b in muts:
    assert src.count(a) == 1, (nom, src.count(a))
    d = S/"mut"; shutil.rmtree(d, ignore_errors=True); shutil.copytree(R/"src", d/"src", ignore=shutil.ignore_patterns("__pycache__"))
    (d/"src/controle_ia/lentilles_sondes_bbis/statistiques_v4.py").write_text(src.replace(a, b))
    (d/"tests").mkdir(); shutil.copy(R/"tests/test_lentilles_sondes_bbis_seconde_passe_statistiques_v1.py", d/"tests")
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-k", "not taux", "--rootdir", str(d),
                        str(d/"tests/test_lentilles_sondes_bbis_seconde_passe_statistiques_v1.py")], cwd=d,
                       env={**os.environ, "PYTHONPATH": str(d/"src"), "PYTHONDONTWRITEBYTECODE": "1"}, capture_output=True, text=True)
    vue = r.returncode != 0; vues += vue
    print(("VUE     " if vue else "NON VUE ") + nom)
print(f"{vues} altérations vues sur {len(muts)}")
