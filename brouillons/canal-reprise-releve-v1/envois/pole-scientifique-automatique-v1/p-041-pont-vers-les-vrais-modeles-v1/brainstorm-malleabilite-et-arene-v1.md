# Brainstorm — la malléabilité d'un vrai réseau et l'arène P-041 : douze pistes — v1

conv-audit (Fable 5.1), 31 octobre 2026. Mot direct de Lazar (08:00 heure de Paris) : « brainstorme dessus », sur la réponse de session-depot (trois voies et examen final). Ce fichier est un brainstorm : des pistes, chacune avec ce qu'elle changerait, son pire cas, une première mesure sans dépense quand elle existe, et un statut d'antériorité (**SUPPOSÉ** = non vérifié sur PDF, à chercher). Rien n'y est décidé ; rien n'y décrit comment fabriquer une entrée qui trompe un moniteur. Il complète `reponse-pont-p041-vrais-modeles-v1.md` et `comparaison-avec-session-depot-v1.md` et va au tour 2 du collisionneur comme pièce.

## 0. Le cadre en une phrase

Bailey montre qu'un défenseur qui apprend sur des **instances** passées perd contre un attaquant qui bouge l'**entrée** d'un vrai réseau ; P-041 parie qu'un défenseur qui apprend sur les **paramètres** d'une famille bornée gagne sur cette famille. La question n'est pas « bornée ou pas », c'est : **quel objet de la réalité est compact à la résolution du moniteur**, et comment le mesurer.

## 1. Décomposer la malléabilité : trois objets, pas un

« Malléabilité » recouvre trois choses qu'il faut séparer avant de les borner.
- **La fibre** : à une couche donnée, l'ensemble des vecteurs d'activation qui produisent la même sortie (le réseau aval est une application plusieurs-vers-un). C'est une propriété du réseau **aval**.
- **L'atteignable** : la partie de la fibre que l'attaquant peut réellement atteindre en bougeant l'entrée sous un budget. Propriété du réseau **amont** et de la contrainte d'entrée.
- **Le jeu de la contrainte de comportement** (« slack ») : l'attaquant n'exige pas la même sortie, il exige une sortie *assez bonne* pour lui ; plus il accepte de perdre, plus la fibre s'élargit.
Un attaquant comme celui de Bailey exploite les trois ; une famille de lois à paramètres bornés n'en modélise aucune. Conséquence : toute borne doit dire laquelle des trois elle borne. La voie 2 de session-depot borne l'atteignable ; la voie 3 borne le jeu de la contrainte ; personne ne borne la fibre — et c'est pourtant la seule qui soit calculable sans attaquant (voir piste 6).

## 2. Réécrire la famille par le jeu de la contrainte : où les voies 2 et 3 se rejoignent

Plutôt que des paramètres arbitraires, paramétrer la famille par **δ, la perte de comportement que l'attaquant accepte** : la famille F_δ = « les lois d'activations compatibles avec un comportement à δ près de la cible ». Alors « le défenseur connaît les paramètres » devient « le défenseur connaît δ », ce qui est une hypothèse **réaliste** (on sait, ou on décide, combien de capacité un attaquant est prêt à perdre), et le certificat devient : « pour tout attaquant qui garde le comportement à δ près, l'erreur du moniteur est ≤ ε(δ) ». La courbe ε(δ) **est** la courbe détection-coût de la voie 3, mais certifiée par construction de la famille et non lue après coup. Dans l'arène synthétique, δ est un paramètre exact ; sur un vrai modèle, δ se mesure (perte de capacité, comme chez Bailey p. 23). Pire cas : δ mal mesuré sur le réel (une capacité perdue invisible à nos tests). Antériorité : les « certificats relatifs à une contrainte d'utilité » existent-ils pour des moniteurs ? SUPPOSÉ, à chercher. Confiance que la piste tient : 0,6.

## 3. Le jeu et sa valeur : ce que la boucle de Bailey ne calcule pas

La boucle de Bailey est un **double oracle dégénéré** : à chaque tour l'attaquant répond au mieux à la défense courante, et la défense « répond » en réentraînant **un seul** moniteur sur toutes les attaques. En théorie des jeux, la réponse correcte à une suite de meilleures réponses adverses n'est pas un joueur unique entraîné sur tout, c'est un **mélange** (stratégie mixte) sur les moniteurs passés, aux poids d'équilibre ; l'attaquant doit alors tromper le mélange, et la valeur du jeu (taux de détection garanti contre la meilleure réponse à la mixture) est l'objet certifiable. Indice en faveur : Bailey trouve un plateau vers 50 % contre un **ensemble** de sondes (p. 23, chiffre à relire), c'est-à-dire qu'un mélange non optimisé résiste déjà à moitié.
- **Ce que l'arène peut faire dès maintenant, sans dépense** : ajouter un bras « population » (mélange d'équilibre sur les défenses des générations passées, calculé par double oracle avec meilleures réponses exactes dans la famille synthétique) contre le bras « défense unique réentraînée » ; prédiction signée : la valeur du jeu du mélange dépasse celle de la défense unique contre le générateur adaptatif (iii).
- **Test sur le réel presque gratuit, si Bailey a publié ses moniteurs et ses attaques tour par tour** (SUPPOSÉ) : construire la matrice de gains 70 × 70 (moniteur du tour i contre attaque du tour j), résoudre le jeu à somme nulle, lire la valeur ; si le mélange d'équilibre détecte nettement plus que 50 %, il existe une méthode transportable que Bailey n'a pas essayée. Aucune carte graphique : une matrice et un programme linéaire.
- Déploiement réel : tirer le moniteur au hasard par requête selon les poids d'équilibre ; l'attaquant optimise contre une espérance, et la malléabilité doit couvrir tout le support du mélange.
- Antériorités à vérifier : double oracle (McMahan et collègues 2003), apprentissage par réponse stratégique à une population (Lanctot et collègues 2017), défenses randomisées (Pinot et collègues 2020) — tous SUPPOSÉ ; la zone « mélange d'équilibre de moniteurs d'activations contre attaquant adaptatif » est à vérifier avant de la revendiquer (R8). Confiance 0,55 ; c'est la piste la plus neuve.

## 4. La dynamique : compacité, nouveauté résiduelle, équilibre

Trois énoncés qui n'en font qu'un : « l'ensemble d'attaque est compact à la résolution du moniteur » ⇔ « la nouveauté des attaques sature avec les tours » ⇔ « le jeu a un équilibre atteignable par la boucle ». Mesure la moins chère de la saturation : pour chaque tour, projeter l'activation de la nouvelle attaque sur l'espace engendré par les attaques passées et lire la **norme du résidu** ; une suite de résidus qui décroît vers zéro dit un espace d'attaque de dimension finie (la boucle convergera) ; une suite plate dit une dimension effectivement infinie (aucun défenseur à échantillons ne converge, et aucune famille de dimension fixe ne couvre). C'est plus fin que le nombre de recouvrement et cela se calcule sur une trajectoire publiée. La théorie de la coévolution (Rosin et Belew ; Cliff et Miller ; Watson et Pollack — primaires fournies par Lazar) nomme les pathologies à exclure par construction : cycles (exclus chez Bailey par le rappel parfait), désengagement, états stables médiocres ; l'arène doit déclarer son **concept de solution** (ici : maximin sur la famille, ou valeur du jeu mixte), ce que Bailey ne fait pas.

## 5. L'examen final, réécrit : ne pas prédire ce qu'on va perdre

Sous le protocole de Bailey, prédire que la défense sortie de l'arène **ne sera jamais contournée** revient à parier contre 70 tours d'évidence : on perdra, et un résultat négatif attendu n'apprend rien. L'issue primaire de l'examen final doit être le **coût par contournement** : nombre de tours ou de requêtes jusqu'au premier contournement, perte de capacité au premier contournement, et pente de ces deux grandeurs sur les tours. L'hypothèse transportable de P-041 devient : « une défense apprise sur des paramètres élève le coût de chaque contournement par rapport à une défense apprise sur des instances, à contournement égal » — signe prédit, seuil, bras témoins à calcul égal (dont l'entraînement adverse complet, attaquant dans la boucle interne, qui est la vraie base du champ et non le réentraînement sur instances). Si même le coût ne monte pas, l'idée tombe proprement.

## 6. Le spectre de malléabilité par couche : une mesure transportable sans attaquant

La fibre (piste 1) se mesure localement sans aucune attaque : à chaque couche, la jacobienne de la sortie par rapport aux activations donne, au premier ordre, les directions qui ne changent pas le comportement ; la **part de la variance des activations propres qui tombe dans ce noyau** est, couche par couche, la fraction du signal qu'un moniteur lit là où l'attaquant peut bouger sans payer. Cela donne un **spectre** par modèle, comparable entre modèles de tailles différentes : la malléabilité suit-elle une loi d'échelle (les grands modèles, plus redondants, seraient-ils plus malléables) ? Prédiction à signer d'avance. Coût : une passe avant-arrière par exemple ; faisable sur un petit modèle ouvert, lourd mais possible sur un 8B. Pire cas : l'approximation au premier ordre sous-estime une fibre très courbe ; à confronter à l'atteignable mesuré (piste 4) sur un sous-ensemble.

## 7. Le substitut comme paramètre d'ambiguïté

La voie 2 passe par un substitut du modèle réel ; or le transfert d'attaques entre modèles est partiel (SUPPOSÉ, littérature de la transférabilité). Plutôt que d'ignorer l'écart, en faire un paramètre de la famille : l'arène certifie sur un **ensemble d'ambiguïté** de substituts (plusieurs tailles, plusieurs entraînements), à la manière de l'optimisation robuste en distribution ; le certificat vaut pour tout vrai modèle « à distance ≤ r » des substituts, et r se mesure (distance entre les spectres de la piste 6, par exemple). Si r réel dépasse r certifié, on le sait avant de lancer.

## 8. Nommer la menace : boîte blanche ou boîte noire

Bailey est en boîte blanche (gradients sur l'entrée). Un attaquant déployé est souvent en boîte noire (sorties seules, budget de requêtes). La malléabilité **sous boîte noire** est bien plus petite, et des bornes de complexité en requêtes existent (SUPPOSÉ). La classe de P-041 doit dire contre quelle menace elle certifie ; un certificat « boîte noire, budget de q requêtes » est peut-être transportable là où le certificat boîte blanche ne l'est pas. Deux revendications, deux régimes, deux examens.

## 9. Ce qui rendrait tout cela faux

- Le moniteur d'activations est peut-être la mauvaise couche de défense : si l'obfuscation est bon marché et le coût de capacité faible, la robustesse habite au niveau du comportement (voie 3 poussée au bout : un contrôle de sortie, pas un moniteur interne).
- L'arène certifie contre notre imagination : artefacts du générateur (même pathologie que les bancs de graphes simulés dans l'épreuve semi-réelle) ; les familles de tiers n'y remédient qu'en partie.
- Un gain dans l'examen final peut venir du calcul supplémentaire, pas de la méthode : bases à calcul égal obligatoires (piste 5).
- La fibre locale (piste 6) peut être minuscule là où la fibre globale est immense : la mesure rassure à tort.

## 10. Sur la question du directeur : accès aux paramètres pour la génération suivante

Donner au défenseur les paramètres de l'attaquant **pour apprendre** est l'entraînement adverse ; le refuser **pour mesurer** est la règle d'estimation (l'attaque joue en dernier). Ce que la réalité offre, ce n'est pas les paramètres de l'adversaire inconnu, c'est la possibilité de **faire tourner un attaquant** (sa famille d'optimiseurs, son budget) dans la boucle d'apprentissage : c'est la différence entre réentraîner sur les instances passées (Bailey, faible) et l'entraînement minimax avec l'attaquant dans la boucle interne (plus fort en vision — Madry et collègues 2018, SUPPOSÉ). Le risque connu est le **surajustement à l'attaquant d'entraînement** (robuste à un optimiseur, pas aux autres ; SUPPOSÉ : Tramèr et Boneh 2019, déjà cité comme littérature mitigée dans la fusion v3). D'où la mesure : apprendre sur une **famille** d'attaquants (paramètres variés) réduit-il l'écart entre familles tenues à l'écart et adversaire adaptatif, par rapport à un seul attaquant ? C'est l'hypothèse de P-041 écrite en termes du champ ; elle a une antériorité partielle à examiner avant toute revendication.

## 11. Premiers pas sans dépense, dans l'ordre

1. Chercher si Bailey a publié moniteurs et attaques tour par tour ; si oui : résidus de nouveauté (piste 4) et matrice de gains avec valeur du jeu (piste 3) — processeur.
2. Dans l'arène synthétique : bras « mélange d'équilibre » contre « défense unique » (piste 3) ; famille paramétrée par δ (piste 2) — processeur.
3. Spectre de malléabilité sur un petit modèle ouvert (piste 6) — processeur lent ou petite carte graphique : devis.
4. Rédiger la revendication en deux régimes de menace (piste 8) et réécrire l'issue primaire de l'examen final (piste 5).
5. Antériorités des pistes 2, 3, 6 (R8) avant d'en revendiquer une.

## 12. Recommandation (brainstorm, pas décision)

Garder 1 + 2 + examen final de session-depot, en y ajoutant : la famille paramétrée par le jeu de la contrainte (piste 2), le bras « mélange d'équilibre » et le test sur la matrice de gains de Bailey (piste 3), la nouveauté résiduelle comme mesure de compacité (piste 4), le coût par contournement comme issue primaire (piste 5). Confiance que l'ensemble vaut une révision de P-041 v2 : 0,6. Tout cela va au tour 2 du collisionneur comme pistes à attaquer ; la synthèse du tour v5 de l'arène, puis le mot de Lazar.
