import shutil, subprocess, sys, os, json
from pathlib import Path
DEPOT = Path("/home/user/controle-ia-travail")
ICI = Path(__file__).resolve().parent / "mut"
M = [
 ("M01 racine courte admise", "graines.py", "racine < 0 or racine.bit_length() < BITS_MIN_RACINE - 8", "racine < 0", "graines"),
 ("M02 invariance d'ordre muette", "graines.py", "    ref = tirage(ordres[0])\n", "    return\n    ref = tirage(ordres[0])\n", "graines"),
 ("M03 revelation avant fin", "graines.py", "        if not self._fin:\n            raise", "        if False:\n            raise", "graines"),
 ("M04 champ sans preuve admis", "vue.py", "            if c.preuve is None:\n                raise", "            if False:\n                raise", "vue"),
 ("M05 canari prive ignore", "vue.py", "    fuites = [n for n in champs_prives if traces[n] in octets]", "    fuites = []", "vue"),
 ("M06 dependance non recalculable admise", "tirage.py", "        hors = set(dependances) - DEPENDANCES_RECALCULABLES", "        hors = set()", "tirage"),
 ("M07 rejeu ne verifie pas les pieces", "tirage.py", "        if not np.array_equal(rejoue.pieces, journal.pieces):", "        if False:", "tirage"),
 ("M08 rejeu independant a tort", "tirage.py", "        if not self.depend_du_passe:\n            pi = np.broadcast_to", "        if True:\n            pi = np.broadcast_to", "tirage"),
 ("M09 racine de rejeu egale admise", "tirage.py", "        if empreinte_racine(racine_rejeu) == journal.empreinte_racine:\n            raise RefusDevin(\"racine de rejeu égale à la racine de la pièce", "        if False:\n            raise RefusDevin(\"racine de rejeu égale à la racine de la pièce", "tirage"),
 ("M10 ajustement sur le pli d'epreuve", "predicteurs.py", "        if set(ids) & self._ids_e:", "        if False:", "predicteurs"),
 ("M11 sorties sans controle d'empreinte", "predicteurs.py", "            if empreinte_objet(p) != self.empreintes[j]:", "            if False:", "predicteurs"),
 ("M12 coffre ouvert sans scellement", "predicteurs.py", "        if famille.empreinte is None:\n            raise RefusDevin(\"ouverture", "        if False:\n            raise RefusDevin(\"ouverture", "predicteurs"),
 ("M13 orientation toujours positive", "predicteurs.py", "        self.orientation = -1.0 if c < 0 else 1.0", "        self.orientation = 1.0", "predicteurs admission"),
 ("M14 p-valeur sans +1", "statistique.py", "    return float((1 + np.sum(M_nul >= M)) / (M_nul.size + 1))", "    return float(np.sum(M_nul >= M) / M_nul.size)", "statistique"),
 ("M15 Z sans centrage par pi", "statistique.py", "    num = (A2 - pi2) @ R.T", "    num = A2 @ R.T", "statistique"),
 ("M16 M = premier predicteur", "statistique.py", "    M = float(np.max(Z))\n    Mnul = Znul.max(axis=1)", "    M = float(Z[0])\n    Mnul = Znul[:, 0]", "statistique"),
 ("M17 Z* avec pi observe", "statistique.py", "    return _resultat(Z, z_piece(R, A_nul, pi_nul), B", "    return _resultat(Z, z_piece(R, A_nul, journal.propensions), B", "statistique"),
 ("M18 standardisation non controlee", "statistique.py", "    if obtenu.shape != attendu.shape or not np.allclose", "    if False and not np.allclose", "statistique"),
 ("M19 verdict incomplet admis", "admission.py", "    if manquants:\n        raise RefusDevin(f\"verdict incomplet", "    if False:\n        raise RefusDevin(f\"verdict incomplet", "admission"),
 ("M20 temoin factice ignore", "admission.py", "    declenchement = (res_f[\"p\"] <= SEUIL_FACTICE) or (res_t[\"p\"] > SEUIL_TEMOIN)", "    declenchement = (res_t[\"p\"] > SEUIL_TEMOIN)", "admission"),
 ("M21 racine en clair non cherchee", "admission.py", "        verifier_racine_absente(rac, textes)", "        pass", "admission"),
 ("M22 racines d'epreuve tirees avant scellement", "admission.py", "    pli_e = _Pli(f\"{base}:epreuve\", ids_e, queue_e, source)\n    je =", "    je =", "admission"),
 ("M23 fuite temoin absente du monde", "admission.py", "tuple(fuites_monde) + (cfg.temoin_fuite,)", "tuple(fuites_monde)", "admission"),
 ("M24 epreuve a part dans M (rejet sur M)", "admission.py", "    rejet = res[\"p\"] <= cfg.alpha", "    rejet = res[\"p\"] <= cfg.alpha or (isinstance(epreuve_a_part, dict) and epreuve_a_part[\"rejet\"])", "admission"),
 ("M25 temoin a secret identique muet", "borne_haute.py", "        if t:\n            raise", "        if False:\n            raise", "borne_haute"),
 ("M26 table 11 ferme-rejette lu conforme", "lien_epreuve_11.py", "    if bras == FERME and devin_rejette:\n        return HARNAIS_FUIT", "    if bras == FERME and devin_rejette:\n        return CONFORME", "lien_epreuve_11"),
 ("M27 test de mort 1 a >= 72", "puissance.py", "    return rejets_sains > SEUIL_MORT_1", "    return rejets_sains >= SEUIL_MORT_1", "puissance"),
 ("M28 source factice admise", "monde_plante.py", "        if self.source == \"factice\":\n            raise", "        if False:\n            raise", "monde_plante"),
 ("M29 garde de canaris sautee dans l'admission", "admission.py", "    canaris = verifier_extracteur(extracteur, modele, canaux_visibles, list(CHAMPS_PRIVES),", "    canaris = {} or (lambda *a: {'saute': True})(extracteur, modele, canaux_visibles, list(CHAMPS_PRIVES),", "admission"),
 ("M30 rejeu lecture racine egale admise", "tirage.py", "            raise RefusDevin(\"racine de rejeu égale à la racine de la lecture\")", "            pass", "tirage statistique"),
 ("M31 seuil temoin fuite 0,5", "admission.py", "SEUIL_TEMOIN = 0.05", "SEUIL_TEMOIN = 0.5", "admission"),
 ("M32 borne haute fausse a 0 difference", "borne_haute.py", "        return 1 - (1 - niveau) ** (1 / N)", "        return 0.0", "borne_haute"),
]
def preparer():
    if ICI.exists(): shutil.rmtree(ICI)
    (ICI/"src").mkdir(parents=True); (ICI/"tests").mkdir()
    shutil.copytree(DEPOT/"src/controle_ia", ICI/"src/controle_ia", ignore=shutil.ignore_patterns("__pycache__"))
    for f in list((DEPOT/"tests").glob("test_devin_v1_*.py")) + [DEPOT/"tests/conftest.py", DEPOT/"tests/greffon_echecs_connus_v2.py"] + list((DEPOT/"tests").glob("echecs-connus-v2*")):
        shutil.copy(f, ICI/"tests"/f.name)
    shutil.copy(DEPOT/"pyproject.toml", ICI/"pyproject.toml")
    (ICI/"tests/conftest.py").write_text("# copie de mutation : sans greffon des echecs connus\n")
    shutil.copytree(ICI/"src/controle_ia/devin_v1", ICI/"orig_devin")
def lancer(cibles):
    fichiers = [f"tests/test_devin_v1_{c}.py" for c in cibles.split()]
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *fichiers], cwd=ICI,
                       env=dict(os.environ, PYTHONPATH=str(ICI/"src")), capture_output=True, text=True)
    return r.returncode, r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:]
preparer()
d = ICI/"src/controle_ia/devin_v1"
seul = sys.argv[1:] 
for nom, f, old, new, cibles in M:
    if seul and nom.split()[0] not in seul: continue
    shutil.rmtree(d); shutil.copytree(ICI/"orig_devin", d)
    t = (d/f).read_text()
    if t.count(old) != 1:
        print(f"{nom}: MOTIF INTROUVABLE ({t.count(old)})", flush=True); continue
    (d/f).write_text(t.replace(old, new))
    rc, fin = lancer(cibles)
    etat = 'TUE' if (rc != 0 and 'failed' in fin) else ('SURVIT' if rc == 0 else 'ERREUR')
    print(f"{nom}: {etat} — {fin}", flush=True)
shutil.rmtree(d); shutil.copytree(ICI/"orig_devin", d)
rc, fin = lancer("graines tirage")
print("controle sans mutation:", rc, fin)
