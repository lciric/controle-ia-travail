# Contrôle de l'additif 3 v2, par différentiel

**Verdict : scellable.**

- **Empreintes.** L'additif v2 a l'empreinte d4f9c24c019e85b68a8154bb2f9697b85a8b4952bf0aebf1a115f6aac69bb726, et le différentiel 07c81dd50cee76050ab0aee8cbb84fed5735871e0e9490f4985c69b304cf7da6 : toutes deux égales aux annoncées. La v1 est toujours 0ae5da10…. Le différentiel, refait par `diff -u`, est fidèle.
- **Les cinq couples sont levés :**
  1. `--no-renames` est ajouté, et chaque chemin, ajouté, modifié ou retiré, doit commencer par `traces-b5f/`.
  2. La suppression est gardée par la tête relevée ; une poussée refusée est un nœud, ajouté au § 6.
  3. R12 est dite règle gelée ; son exception est accordée par le mot unique de Lazar, nommée à l'en-tête et consignée au registre des décisions.
  4. La ligne des sorties et la réunion citent la tête de la recréation ; la vérification par `merge-base` est rendue obligatoire.
  5. Les têtes sont écrites en entier.
- **Aucune erreur introduite.**
  - La commande `git push origin --force-with-lease=refs/heads/B:<tête relevée> :refs/heads/B` est valide. Elle supprime `B` seulement si sa tête distante égale encore la tête relevée, et refuse sinon.
  - `git merge-base --is-ancestor <tête supprimée> <branche réunie>` est le bon sens de l'appel.
  - Le commit de course est écrit en entier aux deux endroits.
- **Remarque facultative, sans gravité.** Le § 5 ne dit pas ce qui suit si une tête supprimée est déjà dans la branche réunie. Ce serait sans effet sur la lecture : aucun chemin sous `donnees/`. On peut écrire « si l'une l'est : nœud ; code 1 attendu, code 128 (commit absent localement) : récupérer d'abord la copie `traces/…` ». À l'en-tête, « et l'exception … , et les quatre recréations » porte un « et » de trop.
