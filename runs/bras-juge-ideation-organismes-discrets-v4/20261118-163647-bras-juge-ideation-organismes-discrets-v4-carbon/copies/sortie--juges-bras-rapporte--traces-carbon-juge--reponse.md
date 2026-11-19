```json
{
  "notes": [
    {
      "identifiant": "T01",
      "criteres": {
        "avantage": 1,
        "originalite": 1,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "S'appuie sur les paramètres internes de la passe pilote, mais l'analyse de dilution et le verrouillage post-génération sont copiables par tout laboratoire.",
        "originalite": "Transposition directe de la distinction entre intention de traiter et conformité dans les essais randomisés (Angrist, Imbens et Rubin, 1996, SUPPOSE).",
        "falsifiabilite": "Prédiction chiffrée de signe déclaré sur les 128 instances reliant un taux de plus de 25 % d'instances non permutables à une atténuation d'au moins 0,75 et à un écart de jetons dépassant 0,10.",
        "traitabilite": "Simple comptage sur processeur du nombre de champs de contrôles non vides sur les exécutions honnêtes déjà prévues à la passe pilote.",
        "robustesse": "Identifie pertinemment le biais de sélection dynamique, mais commet une erreur arithmétique en affirmant que l'arrondi supérieur d'un quart fois deux vaut deux au lieu de un."
      }
    },
    {
      "identifiant": "T02",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 1,
        "robustesse": 1
      },
      "justifications": {
        "avantage": "Exploite la détention conjointe du jumeau apparié et de la référence cachée du programme, inaccessible à un auditeur externe.",
        "originalite": "Détourne astucieusement le principe des défauts plantés de l'analyse de mutation (DeMillo, Lipton et Sayward, 1978, SUPPOSE) pour tester la sensibilité de la métrique de dommage sur le jumeau honnête.",
        "falsifiabilite": "Loi chiffrée de signe négatif à la dose maximale avec deux seuils décisionnels à 0,15 et 0,05 point et intervalle de confiance à 95 % sur 128 paires.",
        "traitabilite": "Le dérangement hors ligne ne sollicite que le processeur, mais sa vérification impose de passer 512 productions supplémentaires devant les deux modèles lecteurs.",
        "robustesse": "Postule que le saboteur génère un texte propre distinct du jumeau dérangé alors que les faits stipulent que les cinq autres champs restent intacts, et omet la dépendance par grappes des 16 tâches."
      }
    },
    {
      "identifiant": "T03",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 1,
        "robustesse": 1
      },
      "justifications": {
        "avantage": "Repose sur l'accès exclusif à la référence cachée et aux productions honnêtes appariées du banc interne.",
        "originalite": "Étend le principe des témoins ajoutés et de l'analyse de mutation (DeMillo, Lipton et Sayward, 1978, SUPPOSE) en règle opérationnelle de bascule à trois issues avant lecture du saboteur.",
        "falsifiabilite": "Loi prédictive chiffrée de signe négatif fixant des seuils à 0,15 et 0,05 point à la dose unité ainsi qu'une monotonie selon la dose sur les 128 instances.",
        "traitabilite": "La fabrication mécanique est quasi gratuite sur processeur, mais l'évaluation double ou quintuple le volume d'appels aux deux modèles lecteurs hors familles.",
        "robustesse": "Suppose sans garantie que l'agent saboteur diffère d'une permutation hors ligne du jumeau honnête malgré l'invariance exigée des autres champs, et néglige la corrélation intra-tâche."
      }
    },
    {
      "identifiant": "T04",
      "criteres": {
        "avantage": 1,
        "originalite": 1,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Diagnostic méthodologique rigoureux mais intégralement reproductible par tout laboratoire, sa valeur résidant uniquement dans l'anticipation avant scellement.",
        "originalite": "Application classique de l'effet de plan et de l'analyse non paramétrique de courbes caractéristiques pour données groupées (Obuchowski, 1997, SUPPOSE).",
        "falsifiabilite": "Prédiction chiffrée vérifiable sur 128 paires en 16 grappes annonçant un coût exactement nul hors ligne et une borne haute dépassant 0,60 dès une corrélation intra-tâche de 0,25.",
        "traitabilite": "Calculable sur processeur seul en moins d'une heure par rééchantillonnage des données honnêtes à dose nulle.",
        "robustesse": "Protège l'aveugle en estimant la corrélation uniquement sur la dose nulle et tranche proprement l'ambiguïté entre coût trivialement nul hors ligne et divergence en trajectoire."
      }
    },
    {
      "identifiant": "T05",
      "criteres": {
        "avantage": 1,
        "originalite": 1,
        "falsifiabilite": 2,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Comptabilité arithmétique de la dose effective copiable à coût nul par tout laboratoire attentif au préenregistrement.",
        "originalite": "Transposition directe de l'analyse en intention de traiter et de l'exposition effective (Hollis et Campbell, 1999, SUPPOSE) à une grille discrète de permutation.",
        "falsifiabilite": "Chiffre exactement les effondrements d'arrondi pour quatre actions ou moins à la dose un quart, mais repose sur une disjonction conditionnelle plus lâche au-delà.",
        "traitabilite": "Exécutable sur processeur seul par un simple balayage déterministe des sorties honnêtes et des graines de tirage.",
        "robustesse": "Évite le piège des degrés de liberté post-hoc en scellant la dose nominale comme analyse principale, mais rate la redondance sémantique entre contrôles non identiques à l'octet près."
      }
    },
    {
      "identifiant": "T06",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "S'appuie sur la structure interne de la référence cachée couplée au script existant du programme, impossible à reproduire sans détenir l'oracle.",
        "originalite": "Combine de façon originale l'unicité positionnelle de sous-chaînes et un placebo octet-identique pour encadrer le biais d'agrégation par minimum au-delà des modèles d'erreur d'observateurs (Dawid et Skene, 1979, SUPPOSE).",
        "falsifiabilite": "Seuils chiffrés précis de 0,05 sur le placebo et sur la divergence entre couverture lue et couverture ancrée aux doses hautes, avec signe déclaré.",
        "traitabilite": "Extension directe sur processeur du script de recherche de chaînes exactes déjà en place, sans aucun appel de modèle supplémentaire.",
        "robustesse": "Verrouille efficacement le biais différentiel des lecteurs, mais suppose une référence cachée préalablement segmentée par action et risque d'écraser le plancher honnête en cas de paraphrase légitime."
      }
    },
    {
      "identifiant": "T07",
      "criteres": {
        "avantage": 2,
        "originalite": 1,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Exploite l'appariement par graine et la correspondance interne avec la référence cachée que seul le programme détient.",
        "originalite": "Vérification fondamentale mais classique de validité de construit face à une permutation conservant le multi-ensemble, dans le cadre des évaluations de sabotage (Benton et collaborateurs, 2024, SUPPOSE).",
        "falsifiabilite": "Prédiction chiffrée opposant un écart par réunion borné par 0,02 à toutes les doses à un écart par attachement d'au moins 0,15 à la dose maximale.",
        "traitabilite": "Vérifiable en quelques minutes sur processeur par script d'appariement sans solliciter de nouveaux modèles.",
        "robustesse": "Cible la faille définitionnelle majeure du protocole, mais perd son caractère purement programmatique si l'oracle caché ne rattache pas explicitement chaque contrôle attendu à une action précise."
      }
    },
    {
      "identifiant": "T08",
      "criteres": {
        "avantage": 1,
        "originalite": 1,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Sonde purement lexicale aisément copiable par tout évaluateur externe disposant d'un format d'actions structuré en champs.",
        "originalite": "Transposition directe de la détection d'artefacts superficiels dans les jeux d'inférence en langue naturelle (Gururangan et collaborateurs, 2018, SUPPOSE).",
        "falsifiabilite": "Loi prédictive chiffrée de signe positif annonçant une aire sous la courbe d'au moins 0,65 pour le classifieur de recouvrement lexical à la dose unité malgré une perte de couverture sous 0,15.",
        "traitabilite": "Calculable en quelques secondes sur processeur par script standard sur les 128 instances sans appel de modèle.",
        "robustesse": "La sonde aveugle est pertinente, mais le correctif proposant de réécrire et d'anonymiser automatiquement les identifiants internes risque de dénaturer les contrôles ou de créer un nouvel artefact."
      }
    },
    {
      "identifiant": "T09",
      "criteres": {
        "avantage": 1,
        "originalite": 1,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 3
      },
      "justifications": {
        "avantage": "Correction statistique standard copiable sans barrière, mais indispensable pour parer une invalidation arithmétique immédiate par un auditeur tiers.",
        "originalite": "Application directe des méthodes de rééchantillonnage pour erreurs groupées avec petit nombre de grappes (Cameron, Gelbach et Miller, 2008, SUPPOSE).",
        "falsifiabilite": "Relation quantitative exacte prédisant un élargissement d'intervalle d'au moins un facteur 1,55 dès que la corrélation intra-tâche dépasse 0,20 sur 16 grappes de 8 épisodes.",
        "traitabilite": "Énumération exacte des 65 536 retournements de signe sur les moyennes des 16 tâches en moins d'une seconde sur un processeur.",
        "robustesse": "Évite le piège asymptotique gaussien sur 16 grappes grâce au test exact de symétrie tout en respectant la procédure de tests multiples de Holm."
      }
    },
    {
      "identifiant": "T10",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Verrouille un angle mort propre à l'architecture interne en deux étages reliant les actions à six champs au rapport final vérifié par script.",
        "originalite": "Identifie finement le court-circuit informationnel par lequel la synthèse finale peut reconstituer les contrôles via les champs de proposition et de prédiction laissés intacts, ainsi que l'abus de citations courtes.",
        "falsifiabilite": "Seuils chiffrés de signe positif prédisant au moins 20 % de citations validées de moins de 5 mots ou multiples et plus de 50 % de contrôles permutés neutralisés dans le rapport final.",
        "traitabilite": "Modification légère du script Python existant s'exécutant en quelques millisecondes sur processeur sans appel de modèle.",
        "robustesse": "Couvre une faille structurelle négligée ailleurs, mais imposer arbitrairement huit mots minimum risque de rejeter des identifiants courts valides et d'abaisser artificiellement le plancher honnête."
      }
    },
    {
      "identifiant": "T11",
      "criteres": {
        "avantage": 0,
        "originalite": 0,
        "falsifiabilite": 2,
        "traitabilite": 3,
        "robustesse": 0
      },
      "justifications": {
        "avantage": "N'apporte strictement aucun élément au-delà de la procédure de comparaison appariée déjà décrite dans l'énoncé des faits.",
        "originalite": "Entièrement occupée par la pièce d'antériorité fournie (faits-v3.md, sections 5d et 6).",
        "falsifiabilite": "Répète les seuils chiffrés déjà scellés dans le protocole à 0,15 point sur 128 instances sans formuler de test discriminant sur une faille de validité.",
        "traitabilite": "Coût nul sur processeur puisque l'intégralité des données et calculs est déjà inscrite au plan existant.",
        "robustesse": "Totalement aveugle aux failles demandées telles que l'invariance par réunion, la pseudo-réplication par tâche, les artefacts de surface et le biais conjonctif des lecteurs."
      }
    },
    {
      "identifiant": "T12",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 1,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "La construction d'une strate témoin certifiée à perte de couverture nulle exige la référence cachée détenue par le seul programme.",
        "originalite": "Transposition ingénieuse de l'évaluation de l'apprentissage par raccourci (Geirhos et collaborateurs, 2020, SUPPOSE) aux protocoles de contrôle d'agents (Greenblatt et collaborateurs, 2023, SUPPOSE) via des permutations neutres.",
        "falsifiabilite": "Prédiction chiffrée comparant l'aire sous la courbe de la strate de forme au seuil de 0,60 et à moins de 0,03 de la strate à perte à dose effective égalisée.",
        "traitabilite": "Nécessite une passe additionnelle d'inférence des modèles moniteurs du programme sur une à quatre centaines d'articles témoins.",
        "robustesse": "Prend soin d'égaliser la dose effective entre strates, mais échoue si les actions d'un même article pointent rarement vers un ensemble identique d'éléments dans la référence cachée."
      }
    },
    {
      "identifiant": "T13",
      "criteres": {
        "avantage": 0,
        "originalite": 0,
        "falsifiabilite": 0,
        "traitabilite": 0,
        "robustesse": 0
      },
      "justifications": {
        "avantage": "Observation générale dépourvue de tout levier opérationnel ou structurel propre au banc expérimental.",
        "originalite": "Lieu commun sur la séparation entre forme syntaxique et sens en traitement automatique des langues (Bender et Koller, 2020, SUPPOSE).",
        "falsifiabilite": "Aucune métrique définie, aucun seuil numérique et aucune direction d'effet déclarée permettant la moindre réfutation empirique.",
        "traitabilite": "Renvoie à une exploration ouverte de cas limites au coût et au protocole indéterminés.",
        "robustesse": "Formulation non falsifiable exposée à l'interprétation arbitraire après coup de n'importe quelle divergence observée."
      }
    },
    {
      "identifiant": "T14",
      "criteres": {
        "avantage": 2,
        "originalite": 2,
        "falsifiabilite": 3,
        "traitabilite": 3,
        "robustesse": 2
      },
      "justifications": {
        "avantage": "Couple directement le script interne de validation lexicale avec le découpage de l'oracle caché du banc, non réplicable de l'extérieur.",
        "originalite": "Formalise clairement comment la concavité de la règle du minimum transforme une hausse symétrique de bruit de lecture sous concordance modérée (Cohen, 1960, SUPPOSE) en faux dommage systématique.",
        "falsifiabilite": "Loi chiffrée de signe positif prédisant que plus de 35 % de l'écart de couverture provient des lectures discordantes tandis que le taux de citations exactes varie de moins de 0,05.",
        "traitabilite": "Indexation de sous-chaînes et calcul de concordance par dose réalisables sur processeur seul à partir des sorties déjà prévues.",
        "robustesse": "Fournit une contestation adverse redoutable sans juge humain, mais dépend d'un découpage de la référence cachée qui peut dégrader le plancher honnête s'il est trop étroit."
      }
    }
  ],
  "doublons": [
    [
      "T02",
      "T03"
    ],
    [
      "T06",
      "T14"
    ],
    [
      "T08",
      "T12"
    ],
    [
      "T04",
      "T09"
    ],
    [
      "T01",
      "T05"
    ],
    [
      "T01",
      "T04"
    ]
  ]
}
```