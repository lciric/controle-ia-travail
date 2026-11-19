"""Essai des essais du contre-lecteur : une garde retirée (ou un seuil faussé) à la fois, sur la copie extraite du commit
128810af ; chaque fichier est remis en l'état après l'essai. Usage : python mutations_v1.py RACINE_ARBRE PYTHON [rapide|lent]."""
import subprocess
import sys
from pathlib import Path

RACINE, PY, LOT = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
B = RACINE / "src/controle_ia/lentilles_sondes_bbis"
RAPIDES = ["entrees", "montage", "lecture", "nuls_statistiques"]
LENT = ["procedure"]

M_RAPIDES = [
 # entrées
 ("entrees_v1.py", 'if vue.champ("run_id") != run:', "if False:"),
 ("entrees_v1.py", 'if vue.cles("sources") != sorted(K.CELLULES):', "if False:"),
 ("entrees_v1.py", 'if champs_sonde or vue.present(*src, "enc") or presents:', "if False:"),
 ("entrees_v1.py", 'if vue.present(*src, "enc", "reglage") or vue.present(*src, "enc", "empreinte") or entrees_enc:', "if False:"),
 ("entrees_v1.py", "                self._npz.close()\n                raise FormeMalComprise", "                pass\n                if False: raise FormeMalComprise"),
 ("entrees_v1.py", "    if str(chemin_relatif) not in set(chemins_permis(run).values()):", "    if False:"),
 ("entrees_v1.py", "if sha_e2 != _compagnon(racine, ch[\"e2_compagnon\"], course.run) or sha_e2 != course.sha256_e2:", "if False:"),
 ("entrees_v1.py", "if scellement.chemin != K.TEXTE or scellement.sha256 != K.EMPREINTE_TEXTE:", "if False:"),
 ("entrees_v1.py", "    if isinstance(couche, bool) or not isinstance(couche, int) or couche not in K.COUCHES:", "    if False:"),
 ("entrees_v1.py", "    if famille not in K.FAMILLES:", "    if False:"),
 ("entrees_v1.py", "    if ch[\"e2\"] != course.chemin_e2:", "    if False:"),
 ("entrees_v1.py", "    if vue.champ(\"fichier_sondes\", \"fichier\") != ch[\"e1\"]:", "    if False:"),
 ("entrees_v1.py", "if vue.champ(*src, \"cellule\") != cellule or vue.champ(*src, \"pli_lu\") != int(pli[1]):", "if False:"),
 ("entrees_v1.py", "if empreinte_sonde(fam_e, nom_e, couche_e, agr_e, we, be, qe) != att_e:", "if False:"),
 ("entrees_v1.py", "    if registre.name == K.REGISTRE_INTERDIT:\n        raise Refus(f\"{registre.name} : registre jamais lu", "    if False:\n        raise Refus(f\"{registre.name} : registre jamais lu"),
 ("entrees_v1.py", "        if cellules[0] == \"VERDICT-BBIS\":\n            sortie[cellules[0]].append(LigneRegistre(cellules[0], cellules[1], None, None))\n            continue", "        pass"),
 ("entrees_v1.py", "    if b.shape != (1,) or b.dtype.kind != \"f\":", "    if False:"),
 # montage
 ("montage_v1.py", "    if \"target_layer\" in prov and prov[\"target_layer\"] != cible:", "    if False:"),
 ("montage_v1.py", "    if not isinstance(prov, dict) or \"capture_point\" not in prov:", "    if not isinstance(prov, dict):"),
 ("montage_v1.py", "    if not ok or sorted(J) != list(couches):", "    if not ok:"),
 ("montage_v1.py", "    if len(contenu) != int(taille) or identifiant_git(contenu) != identifiant:", "    if len(contenu) != int(taille):"),
 ("montage_v1.py", "        if (c.sorte == \"octet\" and len(recu) != 1) or (c.sorte != \"octet\" and len(recu) < 1):", "        if False:"),
 ("montage_v1.py", "        if not p.is_file() or sha256_fichier(p) != attendue:", "        if not p.is_file():"),
 ("montage_v1.py", "    if sha256_fichier(copie_versee) != sha256_copie:", "    if False:"),
 ("montage_v1.py", "    if tete != commit:", "    if False:"),
 ("montage_v1.py", "    if n != int(taille) or h.hexdigest() != sha256:\n        Path(chemin).unlink", "    if n != int(taille):\n        Path(chemin).unlink"),
 ("montage_v1.py", "    if manquants:", "    if False:"),
 ("montage_v1.py", "            if not url.startswith(HOTE_HF + \"/\"):", "            if False:"),
 ("montage_v1.py", "    if str(env.get(\"HF_DEBUG\", \"\")).strip().lower() not in (\"\", \"0\", \"false\", \"no\", \"off\"):", "    if False:"),
 ("montage_v1.py", "    if \"d_model\" in prov and prov[\"d_model\"] != largeur:", "    if False:"),
 ("montage_v1.py", "        if not isinstance(sl, (list, tuple, range)) or [int(x) for x in sl] != list(couches):", "        if False:"),
 ("montage_v1.py", "              and all(p.stat().st_size == self.description[nom][\"octets\"] for nom, p in partiels.items()))", "              )"),
 ("montage_v1.py", "    if lu.get(\"modele\") != K.DEPOT_LLAMA or len(lu[\"ids\"]) != len(lu[\"chaines\"]):", "    if False:"),
 ("montage_v1.py", "    if sortie.exists():\n        raise Arret(\"jetons gardés déjà calculés", "    if False:\n        raise Arret(\"jetons gardés déjà calculés"),
 # lecture
 ("lecture_v1.py", "        if all(abs(float(scores[i, j]) - seuil) <= K.TOLERANCE_EGALITE_GARDE * abs(seuil) for i in a ^ b):", "        if True:"),
 ("lecture_v1.py", "    if jacobienne.dtype != torch.float32 or jacobienne.shape != (v.shape[0], v.shape[0]):", "    if False:"),
 ("lecture_v1.py", "    if wu.dtype != torch.float32:", "    if False:"),
 ("lecture_v1.py", "        raise Arret(\"lentille publique absente : arrêt ; la lecture par la seule lentille des logits n'est pas rendue\")", "        return None, int(couche), \"identite\""),
 # nuls et statistiques
 ("nuls_v1.py", "    eps = rng.integers(0, 2, size=(int(n), v.shape[0]), dtype=np.int8) * 2 - 1", "    eps = rng.integers(0, 2, size=(int(n), v.shape[0]), dtype=np.int8) * 0 + 1"),
 ("nuls_v1.py", "    return u * np.sqrt(np.mean(np.asarray(v, np.float64) ** 2))", "    return u"),
 ("nuls_v1.py", "        return f\"lentilles-bbis/temoins-calibration/{int(couche)}/{nul}/couche\"", "        return f\"lentilles-bbis/nul-isotrope/{int(couche)}\""),
 ("statistiques_v1.py", "    if s.lower() in _COUT:", "    if False:"),
 ("statistiques_v1.py", "    if not bool((ecart > 0).all()):", "    if False:"),
 ("statistiques_v1.py", "    au_moins = resume.m - torch.searchsorted(nuls, c, right=False)", "    au_moins = resume.m - torch.searchsorted(nuls, c, right=True)"),
 ("statistiques_v1.py", "    part = (haut.values > quantile[haut.indices]).float().mean(0)", "    part = (haut.values >= quantile[haut.indices]).float().mean(0)"),
 ("statistiques_v1.py", "    if p_iso > K.P_NON_DISTINCTE or p_signes > K.P_NON_DISTINCTE:", "    if p_iso > K.P_NON_DISTINCTE and p_signes > K.P_NON_DISTINCTE:"),
 ("statistiques_v1.py", "    return bool(p_iso <= K.P_FAMILLE and p_signes <= K.P_FAMILLE)", "    return bool(p_iso <= K.P_FAMILLE)"),
 ("statistiques_v1.py", "    c_max = float(cos.abs().max())", "    c_max = float(cos.max())"),
 ("audits_v1.py", "        if cumul <= niveau:", "        if cumul < niveau / 2:"),
 ("audits_v1.py", "            \"attendu\": n * a / (m + 1), \"tenue\": bool(bas <= compte <= haut),", "            \"attendu\": n * a / (m + 1), \"tenue\": True,"),
 ("audits_v1.py", "    proches = [c for c in cosinus_paires if c[\"type\"] in (\"plis\", \"doses\") and c[\"cosinus\"] > K.SEUIL_COS_DIRECTIONS]", "    proches = []"),
 ("audits_v1.py", "    jumeaux = [c for c in cosinus_paires if c[\"type\"] == \"sonde-lecteur\" and c[\"cosinus\"] > K.SEUIL_COS_SONDE_LECTEUR]", "    jumeaux = []"),
 ("audits_v1.py", "                   if len(d) == 2 and d[K.LENTILLE_PUBLIQUE] == d[K.LENTILLE_LOGITS])", "                   if False)"),
 ("audits_v1.py", "        if l[\"couche\"] in (7, 15) and l.get(\"ids\") is not None:", "        if l.get(\"ids\") is not None:"),
 ("phrases_v1.py", "    if libelle == st.LIBELLE_INTERMEDIAIRE:\n        return None", "    if False:\n        return None"),
 ("lanceur_v1.py", "    if libre < int(minimum):", "    if False:"),
 ("lanceur_v1.py", "    if not (travail / MARQUE).is_file():\n        raise Arret(f\"{travail} ne porte pas", "    if False:\n        raise Arret(f\"{travail} ne porte pas"),
 ("lanceur_v1.py", "    if cle not in K.CLES_PROPRES:", "    if False:"),
]

M_LENTS = [
 ("lanceur_v1.py", "    if ctx.travail.exists():\n        raise Arret(f\"{ctx.travail} existe déjà", "    if False:\n        raise Arret(f\"{ctx.travail} existe déjà"),
 ("lanceur_v1.py", "    mo.aucune_occurrence([ctx.travail, ctx.sortie], cle)\n    horloge.consigner()", "    horloge.consigner()"),
 ("lanceur_v1.py", "            hors = [nul for nul in (nul_iso, K.NUL_SIGNES) if not cal[nul][\"tenue\"]]", "            hors = []"),
 ("lanceur_v1.py", "    if not chemin_etat.is_file():", "    if False:"),
 ("lanceur_v1.py", "        if chemin.exists():\n            raise Arret(f\"{chemin} existe déjà (R12)\")\n    charge", "        pass\n    charge"),
 ("lanceur_v1.py", "    toutes = (len(apprises)", "    toutes = False and (len(apprises)"),
 ("lanceur_v1.py", "                    lecture[\"signes\"][s][\"nuls\"][K.NUL_ISOTROPE][\"remplacee\"] = True\n", ""),
 ("lanceur_v1.py", "        d[\"poles\"][\"libelle\"] = st.libelle(p[nul_iso], p[K.NUL_SIGNES])", "        d[\"poles\"][\"libelle\"] = st.libelle(p[K.NUL_ISOTROPE + ('_remplacee' if nul_iso != K.NUL_ISOTROPE else '')], p[K.NUL_SIGNES])"),
 ("lanceur_v1.py", "        self.horloge.controler(f\"couche {c}, {sonde.cle}/{nom_v}\")\n", ""),
 ("lanceur_v1.py", "            self.controle_disque()\n", ""),
]
# la mutation « toutes = False » vise audits_v1 en réalité
M_LENTS = [(("audits_v1.py",) + m[1:]) if m[1].startswith("    toutes = (len") else m for m in M_LENTS]

mutations = M_RAPIDES if LOT == "rapide" else M_LENTS
essais = RAPIDES if LOT == "rapide" else RAPIDES + LENT
non_vues = 0
for fichier, avant, apres in mutations:
    p = B / fichier
    source = p.read_text()
    if source.count(avant) != 1:
        print("MOTIF INTROUVABLE OU MULTIPLE :", fichier, avant[:70].replace("\n", " "), flush=True)
        continue
    p.write_text(source.replace(avant, apres))
    try:
        r = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider"]
                           + [f"tests/test_lentilles_sondes_bbis_{e}_v1.py" for e in essais],
                           cwd=RACINE, capture_output=True, text=True, env={**__import__("os").environ, "PYTHONPATH": "src"})
    finally:
        p.write_text(source)
    vu = r.returncode != 0
    non_vues += not vu
    print("vue    " if vu else "SURVIT ", fichier, "|", avant.strip()[:90].replace("\n", " "), flush=True)
print("altérations qui survivent :", non_vues, "sur", len(mutations), flush=True)
