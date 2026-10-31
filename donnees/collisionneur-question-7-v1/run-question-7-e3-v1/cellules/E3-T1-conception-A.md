# Proposition A — Question 7 : l'allumage comme ensemble autocatalytique de fiches

## 0. Pièces reçues

Trois pièces lisibles et complètes : `question-3-fertilite-v1`, `reponse-conv-audit-question-3-v1`, réponse d'Argon (sections A–G + bibliographie), `lecture-reponse-argon-bisociation-v1`. Les pièces `question-1-chapelles-v1` et `question-2-niches-v1` sont nommées comme contexte mais **absentes** du lot servi : je ne reconstitue pas leur contenu. Le journal de course de la génération 1 et le « tableau minimal » ne sont pas fournis non plus ; tout ce que je dis sur leur format est une proposition, pas une description.

Statut des pièces : tout ce qui vient de conv-audit et d'Argon est **RAPPORTÉ** (pièces à attaquer, références de mémoire marquées SUPPOSÉ par leurs auteurs). Les mots de Lazar sont **RAPPORTÉ** (transcription). Les chiffres des événements OpenAI de septembre–octobre 2026 cités par Argon sont **OBSERVÉ-NON-AUDITÉ** (sources secondaires, aucune empreinte).

---

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| P1 | Il existe une relation de **catalyse** entre fiches : une fiche *rend possible* une fusion à laquelle elle ne participe pas comme réactif. | HYPOTHÈSE | Un ensemble RAF exige que chaque réaction soit catalysée par un élément de l'ensemble. La pièce conv-audit ne définit aucune catalyse ; sans elle, « autocatalytique » se réduit à « atteignable par fermeture depuis le corpus », ce qui est trivialement vrai dès que le graphe est connexe. |
| P2 | Il existe un mécanisme de **disparition** des fiches (l'analogue de la dilution ou de la dégradation). | HYPOTHÈSE | « S'entretenir sans apport extérieur » n'a de contenu que s'il y a quelque chose contre quoi s'entretenir. Les fiches ne se consomment pas (reconnu par la question) ; si rien ne les tue, tout lot « s'entretient » par inertie. |
| P3 | Le « sans apport extérieur » est définissable alors que le corpus reste accessible à chaque génération. | HYPOTHÈSE | Le corpus joue le rôle du *food set* ; dans un RAF, le food set est toujours présent. Il faut donc distinguer *apport* (nouvelles fiches tirées du corpus) et *substrat* (corpus consultable pour justifier une fusion), ce que la pièce ne fait pas. |
| P4 | La dose de contact (titres, fusions par génération) est le bon paramètre de contrôle. | HYPOTHÈSE | Dans les modèles de Hordijk et Steel, le paramètre de contrôle est le **niveau de catalyse par molécule**, pas le nombre de réactions tentées. Transposé ici : fraction des fusions survivantes qui rendent possible ≥ 1 fusion ultérieure. La dose en est au mieux une variable instrumentale. |
| P5 | Une fermeture autocatalytique est un signe de fertilité. | HYPOTHÈSE, et contre-indiquée par une antériorité | Vasas, Szathmáry et Santos (2010, PNAS, *Lack of evolvability in self-sustaining autocatalytic networks…* ; attribution de mémoire, à vérifier sur PDF) soutiennent que des ensembles autocatalytiques peuvent s'entretenir sans être évolutifs. Un lot qui boucle sur ses paraphrases s'entretient et n'est pas fertile. |
| P6 | Le test de mort (juges LLM) joue le rôle d'une contrainte thermodynamique externe. | HYPOTHÈSE | Un juge figé est optimisable (Argon F.1, RAPPORTÉ). La « survie » n'est pas une loi de conservation ; un lot peut s'allumer en apprenant à passer le juge. |
| P7 | Les modèles de Bettencourt (R0 > 1 ; composante géante) et l'hypothèse RAF sont trois formalisations d'un même phénomène. | RAPPORTÉ (lecture conv-audit) — contenu des papiers SUPPOSÉ | Ce sont trois objets distincts : processus de branchement (R0), percolation (composante géante), fermeture catalytique (RAF). Ils peuvent se contredire : un processus de branchement supercritique n'a besoin d'aucune catalyse. C'est précisément ce qui est à départager (duel 1). |
| P8 | L'algorithme de détection RAF s'applique à un graphe dont l'ensemble des espèces grandit à chaque génération. | HYPOTHÈSE | L'algorithme (Hordijk et Steel 2004, *J. Theor. Biol.*, *Detecting autocatalytic, self-sustaining sets in chemical reaction systems* ; attribution de mémoire, à vérifier) travaille sur un réseau de réactions fixé. Ici les produits sont des types nouveaux : il faut le relancer par génération et définir ce qu'est « la même fiche » d'une génération à l'autre. |

---

## 2. Où l'analogie casse, et la réparation minimale qui la rend testable

**Ce qui tient.** La structure formelle RAF — un food set F, des réactions à réactifs et produits, une relation de catalyse, et le critère « fermeture (tous les réactifs atteignables depuis F) + réflexivité (chaque réaction catalysée de l'intérieur) » — est une structure de graphe hyper-orienté, pas une structure chimique. Elle se transpose à n'importe quel système où des objets en produisent d'autres sous condition d'un troisième. Les fiches, fusions et corpus fournissent trois des quatre ingrédients.

**Ce qui casse, dans l'ordre de gravité.**

1. **Pas de catalyse définie (P1).** C'est la cassure principale. Sans catalyse, le RAF dégénère en atteignabilité, c'est-à-dire en la composante géante de Bettencourt. La pièce conv-audit propose une analogie sans l'ingrédient qui la distingue.
2. **Pas de disparition (P2).** Sans décroissance, « auto-entretien » n'est pas une propriété dynamique.
3. **Pas de stœchiométrie.** Une fiche peut réagir un nombre illimité de fois ; le nombre de fusions possibles croît comme le carré du lot. Le seul facteur limitant est le taux de survie aux tests de mort, qui ramène le problème à un processus de branchement (Galton-Watson, R0) et non à un RAF, sauf si la catalyse est contraignante.
4. **Substrat ouvert (P3).** Le corpus est un food set non borné ; un RAF détecté peut n'être qu'un reflet de la structure du corpus (ponts déjà existants dans la littérature), ce que signale Argon F.2 sur la contamination synthétique (RAPPORTÉ).
5. **Produits nouveaux (P8).** Chimie : espace d'espèces fixé ; ici : espace ouvert. Un « cycle » de fiches peut être une boucle de paraphrases.

**Réparation minimale (définition opérationnelle proposée, HYPOTHÈSE à tester).**

Soit le journal d'une course sous forme d'un hypergraphe orienté par génération g = 0, 1, …, G :

- **Nœuds** : fiches f, chacune avec génération de naissance, statut (survivante / morte / doublon) et empreinte de contenu.
- **Hyperarêtes (fusions)** : r = ({f_i, f_j} → f_k, c), où c est l'ensemble des **fiches de contexte** effectivement citées ou utilisées par le proposeur pour justifier la fusion sans être réactifs. **Catalyse opérationnelle** : f_c catalyse r si f_c ∈ c et si une ablation (relancer la même fusion sans f_c dans le contexte, mêmes graines) fait chuter la survie de f_k sous le seuil du juge. C'est coûteux ; version journalisable sans relance : c = fiches citées comme prémisses dans la fiche produite (DAG de dépendances, comme le recommande Argon E.3 — RAPPORTÉ).
- **Food set F** : fiches tirées du corpus (dose d par génération).
- **Disparition** : une fiche survivante non réutilisée (ni réactif ni catalyseur) pendant τ générations est retirée du lot (τ = 2, illustratif). Les fiches tuées au test de mort sont retirées immédiatement.
- **Doublon** : fiche dont la similarité à une fiche existante dépasse un seuil mécanique (voir §4) ; elle ne compte pas comme produite.

**Allumage (définition A1).** Un lot L_g s'allume à la génération g_0 si, après **gel du food set** (d = 0 pour g > g_0), le sous-hypergraphe des fusions dont réactifs et catalyseurs sont dans L_g ∪ F_{≤g_0} contient un ensemble RAF (fermeture + réflexivité au sens de Hordijk-Steel) **et** ce RAF produit ≥ 1 fiche survivante non-doublon par génération pendant k générations consécutives (k = 3, illustratif).

**Fertilité d'une paire (définition A2).** Contribution de la fusion r à la fermeture : différence entre la taille du plus grand RAF avec et sans r (knock-out), normalisée par la taille du lot. Alternative plus faible : nombre de descendants survivants non-doublons de f_k à horizon k générations (R0 local).

Ces deux définitions sont **exclusives au niveau de la prédiction** : A2-knock-out suppose que la structure catalytique compte ; A2-descendants ne le suppose pas. C'est le duel 4.

---

## 3. (b) Les duels, la prédiction chiffrée et le critère de mort

Tous les seuils ci-dessous sont **illustratifs** : aucun chiffre du lot de faits ne porte sur nos courses.

### Duel 1 — Fermeture catalytique contre processus de branchement (le duel qui tranche l'analogie)

- **H_A (RAF)** : la survie d'un lot après gel dépend de la *structure* des catalyses (existence d'une fermeture réflexive), au-delà du ratio de branchement moyen.
- **H_B (branchement)** : la survie d'un lot après gel est prédite par le seul ratio moyen σ = (fiches survivantes non-doublons produites par fiche et par génération) ; la structure des catalyses est indifférente.
- **Dispositif** : pour chaque lot réel, construire un lot **recâblé** : mêmes fiches, mêmes nombres de fusions par fiche (degrés conservés), mais relation de catalyse permutée au hasard (modèle nul à degrés conservés). Relancer les deux après gel.
- **Métrique** : P(sustain, k=3) pour lots réels vs recâblés, appariés ; différence Δ.
- **Seuil** : Δ ≥ 0,2 en probabilité avec intervalle bootstrap excluant 0 (illustratif) → H_B falsifiée. Δ indistinguable de 0 alors que les lots réels s'entretiennent → H_A falsifiée (l'allumage existe mais n'est pas catalytique ; parler de RAF est alors une surcouche sans contenu).
- **Contrôle négatif** : lots de fiches issues de corpus mélangés au hasard (textes sans rapport) ; aucun des deux ne doit s'entretenir ; s'ils s'entretiennent, le juge est passable par n'importe quoi et le duel n'a pas eu lieu.
- **Ce que chaque issue falsifie** : issue 1 falsifie la lecture « c'est Bettencourt R0 et rien d'autre » ; issue 2 falsifie la transposition RAF de conv-audit. Les deux issues sont informatives.

### Duel 2 — Seuil dans la dose contre croissance lisse

- **H_A (transition)** : P(sustain) en fonction de la dose d présente une bascule : largeur de transition w < 0,25 × étendue de la grille, et la variance de la taille finale du lot est maximale à d_c (susceptibilité).
- **H_B (lisse)** : P(sustain) croît de façon monotone sans point d'inflexion marqué ; la variance ne pique pas ; un modèle linéaire ou saturant simple ajuste aussi bien qu'une sigmoïde.
- **Dispositif** : grille de doses d ∈ {2, 4, 8, 16, 32} fusions par génération (illustratif), n lots par dose, gel à g_0 = 4, suivi k = 3.
- **Métrique** : comparaison sigmoïde vs linéaire/saturant par critère d'information sur doses tenues à l'écart (une dose retirée, prédite) ; pic de variance.
- **Seuil** : ΔAIC ≥ 6 en faveur de la sigmoïde **et** pic de variance à la dose d'inflexion → H_B falsifiée. Aucun des deux → H_A falsifiée. Attention : un processus de branchement a aussi un seuil à σ = 1 ; le duel 2 ne distingue donc pas RAF de branchement, il distingue « bascule » de « pas de bascule ». C'est pourquoi le duel 1 passe avant.
- **Contrôle négatif** : même grille avec juge remplacé par acceptation aléatoire au même taux moyen ; si une bascule apparaît aussi, elle vient de la combinatoire des fusions, pas de la fertilité.

### Duel 3 — Entretien réel contre entretien emprunté au corpus

- **H_A** : après gel, la production de fiches survivantes non-doublons reste ≥ 1 par génération (constante ou croissante).
- **H_B** : la production décroît de façon exponentielle après gel (tout venait des tirages du corpus).
- **Métrique** : série n_g après gel ; ajustement exponentiel vs constant.
- **Seuil** : demi-vie estimée < 1,5 génération → H_A falsifiée ; n_g non décroissant sur k = 3 avec p < 0,05 contre l'exponentielle → H_B falsifiée.
- **Contrôle négatif** : lot où la fusion est désactivée (seuls tirages) → doit s'éteindre instantanément ; lot où le détecteur de doublons est désactivé → si l'entretien n'apparaît que là, l'allumage était un cycle de paraphrases.

### Duel 4 — Fertilité de paire : knock-out de fermeture contre descendance

- **H_A** : la contribution de fermeture (A2-knock-out) prédit la descendance future d'une fusion (nombre de descendants survivants à horizon 3) mieux que les traits de la paire (trou social, structure commune, désaccord — traits de conv-audit §3, RAPPORTÉ) et mieux que la survie initiale de f_k.
- **H_B** : la descendance est prédite par les traits de la paire et le verdict initial ; la contribution de fermeture n'ajoute rien.
- **Métrique** : AUC et gain de log-vraisemblance sur fusions tenues à l'écart, modèle avec vs sans la variable de fermeture.
- **Seuil** : gain d'AUC ≥ 0,05 (illustratif) → H_B falsifiée ; gain ≤ 0,01 → H_A falsifiée.
- **Contrôle négatif** : même prédiction sur les lots recâblés du duel 1 ; la variable de fermeture doit y perdre tout pouvoir.

### Prédiction chiffrée pour la génération 2 et critère de mort

- **Prédiction (HYPOTHÈSE, chiffres illustratifs)** : si la transposition RAF tient, alors, avec un juge dont le taux moyen de survie est p et une dose d, l'allumage apparaît quand σ = p·d·(fraction de fiches catalysantes) dépasse ~1, et la structure recâblée s'entretient significativement moins souvent. L'antériorité de Mossel et Steel (2005, *J. Theor. Biol.*, *Random biochemical networks: the probability of self-sustaining autocatalysis* ; attribution de mémoire, à vérifier) indique que dans le modèle polymère le niveau de catalyse requis croît seulement linéairement avec le nombre d'espèces, soit de l'ordre de un à deux catalyseurs par molécule ; transposé, cela prédit que la bascule se situe à **une ou deux fusions catalysées par fiche survivante et par génération**, pas à des dizaines. C'est une prédiction d'ordre de grandeur, réfutable.
- **Critère de mort 1 (celui de l'arbitre)** : sur toute la grille de doses, aucun lot ne satisfait A1 (k = 3) → l'allumage n'existe pas à cette échelle pour cet organisme ; la question 7 est close pour la génération 2.
- **Critère de mort 2 (plus sévère et plus probable)** : des lots satisfont A1 mais Δ (duel 1) est nul → l'allumage existe, le RAF n'y est pour rien ; on garde R0 et la composante géante, on abandonne le vocabulaire autocatalytique.
- **Critère de mort 3** : des lots satisfont A1 uniquement avec le détecteur de doublons désactivé → l'allumage est un artefact de paraphrase.

---

## 4. (c) Instruments : la mesure minimale qui dirait s'ils fonctionnent

| Instrument | Cas honnêtes appariés | Taux à mesurer | Vérification mécanique à battre |
|---|---|---|---|
| **Détecteur RAF** (Hordijk-Steel relancé par génération) | Hypergraphes synthétiques de taille et degrés identiques aux journaux réels, avec RAF planté (positifs) vs recâblés à degrés conservés (négatifs) ; 100 de chaque (illustratif) | Détection ≥ 0,95 sur plantés ; fausses alertes ≤ 0,05 sur recâblés. Si fausses alertes élevées, le graphe est si dense que tout est RAF : l'instrument ne dit rien. | Fermeture par atteignabilité seule (composante géante). Si la détection RAF ne classe pas mieux que l'atteignabilité sur les cas appariés, elle n'apporte rien. |
| **Détecteur de doublons** (fausses nouveautés) | Paires (fiche, paraphrase produite par un modèle ouvert) vs paires (fiche, fiche réellement différente du même sujet, étiquetée à la main) ; appariées par longueur et sujet ; 200 paires (illustratif) | Détection des paraphrases ≥ 0,9 ; fausses alertes sur vraies nouveautés ≤ 0,1 | Jaccard sur n-grammes (MinHash) à seuil fixé. Le détecteur à plongements doit battre MinHash sur les paraphrases profondes ; sinon on garde MinHash, moins cher et auditable. |
| **Tests de mort (juges figés)** | Fiches saines vs fiches avec défaut planté (erreur de signe dans une construction, hypothèse manquante, transfert spécieux au sens d'Argon F.1), appariées par longueur et domaine ; 100 paires (illustratif). L'épisode des 3 retraits en cascade d'octobre 2026 (OBSERVÉ-NON-AUDITÉ) justifie le défaut « erreur de signe ». | Détection des défauts ≥ 0,8 ; fausses morts sur fiches saines ≤ 0,1 ; et surtout **stabilité** : même verdict à ±5 % sur relance à graines différentes | Tests unitaires exécutables pour les fiches contenant du code ; vérification formelle quand un énoncé est formalisable. Un juge LLM qui ne bat pas ces contrôles mécaniques là où ils existent n'est pas une contrainte externe. |
| **Compteur de dose et gel du food set** | Journal avec tirages marqués ; audit : aucune fiche étiquetée « fusion » ne doit contenir plus de x % de texte copié du corpus (x illustratif = 30) | Fuites du corpus dans les fusions après gel : ≤ 1 cas sur 100 | Comparaison d'empreintes de passages avec le corpus (n-grammes de longueur 8) |
| **Catalyse par ablation** | 50 fusions survivantes (illustratif), relancées sans chaque fiche de contexte ; vérité terrain = chute de survie | Accord entre « citée comme prémisse dans le DAG » et « ablation fait chuter la survie » ≥ 0,7 (kappa) | Si l'accord est bas, la catalyse journalisée (prémisses citées) ne mesure pas la catalyse réelle et le RAF détecté est un artefact de citation. |

---

## 5. Antériorités (toutes : attribution de mémoire, contenu à vérifier sur PDF avant tout préenregistrement)

**Ensembles autocatalytiques, chimie et modèles abstraits.**
- Kauffman, S. A. (1986), *Autocatalytic sets of proteins*, *Journal of Theoretical Biology* — origine du concept ; prédiction d'un seuil dans la densité de catalyse.
- Eigen, M. et Schuster, P. (1979), *The Hypercycle: A Principle of Natural Self-Organization*, Springer — cycle de catalyseurs mutuels ; antériorité du « chaque élément en rend un autre possible ».
- Hordijk, W. et Steel, M. (2004), *Detecting autocatalytic, self-sustaining sets in chemical reaction systems*, *J. Theor. Biol.* — algorithme RAF polynomial.
- Mossel, E. et Steel, M. (2005), *Random biochemical networks: the probability of self-sustaining autocatalysis*, *J. Theor. Biol.* — niveau de catalyse requis linéaire en nombre d'espèces (source de ma prédiction d'ordre de grandeur).
- Hordijk, W., Steel, M. et Kauffman, S. (2012), *The structure of autocatalytic sets: evolvability, enablement, and emergence*, *Acta Biotheoretica* — décomposition en sous-RAF ; pertinent pour « contribution d'une fusion à la fermeture ».
- Vasas, V., Szathmáry, E. et Santos, M. (2010), *Lack of evolvability in self-sustaining autocatalytic networks constraints metabolism-first scenarios for the origin of life*, *PNAS* — auto-entretien ≠ évolutivité (contre P5).
- Fontana, W. et Buss, L. W. (1994), *'The arrival of the fittest': Toward a theory of biological organization*, *Bulletin of Mathematical Biology* — organisations auto-maintenues dans un λ-calcul ; antériorité directe d'« objets symboliques qui se produisent mutuellement sans stœchiométrie ».
- Jain, S. et Krishna, S. (1998), *Autocatalytic sets and the growth of complexity in an evolutionary model*, *Physical Review Letters* — émergence d'un ensemble autocatalytique par dynamique de graphe avec disparition des nœuds non soutenus (modèle de disparition analogue à mon τ).

**Technologie et idées.**
- Arthur, W. B. (2009), *The Nature of Technology*, Free Press ; Arthur, W. B. et Polak, W. (2006), *The evolution of technology within a simple computer model*, *Complexity* — technologies construites par combinaison de technologies existantes ; avalanches de remplacement.
- Weitzman, M. L. (1998), *Recombinant Growth*, *Quarterly Journal of Economics* — croissance par combinaison d'idées ; absence de catalyse explicite (c'est un modèle de branchement, utile comme H_B).
- Padgett, J. F. et Powell, W. W. (2012), *The Emergence of Organizations and Markets*, Princeton University Press ; Padgett, Lee et Collier (2003), *Economic production as chemistry*, *Industrial and Corporate Change* — autocatalyse appliquée aux organisations et aux compétences.
- Hordijk sur les économies comme ensembles autocatalytiques : **référence à vérifier** (je ne peux pas l'attribuer avec titre et année sûrs).

**Cascades d'idées entre générations.**
- Tria, Loreto, Servedio et Strogatz (2014), déjà dans le lot (RAPPORTÉ via conv-audit et Argon) ; Iacopini, Milojević et Latora (2018), *Network Dynamics of Innovation Processes*, *Physical Review Letters* — nouveautés corrélées sur un réseau ; Monechi et al. sur les « vagues de nouveautés » dans l'adjacent possible : **référence à vérifier**.
- Bettencourt et al. 2006, 2008, 2009, 2015 : existence RAPPORTÉE comme vérifiée par conv-audit, contenu SUPPOSÉ ; je retiens qu'elles fournissent les deux H_B naturelles (R0 et composante géante) et non une confirmation de l'hypothèse RAF.

Point que ni conv-audit ni Argon ne signalent : l'antériorité la plus proche de l'objet (fiches symboliques, pas de stœchiométrie, produits de type nouveau) est Fontana-Buss, pas Kauffman. C'est là que je chercherais les pièges déjà rencontrés (organisations triviales, « auto-copieurs »).

---

## 6. (e) Ce qu'il faut journaliser dès la génération 1

Sans coût de calcul supplémentaire, uniquement du format :

1. Pour chaque fusion : identifiants des deux réactifs, de la fiche produite, **liste des fiches de contexte citées comme prémisses** (c'est la catalyse journalisée ; sans elle, le duel 1 est impossible), graine, modèle, génération.
2. Pour chaque fiche : génération de naissance, origine (corpus / fusion), verdict du test de mort et sa stabilité sur relance (au moins 2 graines), empreinte de contenu (MinHash + plongement), générations où elle a été réutilisée comme réactif ou prémisse.
3. Dose effective par génération (fusions tentées, fusions survivantes, tirages du corpus) — distinguée de la dose nominale.
4. **Tous les essais avortés** (fusions mortes, doublons), sans troncature — reprise de la recommandation d'Argon D (RAPPORTÉ) ; sans eux, σ est surestimé.
5. La taille de la composante géante du graphe fiche → fusion → fiche par génération (déjà proposée par conv-audit, RAPPORTÉ) — je l'approuve comme grandeur de H_B, pas comme mesure d'allumage.
6. Un gel de food set effectif sur au moins **un** lot de la génération 1 (d = 0 pendant 2 générations) : c'est la seule donnée qui permette de dire avant la génération 2 si le duel 3 a une chance d'être informatif.

---

## 7. (d) Ancrage matériel — tout est illustratif sauf mention

- **Modèles ouverts** : un proposeur de fusions de taille moyenne (famille ouverte, ~70 milliards de paramètres), trois juges figés dont au moins un d'une famille différente du proposeur (pour que le duel 1 ne mesure pas l'auto-complaisance d'un même modèle), un modèle d'embedding ouvert pour les doublons, MinHash pour la base.
- **Calcul (duels 1–3, génération 2)** : 5 doses × 10 lots × 2 conditions (réel / recâblé) × 7 générations (4 avant gel + 3 après) ≈ 700 lot-générations ; à ≤ 32 fusions par lot-génération et ~18 000 jetons par fusion (proposeur + 3 juges + 2 relances de juge), ≈ 400 millions de jetons. Détection RAF et recâblage : polynomiaux, négligeables (CPU). Ablations de catalyse (§4, 50 fusions × ~5 contextes) : ≈ 5 millions de jetons supplémentaires.
- **Coût** : à un tarif d'hébergement de modèle ouvert de l'ordre de 1 USD par million de jetons, ≈ 400 USD ; sur matériel propre, quelques dizaines d'heures sur 8 GPU de classe H100. Pour comparaison, la seule donnée de coût dans les faits est la requête Argon à 0,61 USD (RAPPORTÉ) : ce banc coûte trois ordres de grandeur de plus, ce qui est le prix d'une question qui a un critère de mort.
- **Ce qui ne coûte rien et vaut d'être fait d'abord** : les points 1–6 du §6 et la vérification des PDF du §5 ; si la catalyse journalisée ne corrèle pas avec la catalyse par ablation (dernière ligne du §4), tout le banc ci-dessus mesure du bruit, et il vaut mieux le savoir avant de dépenser.

---

## Bilan en une phrase par partie

(a) L'analogie ne tient que si l'on ajoute ce que la pièce ne contient pas : une catalyse journalisable et une disparition des fiches ; sans ces deux ajouts elle se réduit à la composante géante. (b) Allumage = RAF détecté après gel du food set produisant ≥ 1 fiche nouvelle non-doublon par génération pendant k générations ; fertilité = perte de taille du RAF au knock-out de la fusion. (c) Le duel qui compte oppose structure catalytique et ratio de branchement sur des lots recâblés ; la prédiction d'ordre de grandeur est une bascule à une ou deux fusions catalysées par fiche et par génération ; trois critères de mort, dont deux plus probables que celui de l'arbitre. (d) Fontana-Buss et Jain-Krishna sont les antériorités les plus proches de l'objet, Mossel-Steel la source du chiffre. (e) Journaliser prémisses citées, essais avortés et un gel réel dès la génération 1, sinon la génération 2 ne pourra pas trancher.

FIN-DE-CELLULE