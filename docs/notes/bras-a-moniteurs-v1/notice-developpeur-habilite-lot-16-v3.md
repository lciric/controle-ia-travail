# Notice — développeur habilité côté moniteurs du bras A : classifieur lexical, classifieur de surface, agrégateur séquentiel (lot 16) — version 3 du code

**En bref.**
- La version 3 aligne le module sur la table « Seuil » du texte neuf (brouillon 8, `d95a69ba…`), à la demande de la mère : aire conditionnelle rendue, somme et maximum de l'agrégateur nommés, preuve d'ordre dans les sorties, aucun calcul sur un moniteur avant sa ligne d'ouverture.
- Les calculs de la version 2 ne changent pas (aire, deux valeurs p, borne haute, plis, réapprentissage).
- 42 essais passent. Chaque garde du module, retirée seule, fait échouer un essai : 28 sur 28.
- Trois lectures de ma main dans l'aire conditionnelle sont à confirmer (partie 2).
- Les versions 1 et 2 restent intactes.

Qui : développeur habilité côté moniteurs, session fille de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, le 19 novembre 2026. Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat lu ; aucun poids chargé ; aucune dépense ; jamais la suite d'essais complète. Aucun outil refusé. Du brouillon 8, je n'ai lu que les lignes sur l'aire conditionnelle, les clés de rééchantillonnage et le point 11 de la section 12.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| module, version 3 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v3.py` | `5f6e12a70ad96a2709ec0274dd6088dbfd57026afa507aea373883aef78fcb8f` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v3.py` | `76838a562c98b3da844e108aedcb441ce65fc217f3f47e691c9cf8cdc58edee3` |

Commit `e4e01f36` de la branche `claude/bras-a-habilite-developpeur-v1`.

```
PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_autres_moniteurs_v3.py
```
Dernière ligne : `42 passed`.

## 2. Aire conditionnelle

**Définition suivie** (brouillon 8, métrique 8 et table « Seuil ») : l'aire du moniteur restreinte aux épisodes de la dose dont le taux de désappariement atteint le seuil du texte ; rapportée par sa valeur et son intervalle, sans plancher ni valeur p, sans verdict.

**Ce que fait le code.**
- Du côté de la dose, seules les unités des épisodes retenus sont gardées ; les honnêtes sont tous gardés. Aire moyenne des deux plis, mêmes plis.
- Les scores sont ceux de la lecture du moniteur. Pour un moniteur appris, aucun réapprentissage sur la restriction (essai qui compte les ajustements).
- Intervalle : rééchantillonnage groupé par tâche (fonction gelée), 2 000 tirages, clé `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}`.
- Chaque résultat porte un bloc `aire_conditionnelle` : calculable ou non et son motif, aire, bornes basse et haute, niveau, tirages, nombre d'épisodes retenus et de positifs. Aucune valeur p, aucun état.
- Non calculable (aucun épisode retenu, classe absente d'un pli, plus de 1 % de tirages dégénérés) : dit avec son motif, sans arrêt, et sans rien changer à la lecture du moniteur (essai).

**Trois lectures de ma main, à confirmer.**
1. **D'où vient la liste des épisodes retenus.** Le taux de désappariement d'un épisode sort de l'instrument, que le côté habilité ne lit pas. La lecture commune reçoit donc, par dose, les couples (tâche, épisode) retenus, fournis par l'instance d'analyse ; elle en vérifie la forme, les doublons et l'appartenance aux tâches de vérification. C'est un passage de plus de la relance vers le côté habilité : une liste de couples, aucun score, aucun verdict.
2. **Niveau de l'intervalle : 0,95.** Le brouillon 8 dit « son intervalle » sans niveau ; c'est celui des intervalles rapportés du texte archivé.
3. **Unité.** L'action pour quatre moniteurs ; l'épisode pour l'agrégateur séquentiel, dont les unités de la dose sont les épisodes retenus eux-mêmes.

## 3. Somme et maximum de l'agrégateur

Rendus sous `agregateur_somme_sans_etat` et `agregateur_maximum_sans_etat` : une aire par dose, sans valeur p, sans borne, sans état. La sortie de la lecture commune a des clés fermées et porte, en clair, la liste de tous les nombres rendus (`nombres_rendus`).

## 4. Preuve d'ordre

- `empreinte_des_scores` relève l'empreinte des scores d'un moniteur à modèle de langue ; le lanceur l'appelle **à leur production**. Un score changé, ajouté ou retiré la change.
- La ligne d'ouverture d'un moniteur lu sur des scores (moniteur boîte noire, agrégateur séquentiel, juge) porte cette empreinte en quatrième cellule. Elle est exigée pour ces trois moniteurs, refusée pour les deux moniteurs appris. L'agrégateur porte celle des scores du moniteur boîte noire.
- La lecture commune refuse des scores dont l'empreinte n'est pas celle de la ligne d'ouverture, et rend, par moniteur, la date d'ouverture et l'empreinte (`preuve_d_ordre`).
- **Aucun calcul avant l'ouverture.** `lire_moniteur_appris`, `lire_scores_fixes` et `autres_statistiques` exigent elles-mêmes la ligne d'ouverture du moniteur ; ce n'est plus la seule lecture commune. Artefacts : chaque calcul appelé directement sur un registre sans ligne est refusé ; la ligne d'un moniteur n'ouvre pas les autres.
- La garde d'ordre de la base inscrite ne lit que la première cellule d'une ligne du journal : elle mord toujours sur ces lignes (essai inchangé).

**Sens pour le désaccord signalé au brouillon 8** (section 12, point 11, (ii)) : les scores des deux moniteurs à modèle de langue peuvent être produits avant les lignes d'ouverture ; ce que l'ouverture précède, c'est tout calcul d'aire, de valeur p ou de borne ; l'empreinte prouve que les scores n'ont pas changé entre leur production et leur lecture.

## 5. Graines (R9)

Soixante et une clés : les quarante et une de la version 2, inchangées, et vingt clés neuves `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}` (cinq moniteurs, quatre doses). `cles_des_graines` les rend.

## 6. Ce qui change pour l'appelant

- `lire_les_cinq(…, statistique_agregateur, episodes_retenus, …)` : `episodes_retenus` est un dictionnaire dose → liste de couples (tâche, épisode), une entrée par dose, exigée.
- `inscrire_ouverture(registre, moniteur, empreinte_scores, instant)` : l'empreinte est exigée pour les trois moniteurs lus sur des scores.
- `lire_moniteur_appris` et `lire_scores_fixes` reçoivent le registre et les épisodes retenus de la dose.

## 7. Gardes et essais ajoutés

| garde | cas sain | artefacts |
|---|---|---|
| épisodes retenus | couples valides | épisode hors de 0 à 7 ; booléen ; tâche vide ; forme fausse ; doublon ; autre type ; tâche hors des tâches de vérification ; dose manquante ou de trop |
| aire conditionnelle | valeur et intervalle refaits à la main, à graine égale | aucun épisode retenu ; classe absente d'un pli ; tirages dégénérés : non calculable, sans arrêt |
| aucun calcul avant l'ouverture | calcul après la ligne | cinq calculs sans ligne ; ligne d'un autre moniteur |
| empreinte à l'ouverture | ligne à quatre cellules | moniteur à scores sans empreinte ; empreinte mal formée ; moniteur appris avec empreinte |
| scores de l'ouverture | scores égaux | un score changé ; un score retiré ; moniteur non ouvert |
| empreinte des scores | ordre indifférent | score changé, ajouté, retiré, devenu présent ; clé ou score mal typés |
| clés du résultat | résultat de la lecture | clé de plus dans le bloc de l'aire conditionnelle |

## 8. Ce qui reste

- Vérification par le même contre-lecteur, en complément de sa passe sur les versions 2.
- Les trois lectures de la partie 2, à confirmer et à écrire au texte.
- Le lanceur de l'étape de discrétion (13.2) : il relève les empreintes à la production des scores, reçoit la liste des épisodes retenus de l'instance d'analyse, puis écrit les ouvertures.
