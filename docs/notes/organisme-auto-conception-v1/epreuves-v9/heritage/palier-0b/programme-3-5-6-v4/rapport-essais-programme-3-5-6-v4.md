# Rapport des essais v4 du programme des étapes 3 à 6 (programme v2 inchangé) — v1

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C). Développeur, modèle O, 2026-11-20. Rien n'est lancé en vrai, aucune graine décisive, aucune écriture dans le dépôt, aucun commit.

- **Vérification des essais v3** : `P0B/verification-essais-programme-3-5-6-v3-v1.md` (`59907a0d59381fe81ea257ab477b7c263a39f3640351b99353b779dafd8482dd`, contrôlée contre son compagnon). Verdict « À corriger », point 4 : la variable `PROGRAMME_3_5_6_MUTANT` est une porte dérobée.
- **Programme** : inchangé, `lancer_etapes_3_5_6_v2.py`, `1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14`. Les essais le chargent depuis ma copie de bloc-notes, d'empreinte égale à celle du fichier versé.
- **Essais v3** : la v3 n'est pas touchée.

## 1. Ce qui change (`differentiel-essais-v3-v4.diff`)

- **Essai neuf `test_le_programme_charge_est_le_v2`.** Il exige que deux empreintes égalent `EMPREINTE_DU_PROGRAMME_V2` (`1f04cb46…`) : celle que rend `PR.empreinte_du_programme()` et celle du fichier chargé. Il passe quand la variable est absente. Il échoue dès que la variable désigne une autre copie, avec un message qui le dit.
- **Message à l'import.** Quand la variable est posée, un avertissement est écrit sur la sortie d'erreur.
- **Docstring de tête.** Mis à jour.
- Rien d'autre ne change.

## 2. Ce que les relevés doivent donner (écrit avant de les jouer, `date -u` : Fri Nov 20 20:49:34 UTC 2026)

1. **Variable absente** : les 33 essais (32 de la v3 et l'essai neuf) doivent tous passer.
2. **Mutant** : la copie jetable du programme reçoit la permutation (chemin, empreinte) → (empreinte, chemin) dans le retour de `lancer`, et la variable est posée sur elle. On doit observer **3 échecs** :
   - l'essai neuf ;
   - `test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue` ;
   - `test_v3_main_imprime_le_retour_de_lancer`.

   Les autres essais du fichier (29) doivent passer.
3. **Essai neuf seul, variable posée à faux** : la variable est posée sur une copie au simple commentaire ajouté. L'essai neuf doit **échouer**, et le message d'import doit apparaître.
4. **Essai neuf, variable absente** : il passe. C'est le relevé 1.

## 3. Ce que les relevés ont donné

Avant les relevés, l'empreinte de ce rapport (§ 1 et 2 seulement, § 3 vide) était `2f20732297c7684de3557dc46cef1083bda1703b5bba2ad6b5b5ddfd979bdf35`. Le § 2 n'a pas été touché depuis. Les relevés ont été joués dans l'ordre demandé, l'un après l'autre, en tâche de fond. Le programme et le code sont les mêmes partout : la copie du code v6 du bloc-notes, égale à la table `639335b9…`, avec `PYTHONPATH=src` et les deux variables `HERITAGE_*`.

| relevé | variable | résultat | attendu (§ 2) | journal |
|---|---|---|---|---|
| 1. les 33 essais | absente | **33 passés, 0 échoué** (824 s) | 33 passés | `releve-1-essais-variable-absente.log` |
| 2. mutant (permutation l. 240, copie jetable `mutant-v4/`, supprimée ensuite) | posée sur le mutant | **3 échoués, 29 passés** (838 s) : `test_le_programme_charge_est_le_v2` (empreinte `2b43da64…` au lieu de `1f04cb46…`, « PROGRAMME_3_5_6_MUTANT est posée »), `test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue` et `test_v3_main_imprime_le_retour_de_lancer` (le premier membre est une empreinte, non le chemin) | 3 échecs, les mêmes | `releve-2-mutant.log` |
| 3. l'essai neuf seul (`-s`, sortie non capturée) | posée sur une copie au seul commentaire ajouté (`copie-commentaire-v4/`, une ligne en fin de fichier, supprimée ensuite) | **1 échoué** (empreinte `d5673dc9…` au lieu de `1f04cb46…`), message d'import écrit : « ATTENTION : PROGRAMME_3_5_6_MUTANT est posée ; programme chargé sans contrôle à l'import : … » | échec, message | `releve-3-essai-neuf-variable-posee.log` |
| 4. l'essai neuf, variable absente | absente | passé (dans le relevé 1) | passe | relevé 1 |

**Tout est conforme à ce qui était dit d'avance.**

**Constat sur le message d'import.** Sous la capture ordinaire de pytest (relevé 2, sans `-s`), le message écrit à l'import n'apparaît pas dans le journal : pytest garde la sortie de la collecte et ne la montre qu'en cas d'erreur de collecte. Il apparaît avec `-s` (relevé 3). Ce qui signale la variable dans tous les cas, c'est l'échec de l'essai neuf, et son message nomme la variable.

Après les relevés, le programme v2 a été recontrôlé : `1f04cb46…`, dans ma copie et dans le dossier versé.

## 4. Fichiers (sous-dossier `programme-3-5-6-v4/`, chacun avec son compagnon)

- `tests/test_lancer_etapes_3_5_6_v4.py`
- `differentiel-essais-v3-v4.diff`
- les trois journaux de relevé
- ce rapport
- `table-empreintes-programme-3-5-6-v4.txt`

Le programme n'est pas recopié.

## 5. Écarts

- Le relevé 3 a été joué avec `-s`, pour que le message d'import se voie (§ 3).
- Deux copies jetables du programme ont été créées dans le bloc-notes, puis supprimées.
- Les deux variables d'environnement des essais, comme avant.
- Aucune commande de liste ni de recherche de processus ; aucune commande d'arrêt ; aucun refus de permission, de classifieur ni de garde.

Développeur, modèle O.
