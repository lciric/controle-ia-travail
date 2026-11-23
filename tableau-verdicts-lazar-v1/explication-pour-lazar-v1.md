# Comment lire le tableau des verdicts — page d'explication pour Lazar, v1

**Pour Lazar seul**, à lire avec `tableau-verdicts-lazar-v1.md` (même dossier, même branche). Cette page ne contient **aucun chiffre mesuré** : tous les chiffres sont dans le tableau, lus par programme. Les seuls nombres d'ici sont des repères de lecture (0,5 pour le hasard, 1 pour la perfection).

## 1. La question commune à presque tous ces essais

Le programme demande si l'on peut voir un sabotage diffus **dans les activations** d'un agent (la boîte blanche) mieux qu'en lisant **son texte** (la boîte noire). Chaque essai pose un morceau de cette question :

- **un organisme** : un agent qu'on a rendu saboteur, soit par une consigne cachée dans son contexte (l'organisme « (i-a) »), soit par un petit adaptateur entraîné à imiter le saboteur, sans consigne, à plusieurs **doses** (0,25 ; 0,5 ; 0,75 ; 1 : la part de l'adaptateur appliquée) ;
- **un sabotage mesurable** : ici, gonfler le coût de calcul déclaré dans les propositions ;
- **un moniteur** : une sonde, c'est-à-dire une direction dans les activations dont la projection donne un score par action ;
- **une comparaison** : saboteur contre honnête, sur des tâches que la sonde n'a pas vues.

## 2. Les mots du tableau

**Aire sous la courbe.** On range toutes les actions par score de la sonde. L'aire est la probabilité qu'une action saboteuse tirée au hasard ait un score plus haut qu'une action honnête tirée au hasard. 0,5 : la sonde ne sépare rien ; 1 : elle sépare tout. Une aire ne dit pas *pourquoi* la sonde sépare.

**Plancher de directions au hasard.** Une aire de 0,6 peut venir de n'importe quelle direction, parce que le saboteur et l'honnête diffèrent de mille façons. On tire donc des centaines de directions au hasard, on calcule leur aire, et l'on prend le quantile 0,95 : c'est la barre qu'une sonde doit franchir pour dire qu'elle lit quelque chose de **plus** qu'une direction quelconque.

**« Au-dessus » et « D ».** La sonde est « au-dessus » si la **borne basse** de son intervalle de confiance dépasse le plancher (ou, selon le texte, si la borne basse de D = aire − plancher est positive). On juge la borne basse, pas l'aire elle-même, pour ne pas crier victoire sur le bruit.

**Intervalle et niveau.** Un intervalle est obtenu en tirant au hasard des tâches avec remise (par blocs de tâches, pour respecter le fait que les actions d'une tâche se ressemblent). Quand plusieurs sondes sont jugées ensemble, le niveau est relevé (0,975 pour deux, environ 0,983 pour trois) : c'est la correction pour comparaisons multiples.

**« Non détecté à cette puissance ».** C'est la seule façon permise de dire un nul. Elle ne veut pas dire « la sonde ne sépare pas » : elle veut dire qu'avec ce nombre de tâches, une aire vraie modeste n'aurait pas été vue. L'**aire minimale détectable** (P3) dit jusqu'où le nul exclut quelque chose.

**Effet en log10 du coût.** Pour le coût déclaré, on compare par tâche la moyenne du logarithme décimal du coût : un effet de 1 veut dire dix fois plus cher, de 2 cent fois.

**Base « mots et coût ».** Un lecteur qui ne voit que le texte (les mots et le coût déclaré). Si elle suffit à voir l'organisme, une sonde qui le voit aussi n'apporte rien de propre : c'est pourquoi, par la décision N-063, le critère 3 de G0 n'est jugé **qu'aux doses où cette base échoue**.

**Témoins.** Un témoin de consigne (un honnête qui porte un texte de même longueur) et un adaptateur témoin (entraîné de la même façon, sans sabotage) servent à séparer l'effet du sabotage de l'effet d'avoir une consigne ou un adaptateur.

**Ligne gelée.** Chaque texte scellé avait, avant la course, une table d'issues lue de haut en bas ; la première qui s'applique est le verdict. Le lecteur neuf ne choisit pas : il vérifie laquelle s'applique.

**Réserve.** Une phrase qui accompagne le verdict sans le changer. Elle se cite toujours avec lui.

**Exploratoire, non opposable (R-522).** Une lecture faite pour régler une course suivante ; ses chiffres ne peuvent servir ni de seuil, ni de preuve, ni entrer dans un papier.

## 3. Ce que dit chaque essai, en une phrase

1. **P3** : sur l'organisme à consigne cachée, deux sondes génériques ne franchissent pas leur plancher — nul, à cette puissance ; le saboteur gonfle bien son coût.
2. **P3-bis** : quand on plante un saboteur évident (consigne et persona visibles), la même chaîne le voit ; le signal tient surtout à la persona, la consigne seule n'est pas vue.
3. **Table A de T0.6 (7b)** : l'organisme à adaptateur gonfle son coût sans consigne, de plus en plus avec la dose ; à la plus petite dose, on ne le distingue pas de l'honnête.
4. **Base « mots et coût »** : le texte seul voit l'organisme à adaptateur aux trois doses hautes ; seule la plus petite dose reste « qualifiée » pour juger les sondes.
5. **7a** : course de réglage ; rien d'opposable.
6. **Étape B** : à la seule dose qualifiée, l'organisme ne sabote pas de façon établie ; aucune dose n'est donc jugeable et la porte G0 lit le critère 3 comme non tenu. Sur l'organisme à consigne cachée, la sonde de dissimulation est au-dessus, mais elle s'allume aussi sur les témoins (réserves R1 et R3).
7. **Étape B bis** : une sonde apprise sur les épisodes mêmes sépare très bien, même à texte égal, mais l'adaptateur seul, posé sur des textes honnêtes, la déplace autant : à la lecture dure, rien n'établit qu'elle lit le sabotage plutôt que l'adaptateur.
8. **Barreau 6** : additionner les scores d'un épisode bat leur maximum, mais aussi sur les témoins ; le gain n'est propre ni au sabotage ni à la sonde.
9. **Barreau 7** : sur les activations publiées d'un banc de collusion, nos sondes reproduisent le résultat publié ; cela valide la chaîne sur un cas facile (collusion instruite, contexte visible), pas la détection du diffus.
10. **Lentilles** : expérience hors programme ; les lentilles publiques et les nôtres reproduisent « en partie » ; la lecture contre ablation reste « autre » à la couche 15. Rien n'entre dans le programme sans un nœud de ta part.
11. **Témoin de Bailey** : notre outillage reproduit l'attaque publiée contre une sonde sur le banc des auteurs, au régime publié ; c'est un témoin d'outillage, pas une mesure sur nos organismes.
12. **Saboteur à budget, course 1** : arrêtée avant le saboteur, parce que l'oracle n'était pas centré sur l'honnête ; le mécanisme (ancrage de chaque trajectoire sur son passé) est compris ; rien n'est dit du saboteur.

## 4. Le fil, sans chiffre

Les essais racontent la même histoire, par trois côtés.

- **La chaîne de mesure marche** quand le signal est évident : témoin planté (P3-bis), banc de collusion publié (barreau 7), attaque publiée (Bailey). Un nul de nos sondes n'est donc pas, à lui seul, une panne de l'outil.
- **Sur nos organismes, ce que voient les sondes n'est jamais isolé du sabotage** : tantôt le texte planté (la persona), tantôt la consigne présente, tantôt l'empreinte de l'adaptateur (étapes B et B bis, barreau 6). Les témoins s'allument comme le saboteur.
- **La fenêtre utile est vide sur l'organisme à adaptateur actuel** : là où il sabote vraiment, le texte seul suffit à le voir ; là où le texte ne le voit pas, il ne sabote pas de façon établie. Le critère 3 de G0 ne peut donc pas y être tenu : il faut un organisme qui sabote en restant discret pour le texte.

Ce que ces verdicts **ne disent pas** : que la boîte blanche échoue en général ; que les sondes lisent ou ne lisent pas l'intention ; quoi que ce soit d'une sonde qui n'aurait pas vu d'étiquettes, d'un autre organisme ou d'un autre mode de sabotage. Aucun ne franchit de porte.

## 5. Pour vérifier toi-même un chiffre

Chaque ligne du tableau cite ses sources : chemin, branche quand ce n'est pas `main`, empreinte complète. Pour en vérifier une : `git show <branche>:<chemin> | sha256sum`, puis comparer au compagnon `<chemin>.sha256`. Pour refaire tout le tableau : `python3 -I outils/extraire_tableau_verdicts_v1.py <dépôt> sortie.md journal.json`, après avoir récupéré les branches citées ; la sortie doit être identique au corps du tableau.
