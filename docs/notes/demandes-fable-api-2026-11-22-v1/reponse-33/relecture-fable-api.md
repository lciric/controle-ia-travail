# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHw2KJXKrFNgQCmFT584`
- Heure (UTC) : 2026-11-22T12:07:03Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 64000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-33-fiches-servies-par-repli-v1.md` — sha256 71902bb491b725e10009ddd8792fbe5a517958ced5671647a2120f81854df8b0 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/question-neutre-idees-originales-servie-v1.md` — sha256 3d2d70d5633a3101705153b4cb403a77d012c12379b1780eb8e361f483a515a2 (compagnon : vérifié)
- Empreinte de l'invite envoyée : f4fa974daa8e3214e15870cdd18df6e71715e0c769329831ad3fde905f01cc58
- Jetons : entrée 1890, sortie 29546 (dont réflexion 20652), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.196960 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 33, version approfondie : les fiches servies par repli et l'héritage

## 0. Ce dont je dispose et ce qui manque

- **FAIT RAPPORTÉ.** La pièce « demande 33 » décrit le dispositif et le choix entre (a) et (b). La pièce « remarques » contient une question neutre sur les idées rares et confirmées, mais pas les réponses d'Argon et de Carbon que la consigne annonce. Je réponds donc sans les avoir vues. Je n'ai pas accès à la « réponse 28 » d'où vient cette question, et je ne peux pas recalculer les empreintes numériques des pièces.
- **Tension de consigne.** « Sans nom de personne » et « antériorité nommée avec ses auteurs » se contredisent. Je nomme les auteurs dans la seule section 7, personne ailleurs.
- **Zones vierges, traitées comme des questions :**
  - le nombre d'espèces, de lignées par espèce et de générations ;
  - le taux de refus ;
  - la règle exacte de récompense et ce qu'elle pilote ;
  - si les modèles de repli sont eux-mêmes des espèces en lice ;
  - ce que devient la place quand toute la chaîne de repli refuse ;
  - si la marque « servie par repli » est visible des modèles.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Un spécialiste des plans d'expérience avec non-observance, doublé d'un praticien des algorithmes évolutionnaires, ferait neuf choses que la demande ne réclame pas.

1. **Définir les grandeurs avant de choisir.** PROPOSITION. « Effet de l'espèce » peut désigner le modèle seul, ou le modèle tel qu'il est déployé, avec le filtre de son fournisseur et sa chaîne de repli. « Effet de l'héritage » peut désigner l'écart entre recevoir un héritage et n'en recevoir aucun, ou l'écart entre héritages de compositions différentes. Les options (a) et (b) ne faussent pas seulement une mesure : elles changent la grandeur mesurée.

2. **Nommer le problème.** HYPOTHÈSE. Trois problèmes classiques se cumulent :
   - la non-observance : le modèle désigné n'est pas celui qui a écrit ;
   - les données manquantes de façon non aléatoire : le refus dépend du contenu ;
   - l'interférence : une fiche héritée influence toutes les générations suivantes de sa lignée.

3. **Séparer trois registres que la demande confond.** PROPOSITION. Ce qu'on conserve, ce qu'on sert et ce qu'on crédite sont trois choses. Tout conserver ne coûte rien et n'est pas en débat. La décision porte sur le service et sur le crédit, qui peuvent recevoir des règles différentes.

4. **Contester deux affirmations de la demande.**
   - HYPOTHÈSE (déduction du dispositif décrit). « Une lecture peut les retirer après coup » n'est vrai que du décompte direct. Une fiche de repli déjà servie a influencé ses descendantes, qu'aucune lecture ne retire. L'option (a) est donc irréversible sur la trajectoire, tout comme (b).
   - Question. La demande dit que, sous (b), la lignée « ne se compare plus à une course sans repli ». Si « sans repli » veut dire « où un refus ne produit rien », l'héritage sous (b) lui est au contraire identique, et c'est (a) qui s'en écarte. Si cela veut dire « où aucun refus n'a eu lieu », aucune des deux options n'y est comparable. Le sens est à préciser.

5. **Chercher la cause du refus.** HYPOTHÈSE.
   - Si le filtre se déclenche sur l'entrée, c'est l'héritage servi qui provoque le refus. Exclure ces fiches revient alors à trier sur une conséquence de ce qu'on veut mesurer.
   - S'il se déclenche sur la sortie, c'est la proposition de l'espèce qui est censurée, vraisemblablement pas au hasard.

6. **Examiner la dynamique de sélection.** HYPOTHÈSE. Sous (a), si le modèle de repli écrit de meilleures fiches que l'espèce, la sélection favorise les lignées dont les sujets déclenchent le filtre. Sous (b), elle défavorise ces sujets et la lignée s'en éloigne. Dans les deux cas, le filtre devient une pression de sélection que personne n'a choisie.

7. **Relier la décision au but du programme.** HYPOTHÈSE. La question neutre vise les idées rarement proposées et confirmées. Si la rareté se mesure par rapport à ce que le système propose d'habitude, une fiche écrite par un autre modèle paraîtra rare dans la lignée d'accueil pour une raison étrangère à l'espèce. Sous (a), une espèce souvent refusée peut ainsi sembler plus originale qu'elle ne l'est.

8. **Vérifier si les modèles de repli sont des espèces en lice.** HYPOTHÈSE. Si oui, (a) crée un transfert d'une lignée concurrente vers une autre : les lignées convergent et l'écart entre espèces se réduit.

9. **Mesurer l'ampleur avant de débattre.** PROPOSITION. Si le repli est rare et réparti uniformément, la décision est sans conséquence mesurable et se tranche par commodité.

## 2. Les données brutes de départ

PROPOSITION. Partir des journaux d'appels aux interfaces de programmation des fournisseurs, et non du compteur « servie par repli » tenu par l'orchestrateur.

Par appel :
- l'identifiant du modèle désigné, et l'identifiant et la version du modèle tels que le fournisseur les renvoie dans sa réponse ;
- le motif d'arrêt et la catégorie de refus si elle existe, en distinguant le filtre sur l'entrée, le filtre sur la sortie et les autres pannes (délai dépassé, quota, sortie mal formée) ;
- le texte intégral de l'invite, donc la liste exacte des fiches d'héritage servies ;
- le texte brut de la sortie avant mise en fiche, y compris pour les tentatives refusées ;
- les paramètres d'échantillonnage, la graine, l'horodatage, le rang dans la chaîne de repli et le nombre de tentatives ;
- le coût facturé.

Par fiche : le verdict du contrôle indépendant, la décision de rétention et son motif, la lignée et la génération.

HYPOTHÈSE. Les fournisseurs modifient parfois filtres et modèles sans préavis. Sans version ni date par appel, un changement de taux de refus se confondrait avec un effet de génération.

## 3. Les méthodes et outils

1. **Graphe de provenance.** PROPOSITION. Relier chaque fiche aux fiches d'héritage présentes dans l'invite qui l'a produite. On en tire, pour chaque fiche, sa part d'ascendance de repli : la proportion de ses ancêtres écrits par un autre modèle que l'espèce.

2. **Modèle du refus.** PROPOSITION. Une régression logistique du refus sur l'espèce, la génération, le sujet et la composition de l'héritage servi. Elle dit si le refus est assimilable à du hasard une fois ces facteurs connus, ou non.

3. **Trois lectures fixées d'avance.** PROPOSITION.
   - Selon l'espèce désignée, quel que soit le modèle qui a écrit (analyse dite « en intention de traiter »). C'est la lecture principale, car seule l'assignation est protégée du tri par le filtre.
   - Selon le producteur réel.
   - Hors fiches de repli et hors descendantes au-delà d'un seuil d'ascendance.

4. **Bornes plutôt qu'estimation ponctuelle.** PROPOSITION. Quand le refus n'est pas ignorable, encadrer l'effet de l'espèce par des bornes sans hypothèse de modèle et par des bornes par élagage (références en section 7).

5. **Tirage au sort par lignée.** PROPOSITION. Assigner chaque lignée à « fiches de repli servies » ou « non servies ». L'inférence se fait par permutation des étiquettes de lignée, et les intervalles par rééchantillonnage de lignées entières, puisque les fiches d'une lignée ne sont pas indépendantes.

6. **Rejeu contrefactuel hors course.** PROPOSITION. Pour un échantillon de générations où un repli a eu lieu, relancer la génération suivante avec et sans la fiche de repli dans l'héritage, en plusieurs répliques par condition. HYPOTHÈSE à vérifier chez chaque fournisseur : la reproductibilité à graine fixée n'est pas garantie, d'où les répliques.

7. **Repli simulé tiré au sort.** PROPOSITION. Forcer le repli sur des appels que le filtre n'a pas refusés, à taux connu. C'est le seul moyen de séparer « écrit par un autre modèle » de « sujet qui déclenche le filtre », que les refus naturels confondent.

8. **Simulation préalable.** PROPOSITION. Un modèle jouet de lignées où l'effet de l'espèce, l'effet de l'héritage et le taux de refus sont fixés à la main. L'analyse doit retrouver ces valeurs avant d'être appliquée aux vraies données.

9. **Rareté.** PROPOSITION. Des appels répétés indépendants et des estimateurs de couverture issus du dénombrement d'espèces, calculés avec et sans les fiches de repli pour voir si la rareté apparente en dépend.

## 4. Ce qui vérifierait la validité, hors du directeur et de Claude

1. **Les métadonnées du fournisseur.** PROPOSITION. La marque « servie par repli » posée par l'orchestrateur doit coïncider avec le modèle renvoyé dans la réponse du fournisseur. Tout désaccord est un défaut de journalisation à corriger avant analyse.
2. **Le contrôle indépendant des modèles.** PROPOSITION. C'est celui que la question neutre décrit, calibré sur des cas à vérité connue. Les fiches lui sont soumises sans marque de provenance.
3. **Le tirage au sort lui-même.** FAIT RAPPORTÉ (principe classique des plans d'expérience). Un test par permutation tire sa validité de l'assignation aléatoire, et non d'un jugement.
4. **Un essai à blanc.** PROPOSITION. Deux bras sous la même règle donnent la mesure du bruit entre lignées, à laquelle tout écart sera comparé.
5. **Un dépôt horodaté du plan d'analyse.** PROPOSITION. Le plan est déposé avec son empreinte numérique avant l'ouverture des résultats.
6. **Un recalcul indépendant à étiquettes masquées.** PROPOSITION. Un tiers humain, ou un programme écrit séparément, recalcule à partir des journaux bruts sans savoir quel bras est lequel.
7. **Des cas plantés.** PROPOSITION. L'analyse doit retrouver le taux connu du repli simulé et les ascendances correspondantes.
8. **Limite de la consultation à trois modèles.** HYPOTHÈSE. L'accord de Fable, d'Argon et de Carbon ne vaut pas vérification : des modèles de langue peuvent partager les mêmes erreurs.

## 5. La demande reformulée

« À partir des journaux bruts d'appels, établir le taux de repli par espèce, génération et sujet, la cause des refus (entrée ou sortie) et l'identité des modèles de repli. Définir, avant tout résultat, l'effet de l'espèce et l'effet de l'héritage que le programme veut estimer. Fixer une règle distincte pour la conservation, le service et le crédit des fiches de repli, de sorte que l'effet de ce choix soit lui-même mesurable dans la course. Dire quel résultat, fixé d'avance, ferait conclure que le choix a compté, et quel contrôle extérieur aux modèles et au directeur le confirmerait. »

## 6. Réponse

### 6.1 Réponse courte, au format de la demande d'origine

**Choix.** PROPOSITION. Ni (a) ni (b) seules. Je propose de tout conserver, de tirer au sort par lignée entre « servies » et « non servies », et de prendre la lecture selon l'espèce désignée comme lecture principale. Ma confiance que cette option domine les deux autres est de 0,6.

**Si le tirage est impossible** (une seule lignée par espèce, budget). PROPOSITION. Je choisis (a), avec graphe de provenance et rejeu contrefactuel. Ma confiance que (a) vaut mieux que (b) n'est que de 0,55.

**Raison de préférer (a) par défaut.** HYPOTHÈSE.
- Sous (b), l'héritage est troué de façon inégale selon les espèces et trié par le filtre. Aucune analyse ne reconstitue ce que les propositions censurées auraient donné.
- Sous (a), la taille de l'héritage reste égale et la contamination se chiffre par la part d'ascendance.
- En contrepartie, (a) dilue les écarts entre espèces.

### 6.2 Ce que chaque option fausse

Toutes les cellules sont des HYPOTHÈSES à tester sur les journaux.

| Mesure | Option (a), servies | Option (b), non servies |
|---|---|---|
| Effet de l'héritage | Mêle la transmission au sein de l'espèce et l'apport d'un autre modèle. Peut gonfler l'effet chez les espèces souvent refusées. | Héritage plus mince et trié par le filtre. Effet atténué là où les refus sont nombreux. Taille de l'héritage confondue avec l'espèce. |
| Effet de l'espèce | Écarts tirés vers zéro. L'espèce peut être créditée du travail d'un autre. | Mesuré sur les seules propositions acceptées, donc biais de sélection. Rendement par appel pénalisé. |
| Rareté des idées | Les fiches étrangères paraissent rares dans la lignée d'accueil. | Les sujets sensibles sont sous-représentés : rareté créée par la censure. |
| Dynamique | Sélection possible en faveur des sujets à refus. | Dérive hors des sujets à refus. |

### 6.3 La troisième option, en détail

- **Conservation.** PROPOSITION. Toute fiche de repli est gardée, avec son producteur réel et son rang dans la chaîne. La marque reste dans les métadonnées, invisible des modèles proposeurs et du contrôle indépendant. Sinon la marque devient elle-même un traitement.
- **Service.** PROPOSITION. Avant le départ, chaque lignée est tirée au sort dans le bras « servies » ou le bras « non servies », et le tirage est enregistré. Dans le bras « non servies », la place reste vide, de sorte que ce bras soit la course où un refus ne produit rien.
- **Crédit.** PROPOSITION. Si la récompense pilote la suite (allocation d'appels, sélection), elle ne crédite pas l'espèce désignée pour une fiche de repli. Sinon, le système récompense le fait d'être refusé. Les analyses rapportent les deux comptes.
- **Hors course.** PROPOSITION. Le rejeu contrefactuel sur échantillon donne l'effet local d'une fiche de repli à une génération d'horizon, sans toucher à la course principale.

### 6.4 L'analyse qui dirait, après coup, si le choix a compté

PROPOSITION. Quatre lectures, fixées avant les résultats.

1. **Écart entre bras.** Sur la mesure principale (idées rares et confirmées par unité de coût), l'écart entre bras est jugé par permutation et rapporté au bruit de l'essai à blanc.
2. **Relation dose-effet.** La mesure est tracée en fonction de la part d'ascendance de repli, dans le bras « servies ».
3. **Rejeu contrefactuel.** On mesure la divergence des fiches produites avec et sans la fiche de repli, sur plusieurs répliques.
4. **Stabilité des conclusions.** On compare le classement des espèces et le signe de l'effet de l'héritage sous les trois lectures de la section 3.

**Résultats attendus.**
- « Le choix a compté » : l'écart entre bras sort de la distribution de permutation au seuil fixé par le directeur, ou le classement des espèces s'inverse d'une lecture à l'autre.
- « Le choix n'a pas compté pour la conclusion » : classements et signes stables, écart dans le bruit.
- « Indécidable » : trop peu de replis pour conclure. Cela ne prouve pas l'absence d'effet et doit être écrit tel quel.

### 6.5 Ce qui me ferait changer d'avis

- **Repli très rare et uniforme entre espèces et sujets.** PROPOSITION. Je retiendrais (a) seule, sans tirage. Le seuil se déduit de la simulation préalable : c'est le taux en deçà duquel l'écart entre lectures reste sous le bruit de l'essai à blanc.
- **Repli concentré sur une espèce au point d'écrire une part majeure de son héritage.** HYPOTHÈSE. Cette espèce n'est plus mesurable, ni sous (a) ni sous (b). La décision devient de changer de fournisseur ou de retirer l'espèce.
- **Refus déclenchés surtout par l'entrée.** HYPOTHÈSE. Le problème est alors dans l'héritage lui-même, dont certaines fiches déclenchent le filtre. Il se traite à la source, avant la question du repli.

## 7. Antériorités connues

Statut commun à toutes ces références : rapporté, non vérifié sur PDF, c'est-à-dire non vérifié sur le document d'origine au format de document portable. Aucun chiffre n'en est tiré.

**Données manquantes, sélection, non-observance**
- Rubin, 1976, « Inference and Missing Data » : conditions sous lesquelles un mécanisme de données manquantes est ignorable.
- Heckman, 1979, « Sample Selection Bias as a Specification Error » : biais d'un échantillon trié par un mécanisme lié au résultat.
- Angrist, Imbens et Rubin, 1996, « Identification of Causal Effects Using Instrumental Variables » : effet chez les observants, quand le traitement reçu diffère du traitement assigné.
- Frangakis et Rubin, 2002, « Principal Stratification in Causal Inference » : comparaison au sein de strates définies par le comportement après assignation.
- Manski, 1990, « Nonparametric Bounds on Treatment Effects », et Lee, 2009, « Training, Wages, and Sample Selection: Estimating Sharp Bounds on Treatment Effects » : bornes sous sélection.

**Plans d'expérience et interférence**
- Fisher, 1935, « The Design of Experiments » : inférence fondée sur le tirage au sort.
- Hudgens et Halloran, 2008, « Toward Causal Inference With Interference » : unités qui s'influencent, tirage par groupes.
- Salganik, Dodds et Watts, 2006, « Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market » : mondes parallèles et dépendance à la trajectoire quand les choix antérieurs sont transmis.

**Évolution et idéation par modèles de langue**
- Lehman et collaborateurs, 2022, « Evolution through Large Models ».
- Meyerson et collaborateurs, 2023, « Language Model Crossover: Variation through Few-Shot Prompting ».
- Romera-Paredes et collaborateurs, 2023, « Mathematical discoveries from program search with large language models » : boucles évolutionnaires dont un modèle de langue est l'opérateur de variation.
- Mouret et Clune, 2015, « Illuminating search spaces by mapping elites » : maintien de la diversité par niches.
- Si, Yang et Hashimoto, 2024, « Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers » (grands modèles de langue ; chercheurs en traitement automatique des langues) : redondance rapportée des idées entre appels répétés.
- Kleinberg et Raghavan, 2021, « Algorithmic monoculture and social welfare » : coût de l'homogénéité entre décideurs algorithmiques.

**Rareté**
- Good, 1953, « The Population Frequencies of Species and the Estimation of Population Parameters ».
- Chao, 1984, « Nonparametric Estimation of the Number of Classes in a Population ».

**Zone vierge.** Je ne connais pas de travail traitant précisément le repli sur refus de filtre comme source de contamination entre lignées dans une idéation à plusieurs modèles. Je n'ai fait aucune recherche bibliographique : c'est une question à instruire, pas une revendication de nouveauté.

## 8. Décisions qui reviennent au directeur

**Décision 1 : choisir la règle de service des fiches de repli.**
- Enjeu : c'est la seule décision irréversible, puisque la trajectoire des lignées en dépend.
- Option (a), servies avec marque. Avantage : héritage de taille égale, rien de perdu. Inconvénient : écarts entre espèces dilués, contamination non retirable.
- Option (b), non servies. Avantage : héritage identique à une course où le refus ne produit rien. Inconvénient : héritage troué et trié par le filtre.
- Option (c), tirage au sort par lignée entre (a) et (b). Avantage : l'effet du choix devient mesurable. Inconvénient : puissance divisée par deux, et il faut plusieurs lignées par espèce.
- Recommandation : (c) si chaque espèce a plusieurs lignées, sinon (a) avec rejeu contrefactuel. Confiance : 0,6.

**Décision 2 : fixer qui est crédité d'une fiche de repli.**
- Enjeu : si la récompense pilote l'allocation, créditer l'espèce désignée récompense le refus.
- Option 1, crédit à l'espèce désignée. Avantage : simple, cohérent avec la lecture principale. Inconvénient : incitation perverse possible.
- Option 2, crédit au producteur réel. Avantage : juste. Inconvénient : mêle les lignées dans les comptes.
- Option 3, crédit neutre pour le pilotage et double compte dans l'analyse. Avantage : aucune pression de sélection parasite. Inconvénient : deux comptes à tenir.
- Recommandation : option 3. Confiance : 0,6, plus basse tant que j'ignore ce que la récompense pilote.

**Décision 3 : faire ou non un audit des journaux bruts avant de trancher la décision 1.**
- Enjeu : si le repli est rare et uniforme, les décisions 1 et 2 sont sans conséquence.
- Option 1, audit court d'abord. Avantage : dimensionne tout le reste, révèle la cause des refus. Inconvénient : délai.
- Option 2, trancher maintenant. Avantage : pas d'attente. Inconvénient : risque de bâtir un tirage au sort pour un phénomène négligeable, ou de manquer une espèce devenue non mesurable.
- Recommandation : option 1. Confiance : 0,8.

**Décision 4 : choisir l'instrument qui sépare « autre modèle » de « sujet à refus ».**
- Enjeu : sans lui, l'analyse après coup reste une corrélation.
- Option 1, rejeu contrefactuel hors course. Avantage : ne contamine rien, coût borné. Inconvénient : horizon d'une génération seulement.
- Option 2, repli simulé tiré au sort dans la course. Avantage : effet à long horizon, cas plantés pour valider l'analyse. Inconvénient : ajoute volontairement de la contamination.
- Option 3, aucun des deux. Avantage : coût nul. Inconvénient : la question « le choix a-t-il compté » reste sans réponse causale.
- Recommandation : option 1 d'abord, option 2 seulement si l'audit montre un repli fréquent. Confiance : 0,65.

**Décision 5 : désigner le contrôle extérieur.**
- Enjeu : trois modèles d'accord ne constituent pas une vérification.
- Option 1, plan déposé à l'avance, essai à blanc et recalcul à étiquettes masquées par un tiers. Avantage : validité indépendante des modèles et du directeur. Inconvénient : charge d'organisation.
- Option 2, relecture croisée par les trois modèles. Avantage : rapide. Inconvénient : erreurs possiblement partagées.
- Recommandation : option 1, l'option 2 ne servant que de complément. Confiance : 0,75.

FIN DE LA RÉPONSE
