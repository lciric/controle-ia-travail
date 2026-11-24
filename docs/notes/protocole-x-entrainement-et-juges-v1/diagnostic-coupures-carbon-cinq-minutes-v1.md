# Diagnostic court — appels à Carbon coupés après cinq minutes de silence (24 novembre 2026)

Écrit le 2026-11-24T12:07:02Z (`date -u`) par la session du protocole X, à la demande de la mère. Classe C. Sans code. Aucune dépense pour ce diagnostic.

## Ce qui est établi

Quatre envois à des modèles de Google sont partis de ce conteneur aujourd'hui.

| Envoi | Départ | Issue | Durée avant l'issue | Source |
|---|---|---|---|---|
| Carbon, appel direct de la demande 1 | 11:17:24Z | premier octet à 11:20:47Z, fin normale à 11:29:17Z | 203 s avant le premier octet ; 713 s en tout | `journal-appel-carbon-demande-1-v1.txt` |
| Carbon, appel direct de la demande 2 | 11:21:25Z | connexion fermée sans aucune réponse à 11:26:26Z | 301 s | `journal-appel-carbon-demande-2-v1.txt` |
| Carbon, conception du collisionneur | 11:55:46Z | connexion fermée sans aucune réponse à 12:00:46Z | 300 s | journal de la course |
| Neon, conception du collisionneur | 12:05:21Z | refus HTTP 503, « high demand », à 12:05:22Z | 1 s | journal de la course |

- Les deux coupures de Carbon sont de même forme : une fermeture propre, sans réponse ni code d'erreur, à cinq minutes de silence, à une seconde près.
- La limite ne porte pas sur la durée totale : l'envoi qui a passé a duré 713 secondes, dont 510 après son premier octet.
- Les deux programmes demandent déjà un flux continu avec les pensées, pour garder la connexion vivante. Le premier octet n'arrive qu'avec la première pensée ; chez Carbon au niveau de réflexion « high », elle peut tarder plus de cinq minutes.
- Le refus de Neon est d'une autre nature : un refus avant traitement, que le service dit passager.
- La notice du mandataire réseau de ce conteneur ne documente aucune limite de silence. Elle dit que les lignes qui nomment l'hôte et la raison d'une connexion abandonnée ne s'affichent que pour une commande au premier plan ; mes envois tournaient en fond.
- Sur les journaux de courses voisines présents sur cette branche, six cellules de Carbon réussies ont duré de 337 à 500 secondes en tout. Ces journaux ne notent pas l'heure du premier octet.

## L'hypothèse

Une limite de 300 secondes de silence avant le premier octet de la réponse, quelque part sur le chemin. Deux lieux possibles : le mandataire de sortie du conteneur, ou le service de Google lui-même. Je ne sais pas lequel. Le hasard est peu plausible : deux coupures à 300 et 301 secondes.

Ce que l'hypothèse prédit : tout appel à Carbon dont la première pensée tarde plus de cinq minutes est coupé, depuis ce chemin ; un appel dont elle arrive plus tôt passe, quelle que soit sa durée. Aujourd'hui : un passé sur trois.

## Les tests qui trancheraient

1. **Sans dépense de modèle** : une requête, par le même chemin, vers un point d'accès que le programme maîtrise et qui ne répond qu'après 310 secondes. Coupée à 300 : la limite est sur le chemin du conteneur. Passée : elle est chez Google. Deux services publics de réponse retardée ont été essayés ; aucun n'accepte un tel délai. Il faut un serveur du programme déjà allumé.
2. **Au prix d'un appel à Carbon** (2,8 USD au pire) : le même appel depuis une machine hors du conteneur. S'il passe avec un premier octet après 300 secondes, la limite est sur le chemin du conteneur.
3. **Sans dépense, pour la suite** : faire noter l'heure du premier octet au journal de chaque appel. Un seul succès avec un premier octet après 300 secondes, depuis un conteneur, réfuterait l'hypothèse.

Un essai au premier plan, qui ferait afficher les lignes du mandataire, n'est pas sûr tel quel : une commande au premier plan est arrêtée au bout de dix minutes, et l'appel qui a passé en a duré près de douze.

## Ce que cela change dès maintenant

- Une relance de Carbon depuis ce conteneur a de l'ordre d'une chance sur deux d'être coupée de nouveau, chaque coupure étant comptée au pire. Cela vaut pour l'appel de la demande 2, suspendu au mot de Lazar.
- Parades possibles, toutes à décider, aucune écrite ici : lancer les appels à Carbon d'un autre chemin ; passer par l'interface de lot, que le programme refuse aujourd'hui à Carbon parce que sa provision de réflexion dépasse la limite de l'appel non diffusé ; baisser le niveau de réflexion de Carbon ; ou accepter le taux de perte et le chiffrer au devis.
