# Journal de la synthèse de l'état de l'art vérifié de niveau 3 — v6

Écrit le 2026-11-14, de 07:41:16 UTC à 07:46:52 UTC (heures relevées par `date -u`). Auteur : modèle A (auteur des v2 à v5) ; contre-lecteur de la v5 : modèle B ; A ≠ B. Compagnon de `etat-de-l-art-verifie-niveau3-v6.md`. Mandat : message de la coordination après la contre-lecture de la v5 (l'intégrer sous un nom neuf, sans toucher la v5 ; porter le mot de Lazar sur L1, inscrit ; juger le constat F sur N-003/N-004).

## 1. Consignes tenues

Consigne commune du compte 2 (`cb0623c4…`) et interdits communs v2, sans exception : aucune commande git, aucun réseau, aucun appel de modèle ; fichiers nommés seulement ; rien de T0.7, de 7a ni de 7b ; rien sous `registres/`, `diag/`, `runs/`, `donnees/` ; aucune suppression par motif ; aucun nom de modèle du programme. Avant d'écrire : `ls` du seul dossier `docs/etat-de-l-art/`, aucun fichier v6 n'existait. Travail versé au fil de l'eau dans le sous-dossier neuf `v6/`.

## 2. Sources nouvelles et empreintes (recalculées, égales à leurs compagnons)

| fichier | sha256 |
|---|---|
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v5.md` (remplacé pour la lecture) | `303c5f2f6d7e52d8cd7e6aefa4f44577474903f6c7477069244059c468af018b` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v5-journal.md` | `6cfe33e3ea2f4432194a455f7b121024e7a5608b3d2acb02216065458de7b541` |
| `docs/etat-de-l-art/fichiers-de-travail-synthese-niveau3-v5.tar` | `90dbb64ead38b1f4b4b38e061cc7fa818b5a496e90ef92eb043a24ea448ed636` |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v5-contre-lecture-v1.md` | `6188e80040468b32ab97ab28f7c101e44510d365dc07ef7c750c44cc838f17cf` |
| `docs/decisions/decision-N-003-N-004-v1.md` | `cc1be39369bc4dae9b3166c513d783b4744c62d839951f047a44396aa3a81a5a` |

## 3. Ce que j'ai lu pour la v6

- La contre-lecture de la v5, en entier (99 lignes).
- N-003/N-004, en entier (87 lignes), pour le constat F.
- Relus pour B, C, E : `rapport-L-voisins-v2.md`, sections 0, 2 et 3 ; `rapport-L-ker2007-v2.md`, sections 0 à 3 (les sections 5 à 7 l'avaient été pour la v5). Pour D : la table des écarts de `rapport-H1-2609.19101-v2.md`. Pour G : `rapport-HC4-2609.15994-v2.md`, section 3.2.
- Le mot de Lazar sur L1 (inscrit, R-2657, C2-0072) et l'état du mot sur H6 (en attente, examiné, R-2657) viennent du message de la coordination ; je n'ai lu aucun registre.

## 4. Décisions A à M (section 2 quinquies de la synthèse)

Toutes « corrigé ». Pour B, le texte proposé par la contre-lecture (« étaler ne sert l'attaquant que face à la moyenne ») est inexact au regard de K-Lv (la moyenne est indifférente ; le rapport de vraisemblance à petite charge pousse à étaler) : j'ai écrit la version des rapports. R7 de la section 2 quater est mis à jour (mot inscrit), décision « réserve maintenue » pour M4 ; R1 renvoie aussi à la section 11.3.

## 5. Constat F, en une ligne

**N-003/N-004 range « invariances exactes » dans la seule revendication de L (section 2, l. 75 ; L1 « exacte », L4 « exactement invariante ») ; celle de T (section 1, l. 45-49) ne l'emploie pas : la zone touchée par Ker est celle de L seul, aucun doute ne reste sur ce rattachement, et T (c) à (f) reste « oui », avec la mention que Ker 2006 et 2007 n'ont été lus que contre L.**

## 6. Lignes « déclarable »

Aucune ne change de valeur. « Oui » : H3, H5, H7, T pour (c) à (f). L : « non » (condition 4), la condition 2 étant levée pour L1 par le mot de Lazar.

## 7. Contrôle des extraits anglais

`controle_guillemets_v3.py`, inchangé, relancé sur la v6 : 454 passages entre guillemets, 12 extraits anglais, 0 erreur. Aucun extrait anglais nouveau. Liste dans `citations-synthese-v6.json`.

## 8. Ce que je n'ai pas fait

Aucun PDF ouvert ; aucune archive de rapport ouverte ; rapports du niveau 3 non rouverts ; registres non lus. Je n'ai pas contre-lu la v6.

## 9. Refus et ouvertures

Aucun refus. Aucune ouverture fautive.

## 10. Archive

`fichiers-de-travail-synthese-niveau3-v6.tar` : `citations-synthese-v6.json`, `controle-guillemets-v6-final.txt`, `scripts/`, `parties/` (parties de la v6), journal de travail v6. Sans PDF, sans texte extrait, sans le recueil de citations.
