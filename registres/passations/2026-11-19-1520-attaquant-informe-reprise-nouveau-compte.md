# Reprise — attaquant informé, session neuve sur un autre compte (2026-11-19, 15:20Z)

Session `session_01XJ6Mgqg6DeUDvNm87LXApc`, branche `claude/festive-cannon-5ys0mz`. Reprise sur le mot de Lazar, selon la
passation de relève `registres/passations/2026-11-19-1505-attaquant-informe-releve-nouveau-compte.md` (`8f141cad…`,
empreinte vérifiée). Ne se réécrit pas (R12). Aucune note, aucun résultat ni aucune pièce du coffre ouverts ; rien
lancé, rien dépensé.

## Routine de reprise sur `main` (tête `def57616`)
- Empreintes de `docs/` : toutes bonnes.
- `verifier-arbre` : 100 écarts, aucun dans les dossiers du témoin ni du bras d'attaque. 99 empreintes compagnons
  absentes (45 sous `docs/notes/organisme-courbe-dose-reponse-v1/`, 41 sous `docs/notes/g0-deux-semaines-v1/`, le reste
  sous d'autres notes, deux sources et une course du collisionneur) ; 1 compagnon qui porte un chemin au lieu d'un nom
  (`docs/notes/organismes-discrets-v1/prereg-organismes-discrets-v1-brouillon6.md.sha256`). Consignés, non corrigés.
- `registres/etat.md` : seules les quinze premières lignes lues, comme le veut l'orientation des sessions.
- Lu : `CLAUDE.md` de `main` (dont « Récupérer ce qui est récupérable ») ; brief de rôle v1 et orientation des sessions
  v1 ; passations `2026-11-19-1208-…` (`b8d19892…`), `2026-11-19-1205-bailey-cloture-et-verdicts.md` (`98f558cd…`) et note
  `2026-11-19-1500-note-go-verdict-bailey.md` (`99d963df…`) : empreintes conformes.
- Inventaire des machines : **impossible d'ici**. Ni `VAST_API_KEY`, ni `HCLOUD_TOKEN`, ni `HF_TOKEN` dans
  l'environnement (noms seuls) ; Vast répond « Invalid user key » et Hetzner « token invalid » à l'en-tête du mandataire.
  Le relevé qui fait foi reste celui de 15:03Z (passation de relève) : aucune machine de ce rôle.
- Essais : la suite complète est trop longue pour ce conteneur (moins de 1 % en 7 min ; arrêtée par ses PID, 387 et 388).
  Les essais du témoin ne sont pas sur `main`. Passés : essais du scellement, de la garde de calcul et du manifeste,
  54 sur 55.

## Écart trouvé, pour la mère (le registre des GO est à elle)
`tests/test_garde_calcul.py::test_registre_reel_du_depot_accepte_le_go_de_calcul_de_la_phase_0` échoue sur `main` : la
ligne `GO-2026-11-19-30` (autonomie de douze heures de la relance du bras A) de `registres/go.md` porte
`2026-11-19T21:50:03Z` dans la colonne d'échéance. La garde de calcul (`.claude/hooks/garde_calcul.py`, l. 95) attend une
date seule (`date.fromisoformat`) et s'arrête en erreur (sortie 2) en lisant le registre. Conséquence probable, à
vérifier par la mère : toute commande de création d'instance payante est refusée par la garde tant que la ligne reste
ainsi. Correction proposée : la date `2026-11-19` dans la colonne, l'heure dans le texte de la ligne, par erratum.

## Nœuds ouverts (inchangés, à Lazar)
Purge de l'historique de `claude/compassionate-meitner-d4ryyk` (clé de l'instance 61170458 au commit `2a1c0ff9`) et
révocation de la clé ; pièce 4 du bras d'attaque (courriel v4 non envoyable) ; réglage de la recharge automatique ;
sort du serveur de sauvegarde Hetzner 176187199 et des instantanés protégés.

## Prochaine action
Attendre le mot de Lazar : lecture des réserves du verdict de Bailey, ou pièce 4 du bras d'attaque.

## Instances actives
Aucune créée par cette session.
