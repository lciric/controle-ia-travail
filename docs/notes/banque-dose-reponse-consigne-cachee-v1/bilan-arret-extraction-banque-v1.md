# Bilan d'arrêt — extraction de la banque de 64 tâches neuves (course de dose–réponse de l'organisme à consigne cachée) — v1

Pièce de classe C, 2026-11-24, session fille d'extraction (mère : session_01Qi7Gr3Ggccg85kjmP654WC). Mandat : `docs/notes/conception-g0-criteres-2-3-v1/mandat-extraction-banque-64-taches-neuves-v1.md` (`61f59ec0…`). Texte qui fait foi : `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (`2263c5c4…`, sur `main`).

## Verdict

**Banque non formée.** La procédure d'extraction scellée s'est arrêtée à son seuil de contre-vérification. Sur 16 papiers de l'échantillon, 12 sont en échec ; le seuil est de 4. Les 12 échecs ont tous le même motif : « l'énoncé révèle ce que l'invite H.9 interdit ». L'audit R4 par quatre contre-vérificateurs neufs confirme les 4 échecs audités (accord 4 sur 4). La suite écrite par la procédure (section 6) est une extraction entière sous une version 2 (invite corrigée). C'est un changement de règle, que le mandat interdit : **arrêt, nœud de Lazar**. Aucune ligne `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` n'est proposée.

## Ce qui est fait et tient

| étape | résultat | pièce (empreinte) |
|---|---|---|
| Code porté sous noms neufs (rang 125, cible 64, marge 16), classe B | contre-lu par un autre modèle (13 remarques, toutes traitées), vérifié « utilisable en l'état » ; erratum 1 (lecture tronquée reprise) | `corpus_arxiv_banque_dose_reponse_v1.py`, `extraire_banque_dose_reponse_v1.py`, `tests/test_banque_dose_reponse_v1.py` (34 essais) ; rapports dans ce dossier |
| Sélection, rangs 125 à 233 | 109 papiers examinés, 80 gardés, 29 exclus par la règle (28 « pandoc a échoué », 1 « texte converti hors bornes ») ; tirage relu et rejoué à l'identique, aucune graine | `runs/20261124-130703-banque-dose-reponse-selection/manifeste.json` (`47840115…`), `diag/…-selection/corpus.json` (`536e0e50…`) |
| Run de sélection interrompu (panne réseau, lecture tronquée) | versé, scellé ; 94 fiches identiques au run relancé (sort et empreinte de texte) | `diag/20261124-125253-banque-dose-reponse-selection-interrompu/` |
| Extraction, tentative 1 (80 papiers) | 79 valides, 1 invalide (sorties absentes : trois arrêts d'un classifieur de sécurité), 1 « theory_only », 1 alerte lexicale | `runs/20261124-131623-banque-dose-reponse-extraction/manifeste.json` (`b9c3dc47…`), `diag/…-extraction/validation-tentative-1.json` |
| Tentative 2 (papier 2602.07588v2) | valide au deuxième lancement (premier lancement arrêté par le classifieur) | `diag/…-extraction/validation-tentative-2.json` |
| Échantillon (graine de l'extraction des 96, contrôlée égale) | 16 papiers | `diag/…-extraction/echantillon-contre-verification.json` |
| Ronde « échantillon » | 12 échecs sur 16, tous « énoncé révélateur » ; cibles défectueuses 2 sur 182 ; classification : 1 désaccord de type de papier (d'un cran, sans échec), 1 domaine discutable | `diag/…-extraction/contre-verification-ronde-1.json` (`cfb0a5d5…`) |
| Ronde « théorie » (2510.15814v2) | « theory_only » confirmé | `contre-verification-ronde-2.json` |
| Arrêt de seuil, puis audit R4 côté sale | 4 échecs confirmés sur 4 ; cible défectueuse 1 sur 48 | `arret-seuil-contre-verification.json` (`da375b9b…`), `accord-audit-cote-sale.json` (`b2ea225a…`), `contre-verification-ronde-3.json` |

Sorties, avis et retours (texte des papiers) : `donnees/20261124-131623-banque-dose-reponse-extraction/`, versés de force au dépôt privé comme pour l'extraction des 96 (à purger avant toute publication). Contrôles mécaniques (anomalies, motifs, compteurs) seuls lus par la session ; une exposition involontaire est déclarée dans la liste « qui a lu quoi » de ce dossier (ligne 11).

## Écarts déclarés

1. **Modèle des sous-agents** : le manifeste de l'extraction des 96 n'en nomme aucun (procédure, section 7). Les sous-agents ont été lancés comme alors, sans choix de modèle, et servis par le modèle de cette session, que le compte rendu à la mère nomme hors du dépôt.
2. **Marge de 16** : la sélection garde 80 papiers. Les 16 de la marge sont extraits dès la tentative 1 et entrent dans le vivier de l'échantillon (permutation sur 80, même graine). Au-delà de 16 exclusions, c'est un nœud de Lazar (suite du tirage existant).
3. **Arrêt sur trois sources indisponibles d'affilée** : c'est une garde de chaîne, non une règle d'exclusion ; elle n'a pas servi.
4. **Erratum 1** : une lecture tronquée par le réseau est reprise par les quatre tentatives du code scellé, au lieu d'arrêter brutalement.
5. **Classifieur de sécurité** : le papier 2602.07588v2 (rang 171, dans les 64 premiers gardés) a été arrêté quatre fois avant toute écriture (trois lancements à la tentative 1, un à la tentative 2), puis extrait au cinquième. Ces arrêts sont traités par la procédure comme des pannes de sous-agent (relances comptées). C'est un faux échec au sens de la règle sur les pannes ; il n'a pas coûté le papier.
6. **Python 3.13** ici, contre 3.11 en octobre ; numpy, scipy et la roue de pandoc (3.9, empreinte vérifiée) sont identiques.

## Nœud de Lazar

**Décision :** comment former la banque, alors que la procédure scellée s'arrête sur l'énoncé.

**Enjeu :** sans banque scellée, la course de dose–réponse ne se crée pas (liste d'arrêt du texte scellé).

**Ce qui n'est pas su :** l'écart avec l'extraction des 96, qui avait passé son seuil, peut venir de l'extracteur d'aujourd'hui, qui écrirait des énoncés plus révélateurs. Il peut aussi venir du contre-vérificateur d'aujourd'hui, qui serait plus strict. L'audit par le même modèle ne sépare pas les deux.

**Options :**
- (a) **Rejeu diagnostique d'abord** : faire juger par le contre-vérificateur d'aujourd'hui 16 énoncés de la banque initiale (même consigne). Cela sépare la dérive de l'extracteur de celle du juge.
  - Avantage : coût faible (16 sous-agents, aucune dépense en dollars) ; le choix entre (b) et (c) se fait ensuite sur un fait.
  - Inconvénient : il sort du mandat, et le diagnostic exige un nouvel accord.
- (b) **Version 2 de l'invite d'enveloppe des énoncés**, puis extraction entière refaite sur les 80 papiers. C'est la suite que la procédure écrit.
  - Avantage : c'est la voie prévue.
  - Inconvénients : changement de règle, à concevoir par Fable puis à contre-lire ; environ 100 sous-agents ; la banque ne serait plus extraite à l'identique de la banque initiale.
- (c) **Extraction refaite sous le modèle de l'extraction d'octobre**, s'il est encore servi.
  - Avantage : aucune règle ne change.
  - Inconvénients : changement de modèle, qui demande un GO ; ce modèle n'est ni nommé dans le dépôt ni forcément disponible.

**Recommandation :** (a), puis (b) ou (c) selon son résultat. Confiance moyenne.

**Défaut sous 48 heures :** aucun. C'est un nœud d'arrêt, la session attend le mot de Lazar.
