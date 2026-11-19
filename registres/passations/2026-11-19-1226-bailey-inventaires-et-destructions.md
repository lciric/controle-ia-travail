# Passation — témoin de Bailey : inventaires par instantané faits, postes détruits (2026-11-19)

## Fait
- **Inventaire par instantané v4**, un poste à la fois (décision de routine de 11:50Z), sous le mot de Lazar « avant
  toute destruction, inventaire et versement scellé ». Les trois marques ont été vérifiées : champs égaux à la table
  scellée `instantanes-postes-v1.json` et au constructeur (empreinte du script rempli), index égal à l'empreinte de
  `empreintes-disque.txt`, compagnons « OK », comptes cohérents, aucun commit non poussé.

  | Poste (instantané) | Serveur d'inventaire | Marque, fini | Commit | Dépôt du poste |
  |---|---|---|---|---|
  | v14, 176575468 (458234516) | 176795924 | `poste-fini-inventaire-instantane-poste-v14-v4.json`, 11:44:11Z | — | tête `b3326f23` ; seuls `.venv/` et `__pycache__` ignorés |
  | inventaire v1, 176778587 (458234528) | 176800220 | `poste-fini-inventaire-instantane-poste-inventaire-instance-v1-v4.json`, 12:13:30Z | `c04d6a35` | tête `2a1c0ff9` ; 567 fichiers ignorés sous `versement-instance-61170458-v1/fichiers/` |
  | inventaire v2, 176780521 (458234531) | 176801311 | `poste-fini-inventaire-instantane-poste-inventaire-instance-v2-v4.json`, 12:21:10Z | `351a6d16` | tête `ae9447ef` ; rien d'ignoré |

  - Hors du dépôt, pour chaque poste : fichiers décrits et empreintés (pas de contenu versé), contenus gardés dans
    l'instantané protégé. Cela comprend `/root/passe` (v1 : 562 fichiers ; v2 : 22) et `/root/versement-local` (v2 :
    738 fichiers).
  - Un seul journal par poste a été versé, chacun avec « 0 valeur exacte remplacée ».
  - **Écart d'une ligne au v1** : l'index compte 20932 lignes pour 20931 fichiers « poste ». La ligne en plus est un
    journal système sous `/var/log/`, touché par le serveur d'inventaire et empreinté selon la règle du script. C'est
    expliqué, sans effet.
- **Destructions par identifiant** (R10), chaque fois avec action « success » puis HTTP 404 relu :
  - 176795924 et 176575468 à 12:09Z ;
  - 176800220 et 176778587 à 12:17-12:18Z ;
  - 176801311 et 176780521 à 12:24-12:25Z.
- **Registre des arrêts** (`registres/arrets.md`) complété aussi pour trois gestes qui n'y figuraient pas :
  - l'arrêt du poste d'inventaire v1 (09:48:43Z) ;
  - la destruction de l'instance Vast 61170458 (10:09:26Z, par la conduite) ;
  - l'arrêt propre du v14 et de l'inventaire v2 (10:26:01Z).
- Seconde tentative de relais vers la session mère `session_013QMayjsoZJFBUCqcnvD5h1` : « not found ». La demande de
  GO est faite à Lazar directement.

## Incident (cloison)
- Vers 12:06-12:08Z, pour vérifier le versement du v14, la session a lancé un calcul local d'empreintes : il
  comparait les chemins de l'index du poste aux fichiers de la copie locale du dépôt.
- Ce calcul **n'excluait pas le coffre**. Il a donc pu lire des octets de fichiers de `donnees/bras-attaque*` ou
  d'autres chemins cloisonnés présents dans la copie locale (deux de ces chemins y existent), pour en calculer
  l'empreinte.
- Il a été arrêté par son identifiant de tâche (b217kxzhr) avant toute sortie. Seule sortie : trois lignes d'empreintes
  de `donnees/T0.7-models-under-pressure-v1/`, hors coffre. Aucun contenu, aucun nom ni aucune empreinte de chemin
  cloisonné n'a été affiché.
- Mesure : la vérification s'est faite ensuite par l'état de git et des comptes seulement. Tout affichage tiré d'un
  index de poste filtre d'abord les chemins cloisonnés. Aucun calcul local sur les fichiers du dépôt n'a été relancé.

## Reste (nœuds pour Lazar)
- GO sur le verdict retenu pour l'étape 1 (R13) : `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-verdicts-temoin-bailey-v1.md`
  (`75db4cbd…`).
- Sort du serveur de sauvegarde 176187199 (allumé, sans usage pour le témoin) :
  - (a) instantané protégé, inventaire par un script v5 vérifié, puis destruction ;
  - (b) le garder.
  - Recommandation (a) ; défaut sous 48 heures (b).
- Effacement des trois instantanés (protégés), purge de l'historique de la branche (clé au commit `2a1c0ff9`),
  révocation des clés et du jeton.

## Instances actives (12:25Z)
- Hetzner : 176187199 (sauvegarde, allumé). Instantanés 458234516, 458234528 et 458234531, protégés.
- Vast : aucune instance de cette session.

## Prochaine action
Attendre le GO et les mots de Lazar. Plus rien à faire sur les machines sans son mot.
