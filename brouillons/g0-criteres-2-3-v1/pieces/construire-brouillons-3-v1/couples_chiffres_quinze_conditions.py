"""Couples « ancien -> nouveau » des chiffres qui suivent le passage de treize à quinze conditions (1 920 épisodes) :
section « Devis » du préenregistrement et devis d'une page. Arithmétique : `calcul-devis-quinze-conditions.txt`."""
P, G, V = "T0.6-organisme-consigne-cachee-dose-reponse-v1", "G0-critere-3-designation-course-v1", "devis-dose-reponse-consigne-cachee-v1"
COUPLES = [
 # ---- préenregistrement, section « Devis »
 (P, "CH-1", "| épisodes | 1 664, à 40,2 à 42,8 s l'un en lots de 8 | 18,6 à 19,8 h |", "| épisodes | 1 920, à 40,2 à 42,8 s l'un en lots de 8 | 21,4 à 22,8 h |"),
 (P, "CH-2", "| passe d'activations | 1 664 × 0,45 s | 0,2 h |", "| passe d'activations | 1 920 × 0,45 s | 0,2 h |"),
 (P, "CH-3", "| **marche totale** | | **≈ 20,0 à 21,2 h** |", "| **marche totale** | | **≈ 22,9 à 24,3 h** |"),
 (P, "CH-4", "Calcul : 21,8 à 27,6 dollars. Disque (250 Go au moins) : au plus 1,7 pendant la marche", "Calcul : 24,9 à 31,6 dollars. Disque (250 Go au moins) : au plus 1,9 pendant la marche"),
 (P, "CH-5", "- **Attendu : 23 à 37 dollars** (valeur centrale ≈ 28). Pire cas (hôte deux fois plus lent au prix plafond, une reprise) : ≈ 73 dollars. **Plafond : 80 dollars** ; alerte à Lazar à 64.",
  "- **Attendu : 26 à 41 dollars** (valeur centrale ≈ 32). Pire cas (hôte deux fois plus lent au prix plafond, une reprise) : ≈ 81 dollars. **Plafond : 90 dollars** ; alerte à Lazar à 72."),
 (P, "CH-6", "- Options écrites au devis : une réplique au lieu de deux (attendu 13 à 24 dollars, puissance moindre) ; deux contrôles croisés de plus (3 à 4 dollars).",
  "- Options écrites au devis : une réplique au lieu de deux (attendu 14 à 25 dollars, puissance moindre) ; deux contrôles croisés de plus (3 à 4 dollars) ; sans les deux témoins instruits du premier test (3 à 4 dollars de moins, plafond 80)."),
 # ---- devis d'une page
 (V, "CH-10", "Accorder la dépense de calcul d'une course de 1 664 épisodes sur une carte louée, **attendu 23 à 37 dollars, plafond 80 dollars**.",
  "Accorder la dépense de calcul d'une course de 1 920 épisodes sur une carte louée, **attendu 26 à 41 dollars, plafond 90 dollars**."),
 (V, "CH-11", "| épisodes | 13 conditions × 64 tâches × 2 répliques = 1 664 | 18,6 à 19,8 h |", "| épisodes | 15 conditions × 64 tâches × 2 répliques = 1 920 | 21,4 à 22,8 h |"),
 (V, "CH-12", "| passe d'activations | 1 664 épisodes × 0,45 s | 0,2 h |", "| passe d'activations | 1 920 épisodes × 0,45 s | 0,2 h |"),
 (V, "CH-13", "| **marche totale** | | **≈ 20,0 à 21,2 h** | |", "| **marche totale** | | **≈ 22,9 à 24,3 h** | |"),
 (V, "CH-14", "(activations : ≈ 91 Go attendus pour trois couches, ≈ 164 Go au pire cas de 400 jetons par action)", "(activations : ≈ 104 Go attendus pour trois couches, ≈ 189 Go au pire cas de 400 jetons par action)"),
 (V, "CH-15", "- **Calcul** : 20,0 à 21,2 h × 1,0889 à 1,30 = **21,8 à 27,6 dollars** ; valeur centrale ≈ 24.", "- **Calcul** : 22,9 à 24,3 h × 1,0889 à 1,30 = **24,9 à 31,6 dollars** ; valeur centrale ≈ 28."),
 (V, "CH-16", "pendant la marche, au plus 0,08 dollar de l'heure (≤ 1,7) ;", "pendant la marche, au plus 0,08 dollar de l'heure (≤ 1,9) ;"),
 (V, "CH-17", "- **Attendu : 23 à 37 dollars** (valeur centrale ≈ 28).", "- **Attendu : 26 à 41 dollars** (valeur centrale ≈ 32)."),
 (V, "CH-18", "sur l'attendu haut : 48 dollars.", "sur l'attendu haut : 54 dollars."),
 (V, "CH-19", "42,4 h × 1,30 = 55,1 ; disque 9,2 ; téléchargement 2 : **≈ 66 dollars**. Avec une reprise après une panne de chaîne (nouvelle mise en place au débit moitié, 2,4 h ; un bloc de 26 épisodes rejoué, 0,6 h ; soit 3,0 h × 1,30 ≈ 3,9 ; téléchargement 2 ; disque 0,3) : **≈ 73 dollars**.",
  "48,5 h × 1,30 = 63,1 ; disque 9,6 ; téléchargement 2 : **≈ 75 dollars**. Avec une reprise après une panne de chaîne (nouvelle mise en place au débit moitié, 2,4 h ; un bloc de 30 épisodes rejoué, 0,7 h ; soit 3,1 h × 1,30 ≈ 4,0 ; téléchargement 2 ; disque 0,3) : **≈ 81 dollars**."),
 (V, "CH-20", "- **Plafond demandé : 80 dollars**, arrêt de l'instance par son identifiant à ce cumul ; alerte à Lazar à 64 dollars (80 %).",
  "- **Plafond demandé : 90 dollars**, arrêt de l'instance par son identifiant à ce cumul ; alerte à Lazar à 72 dollars (80 %)."),
 (V, "CH-21", "- **(b) Une réplique.** 832 épisodes, 10,6 à 11,2 h : attendu 13 à 24 dollars, plafond 45.", "- **(b) Une réplique.** 960 épisodes, 12,0 à 12,7 h : attendu 14 à 25 dollars, plafond 50."),
 (V, "CH-22", "Sans eux, deux lectures de validité du texte scellé des sondes restent en attente.",
  "Sans eux, deux lectures de validité du texte scellé des sondes restent en attente.\n- **(d) Option (a) sans les deux témoins instruits du premier test.** 256 épisodes de moins : 3 à 4 dollars de moins, plafond 80. Inconvénient : les témoins de consigne ne couvrent plus qu'un seul gabarit, alors qu'un seul témoin ne suffit pas à une lecture de validité (préenregistrement, section 0, choix 5)."),
 (V, "CH-23", "course, environ 21 heures ;", "course, environ 24 heures ;"),
 (V, "CH-24", "(ligne de GO à citer, plafond 80 USD)", "(ligne de GO à citer, plafond 90 USD)"),
 (V, "CH-25", "attendu 23 à 37 USD, pire cas ≈ 73 USD ;", "attendu 26 à 41 USD, pire cas ≈ 81 USD ;"),
 (V, "CH-26", "Le critère 2 de la porte G0 demande une dose–réponse pour l'organisme à consigne cachée ; aucune course ne l'a mesurée.",
  "Le critère 2 de la porte G0 demande une dose–réponse pour l'organisme à consigne cachée ; aucune course ne l'a mesurée. Quinze conditions : l'agent honnête, six intensités écrites, deux proportions de pas désignés, trois témoins de consigne sur le gabarit du préenregistrement, et les trois conditions instruites du premier test (son saboteur, témoin positif, et ses deux témoins, second gabarit)."),
]
