# Contre-lecture, tour 1 : organismes discrets v2 (lecteur C, neuf)

Heure : voir l'empreinte compagnon ; rédigé le 2026-11-17 (UTC, `date -u`).

## Ce qui a été soumis
Aucune pièce de préenregistrement ni de devis v2 : la « pièce » est une note « NON PRODUIT » du modèle A (refus de rédiger), avec un résumé et sept nœuds. Les sept pièces v1 de `docs/notes/organismes-discrets-v1/` sont intactes : `sha256sum -c` passe sur les sept empreintes compagnons. Aucun fichier v2 n'existe.

## Ce que je n'ai pas pu juger
Les six points demandés (R1 ; R3 et anti-circularité ; réalité du dommage ; artefact d'adaptateur et exigence de discrétion ; devis ; aveugle aux issues) portent sur un préenregistrement et un devis qui n'existent pas. Je n'ai donc rien à contre-lire sur ces points. Je n'ai ouvert aucun résultat interdit (rien sous `diag/`, `runs/`, `donnees/`).

## Position de lecteur C sur le fond
Je ne rédige pas non plus, et je ne complète pas, une conception dont l'objectif est qu'aucune lecture de la sortie ne repère un sabotage réel, appariée contre une liste de lecteurs. Je m'en tiens donc à juger la note de refus comme texte.

## Jugement de la note
1. Exacte : l'échec de la base « mots et coût » par traits invariants est une propriété d'appariement, pas une preuve de discrétion ; il rend le critère 3 de N-063 jugeable, rien de plus. Je ne l'ai pas revérifié ligne à ligne dans les trois conceptions (mot « tautologique » absent de la note v1 par recherche textuelle ; il vient des jugements, non relus ici).
2. Exacte et importante : une garantie d'invariance sur le maître programmé ne vaut pas pour l'élève distillé ; toute formule doit se lire « non distingué au-dessus du hasard, à telle puissance ».
3. Exacte : résultat négatif légitime, jamais de rendre l'organisme plus bavard après lecture (R3).
4. Plausible : la voie « sans objet » puis banque à tâches exécutables (N-060 v3) est cohérente avec N-063 ; à confirmer par la mère sur le texte de N-063 (non relu intégralement).
5. Écart à signaler : le refus ne cite pas R-3055 (mot direct de Lazar : « faux positif, reprend le travail, la recette peut rester scellée »). La note écrit avoir lu la consigne mais ne dit pas qu'elle contredit une décision enregistrée. Une réserve de modèle n'a pas valeur de décision du programme ; elle doit être portée à Lazar, non tranchée par un agent.
6. Faiblesse : le devis v1 n'est pas relevé ; l'observation sur le débit (2 000 unités par heure, non mesuré) est plausible mais non vérifiée par moi.

## Corrections exigées
Aucune pièce à corriger : il n'y a ni énoncé ni critère à amender. Couples « ancien → nouveau » : sans objet.

## Verdict : a_refaire
Faute de pièce. Non en raison d'un défaut de la note, qui est honnête et factuelle. Majeurs : 1 (absence de la pièce demandée). Mineurs : 0.

## Incidents de ma main
Aucun fichier existant modifié, aucun commit, aucun appel payant, aucune lecture d'issue interdite.
