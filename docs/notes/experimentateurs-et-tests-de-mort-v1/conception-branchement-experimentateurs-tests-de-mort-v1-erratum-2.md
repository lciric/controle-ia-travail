# Erratum 2 à la note de conception « brancher et concevoir les expérimentateurs et les tests de mort » — v1

- **Fichier corrigé** : `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md`, `4f3ae86fe2ffa8c8abeeef95a2c574e723b731db11bb3b20d65d0ab534f11298` (gardé tel quel, règle R12). La note se lit avec l'erratum 1 (`0198f5f8dc6d12e34d0beaa6493e761211ef1d613c9306dc651b432afb8f44d7`) et avec cet erratum, qui priment sur les passages qu'ils citent. Pièce de travail (classe C), non contre-lue ; aucune dépense, aucun appel payant, ni commit ni poussée.
- **Date (UTC)** : 2026-11-21, 08:16Z (`date -u`). **Rédaction** : Claude Fable 5.2, auteur de la note, sur demande de la mère.
- **Source de la correction** : contrôle du plan v3 de l'organisme pour la course principale d'auto-conception, branche `lot/compte-organisme-v1`, tête `462ae3d8b`, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v3/controle-v1/controle-plan-course-principale-v3-v1.md`, `864159fa8f0dd6d972d8c73bf6f0df4085a02d435c5dab0f2179c477ce16fdeb` (empreinte recalculée, égale au compagnon), § 3 : « Le même conflit est déjà dans la note (§ 3.1, point 1 : « l'écrire une fois, la forme d'épreuve en paramètre »). Il est à faire remonter à son auteur, avec celui du « lanceur 11 ». » Le plan v4, qui retient le partage repris ici, n'est pas encore sur la branche au moment de l'écriture : son choix est connu par le mot de la mère.
- **Ce qui fait foi** : l'additif des interrupteurs de l'orchestrateur v69, version 4, scellé (`prereg/organisme-auto-conception-v9/orchestrateur-v69/additif-interrupteurs-orchestrateur-v69-v4.md`, `cb352811f0202aa530fa4fd94de1d7ed4e6a8d589584c06c24c915e3c73bb578`), § 1.2 : « La v69 porte le palier 1. Son étage a un sommet neuf, écrit dans un fichier neuf de la v69 » ; « le mot de Lazar fait écrire la v69, le lanceur version 11 et l'additif pour ce régime et pour cette épreuve ; le palier 1 passe donc par eux » ; § 0, point 1, et § 2, C3 : tout autre régime, toute autre épreuve, reste refusé en réel, et aucune option, variable d'environnement ni champ de configuration ne le lève ; § 6, gardes 10 et 11. C'est la lettre de GO-2026-11-20-05, point 1a.

## 1. Le conflit, et la correction

**Le conflit.** La note proposait d'écrire une fois le sommet d'étage de la v69, « la forme d'épreuve en paramètre », et de loger une « table des épreuves » dans le lanceur de course 11. Or l'additif scellé réserve ce sommet et ce lanceur au seul palier 1 de l'héritage, pour une loi à forme imposée : un paramètre qui ouvrirait ce sommet à une autre épreuve en réel est justement le champ que l'additif interdit, et un greffon qui y passerait serait refusé par la garde 10 ou privé de contre-calcul (garde 11). La proposition de la note rouvrait donc un texte scellé sans le dire.

**La correction.** Un **socle commun, placé sous le sommet, écrit une fois** ; **un sommet d'étage par emploi** ; l'additif scellé intact. Le palier 1 garde le sommet et le lanceur 11 que l'additif fixe ; la course principale d'auto-conception (AC-1) écrit son propre sommet, en fichier neuf, dans AC-1, avec son propre lanceur (fondé par l'additif, § 2, C3) ; le pilier des mathématiques nouvelles et la course « seuil et moniteurs » écrivent chacun le leur. Ce que la note mettait « en paramètre » du sommet descend dans le socle, qui ne connaît aucune forme d'épreuve et reçoit de chaque sommet ce qui lui manque. La variante « le socle dans AC-1, la v69 l'appellera plus tard » n'est pas retenue : elle rouvrirait l'additif (contrôle du plan v3, § 3), ce qui serait un nœud de Lazar.

**Ce qui reste commun — le socle**, écrit une fois, en fichiers neufs hors de la v69, ou déjà existant et appelé sans modification :
- ce que l'additif fait déjà appeler « sans modification » (§ 1.2) : `preparer_generation` v53, `jouer_etage_v57`, l'étage des tests de mort v5, l'adaptateur de l'étage du tour fermé, le contrôle des parts avant l'étage ; l'enveloppe du palier 0b ;
- le **banc joueur** (erratum 1, § 1) : lots par graine, identifiants opaques, invocation du bac à chaque appel, journal chaîné ;
- le **banc noteur** : mesure hors machine, écriture des issues par une fonction dont les seules entrées sont l'engagement scellé, les décisions scellées, la vérité et le journal des coûts (note, § 2.3) ;
- le **contre-calcul** : rejeu de la part déterministe à partir des décisions enregistrées, sans exécuter l'implémentation, égalité à l'octet exigée ;
- la **porte des lots** : composition par graine avec témoins, règle de l'épreuve morte, statuts ;
- le **registre des tentatives** : ajout seul, chaîné, scellé, garde « un mort reste mort », égalité de comportement ;
- les **témoins** : les trois sortes, la table d'admission, les classes d'issue (noms de l'additif, § 4).

**Ce qui est propre à chaque emploi — le sommet**, un par emploi, chacun avec son texte (additif ou préenregistrement) et sa ligne d'accord :
- la **forme d'épreuve** (sur données, par décision, par arbitre, par course réelle ; note, § 2.2), avec son interface, sa statistique et son texte de test imposé ; le constructeur de la fiche servie et le contrôle d'après-étage ;
- la **banque de mondes** et le contenu de ses témoins ;
- le **lanceur** de la course : épinglages, relais et parts, plafonds, machine déclarée, durée de location, ligne d'accord ;
- les **gardes de la course** : conditions d'allumage, liste d'arrêt, ce qui est servi à qui.

Au palier 1, le sommet est celui de l'additif, tel quel : forme imposée du tour fermé, contre-calcul du tour fermé, lanceur 11. Rien n'y change.

## 2. Phrases touchées

1. **§ 0, point 4**, lire : « un socle commun écrit une fois, un sommet d'étage par emploi, l'additif scellé du palier 1 intact » — au lieu de : « un sommet d'étage écrit une fois ».
2. **§ 3.1, paragraphe d'entrée**, lire : « Le sommet d'étage de la v69 et le lanceur de course 11 appartiennent au palier 1 de l'héritage, par l'additif scellé `cb352811…` (§ 1.2) et GO-2026-11-20-05, point 1a. La plus petite différence : un socle commun sous le sommet, écrit une fois, en fichiers neufs hors de la v69, qui ne connaît aucune forme d'épreuve ; et un sommet par emploi, en fichier neuf, qui apporte au socle sa forme, son lanceur et ses gardes. Aucun fichier existant n'est modifié ; l'additif reste tel quel ; en réel, seule la forme imposée du tour fermé est admise tant qu'un texte scellé propre à un emploi n'en nomme pas d'autre, pour cet emploi seul. » — au lieu de : « Le sommet d'étage de la v69 est à écrire de toute façon pour le palier 1. La plus petite différence : l'écrire une fois, la forme d'épreuve en paramètre, la forme imposée du tour fermé restant la seule valeur admise en réel tant qu'un additif n'en nomme pas d'autre. Aucun fichier existant n'est modifié ; l'additif `cb352811…` reste tel quel ; chaque épreuve de plus a le sien. »
3. **§ 3.1, point 1**, lire : « **Socle commun sous le sommet, un sommet par emploi** : le socle reçoit de chaque sommet le constructeur de la fiche servie, le contrôle d'après-étage et la statistique ; il tient plusieurs générations dès l'écriture (plan, D5). Le sommet d'AC-1 s'écrit dans AC-1, en fichier neuf ; celui du palier 1 reste celui de l'additif. » — au lieu de : « **Sommet d'étage paramétré** : constructeur de la fiche servie et contrôle d'après-étage en paramètres ; plusieurs générations dès l'écriture (plan, D5). »
4. **§ 3.1, point 6**, lire : « **Table des épreuves** dans le lanceur propre à chaque emploi, jamais dans le lanceur 11 : épreuve → gabarits, banque de mondes, table d'admission, texte scellé, ligne d'accord. Étendre le régime, c'est écrire un sommet et un lanceur de plus, avec leur texte et leur ligne, non un interrupteur ni un paramètre du sommet du palier 1. » — au lieu de : « **Table des épreuves** dans le lanceur de course 11 : épreuve → gabarits, banque de mondes, table d'admission, additif, ligne d'accord. Étendre le régime, c'est y ajouter une ligne scellée, non un interrupteur. »
5. **§ 3.3, lot C3**, lire : « rejeu de l'implémentation scellée (erratum 1), hors de la v69 ; socle commun ; sommet d'AC-1 en fichier neuf dans AC-1 (le lot E1 du plan se scinde : le sommet de la v69 au palier 1, celui d'AC-1 dans AC-1) » et, pour les heures : « socle : 1 à 2 ; sommet d'AC-1 : 1 à 2 de plus, sous hypothèse (contrôle du plan v3, § 3) ; chaque autre sommet (pilier mathématique, course « seuil et moniteurs ») : du même ordre, sous hypothèse » — au lieu de : « rejeu du script scellé ; paramètre du sommet d'étage (avec le lot E1 du plan) | 1 à 2 en plus de E1 ».
6. **§ 1, table, ligne « orchestrateur v69, cadre de la v70 »**, précision sans correction : ce sommet neuf et le lanceur de course 11 sont ceux du palier 1 seul (additif, § 1.2 ; GO-2026-11-20-05, 1a).
7. **§ 4.1, dernière phrase, et § 6, N3**, précision : la « porte commune » est commune aux cartes de la course principale qui n'ont pas encore de texte scellé, et à elles seules ; chaque emploi garde son sommet et son texte. N3 ne propose pas un texte unique pour plusieurs emplois.

## 3. Ce que cet erratum ne change pas

- Les décisions N1 à N7, leurs options, recommandations, confiances et défauts.
- Les changements minimaux 2 à 5 et 7 du § 3.1, le § 3.2, les emplois et leur ordre, l'erratum 1.
- Aucun texte scellé n'est rouvert ; aucun nœud neuf pour Lazar.

## 4. Réserves

- Le plan v3, son différentiel et le plan v4 ne sont pas lus ; seul le contrôle du plan v3 l'est, par une copie dont l'empreinte est égale au compagnon.
- Que les pièces nommées « socle » se laissent appeler par plusieurs sommets sans réécriture est à établir sur le code (lots C2 et C3) ; les heures sont des ordres de grandeur sous hypothèse.
- La branche de l'organisme a été rapatriée depuis le dépôt de travail pour cette lecture (lecture seule, aucun appel payant) ; rien n'y a été écrit.
