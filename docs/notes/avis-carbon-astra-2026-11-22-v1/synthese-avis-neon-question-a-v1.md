# Synthèse — avis de Neon sur le seuil de 0,75 (question A), 2026-11-22

Sous GO-2026-11-22-109 (plafond 1,50 USD). Même question v2 (51344c2d…). Envoi 17:51:51Z, retour 18:01:46Z. gemini-4-neon, flux, réflexion bornée à 32 768 (31 434 employés), 32 768 de texte ; fin « STOP » ; 1 515 + 37 146 jetons. Coût 0,5617 USD (3 / 15).

## Recommandation
- (b') : diagnostic sans appel de modèle d'abord (poids du classifieur, aires par famille, tables gabarit × strate, classifieur sur l'identifiant de gabarit seul), puis refonte du générateur par appariement des gabarits et des distributions numériques, et remplacement de l'instrument ; (a) symétrisée gardée comme critère secondaire et repli documenté. Rejette (c). Confiance environ 80 % (plus de 90 % contre (c)).
- Instrument : 0,75 non gardé ; trop permissif sur une aire globale, trop sensible sur le maximum des aires par strate ; à la place, invariant de proportions par gabarit et par famille, deux sondes (lexicale et numérique), aire globale ≤ 0,60 et rappel à 10 % de fausses alarmes ≤ 0,20, sur la borne haute d'un intervalle par graines.

## Points qui contredisent ou limitent (b) ou le repli (a) symétrisé
- Contre (b) : si les indices du classifieur ne se transfèrent pas à un modèle qui lit un énoncé à la fois, la refonte peut être disproportionnée ; si l'appariement rend les vrais triviaux dans une famille, (b) crée un biais neuf (fausses alarmes abaissées) ; si l'aire vient d'un défaut de la sonde (métadonnée, fuite entre plis), (b) est inutile, d'où le diagnostic d'abord ; si le protocole est gelé, (a) stricte s'impose.
- Contre (a) symétrisée : même symétrisée, elle change la question (détection en calcul effectif) ; sur les vrais, les fausses alarmes tombent à zéro par construction si on ne les compte pas sur les verdicts bruts ; l'effet de forme reste un guide de l'effort de recherche du bras avec outil (il sait quand chercher au-delà de N), donc gonfle son rappel certifié.
- Hors (a) et (b) : le relecteur d'une autre famille confond l'effet de l'outil ; un bras « nu + même relecteur » ou le retrait du relecteur serait nécessaire pour isoler l'outil.
