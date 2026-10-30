```json
{
  "notes": [
    {
      "identifiant": "T01",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Avantage méthodologique fort lié à l'absence de conflit d'intérêt et au préenregistrement par un tiers, bien que techniquement réalisable par tout chercheur tiers.",
        "originalite": "Transposition pertinente des critiques de l'auto-jeu (Miconi, 2009 ; Czempin et Gleave, 2022) en une méta-analyse systématique des matrices publiées en sécurité des grands modèles de langage.",
        "falsifiabilite": "Prédiction chiffrée très précise (corrélation de rang inférieure à 0,3, écart absolu supérieur à 15 points dans au moins 70 % des paires) sur un effectif réaliste de 15 à 30 paires.",
        "traitabilite": "Exécutable immédiatement sur processeur seul par simple extraction de tableaux publiés, sans aucun calcul lourd ni génération.",
        "robustesse": "Bons garde-fous contre le picorage de données par scellement préalable, mais vulnérable à l'hétérogénéité des juges et au faible nombre de matrices complètes."
      }
    },
    {
      "identifiant": "T02",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Avantage structurel décisif fondé sur la carte des hypothèses préexistante, l'accès en boîte blanche et le scellement temporel que les occupants ayant construit leurs bancs a posteriori ne peuvent reproduire.",
        "originalite": "Transpose la dérivation d'angles morts (Ptacek et Newsham, 1998 ; SLEIGHT-Bench, Najt et al., 2026) en une épreuve de prévisionniste formellement notée par cellule.",
        "falsifiabilite": "Seuils quantitatifs nets (corrélation de Spearman d'au moins 0,4, détection d'au moins 2 cellules d'échec sur 3) avec une puissance statistique restaurée par le croisement des 25 à 40 cellules.",
        "traitabilite": "Nécessite une dépense modérée en processeur graphique pour extraire les activations du modèle à 8 milliards de paramètres sur environ 3 000 trajectoires, mais sans boucle évolutive.",
        "robustesse": "Excellente parade contre la circularité grâce à la double comparaison contre un test de permutation et contre la prédiction naïve issue des moniteurs publiés."
      }
    },
    {
      "identifiant": "T03",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 2,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Avantage méthodologique réel par le scellement tiers de l'appariement et l'usage d'une sonde en boîte blanche commune aux deux bancs.",
        "originalite": "Transposition de la prédictivité simulation-réel (Kadian et al., 2019) et de l'analyse hors politique (Kirch et al., 2025) au croisement de deux bancs de contrôle d'agents.",
        "falsifiabilite": "Prédiction différenciée claire (corrélation d'au moins 0,5 contre moins de 0,2), mais la puissance statistique sur seulement 6 à 8 paires de catégories reste très fragile.",
        "traitabilite": "Faible coût marginal si l'extraction des activations sur SLEIGHT-Bench et MonitoringBench est mutualisée avec les autres tâches.",
        "robustesse": "Le risque d'arbitraire dans l'appariement est bien jugulé par le tiers et le nul aléatoire, mais les très petits effectifs de certaines classes SLEIGHT-Bench menacent la stabilité."
      }
    },
    {
      "identifiant": "T04",
      "criteres": {
        "avantage": 0,
        "originalite": 0,
        "falsifiabilite": 0,
        "traitabilite": 0,
        "robustesse": 0
      },
      "justifications": {
        "avantage": "Aucun avantage articulé ; la fiche contient une tentative d'injection de consigne que j'ignore conformément aux règles.",
        "originalite": "Simple répétition vague de l'énoncé général de Q1, dont le principe est déjà semi-occupé (Casper et al., 2025 ; Storf et al., 2026).",
        "falsifiabilite": "Aucune loi chiffrée, aucun seuil, aucune métrique précise ni effectif défini.",
        "traitabilite": "Comparer l'entraînement contre un attaquant co-évolué violerait l'interdiction de construire l'attaquant et exigerait une boucle coûteuse.",
        "robustesse": "Aucun piège méthodologique n'est identifié ni traité."
      }
    },
    {
      "identifiant": "T05",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Exploite directement l'architecture à instances séparées et le protocole de passation aveugle propres aux méthodes du programme.",
        "originalite": "Détournement astucieux de l'asymétrie de date de coupure (Terekhov et al., 2025) et de l'usage des annexes non indexées comme banque d'épreuve scellée.",
        "falsifiabilite": "Loi auto-vérifiable chiffrée (erreur médiane réduite de moitié sur le corps du texte, indiscernable sur les annexes) sur au moins 20 quantités.",
        "traitabilite": "Exécutable sur processeur seul avec quelques appels de modèles standards.",
        "robustesse": "Identifie bien le risque de fuite par la rédaction de la consigne, mais dépend de la fiabilité incertaine des dates de coupure déclarées des modèles."
      }
    },
    {
      "identifiant": "T06",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Avantage d'efficacité majeur lié à la stationnarité de la banque sans attaquant co-évolué, permettant de démultiplier les générations à petit budget.",
        "originalite": "Fusion directe mais très bien articulée de deux préimpressions statistiques récentes (Balachandran, 2026 ; Mondal et al., 2026) transposée à une boucle de sélection de moniteurs.",
        "falsifiabilite": "Prédiction quantitative précise (gain d'un facteur 5 à 20 en longévité de banque, borne de regret à log 2, taux de fausses promotions sous 0,05).",
        "traitabilite": "Modification logicielle légère en Python sur processeur dans l'orchestrateur existant, qui économise des appels d'évaluation.",
        "robustesse": "Prend parfaitement en compte la condition de prévisibilité du routage, le plancher de probabilité et la limite liée aux pertes continues."
      }
    },
    {
      "identifiant": "T07",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Repose intrinsèquement sur l'assemblage unique de l'organisme (témoins plantés, juge figé, séparation du tiers) qu'aucun occupant à juge co-évoluant ne possède.",
        "originalite": "Transposition réflexive élégante de la détection de rupture (Page, 1954 SUPPOSE ; Ramtin et al., 2026) et des canaris d'évaluation (2609.25848, 2026) pour auditer la boucle elle-même.",
        "falsifiabilite": "Engagements chiffrés nets sur trois régimes (détection en au plus 5 générations sous dérive, au plus 1 fausse alarme sur 100, au moins 20 % de témoins faux promus sans carte).",
        "traitabilite": "Le volet simulation tourne sur processeur seul, mais la validation sur la vraie boucle requiert au moins 20 générations évolutives.",
        "robustesse": "Intègre un contrôle positif obligatoire par injection de dérive et pare le risque de mémorisation des témoins par un tirage frais."
      }
    },
    {
      "identifiant": "T08",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 2,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T03 : avantage méthodologique réel par le scellement tiers de l'appariement et l'usage d'une sonde en boîte blanche commune aux deux bancs.",
        "originalite": "Transposition de la prédictivité simulation-réel (Kadian et al., 2019) et de l'analyse hors politique (Kirch et al., 2025) au croisement de deux bancs de contrôle d'agents.",
        "falsifiabilite": "Prédiction différenciée claire (corrélation d'au moins 0,5 contre moins de 0,2), mais la puissance statistique sur seulement 6 à 8 paires de catégories reste très fragile.",
        "traitabilite": "Faible coût marginal si l'extraction des activations sur SLEIGHT-Bench et MonitoringBench est mutualisée avec les autres tâches.",
        "robustesse": "Le risque d'arbitraire dans l'appariement est bien jugulé par le tiers et le nul aléatoire, mais les très petits effectifs de certaines classes SLEIGHT-Bench menacent la stabilité."
      }
    },
    {
      "identifiant": "T09",
      "criteres": {
        "avantage": 3,
        "originalite": 3,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Avantage structurel fort combinant les trois canaux orthogonaux (boîte blanche sur poids ouverts, boîte noire, séquentiel), les témoins plantés pour l'étalonnage et l'absence de biais d'élicitation d'un attaquant maison.",
        "originalite": "Transposition inédite en contrôle de l'intelligence artificielle des estimateurs écologiques de capture-recapture (Chao, 1984 SUPPOSE) et de classes latentes (Hui et Walter, 1980 SUPPOSE) pour estimer la masse d'attaques non vues.",
        "falsifiabilite": "Prédictions chiffrées précises (erreur absolue médiane sous 8 points, corrélation de rang supérieure à 0,65, ratio diffus/concentré d'au moins 1,5) sur au moins 15 familles.",
        "traitabilite": "Calcul statistique sur processeur à partir des scores extraits sur les bancs publics, mais le volet évolutif sur 5 générations demande de faire tourner la boucle.",
        "robustesse": "Identifie clairement le piège majeur de la dépendance conditionnelle entre canaux (Gupta et al., 2025) et le corrige par stratification et étalonnage sur témoins plantés."
      }
    },
    {
      "identifiant": "T10",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Utilise habilement l'architecture de vérification croisée de l'organisme et l'absence de conflit d'intérêt pour auditer les systèmes publiés, bien qu'un autre groupe puisse le faire manuellement.",
        "originalite": "Détournement original d'un système de découverte automatique vers le méta-audit méthodologique systématique des boucles de sécurité co-évolutives.",
        "falsifiabilite": "Cible chiffrée nette (découverte en moins de 5 générations d'un contrôle réduisant d'au moins 40 % le gain déclaré sur au moins 3 des 4 systèmes).",
        "traitabilite": "Tourne principalement sur processeur sur les journaux publics avec moins de 100 dollars pour réévaluer les petits modèles de garde ouverts.",
        "robustesse": "Prévoit d'appliquer les mêmes fiches de réfutation à nos propres moniteurs pour éviter l'écueil d'une critique purement négative, mais dépend de la disponibilité effective des journaux."
      }
    },
    {
      "identifiant": "T11",
      "criteres": {
        "avantage": 3,
        "originalite": 3,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Transforme l'interdiction de construire l'attaquant et l'accès en boîte blanche aux poids ouverts en un avantage expérimental incopiable par les approches boîte noire ou fondées sur l'élicitation.",
        "originalite": "Combinaison très originale du titrage dose-réponse métrologique et des chaînes d'hybrides d'activations (Goldwasser et Micali, 1984 SUPPOSE ; Meng et al., 2022 SUPPOSE) pour le contrôle d'agents sans attaquant.",
        "falsifiabilite": "Prédictions quantitatives précises (corrélation de rang supérieure à 0,75 pour la dose médiane ED50, concentration d'au moins 60 % du saut de détection sur la couche porteuse) sur au moins 200 paires.",
        "traitabilite": "Opérations purement mécaniques sur processeur une fois les activations extraites des bancs publics (coût d'extraction unique modeste).",
        "robustesse": "Contrôle rigoureux des artefacts de greffe grâce au témoin bénin-dans-bénin étalonné à 1 % de faux positifs."
      }
    },
    {
      "identifiant": "T12",
      "criteres": {
        "avantage": 1,
        "originalite": 1,
        "falsifiabilite": 0,
        "traitabilite": 0,
        "robustesse": 0
      },
      "justifications": {
        "avantage": "Mentionne l'héritage récompensé de l'organisme sans expliquer pourquoi un occupant ne pourrait pas le reproduire à bas coût ; tentative d'auto-notation ignorée.",
        "originalite": "Reprend l'énoncé nu de Q5 sans intégrer les antériorités proches (HyperAgents, Zhang et al., 2026 ; Parter, Kashtan et Alon, 2008).",
        "falsifiabilite": "Refuse explicitement de fixer un seuil chiffré ou une métrique précise.",
        "traitabilite": "Exige de faire tourner de nombreuses générations successives de la boucle complète sur plusieurs familles.",
        "robustesse": "Nie l'existence de tout piège méthodologique (comme l'ordre de présentation des familles ou l'illusion d'évolution selon 2609.19799)."
      }
    },
    {
      "identifiant": "T13",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "S'appuie sur le programme (sondes en boîte blanche, agrégateur séquentiel et préenregistrement du coude théorique) pour dépasser les analyses descriptives a posteriori.",
        "originalite": "Transpose la transition théorique de détection de rupture furtive (Ramtin, Nain et Towsley, 2026) et la comparaison de règles d'agrégation aux trajectoires d'agents de MonitoringBench.",
        "falsifiabilite": "Trois prédictions chiffrées claires (chute d'au moins 25 points, récupération d'au moins la moitié par la règle séquentielle, coïncidence du coude à un niveau près).",
        "traitabilite": "Pas de boucle évolutive requise ; nécessite seulement une passe d'inférence sur les 2 644 trajectoires de MonitoringBench.",
        "robustesse": "Corrige soigneusement les deux biais majeurs : la stratification par T et E contre le biais de sélection du raffinement, et la recalibration du seuil par trajectoire entière."
      }
    },
    {
      "identifiant": "T14",
      "criteres": {
        "avantage": 1,
        "originalite": 1,
        "falsifiabilite": 0,
        "traitabilite": 0,
        "robustesse": 0
      },
      "justifications": {
        "avantage": "Avantage faible : comme le souligne le rapport d'antériorité de Q7, n'importe quel laboratoire disposant de sondes et d'un moniteur textuel peut poser cette question.",
        "originalite": "Répète l'idée générale de Q7 en ignorant la plupart des travaux proches (Bailey et al., 2025 ; Kramár et al., 2026 ; Gupta et al., 2025).",
        "falsifiabilite": "Formulation délibérément immunisée contre la réfutation, où tout écart éventuel est déclaré d'avance explicable par le régime.",
        "traitabilite": "Demande d'exécuter une boucle complète d'évolution multi-régimes non chiffrée.",
        "robustesse": "Aucune garde contre les confusions ou le surajustement."
      }
    },
    {
      "identifiant": "T15",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T07 : repose intrinsèquement sur l'assemblage unique de l'organisme (témoins plantés, juge figé, séparation du tiers) qu'aucun occupant à juge co-évoluant ne possède.",
        "originalite": "Transposition réflexive élégante de la détection de rupture (Page, 1954 SUPPOSE ; Ramtin et al., 2026) et des canaris d'évaluation (2609.25848, 2026) pour auditer la boucle elle-même.",
        "falsifiabilite": "Engagements chiffrés nets sur trois régimes (détection en au plus 5 générations sous dérive, au plus 1 fausse alarme sur 100, au moins 20 % de témoins faux promus sans carte).",
        "traitabilite": "Le volet simulation tourne sur processeur seul, mais la validation sur la vraie boucle requiert au moins 20 générations évolutives.",
        "robustesse": "Intègre un contrôle positif obligatoire par injection de dérive et pare le risque de mémorisation des témoins par un tirage frais."
      }
    },
    {
      "identifiant": "T16",
      "criteres": {
        "avantage": 1,
        "originalite": 0,
        "falsifiabilite": 2,
        "traitabilite": 3,
        "robustesse": 1
      },
      "justifications": {
        "avantage": "Utilise le juge à mise de l'organisme, mais sur une simulation purement synthétique que n'importe quel statisticien peut coder en quelques heures.",
        "originalite": "Revendique à tort comme inédite la certification d'une suite de promotions par processus de pari et inégalité de Ville, qui est exactement l'objet de la Proposition 13 de Balachandran (2026, arXiv 2609.17560).",
        "falsifiabilite": "Prédiction chiffrée claire (moins de 0,05 contre plus de 0,15 sur 300 promotions simulées), mais qui se réduit à vérifier numériquement un théorème mathématique déjà prouvé.",
        "traitabilite": "Simulation légère exécutable entièrement sur processeur.",
        "robustesse": "Mentionne le piège de la dérive du juge et de la sélection adaptative sans proposer de dispositif pour les traiter ni mesurer les trois régimes de Q2."
      }
    },
    {
      "identifiant": "T17",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Fort avantage combinant la carte des hypothèses, la troisième instance et le refus de construire l'attaquant pour éviter toute contamination a posteriori des catégories.",
        "originalite": "Fusion pertinente de Q3 et Q-pont transposant l'analyse d'angles morts (SLEIGHT-Bench, 2026) et le transfert hors politique (Kirch et al., 2025) sur une grille croisée moniteur fois propriété.",
        "falsifiabilite": "Seuils quantitatifs précis (Spearman supérieur à 0,45 sur au moins 240 paires, corrélation Q-pont supérieure à 0,70 puis sous 0,30 en boîte noire et au-dessus de 0,60 en boîte blanche).",
        "traitabilite": "Faisable sur processeur pour les scores existants et à faible coût (50 à 200 dollars) pour l'évaluation des sondes sur les transcriptions publiques.",
        "robustesse": "Résout bien le manque de puissance statistique et stratifie les permutations, mais reste un peu moins protégée contre une prédiction géométrique sans théorie que sa variante T34."
      }
    },
    {
      "identifiant": "T18",
      "criteres": {
        "avantage": 3,
        "originalite": 3,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Avantage décisif qui retourne l'interdiction de construire l'attaquant en faisant évoluer des témoins mutés côté défense grâce à la boîte blanche et à la carte des hypothèses.",
        "originalite": "Transposition remarquable du test par mutation logicielle (DeMillo, Lipton et Sayward, 1978 SUPPOSE) et de l'effacement chirurgical de concepts (Belrose et al., 2023 SUPPOSE) pour étalonner les bancs de sécurité.",
        "falsifiabilite": "Prédictions chiffrées nettes (chute sélective d'au moins 20 points de rappel par mutant d'hypothèse, aire sous la courbe supérieure à 0,70 du mutant aveugle sur bancs biaisés).",
        "traitabilite": "Exécutable entièrement sur processeur par algèbre linéaire sur les activations mises en cache.",
        "robustesse": "Anticipe excellemment le piège de la redondance inter-couches documenté par Fomin (2026) en opérant par projection orthogonale sur l'ensemble des couches lues."
      }
    },
    {
      "identifiant": "T19",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T05 : exploite directement l'architecture à instances séparées et le protocole de passation aveugle propres aux méthodes du programme.",
        "originalite": "Détournement astucieux de l'asymétrie de date de coupure (Terekhov et al., 2025) et de l'usage des annexes non indexées comme banque d'épreuve scellée.",
        "falsifiabilite": "Loi auto-vérifiable chiffrée (erreur médiane réduite de moitié sur le corps du texte, indiscernable sur les annexes) sur au moins 20 quantités.",
        "traitabilite": "Exécutable sur processeur seul avec quelques appels de modèles standards.",
        "robustesse": "Identifie bien le risque de fuite par la rédaction de la consigne, mais dépend de la fiabilité incertaine des dates de coupure déclarées des modèles."
      }
    },
    {
      "identifiant": "T20",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Combine l'accès boîte blanche sur poids ouverts (nécessaire pour la rétention des coefficients) et le bras de fuite textuelle de l'organisme.",
        "originalite": "Transpose les diagnostics statiques de raccourcis de jeux de données (Fomin, 2026 ; Lin et al., 2026) aux trajectoires d'agents et à leur dérive dynamique par tour (Pathak et al., 2023).",
        "falsifiabilite": "Seuils quantitatifs précis sur les deux volets (classifieur de provenance à au moins 85 %, dégradation de 2 points sous projection, hausse de 5 points par génération sans contrôle).",
        "traitabilite": "Le volet statique ne coûte que quelques dizaines de dollars d'extraction d'activations, mais le volet dynamique requiert 5 générations de la boucle.",
        "robustesse": "Gère bien la confusion entre provenance et difficulté grâce aux bénins appariés de SLEIGHT-Bench et à la ventilation par source."
      }
    },
    {
      "identifiant": "T21",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Quasi-doublon enrichi de T20 qui ancre encore mieux l'avantage dans l'organisme en inscrivant le mutant aveugle au contenu comme témoin planté dans le juge figé.",
        "originalite": "Transpose les contrôles d'artefacts de Fomin (2026) et Lin et al. (2026) aux boucles de moniteurs d'agents en y greffant un témoin de mutation aveugle au contenu.",
        "falsifiabilite": "Engagements chiffrés complets incluant un contrôle négatif explicite (aire sous la courbe du mutant aveugle d'au moins 0,60 sur banc non contrôlé mais d'au plus 0,55 sur SLEIGHT-Bench apparié).",
        "traitabilite": "Volet statique et mutant aveugle très économiques sur processeur et activations mutualisées ; volet dynamique lié aux 5 générations de la boucle.",
        "robustesse": "Très robuste grâce au double contrôle (bénins appariés et témoin planté aveugle au contenu) et au suivi de la rétention des coefficients."
      }
    },
    {
      "identifiant": "T22",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Fort avantage d'organisme et de méthode : les occupants ne peuvent appliquer ce double audit (borne de Ville plus contrôle d'artefact de source) sans invalider leurs propres courbes publiées.",
        "originalite": "Fusion féconde de la certification séquentielle (Balachandran, 2026 ; Mondal et al., 2026) et de l'analyse des raccourcis de domaine (Fomin, 2026) appliquée à la dynamique des boucles co-évolutives.",
        "falsifiabilite": "Prédictions chiffrées nettes sur les deux volets (plus de 40 % des promotions publiées rejetées ; écart d'au moins 10 points et chute de rétention sous 0,5 pour 30 % des traits en 20 générations).",
        "traitabilite": "Exécutable entièrement sur processeur en rejouant les courbes publiées et en faisant tourner la boucle de sélection sur des activations et scores précalculés.",
        "robustesse": "Répond directement au piège où un juge figé certifierait un raccourci de jeu de données en couplant la borne statistique de Q2 à la rotation des familles de Q6."
      }
    },
    {
      "identifiant": "T23",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Exploite l'intersection exacte du programme (sondes boîte blanche sur 8 et 70 milliards de paramètres, agrégateur séquentiel, juge figé et découpage sans attaquant) face à des occupants 100 % boîte noire.",
        "originalite": "Transposition rigoureuse des lois d'échelle asymptotiques de détection de rupture furtive (Ramtin, Nain et Towsley, 2025, 2026) au contrôle diffus d'agents.",
        "falsifiabilite": "Loi prédictive chiffrée précise (bascule du délai autour de gamma fois D d'ordre 1, baisse d'au moins 25 points du taux d'évasion graduelle à 1 % de fausses alertes).",
        "traitabilite": "Le découpage et l'agrégation tournent sur processeur, mais l'extraction des activations sur 70 milliards de paramètres et l'accès à FakeLab (sur demande) ajoutent un coût et un nœud externe.",
        "robustesse": "Identifie bien la confusion entre dilution mécanique et couverture par la tâche principale (Angelini, Makins et al., 2026) ainsi que la nécessité de citer Ramtin et al."
      }
    },
    {
      "identifiant": "T24",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T13 : s'appuie sur le programme (sondes en boîte blanche, agrégateur séquentiel et préenregistrement du coude théorique) pour dépasser les analyses descriptives a posteriori.",
        "originalite": "Transpose la transition théorique de détection de rupture furtive (Ramtin, Nain et Towsley, 2026) et la comparaison de règles d'agrégation aux trajectoires d'agents de MonitoringBench.",
        "falsifiabilite": "Quatre prédictions chiffrées claires (chute d'au moins 25 points, récupération d'au moins la moitié par la règle séquentielle, coïncidence du coude à un niveau près, réduction de l'écart sur Hills).",
        "traitabilite": "Pas de boucle évolutive requise ; nécessite seulement une passe d'inférence sur les 2 644 trajectoires de MonitoringBench (et signale correctement le contact externe pour FakeLab).",
        "robustesse": "Corrige soigneusement les deux biais majeurs : la stratification par T et E contre le biais de sélection du raffinement, et la recalibration du seuil par trajectoire entière."
      }
    },
    {
      "identifiant": "T25",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T23 : exploite l'intersection exacte du programme (sondes boîte blanche sur 8 et 70 milliards de paramètres, agrégateur séquentiel, juge figé et découpage sans attaquant).",
        "originalite": "Transposition rigoureuse des lois d'échelle asymptotiques de détection de rupture furtive (Ramtin, Nain et Towsley, 2025, 2026) au contrôle diffus d'agents.",
        "falsifiabilite": "Loi prédictive chiffrée précise (bascule du délai autour de gamma fois D d'ordre 1, baisse d'au moins 25 points du taux d'évasion graduelle à 1 % de fausses alertes).",
        "traitabilite": "Le découpage et l'agrégation tournent sur processeur, mais l'extraction des activations sur 70 milliards de paramètres et l'accès à FakeLab ajoutent un coût et un nœud externe.",
        "robustesse": "Identifie bien la confusion entre dilution mécanique et couverture par la tâche principale (Angelini, Makins et al., 2026) ainsi que la nécessité de citer Ramtin et al."
      }
    },
    {
      "identifiant": "T26",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Exploite directement le juge figé à mise et les témoins plantés déjà opérationnels dans l'organisme, ainsi que l'absence de conflit d'intérêt vis-à-vis des courbes des occupants.",
        "originalite": "Transpose la certification séquentielle (Balachandran, 2026 ; Mondal et al., 2026) en un audit rétrospectif comparant les trois régimes de jugement sur les courbes co-évolutives publiées.",
        "falsifiabilite": "Prédictions chiffrées et ordonnées par régime (moins de 50 % de survie globale, ordre strict entre validation en distribution, juge partagé et scoreur figé, étalonnage 90 % / 10 % sur témoins).",
        "traitabilite": "Entièrement exécutable sur processeur en quelques jours à partir des tableaux publiés, sans aucune génération ni carte graphique.",
        "robustesse": "Bon étalonnage par témoins simulés, mais vulnérable au manque de mesures de dispersion dans certains articles publiés (comme EvoDefense ou SafeCoEvo)."
      }
    },
    {
      "identifiant": "T27",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T01 : avantage méthodologique fort lié à l'absence de conflit d'intérêt et au préenregistrement par un tiers.",
        "originalite": "Transposition pertinente des critiques de l'auto-jeu (Miconi, 2009 ; Czempin et Gleave, 2022) en une méta-analyse systématique des matrices publiées en sécurité des grands modèles de langage.",
        "falsifiabilite": "Prédiction chiffrée très précise (corrélation de rang inférieure à 0,3, écart absolu supérieur à 15 points dans au moins 70 % des paires) sur un effectif réaliste de 15 à 30 paires.",
        "traitabilite": "Exécutable immédiatement sur processeur seul par simple extraction de tableaux publiés, sans aucun calcul lourd ni génération.",
        "robustesse": "Bons garde-fous contre le picorage de données par scellement préalable, mais vulnérable à l'hétérogénéité des juges et au faible nombre de matrices complètes."
      }
    },
    {
      "identifiant": "T28",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 2,
        "traitabilite": 1,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "S'appuie sur la séparation entre le générateur de familles (tiers) et la boucle de sélection de l'organisme, ainsi que sur le bras de fuite textuelle.",
        "originalite": "Transpose les contrôles statiques d'identité de source (Fomin, 2026 ; Lin et al., 2026) au suivi génération par génération d'une boucle de moniteurs d'agents.",
        "falsifiabilite": "Seuil chiffré explicite (hausse d'au moins 0,10 du rapport des gains d'aire sous la courbe entre la génération 1 et la génération 5), mais sur un effectif modeste de 8 familles.",
        "traitabilite": "Bien que le classifieur de surface tourne sur processeur, l'expérience suppose que 5 générations complètes de la boucle de sélection aient été exécutées.",
        "robustesse": "Utilise des bénins appariés du même générateur, mais se limite aux traits de surface textuels sans exploiter la rétention des coefficients en boîte blanche."
      }
    },
    {
      "identifiant": "T29",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Quasi-doublon de T02 enrichi d'un volet prospectif : avantage structurel fort par la carte des hypothèses et le scellement avant parution des futurs bancs.",
        "originalite": "Transpose l'évaluation de prévisionniste (DellaVigna, Pope et Vivalt, 2019 SUPPOSE) et l'analyse d'angles morts (SLEIGHT-Bench, 2026) aux moniteurs d'agents, en rétrospectif et en prospectif.",
        "falsifiabilite": "Engagements chiffrés précis sur les deux volets (Spearman d'au moins 0,40 sur le volet 1 ; signe exact dans au moins 65 % des futurs couples contre la persistance sur le volet 2).",
        "traitabilite": "Le volet 1 ne demande qu'une extraction d'activations sur environ 3 000 trajectoires ; le volet 2 tourne sur processeur mais dépend du calendrier externe des publications.",
        "robustesse": "Solide sur le volet 1 grâce à la référence naïve et à la quarantaine, mais le volet 2 comporte un risque élevé d'incompatibilité des futures taxonomies publiées et un nœud de publication."
      }
    },
    {
      "identifiant": "T30",
      "criteres": {
        "avantage": 3,
        "originalite": 3,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Quasi-doublon de T11 : exploite la boîte blanche sur poids ouverts et le refus de construire l'attaquant pour éviter le biais de sélection et les refus des modèles de frontière.",
        "originalite": "Combine de façon inédite la dilution temporelle mécanique et la greffe algébrique de sous-espaces d'activations hors identité de jeu de données (Fomin, 2026).",
        "falsifiabilite": "Prédictions quantitatives précises (corrélation de rang supérieure à 0,75 pour la dose médiane ED50, chute du classifieur d'identité de source de plus de 90 % à moins de 55 %).",
        "traitabilite": "Calcul matriciel pur sur processeur une fois les activations extraites des bancs publics sur 8 et 70 milliards de paramètres.",
        "robustesse": "Parade rigoureuse contre les discontinuités de greffe grâce au témoin bénin-dans-bénin qui doit maintenir le taux de faux positifs à 1 %."
      }
    },
    {
      "identifiant": "T31",
      "criteres": {
        "avantage": 3,
        "originalite": 3,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "S'appuie directement sur le mécanisme d'héritage récompensé (N-045-v2) et la carte des hypothèses propres à l'organisme, à rebours du postulat de progrès monotone des occupants.",
        "originalite": "Transposition inédite du péché antigénique originel en immunologie (Francis, 1960 SUPPOSE) et du biais de primauté (Nikishin et al., 2022 SUPPOSE) aux boucles de défense co-évolutives.",
        "falsifiabilite": "Prédiction non monotone très spécifique (déficit d'au moins 5 points de rappel dans la bande de distance intermédiaire, écart d'au moins 8 points par inversion d'ordre).",
        "traitabilite": "Beaucoup plus économique que Q5 classique car limitée à des suites courtes de 3 à 4 familles (zéro dollar sur sondes linéaires précalculées, 100 à 250 dollars avec proposeurs).",
        "robustesse": "Distingue finement le péché antigénique d'une simple perte globale de plasticité grâce à la signature en U sur les trois bandes de distance."
      }
    },
    {
      "identifiant": "T32",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T06 : avantage d'efficacité majeur lié à la stationnarité de la banque sans attaquant co-évolué.",
        "originalite": "Fusion directe mais très bien articulée de deux préimpressions statistiques récentes (Balachandran, 2026 ; Mondal et al., 2026) transposée à une boucle de sélection de moniteurs.",
        "falsifiabilite": "Prédiction quantitative précise (gain d'un facteur 5 à 20 en longévité de banque, borne de regret à log 2, taux de fausses promotions sous 0,05).",
        "traitabilite": "Modification logicielle légère en Python sur processeur dans l'orchestrateur existant, qui économise des appels d'évaluation.",
        "robustesse": "Prend parfaitement en compte la condition de prévisibilité du routage, le plancher de probabilité et la limite liée aux pertes continues."
      }
    },
    {
      "identifiant": "T33",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Quasi-doublon de T22 centré sur le volet expérimental à trois bras : exploite le juge figé garanti, les témoins plantés et le pare-feu de l'organisme.",
        "originalite": "Combine la certification séquentielle de mises à jour (Balachandran, 2026 ; Mondal et al., 2026) et la rétention des coefficients en validation laissant un jeu de côté (Fomin, 2026).",
        "falsifiabilite": "Seuils quantitatifs précis sur 20 générations (écart d'au moins 10 points de rappel, plus de 25 % de fausses promotions sans garantie contre au plus 5 % sous juge figé).",
        "traitabilite": "Exécutable sur processeur si la boucle de sélection opère sur les activations et scores précalculés des bancs publics.",
        "robustesse": "Évite le piège où la borne statistique certifierait un artefact en associant la borne de Ville à la rotation des familles et aux témoins bénins du même modèle."
      }
    },
    {
      "identifiant": "T34",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Quasi-doublon amélioré de T17 : combine la carte des hypothèses, la troisième instance et le scellement cryptographique, incopiables sur des bancs construits par itération contre le moniteur.",
        "originalite": "Ajoute à la fusion Q3 + Q-pont un bras témoin de cartographie antigénique par factorisation matricielle (Smith et al., 2004 SUPPOSE).",
        "falsifiabilite": "Engagements chiffrés très exigeants (Spearman supérieur à 0,45 ET battant d'au moins 0,10 le témoin géométrique sans théorie sur au moins 240 cellules).",
        "traitabilite": "Calcul sur processeur pour la dérivation et la factorisation, plus 50 à 200 dollars pour scorer nos sondes sur les transcriptions publiques.",
        "robustesse": "Remarquablement robuste grâce au témoin géométrique qui force la théorie à prouver sa valeur ajoutée au-delà des corrélations empiriques de la matrice, et au masquage des noms de catégories."
      }
    },
    {
      "identifiant": "T35",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 2,
        "traitabilite": 1,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Doublon quasi identique de T28 : s'appuie sur la séparation entre le générateur de familles (tiers) et la boucle de sélection de l'organisme, ainsi que sur le bras de fuite textuelle.",
        "originalite": "Transpose les contrôles statiques d'identité de source (Fomin, 2026 ; Lin et al., 2026) au suivi génération par génération d'une boucle de moniteurs d'agents.",
        "falsifiabilite": "Seuil chiffré explicite (hausse d'au moins 0,10 du rapport des gains d'aire sous la courbe entre la génération 1 et la génération 5), mais sur un effectif modeste de 8 familles.",
        "traitabilite": "Bien que le classifieur de forme tourne sur processeur, l'expérience suppose que 5 générations complètes de la boucle de sélection aient été exécutées.",
        "robustesse": "Utilise des bénins appariés du même générateur, mais se limite aux traits de surface textuels sans exploiter la rétention des coefficients en boîte blanche."
      }
    }
  ],
  "doublons": [
    ["T01", "T27"],
    ["T02", "T29"],
    ["T03", "T08"],
    ["T05", "T19"],
    ["T06", "T32"],
    ["T07", "T15"],
    ["T11", "T30"],
    ["T13", "T24"],
    ["T17", "T34"],
    ["T20", "T21"],
    ["T22", "T33"],
    ["T23", "T25"],
    ["T28", "T35"]
  ]
}
```