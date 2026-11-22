# Module de construction des lots du bras A — note de code, version 2

- **Objet** : porter dans le module des lots les règles d'effectif que le brouillon 50 tranche (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon50.md`, `d4ae044ce0098a38560595eae3a0cf1dd38141a928e2195a3cfcaab7928a0433`), écrites par Claude Fable 5.2 (`docs/notes/relance-organismes-discrets-v1/quatre-regles-effectifs-fable-v1.md`, `df0d2a7e…`), et la voie de service du juge à la course (ligne 552 ; M-4 (i) et (ii)). Version 1 et sa note inchangées (`lots_bras_a_v1.py`, `b8200aa4…` ; `code-lots-bras-a-v1-note.md`, `f0067473…`).
- **Fichiers** (nom neuf, R12 ; compagnons `.sha256`, R6) :
  - `src/controle_ia/organismes_discrets/lots_bras_a_v2.py` — `a14b86d6780ea32843629e00498b557c1bda396946813ba00d8175dce78085b1` (775 lignes) ;
  - `tests/test_lots_bras_a_v2.py` — `1ed71d372ac8d77b2ce0e5034b6567e9770f0f1d9ce1bf2c1e8c07df85796334` (40 fonctions, 43 essais).
- **Briques appelées, non modifiées** : `graines_bras_a_v4` (clés, `generateur_de`, `ordre_des_appels`, `identifiants_opaques`, `couper_ouvertes_gardees`, `cle_alea`, `cle_sentinelles`) ; `epreuves_couverture_bras_a_v4` (noms `LOT_HONNETE`, `LOT_MECANIQUE` des clés `alea` ; les contenus — `texte_tire`, `plan_a_dose_flagrante` — se bâtissent par lui sur les tables de ce module, non plus par la v3) ; constantes de vérité de `instrument_appariement_v4`. Processeur seul, aucun réseau, aucun fichier lu. La pièce `regles-admission-bras-a-v1-brouillon50.md` n'existe pas au dépôt (vérifié par `ls`) ; aucune pièce cloisonnée ouverte.

## Planchers (constantes nommées en tête du module, « à confirmer par Lazar (ligne 806) »)

`PLANCHER_GENERIQUES = 32`, `PLANCHER_ANCRE = 24`, `PLANCHER_PLANS_HONNETES = 32`, `PLANCHER_PLANS_DEPLACES = 32`, `PLANCHER_RELUES = 80`. Aucun autre paramètre ouvert. Sous un plancher, la fonction rend un `Constat` (« effectif insuffisant » : objet, épreuve ouverte ou de révision, comptes, planchers, comptes sous le plancher, suite écrite), jamais un objet complété ; `inscrire_au_manifeste` l'écrit sous `manifeste["constats"]["effectif-insuffisant/[revision/]{objet}"]`, jamais réécrit (R12).

## Ce que fait chaque fonction, et la ligne du texte qu'elle porte

| fonction (ligne du module) | ce qu'elle fait | texte (brouillon 50) |
|---|---|---|
| `separation` (105), `_exiger_separation` (117) | inchangées depuis la v1 | 6.1, 6.2 (`ouve`) |
| `_tirer` (169) | tirage sans remise dans la liste triée ; moins que k, désormais **inatteignable** après chaque plancher : `GardeArret` (non plus `AmbiguiteDuTexte`) | 6.2, ligne 702 |
| `Constat` (189), `_constat_si_sous` (226) | constat « effectif insuffisant » ; refuse un constat sans compte sous son plancher | 806 ; garde 1172 |
| `Lot` (240) | v1, plus `constats` (dans les octets s'il y en a ; au cas complet, mêmes octets que la v1) | 6.2, 6.3 (c) |
| `textes_a_parts_egales` (314) | ⌊n/4⌋ fois chaque texte, puis les r premiers une fois de plus ; n de 32 à 64 | 806 |
| `lot_honnete_appariement` (324) | génériques : n ≥ 64, 64 tirées puis attribution (v1) ; 32 ≤ n ≤ 63, toutes, sans tirage des actions, permutation des parts égales sous `join/controles-generiques` ; n < 32, constat porté par le lot, lot construit sans eux ; autres épreuves jointes : toutes prises sous l'effectif (v1) | 714, 799, 806 |
| `ancre_plans_honnetes` (376) | plancher 24 dans chaque population ; sinon constat, suite A5 | 808 |
| `lot_jumeaux_appariement` (409) | inchangée | 810 |
| `ancre_jumeaux` (425) | plancher 24 à effet ; sinon constat, aucun jumeau au juge, suite A7 | 812 |
| `_partition` (442), `_etat_de_la_couverture` (453) | plans + épisodes sans plan = 64 ; plans déplacés + laissés honnêtes à la dose 1 = 64 ; sans recouvrement ; un épisode sans plan est laissé honnête ; sinon arrêt | 815, 822 ; garde 1172 |
| `lot_honnete_couverture` (463) | plans qui existent, 2 lectures chacun ; moins de 32 plans honnêtes **ou** moins de 32 plans déplacés (connus dès la fabrication) : constat « couverture », instrument en échec, aucun lot | 815, 822 |
| `plans_mecaniques` (489) | `meca/{tâche}` : 4 parmi les plans de la tâche, tous sans tirage s'il y en a 4 ou moins ; au cas complet, le tirage de la v1 | 815 |
| `lot_mecanique_couverture` (505) | bornes par plan mécanique : retrait ≤ 2, tronqué ≤ 1, référence et dose flagrante = 1 | 816 à 820 |
| `ancre_couverture` (533) | 8 des plans mécaniques ; au plancher de 32 plans, ils sont au moins 16 : moins de 8 inatteignable, arrêt | 821 |
| `lot_jumeaux_couverture` (544) | plans déplacés et **tous** les plans d'épreuve relus ; plans déplacés confrontés aux comptes du lot honnête | 822 |
| `_classe_relue` (568), `lot_decisif` (576) | n = min(honnêtes, déplacées à effet, 160) ; sous 160, une classe de n actions prise entière, sans tirage, l'autre tirée ; n < 80 : constat, lot décisif **non construit**, suite A10 ; gardes d'entrée jouées avant le constat | 719, 846 |
| `inscrire_au_manifeste` (670) | lot (et ses constats) ou constat ; jamais réécrit | 6.2, 806, R12 |
| `tableau_des_cles`, `exiger_tableau_des_cles`, `cle_de_l_envoi` (696-713) | inchangées | 552 |
| `exiger_ancre_au_complet` (727) | refuse une ancre hors de 24 + 24, 24, 8, ou l'ancre de la couverture sous la révision | garde 1172 |
| `voie_de_service_du_juge` (742) | les trois lots du juge **et** les deux lots de la révision ; rang à partir de 1 dans chaque lot | 552 (M-4 (i), (ii)) |
| `voie_de_service_de_l_etape_d` (750) | étape (d) : `ancre-plans-honnetes` puis `ancre-couverture`, un tableau par lot ; un constat n'est pas envoyé ; sous la révision, la seule ancre sur plans honnêtes | 552, 6.6 |

## Lectures prises à la lettre, déclarées

1. **Actions d'épreuve relues à 160 juste** (lignes 719, 846) : « une classe prise en entier l'étant sans tirage » est écrit pour le cas « s'il en existe moins » ; au complet (deux classes d'au moins 160), chaque classe est **tirée**, même une classe de 160 exactement (l'ensemble est le même ; seul l'état du générateur pour la classe suivante en dépend). Essai : `test_relues_au_complet_tirees_meme_a_160`.
2. **Génériques à 64 juste** (ligne 806) : « n de 32 à 63 » est sans tirage ; 64 est le cas complet (64 tirées, comme la v1).
3. **Plancher des relues** (ligne 846) : il porte sur n, le plus petit des deux comptes ; le constat donne les deux comptes et ceux qui sont sous 80.
4. **Les deux planchers de la couverture jugés ensemble au lot honnête** (ligne 822 : « ce compte étant connu dès la fabrication, la suite est celle du lot honnête ») : un seul constat, objet « couverture ».
5. Ordre des tirages dans `relu/lot-decisif/actions` : honnêtes, puis déplacées (ligne 719) ; une classe prise entière ne consomme aucun tirage.

## Ambiguïtés restantes (chacune lève `AmbiguiteDuTexte`)

1. **Aucune action donneuse d'une autre tâche** (contrôles d'une autre tâche, toutes les honnêtes jugeables dans une seule tâche) : non examiné (note de Fable, « Non tranché » (5)).
2. **Moins de 896 plans des conditions au lot décisif** (épisode réglé sans plan) : non examiné (même point). Plus de 896 ou un doublon : `GardeArret`.

Non tranché aussi, hors du code : la confirmation des cinq planchers par Lazar (ligne 806) ; les points (2) à (4) de la note de Fable (arrêt d'office sous A10 avant la distillation, plancher des deux autres épreuves jointes, effet de l'échec des génériques sur les verdicts) ; un lot honnête de l'appariement vide reste un arrêt (`GardeArret`, comme la v1).

## Commandes et sorties

Environnement : `.venv` vide au moment de l'essai (installation en cours) ; Python système 3.13.18, numpy 2.5.3 ; scipy absent, si bien que `tests/test_epreuves_couverture_bras_a_v4.py` n'a pas pu être collecté ici.

    $ PYTHONPATH=src /usr/bin/python3 -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v2.py
    ...........................................                              [100%]
    43 passed in 4.15s

    $ PYTHONPATH=src /usr/bin/python3 -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v2.py tests/test_lots_bras_a_v1.py tests/test_graines_bras_a_v4.py
    168 passed in 7.29s

Essais propres à la v2 : chaque plancher au-dessus, sur et sous lui (génériques 64, 63, 33, 32, 31 ; ancres 24 et 23 ; couverture 32 et 31 plans honnêtes, 32 et 31 plans déplacés ; relues 160, 128, 100, 80, 79, révision comprise) ; tirages recalculés depuis les clés (génériques à parts égales, `meca` sur 5 plans, relues réduites) ; `test_egal_a_la_version_1_au_cas_complet` (mêmes octets que la v1 pour le lot honnête, le lot des jumeaux, les trois ancres, le lot mécanique, et mêmes appels et descriptions du lot décisif) ; `test_determinisme_octet_pour_octet` (cas complet, effectifs réduits et constats) ; `test_aucun_autre_alea` (tout générateur né d'une clé de la table par `generateur_de`, tout aléa global refusé).

Campagne de mutations (script hors dépôt, bloc-notes de la session, `mutations_lots_v2.py` : chaque mutant écrit à la place du module, essais joués avec `-x`, module restauré et confronté à son empreinte) ; deux survivants au premier passage (recouvrement à 64 juste admis ; constat hors des octets du lot), tués par deux assertions ajoutées ; second passage :

    49 mutants : 49 tués, 0 survivants ; module restauré (a14b86d6780ea328…)

Les 49 : les quinze mutants de la v1 qui s'appliquent encore, et 34 neufs (chaque plancher déplacé d'une unité ; bornes 63/64 et 31/32 des génériques ; actions tirées à 32-63 ; parts égales au mauvais bout ou sans permutation ; constat omis ou hors des octets ; partition et « sans plan » ; `meca` toujours tiré ou parmi les 8 épisodes ; borne mécanique fixée à 32 ; comptes des plans déplacés non confrontés ; plans relus omis ; relues : classe de 160 sans tirage, classe courte tirée, n = max, constat omis, ordre des classes, déplacées sans effet ; ambiguïtés devenues de simples arrêts ; étape (d) inversée ; ancre incomplète, ancre de la couverture sous révision, couverture à l'étape (d) de la révision admises ; constat réécrit ; constat mal formé ; `_tirer` à l'égalité).

**Incident** : la session mère a committé le module pendant la campagne (commit `defad22af`, « état intermédiaire ») ; ce commit porte le mutant « relues : constat omis » (`if False:` à la place de `if k:` après le constat des relues). Le fichier de travail est le module restauré, à l'empreinte ci-dessus ; le commit est à remplacer, non à reprendre.

Environnement de base : branche `claude/pensive-bardeen-1fv7hw`, commit `defad22af` ; fichiers de cette note non committés.
