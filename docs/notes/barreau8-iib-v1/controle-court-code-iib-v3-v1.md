# Contrôle court du code du saboteur à budget (ii-b) après corrections, tête a31b8970 — v1

> Contrôleur neuf (Claude Opus 5.5, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`). Je n'ai écrit ni la conception, ni le code, ni leurs contre-lectures. Code de course **exploratoire, non opposable (R-522)**. Processeur seulement. Rien n'a été lancé sur une carte, rien n'a été dépensé, aucun modèle réel n'a été chargé, aucune clé n'a été lue. Seul appel réseau : `git fetch origin prep/iib-code-v3 lot/compte-4-v1`. Aucun fichier de `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/` du dépôt ouvert. Ni commit, ni poussée. **J'ai lu la consigne privée par programme : je suis exclu de tout rôle de lecteur des sondes du barreau 8.**

## 0. Identité

- Mandat : `docs/notes/barreau8-iib-v1/mandat-controle-court-code-iib-v3-v1.md`, empreinte `5d34050448b80c43153bd4b913560ea1c06cba16985eb8628a86b24d23d022df`, vérifiée (compagnon égal).
- Tête contrôlée : `origin/prep/iib-code-v3` = `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (vérifiée par `git rev-parse`). Tête de référence : `d88e3d947ec4f05958834e2746a800c854271a8f`. Six commits entre elles : `44f59872c`, `558ac0238`, `2fbadeeac`, `e2fbb612e`, `7a7517d6d`, `a31b8970f`.
- Rapports du développeur : v3 `bbe0b978ef0adb6829819f113cf564e0f35e4e3a3320ea4e2b357cf3a20bbc84`, v4 `abf71b6524363a12a3326de97cca79c8cff8d8c2718b907721b9accf0b8ec279` ; égaux à leurs compagnons et au mandat.
- Rapports demandeurs (dépôt principal), sceaux vérifiés : vérification courte v3 `e5c31d4f6949…` (VC3-01 à VC3-07) ; contre-lecture d'ordre et de devis `d398bf5c4a79…` (O-M1, O-M4 ; O-M5, O-M6 en renseignement).
- Consigne privée : lue par `git show origin/lot/compte-4-v1:…` dans un script hors dépôt ; empreinte `9f8bbdef…90c1`, égale à son compagnon ; découpée par `iib/consigne_v1` : consigne de 95 mots, indication de 12 mots, 9 motifs. Rien affiché, rien recopié.
- Extraction à moi : `git archive a31b8970… | tar -x` vers `/tmp/ctl-iib-v3/x` ; module chargé vérifié (`controle_ia.iib.lanceur_v1.__file__` sous l'extraction). Extraction, dossiers d'essais et dépôts jouets supprimés à la fin.

## 1. Verdict

**Autorisable après corrections.**

Constats : **0 bloquant, 1 majeur, 8 mineurs.**

Les neuf points sont traités dans le code. Huit le sont avec un essai qui protège. Le neuvième, O-M1, est corrigé dans le code, mais son essai ne protège pas : j'ai retiré la correction dans ma copie, et l'essai passe encore (CC-01, majeur). Je n'ai trouvé aucune fuite de la consigne privée sur la branche. Les 424 essais passent. La répétition jouet est identique à l'octet.

## 2. Constats

| identifiant | gravité | où | constat | correction demandée |
|---|---|---|---|---|
| **CC-01** l'essai de O-M1 ne lit pas la ligne réelle du lanceur | **majeur** | `tests/test_iib_amorce_v1.py:198-210` ; `src/controle_ia/iib/lanceur_v1.py:292` | Les deux essais neufs passent deux lignes **écrites à la main** dans les motifs de l'amorce. Ils n'appellent ni le lanceur ni sa fonction de progrès. La contre-lecture demandait que « la ligne réelle du lanceur » passe les deux motifs. Épreuve faite : j'ai remis l'ancienne ligne (`echec=…`) dans ma copie du lanceur. Résultat : `2 passed`. La correction elle-même est juste. Je l'ai rejouée sur les lignes réellement émises par la fonction de progrès du lanceur, passées dans les deux motifs lus dans l'amorce. Avec la correction, `etat=passees epreuve=aucune` et `etat=arret epreuve=E-O3` sont relayées. Sans elle, les deux lignes sont retenues. Sur un jeu jouet complet du lanceur, les 24 lignes de progrès émises sont bien formées et aucune n'est retenue. | L'essai sain doit faire passer dans les deux motifs de l'amorce la sortie d'erreur d'un jeu jouet réel du lanceur, ou un appel réel à la ligne de la l. 292, pour les deux issues des épreuves. Il doit exiger au moins une ligne `etape=epreuves` relayée. L'artefact garde l'ancienne forme et doit la voir retenue. |
| CC-02 essai de non-fuite : protège, avec des angles morts | mineur | `tests/test_iib_exclusion_v1.py:195`, `:201`, `:215-224`, `:234-242` | **VC3-01 est corrigé.** J'ai planté un motif réel de rang 1 (25 caractères) dans `scripts/piege_iib_tmp.py` : l'essai sain **échoue**. Un triplet réel de la consigne planté au même endroit le fait aussi échouer. Fichier retiré : l'essai passe. L'artefact appelle bien la recherche réelle, `_chercher_fuites`. Il reste quatre angles morts. (a) La recherche est sensible à la casse (`motif in texte`) : le même motif planté en capitales passe. (b) Seuls les suffixes `.py`, `.sh`, `.txt` et `.md` sont lus : le motif de rang 5, planté dans `scripts/piege_iib_tmp.json`, passe. (c) Le périmètre ne couvre ni la configuration de course (`prereg/`) ni les messages de commit. (d) L'artefact ne plante qu'un motif, pas de triplet. | Recherche insensible à la casse. Lire tout fichier textuel. Ajouter au périmètre les configurations `*iib*` sous `prereg/`. Planter aussi un triplet dans l'artefact. La recherche des messages de commit reste un contrôle de la mère, fait par programme (§ 5). |
| CC-03 un chemin de fuite hérité, voisin de VC3-05 | mineur | `tests/test_iib_exclusion_v1.py:125` | `assert ex.mentions(c["consigne"], m) and ex.mentions(c["indication"], m)` porte sur la consigne **réelle**. En cas d'échec, l'introspection de `pytest` affiche les arguments de l'appel. Je l'ai vérifié sur un texte factice : il est affiché. Sur l'instance, la sortie de la suite (`tests.txt`) part dans les traces poussées (`amorce_instance_iib_v1.sh:339`). Cette ligne est antérieure à la v3 et n'était pas nommée par VC3-05. | Calculer le booléen à part : `ok = …` puis `assert ok, "rang …"`. |
| CC-04 (06) : l'artefact voit les fichiers, pas les contextes | mineur | `tests/test_iib_consigne_invisible_v1.py:152-158` | Le marqueur est planté dans les actions de l'évaluation hors maître. L'essai vérifie seulement qu'il apparaît dans les fichiers de textes de l'évaluation. La garde de l'essai sain qui était sans artefact porte aussi sur les contextes de `generer_actions` aux pas 1 à 9 de l'évaluation (`ctx_autres`, `:127`). Rien ne prouve que la collecte les voit. | Ajouter `assert any(_fuit(x) for p, x in r["contextes_generer"] if p.startswith("evaluation-"))`. |
| CC-05 (11) : artefact tautologique | mineur | `tests/test_iib_lanceur_v1.py:334-342` | L'essai fabrique un ensemble qui contient « honnete », puis vérifie qu'il contient « honnete ». Il n'appelle ni le lanceur ni la vérification de l'essai sain. C'est la forme reprochée par VC3-01(b). | Mettre la vérification de l'essai sain dans une fonction, et l'appeler sur les fiches vraies (sain) et sur les fiches falsifiées (artefact). Mieux : falsifier la condition dans le lanceur par `monkeypatch` et voir l'essai sain échouer. |
| CC-06 rapport v4 inexact par endroits | mineur | `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v4.md`, § O-M4 « Note », § O-M6, « Comptes » | (a) « 4 fichiers comparés » à la répétition jouet. J'obtiens 48 fichiers comparés à l'entropie 20261118, et 54 à l'entropie 20261114, ce qui confirme le chiffre du rapport v3. (b) « La suspension de la destruction … est déjà présente » est imprécis. En mode réel aussi, la fin anormale demande l'état « stopped » : le disque est gardé (`amorce…:114-127`, `:351-353`). Mais rien dans le code ne suspend une destruction : c'est un acte de la mère (§ 4). (c) Le § O-M6 ne dit pas que l'amorce rejoue le calendrier sur l'instance (`:323`) et refuse un démarrage daté d'après le dernier jour de création. Or c'est le constat de O-M6. (d) Le § O-M5 décrit le clonage de l'amorce, alors que O-M5 portait sur les deux clonages entiers de l'étape 1 de l'ordre, sur la machine de la mère. | Aucune correction du code. La mère lit O-M5 et O-M6 dans la contre-lecture, pas dans le rapport v4. Un rapport v5 (nom neuf) seulement si la branche change encore. |
| CC-07 deux lignes hors des neuf points | mineur | `.gitignore:11-12` (commits `558ac0238`, `7a7517d6d`) | `repetition-jouet-v3/` et `repetition-jouet-v4/` sont ignorés. Ces lignes ne se rattachent à aucun des neuf points. Elles sont sans effet sur la course : l'amorce ne lit `git status` que sous `runs`, `diag`, `donnees` et `traces`. L'ajout de `"--porcelain"` aux marqueurs du diff borné (`tests/test_iib_amorce_v1.py:174`) se rattache à O-M4, mais il élargit ce que l'essai laisse passer. | À déclarer, ou à retirer. Aucun effet sur le verdict. |
| CC-08 VC3-07 fixe un sous-point du nœud du portage | mineur | `src/controle_ia/iib/lecture_v1.py:235-237`, `:299` | Le gradient est maintenant recalculé après le dernier pas, et la clé du facteur est lue sans défaut (présente dans `FIXES_PAR_LE_CODE`, `configuration_v1.py:58`). C'est bien ce que VC3-07 demandait. Mais cela tranche par le code le sous-point (g), « gradient lu avant ou après le dernier pas », de la liste du nœud du portage de la base textuelle (vérification courte v3, § 6.2). | La mère l'écrit dans la décision du portage : (g) est fixé à « après le dernier pas » par ce commit. Aucun autre réglage du portage n'a changé. |
| CC-09 le contrôle des fichiers ignorés ne joue qu'en fin de run | mineur | `scripts/amorce_instance_iib_v1.sh:443-448` ; `:350`, `:291-300` | Le contrôle par `--ignored` ne tourne que sur le chemin de la fin de run. Sur l'arrêt consigné, sur la minuterie et sur un second démarrage, un nom neuf que les motifs de `ajouter_legeres` ne couvrent pas resterait sur le disque sans alerte. C'est tenable : ces chemins finissent en « stopped », disque gardé, et le rapatriement compare avec la liste des empreintes (§ 4). | Aucune correction de code exigée avant la course. Le contrôle du rapatriement (§ 4) couvre ce trou. |

## 3. Les neuf points → état constaté

| point | état | preuve |
|---|---|---|
| VC3-01 essai de non-fuite | **corrigé** (angles morts : CC-02) | Planté → échec ; retiré → passe ; l'artefact appelle `_chercher_fuites`. Périmètre étendu aux rapports du développeur. |
| VC3-02 gardes neuves sans artefact | **corrigé en grande partie** | (13) : neuf bornes de l'offre avec artefact, toutes passées. Ligne de 7b sans identifiant d'instance : refusée (`tests/test_iib_scripts_v1.py`). (12) : clé et calcul vérifiés sur la course jouet, avec un essai du signe. (06) : en partie (CC-04). (11) : artefact sans portée (CC-05). |
| VC3-03 rapport fidèle | **corrigé** pour le rapport v3 (54 fichiers rejoués à son entropie) ; v4 : CC-06 | |
| VC3-04 paire commune | **corrigé** | La plus longue sous-chaîne commune de `jouet_v1.py` avec la consigne passe de 13 à 10 caractères. La plus longue suite commune est d'un mot. Aucun triplet. |
| VC3-05 messages d'échec | **corrigé** aux lignes nommées (`:71`, `:116-117`, messages de `_chercher_fuites` : rang, longueur, nom) ; résidu hérité : CC-03 | |
| VC3-06 ligne de 7b | **artefact fait** ; la **forme** de la ligne reste à fixer par la mère, le motif `7b.*\binstance\s+\d+` étant toujours celui du développeur (`session_v1.py:76`) | |
| VC3-07 défaut silencieux, gradient | **corrigé** (CC-08) | |
| O-M1 ligne de progrès des épreuves | **code corrigé ; essai sans portée** (CC-01, majeur) | Relais rejoué sur les lignes réelles : relayées avec la correction, retenues sans elle. |
| O-M4 fichiers par phase, contrôle de fin | **corrigé** | Voir § 4. |

**Point 1 du mandat, différence entre les deux têtes.** Les 15 fichiers changés se rattachent chacun à un point. Seule exception : les deux lignes du `.gitignore` (CC-07). **Aucun code d'enregistrement de l'activité interne** : `ajouter_morceaux` rend toujours 0, et le diff n'ajoute aucune capture. **Aucun réglage du portage de la base textuelle**, hors le sous-point (g) fixé par VC3-07 (CC-08).

## 4. O-M4 et ce que la session mère doit faire elle-même

**Code, éprouvé dans des dépôts jouets** (bac à sable des essais de l'amorce, `.gitignore` portant `donnees/`) :
- Tête telle quelle : l'essai sain des fichiers par phase et l'artefact des fichiers ignorés passent.
- Motifs par phase retirés de `ajouter_legeres` dans ma copie : l'essai sain **échoue**.
- `--ignored` retiré du contrôle de fin dans ma copie : l'artefact **échoue**.
- Chemin de l'arrêt consigné, par un essai à moi hors dépôt (faux lanceur en arrêt, noms d'étalonnage, de tour 1 et d'évaluation) : les neuf fichiers par phase et leurs sceaux sont poussés. Le même essai **échoue** sans les motifs.
- Les trois chemins (fin de run `:423` ; arrêt consigné `:350` → `:291` ; minuterie `:302-305` → `:291`) passent par la même fonction `ajouter_legeres`.
- Sur un jeu jouet réel du lanceur, les 34 fichiers écrits sous `donnees/<run>/` correspondent tous aux motifs de `ajouter_legeres`. Le contrôle par `--ignored` ne fera donc pas de fausse fin anormale sur ces noms.
- Arrêts par l'identifiant (R10) : la fin, normale ou anormale, demande l'état « stopped » sur l'identifiant de l'instance et garde le disque (`:114-127`). Une destruction passe par la minuterie ou par la session, à l'identifiant (lu à l'outil de lecture, sans recherche en ligne de commande).

**Ce que la mère doit faire, et quand :**
1. **Avant le scellement de l'ordre** :
   - écrire au § 7 (point R-A) la liste des fichiers attendus, en plus des fichiers combinés et des deux adaptateurs : `oracle-iib-<phase>.json`, `ids-actions-iib-<phase>.npz`, `textes-actions-iib-<phase>.jsonl`, chacun avec son `.sha256`, pour la phase valant `etalonnage`, `tour1` … `tour<r>` et `evaluation` ;
   - remplacer le texte de l'étape 5 du § 5 par le couple O-M4 de la contre-lecture : tout fichier listé absent de la branche, ou présent sans compagnon conforme, est un écart rapporté à la mère, et **la destruction (étape 6) attend son mot**, au plus tard jusqu'à 2026-11-27T22:00:00Z ;
   - écrire l'heure limite de création de O-M6 (« aucune commande de création après 23:00 UTC le 2026-11-25 ») : le code ne la porte pas ;
   - écrire la forme réduite du clonage de l'étape 1 (O-M5), après l'avoir jouée à blanc : le code ne la porte pas.
2. **Au rapatriement, instance en « stopped », avant toute destruction** :
   - récupérer la branche du run ;
   - prendre la liste `resultat.empreintes` de `diag/<run>/resume.json` (sur le jeu jouet, elle compte 17 fichiers sous `donnees/`, phases comprises), ou bien `sorties_ecrites` de `diag/<run>/arret.json` si le run s'est arrêté ;
   - la comparer à `git ls-tree -r` de la branche ;
   - vérifier chaque compagnon par `python -m controle_ia.scellement verifier` ;
   - relever dans le journal et les traces : `ERREUR DE CHAÎNE`, `FIN ANORMALE`, `iib-fichiers-trop-gros.txt`, `progres-retenues.txt`.
3. **Si un fichier manque** :
   - ne pas détruire ;
   - relancer l'instance arrêtée (un second démarrage pousse d'abord les commits en attente, C13), ou lire son disque ;
   - puis détruire par l'identifiant, et seulement quand tout est là ou sur le mot de la mère, avant 2026-11-27T22:00:00Z.

## 5. Essais, répétition, graines, non-fuite

- **Suite ciblée** : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<extraction>/src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider --basetemp=<à moi> -rsx $(cat scripts/tests-cibles-iib-v1.txt)`. Dernière ligne : **`424 passed in 127.49s (0:02:07)`**, fin à 2026-11-18T20:58:09Z, aucun saut. La liste ciblée garde l'empreinte `847676ef…e3b6`, égale à celle de l'amorce (`:373`). Les 18 essais neufs (406 → 424) sont ceux que décrivent les rapports v3 et v4.
- **Répétition jouet** (dépôt jetable) : `preparer` (entropie 20261118, configuration `75b8a4a0…09e9fd`), puis deux `jouer` et `comparer`. Résultat : **48 fichiers comparés, 0 différent**, code 0. À l'entropie 20261114 : 54 comparés, 0 différent. Fichiers par phase présents (étalonnage, tour 1, tour 2, évaluation). Les sorties factices ont été supprimées.
- **Graines (R9)** : le diff ne contient aucune source d'aléa nouvelle (aucune graine, aucun générateur, aucun `random`).
- **Moyenne ou médiane sur les jetons** : aucune dans le diff. Le paquet n'a aucune sonde.
- **Non-fuite sur toute la branche** (point 6). Un script hors dépôt a parcouru les 40 fichiers ajoutés ou modifiés depuis la base commune avec `origin/main` (`a3adf4128`), hors les fichiers de consigne eux-mêmes. Il a aussi parcouru les messages des 7 commits de la branche, et l'ensemble des lignes ajoutées. Résultats :
  - triplets communs avec la consigne ou l'indication : **0** partout ;
  - motifs réels à la lettre, sans tenir compte de la casse : **aucun** ;
  - motifs réels qui trouvent quelque chose : **aucun** ;
  - plus longue suite commune : 2 mots au plus ;
  - plus longue sous-chaîne commune : 10 caractères au plus.

  La méthode a été validée sur la consigne elle-même : 93 triplets, 10 triplets de l'indication et les 9 motifs à la lettre. Les fichiers hérités de `main` signalés par la vérification v3 (§ 5.2) restent à trancher par la mère. Je ne les ai pas rouverts.

## 6. Ce qui reste avant la course

1. **CC-01** : essai de O-M1 sur la ligne réelle. Correction courte, puis rejeu de la suite ciblée. Si la liste ciblée ne change pas, son empreinte ne change pas non plus. Le commit qui en sortira sera celui que citeront `COMMIT_CODE_IIB` et `EMPREINTES_CODE_IIB`.
2. Les mineurs **CC-02 à CC-05** sont souhaitables avant la course, en particulier CC-03 (sortie de la suite poussée dans les traces). CC-06 à CC-09 relèvent de la mère, dans l'ordre ou dans les registres.
3. **La forme de la ligne de création de 7b** (VC3-06) : la fixer, puis aligner le motif et son artefact.
4. **Le nœud du portage de la base textuelle** reste non tranché (vérification courte v3, § 6.2), avec le sous-point (g) désormais fixé par le code (CC-08).
5. **L'ordre** : § 7, étape 5, heure de création limite et clonage réduit (§ 4 ci-dessus), puis les autres points de la contre-lecture d'ordre (O-M2, O-M3, les marqueurs), une contre-lecture neuve et le scellement. Ensuite le devis.
6. Restent aussi les points 3, 4, 5, 7, 8, 9 et 10 du § 6 de la vérification courte v3, inchangés par cette branche : CLV2-09 et CLV2-10, la borne bilatérale, la ligne de GO dans le commit, les épreuves en réel, le jetoniseur réel, et la branche v2 sur le distant.

## 7. Lectures hors de ce mandat, limites, refus

- **Lectures hors des fichiers nommés par le mandat**, pour éprouver les points :
  - modules et essais de la branche : `iib/consigne_v1.py`, `iib/lecture_v1.py:205-239`, l'amorce (`:90-130`, `:240-454`), des extraits de `tests/test_iib_*` ;
  - le harnais `tests/test_t06_v12_amorce.py`, pour le faux lanceur ;
  - `scripts/repetition_jouet_iib_v1.py`, en-tête ;
  - `git merge-base`, `git diff --name-only` et `git log` sur `origin/main` et la branche.
- **Exécutés sans relecture de leur code** : `t06.lanceur.progres`, `t06.session_v3`, `premier_test_ia.conditions.blocs_cites`, `manifeste`.
- **Non lus** : la base (A) de T0.8, l'ordre, le devis, la conception, les registres, et rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` du dépôt. Les fichiers `diag/` et `donnees/` lus l'ont été dans mes dépôts jouets jetables, et étaient factices.
- **Limites** :
  - la recherche de fuite compte des triplets, des suites, des sous-chaînes et des motifs : une paraphrase lointaine lui échappe ;
  - les modules inchangés depuis `d88e3d94` n'ont pas été relus ;
  - la routine de reprise n'a pas été jouée (c'est le rôle de la session mère), et aucune instance n'a été inventoriée.
- **Refus** : aucun.
