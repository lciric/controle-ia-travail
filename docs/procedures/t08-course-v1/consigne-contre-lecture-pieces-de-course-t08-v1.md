# Consigne — contre-lecture des pièces de la course de la base boîte noire (T0.8) — v1

- **Nature** : mandat (classe C) d'une contre-lecture de trois pièces de classe A. **Écrite** le 2026-11-22 par leur auteur (modèle B). **Pour** : un sous-agent neuf d'un autre modèle, lancé par la session mère, qui n'a écrit ni le texte de T0.8, ni son code, ni ces pièces. Ce peut être le contre-lecteur 8 du texte, qui le connaît déjà.
- **Ce que tu rends** : un rapport scellé, `prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon1-cl1.md` — un verdict par pièce, tes constats numérotés (bloquant, majeur, mineur), et pour chaque correction le texte ancien et le texte nouveau. Tu vérifies ensuite les corrections.

## 1. Les trois pièces, sous `docs/procedures/t08-course-v1/`

1. `ordre-course-t08-v1-brouillon1.md` — l'ordre de course. Brouillon 1 : il fixe la séquence, les contrôles, les arrêts, la dépense et les rôles ; il n'est pas exécutable, les commandes venant au brouillon 2.
2. `consigne-lecteur-t08-v1-brouillon1.md` — la consigne de l'agent qui joue la lecture sur processeur.
3. `consigne-juge-verdict-t08-v1-brouillon1.md` — la consigne de l'agent qui applique les tables D et F.

À lire aussi, pour la cohérence, sans la juger comme une pièce de classe A : `consigne-chaine-de-lancement-t08-v1.md` (mandat du développeur de la chaîne de lancement).

## 2. Ce que tu lis, et rien d'autre

Ces quatre fichiers ; le texte de T0.8, `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon14.md` (branche `prep/t08-texte-complet-fable-v1`) — « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt », « Machine, devis et dépense », « Ordre des lectures et embargo », « Depuis le gel du 10 novembre » ; dans `registres/go.md`, les lignes `GO-2026-11-10-12`, `GO-2026-11-22-77`, `GO-2026-11-22-79`, `GO-2026-11-22-93`, `GO-2026-11-22-122` ; dans `CLAUDE.md`, les règles R1 à R14, « Récupérer ce qui est récupérable » et « Une panne technique n'est pas un résultat » ; du rapport du premier développeur du code (`docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md`, branche `prep/t08-code-compte4-v1`), le § 6.

**Jamais** : un fichier de données, de diagnostic ou de run ; un verdict ; un score de sonde ; T0.7 ou P3-bis ; une pièce du saboteur à budget, du bras A ou du bras d'attaque ; une recherche récursive large. Un refus d'outil n'est ni rejoué ni contourné. Avant de commencer, tu envoies ta ligne d'inscription à la liste « qui a lu quoi » à la session mère.

## 3. Ce que tu vérifies

1. **Aucune règle neuve.** Chaque pièce dit ne rien ajouter au texte scellé. Cherche ce qui en ajouterait : un seuil, un arrêt, un critère de lecture, une liste, une tolérance. L'ordre fixe un relevé toutes les trente minutes : est-ce un geste de service ou une règle ?
2. **Fidélité à la « Liste d'arrêt » et à « Machine, devis et dépense »** : bornes de l'offre, plafond de 120 USD toutes tentatives comprises, compte rendu à 40 USD, aucune carte H200, aucun couperet de temps, deux heures sans progression, destruction par identifiant.
3. **Fidélité aux tables D et F** dans la consigne du juge : ordre de lecture, « chaque ligne est écrite », réserves qui ne changent aucune ligne, ligne D1 quand il n'y a pas de lecture, ce qui se rapporte à côté de la table F.
4. **Cloisonnement** : l'exécutante ne lit aucune sortie ; le lecteur n'ouvre du résultat que l'audit R4 ; ni le lecteur ni le juge n'ont vu de résultat de sonde ; rien ne va du côté de ceux qui conçoivent un saboteur. Y a-t-il un chemin par lequel un résultat fuit ?
5. **R3 et R4** : aucune phrase ne vise un signe ; l'audit R4 est le même dans les deux sens ; une prédiction réfutée s'écrit comme les autres.
6. **R5** : chaque garde nommée a-t-elle son cas sain et son artefact, dans l'ordre ou dans la consigne de la chaîne ?
7. **Ce qui manque** : un préalable, une étape, un arrêt, une pièce que la course exige et que personne n'a à écrire. En particulier : l'ordre est-il assez précis pour qu'un brouillon 2 n'y ajoute que des commandes ?
8. **Rôles (R13)** : auteur du texte, exécutante, lecteur, juge sont-ils bien distincts, et la consigne du juge exclut-elle ceux qui doivent l'être ?
9. **Panne technique et relance** : une seule relance, si aucune lecture n'a eu lieu ; la borne de 400 jetons n'est jamais une panne.

## 4. Ce que tu ne fais pas

Tu ne proposes aucun changement au texte de T0.8 : un défaut que tu y verrais se dit comme un nœud pour Lazar. Tu n'écris aucune commande : elles viennent du développeur de la chaîne.
