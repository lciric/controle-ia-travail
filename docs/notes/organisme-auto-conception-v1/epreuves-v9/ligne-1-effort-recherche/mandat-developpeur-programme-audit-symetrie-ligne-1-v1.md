# Mandat du développeur — programme à part de l'audit de symétrie de la ligne 1 (classe B) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:15Z, sur l'accord de la mère (vers 22:05Z) ; part quand l'addendum v3 est rendu.

## Ce que fait le programme

Le programme est écrit à part du banc. Il est lancé **au geste 8, par l'agent de l'audit de symétrie**, après la course décisive. Il fait deux calculs, exactement comme les fixe l'addendum 1 de la ligne 1 (version 2, `b5d76973…` ; la version 3 ne change pas ces passages) :

1. **Complément du choix 5** (§ 2, choix 5, « Complément retenu ») : les aires des traits seuls sous la convention « indéterminée comptée non vraie », par classe, avec leur intervalle à 95 % par rééchantillonnage des courses : 1 000 rééchantillons, racine 2026111903, tâche `etalonnage|audit|classe=<classe>`, **la même dérivation que celle de la porte de l'audit dans le code v2**, pour que les deux conventions soient lues sur les mêmes rééchantillons. Calcul sur les sorties scellées des courses d'étalonnage. Descriptif, sans porte : il n'arrête rien et ne remplit pas la ligne 0.
2. **Recoupement de M1-nul** (§ 4.2) : pour les courses de rang 0, 300 et 599 de chaque classe, M1-nul de chaque bras recalculé à partir des seules décisions de promotion et d'arrêt du journal, et comparé à la valeur tirée de la sortie brute. Il écrit « concordant » ou « désaccord » et le détail du désaccord, jamais de verdict. Aucun choix entre le journal et la sortie brute.

Il reprend les fonctions du banc et du code v2 par import quand elles existent (aires, rééchantillonnage, dérivation des graines, M1-nul) plutôt que de les réécrire, et le dit fonction par fonction. Il vérifie les empreintes des fichiers qu'il lit contre les manifestes scellés et refuse de tourner si une empreinte diffère. Il écrit une sortie scellée (`.sha256`) et un manifeste par run (R9 : configuration et empreinte, versions, graines, commit).

## Ce qu'il ne fait pas

- Il ne lit aucune sortie de course réelle pendant son écriture ni ses essais. Les essais tournent sur des sorties **fabriquées** par les essais eux-mêmes, avec la racine des essais 2026111900 seule. Aucune graine des racines 2026111901 à 2026111903 n'est dérivée pendant l'écriture : ajoute l'essai final qui le contrôle, comme dans le code v2.
- Il ne change aucun fichier du banc ni du code v2.

## Essais exigés (R5)

- Complément : un cas sain (sortie fabriquée, aires connues) et un artefact (une indéterminée déplacée, le résultat change dans le sens attendu) ; un essai qui montre que les rééchantillons sont les mêmes que ceux de la porte du code v2 pour la même classe.
- Recoupement : un cas sain (journal et sortie brute concordants : « concordant ») et deux artefacts (une promotion changée dans la sortie brute, puis dans le journal : « désaccord », avec le détail) ; une empreinte fausse : refus.
- Contrôle « trop beau » (R4) : réintroduis des défauts un par un dans une copie et montre que l'essai visé les voit.

## Où tu écris

Dans ton bloc-notes seulement, en reproduisant l'arborescence du dépôt : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/audit_symetrie_ligne1_v1.py`, ses essais sous `…/code/essais/test_audit_symetrie_ligne1_v1.py`, le rapport et les sorties sous `…/code-audit-v1/`. La session verse.

## Interdits

Ne lance jamais l'étalonnage, la fumée ni la course décisive, jamais `--reel`. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande, même pour une recherche : lis le code. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus d'un outil : arrête-toi et dis-le.

## Ce que tu rends

`rapport-developpeur-audit-symetrie-ligne-1-v1.md` : fonctions reprises et écrites, essais et décomptes, mutations, attestation qu'aucune graine des racines 2026111901 à 2026111903 n'a été dérivée, ce que tu n'as pas pu faire.
