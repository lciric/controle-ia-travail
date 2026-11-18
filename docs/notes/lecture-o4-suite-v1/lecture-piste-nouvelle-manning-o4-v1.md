# Lecture de la piste nouvelle MANNING contre O4 (juge au nul formé des lois connues) — v1

- **Lecteur** : modèle I (lecteur neuf, session du compte organisme). Contre-lecture : modèle J, non faite ici.
- **Heures (date -u)** : début 2026-11-18T03:23:33Z ; fin 2026-11-18T03:31:37Z.
- **Source** : Manning, Zhu, Horton, *Automated Social Science: Language Models as Scientist and Subjects*, arXiv 2404.11794 v2 (tampon arXiv du 25 avril 2024 en marge de la p. 1). PDF : `docs/sources/pdf/lecture-o4-v3/arxiv-2404.11794/2404.11794v2.pdf`, 63 pages (pdfinfo), sha256 `c44f50f3fb217788fe19523e77e0818247405e581531c5ad4956037b7e2f6192`, recalculé, égal à celui de la consigne et du compagnon `.sha256`.
- **Profondeur** : PDF entier, pages 1 à 63 (corps p. 1-30, références p. 31-38, annexes A, B, C p. 39-63). Aucun code (proportion fixée par la consigne).
- **Rejeux** : citations PDF **53 sur 53** ; extraits de code **0 sur 0** (liste vide : pièce sans code lu).
- **Verdict en vigueur sur O4 : occupée en partie — inchangé.** La pièce ne déplace ni (ii) ni (iii). Elle prend (i) et (iv-b), déjà pris ailleurs, avec une date plus ancienne (avril 2024) ; elle est voisine de P et de (iv-a). Conjonction non trouvée dans la pièce.

## 1. Profondeur

- Condition de proportion appliquée d'abord : résumé (p. 1), introduction (p. 2-5) et vue d'ensemble du système (section 2, p. 5-10). La pièce n'est **pas sans rapport** : un modèle de langue y propose des hypothèses causales que le système teste (composante (i)), et la statistique y est calculée par un programme, sans modèle de langue (composante (iv-b)). Lecture donc poursuivie sur le PDF entier.
- Lu en entier, page par page, en mode brut de pdftotext : p. 1-63, y compris les annexes A (mise en œuvre, p. 39-50, qui porte la méthode et l'estimation), B (p. 50-53) et C (figures et tables, p. 54-63, dont les tables A.1 et A.2 et l'invite de la figure A.11).
- Numérotation : page du PDF = numéro imprimé, vérifié de la p. 1 à la p. 63 (chaque page extraite se termine par son numéro). Le texte extrait a 64 segments ; le dernier est vide.
- Code : l'article annonce le code et les données sur le site d'un auteur (p. 1 : « Author’s contact information, code, and data are currently or will be available at http://www.benjaminmanning.io/. »). Non lu, non cherché (aucun accès réseau, proportion).
- Version : seule la v2 est lue ; une version ultérieure ou publiée n'est ni lue ni cherchée.

## 2. Recherche de termes

Deux recherches sur le texte extrait (mode brut), toutes les occurrences inspectées à la main : (a) sous-chaîne après la normalisation du programme de rejeu (seuls les caractères alphanumériques gardés) ; (b) expression régulière à bornes de mots, césures de fin de ligne recollées. Les faux positifs de (a) viennent de la suppression des espaces.

| terme | occurrences réelles | ce qu'elles disent |
|---|---|---|
| `e-value` | 0 | (a) seulement : *possible values*, *private values*, *the value(s)*, *whose value(s)*… collés ; aucune e-valeur |
| `e-process` | 0 | (a) seulement : *the process*, *entire process* collés |
| `anytime` | 0 | (b) a rendu *many times* (p. 18, 27) : faux positif |
| `martingale` | 0 | — |
| `optional stopping` | 0 | les seules règles d'arrêt portent sur la fin des conversations simulées (p. 9, 30, 48-49) |
| `sequential` | 0 | — |
| `likelihood ratio` | 1 (p. 50) | test d'ajustement de modèle offert par la bibliothèque d'estimation, pas une règle de décision |
| `Bayes factor` | 0 | *Bayesian information criterion* (p. 25), critère de recherche de graphes causaux dans la section critique |
| `model averaging` | 0 | — |
| `stacking` | 0 | — |
| `encompass` | 0 | — |
| `spanning` | 0 | — |
| `benchmark` | 0 | — |
| `baseline` | 0 | — |
| `null` | 0 au sens statistique | *nullify* (p. 28) ; champ vide d'une référence (p. 34) |
| `multiple testing` | 0 | aussi 0 pour *multiple comparison(s)*, *multiple hypotheses* |
| `false discovery` | 0 | — |
| `Bonferroni` | 0 | — |
| `Holm` | 0 | — |
| `pre-regist` | 2 (p. 29, 41) | p. 29 : pratique humaine ; p. 41 : questions de mesure écrites avant les simulations, rapprochées d'un préenregistrement |
| `pre-commit` | 0 | (b) a rendu *committed* (p. 13, 55, scénario de fraude fiscale) : faux positif |
| `hash` | 0 | noms propres (*Hashim*, p. 36 ; *Hashimoto*, p. 37) et *has heard* collé (p. 14) |
| `seal` | 0 | titre d'une référence (*Sealed Bid Auctions*, p. 31) ; *these algorithms*, *of course also* collés (p. 25, 45) |
| termes ajoutés : `pre-analysis` | 3 (p. 6 ×2, p. 10) | plan d'analyse fixé par le modèle causal structurel avant l'expérience |
| `pre-specified`, `prespecified` | 2 (p. 3, 28) | idem |
| `ex-ante`, `exante` | 5 (p. 10, 22, 25, 27, 42) | spécification de l'analyse avant l'expérience (p. 10) ; identification causale par plan d'expérience (p. 22, 25) ; information absente du modèle avant simulation (p. 27) ; traitements connus d'avance (p. 42) |
| `novel`, `novelty` | 3 (p. 2 ×2, p. 3) | la nouveauté n'est pas optimisée (p. 3) |
| `theory` | nombreuses (p. 1, 3, 4, 18-20, 22, 27, 61 ; p. 35 : titre de référence) | théorie des enchères comme étalon (section 4 de la pièce) |
| `t-test`, `p-value` | 4 et 2 (p. 58, 59) | test de Student entre prédiction du modèle de langue et estimation de l'expérience |
| `correction`, `posterior`, `timestamp`, `freeze` | 0 | — |

## 3. Lecture par composante

### P — juger une proposition contre ce qui est déjà connu, pas contre aucun effet : **voisin (lointain)**

- Les hypothèses du système sont jugées **contre aucun effet** : significativité des coefficients de chemin du modèle causal linéaire. Exemples : « all three causes had a statistically significant effect on the probability of a deal. » (p. 11) ; « Statistically significant paths are marked in red (α = 0.05). » (p. 24) ; une hypothèse rejetée l'est faute d'effet : « However, the judge’s case count before the hearing—which was hypothesized to matter—did not affect the final bail amount. » (p. 3).
- Le connu intervient de trois façons, **aucune n'étant une règle de jugement des propositions** :
  1. **comme étalon de validité de la simulation** : « These simulation results closely match the theory (Maskin and Riley, 1985) and what has been observed empirically (Athey et al., 2011). » (p. 3) ; « We evaluate the approach by comparing results to a setting where the real-world predictions are well known and test to see if an LLM can be used to generate information that it cannot access through direct elicitation. » (p. 2) ; « In contrast, auction theory is highly accurate in its predictions of the final bid price in the experiment » (p. 19) ; « We also showed that such simulations produce results that are highly consistent with theoretical predictions made by the relevant economic theory. » (p. 27) ;
  2. **comme question de l'apport de l'expérience au-delà de ce que le modèle de langue sait déjà** — c'est la forme la plus proche de P dans la pièce, à dire fort : le connu y est la prédiction directe du modèle de langue, sans expérience. « We provide evidence that the insights from these simulations of social interactions are not available to the LLM purely through direct elicitation. » (p. 1) ; « Could an LLM do a “thought experiment” (i.e., make a prediction based on a prompt) about a proposed in silico experiment and achieve the same insight? » (p. 18). La comparaison est descriptive (erreurs quadratiques moyennes, rapports de grandeur) et comprend un test de Student dont la valeur de référence est la prédiction du modèle de langue : « Column 5 gives the p-value of a two-tailed t-test comparing the predictions to the results » (p. 58). Ce test évalue le modèle de langue et la méthode ; il ne promeut ni ne rejette une hypothèse, et le connu n'est pas une archive de lois ;
  3. **comme comparateur mécanique** : la loi ajustée sur les mêmes données sert de base aux prédictions du modèle de langue : « It is also less accurate than the mechanical predictions made by the fitted SCM using the same procedure » (p. 22, note 16).
- La nouveauté par rapport au connu n'est pas visée : « Though yet to be optimized for novelty, the system formulates and tests multiple falsifiable hypotheses—from which it generates several findings. » (p. 3) ; « None of the findings from the system’s experiments are “counterintuitive,” but it is important to emphasize they were the result of empiricism, not just model introspection. » (p. 3). Un tri par intérêt est seulement envisagé : « In future iterations of the system, a researcher could choose outcomes and causes they are interested in, score hypotheses by interestingness » (p. 40).
- Statut : **voisin (lointain)** plutôt que non trouvé (R4), à cause du point 2 : l'idée qu'un résultat d'expérience simulée vaut par ce qu'il apporte au-delà de la prédiction directe du modèle est publiée ici en avril 2024, sous forme descriptive et appliquée à la méthode, non aux propositions.

### (i) proposeurs modèles de langue : **pris**

- « The first step is to generate hypotheses as SCMs based on the social scenario, the scenario being the only necessary input to the system. » (p. 7), suivi de : « LLM for the relevant agents and then interesting outcomes, their potential causes, and methods to operationalize and measure both. » (p. 8). Résumé : « In each case, causal relationships are both proposed and tested by the system, finding evidence for some and not others. » (p. 1) ; « We present an approach for automatically generating and testing, in silico, social scientific hypotheses. » (p. 1).
- Réserve : dans deux scénarios sur quatre, les hypothèses sont choisies par les auteurs : « For (3) and (4), we demonstrate the system’s ability to accommodate human input at any point by selecting the hypotheses ourselves and editing some of the agents » (p. 3) ; et le passage d'une expérience à la suivante n'est pas automatisé : « Although we have not automated the transition from one experiment to the next, the system can generate new causal variables, induce variations, and run another experiment based on the results of the first. » (p. 10).
- (i) était déjà pris ailleurs (note v3 de priorité haute, section 4) ; la pièce n'ajoute qu'une date plus ancienne et un domaine (sciences sociales simulées).

### (ii) nul = mise en commun ajustée des lois prédictives de l'archive : **voisin (lointain)** ; la composante elle-même **non trouvée**

- Le nul des tests est l'absence d'effet (coefficients nuls, section P). Aucune archive de lois connues, aucune mise en commun, aucun ajustement de lois connues comme nul.
- Le plus proche : une **loi connue unique, non ajustée**, la théorie des enchères, sert d'étalon descriptif aux prédictions du modèle de langue et aux résultats simulés (p. 19-22, citations en P). Le seul moment où la loi connue entre dans un modèle ajusté est un ajout fait après coup par les auteurs : « That improvement is feasible with the system: there exists an SCM perfectly consistent with auction theory. » (p. 22) ; « If allowed to generate and test enough potential causes, our system could have selected this variable as a possible cause by itself. » (p. 22) ; « When we do fit this SCM (see Figure A.9), the coefficient is close to one » (p. 22, note 17). Ce n'est ni un nul ni une archive.

### (iii) e-processus ou statistique à validité à tout instant d'arrêt comme règle de promotion : **non trouvé**

- Tests à taille fixée seulement : valeurs p des chemins (p. 11, 14, 16, 18), test de Student (p. 58-59), et tests d'ajustement offerts par la bibliothèque d'estimation : « It can also provide likelihood ratio, Wald, and Lagrange Multiplier tests to evaluate the model fit and compare path estimates. » (p. 50).
- Aucune occurrence de `e-value`, `e-process`, `anytime`, `martingale`, `optional stopping`, `sequential`, `Bayes factor` (section 2). Les règles d'arrêt décrites portent sur les conversations : « After each agent speaks in a simulation, an external LLM is prompted with the transcript of the conversation and asked if the conversation should continue. » (p. 9).
- Aucun contrôle de multiplicité (section 2), alors que les expériences de suite sont prévues sans borne et filtrées par significativité : « Insignificant exogenous variables from the first experiment can be dropped. » (p. 50) ; « Theoretically, the system can run follow-on experiments ad infinitum » (p. 50) — sans correction ni garantie écrite, et non automatisé (p. 10).

### (iv-a) prédictions engagées (scellées) avant que les données existent : **voisin**

- Ce qui est pris : en simulation, les données n'existent pas avant l'expérience, et le plan d'analyse est fixé avant elles. « Note that an SCM specifies, ex-ante, the exact statistical analyses to be conducted after the experiment—akin to a pre-analysis plan. This step of the system’s process is, therefore, mechanical. » (p. 10) ; « Even though the simulations have yet to be conducted, the system generates survey questions. As with pre-registration, this reduces unneeded degrees of freedom in the data collection process after the experiment. » (p. 41) ; « The system presented in this paper can generate these controlled experimental simulations en masse with prespecified plans for data collection and analysis. » (p. 28).
- Ce qui manque :
  1. **aucune prédiction chiffrée ni signée engagée par le proposeur** : l'hypothèse est une liste de causes potentielles (p. 8, citation en (i)) ; la table des informations engendrées par variable (« Example of the information generated for each variable in an SCM. », p. 63) porte opérationnalisation, type, unités, niveaux, questions de mesure, agrégation, portée, attributs et traitements — aucun signe ni grandeur attendus ;
  2. **aucun scellement** (empreinte, horodatage, dépôt figé : section 2) ; l'export est un enregistrement modifiable : « The system’s entire procedure is exportable as a JSON file with the fitted SCM. » (p. 29) ; « These JSONs can be saved or uploaded at any point in the system’s process. » (p. 29) ; « Researchers can edit the system’s decisions at any step in the process. » (p. 7) ;
  3. **écarts au plan dans l'article même** : interactions estimées après coup (« When we estimated the SCM with interactions, the interaction between the judge’s case count and the defendant’s remorse was nontrivial », p. 14) ; observations retirées après coup (« In 80/343 simulations, the agents made the maximum number of statements (20) allowed by the system before the auction ended. » et « We remove these observations because, without additional information, auction theory does not make predictions about partially completed auctions. », p. 19, note 11) ; modèle refait avec une variable ajoutée après lecture (p. 22, citations en (ii)) ;
  4. **les prédictions chiffrées du modèle de langue** (section 4 de la pièce) sont recueillies une fois, à température 0 (« All predictions are made by the LLM once at temperature 0. », p. 18, note 10), et, selon l'invite, après l'expérience : « I have just run an experiment to estimate the paths in the SCM from the TIKZ diagram below » (p. 62) ; « We prompted the LLM to predict the path estimates and whether they would be statistically significant for the simulated experiments in Section 3. » (p. 21). L'introduction écrit pourtant : « To test this idea, we describe the experiments that will be simulated and ask the LLM to predict the results—both the path estimates and point predictions. » (p. 4). L'ordre temporel du recueil n'est donc pas établi ; dans aucun cas il n'y a engagement scellé, et ces prédictions ne sont pas celles du proposeur au moment de proposer.

### (iv-b) statistique calculée hors des agents : **pris** pour la statistique

- « With a complete dataset and the proposed SCM, the system can estimate the linear SCM without further queries to an LLM. The system uses the R package lavaan to estimate all paths in the model » (p. 50) ; « We refrain from asking the LLM to perform mathematical functions whenever possible, as they often make mistakes. » (p. 42) ; étape dite mécanique (p. 10, citation en (iv-a)).
- Réserves : (1) **les données passent par des modèles de langue** — les issues sont mesurées en interrogeant les agents simulés, puis codées par un modèle de langue : « it queries an LLM with the survey question, the agent’s response, and information about the variable’s type to determine its correct numerical value as a string. » (p. 49) ; (2) **aucune règle de promotion** n'est calculée : la statistique est une estimation, la lecture est faite par les auteurs ; (3) isolement du calcul vis-à-vis des agents non décrit au-delà de ces phrases ; code non lu.

### Conjonction (i)+(ii)+(iii)+(iv-a)+(iv-b) : **non trouvée** dans la pièce, à la profondeur déclarée (PDF entier, sans code).

## 4. Réponses aux questions propres

1. **Prédictions engagées avant l'expérience ? plan préenregistré, scellé ?** Le plan d'analyse et les questions de mesure sont fixés avant les simulations, rapprochés par les auteurs d'un plan d'analyse préalable et d'un préenregistrement (p. 10, 41, 28). Mais l'hypothèse ne porte ni signe ni grandeur ; aucun scellement ni horodatage n'est décrit ; l'export en JSON est modifiable à toute étape (p. 7, 29) ; l'article s'écarte lui-même du plan (p. 14, 19, 22). Les prédictions chiffrées du modèle de langue sont recueillies une fois, l'invite les plaçant après l'expérience (p. 62, 21), l'introduction avant (p. 4) : ordre non établi, aucun engagement scellé. **Réponse : plan fixé d'avance, non scellé ; pas de prédiction chiffrée engagée par le proposeur.**
2. **Statistique calculée par le programme ?** Oui pour l'estimation (bibliothèque d'estimation, sans requête à un modèle de langue, p. 50 ; p. 42 ; p. 10). Les valeurs des issues sont produites par des agents simulés et codées par un modèle de langue (p. 49). Aucune règle de promotion calculée.
3. **Contre le connu ou contre zéro ?** **Contre zéro** pour les hypothèses (p. 3, 11, 24). Le connu (théorie des enchères ; prédiction directe du modèle de langue ; loi ajustée sur les mêmes données) sert d'étalon descriptif à la méthode et au modèle de langue (p. 1, 2, 3, 18, 19, 22, 27, 58), jamais de nul pour promouvoir ou rejeter une hypothèse.
4. **Contrôle de multiplicité ou validité à tout instant d'arrêt ?** **Non trouvé** : zéro occurrence des termes de multiplicité et de validité séquentielle (section 2) ; tests à taille fixée (p. 11, 50, 58) ; expériences de suite prévues sans borne et filtrées par significativité (p. 50), sans correction.

## 5. Table de la pièce

| composante | statut | preuve (pages du PDF) |
|---|---|---|
| **P** | **voisin (lointain)** | hypothèses jugées contre aucun effet (3, 11, 24) ; apport de l'expérience au-delà de la prédiction directe du modèle de langue, descriptif, appliqué à la méthode (1, 18, 58) ; théorie connue comme étalon de validité (2, 3, 19, 27) ; nouveauté non visée (3, 40) |
| **(i)** | **pris** | hypothèses causales proposées par un modèle de langue (1, 7, 8) ; deux scénarios sur quatre choisis par les auteurs (3) ; enchaînement non automatisé (10) |
| **(ii)** | **voisin (lointain)** ; composante non trouvée | une loi connue unique, non ajustée, comme étalon descriptif (19-22) ; ajout après coup d'une variable conforme à la théorie (22) |
| **(iii)** | **non trouvé** | tests à taille fixée (11, 50, 58) ; aucun terme séquentiel ni de multiplicité ; arrêts = fin des conversations (9) ; suites sans borne ni correction (50) |
| **(iv-a)** | **voisin** | plan d'analyse et questions de mesure fixés avant que les données simulées existent (10, 28, 41) ; ni prédiction chiffrée du proposeur (8, 63), ni scellement (7, 29), écarts au plan (14, 19, 22) ; prédictions du modèle de langue sans engagement, ordre non établi (4, 18, 21, 62) |
| **(iv-b)** | **pris** (statistique) | estimation sans requête à un modèle de langue (42, 50, 10) ; données codées par un modèle de langue (49) ; pas de règle de promotion |
| **conjonction** | **non trouvée** | à la profondeur déclarée |

## 6. Nœuds pour Lazar (rien n'est déclaré libre ; verdict en vigueur : occupée en partie)

1. **Ajout de MANNING à la note d'englobement** comme voisin daté d'avril 2024 de (i) et (iv-b) (pris) et de (iv-a) (plan d'analyse fixé avant que les données simulées existent, non scellé, sans prédiction chiffrée du proposeur). Option prudente : l'ajouter ; c'est l'antériorité la plus ancienne lue pour la boucle où un modèle de langue propose et un programme teste, statistique hors du modèle.
2. **Forme voisine de P à nommer** : la pièce publie l'idée de juger ce qu'apporte une expérience au-delà de la prédiction directe du modèle de langue (p. 1, 18), avec un test de Student dont la valeur de référence est cette prédiction (p. 58). Décider si cette forme (le connu = ce que le proposeur prédit sans données) doit être citée à côté de P dans l'énoncé de O4. Option prudente : la citer comme voisine, en précisant qu'elle est descriptive et porte sur la méthode, non sur la promotion des propositions.
3. **Verdict sur O4** : aucun changement proposé ; la pièce ne touche ni le nul formé de l'archive mise en commun, ni l'e-processus. Rien ici ne permet de dire (ii) ou (iii) plus libres qu'avant (R8) : seule une pièce de plus ne les occupe pas.
4. **Références de la pièce à verser et lire** (aucun accès réseau ici ; demande à Lazar) : Mullainathan et Rambachan (2023), décrit par la pièce comme « algorithms to find anomalies in formal theories (Mullainathan and Rambachan, 2023) » (p. 2), titre « From Predictive Algorithms to Automatic Generation of Anomalies » (p. 35, SSRN 4443738) — touche peut-être P (prédiction jugée contre une théorie formelle connue) ; Peterson et al. (2021, Science), « Using large-scale experiments and machine learning to discover theories of human decision-making » (p. 36) — touche peut-être P et (ii) ; Ludwig et Mullainathan (2023), « Machine Learning as a Tool for Hypothesis Generation » (p. 34, NBER 31017), décrit comme « generative adversarial networks to formulate new hypotheses (Ludwig and Mullainathan, 2023) » (p. 2) — touche peut-être (i) au sens large. Ce qui précède est la raison de lire, tirée du seul texte de MANNING ; rien n'est affirmé sur ces pièces (R7). Option prudente : lire Mullainathan et Rambachan avant tout énoncé public sur P.
5. **Version et code de MANNING** : seule la v2 (avril 2024) est lue ; une version ultérieure ou publiée pourrait ajouter un engagement ou une comparaison au connu. Le code (site d'un auteur, p. 1) n'est pas lu. Option prudente : faire vérifier qu'aucune version plus récente n'ajoute de scellement ou de règle de promotion avant de citer la pièce comme voisine seulement de (iv-a).

## 7. Ce qui reste non lu

- Le code et les données de la pièce (annoncés p. 1) ; aucune ligne de code n'est citée.
- Toute version de 2404.11794 autre que la v2, et toute version publiée.
- Les références de la pièce, dont celles qui pourraient toucher la conjonction (nœud 4) : Mullainathan et Rambachan 2023 ; Peterson et al. 2021 ; Ludwig et Mullainathan 2023 ; et, plus loin, Enke et Shubatt 2023, Rosenbusch et al. 2023, Girotra et al. 2023, Almaatouq et al. 2022, Horton 2023, Zheng et al. 2022, Wager et Athey 2018 (nommées p. 2, 28, 39 ; contenu non lu).
- Le fichier `provenance-v1.md` du dossier du PDF n'est pas lu (non nommé par la consigne) ; l'empreinte du PDF est recalculée et conforme.
- Les figures sont lues par leur texte extrait (pdftotext) ; aucune image n'est inspectée.

## 8. Incidents

- Aucun refus de permission, de crochet ou de classifieur.
- Faux positifs de la recherche de termes relevés et écartés (section 2) : *many times* pour `anytime`, *committed* pour `pre-commit`, noms propres pour `hash`, titre de référence et mots collés pour `seal`, *nullify* et champ vide pour `null`, mots collés pour `e-value` et `e-process`.
- Pour m'assurer que les noms de fichiers à créer étaient neufs (R12), j'ai listé le dossier `docs/notes/lecture-o4-suite-v1/` filtré sur le seul mot `manning`, et regardé l'historique et l'état git de mes chemins : aucun antécédent. L'état git du dossier a affiché deux fichiers non suivis d'une autre lecture (`lecture-piste-nouvelle-autodisc-o4-v1-*`), ni lus ni touchés.
- La routine de reprise du dépôt (registres, inventaire des machines, tests) n'est pas exécutée : la consigne de la session interdit `registres/` et toute commande vers les loueurs ; tâche de lecture seule sur processeur.
