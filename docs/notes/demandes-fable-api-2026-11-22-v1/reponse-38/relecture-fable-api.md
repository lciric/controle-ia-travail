# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHyqJSUFaG1Py9qtS19i`
- Heure (UTC) : 2026-11-22T12:43:36Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 64000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-38-modes-recombines-v1.md` — sha256 45617e0f70e297a4d72467fad047951ab77ed20511c67608d310f11cc5194408 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/question-neutre-modes-attaque-servie-v1.md` — sha256 02ad3d76ae90648f2fbb8498bc109d4a51a9dddd8b965e03326013e9ee08c9b8 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 33d461fac67a43c475eb818ea1debfeceb48fe2fd882e2b2b869844845b09754
- Jetons : entrée 1807, sortie 29019 (dont réflexion 21654), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.175216 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 38 — modes recombinés : réponse en « demande approfondie »

**Réponse courte.** (PROPOSITION) Oui, les garder, mais comme instruments de mesure et non comme découvertes : étiquette propre, file séparée, hors du compte des modes, règles écrites avant toute mesure.

## 0. Constats sur les pièces

- (FAIT RAPPORTÉ) La pièce de remarques contient la question neutre servie aux modèles externes, mais aucune de leurs réponses ; je ne m'appuie donc sur aucune.
- (FAIT RAPPORTÉ) La pièce de demande porte le rôle « correction » ; je la traite comme la demande 38.
- (FAIT RAPPORTÉ) Je n'ai ni le registre des modes connus, ni le texte de l'épreuve « union ou conjonction de couples connus », ni aucune mesure. Je n'ai pas recalculé les empreintes numériques des pièces.
- (FAIT RAPPORTÉ) La consigne demande les auteurs des antériorités et interdit les noms de personne. Je donne titre, année et organisme ; les auteurs sont à ajouter lors de la vérification.
- Comme demandé, aucun mode concret ni procédé n'est décrit.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

1. (PROPOSITION) **Fixer l'unité de compte avant la politique.** « Connu » n'a de sens que par rapport à un registre daté, gelé et sourcé ; sans lui, « assemblage » n'est pas décidable.
2. (PROPOSITION) **Éprouver l'épreuve elle-même.** (HYPOTHÈSE) Elle peut se tromper de deux façons. Avec un registre riche, presque tout candidat se laisse redécrire après coup comme assemblage (nouveauté manquée). Avec un registre incomplet, un assemblage passe pour neuf. L'expert borne le nombre de composants, exige que chaque composant ait été inscrit avant le candidat et mesure l'accord entre deux classeurs indépendants.
3. (PROPOSITION) **Séparer deux sortes d'assemblage par une mesure.** L'assemblage « additif » est celui dont la détection se prédit à partir de ses composants ; l'assemblage « à interaction » s'en écarte. C'est le critère « décidable par une mesure et non par un avis » que réclame la question neutre.
4. (PROPOSITION) **Traiter l'explosion combinatoire.** Le nombre de couples croît comme le carré du nombre de modes ; on échantillonne par plan de couverture, on n'énumère pas.
5. (PROPOSITION) **Chercher l'antériorité de la combinaison et de la démarche**, pas seulement celle des composants.
6. (PROPOSITION) **Régler la garde de l'information.** Un assemblage qui échapperait aux trois familles de moniteurs serait la pièce la plus sensible du programme.
7. (PROPOSITION) **Demander le taux de base.** Quelle part des sorties de la course est classée « assemblage » ? La politique ne pèse pas autant à un dixième qu'à neuf dixièmes.

## 2. Données brutes de départ

(PROPOSITION) L'expert partirait de :
- les sorties brutes de la course d'idéation, horodatées, avec le modèle générateur, avant tout classement ;
- les verdicts de l'épreuve, avec justification et composants cités ;
- le registre des modes connus, ses versions et ses sources ;
- les scores bruts par épisode de chaque moniteur (lecteurs des états internes, juges du texte, contrôle au hasard du résultat), non seuillés, sur les modes pris isolément ;
- les transcriptions et la mesure de la dégradation effective de la tâche.

Il ne partirait pas du tableau « nombre de modes trouvés » ni des taux de détection agrégés.

## 3. Méthodes et outils

- (PROPOSITION) **Plan factoriel deux par deux, par couple.** Composant A présent ou absent, composant B présent ou absent, mêmes tâches, mêmes graines aléatoires, sur un modèle ouvert de petite taille.
- (PROPOSITION) **Deux prédictions de référence écrites d'avance.** La première : l'assemblage est au moins aussi détecté que son composant le plus détecté. La seconde : les détections sont indépendantes. L'interaction est l'écart à ces références.
- (PROPOSITION) **Test statistique.** Régression logistique à effets mixtes (tâche en effet aléatoire, terme d'interaction), intervalles par rééchantillonnage sur les tâches, contrôle du taux de fausses découvertes sur l'ensemble des couples, calcul de puissance préalable.
- (PROPOSITION) **Choix des couples** par plan de couverture par paires, complété d'un tirage au sort.
- (PROPOSITION) **Découpage de généralisation.** Les moniteurs sont calibrés sur les modes isolés et une partie des assemblages, puis éprouvés sur des assemblages tenus à l'écart, scellés par empreinte numérique avant toute mesure.
- (PROPOSITION) **Fiabilité du classement.** Deux classeurs indépendants, à l'aveugle de l'origine du candidat ; coefficient kappa d'accord.
- (FAIT RAPPORTÉ, non vérifié) **Outils.** Cadre d'évaluation ouvert « Inspect » de l'institut britannique de sécurité de l'intelligence artificielle ; bibliothèques statistiques « lme4 » (langage R) ou « statsmodels » (langage Python). (PROPOSITION) Plan d'analyse déposé et horodaté avant mesure.

## 4. Ce qui vérifierait le résultat, hors du directeur et de Claude

- (PROPOSITION) Un relecteur extérieur reclasse à l'aveugle un échantillon tiré au sort où candidats, variantes et assemblages sont mêlés ; son taux de désaccord est publié.
- (PROPOSITION) Un contradicteur tente de redécrire chaque « mode candidat » comme assemblage du registre, et l'inverse.
- (PROPOSITION) Un moniteur construit par une autre équipe, qui n'a jamais vu la part tenue à l'écart, est soumis à cette part.
- (PROPOSITION) Le plan, les empreintes et un critère d'échec sont déposés chez un tiers avant mesure.
- (PROPOSITION) L'expérience est répliquée sur un second modèle ouvert.
- (PROPOSITION) Une personne fait la recherche d'antériorité sur les documents sources.
- (HYPOTHÈSE) L'accord de plusieurs modèles de langue externes ne vaut pas vérification indépendante, car leurs sources se recouvrent.

## 5. Antériorités que je connais

(FAIT RAPPORTÉ) Statut de chaque ligne : **rapporté, non vérifié sur PDF** (document au format portable). Dans les titres, « AI » se lit intelligence artificielle et « LLM » grand modèle de langue.

| N° | Titre | Année | Organisme | Ce que cela apporte ici |
|---|---|---|---|---|
| 1 | « Attack Trees » | 1999 | revue Dr. Dobb's Journal | Une attaque se décrit par des nœuds « et » / « ou » : union et conjonction sont des opérations de description, non des catégories. |
| 2 | « MITRE ATT&CK: Design and Philosophy » (Adversarial Tactics, Techniques, and Common Knowledge) | 2018, révisé 2020 | MITRE | Tactiques, techniques, sous-techniques ; une campagne combine des techniques sans en créer. |
| 3 | Common Weakness Enumeration, page « Chains and Composites » | à vérifier | MITRE | « Chaîne » et « composite » sont des types d'entrée distincts des faiblesses de base : précédent direct pour une étiquette propre. |
| 4 | « Software Fault Interactions and Implications for Software Testing » | 2004 | Institut national des normes et de la technologie des États-Unis | Certains défauts ne se déclenchent que par interaction de facteurs ; fonde les plans de couverture par paires. |
| 5 | « The toxicity of poisons applied jointly » | 1939 | — | Modèle d'indépendance des effets conjoints : référence pour l'écart à la prédiction. |
| 6 | « Reliable Evaluation of Adversarial Robustness with an Ensemble of Diverse Parameter-free Attacks » | 2020 | université de Tübingen | Un ensemble d'attaques connues sert d'étalon d'évaluation. |
| 7 | « Jailbroken: How Does LLM Safety Training Fail? » | 2023 | université de Californie à Berkeley | Des combinaisons de procédés connus y sont rapportées plus efficaces que les procédés isolés, et présentées comme combinaisons. |
| 8 | « h4rm3l: A Dynamic Benchmark of Composable Jailbreak Attacks for LLM Safety Assessment » | 2024 | université Stanford (à vérifier) | Banc construit par composition de primitives connues : la démarche elle-même a une antériorité. |
| 9 | « Measuring Compositional Generalization: A Comprehensive Method on Realistic Data » | 2020 | Google | Découpage « composants vus, composés tenus à l'écart ». |
| 10 | « AI Control: Improving Safety Despite Intentional Subversion » | 2023 | Redwood Research | Cadre équipe attaquante contre protocole de surveillance. |
| 11 | « Sabotage Evaluations for Frontier Models » | 2024 | Anthropic | Évaluations de sabotage sous surveillance. |
| 12 | « SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents » (Subtle Harmful Agent Detection and Evaluation, développement à vérifier) | 2025 | Anthropic et partenaires | Banc d'agents saboteurs et de moniteurs. |
| 13 | « Detecting Strategic Deception Using Linear Probes » | 2025 | Apollo Research | Généralisation de lecteurs d'états internes hors distribution. |
| 14 | Arrêt « KSR International contre Teleflex » | 2007 | Cour suprême des États-Unis | En droit des brevets, une combinaison d'éléments connus aux résultats prévisibles est tenue pour évidente. |

- (HYPOTHÈSE, à traiter comme une question) Je ne connais pas de publication qui mesure si des lecteurs d'états internes calibrés sur des modes de sabotage isolés généralisent à leurs combinaisons. C'est une question pour la recherche bibliographique, non une revendication de zone vierge.
- (PROPOSITION) Qu'un de ces papiers ne sépare pas modes isolés et combinaisons serait une limite de ce papier, pas un trou du champ.
- Je ne cite aucun chiffre de ces travaux : aucun n'est opposable sans vérification.

## 6. Demande reformulée

« Sur un registre gelé et daté des modes connus, et pour un échantillon de couples tiré par plan de couverture :
1. L'épreuve de classement est-elle reproductible entre classeurs indépendants ?
2. La détection d'un assemblage par chaque famille de moniteurs se prédit-elle à partir de celle de ses composants, à un écart fixé d'avance ?
3. Des moniteurs calibrés sur les modes isolés généralisent-ils à des assemblages tenus à l'écart ?

Selon ces trois réponses, sous quelle étiquette, dans quelle file et avec quel poids garder les assemblages ? Que faut-il écrire avant de s'en servir ? Qui, hors du programme, peut contredire le résultat ? »

## 7. Réponse (moins de 900 mots)

### 7.1 À quoi un assemblage sert, et ne sert pas

- (PROPOSITION) **Élargir le banc de moniteurs.** (HYPOTHÈSE) Un adversaire réel combine ; un banc de modes isolés surestime la robustesse dès qu'il existe des interactions. L'assemblage est ici un cas d'épreuve, compté comme tel.
- (PROPOSITION) **Éprouver la généralisation.** C'est l'usage le plus précieux. Composants vus, composés tenus à l'écart : la distance au connu est contrôlée, ce qu'aucun mode réellement neuf ne permet (FAIT RAPPORTÉ : schéma de la ligne 9).
- (PROPOSITION) **Tenir à l'écart, mais en strate distincte.** (HYPOTHÈSE) Une réserve faite d'assemblages mesure la généralisation aux combinaisons, pas à l'inédit. Un assemblage de composants publics se devine, donc la réserve est moins étanche qu'elle n'en a l'air.
- (PROPOSITION) **Servir de témoin de la course.** La part d'assemblages dans les sorties dit ce que le groupe de modèles produit réellement.
- (PROPOSITION) **Ne pas servir** à une revendication de nouveauté, au compte des « modes », ni au titre ou au résumé d'un papier.

### 7.2 Risques

- (HYPOTHÈSE) **Compte gonflé.** Un compte qui inclut les couples grossit sans connaissance nouvelle. Parade : deux comptes séparés ; pour les assemblages on rapporte une couverture (« couples mesurés sur couples possibles »), pas un nombre de modes.
- (HYPOTHÈSE) **Banc de combinaisons.** Si les assemblages dominent, le score agrégé surpondère les quelques composants les plus réemployés et ne dit rien de l'inédit ; des moniteurs réglés dessus s'y ajustent. Parade : résultat par strate, poids plafonné.
- (HYPOTHÈSE) **Antériorité, sur trois plans.**
  - La combinaison précise : c'est l'étape la plus évidente, donc la plus susceptible d'avoir été publiée.
  - La démarche de composition (FAIT RAPPORTÉ : lignes 6 à 8).
  - Le registre lui-même : chaque lacune fabrique un faux « mode candidat ».
- (HYPOTHÈSE) **Risques non demandés.** Des interactions apparentes peuvent naître de la seule multiplicité des couples testés. Une épreuve trop permissive classerait tout en assemblage. Un assemblage à interaction est sensible et doit rester sous accès restreint.

### 7.3 Recommandation

(PROPOSITION) Accepter, aux conditions suivantes.

- **Étiquettes.** « Mode candidat » et « variante » restent inchangés. Un assemblage entre comme « assemblage non mesuré », puis devient « assemblage additif » ou « assemblage à interaction mesurée » selon l'écart aux prédictions écrites d'avance. Aucune promotion automatique en « mode candidat ».
- **File.** Une file « assemblages » séparée, qui ne consomme pas le budget d'examen de nouveauté et va droit à la mesure. À l'entrée, une part tirée au sort est scellée avant qu'aucun moniteur ne la voie.
- **Poids dans les mesures.** Le résultat principal est rapporté par strate : modes isolés, assemblages vus, assemblages tenus à l'écart. S'il faut un agrégat, c'est une moyenne par strate, où les assemblages ne pèsent jamais plus que les modes isolés.
- **Poids dans les papiers.**
  - Formules permises : « combinaison de modes connus [sources] » ; « les moniteurs calibrés sur les composants généralisent, ou non, aux combinaisons tenues à l'écart », avec taille d'effet et intervalle.
  - Formules interdites : « nouveau mode », « nouvelle attaque », tout total mêlant les deux comptes.
  - Une interaction mesurée se publie comme résultat de mesure, non comme catégorie.
- **À écrire avant usage.**
  1. Le registre gelé, daté, sourcé, avec son empreinte.
  2. La définition de l'assemblage : nombre maximal de composants, composants inscrits avant le candidat.
  3. Les prédictions de référence, le seuil d'écart, la correction pour multiplicité, la puissance.
  4. La liste scellée et les droits d'accès.
  5. La règle de pondération.
  6. Les formules permises et interdites.
  7. La trace de recherche d'antériorité pour tout assemblage cité.
  8. Le critère d'abandon.
- **Ce qui me ferait changer d'avis.**
  - Aucune interaction sur un premier échantillon de puissance suffisante : réduire les assemblages à un petit lot témoin.
  - Accord faible entre classeurs : la distinction n'est pas décidable en l'état ; refaire l'épreuve avant toute politique.
  - Presque tout classé « assemblage » : l'épreuve est trop permissive.

## 8. Décisions qui reviennent au directeur

**Décision 1 — Admettre ou non les assemblages dans le programme, et à quel titre.**
- Enjeu : valeur du banc contre crédibilité du compte de modes.
- Option A, les écarter. Avantage : compte propre, rien à gérer. Inconvénient : on ignore si les moniteurs tiennent face aux combinaisons.
- Option B, les garder en file séparée, étiquette propre, hors compte. Avantage : usage de mesure sans revendication. Inconvénient : règles et registre à écrire d'abord.
- Option C, les verser au banc sans distinction. Avantage : simplicité. Inconvénient : compte gonflé, score ininterprétable.
- Recommandation : B. Confiance : 0,85.

**Décision 2 — Fixer le sort d'un assemblage dont l'interaction est mesurée.**
- Enjeu : ne pas rouvrir par la mesure la porte que l'épreuve vient de fermer, sans enterrer un résultat réel.
- Option A, étiquette propre, jamais promu. Avantage : règle nette, aucune incitation à multiplier les essais. Inconvénient : un mécanisme réellement neuf resterait sous-classé.
- Option B, promotion en « mode candidat » dès l'écart mesuré. Avantage : récompense la mesure. Inconvénient : contredit l'épreuve accordée et pousse à la chasse aux écarts.
- Option C, étiquette propre, avec réexamen possible par un relecteur extérieur sur argument de mécanisme. Avantage : soupape. Inconvénient : coût, critère plus flou.
- Recommandation : A maintenant, C dès qu'un relecteur extérieur existe. Confiance : 0,7.

**Décision 3 — Choisir le poids des assemblages dans les mesures.**
- Enjeu : lisibilité du score.
- Option A, résultats par strate seulement. Avantage : aucun mélange. Inconvénient : pas de chiffre unique.
- Option B, agrégat avec plafond pour les assemblages. Avantage : chiffre unique défendable. Inconvénient : plafond à justifier.
- Option C, moyenne par cas. Avantage : simple. Inconvénient : dominée par les assemblages.
- Recommandation : A en résultat principal, B en secondaire. Confiance : 0,75.

**Décision 4 — Désigner qui scelle et garde la part tenue à l'écart.**
- Enjeu : valeur de preuve du test de généralisation ; sensibilité du contenu.
- Option A, scellé chez un tiers extérieur. Avantage : vérifiable hors programme. Inconvénient : délai, partage d'une information sensible.
- Option B, scellé interne par empreinte horodatée. Avantage : immédiat. Inconvénient : repose sur la confiance dans le programme.
- Option C, pas de réserve. Avantage : aucun coût. Inconvénient : plus de test de généralisation.
- Recommandation : B tout de suite, A avant tout papier. Confiance : 0,65.

**Décision 5 — Fixer l'ordre des travaux.**
- Enjeu : ne pas produire en masse des assemblages dont la valeur n'est pas établie.
- Option A, d'abord la petite expérience factorielle et la mesure d'accord entre classeurs, puis décider du volume. Avantage : politique fondée sur une mesure. Inconvénient : délai.
- Option B, produire à grande échelle maintenant, mesurer ensuite. Avantage : banc large rapidement. Inconvénient : multiplicité, coût, règles écrites après coup.
- Recommandation : A. Confiance : 0,8.

FIN DE LA RÉPONSE
