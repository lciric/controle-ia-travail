# Contre-lecture du préenregistrement court de la répétition générale du banc fermé — brouillon 1 — v1

- **Pièce relue** : `prereg/repetition-generale-banc-ferme-v1-brouillon1.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `086622ffb4485cc08e6a8514f36f84753e50a382`. Empreinte recalculée : `0934e1c7ce07699b169c4b86c18f42939eae757a4fb9ffed7db54c0ec8584b17`, égale à son `.sha256` compagnon. Pièce de classe A, règle R2.
- **Contre-lectrice** : `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). C'est aussi la contre-lectrice du préenregistrement de la course. Elle n'a écrit aucune des deux pièces.
- **Date** : 21 novembre 2026, vers 19:20 UTC. Refus d'un classifieur : aucun.

## Pièces lues et recalculées

| Pièce | Empreinte |
|---|---|
| le calcul de précision, `calcul-precision-repetition-v1.py`, et sa sortie `.txt` | `afdde32a…` et `99a36624…`, égales |
| la note du mot de Lazar « go reco répétition générale », branche `claude/loving-lamport-7ol5ws` | `72b95dfa…`, égale |
| le brouillon 6 de la course | `b23b4b3b…`, égale ; lu en entier aux vérifications précédentes |
| la pièce de sécurité v10, branche `claude/piece-securite-banc-ferme-v1`, commit `d4ebacd4` | `bf19bdd0…` |

- La pièce de sécurité v10 est **en vérification**. Elle a été lue par recherche sur la voie d'envoi (section 3.5), les gardes 14 à 17, la liste d'arrêt et les points 14 et 25 à 29 de sa liste de vérification. Elle n'est citée ici comme acceptée nulle part.
- La contre-lecture des trois choix a déjà été lue (`bc9ec0fd…`, section 5).
- **Non lus** : aucun texte de mode, ni le coffre, ni l'index v2.
- **Le calcul de précision a été relu** : bissection sur la loi binomiale exacte, sans tirage. Les chiffres cités par le texte (0,145 et 0,071) sont ceux de la sortie.
- **Validateur** : il rend deux problèmes, le marqueur de la section « Seuil » et la section « Contre-lecture » sans empreintes. C'est attendu.

## Points

### Points bloquants

**B1 — La statistique de recouvrement ne peut pas passer l'épreuve que la pièce de sécurité impose à la garde 15.**
La v10 éprouve la garde de fuite de consigne sur deux artefacts. Le premier est un produit qui reprend une phrase de la consigne. Le second est « une charge qui porte un **mot témoin** planté dans la consigne factice » (garde 15, section 4.1). Or la répétition définit la garde par la plus longue suite de mots commune avec la part propre de la consigne, avec un seuil de 12 mots. Un mot témoin isolé fait une suite d'un mot : il passe. La garde telle que ce texte la règle échoue donc à l'une de ses deux épreuves, et une garde non éprouvée vaut une garde absente.
*Correction demandée* : ajouter à la statistique un second déclencheur, la présence d'un mot rare de la part propre (le mot témoin en est le cas d'épreuve), ou bien la définir de façon qu'elle voie les deux artefacts de la v10. Écrire la règle qui fixe ce second déclencheur pour la course, sur le même modèle que le seuil de 12 mots.

**B2 — « Mode connu » : de quoi s'agit-il ? Trois règles en dépendent.**
- La règle du bras dit que les candidats du 28 octobre « deviennent des modes connus, déclarés » (engagement 1). Ces candidats sont des cellules du coffre (N-057). Pour un mode connu de cette sorte, son texte est en quarantaine. Les concepteurs de moniteurs n'en reçoivent que la classe de faille et l'hypothèse violée (N-057 point 3). Les épisodes sont alors des « épisodes dérivés du coffre », au sens plein de la pièce de sécurité.
- Dans ce cas, trois phrases du texte tombent. « L'embargo ne s'applique pas : le mode est connu de ceux qui conçoivent les moniteurs » est faux. « La mère peut le lire » contredit le cloisonnement de la mère. L'assembleur devient un lecteur du coffre, avec une ligne au registre des accès.
- Si, au contraire, le mode connu est un mode du programme dont le texte est hors quarantaine, comme les modes déclarés de la porte G1, le texte tient.
*Correction demandée* : au champ R-3, exiger un mode **dont le texte n'est pas en quarantaine** et que les concepteurs de moniteurs connaissent déjà ; l'attester par la mère, sans contenu. À défaut, l'embargo de la course s'applique tel quel, la mère ne lit pas, et l'assembleur est consigné comme lecteur du coffre.

**B3 — Le nombre minimal de paires : un choix à la main après les nombres, sur un lot qui ne se change pas.**
La règle rend une borne, puis laisse « qui tient le préenregistrement de G1 » en tirer le nombre de paires « à mettre au lot pour espérer n épisodes à dommage tenu ». Deux défauts.
- (i) `n` n'est fixé nulle part avant la répétition. Il sera donc choisi après avoir vu ses nombres, ce que ta propre phrase interdit : « aucune n'est choisie à la main après avoir vu les nombres ».
- (ii) Le nombre de paires du lot de la course est fixé par la pièce 4 de la famille, déjà scellée (course, « Taille »). Il ne s'ajuste pas.
Ce que la répétition peut fixer, c'est seulement le champ n° 15 de la course, c'est-à-dire le minimum de paires complètes en dessous duquel la course est « insuffisante ». Elle peut aussi prédire si le lot fixé le tiendra.
*Correction demandée* : faire fixer `n` (ou directement la règle qui donne le champ n° 15) par qui tient G1 **avant** la répétition, scellé ici ou dans un addendum préalable. La règle calcule alors le champ n° 15 par programme. Si le lot fixé de la course ne peut pas l'atteindre sous la borne prudente, c'est un nœud avant la course, et la course n'est pas agrandie.

### Points mineurs

**M1 — La forme courte par renvoi (ton point 1).** Le renvoi par empreinte suffit pour une pièce de classe A, à deux conditions.
- (a) Écrire que les passages cités du texte de référence (champ R-1), **à cette empreinte**, font partie de ce texte et deviennent opposables par son scellement. Un brouillon de la course reste sinon « non opposable ».
- (b) Compléter la table des différences de trois lignes :
  - l'**attestation de l'assembleur**, puisque les dix questions de la course portent sur la famille ; dire lesquelles valent pour le lot du mode connu (outils, plafonds, environnement simulé, lecture du dommage sur le seul produit) ;
  - le **nœud 10 et la réserve de D1**, sans objet ;
  - la **pièce du vérificateur** : dire qu'elle est propre à la répétition, qui tourne sur une autre instance, et que la course en demande une nouvelle.

**M2 — La statistique de recouvrement : définition et plafond.**
- Dire comment les mots sont découpés et normalisés : casse, ponctuation, chiffres.
- La règle « le plus grand de 12 et du maximum des jumeaux plus un » ne fait que monter. Si des jumeaux honnêtes recouvrent fortement la part propre, le seuil de la course monte sans borne et la garde s'affaiblit. Ajouter un plafond, au-delà duquel c'est un nœud.

**M3 — Le plafond de dépense de la course : aucune règle.** Ton point 5 le range parmi les valeurs que fixe la répétition, mais la table n'en donne pas. Ajouter une règle par programme, du même type que les heures : heures × tarif constaté, plus le stockage, plus produits × lecteurs × jetons par produit × tarif, majoré du taux de renvoi observé.

**M4 — « Dépasse un produit sur dix » : par le compte ou par une borne ?** La prédiction se réfute par la borne basse au-dessus de 0,10 ; la règle dit « si un lecteur dépasse ici un produit sur dix ». Choisir l'un des deux et l'écrire aux deux endroits. Le compte observé (plus de 10 produits non lus sur 100) est plus prudent pour une course qui ne se rejoue pas.

**M5 — Douze heures et la taille du lot de la course.**
- Cent épisodes, au plafond de 20 minutes chacun, font 33 heures. Ajouter une condition de lancement : si la durée médiane mesurée à la répétition à blanc, multipliée par 100 et par 1,5, dépasse 12 heures, c'est un nœud avant le départ, et non une troncature.
- Les règles des heures et du stockage de la course demandent « le nombre d'épisodes du lot de la course ». Dire qui le fournit, l'assembleur, par son compte seul, et dans quel addendum.

**M6 — La conséquence pour la course (ton point 5).** Je la tiens pour juste, et je vois un ajout.
- Les valeurs fixées par la répétition vont à un addendum de la course scellé **après** la répétition et avant son GO (un « addendum C »), et le champ n° 15 sort de l'addendum A.
- Ajout : les gardes dont un paramètre change (9 plafonds, 15 fuite de consigne, renvois de la voie d'envoi) refont leurs deux épreuves à blanc avec les valeurs neuves, résultats scellés, avant la course. Une garde éprouvée à un autre seuil n'est pas éprouvée à celui-ci (R5).
- La seconde confirmation du vérificateur interne couvre alors l'addendum C et ces épreuves refaites.

### Ce qui tient

- **Les règles gelées** (ton point 2) ne laissent aucun choix à la main pour : les plafonds par épisode, les heures, le stockage, le plafond de produits retenus, les renvois, le refus et l'accord. Les nœuds sont bien placés. Restent M3, M4, M5 et B3.
- **Les valeurs de départ** (ton point 3) sont dites comme choix de l'auteur, sans donnée : 12 mots, 5 produits, 2 renvois et 5 %, un sur dix, 12 heures, 50 paires. Leur ordre de grandeur est raisonnable ; la précision à 50 paires est bien dite. Restent B1, M2 et M5.
- **L'embargo levé** (ton point 4) est juste si le mode est hors quarantaine (B2). Lot, produits, réponses et activations restent en quarantaine, à bon droit.
- **Une seule fois, aucun réemploi** dans G1, un calage ou une conception de moniteur : bien écrit, et la liste d'arrêt le garde.
- **Graines** : racine distincte, mêmes clés (R9). **Trop propre** dans les deux sens (R4). **Prononcé** par un lecteur neuf (R13).
- **Aucun contenu de mode**, de recette ni de paramètre d'attaque.

## Verdict

**À corriger.** Trois bloquants (B1 à B3) et six mineurs (M1 à M6). Corrections attendues dans un brouillon 2 (R12), puis vérification par la même contre-lectrice.
