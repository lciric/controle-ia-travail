# Question pour le collisionneur et pour Argon — règle d'arrêt de la lecture d'un proposeur (tour (c), dossier fermé) — v1

Écrite par conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 08:54 UTC. **Mots directs de Lazar (09:52 et
09:53 heure de Paris, ma session)** : « il faut laisser l'organisme fixer lui-même le nombre de tours » ; « ou alors une règle mathématique
de convergence, genre information / entropie de Shannon ou critère de Cauchy : demande au collisionneur et à Argon ». Même forme « arbitre »
que les questions précédentes (trois modèles, trois tours, une tentative par cellule, un refus arrête le tour sans reformulation, R-609) ;
**même garde de sûreté** (R-519, R-339, R-597 sur tout ce qui n'est pas le corpus : rien qui conçoive, détaille ou étende une attaque ; ni
internes des moniteurs, ni carte des hypothèses, ni mode tenu à l'écart, ni banques, ni textes d'actions, ni consignes privées de P3, ni
`donnees/`). **Argon répond à la même question, à part** (commande de session-depot, consigne seule). **Dépense : chez session-depot, sur devis
et sur sa ligne de GO ; conv-audit ne lance rien.** La synthèse est matériau pour la décision de Lazar ; elle ne tranche rien ; tout chiffre
reste exploratoire (R7).

## Contexte (pièces : la note du tour (c) `note-tour-c-outils-clotures-v1.md`, `ad330072…` ; le LISEZMOI v43 ; la décision R-441)

Dans la course d'idéation de l'organisme, chaque **proposeur** (Claude par outils confinés, Argon par protocole) lira un **dossier fermé** :
le texte intégral de ≈ 23 papiers (plusieurs millions de caractères, indexés par titre, résumé, sections et pages), à la demande, page par
page ou section par section, avant d'écrire sa **fiche** (hypothèse, prédiction, antériorités, protocole). Lazar refuse un nombre de tours
fixé par nous : **le proposeur fixe lui-même sa lecture**. Restent des plafonds de sûreté (dollars par session, délai, garde-fou anti-boucle
très haut consigné comme incident). Le juge ne lit pas le dossier : il juge les fiches et leurs citations, vérifiables contre le texte.

## Question

« Comment un proposeur doit-il décider qu'il a assez lu, et comment l'orchestrateur peut-il le mesurer sans le contraindre ? Concevez,
pour un proposeur à budget borné qui lit un dossier fermé indexé, **une règle d'arrêt** et sa mesure :

1. **Règle d'arrêt autonome** (le proposeur décide) : quel signal interne ou externe un proposeur peut suivre — stabilité de sa fiche d'un
   tour à l'autre (critère de Cauchy sur une distance entre versions successives de la fiche : laquelle, mesurée comment ?), gain
   d'information des lectures (entropie de Shannon ou perplexité de la fiche conditionnée à ce qui est lu : définissable et calculable
   par l'orchestrateur à partir des textes seuls ?), épuisement de l'index (parts du dossier citées, sections pertinentes couvertes),
   rendement marginal (nouvelles antériorités ou chiffres par page lue), ou un avertissement de budget. Pour chaque signal : définition
   opérationnelle à partir de ce que l'orchestrateur voit (demandes de lecture, pages servies, versions de la fiche), ce qu'il mesure
   vraiment, ce qu'il rate (un proposeur qui s'arrête trop tôt par confiance ; un qui lit tout par prudence), et comment le proposeur y
   accède sans que cela devienne une consigne de l'orchestrateur.
2. **Convergence mathématique** : existe-t-il un critère de convergence lisible et non manipulable — par exemple, distance entre fiches
   successives sous un seuil ε pendant k tours (Cauchy), ou gain d'information attendu d'une lecture de plus sous un seuil — tel que
   l'arrêt soit **justifiable au préenregistrement** (le proposeur s'arrête quand la règle le dit, et la règle est scellée) plutôt que
   laissé au seul jugement ? Dites ce qu'un tel critère suppose (une distance entre fiches : laquelle ? un modèle de ce qui reste à lire ?),
   ce qu'il coûte (calcul, tours), et s'il vaut mieux comme **mesure consignée** (l'organisme s'arrête de lui-même, on mesure sa
   convergence) que comme **règle** (on l'arrête).
3. **Mesure sans contrainte** : ce que l'orchestrateur consigne au manifeste pour que la lecture de chaque proposeur soit une mesure de
   l'organisme (pages lues, ordre, répétitions, versions de la fiche, distance entre versions, gain d'antériorités par page), et comment
   comparer deux proposeurs (Claude et Argon) sur ces mesures sans en faire un critère du juge (N-053 : jamais de sélection sur le verdict ;
   ici : jamais de sélection sur la lecture).
4. **Plafonds de sûreté** : à quel niveau placer le garde-fou anti-boucle et l'avertissement de budget pour qu'ils ne mordent jamais une
   lecture honnête (ordre de grandeur en pages et en dollars, d'après les tailles de la note du tour (c)), et ce qu'il faut faire d'une fiche
   écrite sous avertissement (marquée, pas rejetée ?).

Pour chaque point : options, avantage, inconvénient, votre recommandation et sa confiance ; les chiffres renvoient à une pièce ; ce qui n'est pas
dans les pièces est marqué SUPPOSÉ. N'inventez aucune mesure des moniteurs ; ne demandez aucune donnée hors des pièces. »

## Critères de lecture de la synthèse (gelés avant lecture)

- Une règle n'est retenue comme « commune » que si deux modèles au moins la donnent **avec la même définition opérationnelle** (même distance,
  même seuil) ; sinon « divergente », options au format décision.
- Un critère qui exige de lire la fiche avec un juge-modèle pendant la lecture est marqué « juge dans la boucle » et n'entre pas comme règle
  (il peut entrer comme mesure).
- Une réponse qui transforme la mesure en consigne au proposeur (« lis au moins N pages ») est marquée « contrainte » et n'entre pas (R-441).
- L'avis d'Argon est lu à côté de la synthèse, non compté dans « commune ».
