# Question — D-ML-1 : taille du jeu bénin — v1

Session-depot, 31 octobre 2026, sur le mot direct de Lazar (« demande a conv et collisionneur »). Les répondants ne tranchent rien : Lazar décide.

**Décision.** Le préenregistrement exige 1 000 entrées bénignes pour fixer le seuil de 1 % de fausses alertes et 1 000 autres pour la mesure, disjointes de l'entraînement de la sonde ; le jeu public de référence n'en a que 1 000 en tout, dont 800 servent à entraîner la sonde. Options : **(A)** verser un jeu bénin public plus large (aucun n'est encore choisi ni sur disque) ; **(B)** garder le seul jeu de référence, découpé 400 / 300 / 300 (sonde / seuil / mesure).

**Ce qu'on demande.**
1. Laquelle choisirais-tu, (A), (B) ou une troisième (par exemple validation croisée ou rééchantillonnage pour fixer le seuil, seuil fixé sur une autre statistique, autre découpage), et pourquoi ? Vérifie les intervalles du calcul servi.
2. Pour (A) : quels jeux bénins publics conviendraient (nom, taille, licence — SUPPOSÉ si tu ne les as pas lus), et quel test de ressemblance de distribution avec les bénins d'entraînement de la sonde faudrait-il préenregistrer ? Quel est le risque qu'un jeu plus large mais de distribution différente fausse le seuil plus que la petite taille de (B) ?
3. Pour (B) : la lecture des seuils de détection à 20 % et 5 % reste-t-elle interprétable avec 300 bénins au seuil ? Que faudrait-il rapporter ?
4. Le pire cas de ton choix, et ce qui te ferait changer d'avis.
Niveau statistique et méthode seulement.
