# Additif 1 au plan « sabotage ou empreinte de l'adaptateur » (barreau 5) : relance des six instances de formation — v2

Projet d'additif, écrit le 20 novembre 2026, corrigé après sa contre-lecture (douze couples) et celle du code (six couples). À vérifier par le même contre-lecteur, puis à sceller par la session mère ; il ne vaut rien avant. La version 1 du projet reste à côté, sans modification.

- **Texte visé** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, empreinte sha256 `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935` (ligne `SCELLEMENT-B5F` du registre propre). Le texte n'est pas réécrit ; il se lit avec cet additif, qui prime sur les seuls passages nommés à la section 2 et dans sa table.
- **Chemin de scellement proposé** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-additif-1-relance-six-instances-v2.md`, ou le nom que choisit la session mère. Le code ne lit pas l'additif ; la colonne de référence de la ligne de relance en cite le chemin et l'empreinte.
- **Autorité** :
  - mot de Lazar, tel que le consigne la session mère dans la ligne `GO-2026-11-20-51` (accord de type « décision ») : « relance les instances ». L'écart à « deux instances au plus » (`GO-2026-11-19-87`) y est accordé. « Sous le plafond commun de 200 dollars » et « avant la fin des créations » sont la rédaction de la session mère ;
  - Lazar a ensuite accordé les trois autres écarts au texte que porte cet additif, par `GO-2026-11-20-59 (2)` et `GO-2026-11-20-60 (2)` : « tombée » étendue aux six instances arrêtées faute de crédit (C1) ; le code de formation changé après son gel (C5) ; la ligne de relance qui cite `GO-2026-11-19-86`, avec « sous le plafond commun » et « avant la fin des créations » (C4, C6, C7) ;
  - l'accord de calcul reste `GO-2026-11-19-86`, plafond commun de 200 dollars (USD).
- **« go 30 usd »** : ces mots de Lazar, dans le même message, ne couvrent pas la relance. Ils sont le plafond d'une autre course, inscrit à part (`GO-2026-11-20-52`). Ils ne bornent rien de la formation.
- **Ce que le rédacteur a lu** : les seuls extraits permis du texte ; le code de formation, le registre propre, et les fichiers de code de la même chaîne listés au rapport du développeur (version 2, section 8, point 1) ; les deux contre-lectures. Le devis n'a pas été lu : ses deux coupures citées en C4 sont données par la session mère. Aucune sortie, aucun score, aucune branche de données.
- **Portée** : la relance, et rien d'autre.

## 1. Les faits, sans aucune sortie lue

- **H = 2026-11-20T01:30:16Z**, création de la première instance de formation.
- Le 20 novembre 2026, l'instance 6 a fini sa marche, versement prouvé.
- Les instances 1, 2, 3, 4, 5 et 7, créées vers 10:43Z, ont été arrêtées à 12:12Z parce que le crédit manquait chez le loueur. Aucune de leurs familles n'est formée. Leurs branches de sortie existent.
- Leurs disques ont été inventoriés par `ls` et `du`, puis détruits par identifiant le 20 novembre entre 13:20Z et 13:21Z (`GO-2026-11-20-51`, point 2). Les inventaires sont sur les branches de sortie, sous `traces-b5f/disque-arrete/`. Le contenu des disques n'a pas été versé.
- Le registre propre porte cinq lignes : `SCELLEMENT-B5F`, `CODE-FORMATION-B5F`, `GO-FORMATION-B5F`, `CODE-LECTURE-B5F`, `EPREUVE-B5F`. Le code de lecture est donc déjà figé (commit `c76e79169eee337ce66c7d88f62d039e853eebfc`), et son épreuve à vérité plantée est passée.

La cause de l'arrêt est le crédit. La décision de relancer ne s'appuie sur aucune sortie du plan : elle reste une règle mécanique au sens du point 12 de la liste d'arrêt.

## 2. Ce qui change, et pourquoi

Chaque point dit ce que le texte disait, ce que l'additif dit, et la raison. La table en fin de section nomme les passages remplacés.

**C1. Les six instances arrêtées faute de crédit sont « tombées ».** Le texte énumère les causes qui ne lisent aucune sortie : perte de l'hôte, garde d'instance, échéance atteinte, sorties perdues. L'additif dit : les instances 1, 2, 3, 4, 5 et 7, arrêtées le 20 novembre 2026 à 12:12Z faute de crédit chez le loueur, sont tombées au sens de la règle de la relance ; l'arrêt faute de crédit est une cause qui ne lit aucune sortie. L'instance 6 n'est pas tombée : elle n'est pas relancée, et le code refuse une ligne de relance qui la cite. Écart accordé (`GO-2026-11-20-59 (2)`, `GO-2026-11-20-60 (2)`).

**C2. Six instances relançables, au lieu de deux.** Le texte bornait la ligne de relance à deux instances. L'additif la borne aux six instances tombées. Chaque instance reste relancée une seule fois, entière ; il n'y a pas de seconde relance. Écart accordé (`GO-2026-11-20-51`).

**C3. 147 dollars de coupures au plus, au lieu de 56.** Chaque relance garde la coupure de l'instance qu'elle remplace : 26 dollars pour chacune des instances 1 à 5, 17 dollars pour l'instance 7 (familles d'apprentissage à trois membres). La somme est 5 × 26 + 17 = 147 dollars. Le code refuse une ligne de relance qui cite plus de six instances, ou dont les coupures dépassent 147 dollars ; au-delà, c'est un nœud.

**C4. La relance entre sous le plafond commun.** Le texte mettait la relance hors du plafond du devis, dans une enveloppe à part de 56 dollars (`GO-2026-11-19-87`). L'additif la met sous le plafond commun de 200 dollars de l'accord `GO-2026-11-19-86`, tel que le consigne la session mère dans la ligne `GO-2026-11-20-51` ; écart accordé (`GO-2026-11-20-59 (2)`, `GO-2026-11-20-60 (2)`). En conséquence :
- le compteur commun compte toutes les pièces du devis (premières marches, relecture, répétition) **et toutes les relances** ; la dépense de la première marche d'une instance tombée y reste ;
- le plafond atteint arrête **aussi** une relance en cours ; une relance a donc deux compteurs en cours de marche : la coupure de l'instance qu'elle remplace, et le plafond commun ;
- l'enveloppe à part de `GO-2026-11-19-87` n'est pas employée et ne s'ajoute pas au plafond ;
- **le point 14 de la liste d'arrêt se lit désormais** : « Dépense : chaque instance, relances comprises, s'arrête dès que son cumul relevé plus un quart d'heure atteint sa coupure ; les pièces du devis et les relances s'arrêtent toutes au plafond commun, que leur dépense à toutes compte ; arrêt et destruction par identifiant (R10), après versement de ce qui est récupérable. »

**Réserve, tenue par la session (le code ne la vérifie pas).** La ligne de relance n'est inscrite que si le cumul commun relevé ne dépasse pas **24 dollars** : 200, moins 147 (coupures des relances), moins 21 (coupure de la relecture), moins 8 (coupure de la répétition générale). Ces deux coupures sont celles du devis scellé, `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md`, sha256 `dc886195c77b0d67c31cb8815a1e97b9fa72dd35ebac2b8f3bc49d4e5cf59bcc`, section 4. Au-dessus de 24 dollars : nœud. La session écrit le cumul relevé dans la colonne de référence de la ligne.

La répétition générale et le volume de stockage sont interdits tant qu'ils pourraient prendre la part des relances : tant qu'une relance est à créer ou en cours, aucune de ces pièces ne part si le cumul relevé, plus les coupures des relances qui restent à créer ou à finir, plus 21 dollars pour la relecture, plus la coupure de cette pièce, dépasse 200 dollars. Le prix du volume de stockage reste porté à Lazar avant toute dépense (`GO-2026-11-19-88`).

**C5. Le code des relances : changé après le gel, sans clé neuve au registre.** Le texte disait que les sections dont dépend le code de formation « ne changent plus », et la ligne `CODE-FORMATION-B5F` épingle le commit du code et l'entropie de 128 bits. Le code doit pourtant changer pour C1, C2, C3, C4 et C6. Écart accordé (`GO-2026-11-20-59 (2)`, `GO-2026-11-20-60 (2)`).
- **Aucune clé n'est ajoutée au registre propre.** Le code de lecture, figé à `CODE-LECTURE-B5F`, refuse le registre entier s'il y trouve une clé inconnue ; rien ne doit le lui faire refuser, ni toucher à l'épreuve passée (`EPREUVE-B5F`).
- Le commit du code des relances s'écrit dans la **colonne de référence** de la ligne `GO-RELANCE-FORMATION-B5F`, que le texte laisse libre, sous la forme exacte « `code des relances commit <40 signes>` », une et une seule fois, séparée du reste par « ; ». Les mots « code des relances » n'apparaissent nulle part ailleurs dans cette référence. Le code des relances lit cette mention à la lettre, et lui seul ; le code de lecture lit la ligne par son contenu, qui ne change pas.
- Ce commit descend du commit de `CODE-FORMATION-B5F` et en diffère ; le code le vérifie.
- **L'entropie ne change pas** : c'est celle de `CODE-FORMATION-B5F`.
- Une première marche se compare toujours au commit de `CODE-FORMATION-B5F` ; une relance, au commit du code des relances. Les sorties versées de l'instance 6 ne sont pas touchées : son manifeste cite le code qu'elle a joué.
- Le « code des relances » est le code de `CODE-FORMATION-B5F`, plus les seuls changements que cet additif exige, avec les essais qui les éprouvent, le plancher d'essais de l'amorce que leur nombre force, et les commentaires qui les décrivent. Le fichier `engagement_v1.py`, que partage le code de lecture, n'est pas changé : il reste, à l'octet, celui du commit de `CODE-LECTURE-B5F`.
- Le code des relances vit sur sa branche et sur la branche de course. Il n'entre pas dans l'arbre d'où part la lecture : la relecture et la lecture jouent l'arbre gelé de `CODE-LECTURE-B5F`.
- **Exception déclarée à la règle des noms versionnés (R12)** : le code des relances garde les noms de fichiers du code des premières marches (« v1 »). Sa version est le commit que cite la ligne de relance ; les fichiers des premières marches restent au commit de `CODE-FORMATION-B5F`. Renommer aurait changé l'amorce, le lanceur, le module appelé et les essais, bien au-delà de ce que l'additif exige. La session mère consigne cette exception au registre des décisions.

**C6. La ligne de relance cite l'accord de calcul de la formation.** Le texte faisait citer à la ligne l'accord de l'enveloppe (`GO-2026-11-19-87`). Puisque la relance entre sous le plafond commun (C4), la ligne cite l'accord de ce plafond, celui de `GO-FORMATION-B5F` : `GO-2026-11-19-86`. Le code refuse tout autre accord. Les mots de Lazar (`GO-2026-11-20-51`, de type « décision ») s'écrivent dans la colonne de référence : la garde de calcul du dépôt n'admet qu'un accord de type « calcul » devant une commande du loueur. Écart accordé (`GO-2026-11-20-59 (2)`, `GO-2026-11-20-60 (2)`).

**C7. Les relances sont créées avant la fin des créations, et la ligne de relance avant la première d'entre elles.** Le texte ne fixait pour la relance que la dernière heure de sa ligne (H + 54 heures) et sa fin (H + 65 heures). L'additif ajoute, selon la rédaction de la session mère accordée par Lazar : les six relances sont créées avant la fin des créations, H + 30 heures, soit le 21 novembre 2026 à 07:30:16Z. Une relance qui n'est pas créée à cette heure ne l'est plus ; ses familles sont absentes, pour raison technique écrite. La ligne `GO-RELANCE-FORMATION-B5F` est donc inscrite avant la création de la première relance, donc avant 2026-11-21T07:30:16Z ; la borne de H + 54 heures du texte reste, sans effet ici. Ces échéances sont tenues par la session ; le code ne les vérifie pas.

**C8. Les premières copies des instances tombées n'ont pas été versées.** Le texte dit « la première copie est versée, inventoriée, et jamais lue ni notée » et « aucune sortie n'est supprimée avant son versement ». Pour les instances 1, 2, 3, 4, 5 et 7 : ce que leurs premières marches avaient poussé sur leurs branches de sortie avant l'arrêt est gardé, jamais lu ni noté ; leurs disques ont été inventoriés par `ls` et `du`, les inventaires versés sous `traces-b5f/disque-arrete/`, puis les disques détruits par identifiant. Écart accordé (`GO-2026-11-20-51`, point 2).

**Passages du texte remplacés.**

| passage du texte | ce qui le remplace |
|---|---|
| règle de la relance : liste des causes d'une instance « tombée » | C1 |
| règle de la relance : « au plus tard à H + 54 heures » pour la ligne | C7 : avant la première création, donc avant H + 30 heures |
| règle de la relance : « la première copie est versée, inventoriée » ; « Données gardées » : « aucune sortie n'est supprimée avant son versement » | C8, pour les six instances tombées seulement |
| borne de la relance : « elle n'entre pas sous le plafond du devis » ; « 56 USD de coupures au plus, soit deux instances » ; « le code refuse une ligne de relance qui cite plus de deux instances » | C2, C3, C4 |
| borne de la relance : « la dépense d'une relance n'y entre pas » ; « la relance n'a pas de troisième compteur » ; « le plafond atteint arrête les pièces du devis, non une relance en cours » | C4 |
| borne de la relance : « chaque relance porte la ligne GO-RELANCE-FORMATION-B5F, qui cite cet accord » (`GO-2026-11-19-87`) ; dernière phrase, sur le constat n-4 | C6 ; la relance est sous le plafond commun |
| « Calcul et dépense » : « à part, une enveloppe de relance de 56 USD au plus » | C4 : enveloppe non employée |
| liste d'arrêt, point 14 | libellé neuf, en C4 |
| « Sections dont dépend le code de formation » : « elles ne changent plus » | C5 |
| « Lignes de registre » : format de `GO-RELANCE-FORMATION-B5F` | contenu inchangé ; mention du code des relances dans la référence (C5) ; aucune clé ajoutée |

## 3. Ce qui ne change pas

- **Les familles.** Le plan des instances, les membres, la recette, les tâches, les contrôles : inchangés. Les familles d'une instance relancée sont reformées toutes, sous leur nom suffixé `-x1`.
- **Les graines.** Même entropie, celle de `CODE-FORMATION-B5F` ; graines neuves par le seul suffixe `-x1` dans le nom de la famille (point 14 du plan d'analyse). La clé d'injection de l'instance ne porte pas le suffixe, comme avant.
- **La lecture de la seule copie `-x1`.** Dès que la ligne de relance est inscrite, seule la copie `-x1` est lue pour toutes les familles des instances citées ; aucune copie n'est choisie. Les familles de l'instance 6, non citée, sont lues dans leur première copie.
- **Les échéances.** H = 2026-11-20T01:30:16Z. Fin des créations à H + 30 heures (21 novembre 2026, 07:30:16Z) ; dernière heure de la ligne de relance à H + 54 heures (22 novembre, 07:30:16Z), sans effet ici puisque la ligne précède la première création (C7) ; fin de toute relance à H + 65 heures au plus (22 novembre, 18:30:16Z). La ligne de relance est unique et cite d'un coup toutes les instances.
- **Les coupures par instance.** Celles du devis ; une relance prend la coupure de l'instance qu'elle remplace ; arrêt dès que le cumul de l'instance plus un quart d'heure atteint sa coupure.
- **Le versement des relances.** Aucune sortie d'une relance n'est supprimée avant son versement ; destruction par identifiant, après versement prouvé.
- **L'ordre des créations.** Celui du texte, sans l'instance 6 : 1, 2, 3, 4, 5, 7, au fil des offres que la garde du code accepte. Aucune borne du devis n'est desserrée.
- **Si une relance tombe à son tour.** Les familles qu'elle n'a pas achevées sont absentes, pour raison technique écrite. Les coupes de la section « Calendrier » et le point 13 de la liste d'arrêt (moins de six familles présentes) s'appliquent tels quels.
- **Le code de lecture et son épreuve.** `CODE-LECTURE-B5F` et `EPREUVE-B5F` ne bougent pas.
- **Tout le reste du texte** : métrique, seuil, plan d'analyse, critères de lecture, liste d'arrêt hors du point 14 réécrit en C4, données gardées hors de C8, engagement, relecture, ouverture, verdict.

## 4. Ordre des lignes au registre propre

Lignes ajoutées, jamais réécrites ; instants strictement croissants.

1. Déjà inscrites : `SCELLEMENT-B5F`, `CODE-FORMATION-B5F`, `GO-FORMATION-B5F`, `CODE-LECTURE-B5F`, `EPREUVE-B5F`.
2. **Une seule ligne neuve**, `GO-RELANCE-FORMATION-B5F`, inscrite par la session mère après le scellement de cet additif et la vérification du code des relances, avant la création de la première relance, donc avant 2026-11-21T07:30:16Z :
   `| GO-RELANCE-FORMATION-B5F | <instant> | GO-2026-11-19-86 ; instances 1,2,3,4,5,7 | <référence> |`
   La référence porte, séparés par « ; » : les mots de Lazar `GO-2026-11-20-51` ; les écarts accordés `GO-2026-11-20-59 (2)` et `GO-2026-11-20-60 (2)` ; cet additif scellé (chemin et empreinte) ; la mention exacte « `code des relances commit <40 signes du code vérifié>` », une seule fois ; le cumul commun relevé à l'inscription ; « enveloppe GO-2026-11-19-87 non employée ».
3. Puis, comme dans le texte : `SORTIES-FORMATION-B5F`, puis `ENGAGEMENT-B5F` après la fin de toute relance, puis les lignes de la lecture.

Les relances partent d'un **commit de course** : un commit fils du commit du code des relances, dont seul le dossier des registres diffère. Son registre propre est celui de la branche principale à l'inscription, à l'octet, ligne de relance comprise.

## 5. Qui tient quoi

- **Le code des relances** : la mention du code des relances dans la référence (une et une seule, 40 signes, différente du code des premières marches) ; la filiation de ce commit ; l'accord de la ligne de relance égal à celui de `GO-FORMATION-B5F` ; six instances au plus, 147 dollars au plus, et les seules instances 1, 2, 3, 4, 5 et 7 ; le code d'une relance comparé à ce commit, sur l'instance comme à l'impression de la commande de création ; les deux compteurs de dépense pour toute marche. Cas sain et artefact pour chacune de ces gardes.
- **La session de formation et la session mère** :
  - le contenu exact de la ligne de relance, `GO-2026-11-19-86 ; instances 1,2,3,4,5,7` ;
  - le relevé du cumul commun, relances comprises, la réserve de 24 dollars avant l'inscription, et l'interdit sur la répétition et le stockage (C4) ;
  - la vérification, avant d'inscrire la ligne, que `GO-2026-11-19-86` est en vigueur jusqu'à la dernière création ; sinon, nœud ;
  - les échéances de C7 et la fin à H + 65 heures ; l'ordre des créations ; le versement prouvé avant toute destruction ;
  - le registre du commit de course égal à celui de la branche principale (section 4).

## 6. Nœuds

Remontent à Lazar, sans rien lancer : une relance de l'instance 6, ou une seconde relance d'une même instance ; des coupures de relance au-delà de 147 dollars ; un cumul commun relevé au-dessus de 24 dollars avant l'inscription de la ligne ; un besoin de dépasser le plafond commun de 200 dollars ; une clé neuve au registre propre, ou tout changement de `engagement_v1.py` ; tout changement du code autre que ceux de la section 2 et de leurs suites nommées en C5.
