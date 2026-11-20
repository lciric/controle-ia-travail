"""Contrôle « trop beau » (règle R4) : des défauts réintroduits un par un dans une copie du code, et l'essai qui doit les voir.

Pour chaque défaut : copie neuve de `src/` sous le dossier de travail, remplacements exacts (chacun doit se trouver une seule fois,
sinon le défaut est « non appliqué »), puis les essais nommés, lancés par `python3 -B -m pytest`. Un défaut est « vu » si les
essais échouent. Avant tout défaut, chaque sélection d'essais est jouée sur le code sain et doit passer (« témoin »). Sortie : un
fichier JSON. Arguments : bloc-notes, dossier de travail neuf, fichier de sortie, puis, en option, les identifiants à jouer.
Aucun réseau ; graines « essai » des essais eux-mêmes.

Version 2 (code v3) : les 41 défauts de la version 1, repris à l'identique, et neuf de plus — C1 (refus d'une couche
décisive non consigné, vu par l'essai final joué seul : un ; aucun défaut n'ouvre le verrou, ce qui ferait dériver une graine
décisive), C2 (la copie servie au bras 4b : cinq), C3 (la strate du passage exigée sans besoin : un), notes D4 (table des
gardes incomplète acceptée : un) et D7 (compteurs du jeu perdus : un)."""

import json
import os
import shutil
import subprocess
import sys
import time

BLOC, TRAVAIL, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
SEULS = set(sys.argv[4:])
PAQUET = os.path.join("controle_ia", "heritage_etage_processeur_v1")
T = os.path.join(BLOC, "tests")


def t(nom, k=None):
    return (os.path.join(T, f"test_heritage_etage_processeur_v1_{nom}.py"), k)


DEFAUTS = [
    ("rangs-zeros-retires-avant", "test exact : zéros retirés avant de classer (garde 21)", "rangs_signes.py",
     [("    d = np.asarray(d, dtype=float)\n    a = np.abs(d)", "    d = np.asarray(d, dtype=float)\n    d = d[d != 0]\n    a = np.abs(d)")],
     [t("outils", "exact or garde_21")]),
    ("holm-premiere-marche-a-0-05", "Holm : la première marche lue à 0,05", "rangs_signes.py",
     [("        premier = p_heritage <= alpha / 2", "        premier = p_heritage <= alpha")], [t("outils", "holm")]),
    ("lecture-sans-condition-des-fausses", "M5 : condition des lois fausses sans « strictement inférieure »", "rangs_signes.py",
     [("    return mf <= 1.0 and mf < mv", "    return mf <= 1.0")], [t("outils", "holm")]),
    ("tenue-sur-entrees-etrangeres", "bras 4b : multiplicateur de la tenue sur les entrées étrangères (défaut du dossier versé)",
     "proposeurs.py",
     [('    return p["origine"] == ("course-source" if bras == "source" else "continuation") and p["source"] == f"source-{source}" \\\n'
       '        and p["bras"] == f"bras-{bras}"',
       '    return p["origine"] == ("course-source" if bras == "source" else "continuation")')], [t("mecanique", "garde_27")]),
    ("lecteur-compose-en-course-source", "le lecteur compose ses propres entrées dans la course source (annexe F, point 3)",
     "proposeurs.py",
     [('    compo = [] if bras == "source" else tentatives_du_lecteur(prop, vue, monde, parts, n_tentatives, rng, repli, mesure)',
       "    compo = tentatives_du_lecteur(prop, vue, monde, parts, n_tentatives, rng, repli, mesure)")],
     [t("mecanique", "course_source")]),
    ("strate-vide-repli-regroupe", "strate vide : repli silencieux sur la fréquence regroupée (au lieu d'un arrêt)", "frequences.py",
     [("    if vides:\n        raise ArretFrequences(", "    if False:\n        raise ArretFrequences(")], []),
    ("frequence-source-egale-cible", "la fréquence des lois vraies du monde source prise sur celle des mondes cibles",
     "statistique.py",
     [('        self.tient_src_v = rng.random((S, DOMAINES_A_LOI_SOURCE)) < _f(f, "p_tient_vraie_source")',
       '        self.tient_src_v = rng.random((S, DOMAINES_A_LOI_SOURCE)) < _f(f, "p_tient_vraie_cible")')],
     [t("statistique", "frequence_d_une_loi_vraie")]),
    ("double-balisage", "description balisée une seconde fois dans la fiche (annexe F, point 5)", "registre.py",
     [('    hyp = t["description"] if liste == "avec_description" else HYPOTHESE_NEUTRE',
       '    hyp = DEBUT_DONNEES + "\\n" + t["description"] + "\\n" + FIN_DONNEES if liste == "avec_description" else HYPOTHESE_NEUTRE')],
     [t("gardes", "garde_11")]),
    ("seuil-compare-a-l-envers", "seuil comparé dans l'autre sens (garde 17)", "executeur.py",
     [('    return {"≥": valeur >= seuil,', '    return {"≥": valeur <= seuil,')], [t("organisme", "garde_17")]),
    ("retrait-des-plus-chers", "règle de retrait : les appels les plus chers d'abord (garde 18)", "cout.py",
     [("    restant = float(cout.sum())\n    retires = []\n    for a in permutation:",
       "    restant = float(cout.sum())\n    retires = []\n    for a in [int(x) for x in np.argsort(-cout, kind=\"stable\")]:")],
     [t("gardes", "garde_18")]),
    ("meme-graine-d-echantillonnage", "même graine d'échantillonnage dans tous les bras (garde 20)", "mecanique.py",
     [('    etiq = ctx.etiquette(bras=bras, generation=generation, role="echantillonnage")',
       '    etiq = ctx.etiquette(generation=generation, role="echantillonnage")')], [t("mecanique", "reproductibilite")]),
    ("ecriture-en-generation-finale", "écriture du registre pendant la génération finale (garde 9)", "mecanique.py",
     [("        if not finale:\n            registre.ajouter(", "        if True:\n            registre.ajouter(")],
     [t("mecanique", "reproductibilite")]),
    ("tranche-servie", "une ligne de la tranche d'épreuve dans la part servie (garde 10)", "mondes.py",
     [("    return np.sort(perm[:k]), np.sort(perm[k:])", "    return np.sort(perm[:k + 1]), np.sort(perm[k:])")],
     [t("gardes", "garde_10")]),
    ("comparateur-lit-la-promotion", "le comparateur lit la promotion (garde 12)", "comparateur.py",
     [('    eng = tentative["engagement"]\n', '    eng = tentative["engagement"]\n    if not tentative.get("promue", True):\n'
       '        return None\n')], [t("gardes", "garde_12")]),
    ("clopper-pearson-unilateral", "intervalle binomial : niveau mal partagé entre les deux queues", "intervalles.py",
     [("        a = (1.0 - niveau) / 2.0", "        a = (1.0 - niveau)")], [t("outils", "intervalle")]),
    ("grain-ouvert", "garde 7 : tout nombre permis dans le registre et le retour", "registre.py",
     [('    return (len(chemin) == 2 and chemin[0] == "prediction") or chemin[-1:] == ("cout_usd",)', "    return True")],
     [t("gardes", "garde_7")]),
    ("epreuve-sans-empreinte", "garde 3 : épreuve d'une tentative sans empreinte de prédiction", "executeur.py",
     [("        if not prediction_sha256:\n", "        if False:\n")], [t("gardes", "garde_3")]),
    ("chaine-non-verifiee", "garde 4 : chaîne d'empreintes non vérifiée", "registre.py",
     [('            if e.get("empreinte_precedente") != precedente or e.get("empreinte") != _empreinte_entree(e, precedente):',
       "            if False:")], [t("gardes", "garde_4")]),
    ("historique-accepte", "garde 5 : historique de départ non vide accepté", "registre.py",
     [("    if historique:\n", "    if False:\n")], [t("gardes", "garde_5")]),
    ("bras-1-servi", "garde 8 : champs du bras 1 servis", "registre.py",
     [('    if bras == "1" and servi:\n', "    if False:\n")], [t("gardes", "garde_8")]),
    ("cloisonnement-ouvert", "garde 6 : chemin d'un autre bras servi sans arrêt", "registre.py",
     [("            if forme and forme in texte:\n", "            if False:\n")], [t("gardes", "garde_6")]),
    ("juge-lit-le-registre", "garde 2 : champ du registre accepté chez un juge", "registre.py",
     [("    if trouves:\n", "    if False:\n")], [t("gardes", "garde_2")]),
    ("seuil-sens-ignore", "garde 15 : seul le nombre du seuil relu, non son sens", "executeur.py",
     [("    if lu != tuple(voulu):\n", "    if lu[0] != voulu[0]:\n")], [t("gardes", "garde_15")]),
    ("contre-calcul-lache", "garde 16 : contre-calcul sans prise", "executeur.py",
     [("    if abs(mienne - valeur) > TOLERANCE_CONTRE_CALCUL:\n", "    if abs(mienne - valeur) > 1e9:\n")],
     [t("gardes", "garde_16")]),
    ("taux-inegaux-acceptes", "garde 19 : taux d'échec différents entre bras acceptés", "enveloppe.py",
     [("    if len(set(float(t) for t in taux_par_bras.values())) != 1:\n",
       "    if len(set(float(t) for t in taux_par_bras.values())) > 3:\n")], [t("gardes", "garde_19")]),
    ("budget-en-echec", "garde 14 : « non éprouvée (budget) » compté comme une classe d'échec", "registre.py",
     [('    return {"classe": NON_EPROUVEE, "cout_usd": float(cout_usd)}', '    return {"classe": CLASSES[2], "cout_usd": float(cout_usd)}')],
     [t("gardes", "garde_14")]),
    ("verrou-d-etalonnage-ouvert", "garde 22 : le test appelable pendant l'étalonnage", "etalonnage.py",
     [('    RS.VERROU_ETALONNAGE["leve"] = True\n', '    RS.VERROU_ETALONNAGE["leve"] = False\n')],
     [t("statistique", "garde_22")]),
    ("confirmation-stricte", "garde 26 : échec de confirmation au-delà de 5 236 seulement", "intervalles.py",
     [('    return "en échec" if rejets_sur_100000 >= COMPTE_D_ECHEC_DE_CONFIRMATION else "tenue"',
       '    return "en échec" if rejets_sur_100000 > COMPTE_D_ECHEC_DE_CONFIRMATION else "tenue"')], [t("outils", "garde_26")]),
    ("registre-propre-au-bras-4a", "garde 27 : le registre de la source propre accepté au bras 4a", "registre.py",
     [("        if sha_registre_servi_au_depart == sha_registre_source_propre:\n", "        if False:\n")],
     [t("mecanique", "garde_27")]),
    ("bornes-ignorees", "garde 25 : bornes de la construction ignorées (toujours les bornes gelées)", "mondes.py",
     [("        self.tirages_par_loi, self.essais_par_monde, self.tours_par_suite = tirages_par_loi, essais_par_monde, tours_par_suite",
       "        self.tirages_par_loi, self.essais_par_monde, self.tours_par_suite = TIRAGES_PAR_LOI, ESSAIS_PAR_MONDE, TOURS_PAR_SUITE")],
     [t("mondes", "bornes")]),
    ("traits-de-contenu-nuls", "garde 25 : traits de contenu non lus", "audit.py",
     [("    return np.array(out)\n", "    return np.zeros(6)\n")], [t("mondes", "poids_des_dependantes")]),
    ("marge-non-relue", "garde 25 : l'audit des marges ne voit plus deux lois trop proches", "audit.py",
     [("        s = separation(pr(lois_du_monde[a]), pr(lois_du_monde[b]))\n        if s < seuil:",
       "        s = separation(pr(lois_du_monde[a]), pr(lois_du_monde[b]))\n        if s < -1.0:")], [t("mondes", "trop_proches")]),
    ("exclu-jamais", "garde 13 : ensemble exclu jamais rempli", "mondes.py",
     [('            if finale.oracle.divergence(l["loi"], loi) <= seuil:', '            if finale.oracle.divergence(l["loi"], loi) < 0.0:')],
     [t("mecanique", "garde_13")]),
    ("organisme-elimine-tient", "garde 17 : « éliminée » de l'organisme lue « tient »", "organisme.py",
     [('CORRESPONDANCE_VERDICTS = {"survit": TIENT, "éliminée": NE_TIENT_PAS,',
       'CORRESPONDANCE_VERDICTS = {"survit": TIENT, "éliminée": TIENT,')], [t("organisme", "garde_17")]),
    ("s8-i-sans-prise", "garde 24 : S8 (i) sans prise sur les lois fausses", "frequences.py",
     [("    if not (vs >= SEUIL_S8_I and vc >= SEUIL_S8_I and fa <= SEUIL_S8_I):",
       "    if not (vs >= SEUIL_S8_I and vc >= SEUIL_S8_I and fa <= 1.0):")], [t("mecanique", "garde_24")]),
    ("s8-ii-sans-prise", "garde 23 : S8 (ii) sans arrêt", "equivalence.py",
     [("        if not (bas <= moy <= haut):\n", "        if False:\n")], [t("mecanique", "garde_23")]),
    ("graines-des-bras-non-verifiees", "garde 20 : graines des bras non vérifiées", "graines.py",
     [("            if cle in vues and vues[cle] != b:\n", "            if False:\n")], [t("outils", "garde_20")]),
    ("m10-valeur-absolue", "M10 : la valeur absolue de I retirée de la part, au lieu de son seul côté positif", "analyse.py",
     [("    return ecart_dependantes / (ecart_dependantes + max(ecart_independantes, 0.0))",
       "    return ecart_dependantes / (ecart_dependantes + abs(ecart_independantes))")], [t("statistique", "regles_de_lecture")]),
    ("s9-rapport-strict", "S9 : rapport d'une fois et demie lu strictement", "analyse.py",
     [("    return \"remplie\" if (n2 - n1 >= BEAUCOUP_PLUS_ECART and n2 >= BEAUCOUP_PLUS_RAPPORT * n1) else \"non remplie\"",
       "    return \"remplie\" if (n2 - n1 >= BEAUCOUP_PLUS_ECART and n2 > BEAUCOUP_PLUS_RAPPORT * n1) else \"non remplie\"")],
     [t("outils", "s9")]),
    ("atteint-sans-les-suivants", "C2 et C3 : « atteint » lu sans exiger tous les nombres suivants", "analyse.py",
     [("        if v is None or v < seuil:\n            break\n", "        if v is None or v < seuil:\n            continue\n")],
     [t("statistique", "regles_de_lecture")]),
    ("sorties-non-verifiees", "analyse : sorties relues sans vérifier leur sceau", "analyse.py",
     [("        if _sha256(chemin) != attendu:\n", "        if False:\n")], [t("statistique", "reproductibilite")]),
    # --- version 2 (code v3) ---------------------------------------------------------------------------------------------
    # (aucun défaut n'ouvre le verrou des couches décisives : il ferait dériver une graine décisive dans la copie mutée)
    ("refus-non-consigne", "C1 : refus d'une couche décisive non consigné (vu par l'essai final joué seul)", "graines.py",
     [("            REFUS.append(texte_etiquette)\n", "")], [t("zz_aucune_graine_decisive")]),
    ("registre-propre-au-bras-4b", "C2 : le registre propre du bras 2 déposé et servi au bras 4b (ce serait le bras 2)",
     "mecanique.py",
     [("                                     copie_etrangere_4b=copie_scellee_4b(e)))",
       "                                     copie_etrangere_4b=copie_scellee_4b(premieres[k])))")], [t("mecanique", "garde_27")]),
    ("copie-4b-de-la-source-propre-acceptee", "C2 : copie déposée au bras 4b venue de la source propre acceptée", "registre.py",
     [("    if etrangere == propre:\n", "    if False:\n")], [t("mecanique", "garde_27")]),
    ("entree-propre-au-4b-acceptee", "C2 : entrée de la source propre servie au bras 4b sans arrêt propre", "registre.py",
     [('        if p.get("source") == propre:\n', "        if False:\n")], [t("mecanique", "garde_27")]),
    ("empreinte-4b-non-verifiee", "C2 : empreinte de la copie servie au bras 4b non comparée à celle déposée", "registre.py",
     [("    if empreinte_vue(vue_servie) != empreinte_deposee:\n", "    if False:\n")], [t("mecanique", "garde_27")]),
    ("bras-4b-sans-controle", "C2 : la copie servie au bras 4b n'est pas contrôlée avant d'être servie", "mecanique.py",
     [('                verifier_vue_etrangere_4b(vue, copie_etrangere_4b["empreintes"][gen - 1], ctx.source,\n'
       '                                          copie_etrangere_4b["source"])\n', "")], [t("mecanique", "garde_27")]),
    ("passage-exige-sans-besoin", "C3 : p_passage_vraie exigée par Mondes même quand strates_requises ne l'exige pas",
     "statistique.py", [("            elif passage_requis:\n", "            elif True:\n")], [t("mecanique", "passage_vraie")]),
    ("table-des-gardes-incomplete", "note D4 : table des gardes incomplète acceptée (« C6 tenu » sur une liste partielle)",
     "analyse.py",
     [("    if sorted(gardes) != list(range(1, 28)) or any(v is None for g, v in gardes.items() if g != 17):\n",
       "    if False:\n")], [t("statistique", "regles_de_lecture")]),
    ("compteurs-du-jeu-perdus", "note D7 : compteurs des mondes sources du jeu à sources étrangères perdus", "mondes.py",
     [("        s.compteurs = cumul[k]\n", "")], [t("mecanique", "garde_27")]),
]
# le défaut « strate vide » ne se voit que si la couche statistique ne lève pas non plus à l'emploi : second remplacement
DEFAUTS[5] = (DEFAUTS[5][0], DEFAUTS[5][1], DEFAUTS[5][2], DEFAUTS[5][3], [t("mecanique", "strate_vide")])
SECONDS = {"strate-vide-repli-regroupe": ("statistique.py", [("    if v is None:\n        raise ArretFrequences(",
                                                              "    if v is None:\n        return float(f.get(\"p_tient_non_plantee_base\") or 0.0)\n"
                                                              "        raise ArretFrequences(")])}


def env_pour(src):
    e = dict(os.environ)
    e["PYTHONPATH"] = src
    e["PYTHONDONTWRITEBYTECODE"] = "1"
    return e


def jouer(src, essais):
    rc = []
    for fichier, k in essais:
        cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", fichier]
        if k:
            cmd += ["-k", k]
        r = subprocess.run(cmd, env=env_pour(src), capture_output=True, text=True, cwd=TRAVAIL, timeout=3000)
        rc.append({"essai": os.path.basename(fichier), "selection": k, "code": r.returncode,
                   "fin": r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-300:]})
    return rc


def main():
    os.makedirs(TRAVAIL)
    rapport = {"temoins": {}, "defauts": []}
    selections = sorted({e for d in DEFAUTS if not SEULS or d[0] in SEULS for e in d[4]}, key=str)
    for e in selections:
        r = jouer(os.path.join(BLOC, "src"), [e])[0]
        rapport["temoins"][f"{os.path.basename(e[0])}::{e[1]}"] = r
    for ident, description, fichier, remplacements, essais in DEFAUTS:
        if SEULS and ident not in SEULS:
            continue
        t0 = time.time()
        src = os.path.join(TRAVAIL, ident, "src")
        shutil.copytree(os.path.join(BLOC, "src"), src)
        applique = True
        tous = [(fichier, remplacements)] + ([SECONDS[ident]] if ident in SECONDS else [])
        for f, reps in tous:
            chemin = os.path.join(src, PAQUET, f)
            texte = open(chemin, encoding="utf-8").read()
            for ancien, nouveau in reps:
                if texte.count(ancien) != 1:
                    applique = False
                    break
                texte = texte.replace(ancien, nouveau)
            with open(chemin, "w", encoding="utf-8") as fh:
                fh.write(texte)
        ligne = {"defaut": ident, "description": description, "fichier": fichier, "applique": applique}
        if applique:
            r = jouer(src, essais)
            ligne["essais"] = r
            ligne["vu"] = any(x["code"] not in (0, 5) for x in r) and all(x["code"] != 5 for x in r)
        ligne["duree_s"] = round(time.time() - t0, 1)
        rapport["defauts"].append(ligne)
        print(ident, "appliqué" if applique else "NON APPLIQUÉ", "vu" if ligne.get("vu") else "NON VU", ligne["duree_s"], "s",
              flush=True)
    rapport["temoins_tous_au_vert"] = all(v["code"] == 0 for v in rapport["temoins"].values())
    rapport["defauts_vus"] = sum(1 for d in rapport["defauts"] if d.get("vu"))
    rapport["defauts_joues"] = sum(1 for d in rapport["defauts"] if d["applique"])
    with open(SORTIE, "x", encoding="utf-8") as fh:
        fh.write(json.dumps(rapport, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    print("témoins au vert", rapport["temoins_tous_au_vert"], "défauts vus", rapport["defauts_vus"], "sur",
          rapport["defauts_joues"])


main()
