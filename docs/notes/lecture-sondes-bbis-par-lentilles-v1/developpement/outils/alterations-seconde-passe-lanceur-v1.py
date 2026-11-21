MODULE = "lanceur_seconde_passe_v1.py"
ESSAIS = ["test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py"]
OPTIONS = ["-k", "not (bout_en_bout or premier_palier or deuxieme or non_achevee or lue_l_autre or ligne_de_commande_phrases)"]
ALTERATIONS = [
 ("addendum de la fiche du code non comparé", 'if fiche.get("addendum_concentration") != ADDENDUM:', "if False:"),
 ("modules différents non exigés", 'if list(fiche.get("code_de_lecture_different_de_la_premiere_passe") or []) != list(MODULES_DIFFERENTS):', "if False:"),
 ("essai opposable de l'archive non exigé", "if not isinstance(piece, dict) or not chemin.is_file() or mo.sha256_fichier(chemin) != piece.get(\"sha256\"):", "if False:"),
 ("empreinte d'un module non comparée", "if fichiers.get(nom) != mo.sha256_fichier(ici / f\"{m}.py\"):", "if False:"),
 ("empreinte de la fiche du code non comparée", "if not p.is_file() or mo.sha256_fichier(p) != ligne.sha256:", "if not p.is_file():"),
 ("noms des variables d'environnement non relevés", "noms_de_cles = m2.exiger_noms_des_variables(ctx.env)", "noms_de_cles = []"),
 ("message d'un arrêt cloisonné affiché", "        return l7.ligne_d_arret_cloisonne(arret)\n", "        return f\"ARRÊT : {arret}\"\n"),
 ("lentille lue non montée acceptée", "if conditions[lettre].lue and lettre not in charge.nos:", "if False:"),
 ("plongements absents de l'index acceptés", "    m2.exiger_plongements_dans_l_index(petits[K.INDEX_LLAMA])\n", ""),
 ("fiche de rangement d'après le montage acceptée", 'if lettre in charge.nos and charge.etat["fiche_de_rangement"]["sha256"] != fiche["_ligne"]["sha256"]:', "if False:"),
]
