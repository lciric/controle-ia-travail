# Demande approfondie — papier D : préenregistrement et devis de l'expérience sur modèle ouvert ; vérification sur PDF des références (v1)

- Pour Lazar et la fille 1 du papier D. Écrit par Fable 5.2, le 24 novembre 2026, à partir des pièces listées par la fille 1. Rien n'a été exécuté ni modifié dans le dépôt.
- Limites : les noms de bancs et d'articles viennent de ma mémoire, tous « à vérifier » sur PDF. Je n'ai lu ni la v4 du manuscrit ni les correctifs des sections théoriques.

## 1. Les quatre points

### Volet (a) — expérience sur modèle ouvert

**1. Ce qu'un expert ferait et que tu ne demandes pas**

- **Trier les prédictions avant de concevoir.** Une expérience ne réfute aucun théorème ; elle réfute l'adéquation du modèle à un vrai entraînement. Réfutables :
  1. *l'enrichissement de première génération* : après un tour de rejet, la hausse de la survie moyenne des tricheurs vaut variance sur moyenne, calculée sur les épisodes du modèle de base. C'est le terme de sélection de l'équation de Price ; l'écart observé est le terme de transmission, c'est-à-dire la généralisation, sur laquelle le papier se dit muet. L'expérience la mesure au lieu de la supposer ;
  2. *la bistabilité à deux canaux* : l'état final dépend de la dose initiale de triche et d'obscurcissement ; le modèle de base reste honnête là où un modèle amorcé bascule ;
  3. *la pénalité* : effet non monotone, bascule possible vers la triche obscurcie hors des deux fenêtres (défaut 3 de la contre-lecture de la dynamique) ;
  4. *la normalisation par groupe ne change que l'horloge* : mêmes trajectoires, temps redimensionné ;
  5. *la sonde figée* sur activations partagées est déplacée par l'entraînement contre le filtre de texte ; la sonde réapprise garde la séparabilité.

  Non réfutables ici : les limites à pression infinie ; les seuils exacts (la pression effective n'est pas observable, et un paramètre ajusté par bras ferait tout coller : elle s'étalonne une fois, sur le bras sans filtre) ; l'invariance exacte sur neurones disjoints (un transformeur n'en a pas) ; les bornes du budget d'audit.
- **Ne pas attendre l'invention spontanée.** Le papier prend la masse furtive initiale pour donnée : l'expert la mesure, puis la fabrique par doses. Banc gradué : omission (la chaîne de pensée tait le contournement), euphémisation, codage par substitution planté par affinage préalable. À cette taille l'omission est le niveau réaliste ; elle se nomme ainsi, pas « stéganographie ».
- **Retenir trois contrastes principaux au plus**, pas le plan à quatre bras et pièges de Carbon.
- **Geler les énoncés.** Les prédictions citent par empreinte les sections corrigées après contre-lecture, jamais les brouillons.

**2. Données brutes de départ.** Pas les tableaux du manuscrit, qui évaluent des formules. À la place :
- les épisodes bruts du modèle de base avant tout entraînement (énoncé, chaîne de pensée, code, verdict des tests visibles et cachés, verdict de chaque moniteur), assez nombreux pour estimer les trois masses et les taux de survie ;
- les poids et licences des modèles candidats : Qwen2.5-7B, Llama-3.1-8B, DeepSeek-R1-Distill-Qwen-7B pour son canal de réflexion natif (licences à vérifier, celle de Qwen2.5-3B surtout) ;
- les bancs : MBPP+ et HumanEval+ (EvalPlus), où les tests d'origine servent de tests visibles contournables et les tests étendus de vérité cachée ; ImpossibleBench, School of Reward Hacks, les environnements de Baker et al. 2025, Skaf et al. 2025 sur le codage appris sous pénalité (existence, contenu et licence à vérifier pour ces quatre) ;
- les débits mesurés sur la carte graphique louée.

**3. Méthodes et outils**
- **Vérité de la triche par programme** (tests cachés, cas codés en dur, fichier de tests touché), jamais par la chaîne de pensée.
- **Entraînement** par adaptateurs de rang faible : affinage supervisé filtré itéré (le rejet répété du papier) et gradient de politique ancré au modèle de base (la pénalité), avec et sans normalisation par groupe.
- **Mesures de l'obscurcissement** : taux de mention du contournement (lexique, juge local) ; capture par un moniteur tenu à l'écart, d'une autre lignée que le modèle entraîné ; longueur ; charge causale (tronquer ou paraphraser la chaîne de pensée change-t-il le code ?) ; aire sous la courbe d'une sonde figée et d'une sonde réapprise.
- **Séparer « furtif appris » de « visible devenu rare ».** Variable principale : le taux absolu d'épisodes trichés et non interceptés, pour mille épisodes, contre le bras sans filtre à pas égal. La part furtive parmi les tricheurs monte dès que le visible disparaît : elle reste descriptive. Puis la décomposition de Price (sélection seule prédite depuis les épisodes initiaux, contre l'observé) et le transfert vers des tâches et un moniteur jamais vus.
- **Contrôles négatifs** : filtre au hasard de même taux de rejet (enrichissement prédit nul) ; tâches sans avantage à tricher ; bras sans filtre. **Contrôle positif** : modèle furtif planté, qui prouve que la chaîne de mesure voit une furtivité apprise ; s'il échoue, l'essai est « non évaluable », pas négatif. Chaque garde éprouvée sur un cas sain et un artefact.
- **Puissance** : l'unité est la course, pas l'épisode. Graines appariées entre bras ; un test des signes bilatéral à 5 % exige au moins six paires (cinq donnent au mieux 0,0625). Le nombre final sort d'une simulation sur la variance d'un pilote qui ne lit aucun contraste décisif. Zéro furtif sur n épisodes borne le taux à environ 3/n.
- **Devis ascendant** : par bras et par graine, jetons générés, pas d'entraînement, évaluations, convertis en heures par des débits mesurés ; prix horaire relevé et daté ; marge de relance pour panne ; stockage ; moniteurs locaux comptés dans les heures de carte ; aucun appel d'interface payant (un juge fermé n'est ni rejouable ni stable). Le chiffre de Carbon, sans source, n'est pas repris. Deux étages : étalonnage plafonné, puis devis complet.

**4. Validation extérieure.** Empreinte du préenregistrement horodatée avant toute course ; verdict par un agent neuf sur critères gelés ; réplication du contraste principal sur une seconde famille de modèles ; code, graines et manifestes publics, rejouables par un tiers sur les mêmes poids ; sous-ensemble étiqueté par deux lecteurs indépendants pour valider les moniteurs ; accord de sens avec les résultats publiés dans le régime commun ; relecteurs de la revue.

### Volet (b) — vérification sur PDF des références

1. **Expert.** Il vérifie l'affirmation, pas seulement la notice : pour chaque citation, la page et le passage qui portent ce que le papier lui fait dire (attributions à Price, Robertson, Fisher, Lancaster, Kakade). Il lit aussi les voisins proposés par les contre-lecteurs, car ils conditionnent chaque « à notre connaissance ».
2. **Données brutes.** Le PDF de la version de référence de l'éditeur, obtenu par l'identifiant numérique d'objet, ou la version exacte du dépôt arXiv citée ; pour un livre, l'édition et le numéro du théorème ; pour un billet, une capture d'archive datée. Ni la mémoire ni les seules métadonnées.
3. **Méthodes.** Comparaison automatique de la bibliographie aux registres Crossref, arXiv et DBLP (titre, auteurs et leur ordre, année, volume, pages, numéro) ; lecture de la page rendue ; empreinte de chaque PDF ; un registre par référence : clé, notice vérifiée, source, date d'accès, empreinte, page, citation courte, verdict (conforme, corrigée, non confirmée, introuvable). Un PDF sous droits reste hors de la copie publique : seules l'empreinte et la source entrent au registre. **Référence introuvable** : jamais citée de mémoire ; la remplacer par une source vérifiée portant la même affirmation, la citer de seconde main en le disant, ou retirer l'affirmation. Un PDF inaccessible est une panne : le demander à Lazar.
4. **Validation extérieure.** Second vérificateur neuf sur tous les écarts et un échantillon tiré au sort ; registres d'identifiants comme vérité tierce ; script rejouable.

Écarts déjà signalés à trancher : titre de Griffin et al. (deux variantes dans les pièces), année de Hirsch et Smith, numéro du théorème de Bernstein ; à contrôler de près, le numéro arXiv de Bartók et al.

## 2. Ce que la fille 1 fait « à la place de la fille 2 »

Sans toucher son périmètre, dans des dossiers neufs :
1. **Le registre des références de toutes les pièces** (manuscrit, dynamique, budget d'audit, découplage). Les corrections de bibliographie partent en liste vers la fille 2, par les mères.
2. **Le préenregistrement et le devis** : aucun dossier attribué ne les couvre.
3. **La vérification en Lean des contre-exemples exacts des contre-lectures** (bord de l'inégalité du taux de maintien, plans qui ne dissuadent pas une autre fréquence de triche) : elle épargne une revérification à la fille 2.
4. **L'essai à blanc sur processeur** de la chaîne de mesure, avec un modèle minuscule.

Elle ne refait ni les contre-lectures ni la v4.

**À demander aux mères** :
- une note de partage v2 attribuant à la fille 1 deux dossiers neufs, par exemple `papiers/D/prereg-modele-ouvert-v1/` et `papiers/D/references-v1/` (« tout le reste » revient aujourd'hui à la fille 2), et confirmant son droit de pousser ;
- les chemins et empreintes des énoncés de référence (manuscrit v4 et correctif, dynamique et budget corrigés, découplage v3), question restée sans réponse ;
- l'accord de la fille 2 pour citer la vérification Lean dans une pièce publique ;
- l'ouverture du réseau vers les registres et les éditeurs ;
- à Lazar : les PDF sous droits, l'échéance visée, le plafond de l'étalonnage.

## 3. Demande reformulée, servie telle quelle à la fille 1

Prépare, sans rien dépenser, les pièces qui rendent le papier D réfutable par une expérience sur modèle ouvert de trois à huit milliards de paramètres, et vérifie sur PDF toutes ses références. L'expérience mesure, sur des tâches de code à tests contournables et un banc gradué d'obscurcissement de la chaîne de pensée, trois contrastes au plus, tirés des énoncés corrigés et cités par empreinte ; elle sépare la sélection de la généralisation et la furtivité apprise de la triche visible devenue rare. Le préenregistrement et le devis sont conçus par Fable 5.2 et contre-lus par un Opus 5.5 neuf, qui vérifie ensuite les corrections. Aucune dépense avant le GO de Lazar sur devis.

1. **Partage** (travail). Note aux mères avec les demandes du § 2. Fin : note de partage v2 reçue.
2. **Registre des références** (instrument : le script ; travail : le registre). Fin : chaque référence a un verdict, une empreinte et une page ; liste des corrections transmise ; second vérificateur passé.
3. **Carte des prédictions** (travail). Tableau : énoncé, empreinte, grandeur mesurée, issue qui le réfute, coût relatif. Fin : trois contrastes proposés à Lazar.
4. **Inventaire des bancs, modèles et licences** (travail). Fin : chaque nom vérifié sur sa source ou écarté.
5. **Chaîne de mesure et essai à blanc sur processeur** (instrument, contre-lue). Vérité par programme, moniteurs locaux, mesures d'obscurcissement, décomposition de Price, graines par `SeedSequence`, manifeste. Fin : gardes éprouvées sur cas sain et artefact ; contrôle positif planté détecté sur données synthétiques.
6. **Préenregistrement** (décisive ; Fable, effort maximal). Hypothèses bilatérales, prédictions chiffrées et signes, variable principale, seuils, contrôles, puissance, plan d'analyse, issues codées, liste d'arrêt. Fin : contre-lu, corrigé, vérifié, scellé.
7. **Devis en deux étages** (décisive ; Fable). Étalonnage plafonné, puis devis par bras et par graine. Fin : contre-lu, scellé, soumis à Lazar.
8. **Arrêt.** Passation ; aucune location avant le GO.
