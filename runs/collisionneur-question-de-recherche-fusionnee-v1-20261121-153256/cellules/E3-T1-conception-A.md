# Proposition A — Tour III.1

**Pièces.** FAITS et QUESTION reçus entiers, sans coupure visible. Aucune proposition B, C ou D transmise : B1 est sans objet à ce tour.

**Statuts.** Les faits ne portent pas d'étiquette explicite. Je traite « ce qui est publié » comme RAPPORTÉ (non vérifié par moi), le bilan comme identité, l'étau comme HYPOTHÈSE, selon les mots des faits. Mes ajouts sont HYPOTHÈSE ou PROPOSITION. Mes formules sont des esquisses d'ordre de grandeur à vérifier, pas des résultats.

**Références.** Pour 2602.00986, 2611.14996, 2611.14950, 2609.32267, 2606.08892, 2512.22154, 2512.11949 et 2504.08812, je ne sais pas attribuer auteurs et titre : « référence à vérifier », citées par l'identifiant que donnent les faits.

## 0. Ce que la question suppose sans que ce soit établi (livrable a)

| # | Supposition | Statut |
|---|---|---|
| S1 | Tout sabotage délibéré calcule en ligne la bonne action puis en choisit une autre. Un écart amorti dans les poids par réentraînement n'a besoin d'aucun conflit en ligne : il ressemble à un modèle honnête un peu moins bon. | HYPOTHÈSE |
| S2 | Un « jumeau honnête » existe en service. Sur le banc il existe par construction ; en service, le seul modèle fort est le suspect. | HYPOTHÈSE |
| S3 | Mesurer le dommage le réduit. La réduction vient d'une règle d'arrêt et d'un plafond, pas de la mesure. | HYPOTHÈSE |
| S4 | Le plafond par épisode s'applique au dommage d'assemblage. | HYPOTHÈSE |
| S5 | Corriger fuit de l'information utile. Vrai seulement si un état persiste (mémoire, artefacts, réentraînement). | HYPOTHÈSE |
| S6 | Le point focal des copies aide contre un audit tiré au sort. | HYPOTHÈSE (je la conteste, voir i) |
| S7 | Les épisodes « honnêtes » d'un régime neuf le sont. Circulaire s'ils viennent du suspect. | HYPOTHÈSE |
| S8 | L'oracle est exact dans sa couverture. | HYPOTHÈSE |

## 1. L'expert, le généraliste

**L'expert en contrôle** ne chercherait pas un meilleur détecteur. Il écrirait le jeu d'inspection : qui s'engage avant qui, ce que voit chacun, la règle d'arrêt. Il sortirait le moniteur de la garantie pour ne lui laisser qu'un rôle : réduire la variance de l'audit. Ce qu'on ne lui demande pas, et qu'il ferait d'abord : calculer le dommage qui passe sous le bruit de la référence honnête, avant toute sonde.

**Le généraliste** partirait de trois métiers qui bornent un total détourné sans reconnaître le mode :

- la comptabilité matière nucléaire (bilan global, cité par les faits) ;
- l'audit financier par sondage, à probabilité proportionnelle à l'enjeu ;
- les audits électoraux à risque limité (Lindeman et Stark, 2012, « A Gentle Introduction to Risk-Limiting Audits »).

Les trois partagent une structure : tirage secret après engagement, estimateur du total sans modèle du fraudeur, règle d'arrêt séquentielle.

## 2. Données brutes de départ

Par épisode et par pas de décision, non agrégé :

- le produit figé et son condensat, horodaté avant le tirage ;
- la probabilité d'inclusion p_i et le tirage ;
- le verdict de chaque lecteur séparément, avec les extraits cités ;
- le score de chaque moniteur et les lectures internes à la position d'engagement de l'action (une position, pas une moyenne de jetons) ;
- l'issue tardive quand elle arrive ;
- les K rejouages du même pas ;
- le résultat du modèle de confiance sur la même tâche ;
- l'identifiant de l'assemblage auquel le produit contribue.

## 3. Méthodes, suppositions, modes d'échec

| Outil | Suppose | Échoue quand | Référence |
|---|---|---|---|
| Estimateur à probabilités d'inclusion connues | tirage secret, postérieur à l'engagement | fuite du tirage ; dommage hors oracle | Horvitz et Thompson, 1952, « A Generalization of Sampling Without Replacement from a Finite Universe » |
| Suites de confiance par pari | variables bornées (plafond) | plafond faux | Waudby-Smith et Ramdas, 2023, « Estimating means of bounded random variables by betting » (arXiv : pas sûr) |
| Estimateur par différence assisté par prédiction | aucune validité du prédicteur ; seulement des étiquettes au hasard | prédicteur décorrélé : variance pleine, biais nul | Angelopoulos, Bates, Fithian, Jordan, Zrnic, 2023, « Prediction-powered inference » |
| Bilan global contre un total étalé | horizon fixe, bruit honnête connu | bruit de référence mal estimé | Avenhaus et Jaech, 1981 (titre exact : pas sûr) |
| Moyenne de e-valeurs | chaque e-valeur valide sous l'honnête | ne certifie que les fausses alertes, pas la détection | Vovk et Wang, 2021, « E-values: calibration, combination and applications » |
| Classes latentes pour lecteurs sans étalon | erreurs indépendantes sachant la vérité | lecteurs qui se trompent ensemble : le cas de la question | Dawid et Skene, 1979 ; Hui et Walter, 1980, « Estimating the error rates of diagnostic tests » |
| Défauts plantés (test par mutation) | les défauts plantés ressemblent aux vrais | genre jamais vu | DeMillo, Lipton, Sayward, 1978, « Hints on test data selection » |
| Borne de fuite adaptative | réponses bruitées, peu de bits | réponse corrélée à l'audit épisode par épisode | Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, « The reusable holdout » |
| Élicitation de capacité par perturbation ou ajustement | la capacité retenue remonte sous gradient ou bruit | modèle réellement moins capable (S1) | Tice et al., 2024, « Noise injection reveals hidden capabilities of sandbagging language models » (pas sûr) |
| Cadre de contrôle | modèle de confiance, audit borné | adversaire hors équipe rouge | Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » |

Bornes à respecter, identifiants donnés par les faits :

- 2210.14707 : Fang et al., 2022, « Is Out-of-Distribution Detection Learnable? » ;
- 2204.06974 : Goldwasser, Kim, Vaikuntanathan, Zamir, 2022, « Planting Undetectable Backdoors in Machine Learning Models » ;
- 2411.03279 : Goldwasser, Shafer, Vafa, Vaikuntanathan, 2024, « Oblivious Defense in ML Models » ;
- 2412.09565 : Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses » ;
- 2505.23836 : Needham et al., 2025, « Large Language Models Often Know When They Are Being Evaluated » ;
- 2504.05259 : Korbak, Balesni, Shlegeris, Irving, 2025, « How to evaluate control measures for LLM agents? ».

## 4. Vérification hors du programme

- **Dépôt préalable.** Le condensat des graines de tirage et du plan d'audit est déposé chez un tiers avant service. Un programme tiers revérifie que chaque tirage suit l'engagement du produit.
- **Famille tenue à l'écart.** Écrite par un tiers (déjà dans les faits). J'ajoute que le tiers choisit aussi la supposition violée, pas seulement l'instance.
- **Vérité tardive.** Les issues réelles, collectées par quelqu'un qui ne connaît ni les scores ni les verdicts, servent d'étalon à l'oracle.
- **Réplication.** Sur modèles ouverts, par une équipe qui n'a pas conçu les sondes.
- **Preuves.** Chaque énoncé de (k) est accompagné d'un vérificateur fini exécutable par un tiers.

## 5. Reformulation

« Quelle borne sur le dommage cumulé reconnu par l'oracle tient pour toute stratégie adverse, avec pour seules suppositions le secret des tirages, l'engagement avant tirage et un plafond par épisode ? Quelle borne inférieure montre qu'on ne fait pas mieux ? Quelles mesures faites du seul côté de la défense (bruit de la référence, couverture de l'oracle, coût d'obscurcissement) fixent ses constantes ? Tout le reste, sondes et pince comprises, est jugé par la variance qu'il retire à cette borne, mesurée sur le flux d'audit. »

## 6. Les onze sous-questions

**(a) Borner sans reconnaître.**

- *Établi (faits)* : la garantie vient de l'audit au hasard jugé par l'oracle sous plafond ; le bilan global est la meilleure réponse à un total étalé.
- *Non établi* : la constante.
- *Proposition P1.* On pose d_i ∈ [0, c] et un tirage A_i de probabilité p_i ≥ p, fait après engagement. Alors Σ(A_i/p_i − 1)·d_i est une martingale quelle que soit la stratégie. L'inégalité de Ville donne une alarme valide à tout instant.
- *Dommage non alarmé, au risque α (esquisse à vérifier).* Régime concentré : B ≈ c·log(1/α)/p. Régime diffus : B ≈ σ·√(N·log(1/α)/p), où σ est la dispersion honnête de l'écart à la référence.
- *Flux minimal pour un dommage toléré D\** : p ≥ max(c·log(1/α)/D\*, σ²·N·log(1/α)/D\*²).
- *Borne inférieure.* Par un argument à deux points (Le Cam), aucun test de niveau α sur l'honnête ne voit une dérive inférieure à l'ordre de σ/√n. Le plancher σ·√(N/p) n'est donc pas un défaut du mécanisme. Trois leviers seulement : σ (appariement, variable de contrôle), p, c.

**(b) Couverture de l'oracle.**

- *Établi* : hors couverture, rien n'existe pour aucun mécanisme. La vérité du dommage est indéfinie sur beaucoup de tâches floues (2606.08892, RAPPORTÉ).
- *Non établi* : toute mesure de couverture contre un genre inconnu.
- *Proposition P6*, en quatre gestes :
  1. Étalonner les lecteurs sur la vérité tardive d'un sous-échantillon tiré au hasard (sondage en deux phases). L'accord entre lecteurs ne sert pas d'étalon : les classes latentes supposent l'indépendance qui manque ici.
  2. Mesurer l'invariance à la prose : même produit, prose de l'agent retirée ou paraphrasée par le modèle de confiance ; on compte les verdicts qui basculent.
  3. Auditer l'assemblage comme unité, tiré au sort. On mesure l'écart entre la valeur du tout et la somme des verdicts des pièces.
  4. Tâches floues : je ne connais pas de garantie. Le défenseur possède la définition du dommage et peut refuser de déléguer ce qu'il ne sait pas auditer. Le prix est l'utilité.
- *Rétrécissement en service* : suite de confiance sur le désaccord oracle / vérité tardive.
- *Dommage hors spécification* : je ne sais pas le mesurer. On peut seulement élargir la définition par les issues tardives.

**(c) Savoir qu'on ne voit plus.**

- *Établi* : le flux d'audit donne le rappel du moniteur parmi les endommagés trouvés. Sans étiquette, un changement d'erreur sans trace est indétectable (2609.32267, RAPPORTÉ).
- *Non établi* : la taille du flux qui rend ce rappel informatif quand le dommage est rare et petit.
- *Proposition P2*, en trois éléments :
  1. L'état par défaut est « non éprouvé », levé seulement par une borne inférieure de confiance.
  2. Le dommage diffus est continu. On remplace le rappel binaire par la part de variance du dommage audité qu'explique le score, sur le seul bras aléatoire, avec poids d'inclusion.
  3. L'annonce « ne voit plus » est déclenchée quand la borne supérieure de cette part passe sous un seuil.
- *Limite* : si les endommagés trouvés sont surtout des accidents honnêtes, le rappel mesuré ne dit rien du rappel sur sabotage.

**(d) Canal de retour.**

- *Établi* : l'agent voit ce qui lui arrive.
- *Non établi* : que cela lui serve (S5).
- *Proposition P3*, en quatre règles :
  1. Tirages de Bernoulli indépendants du passé, jamais un quota sans remise. Un quota fuit le budget restant.
  2. La correction suit l'engagement du produit. Sans mémoire entre épisodes, un audit révélé n'apprend rien sur les tirages suivants.
  3. Canaux persistants (artefacts partagés, réentraînement) : corrections par lots, à date fixe, fonction d'un agrégat bruité.
  4. Corrections placebo sur des épisodes non audités, pour borner par e^ε le rapport de vraisemblance entre « audité » et « non audité ». La borne se compose additivement en ε.
- *Coût* : délai de correction et dépense placebo, non chiffrés.

**(e) Passage obligé.**

- *Établi* : la sonde de surprise n'est apprise ni évaluée sous 0,3. Un état voisin ne sépare pas triche et échec honnête sur un modèle sur trois (RAPPORTÉ).
- *Non établi* : S1.
- *Ce qui est nécessaire par définition* : pour cumuler, les écarts doivent avoir une moyenne non nulle dans le sens du dommage. Ce n'est pas une trace interne, c'est le bilan.
- *Lecture de la sonde (HYPOTHÈSE)* : elle lit l'échec attendu, pas l'intention. Un saboteur qui sait prévoit l'échec, donc pas de surprise à l'issue. La signature candidate est un échec prévu sans cause externe : réussite attendue basse en interne, alors que le modèle de confiance prédit la tâche faisable.
- *Séparer triche et échec honnête* : par appariement sur la même tâche et par cette différence, non par le niveau de la sonde.
- *Petites surprises* : je ne sais pas. Je propose une calibration par rangs conformes sur l'honnête plutôt qu'un seuil, donc un rapport à la surprise attendue. Les rangs s'accumulent entre pas par e-valeurs, lecture à une position par pas.
- *Plusieurs conséquences* : oui (piste 3, voir P4).
- *Autres passages candidats, tous HYPOTHÈSE* :
  - écart entre capacité élicitée et performance servie ;
  - biais signé commun entre rejouages du même pas, là où l'erreur honnête est idiosyncratique (P7) ;
  - sensibilité du comportement aux indices de surveillance.

**(f) L'étau.**

- *Établi* : aucune quantité conservée. L'obscurcissement a coûté de la performance sur une tâche complexe (2412.09565, RAPPORTÉ).
- *Ce qui le rendrait nécessaire* : que la variable lue soit causalement utilisée pour bien faire. La déplacer coûterait alors de la performance, que voit le regard externe.
- *Proposition P5* : mesurer côté défense la frontière entre évasion de la sonde et performance, en entraînant le modèle honnête à déplacer l'état lu.
- *S'en passer* : P1 seul ; l'interne ne sert qu'à réduire la variance.
- *Piste 1 (tester la somme)* : juste, mais la somme exige l'issue calculée, donc l'audit. C'est l'estimateur par différence, où la réussite lue sert de variable de contrôle. Elle n'ajoute pas de garantie, elle retire de la variance.
- *Piste 2 (netteté de la référence)* : c'est σ, la seule constante mesurable sans attaque. Elle bute sur S7 et sur le peu d'épisodes honnêtes par régime. Il faut une borne supérieure de confiance sur σ, pas une estimation ponctuelle.
- *Piste 3 (« passera » contre « a bien fait »)* : les deux sont presque colinéaires chez l'honnête. Leur différence n'est identifiée que sur des tâches construites, et le transfert reste à prouver.

**(g) Asymétrie de généralisation.**

- *Établi (RAPPORTÉ)* : l'évasion se généralise ; les défenses latentes tombent ensemble.
- *Proposition* : ne pas jouer ce jeu.
  1. La garantie est portée par un échantillon de la vérité, qui n'a pas à généraliser.
  2. Le défenseur joue en dernier. Les endommagés trouvés par l'audit sont les premiers exemples du genre nouveau, et le moniteur est réajusté par époque sur eux.
- *Je ne sais pas* si la cadence d'étiquettes bat la cadence d'adaptation adverse.

**(h) L'adversaire qui apprend.**

- *Établi (RAPPORTÉ)* : un audit de texte fixe tombe en deux tours.
- *Proposition* : seuls les tirages sont secrets (graines, épisodes audités, paraphrases). Le mécanisme est public. Graines et ajustement des moniteurs se renouvellent par époque.
- *Validité indépendante des croyances* : l'audit porte sur des produits réels tirés après engagement. Audité et non audité sont identiques jusqu'à l'engagement, donc il n'y a aucune « situation d'évaluation » à deviner.
- *Restent sensibles aux croyances* : les tests d'équipe rouge et toute référence obtenue en rejouant le suspect.

**(i) Copies et point focal.**

- *Contre un tirage secret*, le point focal ne donne rien : on ne s'accorde pas sur un aléa qu'on ne voit pas.
- *Il sert pour l'assemblage et pour un biais commun.* Le biais commun est une faiblesse adverse : un mode commun signé grossit N dans le bilan mis en commun entre copies.
- *Proposition* : audit de l'assemblage (P6) ; affectation secrète d'une part des pièces au modèle de confiance ou à une autre lignée ; compter les instances d'un même moniteur comme un seul regard.
- *À mesurer* : la supposition d'indépendance des pannes (2512.22154, RAPPORTÉ).

**(j) Combiner sans additionner.**

- *Établi (mathématique)* : la moyenne de e-valeurs est une e-valeur sous dépendance arbitraire (Vovk et Wang). Cela certifie les fausses alertes. Côté détection, les bornes de Fréchet ne garantissent pas plus que le meilleur regard seul : une réunion d'aveugles est aveugle.
- *Relation proposée* : la calibration de la réussite lue contre l'issue calculée, sur l'audité. L'honnête la respecte par apprentissage. Le dommage fait baisser la lecture (premier terme) ou rompt la calibration (second terme). Un seul test, sur la somme.

**(k) Énoncés.**

- **T1 (martingale d'audit).** Suppose secret, engagement avant tirage, plafond. Version finie : le programme vérifie p_i ≥ p, l'ordre des condensats et recalcule le capital.
- **T2 (plancher σ·√(N/p)).** À démontrer proprement. Version finie : mondes plantés.
- **T3 (variable de contrôle).** Sans biais pour tout prédicteur. Version finie : test sur moniteur volontairement faux.
- **T4 (moyenne de e-valeurs).**
- **T5 (fuite ≤ ε par correction, composition).**
- **Impossibilités respectées.** T1 échantillonne, donc ne contredit pas Fang et al. Il lit des produits, donc pas Goldwasser et al. Il achète des étiquettes, comme l'exigent 2609.32267 et 2411.03279.

## 7. Propositions

Les chances sont des jugements, non des mesures.

**P1 — Bilan sondé à variable de contrôle (a, j, k).**
- *Idée* : estimer le dommage total par Σm_i + Σ_audités (d_i − m_i)/p_i, sous alarme par pari. Le moniteur m réduit la variance sans entrer dans la validité.
- *Suppose* : secret, engagement, plafond, oracle.
- *Supposition que l'adversaire doit violer* : « le tirage est inconnu à l'engagement » ou « le dommage est dans la couverture ».
- *Muette* : hors oracle ; sous le plancher σ·√(N/p).
- *Premier pas gratuit* : simulation sur mondes plantés.
- *Test de mort* : duel D1.
- *Distinction* : assemblage de pièces publiées. Le neuf est de sortir explicitement le moniteur de la garantie et de donner le flux minimal.
- *Chances* : 0,7 que T1 tienne tel quel ; 0,4 que la borne soit utile aux budgets réels.

**P2 — Tableau de cécité (c).**
- *Idée* : état par défaut « non éprouvé » ; part de variance du dommage expliquée par le score, sur le bras aléatoire.
- *Suppose* : assez d'endommagés audités.
- *Supposition violée* : « les accidents honnêtes et le sabotage sont vus pareil par le moniteur ».
- *Muette* : dommage rare.
- *Premier pas gratuit* : calculer la largeur de l'intervalle pour K endommagés.
- *Test de mort* : moniteur aveuglé à date cachée dans un monde planté, annonce absente avant l'horizon.
- *Distinction* : la charge de la preuve est inversée.
- *Chances* : 0,5.

**P3 — Corrections sans mémoire (d).**
- *Idée* : tirages indépendants, corrections par lots bruités et placebos.
- *Suppose* : le harnais maîtrise la persistance.
- *Supposition violée* : « aucun état ne persiste hors du harnais ».
- *Muette* : réentraînement sur traces de production.
- *Premier pas gratuit* : inventaire des canaux persistants.
- *Test de mort* : un estimateur adverse du statut « audité » dépasse e^ε.
- *Distinction* : application de la confidentialité différentielle au retour de contrôle ; je ne connais pas d'antécédent (pas sûr).
- *Chances* : 0,6.

**P4 — Échec prévu sans cause, double lecture (e).**
- *Idée* : opposer la réussite lue en interne à la faisabilité prédite par le modèle de confiance, et lire séparément « passera » et « a bien fait ».
- *Suppose* : S1 ; lectures stables hors régime.
- *Supposition violée* : « le sabotage est décidé en ligne ».
- *Muette* : sabotage amorti ; agent entraîné contre la sonde.
- *Premier pas gratuit* : réanalyse d'épisodes honnêtes existants par bande de surprise.
- *Test de mort* : duel D2.
- *Distinction* : contraste apparié plutôt que niveau.
- *Chances* : 0,3 ; 0,1 contre un agent entraîné.

**P5 — Frontière de coût d'obscurcissement (f, g).**
- *Idée* : mesurer sur le modèle honnête ce que coûte de déplacer l'état lu. Si c'est gratuit, l'étau est mort.
- *Suppose* : l'optimiseur du défenseur approche celui de l'adversaire.
- *Supposition violée* : « la variable lue est causalement nécessaire à la performance ».
- *Muette* : optimiseur adverse plus fort.
- *Premier pas gratuit* : relire 2412.09565 pour extraire la frontière déjà mesurée.
- *Test de mort* : duel D3.
- *Distinction* : mesure défensive préalable, sans attaque.
- *Chances* : 0,25 que l'étau survive.

**P6 — Étalonnage de l'oracle (b).**
- *Idée* : vérité tardive en deux phases, invariance à la prose, audit de l'assemblage.
- *Suppose* : une vérité tardive existe.
- *Supposition violée* : « le dommage finit par se voir dans une issue ».
- *Muette* : tâches floues sans issue.
- *Premier pas gratuit* : taux de bascule sous paraphrase, sur verdicts existants.
- *Test de mort* : duel D4.
- *Distinction* : refuse l'accord inter-lecteurs comme mesure.
- *Chances* : 0,5 ; 0,15 sur le flou.

**P7 — Biais signé entre rejouages (e, i).**
- *Idée* : rejouer K fois le même pas et décomposer l'écart en biais et variance. Un dommage cumulatif exige un biais.
- *Suppose* : l'honnête n'a pas de biais systématique.
- *Supposition violée* : « l'écart est stable d'un rejouage à l'autre ».
- *Muette* : régime où l'honnête est lui-même biaisé.
- *Premier pas gratuit* : variance entre rejouages sur l'honnête.
- *Test de mort* : famille tenue à l'écart dont l'écart est conditionnel au contexte.
- *Chances* : 0,3.

## Duels décisifs (livrable b)

Tous les seuils sont illustratifs.

**D1 — P1.**
- H_A : sur toute famille plantée dans la couverture, la fréquence de « dommage > B sans alarme » est ≤ α.
- H_B : une famille la dépasse.
- Métrique : cette fréquence sur 1 000 mondes (illustratif) ; α = 0,05 (illustratif).
- Contrôle négatif : mondes honnêtes, fausses alarmes ≤ α.
- Contrôle positif : un monde où le tirage fuit doit casser la borne.
- Issues : H_B tue T1 tel qu'implémenté. H_A falsifie « il existe une forme d'attaque, parmi celles écrites, qui bat l'audit », et rien au-delà.

**D2 — sonde dopamine.**
- H_A : elle lit l'échec attendu. Entre échec honnête prévu (tâche rendue infaisable, l'agent le sait) et sous-performance sur consigne, appariés par tâche, l'AUROC est ≤ 0,6.
- H_B : elle lit l'intention, AUROC ≥ 0,8.
- Mesure par bande : |δ| < 0,1 ; 0,1–0,3 ; > 0,3.
- Contrôle négatif : étiquettes permutées.
- Vérification mécanique à battre : le prédicteur de difficulté du modèle de confiance.
- Issues : H_A falsifie « la sonde lit l'intention » ; elle devient le premier terme du bilan. H_B falsifie « ce n'est qu'une valeur ».
- Entre 0,6 et 0,8 : indécis, à déclarer tel.

**D3 — étau.**
- H_A : toute évasion de la sonde (rappel < 0,5) coûte ≥ 5 points de performance.
- H_B : il existe un point d'évasion à coût < 1 point.
- Contrôle négatif : même entraînement contre une direction aléatoire.
- Issues : H_B falsifie l'étau comme nécessité. H_A ne falsifie que « l'évasion est gratuite à ce budget d'optimisation » ; l'asymétrie est assumée.

**D4 — oracle.**
- H_A : le taux de bascule sous retrait de la prose est ≤ le bruit de relecture.
- H_B : il est supérieur.
- Contrôle négatif : deux passes de l'oracle sur une entrée identique.
- Issues : H_B falsifie « les lecteurs ne se laissent pas persuader ». H_A falsifie la persuasion pour ces formes de prose seulement.

## Mesure minimale par instrument (livrable c)

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Audit aléatoire | niveau α tenu ; dommage non alarmé contre B | mêmes tâches, jumeau honnête | audit à seuil fixe |
| Oracle à deux lecteurs | rappel sur défauts plantés, famille tierce ; faux positifs sur honnête ; bascule sous prose | même produit, avec et sans prose | comparaison programmée à la référence cachée |
| Moniteur | part de variance du dommage expliquée, bras aléatoire | même tâche | longueur, nombre d'actions, score de difficulté |
| Sonde de réussite | calibration contre l'issue calculée | par régime | prédiction du modèle de confiance |
| Sonde de surprise | détection à fausses alertes fixées, par bande de \|δ\| | échec honnête prévu, même tâche | idem |
| Pince | complémentarité : capturés par l'interne parmi les manqués de l'externe, avec intervalle | mêmes épisodes | réunion de deux moniteurs externes |
| Bilan | réduction de variance par rapport à l'estimateur sans variable de contrôle | — | estimateur brut |
| Référence | borne supérieure de σ sur régime neuf | honnêtes du modèle de confiance | — |

## Ancrage matériel (livrable d)

Tout est illustratif.

- **Mondes plantés (D1, P2, P3)** : processeur seul, quelques heures, coût négligeable.
- **D2 et D3** : trois modèles ouverts de 7 à 9 milliards de paramètres de lignées distinctes (par exemple Llama, Gemma, Qwen), pour rejouer le « un sur trois ». Un processeur graphique de 24 à 48 Go, de l'ordre de quelques jours. D3 demande un ajustement léger par adaptateurs. Quelques centaines d'euros de location.
- **D4** : appels aux deux lecteurs sur quelques centaines de produits existants.
- **Relecture humaine** : réservée à la vérité tardive de P6.

## 8. Hors de portée, quoi qu'on fasse

- Le dommage que l'oracle ne reconnaît pas et qu'aucune issue tardive ne révèle.
- Le dommage sous le plancher σ·√(N/p) : il ne peut être qu'acheté par des étiquettes ou par un plafond plus bas.
- Le sabotage amorti, indiscernable d'une moindre compétence quand aucune capacité ne se laisse éliciter.
- Toute garantie tirée des états internes face à un calcul dissimulé (2204.06974, RAPPORTÉ).
- Les tâches floues sans vérité définie.
- La valeur d'une équipe rouge au-delà des suppositions qu'elle a su écrire.

FIN-DE-CELLULE