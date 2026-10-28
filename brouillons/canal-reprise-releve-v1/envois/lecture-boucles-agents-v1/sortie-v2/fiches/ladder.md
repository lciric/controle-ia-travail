# « The Ladder: A Reliable Leaderboard for Machine Learning Competitions » — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Avrim Blum, Moritz Hardt. « The Ladder: A Reliable Leaderboard for Machine Learning Competitions ». Prépublication arXiv 1502.04585, version 1 du 16 février 2015 (seule version) — page de résumé arXiv enregistrée le 26 octobre 2026 à 03:44 UTC ; le PDF est daté du 17 février 2015 (p. 1).
- Lieu de publication : non indiqué sur le PDF ni sur la page arXiv ; à vérifier. « Preserving Statistical Validity in Adaptive Data Analysis » (fiche `reusable-holdout-stoc.md`) le cite comme prépublication (p. 21 de ce PDF-là).

## Fichier lu
- `pdfs/ladder/arxiv-1502.04585v1.pdf`, 308 155 octets, 16 pages ; SHA-256 `957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe` (même empreinte que la v1).
- Pages lues : 1 à 15 (tout le texte), références parcourues.

## Comment la boucle est faite
- Des équipes soumettent à répétition des classifieurs (des listes d'étiquettes) ; un tableau de classement public rend un score calculé sur une part du jeu de test ; les équipes s'en servent pour leurs soumissions suivantes ; le classement final se fait sur une part privée (p. 1 et 2).
- Mécanisme « Ladder » (figure 1, p. 6) : il ne publie une nouvelle perte que si elle bat la meilleure précédente d'au moins un pas η, et l'arrondit au multiple de η ; sinon il republie l'ancienne meilleure valeur.
- Variante sans paramètre (figure 2, p. 10) : le pas devient l'écart type du vecteur des différences de perte, appariées point par point, entre la soumission et la meilleure précédente, divisé par la racine de n ; c'est en substance un test t apparié unilatéral, « roughly at the 0.15 significance level » (p. 10).
- Mémoire : la meilleure perte publiée et le vecteur de pertes de la meilleure soumission (p. 10).

## Traitement du bruit et du sur-ajustement
- Garantie : l'erreur du classement reste en O((log(kn))^(1/3)/n^(1/3)) pour k soumissions et une part publique de taille n, sans limiter le nombre de soumissions (théorème 3.1, p. 6) ; borne inférieure en racine de log(k)/n pour tout estimateur (théorème 3.3, p. 7).
- Le mécanisme habituel (publier chaque score avec une haute précision) a une erreur qui croît avec la racine du nombre de soumissions (p. 2 ; corollaire 5.2, p. 11).
- « Attaque par boosting » (p. 10 et 11) : soumettre des vecteurs aléatoires, garder ceux dont la perte publiée est sous 1/2, voter à la majorité ; le score public s'améliore sans aucune compétence réelle. Simulation : 12 000 étiquettes dont 4 000 pour la part publique, résultats moyennés sur 5 répétitions (figure 3, p. 12) ; le mécanisme habituel est fortement biaisé, « Ladder » beaucoup moins.
- Données réelles (concours Kaggle « Photo Quality Prediction ») : 12 000 exemples de test, 8 400 privés et 3 600 publics, 1 830 soumissions dont 1 785 traitées, 200 équipes (p. 12). Le classement « Ladder » est très proche de celui de Kaggle (p. 12) ; 20 découpages aléatoires de la part privée montrent que les fluctuations dues au découpage sont grandes devant les écarts observés (p. 13) ; tests t appariés avec correction de Bonferroni sur les 10 premiers (p. 14).

## Échecs et limites rapportés par les auteurs
- Le test de signification de la variante sans paramètre est « primarily heuristic » : l'approximation de Student ne vaut plus sous adaptativité, et les comparaisons multiples ne sont pas corrigées (p. 10).
- Écart non résolu entre borne supérieure et borne inférieure (p. 15) ; mécanisme jamais déployé dans un vrai concours au moment de l'écriture (p. 15).
- Une instance par équipe suppose qu'aucune équipe n'utilise plusieurs comptes (p. 6).
- Le jeu réel montre peu de sur-ajustement : c'est un « difficult benchmark » pour démontrer l'utilité du mécanisme (p. 3).

## Vérifié par des tiers
- Non trouvé dans les lectures de cette passe. Roelofs et al. (2019, lu, avec Hardt parmi les auteurs) étudient la réutilisation des jeux de test sur Kaggle mais ne testent pas « Ladder ».

## À emprunter
- Boucle extérieure : déclarer une conception meilleure, et publier son score, seulement si elle bat la meilleure courante d'au moins un pas fixé d'avance (par exemple une erreur type), par comparaison appariée ; sinon republier l'ancien meilleur (p. 6 et 10).
- Boucle intérieure : le score rendu à l'organisme entre générations peut être « en échelle » (arrondi, rendu seulement en cas d'amélioration nette) pour limiter l'information qui fuit de la part `test`.
- Mesure du bruit : l'attaque par boosting (p. 10 et 11) est un test de résistance prêt à l'emploi — une population qui garde les variantes au-dessus du hasard peut faire monter son score `test` par sélection seule.
