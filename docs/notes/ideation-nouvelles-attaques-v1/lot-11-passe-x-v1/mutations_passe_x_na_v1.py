"""Mutations du lot 11 : chaque garde cassée doit faire tomber au moins un essai. T0 (témoin non muté) doit survivre."""
import json, os, shutil, subprocess, sys, tempfile
ICI = os.path.dirname(os.path.abspath(__file__))
PY = "/home/user/controle-ia-travail/.venv/bin/python"
M = [
    ("T0", None, None),
    ("G1 empreinte", 'if sha(b) != EMPREINTE_PIECE:', 'if False:'),
    ("G1 motifs", '        if garde_motifs_ligne(ligne):', '        if False:'),
    ("G2 compagnon", "or open(comp).read().split()[0] != sha(b)", ""),
    ("G2 extras", 'if not set(m.get("extras", {})) <= EXTRAS_PERMIS[p["fournisseur"]]:', 'if False:'),
    ("G3 GO", 'raise Refus(f"G3 : {g} absent du registre")', 'pass'),
    ("G5 pire", 'if pire(m, len(piece)) > PIRE_TENTATIVE:', 'if False:'),
    ("G6 garde Google", '    if pb:\n        raise Refus("G6', '    if False:\n        raise Refus("G6'),
    ("G6 défaut Google", 'if GG.defaut_reponse_google(r["fin"], r["texte"], r["pensee_jetons"], blocage=r["blocage"]):', 'if False:'),
    ("G7 sous-part", 'if self.cumul[cle] + self.en_vol[cle] + p_t > D(str(self.c["sous_parts"][cle])) or total + p_t > P_X:', 'if False:'),
    ("G7 somme", 'if sum(D(str(v)) for v in c["sous_parts"].values()) > P_X:', 'if False:'),
    ("G8 arrêt 13", '            self.arret_13.set()', '            pass'),
    ("G8 crédit", 'r["credit"] = bool(MOTIFS_CREDIT.search(r["erreur"] + " " + str(err.get("message", ""))))', 'r["credit"] = False'),
    ("G9 repli", 'if classe != "refus du modèle (classifieur)":', 'if True:'),
    ("G9 refus", 'elif fournisseur == "anthropic" and r["fin"] == "refusal":', 'elif False:'),
    ("G9 par_repli", '"par_repli": rang > 0', '"par_repli": False'),
    ("G10 écrasement", 'with open(chemin, "xb") as brut:', 'with open(chemin, "wb") as brut:'),
    ("G11 clé", 'raise Refus(f"G11 : clé {p[\'cle_var\']} absente")', 'pass'),
    ("G12 substitué", 'if servi is None or not (servi == m or servi.startswith(m + "-")):', 'if False:'),
    ("A3 pire", '        return pire_t, True\n', '        return D(0), True\n'),
    ("illisible", 'elif r["fin"] not in ("end_turn", "stop") or not r["texte"].strip():', 'elif False:'),
    ("texte au journal", 'texte_signes=len((r or {}).get("texte") or ""),', 'texte_signes=(r or {}).get("texte"),'),
]
src = open(os.path.join(ICI, "passe_x_na_v1.py")).read()
res = []
for nom, a, b in M:
    d = tempfile.mkdtemp()
    s = src
    if a is not None:
        assert s.count(a) == 1, nom
        s = s.replace(a, b)
    open(os.path.join(d, "passe_x_na_v1.py"), "w").write(s)
    shutil.copy(os.path.join(ICI, "test_passe_x_na_v1.py"), d)
    p = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "test_passe_x_na_v1.py"],
                       cwd=d, capture_output=True, text=True, env={"PATH": os.environ["PATH"]})
    issue = "survit" if p.returncode == 0 else "tuée"
    res.append({"mutation": nom, "issue": issue})
    shutil.rmtree(d)
ok = res[0]["issue"] == "survit" and all(r["issue"] == "tuée" for r in res[1:])
print(json.dumps({"mutations": res, "conforme": ok}, ensure_ascii=False, indent=1))
sys.exit(0 if ok else 1)
