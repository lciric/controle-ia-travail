# Passation — conseiller Opus sur la garde des activations de la relecture décisive du barreau 5 — 23 novembre 2026, vers 06:28Z

Session `session_013QMayje82YSDPLjNAgRDwr`, fille de la mère `session_013QMayjbmQUdDuDs2S3i3XD`. Passation écrite à la demande de la mère (reprise possible sur un autre compte, GO-2026-11-23-09). Aucun résultat dans ce fichier.

## Mandat
Reçu de la mère le 22 novembre au soir : conseiller Lazar sur une seule décision. Pour la relecture décisive du barreau 5 (test « sabotage ou empreinte » sur 39 adaptateurs jumeaux), garder les activations en « une_sur_dix » (option a, défaut), en « trois_couches » avec un volume chez Hetzner (option b), ou dans la voie médiane « couche_15 ». Un conseiller Fable répondait en parallèle, sans voir ma réponse. Aucune dépense, pas de sous-agent, réponse courte, lecture limitée à une seule pièce.

## Fait
- Routine de reprise réduite au mandat : empreintes de lancement vérifiées (`docs/sha256sums-lancement-v2.txt`, trois fichiers conformes) ; `registres/rappels.md` lu, aucun rappel échu le 22 novembre.
- Lu la seule pièce `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/options-garde-activations-decisive-b5f-v1.md`, par `git show` au commit `449d3cb097b2d26a637bfbe5d2aeb97fa14e64d4` de la branche `conducteur-b5f/lecture-v1`, récupérée par une référence explicite ; empreinte `e227497dbd139eb1fed7e0bfb2c36f6714eb9e97f60e8b3be4beb81132c1db04` vérifiée.
- Avis envoyé à la mère par message entre sessions le 22 novembre au soir : option (a) « une_sur_dix », confiance haute (environ 85 %). Le texte de l'avis est en annexe.

## Non lu (cloisonnement)
Rien d'autre de la branche `conducteur-b5f/lecture-v1` ; ni le texte scellé du barreau 5, ni aucun verdict, ni `diag/`, `runs/`, `donnees/`, ni `registres/etat.md`, ni aucune autre passation.

## Reste
Rien pour cette session. La décision appartient à Lazar et à la mère ; je ne sais pas ce qui a été retenu.

## Réserves
- Routine de reprise partielle : l'état n'a pas été lu, les machines n'ont pas été inventoriées (je n'en ai touché aucune) et les tests n'ont pas été lancés (je n'ai touché à aucun code).
- `registres/etat.md` n'est pas mis à jour : il est tenu par la mère. Cette branche ne porte que la présente passation.
- La condition dont dépend l'avis n'a pas été vérifiée par moi : les entrées d'un rejeu (poids des 43 adaptateurs, textes et épisodes, révision du modèle, code figé et versions) doivent être gardées hors de la carte, avec leurs empreintes.
- Les « 85 % » sont une confiance subjective, pas une mesure.

## Prochaine action
Aucune pour cette session. Pour la mère : consigner l'avis à côté de celui du conseiller Fable ; si l'option (a) est retenue, vérifier la condition sur les entrées d'un rejeu avant le départ.

## Branches et commits
- Lue : `conducteur-b5f/lecture-v1` au commit `449d3cb097b2d26a637bfbe5d2aeb97fa14e64d4`, non modifiée.
- Écrite : `avis/garde-activations-b5f-opus-v1`, partie de `main` au commit `38ac0b3f7e7e6f75922cddc6d54fa20033a37a6a`. Seuls ajouts : cette passation et son `.sha256`.

## Tâches planifiées actives
Aucune créée par cette session. Aucune machine de calcul lancée ni arrêtée.

## Versé
Le bloc-notes de la session est vide. Rien n'a été écrit dans `/tmp`. Il n'y a ni brouillon, ni essai, ni journal, ni autre réponse de modèle que l'avis ci-dessous. Il ne reste rien à verser.

## Annexe — l'avis tel qu'envoyé à la mère (en-tête abrégé)

Conseil Opus — garde des activations de la relecture décisive du barreau 5 (session session_013QMayje82YSDPLjNAgRDwr)

**Qui a lu quoi** : j'ai lu CLAUDE.md, `registres/rappels.md` (aucun rappel échu le 22) et la seule pièce `options-garde-activations-decisive-b5f-v1.md`, par `git show` au commit 449d3cb0 de `conducteur-b5f/lecture-v1` (sha256 e227497d… vérifié), rien d'autre de cette branche — ni texte scellé du barreau 5, ni verdict, ni `diag/`, `runs/`, `donnees/`, ni `registres/etat.md`.
(Routine de reprise réduite au mandat : empreintes de lancement vérifiées, conformes ; ni inventaire des machines — je n'en touche aucune —, ni tests, ni passation, selon ta consigne.)

**Recommandation : (a) « une_sur_dix », ce soir. Confiance haute (≈ 85 %).** Ni (b) ni la voie médiane.

**Raisons**
1. **Rien de décisif n'en dépend, et ce qu'on perd se rachète.** Scores fermés et issue identiques. (b) coûte ce soir ≈ 15 dollars de plus hors carte, plus une carte plus longue, puis ≈ 17 dollars par mois de volume ; un rejeu plus tard, code figé et mêmes entrées, coûte ≈ 10 à 17 dollars, et seulement si le besoin vient. Coût au plus égal même si le besoin est certain.
2. **(b) n'est pas faisable proprement cette nuit.** Trois nœuds à ouvrir (clé inscrite chez le loueur, donc compte changé ; dépassement du plafond de 33 dollars du mot de Lazar, GO-2026-11-22-117 ; volume prévu jusqu'au 21 décembre, au-delà de l'accord qui échoit le 30 novembre), le poste de Lazar joignable de nuit, une procédure de transfert non contre-lue, un erratum au mandat d'une course payante. Surtout, (b) change le chemin d'arrêt et de destruction d'une machine payante le soir même de la relecture décisive : garde jamais éprouvée sur un cas sain ni sur un artefact (R5), instance arrêtée qui facture ; si l'hôte ne revient pas, le repli écrit ramène à (a), plus cher et plus tard.
3. **La voie médiane est dominée.** Elle paie les coûts fixes de (b) (gestes, nœuds, erratum, transfert : l'essentiel) sans les couches 7 et 23, celles que demandent justement les lectures « à poids jumelés ». Si l'on fait ces gestes un jour, autant faire (b).
4. **(a) garde l'utile, et un étalon.** Les diagnostics préalables de la conception v2 des sondes y tiennent. Le dixième apparié, à liste de clés fixe, sert d'étalon à tout rejeu futur : avant toute analyse neuve, vérifier que le rejeu reproduit ces activations à tolérance près (les activations, jamais les scores). Il peut aussi servir de pilote pour chiffrer le besoin de la sonde apprise sur les épisodes honnêtes avant de payer, si ce qui lui manque est du volume et non le jeton.
5. **Ce qui manque sert des analyses ni conçues ni préenregistrées.** Leur besoin réel sera plus étroit que « tout » (épisodes honnêtes, quelques jetons, deux couches) : un rejeu ciblé coûtera moins, et peut se glisser dans la prochaine course de la conception v2. Et une fois lus ce soir, les 30 adaptateurs tenus à l'écart ne serviront plus guère qu'à concevoir, plus à confirmer : tout garder d'eux vaut moins qu'il n'y paraît.

**Ce qui me ferait changer**
- **Les entrées d'un rejeu ne sont pas toutes hors de la carte, avec empreintes** (poids des 43 adaptateurs, textes et épisodes, révision du modèle, code figé et versions). C'est la condition qui rend (a) réversible : à vérifier dans le manifeste avant le départ. S'il en manque, les verser d'abord (c'est petit) ; si c'est impossible, (b).
- Un rejeu ne reproduirait pas ces activations (lecture dépendant d'un tirage ou d'un état propre à la carte).
- Une conception écrite pose la sonde des épisodes honnêtes ou les couches 7 et 23 comme préalables à l'entretien du 1er décembre ou à la porte de sortie de la phase 0, à une date où un rejeu ne pourrait plus être autorisé et fait à temps.
- Gestes de (b) déjà prêts (poste joignable, clé inscrite sur le mot de Lazar, procédure contre-lue, dépassement accordé) et besoin des couches 7 et 23 déjà écrit : (b) devient défendable.

**À côté, sans toucher au code** : vérifier que l'inventaire de ce qui sera détruit (noms, tailles, empreintes) est versé — règle « récupérer ce qui est récupérable » ; sinon, le consigner comme écart connu. Inscrire le rejeu ciblé au registre des idées de la veille de cap, pour qu'il ne se perde pas sans décision nommée.

Fin de ma part.
