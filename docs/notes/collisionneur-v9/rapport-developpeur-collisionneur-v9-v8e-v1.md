# Collisionneur v9-v8e : rapport du développeur

Écrit à 2026-11-22T07:49:03Z (`date -u`). Pièce d'instrument (classe B), Opus 5.5, session des collisionneurs, sur l'ordre de la mère du 22 novembre (07:40Z). Aucun réseau, aucune clé, aucune course. **Aucune course sur la v8e avant le feu de la mère.** Les protocoles X en cours restent sur la v8d.

## Pièces
- `collisionneur_v9_v8e.py` (0d591933…) : copie de la v8d (b7803838…, intacte), fabriquée par remplacements exacts (`fabriquer_v8e_depuis_v8d_v1.py`, chaque ancien texte présent une seule fois, empreinte de la v8d contrôlée).
- `test_collisionneur_v9_v8e.py` (40fe099c…) : 353 essais passés, 11 sautés (les mêmes que la v8d), sous `env -u` des trois clés.
- Source du texte : `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v4/relecture-fable-api.md` (c1cebee3…, sur main), « Ajout hors pièces ». Le texte servi (`FORME_IMPOSEE_DUELS`) est identique, comparé par programme, à la citation de la relecture.

## Changement, et seulement celui-là
1. **Tour III.1** : la « forme imposée » est ajoutée en fin de consigne, sur une ligne neuve, après la phrase « Livrable : (a) … (d) … ». Lecture : cette phrase unique est « la phrase qui demande les duels » (son point (b)). Autre lecture possible, non retenue sans mot de Fable : couper la phrase après le point (b).
2. **Tour III.3** : aucune phrase n'y demande de duel. **La place n'est pas tranchée** : `--place-iii3` est obligatoire à l'étage III (et au `devis` avec `--question`), parmi :
   - `fin` : après « Livrable : (a) … (c) … », en fin de consigne (même place qu'au tour III.1) ;
   - `avant-livrable` : entre « Tour III.3 : … qui visent ta proposition. » et « Livrable : ».
   Places listées, **non écrites** parce qu'elles demandent des mots que Fable n'a pas donnés : (c) au milieu du Livrable, après « (b) les expériences corrigées » ; (d) une phrase neuve qui demande des duels au tour III.3 (par exemple au point (b)). **Remarque pour Fable** : avec (a) ou (b), le tour III.3 reçoit « Avant chaque duel… » sans qu'aucune phrase ne lui demande de duel ; un tour sans duel n'est pas conforme (article 4 : n ≥ 1).
3. **Scellement et non-mélange** : les deux consignes servies sont écrites dans `consignes-etage3.json` (scellé) au premier lancement de l'étage III ; une commande suivante doit redonner la même place ; un dossier qui a déjà des essais sans ce fichier (commencé sous un autre script) est refusé, rien n'est écrit ni envoyé. `verifier` et `devis-reprise` lisent la place dans ce fichier ; un tour III.3 sans place fixée est un arrêt nommé, jamais une erreur de clé.

## Ce qui ne change pas
Tours I, II et III.2, préambule (règle B4 comprise), gardes de motifs (les balises n'y déclenchent rien : essai), critère `falsifiable_duels`, consigne E2-T1 (« quatre protocoles … en duel ») : inchangés, comparés par programme à la v8d. Aucun contrôle de conformité des balises dans les réponses : un tour non conforme n'est ni réparé ni relancé (article 4) ; le comptage appartient au code d'analyse.

## Essais
- Six essais hérités, qui reprenaient à l'étage III des dossiers commencés sous la v2 ou la v3, sont **retirés** (renommés `retire_v8e_…`, non collectés) : la v8e refuse ces reprises par construction. Remplacés par : refus d'un dossier ancien (aucune écriture, aucun envoi, devis de reprise en arrêt nommé) ; reprise d'un dossier commencé sous la v8e et son devis de reprise. Les fonctions de reprise, de rejugement et de ligne de reprise sont inchangées depuis la v8d, où ces six essais passent.
- Les essais hérités ne donnent pas `--place-iii3` : une enveloppe de l'essai l'ajoute (« fin ») à l'étage III ; les essais propres à la v8e appellent le `principal` brut.
- Neufs : texte de Fable mot pour mot et seuls changements ; option obligatoire et contrôlée ; consignes servies et scellées, pour chaque place ; balises injectées au tour III.3 sans refus de la garde ; consignes d'une autre version refusées ; code de référence de Fable sur un texte écrit selon la consigne.

## Ouvert, pour Fable par la mère
- Place au tour III.3 (ci-dessus) ; lecture de « après la phrase » au tour III.1.
- Traduction pour des cellules en anglais : la v8d n'a que des consignes en français (« Format : français ») ; aucune traduction écrite.
- Les critiques du tour III.2 voient la conception balisée et peuvent recopier des balises : sans effet sur les pistes (seuls III.1 et III.3 comptent), à savoir.
- `consignes-etage3.json` porte le nom du script : une version suivante ne reprendra pas un dossier de la v8e sans changement déclaré.
