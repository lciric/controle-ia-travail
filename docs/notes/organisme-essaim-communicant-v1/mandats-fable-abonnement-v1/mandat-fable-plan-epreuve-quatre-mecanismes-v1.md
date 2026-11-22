# Mandat à Fable (session de l'abonnement) — plan d'épreuve de quatre mécanismes de l'organisme d'idéation — v1

Écrit le 2026-11-22T14:33:44Z par la session de l'organisme, sur le mot de Lazar relayé par la mère : « Quatre mécanismes y sont codés mais n'ont jamais été éprouvés sur des données réelles : la stratégie « hors des bassins promus », les marchepieds, le bisociateur et le moissonneur de nouveauté. go teste-les. » **La conception est à Fable.** Rien de payant ne part avant le devis et le mot de Lazar.

## Les quatre mécanismes
Ils sont dans le dépôt public `lciric/ideation-organism`, au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, à lire par chemin exact :

| mécanisme | où | empreinte |
|---|---|---|
| stratégie « hors des bassins promus » | `orchestrator/pole/proposeur.py`, l. 40 (« un couple (moniteur, trait) qu'aucune fiche promue ne couvre encore ») | `a77018584ec5d20c…` |
| marchepieds | `orchestrator/pole/recombinaison.py` (`tirage_marchepieds`, l. 232 ; `tirage="stratifie_marchepieds"`) ; `orchestrator/pole/cycle.py`, l. 117 | `71faad38644c77ae…` (recombinaison) |
| bisociateur | `orchestrator/pole/bisociateur_v53.py` (trois bras) | `962eb8ce22d5af1b…` |
| moissonneur de nouveauté | `orchestrator/pole/moisson.py` | `35d9a996aaacf6d6…` |

## Ce que Fable rend : un plan d'épreuve par mécanisme
1. **Ce qu'il prétend** : l'effet revendiqué, en une phrase, et le mécanisme causal.
2. **La base sans modèle à battre** : tirage au hasard, chercheur mécanique, ou les deux, avec le même budget d'appels.
3. **Le banc** : des mondes à vérité plantée. Un banc de ce nom existe dans une autre session du programme, que l'organisme ne lit pas. Dire ce qu'il doit contenir pour ce mécanisme : la vérité plantée, sa taille et ses distracteurs.
4. **La mesure et le seuil de réussite**, fixés d'avance, avec le signe attendu et le plan d'analyse (multiplicité comprise, puisqu'il y a quatre épreuves).
5. **Le coût et le délai** : appels par épreuve, avec un devis au plus haut et au pire, par modèle, sachant que les modèles Claude passent par l'abonnement.
6. **L'ordre** des quatre épreuves et ce qui permet d'arrêter tôt.
7. **Ce qui ne peut pas être conclu** d'une épreuve réussie ou ratée (limites).

## Règles
- Langue : français.
- Aucun appel payant.
- Ne lire aucun fichier dont le nom porte « vérité », « rendu » ou « scores », ni aucun fichier de `resultats/`.
- Marquer [FAIT RAPPORTÉ], [HYPOTHÈSE] ou [PROPOSITION].
- Le plan est une proposition : il sera préenregistré et contre-lu avant tout envoi (R1, R2).
