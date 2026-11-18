# Contre-lecture de la matière première de l'auto-conception de l'organisme d'idéation — v1

Écrite le 18 novembre 2026 par un contre-lecteur neuf (R2), d'une autre lignée que les rédacteurs : je n'ai écrit aucune des pièces lues. Aucune dépense, aucun appel de modèle externe, aucune clé, aucun contact, aucun commit, aucune poussée, aucun clone. Aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis n'a été ouvert. Demande d'origine : R-3209 et R-3211 de `registres/decisions.md` (« go pour les deux » ; « donne-lui en matière première le moissonnage de tous les articles sur l'optimisation de la recherche exploratoire des idées et leur test »).

## 0. Verdict

**À refaire** pour les deux pièces demandées : le catalogue `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v1.md` et le relevé `docs/notes/matiere-premiere-auto-conception-v1/releve-mecanismes-v1.json` **n'existent pas sur disque** (vérifié par `ls`, par `find /` sur les deux noms, et dans l'historique git de toutes les branches : aucun ajout de ces noms). La tâche transmise porte « Rédacteur du catalogue : null » : le rédacteur n'a rien rendu. Je ne peux donc ni valider ni corriger ces deux pièces, et je n'écris **aucune v2** : il n'y a pas de v1 à corriger.

Ce qui existe, ce sont les **vingt lots du relevé mécanisme par mécanisme** (`lots/lot-01.json` à `lots/lot-20.json`, empreintes compagnons toutes conformes à `sha256sum -c`). J'ai appliqué à ces lots, faute de mieux, toutes les épreuves demandées (quarante travaux tirés, comptes par programme, mécanismes oubliés dans dix travaux lus en profondeur, affirmations et absences). **Verdict sur les lots : à corriger** (liste en section 6). Le fond tient : sur quarante travaux tirés, aucun mécanisme inventé de toutes pièces, aucune empreinte fausse ; les défauts sont un trou de couverture (trente travaux non relevés, dont trois lus en profondeur), des étiquettes de profondeur incohérentes, des mécanismes « suggérés par le seul titre » mêlés aux mécanismes décrits, quatre gloses non sourcées, et une ligne qui reprend une facette d'une famille exclue.

## 1. Pièces lues et empreintes

| Pièce | Empreinte (sha256) |
|---|---|
| `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json` (630 travaux) | `aa3ac9b8e962c496b89f67051ef5c60094aa3d18405e8779ab3e34a33a6010d2` |
| `docs/notes/matiere-premiere-auto-conception-v1/lots/lot-01.json` … `lot-20.json` | compagnons `.sha256` conformes (20 sur 20) |
| `docs/notes/veille-exploration-idees-v1/lecture-03-v1.md` (sections 0 à 5.3 seulement, 5.4 non lue) | `2775dc89cfd1f68f27835a160c3988ff76d966ed94bfe9a357f2a5d4d2a70f3a` |
| `docs/notes/veille-exploration-idees-v1/lecture-huxley-godel-v2.md` (parties citées) | `cb8f9ea395901a7b1de3c588e97b1e3a56f4a78b233d19850e3e6456063907bd` |
| `docs/sources/pdf/veille-exploration-idees-v1/grise-openreview-resumes-retenus-v1.json` | `266ab71577fb0284d4375d55800f3e3b12df2f69a889bcf3c0642291999d402b` |
| `docs/sources/pdf/veille-exploration-idees-v1/adverse-arxiv-2609.33180v2.pdf` (p. 1 à 3) | `20639707e89ee9b13f5bfde4ad30902b3d6a4390ad1c50b737cc2012472ce164` |
| Lectures 02, 04, 05, 07, 08, 09, 12 de la veille (sections « ce que le travail fait » et « mesuré ») ; PDF `adverse-arxiv-2607.04108v1.pdf` (p. 1 à 4) et `grise-anthropic-taste-2026-08.pdf` (p. 1 à 3) par extraction de texte | compagnons au dépôt |

Toutes les empreintes citées dans les champs `source_dans_le_depot` des lots ont été recalculées par programme : **1 446 citations d'empreinte, toutes justes, aucun fichier absent**. 64 mécanismes (tous ceux du lot 04, indices 90 à 119) citent leurs sources **sans empreinte** (R6).

## 2. Comptes, recalculés par programme sur les lots

| Compte | Valeur |
|---|---|
| Travaux de la table fusionnée | 630 (911 entrées brutes, 923 après éclatement) |
| Travaux couverts par les lots | **600** (indices 0 à 599, chacun une seule fois) |
| Travaux non relevés | **30** (indices 600 à 629 : aucun lot 21) |
| Titres et adresses des lots alignés sur la table | 600 sur 600 |
| Marqués « exclue » (familles exclues), sans mécanisme | 18 |
| Marqués « hors sujet », sans mécanisme | 7 |
| Sans mécanisme et sans statut | 12 (216, 263, 264, 265, 282, 297, 306, 354, 356, 477, 478, 479) |
| Travaux portant au moins un mécanisme | 563 |
| Mécanismes au total | 1 054 |
| dont « famille suggérée par le seul titre » ou « d'après le titre » | 203 (169 « par le seul titre ») |
| Par famille | exploration 234, épreuve 219, jugement 162, mémoire 101, originalité 94, sélection 77, coût 74, auto-conception 53, **autre 40** |
| « Éprouvé contre le réel » | oui, mesuré 472 ; inconnu 402 ; oui, affirmé 112 ; non 68 |
| Profondeur déclarée | page ou résumé 351 ; notice seule 240 ; lecture approfondie sur PDF 9 |

Note : R-3211 parle de « 517 après fusion des doublons selon la couverture ». Le 517 est l'union de la strate A de `couverture-v1.json` (travaux annotés des quatre voies), pas un dédoublonnage de la table : les lots relèvent bien les 630 entrées de la table, sans fusion supplémentaire. Le catalogue devra dire lequel des deux nombres il compte.

## 3. Quarante travaux tirés au hasard

**Tirage.** Parmi les 582 travaux des lots non marqués « exclue », quarante sans remise, par `numpy.random.default_rng(numpy.random.SeedSequence(20261118)).choice(pool, 40, replace=False)` (pool = indices des lots dans l'ordre des fichiers lot-01 à lot-20, statut différent de « exclue »). Indices tirés : 17, 25, 27, 33, 45, 49, 55, 57, 72, 76, 154, 168, 173, 201, 218, 221, 229, 248, 289, 300, 302, 303, 305, 306, 327, 355, 362, 363, 380, 403, 404, 405, 427, 439, 442, 449, 532, 570, 579, 593.

**Méthode.** Pour chaque mécanisme attribué : comparaison au champ `fait` et `touche` de l'entrée de la table, puis aux lignes de la veille citées par `sources` (recherche par mots-clés, par citations, littérature grise, recherche adverse), puis, quand le lot cite une lecture ou un PDF, à cette lecture ou à ce PDF (texte extrait, chiffres cherchés).

**Résultat.** 40 travaux, 80 mécanismes relus.

- **Fidèles à l'entrée ou à la lecture citée** : 36 travaux sur 40. Les ajouts au-delà du champ `fait` se retrouvent dans les lignes de veille citées (25 : « trois familles de modèles, langue native, température élevée », ligne adverse 111 ; 27 : « trop peu d'essais indépendants », ligne adverse 56 ; 76 : « à l'aveugle », ligne adverse 142 ; 570 : résumé OpenReview versé, chiffres 1 943 et 10 172 retrouvés ; 579 : « 1 − α », « 20,7 % », retour réduit, trois sources de fausses promotions retrouvés p. 1 à 3 du PDF ; 593 : tirage de Thompson, agrégat de clade, α = 0,6, retrouvés dans la lecture de Huxley-Gödel ; 57 : relu contre la lecture 03, sections 0 à 5.3). Les mécanismes « suggérés par le seul titre » (289, 300, 302, 305, 327, 355, 362, 363, 380) sont marqués comme tels et ne prétendent à rien d'autre.
- **Gloses non sourcées, à retirer ou à marquer comme lecture du relevé** (4 travaux, aucune invention de résultat) :
  - 45 (*Sampling More, Getting Less*) : « non d'un manque de température » n'est ni dans l'entrée ni dans les deux lignes de veille.
  - 173 (*SLDBench v2*) : « l'agent choisit quelles mesures demander avant d'énoncer la loi (seconde version d'un banc existant) » et le mécanisme de coût « suppose une économie de mesures » sont tirés du titre, mais présentés comme description ; l'entrée dit seulement « découverte active de lois d'échelle par agents ».
  - 439 (*What survives honest evaluation?*) : « la correction est appliquée après coup » n'est dans aucune source citée.
  - 403 (*Navigating Epistemic Monocultures*) : « argument pour des proposeurs hétérogènes » est une lecture du relevé, non une affirmation des auteurs ; à marquer comme telle.
- **Cloisonnement** (57, *Selecting LLM-Generated Hypotheses…*) : le lot déclare la facette « optimisation d'un harnais contre un juge » exclue et non lue, mais garde un mécanisme « jugement » qui en reprend le chiffre (perte de précision d'un harnais optimisé pour la note d'un juge). Même tiré de la notice de la table, ce contenu relève de la famille exclue (attaque de Goodhart du juge) : **exclue** ; le catalogue ne doit pas le porter. Je ne l'ai pas lu au-delà de la phrase du lot.

## 4. Mécanismes oubliés dans dix travaux lus en profondeur

Travaux : 57, 98, 112, 121, 136, 258, 450, 456, 581, 593 (les neuf étiquetés « lecture approfondie sur PDF », plus 136, relu par le lot sur PDF p. 1 à 4). Comparaison des mécanismes du lot aux sections « ce que le travail fait » et « mesuré » des lectures du dépôt, et aux PDF extraits.

| Travail | Verdict | Oublis relevés (affirmations des auteurs selon la lecture citée) |
|---|---|---|
| 57 (lecture 03, hors 5.4) | complet | — (voir la ligne exclue, section 3) |
| 98 (lecture 12) | presque complet | jeux publics servis sous des noms neutres contre la contamination (p. 13) |
| 112 (lecture 08) | **incomplet** | séparation signal public vu par l'agent / note privée retenue dans la boucle intérieure ; relecteur modèle qui extrait le score public des sorties (p. 4) ; politique de recherche par bandit, compression du contexte et garde-fous, décrits sans ablation (p. 13) ; diversité du banc de sélection posée comme moteur de généralité, affirmée non testée (p. 3) |
| 121 (lecture 04) | complet | — |
| 136 (PDF p. 1 à 4) | complet | chiffres retrouvés dans le texte extrait (0,045, 0,200, 0,959, 73,2 %, 49,2 %, 165 à 169) |
| 258 TASTE (PDF public p. 1 à 3) | complet sur ce qui est lu | **étiquette de profondeur excessive** : la précision du lot dit « pages 1 à 3 relues, aucune note de lecture approfondie au dépôt », non « lecture approfondie » ; source = PDF public `grise-anthropic-taste-2026-08.pdf`, pas la pièce privée (`f9aed18c…` absente des lots) |
| 450 (lecture 02) | **incomplet** | engagement préalable : verdict et probabilité a priori consignés par l'agent avant tout accès aux données (p. 5) ; les trois modèles commerciaux affirment exactement quand leur probabilité déclarée atteint un demi, 3 990 lancements sur 3 990 (p. 18) |
| 456 (lecture 09) | presque complet | rotation de la fenêtre d'échecs : les cas résolus sortent de la liste, de nouveaux échecs entrent (mécanisme nommé par les auteurs, non séparé) ; réplique sur un second modèle |
| 581 (lecture 07) | complet | — |
| 593 Huxley-Gödel (lecture 05, lecture Huxley-Gödel v2) | **incomplet** | aucune ligne « épreuve » : juge = tests exécutables des bancs, transfert mesuré sur 207 tâches inédites de la même famille et sur un autre modèle (p. 9-10) ; resserrement en fin de budget et exécution asynchrone, nommés par la lecture 05 comme confondus avec l'agrégat de lignée |

**Trois travaux lus en profondeur au dépôt sont absents des lots**, parce qu'ils tombent dans les indices 600 à 629 non relevés : *Bad Genius* (605, lecture 10), *Beyond Symmetric Agents* (612, lecture 11), *MetaEvoForge* (625, lecture 06). Ce sont, avec le reste de la tranche (bancs d'auto-évolution, *Verbalized Sampling*, *The Ladder*, ShinkaEvolve…), des sources directes pour l'auto-conception : l'oubli est le plus lourd du relevé. Je n'ai pas lu ces trois lectures.

## 5. Affirmations présentées comme faits, absences présentées comme trous

- **Absences** : aucune ligne des lots ne présente une absence comme un trou du champ (recherche par motifs : « aucun travail », « zone vierge », « jamais étudié », « premier à », « libre », « lacune du champ » : zéro). L'usage constant est « non précisé par la notice », qui dit une limite de la lecture, non du champ (R8 respectée).
- **Affirmations** : les chiffres sont presque partout attribués (« selon les auteurs », page citée, « d'après la notice »). Recherche par programme des mécanismes chiffrés sans aucune marque d'attribution ni avertissement au niveau de l'entrée : un seul cas, 85 (lot 03 : « tous à p ajustée ≥ 0,56 »), à marquer « selon les auteurs ».
- **Étiquette « oui, mesuré »** : elle veut dire « les auteurs disent avoir mesuré », non « vérifié par nous ». Le catalogue doit l'écrire dans sa légende ; sinon 472 lignes se liraient comme des faits établis. Sept travaux portent « oui, mesuré » quand la table dit « inconnu » ou « affirmé sans mesure » : 121, 581, 593 (lectures approfondies, justifié), 136 (PDF p. 1 à 4, justifié), 569 (résumé OpenReview versé, justifié et dit), 233 et 582 (justifiés par « selon les auteurs » et par la lecture 07).
- **Lots sans avertissement R7 au niveau de l'entrée** : le lot 04 n'a ni `precision_de_lecture` ni `mesure_selon_la_table` ni empreintes ; le lot 20 n'a pas `precision_de_lecture`. Les phrases y sont attribuées une à une, mais l'entrée ne dit pas la profondeur réelle.

## 6. Corrections demandées

Aux pièces à écrire (catalogue et relevé), qui partiront des lots :

1. **Couvrir les indices 600 à 629** (un lot 21), dont les trois travaux lus en profondeur (605, 612, 625). Sans cela, le catalogue ne couvre pas « tous les articles ».
2. **Unifier la profondeur** : une entrée relevée d'après la table « résumé ou page » est « page ou résumé » partout ; les lots 01, 02 et 18 la notent « notice seule » (81 entrées). TASTE (258) passe de « lecture approfondie sur PDF » à « page ou résumé, PDF p. 1 à 3 ».
3. **Séparer les 203 mécanismes « suggérés par le titre »** des mécanismes décrits : comptés à part, jamais additionnés aux 1 054 dans un compte de mécanismes du champ.
4. **Familles fermées** : reclasser ou justifier les 40 « autre » (hors des huit familles de R-3211) ; normaliser l'écriture des familles (« originalité » accentuée, les autres non) avant tout compte.
5. **Retirer ou marquer** les gloses de 45, 173, 403, 439 (section 3), et attribuer la phrase chiffrée de 85.
6. **Retirer la ligne « jugement » de 57** qui reprend la facette exclue (attaque de Goodhart du juge) ; noter « exclue » seulement.
7. **Ajouter les oublis** de 112, 450, 593 (et, s'ils servent, 98 et 456), tableau de la section 4.
8. **Empreintes** pour les 64 mécanismes du lot 04 (R6) ; champs de précision de lecture pour les lots 04 et 20.
9. **Légende** : « oui, mesuré » = mesure affirmée par les auteurs, non vérifiée par le programme ; toute entrée sur notice ou résumé, non opposable (R7) ; toute absence = question (R8).
10. **Les douze entrées sans mécanisme ni statut** (section 2) : leur donner un statut (« hors sujet », « liste sans mécanisme », « notice muette ») pour que le compte se ferme.

## 7. Ce que cette contre-lecture ne fait pas

Elle ne juge pas le catalogue ni le relevé, qui n'existent pas. Elle n'a rouvert aucun PDF au-delà des pages citées pour 136, 258 et 579. Elle n'a lu ni la section 5.4 de la lecture 03, ni les lectures 01, 06, 10, 11, ni aucun contenu des dix-huit entrées marquées « exclue ». Le tirage porte sur les lots tels qu'ils sont ; un lot 21 devra être relu à part.
