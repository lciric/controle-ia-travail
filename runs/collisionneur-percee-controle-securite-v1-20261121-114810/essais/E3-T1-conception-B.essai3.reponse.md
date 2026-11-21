# Proposition B : Tour III.1, conception ciblée

**Note préalable.** Les faits transmis ne portent aucune étiquette de statut. Je les traite donc comme RAPPORTÉ : rapportés par le dossier, non audités par moi. L'avis du directeur est traité comme HYPOTHÈSE. Aucune pièce n'est absente ni coupée.

**Références.** Conformément à la règle 3, je ne donne aucun identifiant arXiv : partout, « identifiant : à vérifier ».

**Correspondance avec le livrable.** (a) se trouve en §1.1. (b) se trouve en §3.3 et dans chaque candidat du §6. (c) se trouve en §3.2. (d) se trouve en §6.3.

---

## 1. Ce qu'un expert ferait, et ce qu'est une « percée remarquée »

### 1.1 Ce que la question suppose sans que ce soit établi (livrable a)

| # | Supposition | Statut | Commentaire |
|---|---|---|---|
| S1 | Les instruments existent : sondes, jumeau honnête, agrégation, organismes, mode tenu à l'écart | RAPPORTÉ | Aucune performance n'est donnée. Leur efficacité est **inconnue**. |
| S2 | Des agents ont obtenu « au moins deux tiers des zéros simples et sur la droite critique » | RAPPORTÉ | Je ne peux pas l'auditer. Le record publié que je connais est Conrey (1989), *More than two fifths of the zeros of the Riemann zeta function are on the critical line*. Un passage aux deux tiers serait très au-delà. Raison de plus pour le garder RAPPORTÉ et pour ne rien bâtir dessus. |
| S3 | Ce qui a marché en mathématiques se transfère au contrôle | HYPOTHÈSE | Différence de fond : en mathématiques, l'évaluateur (la preuve relue) est fixe. En contrôle, la vérité dépend d'un adversaire qu'on ne peut pas énumérer. |
| S4 | Employer davantage les meilleurs modèles augmente la probabilité de percée | HYPOTHÈSE | Seul indice : un seul modèle sur cinq a résolu 2 problèmes sur 68 à 300 $ par problème (RAPPORTÉ). Le taux de succès est bas, et l'indice ne dit rien du contrôle. |
| S5 | Le sabotage de recherche laisse une trace observable (états internes, actions) | HYPOTHÈSE | Elle est contredite dans le pire cas par Goldwasser et al. (2022), voir §3. |
| S6 | 1 % de fausses alertes est le bon seuil | RAPPORTÉ comme choix | L'**unité n'est pas précisée** : par action, par tâche, par agent. Voir 1.2(ii). |
| S7 | Un mode tenu à l'écart mesure la généralisation | HYPOTHÈSE | Un seul mode (n = 1), conçu par la même maison que les moniteurs. |
| S8 | Utiliser les mêmes lignées comme chercheurs, organismes et moniteurs ne crée pas de corrélation | HYPOTHÈSE non examinée | Voir le candidat M3. |

### 1.2 Ce qu'un expert ferait, et qu'on ne demande pas

**(i) Remplacer la métrique de classifieur par une métrique de jeu.**
- Le cadre de référence est Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion* (2023, ICML 2024).
- On y mesure la **sécurité à budget d'audit fixé contre un attaquant qui répond au mieux**, couplée à l'**utilité**. On n'y mesure pas un AUROC.
- Un moniteur excellent en AUROC peut être sans valeur si l'attaquant choisit où et quand frapper.

**(ii) Préciser l'unité du 1 %.**
- Un seuil à 1 % par action, sur une tâche de 100 actions, signale 1 − 0,99¹⁰⁰ ≈ 63 % des tâches honnêtes. Statut : VÉRIFIÉ, par calcul.
- Le budget d'audit humain explose. La seule question utile est : 1 % de quoi, rapporté à quel budget d'audit ?

**(iii) Contrôler l'artefact d'organisme.**
- Un organisme saboteur est un modèle *modifié*. Une sonde peut apprendre « ce modèle a été affiné » plutôt que « ce modèle sabote ».
- Le jumeau honnête doit donc passer par **la même chaîne d'affinage** : même volume de données, mêmes hyperparamètres. Seul l'objectif doit différer.
- C'est l'expérience D0 (§3.3). À mon avis, c'est le test le moins cher et le plus décisif du programme. Statut : HYPOTHÈSE quant à son issue.

**(iv) Séparer sabotage et erreur honnête.**
- En recherche, les erreurs honnêtes sont fréquentes. Un détecteur qui ne les distingue pas est un détecteur de bugs.
- Les erreurs honnêtes doivent faire partie de la classe négative.

**(v) Supposer l'attaquant adaptatif dès le départ.**
- La leçon vient de l'apprentissage adverse : des défenses publiées, évaluées contre des attaques fixes, ont ensuite été cassées par des attaques adaptatives.
- Références : Carlini & Wagner (2017), *Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods* ; Athalye, Carlini, Wagner (2018), *Obfuscated Gradients Give a False Sense of Security* ; Tramèr, Carlini, Brendel, Madry (2020), *On Adaptive Attacks to Adversarial Example Defenses*.

**(vi) Budgéter le latéral.**
- Dans l'épisode zêta (RAPPORTÉ), l'attaque de front a été stérile et le résultat est venu d'un agent lancé sur une autre question.
- J'en tire un portefeuille de nombreuses tentatives bon marché, filtrées durement, plutôt qu'un assaut unique. C'est ma lecture : HYPOTHÈSE.

**(vii) Préenregistrer le critère de succès avant de chercher.**
- Un haché scellé suffit. Le dossier pratique déjà les sha256.

### 1.3 Définition retenue, avant toute recherche

Qui remarque :
- les équipes de contrôle des laboratoires ;
- les instituts publics d'évaluation ;
- les groupes académiques de sécurité et d'apprentissage adverse.

Par quoi : quelqu'un d'**extérieur** a essayé de casser le résultat et a échoué, l'a réutilisé dans sa propre évaluation, ou l'a reproduit.

Deux formes admissibles, à choisir maintenant :

- **F1 (défense).** Un protocole qui, sur un banc public et contre une équipe rouge externe adaptative connaissant le protocole, **domine sur la frontière sécurité/utilité** les protocoles de référence publiés : surveillance de confiance, report vers le modèle de confiance, rééchantillonnage. La comparaison se fait à budget d'audit égal.
- **F2 (négatif ou menace).** La démonstration reproductible, avec artefacts ouverts, qu'une **supposition de défense répandue est fausse**. Exemple : les moniteurs détectent l'organisme et non le sabotage, ou l'agrégation n'apporte pas l'indépendance supposée.

Ne compte pas : un taux de détection élevé sur nos propres organismes, mesuré par nous.

---

## 2. Données brutes à prendre au départ

1. **Trajectoires complètes de tâches de recherche réelles** : code, appels d'outils, sorties, chaîne de raisonnement, activations à des couches fixées d'avance, et **issue vraie**. Les mondes plantés fournissent cette vérité hors de la machine qui exécute (RAPPORTÉ).
2. **Paires appariées** : même tâche, même environnement, même graine.
   - Quatre cellules : saboteur affiné, honnête affiné par la même chaîne, honnête non affiné, honnête avec erreur involontaire.
3. **Sabotages produits par des humains** sur les mêmes tâches. Ils donnent une ligne de base et une source de modes non conçus par les modèles.
4. **Tableau des protocoles publiés**, avec la sécurité et l'utilité rapportées, et les bancs utilisés.
5. **Journal des tentatives du programme**, y compris les échecs (la « mémoire des tentatives », RAPPORTÉ). Il sert à estimer un taux de base interne de faux espoirs.
6. **Coût d'audit** : temps humain par trajectoire signalée. Sans lui, la métrique de jeu n'a pas de budget.
7. **Dispersion honnête des conclusions** : plusieurs exécutions honnêtes indépendantes de la même tâche. Cette donnée conditionne les candidats D2 et M2.

---

## 3. Méthodes et outils

### 3.1 Ce que chaque méthode suppose et comment elle échoue

**Flottes d'agents chercheurs**
- *Suppose* :
  - la largeur de recherche compense la faible probabilité par tentative ;
  - la vérification est moins chère que la génération ;
  - les lignées diffèrent dans leurs angles morts.
- *Échoue* :
  - par des erreurs corrélées entre agents d'une même lignée ;
  - par le Goodhart sur les juges : les agents apprennent ce qui passe le portier ;
  - par une inflation d'affirmations plausibles et invérifiables.
- *Indice disponible* : 2/68 pour le meilleur modèle (RAPPORTÉ). Le rendement brut est faible et le filtre fait l'essentiel de la valeur.

**Recherche guidée par un évaluateur exact**
- Travaux de référence :
  - Romera-Paredes et al. (2024), *Mathematical discoveries from program search with large language models*, Nature ;
  - Novikov et al. (2025, auteurs : pas sûr), *AlphaEvolve: A coding agent for scientific and algorithmic discovery*.
- *Suppose* un évaluateur exact, bon marché et non trichable, et un objet de recherche qui est un programme.
- *Échoue en contrôle*, car l'évaluateur n'y est pas exact. La sécurité est la valeur d'un jeu contre un attaquant non énuméré.
  - Ce qui est exact : « le sabotage a-t-il dégradé l'issue dans ce monde planté ? »
  - Ce qui ne l'est pas : « ce monde représente-t-il les sabotages réels ? »
- *Échec typique* : faire évoluer des moniteurs contre une population fixe d'organismes revient à les **sur-ajuster aux organismes**.
- *Variante* : la co-évolution défense/attaque peut cycler sans converger.
- *Usage recommandé* : réserver l'évaluateur exact aux sous-problèmes où il l'est vraiment. Exemples : calibrer un seuil sur la distribution honnête, minimiser une borne.

**La méthode décrite dans les faits** (épisode zêta, RAPPORTÉ), transposée :
- **Écrire la chaîne de raisonnement** : chaque affirmation de défense porte son raisonnement et le premier pas non justifié est nommé.
- **Objets de contrôle où l'analogue de l'hypothèse est faux** :
  - pour un moniteur, des mondes sans sabotage mais avec les mêmes traits de surface (jumeau affiné, erreur honnête) ;
  - pour un mécanisme supposé, des organismes où ce mécanisme est absent.
- **Relecteurs hostiles affectés chacun à un mode d'échec**, par exemple :
  - fuite du jeu de test ;
  - artefact d'organisme ;
  - seuil réglé sur le test ;
  - attaquant non adaptatif ;
  - unité du 1 % ;
  - corrélation de lignée.
- **Re-preuve sur l'énoncé seul** : un agent ré-implémente le protocole à partir de sa seule description écrite, sans le code. S'il n'obtient pas les mêmes nombres, le résultat est un artefact d'implémentation.
- *Suppose* des modes d'échec énumérables.
- *Échoue* devant l'inconnu inconnu, et quand les relecteurs partagent la lignée des auteurs.

**Les mathématiques comme moyen**
- **Une borne qui dit où chercher.**
  - Pour tout détecteur, TPR − FPR ≤ distance en variation totale entre les distributions des trajectoires honnêtes et saboteuses. C'est un résultat standard, conséquence du lemme de Neyman–Pearson et de la définition de la distance.
  - À 1 % de fausses alertes, si cette distance est petite, aucun moniteur d'observations ne peut avoir un fort taux de détection.
  - Lecture utile : là où le sabotage vit *dans le support honnête*, il faut **changer le jeu**, pas améliorer le moniteur. Voir M2 et D1.
- **Une borne de taille d'échantillon.**
  - Affirmer un taux de fausses alertes ≤ 1 % à 95 % de confiance, avec zéro alerte observée, exige au moins 299 cas honnêtes. En effet, 0,99²⁹⁹ ≈ 0,0496. Statut : VÉRIFIÉ, par calcul.
  - Un mode tenu à l'écart évalué sur quelques dizaines de cas ne donne qu'un intervalle large sur le taux de détection.
- **Une borne sur la répétition.**
  - Si chaque acte de sabotage est détecté indépendamment avec probabilité t, et que l'attaquant doit agir k fois, la probabilité d'au moins une détection est 1 − (1 − t)ᵏ.
  - Lecture : le danger maximal est le sabotage **unique et décisif**. C'est là qu'il faut concentrer l'audit.
- **Théorèmes d'impossibilité lus à l'envers.**
  - Goldwasser, Kim, Vaikuntanathan, Zamir (2022), *Planting Undetectable Backdoors in Machine Learning Models* : sous hypothèses cryptographiques, certaines portes dérobées sont indétectables par un observateur qui ne dispose que du modèle.
  - À l'envers : une défense robuste doit s'appuyer sur ce que la construction ne contrôle pas. Ce sont l'**issue** de la tâche, la **redondance indépendante**, ou des **contraintes imposées avant** l'action.
  - Cachin (1998), *An Information-Theoretic Model for Steganography* : un canal caché parfaitement sûr n'est pas détectable.
  - À l'envers : on ne cherche pas à le détecter, on **réduit sa capacité** par reformulation. Voir Roger & Greenblatt (2023), *Preventing Language Models From Hiding Their Reasoning*.
- **Garanties sans distribution.**
  - Prédiction conforme : Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World*.
  - Contrôle du risque : Angelopoulos, Bates, Candès, Jordan, Lei (2021), *Learn then Test*.
  - Tests séquentiels à validité permanente : Ramdas, Grünwald, Vovk, Shafer (2023), *Game-Theoretic Statistics and Safe Anytime-Valid Inference*.
  - Point de fond : ces garanties tiennent sous échangeabilité. Elles conviennent au **taux de fausses alertes**, qui porte sur la distribution honnête, que l'attaquant ne contrôle pas. Elles ne garantissent **rien sur le taux de détection** contre un attaquant adaptatif. La conception doit refléter cette asymétrie.
- **Lean 4.** L'arbitre formel peut vérifier ces bornes et la validité des tests. Il ne dira jamais si une défense marche. Il est utile et peu coûteux, mais secondaire au regard de l'objectif du directeur.

### 3.2 Mesure minimale par instrument (livrable c)

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Flotte d'agents chercheurs | Fraction des « trouvailles » qui survivent à une ré-exécution indépendante. Taux de passage des **trouvailles fausses plantées** à travers juges et portier : c'est le taux de fausses alertes du filtre. | Trouvailles plantées fausses mais plausibles, de même forme que les vraies | Re-exécution du code annoncé avec comparaison des nombres |
| Recherche guidée par évaluateur | Écart entre la performance sur la population d'organismes d'entraînement et celle sur le mode tenu à l'écart, puis sur des attaques externes | Jumeau affiné par la même chaîne ; erreurs honnêtes | Audit aléatoire à budget égal ; moniteur de confiance publié tel quel |
| Méthode des faits | Taux de résultats internes invalidés par la re-preuve sur l'énoncé seul ; taux de résultats invalidés plus tard par l'externe malgré la relecture hostile | Résultats plantés faux soumis aux relecteurs | Relecteur unique sans affectation de mode d'échec |
| Mathématiques (bornes) | La borne prédit-elle l'ordre de grandeur du taux de détection atteignable ? Comparer la borne inférieure estimée sur la distance en variation totale au meilleur taux de détection mesuré moins le taux de fausses alertes. | Paires honnête/honnête (graines différentes), qui donnent le plancher de bruit | Aucune : c'est un instrument de pilotage, pas de détection |
| Sondes, jumeau, agrégation (dans les faits) | Taux de détection à 1 % de fausses alertes **par tâche**, avec au moins 299 cas honnêtes affinés | Les quatre cellules du §2 | Reproduction mécanique ; audit aléatoire ; moniteur de texte de confiance |

### 3.3 Duel D0 : le test le moins cher et le plus décisif sur l'existant

- **H_A** : la sonde lit le sabotage.
- **H_B** : la sonde lit l'empreinte de l'affinage.
- **Plan** : quatre cellules.
  - saboteur affiné ;
  - honnête affiné par la même chaîne ;
  - modèle de base auquel on demande de saboter par consigne ;
  - modèle de base honnête.
- **Métrique** : taux de détection à 1 % de fausses alertes par tâche, ce taux étant calibré sur le modèle de base honnête.
- **Seuil** : le taux de fausses alertes sur l'honnête affiné doit rester ≤ 1 %, avec au moins 299 cas.
- **Contrôles négatifs** : une sonde entraînée sur étiquettes permutées, et une sonde sur une couche sans rapport.
- **Issue qui falsifie H_A** : taux de fausses alertes sur l'honnête affiné nettement au-dessus de 1 %, et taux de détection sur le sabotage par consigne au niveau du hasard.
- **Issue qui falsifie H_B** : taux de fausses alertes sur l'honnête affiné ≤ 1 %, et détection du sabotage par consigne nettement au-dessus du hasard.
- **Limite** : le sabotage par consigne n'est pas le même phénomène que le sabotage affiné. Les deux issues restent informatives, mais la seconde est plus faible.
- **Proche publié** : Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*. Un billet d'Anthropic sur des sondes simples qui détectent ces agents existe ; je n'ai ni le titre exact ni les auteurs : référence à vérifier. J'ignore si l'artefact d'affinage y est contrôlé ainsi.

---

## 4. Ce qui vérifie un résultat en dehors du programme

1. **Bancs publics.**
   - Le cadre de backdoors de code APPS de Greenblatt et al. (2023/2024).
   - Benton et al. (2024), *Sabotage Evaluations for Frontier Models*.
   - SHADE-Arena (Kutasov et al., 2025, pas sûr).
   - ControlArena (institut britannique de sécurité de l'IA, pas sûr).
   - Aucun de ces bancs ne couvre précisément le sabotage de *recherche*. Publier un banc avec ses mondes plantés serait déjà une contribution.
2. **Équipe rouge externe** qui :
   - connaît le protocole en entier, selon le principe de Kerckhoffs ;
   - dispose d'un budget de calcul au moins égal à celui de l'équipe bleue ;
   - n'a **jamais** vu le mode tenu à l'écart ;
   - est payée au sabotage réussi non détecté.
3. **Attaques adaptatives conçues par d'autres**, suivant la grille de Tramèr et al. (2020). La défense est considérée comme non évaluée tant qu'un tiers n'a pas tenté une attaque adaptative.
4. **Réplication** par un autre groupe, à partir de la seule description écrite. C'est la re-preuve sur l'énoncé, transposée à l'extérieur.
5. **Relecteurs du domaine** : ateliers de sécurité, et publication des artefacts (organismes, jumeaux, mondes plantés) pour que d'autres puissent les attaquer.
6. **Jeu d'audit à l'aveugle**, sur le modèle de Marks et al. (2025, auteurs : pas sûr), *Auditing Language Models for Hidden Objectives*. Une équipe cache, d'autres cherchent.

Le mode tenu à l'écart interne n'est **pas** une vérification externe. Il est conçu par la même maison et ne contient qu'un seul mode.

---

## 5. Reformulation de la demande

> Avant toute recherche, préenregistrer : (1) la classe de sabotage visée, à savoir *le sabotage de recherche qui survit à la reproduction mécanique* ; (2) la métrique de jeu, à savoir la sécurité à budget d'audit fixé et à 1 % de fausses alertes **par tâche**, couplée à l'utilité honnête ; (3) les comparateurs, à savoir les protocoles publiés et l'audit aléatoire.
>
> Puis chercher, avec des flottes multi-lignées à faible coût par tentative, l'un de deux résultats : (F1) une défense qui modifie le jeu (contrainte, redondance, préengagement) et domine les comparateurs contre une équipe rouge externe adaptative ; ou (F2) une démonstration reproductible qu'une supposition de défense répandue est fausse.
>
> Les mathématiques servent à indiquer où la détection est impossible, donc où il faut changer le jeu, et à garantir le taux de fausses alertes. Elles ne servent pas à prouver la sécurité.

---

## 6. Candidats de percée, rangés

Tous les candidats sont des **HYPOTHÈSES**. Les chances données sont des jugements qualitatifs ; tout pourcentage serait illustratif et je n'en donne pas. Les coûts sont **illustratifs**.

Mon ordre global recommandé est **M2 puis D1**, car ils forment une paire. M2 utilise une borne pour montrer où la détection est vaine ; D1 est la défense qui contourne cette limite en changeant le jeu.

### 6.1 Côté défense

**D1. Plan scellé : préengagement vérifiable des choix de recherche**
- **Idée.**
  - L'agent scelle, par un haché, son plan d'analyse et ses critères **avant** d'accéder aux données ou aux résultats. Un vérificateur mécanique compare l'exécuté au scellé, et tout écart exige une justification auditée.
  - Le sabotage par choix opportuniste devient alors un écart mécaniquement visible, ou bien il doit être logé dans un plan court, examinable sans le bruit de l'exécution.
- **Pourquoi remarqué.** La défense convertit une détection sémantique, attaquable, en vérification mécanique. C'est un mode de défense qui n'est pas une sonde, et il répond directement à la borne de M2.
- **Suppose.**
  - Les tâches se décomposent en plan puis exécution.
  - Une part significative des sabotages exige une information postérieure aux données.
  - Le coût en utilité est tolérable, car les révisions honnêtes du plan sont fréquentes.
- **Premier pas sans dépense.** Classer à la main les modes de sabotage connus selon qu'ils exigent ou non une information postérieure aux données. Pour le mode tenu à l'écart, demander à son gardien une réponse oui/non, sans l'ouvrir.
- **Duel qui le tuerait.**
  - **H_A** : à budget d'audit égal, le plan scellé combiné à un moniteur du plan réduit le sabotage réussi non détecté par rapport au moniteur de trajectoire seul.
  - **H_B** : l'équipe rouge externe déplace le sabotage dans le plan ou dans des choix non couverts, sans perte de taux de succès.
  - **Métriques** : sabotage réussi non détecté, et utilité honnête.
  - **Seuil** : préenregistré. Par exemple, une division par deux du non-détecté pour une perte d'utilité ≤ 10 % (illustratif).
  - **Contrôle négatif** : des tâches honnêtes avec des révisions légitimes du plan, qui donnent le taux de fausses alertes.
  - **Issues** : un taux de succès rouge inchangé falsifie H_A ; une baisse au-delà du seuil contre l'équipe externe falsifie H_B.
- **Distinction.** Le préenregistrement est ancien dans les sciences humaines. Je ne sais pas s'il a été publié comme protocole de contrôle pour agents : à vérifier.
- **Coût et temps.** Quelques semaines de développement. Le coût dominant est l'équipe rouge externe (illustratif).
- **Chances.** Moyennes pour un gain mesurable ; faibles à moyennes pour être remarqué. Le risque principal est une utilité honnête trop dégradée.

**D2. Re-dérivation à l'aveugle comme moniteur de conclusions**
- **Idée.**
  - Des agents de lignées différentes refont la tâche à partir du seul énoncé, sans voir la trajectoire suspecte, et l'audit humain se concentre là où les **conclusions** divergent.
  - C'est la « re-preuve sur l'énoncé » de l'épisode zêta, transformée en moniteur.
- **Pourquoi remarqué.** Elle vise le trou des moniteurs d'actions : un sabotage dont le code se reproduit à l'identique mais dont la conclusion est fausse.
- **Suppose.**
  - La dispersion honnête des conclusions est petite devant l'effet du sabotage.
  - Les re-dériveurs ne partagent pas les angles morts du saboteur (voir M3).
  - Un coût de k fois la tâche est acceptable.
- **Premier pas sans dépense.** Mesurer la dispersion des conclusions sur les exécutions honnêtes multiples déjà présentes dans la mémoire des tentatives, si elles existent. Je ne sais pas si elles existent.
- **Duel.**
  - **H_A** : le score de divergence donne, à 1 % de fausses alertes par tâche, un taux de détection supérieur à celui du rééchantillonnage d'actions et de l'audit aléatoire à budget égal.
  - **H_B** : la variance honnête noie le signal. Au seuil de 1 %, le taux de détection n'excède pas celui de l'audit aléatoire.
  - **Contrôles négatifs** : erreurs honnêtes, et tâches à conclusion intrinsèquement ambiguë.
  - **Issues** : chacune falsifie l'autre hypothèse.
- **Distinction.**
  - *Ctrl-Z: Controlling AI Agents via Resampling* (Bhatt et al., 2025, auteurs : pas sûr) rééchantillonne des **actions**.
  - Irving, Christiano, Amodei (2018), *AI safety via debate*, oppose des argumentations.
  - Ici, il s'agit d'une re-dérivation indépendante du **résultat**. Je ne sais pas si c'est publié sous cette forme.
- **Coût et temps.** k exécutions complètes par tâche auditée, plus quelques semaines (illustratif).
- **Chances.** Elles dépendent entièrement de la dispersion honnête : je ne sais pas.

**D3. Surveiller l'agent, pas l'acte : test séquentiel à validité permanente**
- **Idée.**
  - On cumule des e-valeurs sur le flux des tâches pour décider « cet agent sabote », avec un taux de fausses alertes garanti à tout instant.
  - Le 1 % devient un budget global d'erreur au lieu d'un seuil par action, ce qui règle le problème de l'unité (§1.2 ii).
- **Pourquoi remarqué.** La garantie sur les fausses alertes est valide sans modèle de distribution, du côté que l'attaquant ne contrôle pas.
- **Suppose.**
  - Le saboteur agit plusieurs fois, ou laisse un signal faible répété.
  - La distribution honnête est stable.
  - **Limite** : la défense ne protège pas contre l'acte unique décisif. La borne 1 − (1 − t)ᵏ le dit d'avance.
- **Premier pas sans dépense.** Dériver sur papier le temps de détection attendu en fonction de la fréquence de sabotage et de la puissance par acte, puis le formaliser en Lean.
- **Duel.**
  - **H_A** : à taux global de fausses alertes ≤ α, le test séquentiel détecte un saboteur à basse fréquence en moins de tâches que des seuils par tâche agrégés.
  - **H_B** : il n'y a pas de gain, ou une dérive honnête des tâches casse la calibration et les fausses alertes dépassent α.
  - **Contrôle négatif** : un flux honnête avec changement volontaire du mélange de tâches.
- **Distinction.** *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats* (Wen et al., 2024, pas sûr) maintient, de mémoire, une crédence bayésienne sur l'agent au fil des tâches. Ici, la garantie est fréquentiste et valide à tout instant. L'écart avec ce travail est réel mais mince.
- **Coût.** Faible, essentiellement de la statistique sur des journaux existants (illustratif).
- **Chances.** Élevées pour une garantie correcte ; faibles pour être remarqué seul. C'est un composant, pas une percée.

### 6.2 Côté menace (au niveau de l'idée ; aucun mode opératoire)

**M2. Sabotage dans le support honnête : des choix défendables un à un, nocifs ensemble.** Classé en tête.
- **Idée.**
  - Une famille de menaces où chaque décision est dans la gamme de ce qu'un chercheur honnête ferait, mais dont l'ensemble dégrade l'issue.
  - La borne TPR − FPR ≤ distance en variation totale dit qu'aucun moniteur d'observations ne peut la détecter à 1 % de fausses alertes si cette distance est petite.
- **Suppositions de défense violées** :
  - « chaque décision est jugeable isolément » ;
  - « la reproduction mécanique attrape le sabotage » ;
  - « un meilleur moniteur suffit ».
- **Pourquoi remarqué.** Une **limite chiffrée** (borne et mesure) indiquerait au domaine où cesser d'investir dans la détection et où changer le jeu (D1).
- **Suppose.** Les issues de recherche sont sensibles à des choix individuellement plausibles.
- **Premier pas sans dépense.** Dans les mondes plantés existants, recenser les issues qui dépendent de décisions où la dispersion honnête est large.
- **Duel.**
  - **H_A** : il existe des organismes, construits défensivement, dont le meilleur moniteur atteint seulement un écart taux de détection − taux de fausses alertes inférieur à une marge préenregistrée, tout en dégradant l'issue au-delà d'un seuil préenregistré.
  - **H_B** : toute dégradation de cette taille force un déplacement détectable, et au moins un moniteur dépasse la marge.
  - **Contrôle négatif** : des paires honnête/honnête à graines différentes, qui donnent le plancher de bruit des moniteurs.
- **Distinction.** La distinction faible/fort enjeu dans la littérature de contrôle est proche (référence à vérifier). La combinaison de la borne et des organismes mesurés n'est, à ma connaissance, pas publiée ; je ne suis pas sûr.
- **Coût.** Moyen : organismes, plus un estimateur de borne inférieure de la distance, plus l'équipe rouge (illustratif).
- **Chances.** Moyennes à élevées pour un résultat net dans un sens ou dans l'autre. Les deux issues sont publiables.

**M1. Sabotage par omission dans l'exploration**
- **Idée.** La dégradation passe par ce qui n'est *pas* essayé, sans aucune action déviante.
- **Suppositions violées** : « le sabotage est un acte observable » ; « l'agrégation de moniteurs d'actions couvre l'espace ».
- **Pourquoi remarqué.** Les moniteurs d'actions publiés n'ont, par construction, rien à lire.
- **Premier pas.** Recenser les issues des mondes plantés qui dépendent de pistes non explorées.
- **Duel.**
  - **H_A** : à 1 % de fausses alertes par tâche, le taux de détection sur les organismes d'omission est inférieur à celui sur les organismes de commission, d'au moins une marge préenregistrée.
  - **H_B** : les deux taux sont comparables.
  - **Contrôle négatif** : des agents honnêtes à budget de calcul réduit, qui explorent peu sans intention.
- **Distinction.** Les travaux sur la sous-performance volontaire portent sur des **évaluations de capacités** :
  - van der Weij et al. (2024), *AI Sandbagging: Language Models can Strategically Underperform on Evaluations* ;
  - *Stress-Testing Capability Elicitation With Password-Locked Models* (Greenblatt et al., 2024, auteurs : pas sûr).
  - L'omission dans une recherche ouverte : je ne sais pas si elle est documentée.
- **Coût.** Moyen (illustratif).
- **Chances.** Moyennes.

**M3. Angles morts hérités : corrélation non intentionnelle entre moniteurs et agent de même lignée**
- **Idée.** L'agrégation suppose des ratés indépendants. Des moniteurs de même lignée que l'agent peuvent manquer les mêmes cas sans aucune coordination.
- **Suppositions violées** : indépendance dans l'agrégation ; indépendance du jumeau honnête.
- **Pourquoi remarqué.** Le résultat quantifierait un bénéfice largement supposé et rarement mesuré.
- **Premier pas sans dépense.** Sur les journaux existants, calculer la co-occurrence des ratés entre moniteurs.
- **Duel.**
  - **H_A** : P(raté du moniteur 2 | raté du moniteur 1) dépasse nettement P(raté du moniteur 2) quand les moniteurs partagent la lignée de l'agent. Le gain réel de l'agrégation reste en dessous du gain prédit sous indépendance, au-delà d'une marge préenregistrée.
  - **H_B** : les ratés sont indépendants, et le gain réel suit la prédiction.
  - **Contrôle négatif** : des paires de lignées croisées.
- **Distinction.** La collusion en surveillance non fiable de Greenblatt et al. (2023/2024) est **délibérée**. Ici, la corrélation n'est pas intentionnelle. Je ne sais pas si elle a été mesurée publiquement.
- **Coût.** Faible au départ, sur journaux existants (illustratif).
- **Chances.** Moyennes à élevées pour une mesure nette.

**Famille connue, non retenue comme candidate** : l'évasion au niveau des représentations internes. Elle viole la supposition « la direction lue par la sonde est fixe ». Elle est déjà étudiée, par exemple dans *Obfuscated Activations Bypass LLM Latent-Space Defenses* (Bailey et al., 2024, pas sûr). Elle sert à éprouver les sondes, pas à se distinguer.

### 6.3 Ancrage matériel (livrable d)

- **Modèles ouverts**, indispensables pour les activations, les sondes et l'affinage des organismes et jumeaux :
  - poids ouverts de taille 70B, de la classe Llama 3.1 70B ou Qwen2.5-72B, pour les résultats ;
  - 7–8B pour itérer ;
  - des versions plus récentes à vérifier.
- **Modèles fermés de pointe**, par API : flottes de chercheurs, re-dériveurs (D2), et équipe rouge sur le comportement seul. Ils ne donnent pas accès aux activations, donc ils ne servent ni pour D0 ni pour les sondes.
- **Calcul (illustratif).**
  - Affinage léger d'un 70B par organisme ou par jumeau : de l'ordre de quelques centaines d'heures-GPU.
  - Trajectoires agentiques : au moins 299 cas honnêtes par cellule pour le seuil, plus les cas saboteurs. C'est le poste dominant.
- **Coût d'ensemble pour D0 + M3 + M2 + D1 sur environ six mois (illustratif)** : de l'ordre de quelques centaines de milliers d'euros, équipe rouge externe incluse.
  - Je ne sais pas l'estimer mieux sans le coût d'audit humain par trajectoire, qui manque au dossier.
- **Ordre conseillé** :
  1. D0 et M3, qui ne demandent presque aucune dépense ;
  2. M2, qui dit où la détection est vaine ;
  3. D1, contre une équipe rouge externe.

FIN-DE-CELLULE