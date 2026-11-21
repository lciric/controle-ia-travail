# Passation — session « attaquant informé », remise en fille à la nouvelle mère (21 novembre 2026, 15:45 UTC)

- Session sortante : `session_01QPDgKiPN5vEiEdmAYKZt3W`, branche `claude/loving-lamport-7ol5ws`.
- Demandée par la nouvelle mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`, autre compte), message
  `registres/essaim/vers-attaquant-informe/2026-11-21-1533-mere.md` sur `main` (`3a859e3e…`, empreinte vérifiée).
- Brief de lancement de la fille : `docs/procedures/brief-lancement-attaquant-informe-fille-2026-11-21-v1.md`.
- Ne se réécrit pas (R12).

## Pièces de cette session, sur `claude/loving-lamport-7ol5ws`

| pièce | empreinte |
|---|---|
| relais des directives du 20 nov. (`registres/passations/2026-11-20-0953-…-relais-directives-lazar-vers-mere.md`) | `ae7c6f5e…` |
| passation intermédiaire du 20 nov. (`…/2026-11-20-1255-attaquant-informe-reprise-nouveau-compte.md`) | `098af9ac…` |
| passation de fin d'autonomie (`…/2026-11-21-0102-attaquant-informe-fin-autonomie.md`) | `bc1e7fe5…` |
| son erratum 1 (`…/2026-11-21-0105-…-erratum-1.md`) | `7908b769…` |
| mot « go a » : pièces du bras hors de `main` (`…/2026-11-21-0112-…-pieces-bras-hors-main.md`) | `cd2cbfa6…` |
| autonomie du 21 nov. et relais refusé (`…/2026-11-21-1030-….md`) | `092607df…` |
| message à la mère par le canal (`registres/essaim/vers-mere/2026-11-21-1400-attaquant-informe-vers-mere.md`) | voir son `.sha256` |
| papier « dopamine » (`docs/sources/pdf/2602.00986v2.pdf`) | `da004f53…` |
| mandat et consultation de Fable (`docs/notes/papier-dopamine-moniteur-v1/`) | consultation `afc22a5f…` |
| pièces de l'attaquant recopiées depuis `claude/compassionate-meitner-d4ryyk` (préenregistrement du bras d'attaque et ses addenda 1 et 2, témoin de Bailey et ses addenda 1 à 8, trois briefs sous `docs/procedures/`) | `88418df0…` (préenregistrement) ; compagnons vérifiés |

Les deux fichiers du protocole d'essaim v1 à la racine de `registres/essaim/` sont sans objet : la mère les laisse en
place.

## État du bras d'attaque

- Scellement 1, la règle : fait. `prereg/bras-attaque-regle-v1.md` (`88418df0…`), trois contre-lectures,
  deux addenda, empreinte déposée chez le tiers (R-4125).
- Scellement 2, les familles aveugles : **pas fait**.
- Scellement 3, les moniteurs gelés : **pas fait**.
- Revue de sécurité externe du bras (R-611, N-057) : ouverte.
- Aucune sortie du bras tant que les trois scellements ne sont pas faits.
- Mot de Lazar « go a » (21 nov., vers 01:10Z) : les pièces du bras restent sur les branches de l'attaquant,
  jamais sur `main`.

## Rôle dans la course « nouvelles attaques »

**Aucun**, tant que Lazar ou la mère ne lui en donnent pas. Les rôles sont attribués à d'autres (GO-2026-11-20-57 et
-65) : la session à part en Fable 5.2, les deux lecteurs d'antériorité, le concepteur du mode tenu à l'écart.

## Nœuds pendants au mot de Lazar

- effacement des quatre instantanés ;
- révocation de clés : clé de déploiement, clé SSH Vast 1864483, jeton GitHub, clé restreinte 61170458, clé Vast
  collée ;
- purge de l'historique (commit `2a1c0ff9`) ;
- pièce 4 (courriel v4).

## Ce que la mère ne doit pas lire

- Le contenu des pièces du bras d'attaque :
  - `prereg/bras-attaque-regle-v1*.md` ;
  - `prereg/temoin-attaque-publiee-bailey-v1*.md` ;
  - les briefs de l'attaquant sous `docs/procedures/`.
  Les noms et les empreintes suffisent.
- Le coffre : `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`.
- Toute sortie de la course « nouvelles attaques » en quarantaine (GO-2026-11-20-50 et -57).
- La consultation de Fable sur le papier « dopamine » lui revient, à elle : c'est un sujet de moniteurs que
  l'attaquant ne lit pas.

## Ce qui tourne

- Aucune instance de calcul. Aucune dépense de cette session depuis la reprise.
- Aucun sous-agent actif. Aucun test en cours.
- Les deux rappels programmés de cette session (17:00Z et 22:00Z) sont supprimés à la clôture.
- Le rappel daté R-4161 (samedi 21 novembre vers 18 h, heure de Paris) passe à la nouvelle mère.
- Deux tâches programmées restent sur ce compte. Elles appartiennent à l'ancienne mère, pas à cette session :
  - `trig_015gT3hX5xWDUzeCCJWHM2bJ`, à 16:55Z ;
  - `trig_01RTShAGQfNdUA25pdJydG1R`, les 21 et du 24 au 30 novembre vers 17:52 (heure de Paris).
  Les deux tirent dans `session_01QPDgKgejkqwnuaJHJ31Ydo`, l'ancienne mère. À reporter ou à supprimer sur le mot de
  Lazar ; cette session n'y touche pas.

## Réserves

- Depuis ce compte, la voie directe vers la mère et vers l'organisme d'idéation était refusée (appareil de
  confiance). Le canal par dossier de destinataire a été accordé par Lazar (« go les deux »).
- Aucune clé Anthropic dans l'environnement de cette session.
- Tests de `main` au 20 novembre : 196 échecs, dont 178 tests datés de T0.6 (GO figé expiré le 16 novembre) et 18
  liés à l'historique réduit ou à un module absent.

## Prochaine action

La fille reprend avec le brief de lancement, sur le compte de la nouvelle mère. Elle attend sa relance et ne lance
rien.
