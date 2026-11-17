# Contre-lecture, tour 3, du préenregistrement du crible (ii) « proposeurs en série », brouillon 3

- Lecteur : sous-agent neuf, modèle C (n'a écrit aucune pièce lue ; la pièce est du modèle A, les corrections d'un rédacteur d'un autre modèle).
- Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-ii-brouillon3.md` (compagnon vérifié par l'outil de scellement : exact) ; version précédente `crible-ii-brouillon2.md` (compagnon exact) ;
  rapport du tour 2 `contre-lecture-crible-ii-tour2-v1.md` (`ba2ecf66c6994cf8549fd8f12d554e8de82bea59f04bb45b680b1f371c9e6a71`, recalculée, égale).
- Heure de rédaction : 2026-11-17T02:03:37Z (`date -u`).
- Rien d'autre lu ; aucune branche, aucun appel, aucune machine, aucune dépense, aucune clé.

## 1. Verdict : scellable (aucune correction exigée)

## 2. Les trois corrections du tour 2 sont-elles appliquées fidèlement ? Oui
Les quatre couples (m1.1, m1.2, m2.1, m3.1) ont été extraits par programme du rapport du tour 2 ; chaque « ancien » figure une seule fois dans le
brouillon 2 ; appliqués au brouillon 2 dans une copie de travail, puis la copie comparée au brouillon 3. Le seul reste de différence est : le titre
(« brouillon 3 »), une entrée d'en-tête neuve (brouillon 3), le « Statut », la ligne du validateur, la section « Contre-lecture » (entrée
« Contre-lecture 2 » ajoutée) et la ligne vide rétablie avant l'annexe A. Le différentiel direct `diff` entre les brouillons 2 et 3 ne montre rien d'autre ;
il est identique en substance au différentiel scellé `diff-crible-ii-b2-vers-b3.txt` (empreintes de la pièce, du différentiel et du programme d'application vérifiées).

## 3. Passages relus et vérifications
- Validateur `controle_ia.prereg.problemes` rejoué sur le brouillon 3 : liste vide, comme la pièce le dit.
- m1 : « Statut » et « Prédiction » disent désormais « sans donnée … des composantes comptées, hors la classe des conditionnelles » : cohérent avec x = 0 sur 14 lu ; plus de contradiction.
- m2 : la parenthèse se rapporte au seul repli sur la longueur la plus proche ; le cas « aucun donneur » est compté à part, ce que la table des cas (ligne « aucun donneur ne convient ») dit déjà ; cohérent avec la définition de la réserve (écart de longueur).
- m3 : l'en-tête brouillon 2 nomme maintenant ses changements ; l'entrée brouillon 3 est exacte (elle liste ce que le différentiel montre).
- « Contre-lecture 2 » : empreintes citées exactes ; décompte (aucune majeure, 3 mineures, 4 couples) conforme au rapport ; traitement point par point fidèle, remarques facultatives et points pour la mère correctement renvoyés hors pièce.
- L'entrée « Contre-lecture 1 » garde, comme historique, la phrase « non corrigé, signalé » : elle est datée et suivie par l'entrée 2 qui la règle ; pas de contradiction.
- Devis, annexe A, conception, prédictions, R1, R3, R4 : octets inchangés depuis le brouillon 2 (déjà vérifiés au tour 2) ; enveloppe 1 251,67 sur 1 275 inchangée.
- Les occurrences de noms de modèles relevées dans la pièce sont des clés de configuration et des étiquettes de lignes de GO, hors identifiant de modèle nouveau, comme jugé aux tours précédents.

## 4. Corrections exigées : aucune.

## 5. Remarque facultative
L'en-tête cite une tête de dépôt `1df4ae9f` ; la tête actuelle est `b4ecab17` : sans importance, c'était la tête au moment de la correction.

## 6. Pour la session mère
Inchangé depuis le tour 2 : nœud de faisabilité (taille servie, option a recommandée), écarts à la note (proposeur, rang 1 commun, ordre non joué),
marge de 23,33 USD de l'enveloppe, puissance basse (« non tranché » probable), solde de crédits à vérifier. La pièce peut être scellée telle quelle comme brouillon ; elle reste non en vigueur jusqu'à décision.

## 7. Incidents de ma main
1. Trois exécutions ont imprimé trop de texte (appel du validateur avec un texte au lieu d'un chemin, puis différentiel complet) : sans effet, aucun fichier modifié hors ce rapport.
