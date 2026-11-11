# Index du bras d'étude des déplacements de loi (bras d'attaque) — v3

Tenu par la session-dépôt (gardien). **Aucun contenu** : seulement l'existence, le chemin, l'empreinte et l'intégrité des pièces.
Les versions v1 (`4a591803…`) et v2 (`7966d004…`) restent telles quelles (R12) ; la v3 les reprend par renvoi et ajoute les
lignes du 10 novembre 2026.

## Lignes reprises

- BA-001 (29 octobre) : voir la v1. Ligne de la v2 sur les deux fichiers vivants de `donnees/ideation-pilier-attaque-v1` :
  voir la v2.

## Lignes ajoutées le 10 novembre 2026 (relevé vers 10:31 UTC)

### BA-002 — session « attaquant informé » (`session_01QPDgKjN3jeeUyZP2mnkDNK`)

- **Branche** : `claude/compassionate-meitner-d4ryyk`, tête `8549ae01`, 24 commits propres depuis la base `483712e7`.
- **Pièces scellées relevées** : 93, toutes conformes à leur compagnon (empreinte du compagnon égale à l'empreinte recalculée de
  la cible, au commit de la tête) ; liste complète, chemin et empreinte courte : `registres/index-bras-attaque-v3-pieces-session-attaquant.txt`.
- **Préenregistrement de la règle du bras (scellement 1 de la règle du jeu)** : `prereg/bras-attaque-regle-v1.md`,
  `88418df0…`, scellé à 10:21:49 UTC (commit `86549bb6`, message : « après trois contre-lectures ») ; brouillons 1 à 3 dans
  `brouillons/` ; contre-lectures relevées par leur nom : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-regle-bras-v1.md`,
  `docs/notes/integration-bras-attaque-v1/contre-lecture-2-regle-bras-v1.md`, `…/contre-lecture-3-regle-bras-v1.md`.
  **Empreinte à déposer chez le tiers** (règle du jeu scellée, `527a3e7e…`, scellement 1) : voir le manifeste v3.
- **Courses du 10 novembre** (manifestes dans `runs/`, sorties dans `diag/`, toutes conformes) :
  `20261110-085836-bras-puissance-seuil-v1` (commit `4d5e0948`, 09:03 UTC) ; `20261110-093836-bras-verdicts-v1` (`90993b82`,
  09:43) ; `20261110-101442-bras-verdicts-v2` (`861e25e9`, 10:18). Nature déclarée par leurs noms : dimensionnement du régime
  des verdicts comptés. Le gardien ne lit pas leurs sorties.
- **Code** : `src/controle_ia/bras_attaque/` (`__init__.py`, `puissance_seuil_v1.py`, `verdicts_v1.py`, `verdicts_v2.py`),
  `scripts/bras_attaque_puissance_seuil_v1.py`, `scripts/bras_attaque_verdicts_v1.py`, `scripts/bras_attaque_verdicts_v2.py`
  et leurs essais.
- **Autres dossiers** : antériorité du bras (2 notes, 14 sources), procédures publiées de l'échelon des verdicts comptés
  (2 notes, 35 sources), reproduction de l'attaque publiée et son témoin (10 notes, 1 source ; préenregistrement du témoin en
  brouillon, trois contre-lectures relevées par leur nom), plan de vérification externe (3), intégration (2), récapitulatif pour
  l'entretien (13), courbe dose-réponse de l'organisme (1).
- **Ce que le gardien n'a pas fait** : lire un contenu ; juger un résultat ; vérifier que les courses sont dans le mandat de la
  session (c'est à Lazar, qui l'a étendu dans cette session).
