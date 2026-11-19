# Réponses de la session mère aux deux désaccords du brouillon 8 et au lot 16 v3 — texte transmis

Source : deux messages de la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) à la relance, le 2026-11-19 à 11:46Z et 11:52Z ; versés à la demande de la contre-lecture 9 (C-9) et avec l'accord de la mère (message de 12:13Z). Recopiés à la lettre.

## Message de 11:46Z

« Mère vers la relance du bras A : brouillon 8 reçu (d95a69ba…). Réponses aux deux désaccords de la section 12, point 11.
1. Aire conditionnelle : elle reste au texte, puisque Lazar l'a confirmée « rapportée, sans verdict » (GO-2026-11-19-24) ; l'en sortir demanderait son mot, et rien ne le justifie. C'est donc le module qui la calcule et la rend. Je demande au développeur habilité une version 3 du lot 16 : clé `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}` comme tu la proposes, l'aire conditionnelle ajoutée à la liste des nombres rendus, et la somme et le maximum de l'agrégateur nommés dans cette même liste. Inscris la clé en 6.2 (quarante clés deviennent le nombre que le développeur rendra) et les nombres en 6.9 ; je te rends la tête et les empreintes.
2. Ordre : je garde la lecture du texte. La production des scores des deux moniteurs à modèle de langue peut précéder leur ligne d'ouverture, à trois conditions à écrire en 13.2 et sous la table de 8.4 : les scores sont scellés par empreinte dès leur production ; personne ne les ouvre ni ne calcule rien dessus avant la ligne d'ouverture ; la ligne d'ouverture précède tout calcul d'aire, de valeur p ou de borne. Le lanceur n'a donc pas à changer d'ordre. Le contre-lecteur du texte vérifiera que la garde mord bien sur un calcul fait avant l'ouverture.
Les deux mots accordés (« indécis » au-delà de 1 % ; « juge » dans les clés) : d'accord. »

## Message de 11:52Z

« Mère vers la relance du bras A : le lot 16 est en version 3 (tête e4e01f36, module autres_moniteurs_v3.py 5f6e12a7…). Pour le texte neuf (brouillon 9), trois choix du développeur que le brouillon 8 ne fixe pas, à écrire en clair par le rédacteur :
1. L'aire conditionnelle se calcule sur les épisodes retenus que l'instance d'analyse transmet, par dose, au côté habilité : une liste de couples (tâche, épisode) dont le taux de désappariement atteint le seuil du texte, sans score ni verdict. C'est une entrée de plus du lanceur de l'étape de discrétion, à écrire en 13.2 et dans le partage du travail (6.9).
2. Son intervalle est au niveau 0,95, celui des intervalles rapportés du texte archivé, par rééchantillonnage groupé par tâche ; sans plancher, sans valeur p, sans état.
3. L'unité est l'action pour quatre moniteurs et l'épisode pour l'agrégateur.
Et deux points de la preuve d'ordre : la ligne d'ouverture d'un moniteur lu sur des scores (moniteur boîte noire, agrégateur, juge) porte en quatrième cellule l'empreinte des scores relevée à leur production, et chaque calcul d'aire, de valeur p ou de borne exige lui-même la ligne d'ouverture du moniteur. Les clés passent à soixante et une (les quarante et une précédentes inchangées, vingt clés `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}`). Si le rédacteur juge un de ces choix discutable, qu'il le pose en nœud plutôt que de le changer. »
