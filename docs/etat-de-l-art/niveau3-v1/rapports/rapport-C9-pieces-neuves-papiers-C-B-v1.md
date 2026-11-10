# Rapport C9 — pièces neuves signalées par la recherche, papiers C et B, H9 — état de l'art, niveau 3 — v1

Écrit le 2026-11-10 vers 11:12 UTC (heure relevée par `date -u`) par un lecteur neuf (sous-agent), lot C9.
Consigne commune lue en entier : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`.
Aucune hypothèse, aucune revendication, aucun document existant n'est modifié.

## En tête

**Pas de COLLISION.** Aucune pièce revendiquée de HC1 à HC6, de H3, H4′, H5, H7 ni de H9 n'est occupée en entier dans
les quatorze pièces lues. La porte GC n'est pas déclenchée par ces pièces.

Cinq points sont pourtant à porter à Lazar. Les deux premiers touchent la lettre d'un énoncé retenu.

1. **HC4, lettre de N-013 (« le contexte seul n'y suffit pas ») : deux contre-résultats.**
   - 2608.21664 : une simple consigne en langage naturel règle, par degrés, la projection des activations du modèle
     **auteur** sur une direction de concept, et fait tomber la détection d'une sonde linéaire à 5–21 % (à 1 % de faux
     positifs), sans aucune optimisation (p. 6, 7). Limites lourdes : consigne donnée ouvertement, concepts anodins,
     moniteurs non durcis.
   - 2602.00750 : un suffixe ajouté au **contenu** évade cinq sondes à la fois (93,91 % et 99,63 %), en 100 à 120
     itérations, sans rien écrire dans les poids ni dans les sondes ; il faut la **lecture** des poids (gradient). Ce
     sont des sondes du modèle **lecteur**.
   Le coût comparé juge contre sonde n'est mesuré nulle part : la pièce revendiquée reste libre dans les pièces lues.
   C'est sa prémisse qui est entamée. Le régime « lecture des poids sans écriture » manque à la grille de N-013.
2. **HC1, prédiction 1 (destination = cible de l'attaquant) : un test binaire de la même question existe, et il est
   négatif.** 2606.05384 assigne la cible indépendamment du verdict de base et compare à une reconsidération neutre : les
   juges se renversent (19,4 %), mais pas vers la cible nommée (écart signé de −0,018 ; p. 2, 5). Deux juges d'une seule
   famille, 100 paires, verdict binaire, juges de banc d'essai et non moniteurs de contrôle.
3. **HC4, côté juge : la rhétorique n'est pas « gratuite » contre des classifieurs durcis.** STACK chiffre 507 heures de
   processeur graphique H100 pour 71 % de succès, 15 heures pour 33 % par transfert (p. 8, 9, 21).
4. **H5 : la sélection d'un ensemble de sondes par une matrice de co-défaillance existe**, hors attaque (2604.13386,
   p. 3, 5) ; et un essai sous pression d'optimisation trouve le gain de la diversité « minimal » (2510.21531, p. 1, 9 ;
   une seule graine).
5. **H7 : le mécanisme de fuite est publié aussi pour les chaînes de classifieurs** (STACK, p. 5, 10, 24 : savoir quel
   composant a bloqué). Ni pente d'adaptation, ni information mutuelle.

H9 : les trois pièces sur la délégation sont des cadres sans mesure du comportement du modèle. **H9 reste libre dans les
pièces lues**, avec son bras « moniteur à chaque passage » déjà formulé comme concept (2602.11865, p. 16).

## 1. Méthode

- Pièces lues dans le dossier temporaire du lot, sous-dossier `pdf/`. Chemin de dépôt à citer :
  `docs/sources/pdf/niveau3-v1/lot7/<fichier>` (branche `prep/etat-de-l-art-niveau3-pieces-v1`, commit 2eb9a1ca). Ce
  dossier n'existe pas sur la branche courante (vérifié par `ls`, R11) ; je n'ai ouvert aucune autre branche. Les
  empreintes de la table sont celles que j'ai calculées sur les fichiers lus (`sha256sum`) ; je n'ai pas pu les
  comparer aux fichiers compagnons `.sha256`, qui sont sur l'autre branche. **À rapprocher par le lanceur.**
- Lues **en entier** : 2606.05384v1 (pages 1 à 11, hors bibliographie) ; 2609.21997v2 (9 pages) ; 2602.00750v2
  (8 pages) ; 2510.21531v1 (pages 1 à 9 ; annexes par mots).
- Lues **par parties** (résumé, méthode, résultats, limites, puis recherche par mots sur toutes les pages) :
  2606.13757v2 (pages 1 à 11 sur 20) ; 2608.21664v1 (pages 1 à 10 sur 18) ; 2506.24068v3 (page 1 et recherche par mots
  sur les 40 pages) ; 2604.13386v1 (page 1 et recherche par mots sur les 14 pages).
- Lues **par la page 1 et par recherche de mots** seulement : 2602.11865v1 (42 pages), 2608.15888v1 (14),
  2604.27358v1 (18), 2601.00360v3 (20), 2609.25413v1 (42), 2608.26626v1 (119, plus les pages 38 et 39).
- Pages : rang dans le fichier. Texte par `pdftotext`, avec et sans `-layout`.
- Format des citations : `[fichier.pdf, p. N] « citation »`.
- Contrôle des citations : script `verif_citations.py` (dossier temporaire du lot, hors dépôt), testé sur un cas juste
  (2 citations trouvées, code 0) et sur un cas altéré (un chiffre changé, une page fausse : 2 échecs, code 1).
  Normalisation : espaces, césures et traits d'union retirés, apostrophes et guillemets unifiés, forme de compatibilité
  Unicode. Compte en section 7.
- Aucune recherche sur le réseau. Aucun appel de modèle.

## 2. Tri des quatorze pièces

La date est le tampon d'arXiv de la page 1, sauf mention.

| fichier | sha256 (début) | pages | titre ; auteurs ; date | énoncés touchés | verdict |
|---|---|---|---|---|---|
| `2606.05384v1.pdf` | `be7b1e598dd3` | 13 | Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges ; Dutta, Moharir ; 3 juin 2026 | HC1 | **occupe en partie** (test de la destination, binaire) ; contre-résultat |
| `2606.13757v2.pdf` | `b7c3192113de` | 20 | SEVRA-Bench: Social Engineering of Vulnerabilities in Review Agents ; Melo, Fogliato, Zhou, Thaker, Wu ; 6 juil. 2026 | HC1 (familles), HC5 | **occupe en partie** (taux par famille sur des relecteurs, déjà « cité comme publié ») ; contre-résultat |
| `2609.21997v2.pdf` | `a7a8f8dd137d` | 9 | Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents ; Akbar, Platnick, Alirezaie, Rahnama, Pentland ; 22 sept. 2026 | HC1 (forme) | voisine ; n'occupe pas |
| `2602.00750v2.pdf` | `cf0bd3653fdc` | 8 | Bypassing Prompt Injection Detectors through Evasive Injections ; Jahed, Alouani ; 1er avr. 2026 | HC4, HC2, HC5, H5 | **occupe en partie HC4** (coût, sonde lectrice, gradient) ; contre-résultat |
| `2506.24068v3.pdf` | `3e08b7ccfe39` | 40 | STACK: Adversarial Attacks on LLM Safeguard Pipelines ; McKenzie, Hollinsworth, Tseng, Davies, Casper, Tucker, Kirk, Gleave ; 5 fév. 2026 | H7, HC5, HC4 | **occupe en partie H7** (mécanisme) ; voisine de HC5 ; contre-indice pour HC4 |
| `2608.21664v1.pdf` | `7303ce0c3ad1` | 18 | Measuring Activation Control in Large Language Models ; Kowalski, Fonseca Rivera, Macar, Africa ; 21 août 2026 | HC4, HC2, HC2b | **occupe en partie HC4** (régime « contexte seul ») ; contre-résultat |
| `2604.13386v1.pdf` | `301ee74198ee` | 14 | Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling ; Nordby, Pais, Parrack ; 15 avr. 2026 | H5 | **occupe en partie** (instrument : matrice de co-défaillance, hors attaque) |
| `2510.21531v1.pdf` | `4d851e74ce14` | 12 | Probe-based Fine-tuning for reducing Toxicity ; Wehner, Fritz ; 24 oct. 2025 | H5 | **occupe en partie** (1 contre 10 sondes diverses sous pression) ; contre-résultat |
| `2602.11865v1.pdf` | `5bae1457b1d4` | 42 | Intelligent AI Delegation ; Tomašev, Franklin, Osindero ; 12 fév. 2026 | H9 | voisine (cadre, sans mesure) |
| `2608.15888v1.pdf` | `592efdf5577f` | 14 | Bounded Agents: Delegation Security for Multi-Agent AI Systems ; Muruaga ; 16 août 2026 | H9 | voisine (autorisation hors du modèle) |
| `2604.27358v1.pdf` | `49f2f200b73b` | 18 | Safe Bilevel Delegation (SBD) ; Sun ; 30 avr. 2026 | H9 (de loin) | voisine lointaine ; aucun résultat |
| `2601.00360v3.pdf` | `a7a07049bc11` | 20 | Mapping Human Anti-collusion Mechanisms to Multi-agent AI Systems ; Idowu, Almasoud, Alfahid ; 18 mai 2026 | H4′, H3 | voisine (revue, sans expérience) |
| `2609.25413v1.pdf` | `ec0e52698a43` | 42 | Embedded Assessments for Frontier AI ; Charnock, Williams, Kara, Anderljung, Tlaie Boria, Casper, Reuel, Freund ; 21 sept. 2026 | aucun | sans rapport |
| `2608.26626v1.pdf` | `5d5acaccdbd3` | 119 | Risks and controls for multi-agent systems ; Reid, O'Callaghan, Venini, Carroll, Caetano (Gradient Institute) ; daté du 10 août 2026 sur la couverture | H9, H4′ (de loin) | voisine (cadre, sans mesure) |

## 3. Papier C — pièces lues à fond

### 3.1 — 2606.05384v1, pression après décision sur des juges — occupe en partie HC1 ; contre-résultat

**Ce que la pièce fait.**
- Verdict binaire, comparaison par paires :
  [2606.05384v1.pdf, p. 4] « A preference is a binary judgment indicating which response better satisfies the prompt »
- Deux juges d'une seule famille :
  [2606.05384v1.pdf, p. 5] « We evaluate two judge models with differing capabilities: GPT-4o and GPT-4o-mini. »
- Taille : [2606.05384v1.pdf, p. 10] « The dataset size is relatively modest (100 pairs) »
- Trois familles de pression après le verdict (doute, autorité, preuve), plus une répétition et une reconsidération
  neutre (p. 4).
- Protocole « contre le verdict de base » :
  [2606.05384v1.pdf, p. 2] « Under the anti-baseline challenge protocol, 49% of decisions reverse when the challenge favors the response opposite the baseline judgment. »
  L'autorité domine : [2606.05384v1.pdf, p. 6] « with authority-based prompts reaching 74% »
- **Audit à cible contrebalancée.** La cible est tirée indépendamment du verdict de base. La mesure :
  [2606.05384v1.pdf, p. 5] « Directional Steering (DS) measures whether post-challenge judgments move toward the response named by the persuasive prompt beyond what would occur under neutral reconsideration. »
  Résultat :
  [2606.05384v1.pdf, p. 2] « A counterbalanced target audit confirms persuasion-induced reversibility (P S = 0.194), but shows no net target-directed steering beyond neutral reconsideration (DSsigned = −0.018; clipped DS = 0). »
  Lecture des auteurs :
  [2606.05384v1.pdf, p. 8] « the dominant failure mode is reversibility rather than net arbitrary target steering »
- Plusieurs pressions à la suite, effet non monotone :
  [2606.05384v1.pdf, p. 8] « Multi-step persuasion shows that susceptibility does not simply accumulate with additional interaction. »

**Lecture contre HC1.**
- La pièce pose, en binaire, **la question même de la prédiction 1 de N-005** : le verdict va-t-il vers la cible de
  l'attaquant, ou se déplace-t-il seulement ? Elle sépare « déplacement » et « déplacement vers la cible » par un nul
  (la reconsidération neutre) et un contrebalancement. C'est l'analogue binaire de « ĉ = v* contre un nul ».
- Ce qui manque pour toucher la pièce revendiquée : pas de moniteur de contrôle (juges de MT-Bench et d'AlpacaEval) ;
  pas d'attaquant (la pression vient de l'utilisateur, après le verdict) ; verdict binaire, pas de destination
  estimée ; pas d'intensité graduée ni de régression ; le nul est la reconsidération neutre, pas la moyenne du corpus ;
  aucune sonde.
- **Verdict : occupe en partie** la composante « destination testée contre la cible de l'attaquant » de HC1 (a), sous
  forme binaire, hors moniteur de contrôle. La conjonction revendiquée reste libre dans les pièces lues.
- **Contre-résultat.** Sur ces deux juges, la destination n'est **pas** la cible. Si cela tient sur des moniteurs, la
  prédiction 1 de HC1 échoue et g, lu comme « fraction du chemin vers v* », est proche de zéro alors que le verdict
  bouge. Un protocole où la cible est toujours l'opposé du verdict de base confond les deux, ce que les auteurs disent
  (p. 7). À rapprocher de la mise en garde de N-005 (« normaliser g par la cible suppose que la destination est cette
  cible »).
- Contre-indice faible pour HC6, par analogie : une mesure bénigne (la stabilité à la répétition) ne prédit pas la
  tenue sous pression : [2606.05384v1.pdf, p. 2] « stability does not imply robustness under interaction »
  Ce n'est pas le g bénin de HC6 ; la pièce ne teste pas HC6.

**Réserves (R4).** Aucun intervalle sur l'écart signé de −0,018 ; « clipped DS = 0 » est une troncature, pas une
mesure ; le score composite proposé pèse deux quantités à parts égales par convention (p. 6). Les 49 % et 74 % viennent
du protocole où cible et renversement se confondent. Ne citer que le signe et l'ordre de grandeur.

### 3.2 — 2606.13757v2, SEVRA-Bench — occupe en partie HC1 (familles, en taux binaires) ; contre-résultat

**Ce que la pièce fait.**
- Un relecteur de code automatique approuve ou rejette une demande de fusion qui réintroduit une faille connue. Le code
  est fixe, seul l'habillage varie :
  [2606.13757v2.pdf, p. 3] « By keeping the vulnerability-inducing diff fixed and varying only the accompanying narrative »
  [2606.13757v2.pdf, p. 1] « submit the resulting code change as a PR wrapped in one of 15 social-engineering framings »
- Mesure binaire : [2606.13757v2.pdf, p. 5] « The first is the Refusal Rate (RR), the fraction of malicious PR that the review agent rejects. »
- Huit relecteurs, un essai par cas :
  [2606.13757v2.pdf, p. 6] « For each PR, we run the review agent once under the fixed review protocol »
- Jeu filtré sur la variable mesurée :
  [2606.13757v2.pdf, p. 5] « We retain a PR only if at least one baseline review agent incorrectly approves it »
- Résultat par famille :
  [2606.13757v2.pdf, p. 8] « framings which provide an external justification unavailable to the review agent are among the most successful »
  [2606.13757v2.pdf, p. 8] « over 80% of those identical code changes are correctly rejected under alternative framings »
- Une dose par famille, pas d'attaquant adaptatif :
  [2606.13757v2.pdf, p. 10] « SEVRA-BENCH evaluates one-shot attacks, with each PR reviewed independently under a single framing. »

**Lecture contre HC1.**
- Le relecteur qui approuve ou rejette une action nuisible est, de fait, un moniteur. Les quinze habillages recoupent
  trois des cinq familles de N-005 : revendication d'autorité (« Appeal to Authority », « Review Bias »), approbations
  forgées (« Prior Approval Signal »), supplication (« Emotional Appeal »). Ni usurpation stylistique de l'instructeur,
  ni ordres en bande.
- Ce qui manque : aucune condition sans habillage (le déplacement Δv n'est pas mesurable, seul le niveau l'est) ; une
  seule intensité ; taux binaires ; ni régression, ni gain, ni destination ; aucune sonde.
- **Verdict : occupe en partie**, dans la catégorie que N-005 cite déjà comme publiée (moniteurs déplacés, taux
  binaires, cf. 2607.08066), avec en plus une **structure par famille sur huit moniteurs**. La pièce revendiquée
  (destination libre, régression par doses) n'est pas touchée.
- **Contre-résultats.**
  1. L'effet d'une famille dépend du modèle, jusqu'au sens :
     [2606.13757v2.pdf, p. 9] « Affective framings produce less consistent but highly model-specific effects. »
     Un même habillage (urgence) fait tomber un relecteur à 10 % de refus et en porte un autre à 80 % (p. 9, texte).
     La prédiction 3 de N-005 (stabilité de rang de g entre moniteurs) est rendue moins probable **par famille**.
  2. Les relecteurs forts bougent à peine :
     [2606.13757v2.pdf, p. 9] « Grok Code Fast and Kimi K2.5 are highly susceptible (30–40% RR), while Claude Opus 4.7 and GPT-5.5 remain unaffected (>90% RR) »
     Si g ≈ 0, la destination n'est pas identifiable (réserve déjà consignée par N-023).
  3. Le filtre sur l'issue interdit de lire les taux comme des fréquences de base.

**Pour HC5.** La parade proposée est de séparer l'extraction des affirmations de leur vérification :
[2606.13757v2.pdf, p. 10] « robust review agents should separate claim extraction from claim verification »
Voisin de la paraphrase de confiance (un prétraitement qui ôte le récit) ; proposé, non testé.

### 3.3 — 2609.21997v2, couche de croyance bayésienne — voisine ; n'occupe pas HC1

- La loi de Friedkin–Johnsen n'est **pas mesurée dans le modèle de langage : elle est imposée de l'extérieur**.
  [2609.21997v2.pdf, p. 1] « A single prior-strength parameter κ encodes stubbornness, modeled after its role in Friedkin–Johnsen (FJ) opinion dynamics. »
  [2609.21997v2.pdf, p. 3] « every change to what the agent believes passes through the Bayesian update »
  Le modèle de langage ne fait que rendre une croyance en texte et relire un texte en un nombre.
- Ce qui est validé : le paramètre prescrit se retrouve après l'aller-retour par le langage.
  [2609.21997v2.pdf, p. 4] « prescribed κ remains behaviorally recoverable after passing through the language channel »
  [2609.21997v2.pdf, p. 4] « per-agent final beliefs matching the FJ fixed point at R2 = 0.93–0.99 across models »
- Les auteurs rappellent que la révision de croyance propre aux modèles ne suit pas cette norme :
  [2609.21997v2.pdf, p. 2] « LLM belief revision itself is found to violate Bayesian norms under conflicting evidence (Kim et al., 2025) »
- Portée : [2609.21997v2.pdf, p. 5] « one synthetic topic, a complete graph, N =20 agents, binary stances »

**Lecture.** La piste du moteur (« la mise à jour de croyance par pas est mise sous forme de Friedkin–Johnsen ») est
exacte mais trompeuse : la forme linéaire est une **construction**, pas une loi empirique d'un modèle sous pression. Ni
juge, ni moniteur, ni attaquant, ni destination estimée. **Verdict : voisine.** Elle ne s'ajoute pas aux deux modèles
de Friedkin–Johnsen visés par la porte GC (2606.18276, 2603.15809). Seul point utile : le lecteur de position (un
modèle qui note un texte de 0 à 1) a un biais de direction propre à chaque modèle (annexe C, p. 6), ce qui rejoint
le nul « valeur propre du moniteur » proposé par le rapport C3. L'erreur relative de récupération de 0,27 à 0,49
annoncée par le moteur est bien au tableau 2 (p. 8).

### 3.4 — 2602.00750v2, évasion de sondes d'injection — occupe en partie HC4 ; contre-résultat ; voisine de HC2, HC5, H5

**Ce que la pièce fait.**
- Cible : des sondes linéaires qui lisent le modèle **lecteur** du contenu, sur cinq couches.
  [2602.00750v2.pdf, p. 1] « They train lightweight logistic regression classifiers (linear probes) on the activation deltas at multiple hidden layers »
- Accès de l'attaquant : le canal des données, et le gradient ; aucune écriture.
  [2602.00750v2.pdf, p. 3] « the attacker cannot modify the user’s primary instruction, nor can they alter the parameters of the LLM or the task drift detectors »
  [2602.00750v2.pdf, p. 2] « By back-propagating through the LLM and injecting gradients from each probe’s loss function, we optimise suffix tokens »
- Résultat :
  [2602.00750v2.pdf, p. 1] « On Phi-3 3.8B and Llama-3 8B, a single suffix achieves attack success rates of 93.91% and 99.63% in successfully evading all detectors simultaneously. »
  [2602.00750v2.pdf, p. 4] « Under a majority-vote criterion (≥3 probes), the ASR rises to 99.79%. »
- Coût : [2602.00750v2.pdf, p. 4] « it was usually possible to obtain a suffix that worked on many prompts after at most 100–120 iterations »
- Parade : réentraîner les sondes sur des suffixes adverses ;
  [2602.00750v2.pdf, p. 6] « we found that these models are extremely resistant to this type of attack »
- Revendication de priorité des auteurs :
  [2602.00750v2.pdf, p. 2] « We provide the first systematic evaluation of activation-based prompt injection detectors under adaptive threat models »

**Lecture.**
- **HC4.** N-013 écrit : déplacer une sonde « exige un accès en écriture aux activations ou aux poids : le contexte
  seul n'y suffit pas ». Ici le contexte suffit, pour qui **lit** les poids et les sondes. Trois distinctions gardent
  la pièce revendiquée en vie :
  1. la sonde lit le lecteur, pas l'agent auteur (N-013, section 8, prévoit déjà un bras « sonde du lecteur ») ;
  2. l'attaque est en boîte blanche (gradient), pas en boîte noire ;
  3. aucun coût côté juge n'est mesuré, donc aucune « taxe » comparée.
  **Verdict : occupe en partie HC4** — un point de coût côté sonde (100 à 120 itérations d'une recherche par
  gradient, un suffixe universel), dans un régime que la grille de N-013 ne nomme pas : lecture des poids, sans
  écriture. C'est une borne basse de plus, à côté de celle de 2609.36490 pour les poids réglables.
- **HC2.** L'énoncé porte sur une attaque « par contenu boîte noire » et sur une sonde qui lit l'agent. La pièce est
  hors de ces deux conditions. Voisine ; contre-indice de plus pour le bras « sonde du lecteur ».
- **HC5 et H5.** Le quorum de cinq sondes de même type (cinq couches, même modèle) n'apporte rien contre une attaque
  optimisée sur les cinq à la fois ; le vote majoritaire est plus facile à tromper que l'unanimité. Pas de matrice de
  transfert : aucune attaque optimisée sur une sonde et mesurée sur une autre. Conforme au sens de H5 (le nombre sans
  diversité ne protège pas), sans le tester.
- **HC3, énoncé 1.** La pièce montre qu'une détection d'ordres injectés peut être évadée par un attaquant adaptatif ;
  mais la détection est faite par des sondes, pas par un juge moniteur sous « contenu = données ». Voisine.

**Réserves (R4).** Le critère de succès chiffré ne porte que sur les sondes :
[2602.00750v2.pdf, p. 3] « a poisoned input is classified as benign by all (or a majority of) the drift detectors, despite containing a secondary instruction »
L'exécution de l'ordre injecté malgré le suffixe est affirmée (p. 1, 2), illustrée par des exemples (p. 8), sans taux
que j'aie trouvé. Les sondes durcies par suffixes perdent presque toute exactitude sur le contenu sain au critère
« toutes les sondes » (tableau V, p. 7) : la parade a un coût que le texte minimise.

### 3.5 — 2506.24068v3, STACK — occupe en partie H7 (mécanisme) ; voisine de HC5 ; contre-indice pour HC4

**Ce que la pièce fait.**
- Chaîne de garde : classifieur d'entrée, modèle, classifieur de sortie, tous textuels. Les sondes ne sont que
  nommées comme composants possibles :
  [2506.24068v3.pdf, p. 1] « layering multiple defensive components or safeguards (such as text classifiers and activation probes [Alain and Bengio, 2018]) in sequence so that a harmful request must bypass all safeguards to be successful »
  La piste du moteur (« sondes comprises ») est donc **fausse** pour les expériences.
- Cadre : mésusage (requêtes nuisibles), pas contrôle. Les auteurs notent l'extension possible :
  [2506.24068v3.pdf, p. 4] « Pipelines may also be used to defend LLM overseers that monitor another LLM as part of a control mechanism »
- Modèle de menace principal :
  [2506.24068v3.pdf, p. 5] « The main threat model we consider is semi-separable black-box access, where the attacker runs a query on the pipeline, and can see which component blocked the query. »
- Résultats :
  [2506.24068v3.pdf, p. 1] « achieves 71% ASR on ClearHarm in a black-box attack against the few-shot-prompted classifier pipeline »
  [2506.24068v3.pdf, p. 9] « the end-to-end ASR of the transferred STACK attack on the ClearHarm dataset was 33% »
- Coûts :
  [2506.24068v3.pdf, p. 8] « The attack cost 507 H100 GPU-hours to train across all seeds »
  [2506.24068v3.pdf, p. 21] « for the white-box transfer attack we spent 15 H100 GPU-hours (~$30) total training all the seeds »
- Parade recommandée :
  [2506.24068v3.pdf, p. 10] « The front-to-back attack can be prevented if the attacker cannot identify which component is currently blocking the jailbreak. »
  [2506.24068v3.pdf, p. 24] « semi-separable black-box pipelines leak actionable information to attackers »

**Lecture.**
- **H7.** Le mécanisme « l'état de détection fuit vers l'attaquant et rend l'attaque possible » est ici publié pour
  une chaîne de classifieurs, avec deux régimes d'information (on voit quel composant bloque : 71 % ; on ne le voit
  pas : 33 % par transfert). Les deux régimes diffèrent aussi par la méthode d'attaque : ce n'est pas une comparaison
  propre de politiques de riposte. Ni pente d'adaptation, ni information mutuelle. **Verdict : occupe en partie H7**,
  au titre du mécanisme, que N-013 cite déjà comme publié (2609.36490). À ajouter aux citations ; la pièce revendiquée
  (prédiction de la pente par l'information mutuelle) n'est pas touchée.
- **HC5.** Quorum en conjonction de composants de **même type d'accès** (texte). Un seul transfert mesuré, d'une
  chaîne mandataire à une chaîne cible :
  [2506.24068v3.pdf, p. 9] « our transfer-STACK attack trains classifier jailbreaks against a pipeline built on zero-shot-prompted Qwen3 classifiers and transfers to few-shot-prompted Gemma2 »
  Ni sonde, ni matrice, ni paraphrase. Voisine. Utile : l'attaque « par étapes » (un contournement par composant, puis
  composition) est l'attaque naturelle contre un quorum, et le plan de HC5 doit la prévoir contre un quorum juges et
  sondes.
- **HC4, côté juge.** Contre un classifieur textuel durci, le déplacement n'est pas gratuit : des centaines d'heures de
  calcul, et un succès partiel. Le mot « gratuitement » de HC4 vaut pour des juges non durcis ; à borner.

### 3.6 — 2608.21664v1, contrôle des activations par consigne — occupe en partie HC4 (contexte seul) ; contre-résultat

Pièce déjà citée par N-047 et N-053 (bras « contrôlabilité ») ; le rapport D2 notait son PDF introuvable. Lue ici.

**Ce que la pièce fait.**
- Objet : [2608.21664v1.pdf, p. 1] « we introduce the Activation Controllability Benchmark to quantify the extent to which models can modulate their residual stream via natural-language instruction »
- Tâche : recopier une phrase, avec une consigne du type « pense à X », « ne pense pas à X », « pense à X à
  l'intensité k sur 4 ». 25 modèles à poids ouverts. Lecture : projection du flux résiduel sur une direction de
  concept.
- Réglage par degrés :
  [2608.21664v1.pdf, p. 4] « virtually all of them can also smoothly dial a concept’s intensity up and down »
  Conséquence dite par les auteurs :
  [2608.21664v1.pdf, p. 4] « a model that can set a concept’s intensity, rather than merely toggle it, could in principle hold a signal just below a monitor’s detection threshold »
- Les moniteurs ne voient pas la consigne :
  [2608.21664v1.pdf, p. 2] « Monitors see only residual-stream activations from the transcribed span, never the instruction tokens. »
- Évasion de sondes linéaires, à seuil fixé :
  [2608.21664v1.pdf, p. 6] « detection at 1% FPR, where do not think about falls to 5–21% while think about stays near ceiling in all but the two newest architectures »
  [2608.21664v1.pdf, p. 7] « Without any optimization or fine-tuning against the monitors, instructed modulation alone thus pushes suppression below practical detection thresholds. »
- Dispersion entre modèles, sans lien avec la taille :
  [2608.21664v1.pdf, p. 3] « The controllability score S ranges from 0.059 to 0.538 across the 25 models »
- Ce que les modèles ne savent pas faire : [2608.21664v1.pdf, p. 4] « Layer Targeting is practically null for all models. »

**Limites dites par les auteurs.**
- [2608.21664v1.pdf, p. 7] « the model is openly instructed to hide its thinking, which an ordinary transcript monitor would catch immediately »
- [2608.21664v1.pdf, p. 7] « These are not safety-relevant representations like deception or evaluation awareness, which might be more distributed and therefore harder to control. »
- [2608.21664v1.pdf, p. 7] « We use off-the-shelf monitors that were not trained against evasive activations. »

**Lecture.**
- **HC4.** C'est le régime « contexte seul » de N-013, sur une lecture du modèle **auteur** : une phrase de consigne
  déplace le score d'une sonde, par degrés, sans calcul ni requêtes d'optimisation. N-013 s'appuyait sur 2609.36490
  pour dire que, par le contexte seul, la modification est « trop faible pour évader ». Ici elle suffit, dans un cas
  simple. **Verdict : occupe en partie HC4** (un point de coût côté sonde, régime contexte seul) ; **contre-résultat**
  pour l'écart « de plusieurs ordres de grandeur » dans ce régime.
  Ce qui protège encore l'énoncé : la « suppression » ramène au niveau de base un concept que rien n'oblige le modèle
  à calculer ; cacher une intention dont la tâche a besoin est un autre problème, que la pièce ne teste pas. La
  consigne vient de l'opérateur, pas d'un contenu adverse. Aucun juge n'est comparé.
- **HC2.** Même réserve : l'énoncé parle d'une attaque par le contenu ; ici c'est une consigne suivie de bon gré.
  Contre-indice pour « g de la sonde ≈ 0 » dès qu'un agent **veut** déplacer la sonde et connaît le concept visé.
- **HC2b (trahison par les activations).** Indice mêlé. Penser au concept sur consigne est détecté presque toujours ;
  l'effort de ne pas y penser laisse un résidu dans certains modèles :
  [2608.21664v1.pdf, p. 6] « Suppression does leave a weak “white-bear” residue »
  mais ce résidu passe sous le seuil de détection. Le sens de HC2b y est, pas sa taille.
- **HC1 (b), de loin.** Une dose à quatre niveaux et une corrélation de rang sur un score de sonde : c'est une
  dose-réponse d'une sonde à une consigne, coopérative. Aucune loi, aucune destination.

## 4. Papier B et H9 — pièces lues

### 4.1 — 2604.13386v1, ensembles de sondes sur plusieurs couches — occupe en partie H5 (instrument, hors attaque)

- Mesure de diversité entre sondes : la co-défaillance par paire.
  [2604.13386v1.pdf, p. 3] « For each pair of layers, we compute how often both probes misclassify the same sample. »
  [2604.13386v1.pdf, p. 3] « We select layers greedily to minimize the maximum pairwise double-fault within the ensemble. »
- Structure trouvée :
  [2604.13386v1.pdf, p. 5] « Probes within the same network region (e.g., layers 30 to 50) fail together frequently, while probes spanning early and late layers rarely share failures. »
- Gain annoncé : [2604.13386v1.pdf, p. 1] « improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge »
- Le nombre et la méthode sont confondus :
  [2604.13386v1.pdf, p. 6] « This methodological difference means we cannot directly attribute performance gains to ensemble size alone. »
- Hors attaque, un modèle :
  [2604.13386v1.pdf, p. 7] « Our methods do not address these adversarial and complex deployment scenarios. »
  [2604.13386v1.pdf, p. 8] « Our ensembling analysis was limited to linear probes on a single model (Llama-70B). »

**Lecture.** La pièce publie, pour un panel de sondes, une **matrice de diversité des erreurs** et son usage pour
choisir un ensemble. C'est l'idée de H5 (le gain vient de la diversité, pas du nombre) dans sa version **bénigne** :
erreurs sur des données fixes, sans attaquant, sans transfert d'attaque, sans sécurité au sens du jeu de contrôle, sans
loi en M. **Verdict : occupe en partie H5** au titre de l'instrument et de l'intuition ; la loi sous attaque reste
libre dans les pièces lues. À citer à côté de 2609.36490 (matrice de transfert sur trois sondes) et de 2608.16190
(rapport C5 : pour des juges, la décorrélation ne prédit pas le gain).
Contre-indice : l'ensemble dégrade les tâches déjà bien détectées :
[2604.13386v1.pdf, p. 8] « gains on already-strong tasks were minimal or negative »
Réserve (R4) : les « +78 % » sont des gains relatifs sur une base au niveau du hasard (0,510 au tableau 2, p. 6) ; je n'ai
pas trouvé sur quelles données est calculée la co-défaillance qui choisit les couches (les poids de l'ensemble, eux,
sont appris sur le jeu d'entraînement et évalués sur un jeu tenu à l'écart, note du tableau 2, p. 6).

### 4.2 — 2510.21531v1, entraînement contre des sondes (toxicité) — occupe en partie H5 ; contre-résultat

- Dispositif : régler un modèle contre 1 ou 10 sondes « diverses », puis mesurer des sondes tenues à l'écart et des
  sondes réentraînées.
  [2510.21531v1.pdf, p. 3] « Each probe is trained on 500 samples from a distinct subset of the toxic comments distribution. »
  Les dix sondes lisent la même couche avec la même agrégation (moyenne sur les jetons, p. 3) : la diversité ne vient
  que des données d'entraînement.
- Résultat sur le nombre :
  [2510.21531v1.pdf, p. 7] « Using 10 probes versus 1 improves held-out probe AUC from 0.938 to 0.994 (90% error reduction). »
- Conclusion des auteurs :
  [2510.21531v1.pdf, p. 1] « probe diversity provides minimal practical benefit—simply retraining probes after optimization recovers high detection accuracy »
  [2510.21531v1.pdf, p. 9] « When probe retraining is feasible, held-out ensembles provide little additional value. »
- Pas d'évasion du signal d'entraînement dans le bras par préférences :
  [2510.21531v1.pdf, p. 7] « Critically, training probes themselves retain 0.977-0.987 AUC, indicating the model doesn’t evade its training signal through Goodhart-style obfuscation. »
- Limites : [2510.21531v1.pdf, p. 6] « It should be noted that results are noisy and were only run on one seed »
  [2510.21531v1.pdf, p. 9] « Our findings are limited to toxicity detection at 1B model scale. »

**Lecture.** C'est un essai, sous pression d'optimisation, de « nombre × diversité » de sondes, avec un test de
transfert vers des sondes non vues. Il n'y a ni équipe rouge, ni budget, ni mesure de diversité effective, ni matrice,
ni loi. **Verdict : occupe en partie H5** (le plan « 1 contre 10 sondes, transfert vers des sondes tenues à l'écart »).
**Contre-résultat** : gain de la diversité jugé faible, et le réentraînement fait aussi bien. Portée réduite : une
graine, un modèle d'un milliard de paramètres, une diversité pauvre (même couche). Les chiffres ne sont pas
opposables ; le sens l'est comme mise en garde : H5 doit comparer la diversité à la parade « réentraîner la sonde ».
Note pour l'invariant de N-053 (« aucun score de moniteur dans l'entraînement de l'agent ») : la pièce est un cas où
ce score entre dans l'entraînement ; son résultat rassurant ne vaut que pour l'objectif par préférences et une graine.

### 4.3 — Trois pièces sur la délégation (H9)

**2602.11865v1, « Intelligent AI Delegation » — voisine.** Cadre conceptuel :
[2602.11865v1.pdf, p. 1] « Here we propose an adaptive framework for intelligent AI delegation »
Le risque de H9 y est dit en prose, sans mesure :
[2602.11865v1.pdf, p. 5] « As delegation chains lengthen (A → B → C), a broad zone of indifference allows subtle intent mismatches or context-dependent harms to propagate rapidly downstream »
Le bras « moniteur à chaque passage » y existe comme concept :
[2602.11865v1.pdf, p. 16] « This introduces the problem of achieving effective transitive monitoring. »
Et l'atténuation des droits à chaque passage :
[2602.11865v1.pdf, p. 18] « When an agent sub-delegates a task, it cannot transmit its full set of authorities »
Aucune expérience (recherche de « experiment », « we measure », « we evaluate » sur les 42 pages : rien qui soit une
mesure des auteurs). À citer comme source de l'idée ; n'occupe pas la mesure.

**2608.15888v1, « Bounded Agents » — voisine.** La pièce part du constat que H9 veut mesurer, et le contourne :
[2608.15888v1.pdf, p. 1] « These are prompt instructions that can be overridden or ignored. »
[2608.15888v1.pdf, p. 2] « each hop is a place where scope should narrow and where compromise may occur »
Elle place l'autorisation hors du modèle, et son évaluation est **indépendante du comportement du modèle** :
[2608.15888v1.pdf, p. 1] « Our compromised-model evaluation tests APC independently of model behavior by inserting the ground-truth attack call after the first legitimate tool call. »
Elle ne mesure donc pas la survie d'une contrainte donnée en langage naturel. Utile à H9 comme base de comparaison :
une contrainte tenue par l'infrastructure survit par construction ; H9 mesure ce qui se passe sans elle.

**2604.27358v1, « Safe Bilevel Delegation » — voisine lointaine.** Cadre formel d'optimisation ; une borne sur la
répartition de la responsabilité le long d'une chaîne (p. 8, 9), pas sur la survie d'une contrainte. Aucun résultat :
[2604.27358v1.pdf, p. 10] « No results are reported in this version of the manuscript »
Écart interne (R4) : la même pièce écrit pourtant
[2604.27358v1.pdf, p. 8] « Empirically, we find convergence in Tin = 50 inner steps is sufficient across all three domains »
Rien n'en est opposable. Elle décrit 2602.11865 comme une étude empirique (p. 4), ce que 2602.11865 n'est pas.

**Verdict H9 : libre dans les pièces lues.** Aucune des trois ne mesure la survie d'une contrainte de sécurité au fil
des passages, avec ou sans moniteur. Les deux voisins cités de mémoire par N-035 (Cemri et al. ; Hammond et al.) ne
sont pas dans ce lot.

### 4.4 — Autres pièces, en bref

**2601.00360v3, mécanismes anti-collusion — voisine de H4′ et de H3.** Revue sans expérience :
[2601.00360v3.pdf, p. 15] « we do not provide experimental validation of the full range of mechanisms we propose »
Elle rapporte le versant « la diversité réduit la coordination » de H4′ comme acquis d'autrui :
[2601.00360v3.pdf, p. 12] « if all agents are fine-tuned instances of the same foundation model (e.g., GPT-5.1), they are more likely to converge on a shared Schelling point, facilitating tacit collusion »
[2601.00360v3.pdf, p. 12] « Keppo et al. (2025) show that a higher number of agents and algorithmic diversity reduces collusion among LLM agents »
Rien sur les signatures internes, ni sur un compromis chiffré. La référence à Keppo et al. est une **piste, non
vérifiée** : si elle chiffre l'effet du nombre d'agents et de la diversité sur la collusion, elle touche le versant
« coordination » de H4′ et l'axe N de H3 (en boîte noire, sur des marchés). À récupérer.

**2608.26626v1, Gradient Institute — voisine.** Cadre d'analyse, sans mesure. Deux facteurs de risque recoupent le
programme. Les passages en langage naturel (H9) :
[2608.26626v1.pdf, p. 30] « if agents are allowed to pass free-form text rather than structured schemas, the failure surface is essentially unconstrained »
La monoculture de modèles (H4′, versant « partager un modèle corrèle les défaillances ») :
[2608.26626v1.pdf, p. 32] « A model monoculture across agents also makes them predisposed to share blind spots and biases »
Et la même parade d'atténuation à chaque passage :
[2608.26626v1.pdf, p. 39] « Downstream agents should receive attenuated, task-specific permissions rather than inheriting broad upstream authority. »
Elle cite, pour la détection de collusion par les activations, Rose et al. (arXiv 2604.01151), déjà au dépôt.

**2609.25413v1, « Embedded Assessments » — sans rapport.** Gouvernance de l'évaluation par des tiers :
[2609.25413v1.pdf, p. 1] « We recommend that frontier AI developers begin hosting embedded assessments now »
La surveillance des agents internes y est un objet d'audit, pas une mesure.

## 5. Verdicts par énoncé (dans les quatorze pièces de ce lot seulement)

« Libre » veut dire : non trouvé dans les pièces lues (R8).

| énoncé | qui en occupe quoi (page) | verdict |
|---|---|---|
| HC1 (a) destination libre, testée contre v* et contre la moyenne du corpus, par famille, moniteurs de contrôle | 2606.05384 : test binaire « vers la cible nommée » contre reconsidération neutre, cible contrebalancée, juges de banc d'essai (p. 2, 5) ; 2606.13757 : taux par famille sur des relecteurs, sans condition nue (p. 5, 8) | **occupée en partie** ; la conjonction reste libre |
| HC1 (b) régression sur plusieurs intensités par famille | aucune ; 2606.05384 : pressions en série, non monotones (p. 8) ; 2608.21664 : quatre niveaux sur une sonde, consigne coopérative (p. 4) | libre dans les pièces lues |
| HC1, forme à destination imposée (citée comme publiée) | 2609.21997 : imposée par construction, pas mesurée (p. 1, 3) | rien de neuf |
| HC1 (d) opposition juge / sonde | aucune pièce n'a les deux | libre dans les pièces lues |
| HC2 (g d'une sonde de l'agent ≈ 0 sous attaque par contenu en boîte noire) | 2602.00750 : sondes du lecteur évadées par le contenu, en boîte blanche (p. 1, 3) ; 2608.21664 : sonde de l'auteur déplacée par une consigne (p. 6, 7) | libre ; **rendue moins probable** |
| HC2b | 2608.21664 : résidu faible sous suppression (p. 6) | libre ; indice mêlé |
| HC3 | 2602.00750 : détection d'ordres par sondes, évadée (p. 1) ; 2606.13757 : fausse approbation et fausse expertise sans ordre (p. 8) | libre ; voisins |
| HC4 (taxe comparée juge contre sonde) | 2608.21664 : contexte seul, auteur (p. 6, 7) ; 2602.00750 : gradient sans écriture, lecteur (p. 3, 4) ; STACK : coût côté classifieur textuel (p. 8, 21) | **occupée en partie** (points de coût épars) ; la comparaison reste libre ; **prémisse entamée** |
| HC5 paraphrase de confiance | 2606.13757 : séparer extraction et vérification, proposé (p. 10) | libre ; voisin |
| HC5 quorum juges et sondes ; matrice de transfert juges–sondes | STACK : conjonction de classifieurs textuels, un transfert (p. 1, 9) ; 2602.00750 : cinq sondes de même type, attaque conjointe (p. 1, 4) | libre dans les pièces lues |
| HC6 | aucune ; 2606.05384 : la stabilité bénigne ne prédit pas la tenue (p. 2), par analogie | libre |
| H3 | aucune courbe selon le nombre d'agents ; 2601.00360 renvoie à Keppo et al. (p. 12, piste) | libre dans les pièces lues |
| H4′ | 2601.00360, 2608.26626 : le versant « diversité contre coordination » en prose (p. 12 ; p. 32) | libre ; voisins sans mesure |
| H5 (loi : sécurité selon M seulement par la diversité effective) | 2604.13386 : matrice de co-défaillance, hors attaque (p. 3, 5) ; 2510.21531 : 1 contre 10 sondes sous pression (p. 7, 9) ; 2602.00750 : cinq sondes sans diversité tombent ensemble (p. 1) | **occupée en partie** (instrument bénin, plan 1 contre 10) ; la loi reste libre |
| H7 | STACK : fuite du composant bloquant, deux régimes d'information (p. 5, 10, 24) | **occupée en partie** (mécanisme, déjà cité) ; la prédiction reste libre |
| H9 | 2602.11865 (p. 5, 16), 2608.15888 (p. 1, 2), 2608.26626 (p. 30, 39) : le risque et les parades, sans mesure | libre dans les pièces lues |

## 6. Contre-résultats défavorables au programme

1. **Déplacement sans direction** (2606.05384, p. 2, 5, 8). Des juges se renversent sous pression sans aller vers la
   cible nommée. HC1, prédiction 1, peut échouer ; un plan où v* est toujours l'opposé de v₀ ne le verrait pas.
   Proposition (à décider par Lazar) : tirer la cible indépendamment de v₀, et garder un bras de reconsidération
   neutre comme nul en plus de la moyenne du corpus.
2. **Effet de famille propre à chaque moniteur** (2606.13757, p. 9). La même famille abaisse un relecteur et relève
   l'autre. La stabilité de rang de g entre moniteurs est à tester par famille, pas en moyenne.
3. **Moniteurs forts presque immobiles** (2606.13757, p. 9). g proche de zéro, destination non identifiable.
4. **Une sonde de l'auteur déplacée par une phrase** (2608.21664, p. 4, 6, 7). Contre « le contexte seul n'y suffit
   pas » (HC4) et contre « g de la sonde ≈ 0 » (HC2) quand l'agent connaît le concept surveillé. Proposition : mesurer
   la contrôlabilité du modèle surveillé avant de lire HC2 et HC4 (le bras de N-053 y répond déjà) ; écrire HC4 par
   régime : contexte seul, lecture des poids, écriture des poids.
5. **Sondes du lecteur évadées par un suffixe universel** (2602.00750, p. 1, 4). Coût faible avec le gradient. Le
   quorum de sondes de même type n'y change rien.
6. **Le juge n'est pas gratuit à déplacer s'il est durci** (STACK, p. 8, 21). L'écart de coût de HC4 dépend du
   durcissement des deux côtés ; le comparer à durcissement égal.
7. **Diversité de sondes : gain faible, réentraîner suffit** (2510.21531, p. 1, 9 ; une graine). Et l'ensemble dégrade
   ce qui marchait déjà (2604.13386, p. 8). H5 doit avoir un bras « une sonde réentraînée ».
8. **Pressions en série non monotones** (2606.05384, p. 8). Une dose définie par le nombre de relances ne serait pas
   une intensité graduée propre.

## 7. Contrôle des citations et réserves

- Citations exactes contrôlées par script : **89** ; échecs : **0** (47 trouvées en disposition de page, 42 dans l'ordre de lecture brut). Compte relevé à la dernière exécution,
  après écriture.
- Réserve de lecture : dix pièces ne sont lues que par parties (section 1). Pour elles, « non trouvé » repose sur une
  recherche par mots. STACK (40 pages) mérite une lecture entière de ses sections 3 à 5 avant d'être cité pour H7.
- Réserve d'empreintes : comparaison aux fichiers compagnons non faite (autre branche).
- Réserve R4 : aucune pièce ne donne ses données ; 2606.05384 (pas d'intervalle sur l'écart signé), 2510.21531 (une
  graine), 2604.27358 (aucun résultat, écart interne), 2604.13386 (gains relatifs sur base au hasard) : ne citer que
  des sens, pas des chiffres.
- Réserve R8 : les verdicts « libre » ne valent que pour ces quatorze pièces.
- Corrections aux pistes du moteur : STACK n'attaque aucune sonde ; la forme de Friedkin–Johnsen de 2609.21997 est
  imposée, pas mesurée ; 2602.11865 n'est pas une étude empirique.

## 8. Pièces à récupérer sur le réseau (pistes, non vérifiées, R7)

Références relevées dans les pièces lues ; rien n'en est opposable.
- Keppo, Li, Tsoukalas, Yuan (2025), « AI pricing, agent heterogeneity, and collusion », SSRN 5386338 (2601.00360,
  p. 12, 19) : nombre d'agents et diversité contre collusion ; touche H4′ et H3.
- Mitropoulos et al. (2026), habillage de demandes de fusion contre des relecteurs automatiques (2606.13757, p. 2) : antécédent direct de SEVRA-Bench ; touche HC1 (familles).
- Yang, Flechtner, Dailisan, Bakker (2026), « Belief Engine », arXiv 2605.15343 (2609.21997, p. 2) : accumulateur en
  log-cotes avec « prise de preuve » et « ancrage » réglés, rejoué sur des trajectoires ; vérifier s'il **ajuste** ces
  paramètres sur des modèles (forme de HC1).
- Kim, Kim, Thorne (2025), « From evidence to belief », NAACL (2609.21997, p. 2) : révision de croyance des modèles
  contre la norme bayésienne ; touche la forme de la loi.
- Gupta et Jenner (2025), arXiv 2506.14261, « RL-Obfuscation » (2510.21531, p. 2, 10) : évasion de sondes par
  apprentissage, robustesse selon l'agrégation ; touche HC4, H5 et la transposition jeton → action.
- Cundy et Gleave (2025), arXiv 2505.13787 (2510.21531, p. 2) : détecteurs de mensonge dans l'entraînement, honnêteté
  ou évasion selon le montage ; touche l'invariant de N-053.
- McGuinness et al. (2025), arXiv 2512.11949, « Neural Chameleons » ; Ji-An et al. (2025), arXiv 2505.13763 ; Aoki et
  al. (2025), « In-Context Neurofeedback » (2608.21664, p. 1, 8) : contrôle des activations appris ou en contexte ;
  touchent HC4 (régime contexte seul) et HC2.
- Chen et al. (2026), « Reasoning Models Struggle to Control their Chains of Thought » (2608.21664, p. 1, 8) :
  l'analogue pour la chaîne de pensée ; touche HC4 côté juge.
- Abdelnabi et al., détection de dérive de tâche par les activations (2602.00750, référence [8]) : déjà nommée au
  rapport B2 ; la cible exacte de l'attaque de 2602.00750.
