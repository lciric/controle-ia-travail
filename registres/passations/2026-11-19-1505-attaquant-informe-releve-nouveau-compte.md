# Passation de relève — attaquant informé, vers une session neuve sur un autre compte (2026-11-19, 15:05Z)

Session sortante : `session_013QMaynSCWwud812phoDNwn`. Branche de travail : `claude/festive-cannon-5ys0mz`.
Mot de Lazar : « fais la passation sur un autre compte nouvelle session ou fable a des credits ». La session entrante
est ouverte par Lazar sur un autre compte. Elle ne joint aucune session de ce compte par message (« not found » entre
comptes) : la continuité passe par les fichiers du dépôt `lciric/controle-ia-travail`.

## À lire d'abord (et rien d'autre du témoin)
1. `CLAUDE.md` de `main`, avec la section « Récupérer ce qui est récupérable » (R-3661).
2. `docs/procedures/brief-session-attaquant-informe-v1.md` et `docs/procedures/orientation-sessions-v1.md` (sur `main`).
3. Sur cette branche : `registres/passations/2026-11-19-1208-attaquant-informe-surveillance-bailey-close.md`
   (`b8d19892…`), puis la présente passation.
4. Sur `claude/compassionate-meitner-d4ryyk` : `registres/passations/2026-11-19-1205-bailey-cloture-et-verdicts.md`
   (passation de l'ancienne session) et `registres/passations/2026-11-19-1500-note-go-verdict-bailey.md` (`99d963df…`).

## État au relevé de 15:03Z (lecture seule)
- **Témoin de Bailey : clos.** Relance finie (72 tours sur 72, marque à 10:09:59Z). Verdicts scellés selon l'addendum 7,
  § 3. Rapport `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-verdicts-temoin-bailey-v1.md`
  (`75db4cbd…`). **GO-2026-11-19-51** (Lazar, 12:38:35Z, « go recos ») : verdict accepté, « effet reproduit sur le banc
  des auteurs, au régime publié », avec ses réserves. Note du GO posée sur la branche de l'ancienne session (commit
  b6540d22e, avec l'accord de Lazar).
- **Vast** : aucune instance du témoin ni de ce rôle. Arrêtées, intouchables : 58936096, 58936099, 58936100 (« R8 »),
  60988826. Crédit 21,96 USD. La recharge automatique n'a jamais été vue jouer ; celle de 09:43Z était manuelle.
- **Hetzner** : seul reste 176187199 (`sauvegarde-temoin-bailey-v2`, en marche). Le poste v14 et les postes
  d'inventaire sont détruits (commit 44bf764bb de l'ancienne session : six serveurs détruits après inventaire par
  instantané). Le sort de 176187199 et l'effacement des instantanés protégés (458234516, 458234528, 458234531)
  reviennent à l'ancienne session ou à Lazar.
- **Mère en exercice** : `session_013QMayjsoZJFBUCqcnvD5h1`, joignable depuis ce compte seulement.

## Ouvert (nœuds de Lazar)
- **Clé restreinte de 61170458** dans l'historique de `claude/compassionate-meitner-d4ryyk` (commit 2a1c0ff9) :
  révocation dans la console Vast par Lazar ; purge de l'historique (poussée forcée) à trancher. D'ici là : aucune
  fusion de cette branche vers `main`, aucune copie publique.
- **Bras d'attaque, pièce 4** : le projet de courriel v4 (`3f1121f5…`, commit 565a6513) n'est pas envoyable. Il garde
  18 points « À décider » et 11 « À remplir ». Contact externe : tu rédiges, Lazar envoie.
- **Recharge automatique** : vérifier son réglage avant la prochaine longue course.

## Prochaine action de la session entrante
Faire la routine de reprise (R14) sur `main`. Lire les quatre pièces ci-dessus. Constater par lecture qu'aucune machine
de ce rôle ne tourne. Attendre de Lazar la suite du bras d'attaque : lecture des réserves du verdict de Bailey (après le
GO, plus sous cloison), ou pièce 4.

## Cloisonnement inchangé
- Ne lire ni le coffre (`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`), ni les
  épisodes d'épreuve, ni les seuils des moniteurs, ni la réserve de détecteurs.
- Clés : vérifier leur présence par le nom seulement.
- Arrêts et destructions par identifiant.
- Aucune dépense sans GO.
- Garde des secrets avant chaque commit.
