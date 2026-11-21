# Passation courte du développeur de la seconde passe — sous-étape 5 close (reproduction, audits, phrases) — v1

2026-11-21 (UTC), branche `claude/brave-galileo-jhp684`. Suit la passation des sous-étapes 3 et 4 (`d06c6be2…`).

## Fait
- `reproduction_v1.py` (`b2b5881516f86fc478e5e5ccf9e84943901d93ca31179ceef3423ca2d0c7cb44`), `audits_v2.py` (`eb5ac503397255a6f0445afba37291f3700f4e5f4fe7904599ebf207cc51e75c`), `phrases_v2.py` (`1a02343b1a6e1cdd373c2a1199edc6177c2efff47868268c537cf7612b63a8a8`).
- `tests/test_lentilles_sondes_bbis_seconde_passe_phrases_reproduction_v1.py` (`4bd2ab6629589c3bcc28d0149cf27164021888abb8644090e73fa2b0cc23fab8`) : 57 essais, verts.
  Les six phrases permises et la phrase de tête sont comparées, octet pour octet, au texte scellé.
- Essai des essais : 15 sur 15, 8 sur 8, 8 sur 8.
- Lu en entier pour préparer la suite : `lanceur_v7.py`.

## Reste
Sous-étapes 6 et 7. **Prochaine sous-étape exacte** : sous-étape 6, `montage_v2` (plongements ajoutés aux tenseurs gardés, seuil
d'espace de 8 Go, garde par les noms des variables d'environnement, appel de `nos_lentilles_v1`) et `lanceur_seconde_passe_v1`
(montage et calcul des quatre lentilles et des moitiés, horloge de 10 heures, canal des messages d'arrêt de `lanceur_v7` réemployé,
garde du fichier d'arrêt déjà présent, fiche du code `CODE-LENTILLES-BBIS-V2`), bout en bout sur un Llama miniature, une fois par
palier ; puis la sous-étape 7 : table des gardes, conformité point par point, sortie des essais du paquet, empreintes.

## Expositions, instances
Aucune exposition neuve. Aucune machine, aucune dépense, aucun téléchargement de modèle, de lentille ni de corpus ; aucune clé lue.
