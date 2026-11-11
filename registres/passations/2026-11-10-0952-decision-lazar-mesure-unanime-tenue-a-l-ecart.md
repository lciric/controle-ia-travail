# Décision de Lazar — mesure unanime lancée avant le scellement de P3-bis, résultats tenus à l'écart (10 novembre 2026, 09:52 UTC)

Session `session_01QPDgKgcLdggoVJfGC5cBw8` (session-dépôt), en autonomie (`…-0927-…`). Numéro de registre à attribuer à la
fusion dans `main`.

- **Mot direct de Lazar, verbatim** : « Recommandation : (a), confiance 0,7. go ».
- **Question** (message de la session, vers 09:47 UTC) : lancer la mesure unanime (a) dès demain, résultats tenus à l'écart,
  ou (b) après le scellement du préenregistrement de P3-bis (visé au plus tard le 18 novembre). Recommandation (a), confiance
  0,7 ; défaut (b). La session avait ensuite indiqué que, l'entretien étant visé le 27 novembre (R-2130 sur `main`), (b)
  suffisait ; Lazar retient (a).
- **Fermeture prévue par l'annexe scellée** `prereg/usages-anterieurs-scores-p3-mesure-unanime-v2.md` (`d5ffe7cb…`) :
  « sauf autre fermeture décidée par Lazar : […] tenir son auteur à l'écart des sorties ». C'est cette fermeture.

## La cloison (conditions de la session mère, messages de 09:46 et 09:49 UTC, acceptées)

Jusqu'au scellement du préenregistrement de T0.7 **et** de celui de P3-bis :
1. aucun résultat de la mesure vers la session mère, ni dans `main`, ni dans un message entre sessions ;
2. aucun résultat dans la synthèse, le document « depuis zéro » ni aucune pièce pour l'entretien ;
3. aucun résultat vers un rédacteur de T0.7 ou de P3-bis ;
4. les agents qui lisent ces scores (la session-dépôt, exécutante ; le lecteur neuf du verdict) sont exclus de tout rôle de
   lecteur ou de verdict sur T0.6 (course 7b), T0.7, P3-bis et la porte de phase 0.

## Mise en œuvre

- La course n'a lieu qu'une fois la fusion de la branche `claude/upbeat-cray-dmauvv` dans `main` faite par la session mère
  (commit final envoyé avant 17:30 UTC), afin qu'aucun fichier de résultat ne soit dans un commit fusionné ; ou, si Lazar
  l'autorise, les sorties sont versées sur une branche de quarantaine dédiée.
- Une seule course, en arrière-plan, délai de deux heures, depuis le dossier de la v15, avec le commit du scellement en
  argument ; verdict par un lecteur neuf ; tout scellé.
- **Lazar lui-même** tranche les nœuds de P3-bis et de T0.7 : la session lui propose de ne lire le contenu du résultat
  qu'après ces deux scellements, pour ne pas devenir un décideur informé ; c'est son choix.

## Instances actives

Aucune. Aucune dépense (processeur seul).
