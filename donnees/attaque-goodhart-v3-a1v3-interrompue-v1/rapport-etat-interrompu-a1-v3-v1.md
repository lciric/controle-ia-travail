# Rapport de la session fille — A1-v3 interrompue (GO-2026-11-02-21) — v1

Écrit le 3 novembre 2026 à 07:25 UTC (heure relevée par `date -u`), sur le mot (a) de session-depot (message de 07:22:40 UTC).
Aucun fichier de la sortie n'a été lu ; ce rapport n'en donne que les noms. Rien n'a été relancé.

## Heures (toutes UTC, `date -u` ou horodatages des journaux)
- Départ de la course : 06:17:41 (PID 1251), après `--verifier-seulement` en code 0 (06:17:19) ; relais Argon 8805 PID 1011 (06:16:55) ; guetteur PID 1405 (06:18:23).
- Dernière trace du guetteur : 06:23:29 (passage suivant attendu 06:28:29, jamais écrit).
- Dernier appel au relais : n° 41, statut ECHEC, 06:25:32, durée 158,7 s, coût compté au pire cas ; échec « connexion : RemoteDisconnected ». Appels 1 à 40 : OK, fin STOP.
- Redémarrage du conteneur constaté : 07:18:50 (démarrage du processus 1 ; uptime 22 s à 07:19:07), à la relève horaire de 07:18:51.

## Dépense
41 appels ; 4,245753 USD au compte du relais (`depense_cumulee_usd` de la dernière ligne du journal du relais), dont 1,614193 USD au pire cas pour l'appel 41. Le registre de dépense cumulée de la sortie n'a pas été lu.

## Contenu de la sortie (noms seulement)
`sortie-attaque-goodhart-v3/` : `manifeste.json`, `manifeste.json.sha256` (écrit par le lanceur), `registre-depense-cumulee-v1.jsonl`,
`registre-depense-cumulee-v1.jsonl.verrou` (vide). Aucun fichier de résultat (`attaque-goodhart-v3.json` absent).

## Cause probable
Conteneur de la session fille repris après inactivité de la session (dernier tour vers 06:20 UTC) : les processus détachés ne
gardent pas le conteneur en vie, et la relève horaire (tâche planifiée `trig_013F3mbLSqdo5zMEY6dgDHD3`, minute 18, désactivée
depuis) était trop espacée. Cause d'infrastructure ; ni l'interface ni la clé.

## Scellement
- Chaque fichier de `/home/user/hors-clone-a1-v3` a reçu un compagnon `.sha256` (07:25 UTC).
- Liste `EMPREINTES-etat-interrompu-a1-v3-v1.txt` (`04cf5d1b8661075d0b93743cfa97f38816d1ad7f89f29d84b9c91680cd428d66`), scellée telle
  quelle. **Écart** : elle a été calculée à 07:19 UTC ; j'ai ensuite ajouté au journal de lancement une ligne (07:20:01, « alerte
  envoyée ») : la liste donne pour ce journal `778fab67…`, son compagnon donne l'état actuel `16eab4af…`. Les 17 autres
  entrées tiennent.
- Le code de sortie de la course n'est pas connu ici (processus détaché, mort avec le conteneur) ; l'issue se lira dans le manifeste
  scellé par l'auditeur.

## Règle neuve (session-depot, 07:22:40 UTC)
Pour toute course chez la fille : la session reste active pendant toute la course, par une attente en arrière-plan suivie par le
harnais (commande qui attend la fin du processus, réarmée avant son délai), jamais par une seule relève horaire.
