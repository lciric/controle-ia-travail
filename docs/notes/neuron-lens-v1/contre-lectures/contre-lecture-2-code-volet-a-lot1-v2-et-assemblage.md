# Contre-lecture 2 du code de la course du volet A (lot 1 v2, assemblage v2) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé après le commit d2bd8245, rapport lu avant 11:44 UTC ; il n'a écrit aucune des pièces ;
lecture seule (essais et `sha256sum` lancés). Pièces : `volet_a_sondes_v2.py` (`4cbc15ee…`), `volet_a_lectures_v2.py` (`1935b93f…`),
`volet_a_course_v2.py` (`c840c0fb…`), essais v2 ; modules inchangés `volet_a_donnees_v1`, `volet_a_extraction_v1`,
`decisions_volet_a_v4`. Empreintes conformes ; essais passés (sondes 13, lectures 12, données 5, course 3).

**Verdicts** : sondes v2 **scellable en l'état** ; lectures v2 **scellable en l'état** (une mineure) ; assemblage v2 **après corrections**
(une bloquante à l'échelle réelle).

**A.** Remarques 1 à 12 de la contre-lecture 1 : traitées ou déclarées ; il manque un essai « aucun groupe coupé par les plis internes ».
**B.** Conformité au texte gelé vérifiée point par point (ordre, cas sains, découpes et graines, A1, A2, A3, A-ii, ordre et types des
arguments des règles scellées, audit R4). Écarts : « vocabulaire entier rapporté à côté » des cas sains (i), (ii) non rendu ; arrêt si
un jeton de P manque (plus strict que « P sans jeton parmi les gardés »).

**C. Remarques**
1. Bloquante (échelle réelle) — l'extracteur met en cache les neurones des 4 couches de chaque invite retirée de A3 (dizaines à
   centaines de Go) : pour A3, extraire la seule couche lue, flux seulement, sans cache des invites retirées ; devis de passes.
2. Moyenne — rien n'est écrit avant `_decider` ; un NaN d'AUROC de A3 fait lever `condition_a3` et perd la course : écrire `brut`
   scellé avant les décisions, par contraste.
3. Moyenne (mémoire) — empreintes en float64 : 8 lectures × 3,4 Go = 27 Go : réduire ou construire par couche ; déclarer la mémoire.
4. Moyenne — `res.U[res.gardes]` copié à chaque lecture R : calculer une fois ; `argsort` stable.
5. Mineure — `searchsorted` suppose les gardés triés ; `IndexError` possible : vérifier l'ordre strict ; déclarer l'arrêt sur un jeton de P absent.
6. Mineure — base d'AUROC de A3 sur tout le test, chute sur les exemples gardés : recalculer sur les gardés, ou déclarer.
7. Mineure — sonde permutée apprise aussi pour C3 sans usage ; direction de C3 = celle de la découpe de même rang : déclarer.
8. Mineure — rendre aussi les 10 premiers sur le vocabulaire entier pour (i) et (ii).
9. Mineure — essai « plis internes groupés » ; la fumée n'exerce ni l'échelle ni une classe A3 trop petite.
10. Info — composantes principales centrées-réduites avant la régression : à déclarer.
11. Info — égalité de C : bien tranchée ; valeurs non finies refusées par les règles scellées.

**D. Manque pour une vraie course** : chargement réel (lentilles, E, U, γ, pièces des cas sains, empreintes) ; manifeste R9 (versions,
graines, commit, avertissements) ; mesure du coût processeur (A-ii, sondes de 4 096 traits, produits sur 3,4 Go, ≈ 0,6 million d'AUROC
de l'intervalle apparié), parallélisation par couche ; gardes de dépense, minuterie, GO cité ; audit R4 (sixième découpe, direction
permutée sans P) non codé ; rapport final scellé ; base « longueur seule » ; liste de mots de A.5.
