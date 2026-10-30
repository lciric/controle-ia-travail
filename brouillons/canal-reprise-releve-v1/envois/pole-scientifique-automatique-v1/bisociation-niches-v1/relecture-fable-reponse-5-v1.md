# Relecture indépendante de `reponse-conv-audit-question-5-v1.md` (identifier par apprentissage profond les paramètres qui créent la fertilité) — v1

Relecteur : sous-agent neuf (règle R2), n'ayant écrit ni la réponse ni les questions. Modèle : Fable 5.1 (claude-fable-5-1). Date (`date -u`) : Fri Oct 30 17:21:58 UTC 2026 (début de rédaction ; l'horloge du conteneur diffère de celle qui date les fichiers, qui portent 18:10 à 18:15 ; la rédaction a été reprise après une limite d'usage).

Lu : `question-5-causes-v1.md`, `question-1-chapelles-v1.md`, `question-2-niches-v1.md`, `question-3-fertilite-v1.md`, `question-4-apprendre-v1.md`, `reponse-conv-audit-question-5-v1.md` (objet de la relecture, empreinte `a47ba916…e58ae0442`). Non lu : les autres `reponse-*`, les `relecture-*`, `revue-biblio-*`, tout `donnees/`. Aucune dépense, aucune opération git.

Incident de lancement : au démarrage, le fichier à relire était absent du dossier (vérifié par `ls`, `find` sur tout le disque et attente ; règle R11). Il est apparu ensuite ; la relecture porte sur la version d'empreinte ci-dessus.

Niveaux de vérification : **V-session** = page éditeur ou arXiv lue en ligne pendant cette relecture (aucun PDF empreinté, donc rien d'opposable au sens de R7) ; **SUPPOSÉ** = cité de mémoire, à vérifier avant tout usage dans un préenregistrement ou un papier.

## Verdict (une ligne)

Réponse juste dans sa position (observer n'est pas intervenir), tenue en forme et en longueur, mais elle se contredit sur le rôle de la découverte causale observationnelle, passe sous silence le problème de transport entre nos courses et la science réelle, et sa reformulation n'a aucun critère de mort chiffré : à corriger avant usage.

## (a) Les quatre points et la reformulation sont-ils tenus, sans allonger ?

Oui pour la forme : une page, quatre rubriques, une reformulation. Deux réserves de fond :

- Le point (4) « vérification hors de nous » n'est pas hors de nous. Trois des quatre items (prédiction à la course suivante, courses randomisées, tests de mort) sont produits par l'organisme lui-même, avec ses juges figés. Seuls « expériences naturelles indépendantes » et « reproduction sur d'autres domaines et décennies » sont externes. Voir RL5-06.
- La reformulation est une liste de moyens (graphe, trois voies, modèle d'agents, transition, validité), non une demande reformulée « pour répondre précisément à l'exigence » : elle ne dit pas quel paramètre, quelle intervention, quel résultat chiffré tuerait l'hypothèse. Voir RL5-08.

## (b) Affirmations, références, antériorités

### Références citées — état de vérification

| Référence dans la réponse | Attribution | Statut |
|---|---|---|
| Azoulay, Graff Zivin et Wang 2010 (décès de chercheurs étoiles, « Superstar Extinction », *Quarterly Journal of Economics*) | Correcte | SUPPOSÉ (de mémoire ; attribution cohérente avec la littérature) |
| Peters, Bühlmann et Meinshausen 2016 (prédiction causale invariante, *Journal of the Royal Statistical Society B*) | Correcte | SUPPOSÉ |
| Arjovsky 2019 (minimisation du risque invariant, avec Bottou, Gulrajani, Lopez-Paz ; prépublication arXiv, jamais publiée en revue à ma connaissance) | Correcte, mais citer « Arjovsky 2019 » seul est incomplet | SUPPOSÉ |
| Athey et Wager (forêts causales ; Wager et Athey 2018 *Journal of the American Statistical Association* ; Athey, Tibshirani et Wager 2019 *Annals of Statistics* pour les forêts généralisées) | Correcte, année absente | SUPPOSÉ |
| PCMCI de Runge (Runge, Nowack, Kretschmer, Flaxman et Sejdinovic 2019, *Science Advances*) | Correcte | SUPPOSÉ |
| NOTEARS (Zheng, Aragam, Ravikumar et Xing 2018, *NeurIPS*) | Correcte | SUPPOSÉ |
| Dragonnet (Shi, Blei et Veitch 2019, *NeurIPS*), TARNet (Shalit, Johansson et Sontag 2017, *ICML*) | Correcte | SUPPOSÉ |
| Derex et Boyd 2016, *PNAS*, « Partial connectivity of cultural groups promotes cultural diversity and complex problem-solving » | Correcte | V-session (page PubMed Central PMC4801235 ; titre et année confirmés) |
| Mason et Watts (2012, *PNAS*, « Collaborative learning in networks ») | Correcte, année absente | SUPPOSÉ |
| Valeurs E (VanderWeele et Ding 2017, *Annals of Internal Medicine*) | Non attribuée dans la réponse | SUPPOSÉ |
| « Voir » contre « faire » (Pearl) | Correcte | SUPPOSÉ |

Aucune référence inventée ou mal attribuée détectée. Deux imprécisions : « Arjovsky 2019 » sans coauteurs ni statut de prépublication ; Athey-Wager et Mason-Watts sans année.

### Affirmations fausses ou trop fortes

- RL5-01 (**majeur**) — « Non, pas avec des données d'observation seules » puis, trois lignes plus bas, « découverte de structure (PCMCI, NOTEARS) » qui sont précisément des méthodes sur données d'observation seules. La réponse se contredit. La formulation juste : on peut identifier des causes sur données d'observation seules *sous des hypothèses non testables* (suffisance causale, c'est-à-dire aucun facteur caché ; fidélité ; pour NOTEARS, bruit additif et sensibilité à l'échelle des variables) ; ces hypothèses doivent être écrites et, en science des sciences, sont presque toujours fausses (prestige, financement, mode sont des facteurs cachés qui touchent à la fois le contact et la reprise). Le « non » doit devenir « seulement sous hypothèses écrites et attaquées ».
- RL5-02 (**majeur**) — « Apprentissage profond là où il est causal : PCMCI, NOTEARS ». Ni l'un ni l'autre n'est de l'apprentissage profond : PCMCI est une procédure de tests d'indépendance conditionnelle (famille Peter-Clark adaptée aux séries temporelles), NOTEARS une optimisation continue d'un graphe acyclique, linéaire dans sa version de base. Lazar demande explicitement « par apprentissage profond » ; la réponse glisse d'« apprentissage profond » à « méthodes causales » sans le dire. Il faut l'écrire : l'apprentissage profond n'identifie rien par lui-même ; il sert d'estimateur de fonction (réseaux à deux têtes, substitut) à l'intérieur d'un schéma d'identification qui vient d'ailleurs (randomisation, expérience naturelle, hypothèse d'invariance).
- RL5-03 (**modéré**) — NOTEARS cité sans ses faiblesses connues : sur données d'observation il ne peut distinguer que la classe d'équivalence de Markov, et ses bons résultats sur simulations tiennent largement à un artefact d'échelle des variances (« varsortabilité » : Reisach, Seiler et Weichwald 2021, *NeurIPS*, « Beware of the simulated DAG » — V-session, page arXiv 2102.13647). Sur un hypergraphe de citations où les variances croissent avec l'âge et la taille des niches, cet artefact est garanti. « Versions avec interventions » est vague : nommer (par exemple DCDI, Brouillard et al. 2020 — SUPPOSÉ) ou retirer.
- RL5-04 (**modéré**) — « Conférences annulées en 2020 » comme expérience naturelle : en 2020 tout a été annulé en même temps, il n'y a pas de groupe témoin contemporain, seulement une variation de calendrier (conférences tenues en janvier-février contre mars-juin), et la pandémie touche aussi l'issue (reprise) par d'autres canaux. L'expérience naturelle propre existe déjà : Campos, Leon et McQuillin 2018, *Economic Journal*, « Lost in the storm : the academic collaborations that went missing in Hurricane Isaac » (annulation d'une seule conférence de science politique ; V-session, billet et page de résumé).
- RL5-05 (**mineur**) — « Fusions de revues » : événement rare, mal daté, et la revue n'est pas la niche ; peu exploitable. « Financements imposant l'interdisciplinarité » : l'expérience naturelle documentée porte sur l'orientation des sujets par appels ciblés (Myers 2020, *American Economic Journal : Applied Economics*, « The elasticity of science » — SUPPOSÉ), pas sur l'interdisciplinarité imposée.

### Antériorités manquées

- RL5-09 (**majeur**) — Les expériences naturelles de la science des sciences qui portent *exactement* sur les trois leviers que Lazar cite (changement de laboratoire, mise en présence de niches, expérience contrôlée) existent et ne sont pas nommées :
  - chercheurs qui changent de laboratoire : Catalini 2018, *Management Science*, « Microgeography and the direction of inventive activity » (désamiantage du campus de Jussieu, laboratoires déplacés au hasard ; V-session, page éditeur) ;
  - deux communautés mises en présence : Borjas et Doran 2012, *Quarterly Journal of Economics* (effondrement de l'Union soviétique, mathématiciens soviétiques et américains — SUPPOSÉ) ; Moser, Voena et Waldinger 2014, *American Economic Review* (émigrés allemands — SUPPOSÉ) ;
  - canal de communication coupé (le cœur de la question 2) : Iaria, Schwarz et Waldinger 2018, *Quarterly Journal of Economics*, « Frontier knowledge and scientific production : evidence from the collapse of international science » (Première Guerre mondiale — SUPPOSÉ) ; Agrawal et Goldfarb 2008 (réseau Bitnet — SUPPOSÉ) ;
  - mort d'une étoile qui *ouvre* une niche aux entrants, version la plus proche de « niches qui ne se parlent pas » : Azoulay, Fons-Rosen et Graff Zivin 2019, *American Economic Review*, « Does science advance one funeral at a time ? » (SUPPOSÉ) ; la réponse cite seulement le papier de 2010 sur la productivité des collaborateurs ;
  - expérience de terrain randomisée sur la mise en contact de chercheurs : Boudreau, Brady, Ganguli, Gaule, Guinan, Hollenberg et Lakhani 2017, *Review of Economics and Statistics*, « A field experiment on search costs and the formation of scientific collaborations » (V-session, page IDEAS/RePEc) ; Lane, Ganguli, Gaule, Guinan et Lakhani 2021, *Strategic Management Journal*, « Engineering serendipity » (SUPPOSÉ). Ce sont les « Derex et Boyd » de la science réelle ; leur absence est l'oubli le plus coûteux.
- RL5-10 (**modéré**) — Découverte causale sur données scientométriques : je ne connais pas de travail qui applique PCMCI ou NOTEARS à un hypergraphe de citations pour en extraire les causes de la reprise ; les travaux proches sont des simulations étalonnées (Rzhetsky, Foster, Foster et Evans 2015, *PNAS*, déjà cité dans la question 4 ; Lazer et Friedman 2007, *Administrative Science Quarterly*, pour l'effet de la structure du réseau sur l'exploration — SUPPOSÉ) et des travaux de causalité à la Granger. Zone apparemment vierge, donc question, pas trou (règle R8) : vérifier par une recherche dédiée avant de la revendiquer, et se demander pourquoi les économistes de la science, qui connaissent ces outils, ne les ont pas employés (réponse probable : facteurs cachés et non-stationnarité, voir RL5-11).

## (c) Ce qu'un expert aurait dit et qui manque

- RL5-11 (**majeur**) — Transport. L'expert aurait séparé trois questions que la réponse fond en une : (i) ce qui cause la fertilité *dans nos courses* (identifiable par randomisation, mais vrai de nos agents et de nos juges) ; (ii) ce qui cause la fertilité *dans la science réelle* (expériences naturelles) ; (iii) à quelles conditions (i) se transporte vers (ii). La question (iii) est le problème de transportabilité (Pearl et Bareinboim 2011, 2014 — SUPPOSÉ) ; il exige d'écrire quels mécanismes sont supposés communs aux deux mondes et quels nœuds diffèrent (par exemple : nos agents n'ont ni carrière, ni financement, ni prestige). Sans cela, « prédire l'effet d'une intervention jamais vue à la course suivante » prouve une causalité dans le monde de la course, pas dans le monde. La réponse l'effleure (« causalité dans le modèle contre dans le monde ») mais sa reformulation l'oublie.
- RL5-12 (**majeur**) — Manipulabilité. « Les paramètres qui créent la fertilité » mélange deux natures de variables : des variables manipulables (dose de contact, choix de la paire, calendrier) et des attributs non manipulables de la paire (distance de domaine, âge des niches, structure mathématique commune). Pour les secondes, « pas de causalité sans manipulation » (Holland 1986 — SUPPOSÉ) : on ne peut qu'estimer comment l'effet d'une intervention manipulable *varie* selon ces attributs (modération, effets hétérogènes), ce qui est le vrai usage des forêts causales et des réseaux à deux têtes. La réponse cite les bons outils sans dire que c'est pour cela qu'ils servent. Conséquence pratique : la question de Lazar devient « quelles interventions manipulables, et sous quels attributs de la paire, augmentent la fertilité ? », ce qui est testable.
- RL5-13 (**modéré**) — Mesure de l'issue. En littérature réelle, « fertilité » sera mesurée par un proxy (citations, nouveauté à la Uzzi, reprise) ; une cause identifiée sur le proxy n'est pas une cause de la fertilité si le proxy a ses propres causes (effet Matthieu, visibilité des revues). L'expert exigerait un modèle de mesure ou au moins deux proxys indépendants. Lien avec la question 3, non fait.
- RL5-14 (**modéré**) — Survivants et témoins. La question 4 a établi le principe des témoins (paires comparables jamais rencontrées). La réponse 5 l'oublie : tout panel observationnel de « ponts » est un panel de survivants ; le graphe causal du point (1) doit contenir un nœud « sélection » et les expériences naturelles doivent être exploitées sur l'ensemble des paires à risque, pas sur celles qui ont produit un pont.
- RL5-15 (**mineur**) — Outils modernes de différence de différences : avec adoptions échelonnées (déménagements, décès à des dates différentes), l'estimateur à effets fixes classique est biaisé ; nommer les estimateurs robustes (Callaway et Sant'Anna 2021 ; Goodman-Bacon 2021 — SUPPOSÉ). Le contrôle synthétique exige une longue période préalable, ce qui limite son usage à des niches anciennes.
- RL5-16 (**mineur**) — Puissance. Aucun ordre de grandeur du nombre de paires ou de courses nécessaires ; les effets d'expérience naturelle en science des sciences sont de l'ordre de 5 à 10 % sur des milliers d'unités (SUPPOSÉ, ordre de grandeur). Avec quelques dizaines de paires par bras dans nos courses, seule une dose-réponse très forte sera visible.

## (d) Confusions

- Causalité dans le modèle contre dans le monde : la distinction est énoncée (point 1, dernier tiret) mais non appliquée (RL5-11). L'ablation d'un trait dans un réseau entraîné sur les citations dit ce que le réseau utilise, pas ce qui cause la reprise ; la régression symbolique « sur la fonction causale » n'est causale que si la fonction a été apprise sous intervention.
- Invariance : RL5-17 (**modéré**) — Utiliser sous-domaines, décennies et pays comme « environnements » suppose que le mécanisme causal de la reprise est *le même* dans tous et que seuls les facteurs non causaux varient. Or la non-stationnarité du mécanisme (pression à publier, bases de données, taille des équipes) est précisément ce que la science des sciences documente d'une décennie à l'autre ; prendre les décennies comme environnements viole l'hypothèse d'invariance au lieu de l'exploiter. De plus la minimisation du risque invariant a des contre-exemples connus où elle n'est pas meilleure qu'une régression ordinaire (Rosenfeld, Ravikumar et Risteski 2021, *ICLR*, « The risks of invariant risk minimization » — SUPPOSÉ). La prédiction causale invariante de Peters et al. exige en outre que l'issue elle-même ne soit pas intervenue entre environnements, ce qui est douteux quand les pratiques de citation changent.
- Identification : RL5-18 (**modéré**) — Les forêts causales, Dragonnet et l'apprentissage double robuste *estiment* un effet déjà identifié sous « pas de facteur caché » ; ils n'identifient pas « quels paramètres créent ». La réponse les range sous « découverte » par juxtaposition. Les valeurs E quantifient la robustesse à un facteur caché pour un effet donné, pas la validité de la découverte de structure. Le graphe causal du point (1) est le bon point d'entrée, mais il doit être écrit *avant* de choisir l'estimateur, et chaque flèche inconnue doit recevoir une méthode d'identification nommée, sinon aucune.

## (e) La reformulation est-elle testable, avec critère de mort chiffré ?

- RL5-08 (**majeur**) — Non. Le seul critère est « prédire correctement l'effet d'une intervention jamais vue, confirmé par une expérience naturelle indépendante ; sinon corrélat, pas cause ». Il manque : la grandeur prédite (effet de la dose de contact sur le taux de survie aux tests de mort, en points) ; le signe ; la tolérance (intervalle de prédiction préenregistré et seuil au-delà duquel on déclare l'échec) ; la ligne de base à battre (un modèle purement prédictif, sans structure causale, prédit-il aussi bien l'intervention jamais vue ? s'il fait aussi bien, la structure causale n'apporte rien) ; le témoin négatif (une intervention préenregistrée comme sans effet doit donner zéro) ; et la règle d'arrêt (combien de courses, combien d'échecs). « Confirmé par une expérience naturelle » est inopérant tant que l'on n'a pas dit quelle grandeur commune aux deux mondes est comparée (RL5-11).
- Proposition de critère minimal, à chiffrer par Lazar : « l'hypothèse “la dose de contact cause la fertilité” est morte si, sur N courses préenregistrées, l'effet d'une dose jamais testée (par exemple 7 titres après 0, 2, 5, 10) sort de l'intervalle de prédiction à 90 % du modèle causal dans plus de k cas sur N, ou si le modèle purement prédictif entraîné sur les mêmes courses fait aussi bien à ε près ». N, k, ε à fixer avant la première course ; témoin négatif obligatoire (règle R5).
- Transition de phase : RL5-19 (**modéré**) — « Transition de phase par intervention sur la dose comparée à la courbe d'observation » n'est pas testable avec quatre doses (0, 2, 5, 10) : un seuil et une sigmoïde lisse y sont indiscernables. Il faut au moins six à huit doses resserrées autour du seuil supposé, un critère préenregistré de comparaison des deux formes (par exemple rapport de vraisemblance ou facteur de Bayes avec seuil), et une réserve explicite : « transition de phase » au sens de la question 3 n'a pas encore reçu de définition opératoire.

## Tableau des constats

| Code | Gravité | Objet |
|---|---|---|
| RL5-01 | majeur | Contradiction « non sans intervention » contre PCMCI/NOTEARS observationnels ; hypothèses non testables non écrites |
| RL5-02 | majeur | PCMCI et NOTEARS présentés comme apprentissage profond ; glissement sur la question posée |
| RL5-03 | modéré | NOTEARS sans ses limites (classe d'équivalence, varsortabilité) ; « versions avec interventions » vague |
| RL5-04 | modéré | Conférences annulées en 2020 : pas de témoin ; Campos, Leon et McQuillin 2018 est l'expérience propre |
| RL5-05 | mineur | Fusions de revues et financements interdisciplinaires : leviers mal choisis |
| RL5-06 | modéré | Point (4) : trois vérifications sur quatre sont internes à l'organisme |
| RL5-08 | majeur | Reformulation sans critère de mort chiffré, sans ligne de base, sans témoin négatif |
| RL5-09 | majeur | Expériences naturelles et de terrain exactement sur les leviers de Lazar non citées (Catalini, Borjas-Doran, Iaria et al., Azoulay et al. 2019, Boudreau et al.) |
| RL5-10 | modéré | Découverte causale sur scientométrie : zone apparemment vierge à traiter comme question (R8) |
| RL5-11 | majeur | Transport entre nos courses et la science réelle absent de la reformulation |
| RL5-12 | majeur | Manipulable contre non manipulable ; la question devient une question de modération |
| RL5-13 | modéré | Issue mesurée par proxy ; cause du proxy ≠ cause de la fertilité |
| RL5-14 | modéré | Survivants et témoins (question 4) oubliés dans le graphe causal |
| RL5-15 | mineur | Différence de différences échelonnée : estimateurs robustes à nommer |
| RL5-16 | mineur | Aucun ordre de grandeur de puissance |
| RL5-17 | modéré | Décennies comme environnements : viole l'invariance ; limites connues de la minimisation du risque invariant |
| RL5-18 | modéré | Estimation d'effet confondue avec identification et découverte |
| RL5-19 | modéré | Transition de phase indiscernable avec quatre doses |

(Le code RL5-07 n'est pas attribué.)

## Ce que je garderais tel quel

La position d'ouverture (voir contre faire) ; l'idée de prendre les courses comme laboratoire randomisé avec dose de contact ; la liste des trois voies ; l'exigence d'effets signés et chiffrés avec placebo et contrôle négatif ; Derex et Boyd, Mason et Watts comme modèles d'expérience contrôlée. Le squelette est bon ; ce sont les hypothèses d'identification, le transport et le critère de mort qui manquent.
