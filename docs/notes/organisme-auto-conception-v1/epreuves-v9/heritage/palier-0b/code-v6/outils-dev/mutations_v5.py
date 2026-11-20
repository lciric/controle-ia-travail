"""Contrôle « trop beau » (règle R4) : des défauts réintroduits un par un dans une copie du code, et l'essai qui doit les voir.

Pour chaque défaut : copie neuve de `src/` sous le dossier de travail, remplacements exacts (chacun doit se trouver une seule fois,
sinon le défaut est « non appliqué »), puis les essais nommés, lancés par `python3 -B -m pytest`. Un défaut est « vu » si les
essais échouent. Avant tout défaut, chaque sélection d'essais est jouée sur le code sain et doit passer (« témoin »). Sortie : un
fichier JSON. Arguments : bloc-notes, dossier de travail neuf, fichier de sortie, puis, en option, les identifiants à jouer.
Aucun réseau ; graines « essai » des essais eux-mêmes.

Version 2 (code v3) : les 41 défauts de la version 1, repris à l'identique, et neuf de plus — C1 (refus d'une couche
décisive non consigné, vu par l'essai final joué seul : un ; aucun défaut n'ouvre le verrou, ce qui ferait dériver une graine
décisive), C2 (la copie servie au bras 4b : cinq), C3 (la strate du passage exigée sans besoin : un), notes D4 (table des
gardes incomplète acceptée : un) et D7 (compteurs du jeu perdus : un).

Version 3 (code v4) : les 50 défauts de la version 2, repris à l'identique (remplacements et essais), et vingt et un de plus —
audit de présentation (nœuds 1 et 2, note D9, version 8 : treize), note D8 (trois), choix 12 (deux), dose du jeu de la garde 27
(trois). Mode de contrôle sans essai : `python3 -B mutations_v4.py --verifier BLOC` compte chaque texte ancien dans `BLOC/src`
(il doit s'y trouver une seule fois) et n'écrit rien.

Version 4 (code v5, préenregistrement v11) : les 71 défauts de la version 3, dont 69 repris à l'identique (remplacements et
essais ; « regle-calibree-etendue-aux-lois » couvre aussi, sur le code v5, le « calibrage étendu aux audits de lois » du point 6)
et deux adaptés au code v5, leur texte ancien n'existant plus (« zone-mediane-arretee » et « seuil-calibre-a-vingt-sigma ») ; et
des défauts neufs pour chaque règle de « Ce qui demande un code v5 » — seuil resté à 0,55 + 2 σ₀, contenu des doses resté à la lettre, signalement calibré qui arrêterait, calibrage
étendu au contenu des audits de lois, zone médiane du contenu qui pose la mention, arrêt sur une exactitude au plus 0,55, égalité
A = M + 2 σ₀ lue au-dessus, colonnes du seuil (NE-3), plis observés reçus de l'appelant, tirés du générateur des permutations ou
sous le rôle « permutation », chaque condition du verrou, le manifeste, le jeu de la garde 27 (programme de lancement, trois
sources, source précédente au lieu de suivante).

Version 5 (code v6 ; audit des trous du code v5, « Ce que le code v6 doit porter », points 1 à 7) : les 113 défauts de la
version 4, repris à l'identique (remplacements et essais ; leur texte ancien se trouve toujours une seule fois dans le code v6),
et des défauts neufs pour chaque règle du code v6 — champ de mode absent des étiquettes, écrit aussi au mode « tirages », ordre
des champs du code v5 changé ; mode absent du nom des cases, doublon non arrêté ; case sans clé ou à deux clés, nombre non
contrôlé, nombre commun à toutes les cases (tirages ou sources) ; tailles gelées non exigées sous « decisif », confirmation hors
de C1 et de C4, nombres lus hors de la grille, lot d'une seule source accepté, case de confirmation simulée réduite ; reliquat
absent ou écrit en entier, enrichissement absent ou mal pris ; étape 8 sans contrôle des fréquences ou des réglages gelés,
compagnon ou garde 22 des réglages non contrôlés, cases « non atteignables » ou fichiers gelés non inscrits, cases « sources »
laissées hors du lancement ; étape 9 sans vérification du manifeste de l'étape 8, des dossiers, de la couche, des fichiers
gelés, des comptes complets, comptes de C4 lus sur les rejets, lancement sans case à confirmer, statut sans le tirage de
confirmation, nombres lus perdus. Option `--partie v5` : les défauts neufs de cette version."""

import json
import os
import shutil
import subprocess
import sys
import time

VERIFIER = len(sys.argv) == 3 and sys.argv[1] == "--verifier"
if VERIFIER:
    BLOC, TRAVAIL, SORTIE, SEULS = sys.argv[2], None, None, set()
else:
    BLOC, TRAVAIL, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
    SEULS = set(sys.argv[4:])
# version 4 : « --partie v3 » (les 71 défauts de la version 3) ou « --partie v4 » (les défauts neufs) au lieu des identifiants ;
# version 5 : « --partie v4 » joue les 42 défauts neufs de la version 4, « --partie v5 » ceux de la version 5
PARTIE = sorted(SEULS)[1] if len(SEULS) == 2 and "--partie" in SEULS else None
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
    # --- version 3 (code v4) ---------------------------------------------------------------------------------------------
    # nœud 1 (a) : longueur de forme sur le texte aux nombres remplacés, longueur brute parmi les traits de contenu
    ("longueur-de-forme-brute", "nœud 1 : la longueur de forme lue sur le texte brut (elle lit le signe des nombres)", "audit.py",
     [("    v[CASES] = float(len(texte_aux_nombres_remplaces(texte)))\n", "    v[CASES] = float(len(texte))\n")],
     [t("mondes", "longueur_de_forme")]),
    ("longueur-brute-hors-du-contenu", "nœud 1 : la longueur brute absente des traits de contenu", "audit.py",
     [("    out.append(float(len(texte)))\n", "")], [t("mondes", "longueur_de_forme")]),
    # nœud 2 (a) limité aux trois audits des doses ; lettre de la version 6 pour les deux audits de lois
    ("regle-calibree-etendue-aux-lois", "nœud 2 : la règle calibrée appliquée aussi aux deux audits de lois", "audit.py",
     [("    if audit in AUDITS_DES_DOSES:\n        if A <= EXACTITUDE_MAX:\n", "    if True:\n        if A <= EXACTITUDE_MAX:\n")],
     [t("mondes", "lecture_calibree")]),
    ("regle-calibree-retiree", "nœud 2 : les audits des mondes par dose lus à la lettre (au-dessus de 0,55, arrêt)", "audit.py",
     [("    if audit in AUDITS_DES_DOSES:\n        if A <= EXACTITUDE_MAX:\n", "    if False:\n        if A <= EXACTITUDE_MAX:\n")],
     [t("mondes", "lecture_calibree")]),
    # (version 4 : adapté au code v5, le texte ancien de la version 3 n'existant plus ; même défaut, même essai)
    ("zone-mediane-arretee", "nœud 2 : une exactitude des doses entre 0,55 et le seuil calibré arrête", "audit.py",
     [("        return NON_DEPARTAGEE\n", "        return ARRET\n")],
     [t("mondes", "lecture_calibree")]),
    # (version 4 : adapté au code v5 ; le seuil calibré est désormais M + 2 σ₀)
    ("seuil-calibre-a-vingt-sigma", "nœud 2 : seuil calibré des doses à M + 20 σ₀", "audit.py",
     [("    return moyenne + 2.0 * sigma0\n", "    return moyenne + 20.0 * sigma0\n")], [t("mondes", "lecture_calibree")]),
    ("permutation-entre-mondes", "σ₀ des doses : étiquettes permutées entre mondes, non entre suites", "audit.py",
     [("                gm.append(suite_du_monde[k])\n", "                gm.append(k)\n")], [t("mondes", "taille_reduite")]),
    ("etiquettes-non-permutees", "σ₀ des lois : étiquettes laissées en place sous « permutation »", "audit.py",
     [("        return yi[rng.permutation(len(yi))]\n", "        return yi\n")], [t("mondes", "permutation_entre")]),
    ("suite-non-portee", "l'identifiant de la suite n'est pas porté par les mondes de l'audit", "mondes.py",
     [('            out.append({"dose": m.dose, "suite": i, "Z": m.oracle.Z, "G": m.oracle.G,\n',
       '            out.append({"dose": m.dose, "suite": 0, "Z": m.oracle.Z, "G": m.oracle.G,\n')], [t("mondes", "taille_reduite")]),
    # note D9 et version 8 : arrêts de l'audit
    ("pli-prive-accepte", "note D9 : un pli d'entraînement privé d'une classe n'arrête pas", "audit.py",
     [("            if not np.any(ytr == c):\n", "            if False:\n")], [t("mondes", "pli_prive")]),
    ("non-calculable-acceptee", "version 8 : une exactitude non calculable (moins de cinq exemples d'une classe) n'arrête pas",
     "audit.py", [("    if min(comptes) < EXEMPLES_MIN_PAR_CLASSE:\n", "    if False:\n")], [t("mondes", "pli_prive")]),
    ("centre-non-fini-accepte", "note D9 : un centre de classe non fini n'arrête pas", "audit.py",
     [("        if not all(np.all(np.isfinite(c)) for c in centres):\n", "        if False:\n")], [t("mondes", "pli_prive")]),
    ("arret-de-l-audit-non-converti", "étape 3 : l'arrêt de l'audit de présentation n'arrête pas l'étape comme un arrêt du "
     "générateur", "mondes.py",
     [("    except AU.ArretAudit as e:\n", "    except ZeroDivisionError as e:\n")], [t("mondes", "etape_3")]),
    # note D8
    ("d8-ecart-type-nul-accepte", "note D8 : un écart-type entre jumelles nul n'arrête pas l'étalonnage", "etalonnage.py",
     [("    if not (math.isfinite(ecart_type) and ecart_type > 0.0):\n", "    if False:\n")], [t("statistique", "note_d8")]),
    ("d8-taille-non-finie-acceptee", "note D8 : une taille réduite non finie rangée « non atteignable »", "etalonnage.py",
     [("    if taille_reduite is not None and not math.isfinite(taille_reduite):\n", "    if False:\n")],
     [t("statistique", "note_d8")]),
    ("d8-dichotomie-sans-controle", "note D8 : le contrôle retiré des évaluations de la dichotomie", "etalonnage.py",
     [('            exiger_ecart_type_et_taille_finis(s, t, f"({nom}, dose {dose}, cible {cible}, réglage {x!r}) ")\n', "")],
     [t("statistique", "note_d8")]),
    # choix 12
    ("liste-des-etiquettes-autre-que-le-texte-hache", "choix 12 : le fichier des étiquettes n'est pas le texte dont le "
     "manifeste porte l'empreinte", "tirages.py",
     [("        fh.write(texte_liste)\n", '        fh.write(texte_liste + b"\\n")\n')], [t("statistique", "manifeste")]),
    ("liste-des-etiquettes-non-verifiee", "choix 12 : la liste des étiquettes relue sans rejouer son empreinte", "tirages.py",
     [('    if (sha != e.get("fichier_sha256") or hashlib.sha256(liste).hexdigest() != e.get("sha256")\n',
       '    if False and (sha != e.get("fichier_sha256") or hashlib.sha256(liste).hexdigest() != e.get("sha256")\n')],
     [t("statistique", "manifeste")]),
    # dose du jeu de la garde 27 (point 5)
    ("dose-du-jeu-non-exigee-a-la-construction", "garde 27 : le jeu à sources étrangères construit à une autre dose que 0,25",
     "mondes.py", [("    if float(dose) != DOSE_JEU_GARDE_27:\n        raise ArretGenerateur(",
                    "    if False:\n        raise ArretGenerateur(")], [t("mecanique", "dose_du_jeu")]),
    ("dose-du-jeu-non-exigee-au-jeu", "garde 27 : le jeu à sources étrangères joué à une autre dose que 0,25", "mecanique.py",
     [("    if float(dose) != DOSE_JEU_GARDE_27:\n        raise ArretMecanique(", "    if False:\n        raise ArretMecanique(")],
     [t("mecanique", "dose_du_jeu")]),
    ("jeu-de-l-etape-4-a-une-autre-dose", "garde 27 : l'étape 4 joue le jeu à la dose 0,5 et non à la constante", "etapes.py",
     [("    suites = MO.generer_jeu_avec_etrangeres(graines, bases, DOSE_JEU_GARDE_27)\n",
       "    suites = MO.generer_jeu_avec_etrangeres(graines, bases, 0.5)\n")], [t("mecanique", "garde_27_bras")]),
    # --- version 4 (code v5) ---------------------------------------------------------------------------------------------
    # points 1 et 6 : seuil d'arrêt, le plus grand de 0,55 et de M + 2 σ₀ ; colonnes de la table (NE-3)
    ("seuil-reste-a-0-55-plus-2-sigma", "point 1 : le seuil calibré resté à 0,55 + 2 σ₀ (au lieu de M + 2 σ₀)", "audit.py",
     [("    return moyenne + 2.0 * sigma0\n", "    return EXACTITUDE_MAX + 2.0 * sigma0\n")], [t("mondes", "lecture_calibree")]),
    ("arret-sur-une-exactitude-au-plus-0-55", "point 1, version 11 : une exactitude au plus 0,55 et au-dessus de M + 2 σ₀ "
     "arrête (ou est signalée)", "audit.py",
     [('        if A <= EXACTITUDE_MAX:\n            return TENUE if jeu == "forme" else AU_PLUS\n',
       '        if A <= EXACTITUDE_MAX and A <= seuil_calibre(sigma0, moyenne):\n            return TENUE if jeu == "forme" '
       'else AU_PLUS\n')], [t("mondes", "au_plus_0_55")]),
    ("egalite-au-seuil-calibre-lue-au-dessus", "silence n° 4 au seuil neuf : A = M + 2 σ₀ lue « au-dessus »", "audit.py",
     [("        if A > seuil_calibre(sigma0, moyenne):\n", "        if A >= seuil_calibre(sigma0, moyenne):\n")],
     [t("mondes", "egalite")]),
    ("seuil-d-arret-sans-plancher", "NE-3 : la colonne du seuil d'arrêt porte M + 2 σ₀ sans le plancher de 0,55", "audit.py",
     [("        return max(EXACTITUDE_MAX, seuil_calibre(sigma0, moyenne))\n", "        return seuil_calibre(sigma0, moyenne)\n")],
     [t("mondes", "colonne")]),
    ("colonne-du-seuil-calibre-a-0-55-plus-2-sigma", "point 1 : la colonne du seuil de la table porte encore 0,55 + 2 σ₀",
     "audit.py",
     [('                             "seuil_calibre": seuil_calibre(p["sigma0"], p["moyenne_permutee"]),\n',
       '                             "seuil_calibre": EXACTITUDE_MAX + 2.0 * p["sigma0"],\n')], [t("mondes", "taille_reduite")]),
    ("colonne-du-seuil-d-arret-absente", "NE-3 : la colonne du seuil d'arrêt n'est pas écrite à la table", "audit.py",
     [('                             "seuil_d_arret": seuil_d_arret(jeu, a, p["sigma0"], p["moyenne_permutee"]),\n', "")],
     [t("mondes", "taille_reduite")]),
    # point 2 : règle calibrée de signalement (contenu et réunis des doses), audits de lois à la lettre
    ("contenu-des-doses-a-la-lettre", "point 2 : contenu et réunis des doses lus à la lettre (au-dessus de 0,55, signalés)",
     "audit.py",
     [("    if audit in AUDITS_DES_DOSES:\n        if A <= EXACTITUDE_MAX:\n",
       '    if audit in AUDITS_DES_DOSES and jeu == "forme":\n        if A <= EXACTITUDE_MAX:\n')],
     [t("mondes", "lecture_calibree")]),
    ("signalement-calibre-qui-arrete", "point 2 : un signalement calibré du contenu ou des réunis arrête", "audit.py",
     [('            return ARRET if jeu == "forme" else SIGNALEE\n', "            return ARRET\n")],
     [t("mondes", "lecture_calibree")]),
    ("calibrage-etendu-au-contenu-des-lois", "point 2 : le contenu et les réunis des audits de lois lus au seuil calibré",
     "audit.py",
     [("        return SIGNALEE if A > EXACTITUDE_MAX else AU_PLUS\n",
       "        return SIGNALEE if A > max(EXACTITUDE_MAX, seuil_calibre(sigma0, moyenne)) else (NON_DEPARTAGEE if A > "
       "EXACTITUDE_MAX else AU_PLUS)\n")], [t("mondes", "lecture_calibree")]),
    ("zone-mediane-du-contenu-mentionnee", "point 2, lecture (i) : la zone médiane du contenu ou des réunis pose la mention "
     "(comme au code v4)", "audit.py",
     [('            elif l == NON_DEPARTAGEE and jeu == "forme":\n', "            elif l == NON_DEPARTAGEE:\n")],
     [t("mondes", "lecture_calibree")]),
    # point 3 : graine des plis de la lecture observée
    ("plis-recus-de-l-appelant", "point 3 : les plis de la lecture observée reçus de l'appelant", "mondes.py",
     [('def juger_suites_d_audit(suites, compteurs, graines, couche="audit", permutations=PERMUTATIONS_AUDIT):\n',
       'def juger_suites_d_audit(suites, compteurs, graines, couche="audit", permutations=PERMUTATIONS_AUDIT, rng_plis=None):\n'),
      ("    rng_plis, rng_permutation = generateurs_de_l_audit(graines, couche)\n",
       "    rng_plis, rng_permutation = ((rng_plis, generateurs_de_l_audit(graines, couche)[1]) if rng_plis is not None\n"
       "                                 else generateurs_de_l_audit(graines, couche))\n")], [t("mondes", "etape_3")]),
    ("plis-tires-du-generateur-des-permutations", "point 3 : les plis de la lecture observée tirés du générateur des "
     "permutations", "mondes.py",
     [("mondes_pour_l_audit(suites), rng_plis, rng_permutation, permutations)",
       "mondes_pour_l_audit(suites), rng_permutation, rng_permutation, permutations)")], [t("mondes", "etape_3")]),
    ("plis-sous-le-role-permutation", "point 3 : le générateur des plis dérivé sous le rôle « permutation »", "mondes.py",
     [('    rng_plis = graines.g(couche=couche, famille="audit", role=ROLE_PLIS)\n',
       '    rng_plis = graines.g(couche=couche, famille="audit", role=ROLE_PERMUTATION)\n')], [t("mondes", "etape_3")]),
    # point 4 : verrou des graines décisives, chaque condition ; manifeste ; constante de la version 6
    ("constante-de-la-version-6-retablie", "point 4 : l'empreinte de la version 6 écrite de nouveau dans `constantes.py`",
     "constantes.py",
     [('VERSION = "heritage-etage-processeur-v1"\n',
       'VERSION = "heritage-etage-processeur-v1"\n'
       'PREENREGISTREMENT_SHA256 = "4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029"\n')],
     [t("verrou", "constantes")]),
    ("verrou-texte-non-scelle", "verrou : le texte présenté accepté sans son compagnon", "graines.py",
     [("        sha_texte = verifier_scelle(self.texte)\n", "        sha_texte = _sha256_fichier(self.texte)\n")],
     [t("verrou", "artefact")]),
    ("verrou-piece-non-scellee", "verrou : la pièce d'autorisation acceptée sans son compagnon", "graines.py",
     [("        sha_piece = verifier_scelle(piece)\n", "        sha_piece = _sha256_fichier(piece)\n")],
     [t("verrou", "artefact")]),
    ("verrou-compagnon-a-plusieurs-lignes", "verrou, « scellée » au sens du dépôt : un compagnon de plusieurs lignes accepté",
     "graines.py", [("    if len(lignes) != 1:\n", "    if len(lignes) < 1:\n")], [t("verrou", "artefact or depot")]),
    ("verrou-compagnon-au-mauvais-nom", "verrou, « scellée » au sens du dépôt : un compagnon au mauvais nom accepté",
     "graines.py", [("    if m.group(2) != os.path.basename(chemin):\n", "    if False:\n")], [t("verrou", "artefact or depot")]),
    ("verrou-piece-a-moins-de-quatre-lignes", "verrou : une pièce de moins de quatre lignes acceptée à la lecture", "graines.py",
     [("    if len(lignes) != len(CHAMPS_DE_LA_PIECE):\n", "    if len(lignes) > len(CHAMPS_DE_LA_PIECE):\n")],
     [t("verrou", "artefact")]),
    ("verrou-ordre-des-champs-non-exige", "verrou : les quatre champs acceptés dans un autre ordre que celui de R-4123",
     "graines.py", [("        if nom != CHAMPS_DE_LA_PIECE[rang]:\n", "        if False:\n")], [t("verrou", "artefact")]),
    ("verrou-go-non-cherche-au-registre", "verrou : l'identifiant du GO non cherché dans `registres/go.md`", "graines.py",
     [("        if not go_inscrit(self.racine, go):\n", "        if False:\n")], [t("verrou", "artefact")]),
    ("verrou-go-hors-de-la-premiere-colonne", "verrou : l'identifiant du GO lu n'importe où dans une ligne du registre",
     "graines.py",
     [('            if ligne.startswith("|") and len(cellules) > 2 and cellules[1].strip() == identifiant:\n',
       "            if identifiant in ligne:\n")], [t("verrou", "artefact")]),
    ("verrou-forme-du-go-non-lue", "verrou : un identifiant de GO mal formé accepté", "graines.py",
     [("        if not _IDENTIFIANT_DU_GO.match(go):\n", "        if False:\n")], [t("verrou", "artefact")]),
    ("verrou-commit-non-compare", "verrou : le commit de la pièce non comparé à celui du texte", "graines.py",
     [("        if commit != commit_du_texte:\n", "        if False:\n")], [t("verrou", "artefact")]),
    ("verrou-deux-lignes-de-commit", "verrou : un texte à deux lignes « Commit du code d'analyse » accepté (la première lue)",
     "graines.py", [("    if len(rangs) != 1:\n", "    if not rangs:\n")], [t("verrou", "artefact")]),
    ("verrou-empreinte-du-texte-non-comparee", "verrou : l'empreinte du texte de la pièce non comparée au texte présenté",
     "graines.py", [("        if empreinte != sha_texte:\n", "        if False:\n")], [t("verrou", "artefact")]),
    ("verrou-heure-non-lue", "verrou : l'heure de la pièce non contrôlée (UTC)", "graines.py",
     [("        exiger_heure_utc(heure)\n", "")], [t("verrou", "artefact")]),
    ("verrou-modules-non-controles", "verrou : les modules lancés non contrôlés contre la table du texte", "graines.py",
     [("        verifier_modules(table)\n", "")], [t("verrou", "artefact")]),
    ("verrou-empreinte-des-modules-non-comparee", "verrou : un module lancé d'empreinte différente de la table accepté",
     "graines.py",
     [("        if not os.path.isfile(lances[nom]) or _sha256_fichier(lances[nom]) != attendus[nom]:\n",
       "        if not os.path.isfile(lances[nom]):\n")], [t("verrou", "artefact")]),
    ("verrou-module-absent-de-la-table", "verrou : un module lancé absent de la table du texte accepté", "graines.py",
     [("    if manquants or en_trop:\n", "    if en_trop:\n")], [t("verrou", "artefact")]),
    ("verrou-module-non-lance-dans-la-table", "verrou : la table du texte nomme un module qui n'est pas lancé, accepté",
     "graines.py", [("    if manquants or en_trop:\n", "    if manquants:\n")], [t("verrou", "artefact")]),
    ("verrou-non-reverifie-au-lancement", "verrou : l'autorisation non vérifiée de nouveau avant un lancement décisif",
     "tirages.py", [("    if couche in COUCHES_DECISIVES:\n        graines.autorisation.verifier()\n", "")],
     [t("verrou", "verifie_de_nouveau")]),
    ("manifeste-sans-empreintes-du-verrou", "remarque 4 (e) : le manifeste n'inscrit pas l'empreinte du texte présenté",
     "tirages.py",
     [('    autorisation = {"texte_sha256": None if a is None else a.sha_texte,\n', '    autorisation = {"texte_sha256": None,\n')],
     [t("verrou", "cas_sain")]),
    ("manifeste-champs-du-verrou-non-verifies", "remarque 4 (e) : le manifeste relu sans contrôler les empreintes du verrou",
     "tirages.py",
     [('    if "preenregistrement_sha256" in m or any(k not in m for k in champs) or (\n', "    if False and (\n")],
     [t("statistique", "manifeste")]),
    # point 5 : le jeu de la garde 27, appelé par le programme de lancement de l'étape 4 ; trois sources ; source suivante
    ("source-precedente-servie", "garde 27 : le registre de la source précédente déposé aux bras 4a et 4b, au lieu de celui "
     "de la suivante", "mecanique.py",
     [("        e = premieres[(k + 1) % S]\n", "        e = premieres[(k - 1) % S]\n")], [t("etapes", "lancer_etape_4")]),
    ("origine-du-depot-non-verifiee", "garde 27 : l'origine du registre déposé aux bras 4a et 4b non contrôlée", "mecanique.py",
     [('    if etrangere is None or sortie_etrangere["suite"].source is not etrangere:\n', "    if etrangere is None:\n")],
     [t("etapes", "lancer_etape_4")]),
    ("marge-construite-face-a-la-source-precedente", "garde 27 : la marge des mondes cibles construite face à la source "
     "précédente", "mondes.py",
     [("        s.etrangere = sources[(k + 1) % S]  #", "        s.etrangere = sources[(k - 1) % S]  #")],
     [t("mondes", "marge_face")]),
    ("etrangeres-du-jeu-non-verifiees", "garde 27 : la source de construction de la marge non contrôlée à la fin du jeu",
     "mondes.py", [('        if getattr(s, "etrangere", None) is not suites[(k + 1) % S].source:\n', "        if False:\n")],
     [t("mondes", "marge_face")]),
    ("jeu-a-deux-sources", "point 5 : le programme de lancement joue le jeu de la garde 27 à deux sources", "etapes.py",
     [("P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)",
       "P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), 2)")], [t("etapes", "lancer_etape_4")]),
    ("jeu-joue-par-le-lecteur-heritage", "point 5 : le jeu de la garde 27 joué par le lecteur réglé pour l'héritage",
     "etapes.py",
     [("P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)",
       'P.configuration("lecteur-heritage", **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)')], [t("etapes", "lancer_etape_4")]),
    ("jeu-avant-les-bras-1-a-3", "point 5 : le jeu de la garde 27 joué avant les bras 1 à 3", "etapes.py",
     [('    f, comptes, garde_17 = etape_4(graines, couche, os.path.join(dossier, "bras-1-a-3"), doses, proposeurs, sources,\n'
       "                                   sous_ensemble, organisme)\n"
       '    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),\n'
       "                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)\n",
       '    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),\n'
       "                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)\n"
       '    f, comptes, garde_17 = etape_4(graines, couche, os.path.join(dossier, "bras-1-a-3"), doses, proposeurs, sources,\n'
       "                                   sous_ensemble, organisme)\n")], [t("etapes", "lancer_etape_4")]),
    ("jeu-non-joue", "point 5 : le programme de lancement de l'étape 4 n'appelle pas le jeu de la garde 27", "etapes.py",
     [('    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),\n'
       "                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)\n",
       "    jeu = None\n")], [t("etapes", "lancer_etape_4")]),
    # --- version 5 (code v6) ---------------------------------------------------------------------------------------------
    # point 1 : le champ de mode des étiquettes ; aucune graine existante ne change
    ("mode-absent-des-etiquettes", "point 1 : le mode « sources » sans champ d'étiquette (graines communes aux deux modes)",
     "tirages.py",
     [('    if "sources" in case:\n        c["mode"] = "sources"\n', ""),
      ('    if base.get("mode") != "sources":\n'
       '        raise ArretTirages("simulation au mode « sources » d\'une case sans clé « sources »")\n', "")],
     [t("lancement", "point_1")]),
    ("mode-ecrit-aussi-aux-tirages", "point 1 : le champ de mode écrit aussi au mode « tirages » (graines existantes changées)",
     "tirages.py",
     [('    if "sources" in case:\n        c["mode"] = "sources"\n',
       '    c["mode"] = "sources" if "sources" in case else "tirages"\n')], [t("lancement", "point_1")]),
    ("ordre-des-champs-du-code-v5-change", "point 1 : l'ordre des champs du code v5 changé avec l'ajout du mode", "graines.py",
     [('"repere", "mode", "bras",\n                    "jumelle", "tirage", "lot",',
       '"repere", "mode", "lot", "bras",\n                    "jumelle", "tirage",')], [t("lancement", "point_1")]),
    # point 2 : le mode dans le nom des cases
    ("nom-sans-mode", "point 2 : le nom des cases sans le mode (D et H : deux cases au même nom)", "tirages.py",
     [('    if "sources" in case:\n        morceaux.append("sources")\n', "")], [t("lancement", "point_2")]),
    ("doublon-non-arrete", "point 2 : deux cases au même nom non arrêtées avant tout tirage", "tirages.py",
     [('        if nom in plan:\n            raise ArretTirages(f"deux cases au même nom : {nom} (le nom porte le mode ; B8) : '
       'arrêt avant tout tirage")\n', "")], [t("lancement", "point_2")]),
    # point 3 : la clé de chaque case, un seul lancement, tailles gelées
    ("case-sans-cle-acceptee", "point 3 : une case sans clé, ou aux deux clés, prise au mode « tirages »", "tirages.py",
     [("    presents = [m for m in MODES if m in case]\n", '    presents = [m for m in MODES if m in case][:1] or ["tirages"]\n')],
     [t("lancement", "point_3")]),
    ("nombre-non-controle", "point 3 : un nombre nul, non entier ou booléen accepté", "tirages.py",
     [("    if isinstance(n, bool) or not isinstance(n, int) or n < 1:\n", "    if False:\n")], [t("lancement", "point_3")]),
    ("tirages-communs-a-toutes-les-cases", "point 3 : un nombre de tirages commun à toutes les cases, la clé ignorée",
     "tirages.py",
     [("            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, sources_par_tirage=S)\n",
       "            out[nom] = jouer_case(graines, couche, case, f_par_case(case), 2, dossier, grille=lus, sources_par_tirage=S)\n")],
     [t("lancement", "point_3")]),
    ("sources-communes-a-toutes-les-cases", "point 3 : un nombre de sources commun à toutes les cases, la clé ignorée",
     "tirages.py",
     [("            out[nom] = jouer_case_sources(graines, couche, case, f_par_case(case), n, dossier)\n",
       "            out[nom] = jouer_case_sources(graines, couche, case, f_par_case(case), 24, dossier)\n")],
     [t("lancement", "point_3")]),
    ("tailles-gelees-non-exigees", "point 3 : une taille réduite, ou des nombres lus, acceptés sous la couche « decisif »",
     "tirages.py", [('            if n != gelee or "nombres_lus" in case:\n', "            if False:\n")],
     [t("lancement", "point_3")]),
    ("confirmation-hors-de-c1-et-c4", "étape 9 : la couche « confirmation » tire une case hors de C1 et de C4", "tirages.py",
     [('                                         or (case["famille"], case["proposeur"]) not in CASES_DE_CONFIRMATION):\n',
       "                                         or False):\n")], [t("lancement", "point_3")]),
    ("nombres-lus-hors-de-la-grille", "étape 9 : des nombres lus hors de la grille de la case acceptés", "tirages.py",
     [('            if mode != "tirages" or not lus or not set(lus) <= set(grille_de(case["dose"], avec_m13=case["famille"] == '
       '"B")):\n', '            if mode != "tirages" or not lus:\n')], [t("lancement", "point_3")]),
    ("lot-d-une-source-accepte", "point 1 : un lot d'une seule source accepté au mode « sources » (source étrangère sur "
     "elle-même)", "tirages.py", [("            if min(LOT_DE_SOURCES, dernier) < 2:\n", "            if False:\n")],
     [t("lancement", "point_3")]),
    ("confirmation-simulee-reduite", "étape 9 : la case retirée simulée au seul plus grand nombre lu, non entière",
     "tirages.py",
     [("            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, sources_par_tirage=S)\n",
       "            out[nom] = jouer_case(graines, couche, case, f_par_case(case), n, dossier, grille=lus, "
       "sources_par_tirage=None)\n")], [t("lancement", "point_6 and plantes")]),
    # point 4 : reliquat et enrichissement
    ("reliquat-absent", "point 4 : le reliquat par bras absent des sorties scellées", "tirages.py",
     [('"fausses_tenues": np.int16, "reliquat": np.float64}', '"fausses_tenues": np.int16}')], [t("lancement", "point_4")]),
    ("reliquat-en-entier", "point 4 : le reliquat écrit en entier de 16 bits", "tirages.py",
     [('"reliquat": np.float64}', '"reliquat": np.int16}')], [t("lancement", "point_4")]),
    ("enrichissement-absent", "point 4 : la part des entrées gardées et l'enrichissement absents des sorties du repli",
     "tirages.py",
     [('        if case.get("repli"):\n            for champ, v in sorties_du_registre_source(r["source"]).items():\n',
       '        if False:\n            for champ, v in sorties_du_registre_source(r["source"]).items():\n')],
     [t("lancement", "point_4")]),
    ("enrichissement-mal-pris", "point 4 : le facteur au grain des entrées écrit pour toutes les sorties d'enrichissement",
     "tirages.py",
     [("    out.update({k: np.asarray(e[k], dtype=np.float64) for k in CHAMPS_D_ENRICHISSEMENT})\n",
       '    out.update({k: np.asarray(e["facteur_entrees"], dtype=np.float64) for k in CHAMPS_D_ENRICHISSEMENT})\n')],
     [t("lancement", "point_4")]),
    # point 5 : l'étape 8
    ("etape-8-reglages-sans-compagnon", "point 5 : les réglages gelés relus sans contrôle de leur compagnon", "etalonnage.py",
     [("    if len(lignes_compagnon) != 1 or lignes_compagnon[0] != attendue_au_compagnon or sha != sha_attendue:\n",
       "    if sha != sha_attendue:\n")], [t("lancement", "point_5 and controles")]),
    ("etape-8-reglages-sans-garde-22", "point 5 : les réglages gelés relus sans la garde 22", "etalonnage.py",
     [("    verifier_sortie(lignes)\n    return lignes\n", "    return lignes\n")], [t("lancement", "point_5 and controles")]),
    ("etape-8-frequences-non-controlees", "point 5 : le fichier des fréquences relu sans contrôle de son empreinte",
     "etapes.py",
     [("    f = FR.lire_gelees(chemin_frequences, sha_frequences)\n",
       '    f = json.load(open(chemin_frequences, encoding="utf-8"))["frequences"]\n')],
     [t("lancement", "point_5 and controles")]),
    ("etape-8-reglages-non-controles", "point 5 : le fichier des réglages relu sans contrôle de son empreinte", "etapes.py",
     [("    lignes = ET.lire_reglages_geles(chemin_reglages, sha_reglages)\n",
       '    lignes = json.load(open(chemin_reglages, encoding="utf-8"))["reglages"]\n')],
     [t("lancement", "point_5 and controles")]),
    ("etape-8-non-atteignables-non-inscrites", "point 5 : les cases « non atteignables » non inscrites au manifeste",
     "etapes.py",
     [("    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers, cases_non_atteignables=non)\n",
       "    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers)\n")],
     [t("lancement", "point_5 and plan_entier")]),
    ("etape-8-fichiers-geles-non-inscrits", "point 5 : les empreintes vérifiées des fichiers gelés non inscrites au manifeste",
     "etapes.py",
     [("    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers, cases_non_atteignables=non)\n",
       "    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, {}, cases_non_atteignables=non)\n")],
     [t("lancement", "point_5 and plan_entier")]),
    ("etape-8-sans-les-cases-sources", "point 5 : l'étape 8 laisse les cases « sources » hors du lancement", "etapes.py",
     [("    out = TI.lancer_famille(graines, couche, cases, lambda c: f, dossier, commit, fichiers, cases_non_atteignables=non)\n",
       '    out = TI.lancer_famille(graines, couche, [c for c in cases if "tirages" in c], lambda c: f, dossier, commit, '
       "fichiers,\n                            cases_non_atteignables=non)\n")],
     [t("lancement", "point_5 and plan_entier")]),
    # point 6 : l'étape 9
    ("etape-9-manifeste-8-non-verifie", "point 6 : le manifeste de l'étape 8 relu sans `verifier_manifeste`", "etapes.py",
     [("    TI.verifier_manifeste(chemin)\n    octets, sha = TI._lire_scelle(chemin)\n", "    octets, sha = TI._lire_scelle(chemin)\n")],
     [t("lancement", "point_6 and apres")]),
    ("etape-9-dossiers-non-confrontes", "point 6 : les dossiers de l'étape 8 non confrontés à son manifeste", "etapes.py",
     [("    if sorted(noms) != sur_disque:\n", "    if False:\n")], [t("lancement", "point_6 and apres")]),
    ("etape-9-comptes-incomplets-acceptes", "point 6 : des comptes de C1 ou de C4 incomplets acceptés", "etapes.py",
     [("    if (len(c1) != CASES_C1 or len(c4) != CASES_C4 or sorted(comptes_c1, key=str) != sorted(c1, key=str)\n",
       "    if False and (len(c1) != CASES_C1 or len(c4) != CASES_C4 or sorted(comptes_c1, key=str) != sorted(c1, key=str)\n")],
     [t("lancement", "point_6 and plantes")]),
    ("etape-9-c4-lu-sur-les-rejets", "point 6 : les comptes de C4 lus sur les rejets et non sur les déclenchements",
     "etapes.py",
     [('            lecture, cible, cle = "lecture-declenche", comptes_c4,', '            lecture, cible, cle = "lecture-rejette", comptes_c4,')],
     [t("lancement", "point_6")]),
    ("etape-9-couche-non-controlee", "point 6 : la couche de l'étape 8 non confrontée à celle de l'étape 9", "etapes.py",
     [('    if couche == "decisif" or m8["configuration"].get("couche") != ("decisif" if couche == "confirmation" else couche):\n',
       '    if couche == "decisif":\n')], [t("lancement", "point_6 and apres")]),
    ("etape-9-fichiers-geles-non-confrontes", "point 6 : les fichiers gelés présentés non confrontés au manifeste de l'étape 8",
     "etapes.py", [('    if m8.get("fichiers_geles") != fichiers:\n', "    if False:\n")], [t("lancement", "point_6 and apres")]),
    ("etape-9-lance-sans-case-a-confirmer", "point 6 : un lancement de confirmation sans aucune case à confirmer", "etapes.py",
     [("    if not a_confirmer:\n        return resultat\n", "")], [t("lancement", "point_6 and apres")]),
    ("etape-9-statut-sans-confirmation", "point 6 : le statut d'une case retirée rendu sans le compte du tirage de "
     "confirmation", "etapes.py",
     [("        out[tuple(t)] = AN.statut_case_de_niveau(compte, tirages_8[cle], comptes_confirmation[tuple(t)])\n",
       "        out[tuple(t)] = AN.statut_case_de_niveau(compte, tirages_8[cle], None)\n")], [t("lancement", "point_6")]),
    ("etape-9-nombres-lus-perdus", "point 6 : la case retirée sans ses nombres lus (toute la grille lue)", "etapes.py",
     [('"tirages": tirages, "nombres_lus": tuple(sorted(ks))})', '"tirages": tirages})')], [t("lancement", "point_6")]),
]
# le défaut « strate vide » ne se voit que si la couche statistique ne lève pas non plus à l'emploi : second remplacement
DEFAUTS[5] = (DEFAUTS[5][0], DEFAUTS[5][1], DEFAUTS[5][2], DEFAUTS[5][3], [t("mecanique", "strate_vide")])
SECONDS = {"strate-vide-repli-regroupe": ("statistique.py", [("    if v is None:\n        raise ArretFrequences(",
                                                              "    if v is None:\n        return float(f.get(\"p_tient_non_plantee_base\") or 0.0)\n"
                                                              "        raise ArretFrequences(")])}
DEFAUTS_DE_LA_VERSION_3 = 71
DEFAUTS_DE_LA_VERSION_4 = 113
if PARTIE is not None:
    if PARTIE not in ("v3", "v4", "v5"):
        raise SystemExit(f"partie inconnue : {PARTIE!r}")
    TRANCHES = {"v3": DEFAUTS[:DEFAUTS_DE_LA_VERSION_3], "v4": DEFAUTS[DEFAUTS_DE_LA_VERSION_3:DEFAUTS_DE_LA_VERSION_4],
                "v5": DEFAUTS[DEFAUTS_DE_LA_VERSION_4:]}
    SEULS = {d[0] for d in TRANCHES[PARTIE]}


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


def verifier():
    """Chaque texte ancien de chaque défaut se trouve une seule fois dans son fichier de `BLOC/src` ; rien n'est écrit."""
    problemes = 0
    for ident, _, fichier, remplacements, essais in DEFAUTS:
        tous = [(fichier, remplacements)] + ([SECONDS[ident]] if ident in SECONDS else [])
        for f, reps in tous:
            texte = open(os.path.join(BLOC, "src", PAQUET, f), encoding="utf-8").read()
            for ancien, _ in reps:
                n = texte.count(ancien)
                if n != 1:
                    problemes += 1
                    print("PROBLÈME", ident, f, "trouvé", n, "fois")
        for fichier_essai, _ in essais:
            if not os.path.isfile(fichier_essai):
                problemes += 1
                print("PROBLÈME", ident, "essai absent", fichier_essai)
    print("défauts", len(DEFAUTS), "identifiants distincts", len({d[0] for d in DEFAUTS}), "problèmes", problemes)


if VERIFIER:
    verifier()
else:
    main()
