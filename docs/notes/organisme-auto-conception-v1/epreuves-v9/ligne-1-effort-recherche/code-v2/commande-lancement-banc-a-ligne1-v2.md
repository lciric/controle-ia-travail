# Banc A, ligne 1 — commande de lancement (code v2)

Remplace `code-v1/commande-lancement-banc-a-ligne1-v1.md`, qui reste archivée sans modification. Pièce de travail (classe C) ; signée : développeur, modèle L′.

Préenregistrement qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`, sha256 `523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9` (clé PREREG-ORGANISME-V9-LIGNE-1). Code : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/`, fichiers v2 (`lancer_ligne1_v2.py`, `etalonnage_ligne1_v2.py`, `rejouer_journal_ligne1_v2.py`, `analyse_ligne1_v2.py`, `configuration_ligne1_v2.json`) et fichiers v1 repris sans copie (`banc_ligne1_v1.py`, `journal_ligne1_v1.py`) ; empreintes dans `configuration_ligne1_v2.json` (le lanceur refuse un code qui en diffère) et dans `code-v2/rapport-developpeur-corrections-banc-a-v2.md`.

**À ne lancer qu'après** : la vérification des corrections par le contre-lecteur d'un autre modèle ; l'addendum (cinq choix 4.1 à 4.5, noms de fichiers v2 au lieu des noms v1 de l'annexe A, correction 8) et la décision de la mère sur les choix ; le commit du code v2 (le lanceur refuse un code non commis, fichiers neufs non suivis compris) ; la décision de la mère sur le lieu de dépôt des journaux (préenregistrement, « Journal scellé », dernier point ; la recommandation (b) de la contre-lecture retenue — les quelque 155 Mo d'étalonnage hors dépôt — lui revient). Aucune dépense : processeur seul, aucun appel de modèle, aucune connexion (garde A2).

## Lancement (détachable, une seule commande)

Depuis la racine du dépôt de travail, sur le commit qui porte le code v2 vérifié, avec un dossier de sortie neuf hors du dépôt (`D`, nom au choix de la mère) :

```
D=/home/user/runs-banc-a-ligne1-v2 ; mkdir -p "$D" && cd /home/user/controle-ia-travail && setsid nohup env PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/lancer_ligne1_v2.py tout --sortie "$D" --organisme /home/user/ideation-organism/orchestrator --processus 4 >> "$D/lanceur.log" 2>&1 < /dev/null &
```

Réserve 1 de la première contre-lecture (constat 13 a) : le journal du lanceur est ouvert **en ajout** (`>>`) ; une reprise ne l'efface plus.

Ce que fait `tout`, dans l'ordre des gestes du préenregistrement (3 à 7), chaque étape dans un processus à part (session neuve), chacune scellant sa sortie avant la suivante :

1. `etalonner` → `$D/etalonnage/sortie-etalonnage-ligne1-v2.json` (scellée) : quatre forces, couple (s, c), portes (prise A9, cartes jugées par appel A15, audit du générateur A8), part des cartes indéterminées (mesure), T0 seul (A17), versions de Python et de numpy, plateforme, commit de l'organisme, inventaire des fichiers récupérés. Une porte manquée : sortie écrite et scellée, puis arrêt nommé, retour à la mère ; une reprise relit la sortie et lève de nouveau la garde (aucun code 0 silencieux). Une cible de force manquée laisse `$D/etalonnage/etape-forces-echec-A9-NN.json` (scellé : pas de la cible, forces déjà atteintes). Une part d'indéterminées au-dessus de 20 % : dite en tête ; la course décisive refuse de partir (`DecisionMereRequise`, décision de la mère).
2. `decisive` → `$D/decisive/courses/` (un journal et une sortie brute par course et par classe, scellés) puis `$D/decisive/manifeste-course-decisive-ligne1-v2.json` (scellé ; garde A14 ; versions et commit de l'organisme de l'étalonnage et de la course, avec leur égalité ; inventaire des fichiers récupérés).
3. `rejouer` → `$D/decisive/rejeu-ligne1-v2.json` (scellé) : toutes les décisions de tous les journaux décisifs et d'étalonnage rejouées depuis leurs seules entrées, comparées au bit près (A16) ; **chaque journal recoupé avec sa sortie brute** (m de chaque promotion contre le registre, promotions et lignées en course de chaque bras, effet des lignées) ; courses 0, 300 et 599 rejouées à part, avec le recoupement de M1-nul (voir réserve 3).
4. `analyser` → `$D/decisive/lecture-programme-ligne1-v2.json` (scellé) : garde A12, métriques, bornes, table de lecture par programme, prédictions, mentions, points de l'audit de symétrie, gardes A7 et A11 (voir réserve 4). `tout` relance toujours cette étape, même déjà scellée : sa reprise relève A7 ou A11 si elle avait tiré.

Plafond (garde A13) : 43 200 secondes de calcul cumulées sur toutes les sessions (`$D/etat-lancement-ligne1-v2.json`). Au-delà : arrêt du groupe de processus de l'étape par son identifiant (règle R10), arrêt écrit dans `$D/arrets-ligne1-v2.jsonl`, rien n'est lu, code de sortie 13.

Durée prévue sur cette machine (4 cœurs, 4 processus) : environ 1 heure (fourchette 45 minutes à 1 heure 30) ; environ 3 heures 30 sur un cœur (rapport du développeur v1, § 6). Le recoupement du rejeu ajoute la lecture d'une sortie brute par journal : quelques minutes au plus (non mesuré à pleine taille).

## Suivi, reprise, arrêt

- Suivi : `$D/lanceur.log`, `$D/journal-<étape>.log`, `$D/etat-lancement-ligne1-v2.json`.
- **Avant toute reprise** (réserve 2 de la première contre-lecture, constat 13 b) : vérifier que les processus listés dans `$D/pid-lanceur-ligne1-v2.txt` et `$D/pid-etape-ligne1-v2.txt` ne vivent plus, par leur identifiant : `kill -0 $(cat "$D/pid-lanceur-ligne1-v2.txt")` puis `kill -0 $(cat "$D/pid-etape-ligne1-v2.txt")` doivent tous deux répondre « No such process ». Le lanceur v2 fait aussi ce contrôle lui-même au départ de `tout` : si l'un d'eux vit encore, il s'arrête avant toute préparation (`RepriseConcurrente`, code de sortie 4) et n'écrit pas son identifiant. Un identifiant réemployé par un autre processus après un redémarrage fait refuser à tort : vérifier alors à la main ce qu'est ce processus avant de toucher au dossier.
- Reprise après une interruption : **la même commande, le même `D`**. Une étape déjà scellée n'est pas refaite (l'analyse est relancée, voir plus haut) ; dans une étape, une course déjà scellée n'est pas rejouée ; **les fichiers déjà écrits d'une course non scellée (provisoires `.partiel`, journal ou sortie d'une classe déjà renommés, compagnons) sont déplacés, jamais effacés**, dans `courses/partiels-recuperes/reprise-NN/` avec un inventaire scellé `inventaire-partiels-recuperes.json` (nom, octets, sha256), puis la course est rejouée depuis ses graines (sorties identiques au bit près, essai 5). L'inventaire entre dans la sortie de l'étalonnage et dans le manifeste de la course décisive ; l'empaquetage verse ces fichiers avec le reste. La durée cumulée continue de compter.
- Arrêt à la main : par identifiant de processus seulement (règle R10). Le lanceur écrit son identifiant dans `$D/pid-lanceur-ligne1-v2.txt`, et celui de l'étape en cours (chef de son groupe de processus, session neuve) dans `$D/pid-etape-ligne1-v2.txt` : `kill -TERM $(cat "$D/pid-lanceur-ligne1-v2.txt")` puis `kill -TERM -- -$(cat "$D/pid-etape-ligne1-v2.txt")`.

## Les quatre réserves de la première contre-lecture, reprises

1. **Journal du lanceur ouvert en ajout** : `>> "$D/lanceur.log"` dans la commande ci-dessus (au lieu de `>`).
2. **Processus vivants avant toute reprise** : vérification à la main par `kill -0` sur les deux identifiants des fichiers `pid-*.txt` ; le lanceur v2 la refait (`verifier_aucun_processus_vivant`), cas sain et artefact éprouvés.
3. **Recoupement de M1-nul des courses 0, 300 et 599 depuis les décisions du journal** : fait par programme à l'étape `rejouer` (`rejouer_journal_ligne1_v2.recouper_m1_nul`) : pour chaque bras, M1-nul est recalculé depuis les seules décisions d'arrêt du journal (une lignée est « sans effet » si la loi du monde de ses jugements est de type « fixe ») et comparé à celui que calcule l'analyse sur la sortie brute. **Seule la concordance est écrite** dans `rejeu-ligne1-v2.json` (`courses_audit_symetrie.recoupement.m1_nul` : « concordant »), jamais la valeur ; un écart lève `GardeA16Recoupement` et aucun rejeu n'est scellé (l'analyse refuse alors, A12). L'agent de l'audit de symétrie lit ce champ, et peut refaire le calcul par le programme à part : `rejouer_journal_ligne1_v2.py --dossier "$D/decisive/courses" --organisme … --courses 0,300,599 --sortie <fichier neuf>` (le recoupement de M1-nul y est fait dès que `--courses` est donné).
4. **Gardes A7 et A11 qui passent par la ligne 0 de la table** : dans le code v1, elles rendaient la ligne 0 (« lecture refusée ») sans lever leur exception nommée ; la lecture refusée veut dire « rien n'est dit de l'hypothèse ». **Correction 8 (code v2)**, accordée par la mère pour le code (contre-lecture de l'addendum 1 de la ligne 1, décision 3, option C ; la décision reste celle de Lazar) : quand A7 ou A11 tire, la lecture est d'abord écrite et scellée avec la ligne 0 et tous les chiffres (ils servent à l'audit que demande A11), puis l'exception nommée est levée (`GardeA7Indeterminees`, `GardeA11NiveauGeneration`) ; l'étape rend le code 3, `tout` s'arrête sans « chaîne complète », et toute reprise relève la garde.

## Dépôt des journaux (après la chaîne, selon la décision de la mère sur le lieu)

```
env PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/lancer_ligne1_v2.py empaqueter --sortie "$D" --vers <dossier neuf>
```

Morceaux `journaux-banc-a-ligne1-v2-partie-NNN.tar` de 90 Mo au plus, compagnons `.sha256`, manifeste scellé `manifeste-depot-ligne1-v2.json` : empreinte et taille de chaque morceau, empreinte et taille de chaque membre, **empreinte de l'ensemble** (sha256 du JSON canonique de la liste triée [membre, sha256, octets]) et empreinte de la liste des morceaux. `lancer_ligne1_v2.verifier_depot(<dossier>)` relit tout et recalcule ces empreintes avant de pousser (en Python, depuis le dossier du code). Au-delà de 500 Mo compressés au total, le programme refuse (`DepotTropGros`) : arrêt et rapport avant de pousser. Taille prévue : environ 400 Mo (marge de 20 %). Pousser un morceau à la fois.

## Étapes à la main (même effet, une à une)

`lancer_ligne1_v2.py etalonner|decisive|rejouer|analyser --sortie "$D" --organisme /home/user/ideation-organism/orchestrator --processus 4`.

## Essai de fumée

Non rejoué pour le code v2 (consigne du développeur : ni étalonnage ni course). Commande, si la mère le demande : `lancer_ligne1_v2.py fumee --sortie <dossier neuf> --organisme … --processus 4` (racines 2026111990 à 2026111993, disjointes de celles du préenregistrement ; n'imprime que des durées, des tailles, des comptes et des sceaux).
