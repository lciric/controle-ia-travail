# Pièce des empreintes du code d'analyse du versant honnête, version 6 — pour la ligne « Commit du code d'analyse » de la prévision

2026-11-24T16:32Z (`date -u`). Session « dossier de l'entretien », reprise (Opus 5.5). Classe B (instrument). Branche `dossier-entretien/reprise-01qi7-v1`.

**Commit à inscrire** : `8e0746346a21deedd9274e173a3dabc1f7dc41f1` (contient le code v6, ses essais et le complément 1 aux essais).

| pièce | chemin | sha256 |
|---|---|---|
| code d'analyse v6 | `src/controle_ia/versant_honnete_v6.py` | `1cea69307d2a1975139f2888fd5e7a45dd9bf906e3a98892cb8ba08ebdedb3d4` |
| essais v6 | `tests/test_versant_honnete_v6.py` | `ab622c0369459c6fd925c15485935b6761ad5e94cc79eeba7ee9e3ef9ebdfb20` |
| complément 1 aux essais | `tests/test_versant_honnete_v6_complement_1.py` | `9716ba89c0eb7ba9272103e33dce1054e8b90dc1c9680e3183a0aec2b0830240` |
| liste des essais (96, collectés par pytest) | `docs/notes/dossier-entretien-2026-12-01-v1/liste-essais-code-versant-honnete-v6.txt` | `36411aeb8812243bc980e25347a2907d85f6dd0babecf028869660e78d042837` |
| rapports de Sonnet sur les versions 1 à 5 | `docs/notes/dossier-entretien-2026-12-01-v1/rapports-verification-code-versant-honnete-sonnet-v1.md` | `a41e3e78a45c4113ba282bbccb50accb0e4f31a4fa09f46b9e75258edb0f540c` |

**Chaîne de contre-lecture** : auteur Opus 5.5 aveugle (v1 à v3, v5, v6) ; v4 écrite par cette session (refus d'une étape 0 non tenue). Contre-lecteur Claude Sonnet, aveugle, sur chaque version : v1 « conforme sous corrections » ; v2 à v5 « corrections vérifiées » (32 mutations tuées sur la v5) ; v6 « corrections vérifiées sous une réserve mineure » (16:30Z ; mutations tuées : fichier ignoré, domaines, empreinte, obligation hors essai, sortie ; survivante : borne haute de centre_min_actions), réserve levée par le complément 1 (essai 61 et 600 refusés, 60 accepté ; la mutation « <= 60 porté à 600 » est tuée). Rapport v6 : recopié ci-dessous.

> Vérification v6 (Sonnet, 16:30Z) : diff v5 → v6 limité aux réglages du centre ; aucune régression (95 essais) ; aucun autre chemin de lecture réelle ne construit Parametres sans les réglages (main est le seul ; le refus des réglages absents précède le chargement des tables et des entrées) ; essais : cas sain (10 ; tâche à 9 actions sans centre) et artefacts (clé manquante ou en trop, empreinte fausse, fichier absent ou introuvable, valeurs hors domaine) ; mutations tuées : fichier ignoré, domaine bas 1 → 0, domaine « unité » élargi, empreinte non contrôlée, obligation hors --reduit retirée, sortie sans réglages ; survivante : borne 60 → 600. Lu : diff v5 → v6, main de la v6, essais de réglages ; aucune donnée du programme.

**Usage en lecture réelle** : `python -m controle_ia.versant_honnete_v6 analyser … --centre <réglages.json> --centre-sha256 <empreinte> --tables-etape0 <tables> --tables-sha256 <empreinte>` ; le JSON des réglages porte exactement : centre_statistique, centre_echelle, centre_unite, centre_mediane_paire, centre_min_actions (10 selon la mère, lecture littérale de la base).
