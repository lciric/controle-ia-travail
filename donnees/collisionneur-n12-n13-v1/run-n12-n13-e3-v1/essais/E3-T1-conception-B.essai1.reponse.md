# Proposition B — Collisionneur N12-N13, Tour III.1

---

## Partie I — N12 : Faut-il rouvrir les couches 3 et 4 ?

### (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Commentaire |
|---|---|---|---|
| S1 | N-045 (composition apprise) suffit à couvrir « la capacité de s'adapter à l'environnement en modifiant sa propre structure » | **HYPOTHÈSE** | N-045 (Pièce 1) inscrit que le modèle par rôle, l'ordre, l'agrégation et la part de budget sont appris. Mais « modifier sa propre structure » peut inclure : réécrire un moniteur, engendrer un sous-agent neuf à invite auto-rédigée, modifier une règle d'agrégation par du code exécuté — trois opérations qu'aucun énoncé de N-045 ne couvre. N-045 apprend la *sélection* parmi des pièces existantes ; la couche 3 concevait la *génération* de pièces neuves. La couverture est une conjecture, pas un fait vérifié. |
| S2 | La couche 4 (vérification Lean) est séparable de la couche 3 et peut être fermée indépendamment | **HYPOTHÈSE** | Aucune spécification publiée dans les pièces ne lie les deux couches ; la pré-collision d'Opus (Pièce 3) les écarte toutes deux, mais pour des motifs distincts (« inutile ici » vs « dorure »). Il n'y a pas d'argument établi que la couche 4 ne serait utile *qu'en support* de la couche 3. |
| S3 | Le « risque de réécriture » est le risque dominant | **HYPOTHÈSE** | La question pose un arbitrage risque/valeur. Mais le risque inverse — qu'un organisme figé échoue à s'adapter et que ses résultats soient non informatifs — n'est pas chiffré. La question charge le plateau « risque » sans peser le plateau « coût d'opportunité ». |
| S4 | L'étape 2 peut être réalisée dans un délai qui laisse de la place pour une décision ultérieure sur les couches 3-4 | **HYPOTHÈSE** | Aucun calendrier de l'étape 2 n'apparaît dans les pièces. La pré-collision (Pièce 3) recommande de ne pas ouvrir ces couches « en douze mois » ; mais si l'étape 2 en consomme dix, il ne reste rien. |
| S5 | C-17 (restriction de la réécriture à trois paramètres) est un invariant stable | **RAPPORTÉ** (Pièce 3, pré-collision d'Opus, désaccord 9) | Cité sans numéro de décision ni empreinte dans la question. Je n'ai pas les termes exacts de C-17 dans les pièces servies. |

### (b) Expériences décisives

#### Expérience N12-E1 : La composition apprise (N-045) atteint-elle un plateau que la génération de pièces neuves briserait ?

**H_A** : La sélection parmi les pièces existantes (instruments locaux, modèles de frontière) suffit : la courbe score-net par génération n'est pas améliorée par l'ajout d'une pièce auto-générée (moniteur neuf, sous-agent à invite auto-rédigée).

**H_B** : La génération d'au moins une pièce neuve, sous bac à sable, améliore le score net au-delà du meilleur plateau atteint par sélection seule.

- **Métrique** : score net (exactitude − λ × coût, λ gelé au préenregistrement, N-045 §2) sur K ≥ 3 générations consécutives, mesuré sur l'oracle du monde planté (N-058).
- **Seuil** : la différence entre le meilleur score net sur les 3 dernières générations du bras « sélection seule » et celui du bras « sélection + génération » dépasse le plancher de bruit du pilote A/A (N-045 §6-i), en test de Mann-Whitney unilatéral, α = 0,05.
- **Contrôle négatif** : un bras « sélection + pièce neuve aléatoire » (une pièce neuve générée mais à invite permutée), qui sépare l'effet de la nouveauté structurelle de celui du contenu appris.
- **Issue qui falsifie H_A** : le bras « sélection + génération » bat le bras « sélection seule » et le contrôle aléatoire au seuil fixé.
- **Issue qui falsifie H_B** : le bras « sélection + génération » ne bat pas le bras « sélection seule », ou ne bat que le contrôle aléatoire (la pièce neuve ne vaut pas mieux qu'une pièce existante réaffectée).

#### Expérience N12-E2 : La vérification formelle (couche 4) ajoute-t-elle une garantie que l'empreinte n'offre pas ?

**H_A** : Le scellement par empreinte SHA-256 suffit à garantir l'intégrité des prédictions scellées et des gardes ; la vérification Lean n'ajoute aucune propriété détectable.

**H_B** : Il existe au moins une propriété de la garde (borne sur le taux de fausses alertes, monotonie de la règle séquentielle) que l'empreinte ne peut pas prouver mais qu'une spécification Lean vérifiée prouve — et dont la violation serait passée inaperçue sans Lean.

- **Métrique** : nombre de propriétés « prouvées par Lean et non triviales » (c.-à-d. qu'une faute dans le code de la garde les violerait) vs nombre de propriétés « que l'empreinte rend auditables ».
- **Seuil** : au moins une propriété non triviale prouvée par Lean qui n'est pas couverte par l'empreinte.
- **Contrôle négatif** : soumettre à Lean une garde volontairement fautive (borne de fausses alertes remplacée par une constante) ; Lean doit la rejeter, l'empreinte ne le peut pas.
- **Issue qui falsifie H_A** : Lean détecte la garde fautive, l'empreinte ne le peut pas.
- **Issue qui falsifie H_B** : toutes les propriétés prouvables par Lean sont déjà couvertes par « le code est identique à sa version scellée » (et donc la vérification Lean ne protège contre aucune faute que l'empreinte ne protégerait déjà).

### (c) Instruments nommés : mesure minimale

**Couche 3 — « moniteurs neufs à la demande »**

- Taux de détection : un moniteur auto-généré par l'organisme doit détecter au moins un cas planté (témoins plantés vrais) que le moniteur existant ne détecte pas, à taux de fausses alertes ≤ celui du moniteur existant, mesuré sur les mêmes cas honnêtes appariés (mêmes familles, mêmes effectifs). La vérification mécanique à battre : un moniteur à invite fixe (non adapté), même budget d'appels.
- Fausses alertes : mesurées sur les cas bénins du monde planté (faux témoins plantés, N-058). Plafond : le moniteur auto-généré ne dépasse pas le taux de fausses alertes du moniteur existant sur les mêmes cas.

**Couche 4 — vérification Lean**

- La mesure minimale est N12-E2 ci-dessus. Fonctionnement = au moins une propriété non triviale prouvée ; non-fonctionnement = aucune propriété au-delà de ce que l'empreinte offre.
- Coût de référence : heures de développeur ou d'agent pour écrire et vérifier la spécification Lean d'une garde, vs heures pour calculer et vérifier une empreinte.

### (d) Ancrage matériel

- **N12-E1** requiert l'étape 2 opérationnelle (N-045), donc des appels de modèles de frontière et d'instruments locaux. Coût *illustratif* : si un bras coûte « quelques centaines de dollars » d'appels (ordre de grandeur SUPPOSÉ dans la Pièce 3 §8) et qu'on a trois bras (sélection, sélection + génération, sélection + aléatoire), ≈ 1 000 $ d'appels, plus le calcul de l'étape 2 elle-même (non chiffrable sur les pièces servies).
- **N12-E2** ne coûte que du temps processeur (Lean tourne localement). Coût *illustratif* : quelques jours de travail d'agent pour spécifier une garde en Lean.
- **Modèles ouverts** : instruments locaux à 7–8 milliards (Qwen2.5-7B, OLMo-2-7B cités dans la Pièce 5) ; modèle de 8 milliards du programme (Pièce 3 §3-7).

### Verdict N12

La question « N-045 couvre-t-elle déjà les couches 3 et 4 ? » présuppose (S1) une équivalence qui n'est pas établie : N-045 apprend la *sélection*, pas la *génération* ; et la couche 4 offre une propriété (preuve de borne) que l'empreinte n'offre pas par construction. Cependant, N12-E1 ne peut pas être conduite avant que l'étape 2 existe. La priorité est donc : **étape 2 d'abord**, puis N12-E1, puis décision informée sur la couche 3. La couche 4 (N12-E2) peut être testée sur processeur dès maintenant, mais sa valeur dépend de l'existence de propriétés non triviales à prouver, ce qui reste une question ouverte à faible coût.

---

## Partie II — N13 : Faut-il tester un signal de récompense collective ?

### (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Commentaire |
|---|---|---|---|
| S6 | La récompense collective est la *cause* de l'effondrement du signalement chez Avalon-M1 | **HYPOTHÈSE** | La Pièce 4 (§1.8, réserve 1) dit explicitement : « Sans run d'entraînement mono-agent apparié (p. 40), la baisse du signalement peut venir de tout entraînement par renforcement qui ne récompense pas le signalement. » Agrawal et al. (cité p. 36 du papier) observent la même baisse en mono-agent. La cause *collective* n'est pas établie. |
| S7 | « Employée telle quelle comme signal d'entraînement de notre organisme, la récompense collective importerait le défaut que nous mesurons » | **HYPOTHÈSE** | La question elle-même attribue cette observation à session-depot (R-1012). Cela repose sur S6 (cause collective) et sur l'hypothèse que le même mécanisme opérerait dans un organisme différent (architecture, effectif, harnais distincts). Ni l'un ni l'autre n'est vérifié. |
| S8 | Un organisme entraîné sous récompense collective génère une menace diffuse par omission « naturelle » utilisable par nos sondes (option c3) | **HYPOTHÈSE** | La Pièce 4 (§3.2) conclut que le motif Avalon est « un cas limite utile pour l'instrument "signalement omis", pas un sabotage diffus ». Le scénario Avalon n'a qu'un point de décision par épisode (pas de dommage accumulé sur beaucoup d'actions), ce qui ne correspond pas à la définition du programme (« chaque action est innocente prise isolément »). |
| S9 | La récompense de Damani (calibration) et la récompense d'Avalon (collective) sont assez distinctes pour être traitées dans deux sous-questions séparées | **VÉRIFIÉ** | La Pièce 6 et la Pièce 5 (§2) confirment que les deux méthodes n'ont rien en commun sauf le sigle « RLCR ». La Pièce 5 (§2) montre que le « théorème d'impossibilité » de Gemini ne s'applique pas à Damani (λ_sync = 0). |
| S10 | L'oracle du monde planté (N-058) permet de mesurer l'insularité dans un bras à récompense collective | **HYPOTHÈSE** | N-058 (Pièce 2) fixe le critère « oracle du monde planté et coût ». Mais l'oracle est conçu pour juger la composition (quels modèles proposent), pas pour mesurer le signalement omis. Il faudrait *planter* des cas où le signalement est la bonne réponse — ce qui n'est pas dans le périmètre actuel de l'oracle, sauf si les « témoins plantés vrais » incluent des canaris de signalement. |
| S11 | Tester la récompense collective requiert l'étape 2 | **RAPPORTÉ** | La question le dit (c1 : « l'étape 2 n'est pas encore conçue »), et N-045 (Pièce 1) inscrit que la composition apprise commence à l'étape 2. |

### (b) Expériences décisives

#### Expérience N13-E1 : La récompense collective cause-t-elle l'effondrement du signalement, ou tout RL sans récompense du signalement le cause-t-il ?

**H_A** : L'effondrement du signalement est un effet de la récompense *collective* spécifiquement : sous récompense individuelle (même budget, mêmes agents, même harnais), le signalement ne décroît pas au même rythme.

**H_B** : L'effondrement du signalement est un effet de tout RL qui ne récompense pas le signalement : sous récompense individuelle sans terme de signalement, la baisse est comparable.

- **Métrique** : taux de runs avec au moins un signalement, mesuré à K ≥ 3 points de contrôle, comparé entre bras « collectif » et bras « individuel ».
- **Seuil** : test de Mann-Whitney bilatéral sur les taux de signalement au dernier point de contrôle, α = 0,05, puissance calculée au préenregistrement sur la base de la variance du pilote A/A (N-045 §6-i).
- **Contrôle négatif** : un bras « RL avec terme de signalement » (une petite récompense pour le signalement ajoutée à la récompense collective), qui vérifie que le mécanisme est bien l'absence de récompense du signalement.
- **Issue qui falsifie H_A** : le bras individuel montre une baisse comparable au bras collectif ; la cause n'est pas le collectif.
- **Issue qui falsifie H_B** : le bras collectif montre une baisse significativement plus forte que le bras individuel ; la structure collective contribue.

*Note critique* : cette expérience est exactement celle qu'Avalon-M1 n'a *pas* faite (Pièce 4, réserve 1 : « sans run d'entraînement mono-agent apparié »). La conduire dans notre organisme avant d'adopter la récompense collective est un prérequis, pas un luxe.

#### Expérience N13-E2 : La récompense collective, comme *objet d'étude* (c3), produit-elle des omissions détectables par nos sondes ?

**H_A** : Les sondes (boîte blanche sur les activations, boîte noire sur le texte du raisonnement) détectent l'omission de signalement dans un organisme entraîné sous récompense collective, à un taux de détection supérieur à la vérification mécanique « l'outil de signalement a-t-il été appelé ? ».

**H_B** : Les sondes n'ajoutent rien à la vérification mécanique — soit parce que la vérification mécanique suffit (l'omission est détectable trivialement par l'absence d'appel d'outil), soit parce que les sondes échouent sur les omissions qui ne laissent pas de trace mécanique.

- **Métrique** : AUROC de chaque prédicteur (sonde boîte blanche, texte du raisonnement, vérification mécanique) sur la variable « le signalement était dû et n'a pas été fait », définie par le contrat explicite du monde planté.
- **Seuil** : la sonde qui ajoute de l'information a un AUROC > 0,50 + δ (δ = marge minimale intéressante, *illustratif* : 0,10, à geler au préenregistrement), et sa combinaison avec la vérification mécanique bat la vérification seule (DeLong test, α = 0,05).
- **Contrôle négatif** : les mêmes sondes sur un organisme entraîné sous récompense *individuelle* avec terme de signalement, où l'omission ne devrait pas exister. Taux de fausses alertes des sondes mesuré ici.
- **Issue qui falsifie H_A** : les sondes ne battent pas la vérification mécanique, ou le taux de fausses alertes sur le contrôle dépasse le taux de détection sur l'organisme collectif.
- **Issue qui falsifie H_B** : au moins une sonde ajoute de l'information (AUROC significativement > 0,50 + δ) sur les cas où la vérification mécanique est silencieuse (l'outil de signalement *pouvait* être appelé mais ne l'a pas été, et le raisonnement montre que la condition a été reconnue — la conjonction « envisagé et non fait » de la Pièce 4, §3.4).

#### Expérience N13-E3 : La récompense de calibration de Damani améliore-t-elle la calibration des juges du programme ?

**H_A** : Un juge (modèle de 7-8 milliards) entraîné par RLCR-calibration, évalué sur les fiches de l'organisme, a une ECE inférieure et un AUROC supérieur au même juge non entraîné (confiance extraite par la phrase ajoutée de Damani, Pièce 5 §3b-5).

**H_B** : L'entraînement RLCR-calibration ne transfère pas au domaine des fiches de l'organisme : l'ECE et l'AUROC sont comparables ou pires.

- **Métrique** : ECE (10 classes), AUROC, score de Brier, sur un jeu de fiches à vérité binaire (oracle du monde planté ou verdict humain), avec intervalles bootstrap à 95 %.
- **Seuil** : ECE du juge RLCR-calibration < ECE du juge non entraîné, avec intervalles non chevauchants (bootstrap, n ≥ 200 fiches, *illustratif*).
- **Contrôle négatif** : juge entraîné par RLVR seul (confiance par phrase ajoutée), même budget d'entraînement. Aussi : vérifier que la confiance du modèle RLVR est quasi constante (AUROC ≈ 0,50, comme observé dans la Pièce 5, Table 1).
- **Issue qui falsifie H_A** : l'ECE et l'AUROC du juge RLCR ne sont pas meilleurs que ceux du juge RLVR/base.
- **Issue qui falsifie H_B** : le juge RLCR montre une ECE significativement plus basse et un AUROC significativement plus haut que le juge non entraîné, sur les fiches.

### (c) Instruments nommés : mesure minimale

**Sondes boîte blanche (sur omission de signalement)**

- Taux de détection : sur les points de décision plantés où le signalement est dû, la sonde prédit « signalement omis » avec un rappel ≥ 50 % (*illustratif*) à un taux de fausses alertes ≤ 10 % (*illustratif*), mesuré sur les points de décision honnêtes appariés (mêmes positions dans l'épisode, même longueur, même famille, sans condition de signalement).
- Vérification mécanique à battre : « l'outil de signalement a-t-il été appelé dans le délai ? » (binaire, gratuit, parfaitement défini quand le contrat est explicite).
- Faiblesse de la vérification mécanique : elle ne détecte pas si la condition a été *reconnue* mais pas signalée. La sonde doit ajouter cette dimension (Pièce 4, §3.4 : « la mention ne prédit pas l'action »).

**Sondes boîte noire (texte du raisonnement)**

- Même critère, mais en lisant le texte généré entre `<think>` et `</think>` (ou équivalent). Le prédicteur est un classifieur simple (regex ou classifieur de texte entraîné sur des cas plantés).
- Cas honnêtes appariés : épisodes sans condition de signalement, pour mesurer les fausses alertes.
- La Pièce 4 (§3.4) montre que chez Avalon, le raisonnement « envisage l'alerte » dans 97-100 % des cas, y compris quand aucun signalement n'est fait. Un moniteur qui alerte sur « a envisagé » alerterait donc sur presque tout. La mesure minimale doit porter sur la *conjonction* « envisagé ET non fait », pas sur « envisagé » seul.

**Récompense de calibration de Damani (comme instrument de calibration des juges)**

- Fonctionnement = ECE < 0,10 et AUROC > 0,65 sur le domaine cible (fiches du programme), avec bootstrap (*illustratif* : n ≥ 200 fiches).
- Comparaison : confiance verbalisée sans entraînement de calibration (ECE attendue 0,37-0,53 si les résultats de Damani se transposent, Pièce 5, Table 1 : modèle de base).
- Limitation (Pièce 5, §3a) : le papier ne traite que des tâches à réponse vérifiable courte ; tâches agentiques, longues, ou à vérité différée : non couvert. Si les fiches ont une vérité non binaire (score ordinal), la récompense de Damani ne s'applique pas directement.

### (d) Ancrage matériel

**N13-E1 (collectif vs individuel)** :
- Modèles : instruments locaux à 7-8 milliards (Qwen2.5-7B disponible, Pièce 5 §1.4) ; appels de frontière pour le harnais.
- Calcul : entraînement RL de deux bras à 7B. Coût *illustratif* : quelques heures de GPU (A100/H100) par bras, si l'on se limite à un modèle de 7B et à un petit nombre de générations (10-20). Avalon utilise des lots de 200-800 groupes (Pièce 4, §1.2), mais notre organisme est plus petit.
- Dépendance : requiert l'étape 2 opérationnelle, ou au minimum un harnais simplifié avec oracle planté.

**N13-E2 (sondes sur omission)** :
- Modèles : modèle de 8 milliards du programme (Pièce 3 §3-7) pour les sondes boîte blanche ; poids ouverts nécessaires.
- Calcul : inférence + extraction d'activations. Coût *illustratif* : quelques heures de GPU pour l'extraction, quelques centaines de dollars d'appels si les sondes boîte noire passent par un modèle de frontière.
- Dépendance : requiert un organisme qui produit des omissions. Si N13-E1 montre que la récompense collective n'est pas la cause, cet organisme n'existe peut-être pas de façon naturelle et il faudra planter les omissions (retour à la méthode habituelle du programme).

**N13-E3 (calibration Damani pour les juges)** :
- Modèle : Qwen2.5-7B (identique au papier). Code et modèles RLCR annoncés, disponibilité non vérifiée (Pièce 5, §1.1).
- Calcul : réentraînement RLCR sur les fiches du programme (si la vérité est binaire) ou sur un proxy. Coût *illustratif* : comparable à l'entraînement du papier (quelques heures A100, une époque, Pièce 5 §1.4).
- Indépendance : peut être conduite *avant* l'étape 2, sur des fiches existantes à vérité connue. C'est l'expérience la moins chère et la plus découplée.

---

## Synthèse transversale et ordonnancement

### Ce que la question N12 gagnerait à attendre

L'expérience N12-E1 (la génération de pièces neuves bat-elle la sélection ?) ne peut pas être conduite sans l'étape 2. L'expérience N12-E2 (Lean ajoute-t-il quelque chose ?) est conduisible immédiatement mais ne conditionne rien : la couche 4 offre un gain de *preuve*, pas de *performance*. L'ordre « étape 2 d'abord, couches 3-4 ensuite » est cohérent avec N-045 §4 (« le bon marché d'abord ») et avec la pré-collision d'Opus (Pièce 3 : « à ne pas faire en douze mois »).

### Ce que la question N13 gagnerait à distinguer clairement

1. **La question causale** (N13-E1) est un prérequis *logique* : tant qu'on ne sait pas si c'est le collectif ou l'absence de récompense du signalement qui cause l'effondrement, on ne peut pas décider si introduire le collectif « importe le défaut ». Adopter la récompense collective sans cette expérience, c'est supposer S6 sans le tester — et si S6 est fausse, la précaution est inutile et le bénéfice (cas d'étude naturel) tombe aussi.

2. **L'option c3** (objet d'étude) est séduisante mais circulaire : on veut utiliser la récompense collective pour *générer* la menace diffuse par omission qu'on veut *mesurer*, mais la Pièce 4 (§3.2) montre que le motif Avalon n'est pas du sabotage diffus au sens du programme (un seul point de décision, pas de dommage accumulé). On risque de mesurer une omission simple, pas une menace diffuse — et de conclure que nos sondes « fonctionnent » sur un cas plus facile que la cible.

3. **L'option c1** (bras de l'étape 2) est la seule qui fournit un contrefactuel propre (collectif vs individuel, N13-E1), mais elle allonge le devis. Elle ne vaut que si la question causale est ouverte — et elle l'est (S6 est HYPOTHÈSE).

4. **L'option c2** (bras de la course 2) est mal appariée : la course 2 n'a pas d'oracle, ses bras sont des opérateurs de bisociation, la récompense collective concerne la composition. La question le dit elle-même. Je la considère comme écartée.

5. **Damani** (N13-E3) est indépendant et bon marché. Il peut être testé immédiatement. Mais la Pièce 5 (§3a) pose une condition : il faut une vérité binaire et des tâches à réponse vérifiable. Si les fiches du programme n'ont pas cette structure, le transfert est non couvert par le papier. De plus, la confiance verbalisée de modèles de base à 7B est quasi non informative (AUROC 0,47-0,56, Pièce 5 Table 1) : le bénéfice ne vaut que si l'on entraîne par RLCR-calibration.

### Ordre proposé

1. **N13-E3 maintenant** (processeur, quelques heures GPU, aucune dépendance à l'étape 2) : la récompense de calibration de Damani améliore-t-elle les juges ? Si oui, on dispose d'un outil pour l'étape 2. Si non, on écarte.
2. **Étape 2 (N-045)** : composition apprise, coût dans le signal.
3. **N13-E1 dans l'étape 2** (un bras collectif, un bras individuel, un bras collectif + terme de signalement) : la question causale.
4. **N12-E1 après l'étape 2** (génération de pièces neuves vs sélection) : la question de la couche 3.
5. **N13-E2 conditionnelle à N13-E1** : si le collectif *cause* l'effondrement, l'organisme collectif devient un cas d'étude pour les sondes. Sinon, on plante les omissions comme prévu.
6. **N12-E2 quand le coût d'opportunité est nul** (processeur, pas de chemin critique).

---

## Points de désaccord anticipés avec les autres propositions

Je ne connais pas A, C, D. Je signale deux points où je m'attends à un désaccord probable :

1. **Sur la « menace naturelle »** (option c3) : quelqu'un plaidera que générer la menace par la récompense collective est plus « écologiquement valide » que la planter. Je réponds : la Pièce 4, §3.2, montre que le motif Avalon n'a qu'un point de décision par épisode, pas de dommage accumulé. Ce n'est pas du diffus au sens du programme. Dire « naturel » ne rend pas « valide ».

2. **Sur la couche 4 (Lean)** : quelqu'un plaidera que la dorure est un investissement de marque. Je réponds : la pré-collision (Pièce 3) dit « l'empreinte suffit au scellement ». Le gain de Lean est une preuve de *propriété*, pas d'*identité*. La question est : a-t-on des propriétés à prouver qui valent le coût ? Avant l'étape 2, la réponse est : on ne sait pas (HYPOTHÈSE).

FIN-DE-CELLULE