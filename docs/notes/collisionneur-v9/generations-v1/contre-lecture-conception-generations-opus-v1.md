# Contre-lecture de la conception des générations du collisionneur jusqu'au plateau, v1

21 novembre 2026, 19:01Z (`date -u`). Contre-lecteur neuf : Claude Opus 5.5 ; je n'ai rien écrit de la pièce ni de son annexe. Aucun appel à un modèle, aucune clé lue, aucune dépense, aucun commit.

## Pièces contre-lues, empreintes vérifiées (`sha256sum -c`, toutes « OK »)

| pièce | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/generations-v1/conception-generations-jusqu-au-plateau-v1.md` | `2f949f2f812b88ab817ded58f2ca9410d19fe737d2e6cb7d7b4af14ca2748c5d` |
| `docs/notes/collisionneur-v9/generations-v1/calculs-devis-et-seuils-generations-v1.py` | `90e75862a547bd9576a2ee7c53f8927155e31f29225e1672423ca0d5a225c3bb` |
| `docs/notes/collisionneur-v9/generations-v1/calculs-devis-et-seuils-generations-v1-sortie.txt` | `625df52a6e94b3608fa072e53230625065391efce26f5c86ab03eeafe20ebf7a` |

Sources ouvertes, empreintes recalculées, égales aux préfixes que la note cite : `collisionneur_v9_v7.py` (`319a7b66b5b9…`), `rapport-developpeur-collisionneur-v9-v7-v1.md` (`c055018231a0…`), `reflexion-relance-collisionneurs-opus-max-v1.md` (`28ce8440d461…`), `docs/decisions/decision-N-058-v1.md` (`854f2724864f…`), `collisionneur_v9_v8.py` (`b85690310f5c…`). Registre des accords : seule la ligne 668 de `registres/go.md` a été ouverte, par son numéro.

Annexe rejouée hors ligne dans mon bloc-notes : sortie identique à l'octet à la sortie scellée.

## Verdict

**À corriger.** Le calcul tient (chaque somme de la section 7 se retrouve dans la sortie rejouée ; tables des espèces, plafonds, prix et chiffres du rapport de la version 7 vérifiés à leurs lignes). Mais quatre points touchent le critère de décision ou sa source : le mot de Lazar est cité sans « par un tiers » et appliqué à un objet qu'il ne visait pas ; la section 5.6 contredit la règle d'arrêt au regard de la décision N-058 ; un plateau peut être prononcé à la génération 2 sur des marques que la lignée se donne elle-même ; la tolérance de 0,90 laisse passer pour « tenue » une expérience changée sur le fond. Le mandat laisse aussi au développeur des choix qu'il lui interdit de faire.

## Points

1. **Mot de Lazar amputé et déplacé (section 5, phrase d'ouverture ; section 10, nœud 2).** La ligne 668 de `registres/go.md` (accord GO-2026-11-21-69) dit : « une propriété fixée d'avance **par un tiers**, vérifiée par programme, avec repli ». Elle se range sous « Programme : noter la priorité vers la conception du produit », avec le premier geste « compter sur des tâches archivées la part qui admet une telle propriété ». Elle porte donc sur les tâches et le produit, pas sur l'arrêt du collisionneur. La note écrit « une propriété fixée d'avance, vérifiée par programme, avec repli nommé » et dit que le critère « a la forme que le mot du 21 novembre demande ». Les seuils sont posés par Fable, qui est l'une des espèces de la course, et la section 9.8 le reconnaît : « Le seul tiers véritable pour les seuils est Lazar ». Pourtant le nœud 2 prend son défaut au bout de 48 heures. Correction : citer la phrase entière, présenter le rapprochement comme une analogie et non comme la réponse à cette demande, et soit retirer le défaut de 48 heures du nœud 2 (les seuils sont gelés sur le mot de Lazar seulement), soit dire en une ligne pourquoi un défaut par silence vaut « fixé par un tiers ».

2. **Conflit avec la décision N-058 (section 5.6 contre sections 5.3 et 6.1).** La section 5.6 range « combien de générations » parmi les choix de composition qui « se jugent sur l'oracle du monde planté [...] et sur le coût mesuré, jamais sur le verdict d'un juge ni sur ces mesures ». La décision N-058 (`docs/decisions/decision-N-058-v1.md`, point 1) dit « seuls ». Or la section 5.3 fait décider par le plateau si la génération 3 part. Aucun juge n'intervient, donc l'interdit de fond de N-058 (sélection d'un agent sur un verdict) n'est pas touché, mais la note se contredit elle-même. Correction : dire que l'arrêt de la chaîne est une règle de conduite, prise sous la ligne accordée, et non un choix de composition ; garder « combien de générations valent leur prix » pour l'épreuve sur le monde planté ; ou retirer « combien de générations » de la liste de la section 5.6. Si l'auteur tient les deux lectures, c'est un nœud pour Lazar.

3. **Plateau à la génération 2 sur des marques que la lignée se donne elle-même (sections 5.1, 5.3, 9.2).** À la génération 2, le premier pas est « déclaré, non vérifié », et le premier choix ne se compare qu'à l'intérieur de la génération 2. Une lignée qui marque TENUE toutes ses entrées à la conception, puis recopie son registre dans sa réponse, passe les quatre conditions. Le verdict « plateau » arrête alors la chaîne à deux générations. C'est justement ce que la section 5.1 dit exclure (« une lignée ne peut donc pas se dire stable par ses seules marques »). L'audit symétrique ne pose qu'une réserve : le verdict tient. Correction, au choix, à soumettre à Lazar : (a) à la génération 2, un verdict « plateau déclaré » qui n'arrête pas la chaîne, la génération 3 restant la seule à prononcer « plateau » ; (b) vérifier le premier pas en cherchant chaque énoncé marqué TENUE dans la réponse de la génération 1, à la même règle de similarité (chercher n'est pas découper : la règle R5 de la section 3.1 n'est pas touchée) ; un énoncé introuvable compte comme modifié.

4. **La tolérance de 0,90 contredit « mot pour mot » et compte comme « tenue » un changement de fond (sections 5.1 et A.2 ; mandat, point 7).** La consigne A.2 demande « mot pour mot », mais le critère accepte une similarité d'au moins 0,90. Essai dans mon bloc-notes, `difflib.SequenceMatcher` sans `autojunk`, sur un énoncé normalisé (forme NFKC, casse repliée, espaces réduits) d'environ 40 mots. Un seuil changé de 0,05 à 0,01 donne 0,995. « ne fait pas mieux » changé en « fait mieux » (H_B inversée) donne 0,984. 200 paires devenues 20 donnent 0,998. Ces trois énoncés modifiés sur le fond comptent comme tenus s'ils sont marqués TENUE. Correction : égalité exacte après une normalisation fixée (forme NFKC, casse, espaces, ponctuation retirée) ; sinon, exiger au moins l'égalité exacte des nombres et des négations en plus du seuil de similarité.

5. **Le mandat interdit d'improviser mais laisse des choix ouverts (section 4.1 ; section 3.3, point 2 ; sections 4.2, 5.4, 6.1 ; mandat, points 4 et 9).**
   - La section 4.1 donne les noms de commandes comme « proposés, à fixer par le mandat », et le mandat ne les fixe pas.
   - Aucune valeur n'est donnée au plafond de chaîne (section 6.1, point 2).
   - Les options de l'arbitre n'ont ni nom ni forme : admettre une mention, écarter une pièce, laisser passer une pièce trop longue. Rien ne dit non plus comment une pièce écartée est servie (un bloc « pièce absente » ?).
   - « C'est la règle de la garde de motifs de la version 9, étendue » est inexact : la garde de `collisionneur_v9_v8.py` (lignes 530 à 577) refuse et rend la décision à l'arbitre, mais n'a aucune option d'admission. L'option est neuve et doit être spécifiée.
   - La méthode de la recopie « à 0,98 près » n'est pas dite : sur des textes de 25 000 à 65 000 caractères, `SequenceMatcher` sans `autojunk` coûte un temps quadratique.
   - Pour une lignée absente, on ne sait pas quel N vaut dans la condition 4.

   Correction : fixer chacun de ces points dans la note, ou les nommer comme difficultés que le développeur rend à la mère.

6. **Faux positifs de la garde d'identité (section 3.3, point 2).** La liste des « noms du catalogue » n'est pas donnée. Or « fable » est un mot français courant, et « opus » et « carbon » sont des mots ordinaires. Une réponse sur le contrôle peut aussi nommer un modèle comme objet d'étude sans que les faits ou la question le nomment. Chaque refus arrête la génération et la renvoie à l'arbitre. Correction : donner la liste fermée des motifs (bornes de mot, casse, formes « Claude Fable », « gemini-4-… », « gpt-… »), et ajouter aux essais un témoin sain qui emploie « fable » comme mot ordinaire et nomme un modèle comme objet.

7. **Plafond de pièce de 65 000 caractères : fondé sur Carbon seul, unité non dite à la source (section 4.2).** La réflexion d'Opus (section 3) écrit « texte 8 400 à 14 401 » pour 19 réponses de Carbon, sans unité. Le contexte (pensées et sortie en jetons) rend « jetons » probable, mais la note l'affirme sans le dire. Par ailleurs, Carbon peut écrire légitimement 16 384 jetons de texte (plafond de 65 536 moins une provision de 49 152), soit 73 728 caractères à 4,5 caractères par jeton (`CAR_SORTIE_MAX`, ligne 342 du script de la version 7), au-delà du plafond de pièce. Le mot SUPPOSÉ est bien posé. Correction : écrire « unité non dite dans la source, lue comme jetons » et noter qu'une réponse de Carbon à son plafond peut dépasser la borne et passer par l'option.

8. **Deux chiffres sans source ou sur une base mêlée (section 7).**
   - « adjudant » est classé parmi les dossiers à cinq espèces, mais le tableau de la section 1 de la réflexion ne donne pas sa composition : non sourcé.
   - L'attendu de « 17 à 21 USD comptés » part des 14,81 USD de ce dossier, comptés sous l'ancienne table, où Argon était compté à 10 et 50 USD par million (« cinq fois trop », réflexion, section 3). Il y ajoute des surcoûts d'état calculés sous la table de la version 7, où Argon est à 4 et 20. Les deux bases ne sont pas comparables.

   Correction : sourcer la composition ou écrire « non vérifié » ; dire que l'attendu mêle deux tables.

9. **« Borne stricte » : à qualifier (verdict ; section 7).** Les 53,76 et 40,66 USD sont sans relance : avec relances, la sortie rejouée donne 113,36 et 83,58. Ils reposent aussi sur deux constantes SUPPOSÉES du script (2 caractères par jeton d'entrée, `CAR_SORTIE_MAX`). Correction : écrire « borne stricte sans relance, sous les hypothèses de projection du script » dans le verdict comme dans le tableau.

10. **Lecture des seuils en nombres, approchée (section 5.2).** « Au plus 6 entrées touchées en tout » suppose que le dénominateur du renouvellement vaut 25. Or il compte aussi les retirées, et la condition 3 a pour dénominateur les entrées actives à l'arrivée. Cette lecture n'est donc exacte qu'à registre de taille constante, sans retrait. Correction : une ligne qui le dit.

11. **Ordre de présentation en carré latin : formule à écrire (section 3.3, point 3 ; mandat, point 3).** L'ordre cyclique place déjà chaque pièce à chaque rang une fois dans une même génération. Le décalage par génération change seulement quel lecteur voit quelle pièce à quel rang. « Décalé de (g − 2) modulo (N − 1) » est ambigu : décale-t-on la liste des autres, ou les indices ? Correction : écrire la formule. Pour le lecteur i, la pièce j (j différent de i), à la génération g, avec d = (j − i) modulo N et s = (g − 2) modulo (N − 1), est au rang ((d − 1 − s) modulo (N − 1)) + 1 parmi les autres. Pour N = 2, le décalage est nul.

12. **Cloisonnement, petit écart de méthode (en-tête, deuxième paragraphe).** La recherche dans le registre des accords a affiché le début des lignes 669 et 672, et la note en donne les sujets (« ligne de calcul du saboteur à budget ; serveur loué de l'organisme »). Rien n'en est tiré, et je n'y vois ni contenu interdit ni chiffre. Correction pour les pièces suivantes : ouvrir la ligne par son numéro, sans recherche ; ces sujets peuvent être retirés de la note.

## Ce qui a été vérifié et tient

- **Sommes de la section 7**, toutes retrouvées : 7,73 + 2,00 + 28,45 + 0,34 = 38,52 ; 7,73 + 5,27 + 28,45 + 1,05 = 42,50 ; à quatre espèces, 31,03 et 33,32. Pour plusieurs dossiers : 509 et 558 USD. Contrôle du calcul : écarts de +1,6 % et +1,5 %.
- **Tables des espèces** : version 7, lignes 232 à 250 ; version 8, lignes 293 à 311. Plafonds, provisions et prix sont égaux ; la version 8 ne change que le réglage de réflexion d'Argon et de Carbon.
- **Constantes du script** : `RATIO_PROJECTION_ENTREE` (2), `TOLERANCE_COMPTE` ((0,01 ; 32)), `CAR_SORTIE_MAX`, `SURCOUT_BLOC` (200), version 7, lignes 336 à 343. Fonctions `garde_entree` et `cout_pire_garde`, lignes 1366 à 1376.
- **Rapport de la version 7, section 3.2** : 28,45 (9,50 + 18,95), 60,81, 10,27, 9,84 et 14,72 ; dossier « mathématiques », 10 cellules à envoyer. La méthode `devis-reprise` est dite pessimiste (lignes 74 et 162).
- **Réflexion d'Opus** : 14,81 USD, environ 10,9 réels, 15 cellules sur 15, 9 sur 15, 14 sur 15 ; « but » et « fusionnée » à quatre espèces (section 7) ; un seul écrivain par journal (section 2).
- **Version 8** : relevé « Argon, 0 jeton de pensées sur 22 réponses » (lignes 286 et 287) ; règles 6, B1 et B4 et ligne « Format » du préambule (lignes 463 à 473) ; limites de 3 500, 3 000 et 3 500 mots (lignes 444 à 446) ; plafond de sortie d'Astra de 8 000 jetons ; options `--ligne-reprise-usd` et `--go-ligne`.
- **Invariants**, en accord avec la décision N-058 sur le fond : aucune lignée éliminée, aucun juge dans l'arrêt, notes de Jev réservées à l'arbitre. La règle R1 est bien appelée pour l'épreuve sur le monde planté, et la règle R7 est tenue (voisins de l'état de l'art marqués « non vérifié », aucun chiffre).
- **Format des nœuds** conforme à `CLAUDE.md`. Les dépenses n'ont pas de défaut.

## Nœuds qui reviennent à Lazar

- Point 1 : comment le mot « fixée par un tiers » s'applique aux seuils du plateau, et s'il faut un défaut au bout de 48 heures.
- Point 3 : un plateau peut-il arrêter la chaîne à la génération 2 alors que le premier pas n'est que déclaré ?
- Point 2, si l'auteur garde « combien de générations » dans le champ de la décision N-058.
