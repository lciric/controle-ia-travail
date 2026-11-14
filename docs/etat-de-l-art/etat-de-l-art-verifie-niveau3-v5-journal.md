# Journal de la synthèse de l'état de l'art vérifié de niveau 3 — v5

Écrit le 2026-11-14, de 07:12:53 UTC à 07:30:13 UTC (heures relevées par `date -u`). Auteur : modèle A (auteur des v2, v3 et v4) ; contre-lecteur de la v2, vérificateur de la v3 et de la v4 : modèle B ; A ≠ B. Compagnon de `etat-de-l-art-verifie-niveau3-v5.md`. Mandat : message du coordinateur après la confirmation de la v4 (reporter les lectures faites depuis la v4 et les mots de Lazar, sous un nom neuf, sans toucher la v4 ; travail de report, pas de réécriture).

## 1. Consignes tenues

Consigne commune du compte 2 (`cb0623c4…`) et interdits communs v2, sans exception : aucune commande git, aucun réseau, aucun appel de modèle ; fichiers nommés seulement ; rien de T0.7, de 7a ni de 7b ; rien sous `registres/`, `diag/`, `runs/`, `donnees/` ; aucune suppression par motif ; aucun nom de modèle du programme. Avant d'écrire : `ls` du seul dossier `docs/etat-de-l-art/`, aucun fichier v5 n'existait. Travail versé au fil de l'eau dans le sous-dossier neuf `v5/` de mon dossier de travail.

## 2. Sources nouvelles et empreintes (recalculées, égales à leurs compagnons et, pour les rapports, à l'index v2)

| fichier | sha256 |
|---|---|
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v4.md` (remplacé pour la lecture) | `a6a1dcc99883a0bfd3cfc6fd307bb3b6c033b5d1c005c00a26c04c850d737430` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v4-journal.md` | `9843f830bfca9ef39c54538bacd007bfbe97571ac4ceab873e3d83ad39c2f0d0` |
| `docs/etat-de-l-art/fichiers-de-travail-synthese-niveau3-v4.tar` | `796c9efad6b276df7389e5f20b8979e178c46a7c9a6e344b48d34764eb342131` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v4-contre-lecture-v1.md` (confirmation de la v4) | `632004d814a20927d6ffaf33c6f39179ac03891e005ceefa68d99bf837d1617d` |
| `docs/sources/lecture-pdf-niveau3/compte-2/index-rapports-compte-2-v2.md` | `e1d9f3195313cf8b645eed93d583b21653d49c15c0bd72bc6ea4646f396339bb` |
| `rapport-H1-2609.19101-v2.md` (K-H1b) | `80cbb073180298c613eaf24d1232fe9ec898e38f1191d121d67ee074774e0429` |
| `contre-lecture-rapport-H1-2609.19101-v1.md` | `724857f51ef78bc8d8a18e614c87e97c9f67d0e8e33cf8f7fb6fa82586ce7a21` |
| `rapport-HC4-2609.15994-v2.md` (K-HC4b) | `1a09a60d11242c7c4bef620e862b6ffc3481d010f32a46b120c325c3c3d0d63c` |
| `contre-lecture-rapport-HC4-2609.15994-v1.md` | `1db31c1993fd4ca19d96fe85093c13690a76a90ecd5ee936fe3971b0c011b0d7` |
| `rapport-L-voisins-v2.md` (K-Lv) | `649f471e583b1700efa127fb2ef258f9338be322d343529f7fa859c42ff44466` |
| `contre-lecture-rapport-L-voisins-v1.md` | `58e7ad2d5cba602c1c79259340a625af06b8bf8a5a95d343719259c91fcee929` |
| `rapport-L-ker2007-v2.md` (K-Lk) | `6bf86934f1a4769021d8e5caf67c95e8b0831c2d15436a50a3e64d462487bfcd` |
| `contre-lecture-rapport-L-ker2007-v1.md` | `8805d9cf5be364115c9f68a12e58986c03367d2668e9518b0690dd32fcb5686a` |

Les rapports et contre-lectures sont dans `docs/sources/lecture-pdf-niveau3/compte-2/`. Les sources des versions précédentes sont inchangées ; leurs empreintes sont aux journaux de la v2, de la v3 et de la v4.

## 3. Ce que j'ai lu pour la v5, et comment

- L'index v2, en entier (25 lignes), dont la ligne 25 (mots de Lazar), seule source de ces mots : je n'ai pas lu le registre qui les inscrit.
- La confirmation de la v4, en entier.
- Les quatre rapports nouveaux, en entier ; leurs quatre contre-lectures, en entier (celle de K-H1b l'était déjà pour la v3). Archives non ouvertes.
- Ma v4, dans mes fichiers de travail, copiée partie par partie dans `v5/parties/` avant tout report.

## 4. Reports (section 2 quater de la synthèse)

R1 à R6 « corrigé » ; R7 (M4 et mot de Lazar sur L1) et R8 (mot de Lazar sur H6) « réserve maintenue ». Les passages qu'aucune lecture nouvelle ne touche sont ceux de la v4, inchangés. Pour HC4, la condition 4 est ajoutée au motif du « non » (McKenzie et collègues, en tête de la liste ordonnée de K-HC4 ; Yu et collègues, le plus proche selon K-HC4b) : la v4 ne citait que les conditions 2 et 3.

## 5. Lignes « déclarable »

- Aucune ne change de valeur depuis la v4. Les quatre « oui » restent : H3, H5, H7, T pour (c) à (f) ; aucun rapport lu depuis ne les touche.
- Motifs changés : HC4 (condition 2 levée par le mot de Lazar ; conditions 3 et 4) ; HC6 (condition 2 levée ; condition 4) ; L (R-2649 selon K-Lk ; M4 avec la liste nouvelle ; resserrement en attente).

## 6. Contrôle des extraits anglais

`controle_guillemets_v3.py` (inchangé, table `ATTENDU` des PDF attendus) relancé sur la v5 : 429 passages entre guillemets, 12 extraits anglais, 0 erreur. Aucun extrait anglais nouveau : les pièces lues depuis la v4 sont rapportées sans citation anglaise. `citations-synthese-v5.json` donne pour chaque extrait le PDF, son empreinte, la page et le JSON source.

## 7. Ce que je n'ai pas fait

Aucun PDF ouvert. Archives des rapports nouveaux non ouvertes. Rapports du niveau 3 non rouverts. Registre des mots de Lazar non lu. Je n'ai pas contre-lu la v5.

## 8. Refus et ouvertures

Aucun refus. Aucune ouverture fautive.

## 9. Archive

`fichiers-de-travail-synthese-niveau3-v5.tar` : `citations-synthese-v5.json`, `controle-guillemets-v5-final.txt`, `scripts/` (contrôleur, essai et son résultat, scripts du recueil), `parties/` (les parties de la v5), journal de travail v5. Sans PDF, sans texte extrait, sans le recueil de citations.
