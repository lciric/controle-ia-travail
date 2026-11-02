# Rapport de rédaction — analyse appariée boîte blanche / boîte noire, brouillon 3 et code v3

Rédacteur : le sous-agent auteur des brouillons 1 et 2 et du code v1 et v2 (Claude, Opus 5.5), le 2026-11-02 entre 00:00 et 00:12 UTC. Aucune donnée de R1, R2 ni R4 lue ; aucune branche `calcul/…` ; aucun commit ; aucune empreinte compagnon ; aucun fichier existant modifié (R12) : le brouillon 2, le code v2 (commit `b621ad69`) et les rapports de contre-lecture restent tels quels. Textes du fournisseur lus (texte seulement) : message n° 246 et préenregistrement R1-R2, en entier ; `LISEZMOI` v2 et préenregistrement R4, passages des formats et de l'ordre de lecture ; empreintes vérifiées sur les objets git locaux du commit `567260c0` (`32339415…`, `80c85a00…`) et sur les copies du contre-lecteur (`75b61a54…`, `f4f8ca28…`).

## Méthode

1. Point de départ : les copies corrigées du contre-lecteur (`cl2-bn/arbre-corrige-v2/` et `copies-corrigees-v2/`, dans le bloc-notes de la session), dont j'ai vérifié les empreintes (égales à celles de sa section I : `4ee514b8…`, `cdd5dc73…`, `a17e01fe…`, `af08d07f…`, essais `5d0787aa…`). J'ai relu chacun des 101 remplacements dans le rapport et dans le diff du code (copie corrigée contre code v2 commité) avant de les reprendre.
2. Renommage mécanique v2 → v3 (modules, fonctions, alias `C2` → `C3`, chaînes de version, format de la fiche, nom de sortie) : `renommer.py` du bloc-notes ; trois commentaires où « C2 » désignait la correction C2 de la contre-lecture 1 ont été remis à la main.
3. `evaluation_v3.py` : copie de `evaluation_v2.py` sans changement de calcul, pour que la version 3 ne charge aucun module v2 (fermeture des importations de `lecture_v3` : exactement les 25 modules de la liste fermée, 12 du paquet et 13 gelés).
4. Changements de l'auteur, au-delà des remplacements du contre-lecteur, listés plus bas.

## Comparaison avec les empreintes attendues par le contre-lecteur

Les noms changent (v3), donc les empreintes aussi. Comparaison faite après **renommage inverse** (v3 → v2) de mes fichiers, contre ses copies corrigées :

| fichier v3 | empreinte | renommé en v2, comparé à la copie corrigée | différences, toutes voulues |
|---|---|---|---|
| `constantes_v3.py` | `6e7684acb7a7a520b926acc9315fd85db10d7f7b14d4cb8895986f577a3a33c4` | ≠ `4ee514b8…` | docstring ; `VERSIONS_EXIGEES` (S2) ajouté aux constantes gelées |
| `entrees_v3.py` | `57bcb47ebd056b5d4a4164cd1611dc8405033d4bb37e9c1c4a68681d5febcd2b` | ≠ `cdd5dc73…` | docstring seulement |
| `evaluation_v3.py` | `539a0c7b8c9a8913380833d994875d6814cae1c9f7d3dfe6265b043c8e32ee2d` | ≠ `fc0fbd5e…` (v2, non corrigé) | docstring seulement (copie de v2) |
| `lecture_v3.py` | `dd5dffa4c6441981779aaa07816589666466bd4c8c7fc0d84a3b029fdec1d854` | ≠ `a17e01fe…` | docstring ; S1 (`exiger_premier_passage_v3`) et S2 (`exiger_versions`) ; ligne de portée « lecture secondaire » en tête de l'issue (J7, décision de la session) |
| `rendu_v3.py` | `363cd84f6dc2453e33a896e55192f0605340fdeadd80c44046d08cb0ac8d0371` | ≠ `af08d07f…` | docstring ; même ligne « lecture secondaire » en tête du rendu |
| `tests/test_analyse_blanche_noire_v3.py` | `cb86cf6d9bcb8d505277203467c192547b4ebecfa52b45e50d1c7141892b7ed7` | ≠ `5d0787aa…` | docstring ; noms réels des fichiers jouets (J1) ; essais S1 et S2 dans `test_mode_decisif_v3` ; assertion de la ligne « lecture secondaire » |

Le diff complet (code renommé en v2 contre copies corrigées ; brouillon 3 contre brouillon 2 corrigé, par mots) est dans `differences-brouillon3-code-v3-v1.diff`, à côté de ce rapport.

## Traitement de la contre-lecture 2 (`contre-lecture-2-preenregistrement-analyse-v2.md`, `8697d7b2…`)

| point | traitement |
|---|---|
| D1 | appliqué ; date du brouillon 3 écrite ; la phrase sur R-1086 est rattachée au brouillon 2 |
| D2, D3, D4, D5, D6, D7 | appliqués mot pour mot ; D5 complété : les scripts de fréquence importent `lecture_v2`, non `lecture_v3` (règle de décision identique : D14 n'agit que si (L) est non lu, D16 ne change que la phrase) ; non rejoués sur v3 |
| D8 | appliqué ; le renvoi « section I de son rapport » devient la section « Marqueurs de gabarit » du texte (noms v3) ; deux marqueurs restent |
| D9 (révisée) | appliqué (décision de la session : `R1: null` permis seulement avec `motif_R1` ∈ {`rejeu_non_conforme`, `rejeu_en_echec`}) |
| D10, D11, D12 | appliqués mot pour mot |
| D13 | appliqué, branche « ne pas lire le juge à la dose R4 » (décision de la session) : la fiche refuse un `R4.juge` non nul |
| D14, D15, D16, D17, D18 | appliqués mot pour mot |
| J1, J2, J3, J4, J6 | appliqués mot pour mot ; J1 aussi dans les essais (noms réels des fichiers jouets) |
| J5 | sans objet (traité par D9, J2, D17) |
| J7 | section « Concordance avec le préenregistrement R1-R2 du fournisseur » : les cinq écarts du contre-lecteur, gardés ; **recommandation remplacée par la décision de la session** : l'analyse du fournisseur, scellée la première, est la lecture principale ; celle-ci est secondaire (diagnostic, N-026, hors porte) ; les deux sont rapportées en entier quel qu'en soit le signe ; aucune citation externe ne cite l'une sans l'autre ; question portée à Lazar comme réserve ; « aligner » ferait une version nouvelle après coup, déclarée. Ajouté : ce texte ne code pas les bras du fournisseur ; vérification de concordance par un lecteur neuf à l'étape 0.g ; ligne « lecture secondaire » écrite par le code en tête de l'issue et du rendu |
| marqueurs de la section I | registre (`5bdcbbb1…`, vérifié par `git show 7b0ef14f:registres/decisions.md`) et `LISEZMOI` v2 (vérifié sur l'objet git du commit `567260c0`) remplis dès le brouillon 3 ; entrée de la contre-lecture 2 écrite ; restent : commit cité, entrée de la contre-lecture 3 |
| S1, S2 | appliqués (code, constantes, essais) |
| S3, S4, S5, S6 | non retenus (motifs dans la section « Contre-lecture » du brouillon 3) |

## Essais

`nice -n 10`, cache de pytest désactivé : v3 seul, **13 réussis** (29,5 s ; 44,6 s sous charge) ; v1, v2 et v3 ensemble, **36 réussis** en 82,2 s (12 + 11 + 13).

## Ce qui reste ouvert

1. J7 : la réserve sur la concordance, portée à Lazar par conv-audit ; et la lecture principale du fournisseur, dont le code d'analyse (bras W, G, J3s, J3g, J8s, C, T, au taux de 1 %) n'existe pas encore : son plan (point 3) l'attribue à conv-audit, hors de ce texte.
2. Contre-lecture 3 courte (différences seulement), puis scellement par l'étape 0.
3. Scripts de fréquence non rejoués sur le code v3 (règle de décision identique, déclaré).
