# Question de l'héritage (N-073, § 1) — plan à trois bras corrigé — v1

- **Statut : pièce de travail, brouillon 1, à contre-lire.** Ce n'est pas un préenregistrement. Rien ici ne s'applique, n'engage une dépense ni ne modifie une pièce scellée. Chaque étage décrit plus bas demande son propre préenregistrement scellé et contre-lu (règles R1 et R2), et l'étage payant un devis et une ligne d'accord neuve.
- **Écrit par** : le rédacteur (modèle F), le 2026-11-19 vers 13:10Z (`date -u`), sur processeur seul, sans appel à un fournisseur de modèles, sans dépense. Contre-lecteur prévu : modèle O.
- **Mandat** : ligne `GO-2026-11-19-55` de `registres/go.md` (mot de Lazar, « les 5 lignes plus la question de l'heritage »), option (c) de la proposition : « corriger le plan à trois bras selon la lettre du complément 3 de N-073, en y versant les bons éléments des cartes (dose plantée avec dose nulle, mondes avec et sans dépendance, répondeur scripté), puis devis ».
- **Pièces lues**, sur `main` (commit `5dbc658f`), empreinte vérifiée pour chacune :
  - plan d'origine : `docs/notes/veille-yu-memoire-v1/lecture-yu-approfondie-v2.md` (`956842550081abbd0292bc082015e782421c919ad0676764ed89721b3cc2e48f`), section (c) ;
  - les trois corrections attendues : `docs/notes/veille-yu-memoire-v1/verification-courte-versions-2-v1.md` (`98d1152f05e3b60568557dca1d01a84ed2343a7505f1d17c0febdea4815e36dd`), section 3, points a, b, d (et c, e) ; registre des décisions, entrées R-3643, R-3663, R-3685 ;
  - lettre : `docs/decisions/decision-N-073-complement-3-memoire-transmise-v1.md` (`4ca0ce7b040b917d9be145134b2b28755a862bfa7a41e4f16d22893129bb03e5`) ; compléments 2 (`5707dbd8bdd8ccc224578be480107723fad6e5054484082c1a1c38d8fa588e8e`) et 1 (`61903909e8aaaa70d6f1aa26a8025104aa3513244b6723daac529048267d4478`) ; N-073 (`b95688df5e695da7dc32ce71321ba205f44debcc0b7410e598c78c2180733ecd`), § 1, 2 et 4 ; N-058 (définition de l'oracle) ; N-067, titres et section 4 parcourus ; N-071, connue par son entrée au registre des décisions (R-3187) seulement ;
  - proposition `docs/notes/organisme-auto-conception-v1/course-v2/proposition-cartes-a-eprouver-v9-v1.md` (`a2cd45adf7c49a90…`), critères (`8881dbb2f63bdfed…`), lecture descriptive de la course v9 (`0306adf74d321cfa…`), sections 1 à 3 ;
  - neuf cartes de la course v9, et elles seules, extraites par leur identifiant de `fiches.json` (`ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`, branche `lot/compte-organisme-v1`) par un petit programme qui retire le champ `meta` : `fed7a993d9671`, `fdfac3afd4bae`, `f0d21fb62aff2`, `f7a4918afe116`, `fc1f059e8873e`, `f7219bb36cfcb`, `f473bb6a03ca3`, `f760c773d6f15`, `f11193560f4d4`. L'espèce des proposeurs n'a pas été lue.
- **Non lus** : le code de l'orchestrateur, de l'oracle et du générateur des mondes plantés ; les décisions N-045 v2, N-049, N-050 et N-053, connues ici par ce que les pièces ci-dessus en citent ; les autres cartes ; tout verdict, tout classement, tout coffre. Les conséquences sont dites au § 13.
- Chaque carte est l'avis d'un proposeur, jamais un fait. Les travaux que les cartes citent ne sont pas repris ici.

## 0. Verdict

1. Le plan tient en trois bras sur le même objet : **un registre des tentatives de l'organisme, hérité d'une course antérieure puis tenu ; le même registre né vide et tenu ; aucun registre**. Les trois corrections attendues (R-3643) sont appliquées aux § 3.1, 3.2 et 3.3.
2. Trois éléments des cartes sont versés : la dose de dépendance plantée avec une dose nulle qui invalide la lecture, les mondes avec et sans dépendance, le répondeur scripté. Ils donnent un **étage sur processeur à 0 USD** qui doit précéder tout appel payant, et qui fixe la taille de l'étage payant.
3. L'étage payant coûte un ordre de grandeur de plus que ce que la proposition annonçait (de 150 à 350 USD) : le plancher de dix sources le porte à plusieurs milliers de dollars selon la composition des proposeurs (devis joint). **Quatre points restent ouverts et sont des nœuds de Lazar** (§ 12).

## 1. L'objet : un registre des tentatives

L'objet est celui que fixe le complément 3 de N-073 : un **registre des tentatives** de l'organisme. Une entrée par problème ; sous elle, une ligne par tentative.

| champ | qui l'écrit | quand | forme |
|---|---|---|---|
| `probleme` | le proposeur | à la proposition | une phrase bornée, ou l'identifiant d'un problème déjà inscrit |
| `tentative` | le proposeur | à la proposition | l'engagement éprouvé (dans un monde planté : la loi engagée, sous la forme que le programme d'épreuve exécute) et une description bornée |
| `justification` | le proposeur | à la proposition | texte borné |
| `prediction` | le proposeur | à la proposition, **scellée par son empreinte avant toute épreuve** | une probabilité par classe d'issue, sur une liste fermée (§ 3.2) |
| `resultat` | **l'orchestrateur, par programme** | après l'épreuve | la classe d'issue de l'épreuve programmée de cette tentative, et son coût mesuré (§ 3.1 et 3.2) ; aucun texte |
| `gardee` | l'orchestrateur, par programme | après l'épreuve | oui ou non, par une règle écrite sur `resultat` et le coût seuls |
| `provenance` | l'orchestrateur | à l'écriture | génération, source, version de l'orchestrateur, empreinte de la configuration |

Le registre est en ajout seul, chaîné par empreintes et scellé à chaque génération ; les tentatives non gardées y restent. Les longueurs, la liste fermée des classes et la règle de `gardee` se gèlent au préenregistrement.

Ce que le registre ne contient jamais : un verdict, un score ou un texte d'un juge à modèle ; une liste, un rang ou un compte de cartes promues ou survivantes ; une valeur tirée de la clé du monde planté ; un identifiant ou un nombre d'items plantés ; quoi que ce soit du monde de la mesure finale.

## 2. Les trois bras

Pour chaque **source** indépendante — une course antérieure de l'organisme sur un monde planté, pendant laquelle il a tenu un registre né vide —, trois continuations partent du même organisme, sur la même suite de mondes plantés neufs :

| bras | registre au départ | registre pendant la continuation |
|---|---|---|
| 1 — aucun registre | aucun | aucun |
| 2 — registre né vide et tenu | vide | tenu et servi |
| 3 — registre hérité puis tenu | celui de la source | tenu et servi |

- **Bras 3 moins bras 2 : l'héritage**, c'est-à-dire ce que le registre reçu de la source ajoute au fait d'en tenir un.
- **Bras 2 moins bras 1 : la tenue**, c'est-à-dire ce que tenir un registre ajoute à l'historique ordinaire.
- Bras 3 moins bras 1 : rapporté, sans seuil.

Les sept règles du plan d'origine (section c.4) sont gardées, avec deux précisions :

1. **Même organisme de départ.** Les trois bras partent du code et des consignes de l'organisme tel que la source l'a laissé. Le contraste de l'héritage mesure donc ce que le registre transmis ajoute à un organisme qui hérite déjà par son code. C'est une borne, à écrire dans tout texte.
2. **L'historique de la source est remis à zéro dans les trois bras.** Chaque bras ne garde que l'historique ordinaire de sa propre continuation, sous la même forme. Le seul canal par lequel la source parle, au-delà du code, est le registre du bras 3. Garde éprouvée sur un cas sain et sur un artefact (règle R5) : un historique de départ non vide arrête le lancement.
3. **Le même retour ordinaire dans les trois bras, au même grain.** Ce retour est défini au § 3.2 : la classe d'issue de l'épreuve programmée de chaque tentative, et son coût. Le champ `resultat` ne contient rien de plus fin. Le registre ne change donc que l'accès au passé — rangement par problème, justification, prédiction scellée, provenance, et pour le bras 3 le passé de la source —, non la quantité d'information tirée de l'épreuve. *Précision demandée par la vérification courte (point c)* : si le retour ordinaire de l'organisme d'aujourd'hui est autre chose, le servir aux trois bras change l'organisme ; ce changement se déclare au préenregistrement et s'applique aux trois bras à l'identique. Non vérifié ici (§ 13).
4. **Budget en dollars égal par bras**, et le coût dans le signal rendu à l'organisme, sous une forme gelée et identique dans les trois bras.
5. **Dépense réelle rapportée par bras** ; un bras qui ne dépense pas son budget n'est pas complété.
6. **Le bras qui lit un registre paie sa lecture sur le même budget** : il a donc moins d'appels. La manière de retirer des appels est gelée et la même pour tous : réduction du nombre de lots servis, uniforme sur les espèces et les rôles. *Précision demandée par la vérification courte (point e)* : la règle d'arrondi est gelée — arrondi à l'entier inférieur du nombre de lots par espèce, le reliquat de budget n'étant pas dépensé et étant rapporté.
7. **Cloisonnement entre bras.** Aucun dossier lisible n'est commun à deux continuations. Les trois bras d'une source reçoivent la même suite de mondes (graines des mondes dérivées par source et par génération, communes aux trois bras ; graines d'échantillonnage dérivées par bras ; `numpy.random.SeedSequence`, règle R9).

Longueur : trois générations au moins par continuation, comme au plan d'origine.

## 3. Les trois corrections attendues, appliquées

La vérification courte des versions 2 (section 3) conclut que le plan d'origine ne peut pas fonder un préenregistrement avant trois corrections ; R-3643 les reprend. Les voici, chacune avec le défaut, le choix fait, et ce qu'un essai du code doit tester.

### 3.1 Correction 1 — l'invariant face à l'oracle de N-058

**Défaut.** Le plan d'origine posait : « aucune valeur de la mémoire n'est fonction d'une sortie du juge ». Or N-058 définit l'oracle du monde planté par « structures retrouvées, témoins plantés vrais promus et faux rejetés », et les témoins sont promus ou rejetés par le juge. Les champs `resultat` et `gardee`, écrits depuis le score de l'oracle, violaient donc l'invariant par construction ; pris à la lettre, il n'était pas testable.

**Choix.** Des deux voies que la vérification courte propose, je prends la première, et je la durcis : le registre n'emploie **ni** le volet des témoins jugés, **ni** la clé du monde planté.

- Les champs écrits par programme (`resultat`, `gardee`) sont calculés par une fonction dont les **seules entrées** sont : l'engagement scellé de la tentative, les données du jeu d'évolution du monde en cours, et le journal des coûts. Elle ne reçoit ni une sortie d'un juge à modèle, ni la clé du monde planté.
- Raison du durcissement : un registre qui porterait la réponse de l'oracle (« cette tentative est une loi vraie ») ne peut exister que dans un monde planté. Ce que l'on mesurerait en l'héritant ne dirait rien d'un organisme qui travaille sans oracle. L'épreuve programmée sur les données d'évolution, elle, existe dans les deux cas.
- **L'oracle ne sert qu'à la mesure**, hors de tout ce qui est servi à un agent (§ 6).

**Invariant, dans sa forme corrigée.** « Aucun champ du registre n'est calculé à partir d'une sortie d'un juge à modèle, ni à partir de la clé du monde planté. Les champs écrits par programme ne dépendent que de l'engagement scellé de la tentative, des données d'évolution du monde en cours et du journal des coûts. » C'est la lecture conjointe du point 5 de N-053 et du point 2 de N-058 (aucun score de juge dans la sélection de l'agent), étendue à la clé de l'oracle.

**Ce que l'essai teste** (cas sain et artefact, règle R5) :
- sain : sur un journal de course rejoué, permuter toutes les sorties des juges à modèle, puis remplacer la clé du monde par une autre en gardant les mêmes données d'évolution, laisse les champs écrits par programme **identiques à l'octet** ;
- artefact : une version fautive de la fonction d'écriture, qui lit un verdict de juge ou la clé, fait échouer l'essai ;
- ce que l'essai ne teste pas, et que le texte ne doit pas prétendre : les champs écrits par le proposeur dépendent de ce qu'il a lu, qui peut dépendre de tout. L'invariant porte sur les champs écrits par programme et sur les entrées de la fonction, pas sur la pensée du proposeur.

**Ce qui reste un nœud** (§ 12, point 1) : la garde « la mémoire ne sert jamais un verdict ». La classe d'issue d'une épreuve programmée et le champ `gardee` ne sont pas des verdicts de juge à modèle, et le complément 3 les nomme dans l'objet (« résultats écrits par programme », « gardée »). Mais servis à la génération suivante, ils disent ce qui a tenu. Une carte (`fed7a993d9671`) le relève elle-même comme un point « à trancher par le directeur ». Repli écrit si la réponse est non : `resultat` et `gardee` restent écrits sur disque pour l'analyse et ne sont **pas servis** ; le registre servi ne dit alors que ce qui a été tenté, pourquoi, et avec quelle prédiction.

### 3.2 Correction 2 — la prédiction, son taux de base, et le grain du retour

**Défauts.** (i) La prédiction était un signe et une tranche, donc une catégorie ponctuelle, alors qu'une règle de score propre exige des probabilités. (ii) Le taux de base par permutation entre tentatives est dégénéré si les proposeurs prédisent presque toujours la même chose. (iii) Le « changement du score de l'oracle dû à une tentative » n'a pas d'objet mesurable quand le monde change à chaque génération. (iv) Un score servi sous la forme k sur m laisse lire m, le nombre d'items plantés.

**Choix.**

- **Objet de la prédiction** : l'issue de l'épreuve programmée **de cette tentative, sur les données d'évolution du même monde**. L'objet est défini par tentative, sur un seul monde ; il ne compare plus deux générations. Le défaut (iii) disparaît.
- **Forme** : une probabilité par classe, sur une **liste fermée de classes d'issue** gelée au préenregistrement (proposition : « tient », « ne tient pas », « non exécutable ou indéterminée »), en dixièmes, de somme un. Aucun texte libre, aucun identifiant d'item. Le programme refuse une prédiction mal formée ; il refuse d'éprouver une tentative sans empreinte de prédiction, et d'écrire un résultat dont la prédiction ne correspond pas à l'empreinte (garde éprouvée sur un cas sain et sur une prédiction modifiée après coup).
- **Justesse** : score quadratique à plusieurs classes (Brier, 1950 ; référence classique, non lue sur source au dépôt), qui est une règle de score propre pour cette forme.
- **Taux de base, indépendant des prédictions** : la prévision constante égale aux fréquences des classes observées **dans les autres sources**, même bras (une source laissée de côté à tour de rôle). Seconde référence, rapportée à côté : la prévision uniforme. Aucune permutation des prédictions.
- **Cas dégénéré, dit d'avance** : si plus de neuf prédictions sur dix d'un bras sont identiques, la ligne est rapportée « prédiction non informative » et n'est pas interprétée.
- **Statut** : la justesse des prédictions est **rapportée, sans seuil**, par génération, avec un intervalle par rééchantillonnage des sources. Elle n'entre dans aucun signal de sélection ni de récompense, et dans aucune règle du registre.
- **Grain** : le retour ordinaire et le champ `resultat` portent une **classe par tentative** et un coût. Jamais une fraction, jamais un compte rapporté à un total d'items plantés. Comme la clé du monde n'est pas une entrée de la fonction d'écriture (§ 3.1), m ne peut pas y passer. Le défaut (iv) est fermé par construction, et un essai le garde : la sérialisation du registre et du retour ne contient aucun champ numérique hors des probabilités prédites et du coût.

**Ce que la correction coûte.** La prédiction porte sur l'épreuve programmée, non sur la vérité plantée. Une prédiction juste dit que le proposeur connaît son épreuve, pas qu'il trouve des lois vraies. C'est voulu : la justesse est une description du registre, pas une mesure de découverte.

### 3.3 Correction 3 — le plancher du nombre de sources

**Défaut.** Le plan d'origine faisait dépendre le nombre de sources du seul pilote de bruit. Or le test des rangs signés exact, joint à la procédure de Holm sur deux contrastes, impose un plancher quel que soit le bruit.

**Calcul** (`calcul_devis_heritage_v1.py`, sortie `calcul-devis-heritage-v1.json`, champ `rangs_signes_exact` ; sans différence nulle ni ex æquo) :

| sources | plus petite valeur p bilatérale atteignable | plus grande somme de rangs qui passe 0,025 | plus grande somme de rangs qui passe 0,05 |
|---|---|---|---|
| 6 | 0,03125 | aucune | 0 |
| 7 | 0,015625 | 0 | 2 |
| 8 | 0,0078125 | 2 | 3 |
| 10 | 0,001953125 | 5 | 8 |
| 12 | 0,00048828125 | 10 | 13 |

Avec six sources ou moins, le plan ne peut conclure sur aucun contraste. Avec sept, il ne conclut que si les sept différences ont le même signe.

**Choix.**
- **Plancher : dix sources** à dose de dépendance non nulle, **quel que soit le résultat du pilote de bruit**. Le pilote ne peut que relever ce nombre. Recommandation : douze, pour garder dix différences utiles si des différences sont nulles.
- **Différences nulles** : les scores de l'oracle sont des comptes, donc des différences nulles sont probables. Leur traitement est gelé : méthode de Pratt (1959 ; référence classique, non lue sur source au dépôt) — les zéros sont classés avec les autres, puis leurs rangs sont retirés —, la loi exacte étant calculée par programme sur les rangs restants. Les ex æquo reçoivent le rang moyen, et la loi exacte est énumérée sur les rangs observés.
- **Un seul test décide par contraste** : rangs signés exact, bilatéral, sur les différences appariées par source, **à l'échéance seulement**. Deux contrastes (héritage, tenue), risque global de 5 % par la procédure de Holm (1979 ; référence classique, non lue sur source au dépôt) : la plus petite valeur p est comparée à 0,025, l'autre à 0,05 si la première passe.
- **La conséquence de coût est dite au devis**, et non plus laissée hors devis : c'est elle qui fait la taille de l'étage payant.

## 4. Ce qui vient des cartes

### 4.1 Éléments versés

| élément | carte source | où il est versé | ce qui est gardé |
|---|---|---|---|
| Dose de lois héritables plantée, avec une **dose nulle** qui invalide la lecture si un écart y apparaît | `fed7a993d9671` | § 5 et § 8, règle de validité | la fraction ρ des lois vraies de la cible qui reprennent des lois de la source, à plusieurs valeurs dont zéro ; « si l'écart n'est pas nul à ρ = 0, la lecture est invalide » |
| Mondes à **dépendance plantée** et mondes **sans dépendance** | `fc1f059e8873e` ; variante dans un même monde, `f7a4918afe116` | § 5 | une moitié de mondes où les lois de la cible sont composées de lois de la source, une moitié où elles en sont indépendantes ; contrôle de construction : l'écart doit se concentrer là où la dépendance est plantée |
| **Répondeur scripté** qui ne réussit que s'il lit le vrai retour | `f7219bb36cfcb` | § 7, témoin de puissance | un proposeur écrit par programme, sensible par construction au contenu du registre ; s'il n'est pas distingué entre les bras, la mesure n'a pas la puissance de dire quoi que ce soit |
| Lecture au quart du budget, à mi-budget et à l'échéance | les neuf cartes | § 8, lecture descriptive | séparer un effet de départ d'un effet à l'échéance ; seule l'échéance décide |
| Registre factice de même forme, pris à un monde disjoint | `fed7a993d9671`, `f0d21fb62aff2` | § 9, bras de diagnostic | séparer le contenu de la seule présence d'un texte de même forme ; ici, le registre d'une **autre source**, sans seuil |
| Les copies ne comptent pas | `fdfac3afd4bae`, `f0d21fb62aff2` | § 6 | une loi vraie recopiée d'une entrée du registre hérité n'est pas comptée comme retrouvée |
| Garde de troncature par bras | `f0d21fb62aff2`, `f760c773d6f15` | § 8, liste d'arrêt | réponses vides ou tronquées comptées par bras ; lecture refusée si les taux diffèrent au-delà d'une marge gelée |
| Double appariement, en appels puis en dollars | `f760c773d6f15` | § 8, lecture secondaire | si l'ordre des bras s'inverse entre les deux appariements, la mesure ne sépare pas le registre du calcul, et c'est dit |
| Audit du générateur des mondes avant toute lecture | `f7a4918afe116`, `fc1f059e8873e`, `f11193560f4d4` (N-073, § 4) | § 5 | la présentation seule ne doit pas trahir la classe d'une loi ni la dose |

### 4.2 Éléments écartés, et pourquoi

| élément des cartes | cartes | raison |
|---|---|---|
| Servir à la génération suivante la **sélection des survivants** (cartes « survit », avec ou sans étiquette) | les neuf, à des degrés divers | l'objet du complément 3 est un registre des tentatives, non une sélection ; une sélection de survivants transmet un verdict agrégé (garde « la mémoire ne sert jamais un verdict ») |
| Règle « la sélection n'est servie que si le bras vrai dépasse… », porte qui décide de la transmission | `fdfac3afd4bae`, `f7a4918afe116`, `f11193560f4d4` | sert une décision de production sur un agrégat ; ce plan mesure et ne câble rien |
| Critère compté sur les lois « promues par la règle à e-valeurs » ou par le juge statistique | `f0d21fb62aff2`, `f473bb6a03ca3`, `f11193560f4d4` | la mesure se fait par l'oracle, par appariement programmé à la loi plantée (§ 6) ; le juge au nul reste hors de ce plan (N-067, N-071) |
| Vidage sur déclencheur, réducteur de ce qui est servi, dose d'appels sans archive | `f473bb6a03ca3`, `f760c773d6f15`, `f11193560f4d4` | mécanismes d'exploration, autre question ; seule leur parade est gardée (mondes de contrôle, double appariement, troncature) |
| Base « meilleur de N tirages à coût égal » comme critère décisif | plusieurs | condition du programme, pratique publiée et citée (N-073, § 2 ; Oved, Pony, Naparstek, Barzelay, arXiv 2610.23977), tenue à part de ce plan (§ 12, point 4) |
| La lettre d'origine de N-073, § 1, que les cartes recopient, et les voisins qu'elles citent sans les avoir lus | les neuf | lettre remplacée par les compléments 1 à 3 ; voisins non vérifiés (règle R7) |

## 5. Les mondes plantés

- **Paires source et cible.** Pour chaque source : un monde source, puis une suite de mondes cibles neufs, un par génération de la continuation, et un monde final tenu à l'écart, lu une seule fois. Lois vraies et lois fausses plantées de chaque côté.
- **Dose de dépendance ρ.** Une fraction ρ des lois vraies de chaque monde cible est composée, par construction, de lois vraies du monde source ; le reste en est indépendant. Sur processeur : ρ dans {0 ; 0,25 ; 0,5}. À l'étage payant : une seule dose non nulle, fixée après l'étage sur processeur, et la dose nulle.
- **Mondes avec et sans dépendance.** Les sources à ρ non nul portent les deux contrastes du critère. Les sources à ρ nul ne portent que la **règle de validité** : le registre hérité n'y contient, par construction, rien qui serve la cible ; un écart d'héritage non nul n'y peut venir que de la forme (longueur du contexte, présence d'un texte), et la lecture est alors invalide, à reconstruire.
- **Contrôle de construction dans un même monde.** Aux doses non nulles, l'écart d'héritage est aussi calculé à part sur les lois dépendantes et sur les lois indépendantes. Il doit se concentrer sur les premières. Réserve : chercher les lois dépendantes peut déplacer l'effort loin des indépendantes ; un écart négatif sur celles-ci n'est donc pas, seul, un effet de forme. C'est pourquoi la règle de validité repose sur les mondes à dose nulle et non sur ce contrôle.
- **Rien de la dose n'est servi.** Ni ρ, ni la classe d'une loi, ni le nombre de lois plantées ne figurent dans ce qu'un agent reçoit.
- **Audit du générateur avant toute lecture** (N-073, § 4) : un programme vérifie qu'un classifieur simple sur la présentation seule ne sépare ni les lois vraies des fausses, ni les dépendantes des indépendantes, ni les mondes par dose, au-delà du hasard, à une marge gelée. La dépendance plantée est fabriquée par nous et peut ne pas ressembler à une dépendance réelle : c'est une borne de la revendication.

## 6. L'oracle sur monde planté

- **Mesure principale** : sur le monde final tenu à l'écart, lu une seule fois à l'échéance, le **nombre de lois vraies plantées distinctes retrouvées** par le bras. « Retrouvée » se décide par programme : l'engagement scellé d'une tentative est apparié à une loi plantée par le comparateur de l'oracle. Aucun modèle n'intervient.
- **Les copies ne comptent pas** : une loi plantée déjà présente comme tentative dans le registre hérité de la source n'est pas comptée. Aux doses non nulles, les lois dépendantes de la cible sont composées de lois de la source et non identiques à elles ; elles restent à trouver.
- **Lois fausses** : le nombre de lois fausses plantées engagées et tenues par l'épreuve programmée est rapporté par bras. Condition jointe proposée, à geler : un écart d'héritage positif accompagné d'une hausse des lois fausses au-delà d'une marge gelée n'est pas lu comme un succès.
- **Volet des témoins jugés de l'oracle de N-058** (témoins vrais promus, faux rejetés par le juge) : **hors de la mesure principale**. Il n'est rapporté, comme information, que si des juges à modèle sont joués (option du devis). C'est un choix de ce brouillon, à confirmer (§ 12, point 2).
- **Lectures intermédiaires** : au quart et à la moitié du budget de la continuation, la même mesure calculée après coup sur les mondes d'évolution. Elles ne sont servies à aucun agent et ne décident de rien.
- **Jamais** le verdict d'un juge sur un agent ou sur un bras ; l'oracle n'écrit rien dans le registre (§ 3.1).

## 7. L'étage sur processeur, qui précède : répondeurs scriptés

**Aucun appel de modèle, 0 USD.** Il éprouve l'instrument, pas l'héritage chez de vrais proposeurs. Il demande son préenregistrement (règle R1, simulation comprise) et sa contre-lecture (règle R2).

**Banc.** Le générateur des mondes du § 5 ; un exécuteur simulé de l'épreuve programmée ; un compteur de coût simulé où lire un registre retire des appels (règle 6 du § 2) ; quatre proposeurs écrits par programme :

| proposeur scripté | ce qu'il fait | ce qu'il doit montrer |
|---|---|---|
| le lecteur | compose ses tentatives à partir des entrées du registre qui ont tenu ; ne trouve les lois dépendantes que s'il lit le vrai registre de la source | **témoin de puissance** : écart d'héritage positif aux doses non nulles, croissant avec ρ, nul à ρ = 0 |
| le sourd | ignore tout registre | écart d'héritage nul à toute dose ; taux de rejet de la procédure entière au niveau annoncé |
| le suiveur de forme | change de conduite dès qu'un registre non vide est présent, sans en lire le contenu | **artefact planté** : la règle de validité à dose nulle doit se déclencher |
| le copieur | recopie les entrées du registre comme tentatives | zéro loi retrouvée de plus, par la règle « les copies ne comptent pas » |

**Ce que l'étage établit, chaque point avec son cas sain et son artefact (règle R5) :**
1. La puissance : pour le lecteur, la part des tirages où la procédure du § 8 conclut, à dix et à douze sources, pour plusieurs tailles d'effet plantées. Si elle ne distingue pas le lecteur à la taille prévue, **le plan n'a pas la puissance de répondre et se reconstruit avant toute dépense**.
2. Le niveau : pour le sourd, le taux de rejet de la procédure entière (rangs signés exact, méthode de Pratt, procédure de Holm) ne dépasse pas 5 %.
3. La règle de validité à dose nulle : elle ne se déclenche pas sur le sourd plus souvent qu'annoncé, et se déclenche sur le suiveur de forme ; sa puissance est tracée selon le nombre de sources à dose nulle, ce qui **fixe ce nombre pour l'étage payant**.
4. La part de différences nulles attendue avec des scores en comptes, donc le nombre de sources utiles.
5. Les gardes du registre : invariant du § 3.1 (octet pour octet), scellement de la prédiction, chaîne d'empreintes, arrêt sur historique de départ non vide, cloisonnement des dossiers, grain du § 3.2.
6. Le contrôle de construction : l'écart du lecteur se concentre sur les lois dépendantes.
7. Le repli du § 3.1 : avec un registre servi sans `resultat` ni `gardee`, le lecteur trouve-t-il encore quelque chose ? Si non, le repli vide la question, et c'est à savoir avant de trancher le nœud.

**Ce qu'il ne dit pas.** Des proposeurs scriptés ne sont pas des modèles ; l'effet planté est choisi par nous. Une issue « instrument lisible » ne prédit ni le signe ni la taille de l'héritage chez de vrais proposeurs.

## 8. L'étage payant

**Conditions préalables, toutes requises :**
1. étage sur processeur lu, issue « instrument lisible » ;
2. boucle fermée dans l'organisme : la génération suivante lit réellement un registre, et l'épreuve programmée des tentatives est branchée sur le lanceur — ce que la proposition (§ 6, écart 5) et plusieurs cartes disent non fait à ce jour ;
3. générateur des mondes audité (§ 5) ;
4. nœuds du § 12 tranchés ;
5. pilote de bruit (deux courses du même bras, pour l'écart entre deux courses identiques) ;
6. préenregistrement scellé et contre-lu, devis accepté, ligne d'accord neuve.

**Dessin.** Dix sources au moins à dose non nulle (douze recommandées), trois bras, trois générations au moins ; des sources à dose nulle, bras 2 et 3 seulement, en nombre fixé par l'étage sur processeur. Chaque source demande d'abord sa course source, qui produit le registre hérité.

**Analyse.**
- Deux contrastes décisifs à l'échéance, sur la mesure du § 6 : héritage et tenue ; test et multiplicité du § 3.3.
- **Règle de validité** : sur les sources à dose nulle, l'écart d'héritage est soumis au même test, bilatéral, au seuil de 0,05 sans correction (une garde plus sensible est plus prudente). S'il passe, **la lecture entière est déclarée invalide et l'épreuve est à reconstruire** ; ce n'est ni un succès ni un échec de l'héritage.
- Lectures descriptives, sans seuil : bras 3 moins bras 1 ; les trois échéances ; l'écart par classe de lois ; la lecture à nombre d'appels égal, par troncature du journal, à côté de la lecture à dollars égaux ; le score par dollar dépensé ; la justesse des prédictions (§ 3.2) ; le gain du dernier doublement du budget par bras.
- Liste d'arrêt : plafond de dépense ; taux de réponses vides ou tronquées qui diffère entre bras au-delà de la marge gelée ; historique de départ non vide ; chaîne d'empreintes rompue ; garde du générateur en échec.

**Ce qui réfuterait.**
- Héritage : le contraste (bras 3 moins bras 2) ne passe pas son seuil, ou est négatif. Le registre transmis n'a alors pas d'effet établi au-delà de la tenue et de l'organisme hérité.
- Tenue : le contraste (bras 2 moins bras 1) ne passe pas son seuil, ou est négatif, à budget égal.
- Un effet présent au quart du budget et absent à l'échéance est rapporté comme effet de départ ; il ne vaut pas succès.
- Un résultat trop propre déclenche le même audit qu'un échec (règle R4). Un résultat négatif se rapporte tel quel ; aucune reprise ne vise un signe (règle R3).

## 9. Bras de diagnostic

À part des trois bras du critère, sans seuil, sur devis à part, joués après eux, sans effet sur aucun verdict. Repris du plan d'origine : résultats permutés entre entrées ; registre sans le champ de prédiction ; historique brut de la source laissé en place, sans registre ; entrées fausses plantées par l'orchestrateur (dans ce bras seulement) ; registre paraphrasé. Ajouté depuis les cartes : **registre d'une autre source**, de même forme et d'un monde disjoint, qui sépare le contenu de la présence. Les six se jouent d'abord sur processeur, avec les proposeurs scriptés, à 0 USD.

## 10. Ce que le plan ne revendique pas

- Aucune priorité. La séparation de l'héritage et de la tenue a des précédents lus sur source ; ce plan suit la rédaction du complément 3 de N-073, qui décrit une forme et dit ne pas l'avoir trouvée dans les pages lues de six travaux, « ce qui ne dit rien des autres ».
- Rien sur « l'héritage tout court » : seulement ce que le registre ajoute à un organisme qui hérite déjà par son code (§ 2, règle 1).
- Rien sur une mémoire contre rien : le bras 1 garde l'historique ordinaire de sa continuation.
- Rien hors des mondes plantés : la dépendance est fabriquée, la dose n'a pas de réalisme vérifié, et le monde planté n'est pas une banque réelle.
- Rien sur le juge au nul formé des lois connues (N-067, N-071) : il est hors de ce plan, et la mesure n'emploie pas sa règle de promotion.
- Rien sur un concepteur entraîné, des sondes ou des adaptateurs transmis, ni sur la diversité des fournisseurs.
- Rien sur la valeur d'un proposeur ou d'une espèce : aucune composition n'est choisie par ce plan (N-058).
- L'étage sur processeur ne revendique que la tenue de l'instrument.
- Aucune des neuf cartes n'est adoptée ; aucun mécanisme n'est câblé dans l'organisme.

## 11. Citations obligatoires de tout texte sortant tiré de ce plan

La lettre est celle de N-073, § 1, telle que les compléments 1, 2 et 3 l'ont remplacée ; la rédaction de la section C du complément 3 se recopie à l'octet. Les numéros de page sont ceux des décisions ; un texte sortant donnera les références complètes.

**N-073, § 1** : Wang et al., « Huxley-Gödel Machine », arXiv 2510.21614 ; Zhang, Hu, Lu, Lange, Clune, « Darwin Gödel Machine », arXiv 2505.22954 ; Robeyns, Szummer, Aitchison, « A self-improving coding agent », arXiv 2504.15228 ; Sutton et Barto ; Schmidhuber et Zhao (1996), Schmidhuber, Zhao et Wiering (1997), Kirsch et Schmidhuber (2022) — ces trois derniers à lire sur source avant de les citer comme antériorité. Indice contraire à dire avec sa prémisse : Qin et al., arXiv 2611.05108 (ce qui est légué rapporte surtout au départ ; chiffres et pages dans N-073, § 1).

**Complément 1** : Yu, Xia, Pan, Tang, Liu, Yu, Jiang, Chen, Xue et Yu, « Self-Improvement Memory Enables Continual Recursive Self-Improvement », arXiv 2611.18856.

**Complément 2** : Li et Hu, « SkillHone », arXiv 2606.08671 (p. 4, p. 6) ; Lee et al., « Meta-Harness », arXiv 2603.28052, à citer comme indice contraire avec sa prémisse (tableau 3, p. 7).

**Complément 3**, les neuf :
- Xu et al., « Harness² », arXiv 2610.14224 (p. 7, p. 10, p. 11, p. 20) ;
- Qian et al., « MetaSkill », arXiv 2609.38143 (p. 5, p. 9, p. 12, p. 17) ;
- Shi et al., « PluginRSI », arXiv 2609.32423 (p. 8, p. 16) ;
- Zhang et al., « Causal Improvement Graph », arXiv 2610.05039 (p. 9, p. 15, p. 16) ;
- Yuan et al., « Meta² », arXiv 2611.05139 (p. 6, p. 8) ;
- Wang et al., arXiv 2607.12227 (p. 5, p. 8-9, p. 13, p. 24) ;
- Ke et al., « EvoHarnessBench », arXiv 2609.04280 (p. 6, p. 23) ;
- Lin et al., « Agentic Harness Engineering », arXiv 2604.25850 (p. 9, p. 35), pour la mesure de la justesse des prédictions contre un hasard, que ce plan rapporte (§ 3.2) ;
- Kim et al., arXiv 2604.14004 (p. 4-5), à côté de Meta-Harness (p. 7), comme indice sur la forme de la mémoire, avec sa prémisse.

**Autres, selon ce que le texte aborde** : Oved, Pony, Naparstek, Barzelay, arXiv 2610.23977, si la base des tirages indépendants à coût égal est jouée (N-073, § 2 : pratique publiée, citée). Brier (1950), Pratt (1959) et Holm (1979) pour les outils de statistique : références classiques, à vérifier sur source avant citation (règle R7).

## 12. Points ouverts — nœuds de Lazar, aucun défaut

1. **`resultat` et `gardee` peuvent-ils être servis ?** La garde « la mémoire ne sert jamais un verdict » se lit-elle comme interdisant les seuls verdicts de juge à modèle et la sélection des survivants (lecture de ce brouillon, appuyée sur la lettre du complément 3), ou aussi la classe d'issue d'une épreuve programmée ? Repli écrit au § 3.1 ; l'étage sur processeur dira ce que le repli coûte (§ 7, point 7).
2. **La mesure principale laisse de côté le volet des témoins jugés de l'oracle de N-058.** Est-ce une lecture permise de N-058 pour ce plan, ou un écart à porter comme tel ?
3. **Deux contrastes décisifs ou un seul ?** Avec le seul contraste de l'héritage au seuil de 0,05, le plancher technique tombe à six sources (valeur p minimale 0,03125, six signes égaux exigés) ; la tenue deviendrait descriptive. Ce brouillon garde les deux et le plancher de dix.
4. **La base « tirages indépendants à coût égal »** (N-073, § 2) n'est pas un bras de ce plan. La jouer ici, comme quatrième bras descriptif sur devis, ou la tenir à l'épreuve qui lui est propre ?
5. *Hors nœud, à décider au préenregistrement* : la dose non nulle de l'étage payant ; les marges (lois fausses, troncature, audit du générateur) ; la liste des classes d'issue ; la règle de `gardee` ; ce qui est servi quand le registre dépasse la taille bornée.

## 13. Réserves du rédacteur

1. **Je n'ai lu aucun code.** Je ne sais pas ce que l'organisme reçoit aujourd'hui comme retour ordinaire, si une épreuve programmée par tentative existe sur le lanceur, ni si le comparateur de l'oracle apparie un engagement à une loi plantée sans modèle. Les § 2 (règle 3), 3.1, 3.2 et 6 en dépendent. À établir avant tout préenregistrement.
2. N-045 v2, N-049, N-050 et N-053 sont cités d'après le plan d'origine et sa vérification courte, non relus.
3. Le choix du § 3.1 (ni juge, ni clé de l'oracle) va plus loin que les deux voies de la vérification courte. Il change ce que le registre contient par rapport au plan d'origine, qui y écrivait le score de l'oracle. C'est un choix de rédacteur, à contre-lire en premier.
4. La règle de validité à dose nulle est faible avec peu de sources : à six, elle ne se déclenche que si les six écarts ont le même signe. Sa puissance réelle est une sortie de l'étage sur processeur, non une donnée de ce texte.
5. Le plancher de dix sources ne dit rien de la puissance pour un effet de taille réaliste ; il dit seulement en dessous de quoi le test ne peut pas conclure.
6. Les cartes n'ont servi que par leurs éléments d'épreuve ; je n'ai pas vérifié qu'un autre élément utile ne se trouve pas dans les cartes que le mandat ne m'ouvrait pas.

## 14. Vérification de la liste « Ne pas écrire » du complément 3 sur ce texte et sur le devis

Faite par le rédacteur, par recherche de chaînes sur les deux fichiers avant scellement, puis relue ligne à ligne. Le programme de recherche n'est pas versé (il contiendrait les formules interdites) ; le contre-lecteur refera la recherche. Les lignes sont celles de la liste du complément 3, dans l'ordre, désignées par leur sujet et non recopiées.

| ligne de la liste | sujet | dans ce texte et dans le devis |
|---|---|---|
| 1 | quatre formules de priorité (nouveauté de la question, zone, absence de précédent, rang de premier) | absentes ; le § 10 dit qu'aucune priorité n'est revendiquée |
| 2 | la formule du complément 2 opposant découvertes et score d'un harnais comme ce qui distingue le programme | absente |
| 3 | deux affirmations sur Harness² (ce que devient la bibliothèque héritée sur le banc cible ; l'unité de mesure des trois bras) | absentes ; Harness² n'est nommé qu'au § 11, sans affirmation |
| 4 | un écart-type attribué au harnais de base de Harness² | absent ; aucun chiffre de ce papier |
| 5 | deux affirmations sur MetaSkill (apprentissage propre contre héritage ; intervalles) sans leurs précisions | absentes ; MetaSkill n'est nommé qu'au § 11 |
| 6 | l'affirmation sur un état porté mais non révisé, sans ses précisions | absente |
| 7 | l'affirmation chiffrée sur les prédictions de Lin et al. sans ses précisions | absente ; Lin et al. n'est cité que pour le principe de la mesure, dans les mots du complément 3 |
| 8 | deux affirmations sur Wang et al., arXiv 2607.12227 (coût de la modification ; appariement) | absentes |
| 9 | une contradiction affirmée entre Kim et al. et Meta-Harness, dans un sens ou dans l'autre | absente ; les deux sont cités côte à côte, « avec sa prémisse » |
| 10 | l'appellation fautive de notre objet, corrigée par le complément 3 | absente ; l'objet est partout « registre des tentatives » ou « registre » |
| 11 | un chiffre calculé par un lecteur présenté comme chiffre des auteurs | aucun chiffre de la littérature n'est donné ; les seuls chiffres sont ceux du test (calculés par le programme joint) et des coûts de la course v9 |

Vérifié aussi : la liste « Ne pas écrire » du point 4 du complément 2 (six formules sur Yu et al.) et la liste « Ne plus écrire » de N-073, § 1 — aucune de leurs formules n'est employée ; ce plan ne récompense aucun héritage et ne crédite aucune génération par sa descendance : il mesure un objet.
