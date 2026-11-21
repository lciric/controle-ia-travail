# Passation courte du développeur de la seconde passe — sous-étapes 3 et 4 closes (lecture côté entrée, comparaisons entre lentilles) — v1

2026-11-21 (UTC), branche `claude/brave-galileo-jhp684`. Suit la passation de la sous-étape 2 (`205150b8…`).

## Fait
- `lecture_entree_v1.py` (`43f1398e53f9bcd265b11161a5118f6d04a8d6b17f13cf5db4b1f7c5ed85c099`) : lecture par notre S (covecteur à gauche,
  normalisation, plongements centrés), référence « plongements seuls » (même code, K = identité), chemin indépendant en double
  précision, garde de la fonction de lecture de notre S (trois artefacts ; (iii) « sans objet » si les plongements sont liés) et de
  notre R (celle de la première passe, telle quelle), garde du rapport à ε étendue.
- `comparaisons_lentilles_v1.py` (`9a881a965e75b439c4d66d9f25dfbb81661564242114efa21c64b620857100a6`) : recouvrements, p,
  médiane, corrélations, libellés, « non calculable », appariement des nuls par empreinte, calibration du recouvrement (borne haute seule).
- `tests/test_lentilles_sondes_bbis_seconde_passe_lecture_comparaisons_v1.py` (`665da819ed6820152447bf4931fcc0927fb0162b93c58089fc987f92db7f8960`) :
  44 essais. Les trois fichiers d'essais de la seconde passe ensemble : 226 essais, verts.
- Essai des essais : 10 sur 10 et 12 sur 13 (une équivalente).
- Message de la session des lentilles reçu et suivi : noms `corpus_pagine_v1.py`, `lanceur_v8.py` et leur fichier d'essais non
  employés ; `montage_v1.cibles_corpus` ne sera pas réemployé tel quel (nœud N-dev-1).

## Reste
Sous-étapes 5 à 7. **Prochaine sous-étape exacte** : sous-étape 5, `reproduction_v1` (tables de la première passe ouvertes sur
l'empreinte de leur ligne ; comparaison des libellés et des vingt premiers jetons ; empreintes de E-1 et de E-2 entre les passes ;
première passe lancée et non achevée), `audits_v2` (déclencheurs de la seconde passe), `phrases_v2` (phrase de tête, six formes
des phrases permises, verdict d'ensemble, phrases de notre S et des comparaisons, refus des paraphrases interdites) ; puis la
sous-étape 6 : `montage_v2` et `lanceur_seconde_passe_v1`.

## Expositions, instances
Aucune exposition neuve. Aucune machine, aucune dépense, aucun téléchargement de modèle, de lentille ni de corpus ; aucune clé lue.
