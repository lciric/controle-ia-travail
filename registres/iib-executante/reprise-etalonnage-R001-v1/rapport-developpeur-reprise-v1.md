# Rapport du développeur — correctif de reprise R001 de l'étalonnage du saboteur à budget, organisme retenu v5

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de classe B (instrument) : contre-lecture par un autre modèle à faire. Développeur : Claude Opus 5.5, neuf. Rien dépensé, aucun loueur ni modèle externe appelé, rien poussé.

## Verdict
- Arbre final : commit `b4a2c64e6af4bdd8ed781faad73ebfb147877a1a`, parent `997bed6a1`, arbre `4c098d90ba7269cc1331d68a4cf9a9c0608772e4`. Patch : `R001-reprise-etalonnage-iib-v5.patch` (sortie de `git format-patch` ; réappliqué par `git am` sur `997bed6a1` dans une copie neuve, même arbre).
- Liste figée de la reprise (`scripts/tests-cibles-iib-reprise-v5-v1.txt`, 26 fichiers) : **311 essais passent** (294 de la liste v6 et 17 nouveaux). Nombre attendu sur la machine (sans torch) : **311**.
- **L'essai central passe** : un étalonnage jouet coupé après 27 lots (et, dans un second cas, après 25) puis repris rend à l'octet les 28 lots, leurs identifiants et le fichier des graines d'un étalonnage complet. Le fichier des oracles et les rapportés sont égaux eux aussi, sauf les champs mesurés au chronomètre (voir § 3).

## 1. Ce qui est écrit
- `src/controle_ia/iib/reprise_v5.py` (neuf). Ordre de reprise (écriture et relecture). Vérification des lots versés contre le plan scellé. Vérification des graines. Reconstruction des clés de graines d'un lot à partir de ses sorties.
- `src/controle_ia/iib/lanceur_v5.py` :
  - `plan_de_l_etalonnage` et `lots_prevus` (le plan par lot, calculé par le même code que le jeu) ;
  - classe `_Lots` (versement par lot, inchangé dans sa forme) ;
  - `_fin_de_l_etalonnage` : la fin calculée des sorties des lots. Pour un étalonnage complet, le résultat est le même qu'avant : les 23 essais du lanceur passent sans changement.
  - phase neuve **`reprise_etalonnage`**, avec `phase_reprise_etalonnage` et `_executer_reprise`, et l'argument `--etalonnage-partiel <run>`.
  - L'étalonnage ordinaire refuse toujours un dossier déjà joué ; son message nomme maintenant la phase de reprise.
- Le nom de la phase s'écrit avec un trait bas : `reprise_etalonnage`, et non `reprise-etalonnage`. La surveillance du lanceur de session lit la phase avec le motif `[a-z_]*`, qui ne lit pas le trait d'union. Un essai vérifie que l'orthographe à trait d'union est refusée.
- `src/controle_ia/manifeste.py` : nouvel argument facultatif `reserves_declarees`, ajouté à la liste `reserves` du manifeste. C'est là que va la marque de reprise. Rien ne change pour les autres appelants (11 essais du manifeste passent).
- `src/controle_ia/iib/session_v5.py` : la règle de coupure à 16 USD joue aussi en phase `reprise_etalonnage`. Elle se compte depuis le début de l'amorce de la machine neuve.
- `scripts/amorce_instance_iib_reprise_v5.sh` (neuf), tirée de l'amorce de la course. Treize lignes de code sont remplacées une pour une, et aucune n'est ajoutée ; un essai le vérifie. Les six changements :
  - (p1) le lanceur est appelé en phase de reprise ;
  - (p2) le run coupé est celui de l'unique ordre de reprise scellé du commit ;
  - (p3) l'engagement passe par la référence distante `essai/iib-reprise-engagee-<run>` ;
  - (p4) le run est nommé `-iib-reprise-<mode>`, et la fin consigne `diag/<run coupé>/` ;
  - (p5) la liste figée est celle de la reprise ;
  - (p6) le journal dit « reprise ».
- `scripts/lancer_iib_v3.sh` : `IIB_AMORCE=scripts/amorce_instance_iib_reprise_v5.sh` est accepté.
- `scripts/preparer_reprise_iib_v5.sh` (neuf), joué par la session. Il récupère le manifeste, les lots et les identifiants depuis `essai/iib-explo-v6` à son commit nommé, et rien d'autre. Il vérifie qu'ils sont égaux à l'octet au commit et que leurs sceaux tiennent, puis il écrit l'ordre. Il ne committe, ne pousse et ne supprime rien.
- `tests/test_iib_reprise_v5_r001.py` (17 essais). Son nom ne suit pas le motif `test_iib_*_v5.py` : la liste figée v6 de l'étalonnage reste donc intacte, et son essai d'égalité au motif aussi.

## 2. Ce que la reprise fait, dans l'ordre
1. **Gardes avant tout manifeste** (un refus n'écrit rien) :
   - la configuration est égale à celle que scelle `runs/<run>/manifeste.json` ;
   - le run de la reprise est neuf ;
   - aucune reprise n'a déjà eu lieu : ni témoin, ni fin, ni résumé ;
   - l'ordre de reprise est scellé, et chaque fichier qu'il cite a encore son empreinte (R11) ;
   - les lots présents sur le disque sont exactement ceux de l'ordre ;
   - en mode réel, la ligne de GO de l'écart figure dans `registres/go.md` ;
   - les lots versés suivent exactement le début du plan scellé : même ordre des tâches, même taille de lot, mêmes phases, mêmes épisodes et mêmes tâches, une sortie par action et par oracle, schéma tenu, aucun texte ;
   - les graines sont vérifiées : chaque δ consigné par les lots régénérés et plantés est retiré à nouveau sous sa clé et doit être égal au δ consigné ;
   - en mode réel, la machine neuve a un identifiant lisible, autre que celui de la machine 61875617.
2. **Manifeste de la reprise**, avec dans ses réserves :
   - « reprise : lots 1–27 de la machine 61875617, lot 28 de la machine neuve <id> » ;
   - l'écart au texte scellé et GO-2026-11-22-71, avec la mention « deux machines » ;
   - l'empreinte de l'ordre.
3. **Témoin** `reprise-engagee-iib-v5.json`, scellé et poussé avant le premier épisode.
4. **Jeu des seuls lots manquants** (le lot 28 : flagrants r24 à r31). Ils passent par l'ancien chemin `jouer` et `appliquer_oracles`, sous les clés du plan (`iib/etalonnage/flagrant/<tâche>`), en lots de 8. Chacun est versé comme un lot ordinaire, poussé par lot (correctif 0014).
5. **Clés de graines.** Les clés reconstruites des sorties du lot 28 doivent être égales aux clés employées par son jeu : c'est l'épreuve de la reconstruction sur la machine même. Si elles diffèrent, la reprise s'arrête ; le lot 28 reste scellé et versé. Les clés des lots 1 à 27 sont ensuite reconstruites de leurs sorties.
6. **Fin**, écrite par le même code que l'étalonnage complet : fichier des oracles (schéma strict inchangé), rapportés (avec une clé neuve `reprise`), graines.
7. **Résumés.** Le premier va sous le run de la reprise. Le second va sous le run coupé, rattaché à son manifeste, avec l'empreinte du manifeste de la reprise : c'est celui où la course compte ses 28 lots. Les deux portent la marque.

## 3. Durées et dépense : pas de repli silencieux
- Les lots versés ne contiennent aucune durée. Les durées de fin (`durees`, `duree_d_une_action_d_oracle_par_oracle_h`, `chrono`) sont donc mesurées **sur la machine neuve seule**, sur le seul lot 28 de flagrants. Elles ne valent pas pour la génération des honnêtes ni des régénérés, et la carte de la machine neuve peut être différente.
- C'est écrit dans `rapportes-etalonnage-iib-v5.json`, sous `reprise.durees`, qui commence par « MÉLANGE DÉCLARÉ » : les sorties viennent de deux machines, les durées d'une seule. C'est aussi écrit dans les deux résumés.
- Le plafond de tours des conditions de départ lit ces durées telles quelles (nœud 2).
- `depense_etalonnage_usd` vaut la dépense antérieure déclarée par l'ordre plus la dépense de la machine neuve. Le détail est sous `reprise.depense`.
- Le fichier des oracles garde son schéma strict, sans champ neuf : `branches_v5` refuse tout champ en plus. La déclaration est donc dans les rapportés et les résumés, pas dans ce fichier.
- Ce qui est exclu de la comparaison de l'essai central, ce sont ces seuls champs du chronomètre. Un essai témoin montre que deux étalonnages complets du même jouet diffèrent déjà sur ces champs et sont égaux sur tout le reste.

## 4. Constat fait pendant le développement
- Le tokeniseur jouet numérote chaque caractère la première fois qu'il le lit. Repris avec un modèle jouet neuf, le lot 28 avait donc d'autres identifiants que dans un étalonnage complet. La garde ne s'était pas déclenchée, et l'essai central l'a vu.
- L'essai central fixe maintenant le vocabulaire jouet d'avance, et vérifie qu'aucun caractère neuf n'est numéroté en cours de route.
- Un tokeniseur réel a un vocabulaire fixe. Le modèle réel garde pourtant un état qui persiste d'un lot à l'autre : les replis de la forme du lot des suites, de `cache_duplique` vers `prerempli_par_suite`, valent pour le reste du run. Ceux de la machine 61875617 ne sont pas dans les lots (réserve 2).

## 5. Gardes éprouvées (R5 : le cas sain est l'essai central)
Chaque artefact est essayé sur une copie de l'étalonnage jouet coupé :
- lot manquant au milieu ;
- lot en trop ;
- fichier inconnu ;
- identifiants manquants ;
- sceau faux, et ordre refusé sur un sceau faux ;
- fichier changé et rescellé après l'ordre ;
- ordre des tâches différent ;
- taille de lot différente ;
- sortie retirée d'un lot ;
- phase incomplète autre que la dernière (coupure après 20 lots) ;
- graines différentes (entropie, préfixe), refusées avant le témoin ;
- second passage, et témoin d'une reprise interrompue ;
- machine neuve égale à l'ancienne ;
- reconstruction des clés faussée (le lot 28 reste) ;
- formes de l'ordre : dépense négative, ligne de GO illisible, machine nulle ou booléenne, source qui n'est pas une branche d'essai, R12 ;
- ligne de GO absente du registre en mode réel, avec son cas sain ;
- par le point d'entrée : configuration différente de celle du manifeste scellé, second passage, argument hors de sa phase ;
- amorce : engagement unique (référence absente puis poussée ; présente : refus) ;
- préparation : commit qui n'est pas la tête de la branche, fichier inattendu du run dans le commit source.

## 6. Amorce : le chemin de la reprise sur une machine neuve
1. **La session, sur son poste :**
   - sur un clone propre de la branche de code (prep/…) qui porte ce correctif, lancer `bash scripts/preparer_reprise_iib_v5.sh 20261121-234254-iib-reel essai/iib-explo-v6 f4bf68bb7f5ffc4a30d07a4fc949ab02832e904b 61875617 <USD> GO-2026-11-22-71` ;
   - relire ce qui a été récupéré (les noms seulement), committer, pousser la branche de code.
2. **Le lanceur de session v3**, sur la ligne de GO de la configuration scellée (GO-2026-11-21-70 : `go_id` doit lui rester égal) :
   - `IIB_AMORCE=scripts/amorce_instance_iib_reprise_v5.sh` ;
   - `IIB_BRANCHE=essai/iib-explo-v7` (branche neuve) ;
   - `IIB_DEPENSE_ANTERIEURE_USD=<dépense de la machine 61875617>` ;
   - `IIB_TESTS_ATTENDUS=311`.
3. **L'amorce, sur la machine :**
   - clonage réduit, qui porte les lots ;
   - ordre unique ;
   - engagement distant ;
   - poussée initiale ;
   - 311 essais ;
   - lanceur en phase de reprise : témoin poussé, lot 28 poussé, fin ;
   - consignation de `diag/<run coupé>/` ;
   - poussée.
4. **Destruction :** inchangée par rapport à l'amorce de la course. Fin normale : état « stopped » seulement après une poussée réussie, disque gardé. Poussée impossible : disque gardé.
5. **Ensuite :** les conditions de départ se jouent sur processeur, avec `--run-id 20261121-234254-iib-reel`.

## 7. Nœuds pour Lazar
1. **Montant de la dépense antérieure** à écrire dans l'ordre et dans `IIB_DEPENSE_ANTERIEURE_USD` : celui du registre des dépenses, à donner par la session. Je ne l'ai pas lu.
2. **Durées du plafond de tours**, prises sur le seul lot 28 de la machine neuve. Option : la session les dérive des heures des marques de progrès dans le journal de l'instance coupée, que je n'ai pas lu. Cela demanderait un texte à part.
3. **Coupure de la surveillance pendant la reprise** : même seuil de 16 USD, compté sur la machine neuve seule. La coupure de la ligne de GO reste.
4. **Le témoin bloque toute seconde reprise**, même après une reprise interrompue : il faudrait alors un nouveau mot de Lazar et un nouveau correctif.
5. **Réserve « deux machines ».** Le lot 28 est un tirage valide sous les mêmes graines, mais rien ne garantit qu'il soit à l'octet celui que la machine 61875617 aurait tiré : autre carte, déterminisme numérique non garanti, état des replis inconnu.
6. **Les deux résumés** : celui du run coupé est rattaché au manifeste d'origine, que je n'ai pas réécrit. C'est un choix nécessaire, parce que la course compte ses lots à cet endroit.

## 8. Réserves
- Pièce non contre-lue (classe B) : contre-lecture par un autre modèle à faire, puis vérification des corrections.
- Rien n'a été joué sur une carte ni avec torch. L'amorce n'a été éprouvée que par fonctions extraites (engagement, choix par le lanceur de session, phase lue), et non par une répétition locale complète.
- Le code de jeu (génération, oracles, plantés, régénérés) est inchangé entre le commit de lancement `43d6d0673` et `997bed6a1` : `git diff --stat` ne touche que le lanceur, la désignation, la session et le versement. Le lot 28 est donc joué par le même chemin de tirage que les lots 1 à 27.
- Aucune sortie réelle n'a été ouverte. Les lots de la branche `essai/iib-explo-v6` n'ont été que listés par leurs noms. La configuration scellée a été lue pour vérifier le calendrier : création possible jusqu'au 26 novembre, ligne GO-2026-11-21-70, plafond de 55 USD.
