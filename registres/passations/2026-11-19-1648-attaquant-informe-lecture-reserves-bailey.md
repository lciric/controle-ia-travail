# Passation — attaquant informé : réserves du verdict de Bailey lues ; Vast lisible (2026-11-19)

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Suite de la passation de
15:30Z (`f16b5d02…`).

## Fait
- **Mot de Lazar : « lis les réserves du verdict de Bailey ».**
  - Note `docs/notes/reproduction-attaque-publiee-v1/lecture-reserves-verdict-v1/lecture-reserves-verdict-bailey-v1.md`
    (`7d4da5c9…`).
  - Calcul `calcul-reserves-verdict-bailey-v1.py` (`92f9c58d…`) et valeurs `valeurs-reserves-verdict-bailey-v1.json`
    (`71adff7a…`), dans le même dossier ; commit `26714070`.
  - Information après GO-2026-11-19-51, sans effet sur le verdict.
  - Points saillants : suffixe de 13 jetons au lieu de 16 ; marge nette (71 tours gagnés sur 72, défense à 200 sur 200).
    Le seul tour perdu est le dernier : vrai échec partiel de l'attaquant (perte d'obfuscation restée à 0,188), mesure
    sur le fil (intervalle de 1 à 200).
- **Vast.**
  - Lazar a donné une clé Vast en clair dans la conversation, deux fois. Elle a été enregistrée sur l'environnement par le
    formulaire sécurisé (secret réseau, hôte `console.vast.ai`) ; la valeur n'est écrite nulle part dans le dépôt.
    Recommandation faite à Lazar : la révoquer et en saisir une neuve par le formulaire.
  - Relevé de 16:43Z : quatre instances, toutes arrêtées, aucune de ce rôle. 58936096, 58936099 et 58936100 (« R8 »,
    intouchables) ; 60988826 (`jeu-idee-1-1-relance-v1`). 61414494, vue en marche à 12:07Z par la session sortante, n'est
    plus listée.

## Instances actives (16:48Z)
Aucune pour ce rôle. Hetzner : aucun serveur ; quatre instantanés protégés. Vast : voir ci-dessus.

## Prochaine action
Attendre le mot de Lazar. Suite du bras d'attaque : pièce 4, ou autre. Nœuds ouverts : effacement des instantanés,
révocation des clés (dont la clé Vast collée dans la conversation), purge de l'historique de la branche.

## Lignes proposées à la mère
1. « Réserves du verdict de Bailey lues sur le mot de Lazar (information, sans effet) : note `7d4da5c9…` sur
   `claude/compassionate-meitner-d4ryyk`. »
2. « Clé Vast exposée dans une conversation (session attaquant informé, 19 novembre vers 16:40Z) ; révocation recommandée
   à Lazar. »
