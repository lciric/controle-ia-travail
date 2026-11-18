# Brouillon de relais (Lazar → session mère) — témoin de Bailey : dépôt chez le tiers, clés, jeton

Rédigé par la session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`) ; à envoyer par Lazar (contact
extérieur : la session rédige, Lazar envoie). Aucun résultat du témoin n'y figure.

## 1. Dépôt chez le tiers (horodatage des pièces scellées, avant toute lecture)
Pièces à déposer, toutes scellées sur la branche `claude/compassionate-meitner-d4ryyk` de `lciric/controle-ia-travail` :

| pièce | empreinte SHA-256 |
|---|---|
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-3-code-v16-message-erreur-nouvelle-serie.md` | `4b1f33bf4102b4a6dcc0873d41682ebbe00220c5a678c9eacaa4e69ea2624b58` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-troisieme-serie.md` | `89d2f6470a30276197a7ca986355e8026bb7ed6a5e2be43a068166acdcd5bbf3` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-5-relance-seule-code-v20.md` | `eb97994a1ebcd0f3dfa3b413187a0b4dc213ef62ad1e516fc4b8814eb8ab357d` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-6-credit-recharge-auto.md` | `982bfbcbb7ed5634b0f297514133999d4141de53ed458c41e0c95d6f8281d49d` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md` | `554a74d07c848c493c485f5f7c37d26dc419e7da381ee4180235adb76edd7f3e` |
| `src/controle_ia/temoin_bailey/lecture_scellee_v3.py` (code de lecture de l'addendum 7) | `a367853b4aadbf20482001ad086c67fdaa5b6e80bc45ac4a15f01d9211800dcb` |

Rappel : texte `fb6c2f34…`, addenda 1 et 2 déjà déposés selon la mère (à vérifier par elle).

## 2. Clés et jeton (à la fin du témoin seulement)
- Ne pas retirer maintenant : la clé de déploiement `diag-temoin-bailey-depot-20261115` et la clé `ssh` Vast 1864483
  servent encore à la reprise et à la relance de la confirmation (postes Hetzner). À retirer après la clôture.
- Révocation du jeton GitHub du témoin : après la clôture, même raison.

## 3. Serveur de sauvegarde Hetzner 176187199
Gardé jusqu'à la clôture de la confirmation (sauvegarde des transferts) ; destruction proposée après le rapport.
