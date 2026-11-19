# Différences entre le brouillon 9 et le brouillon 10 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 9 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, empreinte `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d`.
- Contre-lecture du brouillon 9 (Opus 5.5, contre-lecteur neuf) : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon9-v1.md`, empreinte `906bec723f0528c6055be8fbb2d88cc44d2be10a09aa9353d492ab4be7c55654` (vérifiée ; lue en entier).
- Brouillon 10 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon10.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 2026-11-19T02:12Z et 2026-11-19T02:13Z (`date -u` ; mêmes heures que la ligne de date du brouillon 10), par programme, à partir du brouillon 9 : onze remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie que les chaînes de la procédure de remplissage restent uniques, qu'il reste exactement deux marqueurs et que la ligne 76 (F-3) est identique à celle du brouillon 9. Ni le code ni ses essais n'ont été lus.

## Une ligne par remplacement

| n° | objet | état | où, dans le brouillon 10 |
|---|---|---|---|
| R-1 (bloquante) | garde des chemins lus de la passe : le refus des chemins portant « iib » ne vaut que hors de la liste fermée | appliqué mot pour mot | garde P8 (ligne 296) |
| R-2 | attribution de la réserve de 4 000 000 octets | appliqué mot pour mot | décision de taille (ligne 210) |
| R-3 | nom des tableaux d'activité brute : valeur du champ `rang` de l'index | appliqué mot pour mot | « Noms et champs », (4) (ligne 264) |
| R-4 (mineure) | « la lecture exige les cinq autres clés » | appliqué mot pour mot | conditions d'ordre du registre (ligne 305) |
| cinquième (développeur de la passe, transmis par la conductrice) | les deux libellés de la liste `agregations`, écrits exactement : `"maximum (production)"` (case 0) et `"moyenne (bras de diagnostic, jamais en production)"` (case 1) ; la lecture refuse sinon | appliqué ; la ligne 261 a été relue en entier : seule la phrase « `agregations`, JSON : les deux libellés des cases. » y change | « Noms et champs », (1) (ligne 261). Les deux libellés sont ceux que la conductrice transmet du code de la passe : le rédacteur ne les a pas vérifiés dans le code, qu'il ne lit pas |

Refusés ou adaptés : aucun.

## Changements hors remplacements (demandés)

- Ligne 1 : titre « brouillon 10 » ; ligne 3 : statut « brouillon 10 » (le numéro seul).
- Ligne 5 : « contre-lecteur du brouillon 9 : Opus 5.5 ».
- Ligne 7 : ligne de date.
- Ligne 24 : après la citation de la notice du code de la passe (version 1, celle que le rédacteur a lue), la demi-phrase « le code de la passe et sa notice sont passés depuis en version 2, sans changement des noms ni des formats de la livraison ; c'est la ligne de registre du code qui fait foi sur la version » (fait transmis par la conductrice).
- Section « Contre-lecture » : entrée « Contre-lecture 3 quinquies » (empreintes du brouillon 9 et du rapport), ajoutée avant l'entrée 4.

Rien d'autre ne change.

## Marqueurs restants

Deux, et deux seulement : ligne 76 (F-3, entropie racine des graines, inchangée au caractère près) et ligne 429 (entrée « Contre-lecture 4 (finale, texte rempli) », décalée d'une ligne par l'entrée ajoutée : la procédure de remplissage du contre-lecteur dit 428). Sortie exacte du validateur sur le brouillon 10 : `['section vide ou à remplir : Contre-lecture']`.
