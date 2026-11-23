"""Devis de l'épreuve plantée des sondes v2, version 2 (calcul sur les durées mesurées, sans donnée de monde planté).

Modèle écrit (plan v2, § 5), appliqué tel quel partout (correction du défaut 6 de la contre-lecture) :
- étalon, monde « identité seule » : 1 300 × (0,52 + 0,0034 × TA) s par réplique pour les 52 cases (paires × familles) ;
- étalon, six autres mondes : 50 s par monde et par réplique pour les 52 cases ;
- complet : 108,6 × (TA_rejeu / 24)^1,09 s par réplique et par monde, huit mondes ; facteur 0,06 + 0,94 × R/199 pour R rejeux.
Prix : ccx63 à hel1, 1,3942 EUR/h toutes taxes (le plus haut relevé : 1,9932), 48 cœurs, taux 1,25 (relevé du 11 novembre)."""
REPLIQUES = 500
EUR, EUR_MAX, TAUX, COEURS = 1.3942, 1.9932, 1.25, 48

def identite(ta):
    return 1300 * (0.52 + 0.0034 * ta) * REPLIQUES / 3600

def autres_etalon():
    return 50 * 6 * REPLIQUES / 3600

def complet(ta, rejeux=199):
    return 8 * REPLIQUES * 108.6 * (ta / 24) ** 1.09 * (0.06 + 0.94 * rejeux / 199) / 3600

def usd(h, prix):
    return h * prix / COEURS * TAUX

def ligne(nom, h):
    return f"{nom};{h:.0f};{usd(h, EUR):.1f};{usd(h, EUR_MAX):.1f};{h / COEURS:.1f}"

print("poste;heures_de_processeur;usd;usd_au_plus_haut;heures_sur_une_ccx63_reparties")
for ta_e, ta_c, nom in ((32, 24, "petit"), (64, 48, "moyen"), (128, 96, "grand"), (128, 192, "tres_grand")):
    e = identite(ta_e) + autres_etalon()
    print(ligne(f"{nom}_A_partout", e + complet(ta_c)))
    print(ligne(f"{nom}_A_etalon_C_complet", e + complet(ta_c, 39)))
# extension de la grille : 416 cases = 52 × tâches (8, 16, 32, 64) × actions (1, 2) ; elle remplace la grille de 52
ext = sum(identite(t * a) + autres_etalon() for t in (8, 16, 32, 64) for a in (1, 2))
print(ligne("extension_416_cases_etalon_seul", ext))
for ta_c, nom in ((24, "petit"), (48, "moyen"), (96, "grand"), (192, "tres_grand")):
    print(ligne(f"extension_plus_complet_{nom}_C", ext + complet(ta_c, 39)))
# part de la sonde d'identité dans l'extension, et effet d'un gain de vitesse sur elle seule
ext_id = sum(identite(t * a) for t in (8, 16, 32, 64) for a in (1, 2))
print(f"part_identite_dans_extension;{ext_id / ext:.3f}")
for g in (2, 4):
    print(ligne(f"extension_identite_{g}_fois_plus_rapide", ext - ext_id + ext_id / g))
