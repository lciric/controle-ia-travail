# Mandat — correction de la conception des épreuves du devin : option (d) et ses deux ajouts (Fable 5.2, par l'abonnement)

- **Date** : 2026-11-22, vers 14:05 UTC. **Rédigé par** : la session des chantiers du 21 (Opus 5.5), qui orchestre, à la demande de la mère. Classe C.
- **Pour** : une session Fable 5.2 créée par la mère, par l'abonnement et non par l'API (règle rappelée par Lazar). **Branche** : `claude/chantiers-21-novembre-v1` du dépôt `lciric/controle-ia-travail`.
- **Décision qui fonde le mandat** : GO-2026-11-22-70. Mots de Lazar, relayés par la mère : « (d) : contrôler chaque test par admission. go » ; « go les deux » ; « go devin d ».
- **Pièce à rendre** : de classe A (correction d'une conception), donc contre-lue par un Opus neuf, puis vérifiée par le même contre-lecteur, puis scellée par la mère.

## Ce que tu dois faire

Corrige la conception scellée des épreuves du devin pour y écrire l'option (d) retenue par Lazar :
1. **Contrôle par admission** : seuil de 0,0125 par test, soit 0,05 réparti sur les quatre tests d'une admission (deux secrets, deux cibles par secret).
2. **Budget** : 8 000 épisodes par test (moitié apprentissage, moitié épreuve), soit 32 000 par admission.
3. **Premier ajout, la confirmation exacte avant toute suspension durable** (proposée dans la réponse d'Opus). Un rejet ne suspend durablement la garantie qu'après confirmation : le seul prédicteur qui a rejeté, figé, éprouvé sur des épisodes neufs à un seuil que tu fixes. Écris-en la loi, la taille, la puissance et le taux de suspensions durables à tort. Écris aussi la règle qui empêche de lever une suspension par simple reprise (la réponse d'Opus chiffre l'effondrement de puissance qu'entraînent les reprises).
4. **Second ajout, les statistiques des valeurs extrêmes pour le secret d'audit** (réponses d'Opus et de Neon). Une fuite concentrée sur peu d'épisodes peut suffire à une attaque, alors que la variation totale la retrouve mal. Ajoute à la famille, pour le seul secret d'audit, des statistiques de queue. Dis comment elles entrent dans le maximum et dans la correction, et ce qu'elles coûtent au reste de la famille.
5. **Recalcule** les tailles détectables, les seuils du cas sain et les tests de mort que ces changements touchent, chiffres rejouables à l'appui. Signale toute phrase de la conception que les changements rendent fausse.

Tu tranches aussi, dans la même pièce, les quatre points que la contre-lecture du code renvoie au concepteur (le code de la v1 en a fait des choix provisoires) :
- **l'artefact « ordre »** : décalage hors du support ou autre mécanisme (rapport du développeur, point 1 ; contre-lecture, sort du point 6) ;
- **la vue de la cible A1** : « avant chaque action », alors que l'artefact d'horodatage porte sur la durée du dernier pas, visible seulement après (point 3) ;
- **le cas hors table de l'épreuve 11** : bras fermé, devin au hasard, courbe qui ne monte pas (point 19) ;
- **le critère « croît avec λ »**, jugé sur une seule réalisation (point 20).

## Ce que tu lis (empreintes à vérifier avant de lire : `sha256sum FICHIER`)

| Fichier | sha256 |
|---|---|
| `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v3-consolidee.md` (la conception scellée, qui fait foi) | `e45bb77049937162cf3ee9608b8883b104129b42eaa3215abfcd474848687bd9` |
| `docs/notes/chantiers-21-novembre-v1/question-seuil-devin-v1/question-seuil-budget-devin-v4.md` (la question servie, corrigée : 0,14 au lieu de 0,13) | `c0ebaa6c7fbba8e678460fc4584a1c759b3829d1c557aff23167002bad029708` |
| `docs/notes/chantiers-21-novembre-v1/question-seuil-devin-v1/synthese-cinq-reponses-v1.md` | `36fbe7d8d07b49b6201f0470d1a9bd8f5fefc2627ee7c8364ed05988dea4f04c` |
| `…/question-seuil-devin-v1/reponses/opus-max/reponse-opus-max-v1.md` (source du premier ajout) | `2ec7e5561f008d8847ceba6a7588140822c7d84be7b5c1177e513e14bb00bd17` |
| `…/question-seuil-devin-v1/reponses/neon/reponse-neon-v1.md` | `4e1375648e265c8e41325c4c603039ea1dfee12f0dc14f7d978b912805ad9763` |
| `…/question-seuil-devin-v1/reponses/fable/relecture-fable-api.md` (ta réponse antérieure) | `89cd8962233cdf2019015890515e1e335b0e2b46d24dc47b00db2cba7814f411` |
| `…/question-seuil-devin-v1/reponses/argon/reponse-argon-v1.md` | `91016856820875acd9905809fb5cf75b360a2c7693bd51b886c59d4e9a1c5dea` |
| `…/question-seuil-devin-v1/reponses/carbon/reponse-carbon-v1.md` | `3b209a252185d8c60916286e87122ec51b246bf7c99d42c243823dce22f5adae` |
| `docs/notes/chantiers-21-novembre-v1/code-v1/contre-lecture-code-devin-opus-v1.md` (pour les quatre points renvoyés) | `40866478ccf1a7a97b66d7ae0cc12912bbc9a8ee11d99382094fb4ff56324986` |
| `docs/notes/chantiers-21-novembre-v1/code-v1/rapport-code-devin-v1.md` (les points ouverts du développeur) | `14c61e54b81a842d0328528e8c7e7b0b6e45203dca063e7e40c5cb736a04854e` |
| `docs/notes/chantiers-21-novembre-v1/inventaire-canaux-devins-v1.md` (ce que voit l'agent dans les harnais du dépôt) | `ddb71d9fd2d1aada8079fa929d96c1ff8a2fc4981f749d3f39d1594c07c04381` |

Si une empreinte ne concorde pas, arrête-toi et dis-le.

## Ce que tu rends, et où

1. **`docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v3-consolidee-erratum-1.md`**. En tête, il dit qu'il prime sur la v3 consolidée (`e45bb770…`). Il contient :
   - des couples ancien/nouveau, mot pour mot : chaque ancien recopié de la v3 consolidée et présent une seule fois (vérifie-le par programme), chaque nouveau dans le format de la v3 ;
   - pour chacun des quatre points renvoyés : ta décision et le couple qui l'écrit ;
   - les décisions qui reviennent encore au directeur, au format du programme ;
   - « Ce que je n'ai pas fait ».
2. **Tes calculs** sous `docs/notes/chantiers-21-novembre-v1/conceptions-v2/calculs-devin-option-d-v1/` : script Python à graines par `numpy.random.SeedSequence`, et sa sortie.
3. **Scelle** chaque fichier : `PYTHONPATH=src python -m controle_ia.scellement sceller FICHIER`. Commite et pousse sur `claude/chantiers-21-novembre-v1` seulement.

## Règles

- Écris en français, sans sigle seul. Marque chaque affirmation : FAIT RAPPORTÉ, HYPOTHÈSE, PROPOSITION, CALCUL.
- Rien n'est revendiqué. Toute antériorité est citée avec son statut (« de mémoire, non vérifiée » sauf lecture attestée).
- Aucune dépense, aucune course sur un modèle, aucun appel à un fournisseur.
- Ne lis rien sous `diag/`, `runs/`, `archives-reponses-modeles/`, `quarantaine/` ni `matiere-premiere/`, ni la branche `matiere-premiere/modes-attaque-reponse-24-fable-v1`. N'ouvre aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ». Ne lis aucun résultat cloisonné.
- Respecte la lettre des points encore ouverts chez le directeur ; ne conçois rien qui les suppose tranchés.
- Ne réécris aucun fichier scellé (R12).
- À la fin, envoie à la session des chantiers du 21 (par la mère si tu ne peux pas la joindre) le chemin et l'empreinte de l'erratum, le nombre de couples et les décisions restantes.
