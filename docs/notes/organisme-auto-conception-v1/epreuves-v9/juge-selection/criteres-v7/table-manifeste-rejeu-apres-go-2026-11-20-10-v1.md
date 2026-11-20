# Table du manifeste d'ouverture du rejeu, après GO-2026-11-20-10 — v1

- **Contre-lecteur, modèle O** : le même que pour les contrôles des critères v4 à v7. Écrit le 2026-11-20 (`date -u` : 2026-11-20T04:53:22Z). Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt.
- **Ce que cette pièce est.** Une table de lecture, valeur par valeur. Elle ne remplace pas le manifeste, que la mère écrit et scelle. Elle ne devine rien : là où une valeur dépend d'une source, la source est nommée.

## Sources, vérifiées

- **GO-2026-11-20-10** : `origin/main:registres/go.md`, ligne 541, copie `1ca0e651…`.
  - Point (O2) : « Juge, critères v7 : en tête (1) et (3) ; décision 1 (a) ; 2 (a) ; 3 (b) au rejeu et (a) en course ; 4 (b) ; 5 (a) au rejeu ; huit confirmations telles qu'écrites. »
  - Mot de Lazar, vers 04:44Z : « O2 recos ».
- **Critères v7 scellés** : `origin/main:prereg/organisme-auto-conception-v9/juge-selection/criteres-choix-cartes-v9-v7.md`, sha256 **`6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f`**, égale au compagnon sur `main` et à la pièce que j'ai contrôlée.
- **Note v7 scellée** : même dossier, `bbd71b7c998866ec249556fe7803015c54aac4081dffc4e5084588819bc98a26`, égale à la pièce contrôlée.
- **Fiche** : rapport v7, § 6 (`2a12a78f…`).
- **Programme** : `criteres-v5/assemblage_selection_v4_v2.py` (`2f5640da…`, inchangé depuis la v5) :
  - `CLES_MANIFESTE`, lignes 49 à 53 ;
  - `REGIMES`, ligne 47 ;
  - `valider_manifeste`, lignes 113 à 151 ;
  - lecture et lignée reconnue, lignes 173 et 226 ;
  - gardes, ligne 1071.

## Table des seize clés

Chaque valeur passe `valider_manifeste`. Le programme refuse un manifeste dont l'ensemble des clés diffère de ces seize.

| clé | valeur | ce qui la fixe | contrôle du programme |
|---|---|---|---|
| `identifiant_course` | `"auto-conception-course-v9-2026-11-19-v1"`, ou une autre chaîne choisie par la mère et scellée avant l'ouverture | critères v7, § 9, point 1 (« à défaut, le nom du dossier d'archive ») ; le nom vient de la statistique de famille, § 2, point 1, **sans ouvrir ce dossier** (correction C1 du contrôle v6 → v7) | chaîne non vide ✓. Elle fixe `h2`, donc tous les tirages : elle ne change plus après le scellement |
| `usage` | `"rejeu"` | décision 1 (a) | « rejeu » ou « course » ✓ |
| `ligne_accord` | `"GO-2026-11-20-10"` (recommandé) ; `""` ou `null` passent aussi | décision 1 (a), prise sous ce GO ; correction C2 : pour un rejeu, le programme ne lit pas la valeur (ligne 123) | exigée seulement pour « course » ✓. La ligne du GO documente le rejeu sans rien ouvrir pour une course |
| `criteres_sha256` | `"6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f"` | critères v7 scellés sur `main` | non contrôlée par `valider_manifeste`, mais `_h1` exige qu'elle égale l'empreinte du fichier passé par `--criteres` ✓ |
| `nombre_vise` | `9` | critères v7, § 6 (« à défaut, K = 9 ») ; confirmation 6, telle qu'écrite | entier ≥ 1 ✓. Si la mère donne un K d'après la charge (GO-2026-11-19-67), c'est ce K, écrit avec sa ligne dans la pièce qui scelle le manifeste |
| `veto_par_titulaire` | `"selon_titulaires"` | décision 2 (a) : trois cartes à trois titulaires au plus, deux au-delà ; avec les deux lecteurs seuls, V = 3 | permis ✓ |
| `suppleantes` | `6` | décision 2 (a) : la lettre du § 8 des critères (« six suppléantes au plus »), annexe B (6). **Le 4 était le défaut du 19 ; il ne vaut plus** depuis que Lazar a choisi (a) | entier ≥ 0 ✓ |
| `filtre_veto` | `"famille"` | décision 2 (a) : retrait des cartes de la famille du titulaire ; critères § 8 | « famille », « lignee » ou « aucun » ✓ |
| `plafond_veto` | `"nombre_vise"` | décision 2 (a) : plafond au nombre visé ; critères § 8 (consigne R-3876) | « nombre_vise », entier ≥ 0 ou null ✓ |
| `regime_items` | `"ajoutables_oui"` | décision 4 (b) : « ajoutable » compte oui. **Orthographe du programme** (`REGIMES`, ligne 47), non le libellé « ajoutables comptés oui » des critères | doit figurer dans `REGIMES` ✓. Les trois régimes restent joués et rapportés |
| `seuil_accord` | `0.75` | confirmation 5, telle qu'écrite ; critères § 5.3 | nombre dans ]0, 1], booléen refusé ✓ |
| `lignee_reconnue_declaree` | `true` | décision 3 (b), **au rejeu**. En course, ce sera (a), donc `false` dans le manifeste d'une course | booléen ✓. Voir « Gestes », point 3 |
| `emploie_lectures_v2` | `false` | critères, annexe B (« faux, sauf assemblage de lectures v2 ») : le rejeu emploie deux lectures neuves des critères v7 | booléen ✓ |
| `familles` | `{"prop-opus": F, "prop-fable": F, "prop-argon": A, "prop-astra": S, "prop-carbon": C}`, avec F, A, S et C quatre chaînes distinctes, au choix de la mère | critères, annexe B (Opus et Fable dans la même famille, chaque autre lignée dans la sienne) ; noms libres, seule l'égalité compte (correction C3) | objet non vide de chaînes ✓. **Étiquettes à confirmer**, voir ci-dessous |
| `hors_choix` | la liste X6, tirée par la mère par programme avant l'ouverture : **à lire dans la sortie de l'aiguilleur de la course v9**, dont aucune pièce que j'ai lue ne donne le chemin. Elle est attendue vide, voir la réserve 1 | critères, § 2, X6 | liste de chaînes ✓ |
| `cartes_attendues` | `94` moins la longueur de `hors_choix` ; donc `94` si la liste est vide | décision 1 (a) : « Rejouer les critères à blanc sur les 94 cartes de la v9 » | entier ≥ 1 ✓. L'assemblage exige que les deux lectures portent exactement ce nombre de cartes |

**Étiquettes de lignée.** La statistique de famille (`bb2fa4a8…`, § 0) donne `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra` et `prop-carbon`, avec sa propre réserve : elle ne les a pas vues sur le fichier des cartes. La source à lire sans ouvrir de carte est la clé `especes` de la configuration de la course : `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json`, `3f662ee8…`. La même chaîne exacte doit figurer en quatre endroits, sans quoi le programme refuse :
- comme clé de `familles` ;
- comme valeur de la table des espèces que la mère tire de `meta` ;
- dans le champ `lignee` de chaque lecture ;
- dans le champ `lignee` de chaque liste de juge, s'il y en a.

## Ce que la mère écrit à côté du manifeste

Correction M1 des critères v7, annexe B : la justification de chaque valeur s'écrit **dans la pièce qui scelle le manifeste**, non dans le manifeste lui-même.

Il n'y a plus de valeur du défaut du 19 à justifier : Lazar a répondu sur les décisions 1 à 3. La pièce qui scelle cite donc **GO-2026-11-20-10 (O2)** pour :
- `usage` ;
- les quatre valeurs du veto ;
- `regime_items` ;
- `lignee_reconnue_declaree`.

Elle cite aussi la ligne de charge, si K ≠ 9.

## Hors du manifeste : ce que les décisions fixent ailleurs

- **En tête, (1) et (3).** La statistique de famille scellée reste telle quelle. La p brute de chaque liste est rapportée en tête de la proposition, « comme indice, sans autre effet ». Aucun fichier neuf, aucune clé.
- **Décision 5 (a), au rejeu.** Configuration A du masque, `configuration-masque-style-cartes-v1.json` : `plafond` = `"mediane"`. La confirmation 8, telle qu'écrite, donne `seuil_formule_recitee` = `0.2` et `minimum_formule_recitee` = `3`. Les autres clés suivent la demande du rapport v7, § 5, point 2 ; `champs` et `intertitres` sont à lire dans le code ou la consigne, avec la règle d'arrêt.
- **Confirmation 7, telle qu'écrite.** Les seuils des gardes sont des constantes du programme (`SEUIL_GARDE` 0,05, `MINIMUM_GARDE` 3, `N_PERMUTATIONS` 10 000). Aucune clé.

## Gestes que la décision 1 (a) fixe

1. **Rejeu d'abord, sans dépense, et aucune adoption de lui-même.**
   - L'adoption ne vient que s'il range : un tiers au plus des places du nombre visé décidé par la clé 8, et huit items au moins gardés dans chaque voie. Le programme écrit les deux dans `conditions_du_rejeu`.
   - **Retour à Lazar avant toute adoption** si une garde se déclenche (`retour_a_lazar_avant_adoption` de `gardes`), ou si la statistique scellée rend « signal présent », dans un sens comme dans l'autre.
   - La règle n'est jamais retouchée pour réussir.
2. **Ordre**, critères, annexe C :
   - scellement de la configuration A, de la configuration B, du manifeste et de la pièce qui le scelle ;
   - masque ;
   - lecteur par programme, deux fois (`--forme fiches`, puis `--forme masque`) ;
   - deux lecteurs neufs, des lignées Opus et Fable, qui n'ont lu ni les cartes ni les rejeux v2 ; chacun lit les cartes masquées, seul, et scelle sa lecture ;
   - table des espèces, par programme ;
   - `assembler`, avec `--lecteur-programme` pour la sortie masquée ;
   - `gardes`, avec les deux sorties du lecteur, sans quoi la baisse de D est « NON RAPPORTÉE » ;
   - la statistique de famille scellée, avec sa correspondance écrite après le dépôt ;
   - la proposition, puis sa contre-lecture.
3. **Sous la décision 3 (b), au rejeu**, chaque lecteur écrit `lignee_reconnue` pour chaque carte, avant de la noter. Le programme refuse une carte qui ne la porte pas (ligne 226).
   **Réserve à porter dans la consigne des lecteurs.** Le programme n'accepte, comme valeur utile, qu'une clé de `familles` ou « aucune ». Il ne contrôle que la présence d'un texte (ligne 226), et compte ensuite la famille par `familles.get(…)` (ligne 1071). Toute autre graphie, comme « Opus » au lieu de `prop-opus`, serait comptée en silence « ne croit pas reconnaître sa famille ». La consigne doit donc imposer, pour `lignee_reconnue`, l'une des cinq étiquettes, lettre pour lettre, ou « aucune », dans les cartes comme dans les listes de veto.
4. **Aucun usage sur une course** sans le mot de Lazar : le programme refuse `usage` « course » sans `ligne_accord`. En course, `lignee_reconnue_declaree` vaudra `false` (décision 3 (a)).

## Réserves

1. **`hors_choix` et les « 94 cartes ».** La décision 1, telle que Lazar l'a prise, porte sur les 94 cartes de la v9. Si la liste X6 que la mère tire par programme n'est pas vide, le rejeu ne peut pas porter sur 94 cartes. C'est alors un écart à dire avant l'ouverture, sans le régler en silence.
2. Les étiquettes `prop-…` restent à confirmer à la source nommée, sans carte.
3. Le choix de `identifiant_course` fixe tous les tirages : il est scellé avec le manifeste et ne se refait pas après une lecture.

## Lu, et incidents

- `git fetch`, puis trois `git show` redirigés vers mon dossier : `go.md`, les critères v7 et la note v7 scellés, et le compagnon des critères.
- Recherches de motifs sur le seul fichier `assemblage_selection_v4_v2.py` et sur ma copie de `go.md`.
- Aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucune commande de liste, une commande simple par appel.
- **Aucun refus** de permission, de classifieur ni de garde.

*contre-lecteur, modèle O*
