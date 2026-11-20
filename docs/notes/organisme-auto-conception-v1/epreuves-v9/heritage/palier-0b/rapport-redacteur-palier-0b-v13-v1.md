# Rapport du rédacteur — préenregistrement du palier 0b, version 13 (corrections de la contre-lecture de la version 12) — v1

- Auteur : rédacteur neuf, modèle F, le même que pour la version 12. Pièce de travail (classe C) rendant une pièce décisive (classe A), à faire vérifier par le contre-lecteur de la version 12.
- Date : 2026-11-20 ; `date -u` à 14:21Z en cours de travail ; heure du journal de l'outil pour la v13 : 14:22:44Z.
- Mandat : celui de la version 12 (`1485b861…`), en-tête compris, et deux messages de la session du compte organisme : le premier demande C1 à C12, NE-1 et la tenue ; le second porte la précision de la mère de 14:21Z (décision R-4292, chemins, forme).
- Conditions : processeur seul ; aucun lancement du code du palier, aucun tirage, aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication ; aucun heredoc, aucun code en ligne ; une commande simple par appel. **Aucun refus de permission, de classifieur ni de garde.**

## 0. Résultat

- **Version 13** : `preenregistrement-heritage-palier-0b-etage-processeur-v13.md`, empreinte `d9591d5bb53ba6688fdfe004ac5fee96ad8e1ea6093ab86850e4eecab177f959`.
- **Trois appels de l'outil** (`391db990…`), chacun réussi au premier essai, sans avertissement, chacun sur la sortie du précédent :
  1. v12 (`a4234028…`, celle du dépôt, égale à la mienne) + `corrections-palier-0b-v12-v1.json` (`82cf1897…`) : « FAIT : 12 remplacement(s) », sortie `bf6e40d2d7448ba5ba750d208293251bba354e2c64697c6de5015db72cf667e0` — **égale à l'essai du contre-lecteur** ;
  2. + `texte-non-exige-palier-0b-v12-v1.json` (`3642b44e…`) : « FAIT : 1 remplacement(s) », sortie `3617d9544aa80e8af5eb073470aacf759ba28be4a89993cb8eebf9d81e867a5d` — **égale à son second essai** ;
  3. + `remplacements-tenue-palier-0b-v12-v13-v1.json` (`9807e41b645f47e7d49f8bd19c570067a9e57dae29038bead5bc548c239714a6`), quatre remplacements de ma main : sortie, la v13.
- **Différentiel** `diff -u` v12 → v13 : `differentiel-palier-0b-v12-v13-v1.diff`, empreinte `95847b5d08824bbe25d90d0b8f82c35472fd4bab8cfca4bf9f8f2dc46b485670` (douze lignes retirées, douze ajoutées).
- **Lignes qui commencent par « - Commit du code d'analyse : »** : **1** (début de ligne : 1 ; `grep -c -F -e` : 1). Le bloc de la table (lignes 10 à 67), retrait ôté, reste égal à l'octet à `table-empreintes-code-v5.txt` (`cmp` muet).

## 1. Les quatre remplacements de ma main (chaque ancre comptée une fois par `grep -c -F -e` dans la sortie du deuxième appel)

| rang | lieu | objet |
|---|---|---|
| 1 | titre | v12 → v13 |
| 2 | ligne de version | statut ; alinéa « Version 13 » (ce qu'elle porte, les trois appels, les deux égalités) ; la version 12 dite au passé |
| 3 | section « Contre-lecture » | alinéa « Version 13 » : contre-lecture de la v12 faite, chemin, empreinte, verdict ; ce qui reste |
| 4 | annexe H, « Version 12 », remarque 5 | alinéa « Version 13 » : décision R-4292 citée à la lettre, les deux chemins, la forme |

## 2. La précision de la mère de 14:21Z

- `git fetch origin main`, puis `git show origin/main:registres/decisions.md >` mon dossier : commit `f880e95d0f097a6b4ad2fa5eab32a9917e729530`, fichier `2ae2f4900df0dcdba263c37efdca59db78b049bad52eb62bd3e2e97910de9bc2`. **R-4292 est à la ligne 4430, sous l'heure 2026-11-20T14:20:58Z** ; la v13 la cite à la lettre.
- La lettre de R-4292 donne en entier le chemin de la pièce de contrôle, et abrège celui du complément (« …-v1-complement-1.md ») ; elle dit « sur le modèle 0dcd2dc7… » pour la règle n° 8. Le chemin entier du complément et la forme (« une table, point par point, l'attendu et le constaté ») viennent du message ; la v13 le dit.
- Les deux pièces n'existent pas sur disque à cette heure (vérifié par leur chemin) ; la v13 le dit.

## 3. Remarques (aucune n'est tranchée)

1. **L'heure de la v13** : la ligne de version écrit « vers 14:25Z (`date -u` à 14:21Z en cours de travail ; les heures exactes sont aux trois journaux) » ; le journal dit 14:22:44Z. « Vers » couvre l'écart de trois minutes, mais c'est la forme que NE-4 et NE-1 corrigent : tenue possible si une version suit.
2. **La ligne de date** (« - Date (UTC) ») n'a pas reçu d'entrée pour la version 13 : le message ne nomme que le titre, la ligne de version, le statut et la section « Contre-lecture » ; l'heure est dite à la ligne de version.
3. **C7 garde la phrase « Ce texte n'en fixe ni le chemin ni la forme. »** (à la lettre du contre-lecteur) ; mon alinéa « Version 13 », qui la suit de près, dit que le chemin est désormais fixé par R-4292. Les deux se lisent ensemble.
4. **La forme de la pièce de contrôle** n'est dans la lettre de R-4292 que pour la règle n° 8 (« sur le modèle ») ; je l'ai écrite pour les deux pièces, comme le message le dit.
5. **L'annexe H n'a pas reçu de section « Version 13 »** ni de table de ce que la version touche : la ligne de version et la section « Contre-lecture » le disent ; hors du message.

## 4. Écarts et gestes

- Aucun écart au message. Les deux sorties intermédiaires portent « non-version » dans leur nom.
- Lu en entier : la contre-lecture de la v12. Les deux jeux du contre-lecteur n'ont pas été relus texte par texte : l'égalité des sorties à ses essais en tient lieu.
- Aucun identifiant de modèle ni de session dans mes textes ; la copie de travail de `decisions.md` en porte, elle n'est pas rendue.

## 5. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v13/` :
- `preenregistrement-heritage-palier-0b-etage-processeur-v13.md`, son compagnon, son journal (`751e58bb…`) et le compagnon du journal ;
- `remplacements-tenue-palier-0b-v12-v13-v1.json` et son compagnon ;
- `differentiel-palier-0b-v12-v13-v1.diff` et son compagnon ;
- ce rapport et son compagnon ;
- sorties intermédiaires, avec compagnons et journaux écrits par l'outil : `etape-1-v12-plus-corrections-non-version.md` (`bf6e40d2…`), `etape-2-v12-plus-corrections-et-ne-1-non-version.md` (`3617d954…`) ;
- fichiers de travail, non rendus : `decisions-main.md`, `bloc-de-la-v13-sans-retrait.txt`.

*Rédacteur neuf, modèle F.*
