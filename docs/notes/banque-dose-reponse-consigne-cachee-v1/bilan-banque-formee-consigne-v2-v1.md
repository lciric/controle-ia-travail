# Bilan — banque de 64 tâches neuves formée sous la consigne d'enveloppe v2 — v1

Pièce de classe C, 2026-11-24, session fille d'extraction (mère : session_01Qi7Gr3Ggccg85kjmP654WC). Mandat : `docs/notes/conception-g0-criteres-2-3-v1/mandat-extraction-banque-64-taches-neuves-v1.md` (`61f59ec0…`). Texte qui fait foi : `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (`2263c5c4…`, sur `main`). Accords : GO-2026-11-24-24 et -25 ; repli (b), version 2 de la consigne d'enveloppe, GO-2026-11-24-27 (« (b) en repli »), relayé par la mère.

## Verdict

**Banque formée et conforme.** Elle compte 64 tâches, du rang 125 au rang 210 du tirage scellé, dans l'ordre du tirage. Aucune ne vient des 96 de la banque initiale (contrôle par programme, identifiants sans suffixe de version). Aucune graine neuve, aucune dépense en dollars. Le contrôle joué ne relève aucun écart.

## Chaîne

| étape | résultat | pièce (empreinte) |
|---|---|---|
| Sélection (inchangée) | rangs 125 à 233 ; 80 papiers gardés, 29 exclus par la règle | `diag/20261124-130703-banque-dose-reponse-selection/corpus.json` (`536e0e50…`) |
| Consigne d'enveloppe v2 (étape 2b : relire l'énoncé contre la liste de H.9) | contre-lue par un autre modèle (« utilisable après corrections », 7 remarques traitées), vérifiée « utilisable en l'état » | `docs/procedures/banque-dose-reponse-consigne-v2/consigne-extracteur-v2.txt` (`44da46b3…`) ; rapports dans ce dossier |
| Essai sur les 16 papiers d'octobre, seuil scellé avant | 1 échec sur 16 (k ≤ 2 : probant) ; il y en avait 10 sous la v1 | `essai-consigne-v2-resultat-v1.md` (`4621f32d…`) |
| Extraction, tentative 1 (80 papiers) | 80 valides, 1 « theory_only », 1 alerte lexicale | `runs/20261124-144844-banque-dose-reponse-extraction-v2/manifeste.json` (`d7408c58…`) |
| Échantillon (graine de l'extraction des 96, contrôlée égale) | 16 papiers | `diag/…-extraction-v2/echantillon-contre-verification.json` |
| Ronde « échantillon » | **3 échecs sur 16** (seuil : plus de 4 arrêtent), tous « énoncé révélateur » ; cibles défectueuses 5 sur 185 ; classification sans désaccord | `contre-verification-ronde-1.json` |
| Ronde « théorie » (2510.15814v2) | « theory_only » confirmé, exclu | `contre-verification-ronde-2.json` |
| Audit R4 | non requis par le code : il y a des échecs, mais sous le seuil | — |
| Reprise, tentative 3 (les 3 papiers en échec) | 3 valides ; contre-vérification : 2 rattrapés, 1 en échec (2510.13328v4, exclu après deux échecs) | `contre-verification-ronde-3.json` |
| Assemblage | 64 tâches de banque, 14 hors banque ; un remplacement (2510.15814v2 remplacé par 2509.22307v2). 2510.13328v4 est exclu sans entrer dans les 64. | `diag/…-extraction-v2/bilan-extraction.json` (`76873c86…`) |
| Fichier des tâches | 64 fiches : questions, cibles, classification, coûts rapportés, empreintes | `donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json` (`0065065b…`) |
| Contrôle joué | 64 exactes, aucune des 96, aucun rang sous 125, rangs dans l'ordre du tirage, `conforme: true`, aucun écart | `diag/…-extraction-v2/controle-banque-joue.json` (`b864a072…`) |

Commit des données de la banque : `e1fe6cea`.

## Écarts déclarés

1. **Consigne d'enveloppe v2**, accordée en repli (b) par Lazar (GO-2026-11-24-27). La v2 ajoute la seule étape 2b et le renvoi de la dernière phrase ; le reste est inchangé : vivier, sélection, contre-vérificateur et sa consigne v1, seuils. La banque n'est donc pas extraite à l'identique de la banque initiale.
2. **Modèle des sous-agents** : le manifeste de l'extraction des 96 n'en nomme aucun. Selon le mot de Lazar relayé par la mère, le modèle d'octobre est celui de cette session. Il est nommé explicitement à l'appel de chaque sous-agent, mais son identifiant n'est pas écrit dans le dépôt (le compte rendu le donne hors du dépôt). L'effort n'est pas fixé à l'appel. Erratum 1 du module v2 (`6e1146fc…`).
3. **Marge de 16** : 80 papiers extraits dès la tentative 1, vivier de l'échantillon sur 80 (même graine).
4. **Classifieur de sécurité**, faux échecs au sens de la règle sur les pannes. Pour 2510.24826v1 et 2602.07588v2, le premier lancement de la tentative 1 a été arrêté avant toute écriture. Le second a abouti. Les deux papiers sont dans la banque. 2602.07588v2 avait déjà été arrêté ainsi lors de l'extraction sous la v1.
5. **Erratum 1 de la sélection** (lecture tronquée reprise) et **Python 3.13** : inchangés depuis le premier bilan.
6. **Run sous la v1 conservé** : `runs/20261124-131623-banque-dose-reponse-extraction/`, arrêté à son seuil, versé et non réemployé.

## Réserves

- **R4.** Sous la v2, les échecs passent de 12 à 3 sur 16 pour l'échantillon de la banque, et de 10 à 1 pour les 16 papiers d'octobre. C'est l'effet visé, mais il reste mesuré par un juge du même modèle que l'extracteur. Le juge est toutefois celui qui faisait échouer la v1. Le code n'a pas requis d'audit (cas intermédiaire).
- **Suite complète des essais** : sous 30 minutes, elle n'a pas abouti dans ce conteneur (arrêt à la limite de durée, sans sortie). Une relance avec arrêt au premier échec tourne ; son résultat ira dans la passation. Les 34 essais de la v1 et les 7 de la v2 passent.

## Ligne de registre proposée (la mère l'inscrit)

`BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` — banque de 64 tâches neuves de la course de dose–réponse de l'organisme à consigne cachée (rangs 125 à 210 du tirage scellé, aucune des 96 initiales) : `donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json`, sha256 `0065065b8958968235f13c48d4e423708fd5aaebb64f8eed6ec553e3c56459e4`, commit `e1fe6cea`, branche `banque/dose-reponse-consigne-cachee-v1`. Contrôle joué conforme : `diag/20261124-144844-banque-dose-reponse-extraction-v2/controle-banque-joue.json` (`b864a072…`). Écarts : consigne d'enveloppe v2 (GO-2026-11-24-27), modèle nommé à l'appel, marge de 16, deux faux échecs du classifieur.
