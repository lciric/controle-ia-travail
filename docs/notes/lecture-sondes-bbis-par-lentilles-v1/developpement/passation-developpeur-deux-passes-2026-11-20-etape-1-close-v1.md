# Passation du développeur neuf des deux passes — étape 1 close, étape 2 non entamée — v1

2026-11-20 (UTC), branche `claude/brave-galileo-jhp684`. Rangée ici, comme celle du premier développeur, et non sous
`registres/passations/`.

## Fait
- Étape 1 : code de la première passe accordé à l'addendum de concentration scellé (`7c738708…`), commit `2e15977b` ; jugé
  « conforme, aucun écart bloquant » par le contre-lecteur neuf (`contre-lectures/contre-lecture-code-premiere-passe-addendum-v1.md`,
  `7954d0fc54320d76ed63a634893063425683806dfb327acec1443e1ed6a96fd4`, vérifié, lu en entier).
- Les trois corrections non bloquantes que la session des lentilles m'a demandé de porter, sans réécrire un fichier existant :
  1. note de conformité neuve, `conformite-code-a-l-addendum-concentration-scelle-v2.md` : le § 6 nomme les deux ajouts de
     `lanceur_v4` hors addendum (rapport du montage exigé ; champ d'égalité de la relecture de l'audit, lignes 872 et 874) ;
  2. et 3. fichier d'essais neuf `tests/test_lentilles_sondes_bbis_contre_lecture_addendum_v1.py` (`d69eac839f9de08381cbbbe24930e08ff42abe0e614dae03237e08a143d8d037`) : plusieurs directions
     marquées dans un même nul (contre l'énumération conjointe des départages, et son artefact) ; ligne des entrées placée après
     la ligne de l'addendum mais d'heure antérieure (cas sain et artefact). Trois essais, verts (`3 passed`) ; l'altération qui
     retire le critère de l'heure fait tomber le troisième (jouée une fois, code remis en l'état).
- Aucun code n'a changé depuis `2e15977b`. La suite du paquet n'a pas été rejouée pour ces trois essais ajoutés (ils n'importent
  que `entrees_v3`, `statistiques_v3` et les jouets des deux fichiers d'essais de l'étape 1).

## Erreur de mon message de rendu de l'étape 1, corrigée ici
J'y donnais `1abbe232…` pour `tests/test_lentilles_sondes_bbis_addendum_concentration_v2.py` : c'était l'empreinte d'avant mon
dernier changement de ce fichier. L'empreinte du fichier committé est `cf92419d…`, celle que porte `empreintes-code-v4.txt`
(relevé du contre-lecteur, point 9).

## Reste : toute l'étape 2
**Non entamée, et le texte v2 n'est toujours pas lu en entier** (l'écart que j'avais déclaré n'est pas réparé). Raison, dite sans
détour : cette session a déjà lu les textes, le paquet et écrit l'étape 1 ; le texte v2 (405 Ko) et la section « Code neuf »
entière (sept modules, un lanceur, tous les essais des brouillons 4 à 6) ne tiennent pas dans ce qui lui reste de mémoire de
travail. Écrire un instrument de classe B dans ces conditions, au risque d'être coupé avant tout commit, serait le mauvais choix.
L'étape 2 est à confier à une session neuve du développeur (même mandat `0a9517ea…`), qui part de ces fichiers.

## Ce que la session neuve doit savoir
- Lire d'abord, en entier, `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`, branche principale), sans la liste
  « Jamais ouverts » ; puis `notes-developpement-v2.md`, la note de conformité v2, la contre-lecture.
- Noms laissés libres pour elle : `montage_v2`, `audits_v2`, `phrases_v2`, `nos_lentilles_v1`, `lecture_entree_v1`,
  `comparaisons_lentilles_v1`, `reproduction_v1`, et le module neuf des statistiques (le prochain nom libre est
  `statistiques_v4` : statistique corrigée et règle de départage par identifiant de jeton croissant, GO-2026-11-19-92).
- `statistiques_v3` porte déjà, réemployables : `premiers_gardes`, `bornes_de_departage`, `p_concentration`,
  `paires_de_lignes_egales`, `ResumeNul` (comptes d'égalités).
- **Nœud 1 de la contre-lecture, chez Lazar** (canal des messages d'arrêt d'égalité) : ne pas changer `lanceur_v4` ; dans le
  lanceur de la seconde passe, isoler l'écriture des messages d'arrêt (une seule fonction qui décide ce qui va à la sortie
  d'erreur et ce qui va dans `arret.json`), pour suivre l'une ou l'autre réponse sans réécriture. **Nœud 2** (relecture de
  l'audit) : garder « écrit, sans arrêt ».
- Jouer les essais avec `PYTHONDONTWRITEBYTECODE=1`. Environnement : `notes-developpement-v2.md`, § 4.

## Instances actives
Aucune machine, aucune dépense, aucun téléchargement de modèle, de lentille ni de corpus ; aucune clé lue.
