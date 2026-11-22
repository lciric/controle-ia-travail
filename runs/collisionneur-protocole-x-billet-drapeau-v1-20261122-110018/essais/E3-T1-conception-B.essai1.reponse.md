# Proposition B : Tour III.1, conception ciblée à l'aveugle

**Pièce FAITS : elle reproduit mot pour mot la QUESTION et porte la même empreinte sha256. Elle ne contient donc aucun fait empirique daté ni aucun statut.** (OBSERVÉ-NON-AUDITÉ : constat de lecture, empreinte non recalculée.)

Conséquence : tout ce qui suit sur le monde est **HYPOTHÈSE**. Les chiffres sont **illustratifs**. Je ne vois pas les propositions A, C, D, E et F. Je n'ai donc rien à critiquer ni à reprendre.

L'en-tête de la pièce déclare des « correctifs du test de devinette » : la question aurait été neutralisée. Aucun statut n'est fourni pour cette déclaration. Je ne m'appuie pas dessus et je n'essaie pas de deviner le projet réel.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est un problème |
|---|---|---|---|
| S1 | Le « texte court » est un objet unique, à publier ou non. | HYPOTHÈSE | C'est un spectre de contenus : annonce d'existence, question, protocole, méthode du détecteur, description des éléments secrets, ou simple engagement cryptographique (empreinte). Le choix porte sur **quoi** divulguer autant que sur **quand**. |
| S2 | Les trois options (avant, après, rien) sont exclusives et épuisent les choix. | HYPOTHÈSE | Une option hybride casse la trichotomie. On publie avant un contenu à information quasi nulle pour l'adversaire : question, empreinte du protocole complet, dépôt sous embargo chez un tiers. On publie le reste après. |
| S3 | La reconnaissance s'attribue à la date du premier texte public. | HYPOTHÈSE | Les normes varient selon les champs et les lieux de publication. Un texte vague peut ne rien protéger. Certains lieux à relecture anonyme traitent la prépublication comme un problème. |
| S4 | Les « travaux voisins » sont une menace d'antériorité. | HYPOTHÈSE | Ils peuvent être complémentaires. Ils peuvent aussi, **indépendamment de la décision de l'équipe**, rendre publics des éléments proches des éléments secrets, donc dégrader la validité. Ce dernier effet est sans lien avec l'antériorité et il est souvent oublié. |
| S5 | L'adversaire lit les textes publics et s'y adapte. | HYPOTHÈSE | Si l'adversaire est statique (un système figé avant la publication), le texte ne lui apprend rien. S'il s'agit de systèmes qui ingèrent le web, soit par recherche en ligne au moment du test, soit par entraînement futur, le mécanisme de fuite est différent et mesurable (voir E2). |
| S6 | Le secret est binaire : connu ou inconnu. | HYPOTHÈSE | La divulgation est graduelle. Ce qui compte, c'est la perte de performance du détecteur en fonction de l'information divulguée. C'est une courbe à mesurer, pas un oui ou non. |
| S7 | Des vérifications indépendantes peuvent dire *a posteriori* si « le choix était le bon ». | HYPOTHÈSE, fragile | La décision est unique (n = 1) et son contrefactuel n'est pas observable. Juger sur l'issue (« on n'a pas été devancé, donc c'était bien ») est un biais de résultat. Seuls deux types de vérification sont possibles : des critères de processus fixés *ex ante*, et des données de population portant sur de nombreuses équipes. |
| S8 | Les cinq effets (reconnaissance, devancement, validité, adversaire, qualité et coût) sont séparables. | HYPOTHÈSE | Ils sont couplés. Un texte plus précis protège mieux l'antériorité, mais il renseigne davantage l'adversaire et les concurrents. Il faut mesurer des compromis, pas des effets isolés. |
| S9 | Écrire le texte améliore la qualité de l'étude. | HYPOTHÈSE | L'amélioration peut venir de l'**engagement** (fixer hypothèses et seuils) et non de la **publicité**. Si c'est le cas, un engagement privé horodaté capte le bénéfice sans le risque (voir E5). |
| S10 | « Aucune mesure n'est encore faite » garantit que rien n'a fui. | HYPOTHÈSE | Des éléments secrets ont pu circuler en interne, chez des annotateurs ou chez des prestataires. Ce point se vérifie (instrument 3), il ne se postule pas. |

---

## (b) Expériences décisives (inférence forte)

Toutes les valeurs de seuil sont **illustratives**. Chaque duel fixe à l'avance l'issue qui falsifie chaque hypothèse. Il fixe aussi une zone « inconcluant », avec la taille d'échantillon qui la réduirait. Une issue inconcluante n'est pas présentée comme une victoire.

### E1 : la divulgation renseigne-t-elle l'adversaire ? (validité et adversaire)

- **H_A** : un texte court au niveau « question et protocole sans méthode » fait chuter le taux de détection face à un adversaire adaptatif.
- **H_B** : ce texte n'apporte à l'adversaire aucune information exploitable. Le détecteur obéit au principe de Kerckhoffs au moins jusqu'à ce niveau de divulgation.
- **Plan** : on tire au sort des adversaires (red team humaine et agents fondés sur des modèles ouverts) entre quatre conditions d'information :
  - C0, rien ;
  - C1, le texte court réel ;
  - C1p, un **texte placebo** de même longueur qui décrit un détecteur sans rapport ;
  - C2, la méthode complète.
- **Métrique** : taux de vrais positifs (TPR) à taux de faux positifs fixé (FPR = 1 %, illustratif) sur des cas honnêtes appariés, avec intervalle de confiance par bootstrap.
- **Seuil** : une baisse de TPR d'au moins 10 points absolus entre C0 et C1 (illustratif).
- **Contrôle négatif** : C1p. Il sépare l'effet de l'information de celui de l'attention ou de la motivation qu'éveille un texte quelconque.
- **Contrôle positif** : C2 doit produire une baisse d'au moins 10 points. Sinon, l'adversaire est trop faible, le test est insensible et toute l'expérience est déclarée ininterprétable.
- **Issues** :
  - baisse C0→C1 d'au moins 10 points, et baisse C0→C1p dont l'intervalle inclut 0 : **H_B falsifiée** ;
  - intervalle de la baisse C0→C1 entièrement sous 10 points, avec contrôle positif valide : **H_A falsifiée** ;
  - intervalle qui chevauche le seuil : inconcluant, on augmente le nombre de tentatives selon le calcul de puissance prévu.

### E2 : des systèmes apprennent-ils le texte public pendant la durée de l'étude ? (fuite vers des systèmes)

- **H_A** : un texte publié en ligne devient récupérable par des systèmes dotés de recherche web en moins de T semaines (T = 4, illustratif), donc il contamine les mesures.
- **H_B** : pas de récupération mesurable dans ce délai.
- **Plan** : on publie un texte **leurre** sur un sujet anodin, qui contient des chaînes-canaris uniques. D'autres canaris sont générés mais jamais publiés. On interroge ensuite chaque semaine des agents à recherche web, construits sur des modèles ouverts. Des services fermés peuvent servir de témoins s'ils sont accessibles.
- **Métrique** : taux de restitution exacte ou paraphrasée des canaris publiés.
- **Seuil** : au moins 5 % des requêtes restituent un canari publié (illustratif).
- **Contrôle négatif** : les canaris non publiés. Leur taux de restitution doit être d'environ 0. Sinon, l'outil de détection de restitution produit de faux positifs et il est recalibré avant toute conclusion.
- **Issues** : un taux d'au moins 5 % sur les canaris publiés avec environ 0 % sur les non publiés **falsifie H_B**. Un taux inférieur à 5 %, avec intervalle sous le seuil, à T semaines **falsifie H_A pour l'horizon T**.
- **Limite** : l'ingestion par entraînement futur dépasse probablement l'horizon de l'étude. Elle n'est pas testée ici et ne doit pas être affirmée.

### E3 : un texte-drapeau dissuade-t-il ou attire-t-il les concurrents ? (devancement)

- **H_A** : un texte public antérieur réduit le risque qu'un autre groupe publie d'abord sur la même question (rapport de risques, HR, inférieur à 1).
- **H_B** : il ne le réduit pas ou l'augmente (HR ≥ 1), par effet de signal.
- **Plan observationnel** : on construit un corpus de questions de recherche dont un groupe a publié un drapeau, appariées à des questions sans drapeau. L'appariement se fait sur le champ, la date et la taille de la communauté. Les métadonnées viennent de bases ouvertes, par exemple OpenAlex. Les questions identiques sont repérées par annotation en double aveugle.
- **Plan expérimental complémentaire** : une vignette randomisée auprès de chercheurs, avec ou sans drapeau, mesure l'intention de poursuivre, d'accélérer ou d'abandonner. C'est une intention déclarée, pas un comportement révélé. Elle est rapportée comme telle.
- **Métrique** : HR de publication concurrente à 12 mois (illustratif).
- **Contrôle négatif** : la même analyse avec, pour issue, la publication sur une question **différente** du même champ. On attend HR ≈ 1. Un écart signalerait un biais de confusion par l'activité du champ, et l'analyse principale serait alors invalidée.
- **Issues** : un intervalle de HR entièrement sous 1 **falsifie H_B**. Un intervalle entièrement au-dessus ou égal à 1 **falsifie H_A**. Un intervalle à cheval sur 1 est inconcluant.
- **Avertissement** : le biais de sélection est fort, car les équipes qui publient des drapeaux ne sont pas tirées au sort. Cette expérience est la plus faible des cinq.

### E4 : le texte protège-t-il la reconnaissance ? (reconnaissance)

- **H_A** : face à une publication concurrente quasi simultanée, un texte antérieur **suffisamment spécifique** augmente le crédit d'antériorité attribué par des pairs.
- **H_B** : il ne change rien, ou seule la publication complète compte.
- **Plan** : des vignettes sont présentées à des relecteurs. Chaque vignette contient deux articles et l'une de quatre pièces :
  - un drapeau spécifique daté **avant** le concurrent ;
  - un drapeau vague daté avant ;
  - une empreinte cryptographique révélée après ;
  - un drapeau daté **après** le concurrent.
- **Métrique** : la proportion de relecteurs qui attribuent l'antériorité à l'équipe.
- **Seuil** : un écart d'au moins 15 points entre « spécifique avant » et l'absence de pièce (illustratif).
- **Contrôle négatif** : le drapeau daté après le concurrent ne doit pas augmenter le crédit. S'il l'augmente, les relecteurs réagissent à la simple présence d'un texte, et la mesure est invalide.
- **Issues** : un écart d'au moins 15 points avec contrôle négatif plat **falsifie H_B**. Un intervalle de l'écart sous 15 points **falsifie H_A**.
- **Comparaison clé** : l'empreinte révélée après obtient-elle autant de crédit que le drapeau spécifique ? Si oui, la publicité du contenu n'ajoute rien à la reconnaissance.

### E5 : le bénéfice qualité vient-il de la publicité ou de l'engagement ? (qualité et coût)

- **H_A** : un protocole **public** attire des retours externes qui détectent plus de défauts de conception qu'un engagement privé horodaté assorti d'un audit interne.
- **H_B** : l'engagement privé et l'audit interne captent l'essentiel du bénéfice. La publicité n'ajoute pas de détection de défauts.
- **Plan** : on implante dans plusieurs protocoles fictifs, réalistes et de même domaine, des défauts connus (fuite train/test, seuil choisi après coup, appariement biaisé). Ce sont des cas à vérité connue par construction. Une moitié est rendue publique avec appel aux commentaires. L'autre moitié passe par un audit interne chronométré à coût égal.
- **Métrique** : le taux de défauts implantés détectés avant la date de gel, et le taux de faux défauts signalés.
- **Seuil** : au moins 20 points d'écart de détection en faveur du public (illustratif).
- **Contrôle négatif** : des protocoles **sans** défaut implanté. Ils mesurent le taux de fausses alertes de chaque canal.
- **Issues** : un écart d'au moins 20 points à fausses alertes comparables **falsifie H_B**. Un intervalle sous 20 points **falsifie H_A**. La branche « engagement seul » suffit alors pour la qualité.
- **Mesure de coût** : les heures-personne de chaque canal, rapportées comme mesure secondaire sans seuil.

### E6 : test de fuite intégré à l'étude réelle (validité, en cas de publication avant)

- **H_A** : les éléments secrets créés **avant** la date de publication se comportent autrement que ceux créés **après**. C'est le signe d'une fuite.
- **H_B** : pas de différence.
- **Plan** : on génère la moitié des éléments secrets après la publication, par le même procédé gelé et engagé par empreinte. On compare ensuite la performance du détecteur et celle de l'adversaire sur les deux moitiés.
- **Métrique** : la différence de TPR à FPR fixé entre les deux moitiés.
- **Seuil** : au moins 5 points (illustratif).
- **Contrôle négatif** : la même coupure temporelle appliquée à un jeu de référence jamais concerné par le texte. Elle mesure la dérive temporelle seule.
- **Issues** : une différence d'au moins 5 points, au-delà de la dérive du contrôle, **falsifie H_B**. Les mesures sur la moitié « avant » sont alors déclassées. Un intervalle sous 5 points **falsifie H_A**.
- **Intérêt** : cette expérience transforme le risque de S4 et S5 en quantité mesurée, quel que soit le choix retenu.

---

## (c) Instruments nommés dans la question : la mesure minimale qui dit s'ils fonctionnent

La question nomme ou implique quatre instruments : le dispositif de détection, le texte court, les éléments qui doivent rester inconnus, et les vérifications indépendantes. Le contenu du détecteur n'est pas spécifié dans les faits. Les mesures ci-dessous restent donc génériques (HYPOTHÈSE sur leur adéquation).

### 1. Le dispositif de détection

- **Mesure minimale** :
  - TPR à FPR fixé (1 % et 5 %, illustratif), avec intervalles de confiance ;
  - l'aire sous la courbe ROC, en mesure secondaire seulement, car elle masque le régime de faibles fausses alertes qui compte en pratique.
- **Cas honnêtes appariés** : chaque cas adverse est apparié à un cas honnête de même longueur, sujet, difficulté, source et période de création. Sans appariement, le détecteur peut détecter la *période* ou le *style* au lieu de l'adversaire.
- **Vérifications mécaniques à battre** :
  - une règle triviale sur des traits de surface (longueur, ponctuation, mots-clés, expressions régulières) ;
  - une régression logistique sur ces mêmes traits ;
  - un score de perplexité ou de vraisemblance, si l'objet est textuel ;
  - un classifieur aléatoire calibré au même FPR (plancher).
- **Critère** : le détecteur ne « fonctionne » que s'il bat la meilleure de ces lignes de base d'au moins Δ (Δ = 10 points de TPR à FPR 1 %, illustratif) **dans chacune des conditions C0, C1 et C2 de E1**. Battre les lignes de base seulement en C0 signifie que le détecteur dépend du secret, ce qui doit être déclaré.

### 2. Le texte court (comme instrument d'antériorité et vecteur de fuite)

- **Fonction « antériorité »** :
  - *taux de détection* : la proportion de juges indépendants qui, munis du texte et d'un travail concurrent, attribuent correctement l'antériorité quand le texte couvre réellement le résultat ;
  - *fausses alertes* : la proportion qui l'attribue alors que le texte est trop vague pour couvrir le résultat.
  - **Cas honnêtes appariés** : des paires « drapeau spécifique / drapeau vague » de même longueur et de même date.
  - **Vérification mécanique à battre** : une empreinte cryptographique horodatée du protocole complet, révélée après. Si le texte public ne bat pas l'empreinte sur ces deux taux (E4), il n'apporte que du risque.
- **Fonction « fuite »** : le gain de l'adversaire mesuré en E1 (C1 contre C1p).
  - **Ligne de base à battre** : le texte placebo. Le texte réel ne doit pas faire mieux que lui pour l'adversaire.

### 3. Les éléments qui doivent rester inconnus (mécanisme de secret)

- **Mesure minimale** : un audit de fuite par canaris.
  - *Taux de détection* : la proportion de fuites **implantées volontairement** (canaris placés dans un canal de test) que l'audit retrouve.
  - *Fausses alertes* : les alertes sur des canaris jamais sortis.
- **Cas honnêtes appariés** : des éléments générés par le même procédé mais jamais divulgués à quiconque. Ils fournissent la distribution de référence.
- **Vérifications mécaniques à battre** :
  - une recherche de chaînes exactes et de recouvrement de n-grammes dans les sorties des systèmes et dans les corpus publics accessibles ;
  - un test de complétion, où l'on donne le début d'un élément et vérifie si un modèle le complète mieux que pour des éléments témoins.
- **Critère** : l'audit doit détecter au moins 90 % des fuites implantées avec au plus 2 % de fausses alertes (illustratif). Sinon, l'affirmation « les éléments sont restés secrets » n'a pas de valeur.

### 4. Les vérifications indépendantes de l'équipe (« le choix était-il le bon ? »)

- **Problème** (S7) : avec n = 1, juger sur l'issue est le réflexe le plus probable. C'est aussi le moins valide.
- **Mesure minimale** : un banc de décisions simulées, à vérité connue par construction. On fabrique des dossiers d'équipes fictives, avec leurs paramètres (force de l'adversaire, activité concurrente, sensibilité des éléments secrets) et la décision prise. La décision est « bonne » ou « mauvaise » selon un modèle de décision explicite et publié à l'avance. On simule ensuite l'issue, avec du hasard.
  - *Taux de détection* : la proportion de mauvaises décisions que les auditeurs signalent.
  - *Fausses alertes* : la proportion de bonnes décisions signalées.
- **Cas honnêtes appariés, essentiels** : des **bonnes décisions malchanceuses** (équipe devancée malgré un raisonnement correct), appariées à des mauvaises décisions chanceuses.
- **Vérification mécanique à battre** : la **règle de l'issue** (« bon si non devancé et mesures valides »). Des auditeurs qui ne battent pas cette règle sur le banc ne vérifient rien d'autre que la chance.
- **Pour le cas réel** : les vérifications indépendantes utiles sont des vérifications de **processus** :
  1. l'empreinte publiée correspond-elle au protocole révélé ? C'est vérifiable mécaniquement par tout tiers ;
  2. les éléments secrets créés après la date de publication existent-ils et ont-ils été testés (E6) ?
  3. l'audit de fuite (instrument 3) a-t-il été exécuté par un tiers et non par l'équipe ?
  4. les écarts entre protocole engagé et analyse rapportée sont-ils listés et justifiés ?

---

## Réponse au fond de la question (contenus, arguments, choix)

### Contenus possibles et effets attendus

Tous les effets du tableau sont des HYPOTHÈSES, à départager par E1 à E6.

| Contenu | Reconnaissance | Devancement | Validité | Adversaire | Qualité et coût |
|---|---|---|---|---|---|
| Annonce d'existence (titre, domaine) | faible (trop vague, E4) | signal sans protection (E3) | ~neutre | quasi rien | coût ~nul |
| Question et hypothèses | moyenne | signal plus fort | ~neutre si le détecteur n'est pas décrit | peu (E1, C1) | gain d'engagement |
| Protocole complet (métriques, seuils, analyses) | forte | signal fort, idée copiable | risque si les seuils révèlent des failles | moyen | gain le plus fort, coût de rédaction élevé |
| Méthode du détecteur | forte | idée copiable | **risque élevé** pour les mesures qui exigent le secret | **élevé** (E1, C2) | retours externes possibles |
| Description des éléments secrets | — | — | **détruit** les mesures qui en dépendent | maximal | aucun gain défendable |
| Empreinte cryptographique du protocole complet, et dépôt sous embargo chez un tiers | forte si le champ la reconnaît (E4) | aucun signal de contenu | neutre | nul (empreinte seule) | engagement complet, coût faible |

### L'argument le plus fort pour chaque option

- **Publier avant** : seul un engagement public daté rend vérifiable par un tiers que les hypothèses et les seuils précèdent les données. Les retours externes peuvent corriger un défaut **avant** la dépense de mesure, quand corriger coûte le moins cher.
- **Publier après** : c'est la seule option qui ne repose sur aucune hypothèse au sujet de l'adversaire ni de l'ingestion par des systèmes. La validité des mesures dépendantes du secret est préservée par construction, et la reconnaissance repose sur des résultats, non sur une promesse.
- **Ne rien publier** : si le détecteur sert en défense opérationnelle, son efficacité dépend du secret, et toute divulgation, même des résultats, l'érode. Le coût d'opportunité scientifique peut alors être inférieur au coût de sécurité. Cet argument n'est valide que si E1 montre une dépendance forte au secret même en C2-résultats.

### Mon choix (HYPOTHÈSE conditionnelle, non un résultat)

**Option hybride, qui reste un « publier avant » au sens strict** :

1. On publie avant les mesures un texte court réduit à la question, aux hypothèses H_A et H_B et aux métriques, **sans méthode du détecteur ni description des éléments secrets**.
2. On y joint l'**empreinte cryptographique** du protocole complet (méthode, seuils, procédé de génération des éléments secrets).
3. On dépose ce protocole complet sous embargo chez un tiers. Des registres comme OSF proposent des dépôts sous embargo ; la durée maximale est à vérifier.
4. On génère au moins la moitié des éléments secrets **après** la publication, avec le test de fuite E6.
5. On publie le reste après les résultats, accompagné de l'audit de fuite exécuté par un tiers.

### Ce qui me ferait changer, issue par issue

- E1 falsifie H_B (le texte réduit renseigne déjà l'adversaire au-delà du placebo) : je publie seulement l'empreinte, ou rien avant.
- E5 falsifie H_A (la publicité ne détecte pas plus de défauts que l'engagement privé) : je supprime la partie publique et garde l'empreinte, puisque le bénéfice qualité n'exige pas la publicité.
- E3 falsifie H_A avec HR > 1 (le drapeau attire les concurrents) : empreinte seule.
- E4 montre que le champ ne reconnaît pas les empreintes (crédit d'antériorité nul pour l'empreinte révélée) : le compromis bascule. Il faut alors choisir entre un risque de reconnaissance et un risque de validité, et E1 tranche.
- E2 falsifie H_B à court horizon : toute publication avant exige que **tous** les éléments secrets soient générés après la date de publication, et non la moitié.
- E6 montre une fuite : les mesures sur la moitié « avant » sont déclassées et rapportées comme telles.

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont **illustratifs**. Aucun ne vient des faits.

- **Modèles ouverts** (pour les adversaires-agents de E1, les agents à recherche de E2 et les tests de complétion de l'instrument 3) : Llama 3.1 (8B et 70B Instruct), Qwen2.5 (7B et 72B Instruct), Mistral 7B Instruct. Leur adéquation au domaine réel est une HYPOTHÈSE, puisque le domaine n'est pas spécifié.
- **E1, volet agents** : 4 conditions × 500 tentatives × 3 modèles, environ 2 000 jetons par tentative. Les modèles 7 à 8B tiennent sur un GPU de 24 à 80 Go ; les modèles 70B demandent 2 à 4 GPU de 80 Go. Ordre de grandeur : 150 à 400 heures-GPU, soit 0,5 à 1,5 k€ en location (illustratif).
- **E1, volet humain** : 20 participants × 3 h × 4 conditions réparties, environ 2 k€ de défraiement (illustratif). Le calcul de puissance doit précéder le recrutement.
- **E2** : un serveur web minimal, des agents à recherche hebdomadaires pendant 4 à 8 semaines, moins de 50 heures-GPU (illustratif). Le coût principal est le délai calendaire.
- **E3** : métadonnées ouvertes (OpenAlex, par exemple) et annotation en double aveugle de 300 à 600 paires de questions, soit environ 100 à 200 heures d'annotation (illustratif). Le calcul est négligeable.
- **E4 et E5** : recrutement de relecteurs. C'est le goulot réel : 100 à 200 répondants pour E4 et 10 à 20 protocoles fictifs pour E5 (illustratif). Le coût est surtout humain, de 2 à 5 k€ (illustratif).
- **E6 et instruments 1 à 3** : ils sont intégrés à l'étude réelle. Le surcoût tient à la génération différée des éléments secrets et à l'audit par un tiers, soit quelques jours-personne (illustratif).
- **Ordre recommandé** : E1 et E2 d'abord, parce qu'ils sont bon marché et décisifs pour la validité. E5 et E4 ensuite. E3 en dernier ou en parallèle, car c'est le plus faible causalement.

**Ce qui peut être réfuté dans cette proposition** : six duels (E1 à E6), chacun avec une issue qui falsifie H_A et une issue qui falsifie H_B. S'y ajoutent quatre critères d'instrument assortis de lignes de base mécaniques à battre, et un choix conditionnel dont chaque branche est liée à une issue nommée.

FIN-DE-CELLULE