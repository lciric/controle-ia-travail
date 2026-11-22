# Vérification des corrections du transport Kimi réel v2 — v1

- Contre-lecteur de la v1, 22 novembre 2026. Aucun appel réel, aucune dépense. La fumée n'a été ni lancée ni répétée hors du faux serveur local, avec une clé factice. Rien n'est écrit dans le dépôt (`git status` vide). Aucun refus d'outil.
- Pièce : `docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v2/`. Les dix compagnons `.sha256` concordent.

## Verdict

**Conforme avec réserves.** B1 et B2 sont levés. Rien n'est bloquant pour la fumée.

## Contrôles

- **Épreuves : 112 réussies**, rejouées en 99 s (`rejeu-pytest-v2.txt`).
- **Outil d'attaque rejoué.** Je l'ai comparé au mien par `diff`.
  - Le chemin et les modules sont ceux de la v2.
  - La construction de l'adaptateur est placée dans le `try`. Chaque issue reste précise : aucune attaque n'est refusée en bloc à la construction.
  - N13 est **renforcée** : l'affectation directe, puis `object.__setattr__`. Les deux sont refusées, et 0 requête part.
  - **N19 est réécrite.** Le docstring ne le déclare pas, mais ce n'est pas un affaiblissement : N19b garde f3 au-delà de sa réserve, et la course s'arrête (16).
  - Mon rejeu (`attaques-cl-v1-sur-v2-rejeu.*`) est identique au tableau du LISEZMOI, § 3.
- **B1.** Le journal garde le diagnostic entier par appel : `usage_brut` imbriqué (détail de réflexion, `cache_write_tokens`), `usage_refuse`, `en_tetes_id`. Il ne contient ni la clé ni le texte (N26).
- **B2.** Les arrêts tiennent :
  - 16 si le coût dépasse la réserve, si l'usage est refusé ou si la sortie dépasse `max_tokens` ;
  - 14 si le cumul dépasse le plafond ;
  - 13 si un appel autre que f5 échoue (N26 : un 500 sur f1 donne 13, à 0,0209 USD) ;
  - f2 passe en premier ;
  - coupure côté client (N10 : 842 octets).
  - Reste au-dessus du client : un amont qui facture après la coupure. Le budget du projet et le solde le bornent, comme le LISEZMOI le déclare.
- **`max_tokens` et `max_completion_tokens`** (N24) : les deux partent, à la même valeur. `champs_max` sert à n'en garder qu'un ; un champ autre ou vide est refusé.

## Artefacts neufs (`attaques-neuves-v2.*`)

- N21 : usage dans `choices` du dernier morceau → refusé.
- N22 : 17 deltas d'un caractère pour `max_tokens` = 16 → **coupure**, AnomalieReponse.
- N23 : commentaire de maintien entre l'usage et `[DONE]` → accepté.
- N25 : clé dans `X-Request-Id` → masquée.
- N26 : voir B2 ci-dessus.

## Bloquant pour la fumée

Aucun.

## À noter

1. **N22.** La coupure à « plus de `max_tokens` morceaux non vides » peut se déclencher à tort si l'amont découpe sous le jeton. Elle se déclenche alors à f2, avant la lecture de l'usage : le champ de H2 serait perdu, et il faudrait un nouveau GO. Recommandation : une marge (par exemple 2 × `max_tokens` + 8), le plafond en octets restant la garde principale.
2. **N21.** Un usage rangé dans `choices` arrête la fumée dès f2. C'est conforme à la documentation (`choices: []`). La forme est gardée au journal.
3. **Docstring du rejeu.** Il annonce trois changements, mais la réécriture de N19 n'y est pas déclarée.
