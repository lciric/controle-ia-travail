# R-5018 : Argon et Carbon à 4 USD par million d'entrée et 20 de sortie, réflexion comprise (page de prix de Google versée sur
# main, docs/sources/prix/page-prix-gemini-api-20261122T104129Z.html, d3aa716e…, l. 153-163 et 372-382).
_n = src.count('"--prix-entree", "8.3", "--prix-sortie", "41.5", "--niveau-reflexion"')
assert _n == 2, _n  # Argon et Carbon
src = src.replace('"--prix-entree", "8.3", "--prix-sortie", "41.5", "--niveau-reflexion"', '"--prix-entree", "4", "--prix-sortie", "20", "--niveau-reflexion"')
r('''# pire cas d'un appel : 2 618 × 8,3 + 65 536 × 41,5, par million = 2,741473 USD (sous 3,00).''',
  '''# R-5018 (4 / 20 USD par million, réflexion comprise) : un appel estimé 2 618 × 4 + (20 000 + 3 500) × 20, par million =
# 0,480472, arrondi 0,4805 ; pire cas : 2 618 × 4 + 65 536 × 20, par million = 1,321192 USD (la commande compte la réflexion
# dans la sortie maximale) ; 1,894632 si la réflexion était facturée en plus de la sortie maximale ; sous 3,00 dans les deux cas.''')
r('''                      "prop-carbon": 0.997, "aiguilleur": 0.031,''', '''                      "prop-carbon": 0.4805, "aiguilleur": 0.031,''')
r('''DEVIS_V5_TOTAL = {"cinq_especes": 49.112, "six_especes": 56.8144}  # v11 : + 16 × (0,997 − 0,4985) = + 7,976''',
  '''DEVIS_V5_TOTAL = {"cinq_especes": 40.848, "six_especes": 48.5504}  # v11 (R-5018) : + 16 × (0,4805 − 0,4985) = − 0,288''')
r('''# (port 8788, modèle gemini-4-argon). Réglages : niveau « high », provision 24 576, sortie 45 056 (texte 20 480 ≥ 16 000 et
# > 2 × 9 000 caractères) ; prix de l'enveloppe d'Argon v5 (8,3 / 41,5, sortie SUPPOSÉE) ; la provision est une HYPOTHÈSE à
# fixer par le devis v11 (aucune pensée d'Argon au niveau « high » n'est relevée dans les pièces lues).''',
  '''# (port 8788, modèle gemini-4-argon). Réglages : niveau « high », provision 24 576, sortie 45 056 (texte 20 480 ≥ 16 000 et
# > 2 × 9 000 caractères) ; prix 4 / 20 USD par million, réflexion comprise (R-5018) ; la commande compte la réflexion dans la
# sortie maximale : pire cas d'un juge = entrée + 45 056 × 20 / 10⁶ ≈ 0,92 USD ; la provision est une HYPOTHÈSE (aucune pensée
# d'Argon au niveau « high » n'est relevée dans les pièces lues).''')
src = src.replace("Réglages de Carbon : niveau « high », provision 28 672, **sortie 65 536**", "Réglages de Carbon : niveau « high », provision 28 672, **sortie 65 536**")
r('''7. devis interne : Carbon à 0,997 USD par appel (même pensée et réponse que le devis v8, sans remise de lot) ;''',
  '''7. devis interne : Carbon à 0,4805 USD par appel (même pensée et réponse que le devis v8, prix 4 / 20 de R-5018, sans remise
   de lot) ; Argon et Carbon déclarés à 4 / 20 USD par million, réflexion comprise (R-5018) ;''')
