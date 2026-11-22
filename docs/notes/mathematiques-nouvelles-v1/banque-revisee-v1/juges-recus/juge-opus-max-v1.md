# Juge Opus 5.5 (effort maximal) — seuil de 0,75 du classifieur de style, mathématiques nouvelles — v1

- Nature : avis de juge, étage 4 de la chaîne de décision (GO-2026-11-22-106 et GO-2026-11-22-112). C'est une recommandation : la décision revient à Lazar (critère d'une pièce de classe A, périmètre et calendrier d'un pilote : nœud).
- Juge : Claude Opus 5.5, effort maximal, session `session_013QMaykUGEC1bvN9Bt8ijJU`. Le second juge (Fable 5.2) n'a pas été consulté ; sa réponse n'a pas été lue.
- Rédigé le 2026-11-22 vers 18:25Z (`date -u`). Processeur seul : aucun appel payant, aucune dépense.
- Cloisonnement : aucune clé plantée lue, ni réelle ni d'essai (ni `cle-*.json`, ni `sous-banque-cle-*`, ni les données par item de la sonde). Lus : code, notes, sorties agrégées.
- Routine de reprise : étape 1 faite (empreintes de lancement conformes ; vérification de l'arbre : 91 problèmes préexistants, aucun dans ce dossier). Étapes 3 à 5 (défauts échus, machines, essais) laissées à la mère : hors du mandat d'un juge.
- Pièces lues et empreintes : § 7. Toutes les empreintes relues sont conformes à leurs compagnons.

## 0. Verdict

1. **Option (b), en trois temps** : un diagnostic gratuit sur les 41 racines d'essai déjà vues ; un critère neuf gelé avant toute mesure de la version 7 de la banque ; une version 7, conçue par le concepteur, qui vise **deux fuites** et non une : la fuite de forme (le style) et la fuite d'instance (des contre-exemples à des instances qu'on devine sans calcul).
2. **0,75 ne reste pas le critère qui décide** pour une banque neuve. À la place : deux sondes (le style, les nombres), leur rappel à 10 % de fausses alarmes au plus, un excès au-dessus du hasard ≤ 0,10 en borne haute, mesuré sur au moins 40 racines neuves, et une épreuve du critère sur un cas sain et sur des artefacts (R5). L'aire reste rapportée. Pour la version 6, rien ne change : verdicts en description dans les deux cas.
3. **L'option (a) symétrisée n'est pas un repli** : c'est la lecture en preuve déjà écrite au brouillon 4 (E1 à E5). Elle porte les affirmations de H3 dans toutes les branches. Seul l'ajout de la lecture en verdict (V1 à V4) dépend du critère.
4. **Relecteur** : il ne choisit que parmi les instances de l'agent ; « S avant relecture » est rapporté au même rang que S ; toute phrase « l'outil apporte » exige la même direction sans relecture ; aucun bras neuf.
5. **Calendrier** : la version 7 peut retarder le scellement jusqu'au 4 décembre 2026, 23:59 UTC, pas au-delà ; sinon la course part sur la version 6, branche de repli écrite d'avance. Confiance d'ensemble : 0,7.

## 1. Trois faits que les trois avis ne pouvaient pas connaître

La question servie (v2, `51344c2d…`) décrit un état antérieur au brouillon 4 du préenregistrement. Trois faits du chantier changent la lecture des avis.

1. **La symétrisation de (a) est déjà écrite.** Au brouillon 4 (`212c6eca…`), la lecture nue (N) reçoit le même schéma de sortie que le bras outillé (S), ses instances passent par la même vérification exacte (T6), chaque sortie est lue sur trois instances au plus, et le dénominateur reste les 75 faux. La lecture en preuve (E1 à E5) vaut dans les deux branches d'aire ; la lecture en verdict (V1 à V4) n'est affirmable que sous le seuil. La question ne mentionnait la vérification exacte que pour le bras outillé, et disait du bras nu qu'il « peut citer une valeur, mais n'exécute aucun calcul », sans dire que ses valeurs citées passent par la même vérification.
2. **Une règle aveugle rend déjà presque tous les contre-exemples.** La règle aveugle A n'évalue pas l'énoncé : elle avance trois instances (variables naturelles à 3N, puis à 1, puis à N + 1). Sur 41 racines d'essai, elle rend un contre-exemple vérifié sur 60 à 68 des 75 faux, soit 80 % à 91 % (médiane 84 %). L'instance 3N seule en fait 0,837. 20 gabarits de faux sur 24 tombent à chaque racine ; 4 résistent ; il reste 7 à 15 faux hors de sa portée (sonde `e6ae3d49…`, vérifiée par un Opus neuf, `bd3b37e9…`). Trois mécanismes s'y mêlent :
   - des seuils monotones dépassés au plafond (les pièges sont plantés dans ]N .. 3N], ils croissent, et le plafond B = 3N est donné en nombre aux deux bras) ;
   - des énoncés faux presque partout ;
   - des énoncés clos ou à variables bornées (16,7 % des faux tôt), où le contre-exemple vérifié se réduit au verdict.

   Avec le plafond servi, la lecture nue peut imiter la règle (remarque 38 du contre-lecteur, `69b8aa58…`). Le concepteur l'a écrit (notes du brouillon 4, `06a92833…`, nœud 5) : la version 7 doit fermer deux fuites, sinon la règle aveugle restera vers 80 %.
3. **Ce que le classifieur voit.** Le découpeur lit « 4481/4608 » en trois jetons, « NUM / NUM » (`grammaire.py`, ligne 63, `4c0a8ffe…` ; `forme_seule.py`, ligne 93, `74c12fed…`). La sonde ne voit pas les grandeurs, mais elle voit si un littéral est une fraction. Les deux aires par strate sont hautes à chaque racine : la plus petite des deux va de 0,929 à 0,976 (`v6-aires.json`, `32cd1781…`, recompte de ce juge sur le fichier scellé). C'est une vraie prévisibilité du faux par la forme, et non l'artefact du maximum des strates. Elle vient selon toute vraisemblance de l'identité des gabarits (inférence de lecture du code, à mesurer à l'étape 1, d) : chaque gabarit est planté dans une seule strate, et ses noms de fonctions et ses opérateurs le trahissent.

Deux faits de cadre complètent : H3 est une hypothèse **secondaire** d'un pilote dont la primaire (H1, proposeurs et tests de mort) ne dépend d'aucune de ces fuites ; chaque item est jugé **seul, dans un contexte neuf** (A8).

## 2. Décision recommandée

### 2.1 En une phrase

Faire (b) maintenant, en commençant par un diagnostic gratuit, contre la fuite de forme et la fuite d'instance, sous un critère neuf gelé avant toute mesure de la version 7, avec la lecture en preuve gardée dans toutes les branches et une date butoir après laquelle la course part sur la version 6.

### 2.2 Ordre des étapes

1. **Diagnostic** (0 USD, processeur, exécutant Opus de la session des mathématiques, un jour au plus). Sur les 41 racines d'essai déjà exposées (0 à 39 et 20261122), jamais sur des racines neuves :
   - a. table gabarit × strate × famille, dans la banque et dans la sous-banque ;
   - b. jetons du classifieur de style aux plus forts rapports de vraisemblance, par famille ;
   - c. aire et rappel à 10 % de fausses alarmes : globaux, par strate contre tous les vrais, par strate contre les vrais des mêmes gabarits, par famille ;
   - d. classifieur sur le seul identifiant de gabarit et de famille, contre le classifieur de style à l'intérieur de chaque gabarit : cela sépare le déséquilibre de composition de la fuite interne ;
   - e. sonde numérique prototype (§ 2.3) ;
   - f. contrôle de chaîne : le texte que lit la sonde est, octet pour octet, l'énoncé servi aux bras ; aucune métadonnée ; plis sans fuite ;
   - g. profil des témoins : pour chaque faux, l'ensemble de ses instances fausses dans [0 .. 3N] ; part réfutée par la règle A telle qu'écrite, par l'instance 3N seule, et par au moins une instance saillante (§ 2.4) ;
   - h. puissance de la lecture en preuve (E1, E4), par simulation, pour v_N = 0,2, 0,5 et 0,85 et pour la part des faux hors de portée de A.

   Sortie : une note de travail scellée. Elle nourrit le dessin de la version 7 ; elle ne décide rien.
2. **Critère et cibles gelés avant toute mesure de la version 7.** Le concepteur (Fable 5.2) les écrit ; un Opus 5.5 les contre-lit, puis vérifie les corrections. On y met : le critère de forme (§ 2.3), la cible d'instance (§ 2.4), le protocole des racines neuves (étape 4) et les branches (étape 5). Ils vont au brouillon 5 s'il n'est pas encore rendu, sinon au brouillon 6, écrit en différences. Le blanc DÉCISION-SEUIL porte l'identifiant du mot de Lazar. Cela entre dans les pièces réservées à Fable (critères de décision, conception d'oracles).
3. **Version 7.** Le concepteur la dessine, un Opus la code, la contre-lecture est de classe B.
   - **Fuite de forme** : des paires minimales. À chaque faux servi à S et N répond un vrai du même gabarit, de même squelette de jetons (nombres à part), de la même famille et si possible du même monde. Sa vérité ne tient qu'aux valeurs. Les grandeurs des littéraux suivent la même loi chez les vrais et chez les faux, sinon la sonde numérique lit la vérité. La paire est l'unité du tirage de la sous-banque.
   - **Fuite d'instance** : les témoins des faux sont hors des instances saillantes. Pistes : énoncés non monotones, fenêtres, deux variables, résidus (les résidus résistent déjà à A).
   - **Périmètre** : la version 7 ne change que ce que lit H3, c'est-à-dire les énoncés servis à S et N. Les mondes, les vérités que retrouvent les proposeurs, H1, H2, H4 et leurs seuils restent ceux de la version 6, sauf nécessité que le concepteur motive par écrit.
   - **Gabarits non appariables** : dits et comptés, jamais retirés en silence.
4. **Une seule mesure de la version 7 figée**, sur au moins 40 racines d'essai neuves. Elles sont tirées au moment du gel par `secrets.randbits(128)`, leurs empreintes sont commises avant la mesure, et personne ne les a vues. Le résultat est rapporté en entier, échec compris. Aucune retouche sur ces racines : une version 8 se mesure sur un autre lot neuf, et toutes les tentatives sont rapportées.
5. **Branches écrites d'avance.**
   - a. Version 7 certifiée (rejeu sans appel conforme, vérification du code sans remarque bloquante) **et** critère de forme tenu : H3 sur la version 7 ; lecture en preuve et lecture en verdict affirmables.
   - b. Version 7 certifiée, critère de forme non tenu, cible d'instance tenue : H3 sur la version 7 ; lecture en preuve seule ; verdicts en description.
   - c. Sinon, ou si la version 7 n'est pas figée et mesurée au **4 décembre 2026, 23:59 UTC** : H3 sur la version 6, telle qu'au brouillon en cours ; lecture en preuve seule ; verdicts en description ; la version 7 passe au pilote 2. Aucun mot de plus n'est requis pour cette bascule.

   La version 7 peut retarder le scellement jusqu'à cette date, pas au-delà. La règle du prix unique d'Argon (aucun appel entre le 30 novembre et le 2 décembre) n'en est pas gênée. L'échéance du 13 décembre tient.
6. **Rejeu de la banque réelle**, toutes branches, avant tout appel : sondes, aires et règles aveugles rapportées. En branche a, si l'excès de la banque réelle dépasse le 95e centile des racines neuves, la lecture en verdict repasse en description, et c'est dit en tête du rapport.

### 2.3 Le critère qui remplace 0,75 (lecture en verdict)

- **Ce qu'on mesure.** Pour chaque racine, sur les items que S et N recevraient (sous-banque analysée), deux sondes en validation croisée par mondes entiers (plis par l'enfant (10, 0), comme aujourd'hui) :
  - le classifieur de style actuel, inchangé ;
  - une sonde numérique, écrite à l'étape 2 et gelée avant toute mesure de la version 7. Elle ne lit que les littéraux : au moins l'ordre de grandeur du numérateur et du dénominateur, entier ou fraction, valeur 0, 1 ou 2, nombre de littéraux, position par rapport aux constantes servies du monde. Calcul exact ou graine consignée ; aucun calcul de la vérité.
- **Le nombre.** Pour chaque sonde et chacun de trois ensembles (faux tôt, pièges, tous les faux) : le rappel au seuil de score qui garde au plus 10 % de fausses alarmes sur les vrais non vus. Un bloc d'ex æquo n'est franchi que s'il tient entier sous 10 %, jamais par tirage. L'**excès** est ce rappel moins 0,10.
- **La règle.** Chaque excès est moyenné sur les racines neuves, avec un intervalle à 90 % par rééchantillonnage des racines (2 000 tirages, enfant neuf, par exemple (10, 3)). Le critère **tient** si la borne haute du plus grand des six excès est ≤ 0,10. Une borne non calculable vaut « non tenu ». 0,10 est une convention déclarée (la moitié de la marge δ = 0,20 entre bras), non une dérivation.
- **Épreuve du critère (R5), avant emploi.** Il doit tenir sur une banque construite saine (paires exactes, grandeurs de même loi). Il doit tomber sur une banque artefact dont la vérité tient à la seule grandeur du littéral, et sur une banque artefact dont la vérité tient au gabarit.
- **Toujours rapporté, sans effet sur la décision** : les aires (globale ; par strate contre tous les vrais ; par strate contre les vrais du même gabarit), avec leur intervalle, et la mention « au-dessus de 0,75 » si c'est le cas.
- **Pourquoi pas 0,75.**
  - Le classifieur actuel ne voit pas les grandeurs, que les modèles lisent. Une version 7 peut passer sous 0,75 et fuir par les nombres.
  - Une aire résume toute la courbe, alors que l'expérience vit à 10 % de fausses alarmes au plus. Sous un modèle binormal, une aire de 0,75 laisse environ 37 % de rappel à 10 % de fausses alarmes (calcul de Neon, refait).
  - La plus grande des aires par strate, contre tous les vrais, peut dépasser 0,75 sans aucune fuite du faux quand chaque strate occupe ses propres gabarits : 0,767 dans l'exemple de Neon, calcul refait.
  - Sur une racine (une trentaine de vrais), l'erreur-type d'une aire est d'environ 0,08 à 0,09 : une décision sur un point ne tient pas près du seuil.

  Le seuil manque donc l'épreuve sur un artefact (une fuite par les nombres passe), et il peut manquer celle sur un cas sain.
- **Pourquoi ce n'est pas un but déplacé.**
  - Le critère est gelé avant la première mesure de la banque à laquelle il s'applique.
  - Aucun critère proposé (celui de Carbon, d'Astra, de Neon, ni celui-ci) ne ferait passer la version 6 : c'est attendu, et l'étape 1 le mesurera.
  - La branche de la version 6 ne change pas.

### 2.4 La cible d'instance (lecture en preuve)

- Ce n'est **pas** un critère qui bloque. La lecture en preuve reste affirmable dans toutes les branches : sa base, la règle aveugle A, en protège la validité.
- **Cible de dessin de la version 7**, mesurée à l'étape 4. Sur les racines neuves, la médiane de la part des faux réfutés par au moins une instance saillante doit être ≤ 0,50. Une instance saillante donne à toutes les variables naturelles la même valeur, prise parmi 0, 1, 2, N, N + 1, 2N, 3N, ou un entier du texte ± 1 pris dans [0 .. 3N] ; les variables bornées prennent leur plus petite valeur. Raison : la comparaison à la règle aveugle doit pouvoir reposer sur la moitié des faux au moins, et non sur 7 à 15 items de quatre gabarits.
- La règle A reste telle qu'écrite (écrite avant sa première mesure) et reste la base de E4. La règle des instances saillantes est un plancher plus fort, rapporté en description.
- Les énoncés clos ou à variables bornées sont rapportés à part dans v_S, v_N et v_A : chez eux, la preuve se réduit au verdict, et la fuite de forme passe dans la lecture en preuve.
- Les prédictions P5, P11 et P12 sont récrites pour la banque retenue avant le scellement.

### 2.5 Le sort de (a)

- (a) symétrisée est la lecture en preuve du brouillon 4 (E1 à E5). Elle **reste dans toutes les branches** et porte les affirmations de H3. Le pilier ne tue que par contre-exemple vérifié : c'est sa question.
- Déjà en place, à garder :
  - même schéma de sortie et même vérification exacte pour S et N ;
  - trois instances lues au plus par sortie ;
  - dénominateur fixe de 75 faux, jamais restreint aux items où l'outil a trouvé ;
  - règle aveugle A en base ;
  - aucun seuil absolu sur v_S.
- **Ajouts** :
  - (i) les fausses alarmes sur les verdicts bruts des 75 vrais (φ_S, φ_N) sont rapportées au même rang que chaque affirmation E1 à E4, jamais en annexe ;
  - (ii) on écrit « réfutation certifiée », jamais « détection » ;
  - (iii) la différence entre les contre-exemples vérifiés de S et les verdicts bruts de N (v_S − r_N) est rapportée en description, comme borne basse de r_S − r_N (idée d'Astra), sans test neuf ;
  - (iv) les énoncés clos sont rapportés à part (§ 2.4).

### 2.6 Le relecteur

- Kimi reste le relecteur de S (aucun changement de modèle sans GO).
- Correction de la remarque 30, déjà demandée au mandat du brouillon 5 (`b59ffc1e…`) : le relecteur choisit et ordonne au plus trois instances parmi celles de l'agent. Il n'en ajoute aucune et peut changer le verdict. Le code retire avant la vérification toute instance absente de la sortie de l'agent, et compte ces retraits.
- La consigne de l'agent lui demande au plus trois instances, les meilleures d'abord : « S avant relecture » se lit alors comme S et N.
- « S avant relecture » passe de la sensibilité au **même rang** que S pour E1 et E4. Ce n'est ni un test ni un seuil de plus.
- Règle d'écriture : une affirmation nomme « le système S (agent outillé, boucle, relecture d'une autre famille) ». La phrase « l'outil apporte » ne s'écrit que si S avant relecture montre la même direction au même test.
- **Pas de bras neuf.** En lecture en preuve, le relecteur ne peut ajouter aucun témoin. Il ne peut que retirer, ou choisir parmi ceux de l'agent. La confusion est donc bornée et joue contre S, sauf quand l'agent avance plus de trois instances et que le relecteur y choisit : la consigne le rend rare, et le code compte ces sorties. « S avant relecture » mesure l'agent sans lui. Un bras « lecture nue + même relecteur » n'éclairerait que la lecture en verdict. Il coûterait au plus environ 0,07 USD par item (Kimi au pire, `bd3b37e9…` § 3), soit 15 USD au plus sur 208 items. À considérer au brouillon suivant seulement si la branche a est atteinte ; sinon au pilote 2.

### 2.7 Ce qui ne change pas

- H1, H2 et H4, et leurs seuils.
- Pour H3 : δ = 0,20, les valeurs critiques, E1 à E5, V1 à V4.
- Le périmètre décidé par Lazar (GO-2026-11-22-77 : S et N courus comme écrit) ; le plafond de 300 USD d'appels et 65 USD de machine ; l'échéance du 13 décembre.
- Aucun appel payant avant le GO sur le devis. Le diagnostic et la mesure de la version 7 se font sur processeur, à 0 USD.

### 2.8 Écart à la décision conditionnelle de Lazar (GO-2026-11-22-109)

- **D'accord** : (b) avant tout appel ; (a) symétrisée écrite d'avance.
- **En écart**, ce qui fait un nœud pour Lazar :
  1. 0,75 n'est pas gardé comme critère d'une banque neuve. Il est gardé dans son effet pour la version 6 (même branche), et rapporté partout.
  2. (a) n'est pas un repli : elle est permanente.
  3. (b) vise deux fuites, non une.
  4. Le diagnostic vient d'abord, et une date butoir s'ajoute.
- Neon contredisait sur 1, sur le rang de (a), sur l'ordre (diagnostic d'abord) et sur le relecteur. Ce juge rejoint Neon sur 1 et sur l'ordre, en ajoutant l'épreuve du critère (R5) et la décision au niveau du générateur (§ 2.3). Il garde (a) au premier rang, et traite le relecteur sans bras neuf.

## 3. Les arguments des trois avis : retenus ou écartés

### Carbon (`aa66edef…`)

| argument | sort | pourquoi |
|---|---|---|
| (c) rejetée : relever le seuil au-delà de 0,98 vide le contrôle | retenu | accord des trois ; aucune valeur ne se justifie après lecture |
| (b) élargie : apparier exactement les gabarits, bornes en constantes nommées | retenu, complété | paires minimales dont la vérité tient aux valeurs ; ajout de la fuite d'instance |
| « NUM rend 0, 1 et 9485731 indiscernables, donc (b) naïve ne bouge pas l'aire » | retenu en partie | vrai pour les entiers (famille F3) ; faux pour les fractions : « a/b » donne trois jetons (familles F1, F2). Le fond tient : l'aire lit surtout l'identité des gabarits (à mesurer, étape 1, d) |
| la forme guide l'agent : il sait quand chercher au-delà de N | reformulé | avec B = 3N servi (45 valeurs au plus), S peut tout énumérer ; le vrai canal est la fuite d'instance, que mesure A |
| puissance sous (a) : plafond vers 0,294 si l'outil s'arrête à N | écarté dans ses chiffres, retenu pour E4 | le plafond 3N est servi ; le manque de puissance de E4, sur 7 à 15 items, est réel (étape 1, h) |
| l'aire ne dit pas le rappel au régime de l'expérience (2 ou 3 fausses alarmes sur 75) | retenu | c'est la raison principale du critère neuf |
| le maximum des strates est le bon principe, mais biaisé | retenu en partie | la strate compte, à mesurer au point de fonctionnement et contre les vrais du même gabarit |
| rappel à 5 % < 0,15 et aire moyenne ≤ 0,65 ; trois classifieurs ; traits numériques ; 40 graines ou plus | retenu dans l'esprit | 10 % comme la borne des fausses alarmes de l'expérience ; l'aire passe en description |
| (a) inéquitable : imposer un témoin au bras nu, même vérificateur | sans objet | déjà fait au brouillon 4 |
| fausses alarmes nulles par construction sous (a) | retenu | φ sur verdicts bruts au même rang (§ 2.5) |
| asymétrie mathématique : décision contre construction de témoin | retenu comme autre question | c'est la question du pilier, pas une iniquité |
| « (a) pratiquement immunisée contre l'effet de forme » | écarté | la règle aveugle obtient 80 % à 91 % sans calcul ; énoncés clos : preuve = verdict |
| contrôles : poids, aire par famille, bases de recherche de témoins (valeurs triviales du texte), puissance | retenu | étape 1, points b, c, g, h ; les valeurs triviales annonçaient la fuite d'instance |
| on mesure le couple « Python + relecture », non Python seul | retenu | § 2.6 |
| si les énoncés sont servis groupés, la nuance sur la sonde supervisée tombe | sans objet | un item par contexte (A8) : la nuance tient, la sonde surestime ce qu'un appel isolé exploite |

### Astra (`c76d48a6…`)

| argument | sort | pourquoi |
|---|---|---|
| (b) avant les appels ; (a) si la banque reste ; (c) rejetée | retenu | ordre précisé : diagnostic, critère gelé, version 7, repli |
| l'aire ne dit ni si les bras exploitent ces indices, ni lequel en profite ; l'appariement expose les deux bras sans garantir le même usage | retenu | raison de faire porter H3 par la lecture en preuve, et de traiter le critère comme une protection prudente |
| le rappel brut répond à « quel système repère le plus de faux sur cette banque », pas à « grâce au calcul » | retenu | verdicts rapportés en description dans toutes les branches |
| garder 0,75 comme engagement du protocole actuel | écarté pour une banque neuve, retenu dans l'effet pour la version 6 | la crainte du but déplacé est traitée par le gel du critère avant la mesure de la version 7 |
| publier les deux aires ; le maximum est optimiste | retenu | § 2.3 |
| rappel par strate au seuil calibré sur mondes séparés, tolérance fixée d'avance, non déduite de δ ; unités de génération rééchantillonnées ; « indéterminé » n'est pas favorable | retenu | tolérance 0,10 dite convention ; borne non calculable vaut « non tenu » |
| ne jamais restreindre le dénominateur ; même consigne et même vérificateur ; v_outil − r_nu comme borne basse | retenu | déjà en place ; borne basse ajoutée en description |
| fausses alarmes sur verdicts bruts | retenu | § 2.5 |
| « un témoin valide ne dit pas que la forme n'a pas guidé la recherche » | retenu | c'est la fuite d'instance |
| table famille × gabarit d'abord ; figer avant des graines neuves ; ne pas choisir une graine qui passe | retenu | étapes 1, 2 et 4 |
| si N est une limite dure, v_outil ≤ 38/75 | sans objet | le plafond servi est 3N |
| métadonnée vue par la sonde : refaire l'audit | retenu | étape 1, f |
| gabarits non appariables : comparaison limitée et annoncée | retenu | dits et comptés, jamais retirés en silence |
| relecture et appels en plus : écart non attribuable au calcul | retenu | § 2.6 |

### Neon (`e0d77af8…`)

| argument | sort | pourquoi |
|---|---|---|
| diagnostic d'abord, puis refonte par appariement des gabarits et des lois numériques, puis instrument remplacé | retenu | étapes 1 à 3 |
| (a) symétrisée en critère secondaire et en repli | écarté sur le rang | la lecture en preuve porte H3 partout : seul un contre-exemple vérifié tue |
| 0,75 non gardé | retenu | § 2.3 |
| « remplacer par 0 ou 1 ne change rien » | retenu en partie | même réserve que pour Carbon (fractions) |
| la première révision n'a presque rien changé | retenu | 0,96 à 0,97 avant, 0,939 à 0,982 après |
| angle mort numérique ; sonde supervisée contre lecture sans exemples | retenus | sonde numérique ; critère tenu pour prudent (§ 4) |
| maximum des strates : 0,767 sans fuite du faux | retenu | calcul refait ; défaut de l'instrument pour une banque équilibrée ; n'explique pas la version 6 (deux strates hautes) |
| 0,75 paradoxal : trop permissif en aire globale, trop sensible en maximum | retenu | le chiffre binormal est une illustration de modèle, non une mesure |
| erreur-type d'environ 0,08 par racine | retenu | décision au niveau du générateur, 40 racines ou plus |
| invariant de proportions par gabarit ; deux sondes ; aire ≤ 0,60 et rappel à 10 % ≤ 0,20 en borne haute | retenu en partie | invariant (paires), deux sondes et rappel retenus ; l'aire ≤ 0,60 passe en description (une seule règle, au point de fonctionnement) |
| (a) change la question | retenu, sans « inéquitable » | c'est la question du pilier |
| fausses alarmes nulles par construction | retenu | § 2.5 |
| la forme comme oracle d'allocation de l'effort | reformulé | S énumère jusqu'à 3N ; le canal réel est la fuite d'instance (§ 2.4) |
| lecture 2 de (a), vérification pour l'outil seul | sans objet | le brouillon 4 vérifie les deux bras |
| restreindre aux items où l'outil a trouvé est invalide | retenu | déjà exclu |
| cinq contrôles sans appel | retenu | étape 1 |
| indices non transférables à un modèle qui lit un énoncé seul | retenu comme risque | § 4 ; la version 7 sert aussi la lecture en preuve |
| des paires qui rendent les vrais triviaux créent un biais neuf | retenu | grandeurs de même loi, sonde numérique, épreuve R5 |
| le relecteur d'une autre famille confond l'effet de l'outil | retenu | traité sans bras neuf (§ 2.6) |
| protocole gelé : (a) stricte | sans objet | rien n'est scellé |
| si la question est la réfutation certifiée, la critique de (a) tombe | retenu | c'est le cas du pilier |
| un bogue de sonde rendrait (b) inutile | retenu en partie | étape 1, f ; la fuite d'instance demeure de toute façon |

## 4. Ce qui pourrait rendre cette décision fausse

1. **La fuite d'instance ne se ferme pas** dans les trois familles. Leurs grandeurs de base croissent avec l'indice, résidus mis à part ; des énoncés non monotones peuvent exiger des fonctions neuves, donc des mondes neufs. La version 7 coûterait alors du temps de Fable pour un gain limité à la forme. La date butoir et la branche c bornent ce coût.
2. **Les indices de la sonde ne servent pas** à un modèle qui lit un énoncé seul, sans exemples étiquetés. Le critère serait trop prudent, et la lecture en verdict perdue pour rien. Le coût est faible (lecture secondaire). Le diagnostic interne déjà prévu le montrera après coup : fausses alarmes de N sur les vrais « seuil » contre les autres.
3. **Mauvaise lecture du mot de Lazar.** Si « (b) » voulait dire « version 7 pour le pilote 2 seulement », ce plan est plus lourd que voulu. Il se réduit alors à : la version 6 et la lecture en preuve pour ce pilote, le critère neuf écrit pour la version 7, le diagnostic tout de suite.
4. **Si Lazar veut d'abord la détection** (le verdict) et non la réfutation certifiée, l'accent mis sur la lecture en preuve est mal placé. La règle du pilier (seul un contre-exemple vérifié tue) rend ce cas peu probable.
5. **La tolérance de 0,10** est une convention. Trop stricte, la lecture en verdict ne s'ouvre jamais ; trop lâche, elle s'ouvre sur une banque contaminée. Les excès mesurés sont rapportés, chacun peut juger.
6. **Le temps de Fable.** Si les pièces de l'entretien du 1er décembre le prennent, la version 7 glisse et la branche c s'applique. C'est voulu, mais H3 restera faible dans ce pilote.
7. **Ce que je n'ai pas refait.** Je n'ai rejoué ni la sonde ni le classifieur. Je m'appuie sur les sorties scellées et sur une vérification indépendante (`bd3b37e9…`). J'ai vérifié le découpeur dans le code, recompté les aires par strate sur le fichier scellé, et refait les calculs de Neon (0,767 ; sous modèle binormal, 37 % de rappel à 10 % de fausses alarmes pour une aire de 0,75, 18 % pour 0,60).

## 5. Confiance

| volet | confiance |
|---|---|
| ne pas garder « plus grande aire par strate ≤ 0,75 » comme règle d'une banque neuve ; critère gelé avant la mesure, deux sondes, point de fonctionnement | 0,75 |
| lecture en preuve permanente, verdicts conditionnels | 0,8 |
| diagnostic d'abord, version 7 contre deux fuites, date butoir et repli | 0,7 |
| valeurs choisies (10 %, 0,10, 40 racines, 0,50, 4 décembre) | 0,55 |
| relecteur traité sans bras neuf | 0,7 |
| **ensemble** | **0,7** |

## 6. Demande approfondie (méthode de Lazar, en bref)

1. **Ce qu'un expert ferait sans qu'on le demande.**
   - Traiter la banque comme un instrument à deux canaux de raccourci : la forme de l'énoncé, et l'instance qu'on devine.
   - Construire des paires minimales.
   - Poser des bases de raccourci (sonde de forme, règles aveugles) pour chaque canal.
   - Décider au niveau du générateur, sur beaucoup de racines, et non sur un seul tirage.
   - Éprouver la règle de décision sur un cas sain et sur des artefacts.
   - Séparer la banque de l'hypothèse secondaire de celle de la primaire.
2. **Données brutes au départ** : la table par item des racines d'essai (gabarit, strate, famille, texte servi, score et contributions des jetons, ensemble des instances fausses dans [0 .. 3N]), plutôt que l'aire résumée.
3. **Méthodes et outils** :
   - le classifieur exact du code v6 ;
   - une sonde numérique déterministe ;
   - le rappel à taux de fausses alarmes fixé ;
   - le rééchantillonnage des racines ;
   - un classifieur sur le seul identifiant de gabarit ;
   - les règles aveugles A et « instances saillantes » ;
   - une simulation de puissance de E1 et E4.
4. **Ce qui vérifie hors de Lazar et de Claude** :
   - l'oracle exact (T2, T6) et les scripts à graines consignées, rejouables par un tiers ;
   - après la course, des diagnostics calculés sur les sorties des bras et non jugés par un modèle (fausses alarmes de N par forme d'énoncé, rappel par strate) ;
   - un statisticien extérieur, si Lazar le souhaite (contact externe : nœud ; un brouillon de message existe au chantier).

**Demande reformulée** : fixer, avant toute mesure de la banque visée, l'instrument et l'ordre des travaux qui rendent H3 lisible sur ses deux canaux de raccourci, sans retarder H1, H2 et H4 au-delà d'une date bornée. Les sections 2 à 5 y répondent.

## 7. Pièces lues et empreintes (SHA-256, relues le 2026-11-22)

| pièce | chemin (branche) | empreinte |
|---|---|---|
| question v2 | `docs/notes/avis-carbon-astra-2026-11-22-v1/question-a-seuil-classifieur-de-style-v2.md` (claude/avis-carbon-astra-v1) | `51344c2d0d6b81b4c95392240f9bdfc0c4a5b658e27947b2223c97a820288ee6` |
| relecture de neutralité | `…/relecture-neutralite-question-a-v1.md` | `5e7111dda19a03ac0e13cf6cff72fd384579591275141140d91e99c484225ec9` |
| synthèse Carbon et Astra | `…/synthese-avis-question-a-v1.md` | `01027f00a24b8235c207098b489315c638c511b013ba15411a90bf58bd7120ef` |
| synthèse Neon | `…/synthese-avis-neon-question-a-v1.md` | `f0571a88f0f29cf474cfe2f7ceafbfe78816987d55f69bbb67e9ec85fecfdc93` |
| réponse de Carbon | `…/reponse-carbon-question-a-v1.md` | `aa66edef457c1be69c9c93b17fe41328a00766a30dd9004a9b4fd4ad4f6f1d6b` |
| réponse d'Astra | `…/reponse-astra-question-a-v1.md` | `c76d48a60b06db3a2e0cbbdf532f78496a25e1e3b851a32f46ffdb5a80665fda` |
| réponse de Neon | `…/reponse-neon-question-a-v1.md` | `e0d77af81a9537b65ea27cf601e9b9bc1486dc592b367286d043aebacd0ac64c` |
| brouillon 4 du préenregistrement | `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-4-v2.md` (claude/mathematiques-nouvelles-v1) | `212c6eca7833603bf96063e228d1a73a36c5deb1bb1c3645200a004f8033b9fe` |
| notes au directeur du brouillon 4 | `prereg/mathematiques-nouvelles-v1/notes-au-directeur-fable-b4-v2.md` | `06a9283355eda817e428d08c8269845dae2942f74ea99dade7fe8811c38ca1af` |
| vérification des corrections du brouillon 4 | `prereg/mathematiques-nouvelles-v1/verification-corrections-brouillon-4-v1.md` | `69b8aa5813fade2cd5f84e55635fdbbc43f4983dea807e6c8c44bffee9e77030` |
| sonde « instances aveugles », sortie | `prereg/mathematiques-nouvelles-v1/calculs-v4/sortie-sonde-instances-aveugles-v1.txt` | `e6ae3d493f8c4a1973b19be1a3a1fbe5a5319f76ddfde2bb2b759115e86771df` |
| vérification de la sonde et du devis v4 | `prereg/mathematiques-nouvelles-v1/calculs-v4/verification-sonde-et-devis-v4-v1.md` | `bd3b37e91fdd2170c01ffb91026581b5dc379964374884c175450f6fcffd5197` |
| mandat du brouillon 5 | `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/mandat-fable-brouillon-5-v1.md` | `b59ffc1e13e7a7959f9e921442fda25955178b6c8c5309783acffb65ecbd5186` |
| note de choix du code v6 | `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/note-choix-implementation-lot-b1-v6.md` | `7c996b824155a8892e4eaebdce76846811edafa65735f5eb6ab3a056a0b8d0b0` |
| rapport des essais du code v6 | `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/rapport-essais-r5-lot-b1-v6.md` | `0e6b4338ef2640bf23ec7f8880a56a0ef7a8926c6252cd8e4077262f56513db1` |
| aires de la version 6 | `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/v6-aires.json` | `32cd1781b48758c48395996829f11ea84eac3c2282ba71d0cfa53cf88e7d4462` |
| classifieur de style (code v6) | `src/controle_ia/oracles_plantes_v6/forme_seule.py` | `74c12fedec2a701e47fa3602bd227e156f43ecd0eab05d4ad03cebc74aab658e` |
| grammaire (code v6) | `src/controle_ia/oracles_plantes_v6/grammaire.py` | `4c0a8ffe55bae1f305ef07952b3c446c65fbcb791236b15bb9f1aa57a4c57150` |

Contexte lu sur `main` : `registres/decisions.md` (R-4898, R-4931, R-4979, R-4983, R-4985) ; `registres/go.md` (GO-2026-11-22-77, -105, -106, -109, -112).
