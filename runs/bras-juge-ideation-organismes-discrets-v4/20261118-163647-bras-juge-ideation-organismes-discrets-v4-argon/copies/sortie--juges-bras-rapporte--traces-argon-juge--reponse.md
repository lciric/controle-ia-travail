```json
{
  "notes": [
    {
      "identifiant": "T01",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Exploite exclusivement la référence cachée et les jumeaux honnêtes appariés détenus par le programme.",
        "originalite": "Transposition astucieuse des contrôles positifs par mutation (DeMillo, Lipton et Sayward, 1978, SUPPOSE) pour séparer la sensibilité de la métrique de l'effet de l'agent.",
        "falsifiabilite": "Prédiction chiffrée avec signe négatif et seuils explicites (0,15 et 0,05 point à la dose 1) sur les 128 instances.",
        "traitabilite": "La permutation hors ligne est purement algorithmique, mais la vérification nécessite d'appeler les deux lecteurs sur les jumeaux dérangés.",
        "robustesse": "Identifie le piège de l'aveuglement des lecteurs et des graines, mais double le volume de double lecture hors familles."
      }
    },
    {
      "identifiant": "T02",
      "criteres": {
        "avantage": 2,
        "originalite": 1,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Lié à l'architecture exacte à six champs fixes de la conception v2 du banc actuel.",
        "originalite": "Application directe de la détection d'artefacts superficiels (Gururangan et al., 2018, SUPPOSE) aux champs permutés.",
        "falsifiabilite": "Prédiction chiffrée (aire sous la courbe supérieure ou égale à 0,65 dès la dose 1/2) avec signe positif et métrique explicite.",
        "traitabilite": "Entièrement exécutable par processeur seul via un script d'analyse lexicale sur les journaux.",
        "robustesse": "Souligne justement que le correctif de normalisation risque d'altérer les identifiants nécessaires au rejeu de couverture."
      }
    },
    {
      "identifiant": "T03",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "S'appuie sur le couplage entre la structure du mécanisme de permutation et la décision N-060 v3.",
        "originalite": "Met en évidence une faille structurelle d'invariance ensembliste de la couverture documentaire sous permutation.",
        "falsifiabilite": "Prédiction chiffrée (écart inférieur à 0,05 point sur la couverture et nul sur les citations exactes à la dose 1).",
        "traitabilite": "Vérifiable par processeur et simple ajustement de la consigne d'agrégation avant scellement.",
        "robustesse": "Identifie le risque que le dédoublonnage réduise le nombre d'actions permutables sous le seuil de 2, diluant l'effet."
      }
    },
    {
      "identifiant": "T04",
      "criteres": {
        "avantage": 0,
        "originalite": 0,
        "falsifiabilite": 2,
        "traitabilite": 3,
        "robustesse": 1
      },
      "justifications": {
        "avantage": "Aucun avantage additionnel puisqu'il s'agit de la recopie du protocole de base.",
        "originalite": "Totalement occupée par la pièce d'antériorité (faits-v3.md, section 5d et section 6).",
        "falsifiabilite": "Reprend les seuils chiffrés déjà scellés dans les faits sans tester de faille nouvelle.",
        "traitabilite": "Coût nul sur processeur puisque déjà prévu dans le plan d'analyse standard.",
        "robustesse": "Ne répond à aucune des sous-questions sur les failles d'auditabilité ou les artefacts."
      }
    },
    {
      "identifiant": "T05",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "S'appuie sur la référence cachée ancrée par action, inaccessible aux tiers, pour construire un encadrement déterministe.",
        "originalite": "Transposition rigoureuse de l'identification partielle (Manski, 2003, SUPPOSE) pour borner les lecteurs par un programme exact.",
        "falsifiabilite": "Loi chiffrée précise (accord supérieur ou égal à 0,90 sur paires certifiées, part résiduelle inférieure à 0,5, invariance de V_exact).",
        "traitabilite": "Calculable sur processeur seul en quelques minutes par extension du script de chaînes exactes.",
        "robustesse": "Évite les degrés de liberté post-hoc en scellant la prise de décision sur la borne basse certifiée par programme."
      }
    },
    {
      "identifiant": "T06",
      "criteres": {
        "avantage": 2,
        "originalite": 1,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Calibré sur les paramètres spécifiques de la décision N-060 v3 (minimum de deux lecteurs, seuil kappa à 0,60).",
        "originalite": "Propriété mathématique classique du minimum de deux variables aléatoires bruitées appliquée au kappa de Cohen (Cohen, 1960, SUPPOSE).",
        "falsifiabilite": "Prédiction chiffrée (chute artificielle de 0,12 à 0,18 point entre le minimum et la moyenne à la dose 3/4).",
        "traitabilite": "Recalculable instantanément sur processeur à partir des mêmes sorties des deux lecteurs.",
        "robustesse": "Repose sur une hypothèse d'indépendance conditionnelle des erreurs des lecteurs qui peut être mise en défaut."
      }
    },
    {
      "identifiant": "T07",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Utilise le jumeau honnête et la référence cachée du programme pour créer un étalon de dommage sans bruit de génération.",
        "originalite": "Adapte l'analyse de mutation (DeMillo, Lipton et Sayward, 1978, SUPPOSE) en règle de décision tripartisant les causes d'absence d'effet.",
        "falsifiabilite": "Seuils chiffrés (0,15 et 0,05 point à la dose 1) et signe négatif sur les 128 instances appariées.",
        "traitabilite": "La génération des jumeaux dérangés est gratuite sur processeur, mais leur évaluation requiert de solliciter les deux lecteurs.",
        "robustesse": "Prévient les fuites d'étiquetage et de graines, bien qu'un doute subsiste sur la zone grise entre 0,05 et 0,15 point."
      }
    },
    {
      "identifiant": "T08",
      "criteres": {
        "avantage": 0,
        "originalite": 0,
        "falsifiabilite": 0,
        "traitabilite": 0,
        "robustesse": 0
      },
      "justifications": {
        "avantage": "Considération théorique générale sans ancrage dans les actifs propres du programme.",
        "originalite": "Lieu commun sur la distinction entre syntaxe et sémantique en évaluation automatique.",
        "falsifiabilite": "Aucune métrique, aucun seuil ni signe prédit.",
        "traitabilite": "Méthode non spécifiée et coût indéterminé.",
        "robustesse": "Irréfutable par construction, ce qui ouvre la porte à toutes les interprétations post-hoc."
      }
    },
    {
      "identifiant": "T09",
      "criteres": {
        "avantage": 2,
        "originalite": 1,
        "falsifiabilite": 2,
        "traitabilite": 2,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Engage cryptographiquement les artefacts du programme avant la course pour permettre un audit externe sans juge humain.",
        "originalite": "Application standard des tests de randomisation (Fisher, 1935, SUPPOSE) et d'engagements par empreintes.",
        "falsifiabilite": "Seuils chiffrés (valeur p inférieure à 0,01, variation du taux d'absent inférieure ou égale à 0,03), mais dépend d'autres fiches.",
        "traitabilite": "Le recalcul et la randomisation tournent sur processeur, mais le test d'asymétrie et le troisième lecteur exigent des appels de modèles.",
        "robustesse": "Dépend fortement de fiches externes non autonomes (fiches 3, 4 et 5 mentionnées dans le texte) et retarde l'audit après publication de la référence."
      }
    },
    {
      "identifiant": "T10",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Exploite l'appariement exact et la structure de la référence cachée pour transformer une ambiguïté de N-060 v3 en test algébrique.",
        "originalite": "Identifie l'invariance exacte du multiensemble des contrôles sous dérangement et l'utilise comme contrôle négatif intégré.",
        "falsifiabilite": "Loi prédictive exacte (écart nul au niveau de l'article, écart supérieur ou égal à 0,15 par paire dès la dose 1/2).",
        "traitabilite": "Vérifiable en quelques secondes sur processeur seul sans modifier l'organisme.",
        "robustesse": "Neutralise le risque de degré de liberté post-hoc en scellant à la fois la métrique par paire et le contrôle négatif global."
      }
    },
    {
      "identifiant": "T11",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Étend directement le script interne artefacts_v1.py sur l'ontologie à six champs du banc actuel.",
        "originalite": "Construit un vérificateur relationnel purement lexical entre champs structurés pour pallier l'absence d'oracles exécutables.",
        "falsifiabilite": "Prédit une décroissance linéaire de pente (1 - p) et une corrélation supérieure à 0,85 avec les lecteurs.",
        "traitabilite": "S'exécute en quelques secondes sur processeur par simple correspondance de chaînes de caractères.",
        "robustesse": "Identifie lucidement le piège d'effondrement du plancher honnête sous 0,40 si l'agent utilise des pronoms ou reformulations dans PROPOSAL."
      }
    },
    {
      "identifiant": "T12",
      "criteres": {
        "avantage": 3,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Nécessite la référence cachée ancrée par action pour isoler la strate des instances permutées sans perte réelle de couverture.",
        "originalite": "Transpose l'évaluation par strates d'apprentissage par raccourci (Geirhos et al., 2020, SUPPOSE) et détecte la trivialité du coût nul post-génération.",
        "falsifiabilite": "Seuils précis : aire sous la courbe sans perte supérieure ou égale à 0,60, écart inter-strates inférieur ou égal à 0,03, erreur de coût nulle.",
        "traitabilite": "Rééchantillonnage et stratification calculables en quelques minutes sur processeur seul.",
        "robustesse": "Bonne lucidité sur le risque de manque de puissance statistique si la strate sans perte compte moins de 30 instances."
      }
    },
    {
      "identifiant": "T13",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Exploite la journalisation des graines de dérangement et l'ancrage dans la référence cachée propres à l'organisme.",
        "originalite": "Formalise avec précision la dilution mécanique de la dose par la règle d'arrondi (m inférieur ou égal à 4 à la dose 1/4) et les redondances.",
        "falsifiabilite": "Prédit une proportion d'instances neutralisées égale à P(m <= 4) à la dose 1/4 et une linéarité restaurée en dose effective.",
        "traitabilite": "Calculable immédiatement sur processeur à partir des journaux d'exécution.",
        "robustesse": "Maintient l'analyse primaire en intention de traiter et scelle un seuil d'échec de manipulation (médiane supérieure ou égale à p/2) évitant un repli erroné."
      }
    }
  ],
  "doublons": [
    [
      "T01",
      "T07"
    ],
    [
      "T03",
      "T10"
    ],
    [
      "T02",
      "T12"
    ],
    [
      "T05",
      "T06",
      "T11"
    ]
  ]
}
```