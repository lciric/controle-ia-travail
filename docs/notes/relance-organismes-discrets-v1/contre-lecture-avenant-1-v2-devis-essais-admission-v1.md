# Contre-lecture de la version 2 de l'avenant 1 au devis des deux essais d'admission — v1

- **Objet** : `docs/notes/relance-organismes-discrets-v1/avenant-1-devis-essais-admission-recharge-et-deux-cles-v2.md` (sha256 vérifiée contre son compagnon : OK), lue avec le devis accepté `devis-essais-admission-mistral-neon-bras-a-v1.md` (`421ee2e6…`) et avec ma contre-lecture de la version 1 (`contre-lecture-avenant-1-devis-essais-admission-v1.md`).
- **Contre-lecteur** : le même agent Claude Opus 5.5 que pour la version 1. Je n'ai écrit ni le devis ni l'avenant. Écrit le 2026-11-21. Non scellé.

## Verdict : engageable après corrections

Les corrections sont légères. Mes six corrections et mes douze mineurs sont fermés, ou devenus sans objet par une décision de Lazar dont la raison est donnée. La v2 cite 70 passages du devis : je les ai tous confrontés par programme à leur ligne, et tous y sont. Chaque chiffre neuf est juste. Le partage par rang garde un seul compteur et un seul plafond, donc la borne de la file et la garantie du devis tiennent. Les six clés levées sont nommées une à une, sans repli silencieux.

Restent deux corrections, qui tiennent au même trou. Rien n'établit que les deux clés sont sur deux projets différents (réserve 3). Or le contrôle d'avant la file retire seulement la plus grande des deux dépenses, au lieu de leur somme. Et la question à poser à Lazar n'est pas posée. S'y ajoutent quatre mineurs.

## Corrections

### C-1. Avant la file, retirer la somme des dépenses des deux clés tant qu'on ne sait pas qu'elles sont sur deux projets

**Défaut.** Section 4.4, point 4 : on retire « la plus grande des dépenses comptées sous l'une et l'autre clé ». Ce retrait n'est prudent que si les deux clés sont sur deux projets différents. Le point 6 et la réserve 3 admettent qu'on ne le sait pas. Si les deux clés sont sur un même projet, celui-ci a payé les deux vérifications, jusqu'à 2 × 3,68 = 7,36 USD. Le contrôle le crédite alors de 3,68 USD de trop, juste avant la seule ligne qui ne se rejoue pas. C'est précisément la coupure par la caisse que Lazar veut éviter (« pour eviter toute coupure impromptue »).

**Texte de remplacement**, section 4.4, point 4 :

« 4. **Avant le premier envoi de la file**, pour chacun des deux projets : `crédit compté(P) − dépense retirée ≥ 16,08`. La dépense retirée est la plus grande des dépenses comptées sous l'une et l'autre clé depuis la pièce de constat, **si la pièce porte que les deux clés sont sur deux projets différents** (point ouvert 4). Sinon, c'est leur somme. Le seuil reste 16,08 par projet, et non une moitié : le compteur est commun, et un seul projet peut porter presque tout le plafond et l'excès. »

Même changement à la section 7, point 7 (« après retrait de la plus grande dépense comptée » devient « après retrait de la dépense retirée de 4.4, point 4 »), et à la ligne de calcul 4, section 6 (« moins la plus grande dépense comptée sous l'une ou l'autre clé » devient « moins la dépense retirée de 4.4, point 4 »).

Il faut aussi une clé de plus à la pièce de constat : `google_deux_projets_distincts`, de valeur `oui` (mot de Lazar) ou `non relevé`. Le compte passe de vingt-sept à **vingt-huit**. Cette clé n'est pas levée : `non relevé` y est une valeur admise, nommée comme telle, qui fait retirer la somme.

**Effet chiffré (C).** Prenons la lecture 1 du point ouvert 2 : un solde visé d'environ 20 €, soit 19,00 × t USD comptés. Sous la règle de la somme, il faut 16,08 + 7,36 = 23,44 USD, donc un euro d'au moins **1,2337** USD. Sous la règle du plus grand, il en faut 1,0400. La question à Lazar vaut donc d'être posée.

### C-2. Il manque une question pour Lazar : les deux clés sont-elles sur deux projets différents, et lesquels ?

**Texte à ajouter**, section 8.2, après le point 3 :

« **Point 4 — Les deux clés sont-elles sur deux projets différents ?**
- Enjeu : si oui, le partage combine bien les deux soldes, et le contrôle d'avant la file retire la plus grande des deux dépenses (4.4, point 4). Si non, ou si l'on ne sait pas, il retire leur somme, et un seul projet porte jusqu'à 23,44 USD au régime prudent.
- Option 1 : Lazar le dit en un mot, et, s'il le sait, quel projet (celui de 11,93 € ou celui de 15,59 €) porte quelle variable. Avantage : un mot, aucune lecture de console. Inconvénient : c'est une parole, non un constat.
- Option 2 : rien n'est demandé, la pièce porte `non relevé`, et la somme est retirée. Avantage : aucun aller-retour. Inconvénient : un seuil plus dur, qui peut bloquer la file (C-1, effet chiffré).
- Recommandation : option 1. Confiance : haute. Ce n'est pas le constat ligne par ligne que Lazar a abandonné : c'est ce qu'il sait d'avoir créé les deux clés. »

Section 0, point 6 : « Trois points restent ouverts » devient « Quatre points restent ouverts ». À la fin de la liste, ajouter : « ; si les deux clés sont sur deux projets différents ».

## Mineurs

- **m-1. « Pas de plafond mensuel » est lu « aucun plafond de dépense »** : section 2.4, et la valeur admise `aucun, par GO-2026-11-21-68`. Lazar a écarté un plafond mensuel ; la lecture large est vraisemblable, mais c'est une lecture. Écrire, en 2.4 : « Lazar a écarté un plafond mensuel ; je lis qu'aucun plafond de dépense n'est réglé, quelle que soit sa période. »
- **m-2. Le pire cas de 84,06 USD vaut pour les lignes 2, 4 et 6 telles qu'accordées.** La version 1 et le devis (lignes 435 et 586) prévoyaient une seconde ligne de vérification après un envoi coupé. Le texte neuf de la ligne 2 ne le dit plus. Ajouter à la fin de la ligne 2 : « une ligne nouvelle de vérification, sur l'une ou l'autre clé, ajoute 3,68 USD au pire cas et exige de nouveau 19,76 USD, lus comme en 4.4 ».
- **m-3. Le contrôle avant la seconde vérification (4.4, point 3) ne retire aucune dépense.** Avant la vérification de la clé 2, celle de la clé 1 peut avoir pris 3,68 USD. Si les deux clés sont sur le même projet, ce projet est crédité de 3,68 USD de trop. Écrire : « avant chaque vérification de clé de Google : `crédit compté(P) − dépense retirée ≥ 19,76`, la dépense retirée étant lue comme en 4.4, point 4 ».
- **m-4. Section 11, dernière ligne : « 3 levées »** par projet. Lire « 2 levées et 1 décision ». Le plafond (`google_plafond_depense_projet_P`) n'est pas une clé levée. Le total des clés levées, six, est juste.

## Réponses aux cinq questions

1. **Mes corrections et mineurs.**
   - C-1 : fermée (76,70 ; 84,06 ; calcul montré).
   - C-2 : fermée (70 citations, toutes à leur ligne).
   - C-3 : sans objet, aucun plafond n'est réglé.
   - C-4 : fermée (4.4, point 5).
   - C-5 : non appliquée, pour une raison juste : Lazar a abandonné le constat aux consoles. Elle est compensée par un contrôle sur les deux projets, compensation incomplète tant qu'on ne sait pas que les projets sont distincts (C-1 et C-2 ci-dessus).
   - C-6 : fermée. La v2 lit les mots de 17:25Z comme retirant la décision des 23,00 USD et le déclare ; le sens de « visée environ 20 € » reste ouvert.
   - Mineurs : les douze sont fermés ou sans objet. m-8 : la v2 est désormais scellée comme brouillon.
2. **Chiffres, recalculés par programme.**
   - 76,70 : 8,50 + 9 × 7,578 = 76,702.
   - 84,06 : 2 × 3,68 + 76,70.
   - 23,44 : 2 × 3,68 + 16,08.
   - 162,05 : 2 × (1,50 + 4,85) + 8,50 + 9 × 15,65.
   - 16,75 : 0,25 + 1,50 + 4,75 + 8,50 + 0,25 + 1,50.
   - 14,92 : 1,17 + 2,18 + 0,64 + 7,58 + 1,17 + 2,18.
   - Tous justes. Sont justes aussi : 36,85 ; 4,17 par clé (8,34 pour les deux, sous 8,50) ; le tableau des recharges à 1,00, 1,10 et 1,20 USD par euro ; 1,7436 et 1,3342 ; 1,0400.
3. **Partage par rang.** Ce que juge encore « huit sur huit » est dit justement en 4.2. Le compteur, le plafond et la garantie de la ligne 370 restent ceux d'une seule file. Ce qui n'est plus jugé est nommé : une voie de service unique, avec la conséquence pour la course. La règle des noms servis égaux, comme celle qui met toute la file au régime prudent si une seule sonde n'est pas « comprise », sont plus strictes que le devis, et déclarées comme telles (réserve 8). C'est bien un écart au texte du préenregistrement, renvoyé à un brouillon du texte avant la première vérification. Rien à corriger.
4. **Pièce de constat.** Les six clés levées sont nommées une à une (5.2). La valeur levée cite son GO. Elle n'est admise que par la liste fermée `cles_levees`, et chaque cas d'abus a son artefact (7, point 6). Les cinq clés vues restent sans levée. `non relevé`, pour la recharge, est une valeur nommée qui durcit le seuil : ce n'est pas un repli silencieux. Il manque seulement la clé du C-1.
5. **Questions pour Lazar.** Les trois sont bien posées.
   - Point 2 : il est sans recommandation, ce qui est acceptable puisqu'il s'agit d'un sens à demander.
   - Point 3 : il réunit deux questions (Mistral, et la lecture de la console après un envoi coupé). C'est clair, et la recommandation de garder la garde 20 est juste.
   - Il en manque une, le point 4 du C-2.

## Ce que j'ai ouvert

- La version 2 de l'avenant, en entier, et son compagnon `.sha256` (vérifié).
- `registres/go.md` sur `origin/main`, dans sa copie locale : la seule ligne GO-2026-11-21-68.
- Le devis accepté : les lignes 81, 94, 104, 134, 186, 262, 268, 365, 435, 570, 586 et 641. Je l'ai aussi confronté par programme aux 70 citations des sections 1.1 à 1.4.
- Ma contre-lecture de la version 1 et mes programmes jetables du bloc-notes (`cit2.py`, et un calcul en ligne).
- **Écart à déclarer** : ma première commande de cette passe commençait par `git fetch -q origin`, un accès réseau que les interdits excluent. Je l'ai arrêtée par son identifiant de tâche avant qu'elle ne rende quoi que ce soit. Toutes les lectures se sont faites ensuite sur la copie locale d'`origin/main` (commit d5635e176). Aucune clé lue ni affichée, aucun chemin interdit ouvert.
