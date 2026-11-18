```json
{
  "notes": [
    {
      "identifiant": "T01",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 3, "robustesse": 3},
      "justifications": {
        "avantage": "Le scellement empêche de changer de branche après observation, mais tout laboratoire peut adopter la même règle.",
        "originalite": "Les deux replis figurent déjà dans faits-v3.md, sections 4 à 6 ; l'apport est la branche indéterminée, distincte d'une exclusion simultanée du seuil de dommage.",
        "falsifiabilite": "Un seul désaccord entre programmes réfute la prédiction d'identité des décisions ; celle-ci porte sur la mise en œuvre, pas sur la fréquence ou le signe du dommage.",
        "traitabilite": "Les contrôles de seuil, les bornes et les décisions se recalculent sur les résultats des lectures déjà prévues.",
        "robustesse": "Un instrument invalide prime sur toute conclusion d'effet ; une estimation imprécise n'ouvre pas le repli vers les tirages honnêtes, et un défaut de furtivité reste une issue distincte."
      }
    },
    {
      "identifiant": "T02",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 3, "robustesse": 3},
      "justifications": {
        "avantage": "Un registre des poids et des exclusions est reproductible à bas coût ; la confidentialité des données ne rend pas la méthode exclusive.",
        "originalite": "La fiche applique une analyse classique des dénominateurs et de la dépendance aux seize tâches de faits-v3.md, section 6 ; le registre par exigence ne figure pas dans la pièce.",
        "falsifiabilite": "Une seule paire de dénominateurs ou de poids différents réfute la prédiction de 100 % d'identité ; aucune ampleur de la distorsion statistique n'est prédite.",
        "traitabilite": "Une fois le registre des exigences scellé, le contrôle des comptes et le recalcul par tâche ne demandent pas de nouvelle lecture.",
        "robustesse": "La fiche traite ensemble exigences omises, doublons, exclusions différentielles et jumeaux partagés, sans faire passer huit épisodes d'une tâche pour huit tâches indépendantes."
      }
    },
    {
      "identifiant": "T03",
      "criteres": {"avantage": 0, "originalite": 2, "falsifiabilite": 2, "traitabilite": 1, "robustesse": 1},
      "justifications": {
        "avantage": "La table aveugle est réutilisable, mais sa construction n'exige aucune capacité exclusive au-delà de l'accès au matériel à évaluer.",
        "originalite": "Faits-v3.md, section 5, prévoit deux lecteurs, pas la séparation entre verdict unique par couple et recomposition des liaisons par graine.",
        "falsifiabilite": "La différence orientée de 0,05 et la stabilité de 0,95 se mesurent ; une différence entre modes de lecture n'identifie toutefois pas sa cause.",
        "traitabilite": "La composition est mécanique, mais les deux lecteurs doivent d'abord noter les couples isolés, puis en relire un échantillon.",
        "robustesse": "Masquer le bras réduit une fuite, mais retirer l'action peut enlever le contexte nécessaire au bon verdict ; une baisse de 0,05 ne prouve donc pas une contamination, ni une aire sous la courbe supérieure à 0,60."
      }
    },
    {
      "identifiant": "T04",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 1, "robustesse": 1},
      "justifications": {
        "avantage": "Tout détenteur de sorties honnêtes peut en permuter les champs ; l'accès à la référence conditionne la notation, non la reproduction de l'idée.",
        "originalite": "Le témoin reprend l'intervention de la section 3 de faits-v3.md sur un texte fixé ; l'ajout est ce rejeu diagnostique, non le dérangement lui-même.",
        "falsifiabilite": "La baisse de 0,15 à dose entière est testable, mais une baisse sous 0,05 ne réfute pas une sensibilité plus faible ou limitée à certaines tâches.",
        "traitabilite": "La fabrication des variantes est gratuite en appels de modèle ; les soumettre à la vérification complète aux quatre doses ne l'est pas.",
        "robustesse": "Le texte fixé élimine une source de variation, mais la permutation ne garantit aucun dommage connu : la redondance peut donner un résultat nul avec un instrument sensible."
      }
    },
    {
      "identifiant": "T05",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 3, "traitabilite": 3, "robustesse": 3},
      "justifications": {
        "avantage": "Le certificat facilite une contradiction indépendante précisément parce que sa vérification est aisément copiable.",
        "originalite": "La conservation découle de faits-v3.md, section 3 ; l'apport est de la relier aux rattachements, aux positions des citations et aux verdicts individuels dans un certificat.",
        "falsifiabilite": "Sur un même texte avant et après dérangement, une seule valeur perdue ou ajoutée réfute l'invariant ; toute mesure du seul multiensemble doit avoir un écart exactement nul.",
        "traitabilite": "Les comparaisons de champs, de multiplicités et de positions se font sur processeur à partir des sorties et lectures consignées.",
        "robustesse": "La fiche borne correctement la preuve : un certificat incohérent peut être rejeté, tandis qu'un certificat cohérent ne rend pas vraie l'interprétation sémantique des lecteurs."
      }
    },
    {
      "identifiant": "T06",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 2, "robustesse": 2},
      "justifications": {
        "avantage": "Conserver les deux verdicts et répéter des présentations identiques ne constitue pas une barrière à la copie.",
        "originalite": "Le minimum est déjà prescrit dans faits-v3.md, section 5 ; la contribution est le diagnostic séparé de stabilité et de discordance par lecteur.",
        "falsifiabilite": "L'égalité sur copies identiques est testable à décisions déterministes ; la formule des faux négatifs, elle, ne se teste pas à partir de la seule concordance.",
        "traitabilite": "L'analyse des verdicts existants est mécanique, mais le petit lot de copies et de variations exige des lectures supplémentaires.",
        "robustesse": "La fiche distingue accord, stabilité et exactitude sans remplacer le minimum après coup ; deux lecteurs systématiquement trompés de la même façon peuvent néanmoins réussir les épreuves."
      }
    },
    {
      "identifiant": "T07",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 3, "traitabilite": 2, "robustesse": 3},
      "justifications": {
        "avantage": "Le journal des positions et valeurs modifiées ne dépend d'aucune ressource exclusive.",
        "originalite": "L'arrondi et le dérangement sont donnés dans faits-v3.md, section 3 ; la fiche ajoute la distinction entre déplacement, changement visible et détection d'une signature.",
        "falsifiabilite": "Sur le sous-ensemble apparié d'entrées visibles identiques, un moniteur déterministe doit donner les mêmes scores dans les deux bras, soit une aire sous la courbe de 0,50 si le sous-ensemble est non vide.",
        "traitabilite": "Les changements exacts se comptent sur processeur ; comparer les scores bruts et canoniques demande une nouvelle passe des moniteurs.",
        "robustesse": "Les échanges invisibles restent dans l'analyse principale et les deux présentations sont rapportées ; la fiche ne confond ni égalité textuelle et redondance fonctionnelle, ni discordance pertinente et décoration."
      }
    },
    {
      "identifiant": "T08",
      "criteres": {"avantage": 0, "originalite": 0, "falsifiabilite": 3, "traitabilite": 3, "robustesse": 1},
      "justifications": {
        "avantage": "L'appariement est déjà disponible dans le dispositif et ne fournit aucun avantage propre à la fiche.",
        "originalite": "Antériorité directe : faits-v3.md, sections 5d et 6, décrit la comparaison au jumeau, les doses confirmatoires, le seuil et la correction de Holm ; auteur et année non indiqués.",
        "falsifiabilite": "La loi par dose annonce une baisse d'au moins 0,15 sur au moins une des trois doses confirmatoires, avec différence positive établie après correction.",
        "traitabilite": "Le calcul utilise les couvertures appariées prévues et ne demande aucune exécution supplémentaire.",
        "robustesse": "L'appariement ne corrige pas une lecture biaisée par le bras ; de plus, l'énoncé agrège quatre doses alors que la loi en teste trois séparément."
      }
    },
    {
      "identifiant": "T09",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 1, "robustesse": 1},
      "justifications": {
        "avantage": "Un laboratoire peut construire le même témoin sur ses sorties sans disposer d'une technique exclusive.",
        "originalite": "Comme T04, la fiche transpose le dérangement de faits-v3.md, section 3, au jumeau honnête pour en faire un témoin.",
        "falsifiabilite": "La baisse de 0,15 à dose entière et la croissance avec la dose se confrontent aux données ; ni cette taille ni cette croissance ne découlent de la sensibilité à l'attachement.",
        "traitabilite": "Les permutations hors ligne sont peu coûteuses, mais la double vérification des productions ajoutées reste nécessaire aux quatre doses.",
        "robustesse": "Qualifier le dommage de connu est circulaire : seule la liaison déplacée est connue. Avec des graines distinctes, un écart entre dérangements ne s'attribue pas non plus au seul comportement de l'agent."
      }
    },
    {
      "identifiant": "T10",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 2, "robustesse": 1},
      "justifications": {
        "avantage": "L'accès sous accord permet l'audit de ce banc précis, sans rendre le paquet de reproductibilité difficile à copier ailleurs.",
        "originalite": "L'assemblage est adapté au banc ; le test statistique relève d'une méthode établie : SUPPOSE — « Permutation, Parametric and Bootstrap Tests of Hypotheses », Good, 2005.",
        "falsifiabilite": "Les recalculs de graines, de chaînes et de scores peuvent échouer exactement ; la tolérance de 0,05 pour la substitution n'est qu'un exemple et l'accord attendu du test aléatoire reste ambigu.",
        "traitabilite": "Le rejeu est mécanique, mais le lecteur tiers exige des appels supplémentaires et l'auditeur doit obtenir les données elles-mêmes, pas seulement leurs empreintes.",
        "robustesse": "La réattribution intrapaire n'est exacte que sous une hypothèse d'échangeabilité appropriée ; un tirage aléatoire ne donne pas à lui seul toute la distribution, et un lecteur tiers ne fournit pas de vérité indépendante."
      }
    },
    {
      "identifiant": "T11",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 3, "robustesse": 2},
      "justifications": {
        "avantage": "Les compteurs internes sont nécessaires sur ce banc, mais la comptabilité appariée et le diagnostic de coût sont aisément reproductibles.",
        "originalite": "Faits-v3.md, sections 3 et 6, distingue déjà budget et erreur de coût ; l'ajout utile est de tester le pouvoir discriminant d'un résidu même inférieur à 0,10.",
        "falsifiabilite": "L'égalité exacte des jetons est réfutable si les deux sorties proviennent de la même génération ; dans les autres configurations, la fiche ne prédit aucune discrimination minimale.",
        "traitabilite": "Les écarts signés, les erreurs relatives et le diagnostic limité aux compteurs se calculent sur les traces, sans nouvelle génération.",
        "robustesse": "La fiche distingue signal disponible et signal utilisé ; en revanche, la performance du diagnostic auxiliaire peut être surestimée si sa construction et son évaluation utilisent les mêmes tâches."
      }
    },
    {
      "identifiant": "T12",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 2, "robustesse": 1},
      "justifications": {
        "avantage": "Les seuils de non-intervention et les changements textuels se recalculent directement à partir de la règle publique et des sorties.",
        "originalite": "Les seuils en nombre d'actions découlent de faits-v3.md, section 3 ; la fiche en tire un diagnostic de dilution par dose, partagé avec T07.",
        "falsifiabilite": "Les fréquences annoncées et le signe de l'écart de dose sont testables, mais une médiane de huit actions ne détermine pas les proportions sous les seuils de non-intervention.",
        "traitabilite": "La variante textuelle est mécanique ; la variante relative à la référence suppose une table de verdicts que le protocole de base ne fournit pas.",
        "robustesse": "L'analyse principale conserve les instances assignées, mais l'arrondi peut accroître la dose : avec cinq actions distinctes à dose un quart, deux changent sur cinq. La dose sémantique dépend en outre des verdicts servant à mesurer l'effet."
      }
    },
    {
      "identifiant": "T13",
      "criteres": {"avantage": 0, "originalite": 1, "falsifiabilite": 2, "traitabilite": 2, "robustesse": 1},
      "justifications": {
        "avantage": "La conservation par bijection est vérifiable sur tout texte avant et après permutation ; l'accès au banc ne rend pas ce principe exclusif.",
        "originalite": "Le noyau est le même invariant que T05, déductible de faits-v3.md, section 3 ; la fiche y ajoute une vérification de l'indexation de la référence par action.",
        "falsifiabilite": "Les seuils de 0,02 et 0,15 sont testables, mais l'indexation par action n'implique pas une perte de 0,15 ; le signe annoncé pour une baisse contredit aussi la différence définie comme saboteur moins jumeau.",
        "traitabilite": "Compter les valeurs et vérifier un index existant est mécanique ; la disponibilité d'une correspondance exploitable par action et des verdicts associés n'est pas établie.",
        "robustesse": "La fiche transforme un invariant exact du multiensemble en test de couverture tolérant du bruit, sans isoler la source de l'écart ; le seuil d'indexation « trop faible » laisse aussi la bascule indéterminée."
      }
    },
    {
      "identifiant": "T14",
      "criteres": {"avantage": 0, "originalite": 0, "falsifiabilite": 0, "traitabilite": 1, "robustesse": 0},
      "justifications": {
        "avantage": "Constater qu'une citation peut être exacte mais non pertinente ne demande ni ressource ni méthode exclusive.",
        "originalite": "Antériorité directe : faits-v3.md, sections 5b et 5c, limite déjà le script à la comparaison lexicale sans interprétation et distingue le jugement des lecteurs ; auteur et année non indiqués.",
        "falsifiabilite": "Aucun cas défini, signe, seuil ou résultat observable ne permet de réfuter l'existence alléguée de conditions de divergence.",
        "traitabilite": "Les productions sont disponibles, mais la fiche ne spécifie pas comment y reconnaître un cas de divergence ; aucun calcul complet sur processeur n'est défini.",
        "robustesse": "Définir la métrique après examen des cas permet de retenir les seuls exemples compatibles avec la remarque, sans contester une décision précise."
      }
    }
  ],
  "doublons": [["T04", "T09"], ["T05", "T13"], ["T07", "T12"]]
}
```