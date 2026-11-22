# Module de construction des lots du bras A — note de code, version 5

- **Objet** : porter au module des lots les règles du brouillon 53 du préenregistrement (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon53.md`, `8ee69fe656e90b10961e7545a4cf214b5872784e45b5d3aafed1f774bd31a6bb`, empreinte vérifiée), à la lettre. Sources des changements de texte : `arret-office-et-echec-generiques-fable-v1.md` (39 couples), `contre-lecture-11-brouillon52-bras-a-v1.md` (9 mineurs), et le différentiel des brouillons 51 et 53 (lignes 714, 719, 762, 797, 806, 808, 812, 819, 822, 846, 848, 1011, 1174, 1175, 1184, 1189, 1260).
- **Fichiers neufs** (R12 : `lots_bras_a_v4.py` et ses essais inchangés ; compagnons `.sha256`, R6) :
  - `src/controle_ia/organismes_discrets/lots_bras_a_v5.py` ;
  - `tests/test_lots_bras_a_v5.py` (81 essais).
- Point de départ : `lots_bras_a_v4.py` (v3 au nom privé près). Processeur seul, aucun réseau, aucune dépense, rien committé ; aucune pièce cloisonnée ouverte. Graines : seules les clés de `graines_bras_a_v4` (`join/…`, `ancr/…`, `meca/…`, `meca-ancre`, `sent/…`, `relu/lot-decisif/…`, `ordr/…`, `opaq/…`, `alea/…`), par `generateur_de` (R9).

## Règles portées, avec leur ligne du brouillon 53

| règle | ligne(s) | code | essais |
|---|---|---|---|
| **Égalité exacte** : liste qui compte juste l'effectif (128 ou 64 pour une épreuve jointe, génériques compris ; 160 ou n pour une classe des relues ; quatre plans d'une tâche) prise en entier, ordre trié, **sans appel du générateur** ; les tirages suivants sous la même clé partent de son état tel qu'il est ; les autres tirages de 6.2 (ancres, sentinelles, plans relus) non touchés | 806 (fin), 714, 719, 846 ; garde 1174 | `_prendre` (épreuves jointes, deux classes des relues) ; `plans_mecaniques` déjà « quatre ou moins » | `test_egalite_exacte_sans_appel_du_generateur`, `…_etat_du_generateur_recalcule`, `test_relues_egalite_exacte_a_160_sans_tirage`, `test_prendre_et_tirer` |
| **Plancher 64** « contrôles d'une autre tâche », **32** « texte sans rapport » ; compte jugé = min(effectif écrit, actions honnêtes jugeables) ; sous le plancher, épreuve non construite, critère en échec (A5), constat porté par le lot, reste construit | 806 | `lot_honnete_appariement`, `PLANCHER_AUTRE_TACHE`, `PLANCHER_SANS_RAPPORT` | `test_planchers_des_epreuves_jointes` (129, 128, 127, 65, 64, 63, 33, 32, 31, 2) |
| Ancre sur plans honnêtes : sous 64 actions, la seconde population est vide → constat aux deux comptes (zéro) et plancher de 24 chacun | 808 | `ancre_plans_honnetes` (forme v4, désormais atteinte par le plancher de 64) | `test_ancre_plans_honnetes_sur_sous_et_au_dessus` (64, 63) |
| **Plan tronqué, 12 plans utilisables** (à artefact **et** à seconde grandeur), comptés sur les plans tirés, avant envoi ; sous 12 : aucun artefact du plan tronqué au lot, constat, les trois autres épreuves construites ; à 12 ou plus : tous les plans à artefact envoyés ; plan sans artefact compté parmi les utilisables : refusé | 819 ; garde 1174 | `lot_mecanique_couverture(…, seconde_grandeur=)` | `test_plan_tronque_sur_sous_et_au_dessus` (12, 13, 11 par les deux voies, 0), `test_plan_tronque_artefacts` |
| **Constat unique de la couverture** à deux comptes, gardes de compte (64) d'abord, dit lequel est sous son plancher | 822 | `lot_honnete_couverture` (forme v4 gardée) | `test_couverture_un_seul_constat_a_deux_comptes`, `…_gardes_de_compte_avant_le_constat` |
| **Ancre des jumeaux non jouée** si l'ancre sur plans honnêtes est à effectif insuffisant, quel que soit le compte des jumeaux ; aucun constat propre, celui de la première partie en tient lieu | 812 | `ancre_jumeaux(…, ancre_plans=)` rend ce constat ; `voie_de_service_de_l_etape_e_prime` rend `[]` et refuse un lot ou un constat propre des jumeaux à côté | `test_ancre_jumeaux_non_jouee_si_premiere_partie_insuffisante`, `…_e_prime_saine`, `…_e_prime_artefacts` |
| **Action donneuse absente** (une tâche à actions, ou aucune) : arrêt de la construction des lots d'épreuve, couverture comprise, **avant tout plancher** ; constat de l'arrêt (épreuve, compte par tâche), jamais un constat d'effectif insuffisant | 714, 797 ; garde 1175 | `garde_de_l_action_donneuse`, `ArretSansDonneuse` (porte `ConstatDArret`, inscrit sous `manifeste["arrets"]`) ; `lot_honnete_couverture` exige le témoin `DonneusesTenues` de l'épreuve ouverte | `test_garde_donneuse_*`, `test_couverture_exige_la_garde_donneuse_tenue` |
| **Épisode sans plan au lot décisif** : hors des lectures de la couverture, compté par condition ; plans et épisodes sans plan disjoints, 896, sinon arrêt | 848 ; garde 1174 | `lot_decisif(…, episodes_sans_plan=)`, compte `episodes-sans-plan-par-condition` | `test_lot_decisif_episodes_sans_plan` |
| **Arrêt d'office sous 80 actions relues** : relevé des deux comptes à l'ouverture de (i), fichier unique par épreuve, constat (suite A18) s'il est sous 80 ; lot décisif refusé après ce constat ; à (j), comptes égaux à ceux du relevé, sinon arrêt | 762, 846, A18 (1011), 1260 ; garde 1184 | `releve_des_actions_relues` → `Releve` ou `Constat` ; `lot_decisif(releve=…)` ; registre `releves-des-actions-relues` (une fois par épreuve) | `test_releve_*`, `test_lot_decisif_refuse_apres_constat_a18`, `test_lot_decisif_comptes_du_releve` |

## Ce qui ne relève pas de ce module

- **Arrêt de la course sous A18** (ne demander ni devis, ni ligne de GO, ni instance de la seconde ligne de carte ; ni refabrication, ni distillation ; étape de discrétion non jouée ; garde de la ligne 1184, premier membre) : relève **du lanceur**. Le module fait le fichier (relevé ou constat) et refuse le lot décisif après un constat.
- **Plan tronqué** : la construction de l'artefact et le calcul de la seconde grandeur (extraits connus) relèvent de `epreuves_couverture_bras_a_v4` (`plan_tronque`, `grandeurs_du_plan_tronque`) ; la corrélation après lecture, « grandeur non définie » et « moins de 12 plans à deux grandeurs après lecture » (échec constaté après lecture, distinct de l'effectif insuffisant) relèvent de l'analyse. Ce module ne fait que le compte des plans utilisables et la composition du lot.
- **Lot des jumeaux de l'appariement non joué** sur une épreuve dont l'ancre sur plans honnêtes est en constat (812 ; 6.3 (f)) : il est construit à l'étape (c) ; ne pas le lire relève du lanceur. De même la garde « ancre des jumeaux après (e) et (h1) » (ligne 1185).
- **Garde des contrôles génériques plantés** (ligne 1189, « non éprouvée ») : rédaction du verdict, hors des lots ; le module fournit le constat d'effectif insuffisant des génériques.

## Ambiguïtés (`AmbiguiteDuTexte`)

Les trois que levait la v4 sont **tranchées par le brouillon 53** et ne lèvent plus : aucune donneuse d'une autre tâche (797 : arrêt) ; moins de 896 plans des conditions (848 : épisodes sans plan) ; première partie de l'ancre à effectif insuffisant avec seconde construite (812 : non jouée). **Aucune ambiguïté neuve** : la classe reste exportée, sans site de levée. Lectures déclarées, non des ambiguïtés : le témoin `DonneusesTenues` exigé par la couverture est la forme en code de « ceux de la couverture compris » (797) ; une épreuve jointe sous son plancher est retirée du lot honnête, constat porté par le lot, comme les génériques en v4 (806 : « elle n'est pas construite » ; « les autres lots… sont lus »).

## Octets qui changent par rapport à la v4 (vérifiés par essai)

- **Inchangés** : cas complet (576) — lot honnête et lot des jumeaux de l'appariement, deux ancres, lots honnête et des jumeaux de la couverture ; lot honnête de 65 à 127 et à 129 ; lot décisif sans couverture à 200/200, 200/160, 160/160, 100/120.
- **Changés** : lot honnête à **128** juste (aucun `choice`, donneuses du générateur neuf) ; à **64** juste (génériques : permutation du générateur neuf ; le texte sans rapport, lui, a le même ensemble) ; **63 et moins** (contrôles d'une autre tâche, puis texte sans rapport, non construits : constats). Lot décisif à **160 honnêtes juste** et plus de 160 déplacées (classe honnête prise sans tirage, déplacées tirées du générateur neuf). **Lot mécanique** : appels et tables égaux, comptes neufs (`plans-tronques-…`). **Lot décisif avec couverture lue** : appels et tables égaux, compte neuf `episodes-sans-plan-par-condition`. Le sha256 de ces lots au manifeste n'est donc pas celui de la v4.

## Commandes et sorties

    $ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_lots_bras_a_v4.py tests/test_lots_bras_a_v5.py tests/test_graines_bras_a_v4.py
    237 passed
    $ PYTHONPATH=src .venv/bin/python -c "…cl.violations_de_la_garde_statique(Path('.')) if 'lots_bras_a_v5' in v…"
    []

Campagne de mutations **sur une copie** (bloc-notes de la session, `mutations_lots_v5.py` ; arbre `src/`, `pyproject.toml`, `tests/conftest.py` et les essais v5 copiés ; chaque mutant écrit dans la copie seule, la copie restaurée à la fin, l'empreinte du module du dépôt confrontée avant et après) :

    57 mutants : 56 tués, 1 survivant ; copie restaurée ; module du dépôt intact

Survivant **équivalent**, déclaré : « sentinelles tirées à 2 » (`>` devenu `>=`) — tirer deux pas parmi deux donne le même ensemble, et aucun tirage ne suit sous la clé `sent/{tâche}/e{k}` ; le lot est assemblé trié, ses octets sont égaux. Les sentinelles ne sont pas dans la liste de la règle « Égalité exacte » (806 : « les autres tirages de 6.2 ne sont pas touchés »).
