# Rapport du développeur — code de la course de l'organisme retenu, version 5 (P1) — v3

Date : 2026-11-22. Pièce d'instrument (classe B). Même développeur (Claude Opus 5.5), même cadre. Ce rapport complète les v1 et v2, intactes. Il traite la contre-lecture `contre-lecture-code-course-v5-cl1.md`, dont le verdict est « course autorisable après corrections ». Les correctifs 0014 à 0018 ne sont pas changés. Rien poussé, rien dépensé, aucune machine, aucun modèle téléchargé.

- **Tête : `997bed6a18397bf5a7c4dab15fbd080d59894b7a`, arbre `cd2366af52f1c05e2773a7daa0755d97703495cc`.**
- Correctif `0019-…patch` (`git format-patch --start-number 19`), à appliquer après 0018.

## Table de traitement

| remarque | traitement | où | essais |
|---|---|---|---|
| **M1**, second passage refusé sur le même disque seulement | **corrigé**, deux étages. (1) `phase_course`, toutes ses gardes passées, écrit, scelle et pousse `diag/<étalonnage>/course-engagee-iib-v5.json` (run, instant, oracle, tours prévus) avant le premier tour ; `exiger_course_non_jouee` refuse tout dossier qui le porte, donc aussi une course morte avant son premier tour et un clone de la branche sur une machine neuve. (2) L'amorce de la course, changement (c6), fonction `engager_course` : `git ls-remote --exit-code origin refs/heads/essai/iib-course-engagee-<étalonnage>`. Code 0 : refus. Code 2 : la référence est poussée (`HEAD:…`) avant la branche et avant l'installation. Autre code, ou poussée refusée : refus. | `lanceur_v5.py` (`ENGAGEMENT`, `exiger_course_non_jouee`, `phase_course` reçoit `run`) ; `scripts/amorce_instance_iib_course_v5.sh` (c6) | engagement scellé, poussé avant le tour 1 (ordre des commits), relu et refusé depuis un clone neuf (cas sain et artefact) ; dossier vide permis, dossier qui ne porte que le témoin refusé ; `engager_course` joué tel qu'écrit contre une origine nue (absente : poussée ; présente : refus, rien de plus) ; différences de l'amorce bornées à 5 lignes retirées et 18 ajoutées hors commentaires ; répétition locale : une seconde machine neuve, sous une branche neuve, est refusée (« course déjà engagée »), aucune branche poussée |
| **m1**, identifiants de l'étalonnage absents ou incomplets | **corrigé** : `exiger_identifiants_de_l_etalonnage`. En mode réel, refus si aucun fichier, si le résumé scellé de l'étalonnage manque, ou si le nombre de fichiers diffère de ses `lots`. Appelée avant le manifeste de la course. | `lanceur_v5.py` | 0 fichier, 2 pour 3, résumé absent : refus ; 3 pour 3 : permis ; mode jouet : rendus tels quels |
| **m2**, délai de consignation | **corrigé** : 3 600 s (le pire du script est de 3 375 s). | `versement_v5.py` | inchangés (l'essai du délai le remplace par 2 s) |
| **m3**, saut dans l'essai neuf de 0018 | **corrigé** : `assert course["conditions"]["issue"] in ("N", "P")`. | `tests/test_iib_distillation_bout_en_bout_v5.py` | — |
| **m4**, coût de la seconde location | **pour l'ordre, non codé** : il doit citer environ 2,0 USD attendus et environ 6,5 USD au pire (devis, l. 55). | — | — |

## Nombres attendus
- Liste figée v6 (étalonnage) : **294** (`ATTENDUS = 294` dans la répétition).
- Liste de la course (`tests-cibles-iib-course-v5-v1.txt`), sur une machine qui a torch : **296**, donc `TESTS_ATTENDUS=296` pour l'ordre de la course. Rejouée sur ce poste, dans l'environnement à part qui a torch : **296 passed** en 12 min 3 s (`sortie-essais-p1-v3.txt`).

## Ce qui reste ouvert (inchangé, voir v1 et v2, et la contre-lecture)
- Nœud C1 : une ou deux machines. Pour le code, il faut une machine neuve ; c'est un écart au devis, et le mot de Lazar est nécessaire.
- Confirmation explicite de la lecture « gardée » de la première action (R-4708, le défaut appliqué sans réponse).
- Moteur à torch sur carte : il se joue aux premières minutes de la machine de la course, par la liste de la course.
- Mode réel non éprouvé.
- Ce que l'ordre de la course doit porter :
  - `IIB_AMORCE` ;
  - une branche neuve ;
  - le commit qui porte l'étalonnage et la désignation ;
  - `TESTS_ATTENDUS=296` ;
  - m4 ;
  - la dernière création le 26 novembre.
- C2 n'est pas un nœud, selon la contre-lecture : GO-2026-11-21-70 couvre « étalonnage puis course ».

## Livrables v3
- `0019-…patch` ;
- ce rapport ;
- `sortie-essais-p1-v3.txt` ;
- `sortie-repetition-locale-0019-courte-v1.txt`.

Arbre final : `cd2366af52f1c05e2773a7daa0755d97703495cc`.
