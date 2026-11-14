# Passation — session « attaquant informé » (autre compte) → session neuve d'un autre compte — témoin de Bailey, relance en retard — 14 novembre 2026, 23:05 UTC

Session sortante `session_01XJ6Mgqg6DeUDvNm87LXApc`, branche `claude/compassionate-meitner-d4ryyk`, tête lue `69b82b8e`
(journaux du poste, 23:00Z). Mot de Lazar, verbatim : « fais la passation a une nouvelle instance sur un autre compte ».
Ne se réécrit pas (R12). Complète, sans la remplacer, la passation
`registres/passations/2026-11-14-0929-passation-attaquant-informe-temoin-bailey-relance-en-cours.md` et son brief
`…-0929-brief-lancement-session-neuve-temoin-bailey.md`, qui restent la référence pour la mission (étapes 0 à 6).
Aucune note de sonde ni de juge lue ; seuls les champs techniques de `conduite-v5.jsonl` et le battement ont été lus.

## Ce que cette session a fait
- 11 novembre : lancement impossible depuis ce compte (note `…-2320-…`, `1122d245…`) ; aucune dépense, aucune instance.
- 14 novembre, 23:00Z : reprise sur le mot « c'est fait » de Lazar. Constaté : `console.vast.ai` (302) et `huggingface.co`
  (200) joignables ; `cdn-lfs.huggingface.co` injoignable, `cas-bridge.xethub.hf.co` refusé (403) ; **`VAST_API_KEY` et
  `HF_TOKEN` toujours absentes de l'environnement de cette session** (noms seuls vérifiés ; les secrets ne sont
  vraisemblablement posés qu'au démarrage d'une session). Aucune commande Vast ni Hetzner passée.
- Lu entre-temps sur la branche : séries 3 et relance menées par `session_01XJ6MgnEhQMZteN9F8a1BST` (passation 09:29Z).
  Aucun commit autre que les journaux du poste depuis cette passation : **personne n'a surveillé la relance depuis
  09:32Z le 14**.

## État au 14 novembre, 23:01Z (lu dans le dépôt, sans Vast)
- `principal-relance` lancé le 13 novembre à 10:05:32Z (journal de conduite, 13 lignes, dernière « principal-relance
  lancée », inchangé depuis le commit du 13 à 10:08:52Z).
- Battement du veilleur d'arrêts (`sortie-conduite-v13/arrets-v5.jsonl.battement`, PID 7881) : 2026-11-14T23:00:04Z ;
  `arrets-v5.jsonl.err` vide. Le poste v12 pousse toujours toutes les 10 min.
- **Durée écoulée 36,9 h pour 26,3 h attendues** (K = 72 × t = 1 315,99 s) : **≈ 10,6 h de retard**, cause inconnue
  (tours plus lents, instance arrêtée par Vast faute de crédit, exécution bloquée : rien de cela n'est lisible sans Vast).
- Aucun des marqueurs de fin : `poste-fini-v12.json`, `bilan-lancement-v13.json`, `sortie-conduite-v13/bilan-conduite-v5.json`
  absents.
- Dépense : si l'instance 60480302 a tourné tout du long à 1,172 USD/h, D ≈ 14,77 + 36,9 × 1,172 ≈ **58 USD** (calcul de
  cette session, non relevé) ; B − 2 = 73 USD serait atteint vers **2026-11-15 11:45Z**, où le chien de garde arrête
  l'instance (lecture 37) ; le run serait alors lu comme tronqué après reprise.
- Instance 60599797 « rr-a3_e4 » (autre chantier, 8,23 USD/h, signalée à 09:27Z) : état inconnu ici ; elle tire sur la
  même carte que la recharge automatique.

## Reste (dans l'ordre ; détail : brief `…-0929-…`, étapes 0 à 6)
1. **D'urgence** : `vastai show instance 60480302 --raw` (état, `cur_state`, `actual_status`), `vastai show user --raw`
   (`credit`, `balance`, `billing_failed`), paiements récents ; inventaire. Dire à Lazar en trois lignes : instance en
   marche ou arrêtée, crédit, D relevé.
2. Selon le cas : run toujours en marche → surveiller jusqu'à la fin ou jusqu'à B − 2 ; instance arrêtée ou poste
   bloqué → reprise (lecture 38, étape 3 du brief `…-0929-…`), jamais de destruction avant un transfert qui fait foi.
3. Fin, assemblage, verdict par un lecteur neuf, passation : étapes 2, 4, 5, 6 du brief `…-0929-…`.

## Réserves
- Le retard n'est pas expliqué ; toute hypothèse ci-dessus est à vérifier sur Vast avant d'agir.
- `verifier-arbre` : les deux écarts antérieurs connus, non corrigés.
- `registres/etat.md` non lu ni mis à jour (cloison).

## Instances actives (d'après la passation de 09:29Z ; non revérifiées)
Vast 60480302 (relance) ; Hetzner 175967712 (poste v12, pilote la relance) et 175884265 (poste v9, sans tâche, gardé
sur consigne de Lazar). Aucune créée par cette session.

## Prochaine action
Session neuve : brief `registres/passations/2026-11-14-2305-brief-session-neuve-temoin-bailey-relance-en-retard.md`.
Cette session n'agit plus après cette passation.
