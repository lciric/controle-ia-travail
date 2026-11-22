"""Mutations du lot 11, v3 : chaque garde cassée doit faire tomber au moins un essai. T0 (témoin non muté) doit survivre."""
import json, os, shutil, subprocess, sys, tempfile
ICI = os.path.dirname(os.path.abspath(__file__))
PY = "/home/user/controle-ia-travail/.venv/bin/python"
M = [
    ("T0", None, None),
    ("G1 empreinte", 'if sha(b) != EMPREINTES_TEXTES[nom]:', 'if False:'),
    ("G1 motifs", '        if garde_motifs_ligne(ligne):', '        if False:'),
    ("G2 compagnon", "or open(comp).read().split()[0] != sha(b)", ""),
    ("G2 extras", 'if not set(m.get("extras", {})) <= EXTRAS_PERMIS[p["fournisseur"]]:', 'if False:'),
    ("G3 GO", 'raise Refus(f"G3 : {g} absent du registre")', 'pass'),
    ("G5 pire", 'if pire(m, len(b)) > PIRE_TENTATIVE:', 'if False:'),
    ("G6 garde Google", '    if pb:\n        raise Refus("G6', '    if False:\n        raise Refus("G6'),
    ("G6 défaut Google", 'if GG.defaut_reponse_google(r["fin"], r["texte"], r["pensee_jetons"], blocage=r["blocage"]):', 'if False:'),
    ("G7 sous-part", 'if self.cumul[cle] + self.en_vol[cle] + p_t > D(str(self.c["sous_parts"][cle])) or total + p_t > self.p_x:', 'if False:'),
    ("G7 somme", 'if sum(D(str(v)) for v in c["sous_parts"].values()) > P_X_FORMES[c["forme"]]:', 'if False:'),
    ("G8 arrêt 13", '            self.arret_13.set()', '            pass'),
    ("G8 crédit", 'r["credit"] = r["credit"] or bool(MOTIFS_CREDIT.search(r["erreur"] + " " + str(err.get("message", ""))))', 'r["credit"] = False'),
    ("G9 repli", 'if classe != "refus du modèle (classifieur)":', 'if True:'),
    ("G9 refus", 'elif fournisseur == "anthropic" and r["fin"] == "refusal":', 'elif False:'),
    ("G9 par_repli", '"par_repli": rang > 0', '"par_repli": False'),
    ("G10 écrasement", 'with open(chemin, "xb") as brut:', 'with open(chemin, "wb") as brut:'),
    ("G11 clé", 'raise Refus(f"G11 : clé {p[\'cle_var\']} absente")', 'pass'),
    ("G12 substitué", 'if not modele_conforme(m, servi):', 'if False:'),
    ("A3 pire", '        return pire_t, True\n', '        return D(0), True\n'),
    ("illisible", 'elif r["fin"] not in ("end_turn", "stop") or not r["texte"].strip():', 'elif False:'),
    ("texte au journal", 'texte_signes=len((r or {}).get("texte") or ""),', 'texte_signes=(r or {}).get("texte"),'),
    ("B1 couverture", 'raise Refus("G4 : couple non éprouvé par la garde de départ : "', 'print("G4 : couple non éprouvé par la garde de départ : "'),
    ("B1 rendu", 'and l["verdict"] != "prêt":', 'and False:'),
    ("B2 sans fin", 'elif r["erreur"] or r["fin"] is None:', 'elif False:'),
    ("B3 fin", 'fin=fin if fin in FINS else ("absente" if fin is None else "autre"),', 'fin=fin,'),
    ("B3 modèle", 'modele_servi=servi if modele_conforme(maillon["modele"], servi) else', 'modele_servi=servi if True else'),
    ("B4 exceptions", 'except Exception as e:  # B4', 'except (OSError, TimeoutError, ValueError) as e:  # B4'),
    ("R1 corps brut", 'return e.code, iter([{"error": {"type": typ or "erreur", "message": texte[:8000]}}])', 'return e.code, iter([{"error": {"type": typ or "erreur"}}])'),
    ("R2 suffixe", 'SUFFIXE_MODELE = r"-(\\d{8}|\\d{4}-\\d{2}-\\d{2}|v?\\d{1,3})"', 'SUFFIXE_MODELE = r"-.*"'),
    ("R3 envoi", 'self._ecrire(dict(base, type_ligne="envoi"', 'self.lignes.append(dict(base, type_ligne="envoi_non_ecrit"'),
    ("R4 dépôts", 'if os.path.exists(o.quarantaine) or not hors_des_depots(o.quarantaine):', 'if os.path.exists(o.quarantaine):'),
    ("R5 6,05", 'p_t = PIRE_TENTATIVE  # R5', 'p_t = pire(maillon, len(self.textes["piece"]))  # R5'),
    ("R6 verrou", '            if self.arret_13.is_set():  # R6', '            if False:  # R6'),
    ("R7 redirection", '_OUVREUR = urllib.request.build_opener(_SansRedirection)', '_OUVREUR = urllib.request.build_opener()'),
    ("R8 Kimi", 'if isinstance(ch.get("usage"), dict):  # R8', 'if False:  # R8'),
    ("G4b ordre", 'or list(ef) != sorted(ef, key=EFFORTS_PERMIS[p["fournisseur"]].index):', ':'),
    ("G4b premier admis", '                        retenu = e\n                        break', '                        retenu = e'),
    ("G4b autre statut", 'if statut != 400:', 'if False:'),
    ("v3 texte servi", 'piece = self.textes[nom_texte]', 'piece = self.textes["piece"]'),
    ("v3 forme des morceaux", 'if sorted(ts) != attendu:', 'if False:'),
    ("v3 morceau hors Google", 'if c["forme"] != "decoupe_google" or p["fournisseur"] != "google":', 'if False:'),
    ("v3 P_X de la forme", '"decoupe_google": D("139.15")}', '"decoupe_google": D("999")}'),
    ("v3 lecture des textes", 'return {nom: verifier_piece(os.path.join(dossier, f), nom) for nom, f in FICHIERS_TEXTES.items()}', 'return {nom: open(os.path.join(dossier, f), "rb").read() for nom, f in FICHIERS_TEXTES.items()}'),
]
src = open(os.path.join(ICI, "passe_x_na_v3.py")).read()
res = []
for nom, a, b in M:
    d = tempfile.mkdtemp()
    s = src
    if a is not None:
        assert s.count(a) == 1, nom
        s = s.replace(a, b)
    open(os.path.join(d, "passe_x_na_v3.py"), "w").write(s)
    shutil.copy(os.path.join(ICI, "test_passe_x_na_v3.py"), d)
    p = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "test_passe_x_na_v3.py"],
                       cwd=d, capture_output=True, text=True, env={"PATH": os.environ["PATH"]})
    res.append({"mutation": nom, "issue": "survit" if p.returncode == 0 else "tuée"})
    shutil.rmtree(d)
ok = res[0]["issue"] == "survit" and all(r["issue"] == "tuée" for r in res[1:])
print(json.dumps({"mutations": res, "conforme": ok}, ensure_ascii=False, indent=1))
sys.exit(0 if ok else 1)
