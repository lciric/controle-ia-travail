# Contrôle du différentiel v1 → v2 — préenregistrement court de la course « nouvelles attaques » — v1

- Contre-lecteur, modèle O. Je suis le même que celui de la contre-lecture `a9886437aeac1c8aa38c132efcdbc34f8593588194e48e1d2c0d5b8c9a78999b`. Écrit le 2026-11-20 ; relevé de `date -u` : 05:44:47Z, après les vérifications et avant l'écriture.
- Mandat du rédacteur : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v1/mandat-redacteur-preenregistrement-court-v2-v1.md`, empreinte `52906f3590c9783a0beed5504a037f4d8b004e41db91b9fb6a6ac36f1f32f15f`, recalculée.
- Pièces contrôlées : dossier `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v2/` (commit `c1510a2c`).
  - Préenregistrement v2 : `be4e3c4a6966400a801f34a4951226b313e54cd5af9ed37cc041b04fa08223a1`.
  - Rapport v2 : `e9735e5d60a9eb8bcf1e29b66a7cba1cb3d750fbb3ba0abd45438c9a627d52e6`.
  - Rapport court : `686c0d7d3f6cc11972a605e1e298720f38fba1607917d86e209079f22823d479`.
  - Remplacements : `5df3277d…` (préenregistrement) et `47197b74…` (rapport).
  - Différentiels : `5747c5d4…` et `3a077924…`.
- Je n'ai fait que du calcul sur processeur : aucun appel à un fournisseur de modèles, aucune dépense, aucune valeur de clé. Je n'ai rien écrit dans le dépôt et rien commité. Je n'ai rien ouvert sous `archives-reponses-modeles/` ni dans le coffre. Réseau : un `git fetch origin main`.
- **Aucun refus de permission, de classifieur ni de garde.**

## 0. Verdict

**Conforme après corrections.**

Ce qui est conforme :
- Les deux pièces v2 sont exactement ce que donne l'outil quand on le rejoue, à l'octet près.
- Les corrections K1 à K24 sont portées à la lettre, avec trois choix de forme admissibles.
- Les relectures de `main` sont justes.
- Il n'y a ni recette, ni identifiant de modèle.

Ce qui reste à corriger avant le scellement :
- Depuis la v2, Lazar a tranché N2 (GO-2026-11-20-22, R-4110). La v2 dit encore « X est ouvert », et elle ne porte pas la répartition retenue.
- La ligne « Statut » et la section « Contre-lecture » sont restées dans leur état de la v1. Avec cette section en l'état, le texte ne passe pas le scellement.

Les corrections L1 à L8 s'appliquent à une **v3** : la v2 a déjà son empreinte et ne s'écrase pas (règle R12). Le texte exact est au § 5.

## 1. Rejeu de l'outil, à l'octet

J'ai rejoué l'outil `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, recalculée) sur les deux pièces v1, avec les remplacements versés, vers mon dossier `rejeu-v2/`. Les deux appels rendent « FAIT » :

| pièce | remplacements | sortie du rejeu | pièce versée |
|---|---|---|---|
| préenregistrement (cible `0f0d8b9b…`) | 41 | `be4e3c4a6966400a801f34a4951226b313e54cd5af9ed37cc041b04fa08223a1` | égale |
| rapport (cible `057b3a4c…`) | 9 | `e9735e5d60a9eb8bcf1e29b66a7cba1cb3d750fbb3ba0abd45438c9a627d52e6` | égale |

J'ai ensuite régénéré les deux différentiels par `diff -u` entre la v1 et la v2 versée. J'ai comparé leurs corps (sans les deux lignes d'en-tête) à ceux des différentiels versés. Ils sont égaux : `daa0342e…` pour le préenregistrement, `e868fb69…` pour le rapport. Aucune autre ligne ne change.

## 2. K1 à K24, à la lettre

J'ai lu les deux différentiels contre le § 8 de ma contre-lecture. Chaque texte nouveau y est au caractère près, à l'endroit dit :

- **Préenregistrement** :
  - K1 à K4 ; K5 (a) à (d) ; K6, avec la phrase de la ligne 116 ;
  - K7, le bloc entier, avec ses deux tables, « Pourquoi », la branche retenue, « ce qui ne change pas » et la condition de GO-2026-11-20-08 ;
  - K8 (a) à (g) ; K10 (a) à (d), avec la phrase ajoutée ; K11 à K20 ;
  - K21, avec sa marque ;
  - le titre et la ligne « Version ».
- **Rapport** : K22 (N1 tranché, N2 récrit, phrase de routine) ; K23 ; K24 (a) à (d) ; le titre et la ligne « Version ».
- **Les trois choix de forme** du rédacteur sont admissibles :
  - **K9** : le crochet est rempli par son relevé (05:35:27Z). C'est ce que la correction demandait.
  - **K10** : la phrase ajoutée forme un paragraphe à part, après la table. C'est la lettre de « après la table, ajouter ».
  - **K21** : la marque « à accepter ou refuser par la mère » est ajoutée, comme son mandat le demande. La mère l'a acceptée depuis, et L7 met la marque à jour.

## 3. Relectures de `main`

- **Au commit `8ba3c932490d915dc8fa2d424a6041e694498ec2`** :
  - `registres/go.md` a pour empreinte `faa6bd5175a6639a944485b6ab6112b938dabb7e8cbd47fca22e5aa8a31f9a4b`, égale à celle de la v2 ;
  - `registres/decisions.md` a pour empreinte `29116cfa43660c3aca5a4a11cb10ccc9e2032848ab66f71a1a34f351caf645c0`, égale à celle de la v2.
  - Entre `0b265f65…` et `8ba3c932…`, `decisions.md` ne gagne que les lignes R-4094 à R-4103. Aucune ne touche cette course, et les lignes nommées sont inchangées. **K2 et K3 sont justes.**
- **`main` a avancé depuis**, au commit `3c9ef9cf37061370bfbacfc76b41b6a61ea73f61` :
  - `go.md` : `3fbfcd40abc0903e7fc2ea0e2d5d7c5f2f63b8a2c76a92bf61d77451f87bbcaf` ;
  - `decisions.md` : `d5a4df8fa2e2e683950151ca5f1aab6169018f706c62874fc7671cb982f63f45`.
  - On y trouve **GO-2026-11-20-22** : « N2 (a) : les 8,35 USD au plus réservés par l'essai de mesure du bras A sont retranchés de la part de la course sur la clé Rigaud. Répartition : le juge sur Minuit, l'aiguilleur et l'espèce 4 sur Luc, l'espèce 3 sur Rigaud ; borne des trois clés 423,56 − 8,35 USD (GO-2026-11-20-16) ».
  - On y trouve aussi **R-4110**. La mère y lit le « go a » de Lazar comme valant pour deux décisions. Elle le déclare, et Lazar peut restreindre cette lecture.
- **Divergence de lettre, à signaler à la mère.** Dans GO-2026-11-20-22, le « (a) » ne correspond pas aux options du rapport v2 :
  - dans le rapport v2, l'option (a) de N2 est la seconde table : rien sur Rigaud ;
  - le contenu écrit de GO-22 correspond à l'option (b) du rapport : X égal à 8,35 et première table.

  La lettre renvoie sans doute à la question que la mère a posée elle-même. Le contenu de la ligne est explicite, et c'est lui que je retiens dans L3 à L6. La mère confirme que Lazar a bien répondu à ce contenu.

## 4. Aucune recette, aucun identifiant de modèle

Aucun des ajouts ne porte de procédé, d'étape ou de détail opérant. J'ai cherché sans casse les noms de modèles, de fournisseurs et de clés de variable dans les deux pièces v2 :

- **Préenregistrement** : `spawn_key`, un faux positif, et une fois « file Claude » (K5 (c)).
- **Rapport** : `claude-0`, dans un chemin de dossier ; `CLAUDE.md` ; « part Claude » et « file Claude », dans N2 (K22).

« Claude » nomme ici une famille, comme dans les lignes de GO. Ce n'est pas un identifiant de modèle. Ces mentions viennent de mes corrections. Le rédacteur v1 évitait de nommer le fournisseur : la mère peut écrire « la part des trois clés » à la place si elle le préfère. Ce n'est pas bloquant.

## 5. Points signalés par le rédacteur, et corrections avant le scellement

| point signalé | correction avant le scellement ? |
|---|---|
| choix de forme K9, K10, K21 | non, sauf la marque de K21, mise à jour par L7 |
| répartition retenue écrite au seul rapport | **oui** : GO-2026-11-20-22 la fixe ; elle va au texte (L4 à L6) |
| « non contre-lue » dans la ligne « Statut » | **oui** (L1) |
| section « Contre-lecture » « non faite » | **oui**, bloquant : le validateur exige deux empreintes, et le gabarit exige le traitement des remarques (L8) |
| restes de la v1 dans le rapport v2 : nom de fichier v1, ancien dossier, commit `8cf0d3d1…`, § 5 points 2 et 6 | **non** : le rapport n'est pas la pièce scellée. Je recommande de ne pas en faire de v3 ; ce contrôle consigne ces restes comme historiques. Le N2 du rapport v2 est dépassé par GO-22 |

Les corrections suivantes s'appliquent sur `preenregistrement-court-course-nouvelles-attaques-v2.md` (`be4e3c4a…`). Elles produisent `preenregistrement-court-course-nouvelles-attaques-v3.md`, et la v2 reste archivée. Le titre passe de « — v2 » à « — v3 ».

**L1** (ligne 7). Ancien :
`- Statut : **pièce de travail, non contre-lue, non scellée.**`

Nouveau :
```
- Statut : **pièce de travail, non scellée.** La v1 est contre-lue (`a9886437aeac1c8aa38c132efcdbc34f8593588194e48e1d2c0d5b8c9a78999b`) ; le différentiel v1 → v2 est contrôlé (`controle-differentiel-preenregistrement-court-v1-v2-v1.md`, [empreinte de ce contrôle]).
```

**L2** (ligne 13). Ancien :
`corrections K1 à K24 appliquées à texte exact ; la v1 reste archivée, non modifiée.`

Nouveau (deux lignes, séparées par un saut de ligne) :
```
corrections K1 à K24 appliquées à texte exact ; la v1 reste archivée, non modifiée.
- Version : la v3 remplace la v2 (`be4e3c4a6966400a801f34a4951226b313e54cd5af9ed37cc041b04fa08223a1`) après le contrôle du différentiel `controle-differentiel-preenregistrement-court-v1-v2-v1.md` ([empreinte de ce contrôle]) ; corrections L1 à L8 appliquées à texte exact ; la v2 reste archivée, non modifiée.
```

**L3** (lignes 26 et 27).

Accords. Ancien :
`` | accords | `registres/go.md` sur `main`, commit `8ba3c932490d915dc8fa2d424a6041e694498ec2` : GO-2026-11-20-05, -08, -10, -12, -13, -14, -16 ; GO-2026-11-19-34 | `faa6bd5175a6639a944485b6ab6112b938dabb7e8cbd47fca22e5aa8a31f9a4b` | ``

Nouveau :
`` | accords | `registres/go.md` sur `main`, commit `3c9ef9cf37061370bfbacfc76b41b6a61ea73f61` : GO-2026-11-20-05, -08, -10, -12, -13, -14, -16, -22 ; GO-2026-11-19-34 | `3fbfcd40abc0903e7fc2ea0e2d5d7c5f2f63b8a2c76a92bf61d77451f87bbcaf` | ``

Décisions. Ancien :
```
R-4088, R-4089, R-4091, R-4092, R-4093 | `29116cfa43660c3aca5a4a11cb10ccc9e2032848ab66f71a1a34f351caf645c0` |
```

Nouveau :
```
R-4088, R-4089, R-4091, R-4092, R-4093, R-4110 | `d5a4df8fa2e2e683950151ca5f1aab6169018f706c62874fc7671cb982f63f45` |
```

Si `main` a encore avancé, le commit et les empreintes sont ceux de la relecture faite au moment d'appliquer, et les lignes nommées doivent y être inchangées.

**L4** (ligne 105, fin du paragraphe « Réserve sur Rigaud »). Ancien :
`**X est ouvert** : la mère l'écrit au complément de valeurs, ou le porte à Lazar (nœud N2 du rapport).`

Nouveau :
`**X est fixé : 8,35 USD** (GO-2026-11-20-22, R-4110 ; nœud N2 tranché). La part de la course sur Rigaud est le reste calculé de Rigaud, moins 8,35 USD, soit environ 38,65 USD. La borne des trois clés est de 423,56 − 8,35 = 415,21 USD (GO-2026-11-20-16). Si le bras A dépense sur Rigaud plus de 8,35 USD pendant la course, cela peut déclencher l'arrêt n° 13 : la mère l'empêche, ou le consigne. Si Lazar restreint la lecture que la mère fait de son mot (R-4110), cette ligne tombe et une version neuve s'écrit.`

**L5** (fin du paragraphe « Pourquoi », ligne 112). Ancien :
`Au pire du devis, aucune répartition ne tient : entre le cas haut et le pire, l'arrêt n° 12 tient la dépense.`

Nouveau :
`Au pire du devis, aucune répartition ne tient : entre le cas haut et le pire, l'arrêt n° 12 tient la dépense.`
(ligne vide)
`**Répartition retenue** (GO-2026-11-20-22) : la première table. Minuit porte le juge de l'espèce 3 (rapport 1,547) ; Luc, l'aiguilleur et le proposeur de l'espèce 4 (1,721) ; Rigaud, le proposeur de l'espèce 3, sur une part d'environ 38,65 USD (1,452). La seconde table reste écrite comme la règle de choix ; elle ne s'applique pas dans cette version.`

**L6** (« Valeurs ouvertes », ligne 120 et sa table).

(a) Ancien :
`**Valeurs ouvertes.** La branche est tranchée (GO-2026-11-20-16). Les parts et la répartition se figent au complément de valeurs, selon les valeurs et la règle écrites ci-dessus. Ce qui reste ouvert est dans la table.`

Nouveau :
`**Valeurs ouvertes.** La branche est tranchée (GO-2026-11-20-16), X et la répartition aussi (GO-2026-11-20-22). Les parts s'écrivent au complément de valeurs, sur le reste calculé de chaque clé au jour du complément. Ce qui reste ouvert est dans la table.`

(b) Ancien :
`| X, le besoin du bras A sur Rigaud, donc la part de Rigaud et le choix entre les deux tables de répartition | écrit par la mère au complément de valeurs, d'après le devis du bras A (essai de mesure : au plus 8,35 USD ; lectures : non trouvé par chemins nommés) ; s'il n'est pas écrit, la seconde table s'applique et le nœud N2 va à Lazar | avant tout allumage et avant la contre-lecture du véhicule |`

Nouveau :
`| la part de Rigaud, en USD | le reste calculé de Rigaud au jour du complément, moins 8,35 (GO-2026-11-20-22). Si cette part est plus basse que 26,61, le cas haut du proposeur de l'espèce 3, la répartition retenue ne tient plus : une version neuve s'écrit, sur le mot de Lazar | avant tout allumage et avant la contre-lecture du véhicule |`

(c) Ancien :
`| la part bornée de chaque clé, en USD | GO-2026-11-20-16 : Minuit 162,56 ; Luc 214 ; Rigaud 47 moins X ; écrite au complément, jamais abaissée en silence (arrêt n° 11) | même moment |`

Nouveau :
`| la part bornée de chaque clé, en USD | GO-2026-11-20-16 et -22 : Minuit 162,56 ; Luc 214 ; Rigaud 47 moins 8,35, soit environ 38,65 ; borne des trois clés 415,21 ; écrite au complément, jamais abaissée en silence (arrêt n° 11) | même moment |`

(d) Ancien :
`| la répartition des rôles du premier relais entre les trois clés | la règle ci-dessus (rapport minimal le plus grand), première ou seconde table selon X, si la contre-lecture du véhicule la confirme ; chaque rôle sur une seule clé, fixe pour les trois générations | même moment |`

Nouveau :
`| la confirmation, par la contre-lecture du véhicule, de la répartition retenue (GO-2026-11-20-22) ; chaque rôle sur une seule clé, fixe pour les trois générations | la contre-lecture du véhicule ; tout écart est une version neuve | même moment |`

(e) Ligne 213, point 3 de « Ce qui reste à écrire avant l'allumage ». Ancien :
`Reste le **complément de valeurs** (section « Seuil ») : X et les parts des trois clés, la table de répartition, le pire par appel de l'aiguilleur et du juge, les bornes en octets.`

Nouveau :
`Reste le **complément de valeurs** (section « Seuil ») : les parts des trois clés (X = 8,35 USD et la répartition sont fixés par GO-2026-11-20-22), le pire par appel de l'aiguilleur et du juge, les bornes en octets.`

**L7** (ligne 211). Ancien :
`(Règle proposée par la contre-lecture, correction K21 : à accepter ou refuser par la mère.)`

Nouveau :
`(Règle proposée par la contre-lecture, correction K21, acceptée par la mère : [ligne du registre des décisions qui consigne l'acceptation].)`

La mère inscrit cette acceptation au registre des décisions avant que L7 s'applique. Je ne l'ai pas trouvée sur `main` au commit `3c9ef9cf…`.

**L8** (ligne 258, toute la section « Contre-lecture »). Ancien :
`Non faite à cette date. Ce texte est à contre-lire par un sous-agent neuf, qui ne l'a pas écrit, à qui l'on donne explicitement les fichiers de la table « Documents qui font foi » (règle R2). Seront portés ici, avant le scellement : son identifiant, l'empreinte du brouillon relu, le chemin et l'empreinte de son rapport, et le traitement de chaque remarque (acceptée, ou refusée et pourquoi). Sans cela, ce texte ne se scelle pas.`

Nouveau :
```
- **Contre-lecture 1** : contre-lecteur neuf, modèle O, sous-agent de la session de l'organisme, le 2026-11-20 ; il n'a écrit ni ce texte ni la conception. Brouillon relu : la v1, `0f0d8b9b4c42b56c2e8928b283ca655f4cd88c9fe1529a0debabaaba94979507`. Rapport : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v1/contre-lecture-preenregistrement-court-nouvelles-attaques-v1.md`, `a9886437aeac1c8aa38c132efcdbc34f8593588194e48e1d2c0d5b8c9a78999b`, verdict « Conforme après corrections ». Traitement : K1 à K24 acceptées, appliquées à texte exact dans la v2 ; K21, une proposition, acceptée par la mère.
- **Contre-lecture 2** (contrôle du différentiel v1 → v2) : le même contre-lecteur. Brouillon relu : la v2, `be4e3c4a6966400a801f34a4951226b313e54cd5af9ed37cc041b04fa08223a1`. Rapport : `controle-differentiel-preenregistrement-court-v1-v2-v1.md`, [empreinte de ce contrôle], verdict « Conforme après corrections ». Traitement : L1 à L8 acceptées, appliquées à texte exact dans la v3.
```

Le chemin du rapport 2 est celui où la mère le verse. Chaque entrée porte deux empreintes, comme `src/controle_ia/prereg.py` l'exige.

Après L1 à L8, il reste une vérification courte : le rejeu de l'outil et le différentiel v2 → v3. Il n'y a rien d'autre à refaire.

## 6. Réserves

1. **La lecture « go a » vaut-elle pour les deux décisions ?** C'est une lecture de la mère, déclarée (R-4110). Elle porte toute la répartition retenue. Si Lazar la restreint, L4 à L6 tombent.
2. **La lettre de GO-2026-11-20-22**, « N2 (a) », ne suit pas la lettre du rapport v2 (§ 3). Le contenu de la ligne prime ; la mère le confirme.
3. **L'acceptation de K21** est dite par la mère. Elle n'est pas encore au registre sur `main` au commit `3c9ef9cf…`.
4. **Le reste de Rigaud est « environ 47 »** : c'est un calcul, non une lecture. La part de 38,65 USD se récrit au complément, sur le reste calculé de ce jour-là (L6 (b)).

## 7. Refus

Aucun refus de permission, de classifieur ni de garde.

— contre-lecteur, modèle O
