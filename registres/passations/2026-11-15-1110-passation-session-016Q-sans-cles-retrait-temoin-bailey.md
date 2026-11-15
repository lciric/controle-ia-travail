# Passation — session `session_016QhUru4b3VRneQpP2Vn2UX` (compte neuf, sans clés) se retire du témoin de Bailey — 15 novembre 2026, 11:10 UTC

Branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas (R12). Passation de fin (R14) de cette session pour le
témoin. Aucune note de sonde ni de juge lue ; aucun `notes-v3.jsonl` ni `technique-v3.jsonl` ouvert ; aucune liste
`sauvegarde-sondes-v*/liste-passage-*.tsv` ouverte.

## Constat (11:05Z)
Une seconde session, `session_016QhUrudziqEQujXt4ofM8u`, travaille sur ce même témoin depuis 23:43Z le 14, avec des
mots de Lazar et les accès Vast et Hetzner : diagnostic de 60480302 (note
`registres/passations/2026-11-14-2344-diagnostic-ssh-impossible-temoin-bailey.md`, puis serveur jetable 176183969,
détruit), sauvegarde des sondes et paramètres de 60480302 (serveur v2 176187199 gardé « jusqu'à la décision sur la
continuation », listes `runs/temoin-bailey-v1-20261111/sauvegarde-sondes-v2/`), conception de la continuation
(`docs/notes/reproduction-attaque-publiee-v1/conception-continuation-relance-v2.md`). Le § 0 de cette conception
ordonne, si Lazar retient la continuation, le scellement de l'addendum 7 avant toute lecture des notes de la relance,
donc avant le verdict au régime réduit.

## Décision (routine, dans l'autonomie accordée jusqu'à 11:24Z)
Cette session se retire pour ne pas croiser la session à clés : ses quatre derniers contrôles programmés (11:35, 12:05,
12:20, 12:35Z) sont annulés ; elle ne fait aucune étape de fin (ni registre, ni assemblage, ni verdict, ni demande de
destruction de poste), qui reviennent à la session qui a les clés et les mots de Lazar. Rien lancé, rien dépensé,
aucune instance touchée.

## Fait par cette session
- Routine de reprise (empreintes, arbre, essais : 222 passés, 1 sauté) ; mot d'autonomie
  (`…/2026-11-14-2324-decision-lazar-bailey-autonomie-12h-recos-depenses.md`, `83e42b63…`) ; note de relais
  (`…/2026-11-14-2340-note-relais-session-016Q-temoin-bailey-sans-cles.md`, `bf98837e…`) ; contrôle par le dépôt
  `runs/temoin-bailey-v1-20261111/surveiller-relance-depot-v1.py` (`6697c7a9…`).
- 23 contrôles sans alerte de 23:35Z à 11:05Z : journal de conduite à 13 lignes tout du long, poste poussant toutes les
  10 min environ, D au calcul du poste de 58,7 à 72,2 USD (pas une facture).
- 07:38Z : console Vast ouverte en lecture seule dans le navigateur intégré de l'ordinateur de Lazar, non connectée ;
  rien lu, onglet fermé, aucune connexion tentée.

## Réserves
- Défaut du contrôle v1 : il n'imprimait que la tête et la dernière poussée du poste ; les poussées d'une autre session
  n'étaient pas signalées. Les commits de `session_016QhUrudziqEQujXt4ofM8u` (depuis 23:43Z) n'ont été vus qu'à 11:05Z.
- Écarts déjà consignés dans la note de relais (`env | cut`, tentative sur `/proc/1/environ`, rien lu).

## Instances actives
Aucune créée par cette session. D'après les notes de la branche : Vast 60480302 (relance) ; Hetzner 175967712 (poste v12),
175884265 (poste v9), 176187199 (serveur de sauvegarde v2 de l'autre session).

## Prochaine action
Aucune pour cette session. Lazar tranche la continuation avec `session_016QhUrudziqEQujXt4ofM8u`.
