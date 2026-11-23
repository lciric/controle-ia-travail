# Synthèse — avis de Carbon et d'Astra sur le seuil de 0,75 (question A), 2026-11-22

Sous GO-2026-11-22-105 (plafond 3,90 USD). Question servie : question-a-seuil-classifieur-de-style-v2.md (51344c2d…). Envoi 17:41:54Z, retours 17:44Z (Astra) et 17:47Z (Carbon). Réponses brutes versées à côté (.md, .json, journaux), scellées.

## Astra (gpt-6.2-astra, effort xhigh, fin « completed », 1 410 + 6 036 jetons dont 4 471 de réflexion)
- Recommande (b) avant tout appel de modèle, et (a) si le générateur reste tel quel ; rejette (c). Confiance élevée contre (c), modérée sur la faisabilité de (b).
- Garder 0,75 comme engagement du protocole actuel ; publier les deux aires ; pour la suite, critère d'usage : rappel du classifieur de forme à au plus 10 % de fausses alarmes, seuil calibré sur des mondes séparés.
- (a) : ne jamais restreindre le dénominateur ; « vérifié outil contre brut nu » est une borne inférieure du gain de rappel brut ; fausses alarmes comptées sur les verdicts bruts. Premier contrôle : table famille × gabarit × strate.

## Carbon (gemini-4-carbon, réflexion 32 768, fin « STOP », 1 515 + 22 782 jetons dont 17 550 de réflexion)
- Recommande (b) élargie (appariement exact des gabarits entre vrais, faux tôt et pièges, bornes en constantes nommées du monde), avec (a) symétrisée en co-analyse et repli préspécifié ; rejette (c) et (a) seule. Confiance 85 % sur la méthode, 70 % sur la faisabilité.
- Seuil 0,75 mal calibré : l'aire ne dit pas le rappel au régime de fausses alarmes du test ; le jeton « NUM » rend le classifieur aveugle aux grandeurs (un grand littéral ne peut pas expliquer l'aire actuelle) ; remplacer par rappel à 5 % de fausses alarmes < 0,15 et aire moyenne ≤ 0,65, trois classifieurs, traits numériques, intervalle sur ≥ 40 graines.
- (a) inéquitable : imposer un témoin au bras nu et le passer au même vérificateur, garder les fausses alarmes sur tous les « faux » ; puissance tendue sous (a) si les pièges ne sont pas résolus au-delà de N. Contrôles : poids du classifieur, aire par famille, bases déterministes de recherche de témoins, calcul de puissance.

## Accords et désaccords
- Accord : (b) d'abord, (c) rejetée, fausses alarmes sur verdicts bruts, critère de rappel à faible taux de fausses alarmes plutôt que l'aire seule, table gabarit × strate.
- Désaccord : Astra garderait 0,75 comme engagement du protocole actuel ; Carbon ne le garderait pas en l'état. Astra lit (a) comme borne inférieure utile ; Carbon la juge inéquitable sans symétrisation.
- À vérifier par l'équipe (non vérifié ici) : l'argument de Carbon sur le jeton « NUM » (dépend du code réel du classifieur) ; ses chiffres de puissance sont des ordres de grandeur.

## Coût
Carbon 0,4617 USD (4 / 20). Astra 0,2527 USD au prix de 8 / 40 (R-4905), 0,3159 au prix haut du script (10 / 50). Total 0,71 USD (0,78 au prix haut), sous 3,90.
