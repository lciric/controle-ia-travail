# Relecture R2, en différentiel v11 → v12, du code de la condition 6 — témoin de Bailey — arrêt autonome de l'instance — v1

- Date : Wed Nov 11 14:26 UTC 2026 (`date -u`). Relecteur : sous-agent neuf (R2). Je n'ai écrit aucune des pièces lues.
- Je reçois d'office le `CLAUDE.md` du dépôt (consignes permanentes), injecté dans mon contexte.
- Dépôt `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `76cee179`.
- Non scellé : le scellement revient à la session qui commande la relecture.

## Pièces lues et empreintes (sha256)

| Pièce | Empreinte |
|---|---|
| `prereg/temoin-attaque-publiee-bailey-v1.md` (l. 300-375 : l. 307-310, 338, 366-372, critères, liste d'arrêt) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v11-bailey-v1.md` (rapport appliqué) | `044ba3e27c38e50dece948276c986c4044424c9daa5a429a13b9244b3187fce4` |
| `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v10.md` (en-tête, lectures 22, 37, 38) | `e4579ef3e23a2b55de860d69eedd2062b8882ad926a3f5cc57b131eec1775e4c` |
| `src/controle_ia/temoin_bailey/instance_v12.py` (différentiel ; plus `requete_etat_instance`, `decider`, `ChienDeGarde` de `_battre` à `boucle`, `empreintes`) | `de46698656b56cc52389c6150af50da7d4aa6ac5120e78561bc2db1b6155086d` |
| `src/controle_ia/temoin_bailey/lanceur_v12.py` (différentiel ; plus `FournisseurVast`, `FournisseurFichier`, `Poste`, `Veilleur`, `VeilleurArret`, lanceurs et vérification des veilleurs, `Conduite._finir` à `_rapatrier`, `Reprise` en entier) | `b083fa2522651b69fb344efcfc8b81ecbcb7625efc610182454d47db493df75c` |
| `tests/test_temoin_bailey_condition6_v12.py` (aides l. 1405-1480, 1900-1945, 2320-2400 ; liste des essais v12, l. 2574-2900, en partie) | `301f9d06153636535ec158f8957369572bd24678d4ddbfe0af9a745b476f8428` |
| Sondes v11 `scratchpad/diff-c6-v11/sondes/test_sondes_v11.py` (S5 à S9) | `ee331e03065487c7c7049fe901a0be53dd8ee0e102e3e00ccd7442b1136a75c8` |
| Sondes v10 `scratchpad/diff-c6-v10/sondes/test_sondes_relecteur.py` (S1 à S4) | `157d67d98dfc2eb588d3b50834c63463aeb0e80b211d00a6a4ff260a1c93f0cc` |
| Copie de travail de la documentation publique de Vast `scratchpad/diff-c6-v10/doc/llms-full.txt` (relue hors réseau par `grep` : l. 1955-1967, 22346) | `5b201cb12430a7c8c1687ce5594de8d74ad29c0b3a14e54f1c2cecb4b3675f85` |
| Paquet installé `vastai` 1.11.0 : `cli/commands/instances.py` l. 276-365 (`start`/`stop` : ligne de succès ou `msg`), `api/instances.py` l. 320-342 (`raise_for_status`) | (non empreintés ; lus par `sed`) |

**Non lu** (cloisons) : `donnees/`, `diag/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`,
`registres/etat.md`, les lignes R-604 à R-610 de `registres/decisions.md`, tout résultat, toute note ou tout seuil de
sonde ou de moniteur, tout résultat d'attaque. Non lus non plus : le reste de `instance_v12.py` et de `lanceur_v12.py`
hors des parties citées ; `lecture_v8.py`.

**Outils** : `diff -u`, `grep`, `sed`, `sha256sum`, `pytest`, `date -u`. Aucun appel à `vastai`, aucune requête réseau,
aucune dépense, aucun commit. Aucune variable d'environnement n'a été imprimée.

**Essais** : `tests/test_temoin_bailey_condition6_v12.py` : **125 passés** (160,7 s), avec la commande prescrite.
Sondes du relecteur (fichier hors dépôt, `scratchpad/diff-c6-v12/sondes/test_sondes_v12.py`,
`7a3c60ebb435de431988b139e074fdf45dba2beabab769849ebbe866912dc842`, lancé avec
`PYTHONPATH=src:tests python -m pytest -q -p no:cacheprovider` ; import par noms, sans rejouer les essais du dépôt) :
**S1 à S9 échouent toutes** (attendu), **S10 à S13 passent** (chacune établit le fait décrit ci-dessous) : 9 échecs,
4 réussites.

## Verdict

**Conforme : l'addendum 2 peut être écrit (après le mot de Lazar sur les lectures 37 et 38).**
- Aucune correction bloquante. V-1 à V-5, Q-1, Q-2 et Q-4 sont appliquées. Leurs essais éprouvent le comportement
  (appel d'arrêt, veilleur lancé, absence de destruction, bornes), et S1 à S9 échouent sur ce comportement.
- Une correction est à faire (W-1) avant le lancement, ou à déclarer dans la lecture 22. Elle n'a aucun effet sur la
  dépense.
- Quatre points sont à préciser dans les lectures 22 et 38 (P-1 à P-4).
- Point (3) : la clé d'instance reste tenue.

## Corrections

### Bloquantes

Aucune. Je n'ai trouvé aucune suite d'événements qui laisse l'instance facturée au taux de la carte sans arrêt, hors
des risques déjà déclarés (poste éteint et chien mort, Q-5 ; coupure de 7 200 s, lecture 37 (a)). Je n'en ai trouvé
aucune non plus qui porte D au-delà de B. Voir le point 1.

### À corriger

**W-1 (point 2 ; effet de V-1 sur C-2) — conteneur « exited » voulu en marche : détruit sans transfert par le veilleur de
secours et par `_finir`, sans arrêt tenté.** `statut_vast` rend `STATUT_EN_ATTENTE` pour tout état réel arrêté
(« stopped » ou « exited ») dont l'état voulu n'est pas arrêté. Or l'état « exited » avec un état voulu « running »
n'est pas seulement l'attente d'une carte. C'est aussi, vraisemblablement (non documenté), l'état d'un conteneur dont
le processus principal est sorti. Deux causes y mènent : le **repli déclaré** du chien (TERM au PID 1 après 10 refus de
l'API, lecture 22), ou un plantage (`llms-full.txt` l. 1967 : « exited (container crashed) », « accruing disk
charges », facturation du disque seule). En v11, « exited » était gardé (C-2 : pas de destruction sans transfert qui
fait foi, « reprise requise »). En v12 :
- le veilleur de secours, au seuil, le détruit sans tenter d'arrêt (sonde **S10** : `detruites == ["77"]`, aucun appel
  à `arreter`) ;
- `_finir`, sur un transfert incomplet, le traite comme « en marche » et le détruit.

Les journaux sont perdus. Or une reprise pourrait les lire : `llms-full.txt` l. 22346 dit qu'on gère le disque d'une
instance « exited ». La lecture 22 (v10) écrit bien la règle de lecture (« jamais "arrêtée" »), mais pas cette
conséquence. Aucun effet sur la dépense : la destruction est la voie la plus sûre pour B.

Correction exacte, dans `Veilleur._passage` et `Conduite._finir`, pour `STATUT_EN_ATTENTE` (et, au choix, pour
`STATUT_ARRET_EN_COURS`, voir P-1) :
- demander l'arrêt par l'identifiant (`arreter`, R10) ; un arrêt annule aussi l'attente d'une carte ;
- relire le statut au passage suivant (veilleur), ou après `periode_prete_s` (`_finir`) ;
- arrêté, avec l'état voulu arrêté, et sans transfert complet : garder l'instance, comme C-2 (« reprise requise ») ;
- détruire seulement après `ESSAIS_DESTRUCTION` arrêts refusés, ou un statut toujours non arrêté.

Le délai ajouté, environ 2 × 30 s au taux c, tient dans la marge de 0,5 USD, comme pour V-4. Il faut ajouter l'essai
(S10 inversée) et un essai de `_finir` sur le même statut. À défaut, déclarer la conséquence dans la lecture 22 :
« conteneur sorti (repli PID 1, plantage) : détruit sans transfert au seuil ou en fin de conduite ».

### À préciser (sans effet sur la dépense ; risque à écrire exactement dans les lectures)

**P-1 (point 5 ; V-5) — le risque déclaré « arrêt que Vast mettrait plus de 180 s à rendre effectif » est inexact :
au pire, l'effet de l'arrêt n'a que 30 s.**
- Les 180 s (`ECART_SECOURS_S` = 2 × 30 + 120) couvrent d'abord le retard du veilleur d'arrêt sur sa borne (jusqu'à une
  période, 30 s), puis la durée de l'appel `vastai stop` (jusqu'à 120 s, délai de `_vast`).
- Un arrêt accepté à borne + 150 s fait passer l'état voulu à « stopped ». Le veilleur de secours, qui lit au seuil
  (borne + 180 s), trouve alors « arrêt en cours » (`STATUT_ARRET_EN_COURS`), qui n'est pas arrêté, et il détruit.
- Sonde **S11** : un effet de 31 s suffit à la destruction.
- Un appel qui expire (120 s) puis est retenté 30 s plus tard laisse 0 s.

Effet sur le budget : aucun. Le risque est exact sur ce point (destruction au seuil, la dépense ne bouge pas).
Journaux : perdus, comme déclaré. À écrire dans la lecture 38 : « effet de l'arrêt en plus de 30 s au pire (180 s
moins la période du veilleur d'arrêt et la durée de l'appel) ». Option sans coût notable : le veilleur de secours relit
une fois au passage suivant un statut « arrêt en cours » (+30 s au taux c, dans la marge de 0,5 USD).

**P-2 (point 5 ; V-1) — le risque déclaré « API qui refuserait l'arrêt d'une instance déjà arrêtée » est exact et sans
coût, mais il est incomplet.**
- Le veilleur d'arrêt ne finit jamais, puisqu'il exige un arrêt accepté. Tant qu'on ne l'arrête pas par son PID, il
  arrête aussi, dès son passage suivant, l'instance qu'une **reprise suivante** redémarre : sa borne est passée (sonde
  **S12**).
- La nouvelle reprise est alors coupée. Elle n'entraîne ni perte de journaux (transfert incomplet, remise à l'arrêt) ni
  dépassement de B (bornes de la reprise), mais elle paie un redémarrage pour rien.
- Dans le même cas, `_remettre_a_l_arret` écrit « instance non remise à l'arrêt après 3 essais » pour une instance déjà
  arrêtée.

À écrire dans la lecture 38 : avant toute nouvelle `reprendre`, arrêter par leur PID (R10) les veilleurs de
`veilleurs_arret_vivants` des bilans précédents, après en avoir vérifié l'identité. Le bilan les nomme.

**P-3 (Q-1) — `Poste.ecrire` emploie un temporaire au nom fixe (`poste-v5.json.tmp`).** Depuis Q-1, la reprise écrit le
poste pendant qu'un veilleur de secours vivant peut l'écrire aussi, après sa propre destruction. Les deux processus
partagent alors ce temporaire (sonde **S13**). Dans le pire cas, l'un des `os.replace` échoue (erreur notée), ou le
poste est mal écrit. Effet : la reprise suivante refuse le redémarrage (poste illisible, nœud) ; le veilleur de secours
garde son dernier poste lu. Rien n'est dépensé de plus. Recommandé : la même écriture que Q-4 (temporaire `.tmp-<pid>`,
`fsync`), aussi pour `_ecrire_rapatriement`.

**P-4 (point 1) — reprise sur un statut ni arrêté, ni « running », ni en attente.** La branche finale ne fait « rien »
et ne laisse aucun veilleur, que le statut soit « arrêt en cours », « loading », « unknown », « offline » ou absent.
C'est ainsi depuis la v10 pour les statuts autres que « arrêt en cours ». Pour « arrêt en cours », un arrêt a déjà été
accepté, et le chien comme le veilleur de secours bornent encore l'instance. Je n'en tire donc aucune suite d'événements
qui dépasse B. Recommandé, par cohérence avec V-2 : laisser un veilleur d'arrêt borné par le budget et l'échéance
(`borne_seule`) pour tout statut non arrêté. À défaut, l'écrire dans la lecture 38.

## Réponses point par point

1. **Instance facturée au taux de la carte sans arrêt ; dépense au-delà de B.** Aucune suite nouvelle.
   - **V-1** : `statut_vast` lit les deux états. Le veilleur d'arrêt ne finit qu'après un arrêt accepté puis un statut
     arrêté relu ; une attente de carte (« scheduling ») est arrêtée, ce qui l'annule. La remise à l'arrêt n'est
     confirmée qu'avec `accepte` et un statut arrêté. Une instance en attente trouvée par la reprise est remise à
     l'arrêt. `_prete` exige « running », état voulu compris.
   - **V-2** : la borne de budget est calculée avant tout `executer` (échéance, poste illisible, < 900 s : remise à
     l'arrêt sans transfert). Un veilleur est lancé et vu vivant avant le battement. Commande en cours ou lecture en
     échec : un veilleur borné à `min(échéance − 180 s, borne de budget)` est laissé.
   - **V-3** : `fin_prevue` est lue sous `try`. Si `observer` lève, `observer_minimal` décide sur la dépense,
     l'échéance et le battement seuls. `_age_battement` est prudent (OSError : âge compté depuis le départ du chien).
   - **V-5** : la borne de budget et l'échéance sont avancées de 180 s pour le veilleur, la minuterie, `_prete` et le
     refus du redémarrage. La minuterie reçoit l'échéance avancée.
   - Reste P-4, sans dépassement.
2. **Destruction avant le transfert et la comparaison.**
   - Reprise : destruction seulement si chaque étape attendue a un transfert qui fait foi (inchangé).
   - **V-4** : trois lectures illisibles de suite avant de détruire, une lecture lisible remettant le compte à zéro.
   - **Q-2** : pas de marque `rapatrie` sans transfert complet.
   - **W-1** : conteneur « exited » voulu en marche, détruit sans transfert. C'est un changement de la v12, non écrit
     comme conséquence.
   - **P-1** : marge réelle de 30 s pour l'effet de l'arrêt. Destruction au seuil, déclarée, sans effet sur la
     dépense.
3. **Clé d'instance.** Tenue. La v12 ne touche ni `requete_etat_instance` ni `lire_environ`.
   - `statut_vast` ne rend que des chaînes d'état. La sortie brute de `vastai show instance --raw` n'est ni journalisée
     ni écrite au bilan (seul `statut`, une chaîne, l'est). Les erreurs ne portent que le type, ou le texte d'une
     `CalledProcessError` (arguments de la commande, sans clé).
   - Les veilleurs et la minuterie ne passent aucune clé. Aucune clé du compte n'est posée sur l'instance. Conforme.
4. **Sondes.**
   - **S1 à S9 échouent toutes sur la v12**, et chacune sur son assertion de comportement :
     - S1, S2, S9 : appels d'arrêt présents ;
     - S3 : pas de transfert, pas de clé `etapes` ;
     - S4 : alerte différente ;
     - S5 : le veilleur ne finit pas ;
     - S6 : veilleur non arrêté ;
     - S7 : « reprise requise » au lieu de la destruction ;
     - S8 : `budget` au bilan.
   - Les essais inversés v12 (`test_v12_V1_*` à `test_v12_Q4_*`) éprouvent le comportement, dont un veilleur d'arrêt
     en processus réel pour un statut « stopped » d'entrée.
   - Aucun essai ne couvre W-1 (« exited » voulu en marche).
5. **Nouveaux risques déclarés.**
   - API refusant l'arrêt d'une instance déjà arrêtée : exact (`stop_instance_impl` n'imprime la ligne de succès que
     sur `success`) et sans effet sur le budget, mais incomplet (P-2).
   - Arrêt rendu effectif après plus de 180 s : sans effet sur le budget, mais le seuil est inexact. Ce sont 30 s au
     pire, non 180 s (P-1).

## Sondes (hors dépôt)

`scratchpad/diff-c6-v12/sondes/test_sondes_v12.py` (`7a3c60eb…`).

| Sonde | Statut sur la v12 | Objet |
|---|---|---|
| S1 à S9 | échouent (attendu) | défauts de la v10 et de la v11 corrigés |
| S10 | passe | W-1 : « exited » voulu en marche, détruit au seuil sans arrêt tenté ni transfert |
| S11 | passe | P-1 : effet d'arrêt de 31 s, « arrêt en cours » lu au seuil, destruction |
| S12 | passe | P-2 : veilleur d'arrêt qui ne finit pas, puis qui arrête l'instance redémarrée par une reprise suivante |
| S13 | passe | P-3 : même temporaire `poste-v5.json.tmp` pour deux processus |
