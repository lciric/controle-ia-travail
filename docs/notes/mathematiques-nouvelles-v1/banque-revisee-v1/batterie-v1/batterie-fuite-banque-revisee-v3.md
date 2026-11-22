# Batterie de fuite de la banque révisée — mathématiques nouvelles — v3 (texte à geler)

- **Nature** : critère de décision (pièce de classe A). Auteur : le concepteur (mandat `mandat-fable-batterie-gelee-v1.md`, `575f8c29…`, et ses compléments, adressés à Claude Fable 5.2, effort maximal ; le modèle servi est relevé dans le message de remise à la mère, non ici). Rédigé le 2026-11-22. Aucun appel de modèle, aucune dépense.
- **État : non gelé.** La v2 (`6b02a1c8…`) a été contre-lue par un Opus 5.5 neuf : « gelable après corrections » (`contre-lecture-batterie-v1.md`, `9718ec04…`). Cette v3 porte les corrections et les décisions de la mère ; ce qu'elle change est listé, remarque par remarque, dans `reponse-contre-lecture-batterie-v1.md`. Le même contre-lecteur vérifie les corrections avant le gel.
- **Ce que la batterie décide** : si la banque révisée d'énoncés plantés (version 7 du générateur, ou 8) peut porter la comparaison du système avec outil (bras S) à la lecture nue (bras N), hypothèse H3 du pilote « oracles plantés », et sous quelle lecture. Elle se calcule sans appel de modèle. Elle se juge sur le générateur, par une seule mesure sur des racines neuves, puis se relit sur la banque réelle avant tout appel.
- **Ce qu'elle ne dit pas** : une batterie tenue veut dire « aucune fuite trouvée par ces sondes et ces règles », jamais « aucune fuite ».
- **Mots de Lazar et décisions de la mère portés ici.**
  - Seuil des sondes : rappel d'au plus 0,20 à fausses alarmes d'au plus 0,10 (GO-2026-11-22-121).
  - La condition C4 joint à la règle aveugle connue une règle de trois instances au hasard (R-5036).
  - La sonde tenue à l'écart est contrôlée par un Opus 5.5 neuf avant son scellement (R-5036).
  - Portée de la banque révisée : aucun plancher ; la portée est dite en tête du rapport. **En attente du mot de Lazar ; défaut le 2026-11-24 vers 20:07Z : aucun plancher** (R-5036).
  - Deux mesures sont rapportées sans devenir des conditions : la fuite « côté vrai » et la fuite cantonnée (R-5038).
- **Écarts déclarés** aux deux jugements, au rapprochement (`bd5c2af3…`) et au mandat. Raisons : notes à la mère, § B et § C ; contre-lecture, remarques 6 et 17.
  1. La sonde des nombres apprend par squelette, sur les viviers des autres racines, et non dans la racine.
  2. Les ex æquo sont comptés au prorata, et non « bloc jamais franchi ».
  3. Le seuil de score se règle sur les vérités notées, et non sur les mondes d'apprentissage.
  4. Les sondes apprennent sur le vivier ; elles sont notées sur la sous-banque.
  5. Les racines neuves sont tirées après le scellement de tout, sonde tenue à l'écart comprise.
  6. La banque réelle est relue sur trois valeurs.
  7. Chacune des bornes hautes de C3 est jugée, et non la seule plus grande.
  8. « Littéraux tirés de la même loi » est lu « même procédure de tirage, strate constatée après » (C1, point 4).
  - Un nombre : **120 racines neuves**, et non « au moins 40 » ; accepté par la mère (R-5036).
- Pièces : `notes-a-la-mere-batterie-v1.md`, lue avec son erratum 1 ; calculs d'appui du concepteur, non vérifiés, dans `calculs-d-appui/` ; calculs du contre-lecteur dans `contre-lecture-calculs-v1/`. Empreintes entières en fin de texte.

## 0. Mots et règles de calcul

**Mots.**
- *Racine* : l'entier dont le générateur tire une banque.
- *Vivier* : tous les énoncés analysables (vérités, faux tôt, pièges) parmi lesquels la sous-banque est tirée.
- *Sous-banque* : les 150 énoncés analysés servis aux deux bras, premier service : 75 vérités, 38 faux tôt, 37 pièges. Témoins et seconds services n'entrent dans aucune mesure.
- *Strates*, jugées jusqu'au plafond 3N servi aux deux bras : *vérité* (aucun contre-exemple jusqu'à 3N), *faux tôt* (un contre-exemple jusqu'à N), *piège* (aucun jusqu'à N, un dans ]N .. 3N]).
- *Squelette* : la suite des jetons d'un énoncé (découpeur figé du paquet), chaque nombre remplacé par une même marque.
- *Paire* : une vérité et un faux (faux tôt ou piège) du même monde et du même squelette.
- *Excès* d'une sonde sur un ensemble de faux : son rappel sur cet ensemble, moins 0,10, au point de fonctionnement.

**Point de fonctionnement.** Pour une racine et une sonde, les scores des 150 énoncés de la sous-banque sont rangés du plus « faux » au plus « vrai ». Le point de fonctionnement est celui où un dixième des 75 vérités sont déclarées fausses. Le seuil se règle sur les vérités notées, hors apprentissage ; il ne lit aucun faux.

**Ex æquo.** Les énoncés de même score forment un bloc. Un bloc est pris en entier tant que la part des vérités déclarées fausses reste au plus 0,10. Le bloc qui franchirait 0,10 est compté au prorata de ce qui reste à prendre. Aucun tirage. Exemple : tous les scores égaux donnent un rappel de 0,10, donc un excès nul. Quand tous les scores sont distincts, les faux rangés entre la septième et la huitième vérité sont comptés en entier : une sonde sans information rend alors un excès moyen de +0,005 (8/76 − 0,10), et non zéro. Ce biais joue contre la banque.

**Jugement sur le générateur.** Chaque grandeur est calculée racine par racine, puis moyennée sur les racines neuves plantées. Sa *borne haute* est le 95e centile de 2 000 moyennes rééchantillonnées avec remise parmi ces racines : c'est la borne haute d'un intervalle à 90 %. Graine : `numpy.random.SeedSequence(20261122, spawn_key=(2000 + j,))`, j donné au § 1 ; centile par interpolation linéaire. Une condition **tient** si sa borne haute est au plus égale à son seuil. Il n'y a pas de zone indéterminée : un intervalle à cheval sur le seuil vaut « non tenu ».

**Non calculable = non tenu.** Si la grandeur manque pour une seule racine plantée (ensemble vide, score absent, aire non définie, sonde non calculable), la condition ne tient pas. Aucune racine n'est écartée pour rendre un calcul possible.

**Chaîne.** Les sondes lisent, octet pour octet, l'énoncé servi aux bras et la définition servie de son monde. Rien d'autre : ni identifiant, ni nom de gabarit, ni strate, ni position. Un contrôle le vérifie à chaque mesure.

## 1. Les quatre conditions

### C1 — l'invariant de construction

- **Mesuré** : rien de statistique. Le code qui plante la banque vérifie l'invariant et refuse toute banque qui s'en écarte (arrêt, comme pour les règles de forme de la version 6).
- **Sur quoi** : le vivier et la sous-banque de chaque racine neuve ; puis la banque réelle.
- **L'invariant.**
  1. *Paires.* Chaque énoncé du vivier appartient à une paire, et à une seule. Les deux membres ont le même monde, le même squelette, et des textes différents. Ils ne diffèrent donc que par des nombres écrits dans l'énoncé ; rien de ce qui les distingue n'est logé dans la définition du monde.
  2. *Proportions.* Dans chaque monde, chaque squelette porte autant de paires à faux tôt que de paires à piège. Le squelette ne dit donc rien de la strate.
  3. *Sous-banque.* La paire est l'unité de tirage : une paire est servie entière, ou pas du tout. Le tirage se fait au hasard dans chaque monde et chaque sorte de faux (enfant [2] de la racine).
  4. *Nombres.* Dans une cellule (un monde, un squelette), les nombres de tous les énoncés sont tirés par une seule procédure, qui ne reçoit pas la strate visée. La strate est constatée après le tirage, par l'évaluateur exact. Un candidat n'est écarté que si l'effectif de sa strate est déjà rempli, ou s'il échoue à la certification. Une construction directe est admise si la note du générateur montre qu'elle donne aux nombres d'une cellule, strates comprises, la même loi jointe que cette procédure. Ce point n'assure pas que les nombres aient la même loi dans les trois strates : quand la vérité dépend d'une grandeur, ces lois diffèrent par nature. Leur égalité est mesurée par C3, non garantie par C1 (écart 8).
  5. *Gabarits non appariables.* Ils sont nommés et comptés dans la note du générateur. Ils n'entrent pas dans le vivier. Aucun n'est retiré en silence.
- **Comment** : les points 1 à 3 sont des assertions du code, exécutées à chaque plantation. Le point 4 est vérifié à la lecture du code par son vérificateur, et éprouvé par la sonde des nombres. Le point 5 se lit dans la note.
- **Seuil** : zéro écart, sur chaque racine neuve plantée et sur la banque réelle.

### C2 — l'aire du classifieur de style

- **Mesuré** : l'aire qui fait foi du classifieur de style actuel, sans changement. Rappel : bayésien naïf sur les jetons de l'énoncé, nombres masqués ; appris sur trois plis de mondes entiers, noté sur le quatrième (plis tirés par l'enfant (10, 0) de la racine) ; aire de chaque strate de faux contre les vérités, hors textes déjà vus à l'apprentissage, scores mis en commun ; l'aire qui fait foi est la plus grande des deux (`forme_seule.mesurer` de la version 6, ou son portage à l'identique).
- **Sur quoi** : le vivier de chaque racine neuve.
- **Seuil** : borne haute de la moyenne ≤ **0,75** (j = 0). Valeur et calcul gardés (GO-2026-11-22-109 et -115).
- Sur une banque qui tient C1, deux membres d'une paire ont le même score : l'aire vaut 0,5 par construction, aux textes répétés près. C2 contrôle alors que C1 est bien tenu.

### C3 — le rappel de trois sondes à fausses alarmes fixées

- **Mesuré** : l'excès de chacune des trois sondes du § 2 sur trois ensembles de faux — les faux tôt, les pièges, tous les faux. Neuf grandeurs.
- **Sur quoi** : la sous-banque de chaque racine neuve. Les sondes apprennent sur des viviers ; elles sont notées sur la sous-banque.
- **Seuil** : pour chacune des neuf, borne haute de l'excès moyen ≤ **0,10**. C'est un rappel d'au plus 0,20 à fausses alarmes de 0,10, lettre retenue par Lazar (GO-2026-11-22-121). (j = 1 à 9, dans l'ordre : style, nombres, tenue à l'écart ; et pour chacune : faux tôt, pièges, tous les faux.)
- Une sonde non calculable pour une racine y rend ses trois grandeurs non calculables.
- 0,10 est une convention : la moitié de la marge de 0,20 entre les deux bras.
- Sur une banque qui tient C1, la sonde de style est aveugle par construction. La décision se joue sur la sonde des nombres et sur la sonde tenue à l'écart.

### C4 — les deux règles aveugles

- **Mesuré**, sur les 75 faux de la sous-banque de chaque racine neuve, deux parts.
  1. *Règle A.* La part des faux où la règle aveugle A du brouillon 4 (`212c6eca…`, § Bases à battre), sans retouche, rend un contre-exemple vérifié. Rappel : sans évaluer l'énoncé, elle avance au plus trois instances ; dans la k-ième, chaque variable naturelle du préfixe de tête vaut 3N, puis 1, puis N + 1 ; chaque variable à domaine borné prend la plus petite valeur de son domaine ; une instance au domaine vide ou non évaluable est abandonnée ; les doublons sont retirés ; chaque instance passe par la vérification exacte de la course (T6, plafond 3N).
  2. *Règle du hasard.* La moyenne, sur les 75 faux, de la probabilité qu'une au moins de trois instances distinctes, tirées au hasard parmi les instances de l'énoncé, soit un contre-exemple.
- **Instances et probabilité.** Une *instance* est une affectation complète du préfixe de tête : chaque variable naturelle parcourt [0 .. 3N] ; chaque variable bornée parcourt son domaine, évalué sous les variables qui la précèdent. Un domaine vide ne donne aucune instance. Une affectation dont un domaine n'est pas évaluable est écartée, et comptée. M est le nombre d'instances ; m, le nombre de celles que la vérification exacte de la course reconnaît comme contre-exemples (énoncé faux ou indéfini). La probabilité vaut 1 − C(M − m, 3)/C(M, 3) ; elle vaut 1 si M ≤ 3 et m ≥ 1, et 0 si m = 0. Un faux sans variable a une seule instance : il est réfuté à coup sûr. Si les instances d'un faux ne peuvent pas être énumérées dans les capacités du paquet, la règle est non calculable ; le générateur les énumère déjà pour certifier la strate.
- **Une probabilité exacte, et non un tirage** : elle ne dépend d'aucune graine, elle varie moins, et l'on ne peut pas la viser.
- **Tirage de contrôle**, rapporté à côté pour contrôler le calcul. Les instances sont rangées dans l'ordre d'énumération du paquet (ordre lexicographique du préfixe). Trois d'entre elles, ou toutes s'il y en a moins de trois, sont tirées sans remise par `numpy.random.default_rng(graine).choice(M, size=min(3, M), replace=False)`. La graine est `numpy.random.SeedSequence(20261122, spawn_key=(3000, i, k))` : i est le rang de la racine dans l'ordre du tirage des racines, k le rang du faux parmi les 75 faux dans l'ordre de la sous-banque servie, tous deux comptés à partir de 0. Chaque instance tirée passe par la vérification exacte. Un écart de plus de 0,02 entre la moyenne du tirage et celle du calcul exact (près de quatre écarts-types à 120 racines) est un fait d'instrument : le calcul est audité avant que C4 soit dite tenue.
- **Seuil** : borne haute de chacune des deux parts moyennes ≤ **0,50** (j = 10 pour la règle A, j = 11 pour la règle du hasard). C4 tient si les deux tiennent. Raison de la moitié, et ce que la règle du hasard coûte : § 6, faits 5 à 7.

## 2. Les trois sondes

**Règles communes.** Une sonde reçoit le texte servi d'un énoncé et la définition servie de son monde ; elle rend un score, plus haut pour « plus faux ». Pour apprendre, elle reçoit en plus la strate des énoncés d'apprentissage. Elle n'apprend jamais sur un monde qu'elle note. Elle ne calcule jamais la vérité : elle n'évalue ni l'énoncé, ni une de ses instances, ni une fonction du monde.

### 2.1 Sonde de style

Le classifieur de C2 : mêmes plis, mêmes modèles, appris sur le vivier. Ses scores sur la sous-banque donnent trois excès.

### 2.2 Sonde des nombres (spécification gelée avec ce texte)

Sa question : à squelette égal, que disent les nombres écrits ?

- **Lecture.** Un *littéral* est un nombre écrit dans l'énoncé. Une fraction entre parenthèses, « (a/b) » ou « (-a/b) », fait un seul littéral ; « (-a) » aussi ; tout autre nombre est un littéral positif, pris à sa valeur. On en garde : le signe, le numérateur écrit a, le dénominateur écrit b (1 hors fraction), la valeur absolue v = a/b. Si b = 0, v et le trait 3 valent 0.
- **Repères du monde.** N, la borne du monde. D, l'ensemble, sans doublon, des valeurs absolues de tous les nombres de la définition servie (borne, paramètres, constantes). d, le plus grand nombre de D.
- **Traits de chaque littéral**, dans l'ordre d'écriture (17) :
  - 1 à 3 : log₁₀(1 + v) ; log₁₀(1 + a) ; log₁₀(b) ;
  - 4 et 5 : log₁₀(1 + 1/v), ou 0 si v = 0 ; log₁₀(1 + 1/|v − 1|), ou 0 si v = 1 ;
  - 6 à 8 : v = 0 ; v = 1 ; v = 2 (chacun vaut 0 ou 1) ;
  - 9 et 10 : v ≤ N ; N < v ≤ 3N ;
  - 11 à 13 : part des nombres de D strictement inférieurs à v ; v est dans D ; log₁₀((1 + v)/(1 + d)) ;
  - 14 à 16 : carrés des traits 1, 2 et 3 ;
  - 17 : signe négatif.
- **Traits de chaque couple de littéraux** (2) : le rapport de la plus petite valeur absolue à la plus grande (1 si les deux sont nulles) ; l'égalité des deux valeurs absolues.
- **Trait de l'énoncé** (1) : le nombre de chiffres écrits.
- **Modèle.** Un modèle par squelette : régression logistique « faux contre vérité ». Traits centrés et réduits sur l'apprentissage (écart-type de l'apprentissage, diviseur n) ; un trait constant est mis à zéro. Le modèle est le minimum, unique, de la *perte* : la somme des pertes logistiques, plus la moitié de la somme des carrés de tous les poids, ordonnée à l'origine comprise. Score : la combinaison linéaire, arrondie à 10 décimales. Calcul en double précision. Aucun tirage.
- **Calcul du minimum : Newton amorti**, à partir de poids nuls. À chaque tour, on calcule la direction de Newton d, solution de « hessienne × d = gradient », et le *décrément*, produit scalaire du gradient et de d.
  - Si le décrément est au plus 10⁻¹³ fois le nombre d'énoncés d'apprentissage, on retranche d aux poids et le calcul s'arrête : il a convergé.
  - Sinon on cherche un pas t : il vaut 1, puis il est divisé par deux tant que la perte aux poids diminués de t × d ne baisse pas d'au moins 10⁻⁴ × t × décrément. Soixante essais au plus (t de 1 à 2⁻⁵⁹). Le premier t qui convient est pris : on retranche t × d aux poids.
  - 200 tours au plus.
- **Garde de convergence.** Un apprentissage qui n'a pas convergé — 200 tours faits, soixante essais sans pas qui convienne, ou une valeur non finie — rend la sonde non calculable pour les racines qu'il sert à noter. Le nombre de ces apprentissages est rapporté. Aucun repli.
- **Pourquoi ce calcul.** Un Newton sans amortissement peut diverger quand la séparation est franche : plus la fuite est nette, plus la sonde risque de la manquer (contre-lecture, remarque 2 : 125 apprentissages sur 480). L'arrêt se juge sur le décrément, et non sur la taille du pas. Jugé sur le pas de Newton entier, il ne se déclenche pas toujours : près du minimum, la baisse de la perte passe sous sa précision de calcul, la recherche du pas piétine, et un apprentissage arrivé au minimum est déclaré « non convergé » (sur le banc : 8 apprentissages sur 12 de l'artefact « fenêtres », 1 sur 12 de la banque saine ; `sortie-calcul-6-v2.txt`, partie E). Jugé sur le pas effectif, comme le propose la contre-lecture, il rend les mêmes poids sur le banc (à 3 × 10⁻⁸ près, même sortie) ; mais il conclut aussi à la convergence quand la recherche piétine. Le décrément mesure l'écart au minimum lui-même.
- **Apprentissage, par mondes entiers.** Pour noter la sous-banque d'une racine, chaque modèle apprend sur les énoncés de son squelette dans les viviers de toutes les autres racines neuves plantées. Un monde d'apprentissage dont les paramètres servis sont ceux d'un monde noté est écarté. Si un squelette a moins de 20 énoncés d'apprentissage, ses énoncés reçoivent le score 0 ; leur nombre est rapporté. Si, pour une racine, plus d'un énoncé de la sous-banque sur dix reçoit ce score 0, la sonde y est non calculable : elle ne sait pas lire cette banque.
- **Banque réelle.** Les modèles apprennent sur les viviers de toutes les racines neuves plantées, avec la même mise à l'écart.
- Sur une banque qui tient C1, l'ordonnée à l'origine est proche de zéro et la sonde ne lit guère que les nombres. Sinon elle lit aussi le squelette, et c'est voulu.

### 2.3 Sonde tenue à l'écart du concepteur : ce que le vérificateur a le droit de faire

Auteur : le vérificateur du code de la banque révisée, qui est un autre modèle que le concepteur. Moment : après le gel du générateur. But : une sonde que le concepteur n'a pas pu viser.

**Permis.**
1. Lire ce texte, le code figé du générateur et sa note, les deux jugements, le diagnostic.
2. Engendrer, par le code figé, autant de banques qu'il veut sur des racines d'essai qu'il écrit dans sa note avant de s'en servir ; y essayer autant de sondes qu'il veut.
3. Choisir librement les traits et le modèle, dans les règles communes. Il peut découper et analyser le texte par la grammaire, compter, et comparer les nombres écrits entre eux et aux nombres servis (ordre, différence, rapport, logarithme, nombre de chiffres, parité, divisibilité).
4. Choisir l'un des deux apprentissages de ce texte : dans la racine, par plis de mondes entiers (enfant (10, 0)), sur le vivier ; ou sur les viviers des autres racines neuves, avec la même mise à l'écart des mondes de mêmes paramètres.

**Interdit.**
5. Voir une racine neuve, une banque qui en vient, ou la banque réelle. Les racines neuves ne sont tirées qu'après le scellement de sa sonde (§ 3).
6. Évaluer l'énoncé ou une de ses instances ; remplacer une variable par une valeur ; calculer une fonction du monde ; appeler l'évaluateur, le normaliseur, les tests de mort ou le générateur.
7. Lire autre chose que le texte servi et la définition servie.
8. Rendre plus d'une sonde, ou garder un choix à faire après le tirage des racines neuves.
9. Recevoir une suggestion du concepteur ; montrer la sonde, sa note ou ses essais au concepteur, ou à quiconque écrit ou corrige le générateur, avant le rapport de la mesure.

**Dû.**
10. Une sonde déterministe, ou à graine consignée, sur processeur seul. Si elle apprend par un calcul itératif, elle porte sa propre garde de convergence.
11. L'épreuve du § 4 : la sonde doit tenir sur la banque saine ; ses résultats sur les artefacts sont rapportés.
12. Code, note (ce que la sonde lit, ce qu'elle apprend, les racines d'essai employées, le nombre de sondes essayées et écartées) et empreintes, scellés et poussés avant le tirage des racines neuves. Avant le scellement, un Opus 5.5 neuf, qui n'est ni le concepteur ni l'auteur de la sonde, contrôle les points 5 à 8. Il ne transmet rien au concepteur avant le rapport de la mesure.

**Retrait.** La sonde peut être retirée, avec une ligne d'écart, si elle n'est pas scellée à temps ou si elle ne tient pas sur la banque saine. Le retrait se décide avant le tirage des racines neuves, jamais après. C3 se juge alors sur six grandeurs.

**Version 8.** La sonde de la version 7, désormais connue du concepteur, reste dans la batterie. Une sonde neuve est écrite dans les mêmes règles.

## 3. Les racines neuves

1. **Tout est gelé avant le tirage** : ce texte ; le code du générateur (commit) et sa certification (rejeu sans appel conforme, vérification du code sans remarque bloquante) ; le code de la batterie, contre-lu ; l'épreuve du § 4, passée ; la sonde tenue à l'écart, scellée ou retirée.
2. **Tirage** : 120 racines, par `secrets.randbits(128)`, par une commande qui inscrit le commit du gel.
3. **Engagement** : l'empreinte SHA-256 de l'écriture décimale de chaque racine, dans l'ordre du tirage, est scellée, commitée et poussée avant qu'aucune banque de ces racines soit engendrée.
4. **Une seule mesure** : toutes les racines, toutes les conditions, un seul rapport, échec compris. Aucune racine n'est choisie ni retirée.
   - Une racine que le générateur refuse de planter est comptée et nommée ; le taux de refus est dit en tête du rapport. Les conditions se calculent sur les racines plantées. S'il en reste moins de 40, aucune condition ne tient.
   - Une panne technique n'est pas un résultat : la mesure est relancée sur les mêmes racines et le même code, et c'est dit.
   - Tout changement de code après le tirage fait une version neuve.
5. **Après la mesure** : les racines sont écrites en clair au manifeste final. Elles deviennent des racines d'essai.
6. **Version 8.** Elle n'est tentée que si la version 7 ne tient pas les quatre conditions. La décision de la tenter est écrite avant sa mesure. Elle se mesure sur un autre lot de 120 racines, tiré de la même façon, avec une sonde tenue à l'écart neuve. Deux cycles au plus (versions 7 et 8), et rien après le 2026-12-04T23:59Z. Toutes les tentatives sont rapportées. La version qui fait foi est fixée d'avance (§ 5).

## 4. L'épreuve de la batterie avant emploi (règle R5)

Le code de la batterie est éprouvé avant le tirage des racines neuves, sur des banques où l'on sait ce qui doit tenir et ce qui doit tomber. Un attendu manqué arrête tout. On corrige alors le code, jamais l'attendu ; si le défaut est dans ce texte, il revient au concepteur.

**Banc d'épreuve.** Une réalisation existe : `calculs-d-appui/calcul_4_banc_d_epreuve_v2.py`. Chaque monde a une borne N (4, 10 ou 15) et une constante servie PM, nombre premier plus grand que 3N + 1. L'énoncé de base est « pour tout n dans NAT, mod(A * n + C, PM) != R », en quatre écritures. Il a au plus un contre-exemple n₀ jusqu'à 3N, et sa strate ne se lit que par le calcul de n₀. 120 racines d'épreuve sont fixées d'avance.

| banque | construction | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|
| saine | A et C tirés uniformément ; n₀ uniforme dans la région de sa strate ([2 .. N] pour un faux tôt) ; R calculé. Mêmes lois de nombres dans les trois strates | tient | tient | tient, pour chaque sonde | tient, pour les deux règles |
| vérité par la grandeur du littéral, doses 1 et 0,5 | avec la probabilité « dose », R est tiré dans la moitié haute ou la moitié basse selon la strate ; le sens change d'une écriture à l'autre | tient | tient | **tombe**, par la sonde des nombres | tient |
| relation entre deux littéraux, dose 1 | pour une vérité, R = C − d modulo PM, d tiré de 1 à 5, A en étant déduit ; les lois de A, C et R, prises une à une, ne changent pas | tient | tient | **tombe**, par la sonde des nombres | tient |
| vérité par le gabarit | chaque écriture ne porte qu'une strate | **tombe** | **tombe** | **tombe**, par les sondes de style et des nombres | rapportée, non exigée |
| contre-exemple au plafond | banque saine, sauf n₀ = 1 pour les faux tôt et n₀ = 3N pour les pièges | tient | tient | tient | **tombe**, par la règle A |
| contre-exemples denses à côté des trois instances connues | énoncé « n < K ou n > L », en quatre écritures, faux sur [K .. L] ; fenêtre large dans [2 .. N] pour un faux tôt, dans [N + 2 .. 3N − 1] pour un piège, vide pour une vérité | tient | tient | rapportée, non exigée | **tombe**, par la règle du hasard ; la règle A tient |
| version 6, sur ses 41 racines d'essai déjà exposées | la banque actuelle | **tombe** | **tombe** (moyenne 0,966) | **tombe** | **tombe** (règle A 0,846 ; règle du hasard 0,738) |

Rapportées, non exigées : « grandeur » à la dose 0,25 (excès moyen 0,086 ; borne haute 0,097 à 0,100 : le bord de la tolérance) ; « relation » à la dose 0,5 (excès moyen 0,109 ; borne haute 0,12 à 0,13 ; mesure « côté vrai » 0,42).

Sur la banque saine du banc, les faux tôt ont leur contre-exemple à n₀ ≥ 2. Ce choix, fait en connaissant la règle A, la rend presque muette (0,07). Ce n'est pas une propriété d'une banque saine quelconque.

**Gardes d'arrêt**, chacune éprouvée sur un cas sain et sur un artefact :
- les assertions de C1, une par une : une paire à cheval sur deux mondes ; une paire de squelettes différents ; une paire de textes identiques ; un squelette à deux paires à faux tôt et aucune à piège dans un monde ; une sous-banque qui sert un seul membre d'une paire. Chacune est arrêtée par l'assertion qu'elle vise ; la banque saine n'en déclenche aucune ;
- le contrôle de chaîne : un harnais qui passe à une sonde l'identifiant, le nom de gabarit ou la strate d'un énoncé noté est arrêté ;
- l'audit « trop beau » : une sonde aux scores inversés (excès de −0,10) le déclenche ;
- le plancher de 40 racines : avec 39 racines plantées, aucune condition ne tient ;
- la garde de convergence : un apprentissage arrêté avant convergence rend la sonde non calculable, et C3 non tenue ;
- l'audit du tirage de contrôle : un calcul exact faussé (contre-exemples comptés jusqu'à N seulement) fait passer l'écart au-dessus de 0,02 ; le calcul juste le laisse au-dessous ;
- « non calculable » : un ensemble vide, un score manquant, une aire non définie, plus d'un énoncé sur dix noté 0 faute d'apprentissage, un faux aux instances non énumérables rendent « non tenu », sans plantage et sans racine écartée.

**Sont aussi éprouvés** :
- la fonction de rappel, sur trois cas d'école : scores tous égaux (excès 0) ; séparation parfaite (excès 0,90) ; 9 vérités sur 75 et 45 faux sur 75 à un même score haut, le reste plus bas (excès 0,40) ;
- la règle du hasard, sur trois cas d'école : un contre-exemple parmi 13 instances (3/13) ; un faux sans variable (1) ; aucun contre-exemple vérifiable (0) ;
- la reproductibilité : deux passes rendent les mêmes sorties à l'octet ;
- la relecture du § 5 : une valeur hors de sa plage ferme la lecture en verdict ;
- la règle « version qui fait foi » du § 5, cas par cas ;
- en description, l'indépendance des racines : la sonde des nombres apprise sur l'autre moitié des racines, comparée à la sonde apprise sur toutes les autres.

Le prototype du concepteur obtient ces attendus, sauf trois gardes qu'il ne porte pas : le contrôle de chaîne, « plus d'un énoncé sur dix noté 0 », et « instances non énumérables » (`sortie-calcul-4-v2.txt` pour le banc, les gardes, les branches et les deux moitiés ; `sortie-calcul-5-v2.txt` pour la version 6 ; `sortie-calcul-6-v2.txt` pour les cas d'école et l'audit du tirage). Dans le prototype, le tirage de contrôle lit le statut des instances dans le profil qui sert au calcul exact ; l'instrument les passe par la vérification exacte de la course.

## 5. Lecture, branches, relecture

**Sur le générateur**, après la mesure.

| issue | les bras courent sur | lecture |
|---|---|---|
| une version fait foi, et elle tient C2 et C3 | cette version | lecture en preuve ; lecture en verdict ouverte |
| une version fait foi, mais C2 ou C3 n'y tient pas | cette version | lecture en preuve seule ; verdicts déclarés en description |
| aucune version ne fait foi | la version 6 | lecture en preuve seule ; verdicts déclarés en description ; la banque révisée passe au pilote 2 |

- **La version qui fait foi** est fixée d'avance : c'est la dernière version (7, puis 8) figée, certifiée et mesurée au plus tard le 2026-12-04T23:59Z qui tient C1 et C4. Rien n'est choisi après lecture. Une version 8 qui tient C1 et C4 remplace la version 7, quel que soit le reste. Une version 8 qui ne les tient pas laisse en place la version 7, si celle-ci les tenait.
- **Portée.** Aucun plancher de familles ni de squelettes n'est exigé. La portée — familles et squelettes servis, gabarits écartés — est dite en tête du rapport. **En attente du mot de Lazar ; défaut le 2026-11-24 vers 20:07Z : aucun plancher.**
- **La lecture en preuve** est calculée dans toutes les branches. Son libellé est « réfutations certifiées » ; jamais « détection », jamais « discerne mieux ». Toute affirmation porte sur « le système avec outil » (agent à outil, plusieurs tours, relecture par une autre famille), jamais sur « l'outil ». Aucun bras payant neuf pour le relecteur.
- **Quand C4 ne tient pas** — c'est le cas de la version 6 —, le rapport porte la phrase écrite d'avance : « un gain d'au moins 0,20 en preuve est hors de portée sur cette banque ». Elle se lit ainsi : une règle sans calcul y rend déjà un contre-exemple sur plus de la moitié des faux ; un écart avec la lecture nue, même établi, n'y est jamais lu comme un gain dû au calcul. La phrase s'applique aussi si, sur la banque réelle, la part de l'une des deux règles dépasse 0,50.
- **Trop beau** (règle R4). Un excès moyen sous −0,03, ou une aire qui fait foi moyenne sous 0,45, est un fait d'instrument. La sonde est auditée (chaîne, plis, étiquettes) avant que sa condition soit dite tenue.
- **Instances saillantes.** Si la règle des instances saillantes (§ 7) dépasse 0,50 en borne haute alors que C4 tient, c'est écrit en tête du rapport. L'affirmation « le système avec outil dépasse la règle aveugle » (E4) se lit alors avec cette réserve.

**Sur la banque réelle**, au rejeu sans appel, avant tout appel.
- C1 est vérifié par le code. Un écart est un défaut de plantation : aucun lancement.
- Trois valeurs sont relues : l'aire qui fait foi ; le plus grand des excès de C3 ; la plus grande des deux parts de C4. Chacune est comparée à la plage, du minimum au maximum, de la même valeur sur les racines neuves plantées.
- Une valeur hors de sa plage, au-dessus ou au-dessous, ferme la lecture en verdict. C'est dit en tête du rapport, et expliqué avant la course. La lecture en preuve reste calculée.
- Avec 120 racines, une banque saine sort d'une des trois plages dans 5 % des cas au plus (2 chances sur 121 par valeur). Ce calcul suppose que la banque réelle s'échange avec une racine neuve : même générateur, racine tirée de la même façon. C'est presque exact : sa sonde des nombres apprend sur 120 viviers, celle d'une racine neuve sur 119.
- Si la lecture en verdict est déjà fermée, les trois valeurs sont seulement rapportées.

## 6. Les faits du diagnostic pris en compte

Source : `note-diagnostic-v6-opus-v1.md` (`da4d80f4…`), 41 racines d'essai de la version 6.

1. **L'identifiant de gabarit sépare tout** : aire 1,000, et aucun gabarit ne porte deux strates. Réponse : C1, points 1 et 2 ; le squelette ne porte plus aucune information. L'artefact « vérité par le gabarit » l'éprouve.
2. **La longueur en jetons sépare en partie** : aire 0,646 pour « court = faux ». Elle entre dans C1, non dans une sonde : deux membres d'une paire ont le même squelette, donc le même nombre de jetons. La longueur en caractères ne dépend alors plus que des chiffres : elle entre dans la sonde des nombres (trait « nombre de chiffres écrits »).
3. **Les nombres trahissent ce que le classifieur ne voit pas** : la règle « chiffres du plus grand littéral » atteint 0,956 sur les pièges. Réponse : la sonde des nombres. Elle apprend par squelette et sur les autres racines, parce qu'une sonde commune à tous les gabarits, apprise dans la racine, ne voit pas une fuite dont le sens change d'un gabarit à l'autre : sur l'artefact « grandeur » à pleine dose, le prototype du diagnostic rend un excès moyen nul (borne haute 0,010) ; la sonde par squelette rend 0,90 (`sortie-calcul-3-v1.txt`, partie A ; refait par le contre-lecteur avec son propre code : 0,00 contre 0,90).
4. **La règle aveugle touche 63 des 75 faux** en médiane (60 à 68 ; moyenne 0,846). Réponse : C4, règle A. La version 6 ne la tient pas.
5. **La comparaison à la règle aveugle manque de puissance** : 0,12 au plus sur la version 6, dès que le système avec outil manque un faux sur dix parmi ceux que la règle touche (diagnostic, partie h). D'où le seuil d'une moitié. Si le système avec outil rend un contre-exemple sur 90 % des faux à portée de la règle et sur 50 % des autres, la puissance de E4 vaut 0,94 quand la règle touche 48 % des faux, 0,74 à 56 %, 0,40 à 64 %, 0,003 à 84 % (calcul exact, `sortie-calcul-1-v1.txt`, partie 5).
6. **La fuite d'instance tient à la densité des contre-exemples, pas seulement au plafond.** Un gabarit ne résiste à la règle aveugle que par accident (« puissance majorée à un pas », faux sur 80 % de ses instances). Trois instances tirées au hasard réfutent 74 % des faux de la version 6 : 91 % des faux tôt, où 77 % des instances en moyenne sont des contre-exemples, et 56 % des pièges, où 28 % le sont (`sortie-calcul-5-v2.txt`). Réponse : la règle du hasard, jointe à C4 par la mère.
7. **Ce que la règle du hasard coûte.** Pour un énoncé à une variable naturelle (13, 31 ou 46 instances selon la famille) :
   - un faux à un seul contre-exemple compte 0,23, 0,10 ou 0,07 ;
   - un piège dont les contre-exemples forment une queue, de son premier contre-exemple jusqu'à 3N, compte 0,65 à 0,69 en moyenne ;
   - un faux sans variable compte 1.
   Repère : la part passe la moitié quand une instance sur cinq environ est un contre-exemple. Dans la petite famille, deux contre-exemples parmi 13 instances comptent 0,42, et trois comptent 0,58 (`sortie-calcul-5-v2.txt` ; `sortie-calcul-6-v2.txt`, partie B). La règle n'est pas intenable par construction : la banque saine du banc est à 0,13. Elle écarte les faux « faux presque partout » et les fenêtres denses. Les pièges en queue étaient déjà limités par la règle A, qui les touche tous à l'instance 3N.

## 7. Rapporté sans effet sur la décision

Par racine (minimum, médiane, maximum) et en moyenne avec sa borne haute :
- les aires du classifieur de style : par strate, sur tous les faux, et contre les vérités du même squelette ; l'aire d'un classifieur sur le seul squelette (0,500 attendu sous C1) ;
- **l'excès « côté vrai »** de chaque sonde : au point où un dixième des 75 faux sont déclarés vrais (scores rangés du plus « vrai » au plus « faux », ex æquo au prorata), la part des vérités déclarées vraies, moins 0,10. Mesure demandée par la mère ; elle n'est pas une condition (R-5038) ;
- **les excès par famille et par squelette** : le même calcul, sur les seuls énoncés de la famille ou du squelette, le seuil étant réglé sur ses vérités ;
- la sonde numérique prototype du diagnostic, telle quelle ; les excès de C3 à la règle « bloc entier » ; le nombre d'apprentissages non convergés et d'énoncés notés 0 ;
- les deux règles de C4 par strate et par squelette ; l'instance 3N seule ; le tirage de contrôle de la règle du hasard ; la part des énoncés clos ou à variables toutes bornées ; le nombre d'affectations écartées ;
- **la règle des instances saillantes** : part des 75 faux réfutés par au moins une instance où toutes les variables naturelles ont la même valeur, prise parmi 0, 1, 2, N, N + 1, 2N, 3N, et c − 1, c, c + 1 pour tout entier c écrit dans l'énoncé, dans [0 .. 3N] ; variables bornées à leur plus petite valeur ;
- le taux de refus des racines.

## 8. Ce qui pourrait rendre cette batterie fausse

1. **Les sondes sont simples.** Un modèle de langue lit des indices qu'aucune sonde ne voit. Tenue ne veut pas dire sans fuite.
2. **Les sondes sont trop fortes.** La sonde des nombres apprend sur des milliers d'énoncés étiquetés ; un bras lit un énoncé seul. C3 peut fermer la lecture en verdict pour une fuite qu'aucun bras n'exploiterait.
3. **La frontière entre forme et calcul est floue.** Une égalité entre deux nombres écrits peut valoir un calcul à l'instance 0. Une sonde peut compter comme fuite un raisonnement élémentaire, ou le manquer.
4. **C3 ne regarde que le côté faux.** Une fuite qui fait reconnaître une partie des vérités, sans rien dire des faux, y est presque invisible : sur l'artefact « relation » à demi-dose, l'excès mesuré est 0,109, au bord du seuil, quand la mesure « côté vrai » rend 0,42. Sous C1, ni C2 ni la sonde de style ne la voient. Elle est rapportée (§ 7), sans effet.
5. **Le seuil de 0,10 tolère une fuite cantonnée ou diluée.** L'excès d'une fuite parfaite, cantonnée à une part des énoncés que la sonde reconnaît, vaut cette part. Sur un quart des énoncés (une écriture sur quatre), elle fait tomber C3 : excès 0,25. Sur nettement moins d'un dixième, elle le tient par construction ; sur le banc, à un douzième, l'excès est 0,064 (borne haute 0,07 à 0,08). Une fuite diluée le tient aussi, de justesse : quand un quart des énoncés suivent une loi révélatrice que les autres imitent par hasard, l'excès est 0,086 (borne haute 0,097 à 0,100). Les excès par squelette (§ 7) sont là pour le voir, sans effet sur la décision (`sortie-calcul-4-v2.txt`, banques « cantonnée » et « grandeur » à la dose 0,25).
6. **C4 peut encore être tenue à la lettre.** La règle du hasard mesure la densité des contre-exemples, non leur place. Des contre-exemples rares, mais toujours logés au même endroit saillant, tiennent les deux règles. La règle des instances saillantes le montre (§ 5, § 7) ; elle ne décide rien.
7. **Le point 2 de C1 peut être hors de portée des mathématiques.** Un squelette qui ne peut porter qu'une sorte de faux sort du vivier. Si trop de squelettes sortent, la banque révisée échoue sans qu'aucune fuite soit en cause.
8. **Sous C1, C2 et la sonde de style ne mesurent plus rien.** Elles ne protègent que contre un invariant mal codé. Le poids de C3 repose sur deux sondes, sur une seule si la sonde tenue à l'écart est retirée.
9. **Les nombres sont des conventions** : 0,10 ; la moitié ; 120 racines ; −0,03 ; 0,75. Avec 120 racines, une banque dont l'excès vrai est 0,08 échoue encore une fois sur deux environ, parce que la condition porte sur la borne haute (`sortie-calcul-1-v1.txt`, partie 3).
10. **La relecture par la plage** ne voit qu'une anomalie grossière. Elle ferme à tort la lecture en verdict dans 5 % des cas au plus.
11. **Le rééchantillonnage suppose des racines indépendantes.** La sonde des nombres apprend sur les autres racines : les valeurs par racine partagent leurs modèles. Sur le banc, la même sonde apprise sur l'autre moitié des racines rend des bornes de même largeur (`sortie-calcul-4-v2.txt`, partie D) : l'effet est petit. Il n'est pas mesuré sur la banque révisée.
12. **La garde de convergence peut se tromper dans l'autre sens.** Un critère d'arrêt mal choisi déclare « non convergé » un apprentissage arrivé au minimum, et ferme C3 à tort (`sortie-calcul-6-v2.txt`, partie E). Le décrément a convergé sur tous les apprentissages du banc et de la version 6, en 16 tours au plus ; cela ne prouve pas qu'il convergera sur la banque révisée.
13. **Le banc d'épreuve est un monde d'école.** Le passer ne prouve pas que la batterie voit les fuites propres à la banque révisée.
14. **La règle des ex æquo est la mienne.** Le rapprochement gardait le bloc entier, qui rend un excès de −0,10 là où le prorata rend 0,40 quand la fuite est portée par un trait grossier (`sortie-calcul-1-v1.txt`, partie 0 ; confirmé par le contre-lecteur). Si la mère revient au bloc entier, cet angle mort revient avec.
15. **Le prototype n'est vérifié qu'en partie.** Il est de moi, alors que le code revient à Opus. Le contre-lecteur a refait par son propre code les deux épreuves qui portent les écarts 1 et 2 ; le reste ne l'est pas. Un défaut y changerait les attendus chiffrés du § 4, non les conditions.
16. **Le même concepteur écrit la batterie puis la banque.** La sonde tenue à l'écart, les racines neuves, la règle du hasard et l'épreuve bornent ce risque ; elles ne le suppriment pas.

## 9. Confiance

| point | confiance |
|---|---|
| C1 ferme la fuite de forme par construction, et se vérifie par le code | 0,85 |
| la sonde des nombres voit une vérité portée par la grandeur d'un littéral ou par une relation entre deux littéraux, quel qu'en soit le sens | 0,80 |
| une banque saine tient C2 et C3 (cas sain simulé et banc d'épreuve) | 0,90 |
| le calcul de la sonde des nombres converge, et sa garde ne se déclenche pas à tort | 0,85 |
| le prorata est la bonne règle des ex æquo | 0,85 |
| C4, à deux règles, garde la lecture en preuve | 0,70 |
| 120 racines, et la relecture par la plage | 0,70 |
| la sonde tenue à l'écart est écrite, scellée et utile dans les délais | 0,60 |
| ensemble : la batterie classe juste une banque saine et une banque qui fuit | 0,75 |

## Empreintes (SHA-256 entières, relevées par `sha256sum` le 2026-11-22)

| pièce | chemin | sha256 |
|---|---|---|
| mandat | `docs/notes/mathematiques-nouvelles-v1/banque-revisee-v1/mandat-fable-batterie-gelee-v1.md` | `575f8c298477aeb72d769b017d4a72e86b63991a7f8b1b38279c213c335eca27` |
| version 2 de ce texte, remplacée | `…/batterie-v1/batterie-fuite-banque-revisee-v2.md` | `6b02a1c86d83355091bbfeb499fd1996fff99b96916f18752d2b8b3404568eee` |
| version 1 de ce texte, remplacée | `…/batterie-v1/batterie-fuite-banque-revisee-v1.md` | `428ddb6c53a8a303d03d49c85949d3adc3eec1c209bdf25c64db5631062dc82a` |
| contre-lecture de la version 2 | `…/batterie-v1/contre-lecture-batterie-v1.md` | `9718ec040598dd73912e525f3403856ee08e5ffd69e8b7c0c447f80c435f4790` |
| rapprochement des deux batteries | `…/banque-revisee-v1/rapprochement-batteries-fable-opus-v1.md` | `bd5c2af3a8d61fb7fb259e0982760cf4e4606ca2981b24f8a3e6903cf559d5bb` |
| jugement du juge Fable | `…/banque-revisee-v1/juges-recus/juge-fable-max-v1.md` | `b1380fe3a7cf0da9304a03bb829d9d22e8c21930b53456485ed2ac7713c0bc08` |
| son erratum 1 | `…/banque-revisee-v1/juges-recus/juge-fable-max-v1-erratum-1.md` | `81073193c2a65a6664ddd9862366e299e357581c0538d4f98cb8c7bf08622223` |
| jugement du juge Opus | `…/banque-revisee-v1/juges-recus/juge-opus-max-v1.md` | `f82e0c8f924e7d5016a5cb464a091a39b510edd8dcdb32d432f95fe898576688` |
| note du diagnostic | `…/banque-revisee-v1/diagnostic-opus-v1/note-diagnostic-v6-opus-v1.md` | `da4d80f48a810367fd036f142c499af30d6caa43f8b836024fcb659e5d67d08e` |
| script du diagnostic | `…/banque-revisee-v1/diagnostic-opus-v1/diagnostic-fuite-v6-opus-v1.py` | `ea853af489f7f285a55ed2a16839f0b736e8f00a8fd69a39a072fb46ae5347e3` |
| brouillon 4 du préenregistrement | `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-4-v2.md` | `212c6eca7833603bf96063e228d1a73a36c5deb1bb1c3645200a004f8033b9fe` |
| classifieur de style (code de la version 6) | `src/controle_ia/oracles_plantes_v6/forme_seule.py` | `74c12fedec2a701e47fa3602bd227e156f43ecd0eab05d4ad03cebc74aab658e` |
| outils des calculs d'appui | `…/batterie-v1/calculs-d-appui/outils_batterie_v1.py` | `40194ed59342579b5f7fb3dcf5b034ed1de25e9d0401cf057b606726079107ef` |
| sondes et conditions, prototype v1 | `…/batterie-v1/calculs-d-appui/sondes_batterie_v1.py` | `9c6947589a59b27c11932ec4bea3cbd556dd8a052a1506f6feca23d4bfe9cb41` |
| sondes et conditions, prototype v2 (Newton amorti, règle du hasard) | `…/batterie-v1/calculs-d-appui/sondes_batterie_v2.py` | `83c45cf9c41b22b6ab4d63b46af557c31a4725a00f661986c0fb8cea683ae50b` |
| calcul 1 (cas sain simulé, lectures du seuil, relecture, puissance) | `…/calculs-d-appui/calcul_1_hasard_lectures_puissance_v1.py` | `83616c771e3573f923b6142149e1d7f35a2a18fcecebb2060665d89e16cf140e` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-1-v1.txt` | `923ea21587d82ca4bfaa3439841b6ee67068351ba1273f61be32a45ec8548d36` |
| calcul 3 (sonde prototype sur le banc ; première batterie sur la version 6) | `…/calculs-d-appui/calcul_3_prototype_et_version_6_v1.py` | `cef21e49c7740ddb2612b60f8a3b024b9eef4713582c34c227410b050fca8f95` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-3-v1.txt` | `f9dffc3683f1851f0d279dabe324655ec3a222e7d75099d32676cc25ed496f8e` |
| calcul 4 (banc d'épreuve de cette version) | `…/calculs-d-appui/calcul_4_banc_d_epreuve_v2.py` | `483700afe831342fc47f1e6ef80c02df533ce93ce370ee7ca4822425ee8b18b2` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-4-v2.txt` | `458daedeac36a72f6277f0388dbaf6f189c75b3acd711c7752b9a34ea7872fc8` |
| calcul 5 (cette version sur la version 6) | `…/calculs-d-appui/calcul_5_version_6_v2.py` | `5908e732412a8683b82250a6484accb59af311c5f301171af197075b3de15df8` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-5-v2.txt` | `4e1cd5c4baa07827a9ecbabbaa6d58e4bfd5bb3c87ffac18be7a799b1381abcf` |
| calcul 6 (cas d'école ; critère d'arrêt de la sonde des nombres ; audit du tirage de contrôle) | `…/calculs-d-appui/calcul_6_cas_d_ecole_v2.py` | `ed7bf57e5e83fdf896559032fac0d67fcd832d3812680016c5b13083c377cca2` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-6-v2.txt` | `2cc95490f89915575e3d3693319bf6b1b76a3ecdae5f7a2237bf2a7c90753ae5` |

Le calcul 2 (banc d'épreuve de la version 1 du texte) et sa sortie restent au dossier ; le calcul 4 les remplace. Les sorties en JSON de chaque calcul sont dans le même dossier, avec leurs compagnons. Mots de Lazar cités : GO-2026-11-22-109, -115 et -121, `registres/go.md` sur `main`. Décisions de la mère citées : R-5036 et R-5038, `registres/decisions.md` sur `main` (lues au commit `184aa5abf7a9502d60bf7f44a6e0f5f97f7183b9`).
