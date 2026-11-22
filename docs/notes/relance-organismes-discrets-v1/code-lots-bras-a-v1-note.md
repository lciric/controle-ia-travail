# Module de construction des lots du bras A — note de code, version 1

- **Objet** : écrire la construction des lots d'épreuve (6.5), des lots du juge des ancres, du lot décisif (6.8) et des lots de la révision bornée (6.6), et le tableau de la voie de service du juge (ligne 551), à la lettre de `prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md` ; constat « aucun module trouvé » de l'enquête `enquete-modules-instrument-m3-v1.md`, ligne 21 ; constat M-4 de la contre-lecture 10.
- **Fichiers** (scellés, R6) :
  - `src/controle_ia/organismes_discrets/lots_bras_a_v1.py` — `b8200aa45800b4d476dad9c5ec6da3c17ec3835818278528e21bfda1e4f2fbff` (533 lignes) ;
  - `tests/test_lots_bras_a_v1.py` — `de2f56a06ece1573057af54939c59946de9892c9fe5de49813d2d3058371b267` (25 essais).
- **Briques appelées, non modifiées** : `graines_bras_a_v4` (clés, `generateur_de`, `ordre_des_appels`, `identifiants_opaques`, `couper_ouvertes_gardees`, `cle_alea`, `cle_sentinelles`) ; constantes de vérité `A_EFFET`, `SANS_EFFET`, `DEPLACEE_NON_JUGEABLE` de `instrument_appariement_v4`. Les contenus (mots tirés, artefacts, entrées aveugles) restent à `epreuves_couverture_bras_a_v3` et `instrument_appariement_v4` : le module compose les lots, il ne fabrique aucun texte. Processeur seul, aucun réseau, aucun fichier lu, rien committé.

## Ce que fait chaque fonction, et la ligne du texte qu'elle porte

| fonction | ce qu'elle fait | texte |
|---|---|---|
| `separation` | 16 tâches de fabrication, 16 de vérification, disjointes ; 8 ouvertes et 8 gardées par la clé `ouve` | 6.1, 6.2 (`ouve`) |
| `_exiger_separation` | refuse une séparation d'une autre entropie, ou dont les ouvertes et gardées ne sont pas celles que tire `ouve` | 6.2 |
| `_action`, `_plan` | position (tâche, épisode 0 à 7, pas 0 à 9) ; **refuse une tâche hors des tâches permises** : vérification dans un lot d'épreuve, gardée hors révision, ouverte sous révision, fabrication au lot décisif hors des relues déclarées | 6.1 (deux gardes), 6.5 « Tâches gardées », 8.4 |
| `_tirer` | tirage sans remise de k éléments dans la liste triée ; moins de k disponibles : `AmbiguiteDuTexte` | 6.2 « la liste où l'on tire est triée » |
| `_assembler` | trie la liste (composante, condition, tâche, épisode, pas, lecteur), refuse un doublon, ordre des appels par `ordr/{lot}` (`ordre_des_appels`), identifiant du rang r = r-ième de `opaq/{lot}` ; rend appels `{rang, identifiant}` (rang à partir de 1) et la ou les tables `identifiant → description` | 6.2 (`ordr`, `opaq`), 6.3 (c), 6.8 |
| `Lot.empreinte`, `Lot.octets` | JSON canonique (clés triées, UTF-8, sans blancs) du lot entier ; sha256 | R6, R9 |
| `lot_honnete_appariement` | honnêtes jugeables (640 au plus) ; `join/controles-autre-tache` : 128 sans remise, puis donneuse **avec remise** parmi les jugeables des autres tâches (liste triée), tirée dans le même générateur, receveur après receveur ; `join/texte-sans-rapport` : 64, clé `alea/lot-honnete-appariement/…` inscrite par action ; `join/controles-generiques` : 64, puis permutation de 4 × 16 textes dans le même générateur ; moins d'honnêtes qu'une épreuve n'en demande : toutes prises, compte rapporté | 6.5 « Lot honnête », 6.2 (`join`, `alea`) |
| `ancre_plans_honnetes` | `ancr/premiere` : 24 honnêtes, puis 24 des « contrôles d'une autre tâche » du lot honnête, sans remise ; 48 mêlées par `ordr/ancre-plans-honnetes` | 6.5 « Ancre sur plans honnêtes », 6.2 (`ancr`) |
| `lot_jumeaux_appariement` | actions déplacées « à effet » et « sans effet » dans leur état déplacé ; « déplacées non jugeables » jamais envoyées, comptées ; toutes les honnêtes jugeables du lot honnête relues sous identifiants neufs | 6.5 « Lot des jumeaux », « Vérité par construction » |
| `ancre_jumeaux` | `ancr/seconde` : 24 jumeaux à effet, sans remise | 6.5 « Ancre des jumeaux » |
| `lot_honnete_couverture` | les 64 plans honnêtes ouverts, 128 lectures | 6.5 |
| `plans_mecaniques` | `meca/{tâche}` : 4 plans sur 8 par tâche ouverte, 32 | 6.2 (`meca`), 6.5 |
| `lot_mecanique_couverture` | artefacts reçus (retrait : un par lecteur éprouvé, lu par lui seul ; référence, plan tronqué, dose flagrante : lecteur `None`, lus par les deux) sur les 32 plans ; au plus 64, 32, 32, 32 ; référence et dose flagrante exactement 32 (le texte n'en écarte aucun) ; 160 artefacts, 256 lectures au complet | 6.5 « lot des quatre épreuves mécaniques » |
| `ancre_couverture` | `meca-ancre` : 8 des 32 plans mécaniques | 6.5, 6.2 (`meca-ancre`) |
| `lot_jumeaux_couverture` | 64 plans déplacés à la dose 1 et les 64 plans d'épreuve relus (en entier, sans tirage), 128 plans, 256 lectures | 6.5, 6.2 (« pris en entier ») |
| `lot_decisif` | actions jugeables des 7 conditions sur les seules tâches de vérification (8 960 au plus) ; `sent/{tâche}/e{k}` : 2 sentinelles parmi les pas à effet du jumeau, moins s'il en a moins (128 épisodes exigés) ; `relu/lot-decisif/actions` : 160 honnêtes puis 160 déplacées à effet de l'épreuve **en vigueur** (lots ouverts ou de révision, même révision exigée des deux) ; si la couverture est lue : 896 plans et `relu/lot-decisif/plans` : 32 des 64 plans honnêtes ouverts ; sinon aucun plan ; tout mêlé par `ordr/lot-decisif` ; deux tables à part, `sentinelles` (sentinelles déplacées, actions et plans d'épreuve relus) et `conditions` | 6.8, 6.1, 6.3 (j) |
| `inscrire_au_manifeste` | écrit sous `manifeste["lots"][clé ordr]` : effectif, clés, sha256 du lot et de chaque table ; jamais réécrit (identique : rien ; différent : arrêt) | 6.2 « Manifeste par course et par lot », R12 |
| `tableau_des_cles` | rang 1..n → `GEMINI_API_KEY` (impair) ou `GEMINI_API_KEY_2` (pair), sans item | ligne 551 |
| `exiger_tableau_des_cles` | refuse un tableau qui nomme un item, change une clé ou un effectif | ligne 551 ; M-4 (iii) |
| `cle_de_l_envoi` | clé du rang ; reprise ou redemande : sous la clé du premier envoi, qui doit être celle du rang, sinon arrêt (« écart, porté à Lazar ») | ligne 551 |
| `voie_de_service_du_juge` | tableau d'un lot du juge, rangs dans l'ordre de `ordr/{lot}` ; seul `ancre-jumeaux` (étape (e′)) est rendu ; les autres lèvent `AmbiguiteDuTexte` | ligne 551 ; M-4 (i), (ii) |

Sous la révision bornée (`revision=True`), les quatre lots `lot-honnete-appariement`, `lot-jumeaux-appariement`, `ancre-plans-honnetes`, `ancre-jumeaux` se construisent sur les seules tâches gardées, avec les clés `join`, `ancr`, `alea`, `opaq`, `ordr` préfixées `revision/` (6.2, dernier paragraphe ; 6.6) ; la couverture n'a pas de révision (la table de `graines_bras_a_v4` refuse la clé).

**Lectures prises à la lettre, déclarées** (non des ambiguïtés, mais des choix d'ordre que 6.2 laisse au code « qui fait foi ») : ordre des tirages dans un générateur (receveurs puis donneuses ; receveurs puis attribution des textes génériques ; honnêtes puis autres) ; identifiant du rang r = r-ième identifiant tiré ; un même lot décisif mêle appariement et couverture (« Tout est mêlé ») ; les 24 honnêtes de l'ancre peuvent recouvrir des positions des 24 « autre tâche » (tirages dans deux populations distinctes) ; les plans d'épreuve relus du lot décisif sont tirés uniformément parmi les 64 plans ouverts, sans contrainte par tâche.

## Ambiguïtés trouvées — à trancher par le texte (chacune lève `AmbiguiteDuTexte`, aucune n'est tranchée)

1. **Voie de service à l'étape (d)** (M-4 (i)) : la ligne 551 dit les deux ancres de la première partie « en un seul lot », mais 6.2 tire deux ordres (`ordr/ancre-plans-honnetes`, `ordr/ancre-couverture`) ; le rang, donc la clé, de chaque item n'est pas fixé. `voie_de_service_du_juge` refuse ces deux lots.
2. **Voie de service sous la révision bornée** (M-4 (ii)) : la ligne 551 ne vise que « les deux étapes où le juge est appelé à la course » ; les lots `revision/…/ancre-plans-honnetes` et `revision/…/ancre-jumeaux` ne sont pas couverts. Refusé.
3. **Contrôles génériques sur un lot de moins de 64 honnêtes jugeables** : « toutes sont prises » (6.5) contredit « seize fois chacun ». Refusé.
4. **Actions d'épreuve relues** : moins de 160 honnêtes ou de 160 déplacées à effet dans l'épreuve en vigueur — 6.8 ne dit pas ce qui est pris. Refusé.
5. **Ancres** : moins de 24 jumeaux à effet (ancre des jumeaux), ou moins de 24 dans une population de l'ancre sur plans honnêtes (inatteignable si le lot honnête passe la garde 3) ; moins de 8 plans mécaniques (inatteignable). Refusé.
6. **64 plans du lot honnête et du lot des jumeaux de la couverture** : le texte dit 64 ; s'il en vient moins (épisode sans plan, ou épisode laissé honnête à la dose 1 compté ou non comme « plan déplacé »), le texte ne dit pas ce qui est lu. Refusé.

**Hors de ce module, déclaré** : les gardes de procédure qui ordonnent la construction (lot des jumeaux construit après le fichier scellé de (h1) ; lot décisif après le fichier scellé d'une prise positive à la dose 1 ; items remis au juge après les scellements de (e) et (h1)) relèvent du lanceur (8.4, 13.2) ; `exiger_identifiant_independant` s'applique aux contenus, que ce module ne voit pas (les identifiants n'en dépendent pas par construction).

## Commandes et sorties

    $ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v1.py
    .........................                                                [100%]
    25 passed in 2.19s

    $ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v1.py tests/test_graines_bras_a_v4.py tests/test_epreuves_couverture_bras_a_v3.py
    129 passed in 3.02s

Campagne de mutations (script hors dépôt, dans le bloc-notes de la session : chaque mutant écrit à la place du module, essais joués avec `-x`, module restauré et confronté à son empreinte) :

    tué       : tirage sans remise -> avec remise
    tué       : 128 -> 127
    tué       : donneuse de la même tâche
    tué       : donneuse sans tirage
    tué       : textes génériques 0..3
    tué       : attribution sans permutation
    tué       : génériques : seuil <=
    tué       : ordre ignoré
    tué       : identifiants inversés
    tué       : ordre sans révision
    tué       : liste non triée
    tué       : non jugeables envoyées
    tué       : ancre jumeaux sans effet admis
    tué       : ancre premiere : honnêtes pris parmi autres
    tué       : méca avec remise
    tué       : sentinelles sans tirage
    tué       : relues déplacées sans effet
    tué       : tables échangées
    tué       : lectures du retrait 2
    tué       : parité inversée
    tué       : reprise sous l'autre clé admise
    tué       : clé alea sans révision
    tué       : garde de la coupe retirée
    tué       : exactes non exigées
    tué       : voie : ambiguïté (d) levée
    tué       : manifeste réécrit
    26 mutants : 26 tués, 0 survivants ; module restauré (b8200aa45800b4d4…)

Déterminisme : `test_determinisme_octet_pour_octet` (mêmes graines → mêmes octets et même empreinte, pour le lot décisif, le lot honnête et le lot des jumeaux ; autre entropie → autre empreinte) ; `test_ordre_et_identifiants_par_les_seules_cles` et `test_donneuses_et_ordre_de_la_revision_recalcules` recalculent ordre, identifiants et donneuses depuis les clés ; `test_aucun_autre_alea` refuse tout générateur numpy né hors de `generateur_de` sur une clé de la table, et tout aléa global.

Environnement : Python 3.13.18, numpy 2.4.6, commit de base `75f4438ef` (branche `claude/pensive-bardeen-1fv7hw`), fichiers non committés.
