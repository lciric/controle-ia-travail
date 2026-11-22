"""Mutations du paquet devin_v2, jouées sur une copie, depuis la racine de la copie.

Reprise des 32 mutations de la contre-lecture (`contre-lecture-code-devin-scripts-v1/
mutations.py`), portées sur les noms de la version 2, plus les mutations des gardes
neuves (C1, C2, C9, C14, C15, C16). La copie a son propre `pyproject.toml` (chemin
`src` relatif à la copie) et un `conftest.py` vide ; `PYTHONPATH` pointe la copie :
le code du dépôt n'est jamais chargé. Usage :
    python mutations_devin_v2.py DOSSIER_DE_COPIE [M13 M15 …]
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[5]
ADM = "admission.py"
M = [
 ("M01 racine courte admise", "graines.py", [("racine < 0 or racine.bit_length() < BITS_MIN_RACINE - 8", "racine < 0")], "graines"),
 ("M02 invariance d'ordre muette", "graines.py", [("    ref = tirage(ordres[0])\n", "    return\n    ref = tirage(ordres[0])\n")], "graines"),
 ("M03 revelation avant fin", "graines.py", [("        if not self._fin:\n            raise", "        if False:\n            raise")], "graines"),
 ("M04 champ sans preuve admis", "vue.py", [("            if c.preuve is None:\n                raise", "            if False:\n                raise")], "vue"),
 ("M05 canari prive ignore", "vue.py", [("    fuites = [n for n in champs_prives if traces[n] in octets]", "    fuites = []")], "vue"),
 ("M06 dependance non recalculable admise", "tirage.py", [("        hors = set(dependances) - DEPENDANCES_RECALCULABLES", "        hors = set()")], "tirage"),
 ("M07 rejeu ne verifie pas les pieces", "tirage.py", [("        if not np.array_equal(rejoue.pieces, journal.pieces):", "        if False:")], "tirage"),
 ("M08 rejeu independant a tort", "tirage.py", [("        if not self.depend_du_passe:\n            pi = np.broadcast_to", "        if True:\n            pi = np.broadcast_to")], "tirage"),
 ("M09 racine de rejeu egale admise", "tirage.py", [("        if empreinte_racine(racine_rejeu) == journal.empreinte_racine:\n            raise RefusDevin(\"racine de rejeu égale à la racine de la pièce", "        if False:\n            raise RefusDevin(\"racine de rejeu égale à la racine de la pièce")], "tirage"),
 ("M10 ajustement sur le pli d'epreuve", "predicteurs.py", [("        if set(ids) & self._ids_e:", "        if False:")], "predicteurs"),
 ("M11 sorties sans controle d'empreinte", "predicteurs.py", [("            if empreinte_objet(p) != self.empreintes[j]:", "            if False:")], "predicteurs"),
 ("M12 coffre ouvert sans scellement", "predicteurs.py", [("        if famille.empreinte is None:\n            raise RefusDevin(\"ouverture", "        if False:\n            raise RefusDevin(\"ouverture")], "predicteurs"),
 ("M13 orientation toujours positive", "predicteurs.py", [("        self.orientation = -1.0 if c < 0 else 1.0", "        self.orientation = 1.0")], "predicteurs admission"),
 ("M14 p-valeur sans +1", "statistique.py", [("    return float((1 + np.sum(M_nul >= M)) / (M_nul.size + 1))", "    return float(np.sum(M_nul >= M) / M_nul.size)")], "statistique"),
 ("M15 Z sans centrage par pi", "statistique.py", [("    num = (A2 - pi2) @ R.T", "    num = A2 @ R.T")], "statistique"),
 ("M16 M = premier predicteur", "statistique.py", [("    M = float(np.max(Z))\n    Mnul = Znul.max(axis=1)", "    M = float(Z[0])\n    Mnul = Znul[:, 0]")], "statistique"),
 ("M17 Z* avec pi observe", "statistique.py", [("    return _resultat(Z, z_piece(R, A_nul, pi_nul), B", "    return _resultat(Z, z_piece(R, A_nul, journal.propensions), B")], "statistique"),
 ("M18 standardisation non controlee", "statistique.py", [("    if obtenu.shape != attendu.shape or not np.allclose", "    if False and not np.allclose")], "statistique"),
 ("M19 verdict incomplet admis", ADM, [("    if manquants:\n        raise RefusDevin(f\"verdict incomplet", "    if False:\n        raise RefusDevin(f\"verdict incomplet")], "admission"),
 ("M20a regle du test de mort 4 sans factice", ADM, [("    return (p_factice <= SEUIL_FACTICE) or (p_temoin > SEUIL_TEMOIN)", "    return (p_temoin > SEUIL_TEMOIN)")], "admission"),
 ("M20b course sans la regle", ADM, [("    declenchement = declenchement_mort_4(res_f[\"p\"], res_t[\"p\"])", "    declenchement = (res_t[\"p\"] > SEUIL_TEMOIN)")], "admission"),
 ("M21a racine en clair non cherchee (epreuve)", ADM, [("        verifier_racine_absente(rac, textes_e)", "        pass")], "admission"),
 ("M21b racine en clair non cherchee (apprentissage)", ADM, [("        verifier_racine_absente(rac, textes_a)", "        pass")], "admission"),
 ("M22a racines d'epreuve tirees avant scellement", ADM, [
     ("    pli_e = _Pli(f\"{base}:epreuve\", ids_e, queue_e, source)\n", ""),
     ("    empreintes_familles = {nom:", "    pli_e = _Pli(f\"{base}:epreuve\", ids_e, queue_e, source)\n    empreintes_familles = {nom:")], "admission"),
 ("M22b garde C14 muette", ADM, [("    if any(r.ordre <= dernier for r in racines_epreuve):", "    if False:")], "admission"),
 ("M22c garde C14 non appelee", ADM, [("    exiger_epreuve_apres_scellement(pli_e.racines.values(),", "    (lambda *a: None)(pli_e.racines.values(),")], "admission admission_garde_c14"),
 ("M23 fuite temoin absente du monde", ADM, [("tuple(fuites_monde) + (cfg.temoin_fuite,)", "tuple(fuites_monde)")], "admission"),
 ("M24 epreuve a part dans M (rejet sur M)", ADM, [("    rejet = res[\"p\"] <= cfg.alpha", "    rejet = res[\"p\"] <= cfg.alpha or (isinstance(epreuve_a_part, dict) and epreuve_a_part[\"rejet\"])")], "admission"),
 ("M25 temoin a secret identique muet", "borne_haute.py", [("        if t:\n            raise", "        if False:\n            raise")], "borne_haute"),
 ("M26 table 11 ferme-rejette lu conforme", "lien_epreuve_11.py", [("    if bras == FERME and devin_rejette:\n        return HARNAIS_FUIT", "    if bras == FERME and devin_rejette:\n        return CONFORME")], "lien_epreuve_11"),
 ("M27 test de mort 1 a >= 72", "puissance.py", [("    return rejets_sains > SEUIL_MORT_1", "    return rejets_sains >= SEUIL_MORT_1")], "puissance"),
 ("M28 source factice admise", "monde_plante.py", [("        if self.source == \"factice\":\n            raise", "        if False:\n            raise")], "monde_plante"),
 ("M29 garde de canaris sautee dans l'admission", ADM, [("    canaris = verifier_extracteur(extracteur, modele, canaux_visibles, list(CHAMPS_PRIVES),", "    canaris = {} or (lambda *a: {'saute': True})(extracteur, modele, canaux_visibles, list(CHAMPS_PRIVES),")], "admission"),
 ("M30 rejeu lecture racine egale admise", "tirage.py", [("            raise RefusDevin(\"racine de rejeu égale à la racine de la lecture\")", "            pass")], "tirage statistique"),
 ("M31 seuil temoin fuite 0,5", ADM, [("SEUIL_TEMOIN = 0.05", "SEUIL_TEMOIN = 0.5")], "admission"),
 ("M32 borne haute fausse a 0 difference", "borne_haute.py", [("        return 1 - (1 - niveau) ** (1 / N)", "        return 0.0")], "borne_haute"),
 ("M33 B < 999 admis (C1)", ADM, [("    if 1 / (B + 1) > SEUIL_FACTICE:", "    if False:")], "admission"),
 ("M34 racine du monde hors de la source (C2)", ADM, [("tirer_racine() if source_racines is None else source(f\"{cfg.nom}{suffixe_pli}:monde\")", "tirer_racine()")], "admission"),
 ("M35 taux du service a 0,5 (C15)", ADM, [("            taux = float(np.mean(np.asarray(cfg.lectures_temoins) > cfg.seuil_decision))", "            taux = 0.5")], "admission"),
 ("M36 empreinte sans le code (C16)", "monde_plante.py", [("             \"code\": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}", "             }")], "monde_plante"),
]


def preparer(ici: Path):
    if ici.exists():
        shutil.rmtree(ici)
    (ici / "src").mkdir(parents=True)
    (ici / "tests").mkdir()
    shutil.copytree(DEPOT / "src/controle_ia", ici / "src/controle_ia", ignore=shutil.ignore_patterns("__pycache__"))
    for f in (DEPOT / "tests").glob("test_devin_v2_*.py"):
        shutil.copy(f, ici / "tests" / f.name)
    shutil.copy(DEPOT / "pyproject.toml", ici / "pyproject.toml")
    (ici / "tests/conftest.py").write_text("# copie de mutation : conftest vide\n")
    shutil.copytree(ici / "src/controle_ia/devin_v2", ici / "orig_devin")


def lancer(ici: Path, cibles: str):
    fichiers = [f"tests/test_devin_v2_{c}.py" for c in cibles.split()]
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-p", "no:warnings", *fichiers],
                       cwd=ici, env=dict(os.environ, PYTHONPATH=str(ici / "src")), capture_output=True, text=True)
    sortie = r.stdout.strip().splitlines()
    return r.returncode, (sortie[-1] if sortie else r.stderr[-300:])


def main():
    ici = Path(sys.argv[1]).resolve()
    seul = sys.argv[2:]
    preparer(ici)
    d = ici / "src/controle_ia/devin_v2"
    # Le code chargé est celui de la copie : contrôle.
    r = subprocess.run([sys.executable, "-c", "import controle_ia.devin_v2 as m; print(m.__file__)"], cwd=ici,
                       env=dict(os.environ, PYTHONPATH=str(ici / "src")), capture_output=True, text=True)
    print("module chargé :", r.stdout.strip(), flush=True)
    for nom, f, paires, cibles in M:
        if seul and nom.split()[0] not in seul:
            continue
        shutil.rmtree(d)
        shutil.copytree(ici / "orig_devin", d)
        t = (d / f).read_text()
        ok = True
        for old, new in paires:
            if t.count(old) != 1:
                print(f"{nom}: MOTIF INTROUVABLE ({t.count(old)}) {old[:50]!r}", flush=True)
                ok = False
                break
            t = t.replace(old, new)
        if not ok:
            continue
        (d / f).write_text(t)
        rc, fin = lancer(ici, cibles)
        etat = "TUEE" if (rc != 0 and "failed" in fin) else ("SURVIT" if rc == 0 else "ERREUR")
        print(f"{nom}: {etat} — {fin}", flush=True)
    shutil.rmtree(d)
    shutil.copytree(ici / "orig_devin", d)
    rc, fin = lancer(ici, "graines tirage")
    print("contrôle sans mutation :", rc, fin, flush=True)


if __name__ == "__main__":
    main()
