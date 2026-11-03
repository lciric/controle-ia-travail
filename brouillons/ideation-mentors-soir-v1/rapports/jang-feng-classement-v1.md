# Classement D : question de Shi Feng et Eyon Jang (valeur et limites des moniteurs et des méthodes d'audit en boîte blanche), v1

Classeur neuf D, 3 novembre 2026. Heures lues par `date -u` : début 17:29:18, notes écrites vers 17:34, paires de 17:36:25 à 17:38:26, script passé à 17:41:45, ce fichier écrit à partir de 17:42:02.
Consigne : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/soir-classeur-D-jang-feng-v1.md`, sha256 `26d6e5e5…7b156`, vérifiée.
Entrées vérifiées par empreinte : fiches `79c0befdf57fa2b4e9a2bc897cda9450f8c3489b2f05829c6e047f95a313a1c5` ; moisson `a75181969cf82b1586a64b1d642f8e9dc06afb06e8eb172a91720040b7e2d0c3` ; protocole du soir `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`. Sans empreinte attendue (relevée seulement) : protocole Heimersheim v1 `942b93241b6e033e34cc7cb035fe1d70f6e944a8a98bc4c556b83b0d7fdbad18` ; pièce `1f42364322988bf591ead6ce41842dd389ab179b11bc27853d66750ab5196774`.

**En tête : pas de témoin déguisé (échéance) : l'axe d'originalité n'est pas contrôlé** (protocole du soir, § 2). En plus, la moisson classe les 29 fiches « voisin, proche » : l'originalité vaut 1 partout et ne départage rien.

## 1. Ordre final (les huit)

| Rang | Identifiant | Log-force (pénalité 0,25) | Victoires sur 14 | Notes (originalité / testable / prolonge = somme) | Drapeau de risque |
|---|---|---|---|---|---|
| 1 | JF-28 | +3,297 | 14 | 1 / 3 / 3 = 7 | oui |
| 2 = | JF-10 | +1,671 | 11 | 1 / 3 / 3 = 7 | non |
| 2 = | JF-06 | +1,671 | 11 | 1 / 2 / 3 = 6 | oui |
| 4 | JF-14 | +0,365 | 8 | 1 / 2 / 3 = 6 | non |
| 5 = | JF-21 | −1,255 | 4 | 1 / 3 / 3 = 7 | oui |
| 5 = | JF-26 | −1,255 | 4 | 1 / 3 / 3 = 7 | oui (léger) |
| 5 = | JF-19 | −1,255 | 4 | 1 / 2 / 3 = 6 | non |
| 8 | JF-18 | −3,239 | 0 | 1 / 2 / 3 = 6 | non (c'est la direction annoncée du mentor) |

Ordre strict : **JF-28, JF-10, JF-06, JF-14, JF-21, JF-26, JF-19, JF-18**. Les « = » sont des forces exactement égales ; l'ordre strict y vient de la règle de départage (§ 4) : JF-10 avant JF-06 par la somme des notes (7 contre 6) ; JF-21 et JF-26 devant JF-19 par la somme ; JF-21 avant JF-26 au tirage.

## 2. Porte

29 fiches sur 29 dans le sujet : toutes portent sur la valeur ou les limites d'un moniteur ou d'une méthode d'audit qui demande plus que la boîte noire (activations, poids, affinage). Cas limites gardés : JF-15 (direction lisible sans valeur causale, marginal pour l'audit) ; JF-10, JF-27, JF-29 (élicitation par affinage, comptée comme accès aux poids ; JF-27 serait boîte noire si ses démonstrations étaient données dans le contexte).
Les réfutations que la moisson propose « au directeur de trancher » (JF-07, JF-12, JF-15, JF-17, JF-20, JF-25) ne sont pas tranchées ici : fiches gardées, propositions signalées. Aucune n'est dans les huit. Doublon de structure probable signalé par la moisson : JF-24 et JF-23 (non fusionnées ici, ce n'est pas l'étape D).

## 3. Notes des 29 fiches (raisons d'une ligne dans `notes-v1.json`)

Ancres de Heimersheim (§ 5). *Originalité* : classe de la moisson seule. *Testable* : 3 = protocole clair avec seuil en 5 jours ou moins selon la fiche ; 2 = 6 à 14 jours ; 1 = plus de 14 jours ou flou ; borne haute si la fiche donne une fourchette ; un point retiré à JF-12 (son organisme non verbalisant est renvoyé aux travaux futurs par 2604.28182 § 6.2). *Prolonge* : travaux de la section 1 de la pièce seulement (flux de l'hiver 2027, 2604.28182, 2411.17693, 2409.12822).

| Id | Orig. | Test. | Prol. | Somme | Moisson (+ / = / −) | Risque |
|---|---|---|---|---|---|---|
| JF-01 | 1 | 1 | 3 | 5 | = | non |
| JF-02 | 1 | 3 | 0 | 4 | = | non |
| JF-03 | 1 | 1 | 3 | 5 | = | non |
| JF-04 | 1 | 3 | 0 | 4 | = | non |
| JF-05 | 1 | 3 | 1 | 5 | − | non |
| JF-06 | 1 | 2 | 3 | 6 | = | oui |
| JF-07 | 1 | 3 | 1 | 5 | − | non |
| JF-08 | 1 | 1 | 3 | 5 | + | oui |
| JF-09 | 1 | 1 | 3 | 5 | + | non |
| JF-10 | 1 | 3 | 3 | 7 | = | non |
| JF-11 | 1 | 2 | 0 | 3 | = | non |
| JF-12 | 1 | 2 | 3 | 6 | − | oui |
| JF-13 | 1 | 1 | 1 | 3 | + | non |
| JF-14 | 1 | 2 | 3 | 6 | + | non |
| JF-15 | 1 | 2 | 0 | 3 | − | non |
| JF-16 | 1 | 2 | 0 | 3 | = | non |
| JF-17 | 1 | 2 | 3 | 6 | − | non |
| JF-18 | 1 | 2 | 3 | 6 | + | non |
| JF-19 | 1 | 2 | 3 | 6 | + | non |
| JF-20 | 1 | 2 | 2 | 5 | − | non |
| JF-21 | 1 | 3 | 3 | 7 | = | oui |
| JF-22 | 1 | 3 | 0 | 4 | − | non |
| JF-23 | 1 | 1 | 3 | 5 | + | non |
| JF-24 | 1 | 2 | 3 | 6 | = | non |
| JF-25 | 1 | 2 | 0 | 3 | − | non |
| JF-26 | 1 | 3 | 3 | 7 | = | oui (léger) |
| JF-27 | 1 | 2 | 2 | 5 | = | non |
| JF-28 | 1 | 3 | 3 | 7 | = | oui |
| JF-29 | 1 | 1 | 0 | 2 | + | non |

## 4. Choix des huit et départages

- Somme 7 : JF-10, JF-21, JF-26, JF-28. Somme 6 : sept fiches pour quatre places (JF-06, JF-12, JF-14, JF-17, JF-18, JF-19, JF-24).
- L'originalité (règle du protocole) ne départage pas : 1 partout. **Règle ajoutée après lecture des notes**, parce que le protocole n'avait pas prévu une originalité uniforme : (2) sous-lecture de la seule entrée de moisson de la fiche, « + » si elle dit le cœur ou une part distinctive non trouvée, « − » si elle propose une réfutation (même partielle) ou dit l'énoncé central déjà publié, « = » sinon ; (3) note « testable » ; (4) tirage `default_rng(SeedSequence(e).spawn(1)[0])`, e = 8773222072072512180.
- Appliquée : « + » JF-14, JF-18, JF-19 entrent ; « = » JF-06 et JF-24, testable 2 et 2, tirage [0, 1] : JF-06 entre, JF-24 sort ; « − » JF-12, JF-17 sortent. **Juste sous la coupe : JF-24, JF-12, JF-17.**
- Égalités de force à la fin : somme des notes, puis originalité, puis sous-lecture, puis tirage `default_rng(SeedSequence(e, spawn_key=(1,)))` (codé dans le script avant son passage, mais après lecture des jugements).

## 5. Paires, Bradley-Terry, cohérence

- 56 jugements (28 paires × 2 ordres), présentés dans l'ordre `default_rng(SeedSequence(e)).permutation(56)`, e = entier des 16 premiers hexadécimaux du sha256 des fiches (`79c0befdf57fa2b4`). Écrits par lots de 7 au fil de la présentation, avec l'heure du lot (`paires-v1.jsonl`).
- **Erreur trouvée par la garde au premier passage du script** : au rang 53, j'ai écrit l'indice 45 au lieu de 44 (A, B et gagnant justes). `paires-v1.jsonl` n'est pas réécrit ; la correction est déclarée dans le script (`CORRECTIONS_DECLAREES` : seul le champ « indice » est corrigeable, valeur lue contrôlée, rendu du plan contrôlé), appliquée et consignée dans la sortie. Défaut mineur : les 7 premières lignes portent une heure entre guillemets doublés (`"\"17:36:25\""`).
- Script `bradley_terry_jang_feng_v1.py` (numpy 2.5.3, sans modèle) : 30 épreuves sur 30 tenues avant tout calcul. Cas sains : ordre parfait connu retrouvé, cohérence 1 et réserve « presque parfait » déclenchée ; ordre avec paires voisines partagées, cohérence 21/28 et réserve « sous 0,8 » déclenchée, gradient nul ; forces simulées retrouvées à moins de 0,15. Artefacts refusés : doublon, jugement manquant, gagnant hors paire, identifiant inconnu, A = B, ordre inversé, lignes hors de l'ordre des rangs, champ absent, graine fausse, JSON invalide, ligne vide, non-convergence forcée, pénalité négative, faute d'indice non déclarée, corrections fausses ou portant sur le gagnant ; ajustement non pénalisé refusé quand l'estimateur n'existe pas.
- **L'estimateur non pénalisé n'existe pas** (JF-28 n'a perdu aucune comparaison, JF-18 n'en a gagné aucune) : forces pénalisées (pénalité 0,25 sur les log-forces, comme un a priori normal de variance 4), à lire comme un ordre ; ordre identique pour les pénalités 0,05, 0,25 et 1,0.
- **Cohérence : 27 paires sur 28, soit 0,964.** Paire discordante : JF-06 contre JF-10 (JF-06 au rang 52, JF-10 au rang 54) ; c'est elle qui décide la deuxième place, et elle finit à égalité.
- **Réserve** : cohérence presque parfaite d'un juge unique. Elle mesure la constance d'un seul jugement, pas son exactitude : un juge qui se souvient de ses choix concorde par construction.
- Biais de position : le premier présenté gagne 29 fois sur 56.
- Triplet intransitif : JF-19 > JF-26, JF-26 > JF-21, JF-21 > JF-19 (chacun 2 à 0). D'où l'égalité exacte des trois.

## 6. Drapeaux de risque devant ce mentor (les huit)

- **JF-28 : oui.** Elle affirme que le bruit de 2604.28182 § 4.1 n'a pas de témoin bénin apparié. C'est une critique directe du papier de Jang, appuyée sur une lecture partielle (la pièce dit l'avoir lu par questions ciblées à un petit modèle) : à vérifier sur le PDF avant de l'écrire.
- **JF-10 : non.** Elle s'appuie sur 80,0 → 98,0 % en 10 pas (2604.28182 § 4.2) dans son sens, et prive le juge boîte noire de chaîne de pensée, ce qui respecte § 6.2. Il faut le dire explicitement.
- **JF-06 : oui.** La référence « 80 actions nuisibles, 98,4 % d'utilité, 10 000 tâches » vient du réglage de 2411.17693 ; la pièce ne dit pas quels modèles y servent. Si le modèle non fiable y est fermé, il n'a pas d'activations et la référence doit être remesurée sur un modèle ouvert. Un coauteur le verra (à vérifier).
- **JF-14 : non.** La moisson note que le centrage est une technique ancienne : la nouveauté tient à l'application.
- **JF-21 : oui.** Elle calibre sur des épisodes honnêtes seulement, alors que 2411.17693 (pièce § 3, p. 4 et p. 7) exige les lois des scores sur sorties malveillantes et non malveillantes. Elle présente aussi le macro-protocole bayésien comme un filtre à seuil. Elle repose enfin sur la banque P3, interne au programme.
- **JF-26 : oui (léger).** Elle affirme ce que 2604.28182 n'a pas fait (bruit sur organismes distillés seulement), sur la même lecture partielle.
- **JF-19 : non.**
- **JF-18 : non** pour la contradiction, mais c'est la direction 1 annoncée par les mentors. À présenter comme leur direction prolongée, pas comme une idée neuve.
- Hors des huit, drapeau « oui » : JF-08 (« boîte noire aveugle » contre 2604.28182 § 6.2) ; JF-12 (présuppose l'organisme non verbalisant que 2604.28182 § 6.2 renvoie aux travaux futurs).

## 7. Réserves

1. L'originalité est uniforme et non contrôlée par un témoin. Les huit et leur ordre reposent donc sur « testable » et « prolonge », puis sur les paires.
2. Les règles de départage ont été fixées après lecture des notes. Elles décident les quatre dernières places parmi sept, et les égalités finales.
3. Un juge unique (moi) pour les notes et les paires, d'où une cohérence presque parfaite (réserve du § 5).
4. Les coûts « testable » sont ceux des fiches, tous « supposés ». La pièce ne dit pas si les organismes Qwen3-14B de 2604.28182 sont publics (JF-10, JF-14, JF-18, JF-19, JF-26, JF-28 en dépendent).
5. Aucun appel d'outil n'a demandé d'approbation ; aucune recherche sur le web, aucun `git`, aucun `.sha256`, aucun fichier existant modifié, rien lu sous `lecteur-A/`, `pour-lazar/`, `/tmp/soir-tours-v1/`, `/home/claude/coffre-*`, ni la clé de préparation.
