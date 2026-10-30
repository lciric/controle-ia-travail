# Vérification des corrections N1 à N4 — brouillon 5 du préenregistrement bisociation v2

- Vérificateur : sous-agent neuf (non-auteur du brouillon 4, du brouillon 5, du script de remplacements ni de la contre-lecture 4)
- Modèle : Sonnet 5.5 (claude-sonnet-5-5)
- Heure UTC : 2026-10-30T02:31:27Z
- Pièces lues : contre-lecture 4 (remarques N1 à N7), `appliquer-corrections-cl4-brouillon5-v1.py`, diff brouillon 4 / brouillon 5, brouillon 5 aux passages voisins, sortie `calcul-puissance-bisociation-v2-brouillon4-v2-sortie.txt` (§ 16, § 17, § 7 bis). Rien sous `donnees/`, aucun réseau.
- Contrôle mécanique : j'ai rejoué le script sur le brouillon 4 (empreinte `7e4557b1…`, conforme à celle citée) : le résultat est identique octet pour octet au brouillon 5 (`2dc810ab…`). Le diff ne contient donc que le texte du script ; 27 marqueurs « À REMPLIR — à geler » avant et après (seule l'entrée « Contre-lecture 4 » a perdu son marqueur).

## Verdict

**À reprendre (retouches mineures, aucune ne touche un chiffre calculé ni un seuil)** : R1 à R3 ci-dessous. Le reste est conforme.

## (a) Chaque correction répond-elle au défaut nommé ?

- **N1 — conforme, une précision à ajouter (R3).** Les trois formulations visées sont traitées : « fourchette honnête » devient « fourchette de transfert » (plus aucune occurrence de l'ancienne) ; « presque uniquement » est remplacé par « deux grandeurs, de sensibilité comparable » (réserve 5) ; la confiance 0,90 de P4 est retirée et remplacée par « sans donnée ». La phrase demandée figure dans le résumé (point 4), la réserve 5, la note des confiances et la ligne de gel. Pas de circularité nouvelle : la confiance retirée n'est remplacée par aucune autre.
  - Réserve de forme : les confiances de P1, P2 et P16 (0,90 / 0,85 / 0,90) restent calculées sur une fourchette qui contient P4 (+3 à +8), donc la même absence de donnée ; la note des confiances dit que la fourchette est supposée uniforme, ce qui est honnête, mais ne signale pas cette dépendance. Facultatif.
- **N2 — conforme.** RACINE = 20261101 et RACINE_VALIDATION = 20261102 sont fixées dans le texte, avant toute exécution, sans lien avec un résultat ; rôles et plages d'indices (0 à 299, 300 à 499) sont dits ; ligne d'arrêt ajoutée. Les deux entropies étant distinctes, l'indépendance entre mondes de validation et mondes de décision tient par construction. Rien de choisi après un coup d'œil.
- **N3 — conforme pour V7 ; défaut résiduel pour l'audit (R2).**
  - V7 : le jugement « monde mal réglé » est retiré ; les renvois (J : Table 1 ligne 8 et Table 2 ligne 4 ; A7 : Table 1 ligne 9) correspondent bien aux tables. Mais une phrase du tableau de traitement de la contre-lecture 3 dit encore « V7 : version nouvelle, sans réglage » (brouillon 5, ligne 798, entrée (f)) : **contradiction directe** avec « V7 ne déclenche rien » (ligne 579) (R1). De plus la ligne 579 répète trois fois « aucun paramètre n'est modifié après sa lecture » (lourdeur, sans effet).
  - Audit : les trois constatations (i) à (iii) sont opérationnelles pour (i) et (ii), et le « si et seulement si » ferme la porte à tout autre jugement. Deux réserves : (ii) ne dit pas pour quel X (M_bien, M_moyen, M_inertes) la borne basse à 99 % est lue ; (iii) s'appuie sur « un contraste décisif » que le texte ne énumère pas (la ligne 200 dit seulement « niveau 95 % pour les contrastes décisifs ») et sur « sa demi-largeur » (de quel contraste ?). Cela laisse un reste d'interprétation au sous-agent d'audit, moindre qu'au brouillon 4 mais non nul (R2).
- **N4 — conforme sur le libellé, défaut nouveau sur le contenu de l'audit (R2).** « Avant toute méthode » devient « avant les bras candidats (N et ses ablations ; seuls d1c et c) » aux endroits visés (validation du générateur, ligne d'arrêt) ; l'audit déclenché par V9 est rendu et scellé avant l'invocation unique (ligne 581, ordre du § 9, ligne 606). **Mais** le contenu de l'audit (ligne 645) comprend le recalcul du placebo N_PCg sur les graines de validation et la constatation (ii), qui sont des bras candidats : un audit de V9 « avant l'invocation » ne peut pas les exécuter sans lancer un bras candidat et lire un contraste avant le scellement du manifeste, ce qui heurte « avant les bras candidats » (même phrase de la ligne 572), l'invocation unique et la règle de non-ouverture du fichier de validation avant verdict (CB-17). Le texte doit dire que, pour un audit déclenché par V9 seul, le contenu est limité à la relecture du code et à la relance de d1c et c, (ii) étant non applicable, et que (iii) y porte sur Δ(d1c, c) sur miroirs (sinon aucune des trois constatations ne vise le contraste que V9 mesure : « aucun artefact » serait prononcé par défaut).

## (b) Chiffres, seuils, valeurs recommandées

- Aucun chiffre calculé, seuil ni valeur recommandée n'a changé : tous les remplacements du script sont des phrases ; les seuls nombres nouveaux sont 20261101, 20261102, 0 à 299, 300 à 499 et les chiffres cités ci-dessous.
- Seule suppression chiffrée : la confiance 0,90 de P4 (demandée par N1). L'en-tête du brouillon 5 annonce « seules changent des phrases » ; il vaudrait mieux nommer cette suppression.
- Chiffres nouvellement cités, comparés à la sortie du script § 17 (forme du brouillon 4) : 0,88 / 0,82 à P4 = 3 (ligne N_β0 − b = 3,0 et 6,6 : exact) ; 0,23 à P4 = 2,5 (0,23 / 0,23 : exact) ; 0,00 à P4 = 1,5 (exact) ; 0,78 / 0,75 et 0,63 / 0,60 inchangés (§ 16). Renvois « § 17 », « § 19 », « § 16 » corrects.
- **Précision manquante (R3)** : ces trois valeurs ne valent que si l'avance de N_β0 sur b en « moyen » est au moins de 3 points ; à N_β0 − b = 1, l'adoption est nulle à P4 = 3 (0,00 / 0,00), à 0 elle est nulle jusqu'à P4 = 3,5. Le résumé et la réserve 5 les énoncent sans cette condition ; ils sous-estiment donc la fragilité plutôt qu'ils ne la surestiment, mais le texte doit être exact.
- Information voisine à ne pas confondre : la ligne 222 (inchangée) cite 0,93 / 0,89 à P4 = 3 et 0,25 à 2,5 ; ce sont les valeurs de A7 seule (script § 7 bis), non de l'adoption complète (§ 17). Une demi-phrase le dirait.

## (c) Cohérence de la nouvelle définition de « artefact trouvé » et du retrait de la conséquence de V7

- Tables : la ligne 2 des deux tables (« audit rendu, artefact trouvé » : non concluant, version nouvelle) et la ligne 1 (« déclencheur présent, audit non rendu ») sont cohérentes avec la définition ; « aucun artefact » = tables telles quelles, dit. Pas de ligne manquante.
- Liste d'arrêt : la ligne « J vraie sur les miroirs (V9) : audit R4, non concluant tant que non rendu » s'accorde avec « audit rendu avant l'invocation » (le verdict ne peut pas être antérieur à l'invocation). La ligne d'arrêt des racines est cohérente avec le § 7. L'exception `AccesLatent` reste un arrêt de run (ligne 694) en plus de (i) : pas de conflit.
- Cas où la définition peut mal fonctionner : (a) V9 seul, voir N4 ci-dessus ; (b) gain_contrôle déclenché sur les mondes de décision mais (ii) lu sur les graines de validation : si (ii) est négatif, le verdict suit les lignes 5 (Table 1) et 3 (Table 2), c'est-à-dire la direction prudente (N non adoptée) : acceptable, à mentionner pour que le lecteur de la porte n'y voie pas une divergence.
- Retrait de la conséquence de V7 : cohérent partout, hormis la ligne 798 (R1).

## Retouches demandées

- **R1** — ligne 798, entrée (f) : remplacer « (V7 : version nouvelle, sans réglage) » par « (V7 lu sans effet ; une version nouvelle ne peut venir qu'après le verdict scellé) » ; facultatif : supprimer la répétition de la ligne 579.
- **R2** — audit : (1) dire que, pour un audit déclenché par V9 seul, il se limite à la relecture du code et à la relance de d1c et c sur miroirs, (ii) étant sans objet, et que (iii) y porte sur Δ(d1c, c) ; (2) préciser le X de (ii) et énumérer les « contrastes décisifs » de (iii) ou renvoyer à une liste ; (3) une phrase sur le cas gain_contrôle sur décision / (ii) négatif sur validation.
- **R3** — résumé point 4 et réserve 5 : ajouter « pour une avance de N_β0 d'au moins 3 points en “moyen” » aux valeurs 0,88 / 0,82, 0,23 et 0,00 ; nommer la suppression de la confiance 0,90 de P4 dans l'en-tête ; facultatif : signaler que les confiances de P1, P2, P16 reposent aussi sur la fourchette de P4 sans donnée.

Aucune de ces retouches ne modifie un chiffre calculé, un seuil ou une valeur recommandée ; une relecture limitée aux phrases modifiées suffira.
