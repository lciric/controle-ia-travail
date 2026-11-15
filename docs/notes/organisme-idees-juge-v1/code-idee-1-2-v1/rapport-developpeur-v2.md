# Code qui joue le préenregistrement de l'idée 1.2 — rapport du développeur — v2

- Auteur : le développeur de la v1 (sous-agent de la session mère) ; je n'ai écrit ni le préenregistrement, ni ses
  relectures, ni la contre-lecture du code, ni le juge.
- Date (UTC) : 2026-11-15, de 11:30 à 12:00 environ (`date -u`). Dépôt lu sur `main`, tête `a7ee8735`. **Aucun commit,
  aucune poussée, aucun appel réseau ni payant ; le run réel n'a pas été lancé** ; aucun `diag/` existant lu ; rien écrit
  sous `donnees/`, `docs/verdicts/`, ni dans `correction-poids-v1/`. Aucun refus d'outil, de garde ou de classifieur.
- Pièces : texte scellé **[T]** `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
  (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`) ; rapport v1 **[RD1]**
  `docs/notes/organisme-idees-juge-v1/code-idee-1-2-v1/rapport-developpeur-v1.md`
  (`774fbf78b1a2c3af52502a5a43ea330c9ad6f7a9998225dfbbf646e127784a66`) ; contre-lecture du code **[CL]**
  `docs/notes/organisme-idees-juge-v1/code-idee-1-2-v1/contre-lecture-code-idee-1-2-v1.md`
  (`36ecc4a4cc97b1530d89a76aa0eed19ad4ce0f226fb5be1dcb9e6eba117c85f3`) ; registre R-2897, R-2899.

## Verdict

Les trois majeurs et les neuf mineurs de [CL] sont traités, **sous noms neufs** (R12) : les 18 fichiers v1 restent en
place, inchangés (empreintes vérifiées) ; la v2 ajoute 11 fichiers. Suite complète : **167 essais sur 167 verts** (109 de la v1, 58 de la v2), passés par `lancer_essais` du lanceur v2 en 690 s. Les quatre mutations
de [CL], rejouées sur la suite complète : **quatre tuées** (dont les deux qui survivaient). Banc de mutations v2 :
**24 sur 24 tuées pour la raison attendue**. Répétition miniature par le lanceur v2 (10 générations, racine d'essai) : conforme. Aucun calcul du banc, aucun bras, aucun seuil, aucune
lecture du texte ne change.

## Fichiers neufs de la v2 (scellés par compagnon `.sha256`)

| fichier | lignes | essais | empreinte sha256 |
|---|---|---|---|
| `src/controle_ia/organisme_idees_juge/verificateur_texte_v2.py` | 168 | — | `b1743aeabe9db7dc6ba1d3eff4ebf15cc955924f1950802c78a3d9ef77fda288` |
| `src/controle_ia/organisme_idees_juge/oracle_v2.py` | 19 | — | `e569805463b8dd855b2633398af4d1a213d5b098cbc374063a682e4a627bee73` |
| `src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py` | 90 | — | `18169a33917807c7ae019202f9ffdac656cccc66c0f1354bc33d710c78a4358d` |
| `src/controle_ia/organisme_idees_juge/mutations_v2.py` | 123 | — | `bfabc7b2a6ba428041b0095487b5423901b5b8c1de771f500be519c75aad5a64` |
| `src/controle_ia/organisme_idees_juge/execution_v2.py` | 184 | — | `ebee076b1ea55017541b5906b48bb3bfb567f250490144250fe0025f24249574` |
| `scripts/jouer_idee_1_2_v2.py` | 255 | — | `f66d4b05d2d05fd1932873211281582e2c8e714199d9bffbc167f9207d3442e0` |
| `scripts/lire_idee_1_2_v2.py` | 69 | — | `ebac3ba06e1ce4484f3976235bd1a083be28f21299d795f97928bea97d9d9ae8` |
| `tests/test_organisme_idees_juge_constantes_v2.py` | 127 | 36 | `d692555eceda79e300663da2f5003b9185ee4228740281b61799d07583d28720` |
| `tests/test_organisme_idees_juge_lecture_v2.py` | 123 | 4 | `f6c61e5114e378684c4d027fed36cd07dc2eaa9270b313086179a4a3494b6c11` |
| `tests/test_organisme_idees_juge_mutations_v2.py` | 30 | 1 | `bbf73075029c58f72ab947da43a2737490d09c8f66548c612c98ebd75c879ab5` |
| `tests/test_organisme_idees_juge_execution_v2.py` | 276 | 17 | `5c15df7089625e8c205ceb8beb51d7a611f2795e978cd015410b1c40ada79fac` |

Fichiers de la v1 encore employés, **inchangés** (mêmes empreintes que [RD1]) : `__init__.py`, `juge_v1.py`, `lois_v1.py`,
`banc_tirages_repartis_v1.py`, `oracle_v1.py`, `rejeu_v1.py`, `synthetique_v1.py`, `lire_banc_tirages_repartis_v1.py`,
`mutations_v1.py`, `execution_v1.py`, `scripts/jouer_idee_1_2_v1.py`, `scripts/lire_idee_1_2_v1.py` (ces deux lanceurs
v1 ne servent plus au jeu ; leurs essais v1 restent dans la suite) et les six essais v1.

Lignes prêtes pour l'addendum d'empreintes (`python -I -B scripts/jouer_idee_1_2_v2.py --lister-empreintes`, 34 fichiers :
code v1 employé, code v2, infrastructure importée, dix fichiers d'essais et `tests/conftest.py`) :

```
c29258ab0069320bbba33d3cdf8b652ba1ce254298b348e2c68ac03e83e6414e  src/controle_ia/organisme_idees_juge/__init__.py
853595cb44260eaaf16bf003f7a7b8155a3785e08c424573fcdaf40a6d1c487e  src/controle_ia/organisme_idees_juge/juge_v1.py
bf7e1f3e6cdbbebed681cf115e6d7e8031e670ffb14d82910d707a09f5b0e1fb  src/controle_ia/organisme_idees_juge/lois_v1.py
9cb63ff12d6198b3acd0ec979e798fe41268b2a50a8d90600614fd01284d65b9  src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py
34b6d356be3d717c7f0ab44711d4e1ee38926d6db6be4cd2a3a9684514db4350  src/controle_ia/organisme_idees_juge/oracle_v1.py
a1a08ef78c87ba8ffaa4147d53854dd4c17e6a70ec5b265cb406a858a49d1086  src/controle_ia/organisme_idees_juge/rejeu_v1.py
febe203ab27796ba573accea6e6fea5692bc2c776191254408ab07d3cc9815d7  src/controle_ia/organisme_idees_juge/synthetique_v1.py
9c25699e280d9179d6c9a541711921a4861b8a129fe434de559b1a51526d4638  src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v1.py
77a74bf7f1e6fdc2fcb08267de90d16845e8b30b1c55762613e77f35a60bf15c  src/controle_ia/organisme_idees_juge/mutations_v1.py
d6da7373efca00b538407794bcd832f3f84970412e6200e49715d23455731747  src/controle_ia/organisme_idees_juge/execution_v1.py
a2a059b298ffc01b2746f32892f6390e46763ba88c665f2d840a56dc7801f640  scripts/jouer_idee_1_2_v1.py
0382ed81c0d65f83505b9790c8dbc48e5ab3d295ad038e639f6e1c2bded87a86  scripts/lire_idee_1_2_v1.py
b1743aeabe9db7dc6ba1d3eff4ebf15cc955924f1950802c78a3d9ef77fda288  src/controle_ia/organisme_idees_juge/verificateur_texte_v2.py
e569805463b8dd855b2633398af4d1a213d5b098cbc374063a682e4a627bee73  src/controle_ia/organisme_idees_juge/oracle_v2.py
18169a33917807c7ae019202f9ffdac656cccc66c0f1354bc33d710c78a4358d  src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py
bfabc7b2a6ba428041b0095487b5423901b5b8c1de771f500be519c75aad5a64  src/controle_ia/organisme_idees_juge/mutations_v2.py
ebee076b1ea55017541b5906b48bb3bfb567f250490144250fe0025f24249574  src/controle_ia/organisme_idees_juge/execution_v2.py
f66d4b05d2d05fd1932873211281582e2c8e714199d9bffbc167f9207d3442e0  scripts/jouer_idee_1_2_v2.py
ebac3ba06e1ce4484f3976235bd1a083be28f21299d795f97928bea97d9d9ae8  scripts/lire_idee_1_2_v2.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439  src/controle_ia/gardes.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2  src/controle_ia/scellement.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d  src/controle_ia/manifeste.py
3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306  src/controle_ia/prereg.py
7c0b30aea0bbc1529a2d1400aa2c11bcb83dfd467c3c65a0b2d7f395d0f385e2  tests/test_organisme_idees_juge_lois_v1.py
565d4217d8bf4fd8c8ab9ab78d91b78313179a43f8b73c94c6031b592d8b1273  tests/test_organisme_idees_juge_banc_v1.py
faf94968a189e82f125dbef1b432f9e04870996af0b88493fe758993d782f7fd  tests/test_organisme_idees_juge_rejeu_v1.py
3606348964a9b00dd817ad6d442f76216b99817fb21843e20face9b37983c27a  tests/test_organisme_idees_juge_lecture_v1.py
14dfd455c963bf4ec84903e11cf4504a65dc2c9c8cecfcad50dbcb8c35fe2eb3  tests/test_organisme_idees_juge_mutations_v1.py
7e0f1bfb4dbc7c237ea0d6e783c1bb25ae110ce8553c15c65769743760998482  tests/test_organisme_idees_juge_execution_v1.py
d692555eceda79e300663da2f5003b9185ee4228740281b61799d07583d28720  tests/test_organisme_idees_juge_constantes_v2.py
f6c61e5114e378684c4d027fed36cd07dc2eaa9270b313086179a4a3494b6c11  tests/test_organisme_idees_juge_lecture_v2.py
bbf73075029c58f72ab947da43a2737490d09c8f66548c612c98ebd75c879ab5  tests/test_organisme_idees_juge_mutations_v2.py
5c15df7089625e8c205ceb8beb51d7a611f2795e978cd015410b1c40ada79fac  tests/test_organisme_idees_juge_execution_v2.py
a1bbfcc935007934dda9b038fb9f187f7627816fd18514b5aabc77715aaedca5  tests/conftest.py
```

## Différentiel déclaré, fichier par fichier

### `src/controle_ia/organisme_idees_juge/execution_v2.py` (neuf ; majeur 1, majeur 3, mineurs 1 et 8)
Reprend `execution_v1` par import (gardes de durée et de réseau, écriture scellée, `consigner_arret`, vérification
d'addendum, tâche E1, tâche de jeu) ; seuls changent :
- `_carte` — ancien (v1, l. 195-203) : `with …Pool(processus) as pool: yield from pool.imap(tache, taches)` ; nouveau :
  `Pool(processus, initializer=_init_fils)`, puis pour chaque tâche une boucle `garde.verifier("attente d'un processus
  fils")` / `resultats.next(timeout=pas)` (pas de 5 s), comme la correction éprouvée de [CL] ; **en plus**, à chaque pas et
  après chaque résultat, l'ensemble des identités des fils (`pool._pool`) est comparé à celui du départ : `Pool` remplace un
  fils mort (une tâche est alors perdue) → `GardeArret("un processus fils est mort (tâche perdue) …")` en quelques
  secondes au lieu d'attendre la borne des 24 h ; attribut absent → `GardeArret` (aucun repli) ; la sortie du bloc `with`
  termine les fils ; `_init_fils` rétablit le signal TERM au défaut dans les fils (seul le parent le consigne). Avec un seul
  processus, la garde est relue avant chaque tâche.
- `executer` — même enchaînement que la v1 (E1, oracle scellé avant le rejeu, jeu, sortie scellée), avec
  `exiger_constantes_du_texte()` au départ et dans chaque tâche, l'oracle v2, et la troisième écriture du texte
  (`verifier_generation`) sur chaque génération jouée ; le journal porte `version_execution = 2` et le nombre de
  générations dont l'oracle a un membre à la borne triviale.
- `FICHIERS_GELES` — le code v1 employé, le code v2, **l'infrastructure importée** (`gardes.py`, `scellement.py`,
  `manifeste.py`, `prereg.py`, `tests/conftest.py` : mineur 8), les dix fichiers d'essais ; `ESSAIS` = les dix.

### `src/controle_ia/organisme_idees_juge/verificateur_texte_v2.py` (neuf ; majeur 3, mineur 9)
Constantes **tirées du texte**, écrites ici (log(1/20), log(24/0,05), blocs de 25, 800, 200, 250, 4 800, 6 000, 10 000
rééchantillons, quantiles 2,5 % et 97,5 %, 20 000 générations synthétiques, plafond 50, 20 000 instances d'oracle,
1 000 tirages du cosinus, 500 et 750 générations, les sept bras) ; `exiger_constantes_du_texte()` compare chaque constante
du moteur ; troisième écriture des bras (bloc par bloc, d'après [T] l. 430-447 et les seuils de l. 325-327), de la valeur
e et de e-BH ; `verifier_generation` refait tout sur chaque génération jouée. Messages sans allocation ni valeur
(mineur 9, côté v2 ; les messages de `rejeu_v1` restent tels quels, jugés acceptables par [CL]).

### `src/controle_ia/organisme_idees_juge/oracle_v2.py` (neuf ; mineur 1)
`table_oracle` = celle de la v1, plus `membres_a_la_borne_triviale` (membres ajustés rendus à 0 par le juge). Couple de
[CL] : ancien `valeurs[m["nom"]] = …valeurs_ajustees(…)[n]` seul ; nouveau : champ écrit dans la table, compte rapporté
par la lecture v2 dans `audit_R4`, sans toucher un critère.

### `src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py` (neuf ; majeur 3, mineurs 1 et 2)
`lire` v2 = `exiger_niveau_intervalle` (l'intervalle rendu sur un vecteur de référence doit égaler les quantiles 2,5 % et
97,5 % recalculés par une écriture indépendante, rééchantillon par rééchantillon, graines `(99, b)`), puis la lecture v1
**inchangée**, plus le rapport des membres à la borne triviale ; `charger_sortie_complete` exige `journal.json` scellé et
rattaché au même manifeste, refuse `arret.json`, compare l'empreinte du manifeste lu à celle des sorties ; écrit
`lecture-gelee-v2.json`.

### `src/controle_ia/organisme_idees_juge/mutations_v2.py` (neuf ; majeur 3 c)
Le banc v1 inchangé (18 mutations), plus les quatre mutations de [CL] (code recopié de son annexe A) et deux variantes
de la quatrième (règle écrite en dur dans `arretee_bas` ; constante mutée avec la garde des constantes neutralisée, pour
éprouver la troisième écriture seule), sur des trajectoires d'essai qui placent des cartes entre 1/20 et 1/10 à 50 tirages.

### `scripts/jouer_idee_1_2_v2.py` (neuf ; majeur 2, mineurs 3, 4, 5)
- majeur 2 — ancien (v1, l. 55 et l. 113) : `def exiger_prereg(racine_depot: Path = RACINE_DEPOT)` ; `exiger_prereg()` ;
  nouveau : `def exiger_prereg(racine_depot: Path)` sans défaut ; `exiger_prereg(RACINE_DEPOT)` dans le jeu décisif et la
  miniature : la racine vérifiée est toujours celle que le lanceur emploie (patchable dans les essais) ; **ordre des
  gardes** écrit en tête du fichier et vérifié par un essai : préenregistrement, arbre propre, sorties et manifestes
  antérieurs, addendum, copie du juge, constantes du texte, essais, mutations, manifeste, jeu ;
- mineur 3 — `exiger_sortie_absente` cherche le suffixe du jeu sous `diag/organisme-idees-juge-v1/` **et** sous `runs/` ;
- mineur 4 — le manifeste est créé avec la tâche « racine-du-texte » et `entropie = racine` : le champ `graines` porte la
  racine et son état de contrôle (la clé de dérivation que `manifeste.graines` attache à cette tâche, empreinte de son nom, n'est employée par aucun tirage du jeu : les clés du jeu sont celles du texte, écrites dans la configuration) ; la configuration porte `etats_de_controle` de neuf clés du texte (monde, archive, issues
  fraîches, positions, placebo, oracle, rééchantillonnage, jeu synthétique), revérifiés par le lecteur v2 (mêmes règles
  de dérivation que le jeu : `SeedSequence(entropy=racine, spawn_key=clé)`) ;
- mineur 5 — `installer_signaux()` pose `gardes.lever_sur_term` sur TERM au début du jeu décisif et de la miniature :
  un arrêt externe est consigné dans `arret.json` ;
- enchaînement `execution_v2`, banc `mutations_v2`, lecture v2 (miniature), essais v1 et v2 (`lancer_essais`).

### `scripts/lire_idee_1_2_v2.py` (neuf ; mineurs 2 et 4)
Ancien (v1, l. 38-45) : `m, _ = lire_manifeste(chemin_m)` ; nouveau : `m, sha_m = lire_manifeste(chemin_m)`, revérifie les
états de contrôle, puis `ecrire_lecture(…, manifeste_sha=sha_m)` (refus si les sorties portent une autre empreinte de
manifeste, si `arret.json` existe, si `journal.json` manque).

### Essais neufs
- `tests/test_organisme_idees_juge_constantes_v2.py` (majeur 3) : seuils épinglés (−2,5 à 50 tirages : pas d'arrêt ;
  −3,0 : arrêt ; −3,5 à 25 seulement : pas d'arrêt ; égalités exactes `SEUIL_BAS == log(1/20)`, `SEUIL_HAUT ==
  log(24/0,05)`) ; niveau de l'intervalle épinglé (égal aux quantiles 2,5 % et 97,5 % recalculés, strictement plus large
  que 5 % et 95 %) ; constantes du texte (sain, huit artefacts) ; troisième écriture égale au moteur sur 30 jeux tirés
  au hasard (dont un tiers en régime proche du banc) ; troisième écriture qui voit un seuil partagé par le moteur et le
  vérificateur v1 ; artefacts de `verifier_generation` (sans chiffre dans le message) ; e-BH du texte = juge.
- `tests/test_organisme_idees_juge_lecture_v2.py` : membres triviaux rapportés sans changer le verdict ; intervalle muté
  refusé ; sortie complète exigée (journal, arrêt, empreinte du manifeste) ; lecteur v2 sur une sortie fabriquée de
  1 250 générations (sain ; état de contrôle altéré ; empreinte de manifeste différente).
- `tests/test_organisme_idees_juge_mutations_v2.py` : banc v2 complet, 24 sur 24, raisons vérifiées.
- `tests/test_organisme_idees_juge_execution_v2.py` (majeurs 1 et 2, mineurs 3 à 5) : attente bornée (sain ; fils mort ;
  garde des 24 h relue avec une tâche bloquée ; un seul processus ; plus de deux refusés) ; arrêt consigné sur fils mort,
  sans `jeu.json` ; fichiers gelés v2 ; enchaînement v2 (oracle v2, troisième écriture appelée, phases dans l'ordre) ;
  constante altérée refusée avant toute écriture ; `exiger_prereg` sans défaut, sain et trois artefacts (absent, compagnon
  absent, modifié puis rescellé) **chacun pour sa raison** ; jeu décisif refusé pour la bonne raison dans les quatre cas
  (dont « modifié » sans rescellement) ; ordre des gardes, manifeste antérieur sous `runs/`, sortie antérieure sous
  `diag/` ; champ `graines` et états de contrôle (sain, artefact) ; signal TERM ; refus de la miniature ;
  `lancer_essais` couvre les dix fichiers.

## Les neuf mineurs de [CL]

| n° | traitement |
|---|---|
| 1 | `oracle_v2` + lecture v2 (signalé, rapporté dans `audit_R4` ; aucun critère touché) |
| 2 | `lire_idee_1_2_v2.py` + `charger_sortie_complete` |
| 3 | `exiger_sortie_absente` v2 (`runs/` et `diag/`) ; essai |
| 4 | champ `graines` rempli (racine) ; `etats_de_controle` dans la configuration, revérifiés par le lecteur ; essai |
| 5 | `installer_signaux` ; fils au défaut ; essai |
| 6 | trois lectures ajoutées ci-dessous (lectures 19 à 21) |
| 7 | dit ci-dessous (lecture 14 complétée) ; sans changement de code |
| 8 | infrastructure dans `FICHIERS_GELES` v2 : l'addendum doit la lister |
| 9 | messages v2 sans chiffre ; messages v1 gardés (acceptables selon [CL]) |

## Lectures du texte : les dix-huit de [RD1], plus trois (mineur 6)

Les dix-huit lectures de [RD1] restent, jugées fidèles par [CL]. Lecture 14 complétée (mineur 7) : les 50 cartes de
l'essai E1 sont toutes dans les cellules 0 et 1 (V1) et, pour la famille N, dans le monde M₀ ; la lettre de [T] l. 469
(« 50 cartes couvrant chaque sorte ») est tenue ; l'égalité de préfixe ne dépend pas de la loi de la carte ni du monde
(elle tient à l'évaluateur), mais aucun monde M₀′ ni cellule V2 à V5 n'y est essayé. Lectures ajoutées :

19. Famille T : la loi de base des trois « copies de la classe » tempérées et inclinées est tirée uniforme parmi S1 à S4
    (`banc` l. 206) ; [T] l. 394-395 ne le précise que pour la famille N (l. 417).
20. Bras P′ : la phase 2 commence au tour max(tour de fin de la phase 1, 8) (`rejeu` l. 159), non au tour qui suit.
21. Étiquette d'arrêt d'une carte (`rejeu` l. 241-249) : ordre haut, plafond, bas, fin ; sous P et P′, une carte arrêtée
    bas qui a repris reste étiquetée « bas » : les parts d'arrêts de ces deux bras se lisent avec cette réserve.

## Écarts au texte scellé

E-1 (lieu du code) et E-2 (monde jouet tiré par génération) : inchangés, jugés acceptables par [CL] (E-2 tenu pour une
lecture), à déclarer dans l'addendum ; le nœud de Lazar reste ouvert (R-2899). La v2 ajoute un lieu de plus pour E-1 (sept
fichiers v2 sous `src/` et `scripts/`). Aucun écart neuf.

## Essais

Suite complète, dix fichiers (`lancer_essais` du lanceur v2, sous la charge du jour) : **167 passés sur 167**, 690 s ; 109 essais v1 (inchangés) et 58 essais v2 (36 + 4 + 1 + 17). Essais d'infrastructure (`test_manifeste`, `test_scellement`, `test_prereg`, `test_run_factice`) : non touchés par la v2 (30 sur 30 à la v1, fichiers inchangés). Deux avertissements de Python (`DeprecationWarning` : `fork` dans un processus à plusieurs fils d'exécution), dans les deux essais où un pool en suit un autre dans le même processus d'essai ; sans effet observé.

Note (R5, majeur 2) : l'essai v1 `test_lanceur_refuse_un_preenregistrement_non_scelle`, vert pour une autre raison, reste dans la suite parce qu'il porte sur le lanceur v1, inchangé ; le lanceur v2 a ses propres essais, qui exigent le motif de chaque refus.

## Les quatre mutations de [CL], rejouées

Greffons recopiés de l'annexe A de [CL], empreintes égales (`c1f2fc4e…`, `60253624…`, `749cb52b…`, `690a4f3a…`) ; lanceur
de [CL] repris, la liste des fichiers d'essais portée aux dix fichiers (v1 et v2) ; sortie au bloc-notes.

| n° | mutation | sort sur la suite de dix fichiers | essais qui la tuent |
|---|---|---|---|
| 1 | A lit le bloc suivant hors de la garde d'accès | **tuée** : 58 échecs, 4 erreurs (238 s) | `rejeu_v1` (23), `constantes_v2` (25), banc de mutations v1 et v2, enchaînements v1 et v2 |
| 2 | placebo ciblé | **tuée** : 50 échecs, 4 erreurs (215 s) | `rejeu_v1` (28), `constantes_v2` (28), banc de mutations v1 et v2, enchaînements v1 et v2 |
| 3 | intervalle à 90 % (survivait à la v1) | **tuée** : 4 échecs, 1 erreur (1 067 s) | `test_niveau_de_l_intervalle_epingle`, trois essais de `lecture_v2` (auto-contrôle), banc v2 |
| 4 | seuil d'arrêt bas à 1/10 (survivait à la v1) | **tuée** : 35 échecs, 1 erreur (1 052 s) | `test_seuils_du_texte_epingles`, `test_constantes_du_texte…`, les 30 `test_troisieme_ecriture_egale_au_moteur`, `…voit_un_seuil_partage`, `verifier_generation`, enchaînement v2, banc v2 |

Empreintes des sorties brutes (bloc-notes) : mutation 1 `d799400aad29b920…`, 2 `e8484350a2970dad…`, 3 `9ccf2e1a9e062ef5…`, 4 `d531be22cef95dcf…` ; lanceur des greffons `16836b0f…` (celui de [CL], liste des essais portée à dix fichiers).

## Banc de mutations v2

24 sur 24 tuées pour la raison attendue (18 du banc v1, inchangé ; 6 neuves) :

| mutation | tuée par |
|---|---|
| [CL] 1 : A lit le bloc suivant hors de la garde d'accès | vérificateur indépendant v1 (« allocation non conforme ») ; la troisième écriture la verrait aussi |
| [CL] 2 : placebo ciblé | vérificateur indépendant v1 |
| [CL] 3 : intervalle à 90 % | auto-contrôle de la lecture v2 (« niveau de l'intervalle ≠ 95 % ») |
| [CL] 4 : seuil bas à 1/10 (constante) | constantes du texte (« rejeu.SEUIL_BAS ») |
| [CL] 4 bis : même règle écrite en dur dans `arretee_bas` | vérificateur indépendant v1 (sa constante est restée juste) |
| [CL] 4 ter : constante mutée, garde des constantes neutralisée | troisième écriture du texte seule (« allocation non conforme au texte ») |

## Répétition miniature par le lanceur v2

`python -I -B scripts/jouer_idee_1_2_v2.py --miniature --sortie <bloc-notes>/miniature-v3-lanceur-v2 --n-T 5 --n-N 5 --processus 2 --synthetique 1000 --reechantillons-synthetiques 1000 --reechantillons-lecture 1000` (racine d'essai, garde : refus de celle du texte). Cinq fichiers scellés et vérifiés (`controles-avant-jeu`, `oracle`, `jeu`, `journal`, `lecture-gelee-v2`) ; journal `version_execution = 2` ; banc de mutations v2 : 24 sur 24 ; E1 (deux cartes) sans échec ; aucun membre du nul à la borne triviale ; champ `graines` rempli, neuf états de contrôle. Durée murale 391 s, sous une charge plus forte qu'à la v1 (la mutation 1 de [CL] tournait en même temps) : 40,7 s par génération et par processus en moyenne (13,5 à 63,3), oracle 7,5 s, E1 105 s par carte. **Je n'ai lu de la lecture que la liste de ses clés.** **Écart de manipulation, dit** : une erreur de ma commande (variable du bloc-notes vide dans un travail en arrière-plan) a d'abord écrit cette sortie jetable sous `/miniature-v3-lanceur-v2` (racine du système de fichiers, hors du dépôt) ; je l'ai déplacée dans le bloc-notes ; rien n'a touché le dépôt.

## Durée estimée du run réel

Inchangée en substance ([RD1], confirmée par [CL]) : ≈ 3 à 5,5 h sur deux processus d'une machine libre, ≈ 6 à 7,5 h
sous la charge du jour. La v2 ajoute par génération la troisième écriture (millisecondes) et, aux contrôles avant jeu,
les essais v2 (environ 11 à 12 min de suite complète sous charge) et les six mutations neuves (secondes).

## Ce qui reste non éprouvé

Comme [RD1] : le run réel, E1 sur les 50 cartes réelles, le banc de mutations avec la racine du texte, l'enchaînement
complet du mode décisif (il exige un commit et l'addendum). En plus : la détection du fils mort repose sur l'attribut
`Pool._pool` de CPython 3.13 (absent : arrêt) ; une tâche bloquée **sans** mort de fils n'est bornée que par la garde des
24 h (relue toutes les 5 s) ; un avertissement de Python (`DeprecationWarning` : `fork` dans un processus à plusieurs fils d'exécution) apparaît
dans les essais où un pool suit un autre dans le même processus pytest (sans effet observé).

## Ce que je n'ai pas fait

Aucun jeu du préenregistrement ; aucune lecture de résultat ; aucun commit ; aucun fichier v1 modifié.
