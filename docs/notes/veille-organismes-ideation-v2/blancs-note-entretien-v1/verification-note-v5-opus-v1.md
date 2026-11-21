# Vérification de la note pour l'entretien v5 (blancs remplis) — Opus, v1

- **Date** : 21 novembre 2026, de 20:42 à 20:50 UTC (`date -u`). **Auteur** : Claude Opus 5.5, vérificateur neuf, qui n'a écrit ni la v5 ni la table des sources. Pièce de classe C. Aucun appel payant, aucune requête en ligne, aucun commit, aucune poussée.
- **Pièce vérifiée** : `note-entretien-controle-diffus-v5.md` (`603419415b181cc06e167258478f6669679d02e1fe8197b42428b8a46fd7ad2f`, égale à son compagnon).
- **Contre** : la v4 (`cd593d8f…71fd`), son erratum 1 (`5e7b4c7b…3480`), son erratum 2 (`ad6debe3…f023`), la vérification de l'erratum 2 (`d8c6a9b9…7fe7df`) et la table des sources `sources-des-blancs-v1.md` (égale à son compagnon) ; chaque empreinte est égale à son compagnon.

## Verdict

**À corriger, sur la forme seulement ; corrigé par moi en v6.** Chaque blanc rempli tient à sa source, chaque source ouverte a l'empreinte dite, aucun chiffre de résultat n'entre, aucun nom de session, identifiant de machine ni courriel. Défaut de forme : la table d'en-tête omet quatre changements que montre le `diff`, et trois formulations sont à reprendre. Le fond n'est pas touché.

Texte final : `../note-entretien-controle-diffus-v6.md` (`c28b4da6b9fea88e3ef83a311dc0a82ffc37f3126867550fe0f575c88318479f`) ; PDF : `../note-entretien-controle-diffus-v6.pdf` (`dd44bc074d5efc66db59bac74ac75f71395af10d7269c0cad66daad66dd6bcb5`), 21 pages, format A4.

## 1. Comparaison par `diff` (v4 → v5)

Chaque bloc du `diff` est rapporté à la table d'en-tête de la v5 :

| Bloc du `diff` | Rang de la table | Constat |
|---|---|---|
| Ligne 1 de la v4 retirée (nom du modèle de l'auteur) ; nouvel en-tête ; titre « En-tête de la v4, gardé » | aucun (dit en prose sous ce titre) | **omis de la table** |
| Titre du § 0, « (de la v3 à la v4) » | aucun | **omis** (sans effet sur le fond) |
| § 1, bloc « Depuis la v4 », quatre points | aucun | **omis** ; il résume les rangs 1, 2, 5 à 9 |
| § 1, point 4 ; § 4, puce de même texte | 1 | conforme à l'erratum 2, correction 2, mot pour mot |
| § 3, phrase 2 | 6 | conforme (section 2 ci-dessous) |
| § 3, phrase 4 | 2 | correction 1 de l'erratum 2, mot pour mot, plus « au même critère, écrit d'avance » (remarque 1) et la référence « N-062, points 1, 3, 4, 5 » |
| § 3, phrases 5 et 9 | 7, 8 | conformes (section 2) |
| § 3, phrase 10 | 5 | mot pour mot, la majuscule initiale mise ; nuance de la remarque 3 portée « pour toi » |
| § 4, trois puces neuves | 11 | tirées des blancs 2-a, 5-a, 9-a |
| § 5, objection 3 | 9 | erratum 1, mot pour mot |
| § 5, objection 5 | 12 | aligné sur 5-a et 5-b |
| § 8, puce D-6 | aucun | **omis** (« Cette v4 » devient « La v4, et cette v5 qui la complète ») |
| § 8, « et si c'est nul deux fois ? » | 3 | correction 3, mot pour mot |
| § 8, D-1 (a) et D-4 (a) | 4 | conforme ; la référence GO-2026-11-21-66 et la citation « on e s'arrete pas sur un resultat negatif » sont exactes à la ligne du registre des accords |
| § 8, nœud neuf « lit le handicap » | 13 | exact à la note `lire-l-intention-v1` (`dd2d97e8…13d2ac`, égale au compagnon), D-5, l. 261 : options (a), (b), (c), recommandation (a), confiance 0,7, contact externe, pas de défaut ; « tout y est scripté » (l. 12) ; aucun mot de Lazar sur D-5 trouvé dans le registre des accords après la demande GO-2026-11-21-68 |
| § 9, Goldowsky-Dill et al., pages | 10 | erratum 1 |
| § 10 renommé ; § 11 neuf | 14 | conforme |

Rien d'autre ne change : le reste du texte est identique à l'octet.

## 2. Chaque blanc à sa source

Registres lus par lignes : `registres/go.md` (lignes GO-2026-11-21-61, -65, -66, -69, -80), `registres/decisions.md` (R-597, R-772, R-1817, R-1849, R-3645, R-4275, R-4511 non relue, R-4600, R-4606, R-4613, R-4621, R-4627, R-4632, R-4635, R-4638, R-4640, R-4642, R-4643, R-4645, R-4654, R-4662, R-4670, R-4680, R-4682, R-4689, R-4694, R-4696, R-4698, R-4700 à R-4702, R-4704, R-4705). Les registres ont bougé depuis 20:27 UTC (`decisions.md` `dd4b11dc…`, `go.md` `32166df0…` à ma lecture ; `etat.md` inchangé, `0751abb2…`) ; les lignes citées sont les mêmes.

| Blanc | Ce qu'écrit la v5 | Source rouverte | Constat |
|---|---|---|---|
| 2-a | Taille de la référence et horizon non fixés ; prévision portée par un texte scellé avant toute lecture des épisodes qui la servent et avant la porte de fin de phase 1 ; en brouillon, renvoyée à corriger, correction interrompue | N-076, l. 51 à 55 (`49b664c1…`) ; `recherche-exhaustive-v1.md` (`73aa7317…`), l. 24 ; `brouillon-1-v1.md` (`08158ab8…`), en-tête seul, « jamais scellé » ; contre-lecture (`7b11cbfe…`), « à corriger » ; `LISEZ-MOI.md` (`3f9a6dd3…`), « ne font pas foi » ; R-4643, R-4702, R-4705 | **conforme**. Aucun chiffre du brouillon n'est repris |
| 2-b | Écart non mesuré ; un des tests de mort ; « la loi est juste et ne sert à rien » | N-076, l. 55, mot pour mot ; contre-lecture du brouillon, constat 3 ; R-4689, R-4696 (course non partie) | **conforme** |
| 5-a | Épreuves écrites, objets construits par programme (retrait, référence d'une autre tâche, troncature) ; garde d'invisibilité écrite, non attestée ; aucune épreuve sous verdict scellé | R-772 ; `artefacts_v1.py` (`22f0fc88…`), `test_cibles_invisibles_v3.py` (`93a6df43…`), égaux aux compagnons ; R-4640 (fautifs de l'inventaire, « à trancher ») ; R-1817 ; R-1849 ; verdict de l'étiqueteur (`9f7830b9…`, non ouvert) ; brouillon d'audit (`ccc0d972…`, non ouvert) | **conforme**. Le compagnon de `test_cibles_invisibles_v1.py` ne correspond plus au fichier (`b5fd257b…` contre `6a833e3e…`), comme le dit la table des sources ; la v5 ne cite pas la v1 |
| 5-b | Étape 0 accordée, en cours, sans dépense ; conceptions corrigées, en vérification ; données simulées seulement ; aucun modèle n'y a tourné | GO-2026-11-21-61 ; protocole X dommage v2 (`c2838803…`), l. 195 : « Étape 0, sans dépense », aucun modèle avant l'étape 1 ; GO-2026-11-21-66 et R-4635 ; R-4700 ; R-4613, R-4621, vérifications (`cd34f640…`, `a6013316…`) | **conforme**, avec la remarque 1 |
| 9-a | Rien de lancé, rien de lu ; règle scellée et contre-lue ; familles écrites, contre-lues, scellées ; préenregistrement de la course accepté, non scellé ; répétition générale avant ; moniteurs gelés non scellés ; comparaison aux juges en brouillon | recherche des pièces manquantes, pièces 2 et 3 ; R-4606, R-4627, R-4642, R-4645, R-4662, R-4670 ; index v3 (`cde486b0…`, non ouvert) ; R-4689, R-4694, R-4696 ; GO-2026-11-21-80 ; attestation du mode connu (`166ed502…`, non ouverte) ; R-4654 ; GO-2026-11-21-65 | **conforme**, avec la remarque 2 |
| Objection 5 | Aucune strate mesurée, aucune borne | N-075, erratum 3 v2 (`fbe3298e…`), l. 56 et 104 | **conforme** ; la v5 citait « erratum 3 » sans « v2 » |

## 3. Cloisons et identifiants

- **Chiffres** : les nombres ajoutés par la v5 sont des pages et des chiffres de papiers déjà présents dans la v4, des identifiants d'accord ou de décision, des empreintes, des heures et la confiance 0,7 de la recommandation D-5. Aucun chiffre de résultat du programme.
- **Noms** : aucun nom de session, identifiant de machine ou de serveur, ni courriel (recherche par motifs sur la v5 et la v6 : rien).
- **Ce que j'ai vu sans le reprendre** : la ligne R-1849 porte les chiffres de la phase 1 de l'étiqueteur, et la ligne R-4700 une phrase sur ce que l'étape 0 du banc à lois plantées a levé ; je n'en reprends rien, ici ni dans la v6. La v5 non plus.

## 4. Corrections de forme portées en v6

1. **Table d'en-tête** : rangs 15 à 18 ajoutés pour les quatre changements omis (section 1).
2. **§ 3, phrase 9, « Pour toi »** : « ni de ce qu'elles ont en commun » est retiré : la formule suggérait quelque chose du contenu des familles tenues à l'écart, sur une branche lue par qui conçoit les moniteurs (R-4670). Elle devient « ne dis rien des familles au-delà de leur existence et de leur état ».
3. **§ 3, phrase 5, « Pour toi »** : « a passé la première phase de ses épreuves sous verdict scellé « non tranché » » pouvait se lire « a réussi » ; elle devient « a reçu pour la première phase de ses épreuves un verdict scellé « non tranché » ».
4. **Deux citations** : « N-075, erratum 3, point 11 » devient « N-075, erratum 3 v2, point 11 ».
5. **En-tête** : une puce v6 et une section 12 disent ces corrections.

Le `diff` de la v5 à la v6 ne montre que ces cinq points.

## 5. Remarques, sans correction

1. **Phrase 5 et objection 5** : « l'étape 0 » réunit deux choses. L'étape 0 accordée par GO-2026-11-21-61 est celle du plan des tâches floues. « Données simulées » vient de la ligne R-4700, qui le dit de l'étape 0 du banc à lois plantées. Pour le plan des tâches floues, la phrase reste vraie par la définition de son étape 0 : sans dépense, aucun modèle avant l'étape 1. La mère peut le préciser à sa relecture de la veille.
2. **Phrase 9** : « familles … scellées » s'entend des pièces scellées par empreinte au coffre. La recherche des pièces manquantes dit que le scellement 2 « n'est pas scellé comme préenregistrement ». Si un juré demande « le préenregistrement des familles est-il scellé ? », la réponse est « non, pas comme préenregistrement ».
3. **Nœud D-5 (rang 13)** : la v5 le déclare, et il est exact. Il dépasse toutefois le remplissage des blancs que demandait GO-2026-11-21-69. Je le laisse, puisqu'il est dit, et c'est à Lazar de le garder ou non.
4. **Mise en page du PDF** : faute de `xelatex` et de `lualatex` sur la machine, il est produit par `pandoc -t html` puis `libreoffice --headless`. Les puces passent à la ligne après leur signe, et le titre des propriétés du document est en ASCII (avec un titre accentué, ces propriétés sortaient mal encodées ; le texte, lui, passait). Contrôlé : `pdfinfo` l'ouvre, 21 pages, A4 ; `pdftotext` sur la première page trouve « é » (34), « è » (6), « à » (4).

## Ce que je n'ai pas fait

- Je n'ai ouvert aucun résultat, aucun score, aucun épisode, aucun verdict au-delà de son empreinte, aucune pièce du coffre, aucune branche, aucun fichier dont le nom porte « vérité », « rendu », « scores », « consigne-privee » ou « conception-ii-b ».
- Je n'ai relu aucune page des papiers.
- Pas de commit, pas de poussée.
