# Relecture du différentiel v1 → v2 du code de l'idée 1.2 — v1

- Auteur : lecteur neuf, sous-agent de la session mère. Je n'ai écrit ni le préenregistrement, ni le code (v1 ou v2), ni
  ses essais, ni la contre-lecture du code, ni les rapports du développeur.
- Date (UTC) : 2026-11-15, de 12:00 à 12:30 environ. Dépôt lu sur `main`, tête `64cb67bd`.
- **Le run réel n'a pas été lancé.** Aucun commit, aucune poussée, aucun appel réseau ni payant ; rien écrit sous `diag/`,
  `donnees/`, `docs/verdicts/`, ni dans `docs/notes/organisme-idees-juge-v1/correction-poids-v1/` ; aucun fichier du dépôt
  modifié hors ce livrable et son compagnon ; aucun tirage avec la racine du texte (racines d'essai, vérifiées
  différentes). Je n'ai lu aucun chiffre de lecture : seulement des empreintes, des égalités et des comptes d'essais.
- Pièces : texte scellé **[T]** `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md` (`bdabf2bc…`) ;
  contre-lecture **[CL]** `…/code-idee-1-2-v1/contre-lecture-code-idee-1-2-v1.md` (`36ecc4a4…`) ; rapport du développeur
  **[RD2]** `…/code-idee-1-2-v1/rapport-developpeur-v2.md` (`d0280175…`). Les trois compagnons sont conformes.
- `<bloc-notes>` : dossier de bloc-notes de la session ; mes programmes et sorties y étaient sous `rl/`, supprimés à la fin
  (les programmes sont recopiés en annexe, les sorties y sont citées avec leur empreinte).

## Verdict

**« Jouable ».** Les trois majeurs de [CL] sont fermés pour la bonne raison, les neuf mineurs sont portés, et le
différentiel ne change aucun calcul, aucun bras, aucun seuil, aucune lecture du texte : sur dix générations d'essai, le
moteur v1 et le moteur v2 rendent **le même oracle et le même jeu, à l'empreinte près** (point 5). Suite : **167 sur
167** ; mutations de [CL] : **4 tuées sur 4**. Une réserve neuve, à écrire dans l'addendum sans changer le code
(point 1) : la mort d'un fils **oisif** laisse encore le parent bloqué sans `arret.json` ; fenêtre de quelques dizaines de
secondes sur le run, échec du côté sûr, consigne d'opérateur donnée. Aucune correction exigée avant l'addendum.

## Refus d'une garde pendant cette relecture (dit comme demandé)

Une de mes commandes a été refusée par la garde de calcul (`.claude/hooks/garde_calcul.py`, R10). Cause : j'avais terminé
la ligne de commande de ma sonde de l'attente bornée par un nettoyage des restes « par motif de ligne de commande », ce
que R10 interdit ; la faute est la mienne. La garde a bloqué la commande entière : rien n'en a été exécuté (le programme
de sonde n'avait même pas été écrit). Je me suis arrêté, je l'ai dit à la mère, je n'ai rien contourné. Sur sa décision,
j'ai rejoué **la sonde seule, sans la partie refusée** : elle se termine d'elle-même (délai propre). Dans le cas « fils
oisif » (point 1), deux fils orphelins sont restés ; je les ai relevés par une commande de lecture à part et arrêtés
**par leur PID** (25323 et 25366) ; relevé suivant : zéro processus. Les trois tâches lancées avant le refus (suite,
comparaison des moteurs, mutations) ont tourné sans y toucher.

## Pièces vérifiées

- Les 29 fichiers du code et des essais (18 de la v1, 11 de la v2) : `python -m controle_ia.scellement verifier` rend
  « OK » pour chacun.
- **Les 18 fichiers v1 sont inchangés** : `git diff --name-status e4411649 HEAD` sur `src/controle_ia/organisme_idees_juge`,
  `scripts`, `tests` et les quatre modules d'infrastructure ne montre que des ajouts (les 11 fichiers v2 et leurs
  compagnons) ; leurs empreintes sont celles de [RD2].
- **Les 34 lignes prêtes pour l'addendum** de [RD2] : passées à `sha256sum -c` depuis la racine du dépôt, 34 conformes,
  0 écart.

## Points

1. **Majeur 1 (fils mort) — fermé pour le cas visé ; un cas résiduel, à déclarer.**
   `execution_v2.py`, l. 80-103 : attente par pas (`resultats.next(timeout=pas)`, l. 96), garde des 24 h relue à chaque
   pas (l. 94), identités des fils comparées au départ à chaque pas et après chaque résultat (l. 99-102), fils au signal
   par défaut (l. 69-70) ; `arret.json` écrit par le lanceur (`jouer_idee_1_2_v2.py`, l. 162-164). Mes sondes (tâches
   factices) : fils tué **en calcul** → `GardeArret` « un processus fils est mort » en 2,1 s, zéro fils restant ; signal
   TERM au parent pendant l'attente → `GardeArret` « signal TERM » en 2,0 s, zéro fils restant. La borne de [T] l. 513
   est donc tenue sur l'artefact de [CL].
   **Cas résiduel (neuf)** : si le fils tué est **oisif** (il attend une tâche et tient le verrou de lecture de la file),
   la mort est bien vue, `GardeArret` est levée, mais la sortie du bloc `with` (l. 89) appelle `Pool.terminate`, qui
   attend ce verrou sans fin (`multiprocessing/pool.py`, l. 675, `_help_stuff_finish` ; pile relevée par ma sonde) : le
   parent reste bloqué, sans `arret.json`, et la garde des 24 h n'est plus relue. Un fils n'est oisif qu'en fin de phase
   (un des deux a fini sa dernière tâche, l'autre non) : quelques dizaines de secondes, trois fois dans le run. Rien n'est
   lu (pas de `jeu.json`, lecteur v2 refusant sans `journal.json`) : échec du côté sûr. Sonde complémentaire : un signal
   TERM envoyé au parent ainsi bloqué lève `GardeArret` (9,6 s), le parent sort, aucun fils ne reste ; dans le lanceur,
   cette exception est consignée dans `arret.json`.
   **Je ne demande pas de correction** (le code est gelé par nom, la fenêtre est étroite, l'issue est sûre). À écrire
   dans l'addendum : « mort d'un fils oisif : parent bloqué, non borné ; si le journal n'est pas écrit à la durée
   attendue, l'opérateur envoie TERM au parent **par son PID** ; run invalide ». Si la mère préfère corriger, le geste
   serait une v3 de `_carte` (nom neuf) : ancien `with ….Pool(…) as pool:` ; nouveau : `pool = ….Pool(…)` puis, sur mort
   de fils, `for p in pool._pool: p.kill()` avant de lever, sans passer par `terminate` — non éprouvé par moi.
2. **Majeur 2 (refus « préenregistrement non scellé ») — fermé.** `jouer_idee_1_2_v2.py`, l. 59 : `exiger_prereg` sans
   valeur par défaut ; l. 133 et l. 181 : appelée avec `RACINE_DEPOT`, la première des gardes. Essais
   (`test_organisme_idees_juge_execution_v2.py`, l. 171-200) : quatre artefacts (absent, compagnon absent, modifié puis
   rescellé, modifié), chacun avec son motif ; aucun de ces motifs n'est contenu dans le message de la garde suivante
   (« addendum d'empreintes scellé exigé »), donc une garde du préenregistrement neutralisée ferait échouer les quatre.
   Ordre : l. 203-227 épingle arbre propre, manifeste antérieur et sortie antérieure avant l'addendum. Remarque sans
   correction : l'ordre entre « préenregistrement » et « arbre propre » n'est épinglé par aucun essai (les deux refusent,
   seul le motif affiché changerait).
3. **Majeur 3 (niveau de l'intervalle, seuil bas, constantes) — fermé.** `verificateur_texte_v2.py`, l. 23-39 : constantes
   écrites à la main, que j'ai relues contre [T] : arrêt bas log(1/20) après 50 tirages et arrêt haut log(m/α) ([T]
   l. 327), blocs de 25 et plafond 800 (l. 325-326), budgets 4 800 et 6 000 (l. 279-280, l. 444), 10 000 rééchantillons
   et intervalle percentile à 95 % (l. 293-294), 20 000 générations synthétiques (l. 309), 20 000 instances d'oracle
   (l. 285), sept bras (l. 328, l. 434-447). `exiger_constantes_du_texte` (l. 42-67) est appelée au départ du lanceur
   (l. 141, l. 183), de `executer` (l. 136) et dans chaque tâche (`execution_v2.py`, l. 110, 121, 128). Niveau de
   l'intervalle : auto-contrôle avant toute lecture (`lire_banc_tirages_repartis_v2.py`, l. 33-40 et l. 52) et essai
   épinglé (`test_…_constantes_v2.py`, l. 52-65). Seuil bas : essai l. 38-49 (−2,5 non arrêtée, −3,0 arrêtée, −3,5 à
   25 tirages non arrêtée, égalités exactes). Les deux mutations survivantes de [CL] sont au banc (`mutations_v2.py`,
   l. 102-117) et meurent sur la suite (point 6).
4. **Troisième écriture des bras (`verificateur_texte_v2.py`, l. 71-134) — relue contre le moteur, équivalente ; pas de
   risque neuf d'arrêt à tort.** Tours, placebo (même graine `(f, g, 1000)`, même ordre des candidates), P′ (reprise au
   tour max(tour, 8)), G (même clé de choix) : je n'ai trouvé aucune différence de règle avec `rejeu_v1.py`, l. 107-171.
   La règle e-BH de l. 141-144 est la même formule que la seconde écriture déjà présente dans le moteur (`rejeu_v1.py`,
   l. 187-194) : elle ne peut pas lever là où la v1 ne lève pas. Sur mes dix générations d'essai, aucune levée.
5. **Aucun calcul changé — vérifié par exécution.** `execution_v2._tache_jeu` (l. 120-124) appelle `execution_v1._tache_jeu`
   puis vérifie ; `oracle_v2.table_oracle` (l. 16-19) ajoute un champ à la table v1 ; `lire` v2 (l. 51-59) appelle la
   lecture v1 puis ajoute deux clés. Comparaison (programme en annexe ; racine d'essai ; 5 générations T et 5 N, deux
   processus, E1 sauté parce que sa tâche est la même fonction dans les deux versions) :
   - oracle, hors durée et champ neuf : v1 `32a82e70c4896cdc`, v2 `32a82e70c4896cdc` — **égal** ;
   - jeu (trajectoires, allocations, valeurs e, promotions, arrêts des sept bras), hors durées et empreinte de l'oracle :
     v1 `08b58a468b0bee43`, v2 `08b58a468b0bee43` — **égal** ;
   - champ `membres_a_la_borne_triviale` : absent de la v1, présent dans les dix tables v2, aucune génération signalée ;
   - lecture v1 et lecture v2 sur la sortie v2, hors clés neuves (`oracle_membres_a_la_borne_triviale`,
     `version_lecture`, et la même clé dans `audit_R4`) : `2aa41c732a8498c3` des deux côtés — **égal** ;
   - lecture de la sortie v1 contre lecture de la sortie v2 : seules diffèrent `run_id` et `sorties_sha256` (attendu :
     l'oracle v2 porte un champ de plus, donc une autre empreinte).
   Durées murales, sous forte charge de la machine : 375 s (v1) et 266 s (v2). Sortie `4910bc29f6b10a44…`.
6. **Suite et mutations (comptes).** Dix fichiers d'essais, sans mutation : **167 passés sur 167**, 564,5 s, deux
   avertissements (point 9) ; sortie `a70cabe2bf112b5b…`. Les quatre greffons de [CL], empreintes égales à son annexe A
   (`c1f2fc4e…`, `60253624…`, `749cb52b…`, `690a4f3a…`), sur les dix fichiers :

   | mutation | sort | comptes | essais qui la tuent |
   |---|---|---|---|
   | 1 — A lit le bloc suivant hors de la garde | **tuée** | 58 échecs, 4 erreurs, 105 passés (554 s) | `rejeu_v1` 28, `constantes_v2` 28, `execution_v1` 1, `execution_v2` 1 ; erreurs : bancs v1 (3) et v2 (1) |
   | 2 — placebo ciblé | **tuée** | 50 échecs, 4 erreurs, 113 passés (351 s) | `rejeu_v1` 23, `constantes_v2` 25, `execution_v1` 1, `execution_v2` 1 ; erreurs : bancs v1 (3) et v2 (1) |
   | 3 — intervalle à 90 % | **tuée** | 4 échecs, 1 erreur, 162 passés (898 s) | `test_niveau_de_l_intervalle_epingle`, trois essais de `lecture_v2` ; erreur : banc v2 |
   | 4 — seuil bas à 1/10 | **tuée** | 35 échecs, 1 erreur, 131 passés (355 s) | `test_seuils_du_texte_epingles`, `test_constantes_du_texte…`, 29 des 30 `test_troisieme_ecriture_egale_au_moteur`, `…voit_un_seuil_partage`, `verifier_generation…`, deux essais de `execution_v2` ; erreur : banc v2 |

   Sorties : `51e8510c90b14545…`, `f1a40bca8053a175…`, `8a92a0613a4fa40a…`, `cfc9f03f50251e0c…`.
7. **Deux inexactitudes de [RD2], sans effet** (totaux justes : 58/4, 50/4, 4/1, 35/1). (a) Tableau des mutations
   rejouées : les comptes par fichier des lignes 1 et 2 sont échangés (28 et 28 vont avec 58, 23 et 25 avec 50).
   (b) Ligne 4 : « les 30 `test_troisieme_ecriture…` » ; c'est 29 (une graine ne sépare pas les deux seuils). À ne pas
   recopier tel quel dans l'addendum.
8. **Les neuf mineurs de [CL] — portés.** 1 : `oracle_v2.py`, l. 11-19, rapporté par la lecture v2 (l. 54-57), aucun
   critère touché (point 5). 2 : `lire_banc_tirages_repartis_v2.py`, l. 62-76, et `lire_idee_1_2_v2.py`, l. 50-59 ; essais
   sain et artefacts. 3 : `jouer_idee_1_2_v2.py`, l. 66-74 ; essai. 4 : l. 86-87, 114, 152 ; revérifié par le lecteur
   (l. 35-42) ; essai. 5 : l. 77-79, 129, 170 ; ma sonde TERM (point 1). 6 et 7 : lectures 19 à 21 et lecture 14 complétée
   dans [RD2], à recopier dans l'addendum. 8 : `execution_v2.py`, l. 47-48 et l. 55. 9 : messages v2 sans allocation ni
   valeur (essai l. 105-117 de `constantes_v2`) ; messages v1 gardés, comme [CL] le permettait.
9. **Réserves du développeur — acceptables pour un jeu sur processeur de quelques heures.**
   (a) *Attribut interne `Pool._pool`* : son absence lève (`execution_v2.py`, l. 73-77), pas de repli ; la version de
   Python est celle des essais (3.13.18) ; les fils ne sont jamais renouvelés hors mort (pas de `maxtasksperchild`), donc
   pas de fausse alerte. Acceptable.
   (b) *Tâche bloquée sans mort de fils, bornée par les seules 24 h* : c'est la borne que le texte demande ([T] l. 513) ;
   elle est relue toutes les 5 s et éprouvée (essai l. 64-72). Acceptable ; coût : jusqu'à 24 h de machine, 0 dollar.
   (c) *Avertissements sur `fork`* : ils ne sortent que dans les deux essais « fils mort », c'est-à-dire quand la
   bibliothèque **remplace** un fils mort pendant que ses fils d'exécution de service tournent ; le run est alors déjà
   invalide et s'arrête. Le chemin sain n'en produit pas (aucun dans ma comparaison de dix générations hors ce même
   avertissement de bibliothèque, sans effet sur l'égalité des sorties). Acceptable.
   (d) S'ajoute le cas résiduel du point 1.
10. **À régler avant le jeu, hors du code.** `exiger_depot_propre` compte les fichiers non suivis (`gardes.py`, l. 100-111) :
    le dossier non suivi `docs/notes/organisme-idees-juge-v1/correction-poids-v1/`, présent aujourd'hui, ferait refuser le
    jeu décisif (« arbre de travail non propre ») tant qu'il n'est pas versé par son auteur. Je n'y ai pas touché.

## Ce que je n'ai pas vérifié

Le run réel, E1 (sauté dans ma comparaison), le banc de mutations et la lecture avec la racine du texte ; la répétition
miniature par le lanceur lui-même (j'ai appelé les deux `executer` directement) ; la variante de correction esquissée au
point 1 ; la fréquence réelle d'une mort de fils sur cette machine.

## Annexe — programmes (bloc-notes, recopiés ; sorties supprimées après relevé de leurs empreintes)

`rl/comparer_moteurs.py` (`ee7e21d4958662bc…`) — joue `execution_v1.executer` puis `execution_v2.executer` sur la même
racine d'essai (`sha256` de la phrase « relecture du differentiel v1 -> v2, idee 1.2 (racine d'essai) », vérifiée
différente de celle du texte), `generations_miniature(5, 5)`, deux processus, `cartes_E1=()`, garde de réseau posée ;
retire `duree_s` et `membres_a_la_borne_triviale` des tables d'oracle, `duree_s`, `duree_evaluations_s` et
`oracle_scelle_sha256` des générations du jeu ; compare par égalité et par empreinte du JSON canonique ; joue
`LB1.lire` sur les deux sorties et `LB2.lire` sur la sortie v2 (1 000 rééchantillons) et n'affiche que des empreintes,
des booléens et des noms de clés.

`rl/sonde_pool.py` (`1c96efe751b9acbb…`) — `execution_v2._carte` à deux processus, pas de 1 s, tâches factices
(`time.sleep`) : cas « tué en calcul » (un fils tué par son PID après 2 s), « term » (`gardes.lever_sur_term` posé,
signal TERM au parent après 2 s), « oisif » (deux tâches, l'une de 0,5 s, l'autre de 12 s ; le fils qui a rendu la
première est tué par son PID pendant qu'il attend) ; ce dernier cas rejoué sous `faulthandler.dump_traceback_later`
(pile au point 1), puis avec un signal TERM au parent après 10 s.

`rl/lancer_mutation.sh` (`7578a15527334c05…`) — le lanceur de l'annexe A de [CL], la liste des essais portée à
`tests/test_organisme_idees_juge_*.py` (dix fichiers), greffons recopiés dans `rl/mut/`.

Sorties des sondes (lignes utiles) :

```
tue-en-calcul : GardeArret après 2.1 s : un processus fils est mort (tâche perdue) : arrêt du run ; run invalide
tue-en-calcul : fils restants : 0
term : GardeArret après 2.0 s : signal TERM reçu (délai externe du run ou plafond de l'amorce) : arrêt consigné
term : fils restants : 0
oisif : (aucun retour en 90 s ; arrêté par son propre délai)
  File "/usr/local/lib/python3.13/multiprocessing/pool.py", line 675 in _help_stuff_finish
  File "/usr/local/lib/python3.13/multiprocessing/pool.py", line 695 in _terminate_pool
  File "/usr/local/lib/python3.13/multiprocessing/pool.py", line 739 in __exit__
  File "…/src/controle_ia/organisme_idees_juge/execution_v2.py", line 89 in _carte
oisif, puis TERM au parent : GardeArret après 9.6 s : signal TERM reçu (…) : arrêt consigné ; sortie normale du parent
```
