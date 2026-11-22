# Jugement sur le seuil de 0,75 du classifieur de style (« mathématiques nouvelles ») — v1

- Nature : avis de juge, étage 4 de la chaîne de décision (GO-2026-11-22-106 et -112), le 2026-11-22. Auteur : le juge de ce mandat (mandat de la mère adressé à une session Fable en effort maximal ; le modèle servi est relevé dans le message de remise à la mère, non ici). L'autre juge n'a pas été consulté ; rien de lui n'a été lu.
- Aucun appel de modèle, aucune dépense. Un diagnostic sur processeur, sur racines d'essai seulement (§ 2).
- Lu, empreintes vérifiées contre les compagnons :
  - la question servie, version 2 (`51344c2d…`) ; les synthèses (Carbon et Astra `01027f00…`, Neon `f0571a88…`) ; les trois réponses complètes (Carbon `aa66edef…`, Astra `c76d48a6…`, Neon `e0d77af8…`) ;
  - sur `main` (commit `4e47b5d69`) : R-4898, R-4931, R-4943, R-4979 à R-4985 ; GO-2026-11-22-77, -105, -106, -109, -112 ;
  - sur `claude/mathematiques-nouvelles-v1` (commit `3abbc7760`) : la note du code de la version 6 (`7c996b82…`) ; les modules `forme_seule.py` et `grammaire.py` du paquet figé (commit `35ac9e10`) ; le brouillon 4 du préenregistrement (`212c6eca…`) ; les notes au directeur (`06a92833…`) ; la sortie de la sonde « règle aveugle » (`e6ae3d49…`) ; la vérification des corrections du brouillon 4 (`69b8aa58…`) ; le mandat du brouillon 5 (`b59ffc1e…`).
- Non lu : le brouillon 5 (en cours, sa branche n'est pas sur le dépôt distant) ; aucune branche ni aucun fichier cloisonné.

## Verdict

1. La décision conditionnelle de Lazar tient : réviser le générateur, garder 0,75, garder la lecture « sur contre-exemples vérifiés » en repli. Neon ne la renverse pas ; il la précise sur quatre points, que je retiens en partie (diagnostic d'abord, critère complété, libellé borné du repli, relecteur).
2. Le seuil de 0,75 est gardé tel quel et il a déjà parlé pour la banque actuelle. Pour la banque révisée, il ne suffit plus seul : il devient une condition nécessaire parmi quatre, écrites avant toute mesure de cette banque.
3. Le fait qui pèse le plus n'était pas dans la question servie aux trois modèles : la lecture « sur contre-exemples vérifiés » a sa propre fuite. Une règle sans calcul y atteint déjà 80 à 91 % des faux. Le repli (a) est donc juste, mais il n'établit presque rien de lisible sur la banque actuelle ; c'est la meilleure raison de réviser la banque avant de payer les deux bras.

## 1. Ce que le dépôt dit, et que les trois modèles ne savaient pas

La question servie était neutre et courte. Cinq faits du chantier changent la lecture de leurs avis.

1. **La lecture « sur contre-exemples vérifiés » existe déjà, et elle est déjà symétrique.** Le brouillon 4 l'appelle « lecture en preuve ». Le bras nu reçoit le même schéma de sortie que le bras avec outil et passe par la même vérification exacte ; trois instances au plus par sortie, pour les deux bras. Elle vaut dans les deux branches du seuil. La « lecture en verdict » (verdicts déclarés) ne s'y ajoute que si l'aire est sous 0,75.
2. **Le plafond de recherche est donné aux deux bras.** L'énoncé se juge jusqu'à 3N, et ce nombre est écrit dans la consigne des deux bras. Aucun bras n'a besoin de la forme pour savoir qu'il faut chercher au-delà de N.
3. **Une règle aveugle fait presque tout le travail de la lecture en preuve.** Avancer trois instances sans évaluer l'énoncé (toutes les variables au plafond, à 1, à N + 1) donne un contre-exemple vérifié sur 60 à 68 des 75 faux, selon la racine d'essai. 20 des 24 gabarits de faux tombent à chaque fois : un seuil monotone dépassé est faux à toute instance assez grande. Quatre gabarits seulement résistent ; il reste 7 à 15 énoncés où un calcul est nécessaire (sonde, `e6ae3d49…`).
4. **Le relecteur ne pourra rien ajouter aux preuves**, une fois la remarque 30 de la vérification portée au brouillon 5 : il choisit et ordonne au plus trois instances parmi celles de l'agent, n'en ajoute aucune, et peut changer le verdict. La sortie de l'agent avant relecture est déjà gardée.
5. **Un énoncé par appel**, en contexte neuf, pour les deux bras. Un bras ne voit donc jamais les fréquences des gabarits.

Deux décisions de Lazar encadrent le sujet et ne s'accordent pas d'elles-mêmes : « go maths » (GO-2026-11-22-77) fait courir les deux bras « comme écrit », sur la banque actuelle, la version 7 étant mise au dossier du pilote 2 ; « go (b) » (GO-2026-11-22-109) demande de réviser le générateur. Le point 3.6 le porte.

## 2. Ce que j'ai vérifié moi-même

Script `juge-fable-max-v1-diagnostic-style.py` (`79c6d862…`), sortie `juge-fable-max-v1-diagnostic-style-sortie.txt` (`f159e02a…`) et son détail en JSON (`b717ae4f…`), même dossier. 41 racines d'essai distinctes, paquet figé de la version 6 lu sans changement, 58 secondes de processeur. **Ce diagnostic est de moi et n'est vérifié par personne** : à refaire par le vérificateur du code avant toute citation dans un texte scellé. Il retrouve la plage de l'équipe (aire qui fait foi de 0,939 à 0,982), ce qui est un contrôle partiel.

| mesure, sur les 41 racines | minimum | moyenne | maximum |
|---|---|---|---|
| aire qui fait foi (plus grande des deux strates, hors textes vus) | 0,939 | 0,966 | 0,982 |
| aire, tous textes, pièges contre vérités | 0,953 | 0,971 | 0,977 |
| aire, tous textes, faux tôt contre vérités | 0,872 | 0,893 | 0,905 |
| aire, tous textes, tous les faux contre vérités, première famille | 0,969 | 0,969 | 0,969 |
| même aire, deuxième famille | 0,932 | 0,957 | 0,984 |
| même aire, troisième famille | 0,792 | 0,865 | 0,898 |
| rappel du classifieur sur tous les faux, à fausses alarmes ≤ 0,10 (borne optimiste) | 0,583 | 0,737 | 0,792 |
| même rappel, à fausses alarmes ≤ 0,05 | 0,562 | 0,615 | 0,677 |
| règle sans apprentissage « nombre de chiffres du plus grand littéral » : aire, pièges contre vérités | 0,932 | 0,956 | 0,970 |
| même règle : aire, pièges contre faux tôt | 0,895 | 0,919 | 0,951 |

Ce que ces mesures et la lecture du code établissent :

- **La fuite est de construction, dans les trois familles.** 24 gabarits de vérités, 12 de faux tôt, 12 de pièges, et aucun gabarit présent dans deux strates : chaque gabarit n'a qu'une valeur de vérité. La première révision a apparié la forme grossière (« seuil »), pas le texte : les vérités « seuil » s'écrivent « t >= k implique E(t) >= littéral » ou « E(t) < 1 », les faux « seuil » s'écrivent « E(t) < littéral ».
- **Le classifieur lit le sens de l'inégalité, pas la taille des nombres.** Jeton le plus « faux » : « < » suivi d'une parenthèse (+3,83). Parmi les jetons les plus « vrai » : ceux de « >= » (−3,04 ; −2,75 ; −2,71). Carbon a raison sur ce point.
- **Mais un littéral rationnel n'est pas un seul jeton.** Le code écrit « (a/b) », lu comme cinq jetons ; 0 ou 1 est lu comme un seul. Remplacer un littéral rationnel par 0 ou 1 change donc ce que voit le classifieur. L'affirmation de Carbon et de Neon (« cela ne change rien ») n'est exacte que pour les littéraux entiers.
- **Une seconde fuite échappe au classifieur.** Les nombres étant masqués, il ne voit pas que les pièges portent des littéraux énormes. Une règle d'une ligne, sans apprentissage, sépare les pièges des vérités à 0,956. Un modèle de langue, lui, lit ces chiffres.
- **Ce n'est pas un défaut de la sonde.** Elle ne lit que le texte de l'énoncé, les plis regroupent des mondes entiers, et l'aire reste haute avec tous les textes (0,93) : l'écart des textes déjà vus ne crée pas l'effet.
- **Dans les familles à suites monotones, la vérité est liée à la forme par les mathématiques.** Une borne haute littérale placée sous la limite d'une quantité croissante est fausse tôt ou tard, et par construction elle l'est toujours avant le plafond ; une borne basse après « t >= k » est vraie. Un lecteur sans outil qui le dit fait un raisonnement juste, pas une tricherie. Ces gabarits ne peuvent pas être appariés ; il en faut d'autres. La troisième famille montre que c'est possible : sa forme de résidu (« mod(u(n), p) != r ») porte déjà une vérité, un faux tôt et un piège, et ses deux versions fausses sont parmi les quatre gabarits qui résistent à la règle aveugle. Même là, la taille du module trahit encore (petit pour la vérité, grand premier pour les faux).

## 3. Décision recommandée

### 3.1 Sur la banque actuelle (version 6)

- Le seuil de 0,75 est gardé, valeur et règle inchangées. Il s'est déclenché sur les 41 racines. Sa conséquence écrite s'applique : les verdicts déclarés passent en description ; rien ne s'affirme sur « le bras avec outil discerne mieux ».
- L'option (c) est rejetée.
- Changer d'instrument ne changerait rien ici : le rappel à fausses alarmes plafonnées vaut 0,74 en moyenne, contre les 0,15 à 0,20 que Carbon et Neon proposent comme limite.
- Le blanc « décision sur le seuil » du préenregistrement se remplit ainsi : gardé à 0,75 (GO-2026-11-22-109), complété pour la banque révisée par la batterie du point 3.3 si Lazar l'accepte.

### 3.2 Ordre des étapes

1. **Diagnostic sans appel de modèle.** Première passe faite ici (§ 2). À refaire et à compléter par le vérificateur du code (pièce d'instrument) : table famille × gabarit × strate avec les textes, poids, règle aveugle par gabarit, contrôle des plis. Coût nul, routine : aucun mot de Lazar n'est requis pour cette étape.
2. **Écrire la batterie de fuite (3.3) dans le mandat du concepteur, avant tout travail sur la banque révisée.** Contre-lue. Aucune mesure de la banque révisée avant ce texte.
3. **Banque révisée (version 7) par le concepteur, codée par Opus.** Elle ferme deux fuites, non une : la fuite de forme et la fuite d'instance (faux dont le contre-exemple n'est pas à une instance extrême). Principe : des gabarits appariés, où le même texte, à un littéral près tiré de la même façon, donne une vérité, un faux tôt ou un piège. Les seuils monotones ne s'apparient pas : en réduire la part. Si une seule fuite peut être fermée, fermer d'abord la fuite d'instance : la lecture en preuve est celle que le pilier emploie. **Deux cycles de conception au plus.**
4. **Mesure sur au moins 40 racines d'essai neuves**, tirées après le gel du code de la version 7 ; pas les 41 déjà lues ; aucune racine choisie.
5. **Branche, lue sur les sondes seules, jamais sur ce qu'un bras obtient (R3).** Batterie tenue : les deux lectures sont ouvertes. Une famille résiste : la banque de la comparaison peut être restreinte, avant tout appel, aux gabarits appariés des familles qui tiennent, et la portée de l'affirmation est réduite d'autant. Batterie non tenue après deux cycles : repli écrit d'avance, la lecture en preuve seule, les verdicts en description.
6. **Les deux bras ne courent qu'ensuite** (point 3.6, qui revient à Lazar).

### 3.3 Le critère : 0,75 gardé, et complété

Quatre conditions, calculées sans appel de modèle. Elles se jugent sur le générateur (les racines neuves de l'étape 4), puis se relisent sur la banque réelle au rejeu, avant tout appel.

1. **Invariant de construction**, contrôlé par le code à la plantation, comme le sont déjà les deux règles de forme : chaque gabarit apparié donne les trois strates dans les mêmes proportions, dans chaque monde, avec des littéraux tirés de la même loi.
2. **L'aire qui fait foi du classifieur actuel reste ≤ 0,75.** Même calcul, même valeur. Les deux aires par strate, l'aire sur tous les faux et l'intervalle sont rapportés.
3. **Rappel à fausses alarmes ≤ 0,10 : au plus 0,20, dans chaque strate de faux**, pour trois sondes : le classifieur actuel ; une sonde qui voit les nombres (nombre et taille des littéraux, proximité de 0 et de 1) ; une sonde tenue à l'écart du concepteur, écrite par le vérificateur du code après le gel de la banque. Le seuil de chaque sonde est réglé sur les mondes d'apprentissage.
4. **La règle aveugle du brouillon 4, sans retouche, rend un contre-exemple vérifié sur au plus la moitié des faux.** C'est la garde propre de la lecture en preuve.

Lecture des conditions :

- Sur le générateur, les conditions 2 à 4 se jugent sur la borne haute d'un intervalle à 90 % par rééchantillonnage des racines.
- 1 à 3 tenues : la lecture en verdict est ouverte. Sinon elle reste en description, comme aujourd'hui.
- 4 non tenue : la lecture en preuve est calculée, mais le texte dit d'avance que « gain d'au moins 0,20 en preuve » est hors de portée.
- Sur la banque réelle, une valeur hors de la plage vue sur les racines neuves est un fait d'instrument à expliquer avant la course ; elle ferme la lecture en verdict.
- Intervalle à cheval sur une limite : la branche prudente s'applique. Indéterminé ne vaut pas favorable.

Pourquoi ces nombres :

- 0,10 est la borne de fausses alarmes du protocole.
- 0,20 de rappel laisse à une règle de forme un excès de 0,10, la moitié de la marge de 0,20 ; Carbon et Neon convergent vers cet excès.
- La moitié pour la règle aveugle : affirmer un gain d'au moins 0,20 sur 75 faux demande un écart observé d'environ 0,30 à 0,33 (ordre de grandeur de Carbon, que mon calcul à la main retrouve ; à recalculer par le script de puissance du concepteur) ; il faut donc au moins cette place au-dessus de ce qu'un lecteur sans calcul peut atteindre.

Ce sont mes valeurs par défaut. Le concepteur peut les ajuster, par écrit et avant la première mesure de la banque révisée.

### 3.4 Sort de l'option (a)

- **Elle n'est pas un repli à inventer.** C'est la lecture en preuve du brouillon 4. Elle est calculée dans les deux branches, et elle est la seule affirmable quand la batterie n'est pas tenue. Le « repli préspécifié » de Lazar est donc respecté.
- **Elle est équitable pour ce qu'elle mesure** : même consigne, même schéma de sortie, même vérificateur, même plafond, même nombre d'instances. Ce que Neon et Carbon appellent une iniquité est un changement d'objet : on ne mesure plus « qui repère le faux », mais « qui le réfute par un témoin exact ». Dans ce pilier, c'est l'objet utile : un test de mort doit être certain, et le bras avec outil n'y tue que par contre-exemple vérifié.
- **Son libellé est borné.** Elle affirme « le bras avec outil ajoute des réfutations certifiées ». Jamais « il discerne mieux », jamais « effet du calcul ». Le brouillon 4 l'écrit déjà ; à garder.
- **Trois gardes, déjà écrites, à ne pas perdre** : les fausses alarmes et les réfutations fausses se comptent sur les verdicts bruts ; le dénominateur reste les 75 faux ; un verdict « faux » sans témoin ne compte pas comme réfutation certifiée.
- **Deux ajouts.**
  1. Rapporter à côté le nombre de faux que le bras nu déclare « faux » sans témoin vérifié. Une réfutation juste par raisonnement ne doit pas disparaître du rapport.
  2. Rapporter en description la borne d'Astra : part des faux avec témoin vérifié du bras avec outil, moins rappel déclaré du bras nu. Aucune affirmation n'en est tirée.
- **Sa limite sur la banque actuelle doit être dite.** Face à la règle aveugle, à 80 à 91 %, il ne reste que 7 à 15 énoncés pour établir quoi que ce soit. Face au bras nu, un écart dirait surtout que ce bras n'a pas pensé à citer le plafond. Le repli est juste, mais il ne sauve pas la comparaison.

### 3.5 Le relecteur d'une autre famille

- **Pas de bras payant de plus maintenant.**
- **Libellé** : toute affirmation porte sur « le système avec outil » (agent à outil, plusieurs tours, relecture par une autre famille) contre la lecture nue. Jamais sur « l'outil ».
- **Contraste gratuit, à écrire d'avance** : la sortie de l'agent avant relecture passe de « sensibilité » à un contraste préspécifié, rapporté à côté du contraste principal, avec le même test. Il isole ce que la relecture change, sans appel de plus.
- **Porter la remarque 30 au brouillon 5** : le relecteur n'ajoute aucune instance ; le code retire les instances absentes de la sortie de l'agent et compte ces retraits. La relecture ne peut alors que garder ou réduire les preuves.
- **Règle de suite, écrite d'avance** : si la relecture change le verdict sur plus d'un énoncé sur dix, ou déplace de plus de 0,05 la part des faux avec témoin vérifié, un bras « lecture nue + même relecteur » est mis au dossier du pilote suivant, sur devis. Sans cela, aucune affirmation en verdict n'est attribuable.

### 3.6 Un point qui revient à Lazar : quand courir les deux bras

- **Décision** : attendre ou non la banque révisée pour courir le bras avec outil et le bras nu.
- **Enjeu** : 92,35 USD attendus sur 165,17 et la seule machine louée du pilote. Sur la banque actuelle, l'issue la plus probable face à la règle aveugle est « rien d'établi », selon le concepteur lui-même, et un écart face au bras nu ne se lirait pas (point 3.4). « Go maths » fait courir les deux bras comme écrit ; « go (b) » révise le générateur. Les deux mots ne disent pas lequel prime.
- **Options**
  - (1) Les hypothèses sur les proposeurs et sur le juge de nouveauté courent sur la banque actuelle ; les deux bras attendent la banque révisée ; un petit lot de fumée éprouve la chaîne du bras avec outil sur la banque actuelle. Avantage : on ne paie la mesure qu'une fois, sur une banque qui peut la porter ; la chaîne est éprouvée quand même. Inconvénient : préenregistrement à scinder ; l'expérimentateur est mesuré plus tard.
  - (2) Tout court comme écrit ; la banque révisée sert le pilote 2. Avantage : aucun retard. Inconvénient : on paie deux fois ; « go (b) » n'a alors aucun effet sur ce pilote.
  - (3) Tout le pilote attend la banque révisée. Avantage : un seul texte. Inconvénient : retarde l'hypothèse primaire, que la fuite ne touche pas.
- **Recommandation** : (1), confiance 0,65. C'est l'option (c) que le concepteur gardait en réserve (notes au directeur, nœud 1), avec un lot de fumée en plus.
- **Défaut** : aucun (périmètre et dépense).

## 4. Les arguments, un par un

### Carbon

| argument | sort | pourquoi |
|---|---|---|
| rejeter (c) : déplacer la barre de 0,75 à plus de 0,98 vide le contrôle | retenu | accord des trois ; rien à ajouter |
| les nombres masqués rendent 0, 1 et un grand nombre indiscernables ; remplacer un littéral par 0 ou 1 ne changerait rien | écarté en partie | vrai pour un entier ; faux pour les seuils, écrits « (a/b) », cinq jetons ; sa propre réserve le prévoyait |
| l'aire vient des gabarits et des opérateurs, pas des grandeurs | retenu | vérifié : le jeton décisif est le sens de l'inégalité |
| apparier les gabarits un pour un entre les trois strates | retenu | c'est le principe de la banque révisée |
| loger les bornes dans des constantes nommées du monde, présentes aussi là où l'énoncé est vrai | retenu avec réserve | cela déplace le nombre de l'énoncé vers la définition servie : la sonde, qui ne lit que l'énoncé, n'y verrait plus rien, le modèle si ; il faut alors que les sondes lisent aussi la définition |
| (a) symétrisée en co-analyse et en repli après une itération bornée | retenu | c'est la lecture en preuve, dans les deux branches ; deux cycles |
| ne pas appliquer (a) seule : la forme dit à l'agent de chercher au-delà de N | écarté ici | le plafond 3N est écrit dans la consigne des deux bras |
| ne pas appliquer (a) seule : puissance tendue | retenu, et aggravé | la gêne ne vient pas d'un bras arrêté à N, mais de la règle aveugle, qui atteint déjà 80 à 91 % |
| l'aire ne dit pas le rappel au régime de fausses alarmes du test | retenu pour la banque révisée | condition 3 ; sans effet aujourd'hui (rappel 0,74) |
| angle mort des nombres masqués | retenu | vérifié : la règle du nombre de chiffres atteint 0,956 |
| apprentissage des deux strates mêlées ; séparabilité des pièges et des faux tôt ignorée | retenu en description | 0,71 par le classifieur, 0,92 par les chiffres ; peu de portée, le plafond étant servi |
| viser une aire de 0,50 à 0,60 ; ajouter « aire moyenne ≤ 0,65 » | écarté comme seuil de plus | 0,75 gardé, la condition 3 est plus stricte et plus proche de l'usage ; un seuil de plus est une fourche de plus |
| le maximum des deux strates : bon principe, biais si une seule graine | retenu | maximum gardé, deux aires rapportées, jugement sur 40 racines |
| absence d'intervalle : juger le générateur, pas un tirage | retenu | intervalle par rééchantillonnage, déjà au brouillon 4 |
| trois classifieurs, traits numériques, au moins 40 graines | retenu | trois sondes, dont une tenue à l'écart |
| rappel à fausses alarmes ≤ 0,05 inférieur à 0,15 | retenu, nombres ajustés | 0,10 est la borne du protocole ; l'excès toléré est le même |
| (a) inéquitable : imposer un témoin au bras nu, même vérificateur | sans objet | déjà fait au brouillon 4 |
| fausses alarmes nulles par construction si on ne compte que les témoins | retenu | déjà traité : verdicts bruts |
| asymétrie mathématique : une réfutation par raisonnement vaut zéro | retenu comme limite du libellé | pas un veto ; le compte des « faux » sans témoin du bras nu est rapporté |
| la mesure sur témoins est presque immunisée contre la forme | écarté pour la banque actuelle | la règle aveugle obtient les témoins sans rien évaluer |
| contrôles : poids, aire par famille, table gabarit × strate | retenu | première passe faite (§ 2) |
| bases déterministes de recherche de témoins | retenu | la troisième existe : c'est la règle aveugle |
| calcul de puissance sous (a) | retenu | à refaire sur la banque révisée, avec la part de la règle aveugle |

### Astra

| argument | sort | pourquoi |
|---|---|---|
| (b) avant les appels ; (a) si le générateur reste tel quel ; pas (c) | retenu | c'est l'ordre des étapes |
| ne pas remplacer simplement les grands littéraux par 0 ou 1 : ils deviendraient les nouveaux indices | retenu | apparier, non déplacer l'indice |
| l'aire ne dit ni si les bras exploitent les indices, ni lequel en profite | retenu | raison de garder les verdicts en description, non de les supprimer |
| le rappel brut dit « qui repère le plus de faux sur cette banque », pas l'effet du calcul | retenu | règle de libellé |
| même sur une banque équilibrée, le bras avec outil a une relecture et plus d'appels | retenu | point 3.5 |
| garder 0,75 comme engagement du protocole actuel, pas comme frontière du suivant | retenu | c'est l'ossature de la décision |
| le maximum comme alarme ; publier les deux aires ; la plage n'est pas un intervalle, mais le cas n'est pas limite | retenu | — |
| critère d'usage : rappel par strate à 10 % de fausses alarmes, seuil réglé sur des mondes séparés | retenu | condition 3 |
| fixer avant mesure l'excès toléré ; il ne se déduit pas de la marge de 0,20 | retenu | 0,10, posé comme convention et dit tel |
| indéterminé ne vaut pas favorable | retenu | branche prudente |
| ne jamais restreindre le dénominateur aux énoncés où l'outil a trouvé un témoin | retenu | déjà écrit |
| témoins vérifiés des deux bras : équitable pour la détection certifiée, autre objet que les verdicts | retenu | libellé |
| témoins du bras avec outil contre verdicts bruts du bras nu : borne inférieure utile | retenu en description | aucune affirmation ; sur la banque actuelle elle ne peut pas être franchie si le bras nu lit la forme |
| fausses alarmes sur verdicts bruts ; discordances appariées ; résultats par strate | retenu | — |
| un témoin valide ne prouve pas que la forme n'a pas guidé la recherche | retenu | une raison de plus de réviser la banque |
| table famille × gabarit ; figer la révision avant de la tester sur des graines neuves ; ne pas choisir une graine | retenu | étapes 1, 3 et 4 |
| part des faux à témoin accessible selon le budget de recherche | retenu | réponse du dépôt : plafond 3N servi, règle aveugle à 80 à 91 % |
| si certains gabarits ne peuvent accueillir les trois strates : comparaison limitée, ou conclusion limitée comme en (a) | retenu | c'est le cas des seuils monotones ; d'où le repli |
| si la cible est la performance des deux systèmes sur ce générateur précis, la forme fait partie de la tâche | écarté comme cible | le pilier veut un instrument qui tienne sur des énoncés sans forme plantée |

### Neon

| argument | sort | pourquoi |
|---|---|---|
| diagnostic sans appel de modèle d'abord | retenu | étape 1 ; première passe faite |
| rejeter (c) | retenu | — |
| ne pas appliquer (a) dès maintenant : lancer sur une banque qui fuit gaspille le budget | retenu | base du point 3.6 |
| remplacer un littéral par 0 ou 1 ne change rigoureusement rien pour le classifieur | écarté | inexact pour ce code (rationnel entre parenthèses) ; l'esprit reste : pas de retouche à l'aveugle |
| la première révision n'a presque rien changé | retenu | elle appariait la forme grossière, pas le texte |
| l'aire intègre tous les taux de fausses alarmes ; angle mort numérique | retenu | conditions 3 et sonde qui voit les nombres |
| un classifieur entraîné surestime ce qu'un modèle lit énoncé par énoncé | retenu comme incertitude | mais ici la forme coïncide avec un raisonnement élémentaire, qu'un modèle fait sans entraînement |
| le maximum par strate dépasse 0,75 même sur des gabarits presque équilibrés (exemple à 0,767) | retenu en partie | calcul juste ; il lit le lien entre strate et gabarit, qui est une fuite réelle ; il disparaît si chaque gabarit porte les trois strates |
| 0,75 trop permissif sur l'aire globale, trop sensible sur le maximum | retenu comme raison de compléter | pas comme raison d'abandonner la valeur |
| ne pas garder 0,75 | écarté dans sa lettre | valeur et règle gardées ; jamais seules pour la banque révisée |
| audit à trois niveaux : invariant, deux sondes, métriques au régime du test | retenu | conditions 1 et 3 |
| aire globale ≤ 0,60 | écarté comme seuil de plus | redondant avec la condition 3 |
| vérifier aussi sur les 150 énoncés réels | retenu | relecture sur la banque réelle |
| (a), les deux bras : asymétrie de procédure | sans objet | déjà symétrique |
| (a), les deux bras : elle change la question, taillée pour le bras avec outil | retenu comme limite du libellé, écarté comme iniquité | l'objet « réfutation certifiée » est celui du pilier ; sa propre réserve 5 le concède |
| (a), bras avec outil seul contre verdicts bruts : borne très prudente | retenu en description | comme pour Astra |
| la forme sert d'oracle pour l'effort de recherche | écarté ici | plafond 3N servi aux deux bras |
| exclure la restriction au sous-ensemble où l'outil a trouvé | retenu | déjà écrit |
| cinq contrôles (décomposition, tables, sonde numérique, plis, profil des contre-exemples) | retenu | faits en première passe, sauf le contrôle des plis et de l'échelle, à faire par le vérificateur |
| si les indices ne se transfèrent pas à un modèle, la refonte est disproportionnée | écarté | voir plus haut ; et la fuite d'instance suffit à justifier la refonte |
| si l'appariement rend les vérités triviales, (b) crée un biais neuf | retenu | risque principal (§ 5) ; d'où deux cycles au plus et le repli |
| le relecteur confond l'effet de l'outil ; ajouter un bras ou retirer le relecteur | retenu, traitement différent | contraste gratuit « avant relecture », libellé « système », bras payant seulement si la règle de suite le demande |
| si le protocole est gelé, appliquer (a) strictement | sans objet | brouillon non scellé, aucun appel |
| si l'aire vient d'un défaut de la sonde, (b) est inutile | écarté | code lu ; mesure refaite et retrouvée |

## 5. Ce qui pourrait rendre cette décision fausse

1. **L'appariement échoue dans une famille.** Là où la vérité tient au sens de l'inégalité, il faut des mathématiques neuves, pas un réglage. Si les vérités appariées deviennent triviales, la révision déplace le biais. La borne de deux cycles limite la perte ; elle ne la supprime pas.
2. **La batterie est trop stricte ou trop lâche.** Trop stricte : la lecture en verdict ne s'ouvre jamais et l'effort n'achète que le repli. Trop lâche : un modèle de langue lit des indices qu'aucune sonde simple ne voit. Une batterie tenue veut dire « aucune fuite trouvée par ces sondes », jamais « aucune fuite ».
3. **Mes nombres sont des conventions.** 0,20, la moitié, deux cycles, 40 racines, et la règle de suite du relecteur (un énoncé sur dix, 0,05) sont des jugements, non des résultats. L'ordre de grandeur de 0,30 à 0,33 est une estimation.
4. **Mon diagnostic n'est pas vérifié.** Il retrouve la plage de l'équipe, mais un défaut dans mes mesures ajoutées (rappel, règle des chiffres) changerait la force du § 2, non le fait de construction, qui se lit dans la note du code.
5. **Le bras nu n'exploite peut-être ni la forme ni les instances extrêmes.** La banque actuelle aurait alors séparé les deux bras. On ne peut pas le savoir sans payer. Je renonce à cette information parce qu'un écart ainsi obtenu ne se lirait pas : il dirait que le bras nu n'a pas pensé à citer le plafond.
6. **Lazar peut vouloir éprouver la chaîne en vraie grandeur dès maintenant.** Alors l'option (2) du point 3.6 se défend, et ma recommandation est fausse pour ses priorités, non pour la mesure.
7. **Le relecteur change peut-être beaucoup de verdicts.** Le contraste gratuit n'isole alors rien pour la lecture en verdict, et le bras payant devient nécessaire.
8. **Le brouillon 5 a pu changer le texte.** Je ne l'ai pas lu. Tout point de ce jugement est à confronter à lui.
9. **La sonde tenue à l'écart alourdit la procédure.** Si la capacité manque, c'est la première chose à retirer, avec une ligne d'écart.

## 6. Confiance

| point | confiance |
|---|---|
| rejeter (c) | plus de 0,95 |
| garder 0,75 tel quel pour la banque actuelle, avec sa conséquence | 0,90 |
| 0,75 nécessaire mais non suffisant pour la banque révisée | 0,85 |
| garder la lecture en preuve dans les deux branches, libellé borné | 0,85 |
| réviser la banque avant de payer les deux bras | 0,75 |
| le relecteur traité par contraste gratuit et libellé, sans bras payant | 0,75 |
| la banque révisée tient la batterie dans les trois familles en deux cycles | 0,45 |
| séquence du point 3.6, option (1) | 0,65 |
| ensemble | 0,75 |

## 7. Réserves sur mon propre travail

- Le script du diagnostic est de moi, alors que le code revient à Opus ; je l'ai écrit parce que les trois avis divergeaient sur ce que lit le classifieur et que la synthèse demandait cette vérification. Il importe le paquet figé sans le modifier.
- Routine de reprise partielle : empreintes des documents de lancement vérifiées (trois sur trois) ; registre des rappels lu, aucun rappel échu le 22 novembre ; `verifier-arbre` rend 91 écarts préexistants sur cette branche, hors de ce dossier, non traités. Ni inventaire des machines, ni défauts échus, ni essais, ni passation : ils reviennent à la mère.
- Ce jugement propose ; il ne modifie ni le préenregistrement ni le programme. Le critère du point 3.3 et la séquence du point 3.6 reviennent à Lazar.
