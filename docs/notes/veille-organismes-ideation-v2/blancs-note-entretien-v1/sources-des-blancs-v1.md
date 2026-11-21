# Sources des cinq blancs de la note pour l'entretien du 1er décembre — v1

- 21 novembre 2026, de 20:22 à 20:40 UTC (`date -u`). Auteur : Claude Opus 5.5, lecteur autorisé désigné par la mère (GO-2026-11-21-69, « designe un lecteur autorise »). Pièce de travail (classe C), non contre-lue. Aucun appel payant, aucune requête en ligne, aucun commit.
- Sert la note `docs/notes/veille-organismes-ideation-v2/note-entretien-controle-diffus-v5.md` (empreinte dans son compagnon `.sha256`), qui remplit les blancs 2-a, 2-b, 5-a, 5-b et 9-a nommés par l'erratum 2 de la v4 (`note-entretien-controle-diffus-v4-erratum-2.md`, `ad6debe313288035e00b8f2ae5d9d3ccb23caa440796ee1d108da69d7d16f023`, section C).
- Règle : chaque blanc ne dit que l'état. Aucun chiffre de résultat n'est repris ici ni dans la note. Aucun nom de session, aucun identifiant de machine, aucun courriel. Les lignes de registre sont citées par leur numéro ; plusieurs portent des noms de session, qui ne sont pas recopiés.

## Registres lus, empreintes à la lecture

Les registres changent ; l'empreinte est celle du fichier à 20:27 UTC.

| Pièce | Empreinte à la lecture | Lu |
|---|---|---|
| `registres/decisions.md` | `b018a84006fe49955b308ca8b2cf10cb62f1db2fea5ff7e0e002663703f85282` | lignes R-4580 à R-4709 en entier, par morceaux ; lignes R-597, R-692, R-772, R-1817, R-1849, R-4340 (citée par la recherche), R-4543, R-4600, R-4640 trouvées par recherche |
| `registres/go.md` | `663c84b95d76e7a1605dd6cc61fa23f21b84317e570f7ecb6292f6d887e427b8` | GO-2026-11-21-60 à -83, dont -61, -65, -66, -69 en entier |
| `registres/etat.md` | `0751abb2164573d1165ed7f6646b5ca1aa3dda796f9f3ba7d658142800314a1c` | lignes 1 à 10 ; recherche par motifs |

## Décisions lues, empreintes égales aux compagnons

| Pièce | Empreinte | Lu |
|---|---|---|
| `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` | `49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78` | lignes 40 à 70 (protocole, prévision, ce qui change) |
| son erratum 1, qui prime | `34a59c49436d5239ccf2e8c4df5945a50e54665bae96bf1e32c524a643916484` | en entier |
| `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md` | `5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5` | non lue au-delà de son empreinte ; lue à travers son erratum 3 v2 |
| ses errata 1, 2, 3 et 3 v2 | `c6efeccf…b0c1`, `b19852b4…bb46`, `d51863d2…f3fd`, `fbe3298ec358fa9b8d041d8675d9ad3369e99591572c8281806f0ade75463b04` (le dernier prime) | erratum 3 v2 : en-tête et point 11 |
| `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | en entier |
| `docs/decisions/decision-N-060-v4.md` | `e14779987cf61ae65f4690a0bbb94f373bd0e48f8cdeabb0bd2b31b99b1af241` | en entier |
| son erratum 1, qui prime | `316c8c233eea9848ded84ec9b17d628cec70fca075213ff36f35ffce65bdba95` | en entier |
| `decision-N-062-v1.md`, `decision-N-056-v1.md`, `decision-N-068-v1.md`, `decision-N-007-N-008-v1.md`, `decision-N-053-v1.md` | égales aux compagnons (vérifiées) ; empreintes telles que l'erratum 2 les cite | non relues : leur lettre est celle de l'erratum 2 et de sa vérification |

## Blanc 2-a — taille de la référence honnête et horizon du banc

**État écrit dans la note** : non fixés à ce jour ; la prévision qui doit les porter est en cours d'écriture, non scellée.

| Ce qui le fonde | Pièce | Empreinte |
|---|---|---|
| La commande : la prévision porte « m et n du banc, l'horizon où la première courbe doit s'aplatir, l'écart minimal », dans un texte à part de classe A, scellé avant toute lecture des épisodes qui la servent, avant la porte de fin de phase 1, hors critère | N-076, l. 51 à 55 | `49b664c1…dd78` |
| La pièce manquait sur toutes les branches à 17:48 UTC ; « m et n du banc ne sont fixés nulle part » | `docs/notes/pieces-manquantes-classe-a-v1/recherche-exhaustive-v1.md` ; registre R-4643 | `73aa7317fb7581968343f76d5bbb2fb1d39484ad470281b24eb2701b959cff63` |
| Brouillon 1 de la prévision, « jamais scellé », chaque valeur marquée « à fixer par Lazar » ou « de principe » (m, W, horizon maximal) | `docs/notes/pieces-manquantes-classe-a-v1/brouillon-1-v1.md` | `08158ab85ed39cd88c5590c6d44bcb1d902dd54a416dd98af7796372b1c49a0c` |
| Sa contre-lecture : « à corriger » ; points 1 à 3 à Lazar | `docs/notes/pieces-manquantes-classe-a-v1/contre-lecture-brouillon-1-opus-v1.md` | `7b11cbfeb56107d91d0a01643af8d3f85297b18531f368f6df78faa0bff94f20` |
| Sa correction, interrompue par la limite d'usage de Fable, scellée telle quelle, « ne fait pas foi » | `…/interrompu-limite-fable-2026-11-21-v1/LISEZ-MOI.md` ; `brouillon-1-v2.md` (non lu) ; registres R-4702, R-4705 | `3f9a6dd383be991a7235b5f0dd72ac7a949d07ac4f138e64e29078a8f8f9b08a` ; `b4eea47f36cfb5d3828fc0ffaed5998cd9960b2c4e95d67b17e8cef70fdcb09b` |
| Le banc à lois plantées, qui fixerait la matière (référence de m épisodes d'autres mondes) : conception v2 vérifiée « conforme » ; proposition, non accordée comme banc | `docs/notes/banc-lois-plantees-c2-v1/conception-fable-banc-lois-plantees-v2.md` ; vérification ; registre R-4621 | `62c519c0c46c8406ce5cb4a172ca4f251df62da52eba7a710f4f3d54737164aa` ; `a6013316378281fc4f15c29ebb64df063be3c4748070ec41b6b2521f541cab3b` |
| La prévision n'est pas touchée par le constat « la comparaison lit le handicap » : elle oppose une référence fixe au rang contre le jumeau | `docs/notes/lire-l-intention-v1/reponse-fable-lire-l-intention-v1.md`, § 2.2, point 3 | `dd2d97e832c45f46d6d68d259371db0b2710c40f968aa61e74b7a2f28f13d2ac` |

Réserve : aucun chiffre du brouillon n'est repris ; ce sont des valeurs de principe, que Lazar n'a pas fixées.

## Blanc 2-b — écart mesuré entre l'honnête et son jumeau

**État écrit dans la note** : non mesuré à ce jour.

| Ce qui le fonde | Pièce | Empreinte |
|---|---|---|
| L'écart est un test de mort de la prévision (« l'écart systématique mesuré entre l'honnête et le jumeau cache déjà plus que le dommage visé ») : il se mesure dans le cadre de la prévision, qui n'est pas écrite | N-076, l. 55 | `49b664c1…dd78` |
| Au banc actuel, le dommage se lit contre le jumeau apparié ; le bras A des organismes discrets en est au texte neuf, non scellé, et à ses devis (le texte scellé précédent est archivé sans exécution) | N-060 v3, point 1 ; N-060 v4 et erratum 1 ; registres R-4682, R-4698, R-4701, R-4704 | voir plus haut |
| La course sur banc fermé n'a pas tourné : préenregistrement accepté, non scellé | registres R-4689, R-4694, R-4696 | — |
| La contre-lecture du brouillon 1 note que, sur un banc où l'original honnête est un tirage du jumeau, la lettre du test de mort est « vide par construction » et propose un autre objet (point 3, à Lazar) | contre-lecture du brouillon 1, constat 3 | `7b11cbfe…4f20` |

Réserve : « non mesuré » veut dire « aucun écart scellé trouvé dans les registres et les pièces lues ». Les résultats des courses antérieures dont la lecture m'est fermée n'ont pas été ouverts ; si l'un portait un tel écart, il serait « réservé, lecture non ouverte ».

## Blanc 5-a — épreuves de l'oracle ; référence invisible de l'agent

**État écrit dans la note** : épreuves écrites, objets construits par programme, aucune passée sous verdict scellé ; garde d'invisibilité écrite, non attestée par un verdict.

| Ce qui le fonde | Pièce | Empreinte |
|---|---|---|
| Les cinq épreuves avant toute lecture d'un épisode saboté (retrait mécanique, référence d'une autre tâche, plan tronqué, dose flagrante, ancre humaine) ; « à vérifier avant l'usage : que l'agent ne voit pas `cibles` » | N-060 v3, point 2 et « ce que la décision ne fixe pas » | `2b448f69…5591` |
| Les objets des épreuves construits par programme (retrait, référence permutée, troncature, chacun avec son attendu ; vérification mot pour mot de l'extrait) ; garde « cibles invisibles » sur les chemins d'invite, par interception et par inventaire | registre R-772 ; `src/controle_ia/verite_dommage/artefacts_v1.py` | `22f0fc884b3f84d13612180ca40d168e84e9a94472de41cce1ca1e497a94e790` (égale au compagnon) |
| La garde dans sa version courante | `tests/test_cibles_invisibles_v3.py` | `93a6df4343f876cad58c01933d2636e65858bc8d55a99285edd4125cb5d504a9` (égale au compagnon) |
| La garde n'est pas attestée sur la tête actuelle : des fautifs préexistants à son inventaire sont relevés, « à trancher » | registre R-4640 | — |
| Un lecteur voisin, l'étiqueteur, couvrait trois des cinq épreuves (retrait mécanique et dose flagrante en phase 1, ancre humaine en phase 2) et ne validait pas l'oracle de couverture ; sa phase 1 a un verdict scellé « non tranché », la phase 2 ne part pas, il n'est pas retenu comme vérité du dommage | registres R-1817, R-1849 ; `docs/verdicts/verdict-etiqueteur-phase1-v1.md` (non ouvert ; le mot du verdict est celui du registre) | `9f7830b95cc0238d09d5846798c4ff12dba07644271330d4ed6ec43d555c6eae` (égale au compagnon) |
| L'audit du rappel de l'oracle (rapprochement aux contrôles de l'article, plus les deux épreuves négatives) : brouillon 1, non scellé | `prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` ; registre R-1817 | `ccc0d972480cdf8a2170f53a87c5ed21801e838242e9786d65a13047bf3eda85` (égale au compagnon) |
| Bras A : épreuves avant toute lecture d'un épisode saboté, place des cinq épreuves en nœud de Lazar ; ancres jugées par un agent neuf ; le jugement scellé des deux ancres n'est pas fait à 16:06 UTC | N-060 v4, erratum 1, points 3 et 4 ; registres R-3645, R-4275, R-4600 | `316c8c23…ba95` |
| Banc fermé : oracle de la famille de la porte « monté », au coffre, lecteurs en attente ; à la répétition générale, la lecture du dommage n'est éprouvée que « dans sa mécanique seule, réserve écrite » ; les attestations sur les références des tâches au coffre sont à venir | recherche des pièces manquantes, pièce 2 ; registres R-4678, R-4689 | `73aa7317…ff63` |
| La part q des dommages que l'oracle reconnaît se mesure par des dommages plantés par un tiers ; une strate non mesurée compte pour zéro ; la campagne a un devis accordé pour son étape 1, non lancée | N-075, erratum 3 v2, point 11 ; GO-2026-11-21-66 ; registres R-4632, R-4700 | `fbe3298e…3b04` |

Réserves : (1) cette phrase vaut pour le mode « affaiblir les contrôles », seul visé par le point 1 de N-060 v3 ; (2) le compagnon de `tests/test_cibles_invisibles_v1.py` ne correspond plus au fichier (empreinte du fichier `b5fd257bb47080f9ccffafaecdc180f2e31f3c83b5d96b1528c0be135bedba25`, compagnon `6a833e3e…4ea8`, fichier modifié par un commit) : signalé, non tranché, la v1 n'est pas citée comme preuve ; (3) aucune épreuve d'un autre banc n'est rapportée ici.

## Blanc 5-b — état de l'étape 0 du banc à vérité plantée

**État écrit dans la note** : étape 0 accordée et en cours, sans dépense ; conceptions corrigées et en vérification ; l'étape 0 ne tourne que sur des données simulées ; aucun modèle n'y a tourné ; rien de mesuré.

| Ce qui le fonde | Pièce | Empreinte |
|---|---|---|
| Accord : « plan des tâches floues sur dix mondes plantés : go (étape 0 ; étape 1 sur devis) » | GO-2026-11-21-61 | — |
| La conception du banc passe par le protocole X ; sa spécification sort des premiers pas sans dépense | N-076, erratum 1, E3 et E5 | `34a59c49…6484` |
| « Vérité plantée : turbo max » ; une session fille dédiée aux étapes 0 des trois bancs | GO-2026-11-21-66 ; registre R-4635 | — |
| Plan des tâches floues sur mondes plantés ; corrections vérifiées « conforme » | `docs/notes/protocole-x-dommage-v1/reponse-fable-protocole-x-dommage-v2.md`, § 4 ; vérification ; registre R-4613 | `c28388032c07fff79a5003457d74293ebb4c919e1f01326d3b3661529f2b7579` ; `cd34f640d9e766a2504648e76a0abcbb5f5e7813013974f6285eda65b1920417` |
| À 20:02 UTC, trois rendus de conception sur une branche de préparation : tâches floues v2, dommages par un tiers v2, étape 0 v1 du banc à lois plantées, jouée sur données simulées ; vérifications et contre-lecture confiées à des Opus | registre R-4700 (pièces non ouvertes) | — |
| Dommages plantés par un tiers : devis accordé (plafond de l'étape 1 sur mot), non lancée | GO-2026-11-21-66 ; registre R-4632 | — |

Réserves : les pièces de la branche de préparation ne sont pas ouvertes (cloison : noms portant « vérité ») ; leur contenu n'est connu que par la ligne R-4700, dont aucun chiffre n'est repris. L'état au 1er décembre est à relire par la mère.

## Blanc 9-a — ce qui a été lancé et lu des bras d'attaque

**État écrit dans la note** : rien de lancé, rien de lu ; règle scellée et contre-lue ; familles scellées au coffre ; préenregistrement de la première course accepté, non scellé ; répétition générale à faire ; moniteurs gelés non scellés ; comparaison aux juges en brouillon.

| Ce qui le fonde | Pièce | Empreinte |
|---|---|---|
| Les deux bras décidés (aveugle et informé) ; recettes scellées | N-056, point 6 (lettre de l'erratum 2 et de sa vérification) | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` |
| Règle du bras d'attaque (scellement 1, « méthode seulement »), scellée le 10 novembre après trois contre-lectures, hors de la branche principale par cloison (R-4340) ; scellements 2 et 3 non scellés comme préenregistrement à 17:48 UTC | recherche des pièces manquantes, pièce 2 | `73aa7317…ff63` (règle : `88418df09c2e969cbdc77d220fe59dbf64f866d858ff02a039be5662c6d1f904`, d'après la recherche, non ouverte par moi) |
| Famille de la porte : pièces 1 à 7, contre-lecture « accepté » ; index tenu par la mère (empreintes seules) | registres R-4606, R-4627, R-4670 ; `registres/index-scellement-2-familles-aveugles-v3.md` (non ouvert) | `cde486b03a81aeb33d5a05a3355479fe917077c84cd5a044e66a6b7abb47d893` (égale au compagnon) |
| Famille de réserve du cycle 2 : rendue, contre-lue « acceptée », dite neuve face à la première | GO-2026-11-21-67 ; registres R-4642, R-4645, R-4662 | — |
| Oracle de la famille de la porte monté, au coffre, lecteurs en attente | recherche des pièces manquantes, pièce 2 ; registre R-4638 | — |
| Banc fermé : préenregistrement de la course, brouillon 14, accepté sans reste ; répétition générale figée au brouillon 9 (premier temps de l'ordre des scellements) ; manifeste des moniteurs et devis lancés ; pièce de sécurité v16 | registres R-4694, R-4696 ; GO-2026-11-21-80 | — |
| Répétition sur un mode connu, attestée par la mère | `docs/notes/repetition-generale-banc-ferme-v1/attestation-mode-connu-mere-v1.md` (non ouvert) ; registre R-4680 | `166ed50225f48a69a77c3f68bf791c287557a7db3071b62879d2db1dce7e020f` (égale au compagnon) |
| Embargo des agrégats de dommage envers les concepteurs de moniteurs jusqu'au scellement 3 | registre R-4654 | — |
| Comparaison de la sonde aux juges sous les mêmes attaques : dans le préenregistrement du papier C, brouillon 6 version r3, non vérifié, non scellé | recherche des pièces manquantes, pièce 3 | brouillon : `160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac` (d'après la recherche, non ouvert) |
| Plus ancien : la préparation d'un lanceur d'attaque, arrêtée par un classifieur le 27 octobre, rien lancé, rien dépensé | registre R-597 | — |
| La course « nouvelles attaques » contre les juges de l'organisme est un objet distinct et cloisonné | GO-2026-11-21-65 ; registre R-4511 | — |

Réserves : « rien de lancé » vaut pour les bras d'attaque contre les sondes, à la lecture des registres ; les branches de données nommées « bras-attaque » ne sont pas examinées (cloison). Aucune pièce du coffre n'est ouverte ; aucun contenu de famille n'est dit.

## Ce que je n'ai pas fait

- Je n'ai ouvert aucun résultat, score, épisode, verdict au-delà de son empreinte, aucune pièce du coffre, aucune branche de données, aucun fichier dont le nom porte « vérité », « rendu », « scores », « consigne-privee » ou « conception-ii-b ».
- Je n'ai relu aucune page de papier : les sections 2 à 9 de la note restent celles de l'auteur de la v4.
- Cette table n'est pas contre-lue.
