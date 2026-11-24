# Lecture à l'aveugle du collisionneur sur le harnais « étroit et profond » — lecteur Opus, v1

Lecteur neuf. Un seul fichier lu en entier : `dossier-aveugle-v1.md` (consigne, question, cinq conceptions A à E au tour III.1, cinq critiques croisées au tour III.2, cinq réponses au tour III.3). Aucun autre fichier ouvert. Je n'ai rien exécuté.

Conventions :
- « T1 », « T2 », « T3 » désignent les tours III.1 (conception), III.2 (critique croisée) et III.3 (réponse aux critiques).
- Pour chaque proposition, je sépare la nature de ce qui la soutient : **argument** (raisonnement de méthode), **calcul** (arithmétique ou identité sur des paramètres hypothétiques, refaite par un modèle mais non auditée), **mesure** (aucune : rien n'a été exécuté dans le dossier). Aucune proposition n'est soutenue par une mesure.
- Tous les coûts et effectifs sont des ordres de grandeur illustratifs, repris ou déduits des pièces ; ils ne sont pas des devis.
- Je n'écris pas de critère de mort (protocole X 2.1) : seulement ce que l'épreuve mesure, son coût, une date au plus tard et un témoin faux connu.

---

## Propositions retenues

### P1 — Étroitesse définie contre un panel de référence nommé, disjoint des bras qui concourent, à budget de sonde découplé du budget du duel
- **Lettres et tours** : outil « borne de handicap » posé par B (T2) ; signalé aussi par A (T2, sur B) et D (T2, sur A et E) ; adopté par A, B, C, D et E (T3).
- **Retenue** : OUI.
- **Pourquoi elle survit** : c'est le seul défaut que les cinq modèles reconnaissent comme structurel (si la référence qui définit « ordinaire » est aussi un bras au même budget, elle perd par définition) ; les réponses divergent seulement sur le remède (panel disjoint chez B et C, budget court b₀ = B/64 ou B/20 chez D et E), ce qui se tranche par calcul. Soutien : argument et calcul (borne P(référence atteint une idée certifiée) ≲ m·p), aucune mesure.
- **Épreuve décisive la moins chère** : calcul à coût nul, puis petite simulation sur processeur, de la borne de handicap et de la puissance de certification pour les triplets (nombre de tirages K, rapport de budgets m = B/b₀, seuil τ) envisagés ; vérifier qu'au moins un réglage laisse un bras hors système au-dessus du plancher mesurable. Coût : moins d'une journée de travail, moins de 10 € de processeur. Date au plus tard : 4 décembre 2026.
- **Témoin faux connu** : « un bras identique à la politique de référence, rejoué au même budget que la référence, peut obtenir un taux de succès étroit-profond supérieur à la marge du duel ».

### P2 — Étroitesse certifiée par borne supérieure unilatérale (zéro ou peu d'occurrences) sur des tirages de référence disjoints, étiquette binaire censurée, coût de sensibilité écrit dans la définition
- **Lettres et tours** : D (T1, Clopper-Pearson) ; A et C (T1, disjonction des exécutions) ; critiques de A, B, D, E (T2) sur la saturation et les ex æquo ; adoptée par A (T3, T2), B (T3, I1), C (T3), D (T3, M₀ = 4 000), E (T3, K_ref = 800).
- **Retenue** : OUI.
- **Pourquoi elle survit** : toutes les critiques ont tué les estimateurs ponctuels (p̂ = 0 donne une rareté infinie) et les corrélations de rang sur valeurs censurées ; la certification par borne, avec exécutions disjointes, reste debout, à condition d'écrire son prix (une classe n'est certifiée avec probabilité 0,8 que si elle est environ 37 fois plus rare que le seuil affiché, calcul de B, T3). Soutien : calcul (identités binomiales), argument (régression vers la moyenne si les exécutions ne sont pas disjointes).
- **Épreuve décisive la moins chère** : simulation sur processeur d'un panel de classes à probabilités d'atteinte connues ; on compare l'étiquette « étroite » obtenue avec des exécutions disjointes et avec les exécutions mêmes qui ont produit les idées (contrôle « étroitesse par sélection » de B, T2) ; on mesure l'excès de classes déclarées étroites dans le second cas et la sensibilité réelle au voisinage du seuil. Coût : quelques heures de processeur, moins de 10 €. Date au plus tard : 8 décembre 2026.
- **Témoin faux connu** : « estimer la rareté sur les mêmes exécutions qui ont produit les idées retenues ne fabrique aucune rareté apparente ».

### P3 — Nomination scellée en nombre fixe, choisie avant l'ouverture du coffre, plus un bras « volume » (spam) à nombre de candidats apparié
- **Lettres et tours** : critique de A (T2) sur B (nombre de candidats confondant, 1 − 0,95⁵⁰ ≈ 0,92) ; B, C, D (T2) sur E (maximum sur tout le vivier) ; adoptée par B (T3, k fixe), E (T3, nomination unique), D (T1 et T3), C (T3, atteinte et livraison séparées).
- **Retenue** : OUI.
- **Pourquoi elle survit** : le calcul du maximum bruité (croissance en σ·√(2 ln m)) et le calcul de la fausse réussite par run montrent qu'une quantité « au moins une idée du vivier » récompense le volume et court-circuite le sélecteur ; aucune réponse ne conteste. La variante de C (deux indicateurs, « atteint dans le journal » et « a livré ») est gardée comme secondaire. Soutien : calcul et argument.
- **Épreuve décisive la moins chère** : simulation sur processeur de viviers de tailles différentes dont toutes les idées ont la même profondeur vraie, notés une fois par le maximum sur le vivier, une fois par k nominations scellées ; mesurer la pente du score avec la taille du vivier. Coût : moins de 10 €. Date au plus tard : 8 décembre 2026.
- **Témoin faux connu** : « le maximum de la profondeur estimée sur tout le vivier est invariant au nombre de candidats quand la profondeur vraie est la même ».

### P4 — Profondeur mesurée comme gain d'un résolveur mécanique figé, « avec l'idée » contre « résolveur nu », sur des buts gelés avant toute idée, avec idée vraie mais inerte comme témoin et reproduction sur deux jeux de buts et deux résolveurs
- **Lettres et tours** : A, B, C (T1) ; critiques de B (T2, profondeur fabriquée si les buts viennent de l'idée plantée), D (T2, placebo qui ralentit le résolveur), E (T2, *ex falso* d'une idée fausse) ; corrigée par C (T3, résolveur nu comparateur principal, buts gelés sans connaître les assertions), B (T3, deux références : nu et vrai-inerte), A (T3, E1′ à deux jeux de conséquences et deux solveurs).
- **Retenue** : OUI.
- **Pourquoi elle survit** : c'est la seule définition de la profondeur qui n'appelle aucun juge de langage ; les trois défauts relevés (circularité des buts, placebo nuisible, prémisse fausse) ont chacun un remède concret et vérifiable. Soutien : argument ; aucune mesure.
- **Épreuve décisive la moins chère** : micromonde exhaustif sur processeur ; mesurer pour chaque classe le gain contre résolveur nu, puis la proportion de classes « profondes » selon (buts 1, résolveur 1) qui le restent selon (buts 2, résolveur 2), à rareté fixée ; inclure des identités vraies isolées et des règles fausses (seules les idées validées passent au résolveur). Coût : moins de 200 cœur-heures, moins de 20 €. Date au plus tard : 15 décembre 2026.
- **Témoin faux connu** : « une identité vraie mais sans aucun effet aval a une profondeur strictement positive ».

### P5 — Score de profondeur par compression signé et ramené par observation, sans troncature par régime, constantes figées sur l'apprentissage
- **Lettres et tours** : formule tronquée de D (T1) ; critiques de A, B, C, E (T2) ; corrigée par D (T3, somme signée intensive, veto du pire régime, loi nulle pour les lemmes).
- **Retenue** : OUI (sous sa forme corrigée).
- **Pourquoi elle survit** : l'identité E[(G)₊] = E|G|/2 montre que la version tronquée crédite une loi nulle bruitée et qu'une loi réfutée sur R − 1 régimes peut passer ; la forme signée intensive supprime ces deux défauts sans changer d'instrument. Soutien : calcul.
- **Épreuve décisive la moins chère** : simulation sur processeur de prédicteurs à gain nul et variance croissante, de lois exactes sur un régime et fausses sur les autres, et d'expressions aléatoires de même complexité aux constantes figées sur l'apprentissage ; mesurer le taux de passage du seuil sous les deux formules. Coût : moins de 10 €. Date au plus tard : 11 décembre 2026.
- **Témoin faux connu** : « la somme des gains tronqués à zéro régime par régime a une espérance nulle pour une loi sans gain ».

### P6 — Canonicalisation des idées éprouvée des deux côtés : fausses fusions et fausses scissions, sur des obscurcissements produits par des modèles hors des règles de réécriture
- **Lettres et tours** : A (T2, sur B : « fusionner 98 % des paraphrases » est satisfait par une canonicalisation constante) ; A, B (T2, sur D : porte circulaire) ; D et E (T2, obscurcissements par termes neutres et paraphrases de modèles) ; adoptée par B (T3, E0′), D (T3, porte 5 adversariale), E (T3), A (T3, verrou).
- **Retenue** : OUI.
- **Pourquoi elle survit** : la canonicalisation est en amont de toute mesure d'étroitesse ; son erreur se propage dans les deux sens (fusion : rareté sous-estimée ; scission : rareté gonflée jusqu'au plafond). Accord des cinq modèles. Soutien : argument et calcul (biais de la masse observée).
- **Épreuve décisive la moins chère** : environ 2 000 paires sur processeur et petit modèle : paraphrases mécaniques, obscurcissements engendrés par un modèle tiers, paires proches mais distinctes (une constante ou un terme), lois égales sur la grille et divergentes hors grille ; mesurer les deux taux. Coût : quelques cœur-heures et une à deux heures de processeur graphique, moins de 30 €. Date au plus tard : 11 décembre 2026.
- **Témoin faux connu** : « une canonicalisation qui renvoie la même classe pour toute entrée est fidèle » (elle passe un test à un seul côté et doit mourir au test à deux côtés).

### P7 — Comparaison principale par intersection-union contre chaque ligne de base, différence appariée par monde contre une marge non nulle, effectif dimensionné contre la marge
- **Lettres et tours** : D (T1, intersection-union) ; critiques de C, D, E (T2) sur l'enveloppe par problème de B et E, et de B, D, E (T2) sur la puissance calculée contre zéro chez A, B, D, E ; adoptée par A (T3, 600 mondes), B (T3, environ 270 problèmes), C (T3), D (T3, 220), E (T3, 160 par famille × 2).
- **Retenue** : OUI.
- **Pourquoi elle survit** : deux identités tuent les variantes concurrentes (E[max] ≥ max E, d'où un biais contre le système sous égalité ; taille contre zéro alors que la règle exige de dépasser une marge, d'où une puissance de 0,15 à 0,53 au lieu de 0,8) ; tous les auteurs ont corrigé dans le même sens. Les effectifs révisés divergent (160 à 935 paires) parce qu'ils dépendent du taux de discordance, inconnu : c'est un paramètre à mesurer au pilote, pas un désaccord de principe. Soutien : calcul.
- **Épreuve décisive la moins chère** : simulation sur processeur d'un A/A multi-copies (une copie d'une politique contre l'enveloppe par problème de M copies identiques) et de la puissance conjointe de l'intersection-union au seuil, avec grappes de familles. Coût : moins de 10 €. Date au plus tard : 4 décembre 2026.
- **Témoin faux connu** : « l'enveloppe des lignes de base prise problème par problème est un comparateur sans biais quand le système égale chaque ligne de base » ; et « 150 mondes suffisent pour la règle « intervalle entièrement au-dessus de +5 points » à 15 % contre 5 % ».

### P8 — Bras de divergence triviale (référence déplacée) et chasseur d'étroitesse comme contrôles négatifs obligatoires
- **Lettres et tours** : posés par B (T2) ; « différent mais pas meilleur » chez A (T2) ; adoptés par A (T3, E3b et E4′), B (T3), C (T3), D (T3, Exp. II), E (T3, E1 et E5).
- **Retenue** : OUI.
- **Pourquoi elle survit** : un A/A ne voit pas le handicap (les deux copies sont handicapées pareil) et un bras « bizarre » scripté obtient zéro par construction ; seuls ces deux chercheurs testent si le critère récompense la distance à la référence ou la rareté seule. Nuance de C (T3), que je retiens : si le bras divergent trouve des classes réellement utiles, ce n'est pas une fausse alerte, mais l'attribution à la collaboration exige alors de le battre aussi. Soutien : argument.
- **Épreuve décisive la moins chère** : le chasseur d'étroitesse (petit modèle qui rejette les candidats probables sous la référence, sans accès à la profondeur) tourne sur 30 à 50 mondes plantés sans idée étroite-profonde mais avec des leurres rares et inertes ; mesurer son taux de succès étroit-profond. Coût : quelques heures de processeur graphique, moins de 50 €. Date au plus tard : 18 décembre 2026.
- **Témoin faux connu** : « un harnais auquel on retire la condition de profondeur distingue une découverte d'une simple chasse à la rareté » (variante délibérément cassée, qui doit se faire battre par le chasseur).

### P9 — Attribution par plusieurs témoins distincts : absence de critique à budget réalloué, message neutre du même problème, critique permutée réservée à la mesure d'une nuisance, sélecteurs comparés sur les mêmes viviers gelés, équipe hétérogène contre chaque famille homogène
- **Lettres et tours** : A, B, C, D, E (T1, sous des formes partielles) ; critiques de C, D, E (T2) sur le placebo hors sujet et sur la réallocation qui mesure une politique budgétaire ; synthèse chez C (T3) et A (T3, E5′), B (T3, E5′), E (T3, E6 sur lot indépendant).
- **Retenue** : OUI.
- **Pourquoi elle survit** : chaque témoin isolé a été réfuté par un calcul simple (une critique permutée nuisible fait gagner le système sans que la critique aide ; la réallocation mesure une politique de budget) ; l'ensemble des témoins, chacun avec sa marge, ne l'a pas été. J'ajoute l'exigence de E (T3) : lot d'instances indépendant du duel principal. Soutien : argument et calcul.
- **Épreuve décisive la moins chère** : avant toute attribution, test de neutralité du placebo sur un petit modèle, 30 à 40 problèmes : critique permutée contre message neutre du même problème contre aucune critique, à budget égal. Coût : moins de 50 €. Date au plus tard : 18 décembre 2026.
- **Témoin faux connu** : « un message délibérément contradictoire et hors sujet injecté dans le contexte est sans effet sur la sortie » (placebo truqué, construit pour nuire).

### P10 — Intégrité de la mesure sous retour séparée de l'utilité du retour : trois jeux (renvoyé, scellé, vierge), différence d'écarts entre bras avec et sans retour, bras de fuite délibérée comme contrôle de sensibilité ; étroitesse jamais renvoyée
- **Lettres et tours** : A (T1, F0 à F3), B, C, D, E (T1) ; critiques de C (T2, la différence pertinente est entre les écarts), E (T2, écart d'optimisme confondu avec corruption) et A, D (T2) ; adoptée par A (T3, E6′ avec couplage comme facteur), B (T3, E6′ avant le duel), C (T3), D (T3, Exp. V avec épreuve du « Thresholdout »), E (T3, E4 avec panel secret).
- **Retenue** : OUI.
- **Pourquoi elle survit** : les critiques ont montré qu'un écart apprentissage-test peut naître de la seule sélection (calcul de E, T2) et qu'un témoin de fuite muet rend l'essai aveugle ; la forme corrigée répond aux deux. Le point de A (T3), que la conclusion ne vaut qu'au niveau de couplage public-privé testé, reste une limite. L'interdiction de renvoyer l'étroitesse fait consensus (argument : elle transforme la référence en adversaire). Soutien : argument et calcul.
- **Épreuve décisive la moins chère** : pilote sur petit modèle, 30 à 60 problèmes, trois bras (retour, silence, fuite délibérée du jeu scellé) ; mesurer d'abord que le bras de fuite dépasse la tolérance. Coût : 50 à 150 € de processeur graphique. Date au plus tard : 22 décembre 2026.
- **Témoin faux connu** : « renvoyer au générateur le score calculé sur le jeu scellé ne gonfle pas ce score par rapport à un jeu vierge ».

### P11 — Plafond de fausses alertes fixé par la prévalence visée (identité de Bayes) et contrôlé strate par strate de leurres, jamais en moyenne
- **Lettres et tours** : C (T1, environ 0,0009) ; A (T2, valeur prédictive ≈ 0,14 chez B) ; D et E (T2, strates agrégées) ; adoptée par A (T3), B (T3, I2, environ 0,002 et 1 500 négatifs par strate), C (T3), E (T3, 2 000 négatifs stratifiés).
- **Retenue** : OUI.
- **Pourquoi elle survit** : l'identité de Bayes est incontestée et refaite par trois modèles ; l'agrégation sur strates masque un défaut concentré sur la strate « rare et stérile » (calcul de E, T2). Réserve non résolue, signalée par B (T3) : la prévalence est inconnue ; on prend le plafond correspondant au bas d'un intervalle préenregistré. Soutien : calcul.
- **Épreuve décisive la moins chère** : calcul du plafond et de l'effectif à zéro alerte, puis audit sur processeur d'environ 1 500 à 2 000 leurres par strate (rare-stérile, commun-utile, commun-stérile) dans des mondes plantés. Coût : quelques centaines de cœur-heures, moins de 50 €. Date au plus tard : 15 décembre 2026.
- **Témoin faux connu** : « à prévalence 0,01, un détecteur de sensibilité 0,8 et de 0,05 de fausses alertes produit une majorité de vraies découvertes ».

### P12 — Aucun juge de langage dans la quantité primaire ; s'il faut un juge hors du primaire, plan factoriel vérité × style avec audit des positifs et des négatifs, et correction par inférence assistée seulement face à un oracle externe objectif
- **Lettres et tours** : B, C (T1, juge hors du primaire) ; D (T1, Rogan-Gladen), E (T1, inférence assistée par prédiction) ; critiques de A, C, D (T2) sur l'audit par verdict, le seul audit des négatifs et les experts humains partageant les biais ; adoptée par A (T3, exclusion totale), B (T3), C (T3), D (T3, Exp. VI factorielle), E (T3, module optionnel E2b).
- **Retenue** : OUI.
- **Pourquoi elle survit** : à faible prévalence, la correction devient non bornée quand sensibilité et fausses alertes se rapprochent ; et un audit par experts ne borne pas un biais commun (D, T2). Aucune réponse ne défend un juge dans le primaire. Soutien : calcul et argument.
- **Épreuve décisive la moins chère** : seulement si un domaine semi-formel est ouvert ; sinon sans objet. Plan 2 × 2 réduit : 100 vrais et 100 faux certifiés par oracle exact, chacun réécrit dans deux styles, avec étiquettes de provenance inversées en clair comme témoin positif. Coût : moins de 100 €. Date au plus tard : 31 décembre 2026.
- **Témoin faux connu** : « un juge de langage dont on affiche en clair une provenance inversée garde exactement les mêmes verdicts » (témoin positif construit, qui doit être détecté).

### P13 — Contrôle positif d'instrument sur un micromonde à deux lois utiles dont une seule est signalée au constructeur, plus une assertion vraie rare sur une observable inutilisée, et écritures différentes d'une même assertion passées par la même interface
- **Lettres et tours** : A (T2, sur C : seconde règle profonde à créditer) ; B (T3, E1′ avec loi non documentée et leurres d'une autre grammaire) ; C (T3, « première expérience à financer ») ; A (T3, E1′ sans étiquette du concepteur).
- **Retenue** : OUI.
- **Pourquoi elle survit** : elle répond à la critique la plus répétée du tour 2 (le contrôle positif sur monde planté est vrai par construction) sans la nier : B et C acceptent qu'un tel essai ne valide qu'une implémentation, et l'ajout d'une loi non documentée rend l'échec possible. Soutien : argument.
- **Épreuve décisive la moins chère** : micromonde exhaustif sur processeur, recensement des classes, probabilités d'accès et gains contre résolveur nu ; classifieur limité au gabarit pour vérifier que les leurres ne se reconnaissent pas à leur forme. Coût : moins de 20 €. Date au plus tard : 11 décembre 2026.
- **Témoin faux connu** : « un détecteur qui ne crédite que la loi documentée comme plantée est un détecteur valide de lois profondes ».

### P14 — Dépendance de l'étroitesse à la référence et au codage mesurée comme désaccord sur l'étiquette au seuil, contre un plancher test-retest, avec traductions qui ne conservent pas la taille et le modèle de référence inclus
- **Lettres et tours** : A, B, D, E (T1, sous forme de corrélations de rang) ; critiques de A, B, C, E (T2 : censure, troncature de type Berkson, isomorphisme conservant la taille vrai par construction, modèle absent de la phase processeur) ; corrigée par A (T3, E2′), B (T3, E2′, « expérience à faire en premier »), D (T3, Exp. I avec κ et 40 heures de processeur graphique), E (T3, E2a).
- **Retenue** : OUI.
- **Pourquoi elle survit** : c'est l'expérience la moins chère qui puisse réfuter le cadrage lui-même (« recherche ordinaire » sans référence nommée), et pas seulement un instrument ; la forme au seuil évite les ex æquo censurés. Soutien : argument ; l'effet attendu reste conjecture (B donne 0,5 de confiance à une issue défavorable au cadrage).
- **Épreuve décisive la moins chère** : ensemble de classes fixé hors des tirages des références ; même nombre de tirages par référence ; désaccord sur le drapeau « étroite certifiée » entre références et entre deux encodages, comparé au désaccord « même référence, deux graines ». Coût : 40 à 50 heures de processeur graphique, 100 à 250 €. Date au plus tard : 22 décembre 2026.
- **Témoin faux connu** : « un encodage non isomorphe qui casse la structure causale du monde donne les mêmes étiquettes d'étroitesse que l'encodage d'origine » (contrôle négatif de E, T3).

### P15 — Choix des régions testé comme rendement net, avec descripteurs calculés sur l'énoncé public seul et une référence disjointe, coût de prospection imputé, familles neuves, conjonction « gain absolu et interaction », familles de sélection exclues du duel
- **Lettres et tours** : B (T1, E8), C (T1), E (T1, E3), D (T1, Exp. IV) ; critiques de B, D, E (T2 : prédicteur de A nourri par la vérité retenue ; circularité de D ; interaction trompeuse de E) ; corrigée par A (T3, E7′ exploratoire), B (T3, E8′), C (T3), D (T3, sonde disjointe), E (T3, 16 familles, conjonction).
- **Retenue** : OUI, comme expérience exploratoire et non confirmatoire.
- **Pourquoi elle survit** : la question du choix des régions est légitime, mais tous les prédicteurs du tour 1 fuyaient ou étaient circulaires ; la forme corrigée est la seule qui puisse échouer. Je retiens le cadrage de A et C : elle mesure un rendement de recherche, pas l'existence de régions. Soutien : argument ; confiance basse chez tous (0,25 à 0,65).
- **Épreuve décisive la moins chère** : contrôle de code sur processeur : recalculer les descripteurs après permutation ou remplacement par du bruit des données privées (régimes retenus, buts aval) ; ils ne doivent pas changer. Coût : négligeable. Date au plus tard : 8 décembre 2026.
- **Témoin faux connu** : le prédicteur « part d'idées inertes parmi les premiers candidats énumérés » (A, T1), qui dépend de la profondeur privée et doit changer quand on permute les régimes retenus.

---

## Propositions examinées et non retenues

- **N1 — Enveloppe des lignes de base prise problème par problème** (B T1, E T1) : biaisée contre le système sous égalité (E[max] ≥ max E, calcul de C, D, E au T2) ; abandonnée par ses auteurs au T3.
- **N2 — Quantité primaire « maximum de la profondeur sur tout le vivier », agrégée en aire sous la courbe découverte-budget, seuils en écarts-types estimés** (E T1) : récompense le volume, utilise le coffre comme sélecteur gratuit, seuils dépendants des données ; retirée par E au T3.
- **N3 — Score de profondeur par compression tronqué à zéro régime par régime, en nats extensifs** (D T1) : crédite les lois nulles bruitées et croît avec la taille du jeu de test ; remplacé par P5.
- **N4 — Étroitesse comme scalaire comparé par corrélation de rang entre références** (A T1 E2, B T1 E2, E T1) : dominée par les ex æquo censurés et non jugeable en régime rare ; remplacée par P14.
- **N5 — Sélecteurs de régions nourris par la vérité retenue ou par les résidus de la référence qui définit l'étroitesse** (A T1 E7 « déceptivité », D T1 Exp. IV) : fuite de l'oracle privé ou circularité avec la cible ; abandonnés par leurs auteurs.
- **N6 — Critique tirée d'un autre problème comme unique témoin de l'apport de la critique** (A T1 E5, C T1 duel 5) : un placebo nuisible fabrique un gain ; gardé seulement comme mesure de nuisance dans P9.
- **N7 — Identité d'idée par égalité extensionnelle sur tout le domaine, avec toute règle fausse inéligible** (C T1) : écrase les classes éligibles à une seule par monde et rend la profondeur dépendante du représentant (B et D, T2) ; C la remplace au T3 par des assertions partielles à portée déclarée, forme que je ne retiens pas encore comme proposition distincte faute d'épreuve chiffrée.
- **N8 — Égalisation simultanée de toutes les composantes du budget, ou plafond identique d'appels au vérificateur pour tous les bras** (A T1 E4, D T1, E T1 E5) : impossible entre processeur et processeur graphique et bride par construction l'énumérateur ; remplacée par une égalisation en coût matériel ou monétaire (A, B, D, E au T3).
- **N9 — Borne du biais d'un juge par inférence assistée sur un audit d'experts humains** (E T1) : ne borne pas un biais partagé entre juge et experts, et dégrade la variance si la corrélation juge-vérité est faible (D T2) ; restreinte par E au T3, absorbée dans P12.
- **N10 — Arrêt du programme entier sur une absence de significativité dans un petit pilote** (D T1 phase II, E T1 arrêt pour futilité à mi-parcours sans plancher de paires discordantes) : confond « non concluant » et « réfuté » ; corrigé au T3 par un arrêt sur borne supérieure sous la marge et un nombre minimal de paires discordantes.

Total : 15 retenues, 10 non retenues, 25 propositions distinctes.

---

## Réserves du lecteur

- Aucune proposition n'est soutenue par une mesure ; les « VÉRIFIÉ » des pièces sont des calculs faits par les modèles eux-mêmes, non audités par moi au-delà d'une relecture de cohérence (j'ai refait mentalement la valeur prédictive ≈ 0,14 et la puissance 0,29 à 0,53 sans y trouver d'erreur, ce qui ne vaut pas audit).
- Les effectifs du duel principal révisés au T3 vont de 160 à 935 paires par contraste selon les hypothèses de discordance : aucun n'est opposable avant un pilote.
- Le coût dominant, signalé par A et C, est l'étalonnage de l'étroitesse sous modèle (jusqu'à plusieurs dizaines de milliers d'euros illustratifs), non le duel lui-même ; les épreuves ci-dessus ont été choisies pour tomber avant ce poste.

## Références citées dans le dossier, à vérifier (aucune tenue pour vraie)

- Platt (1964), « Strong Inference », *Science*.
- Clopper et Pearson (1934), *Biometrika*.
- Hanley et Lippman-Hand (1983), *JAMA*.
- Berger (1982), test d'intersection-union, *Technometrics*.
- Dwork et al. (2015), « The Reusable Holdout », *Science*.
- Blum et Hardt (2015), « The Ladder », ICML.
- Rogan et Gladen (1978), *American Journal of Epidemiology*.
- Begg et Greenes (1983), biais de vérification, *Biometrics*.
- Angelopoulos et al. (2023), « Prediction-Powered Inference », *Science*.
- Zheng et al. (2023), juge de langage, NeurIPS volet jeux de données.
- Panickssery, Bowman et Feng (2024), auto-préférence des évaluateurs, NeurIPS.
- Golchin et Surdeanu (2024), contamination, ICLR.
- Newcombe (1998), intervalles de différences appariées, *Statistics in Medicine*.
- Fieller (1954), intervalles de rapports, *JRSS B*.
- O'Brien et Fleming (1979), *Biometrics*.
- Rissanen (1978), *Automatica* ; Grünwald (2007), MIT Press.
- Schwartz (1980), test d'identité polynomiale, *J. ACM*.
- Wolpert et Macready (1997), théorèmes « No Free Lunch », *IEEE TEC*.
- Cranmer (2023), PySR ; La Cava et al. (2021), SRBench.
- Lehman et Stanley (2011), recherche de nouveauté, *Evolutionary Computation*.
- Moura et Ullrich (2021), Lean 4, CADE ; The mathlib Community (2020), CPP.

FIN DE LA LISTE
