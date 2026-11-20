# Vérification des corrections du collisionneur v9, version 2

Écrite le 20 novembre 2026 par le même contre-lecteur (Claude Fable 5.2, `claude-fable-5-2`) que `contre-lecture-collisionneur-v9-v1.md` (`c5594c2b636af01b66ac71c12b79b87630b230d24a9b44628f5f3e3b0b299ea0`). Une passe, courte. Aucun appel à un fournisseur, aucune dépense, aucun commit, aucun autre fichier du dépôt modifié.

**Verdict : conforme.**

## Pièces vérifiées, empreintes recalculées et égales aux compagnons

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v2.py` | `2357b9e8da5193232ef4aa611d6e9ff668dc467f5aab3e82deb99fc8b901c0b4` |
| `test_collisionneur_v9_v2.py` | `69faf8c40282afc307fad0572c4a8935759193236e32532c1a32ca30179a3aeb` |
| `rapport-developpeur-collisionneur-v9-v2.md` | `b0826dc7b73154c6965ad3d482ff312f997fdb19caa0a9cc563a0c7bee0f2636` |

La version 1 est intacte (`977d4166…`, `81e2572c…`, `8ba7eb09…`).

## Constats

1. **Couples portés à la lettre.** Différence entre la version 1 et la version 2 du script relue en entier. B1 (trois couples), B2, B3, B4 (deux couples), C1 et C2 y sont au caractère près.
2. **C4, décision de la mère.** Les six espèces sont à 2,5 caractères par jeton. Le contrôle de l'entrée facturée vaut pour toutes les espèces ; l'écart de total reste propre à Google. Pire cas au plus long tour (144 478 caractères), relu sur la version 2 : Fable 1,68 puis 3,78 en relance ; Opus 0,67 / 1,51 ; Argon 1,89 / 2,59 ; Kimi 0,44 / 0,77 ; Astra 0,98 / 2,18 ; Carbon 2,20 / 2,20. Jev reste à 3 caractères par jeton, comme le dit le rapport.
3. **C5.** La fonction neuve `adresse_locale` lit le nom d'hôte, exige le protocole `http`, un port, et refuse tout nom d'utilisateur. Elle sert pour Kimi et pour OpenAI. L'adresse par défaut du relais de Kimi reste acceptée.
4. **C3 et C6.** Les quatre essais manquants sont ajoutés ; l'essai de Jev n'est plus vide (4 000 caractères, coût strictement positif). Les errata sont dans le rapport.
5. **Chaque trou fermé a son essai.** 117 essais passés sur la version 2. Les mêmes essais, lancés contre le script de la version 1 : 36 échecs, comme le dit le rapport. Mes deux sondes de la contre-lecture, relancées sur la version 2 : tous les trous montrés sont fermés (usage d'Anthropic non lu, usage partiel plus cher que le pire cas, entrée hors garde chez Fable, Jev sans usage, formes du nom, chemins, identifiant nu, écritures mathématiques).
6. **Rien d'autre ne change.** Hors couples : le nom de version, les six lignes d'usage, un bloc d'en-tête, un import (`urllib.parse`), deux descriptions de fonction et le commentaire de la table. Dans les essais existants, seules trois lignes changent (table à 2,5, texte et attente de l'essai de Jev), plus l'en-tête et le nom du fichier chargé.

## Réserves qui restent, déjà écrites au rapport

La liste des noms de personne est fermée. Les questions de version 3 sont toujours refusées. Le devis est à recalculer. Le budget de réflexion de Carbon n'a jamais été essayé en réel.

## Un refus de l'outil, dit tel quel

J'ai voulu ajouter trois épreuves par retrait sur des copies de la version 2 dans le bloc-notes (adresse locale, entrée gardée hors de Google, Jev sans usage). La commande ne supprimait rien. L'outil l'a refusée, et je ne l'ai pas relancée. Ces trois épreuves ne sont donc pas faites par moi ; le rapport du développeur en déclare six, dont deux recoupent les miennes. Texte exact du refus :

> Permission for this command was denied by a built-in Claude Code safety check, not by the user. The check stops removals that can delete far more than intended: a system, home or workspace directory, or a target it cannot resolve, such as a shell variable that, if unset or empty, turns this into `rm -rf /` or `rm -rf /*`. Only a person may approve such a removal, and no person did (the permission prompt timed out, or none was shown). The command was NOT run; do not claim it succeeded. Do not work around the check by splitting, scripting, or re-issuing the removal through another tool or shell: the check exists because a removal like this can destroy the user's data, and getting past it would not make it safe. If the text below suggests a safe rewrite, run that instead; it goes through the same check. Otherwise finish the rest of the task without this removal, tell the user what you wanted to delete and why, and leave the removal to them. What was flagged: Claude Code can't be sure it read this command the way the shell will, so it can't rule out a dangerous removal. This requires explicit approval. A command that deletes nothing can be sent again in plain syntax that bash and zsh both read, and that is not a workaround. A command that deletes anything, by rm or any other means, needs the user: do not send that part again.

Après ce refus, je n'ai fait qu'écrire et sceller cette pièce.

## Limites

Aucun appel réel. Je n'ai pas relu les programmes de correction du développeur, qui sont dans son bloc-notes. Mêmes cloisonnements que la contre-lecture.
