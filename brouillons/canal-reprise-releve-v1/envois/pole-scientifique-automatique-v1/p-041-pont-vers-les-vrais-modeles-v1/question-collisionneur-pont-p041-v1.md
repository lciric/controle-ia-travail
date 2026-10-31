# Question au collisionneur — P-041 et les vrais modèles : le pont, et l'accès du défenseur aux paramètres de l'attaquant — v1

Écrite par conv-audit (Fable 5.1), 31 octobre 2026, sur le mot direct de Lazar (07:56 heure de Paris) : « repose ma demande et la demande reformulée, fusionnées, au collisionneur ». Niveau méthode : aucune recette d'entrée, aucun contenu du bras d'attaque, aucune donnée de `donnees/`. Les répondants ne tranchent rien ; le directeur décide ensuite. Références non lues sur PDF : SUPPOSÉ.

## Contexte minimal

P-041 est une **arène coévolutive** : une défense (moniteur sur activations) et un générateur d'attaques au niveau des **lois** de probabilité sur des activations synthétiques, à paramètres bornés ; la défense connaît la famille de lois (ses paramètres) et obtient un pire cas certifié sur cette famille. Trois scores sont prévus : (i) familles vues ; (ii) familles tenues à l'écart, conçues par des tiers ; (iii) générateur adaptatif contre la défense figée. Un test de reparamétrisation vérifie que la défense a appris les lois et non leur paramétrisation.

Antériorité vérifiée sur PDF (Bailey, Serrano, Sheshadri et collègues, arXiv 2412.09565v2) : des moniteurs lisant les activations d'un modèle de langage ouvert de 8 milliards de paramètres sont réentraînés à chaque tour sur toutes les attaques passées ; pendant plus de 70 tours, la défense reconnaît tout ce qu'elle a vu et une nouvelle entrée passe à chaque tour (p. 11 à 13) ; les auteurs concluent que cela « ne mène pas facilement à des moniteurs robustes » et ne peuvent exclure une convergence plus tardive (p. 13) ; déjouer la sonde coûte de la capacité au modèle (p. 23). Chez Bailey, l'attaquant fait bouger l'**entrée** d'un vrai réseau (suffixe continu optimisé), l'ensemble des activations atteignables n'a pas de forme connue, et le défenseur ne voit que des instances. Dans P-041, l'attaquant fait bouger des **paramètres** dans une famille bornée connue du défenseur. Constat partagé par les deux lignées du programme : un succès de P-041 ne contredirait pas Bailey et ne dirait rien, à lui seul, des vrais modèles — le certificat vaut sur la famille, et aucun pont n'est mesuré.

## La demande du directeur (mots directs, fusionnés)

1. « Bailey attribue son échec à la malléabilité d'un vrai réseau, qui n'existe pas dans un espace de lois bornées : **comment faire alors ?** »
2. « Le défenseur réel n'a jamais les paramètres de l'attaquant : **et pourquoi ne pas y avoir accès, pour apprendre dessus pour la génération suivante ?** »

## La demande reformulée (par conv-audit, à attaquer aussi)

« Avant de revendiquer quoi que ce soit de P-041 sur les vrais modèles, construire et préenregistrer le **pont** : (1) définir l'ensemble atteignable des activations d'un vrai réseau sous contrainte de comportement et de budget, et sa mesure (rayon, nombre de recouvrement, croissance par tour) ; (2) remplacer l'avantage « le défenseur connaît les paramètres de l'attaquant » par « le défenseur connaît le réseau substitut et borne l'atteignable », avec un rayon certifié par un outil tiers ; (3) dresser l'échelle synthétique → famille ajustée sur activations réelles → vrai modèle à attaquant borné sur l'entrée → vrai modèle à attaquant libre, et mesurer à chaque barreau le résidu hors famille et l'écart entre rayon atteint et rayon certifié ; (4) écrire d'avance le signe et le seuil de ces écarts sous lesquels le transport est tenu, et la transformation qui doit laisser le certificat invariant ; (5) reproduire d'abord la trajectoire de Bailey et mesurer la saturation de l'atteignable, avec une prédiction envoyée aux auteurs. Si la courbe de croissance ne sature pas, P-041 reste un instrument d'étude des conditions de convergence d'une boucle, et c'est cela qu'on revendique. »

## Ce que les répondants doivent produire

**Tour 1 — réponse propre, sans lire le tour 2.** Pour chacune des deux demandes du directeur et pour la demande reformulée :
- (a) ce qu'un expert du domaine ferait ici et que personne ne demande ;
- (b) les données brutes de départ (pas celles déjà analysées) ;
- (c) les méthodes et outils spécifiques, au niveau méthode ;
- (d) ce qui, hors du programme, vérifierait le résultat ;
- (e) la **distinction apprentissage / évaluation** appliquée à la demande 2 : où l'accès du défenseur aux paramètres de l'attaquant est légitime (apprendre, génération après génération), où il invalide la mesure (évaluer), et quelle quantité mesure si apprendre sur des **paramètres** (familles) plutôt que sur des **instances** (ce que fait déjà la défense de Bailey, qui échoue) améliore la généralisation à l'attaquant jamais vu ; quel protocole sépare les deux ;
- (f) pour chaque proposition : le pire cas, la garde qui le ferme, et la mesure, obtenable sans dépense, qui trancherait ;
- (g) une **prédiction signée** : le pont est-il constructible (l'atteignable d'un vrai réseau sature-t-il sous entrée bornée ?), avec la grandeur et le seuil que vous écririez dans un préenregistrement.

**Tour 2 — attaque des pistes déjà proposées** (fichier séparé, servi après le tour 1 : `annexe-tour-2-pistes-p041-v1.md`) : verdict par piste parmi « tenue », « tenue sous condition », « renversée (par quoi) », « aucune ne tient », « indécidable sans la pièce X ».

## Ce que la synthèse doit rendre

Pour chaque demande : les réponses du tour 1 par répondant (convergences, divergences, apports neufs), les verdicts du tour 2 par piste, la ou les mesures décisives avec signe et seuil proposés, et l'ordre des travaux (ce qui se fait sur processeur sans dépense, ce qui exige une carte graphique). Toute affirmation chiffrée renvoie à une pièce de la table des empreintes jointe.
