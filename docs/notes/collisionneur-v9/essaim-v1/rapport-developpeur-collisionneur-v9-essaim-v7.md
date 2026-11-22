# Rapport du développeur : essaim v7

**En bref.** La v7 de l'essaim est écrite : elle porte les remplacements 2 à 5 de Fable dans la finale, sur le moteur
v8p. Essais : 60 passés sous `env -u` de toutes les clés (la v6 en donnait 55) ; les 7 mutations sont prises.

Pièce de classe B, écrite par Claude Opus 5.5 le 22 novembre 2026. Copie de l'essaim v6 (`90274147…`, inchangé), selon
la relecture de Fable (`28cc1d81…`). Rien n'est scellé ni commité ; aucun fournisseur n'a été appelé.

## Fichiers

Tous dans `essaim-v1/`.

| Fichier | sha256 |
| --- | --- |
| `collisionneur_v9_essaim_v7.py` | `98397f49a9366d6c79a0ad47df3e62300db4e83d97de2ac28f3a43af7b71362c` |
| `configuration-pilote-essaim-v7.json` | `301117aa…` |
| `fabriquer_essaim_v7_depuis_v6_v1.py` | `9b0e7444…` |
| `test_collisionneur_v9_essaim_v7.py` | `a14f374a…` |

Le programme de fabrication contrôle quatre empreintes : la v6, la v8p (`5979c712…`), la relecture, et la configuration.

## Changements

1. **Moteur** : la v8p, dont l'empreinte est contrôlée au chargement.
2. **Finale**, dans l'ordre :
   - le paragraphe « Temps final » (remplacement 2), au « tu » ;
   - la ligne « Livrable » neuve (remplacement 3) ;
   - la phrase du remplacement 1 et la forme imposée (remplacement 4) ;
   - la ligne de format du tour III.3 du moteur (remplacement 5). C'est la même chaîne que dans le jumeau isolé.

   La v6 servait « {Livrable du III.3} — 3 500 mots au plus. ». La ligne « Livrable » neuve la remplace en entier : le
   suffixe « — 3 500 mots au plus. » disparaît, et la limite est portée par la ligne de format. C'est une lecture du
   développeur : Fable place le bloc « avant la ligne de format », et la ligne de format est celle du tour III.3.
3. **Cycles.** Après la consigne de Fable, inchangée, chaque invite de cycle reçoit la ligne de format du tour III.3 à la
   limite du cycle (`format_cycle`) : « Format : français, Markdown, 3 000 mots au plus pour l'ensemble de la réponse.
   Termine par une ligne qui contient exactement : FIN-DE-CELLULE ».
   - La mention de la page (point (c)) n'y est pas, puisqu'elle est propre au tour III.3.
   - Les limites de chaque section (150, 600, 400 et 150 mots) restent celles de la consigne des cycles.
4. **Configuration.** `place_iii3` vaut « fin ». Seul le statut change, le reste est égal à la v6 ; un essai le vérifie.
5. **Temps 0.** Il reste l'invite III.1 du moteur, mot pour mot ; un essai le vérifie.

## Essais

Les essais sont une copie de ceux de la v6. Les accords, marqués « v7 », portent sur :
- la détection de la finale, désormais au « tu » ;
- la place « avant-livrable », refusée ;
- la ligne de format des cycles ;
- la forme imposée, que la finale porte désormais.

Les essais neufs comparent par programme les textes de la relecture, dont l'empreinte est contrôlée. Ils vérifient :
- la finale rendue, égale aux remplacements 2, 3, 1 et à la forme, suivis de la ligne de format ;
- la même chaîne dans le jumeau ;
- la ligne de format des cycles ;
- le temps 0, mot pour mot ;
- la configuration.

Les 7 mutations prises :
- E1 : finale au « vous » ;
- E2 : « Livrable » de la v6 ;
- E3 : finale sans la forme imposée ;
- E4 : finale à la ligne de format de la v8f ;
- E5 : cycles sans ligne de format ;
- E6 : limite des cycles à 3 500 ;
- E7 : finale sans la phrase.

Programme : `/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/mutations_v8p_essaim_v7.py`.

## Points ouverts

- **« Visez un dixième sous chaque limite »** est inchangé. Fable l'écrirait « neuf dixièmes de chaque limite » ; c'est
  à trancher par la mère ou par Fable.
- **Le cadre reste au « vous »** dans les phrases écrites par le développeur (« Votre dernière prépublication : », « Vos
  textes publiés : »…), et dans l'en-tête commun et les cycles. Fable n'a demandé le « tu » que pour la finale.
- **Le suffixe « — 3 500 mots au plus. » de la v6 est retiré** (voir le changement 2). Le garder doublerait la limite,
  avec un autre texte que celui de la ligne de format.
- **La ligne de format des cycles est une formulation du développeur**, tirée de la règle de Fable : il lui manquait le
  texte des cycles. Elle est à confirmer.
- **Doublon dans les cycles** : la consigne de Fable dit déjà « 3 000 mots au plus pour l'ensemble », et la ligne de
  format le redit.
