import subprocess, sys, pathlib, time
WT = pathlib.Path("/home/user/controle-ia-travail/.claude/worktrees/agent-a89be1d2701a117b9")
BT = pathlib.Path("/tmp/claude-0/-home-user-controle-ia-travail/b09e1b49-1473-5167-b0d5-946b1adabcb0/scratchpad/bt-mutcl")
PY = "/home/user/controle-ia-travail/.venv/bin/python"
C3 = "src/controle_ia/barreau5_familles/commande_lecture_v3.py"
OV = "src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py"
L3 = "scripts/lancer_b5f_lecture_v3.sh"
TC = "tests/test_commande_lecture_v3.py"
TO = "tests/test_ouverture_suffixes_v1.py"
M = [
 ("M1 erratum non vérifié", C3, 'if m["erratum"] != ERRATUM_SHA256:', 'if False:', [TC]),
 ("M2 branche non vérifiée", C3, 'if m["branche"] != BRANCHE_SORTIE:', 'if False:', [TC]),
 ("M3 candidate sans NFC", C3, '_ESPACES.sub(" ", unicodedata.normalize("NFC", ligne))', '_ESPACES.sub(" ", ligne)', [TC]),
 ("M4 candidate sans espaces ramenées", C3, '_ESPACES.sub(" ", unicodedata.normalize("NFC", ligne))', 'unicodedata.normalize("NFC", ligne)', [TC]),
 ("M5 candidate sans barre", C3, ' or vue.startswith("| " + PREFIXE_EPINGLAGE.rstrip(" "))', '', [TC]),
 ("M6 ascendance v2->v3 non vérifiée", C3, '    if a.returncode != 0:\n        raise GardeArret(f"commit v3', '    if False:\n        raise GardeArret(f"commit v3', [TC]),
 ("M7 présence des modules et lanceurs non exigée", C3, 'for f in (MODULE, LANCEUR, MODULE_OUVERTURE, LANCEUR_OUVERTURE):', 'for f in ():', [TC]),
 ("M8 compte base64 -d retiré (module)", C3, ' or cmd.count("base64 -d") != 1', '', [TC]),
 ("M9 une seule ligne de sortie non exigée (lanceur)", L3, '[ "$(printf \'%s\\n\' "$sortie" | wc -l)" = 1 ]', 'true', [TC]),
 ("M10 texte ancien au moins une fois", C3, 'if octets.count(ancien) != 1:', 'if octets.count(ancien) < 1:', [TC]),
 ("M11 c(base) du résumé sans exiger_copie_lue", OV, 'sortie[b] = exiger_copie_lue(b, formation[b].get("copie"), relance)', 'sortie[b] = formation[b].get("copie")', [TO]),
 ("M12 variante (b) par any", OV, 'elif all(g == copies[b] for b, g in vues.items()):', 'elif any(g == copies[b] for b, g in vues.items()):', [TO]),
 ("M13 épinglage lu au registre donné", OV, 'v2, v3 = commit_de_code_verifie(racine, cl["commit"], prouve)', 'v2, v3 = commit_de_code_verifie(racine, cl["commit"], texte_registre)', [TO]),
 ("M14 CODE-LECTURE du commit prouvé ignoré: commit (c'1) pris de SCORES", OV, 'commit_de_code_verifie(racine, cl["commit"], prouve)', 'commit_de_code_verifie(racine, sc["commit"], prouve)', [TO]),
 ("M15 épinglage omis dans variante", OV, '    if racine is not None:\n        code_au_commit_v3(racine, texte_registre)\n    copies =', '    copies =', [TO]),
 ("M16 traduction en (a) admise", OV, '_exiger(decision["variante"] == "b",', '_exiger(decision["variante"] in "ab",', [TO]),
]
sel = sys.argv[1:] 
for nom, f, old, new, tests in M:
    if sel and nom.split()[0] not in sel: continue
    p = WT / f; orig = p.read_bytes(); s = orig.decode()
    assert s.count(old) == 1, (nom, s.count(old))
    p.write_text(s.replace(old, new, 1), encoding="utf-8")
    t0 = time.time()
    try:
        r = subprocess.run([PY, "-m", "pytest", "-x", "-q", "--tb=no", "-rN", "-p", "no:cacheprovider", f"--basetemp={BT}/{nom.split()[0]}", *tests], cwd=WT, env={**__import__("os").environ, "PYTHONPATH": "src"}, capture_output=True, text=True, timeout=1500)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:]
        print(f"{nom}: {'ATTRAPÉE' if r.returncode else 'NON ATTRAPÉE'} ({last}) {time.time()-t0:.0f}s", flush=True)
    finally:
        p.write_bytes(orig)
subprocess.run(["git", "-C", str(WT), "status", "--short"])
