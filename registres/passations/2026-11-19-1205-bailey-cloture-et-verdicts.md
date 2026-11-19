# Passation — témoin de Bailey : clôture faite, deux verdicts scellés, rapport soumis à Lazar (2026-11-19)

## Fait
- Clôture selon l'addendum 7, § 3 (`554a74d0…7f3e`), à partir du gabarit de commandes v4 rempli
  (`runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/commandes-cloture-bailey-v4-rempli.sh`, `9fc3adae…`).
  Chaque étape est horodatée dans `journal-cloture-v1.txt`.
- Note de clôture : `note-cloture-confirmation-bailey-v1.md`, `d47b32d53816190f480b6f832fff76c5e3daf452152b489fb015903189aa901b`.
- Lectures à l'aveugle, toutes deux « aboutie » :
  - a : `sortie-a-v1.json`, `9d4098eb11faa8a09853218d097827e929fc92b10b48caae1164206e21568a6e` ;
  - b : `sortie-b-v1.json`, `0ce212425c6ddec3281e4e0f3efd968800461b0ca012e65b056979c00a925b82`.
- Lecteurs neufs lancés ensemble à 11:53:15Z. Ils ont rendu à 11:58:00Z (b) et 11:58:32Z (a) :
  - a : `rapport-lecteur-a-v1.md`, `f5d9baedacd1df3fbd796a7c0c23695f579fd2a46da837233ffe97599ab92f5c` ;
  - b : `rapport-lecteur-b-v1.md`, `ca7e6751e13527bcb70d66987939e7d5e5c9af47ddc827123fda35591c57990d`.
- Contrôle final à 11:58:41Z : e7, puis e8, « conforme » pour a et pour b. Tête après poussée : `2848088c`.
- Ouverture des sorties et des rapports après 11:58:42Z. Chaque rapport transcrit fidèlement sa sortie : R13 est
  tenu pour les deux.
- Rapport des deux verdicts, scellé à 12:04:41Z :
  `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-verdicts-temoin-bailey-v1.md`,
  `75db4cbd2adfeb30358ca9fe23f8128a6ff31eb66145276c6c482b25546545b7`, commit `6d8e2801`, poussé (tête distante vérifiée).
- Verdict retenu pour l'étape 1 : celui de la confirmation, K′ = 72, au régime publié. « Effet reproduit sur le banc
  des auteurs, au régime publié. Réserves : longueur de suffixe différente des 16 jetons de l'article (écart 10). »
  Le verdict à 36 tours (K′ = 36, régime réduit) est rapporté à côté ; il concorde.
- Information de la dernière puce du § 3 : les graines sont identiques, et pourtant le premier tour où les empreintes
  de suffixe (écart 9) diffèrent est le tour 0. Les empreintes de sonde sont égales au tour 0 et diffèrent à partir
  du tour 1.

## Erratum
- Le rapport des verdicts dit « vers 12:10 UTC ». L'heure relevée de son scellement est 12:04:41Z. Le rapport n'est
  pas réécrit (R12).

## Reste
- **Nœud pour Lazar** : GO sur le verdict retenu pour l'étape 1 (R13).
- La session mère `session_013QMayjsoZJFBUCqcnvD5h1` était injoignable à la dernière tentative. La demande est donc
  faite à Lazar directement, qui a commandé la clôture.
- Inventaire par instantané v4, un poste à la fois (décision de 11:50Z) :
  - vérification du versement du v14 (marque reçue de 176795924), puis destructions par identifiant ;
  - ensuite l'inventaire v1 (instantané 458234528), puis l'inventaire v2 (instantané 458234531).
- **Nœuds pour Lazar, inchangés** :
  - purge de l'historique de la branche (clé de l'instance au commit `2a1c0ff9`) ;
  - révocation des clés et du jeton ;
  - effacement des instantanés ;
  - sort du serveur de sauvegarde 176187199, gardé jusqu'à la clôture et maintenant sans usage pour le témoin.

## Instances actives (12:05Z)
- Hetzner :
  - 176187199 (sauvegarde, allumé) ;
  - 176795924 (inventaire par instantané du v14, allumé) ;
  - 176575468, 176778587 et 176780521 (éteints).
  - Instantanés 458234516, 458234528 et 458234531, protégés.
- Vast : aucune instance de cette session (61170458 détruite à 10:09:26Z).

## Prochaine action
Vérifier le versement du v14, puis détruire 176795924 et 176575468 par identifiant, avec preuve d'absence, et les
consigner dans `registres/arrets.md`.
