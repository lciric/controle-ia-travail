# Audit de symétrie (règle R4) de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — résumé sans résultat — v1

Ce résumé est écrit pour une session qui ne doit voir aucun résultat. Il ne porte aucun chiffre de résultat, aucun état, aucune issue, ni le sens d'aucune mesure. Les seuls nombres sont ceux des noms de fichiers, des identifiants et de la date. Le rapport complet, avec les chiffres, est à côté (`audit-symetrie-bbis-v1.md`) : il est réservé à Lazar et aux lecteurs exposés.

- **Objet** : l'audit de symétrie que le préenregistrement `prereg/T0.7-etape-B-bis-v1.md` gèle, que le verdict de cette étape déclare dû et non fait, et que Lazar a demandé en acceptant ce verdict (GO-2026-11-19-44), avec en plus la vérification des gardes d'égalité au bit près entre l'ancien et le nouveau chemin de calcul.
- **Date (UTC)** : 2026-11-19.
- **Qui audite** : sous-agent neuf, modèle Claude Fable 5.2, qui n'a écrit ni le préenregistrement, ni ses addenda, ni le code, ni l'analyse, ni le verdict.

## Conclusion

**Transmissible avec réserve.**

## Ce qui a été fait

1. **Relecture des prédicteurs triviaux** (longueur notée, rang du pas, mention étendue) : faite, conforme. Le code les calcule comme le texte gelé le demande ; un recalcul de contrôle, à partir des seuls champs du fichier des mesures de la course de confirmation, rend exactement les valeurs du fichier de lecture.
2. **Relecture de l'alignement des clés et des étiquettes** : faite, conforme. Lecture du code de l'instance et du code de lecture ; puis contrôles par programme : cohérence interne du fichier des mesures, accord avec le fichier des textes, plis recalculés par leur graine, clés et tâches écrites à côté des scores égales à ce que le plan gelé prévoit, étiquettes d'apprentissage, tirages du réétiquetage rederivés de leurs graines, composition des cellules décisives, alignement clé à clé des deux côtés de chaque comparaison entre une série d'origine et une série relue.
3. **Échantillon de vingt clés d'action par condition concernée** : fait, conforme. Tirage par une graine dérivée de `numpy.random.SeedSequence`, écrite dans le rapport complet (règle R9) ; seuls les champs du fichier des mesures ont été lus pour ces clés ; chaque clé est à la place que le plan lui donne.
4. **Gardes d'égalité au bit près entre les deux chemins de calcul** (demande de Lazar) : vérifiées par programme sur les fichiers de la course. Les gardes ont joué pendant la course, sur des épisodes tirés par la graine prévue, et leurs sorties écrites sont conformes au texte gelé, cas sains comme artefact.

Aucun contrôle n'est non conforme. Aucune faute de chaîne n'a été trouvée.

## La réserve

Elle porte sur la portée de la preuve d'égalité entre les deux chemins, non sur un défaut constaté :

- la garde de la course, conforme au texte gelé, ne porte que sur une partie des épisodes et sur une partie des états du chemin neuf ; les autres états ne sont couverts que par un raisonnement sur le code, non par une comparaison ;
- la comparaison est faite en mémoire, avant l'écriture des séries relues ;
- l'audit n'a pas pu refaire lui-même la comparaison à l'octet : les activations de la course n'ont pas été gardées, et rouvrir les scores de sonde ne l'aurait pas permis ; la refaire demanderait une marche nouvelle sur carte, donc un devis et le mot de Lazar ;
- la pièce où la course a écrit le résultat de ses gardes n'est citée par aucune ligne du registre propre et n'a pas été ouverte par la chaîne de lecture ; elle est ancrée par son compagnon et par l'empreinte du manifeste de la course ;
- le commit de la course est un commit local, jamais poussé par construction : le code n'a été relu qu'à son parent et dans le dépôt d'aujourd'hui, où ses empreintes sont celles de la fiche de code en vigueur.

L'audit écarte une faute de chaîne ; il ne dit rien de ce que lisent les sondes, qui reste porté par le verdict et ses réserves.

## Ce que l'audit n'a pas fait

- Il n'a changé aucun état ni l'issue, et n'a produit aucune mesure nouvelle à valeur de lecture.
- Il n'a lu aucun score de sonde. Écart de moyens déclaré : les fichiers de scores ont été ouverts pour y lire les seuls tableaux de clés, de tâches, d'étiquettes d'apprentissage, de tirages du réétiquetage et de validité, que la course a écrits dans les mêmes archives ; pour les autres tableaux, seul l'en-tête (forme et type) a été lu, jamais une valeur.
- Il n'a rien commité, rien dépensé, loué aucune machine ; aucun outil n'a refusé.
- Les interdits de lecture de son mandat ont été tenus.

## Preuves

Programmes et sorties dans le bloc-notes de la session, hors du dépôt, cités avec leurs empreintes dans le rapport complet (§ 7). La sortie des contrôles recopie des valeurs du fichier de lecture : elle n'est pas pour une session sans résultat.
