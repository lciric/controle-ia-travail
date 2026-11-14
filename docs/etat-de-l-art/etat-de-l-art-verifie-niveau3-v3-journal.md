# Journal de la synthèse de l'état de l'art vérifié de niveau 3 — v3

Écrit le 2026-11-14, de 01:17:12 UTC à 2026-11-14 à 01:30:26 UTC (heures relevées par `date -u`). Auteur : modèle A (auteur de la v2) ; contre-lecteur de la v2 : modèle B ; A ≠ B. Compagnon de `etat-de-l-art-verifie-niveau3-v3.md`. Mandat : message du coordinateur reçu après la remise de la v2 (intégrer la contre-lecture de la v2 sous un nom neuf, sans toucher la v2 ; ne rien sceller avant son second message, qui porte le verdict sur 2609.19101 contre H1).

## 1. Consignes tenues

Consigne commune du compte 2 (`cb0623c4…`) et interdits communs v2, sans exception : aucune commande git, aucun réseau, aucun appel de modèle, aucune dépense, aucune valeur de clé ; fichiers nommés seulement ; rien de T0.7, de 7a ni de 7b ; rien sous `registres/`, `diag/`, `runs/`, `donnees/` ; aucune suppression par motif ; aucun nom de modèle du programme écrit. Avant d'écrire dans le dépôt : `ls` du seul dossier `docs/etat-de-l-art/`, aucun des trois fichiers v3 n'existait. Travail versé au fil de l'eau dans le sous-dossier `v3/` de mon dossier de travail.

## 2. Sources nouvelles et empreintes (recalculées, égales à leurs compagnons)

| fichier | sha256 |
|---|---|
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v2.md` (objet remplacé) | `0a744ded38364993d6329ea72f1c639ffaa233e89def75e8a7179aca582bbba5` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v2-journal.md` | `0b65a2d044d50cc19e6fb4df3c88ecef44ba40f6d8a69d5ea19db977740ad3e8` |
| `docs/etat-de-l-art/fichiers-de-travail-synthese-niveau3-v2.tar` | `8fc20719e2d63f632b72388e2cecdaf82ccd9e63a1c19a414be760d3b423a454` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v2-contre-lecture-v1.md` | `bc5909fc43f6aa930a616741937d67847857de789d99bdcc9aa9fbde2b8fbf58` |
| `docs/etat-de-l-art/fichiers-de-travail-contre-lecture-synthese-niveau3-v2.tar` | `c61abff20c748e525c977c1420aa27e66db821fe3331579951057627ed09d887` |
| `docs/decisions/decision-N-067-v1.md` | `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589` |
| `docs/sources/lecture-pdf-niveau3/compte-2/rapport-H1-2609.19101-v1.md` | `498a34939a2d3960cc204b78a655229f36ad66e50dafa2fd1037eeb7e0eb8c82` |
| `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-H1-2609.19101-v1.md` | `724857f51ef78bc8d8a18e614c87e97c9f67d0e8e33cf8f7fb6fa82586ce7a21` |
| `compte-2/fichiers-de-travail-H1-2609.19101-v1.tar` (non ouverte) | `4eefec72af46ea85afe4a89342b47c9205abd4e628aba38c725d69be065a07d1` |
| `compte-2/fichiers-de-travail-contre-lecture-H1-2609.19101-v1.tar` (non ouverte) | `0d8de92cccf7530a572662bd976b85967003ac03b85c7b8e64e9b47dbeb0ee8a` |

Les sources de la v2 (v1, sa contre-lecture, N-068 à N-070, index et 39 fichiers du compte 2) sont inchangées ; leurs empreintes sont au journal de la v2.

## 3. Ce que j'ai lu pour la v3, et comment

- La contre-lecture de la v2, en entier (117 lignes). Son archive, extraite dans `v3/archive-cl/` (sous-dossier neuf) ; liste lue ; aucun script exécuté.
- N-067, en entier (145 lignes).
- Pour vérifier les constats : la v1 et la contre-lecture de la v1 (déjà en mémoire de ma v2 : bascule de la v1, l. 527 ; m6 de la contre-lecture, l. 786) pour F ; K-Tr (pièce 3) pour A ; K-T (sections 8, 9) pour B ; K-HC6 (sections 10, 12) pour C ; N-068 (sections 4, 6, 8) pour D ; K-H2 (sections 3, 10, 11) pour G et K ; K-4B1 (section 7) et K-4B2 (section 8) pour I ; K-H6 et K-HC1 pour J ; K-L (section 0) pour Q ; recherche de passages dans deux contre-lectures nommées : celle de K-Tr (l. 204, « avant toute phrase publique ») et celle de K-4B1 (l. 132, Gao, Schulman et Hilton).
- Après le second message du coordinateur (reçu vers 01:28 UTC) : le rapport de confrontation de 2609.19101 à H1 et sa contre-lecture, en entier. Lecteur et contre-lecteur concordent sur le verdict (« occupé en partie », partie cédée), sur « non » déclarable et sur les conditions de passage à « oui » ; la contre-lecture ajoute trois réserves que je porte (vérité terrain du modèle du moniteur, constat A ; agrégation inégale, constat B ; pas de « concentré », constat C) et un troisième voisin à lire (Zhou et collègues, constat K) : je prends partout la lecture la plus prudente. Aucun extrait anglais n'en est repris ; les deux extraits de 2609.19101 viennent du JSON contrôlé de K-Tr.

## 4. Décisions sur les constats A à R

Toutes « corrigé », chacune vérifiée dans la pièce citée (table de la section 2 bis de la synthèse). Deux écarts au texte proposé, motivés :
- **E** : la règle réécrite fait des pièces de la section 5 de la contre-lecture de la v1 une exposition à nommer, non un empêchement ; sinon aucun déclarable de cette contre-lecture (H3, H5, H7, statistique de population, HC1, H2) ne le resterait, contre son propre partage.
- **K et R** : appliquée de la même façon à tous, la condition 4 range H2 (Makins et Oldfield, « à lire en premier ») et la statistique spatio-temporelle (Bonjour, Aggarwal et Bhargava 2022, priorité haute, « pour la composante statistique conjointe de l'énoncé 2 ») en « non » ; la contre-lecture de la v2 les gardait en « oui ». C'est le traitement de T pour (a) et (b) et de L.
- **HC1** reste « oui » : les pièces désignées en priorité par K-HC1 visent le phénomène, cédé, non la composante déclarée ; Gao, Schulman et Hilton (priorité 2 contre le rôle 1, « l'idée même du papier C » par une remarque de portée, sans rang contre une composante de HC1) et 2605.26156, 2606.10159 (priorité haute contre le rôle 1) sont nommés comme exposition. Ce point est discutable ; il est dit.
- **HC3 et les O non jugés** passent de « non » à « non statué » (condition 5), comme HC2.

## 5. Lignes « déclarable » changées depuis la v2

- de « oui » à « non » : H1 (ci-dessous), H2, la statistique spatio-temporelle (énoncé 2 de N-069), T pour (a) et (b), HC6 ;
- de « oui » à « non statué » : HC2 (avec renvoi à N-068, sections 4, 6, 8) ;
- de « non » à « non statué » : HC3, O5, O6, O7, O9, O10, O12, O13, O14, O15, O16, O18, O19, rôle 3 ;
- H1 : de « oui » à « non » (K-H1b : 2609.19101 occupe en partie la partie cédée ; trois voisins à lire avant toute déclaration) ;
- inchangés en « oui », avec exposition et voisins désormais nommés : H3, H5, H7, statistique de population (énoncé 1), HC1, T pour (c) à (f).

## 6. Contrôle des extraits anglais

`controle_guillemets_v3.py` exige que chaque extrait anglais entre « » figure dans une citation contrôlée d'un JSON du compte 2 **et sur le PDF dont parle la phrase** (table `ATTENDU`, remplie en lisant chaque phrase). Essai : un extrait juste passe, un extrait altéré est refusé (`scripts/essai_v3_resultat.txt`). Résultat final : 12 extraits anglais, 0 erreur (335 passages entre guillemets). Le nom d'atelier contrôlé en v2 contre un autre PDF est retiré des guillemets (constat O). `citations-synthese-v3.json` donne pour chaque extrait le PDF, son empreinte, la page et le JSON source avec son empreinte.

## 7. Ce que je n'ai pas fait

Aucun PDF ouvert. N-064, N-065 et le programme non lus. Archives des contre-lectures du compte 2 non ouvertes. Je n'ai pas contre-lu la v3.

## 8. Refus et ouvertures

Aucun refus. Aucune ouverture fautive.

## 9. Archive

`fichiers-de-travail-synthese-niveau3-v3.tar` : `citations-synthese-v3.json`, `controle-guillemets-v3-final.txt`, `scripts/` (contrôleur v3, essai et son résultat ; scripts de la v2 pour le pool), journal de travail v3, notes de lecture (celles de la v2, nom de méthode remplacé par son identifiant). Sans PDF, sans texte extrait, sans le recueil des 1 266 citations (régénérable par `pool_citations.py` à partir des archives du compte 2).
