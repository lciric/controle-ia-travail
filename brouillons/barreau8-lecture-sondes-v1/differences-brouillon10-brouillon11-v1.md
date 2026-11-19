# Différences entre le brouillon 10 et le brouillon 11 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 10 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon10.md`, empreinte `1676078f73bb75a7f0ce68653918fdf58943038d1344179bd5c2c38a78065fc1` (jugé « PRÊT » par son contre-lecteur : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon10-v1.md`, `e4007fb10b7de2866830b0c87bf493295d407cff93d33087924e228c0ea7641c`, empreinte vérifiée, rapport non ouvert par le rédacteur).
- Sources, sous `docs/notes/barreau8-cote-moniteurs-sorties-v1/`, empreintes vérifiées : (1) `contre-lecture-code-lecture-v1-v1.md`, `c5f12da08cce4ad086f8a8a3cbe317da2afe8b4800c8d4174c720d3a7146cb85`, lue en entier ; (2) `notice-passe-recalcul-v3.md`, `3071b909da39e3044a39e8d968f6433e2fc34ea0b57f9605404f618b461165c9`, sections « Livraison » (comparée par programme à celle de la version 1 : identique), « Garde des chemins » et « Phrases proposées pour le texte » ; (3) `contre-lecture-code-passe-v2-v1.md`, `5f8de45cc53952caf4ebc8c6f366f70cb55f9f5544cb308c5b25512676b4e2c2`, remarques 5, 7 et 8 et section « Lacunes du texte ». **Ni le code ni ses essais n'ont été lus.**
- Brouillon 11 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon11.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 2026-11-19T03:04Z et 2026-11-19T03:07Z (`date -u` ; mêmes heures que la ligne de date du brouillon 11), par programme, à partir du brouillon 10 : remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie que les chaînes de la procédure de remplissage restent uniques, qu'il reste exactement deux marqueurs, que la ligne 76 (F-3) est identique à celle du brouillon 10, et que le bloc « Noms et champs, liste fermée » est identique au caractère près.
- Ni hypothèse, ni prédiction, ni métrique, ni seuil, ni niveau, ni ligne de la table des issues ne changent.

## A. Les neuf phrases de la notice du code de la passe (version 3)

| n° | objet | état | où, dans le brouillon 11 |
|---|---|---|---|
| A-1 | le module lancé compté parmi les modules chargés | porté tel quel | garde P0 ; et, pour les deux codes, « Code, registre », contrôle à l'ouverture |
| A-2 | garde des chemins : lectures et écritures séparées | porté, **adapté** | garde P8. La phrase est reprise mot pour mot ; s'y ajoute, d'après la section « Garde des chemins » de la notice, que la liste fermée des lectures comprend le code du paquet, l'environnement Python et la relecture de ce que la passe vient d'écrire — sinon « tout autre fichier du dépôt est refusé » aurait interdit de lire le code |
| A-3 | garde de taille : place libre ; trace et bordereau mesurés avant d'être écrits | porté tel quel | garde P9 |
| A-4 | ordre des lignes par lot de l'extrait du côté exposé | porté tel quel | condition de départ D-13 |
| A-5 | contrôles de plus de la garde du modèle | porté tel quel | garde P2 |
| A-6 | contrôles de plus de la garde des adaptateurs | porté tel quel | garde P4 |
| A-7 | « chaque action compte au moins un identifiant » ; une direction de plancher en trop rend la sonde « sans objet » | porté ; la seconde moitié est fondue dans la règle unique de B-7 | garde P3 (c) ; règle mécanique, condition (iv) |
| A-8 | essai à blanc sans carte avant la passe | porté tel quel | « Passe », « Qui fait quoi », côté exposé |
| A-9 | limite déclarée du contrôle du contexte | porté tel quel | garde P10 |

## B. Les sept phrases de la contre-lecture du code de la lecture

| n° | objet | état | où, dans le brouillon 11 |
|---|---|---|---|
| B-1 (T-1) | la commande de lecture inscrit elle-même la ligne `LECTURE-SONDES-IIB` et refuse si une sortie existe déjà | porté tel quel | plan, point 4, étape (h), avec « les cinq autres lignes sont inscrites par la session mère ». Cohérence vérifiée : la ligne 305 disait déjà « inscrite par la lecture à sa dernière étape » ; aucun passage du texte ne confiait cette inscription à la session mère (les mentions « inscrite par la session mère » portent sur `LIVRAISON-PASSE-IIB` et `ETATS-COURSE-IIB`) |
| B-2 (T-2) | forme de la ligne d'accord | porté tel quel pour la lecture ; **même règle écrite pour la passe** | D-4 ; garde P0 |
| B-3 (T-3) | essai de la chaîne, artefact positif (ii) | **règle inchangée** ; limite déclarée, sortie de diagnostic et réserve en tête écrites | « Critères », essai A0, après « Si A0 échoue… ». Voir § C |
| B-4 (T-4) | la garde de réception n'est pas une lecture au sens de la ligne 13 | porté, **complété** | D-11 et liste d'arrêt, ligne 13. Ajout du rédacteur, sur demande de la conductrice : qui peut jouer la commande de réception seule (la conductrice du côté des moniteurs ou le lecteur des sondes) et quand (dès que la ligne `LIVRAISON-PASSE-IIB` est inscrite) ; et la précision que le repère r8 est le seul nombre qu'elle écrit |
| B-5 (T-5) | empreinte de la pièce de comparaison de l'ordre scellé citée par le mandat du lecteur | porté tel quel | D-6 |
| B-6 (T-6) | « non lisible sur le témoin-jumeau contre l'honnête » : pour quelles sondes | porté, **tranché par le texte** | « Seuil », clause (2). La phrase était encadrée par « Si une sonde porteuse… » et « La sonde reste porteuse », et B8-P2 disait la réserve « écrite en tête du verdict si elle est porteuse » : la réserve en tête vaut pour les seules sondes porteuses (c'est aussi la lecture du code) ; pour une autre sonde, l'échec est écrit dans la sortie, sans réserve en tête. Aucun état ni aucune ligne ne change |
| B-7 (T-7, remarque 8, phrase 7 de la notice) | règle mécanique, condition (iv) : une règle unique pour les deux codes | porté, **complété en une règle unique** | règle mécanique des sondes lues : recherche par nom et ordre des numéros ; dissimulation dans l'ordre de l'index, toutes à la couche 15 ; noms une fois et une seule ; direction de plus = « sans objet » ; vecteur ou biais non fini, et nom des couches 7 ou 23 en double = arrêt de la passe et refus de la lecture (lecture la plus stricte déjà implémentée, celle du code de la passe) |

Remarques 10 et 14 de la même contre-lecture : ce sont T-4 et T-5. Remarques 5, 7 et 8 de la contre-lecture du code de la passe : ce sont A-4, A-5 et A-6, et A-2.

## C. Ce qui est fait de T-3, et pourquoi la règle ne change pas

- **Le fait** : à tailles réduites (20 tâches, 20 directions de plancher), l'artefact positif (ii) a échoué pour deux sondes (aire de l'artefact 0,891 et 0,851 ; quantile 0,95 du plancher 0,653 et 0,729 ; borne basse de D négative). Cause : les étiquettes de l'essai sont portées par des tâches entières ; quand l'activité dépend de la tâche, des directions aléatoires séparent la moitié tirée.
- **Ce que le rédacteur ne peut pas garantir** : qu'aux tailles de la course (64 tâches, 800 directions) l'essai ne peut pas échouer par ce seul tirage. Un ordre de grandeur de sa main, non mesuré, dit l'échec peu probable (pour des scores entièrement fixés par la tâche, l'aire d'une direction aléatoire entre deux moitiés de 32 tâches a un écart-type d'environ 0,07, donc un quantile 0,95 d'environ 0,62, contre une aire d'artefact d'environ 0,92) ; ce n'est pas une garantie.
- **Les deux autres formes envisagées, écartées faute de garantie sans perte** : (a) étiqueter des actions tirées dans chaque tâche (et non des tâches entières) : l'effet de tâche s'annule et le plancher redescend vers 0,5, mais c'est une autre règle de l'essai, que le rédacteur ne sait pas prouver exempte d'un autre biais (rang du pas, longueur du contexte) ; (b) porter le score injecté au-dessus de tous les scores de `H` (séparation parfaite) : l'essai ne pourrait plus échouer par le tirage, mais il n'éprouverait plus qu'un effet énorme, et perdrait ce qui garde la sensibilité de la chaîne.
- **Ce qui est écrit** : la règle de (ii) est inchangée et peut toujours échouer sur une chaîne cassée ; la limite est déclarée ; quand (ii) échoue, la sortie écrit pour chaque sonde l'aire de l'artefact et le quantile 0,95 du plancher sur le jeu de l'essai ; la ligne L5 porte la cause « plancher haut sur le jeu de l'essai » si ce quantile dépasse 0,70 ; tout verdict rendu sous L5 par un échec de (ii) porte une réserve en tête.
- **Décision à porter plus haut** : garder la règle (état du texte), ou passer à la forme (a) avant le scellement.

## D. Autres changements (demandés)

- En-tête : titre et statut « brouillon 11 » ; ligne de date ; contre-lecteur du brouillon 10 ; les trois sources citées avec leur empreinte ; la demi-phrase sur le code de la passe dit « version 3 ».
- Section « Contre-lecture » : la phrase de renvoi de l'entrée « 3 quater » devient « cette différence est contre-lue par l'entrée 3 quinquies » ; entrée « Contre-lecture 3 sexies » ajoutée (empreintes du brouillon 10 et du rapport ; conclusion « PRÊT » sur le brouillon 10).

## E. À réaligner dans le code (tiré des trois sources seules : le rédacteur n'a lu aucun code)

**Code de la lecture**
1. Inscrire elle-même la ligne `LECTURE-SONDES-IIB` et refuser si une sortie existe déjà (T-1 ; remarque 2 du contre-lecteur).
2. Ligne d'accord : une ligne et une seule dont la première cellule est l'identifiant (T-2 ; remarque 4).
3. Mandat du lecteur : il cite l'empreinte de la pièce de comparaison de l'ordre ; exiger l'égalité (T-5 ; remarque 14).
4. Règle mécanique : recherche des directions par nom et ordre des numéros ; vecteur ou biais non fini = refus ; nom des couches 7 ou 23 en double = refus, et non « absente » (T-7 ; remarque 8).
5. Essai de la chaîne : quand (ii) échoue, écrire l'aire de l'artefact et le quantile 0,95 du plancher par sonde ; cause « plancher haut sur le jeu de l'essai » au-delà de 0,70 ; réserve en tête sous L5.
6. Commande de réception seule : elle ne doit exiger que la ligne `LIVRAISON-PASSE-IIB` et ne rien écrire d'autre que « tenue », le refus et sa cause, et le repère r8.

**Code de la passe**
1. Ligne d'accord de la passe : une ligne et une seule dont la première cellule est l'identifiant de l'accord (même règle que la lecture) : à vérifier.
2. Règle mécanique : pour la dissimulation, compter toutes les entrées de famille « plancher », toutes couches, en exiger 800, toutes à la couche 15 ; une direction de plus = « sans objet » ; à vérifier que c'est bien ce que la version 3 fait.
3. Sonde des couches 7 ou 23 non conforme = arrêt (texte depuis le brouillon 9) : à vérifier dans la version 3.

## F. Marqueurs restants

Deux, et deux seulement : F-3 (entropie racine des graines, ligne 76, inchangée au caractère près) et l'entrée « Contre-lecture 4 (finale, texte rempli) ». Sortie exacte du validateur sur le brouillon 11 : `['section vide ou à remplir : Contre-lecture']`.
