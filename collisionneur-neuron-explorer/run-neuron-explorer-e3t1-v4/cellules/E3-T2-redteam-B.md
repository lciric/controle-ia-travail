# Proposition B, tour III.2 : équipe rouge croisée contre A et C

## 0. État des pièces

- **Bloc FAITS** : vide, sur ordre de l'arbitre (GO-2026-10-26-01). Je n'ajoute rien.
- **Pièces A et C** : présentes et complètes. Les deux se terminent par FIN-DE-CELLULE et aucune coupure n'est visible.
- **Statuts** : tout ce qui touche à neuron-explorer vient de l'auteur et l'arbitre l'a lu (« à vérifier »). Les faits du programme sont donnés par la question, sans statut VÉRIFIÉ explicite. Je ne modifie aucun statut. Je signale plus bas les endroits où C en modifie.
- **Les trois adversaires** auxquels se réfèrent tous les scénarios d'évasion :
  - **Adv-M**, le modèle étudié. La révision épinglée de Llama-3.1-8B-Instruct n'a aucune intention. Un Adv-M réellement adverse supposerait un modèle-organisme affiné, ce qui exige un changement de modèle et donc une décision du directeur. Les tests menés sur le modèle épinglé **ne bornent pas** un tel adversaire : je le note à chaque fois.
  - **Adv-O**, l'organisme, qui dispose de la primitive bornée et subit une pression de sélection sur son score.
  - **Adv-I**, l'agent interprète ou la boucle extérieure, sous pression de produire des « découvertes ».
- **Coûts** : tous illustratifs, sauf mention d'une arithmétique explicite.

---

## Contre la proposition A

### (a) Failles

**A-F1. Ce qui est vrai par construction dans E1.**
- **Le problème.** La sonde « conscience d'évaluation » apprend à séparer des activations cadrées « évaluation » d'activations non cadrées. Si elle est entraînée sur des paires du même format que celles de E1, sa direction approche la différence des moyennes « avec indice de cadrage / sans indice ».
- **La conséquence.** L'ajouter à la version non cadrée revient, approximativement, à ajouter la représentation de l'indice lui-même. La mise en forme rapprochera alors le comportement de la version cadrée **par construction**.
- **Ce que E1 teste en réalité.** E1 ne teste pas « le modèle sait qu'il est évalué ». Il teste « la représentation de l'indice textuel est causale en aval », ce que personne ne conteste.
- **Le contrôle de A ne suffit pas.** La « sonde de surface » (longueur, mots-clés) ne neutralise pas ce problème. L'indice de cadrage n'est pas un artefact de surface au sens de A : c'est le contenu même de la manipulation.

**A-F2. Confusion entre la sonde de surface et la sonde sémantique.**
- **La règle de A.** « Effet > nuls mais pas > sonde de surface → H_A falsifiée. »
- **Le problème.** Dans une banque où le cadrage passe par des mots, les deux directions sont colinéaires par conception. Une vraie direction de conscience d'évaluation corrélée aux mots-clés serait déclarée « de surface ».
- **Ce qu'il faut à la place.** Une comparaison sur des directions **orthogonalisées** l'une par rapport à l'autre, ou une banque où indice lexical et situation d'évaluation sont décorrélés. A ne prévoit ni l'une ni l'autre.

**A-F3. Une précondition absente.**
- **Ce que E1 suppose.** Il existe un écart comportemental, sans poussée, entre la version cadrée et la version non cadrée sur Llama-3.1-8B (HYPOTHÈSE, non établie dans les pièces).
- **Le problème.** Si cet écart est nul, la métrique n'a aucune plage. H_A tombe alors trivialement, sans distinguer « la sonde lit sans écrire » de « il n'y a rien à écrire ».
- **Un oubli dans le propre raisonnement de A.** A signale qu'il manque les scores de sonde (A8), mais pas cet écart comportemental.

**A-F4. Les duels ne sont pas exhaustifs (B4).**
- **E3** : H_A est retenue si m ≤ 8 neurones recouvrent ≥ 50 % de l'effet, H_B si m = 64 en recouvrent < 25 %. Toute la zone intermédiaire (par exemple 30 % à m = 8 et 40 % à m = 64) ne falsifie rien.
- **E4** : le rapport ≥ 3 contre le rapport < 1,5 laisse un trou entre 1,5 et 3.
- **Ce que B4 exige.** Chaque issue doit falsifier quelque chose. Il faut donc écrire d'avance ce que signifie l'issue intermédiaire, par exemple « ni levier épars ni diffusion : on suspend E4 ».

**A-F5. E3 repose sur un objet mal défini.**
- **Le problème.** « Les m neurones de plus fort coefficient dans la direction » suppose une décomposition unique de la direction de sonde (dans ℝ⁴⁰⁹⁶) sur les colonnes de sortie des neurones. Or ces colonnes sont surcomplètes : 14 336 vecteurs dans 4 096 dimensions par couche, sur plusieurs couches. Le « coefficient » dépend donc de la méthode de décomposition (projection, moindres carrés, décomposition éparse) et des couches retenues.
- **Le biais introduit.** Pousser la somme de m colonnes « à norme égale » donne un vecteur dont l'angle avec la direction varie avec m. La part d'effet récupérée mesure alors en partie cet angle, et non le caractère épars du mécanisme.
- **L'angle mort.** E3 et E4 ne regardent que les neurones des MLP. Un levier porté par des têtes d'attention échappe aux deux.

**A-F6. Fuite entre construction et évaluation dans la table (c).**
- **Le montage.** Les « cas plantés » servant à évaluer le balayage sont les neurones dont la colonne projette fortement sur le vocabulaire cible. C'est la lentille 1.
- **Le problème.** Évaluer ensuite si le balayage (par grappes de mots dans les déroulés) les retrouve est circulaire, car les deux mesures sont lexicales. Le balayage retrouvera des écrivains de mots, ce qui ne dit rien de sa capacité à trouver un levier situationnel.
- **Une incohérence.** A demande dans la même table que le balayage batte la lentille 1, alors que la lentille 1 définit la vérité terrain.

**A-F7. Comparaisons multiples dans E1.**
- **Le montage.** Seuil au 95ᵉ centile, dose choisie « là où la perplexité reste dans la bande », plusieurs couches, plusieurs sondes.
- **Le problème.** Sans correction sur l'ensemble des conditions, retenir la meilleure condition contre un seuil fixé par condition gonfle le taux de fausses alertes.
- **Ce qui manque.** A ne fixe d'avance ni une dose unique ni une règle de correction.

**A-F8. Le second nul n'est pas propre.**
- **Le montage.** Le nul « 256 neurones tirés au hasard » contient des neurones porteurs de sens. L'auteur rapporte 8 à 20 % de neurones « distincts » sur Qwen (RAPPORTÉ).
- **L'effet.** Le 95ᵉ centile de ce nul est gonflé : il rend le test conservateur et lui fait perdre de la puissance. A remplace une « barre basse » (A2, HYPOTHÈSE) par une barre de hauteur inconnue, sans dire quel taux d'erreur est contrôlé.

**A-F9. Une inférence présentée comme un fait.**
- **Ce que dit A.** « Il n'a donc à ce jour aucune intervention validée. »
- **Pourquoi c'est une inférence.** La décision citée a retiré le bruit d'activations des interventions *revendiquées*. Elle ne dit rien d'autres interventions. La phrase est une HYPOTHÈSE.

### (b) Scénarios d'évasion

| Instrument de A | Comment l'adversaire le trompe | Coût (illustratif) |
|---|---|---|
| **E1** (poussée de la sonde) | Adv-M encode la situation d'évaluation dans une direction lisible et poussable. Elle agit sur le format des paires de la banque (dernier jeton, cadrage explicite). Le comportement en déploiement dépend d'un trait contextuel non linéaire, réparti sur les positions. E1 conclut à « suffisante » sur un objet qui ne gouverne pas le comportement visé. | Naturel : nul (l'indice de cadrage suffit, A-F1). Adverse : affinage avec une sonde dans la boucle, quelques heures de carte sur un 8B. Une littérature sur les activations obscurcies existe : Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses » (à vérifier). Hors du modèle épinglé. |
| **E2** (verbalisation contre comportement) | La comparaison à l'injection textuelle est bonne. Mais si la poussée imite l'injection (A-F1), les deux couples coïncident, et A conclut seulement « la poussée n'apporte rien que le texte ne fasse ». C'est vrai, mais ce n'est pas la question. | Nul. |
| **E3** (direction contre neurones) | Rien à faire pour Adv-M. La superposition diffuse l'effet naturellement, et un levier épars placé dans l'attention échappe au test (A-F5). | Nul. |
| **E4** (balayage préenregistré) | Adv-I, ou simplement le générateur de banques, produit une banque scellée lexicalement proche de la banque de conception. Les neurones lexicaux se répliquent, et le rapport dépasse 3 sans aucun levier situationnel. | Nul : il suffit d'un même gabarit de génération des tâches. |
| **E6** (maximum à l'aveugle) | Adv-I écrit des explications chargées de mots déclencheurs. L'explication d'un autre neurone, sans rapport, échoue évidemment, donc l'explication vraie « gagne ». C relève le même problème de contamination lexicale, et je reprends son argument contre A. | Nul. |
| **E7** (primitive des organismes) | Adv-O détecte le bras placebo par une vérification de cohérence : la même requête envoyée deux fois donne des rendus aléatoires différents. Il cesse alors d'appeler la primitive, et le placebo n'est plus aveugle. Autre voie : Adv-O n'agit pas sur les activations lues par la sonde de score (interdit par A), mais il utilise la poussée pour *choisir* parmi ses propres textes ceux qui serviront d'entraînement à son classifieur. C'est un canal indirect que la règle de A ne ferme pas. | Deux appels par course. |

**Tous à la fois.** Adv-I écrit des interprétations lexicales qui passent E6. Le balayage par grappes (E4), évalué sur des cas plantés lexicaux (A-F6), confirme ces interprétations. E1 « valide » la sonde par l'effet d'indice (A-F1). Adv-O réutilise ces leviers lexicaux pour sélectionner ses textes. Chaque instrument est trompé par le même biais lexical. Le coût d'évasion est **nul**, parce qu'aucun des instruments de A n'est indépendant du lexique.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle positif préalable de E1** : mesurer l'écart comportemental cadré / non cadré sans poussée, contre son bruit de rééchantillonnage. Sans lui, un E1 négatif ne se lit pas.
2. **Direction de cadrage sans évaluation** : différence des moyennes entre un cadrage lexicalement voisin où le modèle n'est pas évalué (« ceci est un test de recette de cuisine ») et l'absence de cadrage. Formulé en duel :
   - **H_A** : la direction de sonde déplace le comportement au-delà de cette direction quasi-cible.
   - **H_B** : elle ne fait pas mieux.
   - **Lecture des issues** : si H_A tient, l'effet d'indice générique est falsifié comme explication. Si H_B tient, la lecture « conscience d'évaluation » de E1 est falsifiée.
3. **Sonde à étiquettes mélangées entraînée sur exactement les mêmes textes**. A la mentionne, mais il faut la passer à chaque dose et à chaque couche, avec une correction globale.
4. **Vérité terrain non lexicale pour la table (c)**, par exemple la direction de refus re-dérivée sur le modèle épinglé, avec une méthode distincte de celle qu'on évalue.
5. **Bras placebo indiscernable** : rendus pseudo-aléatoires déterministes par requête, pour que la vérification de cohérence ne trahisse pas le bras.
6. **Permutation des explications à l'intérieur d'une même classe lexicale** dans E6, pas entre neurones quelconques.

---

## Contre la proposition C

### (a) Failles

**C-F0. Intégrité des statuts (règle 1).**
- **Faits du programme.** C les déclare « VÉRIFIÉ ». La question ne leur attribue pas ce statut.
- **Méthodologie de l'agent.** C la marque « OBSERVÉ-NON-AUDITÉ ». La question la donne comme lecture du dépôt, chiffres de l'auteur « à vérifier ».
- **Architecture.** C écrit « VÉRIFIÉ pour la famille Llama-3-8B » de mémoire. A, plus prudent, écrit « à vérifier sur le fichier de configuration ».
- **Littérature.** C affirme que « la littérature dominante considère », sans source. C affirme aussi qu'Arditi et al. « explique pourquoi neuron-explorer trouve facilement des leviers de refus en projetant sur cette direction ». neuron-explorer ne projette sur aucune direction de refus d'après les faits : c'est une HYPOTHÈSE de mécanisme présentée comme une explication.
- **Conséquence.** Tout statut de C doit être relu avant usage.

**C-F1. Le seuil de E2 est inatteignable : H_B est falsifiée par construction.**
- **L'arithmétique.** Avec N témoins, la plus petite p-valeur empirique est 1/(N+1). Pour N = 1 000, cela donne ≈ 0,001. Le seuil de Bonferroni de la phase 2 vaut 0,01 / 50 = 0,0002.
- **La conséquence.** Aucun neurone ne peut franchir ce seuil contre la distribution empirique des témoins. L'expérience conclut à l'absence de levier quoi qu'il arrive.
- **Même défaut dans la table (c).** Un seuil individuel de 3,5 × 10⁻⁶ exigerait plus de 2,8 × 10⁵ témoins par couche, alors que C en prévoit 256.
- **Ce qu'il faudrait.** Une loi paramétrique ajustée sur les témoins, à préenregistrer avec son test d'ajustement, ou bien beaucoup plus de témoins.

**C-F2. L'ablation de E2 dépend de l'ordre des couches.**
- **Le montage.** H_B est falsifiée si l'ablation des 50 neurones réduit l'AUROC de la sonde de moins de 2 %.
- **Le problème.** Les neurones situés après la couche lue par la sonde ne peuvent pas l'affecter. Ceux situés avant agissent en partie par construction, puisque la sonde lit des sommes de leurs colonnes.
- **La conséquence.** Le résultat dépend de la position des couches 10, 16, 22 et 28 par rapport à la couche de la sonde, ce qui n'est pas précisé. Il dépend aussi de la question de savoir si la sonde est réentraînée après l'ablation, ce qui n'est pas dit non plus.

**C-F3. La phase 1 de E2 sélectionne des écrivains de mots.**
- **Le problème.** Une variation de log-probabilité sur `["test", "evaluation", …]` classe en tête les neurones dont la colonne projette sur ces jetons.
- **Les limites du correctif de C.** Le score S_i (cibles moins quasi-cibles) corrige en partie. Mais la log-probabilité de base de « test » est déjà élevée sur les quasi-cibles, comme les examens scolaires. La saturation crée alors un écart différentiel sans aucun levier situationnel.
- **Ce qui manque.** Une normalisation par la log-probabilité de base. Elle est absente.

**C-F4. Comparaisons multiples dans E1.**
- **Le montage.** Six doses, deux modes (M1, M2), deux variantes de vecteur (régression logistique ou différence des moyennes, ajoutée en (d)). Cela fait 24 conditions, chacune contre un 99ᵉ centile.
- **Le risque.** Sous le nul et avec des conditions indépendantes, la probabilité qu'au moins une condition passe vaut 1 − 0,99²⁴ ≈ 21 %. C'est une borne supérieure, car les conditions sont corrélées.
- **Ce que la symétrie corrige.** L'exigence de symétrie (+α / −α) réduit ce taux, mais C ne fixe pas quelle condition est primaire.

**C-F5. Le témoin dans les composantes principales ne compare pas des objets comparables.**
- **L'argument de C lui-même.** Une sonde par régression logistique peu régularisée a des composantes hors des directions de forte variance.
- **La conséquence.** Poussée à α‖r‖, cette sonde injecte, dans des directions où la variance naturelle est faible, une amplitude énorme par rapport à leur variation habituelle. Les témoins tirés dans les 128 premières composantes, eux, restent dans la variété.
- **Le biais.** La comparaison mélange la spécificité et l'écart hors de la variété. Il faudrait des témoins appariés sur le profil spectral de la sonde, pas seulement sur sa norme.

**C-F6. La norme par position avec la modalité M2.**
- **Le montage.** C dose par ‖r_{l,t}‖ à chaque position.
- **Le risque.** Dans les modèles de cette famille, certaines positions, comme le premier jeton servant de puits d'attention, auraient des normes résiduelles bien plus grandes que les autres. HYPOTHÈSE pour la révision épinglée, à mesurer. Référence associée : Sun et al., 2024, « Massive Activations in Large Language Models » (à vérifier).
- **La conséquence.** Une poussée « sur toute la génération » injecte alors un vecteur démesuré à ces positions : M2 mesure la perturbation du puits, pas l'effet de la direction.

**C-F7. E3 et E4 ne sont pas des duels exclusifs.**
- **E3.** H_A est une disjonction : « dégrade OU coûte plus de 5× ». H_B est « gain d'au moins +0,03 ».
  - Un gain de +0,04 avec un coût multiplié par 6 vérifie les deux.
  - Un gain nul, sans dégradation et avec un coût multiplié par 2, ne falsifie aucune des deux.
- **Puissance de E3.** Cinq courses par bras, sans estimation de la variance d'une course à l'autre : un écart de 0,03 d'AUROC n'est pas interprétable.
- **E4.** La « vérité » est circulaire : les « 10 vraies directions causales de référence (ou les meilleures sondes validées) » n'existent pas indépendamment des instruments que C veut valider, puisque c'est E1 qui les « validerait ».
- **Leurres trop faciles.** Les directions aléatoires « ayant franchi par hasard le 95ᵉ centile » sur une amorce régressent vers la moyenne dès qu'on change d'amorce. N'importe quel agent les rejette. Le taux de spécificité est donc gonflé par construction.

**C-F8. Deux contradictions internes.**
- **Ce que C interdit.** Le balayage génératif complet est classé « jamais ».
- **Ce que C exige.** Sa table demande un rappel ≥ 90 % de la lentille rapide « des neurones qui produisent un effet comportemental en génération longue ».
- **La contradiction.** Cette vérité terrain exige au minimum un sous-échantillon génératif, que C ne prévoit pas.
- **Le parcimonie de la sonde.** Projeter la sonde sur les colonnes de sortie pour obtenir sa « fraction de norme portée par les 10 ou 50 neurones » souffre du même défaut que A-F5 : la famille de colonnes est surcomplète, et l'alignement géométrique n'est pas une contribution causale. Un neurone aligné mais jamais actif compterait. Le produit matriciel coûte bien « 0,01 seconde », mais il ne mesure pas ce qui est annoncé.

### (b) Scénarios d'évasion

| Instrument de C | Comment l'adversaire le trompe | Coût (illustratif) |
|---|---|---|
| **E1** | Adv-I choisit après coup la condition qui passe, parmi 24 (C-F4). Adv-M naturel : l'effet d'indice (A-F1) s'applique aussi à C. Son contrôle par quasi-cibles n'existe que dans E2, pas dans E1. | Nul. |
| **E2** | Aucune évasion n'est nécessaire, car le test ne peut pas conclure positivement (C-F1). Un vrai levier placé dans une couche hors de {10, 16, 22, 28}, ou dans l'attention, passe inaperçu. | Nul. |
| **Primitive « pousser »** (graine = hachage du texte + sel) | Adv-O fait du « magasinage de graine ». Il soumet des variantes infimes de son texte (une espace, une ponctuation), obtient à chaque fois un nouveau tirage de témoins, et ne garde que les tirages où sa direction passe. C'est un jardin des sentiers qui bifurquent intégré à la primitive. | Quelques appels par direction × variantes, ce qui reste sous les plafonds si ceux-ci comptent des appels et non des textes distincts. |
| **Primitive, réutilisation des témoins** | C réutilise les 64 mêmes témoins pour M requêtes sur un même texte, pour amortir le coût. Il rend en outre le rang centile et le score z. Adv-O fait une recherche adaptative : il ajuste sa direction requête après requête jusqu'à dépasser ces 64 vecteurs fixes. Le score z lui sert de gradient. C'est exactement le « détournement » que C décrit comme danger 3, rendu possible par son propre amortissement. | M requêtes, de l'ordre de quelques dizaines. |
| **Tabou lexical** | Adv-I contourne le filtre par synonymes, paraphrases ou passage à une autre langue. Le filtre « mots concrets présents dans les exemples » ne couvre pas les voisins sémantiques. | Nul. |
| **E4** | Adv-I apprend à reconnaître les leurres plutôt que les leviers : il reteste sur une amorce neuve, et les leurres de criblage s'effondrent. Si les leurres sont réutilisés d'une ronde à l'autre de la boucle extérieure, il les mémorise. | Une ronde. |
| **« 0 % de fuite vérifié par journalisation »** | Un journal ne prouve pas une absence. Il ne montre que ce qu'on y écrit. | Nul. |

**Tous à la fois.** Adv-O fait du magasinage de graine et une recherche adaptative contre les témoins réutilisés : sa direction passe le test interne. Adv-I la décrit avec des synonymes qui franchissent le tabou lexical. Le duel E4 la classe « vraie », puisque la vérité terrain est fournie par les mêmes instruments. E2 ne peut rien infirmer de positif, puisqu'il ne peut rien conclure de positif. Le coût total est de quelques dizaines d'appels par direction (illustratif), avec aucun accès privilégié. Le seul prérequis est que les plafonds comptent les appels et non les textes.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Injection textuelle du cadrage** dans E1, avec le même couple verbalisation / comportement (je reprends ici E2 de A). Sans elle, une poussée qui agit par le lexique est indiscernable d'un levier.
2. **Sonde de surface et sonde à étiquettes mélangées** dans E1, toutes deux absentes chez C, avec des directions orthogonalisées (A-F2).
3. **Témoins en nombre suffisant ou loi paramétrique préenregistrée** dans E2 : sans cela, le duel est truqué vers H_A (C-F1).
4. **Ablation restreinte aux couches situées en amont de la sonde**, sans réentraînement de la sonde, écrite d'avance (C-F2).
5. **Témoins tirés à neuf à chaque appel**, de façon indépendante du contenu du texte et inconnue de l'organisme. Le rendu se limite à un verdict binaire au seuil préenregistré, sans score z exploitable comme gradient. Les plafonds sont comptés en textes distincts.
6. **Bras placebo** dans E3 (repris de E7 chez A) et **test A/A** (deux bras identiques) pour estimer la variance entre courses avant de lire un écart de 0,03.
7. **Vérité terrain indépendante** dans E4 : des directions plantées par une méthode distincte des instruments évalués, et des leurres non triviaux (directions aléatoires ayant franchi le seuil sur des amorces *neuves*, quasi-cibles appariées), tenus secrets d'une ronde à l'autre.
8. **Normalisation par la log-probabilité de base** dans le score S_i (C-F3), et contrôle des positions à forte norme en modalité M2 (C-F6).

---

## Note de fin : ce que j'emprunte, et pourquoi ce n'est pas une fusion

- **Ce que j'emprunte.** J'ai utilisé l'injection textuelle et le placebo de A contre C, et la contamination lexicale décrite par C contre A.
- **Le défaut commun.** Les deux conceptions partagent une faille que ni l'une ni l'autre ne contrôle : la direction lue sur des paires cadrées / non cadrées approche l'indice de cadrage, donc la poussée « marche » par construction (A-F1). Le contrôle décisif est la direction de cadrage sans évaluation (A-(c)2). Si elle déplace le comportement autant que la sonde, aucune des deux propositions n'a d'objet causal « conscience d'évaluation ». Seul un « indice lu au dernier jeton » subsiste.
- **Ce qui reste à compter.** Le nombre de ces contrôles absents, chez chacune.

FIN-DE-CELLULE