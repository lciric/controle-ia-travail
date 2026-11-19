# Rapport du développeur — programme à part de l'audit de symétrie de la ligne 1 (classe B) — v1

Pièce de travail. Développeur neuf, signé « développeur, modèle L′ ». Écrit le 2026-11-19 (temps universel), dans le bloc-notes seulement ; la session verse. Rien de commis, rien de poussé, aucun appel à un fournisseur de modèles, aucune dépense, aucune machine ; aucun étalonnage, aucune fumée, aucune course, jamais `--reel`.

- Mandat : `mandat-developpeur-programme-audit-symetrie-ligne-1-v1.md`, sha256 `310f2a6902afd7a933b9e4febf32dfb393ce20f09b0e4c00e191fdad6fc15f44`, vérifiée avant de commencer (égale).
- Branche lue : `lot/compte-organisme-v1`, commit `d8e09ebfd…` au début ; la branche a avancé pendant le travail (commit `5e51b0b15bad4d62c296a392618279ae257547b5` à la fin) : sous le dossier de la ligne 1, aucun des fichiers lus n'a changé (`git diff --stat` vide sur `code/`, l'addendum v3, le mandat et le texte scellé). Un addendum version 4 et un erratum sont apparus : le choix 5 (§ 2) et le § 4.2 de la version 4 sont identiques, au caractère près, à ceux de la version 3 (comparaison par programme).

## 1. Pièces lues, empreintes vérifiées

| pièce | sha256 | lecture |
|---|---|---|
| mandat | `310f2a69…5fc44` | en entier |
| `CLAUDE.md` | — | en entier (consignes du dépôt) |
| addendum 1, version 3 | `fb48a8ab9aeee1667c46a3d72dbf97d39343ecfb10227c652074d38f46ba55d5` (égale au compagnon) | en entier ; § 2 choix 5 et § 4.2 relus |
| préenregistrement scellé, version 5 | `523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9` (égale au compagnon) | « Métrique », « Seuil », « Plan d'analyse » (jugement, bras, journal, tailles et graines, étalonnage, audit du générateur), « Critères de lecture gelés » (dont « Audit de symétrie »), liste d'arrêt, réserves, annexe A |
| code v2 et banc v1 (`code/`) | tous les compagnons `.sha256` de `code/` et `code/essais/` contrôlés : « OK » ; empreintes égales à la configuration v2 et à l'addendum, § 5.1 | `etalonnage_ligne1_v2.py` en entier ; `rejouer_journal_ligne1_v2.py` en entier ; `journal_ligne1_v1.py` en entier ; `analyse_ligne1_v2.py` : en-tête, `Reechantillonnage`, `mesures_course`, A12 et lecture d'un dossier ; `banc_ligne1_v1.py` : en-tête, empreintes, préenregistrement, organisme, graines, bras, course, entrées et sorties ; `lancer_ligne1_v2.py` : en-tête, refus, étapes ; `configuration_ligne1_v2.json` en entier ; `essais/test_banc_ligne1_v2.py` : en-tête, montage et dernier essai |
| `memoire_v53.py` | `43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0` | extrait par `git show 65574043d:…` dans le bloc-notes ; empreinte égale à la configuration ; non lu |
| autres fichiers de l'organisme | égales à la configuration (vérifiées par la garde A1 à chaque chargement) | copie de `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/` dans le bloc-notes ; non lus |
| `code-v2/rapport-developpeur-corrections-banc-a-v2.md` | — | lignes sur le montage de l'organisme d'essai seulement |

Aucune sortie de course réelle, aucun journal réel, aucune sortie d'essai ou de fumée des dossiers `code-v1/` et `code-v2/` n'a été ouvert.

## 2. Fichiers écrits (chemins relatifs au dépôt, à verser)

| fichier | sha256 |
|---|---|
| `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/audit_symetrie_ligne1_v1.py` | `ca000bba3fe7399adecfcf5c93fd162dcf52524e4951683f3ecd93105047eef7` |
| `…/code/essais/test_audit_symetrie_ligne1_v1.py` | `18031e62feae966a2eb6fd1788df1c481db156a803e4272e277736a1cf85c9f3` |
| `…/code-audit-v1/sortie-essais-audit-symetrie-ligne1-v1.txt` | `2607016e19e87903591126a54cbc77ad35a7a4816affbc489e87a82b27b9dd94` |
| `…/code-audit-v1/sortie-mutations-audit-symetrie-ligne1-v1.txt` | `7e00dd15dc10a9b628aa78189ec06cb1866b2ba55ce7a0e2471eaa0694835658` |
| `…/code-audit-v1/mutations_audit_symetrie_ligne1_v1.py` (outil du contrôle R4) | `ca482b6a8ccedfe3602627c376585d093eb74d7e3ff6d16351b6d146e19f4c87` |
| `…/code-audit-v1/rapport-developpeur-audit-symetrie-ligne-1-v1.md` (ce rapport) | dans son compagnon |

Chaque fichier a son compagnon `.sha256` à côté. **À noter pour le versement** : le lanceur v2 refuse de partir si `git status` n'est pas vide sous `code/` (fichiers non suivis compris, `exiger_code_commis`) ; le programme et ses essais, versés sous `code/`, doivent donc être commis avant tout lancement. Ils ne figurent pas dans la liste du code v2 de la configuration : ni le lanceur ni la configuration ne les contrôlent, et le programme ne change aucun fichier du banc ni du code v2.

## 3. Ce que fait le programme

Lancé au geste 8 par l'agent de l'audit de symétrie, depuis `code/` :

```
PYTHONDONTWRITEBYTECODE=1 python3 -B audit_symetrie_ligne1_v1.py \
  --manifeste <sortie>/decisive/manifeste-course-decisive-ligne1-v2.json \
  --manifeste-sha256 <empreinte du manifeste portée au registre> \
  --organisme <orchestrator/> --vers <dossier neuf> [--etalonnage <sortie-etalonnage-ligne1-v2.json si déplacée>]
```

La commande ne connaît que le mode réel. Dans l'ordre :

1. **Contrôle des empreintes** : le préenregistrement scellé, la configuration v2 (`81f58ce5…`, empreinte de l'addendum, § 5.1), chaque fichier du code v2 (contre la configuration), l'organisme (A1, A2), le manifeste décisif (contre l'empreinte donnée en argument et son compagnon), la sortie de l'étalonnage (contre le manifeste), le code que portent le manifeste et la sortie de l'étalonnage (contre le code importé), la racine de rééchantillonnage (2026111903). Tout écart : refus nommé, rien n'est calculé ni écrit.
2. **Recoupement de M1-nul** (§ 4.2), courses 0, 300 et 599 de la configuration, deux classes. Journal et sortie brute vérifiés contre le manifeste et leur compagnon, chaîne du journal vérifiée. Par bras, quatre lectures : (i) journal, décisions d'arrêt ; (ii) journal, décisions de promotion ; (iii) sortie brute, fonction de l'analyse ; (iv) sortie brute, calcul direct, indépendant de l'analyse. « concordant » si les quatre existent et rendent le même (V, R) et le même M1-nul, à l'égalité exacte ; sinon « désaccord », avec le détail (lectures absentes, (V, R) et M1-nul de chaque lecture). Aucun verdict, aucun choix entre le journal et la sortie brute.
3. **Complément du choix 5**. Les cartes `transformee` des 400 courses d'étalonnage de chaque classe sont lues : empreinte de chaque sortie vérifiée contre la liste scellée de la sortie de l'étalonnage, garde A17 refaite, course et classe vérifiées. Elles sont lues sous les deux conventions ; une carte jugée « indéterminée » est hors des aires dans la porte, et vaut 0 (non vraie) dans le complément ; une carte non jugée est hors de l'étiquette d'effet dans les deux. La porte est **recalculée** par `audit_generateur`, puis comparée au bit près (JSON canonique, toutes les aires, les deux étiquettes) à celle de la sortie scellée. Un écart lève `RecalculPorteDifferent`. Le complément est ensuite calculé par **le même appel** sur les cartes du complément. Sont rapportées, par classe : les aires des trois traits seuls, étiquette d'effet, avec leur intervalle ; la porte recalculée à côté ; les comptes (vraies, fausses, indéterminées, non jugées) ; les traits dont l'intervalle est tout entier hors de [0,45 ; 0,55]. Ces traits sont nommés, sans aucune suite dans le programme.
4. **Sorties** : `audit-symetrie-ligne1-v1.json` et `manifeste-audit-symetrie-ligne1-v1.json`, chacun avec son `.sha256`, à des noms neufs (on n'écrase jamais). Le manifeste de run porte : la configuration (chemin, empreinte, valeurs), le préenregistrement, le programme (chemin, empreinte), le code v2, le commit du dépôt et l'état du programme dans git, l'organisme, les versions (Python, numpy, plateforme), **chaque graine dérivée (racine, tâche, graine)** et les premières dérivations, les fichiers lus et leur empreinte, ainsi que l'empreinte du compte rendu.

## 4. Fonctions reprises par import, et fonctions écrites

**Reprises, sans copie** (essai `test_code_importe_est_le_code_v2_de_la_configuration` : aucune de leurs définitions n'est dans le programme ; ce sont les objets mêmes des modules) :

| fonction | module | usage |
|---|---|---|
| `audit_generateur` (et par elle `auc_ponderee`, `ajuster_logistique`, `predire_logistique`, la dérivation `GRAINES(racine, "etalonnage\|audit\|classe=<classe>")` et les tirages) | `etalonnage_ligne1_v2` | porte recalculée et complément : aires, rééchantillonnage, dérivation des graines |
| `verifier_sortie_sans_bras_interdit` (A17), `FICHIERS_CODE`, `CHEMIN_CONFIGURATION` | `etalonnage_ligne1_v2` | contrôle des sorties ; liste et configuration du code v2 |
| `m1_nul_depuis_journal` | `rejouer_journal_ligne1_v2` | lecture (i), décisions d'arrêt |
| `mesures_course` | `analyse_ligne1_v2` | lecture (iii), M1-nul de l'analyse |
| `verifier_code_configuration` | `lancer_ligne1_v2` | code sur disque contre la configuration v2 |
| `lire` (chaîne d'empreintes), `canonique` | `journal_ligne1_v1` | lecture du journal ; comparaison au bit près |
| `verifier_preenregistrement`, `charger_configuration`, `charger_organisme` (A1, A2), `Graines`/`GRAINES` (graine de tâche de l'organisme), `sha256_fichier`, `verifier_scelle_fichier`, `lire_json_verifie`, `lire_json_xz_verifie`, `ecrire_json_scelle`, `exiger_fini` (A10), `horodatage`, `ArretBanc` | `banc_ligne1_v1` | empreintes, lectures et écritures scellées, graines |

**Écrites** : `verifier_fichier`, `verifier_mode`, `verifier_coherence`, `code_sur_disque` (contrôles et refus) ; `carte_deux_conventions` et `lire_cartes_etalonnage` (lecteur des cartes sous les deux conventions : le tuple de la porte est, à l'identique, celui de `lire_courses`, essai à l'appui) ; `aires_traits_seuls` et `complement_choix_5` ; `lignees_sans_effet_du_journal` et `m1_nul_depuis_promotions` (lecture (ii)) ; `m1_nul_sortie_directe` (lecture (iv)) ; `comparer_bras`, `recouper_course` et `recoupement_m1_nul` ; `GrainesConsignees` (sous-classe de `Graines` : même dérivation, avec en plus la consignation de chaque racine, tâche et graine) ; `etat_depot`, `executer` et `main`.

**Choix de construction, de ma main (routine), dits** :
1. Le complément passe par `audit_generateur` tout entier plutôt que par une boucle réécrite : c'est la seule façon d'avoir les rééchantillons de la porte par construction. En contrepartie, l'appel calcule aussi la régression sur les trois traits et l'étiquette de conception sous la convention du complément. Ni l'une ni l'autre n'est rapportée : la régression ne fait pas partie du complément, et l'étiquette de conception ne dépend pas de la convention. Ce calcul dérive deux tâches de plus de la racine 2026111903 (`…|regression|conception`, `…|regression|effet`), les mêmes que la porte ; le manifeste de run les consigne.
2. Le recalcul de la porte, comparé au bit près à la sortie scellée, est un refus que le mandat ne nomme pas. Sans lui, on ne saurait pas, sur les vraies sorties, que les cartes lues et les rééchantillons sont bien ceux de la porte. Ce n'est pas une garde de la liste d'arrêt : il ne lit aucun chiffre de l'épreuve pour décider, n'arrête que ce programme et revient à la mère.
3. Le recoupement compare aussi (V, R), et pas seulement M1-nul : retirer une promotion d'un monde à effet laisse M1-nul égal à 0 quand V = 0. Le mot « concordant » est donc plus strict que la lettre du § 4.2, et c'est dit.
4. Les lectures (ii) et (iv) sont ajoutées. La (ii) applique la lettre « décisions de promotion et d'arrêt ». La (iv) répond à la limite que dit l'addendum, § 4.2 : le recoupement du code v2 compare M1-nul à la fonction de l'analyse, non à un calcul indépendant. Le caractère sans effet d'une lignée se lit dans le journal par le type « fixe » de la loi du monde de ses jugements, comme dans `m1_nul_depuis_journal` : les seules décisions de promotion et d'arrêt ne portent pas cette information.
5. L'empreinte du manifeste décisif est exigée en argument. Le compagnon seul peut être refait ; l'empreinte du registre ne le peut pas.
6. Que le programme soit commis est consigné au manifeste de run (`programme_commis_et_propre`), sans refus. Son empreinte est portée au registre (addendum, réserve 6) ; c'est à l'agent de l'audit de la comparer à celle du manifeste de run.
7. Le programme ne relit pas le champ `courses_audit_symetrie.recoupement` du fichier de rejeu : l'addendum, § 4.2, confie cette relecture à l'agent de l'audit lui-même.

## 5. Essais (R5)

Lancés dans une copie de travail du bloc-notes (dépôt git à part, organisme copié, vrai `memoire_v53.py`) : **24 passés sur 24** (`sortie-essais-audit-symetrie-ligne1-v1.txt`). Toutes les sorties lues sont fabriquées par les essais. Les sorties d'étalonnage sont écrites à la main ; leur porte est calculée par le chemin du code v2 (`lire_courses`, puis `audit_generateur`). Les courses décisives 0, 300 et 599 sont jouées par le banc, tous bras, sur la racine des essais avec les paramètres d'essai de la configuration.

| exigence du mandat | essai(s) |
|---|---|
| Complément, cas sain (aires connues) | `test_complement_cas_sain_aires_connues_cas_ecrit_a_la_main` (cas à la main : porte 1, complément 4/6) ; `test_complement_cas_sain_aires_et_intervalles_connus` (aires et intervalles égaux, à 1e-12, à une référence indépendante : aire par comptage des paires, tirages refaits depuis la graine de la tâche, cartes tirées de la seule spécification, sans le lecteur du programme) ; `test_complement_lecteur_egal_a_lire_courses_du_code_v2` ; `test_complement_dans_le_run_entier` |
| Complément, artefact (indéterminée déplacée) | `test_complement_artefact_indeterminee_deplacee` : sous la porte, rien ne bouge ; sous le complément, l'aire de l'identifiant **monte**, de la quantité exacte de la référence ; plus `test_complement_artefacts_etiquettes_et_non_jugees` (indéterminée relabellisée « fausse » : le complément ne bouge pas, la porte bouge ; relabellisée « vraie » : le complément bouge ; carte non jugée déplacée : rien ne bouge) |
| Rééchantillons du complément = ceux de la porte | `test_complement_memes_reechantillons_que_la_porte` : interception de `GRAINES` et de `numpy.random.default_rng` ; même racine, même tâche, même graine, mêmes tirages, tirage par tirage, que l'appel de la porte du code v2, pour chaque classe |
| Recoupement, cas sain | `test_recoupement_cas_sain_concordant` : « concordant » pour les 9 bras, 3 courses, 2 classes ; les quatre lectures égales ; au moins une promotion |
| Recoupement, artefact dans la sortie brute | `test_recoupement_artefact_promotion_changee_dans_la_sortie_brute` : une promotion retirée, sortie rescellée et citée par un manifeste neuf → « désaccord », détail nommant le bras et les lectures ; les autres bras restent « concordant » |
| Recoupement, artefact dans le journal | `test_recoupement_artefact_promotion_changee_dans_le_journal` : décisions de promotion et d'arrêt changées, chaîne refaite, manifeste neuf → « désaccord », détail ; et `test_recoupement_promotions_contre_arrets_seuls` |
| Empreinte fausse : refus | `test_refus_empreinte_fausse` (sortie décisive changée, empreinte du manifeste fausse, sortie d'étalonnage changée, sortie de l'étalonnage différente du manifeste, compagnon seul faux ; rien d'écrit) ; `test_refus_journal_rompu` |
| Refus ajoutés (cas sain, artefact) | `test_recalcul_de_la_porte_cas_sain_et_artefact`, `test_refus_porte_scellee_differente_dans_le_run`, `test_lecteur_artefacts_nom_absent_et_course_deplacee`, `test_verifier_mode_cas_sains_et_artefacts`, `test_verifier_coherence_cas_sain_et_artefacts`, `test_refus_organisme_non_charge`, `test_refus_racine_derivee_hors_du_mode`, `test_complement_intervalle_hors_plage_nomme_sans_arret` (nommé, rien n'est levé) |
| Commande (mode réel) | `test_main_mode_reel_refuse_avant_toute_derivation` : préenregistrement, configuration v2 réelle, code et organisme vérifiés, puis refus avant toute dérivation sur un run fabriqué |
| Aucune racine interdite dérivée | `test_zz_aucune_racine_interdite_derivee` (dernier essai, comme dans le code v2) |

Non éprouvé, faute de pouvoir l'être sans dériver la racine 2026111903 : le chemin réel de bout en bout, c'est-à-dire la commande qui passe tous les contrôles et calcule. Il ne diffère du chemin éprouvé en mode essai que par la racine, la configuration et la valeur du mode (fonction `executer` commune).

## 6. Contrôle « trop beau » (R4) : défauts réintroduits

Outil : `code-audit-v1/mutations_audit_symetrie_ligne1_v1.py`. Chaque défaut est appliqué à une copie (dépôt git neuf, copie du préenregistrement), puis l'essai visé est lancé **avec, dans la même passe, le contrôle final des racines** (`test_zz_…`, plus un essai court qui dérive la racine des essais). « vu » veut dire : l'essai visé échoue et le contrôle des racines passe. Un témoin sans défaut passe la suite entière (24 sur 24). Passe finale (`sortie-mutations-audit-symetrie-ligne1-v1.txt`) : **25 défauts vus sur 25** : convention du complément (3), tâche, racine, ordre des courses, recalcul de la porte, intervalle hors plage non nommé, mot du recoupement, (V, R), lecture « promotion », effet de la lecture directe, bras c du journal, cinq contrôles d'empreinte, deux contrôles de mode, contrôle des racines dérivées, lecteur, organisme, chaîne du journal, mode de la commande.

Passes antérieures, déclarées :
- **Passe 1 : 20 vus sur 24.** m01 (indéterminée comptée vraie) n'était **pas vu**. L'essai visé (le cas écrit à la main) ne passait pas par le lecteur. Surtout, la référence du cas sain fabriqué était tirée du lecteur du programme lui-même, et ne pouvait donc pas voir un défaut du lecteur. **Corrigé** : la référence est désormais tirée de la seule spécification des cartes fabriquées, et m01 vise cet essai. m16, m18 et m19 : leur essai visé échouait bien, mais le contrôle des racines échouait aussi. Ces essais ne dérivent aucune graine, et la première assertion du contrôle (« la racine des essais a été dérivée ») tombait ; l'outil a été corrigé (essai court joint).
- **Passe 2 : 24 vus sur 24.** **Passe 3 (finale)** : témoin ajouté, m25 ajouté, 25 sur 25.

## 7. Attestation sur les graines

J'atteste n'avoir dérivé **aucune graine des racines 2026111901, 2026111902 et 2026111903** pendant l'écriture et les essais de ce programme. Racines dérivées : 2026111900 (essais) et 2026111999 (disjointe de toutes les racines du préenregistrement, de la fumée et des contre-lecteurs ; artefact de `test_refus_racine_derivee_hors_du_mode` et défaut m05).

Contrôle par programme (`test_zz_…` : aucune des trois racines dans les premières dérivations du processus) passé :
- dans les cinq passes complètes de la suite ;
- dans le témoin de l'outil ;
- dans 70 des 73 passes de défauts.

Limites, dites :
- **trois passes de la passe 1** (m16, m18, m19) : le contrôle s'est arrêté à sa première assertion, sans lire les racines interdites. Leurs essais visés (`verifier_coherence`, `verifier_mode`) ne dérivent aucune graine, d'après la lecture du code et `test_verifier_mode_cas_sains_et_artefacts`, qui vérifie qu'aucune première dérivation n'est ajoutée.
- **deux premières passes arrêtées au premier échec** (option `-x`), avant le contrôle : les essais joués jusque-là ne passent que la racine des essais, d'après leur code.

La racine 2026111903 n'apparaît que comme valeur comparée (configuration réelle), jamais passée à une dérivation dans un essai ; `test_main_mode_reel_refuse_avant_toute_derivation` le vérifie pour la commande.

## 8. Ce que je n'ai pas pu faire, et écarts

1. **Aucun run réel**, par interdit : le programme n'a jamais tourné sur une sortie réelle, ni au bout de la commande en mode réel. Ni sa durée ni sa mémoire sur 400 courses d'étalonnage par classe ne sont mesurées. Ordre de grandeur, non mesuré et non opposable : deux appels de `audit_generateur` par classe et la lecture des 800 sorties d'étalonnage.
2. **Chemin de la sortie de l'étalonnage** : le manifeste décisif porte un chemin absolu, celui du lancement. Si le dossier a été déplacé (versement), il faut passer `--etalonnage` ; l'empreinte est vérifiée de toute façon. Les dossiers des courses se déduisent du dossier de chaque fichier (`courses/`), comme dans le lanceur.
3. **Le champ de recoupement du rejeu** n'est pas relu par le programme ; c'est la tâche de l'agent (§ 4, point 7).
4. **Écarts aux interdits du mandat, déclarés** :
   - au début, avant d'avoir relu l'interdit sur les blocs de texte en ligne, j'ai lancé une fois `python3 -c` avec une ligne qui n'imprimait que les versions de Python et de numpy. Rien d'autre n'a été exécuté de cette façon ; tous mes autres programmes sont des fichiers ;
   - j'ai lancé une fois `git status --short` sur tout le dépôt (sortie vide) et une fois `git rev-parse HEAD`. Aucune commande n'a nommé un chemin sous `archives-reponses-modeles/` ; `git status` parcourt toutefois l'arbre entier, ce que je déclare. Les autres commandes git ont été restreintes au dossier de la ligne 1.
5. Je n'ai pas relancé les essais du code v2 (58) : le programme ne change aucun de ses fichiers et ne les copie pas.
6. Le programme est d'un seul modèle (L′) ; sa contre-lecture (classe B) reste à faire, avant que son empreinte soit portée au registre et avant le lancement de la course décisive (addendum, réserve 6).

— développeur, modèle L′
