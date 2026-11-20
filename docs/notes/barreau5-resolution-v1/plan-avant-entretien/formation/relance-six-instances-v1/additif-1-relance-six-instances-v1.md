# Additif 1 au plan « sabotage ou empreinte de l'adaptateur » (barreau 5) : relance des six instances de formation — v1

Projet d'additif, écrit le 20 novembre 2026. À contre-lire par un autre modèle, puis à sceller par la session mère ; il ne vaut rien avant.

- **Texte visé** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, empreinte sha256 `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935` (ligne `SCELLEMENT-B5F` du registre propre). Le texte n'est pas réécrit ; il se lit désormais avec cet additif, qui prime sur les seuls points listés à la section 2.
- **Autorité** : mot de Lazar, `GO-2026-11-20-51` (accord de type « décision », registre des accords) : « relance les instances ». L'écart à la règle de relance du texte (deux instances au plus, `GO-2026-11-19-87`) est accordé, et la relance se fait sous l'accord de calcul `GO-2026-11-19-86` et son plafond commun de 200 dollars (USD).
- **Ce que le rédacteur a lu** : les seuls extraits permis du texte (point 14 du plan d'analyse, liste d'arrêt, « Données gardées », « Calcul et dépense », « Calendrier et chemin critique », « Lignes de registre », « Code neuf »), le code de formation et le registre propre. Aucune sortie, aucun score, aucune branche de données.
- **Portée** : la relance, et rien d'autre.

## 1. Les faits, sans aucune sortie lue

Le 20 novembre 2026, l'instance 6 a fini sa marche, versement prouvé. Les instances 1, 2, 3, 4, 5 et 7, créées vers 10:43Z, ont été arrêtées à 12:12Z parce que le crédit manquait chez le loueur (mot de Lazar). Aucune de leurs familles n'est formée. Leurs branches de sortie existent.

La cause de l'arrêt est le crédit. La décision de relancer ne s'appuie sur aucune sortie du plan : elle reste une règle mécanique au sens du point 12 de la liste d'arrêt.

## 2. Ce qui change, et pourquoi

Chaque point dit ce que le texte disait, ce que l'additif dit, et la raison. La raison commune est `GO-2026-11-20-51`.

**C1. Une instance arrêtée faute de crédit est « tombée ».** Le texte énumère les causes qui ne lisent aucune sortie : perte de l'hôte, garde d'instance, échéance atteinte, sorties perdues. L'additif ajoute : arrêt de l'instance par le loueur ou par la session faute de crédit, avant qu'une famille soit formée. Les instances 1, 2, 3, 4, 5 et 7 sont tombées. L'instance 6 ne l'est pas : elle n'est pas relancée, et ses familles sont lues telles qu'elles ont été formées.

**C2. Six instances relançables, au lieu de deux.** Le texte bornait la ligne de relance à deux instances. L'additif la borne à six : c'est le nombre des instances tombées. Chaque instance reste relancée une seule fois, entière ; il n'y a pas de seconde relance.

**C3. 147 dollars de coupures au plus, au lieu de 56.** Chaque relance garde la coupure de l'instance qu'elle remplace : 26 dollars pour chacune des instances 1 à 5, 17 dollars pour l'instance 7 (familles d'apprentissage à trois membres). La somme est 5 × 26 + 17 = 147 dollars. Le code refuse une ligne de relance qui cite plus de six instances, ou dont les coupures dépassent 147 dollars ; au-delà, c'est un nœud.

**C4. La relance entre sous le plafond commun.** Le texte mettait la relance hors du plafond du devis, dans une enveloppe à part de 56 dollars (`GO-2026-11-19-87`). L'additif la met sous le plafond commun de 200 dollars de l'accord `GO-2026-11-19-86`, comme le dit `GO-2026-11-20-51`. En conséquence :
- le compteur commun compte toutes les pièces du devis (premières marches, relecture, répétition) **et toutes les relances** ; la dépense de la première marche d'une instance tombée y reste ;
- le plafond atteint arrête **aussi** une relance en cours (point 14 de la liste d'arrêt : la phrase « une relance, hors de ce plafond, ne compte que dans son enveloppe » ne vaut plus) ;
- une relance a donc deux compteurs en cours de marche : la coupure de l'instance qu'elle remplace, et le plafond commun ;
- l'enveloppe à part de `GO-2026-11-19-87` n'est pas employée et ne s'ajoute pas au plafond ;
- la raison que donnait le texte pour tenir la relance hors du plafond (la somme des coupures de la formation interdirait toute relance) ne tient plus ici : les six premières marches tombées n'ont presque rien dépensé.

**Règle de la session, avant d'inscrire la ligne de relance** (le code ne la vérifie pas) : la session relève le cumul commun, l'écrit dans la colonne de référence de la ligne, et n'inscrit la ligne que si ce cumul, plus 147 dollars, plus 7,02 dollars gardés pour la relecture (5,4 heures d'une carte à 1,30 dollar de l'heure au plus), ne dépasse pas 200 dollars ; c'est-à-dire si le cumul relevé ne dépasse pas 45,98 dollars. Sinon, nœud. Avec la dépense relayée par la session de formation (environ 18,5 dollars), il reste environ 27,5 dollars pour la répétition générale et le stockage.

**C5. Une clé neuve au registre propre pour le code des relances.** La ligne `CODE-FORMATION-B5F` épingle le commit du code des premières marches et l'entropie de 128 bits ; elle n'est jamais réécrite, et aucune clé ne se double. Or le code doit changer pour C2, C3 et C4. L'additif ajoute donc une clé à la liste de la section « Lignes de registre » :

`CODE-RELANCE-FORMATION-B5F` — contenu : « `commit <40 signes>` » — inscrite après `GO-FORMATION-B5F` et avant `GO-RELANCE-FORMATION-B5F`.

- Elle épingle le commit du code que jouent les relances, et lui seul (« code v2 » : le code de `CODE-FORMATION-B5F`, plus les seuls changements que cet additif exige).
- Elle ne porte **aucune entropie**. L'entropie reste celle de `CODE-FORMATION-B5F`.
- Une première marche se compare toujours au commit de `CODE-FORMATION-B5F` ; une relance, au commit de `CODE-RELANCE-FORMATION-B5F`. Les premières marches versées ne sont donc pas touchées : leur manifeste cite le code qu'elles ont joué.
- La ligne de relance exige cette clé : sans elle, refus.
- Tout programme qui lit le registre propre après son inscription doit connaître cette clé (une clé inconnue fait refuser le registre entier). Le code de lecture, figé plus tard à `CODE-LECTURE-B5F`, part donc du code v2.

**C6. La ligne de relance cite l'accord de calcul de la formation.** Le texte faisait citer à la ligne l'accord de l'enveloppe (`GO-2026-11-19-87`). Puisque la relance entre sous le plafond commun (C4), la ligne cite l'accord de ce plafond, celui de `GO-FORMATION-B5F` : `GO-2026-11-19-86`. Le code refuse tout autre accord. Le mot de Lazar `GO-2026-11-20-51`, de type « décision », s'écrit dans la colonne de référence : la garde de calcul du dépôt n'admet qu'un accord de type « calcul » devant une commande du loueur.

**C7. Les instances de relance sont créées avant la fin des créations.** Le texte ne fixait pour la relance que la dernière heure de sa ligne (H + 54 heures) et sa fin (H + 65 heures). `GO-2026-11-20-51`, tel que la session mère le relaie, ajoute : les six relances sont créées avant la fin des créations, H + 30 heures, soit le 21 novembre 2026 à 07:30:16Z. Une relance qui n'est pas créée à cette heure ne l'est plus ; ses familles sont absentes, pour raison technique écrite. Cette échéance est tenue par la session ; le code ne la vérifie pas.

## 3. Ce qui ne change pas

- **Les familles.** Le plan des instances, les membres, la recette, les tâches, les contrôles : inchangés. Les familles d'une instance relancée sont reformées toutes, sous leur nom suffixé `-x1`.
- **Les graines.** Même entropie, celle de `CODE-FORMATION-B5F` ; graines neuves par le seul suffixe `-x1` dans le nom de la famille (point 14 du plan d'analyse). La clé d'injection de l'instance ne porte pas le suffixe, comme avant.
- **La lecture de la seule copie `-x1`.** Dès que la ligne de relance est inscrite, seule la copie `-x1` est lue pour toutes les familles des instances citées ; aucune copie n'est choisie. Les premières copies des instances 1, 2, 3, 4, 5 et 7 sont versées, inventoriées, jamais lues ni notées. Les familles de l'instance 6, non citée, sont lues dans leur première copie.
- **Les échéances.** Fin des créations à H + 30 heures ; dernière heure de la ligne de relance à H + 54 heures (le 22 novembre 2026 à 07:30:16Z) ; fin de toute relance à H + 65 heures au plus (le 22 novembre à 18:30:16Z). La ligne de relance est unique et cite d'un coup toutes les instances.
- **Les coupures par instance.** Celles du devis ; une relance prend la coupure de l'instance qu'elle remplace ; arrêt dès que le cumul de l'instance plus un quart d'heure atteint sa coupure ; arrêt et destruction par identifiant, après versement de ce qui est récupérable.
- **L'ordre des créations.** Celui du texte, sans l'instance 6 : 1, 2, 3, 4, 5, 7, au fil des offres que la garde du code accepte. Aucune borne du devis n'est desserrée.
- **Si une relance tombe à son tour.** Les familles qu'elle n'a pas achevées sont absentes, pour raison technique écrite. Les coupes de la section « Calendrier » et le point 13 de la liste d'arrêt (moins de six familles présentes) s'appliquent tels quels.
- **Tout le reste du texte** : métrique, seuil, plan d'analyse, critères de lecture, liste d'arrêt hors de la phrase du point 14 citée en C4, données gardées, engagement, relecture, ouverture, verdict.

## 4. Ordre des lignes au registre propre

Lignes ajoutées, jamais réécrites, dans cet ordre ; les instants sont strictement croissants.

1. Déjà inscrites : `SCELLEMENT-B5F`, `CODE-FORMATION-B5F`, `GO-FORMATION-B5F`.
2. `CODE-RELANCE-FORMATION-B5F`, inscrite par la session mère après le scellement de cet additif, la contre-lecture du code v2 et la vérification de ses corrections :
   `| CODE-RELANCE-FORMATION-B5F | <instant> | commit <40 signes du commit du code v2> | <référence> |`
   La référence cite : cet additif scellé (chemin et empreinte), `GO-2026-11-20-51`, le rapport du développeur et la vérification du code v2, et la mention « entropie inchangée, celle de CODE-FORMATION-B5F ».
3. `GO-RELANCE-FORMATION-B5F`, inscrite par la session mère au plus tard à H + 54 heures :
   `| GO-RELANCE-FORMATION-B5F | <instant> | GO-2026-11-19-86 ; instances 1,2,3,4,5,7 | <référence> |`
   La référence cite : `GO-2026-11-20-51` (décision de Lazar : relance des six instances, écart à « deux instances au plus » accordé, sous le plafond commun de 200 dollars), cet additif, le cumul commun relevé à l'inscription, et la mention « l'enveloppe GO-2026-11-19-87 n'est pas employée ».
4. Puis, comme dans le texte : `SORTIES-FORMATION-B5F`, puis `ENGAGEMENT-B5F` après la fin de toute relance, puis les lignes de la lecture.

Les relances partent d'un commit de course dont seul le dossier des registres diffère du commit du code v2, et dont le registre propre porte les lignes 1 à 3.

## 5. Qui tient quoi

- **Le code v2** : la clé neuve et son format ; l'exigence de cette clé par la ligne de relance et l'ordre de leurs instants ; l'accord de la ligne de relance égal à celui de `GO-FORMATION-B5F` ; six instances et 147 dollars au plus ; le code d'une relance comparé au commit de `CODE-RELANCE-FORMATION-B5F`, sur l'instance comme à l'impression de la commande de création ; les deux compteurs de dépense pour toute marche. Cas sain et artefact pour chacune de ces gardes.
- **La session de formation et la session mère** : le relevé du cumul commun, relances comprises, et la règle de C4 avant l'inscription ; les échéances H + 30, H + 54 et H + 65 heures ; l'ordre des créations ; le versement prouvé avant toute destruction.

## 6. Nœuds

Remontent à Lazar, sans rien lancer : une septième relance, ou une seconde relance d'une même instance ; des coupures de relance au-delà de 147 dollars ; un cumul commun relevé au-dessus de 45,98 dollars avant l'inscription de la ligne ; un besoin de dépasser le plafond commun de 200 dollars ; tout changement du code autre que ceux de la section 2.
