# Contrôle du différentiel v7 → v8 — préenregistrement du palier 0b — v1

- Auteur : contre-lecteur, modèle O, le même que pour le contrôle de la v7. Pièce de travail (classe C).
- Date : 2026-11-20. `date -u` lu à 04:52Z en cours de travail.
- Demande : message de la session qui m'a lancé (contrôle du différentiel v7 → v8). Mandat du rédacteur : `P0B/mandat-redacteur-palier-0b-v8-v1.md` (`df835a6bd021cc1ddeff82e55a53a9dbf66153f0a0d5649af084b963a243044d`, compagnon OK).
- Conditions : processeur seul. Aucun tirage, aucun lancement du code de l'étage. Aucun appel à un fournisseur de modèles, aucune dépense, aucun réseau. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Deux programmes lancés par leur chemin : l'outil de remplacement (rejeu) et `verifier_corrections_v8_v1.py` (comparaison de textes, sans graine). **Aucun refus de permission, de classifieur ni de garde.**

P0B : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Verdict

**Conforme après corrections — de tenue seulement.** La v8 est exactement la v7 plus les 28 remplacements. Mes dix-sept textes y sont à la lettre. Les onze remplacements du rédacteur sont justes et fidèles à mon § 4, et ne tranchent rien. Neuf remplacements de tenue restent à faire (§ 5). Aucun ne change une règle, un seuil, une valeur gelée, un critère ou une prédiction. Ils peuvent attendre la version qui refera l'erratum du commit ; ils sont à faire avant le scellement, non avant que la fiche aille à Lazar. Les nœuds 1 et 2 sont au format, sans défaut.

## 1. Empreintes

Toutes égales à leur compagnon et aux préfixes donnés :

| pièce (P0B/) | empreinte |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v8.md` | `fd275af81704997f2844e4ee9fdb68c5401658335221ea0768f70e3cdac9586c` |
| `remplacements-preenregistrement-palier-0b-v7-v8.json` | `28c89e35f1e873af7f6f4f29c425ab9a2db93cd2ee14715a500549f92a0ba82b` |
| `…-v8.md.journal-remplacements-v1.json` | `f289516475b8b85af664d6f83539013389d746810f5bd09008a175261b53f30f` |
| `differentiel-preenregistrement-palier-0b-v7-v8.diff` | `14d7b4b8836c3a9153068246bd5c0d47f8ef0de2d5d131f0f2fc2a39fe0bf41c` |
| `rapport-redacteur-palier-0b-v8-v1.md` | `510266a587b21bbfa4a71afaeb95cf31e54c7ce2e934142dfde3b26ef059ee9b` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v7.md` | `2f0f928f…`, intacte |
| `controle-differentiel-palier-0b-v7-v1.md` (versé) | `1211fed3b3ce0baa2324c1976897dda622e9fabc91c6ccbe50ea110346db19d0`, égal à ma pièce |
| `controle-v7-outils/calcul_reserve_23_v1.py` et sa sortie (versés) | `354731b3…` et `d692b301…`, égaux aux miens |

## 2. Point 1 — rejeu

- **Rejeu** : l'outil `391db990…` sur la v7 `2f0f928f…`, avec le JSON `28c89e35…`. Résultat : 28 remplacements, sortie `fd275af8…`, égale à la v8 à l'octet (`cmp` muet).
- **Journal rendu** : outil, cible, remplacements et sortie aux bonnes empreintes ; 28 remplacements ; aucun avertissement ; heure 04:45:22Z.
- **Différentiel** : refait par `diff -u`. Hors des deux lignes d'en-tête, il est égal au différentiel versé.

## 3. Point 2 — mes seize corrections

`verifier_corrections_v8_v1.py` cherche, pour chaque remplacement du JSON, le texte ancien et le texte neuf entre accents graves dans mon contrôle de la v7. Résultat :
- les remplacements n° 1 à 17 sont **tous deux présents à l'octet**, c'est-à-dire mes corrections 1 à 16, avec 9a et 9b ;
- les n° 18 à 28 n'y sont pas, comme il se doit : ce sont ceux du rédacteur.

Rien n'a été retouché.

## 4. Point 3 — les onze remplacements du rédacteur, mot à mot

| n° | lieu | jugement |
|---|---|---|
| 18 | titre « v7 » → « v8 » | juste |
| 19 | ligne de version | juste : la v7 est citée avec chemin et empreinte, puis le contrôle et le mandat ; la correction de fond est dite en une phrase ; les nœuds sont dits « non tranchés et sans défaut ». La règle de lecture (« cette version » vaut pour la v8, sauf ce qui dit comment la v7 a été produite ou relue) est acceptable, mais elle ne peut pas rendre juste la section « Contre-lecture » : remplacement T2 |
| 20 | ligne de date | **inexact** : « vers 04:50Z », alors que le journal dit 04:45:22Z. Le rédacteur le signale (rapport, § 8.2). Remplacement T1 |
| 21 | alinéa « Version 8 » | juste : les seize corrections sont décrites une à une sans erreur ; les onze ajouts sont déclarés ; ce qui est laissé tel quel et ce qui est remis à la mère sont nommés |
| 22 | tête commune et tête du nœud 1 | **fidèle à mon § 4**, sans jugement ajouté et sans rien trancher (voir ci-dessous) |
| 23 | tête du nœud 2 | fidèle (voir ci-dessous) |
| 24 | code v4, point 1 | juste |
| 25 | code v4, point 2 | **une inexactitude** : « sans comparer celle-ci à rien ». Le code v3 compare l'empreinte du fichier à celle qu'on lui passe (`graines.py` l. 92) ; ce qu'il ne fait pas, c'est la comparer à une empreinte fixée hors de l'appel. Remplacement T5 |
| 26 | code v4, point 5 | juste, fidèle à mes § 6 et § 7 |
| 27 | code v4, point 7 neuf | juste, fidèle à ma remarque 1. Le renvoi à la note D9 pour les plis est juste |
| 28 | écart 1, puce « Code » | juste |

**Têtes des nœuds** :
- Origine du savoir, conditions de R1, R3 et R4, ce que dit la v6 (réserves 17, 18, 19 ; liste d'arrêt, point 2 ; annexe C), jugement sur chaque règle, options qui ne dépendent pas de l'attente, chiffres 0,84/0,16 et 0,93/0,31 : tout est repris de mon § 4 et attribué au contrôle.
- Deux simplifications, sans effet sur le sens : la tête omet le précédent de la v4 (annexe F) et la mention de la réserve 22 sous R4.
- « l'arrêt attendu aurait disparu » reprend mon propre mot (« disparaîtrait ») ; il faut l'entendre « deviendrait improbable », de l'ordre de 0,16.
- Les deux inconvénients que la tête du nœud 2 « ajoute » à l'option (a′) viennent bien de mon contrôle (table du § 4.2 et correction 6).
- La tête commune joint ma remarque 4 sur l'issue probable, et le dit. C'est utile à Lazar, et c'est déclaré.

## 5. Remplacements de tenue de plus (texte exact)

Chaque texte ancien figure **une seule fois** dans la v8 (`grep -n -o -F -e`). Ils peuvent être portés avec l'erratum du commit refait, avant le scellement, par l'outil `391db990…`, avec un alinéa de tenue qui les inscrit. Cet alinéa doit dire aussi que la liste « Laissé tel quel » de l'alinéa « Version 8 » est en partie levée par eux.

**T1 (ligne de date, ligne 6).** Ici, comme pour T2, T3 et T5, les accents graves intérieurs font partie du texte ; chaque texte est la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord quand il y en a.
- Ancien : vers 04:50Z (`date -u` à 04:41Z en cours de travail ; heure exacte au journal de l'outil)
- Neuf : à 04:45Z (heure du journal de l'outil : 04:45:22Z ; `date -u` à 04:41Z en cours de travail)

**T2 (section « Contre-lecture », ligne 427).**
- Ancien : `**Cette version 7 n'est pas contre-lue à l'heure où elle est rendue** : elle change des règles (annexe H) et doit l'être par un sous-agent neuf qui ne l'a pas écrite (règle R2), avant tout scellement ; ce texte ne peut pas non plus être scellé avant les mots de Lazar sur les nœuds de l'annexe H, ni avant le code v4 et l'erratum du commit refait.`
- Neuf : `**Contre-lecture de la version 7 faite** (contre-lecteur neuf, modèle O ; `palier-0b/controle-differentiel-palier-0b-v7-v1.md`, `1211fed3b3ce0baa2324c1976897dda622e9fabc91c6ccbe50ea110346db19d0`) : « Conforme après corrections », seize corrections, portées par la version 8. **Contrôle du différentiel de la version 7 à la version 8 fait** (même contre-lecteur, modèle O ; `palier-0b/controle-differentiel-palier-0b-v8-v1.md`, empreinte inscrite par la mère au versement) : les dix-sept remplacements du contrôle sont à la lettre, les onze du rédacteur sont contrôlés, et il reste des remplacements de tenue. **Ce texte ne peut pas être scellé avant les mots de Lazar sur les nœuds de l'annexe H, ni avant le code v4 et l'erratum du commit refait et contre-lu.**`

**T3 (liste des fichiers à donner, ligne 429).**
- Ancien : `et, dans le code v3, les modules `audit.py`, `graines.py`, `constantes.py`, `etalonnage.py` et `tirages.py`.`
- Neuf : `et, dans le code v3, les modules `audit.py`, `graines.py`, `constantes.py`, `etalonnage.py` et `tirages.py`. Pour le contrôle du différentiel de la version 8 : cette version et la version 7, leur différentiel, le fichier des remplacements et le journal de l'outil, le mandat de la version 8, le contrôle de la version 7 et son calcul de la réserve 23 (`palier-0b/controle-v7-outils/`), le rapport du rédacteur de la version 8.`

**T4 (fin de la réserve 23, ligne 524).**
- Ancien : `σ₀ y est alors sous-estimé, ce qui va dans le sens de l'arrêt.`
- Neuf : `σ₀ y est alors sous-estimé ; depuis la version 8, il est rapporté et ne décide d'aucun arrêt, les deux audits de lois étant lus à la lettre de la version 6.`

**T5 (code v4, point 2, ligne 811).**
- Ancien : `sans comparer celle-ci à rien.`
- Neuf : `sans la comparer à aucune empreinte fixée hors de l'appel, ni à celle que porte `constantes.py`.`

**T6 (annexe H, notes, ligne 804).**
- Ancien : `L'étalonnage et l'audit reçoivent ainsi trois causes d'arrêt de plus, écrites en B7 et à la section « Seuil »`
- Neuf : `L'étalonnage et l'audit reçoivent ainsi trois causes d'arrêt de plus, écrites en B7 et à la section « Seuil » (la version 8 en ajoute une quatrième à l'audit : une exactitude qui ne peut être calculée)`

**T7 (« Pour information, par la mère », ligne 865).**
- Ancien : `l'étalonnage et l'audit ont trois causes d'arrêt de plus (notes D8 et D9, choix 6)`
- Neuf : `l'étalonnage et l'audit ont quatre causes d'arrêt de plus (notes D8 et D9, choix 6, et l'exactitude non calculable de la version 8)`

**T8 (table « Ce que cette version touche », ligne 878).**
- Ancien : `| liste d'arrêt | mots inchangés | trois causes d'arrêt de plus, écrites en B7 et à la section « Seuil » |`
- Neuf : `| liste d'arrêt | mots inchangés | trois causes d'arrêt de plus, écrites en B7 et à la section « Seuil » ; une quatrième à l'audit par la version 8 (exactitude non calculable) |`

**T9 (nœud 2, option (a), ligne 849).** Le texte ne fait que dire dans la ligne de l'option ce que la décision (correction 9a) et la tête du nœud disent déjà. Lazar lit l'option ; elle doit porter la restriction.
- Ancien : `*Option (a), celle de cette version* — avantage : un arrêt vaut preuve, et le bruit est mesuré sur les données mêmes ; inconvénient : le seuil d'arrêt monte de deux écarts-types, vers 0,61 pour les mondes par dose, et une exactitude vraie de 0,60 n'y arrête qu'une fois sur trois environ.`
- Neuf : `*Option (a), celle de cette version, restreinte aux trois audits des mondes par dose* — avantage : un arrêt vaut preuve, et le bruit est mesuré sur les données mêmes ; inconvénient : le seuil d'arrêt monte de deux écarts-types, vers 0,61 pour les mondes par dose, plus haut si les mondes d'une suite se ressemblent, et une exactitude vraie de 0,60 n'y arrête que d'une fois sur trois à une fois sur neuf environ (réserve 23) ; deux régimes de lecture pour les cinq exactitudes de forme.`

**Laissés tels quels sans dommage**, l'alinéa « Version 8 » suffisant :
- « cette version est produite par 30 remplacements » au premier alinéa de l'annexe H : c'est l'histoire de la v7, sous la règle de lecture de la ligne de version ;
- les titres et les autres lignes des deux tables de fin de l'annexe H, qui décrivent la v7 ;
- la réserve 22 et la puce « Ce que le rédacteur savait ».

## 6. Les deux points remis à la mère

- **Remarque 3** (les causes d'arrêt de l'étalonnage ne sont portées par aucun point de la liste d'arrêt). Elle n'est **pas à corriger avant Lazar** : elle ne touche aucun nœud, aucune valeur, aucun seuil. Je la recommande avant le scellement, comme tenue de la liste d'arrêt qui ne change pas ses mots. Texte facultatif (ancien unique, ligne 287) :
  - Ancien : `c'est un arrêt de l'étalonnage, rapporté avec sa cause, jamais une case rangée en silence.`
  - Neuf : `c'est un arrêt de l'étalonnage, rapporté avec sa cause, jamais une case rangée en silence ; il se traite comme le point 2 de la liste d'arrêt : rien ne se tire, et la valeur ou la définition en cause se change par un erratum contre-lu.`

  L'action ajoutée va dans le sens de l'arrêt. Si la mère y voit un changement de la liste d'arrêt, c'est une information pour Lazar, non un nœud.
- **Part de la remarque 1 qui changerait une règle** (tirer les plis par suite). Elle n'est **pas à corriger avant Lazar**. Le texte fait déjà rapporter la moyenne des exactitudes permutées, et le point 7 du code v4 la fait regarder. Le biais attendu est petit : trois frères sur environ 160 mondes d'entraînement par classe. Changer les plis changerait la règle de la note D9 et ce qui vaut dépassement pour les doses : si la mère le veut, cela relève du nœud 2, posé à Lazar et non tranché, sans défaut. À mon avis, il vaut mieux attendre ce que la moyenne permutée montre au code v4.

## 7. Points 4 et 5 — format des nœuds ; identifiants de modèle

- **Nœuds 1 et 2** (v8, lignes 831-853) : tête de contexte, décision en une phrase, enjeu, trois options avec avantage et inconvénient, recommandation et confiance, « Défaut : aucun ». Au format.
- **Proposition de la garde 27** (lignes 855-863) : au format, défaut sous 48 heures (a). Inchangée.
- La tête de contexte précède la décision, comme le mandat le demande (« en tête des nœuds »).
- **Identifiants de modèle** : aucun dans la v8 ni dans le fichier JSON. Dans le rapport, les seules occurrences sont des chemins (`/tmp/claude-0/…`, `/root/.claude/`).

## 8. À déclarer de mon côté

- Mon contrôle de la v7 se dit écrit « de 04:21Z à 04:45Z environ ». L'heure de fin était estimée, non lue : mon seul `date -u` de ce travail donne 04:34Z, et la pièce a été rendue avant le premier `date -u` du rédacteur (04:41Z). C'est la faiblesse que ma correction 16 relevait chez le rédacteur. Aucun texte de la v8 ne cite cette heure.
- Dans le verdict du contrôle de la v7, « quatre de tenue ou de silence (corrections 10 à 16) » compte mal : il y en a sept. Le § 9 est juste, et la v8 l'a suivi.

## 9. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-palier-0b-v7/` :
- cette pièce et son compagnon ;
- `verifier_corrections_v8_v1.py` ;
- `rejeu/v8-rejouee.md` (`fd275af8…`) et son journal ;
- `rejeu/diff-v7-v8-refait.diff`.

*Contre-lecteur, modèle O.*
