# Erratum 1 à la note d'accompagnement de la configuration de génération du calage de la porte G1 (v1)

- **Classe C.** Écrit par l'auteur de la note (Claude Fable 5.2, sous-agent de la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`), le 21 novembre 2026 à 19:40 UTC (`date -u`), avant toute remise.
- La note (`322aaa85d0a8b074fc1946b9f166e674b65e60b2a8128301e87d606312043707`) et la configuration (`4bfdd98d2226abe1fc173a68e62700039f14fc8d2b3bb2b2d6ba6bbf7082079d`) restent telles quelles (R12). Aucune valeur de la configuration ne change.

## 1. Une source désignée n'est nommée ni dans la note ni dans le fichier

La contre-lecture des trois choix du banc fermé (`docs/notes/banc-ferme-choix-contre-lecture-fable-v1/contre-lecture-trois-choix-banc-ferme-fable-v1.md`, `bc9ec0fdb7e4ad2baa39e3b21728bb0af301073a7abfe0caf3d558fc4c25f2fb`) a été lue, pour son choix 2 (l. 112 à 129), et suivie. Ses cinq réserves d'écriture, et ce qui y répond :

| Réserve du choix 2 | Ce qui y répond |
|---|---|
| 1. Le nom ne suffit pas : révision complète, absence d'adaptateur, variables du gabarit et date, bibliothèque, version, précision (l. 123) | les entrées `modele.revision`, `modele.adaptateur`, `gabarit_de_conversation.variables`, `pile_d_inference.bibliotheque`, `pile_d_inference.versions` et `pile_d_inference.precision_des_poids` |
| 2. L'ordre s'inverse : un fichier scellé avant la course, que le calage copiera (l. 124) | le fichier lui-même ; son acceptation suit la chaîne du mot de Lazar (contre-lecture, corrections, vérification, scellement) |
| 3. Agent nu ici, adaptateur dans les organismes de T0.6 : à dire dans le résultat (l. 125) | hors du fichier ; le brouillon 11 du banc le porte (l. 83) |
| 4. Abstention de l'agent et nombre minimal de paires (l. 126) | hors du fichier |
| 5. Portée : la mesure vaut pour ce modèle (l. 127) | hors du fichier |

## 2. Une omission dans le fichier

La rubrique « pieces_lues_sans_etre_sources » de la configuration ne nomme pas cette contre-lecture. C'est un oubli de traçabilité : aucune valeur n'en dépend. À ajouter à la version suivante du fichier, que la contre-lecture appellera sans doute.
