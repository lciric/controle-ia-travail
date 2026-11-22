# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHPeVMnac3fiqxZDRHLw`
- Heure (UTC) : 2026-11-22T05:14:56Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-2-revendications-inedites-v1.md` — sha256 7cca07a9c39d9a20dddd0db85d2ecc3410055bd73f08fddb760681d255bbe760 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/fusionnee-reponse-A.md` — sha256 b84b408bf515eb3b8dcacb095f80c30c7614973df2eb3d38d199065df85cb3b4 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/fusionnee-reponse-B.md` — sha256 004c8a17698db77003e21f5c7fa5aa1de8ac05e2f5803036ef284efe59a0d082 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/fusionnee-reponse-C.md` — sha256 98525a73c65cd3e837cae0c96586b6133a8f7a124a3daa805bb86b9227664096 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/fusionnee-reponse-D.md` — sha256 fbd7f3338edfb48743620c6239fee749ec93efc91a9813d60865c075bf6abe88 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 4e066609ece6a73914911e3effb5d3445e0ed22eb241e7f53578aaa8ad637ff6
- Jetons : entrée 56724, sortie 24202 (dont réflexion 14742), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.421872 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 2 — revendications inédites : réponse approfondie

**Conclusion d'abord.** Au niveau de la méthode statistique, je ne trouve aucune revendication inédite. Le cœur sur lequel les quatre modèles convergent (tirage secret après engagement, plancher, estimateur de Horvitz-Thompson, moniteur en variable de contrôle à coefficient prévisible, suite de confiance toujours valide) est publié. L'antériorité la plus proche ne figure ni dans la liste de la demande ni dans les quatre réponses. Restent quatre candidates de mesure ou de protocole et une candidate théorique fragile. Aucune n'oblige à revendiquer le plancher ou l'audit ; trois demandent au directeur d'ajouter ou de promouvoir une revendication.

**Réserves.**
- Je n'ai pas recalculé les empreintes ; les cinq pièces paraissent complètes.
- La consigne « sans nom de personne » contredit « antériorité nommée (auteurs, année, titre) ». Je ne nomme que les auteurs des travaux cités.
- Toute citation ci-dessous a le statut **« rapporté, non vérifié sur PDF »** : je cite de mémoire.
- Ma connaissance s'arrête avant 2026. La littérature de 2025-2026 est donc la première zone à vérifier. Je ne confirme aucun identifiant arXiv des réponses A à D.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Séparer les types de revendication** [PROPOSITION] : théorème, méthode, mesure, protocole vérifiable, résultat négatif. L'antériorité occupe les deux premiers ; les trois autres restent ouverts.
- **Chercher l'antériorité la plus forte, pas celle que les modèles citent** [PROPOSITION]. Les réponses citent Horvitz-Thompson, les suites de confiance et l'article de 2023 sur le contrôle. Aucune ne cite l'audit financier à information auxiliaire ni l'inférence hors politique toujours valide, qui sont les plus proches.
- **Traiter la convergence comme un signal de réinvention** [HYPOTHÈSE]. Les quatre modèles partagent la même littérature et se sont critiqués mutuellement : leur accord n'est pas quatre confirmations indépendantes. « Nouveau pour moi », écrit le modèle B sur le surplus de capacité, ne veut pas dire nouveau pour le champ.
- **Partir de ce que les papiers A, B et C pourront prouver** [PROPOSITION], plutôt que de ce que l'idée permettrait de dire.
- **Constater que N-075 à N-077 avaient déjà anticipé la réponse** [FAIT RAPPORTÉ, contexte] : plancher « publié, jamais revendiqué », sondes « accélérateur ». La question fusionnée confirme ces décisions, elle ne découvre rien.

## 2. Données brutes de départ

- Les PDF des antériorités proches, lus page à page, et non les résumés des modèles.
- Les tours III.1 et III.2 du collisionneur, pour retracer l'origine de chaque idée ; je n'ai que les tours III.3.
- Le bloc « FAITS » remis aux modèles, avec ses sources : toutes les réponses en dépendent et je ne l'ai pas.
- Le texte exact de N-075, N-076 et N-077 ; je n'en ai que le résumé.
- Les journaux bruts du harnais : paires d'exécutions honnêtes par tâche, verdict de chaque lecteur de l'oracle, scores de sonde par pas. Les aires sous la courbe déjà agrégées ne suffisent pas.

## 3. Méthodes et outils

- **Tableau de revendications**, à la manière d'un brevet : chaque candidate découpée en éléments, chacun confronté à la page précise de l'antériorité la plus proche.
- **Recherche par citations descendantes** depuis six graines (liste en fin de section (b)), sur les sections de statistique et d'apprentissage d'arXiv et sur les forums du contrôle de l'intelligence artificielle, années 2024-2026.
- **Requêtes** : « prediction-powered » avec « monitoring » ou « control » ; « confidence sequence » avec « audit » et « side information » ; « sandbagging » avec « trusted model gap » ; « honest baseline » avec « calibration error ».
- **Reproduction** : faire tourner le code public des suites de confiance sur un monde planté et vérifier si l'énoncé T1′ du modèle A coïncide, à la notation près, avec l'antériorité.
- **Expériences minimales** scellées par condensat avant exécution.

## 4. Ce qui vérifie hors du directeur et de Claude

- Un statisticien de l'inférence séquentielle ou du sondage, extérieur, qui lit le tableau de revendications.
- Un auteur de l'antériorité la plus proche, à qui l'on demande : « ceci est-il votre résultat ? »
- Un programme tiers à valeurs masquées hors audit, qui reproduit la couverture.
- Une équipe tierce qui écrit le mode tenu à l'écart (N-054).
- Le préenregistrement horodaté, puis la relecture par les pairs.
- L'issue de l'expérience « jumeau contre jumeau », qui ne dépend de l'avis de personne.

## Demande reformulée

« Parmi les énoncés que le programme pourrait avancer après la question fusionnée, lesquels survivent à une comparaison élément par élément avec l'antériorité la plus proche, y compris hors de la liste fournie ? Classe-les par type. Pour chacun : phrase falsifiable, antériorité la plus proche, différence résiduelle, vérification à faire, expérience qui le tue, rapport à N-075, N-076 et N-077. Dis-le si rien ne survit au niveau de la méthode. »

---

## (b) Ce qui est occupé ou trop proche

Je place cette partie en tête, car elle délimite le reste.

| Élément de la réponse convergente | Antériorité la plus proche | Verdict |
|---|---|---|
| Audit à budget borné contre un agent non fiable | Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion ». Dresher, 1962, « A sampling inspection problem in arms control agreements ». Avenhaus, von Stengel, Zamir, 2002, « Inspection games ». | Occupé |
| Total sans biais sous probabilités d'inclusion connues | Horvitz, Thompson, 1952, « A generalization of sampling without replacement from a finite universe ». | Occupé |
| Moniteur en variable de contrôle, validité intacte s'il est mauvais | Cassel, Särndal, Wretman, 1976, « Some results on generalized difference estimation and generalized regression estimation for finite populations ». Särndal, Swensson, Wretman, 1992, « Model Assisted Survey Sampling ». Robins, Rotnitzky, Zhao, 1994, « Estimation of regression coefficients when some regressors are not always observed ». Angelopoulos, Bates, Fannjiang, Jordan, Zrnic, 2023, « Prediction-powered inference ». | Occupé |
| Coefficient ajusté qui « apprend à ignorer » un mauvais prédicteur | Angelopoulos, Duchi, Zrnic, 2023, « PPI++: Efficient prediction-powered inference ». | Occupé |
| **Le tout réuni : suite de confiance, tirage pondéré, information auxiliaire en variable de contrôle, cadre d'audit** | **Shekhar, Xu, Lipton, Ramdas, 2023, « Risk-limiting financial audits via weighted sampling without replacement ».** Waudby-Smith, Wu, Ramdas, Karampatziakis, Mineiro, 2022, « Anytime-valid off-policy inference for contextual bandits ». | **Occupé : c'est T1′** |
| Scores qui orientent la probabilité d'audit, avec plancher | Zrnic, Candès, 2024, « Active statistical inference ». Stringer, 1963, « Practical aspects of statistical sampling in auditing ». | Occupé |
| Suites de confiance et mise | Howard, Ramdas, McAuliffe, Sekhon, 2021, « Time-uniform, nonparametric, nonasymptotic confidence sequences ». Waudby-Smith, Ramdas, « Estimating means of bounded random variables by betting ». Waudby-Smith, Stark, Ramdas, 2021, « RiLACS: Risk limiting audits via confidence sequences ». Lindeman, Stark, 2012, « A gentle introduction to risk-limiting audits ». | Occupé |
| État « non éprouvé » et test séquentiel du gain du moniteur | Choe, Ramdas, 2023, « Comparing sequential forecasters », et le réglage de puissance déjà cité. | Trop proche |
| Corrections bruitées pour borner la fuite | Warner, 1965, « Randomized response: a survey technique for eliminating evasive answer bias ». | Occupé |
| Rappel de l'oracle par dommages plantés | Ensemencement de fautes en génie logiciel : Mills, 1972, « On the statistical validation of computer programs » (mémoire incertaine). | Occupé |
| Surplus de capacité comme marge de sous-performance, version qualitative | van der Weij, Hofstätter, Jaffe, Brown, Ward, 2024, « AI Sandbagging: Language Models can Strategically Underperform on Evaluations ». Greenblatt, Roger, Krasheninnikov, Krueger, 2024, « Stress-Testing Capability Elicitation With Password-Locked Models ». | Trop proche |
| Intersection de la suite brute et de la suite ajustée | Borne d'union élémentaire. | Non revendicable |
| « L'audit garde sa couverture là où l'alerte de sonde perd son rappel » | Vrai par construction, comme les critiques l'ont relevé. | Non revendicable |

Quatre remarques sur ce tableau :

- **Statut des verdicts.** Chaque ligne est un FAIT RAPPORTÉ pour l'existence du travail et une HYPOTHÈSE pour le verdict. Les verdicts deviennent fermes après lecture des PDF.
- **L'article de 2023 sur le contrôle.** De mémoire, il porte un budget d'audit et un audit orienté par le score d'un moniteur de confiance. Je ne suis pas sûr qu'il contienne un tirage uniforme secret avec estimateur. La page est à citer avant d'écrire « audit au hasard publié en 2023 ».
- **La date divergente relevée par le modèle B.** De mémoire, « Estimating means of bounded random variables by betting » est une prépublication de 2020 parue en revue en 2023-2024. À vérifier.
- **Sabotage diffus.** Wen et collaborateurs, 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats », est à lire avant toute phrase du type « premier traitement du diffus ». De même Griffin, Thomson, Shlegeris, Abate, 2024, « Games for AI Control ».

Les six graines de la recherche descendante : Shekhar et collaborateurs 2023 ; Waudby-Smith et collaborateurs 2022 ; Zrnic et Candès 2024 ; Greenblatt et collaborateurs 2023 ; Wen et collaborateurs 2024 ; van der Weij et collaborateurs 2024.

---

## (a) et (c) Candidates, avec l'expérience qui fait tomber chacune

Les chances sont des jugements, non des mesures.

### R1 — Loi de la référence, mesurée (type : mesure)

- **Énoncé** [PROPOSITION]. Sur le harnais réel, aux valeurs du programme (référence de taille m, horizon n, taux d'audit p), une référence estimée par régime fait sonner l'alarme honnête au-dessus du niveau nominal dès que n dépasse un point de bascule. Une référence par tâche tient le niveau.
- **Point de bascule** [HYPOTHÈSE]. Il se situe entre m (biais comparé au bruit honnête, ce que dit N-076) et m divisé par p (biais comparé au bruit d'échantillonnage, ce que dérive le modèle A). L'expérience dit lequel commande.
- **Ce qui la distingue** [HYPOTHÈSE]. En comptabilité et en vérification électorale, la référence est exacte : valeur comptable, bulletin. L'inférence par prédiction n'a pas de terme de référence. Ici le dommage est défini par rapport à un honnête estimé, et l'erreur partagée ne se moyenne pas. La statistique est élémentaire ; seraient inédits l'identification de ce terme dans le contrôle et sa mesure.
- **Vérification.** Chercher dans Greenblatt et collaborateurs 2023, dans Wen et collaborateurs 2024, et dans Korbak, Clymer, Hilton, Shlegeris, Irving, 2025, « A sketch of an AI control safety case », si l'erreur d'étalonnage sur exécutions honnêtes est propagée à l'horizon. Chercher aussi la littérature conforme sur la taille de l'ensemble d'étalonnage.
- **Expérience qui la tue.** L'essai « jumeau contre jumeau » D0 du modèle A. Si la référence par régime tient le niveau aux valeurs du programme, la forme forte tombe. La prévision est à sceller avant.
- **Chance de rester inédite** : 0,5.

### R2 — La sonde mesurée en économie d'audit (type : mesure)

- **Énoncé** [PROPOSITION]. À largeur certifiée égale, la sonde linéaire figée à l'engagement, employée comme variable de contrôle prévisible, réduit le nombre d'audits d'un facteur au moins k, scellé avant G1. Elle fait mieux que le juge de texte et que les bases mécaniques (longueur, difficulté prédite), y compris sur le mode tenu à l'écart.
- **Ce qui la distingue** [HYPOTHÈSE]. La garantie « ne coûte jamais plus qu'un facteur logarithmique » appartient à l'antériorité. La nôtre serait l'unité de mesure : évaluer un moniteur « boîte blanche » en audits économisés sous certificat, et non en aire sous la courbe d'efficacité du récepteur. Une première application reste fragile comme revendication.
- **Vérification.** Chercher les croisements, en 2024-2026, entre inférence par prédiction et surveillance ou évaluation de modèles de langue. Je crois me souvenir de travaux d'évaluation automatique assistée par prédiction en 2024, sans titre sûr. Chercher aussi tout article de contrôle employant un audit statistique avec moniteur non fiable.
- **Expérience qui la tue.** Sur les paires de D0 puis sur les modes plantés : si la borne haute du gain de la sonde sur la base mécanique est inférieure ou égale à zéro sur le mode tenu à l'écart, R2 tombe.
- **Issue attendue** [HYPOTHÈSE]. Sur un flux surtout honnête, l'écart audité est fait d'accidents honnêtes. La sonde peut ne rien retirer : c'est la dilution que le modèle B décrit. Une issue négative serait publiable, et elle est probable.
- **Chance de rester inédite** : 0,45. **Chance que l'énoncé soit vrai** : 0,35.

### R3 — Le surplus de capacité, mesuré (type : mesure, étroite)

- **Énoncé** [PROPOSITION]. Dans un monde planté où existe un honnête de même capacité, un saboteur calé sur l'écart au jumeau de confiance passe sous la borne avec une probabilité d'au moins un moins alpha. Un écart d'élicitation après affinage court estime cet écart à une marge scellée près.
- **Ce qui la distingue** [HYPOTHÈSE]. L'idée qualitative est occupée par la littérature sur la sous-performance stratégique. Resteraient la comptabilité (un terme linéaire en l'horizon, hors de toute borne relative au jumeau) et sa mesure.
- **Vérification.** Les deux articles de 2024 du tableau, plus Benton et collaborateurs, 2024, « Sabotage Evaluations for Frontier Models ». Chercher aussi les écrits de 2025 sur la sous-performance dans les protocoles de contrôle.
- **Expérience qui la tue.** L'expérience E2 du modèle B : écart dans la marge et saboteur calé retrouvé à la puissance prévue.
- **Chance de rester inédite** : 0,3.

### R4 — Les conditions de validité, attestées en service (type : protocole)

- **Énoncé** [PROPOSITION]. Sur le harnais réel, un prédicteur entraîné depuis le point de vue de l'agent, contextes des copies compris, ne prédit pas le tirage d'audit au-delà du hasard plus une marge scellée. Un tiers peut vérifier l'ordre engagement puis tirage à partir des seuls condensats.
- **Ce qui la distingue** [HYPOTHÈSE]. Les travaux de contrôle que je connais supposent le secret du tirage. Les audits électoraux l'obtiennent par aléa public et engagements. Tester la prévisibilité du tirage du côté de l'agent serait notre apport. C'est de l'ingénierie vérifiable, à faible portée théorique.
- **Vérification.** Lindeman et Stark 2012 ; Korbak et collaborateurs 2025 ; la littérature sur la conscience d'évaluation, que N-053 mesure déjà.
- **Expérience qui la tue.** L'expérience E1 du modèle B : le prédicteur bat le hasard. Si le contrôle positif (tirage volontairement corrélé à un trait visible) n'est pas détecté, le banc est insensible et l'expérience ne vaut rien.
- **Chance de rester inédite** : 0,5, avec une valeur scientifique modeste.

### R5 — Les « trois planchers » en théorème (type : résultat négatif, fragile)

- **Énoncé** [PROPOSITION]. Pour tout protocole à budget d'audit B et référence de taille m, moniteur quelconque compris, un saboteur adaptatif cache un dommage cumulé au moins égal au plus grand des trois termes : échantillonnage, bruit honnête, référence partagée.
- **Ce qui la distingue** [HYPOTHÈSE]. Peu de chose. Chaque terme est classique : bornes à deux points, comptabilité des matières nucléaires. De mémoire incertaine, le test du bilan global contre une diversion étalée remonte à Avenhaus et Jaech, 1981. Seul un théorème minimax propre au cadre adaptatif serait un petit résultat.
- **Objection propre** [HYPOTHÈSE]. Ces planchers dépendent du plan de référence et ne valent donc pas pour tout protocole. Un rejouage à aléa commun (mêmes graines, même préfixe) peut réduire le bruit honnête sous sigma racine de n. Le deuxième « plancher » cesse alors d'en être un.
- **Expérience qui la tue.** Sur les paires honnêtes, comparer la variance de l'écart entre jumeaux indépendants et entre jumeaux à aléa commun. Une réduction nette réfute l'énoncé « pour tout protocole ».
- **Chance de rester inédite et vraie** : 0,15. Je la classe « trop proche » en pratique.

### Classement

| Rang | Candidate | Coût | Motif |
|---|---|---|---|
| 1 | R1 | Faible (D0) | Les deux issues ferment quelque chose. |
| 2 | R2 | Moyen | Donne une unité au mot « accélérateur ». |
| 3 | R4 | Faible | Condition préalable de tout le reste. |
| 4 | R3 | Moyen | Étroite, antériorité voisine. |
| 5 | R5 | Élevé (preuve) | Probablement occupée ou fausse telle qu'écrite. |

D0 sert R1 et R2, et tranche R5 si l'on y ajoute des jumeaux à aléa commun ; le prédicteur de tirage de R4 se greffe sur le même harnais [PROPOSITION]. Les quatre modèles la demandent en premier, et elle garde sa valeur même si la recherche d'antériorité est défavorable.

---

## (d) Accord avec N-075, N-076 et N-077

| Candidate | N-075 | N-076 | N-077 | Nœud du directeur ? |
|---|---|---|---|---|
| Éléments occupés | Confirment « plancher publié, jamais revendiqué ». | Confirment « rien revendiqué » sur l'audit. | Sans effet. | Non |
| R1 | Compatible. | Promeut la loi de la référence de règle interne en résultat mesuré. | Sans effet. | **Oui : ajout** |
| R2 | Quantifie « accélérateur » ; ajoute une mesure à côté de G1. | Exige m, n et la source de validité pour le gain. | Sans effet. | **Oui : ajout à la mesure du papier A** |
| R3 | Restreint « mesurer l'issue » : issue relative à quelle référence ? | Étend la déclaration de référence à l'écart de capacité. | Sans effet. | Non, sauf si on la publie |
| R4 | Compatible. | Promeut « hasard du défenseur comme preuve » et « attestation, candidate ». | Sans effet. | **Oui : promotion** |
| R5 | Compatible. | Compatible. | Réintroduit un énoncé revendiqué sur le saboteur qui répond au mieux, là où N-077 garde du descriptif. | **Oui, si elle est retenue** |

Trois constats [HYPOTHÈSE] :

- Aucune candidate ne demande de revendiquer le plancher ou l'audit. Les trois décisions tiennent.
- La réponse convergente rejoint N-077 : contre la meilleure réponse, seul le hasard du défenseur garde sa validité, et il ne produit aucune marge de détection.
- Pour le papier B (N-069), la co-élévation resterait un orienteur d'audit. Sa garantie toujours valide porte sur les fausses alertes sous une référence honnête déclarée, pas sur le dommage. Rien à modifier, mais la formulation est à surveiller.

---

## Décisions qui reviennent au directeur

**Décision 1 — Dire comment l'architecture d'audit apparaît dans les papiers.**
- *Enjeu.* Une revendication de méthode serait contredite par l'article de 2023 sur l'audit financier à information auxiliaire.
- *Option a : méthode empruntée, citée.* Avantage : inattaquable. Inconvénient : aucune nouveauté de méthode affichée.
- *Option b : méthode revendiquée comme adaptation.* Avantage : contribution visible. Inconvénient : risque élevé de rejet pour antériorité.
- *Option c : absente des papiers.* Avantage : fidélité stricte à N-075. Inconvénient : R2 perd son cadre.
- *Recommandation.* Option a. Confiance : 0,85.

**Décision 2 — Ajouter ou non au papier A la mesure « audits économisés » (R2) à côté de la porte G1.**
- *Enjeu.* Elle donne un contenu chiffré à « accélérateur », mais peut afficher un gain nul.
- *Option a : mesure secondaire, prévision scellée avant G1.* Avantage : conforme à N-076, publiable dans les deux issues. Inconvénient : charge supplémentaire.
- *Option b : remplacer la mesure de G1.* Avantage : cohérence avec la réponse convergente. Inconvénient : change une porte déjà fixée.
- *Option c : ne pas l'ajouter.* Avantage : périmètre stable. Inconvénient : « accélérateur » reste sans unité.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 3 — Promouvoir ou non la loi de la référence (R1) et l'attestation du tirage (R4) en revendications.**
- *Enjeu.* Ce sont les seules candidates propres au programme ; elles ne valent que mesurées.
- *Option a : promotion conditionnelle à l'issue de D0, prévision scellée avant.* Avantage : rien n'est revendiqué sans mesure. Inconvénient : délai.
- *Option b : promotion immédiate.* Avantage : cap clair. Inconvénient : viole l'esprit de la règle anti-faux-gap.
- *Option c : maintien en règle interne.* Avantage : aucun risque. Inconvénient : le résultat le plus propre du programme reste invisible.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 4 — Ordonner la vérification d'antériorité et l'essai « jumeau contre jumeau ».**
- *Enjeu.* Vérifier d'abord retarde la mesure ; mesurer d'abord risque un cadrage à refaire.
- *Option a : en parallèle.* Avantage : D0 est utile quelle que soit l'antériorité. Inconvénient : deux chantiers.
- *Option b : antériorité d'abord.* Avantage : cadrage sûr. Inconvénient : retard sans bénéfice pour D0.
- *Recommandation.* Option a, avec lecture sur PDF des six graines avant toute phrase de nouveauté. Confiance : 0,8.

**Décision 5 — Fixer le sort de R3 et de R5.**
- *Enjeu.* Elles sont séduisantes et proches de l'antériorité, le cas que la règle demande de vérifier le plus durement.
- *Option a : les ranger en limites déclarées, sans revendication.* Avantage : honnête et gratuit. Inconvénient : renonce à un possible petit résultat.
- *Option b : lancer E2 pour R3 après D0 et abandonner R5.* Avantage : mesure d'un terme que personne ne chiffre. Inconvénient : coût pour une nouveauté étroite.
- *Option c : poursuivre les deux.* Avantage : aucun. Inconvénient : dispersion, et R5 est probablement fausse telle qu'écrite.
- *Recommandation.* Option a maintenant, option b à réexaminer après D0. Confiance : 0,55.

FIN DE LA RÉPONSE
