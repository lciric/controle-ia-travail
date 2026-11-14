# Contre-lecture 5 très ciblée du volet A — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé après le commit 8bed7cde, rapport lu avant 12:25 UTC ; lecture seule (`diff`,
`sha256sum`, 14 essais passés). Objet : remarques 5, 7, 8, 9, 10 de la contre-lecture 4. Compagnons des six pièces conformes ; les
`diff` ne contiennent que les changements décrits.

**Verdicts** : `garde_depense_v3.py` et son essai, `volet_a_lancer_v3.py` et son essai, `commande-volet-a-v3.md`,
`scripts/depot_reduit_neuron_lens_volet_a_v4.py` : **scellables en l'état**.

**Remarques** : 5, 7, 8, 9, 10 traitées ; mineure sans effet : la capture d'exception de `detruire_verifie` n'a pas d'essai propre ;
info : `volet_a_extraction_v1.py` deux fois dans `MODULES` (sans effet, dictionnaire) ; versions citées partout justes dans la commande
v3 ; les modules du lanceur sont couverts par la liste du dépôt réduit ; présence des modules communs non confirmée exhaustivement par
le lecteur (script lu en partie) : vérification à l'exécution par `liste-fichiers.sha256` recommandée.
