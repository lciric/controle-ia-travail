MODULE = "montage_v2.py"
ESSAIS = ["test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py"]
OPTIONS = ["-k", "not (bout_en_bout or premier_palier or deuxieme or non_achevee or lue_l_autre or ligne_de_commande_phrases)"]
ALTERATIONS = [
 ("HF_TOKEN seule : toute variable acceptée", "en_trop = [n for n in suspects if n != NOM_CLE_PERMISE]", "en_trop = []"),
 ("HUGGING non regardé", '("HF" in n.upper() or "HUGGING" in n.upper())', '("HF" in n.upper())'),
 ("plongements absents de l'index acceptés", "if K2.TENSEUR_PLONGEMENTS not in carte:", "if False:"),
 ("forme des plongements non comparée", 'if tuple(description.get("shape", ())) != tuple(forme):', "if False:"),
 ("cibles du corpus : repli sur celles de montage_v1", "    except ImportError:\n        raise Arret(", "    except ImportError:\n        return mo.cibles_corpus(voisin, transport)\n        raise Arret("),
 ("premier palier : empreinte du 18 novembre non passée", "K2.EMPREINTE_18_NOVEMBRE[lettre] if palier == 1 else None)", "None)"),
]
