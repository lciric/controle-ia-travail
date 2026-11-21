# Ligne pour `CLAUDE.md` — décision N-075, après les choix de Lazar du 21 novembre (v1)

- **Ce que c'est.** La ligne de la liste « Décisions de Lazar » de `CLAUDE.md` pour N-075, telle qu'elle se lit après `GO-2026-11-21-61`. Elle accompagne l'erratum 3 de la décision (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3-erratum-3.md`, section 7).
- **Auteur et heure.** Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), sur mandat de la session mère ; 21 novembre 2026, 16:13 UTC (`date -u`). Je ne modifie pas `CLAUDE.md` : la mère inscrit la ligne.

## La ligne

> N-075 (GO-2026-11-21-46, -47, -51, -53, -61) : contre le diffus, mesurer l'issue et corriger — plancher d'audit au hasard publié, jamais revendiqué, q mesuré par dommages plantés, strate non mesurée à zéro ; sondes : accélérateur, non garantie ; dilemme, non décorrélation ; pince en trois objets ; alerte = motif et dommage au même lieu, motif seul : audit, jamais témoin ; lemme resserré au reste, à démontrer ; veille à côté des chantiers ; réapprentissage sur l'oracle non tranché, N-060 v3 tient (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, errata 1 à 3, le 3 prime).

Longueur : 598 signes, mesurée par programme (plafond de 600 que la mère avait fixé pour cette ligne).

## Ce qu'elle remplace

`CLAUDE.md` porte déjà une ligne N-075, inscrite par la session mère au commit `466e3c815` avec l'erratum 2 (548 signes) :

> N-075 (GO-2026-11-21-46, -47, -51, -53, -61) : contre le diffus, mesurer l'issue et corriger — plancher d'audit au hasard publié (« Blindfold », Gans et Holden, Podkopaev et Ramdas : base citée), oracle exogène, q mesuré par dommages plantés, strate non mesurée à zéro ; sondes en accélérateur ; alerte = signal et dommage au même endroit, motif seul en audit prioritaire ; lemme resserré au reste ; veille à côté des chantiers ; réentraînement en service ouvert (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`, errata 1 et 2).

La ligne ci-dessus se met à sa place. Trois raisons.

1. **« Réentraînement en service ouvert » peut se lire « permis ».** Le point 9 n'est pas tranché : Lazar penche pour le permettre, la question va au collisionneur et à l'organisme, et d'ici son mot l'invariant de l'oracle (N-060 v3, point 4) s'applique en entier. La ligne neuve dit « non tranché, N-060 v3 tient ».
2. **La règle à deux clés.** La forme retenue (point 8, option (a)) dit « motif », non « signal », et porte « jamais les témoins » : un épisode signalé sans preuve de dommage va à l'audit et n'entre jamais dans les témoins.
3. **Quatre accords antérieurs rendus.** « Jamais revendiqué » (le plancher est publié), « non garantie » (`GO-2026-11-21-46`), « dilemme, non décorrélation » (`GO-2026-11-21-51`), « pince en trois objets » (`GO-2026-11-21-53`) : la ligne de l'erratum 1 les portait, celle du commit `466e3c815` les avait perdus.

Ce que la ligne neuve perd, faute de place : les trois noms cités pour le plancher (« Blindfold », Gans et Holden, Podkopaev et Ramdas), « oracle exogène », « hors porte », « 1981 cité » pour le lemme. Ils restent dans la décision (v3, sections 2, 7 et 8 ; erratum 1, corrections C-1 et C-2).

## Autre effet sur `CLAUDE.md`

Aucun de plus. La dernière puce de « Allègement de la procédure » dit déjà « Veille à côté des chantiers (N-075, point 7) », depuis le même commit : c'est le point 7, option (a).
