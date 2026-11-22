# Vérification courte de l'outil de relecture d'une correction par Fable 5.2 appelé par l'interface d'Anthropic, v3

Même contre-lecteur que la contre-lecture de la v1 et la vérification de la v2 : Claude Opus 5.5, 21 novembre 2026.
Pièce d'instrument, classe B. Aucun appel réel ; aucun fichier de la pièce modifié ; mutations faites dans des copies du
bloc-notes de la session.

## Verdict : **conforme**

La v3 n'ajoute que l'option `--effort`. Ses valeurs sont fermées (low, medium, high, xhigh, max) et le défaut est high.
L'effort part au comptage comme à la génération. Une valeur hors de la liste est refusée avant tout envoi, deux fois :
par l'analyseur d'arguments, puis par `relire`. Le pire coût et les champs du journal ne changent pas, et aucune option
de budget de réflexion n'existe. Sur un dossier temporaire neuf, 95 essais passent ; mes trois mutations sont tuées.

## Pièces vérifiées

| Pièce | Empreinte (compagnon vérifié par `sha256sum -c`) |
|---|---|
| `src/controle_ia/relecture_fable_api_v3.py` | `95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62` — OK |
| `tests/test_relecture_fable_api_v3.py` | `f1b3af948466d8cf042a5ed8fceb0fa57055b7db31af492d4c6bf33f8865961f` — OK |
| `docs/notes/relecture-fable-api-v1/rapport-developpeur-v3.md` | `e6ae3d2a305097134f58679ff73c4465d983af00f5bb023a564db7960489d163` — OK |
| v2 gardée : module, essais | `c8e8506f…`, `89f91fa2…` (inchangés) |

## 1. Différence entre la v2 et la v3 (module)

Les lignes ci-dessous sont les seules qui changent :
- noms de la version : titre, emploi, `VERSION`, `prog` ;
- note d'en-tête v3, ligne d'emploi `[--effort …]`, point 7 de la documentation ;
- `EFFORT = "max"` est remplacé par `EFFORTS = ("low", "medium", "high", "xhigh", "max")` et `EFFORT_DEFAUT = "high"` ;
- l'en-tête de la relecture et `_ligne_base` portent l'effort demandé (`ligne['effort']`, `args.effort`) ;
- un contrôle est ajouté dans `relire`, à l'étape 0 : `if args.effort not in EFFORTS: raise Refus(CODE_USAGE, …)`.
  Il tombe avant la lecture des entrées, la garde de motifs, le comptage et l'envoi ;
- `params["output_config"] = {"effort": args.effort}` ;
- l'analyseur reçoit `--effort` avec `choices=EFFORTS` et `default=EFFORT_DEFAUT`.

Les autres lignes sont identiques. En particulier, la réflexion, le pire coût, le plafond, le journal et les gardes ne
changent pas.

**L'effort au comptage et à la génération.** Le même dictionnaire `params` sert aux deux appels.
`compter_par_sdk` en reprend `output_config`, et `envoyer_par_sdk` passe `params` entier à `messages.stream`.
L'essai `test_chemin_reel_effort_envoye` le confirme : il passe par le vrai kit contre le faux serveur local et contrôle
que chaque requête porte l'effort `medium`. Il n'est pas vide, puisque la mutation M12 ci-dessous le fait échouer.

## 2. Différence entre la v2 et la v3 (essais)

- noms : titre et importation ;
- deux attentes passent de `max` à `high`, conséquence du défaut ;
- 19 essais neufs :
  - les cinq valeurs admises, chacune envoyée et consignée au journal, aux compteurs et à l'en-tête, pire inchangé ;
  - sept valeurs refusées par l'analyseur (code 2) ;
  - trois valeurs refusées par `relire` (`MAX`, `ultra`, `None`), sans envoi, sans dossier de sortie, avec une ligne
    `refus_avant_envoi` ;
  - le défaut `high` ;
  - `--budget-reflexion` refusé comme option inconnue ;
  - l'essai du vrai kit décrit au § 1.
- 76 − 0 + 19 = 95.

## 3. Compétence « claude-api » (rechargée depuis le disque)

`shared/model-migration.md`, « Migrating to Claude Fable 5.2 », « Choosing an effort level - start at `high` » dit :
« All five levels are supported and the default is `high` », et décrit low, medium, high, xhigh et max. La liste fermée
est donc juste.

Sur la réflexion :
- la section Fable 5.1, sur laquelle la section 5.2 est posée, dit « no `thinking` config other than `{type:
  "adaptive"}` (`disabled` and `budget_tokens` both 400) » ;
- la section 5.2 dit de `max_tokens` « hard limit on total output (thinking plus response text) » ;
- les budgets de tâche (`task-budgets-2026-03-13`) sont « a suggestion the model is aware of, not a hard cap ».

Ne pas offrir de budget de réflexion est donc juste. Je n'ai pas pu relire sur le disque le tableau de `SKILL.md` que
cite le rapport, ce fichier n'étant pas dans le dossier rechargé. Le fond de ce tableau est confirmé par les deux
sections citées ci-dessus.

## 4. Rapport du développeur (diff v2 → v3)

- noms, nombre d'essais, ligne d'emploi, point de l'appel, table des essais ;
- réserve 3 complétée par le défaut constaté à l'effort `max` ;
- réserve 9 mise à jour ;
- § 8 neuf.

Les nombres que je peux recalculer sont exacts : 19 essais neufs, 95 au total. Les mutations du développeur sont
cohérentes avec les miennes. Je n'ai pas vérifié les chiffres du défaut constaté (128 000 et 96 000 jetons, 11,68 USD) :
ils viennent du rapport de la mère, et le rapport le dit.

## 5. Essais et mutations rejoués

`PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_relecture_fable_api_v3.py -p no:cacheprovider
--basetemp=<dossier neuf>` : **95 passés**.

Le module et les essais sont copiés à part, chaque mutant dans son propre dossier.

| Mutation | Résultat | Essais qui la tuent |
|---|---|---|
| témoin sans mutation | 95 passés | — |
| M12 : `output_config` retiré du corps du comptage | tuée (1) | `test_chemin_reel_effort_envoye` |
| M13 : effort figé au défaut dans la requête | tuée (5) | `test_effort_admis_envoye_et_consigne[low|medium|xhigh|max]`, `test_chemin_reel_effort_envoye` |
| M14 : contrôle de l'effort dans `relire` retiré | tuée (3) | `test_effort_hors_liste_refuse_par_relire[MAX|ultra|None]` |

## Remarques sans correction demandée

1. M12 n'est tuée que par un seul essai, celui du vrai kit. Les faux comptages des autres essais ne regardent pas
   l'effort. Cela suffit, puisque cet essai passe par le vrai chemin.
2. Le défaut `high` change ce que coûte et produit une relecture lancée sans `--effort`. La compétence dit que l'effet de
   `high` sur nos relectures n'est pas mesuré, et le rapport le dit aussi. Choisir l'effort d'une relecture décisive
   reste à la mère.
