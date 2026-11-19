# Différences entre le brouillon 12 et le brouillon 13 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 12 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon12.md`, empreinte `467c2e8ba627554e454bba09dd640c3d10c5f25ed73cd7d25fcf7e491013bd5a`.
- Sources, empreintes vérifiées : contre-lecture du brouillon 12 (Opus 5.5, contre-lecteur neuf), `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon12-v1.md`, `715cef034f1a50f604bda49b204b9117502fc228b4b111f465097a17904e2f0d`, lue en entier ; contre-lecture du code de la lecture version 3 et second essai d'intégration, `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-code-lecture-v3-integration-v1.md`, `c07e50324925f0d4e47ec09e6342737b9de477f0bd8a83e7df69a44cef210228`, lue en entier ; notice du code de la passe version 4, `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v4.md`, `66f1e6c11aaed7f66d9a50191c4a066ed2a427107678180858d5626a764006db`, section « Différences qui restent » lue pour contrôle. **Ni le code ni ses essais n'ont été lus.**
- Brouillon 13 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 2026-11-19T04:24Z et 2026-11-19T04:26Z (`date -u` ; mêmes heures que la ligne de date du brouillon 13), par programme, à partir du brouillon 12 : remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie que les chaînes de la procédure de remplissage restent uniques, qu'il reste exactement deux marqueurs, que la ligne 76 (F-3) est identique à celle du brouillon 12, que le bloc « Noms et champs, liste fermée » est identique au caractère près, et qu'aucune phrase « comparée à rien » ne reste.
- Ni hypothèse, ni prédiction, ni métrique, ni seuil, ni niveau, ni état, ni ligne de la table des issues ne changent.

## A. Contre-lecture du brouillon 12

| n° | objet | état | où, dans le brouillon 13 |
|---|---|---|---|
| M-1 (a) | égalité exacte des deux chemins, jouée avant le cas sain ; bornes calculées par l'essai | mot pour mot | essai A0, chapeau |
| M-1 (b) | règle d'échec | mot pour mot | essai A0, rejeu unique |
| M-1 (c) | retour à l'option sans scores par jeton | mot pour mot | bloc de décision des scores par jeton, passage (b-5) |
| m-1 | générateur nommé | mot pour mot (porté par M-1 (a)) | essai A0, chapeau |
| m-2 | permutation de l'essai d'alignement fixée | mot pour mot | essai A0, (iii) |
| m-3 | blocs d'un jeu | mot pour mot | « Métrique », intervalle |
| m-4 | limite déclarée de l'essai | mot pour mot | essai A0, dernière ligne |
| m-5 | citations de (b-5) avec leurs marques de gras | mot pour mot (deux remplacements) | passage (b-5) |
| m-6 | du côté exposé, nul n'ouvre les fichiers de scores | mot pour mot | « Passe », « Qui fait quoi » |
| O-1 | nom de la course de la trace égal à `run_id` de l'extrait des états | **ajout à la demande de la conductrice** | à l'ouverture de la lecture, où les deux pièces sont lues ensemble (la commande de réception seule ne lit pas l'extrait) : plan, point 3 ; garde r4 (la phrase « type seulement » devient : la garde de réception contrôle le type, la lecture exige l'égalité) ; D-12 (la phrase « comparée à rien » devient : comparée au seul nom de la course de la trace) ; liste d'arrêt, ligne 3 |

## B. Phrases du second essai d'intégration et de la contre-lecture du code de la lecture version 3

| n° | objet | état | où, dans le brouillon 13 |
|---|---|---|---|
| B-1 | essai de la chaîne, tâche réduite à une classe : première phrase du contre-lecteur (décision de la conductrice) | portée, **une adaptation** | essai A0, (i). La fin « l'essai n'échoue que par (a) ou (b) » devient « l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) », pour ne pas contredire M-1 (b) ; un renvoi « elle reste un bloc : « Métrique », « Intervalle » » la relie à m-3, sans redire la règle |
| B-2 | réception seule : quatre lignes de registre, avec la raison ; pas d'entropie ni de contrôle de F-3 | portées mot pour mot | condition de départ D-11. Cohérence vérifiée : le texte de N-1 nommait trois lignes, la quatrième (`CODE-PASSE-IIB`) s'y ajoute ; les conditions d'ordre (ligne de livraison strictement après celle du code de la passe) la rendaient déjà nécessaire ; « avant toute réception » ne porte que sur le code de la lecture, sans contradiction |
| B-3 | finitude du vecteur et du biais : portée exacte, contrôlée avant toute autre condition | mot pour mot | règle mécanique des sondes lues |
| B-4 | « une direction de plus » : définition | mot pour mot, **précédée de « Pour la tromperie et les enjeux élevés : »** | règle mécanique, (iv). La phrase parle d'un préfixe de nom, que seules ces deux sondes ont ; pour la dissimulation, la règle déjà écrite (800 entrées de famille « plancher », toutes couches comptées) reste |
| B-5 | clé et nom de la sonde décisive | mot pour mot | règle mécanique, avant la recherche des directions |
| B-6 | ligne d'accord : première cellule = l'identifiant seul | mot pour mot, **aux deux endroits** | D-4 (lecture) et garde P0 (passe) |

Les quatre précisions de la notice de la passe version 4 (portée de la finitude, direction de plus, rang et nom de la sonde décisive, ligne d'accord) sont reprises et remplacées par B-3 à B-6 : contrôlé à la lecture de sa section « Différences qui restent ».

## C. Autres changements (demandés)

- En-tête : titre et statut « brouillon 13 » ; ligne de date ; contre-lecteur du brouillon 12 ; les deux rapports et la notice version 4 cités avec leur empreinte ; le code de la passe est dit en version 4, celui de la lecture en version 3.
- Section « Contre-lecture » : la phrase de renvoi de l'entrée « 3 septies » devient « cette différence est contre-lue par l'entrée 3 octies » ; entrée « Contre-lecture 3 octies » ajoutée (empreintes du brouillon 12 et du rapport).

## D. À réaligner dans le code (tiré des rapports seuls : le rédacteur n'a lu aucun code)

**Code de la lecture**
1. Essai de la chaîne : l'égalité des deux chemins, jouée avant le cas sain, avec des bornes calculées par l'essai lui-même à partir de `rang` et `jetons_notes` ; inégalité = échec sans rejeu ; la sortie écrit la sonde et le nombre d'actions inégales, jamais un score.
2. Essai de la chaîne : une tâche réduite à une classe n'est plus une cause d'échec ; elle est nommée dans la sortie (remarque N-1 du contre-lecteur du code ; essai du code à inverser).
3. Essai d'alignement : `permutation(n)` sur les actions de `H` d'au moins un jeton noté, rangées dans l'ordre des clés ; générateur `numpy.random.default_rng(graine)`.
4. Finitude : contrôler toutes les candidates avant toute autre condition, que la sonde soit conforme ou non (remarque N-3).
5. Ouverture de la lecture : refuser si le nom de la course de la trace diffère de `run_id` de l'extrait des états (neuf).
6. Réception seule : exiger les quatre lignes (déjà fait d'après le rapport) ; ne pas contrôler la cellule de F-3 (déjà conforme).

**Code de la passe**
1. Sonde décisive : exiger que son nom ne paraisse qu'une fois dans l'index (remarque N-4).
2. Du côté exposé, aucun programme autre que le code de la passe n'ouvre les fichiers 1, 2 et 4 : règle pour l'exécutante, à porter à la notice de la passe.

## E. Marqueurs restants

Deux, et deux seulement : F-3 (entropie racine des graines, ligne 76, inchangée au caractère près) et l'entrée « Contre-lecture 4 (finale, texte rempli) ». Sortie exacte du validateur sur le brouillon 13 : `['section vide ou à remplir : Contre-lecture']`.
