# Vérification des corrections de la v5 du préenregistrement court « papier dopamine » et de la proposition v2

- **Vérificateur** : le même contre-lecteur, modèle Opus 5.5 (`claude-opus-5-5`), sous-agent. Pièce de classe A. Aucun appel payant, ni commit ni poussée.
- **Date (UTC)** : 21 novembre 2026, 06:23 (`date -u`).
- **Relus** (empreintes recalculées, égales à leurs compagnons) :
  - v5 : `preenregistrement-court-papier-dopamine-v5-brouillon.md`, `56a699d177a9a1570bf0a810b7a74a0ff4ed94e5baf5be01f5d8f48d855c843f` ;
  - différentiel v4 → v5 : `2e3c9b0a1277dcdb6d364b6844a21f93b386556b757a314a9be6594fafb64677` ;
  - proposition v2 : `proposition-sondes-et-lots-lisibles-v2.md`, `03f6a67143753cbcb79a33ab13fc724640092895243d0694625cfe83274b53ff` ;
  - différentiel de la proposition, v1 → v2 : `2ec325ae7e6371af515d47514d241f0e758af312a3fc1f3fd9481cf7291d219f` ;
  - mon rapport de la contre-lecture 4, `21b54a97…`, intact.
- **Différentiels** : je les ai recalculés tous les deux ; ils sont identiques aux fichiers fournis, en-têtes de date mis à part.
- **Validateur** : `problemes()` sur la v5 renvoie une liste vide.

## Verdict

**À corriger, sur un seul point** (W12, ci-dessous) : la règle de correction des analyses secondaires, que le concepteur m'a lui-même soumise. Une fois W12 portée, le texte est conforme et peut être scellé dès que le directeur a tranché VO-17 à VO-20 et approuvé la liste lisible (VO-16). Un seul contrôle suffit.

## Les corrections de la contre-lecture 4

- **W1 à W11** : chaque texte neuf figure une seule fois dans la v5, à sa place, à la lettre. Cela vaut aussi pour la règle 6 de la garde (W1), aux deux endroits de W8, et pour la ligne d'arrêt de W11.
- **Hors de W1 à W11, rien que de la tenue de pièce** :
  - titre, avertissement de tête, dates, commit ;
  - documents qui font foi : mon rapport, la proposition v2 ;
  - « six règles » dans la phrase qui introduit la garde ;
  - VO-11 et VO-16 mis à jour ;
  - VO-17 à VO-20 ajoutés : ce sont mes quatre points du directeur, rendus fidèlement ;
  - la table de traitement, et la remarque sur Holm.

  Aucun énoncé, critère ni seuil d'origine ne change. La conséquence écrite sous W10, une barre de 5 000 épisodes honnêtes d'étalonnage par tranche de longueur, est juste. Elle est à porter au devis.
- **P-1 à P-3** : portées à texte exact dans la proposition v2.
- **P-4** : l'écart d'un mot (« v5 » au lieu de « v4 ») est acceptable, puisque la v4 est remplacée. Les ajouts sont cohérents avec la v5 :
  - statut « sous conditions C-1 et C-3 » aux trois sondes ;
  - couche du verdict fixée à 15, les couches 7 et 23 rapportées ;
  - question 3 réécrite selon W8, les secondaires au niveau 1 − 0,05/2.
- **Reste de la proposition v2** : les numéros d'entrée sont ajoutés aux renvois au registre, l'heure est corrigée et le voisinage du barreau 8 est signalé. C'est de la tenue de pièce.

## Le premier point contesté : la ligne 1981 du registre

**Le concepteur a raison ; je retire ma remarque.** À la contre-lecture 4, je n'avais lu que les 600 premiers signes de la ligne 1981 (entrée R-2023). Je viens de relire, à l'empreinte actuelle du registre (`3f5807bd…`), le seul passage autour du 884ᵉ signe. Il porte bien « 24 celui du fichier léger (`701f73bd…`) ». Le renvoi de la proposition était juste. Rien d'autre n'a été lu dans cette ligne.

## Le second point : les trois mentions de Holm antérieures à la v4

- La mention de la statistique de chemin (« En second, avec correction de Holm… ») porte sur des règles rapportées sans critère de lecture. Elle peut rester telle quelle.
- La mention de l'étape 3 (« Tout le reste est secondaire, corrigé par Holm à l'intérieur de chaque mode ») couvre des quantités qui, elles, ont un critère par intervalle : P5, et « bat » ou « ne bat pas » telle base pour chaque sonde, couche et mode. La règle de décision y reste donc ambiguë, pour la raison même que W8 relevait. Correction W12.
- Le rappel dans la section du mode tenu à l'écart renvoie à l'étape 3. Il suit W12 sans changer.

**W12. Les analyses secondaires de l'étape 3.**
- Ancien : `Tout le reste est secondaire, corrigé par Holm à l'intérieur de chaque mode.`
- Neuf : `Tout le reste est secondaire, corrigé par Holm à l'intérieur de chaque mode : pour toute quantité secondaire jugée par une borne d'intervalle, la décision se prend sur la valeur p de l'épreuve unilatérale qui correspond à cette borne (pour une équivalence, la plus grande des deux valeurs p unilatérales), ajustée par Holm sur la famille des quantités secondaires du mode, déclarée à l'addendum ; l'intervalle rapporté est l'intervalle à 95 % non ajusté, marqué comme tel.`

## Points du directeur, avant le scellement

Ils sont dans la v5 :
- VO-16 : approbation de la liste lisible ;
- VO-17 : épisodes réservés du mode tenu à l'écart ; ma recommandation est (a), confiance 0,8 ;
- VO-18 : ce qui est servi à Lazar sur ce mode ;
- VO-19 : les trois questions de la proposition ;
- VO-20 : routage des résultats loin du côté moniteurs du barreau 8.
