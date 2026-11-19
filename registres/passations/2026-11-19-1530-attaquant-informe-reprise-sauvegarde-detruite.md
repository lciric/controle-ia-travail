# Passation — attaquant informé : rôle repris, sauvegarde inventoriée puis détruite (2026-11-19)

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Cette session est sur un autre
compte que la mère en exercice (`session_013QMayjsoZJFBUCqcnvD5h1`) : les messages ne passent pas, et la continuité passe
par les fichiers du dépôt. La section « Lignes proposées à la mère », en fin de fichier, est faite pour qu'elle les inscrive.

## Mots de Lazar (vers 15:00Z, à cette session)
- « GO sur le verdict » : c'est le même GO que GO-2026-11-19-51, déjà inscrit par la mère (12:38:35Z). Le verdict retenu
  pour l'étape 1 du témoin de Bailey est « effet reproduit sur le banc des auteurs, au régime publié », avec ses réserves.
- « sauvegarde en (a) » : instantané protégé du serveur de sauvegarde, inventaire par un script vérifié, puis
  destruction.
- « Reprends le rôle de l'attaquant informé », avec la routine de reprise sur `main` et la lecture de la passation de
  relève `registres/passations/2026-11-19-1505-attaquant-informe-releve-nouveau-compte.md` (`8f141cad…`, branche
  `claude/festive-cannon-5ys0mz`) et des pièces qu'elle cite.

## Fait
- **Routine de reprise sur `main`** (`def57616`, dans un arbre de travail détaché hors du dépôt) :
  - empreintes de lancement « OK » ;
  - `verifier-arbre` : 100 problèmes, tous de forme, sur des notes d'autres sessions (99 compagnons absents, 1 compagnon
    dont le nom porte le chemin) ; aucune empreinte différente ;
  - `registres/etat.md` non lu (cloison du rôle) ;
  - défauts échus : aucun de ce rôle ;
  - machines : Vast illisible depuis ce compte (« Invalid user key », aucune clé Vast sur cet environnement ; relevé de
    la passation de relève à 15:03Z : aucune instance de ce rôle). Hetzner : seule la sauvegarde 176187199, allumée ;
  - tests : suite complète de `main` (environ 14 000 tests) arrêtée par son PID vers 5 %, sans échec ni erreur ;
    `test_scellement`, `test_manifeste`, `test_prereg` et `test_sondes_temoins` : 68 réussis. Pour la collecte, cinq
    dépendances figées que `main` a ajoutées ont été installées dans `.venv` sans résolution (`--no-deps`) :
    scikit-learn 1.9.1, joblib 1.6.0, threadpoolctl 3.8.0, narwhals 2.28.0, cloudpickle 3.1.3 ; `pip check` propre.
- **Pièces lues** :
  - `CLAUDE.md` de `main`, dont « Récupérer ce qui est récupérable » ;
  - `docs/procedures/brief-session-attaquant-informe-v1.md` (`55108eb8…`) ;
  - `docs/procedures/orientation-sessions-v1.md` (`ecec0cbf…`) ;
  - passation 1208 de `claude/festive-cannon-5ys0mz` (`b8d19892…`) ;
  - la note du GO sur cette branche (`99d963df…`).
- **Sauvegarde des sondes et paramètres du run à 36 tours** (serveur 176187199, créé le 15 novembre) :
  - arrêt propre à 15:11:17Z ; instantané 458341216 pris et protégé à 15:12:16Z (5,67 Go) ;
  - table `runs/temoin-bailey-v1-20261111/instantanes-postes-v2.json` (`2e4b56de…`) et fiche de création reconstituée
    depuis l'interface de Hetzner, `sauvegarde-v2-creation.json` (`7d3e31c3…`), scellées ;
  - inventaire v5 (genre « poste » ou « sauvegarde »), contre-lu par un autre modèle (Fable). Constat bloquant : la
    sauvegarde avait effacé ses clés (`shred -u`) en fin de boucle ;
  - inventaire v6 : clés lues dans les données de démarrage de l'ancienne instance. Vérification des corrections par le
    même contre-lecteur : « conforme, avec réserves ». Rapport versé :
    `runs/temoin-bailey-v1-20261111/contre-lecture-inventaire-instantane-v5-v1.md` (`40e710de…`). Script v6 `26653fa0…`,
    constructeur v6 `c87c57f5…` ;
  - serveur d'inventaire 176825843, créé à 15:24:41Z au lieu `nbg1` ; marque
    `poste-fini-inventaire-instantane-sauvegarde-v2-v6.json` à 15:25:45Z, commit `7dfda0cf`, source des clés « données
    de démarrage » ;
  - vérifié : champs, index, compagnons, comptes (inventaire 57 799 lignes = total − non réguliers ; index 19 348 =
    19 346 fichiers + 2 anomalies d'extinction, `btmp` et horloge de timesync) ; dépôt cloné à jour, sans commit non
    poussé ;
  - **les 74 fichiers sauvegardés ont, dans l'instantané, l'empreinte de l'instance et du serveur portée par la
    dernière liste poussée (`sauvegarde-sondes-v2/liste-passage-09.tsv`) ; aucun manquant, aucun de trop.**
  - Détruits par identifiant, avec 404 relu : 176825843 à 15:28:28Z, puis 176187199 à 15:28:41Z.
  - Plus aucun serveur Hetzner. Quatre instantanés protégés : 458234516, 458234528, 458234531, 458341216.
  - Registre des arrêts complété.
- Réserve N4 de la contre-lecture, levée par les faits : `user-data.txt` était présent, et la clé de déploiement
  `diag-temoin-bailey-depot-20261115` poussait encore à 15:27:46Z.

## Réserves
- Garde des secrets : deux commits portent une ligne relevée, le motif de détection des clés privées du module de
  contrôle (déjà en v4) ; c'est un faux positif.
- Rappel de l'incident de cloison de 12:06-12:08Z : un calcul d'empreintes locales n'excluait pas le coffre. Rien n'a été
  affiché ; il est consigné dans la passation 1226 et dans le registre des arrêts.
- La clé de déploiement `diag-temoin-bailey-depot-20261115` donne toujours l'écriture sur le dépôt. Aucune machine n'en a
  plus besoin : elle est révocable dès le mot de Lazar.

## Reste (nœuds de Lazar)
- Suite du bras d'attaque : lecture des réserves du verdict de Bailey (après le GO, plus sous cloison), ou pièce 4
  (courriel v4 non envoyable).
- Effacement des quatre instantanés protégés ; révocation de la clé de déploiement, de la clé ssh Vast 1864483 et du
  jeton GitHub ; révocation de la clé restreinte de 61170458 (console Vast).
- Purge de l'historique de la branche (commit `2a1c0ff9`). D'ici là : aucune fusion vers `main`, aucune copie publique.

## Machines actives (15:31Z)
Aucune pour ce rôle. Hetzner : aucun serveur. Vast : non lisible d'ici.

## Prochaine action
Attendre le mot de Lazar sur la suite du bras d'attaque.

## Lignes proposées à la mère (à inscrire par elle ; 600 signes au plus chacune)
1. Registre des GO : « Lazar, 19 novembre vers 15:00Z, à la session attaquant informé (autre compte) : sauvegarde du
   témoin de Bailey en (a). Instantané protégé 458341216, inventaire par instantané v6 contre-lu, destruction de
   176187199. Dépense : un serveur cx23 pendant 4 minutes et le stockage d'un instantané de 5,67 Go. »
2. Registre des arrêts : les lignes de 12:09Z à 12:25Z et de 15:11Z à 15:29Z du registre de
   `claude/compassionate-meitner-d4ryyk`.
3. Décisions, routine : inventaire v6 employé après la contre-lecture par un autre modèle (conforme avec réserves) ;
   cinq dépendances figées de `main` installées dans l'environnement de la session ; faux positif de la garde des
   secrets.
4. Erreur déclarée (orientation, § 6) : calcul d'empreintes locales sans exclusion du coffre, 12:06-12:08Z. Portée : des
   octets de fichiers du coffre ont pu être lus pour une empreinte ; rien d'affiché ; arrêté par son identifiant.
5. Pour la mère : `verifier-arbre` sur `main` (`def57616`) relève 100 problèmes de forme. Ils portent sur
   `docs/notes/organisme-courbe-dose-reponse-v1` (45), `docs/notes/g0-deux-semaines-v1` (41),
   `docs/notes/organisme-multi-generations-v1` (5) et quelques autres.
