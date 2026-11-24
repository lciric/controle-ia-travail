# Passation — fille 2 du papier D, 2026-11-24T15:45Z

Session `session_01Qi7Gr5wToiFFpJSjFxt3BZ`, Opus 5.5, sur la branche `papier-d/evasion-post-entrainement-v1`. Les passations de 09:55 et de 10:30 restent valables pour ce qu'elles couvrent.

Dossier de publication : P = `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/`.

## Fait depuis 10:30

### 1. Contre-lectures des chantiers 1 à 3, expérience de seuil, relecture par Fable
Tout est versé (voir les commits de la branche jusqu'à `5f725273`).
- Expérience de seuil du théorème de l'audit tiré au hasard :
  - préenregistrement `papiers/D/prereg/prereg-seuil-chantier3-v3.md` et son erratum 1 ;
  - course sur processeur, verdict du lecteur neuf dans la requête de fusion 105 ;
  - aucune réfutation ; garantie tenue en 137 points sur 138 ; marge conservatrice d'un facteur 1,75 à 3,56 ; 2 à 57 % d'audits réservés en trop, médiane 10,5 %.
- Remarque sur la marge (décision de Lazar R-5284, volet b) : `papiers/D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-4.tex`. Elle est dans le brouillon de la section, **pas dans le manuscrit de base**.

### 2. Propositions du collisionneur retenues par la mère
- **Condition d'inversion** : elle était déjà au manuscrit (théorème 1, point 4(c)).
- **Défaut réel trouvé** : la normalisation de la récompense n'est pas libre sous pénalité ; sous pénalité, c'est l'écart R0 + C qui compte. Les algorithmes qui réalisent chaque opérateur n'étaient pas nommés.
- **Correctifs du manuscrit** :
  - correctif 2 (`5551d38c`) ;
  - contre-lecture par Sonnet 5.5, effort élevé : accepté avec 8 corrections ;
  - correctif 3 avec un script renforcé (`360b01ed`) ;
  - vérification des corrections par le même contre-lecteur : acceptées ;
  - erratum 1 du correctif 3 (`53834c57`).
- **Base de diffusion proposée** : `P/manuscrit-arxiv/main-v4-correctif-3-erratum-1.tex` (25d094dd…) et son PDF (a4fbb499…).
- **Scripts** : `P/verifier_correctif_3_v1.py`, sortie `P/exemples-verifies-correctif-3-v1.json`, aucun défaut.
- **Billet et page de dépôt**, avec la phrase sur la normalisation : `P/billet-…-en-v4-correctif-3.md` et `P/github-page/README-v4-correctif-3.md`.
- **Audits** : `papiers/D/audits/contre-lecture-sonnet-correctif-2-manuscrit-v4-v1.md` et `papiers/D/audits/verification-sonnet-corrections-correctif-3-manuscrit-v4-v1.md`.
- **Test du code sur un cas exact** : déjà fait pour l'expérience de seuil, témoin `papiers/D/resultats/seuil-v1/essai-gardes-bancs-temoins-v3.txt`.

### 3. Programme du papier D, v3 (mot de Lazar relayé par la mère)
Dossier `P/programme-v3/`, commits `115faff4` et `94e69d40`.
- Chaîne suivie :
  - Fable 5.2, effort élevé, écrit la v3 ;
  - un Opus 5.5 neuf, effort élevé, la contre-lit : accepté avec 13 corrections ;
  - Fable écrit le correctif 1 ;
  - le même Opus vérifie : acceptées ;
  - Fable écrit l'erratum 1.
- **Pièce qui fait foi** : `strategie-cibles-et-feuille-de-route-publication-papier-d-v3-correctif-1.md` (67894f0b…), avec son erratum 1 (045d7b7e…).
- **Note pour Lazar** : `note-changements-programme-papier-d-v2-vers-v3-v1.md` et `.pdf` (5f98a01f…).

## Reste
- **Décisions de Lazar**, toutes à transmettre par la mère :
  - (a) atelier non archivistique d'abord ;
  - (b) banc de code à niches de triche, sur devis ;
  - (c) l'accord sur le dépôt public compagnon tient-il tel quel ;
  - la restriction « si la cible l'exige » pour le théorème resserré de la marge ;
  - le sens de « au manuscrit » : faut-il faire entrer la section sur le budget d'audit dans la base ?
- **Calendrier d'avant le 1er décembre** (section 7.2 du programme), neuf tâches sans dépense :
  - lire les appels des cibles et l'antériorité sur PDF ;
  - corriger la référence de Bartók et al. dans un nouveau correctif du manuscrit ;
  - vérifier le billet et la page de dépôt du correctif 3 ;
  - vérifier les correctifs 3 et 4 de la section sur le budget d'audit ;
  - transmettre à la fille 1 les propositions qui touchent son préenregistrement.
- **Reporté après le 1er décembre** : Lean, l'arbre exact à quatre bras, le théorème resserré de la marge (option a de R-5284), tout calcul payant.

## Réserves
- Le billet et la page de dépôt du correctif 3 n'ont pas été contre-lus.
- La remarque sur la marge n'est pas dans le manuscrit de base.
- Les modèles du collisionneur n'ont vu qu'un résumé du manuscrit ; les règles de conférence et les coûts viennent de mémoire de modèle.
- Les auteurs et les contre-lecteurs sont tous de la même maison.

## Prochaine action
Attendre la mère et les décisions de Lazar. Ensuite, sur son accord : le correctif du manuscrit de la tâche 5 du calendrier, puis la vérification du billet et de la page de dépôt (tâche 6).

## Dépenses et machines
Aucune dépense ; aucune instance ni serveur ; rien diffusé ni publié.
