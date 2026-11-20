# Additif 2 au plan « sabotage ou empreinte de l'adaptateur » (barreau 5) : recréation de la relance de l'instance 1 — v1

Projet d'additif, écrit le 20 novembre 2026. **Il attend le mot de Lazar** : c'est un écart à un texte scellé, donc un nœud. Rien n'est recréé avant ce mot, la contre-lecture et le scellement par la session mère.

- **Textes visés** : le plan scellé, `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (sha256 `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`), et son additif 1 scellé, « relance des six instances », version 3 (sha256 `20e862a3155aaf7db27fd765a4b912357057e3b0cb6f4ecdd9adad3add50606a`). Aucun des deux n'est réécrit ; cet additif prime sur les seuls passages nommés à la section 3, et pour le seul cas de la section 1.
- **Ce que le rédacteur a lu** : les extraits permis du plan, l'additif 1, le code des relances (`d116bf78…`), et, dans le code de lecture figé (`c76e7916…`), les seules fonctions qui nomment la copie à lire. Les faits de la section 1 sont ceux que relaie la session mère. Aucune sortie, aucun score, aucune branche de données.
- **Portée** : la relance de l'instance 1, une fois. Rien d'autre.

## 1. Les faits, sans aucune sortie lue

- La ligne `GO-RELANCE-FORMATION-B5F` est inscrite le 20 novembre 2026 à 14:40:40Z : « `GO-2026-11-19-86 ; instances 1,2,3,4,5,7` », avec en référence le code des relances `d116bf78bb2084b2d4f406535a6c6f0a23179efe`. Commit de course : `4bdf0d22e4246b4fe431bd8754e26fea4ccd037f`.
- Les six relances ont été créées entre 14:43Z et 14:46Z.
- La relance de l'instance 1 (identifiant `61655405` chez le loueur ; marche `20261120-144237-b5f-formation-1-x1` ; créée à 14:43:01Z) s'est arrêtée à 14:59:36Z sur « ARRET : installation des paquets ». Le réseau de son hôte était défaillant (git : « RPC failed … CANCEL », « early EOF »). À 15:07:27Z : « versement final incomplet ou en échec ».
- Sa marche n'a jamais commencé : l'arrêt est survenu pendant la préparation de l'instance, avant la ligne « marche : début » du journal. Aucune famille n'est entamée, aucune sortie n'existe. La branche de sortie `donnees/barreau5-familles-jumelles-v1-formation-instance-1-x1` n'existe pas sur le dépôt distant.

La cause est la perte du réseau de l'hôte, cause que le plan range déjà parmi celles qui ne lisent aucune sortie. La décision de recréer ne s'appuie sur aucune sortie : il n'y en a pas.

## 2. Ce que dit l'additif

**La relance de l'instance 1 est recréée une fois, sous le même nom.**

- **Mêmes familles, mêmes graines.** Les familles `T01-x1` et `T02-x1`, sous ces noms exacts. Les graines viennent de l'entropie de `CODE-FORMATION-B5F` et du nom de la famille : même nom, mêmes graines. Aucune copie n'est choisie, puisque la première tentative n'a rien formé.
- **Même commande, même commit de course.** La sous-commande `relance` du lanceur pour l'instance 1, au commit de course `4bdf0d22…`, sous `GO_ID=GO-2026-11-19-86`. Seul l'identifiant de marche est neuf (`AAAAMMJJ-HHMMSS-b5f-formation-1-x1`, à l'heure de la recréation).
- **Aucun changement** du code, du registre propre, ni de la ligne de relance. Aucune ligne n'est ajoutée au registre propre pour cette recréation ; la session mère la consigne dans ses registres courants.
- **Avant la recréation**, la première tentative est arrêtée par son identifiant (`61655405`), son disque est inventorié, et ce qui est récupérable est versé. Ce versement ne va **pas** sur la branche de sortie `…-formation-instance-1-x1`, et n'écrit aucun dossier de marche sous `donnees/` : il va sur une branche de traces d'un autre nom, choisi par la session mère. Sinon l'amorce de l'instance recréée refuserait de partir, et le code de lecture trouverait deux marches là où il en exige une.
- **Coupure : 26 dollars**, celle de l'instance 1, sous le plafond commun de 200 dollars. La dépense de la première tentative reste dans le compteur commun.
- **Échéances inchangées** : création avant la fin des créations, le 21 novembre 2026 à 07:30:16Z ; fin à H + 65 heures au plus (22 novembre, 18:30:16Z).
- **Une seule fois.** Si l'instance recréée tombe à son tour, pour quelque cause que ce soit, les familles `T01` et `T02` qu'elle n'a pas achevées sont absentes, pour raison technique écrite. Les coupes du plan et le point 13 de sa liste d'arrêt s'appliquent.

**Règle mécanique.** La recréation n'est permise que si les deux conditions suivantes sont vraies, relevées par la session sans ouvrir aucune sortie :
1. **la marche n'a jamais commencé** : le journal « B5F » de la première tentative ne porte aucune ligne « marche : début », et son arrêt est l'un des arrêts de préparation de l'amorce (ici, « ARRET : installation des paquets ») ;
2. **la branche de sortie est absente** du dépôt distant : `git ls-remote` ne rend rien pour `refs/heads/donnees/barreau5-familles-jumelles-v1-formation-instance-1-x1`.

Si l'une des deux est fausse, rien n'est recréé : c'est un nœud. La seconde condition est aussi tenue par le code : l'amorce de l'instance recréée s'arrête si cette branche existe.

**Réserve de dépense, tenue par la session.** Avant la recréation, la session relève le cumul commun, et, pour chaque relance encore en cours, ce qui lui reste jusqu'à sa coupure. La recréation ne part que si le cumul relevé, plus ces restes, plus 26 dollars, plus 21 dollars (coupure de la relecture) et 8 dollars (coupure de la répétition générale), ne dépasse pas 200 dollars. Sinon, nœud.

## 3. Ce que l'additif remplace, pour ce seul cas

| passage | ce qui le remplace |
|---|---|
| plan, règle de la relance : « Elle se relance une fois, entière » ; « il n'y a pas de seconde relance » | la relance de l'instance 1, tombée avant le début de sa marche et sans aucune sortie, est recréée une fois sous le même nom |
| plan, règle de la relance : « Si la relance tombe à son tour, les familles qu'elle n'a pas achevées sont absentes » | vaut pour l'instance recréée, non pour la première tentative de la relance 1 |
| additif 1, C2 : « Chaque instance reste relancée une seule fois, entière ; il n'y a pas de seconde relance » | idem |
| additif 1, section 3 : « Si une relance tombe à son tour » | idem |
| additif 1, section 6 : nœud « une seconde relance d'une même instance » | ce nœud est celui que porte cet additif ; toute autre recréation reste un nœud |
| additif 1, C3 : 147 dollars de coupures au plus | la borne de la ligne de relance ne change pas ; une coupure de 26 dollars s'y ajoute pour la recréation, sous la réserve de la section 2 |

Tout le reste du plan et de l'additif 1 est inchangé : lecture de la seule copie `-x1`, plafond commun, contenu de la ligne de relance, code des relances, code de lecture et son épreuve.

## 4. Pourquoi pas une copie « -x2 »

Une seconde relance sous un nom neuf (`T01-x2`, `T02-x2`) aurait des graines neuves, mais elle est impossible sans un nœud bien plus lourd. Le code de lecture, figé à `CODE-LECTURE-B5F` et dont l'épreuve à vérité plantée est passée, ne connaît que deux noms de copie : `<k>` pour une instance non relancée, `<k>-x1` pour une instance que cite la ligne de relance (`lecture_v1.prefixe_de_copie`, `exiger_copie_lue`), et il attend une seule marche de relance par instance. Une copie `-x2` demanderait de changer ce code, de le figer à nouveau et de rejouer son épreuve.

La recréation sous le même nom ne demande rien de cela, et ne coûte rien à la rigueur : aucune sortie de la première tentative n'existe, donc rien n'est écarté ni choisi ; les graines sont celles que le plan fixait pour `T01-x1` et `T02-x1`.

## 5. Qui tient quoi

- **Le code, sans changement** : la commande `relance` pour une instance que cite la ligne ; la branche de sortie libre, exigée par l'amorce ; la coupure de l'instance.
- **La session de formation et la session mère** : les deux conditions de la règle mécanique, écrites avec leur relevé ; l'arrêt par identifiant et l'inventaire de la première tentative avant la recréation ; le versement des traces hors de la branche de sortie ; la réserve de dépense ; « une seule fois » ; l'échéance de création.

## 6. Nœuds

Remontent à Lazar, sans rien lancer : une recréation pour une autre instance, ou une seconde recréation de l'instance 1 ; une première tentative dont la marche a commencé, ou dont la branche de sortie existe ; une réserve de dépense dépassée ; tout changement du code, du registre propre ou de la ligne de relance.
