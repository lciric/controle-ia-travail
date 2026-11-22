# Différences — voie (A), brouillons 4 vers brouillons 5 de l'additif et du devis — v1 (pièce de travail)

Écrit le 2026-11-22 vers 18:39Z par le rédacteur, Claude Fable 5.2, sous `mandat-fable-brouillon5-voie-A-v1.md` (`c25267a7d9dd8e6a3d9007b15f8b567a493ba4ac7e0d4edea68a1330178bf473`), branche `claude/iib-executante-v6`. Brouillons 4 intacts : additif `12196e82731d8f60645e5e813b62c3d3ff92e0c7d1b2081e125bd297318d675f`, devis `02730ddd46c95366d76d4184770a95fcb4f7022b4d10db16a895fae673e03983`. Sources : la vérification du brouillon 4 (`note-verification-brouillon4-voie-A-cl2.md`, `b5e73a07a68893784a513932e87ef78b4aa1205123745f31406eeb050ecdf6fc`) ; les décisions de la mère du 22 novembre à 18:21Z (mandat ; registre des nœuds de l'exécutante, `853969df7fe58d56de7d58680ce6b24df6dfb4d95d42fa9c845ef8f3958be178`, étage 2, sous `GO-2026-11-22-106`). Une différence par ligne. Les passages non nommés ici sont ceux du brouillon 4, à l'octet : les brouillons 5 sont fabriqués par programme depuis les brouillons 4, par remplacements exacts (outil de travail du rédacteur, non versé ; la différence se relit par `diff`).

## Décision 1 de la mère (majeur M1) : seuil du deuxième rempart à l'échéance plus 80 minutes
1. **Seuil** : 4 800 secondes, et non plus 600. C'est la fenêtre normale de la minuterie de l'amorce (consignation, 2 400 secondes au plus ; puis destruction, 1 800 secondes au plus), plus 10 minutes. Relu à l'arbre de la voie, dans les deux amorces. Écrit en A3, au § 3.4, au § 4.4 (étape 5), au § 5 ; au devis, § 4 (tableau) et § 6.
2. **Avant le seuil** : code 0, aucun geste par cette règle, même si la machine tourne (A3 ; § 5). « La minuterie a fait défaut » n'est plus dit qu'au seuil de 80 minutes.
3. **Pire si ce rempart joue, rapatriement vérifié** : 57,23 USD, au lieu de 55,62 [M29] (A3 ; § 7, point 8 ; devis, § 4).
4. **Ligne de session** : le rempart demande l'exécutante 3 heures 30 après l'échéance, au lieu de 2 heures 20 ; 12 600 secondes, au lieu de 8 400 ; course de 30 heures créée au plus tard le 2026-11-24 à 14:30Z, au lieu de 15:40Z [M32] (A3 ; § 5 ; § 7, point 10 ; devis, § 6 et § 7, point 11).

## Décision 2 de la mère (majeur M2) : aucune destruction sans rapatriement vérifié
5. **Code 6 retiré.** Le programme ne le rend plus jamais. À sa place, code 7 : deux heures après l'arrêt, sans rapatriement vérifié, machine gardée à l'arrêt, disque gardé, nœud à Lazar. Un numéro neuf, pour qu'un ancien « 6 » ne puisse pas se lire « détruire ».
6. **La règle n'ordonne plus aucune destruction.** La destruction suit le rapatriement vérifié, par le chemin normal, avec `RAPATRIEMENT_VERIFIE=oui` au seul sens « rapatriement vérifié » (A3).
7. **Mot donné d'avance** : il ne couvre plus aucun écart. En A2, l'exception « sauf par le second rempart » est retirée ; « aucune destruction par une session sans rapatriement vérifié » est écrit en A2, au § 4.4 (étape 7), au § 5 et au § 7 (point 3).
8. **Ce que l'exécutante porte au nœud** (A3, code 7) : l'instant de l'arrêt ; ce qui est vérifié et ce qui manque ; le compte de la voie ; l'heure à laquelle ce compte atteint 60 USD.
9. **Le chiffre de 59,30 USD n'est pas porté comme pire : il ne vaut plus.** Il est calculé au seuil de 10 minutes (55 + 0,46 + 3,84). Au seuil de 80 minutes, le même chemin donne 55 + 2,07 + 3,84 = **60,91 USD à 48 heures d'arrêt, au-delà du plafond de 60 USD** [M29, (b bis)]. À 24 heures : 58,99 USD. Le total reste sous 59,76 USD jusqu'à 33,6 heures d'arrêt, sous 60 USD jusqu'à 36,6 heures. Écrit comme réserve nommée : A3 ; § 7, point 9 ; devis, § 0, § 4, § 7 (point 9) et § 8. Aucune des deux décisions n'est changée.
10. **Deux faits ajoutés pour le nœud** (§ 7, point 9) : l'ordre scellé ne nomme aucune commande qui lise le disque d'une machine à l'arrêt ; un redémarrage après l'échéance pousse ce qui attend, puis détruit la machine (lu dans l'amorce).
11. **« Rapatrier ce que porte le disque »** devient « rapatrier ce qui est versé et le vérifier, comme à l'ordre scellé » (A3) : l'ordre scellé ne sait pas lire le disque d'une machine à l'arrêt.

## Mineur m1 : instant d'arrêt placé dans le futur
12. La condition du code 2 gagne `arret_s > maintenant_s`. Huitième cas à [M30] : code 2. Rejoué par la sous-commande, un cas après l'autre : codes 0, 4, 0, 0, 5, 7, 2, 2. Les textes disent « huit cas » (A3 ; § 4.3 ; devis, § 4).

## Mineur m2 : suites de M1
13. Portées d'un même geste : [M29], [M30], [M32], A3, § 5, devis § 4, § 6 et § 7 (point 11), cette note.

## Point 4 du mandat : troisième rempart tenu par la mère
14. Écrit en A3 et au devis, § 4 : dès la création, dans son conteneur, sur la même échéance absolue ; compté dans aucun pire.
15. **Point neuf rendu à la mère** (§ 7, point 12) : l'ordre ne dit ni ce que ce doublement fait, ni quand. Un geste dans les 70 minutes qui suivent l'échéance couperait la consignation de la minuterie de l'amorce (le défaut M1). Une destruction par lui se ferait sans rapatriement vérifié. Au devis, § 4, « destruction par l'identifiant » devient « son geste et son instant restent à écrire par elle ».

## Autres lignes changées
16. **En-têtes** : statut, cause de la version, pièces neuves (la vérification du brouillon 4, le mandat, le registre des nœuds), devis et arithmétique en v5.
17. **Registre** : `registres/go.md` de `main` relu à la tête `e50edee227f8776993f9e24ec246e68b73544591` (`f09e28de6eb833e7c14556be497797495623c6ed2ae8b66a8349e27b6d726311`) ; les lignes -71, -73, -75, -77, -93 et -94 sont inchangées. `GO-2026-11-22-106` est citée : c'est sous elle que la mère a décidé.
18. **Commandes** : `calcul-devis-voie-A-v5.py` partout où une commande est écrite (A3, A4, A5 ; devis, § 3 et § 4).
19. **Premier rempart** (A3) : une phrase de plus, « sa fenêtre normale dure 70 minutes ».
20. **§ 6** : aucun champ rempli ni ajouté ; l'empreinte du devis se relève dans `devis-voie-A-v1-brouillon5.md.sha256`.
21. **Devis, § 8** : la forme du deuxième rempart n'est plus un choix ouvert ; une ligne neuve pour la machine gardée à l'arrêt.

## Programmes
22. **Calcul v5** (`calcul-devis-voie-A-v5.py`, `9e4bb97e61b40ea8dbbb3038e517d4b039ad8687a318ac973fae6f67ee0524f1` ; sortie `ec46db500d9fdf0bca7f49db5f17b5495a3fe9c18f22d46c4fbc0e04ca151d15`) : seules [M29], [M30] et [M32] changent ; les 25 autres lignes sont égales à la sortie v4, à l'octet (comparé). Même sortie avec le Python du système et celui de l'environnement virtuel. Les sous-commandes `rythme-etalonnage`, `echeance` et `garde-de-rythme` rendent les mêmes textes et les mêmes codes qu'en v4 (comparé sur six appels).
23. **Vérification des gardes du lanceur : non rejouée.** Elle joue `go`, `plafond-total`, `variante`, `calendrier` et `depense` sur le code de la voie. Ni le code, ni le registre des lignes citées, ni les configurations ne changent ; rien de ce qu'elle calcule ne dépend du deuxième rempart. Sa sortie v4 (`sortie-verification-gardes-du-lanceur-v4.txt`, `de0426fbd8a11feab2338561e3af0f953fc93c34e317f962f0b334db9fa0c03b`) reste celle que les brouillons 5 citent. Aucun `verifier-gardes-du-lanceur-v5.sh` n'est écrit.

## Ce qui ne change pas
Plafond 60, coupure 55, pire annoncé 59,76 ; pire de la minuterie seule, 56,61 ; réserve de 64,76 ; essai de vitesse et garde de la course ; échéances des machines ; fichier d'entrées ; configuration ; code de la voie ; chiffres attendu et haut du devis ; les trois champs du § 6.

## Points non portés, et pourquoi
- **59,30 USD comme pire du chemin « machine gardée à l'arrêt »** : faux au seuil de 80 minutes (ligne 9). Le programme donne 60,91 USD à 48 heures. À trancher : accepter la réserve, ou borner la durée de l'arrêt.
- **Cas « instant non entier » à [M30]** : la vérification le dit facultatif ; le mandat demande huit cas. Le chemin rend bien le code 2 (rejoué à la main).
- **Geste du troisième rempart** : il appartient à la mère (ligne 15).
- **`<<ENTROPIE_VOIE_A>>`, `<<EMPREINTE_CONFIG_VOIE_A>>`, `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>`** : comme au brouillon 4, ils se remplissent au scellement.
