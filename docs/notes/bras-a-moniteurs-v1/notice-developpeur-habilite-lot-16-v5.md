# Notice — développeur habilité côté moniteurs du bras A : classifieur lexical, classifieur de surface, agrégateur séquentiel (lot 16) — version 5 du code

**En bref.**
- Mot de Lazar (GO-2026-11-19-52, fiche 6, option (b)) : l'aire conditionnelle est calculée par l'instance d'analyse, sur les scores par unité que ce module rend. La liste des épisodes retenus ne passe jamais du côté des moniteurs.
- La version 5 retire donc le calcul de l'aire conditionnelle et sa clé de graine, et écrit un fichier fermé et scellé des scores par unité.
- 45 essais passent. Chaque garde du module, retirée seule, fait échouer un essai : 32 sur 32.
- **À savoir** : ce fichier porte les scores de tous les moniteurs, action par action. Ce n'est pas un interne de moniteur, mais c'est plus que les nombres agrégés des versions d'avant (partie 3).
- Les versions 1 à 4 restent intactes. Les versions 1 à 3 ne doivent servir à aucune lecture décisive (permutation action par action).

Qui : développeur habilité côté moniteurs, session fille de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, le 19 novembre 2026. Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat lu ; aucun poids chargé ; aucune dépense ; jamais la suite d'essais complète. Aucun outil refusé. J'ai vérifié la ligne GO-2026-11-19-52 au registre des accords, sur la branche principale.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| module, version 5 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v5.py` | `570bf5a232d9157123945193fb154df7e1fc65b01f88ac3348611bd4b5b220f1` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v5.py` | `cd61c2821f044f34c634408c889bfbe1f9ac7518cf26ef1866d128842d65c314` |

Module au commit `9867a3be`, inchangé depuis. Les essais ont reçu un essai de plus après ce commit (partie 4) : leur empreinte d'alors, `37318ce5…`, est remplacée par celle de la table.

```
PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_autres_moniteurs_v5.py
```
Dernière ligne : `45 passed`.

## 2. Ce qui est retiré

- Le calcul de l'aire conditionnelle et le bloc qui la portait dans chaque résultat.
- La vérification des épisodes retenus : aucune liste d'épisodes n'entre plus dans le module.
- La clé `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}`. Les clés sont de nouveau quarante et une, égales à celles de la version 2 (essai).

## 3. Le fichier des scores par unité

- **Nom** : `scores-par-unite-moniteurs-bras-a.jsonl`, écrit et scellé par la lecture commune dans le dossier qu'on lui donne. Jamais écrasé : s'il existe, la lecture refuse avant tout calcul.
- **Une ligne** par moniteur, dose et unité, à dix champs et eux seuls, dans cet ordre : `moniteur`, `dose`, `cle`, `condition`, `tache`, `episode`, `pas`, `pli`, `etiquette`, `score`.
- **Unité** : l'action pour quatre moniteurs ; l'épisode pour l'agrégateur séquentiel, sans pas.
- **Contenu par dose** : les unités de la dose (étiquette 1) et celles de l'honnête (étiquette 0), sur les deux plis.
- **Moniteur appris** : le score d'une action est celui du modèle appris sur l'autre pli pour le jeu de cette dose. Il dépend donc de la dose, y compris pour les actions honnêtes : une action honnête a une ligne par dose.
- **Aucun interne** : ni vocabulaire, ni coefficient, ni trait, ni texte d'action. Une garde vérifie chaque ligne ; un essai cherche dans le fichier écrit les marques d'un mot de vocabulaire ou d'un texte d'action.
- **Après l'ouverture** : les scores ne sont collectés que par les fonctions de lecture, qui exigent la ligne d'ouverture du moniteur ; l'écriture la revérifie pour chaque moniteur présent. Sans ouverture, rien n'est écrit.
- **Dans la sortie** de la lecture commune : nom du fichier, empreinte, nombre de lignes, liste des champs.
- **Cohérence** : pour chacun des cinq moniteurs, l'aire refaite sur le fichier est égale à l'aire rendue (essai).

**Calcul de l'aire conditionnelle par l'instance d'analyse** : pour un moniteur et une dose, garder toutes les lignes d'étiquette 0 et les lignes d'étiquette 1 des épisodes retenus ; aire dans chaque pli ; moyenne des deux plis. Son intervalle demande une clé de graine du côté de l'analyse.

**Ce que ce fichier fait sortir.** Les versions d'avant ne rendaient que des nombres agrégés par moniteur et par dose. Celle-ci rend le score de chaque action. Un score n'est ni un seuil, ni un trait, ni un poids, ni une consigne, et le mot de Lazar le fait sortir vers l'instance d'analyse. Deux conséquences à écrire au texte : la liste de ce qui passe à l'instance d'analyse nomme ce fichier ; et ce fichier ne doit atteindre aucune session qui conçoit ou règle l'agent (invariant « aucun score de moniteur dans l'entraînement de l'agent », décision N-053).

## 4. Gardes et essais ajoutés

| garde | cas sain | artefacts |
|---|---|---|
| ligne de score | ligne d'une lecture | champ de texte ; champ de trait ; champ manquant ; ordre changé ; moniteur, dose ou condition hors liste ; étiquette incohérente ; pli faux ; clé vide ; score non fini ; score entier |
| écriture des scores | fichier scellé | moniteur non ouvert ; unité en double ; ligne à champ de plus ; fichier déjà présent |
| fichier déjà présent, avant tout calcul | — | la lecture commune refuse sans charger la pièce source |
| clés du résultat | résultat d'une lecture | bloc d'aire conditionnelle réintroduit ; vocabulaire ; clé manquante |

L'épreuve par retrait avait laissé survivre une garde : le refus d'écraser placé en tête de la lecture commune, doublé par celui de l'écriture. L'essai `test_fichier_des_scores_deja_present_refuse_avant_tout_calcul` a été ajouté ; il échoue quand cette garde est retirée. Le module n'a pas changé.

## 5. Ce qui change pour l'appelant

- `lire_les_cinq(…, statistique_agregateur, dossier_des_scores, …)` : un dossier pour le fichier des scores, à la place des épisodes retenus.
- `lire_moniteur_appris` et `lire_scores_fixes` reçoivent une liste où elles ajoutent les lignes de score.
- Les résultats ne portent plus de bloc d'aire conditionnelle.

## 6. Ce qui ne change pas

Permutation par épisode et sa garde ; deux valeurs p et valeur p de la famille ; borne haute ; somme et maximum de l'agrégateur ; plis communs ; preuve d'ordre par l'empreinte des scores à l'ouverture ; refus de tout calcul avant l'ouverture.

## 7. Ce qui reste

- Vérification par le même contre-lecteur.
- Case 13.1 : le module des cinq moniteurs à citer est la version 5.
- Lanceur de l'étape de discrétion (13.2) : il donne le dossier des scores et remet le fichier scellé à l'instance d'analyse.
