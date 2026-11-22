"""Essai des essais, version 3 : altérations du code de l'addendum de concentration scellé (`entrees_v3`, `statistiques_v3`,
`lanceur_v4`), une à une. Chaque altération (garde retirée, borne confondue, précision changée) doit faire tomber au moins un
essai des fichiers d'essais neufs ; le fichier altéré est remis en l'état. Lancer depuis la racine du dépôt, `PYTHONPATH=src`."""
import subprocess
import sys
from pathlib import Path

B = Path("src/controle_ia/lentilles_sondes_bbis")
ESSAIS = ["tests/test_lentilles_sondes_bbis_garde_egalite_v1.py", "tests/test_lentilles_sondes_bbis_addendum_concentration_v2.py",
          "tests/test_lentilles_sondes_bbis_corrections_contre_lecture_v3.py"]
M = [
 # --- garde d'égalité (EC-6) ---
 ("statistiques_v3.py", "    egalite = bool(objet and haut.values[k - 1] == haut.values[k])", "    egalite = False"),
 ("statistiques_v3.py", "    egalite = bool(objet and haut.values[k - 1] == haut.values[k])", "    egalite = bool(objet and haut.values[k - 2] == haut.values[k - 1])"),
 ("statistiques_v3.py", "    objet = bool(valeurs.numel() >= k + 1)\n", "    objet = bool(valeurs.numel() >= k)\n"),
 ("statistiques_v3.py", "    if g[\"egalite\"]:\n        nom =", "    if False:\n        nom ="),
 ("statistiques_v3.py", "    marquee = (haut.values[k - 1] == haut.values[k]) if objet else torch.zeros(scores_nuls.shape[1], dtype=torch.bool)",
  "    marquee = torch.zeros(scores_nuls.shape[1], dtype=torch.bool)"),
 ("statistiques_v3.py", "    return base + max(0, places - (egaux - egaux_a_un)), base + min(places, egaux_a_un)", "    return base, base + min(places, egaux_a_un)"),
 ("statistiques_v3.py", "    return base + max(0, places - (egaux - egaux_a_un)), base + min(places, egaux_a_un)", "    return base + max(0, places - (egaux - egaux_a_un)), base + places"),
 ("statistiques_v3.py", "    depasse = valeurs > quantiles_sans_soi(scores_nuls, jetons[:, None], valeurs[:, None])[:, 0]", "    depasse = valeurs > scores_nuls[jetons].quantile(0.99, dim=1)"),
 ("statistiques_v3.py", "    return (float((1 + int((s_min >= int(valeur)).sum())) / (m + 1)), float((1 + int((s_max >= int(valeur)).sum())) / (m + 1)))",
  "    return (float((1 + int((s_max >= int(valeur)).sum())) / (m + 1)), float((1 + int((s_max >= int(valeur)).sum())) / (m + 1)))"),
 ("statistiques_v3.py", "    libres = comptes[~marquee]\n", "    libres = comptes\n"),
 ("statistiques_v3.py", "\"part\": compte / k, \"p_part\": p_part_haut,", "\"part\": compte / k, \"p_part\": p_part_bas,"),
 ("statistiques_v3.py", "                                  \"p\": p_haut, \"p_bas\": p_bas, \"p_haut\": p_haut}", "                                  \"p\": p_bas, \"p_bas\": p_bas, \"p_haut\": p_haut}"),
 ("statistiques_v3.py", "            hz = exiger_sans_egalite(z, k, LISTE_PAR_Z.format(nul=nom_nul), ids_gardes, contexte)", "            hz = premiers_gardes(z, k)"),
 ("statistiques_v3.py", "    haut = exiger_sans_egalite(a, k, LISTE_PAR_SCORE, ids_gardes, contexte)", "    haut = premiers_gardes(a, k)"),
 ("statistiques_v3.py", "    if a_bas != a_haut:\n", "    if False:\n"),
 ("statistiques_v3.py", "    a_bas, a_haut = regle(bas_i, bas_s), regle(haut_i, haut_s)", "    a_bas, a_haut = regle(haut_i, haut_s), regle(haut_i, haut_s)"),
 ("statistiques_v3.py", "    haut = exiger_sans_egalite(signes, k, LISTE_POLES, lambda i: f\"neurone {int(i) % f} signe {'+' if int(i) < f else '-'}\",\n                               contexte)",
  "    haut = premiers_gardes(signes, k)"),
 ("statistiques_v3.py", "    return haut[k - 1] == haut[k]\n", "    return haut[k - 1] != haut[k - 1]\n"),
 ("statistiques_v3.py", "\"paires_de_lignes_egales_octet_pour_octet\": int((groupes * (groupes - 1) // 2).sum()),", "\"paires_de_lignes_egales_octet_pour_octet\": int(groupes.size),"),
 # --- précision de la comparaison (C5) ---
 ("statistiques_v3.py", "    c32 = torch.as_tensor(c, dtype=torch.float32)\n    return float((1 + int((nulles >= c32).sum())) / (nulles.numel() + 1))",
  "    c32 = torch.as_tensor(c, dtype=torch.float64)\n    return float((1 + int((nulles.double() > c32).sum())) / (nulles.numel() + 1))"),
 ("statistiques_v3.py", "    if nulles.dtype != torch.float32:\n        raise Arret(\"concentration des directions nulles : simple précision attendue pour la comparaison à C(v)\")\n    c32",
  "    c32"),
 # --- statistique sans soi (EC-1, EC-2) : retour à la statistique d'origine ---
 ("statistiques_v3.py", "    concentration = concentrations_sans_soi(scores_nuls)\n", "    concentration = ((scores_nuls - moyenne[:, None]) / ecart[:, None]).max(0).values\n"),
 ("statistiques_v3.py", "    compte = (valeurs > quantiles_sans_soi(scores_nuls, rangs, valeurs)).sum(0).to(torch.int64)", "    compte = (valeurs > quantile[rangs]).sum(0).to(torch.int64)"),
 # --- clé de l'addendum (EC-4) ---
 ("entrees_v3.py", "    if not addenda:\n", "    if False:\n"),
 ("entrees_v3.py", "    if len(addenda) > 1:\n", "    if False:\n"),
 ("entrees_v3.py", "    if ligne.chemin != ADDENDUM or ligne.sha256 != EMPREINTE_ADDENDUM:\n", "    if False:\n"),
 ("entrees_v3.py", "    if chemin_de_la_fiche != ligne.chemin or sha256_de_la_fiche != ligne.sha256:\n", "    if False:\n"),
 ("entrees_v3.py", "        if autre_place < place or autre.heure < ligne.heure:\n", "        if autre.heure < ligne.heure:\n"),
 ("entrees_v3.py", "        if autre_place < place or autre.heure < ligne.heure:\n", "        if autre_place < place:\n"),
 ("entrees_v3.py", "    exiger_registre_propre(registre_propre)\n    return _v2.ouvrir_entrees(", "    return _v2.ouvrir_entrees("),
 ("entrees_v3.py", "    exiger_registre_propre(registre_propre)\n    return _v2.recuperer_entrees(", "    return _v2.recuperer_entrees("),
 ("entrees_v3.py", "EMPREINTE_ADDENDUM = \"7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970\"", "EMPREINTE_ADDENDUM = \"0a862760025caf11ff66578dc47c53143ee480c173a733920b9f4b9425d59546\""),
 # --- lanceur ---
 ("lanceur_v4.py", "    if not isinstance(porte, dict) or not isinstance(porte.get(\"chemin\"), str) or not isinstance(porte.get(\"sha256\"), str):\n        raise Refus(",
  "    if not isinstance(porte, dict):\n        porte = dict(ADDENDUM)\n    if False:\n        raise Refus("),
 ("lanceur_v4.py", "    ligne_addendum = en.exiger_addendum(registre_propre, porte[\"chemin\"], porte[\"sha256\"])", "    ligne_addendum = en.exiger_addendum(registre_propre, en.ADDENDUM, en.EMPREINTE_ADDENDUM)"),
 ("lanceur_v4.py", "            exiger_fiche_code(a.depot, a.registre_propre)       # code cité et clé de l'addendum, avant toute requête\n            en.recuperer_entrees(a.url, a.entrees, a.registre_bbis, a.registre_propre)",
  "            en._v2.recuperer_entrees(a.url, a.entrees, a.registre_bbis, a.registre_propre)"),
 ("lanceur_v4.py", "            haut = st.exiger_sans_egalite(scores[:, 0], K.K_JETONS_POLE,\n                                          st.LISTE_JETONS_POLE.format(neurone=p[\"neurone\"], signe=p[\"signe\"]),\n                                          self.charge.ids_gardes, ou | {\"signe\": \"+\", \"lentille\": K.LENTILLE_PUBLIQUE})",
  "            haut = st.premiers_gardes(scores[:, 0], K.K_JETONS_POLE)"),
 ("lanceur_v4.py", "                la_bas = st.exiger_sans_egalite(f * b, K.K_JETONS, st.LISTE_TEMOIN_DE_COUCHE.format(couche=autre),\n                                                self.charge.ids_gardes, ou)",
  "                la_bas = st.premiers_gardes(f * b, K.K_JETONS)"),
 ("lanceur_v4.py", "                        f[\"sur_representee\"] = st.libelle_sous_departage(st.sur_representee, f\"compte de la famille {nom}\", {\n                            \"isotrope\": (nul_iso, fi[\"p_bas\"], fi[\"p_haut\"], marquees[0]),\n                            \"signes\": (K.NUL_SIGNES, fs[\"p_bas\"], fs[\"p_haut\"], marquees[1])}, ou)",
  "                        f[\"sur_representee\"] = st.sur_representee(fi[\"p\"], fs[\"p\"])"),
 ("lanceur_v4.py", "        \"run\": ctx.run, \"texte\": {\"chemin\": K.TEXTE, \"sha256\": K.EMPREINTE_TEXTE}, \"addendum\": dict(ADDENDUM),\n        \"entrees\":",
  "        \"run\": ctx.run, \"texte\": {\"chemin\": K.TEXTE, \"sha256\": K.EMPREINTE_TEXTE},\n        \"entrees\":"),
 ("lanceur_v4.py", "                 \"preenregistrement\": {\"chemin\": K.TEXTE, \"sha256\": K.EMPREINTE_TEXTE}, \"addendum\": dict(ADDENDUM),", "                 \"preenregistrement\": {\"chemin\": K.TEXTE, \"sha256\": K.EMPREINTE_TEXTE},"),
 ("lanceur_v4.py", "    rapport[\"lignes_de_sortie_egales\"] = st.paires_de_lignes_egales(_np(charge.wu))\n", "    pass\n"),
 ("lanceur_v4.py", "    if not rapport_montage.is_file():\n        raise Arret(\"rapport du montage absent", "    if False:\n        raise Arret(\"rapport du montage absent"),
 ("lanceur_v4.py", "            c[\"temoins_a_egalite_au_vingtieme_rang\"] += e[\"a_egalite_au_vingtieme_rang\"]\n", "            pass\n"),
 ("lanceur_v4.py", "            c[\"directions_nulles_marquees\"] += resume.n_marquees\n", "            pass\n"),
]
ko = 0
for fichier, avant, apres in M:
    p = B / fichier
    source = p.read_text(encoding="utf-8")
    if source.count(avant) != 1:
        print("MOTIF INTROUVABLE OU MULTIPLE :", fichier, "|", avant[:70].replace("\n", " "))
        ko += 1
        continue
    p.write_text(source.replace(avant, apres), encoding="utf-8")
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *ESSAIS], capture_output=True, text=True)
    finally:
        p.write_text(source, encoding="utf-8")
    vu = r.returncode != 0
    ko += not vu
    premier = next((l for l in r.stdout.splitlines() if l.startswith("FAILED") or l.startswith("ERROR")), "")
    print("vue    " if vu else "NON VUE", fichier, "|", avant[:70].replace("\n", " "), "|", premier[:150])
print("altérations non vues ou introuvables :", ko, "sur", len(M))
