# Proposition A — Tour III.1 : l'apprentissage profond peut-il identifier à lui seul ce qui crée la fertilité ?

**État des pièces** : les cinq pièces annoncées sont présentes et lisibles ; aucune ne paraît coupée (le code RL5-07 absent est déclaré tel par la relecture elle-même). Rien de `donnees/` n'a été servi, conformément à la consigne.

**Position en une phrase (HYPOTHÈSE de travail, à réfuter ci-dessous)** : « identifier à lui seul » est mal posé, parce que l'identifiabilité est une propriété du couple *classe de modèles × distribution des données*, jamais de l'algorithme ; la question utile devient : *les hypothèses d'identifiabilité peuvent-elles être fournies par la structure interne des données (temps, environnements, non-gaussianité) sans intervention externe, et comment le vérifier ?* Ma réponse provisoire : pour les **sources latentes** (jusqu'à permutation et transformation composante par composante), oui sous hypothèses testables en partie ; pour **la direction causale entre ces sources et la fertilité**, non sans intervention, expérience naturelle ou invariance défendable — et aucune pièce servie n'a séparé ces deux niveaux.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| A1 | « Estimer » et « identifier » sont deux opérations que l'apprentissage profond ferait ou non ; la formule de Lazar (« estimer mais pas identifier à lui seul ») est donc décidable. | HYPOTHÈSE | L'identifiabilité est un énoncé sur la classe de modèles et la loi des données (Hyvärinen et Pajunen 1999, *Nonlinear independent component analysis: Existence and uniqueness results*, RAPPORTÉ). Un réseau est un estimateur de fonction ; il n'« identifie » ni ne « n'identifie pas ». La question doit être reformulée en : quelles hypothèses, d'où viennent-elles, comment les tester. |
| A2 | Il existe des « paramètres qui créent la fertilité » au sens d'un petit nombre de variables manipulables ou non. | HYPOTHÈSE | La relecture (RL5-12) note le mélange manipulable/non manipulable (Holland 1986, *Statistics and Causal Inference*, RAPPORTÉ). Si les « paramètres » sont des attributs de paire (distance de domaine, âge), il n'y a pas d'effet causal défini, seulement une modération. Aucune pièce ne tranche. |
| A3 | Les théorèmes d'identifiabilité (ICA non linéaire avec auxiliaire, CRL) identifient « les causes ». | HYPOTHÈSE — présentée comme résultat par `reponse-conv-audit-question-6-v1` | Ces théorèmes identifient des **sources latentes indépendantes** (conditionnellement à l'auxiliaire), jusqu'à permutation et transformation monotone par composante (Hyvärinen et Morioka 2016, *Unsupervised Feature Extraction by Time-Contrastive Learning and Nonlinear ICA* ; Khemakhem, Kingma, Monti et Hyvärinen 2020, *Variational Autoencoders and Nonlinear ICA: A Unifying Framework* — RAPPORTÉ). Ils ne disent rien de la flèche entre une source et la reprise. conv-audit glisse de « latentes identifiées » à « causes identifiées » sans le dire : c'est le même type de glissement que RL5-02 reprochait à la réponse 5 (PCMCI/NOTEARS présentés comme apprentissage profond). |
| A4 | L'ordre temporel des citations, les sous-domaines/décennies/pays comme environnements, les « décalages parcimonieux de mécanismes » et le bruit non gaussien sont « offerts gratuitement » par les données scientométriques. | HYPOTHÈSE (conv-audit Q6 les affirme ; la relecture RL5-17 attaque déjà les décennies) | (i) L'ordre temporel donne une direction mais n'exclut pas les confondeurs cachés (vagues de financement, modes) ni la rétroaction reprise → visibilité → contact ; (ii) les environnements doivent laisser le *mécanisme* invariant et faire varier le *reste* : les normes de citation varient par discipline et par décennie, c'est-à-dire le mécanisme de l'issue même ; (iii) « décalage parcimonieux » (quelques mécanismes changent entre environnements) est une hypothèse structurelle sur le monde, non une observation ; (iv) la non-gaussianité est mesurable, mais LiNGAM exige aussi linéarité, acyclicité et absence de confondeur caché (Shimizu, Hoyer, Hyvärinen et Kerminen 2006, *A Linear Non-Gaussian Acyclic Model for Causal Discovery*, RAPPORTÉ) — les deux dernières sont douteuses ici. |
| A5 | Les courses de l'organisme fournissent « affectations randomisées, dose de contact contrôlée » utilisables pour la science réelle. | HYPOTHÈSE | Identification valide *dans le monde de la course* ; le transport vers la littérature réelle demande de nommer les mécanismes supposés communs (Bareinboim et Pearl 2016, *Causal inference and the data-fusion problem*, RAPPORTÉ). RL5-11 l'a dit ; conv-audit Q6 dit « transport écrit d'avance » sans dire quoi. |
| A6 | Un « score de recouvrement des facteurs vrais » sur mondes inventés mesure la capacité à identifier les causes. | HYPOTHÈSE | Le recouvrement (MCC, R²) mesure la récupération de *latentes*, pas la discrimination cause/accompagnateur. Un monde où la cause et un leurre confondu ont des variances différentes est gagné par n'importe quelle ACP ; Reisach, Seiler et Weichwald 2021 (*Beware of the Simulated DAG! Causal Discovery Benchmarks May Be Easy to Game*, RAPPORTÉ) l'ont montré pour la découverte de structure. Il faut des mondes **appariés** (cause et leurre de même variance, même corrélation marginale à l'issue). Aucune pièce n'exige l'appariement. |
| A7 | La fertilité est « la probabilité qu'une idée reprise naisse du croisement », mesurable sans dépendre du traitement. | HYPOTHÈSE | La reprise est mesurée par citations futures, elles-mêmes causées par la visibilité (RL5-13 ; Fable indépendante point 5). Toute identification porte alors sur la cause du proxy. |
| A8 | Un modèle non supervisé sur citations apprend « taille, âge, prestige, langue ». | OBSERVÉ-NON-AUDITÉ (plausible par l'avantage cumulatif : Price 1976, *A general theory of bibliometric and other cumulative advantage processes* ; Barabási et Albert 1999, *Emergence of scaling in random networks* — RAPPORTÉ) | Personne dans les pièces ne l'a mesuré sur l'hypergraphe du programme. C'est une prédiction à tester (E5), pas un fait. |

---

## (b) Expériences décisives, en duel

Toutes les métriques et seuils numériques ci-dessous sont **illustratifs** et à préenregistrer avant exécution. Les mondes inventés doivent être **appariés** (A6) : dans chaque monde, un facteur Z_c **cause** la fertilité, un facteur Z_d l'**accompagne** (corrélé via un confondeur U) ; Z_c et Z_d ont même variance marginale et même corrélation marginale avec l'issue, réglées par construction.

### E1 — Les hypothèses « gratuites » suffisent-elles à récupérer la cause plutôt que le leurre ?

- **H_A** : avec l'ordre temporel et les environnements comme seules variables auxiliaires (aucune intervention), un modèle d'ICA non linéaire à auxiliaire (TCL ou iVAE) récupère Z_c et Z_d comme sources distinctes, et un test aval (régression invariante entre environnements, Peters, Bühlmann et Meinshausen 2016, *Causal inference by using invariant prediction*, RAPPORTÉ) retient Z_c et rejette Z_d.
- **H_B** : sans intervention, le modèle mélange Z_c et Z_d ou retient Z_d ; seule l'adjonction de données interventionnelles (dose randomisée) sépare les deux.
- **Métrique** : MCC (coefficient de corrélation moyen après appariement hongrois) entre latentes récupérées et vraies ; taux de rétention de Z_c et de rejet de Z_d par le test d'invariance, sur ≥ 20 mondes × 5 graines.
- **Seuils (illustratifs)** : H_A tenue si MCC(Z_c) ≥ 0,8 et rejet de Z_d dans ≥ 90 % des mondes **en l'absence** d'intervention.
- **Contrôle négatif** : mondes où la fertilité est du bruit pur (aucune cause) : tout facteur « retenu » là est une fausse alerte ; taux toléré ≤ 5 % (illustratif).
- **Issues** : si le bras observationnel atteint le seuil et le bras interventionnel n'ajoute rien → H_B falsifiée (et la thèse « non sans intervention » de la réponse 5 avec elle). Si le bras observationnel échoue là où le bras interventionnel réussit → H_A falsifiée, et la réponse de conv-audit Q6 (« identifient — avec l'hypothèse ») est fausse *pour ces hypothèses-là*. Si les deux échouent → le générateur ou le modèle est en cause ; aucune conclusion sur la question (consigné comme échec de banc).

### E2 — Le graphe découvert sur l'hypergraphe réel est-il structure ou artefact d'échelle ?

- **H_A** : la structure découverte (LiNGAM ou PCMCI sur séries par niche) est stable sous standardisation et sous transformation de rang des variables.
- **H_B** : elle change massivement → ce qui est « découvert » est la varsortabilité (variances croissant avec l'âge et la taille des niches).
- **Métrique** : distance de Hamming structurelle (SHD) normalisée entre graphe brut et graphe standardisé ; stabilité par rééchantillonnage (fréquence de chaque arête sur 100 bootstraps).
- **Seuils (illustratifs)** : H_A tenue si SHD normalisée ≤ 0,1 et ≥ 80 % des arêtes ont une fréquence bootstrap ≥ 0,7.
- **Contrôle négatif** : permutation des années à l'intérieur de chaque niche (détruit l'ordre temporel, conserve les marges) : le graphe doit se dissoudre (densité d'arêtes stables ≤ celle d'un graphe aléatoire).
- **Issues** : stabilité → H_B falsifiée (l'artefact n'explique pas le résultat ; les hypothèses restantes — pas de confondeur caché — demeurent à défendre). Instabilité → H_A falsifiée ; la voie « découverte de structure sur données d'observation » est morte pour ce jeu de données jusqu'à préconditionnement défendu.

### E3 — Les environnements scientométriques sont-ils des environnements au sens de l'invariance ?

- **H_A** : il existe un ensemble non vide de paramètres candidats dont la relation à la fertilité est invariante entre sous-domaines (ICP accepte au moins un ensemble au niveau α), et cette invariance tient sur un environnement **tenu à l'écart** choisi avant analyse.
- **H_B** : ICP rend l'ensemble vide (aucun sous-ensemble invariant) ou l'ensemble accepté échoue sur l'environnement réservé → soit les environnements changent le mécanisme (RL5-17), soit aucun parent causal n'est observé.
- **Métrique** : taille de l'ensemble accepté ; erreur de prédiction sur l'environnement réservé rapportée à celle d'un modèle prédictif ordinaire.
- **Seuil (illustratif)** : H_A tenue si l'ensemble accepté est non vide et si son erreur sur l'environnement réservé est ≤ 1,1 × celle du modèle prédictif ordinaire (un ensemble invariant plus mauvais qu'un modèle naïf hors environnement n'a pas de valeur pratique).
- **Contrôle négatif** : environnements formés par découpage **aléatoire** des mêmes données : ICP doit accepter tout (invariance triviale) ; si l'ensemble se rétrécit avec des environnements aléatoires, le test est mal calibré.
- **Contrôle positif** : retrouver l'invariance sur un monde inventé à décalage parcimonieux planté.
- **Issues** : ensemble vide ou échec hors environnement → H_A falsifiée ; la voie (c) de la réponse 5 et la « multiplicité des environnements » de conv-audit Q6 cessent d'être des hypothèses « offertes ». Ensemble non vide et tenue hors environnement → H_B falsifiée pour ces sous-domaines ; les décennies restent à tester séparément.

### E4 — Les latentes « causales » prédisent-elles une intervention jamais vue mieux qu'un modèle purement prédictif ?

Je reprends ici, en le disant, le critère proposé par la relecture (section e) et je le durcis par la ligne de base.

- **H_A** : le modèle à structure causale (latentes identifiées + estimateur d'effet) prédit l'effet d'une dose de contact jamais testée (par exemple 7 titres après 0, 2, 5, 10 — exemple tiré de la pièce) sur la survie aux tests de mort, avec couverture de l'intervalle de prédiction à 90 % atteinte, et une erreur inférieure à celle d'un modèle prédictif sans structure.
- **H_B** : le modèle prédictif ordinaire fait aussi bien à ε près → la structure causale n'apporte rien dans le monde de la course.
- **Métrique** : couverture empirique sur N courses ; rapport des erreurs absolues moyennes.
- **Seuils (illustratifs)** : N = 30 courses, échec si plus de k = 5 sorties d'intervalle, ou si rapport d'erreurs ≥ 0,95.
- **Contrôle négatif** : une intervention préenregistrée comme inerte (par exemple l'ordre d'affichage des titres dans le tableau minimal) doit donner un effet prédit et observé nul ; un effet là signale une fuite ou une sélection.
- **Issues** : échec de couverture → H_A falsifiée (le modèle estime, il n'identifie pas, au sens de conv-audit Q6). Succès sans battre la ligne de base → H_A falsifiée aussi, point que conv-audit Q6 ne prévoit pas. Succès avec ligne de base battue → H_B falsifiée, *dans le monde de la course seulement* (A5).

### E5 — Qu'apprend en pratique un modèle non supervisé sur l'hypergraphe réel ?

- **H_A** : les composantes dominantes d'un modèle non supervisé (β-VAE ou apprentissage contrastif sur voisinage de citations) sont expliquées par taille, âge, langue, prestige de revue : sonde linéaire R² ≥ 0,8 (illustratif) pour les k premières composantes ; les composantes restantes sont instables entre graines (MCC inter-graines ≤ 0,3).
- **H_B** : il existe au moins une composante stable entre graines (MCC ≥ 0,7) qui prédit la reprise future **après** contrôle des quatre nuisances (R² partiel ≥ 0,05, illustratif).
- **Contrôle négatif** : mêmes sondes avec étiquettes de reprise permutées : R² partiel doit être ≈ 0.
- **Issues** : H_A tenue → la prédiction d'A8 est confirmée et toute voie non supervisée doit commencer par une **projection hors des nuisances** préenregistrée. H_B tenue → la composante devient un **candidat** à soumettre à E3 et E4 ; elle n'est pas une cause.

---

## (c) Pour chaque instrument : la mesure minimale qui dit s'il fonctionne

Protocole commun : banc de mondes inventés **appariés** (cause Z_c et leurre Z_d de même variance et même corrélation marginale avec l'issue ; graines multiples ; niveaux de bruit croissants ; version avec confondeur caché et version sans). Toute mesure est un couple (taux de détection de Z_c comme cause, taux de fausses alertes sur Z_d et sur les mondes sans cause). Les lignes de base mécaniques à battre sont nommées ; si l'instrument ne les bat pas, il n'a pas montré qu'il fait autre chose qu'elles.

| Instrument | Cas honnêtes appariés | Détection / fausses alertes à mesurer | Vérifications mécaniques à battre | Outil ouvert (existence RAPPORTÉE) |
|---|---|---|---|---|
| **Démêlage non supervisé** (β-VAE, FactorVAE) | Mondes appariés ; même modèle, 10 graines | Détection : MCC(Z_c) ≥ seuil sur toutes graines. Fausse alerte : variance de l'appariement entre graines (Locatello et al. 2019, *Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations*, RAPPORTÉ : sans biais inductif, les facteurs changent avec la graine) | ACP ; ICA linéaire | `disentanglement_lib` |
| **ICA non linéaire sans auxiliaire** | Un seul monde suffit | Il faut montrer qu'il existe deux solutions de perte égale et de MCC différent ; si on les exhibe, l'instrument est hors jeu par théorème (Hyvärinen et Pajunen 1999). C'est une **démonstration de non-fonctionnement**, pas un banc | — | — |
| **ICA non linéaire avec auxiliaire** (TCL, iVAE) | Mondes appariés avec auxiliaire = temps (segments) ou = environnement ; variante où l'auxiliaire n'a que 2 valeurs (viole la variabilité suffisante) | Détection : MCC(Z_c) et MCC(Z_d) séparément ; l'instrument « fonctionne » s'il sépare les deux sources ; il ne décide pas laquelle cause. Fausse alerte : MCC élevé avec un auxiliaire **permuté** (fuite) | Régression sur l'auxiliaire seule ; ACP par segment | Implémentations publiques des auteurs (référence à vérifier pour la version) |
| **Apprentissage de représentations causales** (CITRIS et parents : Lippe, Magliacane, Löwe, Asano, Cohen et Gavves 2022, *CITRIS: Causal Identifiability from Temporal Intervened Sequences*, RAPPORTÉ) | Mondes avec interventions à **cible connue** (ce que la théorie exige) contre mondes avec seulement le temps | Détection : récupération du graphe entre latentes (SHD) **uniquement** dans le bras interventionnel ; si le bras temporel seul y parvient, la condition d'intervention était superflue dans ce banc (à publier comme tel) | NOTEARS sur latentes d'ACP | Code public de CITRIS (référence à vérifier) |
| **Découverte sous non-gaussianité** (LiNGAM) | Mondes linéaires non gaussiens sans confondeur (honnête) ; mêmes mondes **avec** confondeur caché et **avec** boucle reprise → contact (déloyaux mais réalistes) | Détection : orientation correcte Z_c → Y dans le cas honnête ≥ 95 % ; fausse alerte : orientation confiante dans le cas confondu (le taux d'orientation erronée *confiante* est le chiffre qui compte) | Ordre des variances (Reisach et al. 2021) ; corrélation simple | `lingam` (Python) |
| **Séries temporelles** (PCMCI : Runge, Nowack, Kretschmer, Flaxman et Sejdinovic 2019, *Detecting and quantifying causal associations in large nonlinear time series datasets*, RAPPORTÉ) | Séries par niche avec contact → fertilité à délai planté ; variante avec tendance commune (mode) non observée | Détection : lien au bon délai ≥ 90 % ; fausse alerte : liens trouvés sur séries à années permutées ≤ 5 % ; liens spurieux dus à la tendance commune | Granger linéaire bivarié ; corrélation croisée décalée | `tigramite` |
| **Score de recouvrement** (l'instrument de conv-audit Q6) | C'est une métrique, non un instrument ; sa validité se mesure par sa **corrélation avec la bonne décision cause/leurre** sur les mondes appariés | Si MCC élevé coexiste avec décision cause/leurre au hasard (50 %), le score ne mesure pas ce que conv-audit lui fait mesurer | Hasard (50 %) | — |
| **Prédiction d'intervention jamais vue** | Courses avec doses tenues à l'écart ; une intervention inerte préenregistrée | Couverture d'intervalle ; erreur relative à la ligne de base prédictive (E4) | Modèle prédictif sans structure ; interpolation linéaire entre doses voisines | — |

Deux remarques d'intégrité : (i) toutes les « lignes de base à battre » sont volontairement triviales ; un instrument qui ne les bat pas sur un banc apparié n'a rien montré ; (ii) la relecture (RL5-10) signale, sans l'établir, que l'application de ces outils à un hypergraphe de citations serait une zone vierge ; je la traite comme question ouverte et non comme avantage.

---

## (d) Ancrage matériel

Tout chiffre ci-dessous est **illustratif** (aucun ne vient des faits servis).

- **Données** : instantané OpenAlex (base ouverte ; existence RAPPORTÉE) restreint aux sous-domaines du programme ; textes pour les confondeurs latents via plongements de documents scientifiques ouverts — SciBERT (Beltagy, Lo et Cohan 2019, *SciBERT: A Pretrained Language Model for Scientific Text*, RAPPORTÉ) ou SPECTER (Cohan, Feldman, Beltagy, Downey et Weld 2020, *SPECTER: Document-level Representation Learning using Citation-informed Transformers*, RAPPORTÉ). Volume de travail après filtrage : de l'ordre de 10⁶ documents × 768 dimensions, soit quelques gigaoctets (illustratif).
- **Mondes inventés appariés** : générateur à graphe causal explicite (cause, leurre, confondeur, temps, environnements), quelques centaines de mondes de 10⁴ à 10⁵ unités ; coût CPU négligeable (heures sur une machine de bureau, illustratif). C'est la pièce la moins chère et la plus décisive ; elle doit être écrite et empreintée avant toute analyse réelle.
- **Modèles** : iVAE/TCL et β-VAE de petite taille (quelques millions de paramètres) : entraînement de l'ordre de 1 à 10 heures GPU par configuration et par graine ; pour E1 et E5 (≈ 20 mondes × 5 graines + hypergraphe réel × 10 graines), quelques centaines d'heures GPU, soit quelques centaines à un ou deux milliers d'euros en location (illustratif). PCMCI, LiNGAM, ICP : CPU, heures à jours selon le nombre de niches.
- **Courses (E4)** : coût dominé par les appels aux modèles de langage de l'organisme ; les pièces ne donnent aucun chiffre, je n'en invente pas. Pour les juges figés, un modèle ouvert gelé (famille Llama, Qwen ou Mistral, version à fixer et à empreinter — existence RAPPORTÉE, version non vérifiée) évite la dérive silencieuse d'un modèle hébergé.
- **Puissance** : la relecture (RL5-16) rappelle, de mémoire, que les effets en science des sciences sont de l'ordre de quelques pour cent sur des milliers d'unités (RAPPORTÉ, non audité). Pour E4, N = 30 courses ne détecte qu'un effet de dose très marqué ; c'est une limite à consigner, pas à contourner.

---

## Ce qui est réfutable ici et ce qui ne l'est pas

Réfutable par les duels ci-dessus : (1) que les hypothèses « gratuites » suffisent à séparer cause et leurre (E1) ; (2) que la structure découverte sur l'hypergraphe n'est pas un artefact d'échelle (E2) ; (3) que les sous-domaines sont des environnements au sens de l'invariance (E3) ; (4) que la structure causale apporte quelque chose à la prédiction d'intervention dans la course (E4) ; (5) que le non supervisé apprend surtout des nuisances (E5).

Non réfutable par ces expériences, et à écrire comme tel : le transport du monde de la course vers la science réelle (A5) ; la nature manipulable ou non des « paramètres » (A2) ; la validité du proxy de fertilité (A7). Sur ces trois points, aucune pièce servie n'apporte autre chose qu'une hypothèse, et la réponse de conv-audit à la question 6 les présente comme réglés : c'est son défaut principal.

FIN-DE-CELLULE