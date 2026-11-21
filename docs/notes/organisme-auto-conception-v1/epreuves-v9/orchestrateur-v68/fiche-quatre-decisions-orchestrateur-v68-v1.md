# Orchestrateur v68 de l'organisme d'idéation — fiche unique des quatre décisions pour Lazar — v1

- Auteur : rédacteur neuf, modèle F. Écrite le 2026-11-19 ; relevés de `date -u` : 22:25:19Z pendant la lecture des pièces, 22:29:34Z à la fin de l'écriture. Pièce de travail : elle propose, la mère te la soumet. Processeur seul, aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement de l'orchestrateur.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/mandat-redacteur-fiche-quatre-decisions-orchestrateur-v68-v1.md` (`fc551c3a0bc45db3933f260eb692215add08f9839b4aceac0a259f0f0b4f206f`), sur la consigne R-3861 de la mère.
- Les sources, avec chemin et empreinte, sont au rapport joint (`rapport-redacteur-fiche-orchestrateur-v68-v1.md`). Dans cette fiche, « le dossier » désigne `docs/notes/organisme-auto-conception-v1/epreuves-v9/` sur la branche `lot/compte-organisme-v1` ; `main` est lu au commit `af473a12`.

## Verdict

1. La version 68 de l'orchestrateur est contre-lue « Conforme », sans correction (`orchestrateur-v68/contre-lecture-orchestrateur-v68-v1.md`, `d2cfeac1a8d96a732c2cd9341aecc96a12778fff9b20ccfa0fef1edb2d47e325`). Elle répare ce qui arrêtait la deuxième génération, sépare deux régimes et tient un plafond de dépense sur la course entière. **Elle n'allume rien et ne permet aucune exécution réelle** : son lanceur refuse le moteur réel par construction.
2. Quatre décisions te reviennent. Mes recommandations : (1) n'autoriser d'abord que les tests de mort sans rien servir, et pour le seul palier 1 de l'héritage, comme tu l'as déjà dit ; (2) ne rien servir aux générations suivantes pour l'instant, et garder cette décision distincte de celle de l'héritage ; (3) ne pas toucher aux champs de fiche de la course d'auto-conception ; (4) louer une machine jetable pour un essai du bac à sable réel, sans appel de modèle, sur un devis de quelques dollars.
3. Un point que tu dois connaître avant de trancher la décision 2 : la lecture de la garde que tu as acceptée pour l'héritage **n'autorise pas** ce que la v68 sait servir. Elle dit que la garde interdit « les verdicts de juge et la sélection des survivants » ; or le régime de lecture de la v68 sert justement les fiches qui ont survécu.

## Ce qui existe aujourd'hui

Deux interrupteurs, éteints par défaut, qu'aucune variable d'environnement ni aucun champ de configuration ne peut allumer (contre-lecture, constats 4 et 7) :

| interrupteur | ce qu'il active | ce qui est servi aux proposeurs |
|---|---|---|
| tests de mort réels (`tests_de_mort_reels`) | un étage de tests de mort après chaque génération, la dernière comprise ; la sélection est écrite et scellée | rien |
| lecture de la sélection par la génération suivante (`lecture_selection_generation_suivante`) | la génération suivante reçoit le nom et l'énoncé des fiches retenues par l'étage, chaque ligne passée à la garde des étiquettes interdites | nom et énoncé des seules fiches « survit » ; exige l'autre interrupteur |

Le régime « éteint » est ce que le lanceur de course en place (version 10) joue déjà : une génération, aucun étage, rien de servi, à l'identique de la course v9 (`rang-0-branchement/contre-lecture-rang-0-v1.md`, `f219e7ccac946c4a985e1be3ed0b45da8cbd71f11290343ab97a35bc38a29fc9`, constat 2). Il ne demande aucune décision neuve.

Dans aucun régime le classement des juges n'est servi, et la mémoire qui évite les redites n'est jamais montrée aux proposeurs (contre-lecture de la v68, constat 6).

**Ce qui manque encore avant toute exécution réelle**, quel que soit ton choix (rapport du développeur, `orchestrateur-v68/rapport-developpeur-orchestrateur-v68-v1.md`, `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6`, § 4 et § 9) : un lanceur de course neuf (version 11) qui épingle la v68 ; un additif de préenregistrement des interrupteurs, scellé ; un devis ; une ligne d'accord qui nomme chaque interrupteur allumé ; la machine jetable et l'essai du bac à sable réel sur elle. Les deux premiers sont du travail sur processeur, sans dépense.

## Décision 1 — activation de chaque interrupteur

**Décision.** Quel interrupteur autorises-tu, pour quelle épreuve, une fois les cinq conditions ci-dessus réunies ?

**Enjeu.** Allumer change l'organisme. La mère a posé : rien en réel sans une ligne d'accord qui nomme l'interrupteur (R-3861). Tu as déjà dit, pour l'héritage, que l'activation « reste un mot à part, palier par palier, d'abord pour le seul palier 1 » (`GO-2026-11-19-76`, point 1).

Ce que chaque interrupteur coûte et débloque :

| interrupteur | coût | lignes de l'ordre de passage v3 qu'il débloque, côté orchestrateur |
|---|---|---|
| éteint | celui d'une course ordinaire ; la v9 a coûté 72,50 dollars pour une génération (devis de l'héritage v5, § 1, `30c87fa68d9d6fa5e961edc45764fe58172b1a1b20d45fd3065a678b42f2880d`) | aucune ligne neuve |
| tests de mort réels, seuls | par génération : le plafond de la génération, plus le plafond de l'étage ; **le coût réel d'un test de mort n'a jamais été mesuré** : entre 0,06 et 0,90 dollar par tentative selon les bornes écrites dans le code (même devis, § 5) ; plus la machine jetable (décision 4) | rangs 1, 2, 4, 10, 11, 14, 18, 21 ; rang 6 si son oracle lit des lois promues |
| lecture de la sélection, avec les tests de mort | le même, sans étage après la dernière génération si l'on n'en veut pas ; aucun appel de plus, mais des consignes plus longues à la génération suivante (non chiffré) | rangs 6, 7, 8, 9 (second temps), 12, 20 (second temps) ; rangs 17 et 19 non vérifiés |

La ligne d'accord doit porter le montant au pire : la v68 réserve le plafond entier de chaque génération avant de la jouer, et s'arrête plutôt que de dépasser. Une course peut donc s'arrêter alors que sa dépense réelle aurait tenu ; c'est voulu (rapport du développeur, § 8).

**Options.**
- **(a) Les tests de mort sans rien servir d'abord, pour une seule épreuve : le palier 1 de l'héritage.** La lecture reste éteinte. Le lanceur version 11 et l'additif s'écrivent en routine pour ce seul régime. Avantage : rien n'est servi à un agent, donc la garde sur la mémoire n'est pas en jeu ; c'est la première chose à mesurer (le coût réel d'un test de mort, de l'ordre de 115 dollars, plafond d'arrêt proposé 290, devis v5, § 5) ; conforme à ton mot sur l'héritage. Inconvénient : les six lignes qui demandent la lecture attendent une seconde décision.
- **(b) Les deux interrupteurs préparés ensemble**, la lecture étant autorisée dès qu'une épreuve sur monde planté la demande. Avantage : un seul additif, un seul aller-retour. Inconvénient : il faut trancher tout de suite ce qui est servi (décision 2), avant de savoir si la sélection porte un signal (rang 7) et avant le résultat du palier sur processeur de l'héritage.
- **(c) Tout reste éteint et rien ne se prépare** jusqu'à la lecture des étages sur processeur des cinq premières lignes. Avantage : aucune charge. Inconvénient : le jour où un étage payant est prêt, il attend encore le lanceur, l'additif et la machine.

**Recommandation.** (a), confiance 0,7. Ce qui me ferait changer : que le palier 1 de l'héritage ne passe pas par ce véhicule (voir la réserve en fin de fiche) ; l'ordre resterait le même, mais la première épreuve à nommer serait une autre.

**Défaut sous 48 heures.** Aucun pour l'allumage : c'est un nœud. Sans ton mot, tout reste éteint ; le lanceur version 11 s'écrit en routine, éteint, sans dépense.

## Décision 2 — ce qui est servi aux générations suivantes

**Décision.** La génération suivante peut-elle lire quelque chose de l'étage des tests de mort, et cette décision suit-elle celle que tu as prise pour l'héritage ?

**Enjeu.** La garde de l'organisme dit que la mémoire ne sert jamais de verdict aux agents. Je ne l'ai pas trouvée dans la lettre du complément 3 de N-073, qui fixe l'objet de l'héritage (un registre des tentatives, non une archive de découvertes) ; elle est écrite dans le dessin de l'organisme (inventaire des idées, ligne JUG-038, voir le rapport joint). Servir le nom d'une fiche parce qu'elle a survécu, c'est dire aux proposeurs « celle-ci a survécu » (ordre de passage v3, § 4, point 14, `b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67`).

Ce que tu as déjà accordé, pour l'héritage seulement :
- `GO-2026-11-19-76`, point 2 : `resultat` et `gardee` sont servis, « comme lecture de la garde », à revoir au point 7 du palier sur processeur. La lecture en question est écrite au devis v5, § 9 : la garde « interdit les verdicts de juge et la sélection des survivants, non la classe d'issue d'une épreuve exécutée ».
- `GO-2026-11-19-81` : aux paliers payants, l'expérimentateur des tests de mort reçoit l'engagement seul.

**Les deux objets ne sont pas les mêmes.** Le registre de l'héritage sert toutes les tentatives, gardées ou non, avec leur classe d'issue, dans une épreuve à trois bras sur monde planté. La v68 sert les seules survivantes, par leur nom et leur énoncé : c'est une sélection de survivants, le cas que la lecture acceptée range du côté interdit.

**Options.**
- **(a) Décision distincte, et rien de servi pour l'instant.** L'interrupteur de lecture reste éteint. La question « servir les survivantes » se tranche plus tard, sur pièces : le rang 7 dit si la sélection porte un signal avant d'être servie ; le rang 8 l'éprouve sur monde planté, avec un bras « mémoire factice de même forme ». Pour l'expérimentateur de l'étage, en revanche, **alignement** sur l'héritage : engagement seul, forme imposée (`GO-2026-11-19-81` ; `GO-2026-11-19-77`, héritage, décision 3), à écrire dans l'additif. Avantage : aucun écart à la garde ; aucune décision prise avant sa preuve. Inconvénient : les lignes à lecture (6, 7, 8, 9, 12, 20) n'ont pas leur étage payant tant que tu n'as pas tranché.
- **(b) Alignement complet sur l'héritage** : la génération suivante lit ce que le registre sert (toutes les tentatives, classe d'issue comprise). Avantage : une seule règle pour tout l'organisme. Inconvénient : la v68 ne sait pas le faire (elle ne sert que nom et énoncé des retenues) ; il faudrait une version de plus ; et ton accord pour l'héritage est lui-même « à revoir » après le palier sur processeur.
- **(c) Autoriser la lecture de la v68 telle quelle, comme bras d'une épreuve sur monde planté seulement**, jamais dans la course d'auto-conception. Avantage : les rangs 7 et 8 peuvent écrire leur préenregistrement et leur devis. Inconvénient : c'est un écart déclaré à la garde telle que tu l'as lue pour l'héritage ; il faut ton mot explicite, celui que le point 14 de l'ordre v3 attend déjà.

**Recommandation.** (a), confiance 0,65. Distincte pour ce que lisent les proposeurs ; alignée pour ce que reçoit l'expérimentateur. Si tu prends (c), je recommande la règle « section omise » quand aucune fiche n'a survécu (défaut de la v68) : « rien n'a survécu » est aussi une information servie.

**Défaut sous 48 heures.** Aucun : ce qui est servi à un agent est un nœud. Sans ton mot, rien n'est servi.

## Décision 3 — les champs de fiche (prédiction, signe, métrique, test de mort)

**Décision.** Ajoute-t-on ces quatre champs aux fiches de la course d'auto-conception ?

**Enjeu.** C'est un nœud : les champs de fiche font partie de la consigne servie aux proposeurs, et la course est sous un préenregistrement scellé qui écrit « pas de tests de mort » et « une seule génération » (`docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md`, `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6`, ligne 57). Les fiches actuelles ont dix champs, dont aucun des quatre (`course-v4/configuration-course-auto-conception-v5.json`, `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8`). À l'essai à blanc, l'étage a refusé chaque fiche présentée : « fiche sans champ test_de_mort » (contre-lecture du rang 0, constat 7).

**Pour les 94 cartes de la course v9 : rien ne change, quelle que soit l'option.** Elles n'ont pas ces champs et personne ne les invente après coup. Elles ne passeront jamais par l'étage des tests de mort ; elles s'éprouvent par les lignes de l'ordre de passage v3, chacune sur son banc à monde planté et sous son préenregistrement. La v68 ne leur apporte rien directement.

**Pour la prochaine course**, une difficulté de fond : une carte d'auto-conception propose un mécanisme pour l'organisme, pas une loi sur des données. Un test de mort calcule une statistique sur une colonne d'un fichier, contre un seuil ; il lui faut une tranche de données, et il n'en existe aucune pour cette course (configuration des interrupteurs, `rang-0-branchement/configuration-interrupteurs-course-auto-conception-v1.json`, `bb4ecbfb24f43d356474d301052ff8df80f829bc7a8b6c0365b64004f8608c3c`, notes). L'épreuve d'un mécanisme, c'est une course de l'organisme sur monde planté, pas un script.

**Options.**
- **(a) Ne rien changer.** La course d'auto-conception garde ses dix champs ; les tests de mort servent sur les bancs à monde planté, dont les fiches portent une loi et un test. Avantage : aucun écart au texte scellé ; la prochaine course reste comparable à la v9. Inconvénient : aucune carte de conception n'est éprouvée dans la boucle ; leur tri repose sur les lignes d'épreuve, plus lentes.
- **(b) Ajouter les quatre champs à la prochaine course.** Configuration, consigne et préenregistrement neufs, plus une tranche et une liste blanche à définir. Avantage : l'étage accepterait les fiches. Inconvénient : on ne sait pas sur quelles données un tel test porterait ; un proposeur écrit alors le test que sa carte passe (« tient » dit seulement que l'engagement a passé son propre seuil) ; la course n'est plus comparable à la v9, dont le coût a déjà été de 1,8 fois son devis.
- **(c) Ajouter prédiction, signe et métrique comme engagements scellés, sans test exécutable.** Proposition du rédacteur, que je n'ai trouvée dans aucune pièce. La carte dit d'avance ce que son épreuve sur monde planté montrerait ; le rédacteur du préenregistrement de sa ligne part de là. Avantage : la discipline de la prédiction écrite avant l'épreuve, sans étage ni machine. Inconvénient : c'est tout de même une consigne neuve et un préenregistrement neuf ; rien n'est exécuté.

**Recommandation.** (a) maintenant, confiance 0,6 ; (c) à te proposer avec le préenregistrement de la prochaine course, si tu veux des cartes qui s'engagent. Je ne recommande pas (b) tant que personne n'a dit sur quelles données le test d'une carte de conception porterait.

**Défaut sous 48 heures.** Aucun : écart à un texte scellé et changement de ce qui est servi. Sans ton mot, les champs restent ceux de la configuration v5.

## Décision 4 — une machine jetable pour le bac à sable réel

**Décision.** Autorises-tu, sur un devis à part, la location d'une machine jetable pour jouer le bac à sable réel de l'étage des tests de mort ?

**Enjeu.** Un test de mort réel exécute un script écrit par un modèle. Les relais qui portent les clés tournent sur la machine de travail : le script ne doit pas s'y exécuter. D'où la règle de l'organisme : une machine louée, sans secret, détruite après la série. L'étage a déjà tourné dans le vrai bac à sable, mais sur la machine locale et avec des scripts fixes écrits par programme (palier 0a de l'héritage, `heritage/palier-0a/rapport-palier-0a-v1.md`, `93d8a104ef551b931a6de84ecdaaca472cf05382ae49934c362e55d600058cd2`, essai E5). Restent à voir : un autre noyau, et des scripts qui ne sont pas fixes.

**Ce qu'il faut.** Une machine louée, sans aucune clé ; le bac à sable et ses outils ; une identité dédiée sans compte ; les relais hors de la machine, ou une série sans clé ; l'essai de la borne de mémoire et un étage complet rejoués sur elle avant tout appel payant ; la destruction par l'identifiant du serveur, consignée dans `registres/arrets.md` (règle R10) ; un loueur qui a la garde de calcul chargée, donc la mère ou une session exécutante, pas ce compte.

**Ordre de grandeur, sans devis.** Les machines jetables déjà louées pour l'organisme ont coûté entre 0,07 et 0,27 dollar chacune, pour 4 minutes à 3 heures 18 (`registres/depenses.md` sur `main`, `43cad7c041ba7f5da3547fa52bcfcf004a3768ebfedb202f86386e20adfe2879`, lignes du 11 et du 12 novembre). Tes lignes d'accord réservaient 3 ou 5 dollars pour ce poste (`GO-2026-11-10-11`, `GO-2026-11-12-06`, `GO-2026-11-14-14`). Pour un essai du bac seul : quelques dollars de plafond, moins d'un dollar attendu. Pour l'héritage entier, la borne écrite est de 3 290 heures d'exécution au plus (devis v5, § 5), soit de l'ordre de 200 à 250 dollars de location au tarif relevé, calcul à la main du rédacteur : une borne, pas une prévision.

**Options.**
- **(a) Un essai du bac seul, d'abord** : machine louée, aucun appel de modèle, scripts fixes ; plafond de quelques dollars. Avantage : lève une inconnue avant le premier appel payant, pour presque rien ; c'est ce que tes lignes précédentes exigeaient (« validée à blanc avant tout appel payant »). Inconvénient : un devis et un aller-retour pour une petite somme.
- **(b) La machine dans le devis du palier 1 de l'héritage**, l'essai du bac étant sa première étape, avec arrêt si elle échoue. Avantage : un seul devis, une seule ligne. Inconvénient : il faut attendre que le palier 1 soit prêt (palier sur processeur lu, lanceur, additif) pour apprendre si le bac tient sur la machine louée.
- **(c) Pas de machine.** Avantage : aucune dépense. Inconvénient : aucun test de mort réel avec un expérimentateur modèle, que tu as gardé (`GO-2026-11-19-75`) ; le palier 1 de l'héritage ne peut pas mesurer le coût d'un test ; tous les étages payants des rangs à tests de mort restent fermés. Seuls restent l'exécuteur factice et les scripts fixes en local.

**Recommandation.** (a), confiance 0,7 ; (b) est presque aussi bonne si tu veux moins d'allers-retours.

**Défaut sous 48 heures.** Aucun : c'est une dépense. Rien n'est loué sans devis et sans ta ligne.

## Lignes de l'ordre de passage v3 : bloquées sans la v68, ou non

« Bloquée » veut dire : son étage réel ou payant ne peut pas tourner dans la course à plusieurs générations de l'orchestrateur sans ce que la v68 corrige. **Aucun étage sur processeur n'est bloqué**, pour aucune ligne. Et la v68 seule ne rend aucune de ces lignes jouable en réel : il reste le lanceur version 11, l'additif, tes mots, un devis, une ligne d'accord et la machine. Source : ordre v3, § 1.2 et § 1.3 ; rapport du développeur de la v68, § 10 ; contre-lecture de la v68, constat 9.

| rang | ligne | sans la v68 | raison |
|---|---|---|---|
| 0 | branchement | sans objet | la v68 est son second livrable ; le lanceur version 10 éteint est fait |
| 1 | effort de recherche compté dans le seuil | étage payant bloqué | tests de mort réels : aucun étage après la dernière génération avant la v68 |
| 2 | ce que le nul formé des lois connues laisse passer | étage payant bloqué | même raison |
| 3 | votes effectifs des juges croisés | **non bloquée**, étage payant compris | ni test de mort ni génération suivante |
| 4 | réentrée des éliminées de peu | étage payant bloqué | tests de mort réels |
| 5 | redite par les prédictions | **non bloquée** | étage sur processeur ; rien d'autre connu |
| 6 | héritage | bloquée **si** l'épreuve se joue dans la course de l'orchestrateur ; non établi | lecture entre générations. Le rapport du palier 0a dit que l'étage peut passer par un autre chemin de l'organisme (le tour fermé), qui n'a pas besoin de la v68 |
| 7 | placebo de sélection et tranche fraîche | étage payant bloqué | tests de mort et lecture ; plus ton mot sur ce qui est servi |
| 8 | ce que la génération suivante lit | étage payant bloqué | tests de mort et lecture ; plus le nœud du point 14, sans lequel rien ne s'écrit |
| 9 | portefeuilles de survivants | second temps bloqué ; premier étage non | lecture entre générations au second temps seulement |
| 10 | jumeau permuté aux tests de mort | étage réel bloqué | tests de mort réels |
| 11 | quarantaine des exécutions avortées | étage réel bloqué | tests de mort réels |
| 12 | banque d'échecs datée | étage payant bloqué | tests de mort et lecture ; plus son nœud sur la mémoire |
| 13 | rejeu d'inertie | **non bloquée** | étage sur processeur |
| 14 | porte de version à témoins plantés | étage réel bloqué | tests de mort réels |
| 15 | choix des expériences qui départagent | **non bloquée** | à la connaissance du rédacteur de l'ordre v3 |
| 16 | certificats de portée | **non bloquée** | même réserve |
| 17 | masquage des explications servies | non vérifié | ce qui est « servi », et à qui, n'a pas été rouvert |
| 18 | paires de fusion à couverture équilibrée | étage réel bloqué | tests de mort réels |
| 19 | quotas de dépense | non vérifié | étage sur processeur non bloqué ; la suite n'a pas été regardée |
| 20 | carrés factoriels | second temps bloqué ; premier étage non | tests de mort et lecture au second temps |
| 21 | porte transactionnelle des auto-modifications | étage réel bloqué | tests de mort réels |
| 22 | arrêt sur plateau de redites | **non bloquée** | étage sur processeur |
| réservé | diriger les proposeurs vers les facettes vides | non bloquée au premier temps | un comptage sans dépense d'abord |
| réservé | fusion par conflit d'issues vérifiées | bloquée | tests de mort réels |

## Réserves

1. **Le véhicule des étages payants n'est pas établi.** Plusieurs lignes jouent leur étage payant sur un monde planté, par le lanceur de leur banc et non par celui de la course d'auto-conception (rapport du développeur, § 10). Pour ces lignes, « bloquée sans la v68 » vaut seulement si le banc passe par la course à plusieurs générations de l'orchestrateur. Le tableau reprend les listes contre-lues ; aucun banc n'a été ouvert pour le vérifier.
2. **Le code de l'orchestrateur n'est pas dans ce conteneur.** Tout ce que je dis de la v68 vient du rapport, du manifeste, du journal et de la contre-lecture.
3. **Aucun coût réel d'un test de mort n'existe.** Les chiffres de la décision 1 sont des bornes écrites dans le code, reprises du devis de l'héritage.
4. **La contre-lecture de la v68 a été faite par un contre-lecteur de repli**, le contre-lecteur prévu étant indisponible ; elle l'écrit en tête. Je la reprends telle qu'elle est.
5. Les recommandations et les confiances sont celles du rédacteur. Aucune n'a été contre-lue.
