"""Campagne de mutations des essais du moteur v9-v8r : seize copies du moteur, une garde retirée chacune ; une mutation est
tuée si un essai au moins échoue. Lancement, dans un environnement vidé de toute clé et depuis la racine du dépôt :
env -i PATH="$PATH" HOME="$HOME" PYTHONPATH=src ESSAIS_V8R_ENVIRONNEMENT_VIDE=1 python3 -B docs/notes/collisionneur-v9/mutations_collisionneur_v9_v8r.py DOSSIER_TEMPORAIRE
Les essais coupent le transport : aucune requête ne part."""
import sys, importlib.util, io, contextlib, os
from pathlib import Path
S = Path(sys.argv[1]); ICI = Path("docs/notes/collisionneur-v9").resolve()
src = (ICI / "collisionneur_v9_v8r.py").read_text(encoding="utf-8")
spec = importlib.util.spec_from_file_location("essais_v8r", ICI / "test_collisionneur_v9_v8r.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
M = {
 "M1 refus du nom refusé retiré (composition)": ("    if nom_cle_gemini in NOMS_CLE_GEMINI_REFUSES:  # v9-v8q", "    if False and nom_cle_gemini in NOMS_CLE_GEMINI_REFUSES:  # v9-v8q"),
 "M2 préfixe non contrôlé": ("    if not nom_cle_gemini.startswith(PREFIXE_CLE_GEMINI):", "    if False and not nom_cle_gemini.startswith(PREFIXE_CLE_GEMINI):"),
 "M3 flux à nom fixe": ("    cle, motif = cle_gemini(m)  # v9-v8r (1) : nom de la composition seulement, sans repli\n    if motif:\n        return Reponse(echec=motif)\n    try:\n        corps = demande_gemini(m, prompt, max_tokens)", "    cle, motif = os.environ.get('GEMINI_API_KEY'), None\n    if motif:\n        return Reponse(echec=motif)\n    try:\n        corps = demande_gemini(m, prompt, max_tokens)"),
 "M4 journal muet": ('        ajouter_journal(dossier, {"nom_cle_gemini": nom,', '        0 and ajouter_journal(dossier, {"nom_cle_gemini": nom,'),
 "C1 forme du nom non contrôlée": ("                nom_cle_gemini):  # v9-v8q\n", "                ):  # v9-v8q\n"),
 "C2 repli au comptage": ('    cle, motif = cle_gemini(m)  # v9-v8r (1) : nom de la composition seulement, sans repli\n    if motif:\n        raise RefusCompte("COMPTE_IMPOSSIBLE", motif)', '    cle, motif = os.environ.get(m.get("nom_cle") or "GEMINI_API_KEY"), None\n    if not cle:\n        raise RefusCompte("COMPTE_IMPOSSIBLE", "absente")'),
 "C3 création de lot à nom fixe": ('    requete = urllib.request.Request(f"{URL_GEMINI}/{m[\'id\']}:batchGenerateContent",\n                                     data=json.dumps(corps, ensure_ascii=False).encode("utf-8"), method="POST",\n                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})', '    requete = urllib.request.Request(f"{URL_GEMINI}/{m[\'id\']}:batchGenerateContent",\n                                     data=json.dumps(corps, ensure_ascii=False).encode("utf-8"), method="POST",\n                                     headers={"Content-Type": "application/json", "x-goog-api-key": os.environ.get("GEMINI_API_KEY") or cle})'),
 "C4 relevé à nom fixe": ('    releve = urllib.request.Request(f"{URL_GEMINI_BASE}/{nom}", method="GET", headers={"x-goog-api-key": cle})', '    releve = urllib.request.Request(f"{URL_GEMINI_BASE}/{nom}", method="GET", headers={"x-goog-api-key": os.environ.get("GEMINI_API_KEY") or cle})'),
 "C5 journal écrit la valeur": ('        ajouter_journal(dossier, {"nom_cle_gemini": nom,', '        ajouter_journal(dossier, {"valeur": os.environ.get(nom), "nom_cle_gemini": nom,'),
 "C6 écran affiche la valeur": ('    print(f"Clé de Google : variable {nom} (nom seulement', '    print(f"Clé de Google : variable {nom} {os.environ.get(nom)} (nom seulement'),
 "C7 défaut de la ligne de commande changé": ('        s.add_argument("--cle-gemini", default=NOMS_CLES["gemini"],  # v9-v8q', '        s.add_argument("--cle-gemini", default="GEMINI_API_KEY_2",  # v9-v8q'),
 "C9 journal du nom avant le contrôle du script": ("        declarer_script(dossier, a.reprise)  # v9-v3\n        declarer_options(dossier, a)  # v9-v8k\n        declarer_cle_gemini(dossier)  # v9-v8q\n", "        declarer_cle_gemini(dossier)  # v9-v8q\n        declarer_script(dossier, a.reprise)  # v9-v3\n        declarer_options(dossier, a)  # v9-v8k\n"),
 "C10 annulation à nom fixe": ('    requete = urllib.request.Request(f"{URL_GEMINI_BASE}/{nom}:cancel", data=b"{}", method="POST",\n                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})', '    requete = urllib.request.Request(f"{URL_GEMINI_BASE}/{nom}:cancel", data=b"{}", method="POST",\n                                     headers={"Content-Type": "application/json", "x-goog-api-key": os.environ.get("GEMINI_API_KEY") or cle})'),
 "R4 restriction de la clé libre retirée": ("    if nom_cle_gemini in NOMS_CLE_GEMINI_RESTREINTS:  # v9-v8r (4)", "    if False and nom_cle_gemini in NOMS_CLE_GEMINI_RESTREINTS:  # v9-v8r (4)"),
 "R5 espace d'Anthropic non contrôlé": ("    if nom_espace_anthropic is not None and nom_espace_anthropic.startswith(PREFIXES_AUTRES_FOURNISSEURS):  # v9-v8r (5)", "    if False and nom_espace_anthropic is not None and nom_espace_anthropic.startswith(PREFIXES_AUTRES_FOURNISSEURS):  # v9-v8r (5)"),
 "D1 défense en profondeur retirée": ('    if m.get("nom_cle") in NOMS_CLE_GEMINI_REFUSES:\n        return None, f"{m[\'nom_cle\']} est refusée', '    if False and m.get("nom_cle") in NOMS_CLE_GEMINI_REFUSES:\n        return None, f"{m[\'nom_cle\']} est refusée'),
}
essais = [(n, f) for n, f in sorted(vars(T).items()) if n.startswith("test_") and callable(f)]
tuees = 0
for nom, (a, b) in M.items():
    assert src.count(a) == 1, (nom, src.count(a))
    p = S / ("mutant_" + nom.split()[0] + ".py"); p.write_text(src.replace(a, b), encoding="utf-8")
    T.MOTEUR = p
    tombes = []
    for n, f in essais:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                f()
        except Exception:
            tombes.append(n)
    tuees += bool(tombes)
    print(("TUÉE   " if tombes else "SURVIT ") + nom + (" : " + ", ".join(tombes[:3]) if tombes else ""))
print(f"{tuees} mutations tuées sur {len(M)}")
