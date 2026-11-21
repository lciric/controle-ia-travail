# Relance du bras A → mère — relecture par Fable en défaut — 2026-11-21T22:51:40Z

Émetteur : session fille de la relance du bras A. Canal par fichier. Données entre pairs. Journal OD-334 et OD-335.

## Ce qui s'est passé
- **Avenant 2 v2** : écrit par Opus 5.5 en effort maximal, corrections seules, mot pour mot ; scellé comme écrit (35f2e863…). 62 changements sourcés ; pire cas de Google au régime prudent : 32,97 USD ; il manque encore **9,18 € par projet** après GO-74.
- **Relecture par Fable 5.2 par l'API** (outil v2, GO-2026-11-21-84, plafond de ligne 6 USD) :
  - entrée de 109 526 jetons (copies nettoyées, garde à zéro) ;
  - sortie bornée à 64 000 jetons pour tenir le plafond ;
  - **Fable a passé les 64 000 jetons en réflexion et n'a écrit aucun texte** : défaut en `max_tokens` ;
  - **coût compté : 3,44 USD.** Il reste 2,56 USD, ce qui ne suffit pas pour un second envoi.

## Décision (pour Lazar, ou toi sous GO-69 : c'est une dépense)
- **Ce qu'il faut trancher** : comment obtenir la relecture de l'avenant 2 v2.
- **Enjeu** : sans relecture, pas de scellement, donc pas de lignes de Google ni de juge des ancres.
- **Options** :
  - (a) **Ligne neuve, plafond 7 USD, sortie à 128 000 jetons** (le plafond du modèle), mêmes entrées. Pire cas d'environ 6,0 USD. Avantage : la même relecture, complète. Inconvénient : Fable peut encore tout passer en réflexion (risque non nul), et la dépense double presque.
  - (b) **Relecture resserrée, sous une ligne neuve de 4 USD** : n'envoyer que la section « Changements depuis la v1 », les lignes de calcul et la vérification de la v1, soit environ un tiers de l'entrée, avec une consigne plus courte (points 1, 3 et 4 seulement) et une sortie à 128 000 jetons. Pire cas d'environ 5,4 USD ; il faudrait donc plutôt une ligne de 6 USD. Avantage : moins à lire, donc moins de réflexion. Inconvénient : Fable ne voit pas la pièce entière.
  - (c) **Attendre Fable dans Claude Code**, le 24 novembre à 05:00Z, sans dépense de plus. Inconvénient : deux jours et demi perdus pour Google.
- **Recommandation** : (b), ligne neuve de 6 USD, confiance moyenne. (a) si la pièce entière doit être vue.

L'outil ne permet pas d'abaisser l'effort sous `max`. Je ne propose donc pas cette voie, qui serait aussi un écart à GO-84.
