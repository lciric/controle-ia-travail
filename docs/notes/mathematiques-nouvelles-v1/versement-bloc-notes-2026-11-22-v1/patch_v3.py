import sys
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
R = [
# docstring
('"""Rejeu par script des calculs du devis v2 du pilote', '"""Rejeu par script des calculs du devis v3 du pilote'),
("""Pièce rejouée : `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v2-brouillon.md`
(sha256 c857e62c1e921cdfc16f1234e54bff2d8dcf1f68bfdb7d8e3dcb96ee1d555ca6), écrit à la main.
Logique reprise en copie du script v1 (`calculs-v1/calculs_devis_pilote_generation_v1.py`, `ad1c85d3…`),
qui n'est pas modifié.""",
"""Pièce rejouée : `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v3-brouillon.md`
(sha256 5c8a0f68518c1f335851c79d09a768b7b99d61c15b6406937cbd79b9fff9abe8), et P7 et A6 du brouillon 3 du
préenregistrement (`preenregistrement-pilote-generation-v1-brouillon-3.md`, e33d7bec…).
Copie adaptée du script v2 (`calculs-v2/calculs_devis_pilote_generation_v2.py`, 3c51f08d…), qui n'est pas modifié ;
logique d'origine : script v1 (`ad1c85d3…`)."""),
("dans le devis v2. Aucune", "dans le devis v3. Aucune"),
("calculs-v2/calculs_devis_pilote_generation_v2.py \\\n      > prereg/mathematiques-nouvelles-v1/calculs-v2/sortie-calculs-devis-pilote-generation-v2.txt",
 "calculs-v3/calculs_devis_pilote_generation_v3.py \\\n      > prereg/mathematiques-nouvelles-v1/calculs-v3/sortie-calculs-devis-pilote-generation-v3.txt"),
("# 1. Effectifs écrits dans le devis v2 (§ 2) et le brouillon 2 du préenregistrement", "# 1. Effectifs écrits dans le devis v3 (§ 2) et le brouillon 3 du préenregistrement"),
("SUPPOSÉ par le devis v2 : quatre appels", "SUPPOSÉ par le devis v3 : quatre appels, un par modèle,"),
("montant forfaitaire écrit au devis v2 (SUPPOSÉ)", "montant forfaitaire écrit au devis v3 (SUPPOSÉ)"),
('print("Rejeu des calculs du devis v2 du pilote « oracles plantés » — calculs v2")', 'print("Rejeu des calculs du devis v3 du pilote « oracles plantés » — calculs v3")'),
# bloc 1
('ligne("items ajoutés au v1 (48 + 10)", 58, items_par_bras - ANALYSES_S_N)',
 'ligne("appels neufs par bras par rapport au v1 (48 + 10)", 58, items_par_bras - ANALYSES_S_N)\nligne("dont énoncés neufs (les témoins)", 48, temoins_servis)\nligne("dont seconds services", 10, REDOUBLES)'),
("""print("   NB : les 10 redoublés sont des énoncés déjà comptés dans les 150, servis une seconde fois ;")
print("        seuls les 48 témoins sont des énoncés absents de la sous-banque v1 (les 58 sont des appels neufs).")
""", ""),
# bloc 3
('ligne("fumée : un appel par modèle, Argon 2/10 (borne haute)", FUMEE_DEVIS, f_quatre_modeles_nov)',
 'ligne("fumée : un appel par modèle, Argon 2/10 (borne haute 0,096 au devis)", 0.096, f_quatre_modeles_nov, tol=0.0005)'),
('ligne("fumée : un appel par modèle, Argon 4/20 (borne haute)", FUMEE_DEVIS, f_quatre_modeles_dec)',
 'ligne("fumée : un appel par modèle, Argon 4/20 (borne haute 0,108 au devis)", 0.108, f_quatre_modeles_dec, tol=0.0005)\nligne("dépassement du forfait 0,10 (« à 0,008 près »)", 0.008, f_quatre_modeles_dec - FUMEE_DEVIS, tol=0.0005)'),
('ligne("fumée : 2 Astra + 2 Kimi (lecture du § 7, point 2) (borne haute)", FUMEE_DEVIS, f_astra_kimi)\n', ''),
('ligne("fumée : 4 Astra (borne haute la plus large)", FUMEE_DEVIS, f_quatre_astra)\n', ''),
# bloc 4
('print("   total appels + machine (non écrit au devis v2) :")', 'print("   total appels + machine (devis v3, § 2) :")\nDEVIS_AM = {"nov": (76.69, 164.69, 629.92), "dec": (79.72, 171.89, 652.96)}\nDEVIS_ECART_JOUR = (3.02, 7.20, 23.04)'),
('for sc in SC:\n    ligne(f"appels (30 nov.) + machine [{sc}]", None, poste[sc]["total_nov"] + poste[sc]["P4"])\n    ligne(f"appels (1er déc.) + machine [{sc}]", None, poste[sc]["total_dec"] + poste[sc]["P4"])',
 'for i, sc in enumerate(SC):\n    ligne(f"appels (30 nov.) + machine [{sc}]", DEVIS_AM["nov"][i], poste[sc]["total_nov"] + poste[sc]["P4"])\n    ligne(f"appels (1er déc.) + machine [{sc}]", DEVIS_AM["dec"][i], poste[sc]["total_dec"] + poste[sc]["P4"])'),
('for sc in SC:\n    ligne(f"écart d\'un jour de prix à l\'autre [{sc}]", None, poste[sc]["total_dec"] - poste[sc]["total_nov"])',
 'for i, sc in enumerate(SC):\n    ligne(f"écart d\'un jour de prix à l\'autre [{sc}]", DEVIS_ECART_JOUR[i], poste[sc]["total_dec"] - poste[sc]["total_nov"])'),
# bloc 5
('print("Bloc 5 — repli R1 (attendu) et lignes absentes du devis")', 'print("Bloc 5 — repli R1 (attendu), trois cas")'),
('ligne("surcoût reformulateur Argon 2/10 (§ 5 écrit +0,84)", 0.84,', 'ligne("surcoût reformulateur Argon 2/10 (v3 : +0,00)", 0.00,'),
('for m, nom in (("argon_nov", "2/10"), ("argon_dec", "4/20")):\n    relect_argon', 'kimi_echoue = {}\nfor m, nom, dv in (("argon_nov", "2/10", 0.00), ("argon_dec", "4/20", 7.50)):\n    relect_argon'),
('    ligne(f"repli « Kimi échoue », surcoût attendu, Argon {nom} (absent du devis)", None, sur)',
 '    kimi_echoue[nom] = sur\n    ligne(f"repli « Kimi échoue », surcoût attendu, Argon {nom}", dv, sur)'),
('for m, nom, tot in (("argon_nov", "2/10", "total_nov"), ("argon_dec", "4/20", "total_dec")):\n    relect_sur',
 'deux_echouent = {}\nfor m, nom, tot, dv in (("argon_nov", "2/10", "total_nov", 142.85), ("argon_dec", "4/20", "total_dec", 155.88)):\n    relect_sur'),
('    ligne(f"repli « les deux échouent », total attendu, Argon {nom} (absent du devis)", None, poste["attendu"][tot] - poste["attendu"]["P1"] + relect_sur)',
 '    deux_echouent[nom] = poste["attendu"][tot] - poste["attendu"]["P1"] + relect_sur\n    ligne(f"repli « les deux échouent », total attendu, Argon {nom}", dv, deux_echouent[nom])\n    ligne(f"repli « Kimi échoue », total attendu, Argon {nom} (non écrit au devis)", None, poste["attendu"][tot] + kimi_echoue[nom])'),
# bloc 6
('ligne("Argon 2/10, juge Kimi, si l\'on ajoutait le +0,84 du texte", 147.89, sens["2/10"][1] + 0.84)\n', ''),
# bloc 7
('ligne("attendu avec lignes conditionnelles, Argon 2/10 (non écrit)", None, att_cond_nov)', 'ligne("attendu avec lignes conditionnelles, Argon 2/10", 184.99, att_cond_nov)'),
('ligne("réserve des appels en vol (3 × 1,50 + 2 × 0,32 + 0,576)", 5.72, reserve_devis)', 'ligne("réserve formule v2 (3 × 1,50 + 2 × 0,32 + 0,576), abandonnée", 5.72, reserve_devis)'),
('ligne("réserve, logique du script v1 (relecteur Kimi au pire compté)", 5.72, reserve_v1_logique)', 'ligne("réserve v3 = logique v1 (relecteur Kimi au pire compté)", 5.93, reserve_v1_logique)'),
('brut = att_cond * 1.5 + reserve_devis\nligne("attendu avec conditionnelles × 1,5 + réserve (non arrondi)", 294.91, brut)\nligne("même calcul sur les valeurs arrondies du devis (192,79 × 1,5 + 5,72)", 294.91, 192.79 * 1.5 + 5.72)\nplafond = math.ceil(brut / 10) * 10',
 'brut_v2 = att_cond * 1.5 + reserve_devis\nbrut = att_cond * 1.5 + reserve_v1_logique\nligne("192,79 × 1,5 + réserve v3 5,93, valeurs exactes (devis écrit 294,90)", 294.90, brut)\nligne("même calcul sur les valeurs arrondies (192,79 × 1,5 + 5,93)", 294.90, 192.79 * 1.5 + 5.93)\nligne("même calcul avec l\'ancienne réserve 5,72, valeurs exactes", 294.90, brut_v2)\nplafond = math.ceil(brut / 10) * 10'),
('ligne("plafond d\'appels, réserve logique v1", 300, math.ceil((att_cond * 1.5 + reserve_v1_logique) / 10) * 10)', 'ligne("plafond d\'appels, ancienne réserve 5,72", 300, math.ceil(brut_v2 / 10) * 10)'),
('ligne("machine 48 h × 1,30 (non arrondi)", 65,', 'ligne("machine 48 h × 1,30 (non arrondi)", 62.40,'),
('"plafond machine (arrondi aux 5 supérieurs, règle du script v1, non écrite au v2)"', '"plafond machine (arrondi aux 5 supérieurs, règle écrite au v3)"'),
]
for a, b in R:
    if t.count(a) != 1:
        sys.exit(f"motif non unique ou absent ({t.count(a)}) : {a[:80]!r}")
    t = t.replace(a, b)
# bloc 8 : remplacé entièrement
i = t.index('print("Bloc 8')
j = t.index('print("Bloc 9')
bloc8 = '''print("Bloc 8 — intervalle de P7 (devis v3, § 4 ; brouillon 3 : [115,39 ; 261,41])")
P7_BAS_DEVIS, P7_HAUT_DEVIS = 115.39, 261.41
p7_bas_exact = 120 / 164.28 * poste["attendu"]["total_nov"]
p7_haut_exact = 260 / 164.28 * poste["attendu"]["total_dec"]
ligne("borne basse (120 / 164,28) × attendu 30 nov., valeurs exactes", P7_BAS_DEVIS, p7_bas_exact)
ligne("borne haute (260 / 164,28) × attendu 1er déc., valeurs exactes", P7_HAUT_DEVIS, p7_haut_exact)
ligne("borne basse sur l'attendu arrondi 157,97", P7_BAS_DEVIS, 120 / 164.28 * 157.97)
ligne("borne haute sur l'attendu arrondi 165,17", P7_HAUT_DEVIS, 260 / 164.28 * 165.17)
for nom, v, attendu_dedans in (
        ("bas 30 nov.", poste["bas"]["total_nov"], False), ("bas 1er déc.", poste["bas"]["total_dec"], False),
        ("attendu 30 nov.", poste["attendu"]["total_nov"], True), ("attendu 1er déc.", poste["attendu"]["total_dec"], True),
        ("R1 Astra échoue, 2/10", sens["2/10"][1], True), ("R1 Astra échoue, 4/20", sens["4/20"][1], True),
        ("R1 Kimi échoue, 2/10", poste["attendu"]["total_nov"] + kimi_echoue["2/10"], True),
        ("R1 Kimi échoue, 4/20", poste["attendu"]["total_dec"] + kimi_echoue["4/20"], True),
        ("R1 les deux échouent, 2/10", deux_echouent["2/10"], True), ("R1 les deux échouent, 4/20", deux_echouent["4/20"], True),
        ("attendu avec conditionnelles 4/20", att_cond, True), ("attendu avec conditionnelles 2/10", att_cond_nov, True),
        ("pire 30 nov.", poste["pire"]["total_nov"], False), ("pire 1er déc.", poste["pire"]["total_dec"], False),
        ("plafond d'appels", float(plafond), False)):
    dedans = P7_BAS_DEVIS <= v <= P7_HAUT_DEVIS
    ok = "conforme au devis" if dedans == attendu_dedans else "CONTRAIRE AU DEVIS"
    print(f"   {nom:36s} {v:8.2f}  {'dans' if dedans else 'HORS de'} [115,39 ; 261,41]  ({ok})")
    if dedans != attendu_dedans:
        ecarts.append((f"P7 : {nom}", float(attendu_dedans), float(dedans)))
print()

'''
t = t[:i] + bloc8 + t[j:]
t = t.replace('print("Bloc 9 — contrôles d\'effectifs du brouillon 2 (P9 et garde A4), sans donnée")', 'print("Bloc 9 — contrôles d\'effectifs du brouillon 3 (P9 et garde A4), sans donnée")')
open(p, "w", encoding="utf-8").write(t)
