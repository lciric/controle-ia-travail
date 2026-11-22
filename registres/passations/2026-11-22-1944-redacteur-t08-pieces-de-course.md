# Passation — rédacteur du texte de la base boîte noire (T0.8) : pièces de la course

- **Session** : `session_013QMayo5SNVbiUW6hGnPrCo` (modèle B), fille de la session mère `session_013QMayjbmQUdDuDs2S3i3XD`. Suit la passation `2026-11-22-1857-redacteur-t08-texte-complet.md`, qui reste.
- **Branche** : `prep/t08-texte-complet-fable-v1`, tête `fe2f6185371d637bf3b961f9745125f5d0b4fb9c` avant cette passation ; demande de fusion n° 61, en brouillon.

## Fait

- **Texte** : brouillon 14 (`e81e4ddb2ea88adb377219780ae18614d1e17502dff4ccd761ddeeef2228937b`), vérifié « conforme : scellable après les marqueurs ». Rien n'y a changé depuis.
- **Pièces de la course**, sous `docs/procedures/t08-course-v1/` : ordre de course, consigne du lecteur, consigne du juge de verdict. Brouillons 1 contre-lus (« après corrections », `3ea629e8…`) ; brouillons 2, les 17 constats appliqués, vérifiés « conformes » (`4440161d…`) ; brouillons 3, à vérifier : ordre `6922ada9651f4bbcb9d9347dff105c003c136c702a63b79cc3e5a4f7ae6d01e8`, lecteur `6a39a5d9aa1dc0e289494c0fea0828fdc8216f866f0358b08446605881c89cdf`, juge `a99adb596f94a82c534d204325f7884180bca6c446dad0d089192c663711cb9c`.
- **Brouillons 3, deux causes** : la décision de la session mère sur le relais du verdict (R-5017 de `registres/decisions.md` : elle ne reçoit que chemins et empreintes, une session relais neuve sans part au saboteur soumet le verdict à Lazar, branches de la lecture et du verdict interdites aux sessions du saboteur) ; le contrôle du commit que porte le manifeste de la course (la tête de la course est un enfant du commit du code).
- **Consigne de la chaîne de lancement**, version 3 (`6f52c4db8d1a3fd0a530cbbfc3cc59e0b0d47f745191d8316aa5d0560e94346e`), envoyée au développeur `session_013QMaykVEGYEXUpWBeemUjb` : plafond restant, accord prolongé, échantillon de l'audit extrait par programme, sortie de la lecture sans nombre de résultat, commit local de la course et ses six conditions.
- **Faits relevés dans le code**, écrits dans les pièces : la garde de calcul contrôle l'échéance de chaque identifiant d'accord de la commande sans suivre les prolongations (`GO-2026-11-10-12` refusé dès le 1er décembre, `GO-2026-11-22-79` admis jusqu'au 31) ; la lecture désigne l'échantillon de l'audit sans en extraire les textes ; le manifeste exige un arbre propre et le texte scellé sous la racine ; la garde de l'instance du code aligné est resserrée au `resume.json` de 7b (`01fe0ea57`, décision de la mère), ce qui est la lettre du texte.

## Reste

1. Vérification courte des brouillons 3 par le contre-lecteur `session_013QMaynYTnoP7ytoW2UMpRB` (demandée).
2. Scellement du texte : jouer `brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v3.py` (à blanc, puis réel) dès les quatre valeurs de la session mère — commit du code aligné contre-lu, chemins de sa pièce d'empreintes et de son rapport de contre-lecture, ligne d'engagement, entropie ; ligne des gardes : R-5014. Commande : journal du brouillon 14 et passation précédente.
3. Brouillon des commandes de l'ordre de course et de la consigne du lecteur, dès le rendu du développeur de la chaîne (commandes de chaque étape, empreintes de la chaîne, chemin du fichier d'échantillon, commande du contrôle du commit) ; puis sa vérification.

## Réserves

- L'ordre de course n'est pas exécutable ; aucune machine ne se crée sur ces brouillons. Chemin critique pour une création le 26 novembre : la chaîne de lancement.
- Les faits relevés dans la garde de calcul, la lecture et le manifeste n'ont pas été relus par le contre-lecteur, qui ne lit pas le code : ils sont à confirmer par les essais du développeur de la chaîne.
- Point ouvert pour Lazar, non tranché, déjà transmis : le mot « diffus » à la porte G1 contre la définition retenue par ce texte.
- Suite de tests complète non jouable dans ce conteneur (bibliothèques lourdes absentes) ; aucun fichier de `src/` ni de `tests/` touché.

## Prochaine action

Attendre l'un des trois retours ci-dessus ; à la reprise, relire cette passation, puis `docs/procedures/t08-course-v1/journal-pieces-de-course-t08-brouillon3-v1.md`.

## Instances actives

Aucune : cette session n'a créé aucune machine et n'a rien dépensé.
