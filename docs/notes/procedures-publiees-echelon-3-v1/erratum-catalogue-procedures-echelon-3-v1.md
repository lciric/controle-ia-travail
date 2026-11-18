# Erratum — catalogue des procédures publiées (échelon 3), v1

Fichier visé : `docs/notes/procedures-publiees-echelon-3-v1/catalogue-procedures-echelon-3-v1.md`, scellé
(`a267b7240c496cc5df06caac1bcc49255b98fbbaa9ab8075016e7deebb01c8c0`, commit `1844c9e3`). Il n'est pas réécrit (R12).

Les heures de l'en-tête de statut sont fausses. Il dit « tirée du brouillon 3 […] le 18 novembre 2026 vers 04:25 UTC » et
« scellée le 18 novembre 2026 vers 04:40 UTC ». Les heures réelles :
- v1 écrite vers 04:13 UTC ;
- scellée et commitée à 04:16:23 UTC (`git log -1 --format=%cI 1844c9e3`).

La session « attaquant informé » avait écrit ces heures d'estime, sans relever `date -u`. La vérification neuve du
plan v1 de la pièce 4 l'a relevé. Le fond du catalogue n'est pas touché.
