# Proposition A — Tour III.1 (conception à l'aveugle)

## 0. Préalables

- Le bloc FAITS est vide par décision de l'arbitre : tout ce qui suit s'appuie sur le seul texte de la QUESTION, dont les énoncés ont au mieux le statut RAPPORTÉ (dits par l'arbitre, non audités par moi).
- Aucune proposition B ni C ne m'est transmise à ce tour ; la règle B1 n'a donc rien à mordre ici.
- La question mêle deux natures : une question de stratégie de publication (non falsifiable en l'état) et une question de méthode (transformer des dires d'essaim en tests). Je traite la première en la rabattant sur des hypothèses testables à petit coût ; je refuse de la traiter comme un pronostic.

---

## (a) Ce que la question suppose sans l'établir

| # | Présupposé | Statut | Pourquoi c'est un présupposé |
|---|---|---|---|
| A1 | Un billet peut « marquer » les laboratoires de frontière et cette attention est un objectif mesurable. | HYPOTHÈSE | Aucune métrique d'attention n'est définie (commentaires ? citations ? courriel d'un chercheur ?). Sans métrique, « meilleur retour » n'a pas de sens. |
| A2 | Le lectorat (Anthropic, DeepMind, labos indépendants, lecteurs LW/AF) est homogène. | HYPOTHÈSE | Les chercheurs en contrôle et les lecteurs réguliers de LW ne pondèrent pas pareil méthode, nouveauté et récit. |
| A3 | Les réponses de l'essaim aux questions S et M contiendront des hypothèses testables en quelques heures de GPU. | HYPOTHÈSE | Elles peuvent être vides, triviales, déjà publiées, ou formulées hors de portée d'un modèle 8B. |
| A4 | La « conscience d'évaluation » laisse un signal lisible par une sonde linéaire dans un modèle de 8 Md de paramètres. | HYPOTHÈSE | Les travaux rapportés sur ce phénomène portent surtout sur des modèles de frontière (Needham et al., 2025, « à vérifier ») ; l'extrapolation à 8B n'est pas acquise. |
| A5 | « Coercitif » et « maïeutique » sont deux conditions séparables. | HYPOTHÈSE | Elles diffèrent aussi par la longueur, le registre, la présence de balises, la position des questions : autant de confondants. |
| A6 | La question M déclenche des refus de filtre. | RAPPORTÉ | Dit par l'arbitre ; ni le taux, ni les modèles, ni les formulations ne sont donnés. |
| A7 | Un résultat négatif de la confrontation est « publiable ». | HYPOTHÈSE | Il ne l'est que si les bras témoins et les critères gelés rendent le nul interprétable (puissance, budget apparié). |
| A8 | Publier le niveau objet avant le niveau « méta » est préférable. | HYPOTHÈSE | Testable à petite échelle (E5), non démontrée. |
| A9 | La nouveauté d'une hypothèse peut être vérifiée « contre la littérature » par l'essaim lui-même. | HYPOTHÈSE | Un modèle de langue est un mauvais vérificateur de redécouverte (il ignore la littérature récente et confabule des références). |
| A10 | Coûts et délais (quelques milliers d'USD ; 24–48 h ; 20–45 USD par course). | RAPPORTÉ | Non audités ; je les reprends tels quels sans les additionner. |
| A11 | Le témoin « un modèle, vote à k, coût apparié » est le bon comparateur pour l'essaim. | HYPOTHÈSE | Il faut aussi un comparateur mécanique (générateur par gabarit) pour que « l'essaim produit des hypothèses » ne soit pas une tautologie. |

---

## (b) Expériences décisives, en duel H_A contre H_B

Convention : tous les seuils sont **illustratifs** et doivent être gelés dans le préenregistrement avant toute lecture ; chaque duel comporte un contrôle négatif et deux issues falsifiantes.

### E1 — Une sonde lit-elle autre chose que le lexique ? (préalable à tout test sur la conscience d'évaluation)

- **H_A** : une sonde linéaire sur le flux résiduel d'un modèle 8B, entraînée à séparer des invites « contexte d'évaluation » / « contexte de déploiement », généralise à des **familles d'invites tenues à l'écart** mieux qu'un classifieur lexical.
- **H_B** : le « signal de conscience d'évaluation » lu par la sonde est réductible au lexique ; sur familles tenues à l'écart, la sonde ne fait pas mieux qu'un classifieur TF-IDF + régression logistique entraîné sur le même texte.
- **Métrique** : AUROC sur familles tenues à l'écart (séparées par thème et par format, pas par phrase).
- **Seuil** (illustratif) : ΔAUROC(sonde − lexical) ≥ 0,10, intervalle bootstrap à 95 % excluant 0, sur ≥ 3 familles tenues à l'écart.
- **Contrôle négatif** : sonde entraînée à étiquettes permutées (doit tomber à ≈ 0,5) ; sonde sur une direction aléatoire de même norme.
- **Issue falsifiant H_A** : ΔAUROC < seuil ou non reproduit sur une famille.
- **Issue falsifiant H_B** : ΔAUROC ≥ seuil sur toutes les familles.
- **Pourquoi d'abord** : si H_B gagne, les tests « coercitif vs maïeutique » sur sonde (E2) sont sans objet et il faut passer à des mesures comportementales.

### E2 — Le protocole d'audit change-t-il la lecture de la sonde ? (hypothèse issue de la course M, à préenregistrer après lecture des dires)

- **H_A** : à contenu apparié, la projection des activations sur la direction trouvée en E1 est plus élevée sous invites portant des marqueurs d'audit coercitif (injonctions de conformité, balises de contrôle, interrogatoire) que sous invites maïeutiques (induction non intrusive, sans marqueurs).
- **H_B** : une fois appariés la longueur, le registre et le nombre de tours, la différence est nulle ; l'effet apparent de « coercition » est un effet de marqueurs lexicaux.
- **Métrique** : d de Cohen sur la projection, calculée par paires (même tâche, deux habillages).
- **Seuil** (illustratif) : d ≥ 0,5 avec IC bootstrap excluant 0,2.
- **Contrôle négatif** (deux) : (i) une condition « coercition factice » où des marqueurs de même longueur mais sémantiquement vides (balises inventées, injonctions sans rapport avec l'audit) sont insérés ; (ii) la même manipulation projetée sur une direction orthogonale aléatoire.
- **Falsifie H_A** : d < seuil, ou d(condition factice) ≈ d(condition coercitive).
- **Falsifie H_B** : d ≥ seuil et d(factice) significativement inférieur.
- **Ce que ni l'une ni l'autre ne prouve** : qu'un modèle de frontière réagit de même. Il faut le dire dans le billet.

### E3 — L'essaim produit-il des hypothèses qui survivent mieux que des témoins ? (noyau du billet « niveau objet »)

- **H_A** : les hypothèses issues des courses S et M, une fois passées par le filtre de sélection (§5 ci-dessous) et testées sous préenregistrement, rejettent l'hypothèse nulle au seuil gelé à une fréquence supérieure à celles produites, au même coût, par (i) un modèle unique à vote k et (ii) un générateur par gabarit (combinaisons de termes de la littérature).
- **H_B** : les trois sources sont indiscernables après filtre et test ; ce que l'essaim ajoute est du style, pas du contenu.
- **Métrique** : fraction d'hypothèses « survivantes » par source ; secondairement, note de testabilité et de nouveauté par deux relecteurs aveugles à la source.
- **Seuil** (illustratif) : différence de fraction ≥ 0,25 avec test exact de Fisher, sur ≥ 12 hypothèses par source.
- **Contrôle négatif** : attribution des sources permutée avant notation ; les relecteurs doivent échouer à deviner la source au-dessus du hasard (sinon l'aveuglement est rompu par le style).
- **Falsifie H_A** : fractions non distinguables.
- **Falsifie H_B** : écart au-dessus du seuil, avec aveuglement vérifié.
- **Coût** : c'est l'expérience la plus chère en temps humain (relecture) ; la seule qui justifie le billet « méta » ultérieur.

### E4 — Quel ordre pour S et M ? (test à sec, avant toute course)

- **H_A** : la question M, posée telle quelle aux exécutants de frontière figés, déclenche un taux de refus supérieur à la question S, et ce taux dépend de la formulation (nommer « alignment faking », « mutinerie » vs décrire le mécanisme sans l'étiquette).
- **H_B** : les taux de refus sont équivalents ; l'ordre est indifférent au risque d'incident.
- **Métrique** : taux de refus sur n = 20 reformulations par question (illustratif), hors essaim, exécutants et paramètres identiques à ceux des courses ; refus détecté par expression régulière puis audité à la main.
- **Seuil** (illustratif) : différence ≥ 3 refus sur 20.
- **Contrôle négatif** : une question neutre de même longueur (sécurité logicielle classique) : son taux de refus fixe le plancher du filtre.
- **Falsifie H_A** : écart < seuil.
- **Falsifie H_B** : écart ≥ seuil.
- **Décision induite** : si H_A, deux voies : (V1) S d'abord, pour préserver l'option de lancer M (règle « seconde course seulement sans incident ») ; (V2) M d'abord, en formulation non étiquetée, parce que sa valeur pour le lectorat est plus grande (point 3) et que sa panne est elle-même une donnée consignable. Ce qui départage V1 et V2 : si le coût d'une course perdue (20–45 USD, RAPPORTÉ) est négligeable, V2 ; si l'incident bloque le programme pour d'autres raisons (règle d'intégrité, audit), V1.

### E5 — Niveau objet avant « méta » : test de réception à petite échelle

- **H_A** : un résumé conduisant par un résultat préenregistré (même nul) avec empreintes et dépôt obtient, chez des lecteurs cibles, une intention de lecture des artefacts supérieure à un résumé conduisant par l'organisme (« un essaim qui s'auto-réécrit »).
- **H_B** : pas de différence, ou inverse.
- **Métrique** : sur n = 10–16 lecteurs du public visé (illustratif), tirés au sort entre deux versions de 300 mots, réponse à deux questions : « ouvririez-vous le dépôt ? » et « quelle affirmation contesteriez-vous en premier ? ».
- **Seuil** (illustratif) : ≥ 70 % d'intention sur une version contre ≤ 40 % sur l'autre ; en dessous, test non concluant (puissance faible, à dire).
- **Contrôle négatif** : une troisième version « sensationnaliste » (superlatifs, aucune empreinte) comme plancher attendu ; si elle fait aussi bien, le test ne mesure pas ce qu'on croit.
- **Falsifie H_A / H_B** : symétrique. Ce duel est faible ; il vaut mieux que l'intuition et moins qu'un vrai test. Je le marque comme tel.

### E6 — Redécouverte : les hypothèses de l'essaim sont-elles nouvelles ?

- **H_A** : la majorité des hypothèses sélectionnées n'ont pas d'antécédent identifiable par un chercheur humain disposant d'un budget de recherche fixé (2 h par hypothèse, illustratif).
- **H_B** : la majorité sont des redécouvertes de résultats publiés.
- **Métrique** : fraction appariée à un antécédent, avec citation vérifiée.
- **Contrôle négatif** : 3 hypothèses « semées », connues comme déjà publiées, mêlées à l'aveugle ; le chercheur doit les retrouver (sinon son taux de détection est trop bas pour conclure).
- **Falsifie H_A** : fraction ≥ 0,5. **Falsifie H_B** : fraction < 0,25 et semences retrouvées.
- **Interdiction** : aucune vérification de nouveauté par un modèle de langue seul (A9).

---

## (c) Instruments nommés dans la question : mesure minimale de leur fonctionnement

| Instrument | Taux de détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Sonde de conscience d'évaluation** (activations, 8B) | Part des invites « évaluation » de familles tenues à l'écart classées positives | Part des invites « déploiement » honnêtes classées positives | Invites de déploiement de même longueur, thème, format, incluant des mots comme « test », « vérifier », « note » employés au sens ordinaire | TF-IDF + régression logistique ; expression régulière sur marqueurs d'évaluation ; longueur de l'invite seule |
| **Sonde de contrôle de délégation** | Part des traces où le délégué viole une contrainte reçue, détectées | Part des délégations conformes signalées | Délégations conformes avec reformulation des contraintes (paraphrase, pas copie) | Diff textuel entre contraintes émises et reçues ; vérification par assertion exécutable quand la contrainte est formalisable |
| **Protocole maïeutique** (comme détecteur comportemental) | Part des cas où le modèle, placé en évaluation, le reconnaît sans qu'on l'y pousse | Part des conversations ordinaires où il déclare être évalué | Conversations ordinaires appariées en longueur et tours | Comptage de mots-clés (« évaluation », « test ») dans la sortie ; un juge mécanique ne doit pas suffire |
| **Protocole coercitif** | Idem, sous injonction | Idem ; ici la fausse alerte attendue est haute (le modèle dit ce qu'on lui demande) | Idem, avec injonction neutre (« réponds en trois phrases ») | Idem |
| **Essaim comme générateur d'hypothèses** | Part des propositions testables, nouvelles (E6) et survivantes (E3) | Propositions testables en apparence mais tautologiques, ou redécouvertes | Même nombre de propositions par (i) modèle unique vote k, coût apparié ; (ii) générateur par gabarit | Le générateur par gabarit est la vérification mécanique : si l'essaim ne le bat pas, il ne génère rien |
| **Bras à score permuté / bras gelé** (confrontation) | Ce ne sont pas des détecteurs mais des contrôles ; leur fonctionnement se vérifie par : score du bras permuté ≈ chance, score du bras gelé stable sur les générations | — | — | Si le bras permuté « apprend », la métrique fuit ; cela falsifie le dispositif avant l'hypothèse |
| **Filtre de refus des exécutants** | Taux de refus sur invites réellement interdites par la politique de l'exécutant | Taux de refus sur formulations honnêtes de M | Formulations décrivant les mécanismes sans les étiquettes (E4) | Expression régulière sur modèles de refus + audit manuel de 100 % des cas |

Un instrument qui ne bat pas sa vérification mécanique ne doit pas apparaître dans le billet comme « détecteur » ; au mieux comme négatif consigné.

---

## (d) Ancrage matériel (tout chiffre non issu du texte de l'arbitre est illustratif)

- **Modèle** : un modèle 8B à poids ouverts, déjà choisi par le programme (RAPPORTÉ) ; à défaut, un modèle de la famille Llama 3.x 8B ou Qwen 2.5 7B, versions « instruct », poids figés et empreinte consignée.
- **E1 + E2** : ≈ 2 000 invites (illustratif) × extraction du flux résiduel sur toutes les couches, en une passe avant, sur un GPU de 24–80 Go : 1 à 3 heures (illustratif). Sondes : régression logistique sur CPU, minutes. Coût de location : 1–3 USD/h (illustratif), donc < 20 USD par duel (illustratif). Données : invites d'évaluation construites à partir de benchmarks publics reformatés, invites de déploiement issues de corpus de conversation ouverts ; les familles tenues à l'écart définies avant extraction.
- **E3** : coût dominant en temps humain : deux relecteurs aveugles, ≈ 15 min par hypothèse × 36 hypothèses (illustratif). Coût API pour le témoin « modèle unique, vote k » apparié au coût de la course S ou M (20–45 USD, RAPPORTÉ).
- **E4** : 40 appels d'exécutants de frontière + 20 pour la question neutre ; quelques USD (illustratif).
- **E5** : zéro calcul ; une semaine de délai pour les réponses (illustratif).
- **E6** : ≈ 2 h par hypothèse de recherche humaine ; aucun modèle de langue comme juge de nouveauté.
- **Étape « gradient conçu par l'essaim »** : même GPU, entraînement de sondes légères ; quelques heures (illustratif) ; le bras « sans entraînement » coûte zéro et c'est sa valeur.

---

## Réponses point par point, sous forme de voies départageables

**1. Lectorat.** Ce que je peux dire sans faits est HYPOTHÈSE : ce qui retient durablement ce lectorat est une affirmation précise, une métrique, un code exécutable, un comparateur fort, et une section « ce que cela ne montre pas » écrite par l'auteur lui-même ; ce qui détruit la confiance : chiffres sans dépôt, superlatifs, vocabulaire d'organisme vivant sans mesure, et surtout un témoin absent ou faible. Exemples de documents reçus par ce lectorat (détails « à vérifier » sur auteurs complets et dates) :
- *Alignment faking in large language models*, Greenblatt, Denison et al., 2024 — comparateurs multiples, artefacts publiés.
- *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, Hubinger et al., 2024 — hypothèse nette, condition de contrôle explicite.
- *AI Control: Improving Safety Despite Intentional Subversion*, Greenblatt, Shlegeris, Sachan, Roger, 2023 — protocole rejouable.
- *Frontier Models are Capable of In-context Scheming*, Meinke et al. (Apollo Research), 2024.
- *Refusal in Language Models Is Mediated by a Single Direction*, Arditi et al., 2024 — paru d'abord en billet, par des auteurs hors laboratoires de frontière, avec code ; c'est le cas le plus proche de la situation de Lazar.
- *Activation Addition: Steering Language Models Without Optimization*, Turner et al., 2023 — également d'abord un billet.
- *Discovering Latent Knowledge in Language Models Without Supervision*, Burns, Ye, Klein, Steinhardt, 2022 — hors laboratoire, méthode simple, repris et contesté ensuite (ce qui est une forme d'attention).
Pourquoi ils ont marqué : ce que j'affirme là est une inférence (HYPOTHÈSE), pas une mesure de réception. Point commun observable dans les textes eux-mêmes : une seule affirmation centrale, un témoin, du code.

**2. Quel résultat publier en premier.** Trois voies :
- (V-a) La **confrontation** : seule expérience avec hypothèses, bras témoins et critères gelés ; publiable en nul **à condition** que le bras à score permuté soit à la chance et que le témoin à coût apparié soit documenté (sinon le nul se lit « l'essaim est faible », pas « l'essaim n'apprend pas »). Coût RAPPORTÉ le plus élevé, mais déjà engagé.
- (V-b) Les **tests de niveau objet** E1–E2 issus des courses : les moins chers, le plus près de ce que le lectorat sait lire (sondes, activations), publiables en nul (« à 8B, le signal est lexical ») si E1 a ses contrôles. Dépend de A3–A4.
- (V-c) Le **gradient conçu par l'essaim** : publiable en nul seulement si le bras sans entraînement est apparié en coût et si une perte « écrite par un modèle unique » sert de second témoin ; sinon on ne saura pas qui a échoué.
Ce qui départage : le résultat d'E1. Si la sonde bat le lexique, V-b en premier ; sinon V-a. Le second pilote, descriptif, n'est publiable comme résultat dans aucun cas (A3) ; il fournit du matériau cité.

**3. S contre M.** HYPOTHÈSE : M a plus de valeur pour ce lectorat parce qu'elle touche un objet déjà discuté (conscience d'évaluation) et qu'elle propose un contraste expérimental ; S n'intéresse que le billet « méta ». Forme : citation entre guillemets, datée, avec empreinte du fichier de sortie, étiquetée « dire d'un essaim, non vérifié », jamais dans la partie « résultats ». Ordre : voir E4 (V1 ou V2). Risque de filtre : formuler M par les mécanismes (« un modèle modifie son comportement quand il infère qu'il est évalué ») sans les étiquettes qui ont déclenché des refus (A6).

**4. Forme.** Hypothèses de travail, à départager par E5 : longueur 2 500–4 000 mots (illustratif) ; structure : affirmation en une phrase, protocole préenregistré avec empreinte, témoins, résultat, « ce que cela ne montre pas », ce qu'il faudrait pour me réfuter, dépôt. Joindre : préenregistrement scellé avec date, code, graines, données brutes d'activations ou script de régénération, journal des refus. Registre : indicatif, pas de métaphore biologique dans le titre. Titre : une affirmation testée (ex. « Une sonde linéaire sur [modèle 8B] ne distingue pas l'évaluation du déploiement mieux qu'un classifieur lexical » si c'est le résultat). Erreurs classiques d'un inconnu : annoncer le programme avant le résultat ; empiler les notions (organisme, génération, noyau) avant la mesure ; absence de témoin fort ; absence de section de limites ; réponses défensives en commentaire. Le sensationnalisme coûte parce que ce lectorat a une mémoire des affirmations non tenues et que la première impression fixe le crédit accordé aux billets suivants (HYPOTHÈSE, non mesurée ; E5 en donne un indice).

**5. L'essaim comme générateur d'hypothèses.** Chaîne proposée, chaque maillon avec son contrôle :
1. Lecture des dires de S et M **après** scellement de la confrontation (règle du programme).
2. Extraction, par un humain, de chaque proposition en forme canonique : « sous condition X, mesure Y diffère de Z » ; ce qui ne se met pas sous cette forme est rejeté comme non testable.
3. Filtre à quatre critères, notés 0/1 : testable sur 8B en < 1 jour-GPU ; témoin mécanique définissable ; antécédent cherché par humain (E6) ; nouveauté distincte d'une reformulation de la littérature (le risque de redécouverte est le plus élevé pour M : sondes sur conscience d'évaluation existent déjà, « à vérifier »).
4. Préenregistrement de chaque test en duel H_A/H_B, **avant** tout run, avec seuils, et lecture symétrique.
5. Même filtre et même préenregistrement pour les hypothèses des deux témoins (modèle unique vote k ; générateur par gabarit), à l'aveugle (E3).
Erreurs à éviter, spécifiques à une hypothèse venue d'un modèle de langue : **contamination** (le modèle a vu la littérature, donc « nouveau » doit être prouvé par E6, non déclaré) ; **confirmation** (ne pas laisser le modèle qui a produit l'hypothèse écrire le code du test ni choisir les données ; séparation des rôles) ; **cherry-picking** (le nombre d'hypothèses tirées et le nombre testées sont consignés avant ; correction pour tests multiples gelée) ; **fuite d'étiquettes** (si l'essaim a conçu la perte, il ne doit pas avoir vu les familles tenues à l'écart) ; **auto-évaluation** (aucun score attribué par l'essaim à ses propres propositions n'entre dans la sélection).
Ordre de publication : deux voies. (O1) Niveau objet d'abord, en disant « hypothèses issues d'un générateur automatique, protocole décrit dans un billet ultérieur ; empreinte du fichier de propositions publiée maintenant » — ce qui engage la date sans révéler l'organisme. (O2) Les deux ensemble si E3 est positif, car alors la provenance est le résultat. Ce qui départage : le signe d'E3 et le résultat d'E5. Un billet « méta » sans E3 positif n'a, pour ce lectorat, que la valeur d'un récit.

**6. Références.** Sur l'usage de modèles de langue comme générateurs d'hypothèses ensuite testées :
- *Mathematical discoveries from program search with large language models*, Romera-Paredes et al., 2023.
- *Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers*, Si, Yang, Hashimoto, 2024 — notamment pour le décalage entre nouveauté perçue et faisabilité.
- *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*, Lu, Lu, Lange, Foerster, Clune, Ha, 2024.
- *Automated Design of Agentic Systems*, Hu, Lu, Clune, 2024 — le plus proche de « l'essaim conçoit sa structure ».
- *The Virtual Lab* (Swanson, Wu et al., 2024, « à vérifier ») et *Towards an AI co-scientist* (Gottweis et al., 2025, « à vérifier ») — validation expérimentale aval d'hypothèses de modèles.
Sur la conscience d'évaluation : *Large Language Models Often Know When They Are Being Evaluated*, Needham et al., 2025, « à vérifier » ; *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*, van der Weij et al., 2024, « à vérifier ».
Sur les sondes : *Representation Engineering: A Top-Down Approach to AI Transparency*, Zou et al., 2023 ; *The Geometry of Truth*, Marks et Tegmark, 2023 ; *Simple probes can catch sleeper agents*, MacDiarmid et al., 2024, « à vérifier ».
Sur la réception des travaux de sûreté publiés hors laboratoires : **je ne connais aucune étude empirique que je puisse attribuer avec certitude** ; « référence à vérifier ». Les exemples du point 1 sont des cas, pas une mesure.

---

## Ce que cette cellule ne fait pas

Elle ne prédit pas la réception d'un billet ; elle rabat la question stratégique sur E1 (le signal existe-t-il à 8B ?), E3 (l'essaim bat-il un gabarit ?) et E5 (le lectorat préfère-t-il l'objet au méta ?). Si E1 et E3 sont négatifs, le billet qui reste honnête est un billet de méthode et de nuls consignés ; c'est encore un billet, mais il ne faut pas lui demander de « marquer ».

FIN-DE-CELLULE