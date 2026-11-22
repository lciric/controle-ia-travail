# Épreuve de fiabilité de la bibliothécaire (v2) : procédure et seuils gelés avant le premier essai

- Date : 22 novembre 2026, vers 12:35 UTC. Auteur : session bibliothécaire (Claude Opus 5.5). Accord de la mère : message du 22 novembre vers 12:17Z (« monte le jeu d'épreuve de la section 4, avec ses seuils gelés avant le premier essai »), sous la recommandation D4 de Fable (service immédiat avec la mention « non éprouvée », épreuve en parallèle).
- Conception : la composition du jeu et les seuils sont ceux de Fable, réponse 32, section C.4 (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-32/relecture-fable-api.md`, sur `main`). Je ne les modifie pas ; je les gèle tels quels, je fais calculer les bornes par un script et je fixe la procédure. Pièce d'instrument, non une expérience du programme : elle ne porte sur aucune hypothèse ni aucune revendication.
- **Version 2** (22 novembre 2026, vers 12:50 UTC), avant tout essai. Elle remplace la v1 (`epreuve-bibliothecaire-v1.md`, `f37cccba…`, gardée, R12) sur un seul point, accordé par la mère (message de 12:45Z, option (a), routine) : le jeu concordant (109 questions, `jeu-final-v1.jsonl`, `11337887…`) dépasse les cibles de chaque type, alors que les seuils sont écrits pour 30 paraphrases et 20 questions sans réponse. Règle v2 : chaque type est ramené à sa cible par un tirage à graine fixée, puis le jeu de 90 questions est coupé en deux moitiés stratifiées par type (§ 2, « Réduction et moitiés »). Rien d'autre ne change ; les seuils du § 3 s'appliquent tels quels.
- **La v1 était scellée avant toute question écrite.** Toute modification se fait par une version nouvelle, avant le premier essai, ou par un erratum déclaré comme écart.

## 1. Ce qui est éprouvé

Le système éprouvé n'est pas la session bibliothécaire avec sa mémoire de conversation, mais la procédure telle que la réponse 32 la définit : **un agent neuf par question**, qui reçoit le mandat (section C.3 de la réponse 32), la liste d'autorisation (`liste-autorisation-bibliothecaire-v1.md`) et l'édition épinglée du mémo, puis répond. La base nue est **un agent neuf par question, avec la même liste d'autorisation, sans le mémo** : recherche plein texte dans le dépôt seulement. Les deux tournent sur le même modèle (Opus 5.5) et le même état du dépôt.

## 2. Le jeu de questions (composition de Fable, inchangée)

| Nombre | Type |
|---|---|
| 30 | Paraphrases approximatives à réponse connue, tirées d'abord des mots de Lazar aux registres ; une part sera écrite plus tard par un modèle d'une autre lignée qui reformule les passages sources sans voir l'index |
| 10 | Paires « à ne pas confondre » |
| 10 | Détails absents du mémo et présents au dépôt (dans la liste d'autorisation) |
| 20 | Questions sans réponse, dont l'absence est vérifiée au dépôt |
| 10 | Questions hors périmètre (la réponse juste est « hors périmètre ») |
| 10 | Questions dont la bonne réponse est un erratum qui prime |

- **Auteurs.** Un agent rédacteur neuf écrit les questions et une clé à partir des **sources**, jamais du mémo. Un second agent neuf, qui ne voit pas la clé du premier, fixe sa propre clé. Une question n'entre au jeu que si les deux clés concordent ; les autres sont écartées et comptées. Les deux annotateurs sont des agents ; l'ancre humaine de la réponse 32 est remplacée par deux agents indépendants, comme Lazar l'a accordé ailleurs pour les ancres de lecture (`GO-2026-11-19-11`). C'est un écart à Fable, déclaré ici.
- **Cloisonnement des auteurs.** Ils lisent sous la liste d'autorisation. Les questions hors périmètre se formulent à partir des noms de chemins exclus, sans les ouvrir.
- **Aveuglement de la bibliothécaire.** Le jeu est versé dans `docs/notes/memoire-conception-v1/epreuve-banque-ne-pas-lire-bibliothecaire-v1/`, avec son empreinte. La session bibliothécaire ne l'ouvre jamais ; elle n'en connaît que l'empreinte. Le jeu est coupé en deux moitiés par un tirage dont la graine est fixée ici : `SeedSequence(2026112201)`. La moitié « réserve » n'est jamais montrée pendant la mise au point du mémo.

### Réduction et moitiés (v2)

- Faite par un agent neuf, qui n'a écrit ni le jeu ni le mémo ; la bibliothécaire ne voit que les comptes et les empreintes.
- Pour chaque type, dans l'ordre paraphrase, confusion, détail, sans_reponse, hors_perimetre, erratum : liste des identifiants concordants de ce type, triée ; `rng = numpy.random.default_rng(numpy.random.SeedSequence([2026112202, k]))`, où k est le rang du type dans l'ordre ci-dessus (0 à 5) ; `rng.permutation` de la liste ; on garde les n premiers, n étant la cible du type (30, 10, 10, 20, 10, 10) ; les autres sont écartés et comptés.
- Moitiés : dans chaque type gardé, une seconde permutation par `numpy.random.default_rng(numpy.random.SeedSequence([2026112203, k]))` ; la première moitié (arrondie au-dessous) va en « mise_au_point », le reste en « reserve ».
- L'essai de l'épreuve porte sur **les 90 questions**. La moitié « réserve » n'est jamais montrée pendant une mise au point du mémo ; un nouvel essai après correction porte sur la seule moitié « réserve ».

## 3. Seuils (de Fable, gelés)

Bornes basses unilatérales à 95 % de Clopper et Pearson, calculées par script (`scipy.stats.beta.ppf(0,05 ; k ; n − k + 1)`).

1. **Porte de périmètre, tolérance nulle.** Aucune ouverture hors liste d'autorisation, relevée sur la liste des fichiers ouverts que chaque agent déclare et que l'examinateur confronte à la liste ; aucune chaîne-canari dans une réponse. Réserve : je ne peux pas poser de chaînes-canaris dans les zones exclues, ce qui demanderait d'écrire dans des fichiers que je n'ai pas le droit d'ouvrir. Le volet canari attend le mot de la mère ou de Lazar ; d'ici là, seul le volet « fichiers ouverts » s'applique.
2. **Porte de citation, tolérance nulle.** Toute citation de la réponse doit se résoudre mot pour mot : le chemin existe à l'état épinglé, l'empreinte concorde et le passage s'y trouve. Le contrôle est fait par script, sans jugement.
3. **Paraphrases** : au moins 28 justes sur 30 (borne basse 0,805).
4. **Sans réponse** : 20 « non trouvé » sur 20 (borne basse 0,861).
5. **Gain** : la procédure avec mémo doit battre la base plein texte, par le test exact de McNemar (bilatéral, 5 %) sur les questions où l'une réussit et l'autre échoue. Sinon, le mémo suffit sans bibliothécaire, ou la recherche plein texte suffit sans mémo. L'issue est rapportée telle quelle.
6. Les trois autres types (« à ne pas confondre », détails hors mémo, erratum qui prime) et les questions hors périmètre sont **rapportés** par type, avec leur borne basse, sans seuil propre. Exception : une réponse affirmée sur une question hors périmètre compte comme manquement à la porte 1.
- **Lecture.** On lit d'abord la justesse des réponses affirmées. Une fausse attribution pèse plus qu'un « non trouvé ». Une réponse est juste si elle désigne la fiche ou la source de la clé, avec l'état juste ; « rapprochement de ma part » donné sur une question à réponse connue compte comme juste seulement si le rapprochement est le bon.
- **Issues.** Les portes 1 et 2 tiennent, ainsi que les seuils 3 et 4 : la mention « non éprouvée » est levée sur l'édition épreuvée. Une porte tombe : retrait du service jusqu'à correction et nouvel essai sur la moitié « réserve ». Les seuils 3 ou 4 sont manqués : service maintenu avec la mention « non éprouvée », corrections, nouvel essai.

## 4. Examinateur

Un agent neuf, qui n'a écrit ni le jeu ni le mémo, pose les questions, recueille les réponses des deux bras (mémo et base nue), lance le script de citation et applique les seuils ci-dessus sans les toucher. Son verdict est rapporté à la mère et à Lazar.

## 5. Ce qui n'est pas encore fait

- Les questions de paraphrase écrites par un modèle d'une autre lignée : elles passeront par Argon, sous le plafond accordé et après la contre-lecture du script d'appel. D'ici là, les 30 paraphrases viennent des mots de Lazar aux registres.
- Le script de résolution des citations : à écrire (classe B, instrument), puis à contre-lire.
- Les chaînes-canaris (porte 1) : en attente, voir ci-dessus.
