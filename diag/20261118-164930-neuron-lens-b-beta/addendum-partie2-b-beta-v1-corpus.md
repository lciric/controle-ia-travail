# Addendum de la tranche de l'ajustement de nos lentilles — partie 2, second relevé (après les comptes de jetons) — v2

Écrit sur la machine juste après l'unique `03_token_counts.py`, avant `lens_compare.py` et la fumée. **Tout écart ci-dessous
arrête la course à cette étape (nœud à la mère).**

## Écarts

Aucun.

## Corpus d'activations

| fichier | sha256 relevé | attendu |
|---|---|---|
| `act-dclm.jsonl` | `64657ecbb54f7899db33564c502f3bb8f01c6d13348855584e7db1894d893ba4` | `64657ecbb54f7899db33564c502f3bb8f01c6d13348855584e7db1894d893ba4` |
| `act-zh.jsonl` | `c3202db1eab8938984f8bea6b49c229610d2eb89ecee6148c8b5ad6942fd4f5b` | `c3202db1eab8938984f8bea6b49c229610d2eb89ecee6148c8b5ad6942fd4f5b` |
| `act-code.jsonl` | `550944a25182286079c581882bb1c5f3bb1ffce153af711506d0e388d01959e6` | `550944a25182286079c581882bb1c5f3bb1ffce153af711506d0e388d01959e6` |
| `act-chat-llama-3.1-8b-instruct.jsonl` | `9dbf9f44cdbf1a218181c886002905885b4b5d941dcdeb4a4cbfa0ffa5e8d828` | `9dbf9f44cdbf1a218181c886002905885b4b5d941dcdeb4a4cbfa0ffa5e8d828` |

## Jetons gardés de Llama : 89498 identifiants, sha256 `c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68`

Jeton de début (128 000) : compte 72000 dans le corpus d'activations ; gardé : True ; rang par compte décroissant parmi les jetons gardés : 117 (1 + jetons gardés de compte strictement plus grand) — rapporté, sans critère.
