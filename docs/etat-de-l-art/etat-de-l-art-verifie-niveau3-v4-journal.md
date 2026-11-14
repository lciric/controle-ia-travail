# Journal de la synthèse de l'état de l'art vérifié de niveau 3 — v4

Écrit le 2026-11-14, de 01:35:38 UTC à 2026-11-14 à 01:38:19 UTC (heures relevées par `date -u`). Auteur : modèle A (auteur des v2 et v3) ; contre-lecteur de la v2 et vérificateur de la v3 : modèle B ; A ≠ B. Compagnon de `etat-de-l-art-verifie-niveau3-v4.md`. Mandat : message du coordinateur après la remise de la v3 (intégrer la vérification de la v3, sous un nom neuf, sans toucher la v3).

## 1. Consignes tenues

Consigne commune du compte 2 (`cb0623c4…`) et interdits communs v2, sans exception : aucune commande git, aucun réseau, aucun appel de modèle ; fichiers nommés seulement ; rien de T0.7, de 7a ni de 7b ; rien sous `registres/`, `diag/`, `runs/`, `donnees/` ; aucune suppression par motif ; aucun nom de modèle du programme. Avant d'écrire : `ls` du seul dossier `docs/etat-de-l-art/`, aucun des trois fichiers v4 n'existait. Travail versé au fil de l'eau dans le sous-dossier neuf `v4/`.

## 2. Sources nouvelles et empreintes (recalculées, égales à leurs compagnons)

| fichier | sha256 |
|---|---|
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v3.md` (remplacé pour la lecture) | `aab1538aaed833f2f06073dbd9ba30a12cbb8584e7d71b40535bef9bde4b918b` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v3-journal.md` | `a4c4ab34e8855ecf3222d59f6b1570dc67bf872acaaa53810f97c4b11cd76234` |
| `docs/etat-de-l-art/fichiers-de-travail-synthese-niveau3-v3.tar` | `3612bc48d21443a3992ebec519925dcf13e977b31d6b932686ce8064ba9483e2` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v3-contre-lecture-v1.md` (vérification de la v3) | `07f33db5cc5ddc41b503c12b85c6ccd4a8787762d6f8fef34fa78bac77de0a0f` |

Les sources des versions précédentes sont inchangées ; leurs empreintes sont aux journaux de la v2 et de la v3.

## 3. Ce que j'ai lu pour la v4, et comment

- La vérification de la v3, en entier (100 lignes). Son archive n'a pas été ouverte.
- Pour juger S et T moi-même, par recherche de passages dans des fichiers nommés : `rapport-HC1-2607.00415-v2.md`, section 6 (les trois voisins « à lire en priorité ») ; `rapport-4B-partie1-v2.md`, sections 6 et 7 (l. 157 : « Rien sur le gain continu de la corruptibilité d'un juge appris tant que Gao, Schulman et Hilton n'est pas lu sur PDF » ; l. 162) ; `contre-lecture-rapport-papierB-v1.md`, section 4 (l. 74 : Bonjour et collègues 2022 « à lire en priorité », sans restriction).
- Pour V : ce que j'avais déjà lu de la v1 (section 9), de sa contre-lecture (sections 5 et 6, M13), des rapports du compte 2 (K-B, section 6 ; K-HC5, section 5) et la section 4 de la contre-lecture de K-B.

## 4. Décisions S à V

Toutes « corrigé » (section 2 ter de la synthèse). S et T : la vérification avait raison, ma v3 appliquait sa propre condition 4 moins durement à HC1 et à l'énoncé 1 qu'à H2 et à T ; je m'y range après relecture, non par déférence. V : la condition 4 est vérifiée pour H3, H5, H7 dans tout ce que j'ai lu ; les rapports du niveau 3 ne sont pas rouverts, et chaque ligne le dit.

## 5. Lignes « déclarable » changées depuis la v3

- de « oui » à « non » : HC1 ; statistique de population, énoncé 1 de N-069 ;
- liste finale des « oui » : H3, H5, H7, T pour (c) à (f).

## 6. Contrôle des extraits anglais

`controle_guillemets_v3.py` (inchangé, table `ATTENDU` des PDF attendus) relancé sur la v4 : 12 extraits anglais, 0 erreur (357 passages entre guillemets). `citations-synthese-v4.json` donne pour chaque extrait le PDF, son empreinte, la page et le JSON source.

## 7. Ce que je n'ai pas fait

Aucun PDF ouvert. Rapports du niveau 3 non rouverts. Je n'ai pas contre-lu la v4.

## 8. Refus et ouvertures

Aucun refus. Aucune ouverture fautive.

## 9. Archive

`fichiers-de-travail-synthese-niveau3-v4.tar` : `citations-synthese-v4.json`, `controle-guillemets-v4-final.txt`, `scripts/` (contrôleur, essai et son résultat, scripts du recueil), journal de travail v4. Sans PDF ni texte extrait.
