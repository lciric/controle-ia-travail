# Additif 2 au plan « sabotage ou empreinte de l'adaptateur » (barreau 5) : recréation des relances tombées avant leur marche — v4

Projet d'additif, écrit le 20 novembre 2026. La version 3, « recréation de la relance de l'instance 1 » (sha256 `82829c2a6ab853c202260c8e97ada4910f574ae1807ee4358f5636359855455b`), contre-lue et scellée par la session mère, reste archivée sans modification. Cette version 4 l'élargit à toute relance de la ligne de relance, ajoute l'exclusion de la machine d'une relance tombée, et recalcule la réserve de dépense. **Elle attend le mot de Lazar** : c'est un écart à un texte scellé, donc un nœud. Rien n'est recréé avant ce mot, la contre-lecture de ce qui est neuf et le scellement par la session mère.

Un seul mot de Lazar accorde à la fois cet additif et la destruction de chaque première tentative tombée au sens de la règle mécanique de la section 2 (pas 4 des six gestes) : celle de la relance 1 (`61655405`), et celle de toute autre relance qui tomberait de même ; la session mère le lui demande en une seule question, et le consigne en une ligne du registre des accords qui nomme l'additif et ces destructions. Les pas 1 à 3 (arrêt par identifiant, sans destruction ; inventaire ; versement prouvé des traces) n'attendent pas ce mot, comme le prévoit le plan pour un versement non prouvé ; les pas 4 à 6 l'attendent.

- **Textes visés** : le plan scellé, `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (sha256 `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`), et son additif 1 scellé, « relance des six instances », version 3 (sha256 `20e862a3155aaf7db27fd765a4b912357057e3b0cb6f4ecdd9adad3add50606a`). Aucun des deux n'est réécrit ; cet additif prime sur les seuls passages nommés à la section 3, et pour les seuls cas de la règle mécanique.
- **Ce que le rédacteur a lu** : les extraits permis du plan, l'additif 1, le code des relances (`d116bf78…`), et, dans le code de lecture figé (`c76e7916…`), les seules fonctions qui nomment la copie à lire. Les faits de la section 1 sont ceux que relaie la session mère, qui les a relevés dans la liste du loueur. Les mots « aucune autre préférence » du choix de l'offre (section 2) sont cités d'après elle : ils ne sont pas dans les extraits du rédacteur. Aucune sortie, aucun score, aucune branche de données.
- **Portée** : les relances que cite la ligne `GO-RELANCE-FORMATION-B5F` (instances 1, 2, 3, 4, 5 et 7), une recréation au plus chacune. Rien d'autre.

## 1. Les faits, sans aucune sortie lue

- La ligne `GO-RELANCE-FORMATION-B5F` est inscrite le 20 novembre 2026 à 14:40:40Z : « `GO-2026-11-19-86 ; instances 1,2,3,4,5,7` », avec en référence le code des relances `d116bf78bb2084b2d4f406535a6c6f0a23179efe`. Commit de course : `4bdf0d22e4246b4fe431bd8754e26fea4ccd037f`.
- Les six relances ont été créées entre 14:43Z et 14:46Z.
- La relance de l'instance 1 (identifiant `61655405` chez le loueur ; marche `20261120-144237-b5f-formation-1-x1` ; créée à 14:43:01Z) s'est arrêtée à 14:59:36Z sur « ARRET : installation des paquets ». Le réseau de son hôte était défaillant (git : « RPC failed … CANCEL », « early EOF »). À 15:07:27Z : « versement final incomplet ou en échec ».
- Sa marche n'a jamais commencé : l'arrêt est survenu pendant la préparation de l'instance, avant la ligne « marche : début » du journal. Aucune famille n'est entamée, aucune sortie n'existe. La branche de sortie `donnees/barreau5-familles-jumelles-v1-formation-instance-1-x1` n'existe pas sur le dépôt distant.
- **Les relances 1, 2, 3 et 4 sont sur la même machine du loueur**, `machine_id` 144450 (offres voisines 61652949, 61652947, 61652952, 61652951). La relance 5 est sur la machine 43621, la relance 7 sur la machine 43919.
- Les relances 5 et 7 marchent normalement : essais du paquet en cinq minutes environ, marche lancée vers 14:51Z et 14:53Z.
- Les relances 2, 3 et 4 n'ont écrit aucune ligne « B5F » depuis leur clonage (14:45Z à 14:46Z). Elles sont encore dans l'installation des paquets, que l'amorce borne à 3600 secondes. Elles ne sont pas tombées à l'heure où ce texte est écrit.

La cause de la chute de la relance 1 est la perte du réseau de l'hôte, assimilée à la perte de l'hôte, cause que le plan range parmi celles qui ne lisent aucune sortie. La décision de recréer ne s'appuie sur aucune sortie : il n'y en a pas.

## 2. Ce que dit l'additif

**Une relance de la ligne de relance, tombée avant le début de sa marche sur la perte du réseau ou de l'hôte, sans aucune sortie, est recréée une fois, sous le même nom.**

**Règle mécanique.** La recréation de la relance de l'instance `<n>` n'est permise que si les trois conditions suivantes sont vraies. Elles sont relevées par la session sur les seules lignes d'état de l'amorce, sur la liste du loueur et sur `git ls-remote`, sans ouvrir aucune sortie de la marche :
1. **la relance est tombée d'elle-même, sur le réseau ou l'hôte** : son journal « B5F » porte un arrêt de préparation de l'amorce qui tient au réseau (« ARRET : clonage », « ARRET : extraction partielle », « ARRET : installation des paquets », « ARRET : descente du modèle »), ou bien le loueur ne rend plus l'instance (hôte perdu). Une relance qui n'a encore écrit aucun arrêt n'est pas tombée : la session ne l'arrête pas sur une présomption, elle attend l'arrêt que l'amorce écrit elle-même (au plus 3600 secondes pour l'installation des paquets). Tout autre arrêt de préparation (carte, essais du paquet, registre, texte) n'ouvre pas la recréation : nœud ;
2. **la marche n'a jamais commencé** : le journal « B5F » de la première tentative ne porte aucune ligne « marche : début » ;
3. **la branche de sortie est absente** du dépôt distant : `git ls-remote` ne rend rien pour `refs/heads/donnees/barreau5-familles-jumelles-v1-formation-instance-<n>-x1`. Cette condition est relevée après la destruction de la première tentative.

Si l'une des trois est fausse, rien n'est recréé pour cette instance : c'est un nœud. La troisième condition est aussi tenue par le code : l'amorce de l'instance recréée s'arrête si cette branche existe (`scripts/amorce_b5f_formation_v1.sh` au commit de course, ligne 282 : `git ls-remote --exit-code origin "refs/heads/$BR"`, puis `[ $? = 2 ] || arret "branche de sortie $BR présente sur le dépôt distant (R12) ou dépôt injoignable"` ; lue par le rédacteur, attestée par la session mère).

**Ce qu'est la recréation.**
- **Une recréation au plus par relance.** Pas de seconde recréation.
- **Mêmes familles, mêmes graines.** Les familles du plan de l'instance, sous leur nom suffixé `-x1` exact (pour l'instance 1 : `T01-x1` et `T02-x1`). Les graines viennent de l'entropie de `CODE-FORMATION-B5F` et du nom de la famille : même nom, mêmes graines. Aucune copie n'est choisie, puisque la première tentative n'a rien formé.
- **Même commande, même commit de course.** La sous-commande `relance` du lanceur pour l'instance `<n>`, au commit de course `4bdf0d22…`, sous `GO_ID=GO-2026-11-19-86`. Seul l'identifiant de marche est neuf (`AAAAMMJJ-HHMMSS-b5f-formation-<n>-x1`, à l'heure de la recréation).
- **Aucun changement** du code, du registre propre, ni de la ligne de relance. Aucune ligne n'est ajoutée au registre propre pour une recréation ; la session mère la consigne dans ses registres courants.
- **Coupure : celle de l'instance** (26 dollars pour les instances 1 à 5, 17 dollars pour l'instance 7), sous le plafond commun de 200 dollars. Le cumul de l'instance recréée compte depuis sa création ; la dépense de la première tentative n'y entre pas, elle reste au compteur commun.
- **Échéances inchangées** : création avant la fin des créations, le 21 novembre 2026 à 07:30:16Z ; fin à H + 65 heures au plus (22 novembre, 18:30:16Z).

**Ordre des gestes**, tenu par la session pour chaque relance tombée, chaque pas après le précédent :
1. arrêt de la première tentative par son identifiant (pour la relance 1 : `61655405`) ;
2. inventaire de son disque ;
3. versement prouvé de ses traces sur une branche de traces à elle, `traces/barreau5-relance-<n>-premiere-tentative`, hors de l'espace `donnees/barreau5-familles-jumelles-v1-formation…`, jamais réunie à la branche de la formation ; aucun chemin de cette branche ne porte un nom de marche de la forme `AAAAMMJJ-HHMMSS-b5f-formation-<n>-x1` sous `donnees/` ;
4. destruction de la première tentative par son identifiant, sur le mot de Lazar, consignée dans le registre des arrêts ;
5. **puis seulement** relevé des trois conditions de la règle mécanique, dont `git ls-remote` ;
6. puis recréation.

**Pourquoi cet ordre et ce lieu.** Tant que la première tentative vit, un versement repris pourrait encore pousser la branche de sortie `…-formation-instance-<n>-x1` : la troisième condition ne se relève donc qu'après sa destruction. Et si des traces d'une première tentative entraient dans la branche de la formation sous un nom de marche, le code de lecture figé trouverait deux marches là où il en exige exactement une, et refuserait la lecture des familles de l'instance.

**La machine d'une relance tombée est exclue des recréations.** Le choix de l'offre, tel que le relaie la session mère, ne connaît « aucune autre préférence » que les bornes du devis. Écart, pour les seules recréations : avant de choisir une offre, la session retire de la recherche toutes les offres dont le champ `machine_id` est celui d'une relance tombée au sens de la condition 1. À ce jour : `machine_id` 144450, la machine de la relance 1. La règle est mécanique : elle ne lit que le champ `machine_id` de l'offre et la liste des relances tombées ; elle ne lit aucune sortie et ne desserre aucune borne du devis. Elle ne touche pas une relance qui marche sur cette machine. Le code ne la vérifie pas : la garde de l'offre ne lit pas ce champ.

**Réserve de dépense, tenue par la session, relevée avant chaque recréation.** Une recréation ne part que si la somme suivante ne dépasse pas 200 dollars :
- le cumul commun relevé (toutes les pièces, premières tentatives comprises) ;
- pour chaque relance ou recréation en cours, ce qui lui reste jusqu'à sa coupure ;
- la coupure de cette recréation : 26 dollars, ou 17 pour l'instance 7 ;
- 21 dollars (coupure de la relecture) et 8 dollars (coupure de la répétition générale).

Les recréations se font une à une, dans l'ordre du plan : 1, 2, 3, 4, puis 5, puis 7. La réserve est relevée à neuf avant chacune ; une recréation déjà partie compte alors parmi les marches en cours. Dès que la réserve ne permet plus la suivante, celle-ci et les autres sont un nœud.

**Calcul pour quatre recréations (instances 1, 2, 3 et 4), avec les chiffres relayés.** Cumul commun de 22,34 dollars à 15:18Z, dépense des premières tentatives des relances 1 à 4 comprise (0,6 à 0,8 dollar chacune jusque-là). Relances 5 et 7 en cours, coupures de 26 et 17 dollars. Borne haute, en comptant les restes des relances 5 et 7 à leur coupure entière :

22,34 + (26 + 17) + 4 × 26 + 21 + 8 = 22,34 + 43 + 104 + 29 = **198,34 dollars**, au plus 200. Marge : 1,66 dollar.

Cette borne compte deux fois ce que les relances 5 et 7 avaient déjà dépensé à 15:18Z : la marge vraie est un peu plus large. En sens inverse, ce que les relances 2, 3 et 4 dépensent encore avant de tomber s'ajoute au cumul commun. Le calcul dit donc que quatre recréations tiennent sous le plafond, de peu ; il ne remplace pas le relevé fait avant chacune. La répétition générale et le volume de stockage restent interdits tant qu'ils pourraient prendre la part des relances (additif 1, C4).

**Plancher.** Si une recréation tombe à son tour, pour quelque cause que ce soit, les familles qu'elle n'a pas achevées sont absentes, pour raison technique écrite ; il n'y a pas de seconde recréation. S'appliquent ensuite, tels quels, les coupes du plan, son plancher de huit familles tenues à l'écart (sous ce plancher : nœud) et le point 13 de sa liste d'arrêt (moins de six familles présentes : issue « niveau non atteignable », nœud).

## 3. Ce que l'additif remplace, pour ces seuls cas

| passage | ce qui le remplace |
|---|---|
| plan, règle de la relance : « Elle se relance une fois, entière » ; « il n'y a pas de seconde relance » | une relance de la ligne de relance, tombée avant le début de sa marche sur la perte du réseau ou de l'hôte et sans aucune sortie, est recréée une fois sous le même nom |
| plan, règle de la relance : « Si la relance tombe à son tour, les familles qu'elle n'a pas achevées sont absentes » | vaut pour l'instance recréée, non pour la première tentative d'une relance qui remplit la règle mécanique |
| additif 1, C2 : « Chaque instance reste relancée une seule fois, entière ; il n'y a pas de seconde relance » | idem |
| additif 1, section 3 : « Si une relance tombe à son tour » | idem |
| additif 1, section 6 : nœud « une seconde relance d'une même instance » | ce nœud est celui que porte cet additif ; toute recréation hors de la règle mécanique reste un nœud |
| plan, règle de la relance : versement non prouvé, « l'instance est alors arrêtée sans être détruite, et la mère reprend le versement » ; « Données gardées » : branche `…-instance-<n>-x1` d'une relance | pour la seule première tentative d'une relance recréée : traces versées sur sa branche de traces (section 2, pas 3), puis destruction sur le mot de Lazar |
| plan, lancement au fil des offres et choix de l'offre : « aucune autre préférence » que les bornes du devis | pour les seules recréations : les offres de la machine d'une relance tombée sont retirées de la recherche |
| additif 1, C3 : 147 dollars de coupures au plus | la borne de la ligne de relance ne change pas ; la coupure de chaque recréation s'y ajoute, sous la réserve de la section 2 |

Tout le reste du plan et de l'additif 1 est inchangé : lecture de la seule copie `-x1`, plafond commun, contenu de la ligne de relance, code des relances, code de lecture et son épreuve.

## 4. Pourquoi pas une copie « -x2 »

Une seconde relance sous un nom neuf (par exemple `T01-x2`, `T02-x2`) aurait des graines neuves, mais elle est impossible sans un nœud bien plus lourd. Le code de lecture, figé à `CODE-LECTURE-B5F` et dont l'épreuve à vérité plantée est passée, ne connaît que deux noms de copie : `<k>` pour une instance non relancée, `<k>-x1` pour une instance que cite la ligne de relance (`lecture_v1.prefixe_de_copie`, `exiger_copie_lue`), et il attend une seule marche de relance par instance. Une copie `-x2` demanderait de changer ce code, de le figer à nouveau et de rejouer son épreuve.

La recréation sous le même nom ne demande rien de cela, et ne coûte rien à la rigueur : aucune sortie de la première tentative n'existe, donc rien n'est écarté ni choisi ; les graines sont celles que le plan fixait pour les familles `-x1` de l'instance.

## 5. Qui tient quoi

- **Le code, sans changement** : la commande `relance` pour une instance que cite la ligne ; la branche de sortie libre, exigée par l'amorce ; la coupure de l'instance.
- **La session de formation et la session mère** : les trois conditions de la règle mécanique, écrites avec leur relevé, pour chaque relance tombée ; l'attente de l'arrêt écrit par l'amorce, sans arrêt sur présomption ; l'ordre des six gestes ; le versement des traces de chaque première tentative sur sa propre branche, hors de l'espace des branches de la formation, jamais réunie à la branche de la formation ; la destruction de chaque première tentative sur le mot de Lazar ; l'exclusion de la machine d'une relance tombée ; la réserve de dépense, relevée avant chaque recréation, et l'ordre 1, 2, 3, 4, 5, 7 ; « une recréation au plus par relance » ; l'échéance de création.

## 6. Nœuds

Remontent à Lazar, sans rien lancer : une recréation pour une instance que la ligne de relance ne cite pas, ou une seconde recréation d'une même relance ; une première tentative dont la marche a commencé, dont la branche de sortie existe, ou dont l'arrêt ne tient ni au réseau ni à l'hôte ; l'arrêt d'une relance qui n'est pas tombée d'elle-même ; une réserve de dépense dépassée ; aucune offre hors de la machine exclue avant la fin des créations ; moins de huit familles tenues à l'écart ; tout changement du code, du registre propre ou de la ligne de relance.
