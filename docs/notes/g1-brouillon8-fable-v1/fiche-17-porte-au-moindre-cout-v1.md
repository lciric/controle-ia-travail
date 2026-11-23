# Fiche 17 — La porte au moindre coût (demande de la mère après le mot de Lazar « c'est cher ») — v1

Classe C. Complète la note des nœuds v1 (inchangée). Aucune recommandation sur l'énoncé du critère contre le véhicule. Calculs : `calculs/calculs-g1-brouillon8-v1-complement-4.py` et sa sortie, lois supposées, aucune donnée du programme, rejoués à l'identique (graine racine 20261123). Écrite le 23 novembre 2026.

**Décision.** Choisir jusqu'où réduire la porte G1 pour qu'elle coûte moins, en sachant ce que chaque économie retire à ce qu'elle peut établir.

**Enjeu.** Le plafond accordé est d'environ 7 600 USD ; le défaut est à 6 331 avec la marge. Réduire est possible sans toucher le critère, mais chaque réduction retire une information ou un contrôle.

**Faits (calcul, § 1, modèle de coût du brouillon 6, central ; avec la marge de 1,3 entre parenthèses).**
- Défaut accordé : 400 tâches, 232 épisodes par tâche (10 jumeaux honnêtes ; 60 sabotés = 3 modes × 10 × 2 familles ; 12 témoin et mention ; 150 de calibrage) : 92 800 épisodes, 4 870 USD (6 331).
- Défaut + garde du critère contre le véhicule, 10 exécutions du témoin dans les 2 cellules de la porte : 5 374 (6 986). Garde à 1 exécution par unité, 6 cellules : 4 996 (6 495). Contraste minimal (300 épisodes de calibrage du témoin par cellule) : 5 468 (7 109).
- Le calibrage honnête pèse 65 % des épisodes : c'est le premier levier.

**Les économies, une par une** (A à D se cumulent).
- **A. Porte seule : retirer le mode « coût » et la famille à consigne de la campagne** (60 → 20 épisodes sabotés par tâche) : 4 030 (5 239). Retire : tout ce que ces deux cellules rapportent (information sur la mesure de H1b entre modes, lecture de l'effet de la consigne, qualification QL2 « gain sur la consigne, non sur l'adaptateur ») ; la porte elle-même est inchangée, puisque ses deux modes décisifs et sa famille restent. Puissance : aucune perte pour la décision.
- **B. Calibrage à 10 fois les unités sabotées au lieu de 15** (150 → 100 par tâche) : 2 981 (3 875). Retire : de la précision de seuil. La conception du pari chiffre l'artefact à 1,4 % par sens à 100 unités sabotées avec 10 fois, contre 3,8 % à 250 avec 16 fois ; la fourchette qu'elle recommande est de 10 à 16, donc 10 est son bord bas, non sa règle de 15 inscrite au brouillon 6. Contrôle des jumeaux en loi (contrôle 12) obligatoire pour lire.
- **C. 288 tâches au lieu de 400** (le minimum que porte le brouillon 6, « au moins 288 unités par mode ») : 2 146 (2 790). Retire : de la marge de puissance (voir § 2) et de la finesse des intervalles ; rien d'autre.
- **D. Sans témoin ni mention** (12 → 0 par tâche) : 1 965 (2 554). Retire : les contrôles de validité par épisodes de la porte (consigne bénigne, mention) ; ces lectures resteraient disponibles sur les épisodes de la campagne de la base boîte noire pour le mode « coût » seulement. La phrase « la boîte blanche ne lit pas la présence d'une consigne » devient « non vérifiée à la porte ».
- **Témoin apparié, ajouté à la variante D** : 1 exécution par unité dans les 2 cellules : 1 995 (2 593) ; 10 exécutions : 2 267 (2 947). Le critère contre le véhicule, sous ses trois énoncés, se paie donc de 30 à 300 USD de plus dans cette variante, avant le calibrage du témoin (fiche 9), qui reste le gros poste du contraste.
- **Moins de comparateurs ou moins de moniteurs notés** : ne se chiffre pas ici. La notation est environ 70 % du coût par épisode ; si elle coûtait moitié moins, le coût par épisode serait multiplié par 0,65 (hypothèse non sourcée). Retirer un comparateur de la liste scellée modifie ta décision du 5 novembre et le critère de N-008 : nœud à part, comparateur par comparateur.
- **Cellules rapportées réduites** : le mode « coût » et la famille à consigne (A ci-dessus), et les cellules « nu » et « à exemples » (une cellule d'information de plus chacune dans le plan du brouillon 6 ; non chiffrées ici, leur part dans les 60 épisodes n'étant pas séparable dans les pièces lues).

**Puissance (calcul, § 2 ; une comparaison, parts binomiales indépendantes, sans hétérogénéité d'unité ni minimum sur douze comparateurs : ce sont des plafonds).** Au seuil 160, écart de rappel 0,10 : 0,66 à 100 unités, 0,97 à 150, 1,00 à 200, à 288 et à 400. Écart 0,20 et 0,30 : 1,00 dès 100 unités. Au seuil 20, comme dans la table de la conception : 0,95 à 100 unités pour 0,10 (la conception donne 0,96, sans seuil 160). Lecture : le nombre de tâches n'est pas le facteur limitant dans ce monde simple ; ce qui l'est, c'est l'hétérogénéité entre unités, le minimum sur douze comparateurs et le calibrage, que ce calcul ne représente pas. La puissance réelle à 288 tâches n'est donc pas établie par cette fiche ; la simulation de la garde appariée à douze comparateurs, déjà notée comme pièce manquante, la donnerait, sans dépense.

**Montants comparés** (avec la marge, USD) : défaut 6 331 ; défaut + garde 6 986 ; défaut + contraste minimal 7 109 ; moindre coût A–D + garde à 1 exécution par unité 2 593 ; A–D + garde à 10 exécutions 2 947. Le calibrage du témoin à l'échelle de l'honnête (fiche 9) n'est pas dans la variante D ; il la porterait à plusieurs milliers de dollars de plus.

**Options.**
- (a) Défaut accordé, sans économie. Avantage : rien n'est retiré. Inconvénient : 6 331 à 7 109 USD.
- (b) A seule. Avantage : la porte et sa puissance sont inchangées ; environ 1 100 USD économisés. Inconvénient : les cellules rapportées disparaissent de la campagne.
- (c) A + B + C (variante « moindre coût » avec témoins et mention) : 2 790 USD avec la marge. Avantage : moins de la moitié du défaut. Inconvénient : un seuil à 10 fois et une puissance non simulée à 288 tâches.
- (d) A à D : 2 554 USD. Avantage : le plus bas. Inconvénient : plus de contrôle de validité des moniteurs par épisodes de la porte.

**Recommandation.** (b) si la décision est de ne rien risquer sur la validité ; (c) si la décision est de payer le moins sans toucher à la liste ni au critère, à condition de faire d'abord la simulation à douze comparateurs. Confiance : 0,6 sur (c), 0,75 sur (b).

**Défaut.** Aucun : dépense et paramètres de porte.

Réserves : la notation et la génération par épisode sont celles du brouillon 6, non remesurées ; le pilote de la couche 2 les rechiffre. Ni le devis des épisodes de qualification de « diffus » (fiche 2) ni les organismes du mode « contrôles affaiblis » (fiche 12) ne sont dans ces montants.
