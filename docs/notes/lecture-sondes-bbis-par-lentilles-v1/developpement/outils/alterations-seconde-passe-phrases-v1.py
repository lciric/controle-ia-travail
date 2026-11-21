MODULE = "phrases_v2.py"
ESSAIS = ["test_lentilles_sondes_bbis_seconde_passe_phrases_reproduction_v1.py"]
ALTERATIONS = [
 ("un mot changé dans une phrase permise", "identiques à l'octet à ceux du 18 novembre (empreintes …)", "identiques, à l'octet, à ceux du 18 novembre (empreintes …)"),
 ("phrase de S seule non construite", ".replace(\n    PHRASE_DES_DEUX_SERIES, REMPLACEMENT_POUR_S)", ".replace(\n    PHRASE_DES_DEUX_SERIES, PHRASE_DES_DEUX_SERIES)"),
 ("pluriel écrit pour une seule lentille au premier palier", 'formes[l] = "deux au premier palier" if p[autre] == 1 else "une seule au premier palier"', 'formes[l] = "deux au premier palier"'),
 ("pluriel écrit pour une seule lentille au deuxième palier", 'formes[l] = "deux au deuxième palier" if p[autre] == 2 else f"{l} seule au deuxième palier"', 'formes[l] = "deux au deuxième palier"'),
 ("paraphrase interdite non refusée", "        if m:\n            raise Refus(f\"phrase interdite", "        if False:\n            raise Refus(f\"phrase interdite"),
 ("phrase (vi) non recopiée", 'if "R" in lettres and conditions["R"].phrase_vi:', "if False:"),
 ("phrase sans mesure oubliée", "if refaites is False:\n                    ligne[\"phrases\"].append(PHRASE_SANS_MESURE)", "if False:\n                    ligne[\"phrases\"].append(PHRASE_SANS_MESURE)"),
 ("fiche muette : phrase écrite quand même", "    if course == nl.COURSE_REJOUEE and lecture_seconde_course_inscrite:\n        return True\n    return None", "    return True"),
 ("mixte : une seule ligne de verdict d'ensemble", "    if deuxieme:\n        mixte = bool(premier)", "    if deuxieme and not premier:\n        mixte = bool(premier)"),
 ("mixte : liste entière des réserves au deuxième palier", 'reserves = RESERVES_DE[deuxieme[0]] if mixte else "[(R-a) à (R-e)]"', 'reserves = "[(R-a) à (R-e)]"'),
 ("soupçon par S à la couche 15", "    if int(couche) != 7:\n        return (f\"La famille {nom} paraît", "    if False:\n        return (f\"La famille {nom} paraît"),
 ("phrase de q égale à celle de w", '    if vecteur == "w":', '    if vecteur in ("w", "q"):'),
 ("lecture non achevée : phrase de reproduction ordinaire", "    if reproduction[\"etat\"] == rp.ETAT_NON_FAITE:\n        return [PHRASE_REPRODUCTION_NON_FAITE]", "    if False:\n        return [PHRASE_REPRODUCTION_NON_FAITE]"),
 ("renvoi du deuxième palier oublié", "    if palier == 2:\n        suite", "    if False:\n        suite"),
 ("pôles de notre R dits lus par la lentille publique", 'return phrase.replace("; la lentille publique les lit :", "; notre lentille R les lit :")', "return phrase"),
]
