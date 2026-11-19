# Passation — attaquant informé, surveillance de la relance de Bailey close (2026-11-19, 12:08Z)

Session `session_013QMaynSCWwud812phoDNwn`, branche `claude/festive-cannon-5ys0mz`. Mot de Lazar : « continue la
surveillance jusqu'à la clôture ». Rôle tenu en surveillance et compte rendu seulement (GO-2026-11-18-46 : la conduite et
le filet B′ restaient à `session_01XJ6MgnEhQMZteN9F8a1BST`). Aucun geste sur aucune machine, aucune dépense, aucune note
ni aucun résultat du témoin ouvert.

## Fait
- Surveillance en lecture seule (crédit Vast, état de 61170458, marque de fin, puis serveurs Hetzner et commits de la
  branche `claude/compassionate-meitner-d4ryyk`) du 18, 13:52Z, au 19, 12:07Z. Repli B′ jamais déclenché.
- Crédit : recharge manuelle de Lazar à 09:43Z (4,81 → 24,75 USD). La recharge automatique n'a pas été vue jouer
  (crédit sous 5 USD au moins 2 min sans recharge) : elle reste non éprouvée.
- Fin de la relance : `poste-fini-v14.json` au commit b3326f23c (10:09:59Z) ; `sortie-durees-v3.jsonl` à 72 lignes
  (72 tours sur K = 72, champ technique) ; 61170458 détruite (10:09:26Z selon l'ancienne session ; absente de l'API à
  10:11Z).
- Clôture suivie par noms et empreintes (dossier `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/` de la
  branche ci-dessus) : note de clôture (3cec03736, 11:52:38Z), sorties scellées du code, consignes des lecteurs,
  rapports des lecteurs b (596b45eb4) et a (4fe266f0d), rapport des deux verdicts
  `rapport-verdicts-temoin-bailey-v1.md` (`75db4cbd2adfeb30358ca9fe23f8128a6ff31eb66145276c6c482b25546545b7`,
  6d8e28018, 12:04:41Z), soumis à Lazar pour GO ; passation de l'ancienne session 2d3ebae95 (12:05:41Z).
- R-3661 (récupérer ce qui est récupérable) : journal de surveillance et scripts versés et scellés dans
  `diag/surveillance-credit-relance-bailey-attaquant-informe-v1/` (v1 au commit 6f947f7c ; v2 dans ce commit).
- Tout relevé et chaque étape portés à la mère (`session_013QMayjsoZJFBUCqcnvD5h1`).

## Réserves
- Joindre 61170458 m'était impossible (pas de SSH sortant dans ce conteneur ; l'API d'exécution de Vast refuse sur une
  instance en marche ; l'essai refusé est versé, `essai-commande-vast-refusee-v1.sh`). L'ancienne session est sur un autre
  compte : `send_message` rend « not found » (de la mère comme de moi).
- Clé restreinte de 61170458 dans l'historique de `claude/compassionate-meitner-d4ryyk` (commit 2a1c0ff9 ; note
  `registres/passations/2026-11-19-1005-incident-cle-instance-versee.md` de cette branche). Révocation non faite
  explicitement ; purge de l'historique = nœud de Lazar. D'ici là, aucune fusion vers `main`, aucune copie publique.
- Depuis R-3661, je ne détruis plus de poste en relève : je ne peux pas l'inventorier d'ici.

## Reste (à l'ancienne session, selon sa passation 2d3ebae95)
Vérifier le versement du v14, puis détruire par identifiant 176795924 et 176575468, ensuite les postes d'inventaire
176778587 et 176780521 après leurs instantanés ; effacer les instantanés ; sort de la sauvegarde 176187199.

## Instances et serveurs (12:07Z, lecture)
- Vast : aucune instance du témoin ; en marche 61414494 (« iib-explo-v1 », hors témoin) ; arrêtées intouchables
  58936096, 58936099, 58936100, 60988826. Crédit 22,27 USD.
- Hetzner : 176187199 et 176795924 allumés ; 176575468, 176778587, 176780521 éteints.

## Prochaine action
Rien de requis pour ce rôle. Si Lazar le demande : constater par lecture la destruction des postes Hetzner restants.
