# Question de l'héritage (N-073, § 1) — plan à trois bras corrigé — v2

- **Statut : pièce de travail, version 2, à vérifier par le contre-lecteur.** Ce n'est pas un préenregistrement. Rien ici ne s'applique ni ne modifie une pièce scellée. Chaque étage décrit plus bas demande son propre préenregistrement scellé et contre-lu (règles R1 et R2) ; chaque étage payant, pilote de bruit compris, demande en plus son devis et une ligne d'accord neuve.
- **Écrit par** : le rédacteur (modèle F), le 2026-11-19 entre 13:24Z et 13:40Z (`date -u`), sur processeur seul, sans appel à un fournisseur de modèles, sans dépense. Contre-lecteur prévu : modèle O.
- **Version remplacée, gardée telle quelle (règle R12)** : `plan-heritage-trois-bras-corrige-v1.md` (`a514c6dc072075d037eb77ba7d0c79fe1e3497180e8606782e67bc09aa2f4a0d`). Contre-lecture appliquée : `contre-lecture-plan-heritage-trois-bras-corrige-v1-v1.md` (`124767e4724bb125801b31df03c7021cc5cef1701349bdfa12c174fc8c3013da`), verdict « scellable après corrections », dix-sept constats. La table « correction → où, comment » est au § 15 ; le différentiel v1 → v2 au § 16.
- **Mandat** : ligne `GO-2026-11-19-55` de `registres/go.md` (mot de Lazar, « les 5 lignes plus la question de l'heritage »), option (c) de la proposition. **Deux principes posés depuis la v1 et tenus ici** :
  - ligne `GO-2026-11-19-60` (mot de Lazar, verbatim : « le cout ne doit pas etre un fcateur limitant s'il ameliore considerablement l'organisme ») : le coût est rapporté, il ne restreint plus à lui seul un plan. La procédure est inchangée : chaque étage payant sur son devis et une ligne d'accord neuve. Ce plan n'est donc plus « préparé sans dépense » par principe : il décrit l'étage payant entier, et le devis joint le chiffre sans le réduire. Dire si la réponse à la question de l'héritage vaut « amélioration considérable » n'est pas du ressort de cette pièce (§ 12, question 9) ;
  - erratum 1 de la lecture descriptive de la course v9 (`docs/notes/organisme-auto-conception-v1/course-v2/lecture-course-v9-v1-erratum-1.md`, `9a77160097458889d4ec7771c05e50d97632b7772466c6023f2e444e0a72b9d3`, sur `main`) et N-058 : **aucune pièce ne prend le verdict des juges comme critère.** Ici : aucun élément de carte n'a été choisi ou écarté sur une note de juge ; aucun critère, aucune garde, aucun champ du registre ne dépend d'un juge ; le volet des témoins jugés n'est qu'une information (§ 6).
- **Pièces lues pour la v2**, empreinte calculée sur le contenu lu (`main` au commit `6aec55f11b7c5f3c2fabbb1a8c909634f99d567b`, branche `lot/compte-organisme-v1` au commit `64501566e0e9562e21e8e4392c2941b737180705`) :
  - les quatre pièces de la v1 et leur contre-lecture, en entier ; `calcul_devis_heritage_v1.py` (`782a86104b518eb5a4a616111ec6fb50d70ac713bf58138013c1b27291b4b186`) et sa sortie (`02bae7980cbba40fb83ea7f30d732e11f9880c24fca3c4a1913b4b8923231765`) ;
  - lettre : `docs/decisions/decision-N-073-complement-3-memoire-transmise-v1.md` (`4ca0ce7b040b917d9be145134b2b28755a862bfa7a41e4f16d22893129bb03e5`), en entier ; complément 2 (`5707dbd8bdd8ccc224578be480107723fad6e5054484082c1a1c38d8fa588e8e`), points 2 à 4 ; complément 1 (`61903909e8aaaa70d6f1aa26a8025104aa3513244b6723daac529048267d4478`), connu par la v1 ; N-073 (`b95688df5e695da7dc32ce71321ba205f44debcc0b7410e598c78c2180733ecd`), § 1 ; N-058 (`docs/decisions/decision-N-058-v1.md`, `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`), définition de l'oracle seulement ; N-067 (`docs/decisions/decision-N-067-v1.md`, `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`), sections 4 et 6 ; N-071 (`docs/decisions/decision-resserrement-juge-au-nul-v1.md`, `9700fe6fce74840d383e3cbbf2e0f87f7914887759df3c0aa0fea687b433c184`), en-tête et points 4 à 6 ;
  - plan d'origine : `docs/notes/veille-yu-memoire-v1/lecture-yu-approfondie-v2.md` (`956842550081abbd0292bc082015e782421c919ad0676764ed89721b3cc2e48f`), section (c) en entier, dont c.7, c.8 et c.9 ; vérification courte `docs/notes/veille-yu-memoire-v1/verification-courte-versions-2-v1.md` (`98d1152f05e3b60568557dca1d01a84ed2343a7505f1d17c0febdea4815e36dd`), connue par la v1 et par la contre-lecture ;
  - proposition `docs/notes/organisme-auto-conception-v1/course-v2/proposition-cartes-a-eprouver-v9-v1.md` (`a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856`), lignes qui nomment les tests de mort et le juge statistique ; critères `criteres-choix-cartes-v9-v1.md` (`8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326`) et lecture descriptive `lecture-course-v9-v1.md` (`0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb`), connus par la v1 ; `registres/go.md`, lignes 55 à 60 ;
  - organisme, en lecture seule (`/home/user/ideation-organism`, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`) : le début de `README.md` (trajet d'une idée, étapes 7 à 9) et **l'en-tête seul** des modules `orchestrator/pole/tests_de_mort_v5.py` (`da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1`) et `tests_de_mort_v4.py` (`35912a3ab5e9e289077ffdceb492bb966f24176244976b3923dcfe95bda1603a`), plus les constantes nommées au § 3.0. C'est ce qui fonde le choix du § 3.0 ; ce n'est pas une lecture du code (§ 13, réserve 1).
- **Cartes** : les neuf cartes de la v1 (`fed7a993d9671`, `fdfac3afd4bae`, `f0d21fb62aff2`, `f7a4918afe116`, `fc1f059e8873e`, `f7219bb36cfcb`, `f473bb6a03ca3`, `f760c773d6f15`, `f11193560f4d4`, dans `fiches.json`, `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`) n'ont pas été rouvertes pour la v2 : la contre-lecture a vérifié leurs attributions carte par carte, et la seule correction qui les touche (constat 12) reprend sa lettre. Aucune autre carte, aucune espèce, aucun verdict n'a été lu.
- **Non lus** : le corps du code de l'orchestrateur, de l'oracle et du générateur des mondes plantés ; les décisions N-045 v2, N-049, N-050 et N-053, connues par ce que les pièces ci-dessus en citent ; tout classement, tout coffre. Les conséquences sont dites au § 13.
- Chaque carte est l'avis d'un proposeur, jamais un fait. Les travaux que les cartes citent ne sont pas repris ici.

## 0. Verdict

1. Le plan tient en trois bras sur le même objet : **un registre des tentatives de l'organisme, hérité d'une course antérieure puis tenu ; le même registre né vide et tenu ; aucun registre servi**. Les trois corrections de la vérification courte (R-3643) restent appliquées (§ 3.1 à 3.3) ; les dix-sept corrections de la contre-lecture le sont toutes (§ 15).
2. **L'épreuve programmée est maintenant définie (§ 3.0) : ce sont les tests de mort de l'organisme, verdict calculé par le noyau de l'orchestrateur.** C'est un choix du rédacteur entre trois voies, porté comme question à la mère (§ 12, question 1).
3. **Ce que le plan mesure est dit plus étroitement** : un écart à budget égal, coût de lecture compris, et seulement l'héritage spécifique à la dépendance plantée ; un savoir-faire général transmis invalide la lecture au lieu d'être mesuré (§ 2, § 5, § 10).
4. L'ordre des étages est : étage sur processeur (0 USD d'appels, critère « instrument lisible » chiffré au § 7) ; **pilote de bruit, sous son propre préenregistrement, son devis et sa ligne d'accord** (§ 8.0) ; étage payant (§ 8). Le devis joint (`devis-heritage-trois-bras-v2.md`) chiffre l'étage payant entier et sa recommandation.
5. **Neuf questions vont à la mère** (§ 12) ; quatre sont des nœuds de Lazar.

## 1. L'objet : un registre des tentatives

L'objet est celui que fixe le complément 3 de N-073 : un **registre des tentatives** de l'organisme. Une entrée par problème ; sous elle, une ligne par tentative.

| champ | qui l'écrit | quand | forme |
|---|---|---|---|
| `probleme` | le proposeur | à la proposition | une phrase bornée, ou l'identifiant d'un problème déjà inscrit |
| `tentative` | le proposeur | à la proposition | l'engagement éprouvé, sous la forme que l'épreuve programmée exécute (§ 3.0), et une description bornée |
| `justification` | le proposeur | à la proposition | texte borné |
| `prediction` | le proposeur | à la proposition, **scellée par son empreinte avant toute épreuve** | une probabilité par classe d'issue, sur une liste fermée (§ 3.2) |
| `resultat` | **l'orchestrateur, par programme** | après l'épreuve | la classe d'issue de l'épreuve programmée de cette tentative (§ 3.0), et son coût mesuré ; aucun texte |
| `gardee` | l'orchestrateur, par programme | après l'épreuve | oui si la classe est « tient », non sinon (§ 3.0) |
| `provenance` | l'orchestrateur | à l'écriture | génération, source, version de l'orchestrateur, empreinte de la configuration |

Le registre est en ajout seul, chaîné par empreintes et scellé à chaque génération ; les tentatives non gardées y restent. Les longueurs et la liste fermée des classes se gèlent au préenregistrement.

Ce que le registre ne contient jamais : un verdict, un score ou un texte d'un juge, à modèle ou statistique ; une liste, un rang ou un compte de cartes promues ou survivantes ; une valeur tirée de la clé du monde planté ; un identifiant ou un nombre d'items plantés ; quoi que ce soit du monde de la mesure finale.

**Ce qui est gardé des sections c.7 et c.8 du plan d'origine** (cloisonnement de ce qui s'écrit ; le registre comme canal d'attaque : celui qui écrit le registre est celui qui est évalué) :

| règle du plan d'origine | sort dans cette version |
|---|---|
| c.7, points 1 et 2 : `resultat` et `gardee` ne viennent que de l'oracle sur le jeu d'évolution | **remplacés** : ils viennent de l'épreuve programmée sur la tranche d'épreuve du monde en cours, jamais de l'oracle ni de sa clé (§ 3.0, § 3.1) ; jamais du monde final |
| c.7, points 3 et 4 : rien du monde de la mesure finale ; aucun identifiant ni nombre d'items plantés, écrit ou servi ; un monde neuf par génération | gardés (ci-dessus, § 3.2, § 5) |
| c.7, point 5 : aucun score de juge, aucun extrait de verdict dans le registre | gardé, étendu au juge statistique (§ 3.1) |
| c.8 : **aucun champ du registre n'est une entrée d'un juge** ; un juge ne lit jamais le registre ni un texte qui en dérive directement | gardé : c'est le sens inverse de l'invariant du § 3.1 ; garde éprouvée sur un cas sain et sur un artefact (règle R5) dès qu'un juge à modèle est joué (option du devis) |
| c.8 : champs typés et bornés ; champs libres servis aux proposeurs **entre balises de donnée** | gardé |
| c.8 : **audit du registre par un lecteur d'une autre lignée que les proposeurs, à chaque génération** (N-053), constats rapportés, rien filtré en silence | gardé ; le lecteur ne note ni un agent ni un bras, ses constats n'entrent dans aucun critère ; un appel par génération de bras qui tient un registre, compté au devis comme poste non chiffré |
| c.8 : l'agent n'écrit ni `resultat` ni `gardee` ; registre en ajout seul, chaîné, scellé ; empreinte de la prédiction avant l'épreuve ; justesse des prédictions hors de tout signal ; dossiers séparés entre bras | gardés (§ 1, § 2, § 3.2) |
| c.8 : canal caché entre générations (bras au registre paraphrasé) ; suivre un registre faux (entrées fausses plantées, dans un bras de diagnostic seulement) | gardés au § 9 |

## 2. Les trois bras

Pour chaque **source** indépendante — une course antérieure de l'organisme sur un monde planté, pendant laquelle il a tenu un registre né vide —, trois continuations partent du même organisme, sur la même suite de mondes plantés neufs :

| bras | registre servi au départ | registre servi pendant la continuation | champs écrits sur disque |
|---|---|---|---|
| 1 — aucun registre servi | aucun | aucun | les mêmes, scellés, **non servis** |
| 2 — registre né vide et tenu | vide | tenu et servi | tenus et servis |
| 3 — registre hérité puis tenu | celui de la source | tenu et servi | tenus et servis |

- **Bras 3 moins bras 2 : l'héritage**, c'est-à-dire ce que le registre reçu de la source ajoute au fait d'en tenir un.
- **Bras 2 moins bras 1 : la tenue**, c'est-à-dire ce que **servir** un registre tenu ajoute à l'historique ordinaire.
- Bras 3 moins bras 1 : rapporté, sans seuil.

**Ce qui est estimé.** Chaque contraste est un **écart à budget égal, coût de lecture compris**. Le bras qui lit un registre a moins d'appels (règle 6) : l'écart mêle donc, par construction, ce que le registre apporte et ce que sa lecture coûte. Un proposeur qui ignorerait le registre aurait un écart d'héritage attendu **négatif**, égal à l'effet du seul coût de lecture. Tout texte tiré de ce plan le dit ainsi ; l'effet du seul coût est mesuré à part (§ 7, le sourd qui paie ; § 8, lecture à nombre d'appels égal).

**Le bras 1 écrit les mêmes champs.** Dans les trois bras, le proposeur écrit `probleme`, `tentative`, `justification` et `prediction`, la prédiction est scellée avant l'épreuve, et l'orchestrateur écrit `resultat`, `gardee` et `provenance`. La garde « refuser d'éprouver une tentative sans empreinte de prédiction » vaut pour les trois. Au bras 1, ces champs restent sur disque et ne sont jamais servis. Conséquences : le contraste de la tenue isole le **service** du registre (rangement par problème, justification, prédiction et provenance relus) et non la charge d'écrire les champs, qui est la même partout ; la justesse des prédictions se lit dans les trois bras. Borne : ce que l'acte d'écrire une justification et une prédiction fait lui-même au proposeur n'est pas mesuré, puisqu'il est commun aux trois bras.

Les sept règles du plan d'origine (section c.4) sont gardées, avec ces précisions :

1. **Même organisme de départ.** Les trois bras partent du code et des consignes de l'organisme tel que la source l'a laissé. Le contraste de l'héritage mesure donc ce que le registre transmis ajoute à un organisme qui hérite déjà par son code. C'est une borne, à écrire dans tout texte.
2. **L'historique de la source est remis à zéro dans les trois bras.** Chaque bras ne garde que l'historique ordinaire de sa propre continuation, sous la même forme. Le seul canal par lequel la source parle, au-delà du code, est le registre du bras 3. Garde éprouvée sur un cas sain et sur un artefact (règle R5) : un historique de départ non vide arrête le lancement.
3. **Le même retour ordinaire dans les trois bras, au même grain.** Ce retour est la classe d'issue de l'épreuve programmée de chaque tentative, et son coût (§ 3.0, § 3.2). Le champ `resultat` ne contient rien de plus fin. Le registre ne change donc que l'accès au passé — rangement par problème, justification, prédiction scellée, provenance, et pour le bras 3 le passé de la source —, non la quantité d'information tirée de l'épreuve. **Changement de l'organisme, déclaré** : les tests de mort ne sont pas branchés aujourd'hui sur le lanceur, et l'organisme ne les fait passer qu'à une part des cartes ; ici toute tentative est éprouvée et son issue est rendue aux trois bras. Ce changement s'écrit au préenregistrement et s'applique aux trois bras à l'identique (§ 3.0).
4. **Budget en dollars égal par bras**, épreuve programmée comprise, et le coût dans le signal rendu à l'organisme, sous une forme gelée et identique dans les trois bras.
5. **Dépense réelle rapportée par bras** ; un bras qui ne dépense pas son budget n'est pas complété.
6. **Le bras qui lit un registre paie sa lecture sur le même budget** : il a donc moins d'appels. La règle de retrait est gelée, la même pour tous, et suit le coût au plus près : à chaque génération, le bras joue **le plus grand nombre d'appels dont le coût prévu, lecture du registre comprise, tient dans le budget de la génération**. Le coût prévu d'un appel est le coût de référence par appel de son espèce (gelé d'après le pilote) plus le coût de lecture du registre servi, calculé sur sa taille mesurée au début de la génération. Les appels retirés le sont un à un, dans l'ordre d'une permutation semée des appels prévus (`numpy.random.SeedSequence`, graine dérivée par bras et par génération, règle R9) : le retrait est donc en espérance proportionnel au nombre d'appels de chaque espèce, et la composition n'est pas déformée par un arrondi. Le reliquat de budget n'est pas dépensé ; il est rapporté. *Remplace la règle de la v1* (arrondi à l'entier inférieur par espèce), qui retirait au moins un appel sur onze à chaque espèce dès que la lecture coûtait quoi que ce soit. Le nombre d'appels perdus par le bras 3 à la première génération, selon la part du coût d'un appel que prend la lecture, est au devis (§ 2 bis).
7. **Cloisonnement entre bras.** Aucun dossier lisible n'est commun à deux continuations. Les trois bras d'une source reçoivent la même suite de mondes (graines des mondes dérivées par source et par génération, communes aux trois bras ; graines d'échantillonnage dérivées par bras ; règle R9).

Longueur : trois générations au moins par continuation, comme au plan d'origine, **puis une génération finale sur le monde tenu à l'écart** (§ 6).

## 3. L'épreuve programmée, puis les trois corrections de la vérification courte

### 3.0 L'épreuve programmée — choix du rédacteur : les tests de mort

**Le défaut de la v1.** Les champs `resultat` et `gardee`, l'objet de la prédiction, le compte des lois fausses « tenues » et l'exécuteur simulé de l'étage sur processeur reposaient tous sur une « épreuve programmée » que la v1 ne définissait pas. Or l'organisme a deux épreuves écrites en programme : le juge statistique (règle à e-valeurs, nul formé des lois connues ; N-067, section 4, point 1 ; N-071) et les tests de mort.

**Les trois voies, et celle qui est prise.**

| voie | ce qu'elle ferait | pourquoi elle est prise ou non |
|---|---|---|
| (a) le juge statistique de l'organisme | `resultat` porterait la promotion par la règle à e-valeurs, contre le nul formé des lois connues | **non prise.** (i) Le registre servirait le verdict d'un juge, programmé mais juge : c'est ce que la vérification courte reprochait au plan d'origine, et ce que le principe « aucun verdict de juge comme critère » écarte. (ii) Le nul de ce juge est formé des lois que l'organisme connaît déjà ; l'instrument qui écrit `resultat` dépendrait donc de ce que chaque bras a accumulé, et ne serait plus le même dans les trois bras. (iii) Le plan toucherait la revendication du juge au nul (N-067, N-071) et sa clause d'usage public, alors qu'il ne mesure rien d'elle. |
| **(b) les tests de mort de l'organisme** | `resultat` porte l'issue d'un test préenregistré, à seuil gelé avant l'exécution, calculée par le noyau de l'orchestrateur | **prise.** (i) L'épreuve existe dans l'organisme et répond déjà à la lettre du complément 3 : prédiction scellée avant l'exécution, résultat écrit par programme, « gardée ». (ii) Son verdict a trois issues, qui sont les trois classes que la v1 proposait. (iii) Elle ne compare la tentative qu'à son propre seuil gelé, sur des données : elle est la même dans les trois bras, et elle existe aussi hors d'un monde planté. (iv) Elle ne touche pas la revendication du juge au nul. |
| (c) une épreuve neuve propre à ce plan | à écrire | **non prise, gardée comme repli.** Elle ferait mesurer l'héritage dans un organisme qui n'existe pas, et demanderait le plus de code neuf. Elle redevient la voie à prendre si les tests de mort ne peuvent pas éprouver une loi d'un monde planté (réserve 1 du § 13). |

**Ce que la voie (b) coûte, dit d'avance.** Les tests de mort ne sont pas branchés sur le lanceur (proposition, § 6, écart 5) : ce branchement est une condition préalable (§ 8). Le test demande aujourd'hui une session d'un modèle qui écrit le script (l'expérimentateur), donc un appel payant par tentative, sans coût réel connu (devis, § 6). Et un verdict « tient » dit que l'engagement a passé **son propre seuil**, pas que la loi est vraie.

**Définition, telle que le préenregistrement de chaque étage la gèle.**

| élément | définition |
|---|---|
| exécutant | l'orchestrateur, par programme : l'étage des tests de mort dans sa version où **le verdict est calculé par le noyau** sur le fichier brut que nomme le préenregistrement court scellé (module `tests_de_mort_v5.py` de l'organisme, en-tête lu). Aucun modèle ne décide du verdict. |
| entrée | l'engagement scellé de la tentative, sous la forme que l'étage exécute : un préenregistrement court qui nomme un fichier, une colonne, une statistique et un seuil avec son sens de comparaison ; scellé par son empreinte avant toute exécution. Une tentative sans ce bloc est refusée à l'étage, jamais éprouvée sur un chiffre que le script imprime. |
| données | **la tranche d'épreuve du monde en cours** : une part nommée du jeu d'évolution de ce monde, tirée par une graine dérivée par monde (règle R9), la même pour les trois bras ; sa proportion est gelée au préenregistrement (valeur proposée : la moitié). Jamais le monde final ; jamais un autre monde. |
| statistique | une de la liste fermée de l'étage (moyenne, médiane, somme, minimum, maximum, nombre, part positive, écart-type), calculée par le noyau sur la colonne nommée du fichier brut de la dernière exécution réussie. |
| seuil | celui que l'engagement scellé porte ; comparaison faite par le noyau, sans arrondi. La forme admise des engagements sur monde planté (statistiques permises, sens, bornes du seuil) est gelée au préenregistrement. |
| passage aux trois classes | « survit » devient **« tient »** ; « éliminée » devient **« ne tient pas »** ; « non concluant » (aucune exécution réussie, fichier absent ou altéré, incident) devient **« non exécutable ou indéterminée »**, jamais mieux traitée que « ne tient pas ». |
| `gardee` | oui si et seulement si la classe est « tient » : c'est la règle de sélection de l'étage, qui ne retient que « survit ». |
| qui est éprouvé | **toute** tentative, dans l'ordre de son scellement. Aucun classement par un juge ne choisit ce qui va à l'épreuve. Si le budget ne suffit pas, les tentatives éprouvées sont tirées par graine, et les autres reçoivent la classe « non exécutable ou indéterminée » avec un motif écrit. |
| coût | payé sur le budget du bras, dans les trois bras à l'identique. |

**Ce que l'épreuve n'est pas.** Elle n'est ni le juge statistique, ni sa règle de promotion, ni un juge à modèle. Le § 4.2 (cartes écartées parce qu'elles comptent les lois promues par le juge statistique) et le § 10 (rien sur le juge au nul) restent donc exacts. Les citations obligatoires de N-067, section 6, et de N-071, point 5, ne sont pas appelées par l'épreuve ; elles le deviennent si un texte sortant présente l'organisme ou son juge (§ 11).

**Limites connues de l'étage, reprises de son en-tête** : les lignes du fichier brut sont écrites par le script, et un script qui fabriquerait ses lignes n'est pas détecté par le noyau ; les essais de cette version sont hors ligne, le vrai bac à sable n'a pas été rejoué avec elle. Sur un monde planté, une épreuve trop facile se lit dans le compte des lois fausses tenues (§ 6). Le lecteur témoin de l'étage, qui ne pèse pas sur le verdict, est gardé ou retiré au préenregistrement (§ 12, question 8).

### 3.1 Correction 1 de la vérification courte — l'invariant face à l'oracle de N-058

**Défaut.** Le plan d'origine posait : « aucune valeur de la mémoire n'est fonction d'une sortie du juge ». Or N-058 définit l'oracle du monde planté par « structures retrouvées, témoins plantés vrais promus et faux rejetés », et les témoins sont promus ou rejetés par le juge. Les champs `resultat` et `gardee`, écrits depuis le score de l'oracle, violaient donc l'invariant par construction ; pris à la lettre, il n'était pas testable.

**Choix : une troisième voie.** La vérification courte proposait deux voies. Ce plan n'en prend aucune : il **remplace le signal de l'oracle par une épreuve sur les données** (§ 3.0). Le registre n'emploie ni le volet des témoins jugés, ni la clé du monde planté, ni le juge statistique.

- Les champs écrits par programme (`resultat`, `gardee`) sont calculés par une fonction dont les **seules entrées** sont : l'engagement scellé de la tentative, la tranche d'épreuve du monde en cours, le fichier brut de l'exécution, et le journal des coûts.
- Raison : un registre qui porterait la réponse de l'oracle (« cette tentative est une loi vraie ») ne peut exister que dans un monde planté. Ce que l'on mesurerait en l'héritant ne dirait rien d'un organisme qui travaille sans oracle. L'épreuve du § 3.0, elle, existe dans les deux cas.
- **L'oracle ne sert qu'à la mesure**, hors de tout ce qui est servi à un agent (§ 6).

**Invariant, dans sa forme corrigée.** « Aucun champ du registre n'est calculé à partir d'une sortie d'un juge, à modèle ou programmé, autre que l'épreuve nommée au § 3.0, ni à partir de la clé du monde planté. Les champs écrits par programme ne dépendent que de l'engagement scellé de la tentative, de la tranche d'épreuve du monde en cours, du fichier brut de l'exécution et du journal des coûts. Aucun champ du registre n'est une entrée d'un juge. » C'est la lecture conjointe du point 5 de N-053 et du point 2 de N-058 (aucun score de juge dans la sélection de l'agent), étendue au juge statistique et à la clé de l'oracle.

**Ce que l'essai teste** (cas sain et artefact, règle R5) :
- sain : sur un journal de course rejoué, permuter toutes les sorties des juges à modèle et du juge statistique, puis remplacer la clé du monde par une autre en gardant les mêmes données d'évolution, laisse les champs écrits par programme **identiques à l'octet** ;
- artefact : une version fautive de la fonction d'écriture, qui lit un verdict de juge, une promotion du juge statistique ou la clé, fait échouer l'essai ;
- ce que l'essai ne teste pas, et que le texte ne doit pas prétendre : les champs écrits par le proposeur dépendent de ce qu'il a lu, qui peut dépendre de tout. L'invariant porte sur les champs écrits par programme et sur les entrées de la fonction, pas sur la pensée du proposeur.

**Ce qui reste un nœud** (§ 12, question 2) : la garde « la mémoire ne sert jamais un verdict ». La classe d'issue d'un test de mort et le champ `gardee` ne sont pas des verdicts de juge, et le complément 3 les nomme dans l'objet (« résultats écrits par programme », « gardée »). Mais servis à la génération suivante, ils disent ce qui a tenu. Une carte (`fed7a993d9671`) relève le même point pour la sélection des survivants servie ; la proposition note, pour une autre ligne, qu'étendre ce que la mémoire sert au verdict du test de mort est un nœud. Repli écrit si la réponse est non : `resultat` et `gardee` restent écrits sur disque pour l'analyse et ne sont **pas servis** ; le registre servi ne dit alors que ce qui a été tenté, pourquoi, et avec quelle prédiction.

### 3.2 Correction 2 — la prédiction, son taux de base, et le grain du retour

**Défauts.** (i) La prédiction était un signe et une tranche, donc une catégorie ponctuelle, alors qu'une règle de score propre exige des probabilités. (ii) Le taux de base par permutation entre tentatives est dégénéré si les proposeurs prédisent presque toujours la même chose. (iii) Le « changement du score de l'oracle dû à une tentative » n'a pas d'objet mesurable quand le monde change à chaque génération. (iv) Un score servi sous la forme k sur m laisse lire m, le nombre d'items plantés.

**Choix.**

- **Objet de la prédiction** : l'issue du test de mort **de cette tentative, sur la tranche d'épreuve du même monde** (§ 3.0). L'objet est défini par tentative, sur un seul monde ; il ne compare plus deux générations. Le défaut (iii) disparaît.
- **Forme** : une probabilité par classe, sur la liste fermée des trois classes du § 3.0, en dixièmes, de somme un. Aucun texte libre, aucun identifiant d'item. Le programme refuse une prédiction mal formée ; il refuse d'éprouver une tentative sans empreinte de prédiction, et d'écrire un résultat dont la prédiction ne correspond pas à l'empreinte (garde éprouvée sur un cas sain et sur une prédiction modifiée après coup).
- **Justesse** : score quadratique à plusieurs classes (Brier, 1950 ; référence classique, non lue sur source au dépôt), qui est une règle de score propre pour cette forme.
- **Taux de base, indépendant des prédictions** : la prévision constante égale aux fréquences des classes observées **dans les autres sources**, même bras (une source laissée de côté à tour de rôle). Seconde référence, rapportée à côté : la prévision uniforme. Aucune permutation des prédictions.
- **Cas dégénéré, dit d'avance** : si plus de neuf prédictions sur dix d'un bras sont identiques, la ligne est rapportée « prédiction non informative » et n'est pas interprétée.
- **Statut** : la justesse des prédictions est **rapportée, sans seuil**, par génération et par bras (les trois, § 2), avec un intervalle par rééchantillonnage des sources. Elle n'entre dans aucun signal de sélection ni de récompense, et dans aucune règle du registre.
- **Grain** : le retour ordinaire et le champ `resultat` portent une **classe par tentative** et un coût. Jamais une fraction, jamais un compte rapporté à un total d'items plantés, jamais la valeur de la statistique ni la distance au seuil. Comme la clé du monde n'est pas une entrée de la fonction d'écriture (§ 3.1), m ne peut pas y passer. Le défaut (iv) est fermé par construction, et un essai le garde : la sérialisation du registre et du retour ne contient aucun champ numérique hors des probabilités prédites, du seuil que le proposeur a lui-même écrit et du coût.

**Ce que la correction coûte.** La prédiction porte sur le test de mort, non sur la vérité plantée. Une prédiction juste dit que le proposeur connaît son épreuve, pas qu'il trouve des lois vraies. C'est voulu : la justesse est une description du registre, pas une mesure de découverte.

### 3.3 Correction 3 — le plancher du nombre de sources

**Défaut.** Le plan d'origine faisait dépendre le nombre de sources du seul pilote de bruit. Or le test des rangs signés exact, joint à la procédure de Holm sur deux contrastes, impose un plancher quel que soit le bruit.

**Calcul** (`calcul_devis_heritage_v2.py`, `5d21b393f03f3e859241d97dea8347937596422c42f6b9f3cc4e5f5661b1a1c9` ; sortie `calcul-devis-heritage-v2.json`, `132a07649dd6d572ad50e5bc6c41a73fee9d54a8bcceef996192fb886b1dca6b`, champ `rangs_signes_exact` ; sans différence nulle ni ex æquo ; les quatre premières colonnes sont identiques à celles de la v1, programme `782a86104b518eb5a4a616111ec6fb50d70ac713bf58138013c1b27291b4b186`, sortie `02bae7980cbba40fb83ea7f30d732e11f9880c24fca3c4a1913b4b8923231765`) :

| sources | plus petite valeur p bilatérale | plus grande somme de rangs qui passe 0,025, bilatéral | plus grande somme de rangs qui passe 0,05, bilatéral | plus petite valeur p unilatérale | plus grande somme des rangs contraires qui passe 0,05, unilatéral |
|---|---|---|---|---|---|
| 5 | 0,0625 | aucune | aucune | 0,03125 | 0 |
| 6 | 0,03125 | aucune | 0 | 0,015625 | 2 |
| 7 | 0,015625 | 0 | 2 | 0,0078125 | 3 |
| 8 | 0,0078125 | 2 | 3 | 0,00390625 | 5 |
| 10 | 0,001953125 | 5 | 8 | 0,0009765625 | 10 |
| 12 | 0,00048828125 | 10 | 13 | 0,000244140625 | 17 |
| 16 | 0,000030517578125 | 25 | 29 | 0,0000152587890625 | 35 |

Avec six sources ou moins, le plan ne peut conclure sur aucun contraste. Avec sept, il ne conclut que si les sept différences ont le même signe. Les deux dernières colonnes servent la règle de validité à dose nulle, devenue unilatérale (§ 5, § 8) : elle peut se déclencher dès cinq sources à dose nulle, et seulement si les cinq écarts sont positifs.

**Choix.**
- **Plancher : dix sources** à dose de dépendance non nulle, **quel que soit le résultat du pilote de bruit**. **Recommandation : douze**, pour garder dix différences utiles si des différences sont nulles ; le coût n'étant plus à lui seul une raison de choisir dix, c'est douze que le devis chiffre. Le nombre retenu sort d'une règle écrite, qui ne peut que le relever (§ 8.0).
- **Différences nulles** : les scores de l'oracle sont des comptes, donc des différences nulles sont probables. Leur traitement est gelé : méthode de Pratt (1959 ; référence classique, non lue sur source au dépôt) — les zéros sont classés avec les autres, puis leurs rangs sont retirés —, la loi exacte étant calculée par programme sur les rangs restants. Les ex æquo reçoivent le rang moyen, et la loi exacte est énumérée sur les rangs observés.
- **Un seul test décide par contraste** : rangs signés exact, bilatéral, sur les différences appariées par source, **sur le monde final seulement**. Deux contrastes (héritage, tenue), risque global de 5 % par la procédure de Holm (1979 ; référence classique, non lue sur source au dépôt) : la plus petite valeur p est comparée à 0,025, l'autre à 0,05 si la première passe.
- **La conséquence de coût est dite au devis.**

## 4. Ce qui vient des cartes

Aucun élément n'est versé ou écarté sur la note ou le verdict d'un juge de la course v9 : les éléments sont pris pour ce qu'ils apportent à l'épreuve, et écartés pour les raisons écrites ci-dessous.

### 4.1 Éléments versés

| élément | carte source | où il est versé | ce qui est gardé |
|---|---|---|---|
| Dose de lois héritables plantée, avec une **dose nulle** qui invalide la lecture si un écart positif y apparaît | `fed7a993d9671` | § 5 et § 8, règle de validité | la fraction ρ des lois vraies de la cible qui reprennent des lois de la source, à plusieurs valeurs dont zéro |
| Mondes à **dépendance plantée** et mondes **sans dépendance** | `fc1f059e8873e` ; variante dans un même monde, `f7a4918afe116` | § 5 | une part de mondes où les lois de la cible sont composées de lois de la source, une part où elles en sont indépendantes ; contrôle de construction : l'écart doit se concentrer là où la dépendance est plantée |
| **Répondeur scripté** qui ne réussit que s'il lit le vrai retour | `f7219bb36cfcb` | § 7, témoin de puissance | un proposeur écrit par programme, sensible par construction au contenu du registre ; s'il n'est pas distingué entre les bras, la mesure n'a pas la puissance de dire quoi que ce soit |
| Lecture au quart du budget, à mi-budget et à l'échéance | les neuf cartes | § 6 et § 8, lecture descriptive | séparer un effet de départ d'un effet à l'échéance, sur une même mesure ; seul le monde final décide |
| Registre factice de même forme, pris à un monde disjoint | `fed7a993d9671`, `f0d21fb62aff2` | § 9, bras de diagnostic | séparer le contenu de la seule présence d'un texte de même forme ; ici, le registre d'une **autre source**, sans seuil |
| Les copies ne comptent pas | `fdfac3afd4bae`, `f0d21fb62aff2` | § 6 | une loi vraie du monde final identique à une tentative du registre de la source n'est comptée pour aucun bras |
| Garde de troncature par bras | `f0d21fb62aff2`, `f760c773d6f15` | § 8, liste d'arrêt | réponses vides ou tronquées comptées par bras ; lecture refusée si les taux diffèrent au-delà d'une marge gelée |
| Double appariement, en appels puis en dollars | `f760c773d6f15` | § 8, lecture secondaire | si l'ordre des bras s'inverse entre les deux appariements, la mesure ne sépare pas le registre du calcul, et c'est dit |
| Audit du générateur des mondes avant toute lecture | `f7a4918afe116`, `fc1f059e8873e`, `f11193560f4d4` (N-073, § 4) | § 5 | la présentation seule ne doit pas trahir la classe d'une loi ni la dose |

### 4.2 Éléments écartés, et pourquoi

| élément des cartes | cartes | raison |
|---|---|---|
| Servir à la génération suivante la **sélection des survivants** (cartes « survit », avec ou sans étiquette) | les neuf, à des degrés divers | l'objet du complément 3 est un registre des tentatives, non une sélection ; une sélection de survivants transmet un verdict agrégé (garde « la mémoire ne sert jamais un verdict ») |
| Règle « la sélection n'est servie que si le bras vrai dépasse… », porte qui décide de la transmission | `fdfac3afd4bae`, `f7a4918afe116`, `f11193560f4d4` | sert une décision de production sur un agrégat ; ce plan mesure et ne câble rien |
| Critère compté sur les lois « promues par la règle à e-valeurs » ou par le juge statistique | `f0d21fb62aff2`, `f473bb6a03ca3`, `f11193560f4d4` | la mesure se fait par l'oracle, par appariement programmé à la loi plantée (§ 6), et l'épreuve du registre est le test de mort, non le juge statistique (§ 3.0) ; le juge au nul reste hors de ce plan (N-067, N-071) |
| Vidage sur déclencheur, réducteur de ce qui est servi, dose d'appels sans mémoire | `f473bb6a03ca3`, `f760c773d6f15`, `f11193560f4d4` | mécanismes d'exploration, autre question ; seule leur parade est gardée (mondes de contrôle, double appariement, troncature) |
| Base « meilleur de N tirages à coût égal » comme critère décisif | plusieurs | condition du programme, pratique publiée et citée (N-073, § 2 ; Oved, Pony, Naparstek, Barzelay, arXiv 2610.23977), tenue à part de ce plan (§ 12, question 5) |
| La lettre d'origine de N-073, § 1, que les cartes recopient, et les voisins qu'elles citent sans les avoir lus | les neuf | lettre remplacée par les compléments 1 à 3 ; voisins non vérifiés (règle R7) |

## 5. Les mondes plantés

- **Paires source et cible.** Pour chaque source : un monde source, puis une suite de mondes cibles neufs, un par génération de la continuation, et un monde final tenu à l'écart, lu une seule fois. Lois vraies et lois fausses plantées de chaque côté.
- **Dose de dépendance ρ.** Une fraction ρ des lois vraies de chaque monde cible, **monde final compris**, est composée, par construction, de lois vraies du monde source ; le reste en est indépendant. Sur processeur : ρ dans {0 ; 0,25 ; 0,5}. À l'étage payant : une seule dose non nulle, fixée après l'étage sur processeur, et la dose nulle.
- **Mondes avec et sans dépendance.** Les sources à ρ non nul portent les deux contrastes du critère. Les sources à ρ nul ne portent que la **règle de validité**.
- **La règle de validité, et sa raison exacte.** À dose nulle, le registre hérité ne contient, par construction, aucune loi dont une loi de la cible soit composée. Un écart d'héritage **positif** n'y peut donc pas venir de la dépendance plantée. Il vient **de la forme** (longueur du contexte, présence d'un texte) **ou d'un savoir-faire général transmis** : la forme d'engagement que le test de mort exécute, les classes de lois fausses qui « tiennent » à tort, la longueur utile d'une tentative. Ce savoir-faire peut être un héritage réel. **Le plan ne mesure que l'héritage spécifique à la dépendance plantée ; un savoir-faire général invalide la lecture au lieu d'être mesuré.** C'est une borne, portée au § 10.
- **La règle est unilatérale.** La lecture est invalide si, sur les sources à dose nulle, l'écart d'héritage est **positif** au test des rangs signés exact, unilatéral, au seuil de 0,05, sans correction. Un écart **négatif** à dose nulle est attendu : c'est le coût de lecture (§ 2). Il est rapporté, et comparé à l'effet du seul coût mesuré sur le proposeur scripté qui paie sa lecture sans la lire (§ 7).
- **Contrôle de construction dans un même monde.** Aux doses non nulles, l'écart d'héritage est aussi calculé à part sur les lois dépendantes et sur les lois indépendantes. Il doit se concentrer sur les premières. Réserve : chercher les lois dépendantes peut déplacer l'effort loin des indépendantes ; un écart négatif sur celles-ci n'est donc pas, seul, un effet de forme. C'est pourquoi la règle de validité repose sur les mondes à dose nulle et non sur ce contrôle.
- **Rien de la dose n'est servi.** Ni ρ, ni la classe d'une loi, ni le nombre de lois plantées ne figurent dans ce qu'un agent reçoit.
- **Audit du générateur avant toute lecture** (N-073, § 4) : un programme vérifie qu'un classifieur simple sur la présentation seule ne sépare ni les lois vraies des fausses, ni les dépendantes des indépendantes, ni les mondes par dose, au-delà du hasard, à une marge gelée. Il vérifie aussi qu'aucune loi du monde final n'est identique à une loi du monde source (§ 6). La dépendance plantée est fabriquée par nous et peut ne pas ressembler à une dépendance réelle : c'est une borne de la revendication.

## 6. L'oracle sur monde planté

- **Mesure principale** : sur le monde final tenu à l'écart, le **nombre de lois vraies plantées distinctes retrouvées** par le bras pendant la génération finale. « Retrouvée » se décide par programme : l'engagement scellé d'une tentative est apparié à une loi plantée par le comparateur de l'oracle. Aucun modèle n'intervient.
- **La génération finale, sa mécanique.** Après les générations de la continuation, chaque bras joue **une génération de plus, sur le monde final**, à budget égal par bras, par la règle 6 du § 2. Aux bras 2 et 3, le registre est servi **en lecture seule, gelé dans l'état de la fin de la continuation** ; au bras 1, l'historique ordinaire de la continuation, gelé de même. **Rien de cette génération n'est écrit dans un registre ni rendu à un agent** : ni tentative, ni résultat. Le monde final porte la même dose ρ et la même construction que les mondes cibles de sa source. Ses graines sont dérivées par source et communes aux trois bras ; les graines d'échantillonnage sont dérivées par bras (règle R9). Il est lu une seule fois, à l'échéance, par le programme d'analyse.
- **Les copies ne comptent pas — règle symétrique, gardée comme garde.** L'ensemble exclu est fixé **par source, avant toute lecture, et il est le même pour les trois bras** : toute loi plantée du monde final que le comparateur de l'oracle apparie à une tentative du registre de la source. Ce que la règle garde : un générateur qui placerait dans le monde final une loi de la source à l'identique, que le bras 3 pourrait recopier sans rien trouver. Par construction cet ensemble doit être vide — les lois dépendantes sont composées de lois de la source, non identiques à elles —, et l'audit du générateur le vérifie (§ 5). Sa taille est rapportée par source ; s'il n'est pas vide, les lois exclues ne comptent pour aucun bras, et le défaut du générateur est rapporté.
- **Lois fausses** : après la génération finale, le noyau fait passer le test de mort aux tentatives de cette génération, hors de tout registre ; le nombre de lois fausses plantées engagées et classées « tient » est rapporté par bras. **Condition jointe, gelée au préenregistrement avec une marge chiffrée** (valeur proposée : la hausse médiane des lois fausses tenues, bras 3 moins bras 2, ne dépasse pas une loi et reste strictement inférieure à la hausse médiane des lois vraies retrouvées ; de même pour la tenue). Au-delà, un écart positif n'est pas lu comme un succès (§ 8).
- **Volet des témoins jugés de l'oracle de N-058** (témoins vrais promus, faux rejetés par le juge) : **hors de la mesure principale et de tout critère**. Il est rapporté, comme information seulement, si des juges à modèle sont joués (option du devis) ; aucun juge ne lit alors un registre (§ 1). À confirmer (§ 12, question 3).
- **Lectures intermédiaires, sur une seule et même mesure.** Sur les **mondes d'évolution** de la continuation, on calcule après coup le nombre cumulé de lois vraies plantées distinctes retrouvées par le bras, à trois coupures du **budget cumulé de la continuation dans le journal des appels** : le quart, la moitié, et la totalité (l'échéance de la continuation). Une coupure est un montant de dépense dans le journal, pas une génération. L'effet de départ se lit sur ces trois points seuls. **Le monde final décide seul, à part** ; il n'est jamais comparé à un point intermédiaire. Ces lectures ne sont servies à aucun agent et ne décident de rien.
- **Jamais** le verdict d'un juge sur un agent ou sur un bras ; l'oracle n'écrit rien dans le registre (§ 3.1).

## 7. L'étage sur processeur, qui précède : répondeurs scriptés

**Aucun appel de modèle, 0 USD.** Il éprouve l'instrument, pas l'héritage chez de vrais proposeurs. Il demande son préenregistrement (règle R1, simulation comprise) et sa contre-lecture (règle R2).

**Banc.** Le générateur des mondes du § 5 ; un exécuteur simulé du test de mort du § 3.0 (engagement, tranche d'épreuve, statistique, seuil, trois classes) ; un compteur de coût simulé où lire un registre retire des appels par la règle 6 du § 2 ; cinq proposeurs écrits par programme :

| proposeur scripté | ce qu'il fait | ce qu'il doit montrer |
|---|---|---|
| le lecteur | compose ses tentatives à partir des entrées du registre qui ont tenu ; ne trouve les lois dépendantes que s'il lit le vrai registre de la source | **témoin de puissance** : écart d'héritage positif aux doses non nulles, croissant avec ρ ; à ρ = 0, l'effet du seul coût de lecture |
| le sourd, en deux variantes | ignore tout registre. **Le sourd qui paie** perd des appels par la règle 6 ; **le sourd à appels égaux** n'en perd aucun (la lecture ne retire rien) | le sourd qui paie mesure **l'effet du seul coût de lecture** : écart d'héritage attendu négatif, rapporté par dose et par règle de retrait. Le **niveau** de la procédure se mesure sur le sourd à appels égaux |
| le suiveur de forme | change de conduite dès qu'un registre non vide est présent, sans en lire le contenu | **artefact planté** : la règle de validité à dose nulle doit se déclencher |
| le généraliste | tire du registre une règle générale (par exemple : n'engager que la classe de lois que l'épreuve exécute), sans lire le contenu spécifique | **savoir-faire général transmis** : la règle de validité se déclenche-t-elle sur lui, et à partir de quelle force ? À savoir et à écrire avant l'étage payant |
| le copieur | recopie les entrées du registre comme tentatives | zéro loi retrouvée de plus ; l'ensemble exclu du § 6 est vide quand le générateur est sain, non vide sur un générateur fautif planté |

**Ce que l'étage établit, chaque point avec son cas sain et son artefact (règle R5) :**
1. La puissance : pour le lecteur, la part des tirages où la procédure du § 8 conclut, sur une grille de nombres de sources (10, 12, 14, 16, 20, 24, étendue par programme si besoin) et de tailles d'effet réduites (écart moyen divisé par l'écart-type des différences entre deux courses identiques).
2. Le niveau : pour le sourd à appels égaux, le taux de rejet de la procédure entière (rangs signés exact, méthode de Pratt, procédure de Holm).
3. La règle de validité à dose nulle : son taux de déclenchement sur le sourd à appels égaux, sur le sourd qui paie, sur le suiveur de forme et sur le généraliste, selon le nombre de sources à dose nulle.
4. La part de différences nulles attendue avec des scores en comptes.
5. Les gardes du registre : invariant du § 3.1 dans ses deux sens (octet pour octet), scellement de la prédiction, chaîne d'empreintes, arrêt sur historique de départ non vide, cloisonnement des dossiers, grain du § 3.2, champs du bras 1 jamais servis, génération finale sans écriture.
6. Le contrôle de construction : l'écart du lecteur se concentre sur les lois dépendantes.
7. Le repli du § 3.1 : avec un registre servi sans `resultat` ni `gardee`, le lecteur trouve-t-il encore quelque chose ? Si non, le repli vide la question, et c'est à savoir avant de trancher la question 2 du § 12.
8. L'effet du seul coût de lecture, sur le sourd qui paie, pour la règle de retrait de la v2 et, à titre de comparaison, pour celle de la v1.

**Issue de l'étage : une table gelée, à seuils chiffrés.** Le plan fixe la forme et propose les valeurs ; le préenregistrement de l'étage les gèle avant tout tirage. Le nombre de tirages par case est fixé d'avance (valeur proposée : 10 000) ; les intervalles sont des intervalles binomiaux exacts à 95 %.

| critère | seuil proposé |
|---|---|
| C1 — niveau, sur le sourd à appels égaux, à chaque nombre de sources de la grille | taux de rejet au plus 0,05, et borne haute de l'intervalle au plus 0,06 |
| C2 — puissance du lecteur, pour chacun des deux contrastes, à la **taille de référence** : un écart moyen égal à un écart-type des différences entre deux courses identiques | au moins 0,8 ; rapportée à 10 et à 12 sources, puis à chaque nombre de la grille |
| C3 — règle de validité sur le suiveur de forme, à dose nulle | déclenchée au moins 8 fois sur 10 |
| C4 — règle de validité sur le sourd à appels égaux et sur le sourd qui paie | déclenchée au plus 1 fois sur 20, borne haute de l'intervalle au plus 0,06 |
| C5 — contrôle de construction, sur le lecteur | au moins 8 dixièmes de l'écart d'héritage portés par les lois dépendantes |
| C6 — gardes du point 5 | toutes tenues, cas sain et artefact |

| issue | condition |
|---|---|
| **« à reconstruire »** | C1, C4 ou C6 en échec ; ou C3 ou C5 en échec à tout nombre de sources de la grille |
| **« non lisible »** | C1, C3, C4, C5 et C6 tenus, mais C2 n'est atteint à aucun nombre de sources de la grille étendue : le plan n'a pas la puissance de répondre à la taille de référence, et il se reconstruit avant toute dépense |
| **« lisible, à n sources et m sources à dose nulle »** | tout est tenu ; **n** est le plus petit nombre de la grille, au moins égal à 10, où C2 est atteint pour les deux contrastes ; **m** est le plus petit nombre où C3 et C4 sont tenus ensemble (au moins 5, par la table du § 3.3) |

Le nombre de sources à dose nulle de l'étage payant est ce m ; il ne se lit pas librement. Le résultat sur le généraliste est rapporté à part : s'il déclenche la règle de validité, le texte de l'étage payant dit d'avance qu'une lecture invalide peut venir d'un savoir-faire général, et non seulement de la forme.

**Ce qu'il ne dit pas.** Des proposeurs scriptés ne sont pas des modèles ; l'effet planté est choisi par nous. Une issue « lisible » ne prédit ni le signe ni la taille de l'héritage chez de vrais proposeurs.

## 8. Le pilote de bruit, puis l'étage payant

### 8.0 Le pilote de bruit — un étage payant à part

Le pilote emploie de vrais proposeurs : il se paie. **Il a son propre préenregistrement à venir (scellé et contre-lu), son devis et sa ligne d'accord.** Aucun appel du pilote ne part avant cette ligne.

- **Ce qu'il mesure** : l'écart entre deux courses identiques. Pour une même source, un même bras et une même suite de mondes, deux continuations **jumelles** ne diffèrent que par leurs graines d'échantillonnage ; la différence de leur mesure principale (§ 6) est une différence « à effet nul » par construction.
- **Dessin** : des sources de pilote à la dose non nulle retenue ; pour chacune, une course source, puis les trois bras joués chacun deux fois, soit trois paires de jumelles par source.
- **Nombre de paires, gelé.** Une paire seule, comme la v1 le comptait, ne donne aucun écart-type. Avec k différences de moyenne nulle connue, la borne haute à 95 % de l'écart-type vaut l'estimation multipliée par un facteur (`calcul-devis-heritage-v2.json`, champ `pilote_borne_haute_de_l_ecart_type`, loi normale supposée) : 2,92 à trois paires, 1,92 à six, 1,65 à neuf, 1,52 à douze. À trois paires, la borne vaut presque trois fois l'estimation : elle ne dimensionne rien. **Plancher : six paires (deux sources de pilote). Recommandation : neuf paires (trois sources).**
- **Ce que le pilote ne lit pas.** Son programme d'analyse ne calcule que des différences entre jumelles d'un même bras. **Aucune différence entre bras n'y est calculée ni lue** : ce serait lire le résultat de l'étage payant avant son scellement (règles R1 et R3). Les sources du pilote ne sont jamais réemployées par l'étage payant. Garde éprouvée sur un cas sain et sur un artefact (règle R5).
- **Ce qu'il rend** : l'écart-type des différences entre jumelles, par bras et tous bras réunis ; sa borne haute à 95 % ; la part de différences nulles ; les coûts de référence par appel de chaque espèce sur monde planté (règle 6 du § 2) ; le coût réel du test de mort par tentative ; la taille mesurée d'un registre de source.
- **La règle chiffrée qui tire le nombre de sources.** Le préenregistrement du pilote gèle, avant tout appel, la **taille de référence en lois** de l'étage payant (valeur proposée : une loi vraie retrouvée de plus par source sur le monde final). Après le pilote : taille réduite visée = taille de référence en lois divisée par la borne haute de l'écart-type. Le nombre de sources à dose non nulle est **le plus petit nombre de la table de puissance de l'étage sur processeur, au moins égal à dix, où la puissance des deux contrastes atteint 0,8 à cette taille réduite**, majoré de la part de différences nulles observée et arrondi à l'entier supérieur. Si la table ne va pas assez loin, elle est étendue par programme. **Ce nombre et son devis sont portés à Lazar tels quels : le coût est rapporté, il n'arrête pas la règle à lui seul.**

### 8.1 Conditions préalables de l'étage payant, toutes requises, dans cet ordre

1. étage sur processeur lu, issue « lisible, à n sources et m sources à dose nulle » (§ 7) ;
2. boucle fermée dans l'organisme : la génération suivante lit réellement un registre, et les tests de mort sont branchés sur le lanceur et éprouvent toute tentative (§ 3.0) — ce que la proposition (§ 6, écart 5) dit non fait à ce jour ;
3. générateur des mondes audité (§ 5) ;
4. questions du § 12 tranchées ;
5. **pilote de bruit joué sous son propre préenregistrement, son devis et sa ligne d'accord** (§ 8.0), et lu ;
6. préenregistrement de l'étage payant scellé et contre-lu, devis de l'étage accepté, ligne d'accord neuve.

**Ce que le préenregistrement de l'étage payant porte, pour chaque contraste** : une prédiction chiffrée — un signe attendu et un ordre de grandeur, tirés de l'étage sur processeur et du pilote —, avec l'indice contraire de Qin et al. dit avec sa prémisse (§ 11). Aucun signe n'est visé (règle R3) : la prédiction est écrite pour être confrontée, pas pour être obtenue.

### 8.2 Dessin

Le nombre de sources à dose non nulle que rend la règle du § 8.0 (dix au moins ; douze recommandées et chiffrées au devis), trois bras, trois générations au moins puis la génération finale ; les m sources à dose nulle que rend l'étage sur processeur, bras 2 et 3 seulement. Chaque source demande d'abord sa course source, qui produit le registre hérité.

### 8.3 Analyse, et table de lecture gelée

- Deux contrastes décisifs sur le monde final, sur la mesure du § 6 : héritage et tenue ; test et multiplicité du § 3.3.
- Règle de validité unilatérale du § 5, sur les sources à dose nulle.
- Lectures descriptives, sans seuil : bras 3 moins bras 1 ; les trois coupures du budget sur les mondes d'évolution (§ 6) ; l'écart par classe de lois ; la lecture à nombre d'appels égal, par troncature du journal, à côté de la lecture à dollars égaux ; l'écart à dose nulle comparé à l'effet du seul coût ; le score par dollar dépensé ; la justesse des prédictions dans les trois bras (§ 3.2) ; le gain du dernier doublement du budget par bras.
- Liste d'arrêt : plafond de dépense ; taux de réponses vides ou tronquées qui diffère entre bras au-delà de la marge gelée ; historique de départ non vide ; chaîne d'empreintes rompue ; garde du générateur en échec ; une écriture dans un registre pendant la génération finale.

**Étape 1 — conditions de lecture.** Si l'une manque, la lecture entière est **« invalide »** :

| condition | échec |
|---|---|
| troncature | les taux de réponses vides ou tronquées diffèrent entre bras au-delà de la marge gelée |
| chaîne d'empreintes | rompue dans un registre, ou prédiction non conforme à son empreinte |
| générateur | audit en échec, ou ensemble exclu du § 6 non vide au-delà du seuil gelé |
| règle de validité | écart d'héritage positif à dose nulle, au seuil unilatéral de 0,05 |

**Étape 2 — par contraste, si la lecture est valide :**

| procédure de Holm | médiane des différences | condition des lois fausses | lecture |
|---|---|---|---|
| passe | positive | tenue | **« établi »** |
| passe | positive | non tenue | **« non lu comme succès »** : l'écart s'accompagne d'une hausse des lois fausses tenues au-delà de la marge |
| passe | négative | — | **« effet négatif établi »** |
| ne passe pas | — | — | **« non établi »** ; jamais « effet nul » |

Une médiane nulle alors que la procédure passe est rapportée telle quelle, sans lecture.

**Ce qui réfuterait.**
- Héritage : le contraste (bras 3 moins bras 2) est « non établi » ou « effet négatif établi ». Le registre transmis n'a alors pas d'effet établi au-delà de la tenue, de l'organisme hérité et du coût de sa lecture.
- Tenue : le contraste (bras 2 moins bras 1) est « non établi » ou « effet négatif établi », à budget égal.
- Un effet présent au quart du budget et absent à la totalité, **sur les mondes d'évolution**, est rapporté comme effet de départ ; il ne vaut pas succès, et ne change pas la lecture du monde final.
- Un résultat trop propre déclenche le même audit qu'un échec (règle R4). Un résultat négatif se rapporte tel quel ; aucune reprise ne vise un signe (règle R3).

**Après une lecture invalide.** Elle est **rapportée telle quelle**, avec sa cause ; ce n'est ni un succès ni un échec de l'héritage. Une épreuve reconstruite est **un préenregistrement neuf, sur des sources neuves**, avec son devis et sa ligne d'accord ; aucune donnée de la lecture invalide n'y est réemployée, et aucune reprise ne vise un signe (règles R3 et R4).

## 9. Bras de diagnostic

À part des trois bras du critère, sans seuil, sur devis à part, joués après eux, sans effet sur aucun verdict. Repris du plan d'origine : résultats permutés entre entrées ; registre sans le champ de prédiction ; historique brut de la source laissé en place, sans registre ; entrées fausses plantées par l'orchestrateur (dans ce bras seulement) ; registre paraphrasé. Ajouté depuis les cartes : **registre d'une autre source**, de même forme et d'un monde disjoint, qui sépare le contenu de la présence. Les six se jouent d'abord sur processeur, avec les proposeurs scriptés, à 0 USD.

## 10. Ce que le plan ne revendique pas

- Aucune priorité. Toute mention de la forme se fait par la rédaction de la section C du complément 3 de N-073, recopiée à l'octet ; ce plan n'en dit rien de plus.
- Rien sur « l'héritage tout court » : seulement ce que le registre ajoute à un organisme qui hérite déjà par son code (§ 2, règle 1).
- **Rien sur un héritage de savoir-faire général** : le plan ne mesure que l'héritage spécifique à la dépendance plantée ; un savoir-faire général transmis invalide la lecture au lieu d'être mesuré (§ 5).
- **Rien sur le registre à coût nul** : chaque contraste est un écart à budget égal, coût de lecture compris (§ 2).
- Rien sur une mémoire contre rien : le bras 1 garde l'historique ordinaire de sa continuation, et écrit les mêmes champs sans les relire.
- Rien hors des mondes plantés : la dépendance est fabriquée, la dose n'a pas de réalisme vérifié, et le monde planté n'est pas une banque réelle.
- Rien sur le juge au nul formé des lois connues (N-067, N-071) : il est hors de ce plan ; ni la mesure ni le registre n'emploient sa règle de promotion (§ 3.0).
- Rien sur la valeur des tests de mort comme épreuve de vérité : « tient » dit qu'un engagement a passé son seuil.
- Rien sur un concepteur entraîné, des sondes ou des adaptateurs transmis, ni sur la diversité des fournisseurs.
- Rien sur la valeur d'un proposeur ou d'une espèce : aucune composition n'est choisie par ce plan (N-058).
- L'étage sur processeur ne revendique que la tenue de l'instrument.
- Aucune des neuf cartes n'est adoptée ; aucun mécanisme n'est câblé dans l'organisme.

## 11. Citations obligatoires de tout texte sortant tiré de ce plan

La lettre est celle de N-073, § 1, telle que les compléments 1, 2 et 3 l'ont remplacée ; la rédaction de la section C du complément 3 se recopie à l'octet. Les numéros de page sont ceux des décisions ; un texte sortant donnera les références complètes.

**N-073, § 1** : Wang et al., « Huxley-Gödel Machine », arXiv 2510.21614 ; Zhang, Hu, Lu, Lange, Clune, « Darwin Gödel Machine », arXiv 2505.22954 ; Robeyns, Szummer, Aitchison, « A self-improving coding agent », arXiv 2504.15228 ; Sutton et Barto ; Schmidhuber et Zhao (1996), Schmidhuber, Zhao et Wiering (1997), Kirsch et Schmidhuber (2022) — ces trois derniers à lire sur source avant de les citer comme antériorité.

**Indice contraire, à dire avec sa prémisse, dans les mots de N-073, § 1** : chez Qin et al. (arXiv 2611.05108), ce qui est légué rapporte surtout au départ (+24,0 au quart du budget) et presque plus à l'échéance (+1,2) (p. 6, tableau 8 p. 21, selon la lecture sur PDF). Ces deux chiffres sont ceux de la décision ; ce rédacteur ne les a pas relus sur le PDF. C'est pour cet indice que le plan lit trois coupures du budget (§ 6).

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

**Sous condition** :
- si un texte parle de ce que le registre **garde ses tentatives non gardées** : le complément 2, point 3, impose de lire d'abord sur source Xia et al., « RRSI », arXiv 2609.24972 (seconde main à ce jour) ;
- si un texte **présente l'organisme, son juge statistique ou ses tests de mort** : les citations obligatoires de N-067, section 6, et celles de N-071, point 5, s'appliquent. L'épreuve du § 3.0 n'est pas le juge statistique ; si la mère retenait la voie (a) du § 3.0, ces citations deviendraient obligatoires pour le plan lui-même ;
- Oved, Pony, Naparstek, Barzelay, arXiv 2610.23977, si la base des tirages indépendants à coût égal est jouée (N-073, § 2 : pratique publiée, citée) ;
- Brier (1950), Pratt (1959) et Holm (1979) pour les outils de statistique : références classiques, à vérifier sur source avant citation (règle R7).

## 12. Questions à la mère — celles marquées « nœud » sont des nœuds de Lazar, sans défaut

1. **(nœud) L'épreuve programmée est-elle bien les tests de mort ?** Choix du rédacteur : voie (b) du § 3.0, verdict calculé par le noyau, toute tentative éprouvée. Raison : c'est l'épreuve de l'organisme qui répond à la lettre du complément 3 sans faire entrer un juge dans le registre, sans dépendre de ce que chaque bras connaît déjà, et sans toucher la revendication du juge au nul. Prix : un branchement sur le lanceur, un appel payant par tentative de coût inconnu, et un changement déclaré de l'organisme. Les voies (a), juge statistique, et (c), épreuve neuve, sont décrites au § 3.0 avec ce qu'elles changeraient.
2. **(nœud) `resultat` et `gardee` peuvent-ils être servis ?** La garde « la mémoire ne sert jamais un verdict » se lit-elle comme interdisant les seuls verdicts de juge et la sélection des survivants (lecture de ce plan, appuyée sur la lettre du complément 3), ou aussi la classe d'issue d'un test de mort ? Repli écrit au § 3.1 ; l'étage sur processeur dira ce que le repli coûte (§ 7, point 7).
3. **(nœud) La mesure principale laisse de côté le volet des témoins jugés de l'oracle de N-058.** Est-ce une lecture permise de N-058 pour ce plan, ou un écart à porter comme tel ? Le principe « aucun verdict de juge comme critère » va dans le sens de ce plan. Le devis recommande de jouer les juges à modèle à l'étage payant pour rapporter ce volet comme information ; à confirmer ou à retirer.
4. **Deux contrastes décisifs.** La v1 posait comme option de ne garder que l'héritage, pour abaisser le plancher à six sources. Le coût n'étant plus à lui seul une raison, ce plan garde les deux contrastes et n'ouvre plus cette option ; la mère peut la rouvrir.
5. **(nœud) La base « tirages indépendants à coût égal »** (N-073, § 2) n'est pas un bras de ce plan. La jouer ici, comme quatrième bras descriptif sur devis, ou la tenir à l'épreuve qui lui est propre ?
6. **Composition des proposeurs.** Le devis recommande la composition de la course v9 (les cinq espèces) : c'est l'organisme tel qu'il existe, et aucune composition ne se choisit ici (N-058 ; tout changement de modèle demande un accord). À confirmer.
7. **Pilote de bruit** : neuf paires de jumelles, trois bras, trois sources de pilote jamais réemployées, aucune différence entre bras lue. Le dessin et la règle du § 8.0 conviennent-ils, et qui écrit son préenregistrement ?
8. **L'expérimentateur et le lecteur témoin des tests de mort sur monde planté** : la session de modèle qui écrit le script est-elle gardée telle que l'étage la prévoit, et le lecteur témoin, qui ne pèse pas sur le verdict, est-il joué ? Les deux se paient par tentative.
9. **Le principe de la ligne `GO-2026-11-19-60`** s'applique-t-il à cette question ? Il vise ce qui « améliore considérablement l'organisme », selon une définition scellée par un lecteur. Ce plan mesure ; il n'améliore l'organisme que par ce que sa réponse permettra de décider. Ce rédacteur a appliqué la procédure (coût rapporté, non réduit) sans se prononcer sur le caractère considérable.
10. *Hors nœud, à décider aux préenregistrements* : la dose non nulle de l'étage payant ; les marges (lois fausses, troncature, audit du générateur) ; la proportion de la tranche d'épreuve ; la forme admise des engagements ; ce qui est servi quand le registre dépasse la taille bornée ; les tailles de référence (§ 7, § 8.0).

## 13. Réserves du rédacteur

1. **Je n'ai pas lu le code.** J'ai lu le début du `README.md` de l'organisme et l'en-tête de deux modules des tests de mort. Je ne sais pas si un test de mort peut éprouver une loi d'un monde planté sans réécriture, ce que l'organisme reçoit aujourd'hui comme retour ordinaire, ni si le comparateur de l'oracle apparie un engagement à une loi plantée sans modèle. Les § 2 (règle 3), 3.0, 3.1, 3.2 et 6 en dépendent. À établir avant tout préenregistrement ; si les tests de mort ne conviennent pas, la voie (c) du § 3.0 est le repli, et c'est un nœud.
2. N-045 v2, N-049, N-050 et N-053 sont cités d'après le plan d'origine et sa vérification courte, non relus.
3. **Le choix du § 3.1 est une troisième voie**, hors des deux que la vérification courte proposait : le signal de l'oracle est remplacé par une épreuve sur les données. Il change ce que le registre contient par rapport au plan d'origine, qui y écrivait le score de l'oracle. Avec l'abandon du volet des témoins jugés dans la mesure principale, ce sont deux écarts de fond au plan d'origine, choix du rédacteur, à porter comme tels devant Lazar (§ 12, questions 1 à 3).
4. La règle de validité à dose nulle est faible avec peu de sources : à cinq, elle ne se déclenche que si les cinq écarts sont positifs. Sa puissance réelle est une sortie de l'étage sur processeur. Et elle ne distingue pas la forme d'un savoir-faire général (§ 5).
5. Le plancher de dix sources ne dit rien de la puissance pour un effet de taille réaliste ; il dit seulement en dessous de quoi le test ne peut pas conclure. Les tailles de référence proposées (un écart-type entre jumelles ; une loi par source) sont des propositions de rédacteur, sans appui mesuré.
6. La règle du § 8.0 suppose des différences entre jumelles de loi normale pour sa borne haute ; avec des scores en comptes, c'est une approximation, à éprouver sur processeur avant le pilote.
7. Le pilote mesure le bruit entre jumelles d'un même bras ; il suppose que ce bruit vaut pour une différence entre bras quand il n'y a pas d'effet. Rapporté par bras pour que l'écart à cette hypothèse se voie.
8. Les seuils du § 7 et la marge des lois fausses du § 6 sont des valeurs proposées ; aucune n'est gelée par ce plan.
9. Les cartes n'ont servi que par leurs éléments d'épreuve ; je n'ai pas vérifié qu'un autre élément utile ne se trouve pas dans les cartes que le mandat ne m'ouvrait pas.

## 14. Vérification des listes « Ne pas écrire » sur ce texte et sur le devis v2

Refaite pour la v2 par le rédacteur, par recherche de chaînes sur les deux fichiers avant scellement, puis relue ligne à ligne. **Le programme de recherche reste hors du dépôt, parce qu'il contient les formules interdites** ; il est dans le dossier de travail de la session et le contre-lecteur refera la recherche. Les lignes sont celles de la liste du complément 3, dans l'ordre, désignées par leur sujet et non recopiées.

| ligne de la liste | sujet | dans ce texte et dans le devis v2 |
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
| 11 | un chiffre calculé par un lecteur présenté comme chiffre des auteurs | les quatre chiffres nommés par la liste sont absents ; les seuls chiffres de la littérature sont les deux de Qin et al. au § 11, dans les mots de N-073, § 1, avec leur page et la mention « selon la lecture sur PDF » ; les autres chiffres sont ceux du test, du pilote et des coûts (programme joint) |

Vérifié aussi, formule par formule :
- la liste « Ne pas écrire » du point 4 du complément 2 (six formules sur Yu et al.) : aucune n'est employée ; aucun chiffre de Yu et al. n'est donné ;
- la liste « Ne plus écrire » de N-073, § 1 (cinq groupes de formules) : aucune n'est employée ; ce plan ne rend aucun signal à ce qui conçoit et ne crédite rien par ce qui en descend : il mesure un objet ;
- N-067, section 4 : rien du juge au nul n'est dit libre, ni dans le dépôt ni hors de lui ;
- N-071, point 4 : la phrase qu'il interdit dans un énoncé public est absente.

Vérification refaite après la dernière modification des deux textes. La recherche emploie des motifs plus larges que les formules (33 motifs) ; elle rend 17 occurrences à relire, 14 dans ce plan et 3 dans le devis, toutes relues : les lignes de la table ci-dessus qui désignent une formule par son sujet, des mots communs sans rapport avec les formules (réponses coupées avant leur fin, champ de texte non contraint, bras de diagnostic, phrase qui écarte la justesse de tout signal) et le montant de la course v9. **Aucune formule interdite n'est employée.** La même recherche ne trouve aucun identifiant de modèle dans les deux textes ; les noms d'espèce du devis sont les noms de rôle du manifeste, comme dans la v1.

## 15. Les dix-sept corrections de la contre-lecture — où, comment

| n° | gravité | constat | où | comment |
|---|---|---|---|---|
| 1 | B | épreuve programmée non définie | § 3.0 (neuf), § 1, § 3.1, § 4.2, § 10, § 11, § 12 (question 1), § 13 (réserves 1 et 3) | § 3.0 écrit : entrée, données, statistique, seuil, classes, exécutant ; **voie (b), tests de mort**, avec sa raison ; invariant étendu à tout juge, à modèle ou programmé ; changement de l'organisme déclaré ; « troisième voie » dite au § 3.1 et à la réserve 3 |
| 2 | B | coût de lecture, niveau du sourd, règle de validité | § 2 (ce qui est estimé ; règle 6), § 5, § 7, § 8.3 ; devis § 2 bis | estimande « à budget égal, coût de lecture compris » ; sourd qui paie et sourd à appels égaux ; règle de validité unilatérale ; retrait d'appels au plus près du coût, par permutation semée ; ligne d'information au devis |
| 3 | B | raison inexacte de la règle de validité | § 5, § 10, § 7 | raison réécrite (forme ou savoir-faire général) ; borne portée au § 10 ; cinquième proposeur scripté, le généraliste |
| 4 | B | « instrument lisible » non chiffré | § 7 | table gelée à six critères chiffrés et trois issues ; tirages fixés d'avance ; n et m tirés d'une règle écrite |
| 5 | M | pilote payant avant le devis ; taille qui n'estime rien | § 8.0 (neuf), § 8.1 (condition 5) ; devis § 3 et § 4 | pilote sous son propre préenregistrement, son devis, sa ligne d'accord ; six paires au moins, neuf recommandées, justifiées par la borne haute ; règle chiffrée du nombre de sources ; ligne du devis recalculée |
| 6 | M | lecture « oui » et « non » non tabulée ; prédiction chiffrée absente | § 8.1, § 8.3, § 6 | table en deux étapes ; condition des lois fausses gelée au préenregistrement avec marge proposée ; signe et ordre de grandeur par contraste au préenregistrement, Qin et al. avec sa prémisse, aucun signe visé |
| 7 | M | lectures intermédiaires sur une autre mesure | § 6, § 8.3 | même mesure sur les mondes d'évolution au quart, à la moitié et à la totalité ; coupure définie sur le budget cumulé du journal ; le monde final décide seul |
| 8 | M | mécanique du monde final | § 6, § 2, § 5 | génération finale à budget égal, registre gelé en lecture seule, aucune écriture, même dose, graines par source communes aux trois bras |
| 9 | M | le bras 1 écrit-il les champs ? | § 2 | oui : mêmes champs, scellés, sur disque, non servis ; la tenue isole le service |
| 10 | M | silence sur c.7 et c.8 | § 1 | table « ce qui est gardé de c.7 et c.8 » : aucun champ n'est une entrée d'un juge, balises de donnée, audit par une autre lignée ; ce qui est remplacé est dit |
| 11 | M | copies : symétrie non dite | § 6, § 5, § 7 | ensemble exclu fixé par source, le même pour les trois bras ; ce que la règle garde ; taille rapportée ; audit du générateur |
| 12 | m | carte citée pour un autre objet | § 3.1 | « une carte relève le même point pour la sélection des survivants servie » |
| 13 | m | paraphrase de la section C | § 10, puce 1 | remplacée par la phrase de la contre-lecture |
| 14 | m | citations à compléter | § 11 | prémisse de Qin et al. dans le texte ; Xia et al. sous condition ; N-067, section 6, et N-071, point 5, sous condition |
| 15 | m | empreintes manquantes ou tronquées | en-tête, § 3.3 ; devis, en-tête | empreintes entières du programme et de sa sortie (v1 et v2), de la proposition, des critères, de la lecture descriptive, de N-067, N-071 et N-058 |
| 16 | m | devis : colonne « minimal », défaut, pilote, appels perdus | devis § 0, § 2 bis, § 3, § 4, § 9 | colonne « minimal » retirée des totaux ; défaut réécrit ; pilote recalculé ; ligne d'information ajoutée |
| 17 | m | reprise après une lecture invalide | § 8.3 | rapportée telle quelle ; préenregistrement neuf, sources neuves, aucune reprise visant un signe |

## 16. Différentiel v1 → v2

- **En-tête** : statut « version 2 » ; principes de la ligne `GO-2026-11-19-60` et de l'erratum 1 ; pièces lues pour la v2 ; empreintes entières (correction 15).
- **§ 0** : cinq points au lieu de trois ; l'ordre des étages et le pilote à part.
- **§ 1** : `tentative`, `resultat`, `gardee` renvoient au § 3.0 ; « juge, à modèle ou statistique » ; table neuve « ce qui est gardé de c.7 et c.8 ».
- **§ 2** : colonne « champs écrits sur disque » ; alinéas neufs « ce qui est estimé » et « le bras 1 écrit les mêmes champs » ; règle 3, changement de l'organisme déclaré ; règle 4, épreuve comprise ; règle 6 réécrite ; génération finale ajoutée à la longueur.
- **§ 3.0** : neuf.
- **§ 3.1** : « une troisième voie » au lieu de « la première, durcie » ; entrées de la fonction précisées ; invariant étendu au juge programmé et au sens inverse ; carte citée pour son vrai objet.
- **§ 3.2** : l'objet de la prédiction est l'issue du test de mort sur la tranche d'épreuve ; justesse lue dans les trois bras ; grain précisé.
- **§ 3.3** : table étendue (cinq et seize sources, colonnes unilatérales) ; empreintes ; douze sources recommandées et chiffrées ; « sur le monde final seulement ».
- **§ 4** : phrase d'en-tête (aucun verdict de juge) ; lignes « dose nulle », « trois coupures », « copies », « critère compté sur les lois promues » ajustées.
- **§ 5** : raison de la règle de validité réécrite ; règle unilatérale ; dose du monde final ; audit des lois identiques.
- **§ 6** : mécanique de la génération finale ; copies symétriques ; condition des lois fausses gelée avec marge proposée ; lectures intermédiaires sur une seule mesure.
- **§ 7** : cinq proposeurs scriptés, le sourd en deux variantes ; point 8 ; table gelée des critères et des issues.
- **§ 8** : § 8.0 neuf (pilote) ; conditions réordonnées ; prédiction chiffrée au préenregistrement ; table de lecture en deux étapes ; suite d'une lecture invalide.
- **§ 10** : puce 1 remplacée ; trois puces ajoutées (savoir-faire général, coût de lecture, tests de mort).
- **§ 11** : prémisse de Qin et al. ; bloc « sous condition ».
- **§ 12** : neuf questions à la mère et une liste hors nœud, au lieu de cinq points ; les questions 1, 6, 7, 8 et 9 sont neuves ; l'option « un seul contraste » n'est plus ouverte par le plan.
- **§ 13** : neuf réserves au lieu de six.
- **§ 14** : vérification refaite, étendue à N-067 et N-071.
- **§ 15 et § 16** : neufs.
- **Rien n'est retiré de la v1** hors ce que les corrections remplacent ; la v1 et ses compagnons restent en place (règle R12).
