# Contrôle du différentiel v6 → v7 des critères et de la note du juge de sélection, et de la fiche — v1

- **Contre-lecteur, modèle O** : le même que pour `ee578a61…`, `86a9813a…` et `a9793588…`. Je n'ai écrit ni les pièces v7, ni la fiche, ni aucune carte. Écrit le 2026-11-20 (`date -u` : 2026-11-20T03:19:20Z). Processeur seul, aucune dépense, aucun appel de modèle, aucun réseau. Rien n'est écrit dans le dépôt.
- Dossiers : V6 = `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v6/` ; V7 = `…/juge-selection/criteres-v7/`.

## Verdict

**Conforme après corrections.**
- Les deux textes v7 sont conformes et scellables tels quels.
- **La fiche du § 6 du rapport est juste, au format, et peut partir à Lazar maintenant.**
- Les trois seules corrections portent sur la demande de configuration pour la mère, au § 5 du rapport (C1 à C3). Elles ne touchent aucun texte scellable. Elles ne retiennent ni la fiche ni le scellement. Elles sont à faire avant que la mère écrive le manifeste.

## 1. Empreintes et rejeu

**Empreintes.** `sha256sum -c` passe sur chaque compagnon :
- le mandat `V6/mandat-redacteur-corrections-criteres-v7-note-v7-v1.md` (`0c366493…`) ;
- les deux textes v7, critères (`6af793a2…`) et note (`bbd71b7c…`) ;
- les deux fichiers de remplacements, les deux journaux et les deux différentiels ;
- le rapport (`2a12a78f…`).

**Outil.** J'ai rejoué `remplacer_texte_exact_v1.py` (`391db990…`, recalculé sur ma copie) sur des copies des v6 (`6ea6f701…`, `5bcae2d3…`) :
- critères : 6 remplacements, sortie **`6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f`** ;
- note : 5 remplacements, sortie **`bbd71b7c998866ec249556fe7803015c54aac4081dffc4e5084588819bc98a26`**.

Les deux sont égales à l'octet aux pièces versées. J'ai lu les deux différentiels ligne à ligne : rien d'autre que T1, M1, les titres et les lignes « Version 7 ».

## 2. F1, T1 et M1 sont portées

- **T1** (i) à (vi) : mot pour mot, sauf le numéro de la pièce sœur, qui est « v7 » au lieu de « v6 ».
- **M1** : critères, annexe B, à la lettre ; rapport, § 5, point 4, à la lettre.
- **F1** : dans la fiche, la décision 5 a trois options, (a), (b) et (d). La phrase est ajoutée à l'enjeu, et la ligne « option (c) … non posée » est présente.

## 3. Les écarts déclarés tiennent

- **« v7 » au lieu de « v6 » pour la pièce sœur** : c'est juste. Mon texte nommait la pièce en vigueur au moment où je l'écrivais. Le garder aurait fait renvoyer les critères v7 à la note v6, remplacée.
- **Quatre options à la décision 5 de la note v7.** Cela ne gêne pas, à deux conditions, toutes deux remplies :
  - la fiche est la pièce posée, et elle est au format ;
  - la note dit elle-même, dans sa ligne « Version 7 », que la fiche fait foi pour ce qui est posé.
  La note est une pièce de conception scellée, non une décision. Ses quatre options y restent comme analyse. Les mettre à trois est possible à une version suivante ; rien ne l'exige.
- **« note v7 » dans la ligne « non posée »** : c'est juste, c'est la note v7 qui porte l'option (c).
- **`criteres_sha256` = `6af793a2…`** : c'est juste si la v7 est scellée telle quelle. Le programme refuse toute autre empreinte (`_h1`).
- **Renvois historiques laissés** : cela tient. Ce sont les lignes « Version 5 » et « Version 6 », les critères § 15 et § 16, la note § 10.3 et § 10.4. La ligne « Version 7 », en tête, dit la lettre en vigueur, et aucun renvoi en vigueur ne mène plus à une v5 ou à une v6.
- **Ce que le rédacteur n'a pas vérifié** : je l'ai vérifié moi-même, au § 5.

## 4. La fiche du § 6

**Elle est juste et exacte sur les défauts et les horloges.**
- Le 21 vers 14:41Z échoient les défauts posés le 19 (R-3890, que j'ai vérifiée mot pour mot sur `origin/main` au contrôle précédent) :
  - décision 1 : le rejeu seul, sans adoption ;
  - décision 2 : le veto à la lettre de la v3 (option (c)).
- Tout ce qui est neuf a 48 heures à compter de la pose de la fiche : les conditions neuves de la décision 1 ; l'option (a) de la décision 2 ; la décision 3, que R-3890 nomme sans défaut ; les décisions 4 et 5 ; les huit confirmations, dont les six premières sont dites portées le 19 sans défaut écrit.

**Elle est au format.** Chaque décision a sa phrase, son enjeu, deux ou trois options avec avantage et inconvénient, une recommandation avec sa confiance, et un défaut. Elle s'ouvre sur le verdict, la réserve sur R-3890 et le point R-4050. Elle ne nomme que les pièces v7, et aucun identifiant de modèle.

## 5. La demande du § 5 : vérifiée sur le programme et la statistique

**Les seize clés.** `CLES_MANIFESTE` dans `V5/assemblage_selection_v4_v2.py` (lignes 49 à 53) contient :
- `identifiant_course`, `usage`, `ligne_accord`, `criteres_sha256` ;
- `nombre_vise`, `veto_par_titulaire`, `suppleantes`, `filtre_veto`, `plafond_veto` ;
- `regime_items`, `seuil_accord`, `lignee_reconnue_declaree`, `emploie_lectures_v2` ;
- `familles`, `hors_choix`, `cartes_attendues`.

C'est exactement l'ensemble du tableau du § 5, point 4. Le programme refuse tout manifeste dont les clés diffèrent.

Les valeurs proposées passent les contrôles de `valider_manifeste` :
- `suppleantes` 4 et `nombre_vise` 9 : entiers ;
- `filtre_veto` « lignee » et `plafond_veto` null : permis ;
- `seuil_accord` 0,75 : dans ]0, 1] ;
- les deux booléens : vrais booléens ;
- `veto_par_titulaire` « selon_titulaires » : permis.

**Les étiquettes de lignée.** La statistique de famille (`bb2fa4a8…`, § 0, ligne 22) donne les étiquettes `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra` et `prop-carbon`, écrites dans `meta` → `proposeur`. Sa propre réserve est qu'elle ne les a pas vues sur le fichier.

Le programme exige que la même étiquette apparaisse partout :
- comme clé de `familles` ;
- comme valeur de la table des espèces, pour le filtre du veto (ligne 508) et pour les gardes (ligne 955) ;
- dans le champ `lignee` de chaque lecture (ligne 164) et de chaque liste de juge (ligne 1232).

Le point 5 du rapport le dit juste. Il suffit, avec la règle d'arrêt.

**La demande suffit à la mère**, avec ses « à lire dans… » et la règle d'arrêt sur les champs de `contenu`, à trois retouches près. Deux de ses « à lire » ont une réponse dans les pièces, et l'un pousserait vers un dossier interdit :

- **C1** — `identifiant_course` : « à lire sur ce dossier, aucune pièce lue ne le nomme ». C'est faux, et cela enverrait la mère regarder sous `archives-reponses-modeles/`. La statistique de famille, § 2, point 1, nomme le dossier : `auto-conception-course-v9-2026-11-19-v1`.
  - Ancien : « la chaîne choisie par la mère ; à défaut, le nom du dossier d'archive de la course v9 : à lire sur ce dossier, aucune pièce lue ne le nomme ».
  - Nouveau : « la chaîne choisie par la mère et scellée avant l'ouverture ; à défaut, le nom du dossier d'archive de la course v9, tel que la statistique de famille le cite (§ 2, point 1) : `auto-conception-course-v9-2026-11-19-v1`, sans ouvrir ce dossier ».
- **C2** — `ligne_accord`.
  - Ancien : « vide pour un rejeu ; la forme du vide (chaîne vide ou null) : à lire dans `assemblage_selection_v4_v2.py` ».
  - Nouveau : « vide pour un rejeu : chaîne vide ou null, l'une et l'autre acceptées ; le programme ne la lit que pour l'usage « course » (`assemblage_selection_v4_v2.py`, ligne 123) ».
- **C3** — `familles`, noms des familles.
  - Ancien : « les noms des familles : à lire dans `assemblage_selection_v4_v2.py` ou ses essais, aucune pièce lue ne les fixe ».
  - Nouveau : « les noms des familles sont libres : le programme ne compare que leur égalité ; `prop-opus` et `prop-fable` reçoivent la même chaîne, chaque autre étiquette une chaîne à elle ».

**Remarque, sans correction.** Après le dépôt des lectures, la statistique de famille scellée demande à la mère un troisième fichier, la « correspondance » (statistique, § 2, point 3). Il ne s'écrit pas avant l'ouverture. Il peut être nommé dans la demande, pour mémoire.

## 6. Ce que j'ai lu, et incidents

- **Lu en entier** : le mandat v7 ; le rapport ; les deux différentiels.
- **Lu en partie** : `V5/assemblage_selection_v4_v2.py`, lignes 49 à 53 (`CLES_MANIFESTE`), et les lignes que donnent mes recherches de motifs sur ce seul fichier ; la statistique de famille, par recherche de motifs sur le fichier nommé.
- **Mes copies** : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-juge-v4/controle-v7/`.
- **Jamais touché** : aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucun fichier, branche ou ligne interdits. Aucun `git show` dans ce contrôle.
- **Aucun refus** de permission, de classifieur ni de garde. Une commande simple par appel, aucun heredoc, aucun code en ligne.

*contre-lecteur, modèle O*
