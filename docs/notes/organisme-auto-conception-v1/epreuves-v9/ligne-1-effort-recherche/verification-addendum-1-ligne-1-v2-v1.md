# Vérification des corrections de l'addendum 1 au préenregistrement scellé de la ligne 1 (effort de recherche compté dans le seuil de promotion), version 2 — v1

Vérificateur : le contre-lecteur de la version 1, modèle O (classe A : la vérification des corrections est faite par le même contre-lecteur). Je n'ai écrit ni l'addendum, ni le code, ni ses rapports. Mandat : ligne GO-2026-11-19-81 (mot de Lazar du 19 novembre à 21:47:18Z, `main`, commit `d4449d327`), puis le complément du coordinateur sur les attestations. Date : 2026-11-19, après 22:01Z (temps universel). Rien lancé : ni étalonnage, ni fumée, ni course, ni essai. Aucune graine dérivée. Aucun réseau sauf `git fetch` et `git show` du dépôt, aucune écriture dans le dépôt, aucun refus d'outil. Rien n'a été touché sous `archives-reponses-modeles/`.

## Verdict

**Scellable après corrections** : quatre corrections de forme et de conduite, toutes à texte exact (§ 6). Les douze corrections de la version 1 sont faites et justes, y compris les trois adaptations aux décisions de Lazar. La matière neuve ne relâche rien du texte scellé. La condition (v) est tenue par les deux attestations versées depuis ; ce qui manque, c'est leur report aux places « À PORTER » (correction 1). La correction 3 est la seule qui touche une conduite : sans elle, la commande `tout` pourrait lancer la course décisive avant le mot de Lazar exigé par GO-2026-11-19-81.

## 1. Empreintes vérifiées par programme

| pièce | sha256 relu | état |
|---|---|---|
| addendum v2 | `b5d769739e8b3be62a802d1d689a89af1537efb55692713e71ccde451e375f57` | conforme (commit `742e5972`) |
| rapport du rédacteur v2 | `999d644668c0956a430223d6e8377140e4f79f2ace40373bd1797a27bfa9f226` | conforme |
| mandat du rédacteur v2 | `fa449b921f9cfac814a5f81a64bb1fa96dddf228135843e86ecb51789567e734` | conforme |
| ma contre-lecture v1 | `b6e64eb62715716f4746a4b83ab96e724ba7a7f196f6ec53b873b30194aee5e4` | conforme |
| addendum v1, rapport v1 | `a28db12c…`, `2112bbcd…` | intacts (R12) |
| `registres/go.md` sur `main` au commit `d4449d327` | `78efe8782883f4de91fa6d06d84d1b93498f8bb3ee5a70e111ffc2d9cd8c1275` | conforme ; ligne GO-2026-11-19-81 relue : décisions 1 A, 2 A, 3 C, et la condition sur la course décisive |
| code v2 : cinq fichiers `_v2`, essais v2, configuration v2 | empreintes du § 5.1 de l'addendum | toutes égales, compagnons conformes |
| `code-v2/` : rapport, commande, vérification, sorties d'essais et de mutations | idem | compagnons conformes ; vérification `6acbf7a6…` |
| code entre `14abb830` et `742e5972` | — | aucun fichier de code changé ; seuls la vérification, le mandat, l'addendum v2, le rapport v2 et leurs compagnons ont été ajoutés |
| attestation du développeur (commit `6f0957a7`) | `7565e0bae853fe5e30d447ae93d3a4b38c9a04466b13fd462a2ecc25d4377f15` | conforme à son compagnon |
| attestation du vérificateur (commit `6f0957a7`) | `56d7e2f6d52da254fee2998fa66f3c55c466ba0df1c713f64567a8fe8037e8e2` | conforme à son compagnon |

Lus en entier : l'addendum v2, le rapport v2, le mandat v2, la vérification du code v2 et les deux attestations. Lus en partie : la commande de lancement v2 (étapes, suivi, conditions de lancement) ; dans `lancer_ligne1_v2.py`, `main` et les retours des étapes. Je n'ai pas relu le code v2 en entier.

## 2. Les douze corrections

| n° | état | remarque |
|---|---|---|
| 1 | faite, juste | adaptée : « décidé par Lazar […] option A, GO-2026-11-19-81 » au lieu de « soumis à Lazar ». C'est juste, puisque la ligne GO accorde bien la décision 1 A. |
| 2 | faite, juste | textes exacts : frontière en virgule flottante ; conduite dès que la sortie dit la porte manquée ; reprise qui relève la garde |
| 3 | faite, juste | puces (a) à (c) exactes ; la puce (d), ajoutée par le rédacteur, est exacte d'après les pièces du code v2 ; la phrase sur le choix 1 est exacte |
| 4 | faite, juste | racine 2026111903, tâche `etalonnage|audit|classe=<classe>` ; programme à part écrit avant l'ouverture des sorties décisives ; sorties d'étalonnage gardées |
| 5 | faite, juste | raison de l'écart au choix 5 ; mot de P8 selon la lettre scellée |
| 6 | faite, juste | en cas de désaccord : aucun verdict, retour à Lazar, aucun agent ne tranche. Le recoupement du code v2 suit la même conduite. |
| 7 | faite, juste | option C portée ; plus d'écart de lettre ; conforme à la correction 8 du code, vérifiée « faite et juste » |
| 8 | faite, juste | cinq conditions ; l'état de chacune est honnête à l'écriture (voir § 4) |
| 9 | faite, juste | essais des gardes faits après le scellement, déclarés ; heure du registre ; journal du lanceur ouvert en ajout (`>>` dans la commande v2, relu) |
| 10 | faite, juste | adaptée au passé, la décision étant venue ; le rapport v2 la traite |
| 11 | faite, juste | dans le rapport v2 ; la décision 3 tombe, Lazar ayant choisi l'option C |
| 12 | faite, juste | dans le rapport v2, et réserves 5 et 6 de l'addendum ; voir § 3 pour la réserve 6 |

## 3. Matière neuve : rien ne relâche le texte scellé

- **Code v2** : la porte A15, `exiger_portes`, l'audit, la table, les prédictions et `verifier_derivations` sont identiques à la v1, d'après la vérification du code et la comparaison du rédacteur. La configuration ne diffère que par trois clés de version. Les refus de calculer ajoutés (§ 5.3) arrêtent tous sans verdict. Le recoupement du rejeu (`GardeA16Recoupement`, sous-classe de la garde A16) est un durcissement : un écart empêche de sceller le rejeu, et la garde A12 refuse alors l'analyse. Il est déclaré et sa conduite est écrite (aucun verdict, retour à Lazar). Aucun refus n'ouvre une issue de secours.
- **Noms `_v2`** (§ 5.2) : un écart de nom à l'annexe A, déclaré, sans effet sur ce qui est jugé ou lu.
- **Dépôt des sorties** (§ 9) : rien n'est effacé avant versement ; au-delà de 500 Mo, retour à la mère sans retirer un fichier ; les fichiers hors de l'empaquetage, dont le journal du lanceur, sont versés à côté ; le versement ne lève aucune règle de lecture. C'est conforme à R-3851, R-3661 et à la lettre scellée (« lieu fixé par la mère avant la course décisive »).
- **Observations du vérificateur du code** : les trois sont portées sans changement du code (§ 3, § 4.2, § 5.2, § 5.3). Pour la garde A12, la parade écrite (l'agent de l'audit relit lui-même le champ « concordant ») suffit.
- **Condition de GO-2026-11-19-81 sur la course décisive** : elle est recopiée en tête et rappelée au § 3. Mais l'addendum n'en tire pas la conséquence sur le lancement. La commande `tout` enchaîne l'étalonnage, la course décisive, le rejeu et l'analyse, et la commande v2 ne cite pas le mot de Lazar parmi ses préalables (« À ne lancer qu'après »). Un lancement de `tout` sur le seul scellement de l'addendum ferait donc partir la course décisive sans ce mot. L'interdit se trouve seulement dans le rapport v2 (décision 4), qui est une pièce de classe C. Il doit entrer dans le texte scellé (correction 3).
- **Réserve 6 (« ouverte » s'entend d'un agent ou de la mère)** : cette lecture est juste à la lettre. Par la lettre scellée, l'analyse par le programme gelé est le geste 7, avant l'audit de symétrie (geste 8). J'ai vérifié que la chaîne n'imprime aucun résultat dans ses journaux de suivi : le lanceur n'écrit que les étapes, les codes de retour, le mot du rejeu et l'empreinte de la lecture, et les gardes n'écrivent que leur propre raison. La réserve laisse pourtant le moment au choix de la mère (« le plus sûr est… ») et renvoie le point à elle si un autre lecteur comprend autrement : c'est une liberté laissée après coup. Puisque la course décisive attend de toute façon un mot de Lazar, il ne coûte rien de fixer le moment : avant ce mot (correction 4).

## 4. Les cinq conditions du scellement

| condition | état |
|---|---|
| (i) cinq choix et points de la porte inchangés entre v1 et v2 | tenue (vérification du code v2, § 1 et § 2 ; banc v1 repris à empreinte égale ; fonctions identiques) |
| (ii) chaque garde neuve éprouvée sur cas sain et artefact | tenue (vérification, corrections 1 à 8, reprise concurrente, recoupement) |
| (iii) aucune graine des racines 2026111901 à 2026111903 dérivée | tenue, d'après cinq pièces : les deux attestations ; le rapport du développeur v1 (§ 5 : « aucune racine d'étalonnage, décisive ni de rééchantillonnage dérivée pendant les essais ») ; l'en-tête de la première contre-lecture du code (« aucune racine du préenregistrement (2026111901 à 2026111903) n'a été dérivée par moi ») ; les rédacteurs et moi n'avons rien exécuté du banc |
| (iv) correction 2 du code appliquée et éprouvée | tenue (vérification, correction 2 : cas sain, trois portes manquées, fumée, sortie altérée) |
| (v) attestations écrites du développeur et du vérificateur | **tenue** depuis le commit `6f0957a7` ; à porter dans l'addendum (correction 1) |

**La condition (v) est-elle remplie ?** Oui. Chaque pièce porte la phrase demandée, signée, datée, avec la liste de ce qui a été exécuté et les racines employées (2026111900 seule). Le contrôle par programme (le dernier essai, `test_zz_aucune_racine_interdite_derivee`) a passé dans toutes les passes complètes : six chez le développeur, trois chez le vérificateur.

La limite écrite par le développeur est acceptable : ses 18 passes de mutation n'exécutent pas ce dernier essai, et pour elles l'affirmation repose sur la lecture du code. Trois raisons :
1. Le développeur la déclare lui-même et la justifie essai par essai : racine des essais, ou échec avant tout appel qui dériverait une racine.
2. Ces passes tournent dans une copie mutée du bloc-notes. Une dérivation qui s'y serait glissée n'entrerait dans aucun manifeste de la vraie course, et elle ne produirait rien qui soit lu.
3. La condition (v) protège contre un tirage d'étalonnage ou décisif fait trop tôt et vu. Une passe limitée à un seul essai, sans sortie de course, ne peut pas en être un.

La limite doit être recopiée avec l'attestation, pour que la lecture la sache (correction 1).

Le rapport v2 du rédacteur (« Trouvé en chemin », point 1) est dépassé sur ce point. C'est une pièce de classe C : aucune correction n'est demandée, mais la mère le note dans la ligne de registre.

## 5. Décision 4 (quand vient le mot de Lazar qui ouvre la course décisive) : avis

**Option A**, confiance 0,8 : un seul mot de Lazar, avant tout lancement, puis la chaîne part d'un trait, et seules les portes écrites l'arrêtent. Ce mot porte les chemins et les empreintes de quatre objets : l'addendum scellé, le code v2 et sa vérification, les deux attestations, et le programme à part de l'audit de symétrie.

C'est ce que la lettre scellée prévoit. Le geste 5 ne fait de la sortie de l'étalonnage qu'un remplissage de paramètres et un état des portes ; aucune place n'y est faite pour un regard. L'option B en ajoute un entre l'étalonnage et la course décisive, avec un écart de cartes jugées par appel attendu près du seuil. Même borné à « portes passées, empreintes conformes », ce regard ferait une porte de fait.

Les avantages de B ne sont pas perdus sous A :
- la garde A14 se contrôle après la chaîne : une dérivation trop tôt invalide la course quel que soit le moment du contrôle ;
- le versement se fait après la chaîne ou à son arrêt (§ 9, point 6).

D'accord avec le rédacteur : pas de défaut sous 48 heures, et rien ne part, ni `tout` ni l'étalonnage seul, avant le mot.

## 6. Corrections numérotées (texte exact)

1. **§ 5.4, table.** Supprimer les deux lignes en double placées juste sous l'en-tête : « | objet | valeur | » et « |---|---| ».
   - Remplacer « À PORTER par la mère » de la ligne du développeur par : « `code-v2/attestation-graines-developpeur-banc-a-v2-v1.md`, `7565e0bae853fe5e30d447ae93d3a4b38c9a04466b13fd462a2ecc25d4377f15`, commit `6f0957a7098ff0cefc8136cfd1c2d7eb3237c14c` de `lot/compte-organisme-v1`, 2026-11-19T22:01:04Z : aucune graine des racines 2026111901 à 2026111903 dérivée pendant l'écriture et les essais du code v2 ; racine 2026111900 seule ; contrôle par programme (`test_zz_aucune_racine_interdite_derivee`) passé sur les six passes complètes ; limite écrite : les 18 passes de mutation n'exécutent pas ce contrôle, et pour elles l'affirmation repose sur la lecture des essais et du code ».
   - Remplacer « À PORTER par la mère » de la ligne du vérificateur par : « `code-v2/attestation-graines-verificateur-banc-a-v2-v1.md`, `56d7e2f6d52da254fee2998fa66f3c55c466ba0df1c713f64567a8fe8037e8e2`, commit `6f0957a7098ff0cefc8136cfd1c2d7eb3237c14c`, 2026-11-19T22:00Z : aucune graine des racines 2026111901 à 2026111903 dérivée pendant la contre-lecture du code v1 et la vérification du code v2 ; trois lancements de la suite d'essais, racine 2026111900 seule, contrôle des racines passé dans chacun ; aucun étalonnage, aucune fumée, aucune course ».
2. **§ 5.4, « État de ces conditions », dernière puce.** Remplacer la puce qui commence par « (iii) et (v) : le rapport des corrections et la vérification disent tous deux… » et finit par « …la condition (v) n'est pas tenue à la lettre. » par : « (iii) et (v) : tenues. Les deux attestations de la table ci-dessus portent la phrase demandée ; pour le code v1, le rapport du développeur v1 (§ 5 : « aucune racine d'étalonnage, décisive ni de rééchantillonnage dérivée pendant les essais ») et l'en-tête de la première contre-lecture du code (« aucune racine du préenregistrement (2026111901 à 2026111903) n'a été dérivée par moi ») le disent aussi ; les rédacteurs de cet addendum et son contre-lecteur n'ont rien exécuté du banc. Limite, dite : pour les 18 passes de mutation du développeur, l'affirmation repose sur la lecture du code, non sur le contrôle par programme ; ces passes tournent dans une copie du bloc-notes et ne produisent aucune sortie de course. »
3. **§ 6, après la phrase « L'étalonnage ne part pas avant le scellement de cet addendum. »** Ajouter : « La commande `tout` enchaîne l'étalonnage et la course décisive ; or la ligne GO-2026-11-19-81 soumet la course décisive à un mot de Lazar avec chemins et empreintes. En conséquence, ni `tout` ni aucune étape lancée à la main n'est lancée avant ce mot, et l'étalonnage seul ne l'est pas non plus tant que Lazar n'a pas dit si ce mot vient avant tout lancement ou après l'étalonnage (rapport du rédacteur v2, décision 4). Si ce mot vient après l'étalonnage, il ne porte que sur « toutes les portes passées, empreintes conformes », jamais sur un chiffre de la sortie de l'étalonnage. »
4. **§ 7, réserve 6.** Remplacer « ; le plus sûr est que ce programme soit écrit, contre-lu et porté au registre avant le lancement de la course décisive. Si le vérificateur de cet addendum lit « ouverte » autrement, le point revient à la mère. » par : « ; en outre, ce programme est écrit, contre-lu et porté au registre avant le lancement de la course décisive, et son empreinte figure parmi les chemins et empreintes du mot de Lazar exigé par la ligne GO-2026-11-19-81. »

Ces quatre textes sont exacts et ne demandent aucun jugement de plus. S'ils sont appliqués à la lettre, la vérification de la version suivante se réduit à un contrôle du différentiel, et je l'accepte sous cette forme.

## 7. Limites

Je n'ai pas relu le code v2 en entier. Ce qui est dit de lui vient de sa vérification « Conforme », de la comparaison du rédacteur, de mon contrôle des empreintes et du différentiel entre commits, et de ma lecture de `main` et des retours d'étape du lanceur. Je n'ai ouvert ni les sorties d'essais, ni de mutations, ni aucune sortie de course.
