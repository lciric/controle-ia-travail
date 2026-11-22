# Journal — brouillon 6 de l'ordre de course (T0.8)

Écrit par `brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon6-v1.py`. Causes : « R-5060 », décision de la session mère (admission du fichier recomposé) ; « chaîne », message du développeur de la chaîne de lancement du 22 novembre vers 21:19 UTC, après la contre-lecture de la chaîne.

| n° | cause | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | sur une machine louée — v1 — brouillon 5… | sur une machine louée — v1 — brouillon 6… |
| 2 | renvoi | - **Statut** : **brouillon 5**, pièce de classe A, qui porte les commandes. Il applique au brouillon… | - **Statut** : **brouillon 6**, pièce de classe A, qui porte les commandes. Il ajoute au brouillon 5… |
| 3 | renvoi | la différence de ce brouillon 5 est à vérifier de même.… | la différence des brouillons 5 et 6 est à vérifier de même.… |
| 4 | R-5060 | Le fichier ainsi versé n'entre dans aucune lecture sans un texte contre-lu (section 8) : si la lectu… | **Admission du fichier recomposé** (décision de la session mère, R-5060 ; cette ligne est le texte c… |
| 5 | chaîne | 11. **Destruction par l'identifiant** (R10), après la vérification de la poussée ;… | 11. **Destruction par l'identifiant** (R10), après la vérification de la poussée — la machine se dét… |
| 6 | chaîne | Avant l'étape 2, par la session mère, au scellement (rappel ; ce n'est pas un geste de l'exécutante)… | Avant l'étape 2, par la session mère, au scellement (rappel ; ce n'est pas un geste de l'exécutante)… |
| 7 | chaîne | L'amorce laisse la machine à l'état arrêté en fin de course ; elle n'est détruite que par ce geste, … | Depuis la contre-lecture de la chaîne, la machine se détruit elle-même en fin normale, après le vers… |

Entrée : `c029aca9dc9b62e43e5e23be2fda2f13728deb3c73b4e4d0ed137f28ac8725b4`. Sortie : `06127b1810973100b22f01d8690fb062bbf4f69c2909d091e0bd3976026ad2dc`. Opérations : 7.

**À juger par le contre-lecteur** : la section 8 demande, pour ce qui est récupéré d'une machine en échec, un texte contre-lu et le mot de Lazar. L'auteur lit le fichier recomposé, égal à l'octet à la sortie scellée, comme la sortie elle-même et non comme un résultat récupéré ; la session mère l'a décidé à son étage (R-5060). Si cette lecture ne tient pas, le mot de Lazar est requis.

**Non vérifié par l'auteur** : les trois changements de la chaîne, connus par un message ; le code n'a pas été relu.
