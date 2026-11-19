# Audit de symétrie (règle R4) du rejeu à blanc des critères de sélection v2, course v9 — v1

- **Auditeur** : modèle O, neuf. Je n'ai écrit ni les critères v2, ni les deux rejeux, ni leur contre-lecture, ni aucune carte. Mandat de la mère (R-3876). Écrit le 2026-11-19 (`date -u` : 2026-11-19T14:31:25Z). Hors ligne, processeur seul, aucune dépense, aucun appel de modèle.
- **Signal audité** (contre-lecture `contre-lecture-juge-v2-criteres-v2-rejeux-v1.md`, sha256 `c75a9abc40e3dd8fef5e17ac9cae61bc7d6f0fa53bc375358e6ad344ea34bc95`, constats 5 et 12) : dans l'assemblage des deux rejeux, aucune des 28 cartes à 12 n'est attribuée par les lignes GO à Astra, Argon ou Opus. Les deux seules cartes de veto dont l'espèce était connue sont de la famille des lecteurs.

## Verdict

1. **Famille des lecteurs.** L'étiquette « auteur de la famille Opus ou Fable » prédit la note 12 bien au-delà du hasard. Sur les 62 cartes notées dont la famille est connue, 11 sur 16 cartes de la famille sont à 12, contre 1 sur 46 hors de la famille (p ≈ 5·10⁻⁵, plancher de 20 000 permutations). Aucun trait de surface mesuré n'en rend compte. Le meilleur, la longueur, explique 27 % de la variance de « à 12 » sur les 92 cartes ; à traits tenus, la famille ajoute encore 23 points de R², les traits n'en ajoutent que 5 à famille tenue.
2. **Le canal est un seul lecteur et un seul critère : le D du lecteur F.** Le lecteur O met 6 presque partout ; sa note ne varie pas avec la famille (6,00 contre 5,93, p = 0,57). Le mécanisme reste **indéterminé**. Ce peut être une préférence pour soi, par reconnaissance du style ; ce peut être aussi une manière d'écrire l'issue « non » propre à la famille, que D récompense. Deux lecteurs de la même famille ne peuvent pas les séparer.
3. **Plus fort qu'au hasard, sous toutes les hypothèses permises sur les 32 cartes d'espèce inconnue.** Tirage des inconnues selon les totaux par espèce : p ≤ 0,010 dans 400 tirages sur 400. Pire cas, où toutes les inconnues hors famille sont à 12 : 16 sur 35 contre 12 sur 57, écart +0,25, p = 0,012. Veto : les 4 titulaires d'espèce connue sont dans la famille, p = 0,024 contre la part de base (37 sur 94), mais ce compte n'est pas indépendant de la note (§ 5).

Limite principale : l'espèce n'est connue que pour 62 cartes sur 94, dont 9 au seul niveau de la famille. Les étiquettes viennent de listes de décision, non d'un tirage. Le contrôle par statut (§ 4) atténue ce défaut sans l'effacer.

## 1. Pièces et empreintes

| pièce | chemin | sha256 |
|---|---|---|
| sélections F | `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/selections-rejeu-a-blanc-criteres-v2-lecteur-f-v1.json` | `e42b5f05d0f9b2c8423fc0d005e5d5c414c1023208e049201074ecf91ec69fc6` |
| sélections O | `…/juge-selection/selections-rejeu-a-blanc-criteres-v2-lecteur-o-v1.json` | `8bd435b98f1b81abf3a4e201977b2b1bf9a72cbe464dfb9127243d1a93e0b7d3` |
| notes des deux rejeux (lues) | `…/rejeu-a-blanc-criteres-v2-lecteur-f-v1.md`, `…-lecteur-o-v1.md` | `5d8d537a…`, `209243b7…` |
| cartes, champ `contenu` seul, par programme | `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json` | `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481` |
| espèces (mère, sur `main`) | `docs/notes/organisme-auto-conception-v1/course-v2/especes-et-originalite-cartes-v9-v1.md` | `2af9e67fce5b8edb3a3cc197347ab35f08e5f1731f5dcc3b3ef11c1fc6c44beb` |
| relecture sans espèce (mère, sur `main`) | `docs/notes/organisme-auto-conception-v1/course-v2/cartes-reexaminees-cout-non-limitant-v9-v1.md` | `de7ed04d06903c507ace3a16130fccf9f22d88e6e16143c3f8f3e0530837d063` |
| lignes GO-55 à -63 | `registres/go.md` sur `main` (commits `a49fa5b1` et `7dcd6a44`, contenu identique) | `72e52540c4b25997d0aa6057ea880bdc765e0cd09c5650b65a0b084da174f558` |
| littérature (recommandations) | `docs/notes/organisme-auto-conception-v1/juge/litterature-juges-preference-pour-soi-v1.md` sur `main` | `bb54b685dfcec23b0c6ec6813dc87385ea1cebac1ed311319e190183bce8bac9` |
| programme | `…/juge-selection/audit_symetrie_rejeu_v2_v1.py` | compagnon `.sha256` |
| sortie | `…/juge-selection/audit-symetrie-rejeu-v2-sortie-v1.json` | compagnon `.sha256` |

- Le programme vérifie les six empreintes d'entrée avant tout calcul et s'arrête sur un écart. Il vérifie aussi que chaque identifiant d'espèce figure dans la ligne GO ou la pièce qu'il cite.
- Le champ `meta` n'a jamais été lu. Le champ `contenu` n'a été que compté ; aucun texte de carte n'a été affiché ni écrit.
- Graines (R9) : `numpy.random.SeedSequence(int(sha256("audit-symetrie-rejeu-v2-v1")))`, `spawn(6)`, numpy 2.5.3. Deux exécutions donnent les mêmes résultats.
- Non ouverts : `diag/`, `donnees/`, coffre, verdicts de juges, classement, conservation des réponses, journaux des relais, bras d'attaque.
- Assemblage, selon la lettre rappelée par la contre-lecture : somme des deux totaux ; exclusion quand les deux lecteurs la voient (`fafa0062508c9`, `fefca0bd94064`). Sur 92 cartes notées : 28 à 12, 60 à 11, 2 à 10, 2 à 9. C'est le compte de la contre-lecture.

## 2. Couverture de l'espèce, et sa limite

| origine | cartes | détail |
|---|---|---|
| nommées par GO-57, -59, -61, -63 | 44 | Astra 12, Argon 16, Carbon 10, Opus 3, Fable 3 |
| nommées par la pièce `2af9e67f…`, § (b) et (c) | 9 | Astra 5 (`f319823a86ea7`, `f9c8c39740352`, `fbae5b702558e`, `f2e3582b5fa97`, `f4cbf7e62ff7b`), Argon 2 (`f1373c384a771`, `f7b38afebd589`), Carbon 1 (`fe887ca5cb62c`), Fable 1 (`fcfa3d98b90f8`) |
| déduites, famille seulement (Opus ou Fable) | 9 | voir ci-dessous |
| inconnues | 32 | dont 2 exclues ; d'après les totaux, il reste parmi elles Astra 3, Argon 3, Carbon 5 et famille 21 |

**Déduction des neuf cartes de famille.** La pièce `2af9e67f…`, § (a), donne les porteuses des huit lignes retenues : Opus 4, Fable 2, Astra 1, Carbon 1. Elle donne aussi les trois instruments transversaux : Opus 2, Fable 1. GO-55 et GO-56 nomment ces porteuses et ces instruments. La porteuse Astra est `f89c771e3ac68` (GO-59), la Carbon `f7782e931911d` (GO-57). Les six autres porteuses et les trois instruments sont donc Opus ou Fable : six Opus et trois Fable, sans savoir lesquels. Ce sont `f169420b8d1d8`, `fcc96538bff00`, `fb3a2cc87251c`, `f856659046065`, `f5373a31410ab`, `f8c05bffe7cb1`, `f6e7646851ba5`, `fc36c3c3125ac` et `fd688912a8667`.

La pièce `de7ed04d…` ne donne l'espèce d'aucune carte.

**Couverture : 53 cartes nommées et 9 de famille, soit 62 sur 94 au niveau de la famille ; 32 inconnues.** Cela impose trois limites.
- Les étiquettes ne sont pas tirées au hasard : elles suivent les listes que la mère a données à Lazar. Côté famille, les neuf déduites sont des porteuses de lignes retenues par la proposition v1, dont le C5 est l'ancêtre de D. Le § 4 contrôle ce statut.
- La famille est surtout connue par déduction : 16 cartes, dont 7 nommées.
- Les 32 inconnues comptent 21 cartes de la famille : les bornes et les tirages du § 3 en tiennent compte.

## 3. Espèce × note

Assemblée (somme 0 à 12), par lecteur (total 0 à 6), et D du lecteur F.

| espèce | n | somme 12 / 11 / 10 / 9 | total F 6 / 5 / 4 | total O 6 / 5 | D de F 2 / 1 |
|---|---|---|---|---|---|
| Astra | 17 | 0 / 14 / 1 / 2 | 0 / 15 / 2 | 14 / 3 | 0 / 17 |
| Argon | 18 | 0 / 18 / 0 / 0 | 0 / 18 / 0 | 18 / 0 | 0 / 18 |
| Carbon | 11 | 1 / 10 / 0 / 0 | 1 / 10 / 0 | 11 / 0 | 1 / 10 |
| Opus | 3 | 0 / 3 / 0 / 0 | 0 / 3 / 0 | 3 / 0 | 0 / 3 |
| Fable | 4 | 3 / 1 / 0 / 0 | 3 / 1 / 0 | 4 / 0 | 3 / 1 |
| Opus ou Fable (déduites) | 9 | 8 / 1 / 0 / 0 | 8 / 1 / 0 | 9 / 0 | 8 / 1 |
| inconnue | 30 | 16 / 13 / 1 / 0 | 16 / 14 / 0 | 29 / 1 | 18 / 12 |

- Le lecteur O ne sépare rien par espèce : il donne 6 à 88 cartes sur 92. Tout l'écart passe par le D du lecteur F (contre-lecture, constat 5).
- Les cartes nommées seules opposent Fable (3 sur 4 à D = 2) à Opus (0 sur 3) : cela irait dans le sens de la lignée du lecteur F. Mais les neuf déduites comptent six Opus, et 8 sur 9 sont à 12 : au moins cinq cartes Opus sont donc à 12. Le signal tient au niveau de la famille, non de la seule lignée.

**Test de permutation de l'étiquette de famille.** Statistique : part à 12 dans la famille moins part à 12 hors de la famille ; test bilatéral ; 20 000 permutations.

| ensemble | famille à 12 | autres à 12 | écart | p |
|---|---|---|---|---|
| 62 cartes étiquetées | 11 / 16 | 1 / 46 | +0,67 | 5·10⁻⁵ (plancher) |
| 53 nommées seules | 3 / 7 | 1 / 46 | +0,41 | 0,0064 |
| 62, permutation dans la voie du lecteur F | idem | idem | +0,67 | 5·10⁻⁵ |
| 62, permutation dans la strate du lecteur F | idem | idem | +0,67 | 5·10⁻⁵ |
| 62, permutation dans le statut « ligne retenue v1 » (§ 4) | idem | idem | +0,67 | 5·10⁻⁵ |
| 94, inconnues tirées selon les totaux (400 tirages × 500 permutations) | 17 à 26 | | +0,29 à +0,67, médiane +0,49 | 0,002 à 0,010 ; 100 % sous 0,05 |
| 94, pire cas pour la famille | 16 / 35 | 12 / 57 | +0,25 | 0,012 (hypergéométrique, unilatéral) |

## 4. Confusion par le mode d'étiquetage

Statut « dans une ligne retenue » : il est connu seulement par GO-57, GO-59 (« déjà dans les lignes retenues ») et la pièce `2af9e67f…`.

| statut | famille à 12 | autres à 12 |
|---|---|---|
| dans une ligne retenue | 9 / 10 | 1 / 16 |
| autre | 2 / 6 | 0 / 30 |

À statut égal, l'écart demeure dans les deux strates. Il ne vient donc pas de ce que les cartes de famille étiquetées seraient les « meilleures » de la proposition v1 : les cartes Carbon, Argon et Astra déjà retenues n'ont, elles, qu'une carte à 12 sur 16.

## 5. Veto

| lecteur | titulaires | suppléantes |
|---|---|---|
| F | `f51c0935052f6` inconnue ; `f6e7646851ba5` famille (déduite) ; `f169420b8d1d8` famille (déduite) | `fed7a993d9671` inconnue ; `f562951db6c70` Opus |
| O | `f76714f1ddda4` Fable ; `fed7a993d9671` inconnue ; `f562951db6c70` Opus | `f4250eb75fbba` Carbon ; `f6e7646851ba5` famille (déduite) |

- Les 4 titulaires d'espèce connue sont dans la famille. Probabilité binomiale d'au moins 4 sur 4 : 0,024 contre la part de base sur 94 (37/94) ; 0,0044 contre la part parmi les étiquetées (16/62).
- **Réserve** : ce n'est pas un second signal indépendant. Les trois veto de F sont à 12 dans l'assemblage, donc à D = 2 chez F, et deux des quatre ne sont connus que par déduction. Le lecteur F dit croire ses trois veto de sa propre famille. Le lecteur O ne reconnaît pas de lignée, mais il reconnaît des familles de style.

## 6. Traits de surface × note

Traits déclarés dans le programme avant tout calcul. Corrélation avec « à 12 » sur 92 cartes ; p par 5 000 permutations ; r² = part de la variance de « à 12 » expliquée par le trait seul. La dernière colonne donne la corrélation du trait avec la famille, sur les 62 cartes étiquetées.

| trait | moyenne à 12 | moyenne sous 12 | r | r² | p | r avec la famille |
|---|---|---|---|---|---|---|
| longueur totale (caractères) | 5 427 | 4 519 | +0,52 | 0,271 | 0,0002 | +0,55 |
| longueur de « ce qui la réfuterait » | 465 | 400 | +0,39 | 0,155 | 0,0004 | +0,28 |
| champs remplis | 10,0 | 10,0 | 0 | 0 | 1 | 0 |
| identifiants de nœuds `N-ddd` cités | 2,64 | 1,98 | +0,14 | 0,021 | 0,18 | +0,07 |
| identifiants distincts | 1,25 | 0,84 | +0,20 | 0,039 | 0,078 | +0,15 |
| années citées (travaux) | 0,57 | 0,14 | +0,21 | 0,046 | 0,031 | −0,08 |
| « et al » | 1,43 | 1,52 | −0,02 | 0,000 | 0,86 | −0,22 |
| « non vérifié » | 5,68 | 7,41 | −0,17 | 0,028 | 0,11 | −0,27 |
| « prédit » | 2,18 | 2,50 | −0,08 | 0,007 | 0,45 | −0,06 |
| « prédiction » | 0,32 | 0,78 | −0,15 | 0,024 | 0,16 | −0,15 |
| gras | 0,00 | 0,88 | −0,15 | 0,024 | 0,24 | −0,13 |
| « budget égal », « apparié » | 1,61 | 1,72 | −0,04 | 0,001 | 0,77 | −0,18 |
| « pourquoi cela compte » | 0,14 | 0,03 | +0,21 | 0,043 | 0,065 | +0,50 |
| mots par phrase | 15,4 | 16,9 | −0,17 | 0,028 | 0,11 | −0,18 |
| « suffit » dans « ce qui la réfuterait » | 0,18 | 0,08 | +0,13 | 0,018 | 0,35 | −0,07 |
| « base » dans le même champ | 0,36 | 0,56 | −0,17 | 0,030 | 0,15 | +0,03 |
| « abandon », « retirer », « couper » dans le même champ | 1,07 | 0,91 | +0,12 | 0,015 | 0,28 | +0,10 |

Traits par catégorie : η² = part de la variance de « à 12 » entre modalités ; 5 000 permutations.

| trait | η² | p | η² avec la famille | à 12 par modalité |
|---|---|---|---|---|
| voie (lecteur F) | 0,084 | 0,018 | 0,150 | I 4/13, N 5/35, P 19/44 |
| strate (lecteur F) | 0,198 | 0,003 | 0,199 | P (a) 4/4, P (e) 4/6, P (c) 7/25, N 5/35 |
| voie (lecteur O) | 0,069 | 0,041 | 0,098 | I 4/14, N 1/17, P 23/61 |
| strate (lecteur O) | 0,105 | 0,078 | 0,158 | |
| axe déclaré par la carte | 0,059 | 0,24 | 0,083 | |
| **famille (62 étiquetées)** | **r² = 0,544** | voir § 3 | | |

**Modèles linéaires simples (probabilité linéaire, 62 cartes étiquetées).** Les trois traits les plus liés sont la longueur totale, la longueur de « ce qui la réfuterait » et les années citées.

| modèle | R² |
|---|---|
| famille seule | 0,544 |
| trois traits seuls | 0,364 |
| famille et traits | 0,591 |
| ce que la famille ajoute aux traits | **+0,227** (test de Freedman et Lane, 20 000 permutations : p ≈ 1·10⁻⁴) |
| ce que les traits ajoutent à la famille | +0,048 |

Lecture :
- La longueur est le seul trait de surface fort. Elle est elle-même liée à la famille (r = +0,55), et la pièce `2af9e67f…` décrit les cartes Fable comme « longues ». Elle n'explique qu'une petite part de l'effet de famille.
- Les citations, « non vérifié », « prédit », le nombre de champs et le gras n'expliquent presque rien (r² ≤ 0,05).
- La voie et la strate expliquent une part (η² jusqu'à 0,20), mais la famille y est aussi liée, et la permutation dans la voie ou la strate laisse l'écart intact.
- Le marqueur « pourquoi cela compte » est très lié à la famille (r = +0,50) et peu à la note : c'est un indice de style, non le canal.

## 7. Conclusion, sans revendication

- **Ce qui est établi, au niveau descriptif** : sur cette course et ces deux lectures, la note maximale suit la famille de l'auteur. Ce n'est ni la longueur, ni les citations, ni « non vérifié », ni les champs, ni la voie, ni la question. L'effet dépasse nettement le hasard, y compris dans le pire cas permis par les espèces inconnues.
- **Ce qui ne l'est pas** :
  - pourquoi D sépare les familles : reconnaissance et préférence, ou phrasé de l'issue « non » propre à la famille. Mes compteurs lexicaux ne captent pas ce phrasé ;
  - l'effet de la lignée seule : Fable 3 sur 4 contre Opus 0 sur 3, trop peu de cartes ;
  - toute généralisation hors de la v9. Une seule course, des étiquettes partielles et non tirées au hasard, deux lecteurs d'une même famille.
- Le signal est « trop propre » (11 sur 16 contre 1 sur 46). La règle R4 demande de le tenir pour une réserve sur toute proposition qui emploierait l'assemblage v2, non pour un fait sur les espèces.

## 8. Ce que le rejeu v3 doit contrôler

1. **Retirer le canal avant de mesurer.** Rétablir la parenthèse du C5 de la v1 dans D (« garder, retirer ou régler un module » ; contre-lecture, constat 5), scellée avant l'ouverture des cartes. Puis mesurer s'il reste un écart par famille. S'il n'en reste pas, le signal v2 tenait à l'écart de lecture ; s'il en reste un, il tient aux lecteurs.
2. **Lecteur d'une autre famille.**
   - Sans dépense, aucun n'est disponible : les espèces Astra, Argon et Carbon ne se lisent que par appels payants. La limite est à écrire en tête du rejeu v3 : « deux lecteurs d'une même famille ; l'écart par famille n'est pas séparable de la préférence pour soi ».
   - À coût nul, ajouter un **lecteur par programme** pour D et pour la voie : une règle structurelle sur le champ « ce qui la réfuterait », scellée avant. Il n'a pas de famille, et il sert de témoin aux deux lecteurs.
   - Un lecteur d'une autre famille se demande sur devis seulement. Il se lit à auteur fixe et à juge changé, en colonnes, et non en comparant ce qu'un juge donne à sa famille et aux autres (piège mesuré par Awuni et al., note `bb54b685…`, § 5).
3. **Masquer le style, par programme, non par un modèle de la famille des lecteurs.** Une réécriture par Opus ou Fable réintroduirait la famille.
   - Plafonner chaque champ au même nombre de caractères : la longueur est le seul trait fort (r² = 0,27).
   - Retirer le gras, les intertitres de type « pourquoi cela compte », les formules de protocole récitées.
   - Présenter les champs dans un ordre fixe.
   - La note `bb54b685…` (§ 1 et § 4) donne le style uniformisé comme la parade publiée la plus proche (Si et al. ; Li et al., de 17,5 % à 9,0 % de fuite). Elle dit aussi qu'une paraphrase générique n'aide pas et que masquer l'auteur ne suffit pas. Le gain reste à mesurer ici, non à supposer.
4. **Mesure écrite d'avance, couverture complète.** La mère calcule l'espèce par programme sur `meta`, après le dépôt des lectures (critères v2, § 10) : couverture 94 sur 94 au lieu de 62. La statistique est scellée avant : part de la famille des lecteurs parmi les cartes à la note maximale, dans le nombre visé et au veto, comparée à sa part de base (37 sur 94). Elle est accompagnée du test de permutation de l'étiquette d'espèce, stratifié par voie, et rapportée par lecteur et assemblée.
5. **Reconnaissance déclarée.** Chaque lecteur écrit, carte par carte et avant de noter, la lignée qu'il croit reconnaître (« aucune » permis). On peut alors tester si la note suit la reconnaissance plutôt que l'espèce vraie. Cette mesure relève de Lazar si elle change les critères.
6. **Veto.** Quand les deux titulaires sont de la même famille, le filtre de lignée du § 7 des critères doit jouer sur la famille, ou le veto doit être compté à part et rapporté par famille. Le compte de ce rejeu (4 sur 4) le demande, sous la réserve du § 5.
7. **En attendant** : ne pas employer l'assemblage v2 des deux rejeux sans écrire en tête l'écart du D de F et le présent signal.
